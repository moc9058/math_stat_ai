on $\mathcal X$ defined by the seminorms $\{p_1,p_2,\ldots\}$. Thus a LCS is metrizable if and only if its topology is determined by a countable family of seminorms.

**Proof.** It is left as an exercise for the reader to show that $d$ is a metric and induces the same topology as $\{p_n\}$. If $\mathcal X$ is a LCS and its topology is determined by a countable family of seminorms, it is immediate that $\mathcal X$ is metrizable. For the converse, assume that $\mathcal X$ is metrizable and its metric is $\rho$. Let $U_n=\{x:\rho(x,0)<1/n\}$. Because $\mathcal X$ is locally convex, there are continuous seminorms $q_1,\ldots,q_k$ and positive numbers $\varepsilon_1,\ldots,\varepsilon_k$ such that $\bigcap_{j=1}^{k}\{x:q_j(x)<\varepsilon_j\}\subseteq U_n$. If $p_n=\varepsilon_1^{-1}q_1+\cdots+\varepsilon_k^{-1}q_k$, then $x\in U_n$ whenever $p_n(x)<1$. Clearly, $p_n$ is continuous for each $n$. Thus if $x_j\to0$ in $\mathcal X$, then for each $n$, $p_n(x_j)\to0$ as $j\to\infty$. Conversely, suppose that for each $n$, $p_n(x_j)\to0$ as $j\to\infty$. If $\varepsilon>0$, let $n>\varepsilon^{-1}$. Then there is a $j_0$ such that for $j\geq j_0$, $p_n(x_j)<1$. Thus, for $j\geq j_0$, $x_j\in U_n\subseteq\{x:\rho(x,0)<\varepsilon\}$. That is, $\rho(x_j,0)<\varepsilon$ for $j\geq j_0$ and so $x_j\to0$ in $\mathcal X$. This shows that $\{p_n\}$ determines the topology on $\mathcal X$. (Why?) ■

**2.2. Example.** If $C(X)$ is as in Example 1.5, then $C(X)$ is metrizable if and only if $X=\bigcup_{n=1}^{\infty}K_n$, where each $K_n$ is compact, $K_1\subseteq K_2\subseteq\cdots$, and if $K$ is any compact subset of $X$, then $K\subseteq K_n$ for some $n$.

**2.3. Example.** If $X$ is locally compact and $C(X)$ is as in Example 1.5, then $C(X)$ is metrizable if and only if $X$ is $\sigma$-compact (that is, $X$ is the union of a sequence of compact sets). If $H(G)$ is as in Example 1.6, then $H(G)$ is metrizable.

If $\mathcal X$ is a vector space and $d$ is a metric on $\mathcal X$, say that $d$ is *translation invariant* if $d(x+z,y+z)=d(x,y)$ for all $x,y,z$ in $\mathcal X$. Note that the metric defined by a norm as well as the metric defined in (2.1) are translation invariant.

**2.4. Definition.** A *Fréchet space* is a TVS $\mathcal X$ whose topology is defined by a translation invariant metric $d$ and such that $(\mathcal X,d)$ is complete.

It should be pointed out that some authors include in the definition of a Fréchet space the assumption that $\mathcal X$ is locally convex.

**2.5. Definition.** If $\mathcal X$ is a TVS and $B\subseteq\mathcal X$, then $B$ is *bounded* if for every open set $U$ containing $0$, there is an $\varepsilon>0$ such that $\varepsilon B\subseteq U$.

If $\mathcal X$ is a normed space, then it is easy to see that a set $B$ is bounded if and only if $\sup\{\|b\|:b\in B\}<\infty$, so the definition is intuitively correct.

Also, notice that if $\|\cdot\|$ is a norm, $\{x:\|x\|<1\}$ is itself bounded. This is not true for seminorms. For example, if $C(\mathbb R)$ is topologized as in (1.5), let $p(f)=\sup\{|f(t)|:0\leq t\leq1\}$. Then $p$ is a continuous seminorm. However,
