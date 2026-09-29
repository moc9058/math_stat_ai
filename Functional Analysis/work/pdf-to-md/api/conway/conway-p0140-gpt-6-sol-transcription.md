topology defined by the seminorms $\{p_x:x\in\mathcal X\}$, where

$$
p_x(x^*)=|\langle x,x^*\rangle|.
$$

So a subset $U$ of $\mathcal X$ is weakly open if and only if for every $x_0$ in $U$ there is an $\varepsilon>0$ and there are $x_1^*,\ldots,x_n^*$ in $\mathcal X^*$ such that

$$
\bigcap_{k=1}^{n}\{x\in\mathcal X:|\langle x-x_0,x_k^*\rangle|<\varepsilon\}\subseteq U.
$$

A net $\{x_i\}$ in $\mathcal X$ converges weakly to $x_0$ if and only if $\langle x_i,x^*\rangle\to\langle x_0,x^*\rangle$ for every $x^*$ in $\mathcal X^*$. (What are the analogous statements for the weak-star topology?)

Note that both $(\mathcal X,\mathrm{wk})$ and $(\mathcal X^*,\mathrm{wk}^*)$ are LCS’s. Also, $\mathcal X$ already possesses a topology so that $\mathrm{wk}$ is a second topology on $\mathcal X$. However, $\mathcal X^*$ has no topology to begin with so that $\mathrm{wk}^*$ is the only topology on $\mathcal X^*$. Of course if $\mathcal X$ is a normed space, this last statement is not correct since $\mathcal X^*$ is a Banach space (III.5.4). The reader should also be cautioned that some authors abuse the language and use the term weak topology to designate both the weak and weak-star topologies. Finally, pay attention to the positions of $\mathcal X$ and $\mathcal X^*$ in the notation $\sigma(\mathcal X,\mathcal X^*)=\mathrm{wk}$ and $\sigma(\mathcal X^*,\mathcal X)=\mathrm{wk}^*$.

If $\{x_i\}$ is a net in $\mathcal X$ and $x_i\to0$ in $\mathcal X$, then for every $x^*$ in $\mathcal X^*$, $\langle x_i,x^*\rangle\to0$. So if $\mathcal T$ is the topology on $\mathcal X$, $\mathrm{wk}\subseteq\mathcal T$ (A.2.9) and each $x^*$ in $\mathcal X^*$ is weakly continuous. The first result gives the converse of this.

**1.2. Theorem.** If $\mathcal X$ is a LCS, $(\mathcal X,\mathrm{wk})^*=\mathcal X^*$.

**Proof.** Since every weakly open set is open in the original topology, each $f$ in $(\mathcal X,\mathrm{wk})^*$ belongs to $\mathcal X^*$. The converse is even easier. $\blacksquare$

**1.3. Theorem.** If $\mathcal X$ is a LCS, $(\mathcal X^*,\mathrm{wk}^*)^*=\mathcal X$.

**Proof.** Clearly if $x\in\mathcal X$, $x^*\mapsto\langle x,x^*\rangle$ is a $\mathrm{wk}^*$ continuous functional on $\mathcal X^*$. Hence $\mathcal X\subseteq(\mathcal X^*,\mathrm{wk}^*)^*$. Conversely, if $f\in(\mathcal X^*,\mathrm{wk}^*)^*$, then (IV.3.1) implies there are vectors $x_1,\ldots,x_n$ in $\mathcal X$ such that $|f(x^*)|\leq\sum_{k=1}^{n}|\langle x_k,x^*\rangle|$ for all $x^*$ in $\mathcal X^*$. This implies that $\bigcap\{\ker x_k:1\leq k\leq n\}\subseteq\ker f$. By (A.1.4) there are scalars $\alpha_1,\ldots,\alpha_n$ such that $f=\sum_{k=1}^{n}\alpha_kx_k$; hence $f\in\mathcal X$. $\blacksquare$

So $\mathcal X$ is the dual of a LCS—$(\mathcal X^*,\mathrm{wk}^*)$—and hence has a weak-star topology—$\sigma((\mathcal X,\mathrm{wk}^*),\mathcal X^*)$. As an exercise in notational juggling, note that $\sigma((\mathcal X,\mathrm{wk}^*),\mathcal X^*)=\sigma(\mathcal X,\mathcal X^*)$.

All unmodified topological statements about $\mathcal X$ refer to its original topology. So if $A\subseteq\mathcal X$ and we say that it is closed, we mean that $A$ is closed in the original topology of $\mathcal X$. To say that $A$ is closed in the weak topology of $\mathcal X$ we say that $A$ is weakly closed or $\mathrm{wk}$-closed. Also $\operatorname{cl}A$ means the closure of $A$ in the original topology while $\mathrm{wk}-\operatorname{cl}A$ means the closure of $A$ in the weak topology. The next result shows that under certain circumstances this distinction is unnecessary.
