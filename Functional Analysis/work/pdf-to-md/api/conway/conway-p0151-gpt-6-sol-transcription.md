So $\psi\in F_m$ and hence $|\langle\psi,f_m\rangle|\leqslant\varepsilon/3$ for $n\geqslant m$. Thus

**5.3**
$$
\left|\sum_{j=1}^{J}\phi(j)f_n(j)+\sum_{j=J+1}^{\infty}|f_n(j)|\right|
\leqslant\frac{\varepsilon}{3}
$$

for $n\geqslant m$. But there is an $m_1\geqslant m$ such that for $n\geqslant m_1$, $\sum_{j=1}^{J}|f_n(j)|<\varepsilon/3$. (Why?) Combining this with (5.3) gives that

$$
\begin{aligned}
\|f_n\|
&=\sum_{j=1}^{\infty}|f_n(j)|\\
&<\frac{\varepsilon}{3}
+\left|\sum_{j=J+1}^{\infty}|f_n(j)|
+\sum_{j=1}^{J}\phi(j)f_n(j)\right|
+\left|\sum_{j=1}^{J}\phi(j)f_n(j)\right|\\
&<\frac{2\varepsilon}{3}+\sum_{j=1}^{J}|f_n(j)|\\
&<\varepsilon
\end{aligned}
$$

whenever $n\geqslant m_1$. $\blacksquare$

So if $(\operatorname{ball} l^1,\mathrm{wk})$ were metrizable, the preceding proposition would say that the weak and norm topologies on $l^1$ agree. But this is not the case (Exercise 1.10).

Also, note that the preceding result demonstrates in a dramatic way that in discussions concerning the weak topology it is essential to consider nets and not just sequences.

A proof of (5.2) that avoids the Baire Category Theorem can be found in Banach [1955], p. 218.

## Exercises

1. Let $B=\operatorname{ball} M[0,1]$ and for $\mu,\nu$ in $M[0,1]$ define
   $$
   d(\mu,\nu)=\sum_{n=0}^{\infty}2^{-n}
   \left|\int_0^1 x^n\,d\mu-\int_0^1 x^n\,d\nu\right|.
   $$
   Show that $d$ is a metric on $M[0,1]$ that defines the weak-star topology on $B$ but not on $M[0,1]$.

2. Let $X$ be a compact space and let $\mathcal U=\{(U,V): U,V\text{ are open subsets of }X\text{ and }\operatorname{cl}U\subseteq V\}$. For $u=(U,V)$ in $\mathcal U$, let $f_u:X\to[0,1]$ be a continuous function such that $f_u\equiv1$ on $\operatorname{cl}U$ and $f_u\equiv0$ on $X\setminus V$. Show: (a) the linear span of $\{f_u:u\in\mathcal U\}$ is dense in $C(X)$; (b) if $X$ is a metric space, then $C(X)$ is separable; (c) if $X$ is a $\sigma$-compact metrizable locally compact space, then $C_0(X)$ is separable. ($X$ is $\sigma$-compact if $X$ is the union of a countable number of compact subsets.)

3. If $\mathcal X$ is a Banach space and $\mathcal X^*$ is separable, show that (a) $\mathcal X$ is separable; (b) if $K$ is a weakly compact subset of $\mathcal X$, then $K$ with the relative weak topology is metrizable.

4. If $B=\operatorname{ball} l^\infty$, show that $d(\phi,\psi)=\sum_{j=1}^{\infty}2^{-j}|\phi(j)-\psi(j)|$ defines a metric on $B$ and that this metric defines the weak-star topology on $B$.

5. Use the type of argument used in the proof of the Principle of Uniform Boundedness to obtain a proof of Proposition 5.2 that does not need the Baire Category Theorem.

6. Show that Proposition 5.2 fails for $l^p$ if $1<p<\infty$.
