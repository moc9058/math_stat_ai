# X. Unbounded Operators


<a id="pdf-page-318"></a>
# CHAPTER X

# Unbounded Operators

It is unfortunate for the world we live in that all of the operators that arise naturally are not bounded. But that is indeed the case. Thus it is important to study such operators.

The idea here is not to study an arbitrary linear transformation on a Hilbert space. In fact, such a study is the province of linear algebra rather than analysis. The operators that are to be studied do possess certain properties that connect them to the underlying Hilbert space. The properties that will be isolated are inspired by natural examples.

All Hilbert spaces in this chapter are assumed separable.

## §1. Basic Properties and Examples

<!-- BEGIN BACKGROUND BG-X.block1 -->
<a id="bg-x-1"></a>
### Definition BG-X.1 — Equality of operators and the graph norm

An unbounded operator includes its domain as part of its data. Thus $A=B$ means both $\operatorname{dom}A=\operatorname{dom}B$ and equal values there. On $\operatorname{dom}A$, its **graph norm** is $\|h\|_A=(\|h\|^2+\|Ah\|^2)^{1/2}$. A subspace $D_0\subset\operatorname{dom}A$ is a **core** if it is dense for this norm; density in the ambient Hilbert-space norm is not sufficient.

<a id="bg-x-2"></a>
### Lemma BG-X.2 — Closedness is completeness in the graph norm

An operator $A$ is closed if and only if its domain is complete in $\|\cdot\|_A$. If $A$ is closed, $D_0$ is a core exactly when the closure of $A|_{D_0}$ equals $A$.

**Proof.** The map $h\mapsto(h,Ah)$ is an isometry of the graph-norm domain onto the graph in $\mathcal H\oplus\mathcal K$. A linear subspace of a Hilbert space is complete exactly when it is closed: completeness puts limits of its Cauchy sequences inside it; closedness retains ambient limits. The assertion about a core is the same statement about the closure of the restricted graph. $\square$

<a id="bg-x-3"></a>
### Definition BG-X.3 — Absolute continuity and the integral form of calculus

A function $f:[a,b]\to\mathbb C$ is **absolutely continuous** if for every $\varepsilon>0$ there is $\delta>0$ such that $\sum_j|f(b_j)-f(a_j)|<\varepsilon$ whenever the intervals $(a_j,b_j)$ are disjoint and have total length less than $\delta$. The real-analysis fundamental theorem for absolutely continuous functions says equivalently that
$$
f(x)=f(a)+\int_a^x v(t)\,dt\quad(v\in L^1[a,b]),
$$
and then $f'=v$ almost everywhere. This is the Lebesgue, not merely the continuously differentiable, form of the fundamental theorem. A useful explanation of its hypotheses is that integrals of $L^1$ functions have absolutely continuous integrals (truncate $|v|$ at a large constant), while differentiation of these integrals holds at the Lebesgue points of $v$. The general equivalence is a real-analysis prerequisite being recalled here; it is not being inferred from pointwise differentiability alone.

<a id="bg-x-4"></a>
### Lemma BG-X.4 — The estimates used for differential-operator domains

If $f$ is absolutely continuous and $f'\in L^2[a,b]$, then
$$
|f(y)-f(x)|\leq\sqrt{|y-x|}\,\|f'\|_{L^2[a,b]}.
$$
If $f,g$ are absolutely continuous on $[a,b]$, then
$$
\int_a^bf'\bar g=[f\bar g]_a^b-\int_a^bf\overline{g'}.
$$

**Proof.** Apply Cauchy–Schwarz to $\int_x^yf'$. For the second assertion, products of bounded absolutely continuous functions are absolutely continuous: expand each increment of $f\bar g$ and bound by $\|f\|_\infty|\Delta g|+\|g\|_\infty|\Delta f|$. The ordinary product rule holds wherever both derivatives exist. Apply the integral fundamental theorem to the product. $\square$

Boundary values in this chapter refer to the absolutely continuous representative of an $L^2$ class. They are not values of an arbitrary representative. The boundary term explains why the same formula $if'$ has different adjoints for different domains.
<!-- END BACKGROUND BG-X.block1 -->

The first relaxation in the concept of operator is not to assume that the operators are defined everywhere on the Hilbert space.

**1.1. Definition.** If $\mathcal H,\mathcal K$ are Hilbert spaces, a *linear operator* $A:\mathcal H\to\mathcal K$ is a function whose domain of definition is a linear manifold, $\operatorname{dom}A$, in $\mathcal H$ and such that $A(\alpha f+\beta g)=\alpha Af+\beta Ag$ for $f,g$ in $\operatorname{dom}A$ and $\alpha,\beta$ in $\mathbb C$. $A$ is *bounded* if there is a constant $c>0$ such that $\|Af\|\leq c\|f\|$ for all $f$ in $\operatorname{dom}A$.

Note that if $A$ is bounded, then $A$ can be extended to a bounded linear operator on $\operatorname{cl}[\operatorname{dom}A]$ and then extended to $\mathcal H$ by letting $A$ be $0$ on $(\operatorname{dom}A)^\perp$. So unless it is specified to the contrary, a bounded operator will always be assumed to be defined on all of $\mathcal H$.

If $A$ is a linear operator from $\mathcal H$ into $\mathcal K$, then $A$ is also a linear operator



<a id="pdf-page-319"></a>
from $\operatorname{cl}[\operatorname{dom}A]$ into $\mathcal K$. So we will often only consider those $A$ such that $\operatorname{dom}A$ is dense in $\mathcal H$; such an operator $A$ is said to be *densely defined*. $\mathcal B(\mathcal H)$ still denotes the bounded operators defined on $\mathcal H$.

If $A,B$ are linear operators from $\mathcal H$ into $\mathcal K$, then $A+B$ is defined with $\operatorname{dom}(A+B)=\operatorname{dom}A\cap\operatorname{dom}B$. If $B:\mathcal H\to\mathcal K$ and $A:\mathcal K\to\mathcal L$, then $AB$ is a linear operator from $\mathcal H$ into $\mathcal L$ with $\operatorname{dom}(AB)=B^{-1}(\operatorname{dom}A)$.

**1.2. Definition.** If $A,B$ are operators from $\mathcal H$ into $\mathcal K$, then $A$ is an *extension* of $B$ if $\operatorname{dom}B\subseteq\operatorname{dom}A$ and $Ah=Bh$ whenever $h\in\operatorname{dom}B$. In symbols this is denoted by $B\subseteq A$.

Note that if $A\in\mathcal B(\mathcal H)$, then the only extension of $A$ is itself. So this concept is only of value for unbounded operators.

If $A:\mathcal H\to\mathcal K$, the *graph* of $A$ is the set

$$
\operatorname{gra}A\equiv\{h\oplus Ah\in\mathcal H\oplus\mathcal K:h\in\operatorname{dom}A\}.
$$

It is easy to see that $B\subseteq A$ if and only if $\operatorname{gra}B\subseteq\operatorname{gra}A$.

**1.3. Definition.** An operator $A:\mathcal H\to\mathcal K$ is *closed* if its graph is closed in $\mathcal H\oplus\mathcal K$. An operator is *closable* if it has a closed extension. Let $\mathcal C(\mathcal H,\mathcal K)=$ the collection of all closed densely defined operators from $\mathcal H$ into $\mathcal K$. Let $\mathcal C(\mathcal H)=\mathcal C(\mathcal H,\mathcal H)$. (It should be emphasized that the operators in $\mathcal C(\mathcal H,\mathcal K)$ are densely defined.)

When is a subset of $\mathcal H\oplus\mathcal K$ a graph of an operator from $\mathcal H$ into $\mathcal K$? If $\mathcal G=\operatorname{gra}A$ for some $A:\mathcal H\to\mathcal K$, then $\mathcal G$ is a submanifold of $\mathcal H\oplus\mathcal K$ such that if $k\in\mathcal K$ and $0\oplus k\in\mathcal G$, then $k=0$. The converse is also true. That is, suppose that $\mathcal G$ is a submanifold of $\mathcal H\oplus\mathcal K$ such that if $k\in\mathcal K$ and $0\oplus k\in\mathcal G$, then $k=0$. Let $\mathcal D=\{h\in\mathcal H:\text{ there exists a }k\text{ in }\mathcal K\text{ with }h\oplus k\text{ in }\mathcal G\}$. If $h\in\mathcal D$ and $k_1,k_2\in\mathcal K$ such that $h\oplus k_1,h\oplus k_2\in\mathcal G$, then $0\oplus(k_1-k_2)=h\oplus k_1-h\oplus k_2\in\mathcal G$. Hence $k_1=k_2$. That is, for every $h$ in $\mathcal D$ there is a unique $k$ in $\mathcal K$ such that $h\oplus k\in\mathcal G$; denote $k$ by $k=Ah$. It is easy to check that $A$ is a linear map and $\mathcal G=\operatorname{gra}A$. This gives an internal characterization of graphs that will be useful in the next proposition.

**1.4. Proposition.** *An operator $A:\mathcal H\to\mathcal K$ is closable if and only if $\operatorname{cl}[\operatorname{gra}A]$ is a graph.*

**Proof.** Let $\operatorname{cl}[\operatorname{gra}A]$ be a graph. That is, there is an operator $B:\mathcal H\to\mathcal K$ such that $\operatorname{gra}B=\operatorname{cl}[\operatorname{gra}A]$. Clearly $\operatorname{gra}A\subseteq\operatorname{gra}B$, so $A$ is closable.

Now assume that $A$ is closable; that is, there is a closed operator $B:\mathcal H\to\mathcal K$ with $A\subseteq B$. If $0\oplus k\in\operatorname{cl}[\operatorname{gra}A]$, $0\oplus k\in\operatorname{gra}B$ and hence $k=0$. By the remarks preceding this proposition, $\operatorname{cl}[\operatorname{gra}A]$ is a graph. $\blacksquare$

If $A$ is closable, call the operator whose graph is $\operatorname{cl}[\operatorname{gra}A]$ the *closure* of $A$.

**1.5. Definition.** If $A:\mathcal H\to\mathcal K$ is densely defined, let



<a id="pdf-page-320"></a>
$$
\operatorname{dom}A^*=\{k\in\mathcal K:h\mapsto\langle Ah,k\rangle\text{ is a bounded linear functional on }\operatorname{dom}A\}.
$$

Because $\operatorname{dom}A$ is dense in $\mathcal H$, if $k\in\operatorname{dom}A^*$, then there is a unique vector $f$ in $\mathcal H$ such that $\langle Ah,k\rangle=\langle h,f\rangle$ for all $h$ in $\operatorname{dom}A$. Denote this unique vector $f$ by $f=A^*k$. Thus

$$
\langle Ah,k\rangle=\langle h,A^*k\rangle
$$

for $h$ in $\operatorname{dom}A$ and $k$ in $\operatorname{dom}A^*$.

**1.6. Proposition.** If $A:\mathcal H\to\mathcal K$ is a densely defined operator, then:

(a) $A^*$ is a closed operator;  
(b) $A^*$ is densely defined if and only if $A$ is closable;  
(c) if $A$ is closable, then its closure is $(A^*)^*\equiv A^{**}$.

Before proving this, a lemma is needed which will also be useful later.

**1.7. Lemma.** If $A:\mathcal H\to\mathcal K$ is densely defined and $J:\mathcal H\oplus\mathcal K\to\mathcal K\oplus\mathcal H$ is defined by $J(h\oplus k)=(-k)\oplus h$, then $J$ is an isomorphism and

$$
\operatorname{gra}A^*=[J\operatorname{gra}A]^\perp.
$$

**Proof.** It is clear that $J$ is an isomorphism. To prove the formula for $\operatorname{gra}A^*$, note that $\operatorname{gra}A^*=\{k\oplus A^*k\in\mathcal K\oplus\mathcal H:k\in\operatorname{dom}A^*\}$. So if $k\in\operatorname{dom}A^*$ and $h\in\operatorname{dom}A$,

$$
\begin{aligned}
\langle k\oplus A^*k,J(h\oplus Ah)\rangle
&=\langle k\oplus A^*k,-Ah\oplus h\rangle\\
&=-\langle k,Ah\rangle+\langle A^*k,h\rangle=0.
\end{aligned}
$$

Thus $\operatorname{gra}A^*\subseteq[J\operatorname{gra}A]^\perp$. Conversely, if $k\oplus f\in[J\operatorname{gra}A]^\perp$, then for every $h$ in $\operatorname{dom}A$, $0=\langle k\oplus f,-Ah\oplus h\rangle=-\langle k,Ah\rangle+\langle f,h\rangle$, so $\langle Ah,k\rangle=\langle h,f\rangle$. By definition $k\in\operatorname{dom}A^*$ and $A^*k=f$. $\blacksquare$

**Proof of Proposition 1.6.** The proof of (a) is clear from Lemma 1.7. For the remainder of the proof notice that because the map $J$ in (1.7) is an isomorphism, $J^*=J^{-1}$ and so $J^*(k\oplus h)=h\oplus(-k)$.

(b) Assume $A$ is closable and let $k_0\in(\operatorname{dom}A^*)^\perp$. We want to show that $k_0=0$. Thus $k_0\oplus0\in[\operatorname{gra}A^*]^\perp=[J\operatorname{gra}A]^{\perp\perp}=\operatorname{cl}[J\operatorname{gra}A]=J[\operatorname{cl}(\operatorname{gra}A)]$. So $0\oplus-k_0=J^*(k_0\oplus0)\in J^*J[(\operatorname{gra}A)]=\operatorname{cl}(\operatorname{gra}A)$. But because $A$ is closable, $\operatorname{cl}(\operatorname{gra}A)$ is a graph; hence $k_0=0$. For the converse, assume $\operatorname{dom}A^*$ is dense in $\mathcal K$. Thus $A^{**}\equiv(A^*)^*$ is defined. By (a), $A^{**}$ is a closed operator. It is easy to see that $A\subseteq A^{**}$, so $A$ has a closed extension.

(c) Note that by Lemma 1.7 $\operatorname{gra}A^{**}=[J^*\operatorname{gra}A^*]^\perp=[J^*[J\operatorname{gra}A]^\perp]^\perp$. But for any linear manifold $\mathcal M$ and any isomorphism $J$, $(J\mathcal M)^\perp=J(\mathcal M^\perp)$. Hence $J^*[(J\mathcal M)^\perp]=\mathcal M^\perp$ and, thus, $[J^*[J\mathcal M]^\perp]^\perp=\mathcal M^{\perp\perp}=\operatorname{cl}\mathcal M$. Putting $\mathcal M=\operatorname{gra}A$ gives that $\operatorname{gra}A^{**}=\operatorname{cl}\operatorname{gra}A$. $\blacksquare$

**1.8. Corollary.** If $A\in\mathcal C(\mathcal H,\mathcal K)$, then $A^*\in\mathcal C(\mathcal K,\mathcal H)$ and $A^{**}=A$.



<a id="pdf-page-321"></a>
**1.9. Example.** Let $e_0,e_1,\ldots$ be an orthonormal basis for $\mathcal H$ and let $\alpha_0,\alpha_1,\ldots$ be complex numbers. Define $\mathcal D=\{h\in\mathcal H:\sum_0^\infty|\alpha_n\langle h,e_n\rangle|^2<\infty\}$ and let $Ah=\sum_0^\infty\alpha_n\langle h,e_n\rangle e_n$ for $h$ in $\mathcal D$. Then $A\in\mathcal C(\mathcal H)$ with $\operatorname{dom}A=\mathcal D$. Also, $\operatorname{dom}A^*=\mathcal D$ and $A^*h=\sum_0^\infty\bar\alpha_n\langle h,e_n\rangle e_n$ for all $h$ in $\mathcal D$.

**1.10. Example.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $\phi:X\to\mathbb C$ be an $\Omega$-measurable function. Let $\mathcal D=\{f\in L^2(\mu):\phi f\in L^2(\mu)\}$ and define $Af=\phi f$ for all $f$ in $\mathcal D$. Then $A\in\mathcal C(L^2(\mu))$, $\operatorname{dom}A^*=\mathcal D$, and $A^*f=\bar\phi f$ for $f$ in $\mathcal D$.

**1.11. Example.** Let $\mathcal D=$ all functions $f:[0,1]\to\mathbb C$ that are absolutely continuous with $f'\in L^2(0,1)$ and such that $f(0)=f(1)=0$. $\mathcal D$ includes all polynomials $p$ with $p(0)=p(1)=0$. So the uniform closure of $\mathcal D$ is $\{f\in C[0,1]:f(0)=f(1)=0\}$. Thus $\mathcal D$ is dense in $L^2(0,1)$. Define $A:L^2(0,1)\to L^2(0,1)$ by $Af=if'$ for $f$ in $\mathcal D$. To see that $A$ is closed, suppose $\{f_n\}\subseteq\mathcal D$ and $f_n\oplus if_n'\to f\oplus g$ in $L^2\oplus L^2$. Let $h(x)=-i\int_0^x g(t)\,dt$; so $h$ is absolutely continuous. Now using the Cauchy-Schwarz inequality we get that $|f_n(x)-h(x)|=|\int_0^x[f_n'(t)+ig(t)]\,dt|\leq\|f_n'+ig\|_2=\|if_n'-g\|_2$. Thus $f_n(x)\to h(x)$ uniformly on $[0,1]$. Since $f_n\to f$ in $L^2(0,1)$, $f(x)=h(x)$ a.e. So we may assume that $f(x)=-i\int_0^x g(t)\,dt$ for all $x$. Therefore $f$ is absolutely continuous and $f_n(x)\to f(x)$ uniformly on $[0,1]$; thus $f(0)=f(1)=0$ and $f'=-ig\in L^2(0,1)$. So $f\in\mathcal D$ and $f\oplus g=f\oplus g=f\oplus if'\in\operatorname{gra}A$; that is, $A\in\mathcal C(L^2(0,1))$.

Note that $\{f':f\in\mathcal D\}=\{h\in L^2(0,1):\int_0^1h(x)\,dx=0\}=[1]^\perp$.

**Claim.** $\operatorname{dom}A^*=\{g:g\text{ is absolutely continuous on }[0,1],\ g'\in L^2(0,1)\}$ and for $g$ in $\operatorname{dom}A^*$, $A^*g=ig'$.

In fact, suppose $g\in\operatorname{dom}A^*$ and let $h=A^*g$. Put $H(x)=\int_0^x h(t)\,dt$. Using integration by parts, for every $f$ in $\mathcal D$, $i\int_0^1 f'\bar g=\langle Af,g\rangle=\langle f,h\rangle=\int_0^1 f\bar h=\int_0^1 f(x)\,d\bar H(x)=-\int_0^1 f'(x)\bar H(x)\,dx$; that is, $\langle f',-ig\rangle=\langle f',-H\rangle$ for all $f$ in $\mathcal D$. Thus $H-ig\in\{f':f\in\mathcal D\}^\perp=[1]^{\perp\perp}$; hence $H-ig=c$, a constant function. Thus $g=ic-iH$ so that $g$ is absolutely continuous and $g'=-ih\in L^2$. Also note that $A^*g=h=ig'$. The proof of the other inclusion is left to the reader.

**1.12. Example.** Let $\mathcal E=\{f\in L^2(0,1):f\text{ is absolutely continuous},\ f'\in L^2,\text{ and }f(0)=f(1)\}$. Define $Bf=if'$ for $f$ in $\mathcal E$. As in (1.11), $B\in\mathcal C(L^2(0,1))$ and $\operatorname{ran}B=[1]^\perp$.

**Claim.** $\operatorname{dom}B^*=\mathcal E$ and $B^*g=ig'$ for $g$ in $\mathcal E$.

Let $g\in\operatorname{dom}B^*$. Put $h=B^*g$ and $H(x)=\int_0^x h(t)\,dt$. As in (1.11), $H(0)=H(1)=0$ and for every $f$ in $\mathcal E$, $i\int_0^1 f'\bar g=-\int_0^1 f'\bar H$. Hence $0=\int_0^1(if'\bar g+f'\bar H)=\int_0^1 if'\overline{(g+iH)}$. Thus $g+iH\perp\operatorname{ran}B$ and so $g+iH=c$, a constant function. Thus $g=c-iH$ is absolutely continuous, $g'=-ih\in L^2$, and $g(0)=g(1)=c$. Thus $g\in\mathcal E$ and $B^*g=h=ig'$. The proof of the other inclusion is left to the reader.



<a id="pdf-page-322"></a>
The preceding two examples illustrate the fact that the calculation of the adjoint depends on the domain of the operator, not just the formal definition of the operator. Note the fact that the next result generalizes (II.2.19).

**1.13. Proposition.** *If $A:\mathcal H\to\mathcal K$ is densely defined, then*

$$
(\operatorname{ran}A)^\perp=\ker A^*.
$$

*If $A$ is also closed, then*

$$
(\operatorname{ran}A^*)^\perp=\ker A.
$$

**Proof.** If $h\perp\operatorname{ran}A$, then for every $f$ in $\operatorname{dom}A$, $0=\langle Af,h\rangle$. Hence $h\in\operatorname{dom}A^*$ and $A^*h=0$. The other inclusion is clear. By Corollary 1.8, if $A\in\mathcal C(\mathcal H,\mathcal K)$, $A^{**}=A$. So the second equality follows from the first. $\blacksquare$

**1.14. Definition.** If $A:\mathcal H\to\mathcal K$ is a linear operator, $A$ is *boundedly invertible* if there is a bounded linear operator $B:\mathcal K\to\mathcal H$ such that $AB=1$ and $BA\subseteq1$.

Note that if $BA\subseteq1$, then $BA$ is bounded on its domain. Call $B$ a *(bounded) inverse* of $A$.

**1.15. Proposition.** *Let $A:\mathcal H\to\mathcal K$ be a linear operator.*

(a) *$A$ is boundedly invertible if and only if $\ker A=(0)$, $\operatorname{ran}A=\mathcal K$, and the graph of $A$ is closed.*

(b) *If $A$ is boundedly invertible, its inverse is unique and denoted by $A^{-1}$.*

**Proof.** (a) Let $B$ be a bounded inverse of $A$. So $\operatorname{dom}B=\mathcal K$. Since $BA\subseteq1$, $\ker A=(0)$; since $AB=1$, $\operatorname{ran}A=\mathcal K$. Also, $\operatorname{gra}A=\{h\oplus Ah:h\in\operatorname{dom}A\}=\{Bk\oplus k:k\in\mathcal K\}$. Since $B$ is bounded, $\operatorname{gra}A$ is closed. Conversely, if $A$ has the stated properties, $Bk=A^{-1}k$ for $k$ in $\mathcal K$ is a well-defined operator on $\mathcal K$. Because $\operatorname{gra}A$ is closed, $\operatorname{gra}B$ is closed. By the Closed Graph Theorem, $B\in\mathcal B(\mathcal K,\mathcal H)$.

(b) This is an exercise. $\blacksquare$

**1.16. Definition.** If $A:\mathcal H\to\mathcal H$ is a linear operator, $\rho(A)$, the *resolvent set* for $A$, is defined by $\rho(A)=\{\lambda\in\mathbb C:\lambda-A\text{ is boundedly invertible}\}$. The *spectrum* of $A$ is the set $\sigma(A)=\mathbb C\setminus\rho(A)$.

It is easy to see that if $A:\mathcal H\to\mathcal H$ is a linear operator and $\lambda\in\mathbb C$, $\operatorname{gra}A$ is closed if and only if $\operatorname{gra}(A-\lambda)$ is closed. So if $A$ does not have closed graph, $\sigma(A)=\mathbb C$. Even if $A$ has closed graph, it is possible that $\sigma(A)$ is empty (see Exercise 10). The spectrum of an unbounded operator, however, does enjoy some of the properties possessed by the spectrum of an element of a Banach algebra. The proof of the next result is left to the reader.

**1.17. Proposition.** *If $A:\mathcal H\to\mathcal H$ is a linear operator, then $\sigma(A)$ is closed and $z\mapsto(z-A)^{-1}$ is an analytic function on $\rho(A)$.*



<a id="pdf-page-323"></a>
Note that if $A$ is defined as in Example 1.9, then $\sigma(A)=\operatorname{cl}\{\alpha_n\}$. Hence it is possible for $\sigma(A)$ to equal any closed subset of $\mathbb C$.

**1.18. Proposition.** Let $A\in\mathcal C(\mathcal H)$.

(a) $\lambda\in\rho(A)$ if and only if $\ker(A-\lambda)=(0)$ and $\operatorname{ran}(A-\lambda)=\mathcal H$.

(b) $\sigma(A^*)=\{\bar\lambda:\lambda\in\sigma(A)\}$ and for $\lambda$ in $\rho(A)$, $(A-\lambda)^{*-1}=[(A-\lambda)^{-1}]^*$.

**Proof.** Exercise.

## Exercises

1. If $A$, $B$, and $AB$ are densely defined linear operators, show that $(AB)^*\supseteq B^*A^*$.

2. Verify the statements in Example 1.9.

3. Verify the statements in Example 1.10.

4. Define an unbounded weighted shift and determine its adjoint.

5. Verify the statements in Example 1.11.

6. If $\mathcal H$ is infinite dimensional, show that there is a linear operator $A:\mathcal H\to\mathcal H$ such that $\operatorname{gra}A$ is dense in $\mathcal H\oplus\mathcal H$. What does this say about $\operatorname{dom}A^*$? (See Lindsay [1984].)

7. Let $\mathcal D$ be the set of absolutely continuous functions $f$ such that $f'\in L^2(0,1)$. Let $Df=f'$ for $f$ in $\mathcal D$ and let $(Af)(x)=xf(x)$ for $f$ in $L^2(0,1)$. Show that $DA-AD\subseteq 1$.

8. If $\mathcal A$ is a Banach algebra with identity, show that there are no elements $a,b$ in $\mathcal A$ such that $ab-ba=1$. (Hint: compute $a^nb-ba^n$.)

9. Prove Proposition 1.18.

10. Define $A:L^2(\mathbb R)\to L^2(\mathbb R)$ by $(Af)(x)=\exp(-x^2)f(x-1)$ for all $f$ in $L^2(\mathbb R)$. (a) Show that $A\in\mathcal B(L^2(\mathbb R))$. (b) Find $\|A^n\|$ and show that $r(A)=0$ so that $\sigma(A)=\{0\}$. (c) Show that $A$ is injective. (d) Find $A^*$ and show that $\operatorname{ran}A$ is dense. (e) Define $B=A^{-1}$ with $\operatorname{dom}B=\operatorname{ran}A$ and show that $B\in\mathcal C(L^2(\mathbb R))$ with $\sigma(B)=\square$.

11. If $A\in\mathcal C(\mathcal H)$, show that $A^*A\in\mathcal C(\mathcal H)$. Show that $-1\notin\sigma(A^*A)$ and that if $B=(1+A^*A)^{-1}$, $\|B\|\leq 1$.

12. If $B$ is the bounded operator obtained in Exercise 11, show that $C=AB$ is also bounded and $\|C\|\leq 1$.

13. If $A$ is a self-adjoint operator, then $\lambda\in\rho(A)$ if and only if $A-\lambda$ is surjective.

## §2. Symmetric and Self-Adjoint Operators

An appropriate introduction to this section consists in a careful examination of Examples 1.11 and 1.12 in the preceding section. In (1.11) we saw that the operator $A$ seemed to be inclined to be self-adjoint, but $\operatorname{dom}A^*$ was different from $\operatorname{dom}A$ so we could not truly say that $A=A^*$. In (1.12), $B=B^*$ in any



<a id="pdf-page-324"></a>
sense of the concept of equality. This points out the distinction between symmetric and self-adjoint operators that it is necessary to make in the theory of unbounded operators.

**2.1. Definition.** An operator $A:\mathcal H\to\mathcal H$ is *symmetric* if $A$ is densely defined and $\langle Af,g\rangle=\langle f,Ag\rangle$ for all $f,g$ in $\operatorname{dom}A$.

The proof of the next proposition is left to the reader.

**2.2. Proposition.** If $A$ is densely defined, the following statements are equivalent.

(a) $A$ is symmetric.  
(b) $\langle Af,f\rangle\in\mathbb R$ for all $f$ in $\operatorname{dom}A$.  
(c) $A\subseteq A^*$.

If $A$ is symmetric, then the fact that $A\subseteq A^*$ implies $\operatorname{dom}A^*$ is dense. Hence $A$ is closable by Proposition 1.6. Symmetric operators can behave cantankerously. For example, there is an example of a closed symmetric operator $T$ such that $\operatorname{dom}(T^2)=(0)$. See Chernoff [1983].

It is easy to check that the operators in Examples 1.11 and 1.12 are symmetric.

**2.3. Definition.** A densely defined operator $A:\mathcal H\to\mathcal H$ is *self-adjoint* if $A=A^*$.

Let us emphasize that the condition that $A=A^*$ in the preceding definition carries with it the requirement that $\operatorname{dom}A=\operatorname{dom}A^*$. Now clearly every self-adjoint operator is symmetric, but the operator $A$ in Example 1.11 shows that there are symmetric operators that are not self-adjoint. If, however, an operator is bounded, then it is self-adjoint if and only if it is symmetric. The operator $B$ in Example 1.12 is an unbounded self-adjoint operator and Examples 1.9 and 1.10 can be used to furnish additional examples of unbounded self-adjoint operators.

Note that Proposition 1.6 implies that a self-adjoint operator is necessarily closed.

**2.4. Proposition.** Suppose $A$ is a symmetric operator on $\mathcal H$.

(a) If $\operatorname{ran}A$ is dense, then $A$ is injective.  
(b) If $A=A^*$ and $A$ is injective, then $\operatorname{ran}A$ is dense and $A^{-1}$ is self-adjoint.  
(c) If $\operatorname{dom}A=\mathcal H$, then $A=A^*$ and $A$ is bounded.  
(d) If $\operatorname{ran}A=\mathcal H$, then $A=A^*$ and $A^{-1}\in\mathcal B(\mathcal H)$.

**Proof.** The proof of (a) is trivial and (b) is an easy consequence of (1.13) and some manipulation.



<a id="pdf-page-325"></a>
(c) We have $A\subseteq A^*$. If $\operatorname{dom}A=\mathcal H$, then $A=A^*$ and so $A$ is closed. By the Closed Graph Theorem $A\in\mathcal B(\mathcal H)$.

(d) If $\operatorname{ran}A=\mathcal H$, then $A$ is injective by (a). Let $B=A^{-1}$ with $\operatorname{dom}B=\operatorname{ran}A=\mathcal H$. If $f=Ag$ and $h=Ak$, with $g,k$ in $\operatorname{dom}A$, then $\langle Bf,h\rangle=\langle g,Ak\rangle=\langle Ag,k\rangle=\langle f,k\rangle=\langle f,Bh\rangle$. Hence $B$ is symmetric. By (c), $B=B^*\in\mathcal B(\mathcal H)$. By (b), $A=B^{-1}$ is self-adjoint. $\blacksquare$

We now will turn our attention to the spectral properties of symmetric and self-adjoint operators. In particular, it will be seen that symmetric operators can have nonreal numbers in their spectra, though the nature of the spectrum can be completely diagnosed (2.8). Self-adjoint operators, however, must have real spectra. The next result begins this spectral discussion.

**2.5. Proposition.** *Let $A$ be a symmetric operator and let $\lambda=\alpha+i\beta$, $\alpha$ and $\beta$ real numbers.*

(a) *For each $f$ in $\operatorname{dom}A$, $\|(A-\lambda)f\|^2=\|(A-\alpha)f\|^2+\beta^2\|f\|^2$.*

(b) *If $\beta\ne0$, $\ker(A-\lambda)=(0)$.*

(c) *If $A$ is closed and $\beta\ne0$, $\operatorname{ran}(A-\lambda)$ is closed.*

**Proof.** Note that

$$
\begin{aligned}
\|(A-\lambda)f\|^2
&=\|(A-\alpha)f-i\beta f\|^2\\
&=\|(A-\alpha)f\|^2+2\operatorname{Re}i\langle(A-\alpha)f,\beta f\rangle+\beta^2\|f\|^2.
\end{aligned}
$$

But

$$
\langle(A-\alpha)f,\beta f\rangle
=\beta\langle Af,f\rangle-\alpha\beta\|f\|^2\in\mathbb R,
$$

so (a) follows. Part (b) is immediate from (a). To prove (c), note that $\|(A-\lambda)f\|^2\geqslant\beta^2\|f\|^2$. Let $\{f_n\}\subseteq\operatorname{dom}A$ such that $(A-\lambda)f_n\to g$. The preceding inequality implies that $\{f_n\}$ is a Cauchy sequence in $\mathcal H$; let $f=\lim f_n$. But $f_n\oplus(A-\lambda)f_n\in\operatorname{gra}(A-\lambda)$ and $f_n\oplus(A-\lambda)f_n\to f\oplus g$. Hence $f\oplus g\in\operatorname{gra}(A-\lambda)$ and so $g=(A-\lambda)f\in\operatorname{ran}(A-\lambda)$. This proves (c). $\blacksquare$

**2.6. Lemma.** *If $\mathcal M,\mathcal N$ are closed subspaces of $\mathcal H$ and $\mathcal M\cap\mathcal N^\perp=(0)$, then $\dim\mathcal M\leqslant\dim\mathcal N$.*

**Proof.** Let $P$ be the orthogonal projection of $\mathcal H$ onto $\mathcal N$ and define $T:\mathcal M\to\mathcal N$ by $Tf=Pf$ for $f$ in $\mathcal M$. Since $\mathcal M\cap\mathcal N^\perp=(0)$, $T$ is injective. If $\mathcal L$ is a finite dimensional subspace of $\mathcal M$, $\dim\mathcal L=\dim T\mathcal L\leqslant\dim\mathcal N$. Since $\mathcal L$ was arbitrary, $\dim\mathcal M\leqslant\dim\mathcal N$. $\blacksquare$

**2.7. Theorem.** *If $A$ is a closed symmetric operator, then $\dim\ker(A^*-\lambda)$ is constant for $\operatorname{Im}\lambda>0$ and constant for $\operatorname{Im}\lambda<0$.*

**Proof.** Let $\lambda=\alpha+i\beta$, $\alpha$ and $\beta$ real numbers and $\beta\ne0$.



<a id="pdf-page-326"></a>
**Claim.** If $|\lambda-\mu|<|\beta|$, $\ker(A^*-\mu)\cap[\ker(A^*-\lambda)]^\perp=(0)$.

Suppose this is not so. Then there is an $f$ in $\ker(A^*-\mu)\cap[\ker(A^*-\lambda)]^\perp$ with $\|f\|=1$. By (2.5c), $\operatorname{ran}(A-\bar\lambda)$ is closed. Hence $f\in[\ker(A^*-\lambda)]^\perp=\operatorname{ran}(A-\bar\lambda)$. Let $g\in\operatorname{dom}A$ such that $f=(A-\bar\lambda)g$. Since $f\in\ker(A^*-\mu)$,

$$
\begin{aligned}
0&=\langle(A^*-\mu)f,g\rangle=\langle f,(A-\bar\mu)g\rangle\\
&=\langle f,(A-\bar\lambda+\bar\lambda-\bar\mu)g\rangle\\
&=\|f\|^2+(\lambda-\mu)\langle f,g\rangle.
\end{aligned}
$$

Hence $1=\|f\|^2=|\lambda-\mu|\,|\langle f,g\rangle|\leq|\lambda-\mu|\,\|g\|$. But (2.5a) implies that $1=\|f\|=\|(A-\bar\lambda)g\|\geq|\beta|\,\|g\|$; so $\|g\|\leq|\beta|^{-1}$. Hence $1\leq|\lambda-\mu|\,\|g\|\leq|\lambda-\mu|\,|\beta|^{-1}<1$ if $|\lambda-\mu|<|\beta|$. This contradiction establishes the claim.

Combining the claim with Lemma 2.6 gives that $\dim\ker(A^*-\mu)\leq\dim\ker(A^*-\lambda)$ if $|\lambda-\mu|<|\beta|=|\operatorname{Im}\lambda|$. Note that if $|\lambda-\mu|<\frac12|\beta|$, then $|\lambda-\mu|<|\operatorname{Im}\mu|$, so that the other inequality also holds. This shows that the function $\lambda\mapsto\dim\ker(A^*-\lambda)$ is locally constant on $\mathbb C\setminus\mathbb R$. A simple topological argument demonstrates the theorem. $\blacksquare$

**2.8. Theorem.** *If $A$ is a closed symmetric operator, then one and only one of the following possibilities occurs:*

(a) $\sigma(A)=\mathbb C$;

(b) $\sigma(A)=\{\lambda\in\mathbb C:\operatorname{Im}\lambda\geq0\}$;

(c) $\sigma(A)=\{\lambda\in\mathbb C:\operatorname{Im}\lambda\leq0\}$;

(d) $\sigma(A)\subseteq\mathbb R$.

**Proof.** Let $H_\pm=\{\lambda\in\mathbb C:\pm\operatorname{Im}\lambda>0\}$. By (2.5) for $\lambda$ in $H_\pm$, $A-\lambda$ is injective and has closed range. So if $A-\lambda$ is surjective, $\lambda\in\rho(A)$. But $[\operatorname{ran}(A-\lambda)]^\perp=\ker(A^*-\bar\lambda)$. So the preceding theorem implies that either $H_\pm\subset\sigma(A)$ or $H_\pm\cap\sigma(A)=\square$. Since $\sigma(A)$ is closed, if $H_\pm\subseteq\sigma(A)$, then either $\sigma(A)=\mathbb C$ or $\sigma(A)=\operatorname{cl}H_\pm$. If $H_\pm\cap\sigma(A)=\square$, $\sigma(A)\subseteq\mathbb R$. $\blacksquare$

**2.9. Corollary.** *If $A$ is a closed symmetric operator, the following statements are equivalent.*

(a) $A$ is self-adjoint.

(b) $\sigma(A)\subseteq\mathbb R$.

(c) $\ker(A^*-i)=\ker(A^*+i)=(0)$.

**Proof.** If $A$ is symmetric, every eigenvalue of $A$ is real (Exercise 1). So if $A=A^*$ and $\operatorname{Im}\lambda\neq0$, $\ker(A^*-\lambda)=\ker(A-\lambda)=(0)$. Thus $A-\lambda$ is injective and has dense range. By (2.5), $A-\lambda$ has closed range and so $A-\lambda$ has a bounded inverse (1.15) whenever $\operatorname{Im}\lambda\neq0$. That is, $\sigma(A)\subseteq\mathbb R$ and so (a) implies (b).

If $\sigma(A)\subseteq\mathbb R$, $\ker(A^*\pm i)=[\operatorname{ran}(A\mp i)]^\perp=\mathcal H^\perp=(0)$. Hence (b) implies (c).

If (c) holds, then this, combined with (2.5c) and (1.13), implies $A+i$ is



<a id="pdf-page-327"></a>
surjective. Let $h\in\operatorname{dom}A^*$. Then there is an $f$ in $\operatorname{dom}A$ such that $(A+i)f=(A^*+i)h$. But $A^*+i\supseteq A+i$, so $(A^*+i)f=(A^*+i)h$. But $A^*+i$ is injective, so $h=f\in\operatorname{dom}A$. Thus $A=A^*$. $\blacksquare$

**2.10. Corollary.** *If $A$ is a closed symmetric operator and $\sigma(A)$ does not contain $\mathbb{R}$, then $A=A^*$.*

It may have occurred to the reader that a symmetric operator $A$ fails to be self-adjoint because its domain is too small and that this can be rectified by merely increasing the size of the domain. Indeed, if $A$ is the symmetric operator in Example 1.11, then the operator $B$ of Example 1.12 is a self-adjoint extension of $A$. However, the general situation is not always so cooperative.

Fix a symmetric operator $A$ and suppose $B$ is a symmetric extension of $A$: $A\subseteq B$. It is easy to verify that $B^*\subseteq A^*$. Since $B\subseteq B^*$, we get $A\subseteq B\subseteq B^*\subseteq A^*$. Thus every symmetric extension of $A$ is a restriction of $A^*$.

**2.11. Proposition.** *(a) A symmetric operator has a maximal symmetric extension. (b) Maximal symmetric extensions are closed. (c) A self-adjoint operator is a maximal symmetric operator.*

**Proof.** Part (a) is an easy application of Zorn’s Lemma. If $A$ is symmetric, $A\subseteq A^*$ and so $A$ is closable. The closure of a symmetric operator is symmetric (Exercise 3), so part (b) is immediate. Part (c) is a consequence of the comments preceding this proposition. $\blacksquare$

**2.12. Definition.** Let $A$ be a closed symmetric operator. The *deficiency subspaces* of $A$ are the spaces

$$
\begin{aligned}
\mathcal L_+ &= \ker(A^*-i)=[\operatorname{ran}(A+i)]^\perp,\\
\mathcal L_- &= \ker(A^*+i)=[\operatorname{ran}(A-i)]^\perp.
\end{aligned}
$$

The *deficiency indices* of $A$ are the numbers $n_\pm=\dim\mathcal L_\pm$.

It is possible for any pair of deficiency indices to occur (see Exercise 6).

In order to study the closed symmetric extensions of a symmetric operator we also introduce the spaces

$$
\begin{aligned}
\mathcal K_+ &= \{f\oplus if:f\in\mathcal L_+\},\\
\mathcal K_- &= \{g\oplus(-ig):g\in\mathcal L_-\}.
\end{aligned}
$$

So $\mathcal K_\pm\leq\mathcal H\oplus\mathcal H$. Notice that $\mathcal K_\pm$ are contained in $\operatorname{gra}A^*$ and are the portions of graph of $A^*$ that lie above $\mathcal L_\pm$. The next lemma will indicate why the deficiency subspaces are so named.

**2.13. Lemma.** *If $A$ is a closed symmetric operator,*

$$
\operatorname{gra}A^*=\operatorname{gra}A\oplus\mathcal K_+\oplus\mathcal K_-.
$$



<a id="pdf-page-328"></a>
**Proof.** Let $f\in\mathcal L_+$ and $h\in\operatorname{dom}A$. Then
$$
\begin{aligned}
\langle h\oplus Ah,f\oplus if\rangle
&=\langle h,f\rangle-i\langle Ah,f\rangle\\
&=-i\langle(A+i)h,f\rangle\\
&=0
\end{aligned}
$$
since $\mathcal L_+=[\operatorname{ran}(A+i)]^\perp$. The remainder of the proof that $\operatorname{gra}A$, $\mathcal K_+$, and $\mathcal K_-$ are pairwise orthogonal is left to the reader. Since it is clear that $\operatorname{gra}A\oplus\mathcal K_+\oplus\mathcal K_-\subseteq\operatorname{gra}A^*$, it remains to show that this direct sum is dense in $\operatorname{gra}A^*$.

Let $h\in\operatorname{dom}A^*$ and assume $h\oplus A^*h\perp\operatorname{gra}A\oplus\mathcal K_+\oplus\mathcal K_-$. Since $h\oplus A^*h\perp\operatorname{gra}A$, for every $f$ in $\operatorname{dom}A$, $0=\langle h\oplus A^*h,f\oplus Af\rangle=\langle h,f\rangle+\langle A^*h,Af\rangle$. So $\langle A^*h,Af\rangle=-\langle h,f\rangle$ for every $f$ in $\operatorname{dom}A$. This implies that $A^*h\in\operatorname{dom}A^*$ and $A^*A^*h=-h$. Therefore $(A^*-i)(A^*+i)h=(A^*A^*+1)h=0$. Thus $(A^*+i)h\in\mathcal L_+$. Reversing the order of these factors also shows that $(A^*-i)h\in\mathcal L_-$. But if $g\in\mathcal L_+$, $0=\langle h\oplus A^*h,g\oplus ig\rangle=\langle h,g\rangle-i\langle A^*h,g\rangle=-i\langle(A^*+i)h,g\rangle$. Since $g$ can be taken equal to $(A^*+i)h$, we get that $(A^*+i)h=0$, or $h\in\mathcal L_-$. Similarly, $h\in\mathcal L_+$. So $h\in\mathcal L_+\cap\mathcal L_-=(0)$. $\blacksquare$

**2.14. Definition.** If $A$ is a closed symmetric operator and $\mathcal M$ is a linear manifold in $\operatorname{dom}A^*$, then $\mathcal M$ is *$A$-symmetric* if $\langle A^*f,g\rangle=\langle f,A^*g\rangle$ for all $f,g$ in $\mathcal M$. Call such a manifold *$A$-closed* if $\{f\oplus A^*f:f\in\mathcal M\}$ is closed in $\mathcal H\oplus\mathcal H$.

So $\mathcal M$ is both $A$-symmetric and $A$-closed precisely when $A^*|_{\mathcal M}$, the restriction of $A^*$ to $\mathcal M$, is a closed symmetric operator; if $\mathcal M\supseteq\operatorname{dom}A$, then $A^*|_{\mathcal M}$ is a closed symmetric extension of $A$.

**2.15. Lemma.** *If $A$ is a closed symmetric operator on $\mathcal H$ and $B$ is a closed symmetric extension of $A$, then there is an $A$-closed, $A$-symmetric submanifold $\mathcal M$ of $\mathcal L_++\mathcal L_-$ such that*
$$
\tag{2.16}
\operatorname{gra}B=\operatorname{gra}A+\operatorname{gra}(A^*|_{\mathcal M}).
$$
*Conversely, if $\mathcal M$ is an $A$-closed, $A$-symmetric manifold in $\mathcal L_++\mathcal L_-$, then there is a closed symmetric extension $B$ of $A$ such that (2.16) holds.*

**Proof.** If the $A$-symmetric manifold $\mathcal M$ in $\mathcal L_++\mathcal L_-$ is given, let $\mathcal D=\operatorname{dom}A+\mathcal M$. Since $\mathcal D\subseteq\operatorname{dom}A^*$, $B=A^*|_{\mathcal D}$ is well defined. Let $f=f_0+f_1$, $g=g_0+g_1$, $f_0,g_0$ in $\operatorname{dom}A$ and $f_1,g_1$ in $\mathcal M$. Then
$$
\begin{aligned}
\langle A^*f,g\rangle
&=\langle A^*f_0+A^*f_1,g_0+g_1\rangle\\
&=\langle Af_0,g_0\rangle+\langle Af_0,g_1\rangle
+\langle A^*f_1,g_0\rangle+\langle A^*f_1,g_1\rangle.
\end{aligned}
$$
Using the $A$-symmetry of $\mathcal M$, the symmetry of $A$, and the definition of $A^*$ we get
$$
\begin{aligned}
\langle A^*f,g\rangle
&=\langle f_0,Ag_0\rangle+\langle f_0,A^*g_1\rangle
+\langle f_1,Ag_0\rangle+\langle f_1,A^*g_1\rangle\\
&=\langle f,A^*g\rangle.
\end{aligned}
$$



<a id="pdf-page-329"></a>
So $B=A^*|_{\mathcal D}$ is symmetric. Note that $\operatorname{gra}A\perp\operatorname{gra}(A^*|_{\mathcal M})$ in $\mathcal H\oplus\mathcal H$. Since both of these spaces are closed, $\operatorname{gra}B$, given by (2.16), is closed.

Now let $B$ be any closed symmetric extension of $A$. As discussed before, $A\subseteq B\subseteq A^*$; so $\operatorname{gra}A\subseteq\operatorname{gra}B\subseteq\operatorname{gra}A^*=\operatorname{gra}A\oplus\mathcal K_+\oplus\mathcal K_-$. Let $\mathcal G=\operatorname{gra}B\cap(\mathcal K_+\oplus\mathcal K_-)$ and let $\mathcal M=$ the set of first coordinates of elements in $\mathcal G$. Clearly, $\mathcal M$ is a manifold in $\mathcal L_++\mathcal L_-$ and $\mathcal M\subseteq\operatorname{dom}B$. Hence for $f,g$ in $\mathcal M$, $\langle A^*f,g\rangle=\langle Bf,g\rangle=\langle f,Bg\rangle=\langle f,A^*g\rangle$. So $\mathcal M$ is $A$-symmetric. Clearly, $\operatorname{gra}(A^*|_{\mathcal M})=\mathcal G$, so $\mathcal M$ is $A$-closed. If $h\oplus Bh\in\operatorname{gra}B$, let $h\oplus Bh=(f\oplus Af)+k$ where $f\in\operatorname{dom}A$ and $k\in\mathcal K_+\oplus\mathcal K_-$. Since $A\subseteq B$, $k\in\operatorname{gra}B$; so $k\in\mathcal G$. This shows that (2.16) holds. ■

**2.17. Theorem.** *Let $A$ be a closed symmetric operator. If $W$ is a partial isometry with initial space in $\mathcal L_+$ and final subspace in $\mathcal L_-$, let*

$$
\mathcal D_W=\{f+g+Wg:f\in\operatorname{dom}A,\ g\in\operatorname{initial}W\}. \tag{2.18}
$$

*and define $A_W$ on $\mathcal D_W$ by*

$$
A_W(f+g+Wg)=Af+ig-iWg. \tag{2.19}
$$

*Then $A_W$ is a closed symmetric extension of $A$. Conversely, if $B$ is any closed symmetric extension of $A$, then there is a unique partial isometry $W$ such that $B=A_W$ as in (2.19).*

*If $W$ is such a partial isometry and $W$ has finite rank, then*

$$
n_\pm(A_W)=n_\pm(A)-\dim(\operatorname{ran}W).
$$

**Proof.** Let $W$ be a partial isometry with initial space $I_+$ in $\mathcal L_+$ and final space $I_-$ in $\mathcal L_-$. Define $\mathcal D_W$ and $A_W$ as in (2.18) and (2.19). Let $\mathcal M=\{g+Wg:g\in I_+\}$; so $\mathcal M$ is a manifold in $\mathcal L_++\mathcal L_-$. If $g,h\in I_+$, then $\langle Wg,Wh\rangle=\langle g,h\rangle$. Hence $\langle A^*(g+Wg),h+Wh\rangle=\langle A^*g,h\rangle+\langle A^*g,Wh\rangle+\langle A^*Wg,h\rangle+\langle A^*Wg,Wh\rangle$. Since $g\in\ker(A^*-i)$ and $Wg\in\ker(A^*+i)$,

$$
\begin{aligned}
\langle A^*(g+Wg),h+Wh\rangle
&=i\langle g,h\rangle+i\langle g,Wh\rangle-i\langle Wg,h\rangle-i\langle Wg,Wh\rangle\\
&=i\langle g,Wh\rangle-i\langle Wg,h\rangle.
\end{aligned}
$$

Similarly, $\langle g+Wg,A^*(h+Wh)\rangle=i\langle g,Wh\rangle-i\langle Wg,h\rangle$, so that $\mathcal M$ is $A$-symmetric. If $\{g_n\}\subseteq I_+$ and $(g_n+Wg_n)\oplus(ig_n-iWg_n)\to f\oplus h$ in $\mathcal H\oplus\mathcal H$, then $2ig_n=i(g_n+Wg_n)+(ig_n-iWg_n)\to if+h$ and $2iWg_n=i(g_n+Wg_n)-(ig_n-iWg_n)\to if-h$. If $g=(2i)^{-1}(if+h)$, then $f=g+Wg$ and $h=ig-iWg$. Hence $\mathcal M$ is $A$-closed. By Lemma 2.15, $A_W$ is a closed symmetric extension of $A$.

To prove that $n_+(A_W)=n_+(A)-\dim I_+$, let $f\in\operatorname{dom}A$, $g\in I_+$. Then

$$
\begin{aligned}
(A_W+i)(f+g+Wg)&=(A+i)f+ig-iWg+ig+iWg\\
&=(A+i)f+2ig.
\end{aligned}
$$

Thus $\operatorname{ran}(A_W+i)=\operatorname{ran}(A+i)\oplus I_+$, and so $n_+(A_W)=\dim[\operatorname{ran}(A_W+i)]^\perp=\dim(\mathcal L_+\ominus I_+)=n_+(A)-\dim I_+$. Similarly, $n_-(A_W)=n_-(A)-\dim I_-=n_-(A)-\dim I_+$.



<a id="pdf-page-330"></a>
Now let $B$ be a closed symmetric extension of $A$. By Lemma 2.15 there is an $A$-symmetric, $A$-closed manifold $\mathcal M$ in $\mathcal L_+ + \mathcal L_-$ such that $\operatorname{gra}B=\operatorname{gra}A+\operatorname{gra}(A^*|\mathcal M)$. If $f\in\mathcal M$, let $f=f^++f^-$, where $f^\pm\in\mathcal L_\pm$; put $I_+=\{f^+:f\in\mathcal M\}$. Since $\mathcal M$ is $A$-symmetric, $0=\langle A^*f,f\rangle-\langle f,A^*f\rangle=2i\langle f^+,f^+\rangle-2i\langle f^-,f^-\rangle$; hence $\|f^+\|=\|f^-\|$ for all $f$ in $\mathcal M$. So if $Wf^+=f^-$ whenever $f=f^++f^-\in\mathcal M$ and if $I_+$ is closed, $W$ is a partial isometry and (2.18) and (2.19) are easily seen to hold. It remains to show that $I_+$ is closed. Suppose $\{f_n\}\subseteq\mathcal M$ and $f_n^+\to g^+$ in $\mathcal L_+$. Since $\|f_n^+-f_m^+\|=\|f_n^--f_m^-\|$, there is a $g^-$ in $\mathcal L_-$ such that $f_n^-\to g^-$. Clearly $f_n\to g^++g^-=g$. Also, $A^*f_n^\pm=\pm if_n^\pm\to\pm ig^\pm$. It follows that $g\oplus A^*g\in\operatorname{cl}\operatorname{gra}(A^*|\mathcal M)=\operatorname{gra}(A^*|\mathcal M)$; thus $g^+\in I_+$. $\blacksquare$

**2.20. Theorem.** Let $A$ be a closed symmetric operator with deficiency indices $n_\pm$.

(a) $A$ is self-adjoint if and only if $n_+=n_-=0$.

(b) $A$ has a self-adjoint extension if and only if $n_+=n_-$. In this case the set of self-adjoint extensions is in natural correspondence with the set of isomorphisms of $\mathcal L_+$ onto $\mathcal L_-$.

(c) $A$ is a maximal symmetric operator that is not self-adjoint if and only if either $n_+=0$ and $n_->0$ or $n_+>0$ and $n_-=0$.

**Proof.** Part (a) is a rephrasing of Corollary 2.9. For (b), $n_+=n_-$ if and only if $\mathcal L_+$ and $\mathcal L_-$ are isomorphic. But this is equivalent to stating that there is a partial isometry on $\mathcal H$ with initial and final spaces $\mathcal L_+$ and $\mathcal L_-$, respectively. Part (c) follows easily from the preceding theorem. $\blacksquare$

**2.21. Example.** Let $A$ and $\mathcal D$ be as in Example 1.11; so $A$ is symmetric. The operator $B$ of Example 1.12 is a self-adjoint extension of $A$. Let us determine all self-adjoint extensions of $A$. To do this it is necessary to determine $\mathcal L_\pm$. Now $f\in\mathcal L_\pm$ if and only if $f\in\operatorname{dom}A^*$ and $\pm if=A^*f=if'$, so $\mathcal L_\pm=\{\alpha e^{\pm x}:\alpha\in\mathbb C\}$. Hence $n_\pm=1$. Also, the isomorphisms of $\mathcal L_+$ onto $\mathcal L_-$ are all of the form $W_\lambda e^x=\lambda e^{-x}$ where $|\lambda|=e$. If $|\lambda|=e$, let

$$
\mathcal D_\lambda\equiv\{f+\alpha e^x+\lambda\alpha e^{-x}:\alpha\in\mathbb C,\ f\in\mathcal D\}.
$$

$$
A_\lambda(f+\alpha e^x+\lambda\alpha e^{-x})
=if'+\alpha ie^x-i\lambda\alpha e^{-x},
$$

if $f\in\mathcal D$, $\alpha\in\mathbb C$.

According to Theorem 2.17, $\{(A_\lambda,\mathcal D_\lambda):|\lambda|=e\}$ are all of the self-adjoint extensions of $A$. The operator $B$ of Example 1.12 is the extension $A_e$.

For more information on symmetric operators and the relation of the problem of finding self-adjoint extensions to physical problems, see Reed and Simon [1975] from which much of the present development is taken.

## EXERCISES

1. If $A$ is symmetric, show that all of the eigenvalues of $A$ are real.

2. If $A$ is symmetric and $\lambda,\mu$ are distinct eigenvalues, show that $\ker(A-\lambda)\perp\ker(A-\mu)$.



   <a id="pdf-page-331"></a>
3. Show that the closure of a symmetric operator is symmetric.

4. Let $\mathcal D=\{f\in L^2(0,\infty):$ for every $c>0$, $f$ is absolutely continuous on $[0,c]$, $f(0)=0$, and $f'\in L^2(0,\infty)\}$. Define $Af=if'$ for $f$ in $\mathcal D$. Show that $A$ is a densely defined closed operator and find $\operatorname{dom}A^*$. Show that $A$ is symmetric with deficiency indices $n_+=0$ and $n_-=1$.

5. Let $\mathcal E=\{f\in L^2(-\infty,0):$ for every $c<0$, $f$ is absolutely continuous on $[c,0]$, $f(0)=0$, and $f'\in L^2(-\infty,0)\}$. Define $Af=if'$ for $f$ in $\mathcal E$. Show that $A$ is a densely defined closed operator and find $\operatorname{dom}A^*$. Show that $A$ is symmetric with deficiency indices $n_+=1$, $n_-=0$.

6. If $k,l$ are any nonnegative integers or $\infty$, show that there is a closed symmetric operator $A$ with $n_+=k$ and $n_-=l$. (Hint: Use Exercises 4 and 5.)

7. Let $C_c^2(0,1)$ be all twice continuously differentiable functions on $(0,1)$ with compact support and let $Af=-f''$ for $f$ in $C_c^2(0,1)$. Show that the closure of $A$ is a densely defined symmetric operator and determine all of its self-adjoint extensions.

8. If $A\in\mathcal C(\mathcal H)$, show that $A^*A$ is self-adjoint (see Exercise 1.11).

9. Say that an operator $A$ is positive if $\langle Ah,h\rangle\geq 0$ for all $h$ in $\operatorname{dom}A$. Prove that if $A$ is positive and self-adjoint, then $\sigma(A)\subseteq[0,\infty)$. If $A$ is only assumed to be closed and positive, show that this conclusion may fail. (Hint: Look at the operator in Exercise 7.)

10. (Lasser [1972]) Let $\mathcal M$ be a dense linear manifold in $\mathcal H$ and let $\mathcal A$ consist of all linear transformations $A$ such that $\operatorname{dom}A=\mathcal M$, $A\mathcal M\subseteq\mathcal M$, the adjoint of $A$ exists, $\mathcal M\subseteq\operatorname{dom}A^*$, and $A^*\mathcal M\subseteq\mathcal M$. Prove that $A\mapsto A^*|_{\mathcal M}$ defines an involution on $\mathcal A$.

## §3. The Cayley Transform

<!-- BEGIN BACKGROUND BG-X.block2 -->
<a id="bg-x-5"></a>
### Lemma BG-X.5 — The scalar Cayley map and its exceptional point

For $z=x+iy\ne-i$ let $w=(z-i)/(z+i)$. Then
$$
|w|^2=\frac{x^2+(y-1)^2}{x^2+(y+1)^2},\qquad
z=i\frac{1+w}{1-w}.
$$
Consequently the upper half-plane maps bijectively onto the unit disk and the real line onto the unit circle minus $1$.

**Proof.** Take squared moduli of numerator and denominator. Their difference is $4y$, so $|w|<1$ precisely for $y>0$, and $|w|=1$ for $y=0$. Solving $w(z+i)=z-i$ gives the inverse; its denominator vanishes only at $w=1$. Substitution proves both bijections. $\square$

<a id="bg-x-6"></a>
### Lemma BG-X.6 — Why the inverse Cayley operator is closed

Let $U$ be a partial isometry with closed initial space $M$, assume $(1-U)|_M$ is injective and has dense range, and define $A((1-U)h)=i(1+U)h$ for $h\in M$. Then $A$ is closed.

**Proof.** Its graph is the image of $M$ under $h\mapsto((1-U)h,i(1+U)h)$. The parallelogram identity and $\|Uh\|=\|h\|$ on $M$ give
$$
\|(1-U)h\|^2+\|(1+U)h\|^2=4\|h\|^2.
$$
Thus this map is twice an isometry, so its range is closed by completeness of $M$. This is the missing justification: a bounded operator times a closed operator is **not** automatically closed. $\square$

For unitary $U$, the condition $\ker(1-U)=0$ makes $\operatorname{ran}(1-U)$ dense because its orthogonal complement is $\ker(1-U^*)=\ker(1-U)$. It need not make this range all of $\mathcal H$. For example, on $\ell^2$, $Ue_n=e^{i/n}e_n$ has no eigenvalue $1$, but $1\in\sigma(U)$. The inverse Cayley operator then has diagonal entries of unbounded magnitude and a proper domain.
<!-- END BACKGROUND BG-X.block2 -->

Consider the Möbius transformation

$$
M(z)=\frac{z-i}{z+i}.
$$

It is immediate that $M(0)=-1$, $M(1)=-i$, and $M(\infty)=1$. Thus $M$ maps the upper half plane onto $\mathbb D$ and $M(\mathbb R\cup\infty)=\partial\mathbb D$. So if $A$ is self-adjoint, $M(A)$ should be unitary. Suppose $A$ is symmetric; does $M(A)$ make sense? What is $M(A)$?

To answer these questions, we should first investigate the meaning of $M(A)$ if $A$ is symmetric. We want to define $M(A)$ as $(A-i)(A+i)^{-1}$. As was seen in the last section, however, $\operatorname{ran}(A+i)$ is not necessarily all of $\mathcal H$ if $A$ is not self-adjoint. In fact, $(\operatorname{ran}(A+i))^\perp=\mathcal L_+$ and $(\operatorname{ran}(A-i))^\perp=\mathcal L_-$, the deficiency spaces for $A$. However (2.5), if $A$ is closed and symmetric, $\operatorname{ran}(A\pm i)$ is closed. Also, realize that if $w=M(z)$, then $z=M^{-1}(w)=i(1+w)/(1-w)$.



<a id="pdf-page-332"></a>
**3.1. Theorem.** (a) If $A$ is a closed densely defined symmetric operator with deficiency subspaces $\mathcal L_\pm$, and if $U:\mathcal H\to\mathcal H$ is defined by letting $U=0$ on $\mathcal L_+$ and

$$
U=(A-i)(A+i)^{-1} \tag{3.2}
$$

on $\mathcal L_+^\perp$, then $U$ is a partial isometry with initial space $\mathcal L_+^\perp$, final space $\mathcal L_-^\perp$, and such that $(1-U)(\mathcal L_+^\perp)$ is dense in $\mathcal H$.

(b) If $U$ is a partial isometry with initial and final spaces $\mathcal M$ and $\mathcal N$, respectively, and such that $(1-U)\mathcal M$ is dense in $\mathcal H$, then

$$
A=i(1+U)(1-U)^{-1} \tag{3.3}
$$

is a densely defined closed symmetric operator with deficiency subspaces $\mathcal L_+=\mathcal M^\perp$ and $\mathcal L_-=\mathcal N^\perp$.

(c) If $A$ is given as in (a) and $U$ is defined by (3.2), then $A$ and $U$ satisfy (3.3). If $U$ is given as in (b) and $A$ is defined by (3.3), then $A$ and $U$ satisfy (3.2).

**Proof.** (a) By (2.5c), $\operatorname{ran}(A\pm i)$ is closed and so $\mathcal L_\pm^\perp=\operatorname{ran}(A\pm i)$. By (2.5b), $\ker(A+i)=(0)$, so $(A+i)^{-1}$ is well defined on $\mathcal L_+^\perp$. Moreover, $(A+i)^{-1}\mathcal L_+^\perp\subseteq\operatorname{dom}A$ so that $U$ defined by (3.2) makes sense and gives a well-defined operator. If $h\in\mathcal L_+^\perp$, then $h=(A+i)f$ for a unique $f$ in $\operatorname{dom}A$. Hence $\|Uh\|^2=\|(A-i)f\|^2\overset{(2.5a)}{=}\|Af\|^2+\|f\|^2=\|(A+i)f\|^2=\|h\|^2$. Hence $U$ is a partial isometry, $(\ker U)^\perp=\mathcal L_+^\perp$, and $\operatorname{ran}U=\mathcal L_-^\perp$. Once again, if $f\in\operatorname{dom}A$ and $h=(A+i)f$, then $(1-U)h=h-(A-i)f=(A+i)f-(A-i)f=2if$. So $(1-U)\mathcal L_+^\perp=\operatorname{dom}A$ and is dense in $\mathcal H$.

(b) Now assume that $U$ is a partial isometry as in (b). It follows that $\ker(1-U)=(0)$. In fact, if $f\in\ker(1-U)$, then $Uf=f$; so $\|f\|=\|Uf\|$ and hence $f\in\text{initial }U$. Since $U^*U$ is the projection onto initial $U$, $f=U^*Uf=U^*f$; so $f\in\ker(1-U^*)=\operatorname{ran}(1-U)^\perp\subseteq[(1-U)\mathcal M]^\perp=(0)$ by hypothesis. Thus $f=0$ and $1-U$ is injective.

Let $\mathcal D=(1-U)\mathcal M$ and define $(1-U)^{-1}$ on $\mathcal D$. Because $1-U$ is bounded, $\operatorname{gra}(1-U)^{-1}$ is closed. If $A$ is defined as in (3.3), it follows that $A$ is a closed densely defined operator. If $f,g\in\mathcal D$, let $f=(1-U)h$ and $g=(1-U)k$, $h,k\in\mathcal M$. Hence

$$
\begin{aligned}
\langle Af,g\rangle
&=i\langle(1+U)h,(1-U)k\rangle\\
&=i[\langle h,k\rangle+\langle Uh,k\rangle-\langle h,Uk\rangle-\langle Uh,Uk\rangle].
\end{aligned}
$$

Since $h,k\in\mathcal M$, $\langle Uh,Uk\rangle=\langle h,k\rangle$; hence $\langle Af,g\rangle=i[\langle Uh,k\rangle-\langle h,Uk\rangle]$. Similarly, $\langle f,Ag\rangle=-i\langle(1-U)h,(1+U)k\rangle=-i[\langle h,Uk\rangle-\langle Uh,k\rangle]=\langle Af,g\rangle$. Hence $A$ is symmetric.

Finally, if $h\in\mathcal M$ and $f=(1-U)h$, then $(A+i)f=Af+if=i(1+U)h+i(1-U)h=2ih$. Thus $\operatorname{ran}(A+i)=\mathcal M$. Similarly, $(A-i)f=i(1+U)h-i(1-U)h=2Uh$, so that $\operatorname{ran}(A-i)=\operatorname{ran}U=\mathcal N$.

(c) Suppose $A$ is as in (a) and $U$ is defined as in (3.2). If $g\in(1-U)\mathcal L_+^\perp$, put $g=(1-U)h$, where $h\in\mathcal L_+^\perp=\operatorname{ran}(A+i)$. Hence $h=(A+i)f$ for some $f$ in $\operatorname{dom}A$. Thus $g=h-Uh=(A+i)f-(A-i)f=2if$; so $f=-\frac12ig$.



<a id="pdf-page-333"></a>
Also,

$$
\begin{aligned}
i(1+U)(1-U)^{-1}g
&=i(1+U)h\\
&=i[h+Uh]\\
&=i[(A+i)f+(A-i)f]\\
&=2iAf\\
&=Ag.
\end{aligned}
$$

Therefore (3.3) holds.

The proof of the remainder of (c) is left to the reader. $\blacksquare$

**3.4. Definition.** If $A$ is a densely defined closed symmetric operator, the partial isometry $U$ defined by (3.2) is called the *Cayley transform* of $A$.

**3.5. Corollary.** *If $A$ is a self-adjoint operator and $U$ is its Cayley transform, then $U$ is a unitary operator with $\ker(1-U)=(0)$. Conversely, if $U$ is a unitary with $1\notin\sigma_p(U)$, then the operator $A$ defined by (3.3) is self-adjoint.*

**Proof.** If $A$ is a densely defined symmetric operator, then $A$ is self-adjoint if and only if $\mathcal L_\pm=(0)$. A partial isometry is a unitary operator if and only if its initial and final spaces are all of $\mathcal H$. This corollary is now seen to follow from Theorem 3.1. $\blacksquare$

One use of the Cayley transform is to study self-adjoint operators by using the theory of unitary operators. Indeed, the preceding results say that there is a bijective correspondence between self-adjoint operators and the set of unitary operators without 1 as an eigenvalue.

## Exercises

1. If $U$ is a partial isometry, show that the following statements are equivalent: (a) $\ker(1-U)=(0)$; (b) $\ker(1-U^*)=(0)$; (c) $\operatorname{ran}(1-U)$ is dense; (d) $\operatorname{ran}(1-U^*)$ is dense.

2. Let $U$ be a partial isometry with initial and final spaces $\mathcal M$ and $\mathcal N$, respectively. Show that the following statements are equivalent: (a) $(1-U)\mathcal M$ is dense; (b) $(1-U^*)\mathcal N$ is dense; (c) $\ker(U^*-U^*U)=(0)$; (d) $\ker(U-UU^*)=(0)$.

3. Find a partial isometry $U$ such that $\ker(1-U)=(0)$ but $(1-U)(\ker U)^\perp$ is not dense.

4. If $A$ is a densely defined closed symmetric operator and $B$ and $C$ are the operators defined in Exercises 1.11 and 1.12, then the Cayley transform of $A$ is an extension of $(C-iB)(C+iB)^{-1}$.

5. Find the Cayley transform of the operator in Example 1.9 when each $\alpha_n$ is real.

6. Find the Cayley transform of the operator in Example 1.10 when $\phi$ is real valued.

7. Let $S$ be the unilateral shift of multiplicity 1 (see Exercise IX.6.4) and find the symmetric operator $A$ such that $S$ is the Cayley transform of $A$.



   <a id="pdf-page-334"></a>
8. Let $U=S^*$, where $S$ is the unilateral shift of multiplicity 1. Is $U$ the Cayley transform of a symmetric operator $A$? If so, find it.

## §4. Unbounded Normal Operators and the Spectral Theorem

<!-- BEGIN BACKGROUND BG-X.block3 -->
<a id="bg-x-7"></a>
### Lemma BG-X.7 — Spectral truncation and domain-sensitive algebra

For a spectral measure $E$ and a complex-valued measurable function $f$, possibly unbounded, set $\mu_h(\Delta)=\langle E(\Delta)h,h\rangle$. The natural domain is
$$
D_f=\{h:\int|f|^2\,d\mu_h<\infty\}.
$$
If $P_n=E(\{|f|\leq n\})$, then $P_nh\to h$ for every $h$, and for $h\in D_f$, $f(E)P_nh\to f(E)h$. Thus the union of the ranges of $P_n$ is a core for $f(E)$.

**Proof.** The norm squares of the two tails are $\int_{|f|>n}1\,d\mu_h$ and $\int_{|f|>n}|f|^2\,d\mu_h$, respectively. Dominated convergence makes them tend to zero. Bounded calculus defines $f(E)P_n$ everywhere, so this also explains the construction of the unbounded integral by truncation. $\square$

In a multiplication model the domain of $f(E)g(E)$ is
$$
\{h:\int|g|^2\,d\mu_h<\infty,\ \int|fg|^2\,d\mu_h<\infty\},
$$
which can be smaller than $D_{fg}$. For example, on $L^2[1,\infty)$ take $f(x)=1/x$, $g(x)=x$. Their product formula is $1$, but $M_fM_g$ is the identity restricted to $D_g$, whereas $M_{fg}$ is defined everywhere. Formal cancellation does not cancel domain conditions.
<!-- END BACKGROUND BG-X.block3 -->

If $A$ is self-adjoint, the classical way to obtain the spectral decomposition of $A$ is to let $U$ be the Cayley transform of $A$, obtain the spectral decomposition of $U$, and then use the inverse Cayley transform to translate this back to a decomposition for $A$. There is a spectral theorem for unbounded normal operators, however, and the Cayley transform is not applicable here.

In this section the approach is to prove the spectral theorem for normal operators by using that theorem for the bounded case. The spectral theorem for self-adjoint operators is then only a special case.

**4.1. Definition.** A linear operator $N$ on $\mathcal{H}$ is *normal* if $N$ is closed, densely defined, and $N^*N=NN^*$.

Note that the equation $N^*N=NN^*$ that appears in Definition 4.1 implicitly carries the condition that $\operatorname{dom}N^*N=\operatorname{dom}NN^*$. The operators in Examples 1.9 and 1.10 are normal and every self-adjoint operator is normal. Examining Example 1.9 it is easy to see that for a normal operator it is not necessarily the case that $\operatorname{dom}N^*N=\operatorname{dom}N$.

Parts of the next result have appeared in various exercises in this chapter, but a complete proof is given here.

**4.2. Proposition.** *If $A\in\mathcal{C}(\mathcal{H})$, then*

(a) *$1+A^*A$ has a bounded inverse defined on all of $\mathcal{H}$.*

(b) *If $B=(1+A^*A)^{-1}$, then $\|B\|\leqslant 1$ and $B\geqslant 0$.*

(c) *The operator $C=A(1+A^*A)^{-1}$ is a contraction.*

(d) *$A^*A$ is self-adjoint.*

(e) *$\{h\oplus Ah:h\in\operatorname{dom}A^*A\}$ is dense in $\operatorname{gra}A$.*

**Proof.** Define $J:\mathcal{H}\oplus\mathcal{H}\to\mathcal{H}\oplus\mathcal{H}$ by $J(h\oplus k)=(-k)\oplus h$. By Lemma 1.7, $\operatorname{gra}A^*=[J\operatorname{gra}A]^\perp$. So if $h\in\mathcal{H}$, there are $f$ in $\operatorname{dom}A$ and $g$ in $\operatorname{dom}A^*$ such that $0\oplus h=J(f\oplus Af)+g\oplus A^*g=(-Af)\oplus f+g\oplus A^*g$. Hence $0=-Af+g$, or $g=Af$; also, $h=f+A^*g=f+A^*Af=(1+A^*A)f$. Thus $\operatorname{ran}(1+A^*A)=\mathcal{H}$.

Also, for $f$ in $\operatorname{dom}A^*A$, $Af\in\operatorname{dom}A^*$ and $\|f+A^*Af\|^2=\|f\|^2+2\|Af\|^2+\|A^*Af\|^2\geqslant\|f\|^2$. Hence $\ker(1+A^*A)=(0)$. Thus $(1+A^*A)^{-1}$ exists and is defined on all of $\mathcal{H}$. In the next paragraph (the proof of (b)) it will be shown that $(1+A^*A)^{-1}$ is a contraction, completing the proof of (a).

It was shown that $\|(1+A^*A)f\|\geqslant\|f\|$ whenever $f\in\operatorname{dom}A^*A$. If $h=(1+A^*A)f$ and $B=(1+A^*A)^{-1}$, then this implies that $\|Bh\|\leqslant\|h\|$.



<a id="pdf-page-335"></a>
Hence $\|B\|\leq 1$. In addition, $\langle Bh,h\rangle=\langle f,(1+A^*A)f\rangle=\|f\|^2+\|Af\|^2\geq 0$, so (b) holds.

Put $C=A(1+A^*A)^{-1}=AB$; if $f\in\operatorname{dom}A^*A$ and $(1+A^*A)f=h$, then $\|Ch\|^2=\|Af\|^2\leq\|(1+A^*A)f\|^2=\|h\|^2$ by the argument used to prove (a). Hence $\|C\|\leq 1$, so (c) is proved.

Now to prove (e). Since $A$ is closed, it suffices to show that no nonzero vector in $\operatorname{gra}A$ is orthogonal to $\{h\oplus Ah:h\in\operatorname{dom}A^*A\}$. So let $g\in\operatorname{dom}A$ and suppose that for every $h$ in $\operatorname{dom}A^*A$,

$$
\begin{aligned}
0&=\langle g\oplus Ag,h\oplus Ah\rangle\\
&=\langle g,h\rangle+\langle Ag,Ah\rangle\\
&=\langle g,h\rangle+\langle g,A^*Ah\rangle\\
&=\langle g,(1+A^*A)h\rangle.
\end{aligned}
$$

So $g\perp\operatorname{ran}(1+A^*A)=\mathcal H$; hence $g=0$.

To prove (d), note that (e) implies that $\operatorname{dom}A^*A$ is dense. Now let $f,g\in\operatorname{dom}A^*A$; so $f,g\in\operatorname{dom}A$ and $Af,Ag\in\operatorname{dom}A^*$. Hence $\langle A^*Af,g\rangle=\langle Af,Ag\rangle=\langle f,A^*Ag\rangle$. Thus $A^*A$ is symmetric. Also, $1+A^*A$ has a bounded inverse. This implies two things. First, $1+A^*A$ is closed, and so $A^*A$ is closed. Also, $-1\notin\sigma(A^*A)$ so that by Corollary 2.10, $A^*A$ is self-adjoint. $\blacksquare$

**4.3. Proposition.** *If $N$ is a normal operator, then $\operatorname{dom}N=\operatorname{dom}N^*$ and $\|Nf\|=\|N^*f\|$ for every $f$ in $\operatorname{dom}N$.*

**Proof.** First observe that if $h\in\operatorname{dom}N^*N=\operatorname{dom}NN^*$, then $Nh\in\operatorname{dom}N^*$ and $N^*h\in\operatorname{dom}N$. Hence $\|Nh\|^2=\langle N^*Nh,h\rangle=\langle NN^*h,h\rangle=\|N^*h\|^2$. Now if $f\in\operatorname{dom}N$, (4.2e) implies that there is a sequence $\{h_n\}$ in $\operatorname{dom}N^*N$ such that $h_n\oplus Nh_n\to f\oplus Nf$; so $\|Nh_n-Nf\|\to 0$. But from the first part of this proof, $\|N^*h_n-N^*h_m\|=\|Nh_n-Nh_m\|$. So there is a $g$ in $\mathcal H$ such that $N^*h_n\to g$. Thus $h_n\oplus N^*h_n\to f\oplus g$. But $N^*$ is closed; thus $f\in\operatorname{dom}N^*$ and $g=N^*f$. So $\operatorname{dom}N\subseteq\operatorname{dom}N^*$ and $\|Nf\|=\lim\|Nh_n\|=\lim\|N^*h_n\|=\|N^*f\|$.

On the other hand, $N^*$ is normal (Why?), and so $\operatorname{dom}N^*\subseteq\operatorname{dom}N^{**}=\operatorname{dom}N$. $\blacksquare$

**4.4. Lemma.** *Let $\mathcal H_1,\mathcal H_2,\ldots$ be Hilbert spaces and let $A_n\in\mathcal B(\mathcal H_n)$ for all $n\geq 1$. If $\mathcal D=\{(h_n)\in\bigoplus_n\mathcal H_n:\sum_{n=1}^{\infty}\|A_nh_n\|^2<\infty\}$ and $A$ is defined on $\mathcal H=\bigoplus_n\mathcal H_n$ by $A(h_n)=(A_nh_n)$ whenever $(h_n)\in\mathcal D$, then $A\in\mathcal C(\mathcal H)$. $A$ is a normal operator if and only if each $A_n$ is normal.*

**Proof.** Since $\mathcal H_n\subseteq\mathcal D$ for each $n$, $\mathcal D$ is dense in $\mathcal H$. Clearly $A$ is linear. If $\{h^{(j)}\}\subseteq\operatorname{dom}A$ and $h^{(j)}\oplus Ah^{(j)}\to h\oplus g$ in $\mathcal H\oplus\mathcal H$, then for each $n$, $h_n^{(j)}\oplus A_nh_n^{(j)}\to h_n\oplus g_n$. Since $A_n$ is bounded, $A_nh_n=g_n$. Hence $\sum_n\|Ah_n\|^2=\sum\|g_n\|^2=\|g\|^2<\infty$; so $h\in\operatorname{dom}A$. Clearly $Ah=g$, so $A\in\mathcal C(\mathcal H)$.

It is left to the reader to show that $\operatorname{dom}A^*=\{(h_n)\in\mathcal H:\sum_{n=1}^{\infty}\|A_n^*h_n\|^2<\infty\}$ and $A^*(h_n)=(A_n^*h_n)$ when $(h_n)\in\operatorname{dom}A^*$. From this the rest of the lemma easily follows. $\blacksquare$



<a id="pdf-page-336"></a>
If $(X,\Omega)$ is a measurable space and $\mathcal H$ is a Hilbert space, recall the definition of a spectral measure $E$ for $(X,\Omega,\mathcal H)$ (IX.1.1). If $h,k\in\mathcal H$, let $E_{h,k}$ be the complex-valued measure given by $E_{h,k}(\Delta)=\langle E(\Delta)h,k\rangle$ for each $\Delta$ in $\Omega$.

Let $\phi:X\to\mathbb C$ be an $\Omega$-measurable function and for each $n$ let $\Delta_n=\{x\in X:n-1\leq|\phi(x)|<n\}$. So $\chi_{\Delta_n}\phi$ is a bounded $\Omega$-measurable function. Put $\mathcal H_n=E(\Delta_n)\mathcal H$. Since $\bigcup_{n=1}^{\infty}\Delta_n=X$ and the sets $\{\Delta_n\}$ are pairwise disjoint, $\bigoplus_{n=1}^{\infty}\mathcal H_n=\mathcal H$. If $E_n(\Delta)=E(\Delta\cap\Delta_n)$, $E_n$ is a spectral measure for $(X,\Omega,\mathcal H_n)$. Also, $\int\phi\,dE_n$ is a normal operator on $\mathcal H_n$. Define

$$
\mathcal D_\phi\equiv\left\{h\in\mathcal H:\sum_{n=1}^{\infty}\left\|\left(\int\phi\,dE_n\right)E(\Delta_n)h\right\|^2<\infty\right\}. \tag{4.5}
$$

By Lemma 4.4, $N_\phi:\mathcal H\to\mathcal H$ given by

$$
N_\phi h=\sum_{n=1}^{\infty}\left(\int\phi\,dE_n\right)E(\Delta_n)h \tag{4.6}
$$

for $h$ in $\mathcal D_\phi$ is a normal operator. The operator $N_\phi$ is also denoted by

$$
N_\phi=\int\phi\,dE.
$$

**4.7. Theorem.** If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$, $\phi:X\to\mathbb C$ is an $\Omega$-measurable function, and $\mathcal D_\phi$ and $N_\phi$ are defined as in (4.5) and (4.6), then:

(a) $\mathcal D_\phi=\{h\in\mathcal H:\int|\phi|^2\,dE_{h,h}<\infty\}$;

(b) for $h$ in $\mathcal D_\phi$ and $f$ in $\mathcal H$, $\phi\in L^1(|E_{h,f}|)$ with

$$
\int|\phi|\,d|E_{h,f}|\leq\|f\|\left(\int|\phi|^2\,dE_{h,h}\right)^{1/2}, \tag{4.8}
$$

$$
\left\langle\left(\int\phi\,dE\right)h,f\right\rangle=\int\phi\,dE_{h,f}, \tag{4.9}
$$

and

$$
\left\|\left(\int\phi\,dE\right)h\right\|^2=\int|\phi|^2\,dE_{h,h}.
$$

**Proof.** Using the $*$-homomorphic properties associated with a spectral measure (IX.1.12), one obtains

$$
\begin{aligned}
\left\|\left(\int\phi\,dE_n\right)E(\Delta_n)h\right\|^2
&=\left\langle
\left(\int\chi_{\Delta_n}\phi\,dE\right)^*
\left(\int\chi_{\Delta_n}\phi\,dE\right)h,h
\right\rangle\\
&=\int_{\Delta_n}|\phi|^2\,dE_{h,h}.
\end{aligned}
$$

From here, (a) is immediate.

Now let $h\in\mathcal D_\phi$, $f\in\mathcal H$. By the Radon–Nikodym Theorem, there is an $\Omega$-measurable function $u$ such that $|u|\equiv1$ and $|E_{h,f}|=uE_{h,f}$, where $|E_{h,f}|$ is



<a id="pdf-page-337"></a>
the variation for $E_{h,f}$. Let $\phi_n=\sum_{k=1}^n\chi_{\Delta_k}\phi$; so $\phi_n$ is bounded, as is $u\phi_n$. Thus

$$
\begin{aligned}
\int |\phi_n|\,d|E_{h,f}|
&=\int |\phi_n|u\,dE_{h,f}\\
&=\left\langle\left(\int |\phi_n|u\,dE\right)h,f\right\rangle\\
&\leq \|f\|\left\|\left(\int |\phi_n|u\,dE\right)h\right\|.
\end{aligned}
$$

But

$$
\begin{aligned}
\left\|\left(\int |\phi_n|u\,dE\right)h\right\|^2
&=\left\langle\left(\int |\phi_n|u\,dE\right)h,
\left(\int |\phi_n|u\,dE\right)h\right\rangle\\
&=\left\langle\left(\int |\phi_n|^2\,dE\right)h,h\right\rangle\\
&=\int |\phi_n|^2\,dE_{h,h}\\
&\leq \int |\phi|^2\,dE_{h,h}.
\end{aligned}
$$

Combining this with the preceding inequality gives that $\int |\phi_n|\,d|E_{h,f}|\leq \|f\|(\int |\phi|^2\,dE_{h,h})^{1/2}$ for all $n$. Letting $n\to\infty$ gives (4.8). Since $\phi_n$ is bounded, $\left\langle(\int\phi_n\,dE)h,f\right\rangle=\int\phi_n\,dE_{h,f}$. If $h\in\mathcal D_\phi$ and $f\in\mathcal H$, then (4.8) and the Lebesgue Dominated Convergence Theorem imply that $\int\phi_n\,dE_{h,f}\to\int\phi\,dE_{h,f}$ as $n\to\infty$. But

$$
\begin{aligned}
\left(\int\phi_n\,dE\right)h
&=\left(\int\phi\,dE\right)E\left(\bigcup_{j=1}^n\Delta_j\right)h\\
&=E\left(\bigcup_{j=1}^n\Delta_j\right)\left(\int\phi\,dE\right)h.
\end{aligned}
$$

Since $E(\bigcup_{j=1}^n\Delta_j)\to E(X)=1$ (SOT) as $n\to\infty$, $\left\langle(\int\phi_n\,dE)h,f\right\rangle\to\left\langle(\int\phi\,dE)h,f\right\rangle$ as $n\to\infty$. This proves (4.9). ■

Note that as a consequence of (4.7) $\operatorname{dom}N_\phi$ and the definition of $N_\phi$ do not depend on the choice of the sets $\{\Delta_n\}$, as would seem to be the case from (4.5) and (4.6). Also, by (4.7.a), $E(\Delta)h\in\operatorname{dom}N_\phi$ if $h\in\operatorname{dom}N_\phi$.

**4.10. Theorem.** *If $(X,\Omega)$ is a measurable space, $\mathcal H$ is a Hilbert space, and $E$ is a spectral measure for $(X,\Omega,\mathcal H)$, let $\Phi(X,\Omega)$ be the algebra of all $\Omega$-measurable functions $\phi:X\to\mathbb C$ and define $\rho:\Phi(X,\Omega)\to\mathcal C(\mathcal H)$ by $\rho(\phi)=\int\phi\,dE$. Then for $\phi,\psi$ in $\Phi(X,\Omega)$:*

(a) $\rho(\phi)^*=\rho(\overline{\phi})$;

(b) $\rho(\phi\psi)\supseteq\rho(\phi)\rho(\psi)$ and $\operatorname{dom}(\rho(\phi)\rho(\psi))=\mathcal D_\psi\cap\mathcal D_{\phi\psi}$;



<a id="pdf-page-338"></a>
(c) If $\psi$ is bounded, $\rho(\phi)\rho(\psi)=\rho(\psi)\rho(\phi)=\rho(\phi\psi)$;

(d) $\rho(\phi)^*\rho(\phi)=\rho(|\phi|^2)$.

The proof of this theorem is left as an exercise.

**4.11. The Spectral Theorem.** *If $N$ is a normal operator on $\mathcal H$, then there is a unique spectral measure $E$ defined on the Borel subsets of $\mathbb C$ such that:*

(a) $N=\int z\,dE(z)$;

(b) $E(\Delta)=0$ if $\Delta\cap\sigma(N)=\square$;

(c) if $U$ is an open subset of $\mathbb C$ and $U\cap\sigma(N)\ne\square$, then $E(U)\ne0$;

(d) if $A\in\mathcal B(\mathcal H)$ such that $AN\subseteq NA$ and $AN^*\subseteq N^*A$, then $A(\int\phi\,dE)\subseteq(\int\phi\,dE)A$ for every Borel function $\phi$ on $\mathbb C$.

Before launching into the proof, a few words motivating the proof are appropriate. Suppose a spectral measure $E$ defined on the Borel subsets of $\mathbb C$ is given and let $N=\int z\,dE(z)$. It is not difficult to see that if $0\leq a\leq b<\infty$ and $\Delta$ is the annulus $\{z:a\leq|z|\leq b\}$, then $\mathcal H_\Delta=E(\Delta)\mathcal H=\{h\in\operatorname{dom}N:h\in\operatorname{dom}N^n\text{ for all }n\text{ and }a^n\|h\|\leq\|N^nh\|\leq b^n\|h\|\}$. $\mathcal H_\Delta$ is a closed subspace of $\mathcal H$ that reduces $N$ and $N|_{\mathcal H_\Delta}$ is bounded. The idea behind the proof is to write $\mathbb C$ as the disjoint union of annuli $\{\Delta_j\}$ such that for each $\Delta_j$ there is a reducing subspace $\mathcal H_{\Delta_j}$ for $N$ with $N_j\equiv N|_{\mathcal H_{\Delta_j}}$ bounded, and, moreover, such that $\mathcal H=\bigoplus_j\mathcal H_{\Delta_j}$. Once this is done the Spectral Theorem for bounded normal operators can be applied to each $N_j$ and direct sums of these can be formed to obtain the spectral measure for $N$.

So we would like to show that for the annulus $\{z:a\leq|z|\leq b\}$, $\{h\in\operatorname{dom}N:h\in\operatorname{dom}N^n\text{ for all }n\text{ and }a^n\|h\|\leq\|N^nh\|\leq b^n\|h\|\}$ is a reducing subspace for $N$. To facilitate this, we will use the operator $B=(1+N^*N)^{-1}$ which is a positive contraction (4.2). To understand what is done below note that $z\mapsto(1+|z|^2)^{-1}$ maps $\mathbb C$ onto $(0,1]$ and $a\leq|z|\leq b$ if and only if $(1+a^2)^{-1}\geq(1+|z|^2)^{-1}\geq(1+b^2)^{-1}$.

**4.12. Lemma.** *If $N$ is a normal operator, $B=(1+N^*N)^{-1}$, and $C=N(1+N^*N)^{-1}$, then $BC=CB$ and $(1+N^*N)^{-1}N\subseteq C$.*

**Proof.** From (4.2), $B$ and $C$ are contractions and $B\geq0$. It will first be shown that $(1+N^*N)^{-1}N\subseteq C$; that is, $BN\subseteq NB$. If $f\in\operatorname{dom}BN$, then $f\in\operatorname{dom}N$. Let $g\in\operatorname{dom}N^*N$ such that $f=(1+N^*N)g$. Then $N^*Ng\in\operatorname{dom}N$; hence $Ng\in\operatorname{dom}NN^*=\operatorname{dom}N^*N$. Thus $Nf=Ng+NN^*Ng=(1+N^*N)Ng$. Therefore $BNf=B(1+N^*N)Ng=Ng$. But $NBf=Ng$, so $BN=NB$ on $\operatorname{dom}N$. Thus $BN\subseteq NB$.

If $h\in\mathcal H$, let $f\in\operatorname{dom}N^*N$ such that $h=(1+N^*N)f$. So $BCh=BNBh=BNf=NBf=NBBh=CBh$. Hence $BC=CB$. $\blacksquare$

**4.13. Lemma.** *With the same notation as in Lemma 4.12, if $B=\int t\,dP(t)$ is its spectral representation, $1>\delta>0$, and $\Delta$ is a Borel subset of $[\delta,1]$, then*



<a id="pdf-page-339"></a>
$\mathcal H_\Delta=P(\Delta)\mathcal H\subseteq\operatorname{dom}N$, $\mathcal H_\Delta$ is invariant for both $N$ and $N^*$, and $N|_{\mathcal H_\Delta}$ is a bounded normal operator with $\|N|_{\mathcal H_\Delta}\|\leq[(1-\delta)/\delta]^{1/2}$.

**Proof.** If $h\in\mathcal H_\Delta$, then because $P(\Delta)=\chi_\Delta(B)$,
$\|Bh\|^2=\langle B^2P(\Delta)h,h\rangle=\int_\Delta t^2\,dP_{h,h}\geq\delta^2\|h\|^2$. So $B|_{\mathcal H_\Delta}$ is invertible and there is a $g$ in $\mathcal H_\Delta$ such that $h=Bg$. But $\operatorname{ran}B=\operatorname{dom}(1+N^*N)\subseteq\operatorname{dom}N$. Hence $h\in\operatorname{dom}N$; that is, $\mathcal H_\Delta\subseteq\operatorname{dom}N$.

Let $h\in\mathcal H_\Delta$ and again let $g\in\mathcal H_\Delta$ such that $h=Bg$. Hence $Nh=NBg=Cg$. By Lemma 4.12, $BC=CB$; so by (IX.2.2), $P(\Delta)C=CP(\Delta)$. Since $g\in\mathcal H_\Delta$, $Nh=Cg\in\mathcal H_\Delta$. Note that if $M=N^*$ and $B_1=(1+M^*M)^{-1}$, then $B_1=B$. From the preceding argument $N^*\mathcal H_\Delta=M\mathcal H_\Delta\subseteq\mathcal H_\Delta$. It easily follows that $N|_{\mathcal H_\Delta}$ is normal.

Finally, if $h\in\mathcal H_\Delta$, then

$$
\begin{aligned}
\|Nh\|^2
&=\langle N^*Nh,h\rangle\\
&=\langle[(N^*N+1)-1]h,h\rangle\\
&=\int_\delta^1(t^{-1}-1)\,dP_{h,h}(t)
\leq\|h\|^2(1-\delta)/\delta.
\end{aligned}
$$

Hence $\|N|_{\mathcal H_\Delta}\|\leq[(1-\delta)/\delta]^{1/2}$. $\blacksquare$

**Proof of the Spectral Theorem.** Let $B=(1+N^*N)^{-1}$ and $C=N(1+N^*N)^{-1}$ as in Lemma 4.12. Let $B=\int_0^1t\,dP(t)$ be the spectral decomposition of $B$ and put $P_n=P(1/(n+1),1/n]$ for $n\geq1$. Since $\ker B=(0)=P(\{0\})\mathcal H$, $\sum_{n=1}^\infty P_n=1$. Let $\mathcal H_n=P_n\mathcal H$. By Lemma 4.13, $\mathcal H_n\subseteq\operatorname{dom}N$, $\mathcal H_n$ reduces $N$, and $N_n\equiv N|_{\mathcal H_n}$ is a bounded normal operator with $\|N_n\|\leq n^{1/2}$. Also, if $h\in\mathcal H_n$, $(1+N_n^*N_n)Bh=B(1+N_n^*N_n)h=h$; that is,

$$
B|_{\mathcal H_n}=(1+N_n^*N_n)^{-1}.
$$

Thus if $\lambda\in\sigma(N_n)$, $(1+|\lambda|^2)^{-1}\in\sigma(B|_{\mathcal H_n})\subseteq[1/(n+1),1/n]$. Thus $\sigma(N_n)\subseteq\{z\in\mathbb C:(n-1)^{1/2}\leq|z|\leq n^{1/2}\}\equiv\Delta_n$. Let $N_n=\int z\,dE_n(z)$ be the spectral decomposition of $N_n$. For any Borel subset $\Delta$ of $\mathbb C$, let $E(\Delta)$ be defined by

$$
\tag{4.14}
E(\Delta)=\sum_{n=1}^{\infty}E_n(\Delta\cap\Delta_n).
$$

Note that $E_n(\Delta\cap\Delta_n)$ is a projection with range in $\mathcal H_n$. Since $\mathcal H_n\perp\mathcal H_m$ for $n\neq m$, (4.14) defines a projection in $\mathcal B(\mathcal H)$. (Technically $E(\Delta)$ should be defined by $E(\Delta)=\sum_{n=1}^\infty E_n(\Delta\cap\Delta_n)P_n$. But this technicality does not add anything to understanding.)

Now to show that $E$ is a spectral measure. Clearly $E(\mathbb C)=1$ and $E(\square)=0$. If $\Lambda_1$ and $\Lambda_2$ are Borel subsets of $\mathbb C$, then

$$
\begin{aligned}
E(\Lambda_1\cap\Lambda_2)
&=\sum_{n=1}^{\infty}E_n(\Lambda_1\cap\Lambda_2\cap\Delta_n)\\
&=\sum_{n=1}^{\infty}E_n(\Lambda_1\cap\Delta_n)E_n(\Lambda_2\cap\Delta_n).
\end{aligned}
$$



<a id="pdf-page-340"></a>
Again, the fact that the spaces $\{\mathcal H_n\}$ are pairwise orthogonal implies

$$
\begin{aligned}
E(\Lambda_1\cap\Lambda_2)
&=\left(\sum_{n=1}^{\infty}E_n(\Lambda_1\cap\Delta_n)\right)
  \left(\sum_{n=1}^{\infty}E_n(\Lambda_2\cap\Delta_n)\right)\\
&=E(\Lambda_1)E(\Lambda_2).
\end{aligned}
$$

If $h\in\mathcal H$, then $\langle E(\Delta)h,h\rangle=\sum_{n=1}^{\infty}\langle E_n(\Delta\cap\Delta_n)h,h\rangle$. So if $\{\Lambda_j\}_{j=1}^{\infty}$ are pairwise disjoint Borel sets,

$$
\begin{aligned}
\left\langle E\left(\bigcup_{j=1}^{\infty}\Lambda_j\right)h,h\right\rangle
&=\sum_{n=1}^{\infty}
\left\langle E_n\left(\left(\bigcup_{j=1}^{\infty}\Lambda_j\right)\cap\Delta_n\right)h,h\right\rangle\\
&=\sum_{n=1}^{\infty}\sum_{j=1}^{\infty}
\langle E_n(\Lambda_j\cap\Delta_n)h,h\rangle.
\end{aligned}
$$

Since each term in this double summation is non-negative, the order of summation can be reversed. Thus

$$
\begin{aligned}
\left\langle E\left(\bigcup_{j=1}^{\infty}\Lambda_j\right)h,h\right\rangle
&=\sum_{j=1}^{\infty}\sum_{n=1}^{\infty}
\langle E_n(\Lambda_j\cap\Delta_n)h,h\rangle\\
&=\sum_{j=1}^{\infty}\langle E(\Lambda_j)h,h\rangle.
\end{aligned}
$$

So $E(\bigcup_{j=1}^{\infty}\Lambda_j)=\sum_{j=1}^{\infty}E(\Lambda_j)$; therefore $E$ is a spectral measure.

Let $M=\int z\,dE(z)$ be defined as in Theorem 4.7. Thus $\mathcal H_n\subseteq\operatorname{dom}M$ and by the Spectral Theorem for bounded operators, $Mh=N_nh=Nh$ if $h\in\mathcal H_n$. If $h$ is any vector in $\operatorname{dom}M$, $h=\sum_1^\infty h_n$, $h_n\in\mathcal H_n$, and $\sum_1^\infty\|Nh_n\|^2<\infty$. Because $N$ is closed, $h\in\operatorname{dom}N$ and $Nh=Mh$. Thus $M\subseteq N$. To prove the other inclusion, note that $M$ is a closed operator by Lemma 4.4. Thus, by (4.2.e), it suffices to show that $\{h\oplus Nh:h\in\operatorname{dom}N^*N\}\subseteq\operatorname{gra}M$. If $h\in\operatorname{dom}N^*N$, there is a vector $g$ such that $h=Bg$. Then $P_nNh=P_nNBg=P_nCg=CP_ng$ (Why?) $=NP_nh$. If $h_n=P_nh$, then $\sum\|Nh_n\|^2=\sum\|P_nNh\|^2=\|Nh\|^2<\infty$. Therefore $h\in\operatorname{dom}M$ and so, by the preceding argument, $Nh=Mh$. That is, $h\oplus Nh\in\operatorname{gra}M$. This proves (a).

**4.15. Claim.**

$$
\sigma(N)=\operatorname{cl}\left[\bigcup_{n=1}^{\infty}\sigma(N_n)\right].
$$

It is left to the reader to show that $\bigcup_{n=1}^{\infty}\sigma(N_n)\subseteq\sigma(N)$. Since $\sigma(N)$ is closed, this proves half of (4.15). If $\lambda\notin\operatorname{cl}[\bigcup_{n=1}^{\infty}\sigma(N_n)]$, then there is a $\delta>0$ such that $|\lambda-z|\geq\delta$ for all $z$ in $\bigcup_{n=1}^{\infty}\sigma(N_n)$. Thus $(N_n-\lambda)^{-1}$ exists and $\|(N_n-\lambda)^{-1}\|\leq\delta^{-1}$ for all $n$. Thus $A=\bigoplus_{n=1}^{\infty}(N_n-\lambda)^{-1}$ is a bounded operator. It follows that $A=(N-\lambda)^{-1}$, so $\lambda\notin\sigma(N)$.

By (4.15) if $\Delta\cap\sigma(N)=\square$, $\Delta\cap\sigma(N_n)=\square$ for all $n$. Thus $E_n(\Delta)=0$ for all $n$. Hence $E(\Delta)=0$ and (b) holds.

If $U$ is open and $U\cap\sigma(N)\ne\square$, then (4.15) implies $U\cap\sigma(N_n)\ne\square$ for some $n$. Since $E_n(U)\ne0$, $E(U)\ne0$ and (c) is true.



<a id="pdf-page-341"></a>
Now let $A\in\mathcal{B}(\mathcal{H})$ such that $AN\subseteq NA$ and $AN^*\subseteq N^*A$. Thus $A(1+N^*N)\subseteq(1+N^*N)A$. It follows that $AB=BA$. By the Spectral Theorem for bounded operators, $A$ commutes with the spectral projections of $B$. In particular, each $\mathcal{H}_n$ reduces $A$ and if $A_n\equiv A|_{\mathcal{H}_n}$, then $A_nN_n=N_nA_n$. Hence $A_nE_n(\Delta)=E_n(\Delta)A_n$ for every Borel set $\Delta$ contained in $\Delta_n$. It follows that $AE(\Delta)=E(\Delta)A$ for every Borel set $\Delta$. The remaining details of the proof of (d) are left to the reader. $\blacksquare$

The Fuglede–Putnam Theorem holds for unbounded normal operators (Exercise 8), so that the hypothesis in part (d) of the Spectral Theorem can be weakened to $AN\subseteq NA$.

**4.16. Definition.** If $N$ is a normal operator on $\mathcal{H}$, then a vector $e_0$ is a *star-cyclic* vector for $N$ if for all non-negative integers $k$ and $l$, $e_0\in\operatorname{dom}(N^{*k}N^l)$ and $\mathcal{H}=\bigvee\{N^{*k}N^le_0:k,l\geqslant0\}$.

**4.17. Example.** Let $\mu$ be a finite measure on $\mathbb{C}$ such that every polynomial in $z$ and $\bar z$ belongs to $L^2(\mu)$ and the collection of such polynomials is dense in $L^2(\mu)$. Let $\mathcal{D}_\mu=\{f\in L^2(\mu):zf\in L^2(\mu)\}$ and define $N_\mu f=zf$ for $f$ in $\mathcal{D}_\mu$. Then $N_\mu$ is a normal operator and $1$ is a star-cyclic vector for $N_\mu$.

Note that $d\mu(z)=e^{-|z|}d\operatorname{Area}(z)$ is a measure satisfying the conditions of (4.17).

**4.18. Theorem.** *If $N$ is a normal operator on $\mathcal{H}$ with a star-cyclic vector $e_0$, then there is a finite measure $\mu$ on $\mathbb{C}$ such that every polynomial in $z$ and $\bar z$ belongs to $L^2(\mu)$ and there is an isomorphism $W:\mathcal{H}\to L^2(\mu)$ such that $We_0=1$ and $WNW^{-1}=N_\mu$.*

The proof of Theorem 4.18 can be accomplished by using the Spectral Theorem to write $N$ as the direct sum (in the sense of Lemma 4.4) of bounded normal operators $N_n$ on $\mathcal{H}_n$ with spectral measures that are pairwise mutually singular and such that each $N_n$ has $e_n$, the projection of $e_0$ onto $\mathcal{H}_n$, as a *-cyclic vector. If $\mu_n=E_{e_n,e_n}$, then (IX.3.4) implies that there is an isomorphism $W_n:\mathcal{H}_n\to L^2(\mu_n)$ such that $W_nN_nW_n^{-1}=N_{\mu_n}$. If $W=\bigoplus_1^\infty W_n$, then $W$ is an isomorphism of $\mathcal{H}$ onto $\bigoplus_1^\infty L^2(\mu_n)$. But the fact that the measures $\mu_n$ are pairwise mutually singular implies that $\bigoplus_1^\infty L^2(\mu_n)=L^2(\mu)$, where $\mu=\sum_{n=1}^\infty\mu_n=E_{e_0,e_0}$. Clearly $WNW^{-1}=N_\mu$.

**4.19. Theorem.** *If $N$ is a normal operator on the separable Hilbert space $\mathcal{H}$, then there is a $\sigma$-finite measure space $(X,\Omega,\mu)$ and an $\Omega$-measurable function $\phi$ such that $N$ is unitarily equivalent to $M_\phi$ on $L^2(\mu)$.*

The proof of Theorem 4.19 is only sketched. Write $N$ as the (unbounded) direct sum of bounded normal operators $\{N_n\}$. By Theorem IX.4.6, there is a $\sigma$-finite measure space $(X_n,\Omega_n,\mu_n)$ and a bounded $\Omega_n$-measurable function



<a id="pdf-page-342"></a>
$\phi_n$ such that $N_n\cong M_{\phi_n}$. Let $X$ = the disjoint union of $\{X_n\}$ and let $\Omega=\{\Delta\subseteq X:\Delta\cap X_n\in\Omega_n\text{ for every }n\}$. If $\Delta\in\Omega$, let $\mu(\Delta)=\sum_{1}^{\infty}\mu_n(\Delta\cap X_n)$. Let $\phi:X\to\mathbb C$ be defined by $\phi(x)=\phi_n(x)$ if $x\in X_n$. Then $\phi$ is $\Omega$-measurable and $N\cong M_\phi$ on $L^2(X,\Omega,\mu)$.

## Exercises

1. Prove Theorem 4.10.

2. Show that if $A$ is a symmetric operator that is normal, then $A$ is self-adjoint.

3. With the notation of Theorem 4.7, show that for $h$ in $\mathcal D_\phi$, $\|(\int\phi\,dE)h\|^2=\int|\phi|^2\,dE_{h,h}$.

4. Using the notation of Theorem 4.10, what is $\sigma(\int\phi\,dE)$?

5. If $\Delta_n$ and $E_n$ are as in the proof of the Spectral Theorem, show that $E_n(\Delta_{n+1})=E_n(\Delta_{n-1})=0$.

6. Use the Spectral Theorem to show that if $0<a\leq b<\infty$, $\Delta=\{z\in\mathbb C:a\leq|z|\leq b\}$, and $N=\int z\,dE(z)$ is the spectral decomposition of the normal operator $N$, then
   $$
   E(\Delta)\mathcal H=\{h\in\operatorname{dom}N:a^n\|h\|\leq\|N^nh\|\leq b^n\|h\|\text{ for all }n\geq1\}.
   $$

7. State and prove a polar decomposition for operators in $\mathcal C(\mathcal H,\mathcal H)$.

8. If $A$ is self-adjoint, prove that $\exp(iA)$ is unitary.

9. (Fuglede–Putnam Theorem.) If $N$, $M$ are normal operators and $A$ is a bounded operator such that $AN\subseteq MA$, then $AN^*\subseteq M^*A$.

10. Prove Theorem 4.18.

11. If $\mu_1,\mu_2$ are finite measures on $\mathbb C$ and $N_{\mu_1},N_{\mu_2}$ are defined as in Example 4.17, show that $N_{\mu_1}\cong N_{\mu_2}$ iff $[\mu_1]=[\mu_2]$.

12. Fill in the details of the proof of Theorem 4.19.

## §5. Stone’s Theorem

<!-- BEGIN BACKGROUND BG-X.block4 -->
<a id="bg-x-8"></a>
### Lemma BG-X.8 — Differentiating a spectral exponential strongly

If $A=\int x\,dE(x)$ is self-adjoint and $U(t)=e^{itA}$, then $t\mapsto U(t)h$ is norm continuous for every $h$, and norm differentiable at zero precisely when $h\in\operatorname{dom}A$. Its derivative is then $iAh$.

**Proof.** The scalar identity $e^{is}-1=\int_0^s ie^{ir}\,dr$ gives $|e^{is}-1|\leq|s|$; also $|e^{is}-1|\leq2$. Consequently
$$
\|(U(t)-1)h\|^2=\int|e^{itx}-1|^2\,d\mu_h\longrightarrow0.
$$
For $h\in\operatorname{dom}A$, the squared difference-quotient error is the integral of $|(e^{itx}-1)/t-ix|^2$, bounded by $4x^2$. The domain condition supplies exactly this integrable bound. Conversely, if the difference quotients converge in norm, their norms are bounded along any sequence $t_n\to0$, $t_n\ne0$. Fatou gives
$$
\int x^2\,d\mu_h\leq\liminf_n\|(U(t_n)-1)h/t_n\|^2<\infty.
$$
Thus $h$ belongs to the domain. The group law extends continuity and differentiation from zero to other times. $\square$

Strong continuity is not norm continuity: for multiplication by $x$ on $L^2(\mathbb R)$, $\|e^{itA}-1\|=2$ for every $t\ne0$, although every individual vector moves continuously.
<!-- END BACKGROUND BG-X.block4 -->

If $A$ is a self-adjoint operator on $\mathcal H$, then $\exp(iA)$ is a unitary operator (Exercise 4.7). Hence $U(t)=\exp(itA)$ is unitary for all $t$ in $\mathbb R$. The purpose of this section is not to investigate the individual operators $\exp(itA)$, but rather the entire collection of operators $\{\exp(itA):t\in\mathbb R\}$. In fact, as the first theorem shows, $U:\mathbb R\to$ unitaries on $\mathcal H$ is a group homomorphism with certain properties. Stone’s Theorem provides a converse to this; every such homomorphism arises in this way.

**5.1. Theorem.** *If $A$ is self-adjoint and $U(t)=\exp(itA)$ for $t$ in $\mathbb R$, then*

(a) $U(t)$ is unitary;

(b) $U(s+t)=U(s)U(t)$ for all $s$ in $\mathbb R$;

(c) if $h\in\mathcal H$, then $\lim_{s\to t}U(s)h=U(t)h$;



<a id="pdf-page-343"></a>
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



<a id="pdf-page-344"></a>
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



<a id="pdf-page-345"></a>
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

**Proof.** Begin by defining $\mathcal D$ to be the set of all vectors $h$ in $\mathcal H$ such that $\lim_{t\to0}t^{-1}[U(t)h-h]$ exists; since $0\in\mathcal D$, $\mathcal D\ne\square$. Clearly $\mathcal D$ is a linear manifold in $\mathcal H$.

**5.7. Claim.** $\mathcal D$ is dense in $\mathcal H$.

Let $\mathcal L=$ all continuous functions $\phi$ on $\mathbb R$ such that $\phi\in L^1(0,\infty)$. Hence for any $h$ in $\mathcal H$, $t\mapsto\phi(t)U(t)h$ is a continuous function of $\mathbb R$ into $\mathcal H$. Because $\|U(t)h\|=\|h\|$ for all $t$, a Riemann integral, $\int_0^\infty\phi(t)U(t)h\,dt$, can be defined and is a vector in $\mathcal H$. Put

$$
\begin{aligned}
\text{5.8}\qquad T_\phi h
&=\int_0^\infty\phi(t)U(t)h\,dt.
\end{aligned}
$$

It is easy to see that $T_\phi:\mathcal H\to\mathcal H$ is linear and bounded with $\|T_\phi\|\leq\int_0^\infty|\phi(t)|\,dt$.



<a id="pdf-page-346"></a>
Similarly, for each $\phi$ in $\mathcal L$

$$
S_\phi h=\int_0^\infty \phi(t)U(-t)h\,dt.
\tag{5.9}
$$

defines a bounded operator on $\mathcal H$.

For any $\phi$ in $\mathcal L$ and $t$ in $\mathbb R$,

$$
\begin{aligned}
U(t)T_\phi h
&=U(t)\int_0^\infty \phi(s)U(s)h\,ds\\
&=\int_0^\infty \phi(s)U(t+s)h\,ds\\
&=\int_t^\infty \phi(s-t)U(s)h\,ds.
\end{aligned}
$$

Similarly,

$$
U(t)S_\phi h=\int_{-t}^\infty \phi(s+t)U(-s)h\,ds.
$$

Now let $\mathcal L^{(1)}=$ all $\phi$ in $\mathcal L$ that are continuously differentiable with $\phi'$ in $\mathcal L$. For $\phi$ in $\mathcal L^{(1)}$,

$$
\begin{aligned}
-\frac{i}{t}[U(t)-1]T_\phi h
&=-\frac{i}{t}\int_t^\infty \phi(s-t)U(s)h\,ds
+\frac{i}{t}\int_0^\infty \phi(s)U(s)h\,ds\\
&=-i\int_t^\infty
\left[\frac{\phi(s-t)-\phi(s)}{t}\right]U(s)h\,ds
+\frac{i}{t}\int_0^t \phi(s)U(s)h\,ds.
\end{aligned}
$$

Now

$$
\left\|\int_0^t
\left[\frac{\phi(s-t)-\phi(s)}{t}\right]U(s)h\,ds\right\|
\leq \|h\|\sup\{|\phi(s-t)-\phi(s)|:0\leq s\leq1\}\to0
$$

as $t\to0$. Hence

$$
\begin{aligned}
\lim_{t\to0}\int_t^\infty
\left[\frac{\phi(s-t)-\phi(s)}{t}\right]U(s)h\,ds
&=-\int_0^\infty \phi'(s)U(s)h\,ds\\
&=-T_{\phi'}h.
\end{aligned}
$$

Since $s\mapsto\phi(s)U(s)h$ is continuous and $U(0)=1$, the Fundamental Theorem of Calculus implies that

$$
\lim_{t\to0}\frac1t\int_0^t\phi(s)U(s)h\,ds=\phi(0)h.
$$

Hence for $\phi$ in $\mathcal L^{(1)}$ and $h$ in $\mathcal H$,

$$
\lim_{t\to0}-\frac{i}{t}[U(t)-1]T_\phi h
=iT_{\phi'}h+i\phi(0)h.
\tag{5.10}
$$



<a id="pdf-page-347"></a>
Similarly, for $\phi$ in $\mathcal L^{(1)}$ and $h$ in $\mathcal H$,

$$
\tag{5.11}
\lim_{t\to 0}-\frac{i}{t}[U(t)-1]S_\phi h
=-iS_{\phi'}h-i\phi(0)h.
$$

So (5.10) implies that

$$
\mathcal D\supseteq\{T_\phi h:\phi\in\mathcal L^{(1)}\text{ and }h\in\mathcal H\}.
$$

But for every positive integer $n$ there is a $\phi_n$ in $\mathcal L^{(1)}$ such that $\phi_n\geq 0$, $\phi_n(t)=0$ for $t\geq 1/n$, and $\int_0^\infty\phi_n(t)\,dt=1$ (Exercise 2). Hence

$$
T_{\phi_n}h-h=\int_0^{1/n}\phi_n(t)[U(t)-1]h\,dt
$$

and so $\|T_{\phi_n}h-h\|\leq\sup\{\|U(t)h-h\|:0\leq t\leq 1/n\}$. Therefore $\|T_{\phi_n}h-h\|\to 0$ as $n\to\infty$ since $U$ is strongly continuous. This says that $\mathcal D$ is dense.

For $h$ in $\mathcal D$, define

$$
\tag{5.12}
Ah=-i\lim_{t\to 0}\frac{1}{t}[U(t)-1]h.
$$

**5.13. Claim.** $A$ is symmetric.

The proof of this is left to the reader.

By (2.2c), $A$ is closable; also denote the closure of $A$ by $A$. According to Corollary 2.9, to prove that $A$ is self-adjoint it suffices to prove that $\ker(A^*\pm i)=(0)$. Equivalently, it suffices to show that $\operatorname{ran}(A\pm i)$ is dense. It will be shown that there are operators $B_\pm$ such that $(A\pm i)B_\pm=1$, so that $A\pm i$ is surjective.

Notice that according to (5.10),

$$
(A+i)T_\phi=AT_\phi+iT_\phi=i(T_{\phi'}+T_\phi)+i\phi(0).
$$

So taking $\phi(t)=-ie^{-1}$, $(A+i)T_\phi=1$. According to (5.11),

$$
(A-i)S_\psi=AS_\psi-iS_\psi=-i(S_{\psi'}+S_\psi)-i\psi(0).
$$

Taking $\psi(t)=ie^{-1}$, $(A-i)S_\psi=1$. Hence $A$ is self-adjoint.

Put $V(t)=\exp(iAt)$. It remains to show that $V=U$. Let $h\in\mathcal D$. By Theorem 5.1(d),

$$
s^{-1}[V(t+s)-V(t)]h=s^{-1}[V(s)-1]V(t)h\to iAV(t)h;
$$

that is, $V'(t)h=iAV(t)h$. Similarly,

$$
s^{-1}[U(t+s)-U(t)]h=s^{-1}[U(s)-1]U(t)h\to iAU(t)h.
$$

So if $h(t)=U(t)h-V(t)h$, then $h:\mathbb R\to\mathcal H$ is differentiable and

$$
h'(t)=iAU(t)h-iAV(t)h=iAh(t).
$$



<a id="pdf-page-348"></a>
But

$$
\begin{aligned}
\frac{d}{dt}\|h(t)\|^2
&= \langle h'(t),h(t)\rangle+\langle h(t),h'(t)\rangle\\
&= \langle iAh(t),h(t)\rangle+\langle h(t),iAh(t)\rangle.
\end{aligned}
$$

Thus $(d/dt)\|h(t)\|^2=0$ and so $\|h\|:\mathbb R\to\mathbb R$ is a constant function. But $h(0)=0$, so $h(t)\equiv0$. This says that $U(t)h=V(t)h$ for all $h$ in $\mathscr D$ and all $t$ in $\mathbb R$. Since $\mathscr D$ is dense, $U=V$. ■

**5.14. Definition.** If $U$ is a strongly continuous one parameter unitary group, then the self-adjoint operator $A$ such that $U(t)=\exp(itA)$ is called the *infinitesimal generator* of $U$.

By virtue of Stone’s Theorem and Theorem 5.1, there is a one-to-one correspondence between self-adjoint operators and strongly continuous one-parameter unitary groups. Thus, it should be possible to characterize certain properties of a group in terms of its infinitesimal generator and vice versa. For example, suppose the infinitesimal generator is bounded; what can be said about the group? (Also see Exercise 6.)

**5.15. Proposition.** *If $U$ is a strongly continuous one parameter unitary group with infinitesimal generator $A$, then $A$ is bounded if and only if $\lim_{t\to0}\|U(t)-1\|=0$.*

**Proof.** First assume that $A$ is bounded. Hence $\|U(t)-1\|=\|\exp(itA)-1\|=\sup\{|e^{itx}-1|:x\in\sigma(A)\}\to0$ as $t\to0$ since $\sigma(A)$ is compact.

Now assume that $\|U(t)-1\|\to0$ as $t\to0$. Let $0<\varepsilon<\pi/4$; then there is a $t_0>0$ such that $\|U(t)-1\|<\varepsilon$ for $|t|<t_0$. Since $U(t)-1=\int_{\sigma(A)}(e^{ixt}-1)\,dE(t)$, $\sup\{|e^{ixt}-1|:x\in\sigma(A)\}=\|U(t)-1\|<\varepsilon$ for $|t|<t_0$. Thus for a small $\delta$, $tx\in\bigcup_{n=-\infty}^{\infty}(2\pi n-\delta,2\pi n+\delta)\equiv G$ whenever $x\in\sigma(A)$ and $|t|<t_0$. In fact, if $\varepsilon$ is chosen sufficiently small, then $\delta$ is small enough that the intervals $\{(2\pi n-\delta,2\pi n+\delta)\}$ are the components of $G$. If $x\in\sigma(A)$, $\{tx:0\leq t<t_0\}$ is the interval from $0$ to $t_0x$ and is contained in $G$. Hence $tx\in(-\delta,\delta)$ for $x$ in $\sigma(A)$ and $|t|<t_0$. In particular, $t_0\sigma(A)\subseteq[-\delta,\delta]$ so $\sigma(A)$ is compact and $A$ is bounded. ■

Let $\mu$ be a positive measure on $\mathbb R$ and let $A_\mu f=xf$ for $f$ in $\mathscr D_\mu=\{f\in L^2(\mu):xf\in L^2(\mu)\}$. We have already seen that $A_\mu$ is self-adjoint. Clearly $\exp(itA_\mu)=M_{e_t}$ on $L^2(\mathbb R)$, where $e_t$ is the function $e_t(x)=\exp(itx)$. This can be generalized a bit.

**5.16. Proposition.** *Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $\phi$ be a real-valued $\Omega$-measurable function on $X$. If $A=M_\phi$ on $L^2(\mu)$ and $U(t)=\exp(itA)$, then $U(t)=M_{e_t}$, where $e_t(x)=\exp(it\phi(x))$.*



<a id="pdf-page-349"></a>
Since each self-adjoint operator on a separable Hilbert space can be represented as a multiplication operator (Theorem 4.19), the preceding proposition gives a representation of all strongly continuous one parameter semigroups.

## Exercises

1. If $U:\mathbb R\to\mathcal B(\mathcal H)$ is such that $U(t)$ is unitary for all $t$, $U(s+t)=U(s)U(t)$ for all $s$, $t$, and $U:\mathbb R\to(\mathcal B(\mathcal H),\mathrm{WOT})$ is continuous, then $U$ is SOT-continuous.

2. Show that for every integer $n$ there is a continuously differentiable function $\phi_n$ such that both $\phi_n$ and $\phi_n'\in L^1(0,\infty)$, $\phi_n(t)=0$ if $t\geq 1/n$, and $\int_0^\infty\phi_n(t)\,dt=1$.

3. Prove Claim 5.13.

4. Adopt the notation from the proof of Stone’s Theorem. Let $\phi,\psi\in\mathcal L$ and show: (a) $T_\phi^*=S_{\bar\phi}$; (b) $T_\phi T_\psi=T_{\phi*\psi}$ and $S_\phi S_\psi=S_{\phi*\psi}$; (c) $T_\phi A\subseteq AT_\phi$.

5. Let $U$ be a strongly continuous one parameter unitary group with infinitesimal generator $A$. Suppose $e$ is a nonzero vector in $\mathcal H$ such that $Ae=\lambda e$. What is $U(t)e$? Conversely, suppose there is a nonzero $t$ such that $U(t)$ has an eigenvector. What can be said about $A$? $U(s)$?

6. (This exercise is designed to give another proof of Proposition 5.15 as well as give additional information. My thanks to R.B. Burckel for pointing this out to me.) Let $U$ be a strongly continuous one-parameter unitary group with infinitesimal generator $A$. Show that if $\|U(t)-1\|\to0$ as $t\to0$, then as $t\to0$, $t^{-1}\int_a^{a+t}U(s)\,ds\to U(a)$ in norm. From here show that as $t\to0$, $t^{-1}[U(t)-1]$ has a norm limit, and hence $A$ is a bounded operator since it is the norm limit of bounded operators.

## §6. The Fourier Transform and Differentiation

<!-- BEGIN BACKGROUND BG-X.block5 -->
<a id="bg-x-9"></a>
### Lemma BG-X.9 — The boundary term at infinity really vanishes

If $f$ is locally absolutely continuous and $f,f'\in L^2(\mathbb R)$, then $f(x)\to0$ as $x\to\pm\infty$.

**Proof.** By the fundamental theorem and Cauchy–Schwarz, $|f(x)-f(y)|\leq\|f'\|_2|x-y|^{1/2}$, so $f$ is uniformly continuous. If values of magnitude at least $\varepsilon$ occurred arbitrarily far to the right, uniform continuity would provide disjoint intervals of a fixed positive length on which $|f|\geq\varepsilon/2$. Their squared integrals would force $\|f\|_2=\infty$. The argument to the left is identical. If $\|f'\|_2=0$, $f$ is constant and $L^2$ forces that constant to vanish. $\square$

<a id="bg-x-10"></a>
### Lemma BG-X.10 — Translation continuity and smooth approximation

For $1\leq p<\infty$, $\|f(\cdot-t)-f\|_p\to0$ for $f\in L^p(\mathbb R)$. Smooth compactly supported functions are dense in $L^p(\mathbb R)$. They also form a core for $if'$ on the domain in Example 6.1.

**Proof.** For an interval indicator the $p$th power of the translation difference norm is the length of the symmetric difference, which tends to zero. Finite linear combinations of bounded interval indicators are dense in $L^p$: truncate the function and its support, approximate by simple functions, and approximate their finite-measure level sets by finite unions of intervals using regularity of Lebesgue measure. Since translations are isometries, a three-term triangle inequality proves the assertion for arbitrary $f$.

Choose a nonnegative smooth compactly supported $\rho$ with $\int\rho=1$; for instance normalize $\exp(-1/(1-x^2))$ on $|x|<1$, extended by zero. Set $\rho_\varepsilon(x)=\varepsilon^{-1}\rho(x/\varepsilon)$, with the usual unnormalized convolution in this paragraph. Hölder's inequality for the probability measure $\rho_\varepsilon(t)dt$ gives $|\int g\rho_\varepsilon|^p\leq\int|g|^p\rho_\varepsilon$ (use the triangle inequality when $p=1$). Integration in $x$ and Tonelli then give
$$
\|\rho_\varepsilon*f-f\|_p^p\leq\int\rho_\varepsilon(t)\|f(\cdot-t)-f\|_p^p\,dt\longrightarrow0.
$$
The right side is at most $\sup_{|t|\leq\varepsilon}\|f(\cdot-t)-f\|_p^p$. First truncating $f$ to compact support, then convolving, proves smooth density. For the core assertion choose smooth cutoffs $\chi_R=1$ on $[-R,R]$, supported on $[-2R,2R]$, with $|\chi_R'|\leq C/R$. Then $\chi_Rf\to f$ in $L^2$ and $(\chi_Rf)'=\chi_Rf'+\chi_R'f\to f'$ in $L^2$. Smooth convolution approximates both this compactly supported function and its derivative; integration by parts gives $(\rho_\varepsilon*f)'=\rho_\varepsilon*f'$ for such functions. A diagonal selection gives convergence in graph norm. $\square$

<a id="bg-x-11"></a>
### Lemma BG-X.11 — Differentiation under the Fourier integral

A **Schwartz function** is a complex-valued $C^\infty$ function $\phi$ such that $\sup_x|x^m\phi^{(n)}(x)|<\infty$ for all nonnegative integers $m,n$; the space of these functions is denoted by $\mathcal S$. For such $\phi$ and the normalization $\widehat\phi(\xi)=(2\pi)^{-1/2}\int\phi(x)e^{-i\xi x}\,dx$,
$$
\frac{d^n}{d\xi^n}\widehat\phi=\widehat{(-ix)^n\phi},\qquad
\widehat{\phi^{(m)}}(\xi)=(i\xi)^m\widehat\phi(\xi).
$$

**Proof.** Rapid decrease implies $x^n\phi\in L^1$ for every $n$: bound it by $C/(1+x^2)$. The difference quotient of the exponential is dominated by $|x|$ using BG-X.8, so dominated convergence justifies one derivative; repeat with $(-ix)^n\phi$. For the second identity, integrate by parts on $[-R,R]$. Boundary terms $\phi^{(j)}(\pm R)e^{\mp i\xi R}$ tend to zero by rapid decrease; the remaining integrals converge absolutely. Iterate. Combining the identities shows all $\xi^m(d/d\xi)^n\widehat\phi$ are bounded, and hence $\widehat\phi$ is Schwartz. $\square$

These arguments explain why neither differentiation under an arbitrary $L^1$ Fourier integral nor pointwise interpretation of an arbitrary $L^2$ transform is automatic. The Fourier–Plancherel transform is later defined by completion, not by assuming every $L^2$ function is integrable.
<!-- END BACKGROUND BG-X.block5 -->

Perhaps the best way to begin this section is by examining an example.

**6.1. Example.** Let $\mathcal D=\{f\in L^2(\mathbb R): f\text{ is absolutely continuous on every bounded interval in }\mathbb R\text{ and }f'\in L^2(\mathbb R)\}$. For $f$ in $\mathcal D$, let $Af=if'$. Then $A$ is self-adjoint.

First let’s show that $A$ is symmetric. If $f\in\mathcal D$, note that $f(x)\to0$ as $x\to\pm\infty$ since $f$ and $f'\in L^2(\mathbb R)$. So if $f,g\in\mathcal D$, $0<a<\infty$,

$$
i\int_{-a}^{a}f'(x)\overline{g(x)}\,dx
=i\bigl[f(a)\overline{g(a)}-f(-a)\overline{g(-a)}\bigr]
-i\int_{-a}^{a}f(x)\overline{g'(x)}\,dx.
$$

Hence $\langle Af,g\rangle=\langle f,Ag\rangle$ and $A$ is symmetric.

Now let $g\in\operatorname{dom}A^*$ and for $0<a<\infty$ let $\mathcal D_a=\{f\in\mathcal D:f(x)=0\text{ for }|x|\geq a\}$. The proof that $g\in\operatorname{dom}A$ follows the lines of the argument used in Example 1.11. In fact, let $h=A^*g$. So if $f\in\mathcal D$, then $\int f(x)\overline{h(x)}\,dx=i\int f'(x)\overline{g(x)}\,dx$. Let $H(x)=\int_0^x h(t)\,dt$. Then using integration by parts we get that



<a id="pdf-page-350"></a>
for $f$ in $\mathcal D_a$,

$$
\begin{aligned}
\int_{-a}^{a} f\bar h
&= \overline{H(a)}f(a)-\overline{H(-a)}f(-a)-\int_{-a}^{a}f'\bar H\\
&= -\int_{-a}^{a}f'\bar H.
\end{aligned}
$$

Therefore $\int_{-a}^{a}f'[\bar H-(\bar i\bar g)]=0$ for every $f$ in $\mathcal D_a$. As in (1.11), it follows that $H-ig$ is constant on $[-a,a]$ and $g$ is absolutely continuous. Moreover, $0=H'-ig'=h-ig'$; hence $A^*g=h=ig'$. Thus $g\in\mathcal D$ and $A$ is self-adjoint.

If $A$ is the differentiation operator in Example 6.1, what is the group $U(t)=\exp(itA)$? Since $A$ is not represented as a multiplication operator, Proposition 5.16 cannot be applied. One could proceed to try and discover the spectral measure for $A$. Since $A=\int x\,dE(x)$, $U(t)=\int e^{itx}\,dE(x)$. Or one could be clever.

Later in this section it will be shown that if $\mathcal F:L^2(\mathbb R)\to L^2(\mathbb R)$ is the Fourier–Plancherel transform, then $\mathcal F$ is a unitary operator (6.17) and $\mathcal F^{-1}A\mathcal F=$ the operator on $L^2(\mathbb R)$ of multiplication by the independent variable (6.18). Thus $\mathcal F^{-1}U(t)\mathcal F$ is multiplication by $e^{ixt}$. But it is possible to find $U(t)$ directly.

Recall that if $f\in\operatorname{dom}A$,

$$
Af=-i\lim_{t\to0}\frac{U(t)f-f}{t}.
$$

So

$$
f'(x)=\lim_{t\to0}-\frac{(U(t)f)(x)-f(x)}{t}.
$$

Being clever, one might guess that $(U(t)f)(x)=f(x-t)$.

**6.2. Theorem.** If $A$ and $\mathcal D$ are as in Example 6.1 and $U(t)=\exp(itA)$, then $(U(t)f)(x)=f(x-t)$ for all $f$ in $L^2(\mathbb R)$ and $x,t$ in $\mathbb R$.

**Proof.** Let $(V(t)f)(x)=f(x-t)$. It is easy to see that $V$ is a strongly continuous one parameter unitary group. Let $B$ be the infinitesimal generator of $V$. It must be shown that $B=A$.

Note that $f\in\operatorname{dom}B$ if and only if $\lim_{t\to0}t^{-1}(V(t)f-f)$ exists. Let $f\in C_c^{(1)}(\mathbb R)$; that is, $f$ is continuously differentiable and has compact support. Thus for $t>0$,

$$
\left[\frac{V(t)f-f}{t}\right](x)
=\frac{f(x-t)-f(x)}{t}
=-\frac1t\int_{x-t}^{x}f'(y)\,dy
$$

and

$$
\begin{aligned}
\left|\frac{V(t)f(x)-f(x)}{t}+f'(x)\right|
&\leqslant \frac1t\int_{x-t}^{x}|f'(x)-f'(y)|\,dy\\
&\leqslant \sup\{|f'(x)-f'(y)|:|x-y|\leqslant t\}.
\end{aligned}
$$



<a id="pdf-page-351"></a>
Because $f'$ is continuous with compact support, $f'$ is uniformly continuous. Let $K=\{x:\operatorname{dist}(x,\operatorname{spt}f')\leq 2\}$. So $K$ is compact. For $\varepsilon>0$, let $\delta(\varepsilon)<1$ be such that if $|x-y|<\delta(\varepsilon)$, then $|f'(x)-f'(y)|<\varepsilon$. Hence $\|t^{-1}[Vf-f]+f'\|_2\leq\varepsilon^2|K|$, where $|K|=$ the Lebesgue measure of $K$. Thus $C_c^{(1)}(\mathbb R)\subseteq\operatorname{dom}B$ and $Bf=Af$ for $f$ in $C_c^{(1)}(\mathbb R)$. But if $f\in\operatorname{dom}A$, there is a sequence $\{f_n\}\subseteq C_c^{(1)}(\mathbb R)$ such that $f_n\oplus Af_n\to f\oplus Af$ in $\operatorname{gra}A$ (Exercise 1). But $f_n\oplus Af_n=f_n\oplus Bf_n\in\operatorname{gra}B$, so $f\oplus Af\in\operatorname{gra}B$; that is, $A\subseteq B$. Since self-adjoint operators are maximal symmetric operators (2.11), $A=B$. ■

To show that the Fourier transform demonstrates that $M_x$ and $id/dx$ are unitarily equivalent, we introduce the Schwartz space of rapidly decreasing functions.

**6.3. Definition.** A function $\phi:\mathbb R\to\mathbb R$ is *rapidly decreasing* if $\phi$ is infinitely differentiable and for all integers $m,n\geq 0$,

$$
\tag{6.4}
\|\phi\|_{m,n}\equiv\sup\{|x^m\phi^{(n)}(x)|:x\in\mathbb R\}<\infty.
$$

Let $\mathcal S=\mathcal S(\mathbb R)$ be the set of all rapidly decreasing functions on $\mathbb R$.

Note that if $\phi\in\mathcal S$, then for all $m,n\geq 0$ there is a constant $C_{m,n}$ such that

$$
|\phi^{(n)}(x)|\leq C_{m,n}|x|^{-m}.
$$

Thus if $p$ is any polynomial and $n\geq 0$, $|p(x)\phi^{(n)}(x)|\to 0$ as $|x|\to\infty$. In fact, this is equivalent to $\phi$ belonging to $\mathcal S$ (Exercise 3). Also note that if $\phi\in\mathcal S$, then $x^m\phi^{(n)}\in\mathcal S$ for all $m,n\geq 0$.

It is not difficult to see that $\|\cdot\|_{m,n}$ is a seminorm on $\mathcal S$. Also, $\mathcal S$ with all of these seminorms is a Fréchet space (Exercise 2). The space $\mathcal S$ is sometimes called the *Schwartz space* after Laurent Schwartz.

**6.5. Proposition.** *If $1\leq p\leq\infty$, $\mathcal S\subseteq L^p(\mathbb R)$. If $1\leq p<\infty$, $\mathcal S$ is dense in $L^p(\mathbb R)$; $\mathcal S$ is weak-star dense in $L^\infty(\mathbb R)$.*

**Proof.** We already have that $\mathcal S\subseteq L^\infty(\mathbb R)$. If $1\leq p<\infty$ and $\phi\in\mathcal S$, then

$$
\begin{aligned}
\int_{-\infty}^{\infty}|\phi|^p\,dx
&=\int_{-\infty}^{\infty}(1+x^2)^{-p}(1+x^2)^p|\phi|^p\,dx\\
&\leq\|(1+x^2)^p|\phi|^p\|_\infty
\int_{-\infty}^{\infty}(1+x^2)^{-p}\,dx.
\end{aligned}
$$

Since $(1+x^2)^p\geq 1+x^2$,

$$
\begin{aligned}
\|\phi\|_p
&\leq\pi^{1/p}\|(1+x^2)\phi\|_\infty\\
&\leq\pi^{1/p}\bigl[\|\phi\|_{0,0}+\|\phi\|_{2,0}\bigr].
\end{aligned}
$$

Since $C_c^{(\infty)}(\mathbb R)\subseteq\mathcal S$, the density statements are immediate. ■

**6.6. Definition.** If $f\in L^1(\mathbb R)$, the *Fourier transform* of $f$ is the function $\hat f$ defined



<a id="pdf-page-352"></a>
by
$$
\hat f(x)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb R}f(t)e^{-ixt}\,dt.
$$

Because $f\in L^1(\mathbb R)$, this integral is well defined.

The interested reader may want to peruse §VII.9, where the Fourier transform is presented in the more general context of locally compact abelian groups. That section will not be assumed here.

Recall that if $f,g\in L^1$, then the convolution of $f$ and $g$,
$$
f*g(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt,
$$
belongs to $L^1(\mathbb R)$ and $\|f*g\|_1\leq\|f\|_1\|g\|_1$ if the norm of a function $f$ in $L^1(\mathbb R)$ is defined as $\|f\|_1\equiv(2\pi)^{-1/2}\int|f(x)|\,dx$. It is also true that if $f\in L^p(\mathbb R)$, $1\leq p\leq\infty$, then $f*g\in L^p(\mathbb R)$ and $\|f*g\|_p\leq\|f\|_p\|g\|_1$ (see Exercise 4).

**6.7. Theorem.** (a) If $f\in L^1(\mathbb R)$, then $\hat f$ is a continuous function on $\mathbb R$ that vanishes at $\pm\infty$. Also, $\|\hat f\|_\infty\leq\|f\|_1$.

(b) If $\phi\in\mathcal S$, $\hat\phi\in\mathcal S$. Also for $m,n\geq0$,
$$
(ix)^m\left(\frac{d}{dx}\right)\hat\phi
=\left[\left(\frac{d}{dx}\right)^m\left((-ix)^n\phi\right)\right]^{\wedge}.
\tag{6.8}
$$

(c) If $f,g\in L^1(\mathbb R)$, then $(f*g)^{\wedge}=\hat f\hat g$. If $f$ and $g\in\mathcal S$, then $f*g\in\mathcal S$. (Note: $[\ \ ]^{\wedge}=$ the Fourier transform of the function defined in the brackets.)

**Proof.** (a) The fact that $\hat f$ is continuous is an easy consequence of Lebesgue’s Dominated Convergence Theorem; it is clear that $\|\hat f\|_\infty\leq\|f\|_1$. For the other part of (a), let $f=$ the characteristic function of the interval $(a,b)$. Then $\hat f(x)=i(2\pi)^{-1/2}x^{-1}[e^{-ixb}-e^{-ixa}]\to0$ as $|x|\to\infty$. So $\hat f(x)$ vanishes at $\pm\infty$ if $f$ is a linear combination of such characteristic functions. The result for a general $f$ follows by approximation.

(b) It is convenient to introduce the notation $D\phi=\phi'$. Thus $D^n\phi=\phi^{(n)}$. Also in this proof, as in many others of this section, $x$ will be used to denote the function whose value at $t$ is $t$ and it will also be used occasionally to denote the independent variable.

If $\phi\in\mathcal S$, then differentiation under the integral sign (Why is this justified?) gives
$$
\begin{aligned}
(D\hat\phi)(y)
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}(-it)e^{-iyt}\phi(t)\,dt\\
&=[(-ix)\phi]^{\wedge}(y).
\end{aligned}
$$
By induction we get that for $n\geq0$,
$$
D^n\hat\phi=[(-ix)^n\phi]^{\wedge}.
\tag{6.9}
$$



<a id="pdf-page-353"></a>
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



<a id="pdf-page-354"></a>
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



<a id="pdf-page-355"></a>
**6.13. Proposition.** *If $\psi\in L^{1}(\mathbb R)$ such that $(2\pi)^{-1/2}\int_{\mathbb R}\psi(x)\,dx=1$ and if, for $\varepsilon>0$, $\psi_\varepsilon(x)=\varepsilon^{-1}\psi(x/\varepsilon)$, then for every $f\in C_0(\mathbb R)$, $\psi_\varepsilon*f(x)\to f(x)$ uniformly on $\mathbb R$.*

**Proof.** Note that $(2\pi)^{-1/2}\int\psi_\varepsilon(x)\,dx=1$ for all $\varepsilon>0$. Hence for any $x$ in $\mathbb R$,

$$
\begin{aligned}
\psi_\varepsilon*f(x)-f(x)
&=(2\pi)^{-1/2}\int [f(x-t)-f(x)]\frac{1}{\varepsilon}\psi\left(\frac{t}{\varepsilon}\right)\,dt\\
&=(2\pi)^{-1/2}\int [f(x-s\varepsilon)-f(x)]\psi(s)\,ds.
\end{aligned}
$$

Put $\omega(y)=\sup\{|f(x-y)-f(x)|:y\in\mathbb R\}$. Now $f$ is uniformly continuous (Why?), so if $\varepsilon>0$, then there is a $\delta>0$ such that $\omega(y)<\varepsilon$ if $|y|<\delta$. Thus $\omega(y)\to0$ as $|y|\to0$. Moreover, the inequality above implies

$$
\|\psi_\varepsilon*f-f\|_\infty
\leqslant (2\pi)^{-1/2}\int\omega(s\varepsilon)|\psi(s)|\,ds.
$$

Since $\psi\in L^{1}(\mathbb R)$, the Lebesgue Dominated Convergence Theorem implies that $\|\psi_{\varepsilon_k}*f-f\|_\infty\to0$ whenever $\varepsilon_k\to0$. This proves the proposition. $\blacksquare$

The next result is often called the *Multiplication Formula*. Remember that if $f\in L^{1}(\mathbb R)$, $\hat f\in C_0(\mathbb R)$. Hence $\hat f g\in L^{1}(\mathbb R)$ when both $f$ and $g\in L^{1}(\mathbb R)$.

**6.14. Theorem.** *If $f,g\in L^{1}(\mathbb R)$, then*

$$
\int_{\mathbb R}\hat f(x)g(x)\,dx
=
\int_{\mathbb R}f(x)\hat g(x)\,dx.
$$

**Proof.** The proof is an easy consequence of Fubini’s Theorem. In fact, if $f,g\in L^{1}(\mathbb R)$, then

$$
\begin{aligned}
\int\hat f(x)g(x)\,dx
&=\int\left[\frac{1}{\sqrt{2\pi}}\int f(t)e^{-ixt}\,dt\right]g(x)\,dx\\
&=\int f(t)\left[\frac{1}{\sqrt{2\pi}}\int g(x)e^{-ixt}\,dx\right]dt\\
&=\int f(t)\hat g(t)\,dt.
\end{aligned}
$$

$\blacksquare$

**6.15. Inversion Formula.** *If $\phi\in\mathcal S$, then*

$$
\phi(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat\phi(t)e^{ixt}\,dt.
$$

**Proof.** Let $\rho_\varepsilon(x)=e^{-\varepsilon^{2}x^{2}}$ and put $\psi(x)=\hat\rho_1(x)$. Then by Lemma 6.12



<a id="pdf-page-356"></a>
$\psi_\varepsilon(x)=\varepsilon^{-1}\psi(x/\varepsilon)=\hat{\rho}_\varepsilon(x)$. Also,

$$
(2\pi)^{-1/2}\int\psi(x)\,dx
=(2\pi)^{-1/2}\int_{-\infty}^{\infty}2^{-1/2}e^{-x^2/4}\,dx
=1.
$$

So $\psi_\varepsilon*h(x)\to h(x)$ uniformly for any $h$ in $C_0(\mathbb R)$. If $\phi\in\mathcal S$, put $f=\phi$ and $g=e_x\rho_\varepsilon$ in (6.14). By Proposition 6.11 and Lemma 6.12, $\hat g=U_x\hat\rho_\varepsilon=U_x\psi_\varepsilon$. Thus

$$
\begin{aligned}
\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat\phi(t)e^{itx}e^{-\varepsilon^2t^2}\,dt
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(t)\psi_\varepsilon(t-x)\,dt\\
&=\phi*\psi_\varepsilon(x)\\
&\to\phi(x)
\end{aligned}
$$

as $\varepsilon\to0$. The Lebesgue Dominated Convergence Theorem implies the left-hand side converges to $(2\pi)^{-1/2}\int\hat\phi(t)e^{ixt}\,dt$ and the theorem is proved. $\blacksquare$

In many ways the next result is a rephrasing of the preceding theorem.

**6.16. Theorem.** *If $\mathcal F:\mathcal S\to\mathcal S$ is defined by $\mathcal F\phi=\hat\phi$, $\mathcal F$ is a bijection with*

$$
(\mathcal F^{-1}\phi)(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(t)e^{ixt}\,dt.
$$

*Moreover, if $\mathcal S$ is given the topology induced by the seminorms $\{\|\cdot\|_{m,n}:m,n\geq0\}$ that were defined in (6.4), $\mathcal F$ is a homeomorphism.*

**Proof.** By (6.7b), $\mathcal F\mathcal S\subseteq\mathcal S$. The preceding theorem says that $\mathcal F$ is bijective and gives the formula for $\mathcal F^{-1}$. The proof of the topological statement is left to the reader. $\blacksquare$

**6.17. Plancherel’s Theorem.** *If $\phi\in\mathcal S$, then $\|\phi\|_2=\|\hat\phi\|_2$ and the Fourier transform $\mathcal F$ extends to a unitary operator on $L^2(\mathbb R)$.*

**Proof.** Let $\phi\in\mathcal S$ and put $\psi(x)=\overline{\phi(-x)}$. So $\rho=\phi*\psi\in L^1(\mathbb R)$ and $\hat\rho=\hat\phi\hat\psi$.

An easy calculation shows that $\hat\psi=\overline{\hat\phi}$; hence $\hat\rho=|\hat\phi|^2$. Also, the Inversion Formula shows that $\rho(0)=(2\pi)^{-1/2}\int\hat\rho(x)\,dx=(2\pi)^{-1/2}\int|\hat\phi(x)|^2\,dx$. Thus

$$
\begin{aligned}
\int|\hat\phi(x)|^2\,dx
&=(2\pi)^{1/2}\rho(0)\\
&=(2\pi)^{1/2}\phi*\psi(0)\\
&=\int\phi(x)\psi(0-x)\,dx\\
&=\int|\phi(x)|^2\,dx.
\end{aligned}
$$



<a id="pdf-page-357"></a>
So if $\mathcal S$ is considered as a subspace of $L^2(\mathbb R)$, $\mathcal F$, the Fourier transform, is an isometry on $\mathcal S$. By Proposition 6.5 and the preceding theorem, $\mathcal F$ extends to a unitary operator on $L^2(\mathbb R)$. $\blacksquare$

Warning! The content of the Plancherel Theorem is that the Fourier transform extends to an isometry. The formula for this isometry is not given by the formula for the Fourier transform. Indeed, this formula does not make sense when $f$ is not an $L^1$ function. However, the same symbol, $\mathcal F$, will be used to denote this unitary operator on $L^2(\mathbb R)$. For emphasis it is called the Plancherel transform.

**6.18. Theorem.** *Let $A$ be the operator on $L^2(\mathbb R)$ given by $Af=if'$ and let $M$ be the operator defined by $Mf=xf$. If $\mathcal F:L^2(\mathbb R)\to L^2(\mathbb R)$ is the Plancherel Transform, then $\mathcal F\operatorname{dom}M=\operatorname{dom}A$ and*

$$
\mathcal F^{-1}A\mathcal F=M.
$$

**Proof.** The fact that $A\mathcal F=\mathcal F M$ on $\mathcal S$ is an immediate consequence of Theorem 6.7(b). Since $\mathcal S$ is dense in both $\operatorname{dom}A$ and $\operatorname{dom}M$, the rest of the result follows (with some work—give the details). $\blacksquare$

Fourier analysis is a subject unto itself. One source is Stein and Weiss [1971]; another is Reed and Simon [1975].

<!-- BEGIN BACKGROUND BG-X.block6 -->
<a id="bg-x-12"></a>
### Lemma BG-X.12 — Finishing the domain argument for Fourier diagonalization

Let $A= i\,d/dx$ with the domain in Example 6.1, $M f(x)=xf(x)$ with its maximal $L^2$ domain, and $\mathcal F$ the unitary Fourier–Plancherel transform. Then the identity $A\mathcal F=\mathcal F M$ on Schwartz functions extends to equality of the closed operators, including their domains.

**Proof.** BG-X.10 shows $C_c^\infty\subset\mathcal S$ is a core for $A$. It is also a core for $M$: truncate $f$ to $[-R,R]$, which makes both $f$ and $xf$ converge in $L^2$ as $R\to\infty$; approximate a fixed truncated function by smooth functions with support in $[-R-1,R+1]$. On this fixed interval, ordinary $L^2$ approximation also approximates $xf$, because multiplication by $x$ has norm at most $R+1$. The operator $T=\mathcal F^{-1}A\mathcal F$ is closed, and $\mathcal S$ is a core for it because $\mathcal F\mathcal S=\mathcal S$ and $\mathcal F$ is unitary. Since $T$ and $M$ coincide on a common core, their graphs are both the closure of the same restricted graph. Hence $T=M$. Ambient $L^2$ density alone would not prove this conclusion. $\square$
<!-- END BACKGROUND BG-X.block6 -->

## Exercises

1. If $\mathcal D$ is as in Example 6.1, show that for every $f$ in $\mathcal D$ there is a sequence $\{f_n\}$ in $C_c^{(1)}(\mathbb R)$ such that $f_n\to f$ and $f_n'\to f'$ in $L^2(\mathbb R)$.

2. Show that the Schwartz space $\mathcal S$ with the seminorms $\{\|\cdot\|_{m,n}:m,n\geq 0\}$ is a Fréchet space.

3. If $\phi$ is infinitely differentiable on $\mathbb R$, show that $\phi\in\mathcal S$ if and only if for every integer $n\geq 0$ and every polynomial $p$, $\phi^{(n)}(x)p(x)\to 0$ as $|x|\to\infty$.

4. If $f\in L^p(\mathbb R)$, $1\leq p\leq\infty$, and $g\in L^1(\mathbb R)$, show that $f*g\in L^p(\mathbb R)$ and $\|f*g\|_p\leq\|f\|_p\|g\|_1$. (Hint: See Dunford and Schwartz [1958], p. 530, Exercise 13 for a generalization of Minkowski’s Inequality.)

5. If $\psi$ and $\psi_\varepsilon$ are as Proposition 6.13 and $f\in L^p(\mathbb R)$, $1\leq p<\infty$, show that $\|f*\psi_\varepsilon-f\|_p\to 0$ as $\varepsilon\to 0$. If $f\in L^\infty(\mathbb R)$, show that $f*\psi_\varepsilon\to f$ (weak$^*$).

6. If $f\in L^1(\mathbb R)$ and $\hat f\in L^1(\mathbb R)$, show that $f(x)=(2\pi)^{-1/2}\int_{\mathbb R}\hat f(t)e^{ixt}\,dt$ a.e.

7. If $\mathcal F:L^2(\mathbb R)\to L^2(\mathbb R)$ is the Plancherel Transform and $f\in L^2(\mathbb R)$, show that $(\mathcal F^{-1}f)(x)=(\mathcal Ff)(-x)$.

8. Show that $\mathcal F^4=1$ but $\mathcal F^2\neq 1$. What does this say about $\sigma(\mathcal F)$?

9. Find the Fourier transform of the Hermite polynomials. What do you think? (This exercise is broken up into a series of easier steps on pages 98–99 of Dym and McKean [1972].)



<a id="pdf-page-358"></a>
# §7. Moments

To understand this section, the preceding two sections are unnecessary.

Let $\mu$ be a positive Borel measure on $\mathbb{R}$ such that $\int |t|^n\,d\mu(t)=m_n<\infty$ for every $n\geq 0$. The numbers $\{m_n\}$ are called the *moments* of $\mu$ in analogy with the corresponding concept from mechanics. The central problem here, called the *Hamburger moment problem*, is to characterize those sequences of numbers that are moment sequences. Just as self-adjoint operators are connected to measures, the theory of self-adjoint operators is connected to the solution of this moment problem.

**7.1. Theorem.** If $\{m_n:n\geq 0\}$ is a sequence of real numbers, the following statements are equivalent.

(a) There is a positive regular Borel measure $\mu$ on $\mathbb{R}$ such that $\int |t|^n\,d\mu(t)<\infty$ for all $n\geq 0$ and $m_n=\int t^n\,d\mu(t)$.

(b) If $\alpha_0,\ldots,\alpha_n\in\mathbb{C}$, then $\sum_{j,k=0}^{n}m_{j+k}\alpha_j\bar{\alpha}_k\geq 0$.

(c) There is a self-adjoint operator $A$ and a vector $e$ such that $e\in\operatorname{dom}A^n$ for all $n$ and $m_n=\langle A^ne,e\rangle$ for all $n\geq 0$.

Before proving this theorem, a preliminary result is needed. This result is useful in many other situations and is one of the standard ways to show that a symmetric operator has a self-adjoint extension.

**7.2. Proposition.** Let $T$ be a symmetric operator on $\mathcal{H}$ and suppose there is a function $J:\mathcal{H}\to\mathcal{H}$ having the following properties:

(a) $J$ is conjugate linear (that is, $J(h+g)=Jh+Jg$ and $J(\alpha h)=\bar{\alpha}Jh$);

(b) $J^2=1$;

(c) $J$ is continuous;

(d) $J\operatorname{dom}T\subseteq\operatorname{dom}T$ and $TJ\subseteq JT$.

Then $T$ has a self-adjoint extension.

**Proof.** First note that if $h\in\operatorname{dom}T$, then $Jh\in\operatorname{dom}T$ and $h=J(Jh)$. Hence $J\operatorname{dom}T=\operatorname{dom}T$ and $JT=TJ$.

Let $h\in\mathcal{H}$ and define $L:\mathcal{H}\to\mathbb{C}$ by $L(f)=\langle h,Jf\rangle$. Since $J$ is conjugate linear, $L$ is a linear functional. By (c), $L$ is continuous. Thus there is a unique vector $h^*$ in $\mathcal{H}$ such that $L(f)=\langle f,h^*\rangle$. Let $J^*h=h^*$. Thus $J^*:\mathcal{H}\to\mathcal{H}$ and

$$
\langle f,J^*h\rangle=\langle h,Jf\rangle. \tag{7.3}
$$

It is clear that $J^*$ is additive. If $\alpha\in\mathbb{C}$, then $\langle f,J^*(\alpha h)\rangle=\langle\alpha h,Jf\rangle=\alpha\langle f,J^*h\rangle=\langle f,\bar{\alpha}J^*h\rangle$. Thus $J^*$ is conjugate linear. Since $J^2=1$, it follows that $J^{*2}=1$.

Let $h\in\operatorname{dom}T^*$ and $f\in\operatorname{dom}T$. Then $\langle TJf,h\rangle=\langle Jf,T^*h\rangle=\langle J^*T^*h,f\rangle$ by (7.3). But also by (d), $\langle TJf,h\rangle=\langle JTf,h\rangle=\langle J^*h,Tf\rangle$. So $\langle J^*T^*h,f\rangle=\langle J^*h,Tf\rangle$ for all $h$ in $\operatorname{dom}T^*$ and $f$ in $\operatorname{dom}T$. But this says that $J^*h\in\operatorname{dom}T^*$.



<a id="pdf-page-359"></a>
whenever $h\in\operatorname{dom}T^*$ and, furthermore, $T^*J^*h=J^*T^*h$. Since $J^{*2}=1$, it follows that $J^*\operatorname{dom}T^*=\operatorname{dom}T^*$ and $J^*T^*=T^*J^*$.

Now let $h\in\ker(T^*\pm i)$. Then $T^*J^*h=J^*T^*h=J^*(\pm ih)=\mp iJ^*h$. Thus $J^*\ker(T^*\pm i)\subseteq\ker(T^*\mp i)$. Since $J^{*2}=1$, $J^*\ker(T^*\pm i)=\ker(T^*\mp i)$. But $J^*$ is injective. Indeed, if $J^*h=0$, then $h=J^*(J^*h)=0$. Thus the deficiency indices of $T$ are equal. By Theorem 2.20, $T$ has a self-adjoint extension. $\blacksquare$

**PROOF OF THEOREM 7.1.** (a) *implies* (b). If $\alpha_0,\ldots,\alpha_n\in\mathbb C$, then

$$
\begin{aligned}
\sum_{j,k=0}^{n}m_{j+k}\alpha_j\overline{\alpha}_k
&=\int\sum_{j,k=0}^{n}\alpha_j\overline{\alpha}_k t^{j+k}\,d\mu(t)\\
&=\int\left(\sum_{j=0}^{n}\alpha_jt^j\right)
          \left(\sum_{k=0}^{n}\overline{\alpha}_kt^k\right)d\mu(t)\\
&=\int\left|\sum_{k=0}^{n}\alpha_kt^k\right|^2d\mu(t)\geqslant0.
\end{aligned}
$$

(b) *implies* (c). Let $\mathcal H_0=$ the collection of all finitely nonzero sequences of complex numbers $\{\alpha_n:n\geqslant0\}$. That is, $\{\alpha_0,\alpha_1,\ldots\}\in\mathcal H_0$ if $\alpha_n\in\mathbb C$ for all $n\geqslant0$ and $\alpha_n=0$ for all but a finite number of values of $n$. If $x=\{\alpha_n\}$, $y=\{\beta_n\}\in\mathcal H_0$ define $[x,y]$ by

$$
[x,y]\equiv\sum_{j,k=0}^{\infty}m_{j+k}\alpha_j\overline{\beta}_k. \tag{7.4}
$$

It is easy to see that $\mathcal H_0$ is a vector space and (7.4) defines a semi-inner product on $\mathcal H_0$. In fact, it is routine that $[\cdot,\cdot]$ is sesquilinear and condition (b) implies that $[x,x]\geqslant0$ for all $x$ in $\mathcal H_0$.

Let $\mathcal K_0=\{x\in\mathcal H_0:[x,x]=0\}$ and let $\mathcal H_1$ be the quotient vector space $\mathcal H_0/\mathcal K_0$. If $h=x+\mathcal K_0$ and $f=y+\mathcal K_0\in\mathcal H_1$, then

$$
\langle h,f\rangle\equiv[x,y] \tag{7.5}
$$

can be verified to be a well-defined inner product on $\mathcal H_1$. Let $\mathcal H$ be the Hilbert space obtained by completing $\mathcal H_1$ with respect to the norm defined by the inner product (7.5).

Now to define some operators. If $x=\{\alpha_n\}\in\mathcal H_0$, let $T_0x=\{0,\alpha_0,\alpha_1,\ldots\}$. It is easy to check that $T_0$ is a linear transformation on $\mathcal H_0$. Also, if $x=\{\alpha_n\}$, $y=\{\beta_n\}\in\mathcal H_0$, let $T_0x=\{\gamma_n\}$. So $\gamma_0=0$ and $\gamma_n=\alpha_{n-1}$ if $n\geqslant1$. Hence

$$
\begin{aligned}
[T_0x,y]
&=\sum_{j,k=0}^{\infty}m_{j+k}\gamma_j\overline{\beta}_k\\
&=\sum_{\substack{j=1\\k=0}}^{\infty}m_{j+k}\alpha_{j-1}\overline{\beta}_k\\
&=\sum_{j,k=0}^{\infty}m_{j+k+1}\alpha_j\overline{\beta}_k.
\end{aligned}
$$



<a id="pdf-page-360"></a>
$$
\begin{aligned}
&= \sum_{\substack{j=0\\ k=1}}^{\infty} m_{j+k}\alpha_j\overline{\beta}_{k-1}\\
&= [x,T_0y].
\end{aligned}
$$

In particular, if $x\in\mathcal K_0$, then the preceding equation and the CBS inequality imply that

$$
\begin{aligned}
\left|[T_0x,T_0x]\right|
&=\left|[T_0^2x,x]\right|
\leqslant [T_0^2x,T_0^2x][x,x]\\
&=0.
\end{aligned}
$$

Hence $T_0\mathcal K_0\subseteq\mathcal K_0$. Thus $T_0$ induces a linear transformation $T$ on $\mathcal H_1$ defined by $T(x+\mathcal K_0)=T_0x+\mathcal K_0$. It follows that $\langle Th,f\rangle=\langle h,Tf\rangle$ for all $h,f$ in $\mathcal H_1$. Since $\mathcal H_1$ is, by definition, dense in $\mathcal H$, $T$ is a densely defined symmetric operator on $\mathcal H$. Now to show that $T$ has a self-adjoint extension.

Define $J_0:\mathcal H_0\to\mathcal H_0$ by $J_0(\{\alpha_n\})=\{\overline{\alpha}_n\}$. It is easy to see that $J_0$ is conjugate linear and $J_0^2=1$. Also, $J_0T_0=T_0J_0$. An easy calculation shows that $[J_0x,J_0y]=[x,y]$ for all $x,y$ in $\mathcal H_0$. So $J_0\mathcal K_0\subseteq\mathcal K_0$ and $J_0$ induces a conjugate linear function $J_1:\mathcal H_1\to\mathcal H_1$ defined by $J_1(x+\mathcal K_0)=J_0x+\mathcal K_0$. It follows that $J_1T=TJ_1$, $J_1^2=1$, and $\|J_1h\|=\|h\|$ for all $h$ in $\mathcal H_1$. Thus $J_1$ extends to a conjugate linear $J:\mathcal H\to\mathcal H$ such that $J^2=1$ and $\|Jh\|=\|h\|$ for all $h$ in $\mathcal H$. Hence $J$ is continuous. Also, $J\operatorname{dom}T=J_1\mathcal H_1\subseteq\mathcal H_1=\operatorname{dom}T$ and $TJ\subseteq JT$. By Proposition 7.2, $T$ has a self-adjoint extension $A$.

Let $e_0=\{1,0,0,\ldots\}\in\mathcal H_0$. Hence $T_0^ne_0$ has a 1 in the $n$th place and zeros elsewhere. If $e=e_0+\mathcal K_0$, then $e\in\operatorname{dom}T^n\subseteq\operatorname{dom}A^n$ for all $n\geqslant0$. Also,

$$
\langle A^ne,e\rangle=[T_0^ne_0,e_0]=m_n
$$

for $n\geqslant0$.

(c) implies (a). By the Spectral Theorem there is a spectral measure $E$ for $A$. Let $\mu=E_{e,e}$; by (4.11) $\mu$ is supported on $\mathbf R$ and, since $e\in\operatorname{dom}A$, $\mu$ is finite. Moreover, since $e\in\operatorname{dom}A^n$ for every $n\geqslant0$ it follows (supply the details) that $\int t^n\,d\mu(t)<\infty$ for every $n\geqslant0$. Finally, by (4.9), $m_n=\langle A^ne,e\rangle=\int t^n\,d\mu(t)$ for every $n\geqslant0$. $\blacksquare$

The measure obtained in Theorem 7.1 need not be unique since, in the proof that (b) implies (c) above, the self-adjoint extension of $T$ may not be unique. See pages 201–202 of Berg, Christensen, and Ressel [1984] for an example as well as further discussions of moment problems.

## Exercises

1. (Stieltjes.) Let $\{m_n:n\geqslant0\}$ be a sequence of real numbers and show that the following statements are equivalent. (a) There is a positive regular Borel measure $\mu$ on $[0,\infty)$ such that $m_n=\int t^n\,d\mu(t)$ for all $n\geqslant0$. (b) If $\alpha_0,\ldots,\alpha_n\in\mathbf C$, then $\sum_{j,k=0}^{n}m_{j+k}\alpha_j\overline{\alpha}_k\geqslant0$ and $\sum_{j,k=0}^{n}m_{j+k+1}\alpha_j\overline{\alpha}_k\geqslant0$. (c) There is a self-adjoint operator $A$ with $\sigma(A)\subseteq[0,\infty)$ and a vector $e$ in $\operatorname{dom}A^n$ for all $n\geqslant0$ such that $m_n=\langle A^ne,e\rangle$ for $n\geqslant0$.

2. (Bochner.) Let $m:\mathbf R\to\mathbf C$ be a function and show that the following statements are



   <a id="pdf-page-361"></a>
   equivalent. (a) There is a finite positive measure $\mu$ on $\mathbb{R}$ such that $m(t)=\int e^{ixt}\,d\mu(x)$ for all $t$ in $\mathbb{R}$. (b) $m$ is continuous and if $\alpha_0,\ldots,\alpha_n\in\mathbb{C}$ and $t_0,\ldots,t_n\in\mathbb{R}$, then $\sum_{j,k=0}^{n}m(t_j-t_k)\alpha_j\bar{\alpha}_k\geq 0$. (c) There is a strongly continuous one-parameter unitary group $U(t)$ and a vector $e$ such that $m(t)=\langle U(t)e,e\rangle$ for all $t$. (Hint: Let $\mathcal{H}_0=$ all functions $f:\mathbb{R}\to\mathbb{C}$ that vanish off a finite set.)

3. Let $\{m_n:n\in\mathbb{Z}\}\subseteq\mathbb{C}$ and show that the following statements are equivalent. (a) There is a positive measure $\mu$ on $\partial\mathbb{D}$ such that $m_n=\int z^n\,d\mu(z)$ for all $n$ in $\mathbb{Z}$. (b) If $\alpha_{-n},\ldots,\alpha_{-1},\alpha_0,\alpha_1,\ldots,\alpha_n\in\mathbb{C}$, then $\sum_{j,k=-n}^{n}m_{j-k}\alpha_j\bar{\alpha}_k\geq 0$. (c) There is a unitary operator $U$ and a vector $e$ such that $m_n=\langle U^n e,e\rangle$ for all $n$.

4. Show that the operator $A$ that appears in the proof that (7.1b) implies (7.1c) is cyclic.

<!-- BEGIN SOLUTIONS X -->

## Exercise Solutions

These are added study solutions. Inner products are linear in the first
variable. Equality of unbounded operators always includes equality of their
domains. We write $H^1(I)$ for the $L^2$ functions with an absolutely
continuous representative locally on $I$ and first derivative in $L^2$;
$H^2(I)$ additionally requires the second derivative in $L^2$. On a bounded
interval their endpoint values, and the first-derivative values for $H^2$,
are continuous for the respective graph norms. For example,
$|f(0)|\leq\|f\|_2+\|f'\|_2$ on $(0,1)$, by integrating
$f(0)=f(x)-\int_0^x f'(t)\,dt$. Weak derivatives give a convenient closedness
test: if $f_n\to f$ and $f_n'\to g$ in $L^2$, integration against smooth
compactly supported test functions gives $f'=g$ in distributions, and
$f$ has the required absolutely continuous representative.

### §1. Domains, adjoints, and resolvents

#### Solution X.1.1 — The adjoint of a product

If $y\in\operatorname{dom}(B^*A^*)$, then $y\in\operatorname{dom}A^*$
and $A^*y\in\operatorname{dom}B^*$. For every
$x\in\operatorname{dom}(AB)$,
$\langle ABx,y\rangle=\langle Bx,A^*y\rangle
=\langle x,B^*A^*y\rangle$. This is precisely the bounded-functional
criterion for $y\in\operatorname{dom}(AB)^*$ and
$(AB)^*y=B^*A^*y$. The domain restriction is why the conclusion is an
inclusion, not a general equality.

#### Solution X.1.2 — A diagonal operator

Finite linear combinations of the $e_n$ belong to $\mathcal D$, so it is
dense. If $h_j\to h$ and $Ah_j\to k$, coordinate convergence gives
$\langle k,e_n\rangle=\alpha_n\langle h,e_n\rangle$ for every $n$.
Since $k\in H$, these coordinates are square summable. Thus
$h\in\mathcal D$ and $Ah=k$, proving closedness. Testing the adjoint
identity on $e_n$ forces
$\langle A^*y,e_n\rangle=\bar\alpha_n\langle y,e_n\rangle$.
This is square summable exactly when $y\in\mathcal D$; for these $y$,
Cauchy–Schwarz justifies summing the adjoint identity. This proves both
the asserted adjoint domain and formula.

#### Solution X.1.3 — A multiplication operator

Let $X_j$ increase to $X$ with finite measure and put
$F_j=X_j\cap\{|\phi|\leq j\}$. Truncation to $F_j$ shows that the
domain is dense. If $f_n\to f$ and $\phi f_n\to g$ in $L^2$, take a
common subsequence converging almost everywhere in both coordinates.
Then $g=\phi f$ almost everywhere, proving closedness. For an adjoint
domain vector $h$, testing against arbitrary $L^2$ functions supported
in $F_j$ forces the representing vector to equal $\bar\phi h$ there.
Exhaustion gives this identity everywhere, so $\bar\phi h\in L^2$.
Conversely this condition makes the integral pairing bounded by
$\|f\|_2\|\bar\phi h\|_2$. Thus $A^*=M_{\bar\phi}$ on the same domain.

#### Solution X.1.4 — An unbounded weighted shift

For scalars $w_n$ on $\ell^2(\mathbb N_0)$ set
$\operatorname{dom}W=\{x:\sum_n|w_nx_n|^2<\infty\}$,
$(Wx)_0=0$, and $(Wx)_{n+1}=w_nx_n$. Finite sequences give density;
coordinate limits, as in X.1.2, give closedness. The operator is unbounded
when $\sup_n|w_n|=\infty$, since $\|We_n\|=|w_n|$.
Testing on $e_n$ and then summing gives
$\operatorname{dom}W^*=\{y:\sum_n|\bar w_ny_{n+1}|^2<\infty\}$ and
$(W^*y)_n=\bar w_ny_{n+1}$.

#### Solution X.1.5 — Differentiation with two zero endpoints

Smooth compactly supported functions give density. The weak-derivative
criterion above and continuity of the endpoint traces show that
$A=iD$ on $\{f\in H^1(0,1):f(0)=f(1)=0\}$ is closed.
Integration by parts gives
$\langle if',g\rangle-\langle f,ig'\rangle
=i[f\bar g]_0^1$. The boundary term vanishes for every domain vector
$f$, without restrictions on $g\in H^1(0,1)$. Conversely the adjoint
identity on test functions forces $g$ to have weak derivative in $L^2$.
Thus $\operatorname{dom}A^*=H^1(0,1)$ and $A^*g=ig'$.
This also verifies that $A$ is symmetric but not self-adjoint.
The derivative range is exactly the functions of integral zero:
$\int_0^1f'=f(1)-f(0)=0$, and conversely the primitive of such an
$L^2$ function has both zero endpoints. To verify the uniform-closure
statement as well, approximate a continuous zero-endpoint function
uniformly by polynomials $p_n$ and replace each by
$p_n(x)-(1-x)p_n(0)-xp_n(1)$. These polynomials lie in the domain
and still converge uniformly.

#### Solution X.1.6 — An everywhere defined operator with dense graph

Let $\kappa$ be the infinite Hilbert dimension of $H$. Choose a dense
subset of $H\oplus H$ of cardinality $\kappa$, and enumerate all its
pairs together with all positive integer accuracy parameters. Recursively
choose linearly independent $x_\alpha$ within the prescribed accuracy
of each first coordinate, and assign $Ax_\alpha$ to be the second
coordinate. This choice is possible: at stage $\alpha<\kappa$ the
algebraic span of the earlier vectors has dimension less than $\kappa$,
is proper, and cannot contain an open ball. Extend the independent set
to a Hamel basis and define $A$ arbitrarily, say as zero, on the added
basis vectors. Its linear extension is defined on all of $H$, and its
graph approximates every member of a dense subset arbitrarily closely.
Hence the graph is dense. If $y\in\operatorname{dom}A^*$, the continuous
functional $(x,z)\mapsto\langle z,y\rangle-\langle x,A^*y\rangle$
vanishes on the dense graph and therefore everywhere. Taking $x=0$
gives $y=0$. Thus $\operatorname{dom}A^*=\{0\}$.

#### Solution X.1.7 — A commutator on its proper domain

If $f\in H^1(0,1)$, then $xf\in H^1(0,1)$ and
$(xf)'=f+xf'$. Consequently $DA$ and $AD$ are both defined on
$\operatorname{dom}D$, and $(DA-AD)f=f$. Thus $DA-AD$ is the restriction
of $I$ to that domain. It is not the everywhere defined identity:
for example a step function lies in $L^2$ but not in $H^1$.

#### Solution X.1.8 — Bounded operators cannot have this commutator

Induction using $ab-ba=1$ gives $a^nb-ba^n=na^{n-1}$. No power of $a$
can vanish: a least zero power would make the preceding identity a
contradiction. Therefore
$n\|a^{n-1}\|\leq2\|b\|\|a^n\|
\leq2\|a\|\|b\|\|a^{n-1}\|$.
Cancel the nonzero factor to obtain $n\leq2\|a\|\|b\|$ for every $n$,
an impossibility. The domain issue in X.1.7 avoids this contradiction.

#### Solution X.1.9 — Resolvents and adjoints

If $T=A-\lambda$ is bijective, its inverse is an everywhere defined
closed operator, so the closed graph theorem makes it bounded. This
proves (a). Put $R=T^{-1}$. For $y\in H$ and $x\in\operatorname{dom}T$,
$\langle Tx,R^*y\rangle=\langle RTx,y\rangle=\langle x,y\rangle$.
Thus $T^*R^*=I$. If $T^*z=0$, then $z\perp\operatorname{ran}T=H$;
therefore $T^*$ is bijective with inverse $R^*$. Applying the same
argument to $T^*$ and using $T^{**}=T$ proves the converse and hence
$\sigma(A^*)=\overline{\sigma(A)}$ (complex conjugation of the set).

#### Solution X.1.10 — An empty unbounded spectrum

The shift is unitary and the weight has essential supremum one, so
$\|A\|=1$. Iteration gives
$(A^nf)(x)=\exp(-\sum_{j=0}^{n-1}(x-j)^2)f(x-n)$.
Completing the square yields
$\sum_{j=0}^{n-1}(x-j)^2=n(x-(n-1)/2)^2+n(n^2-1)/12$.
Hence $\|A^n\|=e^{-n(n^2-1)/12}$ and the spectral-radius formula gives
$r(A)=0$. The positive weight proves injectivity. A change of variables
gives $(A^*g)(x)=e^{-(x+1)^2}g(x+1)$, also injective, so
$\overline{\operatorname{ran}A}=H$.
The graph of $B=A^{-1}$ is the flipped closed graph of $A$; its domain
is dense. For every $\lambda\in\mathbb C$, $I-\lambda A$ is invertible,
and $(B-\lambda)^{-1}=A(I-\lambda A)^{-1}$ is bounded, with range in
$\operatorname{ran}A=\operatorname{dom}B$. Direct multiplication on
these domains proves both inverse identities. Thus $\sigma(B)=\varnothing$.

#### Solution X.1.11 — The positive graph resolvent

The graph domain of $A$, with inner product
$\langle x,y\rangle_A=\langle x,y\rangle+\langle Ax,Ay\rangle$,
is a Hilbert space because $A$ is closed. Riesz representation gives,
for each $f\in H$, a unique $x$ satisfying
$\langle y,x\rangle+\langle Ay,Ax\rangle=\langle y,f\rangle$
for every $y\in\operatorname{dom}A$. Thus $Ax\in\operatorname{dom}A^*$
and $(I+A^*A)x=f$. Taking $y=x$ gives
$\|x\|^2+\|Ax\|^2=\langle f,x\rangle$, hence $\|x\|\leq\|f\|$.
The inverse $B$ is bounded, positive and self-adjoint, by the same
identity with two right-hand sides. It is injective; therefore its
range is dense. Its inverse is closed, so $A^*A=B^{-1}-I$ is densely
defined and closed, $-1\in\rho(A^*A)$, and $\|B\|\leq1$.

#### Solution X.1.12 — The bounded companion

For $x=Bf$, the identity just proved gives
$\|ABf\|^2=\langle f,Bf\rangle-\|Bf\|^2
\leq\|f\|\|Bf\|-\|Bf\|^2\leq\|f\|^2/4$.
Thus $C=AB$ is everywhere defined and bounded; in fact $\|C\|\leq1/2$,
which is stronger than the requested estimate.

#### Solution X.1.13 — Surjectivity for a self-adjoint operator

For nonreal $\lambda$, the estimate
$\|(A-\lambda)x\|\geq|\operatorname{Im}\lambda|\|x\|$ gives
injectivity. For real $\lambda$, self-adjointness gives
$\ker(A-\lambda)=\operatorname{ran}(A-\lambda)^\perp$, so
surjectivity again gives injectivity. A bijective closed operator has
bounded inverse by X.1.9. The converse follows from the definition of
the resolvent.

### §2. Symmetry and self-adjoint extensions

#### Solution X.2.1 — Real eigenvalues

If $Ax=\lambda x$ and $x\ne0$, symmetry makes
$\lambda\|x\|^2=\langle Ax,x\rangle=\langle x,Ax\rangle$
real. Thus $\lambda\in\mathbb R$.

#### Solution X.2.2 — Orthogonal eigenspaces

For $Ax=\lambda x$, $Ay=\mu y$, symmetry and X.2.1 give
$\lambda\langle x,y\rangle=\langle Ax,y\rangle
=\langle x,Ay\rangle=\mu\langle x,y\rangle$.
When $\lambda\ne\mu$ this forces $\langle x,y\rangle=0$.

#### Solution X.2.3 — Closure preserves symmetry

Since $A\subseteq A^*$ and $A^*$ is closed, $A$ is closable.
If $x_n\to x$, $Ax_n\to\bar A x$ and $y_n\to y$,
$Ay_n\to\bar A y$, passing to the limit in
$\langle Ax_n,y_n\rangle=\langle x_n,Ay_n\rangle$
proves symmetry of $\bar A$. Its domain is still dense.

#### Solution X.2.4 — The positive half-line

Compactly supported smooth functions prove density; weak derivatives
and the trace estimate prove closedness. An $H^1(0,\infty)$ function
tends to zero at infinity: $|f|^2$ has integrable derivative
$2\operatorname{Re}(f'\bar f)$ and is integrable, so its limit is zero.
Integration by parts therefore has only the boundary term at zero.
As in X.1.5, the adjoint is $iD$ on all of $H^1(0,\infty)$, without
the zero trace requirement. This also proves symmetry on the original
domain. The equations $A^*g=ig$ and $A^*g=-ig$ give respectively
$g'=g$ and $g'=-g$. Only $e^{-x}$ is square integrable on this half-line.
Thus $(n_+,n_-)=(0,1)$.

#### Solution X.2.5 — The negative half-line

The density, closedness and adjoint proof is identical, with the
boundary term at $-\infty$ zero and a trace at zero. Thus the adjoint
domain is $H^1(-\infty,0)$. Now $e^x$ is square integrable and $e^{-x}$
is not. Consequently $(n_+,n_-)=(1,0)$.

#### Solution X.2.6 — Prescribed deficiency indices

Take $k$ copies of the negative-half-line operator and $l$ copies of
the positive-half-line operator. Use their Hilbert direct sum with domain
$\{(x_j):x_j\in\operatorname{dom}A_j,
\sum_j(\|x_j\|^2+\|A_jx_j\|^2)<\infty\}$.
Coordinate limits prove closedness; finite supported domain vectors
prove density and symmetry. Testing the adjoint coordinate by coordinate
shows that each deficiency space is the Hilbert sum of the corresponding
deficiency spaces. Thus the dimensions are $k,l$, including countably
infinite values. If both are zero, use any bounded self-adjoint operator.

#### Solution X.2.7 — All boundary conditions for the second derivative

The closure of the initial operator is $A_0f=-f''$ on
$\{f\in H^2(0,1):f(0)=f(1)=f'(0)=f'(1)=0\}$.
Indeed its graph norm is equivalent to the $H^2$ norm (integrate twice
and estimate the affine part); the traces are continuous. Conversely
zero extension belongs to $H^2(\mathbb R)$ because both value and
first-derivative jumps vanish. First compress its support slightly
into $(0,1)$ by an affine change of variable, then convolve with a
smooth mollifier supported in a still smaller interval. Translations
and dilations are strongly continuous on $L^2$ for each of the first
two derivatives, and mollification converges there too. This proves
approximation in $H^2$ by test functions.
Testing distributions and integrating twice shows
$A_0^*f=-f''$ on all of $H^2(0,1)$.

Put $q_f=(f(0),f(1))$ and $p_f=(f'(0),-f'(1))$. Green's identity is
$\langle A_0^*f,g\rangle-\langle f,A_0^*g\rangle
=\langle p_f,q_g\rangle-\langle q_f,p_g\rangle$.
The trace map onto $\mathbb C^2\oplus\mathbb C^2$ is surjective:
cubic interpolation prescribes all four traces. Its kernel is the
minimal domain. For each unitary $V$ on $\mathbb C^2$, impose
$q_f+ip_f=V(q_f-ip_f)$ and let $A_Vf=-f''$ on that domain.
The boundary form vanishes there, and the allowed trace space is its
own annihilator, so the adjoint has exactly the same domain.
Conversely a self-adjoint extension gives such a maximal neutral trace
space. On it the maps $q+ip$ and $q-ip$ have equal norm; neither has a
nonzero kernel, and maximality makes their ranges all of $\mathbb C^2$.
They therefore define precisely one unitary $V$. This parametrizes all
extensions; $V=-I$ gives Dirichlet and $V=I$ gives Neumann conditions.

#### Solution X.2.8 — Self-adjointness of A-star-A

Write $T=A^*A$. X.1.11 proves that $T$ is densely defined, positive,
symmetric, and $T+I$ is onto. If $y\in\operatorname{dom}T^*$, choose
$x\in\operatorname{dom}T$ with $(T+I)x=(T^*+I)y$.
Then $(T^*+I)(y-x)=0$. Its kernel is
$\operatorname{ran}(T+I)^\perp=0$. Thus $y=x$ and $T^*=T$.

#### Solution X.2.9 — Positivity alone is insufficient

A self-adjoint operator has real spectrum. If $c>0$, positivity gives
$\|(A+c)x\|\geq c\|x\|$. Its range is closed, and its orthogonal
complement is $\ker(A+c)=0$, so it is onto and $-c\in\rho(A)$.
Thus the spectrum is contained in $[0,\infty)$.
For a counterexample without self-adjointness use $A_0$ in X.2.7.
It is closed and $\langle A_0f,f\rangle=\|f'\|^2\geq0$.
For every complex $\lambda$, the differential equation
$-g''=\bar\lambda g$ has nonzero solutions in $H^2(0,1)$.
Hence $\ker(A_0^*-\bar\lambda)\ne0$, the range of $A_0-\lambda$
is not dense, and $\sigma(A_0)=\mathbb C$.

#### Solution X.2.10 — An involution on a common invariant domain

Write $A^\dagger=A^*|_{\mathcal M}$. For $x,y\in\mathcal M$,
$\langle Ax,y\rangle=\langle x,A^\dagger y\rangle$.
Reversing the identity shows $\mathcal M\subseteq
\operatorname{dom}(A^\dagger)^*$ and
$(A^\dagger)^*x=Ax$ there. Thus $A^\dagger$ belongs to the same class
and $(A^\dagger)^\dagger=A$. The pairing also gives
$(\alpha A+\beta B)^\dagger=\bar\alpha A^\dagger+
\bar\beta B^\dagger$ and $(AB)^\dagger=B^\dagger A^\dagger$.
All products here have domain $\mathcal M$; its invariance ensures they
are defined. Density gives uniqueness of the representing vectors.

### §3. Cayley transforms

#### Solution X.3.1 — Fixed vectors of a partial isometry

If $Ux=x$, equality of norms forces $x$ into the initial space,
so $U^*x=U^*Ux=x$. Applying the same reasoning to $U^*$ proves
$\ker(I-U)=\ker(I-U^*)$. The identities
$\overline{\operatorname{ran}(I-U)}^\perp=\ker(I-U^*)$ and its
adjoint version now give all four equivalences.

#### Solution X.3.2 — Density on the initial space

For $m\in M$, $(I-U^*)Um=Um-m$, so
$(I-U^*)N=-(I-U)M$. Their density conditions are identical.
Also $[(I-U)M]^\perp=\ker(P_M(I-U^*))
=\ker(U^*U-U^*)$, since $P_MU^*=U^*$.
Similarly $[(I-U^*)N]^\perp=\ker(UU^*-U)$.
Taking zero orthogonal complements proves the remaining equivalences.

#### Solution X.3.3 — No fixed vectors does not suffice

On $\mathbb C^2$ let $Ue_1=e_2$, $Ue_2=0$. This is a partial isometry
with initial space $\mathbb Ce_1$ and has no fixed vector, since
$U^2=0$. But $(I-U)M=\mathbb C(e_1-e_2)$ is not dense in $\mathbb C^2$.

#### Solution X.3.4 — A bounded expression for the Cayley transform

Here $B=(I+A^*A)^{-1}$ and $C=AB$. Since $B$ is injective and
$A+i$ is injective, $C+iB=(A+i)B$ is injective. For any $h$,
$(C+iB)h\in\operatorname{ran}(A+i)$, and the Cayley transform $U$
satisfies $U(C+iB)h=(A-i)Bh=(C-iB)h$.
Thus $U$ extends the displayed expression on
$\operatorname{ran}(C+iB)$; no assertion that this range is all of $H$
is needed.

#### Solution X.3.5 — Diagonal Cayley transforms

The transform is the diagonal unitary
$Ue_n=(\alpha_n-i)(\alpha_n+i)^{-1}e_n$.
Its entries have modulus one and are never one. Moreover
$(A+i)^{-1}e_n=(\alpha_n+i)^{-1}e_n$ is bounded, with range exactly
$\operatorname{dom}A$, so the expression has domain all of $H$.

#### Solution X.3.6 — Multiplication Cayley transforms

For real $\phi$, $(A+i)^{-1}=M_{1/(\phi+i)}$, bounded with range
$\operatorname{dom}A$. Thus $U=M_{(\phi-i)/(\phi+i)}$ on all of
$L^2(\mu)$, a unitary multiplication operator. The pointwise inverse
Cayley formula recovers $\phi$ with its maximal multiplication domain.

#### Solution X.3.7 — The unilateral shift

$\ker(I-S^*)=0$, because a constant square-summable sequence is zero.
Thus $(I-S)H$ is dense. Theorem 3.1 gives
$\operatorname{dom}A=(I-S)\ell^2$ and
$A((I-S)x)=i(I+S)x$. More explicitly, if $y=(I-S)x$, then
$x_n=\sum_{j=0}^ny_j$; the domain consists of the $y\in\ell^2$
whose partial-sum sequence lies in $\ell^2$, and
$(Ay)_n=i(x_n+x_{n-1})$, with $x_{-1}=0$.
The initial space of $S$ is all of $H$ and its final space has codimension
one, so this closed symmetric operator has indices $(0,1)$.

#### Solution X.3.8 — The backward shift

The initial space of $S^*$ is $M=e_0^\perp$ and its final space is $H$.
Since $(I-S^*)Sx=-(I-S)x$, $(I-S^*)M$ is dense.
Thus it too is a Cayley transform:
$\operatorname{dom}A=(I-S^*)M$ and
$A((I-S^*)x)=i(I+S^*)x$ for $x\in M$.
These formulas determine the domain as well as the action, and the
indices are $(1,0)$ by Theorem 3.1.

### §4. Unbounded spectral calculus

#### Solution X.4.1 — Products and their domains

Put $T_\phi=\int\phi\,dE$ and
$\mu_h(\Delta)=\langle E(\Delta)h,h\rangle$. Bounded truncations on
$F_n=\{|\phi|\leq n,|\psi|\leq n\}$ increase strongly to $I$.
The bounded calculus there gives all algebraic identities. In particular,
$\|T_\phi h\|^2=\int|\phi|^2\,d\mu_h$, by norm convergence of the
truncations, and
$d\mu_{T_\psi h}=|\psi|^2d\mu_h$ when $h\in\mathcal D_\psi$.
It follows directly that
$\operatorname{dom}(T_\phi T_\psi)=\mathcal D_\psi\cap
\mathcal D_{\phi\psi}$, with action $T_{\phi\psi}h$ there.

For the adjoint, bounded truncations first give
$T_{\bar\phi}\subseteq T_\phi^*$. Conversely if $T_\phi^*y=g$,
testing on $E(\{|\phi|\leq n\})H$ gives
$T_{\bar\phi}E(\{|\phi|\leq n\})y=E(\{|\phi|\leq n\})g$.
The squared norm bound and monotone convergence imply
$\int|\phi|^2d\mu_y<\infty$, proving equality. Applying the product
formula to $\bar\phi,\phi$ gives
$T_\phi^*T_\phi=T_{|\phi|^2}$: integrability of $|\phi|^4$ implies
that of $|\phi|^2$ because $\mu_h$ is finite.

Part (c) as printed needs a domain correction. For bounded $\psi$,
$T_\phi T_\psi=T_{\phi\psi}$, but in general only
$T_\psi T_\phi\subseteq T_{\phi\psi}$; its domain is
$\mathcal D_\phi$. For instance $\psi=0$ and unbounded $T_\phi$
make the left product defined only on $\mathcal D_\phi$, while
$T_0$ is defined everywhere. The closure of the restricted product does
equal $T_{\phi\psi}$: truncate a vector in its maximal domain to
$\{|\phi|\leq n\}$ and use dominated convergence in its graph norm.

#### Solution X.4.2 — Symmetric and normal means self-adjoint

For a closed normal operator, $\operatorname{dom}A=\operatorname{dom}A^*$
(as follows also from the norm formula for its spectral integral).
Symmetry gives $A\subseteq A^*$. Equality of domains therefore upgrades
the inclusion to equality of operators.

#### Solution X.4.3 — The spectral norm identity

For $h\in\mathcal D_\phi$ let $h_n=E(\{|\phi|\leq n\})h$.
The bounded spectral calculus gives
$\|T_\phi h_n\|^2=\int_{|\phi|\leq n}|\phi|^2\,d\mu_h$.
The integrability defining $\mathcal D_\phi$ makes $T_\phi h_n$
a norm-convergent sequence, with limit $T_\phi h$. Monotone convergence
of the right side proves the claimed identity.

#### Solution X.4.4 — The essential range relative to a spectral measure

The answer is the closed set
$K=\{\lambda:E(\{|\phi-\lambda|<\varepsilon\})\ne0
\text{ for every }\varepsilon>0\}$.
If $\lambda\notin K$, the function $1/(\phi-\lambda)$ is essentially
bounded relative to $E$; its integral is a bounded inverse whose range
is the domain of $T_\phi$. If $\lambda\in K$, choose a unit vector
in $E(\{|\phi-\lambda|<1/n\})H$. These vectors belong to the domain
and satisfy $\|(T_\phi-\lambda)h_n\|\leq1/n$, excluding a bounded
inverse. This proves $\sigma(T_\phi)=K$ without assuming bounded $\phi$.

#### Solution X.4.5 — The annulus endpoints require correction

The slices in the proof are $P_n=P((1/(n+1),1/n])$. Consequently the
radial support of $E_n$ is
$\{z:n-1\leq|z|^2<n\}$: the upper endpoint has zero measure but the
lower endpoint is allowed. Thus $E_n(\Delta_{n+1})=0$, whereas the
asserted $E_n(\Delta_{n-1})=0$ need not hold for the closed annuli
printed in the proof. For $n\geq2$, take $N=\sqrt{n-1}\,I$.
Then $B=I/n$, $P_n=I$, and
$E_n(\Delta_{n-1})=I$, a counterexample.
Use instead the half-open annuli
$\widetilde\Delta_n=\{z:n-1\leq|z|^2<n\}$; they are disjoint and
$E_n(\widetilde\Delta_m)=0$ for every $m\ne n$.
The endpoint assertion follows from the bounded calculus
$B|_{H_n}=(I+N_n^*N_n)^{-1}$ and the corresponding spectral projections.

#### Solution X.4.6 — Moment bounds do not give the proposed lower support

The forward inclusion follows immediately from
$\|N^nh\|^2=\int|z|^{2n}\,d\mu_h$. The reverse inclusion is false.
Take $a=1,b=2$, $N=\operatorname{diag}(0,2)$ and
$h=(\sqrt3/2,1/2)$. Then $\|h\|=1$ and
$\|N^nh\|=2^{n-1}$ for every $n\geq1$, which lies between $1$ and
$2^n$, yet $h\notin E(\{1\leq|z|\leq2\})H$.
The upper bound alone does imply support in $|z|\leq b$: positive mass
on $|z|\geq b+\varepsilon$ would violate it for large $n$.
A correct two-sided characterization adds the inverse moment bounds
$\int|z|^{-2n}\,d\mu_h\leq a^{-2n}\|h\|^2$ for every $n$, with
$|0|^{-2n}=+\infty$. The same argument excludes mass on $|z|<a$.
Together with the upper bounds these conditions are equivalent to the
annular spectral support. Ordinary lower bounds on positive moments
cannot replace the inverse moment conditions.

#### Solution X.4.7 — Polar decomposition with domains

By X.2.8, $A^*A$ is positive self-adjoint. Define
$|A|=(A^*A)^{1/2}$ by the spectral calculus. Then
$\operatorname{dom}|A|=\operatorname{dom}A$ and
$\||A|x\|=\|Ax\|$. Here is the domain justification: on
$\operatorname{dom}A^*A$ the norm identity follows by taking inner
products. This domain is a core for $A$: if $x$ is graph-orthogonal to
it, test against $Bf$ from X.1.11 to get
$0=\langle x,Bf\rangle+\langle Ax,ABf\rangle=\langle x,f\rangle$
for every $f$. It is also a core for $|A|$, by spectral truncation.
The two graph-norm completions therefore agree.

Define $V(|A|x)=Ax$ on $\operatorname{ran}|A|$. The norm identity
makes this well defined and isometric. Extend it to its closure and
set it zero on $\ker|A|=\ker A$. Then $V$ is a partial isometry with
initial space $(\ker A)^\perp$, final space
$\overline{\operatorname{ran}A}$, and $A=V|A|$ on their common domain.
These initial and final spaces and the identity determine $V$ uniquely.
Also $A^*=|A|V^*$ on
$\{y:V^*y\in\operatorname{dom}|A|\}$, by the adjoint pairing.

#### Solution X.4.8 — Exponentiating a self-adjoint operator

Its spectral measure is supported on $\mathbb R$. The bounded function
$e^{it}$ has modulus one, so the bounded spectral calculus gives
$(e^{iA})^*=e^{-iA}$ and both products equal $I$.
Thus the exponential is an everywhere defined unitary even when $A$
is unbounded.

#### Solution X.4.9 — Unbounded Fuglede–Putnam

Let $Q_n$ and $P_m$ be the spectral projections of $N$ and $M$ on the
disks of radii $n,m$. Their restrictions $N_n,M_m$ are bounded normal
operators. The hypothesis implies
$M_m(P_mAQ_n)=(P_mAQ_n)N_n$ as operators from $Q_nH$ to $P_mH$.
The bounded Fuglede–Putnam theorem (apply the commuting version to a
block diagonal operator) gives
$M_m^*P_mAQ_n=P_mAQ_nN_n^*$.
For fixed $x\in Q_nH$, the right side converges to $AN^*x$ as
$m\to\infty$, while $P_mAx\to Ax$. Closedness of $M^*$ implies
$Ax\in\operatorname{dom}M^*$ and $M^*Ax=AN^*x$.
Finally for any $x\in\operatorname{dom}N^*$, $Q_nx\to x$ and
$N^*Q_nx\to N^*x$. Another application of closedness proves
$AN^*\subseteq M^*A$, including its domain assertion.

#### Solution X.4.10 — The cyclic scalar model

Let $\mu(\Delta)=\langle E(\Delta)e_0,e_0\rangle$.
For bounded simple $f$ define $Vf=f(N)e_0$. The norm formula makes
$V$ an isometry from the simple functions in $L^2(\mu)$ into $H$,
so it extends isometrically to all of $L^2(\mu)$.
The assumed domains of $e_0$ give every mixed polynomial in $L^2(\mu)$,
and truncating it shows $V(z^l\bar z^k)=N^{*k}N^le_0$.
Star-cyclicity makes the range of $V$ dense, hence all of $H$.
In addition $VE_\mu(\Delta)=E(\Delta)V$, first on simple functions
and then by continuity. Integrating $|z|^2$ proves
$V\operatorname{dom}N_\mu=\operatorname{dom}N$ and $VN_\mu=NV$.
Thus $W=V^{-1}$ has all the required properties, including $We_0=1$.
The polynomial images are dense, so polynomials themselves are dense
in the scalar model as asserted in Example 4.17.

#### Solution X.4.11 — Equivalence of scalar spectral types

If the measures are equivalent, let $r=d\mu_1/d\mu_2$.
$Vf=\sqrt r\,f$ is a unitary $L^2(\mu_1)\to L^2(\mu_2)$,
commuting with multiplication by $z$ and preserving its maximal domain.
Conversely an intertwining unitary intertwines the spectral measures,
by uniqueness of the normal spectral resolution. For the scalar model,
$E_j(\Delta)=0$ if and only if $\mu_j(\Delta)=0$ (use the indicator
of $\Delta$, since the measure is finite). The two measures therefore
have exactly the same null sets. The argument works for arbitrary finite
measures, whether or not polynomials are dense.

#### Solution X.4.12 — A multiplication model on a separable space

Choose a countable dense sequence. Generate a cyclic reducing subspace
from its first vector by all spectral projections. Project the next
vector onto the orthogonal complement and repeat, omitting zero vectors.
The resulting mutually orthogonal subspaces exhaust $H$, since every
vector of the dense sequence is included at its stage. On each subspace
with cyclic vector $e_j$, the simple-function isometry in X.4.10 gives
a model $L^2(\mu_j)$ with finite measure
$\mu_j(\Delta)=\langle E(\Delta)e_j,e_j\rangle$; polynomial cyclicity
is unnecessary for this construction. Take the disjoint union of these
copies of $\mathbb C$, with measure equal to $\mu_j$ on copy $j$,
and set $\phi(j,z)=z$. This measure is sigma-finite. The direct-sum
unitary carries the operator domain to
$\{f:\sum_j\int|z f_j|^2d\mu_j<\infty\}$, exactly the domain of
$M_\phi$. Thus it intertwines the unbounded operators, not just their
bounded truncations.

### §5. One-parameter unitary groups

#### Solution X.5.1 — Weak continuity becomes strong continuity

For every $h$,
$\|(U(t)-U(s))h\|^2=2\|h\|^2-
2\operatorname{Re}\langle U(t)h,U(s)h\rangle$.
WOT continuity makes the last inner product tend to $\|h\|^2$ as
$t\to s$, so the norm tends to zero. This proves SOT continuity at
every $s$.

#### Solution X.5.2 — Explicit smooth averaging functions

The parameter must be a positive integer. Let
$\eta(t)=c\exp(-1/(t(1-t)))$ for $0<t<1$ and zero otherwise,
where $c$ makes $\int\eta=1$. Repeated differentiation shows that
all derivatives tend to zero at the endpoints: every term is a
polynomial in $1/t,1/(1-t)$ times the exponentially decaying factor.
Thus $\eta$ is smooth and compactly supported. Set
$\phi_n(t)=n\eta(nt)$ for $n\geq1$.
Then $\phi_n,\phi_n'\in L^1$, its support is in $[0,1/n]$, and its
integral is one by substitution. For $n\leq0$ the printed condition
is undefined or impossible, so “every integer” means every positive one.

#### Solution X.5.3 — Symmetry of the generator

For $h,g$ in its domain, unitarity gives
$\langle(U(t)-I)h,g\rangle=\langle h,(U(-t)-I)g\rangle$.
Divide by $t$, multiply in the first variable by $-i$, and let $t\to0$.
Conjugate linearity in the second variable and the change from $t$ to
$-t$ cancel the signs, yielding $\langle Ah,g\rangle=\langle h,Ag\rangle$.
The averaging functions from X.5.2 give the dense domain, as in the
text, so this proves the claimed symmetric operator.

#### Solution X.5.4 — Integrated group operators

Here $T_\phi=\int_0^\infty\phi(t)U(t)\,dt$ and
$S_\phi=\int_0^\infty\phi(t)U(-t)\,dt$, interpreted strongly.
The estimate $\|T_\phi h\|\leq\|\phi\|_1\|h\|$ justifies taking
adjoints in scalar pairings and gives $T_\phi^*=S_{\bar\phi}$.
Fubini is justified by the bound
$|\phi(s)\psi(t)|\|h\|$, integrable on the quadrant.
The group law and the substitution $r=s+t$ yield
$T_\phi T_\psi=T_{\phi*\psi}$ and $S_\phi S_\psi=S_{\phi*\psi}$,
where the half-line convolution is $\int_0^r\phi(t)\psi(r-t)dt$.
Finally $T_\phi$ commutes with every $U(t)$. For
$h\in\operatorname{dom}A$, apply the bounded operator $T_\phi$ to
the difference quotients defining $Ah$. Their norm limit proves that
$T_\phi h\in\operatorname{dom}A$ and $AT_\phi h=T_\phi Ah$.

#### Solution X.5.5 — Eigenvectors of a group element

If $Ae=\lambda e$, the spectral measure of $e$ is concentrated at
$\lambda$, and $U(t)e=e^{it\lambda}e$ for every $t$.
Conversely suppose $U(t_0)e=\zeta e$, $t_0\ne0$.
Then $|\zeta|=1$ and the measure of $e$ is supported on the countable
set $\{(\theta+2\pi k)/t_0:k\in\mathbb Z\}$, where
$\zeta=e^{i\theta}$. At least one atom is nonzero. The nonzero vectors
$E(\{\lambda_k\})e$ are eigenvectors of $A$ and of every $U(s)$.
Thus $A$ and all $U(s)$ have eigenvectors. The original $e$ need not
be an eigenvector of $A$, or even belong to its domain: it may be an
infinite sum of these orthogonal eigenvectors with an infinite second
moment. Nor must $e$ be an eigenvector of each $U(s)$.

#### Solution X.5.6 — Norm continuity forces a bounded generator

Norm continuity at zero and the group law imply norm continuity
everywhere. Therefore
$\|t^{-1}\int_a^{a+t}U(s)ds-U(a)\|
\leq\sup_{|s-a|\leq|t|}\|U(s)-U(a)\|\to0$.
Choose a small fixed $a>0$ so that
$V=\int_0^aU(s)ds$ is invertible: $\|a^{-1}V-I\|<1$.
The group law gives
$(U(t)-I)V=\int_a^{a+t}U(s)ds-\int_0^tU(s)ds$.
Divide by $t$ and use the established norm limits to get
$(U(t)-I)/t\to(U(a)-I)V^{-1}$ in operator norm.
Thus the generator is the everywhere defined bounded operator
$-i(U(a)-I)V^{-1}$, by its defining difference quotient.

### §6. Fourier analysis

#### Solution X.6.1 — A core for differentiation

Choose smooth cutoffs $\chi_R(x)=\chi(x/R)$, with $\chi=1$ on
$[-1,1]$ and supported in $[-2,2]$. Then $\chi_R f\to f$ in $L^2$
and $(\chi_Rf)'=\chi_R f'+\chi_R'f\to f'$ in $L^2$;
the extra term is bounded by $\|\chi'\|_\infty\|f\|_2/R$.
For fixed $R$, convolve with a smooth compactly supported mollifier
of total mass one. Translation continuity in $L^2$ implies convergence
of both the function and its weak derivative, since differentiation
commutes with this convolution. The mollifications are smooth and
compactly supported. Choosing their scales small enough for $R=n$
gives the required sequence in $C_c^{(1)}$.

#### Solution X.6.2 — Completeness of Schwartz space

Write $p_{m,n}(f)=\sup_x|x^mf^{(n)}(x)|$. These countably many
seminorms separate points and define the translation-invariant metric
$\sum_{m,n\geq0}2^{-m-n-2}\min(1,p_{m,n}(f-g))$.
A Cauchy sequence has uniformly Cauchy derivatives of every order.
Let their uniform limits be $g_n$. The fundamental theorem of calculus
on compact intervals gives $g_n'=g_{n+1}$; hence $g_0$ is smooth.
For every $m,n$, uniform convergence of $x^mf_j^{(n)}$ shows its limit
is $x^mg_n$, which is bounded. Thus $g_0\in\mathcal S$ and the sequence
converges in every seminorm. This proves completeness, metrizability,
and local convexity, the defining properties of a Fréchet space.

#### Solution X.6.3 — Rapid decay and polynomial weights

If $f\in\mathcal S$, then for $|x|\geq1$,
$|x^mf^{(n)}(x)|\leq p_{m+1,n}(f)/|x|\to0$.
Linearity gives decay for every polynomial. Conversely the stated
limits make each $x^mf^{(n)}(x)$ bounded outside a compact interval;
continuity bounds it inside. Every Schwartz seminorm is therefore finite.

#### Solution X.6.4 — The convolution bound

Use the section's normalized convolution
$(f*g)(x)=(2\pi)^{-1/2}\int f(x-t)g(t)dt$ and
$\|g\|_1=(2\pi)^{-1/2}\int|g|$.
For $1\leq p<\infty$, Minkowski's integral inequality and translation
invariance give
$\|f*g\|_p\leq(2\pi)^{-1/2}\int|g(t)|\|f(\cdot-t)\|_pdt
=\|f\|_p\|g\|_1$.
One can obtain this integral inequality first for simple functions by
the triangle inequality in $L^p$, then by approximation and Fatou's
lemma; Tonelli ensures absolute integrability almost everywhere where
needed. For $p=\infty$, the pointwise bound outside a null set gives
the same inequality directly. With ordinary unnormalized convolution,
the identical proof uses the ordinary $L^1$ norm.

#### Solution X.6.5 — Approximate identities in norm and weak-star topology

Substitution gives
$f*\psi_\varepsilon-f=(2\pi)^{-1/2}\int\psi(t)
[f(\cdot-\varepsilon t)-f]dt$.
For $p<\infty$ translations are norm continuous (first for compactly
supported continuous functions, then by density). Minkowski followed
by dominated convergence, with bound $2\|f\|_p|\psi(t)|$, gives
norm convergence. For $f\in L^\infty$ and a test $g\in L^1$, Fubini
moves the translations onto $g$; their $L^1$ continuity gives
$\int(f*\psi_\varepsilon-f)g\to0$ by the same dominated convergence
argument. This is weak-star convergence, not generally norm convergence.

#### Solution X.6.6 — Integrable transform inversion

Let $g(x)=(2\pi)^{-1/2}\int\hat f(t)e^{ixt}dt$, a bounded continuous
function. Multiply the integrand by $e^{-\varepsilon t^2/2}$.
Fubini, justified by $f\in L^1$ and the integrable Gaussian, identifies
this inverse integral with $f*k_\varepsilon$, where
$k_\varepsilon(x)=\varepsilon^{-1/2}e^{-x^2/(2\varepsilon)}$
has normalized integral one. The approximate-identity argument makes
$f*k_\varepsilon\to f$ in $L^1$. On the other hand
$\hat f\in L^1$ makes the inverse integrals converge uniformly to $g$
by dominated convergence. An $L^1$-convergent subsequence converges
almost everywhere, so $f=g$ almost everywhere, as claimed.

#### Solution X.6.7 — Reflection and the inverse transform

On $\mathcal S$, Fourier inversion gives
$\mathcal F^{-1}f(x)=\mathcal Ff(-x)$. Both sides define bounded
operators on $L^2$: Plancherel gives the two transforms, and reflection
preserves the $L^2$ norm. Density of $\mathcal S$ extends their equality
to every $L^2$ vector. Pointwise notation here denotes equality of
$L^2$ equivalence classes, not an absolutely convergent integral in general.

#### Solution X.6.8 — The fourth power of the Fourier transform

Let $Rf(x)=f(-x)$. The preceding identity and commutation of reflection
with $\mathcal F$ imply $\mathcal F^2=R$ and $\mathcal F^4=I$.
A nonzero odd Schwartz function has $Rf=-f$, so $\mathcal F^2\ne I$.
Polynomial spectral mapping gives
$\sigma(\mathcal F)\subseteq\{1,-1,i,-i\}$.
In fact equality holds: the Hermite functions in X.6.9 give nonzero
eigenvectors for each of these four values.

#### Solution X.6.9 — Hermite functions, rather than bare polynomials

Nonzero polynomials are neither $L^1(\mathbb R)$ nor $L^2(\mathbb R)$,
so their Fourier transforms do not exist in the spaces used in this
section. The classical intended calculation concerns Hermite functions.
With the physicists' convention
$H_n(x)=(-1)^ne^{x^2}(d/dx)^ne^{-x^2}$, set
$h_n(x)=H_n(x)e^{-x^2/2}$. The Gaussian integral gives
$\mathcal Fh_0=h_0$. The recurrence
$h_{n+1}=(x-d/dx)h_n$ follows by differentiation of the definition.
Integration by parts on Schwartz functions gives
$\mathcal F(xf)=i(\mathcal Ff)'$ and
$\mathcal F(f')=ix\mathcal Ff$; hence
$\mathcal F((x-D)f)=-i(x-D)\mathcal Ff$.
Induction yields $\mathcal Fh_n=(-i)^nh_n$.
If one extends the transform to tempered distributions, bare
polynomials instead satisfy
$\mathcal F(x^n)=\sqrt{2\pi}\,i^n\delta_0^{(n)}$;
linearity then gives the distributional transform of any $H_n$.
That extension is a different meaning of “Fourier transform.”

### §7. Moment problems

#### Solution X.7.1 — The Stieltjes moment problem

(a) implies (b) by integrating $|p(t)|^2$ and $t|p(t)|^2$.
For (b), define $L(t^n)=m_n$ and the polynomial inner product
$\langle p,q\rangle=L(p\bar q)$, quotient its null space, and complete.
Cauchy–Schwarz for this positive form shows that a null polynomial
$p$ satisfies $L(p\bar q)=0$ for every polynomial $q$; taking
$q=t^2p$ shows that multiplication by $t$ respects the null space.
It defines a densely defined symmetric operator $S[p]=[tp]$.
The second positivity condition makes $S$ nonnegative.

We need a nonnegative self-adjoint extension, not an arbitrary one.
Here is the required form construction. On $\operatorname{dom}S$
complete the norm
$\|x\|_q^2=\|x\|^2+\langle Sx,x\rangle$ to obtain a Hilbert space $Q$.
Its inclusion $j:Q\to H$ is injective: if a form-Cauchy sequence $x_n$
tends to zero in $H$, its form limit is orthogonal to every
$y\in\operatorname{dom}S$, since
$\langle x_n,y\rangle_q=\langle x_n,y+Sy\rangle\to0$.
Density in $Q$ then makes that limit zero. Set $B=jj^*$ on $H$.
It is a positive injective contraction with dense range. The spectral
calculus defines the nonnegative self-adjoint operator $T=B^{-1}-I$.
For $x\in\operatorname{dom}S$, the pairing above gives
$j^*(I+S)x=x$ in $Q$, hence $B(I+S)x=x$ in $H$.
Thus $T$ extends $S$.

Take $e=[1]$. Since $T$ agrees with multiplication on all polynomials,
$e\in\operatorname{dom}T^n$ and
$\langle T^ne,e\rangle=m_n$. This proves (c).
Finally (c) gives (a) using
$\mu(\Delta)=\langle E_T(\Delta)e,e\rangle$ on $[0,\infty)$.
Its moments are finite by the stated power domains and Cauchy–Schwarz;
the spectral norm and pairing formulas give exactly $m_n$.

#### Solution X.7.2 — Bochner's representation

(a) implies continuity by dominated convergence and positivity by
integrating $|\sum_j\alpha_je^{it_jx}|^2$.
For (b), give finite sums of formal symbols $\delta_t$ the form
$\langle\delta_s,\delta_t\rangle=m(s-t)$, quotient the null space,
and complete. Positivity ensures a Hermitian form and Cauchy–Schwarz,
so the quotient is valid. Translation $U(a)\delta_t=\delta_{t+a}$
preserves the form and has inverse $U(-a)$; it extends to a unitary.
Moreover
$\|(U(a)-I)\delta_t\|^2=2m(0)-2\operatorname{Re}m(a)\to0$.
Finite sums and the common norm bound extend this to strong continuity
on the completion. With $e=\delta_0$ we get (c).
For (c), Stone's theorem supplies $U(t)=e^{itA}$; its scalar spectral
measure at $e$ is finite and satisfies (a). If $m(0)=0$, the positivity
inequality forces $m=0$, covered by the zero measure and zero vector.

#### Solution X.7.3 — Moments on the unit circle

Integrating $|\sum_j\alpha_jz^j|^2$ gives (a) implies (b).
For the converse construct a Hilbert space from Laurent polynomials
with $\langle z^j,z^k\rangle=m_{j-k}$, quotienting null vectors and
completing as above. Multiplication by $z$ preserves this form and has
inverse multiplication by $z^{-1}$, so it extends to a unitary $U$.
For $e=[1]$, $\langle U^ne,e\rangle=m_n$ for all integers $n$,
proving (c). Its unit-circle spectral measure at $e$ proves (a).
The total mass is $m_0$, and the zero case is handled as in X.7.2.

#### Solution X.7.4 — Cyclicity in the Hamburger construction

In the proof of Theorem 7.1, let $e$ be the class of $(1,0,0,\ldots)$.
The initial shift $T$ satisfies $T^ne=[t^n]$. Every chosen self-adjoint
extension $A$ agrees with $T$ on the polynomial domain, which is
$T$-invariant. Inductively $e\in\operatorname{dom}A^n$ and
$A^ne=[t^n]$ for every $n$. Finite linear combinations of these classes
are exactly the dense quotient space used to construct $H$.
Thus $e$ is a cyclic vector for $A$.

<!-- END SOLUTIONS X -->
