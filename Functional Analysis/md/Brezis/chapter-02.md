# 2. The Uniform Boundedness Principle and the Closed Graph Theorem


<a id="pdf-page-46"></a>

# Chapter 2

# The Uniform Boundedness Principle and the Closed Graph Theorem

## 2.1 The Baire Category Theorem

The following classical result plays an essential role in the proofs of Chapter 2.

**• Theorem 2.1 (Baire).** *Let $X$ be a complete metric space and let $(X_n)_{n\geq1}$ be a sequence of closed subsets in $X$. Assume that*

$$
\operatorname{Int}X_n=\varnothing \qquad \text{for every }n\geq1.
$$

*Then*

$$
\operatorname{Int}\left(\bigcup_{n=1}^{\infty}X_n\right)=\varnothing.
$$

**Remark 1.** The Baire category theorem is often used in the following form. Let $X$ be a nonempty complete metric space. Let $(X_n)_{n\geq1}$ be a sequence of closed subsets such that

$$
\bigcup_{n = 1}^{\infty} X_{n} = X.
$$

Then there exists some $n_0$ such that $\operatorname{Int}X_{n_0}\ne\varnothing$.

*Proof.* Set $O_n=X_n^c$, so that $O_n$ is open and dense in $X$ for every $n\geq1$. Our aim is to prove that $G=\bigcap_{n=1}^{\infty}O_n$ is dense in $X$. Let $\omega$ be a nonempty open set in $X$; we shall prove that $\omega\cap G\ne\varnothing$.

As usual, set

$$
B ( x , r ) = \{ y \in X ; d ( y , x ) < r \} .
$$

Pick any $x _ { 0 } \in \omega$ and $r _ { 0 } > 0$ such that

$$
\overline { { B ( x _ { 0 } , r _ { 0 } ) } } \subset \omega .
$$

Then, choose $x _ { 1 } \in B ( x _ { 0 } , r _ { 0 } ) \cap O _ { 1 }$ and $r _ { 1 } > 0$ such that



<a id="pdf-page-47"></a>

$$
\begin{cases}\overline{B(x_1, r_1)} \subset B(x_0, r_0) \cap O_1, \\0 < r_1 < \frac{r_0}{2},\end{cases}
$$

which is always possible since $O _ { 1 }$ is open and dense. By induction one constructs two sequences $( x _ { n } )$ and $( r _ { n } )$ such that

$$
\begin{cases}\overline{B(x_{n+1}, r_{n+1})} \subset B(x_n, r_n) \cap O_{n+1}, \quad \forall n \geq 0, \\0 < r_{n+1} < \frac{r_n}{2}.\end{cases}
$$

It follows that $( x _ { n } )$ is a Cauchy sequence; let $x _ { n } \to \ell .$

Since $x _ { n + p }   \in   B ( x _ { n } ,   r _ { n } )$ for every $n \geq 0$ and for every $p \geq 0$ , we obtain at the limit (as $p \to \infty )$

$$
\ell \in \overline { { B ( x _ { n } , r _ { n } ) } } , \quad \forall n \geq 0 .
$$

In particular, $\ell\in\omega\cap G$.

## 2.2 The Uniform Boundedness Principle

**Notation.** Let E and F be two n.v.s. We denote by $\mathcal { L } ( E , F )$ the space of continuous (= bounded) linear operators from E into F equipped with the norm

$$
\left\| T \right\|_{\mathcal{L}(E, F)} = \sup_{\substack{x \in E \\ \| x \| \leq 1}} \| T x \|.
$$

As usual, one writes ${ \mathcal { L } } ( E )$ instead of ${ \mathcal { L } } ( E , E )$

**• Theorem 2.2 (Banach–Steinhaus, uniform boundedness principle).** *Let $E$ and $F$ be two Banach spaces and let $(T_i)_{i\in I}$ be a family (not necessarily countable) of continuous linear operators from $E$ into $F$. Assume that*

$$
\sup_{i \in I} \| T_i x \| < \infty \quad \forall x \in E.\tag{1}
$$

*Then*

$$
\sup_{i \in I} \left\| T_i \right\|_{\mathcal{L}(E,F)} < \infty.\tag{2}
$$

In other words, there exists a constant c such that

$$
\| T _ { i } x \| \leq c \| x \| \quad \forall x \in E , \quad \forall i \in I .
$$

**Remark 2.** The conclusion of Theorem 2.2 is quite remarkable and surprising. From pointwise estimates one derives a global (uniform) estimate.

*Proof.* For every $n\geq1$, let

$$
X _ { n } = \{ x \in E ; \quad \forall i \in I , \quad \| T _ { i } x \| \leq n \} ,
$$



<a id="pdf-page-48"></a>

so that $X _ { n }$ is closed, and by (1) we have

$$
\bigcup_{n = 1}^{\infty} X_{n} = E.
$$

It follows from the Baire category theorem that Int $( X _ { n _ { 0 } } ) \neq \emptyset$ for some $n _ { 0 } \geq 1$ . Pick $x _ { 0 } \in E$ and $r > 0$ such that $B ( x _ { 0 } , r ) \subset X _ { n _ { 0 } }$ . We have

$$
\| T _ { i } ( x _ { 0 } + r z ) \| \leq n _ { 0 } \quad \forall i \in I , \quad \forall z \in B ( 0 , 1 ) .
$$

This leads to

$$
r \left\| T _ { i } \right\| _ { \mathcal { L } ( E , F ) } \leq n _ { 0 } + \| T _ { i } x _ { 0 } \| ,
$$

which implies (2).

**Remark 3.** Recall that in general, a pointwise limit of continuous maps need not be continuous. The linearity assumption plays an essential role in Theorem 2.2. Note, however, that in the setting of Theorem 2.2 it does not follow that $\|T_n-T\|_{\mathcal L(E,F)}\to0$.

Here are a few direct consequences of the uniform boundedness principle.

**Corollary 2.3.** Let E and F be two Banach spaces. Let $( T _ { n } )$ be a sequence of continuous linear operators from E into F such that for every $x   \in   E ,   T _ { n } x$ converges (as $n \to \infty )$ to a limit denoted by Tx. Then we have

(a) $\sup_n\|T_n\|_{\mathcal L(E,F)}<\infty$,

(b) $T \in { \mathcal { L } } ( E , F )$ ,

(c) $\|T\|_{\mathcal L(E,F)}\leq\liminf_{n\to\infty}\|T_n\|_{\mathcal L(E,F)}$.

Proof. (a) follows directly from Theorem 2.2, and thus there exists a constant c such that

$$
\| T _ { n } x \| \leq c \| x \| \quad \forall n , \quad \forall x \in E .
$$

At the limit we find

$$
\| T x \| \leq c \| x \| \quad \forall x \in E .
$$

Since T is clearly linear, we obtain (b).

Finally, we have

$$
\| T _ { n } x \| \leq \| T _ { n } \| _ { \mathcal { L } ( E , F ) } \| x \| \quad \forall x \in E ,
$$

and (c) follows directly.

• **Corollary 2.4.** Let G be a Banach space and let B be a subset of G. Assume that

(3) for every $f \in G ^ { \star }$ the set $f ( B ) = \{ \langle f , x \rangle ;   x \in B \}$ is bounded (in R).

Then

$B$ is bounded. \tag{4}



<a id="pdf-page-49"></a>

Proof. We shall use Theorem 2.2 with $E   =   G ^ { \star } ,   F   =   \mathbb { R }$ , and $I = B$ . For every $b \in B$ , set

$$
T _ { b } ( f ) = \langle f , b \rangle , \quad f \in E = G ^ { \star } ,
$$

so that by (3),

$$
\sup_{b \in B} |T_b(f)| < \infty \quad \forall f \in E.
$$

It follows from Theorem 2.2 that there exists a constant c such that

$$
| \langle f , b \rangle | \leq c \| f \| \quad \forall f \in G ^ { \star } \quad \forall b \in B .
$$

Therefore we find (using Corollary 1.4) that

$$
\| b \| \leq c \quad \forall b \in B .
$$

Remark 4. Corollary 2.4 says that in order to prove that a set B is bounded it suffices to “look” at B through the bounded linear functionals. This is a familiar procedure in finite-dimensional spaces, where the linear functionals are the components with respect to some basis. In some sense, Corollary 2.4 replaces, in infinite-dimensional spaces, the use of components. Sometimes, one expresses the conclusion of Corollary 2.4 by saying that “weakly bounded” ⇐⇒ “strongly bounded” (see Chapter 3).

Next we have a statement dual to Corollary 2.4:

**Corollary 2.5.** Let G be a Banach space and let $B ^ { \star }$ be a subset of $G ^ { \star }$ . Assume that

(5) for every $x \in G$ the set $\langle B ^ { \star } , x \rangle = \{ \langle f , x \rangle ;   f \in B ^ { \star } \}$ is bounded (in R).

Then

$$
B^*\text{ is bounded}.\tag{6}
$$

Proof. Use Theorem 2.2 with $E = G , F = \mathbb { R } ,$ , and $I = B ^ { \star }$ . For every $b \in B ^ { \star }$ set

$$
T _ { b } ( x ) = \langle b , x \rangle \quad ( x \in G = E ) .
$$

We find that there exists a constant c such that

$$
| \langle b , x \rangle | \leq c \| x \| \quad \forall b \in B ^ { \star } , \quad \forall x \in G .
$$

We conclude (from the definition of a dual norm) that

$$
\| b \| \leq c \quad \forall b \in B ^ { \star } .
$$

## 2.3 The Open Mapping Theorem and the Closed Graph Theorem

Here are two basic results due to Banach.



<a id="pdf-page-50"></a>

**• Theorem 2.6 (open mapping theorem).** *Let $E$ and $F$ be two Banach spaces and let $T$ be a continuous linear operator from $E$ into $F$ that is **surjective** (= onto). Then there exists a constant $c>0$ such that*

$$
T ( B _ { E } ( 0 , 1 ) ) \supset B _ { F } ( 0 , c ) .\tag{7}
$$

Remark 5. Property (7) implies that the image under T of any open set in E is an open set in F (which justifies the name given to this theorem!). Indeed, let us suppose $U$ is open in E and let us prove that $T ( U )$ is open. Fix any point $y _ { 0 }   \in   T ( U )$ , so that $y _ { 0 } \; = \; T x _ { 0 }$ for some $x _ { 0 } \; \in \; U$ . Let $r ~ > ~ 0$ be such that $B ( x _ { 0 } , r ) \; \subset \; U ,$ , i.e., $x _ { 0 } + B ( 0 , r ) \subset U$ . It follows that

$$
y _ { 0 } + T ( B ( 0 , r ) ) \subset T ( U ) .
$$

Using (7) we obtain

$$
T ( B ( 0 , r ) ) \supset B ( 0 , r c )
$$

and therefore

$$
B ( y _ { 0 } , r c ) \subset T ( U ) .
$$

Some important consequences of Theorem 2.6 are the following.

• **Corollary 2.7.** Let E and F be two Banach spaces and let T be a continuous linear operator from E into F that is **bijective**, i.e., injective $( = o n e - t o - o n e )$ and surjective. Then $T ^ { - 1 }$ is also continuous (from F into E).

Proof of Corollary 2.7. Property (7) and the assumption that T is injective imply that if $x \in E$ is chosen so that $\| T x \| < c ,$ then $\| x \| < 1$ . By homogeneity, we find that

$$
\| x \| \leq \frac{1}{c} \| T x \| \quad \forall x \in E
$$

and therefore $T ^ { - 1 }$ is continuous.

**Corollary 2.8.** Let $E$ be a vector space provided with two norms, $\|\cdot\|_1$ and $\|\cdot\|_2$. Assume that $E$ is a Banach space for **both** norms and that there exists a constant $C\geq0$ such that

$$
\| x \| _ { 2 } \leq C \| x \| _ { 1 } \quad \forall x \in E .
$$

Then the two norms are **equivalent**, i.e., there is a constant $c > 0$ such that

$$
\| x \| _ { 1 } \leq c \| x \| _ { 2 } \quad \forall x \in E .
$$

Proof of Corollary 2.8. Apply Corollary 2.7 with

$$
E = ( E , \parallel \parallel _ { 1 } ) , F = ( E , \parallel \parallel _ { 2 } ) , \; \mathrm { a n d } \; T = I .
$$

Proof of Theorem 2.6. We split the argument into two steps:

**Step 1.** Assume that T is a linear surjective operator from E onto F. Then there exists a constant $c > 0$ such that



<a id="pdf-page-51"></a>

$$
\overline { { T ( B ( 0 , 1 ) ) } } \supset B ( 0 , 2 c ) .\tag{8}
$$

Proof. Set $X _ { n } = n { \overline { { T ( B ( 0 , 1 ) ) } } }$ . Since T is surjective, we have $\textstyle \bigcup _ { n = 1 } ^ { \infty } X _ { n } = F$ , and by the Baire category theorem there exists some $n _ { 0 }$ such that Int $( X _ { n _ { 0 } } ) \neq \emptyset .$ It follows that

$$
\operatorname{Int}\overline{T(B(0,1))}\ne\varnothing.
$$

Pick $c > 0$ and $y _ { 0 } \in F$ such that

$$
B ( y _ { 0 } , 4 c ) \subset \overline { { T ( B ( 0 , 1 ) ) } } .\tag{9}
$$

In particular, $y _ { 0 } \in \overline { { T ( B ( 0 , 1 ) ) } }$ , and by symmetry,

$$
- y _ { 0 } \in { \overline { { T ( B ( 0 , 1 ) ) } } } .\tag{10}
$$

Adding (9) and (10) leads to

$$
B(0,4c) \subset \overline{T(B(0,1))} + \overline{T(B(0,1))}.
$$

On the other hand, since $\overline { { T ( B ( 0 , 1 ) ) } }$ is convex, we have

$$
\overline { { T ( B ( 0 , 1 ) ) } } + \overline { { T ( B ( 0 , 1 ) ) } } = 2 \overline { { T ( B ( 0 , 1 ) ) } } ,
$$

and (8) follows.

**Step 2.** Assume T is a continuous linear operator from E into F that satisfies (8). Then we have

$$
T ( B ( 0 , 1 ) ) \supset B ( 0 , c ) .\tag{11}
$$

Proof. Choose any $y \in F$ with $\| y \| < c$ . The aim is to find some $x \in E$ such that

$$
\| x \| < 1 \quad { \mathrm { ~ a n d ~ } } \quad T x = y .
$$

By (8) we know that

$$
\forall\varepsilon>0\quad\exists z\in E\text{ with }\|z\|<\frac12\text{ and }\|y-Tz\|<\varepsilon.\tag{12}
$$

Choosing $\varepsilon = c / 2$ , we find some $z _ { 1 } \in E$ such that

$$
\| z _ { 1 } \| < \frac { 1 } { 2 } \quad \mathrm { a n d } \quad \| y - T z _ { 1 } \| < \frac { c } { 2 } .
$$

By the same construction applied to $y - T z _ { 1 }$ (instead of y) with $\varepsilon = c / 4$ we find some $z _ { 2 } \in E$ such that

$$
\| z _ { 2 } \| < \frac { 1 } { 4 } \; \mathrm { a n d } \; \| ( y - T z _ { 1 } ) - T z _ { 2 } \| < \frac { c } { 4 } .
$$

Proceeding similarly, by induction we obtain a sequence $( z _ { n } )$ such that



<a id="pdf-page-52"></a>

$$
\| z _ { n } \| < \frac { 1 } { 2 ^ { n } } \; \mathrm { ~ a n d ~ } \; \| y - T ( z _ { 1 } + z _ { 2 } + \cdots + z _ { n } ) \| < \frac { c } { 2 ^ { n } } \quad \forall n .
$$

It follows that the sequence $x _ { n } = z _ { 1 } + z _ { 2 } + \cdots + z _ { n }$ is a Cauchy sequence. Let $x _ { n } \to x$ with, clearly, $\| x \| < 1$ and $y = T x$ (since T is continuous).

• **Theorem 2.9 (closed graph theorem).** Let E and F be two Banach spaces. Let T be a linear operator from E into F. Assume that the graph of $T ,   G ( T )$ , is closed in $E \times F$ . Then T is continuous.

Remark 6. The converse is obviously true, since the graph of any continuous map (linear or not) is closed.

Proof of Theorem 2.9. Consider, on E, the two norms

$$
\| x \| _ { 1 } = \| x \| _ { E } + \| T x \| _ { F } \quad { \mathrm { a n d } } \quad \| x \| _ { 2 } = \| x \| _ { E }
$$

(the norm $\parallel \parallel _ { 1 }$ is called the graph norm).

It is easy to check, using the assumption that $G ( T )$ is closed, that E is a Banach space for the norm $\parallel \parallel _ { 1 }$ . On the other hand, E is also a Banach space for the norm 2 and $\parallel \parallel _ { 2 } \leq \parallel \parallel _ { 1 }$ . It follows from Corollary 2.8 that the two norms are equivalent and thus there exists a constant $c > 0$ such that $\| x \| _ { 1 } \leq c \| x \| _ { 2 }$ . We conclude that $\| T x \| _ { F } \leq c \| x \| _ { E }$

## 2.4 Complementary Subspaces. Right and Left Invertibility of Linear Operators

We start with some geometric properties of closed subspaces in a Banach space that follow from the open mapping theorem.

**★ Theorem 2.10.** *Let $E$ be a Banach space. Assume that $G$ and $L$ are two closed linear subspaces such that $G+L$ is closed. Then there exists a constant $C\geq0$ such that*

$$
\begin{cases}
\text{every }z\in G+L\text{ admits a decomposition of the form}\\
z=x+y\text{ with }x\in G,\ y\in L,\ \|x\|\leq C\|z\|\text{ and }\|y\|\leq C\|z\|.
\end{cases}\tag{13}
$$

Proof. Consider the product space $G \times L$ with its norm

$$
\| \left[ x , y \right] \| = \| x \| + \| y \|
$$

and the space $G + L$ provided with the norm of $E$ .

The mapping $T : G \times L \to G + L$ defined by $T [ x , y ] = x + y$ is continuous, linear, and surjective. By the open mapping theorem there exists a constant $c > 0$ such that every $z \in G + L$ with $\| z \| < c$ can be written as $z = x + y$ with $x \in G$ $y \in L$ , and $\| x \| + \| y \| < 1$ . By homogeneity every $z \in G + L$ can be written as



<a id="pdf-page-53"></a>

$$
z = x + y \quad { \mathrm { w i t h } } \quad x \in G , y \in L , { \mathrm { a n d } } \quad \| x \| + \| y \| \leq ( 1 / c ) \| z \| .
$$

**★ Corollary 2.11.** *Under the same assumptions as in Theorem 2.10, there exists a constant $C$ such that*

$$
\mathrm { d i s t } ( x , G \cap L ) \leq C \{ \mathrm { d i s t } ( x , G ) + \mathrm { d i s t } ( x , L ) \} \quad \forall x \in E .\tag{14}
$$

Proof. Given $x \in E$ and $\varepsilon > 0$ , there exist $a \in G$ and $b \in L$ such that

$$
\| x - a \| \leq \mathrm{dist}(x, G) + \varepsilon, \| x - b \| \leq \mathrm{dist}(x, L) + \varepsilon.
$$

Property (13) applied to $z = a - b$ says that there exist $a ^ { \prime } \in G$ and $b ^ { \prime } \in L$ such that

$$
a - b = a' + b', \|a'\| \leq C \|a - b\|, \|b'\| \leq C \|a - b\|.
$$

It follows that $a - a ^ { \prime } \in G \cap L$ and

$$
\begin{align*}\mathrm{dist}(x, G \cap L) & \leq \|x - (a - a')\| \leq \|x - a\| + \|a'\| \\& \leq \|x - a\| + C\|a - b\| \leq \|x - a\| + C(\|x - a\| + \|x - b\|) \\& \leq (1 + C)\operatorname{dist}(x, G) + C\operatorname{dist}(x, L) + (1 + 2C)\varepsilon.\end{align*}
$$

Finally, we obtain (14) by letting $\varepsilon \to 0$

Remark 7. The converse of Corollary 2.11 is also true: If G and L are two closed linear subspaces such that (14) holds, then $G + L$ is closed (see Exercise 2.16).

**Definition.** Let $G   \subset   E$ be a closed subspace of a Banach space E. A subspace $L \subset E$ is said to be a topological complement or simply a complement of G if

(i) L is closed,

(ii) $G \cap L = \{ 0 \}$ and $G + L = E$

We shall also say that G and L are complementary subspaces of E. If this holds, then every $z   \in   E$ may be uniquely written as $z = x + y$ with $x   \in   G$ and $y   \in   L$ It follows from Theorem 2.10 that the projection operators $z \mapsto x$ and $z \mapsto y$ are continuous linear operators. (That property could also serve as a definition of complementary subspaces.)

### Examples

1. Every finite-dimensional subspace G admits a complement. Indeed, let $e _ { 1 }$ $e _ { 2 } , \ldots , e _ { n }$ be a basis of G. Every $x \in G$ may be written as $\textstyle x   =   \sum _ { i = 1 } ^ { n } x _ { i } e _ { i }$ Set $\varphi _ { i } ( x ) = x _ { i }$ . Using Hahn–Banach (analytic form)—or more precisely Corollary 1.2—each $\varphi _ { i }$ can be extended by a continuous linear functional $\tilde { \varphi } _ { i }$ defined on E. It is easy to check that $L = \cap _ { i = 1 } ^ { n } ( \widetilde { \varphi } _ { i } ) ^ { - 1 } ( 0 )$ is a complement of $G ,$

2. Every closed subspace G of finite codimension admits a complement. It suffices to choose any finite-dimensional space L such that $G \cap L = \{ 0 \}$ and $G + L = E$ (L is closed since it is finite-dimensional).



<a id="pdf-page-54"></a>
<!-- PDF page 54; unreviewed OCR draft -->

Here is a typical example of this kind of situation. Let $N \subset E ^ { \star }$ be a subspace of dimension $p .$ . Then

$$
G = \{ x \in E ; \langle f , x \rangle = 0 \quad \forall f \in N \} = N ^ { \perp }
$$

is closed and of codimension $p .$ Indeed, let $f _ { 1 } , f _ { 2 } , \ldots , f _ { p }$ be a basis of N. Then there exist $e _ { 1 } , e _ { 2 } , \ldots , e _ { p } \in E$ such that

$$
\langle f _ { i } , e _ { j } \rangle = \delta _ { i j } \quad \forall i ,   j = 1 , 2 , \ldots ,   p .
$$

[Consider the map $\Phi : E \to \mathbb { R } ^ { p }$ defined by

$$
\Phi ( x ) = ( \langle f _ { 1 } , x \rangle , \langle f _ { 2 } , x \rangle , \ldots , \langle f _ { p } , x \rangle )\tag{15}
$$

and note that $\Phi$ is surjective; otherwise, there would exist—by Hahn–Banach (second geometric form)—some $\alpha = ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { p } ) \neq 0$ such that

$$
\alpha \cdot \Phi ( x ) = \left\langle \sum _ { i = 1 } ^ { p } \alpha _ { i }   f _ { i } , x \right\rangle = 0 \quad \forall x \in E ,
$$

which is absurd].

It is easy to check that the vectors $( e _ { i } ) _ { 1 \leq i \leq p }$ are linearly independent and that the space generated by the ${ e _ { i } } ^ { \prime } \mathbf { \dot { s } }$ is a complement of G. Another proof of the fact that the codimension of $N ^ { \perp }$ equals the dimension of N is presented in Chapter 11 (Proposition 11.11).

3. In a Hilbert space every closed subspace admits a complement (see Section 5.2).

Remark 8. It is important to know that some closed subspaces (even in reflexive Banach spaces) have no complement. In fact, a remarkable result of J. Lindenstrauss and L. Tzafriri [1] asserts that in every Banach space that is not isomorphic to a Hilbert space, there exist closed subspaces without any complement.

**Definition.** Let $T \in { \mathcal { L } } ( E , F )$ . A right inverse of T is an operator $S \in { \mathcal { L } } ( F , E )$ such that $T \circ S = I _ { F }$ . A left inverse of T is an operator $S \in { \mathcal { L } } ( F , E )$ such that $S   \circ   T = I _ { E }$

Our next results provide necessary and sufficient conditions for the existence of such inverses.

\- **Theorem 2.12.** Assume that $T \in { \mathcal { L } } ( E , F )$ is **surjective**. The following properties are equivalent:

(i) T admits a right inverse.

(ii) $N ( T ) = T ^ { - 1 } ( 0 )$ admits a complement in E.

Proof.

$( \mathrm { i } ) \Rightarrow ( \mathrm { i i } )$ . Let S be a right inverse of T . It is easy to see (please check) that $R ( S ) = S ( F )$ is a complement of $N ( T )$ in E.



<a id="pdf-page-55"></a>
<!-- PDF page 55; unreviewed OCR draft -->

$( \mathrm { \ddot { u } } ) \Rightarrow ( \mathrm { \dot { i } } )$ . Let L be a complement of $N ( T )$ . Let P be the (continuous) projection operator from E onto L. Given $f \in F$ , we denote by x any solution of the equation $T x = f$ . Set $S f = P x$ and note that S is independent of the choice of x. It is easy to check that $S \in { \mathcal { L } } ( F , E )$ and that $T \circ S = I _ { F }$

Remark 9. In view of Remark 8 and Theorem 2.12, it is easy to construct surjective operators T without a right inverse. Indeed, let $G \subset E$ be a closed subspace without complement, let $F = E / G$ , and let T be the canonical projection from E onto F (for the definition and properties of the quotient space, see Section 11.2).

\- **Theorem 2.13.** Assume that $T   \in   \mathcal { L } ( E , F )$ is **injective**. The following properties are equivalent:

(i) T admits a left inverse.

(ii) $R ( T ) = T ( E )$ is closed and admits a complement in F.

Proof.

$( \mathrm { i } ) \Rightarrow ( \mathrm { i i } )$ . It is easy to check that $R ( T )$ is closed and that $N ( S )$ is a complement of $R ( T )$ [write $f = T S f + ( f - T S f ) ]$

$( \mathrm { \ddot { u } } ) \Rightarrow ( \mathrm { \dot { i } } )$ . Let P be a continuous projection operator from F onto $R ( T )$ . Let $f   \in   F$ ; since $P f   \in   R ( T )$ , there exists a unique $x   \in   E$ such that $Tx = Pf$ . Set $S f = x$ . It is clear that $S \circ T = I _ { E }$ ; moreover, S is continuous by Corollary 2.7.

## - 2.5 Orthogonality Revisited

There are some simple formulas giving the orthogonal expression of a sum or of an intersection.

**Proposition 2.14.** Let G and L be two closed subspaces in E. Then

(16)

$$
\boxed { G \cap L = ( G ^ { \perp } + L ^ { \perp } ) ^ { \perp } , }\tag{17}
$$

$$
\boxed { G ^ { \perp } \cap L ^ { \perp } = ( G + L ) ^ { \perp } . }
$$

Proof of (16). It is clear that $G \cap L   \subset   ( G ^ { \perp } + L ^ { \perp } ) ^ { \perp }$ ; indeed, if $x   \in   G \cap L$ and $f   \in   G ^ { \perp } + L ^ { \perp }$ then $\langle f , x \rangle   =   0$ . Conversely, we have $G ^ { \perp } \subset G ^ { \perp } + L ^ { \perp }$ and thus $\dot { ( } G ^ { \perp } + L ^ { \perp } ) ^ { \perp }   \subset   G ^ { \perp \perp }   =   G$ (note that if $N _ { 1 } \; \subset \; N _ { 2 }$ then $N _ { 2 } ^ { \perp } \; \subset \; N _ { 1 } ^ { \perp } )$ ; similarly $( G ^ { \perp } + L ^ { \perp } ) ^ { \perp } \subset L$ . Therefore $( G ^ { \perp } + L ^ { \perp } ) ^ { \perp } \subset G \cap L$

Proof of (17). Use the same argument as for the proof of (16).

**Corollary 2.15.** Let G and L be two closed subspaces in E. Then

(18)

$$
( G \cap L ) ^ { \perp } \supset \overline { { G ^ { \perp } + L ^ { \perp } } } ,\tag{19}
$$

$$
( G ^ { \perp } \cap L ^ { \perp } ) ^ { \perp } = \overline { { G + L } } .
$$



<a id="pdf-page-56"></a>
<!-- PDF page 56; unreviewed OCR draft -->

## 2.5 Orthogonality Revisited

Proof. Use Propositions 1.9 and 2.14.

Here is a deeper result.

\- **Theorem 2.16.** Let G and L be two closed subspaces in a Banach space E. The following properties are equivalent:

(a) $G + L$ is closed in E,

(b) $G ^ { \perp } + L ^ { \perp }$ is closed in $E ^ { \star }$

(c) $G + L = ( G ^ { \perp } \cap L ^ { \perp } ) ^ { \perp } ,$

(d) $G ^ { \perp } + L ^ { \perp } = ( G \cap L ) ^ { \perp }$

Proof. $( \mathsf { a } ) \Longleftrightarrow ( \mathsf { c } )$ follows from (19). $( \mathsf { d } ) \Longrightarrow ( \mathsf { b } )$ is obvious.

We are left with the implications $( \mathrm { a } ) \Rightarrow ( \mathrm { d } )$ and $( \mathsf { b } ) \Rightarrow ( \mathsf { a } )$

$( \mathsf { a } ) \Longrightarrow ( \mathsf { d } )$ . In view of (18) it suffices to prove that $( G \cap L ) ^ { \perp } \subset G ^ { \perp }   +   L ^ { \perp }$ . Given $f \in ( G \cap L ) ^ { \perp }$ , consider the functional $\varphi : G   +   L \to \mathbb { R }$ defined as follows. For every $x \in G + L$ write $x = a + b$ with $a \in G$ and $b \in L$ . Set

$$
\varphi ( x ) = \langle f , a \rangle .
$$

Clearly, $\varphi$ is independent of the decomposition of x, and $\varphi$ is linear. On the other hand, by Theorem 2.10 we may choose a decomposition of x in such a way that $\| a \| \leq C \| x \|$ , and thus

$$
| \varphi ( x ) | \leq C \| x \| \quad \forall x \in G + L .
$$

Extend $\varphi$ by a continuous linear functional $\tilde { \varphi }$ defined on all of E (see Corollary 1.2). So, we have

$$
f = ( f - \tilde { \varphi } ) + \tilde { \varphi } \quad \mathrm { w i t h } \quad f - \tilde { \varphi } \in G ^ { \perp } \quad \mathrm { a n d } \quad \tilde { \varphi } \in L ^ { \perp } .
$$

$( \mathsf { b } ) \Longrightarrow ( \mathsf { a } )$ . We know by Corollary 2.11 that there exists a constant C such that

$$
\mathsf { d i s t } ( f , G ^ { \perp } \cap L ^ { \perp } ) \leq C \{ \mathsf { d i s t } ( f , G ^ { \perp } ) + \mathsf { d i s t } ( f , L ^ { \perp } ) \} \quad \forall f \in E ^ { \star } .\tag{20}
$$

On the other hand, we have

$$
\mathrm{dist}(f, G^{\perp}) = \sup_{\substack{x \in G \\ \|x\| \leq 1}} \langle f, x \rangle \quad \forall f \in E^{\star}.\tag{21}
$$

[Use Theorem 1.12 with $\varphi ( x ) = I _ { B _ { E } } ( x ) - \langle f , x \rangle$ and $\psi ( x ) = I _ { G } ( x )$ , where

$$
B _ { E } = \{ x \in E ; \| x \| \leq 1 \} . ]
$$

Similarly, we have



<a id="pdf-page-57"></a>
<!-- PDF page 57; unreviewed OCR draft -->

2 The Uniform Boundedness Principle and the Closed Graph Theorem

$$
\mathbf{dist}(f, L^{\perp}) = \sup_{\substack{x \in L \\ \|x\| \leq 1}} \langle f, x \rangle \quad \forall f \in E^{\star}\tag{22}
$$

and also (by (17))

$$
\mathbf{dist}(f, G^{\perp} \cap L^{\perp}) = \mathbf{dist}(f, (G + L)^{\perp}) = \sup_{\substack{x \in \overline{G + L} \\ \|x\| \leq 1}} \langle f, x \rangle \quad \forall f \in E^{\star}.\tag{23}
$$

Combining (20), (21), (22), and (23) we obtain

$$
\sup_{\substack{x \in \overline{G} + L \\ \|x\| \leq 1}} \langle f, x \rangle \leq C \Bigg\{ \sup_{\substack{x \in G \\ \|x\| \leq 1}} \langle f, x \rangle + \sup_{\substack{x \in L \\ \|x\| \leq 1}} \langle f, x \rangle \Bigg\} \quad \forall f \in E^{\star}.\tag{24}
$$

It follows from (24) that

$$
\overline { { B _ { G } + G _ { L } } } \supset \frac { 1 } { C } B _ { \overline { { G + L } } } .\tag{25}
$$

Indeed, suppose <u>by contr</u>adiction that there existed some $x _ { 0 } \in \overline { { G + L } }$ with $\| x _ { 0 } \| \leq$ $1 / C$ and $x _ { 0 }   \notin   \overline { { B _ { G } + B _ { L } } }$ . Then there would be a closed hyperplane in E strictly separating {x0} and $\overline { { B _ { G } + B _ { L } } }$ . Thus, there would exist some $f _ { 0 } \; \in \; E ^ { \star }$ and some $\alpha \in \mathbb { R }$ such that

$$
\langle f _ { 0 } , x \rangle < \alpha < \langle f _ { 0 } , x _ { 0 } \rangle \quad \forall x \in B _ { G } + B _ { L } .
$$

Therefore, we would have

$$
\sup_{\substack{x \in G \\ \|x\| \leq 1}} \langle f_0, x \rangle + \sup_{\substack{x \in L \\ \|x\| \leq 1}} \langle f_0, x \rangle \leq \alpha < \langle f_0, x_0 \rangle,
$$

which contradicts (24), and (25) is proved.

Finally, consider the space $X = G \times L$ with the norm

$$
\| \left[ x , y \right] \| = \max \{ \| x \| , \| y \| \}
$$

and the space $Y   =   \overline { { G + L } }$ with the norm of E. The map $T : X \to Y$ defined by $T ( [ x , y ] ) = x + y$ is linear and continuous. From (25) we know that

$$
\overline { { T ( B _ { X } ) } } \supset \frac { 1 } { C } B _ { Y } .
$$

Using Step 2 from the proof of Theorem 2.6 (open mapping theorem) we conclude that

$$
T ( B _ { X } ) \supset \frac { 1 } { 2 C } B _ { Y } .
$$

It follows that T is surjective from X onto Y , i.e., $G + L = { \overline { { G + L } } }$



<a id="pdf-page-58"></a>
<!-- PDF page 58; unreviewed OCR draft -->

## 2.6 An Introduction to Unbounded Linear Operators. Definition of the Adjoint

**Definition.** Let E and F be two Banach spaces. An unbounded linear operator from E into F is a linear map $A : D ( A ) \subset E \to F$ defined on a linear subspace $D ( A ) \subset E$ with values in F. The set $D ( A )$ is called the domain of A.

One says that A is bounded (or continuous) if $D ( A ) = E$ and if there is a constant $c \geq 0$ such that

$$
\| A u \| \leq c \| u \| \quad \forall u \in E .
$$

The norm of a bounded operator is defined by

$$
\boxed { \left\| A \right\| _ { \mathcal { L } ( E , F ) } = \operatorname* { S u p } _ { u \neq 0 } \frac { \left\| A u \right\| } { \left\| u \right\| } . }
$$

Remark 10. It may of course happen that an unbounded linear operator turns out to be bounded. This terminology is slightly inconsistent, but it is commonly used and does not lead to any confusion.

Here are some important definitions and further notation:

Graph of $A = G ( A ) = \{ [ u , A u ] ; \: u \in D ( A ) \} \subset E \times F ,$

Range of $A = R ( A ) = \{ A u ;   u \in D ( A ) \} \subset F ,$

Kernel of $A = N ( A ) = \{ u \in D ( A ) ;   A u = 0 \} \subset E .$

A map A is said to be closed if $G ( A )$ is closed in $E \times F$

• Remark 11. In order to prove that an operator A is closed, one proceeds in general as follows. Take a sequence $( u _ { n } )$ in $D ( A )$ such that $u _ { n } \to u$ in $E$ and $A u _ { n } \to f$ in $F .$ Then check two facts:

(a) $u \in D ( A )$ ,

(b) $f = A u .$

Note that it does not suffice to consider sequences $( u _ { n } )$ such that $u _ { n } \to 0$ in E and $A u _ { n } \to f$ in $F$ (and to prove that $f = 0 )$

Remark 12. If A is closed, then $N ( A )$ is closed; however, $R ( A )$ need not be closed.

Remark 13. In practice, most unbounded operators are closed and are densely defined, $\mathbf { i . e . , } D ( A )$ is dense in E.

Definition of the adjoint $A ^ { \star }$ . Let $A   :   D ( A )   \subset   E   \to   F$ be an unbounded linear operator that is densely defined. We shall introduce an unbounded operator $A ^ { \star }$ $D ( A ^ { \star } ) \subset F ^ { \star } \to E ^ { \star }$ as follows. First, one defines its domain:

$$
D ( A ^ { \star } ) = \{ v \in F ^ { \star } ; \exists c \geq 0 { \mathrm { ~ s u c h ~ t h a t ~ } } | \langle v , A u \rangle | \leq c \| u \| \quad \forall u \in D ( A ) \} .
$$



<a id="pdf-page-59"></a>
<!-- PDF page 59; unreviewed OCR draft -->

It is clear that $D ( A ^ { \star } )$ is a linear subspace of $F ^ { \star }$ . We shall now define $A ^ { \star } \nu$ . Given $v \in D ( A ^ { \star } )$ , consider the map $g : D ( A ) \to \mathbb { R }$ defined by

$$
g ( u ) = \langle v , A u \rangle \quad \forall u \in D ( A ) .
$$

We have

$$
| g ( u ) | \leq c \| u \| \quad \forall u \in D ( A ) .
$$

By Hahn–Banach (analytic form; see Theorem 1.1) there exists a linear map $f :$ $E \to \mathbb { R }$ that extends g and such that

$$
| f ( u ) | \leq c \| u \| \quad \forall u \in E .
$$

It follows that $f \in E ^ { \star }$ . Note that the extension of $g$ is unique, since $D ( A )$ is dense in $E$ .

Set

$$
A ^ { \star } v = f .
$$

The unbounded linear operator $A ^ { \star } \colon D ( A ^ { \star } ) \subset F ^ { \star } \to E ^ { \star }$ is called the adjoint of A. In brief, the fundamental relation between A and $A ^ { \star }$ is given by

$$
\boxed { \langle v , A u \rangle _ { F ^ { \star } , F } = \langle A ^ { \star } v , u \rangle _ { E ^ { \star } , E } \quad \forall u \in D ( A ) , \quad \forall v \in D ( A ^ { \star } ) . }
$$

Remark 14. It is not necessary to invoke Hahn–Banach to extend $g .$ It suffices to use the classical extension by continuity, which applies since $D ( A )$ is dense, g is uniformly continuous on $D ( A )$ , and R is complete (see, e.g., H. L. Royden [1] (Proposition 11 in Chapter 7) or J. Dugundji [1] (Theorem 5.2 in Chapter XIV).

\- Remark 15. It may happen that $D ( A ^ { \star } )$ is not dense in $F ^ { \star }$ (even if A is closed); but this is a rather pathological situation (see Exercise 2.22). It is always true that if $A$ is closed then $D ( A ^ { \star } )$ is dense in $F ^ { \star }$ for the weak- topology $\sigma ( F ^ { \star } , F )$ defined in Chapter 3 (see Problem 9). In particular, if $F$ is reflexive, then $D ( A ^ { \star } )$ is dense in $F ^ { \star }$ for the usual (norm) topology (see Theorem 3.24).

Remark 16. If A is a bounded operator then $A ^ { \star }$ is also a bounded operator (from $F ^ { \star }$ into $E ^ { \star } )$ and, moreover,

$$
\boxed { \left\| A ^ { \star } \right\| _ { \mathcal { L } ( F ^ { \star } , E ^ { \star } ) } = \left\| A \right\| _ { \mathcal { L } ( E , F ) } . }
$$

Indeed, it is clear that $D ( A ^ { \star } ) = F ^ { \star }$ . From the basic relation, we have

$$
| \langle A ^ { \star } v , u \rangle | \leq \| A \| \| u \| \| v \| \quad \forall u \in E , \quad \forall v \in F ^ { \star } ,
$$

which implies that $\| A ^ { \star } v \| \leq \| A \| \; \| v \|$ and thus $\| A ^ { \star } \| \leq \| A \|$

We also have

$$
| \langle v , A u \rangle | \leq \| A ^ { \star } \| \| u \| \| v \| \quad \forall u \in E , \quad \forall v \in F ^ { \star } ,
$$



<a id="pdf-page-60"></a>
<!-- PDF page 60; unreviewed OCR draft -->

which implies (by Corollary 1.4) that $\| A u \| \leq \| A ^ { \star } \| \; \| u \|$ and thus $\| A \| \leq \| A ^ { \star } \|$

**Proposition 2.17.** Let $A : D ( A ) \subset E \to F$ be a densely defined unbounded linear operator. Then $A ^ { \star }$ is closed, $i . e . ,   G ( A ^ { \star } )$ is closed in $F ^ { \star } \times E ^ { \star }$

Proof. Let $v _ { n } \in D ( A ^ { \star } )$ be such that $v _ { n } \to v$ in $F ^ { \star }$ and $A ^ { \star } v _ { n } \to f$ in $E ^ { \star }$ . One has to check that $( \mathsf { a } ) \; v \in D ( A ^ { \star } )$ and (b) $A ^ { \star } v = f$

We have

$$
\langle v _ { n } , A u \rangle = \langle A ^ { \star } v _ { n } , u \rangle \quad \forall u \in D ( A ) .
$$

At the limit we obtain

$$
\langle v , A u \rangle = \langle f , u \rangle \quad \forall u \in D ( A ) .
$$

Therefore $v \in D ( A ^ { \star } )$ (since $| \langle v , A u \rangle | \leq \| f \| \; \| u \| \; \forall u \in D ( A ) )$ and $A ^ { \star } v = f$

The graphs of A and $A ^ { \star }$ are related by a very simple orthogonality relation: Consider the isomorphism I : $F ^ { \star } \times E ^ { \star } \to E ^ { \star } \times F ^ { \star }$ defined by

$$
I ( [ v , f ] ) = [ - f , v ] .
$$

Let $A : D ( A ) \subset E \to F$ be a densely defined unbounded linear operator. Then

$$
\boxed { I [ G ( A ^ { \star } ) ] = G ( A ) ^ { \perp } . }
$$

Indeed, let $[ v ,   f ] \in F ^ { \star } \times E ^ { \star }$ , then

$$
\begin{align*}[v,   f] \in G(A^{\star}) & \Longleftrightarrow \langle f, u \rangle = \langle v, A u \rangle \quad \forall u \in D(A) \\& \Longleftrightarrow - \langle f, u \rangle + \langle v, A u \rangle = 0 \quad \forall u \in D(A) \\& \Longleftrightarrow [-f, v] \in G(A)^{\perp}.\end{align*}
$$

Here are some standard orthogonality relations between ranges and kernels:

**Corollary 2.18.** Let $A : D ( A ) \subset E \to F$ be an unbounded linear operator that is densely defined and closed. Then

(i)

$$
N ( A ) = R ( A ^ { \star } ) ^ { \perp } ,\tag{ii}
$$

$$
N ( A ^ { \star } ) = R ( A ) ^ { \perp } ,\tag{iii}
$$

$$
N ( A ) ^ { \perp } \supset { \overline { { R ( A ^ { \star } ) } } } ,\tag{iv}
$$

$$
N ( A ^ { \star } ) ^ { \perp } = { \overline { { R ( A ) } } } .
$$

Proof. Note that (iii) and (iv) follow directly from (i) and (ii) combined with Proposition 1.9. There is a simple and direct proof of (i) and (ii) (see Exercise 2.18). However, it is instructive to relate these facts to Proposition 2.14 by the following device. Consider the space $X = E \times F$ , so that $X ^ { \star } = E ^ { \star } \times F ^ { \star }$ , and the subspaces of X



<a id="pdf-page-61"></a>
<!-- PDF page 61; unreviewed OCR draft -->

2 The Uniform Boundedness Principle and the Closed Graph Theorem

$$
G = G ( A ) \quad \mathrm { a n d } \quad L = E \times \{ 0 \} .
$$

It is very easy to check that

(26)

$$
N ( A ) \times \{ 0 \} = G \cap L ,\tag{27}
$$

$$
E \times R ( A ) = G + L ,\tag{28}
$$

$$
\{ 0 \} \times N ( A ^ { \star } ) = G ^ { \perp } \cap L ^ { \perp } ,\tag{29}
$$

$$
R ( A ^ { \star } ) \times F ^ { \star } = G ^ { \perp } + L ^ { \perp } .
$$

Proof of (i). By (29) we have

$$
\begin{align*}R(A^{\star})^{\perp} \times \{0\} &= (G^{\perp} + L^{\perp})^{\perp} = G \cap L \quad (\mathsf{by} \; (16)) \\&= N(A) \times \{0\} \quad (\mathsf{by} \; (26)).\end{align*}
$$

Proof of (ii). By (27) we have

$$
\begin{align*}\left\{ 0 \right\} \times R(A)^{\perp} = (G + L)^{\perp} &= G^{\perp} \cap L^{\perp} \quad (\mathsf{by} \left( 17 \right)) \\&= \left\{ 0 \right\} \times N(A^{\star}) \quad (\mathsf{by} \left( 28 \right)).\end{align*}
$$

<u>Remar</u>k 17. It may happen, even if A is a bounded linear operator, that $N(A)^{\perp} \neq$ $\overline { { R ( A ^ { \star } ) } }$ (see Exercise 2.23). However, it is always true that $N ( A ) ^ { \perp }$ is the closure of $R ( A ^ { \star } )$ for the weak- <u>topolo</u>gy $\sigma ( E ^ { \star } , E )$ (see Problem 9). In particular, if $E$ is reflexive then $N ( A ) ^ { \perp } = { \overline { { R ( A ^ { \star } ) } } }$

## - 2.7 A Characterization of Operators with Closed Range. A Characterization of Surjective Operators

The main result concerning operators with closed range is the following.

\- **Theorem 2.19.** Let $A : D ( A ) \subset E \to F$ be an unbounded linear operator that is densely defined and closed. The following properties are equivalent:

(i) $R ( A )$ is closed,

(ii) $R ( A ^ { \star } )$ is closed,

(iii) $R(A)=N(A^{\star})^{\perp}$

(iv) $R ( A ^ { \star } ) = N ( A ) ^ { \perp }$

Proof. With the same notation as in the proof of Corollary 2.18, we have

(i) $\Leftrightarrow G + L$ is closed in X (see (27)),

(ii) $\Leftrightarrow G ^ { \perp } + L ^ { \perp }$ is closed in $X ^ { \star } \left( \sec \left( 2 9 \right) \right)$ ),

(iii) $\Leftrightarrow G + L = ( G ^ { \perp } \cap L ^ { \perp } ) ^ { \perp }$ (see (27) and (28)),

(iv) $\Leftrightarrow ( G \cap L ) ^ { \perp } = G ^ { \perp } + L ^ { \perp }$ (see (26) and (29)).

The conclusion then follows from Theorem 2.16.



<a id="pdf-page-62"></a>
<!-- PDF page 62; unreviewed OCR draft -->

Remark 18. Let $A : D ( A ) \subset E \to F$ be a closed unbounded linear operator. Then $R ( A )$ is closed if and only if there exists a constant C such that

$$
\mathbf{dist}(u, N(A)) \leq C \|Au\| \quad \forall u \in D(A);
$$

see Exercise 2.14.

The next result provides a useful characterization of surjective operators.

\- **Theorem 2.20.** Let $A : D ( A ) \subset E \to F$ be an unbounded linear operator that is densely defined and closed. The following properties are equivalent:

(a) A is surjective, i.e., $R ( A ) = F$

(b) there is a constant C such that

$$
\| v \| \leq C \| A ^ { \star } v \| \quad \forall v \in D ( A ^ { \star } ) ,
$$

(c) $N ( A ^ { \star } ) = \{ 0 \}$ and R(A-) is closed.

Remark 19. The implication $( \mathsf { b } ) \Rightarrow ( \mathsf { a } )$ is sometimes useful in practice to establish that an operator A is surjective. One proceeds as follows. Assuming that v satisfies $A ^ { \star } v   =   f$ , one tries to prove that $\| v \|   \leq   C \| f \|$ (with C independent of f ). This is called the method of a priori estimates. One is not concerned with the question whether the equation $A ^ { \star } v = f$ admits a solution; one assumes that v is a priori given and one tries to estimate its norm.

Proof.

(a) ⇒ (b). Set

$$
B ^ { \star } = \{ v \in D ( A ^ { \star } ) ;   \| A ^ { \star } v \| \leq 1 \} .
$$

By homogeneity it suffices to prove that $B ^ { \star }$ is bounded. For this purpose—in view of Corollary 2.5 (uniform boundedness principle)—we have only to show that given any $f _ { 0 } \in F$ the set $\langle B ^ { \star } ,   f _ { 0 } \rangle$ is bounded (in R). Since A is surjective, there is some $u _ { 0 } \in D ( A )$ such that $A u _ { 0 } = f _ { 0 }$ . For every $v \in B ^ { \star }$ we have

$$
\langle v ,   f _ { 0 } \rangle = \langle v , A u _ { 0 } \rangle = \langle A ^ { \star } v , u _ { 0 } \rangle
$$

and thus $| \langle v ,   f _ { 0 } \rangle | \leq \| u _ { 0 } \|$

(b) ⇒ (c). Suppose $f _ { n } = A ^ { \star } v _ { n } \to f$ . Using (b) with $v _ { n } - v _ { m }$ we see that $( v _ { n } )$ is Cauchy, so that $v _ { n } \to v$ . Since $A ^ { \star }$ is closed (by Proposition 2.17), we conclude that $A ^ { \star } v = f .$

$( \mathrm { c } ) \Rightarrow ( \mathrm { a } )$ . Since $R ( A ^ { \star } )$ is closed, we infer from Theorem 2.19 that $R(A)   =$ $N ( A ^ { \star } ) ^ { \perp } = F$

There is a “dual” statement.

\- **Theorem 2.21.** Let $A : D ( A ) \subset F$ be an unbounded linear operator that is densely defined and closed. The following properties are equivalent:



<a id="pdf-page-63"></a>
<!-- PDF page 63; unreviewed OCR draft -->

(a) $A ^ { \star }$ is surjective, i.e., $R ( A ^ { \star } ) = E ^ { \star }$

(b) there is a constant C such that

$$
\| u \| \leq C \| A u \| \quad \forall u \in D ( A ) ,
$$

(c) $N ( A ) = \{ 0 \}$ and R(A) is closed.

Proof. It is similar to the proof of Theorem 2.20 and we shall leave it as an exercise.

Remark 20. If one assumes that either dim $E   <   \infty \; o r$ that dim $F   <   \infty$ , then the following are equivalent:

$$
\begin{aligned}A  surjective  & \Leftrightarrow A^{\star}  injective , \\A^{\star}  surjective  & \Leftrightarrow A  injective ,\end{aligned}
$$

which is indeed a classical result for linear operators in finite-dimensional spaces. The reason that these equivalences hold is that $R ( A )$ and $R ( A ^ { \star } )$ are finite-dimensional (and thus closed).

In the general case one has only the implications

$$
\begin{aligned}A\  surjective  & \Rightarrow A^{\star}\  injective , \\A^{\star}\  surjective  & \Rightarrow A\  injective .\end{aligned}
$$

The converses fail, as may be seen from the following simple example. Let $E =$ $F = \ell ^ { 2 }$ ; for every $x \in \ell ^ { 2 }$ write $x = ( x _ { n } ) _ { n \geq 1 }$ and set $\begin{array} { r } { A x = \left( \frac { 1 } { n } x _ { n } \right) _ { n \geq 1 } } \end{array}$ . It is easy to see that A is a bounded operator and that $A ^ { \star } = A ;   A ^ { \star }$ (resp. A) is injective but A (resp. A-) is not surjective; $R ( A )$ (resp. $R ( A ^ { \star } ) )$ is dense and not closed.

## Comments on Chapter 2

**1.** One may write down explicitly some simple closed subspaces without complement. For example $c _ { 0 }$ is a closed subspace of $\ell ^ { \infty }$ without complement; see, e.g., C. DeVito [1] (the notation $c _ { 0 }$ and $\ell ^ { \infty }$ is explained in Section 11.3). There are other examples in W. Rudin [1] (a subspace of $L ^ { \hat { 1 } } )$ , G. Köthe [1], and B. Beauzamy [1] (a subspace of $\ell ^ { p } ,   p \neq 2 )$

**2.** Most of the results in Chapter 2 extend to Fréchet spaces (locally convex spaces that are metrizable and complete). There are many possible extensions; see, e.g., H. Schaefer [1], J. Horváth [1], R. Edwards [1], F. Treves [1], [3], G. Köthe [1]. These extensions are motivated by the theory of distributions (see L. Schwartz [1]), in which many important spaces are not Banach spaces. For the applications to the theory of partial differential equations the reader may consult L. Hörmander [1] or F. Treves [1], [2], [3].

**3.** There are various extensions of the results of Section 2.5 in T. Kato [1].



<a id="pdf-page-64"></a>
<!-- PDF page 64; unreviewed OCR draft -->

## Exercises for Chapter 2

<u>2.1</u> Continuity of convex functions.

Let E be a Banach space and let $\varphi:E\to(-\infty,+\infty]$ be a convex l.s.c. function. Assume $x _ { 0 } \in \mathbf { I n t } D ( \varphi )$

1. Prove that there exist two constants $R > 0$ and M such that

$$
\varphi ( x ) \leq M \quad \forall x \in E { \mathrm { ~ w i t h ~ } } \| x - x _ { 0 } \| \leq R .
$$

[**Hint**: Given an appropriate $\rho > 0$ , consider the sets

$$
F _ { n } = \{ x \in E ; \quad \| x - x _ { 0 } \| \leq \rho \mathrm { a n d } \varphi ( x ) \leq n \} . ]
$$

2. Prove that $\forall r < R , \exists L \geq 0$ such that

$$
| \varphi ( x _ { 1 } ) - \varphi ( x _ { 2 } ) | \leq L \| x _ { 1 } - x _ { 2 } \| \quad \forall x _ { 1 } , x _ { 2 } \in E \quad { \mathrm { w i t h } } \quad \| x _ { i } - x _ { 0 } \| \leq r , \quad i = 1 , 2 .
$$

More precisely, one may choose $\begin{array} { r } { L = \frac { 2 [ M - \varphi ( x _ { 0 } ) ] } { R - r } } \end{array}$

<u>2.2</u> Let E be a vector space and let $p : E \to \mathbb { R }$ be a function with the following three properties:

(i) $p ( x + y ) \leq p ( x ) + p ( y )   \forall x , y \in E ,$

(ii) for each fixed $x \in E$ the function $\lambda \mapsto p ( \lambda x )$ is continuous from R into R,

(iii) whenever a sequence $( y _ { n } )$ in E satisfies $p ( y _ { n } ) \rightarrow 0$ , then $p ( \lambda y _ { n } ) \rightarrow 0$ for every $\lambda \in \mathbb { R }$

Assume that $( x _ { n } )$ is a sequence in E such that $p ( x _ { n } ) \rightarrow 0$ and $( \alpha _ { n } )$ is a bounded sequence in R. Prove that $p ( 0 ) = 0$ and that $p ( \alpha _ { n } x _ { n } ) \rightarrow 0 .$

[**Hint**: Given $\varepsilon > 0$ consider the sets

$$
F _ { n } = \{ \lambda \in \mathbb { R } ; \quad | p ( \lambda x _ { k } ) | \leq \varepsilon , \quad \forall k \geq n \} . ]
$$

Deduce that if $( x _ { n } )$ is a sequence in E such that $p ( x _ { n } - x ) \to 0$ for some $x   \in   E$ and $( \alpha _ { n } )$ is a sequence in R such that $\alpha _ { n } \to \alpha$ , then $p ( \alpha _ { n } x _ { n } ) \to p ( \alpha x )$

<u>2.3</u> Let E and F be two Banach spaces and let $( T _ { n } )$ be a sequence in $\mathcal { L } ( E , F )$ Assume that for every $x \in E ,   T _ { n } x$ converges as $n \to \infty$ to a limit denoted by $T x$ Show that if $x _ { n } \to x$ in E, then $T _ { n } x _ { n } \to T x$ in F.

<u>2.4</u> Let E and F be two Banach spaces and let $a : E \times F \to \mathbb { R }$ be a bilinear form satisfying:

(i) for each fixed $x \in E$ , the map $y \mapsto a ( x , y )$ is continuous;

(ii) for each fixed $y \in F$ , the map $x \mapsto a ( x , y )$ is continuous.

Prove that there exists a constant $C \geq 0$ such that

$$
| a ( x , y ) | \leq C \| x \| \| y \| \quad \forall x \in E , \quad \forall y \in F .
$$



<a id="pdf-page-65"></a>
<!-- PDF page 65; unreviewed OCR draft -->

[**Hint**: Introduce a linear operator $T : E \to F ^ { \star }$ and prove that T is bounded with the help of Corollary 2.5.]

<u>2.5</u> Let E be a Banach space and let $\varepsilon _ { n }$ be a sequence of positive numbers such that lim $\varepsilon _ { n } = 0$ . Further, let $( f _ { n } )$ be a sequence in $E ^ { \star }$ satisfying the property

$$
\begin{cases}\exists r > 0, \quad \forall x \in E \quad  with  \|x\| < r, \; \exists C(x) \in \mathbb{R} \quad  such that  \\\langle f_n, x \rangle \leq \varepsilon_n \|f_n\| + C(x) \quad \forall n.\end{cases}
$$

Prove that $( f _ { n } )$ is bounded.

[**Hint**: Introduce $g _ { n } = f _ { n } / ( 1 + \varepsilon _ { n } \|   f _ { n } \| ) . ]$

<u>2.6</u> Locally bounded nonlinear monotone operators.

Let E be Banach space and let $D ( A )$ be any subset in E. A (nonlinear) map $A : D ( A ) \subset E \to E ^ { \star }$ is said to be monotone if it satisfies

$$
\langle A x - A y , x - y \rangle \geq 0 \quad \forall x , y \in D ( A ) .
$$

1. Let $x _ { 0 } \in \mathbf { I n t } D ( A )$ . Prove that there exist two constants $R > 0$ and C such that

$$
\| A x \| \leq C \quad \forall x \in D ( A ) { \mathrm { ~ w i t h ~ } } \| x - x _ { 0 } \| < R .
$$

[**Hint**: Argue by contradiction and construct a sequence $( x _ { n } )$ in $D ( A )$ such that $x _ { n } \to x _ { 0 }$ and $\| A x _ { n } \| \to \infty$ . Choose $r > 0$ such that $B ( x _ { 0 } , r ) \subset D ( A )$ . Use the monotonicity of A at $x _ { n }$ and at $( x _ { 0 } + x )$ with $\| x \| < r .   \mathrm { A p p l y }$ Exercise 2.5.]

2. Prove the same conclusion for a point x<sub>0</sub> ∈ Int[conv D(A)].

3. Extend the conclusion of question 1 to the case of A multivalued, i.e., for every $x \in D ( A )$ , Ax is a nonempty subset of $E ^ { \star }$ ; the monotonicity is defined as follows:

$$
\langle f - g, x - y \rangle \geq 0 \quad \forall x, y \in D(A), \quad \forall f \in Ax, \quad \forall g \in Ay.
$$

$\lceil 2 . 7 \rceil$ Let $\alpha = ( \alpha _ { n } )$ be a given sequence of real numbers and let $1 \leq p \leq \infty$ . Assume that $\textstyle \sum | \alpha _ { n } | | x _ { n } | <$ ∞ for every element $x = ( x _ { n } )$ in $\ell ^ { p }$ (the space $\ell ^ { p }$ is defined in Section 11.3).

Prove that $\alpha \in \ell ^ { p ^ { \prime } }$

<u>2.8</u> Let E be a Banach space and let $T : E \to E ^ { \star }$ be a linear operator satisfying

$$
\langle T x , x \rangle \geq 0 \quad \forall x \in E .
$$

Prove that T is a bounded operator.

[Two methods are possible: (i) Use Exercise 2.6 or (ii) Apply the closed graph theorem.]

<u>2.9</u> Let E be a Banach space and let $T : E \to E ^ { \star }$ be a linear operator satisfying

$$
\langle T x , y \rangle = \langle T y , x \rangle \quad \forall x , y \in E .
$$



<a id="pdf-page-66"></a>
<!-- PDF page 66; unreviewed OCR draft -->

Prove that T is a bounded operator.

<u>2.10</u> Let E and F be two Banach spaces and let $T \in { \mathcal { L } } ( E , F )$ be surjective.

1. Let M be any subset of E. Prove that $T ( M )$ is closed in $F \mathrm { i f f } M + N ( T )$ is closed in E.

2. Deduce that if M is a closed vector space in E and dim $N ( T ) < \infty$ , then $T ( M )$ is closed.

<u>2.11</u> Let E be a Banach space, $F = \ell ^ { 1 }$ , and let $T \in { \mathcal { L } } ( E , F )$ be surjective. Prove that there exists $S \in { \mathcal { L } } ( F , E )$ such that $T \circ S = I _ { F } , \mathrm { i . e . , } S$ has a right inverse of $T$ .

[**Hint**: Do not apply Theorem 2.12; try to define S explicitly using the canonical basis of $\ell ^ { 1 }$ .]

<u>2.12</u> Let E and F be two Banach spaces with norms $\parallel \parallel E$ and $\parallel \parallel F$ . Let $T \in$ $\overline { { \mathcal { L } ( E , F ) } }$ be such that $R ( T )$ is closed and dim $N ( T )   <   \infty . \; \mathrm { L e t } \mid \mid$ denote another norm on E that is weaker than $\| \|_{E}, \mathrm{i.e.}, |x| \leq M \|x\|_{E} \forall x \in E$

Prove that there exists a constant C such that

$$
\| x \| _ { E } \leq C ( \| T x \| _ { F } + | x | ) \quad \forall x \in E .
$$

[**Hint**: Argue by contradiction.]

<u>2.13</u> Let E and F be two Banach spaces. Prove that the set

$$
\Omega = \{ T \in { \mathcal { L } } ( E , F ) ; \quad T \quad { \mathrm { a d m i t s ~ a ~ l e f t ~ i n v e r s e } } \}
$$

is open in $\mathcal { L } ( E , F )$

[**Hint**: Prove first that the set

$$
\mathcal { O } = \{ T \in \mathcal { L } ( E , F ) ; T { \mathrm { ~ i s ~ b i j e c t i v e } } \}
$$

is open in $\mathcal { L } ( E , F ) . ]$

<u>2.14</u> Let E and F be two Banach spaces

1. Let $T   \in   \mathcal { L } ( E ,   F )$ . Prove that $R ( T )$ is closed iff there exists a constant C such that

$$
\mathbf { d i s t } ( x , N ( T ) ) \leq C \| T x \| \quad \forall x \in E .
$$

[**Hint**: Use the quotient space $E / N ( T )$ ; see Section 11.2.]

2. Let $A : D ( A ) \subset E \to F$ be a closed unbounded operator.

Prove that $R ( A )$ is closed iff there exists a constant C such that

$$
\mathbf { d i s t } ( u , N ( A ) ) \leq C \| A u \| \quad \forall u \in D ( A ) .
$$

[**Hint**: Consider the operator $T : E _ { 0 } \to F$ , where $E _ { 0 } = D ( A )$ with the graph norm and $T = A . ]$



<a id="pdf-page-67"></a>
<!-- PDF page 67; unreviewed OCR draft -->

<u>2.15</u> Let $E _ { 1 } , \; E _ { 2 }$ , and F be three Banach spaces. Let $T _ { 1 } \; \in \; \mathcal { L } ( E _ { 1 } , F )$ and let $T _ { 2 } \in \mathcal { L } ( E _ { 2 } , F )$ be such that

$$
R ( T _ { 1 } ) \cap R ( T _ { 2 } ) = \{ 0 \} \quad { \mathrm { a n d } } \quad R ( T _ { 1 } ) + R ( T _ { 2 } ) = F .
$$

Prove that $R ( T _ { 1 } )$ and $R ( T _ { 2 } )$ are closed.

[**Hint**: Apply Exercise 2.10 to the map $T : E _ { 1 } \times E _ { 2 } \to F$ defined by

$$
T ( x _ { 1 } , x _ { 2 } ) = T _ { 1 } x _ { 1 } + T _ { 2 } x _ { 2 } . ]
$$

<u>2.16</u> Let E be a Banach space. Let G and L be two closed subspaces of E. Assume that there exists a constant C such that

$$
\operatorname { d i s t } ( x , G \cap L ) \leq C \operatorname { d i s t } ( x , L ) , \quad \forall x \in G .
$$

Prove that $G + L$ is closed.

<u>2.17</u> Let $E = C ( [ 0 , 1 ] )$ with its usual norm. Consider the operator $A : D ( A ) \subset$ $E \to E$ defined by

$$
D ( A ) = C ^ { 1 } ( [ 0 ,   1 ] ) \quad \mathrm { a n d } \quad A u = u ^ { \prime } = \frac { d u } { d t } .
$$

1. Check that ${ \overline { { D ( A ) } } } = E$

2. Is A closed?

3. Consider the operator $B : D ( B ) \subset E \to E$ defined by

$$
D ( B ) = C ^ { 2 } ( [ 0 , 1 ] ) \quad \mathrm { a n d } \quad B u = u ^ { \prime } = \frac { d u } { d t } .
$$

Is B closed?

<u>2.18</u> Let E and F be two Banach spaces and let $A : D ( A ) \subset E \to F$ be a densely defined unbounded operator.

1. Prove that $N(A^{\star}) = R(A)^{\perp}   and   N(A) \subset R(A^{\star})^{\perp}$

2. Assuming that A is also closed prove that $N(A)=R(A^{\star})^{\perp}$

[Try to find direct arguments and do not rely on the proof of Corollary 2.18. For question 2 argue by contradiction: suppose there is some $u \in R ( A ^ { \star } ) ^ { \perp }$ such that $[ u , 0 ] \notin G ( A )$ and apply Hahn–Banach.]

<u>2.19</u> Let E be a Banach space and let $A : D ( A ) \subset E \to E ^ { \star }$ be a densely defined unbounded operator.

1. Assume that there exists a constant C such that

(1)

$$
\langle A u , u \rangle \geq - C \| A u \| ^ { 2 } \quad \forall u \in D ( A ) .
$$

Prove that $N ( A ) \subset N ( A ^ { \star } )$



<a id="pdf-page-68"></a>
<!-- PDF page 68; unreviewed OCR draft -->

2. Conversely, assume that $N ( A ) \subset N ( A ^ { \star } )$ . Also, assume that A is closed and $R ( A )$ is closed. Prove that there exists a constant C such that (1) holds.

<u>2.20</u> Let E and F be two Banach spaces. Let $T \in { \mathcal { L } } ( E , F )$ and let $A : D ( A ) \subset$ $E \rightarrow F$ be an unbounded operator that is densely defined and closed. Consider the operator $B : D ( B ) \subset E \to F$ defined by

$$
D(B)=D(A), \quad B=A+T.
$$

1. Prove that B is closed.

2. Prove that $D ( B ^ { \star } ) = D ( A ^ { \star } )$ and $B ^ { \star } = A ^ { \star } + T ^ { \star }$

<u>2.21</u> Let E be an infinite-dimensional Banach space. Fix an element $a \in E , a \neq 0$ and a discontinuous linear functional $f : E \to \mathbb { R }$ (such functionals exist; see Exercise 1.5). Consider the operator $A : E \to E$ defined by

$$
D ( A ) = E , \quad A x = x - f ( x ) a .
$$

1. Determine $N ( A )$ and $R ( A )$

2. Is A closed?

3. Determine $A ^ { \star }$ (define $D ( A ^ { \star } )$ carefully).

4. Determine N (A-) and $R ( A ^ { \star } )$

5. Compare N (A) with $R ( A ^ { \star } ) ^ { \perp }$ as well as $N ( A ^ { \star } )$ with $R ( A ) ^ { \perp }$

6. Compare with the results of Exercise 2.18.

<u>2.22</u> The purpose of this exercise is to construct an unbounded operator A : $D ( A ) \subset$ $E \to E$ that is densely defined, closed, and such that $\overline { { D ( A ^ { \star } ) } } \neq E ^ { \star }$

Let $E   =   \ell ^ { 1 }$ , so that $E ^ { \star }   =   \ell ^ { \infty }$ . Consider the operator $A   :   D ( A )   \subset   E   \to   E$ defined by

$$
D ( A ) = \left\{ u = ( u _ { n } ) \in \ell ^ { 1 } ; ( n u _ { n } ) \in \ell ^ { 1 } \right\}   \mathrm { a n d }   A u = ( n u _ { n } ) .
$$

1. Check that A is densely defi<u>ned an</u>d closed.

2. Determine $D ( A ^ { \star } ) ,   A ^ { \star }$ , and $\overline { { D ( A ^ { \star } ) } }$

<u>2.23</u> Let $E = \ell ^ { 1 }$ , so that $E ^ { \star } = \ell ^ { \infty }$ . Consider the operator $T \in { \mathcal { L } } ( E , E )$ defined by

$$
Tu = \left( \frac{1}{n} u_n \right)_{n \geq 1}   for every   u = (u_n)_{n \geq 1}   in   \ell^1.
$$

Determine $N ( T ) ,   N ( T ) ^ { \perp } ,   T ^ { \star } ,   R ( T ^ { \star } )$ , and $\overline { { R ( T ^ { \star } ) } }$

Compare with Corollary 2.18.



<a id="pdf-page-69"></a>
<!-- PDF page 69; unreviewed OCR draft -->

<u>2.24</u> Let E, F, and G be three Banach spaces. Let $A   :   D ( A )   \subset   E   \to   F$ be a densely defined unbounded operator. Let $T   \in   { \mathcal { L } } ( F , G )$ and consider the operator $B : D ( B ) \subset E \to G$ defined by $D(B)=D(A)$ and $B = T \circ A$

1. Determine $B ^ { \star }$

2. Prove (by an example) that B need not be closed even if A is closed.

<u>2.25</u> Let E, F, and G be three Banach spaces.

1. Let $T \in { \mathcal { L } } ( E , F )$ and $S \in { \mathcal { L } } ( F , G )$ . Prove that

$$
( S \circ T ) ^ { \star } = T ^ { \star } \circ S ^ { \star } .
$$

2. Assume that $T \in { \mathcal { L } } ( E , F )$ is bijective. Prove that $T ^ { \star }$ is bijective and that $( T ^ { \star } ) ^ { - 1 } =$ $( T ^ { - 1 } ) ^ { \star }$

<u>2.26</u> Let E and F be two Banach spaces and let $T   \in   \mathcal { L } ( E , F )$ . Let $\psi : F \to$ $(-\infty, +\infty]$ be a convex function. Assume that there exists some element in $R ( T )$ where ψ is finite and continuous.

Set

$$
\varphi(x) = \psi(Tx), \quad x \in E.
$$

Prove that for every $f \in F ^ { \star }$

$$
\varphi ^ { \star } ( T ^ { \star } f ) = \operatorname* { i n f } _ { g \in N ( T ^ { \star } ) } \; \psi ^ { \star } ( f - g ) = \operatorname* { m i n } _ { g \in N ( T ^ { \star } ) } \; \psi ^ { \star } ( f - g ) .
$$

<u>2.27</u> Le E, F be two Banach spaces and let $T \in { \mathcal { L } } ( E , F )$ . Assume that $R ( T )$ has finite codimension, i.e., there exists a finite-dimensional subspace X of F such that $X + R ( T ) = F$ and $X \cap R ( T ) = \{ 0 \}$

Prove that R(T ) is closed.

