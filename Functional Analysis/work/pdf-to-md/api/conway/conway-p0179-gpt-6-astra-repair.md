164　　　　　　　　　　　　　　　　　V. Weak Topologies

A proof of James’s Theorem can be found in Pyrce [1966]. Another reference for a proof of this theorem as well as a number of other equivalent formulations of weak compactness and reflexivity is James [1964b]. Also, if $\mathcal X$ is only assumed to be a normed space in Theorem 13.2, the conclusion is false (see James [1971]).

The next result, presented with proof, is also called the Krein–Smulian Theorem and must not be confused with the theorem of the preceding section.

**13.4. Krein–Smulian Theorem.** *If $\mathcal X$ is a Banach space and $K$ is a weakly compact subset of $\mathcal X$, then $\overline{\operatorname{co}}(K)$ is weakly compact.*

**Proof.** *Case 1: $\mathcal X$ is separable.* Endow $K$ with the relative weak topology; so $M(K)=C(K)^*$. If $\mu\in M(K)$, define $F_\mu:\mathcal X^*\to\mathbb F$ by

$$
F_\mu(x^*)=\int_K\langle x,x^*\rangle\,d\mu(x).
$$

It is easy to see that $F_\mu$ is a bounded linear functional on $\mathcal X^*$ and $\|F_\mu\|\leq\|\mu\|\sup\{\|x\|:x\in K\}$.

**13.5. Claim.** $F_\mu:\mathcal X^*\to\mathbb F$ is weak-star continuous.

By (12.8) it suffices to show that $F_\mu$ is weak* sequentially continuous. Let $\{x_n^*\}$ be a sequence in $\mathcal X^*$ such that $x_n^*\to x^*$ (wk*). By the PUB, $M=\sup_n\|x_n^*\|<\infty$. Also, $\langle x,x_n^*\rangle\to\langle x,x^*\rangle$ for every $x$ in $K$. By the Lebesgue Dominated Convergence Theorem, $F_\mu(x_n^*)=\int\langle x,x_n^*\rangle\,d\mu(x)\to F_\mu(x^*)$. So (13.5) is established.

By (1.3), $F_\mu\in\mathcal X$. That is, there is an $x_\mu$ in $\mathcal X$ such that $F_\mu(x^*)=\langle x_\mu,x^*\rangle$. Define $T:M(K)\to\mathcal X$ by $T(\mu)=x_\mu$.

**13.6. Claim.** $T:(M(K),\mathrm{wk}^*)\to(\mathcal X,\mathrm{wk})$ is continuous.

In fact, this is clear. If $\mu_i\to0$ weak* in $M(K)$, then for each $x^*$ in $\mathcal X^*$, $x^*|K\in C(K)$. Hence $\langle T(\mu_i),x^*\rangle=\int\langle x,x^*\rangle\,d\mu_i(x)\to0$.

Let $\mathcal P=$ the probability measures on $K$. By Alaoglu’s Theorem $\mathcal P$ is weak* compact. Thus $T(\mathcal P)$ is weakly compact and convex. However, if $x\in K$, $\langle T(\delta_x),x^*\rangle=\langle x,x^*\rangle$; that is, $T(\delta_x)=x$. So $T(\mathcal P)\supseteq K$. Hence $T(\mathcal P)\supseteq\overline{\operatorname{co}}(K)$ and $\overline{\operatorname{co}}(K)$ must be compact.

*Case 2: $\mathcal X$ is arbitrary.* Let $\{x_n\}$ be a sequence in $\operatorname{co}(K)$. So for each $n$ there is a finite subset $F_n$ of $K$ such that $x_n\in\operatorname{co}(F_n)$. Let $F=\bigcup_{n=1}^{\infty}F_n$ and let $\mathcal M=\bigvee F$. Then $K_1=K\cap\mathcal M$ is weakly compact and $\{x_n\}\subseteq\operatorname{co}(K_1)$. Since $\mathcal M$ is separable, Case 1 implies that $\overline{\operatorname{co}}(K_1)$ is weakly compact. By the Eberlein–Smulian Theorem, there is a subsequence $\{x_{n_k}\}$ and an $x$ in $\overline{\operatorname{co}}(K_1)\subseteq\overline{\operatorname{co}}(K)$ such that $x_{n_k}\to x$. Thus $\overline{\operatorname{co}}(K)$ is weakly compact. $\blacksquare$
