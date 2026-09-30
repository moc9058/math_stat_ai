# I. Hilbert Spaces


<a id="pdf-page-16"></a>
CHAPTER I

# Hilbert Spaces

A Hilbert space is the abstraction of the finite-dimensional Euclidean spaces of geometry. Its properties are very regular and contain few surprises, though the presence of an infinity of dimensions guarantees a certain amount of surprise. Historically, it was the properties of Hilbert spaces that guided mathematicians when they began to generalize. Some of the properties and results seen in this chapter and the next will be encountered in more general settings later in this book, or we shall see results that come close to these but fail to achieve the full power possible in the setting of Hilbert space.

## §1. Elementary Properties and Examples

<!-- BEGIN BACKGROUND BG-I.block1 -->
<a id="bg-i-1"></a>
### Definition BG-I.1. Metric language used throughout this chapter

In a metric space $(X,d)$, $B(x,r)=\{y:d(x,y)<r\}$. A set is **open** if it contains a ball around each of its points, and **closed** if its complement is open. Its closure $\overline A$ consists of points whose every ball meets $A$; $A$ is **dense** if $\overline A=X$. A sequence converges to $x$ if $d(x_n,x)\to0$, and is **Cauchy** if for every $\varepsilon>0$ there is one $N$ such that $d(x_n,x_m)<\varepsilon$ whenever $m,n\geq N$. Completeness means that every Cauchy sequence converges in the space. A space is **separable** if it has a countable dense subset. These definitions concern the metric, not the algebraic dimension.

<a id="bg-i-2"></a>
### Lemma BG-I.2. Closedness, completeness, and passing to limits

In a metric space, $A$ is closed exactly when it contains every limit of a convergent sequence in $A$. A closed subset of a complete space is complete; a complete subspace of any metric space is closed. A Cauchy sequence with a convergent subsequence converges to the same limit. A map between metric spaces is continuous exactly when it preserves limits of sequences.

**Proof.** If $x\in\overline A$, choose $a_n\in A\cap B(x,1/n)$; this proves the nontrivial direction of the closedness criterion. A Cauchy sequence in a closed subset converges in the ambient complete space and its limit remains in that subset. Conversely, if a sequence in a complete subspace converges in the ambient space, it is Cauchy, has a limit in the subspace, and uniqueness of metric limits identifies the two limits. If $x_{n_k}\to x$ and $(x_n)$ is Cauchy, choose $N$ making all tail distances less than $\varepsilon/2$, then choose $n_k\geq N$ with $d(x_{n_k},x)<\varepsilon/2$; the triangle inequality proves $x_n\to x$. Continuity preserves limits by its epsilon-delta definition. If continuity fails at $x$, some $\varepsilon>0$ allows choices $d(x_n,x)<1/n$ but $d(f(x_n),f(x))\geq\varepsilon$, contradicting preservation of limits. $\square$

<a id="bg-i-3"></a>
### Definition BG-I.3. Pointwise, uniform, and locally uniform convergence

For scalar-valued functions on $E$, **pointwise convergence** means that for each $x$ and $\varepsilon>0$ there exists $N=N(x,\varepsilon)$ such that $|f_n(x)-f(x)|<\varepsilon$ for $n\geq N$. **Uniform convergence** requires one $N=N(\varepsilon)$ for all $x\in E$; equivalently $\sup_E|f_n-f|\to0$. **Locally uniform convergence** on an open subset of $\mathbb C$ means uniform convergence on every compact subset. A sequence is uniformly Cauchy if $\sup_E|f_n-f_m|\to0$ as $n,m\to\infty$.

<a id="bg-i-4"></a>
### Theorem BG-I.4. Uniform-limit tools

A uniformly Cauchy sequence of scalar functions has a uniform limit. A uniform limit of continuous functions is continuous. If $\sum_n\sup_E|g_n|<\infty$, then $\sum_n g_n$ converges uniformly and absolutely (the Weierstrass test). For measurable functions on $E$ with $\mu(E)<\infty$, uniform convergence implies that the $L^p$ norm of the difference tends to zero for $1\leq p<\infty$, with

$$
\|f_n-f\|_p\leq\mu(E)^{1/p}\sup_E|f_n-f|.
$$

**Proof.** Scalar completeness first supplies the pointwise limit. In $|f_n(x)-f_m(x)|\leq\varepsilon$, let $m\to\infty$; the same bound holds for every $x$, proving uniform convergence. For continuity at $x_0$, choose $n$ with $\sup|f_n-f|<\varepsilon/3$ and a neighborhood where $|f_n(x)-f_n(x_0)|<\varepsilon/3$, and add the three errors. For a series, its tail is bounded uniformly by $\sum_{n>N}\sup|g_n|$, which tends to zero. Finally integrate $|f_n-f|^p\leq(\sup|f_n-f|)^p$. $\square$

Pointwise convergence alone is insufficient: $x^n$ on $[0,1]$ converges pointwise to a discontinuous function. Also $L^2$ convergence does not mean pointwise convergence of the whole sequence; the precise subsequence statement appears below.

<a id="bg-i-5"></a>
### Definition BG-I.5. Measure-theoretic conventions

A $\sigma$-algebra is closed under complements and countable unions; a measure is a countably additive nonnegative set function with $\mu(\varnothing)=0$. A measurable scalar function has measurable inverse images of Borel sets. A property holds **almost everywhere** (a.e.) if its exceptions lie in a measurable set of measure zero. In $L^p(\mu)$, functions equal a.e. are identified, and $\|f\|_p=(\int|f|^p\,d\mu)^{1/p}$ for finite $p$. Thus a nonzero value at a single null point does not produce a nonzero vector in $L^p$. Integration of complex functions means integration of real and imaginary parts. A measure is $\sigma$-finite if the space is a countable union of sets of finite measure.

<a id="bg-i-6"></a>
### Theorem BG-I.6. Three convergence rules for the Lebesgue integral

For nonnegative measurable $u_n\uparrow u$, $\int u_n\uparrow\int u$ (monotone convergence). For nonnegative $u_n$, $\int\liminf u_n\leq\liminf\int u_n$ (Fatou). If $f_n\to f$ a.e. and $|f_n|\leq g\in L^1$, then $\int|f_n-f|\to0$ (dominated convergence).

**Proof.** Write $L=\lim\int u_n\leq\int u$. For a nonnegative simple function $s\leq u$ and $0<c<1$, the sets $E_n=\{u_n\geq cs\}$ increase and exhaust the support of $s$. Countable additivity gives $\int_{E_n}s\to\int s$, and $\int u_n\geq c\int_{E_n}s$. Consequently $L\geq c\int s$. Take the supremum over simple $s\leq u$ (the definition of the nonnegative integral), then let $c\uparrow1$. For Fatou apply this result to $v_n=\inf_{k\geq n}u_k$, using $\int v_n\leq\inf_{k\geq n}\int u_k$. For dominated convergence apply Fatou to $2g-|f_n-f|\geq0$; since its pointwise limit is $2g$, subtraction of the finite number $2\int g$ yields $\limsup\int|f_n-f|\leq0$. $\square$

<a id="bg-i-7"></a>
### Lemma BG-I.7. The $L^2$ estimates and completeness omitted in Example 1.3

If $f,g\in L^2$, then $f\overline g\in L^1$ and $\int|fg|\leq\|f\|_2\|g\|_2$. The space $L^2$ is complete. Moreover, $f_n\to f$ in $L^2$ has a subsequence converging to $f$ a.e.

**Proof.** For nonzero norms apply $2ab\leq a^2+b^2$ to $a=|f|/\|f\|_2$, $b=|g|/\|g\|_2$ and integrate; the zero-norm cases are immediate. Expanding $|f+g|^2$ and applying this estimate gives the triangle inequality for $\|\cdot\|_2$.

Given a Cauchy sequence, choose $n_k$ with $\|f_{n_{k+1}}-f_{n_k}\|_2\leq2^{-k}$. Put $g_k=f_{n_{k+1}}-f_{n_k}$ and $S_N=\sum_{k=1}^N|g_k|$. The triangle inequality gives $\|S_N\|_2\leq1$; monotone convergence gives $S=\sum|g_k|\in L^2$. Hence the series $f_{n_1}+\sum g_k$ converges a.e. to a measurable $f$. Fatou applied to its tails gives $\|f-f_{n_k}\|_2\leq\sum_{j\geq k}2^{-j}$, so $f\in L^2$ and the subsequence, then the whole Cauchy sequence, converges in norm. For the last assertion choose $n_k$ with $\|f_{n_k}-f\|_2^2\leq2^{-k}$. Monotone convergence gives $\int\sum_k|f_{n_k}-f|^2<\infty$, so the summands tend to zero a.e. $\square$

<a id="bg-i-8"></a>
### Lemma BG-I.8. Sums over an arbitrary index set

For $a_i\geq0$, define $\sum_{i\in I}a_i=\sup\{\sum_{i\in F}a_i:F\subset I\text{ finite}\}$. If this is finite, only countably many $a_i$ are nonzero, and for every $\varepsilon>0$ a finite $F$ leaves a tail sum less than $\varepsilon$. Consequently the definition of $\ell^2(I)$ does not depend on choosing an ordering.

**Proof.** Each $\{i:a_i\geq1/n\}$ is finite, since arbitrarily many of its elements would force unbounded finite sums. Their countable union contains every positive term. If the sum is $s$, choose $F$ with $\sum_Fa_i>s-\varepsilon$. For every finite $G\subset I\setminus F$, $\sum_Ga_i\leq s-\sum_Fa_i<\varepsilon$; take the supremum. For $x,y\in\ell^2(I)$ the finite-sum Schwarz inequality bounds $\sum|x(i)y(i)|$ by $\|x\|_2\|y\|_2$, so their inner product converges absolutely. $\square$
<!-- END BACKGROUND BG-I.block1 -->

Throughout this book $\mathbb{F}$ will denote either the real field, $\mathbb{R}$, or the complex field, $\mathbb{C}$.

**1.1. Definition.** If $\mathscr{X}$ is a vector space over $\mathbb{F}$, a *semi-inner product* on $\mathscr{X}$ is a function $u:\mathscr{X}\times\mathscr{X}\to\mathbb{F}$ such that for all $\alpha,\beta$ in $\mathbb{F}$, and $x,y,z$ in $\mathscr{X}$, the following are satisfied:

(a) $u(\alpha x+\beta y,z)=\alpha u(x,z)+\beta u(y,z),$

(b) $u(x,\alpha y+\beta z)=\bar{\alpha}u(x,y)+\bar{\beta}u(x,z),$

(c) $u(x,x)\geqslant 0,$

(d) $u(x,y)=\overline{u(y,x)}.$

Here, for $\alpha$ in $\mathbb{F}$, $\bar{\alpha}=\alpha$ if $\mathbb{F}=\mathbb{R}$ and $\bar{\alpha}$ is the complex conjugate of $\alpha$ if $\mathbb{F}=\mathbb{C}$. If $\alpha\in\mathbb{C}$, the statement that $\alpha\geqslant 0$ means that $\alpha\in\mathbb{R}$ and $\alpha$ is non-negative.

Note that if $\alpha=0$, then property (a) implies that $u(0,y)=u(\alpha\cdot 0,y)=$



<a id="pdf-page-17"></a>
$\alpha u(0,y)=0$ for all $y$ in $\mathcal X$. This and similar reasoning shows that for a semi-inner product $u$,

(e) $u(x,0)=u(0,y)=0$ for all $x,y$ in $\mathcal X$.

In particular, $u(0,0)=0$.

An *inner product* on $\mathcal X$ is a semi-inner product that also satisfies the following:

(f) If $u(x,x)=0$, then $x=0$.

An inner product in this book will be denoted by

$$
\langle x,y\rangle=u(x,y).
$$

There is no universally accepted notation for an inner product and the reader will often see $(x,y)$ and $(x\mid y)$ used in the literature.

**1.2. Example.** Let $\mathcal X$ be the collection of all sequences $\{\alpha_n:n\geqslant 1\}$ of scalars $\alpha_n$ from $\mathbb F$ such that $\alpha_n=0$ for all but a finite number of values of $n$. If addition and scalar multiplication are defined on $\mathcal X$ by

$$
\begin{aligned}
\{\alpha_n\}+\{\beta_n\}&\equiv\{\alpha_n+\beta_n\},\\
\alpha\{\alpha_n\}&=\{\alpha\alpha_n\},
\end{aligned}
$$

then $\mathcal X$ is a vector space over $\mathbb F$.

If $u(\{\alpha_n\},\{\beta_n\})\equiv\sum_{n=1}^{\infty}\alpha_{2n}\overline{\beta}_{2n}$, then $u$ is a semi-inner product that is not an inner product. On the other hand,

$$
\langle\{\alpha_n\},\{\beta_n\}\rangle
=\sum_{n=1}^{\infty}\alpha_n\overline{\beta}_n,
$$

$$
\langle\{\alpha_n\},\{\beta_n\}\rangle
=\sum_{n=1}^{\infty}\frac{1}{n}\alpha_n\overline{\beta}_n,
$$

$$
\langle\{\alpha_n\},\{\beta_n\}\rangle
=\sum_{n=1}^{\infty}n^5\alpha_n\overline{\beta}_n,
$$

all define inner products on $\mathcal X$.

**1.3. Example.** Let $(X,\Omega,\mu)$ be a measure space consisting of a set $X$, a $\sigma$-algebra $\Omega$ of subsets of $X$, and a countably additive measure $\mu$ defined on $\Omega$ with values in the non-negative extended real numbers. If $f$ and $g\in L^2(\mu)\equiv L^2(X,\Omega,\mu)$, then Hölder’s inequality implies $f\overline g\in L^1(\mu)$. If

$$
\langle f,g\rangle=\int f\overline g\,d\mu,
$$

then this defines an inner product on $L^2(\mu)$.

Note that Hölder’s inequality also states that $\left|\int f\overline g\,d\mu\right|\leqslant\left[\int|f|^2\,d\mu\right]^{1/2}\left[\int|g|^2\,d\mu\right]^{1/2}$. This is, in fact, a consequence of the following result on semi-inner products.



<a id="pdf-page-18"></a>
**1.4. The Cauchy–Bunyakowsky–Schwarz Inequality.** *If* $\langle\cdot,\cdot\rangle$ *is a semi-inner product on* $\mathcal{X}$, *then*

$$
|\langle x,y\rangle|^2\leqslant\langle x,x\rangle\langle y,y\rangle
$$

*for all* $x$ *and* $y$ *in* $\mathcal{X}$. *Moreover, equality occurs if and only if there are scalars* $\alpha$ *and* $\beta$, *both not* $0$, *such that* $\langle\beta x+\alpha y,\beta x+\alpha y\rangle=0$.

**Proof.** If $\alpha\in\mathbf{F}$ and $x$ and $y\in\mathcal{X}$, then

$$
\begin{aligned}
0&\leqslant\langle x-\alpha y,x-\alpha y\rangle\\
&=\langle x,x\rangle-\alpha\langle y,x\rangle-\bar{\alpha}\langle x,y\rangle
+|\alpha|^2\langle y,y\rangle.
\end{aligned}
$$

Suppose $\langle y,x\rangle=be^{i\theta}$, $b\geqslant0$, and let $\alpha=e^{-i\theta}t$, $t$ in $\mathbf{R}$. The above inequality becomes

$$
\begin{aligned}
0&\leqslant\langle x,x\rangle-e^{-i\theta}tbe^{i\theta}
-e^{i\theta}tbe^{-i\theta}+t^2\langle y,y\rangle\\
&=\langle x,x\rangle-2bt+t^2\langle y,y\rangle\\
&=c-2bt+at^2\equiv q(t),
\end{aligned}
$$

where $c=\langle x,x\rangle$ and $a=\langle y,y\rangle$. Thus $q(t)$ is a quadratic polynomial in the real variable $t$ and $q(t)\geqslant0$ for all $t$. This implies that the equation $q(t)=0$ has at most one real solution $t$. From the quadratic formula we find that the discriminant is not positive; that is, $0\geqslant4b^2-4ac$. Hence

$$
0\geqslant b^2-ac=|\langle x,y\rangle|^2-\langle x,x\rangle\langle y,y\rangle,
$$

proving the inequality.

The proof of the necessary and sufficient condition for equality is left to the reader. ■

The inequality in (1.4) will be referred to as the CBS inequality.

**1.5. Corollary.** *If* $\langle\cdot,\cdot\rangle$ *is a semi-inner product on* $\mathcal{X}$ *and* $\|x\|\equiv\langle x,x\rangle^{1/2}$ *for all* $x$ *in* $\mathcal{X}$, *then*

(a) $\|x+y\|\leqslant\|x\|+\|y\|$ *for* $x,y$ *in* $\mathcal{X}$,

(b) $\|\alpha x\|=|\alpha|\|x\|$ *for* $\alpha$ *in* $\mathbf{F}$ *and* $x$ *in* $\mathcal{X}$.

*If* $\langle\cdot,\cdot\rangle$ *is an inner product, then*

(c) $\|x\|=0$ *implies* $x=0$.

**Proof.** The proofs of (b) and (c) are left as an exercise. To see (a), note that for $x$ and $y$ in $\mathcal{X}$,

$$
\begin{aligned}
\|x+y\|^2&=\langle x+y,x+y\rangle\\
&=\|x\|^2+\langle y,x\rangle+\langle x,y\rangle+\|y\|^2\\
&=\|x\|^2+2\operatorname{Re}\langle x,y\rangle+\|y\|^2.
\end{aligned}
$$



<a id="pdf-page-19"></a>
By the CBS inequality, $\operatorname{Re}\langle x,y\rangle\leqslant|\langle x,y\rangle|\leqslant\|x\|\|y\|$. Hence,

$$
\begin{aligned}
\|x+y\|^2
&\leqslant \|x\|^2+2\|x\|\|y\|+\|y\|^2\\
&=(\|x\|+\|y\|)^2.
\end{aligned}
$$

The inequality now follows by taking square roots. $\blacksquare$

If $\langle\cdot,\cdot\rangle$ is a semi-inner product on $\mathcal X$ and if $x,y\in\mathcal X$, then as was shown in the preceding proof,

$$
\|x+y\|^2=\|x\|^2+2\operatorname{Re}\langle x,y\rangle+\|y\|^2.
$$

This identity is often called the *polar identity*.

The quantity $\|x\|=\langle x,x\rangle^{1/2}$ for an inner product $\langle\cdot,\cdot\rangle$ is called the *norm* of $x$. If $\mathcal X=\mathbb F^d$ ($\mathbb R^d$ or $\mathbb C^d$) and $\langle\{\alpha_n\},\{\beta_n\}\rangle\equiv\sum_{n=1}^d\alpha_n\overline{\beta_n}$, then the corresponding norm is $\|\{\alpha_n\}\|=[\sum_{n=1}^d|\alpha_n|^2]^{1/2}$.

The virtue of the norm on a vector space $\mathcal X$ is that $d(x,y)=\|x-y\|$ defines a metric on $\mathcal X$ [by (1.5)] so that $\mathcal X$ becomes a metric space. In fact, $d(x,y)=\|x-y\|=\|(x-z)+(z-y)\|\leqslant\|x-z\|+\|z-y\|=d(x,z)+d(z,y)$. The other properties of a metric follow similarly. If $\mathcal X=\mathbb F^d$ and the norm is defined as above, this distance function is the usual Euclidean metric. It is sometimes useful to note that with this metric the inner product becomes a continuous function from $\mathcal X\times\mathcal X$ into $\mathbb R$.

**1.6. Definition.** A *Hilbert space* is a vector space $\mathcal H$ over $\mathbb F$ together with an inner product $\langle\cdot,\cdot\rangle$ such that relative to the metric $d(x,y)=\|x-y\|$ induced by the norm, $\mathcal H$ is a complete metric space.

If $\mathcal H=L^2(\mu)$ and $\langle f,g\rangle=\int f\overline g\,d\mu$, then the associated norm is $\|f\|=[\int|f|^2\,d\mu]^{1/2}$. It is a standard result of measure theory that $L^2(\mu)$ is a Hilbert space. It is also easy to see that $\mathbb F^d$ is a Hilbert space.

**Remark.** The inner products defined on $L^2(\mu)$ and $\mathbb F^d$ are the “usual” ones. Whenever these spaces are discussed these are the inner products referred to. The same is true of the next space.

**1.7. Example.** Let $I$ be any set and let $l^2(I)$ denote the set of all functions $x:I\to\mathbb F$ such that $x(i)=0$ for all but a countable number of $i$ and $\sum_{i\in I}|x(i)|^2<\infty$. For $x$ and $y$ in $l^2(I)$ define

$$
\langle x,y\rangle=\sum_i x(i)\overline{y(i)}.
$$

Then $l^2(I)$ is a Hilbert space (Exercise 2).

If $I=\mathbb N$, $l^2(I)$ is usually denoted by $l^2$. Note that if $\Omega=$ the set of all subsets of $I$ and for $E$ in $\Omega$, $\mu(E)\equiv\infty$ if $E$ is infinite and $\mu(E)=$ the cardinality of $E$ if $E$ is finite, then $l^2(I)$ and $L^2(I,\Omega,\mu)$ are equal.



<a id="pdf-page-20"></a>
Recall that an absolutely continuous function on the unit interval $[0,1]$ has a derivative a.e. on $[0,1]$.

<!-- BEGIN BACKGROUND BG-I.block2 -->
<a id="bg-i-9"></a>
### Definition BG-I.9. Absolute continuity and its integral representation

A function $f:[a,b]\to\mathbb F$ is **absolutely continuous** if for every $\varepsilon>0$ some $\delta>0$ makes $\sum_j|f(b_j)-f(a_j)|<\varepsilon$ whenever finitely many disjoint intervals $(a_j,b_j)$ have total length less than $\delta$. The real-analysis fundamental theorem in its Lebesgue form says equivalently that

$$
f(x)=f(a)+\int_a^x g(t)\,dt\quad(g\in L^1[a,b]);
\qquad f'=g\text{ a.e.}
$$

This equivalence is a recalled foundational theorem from real analysis; its general differentiation-of-measures proof is not reproduced here. In particular, merely having a derivative a.e. does **not** justify reconstructing a function by integrating that derivative. The absolute-continuity hypothesis is essential.

<a id="bg-i-10"></a>
### Lemma BG-I.10. The concrete Hilbert space in Example 1.8

The map $J:L^2(0,1)\to\mathcal H$, $(Jg)(x)=\int_0^xg(t)\,dt$, is the inverse of $D:\mathcal H\to L^2$, $Df=f'$, and both preserve the inner product. Also $|f(t)-f(s)|\leq\|f'\|_2|t-s|^{1/2}$.

**Proof.** Schwarz gives $L^2(0,1)\subset L^1(0,1)$. The recalled fundamental theorem gives $DJg=g$ a.e. and $JDf=f-f(0)=f$. The inner product of $Jg,Jh$ is therefore $\int g\overline h$. Completeness transfers from $L^2$ through this isometry. Finally apply Schwarz to $\int_s^t f'$. To see directly why $Jg$ is absolutely continuous, choose $M$ with $\int_{\{|g|>M\}}|g|<\varepsilon/2$; if a union of disjoint intervals has length less than $\varepsilon/(2M)$, the sum of the integral increments is at most $\varepsilon$. $\square$
<!-- END BACKGROUND BG-I.block2 -->

**1.8. Example.** Let $\mathcal H$ = the collection of all absolutely continuous functions $f:[0,1]\to\mathbb F$ such that $f(0)=0$ and $f'\in L^2(0,1)$. If $\langle f,g\rangle=\int_0^1 f'(t)\overline{g'(t)}\,dt$ for $f$ and $g$ in $\mathcal H$, then $\mathcal H$ is a Hilbert space (Exercise 3).

Suppose $\mathcal X$ is a vector space with an inner product $\langle\cdot,\cdot\rangle$ and the norm is defined by the inner product. What happens if $(\mathcal X,d)$ ($d(x,y)\equiv\|x-y\|$) is not complete?

**1.9. Proposition.** *If $\mathcal X$ is a vector space and $\langle\cdot,\cdot\rangle_{\mathcal X}$ is an inner product on $\mathcal X$ and if $\mathcal H$ is the completion of $\mathcal X$ with respect to the metric induced by the norm on $\mathcal X$, then there is an inner product $\langle\cdot,\cdot\rangle_{\mathcal H}$ on $\mathcal H$ such that $\langle x,y\rangle_{\mathcal H}=\langle x,y\rangle_{\mathcal X}$ for $x$ and $y$ in $\mathcal X$ and the metric on $\mathcal H$ is induced by this inner product. That is, the completion of $\mathcal X$ is a Hilbert space.*

The preceding result says that an incomplete inner product space can be completed to a Hilbert space. It is also true that a Hilbert space over $\mathbb R$ can be imbedded in a complex Hilbert space (see Exercise 7).

This section closes with an example of a Hilbert space from analytic function theory.

<!-- BEGIN BACKGROUND BG-I.block3 -->
<a id="bg-i-11"></a>
### Lemma BG-I.11. Completion and extension of an inner product

The completion of an inner-product space can be constructed from Cauchy sequences, identifying $(x_n)$ and $(y_n)$ when $\|x_n-y_n\|\to0$. On these classes the formula $\langle[x_n],[y_n]\rangle=\lim_n\langle x_n,y_n\rangle$ is well-defined and extends the original inner product.

**Proof.** Cauchy sequences are bounded, and

$$
|\langle x_n,y_n\rangle-\langle x_m,y_m\rangle|
\leq\|x_n-x_m\|\,\|y_n\|+\|x_m\|\,\|y_n-y_m\|.
$$

Thus the scalar limit exists. The same inequality with equivalent representatives proves independence of representatives. Linearity, conjugate symmetry and nonnegativity pass to limits, and zero squared norm means $\|x_n\|\to0$, exactly the zero class. Constant sequences embed the original space densely. For completeness, given a Cauchy sequence of classes $u_k$, choose original vectors $v_k$ with $d(u_k,v_k)<1/k$; $(v_k)$ is Cauchy, defines a class $u$, and $u_k\to u$ by the triangle inequality. This supplies the omitted proof of Proposition 1.9. $\square$

**First complex-analysis reading checkpoint.** Before Definition 1.10 read CA.21–CA.35 in the [complex-analysis background](background-complex-analysis.md#ca-21): holomorphic functions, contour integrals, Cauchy's formula, the mean-value property, and [locally uniform limits](background-complex-analysis.md#ca-35). “Analytic” below is not a synonym for smooth as a function of two real variables.

<a id="bg-i-12"></a>
### Lemma BG-I.12. The local-to-global step in Bergman completeness

Suppose $f_n$ are holomorphic on $G$ and Cauchy in $L^2(G,d\mathrm{Area})$. Then they converge uniformly on each compact $K\subset G$ to a holomorphic function $g$, and their $L^2$ limit represents the same a.e. class as $g$.

**Proof.** Choose $r>0$ with $B(z,r)\subset G$ for every $z\in K$; compactness supplies a positive distance from $K$ to the complement of $G$. The mean-value formula and Schwarz, exactly as in Corollary 1.12, give

$$
\sup_{z\in K}|f_n(z)-f_m(z)|\leq (r\sqrt\pi)^{-1}\|f_n-f_m\|_2.
$$

Lemma BG-I.4 gives uniform convergence on $K$. Pointwise uniqueness makes these limits agree on overlapping compact sets. The locally uniform limit theorem proved in the complex-analysis background makes $g$ holomorphic. Lemma BG-I.7 gives a subsequence converging a.e. to the $L^2$ limit $f$; the same subsequence converges everywhere to $g$, so $f=g$ a.e. No claim that arbitrary $L^2$ convergence is uniform is being made. $\square$
<!-- END BACKGROUND BG-I.block3 -->

**1.10. Definition.** If $G$ is an open subset of the complex plane $\mathbb C$, then $L_a^2(G)$ denotes the collection of all analytic functions $f:G\to\mathbb C$ such that

$$
\iint_G |f(x+iy)|^2\,dx\,dy<\infty.
$$

$L_a^2(G)$ is called the *Bergman space* for $G$.

Several alternatives for the integral with respect to two-dimensional Lebesgue measure will be used. In addition to $\iint_G f(x+iy)\,dx\,dy$ we will also see

$$
\iint_G f \quad\text{and}\quad \int_G f\,d\mathrm{Area}.
$$

Note that $L_a^2(G)\subseteq L^2(\mu)$, where $\mu=\mathrm{Area}|G$, so that $L_a^2(G)$ has a natural inner product and norm from $L^2(\mu)$.

**1.11. Lemma.** *If $f$ is analytic in a neighborhood of $\overline{B}(a;r)$, then*

$$
f(a)=\frac{1}{\pi r^2}\iint_{B(a;r)} f.
$$

[Here $B(a;r)\equiv\{z:|z-a|<r\}$ and $\overline{B}(a;r)\equiv\{z:|z-a|\leq r\}$.]



<a id="pdf-page-21"></a>
**Proof.** By the mean value property, if $0<t\leq r$, $f(a)=(1/2\pi)\int_{-\pi}^{\pi}f(a+te^{i\theta})\,d\theta$. Hence

$$
\begin{aligned}
(\pi r^2)^{-1}\iint_{B(a;r)}f
&=(\pi r^2)^{-1}\int_0^r t\left[\int_{-\pi}^{\pi}f(a+te^{i\theta})\,d\theta\right]dt\\
&=(2/r^2)\int_0^r tf(a)\,dt=f(a).
\end{aligned}
\qquad\blacksquare
$$

**1.12. Corollary.** If $f\in L_a^2(G)$, $a\in G$, and $0<r<\operatorname{dist}(a,\partial G)$, then

$$
|f(a)|\leq \frac{1}{r\sqrt{\pi}}\|f\|_2.
$$

**Proof.** Since $\overline{B}(a;r)\subseteq G$, the preceding lemma and the CBS inequality imply

$$
\begin{aligned}
|f(a)|
&=\frac{1}{\pi r^2}\left|\iint_{B(a;r)}f\cdot 1\right|\\
&\leq\frac{1}{\pi r^2}
\left[\iint_{B(a;r)}|f|^2\right]^{1/2}
\left[\iint_{B(a;r)}1^2\right]^{1/2}\\
&\leq\frac{1}{\pi r^2}\|f\|_2r\sqrt{\pi}.
\end{aligned}
\qquad\blacksquare
$$

**1.13. Proposition.** $L_a^2(G)$ is a Hilbert space.

**Proof.** If $\mu=$ area measure on $G$, then $L^2(\mu)$ is a Hilbert space and $L_a^2(G)\subseteq L^2(\mu)$. So it suffices to show that $L_a^2(G)$ is closed in $L^2(\mu)$. Let $\{f_n\}$ be a sequence in $L_a^2(G)$ and let $f\in L^2(\mu)$ such that $\int|f_n-f|^2\,d\mu\to0$ as $n\to\infty$.

Suppose $\overline{B}(a;r)\subseteq G$ and let $0<\rho<\operatorname{dist}(B(a;r),\partial G)$. By the preceding corollary there is a constant $C$ such that $|f_n(z)-f_m(z)|\leq C\|f_n-f_m\|_2$ for all $n,m$ and for $|z-a|\leq\rho$. Thus $\{f_n\}$ is a uniformly Cauchy sequence on any closed disk in $G$. By standard results from analytic function theory (Montel’s Theorem or Morera’s Theorem, for example), there is an analytic function $g$ on $G$ such that $f_n(z)\to g(z)$ uniformly on compact subsets of $G$. But since $\int|f_n-f|^2\,d\mu\to0$, a result of Riesz implies there is a subsequence $\{f_{n_k}\}$ such that $f_{n_k}(z)\to f(z)$ a.e. $[\mu]$. Thus $f=g$ a.e. $[\mu]$ and so $f\in L_a^2(G)$. $\blacksquare$

## Exercises

1. Verify the statements made in Example 1.2.
2. Verify that $l^2(I)$ (Example 1.7) is a Hilbert space.
3. Show that the space $\mathcal H$ in Example 1.8 is a Hilbert space.
4. Describe the Hilbert spaces obtained by completing the space $\mathcal X$ in Example 1.2 with respect to the norm defined by each of the inner products given there.



<a id="pdf-page-22"></a>
5. (A variation on Example 1.8) Let $n\geq 2$ and let $\mathcal H =$ the collection of all function $f:[0,1]\to\mathbb F$ such that (a) $f(0)=0$; (b) for $1\leq k\leq n-1$, $f^{(k)}(t)$ exists for all $t$ in $[0,1]$ and $f^{(k)}$ is continuous on $[0,1]$; (c) $f^{(n-1)}$ is absolutely continuous and $f^{(n)}\in L^2(0,1)$. For $f$ and $g$ in $\mathcal H$, define

   $$
   \langle f,g\rangle=\sum_{k=1}^{n}\int_0^1 f^{(k)}(t)\overline{g^{(k)}(t)}\,dt.
   $$

   Show that $\mathcal H$ is a Hilbert space.

6. Let $u$ be a semi-inner product on $\mathcal X$ and put $\mathcal N=\{x\in\mathcal X:u(x,x)=0\}$.

   (a) Show that $\mathcal N$ is a linear subspace of $\mathcal X$.

   (b) Show that if

   $$
   \langle x+\mathcal N,y+\mathcal N\rangle\equiv u(x,y)
   $$

   for all $x+\mathcal N$ and $y+\mathcal N$ in the quotient space $\mathcal X/\mathcal N$, then $\langle\cdot,\cdot\rangle$ is a well-defined inner product on $\mathcal X/\mathcal N$.

7. Let $\mathcal H$ be a Hilbert space over $\mathbb R$ and show that there is a Hilbert space $\mathcal K$ over $\mathbb C$ and a map $U:\mathcal H\to\mathcal K$ such that (a) $U$ is linear; (b) $\langle Uh_1,Uh_2\rangle=\langle h_1,h_2\rangle$ for all $h_1,h_2$ in $\mathcal H$; (c) for any $k$ in $\mathcal K$ there are unique $h_1,h_2$ in $\mathcal H$ such that $k=Uh_1+iUh_2$. ($\mathcal K$ is called the *complexification* of $\mathcal H$.)

8. If $G=\{z\in\mathbb C:0<|z|<1\}$ show that every $f$ in $L_a^2(G)$ has a removable singularity at $z=0$.

9. Which functions are in $L_a^2(\mathbb C)$?

10. Let $G$ be an open subset of $\mathbb C$ and show that if $a\in G$, then $\{f\in L_a^2(G):f(a)=0\}$ is closed in $L_a^2(G)$.

11. If $\{h_n\}$ is a sequence in a Hilbert space $\mathcal H$ such that $\sum_n\|h_n\|<\infty$, then show that $\sum_{n=1}^{\infty}h_n$ converges in $\mathcal H$.

## §2. Orthogonality

<!-- BEGIN BACKGROUND BG-I.block4 -->
<a id="bg-i-13"></a>
### Lemma BG-I.13. Closed spans and continuity of inner products

For a subset $A$ of an inner-product space, $\overline{\operatorname{span}A}$ is the smallest closed linear subspace containing $A$. In a Hilbert space, $A^\perp$ is closed and $A^\perp=(\overline{\operatorname{span}A})^\perp$.

**Proof.** Addition and scalar multiplication preserve limits by the triangle inequality, so the closure of a linear space is linear. Any closed linear space containing $A$ must contain its finite linear combinations and their limits. For fixed $a$, $|\langle x,a\rangle-\langle y,a\rangle|\leq\|x-y\|\|a\|$; hence its zero set is closed. Intersecting these zero sets proves closedness of $A^\perp$. Orthogonality to $A$ first extends to finite combinations, then to their limits by this estimate. The projection theorem below now gives $(A^\perp)^\perp=\overline{\operatorname{span}A}$: if $x=m+n$ with $m$ in that closed span and $n$ perpendicular to it, membership in $(A^\perp)^\perp$ forces $\|n\|^2=0$. This also proves the density criterion in Corollary 2.11. $\square$

<a id="bg-i-14"></a>
### Lemma BG-I.14. Why minimizing sequences exist but minimizers need proof

For nonempty $K$ and $d=\inf_{k\in K}\|h-k\|$, choose $k_n\in K$ with $d\leq\|h-k_n\|<d+1/n$. If this sequence converges to a point of $K$, that point realizes the distance.

**Proof.** Failure to find $k_n$ would make $d+1/n$ a lower bound larger than the infimum. The reverse triangle inequality $|\|h-k_n\|-\|h-k\||\leq\|k_n-k\|$ proves the second assertion. Neither boundedness nor closedness alone makes a sequence converge in infinite dimensions: distinct orthonormal vectors have mutual distance $\sqrt2$. The parallelogram argument below supplies the missing Cauchy property, convexity permits midpoint comparisons, and closedness keeps the eventual limit in $K$. $\square$
<!-- END BACKGROUND BG-I.block4 -->

The greatest advantage of a Hilbert space is its underlying concept of orthogonality.

**2.1. Definition.** If $\mathcal H$ is a Hilbert space and $f,g\in\mathcal H$, then $f$ and $g$ are *orthogonal* if $\langle f,g\rangle=0$. In symbols, $f\perp g$. If $A,B\subseteq\mathcal H$, then $A\perp B$ if $f\perp g$ for every $f$ in $A$ and $g$ in $B$.

If $\mathcal H=\mathbb R^2$, this is the correct concept. Two non-zero vectors in $\mathbb R^2$ are orthogonal precisely when the angle between them is $\pi/2$.

**2.2. The Pythagorean Theorem.** *If $f_1,f_2,\ldots,f_n$ are pairwise orthogonal vectors in $\mathcal H$, then*

$$
\|f_1+f_2+\cdots+f_n\|^2
=\|f_1\|^2+\|f_2\|^2+\cdots+\|f_n\|^2.
$$



<a id="pdf-page-23"></a>
**Proof.** If $f_1\perp f_2$, then

$$
\|f_1+f_2\|^2
=\langle f_1+f_2,f_1+f_2\rangle
=\|f_1\|^2+2\operatorname{Re}\langle f_1,f_2\rangle+\|f_2\|^2
$$

by the polar identity. Since $f_1\perp f_2$, this implies the result for $n=2$. The remainder of the proof proceeds by induction and is left to the reader. ■

Note that if $f\perp g$, then $f\perp -g$, so $\|f-g\|^2=\|f\|^2+\|g\|^2$. The next result is an easy consequence of the Pythagorean Theorem if $f$ and $g$ are orthogonal, but this assumption is not needed for its conclusion.

**2.3. Parallelogram Law.** *If $\mathcal H$ is a Hilbert space and $f$ and $g\in\mathcal H$, then*

$$
\|f+g\|^2+\|f-g\|^2=2(\|f\|^2+\|g\|^2).
$$

**Proof.** For any $f$ and $g$ in $\mathcal H$ the polar identity implies

$$
\begin{aligned}
\|f+g\|^2&=\|f\|^2+2\operatorname{Re}\langle f,g\rangle+\|g\|^2,\\
\|f-g\|^2&=\|f\|^2-2\operatorname{Re}\langle f,g\rangle+\|g\|^2.
\end{aligned}
$$

Now add. ■

The next property of a Hilbert space is truly pivotal. But first we need a geometric concept valid for any vector space over $\mathbb F$.

**2.4. Definition.** If $\mathcal X$ is any vector space over $\mathbb F$ and $A\subseteq\mathcal X$, then $A$ is a *convex set* if for any $x$ and $y$ in $A$ and $0\leq t\leq 1$, $tx+(1-t)y\in A$.

Note that $\{tx+(1-t)y:0\leq t\leq 1\}$ is the straight-line segment joining $x$ and $y$. So a convex set is a set $A$ such that if $x$ and $y\in A$, the entire line segment joining $x$ and $y$ is contained in $A$.

If $\mathcal X$ is a vector space, then any linear subspace in $\mathcal X$ is a convex set. A singleton set is convex. The intersection of any collection of convex sets is convex. If $\mathcal H$ is a Hilbert space, then every open ball $B(f;r)=\{g\in\mathcal H:\|f-g\|<r\}$ is convex, as is every closed ball.

**2.5. Theorem.** *If $\mathcal H$ is a Hilbert space, $K$ is a closed convex nonempty subset of $\mathcal H$, and $h\in\mathcal H$, then there is a unique point $k_0$ in $K$ such that*

$$
\|h-k_0\|=\operatorname{dist}(h,K)\equiv\inf\{\|h-k\|:k\in K\}.
$$

**Proof.** By considering $K-h\equiv\{k-h:k\in K\}$ instead of $K$, it suffices to assume that $h=0$. (Verify!) So we want to show that there is a unique vector $k_0$ in $K$ such that

$$
\|k_0\|=\operatorname{dist}(0,K)\equiv\inf\{\|k\|:k\in K\}.
$$

Let $d=\operatorname{dist}(0,K)$. By definition, there is a sequence $\{k_n\}$ in $K$ such that $\|k_n\|\to d$. Now the Parallelogram Law implies that

$$
\left\|\frac{k_n-k_m}{2}\right\|^2
=\frac12\bigl(\|k_n\|^2+\|k_m\|^2\bigr)
-\left\|\frac{k_n+k_m}{2}\right\|^2.
$$



<a id="pdf-page-24"></a>
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



<a id="pdf-page-25"></a>
If $A\subseteq\mathcal{H}$, Let $A^\perp\equiv\{f\in\mathcal{H}:f\perp g\text{ for all }g\text{ in }A\}$. It is easy to see that $A^\perp$ is a closed linear subspace of $\mathcal{H}$.

Note that Theorem 2.6, together with the uniqueness statement in Theorem 2.5, shows that if $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$ and $h\in\mathcal{H}$, then there is a unique element $f_0$ in $\mathcal{M}$ such that $h-f_0\in\mathcal{M}^\perp$. Thus a function $P:\mathcal{H}\to\mathcal{M}$ can be defined by $Ph=f_0$.

**2.7. Theorem.** If $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$ and $h\in\mathcal{H}$, let $Ph$ be the unique point in $\mathcal{M}$ such that $h-Ph\perp\mathcal{M}$. Then

(a) $P$ is a linear transformation on $\mathcal{H}$,

(b) $\|Ph\|\leq\|h\|$ for every $h$ in $\mathcal{H}$,

(c) $P^2=P$ (here $P^2$ means the composition of $P$ with itself),

(d) $\ker P=\mathcal{M}^\perp$ and $\operatorname{ran}P=\mathcal{M}$.

**Proof.** Keep in mind that for every $h$ in $\mathcal{H}$, $h-Ph\in\mathcal{M}^\perp$ and $\|h-Ph\|=\operatorname{dist}(h,\mathcal{M})$.

(a) Let $h_1,h_2\in\mathcal{H}$ and $\alpha_1,\alpha_2\in\mathbb{F}$. If $f\in\mathcal{M}$, then
$$
\left\langle[\alpha_1h_1+\alpha_2h_2]-[\alpha_1Ph_1+\alpha_2Ph_2],f\right\rangle
=\alpha_1\langle h_1-Ph_1,f\rangle+\alpha_2\langle h_2-Ph_2,f\rangle=0.
$$
By the uniqueness statement of (2.6), $P(\alpha_1h_1+\alpha_2h_2)=\alpha_1Ph_1+\alpha_2Ph_2$.

(b) If $h\in\mathcal{H}$, then $h=(h-Ph)+Ph$, $Ph\in\mathcal{M}$, and $h-Ph\in\mathcal{M}^\perp$. Thus
$$
\|h\|^2=\|h-Ph\|^2+\|Ph\|^2\geq\|Ph\|^2.
$$

(c) If $f\in\mathcal{M}$, then $Pf=f$. For any $h$ in $\mathcal{H}$, $Ph\in\mathcal{M}$; hence $P^2h\equiv P(Ph)=Ph$. That is, $P^2=P$.

(d) If $Ph=0$, then $h=h-Ph\in\mathcal{M}^\perp$. Conversely, if $h\in\mathcal{M}^\perp$, then $0$ is the unique vector in $\mathcal{M}$ such that $h-0=h\perp\mathcal{M}$. Therefore $Ph=0$. That $\operatorname{ran}P=\mathcal{M}$ is clear. ■

**2.8. Definition.** If $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$ and $P$ is the linear map defined in the preceding theorem, then $P$ is called the *orthogonal projection* of $\mathcal{H}$ onto $\mathcal{M}$. If we wish to show this dependence of $P$ on $\mathcal{M}$, we will denote the orthogonal projection of $\mathcal{H}$ onto $\mathcal{M}$ by $P_{\mathcal{M}}$.

It also seems appropriate to introduce the notation $\mathcal{M}\leq\mathcal{H}$ to signify that $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$. We will use the term *linear manifold* to designate a linear subspace of $\mathcal{H}$ that is not necessarily closed. A *linear subspace* of $\mathcal{H}$ will always mean a closed linear subspace.

**2.9. Corollary.** If $\mathcal{M}\leq\mathcal{H}$, then $(\mathcal{M}^\perp)^\perp=\mathcal{M}$.

**Proof.** If $I$ is used to designate the identity operator on $\mathcal{H}$ (viz., $Ih=h$) and $P=P_{\mathcal{M}}$, then $I-P$ is the orthogonal projection of $\mathcal{H}$ onto $\mathcal{M}^\perp$ (Exercise 2). By part (d) of the preceding theorem, $(\mathcal{M}^\perp)^\perp=\ker(I-P)$. But $0=(I-P)h$ iff $h=Ph$. Thus $(\mathcal{M}^\perp)^\perp=\ker(I-P)=\operatorname{ran}P=\mathcal{M}$. ■

**2.10. Corollary.** If $A\subseteq\mathcal{H}$, then $(A^\perp)^\perp$ is the closed linear span of $A$ in $\mathcal{H}$.



<a id="pdf-page-26"></a>
The proof is left to the reader; see Exercise 4 for a discussion of the term “closed linear span.”

**2.11. Corollary.** *If $\mathcal Y$ is a linear manifold in $\mathcal H$, then $\mathcal Y$ is dense in $\mathcal H$ iff $\mathcal Y^\perp=(0)$.*

**Proof.** Exercise.

## Exercises

1. Let $\mathcal H$ be a Hilbert space and suppose $f$ and $g$ are linearly independent vectors in $\mathcal H$ with $\|f\|=\|g\|=1$. Show that $\|tf+(1-t)g\|<1$ for $0<t<1$. What does this say about $\{h\in\mathcal H:\|h\|\leq 1\}$?

2. If $\mathcal M\leq\mathcal H$ and $P=P_{\mathcal M}$, show that $I-P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M^\perp$.

3. If $\mathcal M\leq\mathcal H$, show that $\mathcal M\cap\mathcal M^\perp=(0)$ and every $h$ in $\mathcal H$ can be written as $h=f+g$ where $f\in\mathcal M$ and $g\in\mathcal M^\perp$. If $\mathcal M+\mathcal M^\perp\equiv\{(f,g):f\in\mathcal M,\ g\in\mathcal M^\perp\}$ and $T:\mathcal M+\mathcal M^\perp\to\mathcal H$ is defined by $T(f,g)=f+g$, show that $T$ is a linear bijection and a homeomorphism if $\mathcal M+\mathcal M^\perp$ is given the product topology. (This is usually phrased by stating the $\mathcal M$ and $\mathcal M^\perp$ are *topologically complementary* in $\mathcal H$.)

4. If $A\subseteq\mathcal H$, let $\vee A\equiv$ the intersection of all closed linear subspaces of $\mathcal H$ that contain $A$. $\vee A$ is called the *closed linear span* of $A$. Prove the following:

   (a) $\vee A\leq\mathcal H$ and $\vee A$ is the smallest closed linear subspace of $\mathcal H$ that contains $A$.

   (b) $\vee A=$ the closure of $\left\{\sum_{k=1}^{n}\alpha_k f_k:n\geq 1,\ \alpha_k\in\mathbb F,\ f_k\in A\right\}$.

5. Prove Corollary 2.10.

6. Prove Corollary 2.11.

## §3. The Riesz Representation Theorem

The title of this section is somewhat ambiguous as there are at least two Riesz Representation Theorems. There is one so-called theorem that represents bounded linear functionals on the space of continuous functions on a compact Hausdorff space. That theorem will be discussed later in this book. The present section deals with the representation of certain linear functionals on Hilbert space. But first we have a few preliminaries to dispose of.

**3.1. Proposition.** *Let $\mathcal H$ be a Hilbert space and $L:\mathcal H\to\mathbb F$ a linear functional. The following statements are equivalent.*

(a) $L$ is continuous.

(b) $L$ is continuous at $0$.

(c) $L$ is continuous at some point.

(d) There is a constant $c>0$ such that $|L(h)|\leq c\|h\|$ for every $h$ in $\mathcal H$.

**Proof.** It is clear that $(a)\Rightarrow(b)\Rightarrow(c)$ and $(d)\Rightarrow(b)$. Let’s show that $(c)\Rightarrow(a)$ and $(b)\Rightarrow(d)$.



<a id="pdf-page-27"></a>
(c) $\Rightarrow$ (a): Suppose $L$ is continuous at $h_0$ and $h$ is any point in $\mathcal H$. If $h_n\to h$ in $\mathcal H$, then $h_n-h+h_0\to h_0$. By assumption,
$L(h_0)=\lim[L(h_n-h+h_0)]=\lim[L(h_n)-L(h)+L(h_0)]=\lim L(h_n)-L(h)+L(h_0)$. Hence $L(h)=\lim L(h_n)$.

(b) $\Rightarrow$ (d): The definition of continuity at $0$ implies that $L^{-1}(\{\alpha\in\mathbb F:|\alpha|<1\})$ contains an open ball about $0$. So there is a $\delta>0$ such that $B(0;\delta)\subseteq L^{-1}(\{\alpha\in\mathbb F:|\alpha|<1\})$. That is, $\|h\|<\delta$ implies $|L(h)|<1$. If $h$ is an arbitrary element of $\mathcal H$ and $\varepsilon>0$, then $\|\delta(\|h\|+\varepsilon)^{-1}h\|<\delta$. Hence

$$
1>\left|L\left[\frac{\delta h}{\|h\|+\varepsilon}\right]\right|
=\frac{\delta}{\|h\|+\varepsilon}|L(h)|;
$$

thus

$$
|L(h)|<\frac{1}{\delta}(\|h\|+\varepsilon).
$$

Letting $\varepsilon\to0$ we see that (d) holds with $c=1/\delta$. $\blacksquare$

**3.2. Definition.** A *bounded linear functional* $L$ on $\mathcal H$ is a linear functional for which there is a constant $c>0$ such that $|L(h)|\leqslant c\|h\|$ for all $h$ in $\mathcal H$. In light of the preceding proposition, a linear functional is bounded if and only if it is continuous.

For a bounded linear functional $L:\mathcal H\to\mathbb F$, define

$$
\|L\|=\sup\{|L(h)|:\|h\|\leqslant1\}.
$$

Note that by definition, $\|L\|<\infty$; $\|L\|$ is called the *norm* of $L$.

**3.3. Proposition.** *If $L$ is a bounded linear functional, then*

$$
\begin{aligned}
\|L\|&=\sup\{|L(h)|:\|h\|=1\}\\
&=\sup\{|L(h)|/\|h\|:h\in\mathcal H,\ h\ne0\}\\
&=\inf\{c>0:|L(h)|\leqslant c\|h\|,\ h\text{ in }\mathcal H\}.
\end{aligned}
$$

*Also, $|L(h)|\leqslant\|L\|\|h\|$ for every $h$ in $\mathcal H$.*

**Proof.** Let $\alpha=\inf\{c>0:|L(h)|\leqslant c\|h\|,\ h\text{ in }\mathcal H\}$. It will be shown that $\|L\|=\alpha$; the remaining equalities are left as an exercise. If $\varepsilon>0$, then the definition of $\|L\|$ shows that $|L((\|h\|+\varepsilon)^{-1}h)|\leqslant\|L\|$. Hence $|L(h)|\leqslant\|L\|(\|h\|+\varepsilon)$. Letting $\varepsilon\to0$ shows that $|L(h)|\leqslant\|L\|\|h\|$ for all $h$. So the definition of $\alpha$ shows that $\alpha\leqslant\|L\|$. On the other hand, if $|L(h)|\leqslant c\|h\|$ for all $h$, then $\|L\|\leqslant c$. Hence $\|L\|\leqslant\alpha$. $\blacksquare$

Fix an $h_0$ in $\mathcal H$ and define $L:\mathcal H\to\mathbb F$ by $L(h)=\langle h,h_0\rangle$. It is easy to see that $L$ is linear. Also, the CBS inequality gives that $|L(h)|=|\langle h,h_0\rangle|\leqslant\|h\|\|h_0\|$. So $L$ is bounded and $\|L\|\leqslant\|h_0\|$. In fact, $L(h_0/\|h_0\|)=\langle h_0/\|h_0\|,h_0\rangle=\|h_0\|$, so that $\|L\|=\|h_0\|$. The main result of this section provides a converse to these observations.



<a id="pdf-page-28"></a>
**3.4. The Riesz Representation Theorem.** If $L:\mathcal H\to\mathbb F$ is a bounded linear functional, then there is a unique vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$. Moreover, $\|L\|=\|h_0\|$.

**Proof.** Let $\mathcal M=\ker L$. Because $L$ is continuous $\mathcal M$ is a closed linear subspace of $\mathcal H$. Since we may assume that $\mathcal M\ne\mathcal H$, $\mathcal M^\perp\ne(0)$. Hence there is a vector $f_0$ in $\mathcal M^\perp$ such that $L(f_0)=1$. Now if $h\in\mathcal H$ and $\alpha=L(h)$, then $L(h-\alpha f_0)=L(h)-\alpha=0$; so $h-L(h)f_0\in\mathcal M$. Thus

$$
\begin{aligned}
0&=\langle h-L(h)f_0,f_0\rangle\\
 &=\langle h,f_0\rangle-L(h)\|f_0\|^2.
\end{aligned}
$$

So if $h_0=\|f_0\|^{-2}f_0$, $L(h)=\langle h,h_0\rangle$ for all $h$ in $\mathcal H$.

If $h_0'\in\mathcal H$ such that $\langle h,h_0\rangle=\langle h,h_0'\rangle$ for all $h$, then $h_0-h_0'\perp\mathcal H$. In particular, $h_0-h_0'\perp h_0-h_0'$ and so $h_0'=h_0$. The fact that $\|L\|=\|h_0\|$ was shown in the discussion preceding the theorem. ■

**3.5. Corollary.** If $(X,\Omega,\mu)$ is a measure space and $F:L^2(\mu)\to\mathbb F$ is a bounded linear functional, then there is a unique $h_0$ in $L^2(\mu)$ such that

$$
F(h)=\int h\overline{h_0}\,d\mu
$$

for every $h$ in $L^2(\mu)$.

Of course the preceding corollary is a special case of the theorem on representing bounded linear functionals on $L^p(\mu)$, $1\leq p<\infty$. But it is interesting to note that it is a consequence of the result for Hilbert space [and the result that $L^2(\mu)$ is a Hilbert space].

## EXERCISES

1. Prove Proposition 3.3.

2. Let $\mathcal H=\ell^2(\mathbb N)$. If $N\geq1$ and $L:\mathcal H\to\mathbb F$ is defined by $L(\{\alpha_n\})=\alpha_N$, find the vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$.

3. Let $\mathcal H=\ell^2(\mathbb N\cup\{0\})$. (a) Show that if $\{\alpha_n\}\in\mathcal H$, then the power series $\sum_{n=0}^{\infty}\alpha_n z^n$ has radius of convergence $\geq1$. (b) If $|\lambda|<1$ and $L:\mathcal H\to\mathbb F$ is defined by $L(\{\alpha_n\})=\sum_{n=0}^{\infty}\alpha_n\lambda^n$, find the vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$. (c) What is the norm of the linear functional $L$ defined in (b)?

4. With the notation as in Exercise 3, define $L:\mathcal H\to\mathbb F$ by $L(\{\alpha_n\})=\sum_{n=1}^{\infty}n\alpha_n\lambda^{n-1}$, where $|\lambda|<1$. Find a vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$.

5. Let $\mathcal H$ be the Hilbert space described in Example 1.8. If $0<t\leq1$, define $L:\mathcal H\to\mathbb F$ by $L(h)=h(t)$. Show that $L$ is a bounded linear functional, find $\|L\|$, and find the vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for all $h$ in $\mathcal H$.

6. Let $\mathcal H=L^2(0,1)$ and let $C^{(1)}$ be the set of all continuous functions on $[0,1]$ that have a continuous derivative. Let $t\in[0,1]$ and define $L:C^{(1)}\to\mathbb F$ by $L(h)=h'(t)$. Show that there is no bounded linear functional on $\mathcal H$ that agrees with $L$ on $C^{(1)}$.



<a id="pdf-page-29"></a>
# §4. Orthonormal Sets of Vectors and Bases

<!-- BEGIN BACKGROUND BG-I.block5 -->
<a id="bg-i-15"></a>
### Definition BG-I.15. Zorn's principle and the meaning of maximal

A partial order is reflexive, antisymmetric and transitive. A **chain** is a subset whose members are pairwise comparable. An upper bound of a chain lies above every member; a **maximal** element has no strictly larger element, but need not lie above every element of the partially ordered set. Zorn's lemma states that a nonempty partially ordered set in which every chain has an upper bound has a maximal element. We use it as the usual form of the axiom of choice, rather than as a theorem of analysis requiring proof here.

<a id="bg-i-16"></a>
### Lemma BG-I.16. The maximal-orthonormal-set argument

Every orthonormal set is contained in a maximal orthonormal set.

**Proof.** Order the orthonormal sets containing the given set by inclusion. This collection is nonempty. The union of a chain is orthonormal: two of its vectors belong to two members of the chain, and the larger of these contains both. Thus each chain has an upper bound in the collection, and Zorn's principle applies. An orthonormal basis here permits infinite norm-convergent expansions; it is not the finite-expansion Hamel basis of linear algebra. $\square$
<!-- END BACKGROUND BG-I.block5 -->

It will be shown in this section that, as in Euclidean space, each Hilbert space can be coordinatized. The vehicle for introducing the coordinates is an orthonormal basis. The corresponding vectors in $\mathbb{F}^{d}$ are the vectors $\{e_{1},e_{2},\ldots,e_{d}\}$, where $e_{k}$ is the $d$-tuple having a 1 in the $k$th place and zeros elsewhere.

**4.1. Definition.** An *orthonormal* subset of a Hilbert space $\mathcal{H}$ is a subset $\mathcal{E}$ having the properties: (a) for $e$ in $\mathcal{E}$, $\|e\|=1$; (b) if $e_{1},e_{2}\in\mathcal{E}$ and $e_{1}\ne e_{2}$, then $e_{1}\perp e_{2}$.

A *basis* for $\mathcal{H}$ is a maximal orthonormal set.

Every vector space has a Hamel basis (a maximal linearly independent set). The term “basis” for a Hilbert space is defined as above and it relates to the inner product on $\mathcal{H}$. For an infinite-dimensional Hilbert space, a basis is never a Hamel basis. This is not obvious, but the reader will be able to see this after understanding several facts about bases.

**4.2. Proposition.** *If $\mathcal{E}$ is an orthonormal set in $\mathcal{H}$, then there is a basis for $\mathcal{H}$ that contains $\mathcal{E}$.*

The proof of this proposition is a straightforward application of Zorn’s Lemma and is left to the reader.

**4.3. Example.** Let $\mathcal{H}=L_{\mathbb{C}}^{2}[0,2\pi]$ and for $n$ in $\mathbb{Z}$ define $e_{n}$ in $\mathcal{H}$ by $e_{n}(t)=(2\pi)^{-1/2}\exp(int)$. Then $\{e_{n}:n\in\mathbb{Z}\}$ is an orthonormal set in $\mathcal{H}$. (Here $L_{\mathbb{C}}^{2}[0,2\pi]$ is the space of complex-valued square integrable functions.)

It is also true that the set in (4.3) is a basis, but this is best proved after a bit of theory.

**4.4. Example.** If $\mathcal{H}=\mathbb{F}^{d}$ and for $1\leq k\leq d$, $e_{k}=$ the $d$-tuple with 1 in the $k$th place and zeros elsewhere, then $\{e_{1},\ldots,e_{d}\}$ is a basis for $\mathcal{H}$.

**4.5. Example.** Let $\mathcal{H}=l^{2}(I)$ as in Example 1.7. For each $i$ in $I$ define $e_{i}$ in $\mathcal{H}$ by $e_{i}(i)=1$ and $e_{i}(j)=0$ for $j\ne i$. Then $\{e_{i}:i\in I\}$ is a basis.

The proof of the next result is left as an exercise (see Exercise 5). It is very useful but the proof is not difficult.

**4.6. The Gram–Schmidt Orthogonalization Process.** *If $\mathcal{H}$ is a Hilbert space and $\{h_{n}:n\in\mathbb{N}\}$ is a linearly independent subset of $\mathcal{H}$, then there is an orthonormal set $\{e_{n}:n\in\mathbb{N}\}$ such that for every $n$, the linear space of $\{e_{1},\ldots,e_{n}\}$ equals the linear span of $\{h_{1},\ldots,h_{n}\}$.*

Remember that $\bigvee A$ is the closed linear span of $A$ (Exercise 2.4).



<a id="pdf-page-30"></a>
**4.7. Proposition.** Let $\{e_1,\ldots,e_n\}$ be an orthonormal set in $\mathcal H$ and let $\mathcal M=\bigvee\{e_1,\ldots,e_n\}$. If $P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M$, then

$$
Ph=\sum_{k=1}^{n}\langle h,e_k\rangle e_k
$$

for all $h$ in $\mathcal H$.

**Proof.** Let $Qh=\sum_{k=1}^{n}\langle h,e_k\rangle e_k$. If $1\leq j\leq n$, then
$\langle Qh,e_j\rangle=\sum_{k=1}^{n}\langle h,e_k\rangle\langle e_k,e_j\rangle=\langle h,e_j\rangle$ since $e_k\perp e_j$ for $k\neq j$. Thus $\langle h-Qh,e_j\rangle=0$ for $1\leq j\leq n$. That is, $h-Qh\perp\mathcal M$ for every $h$ in $\mathcal H$. Since $Qh$ is clearly a vector in $\mathcal M$, $Qh$ is the unique vector $h_0$ in $\mathcal M$ such that $h-h_0\perp\mathcal M$ (2.6). Hence $Qh=Ph$ for every $h$ in $\mathcal H$. $\blacksquare$

**4.8. Bessel’s Inequality.** If $\{e_n:n\in\mathbb N\}$ is an orthonormal set and $h\in\mathcal H$, then

$$
\sum_{n=1}^{\infty}|\langle h,e_n\rangle|^2\leq\|h\|^2.
$$

**Proof.** Let $h_n=h-\sum_{k=1}^{n}\langle h,e_k\rangle e_k$. Then $h_n\perp e_k$ for $1\leq k\leq n$ (Why?) By the Pythagorean Theorem,

$$
\begin{aligned}
\|h\|^2
&=\|h_n\|^2+\left\|\sum_{k=1}^{n}\langle h,e_k\rangle e_k\right\|^2\\
&=\|h_n\|^2+\sum_{k=1}^{n}|\langle h,e_k\rangle|^2\\
&\geq\sum_{k=1}^{n}|\langle h,e_k\rangle|^2.
\end{aligned}
$$

Since $n$ was arbitrary, the result is proved. $\blacksquare$

**4.9. Corollary.** If $\mathscr E$ is an orthonormal set in $\mathcal H$ and $h\in\mathcal H$, then $\langle h,e\rangle\neq0$ for at most a countable number of vectors $e$ in $\mathscr E$.

**Proof.** For each $n\geq1$ let $\mathscr E_n=\{e\in\mathscr E:|\langle h,e\rangle|\geq1/n\}$. By Bessel’s Inequality, $\mathscr E_n$ is finite. But $\bigcup_{n=1}^{\infty}\mathscr E_n=\{e\in\mathscr E:\langle h,e\rangle\neq0\}$. $\blacksquare$

**4.10. Corollary.** If $\mathscr E$ is an orthonormal set and $h\in\mathcal H$, then

$$
\sum_{e\in\mathscr E}|\langle h,e\rangle|^2\leq\|h\|^2.
$$

This last corollary is just Bessel’s Inequality together with the fact (4.9) that at most a countable number of the terms in the sum differ from zero.

Actually, the sum that appears in (4.10) can be given a better interpretation—a mathematically precise one that will be useful later. The question is, what is meant by $\sum\{h_i:i\in I\}$ if $h_i\in\mathcal H$ and $I$ is an infinite, possibly uncountable, set? Let $\mathscr F$ be the collection of all finite subsets of $I$ and order



<a id="pdf-page-31"></a>
$\mathcal{F}$ by inclusion, so $\mathcal{F}$ becomes a directed set. For each $F$ in $\mathcal{F}$, define

$$
h_F=\sum\{h_i:i\in F\}.
$$

Since this is a finite sum, $h_F$ is a well-defined element of $\mathcal{H}$. Now $\{h_F:F\in\mathcal{F}\}$ is a net in $\mathcal{H}$.

**4.11. Definition.** With the notation above, the sum $\sum\{h_i:i\in I\}$ converges if the net $\{h_F:F\in\mathcal{F}\}$ converges; the value of the sum is the limit of the net.

If $\mathcal{H}=\mathbb{F}$, the definition above gives meaning to an uncountable sum of scalars. Now Corollary 4.10 can be given its precise meaning; namely, $\sum\{|\langle h,e\rangle|^2:e\in\mathcal{E}\}$ converges and the value $\leq\|h\|^2$ (Exercise 9).

If the set $I$ in Definition 4.11 is countable, then this definition of convergent sum is not the usual one. That is, if $\{h_n\}$ is a sequence in $\mathcal{H}$, then the convergence of $\sum\{h_n:n\in\mathbb{N}\}$ is not equivalent to the convergence of $\sum_{n=1}^{\infty}h_n$. The former concept of convergence is that defined in (4.11) while the latter means that the sequence $\left\{\sum_{k=1}^{n}h_k\right\}_{n=1}^{\infty}$ converges. Even if $\mathcal{H}=\mathbb{F}$, these concepts do not coincide (see Exercise 12). If, however, $\sum\{h_n:n\in\mathbb{N}\}$ converges, then $\sum_{n=1}^{\infty}h_n$ converges (Exercise 10). Also see Exercise 11.

**4.12. Lemma.** *If $\mathcal{E}$ is an orthonormal set and $h\in\mathcal{H}$, then*

$$
\sum\{\langle h,e\rangle e:e\in\mathcal{E}\}
$$

*converges in $\mathcal{H}$.*

**Proof.** By (4.9), there are vectors $e_1,e_2,\ldots$ in $\mathcal{E}$ such that $\{e\in\mathcal{E}:\langle h,e\rangle\neq 0\}=\{e_1,e_2,\ldots\}$. We also know that $\sum_{n=1}^{\infty}|\langle h,e_n\rangle|^2\leq\|h\|^2<\infty$. So if $\varepsilon>0$, there is an $N$ such that $\sum_{n=N}^{\infty}|\langle h,e_n\rangle|^2<\varepsilon^2$. Let $F_0=\{e_1,\ldots,e_{N-1}\}$ and let $\mathcal{F}=$ all the finite subsets of $\mathcal{E}$. For $F$ in $\mathcal{F}$ define $h_F\equiv\sum\{\langle h,e\rangle e:e\in F\}$. If $F$ and $G\in\mathcal{F}$ and both contain $F_0$, then

$$
\begin{aligned}
\|h_F-h_G\|^2
&=\sum\{|\langle h,e\rangle|^2:e\in(F\setminus G)\cup(G\setminus F)\}\\
&\leq\sum_{n=N}^{\infty}|\langle h,e_n\rangle|^2\\
&<\varepsilon^2.
\end{aligned}
$$

So $\{h_F:F\in\mathcal{F}\}$ is a Cauchy net in $\mathcal{H}$. Because $\mathcal{H}$ is complete, this net converges. In fact, it converges to $\sum_{n=1}^{\infty}\langle h,e_n\rangle e_n$. ■

**4.13. Theorem.** *If $\mathcal{E}$ is an orthonormal set in $\mathcal{H}$, then the following statements are equivalent.*

(a) $\mathcal{E}$ is a basis for $\mathcal{H}$.

(b) If $h\in\mathcal{H}$ and $h\perp\mathcal{E}$, then $h=0$.

(c) $\bigvee\mathcal{E}=\mathcal{H}$.

(d) If $h\in\mathcal{H}$, then $h=\sum\{\langle h,e\rangle e:e\in\mathcal{E}\}$.



<a id="pdf-page-32"></a>
(e) If $g$ and $h\in\mathcal H$, then

$$
\langle g,h\rangle=\sum\{\langle g,e\rangle\langle e,h\rangle:e\in\mathcal E\}.
$$

(f) If $h\in\mathcal H$, then $\|h\|^2=\sum\{|\langle h,e\rangle|^2:e\in\mathcal E\}$ (Parseval’s Identity).

**Proof.** (a)$\Rightarrow$(b): Suppose $h\perp\mathcal E$ and $h\ne0$; then $\mathcal E\cup\{h/\|h\|\}$ is an orthonormal set that properly contains $\mathcal E$, contradicting maximality.

(b)$\Leftrightarrow$(c): By Corollary 2.11, $\bigvee\mathcal E=\mathcal H$ if and only if $\mathcal E^\perp=(0)$.

(b)$\Rightarrow$(d): If $h\in\mathcal H$, then $f=h-\sum\{\langle h,e\rangle e:e\in\mathcal E\}$ is a well-defined vector by Lemma 4.12. If $e_1\in\mathcal E$, then $\langle f,e_1\rangle=\langle h,e_1\rangle-\sum\{\langle h,e\rangle\langle e,e_1\rangle:e\in\mathcal E\}=\langle h,e_1\rangle-\langle h,e_1\rangle=0$. That is, $f\in\mathcal E^\perp$. Hence $f=0$. (Is everything legitimate in that string of equalities? We don’t want any illegitimate equalities.)

(d)$\Rightarrow$(e): This is left as an exercise for the reader.

(e)$\Rightarrow$(f): Since $\|h\|^2=\langle h,h\rangle$, this is immediate.

(f)$\Rightarrow$(a): If $\mathcal E$ is not a basis, then there is a unit vector $e_0$ ($\|e_0\|=1$) in $\mathcal H$ such that $e_0\perp\mathcal E$. Hence, $0=\sum\{|\langle e_0,e\rangle|^2:e\in\mathcal E\}$, contradicting (f). $\blacksquare$

Just as in finite dimensional spaces, a basis in Hilbert space can be used to define a concept of dimension. For this purpose the next result is pivotal.

**4.14. Proposition.** *If $\mathcal H$ is a Hilbert space, any two bases have the same cardinality.*

**Proof.** Let $\mathcal E$ and $\mathcal F$ be two bases for $\mathcal H$ and put $\varepsilon=$ the cardinality of $\mathcal E$, $\eta=$ the cardinality of $\mathcal F$. If $\varepsilon$ or $\eta$ is finite, then $\varepsilon=\eta$ (Exercise 15). Suppose both $\varepsilon$ and $\eta$ are infinite. For $e$ in $\mathcal E$, let $\mathcal F_e\equiv\{f\in\mathcal F:\langle e,f\rangle\ne0\}$; so $\mathcal F_e$ is countable. By (4.13b), each $f$ in $\mathcal F$ belongs to at least one set $\mathcal F_e$, $e$ in $\mathcal E$. That is, $\mathcal F=\bigcup\{\mathcal F_e:e\in\mathcal E\}$. Hence $\eta\leq\varepsilon\cdot\aleph_0=\varepsilon$. Similarly, $\varepsilon\leq\eta$. $\blacksquare$

**4.15. Definition.** The *dimension* of a Hilbert space is the cardinality of a basis and is denoted by $\dim\mathcal H$.

If $(X,d)$ is a metric space that is separable and $\{B_i=B(x_i;\varepsilon_i):i\in I\}$ is a collection of pairwise disjoint open balls in $X$, then $I$ must be countable. Indeed, if $D$ is a countable dense subset of $X$, $B_i\cap D\ne\square$ for each $i$ in $I$. Thus there is a point $x_i$ in $B_i\cap D$. So $\{x_i:i\in I\}$ is a subset of $D$ having the cardinality of $I$; thus $I$ must be countable.

**4.16. Proposition.** *If $\mathcal H$ is an infinite dimensional Hilbert space, then $\mathcal H$ is separable if and only if $\dim\mathcal H=\aleph_0$.*

**Proof.** Let $\mathcal E$ be a basis for $\mathcal H$. If $e_1,e_2\in\mathcal E$, then $\|e_1-e_2\|^2=\|e_1\|^2+\|e_2\|^2=2$. Hence $\{B(e;1/\sqrt{2}):e\in\mathcal E\}$ is a collection of pairwise disjoint open balls in $\mathcal H$. From the discussion preceding this proposition, the assumption that $\mathcal H$ is separable implies $\mathcal E$ is countable. The converse is an exercise. $\blacksquare$



<a id="pdf-page-33"></a>
## Exercises

1. Verify the statements in Example 4.3.

2. Verify the statements in Example 4.4.

3. Verify the statements in Example 4.5.

4. Find an infinite orthonormal set in the Hilbert space of Example 1.8.

5. Using the notation of the Gram–Schmidt Orthogonalization Process, show that up to scalar multiple $e_1=h_1/\|h_1\|$ and for $n\geq 2$, $e_n=\|h_n-f_n\|^{-1}(h_n-f_n)$, where $f_n$ is the vector defined formally by
   $$
   f_n=\frac{-1}{\det[\langle h_i,h_j\rangle]_{i,j=1}^{n-1}}
   \det\begin{bmatrix}
   \langle h_1,h_1\rangle & \cdots & \langle h_{n-1},h_1\rangle & \langle h_n,h_1\rangle\\
   \vdots & & \vdots & \vdots\\
   \langle h_1,h_{n-1}\rangle & \cdots & \langle h_{n-1},h_{n-1}\rangle & \langle h_n,h_{n-1}\rangle\\
   h_1 & \cdots & h_{n-1} & 0
   \end{bmatrix}.
   $$

In the next three exercises, the reader is asked to apply the Gram–Schmidt Orthogonalization Process to a given sequence in a Hilbert space. A reference for this material is pp. 82–96 of Courant and Hilbert [1953].

6. If the sequence $1,x,x^2,\ldots$ is orthogonalized in $L^2(-1,1)$, the sequence $e_n(x)=[\tfrac12(2n+1)]^{1/2}P_n(x)$ is obtained, where
   $$
   P_n(x)=\frac{1}{2^n n!}\left(\frac{d}{dx}\right)^n(x^2-1)^n.
   $$
   The functions $P_n(x)$ are called Legendre polynomials.

7. If the sequence $e^{-x^2/2},xe^{-x^2/2},x^2e^{-x^2/2},\ldots$ is orthogonalized in $L^2(-\infty,\infty)$, the sequence $e_n(x)=[2^n n!\sqrt{\pi}]^{-1/2}H_n(x)e^{-x^2/2}$ is obtained, where
   $$
   H_n(x)=(-1)^n e^{x^2}\left(\frac{d}{dx}\right)^n e^{-x^2}.
   $$
   The functions $H_n$ are Hermite polynomials and satisfy $H_n'(x)=2nH_{n-1}(x)$.

8. If the sequence $e^{-x/2},xe^{-x/2},x^2e^{-x/2},\ldots$ is orthogonalized in $L^2(0,\infty)$, the sequence $e_n(x)=e^{-x/2}L_n(x)/n!$ is obtained, where
   $$
   L_n(x)=e^x\left(\frac{d}{dx}\right)^n(x^n e^{-x}).
   $$
   The functions $L_n$ are called Laguerre polynomials.

9. Prove Corollary 4.10 using Definition 4.11.

10. If $\{h_n\}$ is a sequence in Hilbert space and $\sum\{h_n:n\in\mathbb N\}$ converges to $h$ (Definition 4.11), then $\lim_n\sum_{k=1}^n h_k=h$. Show that the converse is false.

11. If $\{h_n\}$ is a sequence in a Hilbert space and $\sum_{n=1}^{\infty}\|h_n\|<\infty$, show that $\sum\{h_n:n\in\mathbb N\}$ converges in the sense of Definition 4.11.

12. Let $\{\alpha_n\}$ be a sequence in $\mathbb F$ and prove that the following statements are equivalent: (a) $\sum\{\alpha_n:n\in\mathbb N\}$ converges in the sense of Definition 4.11. (b) If $\pi$ is any permutation of $\mathbb N$, then $\sum_{n=1}^{\infty}\alpha_{\pi(n)}$ converges (unconditional convergence). (c) $\sum_{n=1}^{\infty}|\alpha_n|<\infty$.



<a id="pdf-page-34"></a>
13. Let $\mathcal E$ be an orthonormal subset of $\mathcal H$ and let $\mathcal M=\bigvee\mathcal E$. If $P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M$, show that $Ph=\sum\{\langle h,e\rangle e:e\in\mathcal E\}$ for every $h$ in $\mathcal H$.

14. Let $\lambda=\text{Area}$ measure on $\{z\in\mathbb C:|z|<1\}$ and show that $1,z,z^2,\ldots$ are orthogonal vectors in $L^2(\lambda)$. Find $\|z^n\|$, $n\geq 0$. If $e_n=\|z^n\|^{-1}z^n$, $n\geq 0$, is $\{e_0,e_1,\ldots\}$ a basis for $L^2(\lambda)$?

15. In the proof of (4.14), show that if either $\varepsilon$ or $\eta$ is finite, then $\varepsilon=\eta$.

16. If $\mathcal H$ is an infinite dimensional Hilbert space, show that no orthonormal basis for $\mathcal H$ is a Hamel basis. Show that a Hamel basis is uncountable.

17. Let $d\geq 1$ and let $\mu$ be a regular Borel measure on $\mathbb R^d$. Show that $L^2(\mu)$ is separable.

18. Suppose $L^2(X,\Omega,\mu)$ is separable and $\{E_i:i\in I\}$ is a collection of pairwise disjoint subsets of $X$, $E_i\in\Omega$, and $0<\mu(E_i)<\infty$ for all $i$. Show that $I$ is countable. Can you allow $\mu(E_i)=\infty$?

19. If $\{h\in\mathcal H:\|h\|\leq 1\}$ is compact, show that $\dim\mathcal H<\infty$.

20. What is the cardinality of a Hamel basis for $l^2$?

## §5. Isomorphic Hilbert Spaces and the Fourier Transform for the Circle

<!-- BEGIN BACKGROUND BG-I.block6 -->
<a id="bg-i-17"></a>
### Lemma BG-I.17. Dense range plus an isometry gives surjectivity

An isometry from a complete space into a metric space has closed image.

**Proof.** If $Ux_n\to y$, then $d(x_n,x_m)=d(Ux_n,Ux_m)$ makes $(x_n)$ Cauchy. Write $x_n\to x$ and use the isometry to obtain $Ux=y$. A closed dense image is the whole codomain. Completeness of the domain matters; the inclusion $\mathbb Q\hookrightarrow\mathbb R$ is an isometry with dense, nonclosed image. $\square$

<a id="bg-i-18"></a>
### Theorem BG-I.18. The Fourier density input, proved by averaging

Every continuous $2\pi$-periodic function is a uniform limit of trigonometric polynomials. These continuous periodic functions are dense in $L^2[0,2\pi]$.

**Proof.** Define the nonnegative Fejér kernel

$$
F_N(t)=\frac1{N+1}\left|\sum_{k=0}^N e^{ikt}\right|^2.
$$

Expanding the square and integrating exponentials shows $(2\pi)^{-1}\int_{-\pi}^{\pi}F_N=1$. For $\delta\leq|t|\leq\pi$, the geometric-sum formula gives $F_N(t)\leq[(N+1)\sin^2(\delta/2)]^{-1}$. Put $p_N(x)=(2\pi)^{-1}\int F_N(t)f(x-t)\,dt$. Expansion of $F_N$ shows that $p_N$ is a trigonometric polynomial. A continuous function on the compact circle is uniformly continuous: otherwise points with distances tending to zero and function differences bounded below would have a common convergent subsequence, contradicting continuity. In $p_N(x)-f(x)$, the portion $|t|<\delta$ is therefore uniformly small; the remaining portion tends uniformly to zero by the displayed bound. This proves uniform approximation and supplies Theorem 5.6 without assuming complex analysis.

For the density assertion, truncate an $L^2$ function to make it bounded and approximate its range by finitely many small squares (or intervals in the real case). Dominated convergence shows that the resulting simple functions approximate in $L^2$. For Lebesgue measure on a finite interval, each measurable set is approximable in measure by a finite union of intervals: choose an open superset with arbitrarily small excess measure, express it as countably many disjoint intervals, and retain a finite part with small omitted measure. This uses the outer regularity in the construction of Lebesgue measure. The indicator of a finite union of intervals can be approximated by continuous piecewise linear functions, altering it only in arbitrarily short neighborhoods of the endpoints. Choose these approximants to vanish near $0$ and $2\pi$; the extra neighborhoods also have arbitrarily small measure. They are periodic at the endpoints, and their squared error is bounded by the length of the altered set. Linear combinations give the required density. Uniform approximation then implies $L^2$ approximation by Lemma BG-I.4. $\square$

The Fourier series in (5.9) converges in the $L^2$ norm; the theorem just proved does not say that its ordinary partial sums converge uniformly. The averaging by $F_N$ is a different approximation procedure.
<!-- END BACKGROUND BG-I.block6 -->

Every mathematical theory has its concept of isomorphism. In topology there is homeomorphism and homotopy equivalence; algebra calls them isomorphisms. The basic idea is to define a map which preserves the basic structure of the spaces in the category.

**5.1. Definition.** If $\mathcal H$ and $\mathcal K$ are Hilbert spaces, an *isomorphism* between $\mathcal H$ and $\mathcal K$ is a linear surjection $U:\mathcal H\to\mathcal K$ such that

$$
\langle Uh,Ug\rangle=\langle h,g\rangle
$$

for all $h,g$ in $\mathcal H$. In this case $\mathcal H$ and $\mathcal K$ are said to be *isomorphic*.

It is easy to see that if $U:\mathcal H\to\mathcal K$ is an isomorphism, then so is $U^{-1}:\mathcal K\to\mathcal H$. Similar such arguments show that the concept of “isomorphic” is an equivalence relation on Hilbert spaces. It is also certain that this is the correct equivalence relation since an inner product is the essential ingredient for a Hilbert space and isomorphic Hilbert spaces have the “same” inner product. One might object that completeness is another essential ingredient in the definition of a Hilbert space. So it is! However, this too is preserved by an isomorphism. An *isometry* between metric spaces is a map that preserves distance.

**5.2. Proposition.** *If $V:\mathcal H\to\mathcal K$ is a linear map between Hilbert spaces, then $V$ is an isometry if and only if $\langle Vh,Vg\rangle=\langle h,g\rangle$ for all $h,g$ in $\mathcal H$.*



<a id="pdf-page-35"></a>
**Proof.** Assume $\langle Vh,Vg\rangle=\langle h,g\rangle$ for all $h,g$ in $\mathcal H$. Then $\|Vh\|^2=\langle Vh,Vh\rangle=\langle h,h\rangle=\|h\|^2$ and $V$ is an isometry.

Now assume that $V$ is an isometry. If $h,g\in\mathcal H$ and $\lambda\in\mathbb F$, then $\|h+\lambda g\|^2=\|Vh+\lambda Vg\|^2$. Using the polar identity on both sides of this equation gives

$$
\|h\|^2+2\operatorname{Re}\bar\lambda\langle h,g\rangle+|\lambda|^2\|g\|^2
=\|Vh\|^2+2\operatorname{Re}\bar\lambda\langle Vh,Vg\rangle+|\lambda|^2\|Vg\|^2.
$$

But $\|Vh\|=\|h\|$ and $\|Vg\|=\|g\|$, so this equation becomes

$$
\operatorname{Re}\bar\lambda\langle h,g\rangle
=\operatorname{Re}\bar\lambda\langle Vh,Vg\rangle
$$

for any $\lambda$ in $\mathbb F$. If $\mathbb F=\mathbb R$, take $\lambda=1$. If $\mathbb F=\mathbb C$, first take $\lambda=1$ and then take $\lambda=i$ to find that $\langle h,g\rangle$ and $\langle Vh,Vg\rangle$ have the same real and imaginary parts. $\blacksquare$

Note that an isometry between metric spaces maps Cauchy sequences into Cauchy sequences. Thus an isomorphism also preserves completeness. That is, if an inner product space is isomorphic to a Hilbert space, then it must be complete.

**5.3. Example.** Definite $S:l^2\to l^2$ by $S(\alpha_1,\alpha_2,\ldots)=(0,\alpha_1,\alpha_2,\ldots)$. Then $S$ is an isometry that is not surjective.

The preceding example shows that isometries need not be isomorphisms.

A word about terminology. Many call what we call an isomorphism a unitary operator. We shall define a *unitary operator* as a linear transformation $U:\mathcal H\to\mathcal H$ that is a surjective isometry. That is, a unitary operator is an isomorphism whose range coincides with its domain. This may seem to be a minor distinction, and in many ways it is. But experience has taught me that there is some benefit in making such a distinction, or at least in being aware of it.

**5.4. Theorem.** *Two Hilbert spaces are isomorphic if and only if they have the same dimension.*

**Proof.** If $U:\mathcal H\to\mathcal K$ is an isomorphism and $\mathcal E$ is a basis for $\mathcal H$, then it is easy to see that $U\mathcal E\equiv\{Ue:e\in\mathcal E\}$ is a basis for $\mathcal K$. Hence, $\dim\mathcal H=\dim\mathcal K$.

Let $\mathcal H$ be a Hilbert space and let $\mathcal E$ be a basis for $\mathcal H$. Consider the Hilbert space $l^2(\mathcal E)$. If $h\in\mathcal H$, define $\hat h:\mathcal E\to\mathbb F$ by $\hat h(e)=\langle h,e\rangle$. By Parseval’s Identity $\hat h\in l^2(\mathcal E)$ and $\|h\|=\|\hat h\|$. Define $U:\mathcal H\to l^2(\mathcal E)$ by $Uh=\hat h$. Thus $U$ is linear and an isometry. It is easy to see that $\operatorname{ran}U$ contains all the functions $f$ in $l^2(\mathcal E)$ such that $f(e)=0$ for all but a finite number of $e$; that is, $\operatorname{ran}U$ is dense. But $U$, being an isometry, must have closed range. Hence $U:\mathcal H\to l^2(\mathcal E)$ is an isomorphism.



<a id="pdf-page-36"></a>
If $\mathcal K$ is a Hilbert space with a basis $\mathcal F$, $\mathcal K$ is isomorphic to $l^2(\mathcal F)$. If $\dim\mathcal H=\dim\mathcal K$, $\mathcal E$ and $\mathcal F$ have the same cardinality; it is easy to see that $l^2(\mathcal E)$ and $l^2(\mathcal F)$ must be isomorphic. Therefore $\mathcal H$ and $\mathcal K$ are isomorphic. ■

**5.5. Corollary.** *All separable infinite dimensional Hilbert spaces are isomorphic.*

This section concludes with a rather important example of an isomorphism, the Fourier transform on the circle.

The proof of the next result can be found as an Exercise on p. 263 of Conway [1978]. Another proof will be given latter in this book after the Stone–Weierstrass Theorem is proved. So the reader can choose to assume this for the moment. Let $\mathbb D=\{z\in\mathbb C:|z|<1\}$.

**5.6. Theorem.** *If $f:\partial\mathbb D\to\mathbb C$ is a continuous function, then there is a sequence $\{p_n(z,\bar z)\}$ of polynomials in $z$ and $\bar z$ such that $p_n(z,\bar z)\to f(z)$ uniformly on $\partial\mathbb D$.*

Note that if $z\in\partial\mathbb D$, $\bar z=z^{-1}$. Thus a polynomial in $z$ and $\bar z$ on $\partial\mathbb D$ becomes a function of the form

$$
\sum_{k=-m}^{n}\alpha_k z^k.
$$

If we put $z=e^{i\theta}$, this becomes a function of the form

$$
\sum_{k=-m}^{n}\alpha_k e^{ik\theta}.
$$

Such functions are called *trigonometric polynomials*.

We can now show that the orthonormal set in Example 4.3 is a basis for $L_{\mathbb C}^{2}[0,2\pi]$. This is a rather important result.

**5.7. Theorem.** *If for each $n$ in $\mathbb Z$, $e_n(t)\equiv(2\pi)^{-1/2}\exp(int)$, then $\{e_n:n\in\mathbb Z\}$ is a basis for $L_{\mathbb C}^{2}[0,2\pi]$.*

**Proof.** Let $\mathcal T=\{\sum_{k=-n}^{n}\alpha_k e_k:\alpha_k\in\mathbb C,\ n\geq 0\}$. Then $\mathcal T$ is a subalgebra of $C_{\mathbb C}[0,2\pi]$, the algebra of all continuous $\mathbb C$-valued functions on $[0,2\pi]$. Note that if $f\in\mathcal T$, $f(0)=f(2\pi)$. We want to show that the uniform closure of $\mathcal T$ is $\mathcal C\equiv\{f\in C_{\mathbb C}[0,2\pi]:f(0)=f(2\pi)\}$. To do this, let $f\in\mathcal C$ and define $F:\partial\mathbb D\to\mathbb C$ by $F(e^{it})=f(t)$. $F$ is continuous. (Why?) By (5.6) there is a sequence of polynomials in $z$ and $\bar z$, $\{p_n(z,\bar z)\}$, such that $p_n(z,\bar z)\to F(z)$ uniformly on $\partial\mathbb D$. Thus $p_n(e^{it},e^{-it})\to f(t)$ uniformly on $[0,2\pi]$. But $p_n(e^{it},e^{-it})\in\mathcal T$.

Now the closure of $\mathcal C$ in $L_{\mathbb C}^{2}[0,2\pi]$ is all of $L_{\mathbb C}^{2}[0,2\pi]$ (Exercise 6). Hence $\bigvee\{e_n:n\in\mathbb Z\}=L_{\mathbb C}^{2}[0,2\pi]$ and $\{e_n\}$ is thus a basis (4.13). ■

Actually, it is usually preferred to normalize the measure on $[0,2\pi]$. That is, replace $dt$ by $(2\pi)^{-1}\,dt$, so that the total measure of $[0,2\pi]$ is 1. Now define



<a id="pdf-page-37"></a>
$e_n(t)=\exp(int)$. Hence $\{e_n:n\in\mathbb Z\}$ is a basis for $\mathcal H\equiv L_{\mathbb C}^{2}([0,2\pi],(2\pi)^{-1}\,dt)$. If $f\in\mathcal H$, then

$$
\hat f(n)\equiv\langle f,e_n\rangle
=\frac{1}{2\pi}\int_0^{2\pi}f(t)e^{-int}\,dt
\tag{5.8}
$$

is called the $n$th Fourier coefficient of $f$, $n$ in $\mathbb Z$. By (5.7) and (4.13d),

$$
f=\sum_{n=-\infty}^{\infty}\hat f(n)e_n,
\tag{5.9}
$$

where this infinite series converges to $f$ in the metric defined by the norm of $\mathcal H$. This is called the Fourier series of $f$. This terminology is classical and has been adopted for a general Hilbert space.

If $\mathcal H$ is any Hilbert space and $\mathcal E$ is a basis, the scalars $\{\langle h,e\rangle;e\in\mathcal E\}$ are called the Fourier coefficients of $h$ (relative to $\mathcal E$) and the series in (4.13d) is called the Fourier expansion of $h$ (relative to $\mathcal E$).

Note that Parseval’s Identity applied to (5.9) gives that $\sum_{n=-\infty}^{\infty}|\hat f(n)|^2<\infty$. This proves a classical result.

**5.10. The Riemann–Lebesgue Lemma.** If $f\in L_{\mathbb C}^{2}[0,2\pi]$, then $\int_0^{2\pi}f(t)e^{-int}\,dt\to0$ as $n\to\pm\infty$.

If $f\in L_{\mathbb C}^{2}[0,2\pi]$, then the Fourier series of $f$ converges to $f$ in $L^2$-norm. It was conjectured by Lusin that the series converges to $f$ almost everywhere. This was proved in Carleson [1966]. Hunt [1967] showed that if $f\in L_{\mathbb C}^{p}[0,2\pi]$, $1<p\leq\infty$, then the Fourier series also converges to $f$ a.e. Long before that, Kolmogoroff had furnished an example of a function $f$ in $L_{\mathbb C}^{1}[0,2\pi]$ whose Fourier series a.e. does not converge to $f$.

For $f$ in $L_{\mathbb C}^{2}[0,2\pi]$, the function $\hat f:\mathbb Z\to\mathbb C$ is called the Fourier transform of $f$; the map $U:L_{\mathbb C}^{2}[0,2\pi]\to l^{2}(\mathbb Z)$ defined by $Uf=\hat f$ is the Fourier transform. The results obtained so far can be applied to this situation to yield the following.

**5.11. Theorem.** The Fourier transform is a linear isometry from $L_{\mathbb C}^{2}[0,2\pi]$ onto $l^{2}(\mathbb Z)$.

**PROOF.** Let $U:L_{\mathbb C}^{2}[0,2\pi]\to l^{2}(\mathbb Z)$ be the Fourier transform. That $U$ maps $L^{2}\equiv L_{\mathbb C}^{2}[0,2\pi]$ into $l^{2}(\mathbb Z)$ and satisfies $\|Uf\|=\|f\|$ is a consequence of Parseval’s Identity. That $U$ is linear is an exercise. If $\{\alpha_n\}\in l^{2}(\mathbb Z)$ and $\alpha_n=0$ for all but a finite number of $n$, then $f=\sum_{n=-\infty}^{\infty}\alpha_ne_n\in L^{2}$. It is easy to check that $\hat f(n)=\alpha_n$ for all $n$, so $Uf=\{\alpha_n\}$. Thus $\operatorname{ran}U$ is dense in $l^{2}(\mathbb Z)$. But $U$ is an isometry, so $\operatorname{ran}U$ is closed; hence $U$ is surjective. $\blacksquare$

Note that functions in $L_{\mathbb C}^{2}[0,2\pi]$ can be defined on $\partial\mathbb D$ by letting $f(e^{i\theta})=f(\theta)$. The ambiguity for $\theta=0$ and $2\pi$ (or $e^{i\theta}=1$) might cause us to pause, but remember that elements of $L_{\mathbb C}^{2}[0,2\pi]$ are equivalence classes of



<a id="pdf-page-38"></a>
functions—not really functions. Since $\{0,2\pi\}$ has zero measure, there is really no ambiguity. In this way $L_{\mathbb C}^{2}[0,2\pi]$ can be identified with $L_{\mathbb C}^{2}(\partial\mathbb D)$, where the measure on $\partial\mathbb D$ is normalized arc-length measure (normalized so that the total measure of $\partial\mathbb D$ is 1). So $L_{\mathbb C}^{2}[0,2\pi]$ and $L_{\mathbb C}^{2}(\partial\mathbb D)$ are (naturally) isomorphic. Thus, Theorem 5.11 is a theorem about the Fourier transform of the circle.

The importance of Theorem 5.11 is not the fact that $L_{\mathbb C}^{2}[0,2\pi]$ and $l^{2}(\mathbb Z)$ are isomorphic, but that the Fourier transform is an isomorphism. The fact that these two spaces are isomorphic follows from the abstract result that all separable infinite dimensional Hilbert spaces are isomorphic (5.5).

## Exercises

1. Verify the statements in Example 5.3.

2. Define $V:L^{2}(0,\infty)\to L^{2}(0,\infty)$ by $(Vf)(t)=f(t-1)$ if $t>1$ and $(Vf)(t)=0$ if $t\leq 1$. Show that $V$ is an isometry that is not surjective.

3. Define $V:L^{2}(\mathbb R)\to L^{2}(\mathbb R)$ by $(Vf)(t)=f(t-1)$ and show that $V$ is an isomorphism (a unitary operator).

4. Let $\mathcal H$ be the Hilbert space of Example 1.8 and define $U:\mathcal H\to L^{2}(0,1)$ by $Uf=f'$. Show that $U$ is an isomorphism and find a formula for $U^{-1}$.

5. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $u:X\to\mathbb F$ be an $\Omega$-measurable function such that $\sup\{|u(x)|:x\in X\}<\infty$. Show that $U:L^{2}(X,\Omega,\mu)\to L^{2}(X,\Omega,\mu)$ defined by $Uf=uf$ is an isometry if and only if $|u(x)|=1$ a.e. $[\mu]$, in which case $U$ is surjective.

6. Let $\mathcal C=\{f\in C[0,2\pi]:f(0)=f(2\pi)\}$ and show that $\mathcal C$ is dense in $L^{2}[0,2\pi]$.

7. Show that $\{1/\sqrt{2\pi},\ (1/\sqrt{\pi})\cos nt,\ (1/\sqrt{\pi})\sin nt:1\leq n<\infty\}$ is a basis for $L^{2}[-\pi,\pi]$.

8. Let $(X,\Omega)$ be a measurable space and let $\mu,\nu$ be two $\sigma$-finite measures defined on $(X,\Omega)$. Suppose $\nu\ll\mu$ and $\phi$ is the Radon–Nikodym derivative of $\nu$ with respect to $\mu$ $(\phi=d\nu/d\mu)$. Define $V:L^{2}(\nu)\to L^{2}(\mu)$ by $Vf=\sqrt{\phi}f$. Show that $V$ is a well-defined linear isometry and $V$ is an isomorphism if and only if $\mu\ll\nu$ (that is, $\mu$ and $\nu$ are mutually absolutely continuous).

9. If $\mathcal H$ and $\mathcal K$ are Hilbert spaces and $U:\mathcal H\to\mathcal K$ is a surjective function such that $\langle Uf,Ug\rangle=\langle f,g\rangle$ for all vectors $f$ and $g$ in $\mathcal H$, then $U$ is linear.

## §6. The Direct Sum of Hilbert Spaces

<!-- BEGIN BACKGROUND BG-I.block7 -->
<a id="bg-i-19"></a>
### Lemma BG-I.19. Completing the direct-sum argument

If each $H_i$ is complete, the square-summable direct sum is complete, including for an arbitrary index set.

**Proof.** For a Cauchy sequence $x_n=(x_n(i))$, $\|x_n(i)-x_m(i)\|\leq\|x_n-x_m\|$ gives a coordinate limit $x(i)$. Boundedness $\|x_n\|\leq C$ and passage to the limit in each finite sum give $\sum_{i\in F}\|x(i)\|^2\leq C^2$. Taking the supremum over finite $F$ gives $x$ in the direct sum. If $\|x_n-x_m\|<\varepsilon$ for $m,n\geq N$, the same finite-sum argument, now letting $m\to\infty$, gives $\sum_{i\in F}\|x_n(i)-x(i)\|^2\leq\varepsilon^2$. Take the supremum to obtain $\|x_n-x\|\leq\varepsilon$. This avoids an unjustified interchange of a limit and an infinite sum. $\square$
<!-- END BACKGROUND BG-I.block7 -->

Suppose $\mathcal H$ and $\mathcal K$ are Hilbert spaces. We want to define $\mathcal H\oplus\mathcal K$ so that it becomes a Hilbert space. This is not a difficult assignment. For any vector spaces $\mathcal X$ and $\mathcal Y$, $\mathcal X\oplus\mathcal Y$ is defined as the Cartesian product $\mathcal X\times\mathcal Y$ where the operations are defined on $\mathcal X\times\mathcal Y$ coordinatewise. That is, if elements of



<a id="pdf-page-39"></a>
$\mathcal X\oplus\mathcal Y$ are defined as $\{x\oplus y:x\in\mathcal X,\ y\in\mathcal Y\}$, then $(x_1\oplus y_1)+(x_2\oplus y_2)\equiv(x_1+x_2)\oplus(y_1+y_2)$, and so on.

**6.1. Definition.** If $\mathcal H$ and $\mathcal K$ are Hilbert spaces, $\mathcal H\oplus\mathcal K=\{h\oplus k:h\in\mathcal H,\ k\in\mathcal K\}$ and

$$
\langle h_1\oplus k_1,h_2\oplus k_2\rangle
\equiv\langle h_1,h_2\rangle+\langle k_1,k_2\rangle.
$$

It must be shown that this defines an inner product on $\mathcal H\oplus\mathcal K$ and that $\mathcal H\oplus\mathcal K$ is complete (Exercise).

Now what happens if we want to define $\mathcal H_1\oplus\mathcal H_2\oplus\cdots$ for a sequence of Hilbert spaces $\mathcal H_1,\mathcal H_2,\ldots$? There is a problem about the completeness of this infinite direct sum, but this can be overcome as follows.

**6.2. Proposition.** *If $\mathcal H_1,\mathcal H_2,\ldots$ are Hilbert spaces, let $\mathcal H=\{(h_n)_{n=1}^{\infty}:h_n\in\mathcal H_n$ for all $n$ and $\sum_{n=1}^{\infty}\|h_n\|^2<\infty\}$. For $h=(h_n)$ and $g=(g_n)$ in $\mathcal H$, define*

$$
\langle h,g\rangle=\sum_{n=1}^{\infty}\langle h_n,g_n\rangle. \tag{6.3}
$$

*Then $\langle\cdot,\cdot\rangle$ is an inner product on $\mathcal H$ and the norm relative to this inner product is $\|h\|=[\sum_{n=1}^{\infty}\|h_n\|^2]^{1/2}$. With this inner product $\mathcal H$ is a Hilbert space.*

**Proof.** If $h=(h_n)$ and $g=(g_n)\in\mathcal H$, then the CBS inequality implies $\sum|\langle h_n,g_n\rangle|\leq\sum\|h_n\|\|g_n\|\leq(\sum\|h_n\|^2)^{1/2}(\sum\|g_n\|^2)^{1/2}<\infty$. Hence the series in (6.3) converges absolutely. The remainder of the proof is left to the reader. $\blacksquare$

**6.4. Definition.** If $\mathcal H_1,\mathcal H_2,\ldots$ are Hilbert spaces, the space $\mathcal H$ of Proposition 6.2 is called the *direct sum* of $\mathcal H_1,\mathcal H_2,\ldots$ and is denoted by $\mathcal H\equiv\mathcal H_1\oplus\mathcal H_2\oplus\cdots$.

This is part of a more general process. If $\{\mathcal H_i:i\in I\}$ is a collection of Hilbert spaces, $\mathcal H\equiv\bigoplus\{\mathcal H_i:i\in I\}$ is defined as the collection of functions $h:I\to\bigcup\{\mathcal H_i:i\in I\}$ such that $h(i)\in\mathcal H_i$ for all $i$ and $\sum\{\|h(i)\|^2:i\in I\}<\infty$. If $h,g\in\mathcal H$, $\langle h,g\rangle\equiv\sum\{\langle h(i),g(i)\rangle:i\in I\}$; $\mathcal H$ is a Hilbert space.

The main reason for considering direct sums is that they provide a way of manufacturing operators on Hilbert space. In fact, Hilbert space is a rather dull subject, except for the fact that there are numerous interesting questions about the linear operators on them that are as yet unresolved. This subject is introduced in the next chapter.

## EXERCISES

1. Let $\{(X_i,\Omega_i,\mu_i):i\in I\}$ be a collection of measure spaces and define $X$, $\Omega$, and $\mu$ as follows. Let $X=$ the disjoint union of $\{X_i:i\in I\}$ and let $\Omega=\{\Delta\subseteq X:\Delta\cap X_i\in\Omega_i$ for all $i\}$. For $\Delta$ in $\Omega$ put $\mu(\Delta)=\sum_i\mu_i(\Delta\cap X_i)$. Show that $(X,\Omega,\mu)$ is a measure space and $L^2(X,\Omega,\mu)$ is isomorphic to $\bigoplus\{L^2(X_i,\Omega_i,\mu_i):i\in I\}$.



<a id="pdf-page-40"></a>
2. Let $(X,\Omega)$ be a measurable space, let $\mu_1,\mu_2$ be $\sigma$-finite measures defined on $(X,\Omega)$, and put $\mu=\mu_1+\mu_2$. Show that the map $V:L^2(X,\Omega,\mu)\to L^2(X,\Omega,\mu_1)\oplus L^2(X,\Omega,\mu_2)$ defined by $Vf=f_1\oplus f_2$, where $f_j$ is the equivalence class of $L^2(X,\Omega,\mu_j)$ corresponding to $f$, is well defined, linear, and injective. Show that $V$ is an isomorphism iff $\mu_1$ and $\mu_2$ are mutually singular.

<!-- BEGIN SOLUTIONS I -->
<a id="exercise-solutions"></a>
## Exercise Solutions

These are added study solutions, not part of Conway's original text. Solution
I.s.n answers Exercise n in §s of Chapter I. All 54 numbered exercises in this
chapter are covered below, including their lettered subparts. Inner products
are linear in the first variable. Hilbert-space isomorphisms are surjective
linear isometries; a Hilbert basis is an orthonormal basis, not a Hamel basis.
The complex-analysis inputs are proved in the
[unified supplement](background-complex-analysis.md).

### §1. Elementary Properties and Examples

#### Solution I.1.1 — Finite sequences and weighted inner products

Finite-support sequences form a vector space: a linear combination has support
contained in the finite union of the original supports. Consequently every
sum in Example 1.2 is finite. Coordinatewise calculation gives linearity in
the first variable and conjugate symmetry. The even-coordinate form has
$u(a,a)=\sum_n|a_{2n}|^2\geq0$, but the nonzero sequence $(1,0,\ldots)$ has
value zero. Thus it is only a semi-inner product.

For each weight $w_n=1$, $w_n=1/n$, or $w_n=n^5$, the corresponding form is
$\langle a,b\rangle_w=\sum_n w_na_n\overline{b_n}$. All weights are strictly
positive, so $\langle a,a\rangle_w=0$ forces every coordinate to vanish.
Together with the identities already checked, this proves all three are inner
products.

#### Solution I.1.2 — Completeness of an arbitrarily indexed square sum

Recall that $\sum_{i\in I}|a_i|^2$ means the supremum of the sums over finite
subsets of $I$. Finite-dimensional Cauchy–Schwarz, followed by this supremum,
shows that $\sum_i a_i\overline{b_i}$ is absolutely summable and defines an
inner product. A square-summable family has countable support: each set
$\{i:|a_i|\geq1/m\}$ is finite, and their union contains its support.

Let $(a^{(n)})$ be Cauchy in this norm. Each coordinate is Cauchy because
$|a_i^{(n)}-a_i^{(m)}|\leq\|a^{(n)}-a^{(m)}\|$; write its limit as $a_i$.
The sequence has a common norm bound $C$. For every finite $F\subset I$,
$\sum_{i\in F}|a_i|^2=\lim_n\sum_{i\in F}|a_i^{(n)}|^2\leq C^2$.
Thus $a\in\ell^2(I)$. Given $\varepsilon>0$, choose $N$ so that the Cauchy
distances are at most $\varepsilon$ for $m,n\geq N$. Taking $m\to\infty$
in each finite coordinate sum gives
$\sum_{i\in F}|a_i^{(n)}-a_i|^2\leq\varepsilon^2$ for $n\geq N$.
Taking the supremum over $F$ proves norm convergence and completeness.

#### Solution I.1.3 — The derivative model of a Hilbert space

The fundamental theorem for absolutely continuous functions gives
$f(t)=\int_0^t f'(s)\,ds$ because $f(0)=0$. The map $D:f\mapsto f'$
is linear, injective, and preserves the proposed inner product.
It is onto $L^2(0,1)$: for $g\in L^2(0,1)\subset L^1(0,1)$ the function
$f(t)=\int_0^t g(s)\,ds$ is absolutely continuous with derivative $g$
almost everywhere. In particular the proposed form is positive definite.
If $(f_n)$ is Cauchy, completeness of $L^2$ gives $f_n'\to g$; the preceding
integral defines $f$ with $\|f_n-f\|_{\mathcal H}=\|f_n'-g\|_2\to0$.
This proves completeness without assuming it in advance.

#### Solution I.1.4 — The three completions

For a positive weight sequence $w$, put
$\ell^2(w)=\{a:\sum_nw_n|a_n|^2<\infty\}$ with its weighted inner product.
The map $a\mapsto(\sqrt{w_n}a_n)_n$ is an onto isometry to $\ell^2$,
so this is complete. Truncations converge since the weighted square-sum
tails tend to zero, so finite-support sequences are dense. The three
completions are therefore, respectively,

$$
\ell^2,\qquad
\left\{a:\sum_{n\geq1}\frac{|a_n|^2}{n}<\infty\right\},\qquad
\left\{a:\sum_{n\geq1}n^5|a_n|^2<\infty\right\},
$$

with the corresponding weighted norms, not the unweighted norm in all three
cases. This identifies the completions together with their original dense
subspaces.

#### Solution I.1.5 — Completeness with several derivatives

All derivatives here have their usual continuous representatives when these
are required in the question. We first record an estimate. For an absolutely
continuous $u$ on $[0,1]$,

$$
\|u\|_\infty\leq\|u\|_1+\|u'\|_1
\leq\|u\|_2+\|u'\|_2.
$$

Indeed $|u(t)|\leq|u(s)|+\int_0^1|u'|$; integrate in $s$, then use
Cauchy–Schwarz. This estimate converts control of two consecutive derivatives
into uniform control of the lower one.

Suppose $(f_j)$ is Cauchy in the proposed norm. For $1\leq k\leq n$,
let $g_k\in L^2$ be the limit of $f_j^{(k)}$. The estimate makes
$f_j^{(k)}$ uniformly Cauchy for $1\leq k<n$. Write their continuous
uniform limits as $u_k$, which represent $g_k$. Passing to the limit in the
fundamental-theorem identities gives

$$
u_k(t)=u_k(0)+\int_0^t u_{k+1}(s)\,ds\quad(1\leq k<n-1),
\qquad
u_{n-1}(t)=u_{n-1}(0)+\int_0^t g_n(s)\,ds.
$$

The last passage is valid uniformly because $L^2$ convergence implies $L^1$
convergence here. Define $f(t)=\int_0^t u_1(s)\,ds$. These identities show
that $f$ has exactly the regularity required, $f^{(k)}=u_k$ for $k<n$,
and $f^{(n)}=g_n$ almost everywhere. Hence $f_j\to f$ in the given norm.
Sesquilinearity and symmetry follow termwise; if the squared norm is zero,
then $f'=0$ almost everywhere and $f(0)=0$, so $f=0$. This proves all
Hilbert-space axioms. Notice that the values of the higher derivatives at
zero were not assumed to vanish.

#### Solution I.1.6 — Removing the null space of a semi-inner product

The Cauchy–Schwarz inequality also holds for a semi-inner product:
$|u(x,y)|^2\leq u(x,x)u(y,y)$. It follows by expanding the nonnegative
quantity $u(x-ty,x-ty)$ and minimizing when $u(y,y)>0$; when $u(y,y)=0$,
nonnegativity for every scalar $t$ forces $u(x,y)=0$.
Thus $n\in\mathcal N$ implies $u(n,x)=u(x,n)=0$ for all $x$.

(a) For $n,m\in\mathcal N$, expansion gives
$u(\alpha n+\beta m,\alpha n+\beta m)=0$. Hence $\mathcal N$ is a subspace.
(b) Replacing $x,y$ by $x+n,y+m$ leaves $u(x,y)$ unchanged, so the quotient
form is well defined. It inherits symmetry, linearity, and positivity.
Its squared norm vanishes precisely when $x\in\mathcal N$, which means
$x+\mathcal N$ is the zero coset. Thus it is an inner product.

#### Solution I.1.7 — Complexification

Take $\mathcal K=\mathcal H\times\mathcal H$, writing $(x,y)$ as $x+iy$.
Define $(a+ib)(x+iy)=(ax-by)+i(bx+ay)$, and set

$$
\langle x+iy,u+iv\rangle_{\mathcal K}
=\langle x,u\rangle+\langle y,v\rangle
+i\bigl(\langle y,u\rangle-\langle x,v\rangle\bigr).
$$

Using the symmetry of the real inner product, expansion verifies complex
linearity in the first variable and conjugate symmetry. The squared norm is
$\|x\|^2+\|y\|^2$, which is positive unless both coordinates vanish.
A Cauchy sequence is Cauchy in each coordinate, so completeness follows
from that of $\mathcal H$. Define $Ux=x+i0$. It is real-linear, preserves
inner products, and every pair has the unique representation $Ux+iUy$.
Real-linearity is the appropriate meaning of (a), since the domain is real.

#### Solution I.1.8 — A square-integrable puncture is removable

Use the Laurent expansion proved in
[CA.40](background-complex-analysis.md#ca-40):
$f(z)=\sum_{k\in\mathbb Z}a_kz^k$ on $0<|z|<1$.
For $m\geq1$, the circle coefficient formula and Cauchy–Schwarz give

$$
|a_{-m}|^2r^{-2m}
=\left|\frac1{2\pi}\int_0^{2\pi}f(re^{it})e^{imt}\,dt\right|^2
\leq\frac1{2\pi}\int_0^{2\pi}|f(re^{it})|^2\,dt.
$$

Fix $0<R<1$. Multiply by $2\pi r$ and integrate from $\delta$ to $R$.
The right side is at most $\|f\|_{L^2(G)}^2$, whereas the left side is
$2\pi|a_{-m}|^2\int_\delta^Rr^{1-2m}\,dr$. The integral diverges as
$\delta\downarrow0$ for every $m\geq1$ (logarithmically for $m=1$).
Thus every negative Laurent coefficient is zero. The remaining power
series extends holomorphically across zero with value $a_0$.
This argument excludes essential singularities as well as poles.

#### Solution I.1.9 — The entire-plane Bergman space

For an entire function, the disk mean-value estimate
[CA.48](background-complex-analysis.md#ca-48) says

$$
|f(a)|^2\leq\frac1{\pi R^2}\int_{|z-a|<R}|f(z)|^2\,dA(z)
\leq\frac{\|f\|_2^2}{\pi R^2}.
$$

Let $R\to\infty$. If $f\in L_a^2(\mathbb C)$, the numerator is finite,
so $f(a)=0$ for every $a$. Conversely zero is square integrable and entire.
Consequently $L_a^2(\mathbb C)=\{0\}$.

#### Solution I.1.10 — Closedness of a vanishing condition

Choose $r>0$ with $\overline{D(a,r)}\subset G$. The same estimate yields
$|f(a)|\leq(\sqrt\pi r)^{-1}\|f\|_{L^2(G)}$.
Thus evaluation at $a$ is a bounded linear functional. If $f_j\to f$ in
the Bergman norm and $f_j(a)=0$, applying the bound to $f-f_j$ proves
$f(a)=0$. Hence the evaluation kernel is closed. Evaluation is taken on
the unique holomorphic representative: two continuous functions agreeing
almost everywhere on an open set agree everywhere.

#### Solution I.1.11 — Absolutely summable vector series

For $m>n$, the triangle inequality gives
$\|\sum_{k=n+1}^m h_k\|\leq\sum_{k=n+1}^m\|h_k\|$.
The scalar tail tends to zero uniformly in $m>n$, so the partial sums are
Cauchy. Completeness produces their limit in $\mathcal H$. This proves
convergence in the given order; unordered convergence is addressed in I.4.11.

### §2. Orthogonality

#### Solution I.2.1 — Strict convexity of the unit ball

Expansion of squared norms gives, for unit vectors,

$$
\|tf+(1-t)g\|^2=1-t(1-t)\|f-g\|^2.
$$

Linear independence implies $f\ne g$, so the right side is less than one
when $0<t<1$. In fact distinct unit vectors suffice. If either endpoint
has norm less than one, the triangle inequality also gives a strict bound
for every proper convex combination. Thus the closed unit ball is strictly
convex: the open segment between any two distinct points of the ball lies
in its interior. In particular its unit sphere contains no nontrivial
line segment.

#### Solution I.2.2 — The complementary projection

The orthogonal decomposition is $h=Ph+(h-Ph)$, with $Ph\in\mathcal M$
and $h-Ph\in\mathcal M^\perp$. Since $\mathcal M$ is closed,
$(\mathcal M^\perp)^\perp=\mathcal M$. Therefore $h-Ph$ is exactly the
$\mathcal M^\perp$ component of $h$. Uniqueness of the orthogonal
decomposition shows $P_{\mathcal M^\perp}=I-P$.

#### Solution I.2.3 — Topologically complementary subspaces

If $h\in\mathcal M\cap\mathcal M^\perp$, then $\langle h,h\rangle=0$,
so $h=0$. The projection theorem gives the required decomposition, and the
zero intersection makes it unique. Consequently $T(f,g)=f+g$ is a linear
bijection with inverse $h\mapsto(Ph,(I-P)h)$.
On the product use the norm $(\|f\|^2+\|g\|^2)^{1/2}$; it induces the
product topology because it is between $\max(\|f\|,\|g\|)$ and
$\sqrt2\max(\|f\|,\|g\|)$. Orthogonality gives
$\|T(f,g)\|^2=\|f\|^2+\|g\|^2$. Thus $T$ and its inverse are continuous,
as required.

#### Solution I.2.4 — Closed linear span

(a) Arbitrary intersections of closed sets are closed, and intersections
of linear subspaces are linear subspaces. The family being intersected is
nonempty since it contains $\mathcal H$. Its intersection contains $A$
and is contained in every closed linear subspace containing $A$.

(b) Write $S=\operatorname{span}A$. Continuity of addition and scalar
multiplication shows $\overline S$ is a linear subspace: if $x_j\to x$
and $y_j\to y$ with $x_j,y_j\in S$, then
$\alpha x_j+\beta y_j\to\alpha x+\beta y$. It is a closed subspace
containing $A$, so $\bigvee A\subseteq\overline S$. Every closed subspace
containing $A$ contains $S$ and then $\overline S$, proving the reverse
inclusion. If $A=\varnothing$, use the usual convention
$\operatorname{span}\varnothing=\{0\}$, allowing an empty sum. Literally
requiring $n\geq1$ in the printed set without this convention would give
the empty set in that exceptional case.

#### Solution I.2.5 — The double orthogonal complement

Put $M=\overline{\operatorname{span}A}$. A vector orthogonal to $A$ is
orthogonal to finite linear combinations and, by continuity of the inner
product, to their limits. Hence $A^\perp=M^\perp$. For a closed subspace,
the projection theorem gives $(M^\perp)^\perp=M$: if $x=m+n$ with
$n\in M^\perp$ and $x\perp M^\perp$, then
$0=\langle x,n\rangle=\|n\|^2$. Therefore
$(A^\perp)^\perp=M$, proving Corollary 2.10.

#### Solution I.2.6 — Density and the orthogonal complement

For a linear manifold $Y$, I.2.5 gives
$\overline Y=(Y^\perp)^\perp$. If $Y^\perp=\{0\}$, this equals
$\mathcal H$. Conversely, if $\overline Y=\mathcal H$, continuity implies
$Y^\perp=\mathcal H^\perp=\{0\}$. This proves both implications of
Corollary 2.11.

### §3. The Riesz Representation Theorem

#### Solution I.3.1 — Equivalent formulas for the functional norm

Assume first $\mathcal H\ne\{0\}$. Let
$M=\sup_{\|x\|=1}|Lx|$. Normalizing each nonzero $h$ gives
$|Lh|/\|h\|=|L(h/\|h\|)|$, so the first two suprema in Proposition 3.3
are equal. The same calculation proves $|Lh|\leq M\|h\|$ for every $h$,
including zero. Every admissible bound $c$ is at least $M$, while every
$c>M$ is admissible, so the stated infimum is $M$. The supremum over the
unit ball is also $M$: it is at least the sphere supremum and at most $M$
by this bound. If the norm is defined using the open unit ball, approach
each unit vector by $rx$ with $r\uparrow1$ to obtain the same value.
For the zero space the functional and norm are zero; sphere formulas
require the convention that this nonnegative empty supremum is zero.

#### Solution I.3.2 — A coordinate functional

Take $h_0=e_N$, the sequence with a one in position $N$ and zeros elsewhere.
Then $\langle h,e_N\rangle=\alpha_N$. Its norm is one, so the functional
has norm one, attained at $e_N$. Riesz uniqueness also follows directly:
if two representers worked, their difference would be orthogonal to every
vector, and hence to itself.

#### Solution I.3.3 — Evaluation of a square-summable power series

(a) For $0\leq r<1$, Cauchy–Schwarz gives

$$
\sum_{n\geq0}|\alpha_n|r^n
\leq\left(\sum_{n\geq0}|\alpha_n|^2\right)^{1/2}
\left(\sum_{n\geq0}r^{2n}\right)^{1/2}
=\frac{\|\alpha\|_2}{\sqrt{1-r^2}}.
$$

Thus the series converges absolutely in the unit disk and uniformly on
every smaller closed disk (apply the same estimate to tails); its radius
is at least one.
(b) Take $h_0=(1,\overline\lambda,\overline\lambda^2,\ldots)$.
Conjugating its coordinates in the inner product gives exactly $L(h)$.
(c) Its norm, and hence the functional norm, is
$(1-|\lambda|^2)^{-1/2}$; equality in the norm bound is attained at
$h_0/\|h_0\|$. In the real-scalar version take real $\lambda$; nonreal
evaluation is naturally a functional on the complex space.

#### Solution I.3.4 — Derivative evaluation

The representer has coordinates
$h_{0,0}=0$ and $h_{0,n}=n\overline\lambda^{\,n-1}$ for $n\geq1$.
At $\lambda=0$ this means $(0,1,0,\ldots)$. Differentiating the geometric
series inside its radius of convergence gives

$$
\|h_0\|^2=\sum_{n\geq1}n^2|\lambda|^{2n-2}
=\frac{1+|\lambda|^2}{(1-|\lambda|^2)^3}<\infty.
$$

For example $\sum n^2x^{n-1}$ is the derivative of
$\sum nx^n=x/(1-x)^2$. Thus the inner product with $h_0$ is well defined
and equals the displayed derivative series. Termwise differentiation is
justified by [CA.25](background-complex-analysis.md#ca-25), not merely by
pointwise convergence of the original series.

#### Solution I.3.5 — Evaluation in the derivative space

Since $h(0)=0$, $h(t)=\int_0^t h'(s)\,ds$, and Cauchy–Schwarz gives
$|h(t)|\leq\sqrt t\,\|h\|_{\mathcal H}$. Set $h_0(s)=\min(s,t)$.
It belongs to $\mathcal H$, has derivative $\mathbf1_{(0,t)}$ almost
everywhere, and
$\langle h,h_0\rangle=\int_0^t h'(s)\,ds=h(t)$.
Its norm is $\sqrt t$. Testing on $h_0/\sqrt t$ proves that the upper
bound is sharp: $\|L\|=\sqrt t$.

#### Solution I.3.6 — Derivative evaluation is not bounded in the L² norm

Fix the specified $t\in[0,1]$ and put
$h_n(s)=n^{-1}\sin(n(s-t))$. These functions are continuously differentiable,
$h_n'(t)=1$, and $\|h_n\|_2\leq1/n\to0$. If a bounded extension $\widetilde L$
existed, continuity would imply $\widetilde L(h_n)\to0$, but agreement on
$C^{(1)}$ requires $\widetilde L(h_n)=1$. This contradiction also covers
the endpoints, where the derivative is understood one-sidedly. The issue
is the chosen norm: the $L^2$ norm does not control pointwise derivatives.

### §4. Orthonormal Sets of Vectors and Bases

#### Solution I.4.1 — Complex exponentials

For integers $m,n$,
$\langle e_n,e_m\rangle=(2\pi)^{-1}\int_0^{2\pi}e^{i(n-m)t}\,dt$.
If $n=m$ this is one. Otherwise the antiderivative is
$e^{i(n-m)t}/(i(n-m))$, whose endpoint values agree, so the integral is
zero. Thus the system is orthonormal, as asserted in Example 4.3.
The further completeness claim is established by the Fourier theorem in
§5; a real trigonometric form is discussed in I.5.7.

#### Solution I.4.2 — The finite coordinate basis

Direct calculation gives $\langle e_j,e_k\rangle=\delta_{jk}$. Every
$x\in\mathbb F^d$ is the finite sum $\sum_{k=1}^d x_ke_k$, so the
orthonormal set spans the space and is maximal. It is therefore a Hilbert
basis as well as an algebraic basis in this finite-dimensional case.

#### Solution I.4.3 — The coordinate basis on an arbitrary index set

Again $\langle e_i,e_j\rangle=\delta_{ij}$. For $a\in\ell^2(I)$ and
$\varepsilon>0$, the definition of the finite-subset supremum provides
a finite $F\subset I$ with $\sum_{i\notin F}|a_i|^2<\varepsilon^2$.
Hence $\|a-\sum_{i\in F}a_ie_i\|<\varepsilon$. Their span is dense, so
they form a Hilbert basis. Equivalently, a vector orthogonal to them all
has every coordinate zero, and no further unit vector can be adjoined.

#### Solution I.4.4 — An orthonormal set in the derivative space

For $n\geq1$, define
$f_n(t)=\sqrt2(1-\cos(n\pi t))/(n\pi)$. Then $f_n(0)=0$ and
$f_n'(t)=\sqrt2\sin(n\pi t)$, so $f_n\in\mathcal H$.
Using $2\sin a\sin b=\cos(a-b)-\cos(a+b)$ shows
$\int_0^1 2\sin(n\pi t)\sin(m\pi t)\,dt=\delta_{nm}$:
nonconstant integer-frequency cosines have zero integral, and for $m=n$
the constant term integrates to one. Thus $(f_n)_{n\geq1}$ is the requested
infinite orthonormal set.

#### Solution I.4.5 — The determinant form of Gram–Schmidt

Let $A_{ji}=\langle h_i,h_j\rangle$ for $1\leq i,j<n$ and
$b_j=\langle h_n,h_j\rangle$. The Gram matrix is invertible: if $Ac=0$,
then $\sum_i c_i h_i$ is orthogonal to every $h_j$ and hence to itself;
linear independence forces $c=0$. The projection of $h_n$ onto their
span is $f_n=\sum_i c_i h_i$, where $Ac=b$, since these equations say
$h_n-f_n$ is orthogonal to that span.

In the formal determinant of the exercise, subtract from its last column
the combination of the first $n-1$ columns with coefficients $c_i$.
Its upper entries become $b-Ac=0$ and its last entry becomes $-f_n$.
Expansion along that column yields $-\det(A)f_n$. The denominator in
the exercise is $\det(A^{\mathsf T})=\det(A)$, proving the stated formula.
This argument interprets the vector-valued last row by cofactor expansion,
so no multiplication of vectors is intended.
Finally $h_n-f_n\ne0$ by independence. Normalizing it produces the next
orthonormal vector, and adjoining it preserves the finite span. Starting
with $e_1=h_1/\|h_1\|$ proves Gram–Schmidt inductively. Multiplication of
each resulting vector by a scalar of modulus one is harmless.

#### Solution I.4.6 — Legendre polynomials

Rodrigues' formula gives a degree-$n$ polynomial $P_n$ with leading
coefficient $c_n=(2n)!/(2^n(n!)^2)$. For any polynomial $q$ of degree
less than $n$, integration by parts $n$ times gives

$$
\int_{-1}^1P_n(x)q(x)\,dx
=\frac{(-1)^n}{2^n n!}\int_{-1}^1(x^2-1)^n q^{(n)}(x)\,dx=0.
$$

All boundary terms vanish because $(x^2-1)^n$ has zeros of order $n$
at both endpoints. Repeating with $q=P_n$, whose $n$th derivative is
$n!c_n$, gives $\|P_n\|_2^2=(c_n/2^n)J_n$, where
$J_n=\int_{-1}^1(1-x^2)^n\,dx$. Integrating the derivative of
$x(1-x^2)^n$ gives
$0=J_n-2n(J_{n-1}-J_n)$, so
$J_n=2nJ_{n-1}/(2n+1)$ and $J_0=2$. Consequently
$J_n=2^{2n+1}(n!)^2/(2n+1)!$, and
$\|P_n\|_2^2=2/(2n+1)$.
Thus $\sqrt{(2n+1)/2}\,P_n$ are normalized and each is orthogonal to all
earlier monomials. Their degrees and positive leading coefficients identify
them with Gram–Schmidt applied to $1,x,x^2,\ldots$.

#### Solution I.4.7 — Hermite polynomials

Differentiating Rodrigues' formula gives
$H_{n+1}=2xH_n-H_n'$, starting with $H_0=1$. Hence $H_n$ is a polynomial
of degree $n$ with leading coefficient $2^n$. For $\deg q<n$,

$$
\int_{\mathbb R}H_n(x)q(x)e^{-x^2}\,dx
=\int_{\mathbb R}e^{-x^2}q^{(n)}(x)\,dx=0.
$$

Here integrate by parts first on finite intervals and then let the
endpoints tend to infinity; every boundary term is a polynomial times a
Gaussian and tends to zero. Taking $q=H_n$ instead gives
$\int H_n^2e^{-x^2}=2^n n!\sqrt\pi$. The Gaussian integral follows by
squaring $\int e^{-x^2}$, using polar coordinates on the plane, and
evaluating $2\pi\int_0^\infty re^{-r^2}\,dr=\pi$.
These computations prove the claimed orthonormalization, since multiplying
polynomials by $e^{-x^2/2}$ turns the weighted integral into the usual
$L^2(\mathbb R)$ inner product.

For the derivative identity, Taylor-expand the entire function
$e^{-(x-t)^2}$ in $t$ and multiply by $e^{x^2}$ to get
$e^{2xt-t^2}=\sum_{n\geq0}H_n(x)t^n/n!$. Differentiate in $x$ and compare
coefficients with $2t e^{2xt-t^2}$. This yields
$H_n'=2nH_{n-1}$ for $n\geq1$. The expansions and differentiation hold
locally uniformly, as follows also from the exponential power series.

#### Solution I.4.8 — Laguerre polynomials and their normalization

With the convention in the question, Leibniz' rule gives

$$
L_n(x)=\sum_{k=0}^n\binom nk\frac{n!}{k!}(-1)^k x^k.
$$

Thus the leading coefficient is $(-1)^n$. If $\deg q<n$, integration
by parts $n$ times gives
$\int_0^\infty L_nq e^{-x}\,dx=(-1)^n\int_0^\infty x^ne^{-x}q^{(n)}\,dx=0$.
At zero, every derivative of $x^ne^{-x}$ of order less than $n$ vanishes;
at infinity, the exponential dominates all polynomial factors. These facts
justify all boundary cancellations. Taking $q=L_n$ and using
$L_n^{(n)}=(-1)^n n!$ gives
$\int_0^\infty L_n^2e^{-x}\,dx=n!\int_0^\infty x^ne^{-x}\,dx=(n!)^2$,
where the final integral is $n!$ by repeated integration by parts.
Therefore $e^{-x/2}L_n(x)/n!$ is orthonormal and has the required successive
spans. Its sign differs by $(-1)^n$ from the positive-leading-coefficient
Gram–Schmidt convention; this is the allowed choice of unit scalar.
Some references call $L_n/n!$, rather than $L_n$, the Laguerre polynomial.

#### Solution I.4.9 — Bessel's inequality as a finite-subset net

For finite $F\subset\mathscr E$, write
$s_F=\sum_{e\in F}|\langle h,e\rangle|^2$. Bessel's finite inequality
says $0\leq s_F\leq\|h\|^2$. Let $s=\sup_Fs_F$.
Given $\varepsilon>0$, choose finite $F_0$ with $s-s_{F_0}<\varepsilon$.
Whenever $F\supseteq F_0$, monotonicity gives
$0\leq s-s_F\leq s-s_{F_0}<\varepsilon$. This is precisely convergence
of the net in Definition 4.11, and its limit satisfies $s\leq\|h\|^2$.
No enumeration of the orthonormal set is needed.

#### Solution I.4.10 — Ordered versus unordered convergence

If the finite-subset net tends to $h$, choose a finite controlling set
$F_0\subset\mathbb N$. Every initial segment $\{1,\ldots,n\}$ with
$n\geq\max F_0$ contains $F_0$, so its sum is close to $h$. Thus the
ordered series converges to $h$.
For the converse take $h_n=(-1)^{n+1}/n$ in the Hilbert space $\mathbb R$.
The alternating-series estimate proves its ordered series converges.
But beyond any prescribed finite set, finitely many unused positive terms
can have sum larger than one, since the odd harmonic subseries diverges.
The two finite-subset sums before and after adjoining those terms differ
by more than one. The net is not Cauchy and cannot converge.

#### Solution I.4.11 — Absolute convergence implies unordered convergence

Let $h$ be the ordered sum, which exists by I.1.11. Choose $N$ such that
$\sum_{n>N}\|h_n\|<\varepsilon$. For any finite $F$ containing
$\{1,\ldots,N\}$, subtract its terms from the convergent ordered series.
The remaining series has norm at most
$\sum_{n\notin F}\|h_n\|\leq\sum_{n>N}\|h_n\|<\varepsilon$.
Thus $\|h-\sum_{n\in F}h_n\|<\varepsilon$, exactly the required net
convergence. This estimate handles arbitrary extra indices in $F$.

#### Solution I.4.12 — Three scalar notions of absolute convergence

(c) implies (a) by the preceding solution. To show (a) implies (b), fix a
permutation $\pi$. For every finite $F_0$, its elements eventually all
occur in $\{\pi(1),\ldots,\pi(N)\}$. Applying the defining net estimate
therefore proves convergence of that rearranged series to the same limit.

For (b) implies (c), first consider real terms. By the identity permutation
the series converges. If it is not absolutely convergent, the sum of its
positive terms is $+\infty$ and the sum of the absolute values of its
negative terms is $+\infty$: otherwise convergence of the original partial
sums would force both sums to be finite. List positive and negative terms
in their original order. Take positive terms until the running sum exceeds
one, then negative terms until it is below zero, and repeat. At each stage
take at least the next unused term of the appropriate sign, and insert the
next unused zero term, if any. The divergent positive and negative totals
make every stage possible; every term is eventually used. The resulting
permutation has partial sums alternately above one and below zero, so does
not converge, contradicting (b).
For complex terms, (b) holds for both real and imaginary parts, hence both
are absolutely summable by the real case. Since
$|\alpha_n|\leq|\operatorname{Re}\alpha_n|+|\operatorname{Im}\alpha_n|$,
(c) follows.

#### Solution I.4.13 — Projection onto a possibly uncountable orthonormal span

Put $c_e=\langle h,e\rangle$. By I.4.9, $\sum_e|c_e|^2<\infty$.
Only countably many $c_e$ are nonzero, since for each $m$ only finitely
many can have modulus at least $1/m$. Enumerate those nonzero coefficients.
Orthogonality gives a squared norm of $\sum|c_e|^2$ for every finite sum
and for every difference of such sums. Thus their ordered partial sums
are Cauchy, and the same square-tail bound shows the full finite-subset
net converges to a vector $v\in M$.
For each $e\in\mathscr E$, continuity gives $\langle v,e\rangle=c_e$;
hence $h-v\perp\mathscr E$ and therefore $h-v\perp M$. Uniqueness of
the orthogonal decomposition proves $v=Ph$.

#### Solution I.4.14 — Monomials on the unit disk

Polar coordinates give

$$
\langle z^n,z^m\rangle
=\int_0^1r^{n+m+1}\,dr\int_0^{2\pi}e^{i(n-m)t}\,dt
=\begin{cases}\pi/(n+1),&n=m,\\0,&n\ne m.\end{cases}
$$

Thus $\|z^n\|=\sqrt{\pi/(n+1)}$ and
$e_n=\sqrt{(n+1)/\pi}\,z^n$ is orthonormal. It is not a basis of the
whole $L^2$ space: the nonzero vector $g(z)=\overline z$ belongs to it and
has $\langle g,z^n\rangle=\int_{|z|<1}\overline z^{\,n+1}\,dA=0$
for all $n\geq0$. The distinction is between all square-integrable
functions and the holomorphic subspace.

#### Solution I.4.15 — Equality of finite basis cardinalities

Suppose one orthonormal basis has $d<\infty$ elements. Its span is closed
(coordinates in a finite orthonormal set converge whenever the vectors
converge) and dense, so the Hilbert space has algebraic dimension $d$.
Any other orthonormal set is linearly independent, hence has at most $d$
elements. If it is a basis, its finite span is the whole space, so it has
at least $d$ elements. Thus both cardinalities are $d$. Interchanging the
two bases covers the case where the second is the one known to be finite.

#### Solution I.4.16 — Hilbert bases are not Hamel bases

Choose countably many distinct members $(e_n)$ of an infinite orthonormal
basis. The series $h=\sum_{n\geq1}2^{-n}e_n$ converges, and
$\langle h,e_n\rangle=2^{-n}\ne0$ for every $n$. A finite combination
of members of the basis has zero coefficients outside that finite set.
Hence $h$ is not such a combination, so the basis is not a Hamel basis.

For the second assertion, here is the needed Baire argument. A nonempty
complete metric space cannot be a countable union of closed sets with
empty interior. Otherwise, recursively choose nonempty closed balls with
radii tending to zero, each inside the previous open ball and avoiding
the next closed set. Their centers form a Cauchy sequence, whose limit
lies in every closed ball and hence avoids every set, a contradiction.
If $(b_n)$ were a countable Hamel basis, then
$\mathcal H=\bigcup_n\operatorname{span}(b_1,\ldots,b_n)$.
Each finite-dimensional span is closed: orthonormalize a finite basis and
use coordinate convergence. It is proper, and a proper linear subspace
has empty interior, since containing a ball would, by subtraction and
scaling, make it the whole space. Baire gives a contradiction. Thus every
Hamel basis is uncountable. This uses the usual choice principles behind
Hamel bases and Hilbert bases.

#### Solution I.4.17 — Separability for a regular Borel measure

Here regular Borel measure has the book's locally finite convention:
compact sets have finite measure. Consequently bounded boxes have finite
measure and increasing compact cubes make $\mu$ sigma-finite.
Let $\mathcal R$ be the countable collection of finite unions of bounded
open boxes with rational endpoints. We claim that indicators of members
of $\mathcal R$ approximate indicators of Borel sets of finite measure.

For such a set $E$ and $\delta>0$, regularity provides compact $K\subset E$
and open $O\supset E$ with $\mu(E\setminus K)<\delta$ and
$\mu(O\setminus E)<\delta$. Cover $K$ by finitely many rational boxes
contained in $O$ and call their union $R$. Then $K\subset R\subset O$,
so $\mu(E\mathbin\triangle R)<2\delta$ and
$\|\mathbf1_E-\mathbf1_R\|_2<\sqrt{2\delta}$.
The empty compact set causes no difficulty; the empty union is allowed.
If the measure space is completed, replace a measurable set by a Borel
representative modulo null sets.

Every $L^2$ function can first be cut off on a large compact cube and at a
large absolute value, with small $L^2$ error by dominated convergence.
The resulting bounded function on a finite-measure set can be approximated
by a simple function by dividing its bounded range into small intervals
(or squares for complex values). Approximate each indicator as above and
then approximate each coefficient by a rational real number, or a complex
number with rational real and imaginary parts. The finite rational linear
combinations of these countably many indicators form a countable dense
set. Therefore $L^2(\mu)$ is separable.

#### Solution I.4.18 — Disjoint positive-measure sets

The functions $e_i=\mathbf1_{E_i}/\sqrt{\mu(E_i)}$ are well-defined unit
vectors, and disjointness makes them orthogonal. Thus distinct ones have
distance $\sqrt2$. In a separable metric space a set of points separated
by this distance is countable: balls of radius $1/3$ around them are
disjoint, and each contains a distinct member of a fixed countable dense
set. Hence $I$ is countable.

Infinite measures cannot be allowed in this generality. On an uncountable
set $X$ take all subsets measurable and set $\mu(\varnothing)=0$ and
$\mu(E)=\infty$ for every nonempty $E$. This is countably additive:
a disjoint union is nonempty exactly when at least one term is nonempty,
in which case both sides of countable additivity are infinite. Every
nonzero function has a nonempty set where $|f|\geq1/n$ for some $n$, so
its squared integral is infinite. Thus $L^2(\mu)=\{0\}$ is separable,
although the uncountable family of singleton sets is disjoint and each
has infinite measure. Extra hypotheses such as sigma-finiteness would
exclude this example.

#### Solution I.4.19 — Compact unit ball forces finite dimension

If the space were infinite dimensional, inductively choose a unit vector
orthogonal to the span of all previously chosen ones. Such a vector exists
because a finite-dimensional subspace is closed and proper. This produces
an orthonormal sequence in the unit ball. Its distinct members have distance
$\sqrt2$, so it has no Cauchy subsequence and hence no convergent subsequence.
But compact metric spaces are sequentially compact (successively use
finite covers by balls of radius $1,1/2,1/4,\ldots$ to extract a Cauchy
subsequence). This contradiction proves finite dimension.

#### Solution I.4.20 — The Hamel dimension of ℓ²

Write $\mathfrak c=|\mathbb R|$. Since $\ell^2\subset\mathbb F^{\mathbb N}$,
its cardinality is at most
$\mathfrak c^{\aleph_0}=(2^{\aleph_0})^{\aleph_0}=\mathfrak c$;
the exponent identity follows by identifying a sequence of binary
sequences with a binary function on the countable set $\mathbb N^2$.
Thus any Hamel basis has cardinality at most $\mathfrak c$.

For each $0<t<1$ let $v_t=(1,t,t^2,\ldots)\in\ell^2$. Any finite set
of these vectors with distinct parameters $t_1,\ldots,t_m$ is linearly
independent: its first $m$ coordinate equations form a Vandermonde matrix
with nonzero determinant $\prod_{i<j}(t_j-t_i)$. Hence these vectors form
a linearly independent family of cardinality $\mathfrak c$. Extending it
to a Hamel basis proves the opposite dimension bound. The Hamel dimension
is therefore exactly $\mathfrak c$, over either $\mathbb R$ or $\mathbb C$.

### §5. Isomorphic Hilbert Spaces and the Fourier Transform for the Circle

#### Solution I.5.1 — The unilateral shift

The map $S(a_1,a_2,\ldots)=(0,a_1,a_2,\ldots)$ is linear and
$\|Sa\|_2^2=\sum_{n\geq1}|a_n|^2=\|a\|_2^2$. Its range is exactly
the sequences with first coordinate zero, since deleting that coordinate
gives a preimage. In particular $e_1$ is not in its range. Thus $S$ is an
isometry but not surjective, as Example 5.3 asserts.

#### Solution I.5.2 — Translation with a zero initial interval

Translation preserves null sets, so the formula defines a linear map on
$L^2$ equivalence classes. Substitution $s=t-1$ gives
$\|Vf\|_2^2=\int_1^\infty|f(t-1)|^2\,dt=\int_0^\infty|f(s)|^2\,ds$.
Every image vanishes almost everywhere on $(0,1)$, so
$\mathbf1_{(0,1)}$ has no preimage. Conversely any $g$ vanishing there
has preimage $f(s)=g(s+1)$. This identifies the range and proves failure
of surjectivity.

#### Solution I.5.3 — Bilateral translation

Substitution on the whole real line proves $\|Vf\|_2=\|f\|_2$, and the
map is linear and well defined modulo null sets. The formula
$(Wg)(t)=g(t+1)$ defines an isometry as well, and $WV=VW=I$. Hence $V$
is onto and is a unitary operator on $L^2(\mathbb R)$. Unlike the previous
problem, no interval is lost at an endpoint.

#### Solution I.5.4 — The derivative isomorphism

The calculation in I.1.3 shows directly that $Uf=f'$ is linear and
$\langle Uf,Ug\rangle_{L^2}=\langle f,g\rangle_{\mathcal H}$.
Its inverse is
$\displaystyle (U^{-1}g)(t)=\int_0^t g(s)\,ds$.
Indeed the fundamental theorem for absolute continuity proves both
$U(U^{-1}g)=g$ almost everywhere and $U^{-1}(Uf)=f$, using $f(0)=0$.
Thus $U$ is a Hilbert-space isomorphism.

#### Solution I.5.5 — Isometric multiplication operators

Boundedness of $u$ makes multiplication a bounded linear operator, since
$\|uf\|_2\leq\|u\|_\infty\|f\|_2$; here an essential bound also suffices.
If $|u|=1$ almost everywhere, this estimate is an equality for every $f$.
Moreover multiplication by $\overline u$ is an inverse, so $U$ is onto.

Conversely, if $U$ is an isometry, testing on $\mathbf1_E$ for every
finite-measure measurable $E$ gives
$\int_E(|u|^2-1)\,d\mu=0$. Let $X=\bigcup_j X_j$ with each $X_j$ of
finite measure. If $\{|u|^2-1>1/k\}\cap X_j$ had positive measure, the
displayed integral on that set would be strictly positive. The analogous
negative level set would give a strictly negative integral. All these
sets therefore have measure zero. Taking their countable union proves
$|u|^2-1=0$ almost everywhere. Sigma-finiteness is used precisely in this
reduction to finite-measure tests.

#### Solution I.5.6 — Density of continuous periodic representatives

Continuous functions on a compact interval are dense in Lebesgue $L^2$:
approximate by bounded simple functions, approximate their measurable sets
by finite unions of intervals in measure, and replace interval indicators
by continuous linear ramps near their endpoints. The squared $L^2$ error
of each bounded ramp replacement is at most its squared height times the
length of the altered endpoint regions, which can be made arbitrarily small.

Now let $g\in C[0,2\pi]$. Choose a continuous cutoff $\chi_\delta$ with
$0\leq\chi_\delta\leq1$, zero at both endpoints, and equal to one on
$[\delta,2\pi-\delta]$. Then $g\chi_\delta\in\mathcal C$ and
$\|g-g\chi_\delta\|_2^2\leq2\delta\|g\|_\infty^2\to0$.
Combining these approximations proves the desired density. Endpoint
values themselves have measure zero, but the cutoff is needed to retain
continuity while making them agree.

#### Solution I.5.7 — The real trigonometric orthonormal basis

Integration of the product-to-sum identities on $[-\pi,\pi]$ gives
$\int1=2\pi$, $\int\cos^2nt=\int\sin^2nt=\pi$ for $n\geq1$, and
zero for all mixed products or distinct frequencies. The stated constants
therefore make the system orthonormal.
For completeness, the Fourier theorem of this section says the normalized
complex exponentials for $n\in\mathbb Z$ span densely (translation of
the interval does not change this). The identities
$e^{int}=\cos nt+i\sin nt$ and
$e^{-int}=\cos nt-i\sin nt$ show that their complex span equals the span
of the displayed real trigonometric functions. Thus it is dense in complex
$L^2$; equivalently its orthogonal complement is zero. In real $L^2$,
take real parts of the approximating trigonometric polynomials, which does
not increase the error. This proves the real version as well.

#### Solution I.5.8 — Changing measure by a square-root density

Let $\phi=d\nu/d\mu\geq0$. We may assume it finite outside a $\mu$-null
set: if $\phi=\infty$ on a set of positive $\mu$ measure, intersecting
that set with a countable cover by finite-$\nu$ sets contradicts
$\nu(E)=\int_E\phi\,d\mu$. Define products to be zero on any exceptional
null set. The Radon–Nikodym integration identity gives

$$
\|Vf\|_{L^2(\mu)}^2=\int\phi|f|^2\,d\mu
=\int|f|^2\,d\nu=\|f\|_{L^2(\nu)}^2.
$$

Applied to a difference of representatives, this proves well-definedness;
it also proves the isometry assertion. Linearity follows pointwise.
Writing $Z=\{\phi=0\}$, the image is exactly the functions in $L^2(\mu)$
vanishing almost everywhere on $Z$. For such a function $g$, define
$f=g/\sqrt\phi$ off $Z$ and zero on $Z$; the same integral identity shows
$f\in L^2(\nu)$ and $Vf=g$.

Thus the map is onto if $\mu(Z)=0$. If $\mu(Z)>0$, sigma-finiteness of
$\mu$ provides $E\subset Z$ with $0<\mu(E)<\infty$, and
$\mathbf1_E$ is not in the image, so it is not onto. Finally
$\mu\ll\nu$ implies $\mu(Z)=0$ because $\nu(Z)=0$. Conversely if
$\mu(Z)=0$, then $\nu(E)=\int_E\phi\,d\mu=0$ implies $\mu(E)=0$
since $\phi>0$ almost everywhere. This proves the equivalence.

#### Solution I.5.9 — Inner-product preservation implies linearity

For scalars $\alpha,\beta$ and vectors $f,g$, put
$w=U(\alpha f+\beta g)-\alpha Uf-\beta Ug$. For every $h\in\mathcal H$,

$$
\langle w,Uh\rangle
=\langle\alpha f+\beta g,h\rangle
-\alpha\langle f,h\rangle-\beta\langle g,h\rangle=0.
$$

Surjectivity makes the vectors $Uh$ range over all of $\mathcal K$;
in particular one may take $Uh=w$. Hence $\|w\|^2=0$ and $w=0$.
This proves additivity and scalar homogeneity. Also
$\|U0\|^2=\langle0,0\rangle=0$, so zero is mapped to zero.

### §6. The Direct Sum of Hilbert Spaces

#### Solution I.6.1 — Disjoint unions of measure spaces

Regard the component spaces as disjoint tagged copies if necessary. Slicing
a complement or a countable union by $X_i$ commutes with that operation.
Since each $\Omega_i$ is a sigma-algebra, the given $\Omega$ is one too.
The function $\mu$ is nonnegative and vanishes on the empty set. If
$(\Delta_n)$ are disjoint, countable additivity on each component yields

$$
\mu\left(\bigcup_n\Delta_n\right)
=\sum_i\sum_n\mu_i(\Delta_n\cap X_i)
=\sum_n\sum_i\mu_i(\Delta_n\cap X_i)
=\sum_n\mu(\Delta_n).
$$

The interchange is valid for nonnegative terms even when $I$ is
uncountable: both iterated sums are the supremum of all sums over finite
subsets of $I\times\mathbb N$. Thus this is a measure.
For any nonnegative measurable $g$ one likewise has

$$
\int_Xg\,d\mu=\sum_i\int_{X_i}g|_{X_i}\,d\mu_i.
$$

First check this on indicators using the definition of $\mu$, then on
nonnegative simple functions by finite additivity of integrals. Approximate
an arbitrary $g$ increasingly by simple functions and use monotone
convergence; the increasing limit commutes with the finite-subset
supremum because each finite set of indices can be treated simultaneously.

Define $Rf=(f|_{X_i})_i$. A globally null set has a null slice in every
component, so this is well defined on equivalence classes. The integral
identity with $g=|f|^2$ shows $\|Rf\|^2=\|f\|_2^2$ and linearity is
immediate. Conversely, a square-summable family $(f_i)_i$ of $L^2$ classes
has at most countably many nonzero classes, because for every $m$ only
finitely many norms can be at least $1/m$. Choose measurable representatives
for those classes and the zero representative for all other components.
Glue them into a function $f$ on the disjoint union. It is measurable
because measurability is exactly slice-by-slice measurability here.
The identity gives $\|f\|_2^2=\sum_i\|f_i\|_2^2<\infty$, and $Rf=(f_i)$.
Thus $R$ is a surjective linear isometry, the requested isomorphism.

#### Solution I.6.2 — When the diagonal restriction map is onto

Since $\mu_j\leq\mu$, equality almost everywhere for $\mu$ implies
equality almost everywhere for both $\mu_j$. Thus $V$ is well defined,
and it is plainly linear. Moreover

$$
\|Vf\|^2=\int|f|^2\,d\mu_1+\int|f|^2\,d\mu_2
=\int|f|^2\,d\mu=\|f\|^2.
$$

It is therefore an isometry and injective. If $\mu_1\perp\mu_2$, choose
a measurable $A$ with $\mu_1(X\setminus A)=0$ and $\mu_2(A)=0$.
Given $g_1\oplus g_2$, glue representatives by
$f=\mathbf1_Ag_1+\mathbf1_{X\setminus A}g_2$. Its squared $\mu$ norm
is $\|g_1\|_{L^2(\mu_1)}^2+\|g_2\|_{L^2(\mu_2)}^2$, and $Vf=g_1\oplus g_2$.
This proves surjectivity in the mutually singular case.

Conversely suppose $V$ is onto. By sigma-finiteness choose measurable
$E_n$ covering $X$ with $\mu_1(E_n)<\infty$. For each $n$, surjectivity
provides a representative $f_n$ whose image is
$\mathbf1_{E_n}\oplus0$. Let $A_n=\{x:f_n(x)\ne0\}$.
The second coordinate implies $\mu_2(A_n)=0$, while the first implies
$\mu_1(E_n\setminus A_n)=0$. Set $A=\bigcup_nA_n$. Then
$\mu_2(A)=0$ and
$\mu_1(X\setminus A)\leq\sum_n\mu_1(E_n\setminus A_n)=0$.
This is mutual singularity. Thus $V$ is an isomorphism exactly under the
condition stated in the exercise.

<!-- END SOLUTIONS I -->
