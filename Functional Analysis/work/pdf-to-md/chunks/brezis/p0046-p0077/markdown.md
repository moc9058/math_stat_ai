# Chapter 2 The Uniform Boundedness Principle and the Closed Graph Theorem

## 2.1 The Baire Category Theorem

The following classical result plays an essential role in the proofs of Chapter 2.

• **Theorem 2.1 (Baire).** Let X be a complete metric space and let $( X _ { n } ) _ { n \geq 1 }$ be a sequence of closed subsets in X. Assume that

$$
\operatorname { I n t } X _ { n } = \emptyset \quad { \it f o r ~ e v e r y } \quad n \geq 1 .
$$

Then

$$
\operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { \operatorname { } } } } I n t } } } } } } } } } } \left( \bigcup _ { n = 1 } ^ { \infty } X _ { n } \right) = \varnothing .
$$

Remark 1. The Baire category theorem is often used in the following form. Let X be a nonempty complete metric space. Let $( X _ { n } ) _ { n \geq 1 }$ be a sequence of closed subsets such that

$$
\bigcup_{n = 1}^{\infty} X_{n} = X.
$$

Then there exists some $n _ { 0 }$ such that Int $X _ { n _ { 0 } } \neq \emptyset .$

Proof. Set $O _ { n } = X _ { n } ^ { c } ,$ , so that $O _ { n }$ is open and dense in X for every $n \geq 1$ . Our aim is to prove that $\begin{array} { r } { G = \bigcap _ { n = 1 } ^ { \infty } O _ { n } } \end{array}$ is dense in X. Let $\omega$ be a nonempty open set in X; we shall prove that $\omega \cap G \neq \emptyset$

As usual, set

$$
B ( x , r ) = \{ y \in X ; d ( y , x ) < r \} .
$$

Pick any $x _ { 0 } \in \omega$ and $r _ { 0 } > 0$ such that

$$
\overline { { B ( x _ { 0 } , r _ { 0 } ) } } \subset \omega .
$$

Then, choose $x _ { 1 } \in B ( x _ { 0 } , r _ { 0 } ) \cap O _ { 1 }$ and $r _ { 1 } > 0$ such that

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

In particular, $\ell \in \omega \cap G$

## 2.2 The Uniform Boundedness Principle

**Notation.** Let E and F be two n.v.s. We denote by $\mathcal { L } ( E , F )$ the space of continuous (= bounded) linear operators from E into F equipped with the norm

$$
\left\| T \right\|_{\mathcal{L}(E, F)} = \sup_{\substack{x \in E \\ \| x \| \leq 1}} \| T x \|.
$$

As usual, one writes ${ \mathcal { L } } ( E )$ instead of ${ \mathcal { L } } ( E , E )$

• **Theorem 2.2 (Banach–Steinhaus, uniform boundedness principle).** Let E and F be two Banach spaces and let $( T _ { i } ) _ { i \in I }$ be a family (not necessarily countable) of continuous linear operators from E into F. Assume that

$$
\sup_{i \in I} \| T_i x \| < \infty \quad \forall x \in E.\tag{1}
$$

Then

(2)

$$
\sup_{i \in I} \left\| T_i \right\|_{\mathcal{L}(E,F)} < \infty.
$$

In other words, there exists a constant c such that

$$
\| T _ { i } x \| \leq c \| x \| \quad \forall x \in E , \quad \forall i \in I .
$$

Remark 2. The conclusion of Theorem 2.2 is quite remarkable and surprising. From pointwise estimates one derives a global (uniform) estimate.

Proof. For every $n \geq 1$ , let

$$
X _ { n } = \{ x \in E ; \quad \forall i \in I , \quad \| T _ { i } x \| \leq n \} ,
$$

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

Remark 3. Recall that in general, a pointwise limit of continuous maps need not be continuous. The linearity assumption plays an essential role in Theorem 2.2. Note, however, that in the setting of Theorem 2.2 it does not follow that $\| T _ { n } - T \| _ { \mathcal { L } ( E , F ) }$ $\to 0 .$

Here are a few direct consequences of the uniform boundedness principle.

**Corollary 2.3.** Let E and F be two Banach spaces. Let $( T _ { n } )$ be a sequence of continuous linear operators from E into F such that for every $x   \in   E ,   T _ { n } x$ converges (as $n \to \infty )$ to a limit denoted by Tx. Then we have

(a) $\operatorname { s u p } _ { n } \left\| T _ { n } \right\| _ { \mathcal { L } ( E , F ) } < \infty ,$

(b) $T \in { \mathcal { L } } ( E , F )$ ,

(c) $\begin{array} { r } { \big \| T \big \| _ { \mathcal { L } ( E , F ) } \leq \operatorname* { l i m } \operatorname* { i n f } _ { n \to \infty } \| T _ { n } \| _ { \mathcal { L } ( E , F ) } . } \end{array}$

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

(4)

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
\overline { { B } } ^ { \star } \quad \mathit { i s ~ b o u n d e d . }\tag{6}
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

• **Theorem 2.6 (open mapping theorem).** Let E and F be two Banach spaces and let T be a continuous linear operator from E into F that is **surjective** $( = o n t o )$ . Then there exists a constant $c > 0$ such that

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

**Corollary 2.8.** Let E be a vector space provided with two norms, $\parallel \parallel 1$ and 2. Assume that E is a Banach space for **both** norms and that there exists a constant $C \geq 0$ such that

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

$$
\overline { { T ( B ( 0 , 1 ) ) } } \supset B ( 0 , 2 c ) .\tag{8}
$$

Proof. Set $X _ { n } = n { \overline { { T ( B ( 0 , 1 ) ) } } }$ . Since T is surjective, we have $\textstyle \bigcup _ { n = 1 } ^ { \infty } X _ { n } = F$ , and by the Baire category theorem there exists some $n _ { 0 }$ such that Int $( X _ { n _ { 0 } } ) \neq \emptyset .$ It follows that

$$
\operatorname { I n t } { \overline { { [ T ( B ( 0 , 1 ) ) ] } } } \neq \emptyset .
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
\forall \varepsilon > 0 \quad \exists z \in E \; { \mathrm { w i t h } } \; \| z \| < { \frac { 1 } { 2 } } \; { \mathrm { a n d } } \; \| y - T z \| < \varepsilon .\tag{12}
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

2.4 Complementary Subspaces. Right and Left Invertibility of Linear Operators

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

## - 2.4 Complementary Subspaces. Right and Left Invertibility of Linear Operators

We start with some geometric properties of closed subspaces in a Banach space that follow from the open mapping theorem.

\- **Theorem 2.10.** Let E be a Banach space. Assume that G and L are two closed linear subspaces such that $G + L$ is closed. Then there exists a constant $C \geq 0$ such that

$$
\begin{cases}e v e r y \: z \in G + L \: a d m i t s \: a \: d e c o m p o s i t i o n \: o f t h e \: f o r m \\z = x + y \: w i t h \: x \in G , y \in L , \| x \| \leq C \| z \| \: a n d \: \| y \| \leq C \| z \|.\end{cases}\tag{13}
$$

Proof. Consider the product space $G \times L$ with its norm

$$
\| \left[ x , y \right] \| = \| x \| + \| y \|
$$

and the space $G + L$ provided with the norm of $E$ .

The mapping $T : G \times L \to G + L$ defined by $T [ x , y ] = x + y$ is continuous, linear, and surjective. By the open mapping theorem there exists a constant $c > 0$ such that every $z \in G + L$ with $\| z \| < c$ can be written as $z = x + y$ with $x \in G$ $y \in L$ , and $\| x \| + \| y \| < 1$ . By homogeneity every $z \in G + L$ can be written as

$$
z = x + y \quad { \mathrm { w i t h } } \quad x \in G , y \in L , { \mathrm { a n d } } \quad \| x \| + \| y \| \leq ( 1 / c ) \| z \| .
$$

\- **Corollary 2.11.** Under the same assumptions as in Theorem 2.10, there exists a constant C such that

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
\begin{align*}\mathrm{dist}(x, G \cap L) & \leq \|x - (a - a')\| \leq \|x - a\| + \|a'\| \\& \leq \|x - a\| + C\|a - b\| \leq \|x - a\| + C(\|x - a\| + \|x - b\|) \\& \leq (1 + C)\operatorname{dist}(x, G) + \operatorname{dist}(x, L) + (1 + 2C)\varepsilon.\end{align*}
$$

Finally, we obtain (14) by letting $\varepsilon \to 0$

Remark 7. The converse of Corollary 2.11 is also true: If G and L are two closed linear subspaces such that (14) holds, then $G + L$ is closed (see Exercise 2.16).

**Definition.** Let $G   \subset   E$ be a closed subspace of a Banach space E. A subspace $L \subset E$ is said to be a topological complement or simply a complement of G if

(i) L is closed,

(ii) $G \cap L = \{ 0 \}$ and $G + L = E$

We shall also say that G and L are complementary subspaces of E. If this holds, then every $z   \in   E$ may be uniquely written as $z = x + y$ with $x   \in   G$ and $y   \in   L$ It follows from Theorem 2.10 that the projection operators $z \mapsto x$ and $z \mapsto y$ are continuous linear operators. (That property could also serve as a definition of complementary subspaces.)

## Examples

1. Every finite-dimensional subspace G admits a complement. Indeed, let $e _ { 1 }$ $e _ { 2 } , \ldots , e _ { n }$ be a basis of G. Every $x \in G$ may be written as $\textstyle x   =   \sum _ { i = 1 } ^ { n } x _ { i } e _ { i }$ Set $\varphi _ { i } ( x ) = x _ { i }$ . Using Hahn–Banach (analytic form)—or more precisely Corollary 1.2—each $\varphi _ { i }$ can be extended by a continuous linear functional $\tilde { \varphi } _ { i }$ defined on E. It is easy to check that $L = \cap _ { i = 1 } ^ { n } ( \widetilde { \varphi } _ { i } ) ^ { - 1 } ( 0 )$ is a complement of $G ,$

2. Every closed subspace G of finite codimension admits a complement. It suffices to choose any finite-dimensional space L such that $G \cap L = \{ 0 \}$ and $G + L = E$ (L is closed since it is finite-dimensional).

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

# Weak Topologies. Reflexive Spaces. Separable Spaces. Uniform Convexity

## 3.1 The Coarsest Topology for Which a Collection of Maps Becomes Continuous

We begin this chapter by recalling a well-known concept in topology. Suppose X is a set (without any structure) and $( Y _ { i } ) _ { i \in I }$ is a collection of topological spaces. We are given a collection of maps $( \varphi _ { i } ) _ { i \in I }$ such that for every $i \in I$ , $\varphi _ { i }$ maps X into $Y _ { i }$ and we consider the following:

**Problem 1.** Construct a topology on X that makes all the maps $( \varphi _ { i } ) _ { i \in I }$ continuous. If possible, find a topology $\mathcal { T }$ that is the most economical in the sense that it has the fewest open sets.

Note that if we equip X with the discrete topology (i.e., every subset of X is open), then every map $\varphi _ { i }$ is continuous; of course, this topology is far from being the “cheapest”; in fact, it is the most expensive one! As we shall see, there is always a (unique) “cheapest” topology $\mathcal { T }$ on X for which every map $\varphi _ { i }$ is continuous. It is called the coarsest or weakest topology (or sometimes the initial topology) associated to the collection $( \varphi _ { i } ) _ { i \in I }$

If $\omega _ { i } \subset Y _ { i }$ <sub>i</sub>s any open set, then $\varphi _ { i } ^ { - 1 } ( \omega _ { i } )$ is necessarily an open set in ${ \mathcal { T } } .   { \mathrm { A s } }$ ωi runs through the family of open sets of $Y _ { i }$ and i runs through I we obtain a family of subsets of $X ,$ each of which must be open in the topology $\mathcal { T }$ . Let us denote this family by $( U _ { \lambda } ) _ { \lambda \in \Lambda }$ . Of course, this family need not be a topology. Therefore, we are led to the following:

**Problem 2.** Given a set X and a family $( U _ { \lambda } ) _ { \lambda \in \Lambda }$ of subsets in X, construct the cheapest topology $\mathcal { T }$ on X in which $U _ { \lambda }$ is open for all $\lambda \in \Lambda$

In other words, we must find the cheapest family $\mathcal { F }$ of subsets of X that is $s t a b l e ^ { 1 }$ by $\Gamma _ { \mathrm { f i n i t e } }$ and $\mathrm { U _ { a r b i t r a r y } }$ and with the property that $U _ { \lambda }   \in   \mathcal { F }$ for every $\lambda \in \Lambda$ . The construction goes as follows. First,consider finite intersections of sets in $( U _ { \lambda } ) _ { \lambda \in \Lambda }$ i.e., $\cap _ { \lambda \in \Gamma } U _ { \lambda }$ where $\Gamma \subset \Lambda$ is finite. In this way we obtain a new family, called , of subsets of X which includes $( U _ { \lambda } ) _ { \lambda \in \Lambda }$ and which is stable under $\cap _ { \mathrm { f i n i t e } }$ . However, it need not be stable under $\mathrm { U _ { a r b i t r a r y } }$ . Therefore, we consider next the family $\mathcal { F }$ obtained by forming arbitrary unions of elements from . It is clear that $\mathcal { F }$ is stable under $\mathrm { U _ { a r b i t r a r y } }$ . It is not clear whether $\mathcal { F }$ is stable under $\cap _ { \mathrm { f i n i t e } }$ ; but indeed we have the following result:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">F</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">F</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 Meaning that a finite intersection of sets in F and an arbitrary union of sets in F both belong F to .</span></small>

## Lemma 3.1. The family $\mathcal { F }$ is stable under ∩finite.

The proof of Lemma 3.1—a delightful exercise in set theory—is left to the reader; see e.g., G. Folland [2]. It is now obvious that the above construction gives the cheapest topology with the required property.

Remark 1. One cannot reverse the order of operations in the construction of $\mathcal { F }$ . It would have been equally natural to start with $\mathrm { U _ { a r b i t r a r y } }$ and then to take $\cap _ { \mathrm { f i n i t e } }$ . The outcome is a family that is stable under $\cap _ { \mathrm { f i n i t e } } ;$ but it is not stable under $\mathrm { U _ { a r b i t r a r y } . }$ One would have to consider once more $\mathrm { U _ { a r b i t r a r y } }$ and the process then stabilizes.

To summarize this discussion we find that the open sets of the topology $\mathcal { T }$ are obtained by considering first $\cap _ { \mathrm { f i n i t e } }$ of sets of the form $\varphi _ { i } ^ { - 1 } ( \omega _ { i } )$ and then $\mathrm { U _ { a r b i t r a r y } }$ . It follows that for every $x \in X$ , we obtain a basis of neighborhoods of x for the topology $\mathcal { T }$ by considering sets of the form ∩finite $\varphi _ { i } ^ { - 1 } ( V _ { i } )$ , where $V _ { i }$ is a neighborhood of $\varphi _ { i } ( x )$ in $Y _ { i }$ . Recall that in a topological space, a basis of neighborhoods of a point x is a family of neighborhoods of x, such that every neighborhood of x contains a neighborhood from the basis.

In what follows we equip X with the topology $\mathcal { T }$ that is the weakest topology associated to the collection $( \varphi _ { i } ) _ { i \in I }$ . Here are two simple properties of the topology $\mathcal { T }$

• **Proposition 3.1.** Let $( x _ { n } )$ be a sequence in X. Then $x _ { n } \rightarrow x ( i n \mathcal { T } )$ if and only if $\varphi _ { i } ( x _ { n } ) \to \varphi _ { i } ( x )$ for every $i \in I$

Proof. If $x _ { n } \to x$ , then $\varphi _ { i } ( x _ { n } ) \to \varphi _ { i } ( x )$ for each i, since each $\varphi _ { i }$ is continuous for $\mathcal { T }$ . Conversely, let U be a neighborhood of x. From the preceding discussion, we may always assume that U has the form $U = \cap _ { i \in J } \varphi _ { i } ^ { - 1 } ( V _ { i } )$ with $J \subset I$ finite. For each $i   \in   J$ there is some integer $N _ { i }$ such that $\varphi _ { i } ( x _ { n } ) \in V _ { i }$ for $n \geq N _ { i }$ . It follows that $x _ { n } \in U$ for $n \geq N = \operatorname* { m a x } _ { i \in J } N _ { i }$

• **Proposition 3.2.** Let Z be a topological space and let ψ be a map from $Z$ into X. Then ψ is continuous if and only if ϕ<sub>i</sub> ◦ ψ is continuous from Z into $Y _ { i }   f _ { } { o r }$ every $i \in I$

Proof. If ψ is continuous then $\varphi _ { i } \circ$ ψ is also continuous for every $i \in I$ . Conversely, we have to prove that $\psi ^ { - 1 } ( U )$ is open (in Z) for every open set U (in X). But we know that $U$ has the form $U = \cup _ { \mathrm { a r b i t r a r y } }$ ∩finite $\varphi _ { i } ^ { - 1 } \dot { ( \omega _ { i } ) }$ , where $\omega _ { i }$ is open in $Y _ { i }$ . Therefore

$$
\psi ^ { - 1 } ( U ) = \underset { \mathrm { a r b i t r a r y } } { \cup } \underset { \mathrm { f i n i t e } } { \cap } \psi ^ { - 1 } [ \varphi _ { i } ^ { - 1 } ( \omega _ { i } ) ] = \underset { \mathrm { a r b i t r a r y } } { \cup } \underset { \mathrm { f i n i t e } } { \cap } ( \varphi _ { i } \circ \psi ) ^ { - 1 } ( \omega _ { i } ) ,
$$

which is open in $Z$ since every map $\varphi _ { i } \circ \psi$ is continuous.

## 3.2 Definition and Elementary Properties of the Weak Topology $\sigma ( E , E ^ { \star } )$

Let E be a Banach space and let $f   \in   E ^ { \star }$ . We denote by $\varphi _ { f } : E   \to   \mathbb { R }$ the linear functional $\varphi _ { f } ( x ) = \langle f , x \rangle . \operatorname { A s }   j$ runs through $E ^ { \star }$ we obtain a collection $( \varphi _ { f } ) _ { f \in E ^ { \star } }$ of maps from E into R. We now ignore the usual topology on E (associated to ) and define a new topology on the set E as follows:

**Definition.** The weak topology $\sigma ( E , E ^ { \star } )$ on E is the coarsest topology associated to the collection $( \varphi _ { f } ) _ { f \in E ^ { \star } }$ (in the sense of Section 3.1 with $X = E ,   Y_i = \mathbb{R}$ , for each i, and $I = E ^ { \star } )$

Note that every map $\varphi _ { f }$ is continuous for the usual topology and therefore the weak topology is weaker than the usual topology.

## Proposition 3.3. The weak topology $\sigma ( E , E ^ { \star } )$ is Hausdorff.

Proof. Given $x _ { 1 } , x _ { 2 }   \in   E$ with $x _ { 1 } \neq x _ { 2 }$ we have to find two open sets $O _ { 1 }$ and $O _ { 2 }$ for the weak topology $\sigma ( E , E ^ { \star } )$ such that $x _ { 1 }   \in   O _ { 1 } ,   x _ { 2 }   \in   O _ { 2 }$ , and $O _ { 1 } \cap O _ { 2 } = \emptyset .$ By Hahn–Banach (second geometric form) there exists a closed hyperplane strictly separating $\{ x _ { 1 } \}$ and $\{ x _ { 2 } \}$ . Thus, there exist some $f \in E ^ { \star }$ and some $\alpha \in \mathbb { R }$ such that

$$
\langle f , x _ { 1 } \rangle < \alpha < \langle f , x _ { 2 } \rangle .
$$

Set

$$
\begin{aligned} &O_{1} = \left\{ x \in E; \left\langle f, x \right\rangle < \alpha \right\} = \varphi_{f}^{-1} \left( \left( -\infty, \alpha \right) \right), \\&O_{2} = \left\{ x \in E; \left\langle f, x \right\rangle > \alpha \right\} = \varphi_{f}^{-1} \left( \left( \alpha, +\infty \right) \right).\\ \end{aligned}
$$

Clearly, $O _ { 1 }$ and $O _ { 2 }$ are open for $\sigma ( E , E ^ { \star } )$ and they satisfy the required properties.

• **Proposition 3.4.** Let $x _ { 0 } \in E ;   g i v e n \; \varepsilon   >   0$ and a **finite** set $\{ f _ { 1 } ,   f _ { 2 } ,   \ldots ,   f _ { k } \}$ in $E ^ { \star }$ consider

$$
V = V ( f _ { 1 } , f _ { 2 } , \ldots , f _ { k } ;   \varepsilon ) = \{ x \in E ; \quad | \langle f _ { i } , x - x _ { 0 } \rangle | < \varepsilon \quad \forall i = 1 , 2 , \ldots , k \}   .
$$

Then V is a neighborhood of x<sub>0</sub> for the topology $\sigma ( E , E ^ { \star } )$ . Moreover, we obtain a **basis of neighborhoods** of x0 for $\sigma ( E , E ^ { \star } )$ by varying ε, k, and the $f _ { i } ^ { \mathrm { ~ , ~ } } s$ in $E ^ { \star }$

Proof. Clearly $V = \cap _ { i = 1 } ^ { k } \varphi _ { f _ { i } } ^ { - 1 } ( ( a _ { i } - \varepsilon , a _ { i } + \varepsilon ) )$ , with $a _ { i } = \langle f _ { i } , x _ { 0 } \rangle$ , is open for the topology $\sigma ( E , E ^ { \star } )$ and contains x<sub>0</sub>. Conversely, let U be a neighborhood of $x _ { 0 }$ for $\sigma ( E , E ^ { \star } )$ . From the discussion in Section 3.1 we know that there exists an open set W containing $x _ { 0 } , W \subset U$ , of the form $W = \cap _ { \mathrm { f i n i t e } } \varphi _ { f _ { i } } ^ { - 1 } ( \omega _ { i } )$ , where $\omega _ { i }$ is a neighborhood (in R) of $a _ { i } = \langle f _ { i } , x _ { 0 } \rangle$ . Hence there exists $\varepsilon > 0$ such that $( a _ { i } - \varepsilon , a _ { i } + \varepsilon ) \subset \omega _ { i }$ for every i. It follows that $x _ { 0 } \in V \subset W \subset U$

**Notation.** If a sequence $( x _ { n } )$ in E converges to x in the weak topology $\sigma ( E , E ^ { \star } )$ we shall write

$$
\boxed { x _ { n } \rightharpoonup x . }
$$

To avoid any confusion we shall sometimes say, $\text{" } x_{n} \text{→ } x$ weakly in $\sigma ( E , E ^ { \star } )$ ” In order to be totally clear we shall sometimes emphasize strong convergence by saying, $\text{" } x_{n} \rightarrow x$ strongly,” meaning that $\| x _ { n } - x \| \to 0$

## • Proposition 3.5. Let $( x _ { n } )$ be a sequence in E. Then

(i) $[ x _ { n } \rightharpoonup x \quad w e a k l y \quad i n \quad \sigma ( E , E ^ { \star } ) ] \Leftrightarrow [ \langle f , x _ { n } \rangle \rightarrow \langle f , x \rangle \quad \forall f \in E ^ { \star } ] .$

(ii) $I f x _ { n } \to x$ strongly, then $x _ { n } \rightharpoonup x$ weakly in $\sigma ( E , E ^ { \star } )$

(iii) $I f x _ { n } \rightharpoonup x$ weakly in $\sigma ( E , E ^ { \star } )$ , then $( \| x _ { n } \| )$ is bounded and $\| x \| \leq$ lim inf $\| x _ { n } \|$

(iv) $I f x _ { n } \rightharpoonup x$ weakly in σ $( E , E ^ { \star } )$ and if $[ f _ { n } \rightarrow f$ strongly in $E ^ { \star } \left( i . e . ,   \| f _ { n }   -   f \| _ { E ^ { \star } } \right) \rightarrow$ 0), then $\langle f _ { n } , x _ { n } \rangle \to \langle f , x \rangle$

Proof.

(i) f ll f P iti 3 1 d th d fi iti f th k t l o ows rom ropos on . an e e n on o e wea opo ogy $\sigma ( E , E ^ { \star } )$

(ii) follows from (i), since $\left| \left\langle f, x_n \right\rangle - \left\langle f, x \right\rangle \right| \leq \left\| f \right\| \left\| x_n - x \right\|$ ; it is also clear from the fact that the weak topology is weaker than the strong topology.

(iii) follows from the uniform boundedness principle (see Corollary 2.4), since for every $f \in E ^ { \star }$ the set $( \langle f , x _ { n } \rangle ) _ { n }$ is bounded. Passing to the limit in the inequality

$$
| \langle f , x _ { n } \rangle | \leq \| f \| \| x _ { n } \| ,
$$

we obtain

$$
| \langle f , x \rangle | \leq \| f \| \liminf \| x _ { n } \| ,
$$

which implies (by Corollary 1.4) that

$$
\| x \| = \sup_{\| f \| \leq 1} | \langle f, x \rangle | \leq \liminf_{n \to \infty} \| x_n \|.
$$

(iv) follows from the inequality

$$
| \langle f _ { n } , x _ { n } \rangle - \langle f , x \rangle | \leq | \langle f _ { n } - f , x _ { n } \rangle | + | \langle f , x _ { n } - x \rangle | \leq \| f _ { n } - f \| \| x _ { n } \| + | \langle f , x _ { n } - x \rangle | ,
$$

combined with (i) and (iii).

• **Proposition 3.6.** When E is **finite-dimensional**, the weak topology $\sigma ( E , E ^ { \star } )$ and the usual topology are the **same**. In particular, a sequence $( x _ { n } )$ converges weakly if and only if it converges strongly.

Proof. Since the weak topology has always fewer open sets than the strong topology, it suffices to check that every strongly open set is weakly open. Let $x _ { 0 } \in E$ and let $U$ be a neighborhood of $x _ { 0 }$ in the strong topology. We have to find a neighborhood V of $x _ { 0 }$ in the weak topology $\sigma ( E , E ^ { \star } )$ such that $V \subset U$ . In other words, we have to find $f _ { 1 } ,   f _ { 2 } , \ldots ,   f _ { k }$ in $E ^ { \star }$ and $\varepsilon > 0$ such that

$$
V = \{ x \in E ; | \langle f _ { i } , x - x _ { 0 } \rangle | < \varepsilon \quad \forall i = 1 , 2 , \ldots , k \} \subset U .
$$

Fix $r ~ > ~ 0$ such that $B ( x _ { 0 } , r ) \; \subset \; U$ . Pick a basis $e _ { 1 } , e _ { 2 } , \ldots , e _ { k }$ in E such that $\| e _ { i } \| = 1$ , ∀i. Every $x \in E$ admits a decomposition $\textstyle x = \sum _ { i = 1 } ^ { k } x _ { i } e _ { i }$ , and the maps $x \mapsto x _ { i }$ are continuous linear functionals on $E$ denoted by $f _ { i }$ . We have

$$
\| x - x _ { 0 } \| \leq \sum _ { i = 1 } ^ { k } \lvert \langle f _ { i } , x - x _ { 0 } \rangle \rvert < k \varepsilon .
$$

for every $x \in V$ . Choosing $\varepsilon = r / k$ , we obtain $V \subset U$

Remark 2. Open (resp. closed) sets in the weak topology $\sigma ( E , E ^ { \star } )$ are always open (resp. closed) in the strong topology. In any infinite-dimensional space the weak topology is strictly coarser than the strong topology; i.e., there exist open (resp. closed) sets in the strong topology that are not open (resp. closed) in the weak topology. Here are two examples:

Example 1. The unit sphere $S = \{ x \in E ; \| x \| = 1 \}$ , with E infinite-dimensional, is never closed in the weak topology $\sigma ( E , E ^ { \star } )$ . More precisely, we have

$$
\overline { { S } } ^ { \sigma ( E , E ^ { \star } ) } = B _ { E } ,\tag{1}
$$

where $\overline { { S } } ^ { \sigma ( E , E ^ { \star } ) }$ denotes the closure of S in the topology $\sigma ( E , E ^ { \star } )$ and $B _ { E }$ (already defined in Chapter 2) denotes the closed unit ball in $E$ ,

$$
B _ { E } = \{ x \in E ; \| x \| \leq 1 \} .
$$

First let us check that every $x _ { 0 } \in E$ with $\| x _ { 0 } \| < 1$ belongs to $\overline { { S } } ^ { \sigma ( E , E ^ { \star } ) }$ . Indeed, let V be a neighborhood of $x _ { 0 }$ in $\sigma ( E , E ^ { \star } )$ . We have to prove that $V \cap S \neq \emptyset$ . In view of Proposition 3.4 we may always assume that V has the form

$$
V = \{ x \in E ; | \langle f _ { i } , x - x _ { 0 } \rangle | < \varepsilon \quad \forall i = 1 , 2 , \ldots , k \}
$$

with $\varepsilon > 0$ and $f _ { 1 } ,   f _ { 2 } ,   \ldots ,   f _ { k } \in E ^ { \star }$ . Fix $y _ { 0 } \in E ,   y _ { 0 } \neq 0$ , such that

$$
\langle f _ { i } , y _ { 0 } \rangle = 0 \qquad \forall i = 1 , 2 , \ldots , k .
$$

[Such a $y _ { 0 }$ exists; otherwise, the map $\varphi \quad : \quad E \quad \to \quad \mathbb { R } ^ { k }$ defined by $\varphi ( x ) ~ = ~$ $( \langle f _ { i } , x \rangle ) _ { 1 \leq i \leq k }$ would be injective and $\varphi$ would be an isomorphism from E onto $\varphi ( E )$ , and thus dim $E \leq k$ , which contradicts the assumption that $E$ is infinitedimensional. $1 ] ^ { 2 }$ The function $g(t) = \left\| x_{0} + t y_{0} \right\|$ is continuous on $[ 0 , \infty )$ with $g ( 0 ) < 1$ and $\begin{array} { r } { \operatorname* { l i m } _ { t \to + \infty }   g ( t ) = + \infty } \end{array}$ . Hence there exists some $t _ { 0 } > 0$ such that $\left\| x_{0} +  t_{0} y_{0} \right\| = 1$ It follows that $x _ { 0 } + t _ { 0 } y _ { 0 } \in V \cap S$ , and thus we have established that

$$
S \subset B _ { E } \subset \overline { { S } } ^ { \sigma ( E , E ^ { \star } ) } .
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">V</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">0.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">σ ( , -)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x0,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2 The geometric interpretation of this construction is the following. When E is infinite-dimensional, every neighborhood V of in the topology E E contains a line passing through even a “huge” affine space passing through x</span></small>

In order to complete the proof of (1) it suffices to know that $B _ { E }$ is closed in the topology $\sigma ( E , E ^ { \star } )$ . But we have

$$
B _ { E } = \bigcap _ { \substack { f \in E ^ { \star } \\ \| f \| \leq 1 } } \{ x \in E ; \; | \langle f , x \rangle | \leq 1 \} ,
$$

which is an intersection of weakly closed sets.

Example 2. The unit ball $U = \{ x   \in   E ; \; \| x \|   <   1 \}$ , with E infinite-dimensional, is never open in the weak topology $\sigma ( E , E ^ { \star } )$ . Suppose, by contradiction, that $U$ is weakly open. Then its complement $U ^ { c }   =   \{ x   \in   E ;   \| x \|   \geq   1 \}$ is weakly closed. It follows that $S = B _ { E } \cap U ^ { c }$ is also weakly closed; this contradicts Example 1.

\- Remark 3. In infinite-dimensional spaces the weak topology is never metrizable, i.e., there is no metric (and a fortiori no norm) on E that induces on E the weak topology $\sigma ( E , E ^ { \star } )$ ; see Exercise 3.8. However, as we shall see later (Theorem 3.29), if $E ^ { \star }$ is separable one can define a norm on E that induces on bounded sets of E the weak topology $\sigma ( E , E ^ { \star } )$

\- Remark 4. Usually, in infinite-dimensional spaces, there exist sequences that converge weakly and do not converge strongly. For example, if $E ^ { \star }$ is separable or if E is reflexive one can construct a sequence $( x _ { n } )$ in E such that $\| x _ { n } \| = 1$ and $x _ { n } \rightharpoonup 0$ weakly (see Exercise 3.22). However, there are infinite-dimensional spaces with the property that every weakly convergent sequence is strongly convergent. For example, $\ell ^ { 1 }$ has that unusual property (see Problem 8). Such spaces are quite “rare” and somewhat “pathological.” This strange fact does not contradict Remark 2, which asserts that in infinite-dimensional spaces, the weak topology and the strong topology are always distinct: the weak topology is strictly coarser than the strong topology. Keep in mind that two metric (or metrizable) spaces with the same convergent sequences have identical topologies; however, if two topological spaces have the same convergent sequences they need not have identical topologies.

## 3.3 Weak Topology, Convex Sets, and Linear Operators

Every weakly closed set is strongly closed and the converse is false in infinitedimensional spaces (see Remark 2). However, it is very useful to know that for convex sets, weakly closed = strongly closed:

• **Theorem 3.7.** Let C be a convex subset of E. Then C is closed in the weak topology $\sigma ( E , E ^ { \star } )$ if and only if it is closed in the strong topology.

Proof. Assume that C is closed in the strong topology and let us prove that C is closed in the weak topology. We shall check that the complement $C ^ { c }$ of C is open in the weak topology. To this end, let $x _ { 0 } \notin C$ . By Hahn–Banach there exists a closed hyperplane strictly separating $\{ x _ { 0 } \}$ and C. Thus, there exist some $f \in E ^ { \star }$ and some $\alpha \in \mathbb { R }$ such that

$$
\langle f , x _ { 0 } \rangle < \alpha < \langle f , y \rangle \quad \forall y \in C .
$$

Set

$$
V = \{ x \in E ; \langle f , x \rangle < \alpha \} ;
$$

so that $x _ { 0 } \in V ,   V \cap C = \varnothing   ( \mathrm { i . e . , }   V \subset C ^ { c } )$ and V is open in the weak topology.

**Corollary 3.8 (Mazur).** Assume $( x _ { n } )$ converges **weakly** to x. Then there exists a sequence $( y _ { n } )$ made up of convex combinations of the $x _ { n }   { \dot { s } }$ that converges **strongly** to x.

Proof. Let $C = \operatorname { \mathsf { c o n v } } ( \cup _ { p = 1 } ^ { \infty } \{ x _ { p } \} )$ denote the convex hull of the ${ x _ { n } } ^ { \prime } \mathbf { s }$ . Since x belongs to the weak closure of $\dot { \cup } _ { p = 1 } ^ { \infty } \{ x _ { p } \}$ it belongs a fortiori to the weak closure of C. By Theorem $3 . 7 , x \in \overline { { C } }$ , the strong closure of C, and the conclusion follows.

Remark 5. There are some variants of Corollary 3.8 (see Exercises 3.4 and 5.24). Also, note that the proof of Theorem 3.7 shows that every closed convex set C coincides with the intersection of all the closed half-spaces containing C.

• **Corollary 3.9.** Assume that $\varphi : E \to ( - \infty + \infty ]$ is convex and l.s.c. in the strong topology. Then ϕ is l.s.c. in the weak topology $\sigma ( E , E ^ { \star } )$ .

Proof. For every $\lambda \in \mathbb { R }$ the set

$$
A = \{ x \in E ; \varphi ( x ) \leq \lambda \}
$$

is convex and strongly closed. By Theorem 3.7 it is weakly closed and thus $\varphi$ is weakly l.s.c.

• Remark 6. It may be rather difficult in practice to prove that a function is l.s.c. in the weak topology. Corollary 3.9 is often used as follows:

ϕ convex and strongly continuous ⇒ ϕ weakly l.s.c.

For example, the function $\varphi ( x ) = \| x \|$ is convex and strongly continuous; thus it is weakly l.s.c. In particular, if $x _ { n } \rightharpoonup x$ weakly, it follows that $\| x \| \leq \operatorname* { l i m }$ inf $\| x _ { n } \|$ (see also Proposition 3.5).

**Theorem 3.10.** Let E and F be two Banach spaces and let T be a linear operator from E into F. Assume that T is continuous in the strong topologies. Then $T$ is continuous from E weak σ $( E , E ^ { \star } )$ into F weak $\sigma ( F , F ^ { \star } )$ and conversely.

Proof. In view of Proposition 3.2 it suffices to check that for every $f \in F ^ { \star }$ the map $x \mapsto \langle f , T x \rangle$ is continuous from E weak $\sigma ( E , E ^ { \star } )$ into R. But the map $x \mapsto \langle f , T x \rangle$ is a continuous linear functional on E. Therefore, it is also continuous in the weak topology $\sigma ( E , E ^ { \star } )$

Conversely, suppose that T is continuous from E weak into F weak. Then $G ( T )$ is closed in $E \times F$ equipped with the product topology $\sigma ( E , E ^ { \star } ) \times \sigma ( F , F ^ { \star } )$ , which is clearly the same as $\sigma ( E \times F , ( E \times F ) ^ { \star } )$ . It follows that $G ( T )$ is strongly closed (any weakly closed set is strongly closed). We conclude with the help of the closed graph theorem (Theorem 2.9) that T is continuous from E strong into F strong.

Remark 7. The argument above shows more: that if a linear operator T is continuous from E strong into F weak then T is continuous from $E$ strong into $F$ strong. As a consequence, for linear operators, the following continuity properties are all the same: $S   \to   S ,   W   \to   W ,   S   \to   W   ( S   = \mathrm { s t r o n g } ,   W   = \mathrm { w e a k } )$ . On the other hand, very few linear operators are continuous $W \to S ;$ this happens if and only if T is continuous $S \rightarrow S$ and, moreover, dim $R ( T ) < \infty$ (see Exercise 6.7).

Also, note that in general, nonlinear maps that are continuous from E strong into $F$ strong are not continuous from E weak into F weak (see, e.g., Exercise 4.20). This is a major source of difficulties in nonlinear problems.

## 3.4 The Weak- Topology σ $( E ^ { \star } , E )$

So far, we have two topologies on $E ^ { \star }$ :

(a) the usual (strong) topology associated to the norm of $E ^ { \star }$ ,

(b) the weak topology $\sigma ( E ^ { \star } , E ^ { \star \star } )$ , obtained by performing on $E ^ { \star }$ the construction of Section 3.3.

We are now going to define a third topology on $E ^ { \star }$ called the weak- topology and denoted by $\sigma ( E ^ { \star } , E )$ (the - is here to remind us that this topology is defined only on dual spaces). For every $x \in E$ consider the linear functional $\varphi _ { x } : E ^ { \star } \to$ R defined by $f \mapsto \varphi _ { x } ( f ) = \langle f , x \rangle$ . As x runs through E we obtain a collection $( \varphi _ { x } ) _ { x \in E }$ of maps from $E ^ { \star }$ into R.

**Definition.** The $w e a k ^ { \star }   t o p o l o g y , \sigma ( E ^ { \star } , E )$ , is the coarsest topology on $E ^ { \star }$ associated to the collection $( \varphi _ { x } ) _ { x \in E }$ (in the sense of Section 3.1 with $X = E ^ { \star } , Y _ { i } = \mathbb { R }$ , for all i, and $I = E )$ .

Since $E \subset E ^ { \star \star }$ , it is clear that the topology $\sigma ( E ^ { \star } , E )$ is coarser than the topology $\sigma ( E ^ { \star } , E ^ { \star \star } ) ; \mathrm { i . e . }$ , the topology $\sigma ( E ^ { \star } , E )$ has fewer open sets (resp. closed sets) than the topology $\sigma ( E ^ { \star } , E ^ { \star \star } )$ , which in turn has fewer open sets (resp. closed sets) than the strong topology.

Remark 8. The reader probably wonders why there is such hysteria over weak topologies! The reason is the following: a coarser topology has more compact sets. For example, the closed unit ball $B _ { E ^ { \star } }$ in $E ^ { \star }$ , which is never compact in the strong topology (unless dim $E < \infty ;$ see Theorem 6.5), is always compact in the weak- topology (see Theorem 3.16). Knowing the basic role of compact sets—for example, in existence mechanisms such as minimization—it is easy to understand the importance of the weak- topology.