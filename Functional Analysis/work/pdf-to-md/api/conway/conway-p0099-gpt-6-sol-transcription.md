it suffices to show that if $\mu\in M(K)$ and $\int g\,d\mu=0$ for each $g$ in $R(K,E)$, then $\int f\,d\mu=0$.

Let $R>0$ and let $\lambda$ be area measure. Pick $\rho>0$ such that $B(0;R)\subseteq B(z;\rho)$ for every $z$ in $K$. Then for $z$ in $K$,

$$
\begin{aligned}
\int_{B(0;R)}|z-w|^{-1}\,d\lambda(w)
&\leq \int_{B(z;\rho)}|z-w|^{-1}\,d\lambda(w)\\
&=\int_0^{2\pi}\int_0^\rho dr\,d\theta=2\pi\rho.
\end{aligned}
$$

If $\mu\in M(K)$, define $\tilde{\mu}\colon\mathbb{C}\to[0,\infty]$ by

$$
\tilde{\mu}(w)=\int\frac{d|\mu|(z)}{|z-w|}
$$

when the integral is finite, and $\tilde{\mu}(w)=\infty$ otherwise. The inequality above implies

$$
\begin{aligned}
\int_{B(0;R)}\tilde{\mu}(w)\,d\lambda(w)
&=\int_{B(0;R)}\int_K\frac{d|\mu|(z)}{|z-w|}\,d\lambda(w)\\
&=\int_K\int_{B(0;R)}\frac{d\lambda(w)}{|z-w|}\,d|\mu|(z)\\
&\leq 2\pi\rho\|\mu\|.
\end{aligned}
$$

Thus $\tilde{\mu}(w)<\infty$ a.e. $[\lambda]$.

**8.2. Lemma.** If $\mu\in M(K)$, then

$$
\hat{\mu}(w)=\int\frac{d\mu(z)}{z-w}
$$

is in $L^1(B(0;R),\lambda)$ for any $R>0$, $\hat{\mu}$ is analytic on $\mathbb{C}_\infty\setminus K$, and $\hat{\mu}(\infty)=0$.

**Proof.** The first statement follows from what came before the statement of this lemma. To show that $\hat{\mu}$ is analytic on $\mathbb{C}_\infty\setminus K$, let $w,w_0\in\mathbb{C}\setminus K$ and note that

$$
\frac{\hat{\mu}(w)-\hat{\mu}(w_0)}{w-w_0}
=\int_K\frac{d\mu(z)}{(z-w)(z-w_0)}.
$$

As $w\to w_0$, $[(z-w)(z-w_0)]^{-1}\to(z-w_0)^{-2}$ uniformly for $z$ in $K$, so that $\hat{\mu}$ has a derivative at $w_0$ and

$$
\frac{d\hat{\mu}}{dw}(w_0)=\int_K(z-w_0)^{-2}\,d\mu(z).
$$

So $\hat{\mu}$ is analytic on $\mathbb{C}\setminus K$. To show that it is analytic at infinity, note that $\hat{\mu}(z)\to0$ as $z\to\infty$, so infinity is a removable singularity. $\blacksquare$
