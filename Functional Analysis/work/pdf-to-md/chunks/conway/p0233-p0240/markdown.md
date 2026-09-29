5. Suppose $A   \in   \mathcal { B } ( \mathcal { X } )$ and there is an entire function f such that $f(A) \in \mathcal{B}_0(\mathcal{X})$ . What can be said about $\sigma ( A ) ?$

6. With the terminology of Exercise 6.13, if $A \in \mathcal { B } _ { 0 } ( \mathcal { X } ) , \lambda \in \sigma ( A ) ,$ and $i \neq 0 .$ , what can be said about the index of λ?

## §8. Abelian Banach Algebras

Recall that it is assumed that every Banach algebra is over C. Also assume that all Banach algebras contain an identity.

A division algebra is an algebra such that every nonzero element has a multiplicative inverse. It may seem incongruous that the first theorem in this section allows the algebra to be nonabelian. However, the conclusion is that the algebra is abelian—and much more.

8.1. The Gelfand-Mazur Theorem. If A is a Banach algebra that is also a division ring, then $\mathcal { A } = \mathbb { C } \left( \equiv \{ \lambda \mathbf { 1 } \colon \lambda \mathbf { \in } \mathbb { C } \} \right)$

PROOF. If $a \in \mathcal { A } _ { j }$ then $\sigma ( a ) \neq \Box$ . If $\lambda   \in   \sigma ( a ) ,$ , then $a - \lambda$ has no inverse. But is a division ring, so $a - \lambda = 0$ . That is, $a = \lambda$ ■

As a corollary of the preceding theorem, the algebra of quaternions, H, is not a Banach algebra. That is, it is impossible to put a norm on H that makes it into a Banach algebra over C. Can you show this directly?

8.2. Proposition. If A is an abelian Banach algebra and M is a maximal ideal, then there is a homomorphism h: $\mathcal { A } \rightarrow \mathbb { C }$ such that $\mathcal { M } = \ker h .$ Conversely, if $h \colon { \mathcal { A } } \to \mathbb { C }$ is a nonzero homomorphism, then ker h is a maximal ideal. Moreover, this correspondence h→ker h between homomorphisms and maximal ideals is bijective.

PRooF. If M is a maximal ideal, then M is closed (2.4b). Hence $\alpha / M$ is a Banach algebra with identity. Let π: $\mathcal { A } \rightarrow \mathcal { A } / \mathcal { M }$ be the natural map. If $a \in \mathcal { A }$ and $\pi ( a )$ is not invertible in $\alpha / M$ , then $\pi ( \mathcal { A } a ) = \pi ( a ) [ \mathcal { A } / \mathcal { M } ]$ is an ideal in $\mathcal { A } / \mathcal { M }$ that is proper. Let $I = \{ b \in \mathcal { A } : \pi ( b ) \in \pi ( \mathcal { A } a ) \} = \pi ^ { - 1 } ( \pi ( \mathcal { A } a ) )$ . Then I is a proper ideal of $\varkappa$ and $\mathcal { M } \subseteq I .$ Since $\mathcal { M }$ is maximal, $\mathcal { M } = I .$ Thus $\pi ( a . \mathcal { A } ) \subseteq \pi ( I ) = \pi ( \mathcal { M } ) = ( 0 )$ . That is, $\pi ( a ) = 0 .$ This says that $\sigma / \mathcal { M }$ is a field. By the Gelfand-Mazur Theorem $\mathcal { A } / \mathcal { M } = \mathbb { C } = \{ \lambda + \mathcal { M } : \lambda \in \mathbb { C } \}$ Define $\tilde { h } ;$ $\mathcal { A } / \mathcal { M } \rightarrow \mathbb { C }$ by $\tilde { h } ( \lambda + \mathcal { M } ) = \lambda$ and define h: $\mathcal { A } \rightarrow \mathbb { C }$ by $h = \tilde { h }   \circ \pi$ Then h is a homomorphism and ker $h = \mathcal { M }$

Conversely, suppose $h \colon { \mathcal { A } }   \to   \mathbb { C }$ is a nonzero homomorphism. Then ker $h = \mathcal { M }$ is a nontrivial ideal and $\mathcal { A } / \mathcal { M } \approx \mathbb { C } . ( \mathrm { W h y ? } ) \mathrm { S o } \mathcal { M }$ is maximal.

If $h , h ^ { \prime }$ are two nonzero homomorphisms and ker h = ker h', then there is an α in C such that $h = \alpha h ^ { \prime } \left( \mathrm { A } . 1 . 4 \right)$ . But $1 = h(1) = \alpha h'(1) = \alpha, \;  so  \; h = h'.$ ■

8.3. Corollary. If A is an abelian Banach algebra and h: $\mathcal { A } \to \mathbb { C }$ is a homomorphism, then h is continuous.

ProOF. Maximal ideals are closed (2.4b).

The next result improves the preceding corollary a little. Remember that by (8.3) if h: $\mathcal { A }   \to   \mathbb { C }$ is a homomorphism, then $h \in \mathcal { A } ^ { * }$ (the Banach space dual of A).

8.4. Proposition. $\iint d$ is abelian and h: $\mathcal { A } \rightarrow \mathbb { C }$ is a non-zero homomorphism, then $\| h \| = 1$

PROOF. Let $a \in \mathcal { A }$ and put $\lambda = h(a).  If  |\lambda| > \|a\|$ , then $\| a / \lambda \| < 1$ . Hence $1 - a / \lambda$ is invertible. Let $b = ( 1 - a / \lambda ) ^ { - 1 }$ , so $1 = b(1 - a / \lambda) = b - b a / \lambda.$ Since $h ( 1 ) = 1$ $1 = h ( b - b a / \lambda ) = h ( b ) - h ( b ) h ( a ) / \lambda = h ( b ) - h ( b ) = 0 ,$ a contradiction. Hence二 $a \parallel \geqslant | \lambda | = | h ( a ) | ;$ sO $\| h \| \leqslant 1$ . Since $h(1) = 1, \| h \| = 1$

8.5. Definition. If  is an abelian Banach algebra, let Σ = the collection of all nonzero homomorphisms of $\mathcal { A } \rightarrow \mathbb { C }$ Give Σ the relative weak\* topology that it has as a subset of $\mathcal { A } ^ { * } . \Sigma$ with this topology is called the maximal ideal space of $\varkappa$

8.6. Theorem. If A is an abelian Banach algebra, then its maximal ideal space $\dot { \Sigma }$ is a compact Hausdorff space. Moreover, if $a \in \mathcal { A }$ then $\sigma ( a ) = \Sigma ( a ) \equiv$ $\{ h ( a ) : h { \in } \Sigma \}$

PROOF. Since $\Sigma \subseteq { \mathrm { b a l l } } { \mathcal { A } } ^ { * } .$ , it suffices for the proof of the first part of the theorem to show that Σ is weak\* closed. Let $\{ h _ { i } \}$ be a net in Σ and suppose h∈ball $\mathcal { A } ^ { * }$ such that $h _ { i }   \rightarrow   h$ weak\*. If $a , b \in \mathcal { A }$ , then $h(ab) = \lim_{i} h_{i}(ab) =$ lim $h _ { i } ( a ) h _ { i } ( b ) = h ( a ) h ( b )$ . So h is a homomorphism. Since $h(1) = \lim_{i} h_{i}(1) = 1$ $h { \in } \Sigma$ . Thus Σ is compact.

If $h { \in } \Sigma$ and $\lambda = h ( a )$ , then $a - \lambda \in \ker h.$ So $a - \lambda$ is not invertible and $\lambda { \in } { \sigma } ( a ) ;$ that is, $\Sigma ( a ) \subseteq \sigma ( a )$ .Now assume that $\lambda   \in   \sigma ( a ) ;$ so $a - \lambda$ is not invertible and, hence, $( a - i ) \mathcal { A }$ is a proper ideal. Let M be a maximal ideal in such that $( a - \lambda ) \mathcal { A } \subseteq \mathcal { M }$ . If $\scriptstyle { \left[ h \in \sum \right. }$ such that $\mathcal { M } = \ker h .$ then $0 = h(a - \lambda) = h(a) - \lambda;$ hence $\sigma ( a ) \subseteq \Sigma ( a ) .$ ■

Now it is time for an example. Here is one that is a little more than an example. If X is compact and $x   \in   X$ , let $\delta _ { x } : C ( X ) \to \mathbb { C }$ be defined by $\delta _ { x } ( f )   =   f ( x )$ It is easy to see that $\delta _ { x }$ is a homomorphism on the algebra $C ( X )$

8.7. Theorem. If X is compact and Σ is the maximal ideal space of $C ( X ) _ { \mathrm { i } }$ then the map $x   \mapsto   \delta _ { x }$ is a homeomorphism of X onto Σ.

PROOF. Let ∆: $X   \to   \Sigma$ be defined by $\Delta ( x ) = \delta _ { x }$ . As was pointed out before, $\Delta ( X ) \subseteq \Sigma$ . It was shown in Proposition V.6.1 that $\Delta \colon X   \to   ( \Delta ( X )$ , weak\*) is a homeomorphism. Thus it only remains to show that $\Delta ( X ) = \Sigma . \mathrm { I f } h \in \Sigma$ , then there is a measure $\mu$ in $M ( X )$ such that $h ( f ) = \int f d \mu$ for all f in $C ( X )$ . Also, $\|   \boldsymbol { \mu }   \| = \|   \boldsymbol { h }   \| = 1$ and $\mu ( X ) = \int 1   d \mu = h ( 1 ) = 1$ . Hence $\mu   \geqslant   0$ (Exercises III.7.2). Let x∈support (μ). It will be shown that $h = \delta _ { x }$

Let $\mathcal { M } = \{ f \in C ( X ) : f ( x ) = 0 \}$ . So M is a maximal ideal of C(X). Note that if it can be shown that ker $h \subseteq \mathcal { M }$ , then it must be that ker $h = \mathcal { M }$ and so $h = \delta _ { x }$ . So let f∈ker h. Because kerh is an ideal, $| f | ^ { 2 } = f { \overline { { f } } } \epsilon$ ker h. Hence $0 = h ( | f | ^ { 2 } ) = \int | f | ^ { 2 } d \mu$ Since $\mu   \geqslant   0$ and $| f | ^ { 2 } \geqslant 0 ,$ it must be that $f = 0 \mathrm { a . e . } [ \mu ]$ Since f is continuous, $f \equiv 0$ on support (μ). In particular, $f ( x )   =   0$ and so $f \in \mathcal { M }$ ■

It follows from the preceding theorem that the maximal ideals of $C ( X )$ are all of the form $\{ f { \in } C ( X ) ; f ( x ) = 0 \}$ for some x in X.

8.8. Definition. Let  be an abelian Banach algebra with maximal ideal space Σ. If $a \in \mathcal { A }$ , then the Gelfand transform of a is the function ${ \hat { a } } \colon \Sigma   \to   \mathbb { C }$ defined by $\hat { a } ( h ) = h ( a )$

8.9. Theorem. If A is an abelian Banach algebra with maximal ideal space Σ and a∈A, then the Gelfand transform of $a ,   \hat { a } ,$ belongs to C(Σ). The map a→â of A into C(Σ) is a continuous homomorphism of A into C(Σ) of norm 1 and its kernel is

$$
\bigcap \{ \mathcal { M } \colon \mathcal { M } { \mathrm { ~ i s ~ } } a { \mathrm { ~ m a x i m a l ~ i d e a l ~ o f ~ } } \mathcal { A } \} .
$$

Moreover, for each a in $\prec ,$

$$
\| \hat { a } \| _ { \infty } = \lim _ { n \rightarrow \infty } \| a ^ { n } \| ^ { 1 / n }
$$

PROOF. If $h _ { i }   \rightarrow   h$ in Σ, then $h _ { i }   \rightarrow   h$ weak\* in $\mathcal { A } ^ { * }$ . So if $a \in \mathcal { A } , \; \hat { a } ( h _ { i } ) = h _ { i } ( a ) \rightarrow$ $h ( a ) = \hat { a } ( h )$ . Thus $\hat { a }   \in   { \cal C } ( \Sigma )$

Define $\gamma \colon { \mathcal { A } }   \to   C ( \Sigma )$ by $\gamma ( a ) = { \hat { a } } .$ If $a , b \in { \mathcal { A } } ,$ then $\gamma(ab)(h)=\widehat{ab}(h)=h(ab)=$ $h ( a ) h ( b ) = { \hat { a } } ( h ) { \hat { b } } ( h )$ .Therefore $\gamma ( a b ) = \gamma ( a ) \gamma ( b )$ . It is easy to see that y is linear, so γ is a homomorphism. Also, by (8.4), if $a \in \mathcal{A}, \left| \hat{a}(h) \right| = \left| h(a) \right| \leqslant \left\| a \right\|$ ; thus $\| \gamma ( a ) \| _ { \infty } = \|   \hat { a }   \| _ { \infty } \leqslant \|   a   \|$ . So $\gamma$ is continuous and $\| \gamma \| \leqslant 1$ . Since $\gamma ( 1 )   =   1$ $\| \gamma \| = 1$

Note that a∈ker γ if and only if $\hat { a } \equiv 0 ;$ that is, a∈ker γ if and only if $h ( a ) = 0$ for each h in Σ. Thus a∈ker γ if and only if a belongs to every maximal ideal of $\varkappa$

Finally, by Theorem 8.6, if $a \in \mathcal { A } _ { j }$ then $\| \hat { a } \| _ { \infty } = \operatorname* { s u p } \{ | \lambda | : \lambda \in \sigma ( a ) \}$ . The last part of this theorem is thus a consequence of this observation and Proposition 3.8.

The homomorphism $a   \mapsto   \hat { a }$ of $\varkappa$ into C(Σ) is called the Gelfand transform of $\not { x } ,$ The kernel of the Gelfand transform is called the radical of $\alpha ,$ rad $\varkappa$ So

rad $\mathcal { A } = \cap \{ \mathcal { M } : \mathcal { M }$ is a maximal ideal of $\mathcal { A } \}$

If X is compact and $\Sigma ,$ the maximal ideal space of $C ( X ) ,$ , is identified with X as in Theorem 8.7, then the Gelfand transform $C ( X )   \to   C ( \Sigma )$ becomes the identity map.

If $\mathcal { A }$ is an abelian algebra, say that a in $\sphericalangle$ is a generator of $\varkappa$ if $\{ p ( a ) \cdot p$ is a polynomial} is dense in $\varkappa$

Recall that if τ: $X \to Y$ is a homeomorphism, then $A \colon C ( Y ) \to C ( X )$ defined by $A f = f \circ \tau$ is an isometric isomorphism (VI.2.1). Denote the relationship between A and τ by $A = \tau ^ { \# }$

8.10. Proposition. If A is an abelian Banach algebra with identity and a is a generator of $\alpha ,$ then there is a homeomorphism $\tau \colon \Sigma   \to   \sigma ( a )$ such that $i f \gamma :$ ${ \mathcal { A } }   \to   C ( \Sigma )$ is the Gelfand transform and p is a polynomial, then $\gamma ( p ( a ) ) = \tau ^ { \# } ( p )$

PROOF. Define τ: $\Sigma   \to   \sigma ( a )$ by $\tau ( h ) = h ( a )$ . By Theorem $8 . 6 ~ \tau$ is surjective. It is easy to see that τ is continuous. To see that τ is injective, suppose $\tau ( h _ { 1 } ) = \tau ( h _ { 2 } )$ sO $h _ { 1 } ( a ) = h _ { 2 } ( a )$ . Hence $h _ { 1 } ( a ^ { n } ) = h _ { 2 } ( a ^ { n } )$ for all $n \geqslant 0 .$ By linearity, $h _ { 1 } ( p ( a ) ) =$ $h _ { 2 } ( p ( a ) )$ for every polynomial $p .$ Since a is a generator for $\varkappa$ and $h _ { 1 }$ and $h _ { 2 }$ are continuous on $\mathcal { A } ,   h _ { 1 } = h _ { 2 }$ , and τ is injective. Since $\Sigma$ is compact, τ is a homeomorphism.

The remainder of the proposition follows from the fact that $\gamma$ and $\tau ^ { \# }$ are homomorphisms. Hence $\gamma(p(a))(h) = p(\gamma(a))(h) = p(\hat{a})(h) = p(\hat{a}(h)) = p(\tau(h)) =$ $\tau ^ { \# } ( p ) ( h )$

8.11. Corollary. If A has two elements $a _ { 1 }$ and $a _ { 2 }$ each of which is a generator, then $\sigma ( a _ { 1 } )$ and $\sigma ( a _ { 2 } )$ are homeomorphic.

The converse to (8.11) is not true. If $\mathcal { A } = C [ - 1 , 1 ]$ , then $f ( x ) = x$ defines a generator $f$ for $\rtimes$ If $g ( x ) = x ^ { 2 }$ , then $\sigma(g)=g([-1,1])=[0,1]$ . So $\sigma ( f )$ and $\sigma ( g )$ are homeomorphic. However, $g$ is not a generator for $\varkappa$ In fact, the Banach algebra generated by g consists of the even functions in $C [ - 1 , 1 ]$

8.12. Example. If V: $L ^ { 2 } ( 0 , 1 ) \to L ^ { 2 } ( 0 , 1 )$ is the Volterra operator and $\varkappa$ is the closure in $\mathcal { B } ( L ^ { 2 } ( 0 , 1 ) )$ of $\{ p ( V ) \colon p$ is a polynomial in $z \}$ , then $\varkappa$ is an abelian Banach algebra and rad ${ \mathcal { A } } = \operatorname { c l } \left\{ p ( V ) : p \right\}$ is a polynomial in z and $p ( 0 ) = 0 \}$ In other words, $\mathcal { A }$ has a unique maximal ideal, rad $\varkappa$ In fact, if $\mathcal { B } = \mathcal { B } ( L ^ { 2 } ( 0 , 1 ) )$ , Theorem 5.4 implies that ∂σ $\sigma ( V ) \subseteq \sigma _ { \mathcal { A } } ( V ) \subseteq \sigma _ { \mathcal { A } } ( V )$ . Since $\sigma _ { \mathcal { A } } ( V ) = \{ 0 \} \quad ( 6 . 1 4 ) , \quad \sigma _ { \mathcal { A } } ( V ) = \{ 0 \}$ . The statement above now follows by Proposition 8.10.

8.13. Example. Let $\varkappa$ be the closure in $C ( \partial \mathbf { D } )$ of the polynomials in z. If Σ is the maximal ideal space of $\alpha ,$ then $\Sigma$ is homeomorphic to $\sigma _ { \mathcal { A } } ( z )$ (Here $z$ is the function whose value at λ in ∂ID is λ.) Now $\sigma _ { \mathcal { A } } ( z ) = \mathrm { c l } \mathbb { D }$ as was shown in Example 5.1. If $f \in \mathcal { A } _ { 1 }$ then the Maximum Modulus Theorem shows that $f$ has a continuous extension to cl D that is analytic in D [see (5.1)]. Also denote this extension by $f .$ The proof of (8.10) shows that the continuous homomorphisms on $\mathcal { A }$ are of the form $f { \mapsto } f ( \lambda )$ for some $\lambda$ in cl D.

In the next section the Banach algebra $L ^ { 1 } ( G )$ is examined for a locally compact abelian group and its maximal ideals are characterized.

## EXERCISES

1. Let $\mathcal { A }$ be a Banach algebra with identity and let J be the smallest closed two-sided ideal of $\varkappa$ containing $\left\{ x y - y x : x , y { \in } { \mathcal { A } } \right\}$ . J is called the commutator ideal of $\alpha .$ (a) Show that $\mathcal { A } / J$ is an abelian Banach algebra. (b) If I is a closed ideal of $\nsim$ such that $\mathcal { A } / I$ is abelian, then $I \supseteq J .$ (c) If h: $\mathcal { A } \rightarrow \mathbb { C }$ is a homomorphism, then $J \subseteq \ker h$ and h induces a homomorphism $\tilde { h } \colon \mathcal { A } / J   \to   \mathbb { C }$ such that $\tilde { \boldsymbol { h } }   \circ   \tilde { \boldsymbol { \pi } } = \boldsymbol { h } ,$ where π: $\mathcal { A }   \rightarrow \mathcal { A } / J$ is the natural map. Hence $\| \widetilde { \boldsymbol { h } } \| = 1$ . (d) Let $\Sigma$ be the set of homomorphisms of $\mathcal { A } \rightarrow \mathbb { C }$ and let ∑ be the set of homomorphisms of $\mathcal { A } / J .$ Show that the map $h { \longmapsto } { \widetilde { h } }$ defined in (c) is a homeomorphism of $\Sigma$ onto $\tilde { \Sigma } ,$

2. Using the terminology of Exercises 2.6 and 2.7, let $\varkappa$ be an abelian Banach algebra without identity and show that if M is a maximal modular ideal, then there is a homomorphism h: $\mathcal { A } \rightarrow \mathbb { C }$ such that $\mathcal { M } = \ker h .$ Conversely, if h: $\mathcal { A }   \to   \mathbb { C }$ is a nonzero homomorphism, then ker h is a maximal modular ideal. Moreover, the correspondence $h \rightarrow$ ker h is a bijection between homomorphisms and maximal modular ideals

3. If $\mathcal { A }$ is an abelian Banach algebra and h: $\mathcal { A } \rightarrow \mathbb { C }$ is a homomorphism, then h is continuous and $\| h \| \leqslant 1$ . If  has an approximate identity $\{ e _ { i } \}$ such that $\| e _ { i } \| \leqslant 1$ for all i, then $\| \boldsymbol { h } \| = 1$ (see Exercise 2.8).

4. Let $\varkappa$ be an abelian Banach algebra and let Σ be the set of nonzero homomorphisms of $\mathcal { A }   \to   \mathbb { C }$ Show that Σ is locally compact if it has the relative weak\* topology from $\mathcal { A }$ (Exercise 3).

5. With the notation of Exercise 4, assume that $\varkappa$ has no identity and let $\alpha _ { 1 }$ be the algebra obtained by adjoining an identity. For a in $\alpha ,$ let $\sigma ( a )$ be the spectrum of a as an element of $\mathcal { A } _ { 1 }$ and show that $\sigma ( a ) = \{ h ( a ) : h \in \Sigma \} \cup \{ 0 \}$ . Also, show that the maximal ideal space of $\mathcal { A } _ { 1 } , \Sigma _ { 1 }$ , is the one-point compactification of $\Sigma .$

6. With the notation of Exercise 4, for each a in $\alpha$ define ${ \hat { a } } \colon \mathbf { \Sigma } \to \mathbf { \mathbb { C } }$ by $\hat { a } ( h ) = h ( a )$ Show that $\hat { a }   \in   \hat { C } _ { 0 } ( \Sigma )$ and the map $a   \mapsto   \hat { a }$ of $\varkappa$ into $C _ { 0 } ( \Sigma )$ is a contractive homomorphism with kernel = ∩{M: M is a maximal modular ideal of $\mathcal { A } \}$

7. If X is locally compact, show that $x   \mapsto   \delta _ { \pmb { x } }$ is a homeomorphism of X onto the maximal ideal space of $C _ { 0 } ( X )$

8. Let X be locally compact and for each open subset U of X let $C_{0}(U)=\left\{f \in C_{0}(X)\right\}$ $f ( x )   =   0$ for x in $X \backslash U \}$ . Show that $C _ { 0 } ( U )$ is a closed ideal of $C _ { 0 } ( X )$ and that every closed ideal of $C _ { 0 } ( X )$ has this form. Moreover, the map $U { \mapsto } C _ { 0 } ( U )$ is a lattice isomorphism from the lattice of open subsets of X onto the lattice of ideals of $C _ { 0 } ( X )$

9. With the notation of the preceding exercise, show that $C _ { 0 } ( U )$ is a modular ideal if and only if $X \backslash U$ is compact.

10. If $\nsim$ is an abelian Banach algebra and $a \in \mathcal { A } ,$ say that a is a rational generator of A if $\{ f ( a ) { : } f$ is a rational function with poles off $\sigma ( a ) \}$ is dense in $\varkappa$ Show that if a is a rational generator of $\alpha ,$ then Σ is homeomorphic to $\sigma ( a ) .$

11. Verify the statements made in Example 8.12

12. Say that $a _ { 1 } , \ldots , a _ { n }$ are generators of $\mathcal { A }$ if $\mathcal { A }$ is the smallest Banach algebra with identity that contains $\{ a _ { 1 } , \ldots , a _ { n } \}$ . Show that $a _ { 1 } , \ldots , a _ { n }$ are generators of $\mathcal { A }$ if and only if $\mathcal{A} = \mathrm{cl} \left\{ p(a_1, \ldots, a_n) : p \right\}$ is a polynomial in n complex variables $\left| z _ { 1 } , \ldots , z _ { n } \right\rangle$ and if Σ is the maximal ideal space, then there is a homeomorphism τ of Σ onto a compact subset K of $\mathbb { C } ^ { n }$ such that if $p$ is a polynomial in n variables, then $\gamma ( p ( a _ { 1 } , \ldots , a _ { n } ) ) = \tau ^ { \# } ( p )$

13. Verify the statements made in Example 8.13.

14. (Zelazko [1968].) Let  be an algebra and suppose $\phi \colon { \mathcal { A } }   \to   \mathbb { C }$ is a linear functional such that $\phi ( a ^ { 2 } ) = \phi ( a ) ^ { 2 }$ for all a in $\prec$ Show that $\phi$ is a homomorphism.

15. Let $\sphericalangle$ be an abelian Banach algebra with identity that is semisimple [that is, rad ${ \mathcal { A } } = ( 0 ) ] . \mathbf { I f } \parallel \cdot \parallel$ is the norm on $\mathcal { A }$ and $\| \cdot \| .$ is another norm on $\mathcal { A }$ that also makes $\sphericalangle$ into a Banach algebra, then these two norms are equivalent. (Hint: use the Closed Graph Theorem to show that the identity map $i \colon ( \mathcal { A } , \left\| \cdot \right\| ) { \rightarrow } ( \mathcal { A } , \left\| \cdot \right\| _ { 1 } )$ is continuous.)

16. Let  be as in Example 8.13 and let $K = \left\{ \phi   \in   \mathcal { A } ^ { * } \colon \phi ( 1 ) = \|   \phi   \| = 1 \right\}$ . Show that ext $K = \left\{ \delta _ { z } ; \left| z \right| = 1 \right\}$ . (See (V.7).)

17. Show that $f(x) = \exp(\pi i x)$ is a generator of $C ( [ 0 , 1 ] )$ but $g(x) = \exp(2\pi i x)$ is not.

18. Show that C(∂D) does not have a single generator though it does have a single rational generator (that is, an element a such that $\{ r ( a ) ;   r$ is a rational function with poles off $\sigma ( a ) \}$ is dense.)

## $\S 9 ^ { * }$ The Group Algebra of a Locally Compact Abelian Group

If G is a locally compact abelian group and m is Haar measure on $G ,$ then $L ^ { 1 } ( G ) \equiv L ^ { 1 } ( m )$ is a Banach algebra (Example 1.11), where for $f , g$ in $L ^ { 1 } ( G )$ the product $f * g$ is the convolution of $f$ and $g :$

$$
f * g(x) = \int_{G} f(xy^{-1})g(y)dy.
$$

Note that $d y$ is used to designate integration with respect to m rather than $d m ( y )$ . Because G is abelian, $L ^ { 1 } ( G )$ is abelian. In fact, $g * f(x) = \int g(xy^{-1})f(y)dy$ $\operatorname { I f } y ^ { -   1 } x$ is substituted for y in this integral, the value of the integral does not change because Haar measure is translation invariant. Hence $g * f ( x ) =$ $\int g(y)f(y^{-1}x)dy=\int g(y)f(xy^{-1})dy=f*g(x).$

Let $e$ denote the identity of G. If G is discrete, then $\delta _ { e } { \in } L ^ { 1 } ( G )$ and $\delta _ { e }$ is an identity for $L ^ { 1 } ( G )$ . If $G$ is not discrete, then $L ^ { 1 } ( G )$ does not have an identity (Exercise 1).

Some examples of nondiscrete locally compact abelian groups are $\mathbb { R } ^ { n }$ and $\mathbb { T } ^ { n }$ , where T = the unit circle ∂D in C with the usual multiplication. Note that $\mathbf { \bar { T } } ^ { \infty }$ is also a compact abelian group while $\mathbb { R } ^ { \infty }$ fails to be locally compact. The Cantor set can be identified with the product of a countable number of copies of $\mathbb { Z } _ { 2 }$ and is thus a compact abelian group. Indeed, the product of a countable number of finite sets (with the discrete topology) is homeomorphic to the Cantor set, so that the Cantor set has infinitely many nonisomorphic group structures.

For a topological group $G , L ^ { 1 } ( G )$ is called the group algebra for G. If G is discrete, the algebraists talk of the group algebra over a field K as the set of all $\begin{array} { r } { f = \sum _ { g \in G } a _ { g } g , } \end{array}$ where $a _ { g }   \in   K$ and $a _ { g }   \neq   0$ for at most a finite number of g in G. If $K = \mathbf { C } ,$ this is the set of functions $f \colon G   \to   \mathbb { C }$ with finite support. Thus in the discrete case the group algebra of the algebraists can be identified with a dense manifold in $L ^ { 1 } ( G ) = l ^ { 1 } ( G )$

Unlike §V.11, if $f \colon G   \to   \mathbb { C }$ and $x \in G$ , define $f _ { x } \colon G   \to   \mathbb { C }$ by $f_{x}(y) = f(yx^{-1});$ SO $f _ { x } ( y ) = f ( x ^ { - 1 } y )$ for G abelian. We want to examine the function $x   \mapsto   f _ { \pmb { x } }$ of $G \to L^{p}(G), \quad 1 \leq p < \infty$ . To do this we first prove the following (see Exercise V.11.10).

9.1. Proposition. If G is a topological group and $f \colon G   \to   \mathbb { C }$ is a continuous function with compact support, then for any $\varepsilon   >   0$ there is a neighborhood U of e such that $| f ( x ) - f ( y ) | < \varepsilon$ whenever $x ^ { - 1 } y { \in } U$

PROOF. Let $\mathcal { U }$ be the collection of open neighborhoods U of e such that $U = U ^ { - 1 }$ . Note that if V is any neighborhood of e, then $U = V \cap V^{-1} \in \mathcal{U}$ and $U \subseteq V .$ Order @ by reverse inclusion.

Suppose the result is false. Then there is an $\varepsilon   >   0$ such that for every U in U there are points $x _ { U } ,   y _ { U }$ in G with $x _ { U } ^ { - 1 } y _ { U }$ in U and $| f ( x _ { U } ) - f ( y _ { U } ) | \geqslant \varepsilon$ Note that either $x _ { U }$ or $y _ { U } { \in } K \equiv$ support f. Since $U = U ^ { - 1 }$ , we may assume that $x _ { U }   \in   K$ for every U in u. Now $\{ x _ { v } \colon U { \in } { \mathcal { U } } \}$ is a net in K. Since K is compact, there is a point x in K such that $x _ { U }   \xrightarrow [ \mathrm { ~ c l ~ } ] { \quad }   x$ . But $x _ { U } ^ { - 1 } y _ { U }   \rightarrow   e$ Since multiplication is continuous, $y_{U}=x_{U}(x_{U}^{-1}y_{U})\xrightarrow[\mathrm{c}]{\mathrm{c}}x$ Therefore if W is any neighborhood of x, there is a U in U with $x _ { U } , y _ { U } \in W$ .But f is continuous at x so W can be chosen such that $| f ( x ) - f ( w ) | < \varepsilon / 2$ whenever $w   \in   W .$ With this choice of $W , \left| f ( x _ { U } ) - f ( y _ { U } ) \right| < \varepsilon ,$ a contradiction.

One can rephrase (9.1) by saying that continuous functions on a topological group that have compact support are uniformly continuous.

In the next result it is the case $p = 1$ which is of principal interest for us at this time. The proof of the general theorem is, however, no more difficult than this special case.

9.2. Proposition. If G is a locally compact group, $1 \leqslant p < \infty$ , and $f   \in   L ^ { p } ( G )$ , then the map $x   \mapsto   f _ { \pmb { x } }$ is a continuous function from G into $L ^ { p } ( G )$

PROOF. Fix f in $L ^ { p } ( G ) ,   x$ in $G ,$ and $\varepsilon   >   0 ;$ it must be shown that there is a neighborhood V of x such that for y in V, $\| f _ { y } - f _ { x } \| _ { p } < \varepsilon .$ First note that there is a continuous function $\phi \colon G   \to   \mathbb { C }$ having compact support such that $\| f - \phi \| _ { p }   < \varepsilon / 3$ . Let $K = \operatorname { s p t } \phi$ .Note that because Haar measure is translation invariant, for any y in G, $\| f _ { y } - \phi _ { y } \| _ { p } = \| f - \phi \| _ { p } < \varepsilon / 3$ Now by Proposition 9.1, there is a neighborhood U of e such that $| \phi ( y ) - \phi ( w ) | <$ $\frac{1}{3} \varepsilon [2m(K)]^{-1/p}$ whenever $y ^ { - 1 } w   \in   U$ . Put $V = U x .$ If $y   \in   V ,$ then

$$
\| \phi _ { y } - \phi _ { x } \| _ { p } ^ { p } = \int | \phi ( z y ^ { - 1 } ) - \phi ( z x ^ { - 1 } ) | ^ { p } d z.
$$

But $y = u x$ for some u in U, so $( z y ^ { - 1 } ) ^ { - 1 } ( z x ^ { - 1 } ) = y x ^ { - 1 } = u \in U$ . Thus

$$
\begin{align*}\| \phi_y - \phi_x \|_p^p = & \int_{Ky \cup Kx} |\phi(zy^{-1}) - \phi(zx^{-1})|^p dz \\\leqslant & \left( \frac{\varepsilon}{3} \right)^p [2m(K)]^{-1} m(Ky \cup Kx) \\\leqslant & \left( \frac{\varepsilon}{3} \right)^p.\end{align*}
$$

Therefore if $y \in V, \| f_x - f_y \|_p \leqslant \| f_x - \phi_x \|_p + \| \phi_x - \phi_y \|_p + \| \phi_y - f_y \|_p < \varepsilon.$

The aim of this section is to discuss the homomorphisms on $L ^ { 1 } ( G )$ when G is abelian and to examine the Gelfand transform. There is a bit of a difficulty here since $L ^ { 1 } ( G )$ does not have an identity when G is not discrete. If $\delta _ { e }$ is the unit point mass at $e ,$ then $\delta _ { e }$ is the identity for $M ( G )$ and hence acts as an identity for $L ^ { 1 } ( G )$ . Nevertheless $\delta _ { e } { \notin } L ^ { 1 } ( G )$ if G is not discrete. All is not lost as $L ^ { 1 } ( G )$ has an approximate identity (Exercise 2.8) of a nice type.

9.3. Proposition. $I f f { \in } L ^ { 1 } ( G )$ and $\varepsilon   >   0 .$ , then there is a neighborhood U of e such that if g is a non-negative Borel function on G that vanishes off U and has $\textstyle \int   g ( x ) d x = 1$ , then $\| f - f { \star } g \| _ { 1 } < \varepsilon$

ProoF. By the preceding proposition, there is a neighborhood U of e such that $\| f - f _ { y } \| _ { 1 } < \varepsilon$ whenever $y   \in   U$ . If $g$ satisfies the conditions, then $f(x) - f * g(x) = \int \left[ f(x) - f(xy^{-1}) \right] g(y) dy$ for all x. Thus,

$$
\begin{align*}\| f - f * g \|_1 &= \int \int_{U} \left[ f(x) - f(xy^{-1}) \right] g(y) dy \Bigg| dx \\&\leqslant \int_{U} g(y) \int_{U} | f(x) - f(xy^{-1}) | dx dy \\&= \int_{U} g(y) \| f - f_y \|_1 dy \\&\leqslant \varepsilon.\end{align*}
$$

9.4. Corollary. There is a net $\{ e _ { i } \}$ of non-negative functions in $L ^ { 1 } ( G )$ such that $\int   e _ { i }   d m = 1$ for all i and $\lVert e _ { i } * f - f \lVert _ { 1 } \rightarrow 0$ for all f in $L ^ { 1 } ( G )$