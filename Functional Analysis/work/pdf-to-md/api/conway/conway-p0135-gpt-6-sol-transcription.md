In fact, $U\subseteq W$, so $U\subset W\cap\mathcal Y$. If $w\in W\cap\mathcal Y$, then $w=tu+(1-t)v$, $u$ in $U$, $v$ in $V$, $0\leq t\leq1$; it may be assumed that $0<t<1$. (Why?) Hence, $v=(1-t)^{-1}(w-tu)\in\mathcal Y$. So $v\in V\cap\mathcal Y\subseteq U$; hence $w\in U$.

Let $\tilde p=$ the gauge of $W$. By Claim 5.14, $\{y\in\mathcal Y:\tilde p(y)<1\}=\{y\in\mathcal Y:p(y)<1\}$. By the uniqueness of the gauge, $\tilde p|_{\mathcal Y}=p$. ■

**5.15. Corollary.** *If $\mathcal X$ is the strict inductive limit of $\{\mathcal X_n\}$, $k$ is fixed, and $p_k$ is a continuous seminorm on $\mathcal X_k$, then there is a continuous seminorm $p$ on $\mathcal X$ such that $p|_{\mathcal X_k}=p_k$. In particular, the inductive limit topology is Hausdorff and the topology on $\mathcal X$ when restricted to $\mathcal X_k$ equals the original topology of $\mathcal X_k$.*

**Proof.** By (5.13) and induction, for every integer $n>k$, there is a continuous seminorm $p_n$ such that $p_n|_{\mathcal X_{n-1}}=p_{n-1}$. If $x\in\mathcal X$, define $p(x)=p_n(x)$ when $x\in\mathcal X_n$. Since $\mathcal X_n\subseteq\mathcal X_{n+1}$ for all $n$, the properties of $\{p_n\}$ insure that $p$ is well defined. Clearly $p$ is a seminorm and by (5.6c) $p$ is continuous.

If $x\in\mathcal X$ and $x\ne0$, there is a $k\geq1$ such that $x\in\mathcal X_k$. Thus there is a continuous seminorm $p_k$ on $\mathcal X_k$ such that $p_k(x)\ne0$. Using the first part of the corollary, we get a continuous seminorm $p$ on $\mathcal X$ such that $p(x)\ne0$. Thus $(\mathcal X,\mathcal T)$ is Hausdorff. The proof that the topology on $\mathcal X$ when relativized to $\mathcal X_k$ equals the original topology is an easy application of (5.13). ■

**5.16. Proposition.** *Let $\mathcal X$ be the strict inductive limit of $\{\mathcal X_n\}$. A subset $B$ of $\mathcal X$ is bounded if and only if there is an $n\geq1$ such that $B\subseteq\mathcal X_n$ and $B$ is bounded in $\mathcal X_n$.*

The proof will be accomplished only after a few preliminaries are settled. Before doing this, here are a few consequences of (5.16).

**5.17. Corollary.** *If $\mathcal X$ is the strict inductive limit of $\{\mathcal X_n\}$, then a subset $K$ of $\mathcal X$ is compact if and only if there is an $n\geq1$ such that $K\subseteq\mathcal X_n$ and $K$ is compact in $\mathcal X_n$.*

**5.18. Corollary.** *If $\mathcal X$ is the strict inductive limit of Fréchet spaces $\{\mathcal X_n\}$, $\mathcal Y$ is a LCS, and $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is continuous if and only if $T$ is sequentially continuous.*

**Proof.** By Proposition 5.7, $T$ is continuous if and only if $T|_{\mathcal X_n}$ is continuous for every $n$. Since each $\mathcal X_n$ is metrizable, the result follows. ■

Note that using Example 5.11 it follows that for an open subset $\Omega$ of $\mathbf R^d$, $\mathcal D(\Omega)$ is the strict inductive limit of Fréchet spaces [each $\mathcal D(K_n)$ is a Fréchet space by Proposition 2.1]. So (5.18) applies.

**5.19. Definition.** If $\Omega$ is an open subset of $\mathbf R^d$, a *distribution* on $\Omega$ is a continuous linear functional on $\mathcal D(\Omega)$.
