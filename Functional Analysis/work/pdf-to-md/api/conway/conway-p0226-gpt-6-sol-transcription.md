or essential singularity) will reveal something of the nature of $\lambda_0$ as an element of $\sigma(A)$. First it is helpful to get the precise form of the Laurent expansion of $(z-A)^{-1}$ about $\lambda_0$.

**6.11. Lemma.** If $\lambda_0$ is an isolated point of $\sigma(A)$, then

$$
(z-A)^{-1}=\sum_{n=-\infty}^{\infty}(z-\lambda_0)^n A_n
$$

for $0<|z-\lambda_0|<r_0=\operatorname{dist}(\lambda_0,\sigma(A)\setminus\{\lambda\})$, where

$$
A_n=\frac{1}{2\pi i}\int_\gamma (z-\lambda_0)^{-n-1}(z-A)^{-1}\,dz
$$

for $\gamma=$ any circle centered at $\lambda_0$ with radius $<r_0$.

The proof follows the lines of the usual Laurent series development (Conway [1978]).

**6.12. Proposition.** If $\lambda_0$ is an isolated point of $\sigma(A)$, then $\lambda_0$ is a pole of $(z-A)^{-1}$ of order $n$ if and only if $(\lambda_0-A)^nE(\lambda_0)=0$ and $(\lambda_0-A)^{n-1}E(\lambda_0)\ne0$.

**Proof.** Let $(z-A)^{-1}=\sum_{n=-\infty}^{\infty}(z-\lambda_0)^nA_n$ as is (6.11). Now $\lambda_0$ is a pole of order $n$ if and only if $A_{-n}\ne0$ and $A_{-k}=0$ for $k>n$. Let $\Gamma$ be a positively oriented system of curves such that $\sigma(A)\setminus\{\lambda_0\}\subseteq\operatorname{ins}\Gamma$ and $\lambda_0\in\operatorname{out}\Gamma$. Let $\gamma$ be a circle centered at $\lambda_0$ and contained in $\operatorname{out}\Gamma$. Let $e(z)\equiv1$ in a neighborhood of $\gamma\cup\operatorname{ins}\gamma$ and $e(z)\equiv0$ in a neighborhood of $\Gamma\cup\operatorname{ins}\Gamma$. So $e\in\operatorname{Hol}(A)$ and $e(A)=E(\lambda_0)$. If $k\geq1$,

$$
\begin{aligned}
A_{-k}
&=\frac{1}{2\pi i}\int_\gamma (z-\lambda_0)^{k-1}(z-A)^{-1}\,dz\\
&=\frac{1}{2\pi i}\int_{\gamma+\Gamma}e(z)(z-\lambda_0)^{k-1}(z-A)^{-1}\,dz\\
&=E(\lambda_0)(A-\lambda_0)^{k-1}
\end{aligned}
$$

since $\sigma(A)\subseteq\operatorname{ins}(\gamma+\Gamma)=\operatorname{ins}\gamma\cup\operatorname{ins}\Gamma$. The proposition now follows. $\blacksquare$

**6.13. Corollary.** If $\lambda_0$ is an isolated point of $\sigma(A)$ and is a pole of $(z-A)^{-1}$, then $\lambda_0\in\sigma_p(A)$.

In fact, the preceding result implies that if $n$ is the order of the pole, then $(0)\ne(\lambda_0-A)^{n-1}E(\lambda_0)\mathcal{X}\subseteq\ker(A-\lambda_0)$.

**6.14. Example.** A measurable function $k:[0,1]\times[0,1]\to\mathbb{C}$ is called a *Volterra kernel* if $k$ is bounded and $k(x,y)=0$ when $x<y$. If $1\leq p\leq\infty$ and
