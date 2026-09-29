Note that the Hausdorff property was used in the preceding proof when we said that a compact subset of $Y$ is closed.

In the study of functional analysis it is often the case that the mathematician is presented with a set that has two topologies. It is useful to know how properties of one topology relate to the other and when the two topologies are, in fact, one.

If $X$ is a set and $\mathcal{T}_1,\mathcal{T}_2$ are two topologies on $X$, say that $\mathcal{T}_2$ is *larger* or *stronger* than $\mathcal{T}_1$ if $\mathcal{T}_2\supseteq\mathcal{T}_1$; in this case you may also say that $\mathcal{T}_1$ is *smaller* or *weaker*. In the literature there is also an unfortunate nomenclature for these concepts; the words “finer” and “coarser” are used.

The following result is easy to prove (it is an exercise) but it is enormously useful in discussing a set with two topologies.

**2.9. Lemma.** *If $\mathcal{T}_1,\mathcal{T}_2$ are topologies on $X$, then $\mathcal{T}_2$ is larger than $\mathcal{T}_1$ if and only if the identity map $i:(X,\mathcal{T}_2)\to(X,\mathcal{T}_1)$ is continuous.*

**2.10. Proposition.** *Let $\mathcal{T}_1,\mathcal{T}_2$ be topologies on $X$ and assume that $\mathcal{T}_2$ is larger than $\mathcal{T}_1$.*

(a) *If $F$ is $\mathcal{T}_1$-closed, $F$ is $\mathcal{T}_2$-closed.*

(b) *If $f:Y\to(X,\mathcal{T}_2)$ is continuous, then $f:Y\to(X,\mathcal{T}_1)$ is continuous.*

(c) *If $f(X,\mathcal{T}_1)\to Y$ is continuous, then $f:(X,\mathcal{T}_2)\to Y$ is continuous.*

(d) *If $K$ is $\mathcal{T}_2$-compact, then $K$ is $\mathcal{T}_1$-compact.*

(e) *If $X$ is $\mathcal{T}_2$-compact, then $\mathcal{T}_1=\mathcal{T}_2$.*

**Proof.** (b) Note that $f:Y\to(X,\mathcal{T}_1)$ is the composition of $f:Y\to(X,\mathcal{T}_2)$ and $i:(X,\mathcal{T}_2)\to(X,\mathcal{T}_1)$ and use Lemma 2.9.

(d) Use Lemma 2.9.

(e) Use Lemma 2.9 and Proposition 2.8.

The remainder of the proof is an exercise. $\blacksquare$
