18. If $\mathcal{X}$ is a finite-dimensional vector space and $\mathcal{T}_1,\mathcal{T}_2$ are two topologies on $\mathcal{X}$ that make $\mathcal{X}$ into a TVS, then $\mathcal{T}_1=\mathcal{T}_2$.

19. If $\mathcal{X}$ is a TVS and $\mathcal{M}$ is a finite dimensional linear manifold in $\mathcal{X}$, then $\mathcal{M}$ is closed and $\mathcal{Y}+\mathcal{M}$ is closed for any closed subspace $\mathcal{Y}$ of $\mathcal{X}$.

20. Let $\mathcal{X}$ be any infinite dimensional vector space and let $\mathcal{T}$ be the collection of all subsets $W$ of $\mathcal{X}$ such that if $x\in W$, then there is a convex balanced set $U$ with $x+U\subseteq W$ and $U\cap\mathcal{M}$ open in $\mathcal{M}$ for every finite dimensional linear manifold $\mathcal{M}$ in $\mathcal{X}$. (Each such $\mathcal{M}$ is given its usual topology.) Show: (a) $(\mathcal{X},\mathcal{T})$ is a LCS; (b) a set $F$ is closed in $\mathcal{X}$ if and only if $F\cap\mathcal{M}$ is closed for every finite dimensional subspace $\mathcal{M}$ of $\mathcal{X}$; (c) if $Y$ is a topological space and $f:\mathcal{X}\to Y$ (not necessarily linear), then $f$ is continuous if and only if $f|_{\mathcal{M}}$ is continuous for every finite dimensional space $\mathcal{M}$; (d) if $\mathcal{Y}$ is a TVS and $T:\mathcal{X}\to\mathcal{Y}$ is a linear map, then $T$ is continuous.

21. Let $X$ be a locally compact space and for each $\phi$ in $C_0(X)$, define $p_\phi(f)=\|\phi f\|_\infty$ for $f$ in $C_b(X)$. Show that $p_\phi$ is a seminorm on $C_b(X)$. Let $\beta=$ the topology defined by these seminorms. Show that $(C_b(X),\beta)$ is a LCS that is complete. $\beta$ is called the *strict topology*.

22. For $0<p<1$, let $l^p=$ all sequences $x$ such that $\sum_{n=1}^{\infty}|x(n)|^p<\infty$. Define $d(x,y)=\sum_{n=1}^{\infty}|x(n)-y(n)|^p$ (no $p$th root). Then $d$ is a metric and $(l^p,d)$ is a TVS that is not locally convex.

23. Let $\mathcal{X}$ and $\mathcal{Y}$ be locally convex spaces and let $T:\mathcal{X}\to\mathcal{Y}$ be a linear transformation. Show that $T$ is continuous if and only if for every continuous seminorm $p$ on $\mathcal{Y}$, $p\circ T$ is a continuous seminorm on $\mathcal{X}$.

24. Let $\mathcal{X}$ be a LCS and let $G$ be an open connected subset of $\mathcal{X}$. Show that $G$ is arcwise connected.

## §2. Metrizable and Normable Locally Convex Spaces

Which LCS’s are metrizable? That is, which have a topology which is defined by a metric? Which LCS’s have a topology that is defined by a norm? Both are interesting questions and both answers could be useful.

If $\mathcal{P}$ is a family of seminorms on $\mathcal{X}$ and $\mathcal{X}$ is a TVS, say that $\mathcal{P}$ determines the topology on $\mathcal{X}$ if the topology of $\mathcal{X}$ is the same as the topology induced by $\mathcal{P}$.

**2.1. Proposition.** *Let $\{p_1,p_2,\ldots\}$ be a sequence of seminorms on $\mathcal{X}$ such that $\bigcap_{n=1}^{\infty}\{x:p_n(x)=0\}=(0)$. For $x$ and $y$ in $\mathcal{X}$, define*

$$
d(x,y)=\sum_{n=1}^{\infty}2^{-n}\frac{p_n(x-y)}{1+p_n(x-y)}.
$$

*Then $d$ is a metric on $\mathcal{X}$ and the topology on $\mathcal{X}$ defined by $d$ is the topology*
