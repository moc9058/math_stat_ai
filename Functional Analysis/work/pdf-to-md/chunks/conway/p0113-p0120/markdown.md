9. If (S, d) is a metric space and $\mathcal { X }$ is a normed space, say that a function $f \colon S   \to   { \mathcal { X } }$ is a Lipschitz function if there is a constant $M > 0$ such that $\| f(s) - f(t) \| \leq M d(s,t)$ for all s,t in S. Show that if $f \colon  { \mathcal { S } }   \to    { \mathcal { X } }$ is a function such that for all L in $\mathcal { X } ^ { * }$ $L \circ f \colon \mathbb { S } \to \mathbb { F }$ is Lipschitz, then $f \colon S   \to   { \mathcal { X } }$ is a Lipschitz function.

10. Let ¿ be a Banach space and suppose $\{ x _ { n } \}$ is a sequence in X such that for each x in $\mathcal { X }$ there are unique scalars $\{ \alpha _ { n } \}$ such that $\lim_{n \to \infty} \| x - \sum_{k=1}^n \alpha_k x_k \| = 0$ Such a sequence is called a Schauder basis. (a) Prove that $\mathcal { X }$ is separable. (b) Let $\mathcal { Y } = \{ \{ \alpha _ { n } \} \in \mathbb { F } ^ { \mathbb { N } } : \sum _ { n = 1 } ^ { \infty } \alpha _ { n } x _ { n }$ converges in $| \mathcal { X } \rangle$ and for $y = \{ \alpha _ { n } \}$ in $\pmb { g }$ define $\| y \| = \sup_{n} \| \sum_{k=1}^{n} \alpha_{k} x_{k} \|$ . Show that Y is a Banach space. (c) Show that there is a bounded bijection $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ (d) If $n \geqslant 1$ and $f _ { n } \colon { \mathcal { X } }   \to   \mathbb { F }$ is defined by $f_{n}(\sum_{k = 1}^{\infty} \alpha_{k}x_{k}) = \alpha_{n}.$ , show that $f _ { n } \in \mathcal { X } ^ { * }$ . (e) Show that $x _ { n } \phi$ the closed linear span of $\{ x _ { k } : k \neq n \}$

# CHAPTER IV Locally Convex Spaces

A topological vector space is a generalization of the concept of a Banach space. The locally convex spaces are encountered repeatedly when discussing weak topologies on a Banach space, sets of operators on Hilbert space, or the theory of distributions. This book will only skim the surface of this theory, but it will treat locally convex spaces in sufficient detail as to enable the reader to understand the use of these spaces in the three areas of analysis just mentioned. For more details on this theory, see Bourbaki [1967], Robertson and Robertson [1966], or Schaefer [1971].

## §1. Elementary Properties and Examples

A topological vector space is a vector space that is also a topological space such that the linear structure and the topological structure are vitally connected.

1.1. Definition. A topological vector space (TVS) is a vector space $\mathcal { X }$ together with a topology such that with respect to this topology

(a) the map of $\mathcal { X } \times \mathcal { X }   \rightarrow   \mathcal { X }$ defined by $( x , y ) { \mapsto }   x + y$ is continuous;

(b) the map of $\mathbb { F } \times \mathcal { X }   \rightarrow   \mathcal { X }$ defined by $( \alpha , x ) { \mapsto } \alpha x$ is continuous.

It is easy to see that a normed space is a TVS (Proposition III.1.3).

Suppose $\mathcal { X }$ is a vector space and $\mathcal { P }$ is a family of seminorms on $\mathcal { X }$ Let $\mathcal { T }$ be the topology on $\mathcal { I }$ that has as a subbase the sets $\left\{ x : p ( x - x _ { 0 } ) < \varepsilon \right\}$ where $$p { \in } { \mathcal { P } } , \: x _ { 0 } { \in } { \mathcal { X } }$$ , and $\varepsilon   >   0$ Thus a subset $U$ of $\mathcal { X }$ is open if and only if for every $x _ { 0 }$ in $U$ there are $p _ { 1 } , \ldots , p _ { n }$ in $\mathcal { P }$ and $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }   >   0$ such that $\bigcap_{j = 1}^{n} \left\{ x \in \mathcal{X} : p_{j}(x - x_{0}) < \varepsilon_{j} \right\} \subseteq U$ . It is not difficult to show that $\mathcal { X }$ with this topology is a TVS (Exercise 2)

1.2. Definition. A locally convex space (LCS) is a TVS whose topology is defined by a family of seminorms $\mathcal { P }$ such that $\bigcap_{p \in \mathcal{P}} \{x: p(x) = 0\} = (0)$

The attitude that has been adopted in this book is that all topological spaces are Hausdorff. The condition in Definition 1.2 that $\bigcap_{p \in \mathcal{P}} \{ x: p(x) =$ $0 \} = ( 0 )$ is imposed precisely so that the topology defined by $\mathcal { P }$ be Hausdorff. In fact, suppose that $x \neq y .$ Then there is a p in $\mathcal { P }$ such that $p(x - y) \neq 0;$ let $p(x - y) > \varepsilon > 0$ If $U = \{ z : p ( x - z ) < \frac { 1 } { 2 } \varepsilon \}$ and $V = \{ z : p ( y - z ) < \frac { 1 } { 2 } \varepsilon \}$ , then $U \cap V = \square$ and U and V are neighborhoods of x and y, respectively.

If X is a TVS and $x _ { 0 } { \in } { \mathcal { X } }$ , then $x   \mapsto   x + x _ { 0 }$ is a homeomorphism of $\mathcal { X }$ ; also, if $\alpha { \in } \mathbb { F }$ and $\alpha \neq 0,   x \mapsto \alpha x$ is a homeomorphism of $\mathcal { X }$ (Exercise 4). Thus the topology of $\mathcal { X }$ looks the same at any point. This might make the next statement less surprising.

1.3. Proposition. Let X be a TVS and let p be a seminorm on $\mathcal { X }$ . The following statements are equivalent.

(a) p is continuous

(b) $\{ x \in \mathcal { X } : p ( x ) < 1 \}$ is open.

(c) $0 \in \mathrm{int} \left\{ x \in \mathcal{X} : p(x) < 1 \right\}$

(d) $0 \in \mathrm{int} \left\{ x \in \mathcal{X} : p(x) \leq 1 \right\}$

(e) p is continuous at 0.

(f) There is a continuous seminorm q on $\mathcal { X }$ such that $p \leqslant q .$

PROOF. It is clear that $( \mathrm { a } )   \Rightarrow   ( \mathrm { b } )   \Rightarrow   ( \mathrm { c } )   \Rightarrow   ( \mathrm { d } ) .$

(d) implies (e): Clearly (d) implies that for every $\varepsilon > 0 , 0 \in \mathrm { i n t } \left\{ x \in \mathcal { X } : p ( x ) \leq \varepsilon \right\}$ so if $\left\{ x _ { i } \right\}$ is a net in $\mathcal { X }$ that converges to 0 and $\varepsilon   >   0 ,$ there is an $i _ { 0 }$ such that $x_{i} \in \left\{ x: p(x) \leq \varepsilon \right\}$ for $i \geqslant i _ { 0 } ;$ that is, $p ( x _ { i } ) \leqslant \varepsilon$ for $i \geqslant i _ { 0 }$ . So p is continuous at 0.

(e) implies (a): If $x _ { i }   \to   x _ { i }$ then $| p ( x ) - p ( x _ { i } ) | \leqslant p ( x - x _ { i } )$ Since $x - x _ { i }   \to   0 ,$ (e) implies that $p ( x - x _ { i } )   \rightarrow   0$ Hence $p ( x _ { i } )   \to   p ( x ) .$

Clearly (a) implies (f). So it remains to show that (f) implies (e). If $x _ { i }   \to   0$ in $\mathcal { X }$ , then $q ( x _ { i } )   \to   0 .$ But $0 \leqslant p(x_{i}) \leqslant q(x_{i}),$ sO $p ( x _ { i } )   \to   0 .$

1.4. Proposition. If X is a TVS and $p _ { 1 } , \ldots , p _ { n }$ are continuous seminorms, then $p _ { 1 } + \cdots + p _ { n }$ and $\operatorname* { m a x } _ { i } ( p _ { i } ( x ) )$ are continuous seminorms. $I f \; \{ p _ { i } \}$ is a family of continuous seminorms such that there is a continuous seminorm q with $p _ { i }   \leqslant   q$ for all i, then $x   \mapsto   \operatorname* { s u p } _ { i } \{ p _ { i } ( x ) \}$ defines a continuous seminorm.

PROOF. Exercise.

If $\mathcal { P }$ is a family of seminorms of $\mathcal { X }$ that makes $\mathcal { X }$ into a LCS, it is often convenient to enlarge $\mathcal { P }$ by assuming that $\mathcal { P }$ is closed under the formation of finite sums and supremums of bounded families [as in (1.4)]. Sometimes it is convenient to assume that $\mathcal { P }$ consists of all continuous seminorms. In either case the resulting topology on $\mathcal { X }$ remains unchanged.

1.5. Example. Let X be completely regular and let $C ( X ) = \mathrm { a l l }$ continuous functions from X into F. If K is a compact subset of X, define $p _ { K } ( f ) = \operatorname* { s u p } \{ | f ( x ) | : x \in K \}$ . Then $\left\{ p _ { \kappa } ; K \right.$ compact in $X \}$ is a family of semi-norms that makes C(X) into a LCS.

1.6. Example. Let G be an open subset of C and let $H ( G )$ be the subset of $C _ { \mathfrak { C } } ( G )$ consisting of all analytic functions on G. Define the seminorms of (1.5) on $H ( G )$ Then $H ( G )$ is a LCS. Also, the topology defined on $H ( G )$ by these seminorms is the topology of uniform convergence on compact subsets—the usual topology for discussing analytic functions.

1.7. Example. Let $\mathcal { X }$ be a normed space. For each $x ^ { * }$ in $\mathcal { X } ^ { * }$ define $p _ { x ^ { * } } ( x ) = | x ^ { * } ( x ) |$ . Then $p _ { x ^ { * } }$ is a seminorm and if $\mathcal { P }   =   \left\{ p _ { x ^ { * } } \colon x ^ { * } { \in } \mathcal { X } ^ { * } \right\}$ $\mathcal { P }$ makes X into a LCS. The topology defined on $\mathcal { X }$ by these seminorms is called the weak topology and is often denoted by $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } )$

1.8. Example. Let $\mathcal { X }$ be a normed space and for each x in $\mathcal { X }$ define $p _ { x } \colon { \mathcal { X } } ^ { * } \to$ $[ 0 , \infty )$ by $p _ { x } ( x ^ { * } ) = | x ^ { * } ( x ) |$ . Then $p _ { x }$ is a seminorm and $\mathcal { P } = \{ p _ { x } ; x { \in } \mathcal { X } \}$ makes $\mathcal { X } ^ { * }$ into a LCS. The topology defined by these seminorms is called the weak-star (or weak\* or $\mathbf { w k ^ { * } } )$ topology on $\mathcal { X } ^ { * }$ . It is often denoted by $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } )$

The spaces $\mathcal { X }$ with its weak topology and $\mathcal { X } ^ { * }$ with its wea ${ \bf k } ^ { * }$ topology are very important and will be explored in depth in Chapter V.

Recall the definition of convex set from (I.2.4). If $a , b   \in   \mathcal { X }$ , then the line segment from $a$ to $b$ is defined as $[ a , b ] \equiv \{ t b + ( 1 - t ) a \colon 0 \leqslant t \leqslant 1 \}$ . So a set A is convex if and only if $[ a , b ] \subseteq { \pmb A }$ whenever $a , b   \in   A$ . The proof of the next result is left to the reader.

1.9. Proposition. (a) A set A is convex if and only if whenever $x _ { 1 } , \ldots , x _ { n } { \in } { \pmb A }$ and $t _ { 1 } , \ldots , t _ { n } \in [ 0 , 1 ]$ with $\textstyle \sum _ { j }   t _ { j }   = 1$ , then $\textstyle \sum _ { j }   t _ { j } x _ { j } { \in } { \pmb { A } } .$ (b) If $\{ A _ { i } ; i { \in } I \}$ is a collection of convex sets, then $\bigcap _ { i } A _ { i }$ is convex.

1.10. Definition. If $A \subseteq { \mathcal { X } }$ , the convex hull of A, denoted by $\operatorname { c o } ( A ) ,$ is the intersection of all convex sets that contain A. If ¿ is a TVS, then the closed convex hull of A is the intersection of all closed convex subsets of $\mathcal { X }$ that contain A; it is denoted by ${ \overline { { \mathbf { c o } } } } ( A )$

Since a vector space is itself convex, each subset of $\mathcal { X }$ is contained in a convex set. This fact and Proposition 1.9(b) imply that co(A) is well defined and convex. Also, ${ \overline { { \mathbf { c o } } } } ( A )$ is a closed convex set.

If $\mathcal { X }$ is a normed space, then $\{ x \colon \|   x   \| \leqslant 1 \}$ and $\left\{ x \colon \|   x   \| < 1 \right\}$ are both convex sets. If $f \in \mathcal{X}^*, \quad \{x: |f(x)| \leq 1\}, \quad \{x: \operatorname{Re} f(x) \leq 1\}, \quad \{x: \operatorname{Re} f(x) > 1\}$ are all convex. In fact, if $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a real linear map and C is a convex subset of $\mathcal { Y } ,$ then $T ^ { - 1 } ( C )$ is convex in $\mathcal { X }$

1.11. Proposition. Let X be a TVS and let A be a convex subset of $\mathcal { X } .$ Then (a) cl A is convex; (b) if a∈int A and b∈cl A, then $[ a , b ) \equiv \{ t b + ( 1 - t )$ a: $0 \leqslant t < 1 \} \subseteq$ int A.

PROOF. Let $a { \in } A$ , b∈cl A, and $0 \leqslant t \leqslant 1$ . Let $\left\{ x _ { i } \right\}$ be a net in A such that $x _ { i }   \rightarrow   b$ Then $t x _ { i } + ( 1 - t ) a \rightarrow t b + ( 1 - t ) a .$ This shows that

b in cl A and a in A imply $[ a , b ] \subseteq { \mathrm { c l } } A .$

Using (1.12) it is easy to show that cl A is convex. To prove (b), fix t, $0 < t < 1$ , and put $c = t b + ( 1 - t ) a ,$ where a∈int A and $b { \in } \mathbf { c l } A .$ There is an open set V in $\mathcal { X }$ such that $0 \in V$ and $a + V \subseteq A. (\mathrm{Why?})$ Hence for any d in A

$$
\begin{aligned} A & \supseteq t d + (1 - t)(a + V) \\& = t(d - b) + t b + (1 - t)(a + V) \\& = \left[ t(d - b) + (1 - t)V \right] + c.\\ \end{aligned}
$$

If it can be shown that there is an element d in A such that $0 { \in } t ( d - b ) +$ $( 1 - t ) V = U ,$ then the preceding inclusion shows that c∈int A since U is open (Exercise $4 )$ . Note that the finding of such a d in A is equivalent to finding a d such that $0 \in t^{-1}(1 - t)V + (d - b)$ or $d { \in } b - t ^ { - 1 } ( 1 - t ) V .$ But $0 \in - t ^ { - 1 } ( 1 - t ) V$ and this set is open. Since b∈cl A, d can be found in A.■

1.13. Corollary. If $A \subseteq { \mathcal { X } }$ , then ${ \overline { { \mathbf { c o } } } } ( A )$ is the closure of co(A).

A set $A \subseteq { \mathcal { X } }$ is balanced if $\alpha x { \in } A$ whenever $x { \in } A$ and $| \alpha | \leqslant 1$ . A set A is absorbing if for each x in $\mathcal { X }$ there is an $\varepsilon   >   0$ such that $t x { \in } A$ for $0 \leqslant t < \varepsilon$ Note that an absorbing set must contain the origin. If $\mathbf { \dot { \mathit { a } } } \mathbf { \in } \mathbf { \mathit { A } } ,$ , then A is absorbing at a if the set $A - a$ is absorbing. Equivalently, A is absorbing at a if for every x in $\mathcal { X }$ there is an $\varepsilon   >   0$ such that $a + t x { \in } { \pmb { A } }$ for $0 \leqslant t < \varepsilon$

If X is a vector space and p is a seminorm, then $V = \{ x : p ( x ) < 1 \}$ is a convex balanced set that is absorbing at each of its points. It is rather remarkable that the converse of this is true. This fact will be used to give an abstract formulation of a LCS and also to explore some geometric consequences of the Hahn-Banach Theorem.

1.14. Proposition. If X is a vector space over F and V is a nonempty convex, balanced set that is absorbing at each of its points, then there is a unique seminorm p on $\mathcal { X }$ such that $V = \{ x \in \mathcal { X } : p ( x ) < 1 \}$

PROOF. Define $p ( \mathbf { x } )$ by

$$
p ( x ) = \operatorname* { i n f } \{ t \colon t \geqslant 0 { \mathrm { ~ a n d ~ } } x \in t V \} .
$$

Since V is absorbing, $\mathcal { X } = \bigcup _ { n = 1 } ^ { \infty } n V ,$ so that the set whose infimum is $p ( x )$ is nonempty. Clearly $p ( 0 ) = 0 .$ To see that $p ( \alpha x ) = | \alpha | p ( x ) .$ , we can suppose that $\alpha \neq 0$ Hence, because V is balanced,

$$
\begin{aligned} p(\alpha x) &= \inf \left\{ t \geqslant 0; \alpha x \in \boldsymbol{t} V \right\} \\&= \inf \left\{ t \geqslant 0; x \in \boldsymbol{t} \left( \frac{1}{\alpha} V \right) \right\} \\&= \inf \left\{ t \geqslant 0; x \in \boldsymbol{t} \left( \frac{1}{|\alpha|} V \right) \right\} \\&= |\alpha| \inf \left\{ \frac{t}{|\alpha|}; x \in \frac{t}{|\alpha|} V \right\} \\&= |\alpha|   p(x).\\ \end{aligned}
$$

To complete the proof that p is a seminorm, note that if $\alpha , \beta \geqslant 0$ and $a , b   \in   V ,$ then

$$
\alpha a + \beta b = (\alpha + \beta) \left( \frac{\alpha}{\alpha + \beta} a + \frac{\beta}{\alpha + \beta} b \right) \in (\alpha + \beta) V
$$

by the convexity of V. If $x , y \in \mathcal { X } , p ( x ) = \alpha ,$ and $p ( y ) = \beta ,$ let $\delta   >   0 .$ Then $x { \in } ( { \pmb { \alpha } } + { \delta } ) V$ and $y { \in } ( \beta + \delta ) V .$ (Why?) Hence $x + y { \in } ( \alpha + \delta ) V + ( \beta + \delta ) V =$ $( \alpha + \beta + 2 \delta ) V$ (Exercise 11). Letting $\delta   \rightarrow   0$ shows that $p(x + y) \leqslant \alpha + \beta = p(x) +$ p(y).

It remains to show that $V = \{ x : p ( x ) < 1 \}$ . If $p ( x ) = \alpha < 1$ , then $\alpha < \beta < 1$ implies $x { \in } \beta V \subseteq V$ since V is balanced. Thus $V \supseteq \{ x \colon p ( x ) < 1 \}$ . If $x   \in   V ,$ then $p ( x )   \leqslant   1$ . Since V is absorbing at x, there is an $\varepsilon   >   0$ such that for $0 < t < \varepsilon ,$ $x + t x = y   \in   V .$ But $x = (1 + t)^{-1} y, \quad y \in V.$ Hence $p(x)=(1+t)^{-1}p(y)\leqslant$ $( 1 + t ) ^ { - 1 } < 1$

Uniqueness follows by (III.1.4).

The seminorm p defined in the preceding proposition is called the Minkowski function of V or the gauge of V.

Note that if X is a TVS space and V is an open set in , then V is absorbing at each of its points.

Using Proposition 1.14, the following characterization of a LCS can be obtained. The proof is left to the reader.

1.15. Proposition. Let X be a TVS and let U be the collection of all open convex balanced subsets of X. Then X is locally convex if and only $i f q$ is a basis for the neighborhood system at 0.

## EXERCISES

1. Let X be a TVS and let U be all the open sets containing 0. Prove the following. (a) If $U { \in } { \mathcal { U } }$ , there is a V in U such that $V + V \subseteq U$ (b) If $U { \in } { \mathcal { U } }$ , there is a V in U such that $V \subseteq U$ and $\alpha V \subseteq V$ for all $| \alpha | \leqslant 1 . ( V$ is balanced.) (Hint: If $W { \in } { \mathcal { U } }$ and $\alpha W \subseteq U$ for $| \alpha | \leqslant \varepsilon ,$ then $\varepsilon W \subseteq \beta U \mathrm { f o r } | \beta | \geqslant 1 .$

2. Show that a LCS is a TVS.

3. Suppose that $\mathcal { X }$ is a TVS but do not assume that $\mathcal { X }$ is Hausdorff. (a) Show that $\mathcal { X }$ is Hausdorff if and only if the singleton set {0} is closed. (b) If X is Hausdorff, show that $\mathcal { X }$ is a regular topological space.

4. Let $\mathcal { X }$ be a TVS. Show: (a) if $x _ { 0 } { \in } { \mathcal { X } }$ , the map $x   \mapsto   x + x _ { 0 }$ is a homeomorphism of X onto X; (b) if $\alpha \in \mathbb { F }$ and $\alpha \neq 0 ,$ the map x→αx is a homeomorphism.

5. Prove Proposition 1.4.

6. Verify the statements made in Example 1.5. Show that a net $\{ f _ { i } \}$ in C(X) converges to f if and only if $f _ { i }   \rightarrow   f$ uniformly on compact subsets of X.

7. Show that the space H(G) defined in (1.6) is complete. (Every Cauchy net converges.)

8. Verify the statements made in Example 1.7. Give a basis for the neighborhood system at 0.

9. Verify the statements made in Example 1.8.

10. Prove Proposition 1.9.

11. Show that if A is a convex set and $\alpha , \beta > 0 ,$ then $\alpha A + \beta A = (\alpha + \beta)A$ , Give an example of a nonconvex set A for which this is untrue.

12. If ¿ is a TVS and A is closed, show that A is convex if and only if $\scriptstyle { \frac { 1 } { 2 } } ( x + y ) \in { \pmb A }$ whenever x and y∈A.

13. Let s = the space of all sequences of scalars. Thus s = all functions $x \colon \mathbf { N }   \to   \mathbf { F } ,$ Define addition and scalar multiplication in the usual way. If x, y∈s, define

$$
d(x,y)=\sum_{n = 1}^{\infty}2^{- n}\frac{\left | x(n) - y(n) \right | }{1 + \left | x(n) - y(n) \right | }
$$

Show that $d$ is a metric on s and that with this topology s is a TVS. Also show that s is complete.

14. Let $( X , \Omega , \mu )$ be a finite measure space, let $\mathcal { M }$ be the space of Ω-measurable functions, and identify two functions that agree a.e. [μ]. If $f , g \in { \mathcal { M } }$ , define

$$
d ( f , g ) = \int \frac { | f - g | } { 1 + | f - g | } d \mu .
$$

Then d is a metric on $\mathcal { M }$ and $( d , d )$ is a complete TVS. Is there a relationship between this example and the space s of Exercise 13?

15. If X is a TVS and $A \subseteq { \mathcal { X } }$ , then cl $A = \cap \left\{ A + V : \right.$ 0∈V and V is open}.

16. If $\mathcal { X }$ is a TVS and M is a closed linear space, then $x / \mathcal { M }$ with the quotient topology is a TVS. If p is a seminorm on $\mathcal { X } ,$ define $\vec { p }$ on $\mathcal { X } / \mathcal { M }$ by $\bar{p}(x + \mathcal{M}) = \inf \left\{ p(x + y) : y \in \mathcal{M} \right\}$ Show that $\bar { p }$ is a seminorm on $x / M$ Show that if X is a LCS, then so is $x / \mathcal { M }$

17. If $\{ \mathcal { X } _ { i } ; i { \in } I \}$ is a family of $\mathbf { T V S ^ { \prime } } \mathbf { s } ,$ then $\mathcal { X }   =   \Pi \{ \mathcal { X } _ { i } ;   i   \in   I \}$ with the product topology is a TVS. If each $\mathcal { X } _ { i }$ is a LCS, then so is X. If X is a LCS, must each $\mathcal { X } _ { i }$ be a LCS?

18. If $\mathcal { X }$ is a finite-dimensional vector space and $\mathcal { T } _ { 1 } , \mathcal { T } _ { 2 }$ are two topologies on $\mathcal { X }$ that make $\mathcal { X }$ into a TVS, then $\mathcal { T } _ { 1 } = \mathcal { T } _ { 2 }$

19. If $\mathcal { X }$ is a TVS and $\mathcal { M }$ is a finite dimensional linear manifold in $\mathcal { X } ,$ then $\mathcal { M }$ is closed and $\mathcal { Y } + \mathcal { M }$ is closed for any closed subspace $\pmb { g }$ of $\mathcal { X }$

20. Let $\mathcal { X }$ be any infinite dimensional vector space and let $\mathcal { T }$ be the collection of all subsets $W$ of $\mathcal { X }$ such that if $x   \in   W ,$ then there is a convex balanced set $U$ with $x + U \subseteq W$ and $U \cap \mathcal { M }$ open in $\mathcal { M }$ for every finite dimensional linear manifold $\mathcal { M }$ in $\mathcal { X }$ (Each such $\mathcal { M }$ is given its usual topology.) Show: (a) $( \mathcal { X } , \mathcal { T } )$ is a LCS; (b) a set $F$ is closed in $\mathcal { X }$ if and only if $F r \mathcal { M }$ is closed for every finite dimensional subspace $\mathcal { M }$ of x; (c) if Y is a topological space and $f \colon { \mathcal { X } } \to Y$ (not necessarily linear), then f is continuous if and only $\mathbf { i f } f | \mathcal { M }$ is continuous for every finite dimensional space $\mathcal { M } ; ( \mathbf { d } )$ if $\mathcal { Y }$ is a TVS and $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear map, then T is continuous.

21. Let X be a locally compact space and for each φ in $C _ { 0 } ( X )$ , define $p _ { \phi } ( f ) = \| \phi f \| _ { \infty }$ for f in $C _ { b } ( X )$ . Show that $p _ { \phi }$ is a seminorm on $C _ { b } ( X )$ . Let $\beta = \mathrm { t h e }$ topology defined by these seminorms. Show that $( C _ { b } ( X ) , \beta )$ is a LCS that is complete. $\beta$ is called the strict topology.

22. For $0 < p < 1$ , let $l ^ { p } = \mathrm { a l l }$ sequences x such that $\sum_{n = 1}^{\infty}|x(n)|^{p} < \infty$ . Define $\begin{array} { r } { d ( x , y ) = \sum _ { n = 1 } ^ { \infty } | x ( n ) - y ( n ) | ^ { p } } \end{array}$ (no pth root). Then d is a metric and $( l ^ { p } , d )$ is a TVS that is not locally convex.

23. Let $\mathcal { X }$ and @ be locally convex spaces and let $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ be a linear transformation. Show that T is continuous if and only if for every continuous seminorm $p$ on $\pmb { y }$ $p \circ T$ is a continuous seminorm on $\mathcal { X }$

24. Let $\mathcal { X }$ be a LCS and let $G$ be an open connected subset of $\mathcal { X } .$ Show that G is arcwise connected.

## §2. Metrizable and Normable Locally Convex Spaces

Which LCS's are metrizable? That is, which have a topology which is defined by a metric? Which $\mathbf { L C S ^ { \prime } s }$ have a topology that is defined by a norm? Both are interesting questions and both answers could be useful.

If $\mathcal { P }$ is a family of seminorms on $\mathcal { X }$ and $\mathcal { X }$ is a TVS, say that $\mathcal { P }$ determines the topology on $\mathcal { X }$ if the topology of $\mathcal { X }$ is the same as the topology induced $\mathcal { P }$

2.1. Proposition. Let $\{ p _ { 1 } , p _ { 2 } , \ldots \}$ be a sequence of seminorms on $\mathcal { X }$ such that $\int_{n = 1}^{\infty} \left\{ x: p_{n}(x) = 0 \right\} = (0)$ . For x and y in $\mathcal { X } ,$ , define

$$
d(x,y)=\sum_{n = 1}^{\infty}2^{- n}\frac{p_{n}(x - y)}{1 + p_{n}(x - y)}
$$

Then d is a metric on $\mathcal { X }$ and the topology on $\mathcal { X }$ defined by d is the topology