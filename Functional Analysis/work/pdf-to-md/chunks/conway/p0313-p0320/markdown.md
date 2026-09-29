for N. Thus, if $\sigma ( N ) = \{ \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n } \}$ , where $\lambda _ { i } \neq \lambda _ { j }$ for $i   \neq   j ,$ then (10.2) becomes

$$
N \cong D _ { 1 } \oplus D _ { 2 } \oplus \cdots \oplus D _ { m } ,\tag{10.14}
$$

where $D _ { 1 } = \mathrm { d i a g } ( \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n } )$ and, for $k \geqslant 2 , D _ { k }$ is a diagonalizable operator whose diagonal consists of one, and only one, of each of the eigenvalues of N having multiplicity at least k.

There is another decomposition for normal operators that furnishes a complete set of unitary invariants and has a connection with the concept of multiplicity. For normal operators on a finite dimensional space, this decomposition takes on the following form.

Let $\Lambda _ { k } = \mathrm { t h } \mathbf { e }$ eigenvalues of N having multiplicity k. So for λ in $\Lambda _ { k } ,$ dim ker $( N - \lambda ) = k .$ If $\Lambda _ { k } = \{ \lambda _ { j } ^ { ( k ) } : 1 \leqslant j \leqslant m _ { k } \}$ , let $N _ { k }$ be the diagonalizable operator on a $k m _ { k }$ dimensional space whose diagonal contains each $\lambda _ { i } ^ { ( k ) }$ repeated k times. So $N \cong { \overline { { N } } } _ { 1 } \oplus { \overline { { N } } } _ { 2 } \oplus \cdots \oplus { \overline { { N } } } _ { p } ,$ if $\sigma ( N ) = \Lambda _ { 1 } \cup \cdots \cup \Lambda _ { p } .$ Now $\sigma ( N _ { k } ) = \Lambda _ { k }$ and each eigenvalue of $N _ { k }$ has multiplicity k. Thus $\dot { N _ { k } } \cong A _ { k } ^ { ( k ) }$ where $A _ { k }$ is a diagonalizable operator on an $m _ { k }$ dimensional space with $\sigma ( A _ { k } ) = \Lambda _ { k }$ . Thus

$$
N \cong A _ { 1 } \oplus A _ { 2 } ^ { ( 2 ) } \oplus \cdots \oplus A _ { p } ^ { ( p ) } ,\tag{10.15}
$$

and $\sigma ( A _ { i } ) \cap \sigma ( A _ { j } ) = \square$ for $i \neq j .$

Now the big advantage of the decomposition (10.15) is that it permits a discussion of $\{ N \} ^ { \prime }$ . Because the spectra of the operators $A _ { k }$ are disjoint,

$$
\{ N \} ^ { \prime }   =   \{ N _ { 1 } \} ^ { \prime }   \oplus   \{ N _ { 2 } \} ^ { \prime }   \oplus   \cdots   \oplus   \{ N _ { p } \} ^ { \prime } .
$$

(Why?) If $\mathcal { H } _ { j } ^ { ( k ) } = \ker ( N - \lambda _ { j } ^ { ( k ) } )$ , then dim $\mathcal { H } _ { j } ^ { ( k ) } = k$ and $\scriptstyle \bigoplus _ { j = 1 } ^ { m _ { k } } { \mathcal { H } } _ { j } ^ { ( k ) } =$ the domain of $N _ { k }$ Since $\left( \hat { \lambda } _ { i } ^ { ( k ) } \neq \hat { \lambda } _ { j } ^ { ( k ) } \right.$ for $i   \neq   j ,$

$$
\{ N _ { k } \} ^ { \prime } = \mathcal { B } ( \mathcal { H } _ { 1 } ^ { ( k ) } ) \oplus \cdots \oplus \mathcal { B } ( \mathcal { H } _ { m _ { k } } ^ { ( k ) } ) ,
$$

and each $\mathcal { B } ( \mathcal { H } _ { j } ^ { ( k ) } )$ is isomorphic to the $k \times k$ matrices.

The decomposition of an arbitrary normal operator that is analogous to decomposition (10.15) for finite dimensional normal operators is contained in the next result. The corresponding discussion of the commutant will follow this theorem.

10.16. Theorem. If N is a normal operator, then there are mutually singular measures $\mu _ { \infty } ,   \mu _ { 1 } ,   \mu _ { 2 } , \ldots$ (some of which may be zero) such that

$$
N \cong N _ { \mu _ { 1 } } ^ { ( \infty ) } \oplus N _ { \mu _ { 1 } } \oplus N _ { \mu _ { 2 } } ^ { ( 2 ) } \oplus \cdots .
$$

If M is another normal operator with corresponding measures $\nu _ { \infty } ,   \nu _ { 1 } ,   \nu _ { 2 } , \ldots ,$ then $N \cong M$ if and only $if \left[ \mu_{n} \right] = \left[ v_{n} \right]$ for $1 \leqslant n \leqslant \infty$

PROOF. Let $\mu$ be a scalar-valued spectral measure for N and let $\{ \Delta _ { n } \}$ be the sequence of Borel subsets of $\sigma ( N )$ obtained in Corollary 10.12. Put $\Sigma _ { \infty } = \bigcap _ { n = 1 } ^ { \infty } \Delta _ { n }$ and $\Sigma _ { n } = \Delta _ { n } \backslash \Delta _ { n + 1 }$ for $1 \leqslant n < \infty;$ let $\mu _ { n } = \mu | \Sigma _ { n } , 1 \leqslant n \leqslant \infty$ . Put $v _ { n } = \mu | \Delta _ { n } , \quad 1 \leqslant n < \infty$ Now $\Delta _ { n } = \Sigma _ { \infty } \cup ( \Delta _ { n } \setminus \Delta _ { n + 1 } ) \cup ( \Delta _ { n + 1 } \setminus \Delta _ { n + 2 } ) \cup \cdots =$ $\textstyle \sum _ { \infty } \cup \sum _ { n } \cup \sum _ { n   +   1 } \cup \cdots$ . Hence $y _ { n } = \mu _ { \infty } + \mu _ { n } + \mu _ { n + 1 } + \cdots$ and the measures $\mu _ { \infty } ,$ $\mu _ { n } , \mu _ { n + 1 } , \ldots$ are pairwise singular. Hence $N _ { v _ { n } } \cong N _ { \mu _ { x } } \oplus N _ { \mu _ { n } } \oplus N _ { \mu _ { n + 1 } } \cdots$ Combining this with Corollary 10.12 gives

$$
\begin{align*}N \cong &   N_{\mathfrak{v}_1} \oplus N_{\mathfrak{v}_2} \oplus N_{\mathfrak{v}_3} \oplus \cdots \\\cong &   (N_{\mu_x} \oplus N_{\mu_1} \oplus N_{\mu_2} \oplus \cdots) \oplus (N_{\mu_x} \oplus N_{\mu_2} \oplus N_{\mu_3} \oplus \cdots) \\&   \oplus (N_{\mu_x} \oplus N_{\mu_3} \oplus N_{\mu_4} \oplus \cdots) \oplus \cdots \\\cong &   N_{\mu_x}^{(\infty)} \oplus N_{\mu_1} \oplus N_{\mu_2}^{(2)} \oplus N_{\mu_3}^{(3)} \oplus \cdots.\end{align*}
$$

The proof of the uniqueness part of the theorem is left to the reader.

Note that the form of the normal operator presented in Example 10.13 is the form of the operator given in the conclusion of the preceding theorem.

Now to discuss $\{ N \} ^ { \prime }$ . Fix a compactly supported positive Borel measure μ on C and let $\mathcal { H } _ { n }$ be an n-dimensional Hilbert space, $1 \leqslant n \leqslant \infty$ . Define a function $f \colon \mathbf { C } \to \mathcal { H } _ { n }$ to be a Borel function if $z \mapsto \langle f ( z ) , g \rangle$ is a Borel function for each g in $\mathcal { H } _ { n } . \mathrm { I f } f : \mathbb { C } \to \mathcal { H } _ { n }$ is a Borel function and $\{ e _ { j } \}$ is an orthonormal basis for $\mathcal { H } _ { n }$ then $\| f ( z ) \| ^ { 2 } = \textstyle \sum _ { j } | \langle f ( z ) , e _ { j } \rangle | ^ { 2 }$ sO $z \to \| f ( z ) \| ^ { 2 }$ is a Borel function. Let $L ^ { 2 } ( \mu ;   \mathcal { H } _ { n } )$ be the space of all Borel functions $f \colon \mathbb { C }   \to   \mathcal { H } _ { n }$ such that $\| f \| ^ { 2 } \equiv \int \| f ( z ) \| ^ { 2 } d \mu ( z ) < \infty$ , where two functions agreeing a.e. [μ] are identified. If f and $g \in L ^ { 2 } ( \mu ; \mathcal { H } _ { n } ) , \langle f , g \rangle \equiv \int \langle f ( z ) , g ( z ) \rangle   d \mu ( z )$ defines an inner product on $L ^ { 2 } ( \mu ;   \mathcal { H } _ { n } )$ It is not difficult to show that $L ^ { 2 } ( \mu ; \mathcal { H } _ { n } )$ is a Hilbert space.

## 10.17. Proposition. If N is multiplication by z on $L ^ { 2 } ( \mu ;   \mathcal { H } _ { n } ) .$ , then $N \cong N _ { \mu } ^ { ( n ) } ,$

PROOF. Let $\{ e _ { j } ; 1 \leqslant j \leqslant n \}$ be an orthonormal basis for $\mathcal { H } _ { n }$ and define U: $L ^ { 2 } ( \mu ; \mathcal { H } _ { n } ) \to \widetilde { L ^ { 2 } ( \mu ) ^ { ( n ) } }$ by $U f = ( \langle f ( \cdot ) , e _ { 1 } \rangle , \langle f ( \cdot ) , e _ { 2 } \rangle , \ldots )$ . Then U is an isomorphism and $U N U ^ { - 1 } = N _ { \mu } ^ { ( n ) }$ . The details are left to the reader.

Combining the preceding proposition with Proposition 6.1(b), we can find $\{ N \} ^ { \prime } ;$ namely, $\left\{ N _ { \mu } ^ { ( n ) } \right\} ^ { \prime } = \mathrm { a l l }$ matrices $( T _ { i j } )$ on $\mathcal { B } ( L ^ { 2 } ( \mu ) ^ { ( n ) } )$ such that $T _ { i j } { \in } \{ N _ { \mu } \} ^ { \prime }$ for all i, j. By Corollary $6.9, \left\{ N_{\mu}^{(n)} \right\}' = \mathrm{ma}$ trices $( M _ { \phi _ { i j } } )$ that belong to $\mathcal { B } ( L ^ { 2 } ( \mu ) ^ { ( n ) } )$ such that $\phi _ { i j } { \in } L ^ { \infty } ( \mu )$ . Now the idea is to use Proposition 10.17 to bring this back to $\mathcal { B } ( L ^ { 2 } ( \mu ; \mathcal { H } _ { n } ) )$ and describe $\{ N \} ^ { \prime }$

A function φ: $\mathbb { C } \rightarrow \mathcal { B } ( \mathcal { H } _ { n } )$ is defined to be a Borel function if for each f and g in $\mathcal { H } _ { n } ,   z \mapsto \langle \phi ( z ) f , g \rangle$ is a Borel function. If $\{ f _ { j } \}$ is a countable dense subset of the unit ball of $\mathcal { H } _ { n } , \| \phi ( z ) \| = \sup \left\{ \left| \zeta \phi ( z ) f _ { i } \right| , f _ { j } \right\rangle : 1 \leqslant i , j < \infty \}$ , SO $z   \mapsto   \|   \phi ( z )   \|$ is a Borel function. Let $L ^ { \infty } ( \mu ; { \mathcal { B } } ( { \mathcal { H } } _ { n } ) )$ be the equivalence classes of bounded Borel functions from C into $\mathcal { B } ( \mathcal { H } _ { n } )$ furnished with the μ-essential supremum norm.

If $\phi \in L ^ { \infty } ( \mu ; { \mathcal { B } } ( { \mathcal { H } } _ { n } ) )$ and $f   \in   L ^ { 2 } ( \mu ; \mathcal { H } _ { n } ) ,$ let $\begin{array} { r } { f ( z )   =   \sum f _ { j } ( z ) e _ { j } , } \end{array}$ where $\left\{ e _ { j } \right\}$ is an orthonormal basis for $\mathcal { H } _ { n }$ and $f _ { j } ( z ) = \langle f ( z ) , e _ { j } \rangle , \mathrm { s o } \sum | f _ { j } ( z ) | ^ { 2 } = \| f ( z ) \| ^ { 2 } .$ Thus $\begin{array} { r } { \phi ( z ) f ( z ) = \sum _ { j } f _ { j } ( z ) \phi ( z ) e _ { j } . } \end{array}$ So for any e in $\mathcal { H } _ { n } , \dot { \langle } \phi ( z ) f ( z ) , e \rangle = \sum f _ { j } ( z ) \langle \phi ( z ) e _ { j } , e \rangle$ is a Borel function. It is easy to check that $\phi f \in L^{2}(\mu; \mathcal{H}_{n})$ and $\|   \phi f   \| \leqslant \|   \phi   \| _ { \infty }   \|   f   \|$ . Let $M _ { \phi } : L ^ { 2 } ( \mu ; \mathcal { H } _ { n } ) \to L ^ { 2 } ( \mu ; \mathcal { H } _ { n } )$ be defined by $M _ { \phi }   f = \phi f$ Combined with the preceding remarks, the following result can be shown to hold. (The proof is left to the reader.)

10.18. Proposition. If N is multiplication by z on $L ^ { 2 } ( \mu ; \mathcal { H } _ { n } ) ,$ then

$$
\{ N \} ^ { \prime }   =   \{ M _ { \phi } \colon \phi   \in   L ^ { \infty } ( \mu ;   \mathcal { B } ( \mathcal { H } _ { n } ) ) \} .
$$

Also, | $\| M _ { \phi } \| = \| \phi \| _ { \infty }$ for every φ in $L ^ { \infty } ( \mu ; { \mathcal { B } } ( { \mathcal { H } } _ { n } ) )$

The next lemma is a consequence of Proposition 6.10 and the fact that unitarily equivalent normal operators have mutually absolutely continuous scalar-valued spectral measures.

10.19. Lemma. $I f N _ { 1 }$ and $N _ { 2 }$ are normal operators with mutually singular scalar spectral measures and $X N _ { 1 } = N _ { 2 } X$ , then $X = 0$

Using the observation made prior to Corollary 6.8, the preceding lemma implies that $\{ N _ { 1 } \oplus N _ { 2 } \} ^ { \prime } = \{ N _ { 1 } \} ^ { \prime } \oplus \{ N _ { 2 } \} ^ { \prime }$ whenever $N _ { 1 }$ and $N _ { 2 }$ are as in the lemma.

The next theorem of this section can be proved by piecing together Theorem 10.16 and the remaining results of this section. The details are left to the reader.

10.20. Theorem. If N is a normal operator on $\mathcal { H }$ , there are mutually singular measures $\mu _ { \infty } , \mu _ { 1 } , \mu _ { 2 } , \ldots$ and an isomorphism

$$
U \colon { \mathcal { H } } \to L ^ { 2 } ( \mu _ { \infty } ;   { \mathcal { H } } _ { \infty } ) \oplus L ^ { 2 } ( \mu _ { 1 } ) \oplus L ^ { 2 } ( \mu _ { 2 } ;   { \mathcal { H } } _ { 2 } ) \oplus \cdots
$$

such that

$$
U N U ^ { - 1 } = N _ { \infty } \oplus N _ { 1 } \oplus N _ { 2 } \oplus \cdots
$$

where $N _ { n } =$ multiplication by z on $L ^ { 2 } ( \mu _ { n } ; \mathcal { H } _ { n } )$ Also,

$$
\begin{align*}\{ \boldsymbol{N}_{\infty} \oplus \boldsymbol{N}_{1} \oplus \boldsymbol{N}_{2} \oplus \cdots \}' = &   L^{\infty}(\mu_{\infty}; \mathcal{B}(\mathcal{H}_{\infty})) \oplus L^{\infty}(\mu_{1}) \\& \oplus L^{\infty}(\mu_{2}; \mathcal{B}(\mathcal{H}_{2})) \oplus \cdots   .\end{align*}
$$

Using the notation of the preceding theorem, if $\mu$ is a scalar-valued spectral measure for N, then there are pairwise disjoint Borel sets $\Delta _ { \infty } ,   \Delta _ { 1 } , \ldots$ . such that $[ \mu _ { n } ] = [ \mu | \Delta _ { n } ]$ Define a function $m _ { N } \colon \mathbb { C } \to \{ 0 , 1 , \ldots \infty \}$ by letting $m _ { N } = \infty \chi _ { \Delta _ { x } } + \chi _ { \Delta _ { 1 } } + 2 \chi _ { \Delta _ { 2 } } + \cdots$ . As it stands the definition of $m _ { N }$ depends on the choice of the sets $\{ \Delta _ { n } \}$ as well as N. However, any two choices of the sets $\{ \Delta _ { n } \}$ differ from one another by sets of μ-measure zero. The function $m _ { N }$ is called the multiplicity function for N. Note that $m _ { N }$ is a Borel function.

If m: $\mathfrak { C }   \rightarrow   \{ \infty , 0 , 1 , 2 , \ldots \}$ is a Borel function and is a compactly supported $\mu$ measure such that $\mu ( \{ z \colon m ( z ) = 0 \} ) = 0 ,$ let $\Delta _ { n } = \{ z ;   m ( z ) = n \} ,   n = \infty ,   1 , 2 , \ldots .$ If $N _ { n } = N _ { \mu | \Delta _ { n } }$ , then $N = N _ { \infty } ^ { ( \infty ) } \oplus N _ { 1 } \oplus N _ { 2 } ^ { ( 2 ) } \oplus \cdots$ is a normal operator whose spectral measure is $\mu$ and whose multiplicity function agrees with m a.e. [μ].

10.21. Theorem. Two normal operators are unitarily equivalent if and only if they have the same scalar-valued spectral measure $\mu$ and their multiplicity functions are equal a.e. [µ].

There is some notation that is used by many and we should mention its connection with what we have just finished. Suppose m: $\mathbb { C }   \rightarrow   \{ \infty , 1 , 2 , \ldots \}$ is a Borel function and $\mu$ is a compactly supported measure on C such that $\mu ( \{ z \colon m ( z ) = 0 \} ) = 0$ . If $z \in \mathbf { C }$ let $\mathcal { H } ( z )$ be a Hilbert space of dimension m(z). The direct integral of the spaces $\mathcal { H } ( z )$ , denoted by $\int \mathcal { H } ( z )   d \mu ( z )$ , is precisely the space

$$
L ^ { 2 } ( \mu | \Delta _ { \infty } ;   \mathcal { H } _ { \infty } )   \oplus   L ^ { 2 } ( \mu | \Delta _ { 1 } )   \oplus   L ^ { 2 } ( \mu | \Delta _ { 2 } ;   \mathcal { H } _ { 2 } )   \oplus \cdots ,
$$

where $\Delta _ { n } = \{ z : m ( z ) = n \}$ and dim $\mathcal { H } _ { n } = n . \mathrm { I f }   \phi \colon \mathbb { C } \to \mathcal { B } ( \mathcal { H } _ { \infty } ) \cup \mathcal { B } ( \mathbb { C } ) \cup \mathcal { B } ( \mathcal { H } _ { 2 } ) \cup \cdots$ such that $\phi ( z ) \in \mathcal { B } ( \mathcal { H } _ { n } )$ when $z { \in } \Delta _ { n } , \phi { : } \Delta _ { n } \to { \mathcal { B } } ( { \mathcal { H } } _ { n } )$ is a Borel function, and there is a constant M such that $\| \phi ( z ) \| \leqslant M \; { \mathrm { a . e . } }$ [μ], then $\int \phi ( z )   d \mu ( z )$ denotes the operator $M _ { \phi | \mathbf { \Delta } _ { \mathtt { x } } } \oplus \cdots$ as in (10.20). Although the direct integral notation is quite suggestive, one must revert to the notation of (10.20) to produce proofs.

Remarks. There are several sources for multiplicity theory. Most begin by proving Theorem 10.16. This is done for nonseparable spaces in Halmos [1951] and Brown [1974]. Another source is Arveson [1976], where the theory is set in the context of C\*-algebras which is its proper milieu. Also, Arveson shows that the theory can be applied to some non-normal operators. The details of this more general multiplicity theory are carried out in Ernest [1976] as part of a more general classification scheme. Another source for multiplicity theory is Dunford and Schwartz [1963].

By Theorem 4.6, every normal operator is unitarily equivalent to a multiplication operator $M _ { \phi }$ on $L ^ { 2 } ( X , \Omega , \mu )$ for some measure space $( X , \Omega , \mu ) .$ The scalar-valued spectral measure for $M _ { \phi }$ is $\mu \circ \phi ^ { - 1 }$ What is the multiplicity function for $M _ { \phi } ?$ One is tempted to say that $m _ { { \cal M } _ { \phi } } ( z ) =$ the number of points in $\phi ^ { - 1 } ( z )$ . This is not quite correct. The answer can be found in Abrahamse and Kriete [1973]. Also, Abrahamse [1978] contains a survey of spectral multiplicity for normal operators treated from this point of view. An especially accessible and readable account of this can be found in Kriete [1986].

## EXERCISES

1. Let A and B be operators on $\mathcal { H }$ and $\mathcal { H }$ , respectively. Let $\mathcal { H } _ { 0 }$ and $\mathcal { H } _ { 0 }$ be reducing subspaces for A and B and suppose that $A \cong B | \mathcal { H } _ { 0 }$ and $B \cong A \vert \mathcal { H } _ { 0 }$ . Show that $A \cong B ,$

2. Let $\mu _ { 1 } , \mu _ { 2 } , \ldots$ be compactly supported measures on C such that $\mu _ { n + 1 } \ll \mu _ { n }$ for all n. Show that if M is any normal operator whose spectral measure is absolutely continuous with respect to each $\mu _ { n } ,$ then $N _ { \mu _ { 1 } } \oplus N _ { \mu _ { 2 } } \oplus \cdots \cong ( N _ { \mu _ { 1 } } \oplus N _ { \mu _ { 2 } } \oplus \cdots ) \oplus M .$

3. If µ = Lebesgue measure on [0, 1], show that $N _ { \mu } \cong N _ { \mu } ^ { p }$ for $0 < p < \infty$

4. Let μ = Lebesgue measure on [0, 1] and characterize the functions $\phi$ in $L ^ { \infty } ( \mu )$ such that $N _ { \mu } \cong \phi ( N _ { \mu } ) .$

5. Let µ = area measure on D and show that $N _ { \mu }$ and $N _ { \mu } ^ { 2 }$ are not unitarily equivalent.

6. Let µ = Lebesgue measure on [0, 1] and let v = Lebesgue measure on [ - 1, 1]. Show that $N _ { y } ^ { 2 }   \cong   N _ { \mu }   \oplus   N _ { \mu ^ { * } }$ How about $N _ { y } ^ { 3 } { } _ { \bullet } ^ { ? }$

7. Let $\mu$ be Lebesgue measure on R and N = multiplication by sin x on $L ^ { 2 } ( \mu )$ . Find the decompositions of N obtained in Theorem 10.1 and 10.16.

8. If $\mu$ is Lebesgue measure on R and N = multiplication by $e ^ { i x }$ on $L ^ { 2 } ( \mu ) ,$ show that $N \cong N _ { m } ^ { ( \infty ) }$ where m = arc length measure on ∂D.

9. Define $U \colon L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } ) \mathrm { ~ b y ~ } ( U f ) ( t ) = f ( t - 1 )$ . Show that $U$ is unitary and find its scalar-valued spectral measure and multiplicity function.

10. Represent N as in Theorem 10.1 and find the corresponding representation for N⊕ $N = N ^ { ( 2 ) } ;$ for $N ^ { ( 3 ) }$ , for $N ^ { ( \infty ) }$ (Are you surprised by the result for $N ^ { ( \infty ) } ? )$

11. Prove the results and solve the exercises from §II.8.

12. Let N be a normal operator and show that $N \cong N ^ { ( 2 ) }$ if and only if there is a \*-cyclic normal operator M such that $N \cong M ^ { ( \infty ) }$ . What does this say about the multiplicity function for N?

13. Let $( X , \Omega , \mu )$ be a measure space such that $L ^ { 2 } ( \mu )$ is separable, let $\phi   \in   L ^ { \infty } ( \mu )$ , and let $N = M _ { \phi }$ on $L ^ { 2 } ( \mu )$ . Find the decompositions of N obtained in Theorems 10.1 and 10.16.

14. Let $\mu$ be a compactly supported measure on $\mathbf { c } , \phi$ a bounded Borel function on C, and suppose $\{ \Delta _ { n } \}$ are pairwise disjoint Borel sets such that φ is one-to-one on each $\Delta _ { n }$ and $\mu(\mathbb{C} \setminus \bigcup_{n = 1}^{\infty} \Delta_{n}) = 0.$ Let $\phi _ { n } = \phi \chi _ { \Delta _ { n } }$ and $\mu _ { n }   =   \mu ^ { \circ } \phi _ { n } ^ { - 1 }$ for $n \geqslant 1$ . Prove that $M _ { \phi }$ on $L ^ { 2 } ( \mu )$ is unitarily equivalent to $\oplus _ { n = 1 } ^ { \infty } N _ { \mu _ { n } } .$

# CHAPTER X Unbounded Operators

It is unfortunate for the world we live in that all of the operators that arise naturally are not bounded. But that is indeed the case. Thus it is important to study such operators.

The idea here is not to study an arbitrary linear transformation on a Hilbert space. In fact, such a study is the province of linear algebra rather than analysis. The operators that are to be studied do possess certain properties that connect them to the underlying Hilbert space. The properties that will be isolated are inspired by natural examples.

All Hilbert spaces in this chapter are assumed separable.

## §1. Basic Properties and Examples

The first relaxation in the concept of operator is not to assume that the operators are defined everywhere on the Hilbert space.

1.1. Definition. If $\mathcal { H } , \mathcal { H }$ are Hilbert spaces, a linear operator $A : \mathcal { H } \rightarrow \mathcal { H }$ is a function whose domain of definition is a linear manifold, dom A, in $\mathcal { H }$ and such that $A(\alpha f + \beta g) = \alpha A f + \beta A g$ for $f , g$ in dom A and $\alpha , \beta$ in C. A is bounded if there is a constant $c   >   0$ such that $\| A f \| \leqslant c \| f \|$ for all f in dom A.

Note that if A is bounded, then A can be extended to a bounded linear operator on cl[dom $A ]$ and then extended to $\mathcal { H }$ by letting A be 0 on (dom $A ) ^ { \perp }$ . So unless it is specified to the contrary, a bounded operator will always be assumed to be defined on all of $\mathcal { H }$

If A is a linear operator from $\mathcal { H }$ into $\mathcal { H } ,$ then A is also a linear operator from cl[dom $[ A ]$ into $\mathcal { H }$ . So we will often only consider those A such that dom A is dense in $\mathcal { H } ;$ such an operator A is said to be densely defined. $\mathcal { B } ( \mathcal { H } )$ still denotes the bounded operators defined on $\mathcal { H }$

If $A , B$ are linear operators from $\mathcal { H }$ into $\varkappa$ , then $A + B$ is defined with dom $(A + B) = \mathrm{dom} A \cap$ dom B. If $B : \mathcal { H } \to \mathcal { H }$ and $A \colon { \mathcal { H } } \to { \mathcal { L } } ,$ then $A B$ is a linear operator from $\mathcal { H }$ into $\mathcal { L }$ with dom $(AB) = B^{-1}(\mathrm{dom} A)$

1.2. Definition. If A, B are operators from $\mathcal { H }$ into $\mathcal { H }$ , then A is an extension of B if dom $B \subseteq \dim A$ and $A h = B h$ whenever hedom B. In symbols this is denoted by $B \subseteq A$

Note that if $A   \in   \mathcal { B } ( \mathcal { H } )$ , then the only extension of A is itself. So this concept is only of value for unbounded operators.

If $A : { \mathcal { H } } \to { \mathcal { H } }$ , the graph of A is the set

$$
\mathrm{grad} A \equiv \{ h \oplus A h \in \mathcal{H} \oplus \mathcal{H} : h \in \mathrm{dom} A \}.
$$

It is easy to see that $B \subseteq A$ if and only if gra $B \subseteq \operatorname { g r a } A$

1.3. Definition. An operator $A : \mathcal { H } \rightarrow \mathcal { H }$ is closed if its graph is closed in $\mathcal { H } \oplus \mathcal { H }$ . An operator is closable if it has a closed extension. Let $\mathcal { C } ( \mathcal { H } , \mathcal { H } ) =$ the collection of all closed densely defined operators from $\mathcal { H }$ into X. Let $\mathcal { C } ( \mathcal { H } ) =$ $\mathcal { C } ( \mathcal { H } , \mathcal { H } )$ . (It should be emphasized that the operators in $\mathcal { C } ( \mathcal { H } , \mathcal { H } )$ are densely defined.)

When is a subset of $\mathcal { H } \oplus \mathcal { H }$ a graph of an operator from $\mathcal { H }$ into $\mathcal { H } ?$ If ${ \mathcal { G } } = \operatorname { g r a } A$ for some $A : \mathcal { H } \rightarrow \mathcal { H }$ , then $\pmb { \mathscr { G } }$ is a submanifold of $\mathcal { H } \oplus \mathcal { H }$ such that if $k \in \mathcal { H }$ and $\mathbf { 0 }   \oplus   k   \in   \mathcal { G } ,$ then $k   =   0 ,$ The converse is also true. That $\mathbf { i s } ,$ suppose that G is a submanifold of $\mathcal { H } \oplus \mathcal { H }$ such that if $k \in \mathcal { H }$ and $0 \oplus k \in { \mathcal { G } } ,$ then $k   =   0 .$ Let $\mathcal { D } = \{ h \in \mathcal { H } :$ there exists a k in $\mathcal { H }$ with h⊕k in $\{ \theta \}$ . If $h { \in } { \mathcal { D } }$ and $k _ { 1 } , k _ { 2 } { \in } \mathcal { H }$ such that $h \oplus k _ { 1 } , h \oplus k _ { 2 } \in \mathcal { G }$ , then $0 \oplus (k_1 - k_2) = h \oplus k_1 - h \oplus k_2 \in \mathcal{G}$ Hence $k _ { 1 } = k _ { 2 }$ . That is, for every h in $\mathcal { D }$ there is a unique k in $\varkappa$ such that $h \oplus k \in { \mathcal { G } } ;$ denote k by $k = A h .$ It is easy to check that A is a linear map and ${ \mathcal { G } } = \operatorname { g r a } A$ . This gives an internal characterization of graphs that will be useful in the next proposition.

1.4. Proposition. An operator $A : \mathcal { H } \to \mathcal { H }$ is closable if and only if cl[gra A] is a graph.

PRooF. Let cl[gra A] be a graph. That is, there is an operator B: $\mathcal { H } \rightarrow \mathcal { H }$ such that gra $B = \mathrm{cl} \left[ \mathrm{grad} A \right]$ . Clearly gra $A \subseteq \operatorname { g r a } B ,$ sO $A$ is closable.

Now assume that A is closable; that is, there is a closed operator $B : \mathcal { H } \to \mathcal { H }$ with $A \subseteq B .$ If 0 ⊕ k∈cl[gra A], 0⊕ k∈gra B and hence $k   =   0$ . By the remarks preceding this proposition, cl[gra A] is a graph.

If A is closable, call the operator whose graph is cl[gra A] the closure of A.

1.5. Definition. If $A : \mathcal { H } \rightarrow \mathcal { H }$ is densely defined, let

dom $A ^ { * }   =   \{ k   \in   \mathcal { H } \colon h     \mapsto   \langle A h , k \rangle$ is a bounded linear functional on dom $\left. A \right\}$

Because dom A is dense in $\mathcal { H } ,$ if k∈dom $A ^ { * }$ , then there is a unique vector f in $\mathcal { H }$ such that $\langle A h , k \rangle = \langle h , f \rangle$ for all h in dom A. Denote this unique vector $f$ by $f = A ^ { * } k$ Thus

$$
\langle A h , k \rangle = \langle h , A ^ { * } k \rangle
$$

for h in dom A and k in dom $A ^ { * }$

1.6. Proposition. If A: $\mathcal { H } \rightarrow \mathcal { H }$ is a densely defined operator, then:

(a) $A ^ { * }$ is a closed operator;

(b) $A ^ { * }$ is densely defined if and only if A is closable;

(c) if A is closable, then its closure is $( A ^ { * } ) ^ { * } \equiv A ^ { * * }$

Before proving this, a lemma is needed which will also be useful later.

1.7. Lemma. $If A: \mathcal{H} \rightarrow \mathcal{H}$ is densely defined and J: $\mathcal { H } \oplus \mathcal { H } \rightarrow \mathcal { H } \oplus \mathcal { H }$ is defined by $J ( h \oplus k ) = ( - k ) \oplus h$ , then J is an isomorphism and

$$
\mathrm{grad} A^{*} = \left[ J \mathrm{grad} A \right]^{\perp}.
$$

PRooF. It is clear that J is an isomorphism. To prove the formula for gra $A ^ { * }$ note that gra $A ^ { * } = \{ k \oplus A ^ { * } k \in { \mathcal { H } } \oplus { \mathcal { H } }$ k∈dom $\{ A ^ { * } \}$ . So if kedom $A ^ { * }$ and hedom A,

$$
\begin{align*}\langle k \oplus A^* k, J(h \oplus A h) \rangle &= \langle k \oplus A^* k, -A h \oplus h \rangle \\&= -\langle k, A h \rangle + \langle A^* k, h \rangle = 0.\end{align*}
$$

Thus gra $A ^ { * } \subseteq [ J \operatorname { g r a } A ] ^ { \perp }$ . Conversely, if $k \oplus f \in [J \operatorname{grad} A]^{\perp}$ , then for every h is dom $A,0=\zeta k\dot{\oplus}f,-A\dot{h}\oplus h\rangle=-\zeta k,A\dot{h}\rangle+\zeta f,\ \mathrm{so}\ \langle A\dot{h},k\rangle=\langle h,f\rangle$ By definition kedom $A ^ { * }$ and $A ^ { * } k = f .$

PRoOF OF PRoPOsITION 1.6. The proof of (a) is clear from Lemma 1.7. For the remainder of the proof notice that because the mapJ in (1.7) is an isomorphism, $J ^ { * } = J ^ { - 1 }$ and so $J ^ { * } ( k \oplus h ) = h \oplus ( - k )$

(b) Assume A is closable and let $k_{0} \in (\mathrm{dom} A^{*})^{\perp}$ . We want to show that $k _ { 0 } = 0$ Thus $k _ { 0 } \oplus 0 \in [ \mathrm { g r a }   A ^ { \star } ] ^ { \perp } = [ J   \mathrm { g r a }   A ] ^ { \perp \perp } = \mathrm { c l } [ J   \mathrm { g r a }   A ] = J [ \mathrm { c l } ( \mathrm { g r a }   A ) ]$ $\mathrm{So} 0 \oplus -k_0 = J^*(k_0 \oplus 0) \in J^*J[(\mathrm{grad} A)] = \mathrm{cl}(\mathrm{grad} A)$ . But because A is closable, cl(gra A) is a graph; hence $k _ { 0 }   =   0$ . For the converse, assume dom $A ^ { * }$ is dense in $\mathcal { H }$ Thus $A ^ { * * } \equiv ( A ^ { * } ) ^ { * }$ is defined. By (a), $A ^ { * * }$ is a closed operator. It is easy to see that $A \subseteq A ^ { * * }$ , so A has a closed extension.

(c) Note that by Lemma 1.7 gra $A ^ { * * } = [ J ^ { * }   \mathtt { g r a }   A ^ { * } ] ^ { \perp } = [ J ^ { * } [ J   \mathtt { g r a }   A ] ^ { \perp } ] ^ { \perp }$ But for any linear manifold $\mathcal { M }$ and any isomorphism $J , ( J \mathcal { M } ) ^ { \perp } = J ( \mathcal { M } ^ { \perp } )$ Hence $J ^ { * } [ ( J \mathcal { M } ) ^ { \perp } ] = \mathcal { M } ^ { \perp }$ and, thus, $[ J ^ { * } [ J . \mathcal { M } ] ^ { \perp } ] ^ { \perp } = \mathcal { M } ^ { \perp \perp } = \mathcal { \mathrm { c l } } . \mathcal { M }$ .Putting ${ \mathcal { M } } = \operatorname { g r a } A$ gives that gra $A ^ { * * } = \mathbf { c l }$ gra A. ■

1.8. Corollary. $If A \in \mathcal{C}(\mathcal{H}, \mathcal{H}),$ then $A ^ { * } \in \mathcal { C } ( \mathcal { H } , \mathcal { H } )$ and $A ^ { * * } = A$