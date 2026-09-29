ProOF. We have already seen that $\alpha / M$ is a Banach space and, as was mentioned prior to the statement of the theorem, $\alpha / M$ is an algebra. If $x , y   \in   \mathcal { A }$ and $u , v \in \mathcal { M }$ then $(x + u)(y + v) = xy + (xv + uv + uv) \in xy + \mathcal{M}$ Hence $\| (x + \mathcal{M})(y + \mathcal{M}) \| = \| xy + \mathcal{M} \| \leqslant \| (x + u)(y + v) \| \leqslant \| x + u \| \| y + v \|$ Taking the infimum over all u, v in M gives that $\| ( x + \mathcal { M } ) ( y + \mathcal { M } ) \| \leq \| x + \mathcal { M } \|$ $\| y + \mathcal { M } \|$ . The remainder of the proof is left to the reader.

It may be that $\alpha / M$ has an identity even if $\varkappa$ does not. For example, let $\mathcal { A } = C _ { 0 } ( \mathbb { R } )$ and let $\mathcal { M } = \{ \phi \in C _ { 0 } ( \mathbb { R } ) : \phi ( x ) = 0$ when $| x | \leqslant 1 \}$ . If $\phi _ { 0 } \in C _ { 0 } ( \mathbb { R } )$ such that $\phi _ { 0 } ( x ) = 1$ for $| x | \leqslant 1$ , then $\phi _ { 0 } + \mathcal { M }$ is an identity for $\sigma / d$ . In fact, if $\phi \in C _ { 0 } ( \mathbb { R } ) , \quad ( \phi \phi _ { 0 } - \phi ) ( x ) = 0 \quad \mathrm { i f } \quad | x | \leqslant 1$ . Hence $( \phi + \mathcal { M } ) ( \phi _ { 0 } + \mathcal { M } ) = \phi + \mathcal { M }$ (see Exercises 6 through 9)

## EXERCISES

1. Let $\varkappa$ be a Banach algebra and let $\mathcal { L }$ be all of the closed left ideals in $\varkappa$ If $I _ { 1 } ,$ $I _ { 2 } \in \mathcal { L } ,$ define $I_{1} \lor I_{2} \equiv \mathrm{cl}(I_{1} + I_{2})$ and $I _ { 1 } \wedge I _ { 2 } = I _ { 1 } \cap I _ { 2 }$ . Show that with these definitions $\mathcal { L }$ is a complete lattice with a largest and a smallest element.

2. Let X be locally compact. For every open subset U of X, let $I ( U ) = \{ \phi \in C _ { 0 } ( X ) \}$ $\phi = 0 \mathrm { o n } X \backslash U \}$ . Show that $U   \mapsto   I ( U )$ is a lattice monomorphism of the collection of open subsets of X into the lattice of close ideals of $C _ { 0 } ( X )$ . (It is, in fact, surjective, but the proof of that should wait.)

3. Let $( X , \Omega , \mu )$ be a σ-finite measure space and let I be an ideal in $L ^ { \infty } ( X , \Omega , \mu )$ that is weak\* closed. Show that there is a set ∆ in Ω such that $I = \{ \phi \in L ^ { \infty } ( X , \Omega , \mu ) :$ $\phi   =   0$ a.e. on $\Delta \}$

4. Let $\mathcal { A } = \left\{ \left[ \begin{matrix} { \alpha } & { 0 } \\ { \beta } & { \alpha } \\ \end{matrix} \right] : \alpha , \beta \in \mathbb { F } \right\}$ and let $\mathcal { M } = \left\{ \left[ \begin{matrix} { 0 } & { 0 } \\ { \beta } & { 0 } \\ \end{matrix} \right] : \beta { \in } \mathbb { F } \right\}$ . Show that $\alpha$ is a Banach algebra and M is a maximal ideal in $\varkappa$

5. Show that for $n \geqslant 1,   M_n(\mathbb{C})$ has no nontrivial ideals. How about $M _ { n } ( \mathbb { R } ) ?$

6. Let $\varkappa$ be a Banach algebra but do not assume that $\alpha$ has an identity. If I is a left ideal of $\alpha ,$ say that I is a modular left ideal if there is a u in $\varkappa$ such that $\mathcal { A } ( 1 - u ) \equiv \{ a - a u : a \in \mathcal { A } \} \subseteq I ;$ call such an element u of $\varkappa$ a right modular unit for I. Similarly, define right modular ideals and left modular units. Prove the following. (a) If u is a right modular unit for the left ideal I and $u { \in } I ,$ then $I = \mathcal { A }$ (b) Maximal modular left ideals are maximal left ideals. (c) If I is a proper modular left ideal, then I is contained in a maximal left ideal. (d) If I is a proper modular left ideal and u is a modular right unit for I, then $\| \boldsymbol { u } - \boldsymbol { x } \| \geqslant 1$ for all x in I and cl I is a proper modular left ideal. (e) Every maximal modular left ideal of $\alpha$ is closed.

7. Using the terminology of Exercise 6, let I be an ideal of $\varkappa$ Show: (a) if u is a right modular unit for I and v is a left modular unit for I, then $u - v   \in   I ,$ (b) If I is closed, $\mathcal { A } / I$ has an identity if and only if there is a right modular unit and a left modular unit for I. Call an ideal I such that $\mathcal { A } / I$ has an identity a modular ideal. An element u such that $u + I$ is an identity for $\mathcal { A } / I$ is called a modular identity for I.

8. If $\varkappa$ is a Banach algebra, a net $\{ e _ { i } \}$ in $\varkappa$ is called an approximate identity for A if $\operatorname { s u p } _ { i } \| e _ { i } \| < \infty$ and for each a in $\mathcal { A } ,   e _ { i } a   \rightarrow   a$ and $a e _ { i }   \rightarrow   a .$ Show that $\varkappa$ has an approximate identity if and only if there is a bounded subset E of  such that for every $\varepsilon   >   0$ and for every a in $\varkappa$ there is an e in E with $\| a e - a \| + \| e a - a \| < \varepsilon .$ See Wichmann [1973] for more information.

9. Show that if X is locally compact, then $C _ { 0 } ( X )$ has an approximate identity.

10. If  is a Hilbert space, show that $\mathcal { B } _ { 0 } ( \mathcal { H } )$ has an approximate identity.

11. If G is a locally compact group, show that $L ^ { 1 } ( G ) ( 1 . 1 1 )$ has an approximate identity. [Hint: Let $\mathcal { U } = \mathrm { a l l }$ neighborhoods U of the identity e of G such that cl U is compact. Order U by reverse inclusion. For U in $q ,$ let $f _ { U } = m ( U ) ^ { - 1 } \chi _ { U }$ . Then $\{ f _ { v } : U { \in } { \mathcal { U } } \}$ is an approximate identity for $L ^ { 1 } ( G ) . ]$

12. For $0 < r < 1$ , let $P _ { r } : \partial \mathbb { D } \to [ 0 , \infty )$ defined by $P _ { r } ( z ) = \sum _ { n = - \infty } ^ { \infty } r ^ { | n | } z ^ { n }$ (the Poisson kernel). Show that $\{ P _ { r } \}$ is an approximate identity for $L ^ { 1 } ( \partial \hat { \mathbf { D } } )$ (under convolution).

13. If $\mathcal { H }$ is a Hilbert space and P is a projection, show that $\mathcal { B } _ { 0 } ( \mathcal { H } ) P$ is a closed modular left ideal of $\mathcal { B } _ { 0 } ( \mathcal { H } )$ . What is the associated right modular unit?

14. Find the minimal proper left ideals of $M _ { n } ( \mathbb { F } )$

15. Find the minimal closed proper left ideals of $\mathcal { B } _ { 0 } ( \mathcal { H } ) , \mathcal { H }$ a Hilbert space. How about for $\mathcal { B } _ { 0 } ( \mathcal { X } ) ,   \mathcal { X }$ a Banach space?

16. What are the maximal modular left ideals of $\mathcal { B } _ { 0 } ( \mathcal { H } ) , \mathcal { H }$ a Hilbert space?

## §3. The Spectrum

3.1. Definition. If  is a Banach algebra with identity and $a \in \mathcal { A } _ { j }$ the spectrum of a, denoted by $\sigma ( a ) .$ , is defined by

$$
\sigma ( a ) = \{ \alpha \in \mathbb { F } \colon a - \alpha { \mathrm { ~ i s ~ n o t ~ i n v e r t i b l e } } \} .
$$

The left spectrum, $\sigma _ { l } ( a ) ,$ , is the set $\{ \alpha { \in } \mathbb { F } \colon a - \alpha$ is not left invertible}; the right spectrum, $\sigma _ { \pmb { r } } ( a ) ,$ is defined similarly.

The resolvent set of a is defined by $\rho(a) = \mathbb{F} \backslash \sigma(a)$ . The left and right resolvents of a are $\rho _ { l } ( a ) = \mathbb { F } \backslash \sigma _ { l } ( a )$ and $\rho _ { r } ( a ) = \mathbb { F } \backslash \sigma _ { r } ( a )$

3.2. Example. Let X be compact. If $f   \in   { \cal C } ( X ) ,$ then $\sigma ( f )   =   f ( X )$ In fact, if $\alpha = f ( x _ { 0 } ) ,$ , then $f - \alpha$ has a zero and cannot be invertible. So $f ( X ) \subseteq \sigma ( f )$ . On the other hand, if $\alpha \notin f ( \mathbf { X } ) , f - \alpha$ is a nonvanishing continuous function on X. Hence $(f - \alpha)^{-1} \in C(X)$ and so $f - \alpha$ is invertible. Thus $\alpha \notin \sigma ( f )$

3.3. Example. If X is a Banach space and $A   \in   \mathcal { B } ( \mathcal { X } )$ , then $\sigma(A) = \{ \alpha \in \mathbb{F} :$ either ker $( A - \alpha ) \neq ( 0 )$ or ra $\tan ( A - \alpha ) \neq X$ . In fact, this means that $\rho(A)=\mathbb{F}\backslash\sigma(A)=$ $\{ \alpha { \in } \mathbb { F } \colon A - \alpha$ is bijective}. If $\alpha   \in   \rho ( A ) ,$ , there is an operator T in $\mathcal { B } ( \mathcal { X } )$ such that $T(A - \alpha) = (A - \alpha)T = 1;$ clearly, $A - \alpha$ is bijective. On the other hand, if $A - \alpha$ is bijective, $( A - \alpha ) ^ { - 1 } \in { \mathcal { B } } ( { \mathcal { X } } )$ by the Inverse Mapping Theorem.

3.4. Example. If $\mathcal { H }$ is a Hilbert space and $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ then $\sigma _ { l } ( A ) = \{ \alpha \in \mathbb { F } :$ inf{ $\left\{ ( A - \alpha ) h   \| \colon   \|   h   \| = 1 \right\} = 0 \}$ . In fact, suppose $B \in \mathcal { B } ( \mathcal { H } )$ such that $B(A - \alpha) = 1.  If  \|h\| = 1$ , then $1 = \| \boldsymbol{h} \| = \| \boldsymbol{B}(\boldsymbol{A} - \boldsymbol{\alpha})\boldsymbol{h} \| \leqslant \| \boldsymbol{B} \| \| (\boldsymbol{A} - \boldsymbol{\alpha})\boldsymbol{h} \|$ . So $\| ( A - \alpha ) h \| \geqslant \| B \| ^ { - 1 }$ whenever $\| \boldsymbol { h } \| = 1$

Conversely, suppose $\| ( A - \alpha ) h \| \geqslant \delta > 0$ whenever $\| h \| = 1$ . Note that ker $(A - \alpha) = (0)$ . It will now be shown that ran(A — α) is closed. In fact, assume that $( A - \alpha ) f _ { n } \to g .$ Then $\delta \left\| f _ { n } - f _ { m } \right\| \leqslant \left\| ( A - \alpha ) ( f _ { n } - f _ { m } ) \right\| = \left\| ( A - \alpha ) f _ { n } - \alpha \right\|$ $(A - \alpha)f_m \parallel . \quad  Thus  \quad \{f_n\}$ is a Cauchy sequence. $\begin{array} { r l } { \mathbf { L e t } } & { { } f _ { n }   \rightarrow   f . } \end{array}$ Then $g = \lim (A - \alpha) f_n = (A - \alpha) f;$ hence $g { \in } \operatorname { r a n } ( A - \alpha )$ Let $\mathcal{H} = \mathrm{ran}(A - \alpha);$ sO $( A - \alpha ) : \mathcal { H } \rightarrow \mathcal { H }$ is a bijection. Thus $( A - \alpha ) ^ { - 1 } : \mathcal { H } \to \mathcal { H }$ is bounded. Define $B : \mathcal { H } \to \mathcal { H }$ by letting $B(k + h) = (A - \alpha)^{-1}k$ when $k \in \mathcal { H }$ and $h \in \mathcal { H } ^ { \perp }$ . Thus $B   \in   \mathcal { B } ( \mathcal { H } )$ and $B ( A - \alpha ) = 1$

3.5. Example. If $\mathcal { A } = M _ { 2 } ( \mathbb { R } )$ and $\boldsymbol{A} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ then $\sigma(A)=\square$ . In fact, $A   -   \alpha$ is not invertible if and only if $0 = \det(A - \alpha) = \alpha^2 + 1$ , which is impossible in R.

The phenomenon of the last example does not occur if $\varkappa$ is a Banach algebra over C.

3.6. Theorem. If A is a Banach algebra over C with an identity, then for each a in ${ \mathcal { A } } , \sigma ( a )$ is a nonempty compact subset $\mathbf { o f } \mathbf { C } .$ Moreover, $if \left| \alpha \right| > \left\| a \right\|, \alpha \notin \sigma(a)$ and $z { \mapsto } ( z - a ) ^ { - 1 }$ is an A-valued analytic function defined on $\rho ( a )$

Before beginning the proof, a few words on vector-valued analytic functions are in order. If G is a region in C and X is a Banach space, define the derivative of $f \colon G   \to   { \mathcal { X } }$ at $z _ { 0 }$ to be $\lim_{h \to 0} h^{-1} \left[ f(z_0 + h) - f(z_0) \right]$ if the limit exists. Say that f is analytic if f has a continuous derivative on G. The whole theory of analytic functions transfers to this situation. The statements and proofs of such theorems as Cauchy's Integral Formula, Liouville's Theorem, etc., transfer verbatim. Also, $f \colon G   \to   { \mathcal { X } }$ is analytic if and only if for each $z _ { 0 }$ in G there is a sequence $x _ { 0 } , \quad x _ { 1 } , \quad x _ { 2 } , \ldots$ in X such that $f(z) = \sum_{k = 0}^{\infty} (z - z_0)^k x_k$ whenever $z   \in   { \pmb B } ( z _ { 0 } ; r )$ , where $\boldsymbol{r} = \mathrm{dist}(z_0, \partial G)$ . Moreover, the convergence is. uniform on compact subsets of $B ( z _ { 0 } ; r )$

There is also a way of obtaining the vector-valued case as a consequence of the scalar-valued case (see Exercise 4).

PROOF OF THEOREM 3.6. If $| \alpha | > \| a \|$ , then $\alpha - a = \alpha(1 - a/\alpha)$ and $\| a / \alpha \| < 1$ By Corollary $2 . 3 , \; ( 1 - a / \alpha )$ is invertible. Hence $\alpha - a$ is invertible and so α∉σ(a). Thus $\sigma ( a ) \subseteq \{ \alpha \in \mathbb { C } : | \alpha | \leqslant \| a \| \}$ and $\sigma ( a )$ is bounded.

Let G be the set of invertible elements of $\varkappa$ The map $\alpha \mapsto ( \alpha - a )$ is a continuous function of $\mathbb { C } \rightarrow \mathcal { A }$ Since G is open and $\rho ( a )$ is the inverse image of G under this map, $\rho ( a )$ is open. Thus $\sigma ( a ) = \mathbf { C } \backslash \rho ( a )$ is compact.

Define $F \colon \rho ( a )   \to   { \mathcal { A } }$ by $F(z) = (z - a)^{-1}$ . In the identity $x ^ { - 1 } - y ^ { - 1 } =$ $x ^ { -   1 } ( y - x ) y ^ { -   1 }$ , let $x = ( \alpha + h - a )$ and $y = ( \alpha - a )$ , where $\alpha   \in   \rho ( a )$ and $h \in \mathbf { C }$ such that $h \neq 0$ and $\alpha + h \in \rho ( a )$ This gives

$$
\frac{F(\alpha + h) - F(\alpha)}{h} = \frac{(\alpha + h - a)^{-1}(-h)(\alpha - a)^{-1}}{h} \\= - (\alpha + h - a)^{-1}(\alpha - a)^{-1}.
$$

Since $( \alpha + h - a ) ^ { - 1 } \rightarrow ( \alpha - a ) ^ { - 1 }$ as $h   \rightarrow   0 ,   F ^ { \prime } ( \alpha )$ exists and

$$
F ^ { \prime } ( \alpha ) = - ( \alpha - a ) ^ { - 2 } .
$$

Clearly $F ^ { \prime } \colon \rho ( a )   \to   { \mathcal { A } }$ is continuous, so F is analytic on $\rho ( a ) .$

From the first paragraph of the proof and Corollary 2.3, if $| z | > \| a \|$ , then $F(z) = z^{-1}(1 - a/z)^{-1}$ . But as $z   \to   \infty , ( 1 - a / z )   \to   1$ and so $( 1 - a / z ) ^ { - 1 } \rightarrow 1$ . Thus $F(z) \to 0   as   z \to \infty$

Therefore if $\rho ( a ) = \mathbb { C }$ , F is an entire function that vanishes at $\infty$ By Liouville's Theorem F is constant. Since $F ^ { \prime } \neq 0 ,$ , this is a contradiction. Thus $\rho ( a ) \neq \mathbb { C } ,$ or $\sigma ( a ) \neq \Box$

Because the spectrum of an element of a complex Banach algebra is not empty, the following assumption is made.

Assumption. Henceforward, all Banach spaces and all Banach algebras are over C.

3.7. Definition. If  is a Banach algebra with identity and $a \in \mathcal { A } _ { 2 }$ the spectral radius of $a ,   r ( a ) ,$ , is defined by

$$
r ( a ) = \operatorname* { s u p } \{ | \alpha | : \alpha \in \sigma ( a ) \} .
$$

Because $\sigma ( a ) \neq \Box$ and is bounded, $r ( a )$ is well defined and finite; because $\sigma ( a )$ is compact, this supremum is attained.

Let $\mathcal { A } = M _ { 2 } ( \pmb { \mathbb { C } } )$ and let $\boldsymbol{A} = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$ Then $A ^ { 2 }   =   0$ and $\sigma ( A ) = \{ 0 \}$ ; so $r ( A ) = 0$ So it is possible to have $r(A)=0$ with $A \neq 0 .$

3.8. Proposition. If A is a Banach algebra with identity and $a \in \mathcal { A } _ { i }$ lim $\| \boldsymbol { a } ^ { n } \| ^ { 1 / n }$ exists and

$$
r(a) = \lim_{n \to \infty} \|a^n\|^{1/n}.
$$

PROOF. Let $G = \{ z \in \mathbb { C } : z = 0 { \mathrm { ~ o r ~ } } z ^ { - 1 } \in \rho ( a ) \}$ . Define $f \colon G   \to   { \mathcal { A } }$ by $f ( 0 )   =   0$ and for $z \ne 0,\; f(z) = (z^{-1} - a)^{-1}$ . Since $(a - \alpha)^{-1} \rightarrow 0$ as $\alpha   \to   \infty .$ , f is analytic on $G ,$ and so f has a power series expansion. In fact, by Corollary 2.3, for $| z | < \| a \| ^ { - 1 }$ 2

$$
f(z)=\sum_{n = 0}^{\infty}a^{n}/(z^{- 1})^{n + 1}=z\sum_{n = 0}^{\infty}z^{n}a^{n}.
$$

From complex variable theory, this power series converges for $| z | <$ $R \equiv \mathrm{dist}(0, \partial G) = \mathrm{dist}(0, \sigma(a)^{-1})$ (Here $\sigma ( a ) ^ { - 1 } = \{ z ^ { - 1 } : z \in \sigma ( a ) \}$ . Thus $R =$ inf $\{ | \alpha | : \alpha ^ { - 1 } \in \sigma ( a ) \} = r ( a ) ^ { - 1 }$ . Also, from the theory of power series, $R^{-1} = \lim \sup \| a^n \|^{1/n}$ Thus

$$
r(a) = \lim \sup \| a^n \|^{1/n}.
$$

Now if $\alpha \in \mathbf { C }$ and $n \geqslant 1,\quad \alpha^{n}-a^{n}=(\alpha-a)(\alpha^{n-1}+\alpha^{n-2}a+\cdots+a^{n-1})=$ $( \alpha ^ { n - 1 } + \alpha ^ { n - 2 } a + \cdots + a ^ { n - 1 } ) ( \alpha - a ) . \mathrm { S o ~ i f ~ } \alpha ^ { n } - a ^ { n }$ is invertible, $\alpha - a$ is invertible and $( \alpha - a ) ^ { - 1 } = ( \alpha ^ { n } - a ^ { n } ) ^ { - 1 } ( \alpha ^ { n - 1 } + \cdots + a ^ { n - 1 } )$ . So for α in $\sigma ( a ) ,   \alpha ^ { n } - a ^ { n }$ is not invertible for every $n \geqslant 1$ . By Theorem $3.6, \left| \alpha \right|^{n} \leqslant \left\| a^{n} \right\|$ . Hence $| \alpha | \leqslant \| a ^ { n } \| ^ { 1 / n }$ for all $n \geqslant 1$ and α in $\sigma ( a ) .$ So if $\alpha \in \sigma(a), |\alpha| \leqslant \liminf \|a^n\|^{1/n}$ .Taking the supremum over all α in σ(a) gives that $r(a) \leqslant \lim$ inf $\| a ^ { n } \| ^ { 1 / n } \leq$ lim sup $\| a ^ { n } \| ^ { 1 / n } =$ $r ( a )$ . So $r(a) = \lim \| a^n \|^{1/n}$

## 3.9. Proposition. Let A be a Banach algebra with identity and let $a \in \mathcal { A }$

(a) If $\alpha   \in   \rho ( a ) ,$ then dist $( \alpha , \sigma ( a ) ) \geqslant \| ( \alpha - a ) ^ { - 1 } \| ^ { - 1 }$

(b) If α, $\beta   \in   \rho ( a ) ,$ then

$$
\begin{aligned}(\alpha - a)^{-1} - (\beta - a)^{-1} &= (\beta - \alpha)(\alpha - a)^{-1}(\beta - a)^{-1} \\&= (\beta - \alpha)(\beta - a)^{-1}(\alpha - a)^{-1}.\end{aligned}
$$

PRoOF. (a) By Corollary 2.3, if $\alpha \in \rho ( a )$ and $\| x - ( \alpha - a ) \| < \| ( \alpha - a ) ^ { - 1 } \| ^ { - 1 } ,$ x is invertible. So if $\beta \in \mathbf { C }$ and $| \beta | < \| ( \alpha - a ) ^ { - 1 } \| ^ { - 1 } , ( \beta + \alpha - a )$ is invertible; that is, $\alpha + \beta \in \rho ( a )$ . Hence dist $( \alpha , \sigma ( a ) ) \geqslant \| ( \alpha - a ) ^ { - 1 } \| ^ { - 1 } . ( b )$ This follows by letting $x = a - a$ and $y   =   \beta - a$ in the identity $x^{-1}-y^{-1}=x^{-1}(y-x)y^{-1}=$ $y ^ { - 1 } ( y - x ) x ^ { - 1 }$ ■

The identity in part (b) of the preceding proposition is called the resolvent identit y and the function $\alpha \mapsto ( \alpha - a ) ^ { - 1 } { \mathrm { ~ o f ~ } } \rho ( a ) \to { \mathcal { A } }$ is called the resolvent of a.

## EXERCISES

1. Let S be the unilateral shift on $l ^ { 2 }$ (II.2.10). Show that S is left invertible but not right invertible.

2. If $\alpha$ is a Banach algebra with identity and $a \in \mathcal { A }$ and is nilpotent (that is, $a ^ { n }   =   0$ for some n), then $\sigma ( a ) = \{ 0 \}$

3. Let $( X , \Omega , \mu )$ be a $\sigma - \mathrm{finite}$ measure space and let $\mathcal { A } = L ^ { \infty } ( X , \Omega , \mu )$ (1.6). If $\phi \in \mathcal { A } ,$ show that the following are equivalent: (a) α∈σ(φ); (b) 0 = sup {inf $\begin{array} { r } { \{ | \phi ( x ) - \alpha | : } \end{array}$ $x { \in } { \pmb { X } } \backslash { \pmb { \Delta } } \} { \colon } { \pmb { \Delta } } { \in } { \pmb { \Omega } }$ and $\mu ( \Delta ) = 0 \} ; ( c )$ if $\varepsilon > 0 , \mu ( \{ x { \in } X { : } | \phi ( x ) - \alpha | < \varepsilon \} ) > 0 ;$ (d) if ν is the measure defined on the Borel subsets of C by $v ( \Delta ) = \mu ( \phi ^ { - 1 } ( \Delta ) )$ , then α∈the support of v.

4. If G is an open subset of C and $f \colon G   \to   { \mathcal { X } }$ is a function such that for each $x ^ { * }$ in ${ \mathcal { X } } ^ { * } , x ^ { * } \circ f { \colon } G { \to } { \mathbb { C } }$ is analytic, then f is analytic. If the word “continuous" is substituted for both occurrences of the word “analytic", is the preceding statement still true?

5. If  is a Banach algebra with identity, $\left\{ a _ { n } \right\} \subseteq \mathcal { A } , a _ { n } \rightarrow a , \alpha _ { n } \in \sigma ( a _ { n } ) ,$ and $\alpha _ { n } \to \alpha _ { 1 }$ then α∈σ(a).

6. If  is a Banach algebra with identity and $r \colon { \mathcal { A } }   \to   [ 0 , \infty )$ is the spectral radius, show that r is upper semicontinuous. If $a   \in   \mathcal { A }$ such that $r ( a )   =   0 .$ , show that r is continuous at a.

7. If  is a Banach algebra with identity, a, b∈, and α is a nonzero scalar such that $( x - a b )$ is invertible, show that $( \alpha - b a )$ is invertible and $( \alpha - b a ) ^ { - 1 } =$ $\alpha^{-1} + \alpha^{-1} b (\alpha - ab)^{-1} a.$ Show that $\sigma ( a b ) \cup \{ 0 \} = \sigma ( b a ) \cup \{ 0 \}$ and give an example such that $\sigma ( a b ) \neq \sigma ( b a )$

## §4. The Riesz Functional Calculus

Before coming to the main course of this section, it is necessary to have an appetizer from complex analysis. Many of these topics can be found in Conway [1978] with complete proofs. Only a few results are presented here.

If $\gamma$ is a closed rectifiable curve in C and $a \notin \{ \gamma \} \equiv \{ \gamma ( t ) ; \; 0 \leqslant t \leqslant 1 \}$ , then the winding number $o f \gamma$ about a is defined to be the number

$$
n ( \gamma ; a ) = \frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { 1 } { z - a } d z .
$$

The number $n ( \gamma ; a )$ is always an integer and is constant on each component of $\mathbf { C } \backslash \{ \gamma \}$ and vanishes on the unbounded component of $\mathbf { C } \backslash \{ \gamma \}$

Let G be an open subset of C and let $\mathcal { X }$ be a Banach space. If $f \colon G   \to   { \mathcal { X } }$ is analytic and $x ^ { * } { \in } { \mathcal { X } } ^ { * }$ , then $z \mapsto \langle f ( z ) , x ^ { * } \rangle$ is analytic on G and its derivative is $\langle f ^ { \prime } ( z ) , x ^ { * } \rangle$ . By Exercise 4 of the preceding section, if $f \colon G   \to   { \mathcal { X } }$ is a function such that $z \mapsto \langle f ( z ) , x ^ { * } \rangle$ is analytic for each $x ^ { * }$ in $\mathcal { X } ^ { * }$ , then $f \colon G   \to   \mathcal { X }$ is analytic. These facts will help in discussing and proving many of the results below.

If γ is a rectifiable curve in G and f is a continuous function defined in a neighborhood of $\{ \gamma \}$ with values in $\mathcal { X } ,$ then $\int _ { \gamma } f$ can be defined as for a scalar-valued $f$ as the limit in $\mathcal { X }$ of sums of the form

$$
\sum _ { j } \left[ \gamma ( t _ { j } ) - \gamma ( t _ { j - 1 } ) \right] f ( \gamma ( t _ { j } ) ) ,
$$

where $\{ t _ { 0 } , t _ { 1 } , \ldots , t _ { n } \}$ is a partition of [0, 1]. Hence $\int _ { \gamma } f = \int _ { 0 } ^ { 1 } f ( \gamma ( t ) ) d \gamma ( t ) \in \mathcal { X }$ . It is easy to see that for every $x ^ { * }$ in $\mathcal { X } ^ { * } , \langle \int _ { \gamma } f , x ^ { * } \rangle = \int _ { \gamma } \langle f ( \cdot ) , x ^ { * } \rangle$

4.1. Cauchy's Theorem. If X is a Banach space, G is an open subset of $\mathbf { c } , f :$ $G   \rightarrow   \mathcal { X }$ is an analytic function, and $\gamma _ { 1 } , \ldots , \gamma _ { m }$ are closed rectifiable curves in G such that $\begin{array} { r } { \sum _ { j = 1 } ^ { m } n ( \gamma _ { j } ; a ) = 0 } \end{array}$ for all a in $\mathbf { C } \backslash G ,$ then $\scriptstyle \sum _ { j = 1 } ^ { m } \int _ { \gamma _ { j } } f \; = \; 0$

PROOF. If $x ^ { * } { \in } { \mathcal { X } } ^ { * }$ then $\left\langle \sum_{j = 1}^{m} \int_{\gamma_{j}} f(x^{*}) = \sum_{j = 1}^{m} \int_{\gamma_{j}} \left\langle f(\cdot), x^{*} \right\rangle = 0 \right.$ by the scalar-valued version of Cauchy's Theorem. Hence $\sum _ { j = 1 } ^ { m } \int _ { \gamma _ { j } } f = 0$ ■

4.2. Cauchy's Integral Formula. If X is a Banach space, G is an open subset of $\mathbb { C } , f \colon G   \to   \mathcal { X }$ is analytic, γ is a closed rectifiable curve in G such that $n ( \gamma ; a ) = 0$ for every a in $\mathbf { C } \backslash G ,$ , and $\lambda \in G \backslash \{ \gamma \}$ , then for every integer $k \geqslant 0 .$

$$
n ( \gamma ; \lambda ) f ^ { ( k ) } ( \lambda ) = \frac { k ! } { 2 \pi i } \int _ { \gamma } ( z - \lambda ) ^ { - ( k + 1 ) } f ( z ) d z.
$$

4.3. Definition. A closed rectifiable curve $\gamma$ is positively oriented if for every a in $G \backslash \{ \gamma \} ,   n ( \gamma ; a )$ is either 0 or 1. In this case the inside of $\gamma ,$ denoted by ins $\gamma ,$ is defined by

$$
\mathrm { i n s }   \gamma \equiv \{ a { \in } \mathbb { C } \backslash \{ \gamma \} { : } ~ n ( \gamma ; a ) = 1 \} .
$$

The outside of $\gamma ,$ denoted by out $\gamma ,$ is defined by

$$
\mathrm { o u t }   \gamma \equiv \{ a { \in } \mathfrak { C } \backslash \{ \gamma \} { : } n ( \gamma ; a ) = 0 \} .
$$

Thus $\mathbf { \bar { C } } = \{ \gamma \} \cup \operatorname { i n s } \gamma \cup \operatorname { o u t } \gamma$ \_4

A curve $\gamma \colon [ 0 , 1 ]   \to   \mathbb { C }$ is simple if $\gamma ( s ) = \gamma ( t )$ implies that either $s = t { \mathrm { ~ o r ~ } } s = 0$ and $t = 1$ . The Jordan Curve Theorem says that if $\gamma$ is a simple closed rectifiable curve, then $\mathbf { C } \backslash \{ \gamma \}$ has two components and $\{ y \}$ is the boundary of each. Hence $n ( \gamma ; a )$ takes on only two values and one of these must be 0; the other must be $\pm   1$

If $\mathbf { \Gamma } = \{ \gamma _ { 1 } , \ldots , \gamma _ { m } \}$ is a collection of closed rectifiable curves, then Γ is positively oriented if: (a) $\{ \gamma _ { i } \} \cap \{ \gamma _ { j } \} = \square$ for $i \neq j ;$ (b) for $a$ in $\mathbf{C} \setminus \bigcup_{j = 1}^{m} \{ \gamma_{j} \}$ $\begin{array} { r } { n ( \Gamma ; a ) \equiv \sum _ { j = 1 } ^ { m } n ( \gamma _ { j } ; a ) } \end{array}$ is either 0 or 1; (c) each $\gamma _ { j }$ is a simple curve. The inside of Γ, ins Γ, is defined by

$$
\mathrm { i n s }   \pmb { \Gamma } \equiv \{ a \colon n ( \Gamma ; a ) = 1 \} .
$$

The outside of Γ, out Γ, is defined by

$$
\mathrm { o u t   } \Gamma \equiv \{ a ; n ( \Gamma ; a ) = 0 \} .
$$

$$
\mathrm { L e t } \{ \Gamma \} \equiv \cup \{ \gamma _ { j } \colon 1 \leqslant j \leqslant m \} .
$$

4.4. Proposition. If G is an open subset of C and K is a compact subset of G, then there is a positively oriented system of curves $\Gamma = \{ \gamma _ { 1 } , \ldots , \gamma _ { m } \}$ in $G \backslash K$ such that $K \subseteq \operatorname { i n s } \Gamma$ and $\mathbf { C } \backslash G \subseteq \mathrm { o u t }   \Gamma$ . The curves $\gamma _ { 1 } { , \ldots , } \gamma _ { m }$ can be found such that they are infinitely differentiable.

The proof of this proposition can be found on p. 195 of Conway [1978], though some details are missing.

If $\mathbf { \Gamma } = \{ \gamma _ { 1 } , \ldots , \gamma _ { m } \}$ and each $\gamma _ { j }$ is rectifiable, define

$$
\int _ { \Gamma } f = \sum _ { j = 1 } ^ { m } \int _ { \gamma _ { j } } f
$$

whenever f is continuous in a neighborhood of $\{ \Gamma \}$

Let $\alpha$ be a Banach algebra with identity and let $a \in \mathcal { A }$ One of the principal

4.5

uses of Proposition 4.4 in this book will occur when $K = \sigma ( a )$ If $f \colon G   \to   \mathbb { C }$ is analytic and $\sigma ( a ) \subseteq G$ , we will define an element $f ( a )$ in $\varkappa$ by

$$
f(a) = \frac{1}{2\pi i} \int_{\Gamma} f(z)(z - a)^{-1} dz
$$

where Γ is as in Proposition 4.4 with $K = \sigma ( a )$ . But first it must be shown that (4.5) does not depend on the choice of Γ. That is, it must be shown that $f ( a )$ is well defined.

4.6. Proposition. Let A be a Banach algebra with identity, let $a \in \mathcal { A } _ { 2 }$ and let G be an open subset of C such that $\sigma ( a ) \subseteq G$ If $\Gamma = \{ \gamma _ { 1 } , \ldots , \gamma _ { m } \}$ and $\Lambda = \{ \lambda _ { 1 } , \ldots , \lambda _ { k } \}$ are two positively oriented collections of curves in G such that $\sigma ( a ) \in \mathrm { i n s }   \Gamma \subseteq G$ and $\sigma ( a ) \in \mathrm { i n s }   \Lambda \subseteq G$ and if $f \colon G \to \mathbb { C }$ is analytic, then

$$
\int _ { \Gamma } f ( z ) ( z - a ) ^ { - 1 } d z = \int _ { \Lambda } f ( z ) ( z - a ) ^ { - 1 } d z.
$$

PROOF. For $1 \leqslant j \leqslant k ,$ let $\gamma _ { m + j } = \lambda _ { j } ^ { - 1 }$ ; that is, $\gamma _ { m + j } ( t ) = \lambda _ { j } ( 1 - t )$ for $0 \leqslant t \leqslant 1$ If $z \notin G \setminus \sigma(a),$ then either $z \in \dot { \mathbb { C } } \setminus G$ or $z   \in   \sigma ( a )$ If $\dot { z \in \mathbb { C } \setminus G } ,$ then $\begin{array} { r } { \sum _ { j = 1 } ^ { m + k } n ( \gamma _ { j } ; z ) = } \end{array}$ $n ( \Gamma ; z ) - n ( \Lambda ; z ) = 0 - 0 = 0$ If $z   \in   \sigma ( a ) ,$ then $\begin{array} { r } { \sum _ { j = 1 } ^ { m + k } n ( \gamma _ { j } ; z ) = n ( \Gamma ; z ) - n ( \dot { \Lambda } ; z ) = } \end{array}$ $1 - 1 = 0 .$ Thus $\Sigma \equiv \left\{ \gamma _ { j } ; 1 \leqslant j \leqslant m + k \right\}$ is a system of closed curves in $U = G \backslash \sigma(a)$ such that $n ( \Sigma ; z ) = 0$ for all z in $\mathbf { C } \backslash U .$ Since $z \mapsto f ( z ) ( z - a ) ^ { - 1 }$ is analytic on U, Cauchy's Theorem implies

$$
0 = \int _ { \Sigma } f ( z ) ( z - a ) ^ { - 1 } d z = \int _ { \Gamma } f ( z ) ( z - a ) ^ { - 1 } d z - \int _ { \Lambda } f ( z ) ( z - a ) ^ { - 1 } d z.
$$

As was pointed out before, Proposition 4.6 implies that (4.5) gives a well-defined element $f ( a )$ of $\mathcal { A }$ whenever f is analytic in a neighborhood of σ(a). Let Hol $( a ) = a ! !$ of the functions that are analytic in a neighborhood of $\sigma ( a )$ . Note that Hol(a) is an algebra where if $f ,   g \in \mathrm { H o l } ( a )$ and $f$ and $g$ have domains $D ( f )$ and $D ( g )$ , then $f g$ and $f + g$ have domain $D ( f ) \cap D ( g )$ . Hol(a) is not, however, a Banach algebra.

4.7. The Riesz Functional Calculus. Let  be a Banach algebra with identity and let $a   \in   \mathcal { A }$

(a) The map $f   \mapsto   f ( a )$ of $\operatorname { H o l } ( a )   \to   { \mathcal { A } }$ is an algebra homomorphism.

(b) If $f(z) = \sum_{k = 0}^{\infty} \alpha_{k} z^{k}$ has radius of convergence $> r ( a )$ , then $f \in \operatorname{HCl}(a)$ and $f(a)=\sum_{k = 0}^{\infty}\alpha_{k}a^{k}.$

(c) $I f f ( z ) \equiv 1$ , then $f ( a ) = 1$

(d) If f(z) = z for all $z ,   f ( a )   =   a .$

(e) $I f f , f _ { 1 } , f _ { 2 } , \ldots$ are all analytic on $G ,   \sigma ( a ) \subseteq G ,$ and $f _ { n } ( z )   \to   f ( z )$ uniformly on compact subsets of $G ,$ then $\| f _ { n } ( a ) - f ( a ) \| \to 0$ as $n   \to   \infty$

PROOF. (a) Let $f ,   g \in \mathrm{HCl}(a)$ and let G be an open neighborhood of $\sigma ( a )$ on which both $f$ and g are analytic. Let $\Gamma$ be a positively oriented system of