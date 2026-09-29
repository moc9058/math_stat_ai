on $\mathcal { X }$ defined by the seminorms $\left\{ p _ { 1 } , p _ { 2 } , \ldots \right\}$ . Thus a LCS is metrizable if and only if its topology is determined by a countable family of seminorms.

PRooF. It is left as an exercise for the reader to show that d is a metric and induces the same topology as $\{ p _ { n } \}$ . If $\mathcal { X }$ is a LCS and its topology is determined by a countable family of seminorms, it is immediate that $\mathcal { X }$ is metrizable. For the converse, assume that ¿ is metrizable and its metric is $\rho .$ Let $U _ { n } = \{ x : \rho ( x , 0 ) < 1 / n \}$ Because $\mathcal { X }$ is locally convex, there are continuous seminorms $q _ { 1 } , \ldots , q _ { k }$ and positive numbers $\varepsilon _ { 1 } , \ldots , \varepsilon _ { k }$ such that $\bigcap _ { j = 1 } ^ { k } \left\{ x : q _ { j } ( x ) < \varepsilon _ { j } \right\} \subseteq U _ { n } .$ If $p _ { n } = \varepsilon _ { 1 } ^ { - 1 } q _ { 1 } + \cdots + \varepsilon _ { k } ^ { - 1 } q _ { k } ,$ then $x { \in } U _ { n }$ whenever $p _ { n } ( x ) < 1$ . Clearly, $p _ { n }$ is continuous for each n. Thus if $x _ { j }   \to   0$ in $\mathcal { X } ,$ then for each n, $p _ { n } ( x _ { j } )   \to   0$ as $j   \rightarrow   \infty$ . Conversely, suppose that for each $n ,$ $p _ { n } ( x _ { j } )   \to   0$ as $j   \to   \infty$ . If $\varepsilon   >   0 ,$ let $n > \varepsilon ^ { - 1 }$ . Then there is a $j _ { 0 }$ such that for $j \geqslant j _ { 0 } , p _ { n } ( x _ { j } ) < 1$ . Thus, for $j \geqslant j_{0}, x_{j} \in U_{n} \subseteq \{x: \rho(x, 0) < \varepsilon\}$ . That is, $\rho ( x _ { j } , 0 ) < \varepsilon$ for $j \geqslant j _ { 0 }$ and so $x _ { j }   \rightarrow   0$ in $\mathcal { X } .$ This shows that $\{ p _ { n } \}$ determines the topology on X. (Why?) ■

2.2. Example. If C(X) is as in Example 1.5, then C(X) is metrizable if and only if $X = \bigcup _ { n = 1 } ^ { \infty } K _ { n } .$ , where each $K _ { n }$ is compact, $K _ { 1 } \subseteq K _ { 2 } \subseteq \cdots$ , and if K is any compact subset of X, then $K \subseteq K _ { n }$ for some n.

2.3. Example. If X is locally compact and $C ( X )$ is as in Example 1.5, then C(X) is metrizable if and only if X is σ-compact (that is, X is the union of a sequence of compact sets). If H(G) is as in Example 1.6, then H(G) is metrizable.

If $\mathcal { X }$ is a vector space and d is a metric on $\mathcal { X } ,$ say that $d$ is translation invariant if $d(x + z, y + z) = d(x, y)$ for all $x , y , z$ in $\mathcal { X }$ .Note that the metric defined by a norm as well as the metric defined in (2.1) are translation invariant.

2.4. Definition. A Fréchet space is a TVS £ whose topology is defined by a translation invariant metric d and such that $( \mathcal { X } , d )$ is complete.

It should be pointed out that some authors include in the definition of a Fréchet space the assumption that £ is locally convex.

2.5. Definition. If X is a TVS and $B \subseteq { \mathcal { X } }$ , then B is bounded if for every open set U containing 0, there is an $\varepsilon   >   0$ such that $\varepsilon B \subseteq U$

If $\mathcal { X }$ is a normed space, then it is easy to see that a set B is bounded if and only if sup $\{ \parallel   b   \parallel :   b { \in } B \} < \infty$ , so the definition is intuitively correct.

Also, notice that if $\| \cdot \|$ is a norm, $\left\{ x \colon \|   x   \| < 1 \right\}$ is itself bounded. This is not true for seminorms. For example, if C(R) is topologized as in (1.5), let $p(f) = \sup \left\{ \left| f(t) \right| : 0 \leqslant t \leqslant 1 \right\}$ . Then $p$ is a continuous seminorm. However, $\left\{ f \colon p ( f ) < 1 \right\}$ is not bounded. In fact, $\mathbf { i } \mathbf { f } _ { 0 }$ is any function in $C ( \mathbb { R } )$ that vanishs on $[ 0 , 1 ] , \{ \alpha f _ { 0 } \colon \alpha { \in } \mathbb { R } \} \subseteq \{ f \colon p ( f ) < 1 \}$ . The fact that a normed space posseses a bounded open set is characteristic.

2.6. Proposition. If X is a LCS, then $\mathcal { X }$ is normable if and only if X has a nonempty bounded open set.

ProoF. It has already been shown that a normed space has a bounded open set. So assume that $\mathcal { X }$ is a LCS that has a bounded open set U. It must be shown that there is norm on $\mathcal { X }$ that defines the same topology. By translation, it may be assumed that $0   \in   U$ (see Exercise 4i). By local convexity, there is a continuous seminorm p such that $\{ x : p ( x ) < 1 \} \equiv V \subseteq U ( \mathrm { W h y ? } )$ . It will be shown that p is a norm and defines the topology on $\mathcal { X }$

To see that $p$ is a norm, suppose that $x { \in } { \mathcal { X } }   ,   x \neq 0 .$ Let $W _ { 0 } ,   W _ { x }$ be disjoint open sets such that $0   \in   \mathbb { W } _ { 0 }$ and $x   \in   \mathbb { W } _ { \pmb { x } }$ . Then there is an $\varepsilon   >   0$ such that $W _ { 0 } \supseteq \varepsilon U \supseteq \varepsilon V$ . But 8 $V = \{ y : p ( y ) < \varepsilon \}$ . Since x∉ $W _ { 0 } , p ( x ) \geqslant \varepsilon .$ Hence $p$ is a norm.

Because p is continuous on $\mathcal { X } ,$ to show that p defines the topology of $\mathcal { X }$ it suffices to show that if $q$ is any continuous seminorm on $\mathcal { X } ,$ there is an $\alpha   >   0$ such that $q \leqslant \alpha p ( \mathrm { W h y ? } )$ . But because $q$ is continuous, there is an $\varepsilon   >   0$ such that $\{ x \colon q ( x ) < 1 \} \supseteq \varepsilon U \supseteq \varepsilon V$ . That is, $p ( x ) < \varepsilon$ implies $q ( x ) < 1$ . By Lemma III.1.4, $q \leqslant \varepsilon ^ { -   1 } p .$ ■

## EXERCISES

1. Supply the missing details in the proof of Proposition 2.1.

2. Verify the statements in Example 2.2.

3. Verify the statements in Example 2.3.

4. Let $\mathcal { X }$ be a TVS and prove the following: (a) If B is a bounded subset of $\mathcal { X } ,$ then so is cl B. (b) The finite union of bounded sets is bounded. (c) Every compact set is bounded. (d) If $B \subseteq { \mathcal { X } }$ , then B is bounded if and only if for every sequence $\{ x _ { n } \}$ contained in B and for every $\{ \alpha _ { n } \}$ in $c _ { 0 } ,   \alpha _ { n } x _ { n }   \rightarrow   0$ in X. (e) If $\pmb { y }$ is a TVS, T: X → y is a continuous linear transformation, and B is a bounded subset of $\mathcal { X } ,$ then $T ( B )$ is a bounded subset of Y. (f) If X is a LCS and $B \subseteq { \mathcal { X } }$ , then B is bounded if and only if for every continuous seminorm p, sup{p(b): $b   \in   \mathbf { B } \} < \infty$ . (g) If $\mathcal { X }$ is a normed space and $B \subseteq { \mathcal { X } }$ , then B is bounded if and only if sup $\left\{ \left\|   b   \right\| :   b { \in } B \right\} < \infty .$ (h) If x is a Fréchet space, then bounded sets have finite diameter, but not conversely. (i) The translate of a bounded set is bounded.

5. If X is a LCS, show that X is metrizable if and only if $\mathcal { X }$ is first countable. Is this equivalent to saying that {0} is a $G _ { \delta }$ set?

6. Let X be a locally compact space and give $C _ { b } ( X )$ the strict topology defined in Exercise 1.21. Show that a subset of $C _ { b } ( X )$ is $\beta .$ -bounded if and only if it is norm bounded.

7. With the notation of Exercise 6, show that $( C _ { b } ( X ) , \beta )$ is metrizable if and only if X is compact.

8. Prove the Open Mapping Theorem for Fréchet spaces.

## §3. Some Geometric Consequences of the Hahn-Banach Theorem

In order to exploit the Hahn-Banach Theorem in the setting of a LCS, it is necessary to establish some properties of continuous linear functionals. The proofs of the relevant propositions are similar to the proofs of the corresponding facts about linear functionals on normed spaces given in §III.5. For example, a hyperplane in a TVS is either closed or dense (see III.5.2). The proof of the next fact is similar to the proof of (III.2.1) and (III.5.3) and will not be given.

3.1. Theorem. If X is a TVS and $f \colon { \mathcal { X } }   \to   \mathbb { F }$ is a linear functional, then the following statements are equivalent.

(a) f is continuous.

(b) f is continuous at 0.

(c) f is continuous at some point.

(d) ker f is closed.

(e) $x   \mapsto   | f ( x ) |$ is a continuous seminorm.

If X is a LCS and P is a family of seminorms that defines the topology on X, then the statements above are equivalent to the following:

(f) There are $p _ { 1 } , \ldots , p _ { n }$ in $\mathcal { P }$ and positive scalars $\alpha _ { 1 } , \ldots , \alpha _ { n }$ such that $| f ( x ) | \leqslant \sum _ { k = 1 } ^ { n } \alpha _ { k } p _ { k } ( x )$ for all x.

The proof of the next proposition is similar to the proof of Proposition 1.14 and will not be given.

3.2. Proposition. Let X be a TVS and suppose that G is an open convex subset of X that contains the origin. If

$$
q ( x ) = \operatorname* { i n f } \{ t \colon t \geqslant 0 { \mathrm { ~ a n d ~ } } x \in t G \} ,
$$

then q is a non-negative continuous sublinear functional and $G = \{ x : q ( x ) < 1 \}$

Note that the difference between the preceding proposition and (1.14) is that here G is not assumed to be balanced and the consequence is a sublinear functional $(q(\alpha x) = \alpha q(x)   if   \alpha \geqslant 0)$ that is not necessarily a seminorm.

The geometric consequences of the Hahn-Banach Theorem are achieved by interpreting that theorem in light of the correspondence between linear functionals and hyperplanes and between sublinear functionals and open convex neighborhoods of the origin. The next result is typical.

3.3. Theorem. If X is a TVS and G is an open convex nonempty subset of X that does not contain the origin, then there is a closed hyperplane M such that $\mathcal { N } \cap G = \square$

PROOF. Case $I , \mathcal { X }$ is an R-linear space. Pick any $x _ { 0 }$ in $G$ and let $H   =   x _ { 0 } - G$ Then H is an open convex set containing 0. (Verify). By (3.2) there is a continuous nonnegative sublinear functional $q \colon { \mathcal { X } }   \to   \mathbb { R }$ such that $H   =$ $\{ x : q ( x ) < 1 \}$ . Since $x _ { 0 } \notin H ,   q ( x _ { 0 } ) \geq 1$

Let $\mathcal { Y } \equiv \left\{ \alpha x _ { 0 } \colon \alpha { \in } \mathbb { R } \right\}$ and define $f _ { 0 } \colon \mathcal { B } \to \mathbb { R }$ by $f _ { 0 } ( \alpha x _ { 0 } ) = \alpha q ( x _ { 0 } )$ If $\alpha \geqslant 0 ,$ then $f_{0}(\alpha x_{0}) = \alpha q(x_{0}) = q(\alpha x_{0}); \quad  if   \alpha < 0.$ then $f_{0}(\alpha x_{0}) = \alpha q(x_{0}) \leqslant \alpha < 0 \leqslant q(\alpha x_{0})$ So $f _ { 0 } \leqslant q$ on Y. Let $f \colon { \mathcal { X } }   \to   \mathbb { R }$ be a linear functional such that $f | \mathcal { Y } = f _ { 0 }$ and $f \leqslant q$ on X. Put M = ker f.

Now if $x { \in } G ,$ then $x _ { 0 }   -   x   \in   H$ and so $f(x_{0}) - f(x) = f(x_{0} - x) \leqslant q(x_{0} - x) < 1$ Therefore $f(x)>f(x_{0})-1=q(x_{0})-1\geqslant0$ for all x in G. Thus $\mathcal { M } \cap G = \square$

Case 2. X is a C-linear space. Lemma III.6.3 will be used here. Using Case 1 and the fact that ¿ is also an R-linear space, there is a continuous R-linear functional $f \colon { \mathcal { X } }   \to   \mathbb { R }$ such that $G \cap$ ker $f = \Box$ . If $F(x) = f(x) - if(ix)$ , then F is a C-linear functional and f = Re F (III.6.3). Hence $F ( x ) = 0$ if and only if $f(x) = f(ix) = 0;$ that is, $\mathcal { M } = \ker F = \ker f \cap [ i \ker f ]$ . So M is a closed hyperplane and $\mathcal { M } \cap G = \square$ ■

An affine hyperplane in $\mathcal { X }$ is a set $\mathcal { M }$ such that for every $x _ { 0 }$ in $\mathcal { M } , \mathcal { M } - x _ { 0 }$ is a hyperplane. (See Exercise 3.) An affine manifold in $\mathcal { X }$ is a set $\theta$ such that for every $x _ { 0 }$ in $\mathcal { G } , \mathcal { G } - x _ { 0 }$ is a linear manifold in ${ \mathcal { R } } .$ An affine subspace of a TVS $\mathcal { X }$ is a closed affine manifold.

3.4. Corollary. Let $\mathcal { X }$ be a TVS and let G be an open convex nonempty subset of X. If $\theta$ is an affine subspace of $\mathcal { X }$ such that $\mathcal { Y } \cap G = \square$ , then there is a closed affine hyperplane M in $\mathcal { X }$ such that $\mathcal { Y } \subseteq \mathcal { M }$ and $\mathcal { M } \cap G = \square$

PROOF. By considering $G - x _ { 0 }$ and $\mathcal { Y } - x _ { 0 }$ for any $x _ { 0 }$ in $\theta ,$ it may be assumed that Y is a linear subspace of $\mathcal { X } ,$ Let $\mathcal { Q } \colon \mathcal { X }   \to   \mathcal { X } / \mathcal { Y }$ be the natural map. Since $Q ^ { - 1 } ( Q ( G ) ) = \{ y + G : y \in { \mathcal { Y } } \}$ , Q(G) is open in $\mathcal { X } / \mathcal { Y }$ . It is easy to see that $Q ( G )$ is also convex. Since $\mathcal { Y } \cap G = \square , \; 0 \notin Q ( G )$ . By the preceding theorem, there is a closed hyperplane $\mathcal { N }$ in $\mathcal { X } / \mathcal { Y }$ such that $\mathcal { N } \cap Q ( G ) = \square$ . Let $\mathcal { M } = Q ^ { - 1 } ( \mathcal { N } )$ It is easy to check that $\mathcal { M }$ has the desired properties.

There is a great advantage inherent in a geometric discussion of real $\mathbf { T V S s . }$ Namely, if $f \colon { \mathcal { X } }   \to   \mathbb { R }$ is a nonzero continuous R-linear functional, then the hyperplane ker f disconnects the space. That is, $| \mathcal { X } \rangle$ ker f has two components (see Exercises 4 and 5). It thus becomes convenient to make the following definitions.

3.5. Definition. Let $\mathcal { X }$ be a real TVS. A subset S of $\mathcal { X }$ is called an open half-space if there is a continuous linear functional $f \colon { \mathcal { X } }   \to   \mathbb { R }$ such that $\mathcal { S } = \{ x \in \mathcal { X } : f ( x ) > \alpha \}$ for some α. S is a closed half-space if there is a continuous linear functional $f \colon { \mathcal { X } }   \to   \mathbb { R }$ such that $S = \{ x \in { \mathcal { X } } : f ( x ) \geqslant \alpha \}$ for some α.

Two subsets A and B of $\mathcal { X }$ are said to be strictly separated if they are contained in disjoint open half-spaces; they are separated if they are contained in two closed half-spaces whose intersection is a closed affine hyperplane.

3.6. Proposition. Let X be a real TVS.

(a) The closure of an open half-space is a closed half-space and the interior of a closed half-space is an open half-space.

(b) If $A , B \subseteq { \mathcal { X } }$ , then A and B are strictly separated (separated) if and only if there is a continuous linear functional f: $\mathcal { X }   \rightarrow   \mathbb { R }$ and a real scalar α such that $f ( a ) > \alpha$ for all a in A and $f ( b ) < \alpha$ for all b in $B \left( f ( a ) \geqslant \alpha \right.$ for all a in A and $f(b) \leqslant \alpha$ for all b in B).

PROOF. Exercise 6.

In many ways, the next result is the most important “separation" theorem as the other separation theorems follow from this one. However, the most used separation theorem is Theorem 3.9 below.

3.7. Theorem. If X is a real TVS and A and B are disjoint convex sets with A open, then there is a continuous linear functional $f \colon { \mathcal { X } }   \to   \mathbb { R }$ and a real scalar α such that $f ( a ) < \alpha$ for all a in A and $f(b) \geqslant \alpha$ for all b in B. If B is also open, then A and B are strictly separated.

PROOF. Let $G = A - B \equiv \{ a - b : a { \in } A , b { \in } B \}$ ; it is easy to verify that G is convex (do it!). Also, $G = \cup   \{ A - b \colon b { \in } B \}$ , so G is open. Moreover, because $A \cap B = \square$ $0 \notin G$ . By Theorem 3.3 there is a closed hyperplane M in $\mathcal { X }$ such that $\mathcal { M } \cap G = \square$ . Let $f \colon { \mathcal { X } }   \to   \mathbb { R }$ be a linear functional such that $\mathcal { M } = \ker f .$ Now f(G) is a convex subset of R and ${ \mathbf { 0 } } { \notin } f ( G )$ . Hence either $f ( x )   >   0$ for all x in G or $f ( x )   <   0$ for all x in G; suppose $f ( x ) > 0$ for all x in G. Thus if $a { \in } A$ and $b \in B, \; 0 < f(a - b) = f(a) - f(b),$ ; that is, $f ( a )   >   f ( b )$ . Therefore there is a real number α such that

$$
\sup \left\{ f(b): b \in B \right\} \leqslant \alpha \leqslant \inf \left\{ f(a): a \in A \right\}.
$$

But $f ( A )$ and $f ( B )$ are open intervals if B is open (Exercise 7), so $f < \alpha$ on B and f > α on A. ■

3.8. Lemma. If X is a TVS, K is a compact subset of $\mathcal { X } ,$ , and V is an open subset of X such that $K \subseteq V$ , then there is an open neighborhood of $[ 0 , U ,$ , such that $K + U \subseteq V$

PROOF. Let $\mathcal { U } _ { 0 } = \mathrm { a l l }$ of the open neighborhoods of 0. Suppose that for each U in $\mathcal { U } _ { 0 } ,   K + U$ is not contained in V. Thus, for each U in $\mathcal { U } _ { 0 }$ there is a vector $x _ { U }$ in K and a $y _ { U }$ in U such that $x _ { U } + y _ { U } { \in } { \mathcal { X } } \backslash V$ . Order $\mathcal { U } _ { 0 }$ by reverse inclusion; that is, $U_{1} \geqslant U_{2}   if   U_{1} \subseteq U_{2}$ Then $\mathcal { U } _ { 0 }$ is a directed set and $\left\{ x _ { v } \right\}$ and $\{ y _ { v } \}$ are nets. Now $y _ { U }   \to   0$ in X. Because K is compact there is an x in K such that $x _ { v }   \underset { \mathrm { c l } } { \longrightarrow }   x \big ( \big \{ x _ { v } \big \}$ cluster at x). Hence $x _ { U } + y _ { U } \longrightarrow x + 0 = x .$ (Why?) Hence x∈cl $( \mathcal { X } \backslash V ) = \mathcal { X } \backslash V ,$ a contradiction.

The condition that K be compact in the preceding lemma is necessary; it is not enough to assume that K is closed. (What is a counterexample?)

3.9. Theorem. Let $\mathcal { X }$ be a real LCS and let A and B be two disjoint closed convex subsets of X. If B is compact, then A and B are strictly separated.

ProoF. By hypothesis, B is a compact subset of the open set ${ \mathcal { X } } \backslash A .$ The preceding lemma implies there is an open neighborhood $U _ { 1 }$ of 0 such that $\boldsymbol { B } + \boldsymbol { U } _ { 1 } \in \mathcal { X } \backslash \boldsymbol { A }$ Because $\mathcal { X }$ is locally convex, there is a continuous seminorm p on $\mathcal { X }$ such that $\{ x \colon p ( x ) < 1 \} \subseteq U _ { 1 }$ . Put $U = \{ x \colon   p ( x )   <   \frac { 1 } { 2 } \}$ Then $( B + U ) \cap ( A + U ) = \square$ (Verify!), and $A + U$ and $B + U$ are open convex subsets of $\mathcal { X }$ that contain A and B, respectively. (Why?) So the result follows from Theorem 3.7.

The fact that one of the two closed convex sets in the preceding theorem is assumed to be compact is necessary. In fact, if $\mathcal { X } = \mathbb { R } ^ { 2 } , \; A = \{ ( x , y ) \in \mathbb { R } ^ { 2 }$ $y \leqslant 0 \}$ , and $B = \left\{ (x,y) \in \mathbb{R}^2 : y \geqslant x^{-1} > 0 \right\}$ , then A and B are disjoint closed convex subsets of $\mathbb { R } ^ { 2 }$ that cannot be strictly separated.

The next result generalizes Corollary III.6.8, though, of course, the metric content of (III.6.8) is missing.

3.10. Corollary. If X is a real LCS, A is a closed convex subset of $\mathcal { X } ,$ and $x \notin A$ , then x is strictly separated from A.

3.11. Corollary. If X is a real LCS and $A \subseteq { \mathcal { X } }$ , then co(A) is the intersection of the closed half-spaces containing A.

PrOOF. Let $\mathcal { H }$ be the collection of all closed half-spaces containing A. Since each set in $\mathcal { H }$ is closed and convex, co $(A) \subseteq \cap \{ H: H \in \mathcal{H} \}$ . On the other hand, i $x _ { 0 } \not \in \overline { { \mathbf { c o } } } \left( A \right)$ , then (3.10) implies there is a continuous linear functional $f \colon { \mathcal { X } }   \to   \mathbb { R }$ and an α in IR such that $f ( x _ { 0 } ) > \alpha$ and $f ( x ) < \alpha$ for all x in co(A). Thus $H = \{ x : f ( x ) \leqslant \alpha \}$ belongs to $\mathcal { H }$ and $x _ { 0 } { \notin } H$ ■

The next result generalizes Theorem III.6.13.

3.12. Corollary. If X is a real LCS and $A \subseteq { \mathcal { X } }$ , then the closed linear span of A is the intersection of all closed hyperplanes containing A.

If € is a complex LCS, it is also a real LCS. This can be used to formulate and prove versions of the preceding results. As a sample, the following complex version of Theorem 3.9 is presented.

3.13. Theorem. Let $\mathcal { X }$ be a complex LCS and let A and B be two disjoint closed convex subsets of X. If B is compact, then there is a continuous linear functional f: $\mathcal { X }   \to   \mathbb { C } ,$ an α in R, and an $\varepsilon   >   0$ such that for a in A and b in B,

$$
\operatorname{Re} f(a) \leqslant \alpha < \alpha + \varepsilon \leqslant \operatorname{Re} f(b).
$$

3.14. Corollary. If X is a LCS and Y is a linear manifold in $\mathcal { X } ,$ then $\mathcal { G }$ is dense in X if and only if the only continuous linear functional on X that vanishes on $\pmb { g }$ is the identically zero functional.

3.15. Corollary. If X is a LCS, Y is a closed linear subspace of X, and $x _ { 0 } \in \mathcal { X } \backslash \mathcal { Y }$ then there is a continuous linear functional f: $\mathcal { X }   \rightarrow   \mathbf { F }$ such that $f(y) = 0   for$ all y in $\mathcal { Y }$ and $f ( x _ { 0 } ) = 1$

These results imply that on a LCS there are many continuous linear functionals. Compare the results of this section with those of §III.6.

The hypothesis that $\mathcal { X }$ is locally convex does not appear in the results prior to Theorem 3.9. The reason for this is that in the preceding results the existence of an open convex subset of $\mathcal { X }$ is assumed. In Theorem 3.9 such a set must be manufactured. Without the hypothesis of local convexity it may be that the only open convex sets are the whole space itself and the empty set.

3.16. Example. For $0 < p < 1$ , let $L ^ { p } ( 0 , 1 )$ be the collection of equivalence classes of measurable functions $f \colon ( 0 , 1 )   \to   \mathbb { R }$ such that

$$
( ( f ) ) _ { p } = \int _ { 0 } ^ { 1 } | f ( x ) | ^ { p } d x < \infty .
$$

It will be shown that $d ( f , g ) = ( ( f - g ) ) _ { p }$ is a metric on $L ^ { p } ( 0 , 1 )$ and that with this metric $L ^ { p } ( 0 , 1 )$ is a Fréchet space. It will also be shown, however, that $L ^ { p } ( 0 , 1 )$ has only one nonempty open convex set, namely itself. So $L ^ { p } ( 0 , 1 )$ $0 < p < 1$ , is most emphatically not locally convex. The proof of these facts begins with the following inequality.

## 3.17

$$
For $s , t \operatorname { i n } \left[ 0 , \infty \right)$ and $0 < p < 1 , \: ( s + t ) ^ { p } \leqslant s ^ { p } + t ^ { p } .$
$$

To see this, let $f ( t ) = s ^ { p } + t ^ { p } - ( s + t ) ^ { p }$ for $t \geqslant 0,\quad s\quad  fixed .$ Then $f^{\prime}(t)=pt^{p - 1}-p(s + t)^{p - 1}$ . Since $p - 1 < 0$ and $s + t \geqslant t,\ f^{\prime}(t) \geqslant 0.$ Thus $0 = f(0) \leq f(t)$ This proves (3.17)

If $d ( f , g ) = ( ( f - g ) ) _ { p }$ for $f , g$ in $L ^ { p } ( 0 , 1 ) ,$ then (3.17) implies that $d(f,g) \leqslant d(f,h) + d(h,g)$ for all $f , g , h$ in $L ^ { p } ( 0 , 1 )$ . It follows that d is a metric on $L ^ { p } ( 0 , 1 )$ . Clearly d is translation invariant.

## 3.18

$$
L^{p}(0,1), 0 < p < 1,  is complete.
$$

The proof of this is left as an exercise.

## 3.19

$$
L ^ { p } ( 0 , 1 ) \mathrm { ~ i s ~ a ~ T V S } .
$$

The continuity of addition is a direct consequence of the translation invariance of d. If $f _ { n }   \rightarrow   f$ and $\alpha _ { n }   \to   \alpha , \alpha _ { n }$ in R, $d(\alpha_{n}f_{n},\alpha f)=((\alpha_{n}f_{n}-\alpha f))_{p}\leqslant$ $\left( \left( \alpha _ { n } f _ { n } - \alpha _ { n } f \right) \right) _ { p } + \left( \left( \alpha _ { n } f - \alpha f \right) \right) _ { p } = \left| \alpha _ { n } \right| ^ { p } \left( \left( f _ { n } - f \right) \right) _ { p } + \left| \alpha _ { n } - \alpha \right| ^ { p } \left( \left( f \right) \right) _ { p } \leqslant C \left( \left( f _ { n } - f \right) \right) _ { p } +$ $| \alpha _ { n } - \alpha | ^ { p } ( ( f ) ) _ { p } ,$ where C is a constant independent of n. Hence $\alpha _ { n } f _ { n }   \to   \alpha f$ Thus $L ^ { p } ( 0 , 1 )$ is a Fréchet space.

If G is a nonempty open convex subset of $L ^ { p } ( 0 , 1 )$ , then

## 3.20

$$
G = L ^ { p } ( 0 , 1 ) .
$$

To see this, first suppose $f   \in   L ^ { p } ( 0 , 1 )$ and $( ( f ) ) _ { p } = r < R$ . As a function of t, $\int _ { 0 } ^ { t } | f ( x ) | ^ { p } d x$ is continuous, assumes the value 0 at $t   =   0 .$ , and assumes the value r at $t = 1$ . Let $0 < t < 1$ such that $\int_{0}^{t} \left| f(x) \right|^p dx = r/2$ . Define $g , h \colon ( 0 , 1 ) \to \mathbb { R }$ by $g ( x )   =   f ( x )$ for $x \leqslant t$ and 0 otherwise; $h ( x )   =   f ( x )$ for $x \geqslant t$ and 0 otherwise. Now $f = g + h = \frac { 1 } { 2 } ( 2 g + 2 h )$ and $( ( 2 g ) ) _ { p } = ( ( 2 h ) ) _ { p } = 2 ^ { p } ( r / 2 ) = r / 2 ^ { 1 - p }$ Hence f∈co $B ( 0 ; R / 2 ^ { 1 - p } )$ .This implies that $B ( 0 ; R ) \subseteq \mathrm { c o } B ( 0 ; R / 2 ^ { 1 - p } ) , \mathrm { o r } ,$ equivalently, $B(0; 2^{1-p}R) \subseteq \mathrm{co} B(0,R)$ . Hence $B(0; 4^{1-p}R) \subseteq \mathrm{co} B(0; 2^{1-p}R) \subseteq \mathrm{co} B(0;R)$ Continuing we see that for all n, $B ( 0 ; 2 ^ { n ( 1 - p ) } R ) \subseteq \mathrm { c o } B ( 0 ; R )$

So if G is a nonempty open convex subset of $L ^ { p } ( 0 , 1 )$ , then by translation it may be assumed that $0 \in G .$ Thus there is an $R   >   0$ with $B ( 0 ; R ) \subseteq G$ . By the preceding paragraph, $B ( 0 ; 2 ^ { n ( 1 - p ) } R ) \subseteq \mathrm { c o }   B ( 0 ; R ) \subseteq G$ for all $n \geqslant 1$ Therefore $L ^ { p } ( 0 , 1 ) \subseteq G$

Also note that this says that the only continuous linear functional on $L ^ { p } ( 0 , 1 ) ,   0 < p < 1$ , is the identically zero functional.

## EXERCISES

1. Prove Theorem 3.1.

2. Let p be a sublinear functional, $G \equiv \left\{ x \colon p ( x ) < 1 \right\}$ , and define the sublinear functional q for the set G as in Proposition 3.2. Show that $q(x) = \max(p(x)), 0$ for all x in X.

3. Let $\mathcal { M } \subseteq \mathcal { X }$ , a TVS, and show that the following statements are equivalent : (a) M is an affine hyperplane; (b) there exists an $x _ { 0 }$ in M such that $\mathcal { M } - x _ { 0 }$ is a hyperplane; (c) there is a non-zero linear function $f \colon { \mathcal { X } }   \to   \mathbb { F }$ and an α in F such that $\mathcal { M } = \{ x \in \mathcal { X } : f ( x ) = \alpha \}$

4. Let ¿ be a real TVS. Show: (a) if G is an open connected subset of $\mathcal { R } ,$ then G is arcwise connected; (b) $\operatorname* { i f } f \colon { \mathcal { X } }   \to   \mathbb { R }$ is a continuous non-zero linear functional, then X\ker f has two components, $\{ x : f ( x ) > 0 \}$ and $\{ x : f ( x ) < 0 \}$

5. If ¿ is a complex TVS and $f \colon { \mathcal { X } }   \to   \mathbb { C }$ is a nonzero continuous linear function, show that X\ker f is connected.

6. Prove Proposition 3.6.

7. If $f \colon { \mathcal { X } }   \to   \mathbb { R }$ is a continuous R-linear functional and A is an open convex subset of X, then $f ( A )$ is an open interval.

8. Prove Corollary 3.12.

9. Prove Theorem 3.13

10. State and prove a version of Theorem 3.7 for a complex TVS.

11. State and prove a version of Corollary 3.11 for a complex LCS.

12. State and prove a version of Corollary 3.12 for a complex LCS.

13. Prove (3.18).