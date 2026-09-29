# XI. Fredholm Theory

<!-- OCR draft; page images require independent visual review. -->


<a id="pdf-page-362"></a>
# CHAPTER XI

# Fredholm Theory

This chapter is entirely independent of the preceding one and only tangentially dependent on Chapters VIII and IX.

The purpose of this chapter is to study certain properties of operators on a Hilbert space that are invariant under compact perturbations. That is, we want to study properties of an operator $A$ in $\mathcal{B}(\mathcal{H})$ that are also possessed by $A+K$ for every $K$ in $\mathcal{B}_0(\mathcal{H})$. The correct view here is to consider this undertaking as a study of the quotient algebra $\mathcal{B}(\mathcal{H})/\mathcal{B}_0(\mathcal{H})=\mathcal{B}/\mathcal{B}_0$—the *Calkin algebra*. Any property associated with an element of the Calkin algebra is a property associated with a coset of operators and vice versa. It is useful—indeed essential—to relate these properties to the way in which the operators act on the underlying Hilbert space.

## §1. The Spectrum Revisited

In Section VII.6 we saw several properties of the spectrum of an operator on a Banach space. In particular, the concepts of point spectrum, $\sigma_p(A)$, and approximate point spectrum, $\sigma_{ap}(A)$, were explored. It was also shown (VII. 6.7) that $\partial\sigma(A)\subseteq\sigma_{ap}(A)$. Recall that $\sigma_l(A)$ is the left spectrum of $A$ and $\sigma_r(A)$ is the right spectrum of $A$.

**1.1. Proposition.** *If $A\in\mathcal{B}(\mathcal{H})$, the following statements are equivalent.*

(a) $\lambda\notin\sigma_{ap}(A)$; that is, $\inf\{\|(A-\lambda)h\|:\|h\|=1\}>0$.

(b) $\operatorname{ran}(A-\lambda)$ is closed and $\dim\ker(A-\lambda)=0$.

(c) $\lambda\notin\sigma_l(A)$.



<a id="pdf-page-363"></a>
(d) $\bar{\lambda}\notin\sigma_r(A^*)$.

(e) $\operatorname{ran}(A^*-\bar{\lambda})=\mathcal H$.

**Proof.** By Proposition VII.6.4, (a) and (b) are equivalent. Also, if $B\in\mathcal B(\mathcal H)$, then $B(A-\lambda)=1$ if and only if $(A^*-\bar{\lambda})B^*=1$ so that (c) and (d) are easily seen to be equivalent.

*(b) implies (c).* Let $\mathcal M=\operatorname{ran}(A-\lambda)$ and define $T:\mathcal H\to\mathcal M$ by $Th=(A-\lambda)h$; then $T$ is bijective. By the Open Mapping Theorem, $T^{-1}:\mathcal M\to\mathcal H$ is continuous. Define $B:\mathcal H\to\mathcal H$ by letting $B=T^{-1}$ on $\mathcal M$ and $B=0$ on $\mathcal M^\perp$. Then $B\in\mathcal B(\mathcal H)$ and $B(A-\lambda)=1$. (Note that we used a property of Hilbert spaces here; see Exercise VII.6.5.)

*(d) implies (e).* Since $\bar{\lambda}\notin\sigma_r(A^*)$, there is an operator $C$ in $\mathcal B(\mathcal H)$ such that $(A^*-\bar{\lambda})C=1$. Hence $\mathcal H=(A^*-\bar{\lambda})C\mathcal H\subseteq\operatorname{ran}(A^*-\bar{\lambda})$.

*(e) implies (a).* Let $\mathcal N=\ker(A^*-\bar{\lambda})^\perp$ and define $T:\mathcal N\to\mathcal H$ by $Th=(A^*-\bar{\lambda})h$. Then $T$ is bijective and hence invertible. Let $C:\mathcal H\to\mathcal H$ be defined by $Ch=T^{-1}h$. Then $C\mathcal H=\mathcal N$ and $(A^*-\bar{\lambda})C=1$. Thus $C^*(A-\lambda)=1$ so that if $h\in\mathcal H$, $\|h\|=\|C^*(A-\lambda)h\|\leq\|C^*\|\|(A-\lambda)h\|$. Hence $\inf\{\|(A-\lambda)h\|:\|h\|=1\}\geq\|C^*\|^{-1}$. $\blacksquare$

If $\Delta\subseteq\mathbb C$, $\Delta^*\equiv\{\bar{\lambda}:\lambda\in\Delta\}$.

**1.2. Corollary.** *If $A\in\mathcal B(\mathcal H)$, then $\partial\sigma(A)\subseteq\sigma_l(A)\cap\sigma_r(A)=\sigma_{ap}(A)\cap\sigma_{ap}(A^*)^*$.*

**Proof.** The equality is immediate from the preceding theorem. In fact, $\sigma_l(A)=\sigma_{ap}(A)$ and $\sigma_r(A)=\sigma_l(A^*)^*=\sigma_{ap}(A^*)^*$. If $\lambda\in\partial\sigma(A)$, then (VII.6.7) $\lambda\in\sigma_{ap}(A)$. But $\bar{\lambda}\in\partial\sigma(A^*)$ so that $\bar{\lambda}\in\sigma_{ap}(A^*)$. $\blacksquare$

For normal elements there is less variety. The pertinent result is proved here in a more general setting than that of operators.

**1.3. Proposition.** *Let $\mathcal A$ be a $C^*$-algebra with identity. If $a$ is a normal element of $\mathcal A$, then the following statements are equivalent.*

(a) $a$ is invertible.

(b) $a$ is left invertible.

(c) $a$ is right invertible.

**Proof.** Assume that $a$ is left invertible, so there is a $b$ in $\mathcal A$ such that $ba=1$. Thus for any $x$ in $\mathcal A$, $\|x\|=\|bax\|\leq\|b\|\|ax\|$, and hence $\|ax\|\geq\|b\|^{-1}\|x\|$. In particular, this is true whenever $x\in C^*(a)$. Because $a$ is normal, $C^*(a)$ is isomorphic to $C(K)$ where $K=\sigma(a)$ and where the isomorphism takes $a$ into the function $z$ ($z(w)=w$). The inequality above thus becomes: $\|zf\|\geq\|b\|^{-1}\|f\|$ for every $f$ in $C(K)$. It must be shown that $0\notin K$ ($=\sigma(a)$). If $0\in K$, then for every integer $n$ there is a function $f_n$ in $C(K)$ such that $0\leq f_n\leq1$, $f_n(0)=1$ and $f_n(z)=0$ for $z$ in $K$ and $|z|\geq n^{-1}$. Since $0\in K$, $\|f_n\|=1$. But $\|zf_n\|\leq1/n$. This contradicts the inequality and so $0\notin\sigma(a)$; that is, $a$ is invertible.

The argument above shows that (b) implies (a). If $a$ is right invertible, then



<a id="pdf-page-364"></a>
$a^*$ is left invertible. By the preceding argument $a^*$ is invertible, and hence so is $a$. ■

**1.4. Proposition.** *If $N$ is a normal operator, then $\sigma(N)=\sigma_r(N)=\sigma_l(N)$. If $\lambda$ is an isolated point of $\sigma(N)$, then $\lambda\in\sigma_p(N)$.*

**Proof.** The first part of the proposition is immediate from the preceding result. If $\lambda$ is an isolated point of $\sigma(N)$ and $N=\int z\,dE(z)$, then $0\neq E(\{\lambda\})\mathcal H=\ker(N-\lambda)$ (Exercise IX.2.1). ■

## Exercises

1. Let $S$ be the unilateral shift of multiplicity 1 on $l^2(\mathbb N)$ and find $\sigma_l(S)$ and $\sigma_r(S)$.

2. The *compression spectrum* of $A$, $\sigma_c(A)$, is defined by $\sigma_c(A)=\{\lambda\in\mathbb C:\operatorname{ran}(A-\lambda)\text{ is not dense in }\mathcal H\}$. Show: (a) $\lambda\in\sigma_c(A)$ if and only if $\bar\lambda\in\sigma_p(A^*)$. (b) $\sigma_c(A)\subseteq\sigma_r(A)$, but this inclusion may be proper. (c) $\sigma_c(A)$ is not necessarily closed. (d) $\sigma(A)=\sigma_{ap}(A)\cup\sigma_c(A)$.

3. If $A\in\mathcal B(\mathcal H)$ and $f\in\operatorname{Hol}(A)$, then $f(\sigma_p(A))\subseteq\sigma_p(f(A))$. If $f$ is not constant on any component of its domain, then $f(\sigma_p(A))=\sigma_p(f(A))$.

4. If $A\in\mathcal B(\mathcal H)$ and $f\in\operatorname{Hol}(A)$, then $f(\sigma_{ap}(A))=\sigma_{ap}(f(A))$.

## §2. Fredholm Operators

We begin with a definition.

**2.1. Definition.** If $\mathcal H$ and $\mathcal H'$ are Hilbert spaces and $A:\mathcal H\to\mathcal H'$ is a bounded operator, then $A$ is said to be *left semi-Fredholm* if there is a bounded operator $B:\mathcal H'\to\mathcal H$ and a compact operator $K$ on $\mathcal H$ such that $BA=1+K$. Analogously, $A$ is *right semi-Fredholm* if there is a such a bounded operator $B$ and a compact operator $K'$ on $\mathcal H'$ such that $AB=1+K'$. $A$ is a *semi-Fredholm operator* if it is either left or right semi-Fredholm and $A$ is a *Fredholm operator* if it is both left and right semi-Fredholm.

Observe that $A$ is left semi-Fredholm if and only if $A^*$ is right semi-Fredholm. Thus results about semi-Fredholm operators will usually only be phrased in terms of left semi-Fredholm operators and the reader will be allowed to make the appropriate statement for right semi-Fredholm operators.

Note that a left invertible operator is left semi-Fredholm. However it is easy to get left semi-Fredholm operators that are not left invertible.

**2.2. Example.** Let $\mathcal H=\mathcal H_0\oplus\mathcal H_1\oplus\cdots$, where $\dim\mathcal H_j=\alpha$ for all $j\geq 0$, and let $S$ be the unilateral shift of multiplicity $\alpha$ with respect to this decomposition. (So $S$ maps $\mathcal H_j$ isometrically onto $\mathcal H_{j+1}$.) Recall that $S^*S=1$ so $S$ is left



<a id="pdf-page-365"></a>
invertible and hence left semi-Fredholm. Also $SS^{*}=1-P_{0}$, where $P_{0}$ is the projection of $\mathcal H$ onto $\mathcal H_{0}$. So $S$ is Fredholm if $\alpha<\infty$.

In the next result, the equivalence of the first three conditions is referred to as Atkinson’s Theorem. The rest of this theorem is from Wolf [1959], Schechter [1968], and Fillmore, Stampfli and Williams [1972].

**2.3. Theorem.** *If $A:\mathcal H\to\mathcal H'$ is a bounded operator, the following statements are equivalent.*

(a) *$A$ is left semi-Fredholm.*

(b) *$\operatorname{ran}A$ is closed and $\dim\ker A<\infty$.*

(c) *There is a bounded operator $B:\mathcal H'\to\mathcal H$ and a finite rank operator $F$ on $\mathcal H$ such that $BA=1+F$.*

(d) *There is no sequence $\{h_n\}$ of unit vectors in $\mathcal H$ such that $h_n\to0$ weakly and $\lim\|Ah_n\|=0$.*

(e) *There is no orthonormal sequences $\{e_n\}$ in $\mathcal H$ such that $\lim\|Ae_n\|=0$.*

(f) *There is a $\delta>0$ such that $\{h\in\mathcal H:\|Ah\|\leq\delta\|h\|\}$ contains no infinite dimensional manifold.*

(g) *If the positive operator $(A^{*}A)^{1/2}=\int_{0}^{\infty}t\,dE(t)$, then there is a $\delta>0$ such that $E[0,\delta]\mathcal H$ is finite dimensional.*

(h) *If $K\in\mathcal B_{0}(\mathcal H)$, then $\dim\ker(A+K)<\infty$.*

**Proof.** (a) implies (b). According to (a) there is a bounded operator $B$ such that $\pi(B)\pi(A)=1$; that is, $\pi(BA-1)=0$. Hence $BA=1+K$ for some compact operator $K$. But $\ker A\subseteq\ker BA=\ker(1+K)$. Since the eigenspaces corresponding to nonzero eigenvalues of compact operators are finite dimensional, $\dim\ker A<\infty$. Also, the Fredholm Alternative (VII.7.9) implies $\operatorname{ran}BA=\operatorname{ran}(K+1)$ is closed. Hence there is a constant $c>0$ such that for $h\perp\ker(BA)$, $\|BAh\|\geq c\|h\|$. Thus if $h\in[\ker BA]^{\perp}$, $c\|h\|\leq\|B\|\|Ah\|$, or $\|Ah\|\geq(c/\|B\|)\|h\|$. This implies that $A([\ker BA]^{\perp})$ is closed. But $\operatorname{ran}A=A([\ker BA]^{\perp})+A(\ker BA)$. Since $A(\ker BA)$ is finite dimensional, $\operatorname{ran}A$ is closed.

(b) implies (c). First define $A_{1}:(\ker A)^{\perp}\to\operatorname{ran}A$ by $A_{1}=A|(\ker A)^{\perp}$ and note that $A_{1}$ is invertible by The Open Mapping Theorem. Let $P$ be the projection of $\mathcal H'$ onto $\operatorname{ran}A$ and define $B:\mathcal H'\to\mathcal H$ by $B=A_{1}^{-1}P$. It is left to the reader to check that $BA=1-F$, where $F$ is the orthogonal projection of $\mathcal H$ onto $\ker A$. Since $\ker A$ is finite dimensional, this establishes (c).

(c) implies (a). This is clear.

(a) implies (d). Suppose $\{h_n\}$ is a sequence of unit vectors in $\mathcal H$ that converges weakly to $0$ and let $B:\mathcal H'\to\mathcal H$ and $K$ be as in the definition of a left semi-Fredholm operator. Since $BA=1+K$, $|1-\|BAh_n\||=|\|h_n\|-\|BAh_n\||\leq\|Kh_n\|$ and $\|Kh_n\|\to0$ since $K$ is compact. Thus $\|BAh_n\|\to1$ and so it is impossible for $\{Ah_n\}$ to converge to $0$ in norm.

(d) implies (e). Orthonormal sequences converge weakly to $0$.

(e) implies (f). If (f) is false, then for every positive integer $n$ there is an infinite dimensional manifold $\mathcal M_n$ such that $\|Ah\|\leq(1/n)\|h\|$ for all $h$ in $\mathcal M_n$.



<a id="pdf-page-366"></a>
Let $e_1$ be a unit vector in $\mathcal M_1$. Suppose $e_1,\ldots,e_n$ are orthonormal vectors such that $e_k\in\mathcal M_k$, $1\leq k\leq n$. Let $E$ be the projection of $\mathcal H$ onto $\bigvee\{e_1,\ldots,e_n\}$. If $\mathcal M_{n+1}\cap[e_1,\ldots,e_n]^\perp=(0)$, then $E$ is injective on $\mathcal M_{n+1}$. Since $\dim\mathcal M_{n+1}=\infty$ and $\dim\operatorname{ran}E<\infty$, this is impossible. Thus there is a unit vector $e_{n+1}$ in $\mathcal M_{n+1}$ such that $e_{n+1}\perp\{e_1,\ldots,e_n\}$. The orthonormal sequence $\{e_n\}$ shows that (e) does not hold.

(f) *implies* (g). Let $|A|=\int t\,dE(t)$ and let $\delta>0$. If $h\in E[0,\delta]\mathcal H$, then

$$
\begin{aligned}
\|Ah\|^2
&=\langle A^*Ah,h\rangle\\
&=\langle |A|^2h,h\rangle\\
&=\int_0^\delta t^2\,dE_{h,h}(t)\leq\delta^2E_{h,h}[0,\delta]\\
&=\delta^2\|h\|^2.
\end{aligned}
$$

So $E[0,\delta]\mathcal H\subseteq\{h:\|Ah\|\leq\delta\|h\|\}$. By (f) there is a $\delta>0$ such that $E[0,\delta)\mathcal H$ is finite dimensional.

(g) *implies* (c). Let $\mathcal M_\delta=\{E[0,\delta]\mathcal H\}^\perp$. Now $|A|$ maps $\mathcal M_\delta$ bijectively onto $\mathcal M_\delta$. In fact, the inverse of $|A|:\mathcal M_\delta\to\mathcal M_\delta$ is $\left(\int_\delta^\infty t^{-1}\,dE(t)\right)|\mathcal M_\delta$. Let $A=U|A|$ be the polar decomposition of $A$. Since $\mathcal M_\delta\subseteq\operatorname{ran}|A|\subseteq\text{initial }U$, $U$ maps $\mathcal M_\delta$ isometrically onto some closed subspace $\mathcal L$ of $\operatorname{ran}A$. Let $V=$ the inverse of $U$ on $\mathcal L$ and $V=0$ on $\mathcal L^\perp$; that is, $V|\mathcal L^\perp=0$ and $V|\mathcal L=(U|\mathcal M_\delta)^{-1}$. Hence $V$ is a partial isometry. Let $B_1=\int_\delta^\infty t^{-1}\,dE(t)$ and put $B=B_1V$. If $h\in\mathcal M_\delta$, then $BAh=B_1VU|A|h=h$. If $h\in\mathcal M_\delta^\perp=E[0,\delta]\mathcal H$, $|A|h\in\mathcal M_\delta^\perp$ and so $U|A|h\perp\mathcal L$; thus $BAh=0$. Hence $BA=E(\delta,\infty)=1-E[0,\delta]$, and $E[0,\delta]$ has finite rank.

(a) *implies* (h). Let $B:\mathcal H'\to\mathcal H$ be a bounded operator such that $BA=1+L$, where $L$ is a compact operator on $\mathcal H$. If $K:\mathcal H\to\mathcal H'$ is any compact operator, then $B(A+K)=1+(L+BK)$ and $L+BK$ is compact. By definition $A+K$ is left semi-Fredholm. Since we have already shown that (a) implies (b), $\dim\ker(A+K)<\infty$.

(h) *implies* (e). Suppose (e) does not hold. So there is an orthonormal sequence, $\{e_n\}$ such that $\|Ae_n\|\to0$. By passing to a subsequence if necessary, it may be assumed that $\sum_{n=1}^\infty\|Ae_n\|^2<\infty$. Thus for any $h$ in $\mathcal H$,

$$
\begin{aligned}
\sum|\langle h,e_n\rangle|\,\|Ae_n\|
&\leq\left[\sum|\langle h,e_n\rangle|^2\right]^{1/2}
\left[\sum\|Ae_n\|^2\right]^{1/2}\\
&\leq C\|h\|,
\end{aligned}
$$

where $C=\left[\sum\|Ae_n\|^2\right]^{1/2}$. Thus $Kh=\sum_{n=1}^\infty\langle h,e_n\rangle Ae_n$ defines a bounded operator. Moreover, if $K_nh=\sum_{j=1}^n\langle h,e_j\rangle Ae_j$, it is easy to see that $\|K_n-K\|\to0$. Thus $K$ is compact. But $(A-K)e_n=0$ for every $n$, so $\dim\ker(A-K)=\infty$. ■

As mentioned previously, the result for right semi-Fredholm operators that is analogous to the preceding theorem is left for the reader to state. We will, however, make explicit part of this result for Fredholm operators.



<a id="pdf-page-367"></a>
**2.4. Corollary.** *A bounded operator $A:\mathcal H\to\mathcal H'$ is Fredholm if and only if $\operatorname{ran}A$ is closed and both $\ker A$ and $\ker A^*$ are finite dimensional.*

In the case of a bounded operator $A$ from a Hilbert space $\mathcal H$ into itself, the concept of a semi-Fredholm operator can be rephrased in terms of the corresponding concept in the Calkin algebra, $\mathcal B/\mathcal B_0$. In fact, this will be the primary situation in which the ideas of Fredholm theory are applied. The next result is immediate from the definition.

**2.5. Proposition.** *For a Hilbert space $\mathcal H$, let $\pi:\mathcal B\to\mathcal B/\mathcal B_0$ be the natural map and let $A\in\mathcal B=\mathcal B(\mathcal H)$. The operator $A$ is left (respectively, right) semi-Fredholm if and only if $\pi(A)$ is left (respectively, right) invertible in the Calkin algebra.*

For notation, let $\mathcal F_\ell=\mathcal F_\ell(\mathcal H)$ and $\mathcal F_r=\mathcal F_r(\mathcal H)$ be the set of left and right semi-Fredholm operators on the Hilbert space $\mathcal H$. So $\mathcal F=\mathcal F_\ell\cap\mathcal F_r$ and $\mathcal{SF}=\mathcal F_\ell\cup\mathcal F_r$ are the sets of Fredholm and semi-Fredholm operators on $\mathcal H$. Since $\mathcal F_\ell=$ the inverse image under $\pi$ of the left invertible elements of the Banach algebra $\mathcal B/\mathcal B_0$, the next proposition is immediate.

**2.6. Proposition.** *Each of the sets $\mathcal F_\ell$, $\mathcal F_r$, $\mathcal F$, and $\mathcal{SF}$ are open subjects of $\mathcal B$.*

## EXERCISES

1. If $A\in\mathcal B(\mathcal H)$ and $\operatorname{ran}A$ is closed, prove than $\operatorname{ran}A^*$ is closed without using Theorem VI.1.10. [Hint: Show that there is a bounded operator $B$ on $\mathcal H$ such that $BA=$ the projection of $\mathcal H$ onto $(\ker A)^\perp$.]

2. Give a direct proof that (b) implies (a) in Theorem 2.3.

3. Let $A,B,C\in\mathcal B(\mathcal H)$ and define $X:\mathcal H^{(2)}\to\mathcal H^{(2)}$ by the matrix $X=\begin{bmatrix}A&B\\0&C\end{bmatrix}$. (a) Show that if $A\in\mathcal F$, then $X\in\mathcal F$ if and only if $C\in\mathcal F$. (b) If $A\in\mathcal F$, show that $X\in\mathcal{SF}$ if and only if $C\in\mathcal{SF}$. (c) Suppose $A,C\in\mathcal{SF}$ with $\dim\ker A=\infty$ and $\dim\ker C^*=\infty$. Show that $X\notin\mathcal{SF}$.

4. If $A\in\mathcal B(\mathcal H)$, show that $A\mathcal M$ is closed for every closed subspace $\mathcal M$ of $\mathcal H$ if and only if $A$ has finite rank or $A$ is left Fredholm.

5. If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $T\in\mathcal B(\mathcal X,\mathcal Y)$ such that the Hamel basis dimension (that is, the algebraic dimension) of $\mathcal Y/(\operatorname{ran}T)$ is finite, then $\operatorname{ran}T$ is closed.

6. Show that a normal operator is Fredholm if and only if $0$ is not a limit point of $\sigma(N)$ and $\dim\ker N<\infty$. (See Proposition 4.5 below.)

## §3. The Fredholm Index

I wish to acknowledge that the basis of this section is a development of the Fredholm index which I learned from my colleague Hari Bercovici.



<a id="pdf-page-368"></a>
If $A$ is a semi-Fredholm operator, define the (*Fredholm*) index of $A$, $\operatorname{ind}A$, by

$$
\begin{aligned}
\operatorname{ind}A
&=\dim\ker A-\dim(\operatorname{ran}A)^\perp\\
&=\dim\ker A-\dim\ker A^*.
\end{aligned}
\tag{3.1}
$$

Note that $\operatorname{ind}A\in\mathbb Z\cup\{\pm\infty\}$ and it is necessary for either $\ker A$ or $\ker A^*$ to be finite dimensional in order for (3.1) to make sense. For $\operatorname{ind}A$ to be well defined, it is not necessary that $\operatorname{ran}A$ be closed (the other part of the definition of semi-Fredholm operators), but this property will be used in a critical way when the properties of the index are established.

See Dieudonné [1985] for some historical notes on the Fredholm index.

The main properties of the Fredholm index are contained in Theorems 3.7, 3.11, and 3.12 below. But we will begin with some elementary results.

**3.2. Proposition.** *If $A:\mathcal H\to\mathcal H'$ and $\mathcal H$ and $\mathcal H'$ are finite dimensional, then $A$ is Fredholm and $\operatorname{ind}A=\dim\mathcal H-\dim\mathcal H'$.*

**Proof.** Clearly $A$ is Fredholm. From linear algebra we know that $\dim\mathcal H=\dim(\operatorname{ran}A)+\dim(\ker A)=[\dim\mathcal H'-\dim(\operatorname{ran}A)^\perp]+\dim(\ker A)$. Thus $\operatorname{ind}A=\dim(\ker A)-\dim(\operatorname{ran}A)^\perp=\dim\mathcal H-\dim\mathcal H'$. ■

The next result is actually just a restatement of the Fredholm Alternative (VII. 7.9).

**3.3. Proposition.** *If $K:\mathcal H\to\mathcal H$ is a compact operator and $\lambda\ne0$, then $\lambda+K$ is Fredholm and $\operatorname{ind}(\lambda+K)=0$.*

We already observed that the adjoint of a semi-Fredholm operator is also a semi-Fredholm operator. This same reasoning produces the calculation of the index.

**3.4. Proposition.** (a) *If $A$ is a semi-Fredholm operator, then $A^*$ is also semi-Fredholm and $\operatorname{ind}A^*=-\operatorname{ind}A$.*

(b) *If $N$ is a normal operator on a Hilbert space $\mathcal H$, then $N$ is semi-Fredholm if and only if $N$ is Fredholm, in which case $\operatorname{ind}N=0$.*

(c) *If $A$ and $B$ are Fredholm operators, then $A\oplus B$ is Fredholm and $\operatorname{ind}(A\oplus B)=\operatorname{ind}A+\operatorname{ind}B$.*

**Proof.** As stated, the proof of (a) is easy. For part (b), recall that for a normal operator $N$, $\|Nh\|=\|N^*h\|$ for every vector $h$ in $\mathcal H$. Thus $\ker N=\ker N^*$. The result is now immediate. The proof of (c) is left to the reader. ■

Also see Exercise 2.6 and Proposition 4.5 below.

The next theorem is one of the main properties of the Fredholm index. But first two lemmas are required.



<a id="pdf-page-369"></a>
**3.5. Lemma.** *Let $A:\mathcal H\to\mathcal H'$, $\mathcal H=\mathcal M\oplus\mathcal N$, $\mathcal H'=\mathcal M'\oplus\mathcal N'$, and suppose $A$ has the matrix*

$$
\begin{bmatrix}
A_1 & X\\
0 & A_2
\end{bmatrix}
$$

*relative to these two decompositions of $\mathcal H$ and $\mathcal H'$. If $A_1$ is invertible and $\mathcal N$ and $\mathcal N'$ are finite dimensional, then $A$ is Fredholm and $\operatorname{ind}A=\dim\mathcal N-\dim\mathcal N'$.*

**Proof.** It is easy to see that $\operatorname{ran}A$ is closed since $\operatorname{ran}A_1=\mathcal M'$ and $\dim\mathcal N<\infty$. Let’s show that $\ker A^*=\ker A_2^*$ and $\dim(\ker A)=\dim(\ker A_2)$. If this is done, then $\operatorname{ind}A=\dim(\ker A)-\dim(\ker A^*)=\dim(\ker A_2)-\dim(\ker A_2^*)=\dim\mathcal N-\dim\mathcal N'$ by Proposition 3.2.

For the first of the two desired equalities, let $f'\in\mathcal M'$ and $g'\in\mathcal N'$. Then $A^*(f'\oplus g')=A_1^*f'\oplus(X^*f'+A_2^*g')$. So $f'\oplus g'\in\ker A^*$ if and only if $A_1^*f'=0$ and $A_2^*g'=-X^*f'$. But $A_1$ is invertible, so this happens exactly when $f'=0$, and hence $A_2^*g'=0$. From here it is clear that $\ker A^*=\ker A_2^*$. For the second equality, note that $g\to-A_1^{-1}Xg\oplus g$ is a bijection between $\ker A_2$ and $\ker A$. $\blacksquare$

The second lemma is elementary and its proof is left to the reader.

**3.6. Lemma.** *Let $\mathcal M$ and $\mathcal N$ be two closed subspaces of the Hilbert space $\mathcal H$.*

(a) *If $\mathcal M\cap\mathcal N=(0)$ and $\dim\mathcal N=\infty$, then $\dim\mathcal M^\perp=\infty$.*

(b) *If $\dim\mathcal M^\perp=\infty$ and $\dim\mathcal N<\infty$, then $\dim(\mathcal M+\mathcal N)^\perp<\infty$.*

**3.7. Theorem.** *If $A:\mathcal H\to\mathcal H'$ and $B:\mathcal H'\to\mathcal H''$ are left semi-Fredholm operators, then $BA$ is a left semi-Fredholm operator and $\operatorname{ind}BA=\operatorname{ind}A+\operatorname{ind}B$.*

**Proof.** By definition, there are operators $X$ and $Y$ such that $XA=1+K$ and $YB=1+K'$, where $K$ and $K'$ are compact operators on the appropriate spaces. Hence $(XY)(BA)=X(1+K')A=1+(K+XK'A)$, and $K+XK'A$ is compact. Therefore $BA$ is left semi-Fredholm.

To prove the formula for the index, we consider 4 cases.

**Case 1.** Both $A$ and $B$ are Fredholm.

Let $\mathcal M'=(\operatorname{ran}A)\cap(\ker B)^\perp$ and put $\mathcal N'=\mathcal M'^\perp$.

**Claim 1:** $\mathcal N'$ is finite dimensional.

To see this note that $\mathcal N'=\mathcal M'^\perp=(\operatorname{ran}A)^\perp\vee(\ker B)$. Since both of these spaces are finite dimensional, so is $\mathcal N'$. Let $\mathcal M=A^{-1}(\mathcal M')\cap(\ker A)^\perp$; $\mathcal N=\mathcal M^\perp$; $\mathcal M''=B\mathcal M'$; $\mathcal N''=\mathcal M''^\perp$. Note the following: $A(\mathcal M)=\mathcal M'$; $A|_{\mathcal M}$ is invertible (because $\ker(A|_{\mathcal M})=\ker A\cap\mathcal M=(0)$); $B|_{\mathcal M'}$ is invertible.



<a id="pdf-page-370"></a>
**Claim 2: $\mathcal N$ is finite dimensional.**

Indeed, let $A_1\equiv A|_{(\ker A)^\perp}$; so $A_1:(\ker A)^\perp\to\operatorname{ran}A$ is invertible. But $A_1^{-1}(\mathcal M')=\mathcal M$, so $\dim[(\ker A)^\perp\cap\mathcal M^\perp]=\dim[(\operatorname{ran}A)\cap(\mathcal M')^\perp]$, and this last dimension is finite since $\mathcal N'$ is finite dimensional.

**Claim 3: $\mathcal N''$ is finite dimensional.**

In fact, $\dim[(\ker B)^\perp\cap(\mathcal M')^\perp]<\infty$ and so $\dim[(\operatorname{ran}B)\cap(\mathcal M'')^\perp]<\infty$. This implies that $\dim\mathcal N''<\infty$. Now represent the operators as $2\times2$ matrices:

$$
A=\begin{bmatrix}A_1&X\\0&A_2\end{bmatrix}:
\begin{matrix}
\mathcal M&&\mathcal M'\\
\oplus&\longrightarrow&\oplus\\
\mathcal N&&\mathcal N'
\end{matrix},
$$

$$
B=\begin{bmatrix}B_1&Y\\0&B_2\end{bmatrix}:
\begin{matrix}
\mathcal M'&&\mathcal M''\\
\oplus&\longrightarrow&\oplus\\
\mathcal N'&&\mathcal N''
\end{matrix},
$$

$$
BA=\begin{bmatrix}B_1A_1&Z\\0&B_2A_2\end{bmatrix}:
\begin{matrix}
\mathcal M&&\mathcal M''\\
\oplus&\longrightarrow&\oplus\\
\mathcal N&&\mathcal N''
\end{matrix}.
$$

It follows that $B_1$ and $A_1$ are invertible. Since $\mathcal N$, $\mathcal N'$, and $\mathcal N''$ are finite dimensional, the preceding lemma implies that $\operatorname{ind}A=\dim\mathcal N-\dim\mathcal N'$, $\operatorname{ind}B=\dim\mathcal N'-\dim\mathcal N''$, and $\operatorname{ind}BA=\dim\mathcal N-\dim\mathcal N''=\operatorname{ind}A+\operatorname{ind}B$.

**Case 2.** Assume $\operatorname{ind}B=-\infty$.

This is equivalent to the assumption that $\dim(\operatorname{ran}B)^\perp=\infty$. But $\operatorname{ran}B\supseteq\operatorname{ran}BA$ and so $\dim(\operatorname{ran}BA)^\perp=\infty$. Hence $\operatorname{ind}BA=-\infty=\operatorname{ind}A+\operatorname{ind}B$.

**Case 3.** Assume $B$ is invertible.

Without loss of generality we may assume that $\operatorname{ind}A=-\infty$ since the alternative situation is covered in Case 1. If $\mathcal M=B(\operatorname{ran}A)=\operatorname{ran}BA$ and $\mathcal N=B[(\operatorname{ran}A)^\perp]$, then the fact that $B$ is invertible implies that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal N$ is infinite dimensional. Thus Lemma 3.6(a) implies that $\infty=\dim\mathcal M^\perp=\dim(\operatorname{ran}BA)^\perp$ and so $\operatorname{ind}BA=-\infty=\operatorname{ind}A+\operatorname{ind}B$.

**Case 4.** $B$ is a Fredholm operator.

Again, without loss of generality we may assume that $\operatorname{ind}A=-\infty$. It must be shown that $\operatorname{ind}BA=-\infty$.

Put $\mathcal H'_1=(\ker B)^\perp$ and $\mathcal H''_1=\operatorname{ran}B$; define $B_1:\mathcal H'_1\to\mathcal H''_1$ as the restriction



<a id="pdf-page-371"></a>
of $B$ to $\mathcal H_1''$. Clearly $B_1$ is invertible. If $P$ is the orthogonal projection of $\mathcal H'$ onto $\mathcal H_1'$, let $A_1:\mathcal H\to\mathcal H_1'$ be defined by $A_1=PA$. Now both $P$ and $A$ are left semi-Fredholm, so $A_1$ is left semi-Fredholm as was established at the opening of the proof.

Note that Lemma 3.6(b) implies that $\dim(\operatorname{ran}A+\ker B)^\perp=\infty$. But $(\operatorname{ran}A_1)^\perp=\ker A_1^*=\ker A^*P=\ker B+(\ker A^*)\cap(\ker B)^\perp=\ker B+(\operatorname{ran}A+\ker B)^\perp$ and so $\operatorname{ind}A_1=-\infty$. According to Case 3, $\operatorname{ind}B_1A_1=-\infty$.

This is equivalent to the condition that $\infty=\dim(\operatorname{ran}B_1A_1)^\perp=\dim(\mathcal H_1''\cap[B(\operatorname{ran}A_1)]^\perp)$. But $B(\operatorname{ran}A_1)=BP(\operatorname{ran}A)=B(\operatorname{ran}A)=\operatorname{ran}BA$ and so $\mathcal H_1''\cap[B(\operatorname{ran}A_1)]^\perp\subseteq(\operatorname{ran}BA)^\perp$. Thus $\operatorname{ind}BA=-\infty$. ■

**3.8. Corollary.** *If $A\in\mathcal F_\ell$ and $R$ is an invertible operator, then $RAR^{-1}\in\mathcal F_\ell$ and $\operatorname{ind}RAR^{-1}=\operatorname{ind}A$.*

Before going further, let’s look at some examples.

**3.9. Example.** Let $S$ be the unilateral shift of multiplicity $\alpha$. We saw in Example 2.2 that $S$ is left semi-Fredholm. It is easy to calculate that $\operatorname{ind}S=-\alpha$. According to the preceding theorem, $\operatorname{ind}S^2=-2\alpha$. But, of course, $S^2$ is the unilateral shift of multiplicity $2\alpha$.

**3.10. Example.** Let $S$ be the unilateral shift of multiplicity $\alpha$ on the Hilbert space $\mathcal H$ and put $A=S\oplus S^*$. Note that $\ker A=(0)\oplus\ker S^*$ and $\operatorname{ran}A=(\operatorname{ran}S)\oplus\mathcal H$. Thus $A$ has closed range. The operator $A$, however, is semi-Fredholm if and only if $\alpha<\infty$, in which case $A$ is a Fredholm operator. Also when $\alpha<\infty$, $\operatorname{ind}A=0$.

**3.11. Theorem.** *If $A:\mathcal H\to\mathcal H'$ is a left (respectively, right) semi-Fredholm operator and $K:\mathcal H\to\mathcal H'$ is a compact operator, then $A+K$ is left (respectively, right) semi-Fredholm and $\operatorname{ind}A=\operatorname{ind}(A+K)$.*

**Proof.** Assume that $A$ is a left semi-Fredholm operator. By definition there is an operator $X:\mathcal H'\to\mathcal H$ and a compact operator $K_0:\mathcal H\to\mathcal H$ such that $XA=1+K_0$. Thus $X(A+K)=1+(K_0+XK)$ and so $A+K$ is left semi-Fredholm.

To verify that $\operatorname{ind}A=\operatorname{ind}(A+K)$, first assume that $A$ is Fredholm. So there is a Fredholm operator $X$ and a compact operator $L$ such that $XA=1+L$. But Theorem 3.7 implies that $XA$ is Fredholm and, using Proposition 3.3, $0=\operatorname{ind}(1+L)=\operatorname{ind}A+\operatorname{ind}X$; so $\operatorname{ind}A=-\operatorname{ind}X$. But $X(A+K)=1+(L+XK)$ and so the same type of reasoning implies that $\operatorname{ind}(A+K)=-\operatorname{ind}X=\operatorname{ind}A$.

Now assume that $A$ is left semi-Fredholm; so $A+K$ is also left semi-Fredholm. If $\operatorname{ind}A$ is finite, then $A$ is Fredholm and we are done by the preceding paragraph. If $\operatorname{ind}A$ is $-\infty$, then $\operatorname{ind}(A+K)$ must also be $-\infty$ for otherwise $A+K$ is Fredholm and it follows that $A=(A+K)-K$ is also Fredholm, a contradiction. ■



<a id="pdf-page-372"></a>
The preceding theorem says that the value of the index is impervious to compact perturbations. The next result, the third in the list of important properties of the Fredholm index, says that the value of the index is unchanged for all perturbations of the operator, provided that the size of the perturbation is sufficiently small.

**3.12. Theorem.** *If $A:\mathcal H\to\mathcal H'$ is a Fredholm operator, then there is an $\varepsilon>0$ such that if $Y\in\mathcal B(\mathcal H,\mathcal H')$ and $\|Y\|<\varepsilon$, then $A+Y$ is Fredholm and $\operatorname{ind}A=\operatorname{ind}(A+Y)$.*

**Proof.** With respect to the decompositions $\mathcal H=(\ker A)^\perp\oplus\ker A$ and $\mathcal H'=\operatorname{ran}A\oplus\ker A^*$, the operator $A$ has the matrix

$$
\begin{bmatrix}
A_1 & 0\\
0 & 0
\end{bmatrix}
$$

and $A_1:(\ker A)^\perp\to\operatorname{ran}A$ is invertible since $A$ is Fredholm. Thus there is an $\varepsilon>0$ such that if $\|Y_1\|<\varepsilon$, then $A_1+Y_1$ is invertible. If $Y:\mathcal H\to\mathcal H'$ and $\|Y\|<\varepsilon$, then, with respect to the same decomposition of $\mathcal H$,

$$
Y=\begin{bmatrix}
Y_1 & Y_2\\
Y_3 & Y_4
\end{bmatrix}
$$

and so

$$
A+Y
=\begin{bmatrix}
A_1+Y_1 & Y_2\\
Y_3 & Y_4
\end{bmatrix}
=\begin{bmatrix}
A_1+Y_1 & 0\\
0 & 0
\end{bmatrix}
+\begin{bmatrix}
0 & Y_2\\
Y_3 & Y_4
\end{bmatrix},
$$

where the first matrix represents a Fredholm operator and the second represents a finite rank operator. Therefore $\operatorname{ind}(A+Y)$ is the index of the first matrix. But since $A_1+Y_1$ is invertible, Lemma 3.5 implies that this index is equal to $\dim(\ker A)-\dim(\ker A^*)=\operatorname{ind}A$. $\blacksquare$

**3.13. Corollary.** *If $\mathcal{SF}$ is given the norm topology and $\mathbb Z\cup\{\pm\infty\}$ is given the discrete topology, then the Fredholm index is a continuous function from $\mathcal{SF}$ into $\mathbb Z\cup\{\pm\infty\}$.*

This continuity statement has an equivalent formulation. Because $\mathcal{SF}$ is an open subset of $\mathcal B(\mathcal H)$, its components are open sets. Thus the continuity of the index is equivalent to the statement that it is constant on the components of $\mathcal{SF}$.

For a treatment of the Fredholm index applicable to unbounded operators on a Banach space, see Kato [1966], pp. 229–244. For other approaches to Fredholm theory, with variations and generalizations of the material in this book, see Caradus, Pfaffenberger, and Yood [1974] and Harte [1982].

## Exercises

1. Prove Lemma 3.6.

2. If $A\in\mathcal B(\mathcal H)$ and $\operatorname{ran}A$ is closed, show that $\operatorname{ran}A^{(\infty)}$ is closed. If $A\in\mathcal{SF}$ and $\ker A=(0)$, show that $A^{(\infty)}\in\mathcal{SF}$ and $\operatorname{ind}A^{(\infty)}=-\infty$ or $0$.



<a id="pdf-page-373"></a>
3. Does the unilateral shift of multiplicity 1 have a square root?

4. Show that for every $n\in\mathbb{Z}\cup\{\pm\infty\}$ there is an operator $A$ in $\mathcal{SF}$ such that $\operatorname{ind}A=n$.

5. If $A\in\mathcal{SF}$, then for every $n\geq 1$, $A^n\in\mathcal{SF}$ and $\operatorname{ind}A^n=n(\operatorname{ind}A)$.

6. If $A:\mathcal{H}\to\mathcal{H}'$ is a left semi-Fredholm operator, then there is a finite rank operator $F:\mathcal{H}\to\mathcal{H}'$ such that $\ker(A+F)=(0)$ and $\operatorname{ind}(A+F)=\operatorname{ind}A$.

7. If $A$ is a Fredholm operator in $\mathcal{B}(\mathcal{H})$, prove that the following statements are equivalent. (a) $\operatorname{ind}A=0$. (b) There is a compact operator $K$ such that $A+K$ is invertible. (c) There is a finite rank operator $F$ such that $A+F$ is invertible.

8. If $U$ is the unilateral shift of multiplicity 1 and $\pi:\mathcal{B}(\mathcal{H})\to\mathcal{B}(\mathcal{H})/\mathcal{B}_0(\mathcal{H})$ is the natural map, show that $\pi(U)$ is normal in $\mathcal{B}(\mathcal{H})/\mathcal{B}_0(\mathcal{H})$ but there is no normal operator $N$ such that $U-N$ is compact. (See Exercise IX.8.14.)

## §4. The Essential Spectrum

Now concentrate on operators acting on a single Hilbert space $\mathcal{H}$ and let $\pi:\mathcal{B}\to\mathcal{B}/\mathcal{B}_0$ be the natural map from $\mathcal{B}(\mathcal{H})$ into the Calkin algebra. Since the Calkin algebra is a Banach algebra with identity, the next definition makes sense.

**4.1. Definition.** If $A\in\mathcal{B}(\mathcal{H})$, the *essential spectrum* of $A$, $\sigma_e(A)$, is the spectrum of $\pi(A)$ in $\mathcal{B}/\mathcal{B}_0$; that is, $\sigma_e(A)=\sigma(\pi(A))$. Similarly the *left and right essential spectrum* of $A$ are defined by $\sigma_{\ell e}(A)=\sigma_\ell(\pi(A))$ and $\sigma_{re}(A)=\sigma_r(\pi(A))$, respectively.

The proof of the next proposition is a straightforward application of the general properties of the various spectra in an arbitrary Banach algebra.

**4.2. Proposition.** Let $A\in\mathcal{B}(\mathcal{H})$.

(a) $\sigma_e(A)=\sigma_{\ell e}(A)\cup\sigma_{re}(A)$.

(b) $\sigma_{\ell e}(A)=\sigma_{re}(A^*)^*$.

(c) $\sigma_{\ell e}(A)\subseteq\sigma_\ell(A)$, $\sigma_{re}(A)\subseteq\sigma_r(A)$, and $\sigma_e(A)\subseteq\sigma(A)$.

(d) $\sigma_{\ell e}(A)$, $\sigma_{re}(A)$, and $\sigma_e(A)$ are compact sets.

(e) If $K$ is a compact operator, $\sigma_{\ell e}(A+K)=\sigma_{\ell e}(A)$, $\sigma_{re}(A+K)=\sigma_{re}(A)$, and $\sigma_e(A+K)=\sigma_e(A)$.

Our understanding of semi-Fredholm operators gained in the preceding sections can now be applied to better understand the essential spectrum. Indeed, $\sigma_{\ell e}(A)=\{\lambda\in\mathbb{C}:A-\lambda\notin\mathcal{SF}_\ell\}$. Thus an application of Theorem 2.3 gives us the following.



<a id="pdf-page-374"></a>
**4.3. Proposition.** Let $A\in\mathcal B(\mathcal H)$.

(a) $\lambda\in\sigma_{le}(A)$ if and only if $\dim\ker(A-\lambda)=\infty$ or $\operatorname{ran}(A-\lambda)$ is not closed.

(b) $\lambda\in\sigma_{re}(A)$ if and only if $\dim[\operatorname{ran}(A-\lambda)]^\perp=\infty$ or $\operatorname{ran}(A-\lambda)$ is not closed.

The reader should compare Proposition 4.3 and Proposition 1.1.

**4.4. Proposition.** If $A\in\mathcal B(\mathcal H)$, then
$$
\sigma_{ap}(A)=\sigma_{le}(A)\cup\{\lambda\in\sigma_p(A):\dim\ker(A-\lambda)<\infty\}.
$$

**Proof.** If $\lambda\in\sigma_{ap}(A)$, then (1.1) either $\operatorname{ran}(A-\lambda)$ is not closed or $\ker(A-\lambda)\ne0$. If $\operatorname{ran}(A-\lambda)$ is not closed or if $\dim\ker(A-\lambda)=\infty$, then $\lambda\in\sigma_{le}(A)$ by (4.3). The proof of other inclusion is left to the reader. ■

**4.5. Proposition.** If $N$ is a normal operator and $\lambda\in\sigma(N)$, then $\operatorname{ran}(N-\lambda)$ is closed if and only if $\lambda$ is not a limit point of $\sigma(N)$.

**Proof.** Assume $\lambda$ is an isolated point of $\sigma(N)$; thus $X=\sigma(N)\backslash\{\lambda\}$ is a closed subset of $\sigma(N)$. If $N=\int z\,dE(z)$ and $\mathcal H_1=E(X)\mathcal H$, then $\mathcal H_1$ reduces $N$ and $\sigma(N|\mathcal H_1)=X$. Hence $(N-\lambda)\mathcal H_1$ is closed. Since $\mathcal H_1^\perp=\ker(N-\lambda)$, $\operatorname{ran}(N-\lambda)=(N-\lambda)\mathcal H_1$; hence $N-\lambda$ has closed range.

Now assume that $\lambda\in\sigma(N)$ but $\lambda$ is not an isolated point. Then there is a strictly decreasing sequence $\{r_n\}$ of positive real numbers such that $r_n\to0$ and such that each open annulus $A_n=\{z:r_{n+1}<|z-\lambda|<r_n\}$ has non-empty intersection with $\sigma(N)$. Thus $E(A_n)\mathcal H\ne(0)$; let $e_n$ be a unit vector in $E(A_n)\mathcal H$. Then $e_n\perp\ker(N-\lambda)\;(=E(\{\lambda\})\mathcal H)$ and
$$
\|(N-\lambda)e_n\|^2
=\int_{A_n}|z-\lambda|^2\,dE_{e_n,e_n}(z)
\le r_n^2\to0.
$$

That is, $\inf\{\|(N-\lambda)h\|:\|h\|=1,\ h\perp\ker(N-\lambda)\}=0$ and so, by the Open Mapping Theorem, $N-\lambda$ does not have closed range. ■

**4.6. Proposition.** If $N$ is a normal operator, then $\sigma_e(N)=\sigma_{le}(N)=\sigma_{re}(N)$ and
$$
\sigma(N)\backslash\sigma_e(N)
=\{\lambda\in\sigma(N):\lambda\text{ is an isolated point of }\sigma(N)\text{ that is an eigenvalue of finite multiplicity}\}.
$$

**Proof.** The first part follows by applying Proposition 1.3 to the Calkin algebra. If $\lambda$ is an isolated point of $\sigma(N)$, then $\operatorname{ran}(N-\lambda)$ is closed by the preceding proposition. So if $\dim\ker(N-\lambda)<\infty$, $\lambda\notin\sigma_{le}(N)=\sigma_e(N)$ by Proposition 4.3. Conversely, if $\lambda\in\sigma(N)\backslash\sigma_e(N)$, then $\operatorname{ran}(N-\lambda)$ is closed and $\dim\ker(N-\lambda)<\infty$. By the preceding proposition, $\lambda$ is an isolated point of $\sigma(N)$. ■

**4.7. Example.** Let $G$ be a bounded region in $\mathbb C$ and, to avoid pathologies, assume $\partial G=\partial[\operatorname{cl}G]$. Let $\mathcal H=L_a^2(G)$ (I.1.10) and define $S:\mathcal H\to\mathcal H$ by $(Sf)(z)=zf(z)$. Then $\sigma(S)=\operatorname{cl}G$, $\sigma_e(S)=\sigma_{le}(S)=\sigma_{re}(S)=\partial G=\sigma_{ap}(S)$,



<a id="pdf-page-375"></a>
$\sigma_p(S)=\square$, and for $\lambda$ in $G$, $\operatorname{ran}(S-\lambda)$ is closed and $\dim[\operatorname{ran}(S-\lambda)]^\perp=1$. Thus $\operatorname{ind}(S-\lambda)=-1$ for $\lambda$ in $G$.

To show that these statements are true, begin by proving:

**4.8** If $\lambda\in G$, $\operatorname{ran}(S-\lambda)=\{f\in L_a^2(G):f(\lambda)=0\}$.

In fact, if $h\in L_a^2(G)$, then $[(S-\lambda)h](z)=(z-\lambda)h(z)$ so that $f=(z-\lambda)h$ vanishes at $\lambda$. Conversely, suppose $f\in L_a^2(G)$ and $f(\lambda)=0$; then $f(z)=(z-\lambda)h(z)$ for some analytic function $h$ on $G$. It must be shown that $h\in L_a^2(G)$. Let $r>0$ such that $D=\{z:|z-\lambda|\leq r\}\subseteq G$. Then

$$
\iint |h|^2=\iint_D |h|^2+\iint_{G\setminus D}|h|^2.
$$

Now $\iint_D|h|^2<\infty$ since $h$ is bounded on $D$. For $z$ in $G\setminus D$, $|h(z)|=|f(z)|/|z-\lambda|\leq r^{-1}|f(z)|$. Hence

$$
\iint_{G\setminus D}|h|^2\leq r^{-2}\iint_G|f|^2<\infty.
$$

Thus $h\in L_a^2(G)$ and $f=(S-\lambda)h$. This proves (4.8).

Using Corollary I.1.12, $f\mapsto f(\lambda)$ is a bounded linear functional on $L_a^2(G)$ whenever $\lambda\in G$. By (4.8), $\operatorname{ran}(S-\lambda)$ is the kernel of this linear functional and hence is closed.

Because $G$ is bounded, the constant functions belong to $L_a^2(G)$. So if $f\in L_a^2(G)$, $f=[f-f(\lambda)]+f(\lambda)$ and $f-f(\lambda)\in\operatorname{ran}(S-\lambda)$. Thus $L_a^2(G)=\operatorname{ran}(S-\lambda)+\mathbb C$. Therefore $\dim[\operatorname{ran}(S-\lambda)]^\perp=\dim[L_a^2(G)/\operatorname{ran}(S-\lambda)]=1$ when $\lambda\in G$.

If $\lambda\in G$, then $S-\lambda$ is not surjective; hence $G\subseteq\sigma(S)$. If $\lambda\notin\operatorname{cl}G$, then $(z-\lambda)^{-1}$ is a bounded analytic function on $G$. If $Af=(z-\lambda)^{-1}f$, then $A$ is a bounded operator on $L_a^2(G)$ and it is easy to check that $A(S-\lambda)=(S-\lambda)A=1$. Thus $\sigma(S)\subseteq\operatorname{cl}G$. Combining these two containments, we get $\sigma(S)=\operatorname{cl}G$.

From Corollary 2.4 we have that $S-\lambda$ is a Fredholm operator whenever $\lambda\in G$; thus $G\cap\sigma_e(S)=\square$. So $\sigma_e(S)\subseteq\partial G=\partial[\operatorname{cl}G]$. If $\lambda\in\partial G$, then $\lambda\in\partial\sigma(S)$; thus $\lambda\in\sigma_{ap}(S)$ (1.2). Since $\ker(S-\lambda)=(0)$, $\operatorname{ran}(S-\lambda)$ is not closed. Thus $\partial G\subseteq\sigma_{le}(S)\cap\sigma_{re}(S)$. This proves that $\sigma_e(S)=\sigma_{le}(S)=\sigma_{re}(S)=\partial G=\sigma_{ap}(S)$.

One of the primary uses of Fredholm theory is the examination of the values of $\operatorname{ind}(A-\lambda)$ for all $\lambda$ for which this makes sense. Such an examination often leads to structural information about the operator $A$. Note that $\operatorname{ind}(A-\lambda)$ is defined when $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$.

**4.9. Proposition.** *If $A\in\mathcal B(\mathcal H)$, then $\operatorname{ind}(A-\lambda)$ is constant on the components of $\mathbb C\setminus[\sigma_{le}(A)\cap\sigma_{re}(A)]$. If $\lambda$ is a boundary point of $\sigma(A)$ and $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$, then $\operatorname{ind}(A-\lambda)=0$.*

**Proof.** The map $\lambda\mapsto A-\lambda$ is a continuous map of $\mathbb C\setminus[\sigma_{le}(A)\cap\sigma_{re}(A)]$ into $\mathcal{SF}$. So the first part of the proposition follows from Corollary 3.13. If $\lambda$ is a



<a id="pdf-page-376"></a>
boundary point of $\sigma(A)$ and $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$, then there is a sequence $\{\lambda_n\}$ in $\mathbb C\setminus\sigma(A)$ such that $\lambda_n\to\lambda$. Thus $\operatorname{ind}(A-\lambda_n)\to\operatorname{ind}(A-\lambda)$. Since $\operatorname{ind}(A-\lambda_n)=0$ for all $n$, the result follows. ■

Here is the remaining spectral information about an old friend.

**4.10. Example.** Let $S$ be the unilateral shift on $l^2$. Then $\sigma_{le}(S)=\sigma_{re}(S)=\partial\mathbb D$ and $\operatorname{ind}(S-\lambda)=-1$ for $|\lambda|<1$.

In Proposition VII.6.5 it was shown that $\sigma(S)=\operatorname{cl}\mathbb D$, $\sigma_p(S)=\square$, and $\sigma_{ap}(S)=\partial\mathbb D$. Thus for $|\lambda|=1$, $\operatorname{ran}(S-\lambda)$ is not closed and hence $\partial\mathbb D\subseteq\sigma_{le}(S)\cap\sigma_{re}(S)$. Also, if $|\lambda|<1$, it was shown that $\operatorname{ran}(S-\lambda)$ is closed and $\dim[\operatorname{ran}(S-\lambda)]^\perp=1$. This implies that $\partial\mathbb D=\sigma_{le}(S)=\sigma_{re}(S)$ and $\operatorname{ind}(S-\lambda)=-1$ for $\lambda$ in $\mathbb D$.

Using this information about the shift and Proposition 3.4(c) we can get complete information about another operator. (Also see Example 3.10.)

**4.11. Example.** Let $S$ be the unilateral shift of multiplicity 1 and put $A=S\oplus S^*$. It follows that $\sigma_{le}(A)=\sigma_{re}(A)=\partial\mathbb D$, $\sigma(A)=\operatorname{cl}\mathbb D$, and $\operatorname{ind}(A-\lambda)=0$ for $|\lambda|<1$.

## EXERCISES

1. Show that the material of this section is only significant for infinite dimensional Hilbert spaces by showing that the essential spectrum of every operator on $\mathcal H$ is non-empty if and only if $\mathcal H$ is infinite dimensional.

2. Let $G$ be a bounded region in $\mathbb C$ such that $\partial G=\partial[\operatorname{cl}G]$ and let $\phi$ be a function that is analytic in a neighborhood of $\operatorname{cl}G$. Define $A:L_a^2(G)\to L_a^2(G)$ by $Af=\phi f$. Find all of the parts of the spectrum of $A$.

3. (Fillmore, Stampfli, and Williams [1972].) If $\lambda\in\sigma_{le}(A)$, then there is a projection $P$, having infinite rank, such that $\pi(A-\lambda)\pi(P)=0$.

4. (Fillmore, Stampfli, and Williams [1972].) Let $A\in\mathcal B(\mathcal H)$. (a) If $A$ has a cyclic vector $e$, show that $\dim\{Ae,A^2e,\ldots\}^\perp\leq 1$. (b) Let $\lambda\in\sigma_{le}(A^*)$. If $\varepsilon>0$, let $f_1,f_2$ be orthonormal vectors such that $\|(A^*-\lambda)f_j\|<\varepsilon$ for $j=1,2$ and let $P=$ the projection onto $\vee\{f_1,f_2\}$. Put $B=\bar\lambda P+(1-P)A$. Show that $\|B-A\|<2\varepsilon$. (c) Show that the noncyclic operators are dense in $\mathcal B(\mathcal H)$ if $\dim\mathcal H>1$.

5. Let $A\in\mathcal F$ and suppose $f$ is analytic in a neighborhood of $\sigma(A)$ and does not vanish on $\sigma_e(A)$. Show that $f(A)\in\mathcal F$ and find $\operatorname{ind}f(A)$.

6. Let $S$ be the unilateral shift and let $f$ be an analytic function in a neighborhood of $\operatorname{cl}\mathbb D$ such that $f(z)\ne0$ if $|z|=1$. Let $\gamma(t)=f(\exp(2\pi it))$, $0\leq t\leq1$. Show that $\sigma_e(f(S))=f(\partial\mathbb D)=\{\gamma(t):0\leq t\leq1\}$ and that if $\lambda\notin f(\partial\mathbb D)$, $\operatorname{ind}(f(S)-\lambda)=-n(\gamma;\lambda)$, where $n(\gamma;\lambda)=$ the winding number of $\gamma$ about $\lambda$. Moreover, show that if $\operatorname{ind}(f(S)-\lambda)=0$, then $\lambda\notin\sigma(f(S))$.

7. Let $S$ be the operator defined in Example 2.11 where $G=\mathbb D$. Show that there is a compact operator $K$ such that $S+K$ is unitarily equivalent to the unilateral shift.



<a id="pdf-page-377"></a>
8. If $S$ is the unilateral shift, show that for every $\varepsilon>0$ there is a rank one operator $F$ with $\|F\|<\varepsilon$ such that $\sigma(S^*\oplus S+F)=\partial\mathbf D$.

9. Let $G$ be an open connected subset of $\sigma(A)\backslash\sigma_{le}(A)\cup\sigma_{re}(A)$ and suppose $\lambda_0\in G$ such that $\operatorname{ind}(A-\lambda_0)=0$. Show that there is a finite rank operator $F$ such that $A+F-\lambda_0$ is invertible. Show that $A+F-\lambda$ is invertible for every $\lambda$ in $G$.

## §5. The Components of $\mathcal{SF}$

Since the index is continuous on $\mathcal{SF}$ and assumes every possible value (Exercise 3.4), $\mathcal{SF}$ cannot be connected. What are its components?

Note that because $\mathcal{SF}$ is an open subset of a Banach space, its components are arcwise connected (Exercise IV.1.24).

**5.1. Theorem.** *If $A,B\in\mathcal{SF}$, then $A$ and $B$ belong to the same component of $\mathcal{SF}$ if and only if $\operatorname{ind}A=\operatorname{ind}B$.*

Half of this theorem is easy. For the other half we first prove a lemma.

**5.2. Lemma.** *If $A\in\mathcal F$ and $\operatorname{ind}A=0$, then there is a path $\gamma:[0,1]\to\mathcal F$ such that $\gamma(0)=1$ and $\gamma(1)=A$.*

**Proof.** By Exercise 3.7 there is a finite-rank operator $F$ such that $A+F$ is invertible. If $\gamma(t)=A+tF$, $\gamma(0)=A$, $\gamma(1)=A+F$, and $\gamma(t)\in\mathcal F$ for all $t$. Thus we may assume that $A$ is invertible.

Let $A=U|A|$ be the polar decomposition of $A$. Because $A$ is invertible, $U$ is a unitary operator and $|A|$ is invertible. Using the Spectral Theorem, $U=\exp(iB)$ where $B$ is hermitian. Also, since $0\notin\sigma(|A|)$, $|A|=\int_{[\delta,r]}x\,dE(x)$, where $0<\delta<r=\|A\|$. Define $\gamma:[0,1]\to\mathcal B(\mathcal H)$ by

$$
\gamma(t)=e^{itB}\int_{[\delta,r]}x^t\,dE(x)=e^{itB}|A|^t.
$$

It is easy to check that $\gamma$ is continuous, $\gamma(0)=1$, and $\gamma(1)=A$. Also, each $\gamma(t)$ is invertible so $\gamma(t)\in\mathcal F$. ■

**Proof of Theorem 5.1.** First assume that $A,B\in\mathcal F$ and $\operatorname{ind}A=\operatorname{ind}B$. So there is an operator $C$ such that $CB=1+K$ for some compact operator $K$. Thus $C\in\mathcal F_r$ and $\operatorname{ind}C=-\operatorname{ind}B=-\operatorname{ind}A$. Hence $AC\in\mathcal F$ and $\operatorname{ind}AC=0$. By the preceding lemma there is a path $\gamma:[0,1]\to\mathcal F$ such that $\gamma(0)=1$ and $\gamma(1)=AC$. Put $\rho(t)=\gamma(t)B-tAK$. Because $AK\in\mathcal B_0$, $\rho(t)\in\mathcal F$ for all $t$ in $[0,1]$. Also, $\rho(0)=B$ and $\rho(1)=ACB-AK=A(1+K)-AK=A$.

Now assume that $\operatorname{ind}A=-\infty$; so $\dim(\operatorname{ran}A)^\perp=\infty$ and $\dim\ker A<\infty$. Let $F$ be a finite-rank operator such that $\ker(A+tF)=0$ for $t\ne0$. (Why does $F$ exist?) This path shows that we may assume that $\ker A=(0)$. Let $V$ be any isometry such that $\dim(\operatorname{ran}V)^\perp=\infty$ and consider the polar decom-



<a id="pdf-page-378"></a>
position $A=U|A|$ of $A$. Since $A\in\mathcal{SF}$ and $\ker A=(0)$, $|A|$ is invertible and $U$ is an isometry. Also, $\operatorname{ran}U=\operatorname{ran}A$, so (Exercise 4) there is a path $\rho:[0,1]\to\mathcal{B}(\mathcal{H})$ such that $\rho(t)$ is an isometry for every $t$ and $\rho(0)=U$ and $\rho(1)=V$. Let $\gamma:[0,1]\to\mathcal{F}$ be a path such that $\gamma(0)=|A|$ and $\gamma(1)=1$. Then $\sigma(t)=\rho(t)\gamma(t)$ for $0\leq t\leq 1$ defines a path $\sigma:[0,1]\to\mathcal{SF}$ (Why?) such that $\sigma(0)=A$ and $\sigma(1)=V$. Similarly, if $\operatorname{ind}B=-\infty$, there is a path connecting $B$ to $V$; so $A$ and $B$ belong to the same component of $\mathcal{SF}$.

If $\operatorname{ind}A=\operatorname{ind}B=+\infty$, apply the preceding paragraph to $A^*$ and $B^*$. ■

**5.3. Corollary.** *The component of the identity in $\mathcal{F}$, $\mathcal{F}_0$, is a normal sub-group of $\mathcal{F}$ and $\mathcal{F}/\mathcal{F}_0$ is an infinite cyclic group.*

**Proof.** By Theorem 3.7, $\operatorname{ind}:\mathcal{F}\to\mathbb{Z}$ is a group homomorphism and it is surjective (Exercise 3.4). By Theorem 5.1, $\ker(\operatorname{ind})=\mathcal{F}_0$. ■

**Exercises**

1. Let $G$ be any topological group and let $G_0$ be the component of the identity. Show that $G_0$ is a normal subgroup of $G$.

2. What are the components of the set of invertible elements in $C(\partial\mathbb{D})$?

3. If $S=$ the unilateral shift, what are the components of the set of invertible elements of $C^*(S)$?

4. If $U$ and $V$ are isometries, show that there is a path consisting entirely of isometries connecting $U$ to $V$ if and only if $\dim(\operatorname{ran}U)^\perp=\dim(\operatorname{ran}V)^\perp$.

5. Find the components of the set of partial isometries.

## §6. A Finer Analysis of the Spectrum

In this section we will examine the spectrum and index more closely. For example, one question that arises: If $A$ is semi-Fredholm and $\delta>0$ is chosen so that $B$ is semi-Fredholm and $\operatorname{ind}B=\operatorname{ind}A$ whenever $\|B-A\|<\delta$ (Corollary 3.13), how does $\dim\ker B$ differ from $\dim\ker A$?

Begin this investigation by associating with every bounded operator $A$ the following number:

$$
\gamma(A)=\inf\{\|Ah\|:\|h\|=1\text{ and }h\perp\ker A\}.
$$

The first proposition contains some elementary properties of $\gamma$ and its proof is left to the reader. (Actually part (a) has appeared several times in this book under different guises.)

**6.1. Proposition.** *Let $A$ be a bounded operator on $\mathcal{H}$.*

(a) $\gamma(A)>0$ if and only if $A$ has closed range.



<a id="pdf-page-379"></a>
(b) $\gamma(A)=\sup\{\gamma:\|Ah\|\geq\gamma\|h\|\text{ for all }h\text{ in }(\ker A)^\perp\}=\inf\{\|Ah\|/\|h\|:h\in(\ker A)^\perp\setminus\{0\}\}$.

**6.2. Proposition.** If $A\in\mathcal{B}(\mathcal{H})$, then $\gamma(A)=\gamma(A^*)$.

**Proof.** Let $h\perp\ker A$. Then $\|A^*Ah\|=\||A||A|h\|=\|A|A|h\|$. But $|A|h\in\operatorname{cl}\operatorname{ran}A^*$ (Why?) $=(\ker A)^\perp$. Hence the definition of $\gamma(A)$ implies that $\|A^*Ah\|\geq\gamma(A)\||A|h\|=\gamma(A)\|Ah\|$; that is, $\|A^*f\|\geq\gamma(A)\|f\|$ for every $f$ in $\operatorname{ran}A$. Since $\operatorname{ran}A$ is dense in $(\ker A^*)^\perp$, $\gamma(A^*)\geq\gamma(A)$. But $A=A^{**}$, so $\gamma(A)\geq\gamma(A^*)$. ■

Note that the preceding two propositions give a proof of the fact that an operator on a Hilbert space has closed range if and only if its adjoint does. See Theorem VI.1.10 and Exercise 2.1.

**6.3. Lemma.** If $\mathcal{M},\mathcal{N}\leq\mathcal{H}$, $\mathcal{N}$ is finite dimensional, and $\dim\mathcal{M}>\dim\mathcal{N}$, then there is a non-zero vector $m$ in $\mathcal{M}$ such that $\|m\|=\operatorname{dist}(m,\mathcal{N})$.

**Proof.** Let $P$ be the projection of $\mathcal{H}$ onto $\mathcal{M}$, so $\dim P(\mathcal{N})\leq\dim\mathcal{N}<\dim\mathcal{M}$. Thus $P(\mathcal{N})$ is a proper subspace of $\mathcal{M}$; let $m\in\mathcal{M}\cap P(\mathcal{N})^\perp$. If $n\in\mathcal{N}$, then $0=\langle Pn,m\rangle=\langle n,Pm\rangle=\langle n,m\rangle$, so $m\perp\mathcal{N}$. Hence $\|m\|=\operatorname{dist}(m,\mathcal{N})$. ■

**6.4. Lemma.** If $h\in\mathcal{H}$, then $\gamma(A)\operatorname{dist}(h,\ker A)\leq\|Ah\|$.

**Proof.** Let $P$ be the projection of $\mathcal{H}$ onto $(\ker A)^\perp$; then $\|Ph\|=\operatorname{dist}(h,\ker A)$. Hence $\|Ah\|=\|APh\|\geq\gamma(A)\|Ph\|=\gamma(A)\operatorname{dist}(h,\ker A)$. ■

If the role of $\gamma(A)$ in the next and subsequent propositions impresses the reader as somewhat mysterious, reflect that if $A$ is invertible, then $\gamma(A)=\|A^{-1}\|^{-1}$ (Exercise 1). Now in Corollary VII.2.3, it was shown that if $\mathcal{A}$ is a Banach algebra, $a_0\in\mathcal{A}$, and $b_0a_0=1$, then $a+b$ is left invertible whenever $\|b\|<\|b_0\|^{-1}$. Of course, a similar result holds for right invertible elements. The number $\gamma(A)$ is trying to play the role of the reciprocal of the norm of a one-sided inverse.

For example, if $A$ is left invertible, then $\operatorname{ran}A$ is closed and $\ker A=(0)$; hence $A\in\mathcal{SF}$. The next result implies that if $\|B\|<\gamma(A)$, then $A+B$ is left invertible.

**6.5. Proposition.** If $A\in\mathcal{SF}$ and $B\in\mathcal{B}(\mathcal{H})$ such that $\|B\|<\gamma(A)$, then $A+B\in\mathcal{SF}$ and:

(a) $\dim\ker(A+B)\leq\dim\ker A$;

(b) $\dim\operatorname{ran}(A+B)^\perp\leq\dim\operatorname{ran}A^\perp$.

**Proof.** First note that because $A\in\mathcal{SF}$, $\gamma(A)>0$.

If $h\in\ker(A+B)$ and $h\ne0$, then $Ah=-Bh$. By Lemma 6.4, $\gamma(A)\operatorname{dist}(h,\ker A)\leq\|Bh\|\leq\|B\|\|h\|<\gamma(A)\|h\|$. Thus $\operatorname{dist}(h,\ker A)<\|h\|$ for every nonzero vector $h$ in $\ker(A+B)$. By Lemma 6.3, (a) holds.



<a id="pdf-page-380"></a>
Since $\|B\|=\|B^*\|$ and $\gamma(A)=\gamma(A^*)$, (a) implies that $\dim\ker(A^*+B^*)\leq\dim\ker A^*$. But this inequality is equivalent to (b).

It remains to prove that $\operatorname{ran}(A+B)$ is closed. Since $A\in\mathcal{SF}$, either $\dim\ker A<\infty$ or $\dim\ker A^*<\infty$. Suppose $\dim\ker A<\infty$. It will be shown that $A+B\in\mathcal{F}_l$ by using Theorem 2.3(f) and showing that if $\delta<\gamma(A)-\|B\|$, then $\{h:\|(A+B)h\|\leq\delta\|h\|\}$ contains no infinite dimensional manifold. Indeed, if it did, it would contain a finite dimensional subspace $\mathcal M$ with $\dim\mathcal M>\dim\ker A$. By Lemma 6.3 there is a non-zero vector $h$ in $\mathcal M$ with $\|h\|=\operatorname{dist}(h,\ker A)$. Now $\|(A+B)h\|\leq\delta\|h\|$, so Lemma 6.4 implies that
$$
\gamma(A)\|h\|=\gamma(A)\operatorname{dist}(h,\ker A)
\leq\|Ah\|\leq\|(A+B)h\|+\|Bh\|
\leq(\delta+\|B\|)\|h\|<\gamma(A)\|h\|,
$$
a contradiction. Thus $A+B\in\mathcal{F}_l$ and so $\operatorname{ran}(A+B)$ is closed.

If $\dim\ker A=\infty$, then $\dim\ker A^*<\infty$. The argument of the preceding paragraph gives that $\operatorname{ran}(A^*+B^*)$ is closed. By (VI.1.10), $\operatorname{ran}(A+B)$ is closed. $\blacksquare$

**6.6. Proposition.** *If $A\in\mathcal{SF}$ and either $\ker A=(0)$ or $\operatorname{ran}A=\mathcal H$, then there is a $\delta>0$ such that if $\|B-A\|<\delta$, then $\dim\ker B=\dim\ker A$ and $\dim\operatorname{ran}B=\dim\operatorname{ran}A$.*

**Proof.** By Proposition 6.5 and Theorem 3.12 there is a $\delta>0$ such that if $\|B-A\|<\delta$, then $\operatorname{ind}A=\operatorname{ind}B$, $\dim\ker B\leq\dim\ker A$, and $\dim(\operatorname{ran}B)^\perp\leq\dim(\operatorname{ran}A)^\perp$. Since one of these dimensions for $A$ is 0, the proposition is proved. $\blacksquare$

If both $\ker A$ and $\operatorname{ran}A$ are nonzero, then there are semi-Fredholm operators $B$ that are arbitrarily close to $A$ such that $\dim\ker B<\dim\ker A$ (see Exercise 2). In fact, just about anything that can go wrong here does go wrong. However, $\dim\ker(A-\lambda)$ does behave rather nicely as a function of $\lambda$.

**6.7. Theorem.** *If $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$, then there is a $\delta>0$ such that $\dim\ker(A-\mu)$ and $\dim(\operatorname{ran}(A-\mu))^\perp$ are constant for $0<|\mu-\lambda|<\delta$.*

**Proof.** We may assume that $\lambda=0$. We may also assume that $\ker A$ is finite dimensional. Indeed, if this is not the case, then $\ker A^*$ must be finite dimensional and the proof that follows applies to $A^*$. But observe that if the conclusion of the theorem is demonstrated for $A^*$, then it also holds for $A$. It follows that for each $n\geq1$, $A^n\in\mathcal{SF}$ (Theorem 3.7). Thus $\mathcal M_n=\operatorname{ran}A^n$ is closed. Note that $\mathcal M_{n+1}\subseteq\mathcal M_n$ and $A\mathcal M_n=\mathcal M_{n+1}$. Let $\mathcal M=\bigcap_{n=1}^{\infty}\mathcal M_n$ and put $B=A|_{\mathcal M}$.

**Claim.** $B\mathcal M=\mathcal M$.

Since $\ker A$ is finite dimensional and the spaces $\mathcal M_n$ are decreasing, there is an integer $m$ such that $\mathcal M_n\cap\ker A=\mathcal M_m\cap\ker A$ for all $n\geq m$. If $h\in\mathcal M$ and $n\geq m$, there is an $f_n$ in $\mathcal M_n$ such that $h=Af_n$. But $f_m-f_n\in(\ker A)\cap\mathcal M_m=(\ker A)\cap\mathcal M_n$. Therefore $f_m\in\mathcal M_n$ for every $n\geq m$. That is, $f_m\in\mathcal M$ and so $h=Af_m=Bf_m\in B\mathcal M$.



<a id="pdf-page-381"></a>
Thus $B\in\mathcal{SF}$ and $\operatorname{ind}B=\dim\ker B$. By (3.12) and (6.5) there is a $\delta>0$ such that if $|\mu|<\delta$, then $\dim\ker(B-\mu)\leq\dim\ker B$, $\dim\operatorname{ran}(B-\mu)^\perp=0$, and $\operatorname{ind}(B-\mu)=\operatorname{ind}B$. Thus $\dim\ker(B-\mu)=\dim\ker B$ for $|\mu|<\delta$. Also, choose $\delta$ such that $\operatorname{ind}(A-\mu)=\operatorname{ind}A$ for $|\mu|<\delta$.

On the other hand, if $\mu\ne0$, then $\ker(A-\mu)\subseteq\mathcal M$. In fact, if $h\in\ker(A-\mu)$, then $A^nh=\mu^nh$, so that $h=A^n(\mu^{-n}h)\in\mathcal M_n$ for every $n$. Thus for $0<|\mu|<\delta$, $\dim\ker(A-\mu)=\dim\ker(B-\mu)=\dim\ker B$; that is, $\dim\ker(A-\mu)$ is constant for $0<|\mu|<\delta$. Since $\operatorname{ind}(A-\mu)$ is constant for these values of $\mu$, $\dim\operatorname{ran}(A-\mu)^\perp$ is also constant. $\blacksquare$

The next result is from Putnam [1968].

**6.8. Theorem.** *If $\lambda\in\partial\sigma(A)$, then either $\lambda$ is an isolated point of $\sigma(A)$ or $\lambda\in\sigma_{le}(A)\cap\sigma_{re}(A)$.*

**Proof.** Suppose $\lambda\in\partial\sigma(A)$ but $\lambda$ is not a point of $\sigma_{le}(A)\cap\sigma_{re}(A)$. Thus $A-\lambda\in\mathcal{SF}$. By the preceding theorem, there is a $\delta>0$ such that $A-\mu\in\mathcal{SF}$ and $\dim\ker(A-\mu)$ and $\dim\operatorname{ran}(A-\mu)^\perp$ are constant for $0<|\mu-\lambda|<\delta$. Since $\lambda\in\partial\sigma(A)$, there is a $\nu$ with $0<|\lambda-\nu|<\delta$ such that $A-\nu$ is invertible. Therefore $\ker(A-\mu)=(0)=\operatorname{ran}(A-\mu)^\perp$ for $0<|\lambda-\mu|<\delta$. But $A-\mu\in\mathcal{SF}$ for these values of $\mu$ and hence has closed range. It follows that $A-\mu$ is invertible whenever $0<|\lambda-\mu|<\delta$. This says that $\lambda$ is an isolated point of $\sigma(A)$. $\blacksquare$

What happens if $\lambda$ is an isolated point of $\sigma(A)$?

**6.9. Proposition.** *If $\lambda$ is an isolated point of $\sigma(A)$, the following statements are equivalent.*

(a) $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$.

(b) The Riesz idempotent $E(\lambda)$ has finite rank.

(c) $A-\lambda\in\mathcal F$ and $\operatorname{ind}(A-\lambda)=0$.

**Proof.** Exercise 4.

If $n\in\mathbb Z\cup\{\pm\infty\}$ and $A\in\mathcal B(\mathcal H)$, define

$$
P_n(A)\equiv\{\lambda\in\sigma(A):A-\lambda\in\mathcal{SF}\text{ and }\operatorname{ind}(A-\lambda)=n\}.
$$

So for $n\ne0$, $P_n(A)$ is an open subset of the plane; the set $P_0(A)$ consists of an open set together with some isolated points of $\sigma(A)$. In fact, Proposition 6.9 can be used to show that $P_0(A)$ contains precisely the isolated points of $\sigma(A)$ for which the Riesz idempotent has finite rank. The proof of the next result is easy.

**6.10. Proposition.** *If $A\in\mathcal B(\mathcal H)$, then $\sigma_e(A)=[\sigma_{le}(A)\cap\sigma_{re}(A)]\cup P_{+\infty}(A)\cup P_{-\infty}(A)$.*



<a id="pdf-page-382"></a>
**6.11. Definition.** If $A\in\mathcal{B}(\mathcal{H})$, then the *Weyl spectrum* of $A$, $\sigma_w(A)$, is defined by

$$
\sigma_w(A)=\bigcap\{\sigma(A+K):K\in\mathcal{B}_0\}.
$$

Note that since $\sigma_e(A+K)=\sigma_e(A)$ for every compact operator, $\sigma_w(A)$ is nonempty and $\sigma_e(A)\subseteq\sigma_w(A)$. The way to think of the Weyl spectrum is that it is the largest part of the spectrum of $A$ that remains unchanged under compact perturbations. It is clear that $\sigma_w(A)=\sigma_w(A+K)$ for every $K$ in $\mathcal{B}_0$ and $\sigma_w(A)\subseteq\sigma(A)$. The following is a result of Schechter [1965].

**6.12. Theorem.** *If $A\in\mathcal{B}(\mathcal{H})$, then $\sigma_w(A)=\sigma_e(A)\cup\bigcup_{n\ne0}P_n(A)$.*

**PROOF.** Clearly $X\equiv\sigma_e(A)\cup\bigcup_{n\ne0}P_n(A)\subseteq\sigma_w(A)$. Now suppose $\lambda\notin X$. Then $A-\lambda\in\mathcal{F}$ and $\operatorname{ind}(A-\lambda)=0$. By Exercise 3.7 there is a finite rank operator $F$ such that $A+F-\lambda$ is invertible. Hence $\lambda\notin\sigma(A+F)$ so that $\lambda\notin\sigma_w(A)$. ■

So for every operator $A$ in $\mathcal{B}(\mathcal{H})$ there is a *spectral picture* for $A$ (a term coined in Pearcy [1978]). There are the open sets $\{P_n(A):0<|n|\leq\infty\}$, the set $P_0(A)=G_0\cup D$ where $D$ consists of isolated points $\lambda$ for which $\dim E(\lambda)=n_\lambda<\infty$, and there is the remainder of $\sigma(A)$, which is the set $\sigma_{le}(A)\cap\sigma_{re}(A)$. The next result is due to Conway [1985].

**6.13. Proposition.** *Let $K$ be a compact subset of $\mathbb{C}$, let $\{G_n:-\infty\leq n\leq\infty\}$ be disjoint open subsets of $K$ (some possibly empty), let $D$ be a subset of the set of isolated points of $K$, and for each $\lambda$ in $D$ let $n_\lambda\in\{1,2,\ldots\}$. Then there is an operator $A$ on $\mathcal{H}$ such that $\sigma(A)=K$, $P_n(A)=G_n$ for $0<|n|\leq\infty$, $P_0(A)=G_0\cup D$, and $\dim E(\lambda)=n_\lambda$ for every $\lambda$ in $D$.*

We prove only a special case of this result; the general case is left to the reader. Let $K$ be any compact subset of $\mathbb{C}$ and let $G$ be an open subset of $K$. Put $H=\operatorname{int}[\operatorname{cl}G]$; so $G\subseteq H$, but it may be that $H\ne G$. However, $\partial H=\partial[\operatorname{cl}H]$. Let $Tf=zf$ for $f$ in $L_a^2(H)$, so $H=P_{-1}(T)$, $\sigma(T)=\operatorname{cl}H$, and $\sigma_{le}(T)\cap\sigma_{re}(T)=\partial H=\partial[\operatorname{cl}G]$. Let $\{\lambda_k\}$ be a countable dense subset of $K\setminus G$ and let $N$ be the diagonalizable normal operator with $\sigma_p(N)=\{\lambda_k\}$ and such that $\dim\ker(N-\lambda_k)=\infty$ for each $\lambda_k$. If $0<n\leq\infty$ and $A=N\oplus T^{(n)}$, then $\sigma(A)=K$, $P_{-n}(A)=G$, and $K\setminus G=\sigma_{le}(A)\cap\sigma_{re}(A)$.

## EXERCISES

1. If $A$ is an invertible operator, show that $\gamma(A)=\|A^{-1}\|^{-1}$.

2. Let $A\in\mathcal{F}$ and suppose that $\ker A\ne(0)$ and $\operatorname{ran}A^\perp\ne(0)$. Show that for every $\delta>0$ there is an operator $B$ in $\mathcal{F}$ such that $\|B-A\|<\delta$, $\dim\ker B<\dim\ker A$, and $\dim\operatorname{ran}B^\perp<\dim\operatorname{ran}A^\perp$.

3. If $A\in\mathcal{SF}$, show that there is a $\delta>0$ such that $\dim\ker(A-\mu)=\dim\ker A$ and $\dim\operatorname{ran}(A-\mu)^\perp=\dim\operatorname{ran}A^\perp$ for $|\mu|<\delta$ if $\ker A\subseteq\operatorname{ran}A^n$ for every $n\geq1$.

4. Prove Proposition 6.9.



<a id="pdf-page-383"></a>
5. Prove Proposition 6.10.

6. If $\lambda\in\partial P_n(A)$ and $n\ne 0$, show that $\operatorname{ran}(A-\lambda)$ is not closed. What happens if $n=0$?

7. (Stampfli [1974].) If $A\in\mathcal B(\mathcal H)$, then there is a $K$ in $\mathcal B_0(\mathcal H)$ such that $\sigma(A+K)=\sigma_w(A)$.

8. Prove Proposition 6.13.

9. (Conway [1985].) If $L$ and $R$ are nonempty compact subsets of $\mathbb C$, then there is a bounded operator $A$ on $\mathcal H$ such that $\sigma_l(A)=L$ and $\sigma_r(A)=R$ if and only if $\partial L\subseteq R$ and $\partial R\subseteq L$.

