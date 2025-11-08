#!/usr/bin/env python3
"""
Convert Augustine's Enchiridion HTML files to Typst format.
Preserves italics, line breaks, and converts footnotes to Typst format.
"""

import re
from html.parser import HTMLParser
from pathlib import Path


class FootnoteParser(HTMLParser):
    """Parse the footnotes HTML file."""
    
    def __init__(self):
        super().__init__()
        self.footnotes = {}
        self.current_footnote_id = None
        self.current_footnote_text = []
        self.in_footnote = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'name' and value.startswith('N'):
                    self.current_footnote_id = value
                    self.in_footnote = True
                    self.current_footnote_text = []
                    
    def handle_data(self, data):
        if self.in_footnote:
            text = data.strip()
            if text and text != '-':
                # Normalize quotes in footnotes too - use single apostrophes
                text = text.replace('«', "'").replace('»', "'")
                text = text.replace('"', "'").replace('"', "'")
                text = text.replace('"', "'")
                text = text.replace(''', "'").replace(''', "'")
                # Remove spaces around quotes
                text = re.sub(r"'\s+", "'", text)
                text = re.sub(r"\s+'", "'", text)
                self.current_footnote_text.append(text)
                
    def handle_endtag(self, tag):
        if tag == 'p' and self.in_footnote:
            if self.current_footnote_id and self.current_footnote_text:
                # Join the text parts, handling the format "1 - content"
                full_text = ' '.join(self.current_footnote_text)
                # Remove the leading number if present
                full_text = re.sub(r'^\d+\s*-?\s*', '', full_text)
                # Fix small caps pattern in author names: "L UCANO" -> "LUCANO"
                # Matches single capital letter + space + 4+ capital letters
                # (author names like LUCANO, VIRGILIO, CICERONE, SALLUSTIO)
                full_text = re.sub(r'\b([A-Z])\s+([A-Z]{4,})\b', r'\1\2', full_text)
                self.footnotes[self.current_footnote_id] = full_text.strip()
            self.in_footnote = False
            self.current_footnote_id = None
            self.current_footnote_text = []


class EnchiridionParser(HTMLParser):
    """Parse the main body HTML file."""
    
    def __init__(self, footnotes_dict):
        super().__init__()
        self.footnotes = footnotes_dict
        self.output = []
        self.current_text = []
        self.in_paragraph = False
        self.in_italic = False
        self.in_bold = False
        self.in_heading = False
        self.in_small_font = False  # Track <font size="2"> for headings
        self.skip_next_data = False
        self.in_script = False
        self.in_style = False
        
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'head'):
            self.in_script = True
            return
        
        # Check for <font size="2"> which indicates a heading paragraph
        if tag == 'font':
            for attr, value in attrs:
                if attr == 'size' and value == '2':
                    self.in_small_font = True
            
        if tag == 'p':
            self.in_paragraph = True
            # If we're in a small font, this paragraph is a heading
            if self.in_small_font:
                self.in_heading = True
        elif tag == 'b':
            self.in_bold = True
        elif tag == 'i':
            self.in_italic = True
        elif tag == 'br':
            self.current_text.append('\n')
        elif tag == 'a':
            # Check for footnote reference
            for attr, value in attrs:
                if attr == 'href' and '#N' in value:
                    footnote_id = value.split('#')[-1]
                    if footnote_id in self.footnotes:
                        footnote_content = self.footnotes[footnote_id]
                        # Escape special Typst characters
                        footnote_content = self.escape_typst(footnote_content)
                        # Add explicit space to prevent Typst from treating
                        # following parentheses as function calls
                        self.current_text.append(f'#footnote[{footnote_content}]#h(0pt) ')
                        self.skip_next_data = True
                        
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'head'):
            self.in_script = False
            return
        
        if tag == 'font':
            self.in_small_font = False
            
        if tag == 'p':
            if self.current_text:
                text = ''.join(self.current_text).strip()
                if text:
                    # Process quotes: remove spaces inside quotes
                    text = re.sub(r"'\s*([^']+?)\s*'", r"'\1'", text)
                    
                    # Replace standalone italicized punctuation with bare punctuation
                    # This prevents Typst from inserting line breaks at these points
                    # Handle both with and without zero-width space
                    text = text.replace('_,_', ',')
                    text = text.replace('_._', '.')
                    text = text.replace('_\u200B,_', ',')  # with zero-width space
                    text = text.replace('_\u200B._', '.')  # with zero-width space
                    
                    # Remove spaces before punctuation (fixes footnotes and italics)
                    # This handles: "text ," -> "text," and "_text_ ." -> "_text_."
                    text = re.sub(r'\s+([,.:;!?\)])', r'\1', text)
                    
                    # Remove spaces before italicized punctuation (e.g., " _._" -> "_._")
                    text = re.sub(r'\s+_​([,.:;!?])_', r'_​\1_', text)
                    
                    # Remove the #h(0pt) before punctuation since it's not needed there
                    text = re.sub(r'#h\(0pt\)\s*([,.:;!?])', r'\1', text)
                    
                    # Also remove #h(0pt) before italicized punctuation
                    text = re.sub(r'#h\(0pt\)\s*_​([,.:;!?])_', r'_​\1_', text)
                    
                    if self.in_heading:
                        self.output.append(f'\n=== {text}\n')
                    else:
                        self.output.append(text + '\n\n')
                self.current_text = []
            self.in_paragraph = False
            self.in_heading = False
        elif tag == 'b':
            self.in_bold = False
        elif tag == 'i':
            self.in_italic = False
            
    def handle_data(self, data):
        if self.in_script or self.in_style or self.skip_next_data:
            self.skip_next_data = False
            return
            
        if self.in_paragraph:
            text = data.strip()
            if text:
                # Normalize quotes - convert all quote types to single apostrophes
                # This prevents Typst from rendering them as guillemets in Latin text
                text = text.replace('«', "'").replace('»', "'")
                text = text.replace('"', "'").replace('"', "'")
                text = text.replace('"', "'")  # Convert regular double quotes too
                text = text.replace(''', "'").replace(''', "'")
                
                # Note: Space removal inside quotes is handled at paragraph level
                
                # Handle italic formatting
                if self.in_italic:
                    text = f'_\u200B{text}_'  # Using zero-width space to handle edge cases
                # Handle bold formatting
                if self.in_bold:
                    text = f'*{text}*'
                    
                self.current_text.append(text + ' ')
                
    def escape_typst(self, text):
        """Escape special Typst characters in footnotes."""
        # Escape characters that have special meaning in Typst
        replacements = {
            '#': '\\#',
            '_': '\\_',
            '*': '\\*',
            '[': '\\[',
            ']': '\\]',
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text


def create_typst_document(content, title="Enchiridion de Fide, Spe et Charitate"):
    """Create a complete Typst document with styling."""
    
    typst_doc = f'''// Augustine's Enchiridion - Typst Version
// Generated from HTML source

#set page(
  paper: "us-letter",
  margin: (x: 1.5in, y: 1in),
  numbering: "1",
)

#set text(
  font: "Linux Libertine",
  size: 11pt,
  lang: "la",  // Latin language
)

#set par(
  justify: true,
  leading: 0.65em,
  first-line-indent: 1.5em,
)

// Heading styles
#show heading.where(level: 3): it => block[
  #set text(size: 10pt, weight: "bold", fill: rgb("#333333"))
  #v(0.5em)
  #it.body
  #v(0.3em)
]

// Footnote styling
#set footnote.entry(
  separator: line(length: 30%, stroke: 0.5pt),
  gap: 0.5em,
  indent: 0em,
)

// Title page
#align(center)[
  #text(size: 20pt, weight: "bold")[
    AUGUSTINUS HIPPONENSIS
  ]
  
  #v(1em)
  
  #text(size: 16pt, weight: "bold", style: "italic")[
    {title}
  ]
  
  #v(1em)
  
  #text(size: 12pt)[
    Liber Unus
  ]
]

#pagebreak()

// Main content
{content}
'''
    
    return typst_doc


def main():
    """Main conversion function."""
    
    # File paths
    main_file = Path('/mnt/user-data/uploads/augustine_enchiridion.txt')
    footnotes_file = Path('/mnt/user-data/uploads/augustine_enchiridion_footnotes.txt')
    output_file = Path('/mnt/user-data/outputs/augustine_enchiridion.typ')
    
    print("Reading footnotes file...")
    with open(footnotes_file, 'r', encoding='utf-8') as f:
        footnotes_html = f.read()
    
    # Parse footnotes
    footnote_parser = FootnoteParser()
    footnote_parser.feed(footnotes_html)
    print(f"Found {len(footnote_parser.footnotes)} footnotes")
    
    print("Reading main body file...")
    with open(main_file, 'r', encoding='utf-8') as f:
        main_html = f.read()
    
    # Parse main content
    print("Parsing main content...")
    main_parser = EnchiridionParser(footnote_parser.footnotes)
    main_parser.feed(main_html)
    
    # Join output
    content = ''.join(main_parser.output)
    
    # Post-process to clean up quotes: remove spaces around single quotes
    # Pattern: : ' text ' becomes: 'text'
    content = re.sub(r":\s*'\s+", ":'", content)  # After colons
    content = re.sub(r"\s+'\s*,", "',", content)  # Before commas
    content = re.sub(r"\s+'\s*\.", "'.", content)  # Before periods
    content = re.sub(r"\s+'\s+", "' ", content)  # General case - space before quote
    
    # Clean up excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Create complete Typst document
    print("Creating Typst document...")
    typst_content = create_typst_document(content)
    
    # Write output
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(typst_content)
    
    print(f"\nConversion complete! Output written to: {output_file}")
    print(f"Document length: {len(content)} characters")
    print("\nYou can compile this with: typst compile augustine_enchiridion.typ")


if __name__ == '__main__':
    main()
