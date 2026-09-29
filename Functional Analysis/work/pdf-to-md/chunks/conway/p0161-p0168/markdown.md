Let $x { \in } X ,   x \neq x _ { 0 }$ . By (b) there is an $f _ { 1 }$ in $\alpha$ such that $f _ { 1 } ( x _ { 0 } ) \neq f _ { 1 } ( x ) = \beta$ By (a), the function $\beta \in \mathcal { A }$ Hence $f _ { 2 } = f _ { 1 } - \beta \in \mathcal { A } , f _ { 2 } ( x _ { 0 } ) \neq 0 = f _ { 2 } ( x )$ By (c), $f_{3} = \left| f_{2} \right|^{2} = f_{2} \bar{f}_{2} \in \mathcal{A}.$ Also, $f_{3}(x)=0<f_{3}(x_{0})$ and $f _ { 3 } \geqslant 0 .$ Put $f =$ $( \| f _ { 3 } \| + 1 ) ^ { - 1 } f _ { 3 }$ Then $f \in \mathcal { A } , \quad f ( x ) = 0 , \quad f ( x _ { 0 } ) > 0 ,$ and $0 \leqslant f < 1$ on $X$ Moreover, because $\alpha$ is an algebra, gf and $g ( 1 - f ) { \in } { \mathcal { A } }$ for every $g$ in $\varkappa$ Because $\mu \in \mathcal { A } ^ { \perp } , 0 = \int g f d \mu = \int g ( 1 - f ) d \mu$ for every g in $\varkappa$ Therefore $f \mu$ and $( 1 - f ) \mu { \in \mathcal { A } } ^ { \perp }$

(For any bounded Borel function h on $X , h \mu$ denotes the measure whose value at a Borel set ∆ is $\int _ { \Delta } h d \mu .$ Note that $\| h \mu \| = \int | h | d | \mu | .$

Put $\alpha = \| f \mu \| = \int f d | \mu |$ .Since $f ( x _ { 0 } ) > 0$ , there is an open neighborhood U of $x _ { 0 }$ and an $\varepsilon   >   0$ such that $f ( y )   >   \varepsilon$ for y in U. Thus, $\alpha = \int f d | \mu | \geqslant \int _ { U } f d | \mu | \geqslant \varepsilon | \mu | ( U ) > 0$ since $\overline { { U } } \cap K \neq \square$ . Similarly, since $f ( x _ { 0 } )   <$ $1 , \quad \alpha < 1$ . Therefore, $0 < \alpha < 1$ . Also, $1 - \alpha = 1 - \int f d | \mu | = \int ( 1 - f ) d | \mu | =$ $\| ( 1 - f ) \mu \|$ . Since

$$
\mu = \alpha \left[ \frac{f \mu}{\left\| f \mu \right\|} \right] + (1 - \alpha) \left[ \frac{(1 - f) \mu}{\left\| (1 - f) \mu \right\|} \right]
$$

and $\mu$ is an extreme point of ball $\mathcal { A } ^ { \perp } ,   \mu = f \mu   \| f \mu \| ^ { - 1 } = \alpha ^ { - 1 } f \mu .$ But the only way that the measures $\mu$ and $\alpha ^ { - 1 } f \mu$ can be equal is if $\alpha ^ { - 1 } f = 1$ a.e. [µ]. Since f is continuous, it must be that $f \equiv \alpha$ on K. Since $x_{0} \in K, f(x_{0}) = \alpha$ But $f(x_0) > f(x) = 0$ . Hence $x \notin K$ This establishes that $K = \left\{ x _ { 0 } \right\}$ and so $\mu = \gamma \delta _ { x _ { 0 } }$ where $| \gamma | = 1$ . But $\mu \in \mathcal { A } ^ { 1 }$ and $1 \in \mathcal { A } ,$ so $0 = \int 1   d\mu = \gamma$ , a contradiction. Therefore $\mathcal { A } ^ { \perp }   =   ( 0 )$ and ${ \mathcal { A } } = C ( X )$

With an important theorem it is good to ask what happends if part of the hypothesis is deleted. If $x _ { 0 } { \in } X$ and $\mathcal { A } = \left\{ f \in C ( X ) : f ( x _ { 0 } ) = 0 \right\}$ , then $\varkappa$ is a closed subalgebra of $C ( X )$ that satisfies (b) and (c) but ${ \mathcal { A } } \neq C ( X )$ . This is the worst that can happen

8.2. Corollary. If X is compact and $\varkappa$ is a closed subalgebra of $C ( X )$ that separates the points of X and is closed under complex conjugation, then either ${ \mathcal { A } } = C ( X )$ or there is a point $x _ { 0 }$ in X such that $\mathcal { A } = \left\{ f \in C ( X ) : f ( x _ { 0 } ) = 0 \right\}$

PRoOF. Identify F and the one-dimensional subspace of C(X) consisting of the constant functions. Since $\varkappa$ is closed, $\mathbf { \partial } \mathbf { \partial } + \mathbf { F }$ is closed (III.4.3). It is easy to see that $\mathcal { A } + \mathbb { F }$ is an algebra and satisfies the hypothesis of the Stone-Weierstrass Theorem; hence ${ \mathcal { A } } + \mathbb { F } = C ( X )$ . Suppose ${ \mathcal { A } } \neq C ( X )$ . Then $C ( X ) / { \mathcal { A } }$ is one dimensional; thus $\alpha ^ { \perp }$ is one dimensional (Theorem 2.2). Let $\mu { \in } { \mathcal { A } } ^ { \perp } ,   \|   \mu   \| = 1$ . If $f \in \mathcal { A } _ { j }$ then $f \mu \in \mathcal { A } ^ { 1 }$ ; hence there is an α in $\mathbf { F }$ such that $f \mu = \alpha \mu .$ This implies that each f in $\alpha$ is constant on the support of $\mu .$ But the functions in $\varkappa$ separate the points of X. Hence the support of $\mu$ is a single point $x _ { 0 }$ and so $\mathcal { A } ^ { \perp } = \{ \beta \delta _ { x _ { 0 } } \colon \beta { \in } \mathbb { F } \}$ Thus $\mathcal { A } = \mathcal { A } ^ { \perp } = \{ f { \in } C ( X ) ;$ $f ( x _ { 0 } ) = 0 \}$

There are many examples of subalgebras of $C ( X )$ that separate the points of $X$ , contain the constants, but are not necessarily closed under complex conjugation. Indeed, a subalgebra of $C ( X )$ having these properties is called a uniform algebra or function algebra and their study forms a separate area of mathematics (Gamelin [1969]). One example (the most famous) is obtained by letting X be a subset of C and letting ${ \mathcal { A } } = R ( X ) \equiv { \mathrm { t h e } }$ uniform closure of rational functions with poles off X.

Let $x _ { 0 } , x _ { 1 } { \in } X ,   x _ { 0 } \neq x _ { 1 }$ , and let $\mathcal { A } \equiv \left\{ f { \in } C ( X ) : f ( x _ { 0 } ) = f ( x _ { 1 } ) \right\}$ Then $\varkappa$ is a uniformly closed subalgebra of C(X), contains the constant functions, and is closed under conjugation. In a certain sense this is the worst that can happen if the only hypothesis of the Stone-Weierstrass Theorem that does not hold is that  fails to separate the points of X (see Exercise 4).

If X is only assumed to be locally compact, then the story is similar.

## 8.3. Corollary. If X is locally compact and A is a closed subalgebra of $C _ { 0 } ( X )$ such that

(a) for each x in X there is an f in A such that $f(x) \neq 0;$

(b) A separates the points of X;

(c) $\overline { { f } } \in \mathcal { A }$ whenever f∈A;

then ${ \mathcal { A } } = C _ { 0 } ( X )$

PROOF. Let $X _ { \infty } =$ the one point compactification of X and identify $C _ { 0 } ( X )$ with $\{ f { \in } C ( X _ { \infty } ) { : } f ( \infty ) = 0 \}$ . So $\varkappa$ becomes a subalgebra of $C ( X _ { \infty } )$ . Now apply Corollary 8.2. The details are left to the reader.

What are the extreme points of the unit ball of $M ( X ) ?$ The characterization of these extreme points as well as the extreme points of the set $P ( X )$ of probability measures on X is given in the next theorem. [A probability measure is a positive measure $\mu$ such that $\mu ( X ) = 1 . ]$

8.4. Theorem. If X is compact, then the set of extreme points of ball M(X) is

$$
\{ \alpha \delta _ { x } : | \alpha | = 1 { \mathrm { ~ a n d ~ } } x \in X \} .
$$

The set of extreme points of P(X), the probability measures on X, is

$$
\{ \delta _ { x } \colon x   \in   X \} .
$$

ProoF. It is left as an exercise for the reader to show that if $x   \in   X ,   \delta _ { x }$ is an extreme point of P(X) and $\alpha \delta _ { \mathbf { x } }$ is an extreme point of ball M(X) (Exercise 3).

It will now be shown that if $\mu$ is an extreme point of P(X), then $\mu$ is an extreme point of ball $M ( X )$ . Thus the first part of the theorem implies the second. Suppose μ is an extreme point of $P ( X )$ and $v _ { 1 } , v _ { 2 } \in \mathrm { b a l l } M ( X )$ such that $\mu = \frac { 1 } { 2 } ( \boldsymbol { v } _ { 1 } + \boldsymbol { v } _ { 2 } )$ Then $1 = \| \mu \| \leqslant \frac{1}{2} ( \| v_1 \| + \| v_2 \| ) \leqslant 1;$ hence $\| \nu _ { 1 } \| +$ $\| \nu _ { 2 } \| = 2$ and so $\| \boldsymbol { v } _ { 1 } \| = \| \boldsymbol { v } _ { 2 } \| = 1$ . Also, $1 = \mu(X) = \frac{1}{2}(v_1(X) + v_2(X))$ . Now $| v _ { 1 } ( X ) | , | v _ { 2 } ( X ) | \leqslant 1$ and 1 is an extreme point of $\{ \alpha \in \mathbb{F} : |\alpha| \leq 1 \}$ . Hence for $k = 1 , 2 , \| v _ { k } \| = v _ { k } ( X ) = 1$ . By Exercise III.7.2, $v _ { k }   \in   P ( X )$ for $k = 1 , 2$ . Since µ∈ext P(X), $\boldsymbol { \mu } = \boldsymbol { v } _ { 1 } = \boldsymbol { v } _ { 2 }$ . So $\mu$ is an extreme point of ball $M ( X )$ Thus it suffices to prove the first part of the theorem.

Suppose that $\mu$ is an extreme point of ball $M ( X )$ and let K be the support of $\mu .$ It will be shown that K is a singleton set.

Fix $x _ { 0 }$ in K and suppose there is a second point x in $K , x \neq x _ { 0 }$ . Let U and V be open subsets of X such that $x _ { 0 }   \in   U ,   x   \in   V ,$ and cl U∩cl $V = \bigtriangleup$ . By Urysohn's Lemma there is an f in $C ( X )$ such that $0 \leqslant f \leqslant 1, f(y) = 1$ for y in cl U, and $f ( y )   =   0$ for y in cl V. Consider the measures $f \mu$ and $( 1 - f ) \mu .$ Put $\alpha = \| f \mu \| = \int | f | d | \mu | = \int f d | \mu |$ Then $\alpha = \int f d | \mu | \leqslant \| \mu \| = 1$ and $\alpha =$ $\int f d | \mu | \geqslant | \mu | ( U ) > 0 \mathrm { s i n c e } U$ is open and $U \cap K \neq \dot{\square}. \mathrm{Also}, 1 - \alpha = 1 - \int f d|\mu| =$ $\int ( 1 - f ) d | \mu | = \| ( 1 - f ) \mu \|$ and so $1 - \alpha \geqslant \int_{V} (1 - f) d|\mu| = |\mu| (V) > 0$ since $x   \in   K$ . Hence $0 < \alpha < 1$

But $f \mu / \alpha$ and $( 1 - f ) \mu / ( 1 - \alpha ) \in$ ball $M ( X )$ and

$$
\mu = \alpha \Bigg [ \frac { f \mu } { \alpha } \Bigg ] + ( 1 - \alpha ) \Bigg [ \frac { ( 1 - f ) \mu } { 1 - \alpha } \Bigg ] .
$$

Since $\mu$ is an extreme point of ball M(X) and $\alpha \neq 0 ,   \mu = f \mu / \alpha$ .This can only happen if $f \equiv \alpha < 1   a.e.   [\mu]$ . But $f \equiv 1$ on U and $| \mu | ( U )   >   0 ,$ a contradiction. Hence $K = \left\{ x _ { 0 } \right\}$

Since the only measures whose support can be the singleton set $\{ x _ { 0 } \}$ have the form $\alpha \delta _ { x _ { 0 } } , \alpha$ in F, the theorem is proved.

## EXERCISES

1. Suppose that $\varkappa$ is a subalgebra of C(X) that separates the points of X and $1 \in \mathcal { A }$ Show that if $x _ { 1 } , \ldots , x _ { n }$ are distinct points in X and $\alpha _ { 1 } , \ldots , \alpha _ { n } \in \mathbb { F }$ , there is an $f$ in $\varkappa$ such that $f ( x _ { j } )   =   \alpha _ { j }$ for $1 \leqslant j \leqslant n .$

2. Give the details of the proof of Corollary8.3.

3. If X is compact, show that for each x in $X , \delta _ { x }$ is an extreme point of $P ( X )$ and $\alpha \delta _ { x } ,   | \alpha | = 1$ , is an extreme point of ball $M ( X )$

4. Let X be compact and let  be a closed subalgebra of $C ( X )$ such that $1 \in \mathcal { A }$ and $\varkappa$ is closed under conjugation. Define an equivalence relation ～ on X by declaring $x \sim y$ if and only if $f ( x ) = f ( y )$ for all $f$ in $\varkappa$ Let $X / \sim$ be the corresponding quotient space and let π: $X   \to   X / \sim$ be the natural map. Give $X / \sim$ the quotient topology. (a) Show that if $f \in \mathcal { A } ,$ then there is a unique function $\pi ^ { * } ( f )$ in $C ( X / { \sim } )$ such that $\pi ^ { * } ( f ) \circ \pi = f .$ (b) Show that $\pi ^ { * } \colon { \mathcal { A } } \to C ( X / \sim )$ is an isometry. (c) Show that $\pi ^ { * }$ is surjective. (d) Show that $\mathcal { A } = \{ f \in C ( X ) : f ( x ) = f ( y )$ whenever $x \sim y \}$

5. (This exercise requires Exercise IV.4.7.) Let X be completely regular and topologize C(X) as in Example IV.1.5. If  is a closed subalgebra of $C ( X )$ such that $1 \in \mathcal { A } _ { 1 }$ $\varkappa$ separates the points of X, and $\bar { f } \in \mathcal { A }$ whenever $f \in \mathcal { A } ,$ then ${ \mathcal { A } } = C ( X )$

6. Let $X , Y$ be compact spaces and show that if $f { \in } C ( X \times Y )$ and $\varepsilon   >   0$ , then there are functions $g _ { 1 } , \ldots , g _ { n }$ in C(X) and $h _ { 1 } , \ldots , h _ { n }$ in C(Y) such that $\{ f ( x , y ) -$ $\begin{array} { r } { \sum _ { k = 1 } ^ { n } g _ { k } ( x ) h _ { k } ( y ) | < \varepsilon } \end{array}$ for all $( x , y )$ in $X \times Y .$

7. Let $\alpha$ be the uniformly closed subalgebra of $C _ { b } ( \mathbb { R } )$ generated by sin x and cos x. Show that $\mathcal { A } = \left\{ f \in C _ { b } ( \mathbb { R } ) : f ( t ) = f ( t + 2 \pi ) \right\}$ for all t in $\left\{ \mathbf { R } \right\}$

8. If K is a compact subset of $\mathbf { C } , f { \in } { \mathbf { C } } ( K ) ,$ and $\varepsilon   >   0 .$ , show that there is a polynomial $p ( z , { \bar { z } } )$ in z and ž such that $| f ( z ) - p ( z , \bar { z } ) | < \varepsilon$ for all z in K.

## $\S 9 ^ { * }$ . The Schauder Fixed Point Theorem

Fixed-point theorems hold a fascination for mathematicians and they are very applicable to a variety of mathematical and physical situations. In this section and the next two such theorems are presented.

The results of this section are different from the rest of this book in an essential way. Although we will continue to look at convex subsets of Banach spaces, the functions will not be assumed to be linear or affine. This is a small part of nonlinear functional analysis.

To begin with, recall the following classical result whose proof can be found in any algebraic topology book. (Also see Dugundji [1966].)

9.1. Brouwer's Fixed Point Theorem. If $1 \leqslant d < \infty,   B = the$ closed unit ball of $\mathbb { R } ^ { d } .$ and f: $B   \rightarrow   B$ is a continuous map, then there is a point x in B such that $f ( x ) = x$

9.2. Corollary. If K is a nonempty compact convex subset of a finite dimensional normed space X and $f \colon K   \to   K$ is a continuous function, then there is a point x in K such that $f ( x ) = x$

PRooF. Since X is isomorphic to either $\mathbf { \mathbb { C } } ^ { d }$ or $\mathbf { R } ^ { d } ;$ it is homeomorphic to either $\mathbb { R } ^ { 2 d }$ or $\mathbb { R } ^ { d } .$ So it suffices to assume that $\mathcal { X } = \mathbb { R } ^ { d } , 1 \leqslant d < \infty$ . If $K = \{ x \in \mathbb { R } ^ { d } : \| x \| \leqslant r \}$ , then the result is immediate from Brouwer's Theorem (Exercise). If K is any compact convex subset of $\mathbf { R } ^ { d } ;$ let $r   >   0$ such that $K \subseteq B \equiv \{ x \in \mathbb { R } ^ { d } : \| x \| \leqslant r \}$ . Let φ: $B   \rightarrow   K$ be the function defined by $\phi ( x ) =$ the unique point y in K such that $\| x - y \| = \mathrm{dist}(x, K)$ (I.2.5). Then $\phi$ is continuous (Exercise) and $\phi ( x ) = x$ for each x in K. (In topological parlance, K is a retract of $B . )$ Hence $f \circ \phi : B \to K \subseteq B$ is continuous. By Brouwer's Theorem, there is an x in B such that $f ( \phi ( x ) ) = x .$ Since $f \circ \phi ( B ) \subseteq K ,   x \in K.$ Hence $\phi ( x ) = x$ and $f ( x ) = x$

Schauder's Fixed Point Theorem is a generalization of the preceding corollary to infinite dimensional spaces.

9.3. Definition. If $\mathcal { X }$ is a normed space and $E \subseteq { \mathcal { X } }$ , a function $f \colon E   \to   { \mathcal { X } }$ is said to be compact if $f$ is continuous and cl $f ( A )$ is compact whenever A is a bounded subset of E.

If E is itself a compact subset of $\mathcal { X } ,$ then every continuous function from E into $\mathcal { X }$ is compact.

The following lemma will be needed in the proof of Schauder's Theorem

9.4. Lemma. If K is a compact subset of the normed space $\mathcal { X } ,   \varepsilon   >   0 ,$ and A is a finite subset of K such that $K \subseteq \bigcup \left\{ B ( a ; \varepsilon ) : a { \in } A \right\}$ , define $\phi _ { A } \colon K   \to   \mathcal { X }$ by

$$
\phi _ { A } ( x ) = \frac { \sum \{ m _ { a } ( x ) a : a \in A \} } { \sum \{ m _ { a } ( x ) : a \in A \} } ,
$$

where $m _ { a } ( x ) = 0 \mathrm { i f } \| x - a \| \geqslant \varepsilon$ and $m _ { a } ( x ) = \varepsilon - \| x - a \| \mathrm { i f } \| x - a \| \leqslant \varepsilon .$ Then $\phi _ { A }$ is a continuous function and

$$
\| \phi _ { A } ( x ) - x \| < \varepsilon
$$

for all x in K.

PRooF. Note that for each a in A, $m _ { a } ( x ) \geqslant 0$ and $\scriptstyle \sum \{ m _ { a } ( x ) : a \in A \} > 0$ for all x in K. So $\phi _ { A }$ is well defined on K. The fact that $\phi _ { A }$ is continuous follows from the fact that for each a in A, $m _ { a } \colon K \to [ 0 , \varepsilon ]$ is continuous. (Verify!)

If $x   \in   K$ , then

$$
\phi _ { A } ( x ) - x = \frac { \sum \{ m _ { a } ( x ) [ a - x ] : a \in A \} } { \sum \{ m _ { a } ( x ) : a \in A \} } .
$$

If $m _ { a } ( x ) > 0$ , then $\| x - a \| < \varepsilon .$ Hence

$$
\| \phi _ { A } ( x ) - x \| \leqslant \frac { \sum \{ m _ { a } ( x ) \| a - x \| : a \in A \} } { \sum \{ m _ { a } ( x ) : a \in A \} } < \varepsilon .
$$

This concludes the proof.

9.5. The Schauder Fixed Point Theorem. Let E be a closed bounded convex subset of a normed space ${ \mathcal { X } } . ~ I f f \colon E   \to   { \mathcal { X } }$ is a compact map such that $f ( E ) \subseteq E ,$ then there is an x in E such that $f ( x ) = x .$

PROOF. Let $K = \operatorname { c l } f ( E ) ,$ so $K \subseteq E$ . For each positive integer n let $A _ { n }$ be a finite subset of K such that $K \subseteq \bigcup \{ B ( a ; 1 / n ) : a \in A _ { n } \}$ . For each n let $\phi _ { n } = \phi _ { A _ { n } }$ as in the preceding lemma. Now the definition of $\phi _ { n }$ clearly implies that $\phi _ { n } ( K ) \subseteq \operatorname { c o } ( K ) \subseteq E$ since E is convex; thus $f _ { n } \equiv \phi _ { n } \circ f$ maps E into E. Also, Lemma 9.4 implies

## 9.6

$$
\| f _ { n } ( x ) - f ( x ) \| < 1 / n \quad \mathrm { f o r } x \mathrm { i n } E .
$$

Let $\mathcal { X } _ { n }$ be the linear span of the set $A _ { n }$ and put $E _ { n } = E \cap { \mathcal { X } } _ { n } .$ So $\mathcal { X } _ { n }$ is a finite dimensional normed space, $E _ { n }$ is a compact convex subset of $\mathcal { X } _ { \pmb { n } }$ and $f_{n}:E_{n}\rightarrow E_{n}(\mathrm{Why?})$ is continuous. By Corollary 9.2, there is a point $x _ { n }$ in $E _ { n }$ such that $f _ { n } ( x _ { n } ) = x _ { n }$

Now $\{ f ( x _ { n } ) \}$ is a sequence in the compact set $K ,$ so there is a point $x _ { 0 }$ and a subsequence $\{ f ( x _ { n _ { j } } ) \}$ such that $f ( x _ { n _ { j } } )   \to   x _ { 0 }$ . Since $f_{n_j}(x_{n_j}) = x_{n_j},$ (9.6) implies

$$
\begin{align*}\|x_{n_j} - x_0\| \leqslant & \|f_{n_j}(x_{n_j}) - f(x_{n_j})\| + \|f(x_{n_j}) - x_0\| \\\leqslant & \frac{1}{n_j} + \|f(x_{n_j}) - x_0\|.\end{align*}
$$

Thus $x _ { n _ { j } }   \rightarrow   x _ { 0 }$ . Since f is continuous, $f(x_{0}) = \lim_{n \to \infty} f(x_{n_{j}}) = x_{0}.$

There is a generalization of Schauder's Theorem where $\mathcal { X }$ is only assumed to be a LCS. See Dunford and Schwartz [1958], p. 456.

EXERCISE

1. Let $E   =   \{ x   \in   l ^ { 2 } ( \mathbb { N } ) : \| x \| \leqslant 1 \}$ and for x in E define $f(x) = \left( \left( 1 - \| x \|^2 \right)^{1/2}, x(1), x(2), \ldots \right)$ Show that $f ( E ) \subseteq E , f$ is continuous, and f has no fixed points.

## $\S 1 0 ^ { * }$ . The Ryll-Nardzewski Fixed Point Theorem

This section begins by proving a fixed point theorem that in addition to being used to prove the result in the title of this section has some interest of its own. Recall that a map T defined from a convex set K into a vector space is said to be affine if $T ( \sum \alpha _ { j } x _ { j } ) = \sum \alpha _ { j } T ( x _ { j } )$ when $x _ { j } { \in } K , \; \alpha _ { j } \geqslant 0 ,$ and $\sum \alpha _ { j } = 1$

10.1. The Markov-Kakutani Fixed Point Theorem. If K is a nonempty compact convex subset of a LCS $\mathcal { X }$ and $\mathcal { F }$ is a family of continuous affine maps of K into itself that is abelian, then there is an $x _ { 0 }$ in $K$ such that $T ( x _ { 0 } ) = x _ { 0 }$ for all T in $\mathcal { F }$

PROOF. If $T   \in   \mathcal { F }$ and $n \geqslant 1$ , define $T ^ { ( n ) } \colon K \to K$ by

$$
T^{(n)} = \frac{1}{n} \sum_{k = 0}^{n - 1} T^k.
$$

If S and $T   \in   \mathcal { F }$ and $n , m \geqslant 1$ , then it is easy to check that $S ^ { ( n ) } T ^ { ( m ) } = T ^ { ( m ) } S ^ { ( n ) }$ Let $\mathcal { H } = \left\{ T ^ { ( n ) } ( K ) \right.$ $T { \in } { \mathcal { F } } , ~ n \geqslant 1 \}$ Each set in $\mathcal { H }$ is compact and convex. If $T _ { 1 } , \ldots , T _ { p } { \in } { \mathcal { F } }$ and $n _ { 1 } , \ldots , n _ { p } \geqslant 1$ , then the commutativity of $\mathcal { F }$ implies that $T _ { 1 } ^ { ( n _ { 1 } ) } \cdots T _ { p } ^ { ( n _ { p } ) } ( K ) \subseteq \bigcap _ { j = 1 } ^ { p } T _ { j } ^ { ( n _ { j } ) } ( K )$ . This says that $\mathcal { H }$ has the finite intersection property and hence there is an $x _ { 0 }$ in $\bigcap \{ B : B \in \mathcal { H } \}$ . It is claimed that $x _ { 0 }$ is the desired common fixed point for the maps in $\mathcal { F }$

If $T { \in } { \mathcal { F } }$ and $n \geqslant 1$ , then $x _ { 0 }   \in   \boldsymbol { T } ^ { ( n ) } ( K )$ . Thus there is an x in K such that

$$
x _ { 0 } = T ^ { ( n ) } ( x ) = \frac { 1 } { n } \left[ x + T ( x ) + \cdots + T ^ { n - 1 } ( x ) \right].
$$

Using this equation for $x _ { 0 }$ , it follows that

$$
\begin{aligned}T(x_{0}) - x_{0} = & \frac{1}{n}[T(x) + \cdots + T^{n}(x)] \\& - \frac{1}{n}[x + T(x) + \cdots + T^{n - 1}(x)] \\= & \frac{1}{n}[T^{n}(x) - x] \\\in & \frac{1}{n}[K - K].\end{aligned}
$$

Now K is compact and so $K - K$ is also. If U is an open neighborhood of 0 in X, there is an integer $n \geqslant 1$ such that $n ^ { - 1 } [ K - \bar { K } ] \subseteq U$ .Therefore $T ( x _ { 0 } )   -   x _ { 0 }   \in   U$ for every open neighborhood U of 0. This implies that $T ( x _ { 0 } ) - x _ { 0 } = 0$

If p is a seminorm on $\mathcal { X }$ and $A \subseteq { \mathcal { X } }$ , define the p-diameter of A to be the number

$$
p - \mathrm{diam} A \equiv \sup\{p(x - y): x, y \in A\}.
$$

10.2. Lemma. If X is a LCS, K is a nonempty separable weakly compact convex subset of X, and p is a continuous seminorm on $\mathcal { X } ,$ , then for every $\varepsilon   >   0$ there is a closed convex subset C of K such that:

(a) $C \neq K ;$

(b) $p - \mathrm{diam}(K \backslash C) \leqslant \varepsilon.$

PROOF. Let $S = \{ x \in \mathcal{X} : p(x) \leq \varepsilon / 4 \}$ and let D = the weak closure of the set of extreme points of K. Note that $D \subseteq K$ . By hypothesis there is a countable subset A of K such that $D \subseteq K \subseteq \bigcup \{ a + S : a \in A \}$ . Now each $a + S$ is weakly closed. (Why?) Since D is weakly compact, there is an a in A such that $( a + S ) \cap D$ has interior in the relative weak topology of D (Exercise 2). Thus, there is a weakly open subset W of $\mathcal { X }$ such that

## 10.3

$$
( a + S ) \cap D \supseteq W \cap D \neq \square .
$$

Let $K_{1} = \overline{\mathrm{co}}(D \setminus W)$ and $K_{2}=\overline{\mathrm{co}}(D\cap W)$ . Because $K _ { 1 }$ and $K _ { 2 }$ are compact and convex and $K _ { 1 }   \cup   K _ { 2 }$ contains the extreme points of K, the Krein-Milman Theorem and Exercise 7.8 imply $K = \operatorname { c o } ( K _ { 1 } \cup K _ { 2 } )$

## 10.4. Claim. $K _ { 1 } \neq K .$

In fact, if $K _ { \mathrm { 1 } } = K$ , then $K = \overline{\mathrm{co}}(D \setminus W)$ so that ext $K \subseteq D \backslash W$ (Theorem 7.8). This implies that $D \subseteq D \backslash W ,$ or that $W \cap D = \square$ , a contradiction to (10.3).

Now (10.3) implies that $K _ { 2 } \subseteq a + S ;$ so the definition of S implies that p-diam $K _ { 2 } \leqslant \varepsilon / 2$ . Let $0 < r \leqslant 1$ and define $f _ { r } \colon K _ { 1 } \times K _ { 2 } \times [ r , 1 ] \to K$ by $f_{r}(x_{1},x_{2},t)=tx_{1}+(1-t)x_{2}$ . So $f _ { r }$ is continuous and $C _ { r } \equiv f _ { r } ( K _ { 1 } \times K _ { 2 } \times$ [r, 1]) is weakly compact and convex. (Verify!)

## 10.5. Claim. $C _ { r } \neq K$ for $0 < r \leqslant 1$

In fact, if $C _ { r }   =   K$ and e∈ext K, then $e = t x _ { 1 } + ( 1 - t ) x _ { 2 }$ for some t, $r \leqslant t \leqslant 1$ $x _ { j }$ in $K _ { j }$ . Because e is an extreme point and $t \neq 0 ,   e = x _ { 1 }$ . Thus ext $K \subseteq K _ { 1 }$ and $\dot { K = K _ { 1 } }$ , contradicting (10.4).

Let $y { \in } K \backslash C _ { r }$ The definition of $C _ { r }$ and the fact that $K = \operatorname { c o } ( K _ { 1 } \cup K _ { 2 } )$ imply $y = t x _ { 1 } + ( 1 - t ) x _ { 2 }$ with $x _ { j }$ in $K _ { j }$ and $0 \leqslant t < r .$ Hence $p ( y - x _ { 2 } ) =$ $p(t(x_1 - x_2)) = t p(x_1 - x_2) \leqslant r d,$ where $d = p - \mathrm{diam} K$ . Therefore, if $y ^ { \prime } = t ^ { \prime } x _ { 1 } ^ { \prime } +$ $(1 - t')x'_2 \in K \setminus C_r,  then   p(y - y') \leqslant p(y - x_2) + p(x_2 - x'_2) + p(x'_2 - y') \leqslant 2r\dot{d} +$ p-diam $K_{2} \leqslant 2rd + \varepsilon / 2$ Choosing $r = \varepsilon / 4 d$ and putting $C = C _ { r } .$ , we have proved the lemma. ■

10.6. Definition. Let $\mathcal { X }$ be a LCS and let $Q$ be a nonempty subset of $\mathcal { X }$ If $\mathcal { S }$ is a family of maps (not necessarily linear) of $Q$ into $Q ,$ then $\mathcal { S }$ is said to be a noncontracting family of maps if for two distinct points x and y in $Q ,$

$$
0 \not \in \mathrm { c l } \{ T ( x ) - T ( y ) : T \in \mathcal { S } \} .
$$

The next lemma has a straightforward proof whose discovery is left to the reader.

10.7. Lemma. If X is a LCS, $Q \subseteq { \mathcal { X } }$ , and $\mathcal { S }$ is a family of maps of $Q$ into $Q ,$ then $\mathcal { S }$ is a noncontracting family if and only if for every pair of distinct points x and $y$ in $Q$ there is a continuous seminorm p such that

$$
\operatorname* { i n f } \left\{ p ( T ( x ) - T ( y ) ) : T \in { \mathcal { S } } \right\} > 0 .
$$

10.8. The Ryll–Nardzewski Fixed Point Theorem. $I f \mathcal { X }$ is a LCS, Q is a weakly compact convex subset of $\mathcal { X } .$ , and $\mathcal { S }$ is a noncontracting semigroup of weakly continuous affine maps of Q into $Q ,$ then there is a point $x _ { 0 }$ in $Q$ such that $T ( x _ { 0 } )   =   x _ { 0 }$ for every $T$ in $\mathcal { S }$ 1

ProoF. The proof begins by showing that every finite subset of $\mathcal { S }$ has a common fixed point.

10.9. Claim. If $\{ T _ { 1 } , \ldots , T _ { n } \} \subseteq { \mathcal { S } }$ , then there is an $x _ { 0 }$ in $Q$ such that $T _ { k } x _ { 0 } = x _ { 0 }$ for $1 \leqslant k \leqslant n .$

Put $T _ { 0 } = ( T _ { 1 } + \cdots + T _ { n } ) / n ;$ so $T _ { 0 } : Q \to Q$ and $T _ { 0 }$ is weakly continuous and affine. By (10.1), there is an $x _ { 0 }$ in $Q$ such that $T _ { 0 } ( x _ { 0 } ) = x _ { 0 }$ . It will be shown that $T _ { k } ( x _ { 0 } ) = x _ { 0 }$ for $1 \leqslant k \leqslant n .$ In fact, if $T _ { k } ( x _ { 0 } ) \neq x _ { 0 }$ for some $k ,$ then by renumbering the $T _ { k } .$ , it can be assumed that there is an integer m such that $T _ { k } ( x _ { 0 } ) \neq x _ { 0 }$ for $1 \leqslant k \leqslant m$ and $T _ { k } ( x _ { 0 } ) = x _ { 0 }$ for $m < k \leqslant n.$ Let $T _ { 0 } ^ { \prime }   =$ $(T_1 + \cdots + T_m)/m$ Then

$$
\begin{align*}x_0 = & \; T_0(x_0) \\= & \; \frac{1}{n} \left[ T_1(x_0) + \cdots + T_m(x_0) \right] + \left( \frac{n - m}{n} \right) x_0.\end{align*}
$$

Hence

$$
\begin{aligned} T_{0}^{\prime}(x_{0}) &= \frac{1}{m}[T_{1}(x_{0}) + \cdots + T_{m}(x_{0})] \\&= \frac{n}{m}\frac{1}{n}[T_{1}(x_{0}) + \cdots + T_{m}(x_{0})] \\&= \frac{n}{m}\left[x_{0} - \left(\frac{n - m}{n}\right)x_{0}\right] \\&= x_{0}.\\ \end{aligned}
$$