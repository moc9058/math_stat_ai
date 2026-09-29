This last corollary is one of the most useful forms of the Krein–Smulian Theorem. To show that a convex subset $A$ of $\mathcal X^*$ is weak-star closed it is not necessary to show that every weak-star convergent net from $A$ has its limit in $A$; it suffices to prove this for sequences.

**12.8. Corollary.** *If $\mathcal X$ is a separable Banach space and $F:\mathcal X^*\to\mathbb F$ is a linear functional, then $F$ is weak-star continuous if and only if $F$ is weak-star sequentially continuous.*

**Proof.** By Theorem IV.3.1, $F$ is $\mathrm{wk}^*$ continuous if and only if $\ker F$ is $\mathrm{wk}^*$ closed. This corollary is, therefore, a direct consequence of the preceding one. $\blacksquare$

A proof of Corollary 12.8 that is independent of The Krein–Smulian Theorem can be found as a lemma in Whitley [1986].

There is a misinterpretation of the Krein–Smulian Theorem that the reader should be warned about. If $A$ is a weak-star closed convex balanced subset of ball $\mathcal X^*$, let $\mathcal M=\bigcup\{rA:r>0\}$. It is easy to see that $\mathcal M$ is a linear manifold, but it does not follow that $\mathcal M$ is weak-star closed. What is true is the following.

**12.9. Theorem.** *Let $\mathcal X$ be a Banach space and let $A$ be a weak-star closed subset of $\mathcal X^*$. If $\mathcal Y=$ the linear span of $A$, then $\mathcal Y$ is norm closed in $\mathcal X^*$ if and only if $\mathcal Y$ is weak-star closed.*

The proof will not be presented here. The interested reader can consult Dunford and Schwartz [1958], p. 429.

There is a method for finding the weak-star closure of a linear manifold that is quite useful despite its seemingly bizarre appearance. Let $\mathcal X$ be a Banach space and let $\mathcal M$ be a linear manifold in $\mathcal X^*$. For each ordinal number $\alpha$ define a linear manifold $\mathcal M_\alpha$ as follows. Let $\mathcal M_1=\mathcal M$. Suppose $\alpha$ is an ordinal number and $\mathcal M_\beta$ has been defined for each ordinal $\beta<\alpha$. If $\alpha$ has an immediate predecessor, $\alpha-1$, let $\mathcal M_\alpha$ be the weak-star sequential closure of $\mathcal M_{\alpha-1}$. If $\alpha$ is a limit ordinal and has no immediate predecessor, let $\mathcal M_\alpha=\bigcup\{\mathcal M_\beta:\beta<\alpha\}$. In each case $\mathcal M_\alpha$ is a linear manifold in $\mathcal X^*$ and $\mathcal M_\beta\subseteq\mathcal M_\alpha$ if $\beta\leq\alpha$.

**12.10. Theorem.** *If $\mathcal X$ is a separable Banach space, $\mathcal M$ is a linear manifold in $\mathcal X^*$, and $\mathcal M_\alpha$ is defined as above for every ordinal number $\alpha$, then $\mathcal M_\Omega$ is the weak-star closure of $\mathcal M$, where $\Omega$ is the first uncountable ordinal. Moreover, there is an ordinal number $\alpha<\Omega$ such that $\mathcal M_\alpha=\mathcal M_\Omega$.*

**Proof.** By Corollary 12.7 it suffices to show that $\mathcal M_\Omega$ is weak-star sequentially closed. Let $\{x_n^*\}$ be a sequence in $\mathcal M_\Omega$ such that $x_n^*\to x^*$ $(\mathrm{wk}^*)$. Since $\mathcal M_\Omega=\bigcup\{\mathcal M_\alpha:\alpha<\Omega\}$, for each $n$ there is an $\alpha_n<\Omega$ such that $x_n^*\in\mathcal M_{\alpha_n}$. But $\alpha=\sup_n\alpha_n<\Omega$. Hence $x_n^*\in\mathcal M_\alpha$ for all $n$; thus $x^*\in\mathcal M_{\alpha+1}\subseteq\mathcal M_\Omega$ and $\mathcal M_\Omega$ is weak-star closed.
