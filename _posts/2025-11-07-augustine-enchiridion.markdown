---
layout: post
title:  "Augustine of Hippo's Handbook on Faith, Hope, and Love in Latin (or: Claude as Pandoc++)"
date: 2025-11-07
---

tl;dr [Here's a pdf](/pdfs/augustine_enchiridion.pdf). The story of me making it is slightly fun.

[Augustine of Hippo](https://en.wikipedia.org/wiki/Augustine_of_Hippo), a prominent Christian of the 4th and 5th centuries who is recognized as a saint by many churches, wrote many things, including a work known as the Handbook on Faith, Hope, and Love (or the Enchiridion on Faith, Hope, and Love, or replace "Love" with "Charity", or, in Latin, Enchiridion de Fide, Spe, et Charitate or Enchiridion ad Laurentium). Recently, [Claude 4.5 Sonnet](https://claude.ai/share/68a86809-96c6-477b-8d8c-668aa4a7b213) recommended I give it a read as an intermediate Latin learner who's interested in Augustine's theology. Unfortunately, [the only website I could find where I could read it in Latin](https://www.augustinus.it/latino/enchiridion/index.htm) looked unpleasing to me, and I wished I could read it in a more beautiful form.

I asked my friends how I could do that, and Oliver Habryka suggested that an LLM could probably one-shot it. Taking up his suggestion, I inspect-elemented to get the raw text from the online text, and [asked Claude 4.5 Sonnet](https://claude.ai/share/2e468e52-e6ba-471e-a6c7-b3a60d091c21) to write a python script to turn that into [typst](https://typst.app/), a new document markup language intended as a LaTeX replacement. To my pleasure, Claude was not only able to write the script but also to run it itself and make its own typst, allowing it to check its work. To my displeasure, there were several problems that needed me to iteratively ask for fixes for. That said, it eventually got to a point where there were few enough issues that I was able to manually fix them all, add a nice picture to the start, and get a [pleasing final product](/pdfs/augustine_enchiridion.pdf) (typst project visible [here](https://typst.app/project/r8tCTYFsn0Lxk92K2qiOpt))

It still isn't quite where I'd like it to be. Firstly, footnotes after italicized punctuation marks look quite nasty: footnote 1 is egregious, and 6 (on page 3) is also quite unpleasant. Also ideally I'd be able to print this out and read it like a book, which the current layout is not ideal for (altho it's a bit long to nicely bind in any case). Even more ideally, it would have facing Latin text with English translation, a la the [Loeb Classical Library](https://en.wikipedia.org/wiki/Loeb_Classical_Library). Such a translation [is publicly available](https://ccel.org/ccel/augustine/enchiridion), but I'm not sure about the copyright status, and making it sync up nicely seems rather difficult.

If you spot any errors, please let me know by sending me an email, and I will endeavour to fix them.
