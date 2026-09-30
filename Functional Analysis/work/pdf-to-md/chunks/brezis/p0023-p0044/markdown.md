A and B by a closed hyperplane. One can even construct such an example in which A and B are both closed (see Exercise 1.14). However, if E is finite-dimensional one can always separate any two nonempty convex sets A and B such that $A \cap B = \varnothing$ (no further assumption is required!); see Exercise 1.9.

We conclude this section with a very useful fact:

• **Corollary 1.8.** Let $F \subset E$ be a linear subspace such that ${ \overline { { F } } } \neq E$ . Then there exists some $f \in E ^ { \star } ,   f \not \equiv 0 ,$ , such that

$$
\langle f , x \rangle = 0 \quad \forall x \in F .
$$

Proof. Let $x _ { 0 } \in E$ with $x _ { 0 } \notin { \overline { { F } } }$ . Using Theorem 1.7 with $A = { \overline { { F } } }$ and $B = \{ x _ { 0 } \}$ , we find a closed hyperplane $[ f = \alpha ]$ that strictly separates $\overline { { F } }$ and $\{ x _ { 0 } \}$ . Thus, we have

$$
\langle f , x \rangle < \alpha < \langle f , x _ { 0 } \rangle \quad \forall x \in F .
$$

It follows that $\langle f , x \rangle = 0 \quad \forall x \in F$ , since $\lambda \langle f , x \rangle < \alpha$ for every $\lambda \in \mathbb { R }$

• Remark 5. Corollary 1.8 is used very often in proving that a linear subspace $F \subset E$ is dense. It suffices to show that every continuous linear functional on E that vanishes on F must vanish everywhere on $E$

## 1.3 The Bidual $E ^ { \star \star }$ . Orthogonality Relations

Let E be an n.v.s. and let $E ^ { \star }$ be the dual space with norm

$$
\| f \|_{E^{\star}} = \sup_{\substack{x \in E \\ \| x \| \leq 1}} | \langle f, x \rangle |.
$$

The bidual $E ^ { \star \star }$ is the dual of $E ^ { \star }$ with norm

$$
\| \xi \|_{E^{\star \star}} = \sup_{\substack{f \in E^{\star} \\ \| f \| \leq 1}} | \langle \xi, f \rangle | \quad (\xi \in E^{\star \star}).
$$

There is a canonical injection $J : E \to E ^ { \star \star }$ defined as follows: given $x   \in   E$ , the map $f \mapsto \langle f , x \rangle$ is a continuous linear functional on $E ^ { \star }$ ; thus it is an element of $E ^ { \star \star }$ , which we denote by ${ J x . } ^ { 4 }$ We have

$$
\langle J x ,   f \rangle _ { E ^ { \star \star } , E ^ { \star } } = \langle f , x \rangle _ { E ^ { \star } , E } \quad \forall x \in E , \quad \forall f \in E ^ { \star } .
$$

It is clear that J is linear and that J is an isometry, that is, $\| J x \| _ { E ^ { \star \star } } = \| x \| _ { E } ;$ indeed, we have

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">F : E → E\*</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4 J should not be confused with the duality map F : E → E- defined in Remark 2.</span></small>

$$
\| J x \|_{E^{\star \star}} = \sup_{\substack{f \in E^{\star} \\ \| f \| \leq 1}} | \langle J x,   f \rangle | = \sup_{\substack{f \in E^{\star} \\ \| f \| \leq 1}} | \langle f,   x \rangle | = \| x \|.
$$

(by Corollary 1.4).

It may happen that J is not surjective from E onto $E ^ { \star \star }$ (see Chapters 3 and 4). However, it is convenient to identify E with a subspace of $E ^ { \star \star }$ using J . If J turns out to be surjective then one says that E is reflexive, and $E ^ { \star \star }$ is identified with $E$ (see Chapter 3).

**Notation.** If $M \subset E$ is a linear subspace we set

$$
\boxed { M ^ { \perp } = \{ f \in E ^ { \star } ; \langle f , x \rangle = 0 \quad \forall x \in M \} . }
$$

If $N \subset E ^ { \star }$ is a linear subspace we set

$$
\boxed { N ^ { \perp } = \{ x \in E \; ; \langle f , x \rangle = 0 \quad \forall f \in N \} . }
$$

Note that—by definition— $- N ^ { \perp }$ is a subset of E rather than $E ^ { \star \star }$ . It is clear that $M ^ { \perp }$ (resp. $N ^ { \perp } )$ is a closed linear subspace of $E ^ { \star } \left( \mathrm { r e s p . } E \right)$ . We say that $M ^ { \perp } \left( \mathrm { r e s p . } ~ N ^ { \perp } \right)$ is the space orthogonal to M (resp. N).

**Proposition 1.9.** Let $M \subset E$ be a linear subspace. Then

$$
\boxed { ( M ^ { \perp } ) ^ { \perp } = \overline { { M } } } .
$$

Let $N \subset E ^ { \star }$ be a linear subspace. Then

$$
( N ^ { \perp } ) ^ { \perp } \supset \overline { { N } } .
$$

Proof. It is clear that $M \; \subset \; ( M ^ { \perp } ) ^ { \perp }$ , and since $( M ^ { \perp } ) ^ { \perp }$ is closed we have $\overline { { M } } \subset$ $( M ^ { \perp } ) ^ { \perp }$ . Conversely, let us show that $( M ^ { \perp } ) ^ { \perp } \subset \overline { { M } }$ . Suppose by contradiction that there is some $x _ { 0 }   \in   ( M ^ { \perp } ) ^ { \perp }$ such that $x _ { 0 }   \notin   { \overline { { M } } }$ . By Theorem 1.7 there is a closed hyperplane that strictly separates $\{ x _ { 0 } \}$ and M. Thus, there are some $f   \in   E ^ { \star }$ and some $\alpha \in \mathbb { R }$ such that

$$
\langle f , x \rangle < \alpha < \langle f , x _ { 0 } \rangle \quad \forall x \in M .
$$

Since M is a linear space it follows that $\langle f , x \rangle = 0 \quad \forall x \in M$ and also $\langle f , x _ { 0 } \rangle > 0 .$ Therefore $f \in M ^ { \perp }$ and consequently $\langle f , x _ { 0 } \rangle = 0 ,$ , a contradiction.

It is also clear that $N \subset ( N ^ { \perp } ) ^ { \perp }$ and thus $\overline { { N } } \subset ( N ^ { \perp } ) ^ { \perp }$

Remark 6. It may happen that $( N ^ { \perp } ) ^ { \perp }$ is strictly bigger than $\overline { { N } }$ (see Exercise 1.16). It is, however, instructive to $``try''$ to prove that $\widetilde { ( N ^ { \perp } ) ^ { \perp } }   =   \overline { { N } }$ and see where the argument breaks down. Suppose $f _ { 0 }   \in   E ^ { \star }$ is such that $f _ { 0 }   \in   ( N ^ { \perp } ) ^ { \perp }$ and $f _ { 0 } \notin \overline { { N } }$ Applying Hahn–Banach in $E ^ { \star }$ , we may strictly separate $\{ f _ { 0 } \}$ and $\overline { { N } }$ . Thus, there is some $\xi   \in   E ^ { \star \star }$ such that $\langle \xi ,   f _ { 0 } \rangle   >   0$ . But we cannot derive a contradiction, since $\xi \notin N ^ { \perp }$ —unless we happen to know (by chance!) that $\xi \in E$ , or more precisely that $\xi = J x _ { 0 }$ for some $x _ { 0 } \in E$ . In particular, if E is reflexive, it is indeed true that $( N ^ { \perp } ) ^ { \perp } = \overline { { N } }$ . In the general case one can show that $( N ^ { \perp } ) ^ { \perp }$ coincides with the closure of N in the weak- topology $\sigma ( E ^ { \star } , E )$ (see Chapter 3).

## 1.4 A Quick Introduction to the Theory of Conjugate Convex Functions

We start with some basic facts about lower semicontinuous functions and convex functions. In this section we consider functions $\varphi$ defined on a set E with values in $(-\infty,   +\infty)$ , so that $\varphi$ can take the value +∞ (but −∞ is excluded). We denote by $D ( \varphi )$ the domain of $\varphi ,$ that is,

$$
\boxed { D ( \varphi ) = \{ x \in E   ;     \varphi ( x ) < + \infty \} . }
$$

**Notation.** The epigraph of $\varphi$ is the $\mathrm { s e t } ^ { 5 }$

$$
\operatorname { \mathsf { e p i } } \varphi = \{ [ x , \lambda ] \in E \times \mathbb { R }   ; \; \varphi ( x ) \leq \lambda \} .
$$

We assume now that E is a topological space. We recall the following.

**Definition.** A function $\varphi   :   E   \to   ( - \infty , + \infty ]$ is said to be lower semicontinuous (l.s.c.) if for every $\lambda \in \mathbb { R }$ the set

$$
[ \varphi \leq \lambda ] = \{ x \in E ; \varphi ( x ) \leq \lambda \}
$$

is closed.

Here are some well-known elementary facts about l.s.c. functions (see, e.g., G. Choquet, [1], J. Dixmier [1], J. R. Munkres [1], H. L. Royden [1]):

1. If $\varphi$ is l.s.c., then epi $\varphi$ is closed in $E \times \mathbb { R } ;$ ; and conversely.

2. If $\varphi$ is l.s.c., then for every $x \in E$ and for every $\varepsilon > 0$ there is some neighborhood V of x such that

$$
\varphi(y) \geq \varphi(x) - \varepsilon \quad \forall y \in V;
$$

and conversely.

In particular, if $\varphi$ is l.s.c., then for every sequence $( x _ { n } )$ in $E$ such that $x _ { n } \to x$ we have

$$
\boxed{\liminf_{n \to \infty} \varphi(x_n) \geq \varphi(x)}
$$

and conversely if E is a metric space.

3. If $\varphi _ { 1 }$ and $\varphi _ { 2 }$ are l.s.c., then $\varphi _ { 1 } + \varphi _ { 2 }$ is l.s.c.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">= (−∞, ∞)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∞.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">5 We insist on the fact that R , so that λ does not take the value</span></small>

4. If $( \varphi _ { i } ) _ { i \in I }$ is a family of l.s.c. functions then their superior envelope is also $l . s . c .$ that is, the function $\varphi$ defined by

$$
\varphi ( x ) = \operatorname* { s u p } _ { i \in I } \varphi _ { i } ( x )
$$

is l.s.c.

5. If E is compact and $\varphi$ is l.s.c., then inf $E \; \varphi$ is achieved.

(If E is a compact metric space one can argue with minimizing sequences. For a general topological compact space consider the sets $[ \varphi \leq \lambda ]$ for appropriate values of λ.)

We now assume that E is a vector space. Recall the following definition.

**Definition.** A function $\varphi:E\to(-\infty,+\infty]$ is said to be convex if

$$
\boxed { \varphi ( t x + ( 1 - t ) y ) \leq t \varphi ( x ) + ( 1 - t ) \varphi ( y ) \quad \forall x , y \in E , \quad \forall t \in ( 0 , 1 ) . }
$$

We shall use some elementary properties of convex functions:

1. If $\varphi$ is a convex function, then epi $\varphi$ is a convex set in $E \times \mathbb { R } ;$ and conversely.

2. If $\varphi$ is a convex function, then for every $\lambda \in \mathbb { R }$ the set $[ \varphi \leq \lambda ]$ is convex; but the converse is not true.

3. If $\varphi _ { 1 }$ and $\varphi _ { 2 }$ are convex, then $\varphi _ { 1 } + \varphi _ { 2 }$ is convex.

4. If $( \varphi _ { i } ) _ { i \in I }$ is a family of convex functions, then the superior envelope, ${ \mathfrak { s u p } } _ { i }   \varphi _ { i }$ , is convex.

We assume hereinafter that E is an n.v.s.

**Definition.** Let $\varphi \; : \; E \; \rightarrow \; ( - \infty , + \infty ]$ be a function such that $$\varphi \; \not \equiv \; + \infty$ (i.e.$ , $D ( \varphi ) \neq \emptyset )$ . We define the conjugate function $\varphi ^ { \star } : E ^ { \star } \to ( - \infty , + \infty ]$ to $\mathbf { b } \mathbf { e } ^ { 6 }$

$$
\boxed { \varphi ^ { \star } ( f ) = \operatorname* { s u p } _ { x \in E } \{ \langle f , x \rangle - \varphi ( x ) \} \quad ( f \in E ^ { \star } ) . }
$$

Note that $\varphi ^ { \star }$ is convex and l.s.c. on $E ^ { \star }$ . Indeed, for each fixed $x   \in   E$ the function $f \mapsto \langle f , x \rangle - \varphi ( x )$ is convex and continuous (and thus l.s.c.) on $E ^ { \star }$ . It follows that the superior envelope of these functions (as x runs through $E )$ is convex and l.s.c.

Remark 7. Clearly we have the inequality

$$
\langle f , x \rangle \leq \varphi ( x ) + \varphi ^ { \star } ( f ) \quad \forall x \in E , \quad \forall f \in E ^ { \star } ,\tag{11}
$$

which is sometimes called Young’s inequality. Of course, this fact is obvious with our definition of $\varphi ^ { \star } !$ The classical form of Young’s inequality (see the proof of Theorem 4.6 in Chapter 4) asserts that

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">φ\*</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ϕ.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">6 ϕ- is sometimes called the Legendre transform of</span></small>

![](images/page_26_image_1.jpg)

Fig. 2

$$
a b \leq \frac { 1 } { p } a ^ { p } + \frac { 1 } { p ^ { \prime } } b ^ { p ^ { \prime } } \quad \forall a , b \geq 0 .\tag{12}
$$

with $1 < p < \infty$ and $\textstyle { \frac { 1 } { p } }   +   { \frac { 1 } { p ^ { \prime } } } = 1$ . Inequality (12) becomes a special case of (11) with $E = E ^ { \star } = \mathbb { R }$ and $\varphi ( t ) = \frac { 1 } { p } | t | ^ { p } , \varphi ^ { \star } ( s ) = \frac { 1 } { p ^ { \prime } } | s | ^ { p ^ { \prime } }$ (see Exercise 1.18, question (h)).

**Proposition 1.10.** Assume that $\varphi:E\to(-\infty,+\infty]$ is convex $l . s . c .$ and $\varphi \not \equiv + \infty .$ Then $\varphi ^ { \star } \neq + \infty$ , and in particular, ϕ is bounded below by an affine continuous function.

Proof. Let $x _ { 0 } \in D ( \varphi )$ and let $\lambda _ { 0 }   <   \varphi ( x _ { 0 } )$ . We apply Theorem 1.7 (Hahn–Banach, second geometric form) in the space $E \times \mathbb { R }$ with $A   =   \mathrm { e p i }   \varphi$ and $B = \{ [ x _ { 0 } , \lambda _ { 0 } ] \}$ $\mathrm { S o } ,$ there exists a closed hyperplane $H = [ \Phi = \alpha ]$ in $E \times \mathbb { R }$ that strictly separates A and $B ;$ see Figure 2. Note that the function $x \in E \mapsto \Phi ( [ x , 0 ] )$ is a continuous linear functional on $E .$ and thus $\Phi ( [ x , 0 ] ) \: = \: \langle f , x \rangle$ for some $f \in E ^ { \star }$ . Letting $k = \Phi ( [ 0 , 1 ] )$ , we have

$$
\Phi ( [ x , \lambda ] ) = \langle f , x \rangle + k \lambda \quad \forall [ x , \lambda ] \in E \times \mathbb { R } .
$$

Writing that $\Phi > \alpha$ on A and $\Phi < \alpha$ on B, we obtain

$$
\langle f , x \rangle + k \lambda > \alpha , \quad \forall [ x , \lambda ] \in \operatorname { \mathsf { e p i } } \varphi ,
$$

and

$$
\langle f , x _ { 0 } \rangle + k \lambda _ { 0 } < \alpha .
$$

In particular, we have

$$
\langle f , x \rangle + k \varphi ( x ) > \alpha \quad \forall x \in D ( \varphi )\tag{13}
$$

and thus

$$
\langle f , x _ { 0 } \rangle + k \varphi ( x _ { 0 } ) > \alpha > \langle f , x _ { 0 } \rangle + k \lambda _ { 0 } .
$$

It follows that $k > 0$ . By (13) we have

1.4 A Quick Introduction to the Theory of Conjugate Convex Functions

$$
\left\langle - \frac { 1 } { k } f , x \right\rangle - \varphi ( x ) < - \frac { \alpha } { k } \quad \forall x \in D ( \varphi ) .
$$

and therefore $\varphi ^ { \star } ( - { \textstyle { \frac { 1 } { k } } } f ) < + \infty$

If we iterate the operation -, we obtain a function $\varphi ^ { \star \star }$ defined on $E ^ { \star \star }$ . Instead, we choose to restrict $\varphi ^ { \star \star }$ to $E .$ , that is, we define

$$
\boxed { \varphi ^ { \star \star } ( x ) = \operatorname* { s u p } _ { f \in E ^ { \star } } \{ \langle f , x \rangle - \varphi ^ { \star } ( f ) \} \quad ( x \in E ) . }
$$

• **Theorem 1.11 (Fenchel–Moreau).** Assume that $\varphi : E \to ( - \infty , + \infty ]$ is convex, $l . s . c .$ , and $\varphi \not \equiv + \infty$ . Then $\varphi ^ { \star \star } = \varphi .$

Proof. We proceed in two steps:

**Step 1:** We assume in addition that $\varphi \geq 0$ and we claim that $\varphi ^ { \star \star } = \varphi .$

First, it is obvious that $\varphi ^ { \star \star } \leq \varphi ,$ since $\langle f , x \rangle   -   \varphi ^ { \star } ( f )   \leq   \varphi ( x ) \forall x   \in   E$ and $\forall f \in E ^ { \star }$ . In order to prove that $\varphi ^ { \star \star } = \varphi$ we argue by contradiction, and we assume that $\varphi ^ { \star \star } ( x _ { 0 } )   <   \varphi ( x _ { 0 } )$ for some $x _ { 0 } \in E$ . We could possibly have $\varphi ( x _ { 0 } ) = + \infty$ , but $\varphi ^ { \star \star } ( x _ { 0 } )$ is always finite. We apply Theorem 1.7 (Hahn–Banach, second geometric form) in the space $E \times \mathbb { R }$ with $A = \operatorname { \mathsf { e p i } } \varphi$ and $B = [ x _ { 0 } , \varphi ^ { \star \star } ( x _ { 0 } ) ]$ . So, there exist, as in the proof of Proposition 1.10, $f \in E ^ { \star } , k \in \mathbb { R }$ , and $\alpha \in \mathbb { R }$ such that

(14)

$$
\langle f , x \rangle + k \lambda > \alpha \quad \forall [ x , \lambda ] \in \operatorname { \mathsf { e p i } } \varphi ,\tag{15}
$$

$$
\langle f , x _ { 0 } \rangle + k \varphi ^ { \star \star } ( x _ { 0 } ) < \alpha .
$$

It follows that $k \geq 0$ (fix some $x \in D ( \varphi )$ and let $\lambda \to + \infty \operatorname { i n } \left( 1 4 \right) )$ . [Here we cannot assert, as in the proof of Proposition 1.10, that $k > 0 ;$ we could possibly have $k = 0$ which would correspond to a “vertical” hyperplane H in $E \times \mathbb { R } . ]$

Let $\varepsilon > 0 ;$ since $\varphi \geq 0$ , we have by (14),

$$
\langle f , x \rangle + ( k + \varepsilon ) \varphi ( x ) \geq \alpha \quad \forall x \in D ( \varphi ) .
$$

Therefore

$$
\varphi ^ { \star } \left( - \frac { f } { k + \varepsilon } \right) \leq - \frac { \alpha } { k + \varepsilon } .
$$

It follows from the definition of $\varphi ^ { \star \star } ( x _ { 0 } )$ that

$$
\varphi ^ { \star \star } ( x _ { 0 } ) \geq \left\langle - \frac { f } { k + \varepsilon } ,   x _ { 0 } \right\rangle - \varphi ^ { \star } \left( - \frac { f } { k + \varepsilon } \right) \geq \left\langle - \frac { f } { k + \varepsilon } ,   x _ { 0 } \right\rangle + \frac { \alpha } { k + \varepsilon } .
$$

Thus we have

$$
\langle f , x _ { 0 } \rangle + ( k + \varepsilon ) \varphi ^ { \star \star } ( x _ { 0 } ) \geq \alpha \quad \forall \varepsilon > 0 ,
$$

which contradicts (15).

**Step 2:** The general case.

Fix some $f _ { 0 } \in D ( \varphi ^ { \star } ) \; ( D ( \varphi ^ { \star } ) \neq \emptyset$ by Proposition 1.10) and define

$$
\overline { { { \varphi } } } ( x ) = \varphi ( x ) - \langle f _ { 0 } , x \rangle + \varphi ^ { \star } ( f _ { 0 } ) ,
$$

so that $\overline { { \varphi } }$ is convex l.s.c., ${ \overline { { \varphi } } } \not \equiv + \infty ,$ , and $\overline { { \varphi } } \geq 0$ . We know from Step 1 that $( { \overline { { \varphi } } } ) ^ { \star \star } = { \overline { { \varphi } } }$ Let us now compute $( { \overline { { \varphi } } } ) ^ { \star }$ and $( { \overline { { \varphi } } } ) ^ { \star \star }$ . We have

$$
( \overline { { \varphi } } ) ^ { \star } ( f ) = \varphi ^ { \star } ( f + f _ { 0 } ) - \varphi ^ { \star } ( f _ { 0 } )
$$

and

$$
( \overline { { { \varphi } } } ) ^ { \star \star } ( x ) = \varphi ^ { \star \star } ( x ) - \langle f _ { 0 } , x \rangle + \varphi ^ { \star } ( f _ { 0 } ) .
$$

Writing that $( { \overline { { \varphi } } } ) ^ { \star \star } = { \overline { { \varphi } } } ,$ we obtain $\varphi ^ { \star \star } = \varphi$

Let us examine some examples.

Example 1. Consider $\varphi ( x ) = \| x \|$ . It is easy to check that

$$
\varphi ^ { \star } ( f ) = \begin{cases} 0 & \quad \mathrm { i f } \| f \| \leq 1, \\ + \infty & \quad \mathrm { i f } \| f \| > 1. \end{cases}
$$

It follows that

$$
\varphi ^ { \star \star } ( x ) = \operatorname* { s u p } _ { \stackrel { f \in E ^ { \star } } { \| f \| \leq 1 } } \langle f , x \rangle .
$$

Writing the equality

$$
\varphi ^ { \star \star } = \varphi ,
$$

we obtain again part of Corollary 1.4.

Example 2. Given a nonempty set $K \subset E$ , we set

$$
\boxed { I _ { K } ( x ) = \left\{ \begin{aligned} & { { } 0 \quad } & { \mathrm { i f } \; x \in K , } \\ & { { } + \infty \quad } & { \mathrm { i f } \; x \notin K . } \end{aligned} \right. }
$$

The function $I _ { K }$ is called the indicator function of K (and should not be confused with the characteristic function, $\chi _ { K }$ , of K, which is 1 on K and 0 outside K). Note that $I _ { K }$ is a convex function iff K is a convex set, and $I _ { K }$ is l.s.c. iff K is closed. The conjugate function $( I _ { K } ) ^ { \star }$ is called the supporting function of $K$

It is easy to see that if $K = M$ is a linear subspace then $( I _ { M } ) ^ { \star } = I _ { M ^ { \perp } }$ and $( I _ { M } ) ^ { \star \star } =$ $I _ { ( M ^ { \perp } ) ^ { \perp } }$ . Assuming that M is a closed linear space and writing that $( I _ { M } ) ^ { \star \star } = I _ { M }$ , we obtain $( M ^ { \perp } ) ^ { \perp } = M$ . In some sense, Theorem 1.11 can be viewed as a counterpart of Proposition 1.9.

We conclude this chapter with another useful property of conjugate functions.

\- **Theorem 1.12 (Fenchel–Rockafellar).** Let $\varphi , \psi : E \to ( - \infty , + \infty ]$ be two convex functions. Assume that there is some x<sub>0</sub> $\mathbf { \nabla } _ { \mathbf { \nabla } _ { \mathbf { \nabla } } } \in D ( \varphi ) \cap D ( \psi )$ such that ϕ is continuous at x<sub>0</sub>. Then

$$
\begin{align*}\inf_{x \in E} \{ \varphi(x) + \psi(x) \} &= \sup_{f \in E^*} \{ -\varphi^{\star}(-f) - \psi^{\star}(f) \} \\&= \max_{f \in E^*} \{ -\varphi^{\star}(-f) - \psi^{\star}(f) \} = -\min_{f \in E^*} \{ \varphi^{\star}(-f) + \psi^{\star}(f) \}.\end{align*}
$$

The proof of Theorem 1.12 relies on the following lemma.

**Lemma 1.4.** Let $C \subset E$ be a convex set, then Int C is convex.7 If, in addition, Int $C \neq \emptyset ,$ , then

$$
{ \overline { { C } } } = { \overline { { \operatorname { I n t } C } } } .
$$

For the proof of Lemma 1.4, see, e.g., Exercise 1.7.

Proof of Theorem 1.12. Set

$$
\begin{aligned}a &= \inf_{x \in E} \{ \varphi(x) + \psi(x) \}, \\b &= \sup_{f \in E^{\star}} \{ -\varphi^{\star}(-f) - \psi^{\star}(f) \}.\end{aligned}
$$

It is clear that $b \leq a . \operatorname { I f } a = - \infty$ , the conclusion of Theorem 1.12 is obvious. Thus we may assume hereinafter that $a \in \mathbb { R } .$ . Let $C = \operatorname { \mathsf { e p i } } \varphi$ , so that Int $C \neq \emptyset$ (since $\varphi$ is continuous at $x _ { 0 } )$ . We apply Theorem 1.6 (Hahn–Banach, first geometric form) with $A = \operatorname { I n t } C$ and

$$
B = \{ [ x , \lambda ] \in E \times \mathbb { R } ; \; \lambda \leq a - \psi ( x ) \} .
$$

Then A and B are nonempty convex sets. Moreover, $A \cap B = \varnothing ;$ indeed, if $[ [ x , \lambda ] \in A$ then $\lambda > \varphi ( x )$ , and on the other hand, $\varphi ( x ) \geq a - \psi ( x )$ (by definition of a), so that $[ x , \lambda ] \notin B$

Hence there exists a closed hyperplane H that separates A and B. It follows that H also separates $\overline { { A } }$ and B. But we know from Lemma 1.4 that ${ \overline { { A } } } = { \overline { { C } } }$ . Therefore, there exist $f \in E ^ { \star } , k \in \mathbb { R }$ , and $\alpha   \in   \mathbb { R }$ such that the hyperplane $H = [ \Phi = \alpha ]$ in $E \times \mathbb { R }$ separates C and B, where

$$
\Phi ( [ x , \lambda ] ) = \langle f , x \rangle + k \lambda \quad \forall [ x , \lambda ] \in E \times \mathbb { R } .
$$

Thus we have

(16)

$$
\langle f , x \rangle + k \lambda \geq \alpha \quad \forall [ x , \lambda ] \in C ,\tag{17}
$$

$$
\langle f , x \rangle + k \lambda \leq \alpha \quad \forall [ x , \lambda ] \in B .
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">7 As usual, Int C denotes the interior of C.</span></small>

1 The Hahn–Banach Theorems. Introduction to the Theory of Conjugate Convex Functions

Choosing $x = x _ { 0 }$ and letting $\lambda \to + \infty$ in (16), we see that $k \geq 0 .$ We claim that

$$
k > 0 .\tag{18}
$$

Assume by contradiction that $k = 0 ;$ it follows that $\| f \| \neq 0$ (since $\Phi \not \equiv 0 )$ . By (16) and (17) we have

$$
\begin{aligned}\langle f, x \rangle & \geq \alpha \quad \forall x \in D(\varphi), \\\langle f, x \rangle & \leq \alpha \quad \forall x \in D(\psi).\end{aligned}
$$

But $B ( x _ { 0 } , \varepsilon _ { 0 } ) \subset D ( \varphi )$ for some $\varepsilon _ { 0 } > 0$ (small enough), and thus

$$
\langle f , x _ { 0 } + \varepsilon _ { 0 } z \rangle \geq \alpha \quad \forall z \in B ( 0 , 1 ) ,
$$

which implies that $\langle f , x _ { 0 } \rangle \geq \alpha + \varepsilon _ { 0 } \| f \|$ . On the other hand, we have $\langle f , x _ { 0 } \rangle \leq \alpha ,$ since $x _ { 0 } \in D ( \psi )$ ; therefore we obtain $\| f \| \; = \; 0$ , which is a contradiction and completes the proof of (18).

From (16) and (17) we obtain

$$
\varphi ^ { \star } \left( - { \frac { f } { k } } \right) \leq - { \frac { \alpha } { k } }
$$

and

$$
\psi ^ { \star } \left( { \frac { f } { k } } \right) \leq { \frac { \alpha } { k } } - a ,
$$

so that

$$
- \varphi ^ { \star } \left( - \frac { f } { k } \right) - \psi ^ { \star } \left( \frac { f } { k } \right) \geq a .
$$

On the other hand, from the definition of b, we have

$$
- \varphi ^ { \star } \left( - \frac { f } { k } \right) - \psi ^ { \star } \left( \frac { f } { k } \right) \leq b.
$$

We conclude that

$$
a = b = - \varphi ^ { \star } \left( - { \frac { f } { k } } \right) - \psi ^ { \star } \left( { \frac { f } { k } } \right) .
$$

Example 3. Let K be a nonempty convex set. We claim that for every $x _ { 0 }   \in   E$ we have

$$
\mathrm{dist}(x_{0}, K) = \inf_{x \in K} \|x - x_{0}\| = \max_{\substack{f \in E^{\star} \\ \|f\| \leq 1}} \{\langle f, x_{0}\rangle - I_{K}^{\star}(f)\}.\tag{19}
$$

Indeed, we have

$$
\inf_{x \in K} \|x - x_0\| = \inf_{x \in E} \{\varphi(x) + \psi(x)\},
$$

with $\varphi(x) = \|x - x_0\|$ and $\psi ( x ) = I _ { K } ( x )$ . Applying Theorem 1.12, we obtain (19). In the special case that $K = M$ is a linear subspace, we obtain the relation

$$
\operatorname { d i s t } ( x _ { 0 } , M ) = \operatorname* { i n f } _ { x \in M } \lVert x - x _ { 0 } \rVert = \operatorname* { m a x } _ { \substack { f \in M ^ { \perp } \\ \lVert f \rVert \leq 1 } } \langle f , x _ { 0 } \rangle .
$$

Remark 8. Relation (19) may provide us with some useful information in the case that in $\mathbb { f } _ { x \in K } \left\| x - x _ { 0 } \right\|$ is not achieved (see, e.g., Exercise 1.17). The theory of minimal surfaces provides an interesting setting in which the primal problem (i.e., $\operatorname* { i n f } _ { x \in E } \{ \varphi ( x )   +   \psi ( x ) \} )$ need not have a solution, while the dual problem (i.e., max $\iota _ { f \in E ^ { \star } } \{ - \varphi ^ { \star } ( - f ) - \psi ^ { \star } ( f ) \} )$ has a solution; see I. Ekeland–R. Temam [1].

Example 4. Let $\varphi : E \to \mathbb { R }$ be convex and continuous and let $M \subset E$ be a linear subspace. Then we have

$$
\inf_{x \in M} \varphi(x) = - \min_{f \in M^{\perp}} \varphi^{\star}(f).
$$

It suffices to apply Theorem 1.12 with $\psi = I _ { M }$

## Comments on Chapter 1

## 1. Generalizations and variants of the Hahn–Banach theorems.

The first geometric form of the Hahn–Banach theorem (Theorem 1.6) is still valid in general topological vector spaces. The second geometric form (Theorem 1.7) holds in locally convex spaces—such spaces play an important role, for example, in the theory of distributions (see, e.g., L. Schwartz [1] and F. Treves [1]). Interested readers may consult, e.g., N. Bourbaki [1], J. Kelley-I. Namioka [1], G. Choquet [2] (Volume 2), A. Taylor–D. Lay [1], and A. Knapp [2].

## 2. Applications of the Hahn–Banach theorems.

The Hahn–Banach theorems have a wide and diversified range of applications. Here are two examples:

## (a) The Krein–Milman theorem.

The second geometric form of the Hahn–Banach theorem is a basic ingredient in the proof of the Krein–Milman theorem. Before stating this result we need some definitions. Let E be an n.v.s. and let A be a subset of E. The convex hull of A, denoted by conv A, is the smallest convex set containing A. Clearly, conv A consists of all finite convex combinations of elements in A, i.e.,

$$
\mathrm{conv}   A = \left\{ \sum_{i \in I} t_i a_i; \quad I   finite , \quad a_i \in A \quad \forall i, \quad t_i \geq 0 \quad \forall i, \quad  and  \quad \sum_{i \in I} t_i = 1 \right\}.
$$

The closed convex hull of A, denoted by convA, is the closure of conv A. Given a convex set $K   \subset   E$ we say that a point $x \in K$ is extremal if x cannot be written as a convex combination of two points $x _ { 0 } , x _ { 1 } \in K , \mathrm { i . e . } , x \neq ( 1 - t ) x _ { 0 } + t x _ { 1 }$ with $t \in ( 0 , 1 )$ , and $x _ { 0 } \neq x _ { 1 }$

• **Theorem 1.13 (Krein–Milman).** Let $K \subset E$ be a compact convex set. Then K coincides with the closed convex hull of its extremal points.

The Krein–Milman theorem has itself numerous applications and extensions (such as Choquet’s integral representation theorem, Bochner’s theorem, Bernstein’s theorem, etc.). On this vast subject, see, e.g., N. Bourbaki [1], G. Choquet [2] (Volume 2), R. Phelps [1], C. Dellacherie-P.A. Meyer [1] (Chapter 10), N. Dunford–J. T. Schwartz [1] (Volume 1), W. Rudin [1], R. Larsen [1], J. Kelley–I. Namioka [1], R. Edwards [1]. An interesting application to PDEs, due toY. Pinchover, is presented in S. Agmon [2]. For a proof of the Krein–Milman theorem, see Problem 1.

(b) In the theory of partial differential equations.

Let us mention, for example, that the existence of a fundamental solution for a general differential operator $P ( D )$ with constant coefficients (the Malgrange–Ehrenpreis theorem) relies on the analytic form of Hahn–Banach; see, e.g., L. Hörmander [1], [2], K. Yosida [1], W. Rudin [1], F. Treves [2], M. Reed-B. Simon [1] (Volume 2). In the same spirit, let us mention also the proof of the existence of the Green’s function for the Laplacian by the method of P. Lax; see P. Lax [1] (Section 9.5) and P. Garabedian [1]. The proof of the existence of a solution $u \in L ^ { \infty } ( \Omega )$ for the equation div $u   =   f$ in $\Omega   \subset   \mathbb { R } ^ { N }$ , given any $f   \in   L ^ { N } ( \Omega )$ , relies on Hahn–Banach (see J. Bourgain–H. Brezis [1], [2]). Surprisingly, the u obtained via Hahn–Banach depends nonlinearly on $f$ . In fact, there exists no bounded linear operator from $L ^ { N }$ into $L ^ { \infty }$ giving u in terms of $f$ . This shows that the use of Zorn’s lemma (and the underlying axiom of choice) in the proof of Hahn–Banach can be delicate and may destroy the linear character of the problem. Sometimes there is no way to circumvent this obstruction.

## 3. Convex functions.

Convex analysis and duality principles are topics which have considerably expanded and have become increasingly popular in recent years; see, e.g., J. J. Moreau [1], R. T. Rockafellar [1], [2], I. Ekeland–R. Temam [1], I. Ekeland–T. Turnbull [1], F. Clarke [1], J. P. Aubin–I. Ekeland [1], J. B. Hiriart–Urutty–C. Lemaréchal [1]. Among the applications let us mention the following:

(a) Game theory, economics, optimization, convex programming; see J. P. Aubin [1], [2], [3], J. P. Aubin–I. Ekeland [1], S. Karlin [1], A. Balakrishnan [1], V. Barbu– I. Precupanu [1], J. Franklin [1], J. Stoer–C. Witzgall [1].

(b) Mechanics; see J. J. Moreau [2], P. Germain [1], [2], G. Duvaut–J. L. Lions [1], R. Temam–G. Strang [1] and the comments by P. Germain following this paper, H. D. Bui [1] and the numerous references therein. Note also the use of (nonconvex) duality by J. F. Toland [1], [2], [3] (for the study of rotating chains), by A. Damlamian [1] (for a problem arising in plasma physics), and by G. Auchmuty [1].

(c) The theory of monotone operators and nonlinear semigroups; see H. Brezis [1], F. Browder [1], V. Barbu [1], and R. Phelps [2].

(d) Variational problems involving periodic solutions of Hamiltonian systems and nonlinear vibrating strings; see the recent works of F. Clarke, I. Ekeland, J. M. Lasry, H. Brezis, J. M. Coron, L. Nirenberg (we refer, e.g., to F. Clarke– I. Ekeland [1], H. Brezis–J. M. Coron–L. Nirenberg [1], H. Brezis [2], J. P. Aubin– I. Ekeland [1], I. Ekeland [1], and their bibliographies).

(e) The theory of large deviations in probability; see, e.g., R. Azencott et al. [1], D. W. Stroock [1].

(f) The theory of partial differential equations and complex analysis; see L. Hörmander [3].

## 4. Extensions of bounded linear operators.

Let E and F be two Banach spaces and let $G \subset E$ be a closed subspace. Let $S : G \to F$ be a bounded linear operator. One may ask whether it is possible to extend S by a bounded linear operator $T : E \to F$ . Note that Corollary 1.2 settles this question only when $F = \mathbb { R }$ . In general, the answer is negative (even if E and F are reflexive spaces; see Exercise 1.27), except in some special cases; for example, the following:

(a) If dim $F < \infty$ . One may choose a basis in F and apply Corollary 1.2 to each component of S.

(b) If G admits a topological complement (see Section 2.4). This is true in particular if dim $G < \infty$ or codim $G < \infty$ or if E is a Hilbert space.

One may also ask the question whether there is an extension T with the same norm, $\mathrm { i . e . , } \; \| T \| _ { \mathcal { L } ( E , F ) } = \| S \| _ { \mathcal { L } ( G , F ) }$ . The answer is yes only in some exceptional cases; see L. Nachbin [1], J. Kelley [1], and Exercise 5.15.

## Exercises for Chapter 1

## 1.1 Properties of the duality map.

Let E be an n.v.s. The duality map F is defined for every $x \in E$ by

$$
F ( x ) = \{ f \in E ^ { \star } ; \; \left\| f \right\| = \left\| x \right\| \mathrm { a n d } \left\langle f , x \right\rangle = \left\| x \right\| ^ { 2 } \} .
$$

1. Prove that

$$
F ( x ) = \{ f \in E ^ { \star } ; \; \left\| f \right\| \leq \left\| x \right\| \mathrm { a n d } \left\langle f , x \right\rangle = \left\| x \right\| ^ { 2 } \}
$$

and deduce that $F ( x )$ is nonempty, closed, and convex.

2. Prove that if $E ^ { \star }$ is strictly convex, then $F ( x )$ contains a single point.

3. Prove that

$$
F ( x ) = \left\{ f \in E ^ { \star } ; \frac { 1 } { 2 } \| y \| ^ { 2 } - \frac { 1 } { 2 } \| x \| ^ { 2 } \geq \langle f , y - x \rangle \quad \forall y \in E \right\} .
$$

4. Deduce that

$$
\langle F ( x ) - F ( y ) ,   x - y \rangle \geq 0 \quad \forall x , y \in E ,
$$

and more precisely that

$$
\langle f - g,   x - y \rangle \geq 0 \quad \forall x, y \in E, \quad \forall f \in F(x), \quad \forall g \in F(y).
$$

Show that, in fact,

$$
\langle f - g,   x - y \rangle \geq ( \| x \| - \| y \| )^2 \quad \forall x, y \in E, \quad \forall f \in F(x), \quad \forall g \in F(y).
$$

5. Assume again that $E ^ { \star }$ is strictly convex and let $x , y \in E$ be such that

$$
\langle F ( x ) - F ( y ) ,   x - y \rangle = 0 .
$$

Show that $F x = F y$

$\boxed { 1 . 2 }$ Let E be a vector space of dimension n and let $( e _ { i } ) _ { 1 \leq i \leq n }$ be a basis of E. Given $x \in E$ , write $\textstyle x = \sum _ { i = 1 } ^ { n } x _ { i } e _ { i }$ with $$x _ { i } \in \mathbb { R } ;$$ ; given $f \in E ^ { \star }$ , set $f _ { i } = \langle f , e _ { i } \rangle$

1. Consider on E the norm

$$
\| x \| _ { 1 } = \sum _ { i = 1 } ^ { n } | x _ { i } | .
$$

(a) Compute explicitly, in terms of the $f _ { i } { } ^ { \prime } \mathbf { s }$ , the dual norm $\| f \| _ { E ^ { \star } }$ of $f \in E ^ { \star }$

(b) Determine explicitly the set $F ( x )$ (duality map) for every $x \in E$

2. Same questions but where E is provided with the norm

$$
\| x \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } | x _ { i } | .
$$

3. Same questions but where E is provided with the norm

$$
\| x \| _ { 2 } = \left( \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { 2 } \right) ^ { 1 / 2 } ,
$$

and more generally with the norm

$$
\| x \| _ { p } = \left( \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { p } \right) ^ { 1 / p } , \quad \mathrm { w h e r e } p \in ( 1 , \infty ) .
$$

$\boxed { 1 . 3 }$ Let $E = \{ u \in C ( [ 0 , 1 ] ; \mathbb { R } ) ; u ( 0 ) = 0 \}$ with its usual norm

$$
\| u \| = \operatorname* { m a x } _ { t \in [ 0 , 1 ] } | u ( t ) | .
$$

Consider the linear functional

1.4 Exercises for Chapter 1

$$
f : u \in E \mapsto f ( u ) = \int _ { 0 } ^ { 1 } u ( t ) d t .
$$

1. Show that $f \in E ^ { \star }$ and compute $\| f \| _ { E ^ { \star } }$

2. Can one find some $u \in E$ such that $\| u \| = 1$ and $f ( u ) = \| f \| _ { E ^ { \star } } ?$

<u>1.4</u> Consider the space $E   =   c _ { 0 }$ (sequences tending to zero) with its usual norm (see Section 11.3). For every element $u = ( u _ { 1 } , u _ { 2 } , u _ { 3 } , \dots )$ in E define

$$
f(u) = \sum_{n = 1}^{\infty}\frac{1}{2^{n}}u_{n}.
$$

1. Check that f is a continuous linear functional on E and compute $\| f \| _ { E ^ { \star } }$

2. Can one find some $u \in E$ such that $\| u \| = 1$ and $f ( u ) = \| f \| _ { E ^ { \star } } ?$

<u>1.5</u> Let E be an infinite-dimensional n.v.s.

1. Prove (using Zorn’s lemma) that there exists an algebraic basis $( e _ { i } ) _ { i \varepsilon I }$ in E such that $\| e _ { i } \| = 1   \forall i \in I$

Recall that an algebraic basis (or Hamel basis) is a subset $( e _ { i } ) _ { i \varepsilon I }$ in E such that every $x \in E$ may be written uniquely as

$$
x = \sum _ { i \varepsilon J } x _ { i } e _ { i } { \mathrm { ~ w i t h ~ } } J \subset I , J { \mathrm { ~ f i n i t e } } .
$$

2. Construct a linear functional $f : E \to \mathbb { R }$ that is not continuous.

3. Assuming in addition that E is a Banach space, prove that I is not countable.

[**Hint:** Use Baire category theorem (Theorem 2.1).]

<u>1.6</u> Let E be an n.v.s. and let $H \subset E$ be a hyperplane. Let $V \subset E$ be an affine subspace containing H.

1. Prove that either $V = H$ or $V = E$

2. Deduce that H is either closed or dense in E.

$\boxed { 1 . 7 }$ Let E be an n.v.s. and let $C \subset E$ be convex.

1. Prove that $\overline { { C } }$ and Int C are convex.

2. Given $x \in C$ and $y \in$ Int C, show that $t x + ( 1 - t ) y \in \operatorname { I n t } C \quad \forall t \in ( 0 , 1 )$

3. Deduce that ${ \overline { { C } } } = { \overline { { \operatorname { I n t } C } } }$ whenever Int $C \neq \emptyset .$

<u>1.8</u> Let E be an n.v.s. with norm . Let $C \subset E$ be an open convex set such that $0 \in C$ . Let p denote the gauge of C (see Lemma 1.2).

1. Assuming C is symmetric $( \mathrm { i . e . , } - C = C )$ and C is bounded, prove that p is a norm which is equivalent to .

1 The Hahn–Banach Theorems. Introduction to the Theory of Conjugate Convex Functions

2. Let $E = C ( [ 0 , 1 ] ;$ R) with its usual norm

$$
\| u \| = \max_{t \in [0,1]} |u(t)|.
$$

Let

$$
C = \left\{ u \in E ; \; \int _ { 0 } ^ { 1 } | u ( t ) | ^ { 2 } d t < 1 \right\} .
$$

Check that C is convex and symmetric and that $0   \in   C$ . Is C bounded in E? Compute the gauge $p$ of C and show that $p$ is a norm on E. Is p equivalent to?

<u>1.9</u> Hahn–Banach in finite-dimensional spaces.

Let E be a finite-dimensional normed space. Let $C \subset E$ be a nonempty convex set such that $0 \notin C$ . We claim that there always exists some hyperplane that separates C and {0}.

[Note that every hyperplane is closed (why?). The main point in this exercise is that no additional assumption on C is required.]

1. Let $( x _ { n } ) _ { n \geq 1 }$ be a countable subset of C that is dense in C (why does it exist?). For every n let

$$
C _ { n } = \operatorname { c o n v } \{ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \} = \left\{ x = \sum _ { i = 1 } ^ { n } t _ { i } x _ { i } ; t _ { i } \geq 0 \; \forall i { \mathrm { ~ a n d ~ } } \sum _ { i = 1 } ^ { n } t _ { i } = 1 \right\} .
$$

Check that $C _ { n }$ is compact and that $\textstyle \bigcup _ { n = 1 } ^ { \infty } C _ { n }$ is dense in C.

2. Prove that there is some $f _ { n } \in E ^ { \star }$ such that

$$
\| f _ { n } \| = 1 \mathrm { a n d } \langle f _ { n } , x \rangle \geq 0 \quad \forall x \in C _ { n } .
$$

3. Deduce that there is some $f \in E ^ { \star }$ such that

$$
\| f \| = 1 { \mathrm { ~ a n d ~ } } \langle f , x \rangle \geq 0 \quad \forall x \in C .
$$

Conclude.

4. Let $A , B   \subset   E$ be nonempty disjoint convex sets. Prove that there exists some hyperplane H that separates A and B.

<u>1.10</u> Let E be an n.v.s. and let I be any set of indices. Fix a subset $( x _ { i } ) _ { i \varepsilon I }$ in E and a subset $( \alpha _ { i } ) _ { i \varepsilon I }$ in R. Show that the following properties are equivalent:

(A) There exists some $f \in E ^ { \star }$ such that $\langle f , x _ { i } \rangle = \alpha _ { i } \quad \forall i \in I$

(B)

There exists a constant $M \geq 0$ such that for each finite subset $J \subset I$ and for every choice of real numbers $( \beta _ { i } ) _ { i \in J }$ , we have

$$
\bigl | \sum _ { i \in J } \beta _ { i } \alpha _ { i } \bigr | \leq M \bigl \| \sum _ { i \in J } \beta _ { i } x _ { i } \bigr \|   .
$$

Note that in the proof of $( \mathrm { B } )   \Rightarrow   ( \mathrm { A } )$ one may find some $f \in E ^ { \star }$ with $\| f \| _ { E ^ { \star } } \leq M$ [Hint: Try first to define f on the linear space spanned by the $( x _ { i } ) _ { i \varepsilon I } . ]$

$\boxed { 1 . 1 1 }$ Let E be an n.v.s. and let $M > 0$ . Fix n elements $( f _ { 1 } ) _ { 1 \leq i \leq n }$ in $E ^ { \star }$ and n real numbers $( \alpha _ { i } ) _ { 1 \leq i \leq n }$ . Prove that the following properties are equivalent:

(A)

$$
\begin{cases}\forall \varepsilon > 0 \quad \exists x_{\varepsilon} \in E \quad  such that  \\\|x_{\varepsilon}\| \leq M + \varepsilon \quad  and  \quad \langle f_{i}, x_{\varepsilon} \rangle = \alpha_{i} \quad \forall i = 1, 2, \ldots, n.\end{cases}\tag{B}
$$

$$
\Big | \sum _ { i = 1 } ^ { n } \beta _ { i } \alpha _ { i } \Big | \leq M \Big \| \sum _ { i = 1 } ^ { n } \beta _ { i }   f _ { i } \Big \| \quad \forall \beta _ { 1 } ,   \beta _ { 2 } , \ldots , \beta _ { n } \in \mathbb { R } .
$$

[**Hint:** For the proof of $( \mathbf { B } ) \Rightarrow ( \mathbf { A } )$ consider first the case in which the $f _ { i } { } ^ { \prime } \mathbf { s }$ are linearly independent and imitate the proof of Lemma 3.3.]

Compare Exercises 1.10, 1.11 and Lemma 3.3.

<u>1.12</u> Let E be a vector space. Fix n linear functionals $( f _ { i } ) _ { 1 \leq i \leq n }$ on E and n real numbers $( \alpha _ { i } ) _ { 1 \leq i \leq n }$ . Prove that the following properties are equivalent:

(A) There exists some $x \in E$ such that $f _ { i } ( x ) = \alpha _ { i } \quad \forall i = 1 , 2 , \ldots , n$

(B)

For any choice of real numbers $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { n }$ such that $\begin{array} { r } { \prod _ { i = 1 } ^ { n } \beta _ { i }   f _ { i } = 0 } \end{array}$ , one also has $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \beta _ { i } \alpha _ { i } = 0 . } \end{array}$

<u>1.13</u> Let $E = \mathbb { R } ^ { n }$ and let

$$
P = \{ x \in \mathbb { R } ^ { n } ; x _ { i } \geq 0 \forall i = 1 , 2 , \ldots , n \} .
$$

Let M be a linear subspace of E such that $M \cap P = \{ 0 \}$ . Prove that there is some hyperplane H in E such that

$$
M \subset H { \mathrm { ~ a n d ~ } } H \cap P = \{ 0 \} .
$$

[**Hint:** Show first that $M ^ { \perp } \cap$ Int $P \neq \emptyset . ]$

<u>1.14</u> Let $E = \ell ^ { 1 }$ (see Section 11.3) and consider the two sets

$$
X = \{ x = ( x _ { n } ) _ { n \geq 1 } \in E ; x _ { 2 n } = 0 \; \forall n \geq 1 \}
$$

and

$$
Y = \left\{ y = ( y _ { n } ) _ { n \geq 1 } \in E ; y _ { 2 n } = \frac { 1 } { 2 ^ { n } } y _ { 2 n - 1 } \; \forall n \geq 1 \right\} .
$$

1. Check that X and Y are closed linear spaces and that ${ \overline { { X + Y } } } = E$

2. Let $c \in E$ be defined by

1 The Hahn–Banach Theorems. Introduction to the Theory of Conjugate Convex Functions

$$
\begin{cases}c_{2n-1} = 0 \quad & \forall n \geq 1, \\c_{2n} = \frac{1}{2^n} \quad & \forall n \geq 1.\end{cases}
$$

Check that $c \notin X + Y$

3. Set $Z = X - c$ and check that $Y \cap Z = \varnothing$ . Does there exist a closed hyperplane in E that separates Y and Z?

Compare with Theorem 1.7 and Exercise 1.9.

4. Same questions in $E = \ell ^ { p } , 1 < p < \infty ,$ and in $E = c _ { 0 }$

<u>1.15</u> Let E be an n.v.s. and let $C \subset E$ be a convex set such that $0 \in C$ . Set

(A)

$$
C ^ { \star } = \{ f \in E ^ { \star }   ; \langle f , x \rangle \leq 1 \quad \forall x \in C \} ,
$$

(B)

$$
C ^ { \star \star } = \{ x \in E   ; \langle f , x \rangle \leq 1 \ \forall f \in C ^ { \star } \} .
$$

1. Prove that $C ^ { \star \star } = { \overline { { C } } }$

2. What is C- if C is a linear space?

<u>1.16</u> Let $E = \ell ^ { 1 }$ , so that $E ^ { \star } = \ell ^ { \infty }$ (see Section 11.3). Consider $N = c _ { 0 }$ as a closed subspace of $E ^ { \star }$

Determine

$$
N ^ { \perp } = \{ x \in E ; \langle f , x \rangle = 0 \ \forall f \in N \}
$$

and

$$
N ^ { \perp \perp } = \{ f \in E ^ { \star } ; \langle f , x \rangle = 0 \quad \forall x \in N ^ { \perp } \} .
$$

Check that $N ^ { \perp \perp } \neq N$

<u>1.17</u> Let E be an n.v.s. and let $f   \in   E ^ { \star }$ with $f \neq 0$ . Let M be the hyperplane $\overline { { [ f = 0 ] } }$

1. Determine $M ^ { \perp }$

2. Prove that for every $x \in E$ , dis $\begin{array} { r } { \mathfrak { t } ( x , M ) = \operatorname* { i n f } _ { y \in M } \| x - y \| = \frac { | \langle f , x \rangle | } { \| f \| } . } \end{array}$

[Find a direct method or use Example 3 in Section 1.4.]

3. Assume now that $E = \{ u \in C ( [ 0 , 1 ] ; \mathbb { R } ) ; u ( 0 ) = 0 \}$ and that

$$
\langle f , u \rangle = \int _ { 0 } ^ { 1 } u ( t ) d t , \quad u \in E .
$$

Prove that dist $\begin{array} { r } { \iota ( u , M ) = | \int _ { 0 } ^ { 1 } u ( t ) d t |   \forall u \in E . } \end{array}$

Show that in $\mathrm { f } _ { v \in M } \left\| u - v \right\|$ is never achieved for any $u \in E \backslash M$

<u>1.18</u> Check that the functions $\varphi   :   \mathbb { R }   \to   ( - \infty ,   + \infty ]$ defined below are convex l.s.c. and determine the conjugate functions $\varphi ^ { \star }$ . Draw their graphs and mark their epigraphs.

1.4 Exercises for Chapter 1

(a)

$$
\varphi ( x ) = a x + b , \qquad { \mathrm { w h e r e ~ } } a , b \in \mathbb { R } .\tag{b}
$$

$$
\varphi ( x ) = e ^ { x } .\tag{c}
$$

$$
\varphi ( x ) = \begin{cases} 0 &  滘設  \quad \mathrm { i f } | x | \leq 1, \\ + \infty &  滘設  \quad \mathrm { i f } | x | > 1. \end{cases}\tag{d}
$$

$$
\varphi ( x ) = \begin{cases} { 0 \qquad } & { \mathrm { i f } \; x = 0 , } \\ { + \infty \qquad } & { \mathrm { i f } \; x \neq 0 . } \end{cases}\tag{e}
$$

$$
\varphi ( x ) =  \begin{cases} { - \log x \qquad } & { \mathrm { i f } \: x > 0 , } \\ { + \infty \qquad } & { \mathrm { i f } \: x \leq 0 . } \end{cases}\tag{f}
$$

$$
\varphi ( x ) = \begin{cases} { - ( 1 - x ^ { 2 } ) ^ { 1 / 2 } \qquad } & { \mathrm { i f } \; | x | \leq 1 , } \\ { + \infty \qquad } & { \mathrm { i f } \; | x | > 1 . } \end{cases}\tag{g}
$$

$$
\varphi ( x ) = \begin{cases} { \frac { 1 } { 2 } | x | ^ { 2 } \qquad } & { \mathrm { i f } \; | x | \leq 1 , } \\ { | x | - \frac { 1 } { 2 } \qquad } & { \mathrm { i f } \; | x | > 1 . } \end{cases}\tag{h}
$$

$$
\varphi ( x ) = { \frac { 1 } { p } } | x | ^ { p } , \qquad { \mathrm { w h e r e ~ } } 1 < p < \infty .
$$

(i) ϕ(x) = x+ = max{x, 0}.

(j)

$$
\varphi ( x ) = \begin{cases} { \frac { 1 } { p } x ^ { p } } & { \quad \mathrm { i f } \; x \geq 0 , \mathrm { w h e r e } \; 1 < p < + \infty , } \\ { + \infty } & { \quad \mathrm { i f } \; x < 0 . } \end{cases}\tag{k}
$$

$$
\varphi ( x ) =  \begin{cases} { - \frac { 1 } { p } x ^ { p } \qquad } & { \mathrm { i f } \; x \geq 0 , \mathrm { w h e r e } \; 0 < p < 1 , } \\ { + \infty \qquad } & { \mathrm { i f } \; x < 0 . } \end{cases}\tag{1}
$$

$$
\varphi ( x ) = \frac { 1 } { p } [ ( | x | - 1 ) ^ { + } ] ^ { p } , \qquad \mathrm { w h e r e } \; 1 < p < \infty .
$$

<u>1.19</u> Let E be an n.v.s.

1. Let $\varphi ,   \psi   :   E   \to   ( - \infty ,   + \infty ]$ be two functions such that $\varphi \leq \psi$ . Prove that $\psi ^ { \star } \leq \varphi ^ { \star }$

2. Let $F : \mathbb { R } \to   ( - \infty ,   + \infty ]$ be a convex l.s.c. function such that $F ( 0 ) = 0$ and $F(t) \geq 0 \forall t \in \mathbb{R}. \operatorname{Set} \varphi(x) = F(\|x\|)$

Prove that $\varphi$ is convex l.s.c. and that $\varphi ^ { \star } ( f ) = F ^ { \star } ( \| f \| )   \forall f \in E ^ { \star }$

<u>1.20</u> Let $E = \ell ^ { p }$ with $1   \leq   p   <   \infty$ (see Section 11.3). Check that the functions $\varphi   :   E   \to   ( - \infty ,   + \infty ]$ defined below are convex l.s.c. and determine $\varphi ^ { \star }$ . For $x =$ $( x _ { 1 } , x _ { 2 } , \dots , x _ { n } , \dots )$ set

$$
\varphi ( x ) =  \begin{cases} { \sum _ { k = 1 } ^ { + \infty } \; k | x _ { k } | ^ { 2 } \qquad } & { \mathrm { i f } \; \sum _ { k = 1 } ^ { \infty } \; k | x _ { k } | ^ { 2 } < + \infty , } \\ { + \infty \qquad } & { \mathrm { o t h e r w i s e } . } \end{cases}\tag{a}
$$

$$
\varphi ( x ) = \sum _ { k = 2 } ^ { + \infty } | x _ { k } | ^ { k } .\tag{b}
$$

$$
( \mathrm{C h e c k ~ t h a t } \; \varphi ( x ) < \infty \; \mathrm{for ~ every } \; x \in E. )
$$

26 1 The Hahn–Banach Theorems. Introduction to the Theory of Conjugate Convex Functions

$$
\varphi(x)=\begin{cases}\displaystyle\sum_{k = 1}^{+\infty}|x_{k}| &  滘  \quad  if  \displaystyle\sum_{k = 1}^{\infty}|x_{k}|<+\infty, \\ +\infty &  滘  otherwise .\end{cases}\tag{c}
$$

<u>1.21</u> Let $E = E ^ { \star } = \mathbb { R } ^ { 2 }$ and let

$$
C = \{ [ x _ { 1 } , x _ { 2 } ] ; x _ { 1 } \geq 0 , x _ { 2 } \geq 0 \} .
$$

On $E$ define the function

$$
\varphi ( x ) = \begin{cases} { - { \sqrt { x _ { 1 } x _ { 2 } } } \qquad } & { { \mathrm { i f } } \; x \in C , } \\ { + \infty \qquad } & { { \mathrm { i f } } \; x \notin C . } \end{cases}
$$

1. Prove that $\varphi$ is convex l.s.c. on $E$

2. Determine $\varphi ^ { \star }$

3. Consider the set $D = \{ [ x _ { 1 } , x _ { 2 } ] ; x _ { 1 } = 0 \}$ and the function $\psi = I _ { D }$ . Compute the value of the expressions

$$
\inf_{x \in E} \{ \varphi(x) + \psi(x) \} \quad  and  \quad \sup_{f \in E^\star} \{ -\varphi^\star(-f) - \psi^\star(f) \}.
$$

4. Compare with the conclusion of Theorem 1.12 and explain the difference.

<u>1.22</u> Let $E$ be an n.v.s. and let $A \subset E$ be a closed nonempty set. Let

$$
\varphi(x) = \mathrm{dist}(x, A) = \inf_{a \in A} \|x - a\|.
$$

1. Check that $| \varphi ( x ) - \varphi ( y ) | \leq \| x - y \|   \forall x ,   y \in E .$

2. Assuming that A is convex, prove that $\varphi$ is convex.

3. Conversely, assuming that ϕ is convex, prove that A is convex.

4. Prove that $\varphi ^ { \star } = ( I _ { A } ) ^ { \star } + I _ { B _ { E ^ { \prime } } }$ - for every A not necessarily convex.

<u>1.23</u> Inf-convolution.

Let E be an n.v.s. Given two functions $\varphi , \psi : E \to ( - \infty , + \infty ]$ , one defines the inf-convolution of $\varphi$ and $\psi$ as follows: for every $x \in E$ , let

$$
( \varphi \nabla \psi ) ( x ) = \operatorname* { i n f } _ { y \in E } \{ \varphi ( x - y ) + \psi ( y ) \} .
$$

Note the following:

(i) $( \varphi \nabla \psi ) ( x )$ may take the values ±∞,

(ii) $( \varphi \nabla \psi ) ( x ) < + \infty { \mathrm { ~ i f f ~ } } x \in D ( \varphi ) + D ( \psi ) .$

1. Assuming that $D ( \varphi ^ { \star } ) \cap D ( \psi ^ { \star } ) \neq \emptyset ,$ , prove that $( \varphi \nabla \psi )$ does not take the value −∞ and that

$$
( \varphi \nabla \psi ) ^ { \star } = \varphi ^ { \star } + \psi ^ { \star } .
$$

2. Assuming that $D ( \varphi ) \cap D ( \psi ) \neq \emptyset$ , prove that

$$
( \varphi + \psi ) ^ { \star } \leq ( \varphi ^ { \star } \nabla \psi ^ { \star } ) { \mathrm { ~ o n ~ } } E ^ { \star } .
$$

3. Assume that $\varphi$ and $\psi$ are convex and there exists $x _ { 0 } \in D ( \varphi ) \cap D ( \psi )$ such that $\varphi$ is continuous at x<sub>0</sub>. Prove that

$$
( \varphi + \psi ) ^ { \star } = ( \varphi ^ { \star } \nabla \psi ^ { \star } ) { \mathrm { ~ o n ~ } } E ^ { \star } .
$$

4. Assume that $\varphi$ and $\psi$ are convex and l.s.c., and that $D ( \varphi ) \cap D ( \psi ) \neq \emptyset$ . Prove that

$$
( \varphi ^ { \star } \nabla \psi ^ { \star } ) ^ { \star } = ( \varphi + \psi ) \; \mathrm { o n } \; E .
$$

Given a function $\varphi:E\to(-\infty,+\infty]$ , set

$$
\operatorname { e p i s t } \varphi = \{ [ x , \lambda ] \in E \times \mathbb { R } ; \varphi ( x ) < \lambda \} .
$$

5. Check that $\varphi$ is convex iff epist $\varphi$ is a convex subset of $E \times \mathbb { R }$

6. Let $\varphi , \psi : E \to ( - \infty , + \infty ]$ be functions such that $D ( \varphi ^ { \star } ) \cap D ( \psi ^ { \star } ) \neq \emptyset$ . Prove that

$$
\mathsf { e p i s t } ( \varphi \nabla \psi ) = ( \mathsf { e p i s t }   \varphi ) + ( \mathsf { e p i s t }   \psi ) .
$$

7. Deduce that if $\varphi , \psi : E \to ( - \infty , + \infty ]$ are convex functions such that $D ( \varphi ^ { \star } ) \cap$ $D ( \psi ^ { \star } ) \neq \emptyset$ , then $( \varphi \nabla \psi )$ is a convex function.

## 1.24 Regularization by inf-convolution.

Let E be an n.v.s. and let $\varphi : E \to ( - \infty , + \infty ]$ be a convex l.s.c. function such that $\varphi \neq + \infty$ . Our aim is to construct a sequence of functions $( \varphi _ { n } )$ such that we have the following:

(i) For every $n , \varphi _ { n } : E \to ( - \infty , + \infty )$ is convex and continuous.

(ii) For every x, the sequence $( \varphi _ { n } ( x ) ) _ { n }$ is nondecreasing and converges to $\varphi ( x )$

For this purpose, let

$$
\varphi _ { n } ( x ) = \operatorname* { i n f } _ { y \in E } \{ n \| x - y \| + \varphi ( y ) \} .
$$

1. Prove that there is some N, large enough, such that for $n \geq N , \varphi _ { n } ( x )$ is finite for all $x \in E$ . From now on, one chooses $n \geq N$

2. Prove that $\varphi _ { n }$ is convex (see Exercise 1.23) and that

$$
| \varphi _ { n } ( x _ { 1 } ) - \varphi _ { n } ( x _ { 2 } ) | \leq n \| x _ { 1 } - x _ { 2 } \| \quad \forall x _ { 1 } , x _ { 2 } \in E .
$$

3. Determine $\left( \varphi _ { n } \right) ^ { \star }$

4. Check that $\varphi _ { n } ( x ) \leq \varphi ( x ) \quad \forall x \in E$ , ∀n. Prove that for every $x \in E$ , the sequence $( \varphi _ { n } ( x ) ) _ { n }$ is nondecreasing.

5. Given $x \in D ( \varphi )$ , choose $y _ { n } \in E$ such that

$$
\varphi _ { n } ( x ) \leq n \| x - y _ { n } \| + \varphi ( y _ { n } ) \leq \varphi _ { n } ( x ) + { \frac { 1 } { n } } .
$$

Prove that li $\operatorname* { m } _ { n \to \infty } y _ { n } = x$ and deduce that $\operatorname { l i m } _ { n \to \infty } \varphi _ { n } ( x ) = \varphi ( x )$

6. For $x \notin D ( \varphi )$ , prove that lim $\operatorname { \mathfrak { n } } _ { n \to \infty } \varphi _ { n } ( x ) = + \infty$

[**Hint:** Argue by contradiction.]

${ \boxed { 1 . 2 5 } } A$ semiscalar product.

Let E be an n.v.s.

1. Let $\varphi:E\to(-\infty,+\infty)$ be convex. Given $x , y \in E$ , consider the function

$$
h(t) = \frac{\varphi(x + ty) - \varphi(x)}{t}, \quad t > 0.
$$

Check that h is nondecreasing on $( 0 , + \infty )$ and deduce that

$$
\lim_{t \downarrow 0} h(t) = \inf_{t > 0} h(t)   exists in   [-\infty, +\infty).
$$

Define the semiscalar product [x, y] by

$$
[ x , y ] = \operatorname* { i n f } _ { t > 0 } { \frac { 1 } { 2 t } } [ \| x + t y \| ^ { 2 } - \| x \| ^ { 2 } ] .
$$

2. Prove that $| [ x , y ] | \leq \| x \| \| y \| \quad \forall x , y \in E$

3. Prove that

$$
[ x ,   \lambda x + \mu y ] = \lambda \| x \| ^ { 2 } + \mu [ x , y ] \quad \forall x , y \in E , \quad \forall \lambda \in \mathbb { R } , \quad \forall \mu \geq 0
$$

and

$$
[ \lambda x , \mu y ] = \lambda \mu [ x , y ] \quad \forall x , y \in E , \quad \forall \lambda \geq 0 , \quad \forall \mu \geq 0 .
$$

4. Prove that for every $x   \in   E$ , the function $y \mapsto [ x , y ]$ is convex. Prove that the function $G ( x , y ) = - [ x , y ]$ is l.s.c. on $E \times E$

5. Prove that

$$
[ x , y ] = \max_{f \in F(x)} \langle f, y \rangle \quad \forall x, y \in E,
$$

where $F$ denotes the duality map (see Remark 2 following Corollary 1.3 and Exercise 1.1).

[**Hint:** Set $\alpha = [ x , y ]$ and apply Theorem 1.12 to the functions $\varphi$ and $\psi$ defined as follows:

$$
\varphi ( z ) = \frac { 1 } { 2 } \| x + z \| ^ { 2 } - \frac { 1 } { 2 } \| x \| ^ { 2 } , \quad z \in E ,
$$

and

$$
\psi ( z ) = \begin{cases} { - t \alpha \quad } & { \mathrm { w h e n } \; z = t y \; \mathrm { a n d } \; t \geq 0 , } \\ { + \infty \quad } & { \mathrm { o t h e r w i s e . } ] } \end{cases}
$$

6. Determine explicitly $[ x , y ]$ , where $E = \mathbb { R } ^ { n }$ with the norm $\| x \| _ { p } ,   1   \leq   p   \leq   \infty$ (see Section 11.3).

[**Hint:** Use the results of Exercise 1.2.]

<u>1.26</u> Strictly convex norms and functions.

Let E be an n.v.s. One says that the norm is strictly convex (or that the space E is strictly convex) if

$$
\| t x + ( 1 - t ) y \| < 1 , \quad \forall x , y \in E \; { \mathrm { w i t h } } \; x \neq y , \; \| x \| = \| y \| = 1 , \quad \forall t \in ( 0 , 1 ) .
$$

One says that a function $\varphi:E\to(-\infty,+\infty]$ is strictly convex if

$$
\varphi ( t x + ( 1 - t ) y ) < t \varphi ( x ) + ( 1 - t ) \varphi ( y ) \quad \forall x , y \in E \; { \mathrm { w i t h } } \; x \neq y , \quad \forall t \in ( 0 , 1 ) .
$$

1. Prove that the norm is strictly convex iff the function $\varphi ( x ) = \| x \| ^ { 2 }$ is strictly convex.

2. Same question with $\varphi(x)=\|x\|^{p}\mathrm{and}1<p<\infty$

<u>1.27</u> Let E and F be two Banach spaces and let $G   \subset   E$ be a closed subspace. Let ${ \overline { { T } } } : G \to F$ be a continuous linear map. The aim is to show that sometimes, T cannot be extended by a continuous linear map ${ \widetilde { T } } : E \to F$ . For this purpose, let E be a Banach space and let $G \subset E$ be a closed subspace that admits no complement (see Remark 8 in Chapter 2). Let $F = G$ and T = I (the identity map). Prove that T cannot be extended.

[**Hint:** Argue by contradiction.]

Compare with the conclusion of Corollary 1.2.