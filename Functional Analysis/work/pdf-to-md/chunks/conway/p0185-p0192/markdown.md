## 1.11. Claim. $B ^ { * } ( y ^ { * } + \ker A ^ { * } ) = A ^ { * } y ^ { * }$ for all $y ^ { * }$ in $\mathcal { G } ^ { * }$

To see this, let $x   \in   \mathcal { X }$ and $y ^ { * } \in \mathcal { Y } ^ { * }$ . Making the appropriate identifications as in (V.2.2) and (V.2.3) gives $\langle   x + \ker A , B ^ { * } ( y ^ { * } + \ker A ^ { * } )   \rangle = \langle   B ( x +$ ker $A \left( y ^ { * } + \ker A ^ { * } \right) = \left\langle A x , y ^ { * } + ( \operatorname { r a n } A ) ^ { \perp } \right\rangle = \left\langle A x , y ^ { * } \right\rangle = \left\langle x , A ^ { * } y ^ { * } \right\rangle = \left\langle x + \operatorname { r a n } A \right\rangle$ $\left\langle \mathrm{ran} A^{*} \right\rangle \left( A^{*} y^{*} \right) = \left\langle x + \mathrm{ker} A, A^{*} y^{*} \right\rangle$ . Since x was arbitrary. (1.11) is established.

Note that Claim 1.11 implies that ran $B^{*} = \tan A^{*}$ . Hence ran $A ^ { * }$ is weak\* (resp., norm) closed if and only if ran $B ^ { * }$ is wea $\mathbf { k } ^ { * }$ (resp., norm) closed.

This discussion shows that the theorem is equivalent to the analogous theorem in which there is the additional hypothesis that A is injective and has dense range. It is assumed, therefore, that ker $A = ( 0 )$ and $\mathrm{cl}(\tan A) = \varnothing$

(a)⇒(b): Since ran A is closed, the additional hypothesis implies that A is bijective. By the Inverse Mapping Theorem, $A ^ { - 1 } \in \mathcal { B } ( \mathcal { Y } , \mathcal { X } )$ Hence $A ^ { * }$ is invertible (1.4c). Since $A ^ { * }$ is invertible, ran $A ^ { * } = \mathcal { X } ^ { * }$ and hence is weak\* closed.

$(c) \Rightarrow (b)$ : Since ran A is dense in $參 ,$ ker $A^{*} = (\mathrm{ran} A)^{\perp} (1.8) = (0)$ Thus $A ^ { * } ; { \mathcal { Y } } ^ { * }   \to   \operatorname { r a n } A ^ { * }$ is a bijection. Since ran $A ^ { * }$ is norm closed, it is a Banach space. By the Inverse Mapping Theorem, there is a constant $c   >   0$ such that $\left\|   A ^ { \star } y ^ { \star }   \right\| \geqslant c \left\|   y ^ { \star }   \right\|$ for all $y ^ { * }$ in $\mathcal { G } ^ { * }$

To show that ran $A ^ { * }$ is weak\* closed, the Krein-Smulian Theorem (V.12.6) will be used. Thus suppose $\{ A ^ { * } y _ { i } ^ { * } \}$ is a net in ran $A ^ { * }$ with $\| A ^ { * } y _ { i } ^ { * } \| \leqslant 1$ such that $A ^ { * } y _ { i } ^ { * }   \to   x ^ { * } \sigma ( { \mathcal { X } } ^ { * } , { \mathcal { X } } )$ for some $x ^ { * }$ in $\mathcal { X } ^ { * }$ . Thus $\| y _ { i } ^ { * } \| \leqslant c ^ { - 1 }$ for all $y _ { i } ^ { * }$ . By Alaoglu's Theorem there is a $y ^ { * }$ in $\mathcal { Q } *$ such that $y _ { i } ^ { * } \xrightarrow [ \mathrm { ~ c ~ } ] { \quad } y ^ { * } \sigma ( \mathcal { Y } ^ { * } , \mathcal { Y } )$ . Thus (1.3), $A ^ { * } y _ { i } ^ { * } \longrightarrow A ^ { * } y ^ { * } \quad \sigma ( \mathcal { X } ^ { * } , \mathcal { X } )$ , and so $x^{*} = A^{*} y^{*} \in \mathrm{rank} A^{*}$ . By (V.12.6), Cl ran $A ^ { * }$ is weak\* closed.

(b)⇒(a): Since ran $A ^ { * }$ is weak\* closed, ran $A^{*} = (\ker A)^{\perp} = \mathcal{X}^{*}$ Also ker $A^{*} = (\mathrm{rank} A)^{\perp} = (0)$ since A has dense range. Thus $A ^ { * }$ is a bijection and is thus invertible. By Proposition 1.9, A is invertible and thus has closed range. ■

A proof that condition (c) in the preceding theorem implies (a) which avoids the weak\* topology can be found in Kaufman [1966].

## EXERCISES

1. Prove Proposition 1.3.

2. Complete the proof of Proposition 1.4.

3. Verify the statement made in (1.5)

4. Verify the statement made in (1.6).

5. Verify the statement made in (1.7).

6. Let $1 \leqslant p < \infty$ and define S: $l ^ { p } \to l ^ { p }$ by $S(\alpha_{1},\alpha_{2},\ldots)=(0,\alpha_{1},\alpha_{2},\ldots)$ Compute $S ^ { * }$

7. Let $A   \in   \mathcal { B } ( c _ { 0 } )$ and for $n \geqslant 1$ , define $e _ { n }$ in $c _ { 0 }$ by $e _ { n } ( n ) = 1$ and $e _ { n } ( m ) = 0$ for $m \neq n .$ Put $\alpha_{mn} = (A e_n)(m)$ for $m , n \geqslant 1$ . Prove: (a) $M \equiv \sup_{m} \sum_{n = 1}^{\infty} \left| \alpha_{mn} \right| < \infty$ for every $n , \alpha _ { m n }   \rightarrow   0$ as $\stackrel { \mathrm { ~ \tiny ~ \bullet ~ } } { m } \rightarrow \infty$ . Conversely, if $\left\{ \alpha _ { m n } ; m , n \geqslant 1 \right\}$ are scalars satisfying (a) and (b), then

$$
(Ax)(m) = \sum_{n = 1}^{\infty} \alpha_{mn} x(n)
$$

defines a bounded operator A on $c _ { 0 }$ and $\| A \| = M$ . Find $A ^ { * } ,$

8. Let $A   \in   \mathcal { B } ( l ^ { 1 } )$ and for $n \geqslant 1$ define $e _ { n }$ in $l ^ { 1 }$ by $e_{n}(n)=1,\;e_{n}(m)=0$ for $m \neq n .$ Put $\alpha_{mn} = (A e_n)(m)$ for $m , n \geqslant 1$ . Prove: $M \equiv \sup_{n} \sum_{m = 1}^{\infty} \left| \alpha_{mn} \right| < \infty$ for every m, $\operatorname { s u p } _ { n } | \alpha _ { m n } | < \infty$ . Conversely, if $\left\{ \alpha _ { m n } : m , n \geqslant 1 \right\}$ are scalars satisfying (a) and (b), then

$$
(Af)(m) = \sum_{n = 1}^{\infty} \alpha_{mn} f(n)
$$

defines a bounded operator A on $l ^ { 1 }$ and $\| A \| = M$ Find $A ^ { * } ,$

9. (Bonsall [1986]) Let $\mathcal { X }$ be a Banach space, Z a nonempty set, and $u \colon  { \mathbb { Z } }   \to   \mathcal { X }$ . If there are positive constants $M _ { 1 }$ and $M _ { 2 }$ such that (i) $\| \boldsymbol { u } ( z ) \| \leqslant M _ { 1 }$ for all z in Z and (ii) for every $x ^ { * }$ in $\mathcal { X } ,$ sup $\left\{ \left| \left\langle u ( z ) , x ^ { * } \right\rangle \right| : z \in Z \right\} \geqslant M _ { 2 } \left\| x ^ { * } \right\| ;$ then for every x in $\mathcal { X }$ there is an f in $\dot { l ^ { 1 } ( Z ) }$ such that $( * ) x = \sum \{ f ( z ) u ( z ) : z { \in } Z \}$ and $M _ { 2 }$ inf $\| f \|_1 \leqslant \| x \| \leqslant M_1$ inf $\begin{array} { r } { \| \int \| _ { 1 } , } \end{array}$ where the infimum is taken over all f in $l ^ { 1 } ( Z )$ such that (\*) holds. (Hint: define $T { : }   l ^ { 1 } ( Z )   \to   \mathcal { X }$ by $T f = \sum \left\{ f ( z ) u ( z ) : z \in Z \right\} . )$

10. (Bonsall [1986]) Let m be normalized Lebesgue measure on ∂D and for $| z | < 1$ and $| w | = 1$ let $p _ { z } ( w ) = ( 1 - | z | ^ { 2 } ) / | 1 - \bar { z } w | ^ { 2 }$ So $p _ { z }$ is the Poisson kernel. Show that if $f { \in } L ^ { 1 } ( m ) ,$ then there is a sequence $\left\{ z _ { n } \right\} \subseteq \mathbf { D }$ and a sequence $\{ \lambda _ { n } \}$ in $l ^ { 1 }$ such that $\begin{array} { r } { ( \ast ) f = \sum _ { n = 1 } ^ { \infty } \lambda _ { n } p _ { z _ { n } } . } \end{array}$ Moreover, $\| f \| _ { 1 } = \inf \sum _ { n = 1 } ^ { \infty } | \lambda _ { n } | ,$ where the infimum is taken over all $\{ \lambda _ { n } \}$ in $l ^ { 1 }$ such that (\*) holds. (Hint: use Exercise 9.)

11. If X and Y are Banach spaces and $B { \in } { \mathcal { B } } ( { \mathcal { Y } } ^ { * } , { \mathcal { X } } ^ { * } ) ,$ , then there is an operator A in $\mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ such that $B = A ^ { * }$ if and only if B is wk\*-continuous.

12. If X is a Banach space and M and $\mathcal { N }$ are closed subspaces, show that the following statements are equivalent. (a) $\mathcal { M } + \mathcal { N }$ is closed. (b) the range of the linear transformation $x \to ( x + \mathcal { M } ) \oplus ( x + \mathcal { N } )$ from X into $\mathcal { X } / \mathcal { M } \oplus \mathcal { X } / \mathcal { N }$ is closed. (c) $\mathcal { M } ^ { \perp } + \mathcal { N } ^ { \perp }$ is norm closed in ${ \mathcal { X } } ^ { * } ,$ (d) $\mathcal { M } ^ { \perp } + \mathcal { N } ^ { \perp }$ is weak\* closed in $\mathcal { X } ^ { * }$

## $\S 2 ^ { * }$ . The Banach-Stone Theorem

As an application of the adjoint of a linear map, the isometries between spaces of the form $C ( X )$ and C(Y) will be characterized. Note that if X and Y are compact spaces, τ: $Y   \rightarrow   X$ is continuous map, and $A f = f \circ \tau$ for $f$ in $C ( X ) ,$ then (III.2.4) A is a bounded linear map and $\| { \pmb A } \| = 1$ Moreover, A is an isometry if and only if τ is surjective. If A is a surjective isometry, then τ must be a homeomorphism. Indeed, suppose A is a surjective isometry; it must be shown that τ is injective. If $y _ { 0 } , y _ { 1 }   \in   Y$ and $y _ { 0 } \neq y _ { 1 }$ , then there is a $g$ in $C ( Y )$ such that $g ( y _ { 0 } )   =   0$ and $g ( y _ { 1 } )   = 1$ . Let $f { \in } C ( X )$ such that $A f = g$ Thus $f(\tau(y_0)) = g(y_0) = 0$ and $f ( \tau ( y _ { 1 } ) ) = 1$ . Hence $\tau ( y _ { 0 } ) \neq \tau ( y _ { 1 } )$

So if τ: $Y   \to   X$ is a homeomorphism and α: $Y   \rightarrow   \mathbb { F }$ is a continuous function, with $| \alpha ( y ) | \equiv 1$ , then $T : C ( X ) \to C ( Y )$ defined by $( T f ) ( y ) = \alpha ( y ) f ( \tau ( y ) )$ is a surjective isometry. The next result gives a converse to this.

2.1. The Banach-Stone Theorem. If X and Y are compact and $T : C ( X ) \to C ( Y )$ is a surjective isometry, then there is a homeomorphism τ: $Y   \to   X$ and a function αin $C ( Y )$ such that $| \alpha ( y ) | = 1$ for all y and

$$
( T f ) ( y ) = \alpha ( y ) f ( \tau ( y ) )
$$

for all f in C(X) and y in Y.

PROOF. Consider $T ^ { * } \colon M ( Y ) \to M ( X )$ . Because T is a surjective isometry, $T ^ { * }$ is also. (Verify.) Thus $T ^ { * }$ is a weak\* homeomorphism of ball $M ( Y )$ onto ball $M ( X )$ that distributes over convex combinations. Hence (Why?)

$$
T ^ { * } ( \operatorname { e x t } [ \operatorname { b a l l } M ( Y ) ] ) = \operatorname { e x t } [ \operatorname { b a l l } M ( X ) ] .
$$

By Theorem V.8.4 this implies that for every y in Y there is a unique $\tau ( y )$ in X and a unique scalar $\alpha ( y )$ such that $| \alpha ( y ) | = 1$ and

$$
T ^ { * } ( \delta _ { y } ) = \alpha ( y ) \delta _ { \tau ( y ) } .
$$

By the uniqueness, α: Y →F and $\tau \colon Y   \to   X$ are well-defined functions.

## 2.2. Claim. α: $Y   \to   \mathbb { F }$ is continuous.

If $\{ y _ { i } \}$ is a net in Y and $y _ { i }   \rightarrow   y _ { \ast }$ then $\delta _ { y _ { i } }   \rightarrow   \delta _ { y }$ wea $\mathbf { k } ^ { * }$ in $M ( Y ) .$ Hence $\alpha ( y _ { i } ) \delta _ { \tau ( y _ { i } ) } = T ^ { * } ( \delta _ { y } ) \rightarrow T ^ { * } ( \delta _ { y } ) = \alpha ( y ) \delta _ { \tau ( y ) }$ weak\* in $M ( X )$ . In particular, $\alpha ( y _ { i } )   =$ $\langle 1 , T ^ { * } ( \delta _ { y _ { i } } ) \rangle \rightarrow \langle 1 , T ^ { * } ( \delta _ { y } ) \rangle = \alpha ( y ) ,$ proving (2.2).

## 2.3. Claim. τ: Y → X is a homeomorphism.

As in the proof of (2.2), if $y _ { i }   \rightarrow   y$ in Y, then $\alpha ( y _ { i } ) \delta _ { \tau ( y _ { i } ) } \rightarrow \alpha ( y ) \delta _ { \tau ( y ) }$ weak\* in M(X). Also, $\alpha ( y _ { i } )   \to   \alpha ( y )$ in F by (2.2). Thus $\delta _ { \tau ( y _ { i } ) } = \alpha ( y _ { i } ) ^ { - 1 } \left[ \alpha ( y _ { i } ) \delta _ { \tau ( y _ { i } ) } \right] \rightarrow \delta _ { \tau ( y ) } .$ By (V.6.1) this implies that $\tau ( y _ { i } )   \to   \tau ( y ) ,$ so that τ: $Y   \to   X$ is continuous.

If $y _ { 1 } , y _ { 2 }   \in   { \pmb Y }$ and $y _ { 1 } \neq y _ { 2 }$ , then $\alpha ( y _ { 1 } ) \delta _ { y _ { 1 } } \neq \alpha ( y _ { 2 } ) \delta _ { y _ { 2 } }$ . Since $T ^ { * }$ is injective, it is easy to see that $\tau ( y _ { 1 } ) \neq \tau ( y _ { 2 } )$ and so τ is one-to-one. If $x { \in } X$ , then the fact that $T ^ { * }$ is surjective implies that there is a $\mu$ in M(Y) such that $T ^ { * } \mu = \delta _ { x } .$ It must be that $\mu { \in } \mathtt { e x t } [$ [ball M(Y)] (Why?), so that $\mu = \beta \delta _ { y }$ for some y in Y and $\beta$ in F with $| \beta | = 1$ . Thus $\delta _ { x } = T ^ { * } ( \beta \delta _ { y } ) = \beta \alpha ( y ) \delta _ { \tau ( y ) }$ . Hence $\beta = \alpha ( y )$ and $\tau ( y ) = x .$ Therefore $\tau \colon Y   \to   X$ is a continuous bijection and hence must be a homeomorphism (A.2.8). This establishes (2.3).

If $f { \in } C ( X )$ and $y { \in } Y ,$ then $T(f)(y)=\left\langle T f, \delta_{y} \right\rangle=\left\langle f, T^{*} \delta_{y} \right\rangle=\left\langle f, \alpha(y) \delta_{\tau(y)} \right\rangle=$ $\alpha ( y ) f ( \tau ( y ) )$

## §3. Compact Operators

The following definition generalizes the concept of a compact operator from a Hilbert space to a Banach space.

3.1. Definition. If $\mathcal { X }$ and $\mathcal { Y }$ are Banach spaces and $A \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear transformation, then A is compact if cl A(ball X) is compact in $\mathcal { Y }$

The reader should become reacquainted with Section II.4.

It is easy to see that compact operators are bounded.

For operators on a Hilbert space the following concept is equivalent to compactness, as will be seen.

3.2. Definition. If $\mathcal { X }$ and $\theta$ are Banach spaces and $A   \in   \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ , then A is completely continuous if for any sequence $\left\{ x _ { n } \right\}$ in $\mathcal { X }$ such that $x _ { n }   \to   x$ weakly it follows that $\| A x _ { n } - A x \| \to 0$

3.3. Proposition. Let X and Y be Banach spaces and let $A   \in   \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$

(a) If A is a compact operator, then A is completely continuous.

(b) $I f \mathcal { X }$ is reflexive and A is completely continuous, then A is compact.

PROOF. (a) Let $\{ x _ { n } \}$ be a sequence in $\mathcal { X }$ such that $x _ { n }   \to   0$ weakly. By the PUB, $M = \sup_{n} \|x_{n}\| < \infty$ . Without loss of generality, it may be assumed that $M \leqslant 1$ . Hence $\{ A x _ { n } \} \subseteq \operatorname { c l } A ( \operatorname { b a l l } { \mathcal { X } } )$ . Since $A$ is compact, there is a subsequence $\left\{ x _ { n _ { k } } \right\}$ and a y in $\mathcal { Y }$ such that $\| A x _ { n _ { k } } - y \| \to 0 .$ But $x _ { n _ { k } } \rightarrow 0 \mathrm { ~ ( w k ) }$ and $A : ( \mathcal { X } , \mathbf { w k } ) \to ( \mathcal { Y } , \mathbf { w k } )$ is continuous (1.1c). Hence $A x _ { n _ { k } } \rightarrow A ( 0 ) = 0 ( \mathrm { w k } )$ . Thus $y = 0$ . Since 0 is the unique cluster point of $\{ A x _ { n } \}$ and this sequence is contained in a compact set, $\| A x _ { n } \|   \to   0$

(b) First assume that ¿ is separable; so (ball x, wk) is a compact metric space. So if $\{ x _ { n } \}$ is a sequence in ball X there is an x in X and a subsequence $\left\{ x _ { n _ { k } } \right\}$ such that $x _ { n _ { k } }   \rightarrow   x$ weakly. Since A is completely continuous, $\parallel A x _ { n _ { k } } -$ $A x \parallel \rightarrow 0$ . Thus A(ball ) is sequentially compact; that is, A is a compact operator.

Now let X be arbitrary and let $\{ x _ { n } \} \subseteq \mathrm { b a l l }   \mathcal { X }$ . If $\mathcal { X } _ { 1 } =$ the closed linear span of $\{ x _ { n } \}$ , then $\mathcal { X } _ { 1 }$ is separable and reflexive. If $A _ { 1 } = A | \mathcal { X } _ { 1 }$ , then $A _ { 1 } ; \mathcal { X } _ { 1 }   \rightarrow   \mathcal { Y }$ is easily seen to be completely continuous. By the first paragraph, $A _ { 1 }$ is compact. Thus $\left\{ A x _ { n } \right\} = \left\{ A _ { 1 } x _ { n } \right\}$ has a convergent subsequence. Since $\left\{ x _ { n } \right\}$ was arbitrary, A is a compact operator.

In the proof of (3.3b), the fact that A(ball X) is compact, and hence closed, is a consequence of the reflexivity of $\mathcal { X }$

By Proposition V.5.2, every operator in $\mathcal { B } ( l ^ { 1 } )$ is completely continuous. However, there are noncompact operators in $\mathcal { B } ( l ^ { 1 } )$ (for example, the identity operator).

There has been relatively little study of completely continuous operators that I am aware of. Most of the effort has been devoted to the study of compact operators and this is the direction we now pursue.

3.4. Schauder's Theorem. If $A   \in   \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ , then A is compact if and only if $A ^ { * }$ is compact.

ProOF. Assume A is a compact operator and let $\{ y _ { n } ^ { * } \}$ be a sequence in ball $\theta ^ { * }$ It must be shown that $\{ A ^ { * } y _ { n } ^ { * } \}$ has a norm convergent subsequence or, equivalently, a cluster point in the norm topology. By Alaoglu's Theorem, there is a $y ^ { * }$ in ball $\theta ^ { * }$ such that $y _ { n } ^ { * } \xrightarrow [ \mathrm { ~ c l ~ } ] { \quad } y ^ { * }$ (weak\*). It will be shown that $A^{*}y_{n}^{*} \xrightarrow[\mathrm{c}]{\quad } A^{*}y^{*}$ in norm.

Let $\varepsilon > 0$ and fix $N \geqslant 1$ . Because A(ball €) has compact closure, there are vectors $y _ { 1 } , \ldots , y _ { m }$ in Y such that $A ( \mathrm { b a l l } \mathcal { X } ) \subseteq \bigcup _ { k = 1 } ^ { m } \{ y \in \mathcal { Y } : \| y - y _ { k } \| < \varepsilon / 3 \}$ Since $y _ { n } ^ { \star } \xrightarrow [ \mathrm { ~ c l ~ } ] { \quad } y ^ { \star }$ (weak\*), there is an $n \geqslant N$ such that $| \langle y _ { k } , y ^ { * } - y _ { n } ^ { * } \rangle | < \varepsilon / 3$ for $1 \leqslant k \leqslant m.$ Let x be an arbitrary element in ball X and choose $y _ { k }$ such that $\| A x - y _ { k } \| < \varepsilon / 3$ . Then

$$
\begin{align*}\left| \left\langle x, A^{\star} y^{\star} - A^{\star} y_n^{\star} \right\rangle \right| &= \left| \left\langle Ax, y^{\star} - y_n^{\star} \right\rangle \right| \\&\leqslant \left| \left\langle Ax - y_k, y^{\star} - y_n^{\star} \right\rangle \right| + \left| \left\langle y_k, y^{\star} - y_n^{\star} \right\rangle \right| \\&\leqslant 2 \left\| Ax - y_k \right\| + \varepsilon / 3 < \varepsilon.\end{align*}
$$

Thus $\| A ^ { \star } y - A ^ { \star } y _ { n } ^ { \star } \| \leqslant \varepsilon .$

For the converse, assume $A ^ { * }$ is compact. By the first half of the proof, $A ^ { * * } ; { \mathcal { X } } ^ { * * }   \rightarrow   { \mathcal { Y } } ^ { * * }$ is compact. It is easy to check that $A = A ^ { * * } | { \mathcal { X } }$ is compact.

For Banach spaces $\mathcal { X }$ and $\mathcal { G } ,   \mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } )$ denotes the set of all compact operators from $\mathcal { X }$ into $\mathcal { Y } ;   \mathcal { B } _ { 0 } ( \mathcal { X } ) = \mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { X } )$

3.5. Proposition. Let ${ \mathcal { X } } , { \mathcal { Y } } ,$ and  be Banach spaces.

(a) $\mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } )$ is a closed linear subspace of $\mathcal { B } ( \mathcal { X } , \mathcal { Y } )$

(b) $If K \in \mathcal{B}_0(\mathcal{X}, \mathcal{Y})$ and $A \in \mathcal{B}(\mathcal{Y}, \mathcal{Z})$ , then $A K { \in } { \mathcal { B } } _ { 0 } ( { \mathcal { X } } , { \mathcal { X } } )$

(c) If $K { \in } { \mathcal { B } } _ { 0 } ( { \mathcal { X } } , { \mathcal { Y } } )$ and $A   \in   \mathcal { B } ( \mathcal { X } , \mathcal { X } )$ , then $K A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } )$

The proof of (3.5) is left as an exercise.

3.6. Corollary. $I f   \mathcal { X }$ is a Banach space, $\mathcal { B } _ { 0 } ( \mathcal { X } )$ is a closed two-sided ideal in the algebra $\mathcal { B } ( \mathcal { X } )$

Let $\mathcal { B } _ { 0 0 } ( \mathcal { X } , \mathcal { Y } ) =$ the bounded operators $T \colon { \mathcal { X } } \to { \mathcal { Y } }$ for which ran $T$ is finite dimensional. Operators in $\mathcal { B } _ { 0 0 } ( \mathcal { X } , \mathcal { Y } )$ are called operators with finite rank. It is easy to see that $\mathcal { B } _ { 0 0 } ( \mathcal { X } , \mathcal { Y } ) \subseteq \mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } )$ and by (3.5a) the closure of $\mathcal { B } _ { 0 0 } ( \mathcal { X } , \mathcal { Y } )$ is contained in $\mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } )$ . Is $\mathcal { B } _ { 0 0 } ( \mathcal { X } , \mathcal { Y } )$ dense in $\mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } ) ?$

It was shown in (II.4.4) that if $\mathcal { H }$ is a Hilbert space, then $\mathcal { B } _ { 0 } ( \mathcal { H } )$ is indeed the closure of $\mathcal { B } _ { 0 0 } ( \mathcal { H } )$ . Note that the availability of an orthonormal basis in a Hilbert space played a significant role in the proof of this theorem. There is a concept of a basis for a Banach space called a Schauder basis. Any Banach space $\mathcal { X }$ with a Schauder basis has the property that $\mathcal { B } _ { 0 0 } ( \mathcal { X } )$ is dense in $\mathcal { B } _ { 0 } ( \mathcal { X } )$ . Enflo [1973] gave an example of a separable reflexive Banach space $\mathcal { X }$ for which $\mathcal { B } _ { 0 0 } ( \mathcal { X } )$ is not dense in $\mathcal { B } _ { 0 } ( \mathcal { X } )$ , and, hence, $\mathcal { H }$ has no Schauder basis. Davie [1973] and [1975] have simplifications of Enflo's proof. For the classical Banach spaces, however, every compact operator is the limit of a sequence of finite-rank operators.

The remainder of this section is devoted to proving that for X compact, $\mathcal { B } _ { 0 0 } ( C ( X ) )$ is dense in $\mathcal { B } _ { 0 } ( C ( X ) )$ . This begins with material that may be familiar to many readers but will be presented for those who are unacquainted with it.

3.7. Definition. If X is completely regular and ${ \mathcal { F } } \subseteq C ( X )$ , then $\mathcal { F }$ is equicontinuous if for every $\varepsilon > 0$ and for every $x _ { 0 }$ in X there is a neighborhood $U$ of $x _ { 0 }$ such that $| f ( x ) - f ( x _ { 0 } ) | < \varepsilon$ for all x in U and for all f in $\mathcal { F }$

Note that for a single function f in $C ( X ) , \mathcal { F } = \{ f \}$ is equicontinuous. The concept of equicontinuity states that one neighborhood works for all $f$ in $\mathcal { F }$

3.8. The Arzela-Ascoli Theorem. If X is compact and ${ \mathcal { F } } \subseteq C ( X )$ , then $\mathcal { F }$ is totally bounded if and only if $\mathcal { F }$ is bounded and equicontinuous.

PROOF. Suppose $\mathcal { F }$ is totally bounded. It is easy to see that $\mathcal { F }$ is bounded. If $\varepsilon > 0 .$ , then there are $f _ { 1 } , \ldots , f _ { n }$ in $\mathcal { F }$ such that $\mathcal { F } \subseteq \bigcup _ { k = 1 } ^ { n } \left\{ f \in C ( X ) \right.$ $\| f - f _ { k } \| < \varepsilon / 3 \}$ . If $x _ { 0 }   \in   X$ , let U be an open neighborhood of $x _ { 0 }$ such that for $1 \leqslant k \leqslant n$ and x in $U ,   | f _ { k } ( x ) - f _ { k } ( x _ { 0 } ) | < \varepsilon / 3$ . If $f \in \mathcal { F }$ , let $f _ { k }$ be such that $\| f - f _ { k } \| < \varepsilon / 3$ . Then for x in U,

$$
\begin{aligned}|f(x) - f(x_0)| \leqslant & \left| f(x) - f_k(x) \right| + \left| f_k(x) - f_k(x_0) \right| \\& + \left| f_k(x_0) - f(x_0) \right| \\\leqslant & \varepsilon.\end{aligned}
$$

Hence $\mathcal { F }$ is equicontinuous.

Now assume that $\mathcal { F }$ is equicontinuous and ${ \mathcal { F } } \subseteq { \mathrm { b a l l } }   C ( X )$ Let $\varepsilon   >   0 .$ For each x in X, let $U _ { x }$ be an open neighborhood of x such that $| f ( x ) - f ( y ) | < \varepsilon / 3$ for $f$ in $\mathcal { F }$ and y in $U _ { x }$ Now $\{ U _ { x } ; x { \in } X \}$ is an open covering of X. Since X is compact, there are points $x _ { 1 } , \ldots , x _ { n }$ in X such that $X = \bigcup_{j = 1}^{n} U_{x}$

Let $\{ \alpha _ { 1 } , \ldots , \alpha _ { m } \} \subseteq \mathbb { D }$ such that cl $\mathbb{D} \subseteq \bigcup_{k=1}^{m} \{ \alpha : | \alpha - \alpha_k | < \varepsilon / 6 \}$ . Consider the collection B of those ordered n-tuples $\tilde { b } = ( \beta _ { 1 } , \ldots , \beta _ { n } )$ for which there is a function $f _ { b }$ in $\mathcal { F }$ such that $| f _ { b } ( x _ { j } ) - \beta _ { j } | < \varepsilon / 6$ for $1 \leqslant j \leqslant n .$ Note that B is not empty since $f ( x ) \subseteq$ cl D for every f in $\mathcal { F }$ . In fact, each f in $\mathcal { F }$ gives rise to such a b in B. Moreover B is finite. Fix one function $f _ { b }$ in $\mathcal { F }$ associated as above with b in B.

3.9. Claim. $\mathcal { F } \subseteq \bigcup _ { \boldsymbol { b } \in \boldsymbol { B } } \{ f \colon \| f - f _ { \boldsymbol { b } } \| < \varepsilon \}$

Note that (3.9) implies that $\mathcal { F }$ is totally bounded.

If $f \in \mathcal { F }$ , there is a b in B such that $| f ( x _ { j } ) - f _ { b } ( x _ { j } ) | < \varepsilon / 3$ for $1 \leqslant j \leqslant n$ Therefore if $x   \in   X$ , let $x _ { j }$ be chosen such that $x { \in } U _ { { \mathfrak { x } } _ { j } } .$ Thus $| f ( x ) - f _ { b } ( x ) | \leqslant$ $| f ( x ) - f ( x _ { j } ) | + | f ( x _ { j } ) - f _ { b } ( x _ { j } ) | + | f _ { b } ( x _ { j } ) - f _ { b } ( x ) | < \varepsilon$ Since x was arbitrary,一 $\| f - f _ { b } \| < \varepsilon$ ■

3.10. Corollary. If X is compact and ${ \mathcal { F } } \subseteq C ( X ) ,$ , then $\mathcal { F }$ is compact if and only $i f \mathcal { F }$ is closed, bounded, and equicontinuous.

3.11. Theorem. If X is compact, then $\mathcal { B } _ { 0 0 } ( C ( X ) )$ is dense in $\mathcal { B } _ { 0 } ( C ( X ) )$ .

PROOF. Let $T { \in } { \mathcal { B } } _ { 0 } ( C ( X ) )$ . Thus T(ball C(X)) is bounded and equicontinuous by the Arzela-Ascoli Theorem. If $\varepsilon   >   0$ and $x   \in   X$ , let $U _ { x }$ be an open neighborhood of x such that $| ( T f ) ( x ) - ( T f ) ( y ) | < \varepsilon$ for all f in ball $C ( X )$ and y in $U _ { x }$ Let $\{ x _ { 1 } , \ldots , x _ { n } \} \subseteq X$ such that $X \subseteq \bigcup _ { j = 1 } ^ { n } U _ { x _ { j } }$ . Let $\{ \phi _ { 1 } , \ldots , \phi _ { n } \}$ be a partition of unity subordinate to $\{ U _ { x _ { 1 } } , \ldots , U _ { x _ { n } } \}$ . Define $T _ { \varepsilon } \colon C ( X ) \to$ C(X) by

$$
T _ { \varepsilon } f = \sum _ { j = 1 } ^ { n } ( T f ) ( x _ { j } ) \phi _ { j } .
$$

Since ran $T _ { \varepsilon } \subseteq \vee \{ \phi _ { 1 } , \ldots , \phi _ { n } \} , T _ { \varepsilon } \in \mathcal { B } _ { 0 0 } ( C ( X ) )$

If f ∈ball C(X) and $x   \in   X$ , then

$$
\begin{align*}\left| (T_{\varepsilon} f)(x) - (T f)(x) \right| &= \left| \sum_{j=1}^{n} \left[ (T f)(x_j) - (T f)(x) \right] \phi_j(x) \right| \\&\leqslant \sum_{j=1}^{n} \left| (T f)(x_j) - (T f)(x) \right| \phi_j(x) \\&\leqslant \varepsilon.\end{align*}
$$

If X is locally compact, then the operators on $C _ { 0 } ( X )$ of finite rank are dense in $\mathcal { B } _ { 0 } ( C _ { 0 } ( X ) )$ . See Exercise 18.

EXERCISES

1. If X is reflexive and $A   \in   \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ , show that A(ball ) is closed in $\pmb { g }$

2. Prove Proposition 3.5.

3. If $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } )$ , show that cl [ran A] is separable.

4. If $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } , \mathcal { Y } )$ and ran A is closed, show that ran A is finite dimensional.

5. If $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ and A is invertible, show that dim $\mathcal { X } < \infty$

6. Let $( X , \Omega , \mu )$ be a finite measure space, $1 < p < \infty$ , and $1 / p + 1 / q = 1$ . If $k \colon X \times X \to \mathbb { F }$ is an $\mathbf { \Omega } \times \mathbf { \Omega } .$ -measurable function such that sup $\left\{ \int \left| k(x,y) \right|^q d\mu(y) \right\}$ $x { \in } X \} < \infty$ , then $(Kf)(x) = \int k(x,y)f(y)d\mu(y)$ defines a compact operator on $L ^ { p } ( \mu )$

7. Let $( X , \Omega , \mu )$ be an arbitrary measure space, $1 < p < \infty$ , and $1 / p + 1 / q = 1$ If $k \colon X \times X \to \mathbb { F }$ is an $\mathbf { \Omega } \times \mathbf { \Omega }$ -measurable function such that M = $\int ( \int | k(x,y) |^p d\mu(x) )^{q/p} d\mu(y) )^{1/q} < \infty$ and if $(Kf)(x) = \int k(x,y)f(y)d\mu(y),$ then $\widetilde { K } \in \mathcal { B } _ { 0 } ( L ^ { p } ( \mu ) )$ and $\left\| K \right\| \leqslant M$

8. Let X be a compact space and let $\mu$ be a positive Borel measure on $X ,$ Let $T { \in } { \mathcal { B } } ( L ^ { p } ( \mu ) , C ( X ) )$ where $1 < p < \infty$ . Show that if $A : L ^ { p } ( \mu ) \to L ^ { p } ( \mu )$ is defined by $A f = T f ,$ then A is compact.

9. (B.J. Pettis) If $\mathcal { X }$ is réflexive and $T   \in   \mathcal { B } ( \mathcal { X } , l ^ { 1 } )$ , then $T$ is a compact operator. Also, if y is reflexive and $T { \in } { \mathcal { B } } ( c _ { 0 } , { \mathcal { Y } } )$ , T is compact.

10. If X is compact and $\{ f _ { 1 } , \ldots , f _ { n } , g _ { 1 } , \ldots , g _ { n } \} \subseteq C ( X ) ,$ define $k(x,y)=\sum_{j = 1}^{n}f_{j}(x)g_{j}(y)$ for $x , y   \in   X$ Let $\mu$ be a regular Borel measure on X and put $K f ( x )   =$ $\int k ( x , y ) f ( y ) d \mu ( y )$ .Show that $K \in \mathcal{B}(C(X))$ and K has finite rank.

11. If X is compact, $k { \in } C ( X \times X ) ,$ and $\mu$ is a regular Borel measure on X, show that $K f ( x ) = \int k ( x , y ) f ( y ) d \mu ( y )$ defines a compact operator on C(X).

12. Let $( X , \Omega , \mu )$ be a σ-finite measure space and for $\phi$ in $L ^ { \infty } ( \mu )$ let $M _ { \phi } \colon L ^ { p } ( \mu ) \to L ^ { p } ( \mu )$ be the multiplication operator defined in Example III.2.2. Give necessary and sufficient conditions on $( X , \Omega , \mu )$ and $\phi$ for $M _ { \phi }$ to be compact.

13. Let $\tau \colon [ 0 , 1 ]   \to   [ 0 , 1 ]$ be continuous and define $A \colon C [ 0 , 1 ] \to C [ 0 , 1 ]$ by $A f = f \circ \tau$ Give necessary and sufficient conditions on τ for A to be compact.

14. Let $A   \in   \mathcal { B } ( c _ { 0 } )$ and let $( \alpha _ { m n } )$ be the corresponding matrix as in Exercise 1.7. Give necessary and sufficient conditions on $( \alpha _ { m n } )$ for A to be compact.

15. Let $A   \in   \mathcal { B } ( l ^ { 1 } )$ and let $( \alpha _ { m n } )$ be the corresponding matrix as in Exercise 1.8. Give a necessary and sufficient condition on $( \alpha _ { m n } )$ for A to be compact.

16. If $( X , d )$ is a compact metric space and ${ \mathcal { F } } \subseteq C ( X )$ , show that $\mathcal { F }$ is equicontinuous if and only if for every $\varepsilon   >   0$ there is a $\delta   >   0$ such that $| f ( x ) - f ( y ) | < \varepsilon$ whenever $d ( x , y ) < \delta$ and $f \in \mathcal { F }$

17. If X is locally compact and $\mathcal { F } \subseteq C _ { 0 } ( X ) ,$ ,show that $\mathcal { F }$ is totally bounded if and only if (a) $\mathcal { F }$ is bounded; (b) $\mathcal { F }$ is equicontinuous; (c) for every $\varepsilon   >   0$ there is a compact subset K of X such that $| f ( x ) | < \varepsilon$ for all f in $\mathcal { F }$ and x in $X \backslash K .$

18. If X is locally compact and $A { \in } { \mathcal { B } } _ { 0 } ( C _ { 0 } ( X ) )$ , then there is a sequence $\{ A _ { n } \}$ of finiterank operators such that $\| A _ { n } - A \| \to 0 .$

19. Let X be a Banach space and suppose there is a net $\left\{ F _ { i } \right\}$ of finite-rank operators on $\mathcal { X }$ such that $(a) \sup_{i} \| \boldsymbol{F}_{i} \| < \infty; (b) \| \boldsymbol{F}_{i} \boldsymbol{x} - \boldsymbol{x} \| \rightarrow 0$ for all x in X. Show that if $A   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ , then $\| \boldsymbol{F}_i \boldsymbol{A} - \boldsymbol{A} \| \rightarrow 0$ and hence there is a sequence $\{ A _ { n } \}$ of finite-rank operators on $\mathcal { X }$ such that $\left\| \boldsymbol{A}_{n} - \boldsymbol{A} \right\| \rightarrow 0$