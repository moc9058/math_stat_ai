that $\mathbb{T}^{\infty}$ is also a compact abelian group while $\mathbb{R}^{\infty}$ fails to be locally compact. The Cantor set can be identified with the product of a countable number of copies of $\mathbb{Z}_2$ and is thus a compact abelian group. Indeed, the product of a countable number of finite sets (with the discrete topology) is homeomorphic to the Cantor set, so that the Cantor set has infinitely many nonisomorphic group structures.

For a topological group $G$, $L^1(G)$ is called the *group algebra* for $G$. If $G$ is discrete, the algebraists talk of the *group algebra* over a field $K$ as the set of all $f=\sum_{g\in G}a_g g$, where $a_g\in K$ and $a_g\ne 0$ for at most a finite number of $g$ in $G$. If $K=\mathbb{C}$, this is the set of functions $f:G\to\mathbb{C}$ with finite support. Thus in the discrete case the group algebra of the algebraists can be identified with a dense manifold in $L^1(G)=l^1(G)$.

Unlike §V.11, if $f:G\to\mathbb{C}$ and $x\in G$, define $f_x:G\to\mathbb{C}$ by $f_x(y)=f(yx^{-1})$; so $f_x(y)=f(x^{-1}y)$ for $G$ abelian. We want to examine the function $x\mapsto f_x$ of $G\to L^p(G)$, $1\leq p<\infty$. To do this we first prove the following (see Exercise V.11.10).

**9.1. Proposition.** *If $G$ is a topological group and $f:G\to\mathbb{C}$ is a continuous function with compact support, then for any $\varepsilon>0$ there is a neighborhood $U$ of $e$ such that $|f(x)-f(y)|<\varepsilon$ whenever $x^{-1}y\in U$.*

**Proof.** Let $\mathcal U$ be the collection of open neighborhoods $U$ of $e$ such that $U=U^{-1}$. Note that if $V$ is any neighborhood of $e$, then $U=V\cap V^{-1}\in\mathcal U$ and $U\subseteq V$. Order $\mathcal U$ by reverse inclusion.

Suppose the result is false. Then there is an $\varepsilon>0$ such that for every $U$ in $\mathcal U$ there are points $x_U,y_U$ in $G$ with $x_U^{-1}y_U$ in $U$ and $|f(x_U)-f(y_U)|\geq\varepsilon$. Note that either $x_U$ or $y_U\in K\equiv\operatorname{support}f$. Since $U=U^{-1}$, we may assume that $x_U\in K$ for every $U$ in $\mathcal U$. Now $\{x_U:U\in\mathcal U\}$ is a net in $K$. Since $K$ is compact, there is a point $x$ in $K$ such that $x_U\xrightarrow[\mathrm{cl}]{}x$. But $x_U^{-1}y_U\to e$. Since multiplication is continuous, $y_U=x_U(x_U^{-1}y_U)\xrightarrow[\mathrm{cl}]{}x$. Therefore if $W$ is any neighborhood of $x$, there is a $U$ in $\mathcal U$ with $x_U,y_U\in W$. But $f$ is continuous at $x$ so $W$ can be chosen such that $|f(x)-f(w)|<\varepsilon/2$ whenever $w\in W$. With this choice of $W$, $|f(x_U)-f(y_U)|<\varepsilon$, a contradiction. $\blacksquare$

One can rephrase (9.1) by saying that continuous functions on a topological group that have compact support are uniformly continuous.

In the next result it is the case $p=1$ which is of principal interest for us at this time. The proof of the general theorem is, however, no more difficult than this special case.

**9.2. Proposition.** *If $G$ is a locally compact group, $1\leq p<\infty$, and $f\in L^p(G)$, then the map $x\mapsto f_x$ is a continuous function from $G$ into $L^p(G)$.*

**Proof.** Fix $f$ in $L^p(G)$, $x$ in $G$, and $\varepsilon>0$; it must be shown that there is a neighborhood $V$ of $x$ such that for $y$ in $V$, $\|f_y-f_x\|_p<\varepsilon$. First note that there is a continuous function $\phi:G\to\mathbb{C}$ having compact support such that
