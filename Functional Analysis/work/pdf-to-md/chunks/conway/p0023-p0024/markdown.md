PROOF. If $f _ { 1 } \bot f _ { 2 }$ , then

$$
\| f _ { 1 } + f _ { 2 } \| ^ { 2 } = \langle f _ { 1 } + f _ { 2 } , f _ { 1 } + f _ { 2 } \rangle = \| f _ { 1 } \| ^ { 2 } + 2 \operatorname { R e } \langle f _ { 1 } , f _ { 2 } \rangle + \| f _ { 2 } \| ^ { 2 }
$$

by the polar identity. Since $f _ { 1 } \bot f _ { 2 } ,$ this implies the result for $n   =   2 .$ The remainder of the proof proceeds by induction and is left to the reader. ■

Note that ${ \mathrm { i f } } f \bot g ,$ thenf $丄  -g,$ so $\| f - g \| ^ { 2 } = \| f \| ^ { 2 } + \| g \| ^ { 2 }$ . The next result is an easy consequence of the Pythagorean Theorem if f and g are orthogonal, but this assumption is not needed for its conclusion.

2.3. Parallelogram Law. If $\mathcal { H }$ is a Hilbert space and f and $g \in \mathcal { H }$ , then

$$
\|   f + g   \| ^ { 2 } + \|   f - g   \| ^ { 2 } = 2 ( \|   f   \| ^ { 2 } + \|   g   \| ^ { 2 } ) .
$$

PROOF. For any f and $g$ in $\mathcal { H }$ the polar identity implies

$$
\begin{array} { r } { \| f + g \| ^ { 2 } = \| f \| ^ { 2 } + 2   \mathrm { R e }   \langle f , g \rangle + \| g \| ^ { 2 } , } \\ { \| f - g \| ^ { 2 } = \| f \| ^ { 2 } - 2   \mathrm { R e }   \langle f , g \rangle + \| g \| ^ { 2 } . } \end{array}
$$

Now add.

The next property of a Hilbert space is truly pivotal. But first we need a geometric concept valid for any vector space over $\mathbf { E }$

2.4. Definition. If ¿ is any vector space over F and $A \subseteq { \mathcal { X } }$ , then A is a convex set if for any x and y in A and $0 \leqslant t \leqslant 1,   tx + (1 - t)y \in A$

Note that $\left\{ t x + ( 1 - t ) y : 0 \leqslant t \leqslant 1 \right\}$ is the straight-line segment joining x and y. So a convex set is a set A such that if x and $y \in A$ , the entire line segment joining x and y is contained in A.

If X is a vector space, then any linear subspace in $\mathcal { X }$ is a convex set. A singleton set is convex. The intersection of any collection of convex sets is convex. If $\mathcal { H }$ is a Hilbert space, then every open ball $B(f;r)=\{g\in\mathcal{H}\}$二 $\left\| f - g \right\| < r \big \}$ is convex, as is every closed ball.

2.5. Theorem. If H is a Hilbert space, K is a closed convex nonempty subset of $\mathcal { H }$ , and $h \in \mathcal { H }$ , then there is a unique point $k _ { 0 }$ in K such that

$$
\| \boldsymbol{h} - \boldsymbol{k}_0 \| = \mathrm{dist}(\boldsymbol{h}, \boldsymbol{K}) \equiv \inf \{ \| \boldsymbol{h} - \boldsymbol{k} \| : \boldsymbol{k} \in \boldsymbol{K} \}.
$$

PROOF. By considering $K - h \equiv \{ k - h { \mathrm { : ~ } } k { \in } K \}$ instead of K, it suffices to assume that $h = 0.   (  Verify ! )$ So we want to show that there is a unique vector $k _ { 0 }$ in K such that

$$
\| \boldsymbol { k } _ { 0 } \| = \mathrm { d i s t } ( 0 , \boldsymbol { K } ) \equiv \inf \{ \| \boldsymbol { k } \| : \boldsymbol { k } \in \boldsymbol { K } \}.
$$

Let $d = \mathrm{dist}(0, K)$ . By definition, there is a sequence $\{ k _ { n } \}$ in K such that一 $k _ { n } \rVert \to d .$ Now the Parallelogram Law implies that

$$
\left\| \frac{k_n - k_m}{2} \right\|^2 = \frac{1}{2} \left( \left\| k_n \right\|^2 + \left\| k_m \right\|^2 \right) - \left\| \frac{k_n + k_m}{2} \right\|^2.
$$

## §2. Orthogonality

Since K is convex, $\scriptstyle { \frac { 1 } { 2 } } ( k _ { n } + k _ { m } ) \in K$ . Hence, $\| \frac { 1 } { 2 } ( k _ { n } + k _ { m } ) \| ^ { 2 } \geqslant d ^ { 2 }$ . If $\varepsilon   >   0 ,$ choose N such that for $n \geqslant N, \left\| \hat{k}_n \right\|^2 < d^2 + \frac{1}{4} \varepsilon^2$ . By the equation above, $\mathrm{if} n, m \geqslant N$ , then

$$
\left\| \frac{k_n - k_m}{2} \right\|^2 < \frac{1}{2} \left( 2d^2 + \frac{1}{2} \varepsilon^2 \right) - d^2 = \frac{1}{4} \varepsilon^2.
$$

Thus, $\| k _ { n } - k _ { m } \| < \varepsilon$ for $n , m \geqslant N$ and $\left\{ k _ { n } \right\}$ is a Cauchy sequence. Since $\mathcal { H }$ is complete and K is closed, there is a $k _ { 0 }$ in K such that $\| k _ { n } - k _ { 0 } \|   \to   0$ Also for all $k _ { n } ,$ T

$$
\begin{aligned}d \leqslant \left\| \boldsymbol{k}_{0} \right\| &= \left\| \boldsymbol{k}_{0} - \boldsymbol{k}_{n} + \boldsymbol{k}_{n} \right\| \\& \leqslant \left\| \boldsymbol{k}_{0} - \boldsymbol{k}_{n} \right\| + \left\| \boldsymbol{k}_{n} \right\| \rightarrow \boldsymbol{d}.\end{aligned}
$$

Thus $\| k _ { 0 } \| = d .$

To prove that $k _ { 0 }$ is unique, suppose $h _ { 0 }   \in   K$ such that $\| \boldsymbol { h } _ { 0 } \| = d$ By convexity, $\scriptstyle { \frac { 1 } { 2 } } ( k _ { 0 } + h _ { 0 } ) \in K$ . Hence

$$
d \leqslant \| \frac{1}{2} (h_0 + k_0) \| \leqslant \frac{1}{2} (\| h_0 \| + \| k_0 \|) = d.
$$

So $\begin{array} { r } { \| \frac { 1 } { 2 } ( h _ { 0 } + k _ { 0 } ) \| = d . } \end{array}$ The Parallelogram Law implies

$$
d ^ { 2 } = \left\| \frac { h _ { 0 } + k _ { 0 } } { 2 } \right\| ^ { 2 } = d ^ { 2 } - \left\| \frac { h _ { 0 } - k _ { 0 } } { 2 } \right\| ^ { 2 } ;
$$

hence $h _ { 0 } = k _ { 0 }$

If the convex set in the preceding theorem is in fact a closed linear subspace of $\mathcal { H }$ , more can be said.

2.6. Theorem. If M is a closed linear subspace of $\mathcal { H } , h \in \mathcal { H }$ , and $f _ { 0 }$ is the unique element of M such that $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } )$ , then $\pmb { h } - f _ { 0 } \bot \mathcal { M }$ . Conversely, if $f _ { 0 } \in \mathcal { M }$ such that $\pmb { h } - f _ { 0 } \bot \mathcal { M } ,$ then $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } )$

PrOOF. Suppose $f _ { 0 } \in \mathcal { M }$ and $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } ) .$ If $f \in \mathcal { M } _ { 1 }$ then $f _ { 0 } + f \in \mathcal { M }$ and so $\| h - f_0 \|^2 \leqslant \| h - (f_0 + f) \|^2 = \| (h - f_0) - f \|^2 = \| h - f_0 \|^2$ $- 2 \operatorname { R e } \left\langle h - f _ { 0 } , f \right\rangle + \| f \| ^ { 2 }$ . Thus

$$
2 \operatorname{Re} \left\langle h - f_0, f \right\rangle \leqslant \| f \|^2
$$

for any f in M. Fix f in M and substitute $t e ^ { i \theta } f$ for f in the preceding inequality, where $\langle h - f _ { 0 } , f \rangle = r e ^ { i \theta } , r \geqslant 0$ .This yields $2 \mathrm{Re} \left\{ t e^{-i \theta} r e^{i \theta} \right\} \leqslant t^2 \| f \|^2$ , or $2 t r \leqslant t ^ { 2 } \left\| f \right\| { } ^ { 2 }$ Letting $t   \rightarrow   0 ,$ we see that $r = 0 ;$ that is, $\pmb { h } - f _ { 0 } \bot f .$

For the converse, suppose $f _ { 0 } \in \mathcal { M }$ such that $\pmb { h } - f _ { 0 } \bot \mathcal { M }$ . If $f \in \mathcal { M }$ , then $h - f _ { 0 } \bot f _ { 0 } - f$ so that

$$
\begin{aligned} \|   h - f   \| ^ { 2 } & = \|   ( h - f _ { 0 } ) + ( f _ { 0 } - f )   \| ^ { 2 } \\ & = \|   h - f _ { 0 }   \| ^ { 2 } + \|   f _ { 0 } - f   \| ^ { 2 } \\ & \geqslant \|   h - f _ { 0 }   \| ^ { 2 } . \end{aligned}
$$

Thus $\| h - f _ { 0 } \| = \mathrm { d i s t } ( h , \mathcal { M } )$