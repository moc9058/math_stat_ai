$U(-t)$. Hence

$$
\begin{aligned}
\langle Bh,g\rangle
&=-i\lim_{t\to0}\left\langle h,\frac{U(-t)g-g}{t}\right\rangle\\
&=\lim_{t\to0}\left\langle h,-i\left[\frac{U(-t)g-g}{-t}\right]\right\rangle\\
&=\langle h,Bg\rangle.
\end{aligned}
$$

Hence $B$ is a symmetric extension of $A$. Since self-adjoint operators are maximal symmetric operators (2.11), $B=A$ and $\mathcal D=\operatorname{dom}A$. $\blacksquare$

The following definition is inspired by the preceding theorem.

**5.3. Definition.** A *strongly continuous one parameter unitary group* is a function $U:\mathbb R\to\mathcal B(\mathcal H)$ such that for all $s$ and $t$ in $\mathbb R$: (a) $U(t)$ is a unitary operator; (b) $U(s+t)=U(s)U(t)$; (c) if $h\in\mathcal H$ and $t_0\in\mathbb R$, then $U(t)h\to U(t_0)h$ as $t\to t_0$.

Note that by Theorem 5.1, if $A$ is self-adjoint, then $U(t)=\exp(itA)$ defines a strongly continuous one parameter unitary group.

Also, $U(0)=1$ and $U(-t)=U(t)^{-1}$, so that $\{U(t):t\in\mathbb R\}$ is indeed a group. Property (c) also implies that $U:\mathbb R\to(\mathcal B(\mathcal H),\mathrm{SOT})$ is continuous. By Exercise 1, if $U$ is only assumed to be WOT-continuous, then $U$ is SOT-continuous. However, this condition can be relaxed even further as the following result of von Neumann [1932] shows.

**5.4. Theorem.** *If $\mathcal H$ is separable, $U:\mathbb R\to\mathcal B(\mathcal H)$ satisfies conditions (a) and (b) of Definition 5.3, and if for all $h,g$ in $\mathcal H$ the function $t\mapsto\langle U(t)h,g\rangle$ is Lebesgue measurable, then $U$ is a strongly continuous one-parameter unitary group.*

**Proof.** If $0<a<\infty$ and $h,g\in\mathcal H$, then $t\mapsto\langle U(t)h,g\rangle$ is a bounded measurable function on $[0,a]$ and hence

$$
\int_0^a|\langle U(t)h,g\rangle|\,dt\leq a\|h\|\|g\|.
$$

Thus

$$
h\mapsto\int_0^a\langle U(t)h,g\rangle\,dt
$$

is a bounded linear function on $\mathcal H$. Therefore there is a $g_a$ in $\mathcal H$ such that

$$
\langle h,g_a\rangle=\int_0^a\langle U(t)h,g\rangle\,dt \tag{5.5}
$$

and $\|g_a\|\leq a\|g\|$.

**Claim.** $\{g_a:g\in\mathcal H,\ a>0\}$ is total in $\mathcal H$.
