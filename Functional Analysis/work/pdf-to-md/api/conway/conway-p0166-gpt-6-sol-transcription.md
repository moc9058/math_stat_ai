EXERCISE

1. Let $E=\{x\in\ell^2(\mathbb N):\|x\|\leq 1\}$ and for $x$ in $E$ define $f(x)=((1-\|x\|^2)^{1/2},x(1),x(2),\ldots)$. Show that $f(E)\subseteq E$, $f$ is continuous, and $f$ has no fixed points.

## §10*. The Ryll–Nardzewski Fixed Point Theorem

This section begins by proving a fixed point theorem that in addition to being used to prove the result in the title of this section has some interest of its own. Recall that a map $T$ defined from a convex set $K$ into a vector space is said to be *affine* if $T(\sum\alpha_jx_j)=\sum\alpha_jT(x_j)$ when $x_j\in K$, $\alpha_j\geq 0$, and $\sum\alpha_j=1$.

**10.1. The Markov–Kakutani Fixed Point Theorem.** *If $K$ is a nonempty compact convex subset of a LCS $\mathscr X$ and $\mathscr F$ is a family of continuous affine maps of $K$ into itself that is abelian, then there is an $x_0$ in $K$ such that $T(x_0)=x_0$ for all $T$ in $\mathscr F$.*

**PROOF.** If $T\in\mathscr F$ and $n\geq 1$, define $T^{(n)}:K\to K$ by

$$
T^{(n)}=\frac{1}{n}\sum_{k=0}^{n-1}T^k.
$$

If $S$ and $T\in\mathscr F$ and $n,m\geq 1$, then it is easy to check that $S^{(n)}T^{(m)}=T^{(m)}S^{(n)}$. Let $\mathscr H=\{T^{(n)}(K):T\in\mathscr F,\ n\geq 1\}$. Each set in $\mathscr H$ is compact and convex. If $T_1,\ldots,T_p\in\mathscr F$ and $n_1,\ldots,n_p\geq 1$, then the commutativity of $\mathscr F$ implies that $T_1^{(n_1)}\cdots T_p^{(n_p)}(K)\subseteq\bigcap_{j=1}^p T_j^{(n_j)}(K)$. This says that $\mathscr H$ has the finite intersection property and hence there is an $x_0$ in $\bigcap\{B:B\in\mathscr H\}$. It is claimed that $x_0$ is the desired common fixed point for the maps in $\mathscr F$.

If $T\in\mathscr F$ and $n\geq 1$, then $x_0\in T^{(n)}(K)$. Thus there is an $x$ in $K$ such that

$$
x_0=T^{(n)}(x)=\frac{1}{n}\left[x+T(x)+\cdots+T^{n-1}(x)\right].
$$

Using this equation for $x_0$, it follows that

$$
\begin{aligned}
T(x_0)-x_0
&=\frac{1}{n}[T(x)+\cdots+T^n(x)]\\
&\quad-\frac{1}{n}[x+T(x)+\cdots+T^{n-1}(x)]\\
&=\frac{1}{n}[T^n(x)-x]\\
&\in\frac{1}{n}[K-K].
\end{aligned}
$$
