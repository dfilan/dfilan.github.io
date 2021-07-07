---
layout: post
title: "A second example of conditional orthogonality in finite factored sets"
date: 2021-07-06
---

Reader's note: It looks like the math on my website is all messed up. To read it better, I suggest checking it out on the [Alignment Forum](https://www.alignmentforum.org/posts/GFGNwCwkffBevyXR2/a-second-example-of-conditional-orthogonality-in-finite).

Yesterday, I wrote a [post](https://danielfilan.com/2021/07/05/simple_example_conditional_orthogonality_ffs.html) that gave an example of conditional non-orthogonality in [finite factored sets](https://www.alignmentforum.org/s/kxs3eeEti9ouwWFzr/p/N5Jm6Nj4HkNKySA5Z). I encourage you to read that post first. However, I'm kind of dissatisfied with it because it doesn't show any interesting cases of conditional orthogonality (despite the title seeming to promise that). So I'd like to show you one today.

First, let's imagine that Alice is a person who has some height. Bob and Charlie both measure her height, and take note of the measurements. However, their measuring instruments have independent sources of error, such that neither gets exactly the right answer. In this world, Bob's measurement is not independent of Charlie's measurement, because they'll both be pretty close - the error isn't that big. However, once you know Alice's height, they will be independent, because given that knowledge, learning Bob's measurement doesn't tell you anything about Charlie's measurement. Below, we'll see how we can formalize that in the language of finite factored sets.

Our finite factored set will be the set of tuples $$(a, \epsilon_b, \epsilon_c)$$, and the basis factors will be $$A$$, which partitions the tuples by their value of $$a$$, $$E_B$$, which partitions them by their value of $$\epsilon_b$$, and $$E_C$$, which partitions them by their value of $$\epsilon_c$$. These represent Alice's height, and the error that Bob's and Charlie's machines respectively introduce. Note that you might have imagined we'd have the basic factors as Alice's height, Bob's measurement, and Charlie's measurement, but then these wouldn't be probabilistically or logically independent, and so would violate the assumptions that go into modelling things as finite factored sets. [footnote 1]

Next, we'll define the function $$b(a, \epsilon_b, \epsilon_c) = a + \epsilon_b$$, which gives the height that Bob measures, and the partition $$B$$ which groups tuples with the same value of $$b$$ together. Similarly, we'll define $$c(a, \epsilon_b, \epsilon_c) = a + \epsilon_c$$, which tells us the height that Charlie measures, and the partition $$C$$ that groups tuples together by their value of $$c$$.

What's the history of $$B$$? Well, it's the smallest set of factors such that if we know the 'value' of the factors, then we know the 'value' of $$B$$, and that's $$\{A, E_B\}$$. Similarly, the history of $$C$$ is $$\{A, E_C\}$$. So $$B$$'s and $$C$$'s histories have $$A$$ in common, and therefore aren't orthogonal.

Now, let's consider the set $$A_2 = \{(a, \epsilon_b, \epsilon_c) \mid a = 2\}$$, which represents the worlds where Alice is 2 metres tall, and check out the conditional histories. The conditional history of $$B$$ in $$A_2$$ is the smallest set of factors such that once you're in $$A_2$$, knowing the 'values' of those factors tells you the 'value' of $$B$$, and that includes all the factors that are 'entangled' with those factors by the set $$A_2$$ - for more detail, check out the [previous post](https://danielfilan.com/2021/07/05/simple_example_conditional_orthogonality_ffs.html). In this case, the conditional history of $$B$$ is just $$\{E_B\}$$: Once you're in $$A_2$$, knowing $$\epsilon_b$$ is enough to tell you the value of $$b$$. Furthermore, the only thing you need to know to figure out whether something's in $$A_2$$ is $$a$$, so $$\{E_B\}$$ also satisfies the second condition: if the 'value' of $$E_B$$ at some tuple is compatible with being in $$A_2$$ (which is always true), and the 'values' of $$A$$ and $$E_C$$ are jointly compatible with being in $$A_2$$, then you must be in $$A_2$$. Similarly, the conditional history of $$C$$ given $$A_2$$ is $$\{E_C\}$$. So, the conditional histories don't intersect, and $$B$$ is orthogonal to $$C$$ given $$A_2$$.

Hopefully this post was useful both in giving you a better sense of conditional orthogonality, and in illustrating how to model things with finite factored sets.

[footnote 1] Note that we could 'change coordinates' and have the underlying set be tuples $$(a,b,c)$$ - Alice's height, Bob's measurement, and Charlie's measurement - and the factors being:
- $$A$$, the partition of points according to their value of $$a$$
- $$E_B$$, the partition of points according to their value of $$b - a$$
- $$E_C$$, the partition of points according to their value of $$c - a$$

This would give exactly the same results as those in the main post!
