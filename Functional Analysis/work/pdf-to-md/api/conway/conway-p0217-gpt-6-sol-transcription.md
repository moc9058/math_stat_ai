closed curves in $G$ such that $\sigma(a)\subseteq\operatorname{ins}\Gamma$. Let $\Lambda$ be a positively oriented system of closed curves in $G$ such that $(\operatorname{ins}\Gamma)\cup\{\Gamma\}=\operatorname{cl}(\operatorname{ins}\Gamma)\subseteq\operatorname{ins}\Lambda$. Then

$$
\begin{aligned}
f(a)g(a)
&=-\frac{1}{4\pi^{2}}
\left[\int_{\Gamma}f(z)(z-a)^{-1}\,dz\right]
\left[\int_{\Lambda}g(\zeta)(\zeta-a)^{-1}\,d\zeta\right]\\
&=-\frac{1}{4\pi^{2}}\int_{\Gamma}\int_{\Lambda}
f(z)g(\zeta)(z-a)^{-1}(\zeta-a)^{-1}\,d\zeta\,dz\\
\text{[by (3.9b)]}\qquad
&=-\frac{1}{4\pi^{2}}\int_{\Gamma}\int_{\Lambda}
f(z)g(\zeta)
\left[\frac{(z-a)^{-1}-(\zeta-a)^{-1}}{\zeta-z}\right]
\,d\zeta\,dz\\
&=-\frac{1}{4\pi^{2}}\int_{\Gamma}f(z)
\left[\int_{\Lambda}\frac{g(\zeta)}{\zeta-z}\,d\zeta\right]
(z-a)^{-1}\,dz\\
&\quad+\frac{1}{4\pi^{2}}\int_{\Lambda}g(\zeta)
\left[\int_{\Gamma}\frac{f(z)}{\zeta-z}\,dz\right]
(\zeta-a)^{-1}\,d\zeta.
\end{aligned}
$$

But for $\zeta$ on $\Lambda$, $\zeta\in\operatorname{out}\Gamma$ and hence $\int_{\Gamma}[f(z)/(\zeta-z)]\,dz=0$ (Cauchy’s Theorem). If $z\in\{\Gamma\}$, then $z\in\operatorname{ins}\Lambda$ and so $\int_{\Lambda}[g(\zeta)/(\zeta-z)]\,d\zeta=2\pi i g(z)$. Hence

$$
\begin{aligned}
f(a)g(a)
&=\frac{1}{2\pi i}\int_{\Gamma}f(z)g(z)(z-a)^{-1}\,dz\\
&=(fg)(a).
\end{aligned}
$$

The proof that $(\alpha f+\beta g)(a)=\alpha f(a)+\beta g(a)$ is left to the reader.

(c) and (d). Let $f(z)=z^{k}$, $k\geq 0$. Let $\gamma(t)=R\exp(2\pi it)$, $0\leq t\leq 1$, where $R>\|a\|$. So $\sigma(a)\subset\operatorname{ins}\gamma$, and hence

$$
\begin{aligned}
f(a)
&=\frac{1}{2\pi i}\int_{\gamma}z^{k}(z-a)^{-1}\,dz\\
&=\frac{1}{2\pi i}\int_{\gamma}z^{k-1}
\left(1-\frac{a}{z}\right)^{-1}\,dz\\
&=\frac{1}{2\pi i}\int_{\gamma}z^{k-1}
\sum_{n=0}^{\infty}a^{n}/z^{n}\,dz,
\end{aligned}
$$

since $\|a/z\|<1$ for $|z|=R$. Since this infinite series converges uniformly for $z$ on $\gamma$,

$$
f(a)=\sum_{n=0}^{\infty}
\left[\frac{1}{2\pi i}\int_{\gamma}\frac{1}{z^{n-k+1}}\,dz\right]a^{n}.
$$

If $n\ne k$, then $z^{-(n-k+1)}$ has a primitive and hence $\int_{\gamma}z^{-(n-k+1)}\,dz=0$. For $n=k$ this integral becomes $\int_{\gamma}z^{-1}\,dz=2\pi i$. Hence $f(a)=a^{k}$.

(e) Let $\Gamma=\{\gamma_{1},\ldots,\gamma_{m}\}$ be a positively oriented system of closed curves in
