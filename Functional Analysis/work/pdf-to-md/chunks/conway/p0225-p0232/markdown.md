then $\sigma ( T ) = \mathrm { c l }   \mathbf { D }$ and for $| \lambda | < 1$ , ker $( T - \lambda )$ is the one-dimensional space spanned by the vector $( 1 , \lambda , \lambda ^ { 2 } , \ldots )$

The next result shows that if S is as in (6.5), then $\partial \mathbf { D } \subseteq \sigma _ { a p } ( S )$

## 6.7. Proposition. If $A   \in   \mathcal { B } ( \mathcal { X } )$ , then $\partial \sigma ( A ) \subseteq \sigma _ { a p } ( A )$

PROOF. Let $\lambda { \in } { \partial } \sigma ( A )$ and let $\left\{ \lambda _ { n } \right\} \subseteq \mathbb { C } \backslash \sigma ( A )$ such that $\lambda _ { n } \rightarrow \lambda _ { 1 }$

6.8. Claim. $\| ( A - \lambda _ { n } ) ^ { - 1 } \| \to \infty \mathrm { a s } n \to \infty$

In fact, if the claim were false, then by passing to a subsequence if necessary, it follows that there is a constant M such that $\| (A - \lambda_n)^{-1} \| \leqslant M$ for all n. Choose n sufficiently large that $| \lambda _ { n } - \lambda | < M ^ { - 1 }$ . Then $\| ( A - \lambda ) - ( A - \lambda _ { n } ) \| <$ $\| ( A - \lambda _ { n } ) ^ { - 1 } \| ^ { - 1 }$ . By (2.3b), this implies that $( A - \lambda )$ is invertible, a contradiction This establishes (6.8).

Let $\| x _ { n } \| = 1$ such that $\alpha_{n} \equiv \left\| \left( A - \lambda_{n} \right)^{-1} x_{n} \right\| > \left\| \left( A - \lambda_{n} \right)^{-1} \right\| - n^{-1}$ , sO $\alpha _ { n } \to \infty$ . Put $y_{n} = \alpha_{n}^{-1}(A - \lambda_{n})^{-1}x_{n};$ hence $\| y _ { \pmb { n } } \| = 1$ Now

$$
\begin{aligned}(A - \lambda)y_{n} &= (A - \lambda_{n})y_{n} + (\lambda - \lambda_{n})y_{n} \\&= \alpha_{n}^{-1}x_{n} + (\lambda - \lambda_{n})y_{n}.\end{aligned}
$$

Thus $\left\| (A - \lambda) y_n \right\| \leqslant \alpha_n^{-1} + \left| \lambda - \lambda_n \right|$ , so that $\| ( A - \lambda ) y _ { n } \| \to 0$ as $n \to \infty$ . That is, $\lambda   \in   \sigma _ { a p } ( A )$ ■

Let $A   \in   \mathcal { B } ( \mathcal { X } )$ and suppose ∆ is a clopen subset of $\sigma ( A ) ;$ that is, ∆ is a subset of $\sigma ( A )$ that is both closed and relatively open. So $\sigma ( A ) = \Delta \cup ( \sigma ( A ) \setminus \Delta )$ . As in Proposition 4.11 (and Exercise 4.9),

$$
E ( \Delta ) = E ( \Delta ; A ) = \frac { 1 } { 2 \pi i } \int _ { \Gamma } ( z - A ) ^ { - 1 } d z ,\tag{6.9}
$$

where Γ is a positively oriented Jordan system such that $\Delta \subseteq$ ins Γ and $\sigma ( A ) \backslash \Delta \subseteq \mathrm { o u t } \Gamma$ , is an idempotent. Moreover, $E ( \Delta ) B = B E ( \Delta )$ whenever $AB = BA$ and if $\mathcal { X } _ { \Delta } = E ( \Delta ) \mathcal { X } , \sigma ( A | \mathcal { X } _ { \Delta } ) = \Delta .$ Call E(∆) the Riesz idempotent corresponding to ∆. If $\mathbf { \Delta } = \mathbf { a }$ singleton set $\{ \lambda \}$ , let $E ( \lambda ) = E ( \{ \lambda \} )$ and $\mathcal { X } _ { \lambda }   =   \mathcal { X } _ { \{ \lambda \} }$ . Note that if λ is an isolated point of $\sigma ( A ) .$ then $\{ l \}$ is a clopen subset of $\sigma ( A )$

6.10. Example. Let $\left\{ \alpha _ { n } \right\} \in l ^ { \infty } , \quad 1 \leqslant p \leqslant \infty$ and define $A \colon \quad l ^ { p }   \to   l ^ { p }$ by $( A x ) ( n ) = \alpha _ { n } x ( n )$ Then $\sigma ( A ) = \mathrm { c l } \left\{ \alpha _ { n } \right\}$ and $\sigma _ { p } ( A ) = \{ \alpha _ { n } \}$ . For each k, define $N _ { k } = \{ n \in \mathbb { N } ;   \alpha _ { n } = \alpha _ { k } \}$ and define $P _ { k } \colon l ^ { p }   \to   l ^ { p }$ by $P _ { k } x = \chi _ { N _ { k } } x$ If $\alpha _ { k }$ is an isolated point of $\sigma ( A )$ , then $\left\{ \alpha _ { k } \right\}$ is a clopen subset of $\sigma ( A )$ and $E(\{ \alpha_{k} \};A) = P_{k}$

Suppose $A   \in   \mathcal { B } ( \mathcal { X } )$ and $\lambda _ { 0 }$ is an isolated point in $\sigma ( A )$ . Hence $E ( \lambda _ { 0 } ) = E ( \lambda _ { 0 } ; A )$ is a well-defined idempotent. Also, $\lambda _ { 0 }$ is an isolated singularity of the analytic function $z \mapsto (z - A)^{-1}  on  \mathbb{C} \backslash \sigma(A)$ . Perhaps the nature of this singularity (pole or essential singularity) will reveal something of the nature of $\lambda _ { 0 }$ as an element of $\sigma ( A )$ . First it is helpful to get the precise form of the Laurent expansion of $( z - A ) ^ { - 1 }$ about $\lambda _ { 0 }$

6.11. Lemma. $\mathit { I f } \: \lambda _ { 0 }$ is an isolated point of $\sigma ( A )$ , then

$$
(z - A)^{-1} = \sum_{n = -\infty}^{\infty} (z - \lambda_0)^n A_n
$$

for $0 < | z - \lambda _ { 0 } | < r _ { 0 } = \mathrm { d i s t } ( \lambda _ { 0 } , \sigma ( A ) \backslash \{ \lambda \} )$ , where

$$
A _ { n } = \frac { 1 } { 2 \pi i } \int _ { \gamma } ( z - \lambda _ { 0 } ) ^ { - n - 1 } ( z - A ) ^ { - 1 } d z
$$

for $\gamma = a n y$ circle centered at $\lambda _ { 0 }$ with radius $< r _ { 0 } .$

The proof follows the lines of the usual Laurent series development (Conway [1978]).

6.12. Proposition. $\mathit { I f } \lambda _ { 0 }$ is an isolated point of σ(A), then $\lambda _ { 0 }$ is a pole of $( z - A ) ^ { - 1 }$ of order n if and only $if \left( \lambda_{0} - A \right)^{n} E(\lambda_{0}) = 0$ and $( \lambda _ { 0 } - A ) ^ { n - 1 } E ( \lambda _ { 0 } ) \neq 0.$

PROOF. Let $(z - A)^{-1} = \sum_{n = -\infty}^{\infty} (z - \lambda_0)^n A_n$ as is (6.11). Now $\lambda _ { 0 }$ is a pole of order n if and only if $A _ { - n } \neq 0$ and $A _ { - k } = 0$ for $k > n .$ Let Γ be a positively oriented system of curves such that $\sigma ( A ) \backslash \{ \lambda _ { 0 } \} \subseteq \mathrm { i n s }   \Gamma$ and $\lambda _ { 0 } { \in } \mathbf { o u t }   \Gamma .$ Let $\gamma$ be a circle centered at $\lambda _ { 0 }$ and contained in out Γ. Let $e ( z ) \equiv 1$ in a neighborhood of $\gamma \cup$ ins γ and $e ( z ) \equiv 0$ in a neighborhood of Γ∪ins Γ. So $e \in \mathrm{HCl}(A)$ and $e(A) = E(\lambda_0)$ . If $k \geqslant 1$

$$
\begin{align*}A_{-k} = & \frac{1}{2\pi i} \int_{\gamma} (z - \lambda_0)^{k-1} (z - A)^{-1} dz \\= & \frac{1}{2\pi i} \int_{\gamma + \Gamma} e(z) (z - \lambda_0)^{k-1} (z - A)^{-1} dz \\= & E(\lambda_0) (A - \lambda_0)^{k-1}\end{align*}
$$

since $\sigma ( A ) \subseteq \mathrm { i n s } ( \gamma + \Gamma ) = \mathrm { i n s }   \gamma \cup \mathrm { i n s }   \Gamma$ . The proposition now follows.

6.13. Corollary. If $\lambda _ { 0 }$ is an isolated point of $\sigma ( A )$ and is a pole of $( z - A ) ^ { - 1 }$ then $\lambda _ { 0 } { \in } \sigma _ { p } ( A )$

In fact, the preceding result implies that if n is the order of the pole, then $(0) \neq (\lambda_0 - A)^{n-1} E(\lambda_0) \mathcal{X} \subseteq \ker(A - \lambda_0)$

6.14. Example. A measurable function k: $[ 0 , 1 ] \times [ 0 , 1 ]   \to   \pmb { \mathbb { C } }$ is called a Volterra kernel if k is bounded and $k ( x ,   y )   =   0$ when $x < y$ . If $1 \leqslant p \leqslant \infty$ and k is a Volterra kernel, define $V _ { k } : L ^ { p } ( 0 , 1 ) \to L ^ { p } ( 0 , 1 )$ by

$$
V_{k}f(x)=\int_{0}^{1}k(x,y)f(y)dy=\int_{0}^{x}k(x,y)f(y)dy.
$$

Then $V _ { k }   \in   \mathcal { B } ( L ^ { p } )$ and $\|   V _ { \boldsymbol { k } } \| \leqslant \|   k   \| _ { \infty }$ (III.2.3).

If k, h are Volterra kernels and

$$
( h k ) ( x , y ) = \int _ { 0 } ^ { 1 } h ( x , t ) k ( t , y ) d t ,
$$

then hk is a Volterra kernel, $\| h k \| _ { \infty } \leqslant \| h \| _ { \infty } \| k \| _ { \infty } ,$ and $V _ { h k } = V _ { h } V _ { k }$ .Note that if $k ( x , y )$ is the characteristic function of $\{ ( x , y ) { \in } [ 0 , 1 ] \times [ 0 , 1 ] { : } y < x \}$ , then $V _ { k }$ is the Volterra operator (II.1.7).

If k is a Volterra kernel, then

$$
\sigma ( V _ { k } ) = \{ 0 \} .
$$

Indeed, from the preceding paragraph it is known that $V _ { k } ^ { n }   =   V _ { k ^ { n } }$ . This will be used to show that the spectral radius of $V _ { k }$ is 0.

## 6.15. Claim. $| k ^ { n } ( x , y ) | \leqslant ( \| k \| _ { \infty } ^ { n } / ( n - 1 ) ! ) ( x - y ) ^ { n - 1 } \text { for } y < x.$

This is proved by induction. Clearly it holds for $n = 1$ . Suppose (6.15) is true for some $n \geqslant 1$ . Then

$$
\begin{align*}|k^{n+1}(x,   y)| &= \Bigg| \int_{y}^{x} k(x,   t)k^n(t,   y)dt \Bigg| \\&\leqslant \int_{y}^{x} |k(x,   t)|   |k^n(t,   y)|   dt \\&\leqslant \|   k   \|_{\infty} \frac{\|   k   \|_{\infty}^n}{(n-1)!} \int_{y}^{x} (t-y)^{n-1} dt \\&\leqslant \frac{\|   k   \|_{\infty}^{n+1}}{n!} (x-y)^n.\end{align*}
$$

This establishes the claim.

From (6.15) it follows that

$$
\| V _ { k } ^ { n } \| \leqslant \| k ^ { n } \| _ { \infty } \leqslant \frac { \| k \| _ { \infty } ^ { n } } { ( n - 1 ) ! } .
$$

Therefore

$$
\| V _ { k } ^ { n } \| ^ { 1 / n } \leqslant \| k \| _ { \infty } [ ( n - 1 ) ! ] ^ { - 1 / n } .
$$

Since $\left[ (n-1)! \right]^{-1/n} \to 0   as   n \to \infty, r(V_k) = 0.   Thus   \Omega \neq \sigma(V_k) \in \{\lambda \in \mathbb{C}: |\lambda| \leq 0\};$ that is, $\sigma ( V _ { k } ) = \{ 0 \}$

It is possible for ker $V _ { k }$ to be nontrivial. For example, if $k ( x , y ) = \chi _ { ( 0 , 1 / 2 ) } ( y )$

when $y < x$ and 0 otherwise, then

$$
V _ { k } f ( x ) = \left\{ \begin{aligned} & \int _ { 0 } ^ { x } f ( y ) d y \quad \text { if } x \leqslant \frac { 1 } { 2 } , \\ & \int _ { 0 } ^ { 1 / 2 } f ( y ) d y \quad \text { if } x \geqslant \frac { 1 } { 2 } . \end{aligned} \right.
$$

So if $f ( y )   =   0$ for $0 \leqslant y \leqslant \frac{1}{2}, V_{k}f = 0.$

On the other hand, the Volterra operator $V [ = V _ { k }$ for $k ( x , y ) = \mathrm { t h e }$ characteristic function of $\{ ( x , y ) ;   y   <   x \} ]$ has ker $V = ( 0 )$ . In fact, if $0 = V f ,$ then for all $x,0=\int_{0}^{x}f(y)dy$ . Differentiating gives that $f = 0$

Is there an analogy between $V _ { k }$ for a Volterra kernel k and a lower triangular matrix?

## EXERCISES

1. Prove Proposition 6.1.

2. Show that for $\mathcal { X }$ a Banach space and A in $\mathcal { B } ( \mathcal { X } ) , \; \sigma _ { l } ( A ) = \sigma _ { r } ( A ^ { * } )$ . What happens in a Hilbert space?

3. If  is an infinite dimension Hilbert space and K is a non-empty compact subset of C, show that there is an A in $\mathcal { B } ( \mathcal { H } )$ such that $\sigma ( A ) = K$ . Can A be found such that $\sigma ( A ) = \sigma _ { a p } ( A ) = K ?$

4. Let K be a compact subset of C. Does there exist an operator A in $\mathcal { B } ( C [ 0 , 1 ] )$ such that $\sigma ( A ) = K ?$

5. If X is a Banach space and $A   \in   \mathcal { B } ( \mathcal { X } )$ , show that A is left invertible if and only if ker $A = ( 0 )$ and ran A is a closed complemented subspace of ¿.

6. If X is a Banach space and $A   \in   \mathcal { B } ( \mathcal { X } )$ , show that A is right invertible if and only if ran $A = { \mathcal { X } }$ and ker A is a complemented subspace of ¿.

7. If X is a Banach space and $T \colon { \mathcal { X } }   \to   { \mathcal { X } }$ is an isometry, then either $\sigma ( T )   \subseteq   \partial \mathbb { D }$ or $\sigma ( T ) = \mathrm { c l }   \mathbf { D } .$

8. Verify the statements made in Example 6.10.

9. Let $1 \leqslant p \leqslant \infty$ and suppose $0 < \alpha_{1} \leqslant \alpha_{2} \cdots$ such that r = lim $\alpha _ { n } < \infty$ . Define A: $l ^ { p } \to l ^ { p }$ by $A(x_{1},x_{2},\ldots)=(0,\alpha_{1}x_{1},\alpha_{2}x_{2},\ldots)$ . Show that $\sigma ( A ) = \{ z \in \mathbb { C } : | z | \leqslant r \}$ and $\sigma _ { a p } ( A ) = \partial \sigma ( A )$ If $| \lambda | < r .$ , then ran $( A - \lambda )$ is closed and has codimension 1. Also, $\sigma _ { p } ( A ) = \square$

10. Verify the statements made in Example 6.14.

11. Let $1 \leqslant p \leqslant \infty$ and let $( X , \Omega , \mu )$ be a σ-finite measure space. For $\phi$ in $L ^ { \infty } ( \mu )$ , define $M _ { \phi }$ on $L ^ { p } ( \mu )$ as in Example III.2.2. Find $\sigma ( M _ { \phi } ) ,   \sigma _ { a p } ( M _ { \phi } ) .$ and $\sigma _ { p } ( M _ { \phi } )$

12. If $A   \in   \mathcal { B } ( \mathcal { X } )$ f ∈Hol(A), and $\lambda   \in   \sigma _ { p } ( A ) ,$ is $f ( \lambda ) \in \sigma _ { p } ( f ( A ) ) ? \quad \mathrm { I f } \quad \lambda \in \sigma _ { a p } ( A )$ $f(\lambda) \in \sigma_{ap}(f(A))?$ Is there a relation between $f ( \sigma _ { a p } ( A ) )$ and $\sigma _ { a p } ( f ( A ) ) ?$

13. If $A   \in   \mathcal { B } ( \mathcal { X } )$ say that a complex number λ has finite index if there is a positive integer k such that ker $(A - \lambda)^k = \ker(A - \lambda)^{k+1};$ the index of $\lambda ,$ denoted by v(λ)

or $v _ { A } ( i )$ , is the smallest such integer k. (a) Show that if λ is an isolated point of $\sigma ( A )$ and a pole of order n of $( z - A ) ^ { - 1 }$ , then $v ( { \hat { \lambda } } ) = n .$ (b) If $v ( \lambda ) < \infty$ , show that

$$
ker(A - \lambda)^{\nu(\lambda)} = \ker(A - \lambda)^{\nu(\lambda) + k}   for all   k \geq 0. \\ (c) If   \mathcal{X} = \mathbb{C}^*   and   A = \begin{bmatrix} 0 & & & \\ 1 & 0 & & \\ & 1 & \ddots & \\ & & \ddots & \\ & & 1 & 0 \end{bmatrix}.
$$

then $\sigma ( A ) = \{ 0 \} \mathrm { a n d } v ( 0 ) = n .$

14. If V is the Volterra operator, show that 0 is an essential singularity of $( z - V ) ^ { - 1 }$

15. Let $\rtimes$ be a Banach algebra with identity. If $a \in \mathcal { A } ,$ define $L _ { a } , R _ { a } { \in } { \mathcal { B } } ( { \mathcal { A } } )$ by $L _ { a } ( x ) = a x$ and $R _ { a } ( x ) = x a$ Show that $\sigma ( L _ { a } ) = \sigma ( R _ { a } ) = \sigma ( a ) .$

16. If E is a projection on a Hilbert space and E is neither 0 nor 1, then $\sigma ( E ) = \{ 0 , 1 \}$

17. (McCabe [1984]) If X is a complex Banach space and $T   \in   \mathcal { B } ( \mathcal { X } ) ,$ ,show that the following statements are equivalent. (a) $r(T) < 1. (b) \|T^m\| < 1$ for some positive integer m. (c) $\scriptstyle \sum _ { n } \| T ^ { n } ( x ) \| < \infty$ for every x in $\mathcal { X }$

## §7. The Spectral Theory of a Compact Operator

Recall that for a Banach space $\mathcal { X } ,   \mathcal { B } _ { 0 } ( \mathcal { X } )$ is the algebra of all compact operators. This Banach algebra has no identity, so if $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ , then $\sigma ( A )$ refers to the spectrum of A as an element of (X). Of course, if $\mathcal { A } = \mathcal { B } _ { 0 } ( \mathcal { X } ) +$ $\mathbf { C } ,$ then $\varkappa$ is a Banach algebra with identity (Why?) and we could consider $\sigma _ { \mathcal { A } } ( A )$ for A in $\mathcal { B } _ { 0 } ( \mathcal { X } )$ . By Theorem 5.4, $\sigma ( A ) \in \sigma _ { \mathcal { A } } ( A )$ $\partial \sigma _ { \mathcal { A } } ( A ) \subseteq \sigma ( A )$ , and $\sigma ( A ) = \sigma _ { \mathcal { A } } ( A )$ . Below, in Theorem 7.1, it will be shown that $\sigma ( A )$ is a countable set and hence $\sigma ( A ) = \partial \sigma ( A ) = \sigma ( A ) ^ { \wedge }$ . Thus $\sigma ( A ) = \sigma _ { \mathcal { A } } ( A )$

7.1. Theorem. (F. Riesz) If dim $\mathcal { X } = \infty$ and $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ , then one and only one of the following possibilities occurs.

(a) $\sigma ( A ) = \{ 0 \}$

(b) $\sigma ( A ) = \{ 0 , \lambda _ { 1 } , \ldots , \lambda _ { n } \}$ , where for $1 \leqslant k \leqslant n,\ \lambda_{k} \neq 0$ , each $\lambda _ { k }$ is an eigenvalue of A, and dim ker $( A - \lambda _ { k } ) < \infty$

(c) $\sigma ( A ) = \{ 0 , \lambda _ { 1 } , \lambda _ { 2 } , \ldots \}$ , where for each $k \geqslant 1 , \lambda _ { k }$ is an eigenvalue of A, dim ker $( A - \lambda _ { k } ) < \infty$ , and, moreover, lim $\lambda _ { k }   =   0$

The proof will use several lemmas. The first lemma was given in the case that $\mathcal { X }$ is a Hilbert space in Proposition II.4.14. The proof is identical and will not be repeated here.

7.2. Lemma. $If A \in \mathcal{B}_0(\mathcal{X}), \lambda \neq 0,$ , and ker(A − λ) = (0), then $\operatorname { \mathsf { r a n } } ( A - \lambda )$ is closed.

The proof of the next lemma is like that of Corollary II.4.15.

7.3. Lemma. $If A \in \mathcal{B}_0(\mathcal{X}), \lambda \neq 0,$ and $\lambda { \in } { \sigma } ( A )$ , then either $\lambda \in \sigma _ { p } ( A )   or   \lambda \in \sigma _ { p } ( A ^ { * } )$

7.4. Lemma. If $\mathcal { M } \leqslant \mathcal { N } , \mathcal { M } \neq \mathcal { N }$ , and $\varepsilon   >   0 .$ , then there is a y in $\mathcal { N }$ such that二 $y \| = 1$ and dist $( y , \mathcal { M } ) \geqslant 1 - \varepsilon .$

PROOF. Let $\delta ( y ) = \mathrm { d i s t } ( y , \mathcal { M } )$ for every y in N. Now if $y _ { 1 } \in \mathcal { N } \backslash \mathcal { M } .$ , there is an $x _ { 0 }$ in M such that $\delta ( y _ { 1 } ) \leqslant \| x _ { 0 } - y _ { 1 } \| \leqslant ( 1 + \varepsilon ) \delta ( y _ { 1 } ) .$ Let $y _ { 2 } = y _ { 1 } - x _ { 0 }$ Then $( 1 + \varepsilon ) \delta ( y _ { 2 } ) = ( 1 + \varepsilon )$ inf $\{ \| y _ { 2 } - x \| \colon x { \in } { \mathcal { M } } \} = ( 1 + \varepsilon )$ inf { Ⅱ $y _ { 1 } - x _ { 0 } - x \parallel :$ $x \in \mathcal { M } \left\{ = ( 1 + \varepsilon ) \delta ( y _ { 1 } ) \right\}$ since $x _ { 0 } \in \mathcal { M }$ . Thus $(1 + \varepsilon) \delta(y_2) > \|x_0 - y_1\| = \|y_2\|$ . Let $y = \|   y _ { 2 }   \| ^ {   -   1 } y _ { 2 }$ . So $\| y \| = 1$ , y∈N, and if $x \in \mathcal { M }$ , then

$$
\begin{align*}\|   y - x   \| &= \|   \|   y_2   \|^{-1} y_2 - x   \| \\&= \|   y_2   \|^{-1}   \|   y_2 - \|   y_2   \|   x   \| > [(1 + \varepsilon) \delta(y_2)]^{-1}   \|   y_2 - \|   y_2   \|   x   \| \\& \quad \geqslant (1 + \varepsilon)^{-1} > 1 - \varepsilon.\end{align*}
$$

If $\mathcal { M }$ and $\mathcal { N }$ are finite dimensional in the preceding lemma, then y can be chosen in $\mathcal { N }$ such that $\| y \| = 1$ and dist $( y , \mathcal { M } ) = 1$ (see Exercise 1).

7.5. Lemma. If $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ and $\{ \lambda _ { n } \}$ is a sequence of distinct elements in $\sigma _ { p } ( A )$ then lim $\lambda _ { n }   =   0$

PROOF. For each n let $x_{n} \in \ker(A - \lambda_{n})$ such that $x _ { n }   \neq   0 .$ It follows that if $\mathcal { M } _ { n } = \vee \{ x _ { 1 } , \ldots , x _ { n } \}$ , then dim $\mathcal { M } _ { n } = n$ (Exercise). Hence $\mathcal { M } _ { n } \leqslant \mathcal { M } _ { n + 1 }$ and $\mathcal { M } _ { n } \neq \mathcal { M } _ { n + 1 }$ . By the preceding lemma there is a vector $y _ { n }$ in $\mathcal { M } _ { n }$ such that二 $\| y _ { n } \| = 1$ and dist $( y _ { n } , \mathcal { M } _ { n - 1 } ) > \frac { 1 } { 2 }$ . Let $y _ { n } = \alpha _ { 1 } x _ { 1 } + \cdots + \alpha _ { n } x _ { n }$ Hence

$$
(A - \lambda_n)y_n = \alpha_1(\lambda_1 - \lambda_n)x_1 + \cdots + \alpha_{n-1}(\lambda_{n-1} - \lambda_n)x_{n-1} \in \mathcal{M}_{n-1}.
$$

So if $n > m$

$$
A(\lambda_{n}^{-1}y_{n})-A(\lambda_{m}^{-1}y_{m})=\lambda_{n}^{-1}(A-\lambda_{n})y_{n}-\lambda_{m}^{-1}(A-\lambda_{m})y_{m}+y_{n}-y_{m}\\=y_{n}-[y_{m}+\lambda_{m}^{-1}(A-\lambda_{m})y_{m}-\lambda_{n}^{-1}(A-\lambda_{n})y_{n}].
$$

But the bracketed expression belongs to $\mathcal { M } _ { n - 1 }$ . Hence $\| A ( \lambda _ { n } ^ { - 1 } y _ { n } ) -$ $\begin{array} { r } { \| A ( \lambda _ { m } ^ { - 1 } y _ { m } ) \| \geqslant \mathrm { d i s t } ( y _ { n } , \mathcal { M } _ { n - 1 } ) > \frac { 1 } { 2 } } \end{array}$ . Therefore $A ( \lambda _ { n } ^ { - 1 } y _ { n } )$ can have no convergent subsequence. But A is a compact operator so that if S is any bounded subset of $\mathcal { X } .$ cl $A ( S )$ is compact. Thus it must be that $\{ \lambda _ { n } ^ { - 1 } y _ { n } \}$ has no bounded subsequence. Since $\| y _ { n } \| = 1$ for all $n ,$ it must be that $\| \lambda _ { n } ^ { - 1 } y _ { n } \| = | \lambda _ { n } | ^ { - 1 } \to \infty$ That is, $0 = \lim_{n \to \infty} \lambda_n.$

PRoOF OF THEOREM 7.1. The first step is to establish the following.

7.6. Claim. If $\lambda   \in   \sigma ( A )$ and $\lambda \neq 0 .$ , then λ is an isolated point of $\sigma ( A )$

In fact, if $\{ \lambda _ { n } \} \subseteq \sigma ( A )$ and $\lambda _ { n } \to \lambda _ { 1 }$ , then each $\lambda _ { n }$ belongs to either $\sigma _ { p } ( A )$ or $\sigma _ { p } ( A ^ { * } ) \left( 7 . 3 \right)$ . So either there is a subsequence $\{ \lambda _ { n _ { k } } \}$ that is contained in $\sigma _ { p } ( A )$

or there is a subsequence contained in $\sigma _ { p } ( A ^ { * } )$ If $\left\{ \lambda _ { n _ { k } } \right\} \subseteq \sigma _ { p } ( A )$ , then Lemma 7.5 implies $\lambda _ { n _ { k } }   \to   0 ,$ , a contradiction. If $\{ \lambda _ { n _ { k } } \} \subseteq \sigma _ { p } ( A ^ { * } )$ , then the fact that $A ^ { * }$ is compact gives the same contradiction. Thus λ must be isolated if $\lambda \neq 0$

7.7. Claim. If $\lambda { \in } { \sigma } ( A )$ and $\lambda \neq 0 ,$ then $\lambda   \in   \sigma _ { p } ( A )$ and dim ker $( A - \lambda ) < \infty$

By (7.6), λ is an isolated point of $\sigma ( A )$ so that $E ( \lambda )$ can be defined as in (6.9). Let $\mathcal { X } _ { \lambda } = E ( \lambda ) \mathcal { X }$ and $A _ { \lambda } = A | \mathcal { X } _ { \lambda }$ By Exercise 4.9 [also see (4.11)], $\sigma ( A _ { \lambda } ) = \{ \lambda \}$ . Thus $A _ { \lambda }$ is an invertible compact operator. By Exercise VI.3.5, dim $\mathcal { X } _ { \lambda } < \infty$ . If $n = \dim \mathcal{X}_{\lambda},$ then $A _ { \lambda } - \lambda$ is a nilpotent operator on an n-dimensional space. Thus $( A _ { \lambda } - \lambda ) ^ { n } = 0$ . Let $y = \mathbf { t h e }$ positive integer such that $( A _ { \lambda } - \lambda ) ^ { v } = 0$ but $( A _ { \lambda } - \lambda ) ^ { v - 1 } \neq 0$ . Let $x { \in } { \mathcal { X } } _ { \lambda }$ such that $0 \ne (A_{\lambda} - \lambda)^{v - 1}x = y;$ then $(A - \lambda)y = 0.$ Thus $\lambda   \in   \sigma _ { p } ( A )$

Also, ker $(A - \lambda) \in \mathrm{Lat} A$ and $A \left| \ker ( A - \lambda ) \right.$ is compact. But $A x = \lambda x$ for all x in ker $( A - \lambda )$ , so dim ker $( A - \lambda ) < \infty$

Now for the dénouement. If dim $\mathcal { X } = \infty$ and $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } ) ,$ , then A cannot be invertible (Exercise VI.3.5). Thus $0   \in   \sigma ( A )$ . If $\lambda \in \sigma ( A )$ and $\lambda \neq 0 ,$ , then Claim 7.7 says that $\lambda   \in   \sigma _ { p } ( A )$ and dim ker $( A - \lambda ) < \infty$ . So if $\sigma ( A )$ is finite, either (a) or (b) of (7.1) hold. If $\sigma ( A )$ is infinite, then Claim 7.6 implies that $\sigma ( A )$ is countable. So let $\sigma ( A ) = \{ 0 , \lambda _ { 1 } , \lambda _ { 2 } , \ldots \}$ . By Lemma 7.5 and Claim 7.7, (c) holds.

Part of the following surfaced in the proof of the theorem.

7.8. Corollary. $I f A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ and $\lambda   \in   \sigma ( A )$ with $\lambda \neq 0 ,$ then λ is a pole of $( z - A ) ^ { - 1 }$ ker $( A - \lambda ) \subseteq E ( \lambda ) \mathcal { X }$ , and dim $E(\lambda)\mathcal{X} < \infty$

ProoF. The only part of this corollary that did not appear in the preceding proof is the fact that ker $( A - \lambda ) \in E ( \lambda ) \mathcal { X }$

Let $\Delta = \sigma ( A ) \backslash \{ \lambda \} , \mathcal { X } _ { \Delta } = E ( \Delta ) \mathcal { X } , A _ { \Delta } = A \backslash \mathcal { X } _ { \Delta }$ . By Exercise $4.9, \sigma(A_{\Delta}) = \Delta;$ sO $A _ { \Delta } - \lambda$ is invertible on $\mathcal { X } _ { \pmb { \Delta } }$ . If $x { \in } \ker ( A - \lambda ) ,$ then $x = E ( \lambda ) x + E ( \Delta ) x$ . Hence $0 = (A - \lambda)x = (A - \lambda)E(\lambda)x + (A - \lambda)E(\Delta)x = (A_{\lambda} - \lambda)E(\lambda)x + (A_{\Delta} - \lambda)E(\Delta)x.$ But $\mathcal { X } _ { \lambda }$ and $\mathcal { X } _ { \Delta } { \in } \operatorname { L a t } A$ ,so $( A _ { \lambda } - \lambda ) E ( \lambda ) x \in \mathcal { X } _ { \lambda }$ and $( A _ { \Delta } - \lambda ) E ( \Delta ) x \in \mathcal { X } _ { \Delta } ;$ since $\mathcal { X } _ { \lambda } \cap \mathcal { X } _ { \Delta } = ( 0 ) , \; 0 = ( A _ { \lambda } - \lambda ) E ( \lambda ) x = ( A _ { \Delta } - \lambda ) E ( \Delta ) x .$ But $A _ { \Delta } - \lambda$ is invertible so $E ( \Delta ) x = 0 ;$ that is, $x = E ( \lambda ) x \in \mathcal { X } _ { \lambda }$ . Hence ker $( A - \lambda ) \subseteq { \mathcal { X } } _ { \lambda }$ ■

If k is a Volterra kernel (6.14), then $V _ { k }$ is a compact operator (Exercise VI.3.6) and $\sigma ( V _ { k } ) = \{ 0 \}$ . So the first possibility of Theorem 7.1 can occur. If V is the Volterra operator, then $\sigma _ { p } ( V ) = \square$

Let V be the Volterra operator on $L ^ { p } ( 0 , 1 ) ,   1 < p < \infty$ . If $\lambda _ { 1 } , \ldots , \lambda _ { n } { \in } \pmb { \mathbb { C } } ,$ let $D \colon \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$ be defined by $D(z_1,\ldots,z_n)=(\lambda_1 z_1,\ldots,\lambda_n z_n)$ Then $A = V \oplus D$ on $L ^ { p } ( 0 , 1 ) \oplus \mathbb { C } ^ { n }$ is compact and $\sigma ( A ) = \{ 0 , \lambda _ { 1 } , \ldots , \lambda _ { n } \} .$ So the second possibility of (7.1) occurs. If $\{ \lambda _ { n } \} \subseteq \mathbf { C }$ and lim $\lambda _ { n }   =   0 .$ , then define D: $l ^ { p } \rightarrow l ^ { p } ( 1 \leqslant p \leqslant \infty )$ by $(Dx)(n) = \lambda_n x(n)$ . If $A = V \oplus D$ on $L ^ { p } ( 0 , 1 ) \oplus l ^ { p } , A$ is compact and $\sigma ( A ) = \{ 0 , \lambda _ { 1 } , \lambda _ { 2 } , \ldots \}$ (see Exercise 3).

The next result has a number of applications in the theory of integral equations.

7.9. The Fredholm Alternative. If $A \in \mathcal { B } _ { 0 } ( \mathcal { X } ) , \lambda \in \mathbf { C }$ , and $\lambda \neq 0 .$ , then $\operatorname { \mathsf { r a n } } ( A - { \mathfrak { i } } )$ is closed and dim ker $(A - \lambda) = \dim \ker(A - \lambda)^* < \infty$

ProOF. It suffices to assume that $\lambda { \in } { \sigma } ( A )$ . Put $\Delta = \sigma ( A ) \backslash \{ \lambda \} , \mathcal { X } _ { \lambda } = E ( \lambda ) \mathcal { X }$ $\mathcal { X } _ { \Delta } = E ( \Delta ) \mathcal { X } , \quad A _ { \lambda } = A | \mathcal { X } _ { \lambda } ,$ and $A _ { \Delta } = A | \mathcal { X } _ { \Delta }$ . Now $\lambda \notin \Delta = \sigma ( A _ { \Delta } ) ,$ so $A _ { \Delta } - \lambda$ is invertible. Thus ran $( A _ { \Delta } - \lambda ) = \mathcal { X } _ { \Delta }$ Hence $\mathrm{ran}(A - \lambda) = (A - \lambda)\mathcal{X}_{\lambda} +$ $(A - \lambda)\mathcal{X}_{\Delta} = \mathrm{ran}(A_{\lambda} - \lambda) + \mathcal{X}_{\Delta}$ .Since dim $\mathcal { X } _ { \lambda } < \infty$ , ran(A - λ) is closed (III.4.3).

Also note that

$$
\begin{aligned}\mathcal{X}/\mathrm{ran}(A - \lambda) &= (\mathcal{X}_{\Delta} + \mathcal{X}_{\lambda})/[\mathrm{ran}(A_{\lambda} - \lambda) + \mathcal{X}_{\Delta}] \\&\approx \mathcal{X}_{\lambda}/\mathrm{ran}(A_{\lambda} - \lambda).\end{aligned}
$$

Since dim $\mathcal { X } _ { \lambda } < \infty$ , dim[X/ran(A − λ)] = dim Xλ − dim ran $( A _ { \lambda }   -   \lambda ) =$ dim ker $( A _ { \lambda } - \lambda ) =$ dim ker(A − λ) < ∞ since $\ker ( A   -   \lambda ) \subseteq { \mathcal { X } } _ { \lambda }   ( 7 . 8 )$ . But $[ { \mathcal { X } } / \mathrm { r a n } ( A - \lambda ) ] ^ { \bullet } = [ \mathrm { r a n } ( A - \lambda ) ] ^ { \perp } ( \mathrm { I I I } . 1 0 . 2 ) = \mathrm { k e r } ( A - \lambda ) ^ { \bullet }$ . Hence dim ker(A − λ) = dim ker(A − λ)\*.

7.10. Corollary. If $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } ) ,   \lambda   \in   \mathbb { C } .$ and $\lambda \neq 0$ , then for every y in $\mathcal { X }$ there is an x in X such that

## 7.11

$$
( A - \lambda ) x = y
$$

if and only if the only vector x such that $(A - \lambda)x = 0   is   x = 0$ . If this condition is satisfied, then the solution to (7.11) is unique.

This corollary is a rephrasing of part of the Fredholm Alternative together with the fact that an operator has dense range if and only if its adjoint has a trivial kernel.

The applications of the Fredholm Alternative occur by taking the compact operator to be an integral operator.

## EXERCISES

1. If $\mathcal { M } , \mathcal { N }$ are finite dimensional spaces and $\mathcal { M } \leqslant \mathcal { N } , \mathcal { M } \neq \mathcal { N }$ , then there is a y in $\mathcal { N }$ such that $\| y \| = 1$ and $\mathrm { d i s t } ( y , \mathcal { M } ) = 1$

2. Let $A   \in   \mathcal { B } ( \mathcal { X } )$ and let $\lambda _ { 1 } , \ldots , \lambda _ { n }$ be distinct points in $\sigma _ { p } ( A )$ . If $x_{k} \in \ker(A - \lambda_{k})$ $1 \leqslant k \leqslant n ,$ and $x _ { k }   \neq   0 .$ , show that $\{ x _ { 1 } , \ldots , x _ { n } \}$ is a linearly independent set.

3. Let $\mathcal { X } _ { 1 } , \mathcal { X } _ { 2 } . .$ . be Banach spaces and put $\mathcal { X } = \oplus _ { p } \mathcal { X } _ { n } .$ Let $A _ { n } \in \mathcal { B } ( \mathcal { X } _ { n } )$ such that $\sup_{n}\|A_{n}\|<\infty$ and define $A \colon { \mathcal { X } }   \to   { \mathcal { X } }$ by $A\left\{x_{n}\right\}=\left\{A_{n}x_{n}\right\}$ . Show that $A   \in   \mathcal { B } ( \mathcal { X } )$ and $\| A \| = \sup_{n} \| A_{n} \|$ . Show that $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ if and only if each $A _ { n } { \in } { \mathcal { B } } _ { 0 } ( { \mathcal { X } } )$ and lim| $\| A _ { n } \| = 0 .$

4. Suppose $A   \in   \mathcal { B } ( \mathcal { X } )$ and there is a polynomial p such that $p ( A ) { \in } { \mathcal { B } } _ { 0 } ( { \mathcal { X } } )$ . What can be said about σ(A)?