It is not difficult to see that for $w_0$ in $\mathbb{C}\setminus K$,

$$
\left(\frac{d}{dw}\right)^n\hat{\mu}(w_0)
=n!\int (z-w_0)^{-n-1}\,d\mu(z). \tag{8.3}
$$

Also, we can easily find the power series expansion of $\hat{\mu}$ at infinity. Indeed,

$$
\hat{\mu}(w)=\int\frac{1}{z-w}\,d\mu(z)
=-\frac{1}{w}\int\left(1-\frac{z}{w}\right)^{-1}\,d\mu(z).
$$

Choose $w$ near enough to infinity that $|z/w|<1$ for all $z$ in $K$. Then

$$
\begin{aligned}
\hat{\mu}(w)
&=-\frac{1}{w}\sum_{n=0}^{\infty}\int\left(\frac{z}{w}\right)^n\,d\mu(z)\\
&=-\sum_{n=0}^{\infty}\frac{a_n}{w^{n+1}},
\end{aligned}\tag{8.4}
$$

where $a_n=\int z^n\,d\mu(z)$.

Now assume $\mu\in M(K)$ and $\int g\,d\mu=0$ for every rational function $g$ with poles in $E$. Let $U$ be a component of $\mathbb{C}_\infty\setminus K$, and let $w_0\in E\cap U$. If $w_0\ne\infty$, then the hypothesis and (8.3) imply that each derivative of $\hat{\mu}$ at $w_0$ vanishes. Hence $\hat{\mu}\equiv0$ on $U$. If $w_0=\infty$, then (8.4) implies $\hat{\mu}\equiv0$ on $U$. Thus $\hat{\mu}\equiv0$ on $\mathbb{C}_\infty\setminus K$.

If $f$ is analytic on an open set $G$ containing $K$, let $\gamma_1,\ldots,\gamma_n$ be straight-line segments in $G\setminus K$ such that

$$
f(z)=\sum_{k=1}^{n}\frac{1}{2\pi i}\int_{\gamma_k}\frac{f(w)}{w-z}\,dw
$$

for all $z$ in $K$. (See p. 195 of Conway [1978].) Thus

$$
\begin{aligned}
\int_K f(z)\,d\mu(z)
&=\sum_{k=1}^{n}\frac{1}{2\pi i}\int_K\int_{\gamma_k}
\frac{f(w)}{w-z}\,dw\,d\mu(z)\\
&=-\sum_{k=1}^{n}\frac{1}{2\pi i}\int_{\gamma_k}
f(w)\hat{\mu}(w)\,dw
\end{aligned}
$$

by Fubini’s Theorem. But $\hat{\mu}(w)=0$ on $\gamma_k$ $(\subseteq\mathbb{C}\setminus K)$, so $\int f\,d\mu=0$. By (6.13), $f\in R(K,E)$. This proves Runge’s Theorem. $\blacksquare$

**8.5. Corollary.** *If $K$ is compact and $\mathbb{C}\setminus K$ is connected and if $f$ is analytic in a neighborhood of $K$, then there is a sequence of polynomials that converges to $f$ uniformly on $K$.*

## Exercises

1. Let $\mu$ be a compactly supported measure on $\mathbb{C}$ that is boundedly absolutely continuous with respect to area measure. Show that $\hat{\mu}$ is continuous on $\mathbb{C}_\infty$.

2. Let $m=$ Lebesgue measure on $[0,1]$. Show that $\hat{m}$ is not continuous at any point of $[0,1]$.
