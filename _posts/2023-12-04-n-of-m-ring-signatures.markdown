---
layout: post
title:  "n of m ring signatures"
date: 2023-12-04
---

A normal cryptographic signature associated with a message and a public key lets you prove to the world that it was made by someone with access to the private key associated with the known public key, without revealing that private key. You can read about it on Wikipedia [here](https://en.wikipedia.org/wiki/Digital_signature).

A ring signature associated with a message and a set of public keys lets you prove to the world that it was made by someone with access to the message and one private key associated to one of the public keys in the set, but nobody will be able to tell which public key it was. This lets you say something semi-anonymously, which is neat. It's also used in the private cryptocurrency Monero. You can read about them on Wikipedia [here](https://en.wikipedia.org/wiki/Ring_signature).

Here's a thing that would be better than a ring signature: a signature that proved that it was made by a subset of public keys of a certain size. In my head, I was calling this an n of m ring signature for a while. But when I googled "n of m ring signature", nothing came up. It turns out this is because in the literature, it's called a "threshold ring signature", a "k of n ring signature", or a "t of n ring signature" instead. I think perhaps the first paper about it is [this one](https://www.iacr.org/archive/crypto2002/24420467/24420467.pdf), but I haven't checked very hard.

Anyway: I would like to make it so that when you search for n-of-m ring signatures online, you find a thing telling you that you should instead search for "threshold ring signature". Hence this post.
