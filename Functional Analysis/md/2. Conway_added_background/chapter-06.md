# VI. Linear Operators on a Banach Space


<a id="pdf-page-181"></a>
# CHAPTER VI

# Linear Operators on a Banach Space

As has been said before in this book, the theory of bounded linear operators on a Banach space has seen relatively little activity owing to the difficult geometric problems inherent in the concept of a Banach space. In this chapter several of the general concepts of this theory are presented. When combined with the few results from the next chapter, they constitute essentially the whole of the general theory of these operators.

We begin with a study of the adjoint of a Banach space operator. Unlike the adjoint of an operator on a Hilbert space (Section II.2), the adjoint of a bounded linear operator on a Banach space does not operate on the space but on the dual space.

## §1. The Adjoint of a Linear Operator

<!-- BEGIN BACKGROUND BG-VI.block1 -->
<a id="bg-vi-1"></a>
### Lemma BG-VI.1 — Bounded below means closed range

For a bounded linear map $T:X\to Y$ between Banach spaces, the following are equivalent: $T$ is injective with closed range; and some $c>0$ satisfies $\|Tx\|\geq c\|x\|$ for all $x$.

**Proof.** Under the inequality, $Tx_n\to y$ implies $\|x_n-x_m\|\leq c^{-1}\|Tx_n-Tx_m\|$, so completeness gives $x_n\to x$ and $Tx=y$. Injectivity is immediate. Conversely, the inverse mapping theorem applied to $T:X\to\operatorname{ran}T$, whose target is Banach because it is closed, gives $\|x\|\leq C\|Tx\|$. $\square$

This estimate is the missing step after the norm inequality in 1.9. With the constant $c$ used there for the radius of the dual ball, the displayed supremum actually equals $c\|x\|$; either positive constant gives the needed conclusion after renaming it.

<a id="bg-vi-2"></a>
### Lemma BG-VI.2 — Adjoint identities and their topology

Let $T:X\to Y$ be bounded. Then
$$
\ker T^*=(\operatorname{ran}T)^\perp,\qquad
\ker T={}^\perp(\operatorname{ran}T^*),\qquad
\overline{\operatorname{ran}T}={}^\perp(\ker T^*).
$$
Furthermore $T^*$ is weak-star continuous and $T$ is weak-to-weak continuous.

**Proof.** The equation $(T^*g)(x)=g(Tx)$ says $T^*g=0$ exactly when $g$ vanishes on the range. A vector annihilating the range of $T^*$ satisfies $g(Tx)=0$ for all $g\in Y^*$, hence $Tx=0$ by Hahn–Banach. Taking a preannihilator in the first identity and using BG-V.3 gives the third. Finally, each scalar test of $T^*g_i$ is the test $g_i(Tx)$, and each scalar test of $Tx_i$ is $(T^*g)(x_i)$, proving the continuity assertions. $\square$

Thus “the adjoint is injective” means “the original range is dense,” not necessarily “the original range is all of $Y$.” Closedness must be established separately.

<a id="bg-vi-3"></a>
### Lemma BG-VI.3 — Quotient estimates keep constants under control

The map $\widetilde T:X/\ker T\to\overline{\operatorname{ran}T}$ given by $\widetilde T(x+\ker T)=Tx$ is well defined, injective, and bounded, with $\|\widetilde T\|\leq\|T\|$.

**Proof.** Equal cosets differ by a kernel vector, so have equal images. If $Tx=0$, the coset is zero. For each $k\in\ker T$, $\|Tx\|=\|T(x+k)\|\leq\|T\|\,\|x+k\|$; take the infimum over $k$. $\square$

This is the boundedness needed for the reduction in the Closed Range Theorem. The quotient is Banach because the kernel of a continuous map is closed.
<!-- END BACKGROUND BG-VI.block1 -->

Suppose $\mathcal{X}$ and $\mathcal{Y}$ are vector spaces and $T:\mathcal{X}\to\mathcal{Y}$ is a linear transformation. Let $\mathcal{Y}'=$ all of the linear functionals of $\mathcal{Y}\to\mathbb{F}$. If $y'\in\mathcal{Y}'$, then $y'\circ T:\mathcal{X}\to\mathbb{F}$ is easily seen to be a linear functional on $\mathcal{X}$. That is, $y'\circ T\in\mathcal{X}'$. This defines a map

$$
T':\mathcal{Y}'\to\mathcal{X}'
$$

by $T'(y')=y'\circ T$. The first result shows that if $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces, then the map $T'$ can be used to determine when $T$ is bounded. Another equivalent formulation of boundedness is given by means of the weak topology.

**1.1. Theorem.** *If $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces and $T:\mathcal{X}\to\mathcal{Y}$ is a linear transformation, then the following statements are equivalent.*



<a id="pdf-page-182"></a>
(a) $T$ is bounded.

(b) $T'(\mathcal Y^*)\subseteq\mathcal X^*$.

(c) $T:(\mathcal X,\text{weak})\to(\mathcal Y,\text{weak})$ is continuous.

**Proof.** (a)$\Rightarrow$(b): If $y^*\in\mathcal Y^*$, then $T'(y^*)\in\mathcal X'$; it must be shown that $T'(y^*)\in\mathcal X^*$. But
$$
|T'(y^*)(x)|=|y^*\circ T(x)|=|\langle T(x),y^*\rangle|
\leq\|T(x)\|\|y^*\|\leq\|T\|\|y^*\|\|x\|.
$$
So $T'(y^*)\in\mathcal X^*$.

(b)$\Rightarrow$(c): If $\{x_i\}$ is a net in $\mathcal X$ and $x_i\to0$ weakly, then for $y^*$ in $\mathcal Y^*$,
$$
\langle T(x_i),y^*\rangle=T'(y^*)(x_i)\to0
$$
since $T'(y^*)\in\mathcal X^*$. Hence $T(x_i)\to0$ weakly in $\mathcal Y$.

(c)$\Rightarrow$(b): If $y^*\in\mathcal Y^*$, then $y^*\circ T:\mathcal X\to\mathbb F$ is weakly continuous by (c). Hence $T'(y^*)=y^*\circ T\in\mathcal X^*$ by (V.1.2).

(b)$\Rightarrow$(a): Let $y^*\in\mathcal Y^*$ and put $x^*=T'(y^*)$. So $x^*\in\mathcal X^*$ by (b). So if $x\in\operatorname{ball}\mathcal X$,
$$
|\langle T(x),y^*\rangle|=|\langle x,x^*\rangle|\leq\|x^*\|.
$$
That is, $\sup\{|\langle T(x),y^*\rangle|:x\in\operatorname{ball}\mathcal X\}<\infty$. Hence $T(\operatorname{ball}\mathcal X)$ is weakly bounded; by the PUB, $T(\operatorname{ball}\mathcal X)$ is norm bounded and so $\|T\|<\infty$. $\blacksquare$

The preceding result is useful, though strictly speaking it is not necessary for the purpose of defining the adjoint of an operator $A$ in $\mathcal B(\mathcal X,\mathcal Y)$, which we now turn to. If $A\in\mathcal B(\mathcal X,\mathcal Y)$ and $y^*\in\mathcal Y^*$, then $y^*\circ A=A'(y^*)\in\mathcal X^*$. This defines a map $A^*:\mathcal Y^*\to\mathcal X^*$, where $A^*=A'|_{\mathcal Y^*}$. Hence

**1.2**
$$
\langle x,A^*(y^*)\rangle=\langle A(x),y^*\rangle
$$

for $x$ in $\mathcal X$ and $y^*$ in $\mathcal Y^*$. $A^*$ is called the *adjoint* of $A$.

Before exploring the concept let’s see how this compares with the definition of the adjoint of an operator on Hilbert space given in §II.2. There is a difference, but only a small one. When $\mathcal H$ is identified with $\mathcal H^*$, the dual space of $\mathcal H$, the identification is not linear but conjugate linear (if $\mathbb F=\mathbb C$). The isometry $h\mapsto L_h$ of $\mathcal H$ onto $\mathcal H^*$, where $L_h(f)=\langle f,h\rangle$, satisfies $L_{\alpha h}=\bar\alpha L_h$. Thus the definition of $A^*$ given in (1.2) above is not the same as the adjoint of an operator on Hilbert space, since in (1.2) $A^*$ is defined on $\mathcal Y^*$ and not some conjugate-linear isomorphic image of it. In particular, if the definition (1.2) is applied to a matrix $A$ acting on $\mathbb C^d$ considered as a Banach space, its adjoint corresponds to the transpose of $A$. If $\mathbb C^d$ is considered as a Hilbert space, then the matrix of $A^*$ is the conjugate transpose of the matrix of $A$. This difference will not confuse us but it will serve to explain minor differences that will appear in the treatment of the two types of adjoints. The first of these occurs in the next result.

**1.3. Proposition.** *If $\mathcal X$ and $\mathcal Y$ are Banach spaces, $A,B\in\mathcal B(\mathcal X,\mathcal Y)$, and $\alpha,\beta\in\mathbb F$, then $(\alpha A+\beta B)^*=\alpha A^*+\beta B^*$. Moreover, $A^*:(\mathcal Y^*,\mathrm{wk}^*)\to(\mathcal X^*,\mathrm{wk}^*)$ is continuous.*

Note the absence of conjugates. The proof is left to the reader.

If $A\in\mathcal B(\mathcal X,\mathcal Y)$, then it is easy to see that $A^*\in\mathcal B(\mathcal Y^*,\mathcal X^*)$. In fact, if $y^*\in\operatorname{ball}\mathcal Y^*$ and $x\in\operatorname{ball}\mathcal X$, then
$$
|\langle x,A^*y^*\rangle|=|\langle Ax,y^*\rangle|\leq\|Ax\|\leq\|A\|.
$$
Hence $\|A^*y^*\|\leq\|A\|$ if $y^*\in\operatorname{ball}\mathcal Y^*$, so that $\|A^*\|\leq\|A\|$. This implies that



<a id="pdf-page-183"></a>
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


<a id="pdf-page-184"></a>
This enables us to prove the converse of Proposition 1.4c.

**1.9. Proposition.** *If $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$, then $A$ is invertible if and only if $A^*$ is invertible.*

**Proof.** In light of (1.4c) it suffices to assume that $A^*$ is invertible and show that $A$ is invertible. Since $A^*$ is an open mapping, there is a constant $c>0$ such that $A^*(\operatorname{ball}\mathcal{Y}^*)\supseteq\{x^*\in\mathcal{X}^*:\|x^*\|\leq c\}$. So if $x\in\mathcal{X}$, then

$$
\begin{aligned}
\|Ax\|
&=\sup\{|\langle Ax,y^*\rangle|:y^*\in\operatorname{ball}\mathcal{Y}^*\}\\
&=\sup\{|\langle x,A^*y^*\rangle|:y^*\in\operatorname{ball}\mathcal{Y}^*\}\\
&\geq\sup\{|\langle x,x^*\rangle|:x^*\in\mathcal{X}^*\text{ and }\|x^*\|\leq c\}\\
&=c^{-1}\|x\|.
\end{aligned}
$$

Thus $\ker A=(0)$ and $\operatorname{ran}A$ is closed. (Why?) On the other hand, $(\operatorname{ran}A)^\perp=\ker A^*=(0)$ since $A^*$ is invertible. Thus $\operatorname{ran}A$ is also dense. This implies that $A$ is surjective and thus invertible. $\blacksquare$

This section concludes with the following useful result that seems to be somewhat unfamiliar to parts of the mathematical community.

**1.10. Theorem.** *If $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces and $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$, then the following statements are equivalent.*

(a) $\operatorname{ran}A$ *is closed.*  
(b) $\operatorname{ran}A^*$ *is weak$^*$ closed.*  
(c) $\operatorname{ran}A^*$ *is norm closed.*

**Proof.** It is clear that (b) implies (c), so it will be shown that (a) implies (b) and (c) implies (a). Before this is done, it will be shown that it suffices to prove the theorem under the additional hypothesis that $A$ is injective and has dense range.

Let $\mathcal{L}=\operatorname{cl}(\operatorname{ran}A)$. Thus $A:\mathcal{X}\to\mathcal{L}$ induces a bounded linear map $B:\mathcal{X}/\ker A\to\mathcal{L}$ defined by $B(x+\ker A)=Ax$. If $Q:\mathcal{X}\to\mathcal{X}/\ker A$ is the natural map, the diagram

$$
\begin{array}{ccccc}
\mathcal{X}&\xrightarrow{\ A\ }&\mathcal{L}&\hookrightarrow&\mathcal{Y}\\
{\scriptstyle Q}\searrow&&\nearrow{\scriptstyle B}&&\\
&\mathcal{X}/\ker A&&&
\end{array}
$$

commutes. (Why is $B$ bounded?) It is easy to see that $B$ is injective and that $B$ has dense range. In fact, $\operatorname{ran}B=\operatorname{ran}A$, so $\operatorname{ran}A$ is closed if and only if $\operatorname{ran}B$ is closed. Let’s examine $B^*:\mathcal{L}^*\to(\mathcal{X}/\ker A)^*$. By (V.2.2), $(\mathcal{X}/\ker A)^*=(\ker A)^\perp=\operatorname{wk}^*\operatorname{cl}(\operatorname{ran}A^*)\subseteq\mathcal{X}^*$ by (1.8). Also by (V.2.3), since $\mathcal{L}\leq\mathcal{Y}$, $\mathcal{L}^*=\mathcal{Y}^*/\mathcal{L}^\perp=\mathcal{Y}^*/(\operatorname{ran}A)^\perp=\mathcal{Y}^*/\ker A^*$ by (1.8). Thus,

$$
B^*:\mathcal{Y}^*/\ker A^*\to(\ker A)^\perp.
$$

![](assets/p0184-page_183_image_14.jpg)


<a id="pdf-page-185"></a>
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



   <a id="pdf-page-186"></a>
   $n$, $\alpha_{mn}\to 0$ as $m\to\infty$. Conversely, if $\{\alpha_{mn}:m,n\geqslant 1\}$ are scalars satisfying (a) and (b), then

   $$
   (Ax)(m)=\sum_{n=1}^{\infty}\alpha_{mn}x(n)
   $$

   defines a bounded operator $A$ on $c_0$ and $\|A\|=M$. Find $A^*$.

8. Let $A\in\mathcal B(l^1)$ and for $n\geqslant 1$ define $e_n$ in $l^1$ by $e_n(n)=1$, $e_n(m)=0$ for $m\neq n$. Put $\alpha_{mn}=(Ae_n)(m)$ for $m,n\geqslant 1$. Prove: (a) $M\equiv\sup_n\sum_{m=1}^{\infty}|\alpha_{mn}|<\infty$; (b) for every $m$, $\sup_n|\alpha_{mn}|<\infty$. Conversely, if $\{\alpha_{mn}:m,n\geqslant 1\}$ are scalars satisfying (a) and (b), then

   $$
   (Af)(m)=\sum_{n=1}^{\infty}\alpha_{mn}f(n)
   $$

   defines a bounded operator $A$ on $l^1$ and $\|A\|=M$. Find $A^*$.

9. (Bonsall [1986]) Let $\mathcal X$ be a Banach space, $Z$ a nonempty set, and $u:Z\to\mathcal X$. If there are positive constants $M_1$ and $M_2$ such that (i) $\|u(z)\|\leqslant M_1$ for all $z$ in $Z$ and (ii) for every $x^*$ in $\mathcal X$, $\sup\{|\langle u(z),x^*\rangle|:z\in Z\}\geqslant M_2\|x^*\|$; then for every $x$ in $\mathcal X$ there is an $f$ in $l^1(Z)$ such that $(*)x=\sum\{f(z)u(z):z\in Z\}$ and $M_2\inf\|f\|_1\leqslant\|x\|\leqslant M_1\inf\|f\|_1$, where the infimum is taken over all $f$ in $l^1(Z)$ such that $(*)$ holds. (Hint: define $T:l^1(Z)\to\mathcal X$ by $Tf=\sum\{f(z)u(z):z\in Z\}$.)

10. (Bonsall [1986]) Let $m$ be normalized Lebesgue measure on $\partial\mathbb D$ and for $|z|<1$ and $|w|=1$ let $p_z(w)=(1-|z|^2)/|1-\bar zw|^2$. So $p_z$ is the Poisson kernel. Show that if $f\in L^1(m)$, then there is a sequence $\{z_n\}\subseteq\mathbb D$ and a sequence $\{\lambda_n\}$ in $l^1$ such that $(*)f=\sum_{n=1}^{\infty}\lambda_np_{z_n}$. Moreover, $\|f\|_1=\inf\sum_{n=1}^{\infty}|\lambda_n|$, where the infimum is taken over all $\{\lambda_n\}$ in $l^1$ such that $(*)$ holds. (Hint: use Exercise 9.)

11. If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $B\in\mathcal B(\mathcal Y^*,\mathcal X^*)$, then there is an operator $A$ in $\mathcal B(\mathcal X,\mathcal Y)$ such that $B=A^*$ if and only if $B$ is wk*-continuous.

12. If $\mathcal X$ is a Banach space and $\mathcal M$ and $\mathcal N$ are closed subspaces, show that the following statements are equivalent. (a) $\mathcal M+\mathcal N$ is closed. (b) the range of the linear transformation $x\to(x+\mathcal M)\oplus(x+\mathcal N)$ from $\mathcal X$ into $\mathcal X/\mathcal M\oplus\mathcal X/\mathcal N$ is closed. (c) $\mathcal M^\perp+\mathcal N^\perp$ is norm closed in $\mathcal X^*$. (d) $\mathcal M^\perp+\mathcal N^\perp$ is weak* closed in $\mathcal X^*$.

## §2*. The Banach–Stone Theorem

<!-- BEGIN BACKGROUND BG-VI.block2 -->
<a id="bg-vi-4"></a>
### Lemma BG-VI.4 — Isometries transfer the geometry of dual balls

If $T:X\to Y$ is a surjective linear isometry, then $T^*:Y^*\to X^*$ is a surjective linear isometry and a weak-star homeomorphism. It maps extreme points of one dual unit ball bijectively onto those of the other.

**Proof.** Since $T$ maps the unit ball onto the unit ball, $\|T^*g\|=\sup_{\|x\|\leq1}|g(Tx)|=\|g\|$. Its inverse is $(T^{-1})^*$, and both maps are weak-star continuous by BG-VI.2. If $T^*g=(u+v)/2$ with $u,v$ in the target ball, apply the inverse isometry. Extremality of $g$ forces both inverse images to equal $g$, hence $u=v=T^*g$. Apply the same argument to the inverse for bijectivity on extreme points. $\square$
<!-- END BACKGROUND BG-VI.block2 -->

As an application of the adjoint of a linear map, the isometries between spaces of the form $C(X)$ and $C(Y)$ will be characterized. Note that if $X$ and $Y$ are compact spaces, $\tau:Y\to X$ is continuous map, and $Af=f\circ\tau$ for $f$ in $C(X)$, then (III.2.4) $A$ is a bounded linear map and $\|A\|=1$. Moreover, $A$ is an isometry if and only if $\tau$ is surjective. If $A$ is a surjective isometry, then $\tau$ must be a homeomorphism. Indeed, suppose $A$ is a surjective isometry; it must be shown that $\tau$ is injective. If $y_0,y_1\in Y$ and $y_0\neq y_1$, then there is a $g$


<a id="pdf-page-187"></a>
in $C(Y)$ such that $g(y_0)=0$ and $g(y_1)=1$. Let $f\in C(X)$ such that $Af=g$. Thus $f(\tau(y_0))=g(y_0)=0$ and $f(\tau(y_1))=1$. Hence $\tau(y_0)\ne\tau(y_1)$.

So if $\tau:Y\to X$ is a homeomorphism and $\alpha:Y\to\mathbb F$ is a continuous function, with $|\alpha(y)|\equiv1$, then $T:C(X)\to C(Y)$ defined by $(Tf)(y)=\alpha(y)f(\tau(y))$ is a surjective isometry. The next result gives a converse to this.

**2.1. The Banach–Stone Theorem.** *If $X$ and $Y$ are compact and $T:C(X)\to C(Y)$ is a surjective isometry, then there is a homeomorphism $\tau:Y\to X$ and a function $\alpha$ in $C(Y)$ such that $|\alpha(y)|=1$ for all $y$ and*

$$
(Tf)(y)=\alpha(y)f(\tau(y))
$$

*for all $f$ in $C(X)$ and $y$ in $Y$.*

**Proof.** Consider $T^*:M(Y)\to M(X)$. Because $T$ is a surjective isometry, $T^*$ is also. (Verify.) Thus $T^*$ is a weak* homeomorphism of ball $M(Y)$ onto ball $M(X)$ that distributes over convex combinations. Hence (Why?)

$$
T^*(\operatorname{ext}[\operatorname{ball}M(Y)])=\operatorname{ext}[\operatorname{ball}M(X)].
$$

By Theorem V.8.4 this implies that for every $y$ in $Y$ there is a unique $\tau(y)$ in $X$ and a unique scalar $\alpha(y)$ such that $|\alpha(y)|=1$ and

$$
T^*(\delta_y)=\alpha(y)\delta_{\tau(y)}.
$$

By the uniqueness, $\alpha:Y\to\mathbb F$ and $\tau:Y\to X$ are well-defined functions.

**2.2. Claim.** $\alpha:Y\to\mathbb F$ is continuous.

If $\{y_i\}$ is a net in $Y$ and $y_i\to y$, then $\delta_{y_i}\to\delta_y$ weak* in $M(Y)$. Hence $\alpha(y_i)\delta_{\tau(y_i)}=T^*(\delta_y)\to T^*(\delta_y)=\alpha(y)\delta_{\tau(y)}$ weak* in $M(X)$. In particular, $\alpha(y_i)=\langle 1,T^*(\delta_{y_i})\rangle\to\langle 1,T^*(\delta_y)\rangle=\alpha(y)$, proving (2.2).

**2.3. Claim.** $\tau:Y\to X$ is a homeomorphism.

As in the proof of (2.2), if $y_i\to y$ in $Y$, then $\alpha(y_i)\delta_{\tau(y_i)}\to\alpha(y)\delta_{\tau(y)}$ weak* in $M(X)$. Also, $\alpha(y_i)\to\alpha(y)$ in $\mathbb F$ by (2.2). Thus $\delta_{\tau(y_i)}=\alpha(y_i)^{-1}[\alpha(y_i)\delta_{\tau(y_i)}]\to\delta_{\tau(y)}$. By (V.6.1) this implies that $\tau(y_i)\to\tau(y)$, so that $\tau:Y\to X$ is continuous.

If $y_1,y_2\in Y$ and $y_1\ne y_2$, then $\overline{\alpha(y_1)}\delta_{y_1}\ne\overline{\alpha(y_2)}\delta_{y_2}$. Since $T^*$ is injective, it is easy to see that $\tau(y_1)\ne\tau(y_2)$ and so $\tau$ is one-to-one. If $x\in X$, then the fact that $T^*$ is surjective implies that there is a $\mu$ in $M(Y)$ such that $T^*\mu=\delta_x$. It must be that $\mu\in\operatorname{ext}[\operatorname{ball}M(Y)]$ (Why?), so that $\mu=\beta\delta_y$ for some $y$ in $Y$ and $\beta$ in $\mathbb F$ with $|\beta|=1$. Thus $\delta_x=T^*(\beta\delta_y)=\beta\alpha(y)\delta_{\tau(y)}$. Hence $\beta=\overline{\alpha(y)}$ and $\tau(y)=x$. Therefore $\tau:Y\to X$ is a continuous bijection and hence must be a homeomorphism (A.2.8). This establishes (2.3).

If $f\in C(X)$ and $y\in Y$, then $T(f)(y)=\langle Tf,\delta_y\rangle=\langle f,T^*\delta_y\rangle=\langle f,\alpha(y)\delta_{\tau(y)}\rangle=\alpha(y)f(\tau(y))$. $\blacksquare$


<a id="pdf-page-188"></a>
# §3. Compact Operators

<!-- BEGIN BACKGROUND BG-VI.block3 -->
<a id="bg-vi-5"></a>
### Definition BG-VI.5 — Total boundedness and relative compactness

A metric set is totally bounded if, for every $\varepsilon>0$, finitely many balls of radius $\varepsilon$ cover it. It is relatively compact if its closure is compact. In a complete metric space these are equivalent.

**Proof of the equivalence.** A compact closure admits a finite subcover by $\varepsilon$-balls. Conversely, successively covering by balls of radii $2^{-n}$ and retaining a ball containing infinitely many remaining terms produces a Cauchy subsequence from any sequence. Completeness gives its limit in the closure. This makes the closure sequentially compact. To see compactness directly, a sequentially compact metric space has a Lebesgue number for any open cover: otherwise points whose $1/n$-balls fit in no member have a convergent subsequence, contradicting openness of a cover member containing its limit. A finite net with radius smaller than this number produces a finite subcover. $\square$

<a id="bg-vi-6"></a>
### Lemma BG-VI.6 — Uniform estimates on compact sets

Let $S_i:X\to Y$ be bounded linear maps with $\sup_i\|S_i\|\leq M$, and suppose $S_ix\to0$ for every $x$. Then $S_i\to0$ uniformly on every norm-compact $K\subseteq X$.

**Proof.** Cover $K$ by finitely many balls of radius $\delta$ with centers $x_1,\ldots,x_m$. For $x\in K$, choose $j$ with $\|x-x_j\|<\delta$ and estimate
$$
\|S_ix\|\leq M\delta+\max_{j\leq m}\|S_ix_j\|.
$$
Choose $\delta$ first and then a common large index for the finitely many centers. $\square$

The same finite-net argument is the core of Schauder's theorem: bounded functionals converging weak-star converge uniformly on the compact closure of $T(B_X)$. It is also the reason uniformly bounded finite-rank approximations to the identity give operator-norm approximations after composition with a compact operator.

<a id="bg-vi-7"></a>
### Lemma BG-VI.7 — Compact operators form a closed operator ideal

Sums and scalar multiples of compact operators are compact, bounded compositions with a compact operator are compact, and an operator-norm limit of compact operators is compact.

**Proof.** For sums, the sum of the two compact closures of the images of the unit ball is compact, being a continuous image of their product. A bounded map sends compact sets to compact sets; a bounded map preceding a compact operator sends the unit ball into a fixed multiple of the unit ball. Finally, if $T_n\to T$ in operator norm, choose $n$ so that $\|T-T_n\|<\varepsilon/2$. A finite $\varepsilon/2$-net for $T_n(B_X)$ is an $\varepsilon$-net for $T(B_X)$. BG-VI.5 gives compactness. $\square$

<a id="bg-vi-8"></a>
### Lemma BG-VI.8 — Pointwise bounded equicontinuous families on compact spaces

Let $K$ be compact Hausdorff. If $\mathcal F\subseteq C(K)$ is equicontinuous and $\sup_{f\in\mathcal F}|f(x)|<\infty$ for each $x$, then $\sup_{f\in\mathcal F}\|f\|_\infty<\infty$. If an equicontinuous net $f_i$ converges pointwise to $f$, the convergence is uniform.

**Proof.** Choose at each $x$ a neighborhood $U_x$ on which all members vary by less than $1$. Finitely many $U_{x_j}$ cover $K$, so $|f(y)|\leq1+\max_j\sup_{g\in\mathcal F}|g(x_j)|$ uniformly. For the second assertion, equicontinuity with tolerance $\varepsilon/3$ transfers to the pointwise limit with a non-strict inequality. Use finitely many corresponding neighborhoods and pointwise convergence at their centers; the three-term triangle inequality bounds $|f_i(y)-f(y)|$ uniformly by $\varepsilon$. $\square$

Equicontinuity is not the same as a bound on $\|f\|_\infty$: $f_n(t)=t^n$ on $[0,1]$ has norm $1$ but is not equicontinuous at $1$. This is exactly the obstruction to compactness in Arzelà–Ascoli.
<!-- END BACKGROUND BG-VI.block3 -->

The following definition generalizes the concept of a compact operator from a Hilbert space to a Banach space.

**3.1. Definition.** If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $A:\mathcal X\to\mathcal Y$ is a linear transformation, then $A$ is *compact* if $\operatorname{cl} A(\operatorname{ball}\mathcal X)$ is compact in $\mathcal Y$.

The reader should become reacquainted with Section II.4.

It is easy to see that compact operators are bounded.

For operators on a Hilbert space the following concept is equivalent to compactness, as will be seen.

**3.2. Definition.** If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $A\in\mathcal B(\mathcal X,\mathcal Y)$, then $A$ is *completely continuous* if for any sequence $\{x_n\}$ in $\mathcal X$ such that $x_n\to x$ weakly it follows that $\|Ax_n-Ax\|\to 0$.

**3.3. Proposition.** *Let $\mathcal X$ and $\mathcal Y$ be Banach spaces and let $A\in\mathcal B(\mathcal X,\mathcal Y)$.*

(a) *If $A$ is a compact operator, then $A$ is completely continuous.*

(b) *If $\mathcal X$ is reflexive and $A$ is completely continuous, then $A$ is compact.*

**Proof.** (a) Let $\{x_n\}$ be a sequence in $\mathcal X$ such that $x_n\to 0$ weakly. By the PUB, $M=\sup_n\|x_n\|<\infty$. Without loss of generality, it may be assumed that $M\leq 1$. Hence $\{Ax_n\}\subseteq\operatorname{cl}A(\operatorname{ball}\mathcal X)$. Since $A$ is compact, there is a subsequence $\{x_{n_k}\}$ and a $y$ in $\mathcal Y$ such that $\|Ax_{n_k}-y\|\to 0$. But $x_{n_k}\to 0$ (wk) and $A:(\mathcal X,\mathrm{wk})\to(\mathcal Y,\mathrm{wk})$ is continuous (1.1c). Hence $Ax_{n_k}\to A(0)=0$ (wk). Thus $y=0$. Since $0$ is the unique cluster point of $\{Ax_n\}$ and this sequence is contained in a compact set, $\|Ax_n\|\to 0$.

(b) First assume that $\mathcal X$ is separable; so $(\operatorname{ball}\mathcal X,\mathrm{wk})$ is a compact metric space. So if $\{x_n\}$ is a sequence in $\operatorname{ball}\mathcal X$ there is an $x$ in $\mathcal X$ and a subsequence $\{x_{n_k}\}$ such that $x_{n_k}\to x$ weakly. Since $A$ is completely continuous, $\|Ax_{n_k}-Ax\|\to 0$. Thus $A(\operatorname{ball}\mathcal X)$ is sequentially compact; that is, $A$ is a compact operator.

Now let $\mathcal X$ be arbitrary and let $\{x_n\}\subseteq\operatorname{ball}\mathcal X$. If $\mathcal X_1=$ the closed linear span of $\{x_n\}$, then $\mathcal X_1$ is separable and reflexive. If $A_1=A|_{\mathcal X_1}$, then $A_1:\mathcal X_1\to\mathcal Y$ is easily seen to be completely continuous. By the first paragraph, $A_1$ is compact. Thus $\{Ax_n\}=\{A_1x_n\}$ has a convergent subsequence. Since $\{x_n\}$ was arbitrary, $A$ is a compact operator. $\blacksquare$

In the proof of (3.3b), the fact that $A(\operatorname{ball}\mathcal X)$ is compact, and hence closed, is a consequence of the reflexivity of $\mathcal X$.

By Proposition V.5.2, every operator in $\mathcal B(l^1)$ is completely continuous. However, there are noncompact operators in $\mathcal B(l^1)$ (for example, the identity operator).

There has been relatively little study of completely continuous operators



<a id="pdf-page-189"></a>
that I am aware of. Most of the effort has been devoted to the study of compact operators and this is the direction we now pursue.

**3.4. Schauder’s Theorem.** If $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$, then $A$ is compact if and only if $A^*$ is compact.

**Proof.** Assume $A$ is a compact operator and let $\{y_n^*\}$ be a sequence in ball $\mathcal{Y}^*$. It must be shown that $\{A^*y_n^*\}$ has a norm convergent subsequence or, equivalently, a cluster point in the norm topology. By Alaoglu’s Theorem, there is a $y^*$ in ball $\mathcal{Y}^*$ such that $y_n^*\xrightarrow[\mathrm{cl}]{}y^*$ (weak*). It will be shown that $A^*y_n^*\xrightarrow[\mathrm{cl}]{}A^*y^*$ in norm.

Let $\varepsilon>0$ and fix $N\geqslant1$. Because $A(\operatorname{ball}\mathcal{X})$ has compact closure, there are vectors $y_1,\ldots,y_m$ in $\mathcal{Y}$ such that
$A(\operatorname{ball}\mathcal{X})\subseteq\bigcup_{k=1}^{m}\{y\in\mathcal{Y}:\|y-y_k\|<\varepsilon/3\}$.
Since $y_n^*\xrightarrow[\mathrm{cl}]{}y^*$ (weak*), there is an $n\geqslant N$ such that $|\langle y_k,y^*-y_n^*\rangle|<\varepsilon/3$ for $1\leqslant k\leqslant m$. Let $x$ be an arbitrary element in ball $\mathcal{X}$ and choose $y_k$ such that $\|Ax-y_k\|<\varepsilon/3$. Then

$$
\begin{aligned}
|\langle x,A^*y^*-A^*y_n^*\rangle|
&=|\langle Ax,y^*-y_n^*\rangle|\\
&\leqslant|\langle Ax-y_k,y^*-y_n^*\rangle|
  +|\langle y_k,y^*-y_n^*\rangle|\\
&\leqslant2\|Ax-y_k\|+\varepsilon/3<\varepsilon.
\end{aligned}
$$

Thus $\|A^*y-A^*y_n^*\|\leqslant\varepsilon$.

For the converse, assume $A^*$ is compact. By the first half of the proof, $A^{**}:\mathcal{X}^{**}\to\mathcal{Y}^{**}$ is compact. It is easy to check that $A=A^{**}|_{\mathcal{X}}$ is compact. $\blacksquare$

For Banach spaces $\mathcal{X}$ and $\mathcal{Y}$, $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ denotes the set of all compact operators from $\mathcal{X}$ into $\mathcal{Y}$; $\mathcal{B}_0(\mathcal{X})=\mathcal{B}_0(\mathcal{X},\mathcal{X})$.

**3.5. Proposition.** Let $\mathcal{X}$, $\mathcal{Y}$, and $\mathcal{Z}$ be Banach spaces.

(a) $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ is a closed linear subspace of $\mathcal{B}(\mathcal{X},\mathcal{Y})$.

(b) If $K\in\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ and $A\in\mathcal{B}(\mathcal{Y},\mathcal{Z})$, then $AK\in\mathcal{B}_0(\mathcal{X},\mathcal{Z})$.

(c) If $K\in\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ and $A\in\mathcal{B}(\mathcal{Z},\mathcal{X})$, then $KA\in\mathcal{B}_0(\mathcal{Z},\mathcal{Y})$.

The proof of (3.5) is left as an exercise.

**3.6. Corollary.** If $\mathcal{X}$ is a Banach space, $\mathcal{B}_0(\mathcal{X})$ is a closed two-sided ideal in the algebra $\mathcal{B}(\mathcal{X})$.

Let $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})=$ the bounded operators $T:\mathcal{X}\to\mathcal{Y}$ for which ran $T$ is finite dimensional. Operators in $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})$ are called operators with *finite rank*. It is easy to see that $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})\subseteq\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ and by (3.5a) the closure of $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})$ is contained in $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$. Is $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})$ dense in $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$?



<a id="pdf-page-190"></a>
It was shown in (II.4.4) that if $\mathcal H$ is a Hilbert space, then $\mathcal B_0(\mathcal H)$ is indeed the closure of $\mathcal B_{00}(\mathcal H)$. Note that the availability of an orthonormal basis in a Hilbert space played a significant role in the proof of this theorem. There is a concept of a basis for a Banach space called a Schauder basis. Any Banach space $\mathcal X$ with a Schauder basis has the property that $\mathcal B_{00}(\mathcal X)$ is dense in $\mathcal B_0(\mathcal X)$. Enflo [1973] gave an example of a separable reflexive Banach space $\mathcal X$ for which $\mathcal B_{00}(\mathcal X)$ is not dense in $\mathcal B_0(\mathcal X)$, and, hence, $\mathcal H$ has no Schauder basis. Davie [1973] and [1975] have simplifications of Enflo’s proof. For the classical Banach spaces, however, every compact operator is the limit of a sequence of finite-rank operators.

The remainder of this section is devoted to proving that for $X$ compact, $\mathcal B_{00}(C(X))$ is dense in $\mathcal B_0(C(X))$. This begins with material that may be familiar to many readers but will be presented for those who are unacquainted with it.

**3.7. Definition.** If $X$ is completely regular and $\mathcal F\subseteq C(X)$, then $\mathcal F$ is *equicontinuous* if for every $\varepsilon>0$ and for every $x_0$ in $X$ there is a neighborhood $U$ of $x_0$ such that $|f(x)-f(x_0)|<\varepsilon$ for all $x$ in $U$ and for all $f$ in $\mathcal F$.

Note that for a single function $f$ in $C(X)$, $\mathcal F=\{f\}$ is equicontinuous. The concept of equicontinuity states that one neighborhood works for all $f$ in $\mathcal F$.

**3.8. The Arzela–Ascoli Theorem.** *If $X$ is compact and $\mathcal F\subseteq C(X)$, then $\mathcal F$ is totally bounded if and only if $\mathcal F$ is bounded and equicontinuous.*

PROOF. Suppose $\mathcal F$ is totally bounded. It is easy to see that $\mathcal F$ is bounded. If $\varepsilon>0$, then there are $f_1,\ldots,f_n$ in $\mathcal F$ such that $\mathcal F\subseteq\bigcup_{k=1}^{n}\{f\in C(X):\|f-f_k\|<\varepsilon/3\}$. If $x_0\in X$, let $U$ be an open neighborhood of $x_0$ such that for $1\leq k\leq n$ and $x$ in $U$, $|f_k(x)-f_k(x_0)|<\varepsilon/3$. If $f\in\mathcal F$, let $f_k$ be such that $\|f-f_k\|<\varepsilon/3$. Then for $x$ in $U$,

$$
\begin{aligned}
|f(x)-f(x_0)|
&\leq |f(x)-f_k(x)|+|f_k(x)-f_k(x_0)|\\
&\qquad+|f_k(x_0)-f(x_0)|\\
&<\varepsilon.
\end{aligned}
$$

Hence $\mathcal F$ is equicontinuous.

Now assume that $\mathcal F$ is equicontinuous and $\mathcal F\subseteq\operatorname{ball}C(X)$. Let $\varepsilon>0$. For each $x$ in $X$, let $U_x$ be an open neighborhood of $x$ such that $|f(x)-f(y)|<\varepsilon/3$ for $f$ in $\mathcal F$ and $y$ in $U_x$. Now $\{U_x:x\in X\}$ is an open covering of $X$. Since $X$ is compact, there are points $x_1,\ldots,x_n$ in $X$ such that $X=\bigcup_{j=1}^{n}U_{x_j}$.

Let $\{\alpha_1,\ldots,\alpha_m\}\subseteq\mathbb D$ such that $\operatorname{cl}\mathbb D\subseteq\bigcup_{k=1}^{m}\{\alpha:|\alpha-\alpha_k|<\varepsilon/6\}$. Consider the collection $B$ of those ordered $n$-tuples $b=(\beta_1,\ldots,\beta_n)$ for which there is a function $f_b$ in $\mathcal F$ such that $|f_b(x_j)-\beta_j|<\varepsilon/6$ for $1\leq j\leq n$. Note that $B$ is


<a id="pdf-page-191"></a>
not empty since $f(x)\subseteq\operatorname{cl}\mathbb D$ for every $f$ in $\mathcal F$. In fact, each $f$ in $\mathcal F$ gives rise to such a $b$ in $B$. Moreover $B$ is finite. Fix one function $f_b$ in $\mathcal F$ associated as above with $b$ in $B$.

**3.9. Claim.** $\displaystyle \mathcal F\subseteq\bigcup_{b\in B}\{f:\|f-f_b\|<\varepsilon\}$.

Note that (3.9) implies that $\mathcal F$ is totally bounded.

If $f\in\mathcal F$, there is a $b$ in $B$ such that $|f(x_j)-f_b(x_j)|<\varepsilon/3$ for $1\leq j\leq n$. Therefore if $x\in X$, let $x_j$ be chosen such that $x\in U_{x_j}$. Thus $|f(x)-f_b(x)|\leq |f(x)-f(x_j)|+|f(x_j)-f_b(x_j)|+|f_b(x_j)-f_b(x)|<\varepsilon$. Since $x$ was arbitrary, $\|f-f_b\|<\varepsilon$. ■

**3.10. Corollary.** *If $X$ is compact and $\mathcal F\subseteq C(X)$, then $\mathcal F$ is compact if and only if $\mathcal F$ is closed, bounded, and equicontinuous.*

**3.11. Theorem.** *If $X$ is compact, then $\mathcal B_{00}(C(X))$ is dense in $\mathcal B_0(C(X))$.*

**PROOF.** Let $T\in\mathcal B_0(C(X))$. Thus $T(\operatorname{ball}C(X))$ is bounded and equicontinuous by the Arzela–Ascoli Theorem. If $\varepsilon>0$ and $x\in X$, let $U_x$ be an open neighborhood of $x$ such that $|(Tf)(x)-(Tf)(y)|<\varepsilon$ for all $f$ in $\operatorname{ball}C(X)$ and $y$ in $U_x$. Let $\{x_1,\ldots,x_n\}\subseteq X$ such that $X\subseteq\bigcup_{j=1}^n U_{x_j}$. Let $\{\phi_1,\ldots,\phi_n\}$ be a partition of unity subordinate to $\{U_{x_1},\ldots,U_{x_n}\}$. Define $T_\varepsilon:C(X)\to C(X)$ by

$$
T_\varepsilon f=\sum_{j=1}^n(Tf)(x_j)\phi_j.
$$

Since $\operatorname{ran}T_\varepsilon\subseteq\bigvee\{\phi_1,\ldots,\phi_n\}$, $T_\varepsilon\in\mathcal B_{00}(C(X))$.

If $f\in\operatorname{ball}C(X)$ and $x\in X$, then

$$
\begin{aligned}
|(T_\varepsilon f)(x)-(Tf)(x)|
&=\left|\sum_{j=1}^n\bigl[(Tf)(x_j)-(Tf)(x)\bigr]\phi_j(x)\right|\\
&\leq\sum_{j=1}^n |(Tf)(x_j)-(Tf)(x)|\phi_j(x)\\
&<\varepsilon.
\end{aligned}
$$

■

If $X$ is locally compact, then the operators on $C_0(X)$ of finite rank are dense in $\mathcal B_0(C_0(X))$. See Exercise 18.

## Exercises

1. If $\mathcal X$ is reflexive and $A\in\mathcal B(\mathcal X,\mathcal Y)$, show that $A(\operatorname{ball}\mathcal X)$ is closed in $\mathcal Y$.
2. Prove Proposition 3.5.
3. If $A\in\mathcal B_0(\mathcal X,\mathcal Y)$, show that $\operatorname{cl}[\operatorname{ran}A]$ is separable.



   <a id="pdf-page-192"></a>
4. If $A\in\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ and $\operatorname{ran}A$ is closed, show that $\operatorname{ran}A$ is finite dimensional.

5. If $A\in\mathcal{B}_0(\mathcal{X})$ and $A$ is invertible, show that $\dim\mathcal{X}<\infty$.

6. Let $(X,\Omega,\mu)$ be a finite measure space, $1<p<\infty$, and $1/p+1/q=1$. If $k:X\times X\to\mathbb{F}$ is an $\Omega\times\Omega$-measurable function such that $\sup\left\{\int |k(x,y)|^q\,d\mu(y):x\in X\right\}<\infty$, then $(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)$ defines a compact operator on $L^p(\mu)$.

7. Let $(X,\Omega,\mu)$ be an arbitrary measure space, $1<p<\infty$, and $1/p+1/q=1$. If $k:X\times X\to\mathbb{F}$ is an $\Omega\times\Omega$-measurable function such that
   $$M=\left[\int\left(\int |k(x,y)|^p\,d\mu(x)\right)^{q/p}d\mu(y)\right]^{1/q}<\infty$$
   and if $(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)$, then $K\in\mathcal{B}_0(L^p(\mu))$ and $\|K\|\leq M$.

8. Let $X$ be a compact space and let $\mu$ be a positive Borel measure on $X$. Let $T\in\mathcal{B}(L^p(\mu),C(X))$ where $1<p<\infty$. Show that if $A:L^p(\mu)\to L^p(\mu)$ is defined by $Af=Tf$, then $A$ is compact.

9. (B.J. Pettis) If $\mathcal{X}$ is reflexive and $T\in\mathcal{B}(\mathcal{X},\ell^1)$, then $T$ is a compact operator. Also, if $\mathcal{Y}$ is reflexive and $T\in\mathcal{B}(c_0,\mathcal{Y})$, $T$ is compact.

10. If $X$ is compact and $\{f_1,\ldots,f_n,g_1,\ldots,g_n\}\subseteq C(X)$, define $k(x,y)=\sum_{j=1}^n f_j(x)g_j(y)$ for $x,y\in X$. Let $\mu$ be a regular Borel measure on $X$ and put $Kf(x)=\int k(x,y)f(y)\,d\mu(y)$. Show that $K\in\mathcal{B}(C(X))$ and $K$ has finite rank.

11. If $X$ is compact, $k\in C(X\times X)$, and $\mu$ is a regular Borel measure on $X$, show that $Kf(x)=\int k(x,y)f(y)\,d\mu(y)$ defines a compact operator on $C(X)$.

12. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and for $\phi$ in $L^\infty(\mu)$ let $M_\phi:L^p(\mu)\to L^p(\mu)$ be the multiplication operator defined in Example III.2.2. Give necessary and sufficient conditions on $(X,\Omega,\mu)$ and $\phi$ for $M_\phi$ to be compact.

13. Let $\tau:[0,1]\to[0,1]$ be continuous and define $A:C[0,1]\to C[0,1]$ by $Af=f\circ\tau$. Give necessary and sufficient conditions on $\tau$ for $A$ to be compact.

14. Let $A\in\mathcal{B}(c_0)$ and let $(\alpha_{mn})$ be the corresponding matrix as in Exercise 1.7. Give necessary and sufficient conditions on $(\alpha_{mn})$ for $A$ to be compact.

15. Let $A\in\mathcal{B}(\ell^1)$ and let $(\alpha_{mn})$ be the corresponding matrix as in Exercise 1.8. Give a necessary and sufficient condition on $(\alpha_{mn})$ for $A$ to be compact.

16. If $(X,d)$ is a compact metric space and $\mathcal{F}\subseteq C(X)$, show that $\mathcal{F}$ is equicontinuous if and only if for every $\varepsilon>0$ there is a $\delta>0$ such that $|f(x)-f(y)|<\varepsilon$ whenever $d(x,y)<\delta$ and $f\in\mathcal{F}$.

17. If $X$ is locally compact and $\mathcal{F}\subseteq C_0(X)$, show that $\mathcal{F}$ is totally bounded if and only if (a) $\mathcal{F}$ is bounded; (b) $\mathcal{F}$ is equicontinuous; (c) for every $\varepsilon>0$ there is a compact subset $K$ of $X$ such that $|f(x)|<\varepsilon$ for all $f$ in $\mathcal{F}$ and $x$ in $X\setminus K$.

18. If $X$ is locally compact and $A\in\mathcal{B}_0(C_0(X))$, then there is a sequence $\{A_n\}$ of finite-rank operators such that $\|A_n-A\|\to0$.

19. Let $\mathcal{X}$ be a Banach space and suppose there is a net $\{F_i\}$ of finite-rank operators on $\mathcal{X}$ such that (a) $\sup_i\|F_i\|<\infty$; (b) $\|F_ix-x\|\to0$ for all $x$ in $\mathcal{X}$. Show that if $A\in\mathcal{B}_0(\mathcal{X})$, then $\|F_iA-A\|\to0$ and hence there is a sequence $\{A_n\}$ of finite-rank operators on $\mathcal{X}$ such that $\|A_n-A\|\to0$.



    <a id="pdf-page-193"></a>
20. Let $1\leq p\leq\infty$ and let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space. If $A\in\mathcal B_0(L^p(\mu))$, show that there is a sequence $\{A_n\}$ of finite-rank operators such that $\|A_n-A\|\to0$. (Hint: Use Exercise 19.)

21. Let $X$ be compact and let $\mathcal U$ be the collection of all pairs $(C,F)$ where $C=\{U_1,\ldots,U_n\}$ is a finite open cover of $X$ and $F=\{x_1,\ldots,x_n\}\subseteq X$ such that $x_j\in U_j$ for $1\leq j\leq n$. If $(C_1,F_1)$ and $(C_2,F_2)\in\mathcal U$, define $(C_1,F_1)\leq(C_2,F_2)$ to mean: (a) $C_2$ is a refinement of $C_1$; that is, each member of $C_2$ is contained in some member of $C_1$. (b) $F_1\subseteq F_2$. If $\alpha=(C,F)\in\mathcal U$ let $\{\phi_1,\ldots,\phi_n\}$ be a partition of unity subordinate to $C$. If $F=\{x_1,\ldots,x_n\}$, define $T_\alpha:C(X)\to C(X)$ by

   $$
   (T_\alpha f)(x)=\sum_{j=1}^{n}f(x_j)\phi_j(x).
   $$

   Then: (a) $T_\alpha\in\mathcal B_{00}(C(X))$; (b) $\|T_\alpha\|=1$; (c) $(\mathcal U,\leq)$ is a directed set and $\{T_\alpha:\alpha\in\mathcal U\}$ is a net; (d) $\|T_\alpha f-f\|\to0$ for each $f$. Now apply Exercise 19 to obtain a new proof of Theorem 3.11.

## §4. Invariant Subspaces

<!-- BEGIN BACKGROUND BG-VI.block4 -->
<a id="bg-vi-9"></a>
### Lemma BG-VI.9 — Closing an orbit preserves invariance

If $\mathcal A$ is a unital algebra of bounded operators and $x\ne0$, the space $M=\overline{\{Ax:A\in\mathcal A\}}$ is a closed linear subspace, contains $x$, and is invariant under every member of $\mathcal A$.

**Proof.** The orbit here is linear because $\mathcal A$ is linear. It contains $x=Ix$. If $A_nx\to y$ and $B\in\mathcal A$, continuity gives $By=\lim BA_nx\in M$ because $BA_n\in\mathcal A$. $\square$

This fills the dense-orbit step in Lomonosov's lemma. “Nontrivial” means neither $\{0\}$ **nor** the whole space; thus the defining exclusions are joined by “and.” In complex dimension at least two, a one-dimensional eigenvector space is proper; dimension one must be excluded from any assertion that every operator has a nontrivial invariant subspace. Existence of complex polynomial roots, if not familiar beyond linear algebra, follows from Liouville's theorem in the [complex-analysis background](background-complex-analysis.md).
<!-- END BACKGROUND BG-VI.block4 -->

**4.1. Definition.** If $\mathcal X$ is a Banach space and $T\in\mathcal B(\mathcal X)$, an *invariant subspace* for $T$ is a closed linear subspace $\mathcal M$ of $\mathcal X$ such that $Tx\in\mathcal M$ whenever $x\in\mathcal M$. $\mathcal M$ is nontrivial if $\mathcal M\neq(0)$ or $\mathcal X$. $\operatorname{Lat}T=$ the collection of all invariant subspaces for $T$. If $\mathcal A\subseteq\mathcal B(\mathcal X)$, then $\operatorname{Lat}\mathcal A=\bigcap\{\operatorname{Lat}T:T\in\mathcal A\}$.

This generalizes the corresponding concept of invariant subspace for an operator on Hilbert space (II.3.5). Note that the idea of a reducing subspace for an operator on a Hilbert space has no generalization to Banach spaces since there is no concept of an orthogonal complement in Banach spaces.

**4.2. Proposition.**

(a) If $\mathcal M_1,\mathcal M_2\in\operatorname{Lat}T$, then $\mathcal M_1\vee\mathcal M_2\equiv\operatorname{cl}(\mathcal M_1+\mathcal M_2)\in\operatorname{Lat}T$ and $\mathcal M_1\wedge\mathcal M_2\equiv\mathcal M_1\cap\mathcal M_2\in\operatorname{Lat}T$.

(b) If $\{\mathcal M_i:i\in I\}\subseteq\operatorname{Lat}T$, then $\vee\{\mathcal M_i:i\in I\}$, the closed linear span of $\bigcup_i\mathcal M_i$, and $\wedge\{\mathcal M_i:i\in I\}\equiv\bigcap_i\mathcal M_i$ belong to $\operatorname{Lat}T$.

The proof of this proposition is left as an exercise. The proposition, however, does justify the use of the symbol “Lat” to denote the collection of invariant subspaces. With the operations $\vee$ and $\wedge$, $\operatorname{Lat}T$ is a lattice (a) that is complete (b). Moreover, $\operatorname{Lat}T$ has a largest element, $\mathcal X$, and a smallest element, $(0)$.

The main question is: does $\operatorname{Lat}T$ have any elements besides $(0)$ and $\mathcal X$? In other words, does $T$ have a nontrivial invariant subspace? C.J. Read [1984] showed the existence of a Banach space and an operator on the Banach space having no non-trivial invariant subspaces. This was preceded by some work of P Enflo (not published, but circulated) which did the same



<a id="pdf-page-194"></a>
thing. Later B Beauzamy [1985] sorted out Enflo’s ideas and gave an exposition and simplification of Enflo’s construction. Enflo’s work eventually appeared in Enflo [1987]. Read [1986] gave a self contained exposition showing that there is a bounded operator on $l^1$ having no nontrivial invariant subspace. This deep work does not completely settle the matter. Which Banach spaces $\mathcal{X}$ have the property that there is a bounded operator on $\mathcal{X}$ with no nontrivial invariant subspaces? If $\mathcal{X}$ is reflexive, is $\operatorname{Lat} T$ nontrivial for every $T$ in $\mathcal{B}(\mathcal{X})$? The question is unanswered even if $\mathcal{X}$ is a Hilbert space. However, for certain specific operators and classes of operators it has been shown that the lattice of invariant subspaces is not trivial. In this section it will be shown that any compact operator has a nontrivial invariant subspace. This will be obtained as a corollary of a more general result of V. Lomonosov. But first some examples.

**4.3. Example.** If $\mathcal{X}$ is a finite dimensional space over $\mathbb{C}$ and $T\in\mathcal{B}(\mathcal{X})$, then $\operatorname{Lat} T$ is not trivial. In fact, let $\mathcal{X}=\mathbb{C}^d$ and let $T=$ a matrix. Then $p(z)=\det(T-zI)$ is a polynomial of degree $d$. Hence it has a zero, say $\alpha$. If $\det(T-\alpha I)=0$, then $(T-\alpha I)$ is not invertible. But in finite dimensional spaces this means that $T-\alpha I$ is not injective. Thus $\ker(T-\alpha I)\ne(0)$. Let $\mathcal{M}\leq\ker(T-\alpha I)$ such that $\mathcal{M}\ne(0)$. If $x\in\mathcal{M}$, then $Tx=\alpha x\in\mathcal{M}$, so $\mathcal{M}\in\operatorname{Lat} T$.

**4.4. Example.** If $T=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ on $\mathbb{R}^2$, then $\operatorname{Lat} T$ is trivial. Indeed, if $\operatorname{Lat} T$ is not trivial, there is a one-dimensional space $\mathcal{M}$ in $\operatorname{Lat} T$. Let $\mathcal{M}=\{\alpha e:\alpha\in\mathbb{R}\}$. Since $\mathcal{M}\in\operatorname{Lat} T$, $Te=\lambda e$ for some $\lambda$ in $\mathbb{R}$. Hence $T^2e=T(Te)=\lambda Te=\lambda^2e$. But $T^2=-I$, so $-e=\lambda^2e$ and it must be that $\lambda^2=-1$ if $e\ne0$. But this cannot be if $\lambda$ is real.

If $d\geq3$, however, and $T\in\mathcal{B}(\mathbb{R}^d)$, then $\operatorname{Lat} T$ is not trivial (Exercise 6).

**4.5. Example.** If $V:L^2[0,1]\to L^2[0,1]$ is the Volterra operator, $Vf(x)=\int_0^x f(t)\,dt$, and $0\leq\alpha\leq1$, put $\mathcal{M}_\alpha=\{f\in L^2[0,1]:f(t)=0\text{ for }0\leq t\leq\alpha\}$. Then $\mathcal{M}_\alpha\in\operatorname{Lat} V$. Moreover, it can be shown $\operatorname{Lat} V=\{\mathcal{M}_\alpha:0\leq\alpha\leq1\}$. (See Donoghue [1957], and Radjavi and Rosenthal [1973], p. 68.)

**4.6. Example.** If $S:l^p\to l^p$ is defined by $S(\alpha_1,\alpha_2,\ldots)=(0,\alpha_1,\alpha_2,\ldots)$, and $\mathcal{M}_n=\{x\in l^p:x(k)=0\text{ for }1\leq k\leq n\}$, then $\mathcal{M}_n\in\operatorname{Lat} S$.

**4.7. Example.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and for $\phi$ in $L^\infty(\mu)$ let $M_\phi$ denote the multiplication operator on $L^p(\mu)$, $1\leq p\leq\infty$. If $\Delta\in\Omega$, let $\mathcal{M}_\Delta=\{f\in L^p(\mu):f=0\text{ a.e. }[\mu]\text{ off }\Delta\}$. Then for each $\phi$ in $L^\infty(\mu)$, $\mathcal{M}_\Delta\in\operatorname{Lat} M_\phi$.

It is a difficult if not impossible task to determine all the invariant subspaces of a specific operator. The Volterra operator and the shift operator are examples where all the invariant subspaces have been determined. But there



<a id="pdf-page-195"></a>
are multiplication operators $M_\phi$ for which there is no characterization of $\operatorname{Lat} M_\phi$ as well as some $M_\phi$ for which such a characterization has been achieved. One such example follows: let $\mu=$ Lebesgue area measure on $\mathbb{D}$ and let $(Af)(z)=zf(z)$ for $f$ in $L^2(\mu)$. There is no known characterization of $\operatorname{Lat} A$.

It is necessary at this point to return to the geometry of Banach spaces to prove the following classical theorem, which appeared as Exercise V.13.2.

**4.8. Mazur’s Theorem.** *If $\mathcal{X}$ is a Banach space and $K$ is a compact subset of $\mathcal{X}$, then $\overline{\operatorname{co}}(K)$ is compact.*

**PROOF.** It suffices to show that $\overline{\operatorname{co}}(K)$ is totally bounded. Let $\varepsilon>0$ and choose $x_1,\ldots,x_n$ in $K$ such that $K\subseteq\bigcup_{j=1}^{n}B(x_j;\varepsilon/4)$. Put $C=\operatorname{co}\{x_1,\ldots,x_n\}$. It is easy to see that $C$ is compact (Exercise V.7.8). Hence there are vectors $y_1,\ldots,y_m$ in $C$ such that $C\subseteq\bigcup_{i=1}^{m}B(y_i;\varepsilon/4)$. If $w\in\overline{\operatorname{co}}(K)$, there is a $z$ in $\operatorname{co}(K)$ with $\|w-z\|<\varepsilon/4$. Thus $z=\sum_{p=1}^{l}\alpha_p k_p$, where $k_p\in K$, $\alpha_p\geq 0$, and $\sum\alpha_p=1$. Now for each $k_p$ there is an $x_{j(p)}$ with $\|k_p-x_{j(p)}\|<\varepsilon/4$. Therefore

$$
\begin{aligned}
\left\|z-\sum_{p=1}^{l}\alpha_p x_{j(p)}\right\|
&=\left\|\sum_{p=1}^{l}\alpha_p(k_p-x_{j(p)})\right\|\\
&\leq\sum_{p=1}^{l}\alpha_p\|k_p-x_{j(p)}\|\\
&<\varepsilon/4.
\end{aligned}
$$

But $\sum_p\alpha_p x_{j(p)}\in C$ so there is a $y_i$ with $\|\sum_p\alpha_p x_{j(p)}-y_i\|<\varepsilon/4$. The triangle inequality now shows that $\overline{\operatorname{co}}(K)\subseteq\bigcup_{i=1}^{m}B(y_i;\varepsilon)$ and so $\overline{\operatorname{co}}(K)$ is totally bounded. ■

The next result is from Lomonosov [1973]. When it appeared it caused great excitement, both for the strength of its conclusion and for the simplicity of its proof. The proof uses Schauder’s Fixed-Point Theorem (V.9.5).

**4.9. Lomonosov’s Lemma.** *If $\mathcal{A}$ is a subalgebra of $\mathcal{B}(\mathcal{X})$ such that $1\in\mathcal{A}$ and $\operatorname{Lat}\mathcal{A}=\{(0),\mathcal{X}\}$ and if $K$ is a nonzero compact operator on $\mathcal{X}$, then there is an $A$ in $\mathcal{A}$ such that $\ker(AK-1)\ne(0)$.*

**PROOF.** It may be assumed that $\|K\|=1$. Fix $x_0$ in $\mathcal{X}$ such that $\|Kx_0\|>1$ and put $S=\{x\in\mathcal{X}:\|x-x_0\|\leq 1\}$. It is easy to check that

$$
\tag*{4.10}
0\notin S\ \text{and}\ 0\notin\operatorname{cl}K(S).
$$

Now if $x\in\mathcal{X}$ and $x\ne 0$, $\operatorname{cl}\{Tx:T\in\mathcal{A}\}$ is an invariant subspace for $\mathcal{A}$ (because $\mathcal{A}$ is an algebra) that contains the nonzero vector $x$ (because $1\in\mathcal{A}$). By hypothesis, $\operatorname{cl}\{Tx:T\in\mathcal{A}\}=\mathcal{X}$. By (4.10) this says that for every $y$ in $\operatorname{cl}K(S)$ there is a $T$ in $\mathcal{A}$ with $\|Ty-x_0\|<1$. Equivalently,


<a id="pdf-page-196"></a>
$$
\operatorname{cl}K(S)\subseteq\bigcup_{T\in\mathcal A}\{y:\|Ty-x_0\|<1\}.
$$

Because $\operatorname{cl}K(S)$ is compact, there are $T_1,\ldots,T_n$ in $\mathcal A$ such that

$$
\operatorname{cl}K(S)\subseteq\bigcup_{j=1}^{n}\{y:\|T_jy-x_0\|<1\}. \tag{4.11}
$$

For $y$ in $\operatorname{cl}K(S)$ and $1\leq j\leq n$, let $a_j(y)=\max\{0,1-\|T_jy-x_0\|\}$. By (4.11), $\sum_{j=1}^{n}a_j(y)>0$ for all $y$ in $\operatorname{cl}K(S)$. Define $b_j:\operatorname{cl}K(S)\to\mathbb R$ by

$$
b_j(y)=\frac{a_j(y)}{\sum_{i=1}^{n}a_i(y)},
$$

and define $\psi:S\to\mathcal X$ by

$$
\psi(x)=\sum_{j=1}^{n}b_j(Kx)T_jKx.
$$

It is easy to see that $a_j:\operatorname{cl}K(S)\to[0,1]$ is a continuous function. Hence $b_j$ and $\psi$ are continuous.

If $x\in S$, then $Kx\in K(S)$. If $b_j(Kx)>0$, then $a_j(Kx)>0$ and so $\|T_jKx-x_0\|<1$. That is, $T_jKx\in S$ whenever $b_j(Kx)>0$. Since $S$ is a convex set and $\sum_{j=1}^{n}b_j(Kx)=1$ for $x$ in $S$,

$$
\psi(S)\subseteq S.
$$

Note that $T_jK\in\mathcal B_0(\mathcal X)$ for each $j$ so that $\bigcup_{j=1}^{n}T_jK(S)$ has compact closure. By Mazur’s Theorem, $\overline{\operatorname{co}}\bigl(\bigcup_{j=1}^{n}T_jK(S)\bigr)$ is compact. But this convex set contains $\psi(S)$ so that $\operatorname{cl}\psi(S)$ is compact. This is, $\psi$ is a compact map. By the Schauder Fixed-Point Theorem, there is a vector $x_1$ in $S$ such that $\psi(x_1)=x_1$.

Let $\beta_j=b_j(Kx_1)$ and put $A=\sum_{j=1}^{n}\beta_jT_j$. So $A\in\mathcal A$ and $AKx_1=\psi(x_1)=x_1$. Since $x_1\ne0$ (Why?), $\ker(AK-1)\ne0$. ■

**4.12. Definition.** If $T\in\mathcal B(\mathcal X)$, then a *hyperinvariant subspace* for $T$ is a subspace $\mathcal M$ of $\mathcal X$ such that $A\mathcal M\subseteq\mathcal M$ for every operator $A$ in the commutant of $T$, $\{T\}'$; that is, $A\mathcal M\subseteq\mathcal M$ whenever $AT=TA$.

Note that every hyperinvariant subspace for $T$ is invariant.

**4.13. Lomonosov’s Theorem.** *If $\mathcal X$ is a Banach space over $\mathbb C$, $T\in\mathcal B(\mathcal X)$, $T$ is not a multiple of the identity, and $TK=KT$ for some nonzero compact operator $K$, then $T$ has a nontrivial hyperinvariant subspace.*

**Proof.** Let $\mathcal A=\{T\}'$. We want to show that $\operatorname{Lat}\mathcal A\ne\{(0),\mathcal X\}$. If this is not the case, then Lomonosov’s Lemma implies that there is an operator $A$ in $\mathcal A$ such that $\mathcal N=\ker(AK-1)\ne(0)$. But $\mathcal N\in\operatorname{Lat}(AK)$ and $AK|_{\mathcal N}$ is the



<a id="pdf-page-197"></a>
identity operator. Since $AK\in\mathcal B_0(\mathcal X)$, $AK|_{\mathcal N}\in\mathcal B_0(\mathcal N)$. Thus $\dim\mathcal N<\infty$. Since $AK\in\mathcal A=\{T\}'$, for any $x$ in $\mathcal N$, $AK(Tx)=T(AKx)=Tx$; hence $T\mathcal N\subseteq\mathcal N$. But $\dim\mathcal N<\infty$ so that $T|_{\mathcal N}$ must have an eigenvalue $\lambda$. Thus $\ker(T-\lambda)=\mathcal M\ne(0)$. But $\mathcal M\ne\mathcal X$ since $T$ is not a multiple of the identity. It is easy to check that $\mathcal M$ is hyperinvariant for $T$. $\blacksquare$

A proof of a slightly weaker version of Lomonosov’s Theorem that avoids Schauder’s Fixed Point Theorem can be found in Michaels [1977].

**4.14. Corollary.** (Aronszajn–Smith [1954].) *If $K\in\mathcal B_0(\mathcal X)$, then $\operatorname{Lat}K$ is nontrivial.*

The next result appeared in Bernstein and Robinson [1966], where it is proved using nonstandard analysis. Halmos [1966] gave a proof using standard analysis. Now it is an easy consequence of Lomonosov’s Theorem.

**4.15. Corollary.** *If $\mathcal X$ is infinite dimensional, $A\in\mathcal B(\mathcal X)$, and there is a polynomial in one variable, $p$, such that $p(A)\in\mathcal B_0(\mathcal X)$, then $\operatorname{Lat}A$ is nontrivial.*

**Proof.** If $p(A)\ne0$, then Lomonosov’s Theorem applies. If $p(A)=0$, let $p(z)=\alpha_0+\alpha_1z+\cdots+\alpha_nz^n$, $\alpha_n\ne0$. For $x\ne0$, let $\mathcal M=\bigvee\{x,Ax,\ldots,A^{n-1}x\}$. Since $A^n=-\alpha_n^{-1}[\alpha_0+\alpha_1A+\cdots+\alpha_{n-1}A^{n-1}]$, $\mathcal M\in\operatorname{Lat}A$. Since $x\in\mathcal M$, $\mathcal M\ne(0)$; since $\dim\mathcal M<\infty$, $\mathcal M\ne\mathcal X$. $\blacksquare$

**4.16. Corollary.** *If $K_1,K_2\in\mathcal B_0(\mathcal X)$ and $K_1K_2=K_2K_1$, then $K_1$ and $K_2$ have a common nontrivial invariant subspace.*

## Exercises

1. Let $A,B,T\in\mathcal B(\mathcal X)$ such that $TA=BT$. Show that $\operatorname{graph}(T)\in\operatorname{Lat}(A\oplus B)$.

2. Prove that $\mathcal M\in\operatorname{Lat}T$ if and only if $\mathcal M^\perp\in\operatorname{Lat}T^*$. What does the map $\mathcal M\mapsto\mathcal M^\perp$ of $\operatorname{Lat}T$ into $\operatorname{Lat}T^*$ do to the lattice operations?

3. Let $\{e_1,e_2,e_3\}$ be the usual basis for $\mathbb F^3$ and let $\alpha_1,\alpha_2,\alpha_3\in\mathbb F$. Define $T:\mathbb F^3\to\mathbb F^3$ by $Te_j=\alpha_je_j$, $1\le j\le3$. (a) If $\alpha_1,\alpha_2,\alpha_3$ are all distinct, show that $\mathcal M\in\operatorname{Lat}T$ if and only if $\mathcal M=\bigvee E$, where $E\subseteq\{e_1,e_2,e_3\}$. (b) If $\alpha_1=\alpha_2\ne\alpha_3$, show that $\mathcal M\in\operatorname{Lat}T$ if and only if $\mathcal M=\mathcal N+\mathcal L$, where $\mathcal N\le\bigvee\{e_1,e_2\}$ and $\mathcal L\le\{\alpha e_3:\alpha\in\mathbb F\}$.

4. Generalize Exercise 3 by characterizing $\operatorname{Lat}T$, where $T$ is defined by $Te_j=\alpha_je_j$, $1\le j\le d$, for any choice of scalars $\alpha_1,\ldots,\alpha_d$ and where $\{e_1,\ldots,e_d\}$ is the usual basis for $\mathbb F^d$.

5. Let $\{e_1,\ldots,e_d\}$ be the usual basis for $\mathbb F^d$, let $\{\alpha_1,\ldots,\alpha_{d-1}\}\subseteq\mathbb F$ with no $\alpha_j=0$. If $Te_j=\alpha_je_{j+1}$ for $1\le j\le d-1$ and $Te_d=0$, find $\operatorname{Lat}T$.

6. If $T\in\mathcal B(\mathbb R^d)$ and $d\ge3$, show that $T$ has a nontrivial subspace.

7. Show that if $T\in\mathcal B(\mathcal X)$ and $\mathcal X$ is not separable, then $T$ has a nontrivial invariant subspace.



   <a id="pdf-page-198"></a>
8. Give an example of an invertible operator $T$ on a Banach space $\mathcal X$ and an invariant subspace $\mathcal M$ for $T$ such that $\mathcal M$ is not invariant for $T^{-1}$.

9. Let $\mathcal X$ be a Banach space over $\mathbb C$, let $K\in\mathcal B_0(\mathcal X)$ and show that if $\mathcal C$ is a maximal chain in $\operatorname{Lat}K$, then $\mathcal C$ is a maximal chain in the lattice of all subspaces of $\mathcal X$.

## §5. Weakly Compact Operators

<!-- BEGIN BACKGROUND BG-VI.block5 -->
<a id="bg-vi-10"></a>
### Lemma BG-VI.10 — Canonical embeddings and bidual images

Write $J_X:X\to X^{**}$ for the canonical isometry. For bounded $T:X\to Y$, $T^{**}J_X=J_YT$. Moreover
$$
T^{**}(B_{X^{**}})=\overline{J_YT(B_X)}^{\sigma(Y^{**},Y^*)}.
$$

**Proof.** Evaluate the first identity at $g\in Y^*$: both sides give $g(Tx)$. For the second, Goldstine's theorem (V.4.1) gives weak-star density of $J_XB_X$ in $B_{X^{**}}$. Weak-star continuity of $T^{**}$ shows that every image point lies in the closure on the right. Conversely, the image of the weak-star compact ball under $T^{**}$ is compact and hence closed in the Hausdorff weak-star topology, and contains $J_YT(B_X)$. $\square$

This proves the “argument using Alaoglu” in 5.3(d). Another implicit step there is that $J_YY$ is norm closed, since $Y$ is complete and $J_Y$ is an isometry. Thus if a bidual point is within $2^{-n}$ of $J_YY$ for every $n$, it belongs to $J_YY$. Finally an isometry $\Phi:R\to X$ has surjective adjoint: for $r^*\in R^*$, define $\ell(\Phi r)=r^*(r)$ on $\Phi(R)$ and extend $\ell$ to $X$ by Hahn–Banach. The extension is a preimage under $\Phi^*$.
<!-- END BACKGROUND BG-VI.block5 -->

**5.1. Definition.** If $\mathcal X$ and $\mathcal Y$ are Banach spaces, an operator $T$ in $\mathcal B(\mathcal X,\mathcal Y)$ is *weakly compact* if the closure of $T(\operatorname{ball}\mathcal X)$ is weakly compact.

Weakly compact operators are generalizations of compact operators, but the hypothesis is not sufficiently strong to yield good information about their structure.

Recall that in a reflexive Banach space the weak closure of any bounded set is weakly compact. Also, a bounded operator $T:\mathcal X\to\mathcal Y$ is continuous if both $\mathcal X$ and $\mathcal Y$ have their weak topologies (1.1). With these facts in mind, the proof of the next result becomes an easy exercise for the reader.

**5.2. Proposition.**

(a) *If either $\mathcal X$ or $\mathcal Y$ is reflexive, then every operator in $\mathcal B(\mathcal X,\mathcal Y)$ is weakly compact.*

(b) *If $T:\mathcal X\to\mathcal Y$ is weakly compact and $A\in\mathcal B(\mathcal Y,\mathcal Z)$, then $AT$ is weakly compact.*

(c) *If $T:\mathcal X\to\mathcal Y$ is weakly compact and $B\in\mathcal B(\mathcal Z,\mathcal X)$, then $TB$ is weakly compact.*

This proposition shows that assuming that an operator is weakly compact is not that strong an assumption. For example, if $\mathcal X$ is reflexive, every operator in $\mathcal B(\mathcal X)$ is weakly compact. In particular, every operator on a Hilbert space is weakly compact. So any theorem about weakly compact operators is a theorem about all operators on a reflexive space.

In fact, there is a degree of validity for the converse of this statement. In a certain sense, theorems about operators on reflexive spaces are also theorems about weakly compact operators. The precise meaning of this statement is the content of Theorem 5.4 below. But before we begin to prove this, a lemma is needed.

Let $\mathcal Y$ be a Banach space and let $W$ be a bounded convex balanced subset of $\mathcal Y$. For $n>1$ put $U_n=2^nW+2^{-n}\operatorname{int}[\operatorname{ball}\mathcal Y]$. Let $p_n=$ the gauge of $U_n$ (IV.1.14). Because $U_n\supseteq 2^{-n}\operatorname{int}[\operatorname{ball}\mathcal Y]$, it is easy to check that $p_n$ is a norm on $\mathcal Y$. In fact, $p_n$ and $\|\cdot\|$ are equivalent norms. To see this note that if $\|y\|<1$, then $2^{-n}y\in U_n$ so that $p_n(y)<2^n$. Hence $p_n(y)\leqslant 2^n\|y\|$. Also, because $W$ is bounded, $U_n$ must be bounded; let $M>\sup\{\|y\|:y\in U_n\}$. So if $p_n(y)<1$, $\|y\|<M$. Thus $\|y\|\leqslant Mp_n(y)$, and $\|\cdot\|$ and $p_n$ are equivalent norms.


<a id="pdf-page-199"></a>
**5.3. Lemma.** For a Banach space $\mathcal Y$ let $W$, $U_n$, and $p_n$ be as above. Let $\mathcal R$ be the set of all $y$ in $\mathcal Y$ such that $\vert\!\vert\!\vert y\vert\!\vert\!\vert\equiv\left[\sum_{n=1}^{\infty}p_n(y)^2\right]^{1/2}<\infty$. Then

(a) $W\subseteq\{y:\vert\!\vert\!\vert y\vert\!\vert\!\vert<1\}$;

(b) $(\mathcal R,\vert\!\vert\!\vert\cdot\vert\!\vert\!\vert)$ is a Banach space and the inclusion map $A:\mathcal R\to\mathcal Y$ is continuous;

(c) $A^{**}:\mathcal R^{**}\to\mathcal Y^{**}$ is injective and $(A^{**})^{-1}(\mathcal Y)=\mathcal R$;

(d) $\mathcal R$ is reflexive if and only if $\operatorname{cl}W$ is weakly compact.

**Proof.** (a) If $w\in W$, then $2^nw\in U_n$. Hence $1>p_n(2^nw)=2^np_n(w)$, so $p_n(w)<2^{-n}$. Thus $\vert\!\vert\!\vert w\vert\!\vert\!\vert^2<\sum_n(2^{-n})^2<1$.

(b) Let $\mathcal Y_n=\mathcal Y$ with the norm $p_n$ and put $\mathcal X=\bigoplus_2\mathcal Y_n$ (III.4.4). Define $\Phi:\mathcal R\to\mathcal X$ by $\Phi(y)=(y,y,\ldots)$. It is easy to see that $\Phi$ is an isometry though it is clearly not surjective. In fact, $\operatorname{ran}\Phi=\{(y_n)\in\mathcal X:y_n=y_m\text{ for all }n,m\}$. Thus $\mathcal R$ is a Banach space. Let $P_1=$ the projection of $\mathcal X$ onto the first coordinate. Then $A=P_1\circ\Phi$ and hence $A$ is continuous.

(c) With the notation from the proof of (b), it follows that $\mathcal X^{**}=\bigoplus_2\mathcal Y_n^{**}$ and $\Phi^{**}:\mathcal R^{**}\to\mathcal X^{**}$ is given by $\Phi^{**}(y^{**})=(A^{**}y^{**},A^{**}y^{**},\ldots)$. Now the fact that $\Phi$ is an isometry implies that $\Phi^*$ is surjective. (This follows in two ways. One is by a direct argument (see Exercise 2). Also, $\operatorname{ran}\Phi^*$ is closed since $\operatorname{ran}\Phi$ is closed (1.10), and $\operatorname{ran}\Phi^*$ is dense since ${}^{\perp}(\operatorname{ran}\Phi^*)=\ker\Phi=(0)$.) Hence $\ker\Phi^{**}=(\operatorname{ran}\Phi^*)^\perp=(0)$; that is, $\Phi^{**}$ is injective. Therefore $A^{**}$ is injective.

Now let $y^{**}\in(A^{**})^{-1}(\mathcal Y)$. It follows that $\Phi^{**}y^{**}=x\in\mathcal X$. Let $\{y_i\}$ be a net in $\mathcal R$ such that $\vert\!\vert\!\vert y_i\vert\!\vert\!\vert\leq\vert\!\vert\!\vert y^{**}\vert\!\vert\!\vert$ for all $i$ and $y_i\to y^{**}$ $\sigma(\mathcal R^{**},\mathcal R^*)$ (V.4.1). Thus $\Phi^{**}(y_i)\to\Phi^{**}(y^{**})$ $\sigma(\mathcal X^{**},\mathcal X^*)$. But $\Phi^{**}(y_i)=\Phi(y_i)\in\mathcal X$ and $\Phi^{**}(y^{**})=x$. Hence $\Phi(y_i)\to x$ $\sigma(\mathcal X,\mathcal X^*)$. Since $\operatorname{ran}\Phi$ is closed, $x\in\operatorname{ran}\Phi$; let $\Phi(y)=x$. Then $0=\Phi^{**}(y^{**}-y)$. Since $\Phi^{**}$ is injective, $y^{**}=y\in\mathcal R$.

(d) An argument using Alaoglu’s Theorem shows that $A^{**}(\operatorname{ball}\mathcal R^{**})=$ the $\sigma(\mathcal Y^{**},\mathcal Y^*)$ closure of $A(\operatorname{ball}\mathcal R)$. Put $C=A(\operatorname{ball}\mathcal R)$. Suppose $\operatorname{cl}W$ is weakly compact. Now $C\subseteq 2^n\operatorname{cl}W+2^{-n}\operatorname{ball}\mathcal Y^{**}$ and this set is $\sigma(\mathcal Y^{**},\mathcal Y^*)$ compact. From the preceding comments, $A^{**}(\operatorname{ball}\mathcal R^{**})\subseteq 2^n\operatorname{cl}W+2^{-n}\operatorname{ball}\mathcal Y^{**}$. Thus,

$$
\begin{aligned}
A^{**}(\operatorname{ball}\mathcal R^{**})
&\subseteq \bigcap_{n=1}^{\infty}
\left[2^n\operatorname{cl}W+2^{-n}\operatorname{ball}\mathcal Y^{**}\right]\\
&\subseteq \bigcap_{n=1}^{\infty}
\left[\mathcal Y+2^{-n}\operatorname{ball}\mathcal Y^{**}\right]\\
&=\mathcal Y.
\end{aligned}
$$

By (c), $\mathcal R^{**}=\mathcal R$ and $\mathcal R$ is reflexive.

Now assume $\mathcal R$ is reflexive; thus $\operatorname{ball}\mathcal R$ is $\sigma(\mathcal R,\mathcal R^*)$-compact. Therefore $C=A(\operatorname{ball}\mathcal R)$ is weakly compact in $\mathcal Y$. By (a), $\operatorname{cl}W$ is weakly compact. $\blacksquare$

The next theorem, as well as the preceding lemma, are from Davis, Figiel, Johnson, and Pelczynski [1974].



<a id="pdf-page-200"></a>
**5.4. Theorem.** *If $\mathcal X,\mathcal Y$ are Banach spaces and $T\in\mathcal B(\mathcal X,\mathcal Y)$, then $T$ is weakly compact if and only if there is a reflexive space $\mathcal R$ and operators $A$ in $\mathcal B(\mathcal R,\mathcal Y)$ and $B$ in $\mathcal B(\mathcal X,\mathcal R)$ such that $T=AB$.*

**Proof.** If $T=AB$, where $A$, $B$ have the described form, then $T$ is weakly compact by Proposition 5.2.

Now assume that $T$ is weakly compact and put $W=T(\operatorname{ball}\mathcal X)$. Define $\mathcal R$ as in Lemma 5.3. By (5.3d), $\mathcal R$ is reflexive. Let $A:\mathcal R\to\mathcal Y$ be the inclusion map. Note that if $x\in\operatorname{ball}\mathcal X$, then $Tx\in W$. By (5.3a), $\lVert\!\lVert\!\lVert Tx\rVert\!\rVert\!\rVert<1$ whenever $\lVert x\rVert\leqslant1$. So $B:\mathcal X\to\mathcal R$ defined by $Bx=Tx$ is a bounded operator. Clearly $AB=T$. ■

The preceding result can be used to prove several standard results from antiquity.

**5.5. Theorem.** *If $\mathcal X,\mathcal Y$ are Banach spaces and $T\in\mathcal B(\mathcal X,\mathcal Y)$, the following statements are equivalent.*

(a) $T$ is weakly compact.

(b) $T^{**}(\mathcal X^{**})\subseteq\mathcal Y$.

(c) $T^*$ is weakly compact.

**Proof.** (a)$\Rightarrow$(b): Let $\mathcal R$ be a reflexive space, $A\in\mathcal B(\mathcal R,\mathcal Y)$, and $B\in\mathcal B(\mathcal X,\mathcal R)$ such that $T=AB$. So $T^{**}=A^{**}B^{**}$. But $A^{**}:\mathcal R\to\mathcal Y^{**}$ since $\mathcal R^{**}=\mathcal R$. Hence $A^{**}=A$. Thus $T^{**}=AB^{**}$, and so $\operatorname{ran}T^{**}\subseteq\operatorname{ran}A\subseteq\mathcal Y$.

(b)$\Rightarrow$(a): $T^{**}(\operatorname{ball}\mathcal X^{**})$ is $\sigma(\mathcal Y^{**},\mathcal Y^*)$ compact by Alaoglu’s Theorem and the weak* continuity of $T^{**}$. By (b), $T^{**}(\operatorname{ball}\mathcal X^{**})=C$ is $\sigma(\mathcal Y,\mathcal Y^*)$ compact in $\mathcal Y$. Hence $T(\operatorname{ball}\mathcal X)\subseteq C$ and must have weakly compact closure.

(c)$\Rightarrow$(a): Let $\mathcal S$ be a reflexive space, $C\in\mathcal B(\mathcal Y^*,\mathcal S)$, $D\in\mathcal B(\mathcal S,\mathcal X^*)$ such that $T^*=DC$. So $T^{**}=C^*D^*$, $D^*:\mathcal X^{**}\to\mathcal S^*$, and $C^*:\mathcal S^*\to\mathcal Y^{**}$. Put $\mathcal R=\operatorname{cl}D^*(\mathcal X)$ and $B=D^*|_{\mathcal X}$; then $B:\mathcal X\to\mathcal R$ and $\mathcal R$ is reflexive. Let $A=C^*|_{\mathcal R}$; so $A:\mathcal R\to\mathcal Y^{**}$. But if $x\in\mathcal X$, $ABx=C^*D^*x=T^{**}x=Tx\in\mathcal Y$. Thus $A:\mathcal R\to\mathcal Y$. Clearly $AB=T$.

(a)$\Rightarrow$(c): Exercise. ■

## Exercises

1. Prove Proposition 5.2.

2. If $\mathcal R$ and $\mathcal X$ are Banach spaces and $\Phi:\mathcal R\to\mathcal X$ is an isometry, give an elementary proof that $\Phi^*$ is surjective.

3. Let $\mathcal X$ be a Banach space and recall the definition of a weakly Cauchy sequence (V.4.4). (a) Show that every bounded sequence in $c_0$ has a weakly Cauchy subsequence, but not every weakly Cauchy sequence in $c_0$ converges. (b) Show that if $T\in\mathcal B(c_0)$ and $T$ is weakly compact, then $T$ is compact.

4. Say that a Banach space $\mathcal X$ is *weakly compactly generated* (WCG) if there is a weakly compact subset $K$ of $\mathcal X$ such that $\mathcal X$ is the closed linear span of $K$. Prove



   <a id="pdf-page-201"></a>
   (Davis, Figiel, Johnson, and Pelczynski, [1974]) that $\mathcal X$ is WCG if and only if there is a reflexive space and an injective bounded operator $T:\mathcal R\to\mathcal X$ such that $\operatorname{ran}T$ is dense. (Hint: The Krein–Smulian Theorem (V.13.4) may be useful.)

5. If $(X,\Omega,\mu)$ is a finite measure space, $k\in L^\infty(X\times X,\Omega\times\Omega,\mu\times\mu)$, and $K:L^1(\mu)\to L^1(\mu)$ is defined by $(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)$, show that $K$ is weakly compact and $K^2$ is compact.

6. Let $\mathcal Y$ be a weakly sequentially complete Banach space. That is, if $\{y_n\}$ is a sequence in $\mathcal Y$ such that $\{\langle y_n,y^*\rangle\}$ is a Cauchy sequence in $\mathbb F$ for every $y^*$ in $\mathcal Y^*$, then there is a $y$ in $\mathcal Y$ such that $y_n\to y$ weakly [see (V.4.4)]. (a) If $T\in\mathcal B(\mathcal X,\mathcal Y)$ and $x^{**}\in\mathcal X^{**}$ such that $x^{**}$ is the $\sigma(\mathcal X^{**},\mathcal X^*)$ limit of a sequence $\{x_n^{**}\}$ from $\mathcal X^{**}$ such that $T^{**}(x_n^{**})\in\mathcal Y$ for every $n$, show that $T^{**}(x^{**})\in\mathcal Y$. Let $X$ be a compact space and put $\mathcal F=$ all subsets of $X$ that are the union of a countable number of compact $G_\delta$ sets. Let $\mathcal L=$ the linear span of $\{\chi_F:F\in\mathcal F\}$ considered as a subset of $M(X)^*=C(X)^{**}$. (b) Show that if $T\in\mathcal B(C(X),\mathcal Y)$, then $T^{**}(\mathcal L)\subseteq\mathcal Y$. (c) (Grothendieck [1953].) If $T\in\mathcal B(C(X),\mathcal Y)$, then $T$ is weakly compact. [Hint (Spain [1976]): Use James’s Theorem V.13.3).]

<!-- BEGIN SOLUTIONS VI -->

## Exercise Solutions

These added solutions use the Banach-space adjoint: the dual pairing is
bilinear, so transposed matrices and kernels have no complex conjugates.
All subspaces in invariant-subspace lattices are closed. An operator is
compact when it sends the closed unit ball to a relatively norm-compact set.

### §1. Adjoints

#### Solution VI.1.1 — Linearity and weak-star continuity

For $f\in Y^*$ and $x\in X$,
$((\alpha A+\beta B)^*f)(x)=f(\alpha Ax+\beta Bx)
=\alpha(A^*f)(x)+\beta(B^*f)(x)$.
If $f_i\to f$ weak-star, then $(A^*f_i)(x)=f_i(Ax)\to f(Ax)$ for every
$x$, which is exactly weak-star convergence in $X^*$. This proves the
claimed continuity for nets, not just for sequences.

#### Solution VI.1.2 — Composition, inverse, and norm

Evaluation gives $((BA)^*f)(x)=f(BAx)=(A^*B^*f)(x)$, proving (d).
If $A$ is invertible, apply this to $A^{-1}A$ and $AA^{-1}$ to see that
$(A^{-1})^*$ is a two-sided inverse of $A^*$, proving (c).
For completeness, $A^{**}J_X=J_YA$ follows by testing on $Y^*$, and
$$\|A^*\|=\sup_{\|f\|\leq1,\|x\|\leq1}|f(Ax)|=\|A\|$$
by Hahn–Banach. These verify (a) and (b) as well.

#### Solution VI.1.3 — The multiplication adjoint

Under the bilinear representation $g(f)=\int fg\,d\mu$,
$\int(M_\phi f)g=\int f(\phi g)$. Since $\phi g\in L^q$ and
$\|\phi g\|_q\leq\|\phi\|_\infty\|g\|_q$, the representing dual vector
is $M_\phi g$. This includes $p=1,q=\infty$ under the chapter's
sigma-finite duality hypotheses.

#### Solution VI.1.4 — The transposed integral kernel

The row and column bounds in the cited example also bound the positive
kernel operator with kernel $|k|$. Thus for $f\in L^p,g\in L^q$,
$\iint|k(x,y)f(y)g(x)|\,d\mu(y)d\mu(x)<\infty$ by Hölder and that
operator bound. Fubini gives
$$\int(Kf)(x)g(x)\,d\mu(x)
=\int f(y)\left(\int k(x,y)g(x)\,d\mu(x)\right)d\mu(y).$$
The bracket is $K^*g(y)$, so its kernel is $k^*(y,x)=k(x,y)$.
The integrability verification is what permits the interchange.

#### Solution VI.1.5 — Pushforward of measures

For a continuous $\tau:Y\to X$, define $\nu(\Delta)=\mu(\tau^{-1}\Delta)$.
It is a finite regular measure on compact Hausdorff $X$: inner regularity
follows by mapping compact subsets of $\tau^{-1}\Delta$ to compact subsets
of $\Delta$, and outer regularity follows by complements for positive
finite measures and then total variation for signed or complex measures.
The pushforward identity, first for indicators, then simple functions,
then bounded measurable functions, gives
$\int_X f\,d\nu=\int_Y f\circ\tau\,d\mu$.
By the definition of the adjoint and uniqueness in Riesz representation,
$A^*\mu=\nu$.

#### Solution VI.1.6 — The shift adjoint

For $a\in\ell^p$ and $b\in\ell^q$,
$\sum_{j\geq1}(Sa)_jb_j=\sum_{j\geq1}a_jb_{j+1}$, with absolute
convergence by Hölder (also for $p=1,q=\infty$). Hence
$S^*(b_1,b_2,\ldots)=(b_2,b_3,\ldots)$, the backward shift.

#### Solution VI.1.7 — Matrices on c0

The $m$th row represents the functional $x\mapsto(Ax)(m)$ on $c_0$,
so its $\ell^1$ norm is at most $\|A\|$. Each column is $Ae_n\in c_0$,
proving (a) and (b). Conversely a matrix with these properties sends a
finitely supported vector to $c_0$, has supremum norm bound
$\|Ax\|_\infty\leq M\|x\|_\infty$, and therefore extends by density to
$c_0$. Its coordinate series converge absolutely and give the displayed
formula. Finite vectors with phases matching any finite row segment show
$\|A\|\geq\sum_{n\leq N}|\alpha_{mn}|$; take the two suprema to obtain
equality. The adjoint on $\ell^1$ is
$$(A^*b)(n)=\sum_m\alpha_{mn}b(m).$$
Indeed the double series has absolute sum at most $M\|b\|_1\|x\|_\infty$,
justifying rearrangement in the pairing; also
$\|A^*b\|_1\leq M\|b\|_1$.

#### Solution VI.1.8 — Matrices on ell-1

Each column is $Ae_n$, so its absolute sum is at most $\|A\|$. This also
implies (b), which is redundant once (a) holds. Conversely
$Ax=\sum_nx(n)(\alpha_{mn})_m$ converges absolutely in $\ell^1$ and
$\|Ax\|_1\leq M\|x\|_1$. Testing $e_n$ gives $\|A\|=M$.
For $b\in\ell^\infty$,
$$(A^*b)(n)=\sum_m\alpha_{mn}b(m),\qquad
\|A^*b\|_\infty\leq M\|b\|_\infty.$$
The absolute double-sum bound $M\|x\|_1\|b\|_\infty$ proves the adjoint
identity. No conjugation occurs with this pairing.

#### Solution VI.1.9 — Absolutely summable representations

In (ii), the test vector must be $x^*\in X^*$, not $X$ as transcribed.
Define $T:\ell^1(Z)\to X$ by the absolutely convergent sum in the hint.
Then $\|T\|\leq M_1$ and $\|T^*x^*\|_\infty\geq M_2\|x^*\|$.
The bipolar/separation theorem gives
$M_2B_X\subseteq\overline{T(B_{\ell^1})}$: otherwise a separating
functional contradicts the last inequality. For any $0<r<M_2$ and
$0<\theta<1$, approximate $x$ by $Tf_1$ with
$\|f_1\|_1\leq\|x\|/r$ and residual at most $\theta\|x\|$.
Repeat on the residuals. The series $f=\sum f_j$ converges in $\ell^1(Z)$,
$Tf=x$, and $\|f\|_1\leq\|x\|/[r(1-\theta)]$.
Let $r\uparrow M_2$ and $\theta\downarrow0$ to get
$\inf_{Tf=x}\|f\|_1\leq\|x\|/M_2$.
The other inequality is $\|x\|\leq M_1\|f\|_1$ for every representation.
Every $\ell^1(Z)$ vector has countable support, so the sums are ordinary
absolutely convergent series even when $Z$ is uncountable.

#### Solution VI.1.10 — Poisson kernels span L1 by summable series

Use VI.1.9 with $u(z)=p_z$, $M_1=M_2=1$. The Poisson kernels are positive
and have integral one. For $g\in L^\infty$, let
$g_r(e^{it})=\int p_{re^{it}}(w)g(w)\,dm(w)$. Then
$\|g_r\|_\infty\leq\|g\|_\infty$, and $g_r\to g$ in $L^1$ as $r\uparrow1$.
For clarity, the latter approximate-identity fact follows from continuity
of translations in $L^1$, integral one, and
$\sup_{|t|\geq\delta}P_r(t)\to0$: split the convolution error into
$|t|<\delta$ and its complement. Translation continuity follows first for
continuous functions by uniform continuity and then by their $L^1$ density.
If $\sup_{z}|\int p_zg|=c$, all $g_r$ are bounded by $c$; an almost-everywhere
convergent subsequence of the $L^1$ convergence gives $|g|\leq c$ almost
everywhere. Hence $c=\|g\|_\infty$, verifying (ii).
VI.1.9 now supplies the countable representation and the equality of the
infimum with $\|f\|_1$. The series converges in $L^1$, not necessarily
pointwise everywhere.

#### Solution VI.1.11 — Which operators are adjoints?

An adjoint is weak-star continuous by VI.1.1. Conversely, if $B$ is
weak-star continuous, then for fixed $x\in X$ the functional
$f\mapsto(Bf)(x)$ on $Y^*$ is weak-star continuous. V.1.3 gives a unique
$Ax\in Y$ with $f(Ax)=(Bf)(x)$. Uniqueness proves linearity of $A$, and
$$\|Ax\|=\sup_{\|f\|\leq1}|(Bf)(x)|\leq\|B\|\|x\|.$$
Thus $A$ is bounded and the defining identity gives $A^*=B$.

#### Solution VI.1.12 — Closed sums and the diagonal quotient map

Let $D:X\to X/M\oplus X/N$ be $Dx=(x+M,x+N)$.
If $M+N$ is closed, $D(X)$ is the kernel of the continuous map
$(u+M,v+N)\mapsto u-v+(M+N)$, so is closed.
Conversely, if $s_k=m_k+n_k\to s$, then
$D(m_k)=(0,s_k+N)\to(0,s+N)$. Closedness of $D(X)$ gives $x\in M$ with
$x+N=s+N$, proving $s\in M+N$. This proves (a) iff (b).
The adjoint has range $M^\perp+N^\perp$, since
$D^*(f,g)=f+g$ under the quotient-dual identifications.
The closed range theorem for $D$ makes (b), (c), and (d) equivalent.

### §3. Compact operators

#### Solution VI.3.1 — Closed image of a reflexive ball

The ball $B_X$ is weakly compact, and every bounded linear operator is
weak-to-weak continuous because $f(Ax)=(A^*f)(x)$. Thus $A(B_X)$ is weakly
compact and hence weakly closed in $Y$. Since norm convergence implies
weak convergence, it is also norm closed. Compactness of $A$ is not needed.

#### Solution VI.3.2 — The compact-operator ideal

(a) The image of a ball under a sum is contained in the sum of two
relatively compact sets; scalar multiples preserve relative compactness.
If $K_n\to K$ in operator norm, approximate $K(B_X)$ within
$\varepsilon/2$ by $K_n(B_X)$ and cover the latter by finitely many
$\varepsilon/2$-balls. Thus $K(B_X)$ is totally bounded; completeness of
$Y$ makes its closure compact. (b) A continuous $A$ sends the compact
closure of $K(B_X)$ to a compact set, so $AK$ is compact.
(c) $A(B_Z)\subseteq\|A\|B_X$, whose image under $K$ is relatively
compact; hence $KA$ is compact.

#### Solution VI.3.3 — Separable closed range

The compact metric space $C=\overline{A(B_X)}$ has a countable dense set,
obtained by taking finite $1/n$-nets. Since $A(X)=\bigcup_{n\geq1}nA(B_X)$,
it is contained in the closed linear span of this countable set. Conversely
$C\subseteq\overline{\operatorname{ran}A}$, so that closed span equals the
closed range. Rational linear combinations give a countable dense subset.

#### Solution VI.3.4 — A compact operator with closed range

Regard $A$ as a surjection onto the Banach space $R=\operatorname{ran}A$.
The open mapping theorem gives $c>0$ with $B_R\subseteq A(cB_X)$ (increase
$c$ to avoid issues about attainment of an infimum). Its right-hand side
has compact closure, so the closed ball $B_R$ is compact. By Riesz's lemma
an infinite-dimensional normed space has a sequence of unit vectors with
pairwise distances greater than $1/2$; its ball cannot be compact.
Therefore $R$ is finite dimensional.

#### Solution VI.3.5 — An invertible compact operator

If $A$ is invertible and compact, $I=A^{-1}A$ is compact by VI.3.2.
Its image of the unit ball is the unit ball itself. The Riesz-lemma
argument in VI.3.4 forces $\dim X<\infty$.

#### Solution VI.3.6 — Uniformly bounded rows of an integral kernel

Let $C^q=\sup_x\int|k(x,y)|^q\,d\mu(y)$. Hölder gives
$|Kf(x)|\leq C\|f\|_p$, hence $\|Kf\|_p\leq C\mu(X)^{1/p}\|f\|_p$.
For a bounded sequence in reflexive $L^p$, take a weakly convergent
subsequence $f_n\rightharpoonup f$. Each row $k(x,\cdot)\in L^q$ tests
this convergence, so $Kf_n(x)\to Kf(x)$. The uniform bound on
$|K(f_n-f)(x)|^p$ is an integrable constant because $\mu(X)<\infty$.
Dominated convergence gives norm convergence, proving compactness.

#### Solution VI.3.7 — A mixed-norm bound

First consider a sigma-finite measure space. Minkowski and Hölder give
$$\|Kf\|_p\leq\int\|k(\cdot,y)\|_p|f(y)|\,d\mu(y)
\leq M\|f\|_p.$$
For a bounded weakly null sequence $g_n\in L^q$, define
$Hg_n(y)=\int k(x,y)g_n(x)\,d\mu(x)$. For almost every $y$ its value tends
to zero by weak convergence, and
$|Hg_n(y)|^q\leq C^q\|k(\cdot,y)\|_p^q$, an integrable majorant.
Thus $Hg_n\to0$ in $L^q$ by dominated convergence. Reflexivity gives
compactness of $H$. Fubini, justified by the mixed-norm bound, identifies
$H=K^*$, and Schauder's theorem makes $K$ compact.

For an arbitrary measure space, the same Minkowski and Hölder estimate
first gives the displayed bound. Given a bounded sequence $f_n$, choose
a sigma-finite measurable set $E$ supporting all $f_n$, and a sigma-finite
measurable set $F$ supporting all $Kf_n$. Such supports exist for every
$L^p$ vector with $p<\infty$: the sets where its modulus is at least $1/j$
have finite measure, and a countable union also handles the whole sequence.
Restrict the kernel to $F\times E$. The preceding proof works unchanged
between $L^p(E)$ and $L^p(F)$, with mixed-norm bound at most $M$, so this
restricted operator is compact. Its values at $f_n$ are exactly $Kf_n$
restricted to $F$, and extension by zero preserves their norms. Hence the
original image sequence has a norm-convergent subsequence. This proves
compactness without a global sigma-finiteness hypothesis.

#### Solution VI.3.8 — An operator taking values in continuous functions

Under the usual convention that the positive Borel measure on compact
$X$ is finite, let $f_n\rightharpoonup f$ be a subsequence of any bounded
sequence in $L^p$. Evaluation at $x$ composed with $T$ is a bounded linear
functional, so $Tf_n(x)\to Tf(x)$ for every $x$. Also
$\|Tf_n-Tf\|_\infty$ is uniformly bounded. Dominated convergence with the
finite measure gives $\|Af_n-Af\|_p\to0$. Hence $A$ is compact.
Finiteness, or a substitute integrable domination hypothesis, matters:
for an unrestricted infinite Borel measure even the displayed definition
need not map into $L^p$. On a compact interval with infinite measure,
a nonzero bounded functional $\ell$ on $L^p$ defines
$Tf=\ell(f)1\in C(X)$, but this constant need not belong to $L^p$.

#### Solution VI.3.9 — Compactness forced by ell-1

A bounded sequence in reflexive $X$ has a weakly convergent subsequence.
Its $T$-images converge weakly in $\ell^1$ and therefore in norm by Schur's
theorem V.5.5. Thus $T:X\to\ell^1$ is compact.
For $T:c_0\to Y$ with $Y$ reflexive, $T^*:Y^*\to\ell^1$ has reflexive
domain and is compact by the first assertion. Schauder's theorem, which
identifies compactness of an operator and its adjoint, gives compactness
of $T$.

#### Solution VI.3.10 — A finite-sum kernel

Write $Kf=\sum_{j=1}^n f_j\ell_j(f)$, where
$\ell_j(f)=\int g_jf\,d\mu$ and
$|\ell_j(f)|\leq\|g_j\|_\infty|\mu|(X)\|f\|_\infty$.
This is bounded and has range in $\operatorname{span}\{f_1,\ldots,f_n\}$,
so has finite rank. The same proof covers signed and complex regular
measures of finite variation.

#### Solution VI.3.11 — A continuous kernel

By V.8.6, approximate $k$ uniformly by finite sums
$k_n(x,y)=\sum_j a_{nj}(x)b_{nj}(y)$. Their operators have finite rank by
VI.3.10, and
$\|K-K_n\|\leq|\mu|(X)\|k-k_n\|_\infty\to0$.
This also proves $Kf$ is continuous, as a uniform limit of continuous
$K_nf$. The norm-closedness of compact operators gives compactness.

#### Solution VI.3.12 — Compact multiplication operators

For every $\varepsilon>0$, the necessary and sufficient condition is that
$E_\varepsilon=\{|\phi|\geq\varepsilon\}$ consist, modulo null sets, of
finitely many atoms. Equivalently $L^p(E_\varepsilon)$ is finite dimensional.
Indeed on this subspace $\|M_\phi f\|_p\geq\varepsilon\|f\|_p$, including
$p=\infty$. Compactness would make its unit ball relatively compact via
the bounded inverse multiplier $1/\phi$, forcing finite dimension.
The atom characterization follows by constructing infinitely many
disjoint positive sets if the space is not a union of finitely many atoms;
their normalized indicators are separated unit vectors.
Conversely, $M_{\phi\chi_{E_\varepsilon}}$ has finite-dimensional range
and differs from $M_\phi$ by norm at most $\varepsilon$.
Thus $M_\phi$ is compact. This includes $\phi=0$ on all nonatomic parts
and atomic values tending to zero whenever infinitely many atoms occur.

#### Solution VI.3.13 — Composition on an interval

The necessary and sufficient condition is that $\tau$ be constant.
If constant, $Af=f(\tau(0))1$ has rank one. If not, its image is a
nondegenerate compact interval $J$. Restriction $C[0,1]\to C(J)$ maps
the unit ball onto the unit ball: extend a function constantly beyond
the endpoints of $J$. Composition $C(J)\to C[0,1]$ is an isometry since
$\tau$ maps onto $J$. Compactness of $A$ would make $B_{C(J)}$ compact,
contradicting infinite dimensionality. Thus no nonconstant $\tau$ works.

#### Solution VI.3.14 — Compact matrices on c0

The condition is
$$\lim_{N\to\infty}\sup_{m>N}\sum_n|\alpha_{mn}|=0.$$
Let $P_N$ truncate the output to its first $N$ coordinates. The matrix
norm formula gives $\|(I-P_N)A\|=\sup_{m>N}\sum_n|\alpha_{mn}|$.
If it tends to zero, $P_NA$ are finite-rank norm approximants.
If $A$ is compact, $P_N\to I$ pointwise and $\|P_N\|\leq1$; convergence
is uniform on $\overline{A(B)}$ by a finite-net argument. Hence the same
norm tends to zero, proving necessity.

#### Solution VI.3.15 — Compact matrices on ell-1

The condition is
$$\lim_{N\to\infty}\sup_n\sum_{m>N}|\alpha_{mn}|=0.$$
Indeed the expression equals $\|(I-P_N)A\|$ by VI.1.8. Compactness gives
uniform convergence of $P_N$ on the compact image closure, and the
converse follows from the finite-rank approximation $P_NA\to A$.
The given column norm bound is already part of boundedness of $A$.

#### Solution VI.3.16 — Uniform equicontinuity

Uniform equicontinuity implies the pointwise definition immediately.
Conversely for each $x$ choose $r_x>0$ so that
$|f(z)-f(x)|<\varepsilon/2$ whenever $d(z,x)<2r_x$, for every $f$.
Select a finite subcover from the balls $B(x,r_x)$ and let
$\delta$ be the minimum of their radii. If $d(y,z)<\delta$, choose a
selected ball containing $y$; both $y,z$ are in its doubled ball, and
the triangle inequality gives $|f(y)-f(z)|<\varepsilon$ uniformly in $f$.

#### Solution VI.3.17 — Arzelà–Ascoli at infinity

A finite uniform $\varepsilon$-net in $\mathcal F$ gives boundedness,
equicontinuity by controlling its finitely many continuous centers, and
uniform vanishing at infinity by taking the union of their finitely many
compact level sets. Thus total boundedness implies (a)–(c).
Conversely extend each function by zero to the one-point compactification
$X_\infty$. Condition (c) is precisely equicontinuity at infinity; (b)
gives equicontinuity elsewhere, and (a) gives a common bound.
Arzelà–Ascoli on compact $X_\infty$ makes the extended family relatively
compact in the supremum norm. Restriction is isometric, so $\mathcal F$
is totally bounded. If $X$ is already compact, the ordinary theorem applies.

#### Solution VI.3.18 — Finite-rank approximation on C0

The compact image closure $K=\overline{A(B)}$ satisfies VI.3.17.
For $\varepsilon>0$, choose a compact set outside which every $g\in K$
has modulus below $\varepsilon$. Cover it by finitely many relatively
compact open sets $U_j$ with $|g(x)-g(x_j)|<\varepsilon$ on $U_j$ for
all $g\in K$. Add the outside open set on which all $g$ are small.
A partition of unity on $X_\infty$ subordinate to this finite cover gives
compactly supported $\phi_j$ for the $U_j$; use zero as the sample value
on the outside set. Define $Pg=\sum_jg(x_j)\phi_j$.
Then $P$ has finite rank, $\|P\|\leq1$, and
$\sup_{g\in K}\|Pg-g\|\leq\varepsilon$. Thus $PA$ is a finite-rank
approximant to $A$. Choose $\varepsilon=1/n$ for the desired sequence.

#### Solution VI.3.19 — Strong approximation becomes uniform on compact sets

Put $C=\sup_i\|F_i\|$. Given a finite $\delta$-net $y_1,\ldots,y_m$ for
$\overline{A(B)}$, choose one index after which
$\|F_iy_j-y_j\|<\varepsilon/2$ for all $j$. For $y$ within $\delta$ of
$y_j$, the error is at most $(C+1)\delta+\varepsilon/2$.
Taking $\delta<\varepsilon/[2(C+1)]$ gives $\|F_iA-A\|<\varepsilon$.
For each $n$, choose an index with this norm below $1/n$ and call the
corresponding finite-rank product $A_n$. No countable cofinal subnet is
required to make these choices.

#### Solution VI.3.20 — Finite-rank approximation on Lp, including Linfinity

For $p<\infty$, use finite disjoint measurable sets $E_j$ of positive
finite measure and the contraction
$$Ff=\sum_j\left(\frac1{\mu(E_j)}\int_{E_j}f\,d\mu\right)\chi_{E_j}.$$
Hölder proves $\|F\|\leq1$. Order these finite partitions by refinement
and increasing finite-measure support. Simple functions of finite-measure
support are dense in $L^p$, so this net tends strongly to the identity.
VI.3.19 applies.
For $p=\infty$, finite-measure support is insufficient. Instead use all
finite measurable partitions, including infinite-measure cells. On each
non-null cell choose a norm-one functional $\ell_j$ on $L^\infty(E_j)$
with $\ell_j(1)=1$, by Hahn–Banach from the constants. The operator
$Ff=\sum_j\ell_j(f|_{E_j})\chi_{E_j}$ is a finite-rank contraction fixing
all functions constant on the cells. A finite family of bounded functions
can simultaneously be uniformly approximated by such step functions,
by partitioning their scalar ranges into small cells. Direct the partitions
by refinement; irrespective of the chosen $\ell_j$, the resulting
contractions converge strongly to the identity. VI.3.19 again proves the
claim. Null cells are discarded.

#### Solution VI.3.21 — Partitions of unity on a compact space

(a) The range of $T_\alpha$ is in the span of its finitely many $\phi_j$.
(b) Positivity of the partition and $\sum\phi_j=1$ give
$\|T_\alpha f\|\leq\|f\|$, and $T_\alpha1=1$ gives norm one for nonempty
$X$. (c) Two covers have a common finite refinement by intersections.
Add, for every point in either sampling set, a refining open neighborhood
containing that point, with it as sample. This retains both sampling sets
and gives a common upper bound. Finite indexed covers, allowing repetitions,
make the indexing convention unambiguous. The relation is a directed
preorder, which is sufficient to define a net; one may quotient equivalent
indices if a partial order is desired.
(d) Cover $X$ by open sets on which $f$ oscillates by less than
$\varepsilon$. For every refinement and its samples, if $\phi_j(x)>0$,
then $x,x_j$ belong to one such set. Thus
$|T_\alpha f(x)-f(x)|\leq\sum_j\phi_j(x)|f(x_j)-f(x)|<\varepsilon$.
VI.3.19 proves the finite-rank approximation theorem.

### §4. Invariant subspaces

#### Solution VI.4.1 — The graph of an intertwiner

The graph is a closed linear subspace since $T$ is bounded. For every $x$,
$(A\oplus B)(x,Tx)=(Ax,BTx)=(Ax,TAx)$ by $TA=BT$.
The latter is again in the graph, proving invariance.

#### Solution VI.4.2 — Annihilators reverse invariance and order

If $TM\subset M$, $f\in M^\perp$, and $m\in M$, then
$(T^*f)(m)=f(Tm)=0$, so $T^*M^\perp\subset M^\perp$.
Conversely that property gives $f(Tm)=0$ for every $f\in M^\perp$;
Hahn–Banach and closedness give $Tm\in{}^\perp(M^\perp)=M$.
The map reverses inclusion and satisfies
$$(\overline{\operatorname{span}}\bigcup_iM_i)^\perp=\bigcap_iM_i^\perp,
\qquad (\bigcap_iM_i)^\perp=
\overline{\operatorname{span}\bigcup_iM_i^\perp}^{\mathrm{wk}^*}.$$
The second formula follows by taking preannihilators and using the bipolar
identity for subspaces. Its closure is weak-star closure; a norm-closed
join in the full lattice of $X^*$ need not suffice. Thus this is a lattice
anti-isomorphism onto the weak-star closed invariant subspaces, with joins
in that lattice interpreted accordingly.

#### Solution VI.4.3 — Three-dimensional diagonal operators

(a) For distinct eigenvalues the Lagrange polynomial
$p_j(t)=\prod_{i\ne j}(t-\alpha_i)/(\alpha_j-\alpha_i)$ gives the coordinate
projection $p_j(T)$. Every invariant subspace is invariant under polynomials
in $T$, hence contains each nonzero coordinate component of each of its
vectors. It is therefore spanned by a subset of the basis. The converse
is immediate from diagonality.
(b) If $\alpha_1=\alpha_2=a\ne b=\alpha_3$, the polynomials
$(b-t)/(b-a)$ and $(t-a)/(b-a)$ give the two eigenspace projections.
Thus $M=(M\cap\operatorname{span}\{e_1,e_2\})\oplus(M\cap\mathbb Fe_3)$.
Every such sum is invariant because $T$ is scalar on each summand.

#### Solution VI.4.4 — Arbitrary finite diagonal operators

For each distinct eigenvalue $\lambda$, let
$E_\lambda=\operatorname{span}\{e_j:\alpha_j=\lambda\}$.
Then all invariant subspaces are precisely
$M=\bigoplus_\lambda M_\lambda$, where each $M_\lambda$ is any subspace
of $E_\lambda$. Interpolating on the distinct eigenvalues gives polynomial
spectral projections onto $E_\lambda$, so invariance forces this
decomposition. Scalar action on each eigenspace proves the converse.

#### Solution VI.4.5 — A single weighted nilpotent chain

The lattice is $\{0\}$ together with the tails
$\operatorname{span}\{e_k,\ldots,e_d\}$ for $1\leq k\leq d$.
To prove exhaustiveness, choose in a nonzero invariant $M$ a vector whose
first nonzero coordinate has the smallest possible index $k$.
Its vectors $v,Tv,\ldots,T^{d-k}v$ have successive leading coordinates
$k,k+1,\ldots,d$, each nonzero because the weights are nonzero.
They form a triangular basis of the entire tail space, so that tail is
contained in $M$. Minimality of $k$ gives the reverse containment.
Each tail is visibly invariant.

#### Solution VI.4.6 — Real operators have a small invariant subspace

The complexification of $T$ has an eigenvalue $\lambda$ and eigenvector
$u+iv$. If $\lambda$ is real, at least one of $u,v$ is a nonzero real
eigenvector. If $\lambda=a+ib$ with $b\ne0$, then
$Tu=au-bv$ and $Tv=bu+av$. The real span of $u,v$ is invariant and has
dimension two (linear dependence would produce a real eigenvector with
nonreal eigenvalue). Thus there is an invariant subspace of dimension
one or two, nonzero and proper when $d\geq3$.

#### Solution VI.4.7 — Nonseparability gives an invariant subspace

For $0\ne x\in X$, let $M=\overline{\operatorname{span}}\{T^nx:n\geq0\}$.
It is nonzero, separable, and invariant: $T$ takes the algebraic span into
itself and continuity extends this to the closure. Since $X$ is not
separable, $M\ne X$. Hence $M$ is nontrivial.

#### Solution VI.4.8 — Invariance need not pass to the inverse

On $\ell^2(\mathbb Z)$ take the bilateral shift $Te_n=e_{n+1}$ and
$M=\overline{\operatorname{span}}\{e_n:n\geq0\}$. The shift is an invertible
isometry and $TM\subset M$. But $T^{-1}e_0=e_{-1}\notin M$.
This is a proper inclusion $TM\subsetneq M$, which is why invertibility
on the ambient space is insufficient.

#### Solution VI.4.9 — Maximal invariant chains of a compact operator

A maximal chain $\mathcal C$ contains 0 and $X$ and is closed under
intersections and closed spans of subchains: those subspaces are invariant
and comparable with the whole chain, so maximality includes them.
Suppose a closed subspace $L$ could be inserted into the chain. Put
$M=\overline{\operatorname{span}}\{C\in\mathcal C:C\subseteq L\}$ and
$N=\bigcap\{C\in\mathcal C:L\subseteq C\}$. Then $M,N\in\mathcal C$ and
$M\subseteq L\subseteq N$, with no chain member strictly between $M,N$.
If $\dim(N/M)>1$, the operator induced by $K$ on $N/M$ is compact:
quotient unit vectors have uniformly bounded representatives, and the
quotient of a relatively compact image is relatively compact.
In finite dimension over $\mathbb C$ it has a nontrivial invariant subspace
by an eigenvector; in infinite dimension use Corollary 4.14 (and for the
zero operator choose any line). Its inverse image inserts a new invariant
subspace between $M,N$, a contradiction. Thus $\dim(N/M)\leq1$, leaving
no intermediate $L$ other than an endpoint. The chain is maximal among
all closed subspaces.

### §5. Weakly compact operators

#### Solution VI.5.1 — Reflexivity and compositions

(a) If $X$ is reflexive, the weakly continuous image $T(B_X)$ of its
weakly compact ball is compact. If $Y$ is reflexive, the norm closure of
$T(B_X)$ is a closed convex subset of $\|T\|B_Y$, hence weakly closed
and weakly compact. (b) For weakly compact $T$, let
$K=\overline{T(B_X)}$. Weak continuity makes $A(K)$ weakly compact and
it contains $AT(B_X)$; the norm closure of that convex set is weakly
closed, so compact. (c) $TB(B_Z)$ lies in $\|B\|T(B_X)$, giving the
same conclusion. The zero operator cases are immediate.

#### Solution VI.5.2 — The adjoint of an isometric embedding

For $r^*\in R^*$, define $\ell(\Phi r)=r^*(r)$ on the subspace $\Phi(R)$.
Because $\Phi$ is an isometry, this is well defined and has norm
$\|r^*\|$. Hahn–Banach extends it to $x^*\in X^*$ with the same norm.
Then $(\Phi^*x^*)(r)=x^*(\Phi r)=r^*(r)$ for every $r$, proving
surjectivity. Completeness is not needed for this extension argument.

#### Solution VI.5.3 — Weakly compact operators on c0

(a) From any bounded sequence in $c_0$, take diagonal subsequences so that
each coordinate converges. Uniform boundedness of the sup norms and the
summable tails of any test in $\ell^1$ show that all dual pairings converge;
the subsequence is weakly Cauchy. The partial sums
$e_1+\cdots+e_n$ are weakly Cauchy, but a weak limit would have every
coordinate equal to one and thus would not belong to $c_0$.
(b) By Theorem 5.4 a weakly compact $T:c_0\to c_0$ factors as $AB$ through
a reflexive space $R$. VI.3.9 says $B:c_0\to R$ is compact. Composition
with bounded $A$ makes $T$ compact.

#### Solution VI.5.4 — Weakly compact generation

If $T:R\to X$ is bounded with $R$ reflexive and dense range, then
$K=T(B_R)$ is weakly compact, and its closed linear span contains
$T(R)$, so equals $X$. Injectivity is not needed in this direction.
Conversely let weakly compact $K$ generate $X$. The set
$K'=\{\alpha k:k\in K,\ |\alpha|=1\}\cup\{0\}$ is weakly compact as
a continuous image of a compact product. Its closed convex hull $W$ is
weakly compact by V.13.4, bounded, convex, and balanced. Apply Lemma 5.3
to $W\subset X$. It gives a reflexive Banach space $R$ consisting of
vectors in $X$, with a bounded injective inclusion $T:R\to X$, and
$W\subset R$. Thus its range contains $K$ and has dense linear span;
since the range is itself linear, it is dense in $X$.

#### Solution VI.5.5 — A bounded kernel on a finite measure space

The kernel defines a bounded map $B:L^1\to L^2$, since
$|Bf(x)|\leq\|k\|_\infty\|f\|_1$ and $\mu(X)<\infty$.
The inclusion $J:L^2\to L^1$ is bounded by Cauchy–Schwarz, and $K=JB$.
It therefore factors through reflexive $L^2$, proving weak compactness.
The map $BJ:L^2\to L^2$ is compact by VI.3.6: its kernel rows have
$L^2$ norm at most $\|k\|_\infty\mu(X)^{1/2}$.
Consequently $K^2=J(BJ)B$ is compact. All assertions are unaffected by
changing the essentially bounded kernel on a product null set, using
Fubini on this finite measure space.

#### Solution VI.5.6 — Operators into weakly sequentially complete spaces

(a) Write $y_n=T^{**}x_n^{**}\in Y$. For $y^*\in Y^*$,
$y^*(y_n)=x_n^{**}(T^*y^*)\to x^{**}(T^*y^*)$.
Thus $y_n$ is weakly Cauchy and has a weak limit $y\in Y$ by the stated
completeness. Equality of all evaluations gives $T^{**}x^{**}=J_Yy$.

(b) A compact $G_\delta$ subset $K$ of compact Hausdorff $X$ is a zero set
of a continuous nonnegative function. Indeed write $K=\bigcap U_n$,
choose continuous $0\leq h_n\leq1$ equal to zero on $K$ and one off $U_n$,
and use $h=\sum2^{-n}h_n$. The functions
$\max(0,1-nh)$ decrease pointwise to $\chi_K$. Their integrals converge
against every finite measure by dominated convergence, so this is a
weak-star convergent sequence in $C(X)^{**}$. Part (a) implies
$T^{**}\chi_K\in Y$. Finite unions of compact $G_\delta$ sets have the
same property. Increasing unions then give $\chi_F$ for the sets in
$\mathcal F$, again by dominated convergence and (a). Linearity proves
the assertion for $\mathcal L$.

(c) We give the additional limit argument needed to apply James's theorem.
Let $\mathcal D$ be the bounded Baire functions obtained from continuous
functions by successive bounded pointwise sequential limits. Every such
function defines an element of $C(X)^{**}$ by integration against measures.
Dominated convergence and (a) imply $T^{**}g\in Y$ for $g\in\mathcal D$;
the assertion is preserved at every successive limit stage.
Fix $y^*\in Y^*$ and let $\mu=T^*y^*$. Choose $f_n\in B_{C(X)}$ with
$\operatorname{Re}\int f_n\,d\mu\to\|\mu\|$. With
$d\mu=h\,d|\mu|$, $|h|=1$, the inequality
$|f_n-\bar h|^2\leq2(1-\operatorname{Re}(f_nh))$ gives convergence to
$\bar h$ in $L^2(|\mu|)$. A subsequence converges $|\mu|$-almost everywhere.
Define $g$ to be its pointwise limit where that limit exists, and zero
elsewhere. This is a bounded Baire function with $|g|\leq1$ and belongs
to the successive-limit class: limsup and liminf of the real and imaginary
parts are obtained by countable suprema and infima, each a limit of finite
maxima/minima; the equality sets are obtained by limits of continuous
scalar cutoffs. These constructions use uniformly bounded functions.
Thus $T^{**}g\in Y$ and
$\operatorname{Re}y^*(T^{**}g)=\|T^*y^*\|$.

Put $C=\overline{T(B_{C(X)})}$ in norm. Goldstine's theorem and weak-star
continuity of $T^{**}$ put $T^{**}g$ in the weak-star closure of $T(B)$.
Since it lies in $Y$, it belongs to the weak closure there, which equals
$C$ by convexity and Hahn–Banach separation. Every real continuous linear
functional on $Y$ is the real part of a complex one when needed, so each
attains its supremum on $C$ by this construction. James's theorem V.13.3
makes the closed bounded convex set $C$ weakly compact. This is precisely
weak compactness of $T$.
<!-- END SOLUTIONS VI -->
