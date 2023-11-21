---
layout: post
title:  "How to type Aleksander Mądry's last name in LaTeX"
date: 2023-11-20
---

1. Type "Madry"
2. Realize that the a has a little tail that you need to include.
3. That's a feature of the Polish alphabet called an [ogonek](https://en.wikipedia.org/wiki/Ogonek).
4. You type it in LaTeX like so: `M\k{a}dry`.
5. You get the error "Command \\k unavailable in encoding OT1".
6. That's because you need LaTeX to use a slightly different font package.
7. In your preamble, add `\usepackage[T1]{fontenc}`.
8. You're done.

My thanks to the Stack Exchange articles about [how to use that symbol](https://tex.stackexchange.com/questions/75396/how-to-use-polishhook-symbol) and [how to deal with the LaTeX error I got implementing that fix](https://tex.stackexchange.com/questions/392208/command-k-unavailable-in-encoding-ot1-error-takes-me-to-line-which-doesnt-eve).
