---
layout: post
title:  "Difficulties in making powerful aligned AI"
date: 2023-05-14
---

Here's my breakdown of the difficulties involved in ensuring powerful AI makes our lives radically better, rather than taking over the world, as well as some reasons why I think they're hard. Here are things it's not:
- It's not primarily a justification of why very powerful AI is possible or scary (altho it briefly discusses why very powerful AI would be scary).
- It's not primarily a list of underlying factors that cause these difficulties (altho it does include and gesture to some of those).
- It's not at all original - basically everything here has been said many times before, plausibly more eloquently.

That said, it is my attempt to group the problems in my own words, in a configuration that I haven't seen before, with enough high-level motivation that one can hopefully tell the extent to which advances in the state of the art address them.

## 1. What sort of thinking do we want?

The first difficulty: we don't have a sense of what sort of thinking we would want AI systems to use, in sufficient detail that one could (for instance) write python code to execute it. Of course, some of the difficulty here is that we don't know how smart machines think, but we can give ourselves access to subroutines like "do perfect Bayesian inference on a specified prior and likelihood" or "take a function from vectors to real numbers and find the vector that minimizes the function" and still not solve the problem. To illustrate:
 1. Take a hard-coded goal predicate, consider a bunch of plans you could take, and execute the plan that best achieves the goal? [Unfortunately](https://arxiv.org/abs/1912.01683), the vast majority of goals you could think of writing down in an executable way will incentivize [behaviour](https://arbital.com/p/instrumental_convergence/) like gaining control over sources of usable energy (so that you definitely have enough to achieve your goal, and to double- and triple-check that you've really achieved it) and stopping [other agents](https://en.wikipedia.org/wiki/Human) from being able to meddle with your plans (because if they could, maybe they'd stop you from achieving your goal).
 2. [Do things that maximize the number of thumbs up you get from humans?](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)[^1] Best plan: take control of the humans, force them to give you a thumbs up, or trick them into doing so. Presumably this is possible if you're much smarter than humans, and it's more reliable than doing good things - some people might not see why your good thing is actually good if left to their own devices.
 3. [Look at humans, figure out what they want based on what they're doing, and do whatever that is?](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/inverseRL.pdf) Main problem: people don't do the literally optimal thing for what they want. For instance, when people play chess, they usually don't play perfect moves - even if they're experts! You need some rule that tells you what people would do if they wanted some goal or another, but [it's not clear what this rule would be](https://ai-alignment.com/the-easy-goal-inference-problem-is-still-hard-fad030e0a876), it's not clear how you make this rule more in line with reality if you never observe "wanting", and so this ends up having essentially the same problems as plans 1 and 2.
 4. [Read some text written by humans about what they'd like you to do, and do that?](https://arxiv.org/abs/2212.08073)[^2] This is passing the buck to the text written by humans to specify how we want the AI to think, but that's precisely the problem we're trying to solve. Concretely, one way you could imagine doing this is to write something relatively informal like "Please be helpful and harmless to your human operators", and have your AI correctly understand what we mean by that. That (a) presumes that there is a coherent thing that we mean by that (which doesn't seem obvious to me, given our difficulty in explicitly formalizing this request), and (b) passes the specification buck to the problem of specifying how you should understand this request.

It's not a priori definitely impossible to build a thinking machine that does what we want without knowing how we want it to think, but it's not at all obvious how one would. A core difficulty here is that the sorts of signs of positive outcomes we know how to specify (like "GDP has gone up a lot" or "a human says that they're happy with the AI's performance") are compatible with extremely bad outcomes - and in general, as mentioned in point 1, things that are trying to achieve their own objectives in the physical world will be incentivized to cause those bad outcomes.

## 2. How do we recognize advanced AIs that we like?

Given that we don't know how to specify advanced AI cognition that will do good stuff and not take control of Earth, how could we hope to build it? One obvious path is a sort of trial and error: we build some AIs, and before putting them in situations where they could conceivably take over (e.g. by having them become able to influence enough of the physical world to build fancy new technology), we figure out if they would do good stuff. Then, we can only deploy things that actually do good stuff, or even better, tweak things such that they're more likely to do better stuff, and less likely to take over. The question is: how would we determine if our AIs will do good stuff once they're able to take over?

One possibility you could imagine is trying to write a proof - after all, AIs are algorithms written in computer code, and one can often prove things about algorithms. The problem is that it's entirely unclear what property we'd want to prove that our AI has, to the level of formal specificity that one could write a proof about it.[^3] This is closely related to the difficulty in section 1: if we had such a "goodness" property, we could build an AI that thought of plans that scored highly on "goodness".

A second possibility is that you could look at your AI's behaviour in a range of circumstances, and see how good it is. If your 'goodness' ratings come as numbers, and there are a bunch of free variables in your AI design, you can even automatedly do [gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) to set those variables to values that get your AI to do things rated as highly good. The basic problem here is that just because your AI does good stuff when it can't take over the world, doesn't mean that it will do good stuff once it can. The basic reason is that by and large, there are a lot of motivations that can cause AIs to do stuff that looks good:
 1. It could be motivated by goodness. In this case, things are OK!
 2. It could be motivated by trying to get you to approve of it. In this case, once it can, it will probably try to control your brain to get you to approve of it (of course, without letting you know beforehand, so that you don't disapprove in the mean time).
 3. It could be motivated by random weird abstractions that come apart from what you were looking for once they're optimized hard enough. For instance, consider how humans were optimized by evolution to reproduce a lot - this seems to have been implemented by enjoying genital contact when in the presence of attractive other humans, so once humans were capable of inventing contraception, they used that instead[^4]. Similarly, you could imagine AIs taking over and pursuing some strange goals, vaguely reminiscent of the goals we attempted to select it for.
 4. It could be motivated by near-arbitrary long-term goals, that all incentivize the AI convincing you to release it. As long as your AI has goals that are better satisfied when it's out of your testing box - and there are tons of goals like this, like "amass a bountiful fortune" or "solve a ton of math" - and as long as it can tell that it's being tested, it can choose to 'play nice' in the short run and pass your tests, until it's free to take over and pursue its own desires.

So, it seems like there are more AIs that pass your behavioural tests without being aligned with your interests than AIs that pass your behavioural tests by being aligned with your interests. Note that this issue is, again, related to difficulties discussed in section 1: just like how many goals we could initially imagine writing down (like "get humans to approve of you" or "run a profitable business without being caught breaking any laws") produce bad behaviour when optimized by an advanced AI, similarly there are many motivations that produce good behaviour before an advanced AI can take over the world, but not after.

Also note that we are talking as if our AIs have "motivations", thus allowing us to re-use some of the reasoning from section 1: thinking of strategies that help achieve some goal, and concluding that the AI will take those strategies. This should be understood as saying that they coherently steer the world into some narrow set of states[^5] (aka the states they are 'motivated' to reach), not as a strong claim about their exact internal functioning. And in order for AIs to be useful, they need to be steering the world into observably different, hard-to-reach states, compared to if they weren't made.

Finally, a worrying aspect of this second possibility is that many of its failure modes can only be exhibited once AI is advanced enough to be dangerous. By analogy, external observers may not have been able to tell that humans would end up using contraception until they were technologically advanced enough to make reliable contraceptives. Similarly, possibility 4 will only show up once AIs can come up with and competently execute such deceptive plans.[^6]

## 3. How do neural networks actually work?

A third issue is that our current best ways of making AI involve taking gigantic tensors of numbers glued together by matrix multiplication and some non-linear functions (aka 'neural networks'), and tweaking them until they do something impressive when run. This design doesn't place strong constraints on specific parts of those tensors having any particular known function - it's just a collection of numbers that happens to exhibit the right behaviours.

There are two closely-related key problems with this type of AI design:
 1. Because the gigantic tensors have no particular pre-determined semantic meaning, it's hard to instill any particular cognitive algorithm into them.
 2. Because the tensors are so large and devoid of meaningful structure that we are currently able to easily comprehend, it's difficult for human engineers to understand the algorithms being implemented by the AI, or to make grounded predictions about how they will behave in new situations.

Problem 1 means that we aren't able to precisely steer the cognition of smart AIs into styles that we like, even if we knew the sort of cognition we wanted to distill; and problem 2 means that we can't easily perform meaningful safety analysis for large capable AIs, even if we knew what this would look like.

## 4. Can safely limited AI solve the problem for us?

Given that we face these difficult problems, you might hope that we are able to use AI to solve them - just like we've used it to solve other problems that are insurmountable by humans, like "beat the best human chess player at chess". This strategy only works if the AI we use isn't the sort that we might be scared of. However, there are a few aspects of the alignment problem that make it seem very difficult for AIs that aren't advanced enough to be scary:
 1. It's hard enough that humans don't have a convincing solution yet, despite many people trying for many years.
 2. It involves thinking carefully about the design of smart, capable agents. Presumably, if you're able to do really good reasoning about the design of such agents, you're in a position to make some for yourself, potentially engendering the problems that such agents bring about.
 3. It involves achieving big successes in technical research. To solve these problems, you likely need to be able to prove novel theorems, think of untested strategies, come up with new sorts of algorithms, etc. These are broadly similar to the abilities necessary to do other kinds of technical research - of course, the detailed types of thinking and knowledge required for different fields are different, but the same sorts of humans can learn to be proficient in multiple different fields of research, and likewise the sort of AI that can learn to successfully do alignment research could also learn to successfully do other sorts of technical research. If we have an AI on our hands that can outcompete humans at a wide array of fields of technical research, that sounds like the sort of AI that may be able to take over the world via technological superiority.

To be sure, limited AIs can help in the meantime by e.g. making Google search better, or facilitating other kinds of human cognitive labour. But it's not obvious how we can successfully outsource the AI alignment problem to other AIs, while being confident that the AIs we outsource to don't need to be aligned themselves.

## Discussion

As mentioned in the introduction, these problems are by no means unknown in the literature. Section 1 is related to work on [value learning](https://www.lesswrong.com/tag/value-learning), [corrigibility](https://intelligence.org/files/Corrigibility.pdf), and [multi-multi alignment](https://acritch.com/papers/arches.pdf). Section 2 is related to work on [inner alignment](https://arxiv.org/abs/1906.01820), robustness and interpretability in machine learning, as well as [informed](https://ai-alignment.com/the-informed-oversight-problem-1b51b4f66b35) and [scalable](https://arxiv.org/abs/1606.06565) oversight. Section 3 is related to work on interpretability in machine learning, as well as deep learning theory. Finally, section 4 is related to [OpenAI's approach to AI alignment](https://openai.com/blog/our-approach-to-alignment-research).

Furthermore, not all these problems need to be solved in order to build powerful aligned AI. I would break it down this way:
- Do you want humans to build powerful aligned AI themselves, or build a machine to solve the problem for them?
    - If we are trying to build powerful aligned AI ourselves, we need to either know what sort of AI cognition we want, or know how to recognize the sort of AI that we want (or perhaps both).
        - Learning what sort of AI cognition we want involves facing difficulty 1. After solving that difficulty, we would still face the problem of building it, which involves facing difficulty 3, either by understanding current machine learning better, or using something else.
        - Recognizing the sort of AI that we want requires facing difficulty 2. Does this involve looking at the internals of the AI, or merely its behaviour?
            - If this involves looking at the internals of the AI, we face difficulty 3.
            - If it instead involves building the sorts of models that only have the right sort of behaviour while unable to take over the world if they would also have the right sort of behaviour when able to take over the world, that sounds like it involves facing difficulty 1 and 3.
    - If we are trying to make a machine build powerful aligned AI, we face difficulty 4.

*My thanks to [Erik Jenner](https://www.lesswrong.com/users/erik-jenner) for commenting on a draft of this post.*

---

[^1]: It's actually slightly unfair to conflate this with RLHF, because [reinforcement learning uses reward to shape agents' thoughts, rather than building agents that optimize for reward](https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target), but I think this critique is relevant to understanding problems with RLHF, for reasons gestured to in section 2.

[^2]: I don't think that this is actually what the people behind 'constitutional AI' were thinking, but it's nice and linkable, and this is a proposal that some people talk about.

[^3]: Also, such a proof would plausibly require modelling the range of situations your AI would find itself in, which is a challenge to formalize. h/t Erik Jenner for making this point.

[^4]: Presumably evolution would, given enough time, eventually shape our psychology so that we abstain from contraception enough to have lots of children. But for the present point, what's important is that it didn't manage to instill the right desires on the first try, before we were powerful enough to invent technology to suit our interests.

[^5]: Note that there are some subtleties in this definition, as described [here](https://www.lesswrong.com/posts/26eupx3Byc8swRS7f/bottle-caps-aren-t-optimisers), but it will do for now.

[^6]: It's [been proposed](https://axrp.net/episode/2023/04/11/episode-20-reform-ai-alignment-scott-aaronson.html#aligning-deceitful-ai) that AIs will first be bad at deception before they're good at it, just like they were bad at chess before they were good at it, and this will give us advanced warning to solve the problem. Besides my worry that existing AIs can already exhibit primitive deceptive behaviour, and that this doesn't seem to be spurring effective research to deal with this failure mode, I also think that AIs will be able to evaluate whether they're able to effectively deceive (in service of another goal) before they can actually effectively deceive (in service of another goal), and given that ineffective deception is worse than useless, I'd expect some regime where AIs refrain from behaving deceitfully until they're able to do so effectively.