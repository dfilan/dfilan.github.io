---
layout: post
title:  "If a little is good, is more better?"
date: 2023-11-04
---

I've recently seen a bunch of discussions of the wisdom of publicly releasing the weights[^1] of advanced AI models. A common argument form that pops up in these discussions is this:
1. The problem with releasing weights is that it means that thing X can happen on a large scale, which causes bad effect Y.
2. But bad effect Y can already happen on a smaller scale because of Z.
3. Therefore, either it's OK to release weights, or it's not OK that Z is true.

One example of this argument form is about the potential to cause devastating pandemics, and goes as follows:
1. The putative problem with releasing the weights of Large Language Models (LLMs) is that it can help teach people a bunch of facts about virology, bacteriology, and biology more generally, that can teach people how to produce pathogens that cause devastating pandemics.
2. But we already have people paid to teach students about those topics.
3. Therefore, if that putative problem is enough to say that we shouldn't release the weights of large language models, we should also not have textbooks and teachers on the topics of virology, bacteriology, and other relevant sub-topics of biology. But that's absurd!

In this example, thing X is teaching people a bunch of facts, bad effect Y is creating devastating pandemics, and Z is the existence of teachers and textbooks.

Another example is one that I'm not sure has been publicly written up, but occurred to me:
1. Releasing the weights of LLMs is supposed to be bad because if people run the LLMs without supervision, they can do bad things.
2. But if you make LLMs in the first place, you can run them without supervision.
3. So if it's bad to publicly release their weights, isn't it also bad to make them in the first place?

In this example, thing X is running the model, bad effect Y is generic bad things that people worry about, and Z is the model existing in the first place.

However, I think these arguments don't actually work, because they implicitly assume that the costs and benefits scale proportionally to how much X happens. Suppose instead that the benefits of thing X grow proportionally to how much it happens[^2]: for example, maybe every person who learns about biology makes roughly the same amount of incremental progress in learning how to cure disease and make humans healthier. Also suppose that every person who does thing X has a small probability of causing bad effect Y for everyone that negates all the benefits of X: for example, perhaps 0.01% of people would cause a global pandemic killing everyone if they learned enough about biology. Then, the expected value of X happening can be high when it happens a little (because you probably get the good effects and not the bad effects Y), but low when it happens a lot (because you almost certainly get bad effect Y, and the tiny probability of the good effects isn't worth it). In this case, it makes sense that it might be fine that Z is true (e.g. that some people can learn various sub-topics of biology with great tutors), but bad to publicly release model weights to make X happen a ton.

So what's the up-shot? To know whether it's a good idea to publicly release model weights, you need to know the costs and benefits of various things that can happen, and how those scale with the user-base. It's not enough to just point to a small amount of the relevant effects of releasing the weights and note that those are fine. I didn't go thru this here, but you can also reverse the sign: it's possible that there's some activity that people can do with model weights that's bad if a small number of people do it, but good if a large number of people do it: so you can't necessarily just point to a small number of people doing nefarious things with some knowledge and conclude that it would be bad if that knowledge were widely publicized.

[^1]: Basically, the parameters of these models. Once you know the parameters and how to put them together, you can run the model and do what you want with it.

[^2]: Or more generally, polynomially (e.g. maybe quadratically because of Metcalfe's law).
