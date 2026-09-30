$x \in P$ such that $m \leq x$ , except for $x = m$ . Note that a maximal element of P need not be an upper bound for P.

We say that P is inductive if every totally ordered subset Q in P has an upper bound.

• **Lemma 1.1 (Zorn).** Every nonempty ordered set that is inductive has a maximal element.

Zorn’s lemma follows from the axiom of choice, but we shall not discuss its derivation here; see, e.g., J. Dugundji [1], N. Dunford–J. T. Schwartz [1] (Volume 1, Theorem 1.2.7), E. Hewitt–K. Stromberg [1], S. Lang [1], and A. Knapp [1].

Remark 1. Zorn’s lemma has many important applications in analysis. It is a basic tool in proving some seemingly innocent existence statements such as “every vector space has a basis” (see Exercise 1.5) and “on any vector space there are nontrivial linear functionals.” Most analysts do not know how to prove Zorn’s lemma; but it is quite essential for an analyst to understand the statement of Zorn’s lemma and to be able to use it properly!

Proof of Lemma 1.2. Consider the set

$$
P = \left\{ h : D ( h ) \subset E \to \mathbb { R } \left| \begin{aligned} & D ( h ) \text { is a linear subspace of } E, \\ & h \text { is linear, } G \subset D ( h ), \\ & h \text { extends } g, \operatorname { and } h ( x ) \leq p ( x ) \quad \forall x \in D ( h ) \end{aligned} \right. \right\}.
$$

On P we define the order relation

$$
( h _ { 1 } \leq h _ { 2 } ) \Leftrightarrow ( D ( h _ { 1 } ) \subset D ( h _ { 2 } ) { \mathrm { ~ a n d ~ } } h _ { 2 } { \mathrm { ~ e x t e n d s ~ } } h _ { 1 } )   .
$$

It is clear that P is nonempty, since $g \in P$ . We claim that P is inductive. Indeed, let $Q \subset P$ be a totally ordered subset; we write Q as $\mathcal { Q } = ( h _ { i } ) _ { i \in I }$ and we set

$$
D(h) = \bigcup_{i \in I} D(h_i), \quad h(x) = h_i(x) \quad  if   x \in D(h_i)   for some   i.
$$

It is easy to see that the definition of h makes sense, that $h   \in   P$ , and that h is an upper bound for $Q .$ . We may therefore apply Zorn’s lemma, and so we have a maximal element f in P. We claim that $D ( f ) = E$ , which completes the proof of Theorem 1.1.

Suppose, by contradiction, that $D(f) \neq E$ . Let x0 $\notin D ( f )$ ; set $D(h) = D(f) +$ $\mathbb { R } x _ { 0 }$ , and for every $x   \in   D ( f )$ , set $h ( x   +   t x _ { 0 } )   =   f ( x )   +   t \alpha   ( t   \in   \mathbb { R } )$ , where the constant $\alpha \in \mathbb { R }$ will be chosen in such a way that $h \in P$ . We must ensure that

$$
f ( x ) + t \alpha \leq p ( x + t x _ { 0 } ) \quad \forall x \in D ( f ) \quad { \mathrm { a n d } } \quad \forall t \in \mathbb { R } .
$$

In view of (1) it suffices to check that

1.1 The Analytic Form of the Hahn–Banach Theorem: Extension of Linear Functionals

$$
\begin{cases}f(x) + \alpha \leq p(x + x_0) & \forall x \in D(f), \\f(x) - \alpha \leq p(x - x_0) & \forall x \in D(f).\end{cases}
$$

In other words, we must find some α satisfying

$$
\operatorname* { s u p } _ { y \in D ( f ) } \{ f ( y ) - p ( y - x _ { 0 } ) \} \leq \alpha \leq \operatorname* { i n f } _ { x \in D ( f ) } \{ p ( x + x _ { 0 } ) - f ( x ) \} .
$$

Such an α exists, since

$$
f(y) - p(y - x_0) \leq p(x + x_0) - f(x) \quad \forall x \in D(f), \quad \forall y \in D(f);
$$

indeed, it follows from (2) that

$$
f ( x ) + f ( y ) \leq p ( x + y ) \leq p ( x + x _ { 0 } ) + p ( y - x _ { 0 } ) .
$$

We conclude that $f \leq h$ ; but this is impossible, since $f$ is maximal and $h \neq f$

We now describe some simple applications of Theorem 1.1 to the case in which E is a normed vector space $( \mathrm { n . v . s . } )$ with norm .

**Notation.** We denote by $E ^ { \star }$ the dual space of E, that is, the space of all continuous linear functionals on $E ;$ the (dual) norm on $E ^ { \star }$ is defined by

$$
\| f \|_{E^{\star}} = \sup_{\substack{\| x \| \leq 1 \\ x \in E}} | f(x) | = \sup_{\substack{\| x \| \leq 1 \\ x \in E}} f(x).\tag{5}
$$

When there is no confusion we shall also write $\| f \|$ instead of $\| f \| _ { E ^ { \star } }$

Given $f \in E ^ { \star }$ and $x \in E$ we shall often write $\langle f , x \rangle$ instead of $f ( x )$ ; we say that $\langle   ,   \rangle$ is the scalar product for the duality $E ^ { \star } , E$

It is well known that $E ^ { \star }$ is a Banach space, i.e., $E ^ { \star }$ is complete (even if E is not); this follows from the fact that R is complete.

• **Corollary 1.2.** Let $G \subset E$ be a linear subspace. If $g : G \to \mathbb { R }$ is a continuous linear functional, then there exists $f \in E ^ { \star }$ that extends g and such that

$$
\| f \|_{E^{\star}} = \sup_{\substack{x \in G \\ \| x \| \leq 1}} |g(x)| = \| g \|_{G^{\star}}.
$$

Proof. Use Theorem 1.1 with $p ( x ) = \| g \| _ { G ^ { \star } } \| x \|$

• **Corollary 1.3.** For every $x _ { 0 } \in E$ there exists $f _ { 0 } \in E ^ { \star }$ such that

$$
\| \mathbf { \nabla } f _ { 0 } \| = \| x _ { 0 } \| \; a n d \; \langle f _ { 0 } , x _ { 0 } \rangle = \| x _ { 0 } \| ^ { 2 } .
$$

Proof. Use Corollary 1.2 with $G = \mathbb { R } x _ { 0 }$ and $g ( t x _ { 0 } ) = t \| x _ { 0 } \| ^ { 2 }$ , so that $\| g \| _ { G ^ { \star } } = \| x _ { 0 } \|$

Remark 2. The element $f _ { 0 }$ given by Corollary 1.3 is in general not unique (try to construct an example or see Exercise 1.2). However, if $E ^ { \star }$ is strictly convex<sup>2</sup>—for example if E is a Hilbert space (see Chapter 5) or if $E   =   L ^ { p } ( \Omega )$ with $1 < p < \infty$ (see Chapter 4)—then $f _ { 0 }$ is unique. In general, we set, for every $x _ { 0 } \in E$

$$
F ( x _ { 0 } ) = \left\{ f _ { 0 } \in E ^ { \star } ;   \| f _ { 0 } \| = \| x _ { 0 } \| \mathrm { ~ a n d ~ } \langle f _ { 0 } , x _ { 0 } \rangle = \| x _ { 0 } \| ^ { 2 } \right\} .
$$

The (multivalued) map $x _ { 0 } \mapsto F ( x _ { 0 } )$ is called the duality map from $E$ into $E ^ { \star }$ ; some of its properties are described in Exercises 1.1, 1.2, and 3.28 and Problem 13.

• **Corollary 1.4.** For every $x \in E$ we have

$$
\| x \| = \sup_{\substack{f \in E^{\star} \\ \| f \| \leq 1}} | \langle f, x \rangle | = \max_{\substack{f \in E^{\star} \\ \| f \| \leq 1}} | \langle f, x \rangle |.\tag{6}
$$

Proof. We may always assume that $x \neq 0$ . It is clear that

$$
\sup_{\substack{f \in E^{\star} \\ \|f\| \leq 1}} |\langle f, x\rangle| \leq \|x\|.
$$

On the other hand, we know from Corollary 1.3 that there is some $f _ { 0 } \in E ^ { \star }$ such that $\| f _ { 0 } \|   =   \| x \|$ and $\langle f _ { 0 } , x \rangle   =   \| x \| ^ { 2 }$ . Set $f _ { 1 }   =   f _ { 0 } / \| x \|$ , so that $\| f _ { 1 } \|   =   1$ and $\langle f _ { 1 } , x \rangle = \| x \|$

Remark 3. Formula (5)—which is a definition—should not be confused with formula (6), which is a statement. In general, the “sup” in (5) is not achieved; see, e.g., Exercise 1.3. However, the “sup” in (5) is achieved if E is a reflexive Banach space (see Chapter 3); a deep result due to R. C. James asserts the converse: if E is a Banach space such that for every $f \in E ^ { \star }$ the sup in (5) is achieved, then E is reflexive; see, e.g., J. Diestel [1, Chapter 1] or R. Holmes [1].

## 1.2 The Geometric Forms of the Hahn–Banach Theorem: Separation of Convex Sets

We start with some preliminary facts about hyperplanes. In the following, E denotes an n.v.s.

**Definition.** An affine hyperplane is a subset H of E of the form

$$
H = \{ x \in E   ;   f ( x ) = \alpha \} ,
$$

where $f$ is a linear functional<sup>3</sup> that does not vanish identically and $\alpha \in \mathbb { R }$ is a given constant. We write $H = [ f = \alpha ]$ and say that $f = \alpha$ is the equation of H.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x + ( − )y < , ∈ ( , ), x, y</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">||x∥=∥|y∥= 1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">y ;</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^ 2 \mathrm { ~ A ~ }$ normed space is said to be strictly convex if t 1 t 1 ∀t 0 1 ∀ with x = y = and x 	= see Exercise 1.26.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3 We do not assume that  is continuous (in every infinite-dimensional normed space there exist discontinuous linear functionals; see Exercise 1.5).</span></small>

**Proposition 1.5.** The hyperplane $H = [ f = \alpha ]$ is closed if and only if f is continuous.

Proof. It is clear that if f is continuous then H is closed. Conversely, let us assume that H is closed. The complement $H ^ { c }$ of H is open and nonempty (since f does not vanish identically). Let $x _ { 0 } \in H ^ { c }$ , so that $f ( x _ { 0 } ) \neq \alpha$ , for example, $f ( x _ { 0 } ) < \alpha$

Fix $r > 0$ such that $B ( x _ { 0 } , r ) \subset H ^ { c }$ , where

$$
B ( x _ { 0 } , r ) = \{ x \in E   ;   \| x - x _ { 0 } \| < r \} .
$$

We claim that

$$
f ( x ) < \alpha \quad \forall x \in B ( x _ { 0 } , r ) .\tag{7}
$$

Indeed, suppose by contradiction that $f(x_{1}) > \alpha$ for some $x _ { 1 } \; \in \; B ( x _ { 0 } , r )$ . The segment

$$
\{ x _ { t } = ( 1 - t ) x _ { 0 } + t x _ { 1 }   ;   t \in [ 0 , 1 ] \}
$$

is contained in $B ( x _ { 0 } , r )$ and thus $f(x_t) \neq \alpha,   \forall t \in [0,1]$ ; on the other hand, $f ( x _ { t } ) =$ α for some $t \in [ 0 , 1 ]$ , namely $\begin{array} { r } { t = \frac { f ( x _ { 1 } ) - \alpha } { f ( x _ { 1 } ) - f ( x _ { 0 } ) } } \end{array}$ , a contradiction, and thus (7) is proved. It follows from (7) that

$$
f ( x _ { 0 } + r z ) < \alpha \quad \forall z \in B ( 0 , 1 ) .
$$

Consequently, f is continuous and $\begin{array} { r } { \| f \| \leq \frac { 1 } { r } ( \alpha - f ( x _ { 0 } ) ) } \end{array}$

**Definition.** Let A and B be two subsets of E. We say that the hyperplane $H = [ f =$ α] separates A and B if

$$
\boxed { f ( x ) \leq \alpha \quad \forall x \in A \quad \mathrm { a n d } \quad f ( x ) \geq \alpha \quad \forall x \in B . }
$$

We say that H strictly separates A and B if there exists some $\varepsilon > 0$ such that

$$
\boxed{f(x) \leq \alpha - \varepsilon \quad \forall x \in A   and   f(x) \geq \alpha + \varepsilon \quad \forall x \in B.}
$$

Geometrically, the separation means that A lies in one of the half-spaces determined by H, and B lies in the other; see Figure 1.

Finally, we recall that a subset $A \subset E$ is convex if

$$
\boxed{tx + (1 - t)y \in A \quad \forall x,y \in A, \quad \forall t \in [0,1].}
$$

• **Theorem 1.6 (Hahn–Banach, first geometric form).** Let $A \subset E$ and $B \subset E$ be two nonempty convex subsets such that $A \cap B = \varnothing . A s s u m e$ that one of them is open. Then there exists a closed hyperplane that separates A and B.

The proof of Theorem 1.6 relies on the following two lemmas.

**Lemma 1.2.** Let $C \subset E$ be an open convex set with $0 \in C$ . For every $x \in E$ set