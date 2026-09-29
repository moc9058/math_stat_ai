closed curves in G such that $\sigma ( a ) \subseteq \operatorname { i n s } \Gamma$ Let Λ be a positively oriented system of closed curves in G such that (ins $\Gamma ) \cup \{ \Gamma \} = \mathrm { c l } ( \mathrm { i n s }   \Gamma ) \subseteq \mathrm { i n s }   \Lambda$ Then

$$
\begin{align*}f(a)g(a) &= - \frac{1}{4\pi^2} \Bigg[ \int_{\Gamma} f(z)(z - a)^{-1} dz \Bigg] \Bigg[ \int_{\Lambda} g(\zeta)(\zeta - a)^{-1} d\zeta \Bigg] \\&= - \frac{1}{4\pi^2} \Bigg]_{\Gamma} \int_{\Lambda} f(z)g(\zeta)(z - a)^{-1}(\zeta - a)^{-1} d\zeta dz \\(b)] &= - \frac{1}{4\pi^2} \int_{\Gamma} \int_{\Lambda} f(z)g(\zeta) \Bigg[ \frac{(z - a)^{-1} - (\zeta - a)^{-1}}{\zeta - z} \Bigg] d\zeta dz \\&= - \frac{1}{4\pi^2} \int_{\Gamma} f(z) \Bigg[ \int_{\Lambda} \frac{g(\zeta)}{\zeta - z} d\zeta \Bigg] (z - a)^{-1} dz \\&\quad + \frac{1}{4\pi^2} \int_{\Lambda} g(\zeta) \Bigg[ \int_{\Gamma} \frac{f(z)}{\zeta - z} dz \Bigg] (\zeta - a)^{-1} d\zeta.\end{align*}
$$

[by (3.9b

But for $\zeta$ on $\Lambda , \zeta \epsilon$ out Γ and hence $\int _ { \Gamma } [ f ( z ) / ( \zeta - z ) ] d z = 0$ (Cauchy's Theorem). If $z   \in   \left\{ \Gamma \right\}$ , then z∈ins Λ and so $\int _ { \Lambda } \left[ g ( \zeta ) / ( \zeta - z ) \right] d \zeta = 2 \pi i g ( z )$ Hence

$$
\begin{aligned}f(a)g(a) = & \frac{1}{2\pi i}\int_{\Gamma}f(z)g(z)(z - a)^{-1}dz \\= & (fg)(a).\end{aligned}
$$

The proof that $( \alpha f + \beta g ) ( a ) = \alpha f ( a ) + \beta g ( a )$ is left to the reader.

(c) and (d). Let $f(z) = z^k, \; k \geqslant 0.$ Let $\gamma(t) = R \exp(2 \pi i t)$ $0 \leqslant t \leqslant 1$ , where $R > \| a \| . \mathrm { S o } \sigma ( a ) \subset \mathrm { i n s } \gamma ,$ and hence

$$
\begin{aligned}f(a) &= \frac{1}{2\pi i}\int_{\gamma}z^{k}(z - a)^{- 1}dz \\&= \frac{1}{2\pi i}\int_{\gamma}z^{k - 1}\left( 1 - \frac{a}{z} \right)^{- 1}dz \\&= \frac{1}{2\pi i}\int_{\gamma}z^{k - 1}\sum_{n = 0}^{\infty}a^{n}/z^{n}dz,\end{aligned}
$$

since $\| a / z \| < 1$ for $| z | = R$ .Since this infinite series converges uniformly for $z \mathbf { o n } \gamma .$

$$
f(a) = \sum_{n = 0}^{\infty} \left[ \frac{1}{2\pi i} \int_{\gamma} \frac{1}{z^{n - k + 1}} dz \right] a^n.
$$

If $n \neq k .$ then $z ^ { - ( n - k + 1 ) }$ has a primitive and hence $\int_{\gamma} z^{-(n-k+1)} dz = 0$ . For $n = k$ this integral becomes $\int_{\gamma} z^{-1}   dz = 2 \pi i.$ Hence $f(a) = a^{k}$

(e) Let $\Gamma = \{ \gamma _ { 1 } , \ldots , \gamma _ { m } \}$ be a positively oriented system of closed curves in

G such that σ(a) ⊆ ins Γ. Fix $1 \leqslant k \leqslant m;$ then

$$
\begin{align*}& \left\| \int_{\gamma_k} f_n(z)(z-a)^{-1} dz - \int_{\gamma_k} f(z)(z-a)^{-1} dz \right\| \\& \quad = \left\| \int_{0}^{1} \left[ f_n(\gamma_k(t)) - f(\gamma_k(t)) \right] \left[ \gamma_k(t) - a \right]^{-1} d\gamma_k(t) \right\| \\& \quad \leqslant \int_{0}^{1} \left| f_n(\gamma_k(t)) - f(\gamma_k(t)) \right| \left\| \left[ \gamma_k(t) - a \right]^{-1} \right\| d|\gamma_k|(t).\end{align*}
$$

Now $t \mapsto \| \left[ \gamma _ { k } ( t ) - a \right] ^ { - 1 } \|$ is continuous on [0, 1] and hence bounded by some constant, say M. Thus

$$
\begin{align*}\left\| \int_{\gamma_k} f_n(z)(z-a)^{-1} dz - \int_{\gamma_k} f(z)(a-a)^{-1} dz \right\| \\\leq M \| \gamma_k \| \max \left\{ |f_n(z) - f(z)| : z \in \{\gamma_k\} \right\},\end{align*}
$$

where $\| \gamma _ { k } \|$ is the total variation (length) of $\gamma _ { k }$ . By hypothesis it follows that $\| f _ { n } ( a ) - f ( a ) \| \to 0$ as $n   \to   \infty$

(b) If $p(z) = \sum_{k = 0}^{n} \alpha_{k} z^{k}$ is a polynomial, then (a), (c), and (d) combine to give that $p(a)=\sum_{k = 0}^{n}\alpha_{k}a^{k}$ . Now let $f ( z ) = \sum _ { k = 0 } ^ { \infty } \alpha _ { k } z ^ { k }$ have radius of convergence $R > r ( a )$ , the spectral radius of a. If $p_{n}(z)=\sum_{k = 0}^{n}\alpha_{k}z^{k}, p_{n}(z) \rightarrow f(z)$ uniformly on compact subsets of $\left\{ z \colon | z | < R \right\}$ . By (e), $p _ { n } ( a )   \to   f ( a )$ . So (b) follows. ■

The Riesz Functional Calculus is used in the study of Banach algebras and is especially useful in the study of linear operators on a Banach space (Sections 6 and 7). Now our attention must focus on the basic properties of this functional calculus. The first such property is its uniqueness.

4.8. Proposition. Let A be a Banach algebra with identity and let $a \in \mathcal { A }$ Let $\tau \colon \mathrm { H o l } ( a ) \to { \mathcal { A } }$ be a homomorphism such that $(a) \tau(1) = 1, (b) \tau(z) = a, (c) if \{f_n\}$ is a sequence of analytic functions on an open set G such that $\sigma ( a ) \subseteq G$ and $f _ { n } ( z )   \to   f ( z )$ uniformly on compact subsets of G, then $\tau ( f _ { n } ) \to \tau ( f )$ Then $\tau ( f )   =   f ( a )$ for every f in Hol(a).

PRooF. The proof uses Runge's Theorem (III.8.1), but first it must be shown that $\tau ( f ) = f ( a )$ whenever f is a rational function. If $n \geqslant 1 , \tau ( z ^ { n } ) = \tau ( z ) ^ { n } = a ^ { n } ;$ hence $\tau ( p ) = p ( a )$ for any polynomial p. Let q be a polynomial such that q never vanishes on $\sigma ( a ) ,$ so $1 / q \in \mathrm { H o l } ( a )$ Also, $1 = \tau(1) = \tau(q \cdot q^{-1}) = \tau(q)\tau(q^{-1}) =$ $q ( a ) \tau ( q ^ { -   1 } )$ . Hence $q ( a )$ is invertible and $q ( a ) ^ { - 1 } = \tau ( q ^ { - 1 } )$ . But using the Riesz Functional Calculus, a similar argument shows that $q ( a ) ^ { - 1 } = ( 1 / q ) ( a )$ . Thus $\tau ( q ^ { - 1 } ) = ( 1 / q ) ( a )$ . Therefore if $f = p / q ,$ where p and q are polynomials and $q$ never vanishes on $\sigma ( a ) , \tau ( f ) = \tau ( p \cdot q ^ { - 1 } ) = \tau ( p ) \tau ( q ^ { - 1 } ) = p ( a ) ( 1 / q ) ( a ) = f ( a )$

Now let $f \in \mathrm{HCl}(a)$ and suppose f is analytic on an open set G such that $\sigma ( a ) \subseteq G$ . By Runge's theorem there are rational functions $\{ f _ { n } \}$ in Hol(a) such that $f _ { n } ( z )   \to   f ( z )$ uniformly on compact subsets of G. By (c) of the hypothesis, $\tau ( f _ { n } ) \to \tau ( f )$ . But $\tau ( f _ { n } ) = f _ { n } ( a )$ and $f _ { n } ( a )   \to   f ( a )$ by (4.7e). Hence $\tau ( f )   =   f ( a )$

A fact that has been implicit in the manipulations involving the functional calculus is that $f ( a )$ and $g ( a )$ commute for all f and g in Hol(a). In fact, if τ: Hol $( a )   \to   \mathcal { A }$ is defined by $\tau ( f ) = f ( a )$ , then $f ( a ) g ( a ) = \tau ( f g ) = \tau ( g f ) = g ( a ) f ( a )$ Still more can be said.

## 4.9. Proposition. If a, b∈, ab = ba, and $f \in \mathrm{HCl}(a)$ , then $f ( a ) b = b f ( a )$

PRooF. An algebraic exercise demonstrates that $f(a)b = bf(a) \;  if  \; f$ is a rational function with poles off $\sigma ( a )$ The general result now follows by Runge's Theorem.

## 4.10. The Spectral Mapping Theorem. If a∈ and $f \in \mathrm{HCl}(a).$ , then

$$
\sigma ( f ( a ) ) = f ( \sigma ( a ) ) .
$$

PROOF. If $\alpha   \in   \sigma ( a ) .$ , let $g \in \mathrm{HCl}(a)$ such that $f(z) - f(\alpha) = (z - \alpha)g(z)$ . If it were the case that $f ( \alpha ) \notin \sigma ( f ( a ) ) .$ then $( a - \alpha )$ would be invertible with inverse $g ( a ) [ f ( a ) - f ( \alpha ) ] ^ { - 1 }$ . Hence $f(\alpha) \in \sigma(f(a));$ that $\mathrm{is}, f(\sigma(a)) \in \sigma(f(a))$

Conversely, if $\beta \notin f ( \sigma ( a ) ) ,$ then $g(z) = \left[ f(z) - \beta \right]^{-1} \in \mathrm{Hol}(a)$ and so $g(a)[f(a) - \beta] = 1$ . Thus $\beta { \notin } \sigma ( f ( a ) ) ,$ ; that is, $\sigma ( f ( a ) ) \subseteq f ( \sigma ( a ) )$

This section closes with an application of the functional calculus that is typical.

4.11. Proposition. Suppose a∈ and $\sigma ( a ) = F _ { 1 } \cup F _ { 2 } .$ where $F _ { 1 }$ and $F _ { 2 }$ are disjoint nonempty closed sets. Then there is a nontrivial idempotent e in $\varkappa$ such that

(a) if ba = ab, then $b e = e b ;$

(b) if $a _ { 1 } = a e$ and $a _ { 2 } = a ( 1 - e ) ,$ then $a = a _ { 1 } + a _ { 2 }$ and $a_{1}a_{2}=a_{2}a_{1}=0;$

(c) $\sigma ( a _ { 1 } ) = F _ { 1 } \cup \{ 0 \} , \sigma ( a _ { 2 } ) = F _ { 2 } \cup \{ 0 \} .$

PROOF. Let $G _ { 1 } ,   G _ { 2 }$ be disjoint open subsets of C such that $F _ { j }   \subset   G _ { j } ,   j   =   1 , 2 .$ Let Γ be a positively oriented system of closed curves in $G _ { 1 }$ such that $\boldsymbol { F } _ { 1 } \in \mathrm { i n s }   \Gamma ,   \boldsymbol { F } _ { 2 } \in \mathrm { o u t }   \Gamma$ . If f = the characteristic function of $G_{1}, f \in \mathrm{HCl}(a);$ let $e   =   f ( a )$ Since $f ^ { 2 } = f ,   e ^ { 2 } = e .$ Part (a) follows from (4.9).

Note that $e ( 1 - e ) = 0 = ( 1 - e ) e$ . Hence (b) is immediate. Let $f _ { 1 } ( z ) = z f ( z ) ,$ $f _ { 2 } ( z ) = z ( 1 - f ( z ) )$ . It follows from (4.7a) that $a _ { j } = f _ { j } ( a ) , \; j = 1 , 2$ Hence the Spectral Mapping Theorem implies that $\sigma ( a _ { j } ) = f _ { j } ( \sigma ( a ) ) = F _ { j } \cup \{ 0 \}$ . The proof that e is neither 0 nor 1 is left to the reader.

Part (c) of the preceding proposition has the somewhat unattractive conclusion that $\sigma ( a _ { 1 } ) = F _ { 1 } \cup \{ 0 \}$ . It would be much neater if the conclusion were that $\sigma ( a _ { 1 } )   =   F _ { 1 }$ . This is, in a sense, the case. Since $a _ { 1 } ( 1 - e ) = 0$ and

$1 - e \neq 0 , a _ { 1 }$ cannot be invertible. However, consider the algebra $\mathcal { A } _ { 1 } \equiv \{ b \in \mathcal { A } :$ $a b = b a$ and $b e = e b = b \}$ . It is left to the reader to show that $\mathcal { A } _ { 1 }$ is a Banach algebra and $e$ is the identity for ${ \mathcal { A } } _ { 1 } . \mathrm { ~ I f ~ } a _ { 1 }$ is considered as an element of the algebra $\mathcal { A } _ { 1 }$ , then its spectrum as an element of $\mathcal { A } _ { 1 }$ is $F _ { 1 }$ . This is an illustration of how the spectrum depends on the Banach algebra (the subject of the next section; also see Exercise 9).

## EXERCISES

1. Let ${ \mathcal { A } } = C ( X )$ , X compact (see Example 3.2). If $g { \in } C ( X )$ and $f \in \mathrm{HCl}(g)$ , show that $f ( g ) = f \circ g .$

2. Let a be a nilpotent element of $\varkappa$ For $f , g$ in Hol(a), give a necessary and sufficient condition on f and $g$ that $f ( a ) = g ( a )$

3. Let $d \geqslant 1$ and let $A \in M_{d}(\mathbb{C})$ . Give a necessary and sufficient condition on f in $\operatorname { H o l } ( A )$ such that $f ( A ) = 0 .$ (Hint: Consider the Jordan canonical form for A.)

4. If $\mathcal { A }$ is a Banach algebra with identity, a∈, $f \in \mathrm{HCl}(a),$ and g is analytic in a neighborhood of $f ( \sigma ( a ) )$ , then $g \circ f \in \mathrm{HCl}(a)$ and $g(f(a)) = g^{\circ}f(a)$

5. If $\mathcal { X }$ is a Banach space, $A   \in   \mathcal { B } ( \mathcal { X } ) ,$ and $\mathcal { M } \leqslant \mathcal { X }$ such that $( A - \alpha ) ^ { - 1 } \mathcal { M } \subseteq \mathcal { M }$ for all α in $\rho ( A )$ , show that $f ( A ) \mathcal { M } \subseteq \mathcal { M }$ whenever $f \in \mathrm{HCl}(A)$

6. If $\mathcal { X }$ is a Banach space, $A   \in   \mathcal { B } ( \mathcal { X } )$ , and $f \in \mathrm{HCl}(A)$ , show that $f(A)^{*} = f(A^{*})$ (See (6.1) below.)

7. If  is a Hilbert space, $A   \in   \mathcal { B } ( \mathcal { H } )$ , and $f \in \mathrm{HCl}(A)$ , show that $f ( A ) ^ { * } = { \widetilde { f } } ( A ^ { * } )$ , where $\tilde{f}(z) = \overline{f(\bar{z})} ( See (6.1) below. )$

8. If ª€ is a Hilbert space, A is a normal operator on $\mathcal { H } .$ and $f \in \mathrm{HCl}(A)$ , show that $f ( A )$ is normal.

9. Let X be a Banach space and let $A   \in   \mathcal { B } ( \mathcal { X } )$ . Show that if $\sigma ( A ) = F _ { 1 } \cup F _ { 2 }$ where $F _ { 1 } , F _ { 2 }$ are disjoint closed subsets of C, then there are topologically complementary subspaces $\mathcal { X } _ { 1 } , \mathcal { X } _ { 2 }$ of $\mathcal { X }$ such that (a) $B \mathcal { X } _ { j }   \in   \mathcal { X } _ { j } \; ( j   =   1 , 2 )$ whenever $BA = AB;$ if $A _ { j } = A \left| \mathcal { X } _ { j } , \sigma ( A _ { j } ) = F _ { j } ; \right.$ (c) there is an invertible operator R: $\mathcal { X }   \rightarrow   \mathcal { X } _ { 1 }   \oplus   _ { 1 } \mathcal { X } _ { 2 }$ such that $R A R ^ { - 1 } = A _ { 1 } \oplus A _ { 2 }$

10. Let $A \in M_{d}(\mathbb{C}), \sigma(A) = \{ \alpha_{1}, \ldots, \alpha_{n} \}$ , where $\alpha _ { i } \neq \alpha _ { j }$ for $i \neq j .$ Show that for $1 \leqslant j \leqslant n$ there is a matrix $A _ { j }$ in $M _ { d _ { j } } ( \mathbb { C } )$ such that $\dot { \sigma } ( A _ { j } ) = \{ \alpha _ { j } \}$ and A is similar to ${ \pmb A } _ { 1 } \oplus \cdots \oplus { \pmb A } _ { n }$

11. If  is a Banach algebra, I is an ideal of $\mathcal { A }$ (not necessarily closed), $a   \in   I$ and $f \in \operatorname{HCl}(a)$ such that $f ( 0 ) = 0$ , show that $f ( a )   \in   I .$

## §5. Dependence of the Spectrum on the Algebra

If $\partial \mathbf { D } = \{ z \in \mathbb { C } : | z | = 1 \}$ , let ${ \mathcal { B } } = \operatorname { t h e }$ uniform closure of the polynomials in C(∂ID). (Here “polynomial" means a polynomial in $z . )$ If $\mathcal { A } = C ( \partial \mathbf { D } )$ , then the spectrum of z as an element of $\mathcal { A }$ is ∂D (Example 3.2). That is,

$$
\sigma _ { \mathcal { A } } ( z ) = \partial \mathbb { D } .
$$

Now $z \in \mathcal { B }$ and so it has a spectrum as an element of this algebra; denote this spectrum by $\sigma _ { \mathcal { B } } ( z )$ . There is no reason to believe that $\sigma _ { \mathcal { B } } ( z ) = \sigma _ { \mathcal { A } } ( z )$ . In fact, they are not equal.

5.1. Example. If $\mathcal { B } =$ the closure in C(∂D) of the polynomials in z, then $\sigma _ { \mathcal { A } } ( z ) = \mathrm { c l } \mathbb { D }$

To see this first note that $\| z \| = 1$ , so that $\sigma _ { \mathcal { B } } ( z ) \subseteq \mathrm { c l }   \mathbb { D }$ by Theorem 3.6. If $| \lambda | \leqslant 1$ and $\lambda \neq \sigma _ { \mathcal { A } } ( z ) ,$ ,there is an f in  such that $(z - \lambda)f = 1$ . Note that this implies that $| \lambda | < 1$ . Because $f \in { \mathcal { B } } ,$ there is a sequence of polynomials $\{ p _ { n } \}$ such that $p _ { n }   \rightarrow   f$ uniformly on ∂D. Thus for every $\varepsilon   >   0$ there is a N such that for $m,n \geqslant N, \varepsilon > \|p_n - p_m\|_{\partial \mathbb{D}} \equiv \sup \left\{ |p_n(z) - p_n(z)| : z \in \partial \mathbb{D} \right\}$ . By the Maximum Principle, $\varepsilon > \| p _ { n } - p _ { m } \| _ { \mathrm { c l }   \mathbb { D } }$ for $m , n \geqslant N .$ Thus $g(z) = \lim_{n \to \infty} p_n(z)$ is analytic on D and continuous on cl D; also, $g | \partial \mathbf { D } = f .$ By the same argument, since $p _ { n } ( z ) ( z - \lambda ) \to 1$ uniformly on ∂D, $p _ { n } ( z ) ( z - \lambda ) \to 1$ uniformly on D. Thus $g ( z ) ( z - \lambda ) = 1$ on ID. But $1 = g(\lambda)(\lambda - \lambda) = 0,$ a contradiction. Thus, cl $\mathbf { D } \subseteq \sigma _ { \mathcal { B } } ( z )$

Thus the spectrum not only depends on the element of the algebra, but also on the algebra. Precisely how this dependence occurs is given below, but it can be said that the example above is typical, both in its statement and its proof, of the general situation. To phrase these results it is necessary to introduce the polynomially convex hull of a compact subset of C.

## 5.2. Definition. If A is a set and $f \colon A   \to   \mathbb { C } ,$ , define

$$
\| f \| _ { A } \equiv \sup \{ | f ( z ) | : z \in A \}.
$$

If K is a compact subset of C, define the polynomially convex hull of K to be the set $K ^ { \star }$ given by

$$
K ^ { \star } \equiv \{ z \in \mathbb { C } : | p ( z ) | \leqslant \| p \| _ { K } { \mathrm { ~ f o r ~ e v e r y ~ p o l y n o m i a l ~ } } p \} .
$$

The set K is polynomially convex if $K = K ^ { \star }$

Note that the polynomially convex hull of ∂D is cl D. This is, again, quite typical. If K is any compact set, then $\mathbf { C } \backslash K$ has a countable number of components, only one of which is unbounded. The bounded components are sometimes called the holes of $K ;$ a few pictures should convince the reader of the appropriateness of this terminology.

5.3. Proposition. If K is a compact subset of $\mathbf { C } ,$ then $\mathbf { C } \backslash K ^ { \wedge }$ is the unbounded component of $\mathbf { C } \backslash K$ . Hence K is polynomially convex $i f$ and only if $\mathbf { C } \backslash K$ is connected.

PROOF. Let $\boldsymbol { U } _ { 0 } , \boldsymbol { U } _ { 1 } , \ldots$ .be the components of $\mathbf { C } \backslash K .$ where $U _ { 0 }$ is unbounded. Put $L = \mathbb { C } \backslash U _ { 0 } ;$ hence $L = K \cup \bigcup_{n = 1}^{\infty} U_{n}$ Clearly $K \subseteq K ^ { \star }$ . If $n \geqslant 1$ , then $U _ { n }$ is a bounded open set and a topological argument implies $\partial U _ { n }   \subset   K$ . By the Maximum Principle $U _ { n } \subseteq K ^ { \star }$ . Thus, $L \subseteq K ^ { \star }$

If $\alpha { \in } { \boldsymbol { U } } _ { 0 } ,   ( z - \alpha ) ^ { - 1 }$ is analytic in a neighborhood of L. By (III.8.5), there is a sequence of polynomials $\{ p _ { n } \}$ such that $\| p _ { n } - ( z - \alpha ) ^ { - 1 } \| _ { L } \to 0$ If $q _ { n } = ( z - \alpha ) p _ { n } ,$ then $\| q _ { n } - 1 \| _ { L } \to 0 .$ Thus for large $n , \| q _ { n } - 1 \| _ { L } < 1 / 2$ . Since $K \subset L$ and $| q _ { n } ( \alpha ) - 1 | = 1$ , this implies that α∉ $K ^ { \star }$ . Thus $K ^ { \star } \subseteq L$ ■

## 5.4. Theorem. If A and B are Banach algebras with a common identity such that $\mathcal { B } \subseteq \mathcal { A }$ and $a { \in } { \mathcal { B } }$ , then

(a) $\sigma _ { \mathcal { A } } ( a ) \subseteq \sigma _ { \mathcal { B } } ( a )$ and ∂σ $\mathcal { A } ( a ) \subseteq \partial \sigma _ { \mathcal { A } } ( a )$

(b) $\sigma _ { \mathcal { A } } ( a ) ^ { \star } = \sigma _ { \mathcal { A } } ( a ) ^ { \star }$

(c) If G is a hole of $\sigma _ { \mathcal { A } } ( a ) .$ , then either $G \subseteq \sigma _ { \mathcal { B } } ( a )$ or $G \cap \sigma _ { \mathcal { B } } ( a ) = \square$

(d) If B is the closure in A of all polynomials in a, then $\sigma _ { \mathcal { B } } ( a ) = \sigma _ { \mathcal { A } } ( a ) ^ { \star }$

PROOF. (a) If $\alpha \not \in \sigma _ { \mathcal { B } } ( a ) ,$ , then there is a b in  such that $b(a - \alpha) = (a - \alpha)b = 1$ Since $\mathcal { B } \subseteq \mathcal { A } , \alpha \notin \sigma _ { \mathcal { A } } ( a )$ . Now assume that $\lambda   \in   \partial \sigma _ { \mathcal { B } } ( a )$ Since int $\sigma _ { \mathcal { A } } ( a ) \subseteq \operatorname { i n t } \sigma _ { \mathcal { B } } ( a )$ it suffices to show that $\lambda { \in } \sigma _ { \mathcal { A } } ( a )$ Suppose $\lambda \notin \sigma _ { \mathcal { A } } ( a ) ;$ there is thus an x in such that $x(a - \lambda) = (a - \lambda)x = 1$ . Since $\lambda { \in } \partial \sigma _ { \mathcal { B } } ( a )$ , there is a sequence $\{ \lambda _ { n } \}$ in $\mathbb { C } \backslash \sigma _ { \mathcal { B } } ( a )$ such that $\lambda _ { n } \to \lambda$ Let $( a - \lambda _ { n } ) ^ { - 1 }$ be the inverse of $( a - \lambda _ { n } )$ in B; so $( a - \lambda _ { n } ) ^ { - 1 } \in \mathcal { A }$ .Since $\lambda _ { n } \rightarrow \lambda , ( a - \lambda _ { n } ) \rightarrow ( a - \lambda )$ . By Theorem $2.2,(a-\lambda_{n})^{-1}\to x$ Thus $x   \in   \mathcal { B }$ since  is complete. This contradicts the fact that $\lambda   \in   \sigma _ { \mathcal { B } } ( a )$

(b) This is a consequence of (a) and the Maximum Principle.

(c) Let G be a hole of $\sigma _ { \mathcal { A } } ( a )$ and put $G _ { 1 } = G \cap \sigma _ { \mathcal { B } } ( a )$ and $G _ { 2 } = G \backslash \sigma _ { \mathcal { B } } ( a )$ So $G   =   G _ { 1 }   \cup   G _ { 2 }$ and $G _ { 1 }   \cap   G _ { 2 }   =   \square$ . Clearly $G _ { 2 }$ is open. On the other hand, the fact that $\partial \sigma _ { \mathcal { A } } ( a ) \subseteq \sigma _ { \mathcal { A } } ( a )$ and $G \cap \sigma _ { \mathcal { A } } ( a ) = \square$ implies that $G _ { 1 } = G \cap \mathrm { i n t } \sigma _ { \mathcal { B } } ( a )$ so $G _ { 1 }$ is open. Because G is connected, either $G _ { 1 }$ or $G _ { 2 }$ is empty.

(d) Let  be as in (d). From (a) and (b) it is known that $\sigma _ { \mathcal { A } } ( a ) \subseteq \sigma _ { \mathcal { B } } ( a ) \subseteq \sigma _ { \mathcal { A } } ( a ) ^ { \prime }$ . Fix λ in $\sigma _ { \mathcal { A } } ( a ) ^ { \prime }$ . If $\lambda \notin \sigma _ { \mathcal { B } } ( a ) , ( a - \lambda ) ^ { - 1 } \in \mathcal { B } \subseteq \mathcal { A }$ Hence there is a sequence of polynomials $\{ p _ { n } \}$ such that $\rho _ { n } ( a ) \to ( a - \lambda ) ^ { - 1 }$ . Let $q_{n}(z) = (z - \lambda)p_{n}(z)$ . Thus $\| q _ { n } ( a ) - 1 \| \to 0$ . By the Spectral Mapping Theorem, $\sigma _ { \mathcal { A } } ( q _ { n } ( a ) ) = q _ { n } ( \sigma _ { \mathcal { A } } ( a ) )$ . Thus, because $\lambda { \in } \sigma _ { \mathcal { A } } ( a ) ^ { \wedge }$

$$
\begin{align*}\| q_n(a) - 1 \| & \geqslant r(q_n(a) - 1) \\& = \sup \left\{ |z - 1| \colon z { \in } \sigma_{\mathcal{A}}(q_n(a)) \right\} \\& = \sup \left\{ |q_n(w) - 1| \colon w { \in } \sigma_{\mathcal{A}}(a) \right\} \\& \geqslant |q_n(\lambda) - 1| \\& = 1.\end{align*}
$$

This is a contradiction.

EXERCISES

1. If K is a compact subset of C, let P(K) be the closure of the polynomials in C(K). Show that the identity map on polynomials extends to an isometric isomorphism of $P ( K )$ onto $P ( K ^ { \prec } )$ 1

2. If K is a compact subset of C, let $R ( K )$ be the closure in $C ( K )$ of all rational functions with poles off K. If $f   \in   R ( K )$ , show that $\sigma_{R(K)}(f) = f(K). \mathrm{If} f \in P(K)$ , show that $\sigma _ { { } _ { P ( K ) } } ( f ) = \hat { f } ( K ^ { \star } )$ , where $\hat { f }$ is a natural extension of f to $K ^ { \star }$

3. Let $\mathcal { A } , \mathcal { B }$ be as in Theorem 5.4. If $a { \in } { \mathcal { B } }$ and $\sigma _ { \mathcal { A } } ( a ) \subseteq \mathbb { R }$ , show that $\sigma _ { \mathcal { A } } ( a ) = \sigma _ { \mathcal { A } } ( a ) .$

4. Let $\varkappa$ be a Banach algebra with identity and let $a \in \mathcal { A }$ If $G _ { 1 } , G _ { 2 } , \ldots$ are the holes of $\sigma _ { \mathcal { A } } ( a )$ and $1 \leqslant n_{1} \leqslant n_{2}, \ldots,$ show that there is a subalgebra $\pmb { \mathscr { B } }$ of $\nsim$ such that $a { \in } { \mathcal { B } }$ and $\sigma_{\mathcal{A}}(a) = \sigma_{\mathcal{A}}(a) \cup \bigcup_{k = 1}^{\infty} G_{n_k}$

5. If $\mathcal { A } , \mathcal { B } ,$ and a are as in Theorem $5 . 4 , \mathcal { A }$ is not abelian, and $\mathcal { B }$ is a maximal abelian subalgebra of $\alpha ,$ show that $\sigma _ { \mathcal { A } } ( a ) = \sigma _ { \mathcal { B } } ( a )$

6. If K is a nonempty compact subset of C that is polynomially convex, show that the components of int K are simply connected.

## §6. The Spectrum of a Linear Operator

The proof of the first result is left as an exercise.

## 6.1. Proposition.

(a) If X is a Banach space and $A \in \mathcal{B}(\mathcal{X}), \sigma(A^*) = \sigma(A)$

(b) If H is a Hilbert space and $A \in \mathcal{B}(\mathcal{H}), \sigma(A^*) = \sigma(A)^*$ , where for any subset $\Delta { \it o f } \mathbb { C } ,   \Delta ^ { * } \equiv \{ \bar { z } { : } z { \in } \Delta \}$

In this section only results about operators on Banach spaces will be given. For the corresponding results about operators on a Hilbert space involving the adjoint, the reader is asked to supply the details. The preceding proposition should be kept in mind as a model of the probable differences.

In this section and the next $\mathcal { X }$ always denotes a Banach space over $\mathbf { C }$

6.2. Definition. If $A   \in   \mathcal { B } ( \mathcal { X } )$ , the point spectrum of $A , \sigma _ { p } ( A )$ , is defined by

$$
\sigma _ { p } ( A ) \equiv \{ \lambda \in \mathbb { C } : \ker ( A - \lambda ) \neq ( 0 ) \} .
$$

As in the case of operators on a Hilbert space, elements of $\sigma _ { p } ( A )$ are called eigenvalues. If $\lambda   \in   \sigma _ { p } ( A )$ , non-zero vectors in $\ker ( A - \lambda )$ are called eigenvectors; ker $( A - \lambda )$ is called the eigenspace of A at λ.

6.3. Definition. If $A   \in   { \mathcal { B } } ( { \mathcal { X } } ) .$ , the approximate point spectrum of $A , \sigma _ { a p } ( A )$ is defined by

$$
\sigma _ { a p } ( A ) \equiv \{ \lambda \in \mathbb { C } : \mathrm { t h e r e ~ i s ~ a ~ s e q u e n c e } \{ x _ { n } \} \mathrm { ~ i n ~ } \mathcal { X }
$$

$$
\mathrm { s u c h } \mathrm { t h a t } \left\| x _ { n } \right\| = 1 \mathrm { f o r } \mathrm { a l l } n \mathrm { a n d } \left\| ( A - \lambda ) x _ { n } \right\| \rightarrow 0 \}.
$$

Note that $\sigma _ { p } ( A ) \subseteq \sigma _ { a p } ( A ) .$

6.4. Proposition. If $A   \in   \mathcal { B } ( \mathcal { X } )$ and $\lambda \in \mathbf { C } ,$ , the following statements are equivalent.

(a) λ∉ $\sigma _ { a p } ( A )$

(b) $\ker(A - \lambda) = (0)$ and $\operatorname { r a n } ( A - \lambda )$ is closed.

(c) There is a constant $c   >   0$ such that $\| ( A - \lambda ) x \| \geqslant c \| x \|$ for all x.

ProoF. Clearly it may be assumed that $\lambda   =   0 .$

(a)⇒(c): Suppose (c) fails to hold; then for every n there is a non-zero vector $x _ { n }$ with $\| A x _ { \mathfrak { n } } \| \leqslant \| x _ { \mathfrak { n } } \| / \mathfrak { n }$ . If $y _ { n } = x _ { n } / \| x _ { n } \| , \| y _ { n } \| = 1$ and $\| A y _ { n } \| \to 0 .$ Hence $0   \in   \sigma _ { a p } ( A )$

(c)⇒(b): Suppose $\| A x \| \geqslant c \| x \|$ . Clearly ker $A   =   ( 0 )$ . If $Ax_{n} \rightarrow y,\left\| x_{n} - x_{m} \right\| \leq$ $c ^ { - 1 } \left\| A x _ { n } - A x _ { m } \right\|$ , SO $\{ x _ { n } \}$ is a Cauchy sequence. Let $x = \lim_{n \to \infty} x_n;$ therefore $A x = y$ and ran A is closed.

(b)⇒(a): Let ${ \mathcal { B } } = \operatorname { r a n } A ;$ sO $A \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a continuous bijection. By the Inverse Mapping Theorem, there is a bounded operator $B \colon { \mathcal { G } }   \to   { \mathcal { X } }$ such that $B A x = x$ for all x in $\mathcal { X }$ . Thus if $\|x\| = 1, \; 1 = \|BAx\| \leqslant \|B\| \|Ax\|$ . That is, $\| A x \| \geqslant \| B \| ^ { - 1 }$ whenever $\| x \| = 1$ . Hence $0 { \notin } \sigma _ { a p } ( A )$ ■

It may be that $\sigma _ { p } ( A )$ is empty, but it will be shown that $\sigma _ { a p } ( A )$ is never empty. The first statement follows from the next result (or from other examples that have been presented); the second statement will be proved later.

6.5. Proposition. $If   1 \leq p \leq \infty$ , define $S \colon l ^ { p }   \to   l ^ { p }$ by $S(x_{1},x_{2},\ldots)=(0,x_{1},x_{2},\ldots)$ Then σ(S) = cl D, $\sigma _ { p } ( S ) = \square$ , and $\sigma _ { a p } ( S ) = \partial \mathbf { D }$ . Moreover, $\mathit { f o r \quad } | \lambda | < 1$ ran $( S - \lambda )$ is closed and dim $\left[ l ^ { p } / \mathrm { r a n } ( S - \dot { \lambda } ) \right] = 1$

PROOF. Let $S _ { p }$ be the shift on lP. For $1 \leqslant p \leqslant \infty$ , define $T _ { p } \colon l ^ { p }   \to   l ^ { p }$ by $T _ { p } ( x _ { 1 } , x _ { 2 } , \ldots ) = ( x _ { 2 } , x _ { 3 } , \ldots )$ . It is easy to check that for $1 \leqslant p < \infty$ and $1 / p + 1 / q = 1 , S _ { p } ^ { * } = T _ { q }$ . Since $\| S _ { p } \| = 1 , \sigma ( S _ { p } ) \in \mathbb { C }$ D.

Suppose $x = (x_1, x_2, \ldots) \in l^p, \quad \lambda \neq 0.$ If $S _ { p } x = \lambda x , \quad 0 = \lambda x _ { 1 } , \quad x _ { 1 } = \lambda x _ { 2 } , \ldots .$ Hence $0 = x _ { 1 } = x _ { 2 } = \cdots .$ Since $S _ { p }$ is an isometry, ker $S _ { p }   =   ( 0 )$ . Thus $\sigma _ { p } ( S _ { p } ) = \Box$

Let $1 \leqslant p \leqslant \infty$ and $| \lambda | < 1$ Put $x _ { \lambda } = ( 1 , \lambda , \lambda ^ { 2 } , \ldots )$ Then $\| x _ { \lambda } \| _ { p } ^ { p } =$ $\begin{array} { r } { \sum _ { n = 0 } ^ { \infty } | \lambda ^ { p } | ^ { n } < \infty } \end{array}$ Also, $T _ { p } x _ { \lambda } = ( \lambda , \lambda ^ { 2 } , \ldots ) = \lambda x _ { \lambda }$ Hence $\lambda { \in } \sigma _ { p } ( T _ { p } )$ and $x _ { \lambda } \in \ker ( T _ { p } - \lambda )$ . If $1 \leqslant p < \infty$ and $1 / p + 1 / q = 1$ $T _ { q } = S _ { p } ^ { * } ;$ SO $\mathbf{D} \in \sigma(T_q) = \sigma(S_p)$ Also, $\dot { S _ { \infty } } = T _ { 1 } ^ { * }$ , so $\mathbf { D } \subseteq \sigma ( S _ { \infty } )$ . Thus for all p, $\vec { \mathbf { D } } \subseteq \sigma ( S _ { p } ) \subseteq \mathbf { c l }$ D. Since $\sigma ( \bar { S } _ { p } )$ is necessarily closed, $\sigma ( S _ { p } ) =$ cl D.

$\mathrm { I f } \left| \lambda \right| \neq 1$ and $x \in l ^ { p } , \left\| \left( S _ { p } - \lambda \right) x \right\| _ { p } = \left\| S _ { p } x - \lambda x \right\| _ { p } \geqslant \left| \left\| S _ { p } x \right\| _ { p } - \left| \lambda \right| \left\| x \right\| _ { p } \right| =$ $\left| \left\| x \right\|_p - \left| \lambda \right| \left\| x \right\|_p \right| = \left| 1 - \left| \dot{\lambda} \right| \right| \left\| x \right\|_p . \mathrm{By} (6.4), \lambda \notin \sigma_{ap}^{'}(S_p)$ Hence $\sigma _ { a p } ( S ) \subseteq \partial \mathbb { D } .$ The fact that $\dot { \sigma _ { a p } } ( S _ { p } ) = \partial \mathbf { D }$ follows from the next proposition (6.7).

Fix $| \lambda | < 1 ;$ ; we will show that dim ker $( T _ { p } - \lambda ) = 1$ for $1 \leqslant p \leqslant \infty$ . Indeed, if $x   \in   ^ { l ^ { p } }$ and $T _ { p } x = \lambda x$ , then $(x_{2},x_{3},\ldots)=(\lambda x_{1},\lambda x_{2},\ldots)$ So $x _ { n + 1 } = \lambda x _ { n }$ for all n. Thus $x _ { n + 1 } = \lambda ^ { n } x _ { 1 }$ for $n \geqslant 1$ . That is, if $x _ { \lambda } = ( 1 , \lambda , \lambda ^ { 2 } , \ldots )$ , then $x = x _ { 1 } x _ { \lambda }$ Since it has already been shown that $x _ { \lambda } \in \ker ( T _ { p } - \lambda )$ , we have that the dimension of this kernel is 1. Therefore, if $1 \leqslant p < \infty, \; 1 = \dim$ ker $( T _ { q } - \lambda ) =$ dim ker $\left( S _ { p } ^ { * } - \lambda \right) = \dim \left[ \operatorname { r a n } \left( S _ { p } - \lambda \right) ^ { \perp } \right] \left( \operatorname { V I } . 1 . 8 \right) = \dim \left[ l ^ { p } / \operatorname { r a n } \left( S _ { p } - \lambda \right) \right] ^ { * } \left( \operatorname { W h y } ? \right)$ But this implies that dim $\left[ l ^ { \dot { p } } / \mathrm { r a n } ( S _ { p } - \lambda ) \right] = 1$ , completing the proof for the case where $p$ is finite. The proof for $p   =   \infty$ is similar and is left to the reader.■

6.6. Corollary. $If   1 \leqslant p \leqslant \infty$ and $T \colon l ^ { p } { \to } l ^ { p }$ is defined by $T ( x _ { 1 } , x _ { 2 } , \ldots ) = ( x _ { 2 } , x _ { 3 } , \ldots ) ,$