The proof of this is an involved construction. Inspired by Corollary C.14, one defines $\nu(U)$ for an open set $U$ by

$$
\nu(U)=\sup\{I(\phi):\phi\in C_c(X)_+,\ \phi\leqslant 1,\ \operatorname{spt}\phi\subseteq U\}.
$$

Then for any Borel set $E$, let

$$
\nu(E)=\inf\{\nu(U):E\subseteq U\text{ and }U\text{ is open}\}.
$$

It must now be shown that $\nu$ is a positive measure and $I(f)=\int f\,d\nu$. For the details see (12.36) in Hewitt and Stromberg [1975] or §56 in Halmos [1974]. Indeed, Theorem C.17 is often called the Riesz Representation Theorem.

**C.18. Riesz Representation Theorem.** *If $X$ is a locally compact space and $\mu\in M(X)$, define $F_\mu:C_0(X)\to\mathbb C$ by*

$$
F_\mu(f)=\int f\,d\mu.
$$

*Then $F_\mu\in C_0(X)^*$ and the map $\mu\mapsto F_\mu$ is an isometric isomorphism of $M(X)$ onto $C_0(X)^*$.*

**Proof.** The fact that $\mu\mapsto F_\mu$ is an isometry is the content of Lemma C.13. It remains to show that $\mu\mapsto F_\mu$ is surjective. Let $F\in C_0(X)^*$ and define $I:C_0(X)\to\mathbb C$ as in Lemma C.15. By Theorem C.17, there is a positive measure $\nu$ in $M(X)$ such that $I(f)=\int f\,d\nu$ for all $f$ in $C_0(X)$. If $f\in C_0(X)$, then the definition of $I$ implies that $|F(f)|\leqslant I(|f|)=\int |f|\,d\nu$. Thus, $f\mapsto F(f)$ defines a bounded linear functional on $C_0(X)$ considered as a linear manifold in $L^1(\nu)$. Now $C_0(X)$ is dense in $L^1(\nu)$ (Why?), so $F$ has a unique extension to a bounded linear functional on $L^1(\nu)$. By Theorem B.1 there is a function $\phi$ in $L^\infty(\nu)$ such that $F(f)=\int f\phi\,d\nu$ for every $f$ in $C_0(X)$ and $\|\phi\|_\infty\leqslant 1$. Let $\mu(E)=\int_E\phi\,d\nu$ for every Borel set $E$. Then $\mu\in M(X)$ and by Theorem C.8(a), $F(f)=\int f\,d\mu$; that is, $F=F_\mu$. $\blacksquare$
