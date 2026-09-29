**1.4. The Cauchy–Bunyakowsky–Schwarz Inequality.** *If* $\langle\cdot,\cdot\rangle$ *is a semi-inner product on* $\mathcal{X}$, *then*

$$
|\langle x,y\rangle|^2\leqslant\langle x,x\rangle\langle y,y\rangle
$$

*for all* $x$ *and* $y$ *in* $\mathcal{X}$. *Moreover, equality occurs if and only if there are scalars* $\alpha$ *and* $\beta$, *both not* $0$, *such that* $\langle\beta x+\alpha y,\beta x+\alpha y\rangle=0$.

**Proof.** If $\alpha\in\mathbf{F}$ and $x$ and $y\in\mathcal{X}$, then

$$
\begin{aligned}
0&\leqslant\langle x-\alpha y,x-\alpha y\rangle\\
&=\langle x,x\rangle-\alpha\langle y,x\rangle-\bar{\alpha}\langle x,y\rangle
+|\alpha|^2\langle y,y\rangle.
\end{aligned}
$$

Suppose $\langle y,x\rangle=be^{i\theta}$, $b\geqslant0$, and let $\alpha=e^{-i\theta}t$, $t$ in $\mathbf{R}$. The above inequality becomes

$$
\begin{aligned}
0&\leqslant\langle x,x\rangle-e^{-i\theta}tbe^{i\theta}
-e^{i\theta}tbe^{-i\theta}+t^2\langle y,y\rangle\\
&=\langle x,x\rangle-2bt+t^2\langle y,y\rangle\\
&=c-2bt+at^2\equiv q(t),
\end{aligned}
$$

where $c=\langle x,x\rangle$ and $a=\langle y,y\rangle$. Thus $q(t)$ is a quadratic polynomial in the real variable $t$ and $q(t)\geqslant0$ for all $t$. This implies that the equation $q(t)=0$ has at most one real solution $t$. From the quadratic formula we find that the discriminant is not positive; that is, $0\geqslant4b^2-4ac$. Hence

$$
0\geqslant b^2-ac=|\langle x,y\rangle|^2-\langle x,x\rangle\langle y,y\rangle,
$$

proving the inequality.

The proof of the necessary and sufficient condition for equality is left to the reader. ■

The inequality in (1.4) will be referred to as the CBS inequality.

**1.5. Corollary.** *If* $\langle\cdot,\cdot\rangle$ *is a semi-inner product on* $\mathcal{X}$ *and* $\|x\|\equiv\langle x,x\rangle^{1/2}$ *for all* $x$ *in* $\mathcal{X}$, *then*

(a) $\|x+y\|\leqslant\|x\|+\|y\|$ *for* $x,y$ *in* $\mathcal{X}$,

(b) $\|\alpha x\|=|\alpha|\|x\|$ *for* $\alpha$ *in* $\mathbf{F}$ *and* $x$ *in* $\mathcal{X}$.

*If* $\langle\cdot,\cdot\rangle$ *is an inner product, then*

(c) $\|x\|=0$ *implies* $x=0$.

**Proof.** The proofs of (b) and (c) are left as an exercise. To see (a), note that for $x$ and $y$ in $\mathcal{X}$,

$$
\begin{aligned}
\|x+y\|^2&=\langle x+y,x+y\rangle\\
&=\|x\|^2+\langle y,x\rangle+\langle x,y\rangle+\|y\|^2\\
&=\|x\|^2+2\operatorname{Re}\langle x,y\rangle+\|y\|^2.
\end{aligned}
$$
