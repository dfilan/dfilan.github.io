---
layout: post
title:  "A Nice Representation of the Laplacian"
date:   2022-02-11
---

_Epistemic status: some proofs here may well contain a small bug._

The Laplacian of a function from n-dimensional space to the real line is a generalization of the second derivative of a normal function: specifically, it's the sum of second derivatives of the function along each dimension. One day, I recall coming across a theorem that said that the Laplacian of a function was equal to something like the limit of the average function value on a shell around a point, minus the function value at that point, divided by the squared radius of the shell. This is a nice theorem, because it connects the Laplacian to one of my favourite mathematical objects, the graph Laplacian. However, I later couldn't find this theorem anywhere. Yesterday, I decided to re-derive the theorem, and today I decided to write it up. You can see the theorem and its proof [here](/pdfs/laplacian_representation.pdf). Do let me know if there are any errors I should fix.
