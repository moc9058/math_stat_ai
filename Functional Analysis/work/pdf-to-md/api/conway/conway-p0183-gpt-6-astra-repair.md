168 VI. Linear Operators on a Banach Space

$(A^*)^*\equiv A^{**}$ can be defined,

$$
A^{**}:\mathcal X^{**}\to\mathcal Y^{**},
$$

$$
\langle A^{**}x^{**},y^*\rangle
=\langle x^{**},A^*y^*\rangle
$$

for $x^{**}$ in $\mathcal X^{**}$ and $y^*$ in $\mathcal Y^*$.

Suppose $x\in\mathcal X$ and consider $x$ as an element of $\mathcal X^{**}$ via the natural embedding of $\mathcal X$ into its double dual. What is $A^{**}(x)$? For $y^*$ in $\mathcal Y^*$,

$$
\begin{aligned}
\langle A^{**}(x),y^*\rangle
&=\langle x,A^*y^*\rangle\\
&=\langle Ax,y^*\rangle.
\end{aligned}
$$

That is, $A^{**}|_{\mathcal X}=A$. This is the first part of the next proposition.

**1.4. Proposition.** *If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $A\in\mathcal B(\mathcal X,\mathcal Y)$, then:*

(a) $A^{**}|_{\mathcal X}=A$;

(b) $\|A^*\|=\|A\|$;

(c) *if $A$ is invertible, then $A^*$ is invertible and $(A^*)^{-1}=(A^{-1})^*$;*

(d) *if $\mathcal Z$ is a Banach space and $B\in\mathcal B(\mathcal Y,\mathcal Z)$, then $(BA)^*=A^*B^*$.*

**Proof.** Part (a) was proved above. It was shown that $\|A^*\|\leqslant\|A\|$. Thus $\|A^{**}\|\leqslant\|A^*\|$. So if $x\in\operatorname{ball}\mathcal X$, then (a) implies that $\|Ax\|=\|A^{**}x\|\leqslant\|A^{**}\|\leqslant\|A^*\|$. Hence $\|A\|\leqslant\|A^*\|$.

The remainder of the proof is left to the reader. $\blacksquare$

**1.5. Example.** Let $(X,\Omega,\mu)$ and $M_\phi:L^p(\mu)\to L^p(\mu)$ be as in Example III.2.2. If $1\leqslant p<\infty$ and $1/p+1/q=1$, then $M_\phi^*:L^q(\mu)\to L^q(\mu)$ is given by $M_\phi^*f=\phi f$. That is, $M_\phi^*=M_\phi$.

**1.6. Example.** Let $K$ and $k$ be as in Example III.2.3. If $1\leqslant p<\infty$ and $1/p+1/q=1$, then $K^*:L^q(\mu)\to L^q(\mu)$ is the integral operator with kernel $k^*(x,y)\equiv k(y,x)$.

**1.7. Example.** Let $X$, $Y$, $\tau$, and $A$ be as in Example III.2.4. Then $A^*:M(Y)\to M(X)$ is given by

$$
(A^*\mu)(\Delta)=\mu(\tau^{-1}(\Delta))
$$

for every Borel subset $\Delta$ of $X$ and every $\mu$ in $M(Y)$.

Compare (1.5) and (1.6) with (II.2.8) and (II.2.9) to see the contrast between the adjoint of an operator on a Banach space with the adjoint of a Hilbert space operator.

**1.8. Proposition.** *If $A\in\mathcal B(\mathcal X,\mathcal Y)$, then $\ker A^*=(\operatorname{ran}A)^\perp$ and $\ker A={}^{\perp}(\operatorname{ran}A^*)$.*

The proof of this useful result is similar to that of Proposition II.2.19 and is left to the reader.
