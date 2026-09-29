the variation for $E _ { h , f }$ . Let $\phi _ { n } = \sum _ { k = 1 } ^ { n } \chi _ { \Delta _ { k } } \phi ;$ so $\phi _ { n }$ is bounded, as is $u \phi _ { n }$ . Thus

$$
\begin{align*}\int \lvert \phi_n \rvert d \lvert E_{h,f} \rvert &= \int \lvert \phi_n \rvert u d E_{h,f} \\&= \left\langle \left( \int \lvert \phi_n \rvert u d E \right) h, f \right\rangle \\&\leqslant \| f \| \left\| \left( \int \lvert \phi_n \rvert u d E \right) h \right\|.\end{align*}
$$

But

$$
\begin{align*}\left\| \left( \int |\phi_n| u d E \right) h \right\|^2 &= \left\langle \left( \int |\phi_n| u d E \right) h, \left( \int |\phi_n| u d E \right) h \right\rangle \\&= \left\langle \left( \int |\phi_n|^2 d E \right) h, h \right\rangle \\&= \int |\phi_n|^2 d E_{h,h} \\&\leqslant \int |\phi|^2 d E_{h,h}.\end{align*}
$$

Combining this with the preceding inequality gives that $\int | \phi _ { n } | d | E _ { h , f } | \leqslant$ $\| f \| ( \int | \phi | ^ { 2 } d E _ { h , h } ) ^ { 1 / 2 }$ for all n. Letting $n   \to   \infty$ gives (4.8). Since $\phi _ { n }$ is bounded, $\left\langle \left( \int \phi _ { n } d E \right) h , f \right\rangle = \int \phi _ { n } d E _ { h , f }$ If $h \in \mathcal { D } _ { \phi }$ and $f \in \mathcal { H }$ , then (4.8) and the Lebesgue Dominated Convergence Theorem imply that $\int \phi _ { n } d E _ { h , f } \rightarrow \int \phi d E _ { h , f }$ as $n   \to   \infty$ But

$$
\begin{align*}\left( \int \phi_n d E \right) h = \left( \int \phi d E \right) E \left( \bigcup_{j=1}^n \Delta_j \right) h \\= E \left( \bigcup_{j=1}^n \Delta_j \right) \left( \int \phi d E \right) h.\end{align*}
$$

Since $E(\bigcup_{j = 1}^{n} \Delta_{j}) \to E(X) = 1  (SOT) as   n \to \infty, \quad \langle (\int \phi_{n}dE)h, f \rangle \to \langle (\int \phi dE)h, f \rangle$ as $n   \to   \infty$ . This proves (4.9). ■

Note that as a consequence of (4.7) dom $N _ { \phi }$ and the definition of $N _ { \phi }$ do not depend on the choice of the sets $\{ \Delta _ { n } \}$ , as would seem to be the case from (4.5) and (4.6). Also, by (4.7.a), E(∆)h ∈ dom $N _ { \phi }$ if h ∈ dom $N _ { \phi }$

4.10. Theorem. ${ \mathit { I f } } \left( X , \Omega \right)$ is a measurable space, $\mathcal { H }$ is a Hilbert space, and E is a spectral measure for $( X , \Omega , { \mathcal { H } } ) ,$ let $\Phi ( X , \Omega )$ be the algebra of all Ω-measurable functions $\phi \colon X   \to   \mathbb { C }$ and define $\rho \colon \Phi ( X , \Omega )   \to   \mathcal { C } ( \mathcal { H } ) \mathrm { ~ } b y \mathrm { ~ } \rho ( \phi )   =   \int \phi   d E .$ Then for $\phi , \psi$ in $\Phi ( X , \Omega )$

(a) $\rho ( \phi ) ^ { * } = \rho ( \overline { { \phi } } ) ;$

(b) $\rho ( \phi \psi )   \supseteq   \rho ( \phi ) \rho ( \psi )$ and dom $( \rho ( \phi ) \rho ( \psi ) ) = \mathcal { D } _ { \psi } \cap \mathcal { D } _ { \phi \psi }$ 2

(c) If ψ is bounded, $\rho ( \phi ) \rho ( \psi )   =   \rho ( \psi ) \rho ( \phi )   =   \rho ( \phi \psi ) ;$

(d) $\rho ( \phi ) ^ { * } \rho ( \phi ) = \rho ( | \phi | ^ { 2 } )$

The proof of this theorem is left as an exercise.

4.11. The Spectral Theorem. If N is a normal operator on $\mathcal { H } ,$ then there is a unique spectral measure E defined on the Borel subsets of C such that:

(a) $N = \int z   d E ( z ) ;$

(b) $E ( \Delta ) = 0  { i f } \Delta \cap \sigma ( N ) = \square ;$

(c) if U is an open subset of C and $U \cap \sigma ( N ) \neq \square$ , then $E ( U ) \neq 0 ;$

(d) if $A   \in   \mathcal { B } ( \mathcal { H } )$ such that $A N \subseteq N A$ and $A N ^ { * } \subseteq N ^ { * } A$ then $A ( \int \phi   d E ) \subseteq$ $( \int   \phi   d E ) A   f _ { } { o r }$ every Borel function φ on C.

Before launching into the proof, a few words motivating the proof are appropriate. Suppose a spectral measure E defined on the Borel subsets of C is given and let $N = \int z   d E ( z )$ . It is not difficult to see that if $0 \leqslant a \leqslant b < \infty$ and $\Delta$ is the annulus $\left\{ z : a \leqslant |z| \leqslant b \right\}$ then $\mathcal { H } _ { \Delta } = E ( \Delta ) \mathcal { H } = \{ h \in \mathrm { d o m } \; N \}$ $\mathbf { \mathit { h } } \in \mathbf { d o m } \; N ^ { \mathbf { \mathit { n } } }$ for all n and $a^{n}\left\|h\right\|\leqslant\left\|N^{n}h\right\|\leqslant b^{n}\left\|h\right\|.\mathcal{H}_{\Delta}$ is a closed subspace of $\mathcal { H }$ that reduces N and $N | \mathcal { H } _ { \Delta }$ is bounded. The idea behind the proof is to write C as the disjoint union of annuli $\{ \Delta _ { j } \}$ such that for each $\Delta _ { j }$ there is a reducing subspace $\mathcal { H } _ { \Delta _ { j } }$ for N with $N _ { j }   \equiv   N | \mathcal { H } _ { \Delta _ { j } }$ bounded, and, moreover, such that $\mathcal { H } = \oplus _ { j } \mathcal { H } _ { \Delta _ { j } } .$ Once this is done the Spectral Theorem for bounded normal operators can be applied to each $N _ { j }$ and direct sums of these can be formed to obtain the spectral measure for N.

So we would like to show that for the annulus $\{ z : a \leqslant | z | \leqslant b \}$ , {h∈dom N: h∈dom $N ^ { n }$ for all n and $a^{n}\left \| h \right \| \leqslant \left \| N^{n}h \right \| \leqslant b^{n}\left \| h \right \|$ is a reducing subspace for N. To facilitate this, we will use the operator $\vec { B } = ( 1 + N ^ { * } N ) ^ { - 1 }$ which is a positive contraction (4.2). To understand what is done below note that $\overline { { z } }   \mapsto   ( 1 + | z | ^ { 2 } ) ^ { - 1 }$ maps C onto (0,1] and $a \leqslant |z| \leqslant b$ if and only if $(1 + a^{2})^{-1} \geqslant (1 + |z|^{2})^{-1} \geqslant (1 + b^{2})^{-1}$

4.12. Lemma. If N is a normal operator, $B   =   ( 1 + N ^ { * } N ) ^ { -   1 }$ , and $C =$ $N ( 1 + N ^ { * } N ) ^ { - 1 }$ , then $BC = CB$ and $( 1 + N ^ { * } N ) ^ { - 1 } N \subseteq C .$

ProoF. From (4.2), B and C are contractions and $B   \geqslant   0 .$ It will first be shown that $( 1 + N ^ { * } N ) ^ { - 1 } N \subseteq C ;$ that is, $B N \subseteq N B .$ If f ∈dom BN, then $f { \in } \mathbf { d o m }   N .$ Let g∈dom $N ^ { * } N$ such that $f   =   ( 1 + N ^ { * } N ) g$ Then $N ^ { * } N g \in \mathrm { d o m } \; N ;$ hence $N g   \in   \mathrm { d o m } \; N N ^ { * } = \mathrm { d o m } \; N ^ { * } N$ Thus $N f = N g + N N ^ { * } N g = ( 1 + N ^ { * } N ) N g$ Therefore $B N f = B ( 1 + N ^ { * } N ) N g = N g$ But $N B f = N g ,$ so $B N = N B$ on dom N. Thus $B N \subseteq N B .$

If $h \in \mathcal { H }$ let $f { \in } \operatorname { \mathbf { d o m } } N ^ { * } N$ such that $h   =   ( 1 + N ^ { * } N ) f$ So $B C h = B N B h =$ $B N f = N B f = N B B h = C B h$ Hence $BC = CB.$

4.13. Lemma. With the same notation as in Lemma 4.12, if $B = \int t   d P ( t )$ is its spectral representation, $1 > \delta > 0 ,$ and ∆ is a Borel subset $\dot { o f } [ \delta , 1 ]$ , then $\mathcal { H } _ { \Delta } = P ( \Delta ) \mathcal { H } \subseteq$ dom $N , \mathcal { H } _ { \pm }$ is invariant for both N and $N ^ { * }$ , and $N | \mathcal { H } _ { \Delta }$ is a bounded normal operator with $\| N | \mathcal { H } _ { \Delta } \| \leqslant \left[ ( 1 - \delta ) / \delta \right] ^ { 1 / 2 }$

PROOF. If $h \in \mathcal { H } _ { \Delta } ,$ then because $P ( \Delta ) = \chi _ { \Delta } ( B ) , \quad \| B h \| ^ { 2 } = \langle B ^ { 2 } P ( \Delta ) h , h \rangle =$ $\int _ { \Delta } t ^ { 2 } d P _ { h , h } \geqslant \delta ^ { 2 } \left\| h \right\| ^ { 2 }$ . So $B | \mathcal { H } _ { \Delta }$ is invertible and there is a g in $\mathcal { H } _ { \pmb { \Delta } }$ such that $h = B g .$ But ran $B = \mathrm{dom}(1 + N^* N) \subseteq \mathrm{dom} N$ Hence hedom $N;$ that is, $\mathcal { H } _ { \Delta } \subseteq \mathrm { d o m }   N .$

Let $h \in \mathcal { H } _ { \Delta }$ and again let $g \in \mathcal { H } _ { \Delta }$ such that $h = B g$ Hence $Nh = NBg = Cg$ By Lemma 4.12, $BC = CB;$ so by (IX.2.2), $P(\Delta)C = CP(\Delta)$ . Since $g \in \mathcal { H } _ { \Delta } ,$ $Nh = Cg \in \mathcal{H}_{\Delta}$ . Note that if $M = N ^ { * }$ and $B _ { 1 } = ( 1 + M ^ { * } M ) ^ { - 1 }$ , then $B _ { 1 } = B .$ From the preceding argument $N ^ { * } \mathcal { H } _ { \Delta } = M \mathcal { H } _ { \Delta } \subseteq \mathcal { H } _ { \Delta }$ . It easily follows that $N | \mathcal { H } _ { \Delta }$ is normal.

Finally, if $h \in \mathcal { H } _ { \Delta }$ , then

$$
\begin{align*}\|   N h   \|^2 &= \langle   N^* N h, h   \rangle \\&= \langle   [ (N^* N + 1) - 1 ] h, h   \rangle \\&= \int_{\delta}^{1} (t^{-1} - 1) d P_{h, h}(t) \leqslant \|   h   \|^2 (1 - \delta) / \delta.\end{align*}
$$

Hence $\| N | \mathcal { H } _ { \Delta } \| \leqslant \left[ ( 1 - \delta ) / \delta \right] ^ { 1 / 2 }$

PROOF OF THE SPECTRAL THEOREM. Let $B   =   ( 1 + N ^ { * } N ) ^ { - 1 }$ and $C = N ( 1 +$ $N ^ { * } N ) ^ { - 1 }$ as in Lemma 4.12. Let $B = \int_{0}^{1} t   d P(t)$ be the spectral decomposition of B and put $P _ { n } = P ( 1 / ( n + 1 ) , 1 / n ]$ for $n \geqslant 1$ . Since ker $B = (0) = P(\{0\}) \mathcal{H}$ $\textstyle \sum _ { n = 1 } ^ { \infty } P _ { n } = 1$ . Let $\mathcal { H } _ { n } = P _ { n } \mathcal { H }$ . By Lemma 4.13, $\mathcal { H } _ { n } \subseteq$ dom $N , \mathcal { H } _ { n }$ reduces N, and $N _ { n } \equiv N | \mathcal { H } _ { n }$ is bounded normal operator with $\| N _ { n } \| \leqslant n ^ { 1 / 2 }$ . Also, it $\mathbf { \nabla } ^ { \dagger } \mathbf { h } \in \mathcal { H } _ { n } ,$ $( 1 + N _ { n } ^ { * } N _ { n } ) B h = B ( 1 + N _ { n } ^ { * } N _ { n } ) h = h ;$ that is,

$$
B | \mathcal { H } _ { n } = ( 1 + N _ { n } ^ { * } N _ { n } ) ^ { - 1 } .
$$

Thus if $\lambda \in \sigma ( N _ { n } ) , \quad ( 1 + | \lambda | ^ { 2 } ) ^ { - 1 } \in \sigma ( B | \mathcal { H } _ { n } ) \subseteq [ 1 / ( n + 1 ) , 1 / n ]$ Thus $\sigma ( N _ { n } ) \subseteq$ $\left\{ z \in \mathbb { C } : ( n - 1 ) ^ { 1 / 2 } \leqslant | z | \leqslant n ^ { 1 / 2 } \right\} \equiv \Delta _ { n }$ Let $N _ { n } = \int z d E _ { n } ( z )$ be the spectral decomposition of $N _ { n }$ . For any Borel subset $\pmb { \Delta }$ of $\mathbf { C } _ { s }$ let $E ( \Delta )$ be defined by

## 4.14

$$
E ( \Delta ) = \sum _ { n = 1 } ^ { \infty } E _ { n } ( \Delta \cap \Delta _ { n } ) .
$$

Note that $E _ { n } ( \Delta \cap \Delta _ { n } )$ is a projection with range in $\mathcal { H } _ { n }$ Since $\mathcal { H } _ { n } \bot \mathcal { H } _ { m }$ for $n \neq m ,$ (4.14) defines a projection in $\mathcal { B } ( \mathcal { H } )$ .(Technically $E ( \Delta )$ should be defined by $E ( \Delta ) = \sum _ { n = 1 } ^ { \infty } E _ { n } ( \Delta \cap \Delta _ { n } ) P _ { n }$ . But this technicality does not add anything to understanding.)

Now to show that E is a spectral measure. Clearly $E ( \mathbf { C } ) = 1$ and $E ( \square ) = 0$ If $\Lambda _ { 1 }$ and $\Lambda _ { 2 }$ are Borel subsets of $\mathbf { C } _ { \mathrm { s } }$ then

$$
\begin{align*}E(\Lambda_1 \cap \Lambda_2) = & \sum_{n=1}^{\infty} E_n(\Lambda_1 \cap \Lambda_2 \cap \Lambda_n) \\= & \sum_{n=1}^{\infty} E_n(\Lambda_1 \cap \Lambda_n) E_n(\Lambda_2 \cap \Lambda_n).\end{align*}
$$

Again, the fact that the spaces $\{ \mathcal { H } _ { n } \}$ are pairwise orthogonal implies

$$
\begin{aligned}E(\Lambda_{1} \cap \Lambda_{2}) &= \left( \sum_{n = 1}^{\infty} E_{n}(\Lambda_{1} \cap \Lambda_{n}) \right) \left( \sum_{n = 1}^{\infty} E_{n}(\Lambda_{2} \cap \Lambda_{n}) \right) \\&= E(\Lambda_{1})E(\Lambda_{2}).\end{aligned}
$$

If $h \in \mathcal { H }$ , then $\begin{array} { r } { \langle E ( \Delta ) h , h \rangle = \sum _ { n = 1 } ^ { \infty } \langle E _ { n } ( \Delta \cap \Delta _ { n } ) h , h \rangle } \end{array}$ . So if $\{ \Lambda _ { j } \} _ { j = 1 } ^ { \infty }$ are pairwise disjoint Borel sets,

$$
\begin{align*}\left\langle E\Bigg( \bigcup_{j=1}^{\infty} \Lambda_j \Bigg) h, h \right\rangle &= \sum_{n=1}^{\infty} \left\langle E_n \Bigg( \Bigg( \bigcup_{j=1}^{\infty} \Lambda_j \Bigg) \cap \Delta_n \Bigg) h, h \right\rangle \\&= \sum_{n=1}^{\infty} \sum_{j=1}^{\infty} \left\langle E_n(\Lambda_j \cap \Delta_n) h, h \right\rangle.\end{align*}
$$

Since each term in this double summation is non-negative, the order of summation can be reversed. Thus

$$
\begin{align*}\left\langle E\Biggl( \bigcup_{j=1}^{\infty} \Lambda_j \Biggr) h, h \right\rangle &= \sum_{j=1}^{\infty} \sum_{n=1}^{\infty} \left\langle E_n(\Lambda_j \cap \Delta_n) h, h \right\rangle \\&= \sum_{j=1}^{\infty} \left\langle E(\Lambda_j) h, h \right\rangle.\end{align*}
$$

So $E(\bigcup_{j = 1}^{\infty} \Lambda_{j}) = \sum_{j = 1}^{\infty} E(\Lambda_{j});$ therefore E is a spectral measure.

Let $\dot { M } = \int z   d E ( z )$ be defined as in Theorem 4.7. Thus $\mathcal { H } _ { n } \subseteq \operatorname { d o m } M$ and by the Spectral Theorem for bounded operators, $M h = N _ { n } h = N h$ if $h \in \mathcal { H } _ { n }$ If h is any vector in dom M, $h = \sum _ { 1 } ^ { \infty } h _ { n } , h _ { n } \in \mathcal { H } _ { n }$ , and $\textstyle \sum _ { 1 } ^ { \infty } \| N h _ { n } \| ^ { 2 } < \infty$ . Because N is closed, hedom N and $N h = M h$ Thus $M \subseteq N$ . To prove the other inclusion, note that M is a closed operator by Lemma 4.4. Thus, by (4.2.e), it suffices to show that {h⊕ Nh: h∈dom $N ^ { \star } N \} \subseteq \operatorname { g r a } M$ . If h∈dom $N ^ { * } N .$ there is a vector $g$ such that $h = B g$ Then $P_{n}Nh = P_{n}NB = P_{n}Cg = CP_{n}g$ $( \mathbf{W} \mathbf{h} \mathbf{y} ? ) = N P_{n} \mathbf{h}$ If $h _ { n } = P _ { n } h ,$ then $\begin{array} { r } { \sum \| N h _ { n } \| ^ { 2 } = \sum \| P _ { n } N h \| ^ { 2 } = \| N h \| ^ { 2 } < \infty } \end{array}$ Therefore hedom M and so, by the preceding argument $N h = M h .$ That is, h⊕ Nh∈gra M. This proves (a).

## 4.15. Claim.

$$
\sigma ( N ) = \mathrm { c l } \left[ \bigcup _ { n = 1 } ^ { \infty } \sigma ( N _ { n } ) \right] .
$$

It is left to the reader to show that $\bigcup_{n = 1}^{\infty} \sigma(N_n) \subseteq \sigma(N)$ Since $\sigma ( N )$ is closed, this proves half of (4.15). If $\lambda \notin \mathrm{cl}[\bigcup_{n = 1}^{\infty} \sigma(N_n)]$ , then there is a $\delta   >   0$ such that $| \lambda - z | \geqslant \delta$ for all z in $\bigcup_{n = 1}^{\infty} \sigma(N_{n}).$ Thus $( N _ { n } - \lambda ) ^ { - 1 }$ exists and $\| (N_n - \lambda)^{-1} \| \leqslant \delta^{-1}$ for all n. Thus $A = \oplus _ { n = 1 } ^ { \infty } ( N _ { n } - \lambda ) ^ { - 1 }$ is a bounded operator. It follows that $A = ( N - \lambda ) ^ { - 1 }$ , so $\lambda \sharp \sigma ( N )$

By (4.15) if $\Delta \cap \sigma(N) = \square, \Delta \cap \sigma(N_n) = \square$ for all n. Thus $E _ { n } ( \Delta ) = 0$ for all n. Hence $E ( \Delta ) = 0$ and (b) holds.

If U is open and $U \cap \sigma ( N ) \neq \square$ , then (4.15) implies $U \cap \sigma(N_n) \neq \square$ for some n. Since $E _ { n } ( U ) \neq 0 , E ( U ) \neq 0$ and (c) is true.

Now let $A   \in   \mathcal { B } ( \mathcal { H } )$ such that $A N \subseteq N A$ and $A N ^ { * } \subseteq N ^ { * } A$ . Thus $A ( 1 + N ^ { * } N )   \subseteq   ( 1 + N ^ { * } N ) A$ . It follows that $AB = BA$ . By the Spectral Theorem for bounded operators, A commutes with the spectral projections of B. In particular, each $\mathcal { H } _ { n }$ reduces A and if $A _ { n } \equiv A | \mathcal { H } _ { n }$ , then $A _ { n } N _ { n } = N _ { n } A _ { n } .$ Hence $A _ { n } E _ { n } ( \Delta ) = E _ { n } ( \Delta ) A _ { n }$ , for every Borel set $\Delta$ contained in $\Delta _ { n }$ . It follows that $AE(\Delta) = E(\Delta)A$ for every Borel set ∆. The remaining details of the proof of (d) are left to the reader.

The Fuglede-Putnam Theorem holds for unbounded normal operators (Exercise 8), so that the hypothesis in part (d) of the Spectral Theorem can be weakened to $A N \subseteq N A$

4.16. Definition. If N is a normal operator on $\mathcal { H }$ , then a vector $e _ { 0 }$ is a star-cyclic vector for N if for all non-negative integers k and $l , e _ { 0 }$ edom $( N ^ { * ^ { k } } N ^ { l } )$ and $\dot { \mathcal { H } } = \nabla \left\{ N ^ { * } { } ^ { k } N ^ { l } e _ { 0 } : k , l \geqslant 0 \right\}$

4.17. Example. Let $\mu$ be a finite measure on C such that every polynomial in z and $\bar { z }$ belongs to $L ^ { 2 } ( \mu )$ and the collection of such polynomials is dense in $L ^ { 2 } ( \mu )$ . Let $\mathcal { D } _ { \mu } = \{ f \in L ^ { 2 } ( \mu ) : z f \in L ^ { 2 } ( \mu ) \}$ and define $N _ { \mu } f = z f$ for f in $\mathcal { D } _ { \mu }$ . Then $N _ { \mu }$ is a normal operator and 1 is a star-cyclic vector for $N _ { \mu } .$

Note that $\mathrm { d } \mu ( z ) = e ^ { - | z | } d \mathrm { A r e a } ( z )$ is a measure satisfying the conditions of (4.17).

4.18. Theorem. If N is a normal operator on $\mathcal { H }$ with a star-cyclic vector $e _ { 0 } ,$ then there is a finite measure µ on C such that every polynomial in z and ž belongs to $L ^ { 2 } ( \mu )$ and there is an isomorphism W: ${ \mathcal { H } } \to L ^ { 2 } ( \mu )$ such that $W e _ { 0 } = 1$ and $W N W ^ { - 1 } = N _ { \mu }$

The proof of Theorem 4.18 can be accomplished by using the Spectral Theorem to write N as the direct sum (in the sense of Lemma $4 . 4 )$ of bounded normal operators $N _ { n }$ on $\mathcal { H } _ { n }$ with spectral measures that are pairwise mutually singular and such that each $N _ { n }$ has $e _ { n } ,$ the projection of $e _ { 0 }$ onto $\mathcal { H } _ { n } ,$ as a \*-cyclic vector. If $\mu _ { n } = E _ { e _ { n } , e _ { n } } ,$ then (IX.3.4) implies that there is an isomorphism $W_{n}:\mathcal{H}_{n}\to L^{2}(\mu_{n})$ such that $W _ { n } N _ { n } W _ { n } ^ { - 1 } = N _ { \mu _ { n } }$ . If $\begin{array} { r } { W = \oplus _ { 1 } ^ { \infty } W _ { n } , } \end{array}$ then W is an isomorphism of $\mathcal { H }$ onto $\oplus _ { 1 } ^ { \infty } L ^ { 2 } ( \mu _ { n } )$ . But the fact that the measures $\mu _ { n }$ are pairwise mutually singular implies that $\oplus _ { 1 } ^ { \infty } L ^ { 2 } ( \mu _ { n } ) = L ^ { 2 } ( \mu )$ , where $\begin{array} { r } { \mu = \sum _ { n = 1 } ^ { \infty } \mu _ { n } = E _ { e _ { 0 } , e _ { 0 } } } \end{array}$ . Clearly $W N W ^ { - 1 } = N _ { \mu }$

4.19. Theorem. If N is a normal operator on the separable Hilbert space $\mathcal { H }$ then there is a σ-finite measure space $( X , \Omega , \mu )$ and an Ω-measurable function $\phi$ such that N is unitarily equivalent to $M _ { \phi }$ on $L ^ { 2 } ( \mu )$

The proof of Theorem 4.19 is only sketched. Write N as the (unbounded) direct sum of bounded normal operators $\{ N _ { n } \}$ . By Theorem IX.4.6, there is a σ-finite measure space $( X _ { n } , \Omega _ { n } , \mu _ { n } )$ and a bounded $\Omega _ { n }$ -measurable function $\phi _ { n }$ such that $N _ { n } \cong M _ { \phi _ { n } }$ Let X = the disjoint union of $\left\{ X _ { n } \right\}$ and let $\mathbf { \Omega } = \{ \mathbf { \Delta } \subseteq X \colon \mathbf { \Delta } \cap X _ { n } \in \mathbf { \Omega } _ { n }$ for every $n \}$ . If $\Delta { \in } \Omega ,$ let $\begin{array} { r } { \mu ( \Delta ) = \sum _ { 1 } ^ { \infty } \mu _ { n } ( \Delta \cap X _ { n } ) } \end{array}$ Let $\phi \colon X   \to   \mathbb { C }$ be defined by $\phi ( x ) = \phi _ { n } ( x )$ if $x   \in   X _ { \pmb { n } }$ . Then $\phi$ is Ω-measurable and $N \cong M _ { \phi }$ on $L ^ { 2 } ( X , \Omega , \mu )$

## EXERCISES

1. Prove Theorem 4.10.

2. Show that if A is a symmetric operator that is normal, then A is self-adjoint.

3. With the notation of Theorem 4.7, show that for h in $\mathcal { D } _ { \phi } ,   \| ( \int \phi   d E ) h \| ^ { 2 } = \int | \phi | ^ { 2 }   d E _ { h , h } .$

4. Using the notation of Theorem 4.10, what is $\sigma ( \int \phi   d E ) ?$

5. If $\Delta _ { n }$ and $E _ { n }$ are as in the proof of the Spectral Theorem, show that $E_{n}(\Delta_{n + 1}) =$ $E_{n}(\Delta_{n - 1}) = 0$

6. Use the Spectral Theorem to show that if $0 < a \leqslant b < \infty, \Delta = \{ z \in \mathbb{C}: a \leqslant |z| \leqslant b \}$ and $N = \int z   d E ( z )$ is the spectral decomposition of the normal operator N, then $E ( \Delta ) \mathcal { H } = \left\{ h \in \mathrm { d o m } N : a ^ { n } \| h \| \leqslant \| N ^ { n } h \| \leqslant b ^ { n } \| h \| \right\}$ for all $n \geqslant 1 \}$

7. State and prove a polar decomposition for operators in $\mathcal { C } ( \mathcal { H } , \mathcal { H } )$

8. If A is self-adjoint, prove that exp(iA) is unitary.

9. (Fuglede-Putnam Theorem.) If N, M are normal operators and A is a bounded operator such that $A N \subseteq M A .$ , then $A N ^ { * } \subseteq M ^ { * } A .$

10. Prove Theorem 4.18.

11. If $\mu _ { 1 } , \mu _ { 2 }$ are finite measures on C and $N _ { \mu _ { 1 } } , N _ { \mu _ { 2 } }$ are defined as in Example 4.17, show that $N _ { \mu _ { 1 } } \cong N _ { \mu _ { 2 } } \mathrm { i f f } \left[ \mu _ { 1 } \right] = \left[ \mu _ { 2 } \right]$

12. Fill in the details of the proof of Theorem 4.19.

## §5. Stone's Theorem

If A is a self-adjoint operator on $\mathcal { H } ,$ then exp(iA) is a unitary operator (Exercise 4.7). Hence $U ( t ) = \exp ( i t A )$ is unitary for all t in R. The purpose of this section is not to investigate the individual operators exp(itA), but rather the entire collection of operators $\{ \exp ( i t A ) : t \in \mathbb { R } \}$ . In fact, as the first theorem shows, U: R→unitaries on $\mathcal { H }$ is a group homomorphism with certain properties. Stone's Theorem provides a converse to this; every such homomorphism arises in this way.

5.1. Theorem. If A is self-adjoint and $U ( t ) = \exp ( i t A )$ for t in R, then

(a) U(t) is unitary;

(b) $U ( s + t ) = U ( s ) U ( t ) { \it ~ f o r ~ a l l ~ } s { \it ~ i n ~ } \mathbb { R } ;$

(c) if $h \in \mathcal { H }$ , then $\mathrm{lim}_{s \to t} U(s)h = U(t)h;$

(d) if h∈dom A, then

5.2

$$
\lim _ { t \rightarrow 0 } \frac { 1 } { t } \left[ U ( t ) h - h \right] = i A h ;
$$

(e) if $h \in \mathcal { H }$ and lim $t ^ { - 1 } [ U ( t ) h - h ]$ exists, then h∈dom A. Consequently, dom A is invariant under each $U ( t ) .$

ProoF. As was mentioned, part (a) is an exercise. Since $\exp(itx)\exp(isx)=$ $\exp ( i ( s + t ) x )$ for all x in R, (b) is a consequence of the functional calculus for normal operators [(4.10) and (4.11)]. Also note that $U ( 0 ) U ( t ) = U ( t ) ,$ so that $U ( 0 ) = 1$

(c) If $h \in \mathcal { H } _ { j }$ then $\| U ( t ) h - U ( s ) h \| = \| U ( t - s + s ) h - U ( s ) h \| = [ \mathrm { b y }$ (b)] $\|   U ( s ) [ U ( t - s ) h - h ]   \| = \|   U ( t - s ) h - h   \|$ since $U ( s )$ is unitary. Thus (c) will be shown if it is proved that $\| U ( t ) h - h \| \to 0$ as $t   \rightarrow   0 ,$ If $A = \int _ { - \infty } ^ { \infty } x   d E ( x )$ is the spectral decomposition of A, then

$$
\| U ( t ) h - h \| ^ { 2 } = \int _ { - \infty } ^ { \infty } | e ^ { i t x } - 1 | ^ { 2 }   d E _ { h , h } ( x ) .
$$

Now $E _ { h , h }$ is a finite measure on $\mathbf { R } ;$ for each x in $\mathbb { R } ,   | e ^ { i t x } - 1 | ^ { 2 } \rightarrow 0$ as $t   \rightarrow   0 ;$ and $| e ^ { i t x } - 1 | ^ { 2 } \leqslant 4.$ So the Lebesgue Dominated Convergence Theorem implies that $U ( t ) h   \rightarrow   h$ as $t   \rightarrow   0 .$

(d) Note that $t ^ { - 1 } [ U ( t ) - 1 ] - i A = f _ { t } ( A )$ , where $f_{t}(x)=t^{-1}\left[\exp(itx)-1\right]-$ ix. So if hedom A,

$$
\begin{align*}\left\| \frac{1}{t} \left[ U(t) h - h \right] - i A h \right\|^2 &= \| f_t(A) h \|^2 \\&= \int_{-\infty}^{\infty} \left| \frac{e^{i t x} - 1}{t} - i x \right|^2 d E_{h,h}(x).\end{align*}
$$

As $t \to 0 ,   t ^ { - 1 } \left[ e ^ { i t x } - 1 \right] - i x \to 0$ for all x in IR. Also, $| e ^ { i s } - 1 | \leqslant | s |$ for all real numbers $s \left( \mathbf { W } \mathbf { h } \mathbf { y } ? \right)$ hence $| f _ { t } ( x ) | \leqslant | t | ^ { - 1 } | e ^ { i t x } - 1 | + | x | \leqslant 2 | x | .$ But $| x | { \in } L ^ { 2 } ( E _ { h , h } )$ by Theorem $4 . 7 ( a )$ . So again the Lebesgue Dominated Convergence Theorem implies that (5.2) is true.

(e) Let $\mathcal { D } = \left\{ h \in \mathcal { H } : \operatorname { l i m } _ { t \rightarrow 0 } t ^ { - 1 } \left[ U ( t ) h - h \right] \right\}$ exists in $\mathcal { H } \}$ . For h in $\mathcal { D } ,$ let Bh be defined by

$$
B h = - i \lim _ { t \rightarrow 0 } \frac { U ( t ) h - h } { t } .
$$

It is easy to see that $\mathcal { D }$ is a linear manifold in $\mathcal { H }$ and B is linear on $\mathcal { D }$ Also, by (d), $B \supseteq A$ so that B is densely defined. Moreover, if $h , g \in \mathcal { D }$ , then

$$
\langle B h , g \rangle = - i \operatorname* { l i m } _ { t \to 0 } \left\langle \frac { U ( t ) h - h } { t } , g \right\rangle .
$$

By (b) and the fact that each $U ( t )$ is unitary, it follows that $U(t)^{*} = U(t)^{-1}$

U(− t). Hence

$$
\begin{align*}\langle \boldsymbol{B} \boldsymbol{h}, \boldsymbol{g} \rangle &= - i \lim_{t \to 0} \left\langle \boldsymbol{h}, \frac{U(-t) \boldsymbol{g} - \boldsymbol{g}}{t} \right\rangle \\&= \lim_{t \to 0} \left\langle \boldsymbol{h}, - i \left[ \frac{U(-t) \boldsymbol{g} - \boldsymbol{g}}{-t} \right] \right\rangle \\&= \langle \boldsymbol{h}, \boldsymbol{B} \boldsymbol{g} \rangle.\end{align*}
$$

Hence B is a symmetric extension of A. Since self-adjoint operators are maximal symmetric operators (2.11), $B = A$ and $\mathcal { D } = \dim A .$

The following definition is inspired by the preceding theorem.

5.3. Definition. A strongly continuous one parameter unitary group is a function $U : \mathbb { R } \to { \mathcal { B } } ( { \mathcal { H } } )$ such that for all s and t in R: (a) U(t) is a unitary operator; (b) $U ( s + t ) = U ( s ) U ( t ) ;$ (c) if $h \in \mathcal { H }$ and $t _ { 0 } { \in } \mathbb { R }$ , then $U ( t ) h \to U ( t _ { 0 } ) h$ as $t   \rightarrow   t _ { 0 }$

Note that by Theorem 5.1, if A is self-adjoint, then $U ( t ) = \exp ( i t A )$ defines a strongly continuous one parameter unitary group.

Also, $U ( 0 )   =   1$ and $U ( - t ) = U ( t ) ^ { - 1 }$ , so that $\{ U ( t ) : t { \in } \mathbb { R } \}$ is indeed a group. Property (c) also implies that $U \colon \mathbb { R }   \to   ( { \mathcal { B } } ( { \mathcal { H } } ) , \mathrm { S O T } )$ is continuous. By Exercise 1, if U is only assumed to be WOT-continuous, then U is SOT-continuous. However, this condition can be relaxed even further as the following result of von Neumann [1932] shows.

5.4. Theorem. If H is separable, U: $\mathbb { R } \rightarrow \mathcal { B } ( \mathcal { H } )$ satisfies conditions (a) and (b) of Definition 5.3, and if for all h, g in H the function $t { \mapsto } \langle U ( t ) h , g \rangle$ is Lebesgue measurable, then U is a strongly continuous one-parameter unitary group.

PROOF. If $0 < a < \infty$ and $h , g \in \mathcal { H }$ , then $t { \mapsto } \langle U ( t ) h , g \rangle$ is a bounded measurable function on $[ 0 , a ]$ and hence

$$
\int _ { 0 } ^ { a } \left| \left\langle U ( t ) h , g \right\rangle \right| d t \leqslant a \left\| h \right\| \left\| g \right\| .
$$

Thus

$$
h \mapsto \int _ { 0 } ^ { a } \langle U ( t ) h , g \rangle   d t
$$

is a bounded linear function on $\mathcal { H } .$ Therefore there is a $g _ { a }$ in $\mathcal { H }$ such that

$$
\langle h , g _ { a } \rangle = \int _ { 0 } ^ { a } \langle U ( t ) h , g \rangle d t\tag{5.5}
$$

and $\| g _ { a } \| \leqslant a \| g \|$

Claim. $\{ g _ { a } ;   g \in \mathcal { H } ,   a > 0 \}$ is total in $\mathcal { H }$