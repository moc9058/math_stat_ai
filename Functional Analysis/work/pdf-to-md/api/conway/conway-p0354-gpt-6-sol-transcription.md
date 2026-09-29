**Proof.** If $f\in L^1(\mathbb R)$,

$$
\begin{aligned}
\widehat{U_y f}(x)
&=(2\pi)^{-1/2}\int [U_y f](t)e^{-ixt}\,dt\\
&=(2\pi)^{-1/2}\int f(t-y)e^{-ixt}\,dt\\
&=(2\pi)^{-1/2}\int f(s)e^{-ix(s+y)}\,ds\\
&=e_{-y}(x)\hat f(x).
\end{aligned}
$$

The proof of the other equation is left as an exercise. $\blacksquare$

In the proof of the next lemma the fact that $\int_{-\infty}^{\infty}e^{-t^2}\,dt=\sqrt{\pi}$ is needed. Those who have never seen this can verify it by putting $I=\int_0^\infty e^{-x^2}\,dx$, noting that $I^2=\int_0^\infty\int_0^\infty e^{-(x^2+y^2)}\,dx\,dy$, and using polar coordinates.

**6.12. Lemma.** *If* $\varepsilon>0$ *and* $\rho_\varepsilon(t)=e^{-\varepsilon^2t^2}$, *then*

$$
\hat\rho_\varepsilon(x)=\frac{1}{\varepsilon\sqrt{2}}e^{-x^2/4\varepsilon^2}.
$$

**Proof.** Note that $\rho_\varepsilon\in\mathcal S$. By (6.8), $D\hat\rho_\varepsilon=(-ix\rho_\varepsilon)^{\wedge}$. Using integration by parts,

$$
\begin{aligned}
(D\hat\rho_\varepsilon)(x)
&=\frac{-i}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-\varepsilon^2t^2}te^{-ixt}\,dt\\
&=\frac{-i}{\sqrt{2\pi}}\left(\frac{-1}{2\varepsilon^2}\right)
\int_{-\infty}^{\infty}e^{-ixt}\,d(e^{-\varepsilon^2t^2})\\
&=\frac{-i}{2\varepsilon^2\sqrt{2\pi}}
\int_{-\infty}^{\infty}e^{-\varepsilon^2t^2}(-ix)e^{-ixt}\,dt\\
&=\frac{-x}{2\varepsilon^2}\hat\rho_\varepsilon(x).
\end{aligned}
$$

Let $\psi_\varepsilon(x)=e^{-x^2/4\varepsilon^2}$. Then both $\hat\rho_\varepsilon$ and $\psi_\varepsilon$ satisfy the differential equation $u'(x)=-(x/2\varepsilon^2)u(x)$. Hence $\hat\rho_\varepsilon=c\psi_\varepsilon$ for some constant $c$. But $\psi_\varepsilon(0)=1$, and

$$
\begin{aligned}
\hat\rho_\varepsilon(0)
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-\varepsilon^2t^2}\,dt\\
&=\frac{1}{\varepsilon\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-s^2}\,ds\\
&=\frac{1}{\varepsilon\sqrt{2\pi}}\sqrt{\pi}
=\frac{1}{\varepsilon\sqrt{2}}.
\end{aligned}
$$

$\blacksquare$
