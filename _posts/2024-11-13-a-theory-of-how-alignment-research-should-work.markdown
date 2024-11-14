---
layout: post
title:  "A theory of how alignment research should work"
date: 2024-11-13
---

Epistemic status:
- I listened to [the Dwarkesh episode with Gwern](https://www.dwarkeshpatel.com/p/gwern-branwen) and started attempting to think about life, the universe, and everything 
- less than an hour of thought has gone into this post
- that said, it comes from a background of me thinking for a while about how the field of AI alignment should relate to agent foundations research

Maybe obvious to everyone but me, or totally wrong (this doesn't really grapple with the challenges of working in a domain where an intelligent being might be working against you), but:
- we currently don't know how to make super-smart computers that do our will
  - this is not just a problem of having a design that is not feasible to implement: we do not even have a sense of what the design would be
  - I'm trying to somewhat abstract over intent alignment vs control approaches, but am mostly thinking about intent alignment
  - I have not thought that much about societal/systemic risks very much, and this post doesn't really address them.
- ideally we would figure out how to do this
- the closest traction that we have: deep learning seems to work well in practice, altho our theoretical knowledge of why it works so well or how capabilities are implemented is lagging
- how should we proceed? Well:
  - thinking about theory alone has not been practical
  - probably we need to look at things that exhibit alignment-related phenomena and understand them, and that will help us develop the requisite theory
    - said things are probably neural networks
  - there are two ways we can look at neural networks: their behaviour, and their implementation.
  - looking at behaviour is conceptually straightforward, and valuable, and being done
  - looking at their implementation is less obvious
  - what we need is tooling that lets us see relevant things about how neural networks are working
  - such tools (e.g. SAEs) are not impossible to create, but it is not obvious that their outputs tell us quantities that are actually of interest
  - in order to discipline the creation of such tools, we should demand that they help us understand models in ways that matter
    - see Stephen Casper's [engineer's interpretability sequence](https://www.alignmentforum.org/s/a6ne2ve5uturEEQK7), [Jason Gross on compact proofs](https://arxiv.org/abs/2406.11779)
  - once we get such tools, we should be trying to use them to understand alignment-relevant phenomena, to build up our theory of what we want out of alignment and how it might be implemented
    - this is also a thing that looking at the external behaviour of models in alignment-relevant contexts should be doing
- so should we be just doing totally empirical things? No.
  - firstly, we need to be disciplined along the way by making sure that we are looking at settings that are in fact relevant to the alignment problem, when we do our behavioural analysis and benchmark our interpretability tools. This involves having a model of what situations are in fact alignment-relevant, what problems we will face as models get smarter, etc
  - secondly, once we have the building blocks for theory, ideally we will put them together and make some actual theorems like "in such-and-such situations models will never become deceptive" (where 'deceptive' has been satisfactorily operationalized in a way that suffices to derive good outcomes from no deception and relatively benign humans)
- I'm imagining the above as being analogous to an imagined history of statistical mechanics (people who know this history or who have read ["inventing temperature"](https://global.oup.com/academic/product/inventing-temperature-9780195337389) should let me know if I'm totally wrong about it):
  - first we have steam engines etc
  - then we figure out that 'temperature' and 'entropy' are relevant things to track for making the engines run
  - then we relate temperature, entropy, and pressure
  - then we get a good theory of thermodynamics 
  - then we develop statistical mechanics
- exceptions to "theory without empiricism doesn't work":
  - thinking about [deceptive mesa-optimization](https://arxiv.org/abs/1906.01820)
  - [RLHF failures](https://www.lesswrong.com/posts/DS3TTpCEFKduC8zPy/paper-blogpost-when-your-ais-deceive-you-challenges-with)
  - [CIRL](https://arxiv.org/abs/1606.03137) analysis
- lesson of above: theory does seem to help us analyze some issues and raise possibilities 
