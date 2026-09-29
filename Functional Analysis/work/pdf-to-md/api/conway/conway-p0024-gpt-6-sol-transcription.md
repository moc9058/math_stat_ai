Since $K$ is convex, $\frac12(k_n+k_m)\in K$. Hence, $\|\frac12(k_n+k_m)\|^2\geq d^2$. If $\varepsilon>0$, choose $N$ such that for $n\geq N$, $\|k_n\|^2<d^2+\frac14\varepsilon^2$. By the equation above, if $n,m\geq N$, then

$$
\left\|\frac{k_n-k_m}{2}\right\|^2
<\frac12\left(2d^2+\frac12\varepsilon^2\right)-d^2
=\frac14\varepsilon^2.
$$

Thus, $\|k_n-k_m\|<\varepsilon$ for $n,m\geq N$ and $\{k_n\}$ is a Cauchy sequence. Since $\mathcal H$ is complete and $K$ is closed, there is a $k_0$ in $K$ such that $\|k_n-k_0\|\to0$. Also for all $k_n$,

$$
\begin{aligned}
d\leq\|k_0\|&=\|k_0-k_n+k_n\|\\
&\leq\|k_0-k_n\|+\|k_n\|\to d.
\end{aligned}
$$

Thus $\|k_0\|=d$.

To prove that $k_0$ is unique, suppose $h_0\in K$ such that $\|h_0\|=d$. By convexity, $\frac12(k_0+h_0)\in K$. Hence

$$
d\leq\left\|\frac12(h_0+k_0)\right\|
\leq\frac12(\|h_0\|+\|k_0\|)=d.
$$

So $\|\frac12(h_0+k_0)\|=d$. The Parallelogram Law implies

$$
d^2=\left\|\frac{h_0+k_0}{2}\right\|^2
=d^2-\left\|\frac{h_0-k_0}{2}\right\|^2;
$$

hence $h_0=k_0$. $\blacksquare$

If the convex set in the preceding theorem is in fact a closed linear subspace of $\mathcal H$, more can be said.

**2.6. Theorem.** *If $\mathcal M$ is a closed linear subspace of $\mathcal H$, $h\in\mathcal H$, and $f_0$ is the unique element of $\mathcal M$ such that $\|h-f_0\|=\operatorname{dist}(h,\mathcal M)$, then $h-f_0\perp\mathcal M$. Conversely, if $f_0\in\mathcal M$ such that $h-f_0\perp\mathcal M$, then $\|h-f_0\|=\operatorname{dist}(h,\mathcal M)$.*

**Proof.** Suppose $f_0\in\mathcal M$ and $\|h-f_0\|=\operatorname{dist}(h,\mathcal M)$. If $f\in\mathcal M$, then $f_0+f\in\mathcal M$ and so $\|h-f_0\|^2\leq\|h-(f_0+f)\|^2=\|(h-f_0)-f\|^2=\|h-f_0\|^2-2\operatorname{Re}\langle h-f_0,f\rangle+\|f\|^2$. Thus

$$
2\operatorname{Re}\langle h-f_0,f\rangle\leq\|f\|^2
$$

for any $f$ in $\mathcal M$. Fix $f$ in $\mathcal M$ and substitute $te^{i\theta}f$ for $f$ in the preceding inequality, where $\langle h-f_0,f\rangle=re^{i\theta}$, $r\geq0$. This yields $2\operatorname{Re}\{te^{-i\theta}re^{i\theta}\}\leq t^2\|f\|^2$, or $2tr\leq t^2\|f\|^2$. Letting $t\to0$, we see that $r=0$; that is, $h-f_0\perp f$.

For the converse, suppose $f_0\in\mathcal M$ such that $h-f_0\perp\mathcal M$. If $f\in\mathcal M$, then $h-f_0\perp f_0-f$ so that

$$
\begin{aligned}
\|h-f\|^2&=\|(h-f_0)+(f_0-f)\|^2\\
&=\|h-f_0\|^2+\|f_0-f\|^2\\
&\geq\|h-f_0\|^2.
\end{aligned}
$$

Thus $\|h-f_0\|=\operatorname{dist}(h,\mathcal M)$. $\blacksquare$
