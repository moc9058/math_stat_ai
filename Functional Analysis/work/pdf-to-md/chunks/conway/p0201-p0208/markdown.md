(Davis, Figiel, Johnson, and Pelczynski, [1974]) that $\mathcal { X }$ is WCG if and only if there is a reflexive space and an injective bounded operator $T \colon { \mathcal { R } } \to { \mathcal { X } }$ such that ran $T$ is dense. (Hint: The Krein-Smulian Theorem (V.13.4) may be useful.)

5. If $( X , \Omega , \mu )$ is a finite measure space, ke $L ^ { \infty } ( X \times X , \mathbf { \Omega } \times \mathbf { \Omega } , \mu \times \mu ) ,$ and $K ;$ $L ^ { 1 } ( \mu ) \to L ^ { 1 } ( \mu )$ is defined by $(Kf)(x) = \int k(x,y)f(y)d\mu(y)$ , show that K is weakly compact and $K ^ { 2 }$ is compact.

6. Let $\pmb { g }$ be a weakly sequentially complete Banach space. That is, if $\{ y _ { n } \}$ is a sequence in Y such that $\{ \langle y _ { n } , y ^ { * } \rangle \}$ is a Cauchy sequence in F for every $y ^ { * }$ in $\theta ^ { * }$ , then there is a y in $\theta$ such that $y _ { n }   \rightarrow   y$ weakly [see (V.4.4)]. (a) If $T \in \mathcal { B } ( \mathcal { X } , \mathcal { Y } )$ and $x^{*} \in \mathcal{X}^{*}$ such that $x ^ { * * }$ is the $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ limit of a sequence $\left\{ x_{n}^{ 本本 } \right\}$ from $\mathcal { X } ^ { * * }$ such that $T^{*} \overline{{x}}_{n}^{*} \in \mathcal{G}$ for every n, show that $T^{\mathrm{半半}}(x^{\mathrm{半半}}) \in \mathcal{G}$ . Let X be a compact space and put $\mathcal { F } = \mathrm { a l l }$ subsets of X that are the union of a countable number of compact $G _ { \delta }$ sets. Let ${ \mathcal { L } } = \operatorname { t h e }$ linear span of $\{ \chi _ { F } : F \in { \mathcal { F } } \}$ considered as a subset of $M(X)^{*} = C(X)^{*}$ (b) Show that if $T \in { \mathcal { B } } ( C ( X ) , { \mathcal { Y } } )$ then $T ^ { * * } ( \mathcal { L } ) \subseteq \mathcal { Y }$ (c) (Grothendieck [1953].) If $T \in \mathcal{B}(C(X), \mathcal{B})$ , then T is weakly compact. [Hint (Spain [1976]): Use James's Theorem V.13.3).]

CHAPTER VII

# Banach Algebras and Spectral Theory for Operators on a Banach Space

The theory of Banach algebras is a large area in functional analysis with several subdivisions and applications to diverse areas of analysis and the rest of mathematics. Some monographs on this subject are by Bonsall and Duncan [1973] and C.E. Rickart [1960].

A significant change occurs in this chapter that will affect the remainder of this book. In order to prove that the spectrum of an element of a Banach algebra is nonvoid (Section 3), it is necessary to assume that the underlying field of scalars $\mathbb { F }$ is the field of complex numbers C. It will be assumed from Section 3 until the end of this book that all vector spaces are over $\mathbf { C } .$ This will also enable us to apply the theory of analytic functions to the study of Banach algebras and linear operators.

In this chapter only the rudiments of this subject are discussed. Enough, however, is presented to allow a treatment of the basics of spectral theory for operators on a Banach space.

## §1. Elementary Properties and Examples

An algebra over $\mathbb { F }$ is a vector space $\varkappa$ over $\mathbb { F }$ that also has a multiplication defined on it that makes $\varkappa$ into a ring such that if $\alpha \in \mathbf { F }$ and $a , b \in \mathcal { A } ,$ $\alpha ( a b ) = ( \alpha a ) b = a ( \alpha b )$

1.1. Definition. A Banach algebra is an algebra $\alpha$ over $\mathbb { F }$ that has a norm $\| \cdot \|$ relative to which $\varkappa$ is a Banach space and such that for all $a , b$ in $\alpha ,$

$$
\| a b \| \leqslant \| a \| \| b \|.
$$

If has an identity, $e ,$ then it is assumed that $\| e \| = 1$

The fact that (1.2) is satisfied is not essential. If $\varkappa$ is an algebra and has a norm relative to which $\varkappa$ is a Banach space and is such that the map of $\mathcal { A } \times \mathcal { A } \rightarrow \mathcal { A }$ defined by $( a , b ) { \mapsto } a b$ is continuous, then there is an equivalent norm on $\varkappa$ that satisfies (1.2) (Exercise 1).

If $\varkappa$ has an identity $e ,$ then the map $\alpha   \mapsto   \alpha e$ is an isomorphism of $\mathbb { F }$ into $\alpha$ and $\| \alpha e \| = | \alpha |$ . So it will be assumed that $\mathbb { F } \subseteq \mathcal { A }$ via this identification. Thus the identity will be denoted by 1.

The content of the next proposition is that if $\varkappa$ does not have an identit $\mathbf { y } ,$ it is possible to find a Banach algebra $\alpha _ { 1 }$ that contains $\varkappa$ , that has an identity, and is such that dim $\mathcal { A } _ { 1 } / \mathcal { A } = 1$

1.3. Proposition. If A is a Banach algebra without an identity, let $\mathcal { A } _ { 1 } = \mathcal { A } \times \mathbb { F }$ Define algebraic operations on ${ \mathcal { A } } _ { 1 } \; b y$

(i) $(a,\alpha)+(b,\beta)=(a+b,\alpha+\beta);$

(ii) $\beta ( a , \alpha ) = ( \beta a , \beta \alpha ) ;$

(iii) $( a , \alpha ) ( b , \beta ) = ( a b + \alpha b + \beta a , \alpha \beta ) .$

Define $\| ( a , \alpha ) \| = \| a \| + | \alpha | .$ Then $\alpha _ { 1 }$ with this norm and the algebraic operations defined in $( \dot { \mathbf { i } } ) , \; ( \dot { \mathbf { i } } \dot { \mathbf { i } } )$ , and (iii) is a Banach algebra with identity $( 0 , 1 )$ and $a { \mapsto } ( a , 0 )$ is an isometric isomorphism of $\alpha$ into $\alpha _ { 1 }$

ProoF. Only (1.2) will be verified here; the remaining details are left to the reader. If $( a , \alpha ) ,   ( b , \beta )   \in   \mathcal { A } _ { 1 }$ , then $\| ( a , \alpha ) ( b , \beta ) \| = \| ( a b + \beta a + \alpha b , \alpha \beta ) \| = \| a b +$ $\beta a+\alpha b\parallel+\left|\alpha\beta\right|\leqslant\left\| a\right\|\parallel b\parallel+\left|\beta\right|\parallel a\parallel+\left|\alpha\right|\parallel b\parallel+\left|\alpha\right|\left|\beta\right|=\left\|(a,\alpha)\right\|\left\|(b,\beta)\right\|$

1.4. Example. If X is a compact space, then $\mathcal { A } = C ( X )$ is a Banach algebra if $( f g ) ( x ) = f ( x ) g ( x )$ whenever $f , g \in \mathcal { A }$ and $x   \in   X$ . Note that $\alpha$ is abelian and has an identity (the constantly 1 function).

If X is completely regular and ${ \mathcal { A } } = C _ { b } ( X ) ,$ , then $\varkappa$ is also a Banach algebra. In fact, $C _ { b } ( X ) \cong C ( \beta X ) ( \mathrm { V } . 6 )$ so that this is a special case of Example 1.4. Another special case is $l ^ { \infty }$

1.5. Example. If X is a locally compact space, $\mathcal { A } = C _ { 0 } ( X )$ is a Banach algebra when the multiplication is defined pointwise as in the preceding example. $\alpha$ is abelian, but if X is not compact, $\varkappa$ does not have an identity. If $X _ { \infty }$ is the one-point compactification of $X ,$ then $C ( X _ { \infty } ) \supseteq C _ { 0 } ( X )$ and $C ( X _ { \infty } )$ is a Banach algebra with identity.

Note that $c _ { 0 }$ is a special case of Example 1.5.

1.6. Example. If $( X , \Omega , \mu )$ is a σ-finite measure space and $\mathcal { A } = L ^ { \infty } ( X , \Omega , \mu ) ,$ then $\alpha$ is an abelian Banach algebra with identity if the operations are defined pointwise.

1.7. Example. Let $\mathcal { X }$ be a Banach space and put $\mathcal { A } = \mathcal { B } ( \mathcal { X } )$ . If multiplication is defined by composition, then $\varkappa$ is a Banach algebra with identity, 1. If dim $\mathcal { X } \geqslant 2 , \mathcal { A }$ is not abelian.

1.8. Example. If $\mathcal { X }$ is a Banach space and $\mathcal { A } = \mathcal { B } _ { 0 } ( \mathcal { X } )$ , the compact operators on $\mathcal { X } .$ then $\varkappa$ is a Banach algebra without identity if dim $\mathcal { X } = \infty$ . In fact, $\mathcal { B } _ { 0 } ( \mathcal { X } )$ is an ideal of $\mathcal { B } ( \mathcal { X } )$

Note that a special case of Example 1.7 occurs when $\mathcal { A } = M _ { n } ( \mathbb { F } )$ , the $n \times n$ matrices, where $\alpha$ is given the norm resulting when $M _ { n } ( \mathbb { F } )$ is identified with $\mathcal { B } ( \mathbf { F } ^ { n } )$

1.9. Example. Let $G$ be a locally compact topological group and let $M ( G ) = a \Pi$ finite regular Borel measures on $G .$ If $\mu , \nu   \in   M ( G )$ , define $L \colon C _ { 0 } ( G ) \to \mathbb { F }$ by

$$
L(f) = \int \int f(xy)   d\mu(x)   d\nu(y) = \int \int f(xy)   d\nu(y)   d\mu(x).
$$

Then L is a linear functional on $C _ { 0 } ( G )$ and

$$
\begin{align*}|L(f)| & \leqslant \iint \lvert f(xy) \rvert d \lvert \mu \rvert (x)   d \lvert \nu \rvert (y) \\& \leqslant \| f \| \| \mu \| \| \nu \|.\end{align*}
$$

So $L   \in   C _ { 0 } ( G ) ^ { * } = M ( G )$ . Define $\mu * \nu$ by $L ( f ) = \int f d \mu * \nu$ for f in $C _ { 0 } ( G )$ That is,

$$
\int f   d \mu * \nu = \int \int f ( x y )   d \mu ( x )   d \nu ( y ) .\tag{1.10}
$$

Note that $\lVert \boldsymbol { \mu }   \ast   \boldsymbol { \nu } \rVert = \lVert \boldsymbol { L } \rVert \leqslant \lVert \boldsymbol { \mu } \rVert \lVert \boldsymbol { \nu } \rVert$ . If follows that $M ( G )$ is a Banach algebra with this definition of multiplication. The product $\mu * \nu$ is called the convolution of $\mu$ and v.

Let $e =$ the identity of $G$ and let $\delta _ { e }   =$ the unit point mass at e. If $f \in C _ { 0 } ( G )$ then

$$
\begin{aligned}\int f d \mu * \delta_{e} &= \int f(xy)   d \mu(x)   d \delta_{e}(y) \\&= \int f(xe)   d \mu(x) \\&= \int f d \mu.\end{aligned}
$$

So $\mu   *   \delta _ { e } = \mu ;$ similarly, $\delta _ { e }   *   \mu = \mu .$ Hence $\delta _ { e }$ is the identity for $M ( G )$

If $x ,   y { \in } G ,$ then it is easy to check that $\delta _ { x }   * \delta _ { y } = \delta _ { x y }$ and $M ( G )$ is abelian if and only if G is abelian.

1.11. Example. Let G be a σ-compact locally compact group and let $m = \mathrm{r i g h t}$ Haar measure on G. That is, m is a non-negative regular Borel measure on $G$ such that $m ( U )   >   0$ for every nonempty open subset $U$ of G and $\int f(xy)dm(x)=\int f(x)dm(x)$ for every $f$ in $C _ { c } ( G )$ (the continuous functions $f ;$ $\scriptstyle { \overleftarrow { G } } \rightarrow \mathbb { F }$ with compact support). If $G$ is compact, the existence of m was established in Section V.11. If $G$ is not compact, m exists but its existence must be established by nonfunctional analytic methods. If G is not assumed to be σ-compact, then a Haar measure exists but it is not regular in the sense defined in this book. (See Nachbin [1965].)

If $f , g { \in } L ^ { 1 } ( m )$ let $\mu = f m$ and $v = g m$ as in the proof of (V.8.1). Then $\mu , v   \in   M ( G )$ and $\| \mu \| = \| f \| _ { 1 } , \quad \| \nu \| = \| g \| _ { 1 }$ . In fact, the Radon-Nikodym Theorem makes it possible to identify $L ^ { 1 } ( m )$ with a closed subspace of $M ( G )$ Is it a closed subalgebra?

Let $\phi   \in   C _ { c } ( G )$ . Then

$$
\begin{align*}\int \phi   d\mu  * \nu &= \int \int \phi(xy) f(x) g(y) dm(x) dm(y) \\&= \int g(y) \Bigg[ \int \phi(xy) f(x) dm(x) \Bigg] dm(y) \\&= \int g(y) \Bigg[ \int \phi(x) f(xy^{-1}) dm(x) \Bigg] dm(y) \\&= \int \phi(x) \Bigg[ \int f(xy^{-1}) g(y) dm(y) \Bigg] dm(x) \\&= \int \phi(x) h(x) dm(x),\end{align*}
$$

where $h ( x ) = \int f ( x y ^ { - 1 } ) g ( y ) d m ( y ) ,$ x in G. It follows that $h   \in   L ^ { 1 } ( m )$ (see Exercise 4). Thus $\mu * v = h m ,$ so $L ^ { 1 } ( m )$ is a Banach subalgebra of $M ( G )$ . In fact, the preceding discussion enables us to define $f * g$ in $L ^ { 1 } ( m ) \operatorname { f o r } f , g$ in $L ^ { 1 } ( m )$ by

$$
f * g ( x ) = \int f ( x y ^ { - 1 } ) g ( y ) d m ( y ) .
$$

The algebra $L ^ { 1 } ( m )$ is denoted by $L ^ { 1 } ( G )$

It can be shown that $L ^ { 1 } ( G )$ is abelian if and only if $G$ is abelian and $L ^ { 1 } ( G )$ has an identity if and only if G is discrete (in which case $L ^ { 1 } ( G ) = M ( G )$ —what is m?). This algebra is examined more closely in Section 9.

If $\{ \mathcal { A } _ { i } \}$ is a collection of Banach algebras, let $\oplus _ { 0 } \mathcal { A } _ { i } \equiv \{ a \in \prod _ { i } \mathcal { A } _ { i } \}$ for all $\varepsilon > 0, \left\{ i: \| a(i) \| \geqslant \varepsilon \right\}$ is finite}.

1.12. Proposition. $\mathit { I f } \{ \mathcal { A } _ { i } \}$ is a collection of Banach algebras, $\Phi _ { 0 } \mathcal { A } _ { i }$ and $\bigoplus _ { \infty } \mathcal { A } _ { i }$ are Banach algebras.

PROOF. Exercise.

## EXERCISES

1. Let  be an algebra that is also a Banach space and such that if $a \in \mathcal { A } ,$ the maps x→ax and x→xa of $\mathcal { A } \rightarrow \mathcal { A }$ are continuous. Let $\mathcal { A } _ { 1 } = \mathcal { A } \times \mathbb { F }$ as in Proposition 1.3. If $a \in \mathcal { A } ,$ define $L _ { a } \colon \mathcal { A } _ { 1 }   \to   \mathcal { A } _ { 1 }$ by $L _ { a } ( x , \xi ) = ( a x + \xi a , 0 )$ . Show that $L _ { a }   \in   \mathcal { B } ( \mathcal { A } _ { 1 } )$ and if $\| a \| = \| L _ { a } \|$ , then· is equivalent to the norm of and $\varkappa$ with · is a Banach algebra.

2. Complete the proof of Proposition 1.3.

3. Verify the statements made in Examples (1.4) through (1.9) and (1.11).

4. Let G be a locally compact group. (a) If $\phi   \in   C _ { c } ( G )$ and $\varepsilon   >   0 ,$ , show that there is an open neighborhood U of e in G such that $\| \phi _ { x } - \phi _ { y } \| < \varepsilon$ whenever $x y ^ { - 1 }   \in   U$ [Here $\phi _ { x } ( z ) = \phi ( x z ) . ]$ (b) Show that if $f   \in   L ^ { p } ( G )$ $1 \leqslant p < \infty$ , and $\varepsilon   >   0 ,$ there is an open neighborhood U of e in G such that $\| f _ { x } - f _ { y } \| _ { p } < \varepsilon$ whenever $x y ^ { - 1 }   \in   U$ . (c) Show that if $f   \in   L ^ { 1 } ( G )$ and $g { \in } L ^ { \infty } ( G )$ $h(x) = \int f(xy^{-1})g(y)dm(y)$ defines a bounded continuous function h: G →F. (d) If f, $g   \in   \dot { L } ^ { 1 } ( G )$ and h is defined as in (c), show that $h   \in   L ^ { 1 } ( G )$

5. Prove Proposition 1.12.

6. Let $\{ \mathcal { A } _ { i } ;   i { \in } I \}$ be a collection of Banach algebras. (a) Show that $\oplus _ { 0 } \mathcal { A } _ { i }$ is a closed ideal of $\oplus _ { \infty } \mathcal { A } _ { i } .$ (b) Show that $\bigoplus _ { \infty } \mathcal { A } _ { i }$ has an identity if and only if each $\mathcal { A } _ { i }$ has an identity. (c) Show that $\bigoplus _ { 0 } { \mathcal { A } } _ { i }$ has an identity if I is finite and each $\mathcal { A } _ { i }$ has an identity.

7. If X, Y are completely regular, show that $C _ { b } ( X ) \oplus _ { \infty } C _ { b } ( Y )$ is isometrically isomorphic to $C _ { b } ( X \oplus Y )$ , where X ⊕ Y is the disjoint union of X and Y.

8. If X and Y are locally compact, show that $C _ { 0 } ( X ) { \oplus } _ { \infty } C _ { 0 } ( Y )$ is isometrically isomorphic to $C _ { 0 } ( X \oplus Y )$

9. Let $\{ X _ { i } ;   i { \in } I \}$ be a collection of locally compact spaces and let X = the disjoint union of these spaces furnished with the topology $\left\{ U \subseteq X \colon U \cap X _ { i } \right.$ is open in $X _ { i }$ for all i}. Show that X is locally compact and $\oplus _ { 0 } C _ { 0 } ( X _ { i } )$ is isometrically isomorphic to $C _ { 0 } ( X )$

## §2. Ideals and Quotients

If  is an algebra, a left ideal of  is a subalgebra M of such that ax∈M whenever a∈, x∈M. A right ideal of  is a subalgebra M such that xa∈M whenever $$a { \in } { \mathcal { A } } , \thinspace x { \in } { \mathcal { M } }$$ . A (bilateral) ideal is a subalgebra of $\varkappa$ that is both a left ideal and a right ideal.

If $a \in \mathcal { A }$ and  has an identity 1, say that a is left invertible if there is an x in with $x a = 1$ . Similarly, define right invertible and invertible elements. If a is invertible and x, y∈ such that $x a = 1 = a y$ , then $y = 1 y = ( x a ) y = x ( a y ) =$ $x 1 = x$ . So if a is invertible, there is a unique element $a ^ { - 1 }$ such that $a a ^ { - 1 } = a ^ { - 1 } a = 1$

If M is a left ideal in $\mathcal { A } ,   a { \in } \mathcal { M } .$ , and a is left invertible, then $\mathcal { M } = \mathcal { A }$ In fact, if $x a = 1$ , then $1 \in \mathcal { M }$ since M is a left ideal. Thus for y in $\mathcal { A } ,   y = y \mathbb { 1 } \in \mathcal { M } .$ This forms a link between ideals and invertibility.

In the case of a Banach algebra some bonuses occur due to the interplay of the norm and the algebra. The results of this section will be for Banach algebras with an identity. To discuss invertibility this is, of course, the only feasible setting. For Banach algebras without an identity some analogous results can be obtained, however, by a consideration of the algebra obtained by adjoining an identity (1.3). The concept of a modular ideal and a modular unit can also be employed (see Exercise 6).

The next proof is based on the geometric series.

2.1. Lemma. If A is a Banach algebra with identity and $x \in \mathcal { A }$ such that $\| x - 1 \| < 1$ , then x is invertible.

PROOF. Let $y = 1 - x ;$ sO $\| y \| = r < 1$ . Since $\| y ^ { n } \| \leqslant \| y \| ^ { n } = r ^ { n } \quad \mathrm { ( W h y ? ) } ,$ $\begin{array} { r } { \sum _ { n = 0 } ^ { \infty } \| y ^ { n } \| < \infty } \end{array}$ . Hence $z = \sum_{n = 0}^{\infty} y^{n}$ converges in $\mathcal { A } . \mathrm { I f } z _ { n } = 1 + y + y ^ { 2 }$ $+ \cdots + y ^ { n } ,$

$$
z_{n}(1 - y) = (1 + y + \cdots + y^{n}) - (y + y^{2} + \cdots + y^{n + 1}) = 1 - y^{n + 1}.
$$

But $\| y^{n + 1} \| \leqslant r^{n + 1}$ , so $y ^ { n + 1 }   \to   0$ as $n   \to   \infty$ . Hence $z(1 - y) = \lim_{n \to \infty} z_n(1 - y) = 1$ Similarly, $(1 - y)z = 1.\ \mathrm{So}\ (1 - y)$ is invertible and $(1 - y)^{-1} = z = \sum_{0}^{\infty} y^{n}$ But $1 - y = 1 - (1 - x) = x.$ ■

Note that completeness was used to show that $\sum y ^ { n }$ converges.

2.2. Theorem. If A is a Banach algebra with identity, $G _ { l } = \{ a \in \mathcal { A } :$ a is left invertible}, $G_{r}=\left\{a \in \mathcal{A}:\right.$ a is right invertible}, and $G = \{ a \in \mathcal { A } :$ a is invertible}, then $G _ { l } ,   G _ { r } ,$ and G are open subsets of A. Also, the map $a   \mapsto   a ^ { - 1 }$ of $G   \rightarrow   G$ is continuous.

PROOF. Let $a _ { 0 } { \in } G _ { l }$ and let $b _ { 0 } \in \mathcal { A }$ such that $b _ { 0 } a _ { 0 } = 1$ . If $\| a - a _ { 0 } \| < \| b _ { 0 } \| ^ { - 1 }$ then $\| b _ { 0 } a - 1 \| = \| b _ { 0 } ( a - a _ { 0 } ) \| < 1$ . By the preceding lemma, $x = b _ { 0 } a$ is invertible. If $b = x ^ { - 1 } b _ { 0 } ,$ then $b a = 1$ . Hence $G _ { l } \supseteq \{ a \in \mathcal { A } : \| a - a _ { 0 } \| < \| b _ { 0 } \| ^ { - 1 } \}$ and $G _ { t }$ must be open. Similarly, G, is open. Since $G = G _ { i } \cap G _ { r } ( \mathrm { W h y ? } ) ,$ G is open.

To prove that $a { \mapsto } a ^ { - 1 }$ is a continuous map of $G   \rightarrow   G ,$ first assume that $\{ a _ { n } \}$ is a sequence in G such that $a _ { n }   \to   1$ . Let $0 < \delta < 1$ and suppose $\| a _ { n } - 1 \| < \delta$ From the preceding lemma, $a_{n}^{-1} = (1 - (1 - a_{n}))^{-1}$ $\begin{array} { r } { \sum _ { k = 0 } ^ { \infty } ( 1 - a _ { n } ) ^ { k } = 1 + \sum _ { k = 1 } ^ { \infty } ( 1 - a _ { n } ) ^ { k } } \end{array}$ . Hence

$$
\begin{aligned}\| a_n^{-1} - 1 \| &= \left\| \sum_{k=1}^{\infty} (1 - a_n)^k \right\|^2 \\&\leqslant \sum_{k=1}^{\infty} \| 1 - a_n \|^k \\&< \delta / (1 - \delta).\end{aligned}
$$

If $\varepsilon   >   0$ is given, then $\delta$ can be chosen such that $\delta / ( 1 - \delta ) < \varepsilon .$ So $\| a _ { n } - 1 \| < \delta$ implies $\| a_n^{-1} - 1 \| < \varepsilon.$ Hence lim $a _ { n } ^ { - 1 } = 1$

Now let $a { \in } G$ and suppose $\{ a _ { n } \}$ is a sequence in G such that $a _ { n }   \to   a .$ Hence $a ^ { - 1 } a _ { n }   \rightarrow   1$ . By the preceding paragraph, $a_{n}^{-1}a = (a^{-1}a_{n})^{-1} \rightarrow 1$ . Hence $a_{n}^{-1}=a_{n}^{-1}aa^{-1}\rightarrow a^{-1}$ ■

Two facts surfaced in the preceding proofs that are worth recording for the future.

2.3. Corollary. Let A be a Banach algebra with identity.

(a) If $\| a - 1 \| < 1$ , then $a^{-1} = \sum_{k = 0}^{\infty} (1 - a)^k$

(b) If $b _ { 0 } a _ { 0 } = 1$ and $\| a - a _ { 0 } \| < \| b _ { 0 } \| ^ { - 1 }$ , then a is left invertible.

A maximal ideal is a proper ideal that is contained in no larger proper ideal.

2.4. Corollary. If A is a Banach algebra with identity, then

(a) the closure of a proper left, right, or bilateral ideal is a proper left, right, or bilateral ideal;

(b) a maximal left, right, or bilateral ideal is closed

PRooF. (a) Let M be a proper left ideal and let $G _ { t }$ be the set of left-invertible elements in $\rtimes ,$ It follows that $\mathcal { M } \cap G _ { l } = \square$ . (See the introduction to this section.) Thus $\mathcal { M } \subseteq \mathcal { A } ( G _ { l } )$ By the preceding theorem, $\mathcal { A } \backslash G _ { l }$ is closed. Hence cl $\mathcal { M } \subseteq \mathcal { A } \backslash G _ { l } ;$ and thus cl $\mathcal { A } \neq \mathcal { A }$ . It is easy to check that cl $\mathcal { M }$ is an ideal. The proof of the remainder of (a) is similar.

(b) If M is a maximal left ideal, cl $\mathcal { M }$ is a proper left ideal by (a). Hence $\mathcal { M } = \mathrm { c l } \mathcal { M }$ by maximality. ■

If  does not have an identity, then $\alpha$ may contain some proper, dense ideals. For example, let $\mathcal { A } = C _ { 0 } ( \mathbb { R } )$ . Then $C _ { c } ( \mathbb { R } ) ,$ , the continuous functions with compact support, is a dense ideal in $C _ { 0 } ( \mathbb { R } )$ . There is something that can be said, however (see Exercise 6).

2.5. Proposition. If A is a Banach algebra with identity, then every proper left, right, or bilateral ideal is contained in a maximal ideal of the same type.

The proof of the preceding proposition is an exercise in the application of Zorn's Lemma and is left to the reader. Actually, this is a theorem from algebra and it is not necessary to assume that  is a Banach algebra.

Let $\varkappa$ be a Banach algebra and let M be a proper closed ideal. Note that $\alpha / M$ becomes an algebra. Indeed, $(x + \mathcal{M})(y + \mathcal{M}) = xy + \mathcal{M}$ is a well-defined multiplication on $\sigma / d .$ (Why?)

2.6. Theorem. If A is a Banach algebra and M is a proper closed ideal in $\alpha ,$ then $\sigma / M$ is a Banach algebra. If A has an identity, so does $\sigma / M$