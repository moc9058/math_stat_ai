(d) *if* $h\in\operatorname{dom}A$, *then*

$$
\lim_{t\to 0}\frac{1}{t}[U(t)h-h]=iAh; \tag{5.2}
$$

(e) *if* $h\in\mathcal H$ *and* $\lim_{t\to 0}t^{-1}[U(t)h-h]$ *exists, then* $h\in\operatorname{dom}A$. *Consequently, $\operatorname{dom}A$ is invariant under each $U(t)$.*

**Proof.** As was mentioned, part (a) is an exercise. Since $\exp(itx)\exp(isx)=\exp(i(s+t)x)$ for all $x$ in $\mathbb R$, (b) is a consequence of the functional calculus for normal operators [(4.10) and (4.11)]. Also note that $U(0)U(t)=U(t)$, so that $U(0)=1$.

(c) If $h\in\mathcal H$, then $\|U(t)h-U(s)h\|=\|U(t-s+s)h-U(s)h\|=$ [by (b)] $\|U(s)[U(t-s)h-h]\|=\|U(t-s)h-h\|$ since $U(s)$ is unitary. Thus (c) will be shown if it is proved that $\|U(t)h-h\|\to 0$ as $t\to 0$. If $A=\int_{-\infty}^{\infty}x\,dE(x)$ is the spectral decomposition of $A$, then

$$
\|U(t)h-h\|^2=\int_{-\infty}^{\infty}|e^{itx}-1|^2\,dE_{h,h}(x).
$$

Now $E_{h,h}$ is a finite measure on $\mathbb R$; for each $x$ in $\mathbb R$, $|e^{itx}-1|^2\to 0$ as $t\to 0$; and $|e^{itx}-1|^2\leq 4$. So the Lebesgue Dominated Convergence Theorem implies that $U(t)h\to h$ as $t\to 0$.

(d) Note that $t^{-1}[U(t)-1]-iA=f_t(A)$, where $f_t(x)=t^{-1}[\exp(itx)-1]-ix$. So if $h\in\operatorname{dom}A$,

$$
\begin{aligned}
\left\|\frac{1}{t}[U(t)h-h]-iAh\right\|^2
&=\|f_t(A)h\|^2\\
&=\int_{-\infty}^{\infty}\left|\frac{e^{itx}-1}{t}-ix\right|^2\,dE_{h,h}(x).
\end{aligned}
$$

As $t\to 0$, $t^{-1}[e^{itx}-1]-ix\to 0$ for all $x$ in $\mathbb R$. Also, $|e^{is}-1|\leq |s|$ for all real numbers $s$ (Why?), hence $|f_t(x)|\leq |t|^{-1}|e^{itx}-1|+|x|\leq 2|x|$. But $|x|\in L^2(E_{h,h})$ by Theorem 4.7(a). So again the Lebesgue Dominated Convergence Theorem implies that (5.2) is true.

(e) Let $\mathcal D=\{h\in\mathcal H:\lim_{t\to 0}t^{-1}[U(t)h-h]\text{ exists in }\mathcal H\}$. For $h$ in $\mathcal D$, let $Bh$ be defined by

$$
Bh=-i\lim_{t\to 0}\frac{U(t)h-h}{t}.
$$

It is easy to see that $\mathcal D$ is a linear manifold in $\mathcal H$ and $B$ is linear on $\mathcal D$. Also, by (d), $B\supseteq A$ so that $B$ is densely defined. Moreover, if $h,g\in\mathcal D$, then

$$
\langle Bh,g\rangle=-i\lim_{t\to 0}\left\langle\frac{U(t)h-h}{t},g\right\rangle.
$$

By (b) and the fact that each $U(t)$ is unitary, it follows that $U(t)^*=U(t)^{-1}=$
