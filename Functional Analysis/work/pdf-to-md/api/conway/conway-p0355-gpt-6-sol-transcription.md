**6.13. Proposition.** *If $\psi\in L^{1}(\mathbb R)$ such that $(2\pi)^{-1/2}\int_{\mathbb R}\psi(x)\,dx=1$ and if, for $\varepsilon>0$, $\psi_\varepsilon(x)=\varepsilon^{-1}\psi(x/\varepsilon)$, then for every $f\in C_0(\mathbb R)$, $\psi_\varepsilon*f(x)\to f(x)$ uniformly on $\mathbb R$.*

**Proof.** Note that $(2\pi)^{-1/2}\int\psi_\varepsilon(x)\,dx=1$ for all $\varepsilon>0$. Hence for any $x$ in $\mathbb R$,

$$
\begin{aligned}
\psi_\varepsilon*f(x)-f(x)
&=(2\pi)^{-1/2}\int [f(x-t)-f(x)]\frac{1}{\varepsilon}\psi\left(\frac{t}{\varepsilon}\right)\,dt\\
&=(2\pi)^{-1/2}\int [f(x-s\varepsilon)-f(x)]\psi(s)\,ds.
\end{aligned}
$$

Put $\omega(y)=\sup\{|f(x-y)-f(x)|:y\in\mathbb R\}$. Now $f$ is uniformly continuous (Why?), so if $\varepsilon>0$, then there is a $\delta>0$ such that $\omega(y)<\varepsilon$ if $|y|<\delta$. Thus $\omega(y)\to0$ as $|y|\to0$. Moreover, the inequality above implies

$$
\|\psi_\varepsilon*f-f\|_\infty
\leqslant (2\pi)^{-1/2}\int\omega(s\varepsilon)|\psi(s)|\,ds.
$$

Since $\psi\in L^{1}(\mathbb R)$, the Lebesgue Dominated Convergence Theorem implies that $\|\psi_{\varepsilon_k}*f-f\|_\infty\to0$ whenever $\varepsilon_k\to0$. This proves the proposition. $\blacksquare$

The next result is often called the *Multiplication Formula*. Remember that if $f\in L^{1}(\mathbb R)$, $\hat f\in C_0(\mathbb R)$. Hence $\hat f g\in L^{1}(\mathbb R)$ when both $f$ and $g\in L^{1}(\mathbb R)$.

**6.14. Theorem.** *If $f,g\in L^{1}(\mathbb R)$, then*

$$
\int_{\mathbb R}\hat f(x)g(x)\,dx
=
\int_{\mathbb R}f(x)\hat g(x)\,dx.
$$

**Proof.** The proof is an easy consequence of Fubini’s Theorem. In fact, if $f,g\in L^{1}(\mathbb R)$, then

$$
\begin{aligned}
\int\hat f(x)g(x)\,dx
&=\int\left[\frac{1}{\sqrt{2\pi}}\int f(t)e^{-ixt}\,dt\right]g(x)\,dx\\
&=\int f(t)\left[\frac{1}{\sqrt{2\pi}}\int g(x)e^{-ixt}\,dx\right]dt\\
&=\int f(t)\hat g(t)\,dt.
\end{aligned}
$$

$\blacksquare$

**6.15. Inversion Formula.** *If $\phi\in\mathcal S$, then*

$$
\phi(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat\phi(t)e^{ixt}\,dt.
$$

**Proof.** Let $\rho_\varepsilon(x)=e^{-\varepsilon^{2}x^{2}}$ and put $\psi(x)=\hat\rho_1(x)$. Then by Lemma 6.12
