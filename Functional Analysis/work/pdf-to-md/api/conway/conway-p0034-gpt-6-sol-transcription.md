13. Let $\mathcal E$ be an orthonormal subset of $\mathcal H$ and let $\mathcal M=\bigvee\mathcal E$. If $P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M$, show that $Ph=\sum\{\langle h,e\rangle e:e\in\mathcal E\}$ for every $h$ in $\mathcal H$.

14. Let $\lambda=\text{Area}$ measure on $\{z\in\mathbb C:|z|<1\}$ and show that $1,z,z^2,\ldots$ are orthogonal vectors in $L^2(\lambda)$. Find $\|z^n\|$, $n\geq 0$. If $e_n=\|z^n\|^{-1}z^n$, $n\geq 0$, is $\{e_0,e_1,\ldots\}$ a basis for $L^2(\lambda)$?

15. In the proof of (4.14), show that if either $\varepsilon$ or $\eta$ is finite, then $\varepsilon=\eta$.

16. If $\mathcal H$ is an infinite dimensional Hilbert space, show that no orthonormal basis for $\mathcal H$ is a Hamel basis. Show that a Hamel basis is uncountable.

17. Let $d\geq 1$ and let $\mu$ be a regular Borel measure on $\mathbb R^d$. Show that $L^2(\mu)$ is separable.

18. Suppose $L^2(X,\Omega,\mu)$ is separable and $\{E_i:i\in I\}$ is a collection of pairwise disjoint subsets of $X$, $E_i\in\Omega$, and $0<\mu(E_i)<\infty$ for all $i$. Show that $I$ is countable. Can you allow $\mu(E_i)=\infty$?

19. If $\{h\in\mathcal H:\|h\|\leq 1\}$ is compact, show that $\dim\mathcal H<\infty$.

20. What is the cardinality of a Hamel basis for $l^2$?

## §5. Isomorphic Hilbert Spaces and the Fourier Transform for the Circle

Every mathematical theory has its concept of isomorphism. In topology there is homeomorphism and homotopy equivalence; algebra calls them isomorphisms. The basic idea is to define a map which preserves the basic structure of the spaces in the category.

**5.1. Definition.** If $\mathcal H$ and $\mathcal K$ are Hilbert spaces, an *isomorphism* between $\mathcal H$ and $\mathcal K$ is a linear surjection $U:\mathcal H\to\mathcal K$ such that

$$
\langle Uh,Ug\rangle=\langle h,g\rangle
$$

for all $h,g$ in $\mathcal H$. In this case $\mathcal H$ and $\mathcal K$ are said to be *isomorphic*.

It is easy to see that if $U:\mathcal H\to\mathcal K$ is an isomorphism, then so is $U^{-1}:\mathcal K\to\mathcal H$. Similar such arguments show that the concept of “isomorphic” is an equivalence relation on Hilbert spaces. It is also certain that this is the correct equivalence relation since an inner product is the essential ingredient for a Hilbert space and isomorphic Hilbert spaces have the “same” inner product. One might object that completeness is another essential ingredient in the definition of a Hilbert space. So it is! However, this too is preserved by an isomorphism. An *isometry* between metric spaces is a map that preserves distance.

**5.2. Proposition.** *If $V:\mathcal H\to\mathcal K$ is a linear map between Hilbert spaces, then $V$ is an isometry if and only if $\langle Vh,Vg\rangle=\langle h,g\rangle$ for all $h,g$ in $\mathcal H$.*
