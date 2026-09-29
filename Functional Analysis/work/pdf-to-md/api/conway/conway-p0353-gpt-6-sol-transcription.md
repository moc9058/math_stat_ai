Using integration by parts,

$$
\begin{aligned}
(D\phi)^\wedge(y)
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-iyt}\phi'(t)\,dt\\
&=-\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(t)\frac{d}{dt}[e^{-iyt}]\,dt\\
&=\frac{iy}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-iyt}\phi(t)\,dt.
\end{aligned}
$$

That is, $(D\phi)^\wedge=(ix)\hat\phi$. By induction,

$$
\tag{6.10}
(D^n\phi)^\wedge=(ix)^n\hat\phi
$$

for all $n\geq 0$. Combining (6.9) and (6.10) gives (6.8).

By (6.8) if $m,n\geq 0$, then for $\phi$ in $\mathcal S$,

$$
\begin{aligned}
\|\hat\phi\|_{m,n}
&=\sup\{|x^m(D^n\hat\phi)(x)|:x\in\mathbb R\}\\
&=\sup\left\{\left|\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}
e^{-ixt}\left(\frac{d}{dt}\right)^m[(-it)^n\phi(t)]\,dt\right|:x\in\mathbb R\right\}\\
&\leq\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}
\left|\left(\frac{d}{dt}\right)^m[t^n\phi(t)]\right|\,dt\\
&<\infty
\end{aligned}
$$

since $D^m(x^n\phi)\in L^1(\mathbb R)$ (6.5).

(c) This is an easy exercise in integration theory and is left to the reader. $\blacksquare$

The fact that $\hat f(x)\to 0$ as $|x|\to\infty$ is called the *Riemann–Lebesgue Lemma*.

The process now begins whereby it will be shown that the Fourier transform on $L^1\cap L^2$ extends to a unitary operator on $L^2(\mathbb R)$. Moreover, the adjoint of this unitary will be calculated and it will be shown that if $id/dx$ is conjugated by this unitary, then the resulting self-adjoint operator is $M_x$.

Changing notation a little, let $U_y$ [instead of $U(y)$] denote the translation operator. Moreover, think of $U_y$ as operating on all of the $L^p$ spaces, not just $L^2$, so $(U_yf)(x)=f(x-y)$ for $f$ in $L^p(\mathbb R)$. Also, let $e_y$ be the function $e_y(x)=\exp(ixy)$.

**6.11. Proposition.** If $f\in L^1(\mathbb R)$ and $y\in\mathbb R$, then

$$
\begin{aligned}
[U_yf]^\wedge&=e_{-y}\hat f,\\
[e_yf]^\wedge&=U_y\hat f.
\end{aligned}
$$
