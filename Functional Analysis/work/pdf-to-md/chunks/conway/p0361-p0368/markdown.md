equivalent. (a) There is a finite positive measure $\mu$ on R such that $m(t) = \int e^{ixt}   d\mu(x)$ for all t in R. (b) m is continuous and if $\alpha _ { 0 } , \ldots , \alpha _ { n } { \in } \mathbb { C }$ and $t _ { 0 } , \ldots , t _ { n } { \in } \mathbb { R }$ , then $\begin{array} { r } { \sum _ { j , k = 0 } ^ { n } m ( t _ { j } - t _ { k } ) \alpha _ { j } \bar { \alpha } _ { k } \geqslant 0 . } \end{array}$ (c) There is a strongly continuous one-parameter unitary group $U ( t )$ and a vector e such that $m ( t ) = \langle U ( t ) e , e \rangle$ for all t. (Hint: Let $\mathcal { H } _ { 0 } = \mathrm { a l l }$ functions $f \colon \mathbb { R }   \to   \mathbb { C }$ that vanish off a finite set.)

3. Let $\{ m _ { n } ; n { \in } \mathbb { Z } \} \subseteq \mathbb { C }$ and show that the following statements are equivalent. (a) There is a positive measure μ on ∂D such that $m _ { n } = \int z ^ { n }   d \mu ( z )$ for all n in Z. (b) If $\alpha_{-n}, \ldots, \alpha_{-1}, \alpha_{0}, \alpha_{1}, \ldots, \alpha_{n} \in \mathbb{C}$ , then $\begin{array} { r } { \sum _ { j , k = - n } ^ { n } m _ { j - k } \alpha _ { j } \bar { \alpha } _ { k } \geqslant 0 . } \end{array}$ (c) There is a unitary operator U and a vector e such that $m_{n}=\left\langle U^{n} e, e\right\rangle$ for all n.

4. Show that the operator A that appears in the proof that (7.1b) implies (7.1c) is cyclic.

# CHAPTER XI Fredholm Theory

This chapter is entirely independent of the preceding one and only tangentially dependent on Chapters VIII and IX.

The purpose of this chapter is to study certain properties of operators on a Hilbert space that are invariant under compact perturbations. That is, we want to study properties of an operator A in $\mathcal { B } ( \mathcal { H } )$ that are also possessed by $A + K$ for every K in $\mathcal { B } _ { 0 } ( \mathcal { H } )$ . The correct view here is to consider this undertaking as a study of the quotient algebra $\mathcal { B } ( \mathcal { H } ) / \mathcal { B } _ { 0 } ( \mathcal { H } ) = \mathcal { B } / \mathcal { B } _ { 0 }$ -the Calkin algebra. Any property associated with an element of the Calkin algebra is a property associated with a coset of operators and vice versa. It is useful—indeed essentialto relate these properties to the way in which the operators act on the underlying Hilbert space.

## §1. The Spectrum Revisited

In Section VII.6 we saw several properties of the spectrum of an operator on a Banach space. In particular, the concepts of point spectrum, $\sigma _ { p } ( A ) ,$ and approximate point spectrum, $\sigma _ { a p } ( A )$ , were explored. It was also shown (VII. 6.7) that $\partial \sigma ( A ) \subseteq \sigma _ { a p } ( A )$ . Recall that $\sigma _ { l } ( A )$ is the left spectrum of A and $\sigma _ { r } ( A )$ is the right spectrum of A.

1.1. Proposition. If $A   \in   \mathcal { B } ( \mathcal { H } ) .$ , the following statements are equivalent.

(a) $\lambda \notin \sigma_{ap}(A);$ that is, inf $\left\{ \left\| (A - \lambda)h \right\| : \left\| h \right\| = 1 \right\} > 0.$

(b) $\operatorname { \mathsf { r a n } } ( A - \lambda )$ is closed and dim ker $( A - \lambda ) = 0 .$

(c) $\lambda \notin \sigma _ { l } ( A )$

(d) $\bar { \lambda } \notin \sigma _ { r } ( A ^ { * } )$

(e) $\mathrm{rank}(A^{*} - \bar{\lambda}) = \mathcal{H}.$

PRooF. By Proposition VII.6.4, (a) and (b) are equivalent. Also, if $B \in \mathcal { B } ( \mathcal { H } )$ then $B ( A - \lambda ) = 1$ if and only if $( A ^ { * } - \bar { \lambda } ) B ^ { * } = 1$ so that (c) and (d) are easily seen to be equivalent.

(b) implies (c). Let $\mathcal { M } = \operatorname { r a n } ( A - \lambda )$ and define $T : \mathcal { H } \rightarrow \mathcal { M }$ by $T h = ( A - \lambda ) h ;$ then T is bijective. By the Open Mapping Theorem, $T ^ { - 1 } : \mathcal { M } \to \mathcal { H }$ is continuous. Define B: $\mathcal { H } \rightarrow \mathcal { H }$ by letting $B = T ^ { - 1 }$ on $\mathcal { M }$ and $B   =   0$ on $\mathcal { M } ^ { \perp }$ Then $B \in \mathcal { B } ( \mathcal { H } )$ and $B ( A - \lambda ) = 1$ . (Note that we used a property of Hilbert spaces here; see Exercise VII.6.5.)

(d) implies (e). Since $\bar { \lambda } \notin \sigma _ { r } ( A ^ { * } ) ,$ , there is an operator C in $\mathcal { B } ( \mathcal { H } )$ such that $( A ^ { * } - \overline { { \lambda } } ) C = 1$ . Hence $\mathcal { H } = ( A ^ { * } - \bar { \lambda } ) C \mathcal { H } \subseteq \mathrm { r a n } ( A ^ { * } - \bar { \lambda } ) .$

(e) implies (a). Let $\mathcal { N } = \ker ( A ^ { * } - \bar { \lambda } ) ^ { \perp }$ and define $T \colon { \mathcal { N } } \to { \mathcal { H } }$ by $T h = ( A ^ { * } - \bar { \lambda } ) h$ . Then T is bijective and hence invertible. Let C: $\mathcal { H } \rightarrow \mathcal { H }$ be defined by $C h = T ^ { - 1 } h .$ Then $C \mathcal { H } = \mathcal { N }$ and $( A ^ { * } - \overline { { \lambda } } ) C = 1$ . Thus $C ^ { * } ( A - \lambda ) = 1$ so that if h∈x, $\| h \| = \|   C ^ { * } ( A - \lambda ) h   \| \leqslant \|   C ^ { * }   \|   \| ( A - \lambda ) h   \|$ Hence inf $\{ \| ( A - \lambda ) h \| \colon \| h \| = 1 \} \geqslant \| C ^ { * } \| ^ { - 1 }$ ■

$$
{ \mathrm { I f ~ } } \Delta \subseteq \mathbb { C } ,   \Delta ^ { * } \equiv \{ { \overline { { \lambda } } } { \mathrm { : ~ } } \lambda   \in   \Delta \} .
$$

1.2. Corollary. If $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ , then ∂o $\sigma ( A ) \subseteq \sigma _ { l } ( A ) \cap \sigma _ { r } ( A ) = \sigma _ { a p } ( A ) \cap \sigma _ { a p } ( A ^ { * } ) ^ { * } .$

ProoF. The equality is immediate from the preceding theorem. In fact, $\sigma _ { l } ( A ) = \sigma _ { a p } ( A )$ and $\sigma _ { r } ( A ) = \sigma _ { l } ( A ^ { * } ) ^ { * } = \sigma _ { a p } ( A ^ { * } ) ^ { * }$ . If $\lambda { \in } { \partial } \sigma ( A )$ then (VII.6.7) $\lambda   \in   \sigma _ { a p } ( A )$ .But $\bar { \lambda }   \in   \partial \sigma ( A ^ { * } )$ so that $\bar { \lambda }   \in   \sigma _ { a p } ( \dot { A ^ { * } } )$

For normal elements there is less variety. The pertinent result is proved here in a more general setting than that of operators.

1.3. Proposition. Let A be a C\*-algebra with identity. If a is a normal element of A, then the following statements are equivalent.

(a) a is invertible.

(b) a is left invertible.

(c) a is right invertible.

PRooF. Assume that a is left invertible, so there is a b in $\varkappa$ such that $b a = 1$ Thus for any x in $\mathcal { A } , \left\| x \right\| = \left\| \boldsymbol { b } \boldsymbol { a } x \right\| \leqslant \left\| \boldsymbol { b } \right\| \left\| \boldsymbol { a } x \right\|$ , and hence $\| a x \| \geqslant \| b \| ^ { - 1 } \| x \|$ In particular, this is true whenever $x   \in   C ^ { * } ( a )$ .Because a is normal, $C ^ { * } ( a )$ is isomorphic to $C ( K )$ where $K = \sigma ( a )$ and where the isomorphism takes a into the function $z \left( z ( w ) = w \right)$ . The inequality above thus becomes: $\| z f \| \geqslant \| b \| ^ { - 1 } \| f \|$ for every f in $C ( K ) ,$ It must be shown that $0 \notin K ( = \sigma ( a ) )$ . If $\mathbf { 0 } { \in } K$ , then for every integer n there is a function $f _ { n }$ in $C ( K )$ such that $0 \leqslant f_{n} \leqslant 1, f_{n}(0)=1$ and $f_{n}(z)=0  for z  in K$ and $| z | \geqslant n ^ { - \frac { 1 } { 1 } }$ . Since $0 { \in } K ,   \| f _ { n } \| = 1$ . But $\| z f _ { n } \| \leqslant 1 / n$ This contradicts the inequality and so $\mathbf { 0 } { \notin } \sigma ( a ) ;$ that is, a is invertible.

The argument above shows that (b) implies (a). If a is right invertible, then $a ^ { * }$ is left invertible. By the preceding argument $a ^ { * }$ is invertible, and hence so is a. ■

1.4. Proposition. If N is a normal operator, then $\sigma ( N ) = \sigma _ { r } ( N ) = \sigma _ { l } ( N )$ . If λ is an isolated point of $\sigma ( N )$ , then $\lambda   \in   \sigma _ { p } ( N )$

ProoF. The first part of the proposition is immediate from the preceding result. If λ is an isolated point of $\sigma ( N )$ and $N = \int z   d E ( z ) ,$ then $0 \neq E(\{\lambda\})\mathcal{H} = \ker(N - \lambda)$ (Exercise IX.2.1). ■

## EXERCISES

1. Let S be the unilateral shift of multiplicity 1 on $l ^ { 2 } ( \mathbb { N } )$ and find $\sigma _ { l } ( S )$ and $\sigma _ { r } ( S )$

2. The compression spectrum of $A ,   \sigma _ { c } ( A )$ , is defined by $\sigma_{c}(A)=\{\lambda\in\mathbb{C}:$ ran $( A - \lambda )$ is not dense in $\mathcal { H } \}$ . Show: (a) $\lambda   \in   \sigma _ { c } ( A )$ if and only if $\bar { \lambda }   \in   \sigma _ { p } ( A ^ { * } )$ (b) $\sigma _ { c } ( A ) \subseteq \sigma _ { r } ( A )$ but this inclusion may be proper. (c) $\sigma _ { c } ( A )$ is not necessarily closed. (d) $\sigma ( A ) = \sigma _ { a p } ( A ) \cup \sigma _ { c } ( A )$

3. If $A   \in   \mathcal { B } ( \mathcal { H } )$ and $f \in \mathrm{HCl}(A)$ then $f ( \sigma _ { p } ( A ) ) \in \sigma _ { p } ( f ( A ) )$ . If f is not constant on any component of its domain, then $f ( \sigma _ { p } ( A ) ) = \sigma _ { p } ( f ( A ) )$

4. If $A   \in   \mathcal { B } ( \mathcal { H } )$ and $f \in \mathrm{HCl}(A)$ , then $f(\sigma_{ap}(A)) = \sigma_{ap}(f(A))$

## §2. Fredholm Operators

We begin with a definition.

2.1. Definition. If $\mathcal { H }$ and $\mathcal { H } ^ { \prime }$ are Hilbert spaces and $A : \mathcal { H } \rightarrow \mathcal { H } ^ { \prime }$ is a bounded operator, then A is said to be left semi-Fredholm if there is a bounded operator B: $\mathcal { H } ^ { \prime } \rightarrow \mathcal { H }$ and a compact operator K on $\mathcal { H }$ such that $B A = 1 + K$ Analogously, A is right semi-Fredholm if there is a such a bounded operator B and a compact operator $K ^ { \prime }$ on $\mathcal { H }$ such that $AB = 1 + K'$ . A is a semi-Fredholm operator if it is either left or right semi-Fredholm and A is a Fredholm operator if it is both left and right semi-Fredholm.

Observe that A is left semi-Fredholm if and only if $A ^ { * }$ is right semi-Fredholm. Thus results about semi-Fredholm operators will usually only be phrased in terms of left semi-Fredholm operators and the reader will be allowed to make the appropriate statement for right semi-Fredholm operators.

Note that a left invertible operator is left semi-Fredholm. However it is easy to get left semi-Fredholm operators that are not left invertible.

2.2. Example. Let $\mathcal { H } = \mathcal { H } _ { 0 } \oplus \mathcal { H } _ { 1 } \oplus \cdots$ , where dim $\mathcal { H } _ { j }   =   \alpha$ for all $j   \geqslant   0 .$ , and let S be the unilateral shift of multiplicity α with respect to this decomposition. (So S maps $\mathcal { H } _ { j }$ isometrically onto $\mathcal { H } _ { j + 1 } . )$ Recall that $S ^ { * } S = 1$ so S is left invertible and hence left semi-Fredholm. Also $S S ^ { * } = 1 - P _ { 0 }$ , where $P _ { 0 }$ is the projection of $\mathcal { H }$ onto $\mathcal { H } _ { 0 }$ . So S is Fredholm if $\alpha < \infty$

In the next result, the equivalence of the first three conditions is referred to as Atkinson's Theorem. The rest of this theorem is from Wolf [1959], Schechter [1968], and Fillmore, Stampfli and Williams [1972]

2.3. Theorem. $If A: \mathcal{H} \rightarrow \mathcal{H}'$ is a bounded operator, the following statements are equivalent.

(a) A is left semi-Fredholm.

(b) ran A is closed and dim ker $A < \infty$

(c) There is a bounded operator B: $\mathcal { H } ^ { \prime } \rightarrow \mathcal { H }$ and a finite rank operator F on $\mathcal { H }$ such that $B A = 1 + F$

(d) There is no sequence $\{ h _ { n } \}$ of unit vectors in $\mathcal { H }$ such that $h _ { n }   \to   0$ weakly and lim $\| A \boldsymbol { h } _ { n } \| = 0 .$

(e) There is no orthonormal sequences $\{ e _ { n } \}$ in $\mathcal { H }$ such that lim $\| A e _ { n } \| = 0$

(f) There is $a   \delta   >   0$ such that $\left\{ h \in \mathcal { H } : \| A h \| \leqslant \delta \| h \| \right\}$ contains no infinite dimensional manifold.

(g) If the positive operator $\left( A ^ { * } A \right) ^ { 1 / 2 } = \int _ { 0 } ^ { \infty } t d E ( t )$ , then there is a $\delta   >   0$ such that $E [ 0 , \delta ] \mathcal { H }$ is finite dimensional.

(h) If $K   \in   \mathcal { B } _ { 0 } ( \mathcal { H } ) .$ , then dim ker $( A + K ) < \infty$

PRooF. (a) implies (b). According to (a) there is a bounded operator B such that $\pi(B)\pi(A)=1; \mathrm{that~is}, \pi(BA-1)=0$ Hence $B A = 1 + K$ for some compact operator K. But ker $A \subseteq \ker B A = \ker ( 1 + K )$ Since the eigenspace corresponding to nonzero eigenvalues of compact operators are finite dimensional, dim ker $A < \infty . \mathrm { A l s o } ,$ the Fredholm Alternative (VII.7.9) implies ran $BA = \mathrm{ran}(K + 1)$ is closed. Hence there is a constant $c   >   0$ such that for $h \perp \ker(BA)$ 1 $\| \boldsymbol{B} \boldsymbol{A} \boldsymbol{h} \| \geqslant c \| \boldsymbol{h} \|$ . Thus if $\boldsymbol{h} \in [\ker \boldsymbol{B} \boldsymbol{A}]^{\perp}, c \| \boldsymbol{h} \| \leqslant \| \boldsymbol{B} \| \| \boldsymbol{A} \boldsymbol{h} \|$ , or $\| A h \| \geqslant (c/\| B \|) \| h \|$ This implies that $A([\ker BA]^{\perp})$ is closed. But ran $A = A ( [ \ker B A ] ^ { \perp } ) + A ( \ker B A )$ . Since A(ker BA) is finite dimensional, ran A is closed.

(b) implies (c). First define $A_{1}:(\ker A)^{\perp}\to\operatorname{ran}A$ by $A_{1} = A \left| (\ker A)^{\perp} \right|$ and note that $A _ { 1 }$ is invertible by The Open Mapping Theorem. Let P be the projection of $\mathcal { H }$ onto ran A and define $B : \mathcal { H } ^ { \prime } \to \mathcal { H }$ by $B = { A _ { 1 } } ^ { - 1 } P$ . It is left to the reader to check that $B A = 1 - F .$ , where F is the orthogonal projection of $\mathcal { H }$ onto ker A. Since ker A is finite dimensional, this establishes (c).

(c) implies (a). This is clear.

(a) implies (d). Suppose $\{ h _ { n } \}$ is a sequence of unit vectors in $\mathcal { H }$ that converges weakly to 0 and let B: $\mathcal { H } ^ { \prime } \rightarrow \mathcal { H }$ and K be as in the definition of a left semi-Fredholm operator. Since $BA = 1 + K, \left| 1 - \left\| BA_n \right\| \right| = \left| \left\| h_n \right\| \right| -$ $\| B A h _ { n } \| \leqslant \| K h _ { n } \|$ and $\| K h _ { n } \|   \to   0$ since K is compact. Thus $\| \boldsymbol{B} \boldsymbol{A} \boldsymbol{h}_n \| \rightarrow 1$ and so it is impossible for $\{ A h _ { n } \}$ to converge to 0 in norm.

(d) implies (e). Orthonormal sequences converge weakly to 0.

(e) implies (f). If (f) is false, then for every positive integer n there is an infinite dimensional manifold $\mathcal { M } _ { n }$ such that $\| A h \| \leqslant (1/n) \| h \|$ for all h in $\mathcal { M } _ { n }$

Let $e _ { 1 }$ be a unit vector in $\mathcal { M } _ { 1 }$ . Suppose $e _ { 1 } , \ldots , e _ { n }$ are orthonormal vectors such that $e_{k} \in \mathcal{M}_{k}, 1 \leqslant k \leqslant n.$ Let E be the projection of $\mathcal { H }$ onto $\vee \left\{ e _ { 1 } , \ldots , e _ { n } \right\}$ If $\mathcal { M } _ { n + 1 } \cap [ e _ { 1 } , \ldots , e _ { n } ] ^ { \perp } = ( 0 )$ , then E is injective on $\mathcal { M } _ { n + 1 }$ . Since dim $\mathcal { M } _ { n + 1 } = \infty$ and dim ran $E < \infty$ , this is impossible. Thus there is a unit vector $e _ { n + 1 }$ in $\mathcal { M } _ { n + 1 }$ such that $e _ { n + 1 } \perp \{ e _ { 1 } , \ldots , e _ { n } \}$ . The orthonormal sequence $\{ e _ { n } \}$ shows that (e) does not hold.

(f) implies (g). Let $| A | = \int t d E ( t )$ and let $\delta > 0 .$ If $h { \in } E [ 0 , \delta ] { \mathcal { H } }$ , then

$$
\begin{align*}\| A h \|^2 &= \langle A^* A h, h \rangle \\&= \langle |A|^2 h, h \rangle \\&= \int_{0}^{\delta} t^2 d E_{h,h}(t) \leqslant \delta^2 E_{h,h}[0,\delta]^2 \\&= \delta^2 \| h \|^2.\end{align*}
$$

So $E [ 0 , \delta ] \mathcal { H } \subseteq \left\{ h : \| A h \| \leqslant \delta \| h \| \right\}$ . By (f) there is a $\delta   >   0$ such that $E [ 0 , \delta ) \mathcal { H }$ is finite dimensional.

(g) implies (c). Let $\mathcal { M } _ { \delta } = \{ E [ 0 , \delta ] \mathcal { H } \} ^ { \perp }$ . Now $| A |$ maps $\mathcal { M } _ { \pmb { \delta } }$ bijectively onto $\mathcal { M } _ { \pmb { \delta } } .$ In fact, the inverse of $| A | \colon \mathcal { M } _ { \delta } { \rightarrow } \mathcal { M } _ { \delta }$ is $\left( \int _ { \delta } ^ { \infty } t ^ { - 1 } d E ( t ) \right) | \mathcal { M } _ { \delta } .$ Let $A = U | A |$ be the polar decomposition of A. Since $\mathcal { M } _ { \delta } \subseteq \operatorname { r a n } | A | \subseteq$ initial U, U maps $\mathcal { M } _ { \pmb { \delta } }$ isometrically onto some closed subspace $\mathcal { L }$ of ran A. Let $V =$ the inverse of U on $\mathcal { L }$ and $V   =   0$ on $\mathcal { L } ^ { \perp }$ ; that is, $V | { \mathcal { L } } ^ { \perp }   =   0$ and $V | \mathcal { L } = ( U | \mathcal { M } _ { \delta } ) ^ { - 1 }$ . Hence V is a partial isometry. Let $B _ { 1 } = \int _ { \delta } ^ { \infty } t ^ { - 1 } d E ( t )$ and put $B = B _ { 1 } V$ . If $h \in \mathcal { M } _ { \delta } ,$ then $BAh = B_{1}VU|A|h = h.$ If $h \in \mathcal{M}_{\delta}^{\perp} = E[0,\delta]h, \quad |A|h \in \mathcal{M}_{\delta}^{\perp}$ and so $U | A | h \bot { \mathcal { L } } ;$ thus $B A h = 0 .$ Hence $B A = E ( \delta , \infty ) = 1 - E [ 0 , \delta ]$ , and $E [ 0 , \delta ]$ has finite rank.

(a) implies (h). Let $B : \mathcal { H } ^ { \prime } \to \mathcal { H }$ be a bounded operator such that $B A = 1 + L ,$ where L is a compact operator on $\mathcal { H }$ . If $K \colon { \mathcal { H } } \to { \mathcal { H } } ^ { \prime }$ is any compact operator, then $B(A + K) = 1 + (L + BK)$ and $L + B K$ is compact. By definition $A + K$ is left semi-Fredholm. Since we have already shown that (a) implies (b), dim ker $( A + K )   < \infty$

(h) implies (e). Suppose (e) does not hold. So there is an orthonormal sequence, $\{ e _ { n } \}$ usch that $\| A e _ { n } \| \to 0$ By passing to a subsequence if necessary, it may be assumed that $\textstyle \sum _ { n = 1 } ^ { \infty } \| A e _ { n } \| ^ { 2 } < \infty$ . Thus for any h in $\mathcal { H }$

$$
\begin{align*}\sum \left| \langle h, e_n \rangle \right| \left\| A e_n \right\| & \leqslant \left[ \sum \left| \langle h, e_n \rangle \right|^2 \right]^{1/2} \left[ \sum \left\| A e_n \right\|^2 \right]^{1/2} \\& \leqslant C \left\| h \right\|,\end{align*}
$$

where $C = [ \sum \| A e _ { n } \| ^ { 2 } ] ^ { 1 / 2 }$ . Thus $\begin{array} { r } { K h = \sum _ { n = 1 } ^ { \infty } \langle h , e _ { n } \rangle A e _ { n } } \end{array}$ defines a bounded operator. Moreover, if $K _ { n } h = \sum _ { j = 1 } ^ { n } \langle h , e _ { j } \rangle A e _ { j } ,$ it is easy to see that $\| K _ { n } - K \| \to 0 .$ Thus K is compact. But $( \boldsymbol{A} - \boldsymbol{K} ) \boldsymbol{e}_{n} = \boldsymbol{0}$ for every n, so dim ker $(A - K) = \infty$ ■

As mentioned previously, the result for right semi-Fredholm operators that is analogous to the preceding theorem is left for the reader to state. We will, however, make explicit part of this result for Fredholm operators.

2.4. Corollary. A bounded operator $A : { \mathcal { H } } \to { \mathcal { H } } ^ { \prime }$ is Fredholm if and only if ran A is closed and both ker A and ker $A ^ { * }$ are finite dimensional.

In the case of a bounded operator A from a Hilbert space $\mathcal { H }$ into itself, the concept of a semi-Fredholm operator can be rephrased in terms of the corresponding concept in the Calkin algebra, $\mathcal { B } / \mathcal { B } _ { 0 }$ . In fact, this will be the primary situation in which the ideas of Fredholm theory are applied. The next result is immediate from the definition.

2.5. Proposition. For a Hilbert space $\mathcal { H } ,$ let $\pi : { \mathcal { B } } \to { \mathcal { B } } / { \mathcal { B } } _ { 0 }$ be the natural map and let $A \in \mathcal { B } = \mathcal { B } ( \mathcal { H } )$ The operator A is left (respectively, right) semi-Fredholm $i f$ and only ${ \it i f } \; \pi ( A )$ is left (respectively, $r i g h t )$ invertible in the Calkin algebra.

For notation, let $\mathcal { F } _ { \ell } = \mathcal { F } _ { \ell } ( \mathcal { H } )$ and $\mathcal { F } _ { r } = \mathcal { F } _ { r } ( \mathcal { H } )$ be the set of left and right semi-Fredholm operators on the Hilbert space $\mathcal { H }$ So $\mathcal { F } = \mathcal { F } _ { \ell } \cap \mathcal { F }$ , and $\mathcal { S } \mathcal { F } = \mathcal { F } _ { \ell } \cup \mathcal { F }$ , are the sets of Fredholm and semi-Fredholm operators on $\mathcal { H }$ . Since $\mathcal { F } _ { \ell } =$ the inverse image under $\pi$ of the left invertible elements of the Banach algebra $\mathcal { B } / \mathcal { B } _ { 0 }$ , the next proposition is immediate.

## 2.6. Proposition. Each of the sets $\mathcal { F } _ { \ell } , \mathcal { F } _ { r } , \mathcal { F }$ , and $\mathcal { I F }$ are open subjects of $\mathcal { B }$

## EXERCISES

1. If $A   \in   \mathcal { B } ( \mathcal { H } )$ and ran A is closed, prove than ran $A ^ { * }$ is closed without using Theorem VI.1.10. [Hint: Show that there is a bounded operator B on $\mathcal { H }$ such that $B A =$ the projection of $\mathcal { H }$ onto (ker $A ) ^ { 1 }$ ]

2. Give a direct proof that (b) implies (a) in Theorem 2.3.

3. Let A, $B , C \in \mathcal { B } ( \mathcal { H } )$ and define $X : { \mathcal { H } } ^ { ( 2 ) } \to { \mathcal { H } } ^ { ( 2 ) }$ by the matrix $X = { \left[ \begin{matrix} { A } & { B } \\ { 0 } & { C } \end{matrix} \right] } .$ (a) Show that if $A { \in } { \mathcal { F } }$ , then $X   \in   \mathcal { F }$ if and only if $C \in \mathcal { F }$ . (b) If $A   \in   \mathcal { F }$ , show that $X   \in   { \mathcal { S P } }$ if and only if $C \in \mathcal { S F }$ . (c) Suppose $A , C \in { \mathcal { P F } }$ with dim ker $A = \infty$ and dim $\ker C ^ { * } = \infty$ . Show that $X \notin { \mathcal { S F } }$

4. If $A   \in   \mathcal { B } ( \mathcal { H } )$ show that $A \mathcal { M }$ is closed for every closed subspace $\mathcal { M }$ of $\mathcal { H }$ if and only if A has finite rank or A is left Fredholm.

5. If X and $\pmb { g }$ are Banach spaces and $T \in \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ such that the Hamel basis dimension (that is, the algebraic dimension) of $\mathcal { G } / ( \mathrm { r a n } \; T )$ is finite, then ran $T$ is closed.

6. Show that a normal operator is Fredholm if and only if 0 is not a limit point of $\sigma ( N )$ and dim ker $N < \infty$ . (See Proposition 4.5 below.)

## §3. The Fredholm Index

I wish to acknowledge that the basis of this section is a development of the Fredholm index which I learned from my colleague Hari Bercovici.

If A is a semi-Fredholm operator, define the (Fredholm) index of A, ind A, by

## 3.1

$$
\begin{aligned}\operatorname{ind} A &= \operatorname{dim} \ker A - \operatorname{dim}(\operatorname{ran} A)^{\perp} \\&= \operatorname{dim} \ker A - \operatorname{dim} \ker A^{*}.\end{aligned}
$$

Note that ind $A { \in } { \mathbb { Z } } \cup \{ \pm \infty \}$ and it is necessary for either ker A or ker $A ^ { * }$ to be finite dimensional in order for (3.1) to make sense. For ind A to be well defined, it is not necessary that ran A be closed (the other part of the definition of semi-Fredholm operators), but this property will be used in a critical way when the properties of the index are established.

See Dieudonné [1985] for some historical notes on the Fredholm index.

The main properties of the Fredholm index are contained in Theorems 3.7, 3.11, and 3.12 below. But we will begin with some elementary results.

3.2. Proposition. If A: $\mathcal { H } \rightarrow \mathcal { H } ^ { \prime }$ and $\mathcal { H }$ and $\mathcal { H }$ are finite dimensional, then A is Fredholm and ind $A = \dim \mathcal{H} - \dim \mathcal{H}'$

ProoF. Clearly A is Fredholm. From linear algebra we know that dim $\mathcal{H} = \dim \left( \mathrm{ran}  A \right) + \dim \left( \ker  A \right) = \left[ \dim \mathcal{H}' - \dim \left( \mathrm{ran}  A \right)^\perp \right] + \dim \left( \ker  A \right)$ Thus ind $A = \dim \left( \ker A \right) - \dim \left( \operatorname{ran} A \right)^{\perp} = \dim \mathcal{H} - \dim \mathcal{H}^{\prime}$ ■

The next result is actually just a restatement of the Fredholm Alternative (VII. 7.9).

3.3. Proposition. If $K \colon { \mathcal { H } } \to { \mathcal { H } }$ is a compact operator and $\lambda \neq 0 .$ , then $\lambda + K$ is Fredholm and ind $( \lambda + K ) = 0$

We already observed that the adjoint of a semi-Fredholm operator is also a semi-Fredholm operator. This same reasoning produces the calculation of the index.

3.4. Proposition. (a) If A is a semi-Fredholm operator, then $A ^ { * }$ is also semi-Fredholm and ind $A ^ { * } = - \operatorname { i n d } A .$

(b) If N is a normal operator on a Hilbert space $\mathcal { H } ,$ , then N is semi-Fredholm if and only if N is Fredholm, in which case ind $N = 0$

(c) If A and B are Fredholm operators, then A⊕B is Fredholm and ind $(A \oplus B) = \mathrm{ind} A + \mathrm{ind} B.$

ProoF. As stated, the proof of (a) is easy. For part (b), recall that for a normal operator $N ,   \|   N h   \| = \|   N ^ { * } h   \|$ for every vector h in . Thus ker $N = \ker N ^ { * }$ The result is now immediate. The proof of (c) is left to the reader.

Also see Exercise 2.6 and Proposition 4.5 below.

The next theorem is one of the main properties of the Fredholm index. But first two lemmas are required.