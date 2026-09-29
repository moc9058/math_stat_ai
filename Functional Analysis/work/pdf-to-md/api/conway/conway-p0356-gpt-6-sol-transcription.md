$\psi_\varepsilon(x)=\varepsilon^{-1}\psi(x/\varepsilon)=\hat{\rho}_\varepsilon(x)$. Also,

$$
(2\pi)^{-1/2}\int\psi(x)\,dx
=(2\pi)^{-1/2}\int_{-\infty}^{\infty}2^{-1/2}e^{-x^2/4}\,dx
=1.
$$

So $\psi_\varepsilon*h(x)\to h(x)$ uniformly for any $h$ in $C_0(\mathbb R)$. If $\phi\in\mathcal S$, put $f=\phi$ and $g=e_x\rho_\varepsilon$ in (6.14). By Proposition 6.11 and Lemma 6.12, $\hat g=U_x\hat\rho_\varepsilon=U_x\psi_\varepsilon$. Thus

$$
\begin{aligned}
\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat\phi(t)e^{itx}e^{-\varepsilon^2t^2}\,dt
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(t)\psi_\varepsilon(t-x)\,dt\\
&=\phi*\psi_\varepsilon(x)\\
&\to\phi(x)
\end{aligned}
$$

as $\varepsilon\to0$. The Lebesgue Dominated Convergence Theorem implies the left-hand side converges to $(2\pi)^{-1/2}\int\hat\phi(t)e^{ixt}\,dt$ and the theorem is proved. $\blacksquare$

In many ways the next result is a rephrasing of the preceding theorem.

**6.16. Theorem.** *If $\mathcal F:\mathcal S\to\mathcal S$ is defined by $\mathcal F\phi=\hat\phi$, $\mathcal F$ is a bijection with*

$$
(\mathcal F^{-1}\phi)(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(t)e^{ixt}\,dt.
$$

*Moreover, if $\mathcal S$ is given the topology induced by the seminorms $\{\|\cdot\|_{m,n}:m,n\geq0\}$ that were defined in (6.4), $\mathcal F$ is a homeomorphism.*

**Proof.** By (6.7b), $\mathcal F\mathcal S\subseteq\mathcal S$. The preceding theorem says that $\mathcal F$ is bijective and gives the formula for $\mathcal F^{-1}$. The proof of the topological statement is left to the reader. $\blacksquare$

**6.17. Plancherel’s Theorem.** *If $\phi\in\mathcal S$, then $\|\phi\|_2=\|\hat\phi\|_2$ and the Fourier transform $\mathcal F$ extends to a unitary operator on $L^2(\mathbb R)$.*

**Proof.** Let $\phi\in\mathcal S$ and put $\psi(x)=\overline{\phi(-x)}$. So $\rho=\phi*\psi\in L^1(\mathbb R)$ and $\hat\rho=\hat\phi\hat\psi$.

An easy calculation shows that $\hat\psi=\overline{\hat\phi}$; hence $\hat\rho=|\hat\phi|^2$. Also, the Inversion Formula shows that $\rho(0)=(2\pi)^{-1/2}\int\hat\rho(x)\,dx=(2\pi)^{-1/2}\int|\hat\phi(x)|^2\,dx$. Thus

$$
\begin{aligned}
\int|\hat\phi(x)|^2\,dx
&=(2\pi)^{1/2}\rho(0)\\
&=(2\pi)^{1/2}\phi*\psi(0)\\
&=\int\phi(x)\psi(0-x)\,dx\\
&=\int|\phi(x)|^2\,dx.
\end{aligned}
$$
