If $A \subseteq { \mathcal { H } }$ , Let $A ^ { \perp }   \equiv   \{   f   \in   \mathcal { H } \colon   f   \perp   g$ for all g in $\left. A \right\}$ . It is easy to see that $A ^ { \perp }$ is a closed linear subspace of $\mathcal { H }$

Note that Theorem 2.6, together with the uniqueness statement in Theorem 2.5, shows that if $\mathcal { M }$ is a closed linear subspace of $\mathcal { H }$ and $h \in \mathcal { H }$ then there is a unique element $f _ { 0 }$ in M such that $h - f _ { 0 } \in \mathcal { M } ^ { \perp }$ . Thus a function $P : \mathcal { H } \rightarrow \mathcal { M }$ can be defined by $P h   =   f _ { 0 }$

2.7. Theorem. If M is a closed linear subspace of $\mathcal { H }$ and $h \in \mathcal { H } _ { 1 }$ let Ph be the unique point in M such that $h - P h \perp \mathcal { M }$ Then

(a) P is a linear transformation on $\mathcal { H } ,$

(b) $\| P h \| \leqslant \| h \|$ for every h in $\mathcal { H } ,$

(c) $P ^ { 2 } = P { \mathrm { ~ ( h e r e } }$ $P ^ { 2 }$ means the composition of P with itself),

(d) ker $P = M ^ { \perp }$ and ran $P = \mathcal { M } .$

PRooF. Keep in mind that for every h in $\mathcal { H } ,   h - P h \in \mathcal { M } ^ { \perp }$ and $\left\| \boldsymbol{h} - \boldsymbol{P} \boldsymbol{h} \right\| =$ dist $( h , \mathcal { M } )$

(a) Let $h _ { 1 } , h _ { 2 } \in \mathcal { H }$ and $\alpha _ { 1 } , \alpha _ { 2 } \in \mathbb { F }$ If $f \in \mathcal { M } ,$ then $\zeta \left[ \alpha _ { 1 } h _ { 1 } + \alpha _ { 2 } h _ { 2 } \right] - \left[ \alpha _ { 1 } P h _ { 1 } + \right.$ $\alpha _ { 2 } P h _ { 2 } ] , f \rangle = \alpha _ { 1 } \langle h _ { 1 } - P h _ { 1 } , f \rangle + \alpha _ { 2 } \langle h _ { 2 } - P h _ { 2 } , f \rangle = 0.$ By the uniqueness statement of $(2.6), P(\alpha h_{1} + \alpha_{2}h_{2}) = \alpha_{1}Ph_{1} + \alpha_{2}Ph_{2}.$

(b) If $h \in \mathcal { H }$ then $h = (h - P h) + P h, \quad P h \in \mathcal{M},$ and $h - P h \in \mathcal { M } ^ { \perp }$ Thus一 $\| h \| ^ { 2 } = \| h - P h \| ^ { 2 } + \| P h \| ^ { 2 } \geqslant \| P h \| ^ { 2 } .$

(c) If $f \in \mathcal { M } ,$ then $P f   =   f .$ For any h in $\mathcal { H } , P h \in \mathcal { M } ;$ hence $P^{2}h \equiv P(Ph) = Ph$ That is, $P ^ { 2 } = P .$

(d) If $P h = 0 ,$ then $h = h - P h \in \mathcal{M}^{\perp}$ Conversely, if $h { \in } M ^ { \perp }$ , then 0 is the unique vector in $\mathcal { M }$ such that $h - 0 = h \perp \mathcal{M}$ Therefore $P h = 0$ That ran $P = \mathcal { M }$ is clear. ■

2.8. Definition. If M is a closed linear subspace of $\mathcal { H }$ and P is the linear map defined in the preceding theorem, then P is called the orthogonal projection of $\mathcal { H }$ onto M. If we wish to show this dependence of P on $\mathcal { M } ,$ we will denote the orthogonal projection of $\mathcal { H }$ onto $\mathcal { M }$ by $P _ { M }$

It also seems appropriate to introduce the notation $\mathcal { M } \leqslant \mathcal { H }$ to signify that $\mathcal { M }$ is a closed linear subspace of $\mathcal { H }$ . We will use the term linear manifold to designate a linear subspace of $\mathcal { H }$ that is not necessarily closed. A linear subspace of $\mathcal { H }$ will always mean a closed linear subspace.

## 2.9. Corollary. $\mathcal { H } \mathcal { M } \leq \mathcal { H }$ then $( \mathcal { M } ^ { \perp } ) ^ { \perp } = \mathcal { M } .$

ProoF. If I is used to designate the identity operator on $\mathcal { H } ( \mathrm { v i z . } , I h = h )$ and $P = P _ { , \mathcal { M } } ,$ then $I - P$ is the orthogonal projection of $\mathcal { H }$ onto $\mathcal { M } ^ { \perp }$ (Exercise 2). By part (d) of the preceding theorem, $( \mathcal { M } ^ { \perp } ) ^ { \perp } = \ker ( I - P )$ . But $0 = (I - P)h$ iff $h = P h .$ Thus $( \mathcal { M } ^ { \perp } ) ^ { \perp } = \ker ( I - P ) = \operatorname { r a n } P = \mathcal { M } .$ ■

2.10. Corollary. If $A \subseteq { \mathcal { H } }$ , then $( A ^ { \perp } ) ^ { \perp }$ is the closed linear span of A in $\mathcal { H } ,$

The proof is left to the reader; see Exercise 4 for a discussion of the term "closed linear span."

2.11. Corollary. $\mathit { I f } \mathcal { Y }$ is a linear manifold in H, then Y is dense in $\mathcal { H } \mathrm { i f f } \mathcal { Y } ^ { \perp } = ( 0 )$

PROOF. Exercise.

## EXERCISES

1. Let $\mathcal { H }$ be a Hilbert space and suppose f and g are linearly independent vectors in H with $\|   f   \| = \|   g   \| = 1$ . Show that $\| t f + ( 1 - t ) g \| < 1$ for $0 < t < 1$ . What does this say about $\{ h \in \mathcal { H } : \| h \| \leqslant 1 \} ?$

2. If $\mathcal { M } \leq \mathcal { H }$ and $P = P _ { , \mathcal { M } } ,$ show that $I - P$ is the orthogonal projection of $\mathcal { H }$ onto $\mathcal { M } ^ { \perp }$

3. If $\mathcal { M } \leqslant \mathcal { H } ,$ show that $\mathcal { M } \cap \mathcal { M } ^ { \perp } = ( 0 )$ and every h in $\mathcal { H }$ can be written as $h = f + g$ where $f \in \mathcal { M }$ and $g \in \mathcal { M } ^ { \perp }$ . If $\mathcal { M } + \mathcal { M } ^ { \perp } \equiv \{ ( f , g ) \colon f { \in } \mathcal { M } , g { \in } \mathcal { M } ^ { \perp } \}$ and $T ;$ $\mathcal { M } + \mathcal { M } ^ { \perp } \rightarrow \mathcal { H }$ is defined by $T ( f , g ) = f + g ,$ show that T is a linear bijection and a homeomorphism if $1 1 + 1 1 ^ { \perp }$ is given the product topology. (This is usually phrased by stating the M and $\mathcal { M } ^ { \perp }$ are topologically complementary in $\mathcal { H } . )$

4. If $A \subseteq { \mathcal { H } }$ , let $\vee A \equiv$ the intersection of all closed linear subspaces of $\mathcal { H }$ that contain A. V A is called the closed linear span of A. Prove the following:

(a) $\vee A \leqslant \mathcal{H}$ andV A is the smallest closed linear subspace of $\mathcal { H }$ that contains A.

(b) $\vee A =$ the closure of $\left\{ \sum_{k = 1}^{n} \alpha_{k} f_{k} : n \geqslant 1, \alpha_{k} \in \mathbb{F}, f_{k} \in A \right\}$

5. Prove Corollary 2.10.

6. Prove Corollary 2.11.

## §3. The Riesz Representation Theorem

The title of this section is somewhat ambiguous as there are at least two Riesz Representation Theorems. There is one so-called theorem that represents bounded linear functionals on the space of continuous functions on a compact Hausdorff space. That theorem will be discussed later in this book. The present section deals with the representation of certain linear functionals on Hilbert space. But first we have a few preliminaries to dispose of.

3.1. Proposition. Let $\mathcal { H }$ be a Hilbert space and $L \colon { \mathcal { H } } \to \mathbb { F }$ a linear functional. The following statements are equivalent.

(a) L is continuous.

(b) L is continuous at 0.

(c) L is continuous at some point.

(d) There is a constant $c   >   0$ such that $| L ( h ) | \leqslant c \| h \|$ for every h in $\mathcal { H }$

PROOF. It is clear that $(a) \Rightarrow (b) \Rightarrow (c)$ and $(d) \Rightarrow (b)$ . Let's show that $(c) \Rightarrow (a)$ and $( b ) \Rightarrow ( d )$

$(c) \Rightarrow (a)$ Suppose L is continuous at $h _ { 0 }$ and h is any point in $\mathcal { H }$ If $h _ { n }   \rightarrow   h$ in $\mathcal { H }$ , then $h_{n}-h+h_{0}\rightarrow h_{0}$ . By assumption, $L(h_0) = \lim_{} \left[ L(h_n - h + h_0) \right] =$ lim $\left[ L ( h _ { n } ) - L ( h ) + L ( h _ { 0 } ) \right] = \operatorname* { l i m } L ( h _ { n } ) - L ( h ) + L ( h _ { 0 } )$ .Hence $L(h) = \lim_{n \to \infty} L(h_n)$

(b)⇒(d): The definition of continuity at 0 implies that $L ^ { - 1 } ( \{ \alpha { \in } \mathbb { F } { : } | \alpha | < 1 \} )$ contains an open ball about 0. So there is $\begin{array} { r l } { \mathfrak { a } } & { { } \delta > 0 } \end{array}$ such that $B ( 0 ; \delta ) \subseteq L ^ { - 1 } ( \{ \alpha \in \mathbb { F } : | \alpha | < 1 \} )$ . That is, $\| h \| < \delta$ implies $| L ( h ) | < 1$ . If h is an arbitrary element of $\mathcal { H }$ and $\varepsilon   >   0 ,$ , then $\| \delta ( \| h \| + \varepsilon ) ^ { - 1 } h \| < \delta$ Hence

$$
1 > \left| L \left[ \frac{\delta h}{\| h \| + \varepsilon} \right] \right| = \frac{\delta}{\| h \| + \varepsilon} \left| L(h) \right|;
$$

thus

$$
| L ( h ) | < \frac { 1 } { \delta } ( \| h \| + \varepsilon ) .
$$

Letting $\varepsilon   \to   0$ we see that (d) holds with $c = 1 / \delta$

3.2. Definition. A bounded linear functional L on $\mathcal { H }$ is a linear functional for which there is a constant $c   >   0$ such that $| L ( h ) | \leqslant c \| h \|$ for all h in $\mathcal { H } .$ In light of the preceding proposition, a linear functional is bounded if and only if it is continuous.

For a bounded linear functional $L \colon { \mathcal { H } } \to \mathbb { F } ,$ define

$$
\| L \| = \sup \{ | L ( h ) | : \| h \| \leqslant 1 \}.
$$

Note that by definition, $\| L \| < \infty ; \| L \|$ is called the norm of L.

## 3.3. Proposition. If L is a bounded linear functional, then

$$
\begin{align*}\left\| L \right\| = & \sup \left\{ \left| L(h) \right| : \left\| h \right\| = 1 \right\} \\= & \sup \left\{ \left| L(h) \right| / \left\| h \right\| : h \in \mathcal{H},   h \neq 0 \right\} \\= & \inf \left\{ c > 0 : \left| L(h) \right| \leqslant c \left\| h \right\|,   h   in   \mathcal{H} \right\}.\end{align*}
$$

$Also, $| L ( h ) | \leqslant \| L \|$ $\| h \|$$ for every h in $\mathcal { H } .$

PROOF. Let $\alpha = \inf \left\{ c > 0 : |L(h)| \leqslant c \|h\| \right\}$ , h in $\mathcal { H } \}$ . It will be shown that $\| L \| = \alpha ;$ the remaining equalities are left as an exercise. If $\varepsilon   >   0 .$ then the definition of $\| L \|$ shows that $| L ( ( \| h \| + \varepsilon ) ^ { - 1 } h ) | \leqslant \| L \|$ . Hence $| L ( \boldsymbol { h } ) | \leqslant \| L \| ( \| \boldsymbol { h } \| + \varepsilon ) .$ Letting $\varepsilon   \to   0$ shows that $| L ( h ) | \leqslant \| L \| \| h \|$ for all h. So the definition of α shows that $\alpha \leqslant \| L \|$ . On the other hand, $\mathrm{if} \left| L(h) \right| \leq c \left\| h \right\|$ for all h, then $\| L \| \leqslant c .$ Hence $\| L \| \leqslant \alpha .$ ■

Fix an $h _ { 0 }$ in $\mathcal { H }$ and define $L \colon { \mathcal { H } } \to \mathbb { F }$ by $L ( h ) = \langle h , h _ { 0 } \rangle$ . It is easy to see that L is linear. Also, the CBS inequality gives that $| L ( h ) | = | \langle h , h _ { 0 } \rangle | \leqslant$ $\| \boldsymbol { h } \|   \| \boldsymbol { h } _ { 0 } \|$ . So L is bounded and $\| L \| \leqslant \| \boldsymbol { h } _ { 0 } \|$ . In fact, $L ( \boldsymbol { h } _ { 0 } / \| \boldsymbol { h } _ { 0 } \| ) =$ $\langle h _ { 0 } / \| h _ { 0 } \| , h _ { 0 } \rangle = \| h _ { 0 } \|$ |, so that $\| \boldsymbol { L } \| = \| \boldsymbol { h } _ { 0 } \|$ . The main result of this section provides a converse to these observations.

3.4. The Riesz Representation Theorem. If $L \colon { \mathcal { H } } \to \mathbb { F }$ is a bounded linear functional, then there is a unique vector $h _ { 0 }$ in $\mathcal { H }$ such that $L ( h ) = \langle h , h _ { 0 } \rangle$ for every h in $\mathcal { H }$ . Moreover, $\|   { \boldsymbol { L } }   \| = \|   { \boldsymbol { h } } _ { 0 }   \|$

PROOF. Let $\mathcal { M } = \ker L$ . Because L is continuous M is a closed linear subspace of $\mathcal { H }$ . Since we may assume that $\mathcal { M } \neq \mathcal { H } , \mathcal { M } ^ { \perp } \neq ( 0 )$ . Hence there is a vector $f _ { 0 }$ in $\mathcal { M } ^ { \perp }$ such that $L ( f _ { 0 } ) = i$ . Now if $h \in \mathcal { H }$ and $\alpha = L ( h )$ , then $L(h - \alpha f_0) = L(h) - \alpha = 0;$ SO $h - L(h) f_0 \in \mathcal{M}$ Thus

$$
\begin{array} { r l } { 0 = \langle h - L ( h ) f _ { 0 } , f _ { 0 } \rangle } & { { } } \\ { = \langle h , f _ { 0 } \rangle - L ( h ) \| f _ { 0 } \| ^ { 2 } . } & { { } } \end{array}
$$

So if $h _ { 0 } = \| f _ { 0 } \| ^ { - 2 } f _ { 0 } , L ( h ) = \langle h , h _ { 0 } \rangle$ for all h in $\mathcal { H }$

If $h _ { 0 } ^ { \prime } \in \mathcal { H }$ such that $\langle h , h _ { 0 } \rangle = \langle h , h _ { 0 } ^ { \prime } \rangle$ for all h, then $h _ { 0 } - h _ { 0 } ^ { \prime } \bot \mathcal { H }$ . In particular, $h _ { 0 } - h _ { 0 } ^ { \prime } \bot h _ { 0 } - h _ { 0 } ^ { \prime }$ and so $h _ { 0 } ^ { \prime } = h _ { 0 }$ The fact that $\| \boldsymbol { L } \| = \| \boldsymbol { h } _ { 0 } \|$ was shown in the discussion preceding the theorem. ■

3.5. Corollary. $I f \left( X , \Omega , \mu \right)$ is a measure space and F: $L ^ { 2 } ( \mu )   \to   \mathbb { F }$ is a bounded linear functional, then there is a unique $h _ { 0 }$ in $L ^ { 2 } ( \mu )$ such that

$$
F ( h ) = \int h \overline { { h _ { 0 } } } d \mu
$$

for every h in $L ^ { 2 } ( \mu )$

Of course the preceding corollary is a special case of the theorem on representing bounded linear functionals on $L ^ { p } ( \mu ) , 1 \leqslant p < \infty$ . But it is interesting to note that it is a consequence of the result for Hilbert space [and the result that $L ^ { 2 } ( \mu )$ is a Hilbert space].

## EXERCISES

1. Prove Proposition 3.3

2. Let $\mathcal { H } = l ^ { 2 } ( \mathbb { N } )$ . If $N \geqslant 1$ and $L \colon { \mathcal { H } } \to \mathbb { F }$ is defined by $L ( \{ \alpha _ { n } \} ) = \alpha _ { N }$ , find the vector $h _ { 0 }$ in  such that $L ( h ) = \langle h , h _ { 0 } \rangle$ for every h in $\mathcal { H }$

3. Let $\mathcal { H } = l ^ { 2 } ( \mathbb { N } \cup \{ 0 \} )$ . (a) Show that if $\{ x _ { n } \} \in \mathcal { H }$ , then the power series $\sum _ { n = 0 } ^ { \infty } \alpha _ { n } z ^ { n }$ has radius of convergence $\geqslant 1$ (b) $\mathrm { ~ I f ~ } \left| \lambda \right| < 1$ and $L \colon \mathcal { H }   \to   \mathbb { F }$ is defined by $L ( \{ \alpha _ { n } \} ) = \sum _ { n = 0 } ^ { \infty } \alpha _ { n } \lambda ^ { n }$ , find the vector $h _ { 0 }$ in H such that $L ( h ) = \langle h , h _ { 0 } \rangle$ for every h in f. (c) What is the norm of the linear functional L defined in (b)?

4. With the notation as in Exercise 3, define L: $\mathcal { H } \rightarrow \mathbb { F }$ by $L(\{ \alpha_n \}) = \sum_{n = 1}^{\infty} n \alpha_n \lambda^{n - 1}$ where $| \lambda | < 1$ . Find a vector $h _ { 0 }$ in $\mathcal { H }$ such that $L ( h ) = \langle h , h _ { 0 } \rangle$ for every h in $\mathcal { H } .$

5. Let  be the Hilbert space described in Example 1.8. If $0 < t \leqslant 1$ , define $L \colon \mathcal { H } \to \mathbb { F }$ by $L ( h ) = h ( t )$ Show that L is a bounded linear functional, find $\| L \|$ , and find the vector $h _ { 0 }$ in $\mathcal { H }$ such that $L ( h ) = \langle h , h _ { 0 } \rangle$ for all h in $\mathcal { H }$

6. Let $\mathcal { H } = L ^ { 2 } ( 0 , 1 )$ and let $C ^ { ( 1 ) }$ be the set of all continuous functions on $[ 0 , 1 ]$ that have a continuous derivative. Let $t   \in   [ 0 , 1 ]$ and define $L \colon C ^ { ( 1 ) }   \to   \mathbb { F }$ by $L ( h ) = h ^ { \prime } ( t )$ Show that there is no bounded linear functional on $\mathcal { H }$ that agrees with L on $C ^ { ( 1 ) }$

## §4. Orthonormal Sets of Vectors and Bases

It will be shown in this section that, as in Euclidean space, each Hilbert space can be coordinatized. The vehicle for introducing the coordinates is an orthonormal basis. The corresponding vectors in $\mathbf { F } ^ { d }$ are the vectors $\{ e _ { 1 } , e _ { 2 } , \ldots , e _ { d } \}$ , where $e _ { k }$ is the d-tuple having a 1 in the kth place and zeros elsewhere.

4.1. Definition. An orthonormal subset of a Hilbert space $\mathcal { H }$ is a subset $\mathcal { E }$ having the properties: (a) for $e$ in $\delta ,   \| e \| = 1 ;$ (b) if $e _ { 1 } ,   e _ { 2 } { \in } { \mathcal { O } }$ and $e _ { 1 } \neq e _ { 2 }$ , then $e _ { 1 } \bot e _ { 2 }$

A basis for $\mathcal { H }$ is a maximal orthonormal set.

Every vector space has a Hamel basis (a maximal linearly independent set). The term “basis" for a Hilbert space is defined as above and it relates to the inner product on $\mathcal { H }$ . For an infinite-dimensional Hilbert space, a basis is never a Hamel basis. This is not obvious, but the reader will be able to see this after understanding several facts about bases.

4.2. Proposition. $\iint \delta$ is an orthonormal set in $\mathcal { H } ,$ then there is a basis for $\mathcal { H }$ that contains $\mathcal { E } .$

The proof of this proposition is a straightforward application of Zorn's Lemma and is left to the reader.

4.3. Example. Let $\mathcal { H } = L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ and for n in $\mathbf { z }$ define $e _ { n }$ in $\mathcal { H }$ by $e _ { n } ( t ) = ( 2 \pi ) ^ { - 1 / 2 }$ exp(int). Then $\{ e _ { n } ;   n { \in } \mathbb { Z } \}$ is an orthonormal set in $\mathcal { H }$ (Here $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ is the space of complex-valued square integrable functions.)

It is also true that the set in (4.3) is a basis, but this is best proved after a bit of theory.

4.4. Example. If $\mathcal { H } = \mathbb { F } ^ { d }$ and for $1 \leqslant k \leqslant d, \; e_{k} =$ the d-tuple with 1 in the kth place and zeros elsewhere, then $\{ e _ { 1 } , \ldots , e _ { d } \}$ is a basis for $\mathcal { H }$

4.5. Example. Let $\mathcal { H } = l ^ { 2 } ( I )$ as in Example 1.7. For each i in I define $e _ { i }$ in $\mathcal { H }$ by $e _ { i } ( i ) = 1$ and $e _ { i } ( j ) = 0$ for $j   \neq   i .$ Then $\{ e _ { i } ;   i { \in } I \}$ is a basis.

The proof of the next result is left as an exercise (see Exercise 5). It is very useful but the proof is not difficult.

4.6. The Gram-Schmidt Orthogonalization Process. If $\mathcal { H }$ is a Hilbert space and $\{ h _ { n } ; \; n { \in } \mathbb { N } \}$ is a linearly independent subset of $\mathcal { H } ,$ , then there is an orthonormal set $\{ e _ { n } ; n \in \mathbb { N } \}$ such that for every $n ,$ the linear space of $\{ e _ { 1 } , \ldots , e _ { n } \}$ equals the linear span of $\{ h _ { 1 } , \ldots , h _ { n } \}$

Remember that $\nabla A$ is the closed linear span of A (Exercise 2.4).

4.7. Proposition. Let $\{ e _ { 1 } , \ldots , e _ { n } \}$ be an orthonormal set in $\mathcal { H }$ and let $\mathcal { M } = \vee \left\{ e _ { 1 } , \ldots , e _ { n } \right\}$ . If P is the orthogonal projection of $\mathcal { H }$ onto M, then

$$
P h = \sum _ { k = 1 } ^ { n } \langle h , e _ { k } \rangle e _ { k }
$$

for all h in $\mathcal { H } ,$

PROOF. Let $\begin{array} { r } { Q h = \sum _ { k = 1 } ^ { n } \left\langle h , e _ { k } \right\rangle e _ { k } . } \end{array}$ $\mathbf { I f } \quad 1 \leqslant j \leqslant n ,$ then $\langle Q h , e _ { j } \rangle =$ $\begin{array} { r } { \sum _ { k = 1 } ^ { n } \langle h , e _ { k } \rangle \langle e _ { k } , e _ { j } \rangle = \langle h , e _ { j } \rangle } \end{array}$ since $e _ { k } \bot e _ { j }$ for $k \neq j .$ Thus $\langle h - Q h , e _ { j } \rangle = 0$ for $1 \leqslant j \leqslant n .$ That is, $h - \varrho h \bot \mathcal { M }$ for every h in $\mathcal { H } .$ Since Qh is clearly a vector in $\mathcal { M } _ { 2 }$ Qh is the unique vector $h _ { 0 }$ in $\mathcal { M }$ such that $\boldsymbol { h } - \boldsymbol { h } _ { 0 } \perp \boldsymbol { \mathcal { M } }$ (2.6). Hence $Q h = P h$ for every h in $\mathcal { H }$ ■

4.8. Bessel's Inequality. $\{ e _ { n } : n \in \mathbb { N } \}$ is an orthonormal set and $h \in \mathcal { H }$ , then

$$
\sum_{n = 1}^{\infty} \left| \left\langle h, e_{n} \right\rangle \right|^{2} \leqslant \left\| h \right\|^{2}.
$$

PROOF. Let $h_{n}=h-\sum_{k = 1}^{n}\left \langle h,e_{k} \right \rangle e_{k}$ . Then $h _ { n } \perp e _ { k }$ for $1 \leqslant k \leqslant n ( \mathrm { W h y ? } )$ By the Pythagorean Theorem,

$$
\begin{align*}\|   h   \|^2 &= \|   h_n   \|^2 + \left\| \sum_{k=1}^n \left\langle   h, e_k \right\rangle e_k \right\|^2 \\&= \|   h_n   \|^2 + \sum_{k=1}^n | \left\langle   h, e_k \right\rangle |^2 \\&\geqslant \sum_{k=1}^n | \left\langle   h, e_k \right\rangle |^2.\end{align*}
$$

Since n was arbitrary, the result is proved.

4.9. Corollary. If E is an orthonormal set in $\mathcal { H }$ and $h \in \mathcal { H }$ , then $\langle h , e \rangle \neq 0$ for at most a countable number of vectors e in $\pmb { \mathscr { E } } .$

PROOF. For each $n \geqslant 1$ let $\mathcal { E } _ { n } = \{ e \in \mathcal { E } : | \langle h , e \rangle | \geqslant 1 / n \}$ . By Bessel's Inequality, $\mathcal { E } _ { n }$ is finite. But $\begin{array} { r } { \bigcup _ { n = 1 } ^ { \infty } \mathcal { Q } _ { n } = \{ e \in \mathcal { E } : \langle h , e \rangle \neq 0 \} } \end{array}$

4.10. Corollary. If E is an orthonormal set and $h \in \mathcal { H }$ , then

$$
\sum_{e \in \mathcal{E}} \left| \left\langle h, e \right\rangle \right|^2 \leqslant \left\| h \right\|^2.
$$

This last corollary is just Bessel's Inequality together with the fact (4.9) that at most a countable number of the terms in the sum differ from zero.

Actually, the sum that appears in (4.10) can be given a better interpretation—a mathematically precise one that will be useful later. The question is, what is meant by $\scriptstyle \sum \{ h _ { i } : i \in I \}$ if $h _ { i } \in \mathcal { H }$ and I is an infinite, possibly uncountable, set? Let $\mathcal { F }$ be the collection of all finite subsets of I and order $\mathcal { F }$ by inclusion, so $\mathcal { F }$ becomes a directed set. For each F in $\mathcal { F }$ , define

$$
h _ { F }   =   \Sigma   \{ h _ { i } ;   i   \in   F \} .
$$

Since this is a finite sum, $h _ { F }$ is a well-defined element of $\mathcal { H }$ . Now $\{ h _ { F } : F \in \mathcal { F } \}$ is a net in $\mathcal { H }$

4.11. Definition. With the notation above, the sum $\scriptstyle \sum \left\{ h _ { i } : \; i \in I \right\}$ converges if the net $\{ h _ { F } : F \in \mathcal { F } \}$ converges; the value of the sum is the limit of the net.

If $\mathcal { H } = \mathbb { F } ,$ the definition above gives meaning to an uncountable sum of scalars. Now Corollary 4.10 can be given its precise meaning; namely, $\scriptstyle \sum \{ | \langle h , e \rangle | ^ { 2 } : e \in { \mathcal { E } } \}$ converges and the value $\leqslant \| h \| ^ { 2 }$ (Exercise 9).

If the set I in Definition 4.11 is countable, then this definition of convergent sum is not the usual one. That is, if $\{ h _ { n } \}$ is a sequence in $\mathcal { H } ,$ then the convergence of $\sum \{ h _ { n } : n \in \mathbb { N } \}$ is not equivalent to the convergence of $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } h _ { n } . } \end{array}$ The former concept of convergence is that defined in (4.11) while the latter means that the sequence $\left\{ \sum_{k = 1}^{n} h_{k} \right\}_{n = 1}^{\infty}$ converges. Even if $\mathcal { H } = \mathbb { F }$ these concepts do not coincide (see Exercise 12). If, however, $\sum \{ h _ { n } : n \in \mathbb { N } \}$ converges, then $\sum _ { n = 1 } ^ { \infty } h _ { n }$ converges (Exercise 10). Also see Exercise 11.

## 4.12. Lemma. If Eis an orthonormal set and $h \in \mathcal { H } _ { j }$ then

$$
\sum \{ \langle h, e \rangle e : e \in \mathcal{E} \}
$$

converges in $\mathcal { H } ,$

PRoOF. By (4.9), there are vectors $e _ { 1 } , e _ { 2 } , \ldots$ in $\mathcal { E }$ such that $\{ e \in \mathcal { G } \}$ $\langle h , e \rangle \neq 0 \} = \{ e _ { 1 } , e _ { 2 } , \ldots \}$ . We also know that $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } | \langle h , e _ { n } \rangle | ^ { 2 } \leqslant \| h \| ^ { 2 } < \infty } \end{array}$ . So if $\varepsilon   >   0 .$ , there is an N such that $\begin{array} { r } { \sum _ { n = N } ^ { \infty } | \langle h , e _ { n } \rangle | ^ { 2 } < \varepsilon ^ { 2 } . } \end{array}$ Let $\boldsymbol { F } _ { 0 } = \{ e _ { 1 } , \ldots , e _ { N - 1 } \}$ and let $\mathcal { F } = \mathfrak { a } \mathbb { I }$ the finite subsets of $\mathcal { E } .$ For F in $\mathcal { F }$ define $h _ { F } \equiv \sum \left\{ \left\langle h , e \right\rangle e \right\}$ $\scriptstyle e \in F \}$ . If F and $G { \in } { \mathcal { F } }$ and both contain $F _ { 0 } ,$ then

$$
\begin{aligned}\| h_{F} - h_{G} \|^{2} &= \sum \{ | \langle h, e \rangle |^{2} : e \in (F \backslash G) \cup (G \backslash F) \}^{2} \\& \leqslant \sum_{n = N}^{\infty} | \langle h, e_{n} \rangle |^{2} \\& < \varepsilon^{2}.\end{aligned}
$$

So $\{ h _ { F } : F \in { \mathcal { F } } \}$ is a Cauchy net in $\mathcal { H }$ Because $\mathcal { H }$ is complete, this net converges. In fact, it converges to $\scriptstyle \sum _ { n = 1 } ^ { \infty } \langle h , e _ { n } \rangle e _ { n }$

4.13. Theorem. $\iint \theta$ is an orthonormal set in $\mathcal { H } ,$ , then the following statements are equivalent.

(a) E is a basis for $\mathcal { H }$

(b) If $h \in \mathcal { H }$ and $h \bot \ell ,$ then $h = 0 .$

(c) V $\delta = \mathcal { H } .$

(d) $If $h { \in } { \mathcal { H } }$$ , then $h = \sum \{ \langle h , e \rangle e : e \in \mathcal { E } \}$

(e) If g and $h \in \mathcal { H }$ then

$$
\langle g , h \rangle = \sum \{ \langle g , e \rangle \langle e , h \rangle : e \in \mathcal { E } \} .
$$

(f) If $h \in \mathcal { H }$ then $\| h \| ^ { 2 } = \sum \{ | \langle h , e \rangle | ^ { 2 } : e \in \mathcal { G } \}$ (Parseval's Identity).

PROOF. (a)⇒(b): Suppose $h \perp \ell$ and $h \neq 0 ;$ then $\mathcal { E } \cup \left\{ \boldsymbol { h } / \left\|   \boldsymbol { h }   \right\| \right\}$ is an orthonormal set that properly contains $\mathcal { E } ,$ contradicting maximality.

(b)⇔(c): By Corollary 2.11, V $\theta = \pi$ if and only if $\pmb { \delta } ^ { \perp } = ( 0 )$

(b)⇒(d): If $h \in \mathcal { H }$ , then $f = h - \sum \{ \langle h, e \rangle e : e \in \mathcal{E} \}$ is a well-defined vector by Lemma 4.12. If $e _ { 1 } \in \mathcal { B }$ then $\langle f , e _ { 1 } \rangle = \langle h , e _ { 1 } \rangle - \sum \{ \langle h , e \rangle \langle e , e _ { 1 } \rangle$ $e \in \mathcal { E } \} = \langle h , e _ { 1 } \rangle - \langle h , e _ { 1 } \rangle = 0 .$ That is, $f \in \theta ^ { \perp }$ . Hence $f = 0 .$ (Is everything legitimate in that string of equalities? We don't want any illegitimate equalities.)

(d)⇒(e): This is left as an exercise for the reader.

(e)⇒(f): Since $\| \boldsymbol{h} \|^2 = \langle \boldsymbol{h}, \boldsymbol{h} \rangle$ , this is immediate.

(f)⇒(a): If  is not a basis, then there is a unit vector $e _ { 0 } \left( \| e _ { 0 } \| = 1 \right)$ in $\mathcal { H }$ such that $e _ { 0 } \bot \ell$ . Hence, $0 = \sum \{ | \langle e _ { 0 } , e \rangle | ^ { 2 } : e \in \mathcal { E } \}$ , contradicting (f).

Just as in finite dimensional spaces, a basis in Hilbert space can be used to define a concept of dimension. For this purpose the next result is pivotal.

4.14. Proposition. If $\mathcal { H }$ is a Hilbert space, any two bases have the same cardinality.

PROOF. Let $\mathcal { E }$ and $\mathcal { F }$ be two bases for $\mathcal { H }$ and put ε = the cardinality of $\mathcal { E } ,$ $\eta = \mathrm { t h e }$ cardinality of $\mathcal { F }$ . If ε or $\eta$ is finite, then $\varepsilon = \eta$ (Exercise 15). Suppose both ε and $\eta$ are infinite. For $e$ in $\mathcal { E } ,$ let $\mathcal { F } _ { e } \equiv \{ f { \in } \mathcal { F } { : } \langle e , f \rangle \neq 0 \} ;$ so $\mathcal { F } _ { e }$ is countable. By (4.13b), each $f$ in $\mathcal { F }$ belongs to at least one set $\mathcal { F } _ { e } , e$ in $\mathcal { E } ,$ That is, $\mathcal { F } = \cup \left\{ \mathcal { F } _ { \mathfrak { e } } ; e { \in } \mathcal { E } \right\}$ . Hence $\eta \leqslant \varepsilon \cdot N_{0} = \varepsilon$ Similarly, $\varepsilon \leqslant \eta$

4.15. Definition. The dimension of a Hilbert space is the cardinality of a basis and is denoted by dim $\mathcal { H }$

If $( X , d )$ is a metric space that is separable and $\left\{ B _ { i } = B ( x _ { i } ; \varepsilon _ { i } ) : i { \in } I \right\}$ is a collection of pairwise disjoint open balls in X, then I must be countable. Indeed, if $D$ is a countable dense subset of $X ,   B _ { i }   \cap   D \neq \Box$ for each i in I. Thus there is a point $x _ { i }$ in $B _ { i } \cap D$ . So $\{ x _ { i } ;   i { \in } I \}$ is a subset of D having the cardinality of $I ;$ thus I must be countable.

4.16. Proposition. If $\mathcal { H }$ is an infinite dimensional Hilbert space, then $\mathcal { H }$ is separable if and only if dim $\mathcal { H } = \aleph _ { 0 }$

PROOF. Let $\mathcal { S }$ be a basis for $\mathcal { H }$ . If $e _ { 1 } , e _ { 2 } { \in } { \mathcal { E } }$ , then $\| e _ { 1 } - e _ { 2 } \| ^ { 2 } = \| e _ { 1 } \| ^ { 2 } +$ $\| e _ { 2 } \| ^ { 2 } = 2$ Hence $\{ B ( e ; 1 / { \sqrt { 2 } } ) : e { \in } { \mathcal { E } } \}$ is a collection of pairwise disjoint open balls in $\mathcal { H }$ From the discussion preceding this proposition, the assumption that $\mathcal { H }$ is separable implies $\mathcal { E }$ is countable. The converse is an exercise.