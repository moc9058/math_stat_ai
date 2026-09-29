$\alpha u ( 0 , y ) = 0$ for all y in $\mathcal { X } .$ This and similar reasoning shows that for a semi-inner product u,

(e) $u(x,0)=u(0,y)=0$ for all $x , y$ in $\mathcal { X }$ p]

In particular, $u ( 0 , 0 ) = 0 .$

An inner product on $\mathcal { X }$ is a semi-inner product that also satisfies the following:

(f) If $u ( x , x ) = 0 .$ then $x = 0 .$

An inner product in this book will be denoted by

$$
\langle x , y \rangle = u ( x , y ) .
$$

There is no universally accepted notation for an inner product and the reader will often see $( x , y )$ and $( x | y )$ used in the literature.

1.2. Example. Let $\mathcal { X }$ be the collection of all sequences $\left\{ \alpha _ { n } ; n \geqslant 1 \right\}$ of scalars $\alpha _ { n }$ from $\mathbb { F }$ such that $\alpha _ { n }   =   0$ for all but a finite number of values of n. If addition and scalar multiplication are defined on $\mathcal { X }$ by

$$
\begin{aligned}\{ \alpha_{n} \} + \{ \beta_{n} \} & \equiv \{ \alpha_{n} + \beta_{n} \} , \\\alpha \{ \alpha_{n} \} & = \{ \alpha \alpha_{n} \} ,\end{aligned}
$$

then $\mathcal { X }$ is a vector space over $\mathbb { F } .$

If $u ( \{ \alpha _ { n } \} , \{ \beta _ { n } \} ) \equiv \sum _ { n = 1 } ^ { \infty } \alpha _ { 2 n } \bar { \beta } _ { 2 n }$ then u is a semi-inner product that is not an inner product. On the other hand,

$$
\langle \{ \alpha _ { n } \} , \{ \beta _ { n } \} \rangle = \sum _ { n = 1 } ^ { \infty } \alpha _ { n } \overline { { \beta } } _ { n } ,
$$

$$
\langle \{ \alpha _ { n } \} , \{ \beta _ { n } \} \rangle = \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n } \alpha _ { n } \overline { { \beta } } _ { n } ,
$$

$$
\langle \{ \alpha _ { n } \} , \{ \beta _ { n } \} \rangle = \sum _ { n = 1 } ^ { \infty } n ^ { 5 } \alpha _ { n } \overline { { \beta } } _ { n } ,
$$

all define inner products on $\mathcal { X }$

1.3. Example. Let $( X , \Omega , \mu )$ be a measure space consisting of a set $X ,$ a σ-algebra Ω of subsets of X, and a countably additive measure $\mu$ defined on Ω with values in the non-negative extended real numbers. If $f$ and $g \in L ^ { 2 } ( \mu ) \equiv L ^ { 2 } ( X , \Omega , \mu )$ , then Hölder's inequality implies $f { \bar { g } } { \in } L ^ { 1 } ( \mu )$ If

$$
\langle f , g \rangle = \int f \bar { g } d \mu ,
$$

then this defines an inner product on $L ^ { 2 } ( \mu ) .$

Note that Hölder's inequality also states that $\left| \int f \bar{g} d \mu \right| \leqslant \left[ \int \left| f \right|^2 d \mu \right]^{1/2}$ $\left[ \int | g | ^ { 2 } d \mu \right] ^ { 1 / 2 }$ . This is, in fact, a consequence of the following result on semi-inner products.

1.4. The Cauchy-Bunyakowsky-Schwarz Inequality. $I f \left\langle \cdot , \cdot \right\rangle$ is a semi-inner product on $\mathcal { X } .$ , then

$$
| \langle x , y \rangle | ^ { 2 } \leqslant \langle x , x \rangle \langle y , y \rangle
$$

for all x and y in $\mathcal { X }$ . Moreover, equality occurs if and only if there are scalars $\alpha$ and $\beta ,$ both not $0 ,$ such that $\langle \beta x + \alpha y , \beta x + \alpha y \rangle = 0$

PROOF. If $\alpha \in \mathbf { F }$ and x and $y { \in } { \mathcal { X } }$ , then

$$
\begin{aligned}0 \leqslant & \langle x - \alpha y, x - \alpha y \rangle \\= & \langle x, x \rangle - \alpha \langle y, x \rangle - \bar{\alpha} \langle x, y \rangle + |\alpha|^2 \langle y, y \rangle.\end{aligned}
$$

Suppose $\langle y , x \rangle = b e ^ { i \theta } ,   b \geqslant 0 ,$ and let $\alpha = e ^ { - i \theta } t ,$ t in R. The above inequality becomes

$$
\begin{aligned}0 & \leqslant \langle x, x \rangle - e^{-i \theta} t b e^{i \theta} - e^{i \theta} t b e^{-i \theta} + t^2 \langle y, y \rangle \\& = \langle x, x \rangle - 2 b t + t^2 \langle y, y \rangle \\& = c - 2 b t + a t^2 \equiv q(t),\end{aligned}
$$

where $c = \langle x , x \rangle$ and $a = \langle y , y \rangle$ . Thus $q ( t )$ is a quadratic polynomial in the real variable t and $q ( t ) \geqslant 0$ for all t. This implies that the equation $q ( t )   =   0$ has at most one real solution t. From the quadratic formula we find that the discriminant is not positive; that is, $0 \geqslant 4b^{2} - 4ac$ . Hence

$$
0 \geqslant b^{2}-ac=\left | \left \langle x,y \right \rangle  \right | ^{2}-\left \langle x,x \right \rangle \left \langle y,y \right \rangle ,
$$

proving the inequality.

The proof of the necessary and sufficient condition for equality is left to the reader. ■

The inequality in (1.4) will be referred to as the CBS inequality.

1.5. Corollary. $H \left\langle \cdot , \cdot \right\rangle$ is a semi-inner product on $\mathcal { X }$ and $\| x \| \equiv \langle x , x \rangle ^ { 1 / 2 }$ for all x in $\mathcal { X } ,$ then

(a) $\| x + y \| \leqslant \| x \| + \| y \| { \it ~ f o r ~ } x , y$ in $\mathcal { X } ,$

(b) $\| \alpha x \| = | \alpha | \| x \|$ for α in $\mathbb { F }$ and x in $\mathcal { X }$

$I f \langle \cdot , \cdot \rangle$ is an inner product, then

(c) $\| x \| = 0$ implies $x = 0 ,$

PRooF. The proofs of (b) and (c) are left as an exercise. To see (a), note that for x and $y$ in $\mathcal { X }$

$$
\begin{aligned} \|   x + y   \| ^ {   2 } &= \langle   x + y , x + y   \rangle \\&= \|   x   \| ^ {   2 } + \langle   y , x   \rangle + \langle   x , y   \rangle + \|   y   \| ^ {   2 } \\&= \|   x   \| ^ {   2 } + 2   \mathsf { R e }   \langle   x , y   \rangle + \|   y   \| ^ {   2 } .\\ \end{aligned}
$$

By the CBS inequality, $\mathrm{Re}\langle x,y\rangle\leqslant|\langle x,y\rangle|\leqslant\|x\|\|y\|$ . Hence,

$$
\begin{aligned}\| x + y \|^2 \leqslant & \left\| x \right\|^2 + 2 \left\| x \right\| \left\| y \right\| + \left\| y \right\|^2 \\= & (\left\| x \right\| + \left\| y \right\|)^2.\end{aligned}
$$

The inequality now follows by taking square roots.

$\mathbf { H } \left< \cdot , \cdot \right>$ is a semi-inner product on $\mathcal { X }$ and if $x , y   \in   { \mathcal { X } } ,$ then as was shown in the preceding proof,

$$
\| x + y \| ^ { 2 } = \| x \| ^ { 2 } + 2 \operatorname { R e } \langle x , y \rangle + \| y \| ^ { 2 } .
$$

This identity is often called the polar identity.

The quantity $\|   x   \| = \langle   x , x   \rangle ^ { 1 / 2 }$ for an inner product $\langle \cdot , \cdot \rangle$ is called the norm of x. If $\mathcal { X } = \mathbb { F } ^ { d } ( \mathbb { R } ^ { d } \mathrm { ~ o r ~ } \mathbb { C } ^ { d } )$ and $\langle \{ \alpha _ { n } \} , \{ \beta _ { n } \} \rangle \equiv \sum _ { n = 1 } ^ { d } \alpha _ { n } \bar { \beta } _ { n }$ then the corresponding norm is $\| \{ \alpha _ { n } \} \| = [ \sum _ { n = 1 } ^ { d } | \alpha _ { n } | ^ { 2 } ] ^ { 1 / 2 }$

The virtue of the norm on a vector space $\mathcal { X }$ is that $d ( x , y ) = \| x - y \|$ defines a metric on $\mathcal { X }$ [by (1.5)] so that $\mathcal { X }$ becomes a metric space. In fact, $d ( x , y ) =$ $\|x - y\| = \|(x - z) + (z - y)\| \leqslant \|x - z\| + \|z - y\| = d(x,z) + d(z,y).$ The other properties of a metric follow similarly. If $\mathcal { X } = \mathbb { F } ^ { d }$ and the norm is defined as above, this distance function is the usual Euclidean metric. It is sometimes useful to note that with this metric the inner product becomes a continuous function from $\mathcal { X } \times \mathcal { X }$ into $\mathbb { R }$

1.6. Definition. A Hilbert space is a vector space $\mathcal { H }$ over $\mathbb { F }$ together with an inner product $\langle \cdot , \cdot \rangle$ such that relative to the metric $d(x,y)=\|x-y\|$ induced by the norm, $\mathcal { H }$ is a complete metric space.

If ${ \mathcal { H } } = L ^ { 2 } ( \mu )$ and $\langle f , g \rangle = \int f \bar { g } d \mu ,$ then the associated norm is $\| f \| =$ $\left[ \int | f | ^ { 2 } d \mu \right] ^ { 1 / 2 }$ . It is a standard result of measure theory that $L ^ { 2 } ( \mu )$ is a Hilbert space. It is also easy to see that $\mathbb { F } ^ { d }$ is a Hilbert space.

Remark. The inner products defined on $L ^ { 2 } ( \mu )$ and $\mathbf { F } ^ { d }$ are the “usual” ones Whenever these spaces are discussed these are the inner products referred to. The same is true of the next space.

1.7. Example. Let I be any set and let $l ^ { 2 } ( I )$ denote the set of all functions x: $I   \rightarrow   \mathbf { F }$ such that $x ( i ) = 0$ for all but a countable number of i and $\scriptstyle \sum _ { i \in I } | x ( i ) | ^ { 2 } < \infty$ For x and y in $l ^ { 2 } ( I )$ define

$$
\langle x , y \rangle = \sum _ { i } x ( i ) { \overline { { y ( i ) } } } .
$$

Then $l ^ { 2 } ( I )$ is a Hilbert space (Exercise 2).

If $I = \mathbb { N } , l ^ { 2 } ( I )$ is usually denoted by $l ^ { 2 }$ .Note that if Ω = the set of all subsets of I and for E in $\Omega ,   \mu ( E ) \equiv \infty$ if E is infinite and $\mu ( E ) = \mathrm { t h e }$ cardinality of E if E is finite, then $l ^ { 2 } ( I )$ and $L ^ { 2 } ( I , \Omega , \mu )$ are equal.

Recall that an absolutely continuous function on the unit interval [0, 1] has a derivative a.e. on [0, 1].

1.8. Example. Let $\mathcal { H } =$ the collection of all absolutely continuous functions $f \colon [ 0 , 1 ] \to \mathbb { F }$ such that $f ( 0 ) = 0$ and $f^{\prime} \in L^{2}(0,1)$ . If $\langle f,g\rangle = \int_{0}^{1} f^{\prime}(t)g^{\prime}(t)$ dt for $f$ and $g$ in $\mathcal { H }$ then $\mathcal { H }$ is a Hilbert space (Exercise 3).

Suppose $\mathcal { X }$ is a vector space with an inner product $\langle \cdot , \cdot \rangle$ and the norm is defined by the inner product. What happens if $( \mathcal { X } , d ) ( d ( x , y ) \equiv \| x - y \| )$ is not complete?

1.9. Proposition. If $\mathcal { X }$ is a vector space and $\langle \cdot , \cdot \rangle _ { \mathcal { X } }$ is an inner product on $\mathcal { X }$ and $i f \mathcal { H }$ is the completion of X with respect to the metric induced by the norm on $\mathcal { X }$ , then there is an inner product $\langle \cdot , \cdot \rangle _ { \mathcal { H } }$ on $\mathcal { H }$ such that $\langle x , y \rangle _ { \mathcal { H } } = \langle x , y \rangle _ { \mathcal { X } }$ for x and y in $\mathcal { X }$ and the metric on $\mathcal { H }$ is induced by this inner product. That $i s ,$ the completion of $\mathcal { X }$ is $a$ Hilbert space.

The preceding result says that an incomplete inner product space can be completed to a Hilbert space. It is also true that a Hilbert space over R can be imbedded in a complex Hilbert space (see Exercise 7).

This section closes with an example of a Hilbert space from analytic function theory.

1.10. Definition. If G is an open subset of the complex plane $\mathbf { C } ,$ then $L _ { a } ^ { 2 } ( G )$ denotes the collection of all analytic functions $f \colon G   \to   \mathbb { C }$ such that

$$
\iint _ { G } | f ( x + i y ) | ^ { 2 } d x d y < \infty .
$$

$L _ { a } ^ { 2 } ( G )$ is called the Bergman space for $G ,$

Several alternatives for the integral with respect to two-dimensional Lebesgue measure will be used. In addition to $\iint_{G} \overline{f}(x + iy)   dx   dy$ we will also see

$$
\iint _ { G } f \quad \mathrm { a n d } \quad \int _ { G } f d \mathrm { A r e a } .
$$

Note that $L _ { a } ^ { 2 } ( G ) \subseteq L ^ { 2 } ( \mu )$ , where $\mu = \operatorname { \mathbf { A r e a } } \left[ G \right]$ so that $L _ { a } ^ { 2 } ( G )$ has a natural inner product and norm from $L ^ { 2 } ( \mu )$

1.11. Lemma. $I f f$ is analytic in a neighborhood of $\bar { B } ( a ; r ) ,$ , then

$$
f(a) = \frac{1}{\pi r^{2}} \iint_{B(a;r)} f.
$$

[Here $B ( a ; r ) \equiv \{ z \colon | z - a | < r \}$ and $\bar { B } ( a ; r ) \equiv \{ z \colon | z - a | \leqslant r \} . ]$

ProoF. By the mean value property, if $0 < t \leqslant r,f(a) = (1/2\pi)\int_{-\pi}^{\pi} f(a + te^{i\theta})d\theta.$ Hence

$$
\begin{align*}\left( \pi r^{2} \right)^{-1} \int_{B(a;r)}^{r} f = & \left( \pi r^{2} \right)^{-1} \int_{0}^{r} t \left[ \int_{-\pi}^{\pi} f(a + t e^{i \theta}) d \theta \right] dt \\= & \left( 2 / r^{2} \right) \int_{0}^{r} t f(a) dt = f(a).\end{align*}
$$

1.12. Corollary. $If f \in L_{a}^{2}(G), a \in G$ , and $0 < r < \mathrm{dist}(a, \partial G)$ then

$$
| f ( a ) | \leqslant \frac { 1 } { r \sqrt { \pi } } \| f \| _ { 2 } .
$$

PROOF. Since $\bar { B } ( a ; r ) \subseteq G ,$ , the preceding lemma and the CBS inequality imply

$$
\begin{align*}|f(a)| = & \frac{1}{\pi r^2} \left| \int_{B(a;r)} f \cdot 1 \right| \\\leqslant & \frac{1}{\pi r^2} \left[ \int_{B(a;r)} |f|^2 \right]^{1/2} \left[ \int_{B(a;r)} 1^2 \right]^{1/2} \\\leqslant & \frac{1}{\pi r^2} \parallel f \parallel_2 r \sqrt{\pi}.\end{align*}
$$

1.13. Proposition. $L _ { a } ^ { 2 } ( G )$ is a Hilbert space.

PROOF. If $\mu =$ area measure on $G ,$ then $L ^ { 2 } ( \mu )$ is a Hilbert space and $L _ { a } ^ { 2 } ( G ) \subseteq L ^ { 2 } ( \mu )$ . So it suffices to show that $L _ { a } ^ { 2 } ( G )$ is closed in $L ^ { 2 } ( \mu )$ Let $\{ f _ { n } \}$ be a sequence in $L _ { a } ^ { 2 } ( G )$ and let $f   \in   L ^ { 2 } ( \mu )$ such that $\int | f _ { n } - f | ^ { 2 }   d \mu \to 0$ as $n   \to   \infty$

Suppose $\tilde { B } ( a ; r ) \subseteq G$ and let $0 < \rho < \mathrm { d i s t } ( B ( a ; r ) , \partial G )$ . By the preceding corollary there is a constant C such that $| f _ { n } ( z ) - f _ { m } ( z ) | \leqslant C \| f _ { n } - f _ { m } \| _ { 2 }$ for all $n ,$ m and for $| z - a | \leqslant \rho .$ Thus $\{ f _ { n } \}$ is a uniformly Cauchy sequence on any closed disk in G. By standard results from analytic function theory (Montel's Theorem or Morera's Theorem, for example), there is an analytic function g on G such that $f _ { n } ( z ) \to g ( z )$ uniformly on compact subsets of G. But since $\int | f _ { n } - f | ^ { 2 }   d \mu \to 0 ,$ a result of Riesz implies there is a subsequence $\{ f _ { n _ { k } } \}$ such that $f _ { n _ { k } } ( z ) \to f ( z ) \mathrm { ~ a . e . ~ } [ \mu ]$ . Thus $f = g \mathrm { a . e . } [ \mu ]$ and so $f   \in   \bar { L _ { a } ^ { 2 } ( G ) }$ ■

## EXERCISES

1. Verify the statements made in Example 1.2.

2. Verify that $l ^ { 2 } ( I )$ (Example 1.7) is a Hilbert space.

3. Show that the space $\mathcal { H }$ in Example 1.8 is a Hilbert space.

4. Describe the Hilbert spaces obtained by completing the space $\mathcal { X }$ in Example 1.2 with respect to the norm defined by each of the inner products given there.

## §2. Orthogonality

5. (A variation on Example 1.8) Let $n \geqslant 2$ and let $\mathcal { H } =$ the collection of all function $f \colon [ 0 , 1 ]   \to   \mathbb { F }$ such that (a) $f(0)=0;$ for $1 \leqslant k \leqslant n - 1, f^{(k)}(t)$ exists for all t in [0,1] and $f ^ { ( k ) }$ is continuous on [0, 1]; (c) $f ^ { ( n - 1 ) }$ is absolutely continuous and $f^{(n)} \in L^2(0,1)$ . For f and g in $\mathcal { H } ,$ , define

$$
\langle f , g \rangle = \sum _ { k = 1 } ^ { n } \int _ { 0 } ^ { 1 } f ^ { ( k ) } ( t ) \overline { { g ^ { ( k ) } ( t ) } } d t.
$$

Show that $\mathcal { H }$ is a Hilbert space.

6. Let u be a semi-inner product on $\mathcal { X }$ and put $\mathcal { N } = \{ x { \in } \mathcal { X } : u ( x , x ) = 0 \}$

(a) Show that $\mathcal { N }$ is a linear subspace of $\mathcal { X } .$ T]

(b) Show that if

$$
\langle x + \mathcal { N } , y + \mathcal { N } \rangle \equiv u ( x , y )
$$

for all $x + \mathcal { N }$ and $y + \mathcal { N }$ in the quotient space $\mathcal { X } / \mathcal { N } ,$ then $\langle \cdot , \cdot \rangle$ is a well-defined inner product on $\mathcal { X } / \mathcal { N }$

7. Let $\mathcal { H }$ be a Hilbert space over R and show that there is a Hilbert space $\mathcal { H }$ over C and a map $U \colon { \mathcal { H } } \to { \mathcal { H } }$ such that (a) U is linear; (b) $\langle U h _ { 1 } , U h _ { 2 } \rangle = \langle h _ { 1 } , h _ { 2 } \rangle$ for all $h _ { 1 } , h _ { 2 }$ in $\mathcal { H } ; ( c )$ for any k in $\mathcal { H }$ there are unique $h _ { 1 } , h _ { 2 }$ in $\mathcal { H }$ such that $k = U h _ { 1 } + i U h _ { 2 } \cdot ( \mathcal { H }$ is called the complexification of $\mathcal { H } . )$

8. If $G = \{ z \in \mathbb { C } : 0 < | z | < 1 \}$ show that every f in $L _ { a } ^ { 2 } ( G )$ has a removable singularity at $z = 0$

9. Which functions are in $L _ { a } ^ { 2 } ( \mathbb { C } ) ?$

10. Let G be an open subset of C and show that if $a { \in } G .$ then $\{ f \in L _ { a } ^ { 2 } ( G ) : f ( a ) = 0 \}$ is closed in $L _ { a } ^ { 2 } ( G )$

11. If $\{ h _ { n } \}$ is a sequence in a Hilbert space $\mathcal { H }$ such that $\textstyle \sum _ { n } \| h _ { n } \| < \infty$ , then show that $\sum _ { n = 1 } ^ { \infty } h _ { n }$ converges in $\mathcal { H }$

## §2. Orthogonality

The greatest advantage of a Hilbert space is its underlying concept of orthogonality.

2.1. Definition. If $\mathcal { H }$ is a Hilbert space and f, $g \in \mathcal { H }$ , then f and g are orthogonal $\mathrm { i f } \langle f , g \rangle = 0$ . In symbols, $f \bot g .$ If $A , B \subseteq { \mathcal { H } }$ , then $A \bot B$ if $f \perp g$ for every f in A and g in B.

If $\mathcal { H } = \mathbb { R } ^ { 2 }$ , this is the correct concept. Two non-zero vectors in $\mathbb { R } ^ { 2 }$ are orthogonal precisely when the angle between them is $\pi / 2$

2.2. The Pythagorean Theorem. $I f f _ { 1 } , f _ { 2 } , \ldots , f _ { n }$ are pairwise orthogonal vectors in $\mathcal { H }$ , then

$$
\| f _ { 1 } + f _ { 2 } + \cdots + f _ { n } \| ^ { 2 } = \| f _ { 1 } \| ^ { 2 } + \| f _ { 2 } \| ^ { 2 } + \cdots + \| f _ { n } \| ^ { 2 } .
$$

PROOF. If $f _ { 1 } \bot f _ { 2 }$ , then

$$
\| f _ { 1 } + f _ { 2 } \| ^ { 2 } = \langle f _ { 1 } + f _ { 2 } , f _ { 1 } + f _ { 2 } \rangle = \| f _ { 1 } \| ^ { 2 } + 2 \operatorname { R e } \langle f _ { 1 } , f _ { 2 } \rangle + \| f _ { 2 } \| ^ { 2 }
$$

by the polar identity. Since $f _ { 1 } \bot f _ { 2 } ,$ this implies the result for $n   =   2 .$ The remainder of the proof proceeds by induction and is left to the reader. ■

Note that ${ \mathrm { i f } } f \bot g ,$ thenf $丄  -g,$ so $\| f - g \| ^ { 2 } = \| f \| ^ { 2 } + \| g \| ^ { 2 }$ . The next result is an easy consequence of the Pythagorean Theorem if f and g are orthogonal, but this assumption is not needed for its conclusion.

2.3. Parallelogram Law. If $\mathcal { H }$ is a Hilbert space and f and $g \in \mathcal { H }$ , then

$$
\|   f + g   \| ^ { 2 } + \|   f - g   \| ^ { 2 } = 2 ( \|   f   \| ^ { 2 } + \|   g   \| ^ { 2 } ) .
$$

PROOF. For any f and $g$ in $\mathcal { H }$ the polar identity implies

$$
\begin{array} { r } { \| f + g \| ^ { 2 } = \| f \| ^ { 2 } + 2   \mathrm { R e }   \langle f , g \rangle + \| g \| ^ { 2 } , } \\ { \| f - g \| ^ { 2 } = \| f \| ^ { 2 } - 2   \mathrm { R e }   \langle f , g \rangle + \| g \| ^ { 2 } . } \end{array}
$$

Now add.

The next property of a Hilbert space is truly pivotal. But first we need a geometric concept valid for any vector space over $\mathbf { E }$

2.4. Definition. If ¿ is any vector space over F and $A \subseteq { \mathcal { X } }$ , then A is a convex set if for any x and y in A and $0 \leqslant t \leqslant 1,   tx + (1 - t)y \in A$

Note that $\left\{ t x + ( 1 - t ) y : 0 \leqslant t \leqslant 1 \right\}$ is the straight-line segment joining x and y. So a convex set is a set A such that if x and $y \in A$ , the entire line segment joining x and y is contained in A.

If X is a vector space, then any linear subspace in $\mathcal { X }$ is a convex set. A singleton set is convex. The intersection of any collection of convex sets is convex. If $\mathcal { H }$ is a Hilbert space, then every open ball $B(f;r)=\{g\in\mathcal{H}\}$二 $\left\| f - g \right\| < r \big \}$ is convex, as is every closed ball.

2.5. Theorem. If H is a Hilbert space, K is a closed convex nonempty subset of $\mathcal { H }$ , and $h \in \mathcal { H }$ , then there is a unique point $k _ { 0 }$ in K such that

$$
\| \boldsymbol{h} - \boldsymbol{k}_0 \| = \mathrm{dist}(\boldsymbol{h}, \boldsymbol{K}) \equiv \inf \{ \| \boldsymbol{h} - \boldsymbol{k} \| : \boldsymbol{k} \in \boldsymbol{K} \}.
$$

PROOF. By considering $K - h \equiv \{ k - h { \mathrm { : ~ } } k { \in } K \}$ instead of K, it suffices to assume that $h = 0.   (  Verify ! )$ So we want to show that there is a unique vector $k _ { 0 }$ in K such that

$$
\| \boldsymbol { k } _ { 0 } \| = \mathrm { d i s t } ( 0 , \boldsymbol { K } ) \equiv \inf \{ \| \boldsymbol { k } \| : \boldsymbol { k } \in \boldsymbol { K } \}.
$$

Let $d = \mathrm{dist}(0, K)$ . By definition, there is a sequence $\{ k _ { n } \}$ in K such that一 $k _ { n } \rVert \to d .$ Now the Parallelogram Law implies that

$$
\left\| \frac{k_n - k_m}{2} \right\|^2 = \frac{1}{2} \left( \left\| k_n \right\|^2 + \left\| k_m \right\|^2 \right) - \left\| \frac{k_n + k_m}{2} \right\|^2.
$$

## §2. Orthogonality

Since K is convex, $\scriptstyle { \frac { 1 } { 2 } } ( k _ { n } + k _ { m } ) \in K$ . Hence, $\| \frac { 1 } { 2 } ( k _ { n } + k _ { m } ) \| ^ { 2 } \geqslant d ^ { 2 }$ . If $\varepsilon   >   0 ,$ choose N such that for $n \geqslant N, \left\| \hat{k}_n \right\|^2 < d^2 + \frac{1}{4} \varepsilon^2$ . By the equation above, $\mathrm{if} n, m \geqslant N$ , then

$$
\left\| \frac{k_n - k_m}{2} \right\|^2 < \frac{1}{2} \left( 2d^2 + \frac{1}{2} \varepsilon^2 \right) - d^2 = \frac{1}{4} \varepsilon^2.
$$

Thus, $\| k _ { n } - k _ { m } \| < \varepsilon$ for $n , m \geqslant N$ and $\left\{ k _ { n } \right\}$ is a Cauchy sequence. Since $\mathcal { H }$ is complete and K is closed, there is a $k _ { 0 }$ in K such that $\| k _ { n } - k _ { 0 } \|   \to   0$ Also for all $k _ { n } ,$

$$
\begin{aligned}d \leqslant \left\| \boldsymbol{k}_{0} \right\| &= \left\| \boldsymbol{k}_{0} - \boldsymbol{k}_{n} + \boldsymbol{k}_{n} \right\| \\& \leqslant \left\| \boldsymbol{k}_{0} - \boldsymbol{k}_{n} \right\| + \left\| \boldsymbol{k}_{n} \right\| \rightarrow \boldsymbol{d}.\end{aligned}
$$

Thus $\| k _ { 0 } \| = d .$

To prove that $k _ { 0 }$ is unique, suppose $h _ { 0 }   \in   K$ such that $\| \boldsymbol { h } _ { 0 } \| = d$ By convexity, $\scriptstyle { \frac { 1 } { 2 } } ( k _ { 0 } + h _ { 0 } ) \in K$ . Hence

$$
d \leqslant \| \frac{1}{2} (h_0 + k_0) \| \leqslant \frac{1}{2} (\| h_0 \| + \| k_0 \|) = d.
$$

So $\begin{array} { r } { \| \frac { 1 } { 2 } ( h _ { 0 } + k _ { 0 } ) \| = d . } \end{array}$ The Parallelogram Law implies

$$
d ^ { 2 } = \left\| \frac { h _ { 0 } + k _ { 0 } } { 2 } \right\| ^ { 2 } = d ^ { 2 } - \left\| \frac { h _ { 0 } - k _ { 0 } } { 2 } \right\| ^ { 2 } ;
$$

hence $h _ { 0 } = k _ { 0 }$

If the convex set in the preceding theorem is in fact a closed linear subspace of $\mathcal { H }$ , more can be said.

2.6. Theorem. If M is a closed linear subspace of $\mathcal { H } , h \in \mathcal { H }$ , and $f _ { 0 }$ is the unique element of M such that $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } )$ , then $\pmb { h } - f _ { 0 } \bot \mathcal { M }$ . Conversely, if $f _ { 0 } \in \mathcal { M }$ such that $\pmb { h } - f _ { 0 } \bot \mathcal { M } ,$ then $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } )$

PROOF. Suppose $f _ { 0 } \in \mathcal { M }$ and $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } ) .$ If $f \in \mathcal { M } _ { 1 }$ then $f _ { 0 } + f \in \mathcal { M }$ and so $\| h - f_0 \|^2 \leqslant \| h - (f_0 + f) \|^2 = \| (h - f_0) - f \|^2 = \| h - f_0 \|^2$ $- 2 \operatorname { R e } \left\langle h - f _ { 0 } , f \right\rangle + \| f \| ^ { 2 }$ . Thus

$$
2 \operatorname{Re} \left\langle h - f_0, f \right\rangle \leqslant \| f \|^2
$$

for any f in M. Fix f in M and substitute $t e ^ { i \theta } f$ for f in the preceding inequality, where $\langle h - f _ { 0 } , f \rangle = r e ^ { i \theta } , r \geqslant 0$ .This yields $2 \mathrm{Re} \left\{ t e^{-i \theta} r e^{i \theta} \right\} \leqslant t^2 \| f \|^2$ , or $2 t r \leqslant t ^ { 2 } \left\| f \right\| { } ^ { 2 }$ Letting $t   \rightarrow   0 ,$ we see that $r = 0 ;$ that is, $\pmb { h } - f _ { 0 } \bot f .$

For the converse, suppose $f _ { 0 } \in \mathcal { M }$ such that $\pmb { h } - f _ { 0 } \bot \mathcal { M }$ . If $f \in \mathcal { M }$ , then $h - f _ { 0 } \bot f _ { 0 } - f$ so that

$$
\begin{aligned} \|   h - f   \| ^ { 2 } & = \|   ( h - f _ { 0 } ) + ( f _ { 0 } - f )   \| ^ { 2 } \\ & = \|   h - f _ { 0 }   \| ^ { 2 } + \|   f _ { 0 } - f   \| ^ { 2 } \\ & \geqslant \|   h - f _ { 0 }   \| ^ { 2 } . \end{aligned}
$$

Thus $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } )$