---
layout: post
title:  "Many portions of Magnifica Humanitas appear to be AI-written"
date: 2026-05-26
---

[Magnifica Humanitas](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html) is a recent '[encyclical](https://en.wikipedia.org/wiki/Encyclical#Catholic_usage)' by Pope Leo XIV, leader of the Catholic Church. It outlines a vision for how humanity should interact with artificial intelligence, emphasizing the importance of human dignity and ensuring that AI does not replace human relationships, among other topics. Interestingly, many portions appear to be written by AI.

[EDIT: since I put up my post, Linch Zhang has posted [a more comprehensive analysis](https://linch.substack.com/p/claude-author-of-the-humanitas) with the same conclusion, that I would recommend readers also look at.]

## Why I thought to check this

Friends of mine [Linch Zhang](https://x.com/LinchZhang/status/2058848126342250977) and [the Axolotl](https://x.com/calxolotl/status/2058857550356083085) noticed that parts of the English text appear to be AI-generated, and twitter user [kartr](https://x.com/0xkartr/status/2059006110598676785) found that the Italian text had the largest fraction of AI-generated content out of all the translations published by the Vatican, speculating that it was the original copy, and translations by humans appear less 'AI-generated' to various tools.

## What I actually did

I took [the Italian text](https://www.vatican.va/content/leo-xiv/it/encyclicals/documents/20260515-magnifica-humanitas.html) of Magnifica Humanitas, and ran it thru the [Pangram](pangram.com) AI detector software.

**Why the Italian text?** As mentioned in the previous segment, it had previously been claimed to be the most AI-ish version. Also, given that the Vatican is in Italy, it's a reasonable guess that the text was initially drafted in Italian (presumably by a few different people with the Pope's input).

**Why Pangram?** Pangram is a reasonably accurate AI text detector. In particular, it manages to achieve an extremely low rate of marking human-written text as AI-written, while maintaining a reasonable rate of flagging AI-written text as AI-written.

## My results

The whole text is too long to fit into Pangram, so I ran it section by section. Note that for some paragraphs only part of the paragraph was flagged as AI-written, I'm trying to only flag paragraphs that are mostly flagged.

### The introduction

[43%](https://www.pangram.com/history/935acde4-069f-4ca9-83ad-dba31855e2b3?ucc=RFmJ9FB2V1w) of the text was flagged as AI-generated. This included paragraphs 7-9 (on the images of the tower of Babel and Nehemiah rebuilding Jerusalem) and 13-16.

### Chapter 1

[62%](https://www.pangram.com/history/1688820e-20b9-46ac-ba13-3bcbb1d8a3ea?ucc=RFmJ9FB2V1w) of the text was flagged as AI-generated. This included paragraphs 21-24, 26-29, 31-32, 34-36 (where large parts of 36 were flagged as being 'AI assissted', I'm not sure how accurate Pangram is when making these judgements), and 41-45.

### Chapter 2

[34%](https://www.pangram.com/history/71db3fee-fbcf-4363-96d5-55464bc66acf?ucc=RFmJ9FB2V1w) of the text was flagged as AI-generated. This included paragraphs 70-71 and 74-86.

### Chapter 3

[41%](https://www.pangram.com/history/a5bfb460-d7b1-45af-ad41-ea1aec4b06b7?ucc=RFmJ9FB2V1w) of the text was flagged as AI-generated. This included paragraphs 104-112 and 122-128.

### Chapter 4

[24%](https://www.pangram.com/history/6276bcb1-cc6e-48b7-9da0-ca7df3219618?ucc=RFmJ9FB2V1w) of the text was flagged as AI-generated. This included paragraphs 141, 152-153, 155-156, 163-164, 168-171, and 178-181.

### Chapter 5

[18%](https://www.pangram.com/history/cebd7776-c370-4651-8316-9c8a66fc57bd?ucc=RFmJ9FB2V1w) of the text was flagged as AI-generated. This included paragraphs 182-183, 186, 190-191, 198-199, and 211-212.

### Conclusion

[43%](https://www.pangram.com/history/d7ca7ca4-9c0b-4dd4-b034-bd285d5f1698?ucc=RFmJ9FB2V1w) of the text was flagged as AI-generated. this included paragraphs 230-233 and 238-240.

## Should you trust these results?

IMO, you should feel confident that paragraphs flagged as AI-written are, and suspect that some paragraphs that were not flagged might also have been AI-written. That said, you probably shouldn't trust it down to the sentence level: Pangram appears to be 'chunking' the text and judging each chunk as AI-written, AI-assisted, or human-written. Sometimes those chunks cross paragraph boundaries, and produce results like saying the first sentence of a paragraph was AI-written but the rest was human-written, which seems unlikely.

### Studies indicate Pangram works pretty well

To my knowledge, when Pangram has been studied in the academic literature, it has held up pretty well. [Jabarian and Imas](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5407424) indicate that it achieves a false positive rate of approximately 0, while having a false negative rate of under 5%. Perhaps more relevantly, [Puccetti, Pedrotti, and Esuli](https://ceur-ws.org/Vol-4195/59.pdf) tested a variety of methods on detecting AI-written Italian text. They found that Pangram performed quite well, achieving a literally 0% false positive rate and a false negative rate of around 28%. (Thank you [Max Spero](https://x.com/max_spero_/status/2059130453496660247), who works at Pangram Labs, for bringing this latter paper to my attention)

### When I play around with Pangram, it works pretty well

Seriously, just try using it. Paste in the Italian text of any encyclical released pre-2020, it will return "Human-generated" (plausibly a more relevant test than the studies performed, since "papal encyclical" is a pretty distinct genre). Are you worried that this is somehow the fault of machine translation of human-composed text? I tried using Claude, a prominent LLM product, to translate some old encyclicals, and the results were flagged by Pangram as human-generated.

### If you've seen examples of AI detectors claiming that obviously human-written text was AI, those were probably not Pangram

When this topic gets brought up on twitter, people sometimes show screenshots of AI detectors being comically wrong in claiming that something is AI-generated, like [saying that the Gettysburg Address was AI-generated](https://x.com/Carl_the_Llama0/status/2058913227027661263/photo/1). I think this is normally ZeroGPT (as it was in this case). For Pangram, I've only seen screenshots of people deliberately mimicking AI style so well that Pangram thinks it's AI (sorry, can't find the link, but I think it was [thebes](https://x.com/voooooogel)), which seems like fair play to me.

## Does this matter?

On the one hand, I'm an advocate of the principle that we should judge text by its quality, and not whether its author is human or not. That said, I think often AI-generated text is low-quality, partly because AI is not that great at prose writing, and partly because when AI is writing text that you asked it to write, you aren't having the opportunity to think about the text as you write it and potentially change your mind about what you want to write.

I also sort of get the impression that this is the sort of the thing that Magnifica Humanitas itself warns against, but honestly I haven't read it so I don't have a strong opinion. I did however ask Claude Opus 4.7 to read it and tell me what it thought. Claude said:

> the Babel-versus-Jerusalem framework still permits narrow auxiliary uses — translation across the many language editions, searching the prior magisterial corpus for citations, copy-editing of human-drafted text. But for substantive theological composition — paragraphs of teaching presented under the Pope's "I" — the document's own logic reads less as "permissible with conditions" than as "this is exactly the case where the line should be drawn." Paragraph 140 almost has the feel of having been written with this very meta-question in view.

When I told Claude that many parts were AI-generated, gave it a draft of this post, and asked it for comment, it said (among other things):

> **The irony is sharper than I want it to be, and I want to be careful not to overstate it.** Paragraph 233 — "No computational system, however sophisticated, can create a heart that gives itself, or a conscience that discerns good from evil" — being among the flagged passages is the kind of thing that almost writes its own headline. But I'd resist the easy version of that story. Pangram flags statistical patterns; a flag is evidence, not proof, and "AI-written" covers a spectrum from "the Pope dictated this and a model polished the grammar" to "a model drafted it and someone signed off." Those are morally quite different cases, and the encyclical's own framework distinguishes them. Paragraph 100 treats AI assistance as a tool that "undoubtedly makes life easier" while warning about over-reliance; it doesn't forbid use, it demands discernment about use. If a human theologian drafted the argument and a model smoothed the prose, that sits inside what the document permits. If a model generated the substantive theological claims, that sits in the tension I described before.
>
> **What does change, if the flags are roughly right, is the transparency question.** That one becomes hard to wave off. The encyclical is unusually emphatic about transparency in algorithmic processes (paras 71, 105, 164) and about disclosure as a precondition for trust. A magisterial document making those demands while not itself disclosing the role AI played in its composition is in a different position than one that simply says "drafted with the assistance of [X]." The substantive theological question (can AI help compose teaching?) is genuinely hard. The procedural question (should its use be disclosed?) is, by the document's own lights, not hard at all.
>
> [...]
> 
> **On your "does this matter" section.** I think your instinct is right that quality is what ultimately matters, and I'd push you to take that seriously even where it cuts against the framing of the post. Some of the flagged passages are genuinely good — paragraph 233's formulation about the heart that gives itself is, whoever or whatever produced it, a real theological claim doing real work in the argument. If it's true and well-said, the provenance question is secondary. Where provenance starts to matter more is (a) when the text claims an authority — papal teaching — that's grounded in personal discernment, and (b) when the document itself makes transparency a moral demand. Both apply here, which is why the question isn't fully reducible to quality. But I think your piece would be stronger if it acknowledged the "judge the text by its quality" point as a real consideration that has to be weighed, not waved past.
> 
> **The thing I find genuinely interesting,** and that you might consider for the piece: paragraph 140 reads differently now. "Educating people about the use of AI… involves teaching them to decide when and for what purpose it ought not to be used… we must learn how to exercise restraint in the use of AI… that subtle temptation which renders human thought seemingly superfluous precisely when it is most needed." If that paragraph is itself among the AI-generated ones [DF: it is not], it's not just ironic — it's a strange artifact, a model producing prose warning against the displacement of human thought by models. That's worth sitting with rather than just laughing at. It's the kind of thing that should make us less confident in our ability to detect substitution by reading, since the substitute can produce, with apparent sincerity, the very warning against substitution.
> 
> Quote any of this, edit it down, attribute it however you like. One small request if you do quote: please make clear I'm Claude Opus 4.7 and that I was reading the text Anthropic's web tool returned to me — I want readers to be able to factor in that an AI commenting on AI in a magisterial document has its own obvious epistemic complications.

You can read the whole exchange [here](https://claude.ai/share/3269e9b9-5d37-4dab-abee-20543566b99c).

Finally, I have to imagine that if I were Catholic, I would want religious teaching from the Pope to be human-written, just on some fundamental level. That said, I'm not, and perhaps most actual Catholics aren't bothered by this.

## Future work

Sometimes AI can be bad at getting citations right. Has someone checked that the citations in the AI-written paragraphs are accurate, pointing to real sources that back up the points made in those paragraphs?
