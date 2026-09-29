## Step D: Recovery of a classical solution.

Assume that the weak solution $u   \in   H _ { 0 } ^ { 1 } ( \Omega )$ of (31) belongs to $C ^ { 2 } ( \overline { { \Omega } } )$ , and assume that  is of class $C ^ { 1 }$ . Then $u   =   0$ on  (by Theorem 9.17). On the other hand, we have

$$
\int _ { \Omega } ( - \Delta u + u ) v = \int _ { \Omega } f v \quad \forall v \in C _ { c } ^ { 1 } ( \Omega ) .
$$

and thus $- \Delta u   +   u   =   f$ a.e. on  (by Corollary 4.24). In fact, $- \Delta u   +   u   =   f$ everywhere on $\Omega ,$ since $u \in C ^ { 2 } ( \Omega )$ ; thus u is a classical solution.

We describe now some other examples. In each case it is essential to specify precisely the function space and the appropriate weak formulation.

Example 2 (inhomogeneous Dirichlet condition). Let $\Omega \subset \mathbb { R } ^ { N }$ be a bounded open set. We look for a function $u : \overline { { \Omega } } \to \mathbb { R }$ satisfying

$$
\left\{ \begin{aligned} - \Delta u + u &= f & &  in   \Omega, \\ u &= g & &  on   \Gamma, \end{aligned} \right.\tag{33}
$$

where $f$ is given on  and g is given on . Suppose that there exists a function $\tilde { g } \in H ^ { 1 } ( \Omega ) \cap C ( \overline { { \Omega } } )$ such tha $\tilde { \mathfrak { t } ^ { 2 2 } } \; \tilde { g } = g$ on $\Gamma$ and consider the set

$$
K = \{ v \in H ^ { 1 } ( \Omega ) ; v - \tilde { g } \in H _ { 0 } ^ { 1 } ( \Omega ) \} .
$$

It follows from Theorem 9.17 that K is independent of the choice of $\tilde { g }$ and depends only on g. K is a nonempty closed convex set in $H ^ { 1 } ( \Omega )$

**Definition.** A classical solution of (33) is a function $u \in C ^ { 2 } ( \overline { { \Omega } } )$ satisfying (33). A weak solution of (33) is a function $u \in K$ satisfying

$$
\int _ { \Omega } ( \nabla u \cdot \nabla v + u v ) = \int _ { \Omega } f v \quad \forall v \in H _ { 0 } ^ { 1 } ( \Omega ) .\tag{34}
$$

As above, any classical solution is a weak solution.

• **Proposition 9.22.** Given any $f \; \in \; L ^ { 2 } ( \Omega )$ , there exists a unique weak solution $u \in K$ of (33). Furthermore, u is obtained by

$$
\operatorname* { m i n } _ { v \in K } \left\{ \frac { 1 } { 2 } \int _ { \Omega } ( | \nabla v | ^ { 2 } + v ^ { 2 } ) - \int _ { \Omega } f v \right\} .
$$

Proof. We claim that $u \in K$ is a weak solution of (33) if and only if we have

$$
\int _ { \Omega } \nabla u \cdot ( \nabla v - \nabla u ) + \int _ { \Omega } u ( v - u ) \geq \int _ { \Omega } f ( v - u ) \quad \forall v \in K .\tag{35}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">d g ∈ C ().</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">g˜  C  .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">˜  H1  , i. .,  H1/2  .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">22 This assumption is satisfied, for example, if  is of class C an 1 If  is regular enough it is not necessary to suppose that ∈ ( ) Applying the theory of traces (see the comments at the end of this chapter), it suffices to know that g ∈ ( ) e g ∈ ( )</span></small>