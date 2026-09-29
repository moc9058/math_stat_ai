In fact, suppose $h\in\mathcal H$ and $h\perp\{g_a:g\in\mathcal H,\ a>0\}$. Then by (5.5), for every $a>0$ and every $g$ in $\mathcal H$,

$$
0=\int_0^a\langle U(t)h,g\rangle\,dt.
$$

Thus for every $g$ in $\mathcal H$, $\langle U(t)h,g\rangle=0$ a.e. on $\mathbb R$. Because $\mathcal H$ is separable there is a subset $\Delta$ of $\mathbb R$ having measure zero such that if $t\notin\Delta$, $\langle U(t)h,g\rangle=0$ whenever $g$ belongs to a preselected countable dense subset of $\mathcal H$. Thus $U(t)h=0$ if $t\notin\Delta$. But $\|h\|=\|U(t)h\|$, so $h=0$ and the claim is established.

Now if $s\in\mathbb R$,

$$
\begin{aligned}
\langle h,U(s)g_a\rangle
&=\langle U(-s)h,g_a\rangle\\
&=\int_0^a\langle U(t-s)h,g\rangle\,dt\\
&=\int_{-s}^{a-s}\langle U(t)h,g\rangle\,dt.
\end{aligned}
$$

Thus $\langle h,U(s)g_a\rangle\to\langle h,g_a\rangle$ as $s\to0$. By the claim and the fact that the group is uniformly bounded, $U:\mathbb R\to(\mathcal B(\mathcal H),\mathrm{WOT})$ is continuous at 0. By the group property, $U:\mathbb R\to(\mathcal B(\mathcal H),\mathrm{WOT})$ is continuous. Hence $U$ is SOT-continuous (Exercise 1). ■

We now turn our attention to the principal result of this section, Stone’s Theorem, which states that the converse of Theorem 5.1 is valid. Note that if $U(t)=\exp(itA)$ for a self-adjoint operator $A$, then part (d) of Theorem 5.1 instructs us how to recapture $A$. This is the route followed in the proof of Stone’s Theorem, proved in Stone [1932].

**5.6. Stone’s Theorem.** *If $U$ is a strongly continuous one parameter unitary group, then there is a self-adjoint operator $A$ such that $U(t)=\exp(itA)$.*

**Proof.** Begin by defining $\mathcal D$ to be the set of all vectors $h$ in $\mathcal H$ such that $\lim_{t\to0}t^{-1}[U(t)h-h]$ exists; since $0\in\mathcal D$, $\mathcal D\ne\varnothing$. Clearly $\mathcal D$ is a linear manifold in $\mathcal H$.

**5.7. Claim.** $\mathcal D$ is dense in $\mathcal H$.

Let $\mathcal L=$ all continuous functions $\phi$ on $\mathbb R$ such that $\phi\in L^1(0,\infty)$. Hence for any $h$ in $\mathcal H$, $t\mapsto\phi(t)U(t)h$ is a continuous function of $\mathbb R$ into $\mathcal H$. Because $\|U(t)h\|=\|h\|$ for all $t$, a Riemann integral, $\int_0^\infty\phi(t)U(t)h\,dt$, can be defined and is a vector in $\mathcal H$. Put

$$
\begin{aligned}
\text{5.8}\qquad T_\phi h
&=\int_0^\infty\phi(t)U(t)h\,dt.
\end{aligned}
$$

It is easy to see that $T_\phi:\mathcal H\to\mathcal H$ is linear and bounded with $\|T_\phi\|\leq\int_0^\infty|\phi(t)|\,dt$.
