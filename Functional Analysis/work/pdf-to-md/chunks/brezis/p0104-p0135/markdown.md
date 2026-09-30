Let $( \Omega , \mathcal { M } , \mu )$ denote a measure space, i.e.,  is a set and

(i) M is a σ -algebra in $\Omega , \mathrm { i . e . } , \mathcal { M }$ is a collection of subsets of  such that:

(a) $\emptyset \in \mathcal { M } ,$

(b) $A \in { \mathcal { M } } \Rightarrow A ^ { c } \in { \mathcal { M } } ,$

(c) $\textstyle \bigcup _ { n = 1 } ^ { \infty } A _ { n } \in { \mathcal { M } }$ whenever $A _ { n } \in \mathcal { M } \quad \forall n$

(ii) μ is a measure, i.e., $\mu : \mathcal { M } \to [ 0 , \infty ]$ satisfies

(a) $\mu ( \varnothing ) = 0 ,$ $\left\{ \mu \left( \bigcup_{n = 1}^{\infty} A_{n} \right) = \bigcup_{n = 1}^{\infty} \mu(A_{n}) \right.$ whenever $( A _ { n } )$ is a disjoint (b) ⎩countable family of members of $\mathcal { M } .$ . The members of M are called the measurable sets. Sometimes we shall write $| A |$ instead of $\mu ( A )$ . We shall also assume—even though this is not essential—that

(iii)  is σ -finite, i.e., there exists a countable family $( \Omega _ { n } )$ in M such that $\Omega =$ $\textstyle \bigcup _ { n = 1 } ^ { \infty } \Omega _ { n }$ and $\mu ( \Omega _ { n } ) < \infty \quad \forall n$

The sets $E \in \mathcal { M }$ with the property that $\mu ( E ) = 0$ are called the null sets. We say that a property holds a.e. (or for almost all $x \in \Omega )$ if it holds everywhere on  except on a null set.

We assume that the reader is familiar with the notions of measurable functions and integrable functions $f : \Omega \to \mathbb { R }$ ; see, e.g., H. L. Royden [1], G. B. Folland [2], A. Knapp [1], D. L. Cohn [1], A. Friedman [3], W. Rudin [2], P. Halmos [1], E. Hewitt– K. Stromberg [1], R. Wheeden–A. Zygmund [1], J. Neveu [1], P. Malliavin [1], A. J. Weir [1], A. Kolmogorov–S. Fomin [1], I. Fonseca–G. Leoni [1]. We denote by $L ^ { 1 } ( \Omega , \mu )$ , or simply $L ^ { 1 } ( \Omega )$ (or just $L ^ { 1 } )$ , the space of integrable functions from  into R.

We shall often write  f instead of $\textstyle \int _ { \Omega } f   d \mu$ , and we shall also use the notation

$$
\| f \| _ { L ^ { 1 } } = \| f \| _ { 1 } = \int _ { \Omega } | f | d \mu = \int | f | .
$$

As usual, we identify two functions that coincide a.e. We recall the following basic facts.

## 4.1 Some Results about Integration That Everyone Must Know

• **Theorem 4.1 (monotone convergence theorem, Beppo Levi).** $L e t \left( f _ { n } \right)$ be a sequence of functions in $L ^ { 1 }$ that satisfy

(a) $f _ { 1 } \leq f _ { 2 } \leq \cdots \leq f _ { n } \leq f _ { n + 1 } \leq \cdots \; \mathrm { a . e . \; o n \; \Omega } ,$

(b) $\begin{array} { r } { \operatorname* { s u p } _ { n } \int f _ { n } < \infty . } \end{array}$

Then $f _ { n } ( x )$ converges a.e. on  to a finite limit, which we denote by $f ( x )$ ; the function f belongs to $L ^ { 1 }$ and $\| f _ { n } - f \| _ { 1 } \to 0 .$

• **Theorem 4.2 (dominated convergence theorem, Lebesgue).** Let $( f _ { n } )$ be a sequence of functions in $L ^ { 1 }$ that satisfy

(a) $f _ { n } ( x ) \to f ( x ) \; \mathrm { a . e . } \; o n \; \Omega ,$

(b) there is a function $g \in L ^ { 1 }$ such that for all n, $| f _ { n } ( x ) | \leq g ( x )$ a.e. on .

Then $f \in L ^ { 1 }$ and $\| f _ { n } - f \| _ { 1 } \to 0 .$

**Lemma 4.1 (Fatou’s lemma).** Let $( f _ { n } )$ be a sequence of functions in $L ^ { 1 }$ that satisfy

(a) for all n, $f _ { n } \geq 0$ a.e.

(b) $\begin{array} { r } { \operatorname* { s u p } _ { n } \int f _ { n } < \infty . } \end{array}$

For almost all $x \in \Omega$ we set $\begin{array} { r } { f ( x ) = \operatorname* { l i m } \operatorname* { i n f } _ { n \to \infty } f _ { n } ( x ) \leq + \infty } \end{array}$ . Then $f \in L ^ { 1 }$ and

$$
\int f \leq \liminf_{n \to \infty} \int f_n.
$$

A basic example is the case in which $\Omega   =   \mathbb { R } ^ { N }$ , M consists of the Lebesgue measurable sets, and $\mu$ is the Lebesgue measure on $\mathbb { R } ^ { N }$

**Notation.** We denote by $C _ { c } ( \mathbb { R } ^ { N } )$ the space of all continuous functions on $\mathbb { R } ^ { N }$ with compact support, i.e.,

$$
C _ { c } ( \mathbb { R } ^ { N } ) = \{ f \in C ( \mathbb { R } ^ { N } ) ;   f ( x ) = 0 \quad \forall x \in \mathbb { R } ^ { N } \backslash K , \mathrm { ~ w h e r e ~ } K \mathrm { ~ i s ~ c o m p a c t } \} .
$$

**Theorem 4.3 (density).** The space $C _ { c } ( \mathbb { R } ^ { N } )$ is dense in $L ^ { 1 } ( \mathbb { R } ^ { N } ) ;   i . e .$

$$
\forall f \in L ^ { 1 } ( \mathbb { R } ^ { N } ) \quad \forall \varepsilon > 0 \quad \exists f _ { 1 } \in C _ { c } ( \mathbb { R } ^ { N } ) \quad s u c h \quad t h a t \quad \| f - f _ { 1 } \| _ { 1 } \leq \varepsilon .
$$

Let $( \Omega _ { 1 } ,   \mathcal { M } _ { 1 } ,   \mu _ { 1 } )$ and $( \Omega _ { 2 } ,   \mathcal { M } _ { 2 } \; ,   \mu _ { 2 } )$ be two measure spaces that are $\sigma \text {-} \mathrm { f i n i t e } .$ One can define in a standard way the structure of measure space $( \Omega , \mathcal { M }   , \mu )$ on the Cartesian product $\Omega = \Omega _ { 1 } \times \Omega _ { 2 }$

**Theorem 4.4 (Tonelli).** Let $F ( x ,   y )   :   \Omega _ { 1 }   \times   \Omega _ { 2 }   \to   \mathbb { R }$ be a measurable function satisfying

$$
\mathtt { ( a ) } \int _ { \Omega _ { 2 } } | F ( x , y ) | d \mu _ { 2 } < \infty   f _ { } { o r } \; \mathtt { a . e . } \; x \in \Omega _ { 1 } .
$$

and

$$
\mathsf { ( b ) } \int _ { \Omega _ { 1 } } d \mu _ { 1 } \int _ { \Omega _ { 2 } } | F ( x , y ) | d \mu _ { 2 } < \infty .
$$

Then $F \in L ^ { 1 } ( \Omega _ { 1 } \times \Omega _ { 2 } )$

**Theorem 4.5 (Fubini).** Assume that $F \; \in \; L ^ { 1 } ( \Omega _ { 1 }   \times   \Omega _ { 2 } )$ . Then for a.e. $x \in \Omega _ { 1 }$ $F ( x , y ) \; \in \; L _ { y } ^ { 1 } ( \Omega _ { 2 } )$ and $\begin{array} { r } { \int _ { \Omega _ { 2 } } F ( x ,   y ) d \mu _ { 2 } \; \in \; L _ { x } ^ { 1 } ( \Omega _ { 1 } ) } \end{array}$ . Similarly, for a.e. $y \in \Omega _ { 2 }$ $F ( x , y ) \in L _ { x } ^ { 1 } ( \Omega _ { 1 } )$ and $\begin{array} { r } { \int _ { \Omega _ { 1 } } F ( x , y ) d \mu _ { 1 } \in L _ { y } ^ { 1 } ( \Omega _ { 2 } ) } \end{array}$

Moreover, one has

$$
\int _ { \Omega _ { 1 } } d \mu _ { 1 } \int _ { \Omega _ { 2 } } F ( x , y ) d \mu _ { 2 } = \int _ { \Omega _ { 2 } } d \mu _ { 2 } \int _ { \Omega _ { 1 } } F ( x , y ) d \mu _ { 1 } = \iint _ { \Omega _ { 1 } \times \Omega _ { 2 } } F ( x , y ) d \mu _ { 1 } d \mu _ { 2 } .
$$

## 4.2 Definition and Elementary Properties of L<sup>p</sup> Spaces

**Definition.** Let $p \in \mathbb { R }$ with $1 < p < \infty$ ; we set

$$
L ^ { p } ( \Omega ) = \left\{ f : \Omega \to \mathbb { R } ;   f \mathrm { i s m e a s u r a b l e a n d }   | f | ^ { p } \in L ^ { 1 } ( \Omega ) \right\}
$$

with

$$
\| f \| _ { L ^ { p } } = \| f \| _ { p } = \left[ \int _ { \Omega } | f ( x ) | ^ { p } d \mu \right] ^ { 1 / p } .
$$

We shall check later on that $\parallel \parallel p$ is a norm.

**Definition.** We set

$$
L ^ { \infty } ( \Omega ) = \left\{ f : \Omega \to \mathbb { R } \Bigg | _ { \begin{aligned} { } & { { } f \mathrm { ~ i s ~ m e a s u r a b l e ~ a n d ~ t h e r e ~ i s ~ a ~ c o n s t a n t ~ } C } \\ { } & { { } \mathrm { s u c h ~ t h a t ~ } | f ( x ) | \leq C \mathrm { ~ a . e . ~ o n ~ } \Omega } \end{aligned} } \right\}
$$

with

$$
\| f \| _ { L ^ { \infty } } = \| f \| _ { \infty } = \operatorname* { i n f } \{ C ; | f ( x ) | \leq C { \mathrm { ~ a . e . ~ o n ~ } } \Omega \} .
$$

The following remark implies that $\parallel \parallel \infty$ is a norm:

Remark 1. If $f \in L ^ { \infty }$ then we have

$$
| f ( x ) | \leq \| f \| _ { \infty } \quad \mathrm { a . e . ~ o n } \quad \Omega .
$$

Indeed, there exists a sequence $C _ { n }$ such that $C _ { n } \to \| f \| _ { \infty }$ and for each n, $| f ( x ) | \leq$ $C _ { n }$ a.e. on $\Omega .$ Therefore $| f ( x ) |   \leq   C _ { n }$ for all $x \; \in \; \Omega \backslash E _ { n }$ , with $| E _ { n } |   =   0$ . We set

$E = \cup _ { n = 1 } ^ { \infty } E _ { n }$ , so that $| E | = 0$ and

$$
| f ( x ) | \leq C _ { n } \quad \forall n , \quad \forall x \in \Omega \backslash E ;
$$

it follows that $| f ( x ) | \leq \| f \| _ { \infty } \quad \forall x \in \Omega \backslash E$

**Notation.** Let $1 \leq p \leq \infty ;$ we denote by $p ^ { \prime }$ the conjugate exponent,

$$
\boxed { \frac { 1 } { p } + \frac { 1 } { p ^ { \prime } } = 1 . }
$$

• **Theorem 4.6 (Hölder’s inequality).** Assume that $f \in L ^ { p }$ and $g \in L ^ { p ^ { \prime } }$ with $1 \leq p \leq \infty$ . Then $f g \in L ^ { 1 }$ and

$$
\boxed { \int | f g | \leq \| f \| _ { p } \| g \| _ { p ^ { \prime } } . }\tag{1}
$$

Proof. The conclusion is obvious if $p   =   1 \; \mathrm { o r } \; p   =   \infty ;$ therefore we assume that $1 < p < \infty$ . We recall Young’s inequality:<sup>1</sup>

$$
\boxed { a b \leq \frac { 1 } { p } a ^ { p } + \frac { 1 } { p ^ { \prime } } b ^ { p ^ { \prime } } \quad \forall a \geq 0 , \quad \forall b \geq 0 . }\tag{2}
$$

Inequality (2) is a straightforward consequence of the concavity of the function log on $( 0 , \infty )$

$$
\log \left( { \frac { 1 } { p } } a ^ { p } + { \frac { 1 } { p ^ { \prime } } } b ^ { p ^ { \prime } } \right) \geq { \frac { 1 } { p } } \log   a ^ { p } + { \frac { 1 } { p ^ { \prime } } } \log   b ^ { p ^ { \prime } } = \log   a b .
$$

We have

$$
| f ( x ) g ( x ) | \leq \frac { 1 } { p } | f ( x ) | ^ { p } + \frac { 1 } { p ^ { \prime } } | g ( x ) | ^ { p ^ { \prime } }   \mathrm { a . e . }   x \in \Omega .
$$

It follows that $f g \in L ^ { 1 }$ and

$$
\int | f g | \leq \frac{1}{p} \big \| f \big \|_p^p + \frac{1}{p'} \big \| g \big \|_{p'}^{p'}.\tag{3}
$$

Replacing f by $\lambda f ( \lambda > 0 )$ in (3), yields

$$
\int | f g | \leq \frac { \lambda ^ { p - 1 } } { p } \big \| f \big \| _ { p } ^ { p } + \frac { 1 } { \lambda p ^ { \prime } } \big \| g \big \| _ { p ^ { \prime } } ^ { p ^ { \prime } } .\tag{4}
$$

Choosing $\lambda   =   \| f \| _ { p } ^ { - 1 } \| g \| _ { p } ^ { p ^ { \prime } / p ^ { \prime } }$ (so as to minimize the right-hand side in (4)), we obtain (1).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">b ≤ εa + Cεb</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">− /(p− )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 It is sometimes convenient to use the form a p pwith Cε = ε 1 1.</span></small>

Remark 2. It is useful to keep in mind the following extension of Hölder’s inequality: Assume that $f _ { 1 } ,   f _ { 2 } , \ldots ,   f _ { k }$ are functions such that

$$
f _ { i } \in L ^ { p _ { i } } , 1 \leq i \leq k { \mathrm { ~ w i t h ~ } } { \frac { 1 } { p } } = { \frac { 1 } { p _ { 1 } } } + { \frac { 1 } { p _ { 2 } } } + \cdots + { \frac { 1 } { p _ { k } } } \leq 1 .
$$

Then the product $f = f _ { 1 } f _ { 2 } \cdots f _ { k }$ belongs to $L ^ { p }$ and

$$
\| f \| _ { p } \leq \| f _ { 1 } \| _ { p _ { 1 } } \| f _ { 2 } \| _ { p _ { 2 } } \cdots \| f _ { k } \| _ { p _ { k } } .
$$

In particular, if $f \in L ^ { p } \cap L ^ { q }$ with $1 \leq p \leq q \leq \infty$ , then $f \in L ^ { r }$ for all $r , p \leq r \leq q$ and the following “interpolation inequality” holds:

$$
\| f \| _ { r } \leq \| f \| _ { p } ^ { \alpha } \| f \| _ { q } ^ { 1 - \alpha } , \mathrm { w h e r e } \frac { 1 } { r } = \frac { \alpha } { p } + \frac { 1 - \alpha } { q } , 0 \leq \alpha \leq 1 ;
$$

see Exercise 4.4.

**Theorem 4.7.** $L ^ { p }$ is a vector space and $\parallel \parallel p$ is a norm for any p, $1 \leq p \leq \infty .$

Proof. The cases $p = 1$ and $p = \infty$ are clear. Therefore we assume $1   <   p   <   \infty$ and let $f , g \in L ^ { p }$ . We have

$$
| f ( x ) + g ( x ) | ^ { p } \leq ( | f ( x ) | + | g ( x ) | ) ^ { p } \leq 2 ^ { p } ( | f ( x ) | ^ { p } + | g ( x ) | ^ { p } ) .
$$

Consequently, $f + g \in L ^ { p }$ . On the other hand,

$$
\| f + g \| _ { p } ^ { p } = \int | f + g | ^ { p - 1 } | f + g | \leq \int | f + g | ^ { p - 1 } | f | + \int | f + g | ^ { p - 1 } | g | .
$$

But $| f + g | ^ { p - 1 } \in L ^ { p ^ { \prime } }$ , and by Hölder’s inequality we obtain

$$
\| f + g \| _ { p } ^ { p } \leq \| f + g \| _ { p } ^ { p - 1 } ( \| f \| _ { p } + \| g \| _ { p } ) ,
$$

i.e., $\| f + g \| _ { p } \leq \| f \| _ { p } + \| g \| _ { p } .$

• **Theorem 4.8 (Fischer–Riesz).** $L ^ { p }$ is a Banach space for any p, $1 \leq p \leq \infty .$

Proof. We distinguish the cases $p = \infty$ and $1 \leq p < \infty$

Case 1: $p = \infty . \operatorname { L e t } \left( f _ { n } \right)$ be a Cauchy sequence is $L ^ { \infty }$ . Given an integer $k \geq 1$ there is an integer $N _ { k }$ such that $\begin{array} { r } { \| f _ { m } - f _ { n } \| _ { \infty } \leq \frac { 1 } { k } } \end{array}$ for m, $n \geq N _ { k }$ . Hence there is a null set $E _ { k }$ such that

$$
| f _ { m } ( x ) - f _ { n } ( x ) | \leq \frac { 1 } { k } \quad \forall x \in \Omega \backslash E _ { k } , \quad \forall m , n \geq N _ { k } .\tag{5}
$$

Then we let $E = \bigcup_{k} E_{k}  —  \mathrm{s}\mathrm{o}$ that E is a null set—and we see that for all $x \in \Omega \backslash E$ the sequence $f _ { n } ( x )$ is Cauchy (in R). Thus $f _ { n } ( x ) \to f ( x )$ for all $x \in \Omega \backslash E$ . Passing to the limit in (5) as $m \to \infty$ we obtain

$$
| f ( x ) - f _ { n } ( x ) | \leq { \frac { 1 } { k } } \quad { \mathrm { f o r ~ a l l } } \; x \in \Omega \backslash E , \quad \forall n \geq N _ { k } .
$$

We conclude that $f   \in   L ^ { \infty }$ and $\begin{array} { r } { \| f   -   f _ { n } \| _ { \infty }   \leq   \frac { 1 } { k } \quad \forall n   \geq   N _ { k } } \end{array}$ ; therefore $f _ { n } \to f$ in $L ^ { \infty }$

**Case 2:** $\mathbf { 1 } \leq p < \infty$ **.** Let $( f _ { n } )$ be a Cauchy sequence in $L ^ { p }$ . In order to conclude, it suffices to show that a subsequence converges in $L ^ { p }$

We extract a subsequence $( f _ { n _ { k } } )$ such that

$$
\| f _ { n _ { k + 1 } } - f _ { n _ { k } } \| _ { p } \leq { \frac { 1 } { 2 ^ { k } } } \quad \forall k \geq 1 .
$$

[One proceeds as follows: choose $n _ { 1 }$ such that $\begin{array} { r } { \| f _ { m } - f _ { n } \| _ { p }   \leq   \frac { 1 } { 2 } } \end{array}$ ∀m, $n \geq n _ { 1 } ;$ then choose $n _ { 2 } \geq n _ { 1 }$ such that $\begin{array} { r } { \| \mathbf { \nabla } f _ { m } - f _ { n } \| _ { p } \leq \frac { 1 } { 2 ^ { 2 } } \quad \forall m , n \geq n _ { 2 } \quad \mathsf { e t c . } ] } \end{array}$ We claim that $f _ { n _ { k } }$ converges in $L ^ { p }$ . In order to simplify the notation we write $f _ { k }$ instead of $f _ { n _ { k } }$ , so that we have

$$
\| f _ { k + 1 } - f _ { k } \| _ { p } \leq { \frac { 1 } { 2 ^ { k } } } \quad \forall k \geq 1 .\tag{6}
$$

Let

$$
g _ { n } ( x ) = \sum _ { k = 1 } ^ { n } | f _ { k + 1 } ( x ) - f _ { k } ( x ) | ,
$$

so that

$$
\| g _ { n } \| _ { p } \leq 1 .
$$

As a consequence of the monotone convergence theorem, $g _ { n } ( x )$ tends to a finite limit, say $g ( x )$ , a.e. on $\Omega ,$ with $g \in L ^ { p }$ . On the other hand, for $m \geq n \geq 2$ we have

$$
| f _ { m } ( x ) - f _ { n } ( x ) | \leq | f _ { m } ( x ) - f _ { m - 1 } ( x ) | + \cdots + | f _ { n + 1 } ( x ) - f _ { n } ( x ) | \leq g ( x ) - g _ { n - 1 } ( x ) .
$$

It follows that a.e. on , $f _ { n } ( x )$ is Cauchy and converges to a finite limit, say $f ( x )$ We have a.e. on $\Omega .$ ,

$$
| f ( x ) - f _ { n } ( x ) | \leq g ( x ) \quad { \mathrm { ~ f o r ~ } } n \geq 2 ,\tag{7}
$$

and in particular $f \in L ^ { p }$ . Finally, we conclude by dominated convergence that $\| f _ { n } - f \| _ { p } \to 0$ , since $| f _ { n } ( x ) - f ( x ) | ^ { p } \to 0 \; { \mathrm { a . e } }$ . and also $| f _ { n } - f | ^ { p } \leq g ^ { p } \in L ^ { 1 }$

**Theorem 4.9.** Let $( f _ { n } )$ be a sequence in L<sup>p</sup> and let $f \in L ^ { p }$ be such that $\| f _ { n } - f \| _ { p }$ $\rightarrow 0$

Then, there exist a subsequence $( f _ { n _ { k } } )$ and a function $h \in L ^ { p }$ such that

(a) $f _ { n _ { k } } ( x ) \to   f ( x ) \; \mathrm { a . e . } \; o n \; \Omega ,$

(b) $| f _ { n _ { k } } ( x ) | \leq h ( x ) \quad \forall k ,   \mathrm { a . e . } \; o n \; \Omega .$

Proof. The conclusion is obvious when $p = \infty$ . Thus we assume $1 \leq p < \infty$ . Since $( f _ { n } )$ is a Cauchy sequence we may go back to the proof of Theorem 4.8 and consider a subsequence $( f _ { n _ { k } } )$ —denoted by $(f_k)  —   satisfying  (6)$ , such that $f _ { k } ( x )$ tends a.e. to a limi $\mathrm { t } ^ { 2 } \bar { f } ^ { \star } ( x )$ with $f ^ { \star } \in L ^ { p }$ . Moreover, by $( 7 )$ , we have $| f ^ { \star } ( x ) - f _ { k } ( x ) |   \leq   g ( x )$ $\forall k$ , a.e. on  with $g \in L ^ { p }$ . By dominated convergence we know that $f _ { k } \to f ^ { \star }$ in $L ^ { p }$ and thus $f = f ^ { \star } \; \mathrm { a . e }$ . In addition, we also have $| f _ { k } ( x ) | \leq | f ^ { \star } ( x ) | + g ( x )$ , and the conclusion follows.

## 4.3 Reflexivity. Separability. Dual of $L ^ { p }$

We shall consider separately the following three cases:

(A) $1 < p < \infty ,$

(B) $p = 1 ,$

(C) $p = \infty .$

A. Study of $L ^ { p } ( \mathbf { \Omega } )$ for $\mathbf { 1 } < p < \infty$

This case is the most “favorable”: $L ^ { p }$ is reflexive, separable, and the dual of $L ^ { p }$ is $L ^ { p ^ { \prime } }$

• **Theorem 4.10.** $L ^ { p }$ is reflexive for any p, $1 < p < \infty .$

The proof consists of three steps:

Step 1 (Clarkson’s first inequality). Let $2 \leq p < \infty$ . We claim that

$$
\left\| \frac{f + g}{2} \right\|_p^p + \left\| \frac{f - g}{2} \right\|_p^p \leq \frac{1}{2} (\|f\|_p^p + \|g\|_p^p) \quad \forall f, g \in L^p.\tag{8}
$$

Proof of (8). Clearly, it suffices to show that

$$
\left| \frac{a + b}{2} \right|^p + \left| \frac{a - b}{2} \right|^p \leq \frac{1}{2} (|a|^p + |b|^p) \quad \forall a, b \in \mathbb{R}.
$$

First we note that

$$
\alpha ^ { p } + \beta ^ { p } \leq ( \alpha ^ { 2 } + \beta ^ { 2 } ) ^ { p / 2 } \quad \forall \alpha , \beta \geq 0
$$

(by homogeneity, assume $\beta = 1$ and observe that the function

$$
( x ^ { 2 } + 1 ) ^ { p / 2 } - x ^ { p } - 1
$$

increases on $[ 0 , \infty ) )$ . Choosing $\begin{array} { r } { \alpha = | \frac { a + b } { 2 } | } \end{array}$ and $\begin{array} { r } { \beta = | \frac { a - b } { 2 } | } \end{array}$ , we obtain

$$
\left| \frac{a + b}{2} \right|^p + \left| \frac{a - b}{2} \right|^p \leq \left( \left| \frac{a + b}{2} \right|^2 + \left| \frac{a - b}{2} \right|^2 \right)^{p/2} = \left( \frac{a^2}{2} + \frac{b^2}{2} \right)^{p/2} \leq \frac{1}{2}(|a|^p + |b|^p).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">nk x x a.e f ( ) → f -( ) .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 f\*:</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">fn → f</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">A priori one should distinguish f and f -: by assumption  in L , and on the other hand,</span></small>

(the last inequality follows from the convexity of the function $x \; \mapsto \; | x | ^ { p / 2 }$ since $p \geq 2 )$ .

Step 2: $L ^ { p }$ is uniformly convex, and thus reflexive for $2   \leq   p   <   \infty$ . Indeed, let $\varepsilon > 0$ and let $f , g \in L ^ { p }$ with $\| f \| _ { p } \leq 1$ , $g \| _ { p } \leq 1$ , and $\| f - g \| _ { p } > \varepsilon$ . We deduce from (8) that

$$
\left\| \frac{f + g}{2} \right\|_p^p < 1 - \left( \frac{\varepsilon}{2} \right)^p
$$

and thus $\begin{array} { r } { \| \frac { f + g } { 2 } \| _ { p } \; < \; 1   -   \delta } \end{array}$ with $\delta   =   1   -   [ 1   -   ( \textstyle \frac { \varepsilon } { 2 } ) ^ { p } ] ^ { 1 / p } \; > \; 0$ . Therefore, $L ^ { p }$ is uniformly convex and thus reflexive by Theorem 3.31.

Step 3: $L ^ { p }$ is reflexive for $1 < p \leq 2 .$

Proof. Let $1 < p < \infty$ . Consider the operator $T : L ^ { p } \to { ( L ^ { p ^ { \prime } } ) } ^ { \star }$ defined as follows: Let $u \in L ^ { p }$ be fixed; the mapping $\textstyle f \in L ^ { p ^ { \prime } } \mapsto \int u f$ is a continuous linear functional on $L ^ { p ^ { \prime } }$ and thus it defines an element, say $T u .$ , in $( L ^ { p ^ { \prime } } ) ^ { \star }$ such that

$$
\langle T u ,   f \rangle = \int u   f \quad \forall f \in L ^ { p ^ { \prime } } .
$$

We claim that

(9)

$$
\| T u \| _ { ( L ^ { p ^ { \prime } } ) ^ { \star } } = \| u \| _ { p } \quad \forall u \in L ^ { p } .
$$

Indeed, by Hölder’s inequality, we have

$$
| \langle T u ,   f \rangle | \leq \| u \| _ { p } \| f \| _ { p ^ { \prime } } \quad \forall f \in L ^ { p ^ { \prime } }
$$

and therefore $\| T u \| _ { { ( L ^ { p ^ { \prime } } ) } ^ { \star } } \leq \| u \| _ { p }$

On the other hand, set

$$
f _ { 0 } ( x ) = | u ( x ) | ^ { p - 2 } u ( x ) \quad ( f _ { 0 } ( x ) = 0 \; { \mathrm { i f } } \; u ( x ) = 0 ) .
$$

Clearly we have

$$
f _ { 0 } \in L ^ { p ^ { \prime } } , \| f _ { 0 } \| _ { p ^ { \prime } } = \left\| u \right\| _ { p } ^ { p - 1 } \quad \mathrm { a n d } \quad \langle T u ,   f _ { 0 } \rangle = \| u \| _ { p } ^ { p } ;
$$

thus

(10)

$$
\| T u \| _ { ( L ^ { p ^ { \prime } } ) ^ { \star } } \geq \frac { \langle T u ,   f _ { 0 } \rangle } { \| f _ { 0 } \| _ { p ^ { \prime } } } = \| u \| _ { p } .
$$

Hence, we have shown that $T$ is an isometry from $L ^ { p }$ into $( L ^ { p ^ { \prime } } ) ^ { \star }$ , which implies that $T ( L ^ { p } )$ is a closed subspace of $( L ^ { p ^ { \prime } } ) ^ { \star }$ (because $L ^ { p }$ is a Banach space).

Assume now $1 < p \leq 2$ . Since $L ^ { p ^ { \prime } }$ is reflexive (by Step 2), it follows that $( L ^ { p ^ { \prime } } ) ^ { \star }$ is also reflexive (Corollary 3.21). We conclude, by Proposition 3.20, that $T ( L ^ { p } )$ is reflexive, and as a consequence, $L ^ { p }$ is also reflexive.

Remark 3. In fact, $L ^ { p }$ is also uniformly convex for $1 < p \leq 2$ . This is a consequence of Clarkson’s second inequality, which holds for $1 < p \leq 2$

$$
\left\| \frac{f + g}{2} \right\|_p^{p'} + \left\| \frac{f - g}{2} \right\|_p^{p'} \leq \left( \frac{1}{2} \| f \|_p^p + \frac{1}{2} \| g \|_p^p \right)^{1/(p-1)} \quad \forall f, g \in L^p.
$$

This inequality is trickier to prove than Clarkson’s first inequality (see, e.g., Problem 20 or E. Hewitt–K. Stromberg [1]). Clearly, it implies that $L ^ { p }$ is uniformly convex when $1 < p \leq 2 ;$ ; for another approach, see also C. Morawetz [1] (Exercise 4.12) or J. Diestel [1].

• **Theorem 4.11 (Riesz representation theorem).** Let $1 \; < \; p \; < \;$ ∞ and let $\phi \in$ $( L ^ { p } ) ^ { \star }$ . Then there exists a unique function $u \in L ^ { p ^ { \prime } }$ such that

$$
\langle \phi ,   f \rangle = \int   u f \quad \forall f \in L ^ { p } .
$$

Moreover,

$$
\left\| u \right\| _ { p ^ { \prime } } = \left\| \phi \right\| _ { \left( L ^ { p } \right) ^ { \star } } .
$$

Remark 4. Theorem 4.11 is very important. It says that every continuous linear functional on $L ^ { p }$ with $1 < p < \infty$ can be represented “concretely” as an integral. The mapping $\phi \mapsto u$ , which is a linear surjective isometry, allows us to identify the “abstract” space $( L ^ { p } ) ^ { \star }$ with $L ^ { p ^ { \prime } }$

In what follows, we shall systematically make the identification

$$
\boxed { ( L ^ { p } ) ^ { \star } = L ^ { p ^ { \prime } } . }
$$

Proof. We consider the operator $T \: : \: L ^ { p ^ { \prime } } \: \rightarrow \: ( L ^ { p } ) ^ { \star }$ defined by $\begin{array} { r } { \langle T u , f \rangle   =   \int u f } \end{array}$ $\forall u   \in   L ^ { p ^ { \prime } } ,   \forall f   \in   L ^ { p }$ . The argument used in the proof of Theorem 4.10 (Step 3) shows that

$$
\| T u \| _ { ( L ^ { p } ) ^ { \star } } = \| u \| _ { p ^ { \prime } } \quad \forall u \in L ^ { p ^ { \prime } } .
$$

We claim that T is surjective. Indeed, let $E = T ( L ^ { p ^ { \prime } } )$ . Since E is a closed subspace, it suffices to prove that E is dense in $( L ^ { p } ) ^ { \star }$ . Let $h   \in   ( L ^ { p } ) ^ { \star \star }$ satisfy $\langle h , T u \rangle = 0$ $\forall u \in L ^ { p ^ { \prime } }$ . Since $L ^ { p }$ is reflexive, $h \in L ^ { p }$ , and satisfies $\boldsymbol { u } h = 0   \forall \boldsymbol { u } \in L ^ { p ^ { \prime } }$ . Choosing $u = | h | ^ { p - 2 } h$ , we see that $h = 0$

**Theorem 4.12.** The space $C _ { c } ( \mathbb { R } ^ { N } )$ is dense in $L ^ { p } ( \mathbb { R } ^ { N } )$ for any p, $1 \leq p < \infty$

Before proving Theorem 4.12, we introduce some notation.

**Notation.** The truncation operation $T _ { n } : \mathbb { R } \to \mathbb { R }$ is defined by

$$
T_{n}r=\begin{cases}r & \quad  if   |r| \leq n, \\\frac{nr}{|r|} & \quad  if   |r| > n.\end{cases}
$$

Given a set $E \subset \Omega$ , we define the characteristic $f u n c t i o n ^ { 3 } \chi _ { E }$ to be

$$
\chi _ { E } ( x ) = \left\{ \begin{aligned} & 1 & \quad &  if   x \in E, \\ & 0 & \quad &  if   x \in \Omega \backslash E. \end{aligned} \right.
$$

Proof. First, we claim that given $f   \in   L ^ { p } ( \mathbb { R } ^ { N } )$ and $\varepsilon   >   0$ there exist a function $g \in \dot { L } ^ { \infty } ( \mathbb { R } ^ { N } )$ and a compact set K in $\mathbb { R } ^ { N }$ such that $g = 0$ outside K and

$$
\| f - g \| _ { p } < \varepsilon .\tag{11}
$$

Indeed, let $\chi _ { n }$ be the characteristic function of $B ( 0 , n )$ and let $f _ { n }   =   \chi _ { n } T _ { n }   f$ . By dominated convergence we see that $\| f _ { n } \mathrm { ~ - ~ } f \| _ { p } \; \to \; 0$ and thus we may choose $g   =   f _ { n }$ with n large enough. Next, given $\delta   >   0$ there exists (by Theorem 4.3) a function $g _ { 1 } \in C _ { c } ( \mathbb { R } ^ { N } )$ such that

$$
\| g - g _ { 1 } \| _ { 1 } < \delta .
$$

We may always assume that $\| g _ { 1 } \| _ { \infty } \leq \| g \| _ { \infty }$ ; otherwise, we replace $g _ { 1 }$ by $T _ { n } g _ { 1 }$ with $n = \| g \| _ { \infty }$ . Finally, we have

$$
\left\| g - g _ { 1 } \right\| _ { p } \leq \left\| g - g _ { 1 } \right\| _ { 1 } ^ { 1 / p } \left\| g - g _ { 1 } \right\| _ { \infty } ^ { 1 - ( 1 / p ) } \leq \delta ^ { 1 / p } ( 2 \left\| g \right\| _ { \infty } ) ^ { 1 - ( 1 / p ) } .
$$

We conclude by choosing $\delta > 0$ small enough that

$$
\delta ^ { 1 / p } ( 2 \| g \| _ { \infty } ) ^ { 1 - ( 1 / p ) } < \varepsilon .
$$

**Definition.** The measure space  is called separable if there is a countable family $( E _ { n } )$ of members of M such that the σ-algebra generated by $( E _ { n } )$ coincides with M (i.e., M is the smallest σ -algebra containing all the $E _ { n }   ^ { \prime } \mathrm { s ) }$

**Example.** The measure space $\Omega = \mathbb { R } ^ { N }$ is separable. Indeed, we may choose for $( E _ { n } )$ any countable family of open sets such that every open set in $\mathbb { R } ^ { N }$ can be written as a union of $E _ { n }   ^ { \prime } \mathrm { s }$ . More generally, if  is a separable metric space and M consists of the Borel sets $( \mathrm { i . e . } , \mathcal { M }$ is the σ-algebra generated by the open sets in ), then  is a separable measure space.

**Theorem 4.13.** Assume that  is a separable measure space. Then $L ^ { p } ( \Omega )$ is separable for any p, $1 \leq p < \infty$

We shall consider only the case $\Omega   =   \mathbb { R } ^ { N }$ , since the general case is somewhat tricky. Note that as a consequence, $L ^ { p } ( \Omega )$ is also separable for any measurable set $\dot { \Omega } \subset \mathbb { R } ^ { N }$ . Indeed, there is a canonical isometry from $L ^ { p } ( \Omega )$ into $L ^ { p } ( \mathbb { R } ^ { N } )$ (the extension by 0 outside ); therefore $L ^ { p } ( \Omega )$ may be identified with a subspace of $L ^ { p } ( \mathbb { R } ^ { N } )$ and hence $L ^ { p } ( \Omega )$ is separable (by Proposition 3.25).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3 Not to be confused with the indicator function I introduced in Chapter 1.</span></small>

Proof of Theorem 4.13 when $\Omega = \mathbb { R } ^ { N }$ . Let $\mathcal { R }$ denote the countable family of sets in $\dot { \mathbb { R } ^ { N } }$ of the form $\begin{array} { r } { R   =   \prod _ { k = 1 } ^ { N } ( a _ { k } , b _ { k } ) } \end{array}$ with $a _ { k } , b _ { k }   \in   \mathbb { Q }$ . Let $\mathcal { E }$ denote the vector space over $\mathbb { Q }$ generated by the functions $( \chi _ { R } ) _ { R \in \mathcal { R } }$ , that is, $\mathcal { E }$ consists of finite linear combinations with rational coefficients of functions $\chi _ { R }$ , so that $\mathcal { E }$ is countable.

We claim that $\mathcal { E }$ is dense in $L ^ { p } ( \mathbb { R } ^ { N } )$ . Indeed, given $f   \in   L ^ { p } ( \mathbb { R } ^ { N } )$ and $\varepsilon   >   0 .$ there exists some $f _ { 1 } \in C _ { c } ( \mathbb { R } ^ { N } )$ such that $\| f - f _ { 1 } \| _ { p } < \varepsilon . \operatorname { L e t } R \in { \mathcal { R } }$ be any cube containing supp $f _ { 1 }$ (the support of $f _ { 1 } )$ . Given $\delta > 0$ it is easy to construct a function $f _ { 2 }   \in   \mathcal { E }$ such that $\| f _ { 1 } - f _ { 2 } \| _ { \infty }   <   \delta$ and $f _ { 2 }$ vanishes outside R: it suffices to split R into small cubes of R where the oscillation $( \mathrm { i . e . ,   s u p - i n f } )$ of $f _ { 1 }$ is less than $\delta .$ Therefore we have $\| f _ { 1 } - f _ { 2 } \| _ { p } \leq \| f _ { 1 } - f _ { 2 } \| _ { \infty } | R | ^ { 1 / p } < \delta | R | ^ { 1 / p }$ . We conclude that $\| f - f _ { 2 } \| _ { p } < 2 \varepsilon$ , provided $\delta > 0$ is chosen so that $\delta | R | ^ { 1 / p } < \varepsilon$

## B. Study of ${ \cal L } ^ { 1 } ( { \bf \Omega } )$

We start with a description of the dual space of $L ^ { 1 } ( \Omega )$

• **Theorem 4.14 (Riesz representation theorem).** Let $\phi \in ( L ^ { 1 } ) ^ { \star }$ . Then there exists a unique function $u \in L ^ { \infty }$ such that

$$
\langle \phi ,   f \rangle = \int u f \quad \forall f \in L ^ { 1 } .
$$

Moreover,

$$
\| u \| _ { \infty } = \| \phi \| _ { ( L ^ { 1 } ) ^ { \star } } .
$$

• Remark 5. Theorem 4.14 asserts that every continuous linear functional on $L ^ { 1 }$ can be represented “concretely” as an integral. The mapping $\phi \mapsto u$ , which is a linear surjective isometry, allows us to identify the “abstract” space $( L ^ { 1 } ) ^ { \star }$ with $L ^ { \infty }$ . In what follows, we shall systematically make the identification

$$
\boxed { ( L ^ { 1 } ) ^ { \star } = L ^ { \infty } . }
$$

Proof. Let $( \Omega _ { n } )$ be a sequence of measurable sets in  such that $\Omega = \cup _ { n = 1 } ^ { \infty } \Omega _ { n }$ and $| \Omega _ { n } | < \infty \quad \forall n$ . Set $\chi _ { n } = \chi _ { \Omega _ { n } }$

The uniqueness of u is obvious. Indeed, suppose $u \in L ^ { \infty }$ satisfies

$$
\int u f = 0 \quad \forall f \in L ^ { 1 } .
$$

Choosing $f = \chi _ { n }$ sign u (throughout this book, we use the convention that sign $0 =$ 0), we see that $u = 0 \; \mathrm { a . e }$ . on $\Omega _ { n }$ and thus $u = 0 \mathrm { ~ a . e . ~ o n ~ } \Omega$

We now prove the existence of u. First, we construct a function $\theta \in L ^ { 2 } ( \Omega )$ such that

$$
\theta ( x ) \geq \varepsilon _ { n } > 0 \quad \forall x \in \Omega _ { n } .
$$

It is clear that such a function θ exists. Indeed, we define $\theta$ to be $\alpha _ { 1 }$ on $\Omega _ { 1 }$ , α<sub>2</sub> on $\Omega _ { 2 } \backslash \Omega _ { 1 } , \ldots , \alpha _ { n }$ on $\Omega _ { n } \backslash \Omega _ { n - 1 }$ , etc., and we adjust the constants $\alpha _ { n } > 0$ in such a way that $\theta \in L ^ { 2 }$

The mapping $f \in L ^ { 2 } ( \Omega ) \mapsto \langle \phi , \theta f \rangle$ is a continuous linear functional on $L ^ { 2 } ( \Omega )$ $\mathbf { B } \mathrm { y }$ Theorem 4.11 (applied with $p = 2 )$ there exists a function $v \in L ^ { 2 } ( \Omega )$ such that

$$
\langle \phi , \theta f \rangle = \int v f \quad \forall f \in L ^ { 2 } ( \Omega ) .\tag{12}
$$

Set $u ( x ) = v ( x ) / \theta ( x )$ . Clearly, u is well defined since $\theta > 0$ on $\Omega ;$ moreover, u is measurable and $u \chi _ { n } \in L ^ { 2 } ( \Omega )$ . We claim that u has all the required properties. We have

$$
\langle \phi ,   \chi _ { n } g \rangle = \int u   \chi _ { n } g \quad \forall g \in L ^ { \infty } ( \Omega ) \quad \forall n .\tag{13}
$$

Indeed, it suffices to choose $f   =   \chi _ { n } g / \theta$ in (12) (note that $f   \in   L ^ { 2 } ( \Omega )$ since $f$ is bounded on $\Omega _ { n }$ and $f = 0$ outside $\Omega _ { n } )$

Next, we claim that $u \in L ^ { \infty } ( \Omega )$ and that

$$
\| u \| _ { \infty } \leq \| \phi \| _ { ( L ^ { 1 } ) ^ { \star } } .\tag{14}
$$

Fix any constant $C > \| \phi \| _ { ( L ^ { 1 } ) } ,$ - and set

$$
A = \{ x \in \Omega ; | u ( x ) | > C \} .
$$

Let us verify that A is a null set. Indeed, by choosing $g = \chi _ { A }$ sign u in (13) we obtain

$$
\int _ { A \cap \Omega _ { n } } | u | \leq \| \phi \| _ { ( L ^ { 1 } ) ^ { \star } } | A \cap \Omega _ { n } |
$$

and therefore

$$
C | A \cap \Omega _ { n } | \leq \| \phi \| _ { ( L ^ { 1 } ) ^ { \star } } | A \cap \Omega _ { n } | .
$$

It follows that $| A \cap \Omega _ { n } | = 0 \quad \forall n$ , and thus A is a null set. This concludes the proof of (14).

Finally, we claim that

$$
\langle \phi , h \rangle = \int u h \quad \forall h \in L ^ { 1 } ( \Omega ) .\tag{15}
$$

Indeed, it suffices to choose $g = T _ { n } h$ (truncation of h) in (13) and to observe that $\chi _ { n } T _ { n } h \to h$ in $L ^ { 1 } ( \Omega )$

In order to complete the proof of Theorem 4.14 it remains only to check that $\| u \| _ { \infty } = \| \phi \| _ { ( L ^ { 1 } ) ^ { \star } }$ . We have, by (15),

$$
| \langle \phi , h \rangle | \leq \| u \| _ { \infty } \| h \| _ { 1 } \quad \forall h \in L ^ { 1 } ( \Omega ) ,
$$

and therefore $\| \phi \| _ { ( L ^ { 1 } ) ^ { \star } } \leq \| u \| _ { \infty }$ . We conclude with the help of (14).

• Remark 6. The space $L ^ { 1 } ( \Omega )$ is never reflexive except in the trivial case where  consists of a finite number of atoms—and then $L ^ { 1 } ( \Omega )$ is finite-dimensional. Indeed suppose, by contradiction, that $L ^ { 1 } ( \Omega )$ is reflexive and consider two cases:

(i) $\forall \varepsilon > 0   \exists \omega \subset \Omega$ measurable with $0 < \mu ( \omega ) < \varepsilon$

(ii) $\exists \varepsilon > 0$ such that $\mu ( \omega ) \geq \varepsilon$ for every measurable set $\omega \subset \Omega$ with $\mu ( \omega ) > 0$

In Case (i) there is a decreasing sequence $( \omega _ { n } )$ of measurable sets such that $\mu ( \omega _ { n } ) \; > \; 0$ ∀n and $\mu ( \omega _ { n } ) \; \rightarrow \; 0$ [choose first any sequence $( \omega _ { k } ^ { \prime } )$ such that $0 ~ <$ $\mu ( \omega _ { k } ^ { \prime } ) < 1 / 2 ^ { k }$ and then set $\omega _ { n } = \bigcup _ { k = n } ^ { \infty } \omega _ { k } ^ { \prime } ]$

Let $\chi _ { n } ~ = ~ \chi _ { \omega _ { n } }$ and define $u _ { n } = \chi _ { n } / \| \chi _ { n } \| _ { 1 }$ . Since $\| u _ { n } \| _ { 1 } ~ = ~ 1$ there is a subsequence—still denoted by un—and some $u \; \in \; L ^ { 1 }$ such that $u _ { n } \; \rightharpoonup \; u$ in the weak topology $\sigma ( L ^ { 1 } , L ^ { \infty } )$ (by Theorem 3.18), i.e.,

$$
\int u _ { n } \phi \rightarrow \int u \phi \quad \forall \phi \in L ^ { \infty } .\tag{16}
$$

On the other hand, for fixed $j ,$ and $n \; > \; j$ we have $\begin{array} { r } { \int u _ { n } \chi _ { j }   =   1 } \end{array}$ . At the limit, as $n \to \infty$ , we obtain $\begin{array} { r } { \int u \chi _ { j } = 1   \forall j } \end{array}$ . Finally, we note (by dominated convergence) that $\begin{array} { r } { \int u \chi _ { j } \rightarrow 0 } \end{array}$ as $j \to \infty  —   a$ contradiction.

In Case (ii) the space  is purely atomic and consists of a countable union of distinct atoms $( a _ { n } )$ (unless there is only a finite number of atoms!). In that case $L ^ { 1 } ( \Omega )$ is isomorphic to $\ell ^ { 1 }$ and it suffices to prove that $\ell ^ { 1 }$ is not reflexive. Consider the canonical basis:

$$
e _ { n } = ( 0 ,   0 , \dots , \underset { ( n ) } { 1 } , 0 , 0 \dots ) .
$$

Assuming $\ell ^ { 1 }$ is reflexive, there exist a subsequence $( e _ { n _ { k } } )$ and some $x \in \ell ^ { 1 }$ such that $e _ { n _ { k } } \rightharpoonup x$ in the weak topology $\sigma ( \ell ^ { 1 } , \ell ^ { \infty } )$ , i.e.,

$$
\langle \varphi , e _ { n _ { k } } \rangle \underset { k \to \infty } { \longrightarrow } \langle \varphi , x \rangle \quad \forall \varphi \in \ell ^ { \infty } .
$$

Choosing

$$
\varphi = \varphi _ { j } = ( 0 , 0 , \dots , \underset { ( j ) } { 1 } , 1 , 1 , \dots )
$$

we find that $\langle \varphi _ { j } , x \rangle   =   1 \; \forall j$ . On the other hand $\langle \varphi _ { j } , x \rangle   \to   0$ as $j   \to   \infty$ (since $x \in \ell ^ { 1 } ) \mathrm { {  —  } a }$ contradiction.

## C. Study of $L ^ { \infty }$

We already know (Theorem 4.14) that $L ^ { \infty }   =   ( L ^ { 1 } ) ^ { \star }$ . Being a dual space, $L ^ { \infty }$ enjoys some nice properties. In particular, we have the following:

(i) The closed unit ball $B _ { L ^ { \infty } }$ is compact in the weak- topology $\sigma ( L ^ { \infty } , L ^ { 1 } )$ (by Theorem 3.16).

(ii) If $\Omega$ is a measurable subset in $\mathbb { R } ^ { N }$ and $( f _ { n } )$ is a bounded sequence in $L ^ { \infty } ( \Omega )$ there exists a subsequence $( f _ { n _ { k } } )$ and some $f \in L ^ { \infty } ( \Omega )$ such that $f _ { n _ { k } } \rightharpoonup f$ in the weak- topology $\sigma ( L ^ { \infty } , L ^ { 1 } )$ (this is a consequence of Corollary 3.30 and Theorem 4.13).

However $L ^ { \infty } ( \Omega )$ is not reflexive, except in the trivial case where  consists of a finite number of atoms; otherwise $L ^ { 1 } ( \Omega )$ would be reflexive (by Corollary 3.21) and we know that $L ^ { 1 }$ is not reflexive (Remark 6). As a consequence, it follows that the dual space $( L ^ { \infty } ) ^ { \star }$ of $L ^ { \infty }$ contains $L ^ { 1 }$ (since $L ^ { \infty } = ( L ^ { 1 } ) ^ { \star } )$ and $( L ^ { \infty } ) ^ { \star }$ is strictly bigger than $L ^ { 1 }$ . In other words, there are continuous linear functionals $\phi$ on $L ^ { \infty }$ which cannot be represented as

$$
\langle \phi ,   f \rangle = \int u f \quad \forall f \in L ^ { \infty } \; { \mathrm { a n d } } \; { \mathrm { s o m e } } \; u \in L ^ { 1 } .
$$

In fact, let us describe a “concrete” example of such a functional. Let $\phi _ { 0 } : C _ { c } ( \mathbb { R } ^ { N } ) \to$ R be defined by

$$
\phi _ { 0 } ( f ) = f ( 0 ) \; { \mathrm { f o r } } \; f \in C _ { c } ( \mathbb { R } ^ { N } ) .
$$

Clearly $\phi _ { 0 }$ is a continuous linear functional on $C _ { c } ( \mathbb { R } ^ { N } )$ for the $\parallel \parallel \infty$ norm. By Hahn– Banach, we may extend $\phi _ { 0 }$ into a continuous linear functional $\phi$ on $L ^ { \infty } ( \mathbb { R } ^ { N } )$ and we have

$$
\langle \phi ,   f \rangle = f ( 0 ) \quad \forall f \in C _ { c } ( \mathbb { R } ^ { N } ) .\tag{17}
$$

Let us verify that there exists no function $u \in L ^ { 1 } ( \mathbb { R } ^ { N } )$ such that

$$
\langle \phi ,   f \rangle = \int u f \quad \forall f \in L ^ { \infty } ( \mathbb { R } ^ { N } ) .\tag{18}
$$

Assume, by contradiction, that such a function u exists. We deduce from (17) and (18) that

$$
\int u f = 0 \quad \forall f \in C _ { c } ( \mathbb { R } ^ { N } ) \; \mathrm { a n d } \; f ( 0 ) = 0 .
$$

Applying Corollary 4.24 (with $\Omega = \mathbb { R } ^ { N } \backslash \{ 0 \} )$ we see that $u = 0 \; \mathrm { a . e . }$ on $\mathbb { R } ^ { N } \backslash \{ 0 \}$ and thus $u = 0 \; \mathrm { a . e }$ . on $\mathbb { R } ^ { N }$ . We conclude (by (18)) that

$$
\langle \phi ,   f \rangle = 0 \quad \forall f \in L ^ { \infty } ( \mathbb { R } ^ { N } ) ,
$$

which contradicts (17).

\- Remark 7. The dual space of $L ^ { \infty }$ does not coincide with $L ^ { 1 }$ but we may still ask the question: what does $( L ^ { \infty } ) ^ { \star }$ look like? For this purpose it is convenient to view $L ^ { \infty } ( \Omega ; \mathbb { C } )$ as a commutative C--algebra (see, e.g., W. Rudin [1]). By Gelfand’s theorem $L ^ { \infty } ( \Omega ; \mathbb { C } )$ is isomorphic and isometric to the space $C ( K ; \mathbb { C } )$ of continuous complex-valued functions on some compact topological space K (K is the spectrum of the algebra $L ^ { \infty } ; K$ is not metrizable except when $\Omega$ consists of a finite number of atoms). Therefore $( L ^ { \infty } ( \Omega ; \mathbb { C } ) ) ^ { \star }$ may be identified with the space of complexvalued Radon measures on K and $L ^ { \infty } ( \Omega ; \mathbb { R } ) ^ { \star }$ may be identified with the space of real-valued Radon measures on K; for more details, see Comment 3 at the end of this chapter, W. Rudin [1] and K. Yosida [1] (p. 118).

Remark 8. The space $L ^ { \infty } ( \Omega )$ is not separable except when  consists of a finite number of atoms. In order to prove this fact it is convenient to use the following.

**Lemma 4.2.** Let E be a Banach space. Assume that there exists a family $( O _ { i } ) _ { i \in I }$ such that

(i) for each $i \in I ,   O _ { i }$ is a nonempty open subset of $E$ ,

(ii) $O _ { i } \cap O _ { j } = \emptyset   i f  i \neq j$

(iii) I is **uncountable**.

Then E is **not** separable.

Proof of Lemma 4.2. Suppose, by contradiction, that E is separable. Let $( u _ { n } ) _ { n \in \mathbb { N } }$ denote a dense countable set in E. For each $i \in I$ , the set $O _ { i } \cap ( u _ { n } ) _ { n \in \mathbb { N } } \neq \emptyset$ and we may choose $n ( i )$ such that $u _ { n ( i ) }   \in   O _ { i }$ . The mapping $i \mapsto n ( i )$ is injective; indeed, if $n ( i )   =   n ( j )$ , then $u _ { n ( i ) }   =   u _ { n ( j ) }   \in   O _ { i }   \cap   O _ { j }$ and thus $i \; = \; j$ . Therefore, I is countable—a contradiction.

We now establish that $L ^ { \infty } ( \Omega )$ is not separable. We claim that there is an uncountable family $( \omega _ { i } ) _ { i \in I }$ of measurable sets in  which are all distinct, that is, the symmetric difference $\omega _ { i }   \Delta   \omega _ { j }$ has positive measure for $i \neq j$ . We then conclude by applying Lemma 4.2 to the family $( O _ { i } ) _ { i \in I }$ defined by

$$
O _ { i } = \{ f \in L ^ { \infty } ( \Omega ) ; \| f - \chi _ { \omega _ { i } } \| _ { \infty } < 1 / 2 \}
$$

(note that $\lVert \chi _ { \omega }   -   \chi _ { \omega ^ { \prime } } \rVert _ { \infty } = 1$ if ω and $\omega ^ { \prime }$ are distinct). The existence of an uncountable family $( \omega _ { i } )$ is clear when  is an open set in $\mathbb { R } ^ { N }$ since we may consider all the balls $B ( x _ { 0 } , r )$ with $x _ { 0 } \in \Omega$ and $r > 0$ small enough.

When  is a general measure space we split  into its atomic part $\Omega _ { a }$ and its nonatomic $( = \mathrm { d i f f u s e } )$ part $\Omega _ { d } ;$ then we distinguish two cases:

(i) $\Omega _ { d }$ is not a null set.

(ii) $\Omega _ { d }$ is a null set.

In Case (i), then for each real number $t , 0   <   t   <   \mu ( \Omega _ { d } )$ , there is a measurable set ω with $\mu ( \omega ) = t ; \mathrm { s e e , e . g . }$ , P. Halmos [1], A. J. Weir [1], or J. Neveu [1]. In this way, we obtain an uncountable family of distinct measurable sets.

In Case (ii)  consists of a countable union of distinct atoms $( a _ { n } )$ (unless  consists of a finite number of atoms). For any collection of integers, $A \subset \mathbb { N }$ , we define $\omega _ { A } = \bigcup _ { n \in \mathbb { A } } a _ { n }$ . Clearly, $( \omega _ { A } )$ is an uncountable family of distinct measurable sets.

The following table summarizes the main properties of the space $L ^ { p } ( \Omega )$ when $\Omega$ is a measurable subset of $\mathbb { R } ^ { N }$ :

|  | Reflexive | Separable | Dual space |
| --- | --- | --- | --- |
| L<sup>p</sup> with 1 &lt; p &lt; ∞ | YES | YES | L<sup>p</sup> |
| L<sup>1</sup> | NO | YES | L∞ |
| L∞ | NO | NO | Strictly bigger than L<sup>1</sup> |

## 4.4 Convolution and regularization

We first define the convolution product of a function $f \in L ^ { 1 } ( \mathbb { R } ^ { N } )$ with a function $g \in L ^ { p } ( \mathbb { R } ^ { N } )$

• **Theorem 4.15 (Young).** Let $f \in L ^ { 1 } ( \mathbb { R } ^ { N } )$ and let $g \in L ^ { p } ( \mathbb { R } ^ { N } )$ with $1 \leq p \leq \infty$ Then for a.e. $x \in \mathbb { R } ^ { N }$ the function $y \mapsto f ( x - y ) g ( y )$ is integrable on $\mathbb { R } ^ { N }$ and we define

$$
\boxed { ( f \star g ) ( x ) = \int _ { \mathbb { R } ^ { N } } f ( x - y ) g ( y ) d y . }
$$

In addition $f \star g \in L ^ { p } ( \mathbb { R } ^ { N } )$ and

$$
\boxed { \| f \star g \| _ { p } \leq \| f \| _ { 1 } \; \| g \| _ { p } . }
$$

Proof. The conclusion is obvious when $p = \infty$ . We consider two cases:

(i) $p = 1$ ,

(ii) $1 < p < \infty .$

Case (i): $p = 1$ . Set $F ( x , y ) = f ( x - y ) g ( y )$

For a.e. $y \in \mathbb { R } ^ { N }$ we have

$$
\int _ { \mathbb { R } ^ { N } } | F ( x , y ) | d x = | g ( y ) | \int _ { \mathbb { R } ^ { N } } | f ( x - y ) | d x = | g ( y ) | \| f \| _ { 1 } < \infty .
$$

and, moreover,

$$
\int _ { \mathbb { R } ^ { N } } d y \int _ { \mathbb { R } ^ { N } } | F ( x , y ) | d x = \| g \| _ { 1 } \parallel f \| _ { 1 } < \infty .
$$

We deduce from Tonelli’s theorem (Theorem 4.4) that $F \in L ^ { 1 } ( \mathbb { R } ^ { N } \times \mathbb { R } ^ { N } )$ . Applying Fubini’s theorem (Theorem 4.5), we see that

$$
\int _ { \mathbb { R } ^ { N } } | F ( x , y ) | d y < \infty \; \mathrm { f o r \; a . e . } \; x \in \mathbb { R } ^ { N }
$$

and, moreover,

$$
\int _ { \mathbb { R } ^ { N } } d x \int _ { \mathbb { R } ^ { N } } | F ( x , y ) | d y = \int _ { \mathbb { R } ^ { N } } d y \int _ { \mathbb { R } ^ { N } } | F ( x , y ) | d x = \| f \| _ { 1 } \| g \| _ { 1 } .
$$

This is precisely the conclusion of Theorem 4.15 when $p = 1$

Case (ii): $1 \; < \; p \; < \; \infty$ . By Case (i) we know that for a.e. fixed $x \; \in \mathbb { R } ^ { N }$ the function $y \mapsto | f ( x - y ) |   | g ( y ) | ^ { p }$ is integrable on $\mathbb { R } ^ { N }$ , that is,

$$
| f ( x - y ) | ^ { 1 / p } | g ( y ) | \in L _ { y } ^ { p } ( \mathbb { R } ^ { N } ) .
$$

Since $| f ( x , y ) | ^ { 1 / p ^ { \prime } } \in L _ { y } ^ { p ^ { \prime } } ( \mathbb { R } ^ { N } )$ , we deduce from Hölder’s inequality that

4.4 Convolution and regularization

$$
| f ( x - y ) | | g ( y ) | = | f ( x - y ) | ^ { 1 / p ^ { \prime } } | f ( x - y ) | ^ { 1 / p } | g ( y ) | \in L _ { y } ^ { 1 } ( \mathbb { R } ^ { N } )
$$

and

$$
\int _ { \mathbb { R } ^ { N } } | f ( x - y ) | | g ( y ) | d y \leq \| f \| _ { 1 } ^ { 1 / p ^ { \prime } } \left( \int _ { \mathbb { R } ^ { N } } | f ( x - y ) | | g ( y ) | ^ { p } d y \right) ^ { 1 / p } ,
$$

that is,

$$
| ( f \star g ) ( x ) | ^ { p } \leq \left\| f \right\| _ { 1 } ^ { p / p ^ { \prime } } ( | f | \star | g | ^ { p } ) ( x ) .
$$

We conclude, by Case (i), that $f \star g \in L ^ { p } ( \mathbb { R } ^ { N } )$ and

$$
{ \big \| } f \star g { \big \| } _ { p } ^ { p } \leq { \big \| } f { \big \| } _ { 1 } ^ { p / p ^ { \prime } } { \| } f { \| } _ { 1 } { \big \| } g { \big \| } _ { p } ^ { p } ,
$$

that is,

$$
\| f \star g \| _ { p } \leq \| f \| _ { 1 } \| g \| _ { p } .
$$

**Notation.** Given a function f on $\mathbb { R } ^ { N }$ we set $\check{f}\left(x\right)=f(-x)$

**Proposition 4.16.** Let $f \in L ^ { 1 } ( \mathbb { R } ^ { N } ) ,   g \in L ^ { p } ( \mathbb { R } ^ { N } )$ and $h \in L ^ { p ^ { \prime } } ( \mathbb { R } ^ { N } )$ . Then we have

$$
\int _ { \mathbb { R } ^ { N } } ( f \star g ) h = \int _ { \mathbb { R } ^ { N } } g ( \check { f } \star h ) .
$$

Proof. The function $F ( x , y ) = f ( x - y ) g ( y ) h ( x )$ belongs to $L ^ { 1 } ( \mathbb { R } ^ { N } \times \mathbb { R } ^ { N } )$ since

$$
\int | h ( x ) | d x \int | f ( x - y ) | | g ( y ) | d y < \infty
$$

by Theorem 4.15 and Hölder’s inequality. Therefore we have

$$
\begin{align*}\int (f \star g)(x)h(x)dx &= \int dx \int F(x,y)dy = \int dy \int F(x,y)dx \\&= \int g(y)(\check{f} \star h)(y)dy.\end{align*}
$$

**Support and convolution.** The notion of support of a function $f$ is standard: supp f is the complement of the biggest open set on which f vanishes; in other words supp f is the closure of the set $\{ x ;   f ( x ) \neq 0 \}$ . This notion is not adequate when dealing with equivalence classes, such as the space $L ^ { p }$ . We need a definition which is intrinsic, that is, supp $f _ { 1 }$ and supp $f _ { 2 }$ should be the same (or differ by a null set) if $f _ { 1 } = f _ { 2 }   \mathrm { a . e }$ The reader will easily admit that the usual notion does not make sense for $f = \chi _ { \mathbb { Q } }$ on $\mathbb { R }$ In the following proposition we introduce the appropriate notion.

**Proposition 4.17 (and definition of the support).** Let $f : \mathbb { R } ^ { N } \to \mathbb { R }$ be any function. Consider the family $( \omega _ { i } ) _ { i \in I }$ of all open sets on $\mathbb { R } ^ { N }$ such that for each $i \in I ,   f = 0$ a.e. on $\omega _ { i }$ . Set $\omega = \textstyle \bigcup _ { i \in I } \omega _ { i }$

Then $f = 0 \; a . e . \; o n \; \omega$

By definition, supp f is the complement of ω in $\mathbb { R } ^ { N }$

Remark 9.

(a) Assume $f _ { 1 } = f _ { 2 } \: \mathrm { a . e }$ . on $\mathbb { R } ^ { N }$ ; clearly we have supp $f _ { 1 } = \operatorname { s u p p } f _ { 2 }$ . Hence we may talk about supp f for a function $f   \in   L ^ { p }$ —without saying what representative we pick in the equivalence class.

(b) If f is a continuous function on $\mathbb { R } ^ { N }$ it is easy to check that the new definition of supp $f$ coincides with the usual definition.

Proof of Proposition 4.17. Since the set I need not be countable it is not clear that $f = 0 \; \mathrm { a . e }$ . on ω. However we may recover the countable case as follows. There is a countable family $( O _ { n } )$ of open sets in $\mathbb { R } ^ { N }$ such that every open set on $\mathbb { R } ^ { N }$ is the union of some $O _ { n } { } ^ { \prime } \mathrm { s }$ . Write $\omega_{i}=\bigcup_{n \in A_{i}} O_{n}$ and $\omega = \textstyle \bigcup _ { n \in B } O _ { n }$ where $\textstyle B = \bigcup _ { i \in I } A _ { i }$ Since $f = 0 \; \mathrm { a . e }$ . on every set $O _ { n }$ with $\dot { n } \in B$ , we conclude that $f = 0 \; \mathrm { a . e . } \; \mathrm { o n } \; \omega$

• **Proposition 4.18.** Let $f \in L ^ { 1 } ( \mathbb { R } ^ { N } )$ and $g \in L ^ { p } ( \mathbb { R } ^ { N } )$ with $1 \leq p \leq \infty$ . Then

$$
\boxed { \mathrm { s u p p } ( f \star g ) \subset \overline { { \mathrm { s u p p } f + \mathrm { s u p p } g } } . }
$$

Proof. Fix $x   \in   \mathbb { R } ^ { N }$ such that the function $y \mapsto f ( x - y ) g ( y )$ is integrable (see Theorem 4.15). We have

$$
(f \star g)(x) = \int f(x - y)g(y)dy = \int_{(x - \operatorname{supp} f) \cap \operatorname{supp} g} f(x - y)g(y)dy.
$$

If $x \notin$ supp $f + \operatorname { s u p p } g$ , then $( x - \operatorname { s u p p } f ) \cap$ supp $g = \emptyset$ and so $( f   \star   g ) ( x ) = 0$ . Thus

$$
( f \star g ) ( x ) = 0 \quad \mathrm { a . e . ~ o n ~ } ( \mathrm { s u p p } \quad f + \mathrm { s u p p } \quad g ) ^ { c } .
$$

In particular,

$$
( f \star g ) ( x ) = 0 \quad { \mathrm { a . e . ~ o n ~ I n t } } [ ( { \mathrm { s u p p ~ } } f + { \mathrm { s u p p ~ } } g ) ^ { c } ]
$$

and therefore

$$
\operatorname { s u p p } ( f \star g ) \subset { \overline { { \operatorname { s u p p } f + \operatorname { s u p p } g } } } .
$$

• Remark 10. If both f and g have compact support, then $f \star g$ also has compact support. However, $f \star g$ need not have compact support if only one of them has compact support.

**Definition.** Let $\Omega   \subset   \mathbb { R } ^ { N }$ be open and let $1 \; \leq \; p \; \leq \; \infty$ . We say that a function $f : \Omega \to$ R belongs to $L _ { \mathrm { l o c } } ^ { p } ( \Omega ) \; \mathrm { i f } \; f \chi _ { K } \in L ^ { p } ( \Omega )$ for every compact set K contained in .

Note that if $f \in L _ { \mathrm { l o c } } ^ { p } ( \Omega )$ , then $f \in L _ { \mathrm { l o c } } ^ { 1 } ( \Omega )$

**Proposition 4.19.** Let $f \; \in \; C _ { c } ( \mathbb { R } ^ { N } )$ and $g \; \in \; L _ { \mathrm { l o c } } ^ { 1 } ( \mathbb { R } ^ { N } )$ . Then $( f \star g ) ( x )$ is well defined for **every** $x \in \mathbb { R } ^ { N }$ , and, moreover, $\stackrel { \cdots } { ( f \star g ) \in C ( \mathbb { R } ^ { N } ) }$

$P r o o f .$ Note that for every $x \in \mathbb { R } ^ { N }$ the function $y \mapsto f ( x - y ) g ( y )$ is integrable on $\mathbb { R } ^ { N }$ and therefore $( f \star g ) ( x )$ is defined for every $x \in \mathbb { R } ^ { N }$

Let $x _ { n } \to x$ and let K be a fixed compact set in $\mathbb { R } ^ { N }$ such that $( x _ { n } - \operatorname { s u p p } f ) \subset K$ $\forall n$ . Therefore, we have $f ( x _ { n } - y ) = 0   \forall n ,   \forall y \notin K$ . We deduce from the uniform continuity of f that

$$
| f ( x _ { n } - y ) - f ( x - y ) | \leq \varepsilon _ { n } \chi _ { K } ( y ) \quad \forall n , \quad \forall y \in \mathbb { R } ^ { N }
$$

with $\varepsilon _ { n } \to 0$ . We conclude that

$$
| ( f \star g ) ( x _ { n } ) - ( f \star g ) ( x ) | \leq \varepsilon _ { n } \int _ { K } | g ( y ) | d y \longrightarrow 0 .
$$

**Notation.** Let $\Omega \subset \mathbb { R } ^ { N }$ be an open set.

$C ( \Omega )$ is the space of continuous functions on $\Omega$ .

$C ^ { k } ( \Omega )$ is the space of functions k times continuously differentiable on $\Omega \: ( k \geq 1$ is an integer).

$$
C ^ { \infty } ( \Omega ) = \cap _ { k } C ^ { k } ( \Omega ) .
$$

$C _ { c } ( \Omega )$ is the space of continuous functions on  with compact support in , i.e., which vanish outside some compact set $K \subset \Omega$

$$
C _ { c } ^ { k } ( \Omega ) = C ^ { k } ( \Omega ) \cap C _ { c } ( \Omega ) .
$$

$$
C _ { c } ^ { \infty } ( \Omega ) = C ^ { \infty } ( \Omega ) \cap C _ { c } ( \Omega ) ,
$$

(some authors write D() or $C _ { 0 } ^ { \infty } ( \Omega )$ instead of $C _ { c } ^ { \infty } ( \Omega ) )$ .

If $f \in C ^ { 1 } ( \Omega )$ , its gradient is defined by

$$
\nabla f = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_N} \right).
$$

If $f \in C ^ { k } ( \Omega )$ and $\boldsymbol { \alpha } = ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { N } )$ is a multi-index of length $| \alpha | = \alpha _ { 1 } + \alpha _ { 2 } +$ $\cdots + \alpha _ { N }$ , less than k, we write

$$
D ^ { \alpha } f = { \frac { \partial ^ { \alpha _ { 1 } } } { \partial x _ { 1 } ^ { \alpha _ { 1 } } } } { \frac { \partial ^ { \alpha _ { 2 } } } { \partial x _ { 2 } ^ { \alpha _ { 2 } } } } \cdots { \frac { \partial ^ { \alpha _ { N } } } { \partial x _ { N } ^ { \alpha _ { N } } } } f .
$$

• **Proposition 4.20.** Let $f \in C _ { c } ^ { k } ( \mathbb { R } ^ { N } ) ( k \geq 1 )$ and let $g \in L _ { \mathrm { l o c } } ^ { 1 } ( \mathbb { R } ^ { N } )$ . Then $f \star g \in$ $C ^ { k } ( \mathbb { R } ^ { \hat { N } } )$ and

$$
\boxed { D ^ { \alpha } ( f \star g ) = ( D ^ { \alpha } f ) \star g \quad \forall \alpha \; w i t h \; | \alpha | \leq k . }
$$

In particular, if $f \in C _ { c } ^ { \infty } ( \mathbb { R } ^ { N } )$ and $g \in L _ { \mathrm { l o c } } ^ { 1 } ( \mathbb { R } ^ { N } )$ , then $f \star g \in C ^ { \infty } ( \mathbb { R } ^ { N } )$

Proof. By induction it suffices to consider the case $k = 1$ . Given $x \in \mathbb { R } ^ { N }$ we claim that $f \star g$ is differentiable at x and that

$$
\nabla ( f \star g ) ( x ) = ( \nabla f ) \star g ( x ) .
$$

Let $h \in \mathbb { R } ^ { N }$ with $| h | < 1$ . We have, for all $y \in \mathbb { R } ^ { N }$

$$
\begin{align*}\left| f(x + h - y) - f(x - y) - h \cdot \nabla f(x - y) \right| & \\= \left| \int_{0}^{1} [h \cdot \nabla f(x + sh - y) - h \cdot \nabla f(x - y)] ds \right| & \leq |h| \varepsilon(|h|).\end{align*}
$$

with $\varepsilon ( | h | ) \to 0$ as $| h | \to 0$ (since $\nabla f$ is uniformly continuous on $\mathbb { R } ^ { N } )$

Let K be a fixed compact set in $\mathbb { R } ^ { N }$ large enough that $x + B ( 0 , 1 ) - \operatorname { s u p p } f \subset K$ We have

$$
f(x+h-y)-f(x-y)-h\cdot\nabla f(x-y)=0 \quad \forall y\notin K, \quad \forall h\in B(0,1)
$$

and therefore

$$
| f ( x + h - y ) - f ( x - y ) - h \cdot \nabla f ( x - y ) | \leq | h | \varepsilon ( | h | ) \chi _ { K } ( y ) \; \forall y \in \mathbb { R } ^ { N } , \; \forall h \in B ( 0 , 1 ) .
$$

We conclude that for $h \in B ( 0 , 1 )$ ,

$$
| ( f \star g ) ( x + h ) - ( f \star g ) ( x ) - h \cdot ( \nabla f \star g ) ( x ) | \leq | h | \varepsilon ( | h | ) \int _ { K } | g ( y ) | d y .
$$

It follows that $f \star g$ is differentiable at x and $\nabla ( f \star g ) ( x ) = ( \nabla f ) \star g ( x )$

## Mollifiers

**Definition.** A sequence of mollifiers $( \rho _ { n } ) _ { n \geq 1 }$ is any sequence of functions on $\mathbb { R } ^ { N }$ such that

$$
\rho _ { n } \in C _ { c } ^ { \infty } ( \mathbb { R } ^ { N } ) , \quad \operatorname { \mathrm { s u p p } } \rho _ { n } \subset \overline { { B ( 0 , 1 / n ) } } , \quad \int \rho _ { n } = 1 ,   \rho _ { n } \geq 0   \mathrm { o n }   \mathbb { R } ^ { N } .
$$

In what follows we shall systematically use the notation $( \rho _ { n } )$ to denote a sequence of mollifiers.

It is easy to generate a sequenc<u>e of m</u>ollifiers starting with a single function $\rho   \in   C _ { c } ^ { \infty } ( \mathbb { R } ^ { N } )$ such that supp $\rho   \subset   \overline { { B ( 0 , 1 ) } } ,   \rho   \geq   0$ on $\mathbb { R } ^ { \check { N } }$ , and $\rho$ does not vanish identically—for example the function

$$
\rho ( x ) = \begin{cases} { e ^ { 1 / ( | x | ^ { 2 } - 1 ) } \quad } & { \mathrm { i f } \; | x | < 1 , } \\ { 0 \quad } & { \mathrm { i f } \; | x | > 1 . } \end{cases}
$$

We obtain a sequence of mollifiers by letting $\rho _ { n } ( x ) = C   n ^ { N } \rho ( n x )$ with $\begin{array} { r } { C = 1 / \int \rho } \end{array}$

**Proposition 4.21.** Assume $f \in C ( \mathbb { R } ^ { N } )$ . Then $( \rho _ { n }   \star f ) \underset { n \to \infty } { \longrightarrow } f$ uniformly on compact sets $\left[ \boldsymbol { o f } \mathbb { R } ^ { N } \right.$

$P r o o f . ^ { 4 }$ Let $K \; \subset \; \mathbb { R } ^ { N }$ be a fixed compact set. Given $\varepsilon \; > \; 0$ there exists $\delta \; > \; 0$ (depending on K and ε) such that

$$
| f ( x - y ) - f ( x ) | < \varepsilon \quad \forall x \in K , \quad \forall y \in B ( 0 , \delta ) .
$$

We have, for $x \in \mathbb { R } ^ { N }$

$$
\begin{align*}(\rho_n \star f)(x) - f(x) = & \int [f(x-y) - f(x)]\rho_n(y)dy \\= & \int_{B(0,1/n)} [f(x-y) - f(x)]\rho_n(y)dy.\end{align*}
$$

For $n > 1 / \delta$ and $x \in K$ we obtain

$$
| ( \rho _ { n } \star f ) ( x ) - f ( x ) | \leq \varepsilon \int \rho _ { n } = \varepsilon .
$$

• **Theorem 4.22.** Assume $f \in L ^ { p } ( \mathbb { R } ^ { N } )$ with $1 \leq p < \infty .$ . Then $( \rho _ { n } \star f ) \underset { n \to \infty } { \longrightarrow } f$ in $L ^ { p } ( \mathbb { R } ^ { N } )$

Proof. Given $\varepsilon > 0$ , we fix a function $f _ { 1 } \in C _ { c } ( \mathbb { R } ^ { N } )$ such that $\| f - f _ { 1 } \| _ { p } < \varepsilon$ (see Theorem 4.12). By Proposition 4.21 we know that $( \rho _ { n } \star f _ { 1 } )   \rightarrow   f _ { 1 }$ uniformly on every compact set of $\mathbb { R } ^ { \bar { N } }$ . On the other hand, we have (by Proposition 4.18) that

$$
\mathrm{supp}(\rho_{n} \star f_{1}) \subset \overline{B(0, 1 / n)}+\mathrm{supp} f_{1} \subset \overline{B(0, 1)}+\mathrm{supp} f_{1},
$$

which is a fixed compact set. It follows that

$$
\| ( \rho _ { n } \star f _ { 1 } ) - f _ { 1 } \| _ { p } \underset { n \to \infty } { \longrightarrow } 0 .
$$

Finally, we write

$$
( \rho _ { n } \star f ) - f = [ \rho _ { n } \star ( f - f _ { 1 } ) ] + [ ( \rho _ { n } \star f _ { 1 } ) - f _ { 1 } ] + [ f _ { 1 } - f ]
$$

and thus

$$
\| ( \rho _ { n } \star f ) - f \| _ { p } \leq 2 \| f - f _ { 1 } \| _ { p } + \| ( \rho _ { n } \star f _ { 1 } ) - f _ { 1 } \| _ { p }
$$

(by Theorem 4.15).

We conclude that

$$
\limsup_{n \to \infty} \| (\rho_n \star f) - f \|_p \leq 2\varepsilon \quad \forall \varepsilon > 0
$$

and therefore li $\begin{array} { r } { \operatorname* { m } _ { n \to \infty } \lVert ( \rho _ { n } \star f ) - f \rVert _ { p } = 0 . } \end{array}$

• **Corollary 4.23.** Let $\Omega \subset \mathbb { R } ^ { N }$ be an open set. Then $C _ { c } ^ { \infty } ( \Omega )$ is dense in $L ^ { p } ( \Omega )$ for any $1 \leq p < \infty$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4 The technique of regularization by convolution was originally introduced by Leray and Friedrichs.</span></small>

Proof. Given $f \in L ^ { p } ( \Omega )$ we set

$$
\bar { f } ( x ) =  \begin{cases} { f ( x ) \quad } & { \mathrm { i f } \: x \in \Omega , } \\ { 0 \quad } & { \mathrm { i f } \: x \in \mathbb { R } ^ { N } \backslash \Omega , } \end{cases}
$$

so that $\bar { f } \in L ^ { p } ( \mathbb { R } ^ { N } )$

Let $( K _ { n } )$ be a sequence of compact sets in $\mathbb { R } ^ { N }$ such that

$$
\bigcup_{n = 1}^{\infty} K_{n} = \Omega \quad  and   dist (K_{n}, \Omega^{c}) \geq 2/n \quad \forall n.
$$

[We may choose, for example, $K _ { n } = \{ x \in \mathbb { R } ^ { N } ;   | x | \leq n$ and dist $( x , \Omega ^ { c } ) \geq 2 / n \} . ]$

Set $g _ { n } = \chi _ { K _ { n } } \bar { f }$ and $f _ { n } = \rho _ { n } \star g _ { n }$ , so that

$$
{ \mathrm { s u p p } } \; f _ { n } \subset { \overline { { B ( 0 , 1 / n ) } } } + K _ { n } \subset \Omega .
$$

It follows that $f _ { n } \in C _ { c } ^ { \infty } ( \Omega )$ . On the other hand, we have

$$
\begin{align*}\left\| f_n - f \right\|_{L^p(\Omega)} &= \left\| f_n - \bar{f} \right\|_{L^p(\mathbb{R}^N)} \\&\leq \left\| (\rho_n \star g_n) - (\rho_n \star \bar{f}) \right\|_{L^p(\mathbb{R}^N)} + \left\| (\rho_n \star \bar{f}) - \bar{f} \right\|_{L^p(\mathbb{R}^N)} \\&\leq \left\| g_n - \bar{f} \right\|_{L^p(\mathbb{R}^N)} + \| (\rho_n \star \bar{f}) - \bar{f} \|_{L^p(\mathbb{R}^N)}.\end{align*}
$$

Finally, we note that $\left\| g _ { n } - { \bar { f } } \right\| _ { L ^ { p } ( \mathbb { R } ^ { N } ) } \to 0$ by dominated convergence and $\| \rho _ { n } \star$ $\left\| \bar{f} ) - \bar{f} \right\|_{L^p(\mathbb{R}^N)} \rightarrow 0$ by Theorem 4.22. We conclude that $\| f _ { n } - f \| _ { L ^ { p } ( \Omega ) } \to 0$

**Corollary 4.24.** Let $\Omega \subset \mathbb { R } ^ { N }$ be an open set and let $u \in L _ { \mathrm { l o c } } ^ { 1 } ( \Omega )$ be such that

$$
\int u f = 0 \quad \forall f \in C _ { c } ^ { \infty } ( \Omega ) .
$$

Then $u = 0$ a.e. on $\Omega$

Proof. Let $g \in L ^ { \infty } ( \mathbb { R } ^ { N } )$ be a function such that supp g is a compact set contained in . Set $g _ { n } = \rho _ { n } \star g$ , so that $g _ { n } \in C _ { c } ^ { \infty } ( \Omega )$ provided n is large enough. Therefore we have

$$
\int u \: g _ { n } = 0 \quad \forall n .\tag{19}
$$

Since $g _ { n } \rightarrow g$ in $L ^ { 1 } ( \mathbb { R } ^ { N } )$ (by Theorem 4.22) there is a subsequence—still denoted by $g _ { n }$ —such that $g _ { n } \to g$ a.e. on $\mathbb { R } ^ { N }$ (see Theorem 4.9). Moreover, we have $\| g _ { n } \| _ { L ^ { \infty } ( \mathbb { R } ^ { N } ) } \leq \| g \| _ { L ^ { \infty } ( \mathbb { R } ^ { N } ) }$ . Passing to the limit in (19) (by dominated convergence), we obtain

$$
\int u g = 0 .\tag{20}
$$

Let K be a compact set contained in . We choose as function g the function

$$
g = \begin{cases} \mathrm{sign}   u & \quad  on   K, \\ 0 & \quad  on   \mathbb{R}^N \backslash K. \end{cases}
$$

We deduce from (20) that $\begin{array} { r } { \int _ { K } | u | = 0 } \end{array}$ and thus $u = 0$ a.e. on K. Since this holds for any compact $K \subset \Omega$ , we conclude that $u = 0$ a.e. on .

## 4.5 Criterion for Strong Compactness in $L ^ { p }$

It is important to be able to decide whether a family of functions in $L ^ { p } ( \Omega )$ has compact closure in $L ^ { p } ( \Omega )$ (for the strong topology). We recall that the Ascoli–Arzelà theorem answers the same question in $C ( K )$ , the space of continuous functions over a compact metric space K with values in R.

• **Theorem 4.25 (Ascoli–Arzelà).** Let K be a compact metric space and let H be a bounded subset of $C ( K )$ . Assume that H is uniformly equicontinuous, that is,

(21) $\forall \varepsilon > 0 \; \exists \delta > 0$ such that $d ( x _ { 1 } , x _ { 2 } ) < \delta \Rightarrow | f ( x _ { 1 } ) - f ( x _ { 2 } ) | < \varepsilon \quad \forall f \in \mathcal { H } .$

Then the closure of H in $C ( K )$ is compact.

For the proof of the Ascoli–Arzelà theorem, see, e.g., W. Rudin [1], [2], A. Knapp [1], J. Dixmier [1], A. Friedman [3], G. Choquet [1], K. Yosida [1], H. L. Royden [1], J. R. Munkres [1], G. B. Folland [2], etc.

**Notation (shift of function).** We set $( \tau _ { h } f ) ( x ) = f ( x + h ) , x \in \mathbb { R } ^ { N } , h \in \mathbb { R } ^ { N }$

The following theorem and its corollary are ${ } ^ { \leftarrow } L ^ { p }$ -versions” of the Ascoli–Arzelà theorem.

• **Theorem 4.26 (Kolmogorov–M. Riesz–Fréchet).** Let F be a bounded set in $L ^ { p } ( \mathbb { R } ^ { N } )$ with $1 \leq p < \infty .$ . Assume $t h a t ^ { 5 }$

$$
\operatorname* { l i m } _ { \| h \| \to 0 } \lVert \tau _ { h } f - f \rVert _ { p } = 0 \quad \mathit { u n i f o r m l y ~ i n ~ } f \in \mathcal { F } ,\tag{22}
$$

$$
\forall \varepsilon > 0   \exists \delta > 0
$$

$$
\| \tau _ { h } f - f \| _ { p } < \varepsilon   \forall f \in \mathcal { F } ,   \forall h \in \mathbb { R } ^ { N }
$$

$$
| h | < \delta
$$

Then the closure of $\mathcal { F } _ { | \Omega | }$ in $L ^ { p } ( \Omega )$ is compact for any measurable set $\Omega \subset \mathbb { R } ^ { N }$ with finite measure.

[Here $\mathcal { F } _ { | \Omega }$ denotes the restrictions to  of the functions in $\mathcal { F } . ]$

The proof consists of four steps:

Step 1: We claim that

$$
\| ( \rho _ { n } \star f ) - f \| _ { L ^ { p } ( \mathbb { R } ^ { N } ) } \leq \varepsilon \quad \forall f \in \mathcal { F } , \quad \forall n > 1 / \delta .\tag{23}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">5 Assumption (22) should be compared with (21). It is an “integral” equicontinuity assumption.</span></small>

Indeed, we have

$$
\begin{align*}|(\rho_n \star f)(x) - f(x)| &\leq \int |f(x-y) - f(x)|\rho_n(y)dy \\&\leq \left[\int |f(x-y) - f(x)|^p\rho_n(y)dy\right]^{1/p}.\end{align*}
$$

by Hölder’s inequality.

Thus we obtain

$$
\begin{align*}\int |(\rho_n \star f)(x) - f(x)|^p dx &\leq \int \int |f(x-y) - f(x)|^p \rho_n(y) dx   dy \\&= \int_{B(0,1/n)} \rho_n(y) dy \int |f(x-y) - f(x)|^p dx \leq \varepsilon^p,\end{align*}
$$

provided $1 / n < \delta$

Step 2: We claim that

$$
\left\| \rho _ { n } \star f \right\| _ { L ^ { \infty } ( \mathbb { R } ^ { N } ) } \leq C _ { n } \left\| f \right\| _ { L ^ { p } ( \mathbb { R } ^ { N } ) } \quad \forall f \in \mathcal { F } .\tag{24}
$$

and

$$
\begin{align*}\left| (\rho_n \star f)(x_1) - (\rho_n \star f)(x_2) \right| \leq C_n \|f\|_p |x_1 - x_2| \\\forall f \in \mathcal{F}, \quad \forall x_1, x_2 \in \mathbb{R}^N,\end{align*}\tag{25}
$$

where $C _ { n }$ depends only on n.

Inequality (24) follows from Hölder’s inequality with $C _ { n } = \| \rho _ { n } \| _ { p ^ { \prime } }$ . On the other hand, we have $\nabla ( \rho _ { n } \star f ) = ( \nabla \rho _ { n } ) \star f$ and therefore

$$
\begin{array} { r } { \| \nabla ( \rho _ { n } \star f ) \| _ { L ^ { \infty } ( \mathbb { R } ^ { N } ) } \leq \| \nabla \rho _ { n } \| _ { L ^ { p ^ { \prime } } ( \mathbb { R } ^ { N } ) } \| f \| _ { L ^ { p } ( \mathbb { R } ^ { N } ) } . } \end{array}
$$

Thus we obtain (25) with $C _ { n } = \| \nabla \rho _ { n } \| _ { L ^ { p ^ { \prime } } ( \mathbb { R } ^ { N } ) }$

Step 3: Given $\varepsilon > 0$ and $\Omega \subset \mathbb { R } ^ { N }$ of finite measure, there is a bounded measurable subset ω of  such that

$$
\| f \| _ { L ^ { p } ( \Omega \setminus \omega ) } < \varepsilon \quad \forall f \in \mathcal { F } .\tag{26}
$$

Indeed, we write

$$
\begin{array} { r } { \big \| f \big \| _ { L ^ { p } ( \Omega \setminus \omega ) } \leq \big \| f - ( \rho _ { n } \star f ) \big \| _ { L ^ { p } ( \mathbb { R } ^ { N } ) } + \big \| \rho _ { n } \star f \big \| _ { L ^ { p } ( \Omega \setminus \omega ) } . } \end{array}
$$

In view of (24) it suffices to choose ω such that $| \Omega \backslash \omega |$ is small enough.

Step 4: Conclusion. Since $L ^ { p } ( \Omega )$ is complete, it suffices (see, e.g., A. Knapp [1] or J. R. Munkres [1], Section 7.3) to show that $\mathcal { F } _ { | \Omega | }$ is totally bounded, i.e., given any $\varepsilon > 0$ there is a finite covering of $\mathcal { F } _ { | \Omega }$ by balls of radius ε. Given $\varepsilon > 0$ we fix a bounded measurable set ω such that (26) holds. Also we fix $n > 1 / \delta$ . The family $\mathcal { H } = ( \rho _ { n } \star \mathcal { F } ) _ { | \bar { \omega } | }$ satisfies all the assumptions of the Ascoli–Arzelà theorem (by Step 2). Therefore H has compact closure in $C ( \bar { \omega } )$ ; consequently H also has compact closure in $L ^ { p } ( \omega )$ . Hence we may cover $\mathcal { H }$ by a finite number of balls of radius ε in $L ^ { p } ( \omega )$ , say,

$$
\mathcal { H } \subset \bigcup _ { i } B ( g _ { i } , \varepsilon ) \; \mathrm { w i t h } \; g _ { i } \in L ^ { p } ( \omega ) .
$$

Consider the functions $\bar { g } _ { i } : \Omega \to \mathbb { R }$ defined by

$$
\bar { g } _ { i } =  \begin{cases} { g _ { i } \quad } & { \mathrm { o n } \; \omega , } \\ { 0 \quad } & { \mathrm { o n } \; \Omega \backslash \omega , } \end{cases}
$$

and the balls $B ( \bar { g } _ { i } , 3 \varepsilon )$ in $L ^ { p } ( \Omega )$

We claim that they cover $\mathcal { F } _ { | \Omega | }$ . Indeed, given $f \in \mathcal { F }$ there is some i such that

$$
\left\| \left( \rho _ { n } \star f \right) - g _ { i } \right\| _ { L ^ { p } ( \omega ) } < \varepsilon .
$$

Since

$$
\left\| f - \bar{g}_i \right\|_{L^p(\Omega)}^p = \int_{\Omega \backslash \omega} |f|^p + \int_{\omega} |f - g_i|^p
$$

we have, by (26),

$$
\begin{align*}\left\| f - \bar{g}_i \right\|_{L^p(\Omega)} & \leq \varepsilon + \left\| f - g_i \right\|_{L^p(\omega)} \\& \leq \varepsilon + \left\| f - (\rho_n \star f) \right\|_{L^p(\mathbb{R}^N)} + \left\| (\rho_n \star f) - g_i \right\|_{L^p(\omega)} < 3\varepsilon.\end{align*}
$$

We conclude that $\mathcal { F } _ { | \Omega | }$ has compact closure in $L ^ { p } ( \Omega )$

Remark 11. When trying to establish that a family $\mathcal { F }$ in $L ^ { p } ( \Omega )$ has compact closure in $L ^ { p } ( \Omega )$ , with  bounded, it is usually convenient to extend the functions to all of $\mathbb { R } ^ { N }$ , then apply Theorem 4.26 and consider the restrictions to $\Omega$

Remark 12. Under the assumptions of Theorem 4.26 we cannot conclude in general that $\mathcal { F }$ itself has compact closure in $L ^ { p } ( \mathbb { R } ^ { N } )$ (construct an example, or see Exercise 4.33). An additional assumption is required; we describe it next:

**Corollary 4.27.** Let $\mathcal { F }$ be a bounded set in $L ^ { p } ( \mathbb { R } ^ { N } )$ with $1 \leq p < \infty$ . Assume (22) and also

$$
\begin{cases}\forall \varepsilon > 0 \quad \exists \Omega \subset \mathbb{R}^N, \quad bounded, \quad m e a s u r a b l e \quad s u c h \quad t h a t, \\\| f \|_{L^p(\mathbb{R}^n \setminus \Omega)} < \varepsilon \quad \forall f \in \mathcal{F}.\end{cases}\tag{27}
$$

Then $\mathcal { F }$ has compact closure in $L ^ { p } ( \mathbb { R } ^ { N } )$

Proof. Given $\varepsilon   > 0$ we fix $\Omega \subset \mathbb { R } ^ { N }$ bounded measurable such that (27) holds. By Theorem 4.26 we know that $\mathcal { F } _ { | \Omega }$ has compact closure in $L ^ { p } ( \Omega )$ . Hence we may cover $\mathcal { F } _ { | \Omega }$ with a finite number of balls of radius ε in $L ^ { p } ( \Omega )$ , say

$$
\mathcal { F } _ { | \Omega } \subset \bigcup _ { i } B ( g _ { i } , \varepsilon ) \quad \mathrm { w i t h } \; g _ { i } \in L ^ { p } ( \Omega ) .
$$

Set

$$
\bar { g } _ { i } ( x ) = \begin{cases} { g _ { i } ( x ) \quad } & { \mathrm { i n } \; \Omega , } \\ { 0 \quad } & { \mathrm { o n } \; \mathbb { R } ^ { N } \backslash \Omega . } \end{cases}
$$

It is clear that $\mathcal { F }$ is covered by the balls $B ( \bar { g } _ { i } , 2 \varepsilon )$ in $L ^ { p } ( \mathbb { R } ^ { N } )$

Remark 13. The converse of Corollary 4.27 is also true (see Exercise 4.34). Therefore we have a complete characterization of compact sets in $L ^ { p } ( \mathbb { R } ^ { N } )$ ).

We conclude with a useful application of Theorem 4.26:

**Corollary 4.28.** Let G be a fixed function in $L ^ { 1 } ( \mathbb { R } ^ { N } )$ and let

$$
\mathcal { F } = G \star \mathcal { B } ,
$$

where B is a bounded set in $L ^ { p } ( \mathbb { R } ^ { N } )$ with $1   \leq   p   <   \infty$ . Then $\mathcal { F } _ { | \Omega | }$ has compact closure in $L ^ { p } ( \Omega )$ for any measurable set  with finite measure.

Proof. Clearly $\mathcal { F }$ is bounded in $L ^ { p } ( \mathbb { R } ^ { N } )$ . On the other hand, if we write $f = G \star u$ with $u \in \mathcal { B }$ we have

$$
\| \tau _ { h } f - f \| _ { p } = \| ( \tau _ { h } G - G ) \star u \| _ { p } \leq C \| \tau _ { h } G - G \| _ { 1 } ,
$$

and we conclude with the help of the following lemma:

**Lemma 4.3.** Let $G \in L ^ { q } ( \mathbb { R } ^ { N } )$ with $1 \leq q < \infty$

Then

$$
\operatorname* { l i m } _ { h \to 0 } \lVert \tau _ { h } G - G \rVert _ { q } = 0 .
$$

Proof. Given $\varepsilon > 0 .$ , there exists (by Theorem 4.12) a function $G _ { 1 } \in C _ { c } ( \mathbb { R } ^ { N } )$ such that $\| G - G _ { 1 } \| _ { q } < \varepsilon$

We write

$$
\begin{align*}\|\tau_h G - G\|_q &\leq \|\tau_h G - \tau_h G_1\|_q + \|\tau_h G_1 - G_1\|_q + \|G_1 - G\|_q \\&\leq 2\varepsilon + \|\tau_h G_1 - G_1\|_q.\end{align*}
$$

Since lim $\scriptstyle \cdot h \to 0 \| \tau _ {   h } G _ { 1 } - G _ { 1 } \| _ { q } = 0$ we see that

$$
\limsup_{h \to 0} \| \tau_h G - G \|_q \leq 2 \varepsilon \quad \forall \varepsilon > 0.
$$

## Comments on Chapter 4

## 1. Egorov’s theorem.

Some basic results of integration theory have been recalled in Section 4.1. One useful result that has not been mentioned is the following.

\- **Theorem 4.29 (Egorov).** Assume that $\Omega$ is a measure space with finite measure. $L e t \left( f _ { n } \right)$ be a sequence of measurable functions on  such that

$$
f _ { n } ( x ) \rightarrow \; f ( x ) \; a . e . \; o n \; \Omega \; ( w i t h \; | f ( x ) | < \infty \; a . e . ) .
$$

Then $\forall \varepsilon   >   0 \quad \exists A   \subset   \Omega$ measurable such that $| \Omega \backslash A |   <   \varepsilon$ and $f _ { n } \rightarrow f$ uniformly on A.

For a proof, see Exercise 4.14, P. Halmos [1], G. B. Folland [2], E. Hewitt– K. Stromberg [1], R. Wheeden–A. Zygmund [1], K. Yosida [1], A. Friedman [3], etc.

## 2. Weakly compact sets in $L ^ { 1 } .$

Since $L ^ { 1 }$ is not reflexive, bounded sets of $L ^ { 1 }$ do not play an important role with respect to the weak topology $\sigma ( L ^ { 1 } , L ^ { \infty } )$ . The following result provides a useful characterization of weakly compact sets of $L ^ { 1 }$

\- **Theorem 4.30 (Dunford–Pettis).** Let $\mathcal { F }$ be a bounded set in $L ^ { 1 } ( \Omega )$ . Then $\mathcal { F }$ has compact closure in the weak topology $\sigma ( L ^ { 1 } , L ^ { \infty } )$ if and only $i f \mathcal { F }$ is equi-integrable, that is,

$$
\begin{cases}\forall \varepsilon > 0 \quad \exists \delta > 0 \quad \mathit{such} \; that \\\displaystyle \int_{A} |f| < \varepsilon \quad \forall A \subset \Omega, \mathit{measurable} \; with \; |A| < \delta, \quad \forall f \in \mathcal{F}.\end{cases}\tag{a}
$$

and

$$
\begin{cases}\forall \varepsilon > 0 \quad \exists \omega \subset \Omega, \quad m e a s u r a b l e \quad w i t h \quad | \omega | < \infty \quad s u c h \quad t h a t \\\displaystyle \int _ { \Omega \setminus \omega } | f | < \varepsilon \quad \forall f \in \mathcal { F } .\end{cases}\tag{b}
$$

For a proof and discussion of Theorem 4.30 see Problem 23 or N. Dunford– J. T. Schwartz [1], B. Beauzamy [1], J. Diestel [2], I. Fonseca–G. Leoni [1], and also J. Neveu [1], C. Dellacherie–P. A. Meyer [1] for the probabilistic aspects; see also Exercise 4.36.

## 3. Radon measures.

As we have just pointed out, bounded sets of $L ^ { 1 }$ enjoy no compactness properties. To overcome this lack of compactness it is sometimes very useful to embed $\bar { L } ^ { 1 }$ into a large space: the space of Radon measures.

Assume, for example, that $\Omega$ is a bounded open set of $\mathbb { R } ^ { N }$ with the Lebesgue measure. Consider the space $E   =   C ( \overline { { \Omega } } )$ with its norm $\| u \|   =   \operatorname { s u p } _ { x \in \overline { { \Omega } } } | u ( x ) |$ . Its dual space, denoted by $\mathcal { M } ( \overline { { \Omega } } )$ , is called the space of Radon measures on $\overline { { \Omega } }$ . The weak- topology on $\mathcal { M } ( \overline { { \Omega } } )$ is sometimes called the “vague” topology.

We shall identify $L ^ { 1 } ( \Omega )$ with a subspace of $\mathcal { M } ( \overline { { \Omega } } )$ . For this purpose we introduce the mapping $L ^ { 1 } ( \Omega ) \to \mathcal { M } ( \overline { { \Omega } } )$ defined as follows. Given $f \in L ^ { 1 } ( \Omega )$ , the mapping $\begin{array} { r } { u \in C ( \overline { { \Omega } } ) \mapsto \int _ { \Omega } } \end{array}$ fu dx is a continuous linear functional on $C ( \overline { { \Omega } } )$ , which we denote $T f$ , so that

$$
\langle T f , u \rangle _ { E ^ { \star } , E } = \int _ { \Omega } f \; u \; d x \quad \forall u \in E .
$$

Clearly T is linear, and, moreover, T is an isometry, since

$$
\| T f \| _ { \mathcal { M } ( \overline { \Omega } ) } = \sup _ { \substack { u \in E \\ \| u \| \leq 1 } } \int _ { \Omega } f u = \| f \| _ { 1 } \quad ( \mathrm { s e e } \; \mathrm { E x e r c i s e } \; 4 . 2 6 ) .
$$

Using $T$ we may identify $L ^ { 1 } ( \Omega )$ with a subspace of $\mathcal { M } ( \overline { { \Omega } } )$ . Since $\mathcal { M } ( \overline { { \Omega } } )$ is the dual space of the separable space $C ( \overline { { \Omega } } )$ , it has some compactness properties in the weak- topology. In particular, if $( f _ { n } )$ is a bounded sequence in $L ^ { 1 } ( \Omega )$ , there exist a subsequence $( f _ { n _ { k } } )$ and a Radon measure $\mu$ such that $f _ { n _ { k } } \stackrel { \star } { \rightharpoonup } \mu$ in the weak- topology $\sigma ( E ^ { \star } , E )$ , that is,

$$
\int _ { \Omega } f _ { n _ { k } } u \to \langle \mu , u \rangle \quad \forall u \in C ( \overline { { \Omega } } ) .
$$

For example, a sequence in $L ^ { 1 }$ can converge to a Dirac measure with respect to the weak- topology. Some futher properties of Radon measures are discussed in Problem 24.

The terminology “measure” is justified by the following result, which connects the above definition with the standard notion of measures in the set-theoretic sense:

**Theorem 4.31 (Riesz representation theorem).** Let μ be a Radon measure on $\overline { { \Omega } } .$ Then there is a unique signed Borel measure ν on $\overline { { \Omega } }$ (that is, a measure defined on Borel sets $o f \overline { { \Omega } } )$ such that

$$
\langle \mu , u \rangle = \int _ { \overline { { \Omega } } } u d \nu \quad \forall u \in C ( \overline { { \Omega } } ) .
$$

It is often convenient to replace the space $E = C ( \overline { { \Omega } } )$ by the subspace

$$
E _ { 0 } = \{ f \in C ( \overline { { \Omega } } ) ;   f = 0   \mathrm { o n \; t h e \; b o u n d a r y \; o f \; } \overline { { \Omega } } \} .
$$

The dual of $E _ { 0 }$ is denoted by $\mathcal { M } ( \Omega )$ (as opposed to $\mathcal { M } ( \overline { { \Omega } } ) )$ . The Riesz representation theorem remains valid with the additional condition that |ν|(boundary of $\overline { { \Omega } } ) = 0$

On this vast and classical subject, see, e.g., H. L. Royden [1], W. Rudin [2], G. B. Folland [2], A. Knapp [1], P. Malliavin [1], P. Halmos [1], I. Fonseca– G. Leoni [1].

## 4. The Bochner integral of vector-valued functions.

Let  be a measure space and let E be a Banach space. The space $L ^ { p } ( \Omega ; E )$ consists of all functions $f$ defined on $\Omega$ with values into E that are measurable in some appropriate sense and such that $\begin{array} { r } { \int _ { \Omega } \| f ( x ) \| ^ { p } d \mu < \infty } \end{array}$ (with the usual modification when $p = \infty )$ . Most of the properties described in Sections 4.2 and 4.3 still hold under some additional assumptions on E. For example, if E is reflexive and $1 < p <$ $\infty ,$ , then $L ^ { p } ( \Omega ; E )$ is reflexive and its dual space is $L ^ { p ^ { \prime } } ( \Omega ; E ^ { \star } )$ . For more details, see K. Yosida [1], D. L. Cohn [1], E. Hille [1], B. Beauzamy [1], L. Schwartz [3]. The space $L ^ { p } ( \Omega ; E )$ is very useful in the study of evolution equations when  is an interval in R (see Chapter 10).

## 5. Interpolation theory.

The most striking result, which began interpolation theory, is the following.

**Theorem 4.32 (Schur, M. Riesz, Thorin).** Assume that  is a measure space with $| \Omega | < \infty ,$ and that $T : L ^ { 1 } ( \Omega ) \to L ^ { 1 } ( \Omega )$ is a bounded linear operator with norm

$$
M _ { 1 } = \| T \| _ { \mathcal { L } ( L ^ { 1 } , L ^ { 1 } ) } .
$$

Assume, in addition, that $T : L ^ { \infty } ( \Omega ) \to L ^ { \infty } ( \Omega )$ is a bounded linear operator with norm

$$
M _ { \infty } = \| T \| _ { \mathcal { L } ( L ^ { \infty } , L ^ { \infty } ) } .
$$

Then T is a bounded operator from $L ^ { p } ( \Omega )$ into $L ^ { p } ( \Omega )$ for all $1 < p < \infty ,$ and its norm $M _ { p }$ satisfies

$$
M _ { p } \leq M _ { 1 } ^ { 1 / p } M _ { \infty } ^ { 1 / p ^ { \prime } } .
$$

Interpolation theory was originally discovered by I. Schur, M. Riesz, G. O. Thorin, J. Marcinkiewicz, and A. Zygmund. Decisive contributions have been made by a number of authors including J.-L. Lions, J. Peetre, A. P. Calderon, E. Stein, and E. Gagliardo. It has become a useful tool in harmonic analysis (see, e.g., E. Stein– G. Weiss [1], E. Stein [1], C. Sadosky [1]) and in partial differential equations (see, e.g., J.-L. Lions–E. Magenes [1]). On these questions see also G. B. Folland [2], N. Dunford–J. T. Schwartz [1] (Volume 1 p. 520), J. Bergh–J. Löfström [1], M. Reed–B. Simon [1], (Volume 2, p. 27) and Problem 22.

## 6. Young’s inequality.

The following is an extension of Theorem 4.15.

**Theorem 4.33 (Young).** Assume $f \in L ^ { p } ( \mathbb { R } ^ { N } )$ and $g \in L ^ { q } ( \mathbb { R } ^ { N } )$ with $1 \leq p \leq \infty ,$ $\begin{array} { r } { 1 \leq q \leq \infty \; a n d \; \frac { 1 } { r } = \frac { \bar { 1 } } { p } + \frac { 1 } { q } - 1 \geq 0 . } \end{array}$

Then $f \star g \in L ^ { r } ( \mathbb { R } ^ { N } )$ and $\| f \star g \| _ { r } \leq \| f \| _ { p } \| g \| _ { q }$

For a proof see, e.g., Exercise 4.30.

**7.** The notion of convolution—extended to distributions (see L. Schwartz [1] or A. Knapp [2])—plays a fundamental role in the theory of partial differential equations. For example, the equation $P ( D ) u = f \operatorname { i n } \mathbb { R } ^ { N }$ , where $P ( D )$ is any differential operator with constant coefficients, has a solution of the form $u = E \star f$ , where E is the fundamental solution of $P ( D )$ (theorem of Malgrange–Ehrenpreis; see also Comment 2b in Chapter 1). In particular, the equation $\tilde{\Delta u} = f \ln \mathbb{R}^3$ has a solution of the form $u = E \star f$ , where $E ( x ) = - ( 4 \pi | x | ) ^ { - 1 }$

## Exercises for Chapter 4

Except where otherwise stated,  denotes a σ-finite measure space.

<u>4.1</u> Let $\alpha > 0$ and $\beta > 0$ . Set

$$
f ( x ) = \left\{ 1 + | x | ^ { \alpha } \right\} ^ { - 1 } \left\{ 1 + | \log | x | | ^ { \beta } \right\} ^ { - 1 } , x \in \mathbb { R } ^ { N } .
$$

Under what conditions does f belong to $L ^ { p } ( \mathbb { R } ^ { N } ) ?$

<u>4.2</u> Assume $| \Omega | < \infty$ and let $1 \leq p \leq q \leq \infty$ . Prove that $L ^ { q } ( \Omega ) \subset L ^ { p } ( \Omega )$ with continuous injection. More precisely, show that

$$
\| f \| _ { p } \leq | \Omega | ^ { \frac { 1 } { p } - \frac { 1 } { q } } \| f \| _ { q } \quad \forall f \in L ^ { q } ( \Omega ) .
$$

[**Hint:** Use Hölder’s inequality.]

<u>4.3</u>

1. Let $f , g \in L ^ { p } ( \Omega )$ with $1 \leq p \leq \infty$ . Prove that

$$
h ( x ) = \operatorname* { m a x } \left\{ f ( x ) , g ( x ) \right\} \in L ^ { p } ( \Omega ) .
$$

2. Let $( f _ { n } )$ and $( g _ { n } )$ be two sequences in $L ^ { p } ( \Omega )$ with $1 \; \leq \; p \; \leq \; \infty$ such that $f _ { n } \rightarrow f$ in $L ^ { p } ( \Omega )$ and $g _ { n } \to g$ in $L ^ { p } ( \Omega )$ . Set $h_{n} = \max\{f_{n}, g_{n}\}$ and prove that $h _ { n } \to h$ in $L ^ { p } ( \Omega )$

3. $\operatorname { L e t } \left( f _ { n } \right)$ be a sequence in $L ^ { p } ( \Omega )$ with $1 \leq p < \infty$ and let $( g _ { n } )$ be a bounded sequence in $L ^ { \infty } ( \Omega )$ . Assume $f _ { n } \rightarrow f$ in $L ^ { p } ( \Omega )$ and $g _ { n } \rightarrow g$ a.e. Prove that $f _ { n } g _ { n } \rightarrow f g$ in $L ^ { p } ( \Omega )$

<u>4.4</u>

1. Let $f _ { 1 } , f _ { 2 } , \ldots , f _ { k }$ be k functions such that $f _ { i } \in L ^ { p _ { i } } ( \Omega )$ ∀i with $1 \leq p _ { i } \leq \infty$ and $\textstyle \sum _ { i = 1 } ^ { k }   { \frac { 1 } { p _ { i } } } \leq 1$ Set

$$
f ( x ) = \prod _ { i = 1 } ^ { k } f _ { i } ( x ) .
$$

Prove that $f \in L ^ { p } ( \Omega )$ with $\begin{array} { r } { \frac { 1 } { p } = \sum _ { i = 1 } ^ { k } \frac { 1 } { p _ { i } } } \end{array}$ and that

$$
\| f \| _ { p } \leq \prod _ { i = 1 } ^ { k } \lVert f _ { i } \rVert _ { p _ { i } } .
$$

[**Hint:** Start with $k = 2$ and proceed by induction.]

2. Deduce that if $f \in L ^ { p } ( \Omega ) \cap L ^ { q } ( \Omega )$ with $1 \leq p \leq$ ∞ and $1 \leq q \leq \infty$ , then $f \in L ^ { r } ( \Omega )$ for every r between p and q. More precisely, write

## 4.5 Exercises for Chapter 4

$$
{ \frac { 1 } { r } } = { \frac { \alpha } { p } } + { \frac { 1 - \alpha } { q } } \quad { \mathrm { w i t h } }   \alpha \in [ 0 , 1 ]
$$

and prove that

$$
{ \big \| } f { \big \| } _ { r } \leq { \big \| } f { \big \| } _ { p } ^ { \alpha } { \big \| } f { \big \| } _ { q } ^ { 1 - \alpha } .
$$

<u>4.5</u> Let $1 \leq p < \infty$ and $1 \leq q \leq \infty$

1. Prove that $L ^ { 1 } ( \Omega ) \cap L ^ { \infty } ( \Omega )$ is a dense subset of $L ^ { p } ( \Omega )$

2. Prove that the set

$$
\left\{ f \in L ^ { p } ( \Omega ) \cap L ^ { q } ( \Omega ) ; \| f \| _ { q } \leq 1 \right\}
$$

is closed in $L ^ { p } ( \Omega )$

3. Let $( f _ { n } )$ be a sequence in $L ^ { p } ( \Omega ) \cap L ^ { q } ( \Omega )$ and let $f \in L ^ { p } ( \Omega )$ . Assume that

$$
f _ { n } \to f \mathrm { i n } L ^ { p } ( \Omega ) \mathrm { a n d } \| f _ { n } \| _ { q } \leq C .
$$

Prove that $f \in L ^ { r } ( \Omega )$ and that $f _ { n } \rightarrow f$ in $L ^ { r } ( \Omega )$ for every r between p and $q , r \neq q$

<u>4.6</u> Assume $| \Omega | < \infty$

1. Let $f \in L ^ { \infty } ( \Omega )$ . Prove that lim $\scriptstyle 1 _ { p \to \infty }   \| f \| _ { p } = \| f \| _ { \infty }$

2. Let $f \in \cap _ { 1 \leq p < \infty } L ^ { p } ( \Omega )$ and assume that there is a constant C such that

$$
\| f \| _ { p } \leq C \quad \forall \; 1 \leq p < \infty .
$$

Prove that $f \in L ^ { \infty } ( \Omega )$ .

3. Construct an example of a function $f \in \cap _ { 1 \leq p < \infty } L ^ { p } ( \Omega )$ such that $f \notin L ^ { \infty } ( \Omega )$ with $\Omega = ( 0 , 1 )$

$\boxed { 4 . 7 }$ Let $1 \leq q \leq p \leq \infty$ . Let $a ( x )$ be a measurable function on $\Omega .$ Assume that $a u \in L ^ { q } ( \Omega )$ for every function $u \in L ^ { p } ( \Omega )$

Prove that $a \in L ^ { r } ( \Omega )$ with

$$
r = { \left\{ \begin{aligned} & { { } { \frac { p q } { p - q } } \quad } & { { \mathrm { i f ~ } } p < \infty , } \\ & { { } q \quad } & { { \mathrm { i f ~ } } p = \infty . } \end{aligned} \right. }
$$

[**Hint:** Use the closed graph theorem.]

<u>4.8</u> Let $X \subset L ^ { 1 } ( \Omega )$ be a closed vector space in $L ^ { 1 } ( \Omega )$ . Assume that

$$
X \subset \bigcup _ { 1 < q \leq \infty } L ^ { q } ( \Omega ) .
$$

1. Prove that there exists some $p > 1$ such that $X \subset L ^ { p } ( \Omega )$

[**Hint:** For every integer $n \geq 1$ consider the set

$$
X_{n} = \left\{ f \in X \cap L^{1 + (1/n)}(\Omega) \; ; \left\| f \right\|_{1 + (1/n)} \leq n \right\}. ]
$$

2. Prove that there is a constant C such that

$$
\| f \| _ { p } \leq C \| f \| _ { 1 } \quad \forall f \in X .
$$

<u>4.9</u> Jensen’s inequality.

Assume $| \Omega | < \infty . \operatorname { L e t } j : \mathbb { R } \to ( - \infty , + \infty ]$ be a convex l.s.c. function, $j \not \equiv + \infty$ Let $f \in L ^ { 1 } ( \Omega )$ be such that $f(x) \in D(j)$ a.e. and $j ( f ) \in L ^ { 1 } ( \Omega )$ . Prove that

$$
j \left( \frac{1}{|\Omega|} \int_{\Omega} f \right) \leq \frac{1}{|\Omega|} \int_{\Omega} j(f).
$$

<u>4.10</u> Convex integrands.

Assume $| \Omega | < \infty$ . Let $1 \leq p < \infty$ and let $j : \mathbb { R } \rightarrow \mathbb { R }$ be a convex and continuous function. Consider the function $J : L ^ { p } ( \Omega ) \rightarrow ( - \infty , + \infty ]$ defined by

$$
J ( u ) = \left\{ \begin{aligned} & \int _ { \Omega } j ( u ( x ) ) d x \quad & \text { if } j ( u ) \in L ^ { 1 } ( \Omega ) , \\ & + \infty \quad & \text { if } j ( u ) \notin L ^ { 1 } ( \Omega ) . \end{aligned} \right.
$$

1. Prove that J is convex.

2. Prove that J is l.s.c.

[**Hint:** Start with the case $j \geq 0$ and use Fatou’s lemma.]

3. Prove that the conjugate function $J ^ { \star } : L ^ { p ^ { \prime } } ( \Omega ) \to ( - \infty , + \infty ]$ is given by

$$
J ^ { \star } ( f ) =  \begin{cases} { \int _ { \Omega } j ^ { \star } ( f ( x ) ) d x \quad } & { \mathrm { i f } j ^ { \star } ( f ) \in L ^ { 1 } ( \Omega ) , } \\ { + \infty \quad } & { \mathrm { i f } j ^ { \star } ( f ) \notin L ^ { 1 } ( \Omega ) . } \end{cases}
$$

[**Hint:** When $1 < p < \infty$ consider $\begin{array} { r } { J _ { n } ( u ) = J ( u )   +   \frac { 1 } { n } \int | u | ^ { p } } \end{array}$ and determine $J _ { n } ^ { \star } . ]$ 4. Let ∂j (resp. ∂J) denote the subdifferential of $j ( \mathrm { \bf r e s p . } J )$ (see Problem 2). Let $u \in L ^ { p } ( \Omega )$ and let $f \in L ^ { p ^ { \prime } } ( \Omega )$ ; prove that

$$
f \in \partial J ( u ) \Longleftrightarrow f ( x ) \in \partial j ( u ( x ) ) \quad \mathrm { a . e . ~ o n } \; \Omega .
$$

<u>4.11</u> The spaces $L ^ { \alpha } ( \Omega )$ with $0 < \alpha < 1$

Let $0 < \alpha < 1$ . Set

$$
L ^ { \alpha } ( \Omega ) = \Big \{ u : \Omega \to \mathbb { R } ; \quad u \mathrm { ~ i s ~ m e a s u r a b l e ~ a n d ~ } | u | ^ { \alpha } \in L ^ { 1 } ( \Omega ) \Big \}
$$