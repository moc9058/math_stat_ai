20. Let $1 \leqslant p \leqslant \infty$ and let $( X , \Omega , \mu )$ be a σ-finite measure space. If $\scriptstyle { \boldsymbol { A } } \in { \mathcal { B } } _ { 0 } ( L ^ { p } ( \mu ) )$ , show that there is a sequence $\{ A _ { n } \}$ of finite-rank operators such that $\| A_n - A \| \to 0$ (Hint: Use Exercise 19.)

21. Let X be compact and let $\mathcal { U }$ be the collection of all pairs $( C , F )$ where $C = \{ U _ { 1 } , \ldots , U _ { n } \}$ is a finite open cover of X and $F = \{ x _ { 1 } , \ldots , x _ { n } \} \subseteq X$ such that $x _ { j } { \in } U _ { j }$ for $1 \leqslant j \leqslant n.  If  \left( C_{1}, F_{1} \right)$ and $(C_{2},F_{2}) \in \mathcal{U}$ , define $( \boldsymbol { C } _ { 1 } , \boldsymbol { F } _ { 1 } ) \leqslant ( \boldsymbol { C } _ { 2 } , \boldsymbol { F } _ { 2 } )$ to mean: (a) $C _ { 2 }$ is a refinement of $C _ { 1 } ;$ that is, each member of $C _ { 2 }$ is contained in some member of $C_{1}. (b) F_{1} \subseteq F_{2}. \mathrm{If} \alpha = (C, F) \in \mathcal{U}$ let $\{ \phi _ { 1 } , \ldots , \phi _ { n } \}$ be a partition of unity subordinate to C. If $F = \{ x _ { 1 } , \ldots , x _ { n } \}$ , define $T _ { \alpha } : C ( X ) \to C ( X )$ by

$$
(T_{\alpha}f)(x) = \sum_{j = 1}^{n} f(x_j) \phi_j(x).
$$

Then: (a) $T _ { \alpha } \in \mathcal { B } _ { 0 0 } ( C ( X ) ) ;$ (b) $T _ { \alpha } \parallel = 1 ; \mathrm { ( c ) } \; ( \mathcal { U } ,   \leqslant )$ is a directed set and $\{ T _ { \alpha } : \alpha \in \mathcal { U } \}$ is a net; (d) $\| T _ { \alpha } f - f \| \to 0$ for each f. Now apply Exercise 19 to obtain a new proof of Theorem 3.11.

## §4. Invariant Subspaces

4.1. Definition. If $\mathcal { X }$ is a Banach space and $T   \in   \mathcal { B } ( \mathcal { X } )$ , an invariant subspace for T is a closed linear subspace $\mathcal { M }$ of $\mathcal { X }$ such that $T x { \in } { \mathcal { M } }$ whenever x∈.M $\mathcal { M }$ is nontrivial if $\mathcal { M } \neq ( 0 )$ or $\mathcal { X }$ Lat T = the collection of all invariant subspaces for T. If $\mathcal { A } \subseteq \mathcal { B } ( \mathcal { X } )$ , then Lat $\mathcal { A } = \bigcap \{ \operatorname { L a t } T : T \in \mathcal { A } \}$

This generalizes the corresponding concept of invariant subspace for an operator on Hilbert space (II.3.5). Note that the idea of a reducing subspace for an operator on a Hilbert space has no generalization to Banach spaces since there is no concept of an orthogonal complement in Banach spaces.

## 4.2. Proposition.

(a) If $\mathcal { M } _ { 1 } , \mathcal { M } _ { 2 } { \in } \operatorname { L a t } T ,$ then $\mathcal { M } _ { 1 } \lor \mathcal { M } _ { 2 } \equiv \mathrm { c l } ( \mathcal { M } _ { 1 } + \mathcal { M } _ { 2 } ) \in \mathrm { L a t } T$ and $\mathcal { M } _ { 1 } \wedge$ $\mathcal { M } _ { 2 } \equiv \mathcal { M } _ { 1 } \cap \mathcal { M } _ { 2 } \in \mathrm { L a t } T .$

(b) $I f \left\{ \mathcal { M } _ { i } : i \in I \right\} \subseteq \mathrm { L a t } T ,$ then $\vee \left\{ { \mathcal { M } } _ { i } ; i { \in } I \right\}$ , the closed linear span of $\bigcup _ { i } \mathcal { M } _ { i }$ and $\wedge \left\{ \mathcal { M } _ { i } \colon i { \in } I \right\} \equiv \bigcap _ { i } \mathcal { M } _ { i }$ belong to Lat T.

The proof of this proposition is left as an exercise. The proposition however, does justify the use of the symbol $\text{" }  L   a   t  \text{" }$ to denote the collection of invariant subspaces. With the operations v and ∧, Lat $T$ is a lattice (a) that is complete (b). Moreover, Lat $T$ has a largest element, $\mathcal { X } .$ and a smallest element, (0)

The main question is: does Lat T have any elements besides (0) and $\mathcal { X } ?$ In other words, does $T$ have a nontrivial invariant subspace? C.J. Read [1984] showed the existence of a Banach space and an operator on the Banach space having no non-trivial invariant subspaces. This was preceded by some work of P Enflo (not published, but circulated) which did the same thing. Later B Beauzamy [1985] sorted out $\mathrm { E n f l o ` s }$ ideas and gave an exposition and simplification of Enflo's construction. Enflo's work eventually appeared in Enflo [1987]. Read [1986] gave a self contained exposition showing that there is a bounded operator on $l ^ { 1 }$ having no nontrivial invariant subspace. This deep work does not completely settle the matter. Which Banach spaces $\mathcal { X }$ have the property that there is a bounded operator on X with no nontrivial invariant subspaces? If $\mathcal { X }$ is reflexive, is Lat $T$ nontrivial for every $T$ in ${ \mathcal { B } } ( { \mathcal { X } } ) ?$ The question is unanswered even if $\mathcal { X }$ is a Hilbert space. However, for certain specific operators and classes of operators it has been shown that the lattice of invariant subspaces is not trivial. In this section it will be shown that any compact operator has a nontrivial invariant subspace. This will be obtained as a corollary of a more general result of V. Lomonosov. But first some examples.

4.3. Example. If $\mathcal { X }$ is a finite dimensional space over C and $T   \in   \mathcal { B } ( \mathcal { X } )$ , then Lat $T$ is not trivial. In fact, let $\mathcal { X } = \mathbb { C } ^ { d }$ and let $T   =   \mathbf { a }$ matrix. Then $p ( z ) = \operatorname* { d e t } ( T - z I )$ is a polynomial of degree $d .$ Hence it has a zero, say $\alpha .$ If det $( T - \alpha I ) = 0 ,$ then $( T - \alpha I )$ is not invertible. But in finite dimensional spaces this means that $T   -   \alpha I$ is not injective. Thus ker $( T - \alpha I ) \neq ( 0 )$ . Let $\mathcal { M } \leqslant \ker ( T - \alpha I )$ such that $\mathcal { M } \neq ( 0 )$ $\operatorname { I f } x \in { \mathcal { M } } ,$ then $Tx = \alpha x \in \mathcal{M}, \mathrm{so} \mathcal{M} \in \mathrm{Lat} T.$

4.4. Example. If $\boldsymbol{T} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ on $\mathbb { R } ^ { 2 }$ , then Lat T is trivial. Indeed, if Lat T is not trivial, there is a one-dimensional space $\mathcal { M }$ in Lat T. Let $\mathcal { M } = \{ \alpha e \colon \alpha \in \mathbb { R } \}$ . Since M ∈Lat T, $T e = \lambda e$ for some λ in R. Hence $T^{2}e = T(Te) = \lambda Te = \lambda^{2}e$ . But $T ^ { 2 } = - I , \mathrm { s o } - e = \lambda ^ { 2 } e$ and it must be that $\lambda ^ { 2 } = - 1 \mathrm { i f } e \neq 0 .$ But this cannot be if λ is real.

If $d \geqslant 3 .$ , however, and $T { \in } { \mathcal { B } } ( \mathbb { R } ^ { d } )$ , then Lat T is not trivial (Exercise 6).

4.5. Example. If $V : L ^ { 2 } [ 0 , 1 ] \to L ^ { 2 } [ 0 , 1 ]$ is the Volterra operator, $V f ( x )   =$ $\textstyle \int _ { 0 } ^ { x } f ( t ) d t ,$ and $0 \leqslant \alpha \leqslant 1$ , put $\mathcal { M } _ { \alpha } = \left\{ f \in L ^ { 2 } [ 0 , 1 ] : f ( t ) = 0 \right\}$ for $0 \leqslant t \leqslant \alpha \}$ . Then $\mathcal { M } _ { \alpha } { \in } \operatorname { L a t } V .$ Moreover, it can be shown Lat $V = \left\{ \mathcal{M}_{\alpha} : 0 \leqslant \alpha \leqslant 1 \right\}$ (See Donoghue [1957], and Radjavi and Rosenthal [1973], p. 68.)

4.6. Example. If $S \colon l ^ { p }   \to   l ^ { p }$ is defined by $S(\alpha_{1},\alpha_{2},\ldots)=(0,\alpha_{1},\alpha_{2},\ldots)$ and $\mathcal { M } _ { n } = \{ x \in l ^ { p } : x ( k ) = 0$ for $1 \leqslant k \leqslant n \}$ , then $\mathcal { M } _ { n } { \in } \operatorname { L a t } S$

4.7. Example. Let $( X , \Omega , \mu )$ be a $\sigma - \mathrm { f i n i t e }$ measure space and for $\phi$ in $L ^ { \infty } ( \mu )$ let $M _ { \phi }$ denote the multiplication operator on $L ^ { p } ( \mu ) , \; 1 \leqslant p \leqslant \infty$ . If $\Delta { \in } \Omega$ let $\mathcal { M } _ { \Delta } = \left\{ f \in L ^ { p } ( \mu ) : f = 0 \mathrm { a . e . } \right\}$ [µ]off $\Delta \}$ . Then for each $\phi$ in $L ^ { \infty } ( \mu )$ $\mathcal { M } _ { \Delta } { \in } \operatorname { L a t } M _ { \phi }$

It is a difficult if not impossible task to determine all the invariant subspaces of a specific operator. The Volterra operator and the shift operator are examples where all the invariant subspaces have been determined. But there are multiplication operators $M _ { \phi }$ for which there is no characterization of Lat $M _ { \phi }$ as well as some $M _ { \phi }$ for which such a characterization has been achieved. One such example follows: let $\mu = \mathbf { L e b e s g u e }$ area measure on D and let $( A f ) ( z ) = z f ( z )$ for f in $L ^ { 2 } ( \mu )$ . There is no known characterization of Lat A.

It is necessary at this point to return to the geometry of Banach spaces to prove the following classical theorem, which appeared as Exercise V.13.2.

4.8. Mazur's Theorem. If X is a Banach space and K is a compact subset of $\mathcal { X }$ , then ${ \overline { { \mathbf { c o } } } } ( K )$ is compact.

ProoF. It suffices to show that co(K) is totally bounded. Let $\varepsilon   >   0$ and choose $x _ { 1 } , \ldots , x _ { n }$ in K such that $K \in \bigcup_{j = 1}^{n} B(x_j; \varepsilon / 4)$ . Put $C = \mathrm{co} \left\{ x_1, \ldots, x_n \right\}$ It is easy to see that C is compact (Exercise V.7.8). Hence there are vectors $y _ { 1 } , \ldots , y _ { m }$ in C such that $C \subseteq \bigcup_{i = 1}^{m} B(y_i; \varepsilon / 4)$ . If $w { \in } { \overline { { \mathsf { c o } } } } ( K )$ , there is a z in co(K) with $\parallel w - z \parallel < \varepsilon / 4$ . Thus $\begin{array} { r } { z = \sum _ { p = 1 } ^ { l } \alpha _ { p } k _ { p } , } \end{array}$ where $k _ { p } \in K ,   \alpha _ { p } \geqslant 0 ,$ and $\sum \alpha _ { p } = 1$ Now for each $k _ { p }$ there is an $x _ { j ( p ) }$ with $\| k _ { p } - x _ { j ( p ) } \| < \varepsilon / 4$ Therefore

$$
\begin{aligned}\left\| z - \sum_{p = 1}^{l} \alpha_{p} x_{j(p)} \right\| &= \left\| \sum_{p = 1}^{l} \alpha_{p} (k_{p} - x_{j(p)}) \right\| \\& \leqslant \sum_{p = 1}^{l} \alpha_{p} \|   k_{p} - x_{j(p)} \| \\& < \varepsilon / 4.\end{aligned}
$$

But $\scriptstyle \sum _ { p } \alpha _ { p } x _ { j ( p ) } \in C$ so there is a $y _ { i }$ with $\begin{array} { r } { \| \sum _ { p } \alpha _ { p } x _ { j ( p ) } - y _ { i } \| < \varepsilon / 4 . } \end{array}$ The triangle inequality now shows that co $(K) \subseteq \bigcup_{i = 1}^{m} B(y_i; \varepsilon)$ and so co(K) is totally bounded. ■

The next result is from Lomonosov [1973]. When it appeared it caused great excitement, both for the strength of its conclusion and for the simplicity of its proof. The proof uses Schauder's Fixed-Point Theorem (V.9.5).

4.9. Lomonosov's Lemma. If  is a subalgebra of $\mathcal { B } ( \mathcal { X } )$ such that $1 \in \mathcal { A }$ and Lat $\mathcal { A } = \{ ( 0 ) , \mathcal { X } \}$ and if K is a nonzero compact operator on $\mathcal { X } ,$ , then there is an A in $\varkappa$ such that ker $( A K - 1 ) \neq ( 0 )$

PRoOF. It may be assumed that $\| K \| = 1$ . Fix $x _ { 0 }$ in $\mathcal { X }$ such that $\| K x _ { 0 } \| > 1$ and put $S = \left\{ x \in \mathcal{X} : \| x - x_0 \| \leq 1 \right\}$ . It is easy to check that

## 4.10

$$
0 \notin S \mathrm { a n d } 0 \notin \operatorname { c l } K ( S ) .
$$

Now if $x { \in } { \mathcal { X } }$ and $x \neq 0 ,$ cl $\{ T x \colon T { \in } { \mathcal { A } } \}$ is an invariant subspace for $\varkappa$ (because $\rtimes$ is an algebra) that contains the nonzero vector x (because $1 \in \mathcal { A } )$ By hypothesis, cl $\{ T x \colon T { \in } { \mathcal { A } } \} = { \mathcal { X } }$ . By (4.10) this says that for every y in cl $K ( S )$ there is a $T$ in $\varkappa$ with $\|   T y - x _ { 0 }   \| < 1$ . Equivalently,

$$
\operatorname { c l } K ( S ) \subseteq \bigcup _ { T \in \mathcal { A } } \left\{ y : \| T y - x _ { 0 } \| < 1 \right\} .
$$

Because cl $K ( S )$ is compact, there are $T _ { 1 } , \ldots , T _ { n }$ in $\varkappa$ such that

$$
\mathrm{cl} K(S) \subseteq \bigcup_{j=1}^{n} \left\{ y: \| T_j y - x_0 \| < 1 \right\}.\tag{4.11}
$$

For y in cl $K ( S )$ and $1 \leqslant j \leqslant n ,$ let $a _ { j } ( y ) = \max \left\{ 0 , 1 - \left\| T _ { j } y - x _ { 0 } \right\| \right\}$ . By (4.11), $\begin{array} { r } { \sum _ { j = 1 } ^ { n } a _ { j } ( y ) > 0 } \end{array}$ for all y in cl $K ( S )$ Define $b _ { j } ;$ cl $K ( S )   \to   \mathbb { R } ^ { 1 }$ by

$$
b _ { j } ( y ) = \frac { a _ { j } ( y ) } { \sum _ { i \; = \; 1 } ^ { n } a _ { i } ( y ) } ,
$$

and define $\psi \colon S \to { \mathcal { X } }$ by

$$
\psi ( x ) = \sum _ { j = 1 } ^ { n } b _ { j } ( K x ) T _ { j } K x .
$$

It is easy to see that $a _ { j } ;$ cl $K ( S )   \to   [ 0 , 1 ]$ is a continuous function. Hence $b _ { j }$ and $\psi$ are continuous.

If x∈S, then $K x { \in } K ( S )$ If $b _ { j } ( K x )   >   0 ,$ then $a _ { j } ( K x )   >   0$ and so $\|   T _ { j } K x -   x _ { 0 }   \| < 1$ . That is, $T _ { j } K { \boldsymbol { x } } { \in } { \mathcal { S } }$ whenever $b _ { j } ( K x )   >   0$ Since S is a convex set and $\scriptstyle \sum _ { j = 1 } ^ { n } b _ { j } ( K x ) = 1$ for x in S,

$$
\psi ( S ) \subseteq S .
$$

Note that $T _ { j } K   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ for each j so that $\bigcup _ { j = 1 } ^ { n } T _ { j } K ( S )$ has compact closure. By Mazur's Theorem, co $\left( \bigcup_{j = 1}^{n} T_{j} K(S) \right)$ is compact. But this convex set contains $\psi ( S )$ so that cl $\psi ( S )$ is compact. This is, $\psi$ is a compact map. By the Schauder Fixed-Point Theorem, there is a vector $x _ { 1 }$ in S such that $\psi ( x _ { 1 } )   =   x _ { 1 }$

Let $\beta _ { j }   =   b _ { j } ( K x _ { 1 } )$ and put $\begin{array} { r } { A = \sum _ { j = 1 } ^ { n } \beta _ { i } T _ { j } } \end{array}$ .So $A \in \mathcal { A }$ and $A K x _ { 1 } = \psi ( x _ { 1 } ) = x _ { 1 }$ Since $x_{1} \neq 0 (\mathrm{Why?})$ , ker $( A K - 1 ) \neq 0 .$ ■

4.12. Definition. If $T   \in   \mathcal { B } ( \mathcal { X } )$ , then a hyperinvariant subspace for T is a subspace $\mathcal { M }$ of X such that $\mathcal { A } \mathcal { M } \subseteq \mathcal { M }$ for every operator A in the commutant of $T ,$ $\{ T \} ^ { \prime }$ ; that is, $A \mathcal { M } \subseteq \mathcal { M }$ whenever $A T = T A$

Note that every hyperinvariant subspace for T is invariant.

4.13. Lomonosov's Theorem. If X is a Banach space over C, $T   \in   \mathcal { B } ( \mathcal { X } )$ , T is not a multiple of the identity, and $T K = K T$ for some nonzero compact operator K, then T has a nontrivial hyperinvariant subspace.

PROOF. Let ${ \mathcal { A } } = \{ T \} ^ { \prime }$ . We want to show that Lat $\mathcal { A } \neq \{ ( 0 ) , \mathcal { X } \}$ . If this is not the case, then Lomonosov's Lemma implies that there is an operator A in $\mathcal { A }$ such that $\mathcal { N } = \ker ( A K - 1 ) \neq ( 0 )$ . But ${ \mathcal { N } } { \in } \mathbf { L a t } ( A K )$ and $A K | \mathcal { N }$ is the identity operator. Since $A K \in \mathcal { B } _ { 0 } ( \mathcal { X } ) , A K \mid \mathcal { N } \in \mathcal { B } _ { 0 } ( \mathcal { N } )$ . Thus dim $\mathcal { N } < \infty$ Since $A K { \in } { \mathcal { A } } = \{ T \} ^ { \prime }$ , for any x in N, $AK(Tx)=T(AKx)=Tx;$ hence $T \mathcal { N } \subseteq \mathcal { N }$ . But dim $\mathcal { N } < \infty$ so that $T | \mathcal { N }$ must have an eigenvalue λ. Thus ker $( T - \lambda ) = \mathcal { M } \neq ( 0 )$ . But $\mathcal { M } \neq \mathcal { X }$ since T is not a multiple of the identity. It is easy to check that M is hyperinvariant for $T .$

A proof of a slightly weaker version of Lomonosov's Theorem that avoids Schauder's Fixed Point Theorem can be found in Michaels [1977].

4.14. Corollary. (Aronszajn-Smith [1954].) If $K   \in   \mathcal { B } _ { 0 } ( \mathcal { X } ) .$ , then Lat K is nontrivial.

The next result appeared in Bernstein and Robinson [1966], where it is proved using nonstandard analysis. Halmos [1966] gave a proof using standard analysis. Now it is an easy consequence of Lomonosov's Theorem.

4.15. Corollary. $I f \mathcal { X }$ is infinite dimensional, $A   \in   \mathcal { B } ( \mathcal { X } ) ,$ , and there is a polynomial in one variable, p, such that $p ( A ) \in \mathcal { B } _ { 0 } ( \mathcal { X } )$ , then Lat A is nontrivial.

PROOF. If $p(A) \neq 0,$ then Lomonosov's Theorem applies. If $p(A) = 0,$ let $p ( z ) =$ $\alpha _ { 0 } + \alpha _ { 1 } z + \cdots + \alpha _ { n } z ^ { n } , \alpha _ { n } \neq 0 . \mathrm { F o r } x \neq 0 ,$ , let $\mathcal { M } = \vee \left\{ x , A x , \ldots , A ^ { n - 1 } x \right\}$ . Since $A^{n} = - \alpha_{n}^{- 1}\left[ \alpha_{0} + \alpha_{1}A + \cdots + \alpha_{n - 1}A^{n - 1} \right]$ , M ∈Lat A. Since $x \in \mathcal { M } _ { 2 }$ $\mathcal { M } \neq ( 0 ) ;$ since dim $\mathcal { M } < \infty , \mathcal { M } \neq \mathcal { X } .$ 國

4.16. Corollary. If $K _ { 1 } ,   K _ { 2 }   \in   \mathcal { B } _ { 0 } ( \mathcal { X } )$ and $K _ { 1 } K _ { 2 } = K _ { 2 } K _ { 1 }$ , then $K _ { 1 }$ and $K _ { z }$ have a common nontrivial invariant subspace.

## EXERCISES

1. Let A, B, $T   \in   \mathcal { B } ( \mathcal { X } )$ such that $T A = B T$ . Show that graph (T)∈Lat(A ⊕ B).

2. Prove that M ∈Lat T if and only if $\mathcal { M } ^ { \perp } { \in } \mathrm { L a t } \; T ^ { * }$ . What does the map $\mathcal { M } \mapsto \mathcal { M } ^ { \perp }$ of Lat T into Lat $T ^ { * }$ do to the lattice operations?

3. Let $\{ e _ { 1 } , e _ { 2 } , e _ { 3 } \}$ be the usual basis for $\mathbb { F } ^ { 3 }$ and let $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } { \in } \mathbb { F }$ Define $T \colon \mathbb { F } ^ { 3 }   \to   \mathbb { F } ^ { 3 }$ by $T e _ { j } = \alpha _ { j } e _ { j } , \; 1 \leqslant j \leqslant 3 .$ If $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 }$ are all distinct, show that $\mathcal { M }   \in   \mathrm { L a t }   T$ if and only if $\mathcal { M } = \nabla E ,$ where $\boldsymbol { E } \in \{ e _ { 1 } , e _ { 2 } , e _ { 3 } \}$ . (b) If $\alpha _ { 1 } = \alpha _ { 2 } \neq \alpha _ { 3 }$ , show that M∈Lat T if and only if $\mathcal { M } = \mathcal { N } + \mathcal { L }$ , where $\mathcal { N } \leqslant \vee \left\{ e _ { 1 } , e _ { 2 } \right\}$ and $\mathcal { L } \leqslant \{ \alpha e _ { 3 } : \alpha \in \mathbb { F } \}$

4. Generalize Exercise 3 by characterizing Lat T, where T is defined by $T e _ { j }   =   \alpha _ { j } e _ { j } ,$ $1 \leqslant j \leqslant d ,$ for any choice of scalars $\alpha _ { 1 } , \ldots , \alpha _ { d }$ and where $\{ e _ { 1 } , \ldots , e _ { d } \}$ is the usual basis for $\mathbf { F } ^ { d }$

5. Let $\{ e _ { 1 } , \ldots , e _ { d } \}$ be the usual basis for $\mathbf { F } ^ { d } ,$ let $\{ \alpha _ { 1 } , \ldots , \alpha _ { d - 1 } \} \subseteq \mathbb { F }$ with no $\alpha _ { j }   =   0 .$ If $T e _ { j }   =   \alpha _ { j } e _ { j   +   1 }$ for $1 \leqslant j \leqslant d - 1$ and $T e _ { d } = 0 ,$ find Lat T.

6. If $T   \in   \mathcal { B } ( \mathbb { R } ^ { d } )$ and $d \geqslant 3 .$ , show that T has a nontrivial subspace

7. Show that if $T   \in   \mathcal { B } ( \mathcal { X } )$ and $\mathcal { X }$ is not separable, then T has a nontrivial invariant subspace.

8. Give an example of an invertible operator T on a Banach space $\mathcal { X }$ and an invariant subspace M for T such that M is not invariant for $T ^ { - 1 }$

9. Let X be a Banach space over C, let $K { \in } { \mathcal { B } } _ { 0 } ( { \mathcal { X } } )$ and show that if $\mathcal { C }$ is a maximal chain in Lat K, then $\mathcal { C }$ is a maximal chain in the lattice of all subspaces of $\mathcal { X }$

## §5. Weakly Compact Operators

5.1. Definition. If X and $\mathcal { Y }$ are Banach spaces, an operator T in $\mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ is weakly compact if the closure of T(ball X) is weakly compact.

Weakly compact operators are generalizations of compact operators, but the hypothesis is not sufficiently strong to yield good information about their structure.

Recall that in a reflexive Banach space the weak closure of any bounded set is weakly compact. Also, a bounded operator T: $\mathcal { X }   \rightarrow   \mathcal { Y }$ is continuous if both $\mathcal { X }$ and @ have their weak topologies (1.1). With these facts in mind, the proof of the next result becomes an easy exercise for the reader.

## 5.2. Proposition.

(a) If either $\mathcal { X }$ or $\mathcal { G }$ is reflexive, then every operator in $\mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ is weakly compact.

(b) If T: $\mathcal { X }   \rightarrow   \mathcal { Y }$ is weakly compact and $A   \in   \mathcal { B } ( \mathcal { Y } , \mathcal { X } )$ , then AT is weakly compact.

(c) If $T { \colon \thinspace } { \mathcal { X } } { \to } { \mathcal { Y } }$ is weakly compact and $B \in \mathcal { B } ( \mathcal { X } , \mathcal { X } )$ ,then TB is weakly compact.

This proposition shows that assuming that an operator is weakly compact is not that strong an assumption. For example, if ¿ is reflexive, every operator in $\mathcal { B } ( \mathcal { X } )$ is weakly compact. In particular, every operator on a Hilbert space is weakly compact. So any theorem about weakly compact operators is a theorem about all operators on a reflexive space.

In fact, there is a degree of validity for the converse of this statement. In a certain sense, theorems about operators on reflexive spaces are also theorems about weakly compact operators. The precise meaning of this statement is the content of Theorem 5.4 below. But before we begin to prove this, a lemma is needed.

Let @ be a Banach space and let W be a bounded convex balanced subset of Y. For $n > 1$ put $U _ { n } = 2 ^ { n } W + 2 ^ { - n }$ int[ball @]. Let $p _ { n } = \mathrm { t h e }$ gauge of $U _ { n }$ (IV.1.14). Because $U _ { n }   \supseteq   2 ^ { - n }$ int[ball ], it is easy to check that $p _ { n }$ is a norm on Y. In fact, $p _ { n }$ and ·∥ are equivalent norms. To see this note that if $\| y \| < 1$ , then $2 ^ { - n } y { \in } U _ { n }$ so that $p _ { n } ( y ) < 2 ^ { n }$ . Hence $p_{n}(y) \leqslant 2^{n}\|y\|$ . Also, because W is bounded, $U _ { n }$ must be bounded; let $M > \operatorname* { s u p } \{ \| y \| \colon y \in U _ { n } \}$ . So if $p _ { \pmb { n } } ( y ) < 1$ $\|   y   \| < M$ Thus $\|   y   \| \leqslant M p _ { n } ( y )$ ,and∥·∥and $p _ { n }$ are equivalent norms.

5.3. Lemma. For a Banach space Y let $W , U _ { n } ,$ and $p _ { n }$ be as above. Let $\mathcal { R } = t h e$ set of all y in Y such that $\| y \| \equiv \left[ \sum_{n = 1}^{\infty} p_{n}(y)^{2} \right]^{1/2} < \infty$ . Then

(a) $W \subseteq \{ y : \| y \| < 1 \}$ 2

(b) $( \mathcal { R } , \left\| \cdot \right\| )$ is a Banach space and the inclusion map $A \colon { \mathcal { R } }   \to   { \mathcal { Y } }$ is continuous;

(c) $A ^ { * * } \overline { { : } } \mathcal { R } ^ { * * }   \rightarrow   \overline { { \mathcal { Y } ^ { * * } } }$ is injective and $(A^{*} *)^{-1}(\mathcal{Y}) = \mathcal{R};$

(d) R is reflexive if and only if cl W is weakly compact.

PROOF. (a) If $w   \in   W ,$ then $2 ^ { n } w { \in } U _ { n }$ Hence $1 > p _ { n } ( 2 ^ { n } w ) = 2 ^ { n } p _ { n } ( w ) , \mathrm { s o } p _ { n } ( w ) < 2 ^ { - n }$ Thus $\| w \| ^ { 2 } < \sum _ { n } ( 2 ^ { - n } ) ^ { 2 } < 1$

(b) Let $\mathcal { G } _ { n } = \mathcal { G }$ with the norm $p _ { n }$ and put $\mathcal { X } = \oplus _ { 2 } \mathcal { Y } _ { n }$ (III.4.4). Define $\mathbf { \Phi } ;$ $\mathcal { R }   \rightarrow   \mathcal { X }$ by $\Phi ( y ) = ( y , y , \ldots )$ . It is easy to see that Φ is an isometry though it is clearly not surjective. In fact, ran $\Phi = \{ (y_n) \in \mathcal{X} : y_n = y_m$ for all $\left. n ,   m \right\}$ . Thus $\mathcal { R }$ is a Banach space. Let $P _ { 1 } = \mathrm { t h e }$ projection of X onto the first coordinate. Then $A = P _ { 1 } \circ \Phi$ and hence A is continuous.

(c) With the notation from the proof of (b), it follows that $\mathcal { X } ^ { * * } = \oplus _ { 2 } \mathcal { Y } _ { n } ^ { * * }$ and $\Phi ^ { * * } \colon { \mathcal { R } } ^ { * * }   \to   { \mathcal { X } } ^ { * * }$ is given by $\Phi ^ { * * } ( y ^ { * * } )   =   ( A ^ { * * } y ^ { * * } , A ^ { * * } y ^ { * * } , \ldots )$ Now the fact that Φ is an isometry implies that $\Phi ^ { * }$ is surjective. (This follows in two ways. One is by a direct argument (see Exercise 2). Also, ran $\Phi ^ { * }$ is closed since ran Φ is closed (1.10), and ran $\Phi ^ { * }$ is dense since $\mathbf { \Phi } ^ { \perp } ( \mathrm { r a n }   \mathbf { \Phi } ^ { * } ) = \ker \mathbf { \Phi } = ( 0 ) .$ Hence ker $\Phi^{**} = (\mathrm{ran} \Phi^*)^\perp = (0);$ that is, $\Phi^{**}$ is injective. Therefore $A ^ { * * }$ is injective.

Now let $y ^ { * * } \in A ^ { * * - 1 } ( \mathcal { Y } )$ . It follows that $\Phi ^ { * * } y ^ { * * }   =   x   \in   \mathcal { X }$ . Let $\{ y _ { i } \}$ be a net in R such that $\|   y_i \| \leqslant \|   y^{* *} \|$ for all i and $y _ { i }   \to   y ^ { * * } \sigma ( \mathcal { R } ^ { * * } , \mathcal { R } ^ { * } ) \mathrm { ~ ( V . 4 . 1 ) }$ . Thus $\Phi ^ { * * } (   y _ { i } )   \to   \Phi ^ { * * } (   y ^ { * * } ) \quad \sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ . But $\Phi ^ { * * } ( y _ { i } ) = \Phi ( y _ { i } ) \in \mathcal { X }$ and $\Phi ^ { * * } ( y ^ { * * } ) = x$ Hence Φ(yi) → x σ(x, X\*). Since ran Φ is closed, x∈ran Φ; let $\Phi ( y ) = x$ .Then $0 = \Phi ^ { * * } ( y ^ { * * } - y )$ Since $\Phi ^ { * * }$ is injective, $y ^ { * * } = y { \in } { \mathcal { R } }$

(d) An argument using Alaoglu's Theorem shows that $A^{*} \left( \mathrm{bal} \mathcal{R}^{*} \right) = \mathrm{the}$ $\sigma ( \mathcal { Y } ^ { * * } , \mathcal { Y } ^ { * } )$ closure of $A ( { \mathrm { b a l l } } { \mathcal { R } } )$ . Put $C = A ( \mathrm{bal}   \mathcal{R} )$ . Suppose cl W is weakly compact. Now $C \subseteq 2 ^ { n } { \mathrm { ~ c l ~ } } W + 2 ^ { - n }$ ball $\mathcal { Y } ^ { * * }$ and this set is $\sigma ( \mathcal { G } ^ { * * } , \mathcal { G } ^ { * } )$ compact. From the preceding comments, $A ^ { * * } ( \mathrm { b a l l } { \mathcal { R } } ^ { * * } ) \subseteq 2 ^ { n }   \mathrm { c l }   W + 2 ^ { - n }$ ball $\mathcal { Y } ^ { * * }$ Thus,

$$
\begin{align*}A^{**}(\mathsf{ball}   \mathcal{R}^{**}) & \subseteq \bigcap_{n=1}^{\infty} \left[ 2^n \mathsf{cl}   W + 2^{-n} \mathsf{ball}   \mathcal{G}^{**} \right] \\& \subseteq \bigcap_{n=1}^{\infty} \left[ \mathcal{G} + 2^{-n}   \mathsf{ball}   \mathcal{G}^{**} \right] \\& = \mathcal{G}.\end{align*}
$$

By (c), $\mathcal { R } ^ { * * } = \mathcal { R }$ and $\mathcal { R }$ is reflexive.

Now assume $\mathcal { R }$ is reflexive; thus ball $\mathcal { R }$ is $\sigma ( \mathcal { R } , \mathcal { R } ^ { * } )$ -compact. Therefore $C = A ( \mathrm{bal}   \mathcal{R} )$ is weakly compact in . By (a), cl W is weakly compact.

The next theorem, as well as the preceding lemma, are from Davis, Figiel Johnson, and Pelczynski [1974].

5.4. Theorem. $\mathit { I f }   \mathcal { X } ,   \mathcal { Y }$ are Banach spaces and $T   \in   \mathcal { B } ( \mathcal { X } , \mathcal { Y } ) ,$ , then T is weakly compact if and only if there is a reflexive space R and operators A in $\mathcal { B } ( \mathcal { R } , \mathcal { Y } )$ and B in $\mathcal { B } ( \mathcal { X } , \mathcal { R } )$ such that $T = A B$

PROOF. If $T = A B ,$ where A, B have the described form, then $T$ is weakly compact by Proposition 5.2.

Now assume that T is weakly compact and put $W = T ( \mathrm { b a l l }   \mathcal { X } )$ . Define R as in Lemma 5.3. By (5.3d), $\mathcal { R }$ is reflexive. Let $A \colon { \mathcal { R } }   \to   { \mathcal { G } }$ be the inclusion map. Note that if x∈ball $\mathcal { X } ,$ then $T x   \in   W .$ By (5.3a), $\| T x \| < 1$ whenever $\| x \| \leqslant 1$ . So $B \colon { \mathcal { X } }   \to   { \mathcal { R } }$ defined by $B x = T x$ is a bounded operator. Clearly $A B = T .$

The preceding result can be used to prove several standard results from antiquity.

5.5. Theorem. If X, Y are Banach spaces and $T   \in   \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ , the following statements are equivalent.

(a) T is weakly compact.

(b) $T ^ { * * } ( { \mathcal { X } } ^ { * * } ) \subseteq { \mathcal { Y } } .$

(c) $T ^ { * }$ is weakly compact.

PROOF. $(a) \Rightarrow (b);$ Let $\mathcal { R }$ be a reflexive space, $A \in \mathcal{B}(\mathcal{R}, \mathcal{Y})$ , and $B \in \mathcal{B}(\mathcal{X}, \mathcal{R})$ such that $T = A B .$ So $T ^ { * * } = A ^ { * * } B ^ { * * }$ . But $A ^ { * * } ;   \mathcal { R }   \to   \mathcal { Y } ^ { * * }$ since $\mathcal { R } ^ { * * } = \mathcal { R }$ Hence $A ^ { * * } = A$ . Thus $T ^ { * * } = A B ^ { * * }$ , and so ran $T ^ { * * } \subseteq \operatorname { r a n } A \subseteq { \mathcal { Y } } .$

$( \mathsf { b } ) { \Rightarrow } ( \mathsf { a } ) { : } T ^ { * * } ( \mathsf { b a l l }   \mathcal { X } ^ { * * } )$ is $\sigma ( \mathcal { Y } ^ { * * } , \mathcal { Y } ^ { * } )$ compact by Alaoglu's Theorem and the weak\* continuity of $T ^ { * * }$ . By (b), $T ^ { * * } ( \mathrm { b a l l }   \mathcal { X } ^ { * * } ) = C$ is $\sigma ( \mathcal { G } , \mathcal { G } ^ { * } )$ compact in Y. Hence $T ( \mathrm { b a l l }   \mathcal { X } ) \subseteq C$ and must have weakly compact closure.

$(c) \Rightarrow (a)$ Let $\mathcal { S }$ be a reflexive space, $C   \in   \mathcal { B } ( \mathcal { Y } ^ { * } , \mathcal { S } ) ,   D   \in   \mathcal { B } ( \mathcal { S } , \mathcal { X } ^ { * } )$ such that $T ^ { * } = D C$ .So $T ^ { * * } = C ^ { * } D ^ { * } , \quad D ^ { * } \colon \quad \mathcal { X } ^ { * * } { \rightarrow } \mathcal { S } ^ { * }$ , and $C ^ { * } \colon \operatorname { \mathcal { I } } ^ { * }   { \rightarrow }   \operatorname { \mathcal { Y } } ^ { * * }$ $\mathbf { P u t }$ ${ \mathcal { R } } = \operatorname { c l } D ^ { * } ( { \mathcal { X } } )$ and $B = D ^ { * } | { \mathcal { X } } ;$ then $B \colon { \mathcal { X } }   \to   { \mathcal { R } }$ and R is reflexive. Let $A = C^{*} \left| \mathcal{R} \right|$ $\mathrm{so} A: \mathcal{R} \to \mathcal{D}^{* *}$ . But if $x { \in } { \mathcal { X } } , A B x = C ^ { * } D ^ { * } x = T ^ { * * } x = T x { \in } { \mathcal { Y } }$ Thus $A : { \mathcal { R } } \to { \mathcal { G } }$ Clearly $A B = T .$

(a)⇒(c): Exercise.

## EXERCISES

1. Prove Proposition 5.2.

2. If $\mathcal { R }$ and $\mathcal { X }$ are Banach spaces and $\Phi \colon { \mathcal { R } }   \to   { \mathcal { X } }$ is an isometry, give an elementary proof that $\Phi ^ { * }$ is surjective.

3. Let $\mathcal { X }$ be a Banach space and recall the definition of a weakly Cauchy sequence $( \mathbf { V } . 4 . 4 )$ (a) Show that every bounded sequence in $c _ { 0 }$ has a weakly Cauchy subsequence, but not every weakly Cauchy sequence in $c _ { 0 }$ converges. (b) Show that if $T   \in   \mathcal { B } ( c _ { 0 } )$ and $T$ is weakly compact, then $T$ is compact.

4. Say that a Banach space $\mathcal { X }$ is weakly compactly generated (WCG) if there is a weakly compact subset K of X such that $\mathcal { X }$ is the closed linear span of K. Prove