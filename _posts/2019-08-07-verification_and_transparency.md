---
layout: post
title:  "Verification and Transparency"
date: 2019-08-07
---

_Epistemic status: I've thought about this topic in general for a while, and recently spent half an hour thinking about it in a somewhat focussed way._

_Cross-posted to the [AI Alignment Forum](https://www.alignmentforum.org/posts/n3YRDJYCnQcDAw29G/verification-and-transparency)._

Verification and transparency are two kinds of things you can do to or with a software system. Verification is where you use a program to prove whether or not a system of interest has a property of interest. Transparency is where you use tools to make it clear how the software system works. I claim that these are intimately related.

## Examples of verification

- Proving that an alleged compiler actually implements the desired semantics of a system (for example, [this verified implementation of ML](https://cakeml.org/)).
- Proving that a neural network's classifications of a set of possible inputs are invariant under small perturbations to those inputs (for example, [the system described in this paper](http://cs229.stanford.edu/proj2018/report/101.pdf)).

## Example of transparency

- Sharing the source code of a program, rather than just compiled machine code (as encouraged by the [open-source software movement](https://en.wikipedia.org/wiki/Open-source-software_movement)).
- Demonstrating the types of inputs that neurons in a neural network are sensitive to (techniques like this are discussed in the fantastic [Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/) blog post).

## How verification and transparency are sort of the same

Apart from aesthetic cases, the purpose of transparency is to make the system transparent to some audience, so that members of that audience can learn about the system, and have that knowledge be intimately and necessarily entangled with the actual facts about the system. In other words, the purpose is to allow the users to verify certain properties of the system. As such, you might wonder why typical transparency methods look different than typical verification methods, which also have as a purpose allowing users to verify certain properties of a system.

## How verification and transparency are different

Verification systems typically work by having a user specify a proposition to be verified, and then attempting to prove or disprove it. Transparency systems, on the other hand, provide an artefact that makes it easier to prove or disprove many properties of interest. It's also the case that engagement with the 'transparency artefact' need not take the form of coming up with a proposition and then attempting to prove or disprove it: one may well instead interleave proving steps and specification steps, by looking at the artefact, having interesting lemmas come to mind, verifying those, which then inspire more lemmas, and so on.

## Intermediate things

Thinking about this made me realise that many sorts of things both serve verification and transparency purposes. Examples:
- Type signatures in a strongly typed language can be seen as a method of ensuring that the compiler proves that certain errors cannot occur, while also giving a human reading the program a better sense of what various functions do.
- A mathematics textbook containing a large numbers of theorems, lemmas, and proofs is made by proving a large number of propositions, and allows a reader to gain an understanding of the relevant mathematical objects by perusing the theorems and lemmas, as well as by looking at the structure of the proofs.

## Addendum (added 2019-08-26)

LessWrong user justinpombrio wrote a comment to this post which included the line:

> [Y]our examples only seem to support that transparency _enables_ verification. Is that closer to what you were trying to say?

My response:

> No, but you've picked up a weakness in my exposition (or rather something that I just forgot to say). Verification also enables transparency: by verifying a large number of properties of a system, one provides a 'view' for a user to understand the system, just as a transparency method can itself be thought of as verifying some properties of a system: for example, sharing the source code of a binary verifies that that source code compiles into the given binary, and that the binary when executed will use such and such memory (if the source code is written in a language that makes that explicit), etc. As such, one can think of both verification and transparency as providing artefacts that prove certain properties of systems, although they 'prove' these properties in somewhat different ways.
