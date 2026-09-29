If $\mathcal M$ is a linear manifold in a vector space $\mathcal X$ (a Banach space or not), then a Hamel-basis argument can be fashioned to produce a linear manifold $\mathcal N$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal X$. So the requirement in the definition that $\mathcal M$ and $\mathcal N$ be closed subspaces of the Banach space $\mathcal X$ makes the existence problem more interesting. Also, since we are dealing with the category of Banach spaces, all definitions should involve only objects in that category.

If $\mathcal M$ and $\mathcal N$ are algebraically complemented closed subspaces of a normed space $\mathcal X$, then $A:\mathcal M\oplus_1\mathcal N\to\mathcal X$ defined by $A(m\oplus n)=m+n$ is a linear bijection. Also, $\|A(m\oplus n)\|=\|m+n\|\leqslant\|m\|+\|n\|=\|m\oplus n\|$. Hence $A$ is bounded. Say that $\mathcal M$ and $\mathcal N$ are *topologically complemented* if $A$ is a homeomorphism; equivalently, if $\|\!\|m+n\|\!\|=\|m\|+\|n\|$ is an equivalent norm. If $\mathcal X$ is a Banach space, then the Inverse Mapping Theorem implies $A$ is a homeomorphism. This proves the following.

**13.1. Theorem.** *If two subspaces of a Banach space are algebraically complementary, then they are topologically complementary.*

This permits us to speak of *complementary subspaces* of a Banach space without modifying the term. The proof of the next result is left to the reader.

**13.2. Theorem.** (a) *If $\mathcal M$ and $\mathcal N$ are complementary subspaces of a Banach space $\mathcal X$ and $E:\mathcal X\to\mathcal X$ is defined by $E(m+n)=m$ for $m$ in $\mathcal M$ and $n$ in $\mathcal N$, then $E$ is a continuous linear operator such that $E^2=E$, $\operatorname{ran}E=\mathcal M$, and $\ker E=\mathcal N$.* (b) *If $E\in\mathcal B(\mathcal X)$ and $E^2=E$, then $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$ are complementary subspaces of $\mathcal X$.*

If $\mathcal M\leqslant\mathcal X$ and $\mathcal M$ is complemented in $\mathcal X$, its complementary subspace may not be unique. Indeed, finite dimensional spaces furnish the necessary examples.

A result due to R.S. Phillips [1940] is that $c_0$ is not complemented in $l^\infty$. A straightforward proof of this can be found in Whitley [1966]. Murray [1937] showed that $l^p$, $p\ne2$, $p>1$ has uncomplemented subspaces. This seems to be the first paper to exhibit uncomplemented subspaces of a Banach space.

Lindenstrauss [1967] showed that if $\mathcal M$ is an infinite dimensional subspace of $l^\infty$ that is complemented in $l^\infty$, then $\mathcal M$ is isomorphic to $l^\infty$. This same result holds if $l^\infty$ is replaced by $l^p$, $1\leqslant p<\infty$, $c$, or $c_0$.

Does there exist a Banach space $\mathcal X$ such that every closed subspace of $\mathcal X$ is complemented? Of course, if $\mathcal X$ is a Hilbert space, then this is true. But are there any Banach spaces that have this property and are not Hilbert spaces? Lindenstrauss and Tzafriri [1971] proved that if $\mathcal X$ is a Banach space and every subspace of $\mathcal X$ is complemented, then $\mathcal X$ is isomorphic to a Hilbert space.
