such that $\rho _ { 1 } ( 1 ) = 1 ( 1 . 9 )$ . Thus it suffices to prove the proposition under the additional assumption that $\varkappa$ and $\mathcal { B }$ have identities and $\rho ( 1 )   = 1$

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