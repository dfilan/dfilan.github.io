---
layout: post
title:  "Bayesian inference without priors"
date: 2024-04-24
---

_Epistemic status: party trick_


## Why remove the prior

One famed feature of Bayesian inference is that it involves prior probability distributions. Given an exhaustive collection of mutually exclusive ways the world could be (hereafter called 'hypotheses'), one starts with a sense of how likely the world is to be described by each hypothesis, in the absence of any contingent relevant evidence. One then combines this prior with a likelihood distribution, which for each hypothesis gives the probability that one would see any particular set of evidence, to get a posterior distribution of how likely each hypothesis is to be true given observed evidence. The prior and the likelihood seem pretty different: the prior is looking at the probability of the hypotheses in question, whereas the likelihood is looking at the probability of the evidence (assuming the hypothesis is true).[^1]

Critics of Bayesian inference sometimes denounce the reliance on priors for being subjective or unscientific. Indeed, they are by design meant to describe what one would think without any relevant (contingent) data. One might therefore be tempted to describe a form of Bayesian inference where no special role is played by the prior distribution, as distinct from the likelihood.

Another motivation comes from doing Bayesian calculations by hand. In real-world cases, such as [trying to infer whether the first COVID-19 outbreak spread from a laboratory or human contact with infected animals](https://docs.google.com/document/d/1qzLC55jRfdS55oSqXJZTFItsvFsawWgNlgLxWqhCuyo/edit?usp=sharing), the kind of thinking one does to determine a prior probability distribution is very similar to the kind of thinking one does to determine likelihoods: in both cases, one has some sort of generative model in mind---that is, some sort of probabilistic process of generating worlds---and one is trying to figure out how often worlds produced by this generative model have various properties. This might make one wonder if one could unify the prior and the likelihood.

## How to remove the prior (by turning it into a likelihood)

So, how are we going to do this?

First, a prerequisite. I'm going to be talking about the "odds ratio" form of Bayes' theorem. This involves comparing the ratio of the probabilities of two hypotheses---that is, asking questions like "how many times more likely is the COVID outbreak to be a lab leak (LL) rather than a zoonotic spillover (Zoo), given the evidence E we've seen?". Symbolically, we're asking about P(LL \| E) / P(Zoo \| E). Bayes' theorem tells us that this is equal to P(LL) / P(Zoo) times P(E \| LL) / P(E \| Zoo) - that is, the ratio of the hypotheses' prior probabilities, multiplied by the ratio of the likelihoods of the given evidence under the hypotheses. If we then observed subsequent evidence E', we would want to know P(LL \| E, E') / P(Zoo \| E, E'), and Bayes' theorem says that that's equal to P(LL) / P(Zoo) times P(E \| LL) / P(E \| Zoo) times P(E' \| LL, E) / P(E' \| Zoo, E)---basically, for each additional piece of evidence, we get a new likelihood ratio for the new evidence given the hypotheses and the old evidence.

With that set-up established, I'd like you to imagine a certain way you could come to be doing this calculation. Suppose someone first asks you: "How many times more likely is the first COVID-19 outbreak to have been a lab leak rather than a zoonotic spillover?". However, you're kind of tired and not paying that close attention, so what you hear is "How many times more likely is _mumble_ to have been _mumble_ rather than _mumble_". You know that the speaker made two utterances, that represent some sort of mutually exclusive hypotheses, but you have no idea what's going on beyond that. You are now in the position of wondering how much more likely the referent of utterance 1 (U1) is to be true compared to the referent of utterance 2 (U2).

In this case, I'm going to assume you have a probability distribution over what hypotheses various utterances might mean. I'm also going to make further assumptions about these hypotheses:
1. The hypotheses are all mutually exclusive.[^2]
2. Both utterances "come from the same distribution", meaning that there's no difference between how likely utterances 1 and 2 are to mean various things. That is, P(U1 means H) = P(U2 means H) for all H.
3. The probability that some utterance U is true, conditional on it meaning hypothesis H, is just the probability that H is true. That is, P(U \| U means H) = P(H \| U means H).
4. The probability of any "mundane" event E1 not involving utterances conditional on utterance U being true, U meaning H, and various other utterances meaning various other things, and possibly also on mundane event E2, is equal to the probability of that event given H being true, U meaning H, and various other utterances meaning various other things, and on E2. That is, P(E1 \| U, U means H, U' means H', E2) = P(E \| H, U means H, U' means H', E2).
5. Which utterances mean which things is probabilistically independent of anything else in the world (except for which utterances are true), including which hypotheses are true and which evidence we'd see under which hypotheses. 
6. Furthermore, conditioned on the meaning of utterance U, whether or not U is true is probabilistically independent of the meaning of other utterances.

Assumption 1 lets us treat the hypotheses as usual, assumption 2 encodes that there's no difference between the first and second utterances, assumptions 3 and 4 say that if utterance U means hypothesis H then we can treat "U is true" the same as "H is true", and assumptions 5 and 6 say that learning what various utterances mean doesn't tell you anything about substantive questions about the world. Note: I wouldn't be surprised if there were a more compact way of writing these assumptions, but I don't know what it is.

Now that we have these assumptions, we can do some calculations. First of all: what's our prior ratio over whether U1 or U2 is true? Intuitively, it should be exactly 1, meaning that they're just as likely as each other to be true, because there's no difference between them. Here's a proof of that: P(U1) can be calculated by summing the probability that U1 means H and U1 is true over every hypothesis H. That is, P(U1) = sum over H of P(U1, U1 means H) = sum over H of P(U1 means H)P(U1 \| U1 means H) = sum over H of P(U1 means H) P(H \| U1 means H) = sum over H of P(U1 means H) P(H), where first we used the chain rule of probability, second we used assumption 3, and third we used assumption 5. Likewise, P(U2) = sum over H of P(U2 means H) P(H). Next, we should notice that assumption 2 says that P(U1 means H) is equal to P(U2 means H) for every H. Therefore, P(U1) = sum over H of P(U1 means H) P(H) = sum over H of P(U2 means H) P(H) = P(U2), so P(U1) / P(U2) = 1.

Alright, so our prior ratio is exactly 1. This is great news, because it means that the prior is doing no work in our computation, because multiplying numbers by 1 doesn't change them! We have therefore banished the feared prior from Bayesian statistics.

Next up, revisit the scenario where someone is asking you to compare the probabilities of two hypotheses, but you didn't really pay attention to understand what they mean. Suppose you then think about it more, and you discover that the first utterance meant "The first COVID-19 outbreak was a lab leak" and the second utterance meant "The first COVID-19 outbreak was a zoonotic spillover". How should you update on this evidence? Intuitively, all we've learned is the meanings of the utterances, without learning anything about how COVID-19 actually started, so our posterior ratio should just be P(LL) / P(Zoo), which means our likelihood ratio would have to be the same (given that our prior ratio is 1).

Here's the proof: for utterance 1, the relevant likelihood term is P(U1 means LL and U2 means Zoo \| U1). Using the definition of conditional probability, this is P(U1, U1 means LL, U2 means Zoo) / P(U1). Using the chain rule, we can manipulate this into P(U1 \| U1 means LL, U2 means Zoo) P(U1 means LL, U2 means Zoo) / P(U1). By assumption 6, P(U1 \| U1 means LL, U2 means Zoo) = P(U1 \| U1 means LL), which by assumption 3 is equal to P(LL). Putting that all together, P(U1 means LL and U2 means Zoo \| U1) = P(LL) P(U1 means LL, U2 means Zoo) / P(U1). Similarly, for utterance 2, the relevant likelihood term is P(U1 means LL and U2 means Zoo \| U2), which is equal to P(Zoo) P(U1 means LL, U2 means Zoo) / P(U2). Since P(U1) = P(U2), the likelihood ratio is therefore P(U1 means LL and U2 means Zoo \| U1) / P(U1 means LL and U2 means Zoo \| U2) = P(LL) / P(Zoo).

What's the significance of this? It means that we can recast the P(LL) / P(Zoo) term as a likelihood ratio, rather than a prior ratio.

Finally, we should check that this different formalism doesn't change how we update on evidence. That is, suppose we further observe evidence E. We should multiply our old posterior ratio by P(E \| U1, U1 means LL, U2 means Zoo) / P(E \| U2, U1 means LL, U2 means Zoo). Intuitively, this should just be the likelihood ratio P(E \| LL) / P(E \| Zoo) because we're just doing normal Bayesian inference, and understanding it in terms of updating on the meanings of utterances shouldn't change anything. Formally, we can look at the numerator, P(E \| U1, U1 means LL, U2 means Zoo), and by assumption 4, write it as P(E \| LL, U1 means LL, U2 means Zoo). By assumption 5, this is just P(E \| LL). Similarly, P(E \| U2, U1 means LL, U2 means Zoo) = P(E \| Zoo). Therefore, our new likelihood ratio P(E \| U1, U1 means LL, U2 means Zoo) / P(E \| U2, U2 means LL, U2 means Zoo) = P(E \| LL) / P(E \| Zoo). Therefore, we're updating the same as we used to be. You can also check that this remains true if we get further "mundane" evidence.

## What does this mean?

Basically, this shows that every term in a standard Bayesian inference, including the prior ratio, can be re-cast as a likelihood term in a setting where you start off unsure about what words mean, and have a flat prior over which set of words is true. How should we interpret that fact?

Firstly, I think that there's some kind of interesting mapping to the intuitive experience of doing Bayesian inference in real-world settings. A lot of the initial task of determining what the prior should be involves understanding what the hypotheses actually mean in a probabilistic sense---what kinds of things would have to happen for COVID-19 to have started via a lab leak, and what would that say about the world? That said, it's possible to over-emphasize these similarities. In the toy setting I sketch, you should be asking yourself "If 'COVID-19 was a lab leak' was true, what's the chance that it would have these implications?", which doesn't quite match to the kinds of thinking I'd tend to do.

Secondly, it points to how strange likelihood ratios can be, by turning likelihood ratios into priors. There are other reasons to think that likelihoods are funny things: if the hypothesis in question is false, the likelihood is asking about how likely we would be to see some evidence in a world that doesn't exist, which is a question that may be hard to get data on. There are therefore serious challenges with thinking of likelihood ratios as more "objective" or "scientific" than priors. As Gelman and Robert [say](http://www.stat.columbia.edu/~gelman/research/published/feller8.pdf), "It is perhaps merely an accident of history that skeptics and subjectivists alike strain on the gnat of the prior distribution while swallowing the camel that is the likelihood".

Finally, it points to an interesting extension. In some cases, the meaning of various utterances might tell you something relevant about the world in question. For instance, suppose some utterance is a computer program, and its "meaning" is what it evaluates to. Learning this might serve as evidence about what other computer programs evaluate to (e.g. those computer programs that use your 'utterance' as a subroutine), meaning that one could not apply Bayesian statistics quite so simply in this setting.

## A challenge

This construction was inspired by noting the similarity between the calculation of the prior term and the likelihood term in Bayes' formula. The way it highlighted that similarity was by turning the prior term into a likelihood. But is there some way of re-casting the problem so that the likelihood term becomes a prior, and the prior term becomes a likelihood?

---

[^1]: Compare priors and posteriors, which are both about the probability of the hypotheses in question, and are therefore more similar---you can use a posterior as a new prior when facing further evidence.

[^2]: This can actually be relaxed without changing our results: we can instead suppose that you're not sure which way the speaker is carving up "hypotheses", but that once they pick such a way, the two hypotheses they state will be mutually exclusive.
