APPENDIX C

# The Dual of $C _ { 0 } ( X )$

The purpose of this section is to show that the dual of $C _ { 0 } ( X )$ is the space of regular Borel measures on $X$ and to put this result, and the accompanying definitions, in the context of complex-valued measures and functions.

Let X be any set and let Ω be a σ-algebra of subsets of $X ;$ so $( X , \Omega )$ is a measurable space. If $\mu$ is a countably additive function defined on Ω such that $\mu ( \Box ) = 0$ and $0 \leqslant \mu ( \Delta ) \leqslant \infty$ for all $\pmb { \Delta }$ in $\mathbf { \Omega } _ { \mathbf { \Omega } _ { \mathbf { \Omega } } }$ call $\mu$ a positive measure on $( X , \Omega ) ;   ( X , \Omega , \mu )$ is called a measure space.

If (X,Ω) is a measurable space, a signed measure is a countably additive function $\mu$ defined on Ω such that $\mu ( \Box ) = 0$ and $\mu$ takes its values in $\mathbb { R } \cup \{ \pm \infty \}$ . (Note: $\mu$ can assume only one of the values $\pm \infty . )$ It is assumed that the reader is familiar with the following result.

C.1. Hahn-Jordan Decomposition. If µ is a signed measure on $( X ,   \Omega ) ,$ then $\mathbf { \mu } = \mathbf { \mu } _ { 1 } - \mathbf { \mu } _ { 2 } ,$ where $\mu _ { 1 }$ and $\mu _ { 2 }$ are positive measures, and $X = E _ { 1 } \cup E _ { 2 } ,$ , where $E _ { 1 } , E _ { 2 }   \in   \Omega , E _ { 1 }   \cap   E _ { 2 }   =   \square , \mu _ { 1 } ( E _ { 2 } )   =   0   =   \mu _ { 2 } ( E _ { 1 } ) .$ The measures $\mu _ { 1 }$ and $\mu _ { 2 }$ are unique and the sets $E _ { 1 }$ and $E _ { 2 }$ are unique up to sets of $\mu _ { 1 } + \mu _ { 2 }$ measure zero.

A measure (or complex-valued measure) is a complex-valued function $\mu$ defined on $\pmb { \Omega }$ that is countably additive and such that $\mu ( \Box ) = 0$ . Note that $\mu$ does not assume any infinite values. If $\mu$ is a measure, then $( \operatorname { R e } \mu ) ( \Delta ) \equiv \operatorname { R e } ( \mu ( \Delta ) )$ is a signed measure, as is $( \mathrm { I m }   \mu ) ( \Delta ) \equiv \mathrm { I m } ( \mu ( \Delta ) )$ ; hence $\mu = \operatorname { R e } \mu + i \operatorname { I m } \mu .$ Applying (C.1) to $\mathbf { R e }   \mu$ and Im $\mu$ we get

## C.2

$$
\mu = ( \mu _ { 1 } - \mu _ { 2 } ) + i ( \mu _ { 3 } - \mu _ { 4 } )
$$

where $\mu _ { j } \left( 1 \leqslant j \leqslant - 4 \right)$ are positive measures, $\mu _ { 1 } \perp \mu _ { 2 } \left( \mu _ { 1 } \right.$ and $\mu _ { 2 }$ are mutually singular) and $\mu _ { 3 } \perp \mu _ { 4 }$ . (C.2) will also be called the Hahn-Jordan decomposition of $\mu .$

C.3. Definition. If $\mu$ is a measure on $( X , \Omega )$ and $\Delta { \in } \Omega ,$ define the variation of $\mu , \left| \mu \right|$ , by

$$
| \mu | ( \Delta ) = \sup \left\{ \sum_{j = 1}^{m} | \mu ( E_j ) | : \{ E_j \}_1^m   is a measurable partition of   \Delta \right\}.
$$

C.4. Proposition. If µ is a measure on $( X , \Omega )$ , then $| \mu |$ is a positive finite measure on (X,Ω). If µ is a signed measure, $| \mu |$ is a positive measure. $I f ( \mathbb { C } . 2 )$ is satisfied, then $| \mu | ( \Delta ) \leqslant \sum _ { k = 1 } ^ { 4 } \mu _ { k } ( \Delta ) ,$ ; if µ is a signed measure, then $| \boldsymbol { \mu } |   =   \mu _ { 1 } + \mu _ { 2 }$

PROOF. Clearly $| \mu | ( \Delta ) \geqslant 0$ Let $\{ \Delta _ { n } \}$ be pairwise disjoint measurable sets and let $\Delta = \bigcup _ { n = 1 } ^ { \infty } \Delta _ { n } . \mathrm { I f } \varepsilon > 0 ,$ then there is a measurable partition $\big \{ E _ { j } \big \} _ { j = 1 } ^ { m }$ of $\Delta$ such that $\begin{array} { r } { | \mu | ( \Delta ) - \varepsilon < \sum _ { j = 1 } ^ { m } | \mu ( E _ { j } ) | } \end{array}$ . Hence

$$
\begin{align*}\| \mu \| (\Delta) - \varepsilon & \leqslant \sum_{j=1}^{m} \left| \sum_{n=1}^{\infty} \mu(E_j \cap \Delta_n) \right| \\& \leqslant \sum_{n=1}^{\infty} \sum_{j=1}^{m} |\mu(E_j \cap \Delta_n)|.\end{align*}
$$

But $\left\{ E _ { j } \cap \Delta _ { n } \right\} _ { j = 1 } ^ { m }$ is a partition of $\Delta _ { n } ,$ so $| \mu | ( \Delta ) - \varepsilon \leqslant \sum _ { n = 1 } ^ { \infty } | \mu | ( \Delta _ { n } ) .$ Therefore $\| \mu \| ( \Delta ) \leqslant \sum _ { n = 1 } ^ { \infty } | \mu | ( \Delta _ { n } )$ For the reverse inequality we may assume that $| \mu | ( \Delta )   < \infty$ . It follows that $| \mu | ( \Delta _ { n } ) < \infty$ for every n. (Why?) Let $\varepsilon   >   0$ and for each $n \geqslant 1$ let $\left\{ E _ { 1 } ^ { ( n ) } , \ldots , E _ { m _ { n } } ^ { ( n ) } \right\}$ be a partition of $\Delta _ { n }$ such that $\begin{array} { r } { \sum _ { j } \lvert \mu ( E _ { j } ^ { ( n ) } ) \rvert > } \end{array}$ $| \mu | ( \Delta _ { n } ) - \varepsilon / 2 ^ { n }$ . Then

$$
\sum_{n = 1}^{N} | \mu | ( \Delta_n ) < \sum_{n = 1}^{N} \left[ \frac{\varepsilon}{2^n} + \sum_{j} | \mu ( E_j^{(n)} ) | \right]
$$

$$
\leqslant \varepsilon + \sum_{n = 1}^{N} \sum_{j} \left| \mu(E_{j}^{(n)}) \right|
$$

$$
\leqslant \varepsilon + | \mu | ( \Delta ) .
$$

Letting $N   \to   \infty$ and $\varepsilon   \to   0$ gives that $\begin{array} { r } { \sum _ { 1 } ^ { \infty } | \mu | ( \Delta _ { n } ) \leqslant | \mu | ( \Delta ) } \end{array}$

Clearly $| \mu ( \Delta ) | \leqslant \sum _ { k = 1 } ^ { 4 } \mu _ { k } ( \Delta )$ , so $| \mu | \leqslant \sum_{k = 1}^{4} \mu_{k}$ . It is left to the reader to show that $| \boldsymbol { \mu } |   =   \boldsymbol { \mu } _ { 1 } + \boldsymbol { \mu } _ { 2 }$ if $\mu$ is a signed measure. Since $\mu _ { 1 } ,   \mu _ { 2 } ,   \mu _ { 3 } ,   \mu _ { 4 }$ are all finite, $| \mu |$ is finite if $\mu$ is complex-valued. ■

C.5. Definition. If $\mu$ is a measure on (X,Ω) and v is a positive measure on (X,Ω), say that $\mu$ is absolutely continuous with respect to $\nu \left( \mu \ll \nu \right)$ if $\mu ( \Delta ) = 0$ whenever $v ( \Delta ) = 0$ . If v is complex-valued, $\mu   \ll   \nu$ means $\mu   \ll   | \nu | .$

C.6. Proposition. Let µ be a measure and v a positive measure on (X,Ω). The following statements are equivalent.

(a) $\mu \ll \nu .$

(b) $| \mu | \ll \nu .$

(c) If (C.2) holds, $\mu _ { k } \ll v \; \mathrm { f o r } \; 1 \leqslant k \leqslant 4 .$

PROOF. Exercise.

The Radon-Nikodym Theorem can now be proved for complex-valued measures $\mu$ by using (C.6) and applying the usual theorem to the real and imaginary parts of $\mu .$ The details are left to the reader.

C.7. Radon-Nikodym Theorem. $I f \left( X , \Omega , \nu \right)$ is a σ-finite measure space and µ is a complex-valued measure on (X,Ω) such that $\mu \ll \nu ,$ then there is a unique complex-valued function f in $L ^ { 1 } ( X , \Omega , \nu )$ such that $\mu ( \Delta ) = \int _ { \Delta } f$ dv for every $\pmb { \Delta }$ inΩ.

The function f obtained in (C.7) is called the Radon-Nikodym derivative of $\mu$ with respect to v and is denoted by $f = d \mu / d v$

C.8. Theorem. Let $( X , \Omega , v )$ be a σ-finite measure space and let $\mu$ be a complex-valued measure on $( X , \Omega )$ such that $\mu   \ll   \nu$ and let $f = d \mu / d v .$

(a) If $g   \in   L ( X , \Omega , | \mu | )$ , then $g f   \in   L ^ { 1 } ( X , \Omega , v )$ and $\int g d \mu = \int g f d v .$

(b) For $\pmb { \Delta }$ in $\Omega , \left| \mu \right| \left( \Delta \right) = \int _ { \Delta } \left| f \right| d v .$

ProoF. Part (a) follows from the corresponding result for signed measures by using (C.2) and a similar decomposition for $f .$

To prove (b), let $\{ E _ { j } \}$ be a measurable partition of ∆. Then

$$
\sum _ { j } | \mu ( E _ { j } ) | \leqslant \sum _ { j } \int _ { E _ { j } } | f | d v = \int _ { \Delta } | f | d v .
$$

For the reverse inequality, let $g ( x ) = \widetilde { f ( x ) } / | f ( x ) |$ if $x { \in } \Delta$ and $f(x) \neq 0;$ let $g ( x ) = 0$ otherwise. Let $\{ g _ { n } \}$ be a sequence of Ω-measurable simple functions such that $g _ { n } ( x ) = 0$ off $\Delta, |g_n| \leqslant |g| \leqslant 1$ , and $g _ { n } ( x )   \rightarrow   g ( x )$ a.e. [v]. Thus $f g _ { n } \to | f | \chi _ { \Delta } \quad \mathrm { a . e . } \quad [ v ] .$ Also, $| f g _ { n } | \leqslant | f | \chi _ { \Delta }$ and $f \chi _ { \Delta }   \in   L ^ { 1 } ( v )$ [see (C.2)]. By the Lebesgue Dominated Convergence Theorem, $\int f g_{n}   dv \rightarrow \int_{\Delta} |f|   dv$ If $\begin{array} { r } { \pmb { g } _ { n } = \sum _ { j }   \pmb { \alpha } _ { j } \chi _ { E _ { j } } , } \end{array}$ where $\{ E _ { j } \}$ is a partition of ∆ and $| \alpha _ { j } | \leqslant 1$ then $\left| \int f g_{n} d v \right| = \left| \int g_{n} d \mu \right| = \left| \sum_{j} \alpha_{j} \mu(E_{j}) \right| \leqslant | \mu | (\Delta)$ . Thus $\int _ { \Delta } | f | d v \leqslant | \mu | ( \Delta )$ ■

One way of phrasing (C.8b) is that $| d \mu / d v | = d | \mu | / d v$ . The next result is left to the reader.

C.9. Corollary. If µ is a complex-valued measure on (X,Ω), then there is an Ω-measurable function f on $X$ such that |f| = 1 a.e. [|µ|] and $\mu ( \Delta ) = \int _ { \Delta } f d | \mu |$ for each ∆ in Ω.

C.10. Definition. Let X be a locally compact space and let Ω be the smallest σ-algebra of subsets of X that contains the open sets. Sets in Ω are called Borel sets. A positive measure $\mu$ on (X,Ω) is a regular Borel measure if (a) $\mu ( K ) < \infty$ for every compact subset K of X; (b) for any E in Ω, $\mu ( E ) = \operatorname* { s u p } \left\{ \mu ( K ) : \right\}$ $K \subseteq E$ and K is compact}; (c) for any E in Ω, $\mu ( E ) = \operatorname* { i n f } \{ \mu ( U ) : U \supseteq E$ and U is open}. If $\mu$ is a complex-valued measure on (X,Ω), μ is a regular Borel measure $\mathbf { i f }   | \mu |   \mathbf { i s }$ Let $M(X) = \mathrm{all}$ of the complex-valued regular Borel measures on X. Note that $M ( X )$ is a vector space over C. For $\mu$ in $M ( X ) _ { \mathrm { i } }$ let

$$
\|   \mu   \| \equiv | \mu | ( X ) .\tag{C.11}
$$

C.12. Proposition. (C.11) defines a norm on $M ( X )$

PROOF. Exercise.

C.13. Lemma. If $\mu { \in } M ( X ) ,$ define $F _ { \mu } \colon C _ { 0 } ( X ) \to \mathbb { C }$ by $F _ { \mu } ( f ) = \int f   d \mu$ Then $F _ { \mu } \in C _ { 0 } ( X ) ^ { * }$ and $\| \boldsymbol { F } _ { \boldsymbol { \mu } } \| = \| \boldsymbol { \mu } \|$

PROOF. If $f   \in   { \cal C } _ { 0 } ( X ) ,$ then $| F _ { \mu } ( f ) | \leqslant \int | f | d | \mu | \leqslant \| f \| \| \mu \|$ . Hence $F _ { \mu } \in C _ { 0 } ( X ) ^ { * }$ and $\| \boldsymbol { F } _ { \boldsymbol { \mu } } \| \leqslant \| \boldsymbol { \mu } \|$

To show equality, let $f _ { 0 }$ be a Borel function such that $| f _ { 0 } | = 1$ a.e. $[ | \mu | ]$ and $\mu ( \Delta ) = \int _ { \Delta } f _ { 0 } d | \mu |$ . By Lusin's Theorem, if $\varepsilon   >   0 ,$ there is a continuous function $\phi$ on X with compact support such that $\int | \phi - \bar { f } _ { 0 } | d | \mu | < \varepsilon$ and $\| \phi \| \leqslant \sup | f_0(x) | = 1$ . Thus $\| \mu \| = \int f_{0} \bar{f}_{0} d | \mu | \quad ( \mathrm{C.8a} ) = \int \bar{f}_{0} d \mu = | \int \bar{f}_{0} d \mu | \leqslant$ $\left| \int ( \bar { f } _ { 0 } - \phi ) d \mu \right| + \left| \int \phi d \mu \right| \leqslant \varepsilon + \left| F _ { \mu } ( \phi ) \right| \leqslant \varepsilon + \left\| F _ { \mu } \right\|$ . Hence $\| \boldsymbol { \mu } \| \leqslant \| \boldsymbol { F } _ { \boldsymbol { \mu } } \|$ ■

C.14. Corollary. (a) If U is an open subset of X and $\mu { \in } M ( X ) ,$ then $| \mu | ( U ) = \operatorname* { s u p } \{ | \int \phi d \mu | : \phi \in C _ { c } ( X )$ spt $\phi \subseteq U ,$ and $\| \phi \| \leqslant 1 \}$ . (b) $\begin{array} { r } { I f \quad \mu \geqslant 0 , } \end{array}$ $\mu ( K ) = \operatorname* { i n f } \left\{ \int \phi ^ { \cdot } d \mu : \phi \in C _ { 0 } ( X ) \right\}$ and $\phi \geqslant \chi _ { K } \}$

ProoF. (a) If U is given the relative topology from X, U is locally compact. Let v be the restriction of $\mu$ to U. Then (a) becomes a restatement of (C.13) for the space U together with the fact that $C _ { c } ( U )$ is norm dense in $C _ { 0 } ( U )$

(b) If $\phi \geqslant \chi _ { K } ,$ then because μ is positive, $\int \phi   d \mu \geqslant \mu ( K ) .$ Thus $\mu ( K ) \leqslant \alpha \equiv \inf \left\{ \int \phi   d \mu : \phi \in C _ { 0 } ( X ) \right\}$ and $\phi \geqslant \chi _ { K } \}$ . Using the regularity of $\mu ,$ for every integer n there is an open set $U _ { n }$ such that $K \subseteq U _ { n }$ and $\mu ( U _ { n } \backslash K ) < n ^ { - 1 }$ Let $\psi _ { n } \in C _ { c } ( X )$ such that $0 \leqslant \psi_{n} \leqslant 1, \psi_{n} = 1$ on K, and $\psi _ { n } = 0$ off $U _ { n } .$ Thus $\psi _ { n } \geqslant \chi _ { K }$ and so $\alpha \leqslant \int \psi _ { n } d \mu \leqslant \mu ( U _ { n } ) < \mu ( K ) + n ^ { - 1 }$

The next step in the process of representing bounded linear functionals on $C _ { 0 } ( X )$ by measures is to associate with each such functional a positive functional. If $\mu { \in } M ( X )$ , then the next lemma would associate with the functional $F _ { \mu }$ the positive functional $I = F _ { | \mu | }$

C.15. Lemma. If $F \colon C _ { 0 } ( X )   \to   \mathbb { C }$ is a bounded linear functional, then there is a unique linear functional $I \colon C _ { 0 } ( X ) \to \mathbb { C }$ such that $\mathit { i f } f   \in   { \cal C } _ { 0 } ( X )$ and $f \geqslant 0 ,$ , then

$$
I ( f ) = \sup \left\{ | F ( g ) | : g \in C _ { 0 } ( X ) \text { a n d } | g | \leqslant f \right\} .\tag{C.16}
$$

Moreover $\| I \| = \| f \|$

PROOF. Let $C _ { 0 } ( X )$ + be the positive functions in $C _ { 0 } ( X )$ and for f in $C _ { 0 } ( X )$ + define $I ( f )$ as in (C.16). If $\alpha   >   0 ,$ , then clearly $I ( \alpha f ) = \alpha I ( f )$ if $f   \in   { \cal C } _ { 0 } ( X ) _ { + }$ . Also, if $g   \in   { \cal C } _ { 0 } ( X )$ and $| g | \leqslant f ,$ then $| F ( g ) | \leqslant \| F \| \| g \| \leqslant \| F \| \| f \|$ . Hence $I ( f )   \leqslant$二 $\boldsymbol{F} \| \left\| \boldsymbol{f} \right\| < \infty$

Now we will show that $I ( f _ { 1 } + f _ { 2 } ) = I ( f _ { 1 } ) + I ( f _ { 2 } )$ whenever $f_{1},f_{2} \in C(X)_{+}$ $\operatorname { I f } \varepsilon   >   0 ,$ let $g _ { 1 } , g _ { 2 } \in C _ { 0 } ( X )$ such that $| g _ { j } | \leqslant f _ { j }$ and $| F ( g _ { j } ) | > I ( f _ { j } ) - \frac { 1 } { 2 } \varepsilon$ for $j   =   1 , 2$ There are complex numbers $\beta _ { j } , j = 1 , 2 ,$ with $| \beta _ { j } | \stackrel { \cdot } { = } 1$ and $F ( g _ { j } ) = \beta _ { j } | F ( g _ { j } ) |$ Thus

$$
\begin{align*}I(f_1) + I(f_2) &< \varepsilon + |F(g_1)| + |F(g_2)| \\&= \varepsilon + \bar{\beta}_1 F(g_1) + \bar{\beta}_2 F(g_2) \\&= \varepsilon + |F(\bar{\beta}_1 g_1 + \bar{\beta}_2 g_2)|.\end{align*}
$$

But $| \bar { \beta } _ { 1 } g _ { 1 } + \bar { \beta } _ { 2 } g _ { 2 } ) | \leqslant | g _ { 1 } | + | g _ { 2 } | \leqslant f _ { 1 } + f _ { 2 }$ . Hence $I(f_1) + I(f_2) \leqslant \varepsilon + I(f_1 + f_2)$ Since ε was arbitrary, we have half of the desired equality.

For the other half of the equality, let $g   \in   \overline { { C _ { 0 } ( X ) } }$ such that $| g | \leqslant f _ { 1 } + f _ { 2 }$ and $I ( f _ { 1 } + f _ { 2 } ) < | F ( g ) | + \varepsilon .$ Let $h_{1} = \min(|g|, f_{1})$ and $h _ { 2 } = | g | - h _ { 1 }$ Clearly $h _ { 1 } , h _ { 2 } \in C _ { 0 } ( X ) _ { + } ,   h _ { 1 } \leqslant f _ { 1 } ,   h _ { 2 } \leqslant f _ { 2 }$ , and $\boldsymbol { h } _ { 1 } + \boldsymbol { h } _ { 2 } = | \boldsymbol { g } |$ . Define $g _ { j } \colon X   \to   \mathbb { C }$ by

$$
g _ { j } ( x ) = \left\{ \begin{aligned} & 0 & &  if   g ( x ) = 0, \\ & \frac { h _ { j } ( x ) g ( x ) } { | g ( x ) | } & &  if   g ( x ) \neq 0. \end{aligned} \right.
$$

It is left to the reader to verify that $g _ { j } { \in } C _ { 0 } ( X )$ and $g _ { 1 } + g _ { 2 } = g$ Hence

$$
\begin{aligned}I(f_{1} + f_{2}) &< |F(g_{1}) + F(g_{2})| + \varepsilon \\&\leqslant |F(g_{1})| + |F(g_{2})| + \varepsilon \\&\leqslant I(f_{1}) + I(f_{2}) + \varepsilon.\end{aligned}
$$

Now let $\varepsilon   \to   0 .$

If f is a real-valued function in $C _ { 0 } ( X ) .$ , then $f = f _ { 1 } - f _ { 2 }$ where $f _ { 1 } f _ { 2 } \in C _ { 0 } ( X ) _ { + }$ If also $f = g _ { 1 } - g _ { 2 }$ for some $g _ { 1 } , g _ { 2 }$ in $C _ { 0 } ( X ) _ { + }$ , then $g_{1} + f_{2} = f_{1} + g_{2}$ . By the preceding argument $I ( g _ { 1 } ) + I ( f _ { 2 } ) = I ( f _ { 1 } ) + I ( g _ { 2 } )$ Hence if we define $I ;$ $\operatorname { R e } C _ { 0 } ( X ) \to \operatorname { R }$ by $I ( f ) = I ( f _ { 1 } ) - I ( f _ { 2 } )$ where $f = f _ { 1 } - f _ { 2 }$ with $f _ { 1 } , f _ { 2 }$ in $\overline { { C _ { 0 } } } ( X ) _ { + }$ I is well defined. It is left to the reader to verify that I is R-linear.

If $f   \in   C _ { 0 } ( X ) ,$ , then $f = f _ { 1 } + i f _ { 2 }$ , where $f _ { 1 } , f _ { 2 } \in \operatorname { R e } C _ { 0 } ( X )$ . Let $I ( f ) = I ( f _ { 1 } ) +$ $i I ( f _ { 2 } )$ . It is left to the reader to show that $I : C _ { 0 } ( X ) \to \mathbb { C }$ is a linear functional.

To prove that $\| I \| = \| F \|$ , first let $f   \in   { \cal C } _ { 0 } ( X )$ and put $I ( f ) = \alpha | I ( f ) |$ where $| \alpha | = 1$ . Hence $\bar { \alpha } f = f _ { 1 } + i f _ { 2 }$ , where $f_{1},f_{2} \in \mathrm{Re} C_{0}(X)$ Thus $| I ( f ) | = \bar { \alpha } I ( f ) =$ $I ( f _ { 1 } ) + i I ( f _ { 2 } )$ Since $\{ I ( f ) \}$ is a positive real number, $I ( f _ { 2 } ) = 0$ and $I ( f _ { 1 } ) = | I ( f ) |$ . But $f_{1} = \mathrm{Re}(\bar{\alpha} f) \leqslant |f|$ . Hence

$$
| I ( f ) | \leqslant I ( | f | ) .
$$

From here we get, as in the beginning of this proof, that $\| I \| \leqslant \| F \|$ . For the other half, if $\varepsilon   >   0 ,$ let $f   \in   { \cal C } _ { 0 } ( X )$ such that $\| f \| \leqslant 1$ and $\| F \| < | F ( f ) | + \varepsilon .$ Thus $\| F \| < I ( | f | ) + \varepsilon \leqslant \| I \| + \varepsilon .$ ■

C.17. Theorem. If $I \colon C _ { 0 } ( X ) { \to } \mathbf { C }$ is a bounded linear functional such that $I ( f )   \geqslant   0$ whenever $f   \in   { \cal C } _ { 0 } ( X ) _ { + }$ , then there is a positive measure v in $M ( X )$ such that $I ( f ) = \int f   d v$ for every f in $C _ { 0 } ( X )$ and $\| I \| = { \mathfrak { v } } ( X )$

The proof of this is an involved construction. Inspired by Corollary C.14, one defines v(U) for an open set U by

$$
\nu ( U ) = \operatorname* { s u p } \{ I ( \phi ) : \phi \in C _ { c } ( X ) _ { + } , \phi \leqslant 1 , \operatorname { s p t } \phi \subseteq U \} .
$$

Then for any Borel set E, let

$$
v ( E ) = \operatorname* { i n f } \{ v ( U ) \colon E \subseteq U { \mathrm { ~ a n d ~ } } U { \mathrm { ~ i s ~ o p e n } } \} .
$$

It must now be shown that v is a positive measure and $I ( f ) = \int f   d v$ For the details see (12.36) in Hewitt and Stromberg [1975] or §56 in Halmos [1974]. Indeed, Theorem C.17 is often called the Riesz Representation Theorem.

C.18. Riesz Representation Theorem. If X is a locally compact space and $\mu { \in } M ( X )$ , define $F _ { \mu } \colon C _ { 0 } ( X ) \to \mathbb { C }$ by

$$
F _ { \mu } ( f ) = \int f   d \mu .
$$

Then $F _ { \mu } \in C _ { 0 } ( X ) ^ { * }$ and the map $\mu   \mapsto   F _ { \mu }$ is an isometric isomorphism of M(X) onto $\dot { C _ { 0 } ( X ) ^ { * } }$

PROOF. The fact that $\mu { \mapsto } F _ { \mu }$ is an isometry is the content of Lemma C.13. It remains to show that $\mu { \mapsto } F _ { \mu }$ is surjective. Let $F   \in   \overline { { C _ { 0 } ( x ) ^ { * } } }$ and define I: $C _ { 0 } ( X )   \to   \mathbb { C }$ as in Lemma C.15. By Theorem C.17, there is a positive measure ν in $M ( X )$ such that $I ( f ) = \int f   d v$ for all f in $C _ { 0 } ( X )$ . If $f   \in   { \cal C } _ { 0 } ( X ) ,$ , then the definition of I implies that $| \dot{F}(f) | \leqslant I( |f| ) = \int |f|   dv$ . Thus, $f { \mapsto } F ( f )$ defines a bounded linear functional on $C _ { 0 } ( X )$ considered as a linear manifold in $L ^ { 1 } ( \mathfrak { v } )$ Now $C _ { 0 } ( X )$ is dense in $L ^ { 1 } ( \mathfrak { v } )$ (Why?), so F has a unique extension to a bounded linear functional on $L ^ { 1 } ( \mathfrak { v } )$ . By Theorem B.1 there is a function φ in $L ^ { \infty } ( v )$ such that $F ( f ) = \int f \phi$ dv for every f in $C _ { 0 } ( X )$ and $\| \phi \| _ { \infty } \leqslant 1$ . Let $\mu ( E ) = \int _ { E } \phi   d \nu$ for every Borel set E. Then $\mu { \in } M ( X )$ and by Theorem $C.8(a),   F(f) = \int f   d\mu;$ that is, $F = F _ { \mu ^ { \circ } }$

M.B. Abrahamse [1978]. Multiplication operators. In Hilbert Space Operators. New York: Springer-Verlag Notes, Vol. 693, pp. 17–36.

M.B. Abrahamse and T.L. Kriete [1973]. The spectral multiplicity function of a multiplication operator. Indiana J. Math., 22, 845–857.

T. Andô [1963]. Note on invariant subspaces of a compact normal operator. Archiv. Math., 14, 337–340.

N. Aronszajn and K.T. Smith [1954]. Invariant subspaces of completely continuous operators. Ann. Math., 60, 345–350.

W. Arveson [1956]. An Invitation to C\*-algebras. New York: Springer-Verlag.

S. Banach [1955]. Theorie des opérations linéaires. New York: Chelsea Publ. Co.

N.K. Bari [1951]. Biorthogonal systems and bases in Hilbert space. Moskov Gos Univ Ucenye Zapinski 148, Matematika 4, 69–107. (Russian)

B. Beauzamy [1985]. Un operateur sans sous-espace invariant: simplification de l’exemple de P. Enflo. Integral Eqs. and Operator Theory, 8, 314–384.

S.K. Berberian [1959]. Note on a theorem of Fuglede and Putnam. Proc. Amer. Math. Soc., 10, 175–182.

C. Berg, J.P.R. Christensen, and P. Ressel [1984]. Harmonic Analysis on Semigroups. New York: Springer-Verlag.

A.R. Bernstein and A. Robinson [1966]. Solution of an invariant subspace problem of K.T. Smith and P.R. Halmos. Pacific J. Math., 16, 421–431.

A. Beurling [1949]. On two problems concerning linear transformations in Hilbert space. Acta. Math., 81, 239–255.

F.F. Bonsall [1986]. Decompositions of functions as sums of elementary functions. Quart J. Math. 37, 129–136.

F.F. Bonsall and J. Duncan [1973]. Complete Normed Algebras. Berlin: Springer-Verlag.

N. Bourbaki [1967]. Espaces Vectoriels Topologiques. Paris: Hermann.

L. de Branges [1959]. The Stone-Weierstrass Theorem. Proc. Amer. Math. Soc., 10, 822-824.

A Brown [1974]. A version of multiplicity theory. Topics in Operator Theory. Math. Surveys A.M.S., Vol. 13, 129–160.

R.C. Buck [1958]. Bounded continuous functions on a locally compact space. Michigan Math. J., 5, 95–104.

J.W. Calkin [1939]. Abstract symmetric boundary conditions. Trans. Amer. Math. Soc., 45, 369–442.

S.R. Caradus, W.E. Pfaffenberger, and B. Yood [1974]. Calkin Algebras and Algebras of Operators of Banach Spaces. New York: Marcel Dekker.

L. Carleson [1966]. On convergence and growth of partial sums of Fourier series. Acta. Math., 116, 135–157.

P. Chernoff [1983]. A semibounded closed symmetric operator whose square has trivial domain. Proc. Amer. Math. Soc., 89, 289–290.

M.D. Choi [1983]. Tricks or treats with the Hilbert matrix. Amer. Math. Monthly, 90, 301–312.

J.A. Clarkson [1936]. Uniformly convex spaces. Trans. Amer. Math. Soc., 40, 396–414.

J.B. Conway [1978]. Functions of One Complex Variable. New York: Springer-Verlag.

J.B. Conway [1981]. Subnormal Operators. Boston: Pitman.

J.B. Conway [1985]. Arranging the disposition of the spectrum. Proc. Royal Irish Acad. 85A, 139–142.

R. Courant and D. Hilbert [1953]. Methods of Mathematical Physics. New York: Interscience.

A.M. Davie [1973]. The approximation problem for Banach spaces. Bull. London Math. Soc., 5, 261–266.

A.M. Davie [1975]. The Banach approximation problem. J. Approx. Theory, 13, 392-394.

W.J. Davis, T. Figiel, W.B. Johnson, and A. Pelczynski [1974]. Factoring weakly compact operators. J. Functional Anal., 17, 311–327.

J. Diestel [1984]. Sequences and series in Banach spaces. New York: Springer-Verlag.

J. Dieudonné [1985]. The index of operators in Banach spaces. Integral Equations and Operator Theory 8, 580–589.

W.F. Donoghue [1957]. The lattice of invariant subspaces of a completely continuous quasi-nilpotent transformation. Pacific J. Math., 7, 1031–1035.

R.Ġ. Douglas [1969]. On the operator equation S\* X T = X and related topics. Acta. Sci. Math. (Szeged), 30, 19–32.

J. Dugundji [1966]. Topology. Boston: Allyn and Bacon.

N. Dunford and J. Schwartz [1958]. Linear Operators. I. New York: Interscience.

N. Dunford and J. Schwartz [1963]. Linear Operators. II. New York: Interscience.

J. Dyer, E. Pedersen, and P. Porcelli [1972]. An equivalent formulation of the invariant subspace conjecture. Bull. Amer. Math. Soc., 78, 1020–1023.

H. Dym and H.P. Mckean [1972]. Fourier Series and Integrals. New York and London: Academic Press.

D.A. Edwards [1961]. On translates of L∞-functions. J. London Math. Soc. 36, 431-432.

D.A. Edwards [1986]. A short proof of a theorem of Machado. Math. Proc. Camb. Phil. Soc. 99, 111–114.

P. Enflo [1973]. A counterexample to the approximation problem in Banach spaces. Acta. Math., 130, 309–317.

P. Enflo [1987]. On the invariant subspace problem for Banach spaces. Acta. Math. 158, 213-313.

J. Ernest [1976]. Charting the operator terrain. Memoirs Amer. Math. Soc., Vol. 71.

P.A. Fillmore, J.G. Stampfli, and J.P. Williams [1972]. On the essential numerical range, the essential spectrum, and a problem of Halmos. Acta Sci. Math. (Szeged) 33, 179–192.

B. Fuglede [1950]. A commutativity theorem for normal operators. Proc. Nat. Acad. Sci., 36, 35–40.

T.W. Gamelin [1969]. Uniform Algebras. Englewood Cliffs: Prentice-Hall.

L. Gillman and M. Jerison [1960]. Rings of Continuous Functions. Princeton: Van Nostrand. Reprinted by Springer-Verlag, New York.