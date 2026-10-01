# VII. Banach Algebras and Spectral Theory for Operators on a Banach Space


<a id="pdf-page-202"></a>
CHAPTER VII

# Banach Algebras and Spectral Theory for Operators on a Banach Space

The theory of Banach algebras is a large area in functional analysis with several subdivisions and applications to diverse areas of analysis and the rest of mathematics. Some monographs on this subject are by Bonsall and Duncan [1973] and C.E. Rickart [1960].

A significant change occurs in this chapter that will affect the remainder of this book. In order to prove that the spectrum of an element of a Banach algebra is nonvoid (Section 3), it is necessary to assume that the underlying field of scalars $\mathbb{F}$ is the field of complex numbers $\mathbb{C}$. It will be assumed from Section 3 until the end of this book that all vector spaces are over $\mathbb{C}$. This will also enable us to apply the theory of analytic functions to the study of Banach algebras and linear operators.

In this chapter only the rudiments of this subject are discussed. Enough, however, is presented to allow a treatment of the basics of spectral theory for operators on a Banach space.

## §1. Elementary Properties and Examples

<!-- BEGIN BACKGROUND BG-VII.block1 -->
<a id="bg-vii-1"></a>
### Lemma BG-VII.1 — Passing limits through multiplication

In a Banach algebra, multiplication is jointly continuous. If $\sum_n\|a_n\|<\infty$ and $\sum_m\|b_m\|<\infty$, the double series $\sum_{n,m}a_nb_m$ converges absolutely and may be summed in either order; its value is $(\sum_na_n)(\sum_mb_m)$.

**Proof.** The estimate
$$
\|a_nb_n-ab\|\leq\|a_n\|\,\|b_n-b\|+\|a_n-a\|\,\|b\|
$$
proves continuity, since a convergent sequence is bounded. For series, $\sum_{n,m}\|a_nb_m\|\leq(\sum_n\|a_n\|)(\sum_m\|b_m\|)<\infty$. Tails outside sufficiently large finite rectangles are small, which proves the Cauchy property and independence of the order of summation. Rectangular partial sums are products of partial sums, so continuity identifies their limit. $\square$

This is the analytic justification for multiplying infinite series in the algebra. It does not permit reversing factors: multiplication may be noncommutative.
<!-- END BACKGROUND BG-VII.block1 -->

An *algebra* over $\mathbb{F}$ is a vector space $\mathcal{A}$ over $\mathbb{F}$ that also has a multiplication defined on it that makes $\mathcal{A}$ into a ring such that if $\alpha\in\mathbb{F}$ and $a,b\in\mathcal{A}$, $\alpha(ab)=(\alpha a)b=a(\alpha b)$.

**1.1. Definition.** A *Banach algebra* is an algebra $\mathcal{A}$ over $\mathbb{F}$ that has a norm $\|\cdot\|$ relative to which $\mathcal{A}$ is a Banach space and such that for all $a,b$ in $\mathcal{A}$,

$$
\text{1.2}\qquad \|ab\|\leq\|a\|\|b\|.
$$



<a id="pdf-page-203"></a>
If $\mathcal A$ has an identity, $e$, then it is assumed that $\|e\|=1$.

The fact that (1.2) is satisfied is not essential. If $\mathcal A$ is an algebra and has a norm relative to which $\mathcal A$ is a Banach space and is such that the map of $\mathcal A\times\mathcal A\to\mathcal A$ defined by $(a,b)\mapsto ab$ is continuous, then there is an equivalent norm on $\mathcal A$ that satisfies (1.2) (Exercise 1).

If $\mathcal A$ has an identity $e$, then the map $\alpha\mapsto\alpha e$ is an isomorphism of $\mathbb F$ into $\mathcal A$ and $\|\alpha e\|=|\alpha|$. So it will be assumed that $\mathbb F\subseteq\mathcal A$ via this identification. Thus the identity will be denoted by 1.

The content of the next proposition is that if $\mathcal A$ does not have an identity, it is possible to find a Banach algebra $\mathcal A_1$ that contains $\mathcal A$, that has an identity, and is such that $\dim\mathcal A_1/\mathcal A=1$.

**1.3. Proposition.** *If $\mathcal A$ is a Banach algebra without an identity, let $\mathcal A_1=\mathcal A\times\mathbb F$. Define algebraic operations on $\mathcal A_1$ by*

(i) $(a,\alpha)+(b,\beta)=(a+b,\alpha+\beta)$;

(ii) $\beta(a,\alpha)=(\beta a,\beta\alpha)$;

(iii) $(a,\alpha)(b,\beta)=(ab+\alpha b+\beta a,\alpha\beta)$.

*Define $\|(a,\alpha)\|=\|a\|+|\alpha|$. Then $\mathcal A_1$ with this norm and the algebraic operations defined in (i), (ii), and (iii) is a Banach algebra with identity $(0,1)$ and $a\mapsto(a,0)$ is an isometric isomorphism of $\mathcal A$ into $\mathcal A_1$.*

**Proof.** Only (1.2) will be verified here; the remaining details are left to the reader. If $(a,\alpha),(b,\beta)\in\mathcal A_1$, then
$$
\begin{aligned}
\|(a,\alpha)(b,\beta)\|
&=\|(ab+\beta a+\alpha b,\alpha\beta)\|\\
&=\|ab+\beta a+\alpha b\|+|\alpha\beta|\\
&\leq\|a\|\|b\|+|\beta|\|a\|+|\alpha|\|b\|+|\alpha||\beta|\\
&=\|(a,\alpha)\|\|(b,\beta)\|.
\end{aligned}
$$
$\blacksquare$

**1.4. Example.** If $X$ is a compact space, then $\mathcal A=C(X)$ is a Banach algebra if $(fg)(x)=f(x)g(x)$ whenever $f,g\in\mathcal A$ and $x\in X$. Note that $\mathcal A$ is abelian and has an identity (the constantly 1 function).

If $X$ is completely regular and $\mathcal A=C_b(X)$, then $\mathcal A$ is also a Banach algebra. In fact, $C_b(X)\cong C(\beta X)$ (V.6) so that this is a special case of Example 1.4. Another special case is $l^\infty$.

**1.5. Example.** If $X$ is a locally compact space, $\mathcal A=C_0(X)$ is a Banach algebra when the multiplication is defined pointwise as in the preceding example. $\mathcal A$ is abelian, but if $X$ is not compact, $\mathcal A$ does not have an identity. If $X_\infty$ is the one-point compactification of $X$, then $C(X_\infty)\supseteq C_0(X)$ and $C(X_\infty)$ is a Banach algebra with identity.

Note that $c_0$ is a special case of Example 1.5.

**1.6. Example.** If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\mathcal A=L^\infty(X,\Omega,\mu)$, then $\mathcal A$ is an abelian Banach algebra with identity if the operations are defined pointwise.



<a id="pdf-page-204"></a>
**1.7. Example.** Let $\mathcal X$ be a Banach space and put $\mathcal A=\mathcal B(\mathcal X)$. If multiplication is defined by composition, then $\mathcal A$ is a Banach algebra with identity, $1$. If $\dim\mathcal X\geq 2$, $\mathcal A$ is not abelian.

**1.8. Example.** If $\mathcal X$ is a Banach space and $\mathcal A=\mathcal B_0(\mathcal X)$, the compact operators on $\mathcal X$, then $\mathcal A$ is a Banach algebra without identity if $\dim\mathcal X=\infty$. In fact, $\mathcal B_0(\mathcal X)$ is an ideal of $\mathcal B(\mathcal X)$.

Note that a special case of Example 1.7 occurs when $\mathcal A=M_n(\mathbb F)$, the $n\times n$ matrices, where $\mathcal A$ is given the norm resulting when $M_n(\mathbb F)$ is identified with $\mathcal B(\mathbb F^n)$.

**1.9. Example.** Let $G$ be a locally compact topological group and let $M(G)=$ all finite regular Borel measures on $G$. If $\mu,\nu\in M(G)$, define $L:C_0(G)\to\mathbb F$ by

$$
L(f)=\iint f(xy)\,d\mu(x)\,d\nu(y)
=\iint f(xy)\,d\nu(y)\,d\mu(x).
$$

Then $L$ is a linear functional on $C_0(G)$ and

$$
\begin{aligned}
|L(f)|&\leq\iint |f(xy)|\,d|\mu|(x)\,d|\nu|(y)\\
&\leq\|f\|\,\|\mu\|\,\|\nu\|.
\end{aligned}
$$

So $L\in C_0(G)^*=M(G)$. Define $\mu*\nu$ by $L(f)=\int f\,d(\mu*\nu)$ for $f$ in $C_0(G)$. That is,

$$
\int f\,d(\mu*\nu)=\iint f(xy)\,d\mu(x)\,d\nu(y). \tag{1.10}
$$

Note that $\|\mu*\nu\|=\|L\|\leq\|\mu\|\,\|\nu\|$. If follows that $M(G)$ is a Banach algebra with this definition of multiplication. The product $\mu*\nu$ is called the *convolution* of $\mu$ and $\nu$.

Let $e=$ the identity of $G$ and let $\delta_e=$ the unit point mass at $e$. If $f\in C_0(G)$, then

$$
\begin{aligned}
\int f\,d(\mu*\delta_e)
&=\iint f(xy)\,d\mu(x)\,d\delta_e(y)\\
&=\int f(xe)\,d\mu(x)\\
&=\int f\,d\mu.
\end{aligned}
$$

So $\mu*\delta_e=\mu$; similarly, $\delta_e*\mu=\mu$. Hence $\delta_e$ is the identity for $M(G)$.

If $x,y\in G$, then it is easy to check that $\delta_x*\delta_y=\delta_{xy}$, and $M(G)$ is abelian if and only if $G$ is abelian.



<a id="pdf-page-205"></a>
**1.11. Example.** Let $G$ be a $\sigma$-compact locally compact group and let $m=$ right Haar measure on $G$. That is, $m$ is a non-negative regular Borel measure on $G$ such that $m(U)>0$ for every nonempty open subset $U$ of $G$ and $\int f(xy)\,dm(x)=\int f(x)\,dm(x)$ for every $f$ in $C_c(G)$ (the continuous functions $f:G\to\mathbb F$ with compact support). If $G$ is compact, the existence of $m$ was established in Section V.11. If $G$ is not compact, $m$ exists but its existence must be established by nonfunctional analytic methods. If $G$ is not assumed to be $\sigma$-compact, then a Haar measure exists but it is not regular in the sense defined in this book. (See Nachbin [1965].)

If $f,g\in L^1(m)$, let $\mu=fm$ and $\nu=gm$ as in the proof of (V.8.1). Then $\mu,\nu\in M(G)$ and $\|\mu\|=\|f\|_1$, $\|\nu\|=\|g\|_1$. In fact, the Radon–Nikodym Theorem makes it possible to identify $L^1(m)$ with a closed subspace of $M(G)$. Is it a closed subalgebra?

Let $\phi\in C_c(G)$. Then

$$
\begin{aligned}
\int \phi\,d(\mu*\nu)
&=\int\!\!\int \phi(xy)f(x)g(y)\,dm(x)\,dm(y)\\
&=\int g(y)\left[\int \phi(xy)f(x)\,dm(x)\right]dm(y)\\
&=\int g(y)\left[\int \phi(x)f(xy^{-1})\,dm(x)\right]dm(y)\\
&=\int \phi(x)\left[\int f(xy^{-1})g(y)\,dm(y)\right]dm(x)\\
&=\int \phi(x)h(x)\,dm(x),
\end{aligned}
$$

where $h(x)=\int f(xy^{-1})g(y)\,dm(y)$, $x$ in $G$. It follows that $h\in L^1(m)$ (see Exercise 4). Thus $\mu*\nu=hm$, so $L^1(m)$ is a Banach subalgebra of $M(G)$. In fact, the preceding discussion enables us to define $f*g$ in $L^1(m)$ for $f,g$ in $L^1(m)$ by

$$
f*g(x)=\int f(xy^{-1})g(y)\,dm(y).
$$

The algebra $L^1(m)$ is denoted by $L^1(G)$.

It can be shown that $L^1(G)$ is abelian if and only if $G$ is abelian and $L^1(G)$ has an identity if and only if $G$ is discrete (in which case $L^1(G)=M(G)$—what is $m$?). This algebra is examined more closely in Section 9.

If $\{\mathcal A_i\}$ is a collection of Banach algebras, let
$$
\bigoplus_0\mathcal A_i
\equiv
\left\{a\in\prod_i\mathcal A_i:\text{ for all }\varepsilon>0,\ \{i:\|a(i)\|\geq\varepsilon\}\text{ is finite}\right\}.
$$

**1.12. Proposition.** *If $\{\mathcal A_i\}$ is a collection of Banach algebras, $\bigoplus_0\mathcal A_i$ and $\bigoplus_\infty\mathcal A_i$ are Banach algebras.*

**Proof.** Exercise.



<a id="pdf-page-206"></a>
## EXERCISES

1. Let $\mathcal A$ be an algebra that is also a Banach space and such that if $a\in\mathcal A$, the maps $x\mapsto ax$ and $x\mapsto xa$ of $\mathcal A\to\mathcal A$ are continuous. Let $\mathcal A_1=\mathcal A\times\mathbb F$ as in Proposition 1.3. If $a\in\mathcal A$, define $L_a:\mathcal A_1\to\mathcal A_1$ by $L_a(x,\xi)=(ax+\xi a,0)$. Show that $L_a\in\mathcal B(\mathcal A_1)$ and if $\lvert\!\lvert\!\lvert a\rvert\!\rvert\!\rvert=\|L_a\|$, then $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert$ is equivalent to the norm of $\mathcal A$ and $\mathcal A$ with $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert$ is a Banach algebra.

2. Complete the proof of Proposition 1.3.

3. Verify the statements made in Examples (1.4) through (1.9) and (1.11).

4. Let $G$ be a locally compact group. (a) If $\phi\in C_c(G)$ and $\varepsilon>0$, show that there is an open neighborhood $U$ of $e$ in $G$ such that $\|\phi_x-\phi_y\|<\varepsilon$ whenever $xy^{-1}\in U$. [Here $\phi_x(z)=\phi(xz)$.] (b) Show that if $f\in L^p(G)$, $1\leqslant p<\infty$, and $\varepsilon>0$, there is an open neighborhood $U$ of $e$ in $G$ such that $\|f_x-f_y\|_p<\varepsilon$ whenever $xy^{-1}\in U$. (c) Show that if $f\in L^1(G)$ and $g\in L^\infty(G)$, $h(x)=\int f(xy^{-1})g(y)\,dm(y)$ defines a bounded continuous function $h:G\to\mathbb F$. (d) If $f,g\in L^1(G)$ and $h$ is defined as in (c), show that $h\in L^1(G)$.

5. Prove Proposition 1.12.

6. Let $\{\mathcal A_i:i\in I\}$ be a collection of Banach algebras. (a) Show that $\bigoplus_0\mathcal A_i$ is a closed ideal of $\bigoplus_\infty\mathcal A_i$. (b) Show that $\bigoplus_\infty\mathcal A_i$ has an identity if and only if each $\mathcal A_i$ has an identity. (c) Show that $\bigoplus_0\mathcal A_i$ has an identity if $I$ is finite and each $\mathcal A_i$ has an identity.

7. If $X$, $Y$ are completely regular, show that $C_b(X)\oplus_\infty C_b(Y)$ is isometrically isomorphic to $C_b(X\oplus Y)$, where $X\oplus Y$ is the disjoint union of $X$ and $Y$.

8. If $X$ and $Y$ are locally compact, show that $C_0(X)\oplus_\infty C_0(Y)$ is isometrically isomorphic to $C_0(X\oplus Y)$.

9. Let $\{X_i:i\in I\}$ be a collection of locally compact spaces and let $X=$ the disjoint union of these spaces furnished with the topology $\{U\subseteq X:U\cap X_i\text{ is open in }X_i\text{ for all }i\}$. Show that $X$ is locally compact and $\bigoplus_0 C_0(X_i)$ is isometrically isomorphic to $C_0(X)$.

## §2. Ideals and Quotients

<!-- BEGIN BACKGROUND BG-VII.block2 -->
<a id="bg-vii-2"></a>
### Lemma BG-VII.2 — A quantitative Neumann-series estimate

If $\|b\|<1$, then $1-b$ is invertible and
$$
(1-b)^{-1}=\sum_{n=0}^\infty b^n,\qquad
\left\|(1-b)^{-1}-\sum_{n=0}^N b^n\right\|
\leq\frac{\|b\|^{N+1}}{1-\|b\|}.
$$
If $a$ is invertible and $\|a^{-1}h\|<1$, then $a+h=a(1+a^{-1}h)$ is invertible.

**Proof.** Submultiplicativity gives $\|b^n\|\leq\|b\|^n$, so completeness supplies the series and the geometric tail bound. Multiplication of its $N$th partial sum by $1-b$ on either side gives $1-b^{N+1}$; pass to the limit using BG-VII.1. Apply the result with $b=-a^{-1}h$ for the perturbation statement. $\square$

The inverse lies in a closed unital subalgebra containing $b$, since every partial sum lies there. This small observation later explains why spectra of an element in different algebras agree near infinity but may differ in bounded holes.
<!-- END BACKGROUND BG-VII.block2 -->

If $\mathcal A$ is an algebra, a *left ideal* of $\mathcal A$ is a subalgebra $\mathcal M$ of $\mathcal A$ such that $ax\in\mathcal M$ whenever $a\in\mathcal A$, $x\in\mathcal M$. A *right ideal* of $\mathcal A$ is a subalgebra $\mathcal M$ such that $xa\in\mathcal M$ whenever $a\in\mathcal A$, $x\in\mathcal M$. A *(bilateral) ideal* is a subalgebra of $\mathcal A$ that is both a left ideal and a right ideal.

If $a\in\mathcal A$ and $\mathcal A$ has an identity 1, say that $a$ is *left invertible* if there is an $x$ in $\mathcal A$ with $xa=1$. Similarly, define *right invertible* and *invertible* elements. If $a$ is invertible and $x,y\in\mathcal A$ such that $xa=1=ay$, then $y=1y=(xa)y=x(ay)=x1=x$. So if $a$ is invertible, there is a unique element $a^{-1}$ such that $aa^{-1}=a^{-1}a=1$.

If $\mathcal M$ is a left ideal in $\mathcal A$, $a\in\mathcal M$, and $a$ is left invertible, then $\mathcal M=\mathcal A$. In



<a id="pdf-page-207"></a>
fact, if $xa=1$, then $1\in\mathcal M$ since $\mathcal M$ is a left ideal. Thus for $y$ in $\mathcal A$, $y=y1\in\mathcal M$. This forms a link between ideals and invertibility.

In the case of a Banach algebra some bonuses occur due to the interplay of the norm and the algebra. The results of this section will be for Banach algebras with an identity. To discuss invertibility this is, of course, the only feasible setting. For Banach algebras without an identity some analogous results can be obtained, however, by a consideration of the algebra obtained by adjoining an identity (1.3). The concept of a modular ideal and a modular unit can also be employed (see Exercise 6).

The next proof is based on the geometric series.

**2.1. Lemma.** *If $\mathcal A$ is a Banach algebra with identity and $x\in\mathcal A$ such that $\|x-1\|<1$, then $x$ is invertible.*

**Proof.** Let $y=1-x$; so $\|y\|=r<1$. Since $\|y^n\|\leqslant\|y\|^n=r^n$ (Why?), $\sum_{n=0}^{\infty}\|y^n\|<\infty$. Hence $z=\sum_{n=0}^{\infty}y^n$ converges in $\mathcal A$. If $z_n=1+y+y^2+\cdots+y^n$,

$$
z_n(1-y)=(1+y+\cdots+y^n)-(y+y^2+\cdots+y^{n+1})=1-y^{n+1}.
$$

But $\|y^{n+1}\|\leqslant r^{n+1}$, so $y^{n+1}\to0$ as $n\to\infty$. Hence $z(1-y)=\lim z_n(1-y)=1$. Similarly, $(1-y)z=1$. So $(1-y)$ is invertible and $(1-y)^{-1}=z=\sum_0^\infty y^n$. But $1-y=1-(1-x)=x$. $\blacksquare$

Note that completeness was used to show that $\sum y^n$ converges.

**2.2. Theorem.** *If $\mathcal A$ is a Banach algebra with identity, $G_l=\{a\in\mathcal A:a\text{ is left invertible}\}$, $G_r=\{a\in\mathcal A:a\text{ is right invertible}\}$, and $G=\{a\in\mathcal A:a\text{ is invertible}\}$, then $G_l$, $G_r$, and $G$ are open subsets of $\mathcal A$. Also, the map $a\mapsto a^{-1}$ of $G\to G$ is continuous.*

**Proof.** Let $a_0\in G_l$ and let $b_0\in\mathcal A$ such that $b_0a_0=1$. If $\|a-a_0\|<\|b_0\|^{-1}$, then $\|b_0a-1\|=\|b_0(a-a_0)\|<1$. By the preceding lemma, $x=b_0a$ is invertible. If $b=x^{-1}b_0$, then $ba=1$. Hence $G_l\supseteq\{a\in\mathcal A:\|a-a_0\|<\|b_0\|^{-1}\}$ and $G_l$ must be open. Similarly, $G_r$ is open. Since $G=G_l\cap G_r$ (Why?), $G$ is open.

To prove that $a\mapsto a^{-1}$ is a continuous map of $G\to G$, first assume that $\{a_n\}$ is a sequence in $G$ such that $a_n\to1$. Let $0<\delta<1$ and suppose $\|a_n-1\|<\delta$. From the preceding lemma, $a_n^{-1}=(1-(1-a_n))^{-1}=\sum_{k=0}^{\infty}(1-a_n)^k=1+\sum_{k=1}^{\infty}(1-a_n)^k$. Hence

$$
\begin{aligned}
\|a_n^{-1}-1\|
&=\left\|\sum_{k=1}^{\infty}(1-a_n)^k\right\|\\
&\leqslant\sum_{k=1}^{\infty}\|1-a_n\|^k\\
&<\delta/(1-\delta).
\end{aligned}
$$



<a id="pdf-page-208"></a>
If $\varepsilon>0$ is given, then $\delta$ can be chosen such that $\delta/(1-\delta)<\varepsilon$. So $\|a_n-1\|<\delta$ implies $\|a_n^{-1}-1\|<\varepsilon$. Hence $\lim a_n^{-1}=1$.

Now let $a\in G$ and suppose $\{a_n\}$ is a sequence in $G$ such that $a_n\to a$. Hence $a^{-1}a_n\to 1$. By the preceding paragraph, $a_n^{-1}a=(a^{-1}a_n)^{-1}\to 1$. Hence $a_n^{-1}=a_n^{-1}aa^{-1}\to a^{-1}$. ■

Two facts surfaced in the preceding proofs that are worth recording for the future.

**2.3. Corollary.** *Let $\mathcal A$ be a Banach algebra with identity.*

(a) *If $\|a-1\|<1$, then $a^{-1}=\sum_{k=0}^{\infty}(1-a)^k$.*

(b) *If $b_0a_0=1$ and $\|a-a_0\|<\|b_0\|^{-1}$, then $a$ is left invertible.*

A *maximal ideal* is a proper ideal that is contained in no larger proper ideal.

**2.4. Corollary.** *If $\mathcal A$ is a Banach algebra with identity, then*

(a) *the closure of a proper left, right, or bilateral ideal is a proper left, right, or bilateral ideal;*

(b) *a maximal left, right, or bilateral ideal is closed.*

**Proof.** (a) Let $\mathcal M$ be a proper left ideal and let $G_l$ be the set of left-invertible elements in $\mathcal A$. It follows that $\mathcal M\cap G_l=\square$. (See the introduction to this section.) Thus $\mathcal M\subseteq\mathcal A\setminus G_l$. By the preceding theorem, $\mathcal A\setminus G_l$ is closed. Hence $\operatorname{cl}\mathcal M\subseteq\mathcal A\setminus G_l$; and thus $\operatorname{cl}\mathcal M\ne\mathcal A$. It is easy to check that $\operatorname{cl}\mathcal M$ is an ideal. The proof of the remainder of (a) is similar.

(b) If $\mathcal M$ is a maximal left ideal, $\operatorname{cl}\mathcal M$ is a proper left ideal by (a). Hence $\mathcal M=\operatorname{cl}\mathcal M$ by maximality. ■

If $\mathcal A$ does not have an identity, then $\mathcal A$ may contain some proper, dense ideals. For example, let $\mathcal A=C_0(\mathbb R)$. Then $C_c(\mathbb R)$, the continuous functions with compact support, is a dense ideal in $C_0(\mathbb R)$. There is something that can be said, however (see Exercise 6).

**2.5. Proposition.** *If $\mathcal A$ is a Banach algebra with identity, then every proper left, right, or bilateral ideal is contained in a maximal ideal of the same type.*

The proof of the preceding proposition is an exercise in the application of Zorn’s Lemma and is left to the reader. Actually, this is a theorem from algebra and it is not necessary to assume that $\mathcal A$ is a Banach algebra.

Let $\mathcal A$ be a Banach algebra and let $\mathcal M$ be a proper closed ideal. Note that $\mathcal A/\mathcal M$ becomes an algebra. Indeed, $(x+\mathcal M)(y+\mathcal M)=xy+\mathcal M$ is a well-defined multiplication on $\mathcal A/\mathcal M$. (Why?)

**2.6. Theorem.** *If $\mathcal A$ is a Banach algebra and $\mathcal M$ is a proper closed ideal in $\mathcal A$, then $\mathcal A/\mathcal M$ is a Banach algebra. If $\mathcal A$ has an identity, so does $\mathcal A/\mathcal M$.*


<a id="pdf-page-209"></a>
**Proof.** We have already seen that $\mathcal A/\mathcal M$ is a Banach space and, as was mentioned prior to the statement of the theorem, $\mathcal A/\mathcal M$ is an algebra. If $x,y\in\mathcal A$ and $u,v\in\mathcal M$, then $(x+u)(y+v)=xy+(xv+uy+uv)\in xy+\mathcal M$. Hence $\|(x+\mathcal M)(y+\mathcal M)\|=\|xy+\mathcal M\|\leqslant\|(x+u)(y+v)\|\leqslant\|x+u\|\|y+v\|$. Taking the infimum over all $u,v$ in $\mathcal M$ gives that $\|(x+\mathcal M)(y+\mathcal M)\|\leqslant\|x+\mathcal M\|\|y+\mathcal M\|$. The remainder of the proof is left to the reader. $\blacksquare$

It may be that $\mathcal A/\mathcal M$ has an identity even if $\mathcal A$ does not. For example, let $\mathcal A=C_0(\mathbb R)$ and let $\mathcal M=\{\phi\in C_0(\mathbb R):\phi(x)=0\text{ when }|x|\leqslant1\}$. If $\phi_0\in C_0(\mathbb R)$ such that $\phi_0(x)=1$ for $|x|\leqslant1$, then $\phi_0+\mathcal M$ is an identity for $\mathcal A/\mathcal M$. In fact, if $\phi\in C_0(\mathbb R)$, $(\phi\phi_0-\phi)(x)=0$ if $|x|\leqslant1$. Hence $(\phi+\mathcal M)(\phi_0+\mathcal M)=\phi+\mathcal M$ (see Exercises 6 through 9).

## EXERCISES

1. Let $\mathcal A$ be a Banach algebra and let $\mathcal L$ be all of the closed left ideals in $\mathcal A$. If $I_1,I_2\in\mathcal L$, define $I_1\vee I_2\equiv\operatorname{cl}(I_1+I_2)$ and $I_1\wedge I_2=I_1\cap I_2$. Show that with these definitions $\mathcal L$ is a complete lattice with a largest and a smallest element.

2. Let $X$ be locally compact. For every open subset $U$ of $X$, let $I(U)=\{\phi\in C_0(X):\phi=0\text{ on }X\setminus U\}$. Show that $U\mapsto I(U)$ is a lattice monomorphism of the collection of open subsets of $X$ into the lattice of close ideals of $C_0(X)$. (It is, in fact, surjective, but the proof of that should wait.)

3. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $I$ be an ideal in $L^\infty(X,\Omega,\mu)$ that is weak$^*$ closed. Show that there is a set $\Delta$ in $\Omega$ such that $I=\{\phi\in L^\infty(X,\Omega,\mu):\phi=0\text{ a.e. on }\Delta\}$.

4. Let $\mathcal A=\left\{\begin{bmatrix}\alpha&0\\ \beta&\alpha\end{bmatrix}:\alpha,\beta\in\mathbb F\right\}$ and let $\mathcal M=\left\{\begin{bmatrix}0&0\\ \beta&0\end{bmatrix}:\beta\in\mathbb F\right\}$. Show that $\mathcal A$ is a Banach algebra and $\mathcal M$ is a maximal ideal in $\mathcal A$.

5. Show that for $n\geqslant1$, $M_n(\mathbb C)$ has no nontrivial ideals. How about $M_n(\mathbb R)$?

6. Let $\mathcal A$ be a Banach algebra but do not assume that $\mathcal A$ has an identity. If $I$ is a left ideal of $\mathcal A$, say that $I$ is a *modular left ideal* if there is a $u$ in $\mathcal A$ such that $\mathcal A(1-u)\equiv\{a-au:a\in\mathcal A\}\subseteq I$; call such an element $u$ of $\mathcal A$ a *right modular unit* for $I$. Similarly, define *right modular ideals* and *left modular units*. Prove the following. (a) If $u$ is a right modular unit for the left ideal $I$ and $u\in I$, then $I=\mathcal A$. (b) Maximal modular left ideals are maximal left ideals. (c) If $I$ is a proper modular left ideal, then $I$ is contained in a maximal left ideal. (d) If $I$ is a proper modular left ideal and $u$ is a modular right unit for $I$, then $\|u-x\|\geqslant1$ for all $x$ in $I$ and $\operatorname{cl} I$ is a proper modular left ideal. (e) Every maximal modular left ideal of $\mathcal A$ is closed.

7. Using the terminology of Exercise 6, let $I$ be an ideal of $\mathcal A$. Show: (a) if $u$ is a right modular unit for $I$ and $v$ is a left modular unit for $I$, then $u-v\in I$. (b) If $I$ is closed, $\mathcal A/I$ has an identity if and only if there is a right modular unit and a left modular unit for $I$. Call an ideal $I$ such that $\mathcal A/I$ has an identity a *modular ideal*. An element $u$ such that $u+I$ is an identity for $\mathcal A/I$ is called a *modular identity* for $I$.



   <a id="pdf-page-210"></a>
8. If $\mathcal A$ is a Banach algebra, a net $\{e_i\}$ in $\mathcal A$ is called an *approximate identity* for $\mathcal A$ if $\sup_i\|e_i\|<\infty$ and for each $a$ in $\mathcal A$, $e_i a\to a$ and $ae_i\to a$. Show that $\mathcal A$ has an approximate identity if and only if there is a bounded subset $E$ of $\mathcal A$ such that for every $\varepsilon>0$ and for every $a$ in $\mathcal A$ there is an $e$ in $E$ with $\|ae-a\|+\|ea-a\|<\varepsilon$. See Wichmann [1973] for more information.

9. Show that if $X$ is locally compact, then $C_0(X)$ has an approximate identity.

10. If $\mathcal H$ is a Hilbert space, show that $\mathcal B_0(\mathcal H)$ has an approximate identity.

11. If $G$ is a locally compact group, show that $L^1(G)$ (1.11) has an approximate identity. [Hint: Let $\mathcal U=$ all neighborhoods $U$ of the identity $e$ of $G$ such that $\operatorname{cl}U$ is compact. Order $\mathcal U$ by reverse inclusion. For $U$ in $\mathcal U$, let $f_U=m(U)^{-1}\chi_U$. Then $\{f_U:U\in\mathcal U\}$ is an approximate identity for $L^1(G)$.]

12. For $0<r<1$, let $P_r:\partial\mathbb D\to[0,\infty)$ defined by $P_r(z)=\sum_{n=-\infty}^{\infty}r^{|n|}z^n$ (the *Poisson kernel*). Show that $\{P_r\}$ is an approximate identity for $L^1(\partial\mathbb D)$ (under convolution).

13. If $\mathcal H$ is a Hilbert space and $P$ is a projection, show that $\mathcal B_0(\mathcal H)P$ is a closed modular left ideal of $\mathcal B_0(\mathcal H)$. What is the associated right modular unit?

14. Find the minimal proper left ideals of $M_n(\mathbb F)$.

15. Find the minimal closed proper left ideals of $\mathcal B_0(\mathcal H)$, $\mathcal H$ a Hilbert space. How about for $\mathcal B_0(\mathcal X)$, $\mathcal X$ a Banach space?

16. What are the maximal modular left ideals of $\mathcal B_0(\mathcal H)$, $\mathcal H$ a Hilbert space?

## §3. The Spectrum

<!-- BEGIN BACKGROUND BG-VII.block3 -->
The scalar tools used in this section are developed from the beginning in the [complex-analysis background](background-complex-analysis.md): [power series](background-complex-analysis.md#ca-25), [Cauchy's formula and estimates](background-complex-analysis.md#ca-30), and [Liouville's theorem](background-complex-analysis.md#ca-33). The following additions explain exactly how those scalar facts apply to Banach-space-valued functions.

<a id="bg-vii-3"></a>
### Definition BG-VII.3 — Banach-valued contour integrals

For a continuous $F$ on the trace of a rectifiable curve $\gamma:[0,1]\to\mathbb C$, define $\int_\gamma F\,dz$ as the limit of tagged sums $\sum_jF(\gamma(\tau_j))(\gamma(t_j)-\gamma(t_{j-1}))$. Rectifiable means that the supremum of $\sum_j|\gamma(t_j)-\gamma(t_{j-1})|$ over partitions is finite; this supremum is the length $\ell(\gamma)$.

<a id="bg-vii-4"></a>
### Lemma BG-VII.4 — Existence, estimates, and scalarization of the integral

The integral above exists in a Banach space $X$ and satisfies
$$
\left\|\int_\gamma F\,dz\right\|\leq\ell(\gamma)\sup_\gamma\|F\|,
\qquad
x^*\left(\int_\gamma F\,dz\right)=\int_\gamma x^*(F)\,dz.
$$
Uniform convergence on the trace permits passage of limits through the integral.

**Proof.** Uniform continuity of $F\circ\gamma$ on $[0,1]$ shows that two tagged sums, after a common refinement of fine partitions, differ in norm by at most $\ell(\gamma)$ times a modulus of continuity tending to zero. Completeness gives their limit. The norm estimate holds for each sum and passes to the limit. A bounded functional commutes with finite sums and norm limits, proving scalarization. Apply the norm estimate to the difference of two integrands for the last assertion. $\square$

<a id="bg-vii-5"></a>
### Theorem BG-VII.5 — Weak analyticity implies norm analyticity

If $F:G\to X$ has the property that $x^*\circ F$ is holomorphic for every $x^*\in X^*$, then $F$ is norm-holomorphic. On each disk compactly contained in $G$, it satisfies the vector-valued Cauchy formula and a norm-convergent Taylor expansion.

**Proof.** On a compact disk $K\subset G$, each scalar function $x^*F$ is bounded. Apply uniform boundedness on the Banach space $X^*$ to the functionals $JF(z)$, $z\in K$: it gives $M=\sup_K\|F(z)\|<\infty$. On a smaller concentric disk, scalar Cauchy estimates give $|(x^*F)'(z)|\leq C M\|x^*\|$, with one $C$ depending only on the gap between the disks. Integrating along a segment in the smaller disk and taking the supremum over $\|x^*\|\leq1$ yields $\|F(z)-F(w)\|\leq CM|z-w|$. Hence $F$ is norm-continuous, so the contour integral in BG-VII.4 exists.

Apply scalar Cauchy's formula to $x^*F$ on a circle $|\zeta-z_0|=r$ contained in $G$. Scalarization and Hahn–Banach imply
$$
F(z)=\frac1{2\pi i}\int_{|\zeta-z_0|=r}\frac{F(\zeta)}{\zeta-z}\,d\zeta
\quad(|z-z_0|<r).
$$
Expand $(\zeta-z)^{-1}$ geometrically about $z_0$. The convergence is uniform when $|z-z_0|\leq s<r$, so BG-VII.4 allows termwise integration and gives $F(z)=\sum_{n\geq0}a_n(z-z_0)^n$ with $\|a_n\|\leq Mr^{-n}$. The derivative series also converges uniformly on smaller disks, since $\sum n(s/r)^{n-1}<\infty$. Thus $F$ has a norm derivative, continuous locally. $\square$

This supplies Exercise 3.4, which the source later uses without proof. Weak continuity alone does not similarly imply norm continuity. The special force here comes from scalar Cauchy estimates.

<a id="bg-vii-6"></a>
### Corollary BG-VII.6 — Nonempty spectra and the role of complex numbers

For a nonzero unital complex Banach algebra and $a$ in it, the spectrum is nonempty. More quantitatively, for $|z|>\|a\|$,
$$
R(z)=(z-a)^{-1}=\sum_{n=0}^\infty a^nz^{-n-1},\qquad
\|R(z)\|\leq\frac1{|z|-\|a\|}.
$$

**Proof.** The estimate and series follow from BG-VII.2. If the spectrum were empty, $R$ would be entire, using either its local Neumann expansion or the derivative calculation below. It tends to zero at infinity by the estimate and is bounded on each compact disk by continuity. Each $x^*R$ would therefore be a bounded entire scalar function, hence constant by Liouville and identically zero by its limit at infinity. Hahn–Banach would give $R=0$, impossible for an inverse. $\square$

<a id="bg-vii-7"></a>
### Lemma BG-VII.7 — Spectral radius without an unexplained power-series boundary

For $a$ in a unital complex Banach algebra, $\lim_n\|a^n\|^{1/n}$ exists. If $r=\sup_{\lambda\in\sigma(a)}|\lambda|$, this limit equals $r$.

**Proof.** If $a^m=0$ for some $m$, all sufficiently high powers vanish and the assertion follows from the finite Neumann inverse outside zero. Otherwise set $b_n=\|a^n\|>0$. The inequality $b_{n+m}\leq b_nb_m$ implies existence of the root limit: for fixed $m$, write $n=qm+s$, $0\leq s<m$, to get $b_n\leq b_m^q\max_{s<m}b_s$. Hence $\limsup b_n^{1/n}\leq b_m^{1/m}$ for every $m$, and the limit equals $\inf_m b_m^{1/m}$.

For $\lambda\in\sigma(a)$, factorization of $\lambda^n-a^n$ into commuting factors shows $\lambda^n\in\sigma(a^n)$, so $|\lambda|^n\leq\|a^n\|$. Thus $r$ is at most the limit. Conversely, $H(z)=(1-za)^{-1}$ is holomorphic for $|z|<1/r$, taking $1/r=\infty$ if $r=0$. Near zero its series is $\sum_{n\geq0}z^na^n$. Vector-valued Cauchy estimates on any circle $|z|=s<1/r$ give $\|a^n\|\leq M_s s^{-n}$. The root limit is at most $s^{-1}$. Let $s\uparrow1/r$ (or $s\to\infty$ when $r=0$). $\square$

This proves the precise missing analytic estimate in Proposition 3.8 and handles the case $r(a)=0$ without taking reciprocals of zero spectral points.
<!-- END BACKGROUND BG-VII.block3 -->

**3.1. Definition.** If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$, the *spectrum* of $a$, denoted by $\sigma(a)$, is defined by

$$
\sigma(a)=\{\alpha\in\mathbb F:a-\alpha\text{ is not invertible}\}.
$$

The *left spectrum*, $\sigma_l(a)$, is the set $\{\alpha\in\mathbb F:a-\alpha\text{ is not left invertible}\}$; the *right spectrum*, $\sigma_r(a)$, is defined similarly.

The *resolvent set* of $a$ is defined by $\rho(a)=\mathbb F\setminus\sigma(a)$. The *left* and *right resolvents* of $a$ are $\rho_l(a)=\mathbb F\setminus\sigma_l(a)$ and $\rho_r(a)=\mathbb F\setminus\sigma_r(a)$.

**3.2. Example.** Let $X$ be compact. If $f\in C(X)$, then $\sigma(f)=f(X)$. In fact, if $\alpha=f(x_0)$, then $f-\alpha$ has a zero and cannot be invertible. So $f(X)\subseteq\sigma(f)$. On the other hand, if $\alpha\notin f(X)$, $f-\alpha$ is a nonvanishing continuous function on $X$. Hence $(f-\alpha)^{-1}\in C(X)$ and so $f-\alpha$ is invertible. Thus $\alpha\notin\sigma(f)$.

**3.3. Example.** If $\mathcal X$ is a Banach space and $A\in\mathcal B(\mathcal X)$, then $\sigma(A)=\{\alpha\in\mathbb F:\text{ either }\ker(A-\alpha)\ne(0)\text{ or }\operatorname{ran}(A-\alpha)\ne\mathcal X\}$. In fact, this means that $\rho(A)=\mathbb F\setminus\sigma(A)=\{\alpha\in\mathbb F:A-\alpha\text{ is bijective}\}$. If $\alpha\in\rho(A)$, there is an operator $T$ in $\mathcal B(\mathcal X)$ such that $T(A-\alpha)=(A-\alpha)T=1$; clearly, $A-\alpha$ is bijective. On the other hand, if $A-\alpha$ is bijective, $(A-\alpha)^{-1}\in\mathcal B(\mathcal X)$ by the Inverse Mapping Theorem.



<a id="pdf-page-211"></a>
**3.4. Example.** If $\mathcal H$ is a Hilbert space and $A\in\mathcal B(\mathcal H)$, then
$\sigma_l(A)=\{\alpha\in\mathbb F:\inf\{\|(A-\alpha)h\|:\|h\|=1\}=0\}$. In fact, suppose $B\in\mathcal B(\mathcal H)$ such that $B(A-\alpha)=1$. If $\|h\|=1$, then $1=\|h\|=\|B(A-\alpha)h\|\leq\|B\|\|(A-\alpha)h\|$. So $\|(A-\alpha)h\|\geq\|B\|^{-1}$ whenever $\|h\|=1$.

Conversely, suppose $\|(A-\alpha)h\|\geq\delta>0$ whenever $\|h\|=1$. Note that $\ker(A-\alpha)=(0)$. It will now be shown that $\operatorname{ran}(A-\alpha)$ is closed. In fact, assume that $(A-\alpha)f_n\to g$. Then $\delta\|f_n-f_m\|\leq\|(A-\alpha)(f_n-f_m)\|=\|(A-\alpha)f_n-(A-\alpha)f_m\|$. Thus $\{f_n\}$ is a Cauchy sequence. Let $f_n\to f$. Then $g=\lim(A-\alpha)f_n=(A-\alpha)f$; hence $g\in\operatorname{ran}(A-\alpha)$. Let $\mathcal K=\operatorname{ran}(A-\alpha)$; so $(A-\alpha):\mathcal H\to\mathcal K$ is a bijection. Thus $(A-\alpha)^{-1}:\mathcal K\to\mathcal H$ is bounded. Define $B:\mathcal H\to\mathcal H$ by letting $B(k+h)=(A-\alpha)^{-1}k$ when $k\in\mathcal K$ and $h\in\mathcal K^\perp$. Thus $B\in\mathcal B(\mathcal H)$ and $B(A-\alpha)=1$.

**3.5. Example.** If $\mathcal A=M_2(\mathbb R)$ and $A=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$, then $\sigma(A)=\square$. In fact, $A-\alpha$ is not invertible if and only if $0=\det(A-\alpha)=\alpha^2+1$, which is impossible in $\mathbb R$.

The phenomenon of the last example does not occur if $\mathcal A$ is a Banach algebra over $\mathbb C$.

**3.6. Theorem.** *If $\mathcal A$ is a Banach algebra over $\mathbb C$ with an identity, then for each $a$ in $\mathcal A$, $\sigma(a)$ is a nonempty compact subset of $\mathbb C$. Moreover, if $|\alpha|>\|a\|$, $\alpha\notin\sigma(a)$ and $z\mapsto(z-a)^{-1}$ is an $\mathcal A$-valued analytic function defined on $\rho(a)$.*

Before beginning the proof, a few words on vector-valued analytic functions are in order. If $G$ is a region in $\mathbb C$ and $\mathcal X$ is a Banach space, define the derivative of $f:G\to\mathcal X$ at $z_0$ to be $\lim_{h\to0}h^{-1}[f(z_0+h)-f(z_0)]$ if the limit exists. Say that $f$ is analytic if $f$ has a continuous derivative on $G$. The whole theory of analytic functions transfers to this situation. The statements and proofs of such theorems as Cauchy’s Integral Formula, Liouville’s Theorem, etc., transfer verbatim. Also, $f:G\to\mathcal X$ is analytic if and only if for each $z_0$ in $G$ there is a sequence $x_0,x_1,x_2,\ldots$ in $\mathcal X$ such that $f(z)=\sum_{k=0}^{\infty}(z-z_0)^kx_k$ whenever $z\in B(z_0;r)$, where $r=\operatorname{dist}(z_0,\partial G)$. Moreover, the convergence is uniform on compact subsets of $B(z_0;r)$.

There is also a way of obtaining the vector-valued case as a consequence of the scalar-valued case (see Exercise 4).

**Proof of Theorem 3.6.** If $|\alpha|>\|a\|$, then $\alpha-a=\alpha(1-a/\alpha)$ and $\|a/\alpha\|<1$. By Corollary 2.3, $(1-a/\alpha)$ is invertible. Hence $\alpha-a$ is invertible and so $\alpha\notin\sigma(a)$. Thus $\sigma(a)\subseteq\{\alpha\in\mathbb C:|\alpha|\leq\|a\|\}$ and $\sigma(a)$ is bounded.

Let $G$ be the set of invertible elements of $\mathcal A$. The map $\alpha\mapsto(\alpha-a)$ is a continuous function of $\mathbb C\to\mathcal A$. Since $G$ is open and $\rho(a)$ is the inverse image of $G$ under this map, $\rho(a)$ is open. Thus $\sigma(a)=\mathbb C\setminus\rho(a)$ is compact.

Define $F:\rho(a)\to\mathcal A$ by $F(z)=(z-a)^{-1}$. In the identity $x^{-1}-y^{-1}=$



<a id="pdf-page-212"></a>
$x^{-1}(y-x)y^{-1}$, let $x=(\alpha+h-a)$ and $y=(\alpha-a)$, where $\alpha\in\rho(a)$ and $h\in\mathbb C$ such that $h\ne0$ and $\alpha+h\in\rho(a)$. This gives

$$
\begin{aligned}
\frac{F(\alpha+h)-F(\alpha)}{h}
&=\frac{(\alpha+h-a)^{-1}(-h)(\alpha-a)^{-1}}{h}\\
&=-(\alpha+h-a)^{-1}(\alpha-a)^{-1}.
\end{aligned}
$$

Since $(\alpha+h-a)^{-1}\to(\alpha-a)^{-1}$ as $h\to0$, $F'(\alpha)$ exists and

$$
F'(\alpha)=-(\alpha-a)^{-2}.
$$

Clearly $F':\rho(a)\to\mathcal A$ is continuous, so $F$ is analytic on $\rho(a)$.

From the first paragraph of the proof and Corollary 2.3, if $|z|>\|a\|$, then $F(z)=z^{-1}(1-a/z)^{-1}$. But as $z\to\infty$, $(1-a/z)\to1$ and so $(1-a/z)^{-1}\to1$. Thus $F(z)\to0$ as $z\to\infty$.

Therefore if $\rho(a)=\mathbb C$, $F$ is an entire function that vanishes at $\infty$. By Liouville’s Theorem $F$ is constant. Since $F'\ne0$, this is a contradiction. Thus $\rho(a)\ne\mathbb C$, or $\sigma(a)\ne\square$. ■

Because the spectrum of an element of a complex Banach algebra is not empty, the following assumption is made.

**Assumption.** *Henceforward, all Banach spaces and all Banach algebras are over $\mathbb C$.*

**3.7. Definition.** If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$, the *spectral radius* of $a$, $r(a)$, is defined by

$$
r(a)=\sup\{|\alpha|:\alpha\in\sigma(a)\}.
$$

Because $\sigma(a)\ne\square$ and is bounded, $r(a)$ is well defined and finite; because $\sigma(a)$ is compact, this supremum is attained.

Let $\mathcal A=M_2(\mathbb C)$ and let $A=\begin{bmatrix}0&0\\1&0\end{bmatrix}$. Then $A^2=0$ and $\sigma(A)=\{0\}$; so $r(A)=0$. So it is possible to have $r(A)=0$ with $A\ne0$.

**3.8. Proposition.** *If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$, $\lim\|a^n\|^{1/n}$ exists and*

$$
r(a)=\lim\|a^n\|^{1/n}.
$$

**Proof.** Let $G=\{z\in\mathbb C:z=0\text{ or }z^{-1}\in\rho(a)\}$. Define $f:G\to\mathcal A$ by $f(0)=0$ and for $z\ne0$, $f(z)=(z^{-1}-a)^{-1}$. Since $(a-\alpha)^{-1}\to0$ as $\alpha\to\infty$, $f$ is analytic on $G$, and so $f$ has a power series expansion. In fact, by Corollary 2.3, for $|z|<\|a\|^{-1}$,

$$
f(z)=\sum_{n=0}^{\infty}a^n/(z^{-1})^{n+1}
=z\sum_{n=0}^{\infty}z^na^n.
$$



<a id="pdf-page-213"></a>
From complex variable theory, this power series converges for $|z|<R\equiv\operatorname{dist}(0,\partial G)=\operatorname{dist}(0,\sigma(a)^{-1})$ (Here $\sigma(a)^{-1}=\{z^{-1}:z\in\sigma(a)\}$). Thus $R=\inf\{|\alpha|:\alpha^{-1}\in\sigma(a)\}=r(a)^{-1}$. Also, from the theory of power series, $R^{-1}=\limsup\|a^n\|^{1/n}$. Thus

$$
r(a)=\limsup\|a^n\|^{1/n}.
$$

Now if $\alpha\in\mathbb C$ and $n\geqslant1$, $\alpha^n-a^n=(\alpha-a)(\alpha^{n-1}+\alpha^{n-2}a+\cdots+a^{n-1})=(\alpha^{n-1}+\alpha^{n-2}a+\cdots+a^{n-1})(\alpha-a)$. So if $\alpha^n-a^n$ is invertible, $\alpha-a$ is invertible and $(\alpha-a)^{-1}=(\alpha^n-a^n)^{-1}(\alpha^{n-1}+\cdots+a^{n-1})$. So for $\alpha$ in $\sigma(a)$, $\alpha^n-a^n$ is not invertible for every $n\geqslant1$. By Theorem 3.6, $|\alpha|^n\leqslant\|a^n\|$. Hence $|\alpha|\leqslant\|a^n\|^{1/n}$ for all $n\geqslant1$ and $\alpha$ in $\sigma(a)$. So if $\alpha\in\sigma(a)$, $|\alpha|\leqslant\liminf\|a^n\|^{1/n}$. Taking the supremum over all $\alpha$ in $\sigma(a)$ gives that $r(a)\leqslant\liminf\|a^n\|^{1/n}\leqslant\limsup\|a^n\|^{1/n}=r(a)$. So $r(a)=\lim\|a^n\|^{1/n}$. $\blacksquare$

**3.9. Proposition.** Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$.

(a) If $\alpha\in\rho(a)$, then $\operatorname{dist}(\alpha,\sigma(a))\geqslant\|(\alpha-a)^{-1}\|^{-1}$.

(b) If $\alpha,\beta\in\rho(a)$, then

$$
\begin{aligned}
(\alpha-a)^{-1}-(\beta-a)^{-1}
&=(\beta-\alpha)(\alpha-a)^{-1}(\beta-a)^{-1}\\
&=(\beta-\alpha)(\beta-a)^{-1}(\alpha-a)^{-1}.
\end{aligned}
$$

**Proof.** (a) By Corollary 2.3, if $\alpha\in\rho(a)$ and $\|x-(\alpha-a)\|<\|(\alpha-a)^{-1}\|^{-1}$, $x$ is invertible. So if $\beta\in\mathbb C$ and $|\beta|<\|(\alpha-a)^{-1}\|^{-1}$, $(\beta+\alpha-a)$ is invertible; that is, $\alpha+\beta\in\rho(a)$. Hence $\operatorname{dist}(\alpha,\sigma(a))\geqslant\|(\alpha-a)^{-1}\|^{-1}$. (b) This follows by letting $x=\alpha-a$ and $y=\beta-a$ in the identity $x^{-1}-y^{-1}=x^{-1}(y-x)y^{-1}=y^{-1}(y-x)x^{-1}$. $\blacksquare$

The identity in part (b) of the preceding proposition is called the *resolvent identity* and the function $\alpha\mapsto(\alpha-a)^{-1}$ of $\rho(a)\to\mathcal A$ is called the *resolvent* of $a$.

## Exercises

1. Let $S$ be the unilateral shift on $l^2$ (II.2.10). Show that $S$ is left invertible but not right invertible.

2. If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$ and is nilpotent (that is, $a^n=0$ for some $n$), then $\sigma(a)=\{0\}$.

3. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $\mathcal A=L^\infty(X,\Omega,\mu)$ (1.6). If $\phi\in\mathcal A$, show that the following are equivalent: (a) $\alpha\in\sigma(\phi)$; (b) $0=\sup\{\inf\{|\phi(x)-\alpha|:x\in X\setminus\Delta\}:\Delta\in\Omega\text{ and }\mu(\Delta)=0\}$; (c) if $\varepsilon>0$, $\mu(\{x\in X:|\phi(x)-\alpha|<\varepsilon\})>0$; (d) if $\nu$ is the measure defined on the Borel subsets of $\mathbb C$ by $\nu(\Delta)=\mu(\phi^{-1}(\Delta))$, then $\alpha$ is in the support of $\nu$.

4. If $G$ is an open subset of $\mathbb C$ and $f:G\to\mathcal X$ is a function such that for each $x^*$ in $\mathcal X^*$, $x^*\circ f:G\to\mathbb C$ is analytic, then $f$ is analytic. If the word “continuous” is substituted for both occurrences of the word “analytic”, is the preceding statement still true?



   <a id="pdf-page-214"></a>
5. If $\mathcal A$ is a Banach algebra with identity, $\{a_n\}\subseteq\mathcal A$, $a_n\to a$, $\alpha_n\in\sigma(a_n)$, and $\alpha_n\to\alpha$, then $\alpha\in\sigma(a)$.

6. If $\mathcal A$ is a Banach algebra with identity and $r:\mathcal A\to[0,\infty)$ is the spectral radius, show that $r$ is upper semicontinuous. If $a\in\mathcal A$ such that $r(a)=0$, show that $r$ is continuous at $a$.

7. If $\mathcal A$ is a Banach algebra with identity, $a,b\in\mathcal A$, and $\alpha$ is a nonzero scalar such that $(\alpha-ab)$ is invertible, show that $(\alpha-ba)$ is invertible and $(\alpha-ba)^{-1}=\alpha^{-1}+\alpha^{-1}b(\alpha-ab)^{-1}a$. Show that $\sigma(ab)\cup\{0\}=\sigma(ba)\cup\{0\}$ and give an example such that $\sigma(ab)\ne\sigma(ba)$.

## §4. The Riesz Functional Calculus

<!-- BEGIN BACKGROUND BG-VII.block4 -->
Before this section read [winding numbers](background-complex-analysis.md#ca-37), [the homological Cauchy theorem](background-complex-analysis.md#ca-38), and [contours surrounding a compact set](background-complex-analysis.md#ca-39). “Positively oriented” for a system can include clockwise inner boundaries: the **total** winding number must be one on the region being enclosed and zero on its holes. A single large circle need not fit in the domain of $f$.

<a id="bg-vii-8"></a>
### Lemma BG-VII.8 — Why the double contour manipulation is valid

For continuous Banach-algebra-valued $F$ and $G$ on rectifiable contours $\gamma$ and $\lambda$,
$$
\left(\int_\gamma F(z)dz\right)\left(\int_\lambda G(w)dw\right)
=\int_\gamma\int_\lambda F(z)G(w)\,dw\,dz.
$$
For any continuous integrand on the product of the two traces, the two iterated integrals agree with the double integral (with the order of algebra factors kept fixed).

**Proof.** Products of finite tagged sums equal the corresponding double sums. Uniform continuity on the compact parameter square and the bound $\ell(\gamma)\ell(\lambda)\sup\|H\|$ show convergence of these double sums independently of the order of refinement. Joint continuity of multiplication identifies their limit with the product of the two integrals. $\square$

<a id="bg-vii-9"></a>
### Lemma BG-VII.9 — The estimate underlying continuity of functional calculus

Fix an admissible contour system $\Gamma$ in the resolvent set enclosing $\sigma(a)$. If $f$ and $g$ are holomorphic on its surrounding domain, then
$$
\|f(a)-g(a)\|\leq
\frac{\ell(\Gamma)}{2\pi}\sup_{z\in\{\Gamma\}}\|(z-a)^{-1}\|
\sup_{z\in\{\Gamma\}}|f(z)-g(z)|.
$$

**Proof.** Subtract the two defining contour integrals and apply BG-VII.4, using submultiplicativity. The resolvent norm is bounded on the contour because it is continuous on its compact trace. $\square$

Thus locally uniform convergence of scalar functions implies norm convergence of their functional-calculus values. Pointwise convergence alone supplies no such estimate. Also, commutation with $a$ implies commutation with every resolvent: multiply $b(z-a)=(z-a)b$ by inverses on both sides. Passing this identity through the contour integral proves Proposition 4.9 directly, without requiring Runge approximation.

<a id="bg-vii-10"></a>
### Lemma BG-VII.10 — Analytic division at a zero

If $f$ is holomorphic near $\alpha$, then the quotient $(f(z)-f(\alpha))/(z-\alpha)$ extends holomorphically to $\alpha$, with value $f'(\alpha)$. If $f$ is holomorphic on a neighborhood of a compact set $K$ and has no zeros on $K$, then $1/f$ is holomorphic on a neighborhood of $K$.

**Proof.** The Taylor expansion $f(z)=\sum c_n(z-\alpha)^n$ turns the quotient into $\sum_{n\geq1}c_n(z-\alpha)^{n-1}$ near $\alpha$, proving the first assertion. For the second, the open set where $f\ne0$ contains $K$; on it the quotient rule gives $(1/f)'=-f'/f^2$. $\square$

These facts construct both auxiliary functions in the Spectral Mapping Theorem. Commutation of the functional-calculus factors is essential when turning a product inverse into an inverse of $a-\alpha$.
<!-- END BACKGROUND BG-VII.block4 -->

Before coming to the main course of this section, it is necessary to have an appetizer from complex analysis. Many of these topics can be found in Conway [1978] with complete proofs. Only a few results are presented here.

If $\gamma$ is a closed rectifiable curve in $\mathbb C$ and $a\notin\{\gamma\}\equiv\{\gamma(t):0\leq t\leq1\}$, then the *winding number of $\gamma$ about $a$* is defined to be the number

$$
n(\gamma;a)=\frac{1}{2\pi i}\int_\gamma\frac{1}{z-a}\,dz.
$$

The number $n(\gamma;a)$ is always an integer and is constant on each component of $\mathbb C\setminus\{\gamma\}$ and vanishes on the unbounded component of $\mathbb C\setminus\{\gamma\}$.

Let $G$ be an open subset of $\mathbb C$ and let $\mathcal X$ be a Banach space. If $f:G\to\mathcal X$ is analytic and $x^*\in\mathcal X^*$, then $z\mapsto\langle f(z),x^*\rangle$ is analytic on $G$ and its derivative is $\langle f'(z),x^*\rangle$. By Exercise 4 of the preceding section, if $f:G\to\mathcal X$ is a function such that $z\mapsto\langle f(z),x^*\rangle$ is analytic for each $x^*$ in $\mathcal X^*$, then $f:G\to\mathcal X$ is analytic. These facts will help in discussing and proving many of the results below.

If $\gamma$ is a rectifiable curve in $G$ and $f$ is a continuous function defined in a neighborhood of $\{\gamma\}$ with values in $\mathcal X$, then $\int_\gamma f$ can be defined as for a scalar-valued $f$ as the limit in $\mathcal X$ of sums of the form

$$
\sum_j[\gamma(t_j)-\gamma(t_{j-1})]f(\gamma(t_j)),
$$

where $\{t_0,t_1,\ldots,t_n\}$ is a partition of $[0,1]$. Hence $\int_\gamma f=\int_0^1 f(\gamma(t))\,d\gamma(t)\in\mathcal X$. It is easy to see that for every $x^*$ in $\mathcal X^*$, $\left\langle\int_\gamma f,x^*\right\rangle=\int_\gamma\langle f(\cdot),x^*\rangle$.

**4.1. Cauchy’s Theorem.** If $\mathcal X$ is a Banach space, $G$ is an open subset of $\mathbb C$, $f:G\to\mathcal X$ is an analytic function, and $\gamma_1,\ldots,\gamma_m$ are closed rectifiable curves in $G$ such that $\sum_{j=1}^m n(\gamma_j;a)=0$ for all $a$ in $\mathbb C\setminus G$, then $\sum_{j=1}^m\int_{\gamma_j}f=0$.

**Proof.** If $x^*\in\mathcal X^*$, then
$$
\left\langle\sum_{j=1}^m\int_{\gamma_j}f,x^*\right\rangle
=\sum_{j=1}^m\int_{\gamma_j}\langle f(\cdot),x^*\rangle=0
$$
by the scalar-valued version of Cauchy’s Theorem. Hence $\sum_{j=1}^m\int_{\gamma_j}f=0$. $\blacksquare$



<a id="pdf-page-215"></a>
**4.2. Cauchy’s Integral Formula.** *If $\mathcal{X}$ is a Banach space, $G$ is an open subset of $\mathbb{C}$, $f:G\to\mathcal{X}$ is analytic, $\gamma$ is a closed rectifiable curve in $G$ such that $n(\gamma;a)=0$ for every $a$ in $\mathbb{C}\setminus G$, and $\lambda\in G\setminus\{\gamma\}$, then for every integer $k\geq 0$,*

$$
n(\gamma;\lambda)f^{(k)}(\lambda)
=\frac{k!}{2\pi i}\int_\gamma (z-\lambda)^{-(k+1)}f(z)\,dz.
$$

**4.3. Definition.** A closed rectifiable curve $\gamma$ is *positively oriented* if for every $a$ in $G\setminus\{\gamma\}$, $n(\gamma;a)$ is either 0 or 1. In this case the *inside* of $\gamma$, denoted by $\operatorname{ins}\gamma$, is defined by

$$
\operatorname{ins}\gamma\equiv
\{a\in\mathbb{C}\setminus\{\gamma\}:n(\gamma;a)=1\}.
$$

The *outside* of $\gamma$, denoted by $\operatorname{out}\gamma$, is defined by

$$
\operatorname{out}\gamma\equiv
\{a\in\mathbb{C}\setminus\{\gamma\}:n(\gamma;a)=0\}.
$$

Thus $\mathbb{C}=\{\gamma\}\cup\operatorname{ins}\gamma\cup\operatorname{out}\gamma$.

A curve $\gamma:[0,1]\to\mathbb{C}$ is *simple* if $\gamma(s)=\gamma(t)$ implies that either $s=t$ or $s=0$ and $t=1$. The Jordan Curve Theorem says that if $\gamma$ is a simple closed rectifiable curve, then $\mathbb{C}\setminus\{\gamma\}$ has two components and $\{\gamma\}$ is the boundary of each. Hence $n(\gamma;a)$ takes on only two values and one of these must be 0; the other must be $\pm1$.

If $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ is a collection of closed rectifiable curves, then $\Gamma$ is *positively oriented* if: (a) $\{\gamma_i\}\cap\{\gamma_j\}=\square$ for $i\ne j$; (b) for $a$ in $\mathbb{C}\setminus\bigcup_{j=1}^{m}\{\gamma_j\}$, $n(\Gamma;a)\equiv\sum_{j=1}^{m}n(\gamma_j;a)$ is either 0 or 1; (c) each $\gamma_j$ is a simple curve. The *inside* of $\Gamma$, $\operatorname{ins}\Gamma$, is defined by

$$
\operatorname{ins}\Gamma\equiv\{a:n(\Gamma;a)=1\}.
$$

The *outside* of $\Gamma$, $\operatorname{out}\Gamma$, is defined by

$$
\operatorname{out}\Gamma\equiv\{a:n(\Gamma;a)=0\}.
$$

Let $\{\Gamma\}\equiv\bigcup\{\gamma_j:1\leq j\leq m\}$.

**4.4. Proposition.** *If $G$ is an open subset of $\mathbb{C}$ and $K$ is a compact subset of $G$, then there is a positively oriented system of curves $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ in $G\setminus K$ such that $K\subseteq\operatorname{ins}\Gamma$ and $\mathbb{C}\setminus G\subseteq\operatorname{out}\Gamma$. The curves $\gamma_1,\ldots,\gamma_m$ can be found such that they are infinitely differentiable.*

The proof of this proposition can be found on p. 195 of Conway [1978], though some details are missing.

If $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ and each $\gamma_j$ is rectifiable, define

$$
\int_\Gamma f=\sum_{j=1}^{m}\int_{\gamma_j}f
$$

whenever $f$ is continuous in a neighborhood of $\{\Gamma\}$.

Let $\mathcal{A}$ be a Banach algebra with identity and let $a\in\mathcal{A}$. One of the principal


<a id="pdf-page-216"></a>
uses of Proposition 4.4 in this book will occur when $K=\sigma(a)$. If $f:G\to\mathbb C$ is analytic and $\sigma(a)\subseteq G$, we will define an element $f(a)$ in $\mathcal A$ by

$$
f(a)=\frac{1}{2\pi i}\int_\Gamma f(z)(z-a)^{-1}\,dz. \tag{4.5}
$$

where $\Gamma$ is as in Proposition 4.4 with $K=\sigma(a)$. But first it must be shown that (4.5) does not depend on the choice of $\Gamma$. That is, it must be shown that $f(a)$ is well defined.

**4.6. Proposition.** *Let $\mathcal A$ be a Banach algebra with identity, let $a\in\mathcal A$, and let $G$ be an open subset of $\mathbb C$ such that $\sigma(a)\subseteq G$. If $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ and $\Lambda=\{\lambda_1,\ldots,\lambda_k\}$ are two positively oriented collections of curves in $G$ such that $\sigma(a)\subseteq\operatorname{ins}\Gamma\subseteq G$ and $\sigma(a)\subseteq\operatorname{ins}\Lambda\subseteq G$ and if $f:G\to\mathbb C$ is analytic, then*

$$
\int_\Gamma f(z)(z-a)^{-1}\,dz
=
\int_\Lambda f(z)(z-a)^{-1}\,dz.
$$

**Proof.** For $1\leq j\leq k$, let $\gamma_{m+j}=\lambda_j^{-1}$; that is, $\gamma_{m+j}(t)=\lambda_j(1-t)$ for $0\leq t\leq1$. If $z\notin G\setminus\sigma(a)$, then either $z\in\mathbb C\setminus G$ or $z\in\sigma(a)$. If $z\in\mathbb C\setminus G$, then $\sum_{j=1}^{m+k}n(\gamma_j;z)=n(\Gamma;z)-n(\Lambda;z)=0-0=0$. If $z\in\sigma(a)$, then $\sum_{j=1}^{m+k}n(\gamma_j;z)=n(\Gamma;z)-n(\Lambda;z)=1-1=0$. Thus $\Sigma\equiv\{\gamma_j:1\leq j\leq m+k\}$ is a system of closed curves in $U=G\setminus\sigma(a)$ such that $n(\Sigma;z)=0$ for all $z$ in $\mathbb C\setminus U$. Since $z\mapsto f(z)(z-a)^{-1}$ is analytic on $U$, Cauchy’s Theorem implies

$$
0=\int_\Sigma f(z)(z-a)^{-1}\,dz
=\int_\Gamma f(z)(z-a)^{-1}\,dz
-\int_\Lambda f(z)(z-a)^{-1}\,dz.
\qquad\blacksquare
$$

As was pointed out before, Proposition 4.6 implies that (4.5) gives a well-defined element $f(a)$ of $\mathcal A$ whenever $f$ is analytic in a neighborhood of $\sigma(a)$. Let $\operatorname{Hol}(a)=$ all of the functions that are analytic in a neighborhood of $\sigma(a)$. Note that $\operatorname{Hol}(a)$ is an algebra where if $f,g\in\operatorname{Hol}(a)$ and $f$ and $g$ have domains $D(f)$ and $D(g)$, then $fg$ and $f+g$ have domain $D(f)\cap D(g)$. $\operatorname{Hol}(a)$ is not, however, a Banach algebra.

**4.7. The Riesz Functional Calculus.** *Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$.*

(a) *The map $f\mapsto f(a)$ of $\operatorname{Hol}(a)\to\mathcal A$ is an algebra homomorphism.*

(b) *If $f(z)=\sum_{k=0}^{\infty}\alpha_kz^k$ has radius of convergence $>r(a)$, then $f\in\operatorname{Hol}(a)$ and $f(a)=\sum_{k=0}^{\infty}\alpha_ka^k$.*

(c) *If $f(z)\equiv1$, then $f(a)=1$.*

(d) *If $f(z)=z$ for all $z$, $f(a)=a$.*

(e) *If $f,f_1,f_2,\ldots$ are all analytic on $G$, $\sigma(a)\subseteq G$, and $f_n(z)\to f(z)$ uniformly on compact subsets of $G$, then $\|f_n(a)-f(a)\|\to0$ as $n\to\infty$.*

**Proof.** (a) Let $f,g\in\operatorname{Hol}(a)$ and let $G$ be an open neighborhood of $\sigma(a)$ on which both $f$ and $g$ are analytic. Let $\Gamma$ be a positively oriented system of



<a id="pdf-page-217"></a>
closed curves in $G$ such that $\sigma(a)\subseteq\operatorname{ins}\Gamma$. Let $\Lambda$ be a positively oriented system of closed curves in $G$ such that $(\operatorname{ins}\Gamma)\cup\{\Gamma\}=\operatorname{cl}(\operatorname{ins}\Gamma)\subseteq\operatorname{ins}\Lambda$. Then

$$
\begin{aligned}
f(a)g(a)
&=-\frac{1}{4\pi^{2}}
\left[\int_{\Gamma}f(z)(z-a)^{-1}\,dz\right]
\left[\int_{\Lambda}g(\zeta)(\zeta-a)^{-1}\,d\zeta\right]\\
&=-\frac{1}{4\pi^{2}}\int_{\Gamma}\int_{\Lambda}
f(z)g(\zeta)(z-a)^{-1}(\zeta-a)^{-1}\,d\zeta\,dz\\
\text{[by (3.9b)]}\qquad
&=-\frac{1}{4\pi^{2}}\int_{\Gamma}\int_{\Lambda}
f(z)g(\zeta)
\left[\frac{(z-a)^{-1}-(\zeta-a)^{-1}}{\zeta-z}\right]
\,d\zeta\,dz\\
&=-\frac{1}{4\pi^{2}}\int_{\Gamma}f(z)
\left[\int_{\Lambda}\frac{g(\zeta)}{\zeta-z}\,d\zeta\right]
(z-a)^{-1}\,dz\\
&\quad+\frac{1}{4\pi^{2}}\int_{\Lambda}g(\zeta)
\left[\int_{\Gamma}\frac{f(z)}{\zeta-z}\,dz\right]
(\zeta-a)^{-1}\,d\zeta.
\end{aligned}
$$

But for $\zeta$ on $\Lambda$, $\zeta\in\operatorname{out}\Gamma$ and hence $\int_{\Gamma}[f(z)/(\zeta-z)]\,dz=0$ (Cauchy’s Theorem). If $z\in\{\Gamma\}$, then $z\in\operatorname{ins}\Lambda$ and so $\int_{\Lambda}[g(\zeta)/(\zeta-z)]\,d\zeta=2\pi i g(z)$. Hence

$$
\begin{aligned}
f(a)g(a)
&=\frac{1}{2\pi i}\int_{\Gamma}f(z)g(z)(z-a)^{-1}\,dz\\
&=(fg)(a).
\end{aligned}
$$

The proof that $(\alpha f+\beta g)(a)=\alpha f(a)+\beta g(a)$ is left to the reader.

(c) and (d). Let $f(z)=z^{k}$, $k\geq 0$. Let $\gamma(t)=R\exp(2\pi it)$, $0\leq t\leq 1$, where $R>\|a\|$. So $\sigma(a)\subset\operatorname{ins}\gamma$, and hence

$$
\begin{aligned}
f(a)
&=\frac{1}{2\pi i}\int_{\gamma}z^{k}(z-a)^{-1}\,dz\\
&=\frac{1}{2\pi i}\int_{\gamma}z^{k-1}
\left(1-\frac{a}{z}\right)^{-1}\,dz\\
&=\frac{1}{2\pi i}\int_{\gamma}z^{k-1}
\sum_{n=0}^{\infty}a^{n}/z^{n}\,dz,
\end{aligned}
$$

since $\|a/z\|<1$ for $|z|=R$. Since this infinite series converges uniformly for $z$ on $\gamma$,

$$
f(a)=\sum_{n=0}^{\infty}
\left[\frac{1}{2\pi i}\int_{\gamma}\frac{1}{z^{n-k+1}}\,dz\right]a^{n}.
$$

If $n\ne k$, then $z^{-(n-k+1)}$ has a primitive and hence $\int_{\gamma}z^{-(n-k+1)}\,dz=0$. For $n=k$ this integral becomes $\int_{\gamma}z^{-1}\,dz=2\pi i$. Hence $f(a)=a^{k}$.

(e) Let $\Gamma=\{\gamma_{1},\ldots,\gamma_{m}\}$ be a positively oriented system of closed curves in



<a id="pdf-page-218"></a>
$G$ such that $\sigma(a)\subseteq\operatorname{ins}\Gamma$. Fix $1\leq k\leq m$; then

$$
\begin{aligned}
\left\|\int_{\gamma_k}f_n(z)(z-a)^{-1}\,dz-\int_{\gamma_k}f(z)(z-a)^{-1}\,dz\right\|
&=\left\|\int_0^1[f_n(\gamma_k(t))-f(\gamma_k(t))][\gamma_k(t)-a]^{-1}\,d\gamma_k(t)\right\|\\
&\leq\int_0^1|f_n(\gamma_k(t))-f(\gamma_k(t))|
\left\|[\gamma_k(t)-a]^{-1}\right\|\,d|\gamma_k|(t).
\end{aligned}
$$

Now $t\mapsto\|[\gamma_k(t)-a]^{-1}\|$ is continuous on $[0,1]$ and hence bounded by some constant, say $M$. Thus

$$
\begin{aligned}
\left\|\int_{\gamma_k}f_n(z)(z-a)^{-1}\,dz-\int_{\gamma_k}f(z)(a-a)^{-1}\,dz\right\|\\
\leq M\|\gamma_k\|\max\{|f_n(z)-f(z)|:z\in\{\gamma_k\}\},
\end{aligned}
$$

where $\|\gamma_k\|$ is the total variation (length) of $\gamma_k$. By hypothesis it follows that $\|f_n(a)-f(a)\|\to0$ as $n\to\infty$.

(b) If $p(z)=\sum_{k=0}^{n}\alpha_kz^k$ is a polynomial, then (a), (c), and (d) combine to give that $p(a)=\sum_{k=0}^{n}\alpha_ka^k$. Now let $f(z)=\sum_{k=0}^{\infty}\alpha_kz^k$ have radius of convergence $R>r(a)$, the spectral radius of $a$. If $p_n(z)=\sum_{k=0}^{n}\alpha_kz^k$, $p_n(z)\to f(z)$ uniformly on compact subsets of $\{z:|z|<R\}$. By (e), $p_n(a)\to f(a)$. So (b) follows. $\blacksquare$

The Riesz Functional Calculus is used in the study of Banach algebras and is especially useful in the study of linear operators on a Banach space (Sections 6 and 7). Now our attention must focus on the basic properties of this functional calculus. The first such property is its uniqueness.

**4.8. Proposition.** *Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$. Let $\tau:\operatorname{Hol}(a)\to\mathcal A$ be a homomorphism such that (a) $\tau(1)=1$, (b) $\tau(z)=a$, (c) if $\{f_n\}$ is a sequence of analytic functions on an open set $G$ such that $\sigma(a)\subseteq G$ and $f_n(z)\to f(z)$ uniformly on compact subsets of $G$, then $\tau(f_n)\to\tau(f)$. Then $\tau(f)=f(a)$ for every $f$ in $\operatorname{Hol}(a)$.*

**Proof.** The proof uses Runge’s Theorem (III.8.1), but first it must be shown that $\tau(f)=f(a)$ whenever $f$ is a rational function. If $n\geq1$, $\tau(z^n)=\tau(z)^n=a^n$; hence $\tau(p)=p(a)$ for any polynomial $p$. Let $q$ be a polynomial such that $q$ never vanishes on $\sigma(a)$, so $1/q\in\operatorname{Hol}(a)$. Also, $1=\tau(1)=\tau(q\cdot q^{-1})=\tau(q)\tau(q^{-1})=q(a)\tau(q^{-1})$. Hence $q(a)$ is invertible and $q(a)^{-1}=\tau(q^{-1})$. But using the Riesz Functional Calculus, a similar argument shows that $q(a)^{-1}=(1/q)(a)$. Thus $\tau(q^{-1})=(1/q)(a)$. Therefore if $f=p/q$, where $p$ and $q$ are polynomials and $q$ never vanishes on $\sigma(a)$, $\tau(f)=\tau(p\cdot q^{-1})=\tau(p)\tau(q^{-1})=p(a)(1/q)(a)=f(a)$.

Now let $f\in\operatorname{Hol}(a)$ and suppose $f$ is analytic on an open set $G$ such that $\sigma(a)\subseteq G$. By Runge’s theorem there are rational functions $\{f_n\}$ in $\operatorname{Hol}(a)$ such



<a id="pdf-page-219"></a>
that $f_n(z)\to f(z)$ uniformly on compact subsets of $G$. By (c) of the hypothesis, $\tau(f_n)\to\tau(f)$. But $\tau(f_n)=f_n(a)$ and $f_n(a)\to f(a)$ by (4.7e). Hence $\tau(f)=f(a)$. $\blacksquare$

A fact that has been implicit in the manipulations involving the functional calculus is that $f(a)$ and $g(a)$ commute for all $f$ and $g$ in $\operatorname{Hol}(a)$. In fact, if $\tau:\operatorname{Hol}(a)\to\mathcal A$ is defined by $\tau(f)=f(a)$, then $f(a)g(a)=\tau(fg)=\tau(gf)=g(a)f(a)$. Still more can be said.

**4.9. Proposition.** *If $a,b\in\mathcal A$, $ab=ba$, and $f\in\operatorname{Hol}(a)$, then $f(a)b=bf(a)$.*

**Proof.** An algebraic exercise demonstrates that $f(a)b=bf(a)$ if $f$ is a rational function with poles off $\sigma(a)$. The general result now follows by Runge’s Theorem. $\blacksquare$

**4.10. The Spectral Mapping Theorem.** *If $a\in\mathcal A$ and $f\in\operatorname{Hol}(a)$, then*

$$
\sigma(f(a))=f(\sigma(a)).
$$

**Proof.** If $\alpha\in\sigma(a)$, let $g\in\operatorname{Hol}(a)$ such that $f(z)-f(\alpha)=(z-\alpha)g(z)$. If it were the case that $f(\alpha)\notin\sigma(f(a))$, then $(a-\alpha)$ would be invertible with inverse $g(a)[f(a)-f(\alpha)]^{-1}$. Hence $f(\alpha)\in\sigma(f(a))$; that is, $f(\sigma(a))\subseteq\sigma(f(a))$.

Conversely, if $\beta\notin f(\sigma(a))$, then $g(z)=[f(z)-\beta]^{-1}\in\operatorname{Hol}(a)$ and so $g(a)[f(a)-\beta]=1$. Thus $\beta\notin\sigma(f(a))$; that is, $\sigma(f(a))\subseteq f(\sigma(a))$. $\blacksquare$

This section closes with an application of the functional calculus that is typical.

**4.11. Proposition.** *Suppose $a\in\mathcal A$ and $\sigma(a)=F_1\cup F_2$, where $F_1$ and $F_2$ are disjoint nonempty closed sets. Then there is a nontrivial idempotent $e$ in $\mathcal A$ such that*

(a) *if $ba=ab$, then $be=eb$;*

(b) *if $a_1=ae$ and $a_2=a(1-e)$, then $a=a_1+a_2$ and $a_1a_2=a_2a_1=0$;*

(c) *$\sigma(a_1)=F_1\cup\{0\}$, $\sigma(a_2)=F_2\cup\{0\}$.*

**Proof.** Let $G_1,G_2$ be disjoint open subsets of $\mathbb C$ such that $F_j\subset G_j$, $j=1,2$. Let $\Gamma$ be a positively oriented system of closed curves in $G_1$ such that $F_1\subseteq\operatorname{ins}\Gamma$, $F_2\subseteq\operatorname{out}\Gamma$. If $f=$ the characteristic function of $G_1$, $f\in\operatorname{Hol}(a)$; let $e=f(a)$. Since $f^2=f$, $e^2=e$. Part (a) follows from (4.9).

Note that $e(1-e)=0=(1-e)e$. Hence (b) is immediate. Let $f_1(z)=zf(z)$, $f_2(z)=z(1-f(z))$. It follows from (4.7a) that $a_j=f_j(a)$, $j=1,2$. Hence the Spectral Mapping Theorem implies that $\sigma(a_j)=f_j(\sigma(a))=F_j\cup\{0\}$. The proof that $e$ is neither 0 nor 1 is left to the reader. $\blacksquare$

Part (c) of the preceding proposition has the somewhat unattractive conclusion that $\sigma(a_1)=F_1\cup\{0\}$. It would be much neater if the conclusion were that $\sigma(a_1)=F_1$. This is, in a sense, the case. Since $a_1(1-e)=0$ and


<a id="pdf-page-220"></a>
$1-e\neq 0$, $a_1$ cannot be invertible. However, consider the algebra $\mathcal A_1\equiv\{b\in\mathcal A:ab=ba\text{ and }be=eb=b\}$. It is left to the reader to show that $\mathcal A_1$ is a Banach algebra and $e$ is the identity for $\mathcal A_1$. If $a_1$ is considered as an element of the algebra $\mathcal A_1$, then its spectrum as an element of $\mathcal A_1$ is $F_1$. This is an illustration of how the spectrum depends on the Banach algebra (the subject of the next section; also see Exercise 9).

## Exercises

1. Let $\mathcal A=C(X)$, $X$ compact (see Example 3.2). If $g\in C(X)$ and $f\in\operatorname{Hol}(g)$, show that $f(g)=f\circ g$.

2. Let $a$ be a nilpotent element of $\mathcal A$. For $f,g$ in $\operatorname{Hol}(a)$, give a necessary and sufficient condition on $f$ and $g$ that $f(a)=g(a)$.

3. Let $d\geq 1$ and let $A\in M_d(\mathbb C)$. Give a necessary and sufficient condition on $f$ in $\operatorname{Hol}(A)$ such that $f(A)=0$. (Hint: Consider the Jordan canonical form for $A$.)

4. If $\mathcal A$ is a Banach algebra with identity, $a\in\mathcal A$, $f\in\operatorname{Hol}(a)$, and $g$ is analytic in a neighborhood of $f(\sigma(a))$, then $g\circ f\in\operatorname{Hol}(a)$ and $g(f(a))=g\circ f(a)$.

5. If $\mathcal X$ is a Banach space, $A\in\mathcal B(\mathcal X)$, and $\mathcal M\leq\mathcal X$ such that $(A-\alpha)^{-1}\mathcal M\subseteq\mathcal M$ for all $\alpha$ in $\rho(A)$, show that $f(A)\mathcal M\subseteq\mathcal M$ whenever $f\in\operatorname{Hol}(A)$.

6. If $\mathcal X$ is a Banach space, $A\in\mathcal B(\mathcal X)$, and $f\in\operatorname{Hol}(A)$, show that $f(A)^*=f(A^*)$. (See (6.1) below.)

7. If $\mathcal H$ is a Hilbert space, $A\in\mathcal B(\mathcal H)$, and $f\in\operatorname{Hol}(A)$, show that $f(A)^*=\widetilde f(A^*)$, where $\widetilde f(z)=\overline{f(\bar z)}$ (See (6.1) below.)

8. If $\mathcal H$ is a Hilbert space, $A$ is a normal operator on $\mathcal H$, and $f\in\operatorname{Hol}(A)$, show that $f(A)$ is normal.

9. Let $\mathcal X$ be a Banach space and let $A\in\mathcal B(\mathcal X)$. Show that if $\sigma(A)=F_1\cup F_2$ where $F_1,F_2$ are disjoint closed subsets of $\mathbb C$, then there are topologically complementary subspaces $\mathcal X_1,\mathcal X_2$ of $\mathcal X$ such that (a) $B\mathcal X_j\subseteq\mathcal X_j$ $(j=1,2)$ whenever $BA=AB$; (b) if $A_j=A|_{\mathcal X_j}$, $\sigma(A_j)=F_j$; (c) there is an invertible operator $R:\mathcal X\to\mathcal X_1\oplus_1\mathcal X_2$ such that $RAR^{-1}=A_1\oplus A_2$.

10. Let $A\in M_d(\mathbb C)$, $\sigma(A)=\{\alpha_1,\ldots,\alpha_n\}$, where $\alpha_i\neq\alpha_j$ for $i\neq j$. Show that for $1\leq j\leq n$ there is a matrix $A_j$ in $M_{d_j}(\mathbb C)$ such that $\sigma(A_j)=\{\alpha_j\}$ and $A$ is similar to $A_1\oplus\cdots\oplus A_n$.

11. If $\mathcal A$ is a Banach algebra, $I$ is an ideal of $\mathcal A$ (not necessarily closed), $a\in I$, and $f\in\operatorname{Hol}(a)$ such that $f(0)=0$, show that $f(a)\in I$.

## §5. Dependence of the Spectrum on the Algebra

<!-- BEGIN BACKGROUND BG-VII.block5 -->
<a id="bg-vii-11"></a>
### Lemma BG-VII.11 — Boundary control extends polynomial limits

If polynomials $p_n$ are uniformly Cauchy on the unit circle, they converge uniformly on the closed disk to a continuous function holomorphic in the open disk.

**Proof.** The maximum modulus principle gives $\sup_{|z|\leq1}|p_n-p_m|\leq\sup_{|z|=1}|p_n-p_m|$, so they are uniformly Cauchy on the disk. Completeness of the scalar field gives a uniform limit, and the uniform-limit continuity theorem makes it continuous on the closed disk. Holomorphy in the interior follows from the locally uniform limit theorem [CA.35](background-complex-analysis.md#ca-35). $\square$

This supplies both limit passages in Example 5.1. A component of an open subset of $\mathbb C$ is open: small disks are connected and must lie in the component of their center. Distinct components therefore contain distinct rational-coordinate points, so there are at most countably many components. If $K$ is compact, its complement has exactly one unbounded component because all points outside a sufficiently large disk lie in one connected subset. Finally, the boundary of any complementary component lies in $K$: a boundary point outside $K$ has a small disk in the complement, forcing it into the same open component, a contradiction. These are the topology facts used in 5.3.
<!-- END BACKGROUND BG-VII.block5 -->

If $\partial\mathbb D=\{z\in\mathbb C:|z|=1\}$, let $\mathcal B=$ the uniform closure of the polynomials in $C(\partial\mathbb D)$. (Here “polynomial” means a polynomial in $z$.) If $\mathcal A=C(\partial\mathbb D)$, then the spectrum of $z$ as an element of $\mathcal A$ is $\partial\mathbb D$ (Example 3.2). That is,

$$
\sigma_{\mathcal A}(z)=\partial\mathbb D.
$$



<a id="pdf-page-221"></a>
Now $z\in\mathcal B$ and so it has a spectrum as an element of this algebra; denote this spectrum by $\sigma_{\mathcal B}(z)$. There is no reason to believe that $\sigma_{\mathcal B}(z)=\sigma_{\mathcal A}(z)$. In fact, they are not equal.

**5.1. Example.** If $\mathcal B=$ the closure in $C(\partial\mathbb D)$ of the polynomials in $z$, then $\sigma_{\mathcal B}(z)=\operatorname{cl}\mathbb D$.

To see this first note that $\|z\|=1$, so that $\sigma_{\mathcal B}(z)\subseteq\operatorname{cl}\mathbb D$ by Theorem 3.6. If $|\lambda|\leqslant1$ and $\lambda\notin\sigma_{\mathcal B}(z)$, there is an $f$ in $\mathcal B$ such that $(z-\lambda)f=1$. Note that this implies that $|\lambda|<1$. Because $f\in\mathcal B$, there is a sequence of polynomials $\{p_n\}$ such that $p_n\to f$ uniformly on $\partial\mathbb D$. Thus for every $\varepsilon>0$ there is an $N$ such that for $m,n\geqslant N$, $\varepsilon>\|p_n-p_m\|_{\partial\mathbb D}\equiv\sup\{|p_n(z)-p_n(z)|:z\in\partial\mathbb D\}$. By the Maximum Principle, $\varepsilon>\|p_n-p_m\|_{\operatorname{cl}\mathbb D}$ for $m,n\geqslant N$. Thus $g(z)=\lim p_n(z)$ is analytic on $\mathbb D$ and continuous on $\operatorname{cl}\mathbb D$; also, $g|_{\partial\mathbb D}=f$. By the same argument, since $p_n(z)(z-\lambda)\to1$ uniformly on $\partial\mathbb D$, $p_n(z)(z-\lambda)\to1$ uniformly on $\mathbb D$. Thus $g(z)(z-\lambda)=1$ on $\mathbb D$. But $1=g(\lambda)(\lambda-\lambda)=0$, a contradiction. Thus, $\operatorname{cl}\mathbb D\subseteq\sigma_{\mathcal B}(z)$.

Thus the spectrum not only depends on the element of the algebra, but also on the algebra. Precisely how this dependence occurs is given below, but it can be said that the example above is typical, both in its statement and its proof, of the general situation. To phrase these results it is necessary to introduce the polynomially convex hull of a compact subset of $\mathbb C$.

**5.2. Definition.** If $A$ is a set and $f:A\to\mathbb C$, define

$$
\|f\|_A\equiv\sup\{|f(z)|:z\in A\}.
$$

If $K$ is a compact subset of $\mathbb C$, define the *polynomially convex hull* of $K$ to be the set $K^\wedge$ given by

$$
K^\wedge\equiv\{z\in\mathbb C:|p(z)|\leqslant\|p\|_K\text{ for every polynomial }p\}.
$$

The set $K$ is *polynomially convex* if $K=K^\wedge$.

Note that the polynomially convex hull of $\partial\mathbb D$ is $\operatorname{cl}\mathbb D$. This is, again, quite typical. If $K$ is any compact set, then $\mathbb C\setminus K$ has a countable number of components, only one of which is unbounded. The bounded components are sometimes called the *holes* of $K$; a few pictures should convince the reader of the appropriateness of this terminology.

**5.3. Proposition.** *If $K$ is a compact subset of $\mathbb C$, then $\mathbb C\setminus K^\wedge$ is the unbounded component of $\mathbb C\setminus K$. Hence $K$ is polynomially convex if and only if $\mathbb C\setminus K$ is connected.*

**Proof.** Let $U_0,U_1,\ldots$ be the components of $\mathbb C\setminus K$, where $U_0$ is unbounded. Put $L=\mathbb C\setminus U_0$; hence $L=K\cup\bigcup_{n=1}^{\infty}U_n$. Clearly $K\subseteq K^\wedge$. If $n\geqslant1$, then $U_n$ is a bounded open set and a topological argument implies $\partial U_n\subset K$. By the Maximum Principle $U_n\subseteq K^\wedge$. Thus, $L\subseteq K^\wedge$.


<a id="pdf-page-222"></a>
If $\alpha\in U_0$, $(z-\alpha)^{-1}$ is analytic in a neighborhood of $L$. By (III.8.5), there is a sequence of polynomials $\{p_n\}$ such that $\|p_n-(z-\alpha)^{-1}\|_L\to0$. If $q_n=(z-\alpha)p_n$, then $\|q_n-1\|_L\to0$. Thus for large $n$, $\|q_n-1\|_L<1/2$. Since $K\subset L$ and $|q_n(\alpha)-1|=1$, this implies that $\alpha\notin K^{\wedge}$. Thus $K^{\wedge}\subseteq L$. ■

**5.4. Theorem.** *If $\mathcal A$ and $\mathcal B$ are Banach algebras with a common identity such that $\mathcal B\subseteq\mathcal A$ and $a\in\mathcal B$, then*

(a) $\sigma_{\mathcal A}(a)\subseteq\sigma_{\mathcal B}(a)$ and $\partial\sigma_{\mathcal B}(a)\subseteq\partial\sigma_{\mathcal A}(a)$.

(b) $\sigma_{\mathcal A}(a)^{\wedge}=\sigma_{\mathcal B}(a)^{\wedge}$.

(c) *If $G$ is a hole of $\sigma_{\mathcal A}(a)$, then either $G\subseteq\sigma_{\mathcal B}(a)$ or $G\cap\sigma_{\mathcal B}(a)=\varnothing$.*

(d) *If $\mathcal B$ is the closure in $\mathcal A$ of all polynomials in $a$, then $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)^{\wedge}$.*

**Proof.** (a) If $\alpha\notin\sigma_{\mathcal B}(a)$, then there is a $b$ in $\mathcal B$ such that $b(a-\alpha)=(a-\alpha)b=1$. Since $\mathcal B\subseteq\mathcal A$, $\alpha\notin\sigma_{\mathcal A}(a)$. Now assume that $\lambda\in\partial\sigma_{\mathcal B}(a)$. Since $\operatorname{int}\sigma_{\mathcal A}(a)\subseteq\operatorname{int}\sigma_{\mathcal B}(a)$, it suffices to show that $\lambda\in\sigma_{\mathcal A}(a)$. Suppose $\lambda\notin\sigma_{\mathcal A}(a)$; there is thus an $x$ in $\mathcal A$ such that $x(a-\lambda)=(a-\lambda)x=1$. Since $\lambda\in\partial\sigma_{\mathcal B}(a)$, there is a sequence $\{\lambda_n\}$ in $\mathbb C\setminus\sigma_{\mathcal B}(a)$ such that $\lambda_n\to\lambda$. Let $(a-\lambda_n)^{-1}$ be the inverse of $(a-\lambda_n)$ in $\mathcal B$, so $(a-\lambda_n)^{-1}\in\mathcal A$. Since $\lambda_n\to\lambda$, $(a-\lambda_n)\to(a-\lambda)$. By Theorem 2.2, $(a-\lambda_n)^{-1}\to x$. Thus $x\in\mathcal B$ since $\mathcal B$ is complete. This contradicts the fact that $\lambda\in\sigma_{\mathcal B}(a)$.

(b) This is a consequence of (a) and the Maximum Principle.

(c) Let $G$ be a hole of $\sigma_{\mathcal A}(a)$ and put $G_1=G\cap\sigma_{\mathcal B}(a)$ and $G_2=G\setminus\sigma_{\mathcal B}(a)$. So $G=G_1\cup G_2$ and $G_1\cap G_2=\varnothing$. Clearly $G_2$ is open. On the other hand, the fact that $\partial\sigma_{\mathcal B}(a)\subseteq\sigma_{\mathcal A}(a)$ and $G\cap\sigma_{\mathcal A}(a)=\varnothing$ implies that $G_1=G\cap\operatorname{int}\sigma_{\mathcal B}(a)$, so $G_1$ is open. Because $G$ is connected, either $G_1$ or $G_2$ is empty.

(d) Let $\mathcal B$ be as in (d). From (a) and (b) it is known that $\sigma_{\mathcal A}(a)\subseteq\sigma_{\mathcal B}(a)\subseteq\sigma_{\mathcal A}(a)^{\wedge}$. Fix $\lambda$ in $\sigma_{\mathcal A}(a)^{\wedge}$. If $\lambda\notin\sigma_{\mathcal B}(a)$, $(a-\lambda)^{-1}\in\mathcal B\subseteq\mathcal A$. Hence there is a sequence of polynomials $\{p_n\}$ such that $p_n(a)\to(a-\lambda)^{-1}$. Let $q_n(z)=(z-\lambda)p_n(z)$. Thus $\|q_n(a)-1\|\to0$. By the Spectral Mapping Theorem, $\sigma_{\mathcal A}(q_n(a))=q_n(\sigma_{\mathcal A}(a))$. Thus, because $\lambda\in\sigma_{\mathcal A}(a)^{\wedge}$,

$$
\begin{aligned}
\|q_n(a)-1\|&\geq r(q_n(a)-1)\\
&=\sup\{|z-1|:z\in\sigma_{\mathcal A}(q_n(a))\}\\
&=\sup\{|q_n(w)-1|:w\in\sigma_{\mathcal A}(a)\}\\
&\geq |q_n(\lambda)-1|\\
&=1.
\end{aligned}
$$

This is a contradiction. ■

**Exercises**

1. If $K$ is a compact subset of $\mathbb C$, let $P(K)$ be the closure of the polynomials in $C(K)$. Show that the identity map on polynomials extends to an isometric isomorphism of $P(K)$ onto $P(K^{\wedge})$.

2. If $K$ is a compact subset of $\mathbb C$, let $R(K)$ be the closure in $C(K)$ of all rational functions with poles off $K$. If $f\in R(K)$, show that $\sigma_{R(K)}(f)=f(K)$. If $f\in P(K)$, show that $\sigma_{P(K)}(f)=\hat f(K^{\wedge})$, where $\hat f$ is a natural extension of $f$ to $K^{\wedge}$.



   <a id="pdf-page-223"></a>
3. Let $\mathcal A,\mathcal B$ be as in Theorem 5.4. If $a\in\mathcal B$ and $\sigma_{\mathcal A}(a)\subseteq\mathbb R$, show that $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)$.

4. Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$. If $G_1,G_2,\ldots$ are the holes of $\sigma_{\mathcal A}(a)$ and $1\leq n_1\leq n_2,\ldots$, show that there is a subalgebra $\mathcal B$ of $\mathcal A$ such that $a\in\mathcal B$ and $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)\cup\bigcup_{k=1}^{\infty}G_{n_k}$.

5. If $\mathcal A,\mathcal B$, and $a$ are as in Theorem 5.4, $\mathcal A$ is not abelian, and $\mathcal B$ is a maximal abelian subalgebra of $\mathcal A$, show that $\sigma_{\mathcal A}(a)=\sigma_{\mathcal B}(a)$.

6. If $K$ is a nonempty compact subset of $\mathbb C$ that is polynomially convex, show that the components of $\operatorname{int}K$ are simply connected.

## §6. The Spectrum of a Linear Operator

<!-- BEGIN BACKGROUND BG-VII.block6 -->
<a id="bg-vii-12"></a>
### Lemma BG-VII.12 — Laurent expansions and spectral projections

For a Banach-valued holomorphic function $F$ on $0<|z-\lambda|<R$, there is a unique Laurent expansion
$$
F(z)=\sum_{n\in\mathbb Z}A_n(z-\lambda)^n,\qquad
A_n=\frac1{2\pi i}\int_{|\zeta-\lambda|=r}
\frac{F(\zeta)}{(\zeta-\lambda)^{n+1}}d\zeta,
$$
valid for any $0<r<R$, converging uniformly on compact subannuli. The coefficients do not depend on $r$.

**Proof.** The scalar annular Cauchy formula in [CA.40](background-complex-analysis.md#ca-40) transfers by BG-VII.4 and separation by $X^*$. On an outer boundary circle expand its kernel in nonnegative powers of $z-\lambda$; on an inner boundary circle expand in negative powers. Both geometric expansions converge uniformly on smaller compact subannuli and may be integrated termwise. Cauchy's theorem in the annulus makes the coefficient integrals independent of radius. Integrating any putative series termwise against powers of $z-\lambda$ extracts its coefficients, proving uniqueness. $\square$

For $F(z)=(z-A)^{-1}$, $A_{-1}$ is exactly the contour integral defining the Riesz idempotent at an isolated spectral point. A pole of order $m$ means $A_{-m}\ne0$ and $A_{-k}=0$ for $k>m$; an essential singularity means infinitely many negative coefficients are nonzero. A removable singularity means all negative coefficients vanish. The resolvent cannot have a removable singularity at a spectral point: a continuous extension $B$ there would satisfy $(\lambda-A)B=B(\lambda-A)=I$ by taking limits.
<!-- END BACKGROUND BG-VII.block6 -->

The proof of the first result is left as an exercise.

**6.1. Proposition.**

(a) *If $\mathcal X$ is a Banach space and $A\in\mathcal B(\mathcal X)$, $\sigma(A^*)=\sigma(A)$.*

(b) *If $\mathcal H$ is a Hilbert space and $A\in\mathcal B(\mathcal H)$, $\sigma(A^*)=\sigma(A)^*$, where for any subset $\Delta$ of $\mathbb C$, $\Delta^*\equiv\{\bar z:z\in\Delta\}$.*

In this section only results about operators on Banach spaces will be given. For the corresponding results about operators on a Hilbert space involving the adjoint, the reader is asked to supply the details. The preceding proposition should be kept in mind as a model of the probable differences.

In this section and the next $\mathcal X$ always denotes a Banach space over $\mathbb C$.

**6.2. Definition.** If $A\in\mathcal B(\mathcal X)$, the *point spectrum* of $A$, $\sigma_p(A)$, is defined by

$$
\sigma_p(A)\equiv\{\lambda\in\mathbb C:\ker(A-\lambda)\ne(0)\}.
$$

As in the case of operators on a Hilbert space, elements of $\sigma_p(A)$ are called *eigenvalues*. If $\lambda\in\sigma_p(A)$, non-zero vectors in $\ker(A-\lambda)$ are called *eigenvectors*; $\ker(A-\lambda)$ is called the *eigenspace* of $A$ at $\lambda$.

**6.3. Definition.** If $A\in\mathcal B(\mathcal X)$, the *approximate point spectrum* of $A$, $\sigma_{ap}(A)$, is defined by

$$
\begin{aligned}
\sigma_{ap}(A)\equiv\{\lambda\in\mathbb C:\;&\text{there is a sequence }\{x_n\}\text{ in }\mathcal X\\
&\text{such that }\|x_n\|=1\text{ for all }n\text{ and }\|(A-\lambda)x_n\|\to0\}.
\end{aligned}
$$

Note that $\sigma_p(A)\subseteq\sigma_{ap}(A)$.

**6.4. Proposition.** *If $A\in\mathcal B(\mathcal X)$ and $\lambda\in\mathbb C$, the following statements are equivalent.*

(a) $\lambda\notin\sigma_{ap}(A)$.

(b) $\ker(A-\lambda)=(0)$ *and* $\operatorname{ran}(A-\lambda)$ *is closed*.


<a id="pdf-page-224"></a>
(c) *There is a constant $c>0$ such that $\|(A-\lambda)x\|\geq c\|x\|$ for all $x$.*

**Proof.** Clearly it may be assumed that $\lambda=0$.

(a)$\Rightarrow$(c): Suppose (c) fails to hold; then for every $n$ there is a non-zero vector $x_n$ with $\|Ax_n\|\leq\|x_n\|/n$. If $y_n=x_n/\|x_n\|$, $\|y_n\|=1$ and $\|Ay_n\|\to0$. Hence $0\in\sigma_{ap}(A)$.

(c)$\Rightarrow$(b): Suppose $\|Ax\|\geq c\|x\|$. Clearly $\ker A=(0)$. If $Ax_n\to y$, $\|x_n-x_m\|\leq c^{-1}\|Ax_n-Ax_m\|$, so $\{x_n\}$ is a Cauchy sequence. Let $x=\lim x_n$; therefore $Ax=y$ and $\operatorname{ran}A$ is closed.

(b)$\Rightarrow$(a): Let $\mathcal Y=\operatorname{ran}A$; so $A:\mathcal X\to\mathcal Y$ is a continuous bijection. By the Inverse Mapping Theorem, there is a bounded operator $B:\mathcal Y\to\mathcal X$ such that $BAx=x$ for all $x$ in $\mathcal X$. Thus if $\|x\|=1$, $1=\|BAx\|\leq\|B\|\|Ax\|$. That is, $\|Ax\|\geq\|B\|^{-1}$ whenever $\|x\|=1$. Hence $0\notin\sigma_{ap}(A)$. ■

It may be that $\sigma_p(A)$ is empty, but it will be shown that $\sigma_{ap}(A)$ is never empty. The first statement follows from the next result (or from other examples that have been presented); the second statement will be proved later.

**6.5. Proposition.** *If $1\leq p\leq\infty$, define $S:l^p\to l^p$ by $S(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots)$. Then $\sigma(S)=\operatorname{cl}\mathbb D$, $\sigma_p(S)=\square$, and $\sigma_{ap}(S)=\partial\mathbb D$. Moreover, for $|\lambda|<1$, $\operatorname{ran}(S-\lambda)$ is closed and $\dim[l^p/\operatorname{ran}(S-\lambda)]=1$.*

**Proof.** Let $S_p$ be the shift on $l^p$. For $1\leq p\leq\infty$, define $T_p:l^p\to l^p$ by $T_p(x_1,x_2,\ldots)=(x_2,x_3,\ldots)$. It is easy to check that for $1\leq p<\infty$ and $1/p+1/q=1$, $S_p^*=T_q$. Since $\|S_p\|=1$, $\sigma(S_p)\subseteq\operatorname{cl}\mathbb D$.

Suppose $x=(x_1,x_2,\ldots)\in l^p$, $\lambda\neq0$. If $S_px=\lambda x$, $0=\lambda x_1$, $x_1=\lambda x_2,\ldots$. Hence $0=x_1=x_2=\cdots$. Since $S_p$ is an isometry, $\ker S_p=(0)$. Thus $\sigma_p(S_p)=\square$.

Let $1\leq p\leq\infty$ and $|\lambda|<1$. Put $x_\lambda=(1,\lambda,\lambda^2,\ldots)$. Then $\|x_\lambda\|_p^p=\sum_{n=0}^{\infty}|\lambda^p|^n<\infty$. Also, $T_px_\lambda=(\lambda,\lambda^2,\ldots)=\lambda x_\lambda$. Hence $\lambda\in\sigma_p(T_p)$ and $x_\lambda\in\ker(T_p-\lambda)$. If $1\leq p<\infty$ and $1/p+1/q=1$, $T_q=S_p^*$; so $\mathbb D\subseteq\sigma(T_q)=\sigma(S_p)$. Also, $S_\infty=T_1^*$, so $\mathbb D\subseteq\sigma(S_\infty)$. Thus for all $p$, $\mathbb D\subseteq\sigma(S_p)\subseteq\operatorname{cl}\mathbb D$. Since $\sigma(S_p)$ is necessarily closed, $\sigma(S_p)=\operatorname{cl}\mathbb D$.

If $|\lambda|\neq1$ and $x\in l^p$, $\|(S_p-\lambda)x\|_p=\|S_px-\lambda x\|_p\geq\bigl|\|S_px\|_p-|\lambda|\|x\|_p\bigr|=\bigl|\|x\|_p-|\lambda|\|x\|_p\bigr|=\bigl|1-|\lambda|\bigr|\|x\|_p$. By (6.4), $\lambda\notin\sigma_{ap}(S_p)$. Hence $\sigma_{ap}(S)\subseteq\partial\mathbb D$. The fact that $\sigma_{ap}(S_p)=\partial\mathbb D$ follows from the next proposition (6.7).

Fix $|\lambda|<1$; we will show that $\dim\ker(T_p-\lambda)=1$ for $1\leq p\leq\infty$. Indeed, if $x\in l^p$ and $T_px=\lambda x$, then $(x_2,x_3,\ldots)=(\lambda x_1,\lambda x_2,\ldots)$. So $x_{n+1}=\lambda x_n$ for all $n$. Thus $x_{n+1}=\lambda^n x_1$ for $n\geq1$. That is, if $x_\lambda=(1,\lambda,\lambda^2,\ldots)$, then $x=x_1x_\lambda$. Since it has already been shown that $x_\lambda\in\ker(T_p-\lambda)$, we have that the dimension of this kernel is 1. Therefore, if $1\leq p<\infty$, $1=\dim\ker(T_q-\lambda)=\dim\ker(S_p^*-\lambda)=\dim[\operatorname{ran}(S_p-\lambda)^\perp]$ (VI.1.8) $=\dim[l^p/\operatorname{ran}(S_p-\lambda)]^*$ (Why?). But this implies that $\dim[l^p/\operatorname{ran}(S_p-\lambda)]=1$, completing the proof for the case where $p$ is finite. The proof for $p=\infty$ is similar and is left to the reader. ■

**6.6. Corollary.** *If $1\leq p\leq\infty$ and $T:l^p\to l^p$ is defined by $T(x_1,x_2,\ldots)=(x_2,x_3,\ldots)$,*


<a id="pdf-page-225"></a>
*then $\sigma(T)=\operatorname{cl}\mathbb D$ and for $|\lambda|<1$, $\ker(T-\lambda)$ is the one-dimensional space spanned by the vector $(1,\lambda,\lambda^2,\ldots)$.*

The next result shows that if $S$ is as in (6.5), then $\partial\mathbb D\subseteq\sigma_{ap}(S)$.

**6.7. Proposition.** *If $A\in\mathcal B(\mathcal X)$, then $\partial\sigma(A)\subseteq\sigma_{ap}(A)$.*

**PROOF.** Let $\lambda\in\partial\sigma(A)$ and let $\{\lambda_n\}\subseteq\mathbb C\setminus\sigma(A)$ such that $\lambda_n\to\lambda$.

**6.8. Claim.** $\|(A-\lambda_n)^{-1}\|\to\infty$ as $n\to\infty$.

In fact, if the claim were false, then by passing to a subsequence if necessary, it follows that there is a constant $M$ such that $\|(A-\lambda_n)^{-1}\|\leq M$ for all $n$. Choose $n$ sufficiently large that $|\lambda_n-\lambda|<M^{-1}$. Then $\|(A-\lambda)-(A-\lambda_n)\|<\|(A-\lambda_n)^{-1}\|^{-1}$. By (2.3b), this implies that $(A-\lambda)$ is invertible, a contradiction. This establishes (6.8).

Let $\|x_n\|=1$ such that $\alpha_n\equiv\|(A-\lambda_n)^{-1}x_n\|>\|(A-\lambda_n)^{-1}\|-n^{-1}$, so $\alpha_n\to\infty$. Put $y_n=\alpha_n^{-1}(A-\lambda_n)^{-1}x_n$; hence $\|y_n\|=1$. Now

$$
\begin{aligned}
(A-\lambda)y_n&=(A-\lambda_n)y_n+(\lambda-\lambda_n)y_n\\
&=\alpha_n^{-1}x_n+(\lambda-\lambda_n)y_n.
\end{aligned}
$$

Thus $\|(A-\lambda)y_n\|\leq\alpha_n^{-1}+|\lambda-\lambda_n|$, so that $\|(A-\lambda)y_n\|\to0$ as $n\to\infty$. That is, $\lambda\in\sigma_{ap}(A)$. $\blacksquare$

Let $A\in\mathcal B(\mathcal X)$ and suppose $\Delta$ is a *clopen* subset of $\sigma(A)$; that is, $\Delta$ is a subset of $\sigma(A)$ that is both closed and relatively open. So $\sigma(A)=\Delta\cup(\sigma(A)\setminus\Delta)$. As in Proposition 4.11 (and Exercise 4.9),

$$
E(\Delta)=E(\Delta;A)=\frac{1}{2\pi i}\int_\Gamma(z-A)^{-1}\,dz, \tag{6.9}
$$

where $\Gamma$ is a positively oriented Jordan system such that $\Delta\subseteq\operatorname{ins}\Gamma$ and $\sigma(A)\setminus\Delta\subseteq\operatorname{out}\Gamma$, is an idempotent. Moreover, $E(\Delta)B=BE(\Delta)$ whenever $AB=BA$ and if $\mathcal X_\Delta=E(\Delta)\mathcal X$, $\sigma(A|_{\mathcal X_\Delta})=\Delta$. Call $E(\Delta)$ the *Riesz idempotent* corresponding to $\Delta$. If $\Delta=$ a singleton set $\{\lambda\}$, let $E(\lambda)=E(\{\lambda\})$ and $\mathcal X_\lambda=\mathcal X_{\{\lambda\}}$. Note that if $\lambda$ is an isolated point of $\sigma(A)$, then $\{\lambda\}$ is a clopen subset of $\sigma(A)$.

**6.10. Example.** Let $\{\alpha_n\}\in l^\infty$, $1\leq p\leq\infty$, and define $A:l^p\to l^p$ by $(Ax)(n)=\alpha_nx(n)$. Then $\sigma(A)=\operatorname{cl}\{\alpha_n\}$ and $\sigma_p(A)=\{\alpha_n\}$. For each $k$, define $N_k=\{n\in\mathbb N;\ \alpha_n=\alpha_k\}$ and define $P_k:l^p\to l^p$ by $P_kx=\chi_{N_k}x$. If $\alpha_k$ is an isolated point of $\sigma(A)$, then $\{\alpha_k\}$ is a clopen subset of $\sigma(A)$ and $E(\{\alpha_k\};A)=P_k$.

Suppose $A\in\mathcal B(\mathcal X)$ and $\lambda_0$ is an isolated point in $\sigma(A)$. Hence $E(\lambda_0)=E(\lambda_0;A)$ is a well-defined idempotent. Also, $\lambda_0$ is an isolated singularity of the analytic function $z\mapsto(z-A)^{-1}$ on $\mathbb C\setminus\sigma(A)$. Perhaps the nature of this singularity (pole


<a id="pdf-page-226"></a>
or essential singularity) will reveal something of the nature of $\lambda_0$ as an element of $\sigma(A)$. First it is helpful to get the precise form of the Laurent expansion of $(z-A)^{-1}$ about $\lambda_0$.

**6.11. Lemma.** If $\lambda_0$ is an isolated point of $\sigma(A)$, then

$$
(z-A)^{-1}=\sum_{n=-\infty}^{\infty}(z-\lambda_0)^n A_n
$$

for $0<|z-\lambda_0|<r_0=\operatorname{dist}(\lambda_0,\sigma(A)\setminus\{\lambda\})$, where

$$
A_n=\frac{1}{2\pi i}\int_\gamma (z-\lambda_0)^{-n-1}(z-A)^{-1}\,dz
$$

for $\gamma=$ any circle centered at $\lambda_0$ with radius $<r_0$.

The proof follows the lines of the usual Laurent series development (Conway [1978]).

**6.12. Proposition.** If $\lambda_0$ is an isolated point of $\sigma(A)$, then $\lambda_0$ is a pole of $(z-A)^{-1}$ of order $n$ if and only if $(\lambda_0-A)^nE(\lambda_0)=0$ and $(\lambda_0-A)^{n-1}E(\lambda_0)\ne0$.

**Proof.** Let $(z-A)^{-1}=\sum_{n=-\infty}^{\infty}(z-\lambda_0)^nA_n$ as is (6.11). Now $\lambda_0$ is a pole of order $n$ if and only if $A_{-n}\ne0$ and $A_{-k}=0$ for $k>n$. Let $\Gamma$ be a positively oriented system of curves such that $\sigma(A)\setminus\{\lambda_0\}\subseteq\operatorname{ins}\Gamma$ and $\lambda_0\in\operatorname{out}\Gamma$. Let $\gamma$ be a circle centered at $\lambda_0$ and contained in $\operatorname{out}\Gamma$. Let $e(z)\equiv1$ in a neighborhood of $\gamma\cup\operatorname{ins}\gamma$ and $e(z)\equiv0$ in a neighborhood of $\Gamma\cup\operatorname{ins}\Gamma$. So $e\in\operatorname{Hol}(A)$ and $e(A)=E(\lambda_0)$. If $k\geq1$,

$$
\begin{aligned}
A_{-k}
&=\frac{1}{2\pi i}\int_\gamma (z-\lambda_0)^{k-1}(z-A)^{-1}\,dz\\
&=\frac{1}{2\pi i}\int_{\gamma+\Gamma}e(z)(z-\lambda_0)^{k-1}(z-A)^{-1}\,dz\\
&=E(\lambda_0)(A-\lambda_0)^{k-1}
\end{aligned}
$$

since $\sigma(A)\subseteq\operatorname{ins}(\gamma+\Gamma)=\operatorname{ins}\gamma\cup\operatorname{ins}\Gamma$. The proposition now follows. $\blacksquare$

**6.13. Corollary.** If $\lambda_0$ is an isolated point of $\sigma(A)$ and is a pole of $(z-A)^{-1}$, then $\lambda_0\in\sigma_p(A)$.

In fact, the preceding result implies that if $n$ is the order of the pole, then $(0)\ne(\lambda_0-A)^{n-1}E(\lambda_0)\mathcal{X}\subseteq\ker(A-\lambda_0)$.

**6.14. Example.** A measurable function $k:[0,1]\times[0,1]\to\mathbb{C}$ is called a *Volterra kernel* if $k$ is bounded and $k(x,y)=0$ when $x<y$. If $1\leq p\leq\infty$ and



<a id="pdf-page-227"></a>
$k$ is a Volterra kernel, define $V_k:L^p(0,1)\to L^p(0,1)$ by

$$
V_kf(x)=\int_0^1 k(x,y)f(y)\,dy=\int_0^x k(x,y)f(y)\,dy.
$$

Then $V_k\in\mathcal{B}(L^p)$ and $\|V_k\|\leq\|k\|_\infty$ (III.2.3).

If $k$, $h$ are Volterra kernels and

$$
(hk)(x,y)=\int_0^1 h(x,t)k(t,y)\,dt,
$$

then $hk$ is a Volterra kernel, $\|hk\|_\infty\leq\|h\|_\infty\|k\|_\infty$, and $V_{hk}=V_hV_k$. Note that if $k(x,y)$ is the characteristic function of $\{(x,y)\in[0,1]\times[0,1]:y<x\}$, then $V_k$ is the Volterra operator (II.1.7).

If $k$ is a Volterra kernel, then

$$
\sigma(V_k)=\{0\}.
$$

Indeed, from the preceding paragraph it is known that $V_k^n=V_{k^n}$. This will be used to show that the spectral radius of $V_k$ is 0.

**6.15. Claim.** $|k^n(x,y)|\leq(\|k\|_\infty^n/(n-1)!)(x-y)^{n-1}$ for $y<x$.

This is proved by induction. Clearly it holds for $n=1$. Suppose (6.15) is true for some $n\geq1$. Then

$$
\begin{aligned}
|k^{n+1}(x,y)|
&=\left|\int_y^x k(x,t)k^n(t,y)\,dt\right|\\
&\leq\int_y^x |k(x,t)|\,|k^n(t,y)|\,dt\\
&\leq\|k\|_\infty\frac{\|k\|_\infty^n}{(n-1)!}
\int_y^x(t-y)^{n-1}\,dt\\
&\leq\frac{\|k\|_\infty^{n+1}}{n!}(x-y)^n.
\end{aligned}
$$

This establishes the claim.

From (6.15) it follows that

$$
\|V_k^n\|\leq\|k^n\|_\infty\leq\frac{\|k\|_\infty^n}{(n-1)!}.
$$

Therefore

$$
\|V_k^n\|^{1/n}\leq\|k\|_\infty[(n-1)!]^{-1/n}.
$$

Since $[(n-1)!]^{-1/n}\to0$ as $n\to\infty$, $r(V_k)=0$. Thus $\square\ne\sigma(V_k)\subseteq\{\lambda\in\mathbb{C}:|\lambda|\leq0\}$; that is, $\sigma(V_k)=\{0\}$.

It is possible for $\ker V_k$ to be nontrivial. For example, if $k(x,y)=\chi_{(0,1/2)}(y)$



<a id="pdf-page-228"></a>
when $y<x$ and $0$ otherwise, then

$$
V_kf(x)=
\begin{cases}
\displaystyle\int_0^x f(y)\,dy & \text{if }x\leq\frac12,\\[6pt]
\displaystyle\int_0^{1/2} f(y)\,dy & \text{if }x\geq\frac12.
\end{cases}
$$

So if $f(y)=0$ for $0\leq y\leq\frac12$, $V_kf=0$.

On the other hand, the Volterra operator $V$ [$=V_k$ for $k(x,y)=$ the characteristic function of $\{(x,y):y<x\}$] has $\ker V=(0)$. In fact, if $0=Vf$, then for all $x$, $0=\int_0^x f(y)\,dy$. Differentiating gives that $f=0$.

Is there an analogy between $V_k$ for a Volterra kernel $k$ and a lower triangular matrix?

## Exercises

1. Prove Proposition 6.1.

2. Show that for $\mathcal{X}$ a Banach space and $A$ in $\mathcal{B}(\mathcal{X})$, $\sigma_l(A)=\sigma_r(A^*)$. What happens in a Hilbert space?

3. If $\mathcal{H}$ is an infinite dimension Hilbert space and $K$ is a non-empty compact subset of $\mathbb{C}$, show that there is an $A$ in $\mathcal{B}(\mathcal{H})$ such that $\sigma(A)=K$. Can $A$ be found such that $\sigma(A)=\sigma_{ap}(A)=K$?

4. Let $K$ be a compact subset of $\mathbb{C}$. Does there exist an operator $A$ in $\mathcal{B}(C[0,1])$ such that $\sigma(A)=K$?

5. If $\mathcal{X}$ is a Banach space and $A\in\mathcal{B}(\mathcal{X})$, show that $A$ is left invertible if and only if $\ker A=(0)$ and $\operatorname{ran}A$ is a closed complemented subspace of $\mathcal{X}$.

6. If $\mathcal{X}$ is a Banach space and $A\in\mathcal{B}(\mathcal{X})$, show that $A$ is right invertible if and only if $\operatorname{ran}A=\mathcal{X}$ and $\ker A$ is a complemented subspace of $\mathcal{X}$.

7. If $\mathcal{X}$ is a Banach space and $T:\mathcal{X}\to\mathcal{X}$ is an isometry, then either $\sigma(T)\subseteq\partial\mathbb{D}$ or $\sigma(T)=\operatorname{cl}\mathbb{D}$.

8. Verify the statements made in Example 6.10.

9. Let $1\leq p\leq\infty$ and suppose $0<\alpha_1\leq\alpha_2\cdots$ such that $r=\lim\alpha_n<\infty$. Define $A:\ell^p\to\ell^p$ by $A(x_1,x_2,\ldots)=(0,\alpha_1x_1,\alpha_2x_2,\ldots)$. Show that $\sigma(A)=\{z\in\mathbb{C}:|z|\leq r\}$ and $\sigma_{ap}(A)=\partial\sigma(A)$. If $|\lambda|<r$, then $\operatorname{ran}(A-\lambda)$ is closed and has codimension 1. Also, $\sigma_p(A)=\square$.

10. Verify the statements made in Example 6.14.

11. Let $1\leq p\leq\infty$ and let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space. For $\phi$ in $L^\infty(\mu)$, define $M_\phi$ on $L^p(\mu)$ as in Example III.2.2. Find $\sigma(M_\phi)$, $\sigma_{ap}(M_\phi)$, and $\sigma_p(M_\phi)$.

12. If $A\in\mathcal{B}(\mathcal{X})$, $f\in\operatorname{Hol}(A)$, and $\lambda\in\sigma_p(A)$, is $f(\lambda)\in\sigma_p(f(A))$? If $\lambda\in\sigma_{ap}(A)$, is $f(\lambda)\in\sigma_{ap}(f(A))$? Is there a relation between $f(\sigma_{ap}(A))$ and $\sigma_{ap}(f(A))$?

13. If $A\in\mathcal{B}(\mathcal{X})$, say that a complex number $\lambda$ has *finite index* if there is a positive integer $k$ such that $\ker(A-\lambda)^k=\ker(A-\lambda)^{k+1}$; the *index* of $\lambda$, denoted by $\nu(\lambda)$



    <a id="pdf-page-229"></a>
    or $\nu_A(\lambda)$, is the smallest such integer $k$. (a) Show that if $\lambda$ is an isolated point of $\sigma(A)$ and a pole of order $n$ of $(z-A)^{-1}$, then $\nu(\lambda)=n$. (b) If $\nu(\lambda)<\infty$, show that

    $$
    \ker(A-\lambda)^{\nu(\lambda)}
    =\ker(A-\lambda)^{\nu(\lambda)+k}
    \quad\text{for all }k\geq 0.
    $$

    (c) If $\mathcal X=\mathbb C^n$ and

    $$
    A=\begin{bmatrix}
    0 & & & & \\
    1 & 0 & & & \\
    & 1 & \ddots & & \\
    & & \ddots & \ddots & \\
    & & & 1 & 0
    \end{bmatrix},
    $$

    then $\sigma(A)=\{0\}$ and $\nu(0)=n$.

14. If $V$ is the Volterra operator, show that $0$ is an essential singularity of $(z-V)^{-1}$.

15. Let $\mathcal A$ be a Banach algebra with identity. If $a\in\mathcal A$, define $L_a,R_a\in\mathcal B(\mathcal A)$ by $L_a(x)=ax$ and $R_a(x)=xa$. Show that $\sigma(L_a)=\sigma(R_a)=\sigma(a)$.

16. If $E$ is a projection on a Hilbert space and $E$ is neither $0$ nor $1$, then $\sigma(E)=\{0,1\}$.

17. (McCabe [1984]) If $\mathcal X$ is a complex Banach space and $T\in\mathcal B(\mathcal X)$, show that the following statements are equivalent. (a) $r(T)<1$. (b) $\|T^m\|<1$ for some positive integer $m$. (c) $\sum_n\|T^n(x)\|<\infty$ for every $x$ in $\mathcal X$.

## §7. The Spectral Theory of a Compact Operator

<!-- BEGIN BACKGROUND BG-VII.block7 -->
<a id="bg-vii-13"></a>
### Lemma BG-VII.13 — The compactness contradiction in the closed-range lemma

If $K:X\to X$ is compact, $\lambda\ne0$, and $K-\lambda I$ is injective, then it is bounded below and has closed range.

**Proof.** If it were not bounded below, choose $\|x_n\|=1$ with $(K-\lambda I)x_n\to0$. Compactness gives a subsequence for which $Kx_n\to y$. Then $x_n=\lambda^{-1}(Kx_n-(K-\lambda I)x_n)\to\lambda^{-1}y=x$. Its limit has norm $1$ and satisfies $(K-\lambda I)x=0$, contradicting injectivity. Apply BG-VI.1 for the range assertion. $\square$

<a id="bg-vii-14"></a>
### Corollary BG-VII.14 — The solvability meaning of the Fredholm alternative

Once the range of $K-\lambda I$ is known to be closed, the equation $(K-\lambda I)x=y$ has a solution exactly when
$$
g(y)=0\quad\text{for every }g\in\ker(K^*-\lambda I).
$$

**Proof.** By BG-VI.2, the preannihilator of this adjoint kernel is $\overline{\operatorname{ran}(K-\lambda I)}$. Closedness removes the closure. $\square$

For Banach adjoints the scalar is $\lambda$, not $\overline\lambda$; for Hilbert adjoints the latter appears. Also, a compact identity operator can occur only in finite dimension: Riesz's lemma constructs, in an infinite-dimensional space, unit vectors separated by a fixed positive distance, contradicting compactness of the unit ball. This explains the finite-dimensional spectral subspace step in 7.7.
<!-- END BACKGROUND BG-VII.block7 -->

Recall that for a Banach space $\mathcal X$, $\mathcal B_0(\mathcal X)$ is the algebra of all compact operators. This Banach algebra has no identity, so if $A\in\mathcal B_0(\mathcal X)$, then $\sigma(A)$ refers to the spectrum of $A$ as an element of $\mathcal B(\mathcal X)$. Of course, if $\mathcal A=\mathcal B_0(\mathcal X)+\mathbb C$, then $\mathcal A$ is a Banach algebra with identity (Why?) and we could consider $\sigma_{\mathcal A}(A)$ for $A$ in $\mathcal B_0(\mathcal X)$. By Theorem 5.4, $\sigma(A)\subseteq\sigma_{\mathcal A}(A)$, $\partial\sigma_{\mathcal A}(A)\subseteq\sigma(A)$, and $\sigma(A)^{\wedge}=\sigma_{\mathcal A}(A)^{\wedge}$. Below, in Theorem 7.1, it will be shown that $\sigma(A)$ is a countable set and hence $\sigma(A)=\partial\sigma(A)=\sigma(A)^{\wedge}$. Thus $\sigma(A)=\sigma_{\mathcal A}(A)$.

**7.1. Theorem.** (F. Riesz) *If $\dim\mathcal X=\infty$ and $A\in\mathcal B_0(\mathcal X)$, then one and only one of the following possibilities occurs.*

(a) $\sigma(A)=\{0\}$.

(b) $\sigma(A)=\{0,\lambda_1,\ldots,\lambda_n\}$, where for $1\leq k\leq n$, $\lambda_k\neq 0$, each $\lambda_k$ is an eigenvalue of $A$, and $\dim\ker(A-\lambda_k)<\infty$.

(c) $\sigma(A)=\{0,\lambda_1,\lambda_2,\ldots\}$, where for each $k\geq 1$, $\lambda_k$ is an eigenvalue of $A$, $\dim\ker(A-\lambda_k)<\infty$, and, moreover, $\lim\lambda_k=0$.

The proof will use several lemmas. The first lemma was given in the case that $\mathcal X$ is a Hilbert space in Proposition II.4.14. The proof is identical and will not be repeated here.

**7.2. Lemma.** *If $A\in\mathcal B_0(\mathcal X)$, $\lambda\neq 0$, and $\ker(A-\lambda)=(0)$, then $\operatorname{ran}(A-\lambda)$ is closed.*



<a id="pdf-page-230"></a>
The proof of the next lemma is like that of Corollary II.4.15.

**7.3. Lemma.** *If $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\ne0$, and $\lambda\in\sigma(A)$, then either $\lambda\in\sigma_p(A)$ or $\lambda\in\sigma_p(A^*)$.*

**7.4. Lemma.** *If $\mathcal{M}\leqslant\mathcal{N}$, $\mathcal{M}\ne\mathcal{N}$, and $\varepsilon>0$, then there is a $y$ in $\mathcal{N}$ such that $\|y\|=1$ and $\operatorname{dist}(y,\mathcal{M})\geqslant1-\varepsilon$.*

**Proof.** Let $\delta(y)=\operatorname{dist}(y,\mathcal{M})$ for every $y$ in $\mathcal{N}$. Now if $y_1\in\mathcal{N}\setminus\mathcal{M}$, there is an $x_0$ in $\mathcal{M}$ such that $\delta(y_1)\leqslant\|x_0-y_1\|\leqslant(1+\varepsilon)\delta(y_1)$. Let $y_2=y_1-x_0$. Then $(1+\varepsilon)\delta(y_2)=(1+\varepsilon)\inf\{\|y_2-x\|:x\in\mathcal{M}\}=(1+\varepsilon)\inf\{\|y_1-x_0-x\|:x\in\mathcal{M}\}=(1+\varepsilon)\delta(y_1)$ since $x_0\in\mathcal{M}$. Thus $(1+\varepsilon)\delta(y_2)>\|x_0-y_1\|=\|y_2\|$. Let $y=\|y_2\|^{-1}y_2$. So $\|y\|=1$, $y\in\mathcal{N}$, and if $x\in\mathcal{M}$, then
$$
\begin{aligned}
\|y-x\|&=\bigl\|\|y_2\|^{-1}y_2-x\bigr\|\\
&=\|y_2\|^{-1}\bigl\|y_2-\|y_2\|x\bigr\|>[(1+\varepsilon)\delta(y_2)]^{-1}\bigl\|y_2-\|y_2\|x\bigr\|\\
&\geqslant(1+\varepsilon)^{-1}>1-\varepsilon.
\end{aligned}
$$
$\blacksquare$

If $\mathcal{M}$ and $\mathcal{N}$ are finite dimensional in the preceding lemma, then $y$ can be chosen in $\mathcal{N}$ such that $\|y\|=1$ and $\operatorname{dist}(y,\mathcal{M})=1$ (see Exercise 1).

**7.5. Lemma.** *If $A\in\mathcal{B}_0(\mathcal{X})$ and $\{\lambda_n\}$ is a sequence of distinct elements in $\sigma_p(A)$, then $\lim\lambda_n=0$.*

**Proof.** For each $n$ let $x_n\in\ker(A-\lambda_n)$ such that $x_n\ne0$. It follows that if $\mathcal{M}_n=\bigvee\{x_1,\ldots,x_n\}$, then $\dim\mathcal{M}_n=n$ (Exercise). Hence $\mathcal{M}_n\leqslant\mathcal{M}_{n+1}$ and $\mathcal{M}_n\ne\mathcal{M}_{n+1}$. By the preceding lemma there is a vector $y_n$ in $\mathcal{M}_n$ such that $\|y_n\|=1$ and $\operatorname{dist}(y_n,\mathcal{M}_{n-1})>\frac12$. Let $y_n=\alpha_1x_1+\cdots+\alpha_nx_n$. Hence
$$
(A-\lambda_n)y_n=\alpha_1(\lambda_1-\lambda_n)x_1+\cdots+\alpha_{n-1}(\lambda_{n-1}-\lambda_n)x_{n-1}\in\mathcal{M}_{n-1}.
$$
So if $n>m$,
$$
\begin{aligned}
A(\lambda_n^{-1}y_n)-A(\lambda_m^{-1}y_m)
&=\lambda_n^{-1}(A-\lambda_n)y_n-\lambda_m^{-1}(A-\lambda_m)y_m+y_n-y_m\\
&=y_n-[y_m+\lambda_m^{-1}(A-\lambda_m)y_m-\lambda_n^{-1}(A-\lambda_n)y_n].
\end{aligned}
$$
But the bracketed expression belongs to $\mathcal{M}_{n-1}$. Hence $\|A(\lambda_n^{-1}y_n)-A(\lambda_m^{-1}y_m)\|\geqslant\operatorname{dist}(y_n,\mathcal{M}_{n-1})>\frac12$. Therefore $A(\lambda_n^{-1}y_n)$ can have no convergent subsequence. But $A$ is a compact operator so that if $S$ is any bounded subset of $\mathcal{X}$, $\operatorname{cl}A(S)$ is compact. Thus it must be that $\{\lambda_n^{-1}y_n\}$ has no bounded subsequence. Since $\|y_n\|=1$ for all $n$, it must be that $\|\lambda_n^{-1}y_n\|=|\lambda_n|^{-1}\to\infty$. That is, $0=\lim\lambda_n$. $\blacksquare$

**Proof of Theorem 7.1.** The first step is to establish the following.

**7.6. Claim.** If $\lambda\in\sigma(A)$ and $\lambda\ne0$, then $\lambda$ is an isolated point of $\sigma(A)$.

In fact, if $\{\lambda_n\}\subseteq\sigma(A)$ and $\lambda_n\to\lambda$, then each $\lambda_n$ belongs to either $\sigma_p(A)$ or $\sigma_p(A^*)$ (7.3). So either there is a subsequence $\{\lambda_{n_k}\}$ that is contained in $\sigma_p(A)$


<a id="pdf-page-231"></a>
or there is a subsequence contained in $\sigma_p(A^*)$. If $\{\lambda_{n_k}\}\subseteq\sigma_p(A)$, then Lemma 7.5 implies $\lambda_{n_k}\to 0$, a contradiction. If $\{\lambda_{n_k}\}\subseteq\sigma_p(A^*)$, then the fact that $A^*$ is compact gives the same contradiction. Thus $\lambda$ must be isolated if $\lambda\ne 0$.

**7.7. Claim.** If $\lambda\in\sigma(A)$ and $\lambda\ne 0$, then $\lambda\in\sigma_p(A)$ and $\dim\ker(A-\lambda)<\infty$.

By (7.6), $\lambda$ is an isolated point of $\sigma(A)$ so that $E(\lambda)$ can be defined as in (6.9). Let $\mathcal X_\lambda=E(\lambda)\mathcal X$ and $A_\lambda=A|_{\mathcal X_\lambda}$. By Exercise 4.9 [also see (4.11)], $\sigma(A_\lambda)=\{\lambda\}$. Thus $A_\lambda$ is an invertible compact operator. By Exercise VI.3.5, $\dim\mathcal X_\lambda<\infty$. If $n=\dim\mathcal X_\lambda$, then $A_\lambda-\lambda$ is a nilpotent operator on an $n$-dimensional space. Thus $(A_\lambda-\lambda)^n=0$. Let $\nu=$ the positive integer such that $(A_\lambda-\lambda)^\nu=0$ but $(A_\lambda-\lambda)^{\nu-1}\ne 0$. Let $x\in\mathcal X_\lambda$ such that $0\ne(A_\lambda-\lambda)^{\nu-1}x=y$; then $(A-\lambda)y=0$. Thus $\lambda\in\sigma_p(A)$.

Also, $\ker(A-\lambda)\in\operatorname{Lat}A$ and $A|_{\ker(A-\lambda)}$ is compact. But $Ax=\lambda x$ for all $x$ in $\ker(A-\lambda)$, so $\dim\ker(A-\lambda)<\infty$.

Now for the *dénouement*. If $\dim\mathcal X=\infty$ and $A\in\mathcal B_0(\mathcal X)$, then $A$ cannot be invertible (Exercise VI.3.5). Thus $0\in\sigma(A)$. If $\lambda\in\sigma(A)$ and $\lambda\ne 0$, then Claim 7.7 says that $\lambda\in\sigma_p(A)$ and $\dim\ker(A-\lambda)<\infty$. So if $\sigma(A)$ is finite, either (a) or (b) of (7.1) hold. If $\sigma(A)$ is infinite, then Claim 7.6 implies that $\sigma(A)$ is countable. So let $\sigma(A)=\{0,\lambda_1,\lambda_2,\ldots\}$. By Lemma 7.5 and Claim 7.7, (c) holds. ■

Part of the following surfaced in the proof of the theorem.

**7.8. Corollary.** *If $A\in\mathcal B_0(\mathcal X)$ and $\lambda\in\sigma(A)$ with $\lambda\ne 0$, then $\lambda$ is a pole of $(z-A)^{-1}$, $\ker(A-\lambda)\subseteq E(\lambda)\mathcal X$, and $\dim E(\lambda)\mathcal X<\infty$.*

**Proof.** The only part of this corollary that did not appear in the preceding proof is the fact that $\ker(A-\lambda)\subseteq E(\lambda)\mathcal X$.

Let $\Delta=\sigma(A)\setminus\{\lambda\}$, $\mathcal X_\Delta=E(\Delta)\mathcal X$, $A_\Delta=A|_{\mathcal X_\Delta}$. By Exercise 4.9, $\sigma(A_\Delta)=\Delta$; so $A_\Delta-\lambda$ is invertible on $\mathcal X_\Delta$. If $x\in\ker(A-\lambda)$, then $x=E(\lambda)x+E(\Delta)x$. Hence $0=(A-\lambda)x=(A-\lambda)E(\lambda)x+(A-\lambda)E(\Delta)x=(A_\lambda-\lambda)E(\lambda)x+(A_\Delta-\lambda)E(\Delta)x$. But $\mathcal X_\lambda$ and $\mathcal X_\Delta\in\operatorname{Lat}A$, so $(A_\lambda-\lambda)E(\lambda)x\in\mathcal X_\lambda$ and $(A_\Delta-\lambda)E(\Delta)x\in\mathcal X_\Delta$; since $\mathcal X_\lambda\cap\mathcal X_\Delta=(0)$, $0=(A_\lambda-\lambda)E(\lambda)x=(A_\Delta-\lambda)E(\Delta)x$. But $A_\Delta-\lambda$ is invertible so $E(\Delta)x=0$; that is, $x=E(\lambda)x\in\mathcal X_\lambda$. Hence $\ker(A-\lambda)\subseteq\mathcal X_\lambda$. ■

If $k$ is a Volterra kernel (6.14), then $V_k$ is a compact operator (Exercise VI.3.6) and $\sigma(V_k)=\{0\}$. So the first possibility of Theorem 7.1 can occur. If $V$ is the Volterra operator, then $\sigma_p(V)=\square$.

Let $V$ be the Volterra operator on $L^p(0,1)$, $1<p<\infty$. If $\lambda_1,\ldots,\lambda_n\in\mathbb C$, let $D:\mathbb C^n\to\mathbb C^n$ be defined by $D(z_1,\ldots,z_n)=(\lambda_1z_1,\ldots,\lambda_nz_n)$. Then $A=V\oplus D$ on $L^p(0,1)\oplus\mathbb C^n$ is compact and $\sigma(A)=\{0,\lambda_1,\ldots,\lambda_n\}$. So the second possibility of (7.1) occurs. If $\{\lambda_n\}\subseteq\mathbb C$ and $\lim\lambda_n=0$, then define $D:\ell^p\to\ell^p$ $(1\le p\le\infty)$ by $(Dx)(n)=\lambda_nx(n)$. If $A=V\oplus D$ on $L^p(0,1)\oplus\ell^p$, $A$ is compact and $\sigma(A)=\{0,\lambda_1,\lambda_2,\ldots\}$ (see Exercise 3).


<a id="pdf-page-232"></a>
§7. The Spectral Theory of a Compact Operator  217

The next result has a number of applications in the theory of integral equations.

**7.9. The Fredholm Alternative.** *If $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\in\mathbb{C}$, and $\lambda\neq 0$, then $\operatorname{ran}(A-\lambda)$ is closed and $\dim\ker(A-\lambda)=\dim\ker(A-\lambda)^*<\infty$.*

**Proof.** It suffices to assume that $\lambda\in\sigma(A)$. Put $\Delta=\sigma(A)\setminus\{\lambda\}$, $\mathcal{X}_\lambda=E(\lambda)\mathcal{X}$, $\mathcal{X}_\Delta=E(\Delta)\mathcal{X}$, $A_\lambda=A|_{\mathcal{X}_\lambda}$, and $A_\Delta=A|_{\mathcal{X}_\Delta}$. Now $\lambda\notin\Delta=\sigma(A_\Delta)$, so $A_\Delta-\lambda$ is invertible. Thus $\operatorname{ran}(A_\Delta-\lambda)=\mathcal{X}_\Delta$. Hence $\operatorname{ran}(A-\lambda)=(A-\lambda)\mathcal{X}_\lambda+(A-\lambda)\mathcal{X}_\Delta=\operatorname{ran}(A_\lambda-\lambda)+\mathcal{X}_\Delta$. Since $\dim\mathcal{X}_\lambda<\infty$, $\operatorname{ran}(A-\lambda)$ is closed (III.4.3).

Also note that

$$
\begin{aligned}
\mathcal{X}/\operatorname{ran}(A-\lambda)
&=(\mathcal{X}_\Delta+\mathcal{X}_\lambda)/[\operatorname{ran}(A_\lambda-\lambda)+\mathcal{X}_\Delta]\\
&\approx\mathcal{X}_\lambda/\operatorname{ran}(A_\lambda-\lambda).
\end{aligned}
$$

Since $\dim\mathcal{X}_\lambda<\infty$, $\dim[\mathcal{X}/\operatorname{ran}(A-\lambda)]=\dim\mathcal{X}_\lambda-\dim\operatorname{ran}(A_\lambda-\lambda)=\dim\ker(A_\lambda-\lambda)=\dim\ker(A-\lambda)<\infty$ since $\ker(A-\lambda)\subseteq\mathcal{X}_\lambda$ (7.8). But $[\mathcal{X}/\operatorname{ran}(A-\lambda)]^*=[\operatorname{ran}(A-\lambda)]^\perp$ (III.10.2) $=\ker(A-\lambda)^*$. Hence $\dim\ker(A-\lambda)=\dim\ker(A-\lambda)^*$. $\blacksquare$

**7.10. Corollary.** *If $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\in\mathbb{C}$, and $\lambda\neq 0$, then for every $y$ in $\mathcal{X}$ there is an $x$ in $\mathcal{X}$ such that*

$$
(A-\lambda)x=y \tag*{7.11}
$$

*if and only if the only vector $x$ such that $(A-\lambda)x=0$ is $x=0$. If this condition is satisfied, then the solution to (7.11) is unique.*

This corollary is a rephrasing of part of the Fredholm Alternative together with the fact that an operator has dense range if and only if its adjoint has a trivial kernel.

The applications of the Fredholm Alternative occur by taking the compact operator to be an integral operator.

## Exercises

1. If $\mathcal{M},\mathcal{N}$ are finite dimensional spaces and $\mathcal{M}\leq\mathcal{N}$, $\mathcal{M}\neq\mathcal{N}$, then there is a $y$ in $\mathcal{N}$ such that $\|y\|=1$ and $\operatorname{dist}(y,\mathcal{M})=1$.

2. Let $A\in\mathcal{B}(\mathcal{X})$ and let $\lambda_1,\ldots,\lambda_n$ be distinct points in $\sigma_p(A)$. If $x_k\in\ker(A-\lambda_k)$, $1\leq k\leq n$, and $x_k\neq 0$, show that $\{x_1,\ldots,x_n\}$ is a linearly independent set.

3. Let $\mathcal{X}_1,\mathcal{X}_2\ldots$ be Banach spaces and put $\mathcal{X}=\bigoplus_p\mathcal{X}_n$. Let $A_n\in\mathcal{B}(\mathcal{X}_n)$ such that $\sup_n\|A_n\|<\infty$ and define $A:\mathcal{X}\to\mathcal{X}$ by $A\{x_n\}=\{A_nx_n\}$. Show that $A\in\mathcal{B}(\mathcal{X})$ and $\|A\|=\sup_n\|A_n\|$. Show that $A\in\mathcal{B}_0(\mathcal{X})$ if and only if each $A_n\in\mathcal{B}_0(\mathcal{X})$ and $\lim\|A_n\|=0$.

4. Suppose $A\in\mathcal{B}(\mathcal{X})$ and there is a polynomial $p$ such that $p(A)\in\mathcal{B}_0(\mathcal{X})$. What can be said about $\sigma(A)$?



   <a id="pdf-page-233"></a>
5. Suppose $A\in\mathcal{B}(\mathcal{X})$ and there is an entire function $f$ such that $f(A)\in\mathcal{B}_0(\mathcal{X})$. What can be said about $\sigma(A)$?

6. With the terminology of Exercise 6.13, if $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\in\sigma(A)$, and $\lambda\ne0$, what can be said about the index of $\lambda$?

## §8. Abelian Banach Algebras

<!-- BEGIN BACKGROUND BG-VII.block8 -->
<a id="bg-vii-15"></a>
### Lemma BG-VII.15 — Characters are automatically bounded

If $h$ is a nonzero complex-linear multiplicative map from a unital complex Banach algebra to $\mathbb C$, then $h(1)=1$, $h(a)\in\sigma(a)$, and $\|h\|=1$.

**Proof.** Choose $b$ with $h(b)\ne0$. The identity $h(b)=h(1)h(b)$ gives $h(1)=1$. If $a-h(a)1$ were invertible, applying $h$ to its product with its inverse would give $1=0$. Thus $h(a)\in\sigma(a)$, so $|h(a)|\leq r(a)\leq\|a\|$. This proves boundedness without assuming it, and evaluation at $1$ gives norm $1$. $\square$

This applies even without commutativity, though existence and classification of characters require further hypotheses. In the maximal ideal space, weak-star convergence is precisely pointwise convergence on algebra elements. Consequently multiplicativity survives limits; the identity condition $h(1)=1$ prevents the limiting character from becoming zero.
<!-- END BACKGROUND BG-VII.block8 -->

Recall that it is assumed that every Banach algebra is over $\mathbb{C}$. Also assume that all Banach algebras contain an identity.

A *division algebra* is an algebra such that every nonzero element has a multiplicative inverse. It may seem incongruous that the first theorem in this section allows the algebra to be nonabelian. However, the conclusion is that the algebra is abelian—and much more.

**8.1. The Gelfand–Mazur Theorem.** *If $\mathcal{A}$ is a Banach algebra that is also a division ring, then $\mathcal{A}=\mathbb{C}\;(=\{\lambda1:\lambda\in\mathbb{C}\})$.*

**Proof.** If $a\in\mathcal{A}$, then $\sigma(a)\ne\square$. If $\lambda\in\sigma(a)$, then $a-\lambda$ has no inverse. But $\mathcal{A}$ is a division ring, so $a-\lambda=0$. That is, $a=\lambda$. ■

As a corollary of the preceding theorem, the algebra of quaternions, $\mathbb{H}$, is not a Banach algebra. That is, it is impossible to put a norm on $\mathbb{H}$ that makes it into a Banach algebra over $\mathbb{C}$. Can you show this directly?

**8.2. Proposition.** *If $\mathcal{A}$ is an abelian Banach algebra and $\mathcal{M}$ is a maximal ideal, then there is a homomorphism $h:\mathcal{A}\to\mathbb{C}$ such that $\mathcal{M}=\ker h$. Conversely, if $h:\mathcal{A}\to\mathbb{C}$ is a nonzero homomorphism, then $\ker h$ is a maximal ideal. Moreover, this correspondence $h\mapsto\ker h$ between homomorphisms and maximal ideals is bijective.*

**Proof.** If $\mathcal{M}$ is a maximal ideal, then $\mathcal{M}$ is closed (2.4b). Hence $\mathcal{A}/\mathcal{M}$ is a Banach algebra with identity. Let $\pi:\mathcal{A}\to\mathcal{A}/\mathcal{M}$ be the natural map. If $a\in\mathcal{A}$ and $\pi(a)$ is not invertible in $\mathcal{A}/\mathcal{M}$, then $\pi(\mathcal{A}a)=\pi(a)[\mathcal{A}/\mathcal{M}]$ is an ideal in $\mathcal{A}/\mathcal{M}$ that is proper. Let $I=\{b\in\mathcal{A}:\pi(b)\in\pi(\mathcal{A}a)\}=\pi^{-1}(\pi(\mathcal{A}a))$. Then $I$ is a proper ideal of $\mathcal{A}$ and $\mathcal{M}\subseteq I$. Since $\mathcal{M}$ is maximal, $\mathcal{M}=I$. Thus $\pi(a\mathcal{A})\subseteq\pi(I)=\pi(\mathcal{M})=(0)$. That is, $\pi(a)=0$. This says that $\mathcal{A}/\mathcal{M}$ is a field. By the Gelfand–Mazur Theorem $\mathcal{A}/\mathcal{M}=\mathbb{C}=\{\lambda+\mathcal{M}:\lambda\in\mathbb{C}\}$. Define $\tilde h:\mathcal{A}/\mathcal{M}\to\mathbb{C}$ by $\tilde h(\lambda+\mathcal{M})=\lambda$ and define $h:\mathcal{A}\to\mathbb{C}$ by $h=\tilde h\circ\pi$. Then $h$ is a homomorphism and $\ker h=\mathcal{M}$.

Conversely, suppose $h:\mathcal{A}\to\mathbb{C}$ is a nonzero homomorphism. Then $\ker h=\mathcal{M}$ is a nontrivial ideal and $\mathcal{A}/\mathcal{M}\approx\mathbb{C}$. (Why?) So $\mathcal{M}$ is maximal.

If $h,h'$ are two nonzero homomorphisms and $\ker h=\ker h'$, then there is an $\alpha$ in $\mathbb{C}$ such that $h=\alpha h'$ (A.1.4). But $1=h(1)=\alpha h'(1)=\alpha$, so $h=h'$. ■


<a id="pdf-page-234"></a>
**8.3. Corollary.** If $\mathcal A$ is an abelian Banach algebra and $h:\mathcal A\to\mathbb C$ is a homomorphism, then $h$ is continuous.

**Proof.** Maximal ideals are closed (2.4b). ■

The next result improves the preceding corollary a little. Remember that by (8.3) if $h:\mathcal A\to\mathbb C$ is a homomorphism, then $h\in\mathcal A^*$ (the Banach space dual of $\mathcal A$).

**8.4. Proposition.** If $\mathcal A$ is abelian and $h:\mathcal A\to\mathbb C$ is a non-zero homomorphism, then $\|h\|=1$.

**Proof.** Let $a\in\mathcal A$ and put $\lambda=h(a)$. If $|\lambda|>\|a\|$, then $\|a/\lambda\|<1$. Hence $1-a/\lambda$ is invertible. Let $b=(1-a/\lambda)^{-1}$, so $1=b(1-a/\lambda)=b-ba/\lambda$. Since $h(1)=1$, $1=h(b-ba/\lambda)=h(b)-h(b)h(a)/\lambda=h(b)-h(b)=0$, a contradiction. Hence $\|a\|\geq|\lambda|=|h(a)|$; so $\|h\|\leq1$. Since $h(1)=1$, $\|h\|=1$. ■

**8.5. Definition.** If $\mathcal A$ is an abelian Banach algebra, let $\Sigma=$ the collection of all nonzero homomorphisms of $\mathcal A\to\mathbb C$. Give $\Sigma$ the relative weak* topology that it has as a subset of $\mathcal A^*$. $\Sigma$ with this topology is called the *maximal ideal space* of $\mathcal A$.

**8.6. Theorem.** If $\mathcal A$ is an abelian Banach algebra, then its maximal ideal space $\Sigma$ is a compact Hausdorff space. Moreover, if $a\in\mathcal A$, then $\sigma(a)=\Sigma(a)\equiv\{h(a):h\in\Sigma\}$.

**Proof.** Since $\Sigma\subseteq\operatorname{ball}\mathcal A^*$, it suffices for the proof of the first part of the theorem to show that $\Sigma$ is weak* closed. Let $\{h_i\}$ be a net in $\Sigma$ and suppose $h\in\operatorname{ball}\mathcal A^*$ such that $h_i\to h$ weak*. If $a,b\in\mathcal A$, then $h(ab)=\lim_i h_i(ab)=\lim_i h_i(a)h_i(b)=h(a)h(b)$. So $h$ is a homomorphism. Since $h(1)=\lim_i h_i(1)=1$, $h\in\Sigma$. Thus $\Sigma$ is compact.

If $h\in\Sigma$ and $\lambda=h(a)$, then $a-\lambda\in\ker h$. So $a-\lambda$ is not invertible and $\lambda\in\sigma(a)$; that is, $\Sigma(a)\subseteq\sigma(a)$. Now assume that $\lambda\in\sigma(a)$; so $a-\lambda$ is not invertible and, hence, $(a-\lambda)\mathcal A$ is a proper ideal. Let $\mathcal M$ be a maximal ideal in $\mathcal A$ such that $(a-\lambda)\mathcal A\subseteq\mathcal M$. If $h\in\Sigma$ such that $\mathcal M=\ker h$, then $0=h(a-\lambda)=h(a)-\lambda$; hence $\sigma(a)\subseteq\Sigma(a)$. ■

Now it is time for an example. Here is one that is a little more than an example. If $X$ is compact and $x\in X$, let $\delta_x:C(X)\to\mathbb C$ be defined by $\delta_x(f)=f(x)$. It is easy to see that $\delta_x$ is a homomorphism on the algebra $C(X)$.

**8.7. Theorem.** If $X$ is compact and $\Sigma$ is the maximal ideal space of $C(X)$, then the map $x\mapsto\delta_x$ is a homeomorphism of $X$ onto $\Sigma$.

**Proof.** Let $\Delta:X\to\Sigma$ be defined by $\Delta(x)=\delta_x$. As was pointed out before, $\Delta(X)\subseteq\Sigma$. It was shown in Proposition V.6.1 that $\Delta:X\to(\Delta(X),\text{ weak}^*)$ is a homeomorphism. Thus it only remains to show that $\Delta(X)=\Sigma$. If $h\in\Sigma$, then



<a id="pdf-page-235"></a>
there is a measure $\mu$ in $M(X)$ such that $h(f)=\int f\,d\mu$ for all $f$ in $C(X)$. Also, $\|\mu\|=\|h\|=1$ and $\mu(X)=\int 1\,d\mu=h(1)=1$. Hence $\mu\geq 0$ (Exercises III.7.2). Let $x\in\operatorname{support}(\mu)$. It will be shown that $h=\delta_x$.

Let $\mathcal M=\{f\in C(X):f(x)=0\}$. So $\mathcal M$ is a maximal ideal of $C(X)$. Note that if it can be shown that $\ker h\subseteq\mathcal M$, then it must be that $\ker h=\mathcal M$ and so $h=\delta_x$. So let $f\in\ker h$. Because $\ker h$ is an ideal, $|f|^2=f\overline f\in\ker h$. Hence $0=h(|f|^2)=\int|f|^2\,d\mu$. Since $\mu\geq 0$ and $|f|^2\geq 0$, it must be that $f=0$ a.e. $[\mu]$. Since $f$ is continuous, $f\equiv 0$ on $\operatorname{support}(\mu)$. In particular, $f(x)=0$ and so $f\in\mathcal M$. ■

It follows from the preceding theorem that the maximal ideals of $C(X)$ are all of the form $\{f\in C(X):f(x)=0\}$ for some $x$ in $X$.

**8.8. Definition.** Let $\mathcal A$ be an abelian Banach algebra with maximal ideal space $\Sigma$. If $a\in\mathcal A$, then the *Gelfand transform* of $a$ is the function $\hat a:\Sigma\to\mathbb C$ defined by $\hat a(h)=h(a)$.

**8.9. Theorem.** *If $\mathcal A$ is an abelian Banach algebra with maximal ideal space $\Sigma$ and $a\in\mathcal A$, then the Gelfand transform of $a$, $\hat a$, belongs to $C(\Sigma)$. The map $a\mapsto\hat a$ of $\mathcal A$ into $C(\Sigma)$ is a continuous homomorphism of $\mathcal A$ into $C(\Sigma)$ of norm 1 and its kernel is*

$$
\bigcap\{\mathcal M:\mathcal M\text{ is a maximal ideal of }\mathcal A\}.
$$

*Moreover, for each $a$ in $\mathcal A$,*

$$
\|\hat a\|_\infty=\lim_{n\to\infty}\|a^n\|^{1/n}.
$$

**Proof.** If $h_i\to h$ in $\Sigma$, then $h_i\to h$ weak* in $\mathcal A^*$. So if $a\in\mathcal A$, $\hat a(h_i)=h_i(a)\to h(a)=\hat a(h)$. Thus $\hat a\in C(\Sigma)$.

Define $\gamma:\mathcal A\to C(\Sigma)$ by $\gamma(a)=\hat a$. If $a,b\in\mathcal A$, then $\gamma(ab)(h)=\widehat{ab}(h)=h(ab)=h(a)h(b)=\hat a(h)\hat b(h)$. Therefore $\gamma(ab)=\gamma(a)\gamma(b)$. It is easy to see that $\gamma$ is linear, so $\gamma$ is a homomorphism. Also, by (8.4), if $a\in\mathcal A$, $|\hat a(h)|=|h(a)|\leq\|a\|$; thus $\|\gamma(a)\|_\infty=\|\hat a\|_\infty\leq\|a\|$. So $\gamma$ is continuous and $\|\gamma\|\leq 1$. Since $\gamma(1)=1$, $\|\gamma\|=1$.

Note that $a\in\ker\gamma$ if and only if $\hat a\equiv 0$; that is, $a\in\ker\gamma$ if and only if $h(a)=0$ for each $h$ in $\Sigma$. Thus $a\in\ker\gamma$ if and only if $a$ belongs to every maximal ideal of $\mathcal A$.

Finally, by Theorem 8.6, if $a\in\mathcal A$, then $\|\hat a\|_\infty=\sup\{|\lambda|:\lambda\in\sigma(a)\}$. The last part of this theorem is thus a consequence of this observation and Proposition 3.8. ■

The homomorphism $a\mapsto\hat a$ of $\mathcal A$ into $C(\Sigma)$ is called the *Gelfand transform* of $\mathcal A$. The kernel of the Gelfand transform is called the *radical* of $\mathcal A$, $\operatorname{rad}\mathcal A$. So

$$
\operatorname{rad}\mathcal A=\bigcap\{\mathcal M:\mathcal M\text{ is a maximal ideal of }\mathcal A\}.
$$



<a id="pdf-page-236"></a>
If $X$ is compact and $\Sigma$, the maximal ideal space of $C(X)$, is identified with $X$ as in Theorem 8.7, then the Gelfand transform $C(X)\to C(\Sigma)$ becomes the identity map.

If $\mathcal A$ is an abelian algebra, say that $a$ in $\mathcal A$ is a *generator* of $\mathcal A$ if $\{p(a):p\text{ is a polynomial}\}$ is dense in $\mathcal A$.

Recall that if $\tau:X\to Y$ is a homeomorphism, then $A:C(Y)\to C(X)$ defined by $Af=f\circ\tau$ is an isometric isomorphism (VI.2.1). Denote the relationship between $A$ and $\tau$ by $A=\tau^\#$.

**8.10. Proposition.** *If $\mathcal A$ is an abelian Banach algebra with identity and $a$ is a generator of $\mathcal A$, then there is a homeomorphism $\tau:\Sigma\to\sigma(a)$ such that if $\gamma:\mathcal A\to C(\Sigma)$ is the Gelfand transform and $p$ is a polynomial, then $\gamma(p(a))=\tau^\#(p)$.*

**Proof.** Define $\tau:\Sigma\to\sigma(a)$ by $\tau(h)=h(a)$. By Theorem 8.6 $\tau$ is surjective. It is easy to see that $\tau$ is continuous. To see that $\tau$ is injective, suppose $\tau(h_1)=\tau(h_2)$, so $h_1(a)=h_2(a)$. Hence $h_1(a^n)=h_2(a^n)$ for all $n\geq 0$. By linearity, $h_1(p(a))=h_2(p(a))$ for every polynomial $p$. Since $a$ is a generator for $\mathcal A$ and $h_1$ and $h_2$ are continuous on $\mathcal A$, $h_1=h_2$, and $\tau$ is injective. Since $\Sigma$ is compact, $\tau$ is a homeomorphism.

The remainder of the proposition follows from the fact that $\gamma$ and $\tau^\#$ are homomorphisms. Hence $\gamma(p(a))(h)=p(\gamma(a))(h)=p(\hat a)(h)=p(\hat a(h))=p(\tau(h))=\tau^\#(p)(h)$. $\blacksquare$

**8.11. Corollary.** *If $\mathcal A$ has two elements $a_1$ and $a_2$ each of which is a generator, then $\sigma(a_1)$ and $\sigma(a_2)$ are homeomorphic.*

The converse to (8.11) is not true. If $\mathcal A=C[-1,1]$, then $f(x)=x$ defines a generator $f$ for $\mathcal A$. If $g(x)=x^2$, then $\sigma(g)=g([-1,1])=[0,1]$. So $\sigma(f)$ and $\sigma(g)$ are homeomorphic. However, $g$ is not a generator for $\mathcal A$. In fact, the Banach algebra generated by $g$ consists of the even functions in $C[-1,1]$.

**8.12. Example.** If $V:L^2(0,1)\to L^2(0,1)$ is the Volterra operator and $\mathcal A$ is the closure in $\mathcal B(L^2(0,1))$ of $\{p(V):p\text{ is a polynomial in }z\}$, then $\mathcal A$ is an abelian Banach algebra and $\operatorname{rad}\mathcal A=\operatorname{cl}\{p(V):p\text{ is a polynomial in }z\text{ and }p(0)=0\}$. In other words, $\mathcal A$ has a unique maximal ideal, $\operatorname{rad}\mathcal A$. In fact, if $\mathcal B=\mathcal B(L^2(0,1))$, Theorem 5.4 implies that $\partial\sigma_{\mathcal A}(V)\subseteq\sigma_{\mathcal B}(V)\subseteq\sigma_{\mathcal A}(V)$. Since $\sigma_{\mathcal B}(V)=\{0\}$ (6.14), $\sigma_{\mathcal A}(V)=\{0\}$. The statement above now follows by Proposition 8.10.

**8.13. Example.** Let $\mathcal A$ be the closure in $C(\partial\mathbb D)$ of the polynomials in $z$. If $\Sigma$ is the maximal ideal space of $\mathcal A$, then $\Sigma$ is homeomorphic to $\sigma_{\mathcal A}(z)$. (Here $z$ is the function whose value at $\lambda$ in $\partial\mathbb D$ is $\lambda$.) Now $\sigma_{\mathcal A}(z)=\operatorname{cl}\mathbb D$ as was shown in Example 5.1. If $f\in\mathcal A$, then the Maximum Modulus Theorem shows that $f$ has a continuous extension to $\operatorname{cl}\mathbb D$ that is analytic in $\mathbb D$ [see (5.1)]. Also denote this extension by $f$. The proof of (8.10) shows that the continuous homomorphisms on $\mathcal A$ are of the form $f\mapsto f(\lambda)$ for some $\lambda$ in $\operatorname{cl}\mathbb D$.



<a id="pdf-page-237"></a>
In the next section the Banach algebra $L^1(G)$ is examined for a locally compact abelian group and its maximal ideals are characterized.

## Exercises

1. Let $\mathcal A$ be a Banach algebra with identity and let $J$ be the smallest closed two-sided ideal of $\mathcal A$ containing $\{xy-yx:x,y\in\mathcal A\}$. $J$ is called the *commutator ideal* of $\mathcal A$. (a) Show that $\mathcal A/J$ is an abelian Banach algebra. (b) If $I$ is a closed ideal of $\mathcal A$ such that $\mathcal A/I$ is abelian, then $I\supseteq J$. (c) If $h:\mathcal A\to\mathbb C$ is a homomorphism, then $J\subseteq\ker h$ and $h$ induces a homomorphism $\tilde h:\mathcal A/J\to\mathbb C$ such that $\tilde h\circ\pi=h$, where $\pi:\mathcal A\to\mathcal A/J$ is the natural map. Hence $\|\tilde h\|=1$. (d) Let $\Sigma$ be the set of homomorphisms of $\mathcal A\to\mathbb C$ and let $\tilde\Sigma$ be the set of homomorphisms of $\mathcal A/J$. Show that the map $h\mapsto\tilde h$ defined in (c) is a homeomorphism of $\Sigma$ onto $\tilde\Sigma$.

2. Using the terminology of Exercises 2.6 and 2.7, let $\mathcal A$ be an abelian Banach algebra without identity and show that if $\mathcal M$ is a maximal modular ideal, then there is a homomorphism $h:\mathcal A\to\mathbb C$ such that $\mathcal M=\ker h$. Conversely, if $h:\mathcal A\to\mathbb C$ is a nonzero homomorphism, then $\ker h$ is a maximal modular ideal. Moreover, the correspondence $h\mapsto\ker h$ is a bijection between homomorphisms and maximal modular ideals.

3. If $\mathcal A$ is an abelian Banach algebra and $h:\mathcal A\to\mathbb C$ is a homomorphism, then $h$ is continuous and $\|h\|\leq 1$. If $\mathcal A$ has an approximate identity $\{e_i\}$ such that $\|e_i\|\leq 1$ for all $i$, then $\|h\|=1$ (see Exercise 2.8).

4. Let $\mathcal A$ be an abelian Banach algebra and let $\Sigma$ be the set of nonzero homomorphisms of $\mathcal A\to\mathbb C$. Show that $\Sigma$ is locally compact if it has the relative weak* topology from $\mathcal A^*$ (Exercise 3).

5. With the notation of Exercise 4, assume that $\mathcal A$ has no identity and let $\mathcal A_1$ be the algebra obtained by adjoining an identity. For $a$ in $\mathcal A$, let $\sigma(a)$ be the spectrum of $a$ as an element of $\mathcal A_1$ and show that $\sigma(a)=\{h(a):h\in\Sigma\}\cup\{0\}$. Also, show that the maximal ideal space of $\mathcal A_1$, $\Sigma_1$, is the one-point compactification of $\Sigma$.

6. With the notation of Exercise 4, for each $a$ in $\mathcal A$ define $\hat a:\Sigma\to\mathbb C$ by $\hat a(h)=h(a)$. Show that $\hat a\in C_0(\Sigma)$ and the map $a\mapsto\hat a$ of $\mathcal A$ into $C_0(\Sigma)$ is a contractive homomorphism with kernel $=\bigcap\{\mathcal M:\mathcal M\text{ is a maximal modular ideal of }\mathcal A\}$.

7. If $X$ is locally compact, show that $x\mapsto\delta_x$ is a homeomorphism of $X$ onto the maximal ideal space of $C_0(X)$.

8. Let $X$ be locally compact and for each open subset $U$ of $X$ let $C_0(U)=\{f\in C_0(X):f(x)=0\text{ for }x\text{ in }X\setminus U\}$. Show that $C_0(U)$ is a closed ideal of $C_0(X)$ and that every closed ideal of $C_0(X)$ has this form. Moreover, the map $U\mapsto C_0(U)$ is a lattice isomorphism from the lattice of open subsets of $X$ onto the lattice of ideals of $C_0(X)$.

9. With the notation of the preceding exercise, show that $C_0(U)$ is a modular ideal if and only if $X\setminus U$ is compact.

10. If $\mathcal A$ is an abelian Banach algebra and $a\in\mathcal A$, say that $a$ is a *rational generator* of $\mathcal A$ if $\{f(a):f\text{ is a rational function with poles off }\sigma(a)\}$ is dense in $\mathcal A$. Show that if $a$ is a rational generator of $\mathcal A$, then $\Sigma$ is homeomorphic to $\sigma(a)$.



    <a id="pdf-page-238"></a>
11. Verify the statements made in Example 8.12.

12. Say that $a_1,\ldots,a_n$ are generators of $\mathcal A$ if $\mathcal A$ is the smallest Banach algebra with identity that contains $\{a_1,\ldots,a_n\}$. Show that $a_1,\ldots,a_n$ are generators of $\mathcal A$ if and only if $\mathcal A=\operatorname{cl}\{p(a_1,\ldots,a_n):p\text{ is a polynomial in }n\text{ complex variables }z_1,\ldots,z_n\}$, and if $\Sigma$ is the maximal ideal space, then there is a homeomorphism $\tau$ of $\Sigma$ onto a compact subset $K$ of $\mathbb C^n$ such that if $p$ is a polynomial in $n$ variables, then $\gamma(p(a_1,\ldots,a_n))=\tau^\#(p)$.

13. Verify the statements made in Example 8.13.

14. (Zelazko [1968].) Let $\mathcal A$ be an algebra and suppose $\phi:\mathcal A\to\mathbb C$ is a linear functional such that $\phi(a^2)=\phi(a)^2$ for all $a$ in $\mathcal A$. Show that $\phi$ is a homomorphism.

15. Let $\mathcal A$ be an abelian Banach algebra with identity that is semisimple [that is, $\operatorname{rad}\mathcal A=(0)$]. If $\|\cdot\|$ is the norm on $\mathcal A$ and $\|\cdot\|_1$ is another norm on $\mathcal A$ that also makes $\mathcal A$ into a Banach algebra, then these two norms are equivalent. (Hint: use the Closed Graph Theorem to show that the identity map $i:(\mathcal A,\|\cdot\|)\to(\mathcal A,\|\cdot\|_1)$ is continuous.)

16. Let $\mathcal A$ be as in Example 8.13 and let $K=\{\phi\in\mathcal A^*:\phi(1)=\|\phi\|=1\}$. Show that $\operatorname{ext}K=\{\delta_z:|z|=1\}$. (See (V.7).)

17. Show that $f(x)=\exp(\pi ix)$ is a generator of $C([0,1])$ but $g(x)=\exp(2\pi ix)$ is not.

18. Show that $C(\partial\mathbb D)$ does not have a single generator though it does have a single rational generator (that is, an element $a$ such that $\{r(a):r\text{ is a rational function with poles off }\sigma(a)\}$ is dense.)

## §9*. The Group Algebra of a Locally Compact Abelian Group

<!-- BEGIN BACKGROUND BG-VII.block9 -->
<a id="bg-vii-16"></a>
### Lemma BG-VII.16 — Convolution estimates and approximate identities

For $f,g\in L^1(G)$ on a locally compact abelian group with Haar measure,
$$
\|f*g\|_1\leq\|f\|_1\|g\|_1.
$$
If $g\geq0$, $\int g=1$, and $g$ vanishes outside a neighborhood $U$ of the identity, then
$$
\|f*g-f\|_1\leq\sup_{y\in U}\|f_y-f\|_1,
\qquad f_y(x)=f(xy^{-1}).
$$

**Proof.** First suppose $G$ is $\sigma$-compact, so Haar measure is $\sigma$-finite. The triangle inequality, Tonelli's theorem for the nonnegative absolute-value integrand, and translation invariance give
$$
\int\!\int|f(xy^{-1})g(y)|\,dy\,dx
=\int|g(y)|\,\|f\|_1dy.
$$
This also justifies Fubini for the original integrand. For the second bound write $f*g-f=\int(f_y-f)g(y)dy$, apply the same norm estimate, and use the support and normalization of $g$.

For a general locally compact abelian group, regularity on finite-measure sets allows each $L^1$ function to be represented by one supported on a countable union of compact sets: apply inner approximation to the finite-measure level sets $\{|f|\geq1/n\}$, with approximation errors tending to zero. Choose all these compact sets for $f$ and $g$, together with one compact identity neighborhood. The subgroup $H$ they generate is open and $\sigma$-compact: it is a countable union of compact finite products and their inverses, and it contains an open identity neighborhood. Both functions vanish off $H$, and their convolution vanishes off $H$ too. Restrict the calculation to $H\times H$, where the measure is $\sigma$-finite. This proves the displayed estimates without assuming an unjustified global $\sigma$-finiteness hypothesis. $\square$

When choosing $g_U=m(U)^{-1}\chi_U$, use **relatively compact open** identity neighborhoods: then $0<m(U)<\infty$. Arbitrary neighborhoods need not have finite measure. Such neighborhoods form a base, so this restriction does not change the limiting argument in 9.4. On $\mathbb R$, the character calculation also has an elementary final step: from $\gamma'=c\gamma$ and $\gamma(0)=1$, differentiation gives $(e^{-cx}\gamma(x))'=0$, hence $\gamma(x)=e^{cx}$; $|\gamma(x)|=1$ forces $\operatorname{Re}c=0$.
<!-- END BACKGROUND BG-VII.block9 -->

If $G$ is a locally compact abelian group and $m$ is Haar measure on $G$, then $L^1(G)\equiv L^1(m)$ is a Banach algebra (Example 1.11), where for $f,g$ in $L^1(G)$ the product $f*g$ is the convolution of $f$ and $g$:

$$
f*g(x)=\int_G f(xy^{-1})g(y)\,dy.
$$

Note that $dy$ is used to designate integration with respect to $m$ rather than $dm(y)$. Because $G$ is abelian, $L^1(G)$ is abelian. In fact, $g*f(x)=\int g(xy^{-1})f(y)\,dy$. If $y^{-1}x$ is substituted for $y$ in this integral, the value of the integral does not change because Haar measure is translation invariant. Hence $g*f(x)=\int g(y)f(y^{-1}x)\,dy=\int g(y)f(xy^{-1})\,dy=f*g(x)$.

Let $e$ denote the identity of $G$. If $G$ is discrete, then $\delta_e\in L^1(G)$ and $\delta_e$ is an identity for $L^1(G)$. If $G$ is not discrete, then $L^1(G)$ does not have an identity (Exercise 1).

Some examples of nondiscrete locally compact abelian groups are $\mathbb R^n$ and $\mathbb T^n$, where $\mathbb T=$ the unit circle $\partial\mathbb D$ in $\mathbb C$ with the usual multiplication. Note



<a id="pdf-page-239"></a>
that $\mathbb{T}^{\infty}$ is also a compact abelian group while $\mathbb{R}^{\infty}$ fails to be locally compact. The Cantor set can be identified with the product of a countable number of copies of $\mathbb{Z}_2$ and is thus a compact abelian group. Indeed, the product of a countable number of finite sets (with the discrete topology) is homeomorphic to the Cantor set, so that the Cantor set has infinitely many nonisomorphic group structures.

For a topological group $G$, $L^1(G)$ is called the *group algebra* for $G$. If $G$ is discrete, the algebraists talk of the *group algebra* over a field $K$ as the set of all $f=\sum_{g\in G}a_g g$, where $a_g\in K$ and $a_g\ne 0$ for at most a finite number of $g$ in $G$. If $K=\mathbb{C}$, this is the set of functions $f:G\to\mathbb{C}$ with finite support. Thus in the discrete case the group algebra of the algebraists can be identified with a dense manifold in $L^1(G)=l^1(G)$.

Unlike §V.11, if $f:G\to\mathbb{C}$ and $x\in G$, define $f_x:G\to\mathbb{C}$ by $f_x(y)=f(yx^{-1})$; so $f_x(y)=f(x^{-1}y)$ for $G$ abelian. We want to examine the function $x\mapsto f_x$ of $G\to L^p(G)$, $1\leq p<\infty$. To do this we first prove the following (see Exercise V.11.10).

**9.1. Proposition.** *If $G$ is a topological group and $f:G\to\mathbb{C}$ is a continuous function with compact support, then for any $\varepsilon>0$ there is a neighborhood $U$ of $e$ such that $|f(x)-f(y)|<\varepsilon$ whenever $x^{-1}y\in U$.*

**Proof.** Let $\mathcal U$ be the collection of open neighborhoods $U$ of $e$ such that $U=U^{-1}$. Note that if $V$ is any neighborhood of $e$, then $U=V\cap V^{-1}\in\mathcal U$ and $U\subseteq V$. Order $\mathcal U$ by reverse inclusion.

Suppose the result is false. Then there is an $\varepsilon>0$ such that for every $U$ in $\mathcal U$ there are points $x_U,y_U$ in $G$ with $x_U^{-1}y_U$ in $U$ and $|f(x_U)-f(y_U)|\geq\varepsilon$. Note that either $x_U$ or $y_U\in K\equiv\operatorname{support}f$. Since $U=U^{-1}$, we may assume that $x_U\in K$ for every $U$ in $\mathcal U$. Now $\{x_U:U\in\mathcal U\}$ is a net in $K$. Since $K$ is compact, there is a point $x$ in $K$ such that $x_U\xrightarrow[\mathrm{cl}]{}x$. But $x_U^{-1}y_U\to e$. Since multiplication is continuous, $y_U=x_U(x_U^{-1}y_U)\xrightarrow[\mathrm{cl}]{}x$. Therefore if $W$ is any neighborhood of $x$, there is a $U$ in $\mathcal U$ with $x_U,y_U\in W$. But $f$ is continuous at $x$ so $W$ can be chosen such that $|f(x)-f(w)|<\varepsilon/2$ whenever $w\in W$. With this choice of $W$, $|f(x_U)-f(y_U)|<\varepsilon$, a contradiction. $\blacksquare$

One can rephrase (9.1) by saying that continuous functions on a topological group that have compact support are uniformly continuous.

In the next result it is the case $p=1$ which is of principal interest for us at this time. The proof of the general theorem is, however, no more difficult than this special case.

**9.2. Proposition.** *If $G$ is a locally compact group, $1\leq p<\infty$, and $f\in L^p(G)$, then the map $x\mapsto f_x$ is a continuous function from $G$ into $L^p(G)$.*

**Proof.** Fix $f$ in $L^p(G)$, $x$ in $G$, and $\varepsilon>0$; it must be shown that there is a neighborhood $V$ of $x$ such that for $y$ in $V$, $\|f_y-f_x\|_p<\varepsilon$. First note that there is a continuous function $\phi:G\to\mathbb{C}$ having compact support such that



<a id="pdf-page-240"></a>
$\|f-\phi\|_p<\varepsilon/3$. Let $K=\operatorname{spt}\phi$. Note that because Haar measure is translation invariant, for any $y$ in $G$, $\|f_y-\phi_y\|_p=\|f-\phi\|_p<\varepsilon/3$. Now by Proposition 9.1, there is a neighborhood $U$ of $e$ such that $|\phi(y)-\phi(w)|<\frac{1}{3}\varepsilon[2m(K)]^{-1/p}$ whenever $y^{-1}w\in U$. Put $V=Ux$. If $y\in V$, then

$$
\|\phi_y-\phi_x\|_p^p=\int|\phi(zy^{-1})-\phi(zx^{-1})|^p\,dz.
$$

But $y=ux$ for some $u$ in $U$, so $(zy^{-1})^{-1}(zx^{-1})=yx^{-1}=u\in U$. Thus

$$
\begin{aligned}
\|\phi_y-\phi_x\|_p^p
&=\int_{Ky\cup Kx}|\phi(zy^{-1})-\phi(zx^{-1})|^p\,dz\\
&\leq\left(\frac{\varepsilon}{3}\right)^p[2m(K)]^{-1}m(Ky\cup Kx)\\
&\leq\left(\frac{\varepsilon}{3}\right)^p.
\end{aligned}
$$

Therefore if $y\in V$, $\|f_x-f_y\|_p\leq\|f_x-\phi_x\|_p+\|\phi_x-\phi_y\|_p+\|\phi_y-f_y\|_p<\varepsilon$. $\blacksquare$

The aim of this section is to discuss the homomorphisms on $L^1(G)$ when $G$ is abelian and to examine the Gelfand transform. There is a bit of a difficulty here since $L^1(G)$ does not have an identity when $G$ is not discrete. If $\delta_e$ is the unit point mass at $e$, then $\delta_e$ is the identity for $M(G)$ and hence acts as an identity for $L^1(G)$. Nevertheless $\delta_e\notin L^1(G)$ if $G$ is not discrete. All is not lost as $L^1(G)$ has an approximate identity (Exercise 2.8) of a nice type.

**9.3. Proposition.** *If $f\in L^1(G)$ and $\varepsilon>0$, then there is a neighborhood $U$ of $e$ such that if $g$ is a non-negative Borel function on $G$ that vanishes off $U$ and has $\int g(x)\,dx=1$, then $\|f-f*g\|_1<\varepsilon$.*

**Proof.** By the preceding proposition, there is a neighborhood $U$ of $e$ such that $\|f-f_y\|_1<\varepsilon$ whenever $y\in U$. If $g$ satisfies the conditions, then $f(x)-f*g(x)=\int[f(x)-f(xy^{-1})]g(y)\,dy$ for all $x$. Thus,

$$
\begin{aligned}
\|f-f*g\|_1
&=\int\left|\int_U[f(x)-f(xy^{-1})]g(y)\,dy\right|dx\\
&\leq\int_U g(y)\int|f(x)-f(xy^{-1})|\,dx\,dy\\
&=\int_U g(y)\|f-f_y\|_1\,dy\\
&\leq\varepsilon.
\end{aligned}
$$

$\blacksquare$

**9.4. Corollary.** *There is a net $\{e_i\}$ of non-negative functions in $L^1(G)$ such that $\int e_i\,dm=1$ for all $i$ and $\|e_i*f-f\|_1\to0$ for all $f$ in $L^1(G)$.*



<a id="pdf-page-241"></a>
**Proof.** Let $\mathcal U$ be the collection of all neighborhoods of $e$ and order $\mathcal U$ by reverse inclusion. Let $\mathcal U=\{U_i:i\in I\}$ where $i\leq j$ if and only if $U_j\subseteq U_i$. For each $i$ in $I$ put $e_i=m(U_i)^{-1}\chi_{U_i}$, so $e_i\geq 0$ and $\int e_i\,dm=1$. If $f\in L^1(G)$ and $\varepsilon>0$, let $U_i$ be as in the preceding proposition. So if $j\geq i$, $e_j$ satisfies the conditions on $g$ in (9.3) and hence $\|f-f*e_j\|_1<\varepsilon$. $\blacksquare$

**9.5. Corollary.** If $h:L^1(G)\to\mathbb C$ is a nonzero homomorphism, then $h$ is bounded and $\|h\|=1$.

**Proof.** The fact that $h$ is bounded and $\|h\|\leq 1$ is Exercise 8.3. In light of the preceding corollary if $h(f)\neq 0$, $h(f)=\lim h(f*e_i)=h(f)\lim h(e_i)$. Hence $h(e_i)\to 1$. Since $\|e_i\|=1$ for all $i$, $\|h\|=1$. $\blacksquare$

Even though Haar measure on most of the popular examples is $\sigma$-finite, this is not true in general. For example, if $D$ is an uncountable discrete group, the Haar measure on $D$ is counting measure and, hence, not $\sigma$-finite. Similarly, Haar measure on $D\times\mathbb R$ is not $\sigma$-finite. Nevertheless, it is true that $L^1(G)^*=L^\infty(G)$ for any locally compact group because $(G,m)$ is an example of a decomposable measure space, though $L^\infty(G)$ must be redefined to be the equivalence classes of bounded Borel functions that are equal a.e. on every set of finite Haar measure. This fact will be assumed here. The interested reader can consult Hewitt and Ross [1963].

**9.6. Theorem.** If $G$ is a locally compact abelian group and $\gamma:G\to\mathbb T$ is a continuous homomorphism, define $\hat f(\gamma)$ by

$$
\hat f(\gamma)=\int f(x)\gamma(x^{-1})\,dx \tag{9.7}
$$

for every $f$ in $L^1(G)$. Then $f\mapsto\hat f(\gamma)$ is a nonzero homomorphism on $L^1(G)$. Conversely, if $h:L^1(G)\to\mathbb C$ is a nonzero homomorphism, there is a continuous homomorphism $\gamma:G\to\mathbb T$ such that $h(f)=\hat f(\gamma)$.

**Proof.** First note that if $\gamma:G\to\mathbb T$ is a homomorphism, $\gamma(xy)=\gamma(x)\gamma(y)$ and $\gamma(x^{-1})=\gamma(x)^{-1}=\overline{\gamma(x)}$, the complex conjugate of $\gamma(x)$. If $f,g\in L^1(G)$, then

$$
\begin{aligned}
\widehat{f*g}(\gamma)
&=\int(f*g)(x)\gamma(x^{-1})\,dx\\
&=\int\gamma(x^{-1})\int f(xy^{-1})g(y)\,dy\,dx\\
&=\int g(y)\gamma(y^{-1})
  \left[\int f(xy^{-1})\gamma\bigl((xy^{-1})^{-1}\bigr)\,dx\right]dy.
\end{aligned}
$$

But the invariance of the Haar integral gives that $\int f(xy^{-1})\gamma\bigl((xy^{-1})^{-1}\bigr)\,dx=\int f(x)\gamma(x^{-1})\,dx$. Hence



<a id="pdf-page-242"></a>
$$
\widehat{f*g}(\gamma)
=\int g(y)\gamma(y^{-1})
\left[\int f(x)\gamma(x^{-1})\,dx\right]dy
=\hat f(\gamma)\hat g(\gamma).
$$

So $f\mapsto\hat f(\gamma)$ is a homomorphism. Since $\gamma$ is continuous and $\gamma(G)\subseteq\mathbb T$, $\gamma\in L^\infty(G)$ and $\|\gamma\|_\infty=1$. Thus $f\mapsto\hat f(\gamma)$ is not identically zero.

Now assume that $h:L^1(G)\to\mathbb C$ is a nonzero homomorphism. Since $h$ is a bounded linear functional, there is a $\phi$ in $L^\infty(G)$ such that $h(f)=\int f(x)\phi(x)\,dx$ and $\|\phi\|_\infty=\|h\|=1$. If $f,\ g\in L^1(G)$, then $h(f*g)=\int(f*g)(x)\phi(x)\,dx=\int g(y)[\int f(xy^{-1})\phi(x)\,dx]\,dy=\int g(y)h(f_y)\,dy$. [Note that $y\mapsto h(f_y)$ is a continuous scalar-valued function by Proposition 9.2.] But $h(f*g)=h(f)h(g)=\int g(y)h(f)\phi(y)\,dy$. So

$$
0=\int g(y)[h(f_y)-h(f)\phi(y)]\,dy
$$

for every $g$ in $L^1(G)$. But $y\mapsto h(f_y)-h(f)\phi(y)$ belongs to $L^\infty(G)$, so for any $f$ in $L^1(G)$,

$$
\tag{9.8} h(f_y)=h(f)\phi(y)
$$

for locally almost all $y$ in $G$. Pick $f$ in $L^1(G)$ such that $h(f)\ne0$. By (9.8), $\phi(y)=h(f_y)/h(f)$ a.e. But the right-hand side of this equation is continuous. Hence we may assume that $\phi$ is a continuous function. Thus for every $f$ in $L^1(G)$, (9.8) holds everywhere.

In (9.8), replace $y$ by $xy$ and we obtain $h(f)\phi(xy)=h(f_{xy})=h((f_x)_y)$. Now replace $f$ in (9.8) by $f_x$ to get $h(f_x)\phi(y)=h(f_{xy})$. Thus $h(f)\phi(xy)=h(f_x)\phi(y)=[h(f)\phi(x)]\phi(y)$. If $h(f)\ne0$, this implies $\phi(xy)=\phi(x)\phi(y)$ for all $x,y$ in $G$. Thus $\phi:G\to\mathbb C$ is a homomorphism and $|\phi(x)|\leq1$ for all $x$. But $1=\phi(e)=\phi(x)\phi(x^{-1})=\phi(x)\phi(x)^{-1}$ and $|\phi(x)|,|\phi(x)^{-1}|\leq1$. Hence $|\phi(x)|=1$ for all $x$ in $G$. If $\gamma(x)=\phi(x^{-1})$, then $\gamma:G\to\mathbb T$ is a continuous homomorphism and $h(f)=\hat f(\gamma)$ for all $f$ in $L^1(G)$. $\blacksquare$

Let $\Sigma$ be the set of nonzero homomorphisms on $L^1(G)$, where $G$ is assumed to be abelian (both here and throughout the rest of the chapter). So $\Sigma\subseteq\operatorname{ball}L^1(G)^*$. If $h\in\operatorname{ball}L^1(G)^*$ and $\{h_i\}$ is a net in $\Sigma$ such that $h_i\to h$ weak$^*$, then it is easy to see that $h$ is multiplicative. Thus the weak$^*$ closure of $\Sigma\subseteq\Sigma\cup\{0\}$. Hence the relative weak$^*$ topology on $\Sigma$ makes $\Sigma$ into a locally compact Hausdorff space (see Exercise 8.4).

Let $\Gamma=$ all the continuous homomorphisms $\gamma:G\to\mathbb T$. By Theorem 9.6, $\Sigma$ and $\Gamma$ can be identified using formula (9.7). In fact, the map defined in (9.7) is the Gelfand transform when this identification is made. (Just look at the definitions.) Since $\Sigma$ and $\Gamma$ are identified and $\Sigma$ has a topology, $\Gamma$ can be given a topology. Thus $\Gamma$ becomes a locally compact space with this topology. (For another description of the topology, see Exercise 6.) The functions in $\Gamma$ are called *characters* and are sometimes denoted by $\Gamma=\hat G$ and called the *dual group*.



<a id="pdf-page-243"></a>
Also notice that in a natural way $\Gamma$ is a group. If $\gamma_1,\gamma_2\in\Gamma$, then $(\gamma_1\gamma_2)(x)\equiv\gamma_1(x)\gamma_2(x)$ and $\gamma_1\gamma_2\in\Gamma$.

**9.9. Proposition.** $\Gamma$ is a *locally compact abelian group*.

Clearly $\Gamma$ is an abelian group and we know that $\Gamma$ is a locally compact space. It must be shown that $\Gamma$ is a topological group. To do this we first prove a lemma.

**9.10. Lemma.**

(a) *The map $(x,\gamma)\mapsto\gamma(x)$ of $G\times\Gamma\to\mathbb T$ is continuous.*

(b) *If $\{\gamma_i\}$ is a net in $\Gamma$ and $\gamma_i\to\gamma$ in $\Gamma$, then $\gamma_i(x)\to\gamma(x)$ uniformly for $x$ belonging to any compact subset of $G$.*

**Proof.** First note that if $x\in G$ and $f\in L^1(G)$, then for every $\gamma$ in $\Gamma$,

$$
\begin{aligned}
\widehat f_x(\gamma)
&=\int f_x(y)\gamma(y^{-1})\,dy\\
&=\int f(yx^{-1})\gamma(y^{-1})\,dy\\
&=\int f(z)\gamma(z^{-1}x^{-1})\,dz\\
&=\gamma(x^{-1})\widehat f(\gamma).
\end{aligned}
$$

So if $\gamma_i\to\gamma$ in $\Gamma$ and $x_i\to x$ in $G$,

$$
\begin{aligned}
\left|\widehat f(\gamma_i)\gamma_i(x_i)-\widehat f(\gamma)\gamma(x)\right|
&=\left|\widehat f_{x_i^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma)\right|\\
&\leq\left|\widehat f_{x_i^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma_i)\right|
+\left|\widehat f_{x^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma)\right|.
\end{aligned}
$$

But $\left|\widehat f_{x_i^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma_i)\right|\leq\|f_{x_i^{-1}}-f_{x^{-1}}\|_1\to0$ by (9.2). Because $f_{x^{-1}}\in L^1(G)$, $\widehat f_{x^{-1}}(\gamma_i)\to\widehat f_{x^{-1}}(\gamma)$ since $\gamma_i\to\gamma$. Thus $\widehat f(\gamma_i)\gamma_i(x_i)\to\widehat f(\gamma)\gamma(x)$. If $f$ is chosen so that $\widehat f(\gamma)\ne0$, then because $\widehat f(\gamma_i)\to\widehat f(\gamma)$, there is an $i_0$ such that $\widehat f(\gamma_i)\ne0$ for $i\geq i_0$. Therefore $\gamma_i(x_i)\to\gamma(x)$ and (a) is proven.

Now let $K$ be a compact subset of $G$ and let $\{\gamma_i\}$ be a net in $\Gamma$ such that $\gamma_i\to\gamma_0$. Suppose $\{\gamma_i(x)\}$ does not converge uniformly on $K$ to $\gamma_0(x)$. Then there is an $\varepsilon>0$ such that for every $i$, there is a $j_i\geq i$ and an $x_i$ in $K$ such that $|\gamma_{j_i}(x_i)-\gamma_0(x_i)|\geq\varepsilon$. Now $\{\gamma_{j_i}\}$ is a net and $\gamma_{j_i}\to\gamma_0$ (Exercise). Since $K$ is compact, there is an $x_0$ in $K$ such that $x_i\xrightarrow[\mathrm{cl}]{}x_0$. Now part (a) implies that the map $(x,\gamma)\mapsto(\gamma(x),\gamma_0(x))$ of $G\times\Gamma$ into $\mathbb T\times\mathbb T$ is continuous. Since $(x_i,\gamma_{j_i})\xrightarrow[\mathrm{cl}]{}(x_0,\gamma_0)$ in $G\times\Gamma$, $(\gamma_{j_i}(x_i),\gamma_0(x_i))\xrightarrow[\mathrm{cl}]{}(\gamma_0(x_0),\gamma_0(x_0))$. So for any $i_0$, there is an $i\geq i_0$ such that $|\gamma_{j_i}(x_i)-\gamma_0(x_0)|<\varepsilon/2$ and $|\gamma_0(x_i)-\gamma_0(x_0)|<\varepsilon/2$. Hence $|\gamma_{j_i}(x_i)-\gamma_0(x_i)|<\varepsilon$, a contradiction. $\blacksquare$

**Proof of Proposition 9.9.** Let $\{\gamma_i\}$, $\{\lambda_i\}$ be nets in $\Gamma$ such that $\gamma_i\to\gamma$ and $\lambda_i\to\lambda$. It must be shown that $\gamma_i\lambda_i^{-1}\to\gamma\lambda^{-1}$. Let $\phi\in C_c(G)$ and put $K=\operatorname{spt}\phi$.



<a id="pdf-page-244"></a>
Then $\widehat{\phi}(\gamma_i\lambda_i^{-1})=\int_K\phi(x)\gamma_i(x^{-1})\lambda_i(x)\,dx$. By the preceding lemma, $\gamma_i(x^{-1})\to\gamma(x^{-1})$ and $\lambda_i(x)\to\lambda(x)$ uniformly for $x$ in $K$. Thus $\widehat{\phi}(\gamma_i\lambda_i^{-1})\to\widehat{\phi}(\gamma\lambda^{-1})$. If $f\in L^1(G)$ and $\varepsilon>0$, let $\phi\in C_c(G)$ such that $\|f-\phi\|_1<\varepsilon/3$. Then

$$
\left|\widehat f(\gamma_i\lambda_i^{-1})-\widehat f(\gamma\lambda^{-1})\right|
<\frac{2\varepsilon}{3}
+\left|\widehat\phi(\gamma_i\lambda_i^{-1})-\widehat\phi(\gamma\lambda^{-1})\right|.
$$

It follows that $\widehat f(\gamma_i\lambda_i^{-1})\to\widehat f(\gamma\lambda^{-1})$ for every $f$ in $L^1(G)$. Hence $\gamma_i\lambda_i^{-1}\to\gamma\lambda^{-1}$ in $\Gamma$. ■

Since $\Gamma$ is a locally compact abelian group, it too has a dual group. Let $\widehat\Gamma$ be this dual group. If $x\in G$, define $\rho(x):\Gamma\to\mathbb T$ by $\rho(x)(\gamma)=\gamma(x)$. It is easy to see that $\rho$ is a homomorphism. It is a rather deep fact, entitled the Pontryagin Duality Theorem, that $\rho:G\to\widehat\Gamma$ is a homeomorphism and an isomorphism. That is, $G$ “is” the dual group of its dual group. The interested reader may consult Rudin [1962]. We turn now to some examples.

**9.11. Theorem.** *If $y\in\mathbb R$, then $\gamma_y(x)=e^{ixy}$ defines a character on $\mathbb R$ and every character on $\mathbb R$ has this form. The map $y\mapsto\gamma_y$ is a homeomorphism and an isomorphism of $\mathbb R$ onto $\widehat{\mathbb R}$. If $y\in\mathbb R$ and $f\in L^1(\mathbb R)$, then*

$$
\tag{9.12}
\widehat f(\gamma_y)=\widehat f(y)=\int_{-\infty}^{\infty}f(x)e^{-ixy}\,dx,
$$

*the Fourier transform of $f$.*

**Proof.** If $y\in\mathbb R$, then $|\gamma_y(x)|=1$ for all $x$ and $\gamma_y(x_1+x_2)=\gamma_y(x_1)\gamma_y(x_2)$. So $\gamma_y\in\widehat{\mathbb R}$. Also, $\gamma_{y_1+y_2}(x)=\gamma_{y_1}(x)\gamma_{y_2}(x)$. Hence $y\mapsto\gamma_y$ is a homomorphism of $\mathbb R$ into $\widehat{\mathbb R}$.

Now let $\gamma\in\widehat{\mathbb R}$. $\gamma(0)=1$ so that there is a $\delta>0$ such that $\int_0^\delta\gamma(x)\,dx=a\ne0$. Thus

$$
\begin{aligned}
a\gamma(x)
&=\gamma(x)\int_0^\delta\gamma(t)\,dt\\
&=\int_0^\delta\gamma(x+t)\,dt\\
&=\int_x^{x+\delta}\gamma(t)\,dt.
\end{aligned}
$$

Hence $\gamma(x)=a^{-1}\int_x^{x+\delta}\gamma(t)\,dt$. Because $\gamma$ is continuous, the Fundamental Theorem of Calculus implies that $\gamma$ is differentiable. Also,

$$
\frac{\gamma(x+h)-\gamma(x)}{h}
=\gamma(x)\left[\frac{\gamma(h)-1}{h}\right].
$$

So $\gamma'(x)=\gamma'(0)\gamma(x)$. Since $\gamma(0)=1$ and $|\gamma(x)|=1$ for all $x$, the elementary



<a id="pdf-page-245"></a>
theory of differential equations implies that $\gamma=\gamma_y$ for some $y$ in $\mathbb R$. This implies that $y\mapsto\gamma_y$ is an isomorphism of $\mathbb R$ onto $\mathbb R$.

It is clear from (9.7) that (9.12) holds. From here it is easy to see that $y\mapsto\gamma_y$ is a homeomorphism of $\mathbb R$ onto $\widehat{\mathbb R}$. ■

So the preceding result says that $\mathbb R$ is its own dual group. Because of (9.12), the function $\widehat f$ as defined in (9.7) is called the *Fourier transform* of $f$. The next result lends more weight to the use of this terminology.

**9.13. Theorem.** *If $n\in\mathbb Z$, define $\gamma_n:\mathbb T\to\mathbb T$ by $\gamma_n(z)=z^n$. Then $\gamma_n\in\widehat{\mathbb T}$ and the map $n\mapsto\gamma_n$ is a homeomorphism and an isomorphism of $\mathbb Z$ onto $\widehat{\mathbb T}$. If $n\in\mathbb Z$ and $f\in L^1(\mathbb T)$, then*

**9.14**
$$
\widehat f(\gamma_n)=\widehat f(n)\equiv\frac{1}{2\pi}\int_0^{2\pi}f(e^{i\theta})e^{-in\theta}\,d\theta.
$$

**Proof.** It is left to the reader to check that $\gamma_n\in\widehat{\mathbb T}$ and $n\mapsto\gamma_n$ is an injective homomorphism of $\mathbb Z$ into $\widehat{\mathbb T}$. If $\gamma\in\widehat{\mathbb T}$, define $\sigma:\mathbb R\to\mathbb T$ by $\sigma(t)=\gamma(e^{it})$; it follows that $\sigma\in\widehat{\mathbb R}$. By (9.11), $\sigma(t)=e^{iyt}$ for some $y$ in $\mathbb R$. But $\sigma(t+2\pi)=\sigma(t)$, so $e^{2\pi iy}=1$. Hence $y=n\in\mathbb Z$. Thus $\gamma(e^{i\theta})=\sigma(\theta)=e^{in\theta}$, $\gamma=\gamma_n$, and $n\mapsto\gamma_n$ is an isomorphism of $\mathbb Z$ onto $\widehat{\mathbb T}$. Formula (9.14) is immediate from (9.7). The fact that $n\mapsto\gamma_n$ is a homeomorphism is left as an exercise. ■

So $\widehat{\mathbb T}=\mathbb Z$, a discrete group. This can be generalized.

**9.15. Theorem.** *If $G$ is compact, $\widehat G$ is discrete; if $G$ is discrete, $\widehat G$ is compact.*

**Proof.** Put $\Gamma=\widehat G$. If $G$ is discrete, then $L^1(G)$ has an identity. Hence its maximal ideal space is compact. That is, $\Gamma$ is compact.

Now assume that $G$ is compact. Hence $\Gamma\subseteq L^1(G)$ since $m(G)=1$. Suppose $\gamma\in\Gamma$ and $\gamma\ne$ the identity for $\Gamma$, then there is a point $x_0$ in $G$ such that $\gamma(x_0)\ne1$. Thus
$$
\begin{aligned}
\int\gamma(x)\,dx
&=\int\gamma(xx_0^{-1}x_0)\,dx\\
&=\gamma(x_0)\int\gamma(xx_0^{-1})\,dx\\
&=\gamma(x_0)\int\gamma(x)\,dx,
\end{aligned}
$$
since Haar measure is translation invariant. Since $\gamma(x_0)\ne1$, this implies that
$$
\int_G\gamma(x)\,dx=0\qquad\text{if }\gamma\ne1.
$$

Of course if $\gamma=1$, $\int 1\,dx=m(G)=1$. So if $f=1$ on $G$, $f\in L^1(G)$ and



<a id="pdf-page-246"></a>
$$
\hat f(\gamma)=\int \gamma(x^{-1})\,dx=\chi_{\{1\}}(\gamma).
$$

Since $\hat f$ is continuous on $\Gamma$, $\{1\}$ is an open set. By translation, every singleton set in $\Gamma$ is open and hence $\Gamma$ is discrete. $\blacksquare$

**9.16. Theorem.** If $a\in\mathbb T$, define $\gamma_a:\mathbb Z\to\mathbb T$ by $\gamma_a(n)=a^n$. Then $\gamma_a\in\widehat{\mathbb Z}$ and the map $a\mapsto\gamma_a$ is a homeomorphism and an isomorphism of $\mathbb T$ onto $\widehat{\mathbb Z}$. If $a\in\mathbb T$ and $f\in L^1(\mathbb Z)=l^1(\mathbb Z)$, then

$$
\hat f(\gamma_a)=\hat f(a)=\sum_{n=-\infty}^{\infty}f(n)a^{-n}. \tag{9.17}
$$

**Proof.** Again the proof that $a\mapsto\gamma_a$ is a monomorphism of $\mathbb T\to\widehat{\mathbb Z}$ is left to the reader. If $\gamma\in\widehat{\mathbb Z}$, let $\gamma(1)=a\in\mathbb T$. Also, $\gamma(n)=\gamma(1)^n=a^n$, so $\gamma=\gamma_a$. Hence $a\mapsto\gamma_a$ is an isomorphism. It is easy to show that this map is continuous and hence, by compactness, a homeomorphism. $\blacksquare$

For additional reading, consult Rudin [1962].

## Exercises

1. Prove that if $L^1(G)$ has an identity, then $G$ is discrete.

2. If $f\in L^\infty(G)$, show that $x\mapsto f_x$ is a continuous function from $G$ into $(L^\infty(G),\mathrm{wk}^*)$.

3. Is there a measure $\mu$ on $\mathbb R$ different from Lebesgue measure such that for $f$ in $L^1(\mu)$, $x\mapsto f_x$ is continuous? Is there a measure for which this map is discontinuous?

4. If $f\in C_0(G)$, show that $x\mapsto f_x$ is a continuous map from $G\to C_0(G)$.

5. If $f\in L^\infty(G)$ and $f$ is uniformly continuous on $G$, show that $x\mapsto f_x$ is a continuous function from $G\to L^\infty(G)$. Is the converse true? See Edwards [1961].

6. If $K$ is a compact subset of $G$, $\gamma_0\in\Gamma$, and $\varepsilon>0$, let $U(K,\gamma_0,\varepsilon)=\{\gamma\in\Gamma:|\gamma(x)-\gamma_0(x)|<\varepsilon\text{ for all }x\in K\}$. Show that the collection of all such sets is a base for the topology of $\Gamma$. (This says that the topology on $\Gamma$ is the *compact-open topology*.)

7. Show that there is a discontinuous homomorphism $\gamma:\mathbb R\to\mathbb T$. If $\gamma:\mathbb R\to\mathbb T$ is a homomorphism that is a Borel function, show that $\gamma$ is continuous.

8. If $G$ is a compact abelian group, show that the linear span of $\Gamma$ is dense in $C(G)$.

9. If $G$ is a compact abelian group, show that $\Gamma$ forms an orthonormal basis in $L^2(G)$.

10. If $G$ is a compact abelian group, show that $G$ is metrizable if and only if $\Gamma$ is countable.

11. Let $\{G_\alpha\}$ be a family of compact abelian groups and $G=\prod_\alpha G_\alpha$. If $\Gamma_\alpha=\widehat{G_\alpha}$, show that the character group of $G$ is $\{\{\gamma_\alpha\}\in\prod_\alpha\Gamma_\alpha:\gamma_\alpha=e\text{ except for at most a finite number of }\alpha\}$.

