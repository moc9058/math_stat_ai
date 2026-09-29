In fact, suppose $h \in \mathcal { H }$ and $h \perp \{ g _ { a } : g \in \mathcal { H } , \; a > 0 \}$ . Then by (5.5), for every $a   >   0$ and every $g$ in $\mathcal { H }$

$$
0 = \int _ { 0 } ^ { a } \langle U ( t ) h , g \rangle d t .
$$

Thus for every $g$ in $\mathcal { H } , \langle U ( t ) h , g \rangle = 0$ a.e. on $\mathbb { R }$ Because $\mathcal { H }$ is separable there is a subset $\Delta$ of R having measure zero such that if $t \notin \Delta , \langle U ( t ) h , g \rangle = 0$ whenever $g$ belongs to a preselected countable dense subset of $\mathcal { H } ,$ Thus $U(t)h = 0   if   t \notin \Delta$ But $\| \boldsymbol { h } \| = \| \boldsymbol { U } ( t ) \boldsymbol { h } \|$ , so $h   =   0$ and the claim is established. Now if $s { \in } \mathbb { R }$

$$
\begin{align*}\langle h, U(s)g_a \rangle &= \langle U(-s)h, g_a \rangle \\&= \int_{0}^{a} \langle U(t-s)h, g \rangle dt \\&= \int_{-s}^{a-s} \langle U(t)h, g \rangle dt.\end{align*}
$$

Thus $\langle h , U ( s ) g _ { a } \rangle \to \langle h , g _ { a } \rangle \mathrm { a s } s \to 0 .$ By the claim and the fact that the group is uniformly bounded, $U : \mathbb { R } \to ( { \mathcal { B } } ( { \mathcal { H } } )$ , WOT) is continuous at 0. By the group property, $U : \mathbb { R } \to ( { \mathcal { B } } ( { \mathcal { H } } )$ , WOT) is continuous. Hence $U$ is SOT-continuous (Exercise 1). ■

We now turn our attention to the principal result of this section, Stone's Theorem, which states that the converse of Theorem 5.1 is valid. Note that if $U ( t ) = \exp ( i t A )$ for a self-adjoint operator $A ,$ then part (d) of Theorem 5.1 instructs us how to recapture $A .$ This is the route followed in the proof of Stone's Theorem, proved in Stone [1932].

5.6. Stone's Theorem. If U is a strongly continuous one parameter unitary group, then there is a self-adjoint operator A such that $U ( t ) = \exp ( i t A )$

PROOF. Begin by defining $\mathcal { D }$ to be the set of all vectors h in $\mathcal { H }$ such that $\operatorname* { l i m } _ { t \to 0 } t ^ { - 1 } [ U ( t ) h - h ]$ exists; since $0 { \in } { \mathcal { D } } , { \mathcal { D } } \neq \square$ . Clearly $\mathcal { D }$ is a linear manifold in $\mathcal { H }$

## 5.7. Claim. $\mathcal { D }$ is dense in $\mathcal { H }$

Let $\mathcal { L } = \mathrm { a l l }$ continuous functions $\phi$ on R such that $\phi   \in   L ^ { 1 } ( 0 , \infty )$ . Hence for any h in $\mathcal { H } ,   t   \mapsto   \phi ( t ) U ( t ) h$ is a continuous function of R into $\mathcal { H }$ . Because $\| \boldsymbol{U}(t) \boldsymbol{h} \| = \| \boldsymbol{h} \|$ for all t, a Riemann integral, $\begin{array} { r } { \int _ { 0 } ^ { \infty } \phi ( t ) U ( t ) h   d t . } \end{array}$ , can be defined and is a vector in $\mathcal { H }$ . Put

$$
T _ { \phi } h = \int _ { 0 } ^ { \infty } \phi ( t ) U ( t ) h   d t .
$$

It is easy to see that $T _ { \phi } : \mathcal { H } \rightarrow \mathcal { H }$ is linear and bounded with $\| T _ { \phi } \| \leqslant \int _ { 0 } ^ { \infty } | \phi ( t ) | d t .$

Similarly, for each $\phi$ in $\mathcal { L }$

5.9

$$
S _ { \phi } h = \int _ { 0 } ^ { \infty } \phi ( t ) U ( - t ) h   d t .
$$

defines a bounded operator on $\mathcal { H }$

For any $\phi$ in $\mathcal { L }$ and t in $\mathbb { R } _ { \cdot }$

$$
\begin{align*}U(t)T_{\phi}h &= U(t)\int_{0}^{\infty}\phi(s)U(s)h ds \\&= \int_{0}^{\infty}\phi(s)U(t + s)h ds \\&= \int_{t}^{\infty}\phi(s - t)U(s)h ds.\end{align*}
$$

Similarly,

$$
U ( t ) S _ { \phi } h = \int _ { - t } ^ { \infty } \phi ( s + t ) U ( - s ) h d s .
$$

Now let $\mathcal { L } ^ { ( 1 ) }   =   \mathrm { a l l }$ $\phi$ in $\mathcal { L }$ that are continuously differentiable with $\phi ^ { \prime }$ in $\mathcal { L }$ For $\phi$ in $\mathcal { L } ^ { ( 1 ) }$

$$
- \frac{i}{t} \left[ U(t) - 1 \right] T_{\phi} h = - \frac{i}{t} \int_{t}^{\infty} \phi(s - t) U(s) h ds + \frac{i}{t} \int_{0}^{\infty} \phi(s) U(s) h ds \\= - i \int_{t}^{\infty} \left[ \frac{\phi(s - t) - \phi(s)}{t} \right] U(s) h ds + \frac{i}{t} \int_{0}^{t} \phi(s) U(s) h ds.
$$

Now

$$
\left\| \int_{0}^{t} \left[ \frac{\phi(s-t) - \phi(s)}{t} \right] U(s) h ds \right\| \leq \| h \| \sup \left\{ \left| \phi(s-t) - \phi(s) \right| : 0 \leq s \leq 1 \right\} \rightarrow 0.
$$

as $t   \to   0 ,$ Hence

$$
\begin{align*}\lim_{t \to 0} \int_{t}^{\infty} \left[ \frac{\phi(s-t) - \phi(s)}{t} \right] U(s) h ds &= - \int_{0}^{\infty} \phi'(s) U(s) h ds \\&= - T_{\phi} h.\end{align*}
$$

Since $s   \mapsto   \phi ( s ) U ( s ) \pmb { h }$ is continuous and $U ( 0 )   =   1$ , the Fundamental Theorem of Calculus implies that

$$
\lim _ { t \rightarrow 0 } \frac { 1 } { t } \int _ { 0 } ^ { t } \phi ( s ) U ( s ) h   d s = \phi ( 0 ) h .
$$

Hence for $\phi$ in $\mathcal { L } ^ { ( 1 ) }$ and $h$ in $\mathcal { H }$

5.10

$$
\lim _ { t \rightarrow 0 } - \frac { i } { t } \left[ U ( t ) - 1 \right] T _ { \phi } h = i T _ { \phi } h + i \phi ( 0 ) h .
$$

5.11

Similarly, for $\phi$ in $\mathcal { L } ^ { ( 1 ) }$ and h in $\mathcal { H } .$

$$
\operatorname * { l i m } _ { t \rightarrow 0 } - \frac { i } { t } [ U ( t ) - 1 ] S _ { \phi } h = - i S _ { \phi } . h - i \phi ( 0 ) h .
$$

So (5.10) implies that

$$
\mathcal { D } \supseteq \{ T _ { \phi } h \colon \phi   \in   \mathcal { L } ^ { ( 1 ) } \mathrm { ~ a n d ~ } h   \in   \mathcal { H } \} .
$$

But for every positive integer n there is a $\phi _ { n }$ in $\mathcal { L } ^ { ( 1 ) }$ such that $\phi _ { n } \geqslant 0 , \phi _ { n } ( t ) = 0$ for $t \geqslant 1 / n ,$ and $\int _ { 0 } ^ { \infty } \phi _ { n } ( t ) d t = 1$ (Exercise 2). Hence

$$
T _ { \phi _ { n } } h - h = \int _ { 0 } ^ { 1 / n } \phi _ { n } ( t ) [ U ( t ) - 1 ] h d t .
$$

and so | $\| T _ { \phi _ { n } } h - h \| \leqslant \sup \left\{ \| U ( t ) h - h \| : 0 \leqslant t \leqslant 1 / n \right\}$ . Therefore $\| T _ { \phi _ { n } } h - h \| \to 0$ as $n   \to   \infty$ since U is strongly continuous. This says that $\mathcal { D }$ is dense.

For h in $\mathcal { D } ,$ define

## 5.12

$$
A h = - i \lim _ { t \rightarrow 0 } \frac { 1 } { t } \left[ U ( t ) - 1 \right] h .
$$

## 5.13. Claim. A is symmetric.

The proof of this is left to the reader.

By (2.2c), A is closable; also denote the closure of A by A. According to Corollary 2.9, to prove that A is self-adjoint it suffices to prove that ker $( A ^ { * } \pm i )   =   ( 0 )$ . Equivalently, it suffices to show that $\operatorname { \mathsf { r a n } } ( A \pm i )$ is dense. It will be shown that there are operators $B _ { \pm }$ such that $( A \pm i ) B _ { \pm } = 1$ , so that $A \pm i$ is surjective.

Notice that according to (5.10),

$$
( A + i ) T _ { \phi } = A T _ { \phi } + i T _ { \phi } = i ( T _ { \phi ^ { \prime } } + T _ { \phi } ) + i \phi ( 0 ) .
$$

So taking $\phi ( t ) = - i e ^ { - 1 } , ( A + i ) T _ { \phi } = 1$ . According to (5.11),

$$
( A - i ) S _ { \psi } = A S _ { \psi } - i S _ { \psi } = - i ( S _ { \psi ^ { \prime } } + S _ { \psi } ) - i \psi ( 0 ) .
$$

Taking $\psi ( t ) = i e ^ { - 1 } , ( A - i ) S _ { \psi } = 1$ . Hence A is self-adjoint.

Put $V ( t ) = \exp ( i A t )$ . It remains to show that $V = U$ .Let $h \in \mathcal { D }$ . By Theorem 5.1(d),

$$
s ^ { - 1 } [ V ( t + s ) - V ( t ) ] h = s ^ { - 1 } [ V ( s ) - 1 ] V ( t ) h \rightarrow i A V ( t ) h ;
$$

that is, $V ^ { \prime } ( t ) h = i A V ( t ) h .$ Similarly,

$$
s ^ { - 1 } [ U ( t + s ) - U ( t ) ] h = s ^ { - 1 } [ U ( s ) - 1 ] U ( t ) h \to i A U ( t ) h .
$$

So if $h ( t ) = U ( t ) h - V ( t ) h ,$ then h: $\mathbb { R } \rightarrow \mathcal { H }$ is differentiable and

$$
h ^ { \prime } ( t ) = i A U ( t ) h - i A V ( t ) h = i A h ( t ) .
$$

But

$$
\begin{align*}\frac{d}{dt}\|h(t)\|^2 &= \langle h'(t), h(t) \rangle + \langle h(t), h'(t) \rangle \\&= \langle iAh(t), h(t) \rangle + \langle h(t), iAh(t) \rangle.\end{align*}
$$

Thus $\left( \boldsymbol{d} / \boldsymbol{d} t \right) \| \boldsymbol{h}(t) \|^2 = 0$ and so $\| \boldsymbol { h } \| \colon \mathbb { R } \to \mathbb { R }$ is a constant function. But $h ( 0 ) = 0 ,$ SO $h ( t ) \equiv 0$ This says that $U ( t ) \dot { \boldsymbol { h } } = V ( t ) \dot { \boldsymbol { h } }$ for all h in $\mathcal { D }$ and all t in R. Since D is dense, $U = V .$

5.14. Definition. If U is a strongly continuous one parameter unitary group, then the self-adjoint operator A such that $U ( t ) = \exp ( i t A )$ is called the infinitesimal generator of U.

By virtue of Stone's Theorem and Theorem 5.1, there is a one-to-one correspondence between self-adjoint operators and strongly continuous one-parameter unitary groups. Thus, it should be possible to characterize certain properties of a group in terms of its infinitesimal generator and vice versa. For example, suppose the infinitesimal generator is bounded; what can be said about the group? (Also see Exercise 6.)

5.15. Proposition. If U is a strongly continuous one parameter unitary group with infinitesimal generator A, then A is bounded if and only if $\operatorname* { l i m } _ { t \to 0 } \| U ( t ) - 1 \| = 0$

PRooF. First assume that A is bounded. Hence $\| U ( t ) - 1 \| = \| \exp ( i t A ) - 1 \| =$ sup $\left\{ \left| e^{itx} - 1 \right| : x \in \sigma(A) \right\} \rightarrow 0$ as $t   \rightarrow   0$ since $\sigma ( A )$ is compact.

Now assume that l $U ( t ) - 1 \parallel \rightarrow 0$ as $t   \rightarrow   0$ Let $0 < \varepsilon < \pi / 4 ;$ then there is a $t _ { 0 }   >   0$ such that $\| U ( t ) - 1 \| < \varepsilon$ for $| t | < t _ { 0 } .$ Since $U ( t ) - 1 = \int _ { \sigma ( A ) } ( e ^ { i x t } - 1 ) d E ( t ) ,$ sup $\left\{ \left| e^{i x t} - 1 \right| : x \in \sigma(A) \right\} = \left\| U(t) - 1 \right\| < \varepsilon$ for $| t | < t _ { 0 }$ Thus for a small $\delta ,$ $t x \in \bigcup _ { n = - \infty } ^ { \infty } ( 2 \pi n - \delta , 2 \pi n + \delta ) \equiv G$ whenever $x { \in } { \sigma } ( A )$ and $| t | < t _ { 0 }$ . In fact, if ε is chosen sufficiently small, then $\delta$ is small enough that the intervals $\left\{ \left( 2 \pi n - \delta , 2 \pi n + \delta \right) \right\}$ are the components of G. If x∈σ(A), {tx: $0 \leqslant t < t_{0} \}$ is the interval from 0 to $t _ { 0 } x$ and is contained in G. Hence $t x { \in } ( - \delta , \delta )$ for x in $\sigma ( A )$ and $| t | < t _ { 0 }$ . In particular, $t _ { 0 } \sigma ( A ) \in [ - \delta , \delta ]$ sO $\sigma ( A )$ is compact and A is bounded. ■

Let μ be a positive measure on R and let $A _ { \mu } f = x f$ for f in $\mathcal { D } _ { \mu } = \{ f \in L ^ { 2 } ( \mu ) \}$ $x f   \in   L ^ { 2 } ( \mu ) \}$ We have already seen that $A _ { \mu }$ is self-adjoint. Clearly exp $( i t A _ { \mu } ) = M _ { e _ { t } }$ on $L ^ { 2 } ( \mathbb { R } )$ , where $e _ { t }$ is the function $e _ { t } ( x ) = \exp ( i t x )$ . This can be generalized a bit.

5.16. Proposition. Let $( X , \Omega , \mu )$ be a σ-finite measure space and let φ be a real-valued Ω-measurable function on X. If $A = M _ { \phi }$ on $L ^ { 2 } ( \mu )$ and $U ( t ) = \exp ( i t A )$ , then $U ( t ) = M _ { e _ { t } } ,$ where $e _ { t } ( x ) = \exp ( i t \phi ( x ) )$

Since each self-adjoint operator on a separable Hilbert space can be represented as a multiplication operator (Theorem 4.19), the preceding proposition gives a representation of all strongly continuous one parameter semigroups.

## EXERCISES

1. If $U \colon \mathbb { R } \to { \mathcal { B } } ( { \mathcal { H } } )$ is such that $U ( t )$ is unitary for all $t , \; U ( s + t ) = U ( s ) U ( t )$ for all $s ,$ $t ,$ and $U \colon \mathbb { R }   \to   ( { \mathcal { B } } ( { \mathcal { H } } ) , \mathrm { W O T } )$ is continuous, then U is SOT-continuous.

2. Show that for every integer n there is a continuously differentiable function $\phi _ { n }$ such that both $\phi _ { n }$ and $\phi _ { n } ^ { \prime } \in L ^ { 1 } ( 0 , \infty ) , \phi _ { n } ( t ) = 0 \mathrm { i f } t \geqslant 1 / n ,$ and $\int _ { 0 } ^ { \infty } \phi _ { n } ( t ) d t = 1$

3. Prove Claim 5.13.

4. Adopt the notation from the proof of Stone's Theorem. Let $\phi , \psi \in \mathcal { L }$ and show: (a) $T _ { \phi } ^ { * } = S _ { \bar { \phi } } ;   ( \mathrm { b } ) T _ { \phi } T _ { \psi } = T _ { \phi _ { * } \psi } \mathrm { a n d } S _ { \phi } S _ { \psi } = S _ { \phi _ { * } \psi } ;   ( \mathrm { c } ) T _ { \phi } A \subseteq A T _ { \phi } .$

5. Let U be a strongly continuous one parameter unitary group with infinitesimal generator A. Suppose e is a nonzero vector in $\varkappa$ such that $A e = \lambda e$ . What is $U ( t ) e ?$ Conversely, suppose there is a nonzero t such that $U ( t )$ has an eigenvector. What can be said about $A ? U ( s ) ?$

6. (This exercise is designed to give another proof of Proposition 5.15 as well as give additional information. My thanks to R.B. Burckel for pointing this out to me.) Let U be a strongly continuous one- parameter unitary group with infinitesimal generator A. Show that if $\| U ( t ) - 1 \| \to 0$ as $t   \rightarrow   0 ,$ then as $t \to 0 , t ^ { - 1 } \int _ { a } ^ { a + t } U ( s ) d s \to U ( a )$ in norm. From here show that as $t \to 0 , t ^ { - 1 } [ U ( t ) - 1 ]$ has a norm limit, and hence A is a bounded operator since it is the norm limit of bounded operators.

## §6. The Fourier Transform and Differentiation

Perhaps the best way to begin this section is by examining an example.

6.1. Example. Let $\mathcal { D } = \{ f \in L ^ { 2 } ( \mathbb { R } ) \}$ f is absolutely continuous on every bounded interval in R and $f ^ { \prime } { \in } L ^ { 2 } ( \mathbb { R } ) \}$ . For f in $\mathcal { D } ,$ let $A f = i f ^ { \prime }$ . Then A is self-adjoint.

First let's show that A is symmetric. If $f \in \mathcal { D } _ { 1 }$ , note that $f(x) \to 0   as   x \to \pm \infty$ since $f$ and $f ^ { \prime } { \in } L ^ { 2 } ( \mathbb { R } )$ . So if $f ,   g \in \mathcal { D } ,   0 < a < \infty$ 5

$$
i \int_{-a}^{a} f'(x) \overline{g(x)} dx = i \left[ f(a) \overline{g(a)} - f(-a) \overline{g(-a)} \right] - i \int_{-a}^{a} f(x) \overline{g'(x)} dx.
$$

Hence $\langle A f , g \rangle = \langle f , A g \rangle$ and A is symmetric.

Now let gedom $A ^ { * }$ and for $0 < a < \infty$ let $\mathcal { D } _ { a } = \{ f \in \mathcal { D } : f ( x ) = 0 \mathrm { ~ f o r ~ } | x | \geqslant a \}$ The proof that g∈dom A follows the lines of the argument used in Example 1.11. In fact, let $h = A ^ { * } g$ So if $f \in \mathcal { D } .$ then $\int f(x) \overline{h(x)}   dx =$ $i \int f^{\prime}(x) \overline{g(x)} dx$ .Let $H(x) = \int_{0}^{x} h(t)   dt$ . Then using integration by parts we get that

for f in $\mathcal { D } _ { \alpha }$

$$
\begin{align*}\int_{-a}^{a} f \bar{h} &= \overline{H(a)} f(a) - \overline{H(-a)} f(-a) - \int_{-a}^{a} f' \bar{H} \\&= - \int_{-a}^{a} f' \bar{H}.\end{align*}
$$

Therefore $\int _ { - a } ^ { a } f ^ { \prime } [ \bar { H } - ( \bar { \imath } \bar { g } ) ] = 0$ for every f in $\mathcal { D } _ { a ^ { \cdot } } \mathbf { A } \mathbf { s }$ in (1.11), it follows that $H - i g$ is coñstant on $[ - a , a ]$ and g is absolutely continuous. Moreover, $0 = H ^ { \prime } - i g ^ { \prime } = h - i g ^ { \prime } ;$ hence $A^{*}g = h =ig^{\prime}$ . Thus $g \in \mathcal { D }$ and A is self-adjoint.

If A is the differentiation operator in Example 6.1, what is the group $U ( t ) = \exp ( i t A ) ?$ Since A is not represented as a multiplication operator, Proposition 5.16 cannot be applied. One could proceed to try and discover the spectral measure for A. Since $A = \int x d E ( x ) , U ( t ) = \int e ^ { i t x } d E ( x )$ . Or one could be clever.

Later in this section it will be shown that if $\mathcal { F } \colon L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ is the Fourier-Plancherel transform, then $\mathcal { F }$ is a unitary operator (6.17) and $\mathcal{F}^{-1} A \mathcal{F} =$ the operator on $L ^ { 2 } ( \mathbb { R } )$ of multiplication by the independent variable (6.18). Thus $\mathcal { F } ^ { - 1 } U ( t ) \mathcal { F }$ is multiplication by $e ^ { i x t } ,$ But it is possible to find U(t) directly.

Recall that if f ∈dom A,

$$
A f = - i \lim _ { t \rightarrow 0 } \frac { U ( t ) f - f } { t }
$$

So

$$
f^{\prime}(x)=\lim_{t \to 0}-\frac{(U(t)f)(x)-f(x)}{t}
$$

Being clever, one might guess that $( U ( t ) f ) ( x ) = f ( x - t )$

6.2. Theorem. If A and $\mathcal { D }$ are as in Example 6.1 and $U ( t ) = \exp ( i t A )$ , then $( U ( t ) f ) ( x ) = f ( x - t )$ for all f in $L ^ { 2 } ( \mathbb { R } )$ and x,t in R.

PROOF. Let $(V(t)f)(x) = f(x - t)$ . It is easy to see that V is a strongly continuous one parameter unitary group. Let B be the infinitesimal generator of V. It must be shown that $B = A$

Note that f ∈dom B if and only if $\operatorname* { l i m } _ { t \to 0 } t ^ { - 1 } ( V ( t ) f - f )$ exists. Let $f   \in   \mathsf { C } _ { c } ^ { ( 1 ) } ( \mathbb { R } ) ;$ that is, f is continuously differentiable and has compact support. Thus for $t > 0$

$$
\left[ \frac{V(t)f - f}{t} \right](x) = \frac{f(x - t) - f(x)}{t} = - \frac{1}{t} \int_{x - t}^{x} f'(y)dy
$$

and

$$
\begin{aligned}\left| \frac{V(t)f(x) - f(x)}{t} + f^{\prime}(x) \right| & \leqslant \frac{1}{t} \int_{x - t}^{x} \left| f^{\prime}(x) - f^{\prime}(y) \right| dy \\& \leqslant \sup \left\{ \left| f^{\prime}(x) - f^{\prime}(y) \right| : |x - y| \leqslant t \right\}.\end{aligned}
$$

Because $f ^ { \prime }$ is continuous with compact support, $f ^ { \prime }$ is uniformly continuous. Let $K = \{ x : \mathrm { d i s t } ( x , \mathrm { s p t } f ^ { \prime } ) \leqslant 2 \}$ . So K is compact. For $\varepsilon   >   0 .$ , let $\delta ( \varepsilon ) < 1$ be such that if $| x - y | < \delta ( \varepsilon ) .$ , then $| f ^ { \prime } ( x ) - f ^ { \prime } ( y ) | < \varepsilon .$ Hence $\| t ^ { - 1 } [ V f - f ] + f ^ { \prime } \| _ { 2 } \leqslant$ $\varepsilon ^ { 2 } | K | ,$ where $| K | =$ the Lebesgue measure of K. Thus $C _ { c } ^ { ( 1 ) } ( \mathbb { R } ) \subseteq$ dom B and $B f = A f$ for f in $C _ { c } ^ { ( 1 ) } ( \mathbb { R } )$ . But if $f { \in } \mathbf { d o m } A ,$ there is a sequence $\{ f _ { n } \} \subseteq C _ { c } ^ { ( 1 ) } ( \mathbb { R } )$ such that $f _ { n } { \oplus } A f _ { n } { \to } f { \oplus } A f$ in gra A (Exercise 1). But $f_{n} \oplus A f_{n}=f_{n} \oplus B f_{n} \in \operatorname{grad} B,$ so $f \oplus A f \in \mathrm{grad} B;$ that is, $A \subseteq B$ Since self-adjoint operators are maximal symmetric operators (2.11), $A = B ,$ ■

To show that the Fourier transform demonstrates that $M _ { x }$ and $i d / d x$ are unitarily equivalent, we introduce the Schwartz space of rapidly decreasing functions.

6.3. Definition. A function φ: $\mathbb { R }   \rightarrow   \mathbb { R }$ is rapidly decreasing if $\phi$ is infinitely differentiable and for all integers $m ,   n \geqslant 0$

6.4

$$
\| \phi \| _ { m , n } \equiv \sup \left\{ \left| x ^ { m } \phi ^ { ( n ) } ( x ) \right| : x \in \mathbb { R } \right\} < \infty.
$$

Let $\mathcal { S } = \mathcal { P } ( \mathbb { R } )$ be the set of all rapidly decreasing functions on $\mathbb { R }$

Note that if $\phi \in \mathcal { S }$ , then for all $m , n \geqslant 0$ there is a constant $C _ { m , n }$ such that

$$
| \phi ^ { ( n ) } ( x ) | \leqslant C _ { m , n } | x | ^ { - m } .
$$

Thus if $p$ is any polynomial and $n \geqslant 0,\ \left| p(x) \phi^{(n)}(x) \right| \to 0$ as $| x |   \to   \infty$ . In fact, this is equivalent to $\phi$ belonging to $\mathcal { S }$ (Exercise 3). Also note that if $\phi \in \mathcal { S }$ then $x ^ { m } \phi ^ { ( n ) } \in \mathcal { G }$ for all $m , n \geqslant 0$

It is not difficult to see that $\left\| \cdot \right\| _ { m , n }$ is a seminorm on ${ \mathcal { S } } . ~ \mathrm { A l s o } ,   { \mathcal { S } }$ with all of these seminorms is a Fréchet space (Exercise 2). The space $\mathcal { S }$ is sometimes called the Schwartz space after Laurent Schwartz.

6.5. Proposition. If $1 \leqslant p \leqslant \infty, \mathcal{S} \subseteq L^{p}(\mathbb{R}). If   1 \leqslant p < \infty, \mathcal{S}$ is dense in $L ^ { p } ( \mathbb { R } ) ;$ $\mathcal { S }$ is weak-star dense in $L ^ { \infty } ( \mathbb { R } )$

PRoOF. We already have that $\mathcal { S } \subseteq L ^ { \infty } ( \mathbb { R } )$ . If $1 \leqslant p < \infty$ and $\phi \in \mathcal { S }$ , then

$$
\int _ { - \infty } ^ { \infty } | \phi | ^ { p } d x = \int _ { - \infty } ^ { \infty } ( 1 + x ^ { 2 } ) ^ { - p } ( 1 + x ^ { 2 } ) ^ { p } | \phi | ^ { p } d x
$$

$$
\leqslant \| ( 1 + x ^ { 2 } ) ^ { p } | \phi | ^ { p } \| _ { \infty } \int _ { - \infty } ^ { \infty } ( 1 + x ^ { 2 } ) ^ { - p } d x .
$$

Since $( 1 + x ^ { 2 } ) ^ { p } \geqslant 1 + x ^ { 2 } .$

$$
\begin{align*}\| \phi \|_p \leqslant \pi^{1/p} \| (1 + x^2) \phi \|_\infty \\\leqslant \pi^{1/p} [ \| \phi \|_{0,0} + \| \phi \|_{2,0} ].\end{align*}
$$

Since $C _ { c } ^ { ( \infty ) } ( \mathbb { R } ) \subseteq { \mathcal { S } }$ , the density statements are immediate.

6.6. Definition. If $f   \in   L ^ { 1 } ( \mathbb { R } )$ , the Fourier transform of f is the function $\hat { f }$ defined

by

$$
\hat { f } ( x ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { \mathbb { R } } f ( t ) e ^ { - i x t } d t.
$$

Because $f   \in   L ^ { 1 } ( \mathbb { R } ) ,$ , this integral is well defined.

The interested reader may want to peruse $\S \mathbf { V } \Pi . 9 ,$ where the Fourier transform is presented in the more general context of locally compact abelian groups. That section will not be assumed here.

Recall that if $f ,   g   \in   L ^ { 1 }$ , then the convolution of f and $g ,$

$$
f * g(x) = (2\pi)^{-1/2} \int_{\mathbb{R}} f(x-t)g(t)dt,
$$

belongs to $L ^ { 1 } ( \mathbb { R } )$ and $\| f \star g \| _ { 1 } \leqslant \| f \| _ { 1 } \| g \| _ { 1 }$ if the norm of a function f in $L ^ { 1 } ( \mathbb { R } )$ is defined as $\| f \| _ { 1 } \equiv ( 2 \pi ) ^ { - 1 / 2 } \int | f ( x ) | d x$ . It is also true that if $f   \in   L ^ { p } ( \mathbb { R } )$ $1 \leqslant p \leqslant \infty$ , then $f * g \in L ^ { p } ( \mathbb { R } )$ and $\| f \cdot g \| _ { p } \leqslant \| f \| _ { p } \| g \| _ { 1 }$ (see Exercise 4).

6.7. Theorem. (a) $If \in L^{1}(\mathbb{R}),$ then f is a continuous function on R that vanishes $at \pm \infty. Also, \| \hat{f} \|_{\infty} \leqslant \| f \|_{1}$

(b) If $\scriptstyle \phi \in { \mathcal { S } } ,   { \hat { \phi } } \in { \mathcal { S } }$ . Also for $m , n \geqslant 0$

6.8

$$
(ix)^m \left( \frac{d}{dx} \right) \hat{\phi} = \left[ \left( \frac{d}{dx} \right)^m \left( (-ix)^n \phi \right) \right]^n.
$$

(c) If $f , g { \in } L ^ { 1 } ( \mathbb { R } ) ,$ then $( f * g ) ^ { \wedge } = { \hat { f } } { \hat { g } } .$ If f and $g \in { \mathcal { S } } _ { 1 }$ , then $f * g \in { \mathcal { P } } .$ (Note: $[ \hat { \mathbf { \Sigma } } ] ^ { \hat { \mathbf { \Sigma } } } = t h e$ Fourier transform of the function defined in the brackets.)

PROOF. (a) The fact that $\hat { f }$ is continuous is an easy consequence of Lebesgue's Dominated Convergence Theorem; it is clear that $\| \hat { f } \| _ { \infty } \leqslant \| f \| _ { 1 }$ . For the other part of (a), let f = the characteristic function of the interval $( a , b )$ Then $\hat { f } ( x ) = i ( 2 \pi ) ^ { - 1 / 2 } x ^ { - 1 } \left[ e ^ { - i x b } - e ^ { - i x a } \right] \rightarrow 0 \text { as } | x | \rightarrow \infty \text {. So } \hat { f } ( x )$ vanishes $\mathfrak { a t } \pm \infty$ if f is a linear combination of such characteristic functions. The result for a general f follows by approximation.

(b) It is convenient to introduce the notation $D \phi = \phi ^ { \prime }$ . Thus $D ^ { n } \phi = \phi ^ { ( n ) }$ Also in this proof, as in many others of this section, x will be used to denote the function whose value at t is t and it will also be used occasionally to denote the independent variable.

If $\phi \in \mathcal { S }$ , then differentiation under the integral sign (Why is this justified?) gives

$$
\begin{aligned} (D\hat{\phi})(y) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} (-it)e^{-it} \phi(t)dt \\&= [(-ix)\phi]^{\hat{}}(y).\\ \end{aligned}
$$

By induction we get that for $n   \geqslant   0$

6.9

$$
D ^ { n } \hat { \phi } = \left[ ( - i x ) ^ { n } \phi \right] ^ { \star } .
$$