Hyperplanes in a normed space fall into one of two categories.

5.2. Proposition. If $\mathcal { X }$ is a normed space and M is a hyperplane in $\mathcal { X } ,$ then either M is closed or M is dense.

PRooF. Consider cl M, the closure of M. By Proposition 1.3, cl $\mathcal { M }$ is a linear manifold in $\mathcal { X }$ Since $\mathcal { M } \subseteq \mathrm { c l } \mathcal { M }$ and dim $\mathcal { X } / \mathcal { M } = 1$ , either cl $\mathcal { M } = \mathcal { M }$ or cl $\mathcal { M } = \mathcal { X }$ ■

If $\mathcal { X } = c _ { 0 }$ and $f \colon { \mathcal { X } }   \to   \mathbb { F }$ is defined by $f(\alpha_{1},\alpha_{2},\ldots)=\alpha_{1}$ , then ker $f =$ $\left\{ ( \alpha _ { n } ) \in c _ { 0 } : \alpha _ { 1 } = 0 \right\}$ is closed in $c _ { 0 }$ . To get an example of a dense hyperplane, let $\mathcal { X }   =   c _ { 0 }$ and let $e _ { n }$ be the element of $c _ { 0 }$ such that $e _ { n } ( k ) = 0$ if $k \neq n$ and $e _ { n } ( n ) = 1$ . (It is best to think of $c _ { 0 }$ as a collection of functions on N.) Let $x _ { 0 } ( n ) = 1 / n$ for all $n ,$ so $x _ { 0 } { \in } c _ { 0 }$ and $\{ x _ { 0 } , e _ { 1 } , e _ { 2 } , \ldots \}$ is a linearly independent set in $c _ { 0 }$ . Let $\mathcal { B } = \mathbf { a }$ Hamel basis in $c _ { 0 }$ which contains $\{ x _ { 0 } , e _ { 1 } , e _ { 2 } , \ldots \}$ . Put $\mathcal { B } = \{ x _ { 0 } , e _ { 1 } , e _ { 2 } , \ldots \} \cup \{ b _ { i } : i \in I \} , b _ { i } \neq x _ { 0 }$ or $e _ { n }$ for any i or n. Define $f \colon c _ { 0 }   \to   \mathbb { F }$ by $f(\alpha_{0}x_{0}+\sum_{n = 1}^{\infty}\alpha_{n}e_{n}+\sum_{i}\beta_{i}b_{i})=\alpha_{0}$ . (Remember that in the preceding expression at most a finite number of the $\alpha _ { n }$ and $\beta _ { i }$ are not zero.) Since $e _ { n }$ ∈ker f for all $n \geqslant 1$ , ker f is dense but clearly ker $f \neq c _ { 0 }$

The dichotomy that exists for hyperplanes should be reflected in a dichotomy for linear functionals.

5.3. Theorem. If X is a normed space and $f \colon { \mathcal { X } }   \to   \mathbf { F }$ is a linear functional, then f is continuous if and only if ker f is closed.

PRoOF. If f is continuous, ker $f   =   f ^ { -   1 } ( \{ 0 \} )$ and so ker f must be closed. Assume now that ker f is closed and let $\mathcal { Q } \colon \mathcal { X }   \to   \mathcal { X } / \ker f$ be the natural map. By (4.2), Q is continuous. Let T: X/ker $f   \to   \mathbb { F }$ be an isomorphism; by (3.4), T is continuous. Thus, if $g = T \circ Q : \mathcal { X } \to \mathbb { F } , g$ is continuous and ker $f = \ker g .$ Hence (5.1) $f = \alpha g$ for some α in F and so $f$ is continuous. ■

If $f \colon { \mathcal { X } }   \to   \mathbb { F }$ is a linear functional, then f is a linear transformation and so Proposition 2.1 applies. Continuous linear functionals are also called bounded linear functionals and

$$
\| f \| \equiv \sup \{ | f ( x ) | : \| x \| \leqslant 1 \}.
$$

The other formulas for $\| f \|$ given in (2.1) are also valid here. Let $\mathcal { X } ^ { * } \equiv \mathsf { t h e }$ collection of all bounded linear functionals on $\mathcal { X }$ If $f , g   \in   \mathcal { X } ^ { * }$ and $\alpha { \in } F$ , define $( \alpha f + g ) ( x ) = \alpha f ( x ) + g ( x ) ; \quad \mathcal { X } ^ { * }$ is called the dual space of $\mathcal { X }$ . Note that $\mathcal { X } ^ { * } = \mathcal { B } ( \mathcal { X } , \mathbb { F } )$

## 5.4. Proposition. If X is a normed space, $\mathcal { X } ^ { * }$ is a Banach space.

ProoF. It is left as an exercise for the reader to show that $\mathcal { X } ^ { * }$ is a normed space. To show that $\mathcal { X } ^ { * }$ is complete, let $B = \{ x \in \mathcal { X } : \| x \| \leqslant 1 \}$ $\operatorname { I f } f { \in } { \mathcal { X } } ^ { * }$ , define $\rho ( f ) \colon B \to \mathbb { F }$ by $\rho ( f ) ( x ) = f ( x ) ;$ that is, $\rho ( f )$ is the restriction of f to B. Note that $\rho \colon { \mathcal { X } } ^ { * }   \to   { \mathsf { C } } _ { b } ( B )$ is a linear isometry. Thus to show that $\mathcal { X } ^ { * }$ is complete, it suffices, since $C _ { b } ( B )$ is complete (1.6), to show that $\rho ( \mathcal { X } ^ { * } )$ is closed. Let $\left\{ f _ { n } \right\} \subseteq { \mathcal { X } } ^ { * }$ and suppose $g   \in   \bar { C } _ { b } ( B )$ such that $\| \rho ( f _ { n } ) - g \| \to 0$ as $n   \to   \infty$ . Let $x { \in } { \mathcal { X } }$ . If $\alpha , \beta \in \mathbb { F } , \alpha , \beta \neq 0 ,$ such that αx, $\beta x { \in } B ,$ then $\alpha ^ { - 1 } g ( \alpha x ) =$ lim $\alpha^{-1} f_n(\alpha x) =$ lim $\beta ^ { - 1 } f _ { n } ( \beta x ) = \beta ^ { - 1 } g ( \beta x )$ . Define $f \colon { \mathcal { X } }   \to   \mathbb { F }$ by letting $f(x) = \alpha^{-1} g(\alpha x)$ for any $\alpha \neq 0$ such that $\alpha x { \in } B .$ It is left as an exercise for the reader to show that $f \in \mathcal { X } ^ { * }$ and $\rho ( f )   =   g$ ■

Compare the preceding result with Exercise 2.1.

It should be emphasized that it is not assumed in the preceding proposition that $\mathcal { X }$ is complete. In fact, if $\mathcal { X }$ is a normed space and $\hat { \mathcal { X } }$ is its completion (Exercise 1.16), then $\mathcal { X } ^ { * }$ and $\hat { \mathcal { X } } ^ { * }$ are isometrically isomorphic (Exercise 2.2).

5.5. Theorem. Let $( X , \Omega , \mu )$ be a measure space and let $1 < p < \infty$ . If $1 / p + 1 / q = 1$ and $g   \in   L ^ { q } ( X , \Omega , \mu ) ,$ define $F _ { g } \colon L ^ { p } ( \mu ) \to \mathbb { F } \; b y$

$$
F _ { g } ( f ) = \int f g   d \mu .
$$

Then $F _ { g } \in L ^ { p } ( \mu ) ^ { * }$ and the map $g   \mapsto   F _ { g }$ defines an isometric isomorphism of $L ^ { \pmb { q } } ( \mu )$ onto $L ^ { p } ( \mu ) ^ { * }$

Since this theorem is often proved in courses in measure and integration, the proof of this result, as well as the next two, is contained in the Appendix See Appendix B for the proofs of (5.5) and (5.6).

5.6. Theorem. $I f ( X , \Omega , \mu )$ is a σ-finite measure space and $g { \in } L ^ { \infty } ( X , \Omega , \mu )$ , define $F _ { g } : L ^ { 1 } ( \mu ) \to \mathbb { F } b y$

$$
F _ { g } ( f ) = \int f g   d \mu .
$$

Then $F _ { g }   \in   L ^ { 1 } ( \mu ) ^ { * }$ and the map $g   \mapsto   F _ { g }$ defines an isometric isomorphism of $L ^ { \infty } ( \mu )$ onto $L ^ { 1 ^ { \circ } } ( \mu ) ^ { * }$

Note that when $p = 2$ in Theorem 5.5, there is a little difference between (5.5) and (I.3.5) owing to the absence of a complex conjugate in (5.5). Also, note that (5.6) is false if the measure space is not assumed to be σ-finite (Exercise 3).

If X is a locally compact space, M(X) denotes the space of all F-valued regular Borel measures on X with the total variation norm. See Appendix C for the definitions as well as the proof of the next theorem.

5.7. Riesz Representation Theorem. If X is a locally compact space and $\mu { \in } M ( X ) ,$ , define $F _ { \mu } \colon C _ { 0 } ( X ) \to \mathbb { F } \; b y$

$$
F _ { \mu } ( f ) = \int f d \mu .
$$

Then $F _ { \mu } \in C _ { 0 } ( X ) ^ { * }$ and the map $\mu   \rightarrow   { \cal F } _ { \mu }$ is an isometric isomorphism of $M ( X )$ onto $\dot { C _ { 0 } ( X ) ^ { * } }$

There are special cases of these theorems that deserve to be pointed out.

5.8. Example. The dual of $c _ { 0 }$ is isometrically isomorphic to $l ^ { 1 }$ . In fact, $c _ { 0 } = C _ { 0 } ( \mathbb { N } )$ , if N is given the discrete topology, and $l ^ { 1 } = M ( \mathbb { N } )$

5.9. Example. The dual of $l ^ { 1 }$ is isometrically isomorphic to $l ^ { \infty }$ . In fact, $l ^ { 1 } = L ^ { 1 } ( \mathbb { N } , 2 ^ { \mathbb { N } } , \mu )$ , where $\mu ( \Delta ) = \mathrm { t h e }$ number of points in ∆. Also, $l ^ { \infty } =$ $L ^ { \infty } ( \mathbb { N } , 2 ^ { \mathbb { N } } , \mu )$

5.10. Example. If $1 < p < \infty$ , the dual of $l ^ { p }$ is lª, where $1 = 1 / p + 1 / q .$

What is the dual of $L ^ { \infty } ( X , \Omega , \mu ) ?$ There are two possible representations. One is to identify $L ^ { \infty } ( X , \overline { { \Omega } } , \mu ) ^ { * }$ with the space of finitely additive measures defined on $\mathbf { \Omega }$ that are “absolutely continuous" with respect to $\mu$ and have finite total variation (see Dunford and Schwartz [1958], p. 296). Another representation is to obtain a compact space $Z$ such that $L ^ { \infty } ( X , \Omega , \mu )$ is isometrically isomorphic to $C ( Z )$ and then use the Riesz Representation Theorem. This will be done later in this book (VIII.2.1).

What is the dual of $M ( X ) ?$ For this, define $L ^ { \infty } ( M ( X ) )$ as the set of all F in $\prod \{ L ^ { \infty } ( \mu ) { : }   \mu { \in } M ( X ) \}$ such that if $\mu \ll \mathfrak { v } ,$ then $F ( \mu ) = F ( v )$ a.e. [µ]. This is an inverse limit of the spaces $L ^ { \infty } ( \mu ) , \mu$ in $M ( X )$

5.11. Lemma. If $F { \in } L ^ { \infty } ( M ( X ) )$ , then

$$
\| F \| \equiv \sup_{\mu} \| F(\mu) \|_{\infty} < \infty.
$$

PROOF. If $\| F \| = \infty$ , then there is a sequence $\{ \mu _ { n } \}$ in $M ( X )$ such that $\| F ( \mu _ { n } ) \| _ { \infty } \geqslant n .$ Let $\mu = \sum _ { n = 1 } ^ { \infty } 2 ^ { - n } | \mu _ { n } | / \| \mu _ { n } \|$ . Then $\mu _ { n }   \ll   \mu$ for all n, so $F ( \mu _ { n } ) = F ( \mu )$ a.e. $[ \mu _ { n } ]$ for each n. Hence $\| F ( \mu ) \| _ { \infty } \geqslant \| F ( \mu _ { n } ) \| _ { \infty } \geqslant n$ for each n, a contradiction. ■

5.12. Theorem. If X is locally compact and $F { \in } L ^ { \infty } ( M ( X ) )$ , define $\Phi _ { F } : M ( X ) \to \mathbb { F }$ by

$$
\Phi _ { F } ( \mu ) = \int _ { } F ( \mu )   d \mu .
$$

Then $\Phi _ { F } { \in } M ( X ) ^ { * }$ and the map $F { \mapsto } \Phi _ { F }$ is an isometric isomorphism of $L ^ { \infty } ( M ( X ) )$ onto $M ( X ) ^ { * }$

ProOF. It is easy to see that $\Phi _ { F }$ is linear. Also, $| \Phi _ { F } ( \mu ) | \leqslant \int | F ( \mu ) | d | \mu | \leqslant$ $\left\| F ( \mu ) \right\| _ { \infty } \left\| \mu \right\| \leqslant \left\| F \right\| \left\| \mu \right\|$ . Thus $\Phi _ { F } { \in } M ( X ) ^ { * }$ and $\| \Phi _ { F } \| \leqslant \| F \|$

Now fix Φ in $M(X)^*. \mathrm{If} \mu \in M(X)$ and $f { \in } L ^ { 1 } ( | \mu | )$ , then $y = f \mu \in M(X)$ . (That is, $v ( \Delta ) = \int _ { \Delta } f   d \mu$ for every Borel set $\Delta )$ Also $\| v \| = \int | f | d | \mu |$ In fact, the

Radon-Nikodym Theorem can be interpreted as an identification (isometrically isomorphic) of $L ^ { 1 } ( | \mu | )$ with $\{ \eta \in M ( X ) : \eta \ll | \mu | \}$ . Thus $f { \mapsto } \Phi ( f \mu )$ is a linear functional on $L ^ { 1 } ( | \mu | )$ and $| \Phi ( \dot { f } \mu ) | \leqslant \| \Phi \| \int | f | d | \mu |$ . Hence there is an $F ( \mu )$ in $L ^ { \infty } ( | \mu | )$ such that $\Phi ( f \mu ) = \int f F ( \mu )   d \mu$ for every f in $L ^ { 1 } ( | \mu | )$ and $\left\| F ( \mu ) \right\| _ { \infty } \leqslant \left\| \boldsymbol { \Phi } \right\|$ . (We have been a little nonchalant about using $\mu$ or $| \mu |$ , but what was said is perfectly correct. Fill in the details.) In particular, taking $f = 1$ gives $\Phi ( \mu ) = \int F ( \mu )   d \mu$ . It must be shown that $F { \in } L ^ { \infty } ( M ( X ) ) ;$ it then follows that $\Phi = \Phi _ { F }$ and $\| \boldsymbol { \Phi } _ { \boldsymbol { F } } \| \geqslant \| \boldsymbol { F } \| _ { \infty }$

To show that $F { \in } L ^ { \infty } ( M ( X ) )$ , let μ and v be measures such that $\pmb { v } \ll \pmb { \mu } .$ By the Radon-Nikodym Theorem, there is an $f$ in $L ^ { 1 } ( | \mu | )$ such that $v = f \mu .$ Hence if $g { \in } L ^ { 1 } ( | \nu | )$ , then $g f   \in   L ^ { 1 } ( | \mu | )$ and $\int g   d v = \int g f   d \mu .$ Thus, $\int gF(v)dv = \Phi(gv) = \Phi(gf\mu) = \int gfF(\mu)d\mu = \int gF(\mu)dv$ . So $F ( v ) = F ( \mu )$ a.e. [v] and $F { \in } L ^ { \infty } ( M ( X ) )$ ■

## EXERCISES

1. Complete the proof of Proposition 5.4.

2. Show that $\mathcal { X } ^ { * }$ is a normed space.

3. Give an example of a measure space $( X , \Omega , \mu )$ that is not σ-finite for which the conclusion of Theorem 5.6 is false.

4. Let $\{ \mathcal { X } _ { i } \colon i { \in } I \}$ be a collection of normed spaces. If $1 \leqslant p < \infty$ , show that the dual space of $\oplus _ { p } \mathcal { X } _ { i }$ is isometrically isomorphic to $\oplus _ { \pmb { q } } \mathcal { X } _ { i } ^ { \ast }$ , where $1 / p + 1 / q = 1$

5. If $\mathcal { X } _ { 1 } , \mathcal { X } _ { 2 } , \ldots$ are normed spaces, show that $( \oplus _ { 0 } \mathcal { X } _ { n } ) ^ { * }$ is isometrically isomorphic to $\oplus _ { 1 } \mathcal { X } _ { n } ^ { * }$

6. Let $n \geqslant 1$ and let $C ^ { ( n ) } [ 0 , 1 ]$ be defined as in Example 1.10. Show that $\| f \| =$ $\sum_{k = 0}^{n - 1}|f^{(k)}(0)| + \sup\{|f^{(n)}(x)|:0 \leq x \leq 1\}$ is an equivalent norm on $C ^ { ( n ) } [ 0 , 1 ]$ . Show that $L \in (C^{(n)}[0,1])^*$ if and only if there are scalars $\alpha _ { 0 } , \alpha _ { 1 } , \ldots , \alpha _ { n - 1 }$ and a measure μon $[ 0 , 1 ]$ such that $L(f) = \sum_{k = 0}^{n - 1} \alpha_{k} f^{(k)}(0) + \int f^{(n)}   d\mu$ . If $C ^ { ( n ) } [ 0 , 1 ]$ is given this new norm, find a formula for $\| L \|$ in terms of $| \alpha _ { 0 } | , | \alpha _ { 1 } | , \ldots , | \alpha _ { n - 1 } | ,$ and $\| \mu \| ?$

7. Give $\mathcal { X } = C ( [ 0 , 1 ] )$ the norm $\| f \| = \int | f ( t ) |$ dt and define $L \colon { \mathcal { X } }   \to   F$ by $\begin{array} { r } { L ( f )   =   f ( \frac { 1 } { 2 } ) } \end{array}$ Show directly (without using Theorem 5.6) that L is not bounded. Now prove this as a consequence of (5.6).

## §6. The Hahn-Banach Theorem

The Hahn-Banach Theorem is one of the most important results in mathematics. It is used so often it is rightly considered as a cornerstone of functional analysis. It is one of those theorems that when it or one of its immediate consequences is used, it is used without quotation or reference and the reader is assumed to realize that it is being invoked.

6.1. Definition. If $\mathcal { X }$ is a vector space, a sublinear functional is a function

q: $\mathcal { X }   \to   \mathbb { R }$ such that

(a) $q(x + y) \leqslant q(x) + q(y)$ for all $x , y$ in $\mathcal { X } ;$

(b) $q ( \alpha x ) = \alpha q ( x )$ for x in $\mathcal { X }$ and $\alpha \geqslant 0 .$

Note that every seminorm is a sublinear functional, but not conversely. In fact, it should be emphasized that a sublinear functional is allowed to assume negative values and that (b) in the definition only holds for $\alpha \geqslant 0$

6.2. The Hahn-Banach Theorem. Let X be a vector space over IR and let q be a sublinear functional on $\mathcal { X }$ If M is a linear manifold in $\mathcal { X }$ and $f \colon { \mathcal { M } } \to \mathbb { R }$ is a linear functional such that $f(x) \leqslant q(x)$ for all x in $\mathcal { M } ,$ then there is a linear functional $F \colon { \mathcal { X } }   \to   \mathbb { R }$ such that $F | \mathcal { M } = f$ and $F(x) \leqslant q(x)$ for all x in $\mathcal { X }$

Note that the substance of the theorem is not that the extension exists but that an extension can be found that remains dominated by q. Just to find an extension, let $\{ e _ { i } \}$ be a Hamel basis for $\mathcal { M }$ and let $\{ y _ { j } \}$ be vectors in $\mathcal { X }$ such that $\{ e _ { i } \} \cup \{ \dot { y } _ { j } \}$ is a Hamel basis for $\mathcal { X } .$ Now define $F \colon { \mathcal { X } }   \to   \mathbb { R }$ by $F ( \sum _ { i } \alpha _ { i } e _ { i } + \sum _ { j } \beta _ { j } y _ { j } ) = \sum _ { i } \alpha _ { i } f ( e _ { i } ) = f ( \sum _ { i } \alpha _ { i } e _ { i } ) .$ This extends $f .$ If $\{ \gamma _ { j } \}$ is any collection of real numbers, then $\begin{array} { r } { F ( \sum _ { i } \alpha _ { i } e _ { i } + \sum _ { j } \beta _ { j } y _ { j } ) = f ( \sum _ { i } \alpha _ { i } e _ { i } ) + \sum _ { j } \beta _ { j } \gamma _ { j } } \end{array}$ is also an extension of $f .$ Moreover, any extension of $f$ has this form. The difficulty is that we must find one of these extensions that is dominated by q.

Before proving the theorem, let's see some of its immediate corollaries. The first is an extension of the theorem to complex spaces. For this a lemma is needed. Note that if ¿ is a vector space over C, it is also a vector space over R. Also, if $f \colon { \mathcal { X } }   \to   \mathbb { C }$ is $\mathbf { C } \mathbf { - } \mathrm { l i n e a r } ,$ then Re $f \colon { \mathcal { X } }   \to   \mathbb { R }$ is R-linear. The following lemma is the converse of this.

6.3. Lemma. Let X be a vector space over $\mathbf { C } .$

(a) $I f f \colon { \mathcal { X } }   \to   \mathbb { R }$ is an R-linear functional, then $\tilde { f } ( x ) = f ( x ) - i f ( i x )$ is a C-linear functional and $f = \operatorname { R e } { \tilde { f } } .$

(b) If $g \colon { \mathcal { X } }   \to   \mathbb { C }$ is C-linear, $f = \operatorname { R e } g ,$ and $\widetilde { f }$ is defined as in (a), then $\tilde { f }   =   g$ (c) If p is a seminorm on X and f and $\widetilde { f }$ are as in (a), then $| f ( x ) | \leqslant p ( x )$ for all x if and only $\begin{array} { r } { i f \; | \widetilde { f } ( x ) | \leqslant p ( x ) } \end{array}$ for all x.

(d) If X is a normed space and f and $\tilde { f }$ are as in (a), then $\| f \| = \| { \tilde { f } } \|$

ProoF. The proofs of (a) and (b) are left as an exercise. To prove (c), suppose $| \widetilde { f } ( x ) | \leqslant p ( x )$ . Then $f(x) = \mathrm{Re} \tilde{f}(x) \leqslant |\tilde{f}(x)| \leqslant p(x)$ Also, $-f(x)=\operatorname{Re}\tilde{f}(-x)\leqslant$ $| \widetilde{f} ( - x ) | \leqslant p ( x )$ . Hence $| f ( x ) | \leqslant p ( x )$ .Now assume that $| f ( x ) | \leqslant p ( x )$ Choose θ such that $\tilde { f } ( x ) = e ^ { i \theta } | \tilde { f } ( x ) |$ . Hence $| \tilde { f } ( x ) | = \tilde { f } ( e ^ { - i \theta } x ) = \operatorname { R e } \tilde { f } ( e ^ { - i \theta } x ) = f ( e ^ { - i \theta } x ) \leqslant$ $p ( e ^ { - i \theta } x ) = p ( x ) .$

Part (d) is an easy application of (c).

6.4. Corollary. Let $\mathcal { X }$ be a vector space, let $\mathcal { M }$ be a linear manifold in $\mathcal { X }$ , and let $p \colon { \mathcal { X } }   \to   [ 0 , \infty )$ be a seminorm. $I f   f \colon { \mathcal { M } }   \to   \mathbb { F }$ is a linear functional such that $| f ( x ) | \leqslant p ( x )$ for all x in M, then there is a linear functional $F \colon { \mathcal { X } }   \to   \mathbb { F }$ such that $F | \mathcal { M } = f$ and $| F ( x ) | \leqslant p ( x )$ for all x in X.

PROOF. Case 1: $\mathbf { F }   =   \mathbf { R }$ . Note that $f(x) \leqslant |f(x)| \leqslant p(x)$ for x in M. By (6.2) there is an extension $F \colon { \mathcal { X } }   \to   \mathbb { R }$ of f such that $F(x) \leqslant p(x)$ for all x. Hence $- F(x) = F( - x) \leqslant p( - x) = p(x)$ Thus $| F | \leqslant p .$

$Case 2: \mathbb{F} = \mathbb{C}.$ Let $f _ { 1 } = \operatorname { R e } f .$ By (6.3c), $| f _ { 1 } | \leqslant p .$ By Case 1, there is an R-linear functional $\boldsymbol { F } _ { 1 } \colon \mathcal { X } \to \mathbb { R }$ such that $\boldsymbol { F } _ { 1 } | \mathcal { M } = \boldsymbol { f } _ { 1 }$ and $| F _ { 1 } | \leqslant p .$ Let $F ( x ) = F _ { 1 } ( x ) - i F _ { 1 } ( i x )$ for all x in $\mathcal { X } .$ By (6.3c), $| F | \leqslant p .$ Clearly, $F | { \mathcal { M } } = f .$

6.5. Corollary. If X is a normed space, M is a linear manifold in $\mathcal { X }$ and $f \colon { \mathcal { M } } \to \mathbb { F }$ is a bounded linear functional, then there is an F in $\mathcal { X } ^ { * }$ such that $F | { \mathcal { M } } = f$ and $\| F \| = \| f \|$

PRooF. Use Corollary 6.4 with $p ( x ) = \| f \| \| x \|$

6.6. Corollary. $I f \mathcal { X }$ is a normed space, $\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { d } \}$ is a linearly independent subset of $\mathcal { X } ,$ and $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { d }$ are arbitrary scalars, then there is an f in $\mathcal { X } ^ { * }$ such that $f ( x _ { j } ) = \alpha _ { j } \; \mathit { f o r } \; 1 \leqslant j \leqslant d .$

PROOF. Let $\mathcal { M } = \mathrm { t h e }$ linear span of $x _ { 1 } , \ldots , x _ { d }$ and define $g \colon { \mathcal { M } } \to \mathbb { F }$ by $\begin{array} { r } { g ( \sum _ { j }   \beta _ { j } x _ { j } )   =   \sum _ { j }   \beta _ { j } \alpha _ { j } } \end{array}$ . So $g$ is linear. Since $\mathcal { M }$ is finite dimensional, $g$ is continuous. Let f be a continuous extension of $g$ to $\mathcal { X }$

6.7. Corollary. If X is a normed space and $x { \in } { \mathcal { X } }$ , then

$$
\| x \| = \sup \{ | f ( x ) | : f \in \mathcal { X } ^ { * } \text { and } \| f \| \leqslant 1 \}.
$$

Moreover, this supremum is attained.

PROOF. Let $\alpha = \sup \left\{ \left| f(x) \right| : f \in \mathcal{X}^* \right\}$ and $\| f \| \leqslant 1 \}$ . If $f { \in } { \mathcal { X } } ^ { * }$ and $\| f \| \leqslant 1$ , then $| f ( x ) | \leqslant \| f \| \| x \| \leqslant \| x \| ;$ hence $\alpha \leqslant \| x \|$ . Now let $\mathcal { M } = \left\{ \beta x \mathbf { : } \beta \mathbf { \in } \mathbf { F } \right\}$ define $g \colon \mathcal { M } \to \mathbb { F } \mathrm { b y } g ( \beta x ) = \beta \| x \|$ . Then $g \in \mathcal { M } ^ { * }$ and $\| g \| = 1$ . By Corollary 6.5, there is an f in $\mathcal { X } ^ { * }$ such that $\| f \| = 1$ and $f ( x ) = g ( x ) = \| x \|$ ■

This introduces a certain symmetry in the definitions of the norms in $\mathcal { X }$ and $\mathcal { X } ^ { * }$ that will be explored later (§11).

6.8. Corollary. If X is a normed space, $\mathcal { M } \leqslant \mathcal { X } , x _ { 0 } \in \mathcal { X } \backslash \mathcal { M }$ , and $d = \mathrm { d i s t } ( x _ { 0 } , \mathcal { M } ) ,$ then there is an f in $\mathcal { X } ^ { * }$ such that $f(x_0) = 1, \; f(x) = 0$ for all x in M, and $\| f \| = d ^ { - 1 }$

PROOF. Let $Q \colon { \mathcal { X } }   \to   { \mathcal { X } } / { \mathcal { M } }$ be the natural map. Since $\| x _ { 0 } + { \mathcal { M } } \| = d ,$ by the preceding corollary there is a g in $( \mathcal { X } / \mathcal { M } ) ^ { * }$ such that $g ( x _ { 0 } + \mathcal { M } ) = d$ and $\| g \| = 1$ . Let $f = d^{-1} g \circ Q : \mathcal{X} \to \mathbb{F}.$ Then f is continuous, $f ( x ) = 0$ for x in $\mathcal { M } ,$ and $f(x_{0}) = 1.\ \mathrm{Also},\ |f(x)| = d^{-1} \left| g(Q(x)) \right| \leqslant d^{-1} \left\| Q(x) \right\| \leqslant d^{-1} \left\| x \right\|.$ hence二 $\| f \| \leqslant d ^ { -   1 }$ . On the other hand, $\| g \| = 1$ so there is a sequence $\{ x _ { n } \}$ such that $| g ( x _ { n } + \mathcal { M } ) | \to 1$ and $\| x _ { n } + \mathcal { M } \| < 1$ for all n. Let $y _ { n } \in \mathcal { M }$ such that $\| x _ { n } + y _ { n } \| < 1$ . Then $| f ( x _ { n } + y _ { n } ) | = d ^ { - 1 } | g ( x _ { n } + \mathcal { M } ) | \rightarrow d ^ { - 1 }$ , so $\| f \| = d ^ { - 1 }$ ■

To prove the Hahn-Banach Theorem, we first show that we can extend the functional to a space of one dimension more.

6.9. Lemma. Suppose the hypothesis of (6.2) is satisfied and, in addition, dim $\mathcal { X } / \mathcal { M } = 1$ . Then the conclusion of (6.2) is valid.

PROOF. Fix $x _ { 0 }$ in $x < \pi ;$ so $\mathcal { X } = \mathcal { M } \vee \{ x _ { 0 } \} = \{ t x _ { 0 } + y : t { \in } \mathbb { R } , y { \in } \mathcal { M } \}$ . For the moment assume that the extension $F \colon { \mathcal { X } }   \to   \mathbb { R }$ of $f$ exists with $F \leqslant q$ Let's see what F must look like. Put $\alpha _ { 0 } = F ( x _ { 0 } )$ . If $t   >   0$ and $y _ { 1 } \in \mathcal { M } ,$ then $F(tx_{0}+y_{1})=t\alpha_{0}+f(y_{1})\leqslant q(tx_{0}+y_{1})$ Hence $\alpha _ { 0 } \leqslant - t ^ { - 1 } f ( y _ { 1 } ) +$ $t^{-1}q(tx_{0}+y_{1})=-f(y_{1}/t)+q(x_{0}+y_{1}/t)$ for every $y _ { 1 }$ in $\mathcal { M }$ Since $y _ { 1 } / t \in \mathcal { M }$ this gives that.

$$
\alpha_{0} \leqslant - f(y_{1}) + q(x_{0} + y_{1})\tag{6.10}
$$

for all $y _ { 1 }$ in $\mathcal { M } .$ Also note that if $\alpha _ { 0 }$ satisfies (6.10), then by reversing the preceding argument, it follows that $t \alpha _ { 0 } + f ( y _ { 1 } ) \leqslant q ( t x _ { 0 } + y _ { 1 } )$ whenever $t   \geqslant   0$

If $t \geqslant 0$ and $y _ { 2 } \in \mathcal { M }$ and if F exists, then $F(-tx_{0}+y_{2})=-tx_{0}+f(y_{2})\leqslant$ $q ( - t x _ { 0 } + y _ { 2 } )$ . As above, this implies that

$$
\alpha_{0} \geqslant f(y_{2}) - q(-x_{0} + y_{2})\tag{6.11}
$$

for all $y _ { 2 }$ in $\mathcal { M }$ Moreover, (6.11) is sufficient that $- t \alpha _ { 0 } + f ( y _ { 2 } ) \leqslant q ( - t x _ { 0 } + y _ { 2 } )$ for all $t \geqslant   0$ and $y _ { 2 }$ in $\mathcal { M } ,$

Combining (6.10) and (6.11) we see that we must show that $\alpha _ { 0 }$ can be chosen satisfying (6.10) and (6.11) simultaneously. Thus we must show that

$$
f(y_{2}) - q(-x_{0} + y_{2}) \leqslant - f(y_{1}) + q(x_{0} + y_{1})\tag{6.12}
$$

for all $y _ { 1 } , y _ { 2 }$ in $\mathcal { M }$ But this means we want to show that $f(y_{1} + y_{2}) \leqslant$ $q(x_{0}+y_{1})+q(-x_{0}+y_{2})$ . But

$$
\begin{aligned}f(y_{1} + y_{2}) & \leqslant q(y_{1} + y_{2}) = q((y_{1} + x_{0}) + (-x_{0} + y_{2})) \\& \leqslant q(y_{1} + x_{0}) + q(-x_{0} + y_{2}),\end{aligned}
$$

so (6.12) is satisfied. If $\alpha _ { 0 }$ is chosen with sup $\left\{ f(y_{2}) - q(-x_{0} + y_{2}) : y_{2} \in \mathcal{M} \right\} \leqslant$ $\alpha _ { 0 } \leqslant \inf \left\{ - f ( y _ { 1 } ) + q ( x _ { 0 } + y _ { 1 } ) : y _ { 1 } \in \mathcal { M } \right\}$ and $F(tx_{0}+y)\equiv t\alpha_{0}+f(y_{1}),$ F satisfies the conclusion of (6.2).

PROOF OF THE HAHN-BANACH THEOREM. Let $\mathcal { S }$ be the collection of all pairs $( \mathcal { M } _ { 1 } , f _ { 1 } ) ,$ where $\mathcal { M } _ { 1 }$ is a linear manifold in $\mathcal { X }$ such that $\mu _ { 1 } = \mu$ and $f _ { 1 } \colon \mathcal { M } _ { 1 } \to \mathbb { R }$ is a linear functional with $f _ { 1 } | \mathcal { M } = f$ and $f _ { 1 } \leqslant q$ on $\mathcal { M } _ { 1 } . \operatorname { I f } \left( \mathcal { M } _ { 1 } , f _ { 1 } \right)$ and $( \mathcal { M } _ { 2 } , f _ { 2 } ) \in \mathcal { S }$ define $( \mathcal { M } _ { 1 } , f _ { 1 } )   \lesssim   ( \mathcal { M } _ { 2 } , f _ { 2 } )$ to mean that $\mathcal { M } _ { 1 } \subseteq \mathcal { M } _ { 2 }$ and $f_{2} \mid \mathcal{M}_{1} = f_{1}. \mathrm{So} (\mathcal{S}, \lesssim)$ is a partially ordered set. Suppose $\mathcal { C } = \{ ( \mathcal { M } _ { i } , f _ { i } ) : i { \in } I \}$ is a chain in $\mathcal { S }$ If $\mathcal { N } \equiv \cup \left\{ \mathcal { M } _ { i } \colon i { \in } I \right\}$ , then the fact that € is a chain implies that $\mathcal { N }$ is a linear manifold. Define $F \colon { \mathcal { N } } \to \mathbb { R }$ by setting $F(x) = f_i(x)   if   x \in \mathcal{M}_i$

It is easily checked that F is well defined, linear, and satisfies $F \leqslant q$ on $\mathcal { N }$ So $( \mathcal { N } , F ) { \in } { \mathcal { P } }$ and $( \mathcal { N } , F )$ is an upper bound for ${ \mathcal { C } } .$ By Zorn's Lemma, $\mathcal { S }$ has a maximal element $( \mathcal { Y } , F )$ . But the preceding lemma implies that $\mathcal { Y } = \mathcal { X }$ Hence F is the desired extension.

This section concludes with one important consequence of the Hahn-Banach Theorem. It will be generalized later (IV.3.11), but it is used so often it is worth singling out for consideration.

## 6.13. Theorem. If X is a normed space and M is a linear manifold in $\mathcal { X } ,$ then

$$
\mathrm{cl} \mathcal{M} = \cap \{ \ker f : f \in \mathcal{X}^*   and   \mathcal{M} \subseteq \ker f \}.
$$

PROOF. Let $\mathcal { N } = \cap \{ \ker f \colon f { \in } \mathcal { X } ^ { \star }$ and ${ \mathcal { M } } \subseteq \ker f \}$ . If $f \in \mathcal { X } ^ { * }$ and ${ \mathcal { M } } \subseteq \ker f ,$ then the continuity of f implies that cl ${ \mathcal { M } } \subseteq \ker f .$ Hence cl $\mathcal { M } \subseteq \mathcal { N }$ . If $x _ { 0 } \notin \operatorname { c l } \mathcal { M }$ then $d = \mathrm{dist}(x_0, \mathcal{M}) > 0.$ By Corollary 6.8 there is an f in $\mathcal { X } ^ { * }$ such that $f ( x _ { 0 } )   =   1$ and $f ( x ) = 0$ for every x in M. Hence $x _ { 0 } \not \in \mathcal { N }$ . Thus $\mathcal { N } \subseteq \mathrm { c l } \mathcal { M }$ and the proof is complete. ■

6.14. Corollary. If X is a normed space and M is a linear manifold in $\mathcal { X } ,$ then M is dense in X if and only if the only bounded linear functional on X that annihilates M is the zero functional.

## EXERCISES

1. Complete the proof of Lemma 6.3.

2. Give the details of the proof of Corollary 6.5.

3. Show that $c ^ { * }$ is isometrically isomorphic to $l ^ { 1 }$ . Are c and $c _ { 0 }$ isometrically isomorphic?

4. $\mathbf { H } \mu$ is a Borel measure on [0, 1] and $\int x ^ { n }   d \mu ( x ) = 0$ for all $n \geqslant 0 .$ , show that $\mu   =   0$

5. If $n \geqslant 1$ , show that there is a measure $\mu$ on [0, 1] such that for every polynomial p of degree at most n,

$$
\int p   d \mu = \sum _ { k = 1 } ^ { n } p ^ { ( k ) } ( k / n ) .
$$

6. If $n \geqslant 1$ , does there exist a measure $\mu$ on [0, 1] such that $p ^ { \prime } ( 0 ) = \int p   d \mu$ for every polynomial of degree at most $n ?$

7. Does there exist a measure $\mu$ on [0,1] such that $\int p   d \mu = p ^ { \prime } ( 0 )$ for every polynomial $p !$

8. Let K be a compact subset of C and define $A ( K )$ to be $\{ f \in C ( K ) : f$ is analytic on int $| K \}$ . (Functions here are complex valued.) Show that if a∈K, then there is a probability measure μ supported on ∂K such that $f ( a ) = \int f   d \mu$ for every f in $A ( K )$ . (A probability measure is a nonnegative measure $\mu$ such that $\| \boldsymbol { \mu } \| = 1 . )$

9. If $K = \mathrm { c l }   \mathbb { D } ( \mathbb { D } = \{ | z | < 1 \} )$ and $a { \in } K$ , find the measure $\mu$ whose existence was proved in Exercise 8.