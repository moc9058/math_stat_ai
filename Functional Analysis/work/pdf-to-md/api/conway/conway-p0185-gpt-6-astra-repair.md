170 $\qquad$ VI. Linear Operators on a Banach Space

**1.11. Claim.** $B^*(y^*+\ker A^*)=A^*y^*$ for all $y^*$ in $\mathcal Y^*$.

To see this, let $x\in\mathcal X$ and $y^*\in\mathcal Y^*$. Making the appropriate identifications as in (V.2.2) and (V.2.3) gives
$$
\begin{aligned}
\langle x+\ker A,B^*(y^*+\ker A^*)\rangle
&=\langle B(x+\ker A),y^*+\ker A^*\rangle\\
&=\langle Ax,y^*+(\operatorname{ran}A)^\perp\rangle\\
&=\langle Ax,y^*\rangle
=\langle x,A^*y^*\rangle\\
&=\langle x+{}^\perp(\operatorname{ran}A^*),A^*y^*\rangle\\
&=\langle x+\ker A,A^*y^*\rangle.
\end{aligned}
$$
Since $x$ was arbitrary. (1.11) is established.

Note that Claim 1.11 implies that $\operatorname{ran}B^*=\operatorname{ran}A^*$. Hence $\operatorname{ran}A^*$ is weak* (resp., norm) closed if and only if $\operatorname{ran}B^*$ is weak* (resp., norm) closed.

This discussion shows that the theorem is equivalent to the analogous theorem in which there is the additional hypothesis that $A$ is injective and has dense range. It is assumed, therefore, that $\ker A=(0)$ and $\operatorname{cl}(\operatorname{ran}A)=\mathcal Y$.

(a)$\Rightarrow$(b): Since $\operatorname{ran}A$ is closed, the additional hypothesis implies that $A$ is bijective. By the Inverse Mapping Theorem, $A^{-1}\in\mathcal B(\mathcal Y,\mathcal X)$. Hence $A^*$ is invertible (1.4c). Since $A^*$ is invertible, $\operatorname{ran}A^*=\mathcal X^*$ and hence is weak* closed.

(c)$\Rightarrow$(b): Since $\operatorname{ran}A$ is dense in $\mathcal Y$, $\ker A^*=(\operatorname{ran}A)^\perp$ (1.8) $=(0)$. Thus $A^*:\mathcal Y^*\to\operatorname{ran}A^*$ is a bijection. Since $\operatorname{ran}A^*$ is norm closed, it is a Banach space. By the Inverse Mapping Theorem, there is a constant $c>0$ such that $\|A^*y^*\|\geqslant c\|y^*\|$ for all $y^*$ in $\mathcal Y^*$.

To show that $\operatorname{ran}A^*$ is weak* closed, the Krein–Smulian Theorem (V.12.6) will be used. Thus suppose $\{A^*y_i^*\}$ is a net in $\operatorname{ran}A^*$ with $\|A^*y_i^*\|\leqslant1$ such that $A^*y_i^*\to x^*$ $\sigma(\mathcal X^*,\mathcal X)$ for some $x^*$ in $\mathcal X^*$. Thus $\|y_i^*\|\leqslant c^{-1}$ for all $y_i^*$. By Alaoglu’s Theorem there is a $y^*$ in $\mathcal Y^*$ such that $y_i^*\xrightarrow[\mathrm{cl}]{}y^*$ $\sigma(\mathcal Y^*,\mathcal Y)$. Thus (1.3), $A^*y_i^*\xrightarrow[\mathrm{cl}]{}A^*y^*$ $\sigma(\mathcal X^*,\mathcal X)$, and so $x^*=A^*y^*\in\operatorname{ran}A^*$. By (V.12.6), $\operatorname{ran}A^*$ is weak* closed.

(b)$\Rightarrow$(a): Since $\operatorname{ran}A^*$ is weak* closed, $\operatorname{ran}A^*=(\ker A)^\perp=\mathcal X^*$. Also $\ker A^*=(\operatorname{ran}A)^\perp=(0)$ since $A$ has dense range. Thus $A^*$ is a bijection and is thus invertible. By Proposition 1.9, $A$ is invertible and thus has closed range. $\blacksquare$

A proof that condition (c) in the preceding theorem implies (a) which avoids the weak* topology can be found in Kaufman [1966].

## EXERCISES

1. Prove Proposition 1.3.

2. Complete the proof of Proposition 1.4.

3. Verify the statement made in (1.5).

4. Verify the statement made in (1.6).

5. Verify the statement made in (1.7).

6. Let $1\leqslant p<\infty$ and define $S:l^p\to l^p$ by $S(\alpha_1,\alpha_2,\ldots)=(0,\alpha_1,\alpha_2,\ldots)$. Compute $S^*$.

7. Let $A\in\mathcal B(c_0)$ and for $n\geqslant1$, define $e_n$ in $c_0$ by $e_n(n)=1$ and $e_n(m)=0$ for $m\neq n$. Put $\alpha_{mn}=(Ae_n)(m)$ for $m,n\geqslant1$. Prove: (a) $M\equiv\sup_m\sum_{n=1}^{\infty}|\alpha_{mn}|<\infty$; (b) for every
