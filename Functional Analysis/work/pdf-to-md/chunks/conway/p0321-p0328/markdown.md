1.9. Example. Let $e _ { 0 } , e _ { 1 } , \ldots$ . be an orthonormal basis for $\mathcal { H }$ and let $\alpha _ { 0 } , \alpha _ { 1 } , \ldots$ be complex numbers. Define $\mathcal { D } = \left\{ h \in \mathcal { H } : \sum _ { 0 } ^ { \infty } | \alpha _ { n } \langle h , e _ { n } \rangle | ^ { 2 } < \infty \right\}$ and let $\begin{array} { r } { A h = \sum _ { 0 } ^ { \infty } \alpha _ { n } \langle h , e _ { n } \rangle e _ { n } } \end{array}$ for h in D. Then $A \in \mathcal { C } ( \mathcal { H } )$ with dom $A = \mathcal { D }$ . Also, dom $A ^ { * } = \mathcal { D }$ and $\begin{array} { r } { A ^ { * } h = \sum _ { 0 } ^ { \infty } \bar { \alpha } _ { n } \langle h , e _ { n } \rangle e _ { n } } \end{array}$ for all h in $\mathcal { D }$

1.10. Example. Let $( X , \Omega , \mu )$ be a σ-finite measure space and let $\phi \colon X   \to   \mathbb { C }$ be an Ω-measurable function. Let $\mathcal { D } = \{ f { \in } L ^ { 2 } ( \mu ) ; \phi f { \in } L ^ { 2 } ( \mu ) \}$ and define $A f = \phi f$ for all f in $\mathcal { D }$ Then $A   \in   \mathcal { C } ( L ^ { 2 } ( \mu ) )$ , dom $A ^ { * } = \mathcal { D }$ , and $A ^ { * } { \dot { f } } = { \bar { \phi } } f$ for f in D.

1.11. Example. Let $\mathcal { D } = \mathfrak { a } \mathbb { I }$ functions $f \colon [ 0 , 1 ]   \to   \mathbb { C }$ that are absolutely continuous with $f ^ { \prime } { \in } L ^ { 2 } ( 0 , 1 )$ and such that $f(0)=f(1)=0.\ \mathcal{D}$ includes all polynomials p with $p ( 0 ) = p ( 1 ) = 0 .$ So the uniform closure of $\mathcal { D }$ is $\{ f { \in } C [ 0 , 1 ] : f ( 0 ) = f ( 1 ) = 0 \}$ . Thus  is dense in $L ^ { 2 } ( 0 , 1 )$ . Define $A \colon L ^ { 2 } ( 0 , 1 ) \to$ $L ^ { 2 } ( 0 , 1 )$ by $A f   =   i f ^ { \prime }$ for f in D. To see that A is closed, suppose $\{ f _ { n } \} \leq \emptyset$ and $f _ { n } \oplus i f _ { n } ^ { \prime } \to f \oplus g$ in ${ \dot { L ^ { 2 } } } \oplus L ^ { 2 } .$ Let $h(x) = - i \int_{0}^{x} g(t)   dt;$ so h is absolutely continuous. Now using the Cauchy-Schwarz inequality we get that $\left| f _ { n } ( x ) - h ( x ) \right| = \left| \int _ { 0 } ^ { x } \left[ f _ { n } ^ { \prime } ( t ) + i g ( t ) \right] d t \right| \leqslant \left\| f _ { n } ^ { \prime } + i g \right\| _ { 2 } = \left\| i f _ { n } ^ { \prime } - g \right\| _ { 2 }$ . Thus $f _ { n } ( x )   \rightarrow$ $h ( x )$ uniformly on $[ 0 , 1 ]$ Since $f _ { n }   \rightarrow   f$ in $L ^ { 2 } ( 0 , 1 ) , f ( x ) = h ( x ) \mathrm { a . e . }$ So we may assume that $f(x) = - i \int_{0}^{x} g(t)   dt$ for all x. Therefore f is absolutely continuous and $f _ { n } ( x )   \to   f ( x )$ uniformly on $[ 0 , 1 ] ;$ thus $f(0)=f(1)=0$ and $f ^ { \prime } = - i g \in$ $L ^ { 2 } ( 0 , 1 )$ . So $f \in \mathcal { D }$ and $f \oplus g = f \oplus g = f \oplus if' \in \mathrm{grad} A;$ that is, $A   \in   \mathcal { C } ( L ^ { 2 } ( 0 , 1 ) )$ Note that $\{ f ^ { \prime } : f \in \mathcal { D } \} = \{ h \in L ^ { 2 } ( 0 , 1 ) : \int _ { 0 } ^ { 1 } h ( x ) d x = 0 \} = [ 1 ] ^ { \perp } .$

Claim. dom $A ^ { * } = \{ g \colon g$ is absolutely continuous on $[ 0 , 1 ] ,   g ^ { \prime }   \in   L ^ { 2 } ( 0 , 1 ) \}$ and for g in dom $A ^ { * } , \; A ^ { * } g = i g ^ { \prime }$

In fact, suppose gedom $A ^ { * }$ and let $h = A ^ { * } g$ Put $H(x) = \int_{0}^{x} h(t)   dt$ Using integration by parts, for every f in D, $i \int_{0}^{1} f^{\prime} \bar{g} = \langle A f, g \rangle = \langle \bar{f}, h \rangle = \int_{0}^{1} f \bar{h} =$ $\int_{0}^{1} f(x)   d\bar{H}(x) = - \int_{0}^{1} f'(x) \bar{H}(x)   dx;$ that is, $\langle f ^ { \prime } , - i g \rangle = \langle f ^ { \prime } , - H \rangle$ for all f in D. Thus $H - i g \in \{ \tilde { f } ^ { \prime } : f \in \mathcal { D } \} ^ { \perp } = [ 1 ] ^ { \perp \perp }$ ; hence $H - i g = c ,$ a constant function. Thus $g = i c - i H$ so that g is absolutely continuous and $g ^ { \prime } = - i h \in L ^ { 2 }$ . Also note that $A ^ { * } g = h = i g ^ { \prime }$ . The proof of the other inclusion is left to the reader.

1.12. Example. Let $\mathcal { E } = \{ f \in L ^ { 2 } ( 0 , 1 ) :$ f is absolutely continuous, $f ^ { \prime } { \in } L ^ { 2 }$ , and $f(0) = f(1)$ . Define $B f = i f ^ { \prime }$ for f in E. As in (1.11), $B   \in   \mathcal { C } ( L ^ { 2 } ( 0 , 1 ) )$ and ran $B = [ 1 ] ^ { \perp }$

Claim. dom $B ^ { * } = 6$ and $B ^ { * } g = i g ^ { \prime }$ for g in $\ell .$

Let gedom $B ^ { * }$ . Put $h = B ^ { * } g$ and $H(x) = \int_{0}^{x} h(t)   dt.$ As in (1.11), $H ( 0 ) = H ( 1 ) = 0$ and for every f in , $i \int_{0}^{1} f^{\prime} \bar{g} = - \int_{0}^{1} f^{\prime} \bar{H}.$ Hence $0 =$ $\int _ { 0 } ^ { 1 } ( i f ^ { \prime } \overline { { { g } } } + f ^ { \prime } \overline { { { H } } } ) = \int _ { 0 } ^ { 1 } i f ^ { \prime } ( \overline { { { g + i H } } } )$ . Thus $g + i H \perp \operatorname { r a n } B$ and so $g + i H = c ,$ a constant function. Thus $g = c - i H$ is absolutely continuous, $g ^ { \prime } = - i h \in L ^ { 2 } .$ and $g ( 0 ) = g ( 1 ) = c$ Thus $g \in \theta$ and $B ^ { * } g = h = i g ^ { \prime }$ . The proof of the other inclusion is left to the reader.

The preceding two examples illustrate the fact that the calculation of the adjoint depends on the domain of the operator, not just the formal definition of the operator. Note the fact that the next result generalizes (II.2.19).

## 1.13. Proposition. $I f A : { \mathcal { H } } \to { \mathcal { H } }$ is densely defined, then

$$
( \operatorname { r a n } A ) ^ { \perp } = \ker A ^ { * } .
$$

If A is also closed, then

$$
( \operatorname{rank} A^{*} )^{\perp} = \operatorname{ker} A.
$$

ProoF. If h ⊥ ran A, then for every f in dom $A,0 = \langle A f, h \rangle$ . Hence hedom $A ^ { * }$ and $A^{*}h = 0$ . The other inclusion is clear. By Corollary 1.8, if $A \in \mathcal { C } ( \mathcal { H } , \mathcal { H } ) ,$ $A ^ { * * } = A$ .So the second equality follows from the first. ■

1.14. Definition. If $A : \mathcal { H } \rightarrow \mathcal { H }$ is a linear operator, A is boundedly invertible if there is a bounded linear operator $B : \mathcal { H } \to \mathcal { H }$ such that $A B = 1$ and $B A \subseteq 1$

Note that if $B A \subseteq 1$ , then $B A$ is bounded on its domain. Call B a (bounded) inverse of A.

1.15. Proposition. Let A: $\mathcal { H } \rightarrow \mathcal { H }$ be a linear operator.

(a) A is boundedly invertible if and only if ker $A   =   ( 0 )$ , ran $A = \mathcal { H }$ , and the graph of A is closed.

(b) If A is boundedly invertible, its inverse is unique and denoted by $A ^ { - 1 }$

PRooF. (a) Let B be a bounded inverse of A. So dom $B = \mathcal { H }$ . Since $B A \subseteq 1$ ker $A = ( 0 ) ;$ since $A B = 1$ , ran $A = \mathcal { H }$ . Also, gra $A = \{ h \oplus A h \}$ hedom $A \} =$ $\{ B k \oplus k \colon k { \in } { \mathcal { H } } \}$ . Since B is bounded, gra A is closed. Conversely, if A has the stated properties, $B k = A ^ { - 1 } k$ for k in $\mathcal { H }$ is a well-defined operator on $\mathcal { H }$ Because gra A is closed, gra B is closed. By the Closed Graph Theorem, $B \in \mathcal{B}(\mathcal{H}, \mathcal{H})$

(b) This is an exercise.

1.16. Definition. If $A : \mathcal { H } \rightarrow \mathcal { H }$ is a linear operator, $\rho ( A ) ,$ the resolvent set for A, is defined by $\rho ( A ) = \{ \lambda \in \pmb { \mathbb { C } } : \lambda - A$ is boundedly invertible}. The spectrum of A is the set $\sigma(A)=\mathbf{C}\backslash\rho(A);$

It is easy to see that if A: $\mathcal { H } \rightarrow \mathcal { H }$ is a linear operator and $\lambda \in \mathbf { C } ,$ gra A is closed if and only if gra $( A - \lambda )$ is closed. So if A does not have closed graph, $\sigma(A) = \mathbf{C}$ . Even if A has closed graph, it is possible that $\sigma ( A )$ is empty (see Exercise 10). The spectrum of an unbounded operator, however, does enjoy some of the properties possessed by the spectrum of an element of a Banach algebra. The proof of the next result is left to the reader.

1.17. Proposition. If A: $\mathcal { H } \rightarrow \mathcal { H }$ is a linear operator, then $\sigma ( A )$ is closed and $z { \mapsto } ( z - A ) ^ { - 1 }$ is an analytic function on $\rho ( A )$

Note that if A is defined as in Example 1.9, then $\sigma ( A ) = \mathrm { c l } \left\{ \alpha _ { n } \right\}$ . Hence it is possible for $\sigma ( A )$ to equal any closed subset of C.

## 1.18. Proposition. Let $A \in \mathcal { C } ( \mathcal { H } )$

(a) $\lambda \in \rho ( A )$ if and only if ker $(A - \lambda) = (0)$ and $\mathrm{rank}(A - \lambda) = \mathcal{H}.$

(b) $\sigma ( A ^ { * } ) = \{ \bar { \lambda } : \lambda \in \sigma ( A ) \}$ and for λ in $\rho ( A ) , ( A - \lambda ) ^ { * } = [ ( A - \lambda ) ^ { - 1 } ] ^ { * } .$

PROOF. Exercise.

## EXERCISES

1. If A, B, and AB are densely defined linear operators, show that $( A B ) ^ { * } \supseteq B ^ { * } A ^ { * }$

2. Verify the statements in Example 1.9

3. Verify the statements in Example 1.10.

4. Define an unbounded weighted shift and determine its adjoint.

5. Verify the statements in Example 1.11.

6. If $\mathcal { H }$ is infinite dimensional, show that there is a linear operator A: $\mathcal { H } \rightarrow \mathcal { H }$ such that gra A is dense in $\mathcal { H } \oplus \mathcal { H }$ . What does this say about dom $A ^ { * } ?$ (See Lindsay [1984].)

7. Let  be the set of absolutely continuous functions f such that $f ^ { \prime } { \in } L ^ { 2 } ( 0 , 1 )$ . Let $D f = f ^ { \prime }$ for f in D and let $(Af)(x) = xf(x)$ for f in $L ^ { 2 } ( 0 , 1 )$ .Show that $DA - AD \subseteq 1$

8. If $\varkappa$ is a Banach algebra with identity, show that there are no elements $a , b$ $\varkappa$ such that $ab - ba = 1$ . (Hint: compute $a^{n}b - ba^{n}.$

9. Prove Proposition 1.18.

10. Define A: $L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ by $(Af)(x) = \exp(-x^2)f(x-1)$ for all f in $L ^ { 2 } ( \mathbb { R } )$ (a) Show that $A   \in   \mathcal { B } ( L ^ { 2 } ( \mathbb { R } ) )$ . (b) Find $\| A ^ { n } \|$ and show that $r(A)=0$ so that $\sigma ( A ) = \{ 0 \}$ . (c) Show that A is injective. (d) Find $A ^ { * }$ and show that ran A is dense. (e) Define $B = A ^ { - 1 }$ with dom $B = \tan A$ and show that $B   \in   \mathcal { C } ( L ^ { 2 } ( \mathbb { R } ) )$ with $\sigma ( B ) = \square$

11. If $A \in \mathcal { C } ( \mathcal { H } ) ,$ show that $A^{*}A\in\mathcal{C}(\mathcal{H})$ . Show that $-1 \notin \sigma(A^{*}A)$ and that if $B = \left( 1 + A^{*} A \right)^{-1}, \quad \| B \| \leqslant 1$

12. If B is the bounded operator obtained in Exercise 11, show that $C = A B$ is also bounded and $\| C \| \leqslant 1$

13. If A is a self-adjoint operator, then $\lambda \in \rho ( A )$ if and only if $A - \lambda$ is surjective.

## §2. Symmetric and Self-Adjoint Operators

An appropriate introduction to this section consists in a careful examination of Examples 1.11 and 1.12 in the preceding section. In (1.11) we saw that the operator A seemed to be inclined to be self-adjoint, but dom $A ^ { * }$ was different from dom A so we could not truly say that $A = A ^ { * }$ . In (1.12), $B = B ^ { * }$ in any sense of the concept of equality. This points out the distinction between symmetric and self-adjoint operators that it is necessary to make in the theory of unbounded operators.

2.1. Definition. An operator A: $\mathcal { H } \rightarrow \mathcal { H }$ is symmetric if A is densely defined and $\langle A f , g \rangle = \langle f , A g \rangle$ for all $f , g$ in dom A.

The proof of the next proposition is left to the reader.

2.2. Proposition. If A is densely defined, the following statements are equivalent.

(a) A is symmetric.

(b) $\langle A f , f \rangle   \in   \mathbb { R }$ for all f in dom A.

(c) ${ \overline { { A } } } \subseteq A ^ { * } .$

If A is symmetric, then the fact that $A \subseteq A ^ { * }$ implies dom $A ^ { * }$ is dense. Hence A is closable by Proposition 1.6. Symmetric operators can behave cantankerously. For example, there is an example of a closed symmetric operator T such that dom $( T ^ { 2 } ) = ( 0 )$ . See Chernoff [1983].

It is easy to check that the operators in Examples 1.11 and 1.12 are symmetric.

2.3. Definition. A densely defined operator A: $\mathcal { H } \rightarrow \mathcal { H }$ is self-adjoint if $A = A ^ { * }$

Let us emphasize that the condition that $A = A ^ { * }$ in the preceding definition carries with it the requirement that dom $A = \mathrm{dom} A^{*}$ . Now clearly every self-adjoint operator is symmetric, but the operator A in Example 1.11 shows that there are symmetric operators that are not self-adjoint. If, however, an operator is bounded, then it is self-adjoint if and only if it is symmetric. The operator B in Example 1.12 is an unbounded self-adjoint operator and Examples 1.9 and 1.10 can be used to furnish additional examples of unbounded self-adjoint operators.

Note that Proposition 1.6 implies that a self-adjoint operator is necessarily closed.

2.4. Proposition. Suppose A is a symmetric operator on $\mathcal { H }$

(a) If ran A is dense, then A is injective.

(b) $If A = A^*$ and A is injective, then ran A is dense and $A ^ { - 1 }$ is self-adjoint.

(c) If dom $A = \mathcal { H }$ then $A = A ^ { * }$ and A is bounded.

(d) If ran $A = \mathcal { H }$ , then $A = A ^ { * }$ and $A^{-1} \in \mathcal{B}(\mathcal{H})$

PRooF. The proof of (a) is trivial and (b) is an easy consequence of (1.13) and some manipulation.

(c) We have $A \subseteq A ^ { * }$ . If dom $A = \mathcal { H }$ , then $A = A ^ { * }$ and so A is closed. By the Closed Graph Theorem $A \in \mathcal { B } ( \mathcal { H } )$

(d) If ran $A = \mathcal { H }$ , then A is injective by (a). Let $B = A ^ { - 1 }$ with dom $B =$ ran $A = \mathcal { H }$ . If $f = A g$ and $h = A k$ , with g, k in dom A, then $\langle B f , h \rangle = \langle g , A k \rangle =$ $\langle A g , k \rangle = \langle f , k \rangle = \langle f , B h \rangle$ . Hence B is symmetric. By (c), $B = B ^ { * } \in { \mathcal { B } } ( { \mathcal { H } } )$ By (b), $A = B ^ { - 1 }$ is self-adjoint. ■

We now will turn our attention to the spectral properties of symmetric and self-adjoint operators. In particular, it will be seen that symmetric operators can have nonreal numbers in their spectra, though the nature of the spectrum can be completely diagnosed (2.8). Self-adjoint operators, however, must have real spectra. The next result begins this spectral discussion.

2.5. Proposition. Let A be a symmetric operator and let $\lambda = \alpha + i \beta ,$ α and $\beta$ real numbers.

(a) For each f in dom $A , \left\| ( A - \lambda ) f \right\| ^ { 2 } = \left\| ( A - \alpha ) f \right\| ^ { 2 } + \beta ^ { 2 } \left\| f \right\| ^ { 2 } .$

(b) If $\beta \neq 0 ,$ ker $(A - \lambda) = (0).$

(c) If A is closed and $\beta \neq 0 ,$ , ran $( A - \lambda )$ is closed.

PROOF. Note that

$$
\begin{align*}\| (A - \lambda) f \|^2 &= \| (A - \alpha) f - i \beta f \|^2 \\&= \| (A - \alpha) f \|^2 + 2 \operatorname{Re} i \langle (A - \alpha) f, \beta f \rangle + \beta^2 \| f \|^2.\end{align*}
$$

But

$$
\langle ( A - \alpha ) f , \beta f \rangle = \beta \langle A f , f \rangle - \alpha \beta \| f \| ^ { 2 } \in \mathbb { R } ,
$$

so (a) follows. Part (b) is immediate from (a). To prove (c), note that $\| ( A - \lambda ) f \| ^ { 2 } \geqslant \beta ^ { 2 } \| f \| ^ { 2 }$ . Let $\{ f _ { n } \} \subseteq \operatorname { d o m } A$ such that $(A - \lambda)f_n \to g.$ The preceding inequality implies that $\{ f _ { n } \}$ is a Cauchy sequence in $\mathcal { H } ;$ let $f = \lim_{n \to \infty} f_n$ But $f_{n} \oplus (A - \lambda) f_{n} \in \mathrm{grad} (A - \lambda)$ and $f _ { n } \oplus ( A - \lambda ) f _ { n } \to f \oplus g$ Hence $f \oplus g \in \operatorname{grad}(A - \lambda)$ and so $g = (A - \lambda)f \in \mathrm{ran}(A - \lambda)$ . This proves (c).

2.6. Lemma. If M, N are closed subspaces of H and $\mathcal { M } \cap \mathcal { N } ^ { \perp } = ( 0 ) .$ , then dim $\mathcal { M } \leqslant \dim \mathcal { N }$

ProOF. Let P be the orthogonal projection of $\mathcal { H }$ onto $\mathcal { N }$ and define $T \colon { \mathcal { M } } \to { \mathcal { N } }$ by $T f = P f$ for f in M. Since $\mathcal { M } \cap \mathcal { N } ^ { \perp }   =   ( 0 )$ , T is injective. If $\mathcal { L }$ is a finite dimensional subspace of M, dim $\mathcal { L } = \dim T \mathcal { L } \leqslant \dim \mathcal { N }$ Since $\mathcal { L }$ was arbitrary, dim $\mathcal { M } \leqslant \dim \mathcal { N }$

2.7. Theorem. If A is a closed symmetric operator, then dim ker $( A ^ { * } - \lambda )$ is constant for Im $\lambda   >   0$ and constant for Im $\lambda   <   0 .$

PROOF. Let $\lambda = \alpha + i \beta ,$ α and $\beta$ real numbers and $\beta \neq 0 .$

Claim. $\left| \lambda - \mu \right| < \left| \beta \right|, \ker(A^* - \mu) \cap \left[ \ker(A^* - \lambda) \right]^\perp = (0).$

Suppose this is not so. Then there is an f in ker $( A ^ { * } - \mu ) \cap [ \ker ( A ^ { * } - \lambda ) ] ^ { \perp }$ with $\| f \| = 1$ . By (2.5c), ran(A − λ) is closed. Hence $f \in [ \ker ( A ^ { * } - \lambda ) ] ^ { \perp } =$ $\operatorname { \mathbf { r a n } } ( A - { \overline { { \lambda } } } )$ . Let $g \in \mathbf { d o m } A$ such that $f = ( A - \overline { { \lambda } } ) g$ Since $f { \in } \ker ( A ^ { * } - \mu )$

$$
\begin{align*}0 &= \langle (A^* - \mu)f, g \rangle = \langle f, (A - \bar{\mu})g \rangle \\&= \langle f, (A - \bar{\lambda} + \bar{\lambda} - \bar{\mu})g \rangle \\&= \|f\|^2 + (\lambda - \mu)\langle f, g \rangle.\end{align*}
$$

Hence $1 = \| f \| ^ { 2 } = | \lambda - \mu | | \langle f , g \rangle | \leqslant | \lambda - \mu | \| g \|$ . But (2.5a) implies that $1 = \| f \| = \| ( A - \bar { \lambda } ) g \| \geqslant | \beta |   \| g \| ;$ SO $\| g \| \leqslant | \beta | ^ { - 1 }$ . Hence $1 \leqslant \left| \lambda - \mu \right| \left\| g \right\| \leqslant$ $| \lambda - \mu | | \beta | ^ { - 1 } < 1 \text { if } | \lambda - \mu | < | \beta |$ . This contradiction establishes the claim.

Combining the claim with Lemma 2.6 gives that dim ker $( A ^ { * } - \mu ) \leqslant$ dim ker $( A ^ { * } - \lambda )$ if $| \lambda - \mu | < | \beta | = | \mathrm{Im} \lambda |$ Note that if $| \lambda - \mu | < \frac { 1 } { 2 } | \beta |$ , then $| \lambda - \mu | < | \operatorname { I m } \mu | ,$ , so that the other inequality also holds. This shows that the function λ→dim ker $( A ^ { * } - \lambda )$ is locally constant on $\mathbf { C } \backslash \mathbb { R }$ . A simple topological argument demonstrates the theorem. ■

2.8. Theorem. If A is a closed symmetric operator, then one and only one of the following possibilities occurs:

(a) $\sigma ( A ) = \mathbb { C } ;$

(b) $\sigma ( A ) = \{ \lambda \in \mathbb { C } : \mathrm { I m } \lambda \geqslant 0 \} ;$

$$
\sigma ( A ) = \{ \lambda \in \mathbb { C } : \mathrm { I m } \lambda \leqslant 0 \} ;
$$

(d) $\sigma ( A ) \subseteq \mathbb { R } .$

PROOF. Let $H _ { \pm } = \left\{ \lambda { \in } \pm \mathbf { \mathbb { C } } { : } \pm \operatorname { I m } \lambda > 0 \right\}$ . By (2.5) for λ in $H _ { \pm } , A - \lambda$ is injective and has closed range. So if $A - \lambda$ is surjective, $\lambda \in \rho ( A )$ . But [ran $( A - \lambda ) ] ^ { \perp } =$ $\ker ( A ^ { * } - { \overline { { \lambda } } } )$ . So the preceding theorem implies that either $H _ { \pm } \subset \sigma ( A )$ or $H _ { \pm } \cap \sigma ( A ) = \square$ . Since $\sigma ( A )$ is closed, if $H _ { \pm } \subseteq \sigma ( A )$ , then either $\sigma ( A ) = \mathbf { C }$ or $\sigma ( A ) = \mathrm { c l } H _ { \pm } . \mathrm { I f } H _ { \pm } \cap \sigma ( A ) = \square , \sigma ( A ) \subseteq \mathbb { R }$

2.9. Corollary. If A is a closed symmetric operator, the following statements are equivalent.

(a) A is self-adjoint.

(b) $\sigma ( A ) \subseteq \mathbb { R } .$

(c) $\ker ( A ^ { * } - i ) = \ker ( A ^ { * } + i ) = 0 .$

PRooF. If A is symmetric, every eigenvalue of A is real (Exercise 1). So if $A = A ^ { * }$ and Im $\lambda \ne 0,\ker(A^* - \lambda) = \ker(A - \lambda) = 0$ Thus $A - \lambda$ is injective and has dense range. By (2.5), A – λ has closed range and so $A - \lambda$ has a bounded inverse (1.15) whenever Im $\lambda \neq 0 .$ That is, $\sigma ( A ) \subseteq \mathbb { R }$ and so (a) implies (b).

If $\sigma ( A ) \subseteq \mathbb { R }$ , ker $(A^{*} \pm i) = [\mathrm{ran}(A \mp i)]^{\perp} = \mathcal{H}^{\perp} = (0)$ .Hence (b) implies (c).

If (c) holds, then this, combined with (2.5c) and (1.13), implies $A + i$ is surjective. Let hedom $A ^ { * } ,$ Then there is an f in dom A such tha $\mathsf { t } ( A + i ) f =$ $( A ^ { * } + i ) h$ . But $A ^ { * } + i \supseteq A + i ,$ SO $( A ^ { * } + i ) f = ( A ^ { * } + i ) h .$ But $A ^ { * } + i$ is injective, so $h = f \in \mathrm{dom} A$ . Thus $A = A ^ { * }$ ■

2.10. Corollary. $I f A$ is a closed symmetric operator and $\sigma ( A )$ does not contain R, then $A = A ^ { * }$

It may have occurred to the reader that a symmetric operator A fails to be self-adjoint because its domain is too small and that this can be rectified by merely increasing the size of the domain. Indeed, if A is the symmetric operator in Example 1.11, then the operator B of Example 1.12 is a self-adjoint extension of A. However, the general situation is not always so cooperative.

Fix a symmetric operator A and suppose B is a symmetric extension of $A { \mathrel { \mathop : } } A \subseteq B .$ It is easy to verify that $B ^ { * } \subseteq A ^ { * }$ . Since $B \subseteq B ^ { * }$ , we get $A \subseteq B \subseteq B ^ { * } \subseteq A ^ { * }$ . Thus every symmetric extension of A is a restriction of $A ^ { * }$

2.11. Proposition. (a) A symmetric operator has a maximal symmetric extension. (b) Maximal symmetric extensions are closed. (c) A self-adjoint operator is a maximal symmetric operator.

PRooF. Part (a) is an easy application of Zorn's Lemma. If A is symmetric, $A \subseteq A ^ { * }$ and so A is closable. The closure of a symmetric operator is symmetric (Exercise 3), so part (b) is immediate. Part (c) is a consequence of the comments preceding this proposition.

2.12. Definition. Let A be a closed symmetric operator. The deficiency subspaces of A are the spaces

$$
\begin{aligned}\mathcal{L}_{+} &= \ker(A^{*} - i) = [\operatorname{ran}(A + i)]^{\perp}, \\\mathcal{L}_{-} &= \ker(A^{*} + i) = [\operatorname{ran}(A - i)]^{\perp}.\end{aligned}
$$

The deficiency indices of A are the numbers $n _ { \pm } = \dim { \mathcal { L } } _ { \pm }$

It is possible for any pair of deficiency indices to occur (see Exercise 6). 1t is possioie ior any pair oí aenciency inaices to occur (see Exercise o).

In order to study the closed symmetric extensions of a symmetric operator we also introduce the spaces

$$
\begin{array} { r l } & { \mathcal { K } _ { + } = \{ f   \oplus   i f \colon f   \in   \mathcal { L } _ { + } \} , } \\ & { \mathcal { K } _ { - } = \{ g   \oplus   ( - i g ) \colon g   \in   \mathcal { L } _ { - } \} . } \end{array}
$$

So $\mathcal { H } _ { \pm } \leqslant \mathcal { H } \oplus \mathcal { H }$ Notice that $\mathcal { K } _ { \pm }$ are contained in gra $A ^ { * }$ and are the portions of graph of $A ^ { * }$ that lie above $\mathcal { L } _ { \pm }$ . The next lemma will indicate why the deficiency subspaces are so named.

2.13. Lemma. If A is a closed symmetric operator,

$$
\mathrm{grad} A^{*} = \mathrm{grad} A \oplus \mathcal{H}_{+} \oplus \mathcal{H}_{-}.
$$

PROOF. Let $f \in \mathcal { L }$ + and h∈dom A. Then

$$
\begin{aligned}\langle h \oplus A h, f \oplus i f \rangle = & \langle h, f \rangle - i \langle A h, f \rangle \\= & - i \langle (A + i) h, f \rangle \\= & 0\end{aligned}
$$

since $\mathcal { L } _ { + } = [ \operatorname { r a n } ( A + i ) ] ^ { \perp }$ . The remainder of the proof that gra $A , \mathcal { H } _ { + } ,$ ,and $\mathcal { H } _ { - }$ are pairwise orthogonal is left to the reader. Since it is clear that gra $A \oplus \mathcal{H}_{+} \oplus \mathcal{H}_{-} \subseteq \mathrm{grad} A^*$ , it remains to show that this direct sum is dense in gra $A ^ { * }$

Let hedom $A ^ { * }$ and assume $h \oplus A^{*} h \perp \mathrm{grad} A \oplus \mathcal{H}_{+} \oplus \mathcal{H}_{-}$ Since $h \oplus$ $A ^ { * } h \perp \mathrm { g r a } A ,$ for every f in dom A, $0 = \langle h \oplus A ^ { * } h , f \oplus A f \rangle = \langle h , f \rangle +$ $\langle A ^ { * } h , A f \rangle$ . So $\langle A ^ { * } h , A f \rangle = - \langle h , f \rangle$ for every $f$ in dom A. This implies that A\*h∈dom $A ^ { * }$ and $A ^ { * } A ^ { * } h = -   h .$ Therefore $( A ^ { * } - i ) ( A ^ { * } + i ) h =$ $( A ^ { * } A ^ { * } + 1 ) h = 0 .$ Thus $( A ^ { * } + i ) h { \in } { \mathcal { L } } _ { + }$ . Reversing the order of these factors also shows that $( A ^ { * } - i ) h { \in } { \mathcal { L } } .$ . But if $g \in \mathcal { L } _ { + } , 0 = \langle h \oplus A ^ { * } h , g \oplus i g \rangle = \langle h , g \rangle -$ $i \langle A ^ { * } h , g \rangle = -   i \langle ( A ^ { * } + i ) h , g \rangle$ . Since g can be taken equal to $( A ^ { * } + i ) h ,$ we get that $( A ^ { * } + i ) h = 0 , \mathrm { o r } h \in \mathcal { L } _ { - }$ . Similarly, $h \in \mathcal { L } _ { + }$ . So $h \in \mathcal { L } _ { + } \cap \mathcal { L } _ { - } = ( 0 )$

2.14. Definition. If A is a closed symmetric operator and M is a linear manifold in dom $A ^ { * } ,$ then $\mathcal { M }$ is A-symmetric if $\langle A ^ { * } f , g \rangle = \langle f , A ^ { * } g \rangle$ for all $f , g$ in $\mathcal { M } .$ Call such a manifold A-closed if $\left\{ f \oplus A ^ { * } f \colon f { \in } { \mathcal { M } } \right\}$ is closed in $\mathcal { H } \oplus \mathcal { H }$

So $\mathcal { M }$ is both A-symmetric and A-closed precisely when $A ^ { * } | \mathcal { M }$ the restriction of $A ^ { * }$ to $\mathcal { M } ,$ is a closed symmetric operator; if $\mathcal { M } \supseteq \mathrm { d o m } \mathcal { A } ,$ then $A ^ { * } | M$ is a closed symmetric extension of A.

2.15. Lemma. If A is a closed symmetric operator on $\mathcal { H }$ and B is a closed symmetric extension of A, then there is an A-closed, A-symmetric submanifold M of $\mathcal { L } _ { + } + \mathcal { L } _ { - }$ - such that

## 2.16

$$
\mathrm { g r a }   B = \mathrm { g r a }   A + \mathrm { g r a } ( A ^ { * } | \mathcal { M } ) .
$$

Conversely, if M is an A-closed, A-symmetric manifold in $\mathcal { L } _ { + } + \mathcal { L } _ { - }$ , then there is a closed symmetric extension B of A such that (2.16) holds.

PRooF. If the A-symmetric manifold M in $\mathcal { L } _ { + } + \mathcal { L } _ { - }$ is given, let $\mathcal{D} = \mathrm{dom} A + \mathcal{M}$ Since $\mathcal { D } \subseteq \mathrm { d o m } A ^ { * } , \quad B = A ^ { * } | \mathcal { D }$ is well defined. Let $f = f _ { 0 } + f _ { 1 } , g = g _ { 0 } + g _ { 1 } , f _ { 0 } , g _ { 0 }$ in dom A and $f _ { 1 } , g _ { 1 }$ in $\mathcal { M } ,$ Then

$$
\begin{align*}\langle A^{\bullet} f, g \rangle &= \langle A^{\bullet} f_0 + A^{\bullet} f_1, g_0 + g_1 \rangle \\&= \langle A f_0, g_0 \rangle + \langle A f_0, g_1 \rangle + \langle A^{\bullet} f_1, g_0 \rangle + \langle A^{\bullet} f_1, g_1 \rangle.\end{align*}
$$

Using the A-symmetry of $\mathcal { M } ,$ the symmetry of $A ,$ and the definition of $A ^ { * }$ we get

$$
\begin{align*}\langle A^{\bullet} f, g \rangle &= \langle f_0, A g_0 \rangle + \langle f_0, A^{\bullet} g_1 \rangle + \langle f_1, A g_0 \rangle + \langle f_1, A^{\bullet} g_1 \rangle \\&= \langle f, A^{\bullet} g \rangle.\end{align*}
$$