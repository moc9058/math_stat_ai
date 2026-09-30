# I. Hilbert Spaces


<a id="pdf-page-16"></a>
CHAPTER I

# Hilbert Spaces

A Hilbert space is the abstraction of the finite-dimensional Euclidean spaces of geometry. Its properties are very regular and contain few surprises, though the presence of an infinity of dimensions guarantees a certain amount of surprise. Historically, it was the properties of Hilbert spaces that guided mathematicians when they began to generalize. Some of the properties and results seen in this chapter and the next will be encountered in more general settings later in this book, or we shall see results that come close to these but fail to achieve the full power possible in the setting of Hilbert space.

## §1. Elementary Properties and Examples

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

**1.8. Example.** Let $\mathcal H$ = the collection of all absolutely continuous functions $f:[0,1]\to\mathbb F$ such that $f(0)=0$ and $f'\in L^2(0,1)$. If $\langle f,g\rangle=\int_0^1 f'(t)\overline{g'(t)}\,dt$ for $f$ and $g$ in $\mathcal H$, then $\mathcal H$ is a Hilbert space (Exercise 3).

Suppose $\mathcal X$ is a vector space with an inner product $\langle\cdot,\cdot\rangle$ and the norm is defined by the inner product. What happens if $(\mathcal X,d)$ ($d(x,y)\equiv\|x-y\|$) is not complete?

**1.9. Proposition.** *If $\mathcal X$ is a vector space and $\langle\cdot,\cdot\rangle_{\mathcal X}$ is an inner product on $\mathcal X$ and if $\mathcal H$ is the completion of $\mathcal X$ with respect to the metric induced by the norm on $\mathcal X$, then there is an inner product $\langle\cdot,\cdot\rangle_{\mathcal H}$ on $\mathcal H$ such that $\langle x,y\rangle_{\mathcal H}=\langle x,y\rangle_{\mathcal X}$ for $x$ and $y$ in $\mathcal X$ and the metric on $\mathcal H$ is induced by this inner product. That is, the completion of $\mathcal X$ is a Hilbert space.*

The preceding result says that an incomplete inner product space can be completed to a Hilbert space. It is also true that a Hilbert space over $\mathbb R$ can be imbedded in a complex Hilbert space (see Exercise 7).

This section closes with an example of a Hilbert space from analytic function theory.

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

