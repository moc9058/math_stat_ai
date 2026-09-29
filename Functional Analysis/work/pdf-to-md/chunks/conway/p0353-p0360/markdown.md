Using integration by parts,

$$
\begin{align*}\left( D \phi \right) \hat{\mathbf{\Phi}}(y) = & \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-i y t} \phi^{\prime}(t) dt \\= & \frac{-1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} \phi(t) \frac{d}{dt} [e^{-i y t}] dt \\= & \frac{i y}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-i y t} \phi(t) dt.\end{align*}
$$

That is, $( D \phi ) ^ { \wedge } = ( i x ) \hat { \phi } .$ By induction,

6.10

$$
( D ^ { n } \phi ) ^ { \wedge } = ( i x ) ^ { n } \hat { \phi }
$$

for all $n   \geqslant   0 .$ Combining (6.9) and (6.10) gives (6.8)

By (6.8) if $m , n \geqslant 0 ,$ then for $\phi$ in $\mathcal { L } ,$

$$
\begin{align*}\|\hat{\phi}\|_{m,n} = & \sup\{|x^m(D^n\hat{\phi})(x)|:x\in\mathbb{R}\} \\= & \sup\left\{\left|\frac{1}{\sqrt{2\pi}}\right|_{-\infty}^{\infty}e^{-ixt}\left(\frac{d}{dt}\right)^m[(-it)^n\phi(t)]dt\right|:x\in\mathbb{R}\} \\\leqslant & \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\left|\left(\frac{d}{dt}\right)^m[t^n\phi(t)]\right|dt \\< & \infty.\end{align*}
$$

since $D ^ { m } ( x ^ { n } \phi ) \in L ^ { 1 } ( \mathbb { R } )$ (6.5).

(c) This is an easy exercise in integration theory and is left to the reader.

The fact that $\hat { f } ( x ) \to 0 \mathrm { a s } | x | \to \infty$ is called the Riemann-Lebesgue Lemma.

The process now begins whereby it will be shown that the Fourier transform on $L ^ { 1 } \cap L ^ { 2 }$ extends to a unitary operator on $L ^ { 2 } ( \mathbb { R } )$ . Moreover, the adjoint of this unitary will be calculated and it will be shown that if $i d / d x$ is conjugated by this unitary, then the resulting self-adjoint operator is $M _ { x }$

Changing notation a little, let $U _ { y }$ [instead of $U ( y ) ]$ denote the translation operator. Moreover, think of $U _ { y }$ as operating on all of the $L ^ { p }$ spaces, not just $L ^ { 2 } ,$ so $( U _ { y } f ) ( x ) = f ( x - y )$ for $f$ in $L ^ { p } ( \mathbb { R } )$ . Also, let $e _ { y }$ be the function $e _ { y } ( x ) = \exp ( i x y ) .$

6.11. Proposition. $If \in L^{1}(\mathbb{R})$ and $y { \in } \mathbb { R } ,$ then

$$
\begin{array} { r } { [ U _ { y } f ] ^ { \wedge } = e _ { - y } \hat { f } , } \\ { [ e _ { y } f ] ^ { \wedge } = U _ { y } \hat { f } . } \end{array}
$$

PROOF. If $f { \in } L ^ { 1 } ( \mathbb { R } )$

$$
\begin{aligned} \left[ U_{y} f \right]^{\prime}(x) &= (2\pi)^{-1/2} \int \left[ U_{y} f \right](t) e^{-ixt}   dt \\&= (2\pi)^{-1/2} \int f(t-y) e^{-ixt}   dt \\&= (2\pi)^{-1/2} \int f(s) e^{-ix(s+y)}   ds \\&= e_{-y}(x) \hat{f}(x).\\ \end{aligned}
$$

The proof of the other equation is left as an exercise.

In the proof of the next lemma the fact that $\int _ { - \infty } ^ { \infty } e ^ { - t ^ { 2 } } d t = \sqrt { \pi }$ is needed. Those who have never seen this can verify it by putting $I = \int_{0}^{\infty} e^{-x^2}   dx.$ , noting that $I ^ { 2 } = \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } e ^ { - \left( x ^ { 2 } + y ^ { 2 } \right) } d x d y ,$ ,and using polar coordinates.

6.12. Lemma. $\mathit { I f } \varepsilon   >   0$ and $\rho _ { \varepsilon } ( t ) = e ^ { - \varepsilon ^ { 2 } t ^ { 2 } }$ , then

$$
\hat { \rho } _ { \varepsilon } ( x ) = \frac { 1 } { \varepsilon \sqrt { 2 } } e ^ { - x ^ { 2 } / 4 \varepsilon ^ { 2 } } .
$$

PROOF. Note that $\rho _ { \varepsilon } \in \mathcal { S }$ .By (6.8), $D \hat { \rho } _ { \varepsilon } = ( - i x \rho _ { \varepsilon } ) ^ { \prime }$ . Using integration by parts,

$$
\begin{align*}(D\hat{\rho}_{\varepsilon})(x) = & \frac{-i}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\varepsilon^2 t^2} te^{-\it{ixt}}   dt \\= & \frac{-i}{\sqrt{2\pi}} \left( \frac{-1}{2\varepsilon^2} \right) \int_{-\infty}^{\infty} e^{-\it{ixt}}   d(e^{-\varepsilon^2 t^2}) \\= & \frac{-i}{2\varepsilon^2 \sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\varepsilon^2 t^2} (-ix)e^{-\it{ixt}}   dt \\= & \frac{-x}{2\varepsilon^2} \hat{\rho}_{\varepsilon}(x).\end{align*}
$$

Let $\psi _ { \varepsilon } ( x ) = e ^ { - x ^ { 2 } / 4 \varepsilon ^ { 2 } }$ . Then both $\hat { \rho } _ { \varepsilon }$ and $\psi _ { \varepsilon }$ satisfy the differential equation $u ^ { \prime } ( x ) = - ( x / 2 \varepsilon ^ { 2 } ) u ( x )$ . Hence $\hat { \rho } _ { \varepsilon }   =   c \psi _ { \varepsilon }$ for some constant c. But $\psi _ { \varepsilon } ( 0 ) = 1$ , and

$$
\begin{aligned}\hat{\rho}_{\varepsilon}(0) = & \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{-\varepsilon^2 t^2}   dt \\= & \frac{1}{\varepsilon\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{-s^2}   ds \\= & \frac{1}{\varepsilon\sqrt{2\pi}}\sqrt{\pi} = \frac{1}{\varepsilon\sqrt{2}}.\end{aligned}
$$

6.13. Proposition. If $\psi   \in   L ^ { 1 } ( \mathbb { R } )$ such that $(2\pi)^{-1/2} \int_{\mathbb{R}} \psi(x)   dx = 1$ and if for $\varepsilon > 0 , \psi _ { \varepsilon } ( x ) = \varepsilon ^ { - 1 } \psi ( x / \varepsilon )$ , then for every f in $C _ { 0 } ( \mathbb { R } ) , \psi _ { \varepsilon } * f ( x ) \to f ( x )$ uniformly on R.

PROOF. Note that $( 2 \pi ) ^ { - 1 / 2 } \int \psi _ { \varepsilon } ( x )   d x = 1$ for all $\varepsilon   >   0 .$ Hence for any x in $\mathbb { R }$

$$
\begin{align*}\psi_{\varepsilon} * f(x) - f(x) = & \left( 2 \pi \right)^{-1/2} \int \left[ f(x-t) - f(x) \right] \frac{1}{\varepsilon} \psi \left( \frac{t}{\varepsilon} \right) dt \\= & \left( 2 \pi \right)^{-1/2} \int \left[ f(x-s \varepsilon) - f(x) \right] \psi(s)   ds.\end{align*}
$$

Put $\omega(y)=\sup\left\{\left|f(x-y)-f(x)\right|:y\in\mathbb{R}\right\}$ . Now f is uniformly continuous $( \mathbf { W h y } ? ) ,$ so if $\varepsilon   >   0 ,$ , then there is a $\delta   >   0$ such that $\omega ( y ) < \varepsilon \mathrm { i f } | y | < \delta$ . Thus $\omega ( y ) \to 0 \mathrm { a s } | y | \to 0$ . Moreover, the inequality above implies

$$
\| \psi _ { \varepsilon } * f - f \| _ { \infty } \leqslant ( 2 \pi ) ^ { - 1 / 2 } \int \omega ( s \varepsilon ) | \psi ( s ) |   d s .
$$

Since $\psi   \in   L ^ { 1 } ( \mathbb { R } )$ , the Lebesgue Dominated Convergence Theorem implies that $\lVert \psi _ { \varepsilon _ { k } } * f - f \rVert _ { \infty }   \to   0$ whenever $\varepsilon _ { k }   \to   0$ .This proves the proposition.

The next result is often called the Multiplication Formula. Remember that if $f \in L ^ { 1 } ( \mathbb { R } ) , \hat { f } \in C _ { 0 } ( \mathbb { R } )$ . Hence $\hat { f } \underset {} { g } { \in } L ^ { 1 } ( \mathbb { R } )$ when both f and $g   \in   L ^ { 1 } ( \mathbb { R } )$ .

## 6.14. Theorem. If f, $g { \in } L ^ { 1 } ( \mathbb { R } ) ,$ then

$$
\int _ { \mathbb { R } } \hat { f } ( x ) g ( x )   d x = \int _ { \mathbb { R } } f ( x ) \hat { g } ( x )   d x .
$$

ProoF. The proof is an easy consequence of Fubini's Theorem. In fact, if $f , g { \in } L ^ { 1 } ( \mathbb { R } ) ,$ then

$$
\begin{aligned}\int \hat{f}(x) g(x)   dx &= \int \left[ \frac{1}{\sqrt{2\pi}} \int f(t) e^{-i x t}   dt \right] g(x)   dx \\&= \int f(t) \left[ \frac{1}{\sqrt{2\pi}} \int g(x) e^{-i x t}   dx \right] dt \\&= \int f(t) \hat{g}(t)   dt.\end{aligned}
$$

## 6.15. Inversion Formula. If $\phi \in \mathcal { P } ,$ then

$$
\phi ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } { \hat { \phi } } ( t ) e ^ { i x t }   d t .
$$

PROOF. Let $\rho _ { \varepsilon } ( x ) = e ^ { - \varepsilon ^ { 2 } x ^ { 2 } }$ and put $\psi ( x ) = \hat { \rho } _ { 1 } ( x )$ Then by Lemma 6.12

$\psi _ { \varepsilon } ( x ) = \varepsilon ^ { - 1 } \psi ( x / \varepsilon ) = \hat { \rho } _ { \varepsilon } ( x ) .$ Also,

$$
(2\pi)^{-1/2}\int \psi(x)dx = (2\pi)^{-1/2}\int_{-\infty}^{\infty} 2^{-1/2}e^{-x^2/4}dx = 1.
$$

So $\psi _ { \varepsilon }   *   h ( x )   \to   h ( x )$ uniformly for any $h$ in $C _ { 0 } ( \mathbb { R } )$ If $\phi \in \mathcal { S } _ { 1 }$ put $f = \phi$ and $g = e _ { x } \rho _ { \varepsilon }$ in (6.14). By Proposition 6.11 and Lemma 6.12, $\hat { g } = \boldsymbol { U } _ { x } \hat { \boldsymbol { \rho } } _ { \varepsilon } = \boldsymbol { U } _ { x } \boldsymbol { \psi } _ { \varepsilon } .$ Thus

$$
\begin{aligned}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \hat{\phi}(t)e^{itx}e^{-\varepsilon^2 t^2}dt &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(t)\psi_{\varepsilon}(t-x)dt \\&= \phi * \psi_{\varepsilon}(x) \\&\rightarrow \phi(x)\end{aligned}
$$

as $\varepsilon   \rightarrow   0 ,$ The Lebesgue Dominated Convergence Theorem implies the left-hand side converges to $( 2 \pi ) ^ { - 1 / 2 } \int \hat { \phi } ( t ) e ^ { i x t } d t$ and the theorem is proved.

In many ways the next result is a rephrasing of the preceding theorem.

6.16. Theorem. If ${ \mathcal { F } } \colon { \mathcal { P } }   \to   { \mathcal { P } }$ is defined by $\mathcal { F } \phi = \hat { \phi } , \mathcal { F }$ is a bijection with

$$
( \mathcal { F } ^ { - 1 } \phi ) ( x ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \phi ( t ) e ^ { i x t } d t.
$$

Moreover, $\mathcal { Y } \mathcal { S }$ is given the topology induced by the seminorms $\left\{ \left\| \cdot \right\|_{m,n} : m,n \geqslant 0 \right\}$ that were defined in $( 6 . 4 ) ,   \mathcal { F }$ is a homeomorphism.

PROOF. By (6.7b), ${ \mathcal { F } } { \mathcal { P } } \subseteq { \mathcal { P } }$ The preceding theorem says that $\mathcal { F }$ is bijective and gives the formula for $\mathcal { F } ^ { - 1 }$ . The proof of the topological statement is left to the reader. ■

6.17. Plancherel's Theorem. If $\phi \in \mathcal { S }$ , then $\|   \phi   \| _ { 2 } = \|   \hat { \phi }   \| _ { 2 }$ and the Fourier transform $\mathcal { F }$ extends to a unitary operator on $L ^ { 2 } ( \mathbb { R } )$

PROOF. Let $\phi \in \mathcal { S }$ and put $\psi ( x ) = \phi ( - x ) .$ So $\rho = \phi   *   \psi   \in   L ^ { 1 } ( \mathbb { R } )$ and $\hat { \rho } = \hat { \phi } \hat { \psi } .$

An easy calculation shows that $\hat { \psi } = \bar { \hat { \phi } } ;$ hence $\hat { \rho } = | \hat { \phi } | ^ { 2 } . \mathrm { A l s o } ,$ the Inversion Formula shows that $\rho ( 0 ) = ( 2 \pi ) ^ { - 1 / 2 } \int \hat { \rho } ( x ) d x = ( 2 \pi ) ^ { - 1 / 2 } \int | \hat { \phi } ( x ) | ^ { 2 } d x$ Thus

$$
\begin{aligned}\int |\hat{\phi}(x)|^2   dx &= (2\pi)^{1/2} \rho(0) \\&= (2\pi)^{1/2} \phi * \psi(0) \\&= \int \phi(x) \psi(0-x)   dx \\&= \int |\phi(x)|^2   dx.\end{aligned}
$$

So if $\mathcal { S }$ is considered as a subspace of $L ^ { 2 } ( \mathbb { R } ) , \mathcal { F }$ , the Fourier transform, is an isometry on $\mathcal { S }$ . By Proposition 6.5 and the preceding theorem, $\mathcal { F }$ extends to a unitary operator on $L ^ { 2 } ( \mathbb { R } )$

Warning! The content of the Plancherel Theorem is that the Fourier transform extends to an isometry. The formula for this isometry is not given by the formula for the Fourier transform. Indeed, this formula does not make sense when $f$ is not an $L ^ { 1 }$ function. However, the same symbol, $\mathcal { F }$ , will be used to denote this unitary operator on $L ^ { 2 } ( \mathbb { R } )$ . For emphasis it is called the Plancherel transform.

6.18. Theorem. Let A be the operator on $L ^ { 2 } ( \mathbb { R } )$ given by $A f = i f ^ { \prime }$ and let M be the operator defined by $M f = x f .$ If $\mathcal { F } : L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ is the Plancherel Transform, then $\mathcal { F }$ dom M = dom A and

$$
\mathcal{F}^{-1} A \mathcal{F} = M.
$$

PROOF. The fact that $A \mathcal { F } = \mathcal { F } M$ on $\mathcal { S }$ is an immediate consequence of Theorem $6 . 7 ( b )$ . Since $\mathcal { S }$ is dense in both dom A and dom M, the rest of the result follows (with some work—give the details).

Fourier analysis is a subject unto itself. One source is Stein and Weiss $[ 1 9 7 1 ] ;$ another is Reed and Simon [1975].

## EXERCISES

1. If  is as in Example 6.1, show that for every $f$ in $\mathcal { D }$ there is a sequence $\{ f _ { n } \}$ in $C _ { c } ^ { ( 1 ) } ( \mathbb { R } )$ such that $f _ { n }   \rightarrow   f$ and $f _ { n } ^ { \prime }   \rightarrow   f ^ { \prime }$ in $L ^ { 2 } ( \mathbb { R } )$

2. Show that the Schwartz space $\mathcal { S }$ with the seminorms $\left\{ \left\| \cdot \right\| _ { m , n } : m , n \geqslant 0 \right\}$ is a Fréchet space.

3. If $\phi$ is infinitely differentiable on R, show that $\phi \in \mathcal { S }$ if and only if for every integer $n   \geqslant   0$ and every polynomial $p , \phi ^ { ( n ) } ( x ) p ( x ) \to 0 \mathrm { a s } | x | \to \infty$

4. If $f \in L^{p}(\mathbb{R}), 1 \leqslant p \leqslant \infty$ , and $g { \in } L ^ { 1 } ( \mathbb { R } )$ , show that $f * g \in L ^ { p } ( \mathbb { R } )$ and $\| f \ast g \| _ { p } \leqslant \| f \| _ { p } \| g \| _ { 1 }$ (Hint: See Dunford and Schwartz [1958], p. 530, Exercise 13 for a generalization of Minkowski's Inequality.)

5. If $\psi$ and $\psi _ { \varepsilon }$ are as Proposition 6.13 and $f   \in   L ^ { p } ( \mathbb { R } )$ $1 \leqslant p < \infty$ , show that $f \cdot \psi _ { \varepsilon } - f \parallel _ { p } \to 0$ as $\varepsilon   \to   0$ If $f { \in } L ^ { \infty } ( \mathbb { R } )$ , show that $f * \psi _ { \varepsilon } \to f ( \mathrm { w e a k } ^ { * } )$

6. If $f { \in } L ^ { 1 } ( \mathbb { R } )$ and $\hat { f }   \in   L ^ { 1 } ( \mathbb { R } )$ , show that $f(x) = (2\pi)^{-1/2} \int_{\mathbb{R}} \hat{f}(t) e^{ixt}$ dt a.e.

7. If $\mathcal { F } : L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ is the Plancherel Transform and $f   \in   L ^ { 2 } ( \mathbb { R } ) ,$ show that $( \mathcal { F } ^ { - 1 } f ) ( x ) = ( \mathcal { F } f ) ( - x )$

8. Show that $\mathcal { F } ^ { 4 } = 1$ but $\mathcal { F } ^ { 2 } \neq 1$ . What does this say about $\sigma ( \mathcal { F } ) ?$

9. Find the Fourier transform of the Hermite polynomials. What do you think? (This exercise is broken up into a series of easier steps on pages 98–99 of Dym and McKean [1972].)

## §7. Moments

To understand this section, the preceding two sections are unnecessary.

Let $\mu$ be a positive Borel measure on R such that $\int | t | ^ { n }   d \mu ( t ) = m _ { n } < \infty$ for every $n \geqslant 0 .$ The numbers $\{ m _ { n } \}$ are called the moments of $\mu$ in analogy with the corresponding concept from mechanics. The central problem here, called the Hamburger moment problem, is to characterize those sequences of numbers that are moment sequences. Just as self-adjoint operators are connected to measures, the theory of self-adjoint operators is connected to the solution of this moment problem.

7.1. Theorem. If $\left\{ m _ { n } : n \geqslant 0 \right\}$ is a sequence of real numbers, the following statements are equivalent.

(a) There is a positive regular Borel measure $\mu$ on R such that $\int | t | ^ { n }   d \mu ( t ) < \infty$ for all $n   \geqslant   0$ and $m_{n} = \int t^{n}   d\mu(t)$

(b) If $\alpha _ { 0 } , \ldots , \alpha _ { n } { \in } \mathbb { C } ,$ then $\begin{array} { r } { \sum _ { j , k = 0 } ^ { n } m _ { j + k } \alpha _ { j } \bar { \alpha } _ { k } \geqslant 0 . } \end{array}$ (c) There is a self-adjoint operator A and a vector e such that e∈dom $A ^ { n }$ for all n and $m _ { n } = \langle A ^ { n } e , e \rangle$ for all $n   \geqslant   0$

Before proving this theorem, a preliminary result is needed. This result is useful in many other situations and is one of the standard ways to show that a symmetric operator has a self-adjoint extension.

7.2. Proposition. Let T be a symmetric operator on $\mathcal { H }$ and suppose there is a function $J : \mathcal { H } \rightarrow \mathcal { H }$ having the following properties:

(a) J is conjugate linear (that $i s ,   J ( h + g ) = J h + J g { \mathrm { ~ a n d ~ } } J ( \alpha h ) = \bar { \alpha } J h ;$

(b) $J ^ { 2 } = 1$

(c) J is continuous;

(d) J dom T ⊆ dom T and $T J \subseteq J T .$

Then T has a self-adjoint extension.

ProoF. First note that if h∈dom T, then Jhedom T and $\pmb { h } = J ( J \pmb { h } )$ . Hence J dom $T = \mathrm{dom} T$ and $J T = T J$

Let $h \in \mathcal { H }$ and define $L \colon { \mathcal { H } } \to \mathbb { C }$ by $L ( f ) = \langle h , J f \rangle$ . Since J is conjugate linear, L is a linear functional. By (c), L is continuous. Thus there is a unique vector $h ^ { * }$ in $\mathcal { H }$ such that $L ( f ) = \langle f , h ^ { * } \rangle$ . Let $J ^ { * } h = h ^ { * }$ . Thus $J ^ { * } ; { \mathcal { H } } \to { \mathcal { H } }$ and

$$
\langle f , J ^ { * } h \rangle = \langle h , J f \rangle .
$$

It is clear that $J ^ { * }$ is additive. If $\alpha \in \mathbf { C } ,$ then $\langle f , J ^ { * } ( \alpha h ) \rangle = \langle \alpha h , J f \rangle =$ $\alpha \langle f , J ^ { * } h \rangle = \langle f , \bar { \alpha } J ^ { * } h \rangle$ . Thus $J ^ { * }$ is conjugate linear. Since $J ^ { 2 } = 1$ , it follows that $J ^ { * 2 } = 1$

Let hedom $T ^ { * }$ and f ∈dom T. Then $\langle T J f , h \rangle = \langle J f , T ^ { * } h \rangle = \langle J ^ { * } T ^ { * } h , f \rangle$ by (7.3). But also by $\langle T J f , h \rangle = \langle J T f , h \rangle = \langle J ^ { * } h , T f \rangle . \mathrm { S o } \langle J ^ { * } T ^ { * } h , f \rangle =$ $\langle J ^ { * } h , T f \rangle$ for all h in dom $T ^ { * }$ and f in dom T. But this says that $J ^ { * } h { \in } \mathrm { d o m } T ^ { * }$ whenever hedom $T ^ { * }$ and, furthermore, $T ^ { * } J ^ { * } h = J ^ { * } T ^ { * } h$ Since $J ^ { * 2 } = 1$ , it follows that $J ^ { * }$ dom $T ^ { * } = \mathrm { d o m } T ^ { * }$ and $J ^ { * } T ^ { * } = T ^ { * } J ^ { * }$

Now let heker $( T ^ { * } \pm i )$ Then $T ^ { * } J ^ { * } h = J ^ { * } T ^ { * } h = J ^ { * } ( \pm i h ) = \mp i J ^ { * } h .$ Thus $J ^ { * }$ $\ker ( T ^ { * } \pm i ) \subseteq \ker ( T ^ { * } \mp i )$ . Since $J ^ { *   2 } = 1 , J ^ { * }   \ker ( T ^ { * } \pm i ) = \ker ( T ^ { * } \mp i )$ . But $J ^ { * }$ is injective. Indeed, if $J ^ { * } h = 0 ,$ then $\begin{array} { r } { \pmb { h } = J ^ { * } ( J ^ { * } h ) = 0 . } \end{array}$ Thus the deficiency indices of T are equal. By Theorem 2.20, T has a self-adjoint extension. ■

PROOF OF THEOREM 7.1. (a) implies (b). If $\alpha _ { 0 } , \ldots , \alpha _ { n } { \in } \mathbb { C } ,$ then

$$
\begin{align*}\sum_{j,k=0}^{n} m_{j+k} \alpha_j \bar{\alpha}_k &= \int \sum_{j,k=0}^{n} \alpha_j \bar{\alpha}_k t^{j+k}   d\mu(t) \\&= \int \Bigg( \sum_{j=0}^{n} \alpha_j t^j \Bigg) \Bigg( \sum_{k=0}^{n} \bar{\alpha}_k t^k \Bigg) d\mu(t) \\&= \int \Bigg| \sum_{k=0}^{n} \alpha_k t^k \Bigg|^2   d\mu(t) \geqslant 0.\end{align*}
$$

(b) implies (c). Let $\mathcal { H } _ { 0 } =$ the collection of all finitely nonzero sequences of complex numbers $\{ \alpha _ { n } : n \geqslant 0 \}$ . That is, $\{ \alpha _ { 0 } , \alpha _ { 1 } , \ldots \} { \in } { \mathcal { H } } _ { 0 }$ if $\alpha _ { n } \in \mathbb { C }$ for all $n   \geqslant   0$ and $\alpha _ { n }   =   0$ for all but a finite number of values of n. If $x = \{ \alpha _ { n } \} , y = \{ \beta _ { n } \} \in \mathcal { H } _ { 0 }$ define $[ x , y ]$ by

## 7.4

$$
[ x , y ] \equiv \sum _ { j , k = 0 } ^ { \infty } m _ { j + k } \alpha _ { j } \overline { { { \beta } } } _ { k } .
$$

It is easy to see that $\mathcal { H } _ { 0 }$ is a vector space and (7.4) defines a semi-inner product on $\mathcal { H } _ { 0 }$ . In fact, it is routine that $[ \cdot , \cdot ]$ is sesquilinear and condition (b) implies that $[ x , x ]   \geqslant   0$ for all x in $\mathcal { H } _ { 0 }$

Let $\mathcal { H } _ { 0 } = \{ x \in \mathcal { H } _ { 0 } : [ x , x ] = 0 \}$ and let $\mathcal { H } _ { 1 }$ be the quotient vector space $\mathcal { H } _ { 0 } / \mathcal { H } _ { 0 }$ . If $\pmb { h } = \pmb { x } + \pmb { \mathcal { H } } _ { 0 }$ and $f = y + \mathcal{H}_{0} \in \mathcal{H}_{1}$ , then

$$
\langle h , f \rangle \equiv [ x , y ]
$$

can be verified to be a well-defined inner product on $\mathcal { H } _ { 1 }$ . Let $\mathcal { H }$ be the Hilbert space obtained by completing $\mathcal { H } _ { 1 }$ with respect to the norm defined by the inner product (7.5).

Now to define some operators. If $x = \{ \alpha _ { n } \} \in \mathcal { H } _ { 0 } ,$ let $T _ { 0 } x = \{ 0 , \alpha _ { 0 } , \alpha _ { 1 } , \ldots \}$ It is easy to check that $T _ { 0 }$ is a linear transformation on $\mathcal { H } _ { 0 }$ . Also, if $x = \{ \alpha _ { n } \}$ $y = \{ \beta _ { n } \} \in \mathcal { H } _ { 0 }$ , let $T _ { 0 } x = \{ \gamma _ { n } \}$ . So $\gamma _ { 0 }   =   0$ and $\gamma _ { n } = \alpha _ { n - 1 }$ $n \geqslant 1$ . Hence

$$
\begin{align*}\left[ T_{0}x, y \right] &= \sum_{j,k   =   0}^{\infty} m_{j   +   k}\gamma_{j}\bar{\beta}_{k} \\&= \sum_{j   =   1 \atop k   =   0}^{\infty} m_{j   +   k}\alpha_{j   -   1}\bar{\beta}_{k} \\&= \sum_{j,k   =   0}^{\infty} m_{j   +   k   +   1}\alpha_{j}\bar{\beta}_{k}.\end{align*}
$$

$$
\begin{aligned} &= \sum_{ \substack{ j =   0 \\ k =   1 } }^{\infty} m_{j + k} \alpha_{j} \overline{\beta}_{k -   1} \\&= [x,   T_{0} y].\\ \end{aligned}
$$

In particular, if $x   \in   \mathcal { H } _ { 0 } ,$ , then the preceding equation and the CBS inequality imply that

$$
\begin{aligned}\left| \left[ T_{0}x, T_{0}x \right] \right| &= \left| \left[ T_{0}^{2}x, x \right] \right| \leqslant \left[ T_{0}^{2}x, T_{0}^{2}x \right] \left[ x, x \right] \\&= 0\end{aligned}
$$

Hence $T _ { 0 } \mathcal { H } _ { 0 } \subseteq \mathcal { H } _ { 0 }$ . Thus $T _ { 0 }$ induces a linear transformation T on $\mathcal { H } _ { 1 }$ defined by $T ( x + \mathcal { H } _ { 0 } ) = T _ { 0 } x + \mathcal { H } _ { 0 }$ . It follows that $\langle T h , f \rangle = \langle h , T f \rangle$ for all $h , f$ in $\mathcal { H } _ { 1 }$ . Since $\mathcal { H } _ { 1 }$ is, by definition, dense in $\mathcal { H } , T$ is a densely defined symmetric operator on $\mathcal { H }$ . Now to show that T has a self-adjoint extension.

Define $J _ { 0 } \colon \mathcal { H } _ { 0 } \to \mathcal { H } _ { 0 }$ by $J _ { 0 } ( \{ \alpha _ { n } \} ) = \{ \tilde { \alpha } _ { n } \}$ . It is easy to see that $J _ { 0 }$ is conjugate linear and $J _ { 0 } ^ { 2 } = 1$ . Also, $J _ { 0 } T _ { 0 } = T _ { 0 } J _ { 0 } .$ An easy calculation shows that $[ J _ { 0 } x , J _ { 0 } y ] = [ x , y ]$ for all $x , y$ in $\mathcal { H } _ { 0 }$ . So $J _ { 0 } \mathcal { H } _ { 0 } \subseteq \mathcal { H } _ { 0 }$ and $J _ { 0 }$ induces a conjugate linear function $J _ { 1 } \colon \mathcal { H } _ { 1 } \to \mathcal { H } _ { 1 }$ defined by $J _ { 1 } ( x + \mathcal { H } _ { 0 } ) = J _ { 0 } x + \mathcal { H } _ { 0 }$ It follows that $J _ { 1 } T = T J _ { 1 } ,   J _ { 1 } ^ { 2 } = 1$ , and $\| \boldsymbol { J } _ { 1 } \boldsymbol { h } \| = \| \boldsymbol { h } \|$ for all h in $\mathcal { H } _ { 1 }$ . Thus $J _ { 1 }$ extends to a conjugate linear $J : \mathcal { H } \rightarrow \mathcal { H }$ such that $J ^ { 2 } = 1$ and $J \boldsymbol { h } \parallel = \parallel \boldsymbol { h } \parallel$ for all h in $\mathcal { H } ,$ Hence J is continuous. Also, J dom $T = J_{1} \mathcal{H}_{1} \subseteq \mathcal{H}_{1} = \mathrm{dom} T$ and $T J \subseteq J T$ By Proposition 7.2, T has a self-adjoint extension A.

Let $e _ { 0 } = \{ 1 , 0 , 0 , \ldots \} \in \mathcal { H } _ { 0 }$ . Hence $T _ { 0 } ^ { n } e _ { 0 }$ has a 1 in the nth place and zeros elsewhere. If $e = e _ { 0 } + \mathcal { H } _ { 0 }$ , then eedom $T ^ { n } \subseteq \operatorname { d o m } A ^ { n }$ for all $n \geqslant 0 .$ Also,

$$
\langle A ^ { n } e , e \rangle = [ T _ { 0 } ^ { n } e _ { 0 } , e _ { 0 } ] = m _ { n }
$$

for $n   \geqslant   0 .$

(c) implies (a). By the Spectral Theorem there is a spectral measure E for A. Let $\mu = E _ { e , e } ;$ by (4.11) µ is supported on R and, since eedom $A , \mu$ is finite. Moreover, since e∈dom $A ^ { n }$ for every $n \geqslant 0$ it follows (supply the details) that $\int t ^ { n }   d \mu ( t ) < \infty$ for every $n \geqslant 0 .$ Finally, by (4.9), $m _ { n } = \langle A ^ { n } e , e \rangle = \int t ^ { n }   d \mu ( t )$ for every $n \geqslant 0$

The measure obtained in Theorem 7.1 need not be unique since, in the proof that (b) implies (c) above, the self-adjoint extension of $T$ may not be unique. See pages 201–202 of Berg, Christensen, and Ressel [1984] for an example as well as further discussions of moment problems.

## EXERCISES

1. (Stieltjes.) Let $\left\{ m _ { n } : n \geqslant 0 \right\}$ be a sequence of real numbers and show that the following statements are equivalent. (a) There is a positive regular Borel measure $\mu$ on $[ 0 , \infty )$ such that $m _ { n } = \int t ^ { n }   d \mu ( t )$ for all $n   \geqslant   0$ (b) If $\alpha _ { 0 } , \ldots , \alpha _ { n } { \in } \mathbb { C } ,$ then $\begin{array} { r } { \sum _ { j , k = 0 } ^ { n } m _ { j + k } \alpha _ { j } \bar { \alpha } _ { k } \geqslant 0 } \end{array}$ and $\begin{array} { r } { \sum _ { j , k \; = \; 0 } ^ { n } m _ { j \; + \; k \; + \; 1 } \alpha _ { j } \bar { \alpha } _ { k } \geqslant 0 . } \end{array}$ (c) There is a self-adjoint operator A with $\sigma ( A ) \in [ 0 , \infty )$ and a vector e in dom $A ^ { n }$ for all $n   \geqslant   0$ such that $m _ { n } = \langle A ^ { n } e , e \rangle$ for $n   \geqslant   0 .$

2. (Bochner.) Let m: $\mathbf { R }   \rightarrow   \mathbf { C }$ be a function and show that the following statements are