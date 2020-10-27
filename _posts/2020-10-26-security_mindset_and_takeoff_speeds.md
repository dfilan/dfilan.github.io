---
layout: post
title:  "Security Mindset and Takeoff Speeds"
date:   2020-10-26
---

## About this post

This post is a stylized transcript of a conversation between Rohin Shah and Daniel Filan, two graduate students at CHAI, that happened in 2018. It should not be taken as an exact representation of what was said, or even what order topics were brought up in, but it should give readers a sense of what was discussed, and our opinions on the topic of conversation at the time of the discussion. It also should not be assumed that any of the points brought up are original to Rohin or Daniel, just that they represent our thinking at the time of the conversation. Notes were taken by Rohin during the conversation, and Daniel took the lead in writing it into a blog post.

The conversation was precipitated when Rohin noted that researchers at CHAI, and in AI alignment more broadly, diverged in their attitudes towards something like [security mindset](https://intelligence.org/2017/11/25/security-mindset-ordinary-paranoia/), that we will just call security mindset despite being somewhat different to what is described in the linked blog post.

Some researchers at CHAI are very concerned about building an axiomatic understanding of artificial intelligence and proving solid theorems about the behaviour of systems that we are likely to build. In particular, they are very concerned about expecting benign behaviour without a formal proof to that effect, and believe that we should start worrying about problems as soon as we have a story for why they will be problems, rather than when they start manifesting. At the time of the conversation, Daniel was one of these researchers, who have what we'll call "security mindset".

In contrast, some other researchers believe that we should focus on thinking about what extra machinery is needed to build aligned AI, and try building that extra machinery for current systems. Instead of dealing with future anticipated problems today and developing a theory that rules out all undesired behaviour, these researchers believe that we should spend engineering effort to detect their occurence and fix problems once we know that they occur and have more information about them. They think that rigour and [ordinary paranoia](https://intelligence.org/2017/11/25/security-mindset-ordinary-paranoia/) are important, but less important than security mindset advocates claim. At the time of the conversation, Rohin was one of these researchers.

During a prior conversation, Rohin noted that he believed that security mindset was less important in a world where the power of AI systems gradually increased, perhaps on an exponential curve, over a period of multiple years, as opposed to a world where AI systems could gain a huge amount of power rather suddenly from designers having conceptual breakthroughs. Daniel was intrigued by this claim, as he had recently come to agree with [two](https://sideways-view.com/2018/02/24/takeoff-speeds/) [posts](https://aiimpacts.org/likelihood-of-discontinuous-progress-around-the-development-of-agi/) arguing that this sort of 'slow takeoff' was more likely than the [alternative](https://intelligence.org/files/IEM.pdf), and was unsure how this should affect all his other views on AI alignment. As a result, he booked a separate meeting to exchange and discuss models on this topic. What follows is a record of that separate meeting.

## The conversation

**Daniel**: Here's my worry. Suppose that we're thinking about an AI system that is better at, say, math or engineering than humans. It seems to me that this AI system is going to have to be able to do some sort of optimization itself---maybe thinking about how to optimize physical structures so that they don't fall down, or maybe thinking about how to optimize its own computation so that it can efficiently find proofs of a desired theorem. At any rate, if this is the case, then what we have on our hands is optimization that is being done in a direction other than "behave maximally predictably", and is plausibly being done adversarially. This is precisely the situation in which you need security mindset to reason about the system on your hands.

**Rohin**: I agree that security mindset is appropriate when something is optimizing adversarially. I also agree that holding capability levels constant, the more we take a security mindset approach, the more safe our resulting systems are. However:

1. We simply don't have time to create a system that can be proved aligned using security-mindset-level rigour before the first [prepotent](http://acritch.com/arches/) AI system. This means that we need to prioritize other research directions.

2. Because we will likely face a slow takeoff, things will only change gradually. We can rely on processes like testing AIs, monitoring their thoughts, boxing them, and red-teaming to determine likely failure scenarios. If a system has dangerous abilities that we didn't test for, it will be the weakest possible system with those dangerous abilities, so we can notice them in action as they produce very minor damage, disable that system, create a new test, and fix the problem.

3. We should instead focus on constructing AI systems that correctly infer the nuances of human intent, rather than trying to address problems that could arise ahead of time. This will plausibly work to create an AI that can solve the harder problems for us.

**Daniel**: I have a few responses to those points.

1. Regarding your first point, I'm more optimistic than you. If you look at the progress made on the [Agent Foundations research agenda](https://intelligence.org/technical-agenda/) in the past five years (such as work on [reflective oracles](https://arxiv.org/pdf/1508.04145.pdf) and [logical induction](https://arxiv.org/pdf/1609.03543.pdf)), for example, it seems like we could solve the remaining problems in time. That being said, this isn't very [cruxy](http://www.rationality.org/resources/updates/2016/double-crux) for me.

2. Regarding your second point, I think that in order to write good tests, we will need to take a security mindset approach, or at least an ordinary paranoia approach, in order to determine what things to test for and in order to write tests that actually rule out undesired properties.

3. In general, I believe that if you do not build an AI with security mindset at the forefront of your concerns, the result will be very bad---either it will cause an unacceptable level of damage to humanity, or more likely it just won't work, and it will take a very long time to fix it. This sucks, not just because it means that your work is in some sense wasted, but also because...

4. There will likely be a competing AI group that is just a bit less capable than you, and a different group just less capable than them, and so on. That is to say, I expect AI capabilities to be continuous across space for similar reasons that I would expect them to be continuous across time.

5. As a result of 3 and 4, I expect that if your group is trying to develop AI without heavy emphasis on security mindset, you fail and get overtaken by another group, and this cycle continues until it reaches a group that does put heavy emphasis on security mindset, or until it creates an AI that causes unacceptable levels of damage to humanity.

**Rohin**: I doubt your point 4. In our current world, we don't see a huge number of groups that are realistic contenders to create smarter-than-human AI, and the groups that we [do](https://openai.com/) [see](https://deepmind.com/) show a promising degree of cooperation, such as collaborating on [safety](https://blog.openai.com/deep-reinforcement-learning-from-human-preferences/) [research](https://deepmind.com/blog/learning-through-human-feedback/) and making promising [commitments](https://blog.openai.com/openai-charter/) towards avoiding dangerous race dynamics. Also, I think that in worlds where there is such a break-down of cooperation that your point 4 applies, I think that technical work today is near-useless, so I'm happy to just ignore these worlds.

I also think that the arguments that you give for point 4 are flawed. In particular, the arguments for slow take-off require gradual improvement that builds on itself, which happens over time but is not guaranteed to happen over space. In fact, I expect there to be great resource inequalities between groups and limited communication between competing groups, which should generate very large capabilities gaps between competing groups. This is something like a local crux for me: if I thought that there weren't resource inequalities and limited communication, I would also anticipate competing groups to have similar levels of capabilities.

**Daniel**: Hmmmmmm. I'll have to think about the arguments that I should anticipate large capability gaps between competing groups, but they seem pretty convincing right now.

Actually, maybe we should expect the future to look different to the past, with countries like China and India growing capable AI labs. In this world, it's sadly plausible to me that pairs of countries' research groups could end up failing to cooperate. But again, I'll have to think about it more.

At any rate, even if my point 4 fails, the rest of my points imply that research done without security mindset at the forefront will reliably be useless, which still feels like a strong argument in favour of security mindset.

**Rohin**: Then let's move on to your points 2 and 3.

Regarding 3, I agree that if you have a vastly super-human AI that was not designed with security mindset in mind, then the outcome will be very bad. However, for an AI that is only incrementally more powerful than previous, already-understood agents, I think that incremental improvements on existing levels of rigour displayed by top AI researchers are sufficient, and also lower than the levels of rigour you, Daniel, would want.

For example, many putative flaws with superintelligence involve a failure of generalization from the training and test environments, where the AI appears to behave benignly, to the real world, where the AI allegedly causes massive harm. However, I think that AI researchers think rigorously enough about generalization failures---if they did not, then things like [neural architecture search](https://arxiv.org/abs/1802.03268) and machine learning more broadly would fail to generalize from the training set to the test set.

**Daniel, not quite getting the point**: This feels quite cruxy for me. I believe that top AI researchers can see problems as they happen. However, I do think that they have significantly less rigour than I would want, because I can see problems that I suspect are likely to come up with many approaches, such as [inner alignment failures](https://arxiv.org/abs/1906.01820), and these problems weren't brought to my attention by the AI research community, but rather by the more security-mindset-focussed contingent of the AI alignment research community. If this is the case, it seems like a big win to find these problems early and work on them now.

**Rohin**: If inner alignment failures are a big problem, I expect that we would find that out in ~5 years, and that a unit of work done on it now is worth ~10-20% of a unit of work done on it after we have a concrete example of how they are a problem. Given this, instead of working on those sorts of problems now, I think that it makes sense to work on things that we actually know are problems, and have a hope of solving in the present, such as communicating human intent to neural networks.

**Daniel**: I'm skeptical of those numbers. At any rate, it seems to me that there might be problems that you can solve in that way, but that there are also some things that you need to get right from the beginning. Furthermore, I think that you can form decent models about what these things are, and examples include the [Agent Foundations agenda](https://intelligence.org/technical-agenda/) as well as the more theoretical aspects of [iterated distillation and amplification research](https://ai-alignment.com/).

**Rohin**: Interesting. I'd like to get down later into our models of what problems need to be done right now, but for now that feels a bit off topic. Instead, I'd like to hear why you believe your point 2, that security mindset is needed to do monitoring, testing, and boxing well.

**Daniel**: Well, I have three reasons to think this:

1. You are plausibly dealing with an AI that is optimizing to pass your test. This is the sort of case where security mindset is required for good reasoning about the system.

2. Your suggestion of monitoring thoughts is quite exciting to me, since it could plausibly detect any adversarial optimization early, but it's hard for me to see how you could be sure that you've done that adequately without the type of thinking produced by security mindset.

3. You are optimizing to create an AI that passes the test by trying a bunch of things and thinking about how to do it. Again, this is a situation where optimization is being done, perhaps to pass the specific tests that you've set, and therefore a situation that you need security mindset to reason correctly about.

**Rohin**: Points 1 and 3 seem solid to me, but I'm not sure about point 2. For instance, it seems like if I could 'read minds' in the way depicted in popular fiction, then by reading the mind of another human all the time, I would be able to detect them trying to take over the world just by reasoning informally about the contents of their thoughts. Do you agree?

**Daniel, answering a slightly different question**: If you mean that I get to hear what's happening in their verbal loop, then I'm not sure that I could detect what people were optimizing for. For instance, it's plausible to me that if you heard the verbal loop of a dictator like [Stalin](https://en.wikipedia.org/wiki/Joseph_Stalin), you would hear a lot about serving his country and helping the workers of the world, and very little about maximizing personal power and punishing people for disagreeing with him.

That being said, it seems to me like the primary part where security mindset is required is in looking at a particular human brain and deducing that there's a verbal loop containing useful information at all.

Well, it's about time to wrap up the conversation. Just to close, here are my cruxes:

- How high is the "default" level of security mindset and rigour? In particular, is it high enough that we should outsource work to the future?
- How much security mindset/rigour does one need to do monitoring, testing, and boxing of incrementally advanced AIs well?
  - The underlying question here is something like how much optimization does a smart AI do itself?
- At any given time, how far apart in capabilities are competing groups?
