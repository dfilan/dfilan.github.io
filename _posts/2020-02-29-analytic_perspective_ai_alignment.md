---
layout: post
title:  "An Analytic Perspective on AI Alignment"
date:   2020-02-29
---

_Cross-posted to the [AI Alignment Forum](https://www.alignmentforum.org/posts/8GdPargak863xaebm/an-analytic-perspective-on-ai-alignment)._

This is a perspective I have on how to do useful AI alignment research. Most perspectives I'm aware of are constructive: they have some blueprint for how to build an aligned AI system, and propose making it more concrete, making the concretisations more capable, and showing that it does in fact produce an aligned AI system. I do not have a constructive perspective - I'm not sure how to build an aligned AI system, and don't really have a favourite approach. Instead, I have an analytic perspective. I would like to understand AI systems that are built. I also want other people to understand them. I think that this understanding will hopefully act as a 'filter' that means that dangerous AI systems are not deployed. The following dot points lay out the perspective.

Since the remainder of this post is written as nested dot points, some readers may prefer to read it in [workflowy](https://workflowy.com/s/an-analytical-perspe/eU45Fsjd7lzidjM8).

## Background beliefs

- I am imagining a future world in which powerful AGI systems are made of components roughly like neural networks (either feedforward or recurrent) that have a large number of parameters.
- Futhermore, I'm imagining that the training process of these ML systems does not provide enough guarantees about deployment performance.
  - In particular, I'm supposing that systems are being trained based on their ability to deal with simulated situations, and that that's insufficient because deployment situations are hard to model and therefore simulate.
    - One reason that they are hard to model is the complexities of the real world.
	  - The real world might be intrinsically difficult to model for the relevant system. For instance, it's difficult to simulate all the situations in which the CEO of Amazon might find themselves.
	  - Another reason that real world situations may be hard to model is that they are dependent on the final trained system.
	    - The trained system may be able to affect what situations it ends up in, meaning that situations during earlier training are unrepresentative.
	    - Parts of the world may be changing their behaviour in response to the trained system...
		  - in order to exploit the system.
		  - by learning from the system's predictions.
	  - The real world is also systematically different than the trained world: for instance, while you're training, you will never see the factorisation of RSA-2048 (assuming you're training in the year 2020), but in the real world you eventually will.
	    - This is relevant because you could imagine [mesa-optimisers](https://arxiv.org/abs/1906.01820) appearing in your system that choose to act differently when they see such a factorisation.				
- I'm imagining that the world is such that if it's simple for developers to check if an AI system would have disastrous consequences upon deployment, then they perform this check, and fail to deploy if the check says that it would.

## Background desiderata

- I am mostly interested in allowing the developers of AI systems to determine whether their system has the cognitive ability to cause human extinction, and whether their system might try to cause human extinction.
  - I am not primarily interested in reducing the probabilities of other ways in which AI systems could cause humanity to go extinct, such as research groups intentionally behaving badly, or an uncoordinated set of releases of AI systems that interact in negative ways. 
	- That being said, I think that pursuing research suggested by this perspective could help with the latter scenario, by making it clear which interaction effects might be present.
- I want this determination to be made before the system is deployed, in a 'zero-shot' fashion, since this minimises the risk of the system actually behaving badly before you can detect and prevent it.

## Transparency

- The type of transparency that I'm most excited about is mechanistic, in a sense that I've described [elsewhere](https://www.lesswrong.com/posts/3kwR2dufdJyJamHQq/mechanistic-transparency-for-machine-learning).
- The transparency method itself should be based on a trusted algorithm, as should the method of interpreting the transparent artefact.
  - In particular, these operations should not be done by a machine learning system, unless that system itself has already been made transparent and verified.
    - This could be done [amplification-style](https://ai-alignment.com/iterated-distillation-and-amplification-157debfd1616).
- Ideally, models could be regularised for transparency during training, with little or no cost to performance.
  - This would be good because by default models might not be very transparent, and it might be hard to hand-design very transparent models that are also capable.
    - I think of this as what one should derive from Rich Sutton's [bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
  - This will be easier to do if the transparency method is simpler, more 'mathematical', and minimally reliant on machine learning.
  - You might expect little cost to performance since neural networks can often reach high performance given constraints, as long as they are deep enough.
    - [This paper](https://arxiv.org/abs/1804.08838) on the intrinsic dimension of objective landscapes shows that you can constrain neural network weights to a low-dimensional subspace and still find good solutions.
    - [This paper](https://arxiv.org/abs/1908.01755) argues that there are a large number of models with roughly the same performance, meaning that ones with good qualities (e.g. interpretability) can be found.
  - [This paper](https://arxiv.org/abs/1711.06178) applies regularisation to machine learning models that ensures that they are represented by small decision trees.
- The transparency method only has to reveal useful information to developers, not to the general public.
  - This makes the problem easier but still difficult.
  - Presumably developers will not deploy catastrophically terrible systems, since catastrophes are usually bad for most people, and I'm most interested in averting catastrophic outcomes.

## Foundations

- In order for the transparency to be useful, practitioners need to know what problems to look for, and how to reason about these problems.
- I think that an important part of this is 'agent foundations', by which I broadly mean a theory of what agents should look like, and what structural facts about agents could cause them to display undesired behaviour.
  - Examples:
	- Work on [mesa-optimisation](https://arxiv.org/abs/1906.01820)
	- Utility theory, e.g. the [von Neumann-Morgenstern theorem](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem)
	- Methods of detecting which agents are likely to be intelligent or dangerous.
- For this, it is important to be able to look at a machine learning system and learn if (or to what degree) it is agentic, detect belief-like structures and preference-like structures (or to deduce things analogous to beliefs and preferences), and learn other similar things.
  - This requires structural definitions of the relevant primitives (such as agency), not subjective or performance-based definitions.
	- By 'structural definitions', I mean definitions that refer to facts that are easily accessible about the system before it is run.
	- By 'subjective definitions', I mean definitions that refer to an observer's beliefs or preferences regarding the system.
	- By 'performance-based definitions', I mean definitions that refer to facts that can be known about the system once it starts running.
	- Subjective definitions are inadequate because they do not refer to easily-measurable quantities.
	- Performance-based definitions are inadequate because they can only be evaluated once the system is running, when it could already pose a danger, violating the "zero-shot" desideratum.
	- Structural definitions are required because they are precisely the definitions that are not subjective or performance-based that also only refer to facts that are easly accessible, and therefore are easy to evaluate whether a system satisfies the definition.
    - As such, definitions like "an agent is a system whose behaviour can't usefully be predicted mechanically, but can be predicted by assuming it near-optimises some objective function" (which was proposed in [this paper](https://arxiv.org/abs/1805.12387)) are insufficient because they are both subjective and performance-based.
	- It is possible to turn subjective definitions into structural definitions trivially, by asking a human about their beliefs and preferences. This is insufficient.
	  - e.g. "X is a Y if you are scared of it" can turn to "X is a Y if the nearest human to X, when asked if they are scared of X, says 'yes'".
	  - It is insufficient because such a definition doesn't help the human form their subjective beliefs and impressions.
    - It is also possible to turn subjective definitions that only depend on beliefs into structural definitions by determining which circumstances warrant a rational being to have which beliefs. This is sufficient.
      - Compare the subjective definition of temperature as "the derivative of a system's energy with respect to entropy at fixed volume and particle number" to the objective definition "equilibrate the system with a thermometer, read it off the thermometer". For a rational being, these two definitions yield the same temperature for almost all systems.

## Relation between transparency and foundations

- The agent foundations theory should be informed by transparency research, and vice versa.
  - This is because the information that transparency methods can yield should be all the information that is required to analyse the system using the agent foundations theory.
  - Both lines of research can inform the other.
    - Transparency researchers can figure out how to reveal the information required by agent foundations theory, and detect the existence of potential problems that agent foundations theory suggests might occur given certain training procedures.
    - Agent foundations researchers can figure out what is implied by the information revealed by existing transparency tools, and theorise about problems that transparency researchers detect.

## Criticisms of the perspective

- It isn't clear if neural network transparency is possible.
  - More specifically, it seems imaginable that some information required to usefully analyse an AI system cannot be extracted from a typical neural network in polynomial time.
- It isn't clear that relevant terms from agency theory can in fact be well-defined.
  - E.g. "optimisation" and "belief" have eluded a satisfactory computational grounding for quite a while.
  - Relatedly, the philosophical question of which physical systems enable which computations has not to my mind been satisfactorily resolved. See [this](https://plato.stanford.edu/entries/computation-physicalsystems/) relevant SEP article.
- An easier path to transparency than the "zero-shot" approach might be to start with simpler systems, observe their behaviour, and slowly scale them up. As you see problems, stop scaling up the systems, and instead fix them so the problems don't occur.
  - I disagree with this criticism.
    - At one point, it's going to be the first time you use a system of a given power in a domain, and the problems caused by the system might be discontinuous with its power, meaning that they would be hard to predict.
      - Especially if the power of the system increases discontinously.
      - It is plausibly be the case that systems that are a bit 'smarter than humanity' are discontinuously more problematic than those that are a bit less 'smart than humanity'.
- One could imagine giving up the RL dream for something like debate, where you really can get guarantees from the training procedure.
  - I think that this is not true, and that things like debate require transparency tools to work well, so as to let debaters know when other debaters are being deceitful. An argument for an analogous conclusion can be found in evhub's post on [Relaxed adversarial training for inner alignment](https://www.lesswrong.com/posts/9Dy5YRaoCxH9zuJqa/relaxed-adversarial-training-for-inner-alignment).
- One could imagine inspecting training-time reasoning and convincing yourself that way that future reasoning will be OK.
  - But reasoning could look different in different environments.
- This perspective relies on things continuing to look pretty similar to current ML.
  - This would be alleviated if you could come up with some sort of sensible theory for how to make systems transparent.
  - I find it plausible that the devolpment of such a theory should start with people messing around and doing things with systems they have.
- Systems should be transparent to all relevant human stakeholders, not just developers.
  - Sounds right to me - I think people should work on this broader problem. But:
    - I don't know how to solve that problem without making them transparent to developers initially.
    - I have ideas about how to solve the easier problem.
