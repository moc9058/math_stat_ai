**Proof.** By the mean value property, if $0<t\leq r$, $f(a)=(1/2\pi)\int_{-\pi}^{\pi}f(a+te^{i\theta})\,d\theta$. Hence

$$
\begin{aligned}
(\pi r^2)^{-1}\iint_{B(a;r)}f
&=(\pi r^2)^{-1}\int_0^r t\left[\int_{-\pi}^{\pi}f(a+te^{i\theta})\,d\theta\right]dt\\
&=(2/r^2)\int_0^r tf(a)\,dt=f(a).
\end{aligned}
\qquad\blacksquare
$$

**1.12. Corollary.** If $f\in L_a^2(G)$, $a\in G$, and $0<r<\operatorname{dist}(a,\partial G)$, then

$$
|f(a)|\leq \frac{1}{r\sqrt{\pi}}\|f\|_2.
$$

**Proof.** Since $\overline{B}(a;r)\subseteq G$, the preceding lemma and the CBS inequality imply

$$
\begin{aligned}
|f(a)|
&=\frac{1}{\pi r^2}\left|\iint_{B(a;r)}f\cdot 1\right|\\
&\leq\frac{1}{\pi r^2}
\left[\iint_{B(a;r)}|f|^2\right]^{1/2}
\left[\iint_{B(a;r)}1^2\right]^{1/2}\\
&\leq\frac{1}{\pi r^2}\|f\|_2r\sqrt{\pi}.
\end{aligned}
\qquad\blacksquare
$$

**1.13. Proposition.** $L_a^2(G)$ is a Hilbert space.

**Proof.** If $\mu=$ area measure on $G$, then $L^2(\mu)$ is a Hilbert space and $L_a^2(G)\subseteq L^2(\mu)$. So it suffices to show that $L_a^2(G)$ is closed in $L^2(\mu)$. Let $\{f_n\}$ be a sequence in $L_a^2(G)$ and let $f\in L^2(\mu)$ such that $\int|f_n-f|^2\,d\mu\to0$ as $n\to\infty$.

Suppose $\overline{B}(a;r)\subseteq G$ and let $0<\rho<\operatorname{dist}(B(a;r),\partial G)$. By the preceding corollary there is a constant $C$ such that $|f_n(z)-f_m(z)|\leq C\|f_n-f_m\|_2$ for all $n,m$ and for $|z-a|\leq\rho$. Thus $\{f_n\}$ is a uniformly Cauchy sequence on any closed disk in $G$. By standard results from analytic function theory (Montel’s Theorem or Morera’s Theorem, for example), there is an analytic function $g$ on $G$ such that $f_n(z)\to g(z)$ uniformly on compact subsets of $G$. But since $\int|f_n-f|^2\,d\mu\to0$, a result of Riesz implies there is a subsequence $\{f_{n_k}\}$ such that $f_{n_k}(z)\to f(z)$ a.e. $[\mu]$. Thus $f=g$ a.e. $[\mu]$ and so $f\in L_a^2(G)$. $\blacksquare$

## Exercises

1. Verify the statements made in Example 1.2.
2. Verify that $l^2(I)$ (Example 1.7) is a Hilbert space.
3. Show that the space $\mathcal H$ in Example 1.8 is a Hilbert space.
4. Describe the Hilbert spaces obtained by completing the space $\mathcal X$ in Example 1.2 with respect to the norm defined by each of the inner products given there.
