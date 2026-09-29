is a \*-homomorphism, then $\nu _ { 1 } \colon { \mathcal { A } } _ { 1 }   \to   { \mathcal { C } } .$ , defined by $v_{1}(a + \alpha) = v(a) + \alpha$ for a in $\varkappa$ and α in $\mathbf { C } ,$ is a \*-homomorphism.

ProOF. It may be assumed that $\varkappa$ does not have an identity. Let $\mathcal { A } _ { 1 } = \left\{ a + \alpha \right\}$ $a \in \mathcal { A } , \alpha \in \mathbb { C } \} ( a + \alpha$ is just a formal sum). Define multiplication and addition in the obvious way. Let $( a + \alpha ) ^ { * } = a ^ { * } + { \bar { \alpha } }$ and define the norm on $\mathcal { A } _ { 1 }$ by

$$
\| a + \alpha \| = \sup \{ \| a x + \alpha x \| : x \in \mathcal{A}, \| x \| \leqslant 1 \}.
$$

Clearly, this is a norm on $\mathcal { A } _ { 1 }$ . It must be shown that $\| y ^ { \star } y \| = \| y \| ^ { 2 }$ for every y in $\mathcal { A } _ { 1 }$

Fix a in $\alpha$ and α in $\mathbf { C } . \mathrm { I f }   \varepsilon   >   0$ , then there is an x in $\varkappa$ such that $\| x \| \leqslant 1$ and

$$
\begin{align*}\| a + \alpha \|^2 - \varepsilon &< \| ax + \alpha x \|^2 = \| (x^* a^* + \bar{\alpha} x^*)(ax + \alpha x) \| \\&= \| x^* (a + \alpha)^* (a + \alpha) x \| \leq \| (a + \alpha)^* (a + \alpha) \|.\end{align*}
$$

Thus $\| a + \alpha \| ^ { 2 } \leqslant \| ( a + \alpha ) ^ { * } ( a + \alpha ) \|$

It is left to the reader to prove that the norm on $\mathcal { A } _ { 1 }$ makes $\mathcal { A } _ { 1 } \mathrm { ~ a ~ }$ Banach algebra. For the other inequality, note that $\| ( a + \alpha ) ^ { * } ( a + \alpha ) \| \leqslant$ $\| a + \alpha \| \| a + \alpha \|$ . So the proof will be complete if it can be shown that $\| ( a + \alpha ) ^ { * } \| \leqslant \| a + \alpha \|$ . Now if $x , y \in \mathcal { A }$ and $\| x \| , \| y \| \leqslant 1$ , then $\| y ( a + \alpha ) ^ { * } x \| =$ $\| y a ^ { \ast } x + { \bar { \alpha } } y x \| = \| x ^ { \ast } a y ^ { \ast } + \alpha x ^ { \ast } y ^ { \ast } \| = \| x ^ { \ast } ( a + \alpha ) y ^ { \ast } \| \leqslant \| a + \alpha \|$ . Taking the supremum over all such $x ,   y$ gives the desired inequality.

It remains to prove the statement concerning the \*-homomorphism v, that $v(a^{*}) = v(a)^{*}$ . The details are left to the reader. ■

If $\varkappa$ is a $C ^ { * } \mathtt { - a l g e b r a }$ with identity and $a \in \mathcal { A } _ { j }$ then $\sigma ( a ) ,$ the spectrum of $a ,$ is well defined. If $\varkappa$ does not have an identity, $\sigma ( a )$ is defined as the spectrum of a as an element of the $C ^ { * }$ -algebra $\alpha _ { 1 }$ obtained in Proposition 1.9.

1.10. Definition. If $\varkappa$ is a C\*-algebra and $a \in \mathcal { A } _ { j }$ , then (a) a is hermitian if $a = a^{*}; (b)$ a is normal if $a^{*}a = aa^{*};$ (c) a is unitary if $a^{*}a = aa^{*} = 1$ (this only makes sense if  has an identity).

1.11. Proposition. Let  be a $C ^ { * } .$ -algebra and let $a \in \mathcal { A }$

(a) If a is invertible, then $a ^ { * }$ is invertible and $(a^{*})^{-1} = (a^{-1})^{*}$

(b) $a = x + i y$ where x and y are hermitian elements of $\varkappa$

(c) If u is a unitary element of $\mathcal { A } ,   \| \boldsymbol { u } \| = 1$

(d) If B is a C\*-algebra and $\rho \colon { \mathcal { A } }   \to   { \mathcal { B } }$ is a \*-homomorphism, then $\| \rho ( a ) \| \leqslant \| a \|$

(e) If $a   =   a ^ { * }$ , then $\| a \| = r ( a )$

ProoF. The proofs of (a), (b), and (c) are left as exercises.

(e) Since $a ^ { * } = a , \| a ^ { 2 } \| = \| a ^ { * } a \| = \| a \| ^ { 2 } ;$ by induction, $\| a^{2^n} \| = \| a \|^{2^n}$ for $n \geqslant 1$ . That is, $\| a^{2^n} \|^{1/2^n} = \| a \|$ for $n \geqslant 1$ . Hence $r ( a ) =$ lim $\| a ^ { 2 ^ { n } } \| ^ { 1 / 2 ^ { n } } = \| a \|$

(d) If $\varkappa$ has an identity, it is not assumed that $\rho ( 1 )   = 1$ the identity of B. However, it is easy to see that $\rho ( 1 )$ is the identity for cl $\rho ( \alpha )$ . If  does not have an identity, then $\rho$ can be extended to a \*-homomorphism $\rho _ { 1 } \colon \mathcal { A } _ { 1 }   \to   \mathcal { B } _ { 1 }$ such that $\rho _ { 1 } ( 1 ) = 1 ( 1 . 9 )$ . Thus it suffices to prove the proposition under the additional assumption that $\varkappa$ and $\mathcal { B }$ have identities and $\rho ( 1 )   = 1$

$\operatorname { I f } x   \in   { \mathcal { A } } .$ , then it follows that $\sigma ( \rho ( x ) ) \subseteq \sigma ( x )   { \mathrm { ( V e r i f y ! ) } }$ and hence $r(\rho(x)) \leqslant r(x)$ $\mathbf { S o } ,$ , using part (e) and the fact that $a ^ { * } a$ is hermitian, $\| \rho ( a ) \| ^ { 2 } = \| \rho ( a ^ { * } a ) \| =$ $r(\rho(a^{*}a)) \leqslant r(a^{*}a) = \|a^{*}a\| = \|a\|^{2}$

1.12. Proposition. If A is a C\*-algebra and h: $\mathcal { A } \to \mathbb { C }$ is a non-zero homomorphism, then:

(a) $h ( a )   \in   \mathbb { R }$ whenever $a = a ^ { * }$ •D

(b) $h ( a ^ { * } ) = h ( a )$ for all a in $\mathcal { A } ;$

(c) $h ( a ^ { * } a ) \geqslant 0$ for all a in $\alpha ;$

(d) if $1 \in \mathcal { A }$ and u is unitary, then $| h ( u ) | = 1$

PRoOF. If  has no identity, extend h to $\mathcal { A } _ { 1 }$ by letting $h ( 1 ) = 1$ . Thus, we may assume that $\varkappa$ has an identity. By Exercise VII.8.1, $\| h \| = 1$ . If $a = a ^ { * }$ and $t { \in } \mathbb { R }$

$$
\begin{aligned}\| h(a + it) \|^2 & \leqslant \|   a + it \|^2 = \| (a + it)^* (a + it) \| \\& = \| (a - it) (a + it) \| \\& = \|   a^2 + t^2 \| \leqslant \|   a   \|^2 + t^2.\end{aligned}
$$

If $h ( a ) = \alpha + i \beta , \alpha , \beta$ in R, then this yields

$$
\begin{aligned}\| \boldsymbol{a} \|^2 + t^2 & \geqslant | \boldsymbol{\alpha} + i (\beta + t) |^2 \\& = \boldsymbol{\alpha}^2 + (\beta + t)^2 \\& = \boldsymbol{\alpha}^2 + \beta^2 + 2\beta t + t^2 ;\end{aligned}
$$

hence $\| a \| ^ { 2 } \geqslant \alpha ^ { 2 } + \beta ^ { 2 } + 2 \beta t$ for all t in R. If $\beta \neq 0 .$ then letting $t   \rightarrow \pm \infty$ depending on the sign of $\beta ,$ gives a contradiction. Therefore $\beta   =   0$ or $h ( a )   \in   \mathbb { R }$ This proves (a).

Let $a = x + i y ,$ , where x and y are hermitian. Since $h ( x ) , h ( y ) { \in } \mathbb { R }$ by (a) and $a ^ { \star } = x - i y$ , (b) follows. Also, $h(a^{*}a)=h(a^{*})h(a)=|h(a)|^{2}\geqslant0$ , so (c) holds. Finally, if u is unitary, $| h ( u ) | ^ { 2 } = h ( u ^ { * } ) h ( u ) = h ( u ^ { * } u ) = h ( 1 ) = 1 .$

Note that part (b) of the preceding proposition implies that any homomorphism h: $\mathcal { A } \to \mathbb { C }$ is a \*-homomorphism. This, coupled with (VII.8.6), gives the following corollary.

1.13. Corollary. If A is an abelian $C ^ { * } { \textbar } { - a l g e b r a }$ and a is a hermitian element of A, then $\sigma ( a ) \subseteq \mathbb { R }$

This corollary is short-lived as the conclusion remains valid even if $\varkappa$ is not abelian.

1.14. Proposition. Let A and B be C\*-algebras with a common identity and norm such that $\mathcal { A } \subseteq \mathcal { B }$ If $a \in \mathcal { A } ,$ then $\sigma _ { \mathcal { A } } ( a ) = \sigma _ { \mathcal { B } } ( a )$

ProoF. First assume that a is hermitian and let $\mathcal { C } = C ^ { * } ( a ) ,$ ,the C\*-algebra generated by a and 1. So $\mathcal { C }$ is abelian. By Corollary 1.13 $\sigma _ { \mathcal { C } } ( a ) \subseteq \mathbb { R }$ . By Theorem VII.5.4, $\sigma _ { \mathcal { A } } ( a ) \subseteq \sigma _ { \mathcal { C } } ( a ) = \partial \sigma _ { \mathcal { C } } ( a ) \subseteq \sigma _ { \mathcal { A } } ( a ) ;$ sO $\sigma _ { \mathcal { A } } ( a ) = \sigma _ { \mathcal { C } } ( a ) \subseteq \mathbb { R }$ . By similar reasoning, $\sigma _ { \mathcal { A } } ( a ) = \sigma _ { \mathcal { C } } ( a )$ , and hence $\sigma _ { \mathcal { A } } ( a ) = \sigma _ { \mathcal { B } } ( a ) .$

Now let a be arbitrary. It suffices to show that if a is invertible in $\mathcal { B } ,$ a is invertible in &. So suppose there is a b in  such that $ab = ba = 1$ . Thus, $( a ^ { * } a ) ( b b ^ { * } )   =   ( b b ^ { * } ) ( a ^ { * } a )   =   1$ . Since $a ^ { * } a$ is hermitian, the first part of the proof implies $a ^ { * } a$ is invertible in . But inverses are unique, so $b b ^ { * } = ( a ^ { * } a ) ^ { - 1 } \in \mathcal { A }$ Hence $b = b ( b ^ { * } a ^ { * } ) = ( b b ^ { * } ) a ^ { * } \in { \mathcal { A } }$ ■

This result must, of course, be contrasted with Theorem VII.5.4.

## EXERCISES

1. Verify the statements made in Examples 1.2 through 1.6.

2. Let ${ \mathcal { A } } = \{ f \in C ( \operatorname { c l } \mathbb { D } ) : f$ is analytic in D} and for f in  define f\* by $f ^ { * } ( z ) = { \overline { { f ( { \bar { z } } ) } } } .$ Show that $\mathcal { A }$ is a Banach algebra, $f ^ { * } \in \mathcal { A }$ when $f \in \mathcal { A } _ { 1 }$ and $\| f ^ { * } \| = \| f \|$ , but  is not a C\*-algebra.

3. If $\{ { \mathcal { A } } _ { i } ;   i { \in } I \}$ is a collection of C\*-algebras, show that $\bigoplus _ { \infty } \mathcal { A } _ { i }$ and $\oplus _ { 0 } \mathcal { A } _ { i }$ are C\*-algebras.

4. Let X be a locally compact space and let  be a C\*-algebra. If $C _ { b } ( X , { \mathcal { A } } ) = { \mathrm { t h e } }$ collection of bounded continuous functions from $X   \to   { \mathcal { A } } ,$ show that $C _ { b } ( X , { \mathcal { A } } )$ is a C\*-algebra. Let $C _ { 0 } ( X , { \mathcal { A } } ) = \mathrm { a l l }$ of the continuous functions $f \colon X   \to   { \mathcal { A } }$ such that for every $\varepsilon > 0,\left\{ x \in X:\left\| f(x) \right\| \geqslant \varepsilon \right\}$ is compact. Show that $C _ { 0 } ( X , { \mathcal { A } } )$ is a C\*-algebra.

## §2. Abelian C\*-Algebras and the Functional Calculus in C\*-Algebras

The next theorem is the basic result of this section. It will be used to develop a functional calculus for normal elements that extends the Riesz Functional Calculus.

2.1. Theorem. If A is an abelian C\*-algebra with identity and Σ is its maximal ideal space, then the Gelfand transform $\gamma \colon { \mathcal { A } } \to C ( \Sigma )$ is an isometric \*-isomorphism of A onto C(Σ).

PROOF. By Theorem VII.8.9, $\|   \hat { x }   \| _ { \infty } \leqslant \|   x   \|$ for every x in . But $\| { \hat { x } } \| _ { \infty }$ is the spectral radius of x, so by (1.11e), $\|   x   \| = \|   \hat { x }   \| _ { \infty }$ for every hermitian element x of . In particular, $\left\|   x ^ { \star } x   \right\| = \left\|   x ^ { \star } x   \right\| _ { \infty }$ for every x in .

If $a \in \mathcal { A }$ and $h { \in } \Sigma .$ then $a^{*}(h) = h(a^{*}) = \overline{h(a)} = \overline{\hat{a}(h)}$ That is, $\widehat { a } ^ { * } = \overline { { \hat { a } } } .$ Equivalently, $\gamma ( a ^ { * } ) = \gamma ( a ) ^ { * }$ since the involution on C(Σ) is defined by complex conjugation. Thus, γ is a \*-homomorphism. Also, $\| a \| ^ { 2 } = \| a ^ { * } a \| = \| \widehat { a ^ { * } a } \| _ { \infty } ^ { 2 } =$ $\|   |   | \dot { \hat { a } } | ^ { 2 } \|   _ { \infty } = \|   \dot { \hat { a } }   \|   _ { \infty } ^ { 2 }$ ; therefore $\| a \| = \| { \hat { a } } \| _ { \infty }$ and γ is an isometry.

Because γ is an isometry, it has closed range. To show that $\gamma$ is surjective, therefore, it suffices to show that it has dense range. This is accomplished by applying the Stone-Weierstrass Theorem. Note that $\hat { \mathbf { l } } = \mathbf { l }$ , so $\gamma ( \mathcal { A } )$ is a subalgebra of $C ( \Sigma )$ containing the constants. Because γ preserves the involution, $\gamma ( \alpha )$ is closed under complex conjugation. It remains to show that $\gamma ( \mathcal { A } )$ separates the points of Σ. But if $h _ { 1 }$ and $h _ { 2 }$ are distinct homomorphisms in $\Sigma .$ they are distinct because there is an a in $\varkappa$ such that $h _ { 1 } ( a ) \neq h _ { 2 } ( a )$ Hence $\hat { a } ( h _ { 1 } )   \neq   \hat { a } ( h _ { 2 } )$

By combining the preceding theorem with Proposition 1.9 and Exercise VII.8.6, the following is obtained.

2.2. Corollary. If  is an abelian $C ^ { * }$ -algebra without identity and $\Sigma$ is its maximal ideal space, then the Gelfand transform γ: $\mathcal { A }   \to   C _ { 0 } ( \Sigma )$ is an isometric \*-isomorphism of A onto $C _ { 0 } ( \Sigma )$

In order to focus our attention on the key concepts and not be distracted by peripheral considerations, we now make the following.

Assumption. All C\*-algebras that are considered have an identity.

Let $\mathcal { B }$ be an arbitrary $C ^ { * }$ -algebra and let a be a normal element of . So if ${ \mathcal { A } } = C ^ { * } ( a ) ,$ the $C ^ { * } \text {-} \mathrm { a l g e b r a }$ generated by a (and 1), $\varkappa$ is abelian. Hence ${ \mathcal { A } } \cong C ( \Sigma )$ , where Σ is the maximal ideal space of $\prec$ So by Theorem 2.1 if $f   \in   C ( \Sigma )$ , there is a unique element x of $\mathcal { A }$ such that ${ \hat { x } } = f .$ We want to think of x as $f ( a )$ and thus define a functional calculus for normal elements of a $C ^ { * } \mathtt { - a l g e b r a } .$ To be useful, however, we should have a ready way of identifying Σ. Moreover, since ${ \mathcal { A } } = C ^ { * } ( a )$ and thus depends on $a ,$ it should be that $\Sigma$ depends on a in a clear way. The idea embodied in Proposition VII.8.10 that ∑ and $\sigma ( a )$ are homeomorphic via a natural map is the key here, although (VII.8.10) is not directly applicable here since a is not a generator of $C ^ { * } ( a )$ as a Banach algebra but only as a C\*-algebra. $\operatorname { I f } a = a ^ { * }$ , then a is a generator of $C ^ { * } ( a )$ as a Banach algebra.] Nevertheless the result is true.

2.3. Proposition. If A is an abelian C\*-algebra with maximal ideal space Σ and $a \in \mathcal { A }$ such that ${ \mathcal { A } } = C ^ { * } ( a )$ , then the map τ: $\Sigma   \to   \sigma ( a )$ defined by $\tau ( h ) = h ( a )$ is a homeomorphism. If $p ( z , { \bar { z } } )$ is a polynomial in z and $\bar { z }$ and γ: ${ \mathcal { A } }   \to   C ( \Sigma )$ is the Gelfand transform, then $\gamma ( p ( a , a ^ { * } ) ) = p \circ \tau$

The proof of this result follows, with a few variations, along the lines of the proof of Proposition VII.8.10 and is left to the reader.

$\operatorname { I f } \tau \colon \Sigma   \to   \sigma ( a )$ is defined as in the preceding proposition, then $\tau ^ { \# } \colon C ( \sigma ( a ) ) \to$ $C ( \Sigma )$ is defined by $\tau ^ { \# } ( f ) = f \circ \tau$ Note that $\tau ^ { \# }$ is a \*-isomorphism and an isometry, because τ is a homeomorphism. Note that ${ \mathcal { A } } = C ^ { * } ( a )$ is the closure of $\left\{ p ( a , a ^ { \star } ) ;   p ( z , \bar { z } ) \right.$ is a polynomial in z and $\bar { z } \}$ . Now such a polynomial $p ( z , { \bar { z } } )$

is, of course, a function on $\sigma ( a ) .$ [Just evaluate the polynomial at any $z$ in $\sigma ( a ) . ]$ The last part of (2.3) says that $\gamma ( p ( a , a ^ { * } ) ) = \tau ^ { \# } ( p )$ . We define a map $\rho ;$ $C ( \sigma ( a ) )   \to   C ^ { * } ( a )$ so that the following diagram commutes:

## 2.4

![](images/page_252_image_4.jpg)

Note that if $\mathcal { B }$ is any $C ^ { * }$ -algebra and $a$ is a normal element of $\mathcal { B } ,$ then ${ \mathcal { A } } = C ^ { * } ( a )$ is an abelian $C^{*} - \mathrm{algebra}$ contained in $\mathcal { B }$ and so (2.4) applies. Moreover, in light of Proposition 1.14, the spectrum of $a$ does not depend on whether $a$ is considered as an element of $\varkappa$ or $\mathcal { B } .$ The following definition is, therefore, unambiguous.

2.5. Definition. If  is a $c ^ { * } - a ]$ lgebra with identity and a is a normal element of $\mathcal { B } ,$ let $\rho \colon C ( \sigma ( a ) ) \to C ^ { * } ( a ) \subseteq { \mathcal { B } }$ be as in (2.4). If $f { \in } C ( \sigma ( a ) )$ define

$$
f ( a ) \equiv \rho ( f ) .
$$

The map $f { \mapsto } f ( a )$ of $C ( \sigma ( a ) )   \to   \mathcal { B }$ is called the functional calculus for a.

Note that if $p ( z , { \bar { z } } )$ is a polynomial in z and $\bar { z } ,$ then $\rho ( p ( z , \bar { z } ) ) = p ( a , a ^ { * } )$ . In particular, $\rho ( z ^ { n } \bar { z } ^ { m } ) = a ^ { n } a ^ { * m }$ so that $\rho ( z ) = a$ and $\rho ( \bar { z } ) = a ^ { * }$ . Also, $\rho ( 1 )   = 1$

The properties of this functional calculus can be obtained from the fact that $\rho$ is an isometric \*-isomorphism of $C ( \sigma ( a ) )$ into $\mathcal { B }$ —with one exception. How does this functional calculus compare with the Riesz Functional Calculus? If $f \in \operatorname{HCl}(a)$ $f \mid \sigma(a) \in C(\sigma(a));$ sO $f ( a )$ has two possible interpretations. Or does it?

2.6. Theorem. If $\mathcal { B }$ is a C\*-algebra and a is a normal element of $\mathcal { B } ,$ then the functional calculus has the following properties.

(a) $f { \mapsto } f ( a )$ is a \*-monomorphism.

(b) $\| f ( a ) \| = \| f \| _ { \infty }$

(c) $f   \mapsto   f ( a )$ is an extension of the Riesz Functional Calculus.

Moreover, the functional calculus is unique in the sense that $\operatorname { i f } \tau \colon C ( \sigma ( a ) ) \to$ $C ^ { * } ( a )$ is a \*-homomorphism that extends the Riesz Functional Calculus, then $\tau ( f )   =   f ( a )$ for every f in $C ( \sigma ( a ) )$

PROOF. Let $\rho \colon C ( \sigma ( a ) )   \to   C ^ { * } ( a )$ be the map defined by $\rho ( f )   =   f ( a )$ . From (2.4), (a) and (b) are immediate.

Let π: Hol $( a )   \to   { \mathcal { A } } \subseteq { \mathcal { B } }$ denote the map defined by the Riesz Functional Calculus. Since $\rho ( z ) = \pi ( z ) = a ,$ an algebraic manipulation gives that $\rho ( f )   =$ $\pi ( f )$ for every rational function $f$ with poles off $\sigma ( a )$ . If $f \in \mathrm{HCl}(a)$ , then by Runge's Theorem there is a sequence $\{ f _ { n } \}$ of such rational functions such that $f _ { n } ( z )   \to   f ( z )$ uniformly in a neighborhood of $\sigma ( a )$ . Thus $\pi ( f _ { n } ) \to \pi ( f )$ . By (b), $\rho ( f _ { n } ) \to \rho ( f )$ . Thus $\rho ( f )   =   \pi ( f )$

To prove uniqueness, let $\tau \colon C ( \sigma ( a ) )   \to   \mathcal { B }$ be a \*-homomorphism that extends the Riesz Functional Calculus. If $f { \in } C ( \sigma ( a ) )$ , then there is a sequence $\{ p _ { n } \}$ of polynomials in z and ž such that $p _ { n } ( z , { \bar { z } } ) \to f ( z )$ uniformly on $\sigma ( a )$ But $\tau ( p _ { n } ) = p _ { n } ( a , a ^ { * } ) , \; \tau ( p _ { n } ) \to \tau ( f )$ (1.11d), and $p _ { n } ( a , a ^ { * } ) \to f ( a )$ . Hence $\tau ( f )   =   f ( a )$

Because of the uniqueness statement in the preceding theorem, it is not necessary to remember the form of the functional calculus $f { \mapsto } f ( a ) _ { : }$ , but only the fact that it is an isometric \*-monomorphism that extends the Riesz Functional Calculus. Indeed, by the uniqueness of the Riesz Functional Calculus, it suffices to have that $f { \mapsto } f ( a )$ is an isometric \*-monomorphism such that $\mathbf{i} f(z) \equiv 1$ , then $f ( a ) = 1$ , and if $f ( z ) = z$ , then $f ( a ) = a .$ Any properties or applications of the functional calculus can be derived or justified using only these properties. There may, however, be an occasion when the precise form of the functional calculus [viz., (2.4)] facilitates a proof. There are also situations in which the definition of the functional calculus gets in the way of a proof and the properties in (2.6) give the clean way of applying this powerful tool.

2.7. Spectral Mapping Theorem. $\iint \mathcal { A }$ is a C\*-algebra and a is a normal element of A, then for every f in $C ( \sigma ( a ) )$

$$
\sigma ( f ( a ) ) = f ( \sigma ( a ) ) .
$$

PROOF. Let $\rho \colon C ( \sigma ( a ) )   \to   C ^ { * } ( a )$ be defined by $\rho ( f )   =   f ( a ) .$ So $\rho$ is a \*-isomorphism. Hence $\sigma ( f ( a ) ) = \sigma ( \rho ( f ) ) = \sigma ( f )$ . But $\sigma ( f ) = f ( \sigma ( a ) )   \mathrm { ( V I I . 3 . 2 ) }$

Once again (1.14) was used implicitly in the preceding proof.

## EXERCISES

1. Prove a converse to Proposition 2.3. If K is a compact subset of $\mathbb { C } ,   C ( K )$ is a singly generated C\*-algebra.

2. If $\mathcal { A }$ is an abelian C\*-algebra with a finite number of C\*-generators $a _ { 1 } , \ldots , a _ { n } ,$ then there is a compact subset X of $\mathbb { C } ^ { n }$ and an isometric \*-isomorphism $\rho \colon \mathcal { A } \to$ C(X) such that $\rho ( a _ { k } ) = z _ { k } , 1 \leqslant k \leqslant n ,$ where $z _ { k } ( \lambda _ { 1 } , \ldots , \lambda _ { n } ) = \lambda _ { k }$ (see Exercise VII.8.12).

3. If X is a compact Hausdorff space, show that X is totally disconnected if and only if $C ( X )$ is the closed linear span of its projections (≡ hermitian idempotents).

4. Using the terminology of Exercise 3, show that if $( X , \Omega , \mu )$ is a σ-finite measure space, the maximal ideal space of $L ^ { \infty } ( X , \Omega , \mu )$ is totally disconnected.

5. If  is a C\*-algebra with identity and $a   =   a ^ { * }$ , show that $\exp ( i a ) = u$ is unitary. Is the converse true?

6. Let X be compact and fix a point $x _ { 0 }$ in X. Let $\mathcal { A } = \left\{ \left\{ f _ { n } \right\} : f _ { n } \in C ( X ) , \sup _ { n } \left\| f _ { n } \right\| < \infty \right\}$ and $\left\{ f _ { n } ( x _ { 0 } ) \right\}$ is a convergent sequence}. Show that $\nsim$ is an abelian $C^{*} - \mathrm{algebra}$ with identity and find its maximal ideal space.

7. If X is completely regular, then $C _ { b } ( X )$ is a $C ^ { * }$ -algebra and its maximal ideal space is the Stone-Čech compactification of X.

## §3. The Positive Elements in a $C ^ { * } - A I$ gebra

This section is an application of the functional calculus developed in the preceding section. The results here are very useful in the study of operators on Hilbert space and they demonstrate the power of the functional calculus.

If $\varkappa$ is a C\*-algebra, let Re  denote the hermitian elements of $\varkappa$

3.1. Definition. If $\varkappa$ is a $C ^ { * }$ -algebra and $a \in \mathcal { A }$ , then a is positive if $a \in \mathbb { R e } \mathcal { A }$ and $\sigma ( a ) \subseteq [ 0 , \infty )$ . If a is positive, this is denoted by $a   \geqslant   0 .$ Let $\varkappa$ + be the set of all positive elements of $\varkappa$

3.2. Example. If ${ \mathcal { A } } = C ( X ) .$ , then $f$ is positive in $\varkappa$ if and only if $f ( x )   \geqslant   0$ for all x in X.

3.3. Example. If $\mathcal { A } = L ^ { \infty } ( \mu )$ and $f { \in } L ^ { \infty } ( \mu )$ , then $f \geqslant 0$ if and only if $f ( x ) \geqslant 0$ a.e. [µ].

3.4. Proposition. $If a \in \mathbb{R} \setminus \mathcal{A},$ , then there are unique positive elements $u , v$ in $\varkappa$ such that $a = u - v$ and $uv = vu = 0$

PROOF. Let $f(t) = \max(t, 0), \quad g(t) = -\min(t, 0).$ Then $f , g \in C ( \mathbb { R } )$ and $f ( t ) - g ( t ) = t .$ Using the functional calculus, let $u = f ( a )$ and $v = g ( a )$ . So u and v are hermitian and by the Spectral Mapping Theorem $u , v \geqslant 0$ Also, $u - v = f(a) - g(a) = a$ and $uv = vu = (gf)(a) = 0$ since $f g \equiv 0 .$

To show uniqueness, let $u _ { 1 } , v _ { 1 } { \in } { \mathcal { A } }$ + such that $\boldsymbol { u } _ { 1 } - \boldsymbol { v } _ { 1 } = \boldsymbol { a }$ and $\boldsymbol { u } _ { 1 } \boldsymbol { v } _ { 1 } =$ $v _ { 1 } u _ { 1 } = 0$ Let $\{ p _ { n } \}$ be a sequence of polynomials such that $p _ { n } ( 0 ) = 0$ for all n and $p _ { n } ( t )   \to   f ( t )$ uniformly on $\sigma ( a )$ . Hence $p _ { n } ( a )   \rightarrow   u$ in $\varkappa$ But $u _ { 1 } a = a u _ { 1 }$ . So $u _ { 1 } p _ { n } ( a ) = p _ { n } ( a ) u _ { 1 }$ for all $n ,$ hence $\pmb { u } _ { 1 } \pmb { u } = \pmb { u } \pmb { u } _ { 1 }$ . Similarly, it follows that $a , u , v , u _ { 1 } .$ and $\nu _ { 1 } \quad \mathbf { a r e }$ pairwise commuting hermitian elements of $\varkappa$ Let $\mathcal { B } =$ the $C ^ { * } .$ -algebra generated by $a , u , v , u _ { 1 }$ , and $v _ { 1 } ;$ so $\mathcal { B }$ is abelian. Hence $\mathcal { B } \cong C ( \Sigma )$ where $\Sigma$ is the maximal ideal space of . The uniqueness now follows from the uniqueness statement for C(Σ) (Exercise 1).

The next result follows in a similar way.

3.5. Proposition. If a∈ $\mathcal { A } _ { + }$ and $n \geqslant 1$ , there is a unique element b in $\varkappa .$ such that $a = b ^ { n }$

The decomposition $a = u - v$ of a hermitian element a is sometimes called the orthogonal decomposition of a. The elements u and v are called the positive and negative parts of a and are denoted by $u = a$ + and $v = a _ { - }$ . Note that $a _ { - } \geqslant 0 .$

If $a \in \mathcal { A } _ { + }$ , then the unique b obtained in (3.5) is called the nth root of a and is denoted by $b = a ^ { 1 / n } .$ Note that if b is not assumed to be positive, it is not necessarily unique (see Exercise 5).

If X is compact and $f { \in } C ( X ) _ { + }$ , then notice that $| f ( x ) - t | \leqslant t$ for every real number $t \geqslant \| f \|$ . Conversely, if $| f ( x ) - t | \leqslant t$ for some $t \geqslant \| f \|$ , then $f ( x )   \geqslant   0$ for all x and so $f \geqslant 0 .$ These observations are behind some of the statements in the next result.

3.6. Theorem. If A is a C\*-algebra and $a \in \mathcal { A }$ , then the following statements are equivalent.

(a) $a \geqslant 0 .$

(b) $a = b ^ { 2 }$ for some b in Re A.

(c) $a = x ^ { * } x$ for some x in A.

(d) $a = a ^ { * }$ and $\| t - a \| \leqslant t \; { \it f o r ~ a l l } \; t \geqslant \| a \|$

(e) $a = a ^ { * }$ and $\| t - a \| \leqslant t$ for some $t \geqslant \| a \|$

PRooF. It is clear that (b) implies (c) and (d) implies (e). By (3.5), (a) implies (b).

$(e) \Rightarrow (a)$ Since $a = a ^ { * } ,   C ^ { * } ( a )$ is abelian. If $X = \sigma ( a ) ,   X \subseteq \mathbb { R }$ and $f   \mapsto   f ( a )$ is a \*-isomorphism of $C ( X )$ onto $C ^ { * } ( a )$ . Using this isomorphism and (e), $| t - x | \leqslant t$ for some $t \geqslant \| a \| = \sup \{ | s | : s \in X \}$ and all x in X. From the discussions preceding this theorem (with $f ( x ) = x ) ,   x \geqslant 0$ for all x in X. That is, $X = \sigma(a) \in [0, \infty)$ . Hence $a \geqslant 0$

(a)⇒(d): This proof follows the lines of the preceding paragraph and is left to the reader.

(c)⇒(a): If $a = x ^ { * } x$ for some x in , then it is clear that $a = a ^ { * }$ . Let $a = u - \mathbf { v } ,$ where $u , v \geqslant 0$ and $uv = vu = 0.$ It must be shown that $v = 0$

If $x v ^ { 1 / 2 }   =   b + i c ,$ where $b , c \in \operatorname { R e } { \mathcal { A } } ,$ then $( x v ^ { 1 / 2 } ) ^ { * } ( x v ^ { 1 / 2 } ) = ( b - i c ) ( b + i c ) =$ $b ^ { 2 } + c ^ { 2 } + i ( b c - c b )$ . But also $(x v^{1 / 2})^* (x v^{1 / 2}) = v^{1 / 2} x^* x v^{1 / 2} = v^{1 / 2} (u - v) v^{1 / 2} =$ $- v ^ { 2 }$ . Hence $i(bc - cb) = - v^{2} - b^{2} - c^{2}$ . By Proposition 3.7 below, $i ( b c - c b ) \leqslant$ 0. Also $( x v ^ { 1 / 2 } ) ^ { * } ( x v ^ { 1 / 2 } ) = - v ^ { 2 } \leqslant 0$ because (a) and (b) are equivalent. By Exercise $\mathrm { V I I } . 3 . 7 ,   ( x v ^ { 1 / 2 } ) ( x v ^ { 1 / 2 } ) ^ { * } \leqslant 0$ . Put $( x v ^ { 1 / 2 } ) ( x v ^ { 1 / 2 } ) ^ { * } = - y ,$ where $y \in \mathcal { A } _ { + } .$ $\mathrm{So}-y=(b+ic)(b-ic)=b^{2}+c^{2}-i(bc-cb)$ Hence $i(bc - cb) = b^2 + c^2 +$ $y \in \mathcal { A } _ { + }$ by (3.7). Therefore $i ( b c - c b ) \in ( - \mathcal { A } _ { + } ) \cap \mathcal { A } _ { + } = ( 0 )$ . But this implies that $- v ^ { 2 } = ( x v ^ { 1 / 2 } ) ^ { * } ( x v ^ { 1 / 2 } ) = b ^ { 2 } + c ^ { 2 } \in ( - \mathcal { A } _ { + } ) \cap \mathcal { A } _ { + }$ , so that $v ^ { 2 } = 0$ .But $v \leqslant 0$ so $v = 0$ That is, $a = u \geqslant 0$

The next result will be proved only using the equivalence of (a), (d), and (e) from the preceding theorem.

## 3.7. Proposition. If A is $a C ^ { * } \text { - } a l g e b r a _ { * }$ then $\mathcal { A } .$ , is a closed cone.

PROOF. Let $\{ a _ { n } \} \subseteq { \mathcal { A } }$ + and suppose $a _ { n }   \to   a .$ Clearly $a   \in   \mathbf { R e } \mathcal { A }$ By (3.6d),一 $\| a_n - \| a_n \| \| \leqslant \| a_n \|$ . Hence $\| a - \| a \| \| \leqslant \| a \|$ , so by $(3.6\mathrm{e}),   a \geqslant 0.$