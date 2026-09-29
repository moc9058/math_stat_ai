**4.7. Proposition.** Let $\{e_1,\ldots,e_n\}$ be an orthonormal set in $\mathcal H$ and let $\mathcal M=\bigvee\{e_1,\ldots,e_n\}$. If $P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M$, then

$$
Ph=\sum_{k=1}^{n}\langle h,e_k\rangle e_k
$$

for all $h$ in $\mathcal H$.

**Proof.** Let $Qh=\sum_{k=1}^{n}\langle h,e_k\rangle e_k$. If $1\leq j\leq n$, then
$\langle Qh,e_j\rangle=\sum_{k=1}^{n}\langle h,e_k\rangle\langle e_k,e_j\rangle=\langle h,e_j\rangle$ since $e_k\perp e_j$ for $k\neq j$. Thus $\langle h-Qh,e_j\rangle=0$ for $1\leq j\leq n$. That is, $h-Qh\perp\mathcal M$ for every $h$ in $\mathcal H$. Since $Qh$ is clearly a vector in $\mathcal M$, $Qh$ is the unique vector $h_0$ in $\mathcal M$ such that $h-h_0\perp\mathcal M$ (2.6). Hence $Qh=Ph$ for every $h$ in $\mathcal H$. $\blacksquare$

**4.8. Bessel’s Inequality.** If $\{e_n:n\in\mathbb N\}$ is an orthonormal set and $h\in\mathcal H$, then

$$
\sum_{n=1}^{\infty}|\langle h,e_n\rangle|^2\leq\|h\|^2.
$$

**Proof.** Let $h_n=h-\sum_{k=1}^{n}\langle h,e_k\rangle e_k$. Then $h_n\perp e_k$ for $1\leq k\leq n$ (Why?) By the Pythagorean Theorem,

$$
\begin{aligned}
\|h\|^2
&=\|h_n\|^2+\left\|\sum_{k=1}^{n}\langle h,e_k\rangle e_k\right\|^2\\
&=\|h_n\|^2+\sum_{k=1}^{n}|\langle h,e_k\rangle|^2\\
&\geq\sum_{k=1}^{n}|\langle h,e_k\rangle|^2.
\end{aligned}
$$

Since $n$ was arbitrary, the result is proved. $\blacksquare$

**4.9. Corollary.** If $\mathscr E$ is an orthonormal set in $\mathcal H$ and $h\in\mathcal H$, then $\langle h,e\rangle\neq0$ for at most a countable number of vectors $e$ in $\mathscr E$.

**Proof.** For each $n\geq1$ let $\mathscr E_n=\{e\in\mathscr E:|\langle h,e\rangle|\geq1/n\}$. By Bessel’s Inequality, $\mathscr E_n$ is finite. But $\bigcup_{n=1}^{\infty}\mathscr E_n=\{e\in\mathscr E:\langle h,e\rangle\neq0\}$. $\blacksquare$

**4.10. Corollary.** If $\mathscr E$ is an orthonormal set and $h\in\mathcal H$, then

$$
\sum_{e\in\mathscr E}|\langle h,e\rangle|^2\leq\|h\|^2.
$$

This last corollary is just Bessel’s Inequality together with the fact (4.9) that at most a countable number of the terms in the sum differ from zero.

Actually, the sum that appears in (4.10) can be given a better interpretation—a mathematically precise one that will be useful later. The question is, what is meant by $\sum\{h_i:i\in I\}$ if $h_i\in\mathcal H$ and $I$ is an infinite, possibly uncountable, set? Let $\mathscr F$ be the collection of all finite subsets of $I$ and order
