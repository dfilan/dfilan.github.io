---
layout: post
title: "Challenge: know everything that the best go bot knows about go"
date: 2021-05-10
---

On a few different views, understanding the computation done by neural networks is crucial to building neural networks that constitute human-level artificial intelligence that doesn’t destroy all value in the universe. Given that many people are trying to build neural networks that constitute artificial general intelligence, it seems important to understand the computation in cutting-edge neural networks, and we basically do not.

So, how should we go from here to there? One way is to try hard to think about understanding, until you understand understanding well enough to reliably build understandable AGI. But that seems hard and abstract. A better path would be something more concrete.

Therefore, I set this challenge: know everything that the best go bot knows about go. At the moment, the best publicly available bot is [KataGo](https://github.com/lightvector/KataGo), if you’re at DeepMind or OpenAI and have access to a better go bot, I guess you should use that instead. If you think those bots are too hard to understand, you’re allowed to make your own easier-to-understand bot, as long as it’s the best.

What constitutes success?
- You have to be able to know literally everything that the best go bot that you have access to knows about go.
- It has to be applicable to the current best go bot (or a bot that is essentially as good - e.g. you’re allowed to pick one of the versions of KataGo whose elo is statistically hard-to-distinguish from the best version), not the best go bot as of one year ago.
  - That being said, I think you get a ‘silver medal’ if you understand any go bot that was the best at some point from today on.

Why do I think this is a good challenge?
- To understand these bots, you need to understand planning behaviour, not just pick up on various visual detectors.
- In order to solve this challenge, you need to actually understand what it means for models to know something.
- There’s a time limit: your understanding has to keep up with the pace of AI development.
- We already know some things about these bots based on how they play and evaluate positions, but obviously not everything.
- We have some theory about go: e.g. we know that certain symmetries exist, we understand [optimal play in the late endgame](https://en.wikipedia.org/wiki/Combinatorial_game_theory), we have some neat [analysis techniques](http://www.361points.com/articles/1/1/).
- I would like to play go as well as the best go bot. Or at least to learn some things from it.

Corollaries of success (non-exhaustive):
- You should be able to answer questions like “what will this bot do if someone plays [mimic go](https://www.youtube.com/watch?v=w9AeJ_M1D5g&feature=youtu.be) against it” without actually literally checking that during play. More generally, you should know how the bot will respond to novel counter strategies.
- You should be able to write a computer program anew that plays go just like that go bot, without copying over all the numbers.

Drawbacks of success:
- You might learn how to build a highly intelligent and capable AI in a way that does not require deep learning. In this case, please do not tell the wider world or do it yourself.
- It becomes harder to check if professional human go players are cheating by using AI.

Related work:
- The work on identifying the ‘[circuits](https://distill.pub/2020/circuits/)’ of [Inception v1](https://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Szegedy_Going_Deeper_With_2015_CVPR_paper.html)
- [The case for aligning narrowly superhuman models](https://www.lesswrong.com/posts/PZtsoaoSLpKjjbMqM/the-case-for-aligning-narrowly-superhuman-models)

*A conversation with Nate Soares on a related topic probably helped inspire this post. Please don't blame him if it's dumb though.*
