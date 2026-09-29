hand, it is assumed that $y _ { i } + z _ { i }   \rightarrow   y + z _ { 1 }$ then $y = P(y + z) = \lim_{} P(y_i + z_i) =$ lim and $y _ { i }$ $z _ { i } = ( y _ { i } + z _ { i } ) - y _ { i } \rightarrow z$ This proves (a).

5.23. Definition. If $\mathcal { X }$ is a TVS and $\mathcal { G } \leqslant \mathcal { X } , \mathcal { G }$ is topologically complemented in $\mathcal { X }$ if either (a) or (b) of (5.22) is satisfied.

5.24. Proposition. If X is a LCS and $\mathcal { Y } \leqslant \mathcal { X }$ such that either dim $\mathcal { Y } < \infty$ or dim $\mathcal { X } / \mathcal { Y } < \infty$ , then Y is topologically complemented in $\mathcal { X }$

ProoF. The proof will only be sketched. The reader is asked to supply the details (Exercise 9).

(a) Suppose $d = \dim \mathcal{B} < \infty$ and let $y _ { 1 } , \ldots , y _ { d }$ be a basis for $\mathcal { Y }$ By the Hahn-Banach Theorem (III.6.6), there are $f _ { 1 } , . . . , f _ { d }$ in $\mathcal { X } ^ { * }$ such that $f _ { i } ( y _ { j } )   = 1$ if $i   =   j$ and 0 otherwise. Define $P x = \sum _ { j = 1 } ^ { d } f _ { j } ( x ) y _ { j }$

(b) Suppose $d = \dim \mathcal{X} / \mathcal{Y} < \infty, \quad Q : \mathcal{X} \to \mathcal{X} / \mathcal{Y}$ is the natural map, and $z _ { 1 } , \ldots , z _ { d } { \in } { \mathcal { X } }$ such that $Q ( z _ { 1 } ) , \ldots , Q ( z _ { d } )$ is a basis for $\mathcal { X } / \mathcal { Y }$ . Let $\mathcal { X } = \vee \left\{ z _ { 1 } , \ldots , z _ { d } \right\}$ L

PROOF OF PROPOSITION 5.16. Suppose $\mathcal { X }$ is the strict inductive limit of $\{ ( \mathcal { X } _ { n } , \mathcal { T } _ { n } \} )$ and B is a bounded subset of $\mathcal { X }$ It must be shown that there is an n such that $B \subseteq { \mathcal { X } } _ { n }$ (the rest of the proof is easy). Suppose this is not the case. By replacing $\{ \mathcal { X } _ { n } \}$ by a subsequence if necessary, it follows that for each n there is an $x _ { n }$ in $( B \cap \mathcal { X } _ { n + 1 } ) \backslash \mathcal { X } _ { n }$ . Let $p _ { 1 }$ be a continuous seminorm on $\mathcal { X } _ { 1 }$ such that $p _ { 1 } ( x _ { 1 } )   = 1$

5.25. Claim. For every $n \geqslant 2$ there is a continuous seminorm $p _ { n }$ on $\mathcal { X } _ { n }$ such that $p _ { n } ( x _ { n } ) = n$ and $p_{n}|\mathcal{X}_{n - 1} = p_{n - 1}$

The proof of (5.25) is by induction. Suppose $p _ { n }$ is given and let $\mathcal { G } = \mathcal { X } _ { n } \vee$ $\{ x _ { n + 1 } \}$ . By (5.24), $\mathcal { X } _ { n }$ and $\vee \left\{ x _ { n + 1 } \right\}$ are topologically complementary in $俾 ,$ Define $q \colon { \mathcal { G } }   \to   [ 0 , \infty )$ by $q ( x + \alpha x _ { n + 1 } ) = p _ { n } ( x ) + ( n + 1 ) | \alpha | ,$ ,where $x { \in } { \mathcal { X } } _ { n }$ and $\alpha \in \mathbb { F }$ Then q is a continuous seminorm on $( \mathcal { Y } , \mathcal { T } _ { n + 1 } | \mathcal { Y } )$ (Verify!) By Proposition 5.13 there is a continuous seminorm $p _ { n + 1 }$ on $\mathcal { X } _ { n + 1 }$ such that $p _ { n + 1 } | \mathcal { G } = q .$ Thus $p_{n + 1} \mid \mathcal{X}_n = p_n$ and $p_{n + 1}(x_{n + 1}) = n + 1$ . This proves the claim. Now define p: $\mathcal { X }   \to   [ 0 , \infty )$ by $p ( x ) = p _ { n } ( x )$ if $x { \in } { \mathcal { X } } _ { n }$ . By (5.25), p is well defined. It is easy to see that p is a continuous seminorm. However, sup $\{ p ( x ) : x \in B \} = \infty$ so B is not bounded (Exercise 2.4f).

## EXERCISES

1. Verify the statements made in Example 5.2.

2. Fill in the details of the proof of Proposition 5.3.

3. Prove Proposition 5.6.

4. Verify the statements made in Example 5.9.

5. Verify the statements made in Example 5.10.

6. Verify the statements made in Example 5.11.

7. With the notation of (5.10), show that if X is σ-compact, then the dual of $C _ { c } ( X )$ is the space of all extended F-valued measures.

8. Is the inductive limit topology on $C _ { c } ( X )$ (5.10) different from the topology of uniform convergence on compact subsets of X (1.5)?

9. Prove Proposition 5.24.

10. Verify the statements made in Example 5.20.

For the remaining exercises, Ω is always an open subset of $\mathbb { R } ^ { d } ,   d \geqslant 1$

11. If $\mu$ is a measure on $\Omega , \phi   \mapsto   \int   \phi   d \mu$ is a distribution Ω.

12. Let $f \colon \Omega   \to   \mathbb { F }$ be a function with continuous partial derivatives and let $L _ { f }$ be defined as in (5.20). Show that for every $\phi$ in $\mathcal { D } ( \Omega )$ and $1 \leqslant j \leqslant d,\; L_{f}(\partial \phi / \partial x_{j}) =$ $- L _ { g } ( \phi )$ , where $g = \partial f / \partial x _ { j }$ . (Hint: Use integration by parts.)

13. Exercise 12 motivates the following definition. If L is a distribution on $\mathbf { \Omega } ,$ define $\partial L / \partial x _ { j } \colon \mathcal { D } ( \Omega ) \to \mathbb { F }$ by $\partial L / \partial x _ { j } ( \phi ) = -   L ( \partial \phi / \partial x _ { j } )$ for all φ in (Ω). Show that $\partial L / \partial x _ { j }$ is a distribution.

14. Using Example 5.20 and Exercise 13, one is justified to talk of the derivative of any locally integrable function as a distribution. By Exercise 11 we can differentiate measures. Let $f \colon \mathbb { R } \to \mathbb { R }$ be the characteristic function of $[ 0 , \infty )$ and show that its derivative as a distribution is $\delta _ { 0 } ,$ the unit point mass at 0. [That is, $\delta _ { 0 }$ is the measure such that $\delta _ { 0 } ( \Delta ) = 1$ $\mathbf { 0 } { \in } \Delta$ and $\delta _ { 0 } ( \Delta ) = 0 \mathrm { i f } 0 \notin \Delta .$

15. Let f be an absolutely continuous function on R and show that $( L _ { f } ) ^ { \prime }   =   L _ { f ^ { \prime } }$

16. Let f be a left continuous nondecreasing function on R and show that $( L _ { f } ) ^ { \prime }$ is the distribution defined by the measure $\mu$ such that $\mu [ a , b ) = f ( b ) - f ( a )$ for all $a   <   b$

17. Let f be $\textbf { a } C ^ { \infty }$ function on Ω and let L be a distribution on $\mathcal { D } ( \Omega ) .$ Show that $M ( \phi ) \equiv L ( \phi f ) , \phi$ in (Ω), is a distribution. State and prove a product rule for finding the derivative of M.

CHAPTER V

# Weak Topologies

The principal objects of study in this chapter are the weak topology on a Banach space and the weak-star topology on its dual. In order to carry out this study efficiently, the first two sections are devoted to the study of the weak topology on a locally convex space.

## §1. Duality

As in §IV.4, for a LCS $\mathcal { X } ,$ let $\mathcal { X } ^ { * }$ denote the space of continuous linear functionals on $\mathcal { R } .$ If $x ^ { * } , y ^ { * }   \in   \mathcal { X } ^ { * }$ and α∈F, then $( \alpha x ^ { * } + y ^ { * } ) ( x ) \equiv \alpha x ^ { * } ( x ) + y ^ { * } ( x ) .$ x in $\mathcal { X }$ , defines an element $\alpha x ^ { * } + y ^ { * }$ in $\mathcal { X } ^ { * }$ . Thus $\mathcal { X } ^ { * }$ has a natural vector-space structure.

It is convenient and, more importantly, helpful to introduce the notation

$$
\langle x , x ^ { * } \rangle
$$

to stand for $x ^ { * } ( x )$ , for x in $\mathcal { X }$ and $x ^ { * }$ in $\mathcal { X } ^ { * }$ . Also, because of a certain symmetry, we will use $\langle x ^ { * } , x \rangle$ to stand for $x ^ { * } ( x )$ . Thus

$$
x ^ { * } ( x ) = \langle x , x ^ { * } \rangle = \langle x ^ { * } , x \rangle .
$$

We begin by recalling two definitions (IV.1.7 and IV.1.8).

1.1. Definition. If $\mathcal { X }$ is a LCS, the weak topology on $\mathcal { X } ,$ denoted by “wk” or $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } )$ , is the topology defined by the family of seminorms $\left\{ p _ { x ^ { * } } : x ^ { * } \in \mathcal { X } ^ { * } \right\}$ where

$$
p _ { x ^ { * } } ( x ) = | \langle x , x ^ { * } \rangle | .
$$

The weak-star topology on $\mathcal { X } ^ { * }$ , denoted by “wk\*” or $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } )$ , is the

topology defined by the seminorms $\{ p _ { x } ; x \in \mathcal { X } \}$ , where

$$
p _ { x } ( x ^ { * } ) = | \langle x , x ^ { * } \rangle | .
$$

So a subset $U$ of $\mathcal { X }$ is weakly open if and only if for every $x _ { 0 }$ in $U$ there is an $\varepsilon   >   0$ and there are $x _ { 1 } ^ { * } , \ldots , x _ { n } ^ { * }$ in $\mathcal { X } ^ { * }$ such that

$$
\bigcap_{k = 1}^{n} \left\{ x \in \mathcal{X} : \left| \left\langle x - x_{0}, x_{k}^{*} \right\rangle \right| < \varepsilon \right\} \subseteq U.
$$

A net $\{ x _ { i } \}$ in $\mathcal { X }$ converges weakly to $x _ { 0 }$ if and only if $\langle x _ { i } , x ^ { * } \rangle   \to   \langle x _ { 0 } , x ^ { * } \rangle$ for every $x ^ { * }$ in $\mathcal { X } ^ { * }$ . (What are the analogous statements for the weak-star topology?)

Note that both $( \mathcal { X } )$ ,wk) and $( \mathcal { X } ^ { * } , \mathbf { w } \mathbf { k } ^ { * } )$ are LCS's. Also, $\mathcal { X }$ already possesses a topology so that wk is a second topology on $\mathcal { X } .$ However, $\mathcal { X } ^ { * }$ has no topology to begin with so that $\mathbf { w } \mathbf { k } ^ { * }$ is the only topology on $\mathcal { X } ^ { * }$ . Of course i $\mathcal { X }$ is a normed space, this last statement is not correct since $\mathcal { X } ^ { * }$ is a Banach space (III.5.4). The reader should also be cautioned that some authors abuse the language and use the term weak topology to designate both the weak and weak-star topologies. Finally, pay attention to the positions of $\mathcal { X }$ and $\mathcal { X } ^ { * }$ in the notation $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } ) =$ wk and $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } ) = \mathbf { w } \mathbf { k } ^ { * }$

If $\left\{ x _ { i } \right\}$ is a net in $\mathcal { X }$ and $x _ { i }   \rightarrow   0$ in $\mathcal { X } ,$ , then for every $x ^ { * }$ in $\mathcal { X } ^ { * } , \langle x _ { i } , x ^ { * } \rangle   \rightarrow   0 .$ So if $\mathcal { T }$ is the topology on $\mathcal { X }$ $\mathbf { w } \mathbf { k } \subseteq \mathcal { T } ( \mathbf { A } . 2 . 9 )$ and each $x ^ { * }$ in $\mathcal { X } ^ { * }$ is weakly continuous. The first result gives the converse of this.

## 1.2. Theorem. If X is a LCS, $( \mathcal { X } , \mathrm { w k } ) ^ { * } = \mathcal { X } ^ { * }$

ProoF. Since every weakly open set is open in the original topology, each f in $( \mathcal { X } , \mathbf { w } \mathbf { k } ) ^ { * }$ belongs to $\mathcal { X } ^ { * }$ . The converse is even easier.

## 1.3. Theorem. If X is a LCS, $( \mathcal { X } ^ { * } , \mathrm { w k } ^ { * } ) ^ { * } = \mathcal { X } .$

PROOF. Clearly if $x { \in } { \mathcal { X } } , x ^ { * } { \to } \langle x , x ^ { * } \rangle$ is a $\mathbf { w } \mathbf { k } ^ { * }$ continuous functional on $\mathcal { X } ^ { * }$ Hence $\mathcal { X }   \subseteq   ( \mathcal { X } ^ { * } , \mathrm { w k } ^ { * } ) ^ { * }$ . Conversely, if $f   \in   ( \mathcal { X } ^ { * } , \mathrm { w k } ^ { * } ) ^ { * }$ , then (IV.3.1) implies there are vectors $x _ { 1 } , \ldots , x _ { n }$ in X such that $| f ( x ^ { * } ) | \leqslant \sum _ { k = 1 } ^ { n } | \langle x _ { k } , x ^ { * } \rangle |$ for all $x ^ { * }$ in $\mathcal { X } ^ { * }$ . This implies that $\cap \left\{ \ker x_{k} : 1 \leqslant k \leqslant n \right\} \subseteq \ker f$ By (A.1.4) there are scalars $\alpha _ { 1 } , \ldots , \alpha _ { n }$ such that $f = \sum_{k = 1}^{n} \alpha_{k} x_{k};$ hence $f \in \mathcal { X }$

So $\mathcal { X }$ is the dual of a $\mathrm { L C S } \mathrm { { \textellipsis } ( { \mathcal X } ^ { * } , w k ^ { * } ) }$ —and hence has a weak-star topolo $\mathrm{gy} -- \sigma((\mathcal{X}, \mathrm{wk}^*), \mathcal{X}^*)$ . As an exercise in notational juggling, note that $\sigma ( ( \mathcal { X } , \mathrm { w k } ^ { * } ) , \mathcal { X } ^ { * } ) = \sigma ( \mathcal { X } , \mathcal { X } ^ { * } )$

All unmodified topological statements about $\mathcal { X }$ refer to its original topology. So if $A \subseteq { \mathcal { X } }$ and we say that it is closed, we mean that A is closed in the original topology of $\mathcal { X }$ .To say that $A$ is closed in the weak topology of $\mathcal { X }$ we say that $A$ is weakly closed or wk-closed. Also cl A means the closure of A in the original topology while wk – cl A means the closure of A in the weak topology. The next result shows that under certain circumstances this distinction in unnecessary.

1.4. Theorem. If X is a LCS and A is a convex subset of $\mathcal { X } ,$ then cl $A = \mathbf{w}\mathbf{k} - \mathbf{c}\mathbf{l}A.$

PROOF. If $\mathcal { T }$ is the original topology of $\mathcal { X } ,$ then $\mathbf { w } \mathbf { k } \subseteq \mathcal { T }$ , hence cl $A \subseteq \mathbf { w } \mathbf { k } - \mathbf { c } \mathbf { l } \; A$ Conversely, if $x \in { \mathcal { X } } \backslash { \mathrm { c l } } A$ , then (IV.3.13) implies that there is an $x ^ { * }$ in $\mathcal { X } ^ { * }$ , an α in R, and an $\varepsilon   >   0$ such that

$$
\operatorname { R e } \langle a , x ^ { * } \rangle \leqslant \alpha < \alpha + \varepsilon \leqslant \operatorname { R e } \langle x , x ^ { * } \rangle
$$

for all a in cl A. Hence cl $A \subseteq B \equiv \{ y \in \mathcal{X} : \operatorname{Re}(y, x^*) \leq \alpha \}$ . But B is clearly wk-closed since $x ^ { * }$ is wk-continuous. Thus wk - cl $A \subseteq B .$ Since $x \notin B ,$ $x \notin \mathbf { w } \mathbf { k } - \mathbf { c } \mathbf { l } \mathbf { \nabla } A$ ■

## 1.5. Corollary. A convex subset of £ is closed if and only if it is weakly closed.

There is a useful observation that can be made here. Because of (III.6.3) it can be shown that if  is a complex linear space, then the weak topology on $\mathcal { X }$ is the same as the weak topology it has if it is considered as a real linear space (Exercise $4 ) .$ This will be used in the future.

1.6. Definition. If $A \subseteq { \mathcal { X } }$ , the polar of A, denoted by $A ^ { \circ }$ , is the subset of $\mathcal { X } ^ { * }$ defined by

$$
A ^ { \circ } \equiv \{ x ^ { * } \in \mathcal { X } ^ { * } : | \langle a , x ^ { * } \rangle | \leqslant 1 { \mathrm { ~ f o r ~ a l l ~ } } a { \mathrm { ~ i n ~ } } A \} .
$$

If $B \subseteq { \mathcal { X } } ^ { * }$ , the prepolar of $B ,$ denoted by ${ } ^ { \circ } B ,$ is the subset of $\mathcal { X }$ defined by

$$
{ \boldsymbol { B } } \equiv \{ { \boldsymbol { x } } \in { \mathcal { X } } : | \langle { \boldsymbol { x } } , { \boldsymbol { b } } ^ { * } \rangle | \leqslant 1 { \mathrm { ~ f o r ~ a l l ~ } } { \boldsymbol { b } } ^ { * } { \mathrm { ~ i n ~ } } { \boldsymbol { B } } \} .
$$

If $A \subseteq { \mathcal { X } }$ the bipolar of A is the set ${ } ^ { \circ } ( A ^ { \circ } )$ . If there is no confusion, then it is also denoted by ${ } ^ { \circ } A ^ { \circ }$

The prototype for this idea is that if A is the unit ball in a normed space, $A ^ { \circ }$ is the unit ball in the dual space.

## 1.7. Proposition. If $A \subseteq { \mathcal { X } } .$ , then

(a) $A ^ { \circ }$ is convex and balanced.

(b) ${ \boldsymbol { I f } } ~ { \boldsymbol { A } } _ { 1 } \subseteq { \boldsymbol { A } }$ , then $A ^ { \circ } \subseteq A _ { 1 } ^ { \circ }$

(c) $\scriptstyle { \boldsymbol { I } } { \boldsymbol { f } } \; { \boldsymbol { \alpha } } \in \mathbf { F }$ and $\alpha \ne 0,(\alpha A)^{\circ}=\alpha^{-1}A^{\circ}$

(d) $A \subseteq { } ^ { \circ } A ^ { \circ }$

(e) $A^{\circ} = (^{\circ}A^{\circ})^{\circ}$

ProoF. The proofs of parts (a) through (d) are left as an exercise. To prove (e) note that $A \subseteq { } ^ { \circ } A ^ { \circ }$ by (d), so $( ^ { \circ } \pmb { A } ^ { \circ } ) ^ { \circ } \subseteq \pmb { A } ^ { \circ }$ by (b). But $A ^ { \circ } \subseteq { } ^ { \circ } ( A ^ { \circ } ) ^ { \circ }$ by an analog of (d) for prepolars. Also, $(A^{\circ})^{\circ} = (^{\circ}A^{\circ})^{\circ}$ ■

There is an analogous result for prepolars. In fact, it is more than analogy that is at work here. By Theorem 1.3, $( \mathcal { X } ^ { * } , \mathrm { w k } ^ { * } ) ^ { * } = \mathcal { X }$ . Thus the result for prepolars is a consequence of the preceding proposition.

If A is a linear manifold in X and $x ^ { * }   \in   A ^ { \circ }$ , then $t a   \in   A$ for all $t   >   0$ and a in A. So $1 \geqslant \left| \left\langle t a , x ^ { * } \right\rangle \right| = t \left| \left\langle a , x ^ { * } \right\rangle \right|$ . Letting $t   \rightarrow   \infty$ show that $A ^ { \circ } = A ^ { \perp }$ , where

$$
A ^ { \perp } \equiv \{ x ^ { * } \mathrm { i n } \mathcal { X } ^ { * } : \langle a , x ^ { * } \rangle = 0 \mathrm { f o r a l l } a \mathrm { i n } A \} .
$$

Similarly, if B is a linear manifold in ${ \mathcal { X } } ^ { \star } , { } ^ { \circ } { \pmb { B } } = { } ^ { \perp } { \pmb { B } } ,$ where

$$
{ } ^ { \perp } B \equiv \{ x \mathrm { i n } \mathcal { X } : \langle x , b ^ { * } \rangle = 0 \mathrm { f o r a l l } b ^ { * } \mathrm { i n } B \} .
$$

The next result is a slight generalization of Corollary IV.3.12

1.8. Bipolar Theorem. If X is a LCS and $A \subseteq { \mathcal { X } }$ , then ${ } ^ { \circ } A ^ { \circ }$ is the closed convex balanced hull of A.

PROOF. Let $A _ { 1 }$ be the intersection of all closed convex balanced subsets of X that contain A. It must be shown that $A _ { 1 } = { } ^ { \circ } A ^ { \circ }$ . Since ${ } ^ { \circ } A ^ { \circ }$ is closed, convex, and balanced and $A \subseteq { } ^ { \circ } A ^ { \circ }$ , it follows that $A _ { 1 } \subseteq { } ^ { \circ } A ^ { \circ }$

Now assume that $x _ { 0 } { \in } { \mathcal { X } } \backslash A _ { 1 } . A _ { 1 }$ is a closed convex balanced set so by (IV.3.13) there is an $x ^ { * }$ in $\mathcal { X } ^ { * }$ , an α in R, and an $\varepsilon   >   0$ such that

$$
\mathrm{Re}\langle a_{1},x^{*}\rangle<\alpha<\alpha+\varepsilon<\mathrm{Re}\langle x_{0},x^{*}\rangle
$$

for all $a _ { 1 }$ in $A _ { 1 }$ . Since $0 \in A _ { 1 } , 0 = \langle 0 , x ^ { * } \rangle < \alpha .$ By replacing $x ^ { * }$ with $\alpha ^ { - 1 } x ^ { * }$ it follows that there is an $\varepsilon   >   0$ (not the same as the first ε) such that

$$
\mathrm{Re}\langle a_{1},x^{*}\rangle < 1 < 1 + \varepsilon < \mathrm{Re}\langle x_{0},x^{*}\rangle
$$

for all $a _ { 1 }$ in $A _ { 1 } . \mathrm { I f } a _ { 1 }   \in   A _ { 1 }$ and $\langle a _ { 1 } , x ^ { * } \rangle = | \langle a _ { 1 } , x ^ { * } \rangle | e ^ { - i \theta }$ , then $e ^ { - i \theta } a _ { 1 }   \in   { \cal A } _ { 1 }$ and SO

$$
| \langle a _ { 1 } , x ^ { * } \rangle | = \mathrm { R e } \langle e ^ { - i \theta } a _ { 1 } , x ^ { * } \rangle < 1 < \mathrm { R e } \langle x _ { 0 } , x ^ { * } \rangle
$$

for all $a _ { 1 }$ in $A _ { 1 }$ . Hence $x ^ { * } { \in } A _ { 1 } ^ { \circ }$ , and $x _ { 0 } \notin ^ { \circ } A ^ { \circ }$ . That is, $\mathcal { X } \backslash A _ { 1 } \subseteq \mathcal { X } \backslash ^ { \circ } A ^ { \circ }$

1.9. Corollary. If X is a LCS and $B \subseteq { \mathcal { X } } ^ { * }$ , then $( ^ { \circ } \pmb { B } ) ^ { \circ }$ is the wk\*closed convex balanced hull of B.

Using the weak and weak\* topologies and the concept of a bounded subset of a LCS (IV.2.5), it is possible to rephrase the results associated with the Principle of Uniform Boundedness (§III.14). As an example we offer the following reformulation of Corollary III.14.5 (which is, in fact, the most general form of the result).

1.10. Theorem. $I f \mathcal { X }$ is a Banach space, Y is a normed space, and $\mathcal { A } \subseteq \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ such that for every x in $\mathcal { X } ,   \{ A x \colon A { \in } { \mathcal { A } } \}$ is weakly bounded in $\mathcal { G } ,$ then $\alpha$ is norm bounded in $\mathcal { B } \left( \mathcal { X } , \mathcal { Y } \right)$

EXERCISES

1. Show that wk is the smallest topology on $\mathcal { X }$ such that each $x ^ { * }$ in $\mathcal { X } ^ { * }$ is continuous.

2. Show that wk\* is the smallest topology on $\mathcal { X } ^ { * }$ such that for each x in $\mathcal { X } ,$ $x ^ { * } { \mapsto } \langle x , x ^ { * } \rangle$ is continuous.

3. Prove Theorem 1.3.

4. Let $\mathcal { X }$ be a complex LCS and let $\mathcal { X } _ { \mathbf { R } } ^ { * }$ denote the collection of all continuous real linear functionals on $\mathcal { X }$ Use the elements of $\mathcal { X } _ { \mathbf { R } } ^ { * }$ to define seminorms on $\mathcal { X }$ and let $\sigma ( \mathcal { X } , \mathcal { X } _ { \mathbb { R } } ^ { * } )$ be the corresponding topology. Show that $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } ) = \sigma ( \mathcal { X } , \mathcal { X } _ { \mathrm { ~ \tiny ~ R ~ } } ^ { * } )$

5. Prove the remainder of Proposition 1.7.

6. If $A \subseteq { \mathcal { X } }$ , show that A is weakly bounded if and only if $A ^ { \circ }$ is absorbing in $\mathcal { X } ^ { * }$

7. Let $\mathcal { X }$ be a normed space and let $\{ x _ { n } \}$ be a sequence in $\mathcal { X }$ such that $x _ { n }   \to   x$ weakly. Show that there is a sequence $\{ y _ { n } \}$ such that $y _ { n } \in \mathsf { c o } \left\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \right\}$ and 11 $y _ { n } - x \parallel \rightarrow 0 .$ (Hint: use Theorem 1.4.)

8. If $\mathcal { H }$ is a Hilbert space and $\{ h _ { n } \}$ is a sequence in $\mathcal { H }$ such that $h _ { n }   \rightarrow   h$ weakly and $\| \boldsymbol { h } _ { n } \| \rightarrow \| \boldsymbol { h } \|$ , then $\| \boldsymbol{h}_n - \boldsymbol{h} \| \rightarrow 0.$ (The same type of result is true for LP-spaces if $1 < p < \infty$ . See W.P. Novinger [1972].)

9. If $\mathcal { X }$ is a normed space show that the norm on $\mathcal { X }$ is lower semicontinuous for the weak topology and the norm of $\mathcal { X } ^ { * }$ is lower semicontinuous for the weak-star topology.

10. Suppose $\mathcal { X }$ is an infinite-dimensional normed space. If $S = \{ x \in { \mathcal { X } } : \| x \| = 1 \}$ , then the weak closure of S is $\{ x \colon \|   x   \| \leqslant 1 \}$

## §2. The Dual of a Subspace and a Quotient Space

In §III.4 the quotient of a normed space $\mathcal { X }$ by a closed subspace $\mathcal { M }$ was defined and in (III.10.2) it was shown that the dual of a quotient space $\mathcal { X } / \mathcal { M }$ is isometrically isomorphic to $\mathcal { M } ^ { \perp }$ . These results are generalized in this section to the setting of a LCS and, moreover, it is shown that when $( \mathcal { X } / \mathcal { M } ) ^ { * }$ and $\mathcal { M } ^ { \perp }$ are identified, the weak-star topology on $( \mathcal { X } / \mathcal { M } ) ^ { * }$ is precisely the relative weak-star topology that $\mathcal { M } ^ { \perp }$ receives as a subspace of $\mathcal { X } ^ { * }$

The first result was presented in abbreviated form as Exercise IV.1.16.

2.1. Proposition. If p is a seminorm on $x , \mathcal { M }$ is a linear manifold in $\mathcal { X }$ , and $\bar { p } \colon \mathcal { X } / \mathcal { M } \to [ 0 , \infty )$ is defined by

$$
\bar { p } ( x + \mathcal { M } ) = \inf \left\{ p ( x + y ) : y \in \mathcal { M } \right\} ,
$$

then $\bar { p }$ is a seminorm on $\alpha / \mathcal { M }$ If X is a locally convex space and $\mathcal { P }$ is the family of all continuous seminorms on $\mathcal { X }$ , then the family $\bar { \mathcal { P } }   \equiv   \{ \bar { p }   :   p   \in   \mathcal { P } \}$ defines the quotient topology on $x / M$

PROOF. Exercise.

Thus if $\mathcal { X }$ is a LCS and $\mathcal { M } \leqslant \mathcal { X } ,$ then $x / M$ is a LCS. Let $f \in ( \mathcal { X } / \mathcal { M } ) ^ { * }$ . If $\mathcal { Q } \colon \mathcal { X }   \to   \mathcal { X } / \mathcal { M }$ is the natural map, then $f \circ Q \in \mathcal { X } ^ { * }$ . Moreover, $f \circ g \in \mathcal { M } ^ { \perp }$ . Hence $f { \mapsto } f { \circ } Q$ is a map of $( \mathcal { X } / \mathcal { M } ) ^ { * } \rightarrow \mathcal { M } ^ { \perp } \subseteq \dot { \mathcal { X } ^ { * } }$

2.2. Theorem. If X is a $\mathrm { L C S } ,   \mathcal { M } \leq \mathcal { X }$ , and $\mathcal { Q } \colon \mathcal { X }   \to   \mathcal { X } / \mathcal { M }$ is the natural map, then $f { \mapsto } f ^ { \circ } Q$ defines a linear bijection between $( \mathcal { X } / \mathcal { M } ) ^ { * }$ and $\mathcal { M } ^ { \perp } . \; I f \; ( \mathcal { X } / \mathcal { M } ) ^ { * }$ has its weak-star topology $\sigma ( ( \mathcal { X } / \mathcal { M } ) ^ { * } , \mathcal { X } / \mathcal { M } )$ and $\mathcal { M } ^ { \perp }$ has the relative weak-star topology $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } ) | \mathcal { M } ^ { \perp }$ , then this bijection is a homeomorphism. If $\mathcal { X }$ is $a$ normed space, then this bijection is an isometry.

PROOF. Let $\rho : ( \mathcal { X } / \mathcal { M } ) ^ { * } \to \mathcal { M } ^ { \perp }$ be defined by $\rho ( f ) = f \circ Q$ . It was shown prior to the statement of the theorem that $\rho$ is well defined and maps $( \mathcal { X } / \mathcal { M } ) ^ { * }$ into $\mathcal { M } ^ { \perp }$ . It is easy to see that $\rho$ is linear and if $0 = \rho ( f ) = f ^ { \circ } Q ,$ then $f = 0$ since $Q$ is surjective. So $\rho$ is injective. Now let $x ^ { * } \in \mathcal { M } ^ { \perp }$ and define $f \colon \mathcal { X } / \mathcal { M } \to \mathbb { F }$ by $f ( x + \mathcal { M } ) = \langle x , x ^ { * } \rangle$ . Because $\mathcal { M } \subseteq \ker x ^ { * } , f$ is well defined and linear. Also, $Q ^ { - 1 } \{ x + \mathcal { M } \colon | f ( x + \mathcal { M } ) | < 1 \} = \{ x \in \mathcal { X } \colon | \langle x , x ^ { * } \rangle | < 1 \}$ and this is open in X since $x ^ { * }$ is continuous. Thus $\left\{ x + \mathcal { M } \colon | f ( x + \mathcal { M } ) | < 1 \right\}$ is open in $x / M$ and so $f$ is continuous. Clearly $\rho ( f ) = x ^ { * } ,$ so $\rho$ is a bijection.

If $\mathcal { X }$ is a normed space, it was shown in (III.10.2) that $\rho$ is an isometry. It remains to show that $\rho$ is a weak-star homeomorphism. Let v $\mathbf { v } \mathbf { k } ^ { * } = \sigma ( \mathcal { X } ^ { * } , \mathcal { X } )$ and let $\sigma ^ { * } = \sigma ( ( \mathcal { X } / \mathcal { M } ) ^ { * } , \mathcal { X } / \mathcal { M } ) . \mathrm { ~ I f ~ } \{ f _ { i } \}$ is a net in $( \mathcal { X } / \mathcal { M } ) ^ { * }$ and $f _ { i }   \rightarrow   0 ( \sigma ^ { * } ) ,$ then for each x in $\mathcal { X } , \langle x , \rho ( f _ { i } ) \rangle = f _ { i } ( Q ( x ) ) \rightarrow 0$ Hence $\rho ( f _ { i } ) \to 0 ( \mathrm { w k } ^ { * } )$ Conversely, if $\rho ( f _ { i } ) \to 0 ( \mathrm { w k } ^ { * } )$ , then for each x in X, $f _ { i } ( x + \mathcal { M } ) = \langle x , \rho ( f _ { i } ) \rangle \rightarrow 0 ;$ hence $f _ { i }   \rightarrow   0 ( \sigma ^ { * } )$

Once again let $\mathcal { M } \leq \mathcal { X } . \mathrm { I f } x ^ { * } \in \mathcal { X } ^ { * }$ , then the restriction of $\mathcal { X } ^ { * }$ to $\mathcal { M } , x ^ { * } | \mathcal { M }$ belongs to $\mathcal { M } ^ { * }$ . Also, the Hahn-Banach Theorem implies that the map $x ^ { * }   \mapsto   x ^ { * } | { \mathcal { M } }$ is surjective. If $\rho ( x ^ { * } )   =   x ^ { * } | \mathcal { M }$ , then $\rho \colon \mathcal { X } ^ { * }   \to   \mathcal { M } ^ { * }$ is clearly linear as well as surjective. It fails, however, to be injective. How does it fail? It's easy to see that ker $p = M ^ { \perp }$ . Thus $\rho$ induces a linear bijection $\tilde { \rho } : \mathcal { X } ^ { * } / \mathcal { M } ^ { \perp } \to \mathcal { M } ^ { * }$

2.3. Theorem. If X is a $\mathrm { L C S } , \mathcal { M } \leq \mathcal { X }$ , and $\rho \colon \mathcal { X } ^ { * }   \to   \mathcal { M } ^ { * }$ is the restriction map, then $\rho$ induces a linear bijection $\tilde { \rho } \colon \mathcal { X } ^ { * } / \mathcal { M } ^ { \perp } \to \mathcal { M } ^ { * } . I f \mathcal { X } ^ { * } / \mathcal { M } ^ { \perp }$ has the quotient topology induced by $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } )$ and $\mathcal { M } ^ { * }$ has its weak-star topology $\sigma ( \mathcal { M } ^ { * } , \mathcal { M } )$ then $\tilde { \rho }$ is a homeomorphism. If X is a normed space, then $\tilde { \rho }$ is an isometry.

PROOF. The fact that $\tilde { \rho }$ is an isometry when $\mathcal { X }$ is a normed space was shown in (III.10.1). Let wl $\mathbf { k } ^ { * }   =   \sigma ( \mathcal { M } ^ { * } , \mathcal { M } )$ and let $\eta ^ { * }$ be the quotient topology on $x ^ { * } / d ^ { \perp }$ defined by $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } )$ . Let $\mathcal { Q } \colon \mathcal { X } ^ { * }   \to   \mathcal { X } ^ { * } / \mathcal { M } ^ { \perp }$ be the natural map. Therefore the diagram

![](images/page_143_image_8.jpg)

$$
\begin{align*}\mathcal{Q}^{-1}(\tilde{\rho}^{-1}\{y^{\bullet}\in\mathcal{M}^{\bullet};|\langle y,y^{\bullet}\rangle|<1\})&=\mathcal{Q}^{-1}\{x^{\bullet}+\mathcal{M}^{\perp};|\langle y,x^{\bullet}\rangle|<1\}\\&=\{x^{\bullet}\in\mathcal{X}^{\bullet};|\langle y,x^{\bullet}\rangle|<1\},\end{align*}
$$

commutes. If $y \in \mathcal { M } _ { 1 }$ then the commutativity of the diagram implies that