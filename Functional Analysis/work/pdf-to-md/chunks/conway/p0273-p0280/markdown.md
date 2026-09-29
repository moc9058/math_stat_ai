result is crucial for this purpose. It tells us how to integrate with respect to a spectral measure.

1.10. Proposition. If E is a spectral measure for $( X , \Omega , \mathcal { H } )$ and φ: $X   \to   \mathbb { C }$ is a bounded Ω-measurable function, then there is a unique operator A in $\mathcal { B } ( \mathcal { H } )$ such that $\mathit { i f }   \varepsilon   >   0$ and $\{ \Delta _ { 1 } , \ldots , \Delta _ { n } \}$ is an Ω-partition of X with sup $\left\{ | \phi ( x ) - \phi ( x ^ { \prime } ) | \right.$ $x , x ^ { \prime } { \in } \Delta _ { k } \} < \varepsilon$ for $1 \leqslant k \leqslant n ,$ then for any $x _ { k }$ in $\Delta _ { k } ,$

$$
\left\| A - \sum_{k = 1}^{n} \phi(x_k) E(\Delta_k) \right\| < \varepsilon.
$$

PROOF. Define $B ( g , h ) \equiv \int \phi   d E _ { g , h }$ for $g , h$ in $\mathcal { H } ,$ By the preceding lemma it is easy to see that B is a sesquilinear form with $| B ( g , h ) | \leqslant \| \phi \| _ { \infty } \| g \| \| h \|$ 1 Hence there is a unique operator A such that $B ( g , h ) = \langle A g , h \rangle$ for all g and h in $\mathcal { H }$

Let $\{ \Delta _ { 1 } , \ldots , \Delta _ { n } \}$ be an Ω-partition satisfying the condition in the statement of the proposition. If $g$ and h are arbitrary vectors in $\mathcal { H }$ and $x _ { k } { \in } \Delta _ { k }$ for $1 \leqslant k \leqslant n ,$ then

$$
\begin{align*}\left| \langle Ag, h \rangle - \sum_{k=1}^n \phi(x_k) \langle E(\Delta_k) g, h \rangle \right| &= \left| \sum_{k=1}^n \int_{\Delta_k} \left[ \phi(x) - \phi(x_k) \right] d \langle E(x) g, h \rangle \right| \\& \leq \sum_{k=1}^n \int_{\Delta_k} \left| \phi(x) - \phi(x_k) \right|   d \left| \langle E(x) g, h \rangle \right| \\& \leq \varepsilon \int_{\varepsilon} d \left| \langle E(x) g, h \rangle \right| \leq \varepsilon \| g \| \| h \|.\end{align*}
$$

The operator A obtained in the preceding proposition is the integral of $\phi$ with respect to E and is denoted by

$$
\int \phi d E .
$$

Therefore if $g , h \in \mathcal { H }$ and $\phi$ is a bounded Ω-measurable function on $X ,$ the preceding proof implies that

## 1.11

$$
\left\langle \left( \int \phi d E \right)   g , h \right\rangle = \int \phi d E _ { g , h } .
$$

Let B(X,Ω) denote the set of bounded Ω-measurable functions $\phi \colon X   \to   \mathbb { C }$ and let $\| \phi \| = \operatorname* { s u p } \{ | \phi ( x ) | : x { \in } X \}$ . It is easy to see that $B ( X , \Omega )$ is a Banach algebra with identity. In fact, if $\phi ^ { \star } ( x ) \equiv \phi ( x )$ , then $B ( X , \Omega )$ is an abelian $C ^ { * } \mathtt { - a l g e b r a }$ . The properties of the integral $\int   \phi d E$ are summarized by the following result.

1.12. Proposition. If E is a spectral measure for $( X , \Omega , \mathcal { H } )$ and $\rho ;$ $B ( X , \Omega ) \to \mathcal { B } ( \mathcal { H } )$ is defined by $\rho ( \phi ) = \int \phi   d E ,$ , then ρ is representation of $B ( X , \Omega )$ and $\rho ( \phi )$ is a normal operator for every $\phi$ in $B ( X , \Omega )$

PRooF. It will only be shown that $\rho$ is multiplicative; the remainder is an exercise. Let $\phi$ and $\psi   \in   B ( X , \Omega )$ . Let $\varepsilon   >   0$ and choose a Borel partition $\{ \Delta _ { 1 } , \ldots , \Delta _ { n } \}$ of X such that sup $\left\{ | \omega ( x ) - \omega ( x ^ { \prime } ) | : x , x ^ { \prime } \in \Delta _ { k } \right\} < \varepsilon$ for $\omega = \phi .$ ψ or $\phi \psi$ and for $1 \leqslant k \leqslant n$ Hence, if $x_{k} \in \Delta_{k} \left( 1 \leqslant k \leqslant n \right)$

$$
\left\| \int \omega d E - \sum_{k=1}^{n} \omega(x_k) E(\Delta_k) \right\| < \varepsilon
$$

for $\omega = \phi , \psi .$ or $\phi \psi .$ Thus, using the triangle inequality,

$$
\begin{align*}\left\| \int & \phi \psi   dE - \left( \int \phi   dE \right) \left( \int \psi   dE \right) \right\| \\& \leqslant \varepsilon + \left\| \sum_{k=1}^{n} \phi(x_k) \psi(x_k) E(\Delta_k) - \left[ \sum_{i=1}^{n} \phi(x_i) E(\Delta_i) \right] \left[ \sum_{j=1}^{n} \psi(x_j) E(\Delta_j) \right] \right\| \\& \quad + \left\| \left[ \sum_{i=1}^{n} \phi(x_i) E(\Delta_i) \right] \left[ \sum_{j=1}^{n} \psi(x_j) E(\Delta_j) \right] - \left( \int \phi   dE \right) \left( \int \psi   dE \right) \right\|.\end{align*}
$$

But $E ( \Delta _ { i } ) E ( \Delta _ { j } ) = E ( \Delta _ { i } \cap \Delta _ { j } )$ and $\{ \Delta _ { 1 } , \ldots , \Delta _ { n } \}$ is a partition. So the middle term in this sum is zero. Hence

$$
\begin{align*}& \left\| \int \phi \psi   dE - \left( \int \phi   dE \right) \left( \int \phi dE \right) \right\| \\& \quad \leqslant \varepsilon + \left\| \left[ \sum_{i=1}^{n} \phi(x_i) E(\Delta_i) \right] \left[ \sum_{j=1}^{n} \psi(x_j) E(\Delta_j) - \int \psi dE \right] \right\| \\& \quad + \left\| \left[ \sum_{i=1}^{n} \phi(x_i) E(\Delta_i) - \int \phi dE \right] \left[ \int \psi dE \right] \right\| \leqslant \varepsilon [1 + \| \phi \| + \| \psi \|].\end{align*}
$$

Since ε was arbitrary, $\int \phi \psi   d E = ( \int \phi   d E ) ( \int \psi   d E )$

1.13. Corollary. If X is a compact Hausdroff space and E is a spectral measure defined on the Borel subsets of X, then $\rho : C ( X ) \to { \mathcal { B } } ( { \mathcal { H } } )$ defined by $\rho ( u ) = \int$ udE is a representation of C(X).

The next result is the main result of this section and it states that the converse to the preceding corollary holds.

1.14. Theorem. $I f \rho : C ( X ) \to { \mathcal { B } } ( { \mathcal { H } } )$ is a representation, there is a unique spectral measure E defined on the Borel subsets of X such that for all $g$ and h in $\mathcal { H }$ $E _ { g , h }$ is a regular measure and

$$
\rho ( u ) = \int u d E
$$

for every u in $C \left( X \right)$

ProoF. The idea of the proof is similar to the idea of the proof of the Riesz

Representation Theorem for linear functionals on $C ( X )$ . We wish to extend $\rho$ to a representation $\tilde { \rho } \colon B ( X ) \to { \mathcal { B } } ( { \mathcal { H } } )$ , where $B ( X )$ is the $C ^ { * } \mathtt { - a l g e b r a }$ of bounded Borel functions. The measure E of a Borel set $\pmb { \Delta }$ is then defined by letting $E ( \Delta ) = \tilde { \rho } ( \chi _ { \Delta } )$ In fact, it is possible to give a proof of the theorem patterned on the proof of the Riesz Representation Theorem. Here, however, the proof will use the Riesz Representation Theorem to simplify the technical details.

If $g , h \in \mathcal { H }$ , then $u \mapsto \langle \rho ( u ) g , h \rangle$ is a linear functional on $C ( X )$ with norm $\leqslant \| g \| \| \boldsymbol { h } \|$ . Hence there is a unique measure, $\mu _ { g , h }$ in $M ( X )$ such that

## 1.15

$$
\langle \rho ( u ) g , h \rangle = \int u d \mu _ { g , h }
$$

for all u in $C ( X ) .$ It is easy to verify that the map $( g , h )   \mapsto   \mu _ { g , h }$ is sesquilinear (use uniqueness) and $\| \mu _ { g , h } \| \leqslant \| g \|   \| h \|$ . Now fix $\phi$ in B(X) and define $[ g , h ] = \int \phi   d \mu _ { g , h } .$ Then $[ \cdot , \cdot ]$ is a sesquilinear form and $| [ g , h ] | \leqslant \| \phi \|   \| g \|   \| h \|$ Hence there is a unique bounded operator $A$ such that $[ g , h ] = \langle A g , h \rangle$ and $\| A \| \leqslant \| \phi \|$ (II.2.2). Denote the operator $A$ by $\tilde { \rho } ( \phi )$ . So $\tilde { \rho } \colon B ( X ) \to { \mathcal { B } } ( { \mathcal { H } } )$ is a well-defined function, $\| \tilde { \rho } ( \phi ) \| \leqslant \| \phi \|$ , and for all $g , h$ in $\mathcal { H } ,$

## 1.16

$$
\langle   \tilde { \rho } ( \phi ) g , h   \rangle = \int   \phi   d \mu _ { g , h } .
$$

1.17. Claim. $\tilde { \rho } \colon B ( X ) \to { \mathcal { B } } ( { \mathcal { H } } )$ is a representation and $\tilde { \rho } | C ( X ) = \rho .$

The fact that $\tilde { \rho } ( u ) = \rho ( u )$ whenever $u   \in   C ( X )$ follows immediately from (1.15) and (1.16). If $\phi   \in   B ( X )$ , consider $\phi$ as an element of $M ( X ) ^ { * } ( = C ( X ) ^ { * * } ) .$ ; that is, $\phi$ corresponds to the linear functional $\mu { \mapsto } { \int } \phi   d \mu .$ By Proposition V.4.1, $\{ u { \in } C ( X ) { : } \| u \| \leqslant \| \phi \| \}$ is $\sigma ( M ( X ) ^ { * } ,   M ( X ) )$ dense in $\{ L { \in } M ( X ) ^ { * } { : } \| L \| \leqslant \| \phi \| \}$ Thus there is a net $\{ u _ { i } \}$ in $C ( X )$ such that $\| u _ { i } \| \leqslant \| \phi \|$ for all $u _ { i }$ and $\int   u _ { i }   d \mu   \to   \int   \phi   d \mu$ for every $\mu$ in $M ( X )$ . If $\psi   \in   B ( X )$ , then $\psi \mu { \in } M ( X )$ whenever $\mu { \in } M ( X ) .$ Hence $\int   u _ { i } \psi   d \mu   \to   \int   \phi \psi   d \mu$ for every ψ in B(X) and $\mu$ in M(X). By $( 1 . 1 6 ) ,   \tilde { \rho } ( u _ { i } \psi )   \rightarrow   \tilde { \rho } ( \dot { \phi } \psi )   ( \mathrm { W O T } )$ for all $\psi$ in B(X). In particular, if $\psi   \in   C ( X )$ , then $\tilde { \rho } ( \phi \psi ) = \mathrm { W O T } - \lim \tilde { \rho } ( u _ { i } \psi ) = \mathrm { W O T } - \lim \rho ( u _ { i } ) \rho ( \psi ) = \tilde { \rho } ( \phi ) \rho ( \psi )$ . That is,

$$
\tilde { \rho } ( \phi \psi ) = \tilde { \rho } ( \phi ) \rho ( \psi )
$$

whenever $\phi   \in   B ( X )$ and $\psi \in C ( X )$ . Hence $\tilde { \rho } ( u _ { i } \psi ) = \rho ( u _ { i } ) \tilde { \rho } ( \psi )$ for any $\psi$ in $B ( X )$ and for all $u _ { i } .$ Since $\tilde { \rho } ( u _ { i } )   \rightarrow   \tilde { \rho } ( \phi )$ (WOT) and $\tilde { \rho } ( u _ { i } \psi )   \rightarrow   \tilde { \rho } ( \phi \psi ) ~ \left( \mathrm { W O T } \right)$ , this implies that

$$
\tilde { \rho } ( \phi \psi ) = \tilde { \rho } ( \phi ) \tilde { \rho } ( \psi )
$$

whenever $\phi ,   \psi   \in   B ( X )$

The proof that $\tilde { \rho }$ is linear is immediate by (1.16). To see that $\tilde { \rho } ( \phi ) ^ { * } = \tilde { \rho } ( \bar { \phi } )$ Let $\{ u _ { i } \}$ be the net obtained in the preceding paragraph. If $\mu { \in } M ( X ) ,$ let $\bar { \mu }$ be the measure defined by $\bar { \mu } ( \Delta ) = \mu ( \Delta )$ . Then $\rho ( u _ { i } )   \to   \tilde { \rho } ( \phi )$ (WOT) and so $\rho ( u _ { i } ) ^ { * }   \rightarrow   \tilde { \rho } ( \phi ) ^ { * } \mathrm { ~ ( W O T ) }$ . But $\int \bar{u}_{i} d \mu = \int \overline{u_{i} d \bar{\mu}} \rightarrow \int \phi d \bar{\mu} = \int \bar{\phi} d \mu$ for every measure $\mu .$ Hence $\rho ( \bar { u } _ { i } )   \rightarrow   \tilde { \rho } ( \bar { \phi } )$ . But $\rho ( u _ { i } ) ^ { * } = \rho ( \bar { u } _ { i } )$ since $\rho$ is a \*-homomorphism. Thus $\tilde { \rho } ( \phi ) ^ { * } = \tilde { \rho } ( \bar { \phi } )$ and $\tilde { \rho }$ is a representation.

For any Borel subset $\Delta$ of X let $E ( \Delta ) \equiv \tilde { \rho } ( \chi _ { \Delta } )$ . We want to show that E is a spectral measure. Since $\chi _ { \Delta }$ is a hermitian idempotent in $B ( X ) , \; E ( \Delta )$ is a projection by (1.17). Since $\chi _ { \Box }   =   0$ and $\chi_{X}=1, E(\Box)=0$ and $E ( X ) = 1$ . Also, $E ( \Delta _ { 1 } \cap \Delta _ { 2 } ) = \tilde { \rho } ( \chi _ { \Delta _ { 1 } \cap \Delta _ { 2 } } ) = \tilde { \rho } ( \chi _ { \Delta _ { 1 } } \chi _ { \Delta _ { 2 } } ) = E ( \Delta _ { 1 } ) E ( \Delta _ { 2 } )$ . Now let $\{ \Delta _ { n } \}$ be a pairwise disjoint sequence of Borel sets and put $\Lambda_{n}=\bigcup_{k = n + 1}^{\infty}\Delta_{k}$ . It is easy to see that $E$ is finitely additive so if $h \in \mathcal { H }$ , then

$$
\begin{align*}\left\| E \Bigg( \bigcup_{k=1}^{\infty} \Delta_k \Bigg) h - \sum_{k=1}^{n} E(\Delta_k) h \right\|^2 &= \langle E(\Lambda_n) h, E(\Lambda_n) h \rangle \\&= \langle E(\Lambda_n) h, h \rangle \\&= \langle \tilde{\rho}(\chi_{\Lambda_n}) h, h \rangle \\&= \int \chi_{\Lambda_n} d\mu_{h,h} \\&= \sum_{k=n+1}^{\infty} \mu_{h,h}(\Delta_k) \to 0.\end{align*}
$$

as $n   \rightarrow   \infty$ . Therefore E is a spectral measure.

It remains to show that $\rho ( u ) = \int u   d E$ . It will be shown that $\tilde { \rho } ( \phi ) = \int \phi   d E$ for every $\phi$ in B(X). Fix $\phi$ in $B ( \dot { X } )$ and $\varepsilon   >   0$ If $\{ \Delta _ { 1 } , \ldots , \Delta _ { n } \}$ is any Borel partition of X such that sup $\left\{ | \phi ( x ) - \phi ( x ^ { \prime } ) | : x , x ^ { \prime } \in \Delta _ { k } \right\} < \varepsilon$ for $1 \leqslant k \leqslant n .$ , then $\begin{array} { r } { \| \phi - \sum _ { k = 1 } ^ { n } \phi ( x _ { k } ) \chi _ { \Delta _ { k } } \| _ { \infty } < \varepsilon } \end{array}$ for any choice of $x _ { k }$ in $\Delta _ { k }$ Since $\| \tilde { \boldsymbol { \rho } } \| = 1$ 2 $\begin{array} { r } { \varepsilon > \| \tilde { \rho } ( \phi ) - \sum _ { k = 1 } ^ { n } \phi ( x _ { k } ) E ( \Delta _ { k } ) \| } \end{array}$ . This implies that $\tilde { \rho } ( \phi ) = \int \phi   d E$ for any $\phi$ in B(X).

The proof of the uniqueness of E is left to the reader.

## EXERCISES

1. Prove Proposition 1.3.

2. Show that ball $\mathcal { B } ( \mathcal { H } )$ is WOT compact.

3. Show that $\operatorname { R e } { \mathcal { B } } ( { \mathcal { H } } )$ and $\mathcal { B } ( \mathcal { H } ) ,$ are WOT and SOT closed.

4. If $L : \mathcal { B } ( \mathcal { H } ) \to \mathbb { C }$ is a linear functional, show that the following statements are equivalent: (a) Lis SOT-continuous; (b) Lis WOT-continuous; (c) there are vectors $h _ { 1 } , \ldots , h _ { n } , g _ { 1 } , \ldots , g _ { n }$ in $\mathcal { H }$ such that $L(A)=\sum_{j = 1}^{n}\langle A h_{j},g_{j}\rangle$

5. Show that a convex subset of $\mathcal { B } ( \mathcal { H } )$ is WOT closed if and only if it is SOT closed.

6. Verify the statement in Example 1.5.

7. Verify the statements made in Examples 1.6, 1.7, and 1.8.

8. For the spectral measures in (1.6), (1.7), and (1.8), give the corresponding representations.

9. If $\{ \mathbf { E } _ { i } \}$ is a net of projections and E is a projection, show that $E _ { i }   \rightarrow   E \left( \mathrm { W O T } \right)$ if and only if $E _ { i }   \rightarrow   E \left( \mathrm { S O T } \right)$

10. For the representation in (VIII.5.5), find the corresponding spectral measure.

11. In Example VIII.5.4, the representation is not quite covered by Theorem 1.14 since it is a representation of $L ^ { \infty } ( \mu )$ and not C(X). Nevertheless, this representation is given by a spectral measure defined on Ω. Find it.

12. Let X be a compact Hausdorff space and let $\{ x _ { n } \}$ be a sequence in $X .$ Let $\{ e _ { n } \}$ be an orthonormal basis for $\mathcal { H }$ and for each u in $C ( X )$ define $\rho ( u )$ in $\mathcal { B } ( \mathcal { H } )$ by $\rho ( u ) e _ { n } = u ( x _ { n } ) e _ { n } .$ Show that $\rho$ is a representation and find the corresponding spectral measure.

13. A representation $\rho \colon \mathcal { A } \to \mathcal { B } ( \mathcal { H } )$ is irreducible if the only projections in $\mathcal { B } ( \mathcal { H } )$ that commute with every $\rho ( a )$ , a in $\alpha ,$ are 0 and 1. Prove that if $\varkappa$ is abelian and $\rho$ is an irreducible representation of $\alpha ,$ then dim $\mathcal { H } = 1$ . Find the corresponding spectral measure.

14. Show that a representation $\rho \colon C ( X ) \to { \mathcal { B } } ( { \mathcal { H } } )$ is injective if and only if $E ( G ) \neq 0$ for every non-empty open set G, where E is the corresponding spectral measure.

15. Let $\{ A _ { i } \}$ be a net of hermitian operators on $\mathcal { H }$ and suppose that there is a hermitian operator $T$ such that $A _ { i }   \leqslant   T$ for all i. If $\{ \langle A _ { i } h , h \rangle \}$ is an increasing net in R for every h in $\mathcal { H }$ , then there is a hermitian operator A such that $A _ { i } \rightarrow A ( \mathrm { W O T } )$

16. Show that there is a contraction $\tau : { \mathcal { B } } ( { \mathcal { H } } ) ^ { * * } \to { \mathcal { B } } ( { \mathcal { H } } )$ such that $\tau ( T )   =   T$ for T in $\mathcal { B } ( \mathcal { H } )$ . If $\rho : C ( X ) \to { \mathcal { B } } ( { \mathcal { H } } )$ is a representation, show that the map $\tilde { \rho }$ in the proof of Theorem 1.14 is given by $\tilde { \rho } ( \phi ) = \tau \circ \rho ^ { * * } ( \phi )$

## §2. The Spectral Theorem

The Spectral Theorem is a landmark in the theory of operators on a Hilbert space. It provides a complete statement about the nature and structure of normal operators. This accolade will be seen to be deserved when in Section 10 the Spectral Theorem is used to give a complete set of unitary invariants. Two operators A and B are unitarily equivalent if there is a unitary operator U such that $U A U ^ { * } = B ;$ in symbols, $A \cong B .$ Using the Spectral Theorem, a (countable) set of objects is attached to a normal operator N on a (separable) Hilbert space. It is then shown that two normal operators are unitarily equivalent if and only if these objects are equal.

The Spectral Theorem for a normal operator N on a Hilbert space with dim $\mathcal { H } = d < \infty$ says that N can be diagonalized. That is, if $\alpha _ { 1 } , \ldots , \alpha _ { d }$ are the eigenvalues of N (repeated as often as their multiplicities), then the corresponding eigenvectors $e _ { 1 } , e _ { 2 } , \ldots , e _ { d }$ from an orthonormal basis for $\mathcal { H }$ In infinite dimensional spaces a normal operator need not have eigenvalues. For example, let N = multiplication by the independent variable on $L ^ { 2 } ( 0 , 1 )$ So an alternative formulation that can be generalized is desired.

Let N be normal on $\mathcal { H }$ , dim $\mathcal { H } = d < \infty$ . Let $\lambda _ { 1 } , . . . , \lambda _ { n }$ be the distinct eigenvalues of N and let $E _ { k }$ be the orthogonal projection of $\mathcal { H }$ onto ker $( N - \lambda _ { k } ) , \; 1 \leqslant k \leqslant n$ . Then the Spectral Theorem says that

## 2.1

$$
N = \sum _ { k   =   1 } ^ { n } \lambda _ { k } E _ { k } .
$$

In this form a generalization is possible. Rather than discuss orthogonal projections on eigenspaces (which may not exist), the concept of a spectral measure is used; rather than the sum that appears in (2.1), an integral is used. It is worth mentioning that the finite dimensional version is a corollary of the general theorem (see Exercise 4).

2.2. The Spectral Theorem. If N is a normal operator, there is a unique spectral measure E on the Borel subsets of $\sigma ( N )$ such that:

(a) $N = \int z   d E ( z ) ;$

(b) if G is a nonempty relatively open subset of $\sigma ( N ) ,   E ( G ) \neq 0 ;$

(c) if $A \in \mathcal { B } ( \mathcal { H } ) ,$ then $A N = N A$ and $A N ^ { * } = N ^ { * } A$ if and only if $A E ( \Delta ) =$ E(∆)A for every ∆.

PROOF. Let $\mathcal { A } = C ^ { * } ( N )$ , the $C ^ { * } .$ -algebra generated by N. So  is the closure of all polynomials in N and $N ^ { * }$ . By Theorem VIII.2.6, there is an isometric isomorphism $\rho \colon C ( \sigma ( N ) )   \to   \mathcal { A } \subseteq \mathcal { B } ( \mathcal { H } )$ given by $\rho ( u ) = u ( N )$ (the functional calculus). By Theorem 1.14 there is a unique spectral measure E defined on the Borel subsets of $\sigma ( N )$ such that $\rho ( u ) = \int u   d E$ for all u in $C ( \sigma ( N ) )$ . In particular, (a) holds since $N = \rho ( z )$

If G is a nonempty relatively open subset of $\sigma ( N )$ , there is a nonzero continuous function u on $\sigma ( N )$ such that $0 \leqslant u \leqslant \chi _ { G }$ . Using Claim 1.17, one obtains that $E ( G ) = \tilde { \rho } ( \chi _ { G } ) \geqslant \rho ( u ) \neq 0 ;$ so (b) holds.

Now let $A   \in   \mathcal { B } ( \mathcal { H } )$ such that $A N = N A$ and $A N ^ { * } = N ^ { * } A$ . It is not hard to see that this implies, by the Stone-Weierstrass Theorem, that $A \rho ( u ) = \rho ( u ) A$ for every u in $C ( \sigma ( \bar { N } ) ) ;$ that is, $A u ( N ) = u ( N ) A$ for all u in $C ( \sigma ( N ) )$ . Let $\mathbf { \Omega } = \left\{ \mathbf { \Delta } \mathbf { : \Delta } \right.$ is a Borel set and $AE(\Delta) = E(\Delta)A$ . It is left to the reader to show that Ω is a $\sigma - \mathrm { a l g e b r a }$ . If G is an open set in $\sigma ( N ) .$ , there is a sequence $\{ u _ { n } \}$ of positive continuous functions on $\sigma ( N )$ such that $u _ { n } ( z ) \uparrow \chi _ { G } ( z )$ for all z. Thus

$$
\begin{aligned}\langle   AE(G)g,h   \rangle &= \langle   E(G)g,A^*h   \rangle \\&= E_{g,A^*h}(G) \\&= \lim \int u_n   dE_{g,A^*h} \\&= \lim \langle   u_n(N)g,A^*h   \rangle \\&= \lim \langle   Au_n(N)g,h   \rangle \\&= \lim \langle   u_n(N)Ag,h   \rangle \\&= \langle   E(G)Ag,h   \rangle.\end{aligned}
$$

So Ω contains every open set and, hence, it must be the collection of Borel sets. The converse is left to the reader.

The unique spectral measure E obtained in the Spectral Theorem is called the spectral measure for N. An abbreviation for the Spectral Theorem is to say, "Let $N = \int \lambda   d E ( \lambda )$ be the spectral decomposition of $N . ^ { \ast }$ If $\phi$ is a bounded Borel function on $\sigma ( N )$ , define $\phi ( N )$ by

$$
\phi ( N ) \equiv \int \phi   d E ,
$$

where E is the spectral measure for $N .$

2.3. Theorem. If N is a normal operator on $\mathcal { H }$ with spectral measure E and $B ( \sigma ( N ) )$ is the $C ^ { * } - a l g e b r a$ of bounded Borel functions on $\sigma ( N )$ , then the map

$$
\phi { \mapsto } \phi ( N )
$$

is a representation of the $C ^ { * } { - a l g e b r a }$ $B ( \sigma ( N ) )$ . If $\{ \phi _ { i } \}$ is a net in $B ( \sigma ( N ) )$ such that $\int   \phi _ { i }   d \mu   \to   0$ for every $\mu$ in $M ( \sigma ( N ) )$ , then $\phi _ { i } ( N )   \rightarrow   0 \; \mathrm { ( W O T ) }$ . This map is unique in the sense that if $\tau \colon B ( \sigma ( N ) ) \to { \mathcal { B } } ( { \mathcal { H } } )$ is a representation such that $\tau ( z ) = N$ and $\tau ( \phi _ { i } ) \rightarrow 0   ( \mathrm { W O T } )$ whenever $\{ \phi _ { i } \}$ is a bounded net in $B ( \sigma ( N ) )$ such that $\int   \phi _ { i }   d \mu   \rightarrow   0   f o r$ every µ in $M ( \sigma ( N ) )$ , then $\tau ( \phi ) = \phi ( N )$ for all φ in $B ( \sigma ( N ) )$

PROOF. The fact that $\phi { \mapsto } \phi ( N )$ is a representation is a consequence of Proposition 1.12. If $\{ \phi _ { i } \}$ is as in the statement, then the fact that $E _ { g , h }   \in   M ( \sigma ( N ) )$ implies that $\phi _ { i } ( N )   \rightarrow   0 \; \mathrm { ( W O T ) }$

To prove uniqueness, let $\tau \colon B ( \sigma ( N ) ) \to { \mathcal { B } } ( { \mathcal { H } } )$ be a representation with the appropriate properties. Then $\tau ( u ) = u ( N )$ if $u   \in   \mathbb { C } ( \sigma ( N ) )$ by the uniqueness of the functional calculus for normal elements of a C\*-algebra (VIII.2.6). If $\phi   \in   \boldsymbol { B } ( \sigma ( N ) )$ , then Proposition V.4.1 implies that there is a net $\left\{ u _ { i } \right\}$ in $C ( \sigma ( N ) )$ such that $\| \boldsymbol { u } _ { i } \| \leqslant \| \boldsymbol { \phi } \|$ for all $\pmb { u } _ { i }$ and $\int   u _ { i }   d \mu \to \int   \phi   d \mu$ for every $\mu$ in $M ( \sigma ( N ) )$ Thus $u _ { i } ( N )   \rightarrow   \phi ( N ) \; \mathrm { ( W O T ) }$ . But $\tau ( \phi ) = \mathrm { W O T } - \lim \tau ( u _ { i } ) = \mathrm { W O T } - \lim u _ { i } ( N ) ;$ therefore $\tau ( \phi ) = \phi ( N )$

It is worthwhile to rewrite (1.11) as

## 2.4

$$
\langle \phi ( N ) g , h \rangle = \int \phi   d E _ { g , h }
$$

for $\phi$ in $B ( \sigma ( N ) )$ and $g , h$ in $\mathcal { H } .$ If $\phi   \in   B ( \mathbb { C } )$ , then the restriction of $\phi$ to $\sigma ( N )$ belongs to $B ( \sigma ( N ) )$ . Since the support of each measure $E _ { \pmb { g } , \pmb { h } }$ is contained in $\sigma ( N ) ,$ (2.4) holds for every bounded Borel function $\phi$ on $\mathbf { \Phi }$ This has certain technical advantages that will become apparent when we begin to apply (2.4).

Proposition 2.3 thus extends the functional calculus for normal operators. This functional calculus or, equivalently, the Spectral Theorem, will be exploited in this chapter. But right now we look at some examples.

2.5. Example. If $\mu$ is a regular Borel measure on C with compact support $K ,$ define $N _ { \mu }$ on $L ^ { 2 } ( \mu )$ by $N _ { \mu } f = z f$ for each $f$ in $L ^ { 2 } ( \mu )$ . It is easy to check that $N _ { \mu } ^ { * } f = \bar { z } f ,$ and, hence, $N _ { \mu }$ is normal.

(a) $\sigma ( N _ { \mu } ) = K = \mathrm { s u p p o r t }$ of µ. (Exercise.)

(b) If, for a bounded Borel function $\phi ,$ we define $M _ { \phi }$ on $L ^ { 2 } ( \mu )$ by $M _ { \phi } f = \phi f ,$ then $\phi ( N _ { \mu } ) = M _ { \phi }$

Indeed, this is an easy application of the uniqueness part of (2.3).

(c) If E is the spectral measure for $N _ { \mu } ,$ then $E ( \Delta ) = M _ { \chi _ { \Delta } }$

Just note that $E ( \Delta ) = \chi _ { \Delta } ( N _ { \mu } ) .$

2.6. Example. Let $( X , \Omega , \mu )$ be any σ-finite measure space and put $\mathcal { H } =$ $L ^ { 2 } ( X , \Omega , \mu )$ . For $\phi$ in $L ^ { \infty } ( \mu ) \equiv L ^ { \infty } ( X , \Omega , \mu ) ,$ define $M _ { \phi }$ on $\mathcal { H }$ by $M _ { \phi } f = \phi f .$

(a) $M _ { \phi }$ is normal and $M _ { \phi } ^ { * } = M _ { \bar { \phi } } \left( \mathrm { I I } . 2 . 8 \right)$

(b) $\phi   \mapsto   M _ { \phi }$ is a representation of $L ^ { \infty } ( \mu ) \: ( \mathrm { V I I I } . 5 . 4 )$

(c) If $\phi { \in } L ^ { \infty } ( \mu ) , \: \|   \phi   \| _ { \infty } = \|   M _ { \phi }   \| \mathrm { ~ ( I I . } 1 . 5 ) .$

(d) Define the essential range of $\phi$ by

$$
\operatorname { e s s - r a n } ( \phi ) \equiv \cap \{ \operatorname { c l } ( \phi ( \Delta ) ) \colon \Delta   \in   \Omega { \mathrm { ~ a n d ~ } } \mu ( X \setminus \Delta ) = 0 \} .
$$

Then $\sigma ( M _ { \phi } ) = \mathrm { e s s - r a n } ( \phi )$ . (This appears as Exercise VII.3.3, but a proof is given here.)

First assume that $\lambda \notin \mathrm{ess-ran}(\phi)$ . So there is a set ∆ in Ω with $\mu ( X \backslash \Delta ) = 0$ and λ not in cl $( \phi ( \Delta ) ) ;$ thus there is a $\delta   >   0$ with $| \phi ( x ) - \lambda | \geqslant \delta$ for all x in ∆. If $\psi = ( \phi - \lambda ) ^ { - 1 } , \psi \in L ^ { \infty } ( \mu )$ and $M _ { \psi } = ( M _ { \phi } - \lambda ) ^ { - 1 }$

Conversely, assume $\lambda \in \mathrm{ess-ran}(\phi)$ .It follows that for every integer n there is a set $\Delta _ { n }$ in Ω such that $0 < \mu ( \Delta _ { n } ) < \infty$ and $| \phi ( x ) - \lambda | < 1 / n$ for all x in $\Delta _ { n } .$ $\mathrm{Put} f_{n} = (\mu(\Delta_{n}))^{-1/2} \chi_{\Delta_{n}}; \mathrm{so} f_{n} \in L^{2}(\mu)$ and $\| f _ { n } \| _ { 2 } = 1$ . However, $\| ( M _ { \phi } - \lambda ) f _ { n } \| _ { 2 } ^ { 2 } =$ $\left( \mu ( \Delta _ { n } ) \right) ^ { - 1 } \int _ { \Delta _ { n } } | \phi - \lambda | ^ { 2 } \hat { d } \mu \leqslant 1 / n ^ { 2 }$ , showing that $\lambda { \in } \sigma _ { a p } ( M _ { \phi } )$

(e) If E is the spectral measure for $M _ { \phi }$ [so E is defined on the Borel subsets of $\sigma ( M _ { \phi } ) = \mathrm { e s s - r a n } ( \phi ) \subseteq \mathbb { C } [$ , then for every Borel subset $\Delta$ of $\sigma ( M _ { \phi } )$ 2 $E ( \Delta ) = M _ { \chi _ { \phi ^ { - 1 } ( \Delta ) } } .$

2.7. Proposition. If for $k \geqslant 1 , N _ { k }$ is a normal operator on $\mathcal { H } _ { k }$ with $\operatorname* { s u p } _ { \boldsymbol { k } } \| \boldsymbol { N } _ { \boldsymbol { k } } \| < \infty , \; E _ { \boldsymbol { k } }$ is the spectral measure for $N _ { k }$ , and if $N = \oplus _ { k = 1 } ^ { \infty } N _ { k }$ on $\mathcal { H } = \oplus _ { k = 1 } ^ { \infty } \mathcal { H } _ { k }$ , then:

(a) $\sigma ( N ) = \mathrm { c l } \left[ \bigcup _ { k = 1 } ^ { \infty } \sigma ( N _ { k } ) \right] ;$

(b) if E is the spectral measure for N, $E ( \Delta ) = \oplus _ { k = 1 } ^ { \infty } E _ { k } ( \Delta \cap \sigma ( N _ { k } ) )$ for every Borel subset ∆ of $\sigma ( N )$

PROOF. Exercise.

A historical account of the spectral theorem is an enormous undertaking