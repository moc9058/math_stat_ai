Fix f in $C _ { b } ( X )$ and define $f ^ { \beta } \colon \beta X \to \mathbb { F }$ by $f ^ { \beta } ( \tau ) = \langle f , \tau \rangle$ for every $\tau$ in $\beta X$ [Remember that $\beta X \subseteq C _ { b } ( X ) ^ { * } .$ , so that this makes sense.] Clearly $f ^ { \beta }$ is continuous and $f ^ { \beta } \circ \Delta ( x ) = f ^ { \beta } ( \delta _ { x } ) = \langle f , \delta _ { x } \rangle = f ( x ) . \mathrm { S o } f ^ { \beta } \circ \Delta = f$ and (c) holds. To show that To show that $\beta X$ is unique, assume that Ω is a compact space and is unique assume that O is a comnact space and $\pi \cdot$

$X   \to   \Omega$ is a continuous map such that:

(a') $\pi \colon X   \to   \pi ( X )$ is a homeomorphism;

(b′) $\pi ( X )$ is dense in Ω;

(c') if $f   \in   { \cal C } _ { b } ( X )$ , there is an $\tilde { f }$ in C(Ω) such that $\tilde { f }   \circ   \pi = f .$

Define $g \colon \Delta ( X ) \to \Omega { \mathrm { ~ b y ~ } } g ( \Delta ( x ) ) = \pi ( x )$ In other words, $g = \pi \circ \Delta ^ { - 1 }$ . The idea is to extend g to a homeomorphism of βX onto Ω. If $\tau _ { 0 } { \in } \beta X$ , then (b) implies that there is a net $\{ x _ { i } \}$ in X such that $\Delta ( x _ { i } )   \rightarrow   \tau _ { 0 }$ in $\beta X$ . Now $\{ \pi ( \mathbf { x } _ { i } ) \}$ is a net in Ω and since Ω is compact, there is an $\omega _ { 0 }$ in Ω such that $\pi ( x _ { i } ) \xrightarrow [ \mathrm { ~ c l ~ } ] { \quad } \omega _ { 0 }$ If $F   \in   C ( \Omega )$ , let $f = F \circ \pi ;$ so $f   \in   { \cal C } _ { b } ( X )$ (and $F = \tilde { f } )$ . Also, $f(x_{i}) = \langle f, \delta_{x_{i}} \rangle \rightarrow$ $\langle f , \tau _ { 0 } \rangle = f ^ { \beta } ( \tau _ { 0 } )$ . But it is also true that $f(x_{i}) = F(\pi(x_{i})) \xrightarrow[\mathrm{c1}]{} F(\omega_{0})$ . Hence $F ( \omega _ { 0 } )   =   f ^ { \beta } ( \tau _ { 0 } )$ for any F in $C ( \Omega )$ . This implies that $\omega _ { 0 }$ is the unique cluster point of $\{ \pi ( x _ { i } ) \}$ ; thus $\pi ( x _ { i } )   \rightarrow   \omega _ { 0 } ( \mathrm { A } . 2 . 7 )$ . Let $g ( \tau _ { 0 } ) = \omega _ { 0 }$ . It must be shown that the definition of $g ( \tau _ { 0 } )$ does not depend on the net $\left\{ x _ { i } \right\}$ in $X$ such that $\Delta ( x _ { i } )   \rightarrow   \tau _ { 0 }$ . This is left as an exercise. To summarize, it has been shown that

$$
There is a function $g \colon \beta X \to \pmb { \Omega }$
$$

## 6.3

$$
such that if $f { \in } C _ { b } ( X ) , \; { \mathrm { t h e n } } \; f ^ { \beta } = { \widetilde { f } } ^ { \circ } g .$
$$

To show that g: $\beta X   \to   \Omega$ is continuous, let $\left\{ \tau _ { i } \right\}$ be a net in $\beta X$ such that $\tau _ { i }   \to   \tau .$ If $F   \in   C ( \Omega )$ , let $f = F \circ \pi;$ so $f   \in   C _ { b } ( X )$ and ${ \tilde { f } } = F .$ Also, $f ^ { \beta } ( \tau _ { i } )   \rightarrow   f ^ { \beta } ( \tau )$ But $F ( g ( \tau _ { i } ) ) = f ^ { \beta } ( \tau _ { i } ) \rightarrow f ^ { \beta } ( \tau ) = F ( g ( \tau ) )$ . It follows (6.1) that $g ( \tau _ { i } )   \rightarrow   g ( \tau )$ in Ω. Thus $g$ is continuous.

It is left as an exercise for the reader to show that $g$ is injective. Since $g ( \beta X ) \supseteq g ( \Delta ( X ) ) = \pi ( X ) , g ( \beta X )$ is dense in $\mathbf { \Omega } ,$ But $g ( \beta X )$ is compact, so $g$ is bijective. By (A.2.8), g is a homeomorphism.

The compact set $\beta X$ obtained in the preceding theorem is called the Stone-Čech compactification of X. By properties (a) and (b), X can be considered as a dense subset of $\beta X$ and the map $\Delta$ can be taken to be the inclusion map. With this convention, (c) can be interpreted as saying that every bounded continuous function on X has a continuous extension to $\beta X$

The space βX is usually very much larger than $\dot { X } .$ In particular, it is almost never tr'ue that $\beta X$ is the one-point compactification of X. For example, if $X = ( 0 , 1 ]$ , then the one-point compactification of X is [0, 1]. However, sin $( 1 / x ) { \in } C _ { b } ( X )$ but it has no continuous extension to [0, 1], so $\beta X \neq [ 0 , 1 ]$

To obtain an idea of how large $\beta X \backslash X$ is, see Exercise 6, which indicates how to show that if N has the diserete topology, then $\beta \mathbf { N } \backslash \mathbf { N }$ has $2 ^ { N _ { 0 } }$ pairwise disjoint open sets. The best source of information on the

Stone-Čech compactification is the book by Gillman and Jerison [1960], though the approach to $\beta X$ is somewhat different there than here. Two recent works on the Stone-Čech compactification are Johnstone [1982] and Walker [1974].

6.4. Corollary. if X is completely regular and $\mu { \in } M ( \beta X ) .$ define $L _ { \mu } \colon C _ { b } ( X ) \to \mathbb { F }$ by

$$
L _ { \mu } ( f ) = \int _ { \beta X } f ^ { \beta } d \mu
$$

for each f in $C _ { b } ( X )$ . Then the map $\mu { \mapsto } L _ { \mu }$ is an isometric isomorphism of $M ( \beta X )$ onto $C _ { b } ( X ) ^ { * }$

PROOF. Define $V : C _ { b } ( X ) \to C ( \beta X )$ by $V f   =   f ^ { \beta }$ . It is easy to see that V is linear. Considering X as a subset of $\beta X$ , the fact that $\beta X = \operatorname { c l } X$ implies that V is an isometry. If $g \in C ( \beta X )$ and $f   =   g |   X$ , then $g = f ^ { \beta } = V f ;$ hence V is surjective.

I $\mathbf{f} \mu \in M(\beta X) = C(\beta X)^*$ , it is easy to check that $L _ { \mu } { \in } C _ { b } ( X ) ^ { * }$ and $\| L _ { \pmb { \mu } } \| = \| \pmb { \mu } \|$ since V is an isometry. Conversely, if $L { \in } C _ { b } ( X ) ^ { * }$ , then $L \circ V ^ { - 1 } \in C ( \dot { \beta } X ) ^ { * }$ and $\| L \circ V ^ { - 1 } \| = \| L \|$ . Hence there is a μ in $M ( \beta X )$ such that $\int f g   d \mu = L \circ V ^ { - 1 } ( g )$ for every g in $C ( \beta X )$ . Since $V ^ { - 1 } g = | X |$ , it follows that $L = L _ { \mu ^ { * } }$ ■

The next result is from topology. It may be known to the reader, but it is presented here for the convenience of those to whom it is not.

6.5. Partition of Unity. If X is normal and $\{ \boldsymbol { U } _ { 1 } , \dots , \boldsymbol { U } _ { n } \}$ is an open covering $o f X .$ , then there are continuous functions $f _ { 1 } , . . . , f _ { n }$ from X into [0, 1] such that

(a) $\textstyle \sum _ { k = 1 } ^ { n } f _ { k } ( x ) = 1$ for all x in X;

(b) $f _ { k } ( x ) = 0 \; f o r \; x$ in $X \backslash U _ { \pmb { k } }$ and $1 \leqslant k \leqslant n.$

PRooF. First observe that it may be assumed that $\{ \boldsymbol { U } _ { 1 } , \dots , \boldsymbol { U } _ { n } \}$ has no proper subcover. The proof now proceeds by induction

If $n = 1$ , let $f _ { 1 } \equiv 1$ . Suppose $n = 2 .$ Then $X \backslash U _ { 1 }$ and $X \backslash U _ { 2 }$ are disjoint closed subsets of X. By Urysohn's Lemma there is a continuous function $f _ { 1 }$ $X   \rightarrow   [ 0 , 1 ]$ such that $f _ { 1 } ( x ) = 0$ for x in $X \backslash U _ { 1 }$ and $f _ { 1 } ( x )   = 1$ for x in $X \backslash U _ { 2 }$ Let $f _ { 2 } = 1 - f _ { 1 }$ and the proof of this case is complete.

Now suppose the theorem has been proved for some $n \geqslant 2$ and $\{ U _ { 1 } , \ldots , U _ { n + 1 } \}$ is an open cover of X that is minimal. Let $F = X \backslash U_{n+1};$ then F is closed, nonempty, and $F \subseteq \bigcup _ { k = 1 } ^ { n } U _ { k }$ . Let V be an open subset of X such that $F \subseteq V \subseteq \mathrm{cl} V \subseteq \bigcup_{k = 1}^{n} U_{k}$ . Since cl V is normal and $\{ U _ { 1 } \cap$ cl $V , \ldots , U _ { n } \cap$ cl $V \}$ is an open cover of cl V, the induction hypothesis implies that there are continuous functions $g _ { 1 } , \ldots , g _ { n }$ on cl V such that $\textstyle \sum _ { k = 1 } ^ { n } g _ { k } = 1$ and for $1 \leqslant k \leqslant n ,$ $0 \leqslant g _ { k } \leqslant 1$ , and $g _ { k } ( \mathrm { c l } V \backslash U _ { k } ) = 0$ . By Tietze's Extension Theorem there are continuous functions $\tilde { g } _ { 1 } , \dots , \tilde { g } _ { n }$ on X such that $\tilde { g } _ { \boldsymbol { k } } = g _ { \boldsymbol { k } }$ on cl V and $0 \leqslant \tilde { g } _ { k } \leqslant 1$ for $1 \leqslant k \leqslant n .$

Also, there is a continuous function h: $X   \to   [ 0 , 1 ]$ such that $h   =   0$ on $X \backslash V$ and $h = 1$ on F. Put $f _ { k } = \tilde { g } _ { k } h$ for $1 \leqslant k \leqslant n$ and let $f_{n + 1} = 1 - \sum_{k = 1}^{n} f_{k}$ Clearly $0 \leqslant f _ { k } \leqslant 1$ if $1 \leqslant k \leqslant n$ .If x∈cl V, then $f_{n + 1}(x) = 1 - \left( \sum_{k = 1}^{n} g_{k}(x) \right) h(x) = 1 -$ h(x); so $0 \leqslant f_{n + 1}(x) \leqslant 1$ on cl V. If $x { \in } X \backslash V ,$ then $f _ { n + 1 } ( x ) = 1$ since $h ( x ) = 0$ Hence $0 \leqslant f_{n + 1} \leqslant 1$

Clearly (a) holds. Let $1 \leqslant k \leqslant n;$ if $x { \in } X \backslash U _ { k } ,$ then either $x \in ( \operatorname { c l } V ) \setminus U _ { k }$ or $x \in (X \setminus \mathrm{cl} V) \setminus U_k$ If the first alternative is the case, then $g _ { k } ( x ) = 0 ,$ sO $f _ { k } ( x ) = 0 .$ If the second alternative is true, then $h ( x ) = 0$ so that $f _ { k } ( x ) = 0$ If $x \in X \setminus U_{n+1} = F$ , then $h ( x )   = 1$ and so $f_{n + 1}(x) = 1 - \sum_{k = 1}^{n}g_{k}(x) = 0.$ ■

Partitions of unity are a standard way to put together local results to obtain global results. If $\{ f _ { k } \}$ is related to $\{ U _ { k } \}$ as in the statement of (6.5) then $\{ f _ { k } \}$ is said to be a partition of unity subordinate to the cover $\{ U _ { k } \}$

6.6. Theorem. If X is completely regular, then $C _ { b } ( X )$ is separable if and only if X is a compact metric space.

ProoF. Suppose X is a compact metric space with metric d. For each $n ,$ let $\left\{ U_{k}^{(n)}: 1 \leqslant k \leqslant N_{n} \right\}$ be an open cover of X by balls of radius $1 / n .$ Let $\left\{ f _ { k } ^ { ( n ) } : 1 \leqslant k \leqslant N _ { n } \right\}$ be a partition of unity subordinate to $\left\{ U _ { k } ^ { ( n ) } : 1 \leqslant k \leqslant N _ { n } \right\}$ Let @ be the rational (or complex-rational) linear span of $\left\{ f _ { k } ^ { ( n ) } : n \geqslant \stackrel { \cdot } { 1 } \right.$ $1 \leqslant k \leqslant N _ { n } \}$ ; thus $\mathcal { Y }$ is countable. It will be shown that $\theta$ is dense in C(X).

Fix f in C(X) and $\varepsilon   >   0 .$ Since f is uniformly continuous there is a $\delta   >   0$ such that $| f ( x _ { 1 } ) - f ( x _ { 2 } ) | < \varepsilon / 2$ whenever $d ( x _ { 1 } , x _ { 2 } )   <   \delta .$ Choose $n > 2 / \delta$ and consider the cover $\{ U _ { k } ^ { ( n ) } : 1 \leqslant k \leqslant N _ { n } \} , \mathrm { I f } x _ { 1 } , x _ { 2 } \in U _ { k } ^ { ( n ) } , d ( x _ { 1 } , x _ { 2 } ) < 2 / n < \delta ;$ hence $| f ( x _ { 1 } ) - f ( x _ { 2 } ) | < \varepsilon / 2$ Pick $x _ { k }$ in $U _ { k } ^ { ( n ) }$ and let $\alpha _ { k } \in \mathbb { Q } + i \mathbb { Q }$ such that $| \alpha _ { k } - f ( x _ { k } ) | < \varepsilon / 2$ Let $\begin{array} { r } { \boldsymbol { g } = \sum _ { \boldsymbol { k } } \alpha _ { \boldsymbol { k } } f _ { \boldsymbol { k } } ^ { ( n ) } } \end{array}$ , so $g \in \mathcal { Y }$ .Therefore for every x in X,

$$
\begin{aligned}\left| f(x) - g(x) \right| &= \left| \sum_{k} f(x) f_{k}^{(n)}(x) - \sum_{k} \alpha_{k} f_{k}^{(n)}(x) \right| \\& \leqslant \sum_{k} \left| f(x) - \alpha_{k} \right| f_{k}^{(n)}(x).\end{aligned}
$$

Examine each of these summands. If $x   \in   U _ { k } ^ { ( n ) } ,$ then $| f ( x ) - \alpha _ { k } | \leqslant | f ( x ) -$ $| f ( x _ { k } ) | + | f ( x _ { k } ) - \alpha _ { k } | < \varepsilon .$ If $x   \not \in   U _ { k } ^ { ( n ) }$ , then $f_{k}^{(n)}(x) = 0.$ Hence $| f ( x ) - g ( x ) | <$ $\begin{array} { r } { \sum _ { k } \varepsilon f _ { k } ^ { ( n ) } ( x ) = \varepsilon . } \end{array}$ Thus $\| f - g \| < \varepsilon$ and $\pmb { \mathscr { y } }$ is dense in C(X). This shows that C(X) is separable.

Now assume that $C _ { b } ( X )$ is separable. Thus (ball $C _ { b } ( X ) ^ { * } , \mathrm { w k } ^ { * } )$ is metrizable (5.1). Since X is homeomorphic to a subset of ball $C _ { b } ( X ) ^ { * }   ( 6 . 1 ) ,$ , X is metrizable. It also follows that $\beta X$ is metrizable. It must be shown that $X = \beta X$

Suppose there is a τ in $\beta X \backslash X$ Let $\{ x _ { n } \}$ be a sequence in X such that $x _ { n }   \to   \tau .$ It can be assumed that $x _ { n } \neq x _ { m }$ for $n \neq m .$ Let $A = \{ x _ { n } \}$ n is even} and $B = \left\{ x _ { n } \right\}$ n is odd}. Then A and B are disjoint closed subsets of X (not closed in $\beta X$ , but in X) since A and B contain all of their limit points in X. Since X is normal, there is a continuous function $f \colon X   \to   [ 0 , 1 ]$ such that $f   =   0$ on A and $f = 1$ on B. But then $f ^ { \beta } ( \tau ) = \lim f ( x _ { 2 n } ) = 0$ and $f^{\beta}(\tau) = \lim_{n \to \infty} f(x_{2n+1}) =$ 1, a contradiction. Thus $\beta X \backslash X = \Box$

## EXERCISES

1. If $x   \in   X$ and $\delta _ { x } ( f )   =   f ( x )$ for all f in $C _ { b } ( X ) .$ , show that $\| \delta _ { x } \| = 1$

2. Prove that a subset of a completely regular space is completely regular.

3. Fill in the details of the proof of Theorem 6.2.

4. If X is completely regular, Ω is compact, and $f \colon X   \to   \Omega$ is continuous, show that there is a continuous map $f ^ { \beta } \colon \beta X   \to   \Omega$ such that $f ^ { \pmb { \beta } } | X = f .$

5. If X is completely regular, show that X is open in βX if and only if X is locally compact.

6. Let N have the discrete topology. Let $\{ r _ { n } : n \in \mathbb { N } \}$ be an enumeration of the rational numbers in [0, 1]. Let S = the irrational numbers in [0, 1] and for each s in S let $\{ r _ { n } ; n { \in } N _ { s } \}$ be a subsequence of $\{ r _ { n } \}$ such that $s = \lim \left\{ r_{n} : n \in N_{s} \right\}$ . Show: (a) if $s , t   \in   \mathbb { S }$ and $s \neq t ,   N _ { s }   \cap   N _ { t }$ is finite; (b) if for each s in S, cl $N _ { s }   =   \mathsf { t h e }$ closure of $N _ { s }$ in $\beta \mathbf { N }$ and $A _ { s } = ( \mathrm { c l } N _ { s } ) \backslash \mathbb { N } ,$ then $\{ A _ { s } ; s { \in } S \}$ are pairwise disjoint subsets of $\beta \mathbf { N } \backslash \mathbf { N }$ that are both open and closed.

7. Show that if X is normal, $\tau   \in   \beta X$ , and there is a sequence $\{ x _ { n } \}$ in X such that $x _ { n }   \to   \tau$ in $\beta X$ , then $\tau   \in   X$ . If X is not normal, is the result still true?

8. Let X be the space of all ordinals less than the first uncountable ordinal and give X the order topology. Show that $\beta X = \mathrm{the}$ one point compactification of X. (You can find the pertinent definitions in Kelley [1955].)

## §7. The Krein-Milman Theorem

7.1. Definition. If K is a convex subset of a vector space $\mathcal { X } ,$ then a point a in K is an extreme point of K if there is no proper open line segment that contains a and lies entirely in K. Let ext K be the set of extreme points of K.

Recall that an open line segment is a set of the form $(x_{1},x_{2}) \equiv \{tx_{2}+$ $(1 - t)x_{1}:0 < t < 1$ , and to say that this line segment is proper is to say that $x _ { 1 } \neq x _ { 2 }$

## 7.2. Examples.

(a) If $\mathcal { X } = \mathbb { R } ^ { 2 }$ and $K = \left\{ (x,y) \in \mathbb{R}^2 : x^2 + y^2 \leqslant 1 \right\}$ , then ext $K = \{ ( x , y ) \}$ $x ^ { 2 } + y ^ { 2 } = 1 \}$

(b) If $\mathcal { X } = \mathbb { R } ^ { 2 }$ and $K = \left\{ (x,y) \in \mathbb{R}^2 : x \leq 0 \right\}$ , then ext $K = \bigsqcup$

(c) If $\mathcal { X }   =   \mathbb { R } ^ { 2 }$ and $K = \left\{ (x,y) \in \mathbb{R}^2 : x < 0 \right\} \cup \left\{ (0,0) \right\}$ , then ext $K = \{ ( 0 , 0 ) \}$

(d) If K = the closed region in $\mathbb { R } ^ { 2 }$ bordered by a regular polygon, then ext K = the vertices of the polygon.

(e) If x is any normed space and $K = \left\{ x \in \mathcal { X } : \| x \| \leqslant 1 \right\}$ , then ext $K \subseteq$

$\left\{ x \colon \left\|   x   \right\| = 1 \right\}$ , though for all we know it may be that ext $K = \bigtriangleup$

(f) if $\mathcal { X } = L ^ { 1 } [ 0 , 1 ]$ and $K = \left\{ f { \in } L ^ { 1 } [ 0 , 1 ] { : } \| f \| _ { 1 } \leqslant 1 \right\}$ , then ext $K = \bigtriangleup$ . This last statement requires a bit of proof. Let $f { \in } L ^ { 1 } [ 0 , 1 ]$ such that $\| f \| _ { 1 } = 1$ Choose x in [0, 1] such that $\int_{0}^{x} \left| f(t) \right| dt = \frac{1}{2}$ . Let $\boldsymbol { h } ( t ) = 2 \boldsymbol { f } ( t )$ if $t \leqslant x$ and 0 otherwise; let $g(t) = 2f(t)   if   t \geqslant x$ and 0 otherwise. Then $\| h \| _ { 1 } = \| g \| _ { 1 } = 1$ and $f   =   \frac { 1 } { 2 } ( h + g )$ . So ball $L ^ { 1 } [ 0 , 1 ]$ has no extreme points.

The next proposition is left as an exercise.

7.3. Proposition. If K is a convex subset of a vector space X and $a   \in   K$ , then the following statements are equivalent.

(a) a∈ext K.

(b) $I f x _ { 1 } , x _ { 2 } \in \mathcal { X }$ and $a = \frac { 1 } { 2 } ( x _ { 1 } + x _ { 2 } )$ , then either $x _ { 1 } \notin K$ or $x _ { 2 } \notin K$ or $x _ { 1 } = x _ { 2 } = a .$

(c) $I f x _ { 1 } , x _ { 2 } \in \mathcal { X } , 0 < t < 1$ , and $a = t x _ { 1 } + ( 1 - t ) x _ { 2 }$ , then either $x _ { 1 } { \notin } K ,   x _ { 2 } { \notin } K .$ or $x _ { 1 } = x _ { 2 } = a .$

(d) $I f   x _ { 1 } , \ldots , x _ { n } { \in } K$ and a∈co $\{ x _ { 1 } , \ldots , x _ { n } \}$ , then $a = x _ { k }   f _ { } { o r }$ some k.

(e) $K \backslash \{ a \}$ is a convex set.

7.4. The Krein-Milman Theorem. If K is a nonempty compact convex subset of a LCS X, then ext $K \neq \square$ and $K = \overline{\mathrm{co}}(\mathrm{ext} K)$

ProoF. (Léger [1968].) Note that (7.3e) says that a point a is an extreme point if and only if $K \backslash \{ a \}$ is a relatively open convex subset. We thus look for a maximal proper relatively open convex subset of K. Let u be all the proper relatively open convex subsets of K. Since ¿ is a LCS and $K \neq \square$ (and let's assume that K is not a singleton), $\mathcal { U } \neq \square$ . Let $\mathcal { U } _ { 0 }$ be a chain in U and put $U _ { 0 } = \cup \left\{ U { : } U { \in } \mathcal { U } _ { 0 } \right\}$ . Clearly $U _ { 0 }$ is open, and since $\mathcal { U } _ { 0 }$ is a chain, $U _ { 0 }$ is convex. If $U _ { 0 } = K$ , then the compactness of K implies that there is a U in $\mathcal { U } _ { 0 }$ with $U = K ,$ a contradiction to the property of U. Thus $U _ { 0 }   \in   \mathcal { U }$ .By Zorn's Lemma, @ has a maximal element U.

If $x   \in   K$ and $0 \leqslant i \leqslant 1$ , let $T _ { x , \lambda } \colon K \to K$ be defined by $T _ { x , \lambda } ( y ) = \lambda y + ( 1 - \lambda ) x$ Note that $T _ { \mathbf { x } , \lambda }$ is continuous and $T_{x,\lambda}(\sum_{j = 1}^{n} \alpha_{j} y_{j}) = \sum_{j = 1}^{n} \alpha_{j} T_{x,\lambda}(y_{j})$ whenever $y_{1},\ldots,y_{n}\in K,\alpha_{1},\ldots,\alpha_{n}\geqslant0.$ and $\textstyle \sum _ { j = 1 } ^ { n } \alpha _ { j }   \stackrel { \circ } { = } 1$ . (This means that $T _ { \mathbf { x } , \lambda }$ is an affine map of K into K.) If $x   \in   U$ and $0 \leq \lambda < 1$ , then $T _ { x , \lambda } ( U ) \subseteq U$ Thus $\overline { { U } } \subseteq T _ { x , \lambda } ^ { - 1 } ( U )$ and $T _ { x , \lambda } ^ { - 1 } ( U )$ is an open convex subset of K. If $y \in ( \mathrm { c l } U ) \backslash U ,   T _ { x , \lambda } ( y ) \in [ x , y ) \subseteq U$ by Proposition IV.1.11. So cl $U \subseteq T _ { x , \lambda } ^ { - 1 } ( U )$ and hence the maximality of U implies $T _ { x , \lambda } ^ { - 1 } ( U ) = K$ . That is,

$$
T _ { x , \lambda } ( K ) \subseteq U \quad \mathrm { i f } \quad x \in U \quad \mathrm { a n d } \quad 0 \leqslant \lambda < 1 .
$$

Claim. If V is any open convex subset of K, then either $V \cup U = U$ or $V \cup U = K$

In fact, (7.5) implies that $V \cup U$ is convex so that the claim follows from the maximality of U.

It now follows from the claim that $K \backslash U$ is a singleton. In fact, if a $, b { \in } K \backslash U$ and $a \neq b$ , let $V _ { a } , V _ { b }$ be disjoint open convex subsets of K such that $a   \in   V _ { a }$ and $b   \in   V _ { b }$ . By the claim $V _ { a } \cup U = K$ since a∉U. But b∉ $V _ { a } \cup U$ ,a contradiction. Thus $K \backslash U = \{ a \}$ and a∈ext K by (7.3e). Hence ext $K \neq \square$

Note that we have actually proved the following

## 7.6 If V is an open convex subset of $\mathcal { X }$ and ext $K \subseteq V ,$ then $K \subseteq V .$

Assume (7.6) is false. That is, assume there is an open convex subset V of X such that ext $K \subseteq V$ but $V   \cap   K \neq K$ Then $V   \cap   K   \in   \mathcal { U }$ and is contained in a maximal element U of U. Since $K \backslash U = \left\{ a \right\}$ for some a in ext K, this is a contradiction. Thus (7.6) holds

Let $E = \overline { { \mathrm { c o } } } ( \mathrm { e x t }   K )$ . If $x ^ { * } { \in } { \mathcal { X } } ^ { * } , \; { \mathfrak { a } } { \in } { \mathbb { R } }$ , and $E \subseteq \{ x \in { \mathcal { X } } \colon \operatorname { R e } \langle x , x ^ { * } \rangle < \alpha \} = V ,$ then $K \subseteq V$ by (7.6). Thus the Hahn-Banach Theorem (IV.3.13) implies $E = K$ ■

The Krein-Milman Theorem seems innocent enough, but it has widespread application. Two such applications will be seen in Sections 8 and 10; another will occur later when $C ^ { * }$ -algebras are studied. Here a small application is given.

If $\mathcal { X }$ is a Banach space, then ball $\mathcal { X } ^ { * }$ is weak\* compact by Alaoglu's Theorem. By the Krein-Milman Theorem, ball $\mathcal { X } ^ { * }$ has many extreme points. Keep this in mind.

7.7. Example. $c _ { 0 }$ is not the dual of a Banach space. That is, $c _ { 0 }$ is not isometrically isomorphic to the dual of a Banach space. In light of the preceding comments, in order to prove this statement, it suffices to show that ball $c _ { 0 }$ has few extreme points. In fact, ball $c _ { 0 }$ has no extreme points. Let x∈ball $c _ { 0 }$ It must be that $0 = \lim_{} x(n)$ . Let N be such that $| x ( n ) | < \frac { 1 } { 2 }$ for $n \geqslant N$ Define $y _ { 1 } , y _ { 2 }$ in $c _ { 0 }$ by letting $y_{1}(n) = y_{2}(n) = x(n)$ for $n \leqslant N .$ , and for $n > N$ let $y _ { 1 } ( n ) = x ( n ) + 2 ^ { - n }$ and $y _ { 2 } ( n ) = x ( n ) - 2 ^ { - n }$ . It is easy to check that $y _ { 1 }$ and $y_{2} \in \mathrm{ball} c_{0}, \frac{1}{2}(y_{1} + y_{2}) = x,$ and $y _ { 1 } \neq x$

In light of Example 7.2(f), $L ^ { 1 } [ 0 , 1 ]$ is not the dual of a Banach space.

The next two results are often useful in applying the Krein-Milman Theorem. Indeed, the first is often taken as part of that result.

7.8. Theorem. If X is a LCS, K is a compact convex subset of $\mathcal { X } ,$ and $F \subseteq K$ such that $K = { \overline { { \mathbf { c o } } } } ( F ) .$ , then ext $K \subseteq \operatorname { c l } F$

ProoF. Clearly it suffices to assume that F is closed. Suppose that there is an extreme point $x _ { 0 }$ of K such that $x _ { 0 } \not \in F$ . Let p be a continuous seminorm on $\mathcal { X }$ such that $F \cap \left\{ x \in \mathcal { X } : p ( x - x _ { 0 } ) < 1 \right\} = \square$ Let $U _ { 0 } = \{ x \in \mathcal { X } : p ( x ) < \frac { 1 } { 3 } \}$ . So $( \boldsymbol { x } _ { 0 } + \boldsymbol { U } _ { 0 } )   \cap   ( \boldsymbol { F } + \boldsymbol { U } _ { 0 } ) = \Box .$ hence $x _ { 0 } { \notin } { \bf c l } ( F + U _ { 0 } )$

Because F is compact, there are $y _ { 1 } , \ldots , y _ { n }$ in F such that $F \subseteq \bigcup_{k = 1}^{n} (y_{k} + U_{0})$ Let $K _ { k } = \overline { { \mathrm { c o } } } \left( F \cap \left( y _ { k } + U _ { 0 } \right) \right)$ . Thus $K _ { k } \subseteq y _ { k } + \mathrm { c l } \; U _ { 0 } \; ( \mathrm { W h y } ) .$ and $K _ { k } \subseteq K$ . Now that fact that $K _ { 1 } , \ldots , K _ { n }$ are compact and convex implies that co $( K _ { 1 } \cup \cdots \cup K _ { n } ) =$ co $( K _ { 1 } \cup \cdots \cup K _ { n } )$ (Exercise 8). Therefore

$$
K = \overline{\mathrm{co}}(F) = \mathrm{co}(K_1 \cup \cdots \cup K_n).
$$

Since $x _ { 0 }   \in   { \pmb K } , x _ { 0 }   =   \sum _ { k = 1 } ^ { n } \alpha _ { k } x _ { k } , x _ { k }   \in   { \pmb K } _ { k } , \alpha _ { k }   \geqslant   0 , \alpha _ { 1 }   +   \cdots   +   \alpha _ { n }   =   1$ . But $x _ { 0 }$ is an extreme point of K. Thus, $x _ { 0 } = x _ { k } { \in } K _ { k }$ for some k. But this implies that $x _ { 0 } \in K _ { k } \subseteq y _ { k } + \mathrm { c l } U _ { 0 } \subseteq \mathrm { c l } ( F + U _ { 0 } )$ , a contradiction. ■

You might think that the set of extreme points of a compact convex subset would have to be closed. This is untrue even if the LCS is finite dimensional, as Figure V-1 illustrates.

![](images/page_158_image_4.jpg)

Figure V-1

7.9. Proposition. If K is a compact convex subset of a LCS $\mathcal { X } , \mathcal { Y }$ is a LCS, and T: $K   \rightarrow   \mathcal { Y }$ is a continuous affine map, then $T ( K )$ is a compact convex subset of Y and $i f y$ is an extreme point of $T ( K )$ , then there is an extreme point x of K such that $T ( x ) = y$

PROOF. Because T is affine, $T ( K )$ is convex and it is compact by the continuity of T. Let y be an extreme point of $T ( K )$ . It is easy to see that $T ^ { - 1 } ( y )$ is compact and convex. Let x be an extreme point of $T ^ { - 1 } ( y )$ . It now follows that x∈ext K (Exercise 9).

Note that it is possible that there are extreme points x of K such that $T ( x )$ is not an extreme point of $T ( K )$ . For example, let $T$ be the orthogonal projection of $\mathbb { R } ^ { 3 }$ onto $\bar { \mathbb { R } } ^ { 2 }$ and let $K = \mathrm{bal}   \mathbb{R}^3$

## EXERCISES

1. If $( X , \Omega , \mu )$ is a σ-finite measure space and $1 < p < \infty$ , then the set of extreme points of ball $L ^ { p } ( \mu )$ is $\{ f \in L ^ { p } ( \mu ) : \| f \| _ { p } = 1 \}$

2. If $( X , \Omega , \mu )$ is a σ-finite measure space, the set of extreme points of ball $L ^ { 1 } ( \mu )$ is $\{ \alpha \chi _ { E } : E$ is an atom of µ, α∈F, and $| \alpha |   =   \mu ( E ) ^ { -   1 } \}$

3. If $( X , \Omega , \mu )$ is a σ-finite measure space, the set of extreme points of ball $L ^ { \infty } ( \mu )$ is $\left\{ f { \in } L ^ { \infty } ( \mu ) { : } | f ( x ) | = 1 { \mathrm { ~ a . e . ~ } } [ \mu ] \right\}$

4. If X is completely regular, the set of extreme points of ball $C _ { b } ( X )$ is $\{ f   \in   { \cal C } _ { b } ( X ) \}$ $| f ( x ) | = 1$ for all $x \}$ . So ball $C _ { \mathbb { R } } [ 0 , 1 ]$ has only two extreme points.

5. Let X be a totally disconnected compact space. (That is, X is compact and if $x   \in   X$ and U is an neighborhood of x, then there is a subset V of X that is both open and closed and such that $x   \in   { \pmb V }   \subseteq   { \pmb U }$ . The Cantor set is an example of such a space.) Show that ball $C ( X )$ is the norm closure of the convex hull of its extreme points. (If $\mathbf { F } = \mathbf { C } ,$ the result is true for all compact Hausdorff spaces X (Phelps [1965]). If $\mathbf { F }   =   \mathbf { R }$ , then this characterizes totally disconnected compact spaces (Goodner [1964]).)

6. Show that ball $l ^ { 1 }$ is the norm closure of the convex hull of its extreme points.

7. Show that if X is locally compact but not compact, then ball $C _ { 0 } ( X )$ has no extreme points.

8. If $\mathcal { X }$ is a LCS and $K _ { 1 } , \ldots , K _ { n }$ are compact convex subsets of $\mathcal { X } ,$ then $\overline{\mathrm{co}}(K_1 \cup \cdots \cup K_n) = \mathrm{co}(K_1 \cup \cdots \cup K_n)$ and this convex hull is compact.

9. Let K be convex and let $T \colon K   \to   { \mathcal { Y } }$ be an affine map. If y is an extreme point of $T ( K )$ and x is an extreme point of $T ^ { -   1 } ( y )$ , then x is an extreme point of K.

10. If ª is a Hilbert space and either T or $T ^ { * }$ is an isometry, show that T is an extreme point of the closed unit ball of $\mathcal { B } ( \mathcal { H } )$ (The converse of this is also true, but it may be hard unless you use the Polar Decomposition of operators (VIII.3.11).)

## §8. An Application: The Stone-Weierstrass Theorem

If $f \colon X   \to   \mathbb { C }$ is a function, then $\bar { f }$ denotes the function from X into C whose value at each x is the complex conjugate of $f(x), \widehat{f(x)}$

8.1. The Stone-Weierstrass Theorem. If X is compact and  is a closed subalgebra of C(X) such that:

(a) $1 \in \mathcal { A } ;$

(b) ${ \it i f ~ } x , y { \in } X$ and $x \neq y ,$ then there is an f in $\varkappa$ such that $f(x) \neq f(y);$

(c) ${ \it i f } \; f { \in } { \mathcal { A } } ,$ then $\bar { f } \in \mathcal { A } ;$

then ${ \mathcal { A } } = C ( X )$

If C(X) is the algebra of continuous functions from X into $\mathbf { R } ,$ then condition (c) is not needed. Also, an algebra in $C ( X )$ that has property (b) is said to separate the points of X (see Exercise 1).

The proof of this result that will be presented here makes use of the Krein-Milman Theorem and is due to L. de Branges [1959].

PROOF OF THE STONE-WEIERSTRASS THEOREM. To prove the theorem it suffices to show that $\mathcal { A } ^ { \perp } = ( 0 )$ (III.6.14). Suppose $\mathcal { A } ^ { \perp } \neq ( 0 )$ . By Alaoglu's Theorem, ball $\alpha ^ { \perp }$ is weak\* compact. By the Krein-Milman Theorem, there is an extreme point $\mu$ of ball $\mathcal { A } ^ { \perp }$ . Let K = the support of $\mu .$ That is,

$$
K = X \setminus \bigcup \{ V \colon V { \mathrm { ~ i s ~ o p e n ~ a n d ~ } } | \mu | ( V ) = 0 \} .
$$

Hence $| \mu | ( X \backslash K ) = 0$ and $\int f d \mu = \int _ { K } f d \mu$ for all continuous functions $f$ on X. Since $\mathcal { A } ^ { \perp } \neq ( 0 )$ $\| \mu \| = 1$ and $K \neq \bigtriangleup$ . Fix $x _ { 0 }$ in $K .$ It will be shown that $K = \left\{ x _ { 0 } \right\}$