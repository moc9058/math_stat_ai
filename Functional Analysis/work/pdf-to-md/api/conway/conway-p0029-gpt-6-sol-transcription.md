# §4. Orthonormal Sets of Vectors and Bases

It will be shown in this section that, as in Euclidean space, each Hilbert space can be coordinatized. The vehicle for introducing the coordinates is an orthonormal basis. The corresponding vectors in $\mathbb{F}^{d}$ are the vectors $\{e_{1},e_{2},\ldots,e_{d}\}$, where $e_{k}$ is the $d$-tuple having a 1 in the $k$th place and zeros elsewhere.

**4.1. Definition.** An *orthonormal* subset of a Hilbert space $\mathcal{H}$ is a subset $\mathcal{E}$ having the properties: (a) for $e$ in $\mathcal{E}$, $\|e\|=1$; (b) if $e_{1},e_{2}\in\mathcal{E}$ and $e_{1}\ne e_{2}$, then $e_{1}\perp e_{2}$.

A *basis* for $\mathcal{H}$ is a maximal orthonormal set.

Every vector space has a Hamel basis (a maximal linearly independent set). The term “basis” for a Hilbert space is defined as above and it relates to the inner product on $\mathcal{H}$. For an infinite-dimensional Hilbert space, a basis is never a Hamel basis. This is not obvious, but the reader will be able to see this after understanding several facts about bases.

**4.2. Proposition.** *If $\mathcal{E}$ is an orthonormal set in $\mathcal{H}$, then there is a basis for $\mathcal{H}$ that contains $\mathcal{E}$.*

The proof of this proposition is a straightforward application of Zorn’s Lemma and is left to the reader.

**4.3. Example.** Let $\mathcal{H}=L_{\mathbb{C}}^{2}[0,2\pi]$ and for $n$ in $\mathbb{Z}$ define $e_{n}$ in $\mathcal{H}$ by $e_{n}(t)=(2\pi)^{-1/2}\exp(int)$. Then $\{e_{n}:n\in\mathbb{Z}\}$ is an orthonormal set in $\mathcal{H}$. (Here $L_{\mathbb{C}}^{2}[0,2\pi]$ is the space of complex-valued square integrable functions.)

It is also true that the set in (4.3) is a basis, but this is best proved after a bit of theory.

**4.4. Example.** If $\mathcal{H}=\mathbb{F}^{d}$ and for $1\leq k\leq d$, $e_{k}=$ the $d$-tuple with 1 in the $k$th place and zeros elsewhere, then $\{e_{1},\ldots,e_{d}\}$ is a basis for $\mathcal{H}$.

**4.5. Example.** Let $\mathcal{H}=l^{2}(I)$ as in Example 1.7. For each $i$ in $I$ define $e_{i}$ in $\mathcal{H}$ by $e_{i}(i)=1$ and $e_{i}(j)=0$ for $j\ne i$. Then $\{e_{i}:i\in I\}$ is a basis.

The proof of the next result is left as an exercise (see Exercise 5). It is very useful but the proof is not difficult.

**4.6. The Gram–Schmidt Orthogonalization Process.** *If $\mathcal{H}$ is a Hilbert space and $\{h_{n}:n\in\mathbb{N}\}$ is a linearly independent subset of $\mathcal{H}$, then there is an orthonormal set $\{e_{n}:n\in\mathbb{N}\}$ such that for every $n$, the linear space of $\{e_{1},\ldots,e_{n}\}$ equals the linear span of $\{h_{1},\ldots,h_{n}\}$.*

Remember that $\bigvee A$ is the closed linear span of $A$ (Exercise 2.4).
