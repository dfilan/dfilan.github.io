---
layout: post
title:  "Watermarking considered overrated?"
date: 2023-07-31
---

_Status: a slightly-edited copy-paste of [a ~~Twitter~~ X thread](https://twitter.com/dfrsrchtwts/status/1682529184881709056) I quickly dashed off a week or so ago._

Here's a thought I'm playing with that I'd like feedback on: I think [watermarking](https://arxiv.org/abs/2301.10226) large language models is probably overrated. Most of the time, I think what you want to know is "is this text endorsed by the person who purportedly authored it", which can be checked with digital signatures. Another big concern is that people are able to cheat on essays. This is sad. But what do we give up by having watermarking?

Well, as far as I can tell, if you give people access to model internals - certainly weights, certainly logprobs, but maybe even last-layer activations if they have enough - they can bypass the watermarking scheme. This is even sadder - it means you have to strictly limit the set of people who are able to do certain kinds of research that could be pretty useful for safety. In my mind, that makes it not worth the benefit.

What could I be missing here?
1. Maybe we can make watermarking compatible with releasing model info, e.g. by baking it into the weights?
2. Maybe the info I want to be available is inherently dangerous, by e.g. allowing people to fine-tune scary models?
3. Maybe I'm missing some important reasons we care about watermarking, that make the cost-benefit analysis look better? E.g. avoiding a situations where AIs become really good at manipulation, so good that you don't want to inadvertently read AI-generated text, but we don't notice until too late? 

Anyway there's a good shot I don't know what I'm missing, so let me know if you know what it is.

Postscript: Someone has pointed me to [this paper](https://arxiv.org/abs/2012.08726) that purports to bake a watermark into the weights. I can't figure out how it works (at least not at twitter-compatible speeds), but if it does, I think that would alleviate my concerns.
