PROOF. Let $\mathcal { U }$ be the collection of all neighborhoods of e and order $\mathcal { U }$ by reverse inclusion. Let $\mathcal { U } = \{ U _ { i } \colon i { \in } I \}$ where $i   \leqslant   j$ if and only if $U _ { i }   \subseteq   U _ { i }$ . For each i in I put $e_{i} = m(U_{i})^{-1} \chi_{U_{i}}, \mathrm{so} e_{i} \geqslant 0$ and $\int e _ { i } d m = 1$ . If $f { \in } L ^ { 1 } ( { \dot { G ) } }$ and $\varepsilon   >   0 ,$ let $U _ { i }$ be as in the preceding proposition. So $\mathrm { i f }   j   \geqslant   i ,   e _ { j }$ satisfies the conditions on g in (9.3) and hence $\| f - f   \star e _ { j } \| _ { 1 } < \varepsilon$

9.5. Corollary. If h: $L ^ { 1 } ( G )   \to   \mathbb { C }$ is a nonzero homomorphism, then h is bounded and $\| h \| = 1$

PRoOF. The fact that h is bounded and $\| h \| \leqslant 1$ is Exercise 8.3. In light of the preceding corollary if $h(f) \neq 0,   h(f) =$ lim $h ( f * e _ { i } ) = h ( f )$ lim $h ( e _ { i } )$ . Hence $h ( e _ { i } )   \rightarrow 1$ . Since $\| e _ { i } \| = 1$ for all $i ,   \| \boldsymbol { h } \| = 1$

Even though Haar measure on most of the popular examples is σ-finite, this is not true in general. For example, if D is an uncountable discrete group, the Haar measure on D is counting measure and, hence, not σ-finite. Similarly, Haar measure on $D \times \mathbb { R }$ is not $\sigma \mathrm { - f i n i t e } .$ Nevertheless, it is true that $L ^ { 1 } ( G ) ^ { * } = L ^ { \infty } ( G )$ for any locally compact group because $( G , m )$ is an example of a decomposable measure space, though $L ^ { \infty } ( G )$ must be redefined to be the equivalence classes of bounded Borel functions that are equal a.e. on every set of finite Haar measure. This fact will be assumed here. The interested reader can consult Hewitt and Ross [1963].

9.6. Theorem. If G is a locally compact abelian group and $\gamma \colon G   \to   \mathbf { T }$ is a continuous homomorphism, define $\hat { f } ( \gamma )$ by

$$
\hat { f } ( \gamma ) = \int f ( x ) \gamma ( x ^ { - 1 } ) d x
$$

for every f in $L ^ { 1 } ( G )$ . Then $f   \mapsto   { \hat { f } } ( \gamma )$ is a nonzero homomorphism on $L ^ { 1 } ( G )$ Conversely, if h: $L ^ { 1 } ( G )   \to   \mathbb { C }$ is a nonzero homomorphism, there is a continuous homomorphism $\gamma \colon G   \to   \mathbf { T }$ such that $h ( f ) = { \hat { f } } ( \gamma )$

PRoOF. First note that if $\gamma \colon G   \to   \mathbf { T }$ is a homomorphism, $\gamma ( x y ) = \gamma ( x ) \gamma ( y )$ and $\gamma(x^{-1}) = \gamma(x)^{-1} = \overline{\gamma(x)}$ , the complex conjugate of $\gamma ( x )$ If f, $g   \in   L ^ { 1 } ( G )$ , then

$$
\begin{align*}\widehat{f * g}(\gamma) &= \int (f * g)(x) \gamma(x^{-1}) dx \\&= \int \gamma(x^{-1}) \int f(xy^{-1}) g(y) dy dx \\&= \int g(y) \gamma(y^{-1}) \Bigg[ \int f(xy^{-1}) \gamma((xy^{-1})^{-1}) dx \Bigg] dy.\end{align*}
$$

But the invariance of the Haar integral gives that $\int f(xy^{-1})\gamma((xy^{-1})^{-1})dx=$ $\int f ( x ) \gamma ( x ^ { - 1 } ) d x$ Hence

$$
f * g(\gamma) = \int g(y) \gamma (y^{-1}) \left[ \int f(x) \gamma (x^{-1})   dx \right] dy = \hat{f}(\gamma) \hat{g}(\gamma).
$$

So $f   \mapsto   { \hat { f } } ( \gamma )$ is a homomorphism. Since $\gamma$ is continuous and $\gamma ( G ) \subseteq \mathbb { T } , \gamma \in L ^ { \infty } ( G )$ and $\| \gamma \| _ { \infty } = 1$ . Thus $f   \mapsto   { \hat { f } } ( \gamma )$ is not identically zero.

Now assume that h: $L ^ { 1 } ( G )   \to   \mathbb { C }$ is a nonzero homomorphism. Since h is a bounded linear functional, there is a φ in $L ^ { \infty } ( G )$ such that $h(f) = \int f(x) \phi(x)$ dx and $\phi   \|   _ { \infty } = \|   \boldsymbol { h }   \| = 1$ . If f, $g   \in   L ^ { 1 } ( G )$ then $h(f * g) = \int (f * g)(x) \phi(x) dx =$ $\int g(y)[\int f(xy^{-1})\phi(x)dx]dy=\int g(y)h(f_y)dy.$ [Note that $y   \mapsto   h ( f _ { y } )$ is a continuous scalar-valued function by Proposition 9.2.] But $h(f * g) = h(f)h(g) =$ $\int   g ( y ) h ( f ) \phi ( y ) d y$ . So

$$
0 = \int g ( y ) [ h ( f _ { y } ) - h ( f ) \phi ( y ) ] d y .
$$

for every $g$ in $L ^ { 1 } ( G )$ But $y \mapsto h ( f _ { y } ) - h ( f ) \phi ( y )$ belongs to $L ^ { \infty } ( G )$ , so for any f in $L ^ { 1 } ( G )$ 2

## 9.8

$$
h ( f _ { y } ) = h ( f ) \phi ( y )
$$

for locally almost all y in G. Pick f in $L ^ { 1 } ( G )$ such that $h ( f )   \neq   0$ By (9.8), $\phi ( y ) = h ( f _ { y } ) / h ( f )$ a.e. But the right-hand side of this equation is continuous. Hence we may assume that $\phi$ is a continuous function. Thus for every f in $L ^ { 1 } ( G )$ , (9.8) holds everywhere.

In (9.8), replace y by xy and we obtain $h(f)\phi(xy)=h(f_{xy})=h((f_x))_y$ Now replace f in (9.8) by $f _ { x }$ to get $h ( f _ { x } ) \phi ( y ) = h ( f _ { x y } )$ Thus $h(f)\phi(xy) = h(f_x)\phi(y) =$ $[ h ( f ) \phi ( x ) ] \phi ( y )$ . If $h ( f )   \neq   0 .$ , this implies $\phi ( x y ) = \phi ( x ) \phi ( y )$ for all $x , y$ in $G .$ Thus $\phi \colon G   \to   \mathbb { C }$ is a homomorphism and $| \phi ( x ) | \leqslant 1$ for all x. But $1 = \phi ( e ) = \phi ( x ) \phi ( x ^ { - 1 } ) = \phi ( x ) \phi ( x ) ^ { - 1 }$ and $| \phi ( x ) | , | \phi ( x ) ^ { - 1 } | \leqslant 1$ . Hence $| \phi ( x ) | = 1$ for all x in $G.\  If \ \gamma(x) = \phi(x^{-1})$ , then $\gamma \colon G   \to   \mathbf { T }$ is a continuous homomorphism and $h ( f ) = { \hat { f } } ( \gamma )$ for all f in $L ^ { 1 } ( G )$ ■

Let ∑ be the set of nonzero homomorphisms on $L ^ { 1 } ( G ) ,$ , where G is assumed to be abelian (both here and throughout the rest of the chapter). So ∑⊆ball $L ^ { 1 } ( G ) ^ { * }$ . If h∈ball $L ^ { 1 } ( G ) ^ { * }$ and $\{ h _ { i } \}$ is a net in Σ such that $h _ { i } \rightarrow h \mathrm { w e a k } ^ { * }$ then it is easy to see that h is multiplicative. Thus the weak\* closure of $\Sigma \subseteq \Sigma \cup \{ 0 \}$ . Hence the relative wea $\mathbf { k } ^ { * }$ topology on Σ makes Σ into a locally compact Hausdorff space (see Exercise 8.4)

Let Γ = all the continuous homomorphisms $\gamma \colon G   \to   \mathbf { T } ,$ By Theorem 9.6, Σ and Γ can be identified using formula (9.7). In fact, the map defined in (9.7) is the Gelfand transform when this identification is made. (Just look at the definitions.) Since Σ and Γ are identified and Σ has a topology, Γ can be given a topology. Thus $\Gamma$ becomes a locally compact space with this topology. (For another description of the topology, see Exercise 6.) The functions in Γ are called characters and are sometimes denoted by $\Gamma = \hat { G }$ and called the dual group.

Also notice that in a natural way Γ is a group. If $\gamma _ { 1 } , \gamma _ { 2 }   \in   \Gamma$ , then $( \gamma _ { 1 } \gamma _ { 2 } ) ( x ) \equiv \gamma _ { 1 } ( x ) \gamma _ { 2 } ( x )$ and $\gamma _ { 1 } \gamma _ { 2 }   \in   \Gamma$

## 9.9. Proposition. Γ is a locally compact abelian group.

Clearly Γ is an abelian group and we know that Γ is a locally compact space. It must be shown that Γ is a topological group. To do this we first prove a lemma.

## 9.10. Lemma.

(a) The map $( x , \gamma ) { \mapsto } \gamma ( x )$ of $G \times \Gamma   \rightarrow   \mathfrak { T }$ is continuous.

(b) If $\{ \gamma _ { i } \}$ is a net in Γ and $\gamma _ { i }   \rightarrow   \gamma$ in Γ, then $\gamma _ { i } ( x )   \rightarrow   \gamma ( x )$ uniformly for x belonging to any compact subset of G.

PRoOF. First note that if $x   \in   G$ and $f { \in } L ^ { 1 } ( G )$ , then for every γ in Γ,

$$
\begin{aligned} \hat{f}_{x}(\gamma) &= \int f_{x}(y)\gamma(y^{-\frac{1}{1}})dy \\&= \int f(yx^{-\frac{1}{1}})\gamma(y^{-\frac{1}{1}})dy \\&= \int f(z)\gamma(z^{-\frac{1}{1}}x^{-\frac{1}{1}})dz \\&= \gamma(x^{-\frac{1}{1}})\hat{f}(\gamma).\\ \end{aligned}
$$

So if $\gamma _ { i }   \rightarrow   \gamma$ in Γ and $x _ { i }   \to   { \pmb x }$ in G,

$$
\begin{array} { r l } & { | \hat { f } ( \gamma _ { i } ) \gamma _ { i } ( x _ { i } ) - \hat { f } ( \gamma ) \gamma ( x ) | = | \hat { f } _ { x _ { i } ^ { - 1 } } ( \gamma _ { i } ) - \hat { f } _ { x ^ { - 1 } } ( \gamma ) | } \\ & { \quad \leqslant | \hat { f } _ { x _ { i } ^ { - 1 } } ( \gamma _ { i } ) - \hat { f } _ { x ^ { - 1 } } ( \gamma _ { i } ) | + | \hat { f } _ { x ^ { - 1 } } ( \gamma _ { i } ) - \hat { f } _ { x ^ { - 1 } } ( \gamma ) | . } \end{array}
$$

But $| \hat { f } _ { x _ { i } ^ { - 1 } } ( \gamma _ { i } ) - \hat { f } _ { x ^ { - 1 } } ( \gamma _ { i } ) | \leqslant \| f _ { x _ { i } ^ { - 1 } } - f _ { x ^ { - 1 } } \| _ { 1 } \rightarrow 0$ by (9.2). Because $f _ { x ^ { - 1 } } \in L ^ { 1 } ( G )$ $\hat { f } _ { x ^ { - 1 } } ( \gamma _ { i } ) \xrightarrow { \cdot } \hat { f } _ { x ^ { - 1 } } ( \gamma )$ since $\gamma _ { i }   \rightarrow   \gamma$ Thus $\hat { f } ( \gamma _ { i } ) \gamma _ { i } ( x _ { i } )   \rightarrow \hat { f } ( \gamma ) \gamma ( x )$ . If f is chosen so that $\hat { f } ( \gamma ) \neq 0 ,$ then because $\hat { f } ( \gamma _ { i } )   \rightarrow \hat { f } ( \gamma )$ , there is an $i _ { 0 }$ such that $\hat { f } ( \gamma _ { i } )   \neq   0$ for $i \geqslant i _ { 0 }$ Therefore $\gamma _ { i } ( x _ { i } )   \rightarrow   \gamma ( x )$ and (a) is proven.

Now let K be a compact subset of G and let $\{ \gamma _ { i } \}$ be a net in Γ such that $\gamma _ { i }   \rightarrow   \gamma _ { 0 }$ . Suppose $\{ \gamma _ { i } ( x ) \}$ does not converge uniformly on K to $\gamma _ { 0 } ( x )$ Then there is an $\varepsilon   >   0$ such that for every i, there is a $j _ { i }   \geqslant   i$ and an $x _ { i }$ in K such that $| \gamma _ { j _ { i } } ( x _ { i } ) - \gamma _ { 0 } ( x _ { i } ) | \geqslant \varepsilon .$ Now $\{ \gamma _ { j _ { i } } \}$ is a net and $\gamma _ { j _ { i } }   \rightarrow   \gamma _ { 0 }$ (Exercise). Since K is compact, there is an $x _ { 0 }$ in K such that $x _ { i }   \xrightarrow [ \mathrm { ~ c l ~ } ] { \quad }   x _ { 0 }$ . Now part (a) implies that the map $( x , \gamma ) { \mapsto } ( \gamma ( x ) , \gamma _ { 0 } ( x ) )$ of $G \times \Gamma$ into T × T is continuous. Since $(x_{i}, \gamma_{j_{i}}) \xrightarrow[\mathrm{cl}]{\quad} (x_{0}, \gamma_{0})$ in $G \times \Gamma , ( \gamma _ { j _ { i } } ( x _ { i } ) , \gamma _ { 0 } ( x _ { i } ) ) \xrightarrow [ \mathrm { c l } ] { } ( \gamma _ { 0 } ( x _ { 0 } ) , \gamma _ { 0 } ( x _ { 0 } ) )$ . So for any $i _ { 0 } ,$ there is an $i \geqslant i _ { 0 }$ such that $| \gamma _ { j _ { i } } ( x _ { i } ) - \gamma _ { 0 } ( x _ { 0 } ) | \stackrel { \sim } { < } \varepsilon / 2$ and $| \gamma _ { 0 } ( x _ { i } ) - \gamma _ { 0 } ( x _ { 0 } ) | < \varepsilon / 2$ Hence $| \gamma _ { j _ { i } } ( x _ { i } ) - \gamma _ { 0 } ( x _ { i } ) | < \varepsilon ,$ a contradiction.

PROOF OF PROPOSITION 9.9. Let $\{ \gamma _ { i } \} , \{ \lambda _ { i } \}$ be nets in Γ such that $\gamma _ { i }   \rightarrow   \gamma$ and $\lambda _ { i }   \rightarrow   \lambda _ { i }$ It must be shown that $\gamma_{i}\lambda_{i}^{-1}\rightarrow\gamma\lambda^{-1}$ . Let $\phi   \in   C _ { c } ( G )$ and put $K = \operatorname { s p t } \phi$

Then $\hat { \phi } ( \gamma _ { i } \lambda _ { i } ^ { - 1 } ) = \int _ { K } \phi ( x ) \gamma _ { i } ( x ^ { - 1 } ) \lambda _ { i } ( x ) d x$ .By the preceding lemma, $\gamma _ { i } ( x ^ { - 1 } )   \rightarrow$ $\gamma ( { x ^ { - } } ^ { 1 } )$ and $\lambda _ { i } ( x )   \rightarrow   \lambda ( x )$ uniformly for x in K. Thus $\hat { \phi } ( \gamma _ { i } \lambda _ { i } ^ { - 1 } )   \rightarrow   \hat { \phi } ( \gamma \lambda ^ { - 1 } )$ . If $f { \in } L ^ { 1 } ( G )$ and $\varepsilon   >   0 .$ let $\phi   \in   C _ { c } ( G )$ such that $\|   f - \phi   \| _ { 1 } < \varepsilon / 3$ Then

$$
| \hat { f } ( \gamma _ { i } \lambda _ { i } ^ { - 1 } ) - \hat { f } ( \gamma \lambda ^ { - 1 } ) | < \frac { 2 \varepsilon } { 3 } + | \hat { \phi } ( \gamma _ { i } \lambda _ { i } ^ { - 1 } ) - \hat { \phi } ( \gamma \lambda ^ { - 1 } ) | .
$$

It follows that $\hat { f } ( \gamma _ { i } \lambda _ { i } ^ { - 1 } )   \rightarrow   \hat { f } ( \gamma \lambda ^ { - 1 } )$ for every f in $L ^ { 1 } ( G )$ . Hence $\gamma _ { i } \lambda _ { i } ^ { - 1 }   \rightarrow   \gamma \lambda ^ { - 1 }$ in Γ.

Since Γ is a locally compact abelian group, it too has a dual group. Let $\hat { \Gamma }$ be this dual group. If $x   \in   G _ { i }$ define $\rho ( x ) \colon \Gamma   \to   \mathfrak { T }$ by $\rho ( x ) ( \gamma ) = \gamma ( x )$ . It is easy to see that $\rho$ is a homomorphism. It is a rather deep fact, entitled the Pontryagin Duality Theorem, that $\rho \colon G   \to   \hat { \Gamma }$ is a homeomorphism and an isomorphism. That is, $G \mathrm { { ` ` } 1 \mathrm { { S } } ^ { \mathrm { { ' } ^ { \prime } } } }$ the dual group of its dual group. The interested reader may consult Rudin [1962]. We turn now to some examples.

9.11. Theorem. $\scriptstyle { \boldsymbol { I } } { \boldsymbol { f } }   { \boldsymbol { y } } \in \mathbf { R }$ , then $\gamma _ { y } ( x ) = e ^ { i x y }$ defines a character on R and every character on R has this form. The map $y   \mapsto   \gamma _ { y }$ is a homeomorphism and an isomorphism of R onto $\hat { \mathbf { R } }$ $\scriptstyle { \boldsymbol { I } } { \boldsymbol { f } } \; y \in \mathbb { R }$ and $f   \in   L ^ { 1 } ( \dot { \mathbb { R } } )$ , then

## 9.12

$$
\hat { f } ( \gamma _ { y } ) = \hat { f } ( y ) = \int _ { - \infty } ^ { \infty } f ( x ) e ^ { - i x y } d x ,
$$

the Fourier transform of f.

PROOF. If $y   \in   \mathbb { R }$ , then $| \gamma _ { y } ( x ) | = 1$ for all x and $\gamma _ { y } ( x _ { 1 } + x _ { 2 } ) = \gamma _ { y } ( x _ { 1 } ) \gamma _ { y } ( x _ { 2 } )$ So $\gamma _ { y }   \in   \hat { \mathbb { R } } _ { j }$ Also, $\gamma _ { y _ { 1 } + y _ { 2 } } ( x ) = \gamma _ { y _ { 1 } } ( x ) \gamma _ { y _ { 2 } } ( x )$ . Hence $y   \mapsto   \gamma _ { y }$ is a homomorphism of IR into Ř.

Now let $$\gamma { \in } \hat { \mathbb { R } } .$ $\gamma ( 0 ) = 1$$ so that there is a $\delta > 0$ such that $\int _ { 0 } ^ { \delta } \gamma ( x ) d x = a \neq 0 .$ Thus

$$
\begin{aligned}a \gamma (x) &= \gamma (x) \int_{0}^{\delta} \gamma (t) dt \\&= \int_{0}^{\delta} \gamma (x + t) dt \\&= \int_{x}^{x + \delta} \gamma (t) dt.\end{aligned}
$$

Hence $\gamma(x)=a^{-1}\int_{x}^{x+\delta}\gamma(t)dt$ Because γ is continuous, the Fundamental Theorem of Calculus implies that γ is differentiable. Also,

$$
\frac{\gamma(x + h) - \gamma(x)}{h} = \gamma(x) \left[ \frac{\gamma(h) - 1}{h} \right].
$$

So $\gamma ^ { \prime } ( x ) = \gamma ^ { \prime } ( 0 ) \gamma ( x )$ . Since $\gamma ( 0 ) = 1$ and $| \gamma ( x ) | = 1$ for all x, the elementary theory of differential equations implies that $\gamma = \gamma _ { y }$ for some y in $\mathbb { R }$ This implies that $y   \mapsto   \gamma _ { y }$ is an isomorphism of R onto R.

It is clear from (9.7) that (9.12) holds. From here it is easy to see that $y   \mapsto   \gamma _ { y }$ is a homeomorphism of R onto $\hat { \mathbb { R } }$ ■

So the preceding result says that R is its own dual group. Because of (9.12), the function $\widehat { f }$ as defined in (9.7) is called the Fourier transform of $f .$ The next result lends more weight to the use of this terminology.

9.13. Theorem. $\scriptstyle { \boldsymbol { I } } \scriptstyle { \boldsymbol { f } } \scriptstyle { \boldsymbol { n } } \in \mathbb { Z } ,$ define $\gamma _ { n } ; \mathbf { T }   \rightarrow   \mathbf { T }$ by $\gamma _ { n } ( z ) = z ^ { n }$ .Then $\gamma _ { n } \in \widehat { \mathbb { T } }$ and the map $n   \mapsto   \gamma _ { n }$ is a homeomorphism and an isomorphism of $\mathbb { Z }$ onto Î. If $n { \in } \mathbb { Z }$ and $f { \in } L ^ { 1 } ( \mathbf { \bar { H } } )$ , then

## 9.14

$$
\hat { f } ( \gamma _ { n } ) = \hat { f } ( n ) \equiv \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( e ^ { i \theta } ) e ^ { - i n \theta } d \theta.
$$

ProoF. It is left to the reader to check that $\gamma _ { n } \in \hat { \mathbf { I } }$ and $n   \mapsto   \gamma _ { n }$ is an injective homomorphism of Z into $\hat { \mathbf { T } }$ If $\gamma \in \hat { \mathbf { \Pi } }$ , define $\sigma \colon \mathbb { R } \to \mathbb { T }$ by $\sigma ( t ) = \gamma ( e ^ { i t } ) ;$ it follows that $\sigma   \in   \hat { \mathbb { R } }$ . By (9.11), $\sigma ( t ) = e ^ { i y t }$ for some y in R. But $\sigma(t + 2\pi) = \sigma(t)$ sO $e ^ { 2 \pi i y } = 1$ . Hence $y = n   \in   \mathbb { Z } .$ Thus $\gamma ( e ^ { i \theta } ) = \sigma ( \theta ) = e ^ { i n \theta } , \gamma = \gamma _ { n } ,$ and $n   \mapsto   \gamma _ { n }$ is an isomorphism of $\mathbf { z }$ onto $\hat { \mathbf { T } }$ Formula (9.14) is immediate from (9.7). The fact that $n   \mapsto   \gamma _ { n }$ is a homeomorphism is left as an exercise.

So $\mathbf { \hat { \mathbb { T } } } = \mathbf { \mathbb { Z } } ,$ a discrete group. This can be generalized.

9.15. Theorem. $I f   G$ is compact, $\hat { G }$ is discrete; if G is discrete, $\hat { G }$ is compact.

PROOF. Put $\Gamma = { \hat { G } } ,$ If G is discrete, then $L ^ { 1 } ( G )$ has an identity. Hence its maximal ideal space is compact. That is, Γ is compact.

Now assume that $G$ is compact. Hence $\Gamma \subseteq L ^ { 1 } ( G )$ since $m ( G ) = 1$ . Suppose $\gamma   \in   \Gamma$ and $\gamma \neq$ the identity for $\Gamma ,$ then there is a point $x _ { 0 }$ in $G$ such that $\gamma ( x _ { 0 } ) \neq 1$ . Thus

$$
\begin{aligned}\int \gamma(x)dx &= \int \gamma(xx_{0}^{-1}x_{0})dx \\&= \gamma(x_{0})\int \gamma(xx_{0}^{-1})dx \\&= \gamma(x_{0})\int \gamma(x)dx,\end{aligned}
$$

since Haar measure is translation invariant. Since $\gamma ( x _ { 0 } ) \neq 1$ , this implies that

$$
\int _ { G } \gamma ( x ) d x = 0 \qquad \mathrm { i f } \gamma \neq 1 .
$$

Of course if $\gamma = 1 , \int 1   dx = m(G) = 1$ . So if $f = 1$ on $G , \quad f { \in } L ^ { 1 } ( G )$ and $\hat { f } ( \gamma ) = \int \gamma ( x ^ { - 1 } ) d x = \chi _ { \{ 1 \} } ( \gamma )$ . Since $\hat { f }$ is continuous on $\Gamma , \{ 1 \}$ is an open set. By translation, every singleton set in Γ is open and hence Γ is discrete.

9.16. Theorem. $\scriptstyle { \boldsymbol { I } } \scriptstyle { \boldsymbol { f } }   { \boldsymbol { a } } \in \mathbf { T } .$ define $\gamma _ { a } \colon \mathbb { Z } \to \mathbb { T }$ by $\gamma _ { a } ( n ) = a ^ { n }$ . Then $\gamma _ { a }   \in   \hat { \mathbb { Z } }$ and the map $a   \mapsto   \gamma _ { a }$ is a homeomorphism and an isomorphism of T onto $\hat { z } .$ If $a   \in   \mathbf { T }$ and $f { \in } L ^ { 1 } ( \mathbb { Z } ) = l ^ { 1 } ( \mathbb { Z } )$ , then

## 9.17

$$
\hat { f } ( \gamma _ { a } ) = \hat { f } ( a ) = \sum _ { n = - \infty } ^ { \infty } f ( n ) a ^ { - n } .
$$

PROOF. Again the proof that $a   \mapsto   \gamma _ { a }$ is a monomorphism of $\mathbf { T }   \rightarrow   \hat { \mathbb { Z } }$ is left to the reader. If $\gamma \in \widehat { \mathbb { Z } } _ { 1 }$ let $\gamma ( 1 ) = a   \in   \mathbf { T }$ . Also, $\gamma ( n ) = \gamma ( 1 ) ^ { n } = a ^ { n }$ SO $\gamma = \gamma _ { a }$ . Hence $a   \mapsto   \gamma _ { a }$ is an isomorphism. It is easy to show that this map is continuous and hence, by compactness, a homeomorphism

For additional reading, consult Rudin [1962]

## EXERCISES

1. Prove that if $L ^ { 1 } ( G )$ has an identity, then G is discrete.

2. If $f   \in   L ^ { \infty } ( G )$ , show that $x   \mapsto   f _ { x }$ is a continuous function from G into $( L ^ { \infty } ( G ) , \mathbf { w } \mathbf { k } ^ { * } )$

3. Is there a measure $\mu$ on R different from Lebesgue measure such that for $f$ in $L ^ { 1 } ( \mu ) , x   \mapsto   f _ { x }$ is continuous? Is there a measure for which this map is discontinuous?

4. If $f   \in   { \cal C } _ { 0 } ( G )$ , show that $x   \mapsto   f _ { x }$ is a continuous map from $G   \rightarrow   { \cal C } _ { 0 } ( G )$

5. If $f   \in   L ^ { \infty } ( G )$ and f is uniformly continuous on G, show that $x   \mapsto   f _ { x }$ is a continuous function from $G   \to   L ^ { \infty } ( G )$ . Is the converse true? See Edwards [1961].

6. If K is a compact subset of $G , \gamma _ { 0 } { \in } \Gamma$ ,and $\varepsilon > 0 ,$ let $U ( K , \gamma _ { 0 } , \varepsilon ) = \{ \gamma \in \Gamma :$ $| \gamma ( x ) - \gamma _ { 0 } ( x ) | < \varepsilon$ for all x in $| K \}$ . Show that the collection of all such sets is a base for the topology of Γ. (This says that the topology on $\Gamma$ is the compact-open topology.)

7. Show that there is a discontinuous homomorphism $\gamma \colon \mathbb { R }   \to   \mathbb { T } . { \mathrm { ~ I f ~ } } \gamma \colon \mathbb { R }   \to   \mathbb { T }$ is a homomorphism that is a Borel function, show that $\gamma$ is continuous.

8. If G is a compact abelian group, show that the linear span of Γ is dense in $C ( G )$

9. If G is a compact abelian group, show that Γ forms an orthonormal basis in $L ^ { 2 } ( G )$

10. If G is a compact abelian group, show that G is metrizable if and only if Γ is countable.

11. Let $\{ G _ { \alpha } \}$ be a family of compact abelian groups and $G = \Pi _ { \alpha } G _ { \alpha } . \mathrm { I f } \Gamma _ { \alpha } = \hat { G } _ { \alpha }$ , show that the character group of G is $\left\{ \left\{ \gamma _ { \mathfrak { a } } \right\} \in \mathbf { \Pi } _ { \mathfrak { a } } \mathbf { \Gamma } _ { \mathfrak { a } } \colon \gamma _ { \mathfrak { a } } = e \right.$ except for at most a finite number of $\alpha \}$

C\*-Algebras

A C\*-algebra is a particular type of Banach algebra that is intimately connected with the theory of operators on a Hilbert space. If $\mathcal { H }$ is a Hilbert space, then $\mathcal { B } ( \mathcal { H } )$ is an example of a $C ^ { * }$ -algebra. Moreover, if $\varkappa$ is any $C ^ { * } \text {-} \mathrm { a l g e b r a } ,$ , then it is isomorphic to a subalgebra of $\mathcal { B } ( \mathcal { H } )$ (see Section 5). Some of the general theory developed in this chapter will be used in the next chapter to prove the Spectral Theorem, which reveals the structure of normal operators.

A more thorough treatment of $C ^ { * } .$ -algebras is available in Arveson [1976] or Sakai [1971].

## §1. Elementary Properties and Examples

If  is a Banach algebra, an involution is a map $a   \mapsto   a ^ { * }$ of $\varkappa$ into $\varkappa$ such that the following properties hold for a and b in $\varkappa$ and α in $\mathfrak { C } ;$

(i) $( a ^ { * } ) ^ { * } = a ;$

(ii) $( a b ) ^ { * } = b ^ { * } a ^ { * } ;$

(iii) $( \alpha a + b ) ^ { \star } = { \bar { \alpha } } a ^ { \star } + b ^ { \star } .$

Note that if $\varkappa$ has involution and an identity, then $1^{*} \cdot a = (1^{*} \cdot a)^{*} =$ $( a ^ { * }   \cdot   1 ) ^ { * } = ( a ^ { * } ) ^ { * } = a ;$ similarly, $a \cdot 1 ^ { * } = a .$ Since the identity is unique, $1 ^ { * } = 1$ Also, for any α in $\alpha ^ { * } = \alpha$

1.1. Definition. A C\*-algebra is a Banach algebra $\varkappa$ with an involution such that for every a in $\varkappa$

$$
\| a ^ { \star } a \| = \| a \| ^ { 2 } .
$$

1.2. Example. If $\mathcal { H }$ is a Hilbert space, $\mathcal { A } = \mathcal { B } ( \mathcal { H } )$ is a $C ^ { * }$ -algebra where for each A in $\mathcal { B } ( \mathcal { H } ) ,   A ^ { * } = \mathrm { t h e }$ adjoint of A. (See Proposition II.2.7.)

1.3. Example. If $\mathcal { H }$ is a Hilbert space, $\mathcal { B } _ { 0 } ( \mathcal { H } )$ is a $C ^ { * }$ -subalgebra of $\mathcal { B } ( \mathcal { H } )$ though $\mathcal { B } _ { 0 } ( \mathcal { H } )$ does not have an identity if $\mathcal { H }$ is infinite dimensional.

1.4. Example. If X is a compact space, $C ( X )$ is a $C ^ { * } .$ -algebra where $f ^ { * } ( x ) = { \overline { { f ( x ) } } }$ for f in C(X) and x in X.

1.5. Example. If $( X , \Omega , \mu )$ is a σ-finite measure space, $L ^ { \infty } ( X , \Omega , \mu )$ is a C\*-algebra where the involution is defined as in (1.4)

1.6. Example. If X is locally compact but not compact, $C _ { 0 } ( X )$ is a $C ^ { * }$ -algebra without identity.

1.7. Proposition. If  is $a ~ C ^ { * }$ -algebra and $a \in \mathcal { A } _ { 2 }$ then $\| a ^ { \star } \| = \| a \|$

PROOF. Note that $\| a \| ^ { 2 } = \| a ^ { \star } a \| \leqslant \| a ^ { \star } \| \| a \| ;$ sO $\| a \| \leqslant \| a ^ { * } \|$ . Since $a = a ^ { * * } .$ substituting $a ^ { * }$ for a in this inequality gives $\| a ^ { \star } \| \leqslant \| a \|$ ■

1.8. Proposition. $\mathit { I f . 3 1 }$ is a C\*-algebra and $a \in \mathcal { A } _ { i }$ then

$$
\begin{aligned}\| a \| = \sup \{ \| a x \| : x \in \mathcal{A}, \| x \| \leqslant 1 \} \\= \sup \{ \| x a \| : x \in \mathcal{A}, \| x \| \leqslant 1 \}.\end{aligned}
$$

PROOF. Let $\alpha = \sup \left\{ \| a x \| : x \in \mathcal{A}, \| x \| \leqslant 1 \right\}$ . Then $\| a x \| \leqslant \| a \| \| x \|$ for any x in $\mathcal { A } ;$ hence $\alpha \leqslant \| a \|$ . If $x = a ^ { * } / \| a \|$ , then $\| x \| = 1$ by the preceding proposition. For this x, $\| a x \| = \| a \|$ , so $\alpha = \| a \|$ . The proof of the other equality is similar. ■

This last proposition has an alternative formulation that is useful. If $a \in \mathcal { A } _ { j }$ define $L _ { a } \colon { \mathcal { A } }   \to   { \mathcal { A } }$ by $L _ { a } ( x )   =   a x$ . By $( 1 . 8 ) ,   L _ { a } { \in } { \mathcal { B } } ( { \mathcal { A } } )$ and $\| L _ { a } \| = \| a \|$ . If $\rho ;$ $\mathcal { A }   \rightarrow   \mathcal { B } ( \mathcal { A } )$ is defined by $\rho ( a )   =   L _ { a } ,$ then $\rho$ is a homomorphism and an isometry. That is, $\mathcal { A }$ is isometrically isomorphic to a subalgebra of $\mathcal { B } ( \mathcal { A } )$ The map $\rho$ is called the left regular representation of $\varkappa$

The left regular representation can be used to discuss the process of adjoining an identity to $\measuredangle ,$ Since $\mathcal { A }$ is isomorphic to a subalgebra $\mathcal { B } ( \mathcal { A } )$ and $\mathcal { B } ( \mathcal { A } )$ has an identity, why not just look at the subalgebra of $\mathcal { B } ( \mathcal { A } )$ generated by $\sphericalangle$ and the identity operator? Why not, indeed. This is just what is done below.

If $\mathcal { A }$ and $\mathcal { C }$ are Banach algebras and $v : { \mathcal { A } }   \to   { \mathcal { C } }$ , then v is \*-homomorphism if v is an algebra homomorphism such that $v(a^{*}) = v(a)^{*}$ for all a in $\mathcal { A }$

1.9. Proposition. If A is a C\*-algebra, then there is a C\*-algebra $\mathcal { A } _ { 1 }$ with an identity such that $\mathcal { A } _ { 1 }$ contains $\varkappa$ as an ideal. If A does not have an identity, then $\mathcal { A } _ { 1 } / \mathcal { A }$ is one dimensional. $I f \mathcal { C }$ is a $C ^ { * }$ -algebra with identity, and $v : \mathcal { A } \rightarrow \mathcal { C }$