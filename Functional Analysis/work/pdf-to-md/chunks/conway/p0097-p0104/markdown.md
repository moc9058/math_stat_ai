10. Let $P = \{ p | \partial \mathbb { D } : p = \mathrm { a n }$ analytic polynomial} and consider P as a manifold in $C ( \partial \mathbf { D } )$ .Show that if μ is a real-valued measure on ∂D such that $\int   p   d \mu = 0$ for every p in $P ,$ then $\mu   =   0$ Give an example of a complex-valued measure $\mu$ such that $\mu \neq 0$ $\int p   d \mu = 0$ for every $p$ in $P .$

## $\S 7 ^ { * }$ . An Application: Banach Limits

If $x = \{ x ( n ) \} \in c ,$ define $L(x) = \lim_{} x(n)$ . Then L is a linear functional, $\| L \| = 1$ and, if for x in $c ,   x ^ { \prime }$ is defined by $x ^ { \prime } = ( x ( 2 ) , x ( 3 ) , \ldots ) ,$ then $L ( x ) = L ( x ^ { \prime } )$ . Also, if $x \geqslant 0$ [that is, $x ( n ) \geqslant 0$ for all n], then $L ( x ) \geqslant 0 .$ In this section it will be shown that these properties of the limit functional can be extended to $l ^ { \infty }$ The proof uses the Hahn-Banach Theorem.

## 7.1. Theorem. There is a linear functional L: $l ^ { \infty }   \rightarrow   \mathbf { F }$ such that

(a) $\| L \| = 1$

(b) $If x \in c,   L(x) = \lim_{n \to \infty} x(n).$

(c) $\scriptstyle { \boldsymbol { I } } { \boldsymbol { f } } \; x \in { \boldsymbol { l } } ^ { \infty }$ and $x ( n ) \geqslant 0$ for all n, then $L ( x ) \geqslant 0 .$

(d) If $x { \in } l ^ { \infty }$ and $x ^ { \prime }   \equiv   ( x ( 2 ) , x ( 3 ) , \ldots ) ,$ then $L ( x ) = L ( x ^ { \prime } ) .$

PrOOF. First assume $\mathbf { F }   =   \mathbf { R } ;$ that is, $l ^ { \infty } = l _ { \mathbb { R } } ^ { \infty } . \operatorname { \bf I f } x { \in } l ^ { \infty }$ , let $x ^ { \prime }$ denote the element of $l ^ { \infty }$ defined in part (d) above. Put $\mathcal { M } = \left\{ x - x ^ { \prime } ; x { \in } l ^ { \infty } \right\}$ . Note that $(x + \alpha y)' =$ $x ^ { \prime } + \alpha y ^ { \prime }$ for any $x , y$ in $l ^ { \infty }$ and αin $\mathbb { R } ;$ hence $\mathcal { M }$ is a linear manifold in $l ^ { \infty }$ Let 1 denote the sequence $( 1 , 1 , 1 , \ldots )$ in $l ^ { \infty }$

## 7.2. Claim. dist $( 1 , \mathcal { M } ) = 1$

Since $0 \in \mathcal { M } ,$ dist $( 1 , \mathcal { M } ) \leqslant 1$ . Let $x { \in } l ^ { \infty } ,$ if $(x - x^{\prime})(n) \leqslant 0$ for any n, then $\| 1 - (x - x') \|_{\infty} \geqslant |1 - (x(n) - x'(n))| \geqslant 1.$ ppose $0 \leqslant (x - x^{\prime})(n) = x(n) - x^{\prime}(n) =$ $x ( n ) - x ( n + 1 )$ for all n. Thus $x(n + 1) \leq x(n)$ for all n. Since x∈l∞, α = lim x(n) exists. Thus lim $( x - x ^ { \prime } ) ( n ) = 0$ and $\| 1 - ( x - x ^ { \prime } ) \| _ { \infty } \geqslant 1$ . This proves the claim.

By Corollary 6.8 there is a linear functional $L \colon l ^ { \infty }   \to   \mathbb { R }$ such that $\| L \| = 1$ $L ( 1 )   =   1$ , and $L ( \mathcal { M } ) = 0 .$ So this functional satisfies (a) and (d) of the theorem. To prove (b), we establish the following.

## 7.3. Claim. $c _ { 0 } \subseteq \ker L$

If $x { \in } c _ { 0 } ,$ let $x ^ { ( 1 ) } = x ^ { \prime }$ and let $x^{(n+1)} = (x^{(n)})'$ for $n \geqslant 1$ . Note that $x^{(n+1)} - x = \left[ x^{(n+1)} - x^{(n)} \right] + \cdots + \left[ x^{\prime} - x \right] \in \mathcal{M}$ Hence $L ( x ) = L ( x ^ { ( n ) } )$ for all $n \geqslant 1$ . If $\varepsilon   >   0 ,$ then let n be such that $| x ( m ) | < \varepsilon$ for $m > n$ Hence $| L ( x ) | = | L ( x ^ { ( n ) } ) | \leqslant \| x ^ { ( n ) } \| _ { \infty } = \sup \{ | x ( m ) | : m > n \} < \varepsilon$ Thus x∈ker L. Condition (b) is now clear.

To show (c), suppose there is an x in $l ^ { \infty }$ such that $x ( n ) \geqslant 0$ for all n and $L ( x )   <   0$ If x is replaced by $x / \| x \| _ { \infty } ,$ it remains true that $L ( x )   <   0$ and it is also true that $1 \geqslant x ( n ) \geqslant 0$ for all n. But then $\|   1 - x   \| _ { \infty } \leqslant 1$ and $L ( 1 - x ) =$ $1 - L ( x ) > 1$ , contradicting (a). Thus (c) holds.

Now assume that $\mathbf { F } = \mathbf { C }$ Let $L _ { 1 }$ be the functional obtained on $l _ { \mathbb { R } } ^ { \infty } . \mathrm { ~ I f ~ } x { \in } l _ { \mathbb { C } } ^ { \infty } .$ then $x = x _ { 1 } + i x _ { 2 }$ where $x _ { 1 } , x _ { 2 } { \in } l _ { \mathbb { R } } ^ { \infty }$ Define $L ( x ) = L _ { 1 } ( x _ { 1 } ) + i L _ { 1 } ( x _ { 2 } )$ . It is left as an exercise to show that L is C-linear. It's clear that (b), (c), and (d) hold. It remains to show that $\| L \| = 1$

Let $E _ { 1 } , \ldots , E _ { m }$ be pairwise disjoint subsets of N and let $\alpha _ { 1 } , \ldots , \alpha _ { m } { \in } { \pmb { \mathbb { C } } }$ with $| \alpha _ { k } | \leqslant 1$ for all k. Put $x = \sum_{k = 1}^{m} \alpha_{k} \chi_{E_{k}};$ sO $x { \in } l ^ { \infty }$ and $\| x \| _ { \infty } \leqslant 1$ Then $L(x) = \sum_{k} \alpha_{k} L(\chi_{E_{k}}) = \sum_{k} \alpha_{k} L_{1}(\chi_{E_{k}})$ But $L _ { 1 } ( \chi _ { E _ { k } } ) \geqslant 0$ and $\begin{array} { r } { \sum _ { k } L _ { 1 } ( \chi _ { E _ { k } } ) = L _ { 1 } ( \chi _ { E } ) , } \end{array}$ where $E = { \bigcup } _ { k } E _ { k }$ . Hence $\begin{array} { r } { \sum _ { k } L _ { 1 } ( \chi _ { E _ { k } } ) \leqslant 1 } \end{array}$ . Because $| \alpha _ { k } | \leqslant 1$ for all k, $| L ( x ) | \leqslant 1$ If x is an arbitrary element of $l ^ { \infty } ,   \|   x   \| _ { \infty } \leqslant 1$ , then there is a sequence $\{ x _ { n } \}$ of elements of $l ^ { \infty }$ such that $\| x_n - x \|_{\infty} \to 0, \| x_n \|_{\infty} \leqslant 1$ , and each $x _ { n }$ is the type of element of $l ^ { \infty }$ just discussed that takes on only a finite number of values (Exercise 3). Clearly, $\| L \| \leqslant 2 .$ sO $L ( x _ { n } ) \to L ( x )$ . Since $| L ( x _ { n } ) | \leqslant 1$ for all $n ,$ $| L ( x ) | \leqslant 1$ . Hence $\| L \| \leqslant 1$ . Since $L ( 1 ) = 1 ,   \| L \| = 1$ ■

A linear functional of the type described in Theorem 7.1 is called a Banach limit. They are useful for a variety of things, among which is the construction of representations of the algebra of bounded operators on a Hilbert space.

## EXERCISES

1. If Lis a Banach limit, show that there are x and y in $l ^ { \infty }$ such that $L(xy) \neq L(x)L(y)$

2. Let X be a set and Ω a σ-algebra of subsets of X. Suppose $\mu$ is a complex-valued countably additive measure defined on Ω such that $\|   \mu   \| = \mu ( X ) < \infty$ . Show that $\mu ( \Delta ) \geqslant 0$ for every ∆ in Ω. (Though it is difficult to see at this moment, this fact is related to the proof of (c) in Theorem 7.1 for the complex case.)

3. Show that if $x { \in } l ^ { \infty } , \; \left\|   x   \right\| _ { \infty } \leqslant 1$ , then there is a sequence $\{ x _ { n } \} ,   x _ { n }$ in $l ^ { \infty }$ such that $x _ { n } \parallel _ { \infty } \leqslant 1 , \| x _ { n } - x \| _ { \infty } \to 0 ,$ and each $x _ { n }$ takes on only a finite number of values.

## §8\*. An Application: Runge's Theorem

The symbol $\mathbf { C } _ { \infty }$ denotes the extended complex plane.

8.1. Runge's Theorem. Let K be a compact subset of C and let E be a subset $of \mathbf { \bar { C } } _ { \propto } \backslash K$ that meets each component of $\mathbf { ^ { \circ } \mathbb { C } } _ { \infty } \backslash K$ If f is analytic in a neighborhood of K, then there are rational functions $f _ { n }$ whose only poles lie in E such that $f _ { n }   \rightarrow   f$ uniformly on K.

The main tool in proving Runge's Theorem is Theorem 6.13. (A proof that does not use functional analysis can be found on p. 189 of Conway [1978].) To do this, let $R ( K , E )$ be the closure in the space C(K) of the rational functions with poles in E. By (6.13) and the Riesz Representation Theorem, it suffices to show that if $\mu { \in } M ( K )$ and $\int   g   d \mu = 0$ for each $g$ in $R ( K , E )$ , then $\int f d \mu = 0 .$

Let $R   >   0$ and let λ be area measure. Pick $\rho   >   0$ such that $B ( 0 ; R ) \subseteq B ( z ; \rho )$ for every z in K. Then for z in K,

$$
\begin{align*}\int_{B(0;R)} \left| z - w \right|^{-1}   d\lambda(w) & \leqslant \int_{B(z;\rho)} \left| z - w \right|^{-1}   d\lambda(w) \\& = \int_{0}^{2\pi} \int_{0}^{\rho} dr   d\theta = 2\pi\rho.\end{align*}
$$

If $\mu { \in } M ( K ) ,$ define $\tilde { \mu } \colon \mathbb { C }   \to   [ 0 , \infty ]$ by

$$
\tilde { \mu } ( w ) = \int \frac { d | \mu | ( z ) } { | z - w | }
$$

when the integral is finite, and $\tilde { \mu } ( w ) = \infty$ otherwise. The inequality above implies

$$
\begin{align*}\int_{B(0;R)} \tilde{\mu}(w)d\lambda(w) &= \int_{B(0;R)} \int_{K} \frac{d|\mu|(z)}{|z-w|}d\lambda(w) \\&= \int_{K} \int_{B(0;R)} \frac{d\lambda(w)}{|z-w|}d|\mu|(z) \\&\leqslant 2\pi\rho\left\| \mu \right\|.\end{align*}
$$

Thus $\tilde { \mu } ( w ) < \infty$ a.e. [λ].

8.2. Lemma. If $\mu { \in } M ( K ) .$ , then

$$
\hat { \mu } ( w ) = \int \frac { d \mu ( z ) } { z - w }
$$

is in $L ^ { 1 } ( B ( 0 ; R ) , \lambda )$ for any $R > 0 ,   \hat { \mu }$ is analytic on $\mathbf { C } _ { \infty } \backslash K$ , and $\hat { \mu } ( \infty )   =   0$

ProoF. The first statement follows from what came before the statement of this lemma. To show that $\hat { \mu }$ is analytic on $\mathbf { C } _ { \infty } \backslash K$ , let w, $w _ { 0 } { \in } { \mathbb { C } } \backslash K$ and note that

$$
\frac { \hat { \mu } ( w ) - \hat { \mu } ( w _ { 0 } ) } { w - w _ { 0 } } = \int _ { K } \frac { d \mu ( z ) } { ( z - w ) ( z - w _ { 0 } ) } .
$$

As $w \to w _ { 0 } ,   \left[ ( z - w ) ( z - w _ { 0 } ) \right] ^ { - 1 } \to ( z - w _ { 0 } ) ^ { - 2 }$ uniformly for z in $K ,$ so that $\hat { \mu }$ has a derivative at $w _ { 0 }$ and

$$
\frac { d \hat { \mu } } { d w } ( w _ { 0 } ) = \int _ { K } ( z - w _ { 0 } ) ^ { - 2 } d \mu ( z ) .
$$

So $\hat { \mu }$ is analytic on $\mathbf { C } \backslash K .$ To show that it is analytic at infinity, note that $\hat { \mu } ( z )   \rightarrow   0$ as $z \rightarrow \infty$ , so infinity is a removable singularity.

It is not difficult to see that for $w _ { 0 }$ in $\mathbf { C } \backslash K$

$$
\left( \frac{d}{dw} \right)^n \hat{\mu}(w_0) = n! \int (z - w_0)^{-n-1} d\mu(z).
$$

Also, we can easily find the power series expansion of $\hat { \mu }$ at infinity. Indeed,

$$
\hat { \mu } ( w ) = \int \frac { 1 } { z - w } d \mu ( z ) = - \frac { 1 } { w } \int \left( 1 - \frac { z } { w } \right) ^ { - 1 } d \mu ( z ) .
$$

Choose w near enough to infinity that $| z / w | < 1$ for all $z$ in K. Then

## 8.4

$$
\begin{align*}\hat{\mu}(w) = & - \frac{1}{w} \sum_{n = 0}^{\infty} \int \left( \frac{z}{w} \right)^n d\mu(z) \\= & - \sum_{n = 0}^{\infty} \frac{a_n}{w^{n + 1}},\end{align*}
$$

where $a _ { n } = \int z ^ { n } d \mu ( z ) .$

Now assume $\mu { \in } M ( K )$ and $\int   g   d \mu = 0$ for every rational function $g$ with poles in E. Let U be a component of $\mathbf { C } _ { \infty } \backslash K ,$ and let $w _ { 0 } { \in } E \cap U$ . If $w _ { 0 } \neq \infty$ then the hypothesis and (8.3) imply that each derivative of $\hat { \mu }$ at $w _ { 0 }$ vanishes. Hence $\hat { \mu } \equiv 0$ on U. If $w _ { 0 } = \infty$ , then (8.4) implies $\hat { \mu } \equiv 0$ on U. Thus $\hat { \mu } \equiv 0$ on $\mathbb { C } _ { \infty } \backslash K$

If f is analytic on an open set G containing K, let $\gamma _ { 1 } , \ldots , \gamma _ { n }$ be straight-line segments in $G \backslash K$ such that

$$
f(z) = \sum_{k = 1}^{n} \frac{1}{2\pi i} \int_{\gamma_{k}} \frac{f(w)}{w - z} dw
$$

for all $z$ in K. (See p. 195 of Conway [1978].) Thus

$$
\begin{align*}\int_{K} f(z) d\mu(z) &= \sum_{k=1}^{n} \frac{1}{2\pi i} \int_{K} \int_{\gamma_k} \frac{f(w)}{w-z} dw d\mu(z) \\&= - \sum_{k=1}^{n} \frac{1}{2\pi i} \int_{\gamma_k} f(w) \hat{\mu}(w) dw\end{align*}
$$

by Fubini's Theorem. But $\hat { \mu } ( w ) = 0$ on $\gamma _ { k } ~ ( \in \pmb { \mathbb { C } } \backslash K )$ so $\int f   d \mu = 0$ By (6.13), $f   \in   R ( K , E )$ . This proves Runge's Theorem.

8.5. Corollary. If K is compact and $\mathbf { C } \backslash K$ is connected and if f is analytic in a neighborhood of K, then there is a sequence of polynomials that converges to f uniformly on K.

## EXERCISES

1. Let $\mu$ be a compactly supported measure on C that is boundedly absolutely continuous with respect to area measure. Show that $\hat { \mu }$ is continuous on $\mathbf { C } _ { \infty } ,$

2. Let m = Lebesgue measure on [0, 1]. Show that m is not continuous at any point of [0, 1].

## $\S 9 ^ { * }$ . An Application: Ordered Vector Spaces

In this section only vector spaces over R are considered.

There are numerous spaces in which there is a notion of $\leqslant$ in addition to the vector space structure. The LP spaces and $C ( X )$ are some that spring to mind. The concept of an ordered vector space is an attempt to study such spaces in an abstract setting. The first step is to abstract the notion of the positive elements.

9.1. Definition. An ordered vector space is a pair $( \mathcal { X } , \leqslant )$ where $\mathcal { X }$ is a vector space over IR and $\leqslant$ is a relation on $\mathcal { X }$ satisfying

(a) $x \leqslant x$ for all x;

(b) if $x \leqslant y$ and $y \leqslant z ,$ then $x \leqslant z ;$

(c) if $x \leqslant y$ and $z \in \mathcal { X }$ then $x + z \leqslant y + z;$

(d) if $x \leqslant y$ and $\alpha { \in } [ 0 , \infty )$ , then $\alpha x \leqslant \alpha y .$

Note that it is not assumed that $\leqslant$ is antisymmetric. That is, it is not assumed that if $x \leqslant y$ and $y \leqslant x ,$ then $x = y .$

9.2. Definition. If X is a real vector space, a wedge is a nonempty subset P of $\mathcal { X }$ such that

(a) if $x , y { \in } P ,$ then $x + y { \in } P ;$

(b) if $x { \in } P$ and $\alpha \in [ 0 , \infty ) .$ , then ${ \pmb { \alpha } } { \pmb { x } } { \in } { \pmb { P } } ,$

9.3. Proposition. (a) $\mathit { I f } ( \mathcal { X } , \leqslant )$ is an ordered vector space and $P = \{ x \in \mathcal { X } : x \geqslant 0 \}$ then P is a wedge. (b) If P is a wedge in the real vector space $\mathcal { X }$ and $\leqslant$ is defined on $\mathcal { X }$ by declaring $x \leqslant y$ if and only if $y - x { \in } P ,$ then $( \mathcal { X } , \leqslant )$ is an ordered vector space.

PROOF. Exercise.

If $( \mathcal { X } , \leqslant )$ is an ordered vector space, $P = \{ x \in \mathcal { X } : x \geqslant 0 \}$ is called the wedge of positive elements. The next result is also left as an exercise.

9.4. Proposition. $\mathit { I f } \left( \mathcal { X } , \leqslant \right)$ is an ordered vector space and P is the wedge of positive elements, $\leqslant$ is antisymmetric if and only if $P \cap ( - P ) = ( 0 )$

9.5. Definition. A cone in $\mathcal { X }$ is a wedge P such that $P \cap ( - P ) = ( 0 )$

9.6. Definition. If $[ \mathcal { X } , \leqslant )$ is an ordered vector space, a subset A of $\mathcal { X }$ is cofinal if for every $x \geqslant 0$ in X there is an a in A such that $a \geqslant x$ An element e of $\mathcal { X }$ is an order unit if for every x in $\mathcal { X }$ there is a positive integer n such that $- n e \leqslant x \leqslant n e.$

If X is a compact space ${ \mathcal { X } } = C ( X ) ,$ , then any non-zero constant function is an order unit. $( f \leqslant g$ if and only if $f(x) \leqslant g(x)$ for all $x . )$ If ${ \mathcal { X } } = C ( \mathbb { R } )$ , all real-valued continuous functions on R, then $\mathcal { X }$ has no order unit (Exercise 4). If e is an order unit, then $\{ n e \colon n \geqslant 1 \}$ is cofinal.

9.7. Definition. If $( \mathcal { X } , \leqslant )$ and $( \mathcal { Y } , \leqslant )$ are ordered vector spaces and $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear map, then Tis positive (in symbols $T \geqslant 0 )$ if $T x \geqslant 0$ whenever $x   \geqslant   0$

The principal result of this section is the following.

9.8. Theorem. Let $( \mathcal { X } , \leqslant )$ be an ordered vector space and let $\pmb { y }$ be a linear manifold in $\mathcal { X }$ that is confinal. $I f f \colon { \mathcal { B } }   \to   \mathbb { R }$ is a positive linear functional, then there is a positive linear functional $\tilde { f } \colon \mathcal { X }   \to   \mathbb { R }$ such that $\tilde { f } | \mathcal { Y } = f .$

PROOF. Let $P = \{ x \in \mathcal { X } : x \geqslant 0 \}$ and put $\mathcal { X } _ { 1 } = \mathcal { Y } + P - P$ It is easy to see that $\mathcal { X } _ { 1 }$ is a linear manifold in ¿. If there is a positive linear functional $g \colon \mathcal { X } _ { 1 }   \to   \mathbb { R }$ that extends $f ,$ let $\widetilde { f }$ be any linear functional on $\mathcal { X }$ that extends g (use a Hamel basis). $\operatorname { I f } x \geqslant 0 .$ then $x { \in } P \subseteq { \mathcal { X } } _ { 1 }$ so that $\tilde { f } ( x ) = g ( x ) \geqslant 0$ Hence $\widetilde { f }$ is positive. Thus, we may assume that $\mathcal { X } = \mathcal { Y } + P - P .$

## 9.9. Claim. $\mathcal { X } = \mathcal { Y } + P = \mathcal { Y } - P .$

Let $x { \in } { \mathcal { X } } ;$ sO $x = y + p _ { 1 } - p _ { 2 } ,   y$ in $\mathcal { G } ,   p _ { 1 } ,   p _ { 2 }$ in P. Since $\mathcal { Y }$ is confinal there is a $y _ { 1 }$ in @ such that $y _ { 1 } \geqslant p _ { 1 }$ . Hence $p_{1}=y_{1}-(y_{1}-p_{1})\in \mathcal{Y}-P$ Thus $x = y - p_{2} + p_{1} \in (\mathcal{A} - P) + (\mathcal{A} - P) \subseteq \mathcal{A} - P. \mathrm{So} \mathcal{X} = \mathcal{A} - P. \mathrm{Also}, \mathcal{X} = - \mathcal{X} =$ $- { \mathcal { Y } } + P = { \mathcal { Y } } + P .$

9.10. Claim. If $x { \in } { \mathcal { X } }$ , there are $y _ { 1 } , y _ { 2 }$ in $\theta$ such that $y _ { 2 } \leqslant x \leqslant y _ { 1 }$

In fact, Claim 9.9 states that we can write $x = y _ { 1 } - p _ { 1 } = y _ { 2 } + p _ { 2 } ,   p _ { 1 } ,   p _ { 2 } \in P$ and $y _ { 1 } ,   y _ { 2 } { \in } { \mathcal { Y } }$ . Thus $y _ { 2 } \leqslant x \leqslant y _ { 1 }$

By Claim 9.10, it is possible to define for each x in $\mathcal { X }$

$$
q ( x ) = \operatorname* { i n f } \left\{ f ( y ) : y \in { \mathcal { Y } } { \mathrm { ~ a n d ~ } } y \geq x \right\} .
$$

9.11. Claim. The function q is a sublinear functional on $\mathcal { X } .$

The proof of (9.11) is left as an exercise.

For y in $\mathcal { Y } ,$ let $y _ { 1 }   \in   \mathcal { Y }$ such that $y _ { 1 } \geqslant y _ { 1 }$ Because f is positive, $f ( y )   \leqslant   f ( y _ { 1 } )$ Hence $f ( y ) \leqslant q ( y )$ for all y in $參 .$ The Hahn-Banach Theorem implies that there is a linear functional $\tilde { f } \colon \mathcal { X }   \to   \mathbb { R }$ such that $\tilde { f } | \mathcal { G } = f$ and $\tilde { f } \leqslant q ^ { \prime }$ on $\mathcal { X }$ If $x { \in } P ,$ then $- x \leqslant 0$ (and $0 \in \mathcal { Y }$ Hence $q(-x) \leqslant f(0)$ . Thus $- { \tilde { f } } ( x ) =$ $\tilde { f } ( - x ) \leqslant q ( - x ) \leqslant 0 ,$ or $\left[ \widetilde { f } ( x ) \geqslant 0 \right.$ Therefore $\tilde { f }$ is positive. ■

9.12. Corollary. Let $( \mathcal { X } , \leqslant )$ be an ordered vector space with an order unit e. If Y is a linear manifold in $\mathcal { X }$ and $e \in \mathcal { Y }$ , then any positive linear functional defined on  has an extension to a positive linear functional defined on $\mathcal { X }$

EXERCISES

1. Prove Proposition 9.3.

2. Prove Proposition 9.4.

3. Show that e is an order unit for $( \mathcal { X } , \leqslant )$ if and only if for every x in $\mathcal { X }$ there is a $\delta   >   0$ such that $e \pm t x \geqslant 0$ for $0 \leqslant t \leqslant \delta.$

4. Show that $C ( \mathbb { R } ) ,$ , the space of all continuous real-valued functions on $\mathbf { R } ,$ has no order unit.

5. Prove (9.11).

6. Characterize the order units of $C _ { b } ( X )$ . Does $C _ { b } ( X )$ always have an order unit?

7. Characterize the order units of $C _ { 0 } ( X )$ if X is locally compact. Does $C _ { 0 } ( X )$ always have an order unit?

8. Let $\mathcal { X } = M _ { 2 } ( \mathbb { R } ) .$ the $2 \times 2$ matrices over R. Define A in $M _ { 2 } ( \mathbb { R } )$ to be positive if $A = A ^ { * }$ and $\langle A x , x \rangle \geqslant 0$ for all x in $\mathbb { R } ^ { 2 }$ Characterize the order units of $M _ { 2 } ( \mathbb { R } )$

9. If $1 \leqslant p < \infty$ and $\mathcal { X } = L ^ { p } ( 0 , 1 )$ , define $f \leqslant g$ to mean that $f(x) \leqslant g(x)$ a.e. Show that $\mathcal { X }$ is an ordered vector space that has no order unit.

## §10. The Dual of a Quotient Space and a Subspace

Let $\mathcal { X }$ be a normed space and $\mathcal { M } \leqslant \mathcal { X }$ . If $f \in \mathcal { X } ^ { * }$ , then $f \vert \mathcal { M }$ , the restriction of $f ( 0 )$ belongs to $\mathcal { M } ^ { * }$ and $\| f | \mathcal { M } \| \leqslant \| f \|$ . According to the Hahn-Banach Theorem, every bounded linear functional on $\mathcal { M }$ is obtainable as the restriction of a functional from $\mathcal { X } ^ { * }$ . In fact, more can be said.

Note that if $\mathcal { M } ^ { \perp } \equiv \{ g \in \mathcal { X } ^ { * } ; g ( \mathcal { M } ) = 0 \}$ (note the analogy with Hilbert space notation); then $\mathcal { M } ^ { \perp }$ is a closed subspace of the Banach space $\mathcal { X } ^ { * }$ . Hence $x ^ { * } / d ^ { 1 }$ is a Banach space. Moreover, if $f + \mathcal { M } ^ { \perp } { \in } \mathcal { X } ^ { * } / \mathcal { M } ^ { \perp }$ , then $f + M ^ { \perp }$ induces a linear functional on $\mathcal { M } ,$ namely $f \vert \mathcal { M }$

10.1. Theorem. If $\mathcal { M } \leqslant \mathcal { X }$ and $\mathcal { M } ^ { \perp } \equiv \{ g   \in   \mathcal { X } ^ { * } \colon   g ( \mathcal { M } )   =   0 \}$ , then the map $\rho ;$ $\mathcal { X } ^ { * } / \mathcal { M } ^ { \perp }   \rightarrow   \mathcal { M } ^ { * }$ defined by

$$
\rho ( f + \mathcal { M } ^ { \perp } ) = f | \mathcal { M }
$$

is an isometric isomorphism.

PRoOF. It is easy to see that $\rho$ is linear and injective. If $f \in \mathcal { X } ^ { * }$ and $g \in \mathcal { M } ^ { \perp }$ then $\| f | \mathcal { M } \| = \| ( f + g ) | \mathcal { M } \| \leqslant \| f + g \|$ . Taking the infimum over all $g$ we get that $\| f | \mathcal { M } \| \leqslant \| f + \mathcal { M } ^ { \perp } \|$ . Suppose $\phi \in \mathcal { M } ^ { * }$ . The Hahn-Banach Theorem implies that there is an $f$ in $\mathcal { X } ^ { * }$ such that $f | \mathcal { M } = \phi$ and $\| f \| = \| \phi \|$ . Hence $\phi = \rho ( f + \mathcal { M } ^ { \perp } )$ and $\|   \phi   \| = \|   f   \| \geqslant \|   f + \mathcal { M } ^ { \perp }   \|$ ■

Now consider $\mathcal { X } / \mathcal { M } ;$ what is $( \mathcal { X } / \mathcal { M } ) ^ { * } ?$ Let $\mathcal { Q } \colon \mathcal { X }   \to   \mathcal { X } / \mathcal { M }$ be the natural map. If $f \in ( \mathcal { X } / \mathcal { M } ) ^ { * }$ , then $f \circ Q \in \mathcal { X } ^ { * }$ and $\| f \circ Q \| \leqslant \| f \|$ . (Why?) This gives a way of mapping $( \mathcal { X } / \mathcal { M } ) ^ { \star }   \to   \mathcal { X } ^ { \star }$ . What is its image? Is it an isometry?

10.2. Theorem. If $\mathcal { M } \leqslant \mathcal { X }$ and $\mathcal { Q } \colon \mathcal { X }   \to   \mathcal { X } / \mathcal { M }$ is the natural map, then $\rho ( f ) = f \circ Q$ defines an isometric isomorphism of $( \mathcal { X } / \mathcal { M } ) ^ { * }$ onto $\mathcal { M } ^ { \perp }$

PROOF. If $f \in ( \mathcal { X } / \mathcal { M } ) ^ { * }$ and $y \in \mathcal { M } ,$ then $f \circ Q ( y ) = 0 ,$ so $f \circ Q \in \mathcal { M } ^ { \perp }$ . Again, it is easy to see that $\rho \colon ( \mathcal { X } / \mathcal { M } ) ^ { * }   \to   \mathcal { M } ^ { \perp }$ is linear and, as was seen earlier, $\| \rho ( f ) \| \leqslant \| f \|$ . Let $\{ x _ { n } + M \}$ be a sequence in $\mathcal { X } / \mathcal { M }$ such that $\| x _ { n } + \mathcal { M } \| < 1$ and $| f ( x _ { n } + { \mathcal { M } } ) | \to \| f \|$ . For each n there is a $y _ { n }$ in M such that $\| x _ { n } + y _ { n } \| < 1$ Thus $\| \rho ( f ) \| \geqslant | \rho ( f ) ( x _ { n } + y _ { n } ) | = | f ( x _ { n } + \mathcal { M } ) | \rightarrow \| f \|$ , so $\rho$ is an isometry.

To see that $\rho$ is surjective, let $g \in \mathcal { M } ^ { \perp } ;$ then $g { \in } { \mathcal { X } } ^ { * }$ and $g ( \mathcal { M } ) = 0 .$ Define $f ;$ $\mathcal { X } / \mathcal { M } \rightarrow \mathbb { F }$ by $f ( x + { \mathcal { M } } ) = g ( x )$ . Because $g ( \mathcal { M } ) = 0 , f$ is well defined. Also, if $x { \in } { \mathcal { X } }$ and $y \in \mathcal{M}, \left| f(x + \mathcal{M}) \right| = \left| g(x) \right| = \left| g(x + y) \right| \leqslant \left\| g \right\| \left\| x + y \right\|$ . Taking the infimum over all y gives $| f ( x + \mathcal { M } ) | \leqslant \| g \| \| x + \mathcal { M } \|$ . Hence $f { \in } ( { \mathcal { X } } / { \mathcal { M } } ) ^ { * }$ $\rho ( f )   =   g ,$ and $\| f \| \leqslant \| \rho ( f ) \|$

## §11. Reflexive Spaces

If $\mathcal { X }$ is a normed space, then we have seen that $\mathcal { X } ^ { * }$ is a Banach space (5.4). Because $\mathcal { X } ^ { * }$ is a Banach space, it too has a dual space $( \mathcal { X } ^ { * } ) ^ { * } \equiv \mathcal { X } ^ { * * }$ and $\mathcal { X } ^ { * * }$ is a Banach space. Hence $\mathcal { X } ^ { * * }$ has a dual. Can this be kept up?

Before answering this question, let's examine a curious phenomenon. If $x { \in } { \mathcal { X } }$ , then x defines an element  of $\mathcal { X } ^ { * * }$ ; namely, define $\hat { x } \colon \mathcal { X } ^ { * }   \to   \mathbb { F }$ by

$$
\hat { x } ( x ^ { * } )   =   x ^ { * } ( x )\tag{11.1}
$$

for every $x ^ { * }$ in $\mathcal { X } ^ { * }$ . Note that Corollary 6.7 implies that $\| { \hat { \boldsymbol { x } } } \| = \| { \boldsymbol { x } } \|$ for all $x$ in $\mathcal { X }$ . The map $x   \to   \hat { x }$ of $\mathcal { X }   \rightarrow   \mathcal { X } ^ { * * }$ is called the natural map of $\mathcal { X }$ into its second dual.

11.2. Definition. A normed space $\mathcal { X }$ is reflexive if $\mathcal { X } ^ { * * } = \{ \hat { x } \colon x { \in } \mathcal { X } \}$ , where X is defined in (11.1).

First note that a reflexive space $\mathcal { X }$ is isometrically isomorphic to $\mathcal { X } ^ { * * }$ , and hence must be a Banach space. It is not true however, that a Banach space $\mathcal { X }$ that is isometric to $\mathcal { X } ^ { * * }$ is reflexive. The definition of reflexivity stipulates that the isometry be the natural embedding of $\mathcal { X }$ into $\mathcal { X } ^ { * * }$ . In fact, James [1951] gives an example of a nonreflexive space $\mathcal { X }$ that is isometric to $\mathcal { X } ^ { * * }$

11.3. Example. If $1 < p < \infty ,   L ^ { p } ( X , \Omega , \mu )$ is reflexive.

11.4. Example. $c _ { 0 }$ is not reflexive. We know that $c _ { 0 } ^ { * } = l ^ { 1 }$ , so $c _ { 0 } ^ { * * } = ( l ^ { 1 } ) ^ { * } = l ^ { \infty }$ With these identifications, the natural map $c _ { 0 }   \rightarrow   c _ { 0 } ^ { * * }$ is precisely the inclusion map $c _ { 0 }   \to   l ^ { \infty }$

A discussion of reflexivity is best pursued after the weak topology is understood (Chapter V). Until that time, we will say adieu to reflexivity.