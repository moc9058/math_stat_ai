# III. Banach Spaces

<!-- OCR draft; page images require independent visual review. -->


<a id="pdf-page-78"></a>
# CHAPTER III

# Banach Spaces

The concept of a Banach space is a generalization of Hilbert space. A Banach space assumes that there is a norm on the space relative to which the space is complete, but it is not assumed that the norm is defined in terms of an inner product. There are many examples of Banach spaces that are not Hilbert spaces, so that the generalization is quite useful.

## §1. Elementary Properties and Examples

**1.1. Definition.** If $\mathcal{X}$ is a vector space over $\mathbb{F}$, a *seminorm* is a function $p:\mathcal{X}\to[0,\infty)$ having the properties:

(a) $p(x+y)\leq p(x)+p(y)$ for all $x,y$ in $\mathcal{X}$.

(b) $p(\alpha x)=|\alpha|p(x)$ for all $\alpha$ in $\mathbb{F}$ and $x$ in $\mathcal{X}$.

It follows from (b) that $p(0)=0$. A *norm* is a seminorm $p$ such that

(c) $x=0$ if $p(x)=0$.

Usually a norm is denoted by $\|\cdot\|$.

The norm on a Hilbert space is a norm. Also, the norm on $\mathcal{B}(\mathcal{H})$ is a norm.

If $\mathcal{X}$ has a norm, then $d(x,y)=\|x-y\|$ defines a metric on $\mathcal{X}$.

**1.2. Definition.** A *normed space* is a pair $(\mathcal{X},\|\cdot\|)$, where $\mathcal{X}$ is a vector space and $\|\cdot\|$ is a norm on $\mathcal{X}$. A *Banach space* is a normed space that is complete with respect to the metric defined by the norm.

**1.3. Proposition.** *If $\mathcal{X}$ is a normed space, then*

(a) *the function $\mathcal{X}\times\mathcal{X}\to\mathcal{X}$ defined by $(x,y)\mapsto x+y$ is continuous;*

(b) *the function $\mathbb{F}\times\mathcal{X}\to\mathcal{X}$ defined by $(\alpha,x)\mapsto\alpha x$ is continuous.*



<a id="pdf-page-79"></a>
64　　　　　　　　　　　　　　　　　III. Banach Spaces

**Proof.** If $x_n\to x$ and $y_n\to y$, then $\|(x_n+y_n)-(x+y)\|=\|(x_n-x)+(y_n-y)\|\leq\|x_n-x\|+\|y_n-y\|\to0$ as $n\to\infty$. This proves (a). The proof of (b) is left to the reader. $\blacksquare$

The next lemma is quite useful.

**1.4. Lemma.** *If $p$ and $q$ are seminorms on a vector space $\mathcal{X}$, then the following statements are equivalent.*

(a) $p(x)\leq q(x)$ *for all* $x$. (*That is,* $p\leq q$.)

(b) $\{x\in\mathcal{X}:q(x)<1)\}\subseteq\{x\in\mathcal{X}:p(x)<1\}$.

(b′) $p(x)<1$ *whenever* $q(x)<1$.

(c) $\{x:q(x)\leq1\}\subseteq\{x:p(x)\leq1\}$.

(c′) $p(x)\leq1$ *whenever* $q(x)\leq1$.

(d) $\{x:q(x)<1\}\subseteq\{x:p(x)\leq1\}$.

(d′) $p(x)\leq1$ *whenever* $q(x)<1$.

**Proof.** It is clear that (b) and (b′), (c) and (c′), and (d) and (d′) are equivalent. It is also clear that (a) implies all of the remaining conditions and that both (b) and (c) imply (d). It remains to show that (d) implies (a).

Assume that (d) holds and put $q(x)=\alpha$. If $\varepsilon>0$, then $q((\alpha+\varepsilon)^{-1}x)=(\alpha+\varepsilon)^{-1}\alpha<1$. By (d), $1\geq p((\alpha+\varepsilon)^{-1}x)=(\alpha+\varepsilon)^{-1}p(x)$, so $p(x)\leq\alpha+\varepsilon=q(x)+\varepsilon$. Letting $\varepsilon\to0$ shows (a). $\blacksquare$

If $\|\cdot\|_1$ and $\|\cdot\|_2$ are two norms on $\mathcal{X}$, they are said to be *equivalent norms* if they define the same topology on $\mathcal{X}$.

**1.5. Proposition.** *If $\|\cdot\|_1$ and $\|\cdot\|_2$ are two norms on $\mathcal{X}$, then these norms are equivalent if and only if there are positive constants $c$ and $C$ such that*

$$
c\|x\|_1\leq\|x\|_2\leq C\|x\|_1
$$

*for all $x$ in $\mathcal{X}$.*

**Proof.** Suppose there are constants $c$ and $C$ such that $c\|x\|_1\leq\|x\|_2\leq C\|x\|_1$ for all $x$ in $\mathcal{X}$. Fix $x_0$ in $\mathcal{X}$, $\varepsilon>0$. Then

$$
\{x\in\mathcal{X}:\|x-x_0\|_1<\varepsilon/C\}\subseteq
\{x\in\mathcal{X}:\|x-x_0\|_2<\varepsilon\},
$$

$$
\{x\in\mathcal{X}:\|x-x_0\|_2<c\varepsilon\}\subseteq
\{x\in\mathcal{X}:\|x-x_0\|_1<\varepsilon\}.
$$

This shows that the two topologies are the same. Now assume that the two norms are equivalent. Hence $\{x:\|x\|_1<1\}$ is an open neighborhood of $0$ in the topology defined by $\|\cdot\|_2$. Therefore there is an $r>0$ such that $\{x:\|x\|_2<r\}\subseteq\{x:\|x\|_1<1\}$. If $q(x)=r^{-1}\|x\|_2$ and $p(x)=\|x\|_1$, the preceding lemma implies $\|x\|_1\leq r^{-1}\|x\|_2$ or $c\|x\|_1\leq\|x\|_2$, where $c=r$. The other inequality is left to the reader. $\blacksquare$

There are two types of properties of a Banach space: those that are topological and those that are metric. The metric properties depend on the



<a id="pdf-page-80"></a>
precise norm; the topological ones depend only on the equivalence class of norms (see Exercise 4).

**1.6. Example.** Let $X$ be any Hausdorff space (all spaces in this book are assumed to be Hausdorff unless the contrary is specified) and let $C_b(X)=$ all continuous functions $f:X\to\mathbb F$ such that $\|f\|\equiv\sup\{|f(x)|:x\in X\}<\infty$. For $f,g$ in $C_b(X)$, define $(f+g):X\to\mathbb F$ by $(f+g)(x)=f(x)+g(x)$; for $\alpha$ in $\mathbb F$ define $(\alpha f)(x)=\alpha f(x)$. Then $C_b(X)$ is a Banach space.

The proofs of the statements in (1.6) are all routine except, perhaps, for the fact that $C_b(X)$ is complete. To see this, let $\{f_n\}$ be a Cauchy sequence in $C_b(X)$. So if $\varepsilon>0$, there is an integer $N_\varepsilon$ such that for $n,m\geqslant N_\varepsilon$,
$\varepsilon>\|f_n-f_m\|=\sup\{|f_n(x)-f_m(x)|:x\in X\}$. In particular, for any $x$ in $X$, $|f_n(x)-f_m(x)|\leqslant\|f_n-f_m\|<\varepsilon$ when $n,m\geqslant N_\varepsilon$. So $\{f_n(x)\}$ is a Cauchy sequence in $\mathbb F$. Let $f(x)=\lim_{n\to\infty}f_n(x)$ if $x\in X$. Now fix $x$ in $X$. If $n,m\geqslant N_\varepsilon$, then $|f(x)-f_n(x)|\leqslant|f(x)-f_m(x)|+\|f_m-f_n\|<|f(x)-f_m(x)|+\varepsilon$. Letting $m\to\infty$ gives that $|f(x)-f_n(x)|\leqslant\varepsilon$ when $n\geqslant N_\varepsilon$. This is independent of $x$. Hence $\|f-f_n\|\leqslant\varepsilon$ for $n\geqslant N_\varepsilon$.

What has been just shown is that $\|f-f_n\|\to0$ as $n\to\infty$. Note that this implies that $f_n(x)\to f(x)$ uniformly on $X$. It is standard that $f$ is continuous. Also, $\|f\|\leqslant\|f-f_n\|+\|f_n\|<\infty$. Hence $f\in C_b(X)$ and so $C_b(X)$ is complete.

Note that a linear subspace $\mathcal Y$ of a Banach space $\mathcal X$ that is topologically closed is also a Banach space if it has the norm of $\mathcal X$.

**1.7. Proposition.** *If $X$ is a locally compact space and $C_0(X)=$ all continuous functions $f:X\to\mathbb F$ such that for all $\varepsilon>0$, $\{x\in X:|f(x)|\geqslant\varepsilon\}$ is compact, then $C_0(X)$ is a closed subspace of $C_b(X)$ and hence is a Banach space.*

**Proof.** That $C_0(X)$ is a linear manifold in $C_b(X)$ is left as an exercise. It will only be shown that $C_0(X)$ is closed in $C_b(X)$. Let $\{f_n\}\subseteq C_0(X)$ and suppose $f_n\to f$ in $C_b(X)$. If $\varepsilon>0$, there is an integer $N$ such that $\|f_n-f\|<\varepsilon/2$; that is, $|f_n(x)-f(x)|<\varepsilon/2$ for all $n\geqslant N$ and $x$ in $X$. If $|f(x)|\geqslant\varepsilon$, then $\varepsilon\leqslant|f(x)-f_n(x)+f_n(x)|\leqslant\varepsilon/2+|f_n(x)|$ for $n\geqslant N$; so $|f_n(x)|\geqslant\varepsilon/2$ for $n\geqslant N$. Thus, $\{x\in X:|f(x)|\geqslant\varepsilon\}\subseteq\{x\in X:|f_N(x)|\geqslant\varepsilon/2\}$ so that $f\in C_0(X)$. ■

The space $C_0(X)$ is the set of continuous functions on $X$ that *vanish at infinity*. If $X=\mathbb R$, then $C_0(\mathbb R)=$ all of the continuous functions $f:\mathbb R\to\mathbb F$ such that $\lim_{x\to\pm\infty}f(x)=0$. If $X$ is compact, $C_0(X)=C_b(X)\equiv C(X)$.

If $I$ is any set, then give $I$ the discrete topology. Hence $I$ becomes locally compact. Also any function on $I$ is continuous. Rather than $C_b(I)$, the customary notation is $\ell^\infty(I)$. That is, $\ell^\infty(I)=$ all bounded functions $f:I\to\mathbb F$ with $\|f\|=\sup\{|f(i)|:i\in I\}$. $c_0(I)$ consists of all functions $f:I\to\mathbb F$ such that for every $\varepsilon>0$, $\{i\in I:|f(i)|\geqslant\varepsilon\}$ is finite. If $I=\mathbb N$, the usual notation for these spaces is $\ell^\infty$ and $c_0$. Note that $\ell^\infty$ consists of all bounded sequences of scalars and $c_0$ consists of all sequences that converge to 0.



<a id="pdf-page-81"></a>
**1.8. Example.** If $(X,\Omega,\mu)$ is a measure space and $1\leq p\leq\infty$, then $L^p(X,\Omega,\mu)$ is a Banach space.

The preceding example is usually proved in courses on integration and no proof is given here.

**1.9. Example.** Let $I$ be a set and $1\leq p<\infty$. Define $\ell^p(I)$ to be the set of all functions $f:I\to\mathbf F$ such that $\sum\{|f(i)|^p:i\in I\}<\infty$; and define $\|f\|_p=(\sum\{|f(i)|^p:i\in I\})^{1/p}$. Then $\ell^p(I)$ is a Banach space. If $I=\mathbf N$, then $\ell^p(\mathbf N)=\ell^p$.

If $\Omega=$ all subsets of $I$ and for each $\Delta$ in $\Omega$, $\mu(\Delta)=$ the number of points in $\Delta$ if $\Delta$ is finite and $\mu(\Delta)=\infty$ otherwise, then $\ell^p(I)=L^p(I,\Omega,\mu)$. So the statement in (1.9) is a consequence of the one in (1.8).

**1.10. Example.** Let $n\geq1$ and let $C^{(n)}[0,1]=$ the collection of functions $f:[0,1]\to\mathbf F$ such that $f$ has $n$ continuous derivatives. Define $\|f\|=\sup_{0\leq k\leq n}\{\sup\{|f^{(k)}(x)|:0\leq x\leq1\}\}$. Then $C^{(n)}[0,1]$ is a Banach space.

**1.11. Example.** Let $1\leq p<\infty$ and $n\geq1$ and let $W_p^n[0,1]=$ the functions $f:[0,1]\to\mathbf F$ such that $f$ has $n-1$ continuous derivatives, $f^{(n-1)}$ is absolutely continuous, and $f^{(n)}\in L^p[0,1]$. For $f$ in $W_p^n[0,1]$, define

$$
\|f\|=\sum_{k=0}^{n}\left[\int_0^1|f^{(k)}(x)|^p\,dx\right]^{1/p}.
$$

Then $W_p^n[0,1]$ is a Banach space.

The following is a useful fact about seminorms.

**1.12. Proposition.** If $p$ is a seminorm on $\mathcal X$, $|p(x)-p(y)|\leq p(x-y)$ for all $x,y$ in $\mathcal X$. If $\|\cdot\|$ is a norm, then $|\|x\|-\|y\||\leq\|x-y\|$ for all $x,y$ in $\mathcal X$.

**Proof.** Of course, the inequality for norms is a consequence of the one for seminorms. Note that if $x,y\in\mathcal X$, $p(x)=p(x-y+y)\leq p(x-y)+p(y)$, so $p(x)-p(y)\leq p(x-y)$. Similarly, $p(y)-p(x)\leq p(x-y)$. ■

There is the concept of “isomorphism” for the category of Banach spaces.

**1.13. Definition.** If $\mathcal X$ and $\mathcal Y$ are normed spaces, $\mathcal X$ and $\mathcal Y$ are *isometrically isomorphic* if there is a surjective linear isometry from $\mathcal X$ onto $\mathcal Y$.

The term *isomorphism* in Banach space theory is reserved for linear bijections $T:\mathcal X\to\mathcal Y$ that are homeomorphisms.

**EXERCISES**

1. Complete the proof of Proposition 1.3.
2. Complete the proof of Proposition 1.5.



<a id="pdf-page-82"></a>
3. For $1\leq p<\infty$ and $x=(x_1,\ldots,x_d)$ in $\mathbb F^d$, define $\|x\|_p\equiv\left[\sum_{j=1}^d|x_j|^p\right]^{1/p}$; define $\|x\|_\infty\equiv\sup\{|x_j|:1\leq j\leq d\}$. Show that all of these norms are equivalent. For $1\leq p,q\leq\infty$, what are the best constants $c$ and $C$ such that $c\|x\|_p\leq\|x\|_q\leq C\|x\|_p$ for all $x$ in $\mathbb F^d$?

4. If $1\leq p\leq\infty$ and $\|\cdot\|_p$ is defined on $\mathbb R^2$ as in Exercise 3, graph $\{x\in\mathbb R^2:\|x\|_p=1\}$. Note that if $1<p<\infty$, $\|x\|_p=\|y\|_p=1$, and $x\neq y$, then for $0<t<1$, $\|tx+(1-t)y\|_p<1$. The same cannot be said for $p=1,\infty$.

5. Let $c$ = the set of all sequences $\{\alpha_n\}_1^\infty$, $\alpha_n$ in $\mathbb F$, such that $\lim\alpha_n$ exists. Show that $c$ is a closed subspace of $l^\infty$ and hence is a Banach space.

6. Let $X=\{n^{-1}:n\geq1\}\cup\{0\}$. Show that $C(X)$ and the space of $c$ of Exercise 5 are isometrically isomorphic.

   (a) Show that if $1\leq p<\infty$ and $I$ is an infinite set, then $l^p(I)$ has a dense set of the same cardinality as $I$.

   (b) Show that if $1\leq p<\infty$, $l^p(I)$ and $l^p(J)$ are isometrically isomorphic if and only if $I$ and $J$ have the same cardinality.

7. If $l^\infty(I)$ and $l^\infty(J)$ are isometrically isomorphic, do $I$ and $J$ have the same cardinality?

8. Show that $l^\infty$ is not separable.

9. Complete the proof of Proposition 1.7.

10. Verify the statements in Example 1.10.

11. Verify the statements in Example 1.11.

12. Let $X$ be locally compact and let $X_\infty=X\cup\{\infty\}$ be the one-point compactification of $X$. Show that $C_0(X)$ and $\{f\in C(X_\infty):f(\infty)=0\}$, with the norm it inherits as a subspace of $C(X_\infty)$, are isometrically isomorphic Banach spaces.

13. Let $X$ be locally compact and define $C_c(X)$ to be the continuous functions $f:X\to\mathbb F$ such that $\operatorname{spt}f\equiv\operatorname{cl}\{x\in X:f(x)\neq0\}$ is compact ($\operatorname{spt}f$ is the *support* of $f$). Show that $C_c(X)$ is dense in $C_0(X)$.

14. If $W_p^n[0,1]$ is defined as in Example 1.11 and $f\in W_p^n[0,1]$, let $\lvert\!\lvert\!\lvert f\rvert\!\rvert\!\rvert\equiv\left[\int|f(x)|^p\,dx\right]^{1/p}+\left[\int|f^{(n)}(x)|^p\,dx\right]^{1/p}$. Show that $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert$ is equivalent to the norm defined on $W_p^n[0,1]$.

15. Let $\mathcal X$ be a normed space and let $\widehat{\mathcal X}$ be its completion as a metric space. Show that $\widehat{\mathcal X}$ is a Banach space.

16. Show that the norm on $C([0,1])=C_b([0,1])$ does not come from an inner product by showing that it does not satisfy the parallelogram law.

## §2. Linear Operators on Normed Spaces

This section gathers together a few pertinent facts and examples concerning linear operators on normed spaces. A fuller study of operators on Banach spaces will be pursued later.



<a id="pdf-page-83"></a>
The proof of the first result is similar to that of Proposition I.3.1 and is left to the reader. [Also see (II.1.1).] $\mathcal{B}(\mathcal{X},\mathcal{Y})=$ all continuous linear transformations $A:\mathcal{X}\to\mathcal{Y}$.

**2.1. Proposition.** *If $\mathcal{X}$ and $\mathcal{Y}$ are normed spaces and $A:\mathcal{X}\to\mathcal{Y}$ is a linear transformation, the following statements are equivalent.*

(a) $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$.

(b) $A$ is continuous at $0$.

(c) $A$ is continuous at some point.

(d) There is a positive constant $c$ such that $\|Ax\|\leq c\|x\|$ for all $x$ in $\mathcal{X}$.

*If $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$ and*

$$
\|A\|=\sup\{\|Ax\|:\|x\|\leq 1\},
$$

*then*

$$
\begin{aligned}
\|A\|&=\sup\{\|Ax\|:\|x\|=1\}\\
&=\sup\{\|Ax\|/\|x\|:x\ne 0\}\\
&=\inf\{c>0:\|Ax\|\leq c\|x\|\text{ for }x\text{ in }\mathcal{X}\}.
\end{aligned}
$$

$\|A\|$ is called the *norm* of $A$ and $\mathcal{B}(\mathcal{X},\mathcal{Y})$ becomes a normed space if addition and scalar multiplication are defined pointwise. $\mathcal{B}(\mathcal{X},\mathcal{Y})$ is a Banach space if $\mathcal{Y}$ is a Banach space (Exercise 1). A continuous linear operator is also called a *bounded linear operator*.

The following examples are reminiscent of those that were given in Section II.1.

**2.2. Example.** If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\phi\in L^\infty(X,\Omega,\mu)$, define $M_\phi:L^p(X,\Omega,\mu)\to L^p(X,\Omega,\mu)$, $1\leq p\leq\infty$, by $M_\phi f=\phi f$ for all $f$ in $L^p(X,\Omega,\mu)$. Then $M_\phi\in\mathcal{B}(L^p(X,\Omega,\mu))$ and $\|M_\phi\|=\|\phi\|_\infty$.

**2.3. Example.** If $(X,\Omega,\mu)$, $k$, $c_1$, and $c_2$ are as in Example II.1.6 and $1\leq p\leq\infty$, then $K:L^p(\mu)\to L^p(\mu)$, defined by

$$
(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)
$$

for all $f$ in $L^p(\mu)$ and $x$ in $X$, is a bounded operator on $L^p(\mu)$ and $\|K\|\leq c_1^{1/q}c_2^{1/p}$, where $1/p+1/q=1$.

**2.4. Example.** If $X$ and $Y$ are compact spaces and $\tau:Y\to X$ is a continuous map, define $A:C(X)\to C(Y)$ by $(Af)(y)=f(\tau(y))$. Then $A\in\mathcal{B}(C(X),C(Y))$ and $\|A\|=1$.

## EXERCISES

1. Show that for $\mathcal{B}(\mathcal{X},\mathbb{F})\ne(0)$, $\mathcal{B}(\mathcal{X},\mathcal{Y})$ is a Banach space if and only if $\mathcal{Y}$ is a Banach space.



<a id="pdf-page-84"></a>
2. Let $\mathcal X$ be a normed space, let $\mathcal Y$ be a Banach space, and let $\widehat{\mathcal X}$ be the completion of $\mathcal X$. Show that if $\rho:\mathcal B(\widehat{\mathcal X},\mathcal Y)\to\mathcal B(\mathcal X,\mathcal Y)$ is defined by $\rho(A)=A|_{\mathcal X}$, then $\rho$ is an isometric isomorphism.

3. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, $\phi:X\to\mathbb F$ is an $\Omega$-measurable function, $1\leq p\leq\infty$, and $\phi f\in L^p(\mu)$ whenever $f\in L^p(\mu)$, then show that $\phi\in L^\infty(\mu)$.

4. Verify the statements in Example 2.2.

5. Verify the statements in Example 2.3.

6. Verify the statements in Example 2.4.

7. Let $A$ and $\tau$ be as in Example 2.4. (a) Give necessary and sufficient conditions on $\tau$ that $A$ be injective. (b) Give such a condition that $A$ be surjective. (c) Give such a condition that $A$ be an isometry. (d) If $X=Y$, show that $A^2=A$ if and only if $\tau$ is a retraction.

8. (Wilansky [1951]) Assume that $A:\mathcal X\to\mathcal Y$ is an additive mapping (that is, $A(x_1+x_2)=A(x_1)+A(x_2)$ for all $x_1$ and $x_2$ in $\mathcal X$) and show that conditions (b), (c), and (d) in Proposition 2.1 are equivalent to the continuity of $A$.

## §3. Finite Dimensional Normed Spaces

In functional analysis it is always good to see what significance a concept has for finite dimensional spaces.

**3.1. Theorem.** *If $\mathcal X$ is a finite dimensional vector space over $\mathbb F$, then any two norms on $\mathcal X$ are equivalent.*

**Proof.** Let $\{e_1,\ldots,e_d\}$ be a Hamel basis for $\mathcal X$. For $x=\sum_{j=1}^{d}x_je_j$, define $\|x\|_\infty\equiv\max\{|x_j|:1\leq j\leq d\}$. It is left to the reader to verify that $\|\cdot\|_\infty$ is a norm. Let $\|\cdot\|$ be any norm on $\mathcal X$. It will be shown that $\|\cdot\|$ and $\|\cdot\|_\infty$ are equivalent.

If $x=\sum_j x_je_j$, then $\|x\|\leq\sum_j|x_j|\|e_j\|\leq C\|x\|_\infty$, when $C=\sum_j\|e_j\|$. To show the other inequality, let $\mathcal T$ be the topology defined on $\mathcal X$ by $\|\cdot\|_\infty$ and let $\mathcal U$ be the topology defined on $\mathcal X$ by $\|\cdot\|$. Put $B=\{x\in\mathcal X:\|x\|_\infty\leq1\}$. The first part of the proof implies $\mathcal T\supseteq\mathcal U$. Since $B$ is $\mathcal T$-compact and $\mathcal T\supseteq\mathcal U$, $B$ is $\mathcal U$-compact and the relativizations of the two topologies to $B$ agree. Let $A=\{x\in\mathcal X:\|x\|_\infty<1\}$. Since $A$ is $\mathcal T$-open, it is open in $(B,\mathcal U)$. Hence there is a set $U$ in $\mathcal U$ such that $U\cap B=A$. Thus $0\in U$ and there is an $r>0$ such that $\{x\in\mathcal X:\|x\|<r\}\subseteq U$. Hence

$$
\|x\|<r\text{ and }\|x\|_\infty\leq1\text{ implies }\|x\|_\infty<1. \tag{3.2}
$$

**Claim.** $\|x\|<r$ implies $\|x\|_\infty<1$.

Let $\|x\|<r$ and put $x=\sum_jx_je_j$, $\alpha=\|x\|_\infty$. So $\|x/\alpha\|_\infty=1$ and $x/\alpha\in B$. If



<a id="pdf-page-85"></a>
$\alpha\geqslant 1$, then $\|x/\alpha\|<r/\alpha\leqslant r$, and hence $\|x/\alpha\|_{\infty}<1$ by (3.2), a contradiction. Thus $\|x\|_{\infty}=\alpha<1$ and the claim is established.

By Lemma 1.4, $\|x\|_{\infty}\leqslant r^{-1}\|x\|$ for all $x$ and so the proof is complete. $\blacksquare$

**3.3. Proposition.** *If $\mathcal X$ is a normed space and $\mathcal M$ is a finite dimensional linear manifold in $\mathcal X$, then $\mathcal M$ is closed.*

**Proof.** Using a Hamel basis $\{e_1,\ldots,e_n\}$ for $\mathcal M$, define a norm $\|\cdot\|_{\infty}$ on $\mathcal M$ as in the proof of Theorem 3.1. It is easy to see that $\mathcal M$ is complete with respect to this new norm. But then Theorem 3.1 implies that $\mathcal M$ is complete with respect to its original norm and hence must be a closed subspace of $\mathcal X$. $\blacksquare$

**3.4. Proposition.** *Let $\mathcal X$ be a finite dimensional normed space and let $\mathcal Y$ be any normed space. If $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is continuous.*

**Proof.** Since all norms on $\mathcal X$ are equivalent and $T:\mathcal X\to\mathcal Y$ is continuous with respect to one norm on $\mathcal X$ precisely when it is continuous with respect to any equivalent norm, we may assume that $\|\sum_{j=1}^{d}\xi_j e_j\|=\max\{|\xi_j|:1\leqslant j\leqslant d\}$, where $\{e_j\}$ is a Hamel basis for $\mathcal X$. Thus, for $x=\sum_j\xi_j e_j$, $\|Tx\|=\|\sum_j\xi_jTe_j\|\leqslant\sum_j|\xi_j|\|Te_j\|\leqslant C\|x\|$, where $C=\sum_j\|Te_j\|$. By (2.1), $T$ is continuous. $\blacksquare$

**Exercises**

1. Show that if $\mathcal X$ is a locally compact normed space, then $\mathcal X$ is finite dimensional. (This same result, due to F Riesz, is valid in the more general topological vector spaces—see IV.1.1 for the definition. For a nice proof of this look at Pitcairn [1966].)

2. Show that $\|\cdot\|_{\infty}$ defined in the proof of Theorem 3.1 is a norm.

## §4. Quotients and Products of Normed Spaces

Let $\mathcal X$ be a normed space, let $\mathcal M$ be a linear manifold in $\mathcal X$, and let $Q:\mathcal X\to\mathcal X/\mathcal M$ be the natural map $Qx=x+\mathcal M$. We want to make $\mathcal X/\mathcal M$ into a normed space, so define

$$
\|x+\mathcal M\|=\inf\{\|x+y\|:y\in\mathcal M\}. \tag{4.1}
$$

Note that because $\mathcal M$ is a linear space, $\|x+\mathcal M\|=\inf\{\|x-y\|:y\in\mathcal M\}=\operatorname{dist}(x,\mathcal M)$, the distance from $x$ to $\mathcal M$. It is left to the reader to show that (4.1) defines a seminorm on $\mathcal X/\mathcal M$. But if $\mathcal M$ is not closed in $\mathcal X$, (4.1) cannot define a norm. (Why?) If, however, $\mathcal M$ is closed, then (4.1) does define a norm.

**4.2. Theorem.** *If $\mathcal M\leqslant\mathcal X$ and $\|x+\mathcal M\|$ is defined as in (4.1), then $\|\cdot\|$ is a norm on $\mathcal X/\mathcal M$. Also:*

(a) *$\|Q(x)\|\leqslant\|x\|$ for all $x$ in $\mathcal X$ and hence $Q$ is continuous.*

(b) *If $\mathcal X$ is a Banach space, then so is $\mathcal X/\mathcal M$.*



<a id="pdf-page-86"></a>
(c) A subset $W$ of $\mathcal{X}/\mathcal{M}$ is open relative to the norm if and only if $Q^{-1}(W)$ is open in $\mathcal{X}$.

(d) If $U$ is open in $\mathcal{X}$, then $Q(U)$ is open in $\mathcal{X}/\mathcal{M}$.

**Proof.** It is left as an exercise to show that (4.1) defines a norm on $\mathcal{X}/\mathcal{M}$. To show (a), $\|Q(x)\|=\|x+\mathcal{M}\|\leq\|x\|$ since $0\in\mathcal{M}$; $Q$ is therefore continuous by (2.1).

(b) Let $\{x_n+\mathcal{M}\}$ be a Cauchy sequence in $\mathcal{X}/\mathcal{M}$. There is a subsequence $\{x_{n_k}+\mathcal{M}\}$ such that

$$
\|(x_{n_k}+\mathcal{M})-(x_{n_{k+1}}+\mathcal{M})\|
=\|x_{n_k}-x_{n_{k+1}}+\mathcal{M}\|<2^{-k}.
$$

Let $y_1=0$. Choose $y_2$ in $\mathcal{M}$ such that

$$
\|x_{n_1}-x_{n_2}+y_2\|
\leq\|x_{n_1}-x_{n_2}+\mathcal{M}\|+2^{-1}
<2\cdot2^{-1}.
$$

Choose $y_3$ in $\mathcal{M}$ such that

$$
\|(x_{n_2}+y_2)-(x_{n_3}+y_3)\|
\leq\|x_{n_2}-x_{n_3}+\mathcal{M}\|+2^{-2}
<2\cdot2^{-2}.
$$

Continuing, there is a sequence $\{y_k\}$ in $\mathcal{M}$ such that

$$
\|(x_{n_k}+y_k)-(x_{n_{k+1}}+y_{k+1})\|<2\cdot2^{-k}.
$$

Thus $\{x_{n_k}+y_k\}$ is a Cauchy sequence in $\mathcal{X}$ (Why?). Since $\mathcal{X}$ is complete, there is an $x_0$ in $\mathcal{X}$ such that $x_{n_k}+y_k\to x_0$ in $\mathcal{X}$. By (a), $x_{n_k}+\mathcal{M}=Q(x_{n_k}+y_k)\to Qx_0=x_0+\mathcal{M}$. Since $\{x_n+\mathcal{M}\}$ is a Cauchy sequence, $x_n+\mathcal{M}\to x_0+\mathcal{M}$ and $\mathcal{X}/\mathcal{M}$ is complete (Exercise 3).

(c) If $W$ is open in $\mathcal{X}/\mathcal{M}$, then $Q^{-1}(W)$ is open in $\mathcal{X}$ because $Q$ is continuous. Now assume that $W\subseteq\mathcal{X}/\mathcal{M}$ and $Q^{-1}(W)$ is open in $\mathcal{X}$. Let $r>0$ and put $B_r=\{x\in\mathcal{X}:\|x\|<r\}$. It will be shown that $Q(B_r)=\{x+\mathcal{M}:\|x+\mathcal{M}\|<r\}$. In fact, if $\|x\|<r$, then $\|x+\mathcal{M}\|\leq\|x\|<r$. On the other hand, if $\|x+\mathcal{M}\|<r$, then there is a $y$ in $\mathcal{M}$ such that $\|x+y\|<r$. Thus $x+\mathcal{M}=Q(x+y)\in Q(B_r)$. If $x_0+\mathcal{M}\in W$, then $x_0\in Q^{-1}(W)$. Since $Q^{-1}(W)$ is open, there is an $r>0$ such that $x_0+B_r=\{x:\|x-x_0\|<r\}\subseteq Q^{-1}(W)$. The preceding argument now implies that $W=QQ^{-1}(W)\supseteq Q(x_0+B_r)=\{x+\mathcal{M}:\|x-x_0+\mathcal{M}\|<r\}$. Hence $W$ is open.

(d) If $U$ is open in $\mathcal{X}$, then $Q^{-1}(Q(U))=U+\mathcal{M}\equiv\{u+y:u\in U,\ y\in\mathcal{M}\}=\bigcup\{U+y:y\in\mathcal{M}\}$. Each $U+y$ is open, so $Q^{-1}(Q(U))$ is open in $\mathcal{X}$. By (c), $Q(U)$ is open in $\mathcal{X}/\mathcal{M}$. $\blacksquare$

Because $Q$ is an open map [part (d)], it does not follow that $Q$ is a closed map (Exercise 4).

**4.3. Proposition.** *If $\mathcal{X}$ is a normed space, $\mathcal{M}\leq\mathcal{X}$, and $\mathcal{N}$ is a finite dimensional subspace of $\mathcal{X}$, then $\mathcal{M}+\mathcal{N}$ is a closed subspace of $\mathcal{X}$.*

**Proof.** Consider $\mathcal{X}/\mathcal{M}$ and the quotient map $Q:\mathcal{X}\to\mathcal{X}/\mathcal{M}$. Since $\dim Q(\mathcal{N})\leq\dim\mathcal{N}<\infty$, $Q(\mathcal{N})$ is closed in $\mathcal{X}/\mathcal{M}$. Since $Q$ is continuous $Q^{-1}(Q(\mathcal{N}))$ is closed in $\mathcal{X}$; but $Q^{-1}(Q(\mathcal{N}))=\mathcal{M}+\mathcal{N}$. $\blacksquare$



<a id="pdf-page-87"></a>
Now for the product or direct sum of normed spaces. Here there is a difficulty because, unlike Hilbert space, there is no canonical way to proceed. Suppose $\{\mathcal X_i:i\in I\}$ is a collection of normed spaces. Then $\prod\{\mathcal X_i:i\in I\}$ is a vector space if the linear operations are defined coordinatewise. The idea is to put a norm on a linear subspace of this product.

Let $\|\cdot\|$ denote the norm on each $\mathcal X_i$. For $1\leq p<\infty$, define

$$
\bigoplus_p\mathcal X_i\equiv
\left\{x\in\prod_i\mathcal X_i:\|x\|\equiv
\left[\sum_i\|x(i)\|^p\right]^{1/p}<\infty\right\}.
$$

Define

$$
\bigoplus_\infty\mathcal X_i\equiv
\left\{x\in\prod_i\mathcal X_i:\|x\|\equiv
\sup_i\|x(i)\|<\infty\right\}.
$$

If $\{\mathcal X_1,\mathcal X_2,\ldots\}$ is a sequence of normed spaces, define

$$
\bigoplus_0\mathcal X_n\equiv
\left\{x\in\prod_{n=1}^{\infty}\mathcal X_n:\|x(n)\|\to0\right\};
$$

give $\bigoplus_0\mathcal X_n$ the norm it has as a subspace of $\bigoplus_\infty\mathcal X_n$.

The proof of the next proposition is left as an exercise.

**4.4. Proposition.** Let $\{\mathcal X_i:i\in I\}$ be a collection of normed spaces and let $\mathcal X=\bigoplus_p\mathcal X_i$, $1\leq p\leq\infty$.

(a) $\mathcal X$ is a normed space and the projection $P_i:\mathcal X\to\mathcal X_i$ is a continuous linear map with $\|P_i(x)\|\leq\|x\|$ for each $x$ in $\mathcal X$.

(b) $\mathcal X$ is a Banach space if and only if each $\mathcal X_i$ is a Banach space.

(c) Each projection $P_i$ is an open map of $\mathcal X$ onto $\mathcal X_i$.

A similar result holds for $\bigoplus_0\mathcal X_n$, but the formulation and proof of this is left to the reader.

## EXERCISES

1. Show that if $\mathcal M\leq\mathcal X$, then (4.1) defines a norm on $\mathcal X/\mathcal M$.

2. Prove that $\mathcal X$ is a Banach space if and only if whenever $\{x_n\}$ is a sequence in $\mathcal X$ such that $\sum\|x_n\|<\infty$, then $\sum_{n=1}^{\infty}x_n$ converges in $\mathcal X$.

3. Show that if $(X,d)$ is a metric space and $\{x_n\}$ is a Cauchy sequence such that there is a subsequence $\{x_{n_k}\}$ that converges to $x_0$, then $x_n\to x_0$.

4. Find a Banach space $\mathcal X$ and a closed subspace $\mathcal M$ such that the natural map $Q:\mathcal X\to\mathcal X/\mathcal M$ is not a closed map. Can the natural map ever be a closed map?

5. Prove the converse of (4.2b): If $\mathcal X$ is a normed space, $\mathcal M\leq\mathcal H$, and both $\mathcal M$ and $\mathcal X/\mathcal M$ are complete, then $\mathcal X$ is complete. (This is an example of what is called a “two-out-of-three” result. If any two of $\mathcal X$, $\mathcal M$, and $\mathcal X/\mathcal M$ are complete, so is the third.)

6. Let $\mathcal M=\{x\in\ell^p:x(2n)=0\text{ for all }n\}$, $1\leq p\leq\infty$. Show that $\ell^p/\mathcal M$ is isometrically isomorphic to $\ell^p$.



<a id="pdf-page-88"></a>
7. Let $X$ be a normal locally compact space and $F$ a closed subset of $X$. If $\mathcal M\equiv\{f\in C_0(X):f(x)=0\text{ for all }x\text{ in }F\}$, then $C_0(X)/\mathcal M$ is isometrically isomorphic to $C_0(F)$.

8. Prove Proposition 4.4.

9. Formulate and prove a version of Proposition 4.4 for $\bigoplus_0\mathcal X_n$.

10. If $\{\mathcal X_1,\ldots,\mathcal X_n\}$ is a finite collection of normed spaces and $1\leq p\leq\infty$, show that the norms on $\bigoplus_p\mathcal X_k$ are all equivalent.

11. Here is an abstraction of Proposition 4.4. Suppose $\{\mathcal X_i:i\in I\}$ is a collection of normed spaces and $Y$ is a normed space contained in $\mathbb F^I$. Define $\mathcal X\equiv\{x\in\prod_i\mathcal X_i:\text{ there is a }y\text{ in }Y\text{ with }\|x(i)\|\leq y(i)\text{ for all }i\}$. If $x\in\mathcal X$, define $\|x\|\equiv\inf\{\|y\|:\|x(i)\|\leq y(i)\text{ for all }i\}$. Then $(\mathcal X,\|\cdot\|)$ is a normed space. Give necessary and sufficient conditions on $Y$ that each of the parts of (4.4) be valid for $\mathcal X$.

12. Let $\mathcal X$ be a normed space and $\mathcal M\leq\mathcal X$. (a) If $\mathcal X$ is separable, so is $\mathcal X/\mathcal M$. (b) If $\mathcal X/\mathcal M$ and $\mathcal M$ are separable, then $\mathcal X$ is separable. (c) Give an example such that $\mathcal X/\mathcal M$ is separable but $\mathcal X$ is not.

13. Let $\{\mathcal X_i:i\in I\}$ be a collection of non-zero normed spaces. For $1\leq p<\infty$, put $\mathcal X=\bigoplus_p\mathcal X_i$. Show that $\mathcal X$ is separable if and only if $I$ is countable and each $\mathcal X_i$ is separable. Show that $\bigoplus_\infty\mathcal X_i$ is separable if and only if $I$ is finite and each $\mathcal X_i$ is separable.

14. Show that $\bigoplus_0\mathcal X_n$ is separable if and only if each $\mathcal X_n$ is separable.

15. Let $J\subseteq I$, and $\mathcal X\equiv\bigoplus_p\{\mathcal X_i:i\in I\}$, $\mathcal M\equiv\{x\in\mathcal X:x(j)=0\text{ for }j\text{ in }J\}$. Show that $\mathcal X/\mathcal M$ is isometrically isomorphic to $\bigoplus_p\{\mathcal X_j:j\in J\}$.

16. Let $\mathcal H$ be a Hilbert space and suppose $\mathcal M\leq\mathcal H$. Show that if $Q:\mathcal H\to\mathcal H/\mathcal M$ is the natural map, then $Q:\mathcal M^\perp\to\mathcal H/\mathcal M$ is an isometric isomorphism.

## §5. Linear Functionals

Let $\mathcal X$ be a vector space over $\mathbb F$. A *hyperplane* in $\mathcal X$ is a linear manifold $\mathcal M$ in $\mathcal X$ such that $\dim(\mathcal X/\mathcal M)=1$. If $f:\mathcal X\to\mathbb F$ is a linear functional and $f\ne0$, then $\ker f$ is a hyperplane. In fact, $f$ induces an isomorphism between $\mathcal X/\ker f$ and $\mathbb F$. Conversely, if $\mathcal M$ is a hyperplane, let $Q:\mathcal X\to\mathcal X/\mathcal M$ be the natural map and let $T:\mathcal X/\mathcal M\to\mathbb F$ be an isomorphism. Then $f\equiv T\circ Q$ is a linear functional on $\mathcal X$ and $\ker f=\mathcal M$.

Suppose now that $f$ and $g$ are linear functionals on $\mathcal X$ such that $\ker f=\ker g$. Let $x_0\in\mathcal X$ such that $f(x_0)=1$; so $g(x_0)\ne0$. If $x\in\mathcal X$ and $\alpha=f(x)$, then $x-\alpha x_0\in\ker f=\ker g$. So $0=g(x)-\alpha g(x_0)$, or $g(x)=(g(x_0))\alpha=(g(x_0))f(x)$. Thus $g=\beta f$ for a scalar $\beta$. This is summarized as follows.

**5.1. Proposition.** *A linear manifold in $\mathcal X$ is a hyperplane if and only if it is the kernel of a non-zero linear functional. Two linear functionals have the same kernel if and only if one is a non-zero multiple of the other.*



<a id="pdf-page-89"></a>
Hyperplanes in a normed space fall into one of two categories.

**5.2. Proposition.** *If $\mathcal X$ is a normed space and $\mathcal M$ is a hyperplane in $\mathcal X$, then either $\mathcal M$ is closed or $\mathcal M$ is dense.*

**Proof.** Consider $\operatorname{cl}\mathcal M$, the closure of $\mathcal M$. By Proposition 1.3, $\operatorname{cl}\mathcal M$ is a linear manifold in $\mathcal X$. Since $\mathcal M\subseteq\operatorname{cl}\mathcal M$ and $\dim\mathcal X/\mathcal M=1$, either $\operatorname{cl}\mathcal M=\mathcal M$ or $\operatorname{cl}\mathcal M=\mathcal X$. $\blacksquare$

If $\mathcal X=c_0$ and $f:\mathcal X\to\mathbf F$ is defined by $f(\alpha_1,\alpha_2,\ldots)=\alpha_1$, then $\ker f=\{(\alpha_n)\in c_0:\alpha_1=0\}$ is closed in $c_0$. To get an example of a dense hyperplane, let $\mathcal X=c_0$ and let $e_n$ be the element of $c_0$ such that $e_n(k)=0$ if $k\ne n$ and $e_n(n)=1$. (It is best to think of $c_0$ as a collection of functions on $\mathbb N$.) Let $x_0(n)=1/n$ for all $n$; so $x_0\in c_0$ and $\{x_0,e_1,e_2,\ldots\}$ is a linearly independent set in $c_0$. Let $\mathcal B$ = a Hamel basis in $c_0$ which contains $\{x_0,e_1,e_2,\ldots\}$. Put $\mathcal B=\{x_0,e_1,e_2,\ldots\}\cup\{b_i:i\in I\}$, $b_i\ne x_0$ or $e_n$ for any $i$ or $n$. Define $f:c_0\to\mathbf F$ by $f(\alpha_0x_0+\sum_{n=1}^{\infty}\alpha_ne_n+\sum_i\beta_ib_i)=\alpha_0$. (Remember that in the preceding expression at most a finite number of the $\alpha_n$ and $\beta_i$ are not zero.) Since $e_n\in\ker f$ for all $n\geq1$, $\ker f$ is dense but clearly $\ker f\ne c_0$.

The dichotomy that exists for hyperplanes should be reflected in a dichotomy for linear functionals.

**5.3. Theorem.** *If $\mathcal X$ is a normed space and $f:\mathcal X\to\mathbf F$ is a linear functional, then $f$ is continuous if and only if $\ker f$ is closed.*

**Proof.** If $f$ is continuous, $\ker f=f^{-1}(\{0\})$ and so $\ker f$ must be closed. Assume now that $\ker f$ is closed and let $Q:\mathcal X\to\mathcal X/\ker f$ be the natural map. By (4.2), $Q$ is continuous. Let $T:\mathcal X/\ker f\to\mathbf F$ be an isomorphism; by (3.4), $T$ is continuous. Thus, if $g=T\circ Q:\mathcal X\to\mathbf F$, $g$ is continuous and $\ker f=\ker g$. Hence (5.1) $f=\alpha g$ for some $\alpha$ in $\mathbf F$ and so $f$ is continuous. $\blacksquare$

If $f:\mathcal X\to\mathbf F$ is a linear functional, then $f$ is a linear transformation and so Proposition 2.1 applies. Continuous linear functionals are also called *bounded linear functionals* and

$$
\|f\|\equiv\sup\{|f(x)|:\|x\|\leq1\}.
$$

The other formulas for $\|f\|$ given in (2.1) are also valid here. Let $\mathcal X^*\equiv$ the collection of all bounded linear functionals on $\mathcal X$. If $f,g\in\mathcal X^*$ and $\alpha\in\mathbf F$, define $(\alpha f+g)(x)=\alpha f(x)+g(x)$; $\mathcal X^*$ is called the *dual space* of $\mathcal X$. Note that $\mathcal X^*=\mathcal B(\mathcal X,\mathbf F)$.

**5.4. Proposition.** *If $\mathcal X$ is a normed space, $\mathcal X^*$ is a Banach space.*

**Proof.** It is left as an exercise for the reader to show that $\mathcal X^*$ is a normed space. To show that $\mathcal X^*$ is complete, let $B=\{x\in\mathcal X:\|x\|\leq1\}$. If $f\in\mathcal X^*$, define $\rho(f):B\to\mathbf F$ by $\rho(f)(x)=f(x)$; that is, $\rho(f)$ is the restriction of $f$ to $B$. Note that $\rho:\mathcal X^*\to C_b(B)$ is a linear isometry. Thus to show that $\mathcal X^*$ is complete,



<a id="pdf-page-90"></a>
it suffices, since $C_b(B)$ is complete (1.6), to show that $\rho(\mathcal X^*)$ is closed. Let $\{f_n\}\subseteq\mathcal X^*$ and suppose $g\in C_b(B)$ such that $\|\rho(f_n)-g\|\to0$ as $n\to\infty$. Let $x\in\mathcal X$. If $\alpha,\beta\in\mathbb F$, $\alpha,\beta\ne0$, such that $\alpha x,\beta x\in B$, then $\alpha^{-1}g(\alpha x)=\lim\alpha^{-1}f_n(\alpha x)=\lim\beta^{-1}f_n(\beta x)=\beta^{-1}g(\beta x)$. Define $f:\mathcal X\to\mathbb F$ by letting $f(x)=\alpha^{-1}g(\alpha x)$ for any $\alpha\ne0$ such that $\alpha x\in B$. It is left as an exercise for the reader to show that $f\in\mathcal X^*$ and $\rho(f)=g$. $\blacksquare$

Compare the preceding result with Exercise 2.1.

It should be emphasized that it is not assumed in the preceding proposition that $\mathcal X$ is complete. In fact, if $\mathcal X$ is a normed space and $\widehat{\mathcal X}$ is its completion (Exercise 1.16), then $\mathcal X^*$ and $\widehat{\mathcal X}^{\,*}$ are isometrically isomorphic (Exercise 2.2).

**5.5. Theorem.** *Let $(X,\Omega,\mu)$ be a measure space and let $1<p<\infty$. If $1/p+1/q=1$ and $g\in L^q(X,\Omega,\mu)$, define $F_g:L^p(\mu)\to\mathbb F$ by*

$$
F_g(f)=\int fg\,d\mu.
$$

*Then $F_g\in L^p(\mu)^*$ and the map $g\mapsto F_g$ defines an isometric isomorphism of $L^q(\mu)$ onto $L^p(\mu)^*$.*

Since this theorem is often proved in courses in measure and integration, the proof of this result, as well as the next two, is contained in the Appendix. See Appendix B for the proofs of (5.5) and (5.6).

**5.6. Theorem.** *If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $g\in L^\infty(X,\Omega,\mu)$, define $F_g:L^1(\mu)\to\mathbb F$ by*

$$
F_g(f)=\int fg\,d\mu.
$$

*Then $F_g\in L^1(\mu)^*$ and the map $g\mapsto F_g$ defines an isometric isomorphism of $L^\infty(\mu)$ onto $L^1(\mu)^*$.*

Note that when $p=2$ in Theorem 5.5, there is a little difference between (5.5) and (I.3.5) owing to the absence of a complex conjugate in (5.5). Also, note that (5.6) is false if the measure space is not assumed to be $\sigma$-finite (Exercise 3).

If $X$ is a locally compact space, $M(X)$ denotes the space of all $\mathbb F$-valued regular Borel measures on $X$ with the total variation norm. See Appendix C for the definitions as well as the proof of the next theorem.

**5.7. Riesz Representation Theorem.** *If $X$ is a locally compact space and $\mu\in M(X)$, define $F_\mu:C_0(X)\to\mathbb F$ by*

$$
F_\mu(f)=\int f\,d\mu.
$$



<a id="pdf-page-91"></a>
76  III. Banach Spaces

*Then $F_\mu\in C_0(X)^*$ and the map $\mu\to F_\mu$ is an isometric isomorphism of $M(X)$ onto $C_0(X)^*$.*

There are special cases of these theorems that deserve to be pointed out.

**5.8. Example.** The dual of $c_0$ is isometrically isomorphic to $l^1$. In fact, $c_0=C_0(\mathbb N)$, if $\mathbb N$ is given the discrete topology, and $l^1=M(\mathbb N)$.

**5.9. Example.** The dual of $l^1$ is isometrically isomorphic to $l^\infty$. In fact, $l^1=L^1(\mathbb N,2^{\mathbb N},\mu)$, where $\mu(\Delta)=$ the number of points in $\Delta$. Also, $l^\infty=L^\infty(\mathbb N,2^{\mathbb N},\mu)$.

**5.10. Example.** If $1<p<\infty$, the dual of $l^p$ is $l^q$, where $1=1/p+1/q$.

What is the dual of $L^\infty(X,\Omega,\mu)$? There are two possible representations. One is to identify $L^\infty(X,\Omega,\mu)^*$ with the space of finitely additive measures defined on $\Omega$ that are “absolutely continuous” with respect to $\mu$ and have finite total variation (see Dunford and Schwartz [1958], p. 296). Another representation is to obtain a compact space $Z$ such that $L^\infty(X,\Omega,\mu)$ is isometrically isomorphic to $C(Z)$ and then use the Riesz Representation Theorem. This will be done later in this book (VIII.2.1).

What is the dual of $M(X)$? For this, define $L^\infty(M(X))$ as the set of all $F$ in $\prod\{L^\infty(\mu):\mu\in M(X)\}$ such that if $\mu\ll\nu$, then $F(\mu)=F(\nu)$ a.e. $[\mu]$. This is an inverse limit of the spaces $L^\infty(\mu)$, $\mu$ in $M(X)$.

**5.11. Lemma.** *If $F\in L^\infty(M(X))$, then*

$$
\|F\|\equiv\sup_\mu\|F(\mu)\|_\infty<\infty.
$$

**Proof.** If $\|F\|=\infty$, then there is a sequence $\{\mu_n\}$ in $M(X)$ such that $\|F(\mu_n)\|_\infty\geq n$. Let $\mu=\sum_{n=1}^\infty 2^{-n}|\mu_n|/\|\mu_n\|$. Then $\mu_n\ll\mu$ for all $n$, so $F(\mu_n)=F(\mu)$ a.e. $[\mu_n]$ for each $n$. Hence $\|F(\mu)\|_\infty\geq\|F(\mu_n)\|_\infty\geq n$ for each $n$, a contradiction. ■

**5.12. Theorem.** *If $X$ is locally compact and $F\in L^\infty(M(X))$, define $\Phi_F:M(X)\to\mathbb F$ by*

$$
\Phi_F(\mu)=\int F(\mu)\,d\mu.
$$

*Then $\Phi_F\in M(X)^*$ and the map $F\mapsto\Phi_F$ is an isometric isomorphism of $L^\infty(M(X))$ onto $M(X)^*$.*

**Proof.** It is easy to see that $\Phi_F$ is linear. Also, $|\Phi_F(\mu)|\leq\int|F(\mu)|\,d|\mu|\leq\|F(\mu)\|_\infty\|\mu\|\leq\|F\|\|\mu\|$. Thus $\Phi_F\in M(X)^*$ and $\|\Phi_F\|\leq\|F\|$.

Now fix $\Phi$ in $M(X)^*$. If $\mu\in M(X)$ and $f\in L^1(|\mu|)$, then $\nu=f\mu\in M(X)$. (That is, $\nu(\Delta)=\int_\Delta f\,d\mu$ for every Borel set $\Delta$.) Also $\|\nu\|=\int|f|\,d|\mu|$. In fact, the



<a id="pdf-page-92"></a>
Radon–Nikodym Theorem can be interpreted as an identification (isometrically isomorphic) of $L^1(|\mu|)$ with $\{\eta\in M(X):\eta\ll|\mu|\}$. Thus $f\mapsto\Phi(f\mu)$ is a linear functional on $L^1(|\mu|)$ and $|\Phi(f\mu)|\leq\|\Phi\|\int|f|\,d|\mu|$. Hence there is an $F(\mu)$ in $L^\infty(|\mu|)$ such that $\Phi(f\mu)=\int fF(\mu)\,d\mu$ for every $f$ in $L^1(|\mu|)$ and $\|F(\mu)\|_\infty\leq\|\Phi\|$. (We have been a little nonchalant about using $\mu$ or $|\mu|$, but what was said is perfectly correct. Fill in the details.) In particular, taking $f=1$ gives $\Phi(\mu)=\int F(\mu)\,d\mu$. It must be shown that $F\in L^\infty(M(X))$; it then follows that $\Phi=\Phi_F$ and $\|\Phi_F\|\geq\|F\|_\infty$.

To show that $F\in L^\infty(M(X))$, let $\mu$ and $\nu$ be measures such that $\nu\ll\mu$. By the Radon–Nikodym Theorem, there is an $f$ in $L^1(|\mu|)$ such that $\nu=f\mu$. Hence if $g\in L^1(|\nu|)$, then $gf\in L^1(|\mu|)$ and $\int g\,d\nu=\int gf\,d\mu$. Thus,
$$
\int gF(\nu)\,d\nu
=\Phi(g\nu)
=\Phi(gf\mu)
=\int gfF(\mu)\,d\mu
=\int gF(\mu)\,d\nu.
$$
So $F(\nu)=F(\mu)$ a.e. $[\nu]$ and $F\in L^\infty(M(X))$. ■

## Exercises

1. Complete the proof of Proposition 5.4.

2. Show that $\mathcal{X}^*$ is a normed space.

3. Give an example of a measure space $(X,\Omega,\mu)$ that is not $\sigma$-finite for which the conclusion of Theorem 5.6 is false.

4. Let $\{\mathcal{X}_i:i\in I\}$ be a collection of normed spaces. If $1\leq p<\infty$, show that the dual space of $\bigoplus_p\mathcal{X}_i$ is isometrically isomorphic to $\bigoplus_q\mathcal{X}_i^*$, where $1/p+1/q=1$.

5. If $\mathcal{X}_1,\mathcal{X}_2,\ldots$ are normed spaces, show that $(\bigoplus_0\mathcal{X}_n)^*$ is isometrically isomorphic to $\bigoplus_1\mathcal{X}_n^*$.

6. Let $n\geq1$ and let $C^{(n)}[0,1]$ be defined as in Example 1.10. Show that
   $$
   \|f\|=\sum_{k=0}^{n-1}|f^{(k)}(0)|+\sup\{|f^{(n)}(x)|:0\leq x\leq1\}
   $$
   is an equivalent norm on $C^{(n)}[0,1]$. Show that $L\in(C^{(n)}[0,1])^*$ if and only if there are scalars $\alpha_0,\alpha_1,\ldots,\alpha_{n-1}$ and a measure $\mu$ on $[0,1]$ such that
   $$
   L(f)=\sum_{k=0}^{n-1}\alpha_k f^{(k)}(0)+\int f^{(n)}\,d\mu.
   $$
   If $C^{(n)}[0,1]$ is given this new norm, find a formula for $\|L\|$ in terms of $|\alpha_0|,|\alpha_1|,\ldots,|\alpha_{n-1}|$, and $\|\mu\|$?

7. Give $\mathcal{X}=C([0,1])$ the norm $\|f\|=\int|f(t)|\,dt$ and define $L:\mathcal{X}\to F$ by $L(f)=f(\tfrac12)$. Show directly (without using Theorem 5.6) that $L$ is not bounded. Now prove this as a consequence of (5.6).

## §6. The Hahn–Banach Theorem

The Hahn–Banach Theorem is one of the most important results in mathematics. It is used so often it is rightly considered as a cornerstone of functional analysis. It is one of those theorems that when it or one of its immediate consequences is used, it is used without quotation or reference and the reader is assumed to realize that it is being invoked.

**6.1. Definition.** If $\mathcal{X}$ is a vector space, a *sublinear functional* is a function



<a id="pdf-page-93"></a>
$q:\mathcal X\to\mathbb R$ such that

(a) $q(x+y)\leq q(x)+q(y)$ for all $x,y$ in $\mathcal X$;  
(b) $q(\alpha x)=\alpha q(x)$ for $x$ in $\mathcal X$ and $\alpha\geq 0$.

Note that every seminorm is a sublinear functional, but not conversely. In fact, it should be emphasized that a sublinear functional is allowed to assume negative values and that (b) in the definition only holds for $\alpha\geq 0$.

**6.2. The Hahn–Banach Theorem.** *Let $\mathcal X$ be a vector space over $\mathbb R$ and let $q$ be a sublinear functional on $\mathcal X$. If $\mathcal M$ is a linear manifold in $\mathcal X$ and $f:\mathcal M\to\mathbb R$ is a linear functional such that $f(x)\leq q(x)$ for all $x$ in $\mathcal M$, then there is a linear functional $F:\mathcal X\to\mathbb R$ such that $F|_{\mathcal M}=f$ and $F(x)\leq q(x)$ for all $x$ in $\mathcal X$.*

Note that the substance of the theorem is not that the extension exists but that an extension can be found that remains dominated by $q$. Just to find an extension, let $\{e_i\}$ be a Hamel basis for $\mathcal M$ and let $\{y_j\}$ be vectors in $\mathcal X$ such that $\{e_i\}\cup\{y_j\}$ is a Hamel basis for $\mathcal X$. Now define $F:\mathcal X\to\mathbb R$ by $F(\sum_i\alpha_i e_i+\sum_j\beta_j y_j)=\sum_i\alpha_i f(e_i)=f(\sum_i\alpha_i e_i)$. This extends $f$. If $\{\gamma_j\}$ is any collection of real numbers, then $F(\sum_i\alpha_i e_i+\sum_j\beta_j y_j)=f(\sum_i\alpha_i e_i)+\sum_j\beta_j\gamma_j$ is also an extension of $f$. Moreover, any extension of $f$ has this form. The difficulty is that we must find one of these extensions that is dominated by $q$.

Before proving the theorem, let’s see some of its immediate corollaries. The first is an extension of the theorem to complex spaces. For this a lemma is needed. Note that if $\mathcal X$ is a vector space over $\mathbb C$, it is also a vector space over $\mathbb R$. Also, if $f:\mathcal X\to\mathbb C$ is $\mathbb C$-linear, then $\operatorname{Re}f:\mathcal X\to\mathbb R$ is $\mathbb R$-linear. The following lemma is the converse of this.

**6.3. Lemma.** *Let $\mathcal X$ be a vector space over $\mathbb C$.*

(a) *If $f:\mathcal X\to\mathbb R$ is an $\mathbb R$-linear functional, then $\tilde f(x)=f(x)-if(ix)$ is a $\mathbb C$-linear functional and $f=\operatorname{Re}\tilde f$.*

(b) *If $g:\mathcal X\to\mathbb C$ is $\mathbb C$-linear, $f=\operatorname{Re}g$, and $\tilde f$ is defined as in (a), then $\tilde f=g$.*

(c) *If $p$ is a seminorm on $\mathcal X$ and $f$ and $\tilde f$ are as in (a), then $|f(x)|\leq p(x)$ for all $x$ if and only if $|\tilde f(x)|\leq p(x)$ for all $x$.*

(d) *If $\mathcal X$ is a normed space and $f$ and $\tilde f$ are as in (a), then $\|f\|=\|\tilde f\|$.*

**Proof.** The proofs of (a) and (b) are left as an exercise. To prove (c), suppose $|\tilde f(x)|\leq p(x)$. Then $f(x)=\operatorname{Re}\tilde f(x)\leq|\tilde f(x)|\leq p(x)$. Also, $-f(x)=\operatorname{Re}\tilde f(-x)\leq|\tilde f(-x)|\leq p(x)$. Hence $|f(x)|\leq p(x)$. Now assume that $|f(x)|\leq p(x)$. Choose $\theta$ such that $\tilde f(x)=e^{i\theta}|\tilde f(x)|$. Hence $|\tilde f(x)|=\tilde f(e^{-i\theta}x)=\operatorname{Re}\tilde f(e^{-i\theta}x)=f(e^{-i\theta}x)\leq p(e^{-i\theta}x)=p(x)$.

Part (d) is an easy application of (c). $\blacksquare$

**6.4. Corollary.** *Let $\mathcal X$ be a vector space, let $\mathcal M$ be a linear manifold in $\mathcal X$, and let $p:\mathcal X\to[0,\infty)$ be a seminorm. If $f:\mathcal M\to\mathbb F$ is a linear functional such that*



<a id="pdf-page-94"></a>
$|f(x)|\leqslant p(x)$ for all $x$ in $\mathcal M$, then there is a linear functional $F:\mathcal X\to\mathbb F$ such that $F|_{\mathcal M}=f$ and $|F(x)|\leqslant p(x)$ for all $x$ in $\mathcal X$.

**Proof.** *Case 1: $\mathbb F=\mathbb R$.* Note that $f(x)\leqslant |f(x)|\leqslant p(x)$ for $x$ in $\mathcal M$. By (6.2) there is an extension $F:\mathcal X\to\mathbb R$ of $f$ such that $F(x)\leqslant p(x)$ for all $x$. Hence $-F(x)=F(-x)\leqslant p(-x)=p(x)$. Thus $|F|\leqslant p$.

*Case 2: $\mathbb F=\mathbb C$.* Let $f_1=\operatorname{Re}f$. By (6.3c), $|f_1|\leqslant p$. By Case 1, there is an $\mathbb R$-linear functional $F_1:\mathcal X\to\mathbb R$ such that $F_1|_{\mathcal M}=f_1$ and $|F_1|\leqslant p$. Let $F(x)=F_1(x)-iF_1(ix)$ for all $x$ in $\mathcal X$. By (6.3c), $|F|\leqslant p$. Clearly, $F|_{\mathcal M}=f$. $\blacksquare$

**6.5. Corollary.** *If $\mathcal X$ is a normed space, $\mathcal M$ is a linear manifold in $\mathcal X$, and $f:\mathcal M\to\mathbb F$ is a bounded linear functional, then there is an $F$ in $\mathcal X^*$ such that $F|_{\mathcal M}=f$ and $\|F\|=\|f\|$.*

**Proof.** Use Corollary 6.4 with $p(x)=\|f\|\|x\|$. $\blacksquare$

**6.6. Corollary.** *If $\mathcal X$ is a normed space, $\{x_1,x_2,\ldots,x_d\}$ is a linearly independent subset of $\mathcal X$, and $\alpha_1,\alpha_2,\ldots,\alpha_d$ are arbitrary scalars, then there is an $f$ in $\mathcal X^*$ such that $f(x_j)=\alpha_j$ for $1\leqslant j\leqslant d$.*

**Proof.** Let $\mathcal M=$ the linear span of $x_1,\ldots,x_d$ and define $g:\mathcal M\to\mathbb F$ by $g(\sum_j\beta_jx_j)=\sum_j\beta_j\alpha_j$. So $g$ is linear. Since $\mathcal M$ is finite dimensional, $g$ is continuous. Let $f$ be a continuous extension of $g$ to $\mathcal X$. $\blacksquare$

**6.7. Corollary.** *If $\mathcal X$ is a normed space and $x\in\mathcal X$, then*

$$
\|x\|=\sup\{|f(x)|:f\in\mathcal X^*\text{ and }\|f\|\leqslant 1\}.
$$

*Moreover, this supremum is attained.*

**Proof.** Let $\alpha=\sup\{|f(x)|:f\in\mathcal X^*\text{ and }\|f\|\leqslant 1\}$. If $f\in\mathcal X^*$ and $\|f\|\leqslant 1$, then $|f(x)|\leqslant\|f\|\|x\|\leqslant\|x\|$; hence $\alpha\leqslant\|x\|$. Now let $\mathcal M=\{\beta x:\beta\in\mathbb F\}$, define $g:\mathcal M\to\mathbb F$ by $g(\beta x)=\beta\|x\|$. Then $g\in\mathcal M^*$ and $\|g\|=1$. By Corollary 6.5, there is an $f$ in $\mathcal X^*$ such that $\|f\|=1$ and $f(x)=g(x)=\|x\|$. $\blacksquare$

This introduces a certain symmetry in the definitions of the norms in $\mathcal X$ and $\mathcal X^*$ that will be explored later (§11).

**6.8. Corollary.** *If $\mathcal X$ is a normed space, $\mathcal M\leqslant\mathcal X$, $x_0\in\mathcal X\setminus\mathcal M$, and $d=\operatorname{dist}(x_0,\mathcal M)$, then there is an $f$ in $\mathcal X^*$ such that $f(x_0)=1$, $f(x)=0$ for all $x$ in $\mathcal M$, and $\|f\|=d^{-1}$.*

**Proof.** Let $Q:\mathcal X\to\mathcal X/\mathcal M$ be the natural map. Since $\|x_0+\mathcal M\|=d$, by the preceding corollary there is a $g$ in $(\mathcal X/\mathcal M)^*$ such that $g(x_0+\mathcal M)=d$ and $\|g\|=1$. Let $f=d^{-1}g\circ Q:\mathcal X\to\mathbb F$. Then $f$ is continuous, $f(x)=0$ for $x$ in $\mathcal M$, and $f(x_0)=1$. Also, $|f(x)|=d^{-1}|g(Q(x))|\leqslant d^{-1}\|Q(x)\|\leqslant d^{-1}\|x\|$; hence $\|f\|\leqslant d^{-1}$. On the other hand, $\|g\|=1$ so there is a sequence $\{x_n\}$ such



<a id="pdf-page-95"></a>
80　　　　　　　　　　　　　　　　　III. Banach Spaces

that $|g(x_n+\mathcal M)|\to 1$ and $\|x_n+\mathcal M\|<1$ for all $n$. Let $y_n\in\mathcal M$ such that $\|x_n+y_n\|<1$. Then $|f(x_n+y_n)|=d^{-1}|g(x_n+\mathcal M)|\to d^{-1}$, so $\|f\|=d^{-1}$. ■

To prove the Hahn–Banach Theorem, we first show that we can extend the functional to a space of one dimension more.

**6.9. Lemma.** *Suppose the hypothesis of (6.2) is satisfied and, in addition, $\dim\mathcal X/\mathcal M=1$. Then the conclusion of (6.2) is valid.*

**Proof.** Fix $x_0$ in $\mathcal X\setminus\mathcal M$; so $\mathcal X=\mathcal M\vee\{x_0\}=\{tx_0+y:t\in\mathbb R,\ y\in\mathcal M\}$. For the moment assume that the extension $F:\mathcal X\to\mathbb R$ of $f$ exists with $F\leq q$. Let’s see what $F$ must look like. Put $\alpha_0=F(x_0)$. If $t>0$ and $y_1\in\mathcal M$, then $F(tx_0+y_1)=t\alpha_0+f(y_1)\leq q(tx_0+y_1)$. Hence $\alpha_0\leq-t^{-1}f(y_1)+t^{-1}q(tx_0+y_1)=-f(y_1/t)+q(x_0+y_1/t)$ for every $y_1$ in $\mathcal M$. Since $y_1/t\in\mathcal M$, this gives that.

$$
\alpha_0\leq-f(y_1)+q(x_0+y_1)
\tag*{6.10}
$$

for all $y_1$ in $\mathcal M$. Also note that if $\alpha_0$ satisfies (6.10), then by reversing the preceding argument, it follows that $t\alpha_0+f(y_1)\leq q(tx_0+y_1)$ whenever $t\geq0$.

If $t\geq0$ and $y_2\in\mathcal M$ and if $F$ exists, then $F(-tx_0+y_2)=-t\alpha_0+f(y_2)\leq q(-tx_0+y_2)$. As above, this implies that

$$
\alpha_0\geq f(y_2)-q(-x_0+y_2)
\tag*{6.11}
$$

for all $y_2$ in $\mathcal M$. Moreover, (6.11) is sufficient that $-t\alpha_0+f(y_2)\leq q(-tx_0+y_2)$ for all $t\geq0$ and $y_2$ in $\mathcal M$.

Combining (6.10) and (6.11) we see that we must show that $\alpha_0$ can be chosen satisfying (6.10) and (6.11) simultaneously. Thus we must show that

$$
f(y_2)-q(-x_0+y_2)\leq-f(y_1)+q(x_0+y_1)
\tag*{6.12}
$$

for all $y_1,y_2$ in $\mathcal M$. But this means we want to show that $f(y_1+y_2)\leq q(x_0+y_1)+q(-x_0+y_2)$. But

$$
\begin{aligned}
f(y_1+y_2)&\leq q(y_1+y_2)=q((y_1+x_0)+(-x_0+y_2))\\
&\leq q(y_1+x_0)+q(-x_0+y_2),
\end{aligned}
$$

so (6.12) is satisfied. If $\alpha_0$ is chosen with $\sup\{f(y_2)-q(-x_0+y_2):y_2\in\mathcal M\}\leq\alpha_0\leq\inf\{-f(y_1)+q(x_0+y_1):y_1\in\mathcal M\}$ and $F(tx_0+y)\equiv t\alpha_0+f(y_1)$, $F$ satisfies the conclusion of (6.2). ■

**Proof of the Hahn–Banach Theorem.** Let $\mathcal S$ be the collection of all pairs $(\mathcal M_1,f_1)$, where $\mathcal M_1$ is a linear manifold in $\mathcal X$ such that $\mathcal M_1\supseteq\mathcal M$ and $f_1:\mathcal M_1\to\mathbb R$ is a linear functional with $f_1|_{\mathcal M}=f$ and $f_1\leq q$ on $\mathcal M_1$. If $(\mathcal M_1,f_1)$ and $(\mathcal M_2,f_2)\in\mathcal S$, define $(\mathcal M_1,f_1)\lesssim(\mathcal M_2,f_2)$ to mean that $\mathcal M_1\subseteq\mathcal M_2$ and $f_2|_{\mathcal M_1}=f_1$. So $(\mathcal S,\lesssim)$ is a partially ordered set. Suppose $\mathcal C=\{(\mathcal M_i,f_i):i\in I\}$ is a chain in $\mathcal S$. If $\mathcal N\equiv\bigcup\{\mathcal M_i:i\in I\}$, then the fact that $\mathcal C$ is a chain implies that $\mathcal N$ is a linear manifold. Define $F:\mathcal N\to\mathbb R$ by setting $F(x)=f_i(x)$ if $x\in\mathcal M_i$.



<a id="pdf-page-96"></a>
It is easily checked that $F$ is well defined, linear, and satisfies $F\leq q$ on $\mathcal N$. So $(\mathcal N,F)\in\mathcal S$ and $(\mathcal N,F)$ is an upper bound for $\mathcal C$. By Zorn’s Lemma, $\mathcal S$ has a maximal element $(\mathcal Y,F)$. But the preceding lemma implies that $\mathcal Y=\mathcal X$. Hence $F$ is the desired extension. $\blacksquare$

This section concludes with one important consequence of the Hahn–Banach Theorem. It will be generalized later (IV.3.11), but it is used so often it is worth singling out for consideration.

**6.13. Theorem.** *If $\mathcal X$ is a normed space and $\mathcal M$ is a linear manifold in $\mathcal X$, then*

$$
\operatorname{cl}\mathcal M
=\bigcap\{\ker f:f\in\mathcal X^*\text{ and }\mathcal M\subseteq\ker f\}.
$$

**Proof.** Let $\mathcal N=\bigcap\{\ker f:f\in\mathcal X^*\text{ and }\mathcal M\subseteq\ker f\}$. If $f\in\mathcal X^*$ and $\mathcal M\subseteq\ker f$, then the continuity of $f$ implies that $\operatorname{cl}\mathcal M\subseteq\ker f$. Hence $\operatorname{cl}\mathcal M\subseteq\mathcal N$. If $x_0\notin\operatorname{cl}\mathcal M$, then $d=\operatorname{dist}(x_0,\mathcal M)>0$. By Corollary 6.8 there is an $f$ in $\mathcal X^*$ such that $f(x_0)=1$ and $f(x)=0$ for every $x$ in $\mathcal M$. Hence $x_0\notin\mathcal N$. Thus $\mathcal N\subseteq\operatorname{cl}\mathcal M$ and the proof is complete. $\blacksquare$

**6.14. Corollary.** *If $\mathcal X$ is a normed space and $\mathcal M$ is a linear manifold in $\mathcal X$, then $\mathcal M$ is dense in $\mathcal X$ if and only if the only bounded linear functional on $\mathcal X$ that annihilates $\mathcal M$ is the zero functional.*

## Exercises

1. Complete the proof of Lemma 6.3.

2. Give the details of the proof of Corollary 6.5.

3. Show that $c^*$ is isometrically isomorphic to $l^1$. Are $c$ and $c_0$ isometrically isomorphic?

4. If $\mu$ is a Borel measure on $[0,1]$ and $\int x^n\,d\mu(x)=0$ for all $n\geq 0$, show that $\mu=0$.

5. If $n\geq 1$, show that there is a measure $\mu$ on $[0,1]$ such that for every polynomial $p$ of degree at most $n$,
   $$
   \int p\,d\mu=\sum_{k=1}^{n}p^{(k)}(k/n).
   $$

6. If $n\geq 1$, does there exist a measure $\mu$ on $[0,1]$ such that $p'(0)=\int p\,d\mu$ for every polynomial of degree at most $n$?

7. Does there exist a measure $\mu$ on $[0,1]$ such that $\int p\,d\mu=p'(0)$ for every polynomial $p$?

8. Let $K$ be a compact subset of $\mathbb C$ and define $A(K)$ to be $\{f\in C(K):f\text{ is analytic on int }K\}$. (Functions here are complex valued.) Show that if $a\in K$, then there is a probability measure $\mu$ supported on $\partial K$ such that $f(a)=\int f\,d\mu$ for every $f$ in $A(K)$. (A *probability measure* is a nonnegative measure $\mu$ such that $\|\mu\|=1$.)

9. If $K=\operatorname{cl}\mathbb D$ ($\mathbb D=\{|z|<1\}$) and $a\in K$, find the measure $\mu$ whose existence was proved in Exercise 8.



<a id="pdf-page-97"></a>
10. Let $P=\{p|_{\partial\mathbb D}:p=\text{an analytic polynomial}\}$ and consider $P$ as a manifold in $C(\partial\mathbb D)$. Show that if $\mu$ is a real-valued measure on $\partial\mathbb D$ such that $\int p\,d\mu=0$ for every $p$ in $P$, then $\mu=0$. Give an example of a complex-valued measure $\mu$ such that $\mu\ne0$ but $\int p\,d\mu=0$ for every $p$ in $P$.

## §7*. An Application: Banach Limits

If $x=\{x(n)\}\in c$, define $L(x)=\lim x(n)$. Then $L$ is a linear functional, $\|L\|=1$, and, if for $x$ in $c$, $x'$ is defined by $x'=(x(2),x(3),\ldots)$, then $L(x)=L(x')$. Also, if $x\geqslant0$ [that is, $x(n)\geqslant0$ for all $n$], then $L(x)\geqslant0$. In this section it will be shown that these properties of the limit functional can be extended to $l^\infty$. The proof uses the Hahn–Banach Theorem.

**7.1. Theorem.** There is a linear functional $L:l^\infty\to\mathbb F$ such that

(a) $\|L\|=1$.

(b) If $x\in c$, $L(x)=\lim x(n)$.

(c) If $x\in l^\infty$ and $x(n)\geqslant0$ for all $n$, then $L(x)\geqslant0$.

(d) If $x\in l^\infty$ and $x'\equiv(x(2),x(3),\ldots)$, then $L(x)=L(x')$.

**Proof.** First assume $\mathbb F=\mathbb R$; that is, $l^\infty=l_{\mathbb R}^\infty$. If $x\in l^\infty$, let $x'$ denote the element of $l^\infty$ defined in part (d) above. Put $\mathcal M=\{x-x':x\in l^\infty\}$. Note that $(x+\alpha y)'=x'+\alpha y'$ for any $x,y$ in $l^\infty$ and $\alpha$ in $\mathbb R$; hence $\mathcal M$ is a linear manifold in $l^\infty$. Let $1$ denote the sequence $(1,1,1,\ldots)$ in $l^\infty$.

**7.2. Claim.** $\operatorname{dist}(1,\mathcal M)=1$.

Since $0\in\mathcal M$, $\operatorname{dist}(1,\mathcal M)\leqslant1$. Let $x\in l^\infty$; if $(x-x')(n)\leqslant0$ for any $n$, then $\|1-(x-x')\|_\infty\geqslant|1-(x(n)-x'(n))|\geqslant1$. Suppose $0\leqslant(x-x')(n)=x(n)-x'(n)=x(n)-x(n+1)$ for all $n$. Thus $x(n+1)\leqslant x(n)$ for all $n$. Since $x\in l^\infty$, $\alpha=\lim x(n)$ exists. Thus $\lim(x-x')(n)=0$ and $\|1-(x-x')\|_\infty\geqslant1$. This proves the claim.

By Corollary 6.8 there is a linear functional $L:l^\infty\to\mathbb R$ such that $\|L\|=1$, $L(1)=1$, and $L(\mathcal M)=0$. So this functional satisfies (a) and (d) of the theorem. To prove (b), we establish the following.

**7.3. Claim.** $c_0\subseteq\ker L$.

If $x\in c_0$, let $x^{(1)}=x'$ and let $x^{(n+1)}=(x^{(n)})'$ for $n\geqslant1$. Note that $x^{(n+1)}-x=[x^{(n+1)}-x^{(n)}]+\cdots+[x'-x]\in\mathcal M$. Hence $L(x)=L(x^{(n)})$ for all $n\geqslant1$. If $\varepsilon>0$, then let $n$ be such that $|x(m)|<\varepsilon$ for $m>n$. Hence $|L(x)|=|L(x^{(n)})|\leqslant\|x^{(n)}\|_\infty=\sup\{|x(m)|:m>n\}<\varepsilon$. Thus $x\in\ker L$. Condition (b) is now clear.

To show (c), suppose there is an $x$ in $l^\infty$ such that $x(n)\geqslant0$ for all $n$ and $L(x)<0$. If $x$ is replaced by $x/\|x\|_\infty$, it remains true that $L(x)<0$ and it is



<a id="pdf-page-98"></a>
also true that $1\geq x(n)\geq 0$ for all $n$. But then $\|1-x\|_\infty\leq 1$ and $L(1-x)=1-L(x)>1$, contradicting (a). Thus (c) holds.

Now assume that $\mathbf F=\mathbf C$. Let $L_1$ be the functional obtained on $l_{\mathbf R}^{\infty}$. If $x\in l_{\mathbf C}^{\infty}$, then $x=x_1+ix_2$ where $x_1,x_2\in l_{\mathbf R}^{\infty}$. Define $L(x)=L_1(x_1)+iL_1(x_2)$. It is left as an exercise to show that $L$ is $\mathbf C$-linear. It’s clear that (b), (c), and (d) hold. It remains to show that $\|L\|=1$.

Let $E_1,\ldots,E_m$ be pairwise disjoint subsets of $\mathbf N$ and let $\alpha_1,\ldots,\alpha_m\in\mathbf C$ with $|\alpha_k|\leq 1$ for all $k$. Put $x=\sum_{k=1}^{m}\alpha_k\chi_{E_k}$; so $x\in l^\infty$ and $\|x\|_\infty\leq 1$. Then $L(x)=\sum_k\alpha_kL(\chi_{E_k})=\sum_k\alpha_kL_1(\chi_{E_k})$. But $L_1(\chi_{E_k})\geq 0$ and $\sum_kL_1(\chi_{E_k})=L_1(\chi_E)$, where $E=\bigcup_kE_k$. Hence $\sum_kL_1(\chi_{E_k})\leq 1$. Because $|\alpha_k|\leq 1$ for all $k$, $|L(x)|\leq 1$. If $x$ is an arbitrary element of $l^\infty$, $\|x\|_\infty\leq 1$, then there is a sequence $\{x_n\}$ of elements of $l^\infty$ such that $\|x_n-x\|_\infty\to 0$, $\|x_n\|_\infty\leq 1$, and each $x_n$ is the type of element of $l^\infty$ just discussed that takes on only a finite number of values (Exercise 3). Clearly, $\|L\|\leq 2$, so $L(x_n)\to L(x)$. Since $|L(x_n)|\leq 1$ for all $n$, $|L(x)|\leq 1$. Hence $\|L\|\leq 1$. Since $L(1)=1$, $\|L\|=1$. ■

A linear functional of the type described in Theorem 7.1 is called a *Banach limit*. They are useful for a variety of things, among which is the construction of representations of the algebra of bounded operators on a Hilbert space.

## Exercises

1. If $L$ is a Banach limit, show that there are $x$ and $y$ in $l^\infty$ such that $L(xy)\neq L(x)L(y)$.

2. Let $X$ be a set and $\Omega$ a $\sigma$-algebra of subsets of $X$. Suppose $\mu$ is a complex-valued countably additive measure defined on $\Omega$ such that $\|\mu\|=\mu(X)<\infty$. Show that $\mu(\Delta)\geq 0$ for every $\Delta$ in $\Omega$. (Though it is difficult to see at this moment, this fact is related to the proof of (c) in Theorem 7.1 for the complex case.)

3. Show that if $x\in l^\infty$, $\|x\|_\infty\leq 1$, then there is a sequence $\{x_n\}$, $x_n$ in $l^\infty$ such that $\|x_n\|_\infty\leq 1$, $\|x_n-x\|_\infty\to 0$, and each $x_n$ takes on only a finite number of values.

## §8*. An Application: Runge’s Theorem

The symbol $\mathbf C_\infty$ denotes the extended complex plane.

**8.1. Runge’s Theorem.** *Let $K$ be a compact subset of $\mathbf C$ and let $E$ be a subset of $\mathbf C_\infty\setminus K$ that meets each component of $\mathbf C_\infty\setminus K$. If $f$ is analytic in a neighborhood of $K$, then there are rational functions $f_n$ whose only poles lie in $E$ such that $f_n\to f$ uniformly on $K$.*

The main tool in proving Runge’s Theorem is Theorem 6.13. (A proof that does not use functional analysis can be found on p. 189 of Conway [1978].) To do this, let $R(K,E)$ be the closure in the space $C(K)$ of the rational functions with poles in $E$. By (6.13) and the Riesz Representation Theorem,



<a id="pdf-page-99"></a>
it suffices to show that if $\mu\in M(K)$ and $\int g\,d\mu=0$ for each $g$ in $R(K,E)$, then $\int f\,d\mu=0$.

Let $R>0$ and let $\lambda$ be area measure. Pick $\rho>0$ such that $B(0;R)\subseteq B(z;\rho)$ for every $z$ in $K$. Then for $z$ in $K$,

$$
\begin{aligned}
\int_{B(0;R)}|z-w|^{-1}\,d\lambda(w)
&\leq \int_{B(z;\rho)}|z-w|^{-1}\,d\lambda(w)\\
&=\int_0^{2\pi}\int_0^\rho dr\,d\theta=2\pi\rho.
\end{aligned}
$$

If $\mu\in M(K)$, define $\tilde{\mu}\colon\mathbb{C}\to[0,\infty]$ by

$$
\tilde{\mu}(w)=\int\frac{d|\mu|(z)}{|z-w|}
$$

when the integral is finite, and $\tilde{\mu}(w)=\infty$ otherwise. The inequality above implies

$$
\begin{aligned}
\int_{B(0;R)}\tilde{\mu}(w)\,d\lambda(w)
&=\int_{B(0;R)}\int_K\frac{d|\mu|(z)}{|z-w|}\,d\lambda(w)\\
&=\int_K\int_{B(0;R)}\frac{d\lambda(w)}{|z-w|}\,d|\mu|(z)\\
&\leq 2\pi\rho\|\mu\|.
\end{aligned}
$$

Thus $\tilde{\mu}(w)<\infty$ a.e. $[\lambda]$.

**8.2. Lemma.** If $\mu\in M(K)$, then

$$
\hat{\mu}(w)=\int\frac{d\mu(z)}{z-w}
$$

is in $L^1(B(0;R),\lambda)$ for any $R>0$, $\hat{\mu}$ is analytic on $\mathbb{C}_\infty\setminus K$, and $\hat{\mu}(\infty)=0$.

**Proof.** The first statement follows from what came before the statement of this lemma. To show that $\hat{\mu}$ is analytic on $\mathbb{C}_\infty\setminus K$, let $w,w_0\in\mathbb{C}\setminus K$ and note that

$$
\frac{\hat{\mu}(w)-\hat{\mu}(w_0)}{w-w_0}
=\int_K\frac{d\mu(z)}{(z-w)(z-w_0)}.
$$

As $w\to w_0$, $[(z-w)(z-w_0)]^{-1}\to(z-w_0)^{-2}$ uniformly for $z$ in $K$, so that $\hat{\mu}$ has a derivative at $w_0$ and

$$
\frac{d\hat{\mu}}{dw}(w_0)=\int_K(z-w_0)^{-2}\,d\mu(z).
$$

So $\hat{\mu}$ is analytic on $\mathbb{C}\setminus K$. To show that it is analytic at infinity, note that $\hat{\mu}(z)\to0$ as $z\to\infty$, so infinity is a removable singularity. $\blacksquare$



<a id="pdf-page-100"></a>
It is not difficult to see that for $w_0$ in $\mathbb{C}\setminus K$,

$$
\left(\frac{d}{dw}\right)^n\hat{\mu}(w_0)
=n!\int (z-w_0)^{-n-1}\,d\mu(z). \tag{8.3}
$$

Also, we can easily find the power series expansion of $\hat{\mu}$ at infinity. Indeed,

$$
\hat{\mu}(w)=\int\frac{1}{z-w}\,d\mu(z)
=-\frac{1}{w}\int\left(1-\frac{z}{w}\right)^{-1}\,d\mu(z).
$$

Choose $w$ near enough to infinity that $|z/w|<1$ for all $z$ in $K$. Then

$$
\begin{aligned}
\hat{\mu}(w)
&=-\frac{1}{w}\sum_{n=0}^{\infty}\int\left(\frac{z}{w}\right)^n\,d\mu(z)\\
&=-\sum_{n=0}^{\infty}\frac{a_n}{w^{n+1}},
\end{aligned}\tag{8.4}
$$

where $a_n=\int z^n\,d\mu(z)$.

Now assume $\mu\in M(K)$ and $\int g\,d\mu=0$ for every rational function $g$ with poles in $E$. Let $U$ be a component of $\mathbb{C}_\infty\setminus K$, and let $w_0\in E\cap U$. If $w_0\ne\infty$, then the hypothesis and (8.3) imply that each derivative of $\hat{\mu}$ at $w_0$ vanishes. Hence $\hat{\mu}\equiv0$ on $U$. If $w_0=\infty$, then (8.4) implies $\hat{\mu}\equiv0$ on $U$. Thus $\hat{\mu}\equiv0$ on $\mathbb{C}_\infty\setminus K$.

If $f$ is analytic on an open set $G$ containing $K$, let $\gamma_1,\ldots,\gamma_n$ be straight-line segments in $G\setminus K$ such that

$$
f(z)=\sum_{k=1}^{n}\frac{1}{2\pi i}\int_{\gamma_k}\frac{f(w)}{w-z}\,dw
$$

for all $z$ in $K$. (See p. 195 of Conway [1978].) Thus

$$
\begin{aligned}
\int_K f(z)\,d\mu(z)
&=\sum_{k=1}^{n}\frac{1}{2\pi i}\int_K\int_{\gamma_k}
\frac{f(w)}{w-z}\,dw\,d\mu(z)\\
&=-\sum_{k=1}^{n}\frac{1}{2\pi i}\int_{\gamma_k}
f(w)\hat{\mu}(w)\,dw
\end{aligned}
$$

by Fubini’s Theorem. But $\hat{\mu}(w)=0$ on $\gamma_k$ $(\subseteq\mathbb{C}\setminus K)$, so $\int f\,d\mu=0$. By (6.13), $f\in R(K,E)$. This proves Runge’s Theorem. $\blacksquare$

**8.5. Corollary.** *If $K$ is compact and $\mathbb{C}\setminus K$ is connected and if $f$ is analytic in a neighborhood of $K$, then there is a sequence of polynomials that converges to $f$ uniformly on $K$.*

## Exercises

1. Let $\mu$ be a compactly supported measure on $\mathbb{C}$ that is boundedly absolutely continuous with respect to area measure. Show that $\hat{\mu}$ is continuous on $\mathbb{C}_\infty$.

2. Let $m=$ Lebesgue measure on $[0,1]$. Show that $\hat{m}$ is not continuous at any point of $[0,1]$.



<a id="pdf-page-101"></a>
## §9*. An Application: Ordered Vector Spaces

In this section only vector spaces over $\mathbf{R}$ are considered.

There are numerous spaces in which there is a notion of $\leq$ in addition to the vector space structure. The $L^p$ spaces and $C(X)$ are some that spring to mind. The concept of an ordered vector space is an attempt to study such spaces in an abstract setting. The first step is to abstract the notion of the positive elements.

**9.1. Definition.** An *ordered vector space* is a pair $(\mathscr{X},\leq)$ where $\mathscr{X}$ is a vector space over $\mathbf{R}$ and $\leq$ is a relation on $\mathscr{X}$ satisfying

(a) $x\leq x$ for all $x$;  
(b) if $x\leq y$ and $y\leq z$, then $x\leq z$;  
(c) if $x\leq y$ and $z\in\mathscr{X}$, then $x+z\leq y+z$;  
(d) if $x\leq y$ and $\alpha\in[0,\infty)$, then $\alpha x\leq\alpha y$.

Note that it is not assumed that $\leq$ is *antisymmetric*. That is, it is not assumed that if $x\leq y$ and $y\leq x$, then $x=y$.

**9.2. Definition.** If $\mathscr{X}$ is a real vector space, a *wedge* is a nonempty subset $P$ of $\mathscr{X}$ such that

(a) if $x,y\in P$, then $x+y\in P$;  
(b) if $x\in P$ and $\alpha\in[0,\infty)$, then $\alpha x\in P$.

**9.3. Proposition.** *(a) If $(\mathscr{X},\leq)$ is an ordered vector space and $P=\{x\in\mathscr{X}:x\geq0\}$, then $P$ is a wedge. (b) If $P$ is a wedge in the real vector space $\mathscr{X}$ and $\leq$ is defined on $\mathscr{X}$ by declaring $x\leq y$ if and only if $y-x\in P$, then $(\mathscr{X},\leq)$ is an ordered vector space.*

**Proof.** Exercise.

If $(\mathscr{X},\leq)$ is an ordered vector space, $P=\{x\in\mathscr{X}:x\geq0\}$ is called the *wedge of positive elements*. The next result is also left as an exercise.

**9.4. Proposition.** *If $(\mathscr{X},\leq)$ is an ordered vector space and $P$ is the wedge of positive elements, $\leq$ is antisymmetric if and only if $P\cap(-P)=(0)$.*

**9.5. Definition.** A *cone* in $\mathscr{X}$ is a wedge $P$ such that $P\cap(-P)=(0)$.

**9.6. Definition.** If $(\mathscr{X},\leq)$ is an ordered vector space, a subset $A$ of $\mathscr{X}$ is *cofinal* if for every $x\geq0$ in $\mathscr{X}$ there is an $a$ in $A$ such that $a\geq x$. An element $e$ of $\mathscr{X}$ is an *order unit* if for every $x$ in $\mathscr{X}$ there is a positive integer $n$ such that $-ne\leq x\leq ne$.



<a id="pdf-page-102"></a>
If $X$ is a compact space $\mathcal{X}=C(X)$, then any non-zero constant function is an order unit. ($f\leq g$ if and only if $f(x)\leq g(x)$ for all $x$.) If $\mathcal{X}=C(\mathbb{R})$, all real-valued continuous functions on $\mathbb{R}$, then $\mathcal{X}$ has no order unit (Exercise 4). If $e$ is an order unit, then $\{ne:n\geq 1\}$ is cofinal.

**9.7. Definition.** If $(\mathcal{X},\leq)$ and $(\mathcal{Y},\leq)$ are ordered vector spaces and $T:\mathcal{X}\to\mathcal{Y}$ is a linear map, then $T$ is *positive* (in symbols $T\geq 0$) if $Tx\geq 0$ whenever $x\geq 0$.

The principal result of this section is the following.

**9.8. Theorem.** *Let $(\mathcal{X},\leq)$ be an ordered vector space and let $\mathcal{Y}$ be a linear manifold in $\mathcal{X}$ that is cofinal. If $f:\mathcal{Y}\to\mathbb{R}$ is a positive linear functional, then there is a positive linear functional $\tilde f:\mathcal{X}\to\mathbb{R}$ such that $\tilde f|_{\mathcal{Y}}=f$.*

**Proof.** Let $P=\{x\in\mathcal{X}:x\geq 0\}$ and put $\mathcal{X}_1=\mathcal{Y}+P-P$. It is easy to see that $\mathcal{X}_1$ is a linear manifold in $\mathcal{X}$. If there is a positive linear functional $g:\mathcal{X}_1\to\mathbb{R}$ that extends $f$, let $\tilde f$ be any linear functional on $\mathcal{X}$ that extends $g$ (use a Hamel basis). If $x\geq 0$, then $x\in P\subseteq\mathcal{X}_1$ so that $\tilde f(x)=g(x)\geq 0$. Hence $\tilde f$ is positive. Thus, we may assume that $\mathcal{X}=\mathcal{Y}+P-P$.

**9.9. Claim.** $\mathcal{X}=\mathcal{Y}+P=\mathcal{Y}-P$.

Let $x\in\mathcal{X}$; so $x=y+p_1-p_2$, $y$ in $\mathcal{Y}$, $p_1,p_2$ in $P$. Since $\mathcal{Y}$ is cofinal there is a $y_1$ in $\mathcal{Y}$ such that $y_1\geq p_1$. Hence $p_1=y_1-(y_1-p_1)\in\mathcal{Y}-P$. Thus $x=y-p_2+p_1\in(\mathcal{Y}-P)+(\mathcal{Y}-P)\subseteq\mathcal{Y}-P$. So $\mathcal{X}=\mathcal{Y}-P$. Also, $\mathcal{X}=-\mathcal{X}=-\mathcal{Y}+P=\mathcal{Y}+P$.

**9.10. Claim.** If $x\in\mathcal{X}$, there are $y_1,y_2$ in $\mathcal{Y}$ such that $y_2\leq x\leq y_1$.

In fact, Claim 9.9 states that we can write $x=y_1-p_1=y_2+p_2$, $p_1,p_2\in P$ and $y_1,y_2\in\mathcal{Y}$. Thus $y_2\leq x\leq y_1$.

By Claim 9.10, it is possible to define for each $x$ in $\mathcal{X}$,

$$
q(x)=\inf\{f(y):y\in\mathcal{Y}\text{ and }y\geq x\}.
$$

**9.11. Claim.** The function $q$ is a sublinear functional on $\mathcal{X}$.

The proof of (9.11) is left as an exercise.

For $y$ in $\mathcal{Y}$, let $y_1\in\mathcal{Y}$ such that $y_1\geq y$. Because $f$ is positive, $f(y)\leq f(y_1)$. Hence $f(y)\leq q(y)$ for all $y$ in $\mathcal{Y}$. The Hahn–Banach Theorem implies that there is a linear functional $\tilde f:\mathcal{X}\to\mathbb{R}$ such that $\tilde f|_{\mathcal{Y}}=f$ and $\tilde f\leq q$ on $\mathcal{X}$. If $x\in P$, then $-x\leq 0$ (and $0\in\mathcal{Y}$). Hence $q(-x)\leq f(0)$. Thus $-\tilde f(x)=\tilde f(-x)\leq q(-x)\leq 0$, or $\tilde f(x)\geq 0$. Therefore $\tilde f$ is positive. ■

**9.12. Corollary.** *Let $(\mathcal{X},\leq)$ be an ordered vector space with an order unit $e$. If $\mathcal{Y}$ is a linear manifold in $\mathcal{X}$ and $e\in\mathcal{Y}$, then any positive linear functional defined on $\mathcal{Y}$ has an extension to a positive linear functional defined on $\mathcal{X}$.*



<a id="pdf-page-103"></a>
# Exercises

1. Prove Proposition 9.3.

2. Prove Proposition 9.4.

3. Show that $e$ is an order unit for $(\mathcal{X},\leqslant)$ if and only if for every $x$ in $\mathcal{X}$ there is a $\delta>0$ such that $e\pm tx\geqslant 0$ for $0\leqslant t\leqslant\delta$.

4. Show that $C(\mathbb{R})$, the space of all continuous real-valued functions on $\mathbb{R}$, has no order unit.

5. Prove (9.11).

6. Characterize the order units of $C_b(X)$. Does $C_b(X)$ always have an order unit?

7. Characterize the order units of $C_0(X)$ if $X$ is locally compact. Does $C_0(X)$ always have an order unit?

8. Let $\mathcal{X}=M_2(\mathbb{R})$, the $2\times2$ matrices over $\mathbb{R}$. Define $A$ in $M_2(\mathbb{R})$ to be positive if $A=A^*$ and $\langle Ax,x\rangle\geqslant0$ for all $x$ in $\mathbb{R}^2$. Characterize the order units of $M_2(\mathbb{R})$.

9. If $1\leqslant p<\infty$ and $\mathcal{X}=L^p(0,1)$, define $f\leqslant g$ to mean that $f(x)\leqslant g(x)$ a.e. Show that $\mathcal{X}$ is an ordered vector space that has no order unit.

# §10. The Dual of a Quotient Space and a Subspace

Let $\mathcal{X}$ be a normed space and $\mathcal{M}\leqslant\mathcal{X}$. If $f\in\mathcal{X}^*$, then $f|_{\mathcal{M}}$, the restriction of $f$ to $\mathcal{M}$, belongs to $\mathcal{M}^*$ and $\|f|_{\mathcal{M}}\|\leqslant\|f\|$. According to the Hahn–Banach Theorem, every bounded linear functional on $\mathcal{M}$ is obtainable as the restriction of a functional from $\mathcal{X}^*$. In fact, more can be said.

Note that if $\mathcal{M}^{\perp}\equiv\{g\in\mathcal{X}^*:g(\mathcal{M})=0\}$ (note the analogy with Hilbert space notation); then $\mathcal{M}^{\perp}$ is a closed subspace of the Banach space $\mathcal{X}^*$. Hence $\mathcal{X}^*/\mathcal{M}^{\perp}$ is a Banach space. Moreover, if $f+\mathcal{M}^{\perp}\in\mathcal{X}^*/\mathcal{M}^{\perp}$, then $f+\mathcal{M}^{\perp}$ induces a linear functional on $\mathcal{M}$, namely $f|_{\mathcal{M}}$.

**10.1. Theorem.** *If $\mathcal{M}\leqslant\mathcal{X}$ and $\mathcal{M}^{\perp}\equiv\{g\in\mathcal{X}^*:g(\mathcal{M})=0\}$, then the map $\rho:\mathcal{X}^*/\mathcal{M}^{\perp}\to\mathcal{M}^*$ defined by*

$$
\rho(f+\mathcal{M}^{\perp})=f|_{\mathcal{M}}
$$

*is an isometric isomorphism.*

**Proof.** It is easy to see that $\rho$ is linear and injective. If $f\in\mathcal{X}^*$ and $g\in\mathcal{M}^{\perp}$, then $\|f|_{\mathcal{M}}\|=\|(f+g)|_{\mathcal{M}}\|\leqslant\|f+g\|$. Taking the infimum over all $g$ we get that $\|f|_{\mathcal{M}}\|\leqslant\|f+\mathcal{M}^{\perp}\|$. Suppose $\phi\in\mathcal{M}^*$. The Hahn–Banach Theorem implies that there is an $f$ in $\mathcal{X}^*$ such that $f|_{\mathcal{M}}=\phi$ and $\|f\|=\|\phi\|$. Hence $\phi=\rho(f+\mathcal{M}^{\perp})$ and $\|\phi\|=\|f\|\geqslant\|f+\mathcal{M}^{\perp}\|$. ■

Now consider $\mathcal{X}/\mathcal{M}$; what is $(\mathcal{X}/\mathcal{M})^*$? Let $Q:\mathcal{X}\to\mathcal{X}/\mathcal{M}$ be the natural map. If $f\in(\mathcal{X}/\mathcal{M})^*$, then $f\circ Q\in\mathcal{X}^*$ and $\|f\circ Q\|\leqslant\|f\|$. (Why?) This gives a way of mapping $(\mathcal{X}/\mathcal{M})^*\to\mathcal{X}^*$. What is its image? Is it an isometry?



<a id="pdf-page-104"></a>
**10.2. Theorem.** If $\mathcal M\leqslant\mathcal X$ and $Q:\mathcal X\to\mathcal X/\mathcal M$ is the natural map, then $\rho(f)=f\circ Q$ defines an isometric isomorphism of $(\mathcal X/\mathcal M)^*$ onto $\mathcal M^\perp$.

**Proof.** If $f\in(\mathcal X/\mathcal M)^*$ and $y\in\mathcal M$, then $f\circ Q(y)=0$, so $f\circ Q\in\mathcal M^\perp$. Again, it is easy to see that $\rho:(\mathcal X/\mathcal M)^*\to\mathcal M^\perp$ is linear and, as was seen earlier, $\|\rho(f)\|\leqslant\|f\|$. Let $\{x_n+\mathcal M\}$ be a sequence in $\mathcal X/\mathcal M$ such that $\|x_n+\mathcal M\|<1$ and $|f(x_n+\mathcal M)|\to\|f\|$. For each $n$ there is a $y_n$ in $\mathcal M$ such that $\|x_n+y_n\|<1$. Thus $\|\rho(f)\|\geqslant|\rho(f)(x_n+y_n)|=|f(x_n+\mathcal M)|\to\|f\|$, so $\rho$ is an isometry.

To see that $\rho$ is surjective, let $g\in\mathcal M^\perp$; then $g\in\mathcal X^*$ and $g(\mathcal M)=0$. Define $f:\mathcal X/\mathcal M\to\mathbb F$ by $f(x+\mathcal M)=g(x)$. Because $g(\mathcal M)=0$, $f$ is well defined. Also, if $x\in\mathcal X$ and $y\in\mathcal M$, $|f(x+\mathcal M)|=|g(x)|=|g(x+y)|\leqslant\|g\|\|x+y\|$. Taking the infimum over all $y$ gives $|f(x+\mathcal M)|\leqslant\|g\|\|x+\mathcal M\|$. Hence $f\in(\mathcal X/\mathcal M)^*$, $\rho(f)=g$, and $\|f\|\leqslant\|\rho(f)\|$. $\blacksquare$

## §11. Reflexive Spaces

If $\mathcal X$ is a normed space, then we have seen that $\mathcal X^*$ is a Banach space (5.4). Because $\mathcal X^*$ is a Banach space, it too has a dual space $(\mathcal X^*)^*\equiv\mathcal X^{**}$ and $\mathcal X^{**}$ is a Banach space. Hence $\mathcal X^{**}$ has a dual. Can this be kept up?

Before answering this question, let’s examine a curious phenomenon. If $x\in\mathcal X$, then $x$ defines an element $\hat x$ of $\mathcal X^{**}$; namely, define $\hat x:\mathcal X^*\to\mathbb F$ by

$$
\hat x(x^*)=x^*(x)\tag{11.1}
$$

for every $x^*$ in $\mathcal X^*$. Note that Corollary 6.7 implies that $\|\hat x\|=\|x\|$ for all $x$ in $\mathcal X$. The map $x\to\hat x$ of $\mathcal X\to\mathcal X^{**}$ is called the *natural map* of $\mathcal X$ into its *second dual*.

**11.2. Definition.** A normed space $\mathcal X$ is *reflexive* if $\mathcal X^{**}=\{\hat x:x\in\mathcal X\}$, where $\hat x$ is defined in (11.1).

First note that a reflexive space $\mathcal X$ is isometrically isomorphic to $\mathcal X^{**}$, and hence must be a Banach space. It is not true however, that a Banach space $\mathcal X$ that is isometric to $\mathcal X^{**}$ is reflexive. The definition of reflexivity stipulates that the isometry be the natural embedding of $\mathcal X$ into $\mathcal X^{**}$. In fact, James [1951] gives an example of a nonreflexive space $\mathcal X$ that is isometric to $\mathcal X^{**}$.

**11.3. Example.** If $1<p<\infty$, $L^p(X,\Omega,\mu)$ is reflexive.

**11.4. Example.** $c_0$ is not reflexive. We know that $c_0^*=l^1$, so $c_0^{**}=(l^1)^*=l^\infty$. With these identifications, the natural map $c_0\to c_0^{**}$ is precisely the inclusion map $c_0\to l^\infty$.

A discussion of reflexivity is best pursued after the weak topology is understood (Chapter V). Until that time, we will say *adieu* to reflexivity.



<a id="pdf-page-105"></a>
## Exercises

1. Show that $(\mathcal{X}^{*})^{**}$ and $(\mathcal{X}^{**})^{*}$ are equal.

2. Show that for a locally compact space $X$, $C_b(X)$ is reflexive if and only if $X$ is finite.

3. Let $\mathcal{M}\leqslant\mathcal{X}$ and let $\rho_{\mathcal{X}}:\mathcal{X}\to\mathcal{X}^{**}$ and $\rho_{\mathcal{M}}:\mathcal{M}\to\mathcal{M}^{**}$ be the natural maps. If $i:\mathcal{M}\to\mathcal{X}$ is the inclusion map, show that there is an isometry $\phi:\mathcal{M}^{**}\to\mathcal{X}^{**}$ such that the diagram

   [FIGURE: Commutative square with $\mathcal{X}$ at upper left, $\mathcal{X}^{**}$ at upper right, $\mathcal{M}$ at lower left, and $\mathcal{M}^{**}$ at lower right. The horizontal arrows point right and are labeled $\rho_{\mathcal{X}}$ (top) and $\rho_{\mathcal{M}}$ (bottom); the vertical arrows point up and are labeled $i$ (left) and $\phi$ (right).]

   commutes. Prove that $\phi(\mathcal{M}^{**})=(\mathcal{M}^{\perp})^{\perp}\equiv\{x^{**}\in\mathcal{X}^{**}:x^{**}(\mathcal{M}^{\perp})=0\}$.

4. Use Exercise 3 to show that if $\mathcal{X}$ is reflexive, then any closed subspace of $\mathcal{X}$ is also reflexive. See Yang [1967].

## §12. The Open Mapping and Closed Graph Theorems

**12.1. The Open Mapping Theorem.** *If $\mathcal{X},\mathcal{Y}$ are Banach spaces and $A:\mathcal{X}\to\mathcal{Y}$ is a continuous linear surjection, then $A(G)$ is open in $\mathcal{Y}$ whenever $G$ is open in $\mathcal{X}$.*

**Proof.** For $r>0$, let $B(r)=\{x\in\mathcal{X}:\|x\|<r\}$.

**12.2. Claim.** $0\in\operatorname{int}\operatorname{cl}A(B(r))$.

Note that because $A$ is surjective,
$$
\mathcal{Y}
=\bigcup_{k=1}^{\infty}\operatorname{cl}[A(B(kr/2))]
=\bigcup_{k=1}^{\infty}k\operatorname{cl}[A(B(r/2))].
$$
By the Baire Category Theorem, there is a $k\geqslant1$ such that $k\operatorname{cl}[A(B(r/2))]$ has nonempty interior. Thus $V=\operatorname{int}\{\operatorname{cl}[A(B(r/2))]\}\ne\square$. If $y_0\in V$, let $s>0$ such that $\{y\in\mathcal{Y}:\|y-y_0\|<s\}\subseteq V\subseteq\operatorname{cl}A(B(r/2))$. Let $y\in\mathcal{Y}$, $\|y\|<s$. Since $y_0\in\operatorname{cl}A(B(r/2))$, there is a sequence $\{x_n\}$ in $B(r/2)$ such that $A(x_n)\to y_0$. There is also a sequence $\{z_n\}$ in $B(r/2)$ such that $A(z_n)\to y_0+y$. Thus $A(z_n-x_n)\to y$ and $\{z_n-x_n\}\subseteq B(r)$; that is, $\{y\in\mathcal{Y}:\|y\|<s\}\subseteq\operatorname{cl}A(B(r))$. This establishes Claim 12.2.

It will now be shown that

$$
\tag{12.3}
\operatorname{cl}A(B(r/2))\subseteq A(B(r)).
$$

Note that if (12.3) is proved, then Claim 12.2 implies that $0\in\operatorname{int}A(B(r))$ for any $r>0$. From here the theorem is easily proved. Indeed, if $G$ is an open subset of $\mathcal{X}$, then for every $x$ in $G$ let $r_x>0$ such that $B(x;r_x)\subseteq G$. But $0\in\operatorname{int}A(B(r_x))$ and so $A(x)\in\operatorname{int}A(B(x;r_x))$. Thus there is an $s_x>0$ such that $U_x\equiv\{y\in\mathcal{Y}:\|y-A(x)\|<s_x\}\subseteq A(B(x;r_x))$. Therefore $A(G)\supseteq\bigcup\{U_x:x\in G\}$. But $A(x)\in U_x$, so $A(G)=\bigcup\{U_x:x\in G\}$ and hence $A(G)$ is open.



<a id="pdf-page-106"></a>
To prove (12.3), fix $y_1$ in $\operatorname{cl}A(B(r/2))$. By (12.2), $0\in\operatorname{int}[\operatorname{cl}A(B(2^{-2}r))]$. Hence
$[y_1-\operatorname{cl}A(B(2^{-2}r))]\cap A(B(r/2))\ne\varnothing$.
Let $x_1\in B(r/2)$ such that $A(x_1)\in[y_1-\operatorname{cl}A(B(2^{-2}r))]$; now $A(x_1)=y_1-y_2$, where $y_2\in\operatorname{cl}A(B(2^{-2}r))$. Using induction, we obtain a sequence $\{x_n\}$ in $\mathscr{X}$ and a sequence $\{y_n\}$ in $\mathscr{Y}$ such that

$$
\tag{12.4}
\left\{
\begin{array}{ll}
\text{(i)} & x_n\in B(2^{-n}r),\\
\text{(ii)} & y_n\in\operatorname{cl}A(B(2^{-n}r)),\\
\text{(iii)} & y_{n+1}=y_n-A(x_n).
\end{array}
\right.
$$

But $\|x_n\|<2^{-n}r$, so $\sum_1^\infty\|x_n\|<\infty$; hence $x=\sum_{n=1}^\infty x_n$ exists in $\mathscr{X}$ and $\|x\|<r$. Also,

$$
\sum_{k=1}^{n}A(x_k)
=\sum_{k=1}^{n}(y_k-y_{k+1})
=y_1-y_{n+1}.
$$

But (12.4ii) implies $\|y_n\|\leqslant\|A\|2^{-n}r$; hence $y_n\to0$. Therefore $y_1=\sum_{k=1}^\infty A(x_k)=A(x)\in A(B(r))$, proving (12.3) and completing the proof of the theorem. $\blacksquare$

The same method used to prove the Open Mapping Theorem can also be used to prove the Tietze Extension Theorem. See Grabiner [1986].

The Open Mapping Theorem has several applications. Here are two important ones.

**12.5. The Inverse Mapping Theorem.** *If $\mathscr{X}$ and $\mathscr{Y}$ are Banach spaces and $A:\mathscr{X}\to\mathscr{Y}$ is a bounded linear transformation that is bijective, then $A^{-1}$ is bounded.*

**Proof.** Because $A$ is continuous, bijective, and open by Theorem 12.1, $A$ is a homeomorphism. $\blacksquare$

**12.6. The Closed Graph Theorem.** *If $\mathscr{X}$ and $\mathscr{Y}$ are Banach spaces and $A:\mathscr{X}\to\mathscr{Y}$ is a linear transformation such that the graph of $A$,

$$
\operatorname{gra}A\equiv
\{x\oplus Ax\in\mathscr{X}\oplus_1\mathscr{Y}:x\in\mathscr{X}\}
$$

is closed, then $A$ is continuous.*

**Proof.** Let $\mathscr{G}=\operatorname{gra}A$. Since $\mathscr{X}\oplus_1\mathscr{Y}$ is a Banach space and $\mathscr{G}$ is closed, $\mathscr{G}$ is a Banach space. Define $P:\mathscr{G}\to\mathscr{X}$ by $P(x\oplus Ax)=x$. It is easy to check that $P$ is bounded and bijective. (Do it). By the Inverse Mapping Theorem, $P^{-1}:\mathscr{X}\to\mathscr{G}$ is continuous. Thus $A:\mathscr{X}\to\mathscr{Y}$ is the composition of the continuous map $P^{-1}:\mathscr{X}\to\mathscr{G}$ and the continuous map of $\mathscr{G}\to\mathscr{Y}$ defined by $x\oplus Ax\mapsto Ax$; $A$ is therefore continuous. $\blacksquare$

Let $\mathscr{X}=$ all functions $f:[0,1]\to\mathbb{F}$ such that the derivative $f'$ exists and is continuous on $[0,1]$. Let $\mathscr{Y}=C[0,1]$ and give both $\mathscr{X}$ and $\mathscr{Y}$ the supremum norm: $\|f\|=\sup\{|f(t)|:t\in[0,1]\}$. So $\mathscr{X}$ is not a Banach space, though $\mathscr{Y}$ is. Define $A:\mathscr{X}\to\mathscr{Y}$ by $Af=f'$. Clearly, $A$ is linear. If $\{f_n\}\subseteq\mathscr{X}$ and



<a id="pdf-page-107"></a>
92  III. Banach Spaces

$(f_n,f_n')\to(f,g)$ in $\mathscr X\times\mathscr Y$, then $f_n'\to g$ uniformly on $[0,1]$. Hence

$$
f_n(t)-f_n(0)=\int_0^t f_n'(s)\,ds\to\int_0^t g(s)\,ds.
$$

But $f_n(t)-f_n(0)\to f(t)-f(0)$, so

$$
f(t)=f(0)+\int_0^t g(s)\,ds.
$$

Thus $f'=g$ and gra $A$ is closed. However, $A$ is not bounded. (Why?)

The preceding example shows that the domain of the operator in the Closed Graph Theorem must be assumed to be complete. The next example (due to Alp Eden) shows that the range must also be assumed to be complete.

Let $\mathscr X$ be a separable infinite-dimensional Banach space and let $\{e_i:i\in I\}$ be a Hamel basis for $\mathscr X$ with $\|e_i\|=1$ for all $i$. Note that a Baire Category argument shows that $I$ is uncountable. If $x\in\mathscr X$, then $x=\sum_i\alpha_i e_i$, $\alpha_i\in\mathbb F$, and $\alpha_i=0$ for all but a finite number of $i$ in $I$. Define $\|x\|_1\equiv\sum_i|\alpha_i|$. It is left as an exercise for the reader to show that $\|\cdot\|_1$ is a norm on $\mathscr X$. Since $\|e_i\|=1$ for all $i$, $\|x\|\leq\sum_i|\alpha_i|=\|x\|_1$. Let $\mathscr Y=\mathscr X$ with the norm $\|\cdot\|_1$ and let $T:\mathscr Y\to\mathscr X$ be defined by $T(x)=x$. Note that it was just shown that $T:\mathscr Y\to\mathscr X$ is a contraction. Therefore gra $T$ is closed and hence so is gra $T^{-1}$. But $T^{-1}$ is not continuous because if it were, then $T$ would be a homeomorphism. Since $\mathscr X$ is separable, it would follow that $\mathscr Y$ is separable. But $\mathscr Y$ is not separable. To see this, note that $\|e_i-e_j\|_1=2$ for $i\ne j$ and since $I$ is uncountable, $\mathscr Y$ cannot be separable.

When applying the Closed Graph Theorem, the following result is useful.

**12.7. Proposition.** *If $\mathscr X$ and $\mathscr Y$ are normed spaces and $A:\mathscr X\to\mathscr Y$ is a linear transformation, then gra $A$ is closed if and only if whenever $x_n\to0$ and $Ax_n\to y$, it must be that $y=0$.*

PROOF. Exercise 3.

Note that (12.7) underlines the advantage of the Closed Graph Theorem. To show that $A$ is continuous, it suffices to show that if $x_n\to0$, then $Ax_n\to0$. By (12.7) this is eased by allowing us to assume that $\{Ax_n\}$ is convergent.

It is possible to give a measure-theoretic solution to Exercise 2.3, but here is one using the Closed Graph Theorem. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space, $1\leq p\leq\infty$, and $\phi:X\to\mathbb F$ an $\Omega$-measurable function such that $\phi f\in L^p(\mu)$ whenever $f\in L^p(\mu)$. Define $A:L^p(\mu)\to L^p(\mu)$ by $Af=\phi f$. Thus $A$ is linear and well defined. Suppose $f_n\to0$ and $\phi f_n\to g$ in $L^p(\mu)$. If $1\leq p<\infty$, then $f_n\to0$ in measure. By a theorem of Riesz, there is a subsequence $\{f_{n_k}\}$ such that $f_{n_k}(x)\to0$ a.e. $[\mu]$. Hence $\phi(x)f_{n_k}(x)\to0$ a.e. $[\mu]$. This implies $g=0$ and so gra $A$ is closed. If $p=\infty$, then $f_n(x)\to0$ a.e. $[\mu]$ and the same argument implies gra $A$ is closed. By the Closed Graph Theorem, $A$ is bounded. Clearly, it may be assumed that $\|A\|=1$. If $\delta>0$, let $E$ be a measurable subset of



<a id="pdf-page-108"></a>
$\{x:|\phi(x)|\geq 1+\delta\}$ with $\mu(E)<\infty$. We want to show that $\mu(E)=0$. But if $f=\chi_E$, then
$$
\mu(E)=\|f\|_p^p\geq\|Af\|_p^p=\|\phi f\|_p^p
=\int_E|\phi|^p\,d\mu\geq(1+\delta)^p\mu(E).
$$
Hence $\mu(E)=0$. Since $E$ was arbitrary it follows that $\phi$ is an essentially bounded function and $\|\phi\|_\infty\leq 1$. $\blacksquare$

**12.8. Definition.** If $\mathcal X,\mathcal Y$ are Banach spaces, an *isomorphism* of $\mathcal X$ and $\mathcal Y$ is a linear bijection $T:\mathcal X\to\mathcal Y$ that is a homeomorphism. Say that $\mathcal X$ and $\mathcal Y$ are *isomorphic* if there is an isomorphism of $\mathcal X$ onto $\mathcal Y$.

Note that the Inverse Mapping Theorem says that a continuous bijection is an isomorphism.

The use of the word “isomorphism” is counter to the spirit of category theory, but it is traditional in Banach space theory.

## Exercises

1. Suppose $\mathcal X$ and $\mathcal Y$ are Banach spaces. If $A\in\mathcal B(\mathcal X,\mathcal Y)$ and $\operatorname{ran}A$ is a second category space, show that $\operatorname{ran}A$ is closed.

2. Give both $C^{(1)}[0,1]$ and $C[0,1]$ the supremum norm. If $A:C^{(1)}[0,1]\to C[0,1]$ is defined by $Af=f'$, show that $A$ is not bounded.

3. Prove Proposition 12.7.

4. Let $\mathcal X$ be a vector space and suppose $\|\cdot\|_1$ and $\|\cdot\|_2$ are two norms on $\mathcal X$ and that $\mathscr T_1$ and $\mathscr T_2$ are the corresponding topologies. Show that if $\mathcal X$ is complete in both norms and $\mathscr T_1\supseteq\mathscr T_2$, then $\mathscr T_1=\mathscr T_2$.

5. Let $\mathcal X$ and $\mathcal Y$ be Banach spaces and let $A\in\mathcal B(\mathcal X,\mathcal Y)$. Show that there is a constant $c>0$ such that $\|Ax\|\geq c\|x\|$ for all $x$ in $\mathcal X$ if and only if $\ker A=(0)$ and $\operatorname{ran}A$ is closed.

6. Let $X$ be compact and suppose that $\mathcal X$ is a Banach subspace of $C(X)$. If $E$ is a closed subset of $X$ such that for every $g$ in $C(E)$ there is an $f$ in $\mathcal X$ with $f|E=g$, show that there is a constant $c>0$ such that for each $g$ in $C(E)$ there is an $f$ in $\mathcal X$ with $f|E=g$ and $\max\{|f(x)|:x\in X\}\leq c\max\{|g(x)|:x\in E\}$.

7. Let $1\leq p\leq\infty$ and suppose $(\alpha_{ij})$ is a matrix such that $(Af)(i)=\sum_{j=1}^{\infty}\alpha_{ij}f(j)$ defines an element $Af$ of $l^p$ for every $f$ in $l^p$. Show that $A\in\mathcal B(l^p)$.

8. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space, $1\leq p<\infty$, and suppose that $k:X\times X\to\mathbb F$ is an $\Omega\times\Omega$ measurable function such that for $f$ in $L^p(\mu)$ and a.e. $x$, $k(x,\cdot)f(\cdot)\in L^1(\mu)$ and $(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)$ defines an element $Kf$ of $L^p(\mu)$. Show that $K:L^p(\mu)\to L^p(\mu)$ is a bounded operator.

## §13. Complemented Subspaces of a Banach Space

If $\mathcal X$ is a Banach space and $\mathcal M\leq\mathcal X$, say that $\mathcal M$ is *algebraically complemented* in $\mathcal X$ if there is an $\mathcal N\leq\mathcal X$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal X$. Of course, the definition makes sense in a purely algebraic setting, so the requirement that $\mathcal M$ and $\mathcal N$ be closed seems fatuous. Why is it made?



<a id="pdf-page-109"></a>
94                                                        III. Banach Spaces

If $\mathcal M$ is a linear manifold in a vector space $\mathcal X$ (a Banach space or not), then a Hamel-basis argument can be fashioned to produce a linear manifold $\mathcal N$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal X$. So the requirement in the definition that $\mathcal M$ and $\mathcal N$ be closed subspaces of the Banach space $\mathcal X$ makes the existence problem more interesting. Also, since we are dealing with the category of Banach spaces, all definitions should involve only objects in that category.

If $\mathcal M$ and $\mathcal N$ are algebraically complemented closed subspaces of a normed space $\mathcal X$, then $A:\mathcal M\oplus_1\mathcal N\to\mathcal X$ defined by $A(m\oplus n)=m+n$ is a linear bijection. Also, $\|A(m\oplus n)\|=\|m+n\|\leqslant\|m\|+\|n\|=\|m\oplus n\|$. Hence $A$ is bounded. Say that $\mathcal M$ and $\mathcal N$ are *topologically complemented* if $A$ is a homeomorphism; equivalently, if $\lvert\!\lVert m+n\rVert\!\rvert=\|m\|+\|n\|$ is an equivalent norm. If $\mathcal X$ is a Banach space, then the Inverse Mapping Theorem implies $A$ is a homeomorphism. This proves the following.

**13.1. Theorem.** *If two subspaces of a Banach space are algebraically complementary, then they are topologically complementary.*

This permits us to speak of *complementary subspaces* of a Banach space without modifying the term. The proof of the next result is left to the reader.

**13.2. Theorem.** (a) *If $\mathcal M$ and $\mathcal N$ are complementary subspaces of a Banach space $\mathcal X$ and $E:\mathcal X\to\mathcal X$ is defined by $E(m+n)=m$ for $m$ in $\mathcal M$ and $n$ in $\mathcal N$, then $E$ is a continuous linear operator such that $E^2=E$, $\operatorname{ran}E=\mathcal M$, and $\ker E=\mathcal N$.* (b) *If $E\in\mathcal B(\mathcal X)$ and $E^2=E$, then $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$ are complementary subspaces of $\mathcal X$.*

If $\mathcal M\leqslant\mathcal X$ and $\mathcal M$ is complemented in $\mathcal X$, its complementary subspace may not be unique. Indeed, finite dimensional spaces furnish the necessary examples.

A result due to R.S. Phillips [1940] is that $c_0$ is not complemented in $l^\infty$. A straightforward proof of this can be found in Whitley [1966]. Murray [1937] showed that $l^p$, $p\ne2$, $p>1$ has *uncomplemented* subspaces. This seems to be the first paper to exhibit uncomplemented subspaces of a Banach space.

Lindenstrauss [1967] showed that if $\mathcal M$ is an infinite dimensional subspace of $l^\infty$ that is complemented in $l^\infty$, then $\mathcal M$ is isomorphic to $l^\infty$. This same result holds if $l^\infty$ is replaced by $l^p$, $1\leqslant p<\infty$, $c$, or $c_0$.

Does there exist a Banach space $\mathcal X$ such that every closed subspace of $\mathcal X$ is complemented? Of course, if $\mathcal X$ is a Hilbert space, then this is true. But are there any Banach spaces that have this property and are not Hilbert spaces? Lindenstrauss and Tzafriri [1971] proved that if $\mathcal X$ is a Banach space and every subspace of $\mathcal X$ is complemented, then $\mathcal X$ is isomorphic to a Hilbert space.



<a id="pdf-page-110"></a>
## Exercises

1. If $\mathcal X$ is a vector space and $\mathcal M$ is a linear manifold in $\mathcal X$, show that there is a linear manifold $\mathcal N$ in $\mathcal X$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal X$.

2. Let $\mathcal X$ be a Banach space and let $E:\mathcal X\to\mathcal X$ be a linear map such that $E^2=E$ and both $\operatorname{ran}E$ and $\ker E$ are closed. Show that $E$ is continuous.

3. Prove Theorem 13.2.

4. Let $\mathcal X$ be a Banach space and show that if $\mathcal M$ is a complemented subspace of $\mathcal X$, then every complementary subspace is isomorphic to $\mathcal X/\mathcal M$.

5. Let $X$ be a compact set and let $Y$ be a closed subset of $X$. A *simultaneous extension* for $Y$ is a bounded linear map $T:C(Y)\to C(X)$ such that for each $g$ in $C(Y)$, $T(g)|Y=g$. Let $C_0(X\setminus Y)=\{f\in C(X):f(y)=0\text{ for all }y\text{ in }Y\}$. Show that if there is a simultaneous extension for $Y$, then $C_0(X\setminus Y)$ is complemented in $C(X)$.

6. Show that if $Y$ is a closed subset of $[0,1]$, then there is a simultaneous extension for $Y$ (see Exercise 5). (Hint: Write $[0,1]\setminus Y$ as the union of disjoint intervals.)

7. Using the notation of Exercise 5, show that if $Y$ is a retract of $X$, then $C_0(X\setminus Y)$ is complemented in $C(X)$.

## §14. The Principle of Uniform Boundedness

There are several results that may be called the Principle of Uniform Boundedness (PUB) and all of these are called the PUB by various mathematicians. In this book the PUB will refer to any of the results of this section, though in a formal way the next result plays the role of the founder of the family.

**14.1. Principle of Uniform Boundedness (PUB).** *Let $\mathcal X$ be a Banach space and $\mathcal Y$ a normed space. If $\mathcal A\subseteq\mathcal B(\mathcal X,\mathcal Y)$ such that for each $x$ in $\mathcal X$, $\sup\{\|Ax\|:A\in\mathcal A\}<\infty$, then $\sup\{\|A\|:A\in\mathcal A\}<\infty$.*

**Proof.** (Due to William R. Zame, 1978. Also see J. Hennefeld [1980].) For each $x$ in $\mathcal X$ let $M(x)=\sup\{\|Ax\|:A\in\mathcal A\}$, so $\|Ax\|\leq M(x)$ for all $x$ in $\mathcal X$. Suppose $\sup\{\|A\|:A\in\mathcal A\}=\infty$. Then there is a sequence $\{A_n\}\subseteq\mathcal A$ and a sequence $\{x_n\}$ of vectors in $\mathcal X$ such that $\|x_n\|=1$ and $\|A_nx_n\|>4^n$. Let $y_n=2^{-n}x_n$; thus $\|y_n\|=2^{-n}$ and $\|A_ny_n\|>2^n$.

**14.2. Claim.** There is a subsequence $\{y_{n_k}\}$ such that for $k\geq 1$:

(a) $$\|A_{n_{k+1}}y_{n_{k+1}}\|>1+k+\sum_{j=1}^{k}M(y_{n_j});$$

(b) $$\|y_{n_{k+1}}\|<2^{-k-1}\left[\sup\{\|A_{n_j}\|:1\leq j\leq k\}\right]^{-1}.$$

The proof of (14.2) is by induction. Let $n_1=1$. The induction step is valid since $\|y_n\|\to 0$ and $\|A_ny_n\|\to\infty$. The details are left to the reader.



<a id="pdf-page-111"></a>
Since $\sum_k \|y_{n_k}\|<\infty$, $\sum_k y_{n_k}=y$ in $\mathcal{X}$ (here is where the completeness of $\mathcal{X}$ is used.) Now for any $k\geq 1$,

$$
\begin{aligned}
\|A_{n_{k+1}}y\|
&=\left\|\sum_{j=1}^{k}A_{n_{k+1}}y_{n_j}
+A_{n_{k+1}}y_{n_{k+1}}
+\sum_{j=k+2}^{\infty}A_{n_{k+1}}y_{n_j}\right\|\\
&=\left\|A_{n_{k+1}}y_{n_{k+1}}
-\left[-\sum_{j=1}^{k}A_{n_{k+1}}y_{n_j}
-\sum_{j=k+2}^{\infty}A_{n_{k+1}}y_{n_j}\right]\right\|\\
&\geq \|A_{n_{k+1}}y_{n_{k+1}}\|
-\left\|\sum_{j=1}^{k}A_{n_{k+1}}y_{n_j}
+\sum_{j=k+2}^{\infty}A_{n_{k+1}}y_{n_j}\right\|\\
&\geq 1+k+\sum_{j=1}^{k}M(y_{n_j})
-\left[\sum_{j=1}^{k}M(y_{n_j})
+\sum_{j=k+2}^{\infty}\|A_{n_{k+1}}\|\,\|y_{n_j}\|\right]\\
&\geq 1+k-\sum_{j=k+2}^{\infty}2^{-j}\\
&\geq k.
\end{aligned}
$$

That is, $M(y)\geq k$ for all $k$, a contradiction. $\blacksquare$

**14.3. Corollary.** *If $\mathcal{X}$ is a normed space and $A\subseteq\mathcal{X}$, then $A$ is a bounded set if and only if for every $f$ in $\mathcal{X}^{*}$, $\sup\{|f(a)|:a\in A\}<\infty$.*

**PROOF.** Consider $\mathcal{X}$ as a subset of $\mathcal{B}(\mathcal{X}^{*},\mathbb{F})$ $(=\mathcal{X}^{**})$ by letting $\hat{x}(f)=f(x)$ for every $f$ in $\mathcal{X}^{*}$. Since $\mathcal{X}^{*}$ is a Banach space and $\|x\|=\|\hat{x}\|$ for all $x$, the corollary is a special case of the PUB. $\blacksquare$

**14.4. Corollary.** *If $\mathcal{X}$ is a Banach space and $A\subseteq\mathcal{X}^{*}$, then $A$ is a bounded set if and only if for every $x$ in $\mathcal{X}$, $\sup\{|f(x)|:f\in A\}<\infty$.*

**PROOF.** Consider $\mathcal{X}^{*}$ as $\mathcal{B}(\mathcal{X},\mathbb{F})$. $\blacksquare$

Using Corollary 14.3, it is possible to prove the following improvement of (14.1).

**14.5. Corollary.** *If $\mathcal{X}$ is a Banach space and $\mathcal{Y}$ is a normed space and if $\mathcal{A}\subseteq\mathcal{B}(\mathcal{X},\mathcal{Y})$ such that for every $x$ in $\mathcal{X}$ and $g$ in $\mathcal{Y}^{*}$,*

$$
\sup\{|g(A(x))|:A\in\mathcal{A}\}<\infty,
$$

*then $\sup\{\|A\|:A\in\mathcal{A}\}<\infty$.*

**PROOF.** Fix $x$ in $\mathcal{X}$. By the hypothesis and Corollary 14.3, $\sup\{\|A(x)\|:A\in\mathcal{A}\}<\infty$. By (14.1), $\sup\{\|A\|:A\in\mathcal{A}\}<\infty$. $\blacksquare$

A special form of the PUB that is quite useful is the following.

**14.6. The Banach–Steinhaus Theorem.** *If $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces and*



<a id="pdf-page-112"></a>
$\{A_n\}$ is a sequence in $\mathcal{B}(\mathcal{X},\mathcal{Y})$ with the property that for every $x$ in $\mathcal{X}$ there is a $y$ in $\mathcal{Y}$ such that $\|A_nx-y\|\to 0$, then there is an $A$ in $\mathcal{B}(\mathcal{X},\mathcal{Y})$ such that $\|A_nx-Ax\|\to 0$ for every $x$ in $\mathcal{X}$ and $\sup_n\|A_n\|<\infty$.

**Proof.** If $x\in\mathcal{X}$, let $Ax=\lim_{n\to\infty}A_nx$. By hypothesis $A:\mathcal{X}\to\mathcal{Y}$ is defined and it is easy to see that it is linear. To show that $A$ is bounded, note that the PUB implies that there is a constant $M>0$ such that $\|A_n\|\leq M$ for all $n$. If $x\in\mathcal{X}$ and $\|x\|\leq 1$, then for any $n\geq 1$, $\|Ax\|\leq\|Ax-A_nx\|+\|A_nx\|\leq\|Ax-A_nx\|+M$. Letting $n\to\infty$ shows that $\|Ax\|\leq M$ whenever $\|x\|\leq 1$. $\blacksquare$

The Banach–Steinhaus Theorem is a result about sequences, not nets. Note that if $I$ is the identity operator on $\mathcal{X}$ and for each $n\geq 1$, $A_n=n^{-1}I$ and for $n\leq 0$, $A_n=nI$, then $\{A_n:n\in\mathbb{Z}\}$ is a countable net that converges in norm to $0$, but the net is not bounded.

**14.7. Proposition.** *Let $X$ be locally compact and let $\{f_n\}$ be a sequence in $C_0(X)$. Then $\int f_n\,d\mu\to\int f\,d\mu$ for every $\mu$ in $M(X)$ if and only if $\sup_n\|f_n\|<\infty$ and $f_n(x)\to f(x)$ for every $x$ in $X$.*

**Proof.** Suppose $\int f_n\,d\mu\to\int f\,d\mu$ for every $\mu$ in $M(X)$. Since $M(X)=C_0(X)^*$, (14.3) implies that $\sup_n\|f_n\|<\infty$. By letting $\mu=\delta_x$, the unit point mass at $x$, we see that $\int f_n\,d\delta_x=f_n(x)\to f(x)$. The converse follows by the Lebesgue Dominated Convergence Theorem. $\blacksquare$

## Exercises

1. Here is another proof of the PUB using the Baire Category Theorem. With the notation of (14.1), let $B_n\equiv\{x\in\mathcal{X}:\|Ax\|\leq n\text{ for all }A\text{ in }\mathcal{A}\}$. By hypothesis, $\bigcup_{n=1}^{\infty}B_n=\mathcal{X}$. Now apply the Baire Category Theorem.

2. If $1<p<\infty$ and $\{x_n\}\subseteq l^p$, then $\sum_{j=1}^{\infty}x_n(j)y(j)\to 0$ for every $y$ in $l^q$, $1/p+1/q=1$, if and only if $\sup_n\|x_n\|_p<\infty$ and $x_n(j)\to 0$ for every $j\geq 1$.

3. If $\{x_n\}\subseteq l^1$, then $\sum_{j=1}^{\infty}x_n(j)y(j)\to 0$ for every $y$ in $c_0$ if and only if $\sup_n\|x_n\|_1<\infty$ and $x_n(j)\to 0$ for every $j\geq 1$.

4. If $(X,\Omega,\mu)$ is a measure space, $1<p<\infty$, and $\{f_n\}\subseteq L^p(X,\Omega,\mu)$, then $\int f_ng\,d\mu\to 0$ for every $g$ in $L^q(\mu)$, $1/p+1/q=1$, if and only if $\sup\{\|f_n\|_p:n\geq 1\}<\infty$ and for every set $E$ in $\Omega$ with $\mu(E)<\infty$, $\int_E f_n\,d\mu\to 0$ as $n\to\infty$.

5. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\{f_n\}$ is a sequence in $L^1(X,\Omega,\mu)$, then $\int f_ng\,d\mu\to 0$ for every $g$ in $L^\infty(\mu)$ if and only if $\sup\{\|f_n\|_1:n\geq 1\}<\infty$ and $\int_E f_n\,d\mu\to 0$ for every $E$ in $\Omega$.

6. Let $\mathcal{H}$ be a Hilbert space and let $\mathcal{E}$ be an orthonormal basis for $\mathcal{H}$. Show that a sequence $\{h_n\}$ in $\mathcal{H}$ satisfies $\langle h_n,h\rangle\to 0$ for every $h$ in $\mathcal{H}$ if and only if $\sup\{\|h_n\|:n\geq 1\}<\infty$ and $\langle h_n,e\rangle\to 0$ for every $e$ in $\mathcal{E}$.

7. If $X$ is locally compact and $\{\mu_n\}$ is a sequence in $M(X)$, then $L(\mu_n)\to 0$ for every $L$ in $M(X)^*$ if and only if $\sup\{\|\mu_n\|:n\geq 1\}<\infty$ and $\mu_n(E)\to 0$ for every Borel set $E$.

8. In (14.6), show that $\|A\|\leq\liminf\|A_n\|$.



<a id="pdf-page-113"></a>
9. If $(S,d)$ is a metric space and $\mathcal X$ is a normed space, say that a function $f:S\to\mathcal X$ is a *Lipschitz function* if there is a constant $M>0$ such that $\|f(s)-f(t)\|\leq Md(s,t)$ for all $s,t$ in $S$. Show that if $f:S\to\mathcal X$ is a function such that for all $L$ in $\mathcal X^*$, $L\circ f:S\to\mathbb F$ is Lipschitz, then $f:S\to\mathcal X$ is a Lipschitz function.

10. Let $\mathcal X$ be a Banach space and suppose $\{x_n\}$ is a sequence in $\mathcal X$ such that for each $x$ in $\mathcal X$ there are unique scalars $\{\alpha_n\}$ such that $\lim_{n\to\infty}\|x-\sum_{k=1}^n\alpha_kx_k\|=0$. Such a sequence is called a *Schauder basis*. (a) Prove that $\mathcal X$ is separable. (b) Let $\mathcal Y=\{\{\alpha_n\}\in\mathbb F^{\mathbb N}:\sum_{n=1}^{\infty}\alpha_nx_n\text{ converges in }\mathcal X\}$ and for $y=\{\alpha_n\}$ in $\mathcal Y$ define $\|y\|=\sup_n\|\sum_{k=1}^n\alpha_kx_k\|$. Show that $\mathcal Y$ is a Banach space. (c) Show that there is a bounded bijection $T:\mathcal X\to\mathcal Y$. (d) If $n\geq1$ and $f_n:\mathcal X\to\mathbb F$ is defined by $f_n(\sum_{k=1}^{\infty}\alpha_kx_k)=\alpha_n$, show that $f_n\in\mathcal X^*$. (e) Show that $x_n\notin$ the closed linear span of $\{x_k:k\neq n\}$.

