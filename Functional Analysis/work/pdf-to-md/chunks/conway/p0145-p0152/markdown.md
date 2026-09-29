which is weak-star open in $\mathcal { X } ^ { * }$ . Hence $\tilde { \rho } \colon ( \mathcal { X } ^ { \ast } / \mathcal { M } ^ { \perp } , \eta ^ { \ast } ) { \rightarrow } ( \mathcal { M } ^ { \ast } , \mathrm { w k } ^ { \ast } )$ is continuous.

How is the topology on $x ^ { * } / d ^ { 1 }$ defined? If $x \in \mathcal { X } ,   p _ { x } ( x ^ { * } ) = | \langle x , x ^ { * } \rangle |$ is a typical seminorm on $\mathcal { X } ^ { * }$ . By Proposition 2.1, the topology on $x ^ { * } / d ^ { \perp }$ is defined by the seminorms $\{ \bar { p } _ { x } : x { \in } { \mathcal { X } } \}$ , where

$$
\bar { p } _ { x } ( x ^ { * } + \mathcal { M } ^ { \perp } ) = \operatorname* { i n f } \{ | \langle x , x ^ { * } + z ^ { * } \rangle | : z ^ { * } \in \mathcal { M } ^ { \perp } \} .
$$

## 2.4. Claim. If $x \notin \mathcal { M } ,$ then $\bar { p } _ { x }   =   0$

In fact, let $\mathcal { L } = \{ \alpha x \colon \alpha \in \mathbb { F } \}$ . If $x \neq M ,$ then $\mathcal { X } \cap \mathcal { M } = ( 0 )$ . Since dim $\mathcal { L } < \infty$ $\mathcal { M }$ is topologically complemented in $2 + 1 6$ . Let $x ^ { * } \in \mathcal { X } ^ { * }$ and define $f ;$ $\mathcal { X } + \mathcal { M } \rightarrow \mathbb { F }$ by $f(\alpha x + y) = \langle y, x^* \rangle$ for y in M and α in F. Because $\mathcal { M }$ is topologically complemented in $2 + 1 4 .$ if $\alpha _ { i } x + y _ { i }   \rightarrow   0 ,$ then $y _ { i }   \to   0 .$ Hence $f ( \alpha _ { i } x + y _ { i } ) = \langle y _ { i } , x ^ { * } \rangle \to 0$ Thus f is continuous. By the Hahn-Banach Theorem, there is an x\* in $\mathcal { X } ^ { * }$ that extends f. Note that $x ^ { * } - x _ { 1 } ^ { * } { \in } \mathcal { M } ^ { \perp }$ . Thus $\bar { p } _ { x } ( x ^ { * } + \mathcal { M } ^ { \perp } ) = \bar { p } _ { x } ( x _ { 1 } ^ { * } + \mathcal { M } ^ { \perp } ) \leqslant p _ { x } ( x _ { 1 } ^ { * } ) = | \zeta x , x _ { 1 } ^ { * } \rangle | = 0 .$ This proves (2.4).

Now suppose that {x\* + M} is a net in $x ^ { * } / M ^ { \perp }$ such that $\tilde { \rho } ( x _ { i } ^ { * } + \mathcal { M } ^ { \perp } ) = x _ { i } ^ { * } | \mathcal { M } \rightarrow 0 ( \mathrm { w k } ^ { * } )$ in $\mathcal { M } ^ { * }$ . If $x   \in   \mathcal { X }$ and $x \neq M ,$ ,the Claim (2.4) implies that $\bar { p } _ { x } ( x _ { i } ^ { * } + \mathcal { M } ^ { \perp } ) = 0 .$ If $x \in \mathcal { M }$ then $\bar { p } _ { x } ( x _ { i } ^ { * } + \mathcal { M } ^ { \perp } ) \leqslant | \langle x , x _ { i } ^ { * } \rangle | \to 0 .$ Thus $x _ { i } ^ { * } + \mathcal { M } ^ { \perp }   \rightarrow   0 ( \eta ^ { * } )$ and $\tilde { \rho }$ is a weak-star homeomorphism. ■

## EXERCISES

1. In relation to Claim 2.4, show that if $\mathcal { X } \leqslant \mathcal { X }$ , dim $\mathcal { L } < \infty$ , and $\mathcal { M } \leqslant \mathcal { X }$ , then $\mathcal { I } + \mathcal { M }$ is closed.

2. Show that if $\mathcal { M } \leqslant \mathcal { X }$ and M is topologically complemented in $\mathcal { X } ,$ then $\mathcal { M } ^ { \perp }$ is topologically complemented in $\mathcal { X } ^ { * }$ and that its complement is weak-star and linearly homeomorphic to $x ^ { * } / d ^ { 1 }$

## §3. Alaoglu's Theorem

If £ is any normed space, let's agree to denote by ball X the closed unit ball in X. So ball $\mathcal { X } \equiv \left\{ x { \in } \mathcal { X } \colon \|   x   \| \leqslant 1 \right\}$

3.1. Alaoglu's Theorem. If X is a normed space, then ball $\mathcal { X } ^ { * }$ is weak-star compact.

PRoOF. For each x in ball x, let $D_{x} \equiv \left\{ \alpha \in \mathbb{F}: |\alpha| \leqslant 1 \right\}$ and put $D =$ $\prod \{ D_{x} : x \in \mathrm{ball} \mathcal{X} \}$ . By Tychonoff's Theorem, D is compact. Define τ: ball $\mathcal { X } ^ { * }   \rightarrow   D$ by

$$
\tau ( x ^ { * } ) ( x ) = \langle x , x ^ { * } \rangle .
$$

That is, $\tau ( x ^ { * } )$ is the element of the product space D whose x coordinate is $\langle x , x ^ { * } \rangle$ . It will be shown that τ is a homeomorphism from (ball $\mathcal { X } ^ { * }$ , wk\*)

onto $\tau ( \mathrm { b a l l }   \mathcal { X } ^ { * } )$ with the relative topology from D, and that $\tau ( \mathrm { b a l l }   \mathcal { X } ^ { * } )$ is closed in D. Thus it will follow that $\tau ( \mathrm { b a l l }   \mathcal { X } ^ { * } )$ , and hence ball $\mathcal { X } ^ { * }$ , is compact.

To see that τ is injective, suppose that $\tau ( x _ { 1 } ^ { * } ) = \tau ( x _ { 2 } ^ { * } )$ . Then for each x in ball $\mathcal { X } , \langle x , x _ { 1 } ^ { * } \rangle = \langle x , x _ { 2 } ^ { * } \rangle$ . It follows by definition that $x _ { 1 } ^ { * } = x _ { 2 } ^ { * }$

Now let $\left\{ x _ { i } ^ { * } \right\}$ be a net in ball $\mathcal { X } ^ { * }$ such that $x _ { i } ^ { * }   \rightarrow   x ^ { * }$ Then for each x in ball $\mathcal { X } , \tau ( x _ { i } ^ { * } ) ( x ) = \langle x , x _ { i } ^ { * } \rangle \rightarrow \langle x , x ^ { * } \rangle = \tau ( x ^ { * } ) ( x )$ . That is, each coordinate of $\{ \tau ( x _ { i } ^ { * } ) \}$ converges to $\tau ( x ^ { * } )$ Hence $\tau ( x _ { i } ^ { * } )   \to   \tau ( x ^ { * } )$ and τ is continuous.

Let $x _ { i } ^ { * }$ be a net in ball $\mathcal { X } ^ { * }$ , let $f \in D$ , and suppose $\tau ( x _ { i } ^ { * } )   \rightarrow   f$ in D. So $f(x) = \lim_{i \to \infty} \langle x, x_i^* \rangle$ exists for every x in ball £. If $x   \in   \mathcal { X }$ , let $\alpha   >   0$ such that $\| \alpha x \| \leqslant 1$ . Then define $f(x) = \alpha^{-1} f(\alpha x)$ . If also $\beta   >   0$ such that $\| \beta x \| \leqslant 1$ , then $\alpha^{-1} f(\alpha x) = \alpha^{-1} \lim \left\langle \alpha x, x_i^* \right\rangle = \beta^{-1} \lim \left\langle \beta x, x_i^* \right\rangle = \beta^{-1} f(\beta x).$ So $f ( x )$ is well defined. It is left as an exercise for the reader to show that $f \colon { \mathcal { X } }   \to   \mathbb { F }$ is a linear functional. Also, if $\|x\| \leqslant 1,\ f(x) \in D_x$ sO $|f(x)| \leqslant 1$ . Thus $x ^ { * } \in$ ball $\mathcal { X } ^ { * }$ and $\tau ( x ^ { * } ) = f .$ Thus $\tau ( \mathrm { b a l l }   \mathcal { X } ^ { * } )$ is closed in D. This implies that τ(ball $\mathcal { X } ^ { * } )$ is compact. The proof that $\tau ^ { - 1 }$ is continuous is left to the reader.■

## EXERCISES

1. Show that the functional f occurring in the proof of Alaoglu's Theorem is linear.

2. Let $\mathcal { X }$ be a LCS and let V be an open neighborhood of 0. Show that $V ^ { \circ }$ is weak-star compact in $\mathcal { X } ^ { * }$

3. If $\mathcal { X }$ is a Banach space, show that there is a compact space X such that $\mathcal { X }$ is isometrically isomorphic to a closed subspace of $C ( X )$

## §4. Reflexivity Revisited

In §III.11 a Banach space $\mathcal { X }$ was defined to be reflexive if the natural embedding of $\mathcal { X }$ into its double dual, $\mathcal { X } ^ { * * }$ , is surjective. Recall that if $x   \in   \mathcal { X }$ then the image of x in $\mathcal { X } ^ { * * } , \hat { x } ,$ is defined by (using our recent notation)

$$
\langle x ^ { * } , { \hat { x } } \rangle = \langle x , x ^ { * } \rangle
$$

for all $x ^ { * }$ in $\mathcal { X } ^ { * }$ . Also recall that the map $x   \mapsto   { \hat { x } }$ is an isometry.

To begin, note that $\mathcal { X } ^ { * * }$ , being the dual space of $\mathcal { X } ^ { * }$ , has its weak-star topology $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ . Also note that if  is considered as a subspace of $\mathcal { X } ^ { * * }$ then the topology $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ when relativized to $\mathcal { X }$ is $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } ) ,$ , the weak topology on $\mathcal { X }$ This will be important later when it is combined with Alaoglu's Theorem applied to $\mathcal { X } ^ { * * }$ in the discussion of reflexivity. But now the next result must occupy us.

4.1. Proposition. If X is a normed space, then ball $\mathcal { X }$ is $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ dense in ball $\mathcal { X } ^ { * * }$

PROOF. Let B = the $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ closure of ball $\mathcal { X }$ in $\mathcal { X } ^ { * * }$ ; clearly, $B \subseteq \mathrm{ball}   \mathcal{X}^{* *}$ If there is an $x _ { 0 } ^ { * * }$ in ball ${ \mathcal { X } } ^ { * * } \backslash B ,$ then the Hahn-Banach Theorem implies there is an $x ^ { * }$ in $\mathcal { X } ^ { * }$ an $\alpha$ in $\mathbf { R } ,$ and an $\varepsilon   >   0$ such that

$$
\operatorname { R e } \langle x , x ^ { * } \rangle < \alpha < \alpha + \varepsilon < \operatorname { R e } \langle x ^ { * } , x _ { 0 } ^ { * * } \rangle
$$

for all x in ball $\mathcal { X } .$ (Exactly how does the Hahn-Banach Theorem imply this?) Since $0 \in \mathrm{bal} \mathcal{X}, 0 < \alpha.$ Dividing by α and replacing $x ^ { * }$ by $\alpha ^ { - 1 } x ^ { * }$ , it may be assumed that there is an $x ^ { * }$ in $\mathcal { X } ^ { * }$ and an $\varepsilon   >   0$ such that

$$
\operatorname { R e } \langle x , x ^ { * } \rangle < 1 < 1 + \varepsilon < \operatorname { R e } \langle x ^ { * } , x _ { 0 } ^ { * * } \rangle
$$

for all x in ball $\mathcal { X } .$ Since $e ^ { i \theta } x \in \mathrm { b a l l } { \mathcal { X } }$ whenever x∈ball $\mathcal { X } ,$ this implies that $| \langle x , x ^ { * } \rangle | \leqslant 1 \mathrm { i f } \| x \| \leqslant 1$ . Hence $x ^ { * } \epsilon$ ball $\mathcal { X } ^ { * }$ . But then $1 + \varepsilon < \mathrm{Re} \langle x^*, x^*_0 \rangle \leqslant$ $| \langle x ^ { * } , x _ { 0 } ^ { * * } \rangle | \leqslant \| x _ { 0 } ^ { * * } \| \leqslant 1$ , a contradiction.

4.2. Theorem. If X is a Banach space, the following statements are equivalent.

(a) $\mathcal { X }$ is reflexive.

(b) $\mathcal { X } ^ { * }$ is reflexive.

(c) $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } ) = \sigma ( \mathcal { X } ^ { * } , \mathcal { X } ^ { * * } ) .$

(d) ball X is weakly compact.

PROOF. $(a) \Rightarrow (c)$ This is clear since $\mathcal { X } = \mathcal { X } ^ { * * } .$

(d)⇒(a): Note that $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } ) | \mathcal { X } = \sigma ( \mathcal { X } , \mathcal { X } ^ { * } )$ . By (d), ball $\mathcal { X }$ is $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ closed in ball $\mathcal { X } ^ { * * }$ . But the preceding proposition implies ball £ is $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ dense in ball $\mathcal { X } ^ { * * }$ . Hence ball $\mathcal { X } = \mathrm { b a l l } \mathcal { X } ^ { * * }$ and so $\mathcal { X }$ is reflexive.

(c)⇒(b): By Alaoglu's Theorem, ball $\mathcal { X } ^ { * }$ is $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } )$ -compact. By (c), ball $\mathcal { X } ^ { * }$ is $\sigma ( \mathcal { X } ^ { * } , \mathcal { X } ^ { * * } )$ compact. Since it has already been shown that (d) implies (a), this implies that $\mathcal { X } ^ { * }$ is reflexive.

(b)⇒(a): Now ball $\mathcal { X }$ is norm closed in $\mathcal { X } ^ { * * }$ ; hence ball $\mathcal { X }$ is $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * * * } )$ closed in $\mathcal { X } ^ { * * }$ (Corollary 1.5). Since $\mathcal { X } ^ { * } = \mathcal { X } ^ { * * * }$ by (b), this says that ball $\mathcal { X }$ is $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ closed in $\mathcal { X } ^ { * * }$ . But, according to (4.1), ball $\mathcal { X }$ is $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ dense in ball $\mathcal { X } ^ { * * }$ . Hence ball X = ball $\mathcal { X } ^ { * * }$ and $\mathcal { X }$ is reflexive.

$(a) \Rightarrow (d)$ By Alaoglu's Theorem, ball $\mathcal { X } ^ { * * }$ is $\sigma ( \mathcal { X } ^ { * * } , \mathcal { X } ^ { * } )$ compact. Since $\mathcal { X } = \mathcal { X } ^ { * * }$ , this says that ball x is $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } )$ compact. ■

4.3. Corollary. If X is a reflexive Banach space and $\mathcal { M } \leqslant \mathcal { X }$ , then $\mathcal { M }$ is a reflexive Banach space.

PRoOF. Note that ball $\mathcal { M } = \mathcal { M } \cap [ \mathrm { b a l l }   \mathcal { X } ] .$ , so ball M is $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } )$ compact. It remains to show that $\sigma ( \mathcal { X } , \mathcal { X } ^ { * } ) | \mathcal { M } = \sigma ( \mathcal { M } , \mathcal { M } ^ { * } )$ . But this follows by (2.3). (How?) ■

Call a sequence $\{ x _ { n } \}$ in $\mathcal { X }$ a weakly Cauchy sequence if for every $x ^ { * }$ in $\mathcal { X } ^ { \ast } ,   \left\{ \left\langle x _ { n } , x ^ { \ast } \right\rangle \right\}$ is a Cauchy sequence in F.

4.4. Corollary. If X is reflexive, then every weakly Cauchy sequence in $\mathcal { X }$ converges weakly. That $i s , \mathcal { X }$ is weakly sequentially complete.

PROOF. Since $\{ \langle x _ { n } , x ^ { * } \rangle \}$ is a Cauchy sequence in $\mathbf { F }$ for each $x ^ { * }$ in $\mathcal { X } ^ { * } ,   \{ x _ { n } \}$ is weakly bounded. By the PUB there is a constant M such that $\| x _ { n } \| \leqslant M$ for all $n \geqslant 1$ . But $\{ x { \in } { \mathcal { X } } { : } \|   x   \| \leqslant M \}$ is weakly compact since $\mathcal { X }$ is reflexive. Thus there is an x in $\mathcal { X }$ such that $x _ { n } \xrightarrow [ \mathrm { c l } ] { } x$ weakly. But for each $x ^ { * }$ in $\mathcal { X } ^ { * }$ lim $\langle x _ { n } , x ^ { * } \rangle$ exists. Hence $\langle x _ { n } , x ^ { * } \rangle \to \langle x , x ^ { * } \rangle$ , so $x _ { n }   \to   x$ weakly.

Not all Banach spaces are weakly sequentially complete.

4.5. Example. $C [ 0 , 1 ]$ is not weakly sequentially complete. In fact, let $f _ { n } ( t ) = ( 1 - n t )$ if $0 \leqslant t \leqslant 1 / n$ and $f _ { n } ( t ) = 0$ if $1 / n \leqslant t \leqslant 1$ . If $\mu { \in } M [ 0 , 1 ]$ , then $\int f _ { n } d \mu \rightarrow \mu ( \{ 0 \} )$ by the Monotone Convergence Theorem. Hence $\{ f _ { n } \}$ is a weakly Cauchy sequence. However, $\{ f _ { n } \}$ does not converge weakly to any continuous function on [0, 1].

4.6. Corollary. If X is a reflexive Banach space, $\mathcal { M } \leqslant \mathcal { X } ,$ and $x _ { 0 } \in \mathcal { X } \backslash \mathcal { M }$ , then there is a point $y _ { 0 }$ in M such that $\|x_{0}-y_{0}\|=\mathrm{dist}(x_{0},\mathcal{M})$

PROOF. $x   \mapsto   \|   x - x _ { 0 }   \|$ is weakly lower semicontinuous (Exercise 1.9). If $d = \mathrm { d i s t } ( x _ { 0 } , \mathcal { M } ) ,$ , then $\mathcal { M } \cap \left\{ x : \| x - x _ { 0 } \| \leqslant 2 d \right\}$ is weakly compact and a lower semicontinuous function attains its minimum on a compact set. ■

It is not generally true that the distance from a point to a linear subspace is attained. If $\mathcal { M } \subseteq \mathcal { X }$ , call M proximinal if for every x in $\mathcal { X }$ there is a y in $\mathcal { M }$ such that $\|x - y\| =  dist (x, \mathcal{M})$ . So if ¿ is reflexive, Corollary 4.6 implies that every closed linear subspace of $\mathcal { X }$ is proximinal. If $\mathcal { X }$ is any Banach space and $\mathcal { M }$ is a finite dimensional subspace, then it is easy to see that M is proximinal. How about if dim $( \mathcal { X } / \mathcal { M } ) < \infty ?$

4.7. Proposition. If X is a Banach space and $x ^ { * }   \in   \mathcal { X } ^ { * }$ , then ker $x ^ { * }$ is proximinal if and only if there is an x in ${ \mathcal { X } } ,   \|   x   \| = 1$ , such that $\left\langle x , x ^ { * } \right\rangle = \left\| x ^ { * } \right\|$

PROOF. Let $\mathcal { M } = \ker x ^ { * }$ and suppose that M is proximinal. If $f \colon { \mathcal { X } } / { \mathcal { M } } \to \mathbb { F }$ is defined by $f(x + \mathcal{M}) = \langle x, x^* \rangle$ , then f is a linear functional and $\| f \| = \|   x ^ { \star }   \|$ . Since dim $\mathcal { X } / \mathcal { M } = 1$ , there is an x in $\mathcal { X }$ such that $\| x + \mathcal { M } \| = 1$ and $f ( x + { \mathcal { M } } ) = \| f \|$ . Because M is proximinal, there is a y in $\mathcal { M }$ such that $1 = \|   x + { \mathcal { M } }   \| = \|   x + y   \|$ . Thus $\langle x + y, x^* \rangle = \langle x, x^* \rangle = f(x + \mathcal{M}) = \| f \| =$ $\| x ^ { * } \|$

Now assume that there is an $x _ { 0 }$ in $\mathcal { X }$ such that $\| x _ { 0 } \| = 1$ and $\langle x _ { 0 } , x ^ { * } \rangle = \| x ^ { * } \|$ . If $x   \in   \mathcal { X }$ and $\| x + \mathcal { M } \| = \alpha > 0 ,$ then $\| \alpha ^ { - 1 } x + \mathcal { M } \| = 1$ . But also $\| x _ { 0 } + \mathcal { M } \| = 1 . ( \mathrm { W h y } ? )$ Since dim $\mathcal { X } / \mathcal { M } = 1$ , there is a $\beta$ in $\mathbb { F } ,   | \beta | = 1$ such that $\alpha^{-1}x + \mathcal{M} = \beta(x_0 + \mathcal{M})$ . Hence $\alpha ^ { - 1 } x - \beta x _ { 0 } \in \mathcal { M } .$ , or, equivalently, $x - \alpha \beta x _ { 0 } \in \mathcal { M }$ .However, $\| x - (x - \alpha \beta x_0) \| = \| \alpha \beta x_0 \| = \alpha =  dist (x, \mathcal{M})$ . So the distance from x to $\mathcal { M }$ is attained at $x - \alpha \beta x _ { 0 }$ ■

4.8. Example. If $L \colon C [ 0 , 1 ]   \to   \mathbb { F }$ is defined by

$$
L ( f ) = \int _ { 0 } ^ { 1 / 2 } f ( x ) d x - \int _ { 1 / 2 } ^ { 1 } f ( x ) d x ,
$$

then ker L is not proximinal

There is a result in James [1964b] that states that a Banach space is reflexive if and only if every closed hyperplane is proximinal. This result is very deep. A nice reference on reflexivity is Yang [1967].

## EXERCISES

1. Show that if X is reflexive and $\mathcal { M } \leqslant \mathcal { X }$ , then $x / M$ is reflexive.

2. If $\mathcal { X }$ is a Banach space, $\mathcal { M } \leqslant \mathcal { X }$ , and both M and $\mathcal { X } / \mathcal { M }$ are reflexive, must $\mathcal { X }$ be reflexive?

3. If $( X , \Omega , \mu )$ is a σ-finite measure space, show that $L ^ { 1 } ( X , \Omega , \mu )$ is reflexive if and only if it is finite dimensional.

4. Give the details of the proofs of the statements made in Example 4.5.

5. Verify the statement made in Example 4.8.

6. If $( X , \Omega , \mu )$ is a σ-finite measure space, show that $L ^ { \infty } ( \mu )$ is weak-star sequentially complete but is reflexive if and only if it is finite dimensional.

7. Let X be compact and suppose there is a norm on C(X) that is given by an inner product making C(X) into a Hilbert space such that for every x in X the functional $f { \mapsto } f ( x )$ on C(X) is continuous with respect to the Hilbert space norm. Show that X is finite.

## §5. Separability and Metrizability

The weak and weak-star topologies on an infinite dimensional Banach space are never metrizable. It is possible, however, to show that under certain conditions these topologies are metrizable when restricted to bounded sets. In applications this is often sufficient.

5.1. Theorem. If X is a Banach space, then ball $\mathcal { X } ^ { * }$ is weak-star metrizable if and only if X is separable.

PrOOF. Assume that $\mathcal { X }$ is separable and let $\{ x _ { n } \}$ be a countable dense subset of ball ¿. For each n let $D_{n}=\left\{ \alpha \in \mathbb{F}:|\alpha| \leqslant 1 \right\}$ . Put $X = \prod_{n = 1}^{\infty} D_{n};$ X is a compact metric space. So if (ball $\mathcal { X } ^ { * } , \mathbf { w } \mathbf { k } ^ { * } )$ is homeomorphic to a subset of $X ,$ ball $\mathcal { X } ^ { * }$ is weak-star metrizable

Define τ: ball $\mathcal { X } ^ { * }   \to   X$ by $\tau ( x ^ { * } ) = \{ \langle x _ { n } , x ^ { * } \rangle \}$ . If $\left\{ x _ { i } ^ { * } \right\}$ is a net in ball $\mathcal { X } ^ { * }$ and $x _ { i } ^ { * }   \rightarrow   x ^ { * } \quad ( \mathbf { w } \mathbf { k } ^ { * } ) ,$ then for each $n \geqslant 1,\quad \langle x_n, x_i^* \rangle \to \langle x_n, x^* \rangle;$ hence $\tau ( x _ { i } ^ { * } )   \to   \tau ( x ^ { * } )$ and τ is continuous. If $\tau ( x ^ { * } ) = \tau ( y ^ { * } ) , \; \langle x _ { n } , x ^ { * } - y ^ { * } \rangle = 0$ for all n. Since $\{ x _ { n } \}$ is dense, $x ^ { * } - y ^ { * } = 0$ . Thus τ is injective. Since ball $\mathcal { X } ^ { * }$ is $\mathbf { w } \mathbf { k } ^ { * }$ compact, τ is a homeomorphism onto its image (A.2.8) and ball $\mathcal { X } ^ { * }$ is $\mathbf { w } \mathbf { k } ^ { * }$ metrizable.

Now assume that (ball $\mathcal { X } ^ { * } , \mathbf { w } \mathbf { k } ^ { * } )$ is metrizable. Thus there are open sets $\left\{ U _ { n } ; n \geqslant 1 \right\}$ in (ball $\mathcal { X } ^ { * } , \mathbf { w } \mathbf { k } ^ { * } )$ such that $\mathbf { 0 } { \in } U _ { \pmb { n } }$ and $\bigcap_{n = 1}^{\infty} U_{n} = (0)$ . By the definition of the relative weak-star topology on ball $\mathcal { X } ^ { * }$ , for each n there is a finite set $F _ { n }$ contained in $\mathcal { X }$ such that $\{ x ^ { * } { \in } \mathsf { b a l l } \; { \mathcal { X } } ^ { * } { : }   | \langle x , x ^ { * } \rangle | < 1$ for all $x$ in $\left\{ F _ { n } \right\} \subseteq U _ { n }$ . Let $F = \bigcup_{n = 1}^{\infty} F_{n};$ sO $F$ is countable. Also, $^ { \perp } ( F ^ { \perp } )$ is the closed linear span of $F$ and this subspace of $\mathcal { X }$ is separable. But if $x ^ { * }   \in   F ^ { \perp }$ , then for each $n \geqslant 1$ and for each x in $F _ { n } , \left| \left\langle x , x ^ { * } / \| x ^ { * } \| \right\rangle \right| = 0 < 1$ . Hence $x ^ { * } / \left\|   x ^ { * }   \right\|   \in   U _ { n }$ for all $n \geqslant 1$ ; thus $x ^ { * }   =   0$ Since $F ^ { \perp } = ( 0 ) , \quad ^ { \perp } ( F ^ { \perp } ) = \mathcal { X }$ and $\mathcal { X }$ must be separable.

Is there a corresponding result for the weak topology? $\operatorname { I f } { \mathcal { X } } ^ { * }$ is separable, then the weak topology on ball $\mathcal { R }$ is metrizable. In fact, this follows from Theorem 5.1 if the embedding of $\mathcal { X }$ into $\mathcal { X } ^ { * * }$ is considered. This result is not very useful since there are few examples of Banach spaces $\mathcal { X }$ such that $\mathcal { X } ^ { * }$ is separable. Of course if $\mathcal { X }$ is separable and reflexive, then $\mathcal { X } ^ { * }$ is separable (Exercise 3), but in this case the weak topology on $\mathcal { X }$ is the same as its weak-star topology when $\mathcal { X }$ is identified with $\mathcal { X } ^ { * * }$ . Thus (5.1) is adequate for a discussion of the weak topology on the unit ball of a separable reflexive space. If $\mathcal { X } = c _ { 0 }$ , then $\mathcal { X } ^ { * } = l ^ { 1 }$ and this is separable but not reflexive. This is one of the few nonreflexive spaces with a separable dual space.

If $\mathcal { X }$ is separable, is (ball $\mathcal { X }$ , wk) metrizable? The answer is no, as the following result of Schur demonstrates.

## 5.2. Proposition. If a sequence in $l ^ { 1 }$ converges weakly, it converges in norm.

PROOF. Recall that $l ^ { \infty } = ( l ^ { 1 } ) ^ { * }$ . Since $l ^ { 1 }$ is separable, Theorem 5.1 implies that ball $l ^ { \infty }$ is $\mathbf { w } \mathbf { k } ^ { * }$ metrizable. By Alaoglu's Theorem, ball $l ^ { \infty }$ is $\mathbf { w } \mathbf { k } ^ { * }$ compact. Hence (ball $l ^ { \infty } , \mathbf { w } \mathbf { k } ^ { * } )$ is a complete metric space and the Baire Category Theorem is applicable.

Let $\{ f _ { n } \}$ be a sequence of elements in $l ^ { 1 }$ such that $f _ { n }   \to   0$ weakly and let $\varepsilon > 0$ . For each positive integer m let

$$
F _ { m } = \{ \phi \in \mathrm { b a l l } l ^ { \infty } : | \langle f _ { n } , \phi \rangle | \leqslant \varepsilon / 3 \mathrm { f o r } n \geqslant m \} .
$$

It is easy to see that $F _ { m }$ is $\mathbf { w } \mathbf { k } ^ { * }$ closed in ball $l ^ { \infty }$ and, because $f _ { n } \to 0 ( \mathbf { w } \mathbf { k } )$ $\bigcup_{m = 1}^{\infty} F_{m} = \mathrm{bal} l^{\infty}$ . By the theorem of Baire, there is an $F _ { m }$ with non-empty weak-star interior.

An equivalent metric on (ball $l ^ { \infty } ,   \mathbf { w } \mathbf { k } ^ { * } )$ is given by

$$
d ( \phi , \psi ) = \sum _ { j = 1 } ^ { \infty } 2 ^ { - j } | \phi ( j ) - \psi ( j ) |
$$

(see Exercise $4 )$ Since $F _ { m }$ has a nonempty $\mathbf { w } \mathbf { k } ^ { * }$ interior, there is a $\phi$ in $F _ { m }$ and a $\delta   >   0$ such that {ψ∈balll∞: $d ( \phi , \psi ) < \delta \} \subseteq F _ { m } .$ Let $J \geqslant 1$ such that $2 ^ { -   ( J   -   1 ) }   <   \delta .$ Fix $n \geqslant m$ and define ψ in $l ^ { \infty }$ by $\psi ( j ) = \phi ( j )$ for $1 \leqslant j \leqslant J$ and $\psi ( j ) = \operatorname{sign}( f _ { n } ( j ) )$ for $j > J$ Thus $\psi ( j ) f _ { n } ( j ) = | f _ { n } ( j ) |$ for $j > J .$ It is easy to see thatψ∈ball $l ^ { \infty }$ . Also, $d(\phi,\psi)=\sum_{j=J+1}^{\infty}2^{-j}|\phi(j)-\psi(j)|\leqslant2\cdot2^{-J}=2^{-(J-1)}<\delta$

So $\psi   \in   F _ { m }$ and hence $| \langle \psi , f _ { m } \rangle | \leqslant \varepsilon / 3$ for $n \geqslant m .$ Thus

## 5.3

$$
\left| \sum_{j = 1}^{J} \phi(j) f_n(j) + \sum_{j = J + 1}^{\infty} |f_n(j)| \right| \leqslant \frac{\varepsilon}{3}
$$

for $n \geqslant m$ But there is an $m _ { 1 } \geqslant m$ such that for $n \geqslant m_{1}, \sum_{j = 1}^{J} \left| f_{n}(j) \right| < \varepsilon / 3$ (Why?) Combining this with (5.3) gives that

$$
\begin{align*}\| f_n \| = & \sum_{j=1}^{\infty} | f_n(j) | \\& < \frac{\varepsilon}{3} + \left| \sum_{j=J+1}^{\infty} | f_n(j) | + \sum_{j=1}^{J} \phi(j) f_n(j) \right| + \left| \sum_{j=1}^{J} \phi(j) f_n(j) \right| \\& < \frac{2\varepsilon}{3} + \sum_{j=1}^{J} | f_n(j) | \\& < \varepsilon.\end{align*}
$$

whenever $n \geqslant m _ { 1 }$

So if (ball l¹, wk) were metrizable, the preceding proposition would say that the weak and norm topologies on $l ^ { 1 }$ agree. But this is not the case (Exercise 1.10).

Also, note that the preceding result demonstrates in a dramatic way that in discussions concerning the weak topology it is essential to consider nets and not just sequences.

A proof of (5.2) that avoids the Baire Category Theorem can be found in Banach [1955], p. 218.

## EXERCISES

1. Let B = ball M[0, 1] and for $\mu , \nu$ in $M [ 0 , 1 ]$ define $d(\mu, v) = \sum_{n = 0}^{\infty} 2^{-n} \left| \int_{0}^{1} x^n   d\mu - \right.$ $\int _ { 0 } ^ { 1 } x ^ { n } d v |$ .Show that d is a metric on $M [ 0 , 1 ]$ that defines the weak-star topology on B but not on M[0, 1].

2. Let X be a compact space and let $\mathcal { U } = \{ ( U , V ) : U , V$ are open subsets of X and cl $U \subseteq V \}$ . For $\boldsymbol { u }   =   ( U , V )$ in U, let $f _ { u } \colon \dot { X } \to [ 0 , 1 ]$ be a continuous function such that $f _ { u } \equiv 1$ on cl U and $f _ { u } \equiv 0$ on $X \backslash V .$ Show: (a) the linear span of $\{ f _ { u } : u \in \mathcal { U } \}$ is dense in $C ( X ) ;$ (b) if X is a metric space, then C(X) is separable; (c) if X is a σ-compact metrizable locally compact space, then $C _ { 0 } ( X )$ is separable. (X is σ-compact if X is the union of a countable number of compact subsets.)

3. If $\mathcal { X }$ is a Banach space and $\mathcal { X } ^ { * }$ is separable, show that (a) $\mathcal { X }$ is separable; (b) if K is a weakly compact subset of $\mathcal { X } ,$ then K with the relative weak topology is metrizable.

4. If $B = \mathrm{bal} l^{\infty}$ , show that $\begin{array} { r } { d ( \phi , \psi ) = \sum _ { j = 1 } ^ { \infty } 2 ^ { - j } | \phi ( j ) - \psi ( j ) | } \end{array}$ defines a metric on B and that this metric defines the weak-star topology on B.

5. Use the type of argument used in the proof of the Principle of Uniform Boundedness to obtain a proof of Proposition 5.2 that does not need the Baire Category Theorem.

6. Show that Proposition 5.2 fails for $l ^ { \pmb { p } }$ if $1 < p < \infty$

# $\S 6 ^ { * }$ . An Application: The Stone-Čech Compactification

Let X be any topological space and consider the Banach space $C _ { b } ( X )$ . Unless some assumption is made regarding X, it may be that $C _ { b } ( X )$ is “very small." If, for example, it is assumed that X is completely regular, then $C _ { b } ( X )$ has many elements. The next result says that this assumption is also necessary in order for $C _ { b } ( X )$ to be “large." But first, here is some notation.

If $x   \in   X$ , let $\delta _ { x } \colon C _ { b } ( X ) \to \mathbb { F }$ be defined by $\delta _ { x } ( f )   =   f ( x )$ for every f in $C _ { b } ( X )$ It is easy to see that $\delta _ { x } \in C _ { b } ( X ) ^ { * }$ and $\| \delta _ { x } \| = 1$ . Let $\Delta \colon X \to C _ { b } ( X ) ^ { * }$ be defined by $\Delta ( x ) = \delta _ { x } . \mathrm { ~ I f ~ } \{ x _ { i } \}$ is a net in X and $x _ { i }   \to   x _ { i }$ then $f ( x _ { i } )   \to   f ( x )$ for every f in $C _ { b } ( X )$ . This says that $\delta _ { x _ { i } }   \rightarrow   \delta _ { x } \left( \mathbf { w } \mathbf { k } ^ { * } \right)$ in $C _ { b } ( X ) ^ { * }$ . Hence ∆: $X   \to   ( C _ { b } ( X ) ^ { * } )$ wk\*) is continuous. Is ∆ a homeomorphism of X onto $\Delta ( X ) ?$

6.1. Proposition. The map $\Delta : X   \to   ( \Delta ( X ) , \mathrm { w k } ^ { * } )$ is a homeomorphism if and only if X is completely regular.

ProoF. Assume X is completely regular. If $x _ { 1 } \neq x _ { 2 }$ , then there is an f in $C _ { b } ( X )$ such that $f ( x _ { 1 } )   =   1$ and $f(x_{2}) = 0;$ thus $\delta _ { x _ { 1 } } ( f ) \neq \delta _ { x _ { 2 } } ( f )$ Hence Δ is injective. To show that $\Delta : X \to ( \Delta ( X ) , \mathrm { w k } ^ { * } )$ is an open map, let U be an open subset of X and let $x _ { 0 } { \in } U$ . Since X is completely regular, there is an f in $C _ { b } ( X )$ such that $f ( x _ { 0 } ) = 1$ and $f \equiv 0$ on $X \backslash U .$ Let $V _ { 1 } = \{ \mu \in C _ { b } ( X ) ^ { * } : \langle f , u \rangle > 0 \}$ Then $V _ { 1 }$ is wk\* open in $C _ { b } ( X ) ^ { * }$ and $V _ { 1 } \cap \Delta ( X ) = \{ \delta _ { x } : f ( x ) > 0 \}$ . So if $V = V _ { 1 } \cap \Delta ( X )$ , V is $\mathbf { w } \mathbf { k } ^ { * }$ open in $\Delta ( X )$ and $\delta _ { x _ { 0 } }   \in   V \subseteq \Delta ( U )$ . Since $x _ { 0 }$ was arbitrary, $\Delta ( U )$ is open in $\Delta ( X )$ . Therefore $\Delta : X \to ( \Delta ( X ) , \mathrm { w k } ^ { * } )$ is a homeomorphism.

Now assume that ∆ is a homeomorphism onto its image. Since (ball $C _ { b } ( X ) ^ { * } , \mathbf { w } \mathbf { k } ^ { * } )$ is a compact space, it is completely regular. Since $\Delta ( X ) \subseteq { \mathrm { b a l l } } \; C _ { b } ( X ) ^ { * } , \; \Delta ( X )$ is completely regular (Exercise 2). Thus X is completely regular.

6.2. Stone-Čech Compactification. If X is completely regular, then there is a compact space βX such that:

(a) there is a continuous map $\Delta \colon X   \to   \beta X$ with the property that $\Delta \colon X   \to   \Delta ( X )$ is a homeomorphism;

(b) $\Delta ( X )$ is dense in $\beta X$

(c) if $f   \in   C _ { b } ( X )$ , then there is a continuous map $f ^ { \beta } \colon \beta X   \to   \mathbb { F }$ such that $f ^ { \beta } \circ \Delta = f .$

Moreover, if Ω is a compact space having these properties, then Ω is homeomorphic to $\beta X$

PROOF. Let $\Delta : X \to C _ { b } ( X ) ^ { * }$ be the map defined by $\Delta ( x ) = \delta _ { x }$ and let $\beta X =$ the weak-star closure of $\Delta ( X )$ in $C _ { b } ( X ) ^ { * }$ . By Alaoglu's Theorem and the fact that $\| \delta _ { x } \| = 1$ for all $x , \beta X$ is compact. By the preceding proposition, (a) holds. Part (b) is true by definition. It remains to show (c).