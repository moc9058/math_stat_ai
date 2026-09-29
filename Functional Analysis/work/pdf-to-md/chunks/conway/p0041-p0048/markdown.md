# Operators on Hilbert Space

A large area of current research interest is centered around the theory of operators on Hilbert space. Several other chapters in this book will be devoted to this topic.

There is a marked contrast here between Hilbert spaces and the Banach spaces that are studied in the next chapter. Essentially all of the information about the geometry of Hilbert space is contained in the preceding chapter. The geometry of Banach space lies in darkness and has attracted the attention of many talented research mathematicians. However, the theory of linear operators (linear transformations) on a Banach space has very few general results, whereas Hilbert space operators have an elegant and well-developed general theory. Indeed, the reason for this dichotomy is related to the opposite status of the geometric considerations. Questions concerning operators on Hilbert space don't necessitate or imply any geometric difficulties.

In addition to the fundamentals of operators, this chapter will also present an interesting application to differential equations in Section 6.

## §1. Elementary Properties and Examples

The proof of the next proposition is similar to that of Proposition I.3.1 and is left to the reader.

1.1. Proposition. Let $\mathcal { H }$ and $\mathcal { H }$ be Hilbert spaces and A: $\mathcal { H } \rightarrow \mathcal { H }$ a linear transformation. The following statements are equivalent.

(a) A is continuous.

(b) A is continuous at 0.

(c) A is continuous at some point.

(d) There is a constant $c   >   0$ such that $\| A \boldsymbol{h} \| \leqslant c \| \boldsymbol{h} \|$ for all h in $\mathcal { H } .$

As in (I.3.3), if

$$
\| A \| = \sup \{ \| A h \| : h \in \mathcal{H},   \| h \| \leqslant 1 \},
$$

then

$$
\begin{aligned}\| A \| &= \sup \{ \| A h \| : \| h \| = 1 \} \\&= \sup \{ \| A h \| / \| h \| : h \neq 0 \} \\&= \inf \{ c > 0 : \| A h \| \leqslant c \| h \| , h   in   \mathcal{H} \}.\end{aligned}
$$

Also, $\| A h \| \leqslant \| A \| \| h \|. \| A \|$ is called the norm of A and a linear transformation with finite norm is called bounded. Let $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ be the set of bounded linear transformations from $\mathcal { H }$ into $\mathcal { H }$ .For $\mathcal { H } = \mathcal { H }$ $\mathcal { B } ( \mathcal { H } , \mathcal { H } ) \equiv \mathcal { B } ( \mathcal { H } )$ . Note that $\mathcal { B } ( \mathcal { H } , \mathbb { F } ) = \mathrm { a l l }$ the bounded linear functionals on $\mathcal { H }$

1.2. Proposition. (a) If A and $B \in \mathcal{B}(\mathcal{H}, \mathcal{H}),$ then $A + B \in \mathcal{B}(\mathcal{H}, \mathcal{H})$ and $\| A + B \| \leqslant \| A \| + \| B \|$

(b) $\scriptstyle \int   \alpha \in \mathbb { F }$ and $A \in \mathcal { B } ( \mathcal { H } , \mathcal { H } ) ,$ , then $\alpha A \in \mathcal{B}(\mathcal{H}, \mathcal{H})$ and $\left\| \alpha \boldsymbol{A} \right\| = \left| \alpha \right| \left\| \boldsymbol{A} \right\|$

(c) $If A \in \mathcal{B}(\mathcal{H}, \mathcal{H})$ and $B \in \mathcal { B } ( \mathcal { H } , \mathcal { L } ) ,$ then $BA \in \mathcal{B}(\mathcal{H}, \mathcal{L})$ and $\left\| \boldsymbol{B} \boldsymbol{A} \right\| \leqslant \left\| \boldsymbol{B} \right\| \left\| \boldsymbol{A} \right\|$

ProoF. Only (c) will be proved; the rest of the proof is left to the reader. If $k \in \mathcal { H }$ , then $\| B k \| \leqslant \| B \| \| k \|$ Hence, if $h \in \mathcal { H }$ $k = A h \in \mathcal{H}$ and so $\left\| \boldsymbol{B} \boldsymbol{A} \boldsymbol{h} \right\| \leqslant \left\| \boldsymbol{B} \right\| \left\| \boldsymbol{A} \boldsymbol{h} \right\| \leqslant \left\| \boldsymbol{B} \right\| \left\| \boldsymbol{A} \right\| \left\| \boldsymbol{h} \right\|$

By virtue of preceding proposition, $d ( A , B ) = \| A - B \|$ defines a metric on $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ . So it makes sense to consider $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ as a metric space. This will not be examined closely until later in the book, but later in this chapter the idea of the convergence of a sequence of operators will be used.

1.3. Example. If dim $\mathcal { H } = n < \infty$ and dim $\mathcal { H } = m < \infty$ , let $\{ e _ { 1 } , \ldots , e _ { n } \}$ be an orthonormal basis for $\mathcal { H }$ and let $\{ \varepsilon _ { 1 } , \ldots , \varepsilon _ { m } \}$ be an orthonormal basis for $\mathcal { H }$ . It can be shown that every linear transformation from $\mathcal { H }$ into $\mathcal { H }$ is bounded (Exercise 3). If $1 \leqslant j \leqslant n, 1 \leqslant i \leqslant m,$ let $a _ { i j } = \langle A e _ { j } , \varepsilon _ { i } \rangle$ . Then the $m \times n$ matrix $( \pmb { \alpha } _ { i j } )$ represents A and every such matrix represents an element of $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$

1.4. Example. Let $l ^ { 2 } \equiv l ^ { 2 } ( \mathbb { N } )$ and let $e _ { 1 } , e _ { 2 } , \ldots$ .be its usual basis. If $A   \in   \mathcal { B } ( l ^ { 2 } ) ,$ form $\alpha _ { i j } = \langle A e _ { j } , e _ { i } \rangle$ . The infinite matrix $( \pmb { \alpha } _ { i j } )$ represents A as finite matrices represent operators on finite dimensional spaces. However, this representation has limited value unless the matrix has a special form. One difficulty is that it is unknown how to find the norm of A in terms of the entries in the matrix. In fact, if $4 < n < \infty$ , there is no known formula for the norm of an $n \times n$ matrix in terms of its entries. (This restriction on the values of n is due to our inability to solve polynomial equations of degree greater than $4 . )$ See

Exercise 11. A sufficient condition for the boundedness of an infinite matrix that is useful is known. (See Exercise 9.) Another sufficient condition for a matrix to be bounded can be found on page 61 of Maddox [1980].

1.5. Theorem. Let $( X , \Omega , \mu )$ be a σ-finite measure space and put $\mathcal { H } = L ^ { 2 } ( X , \Omega , \mu ) \equiv L ^ { 2 } ( \mu )$ If $\phi   \in   L ^ { \infty } ( \mu ) .$ , define $M _ { \phi } { : } L ^ { 2 } ( \mu )   \to   L ^ { 2 } ( \mu ) b y M _ { \phi } f = \phi f$ Then $M _ { \phi } { \in } { \mathcal { B } } ( L ^ { 2 } ( \mu ) )$ and $\|   M _ { \phi } \| = \|   \phi   \| _ { \infty }$

PROOF. Here $\| \phi \| _ { \infty }$ is the µ-essential supremum norm. That is,

$$
\begin{align*}\| \phi \|_{\infty} & \equiv \inf \left\{ \sup \left\{ | \phi(x) | : x \neq N \right\} : N \in \Omega, \mu(N) = 0 \right\} \\& = \inf \left\{ c > 0 : \mu( \left\{ x \in X : | \phi(x) | > c \right\} ) = 0 \right\}.\end{align*}
$$

Thus $\| \phi \| _ { \infty }$ is the infimum of all $c   >   0$ such that $| \phi ( x ) | \leqslant c$ a.e. [μ] and, moreover, $| \phi ( x ) | \leqslant \| \phi \| _ { \infty } { \mathrm { ~ a . e . ~ } } [ \mu ]$ Thus we can, and do, assume that $\phi$ is a bounded measurable function and $| \phi ( x ) | \leqslant \| \phi \| _ { \infty }$ for all x. So if $f   \in   L ^ { 2 } ( \mu )$ , then $\int | \phi f | ^ { 2 } d \mu \leqslant \| \phi \| _ { \infty } ^ { 2 } \int | f | ^ { 2 } d \mu.$ That is, $M _ { \phi } { \in } { \mathcal { B } } ( L ^ { 2 } ( \mu ) )$ and $\| M _ { \phi } \| \leqslant \| \phi \| _ { \infty }$ If $\varepsilon   >   0 .$ , the σ-finiteness of the measure space implies that there is a set ∆ in $\Omega , 0 < \mu ( \Delta ) < \infty$ , such that $| \phi ( x ) | \geqslant \|   \phi   \| _ { \infty } - \varepsilon$ on $\Delta . ( \mathrm { W h y ? } ) \mathrm { I f } f = ( \mu ( \Delta ) ) ^ { - 1 / 2 } \chi _ { \Delta } ,$ then $f   \in   L ^ { 2 } ( \mu )$ and $\| f \| _ { 2 } = 1$ . So $\| M _ { \phi } \| ^ { 2 } \geqslant \| \phi f \| _ { 2 } ^ { 2 } = ( \mu ( \Delta ) ) ^ { - 1 } \int _ { \Delta } | \phi | ^ { 2 } d \mu \geqslant$ $( \parallel   \phi   \parallel _ { \infty } - \varepsilon ) ^ { 2 }$ . Letting $\varepsilon   \to   0 ,$ we get that $\| M _ { \phi } \| \geqslant \| \phi \| _ { \infty } .$

The operator $M _ { \phi }$ is called a multiplication operator. The function $\phi$ is its symbol.

If the measure space $( X , \Omega , \mu )$ is not $\sigma \text {-f} \mathrm { n i t e }$ then the conclusion of Theorem 1.5 is not necessarily valid. Indeed, let $\Omega = \mathrm { t h e }$ Borel subsets of $[ 0 , 1 ]$ and define $\mu$ onΩ by $\mu ( \Delta ) =$ the Lebesgue measure of $\Delta$ if $0 \notin \Delta$ and $\mu ( \Delta ) = \infty$ if $0 { \in } \Delta$ This measure has an infinite atom at 0 and, therefore, is not σ-finite. Let $\phi = \chi _ { \{ 0 \} }$ Then $\phi   \in   L ^ { \infty } ( \mu )$ and $\| \phi \| _ { \infty } = 1$ . If $f   \in   L ^ { 2 } ( \mu )$ , then $\infty > \int | f | ^ { 2 } d \mu \geqslant | f ( 0 ) | ^ { 2 } \mu ( \{ 0 \} )$ . Hence every function in $L ^ { 2 } ( \mu )$ vanishes at $0 .$ Therefore $M _ { \phi } = 0$ and $\|   M _ { \phi } \| < \|   \phi   \| _ { \infty } .$

There are more general measure spaces for which (1.5) is valid—the decomposable measure spaces (see Kelley [1966]).

1.6. Theorem. Let $( X , \Omega , \mu )$ be a measure space and suppose k: $X \times X \to \mathbb { F }$ is an $\mathbf { \Omega } \times \mathbf { \Omega } .$ -measurable function for which there are constants $c _ { 1 }$ and $c _ { 2 }$ such that

$$
\begin{align*}\int_{X} |k(x,y)|   d\mu(y) \leqslant c_1 \quad  a.e.   [\mu], \\\int_{X} |k(x,y)|   d\mu(x) \leqslant c_2 \quad  a.e.   [\mu].\end{align*}
$$

If K: $L ^ { 2 } ( \mu ) \to L ^ { 2 } ( \mu )$ is defined by

$$
( K f ) ( x ) = \int k ( x , y ) f ( y ) d \mu ( y ) ,
$$

then K is a bounded linear operator and $\| K \| \leqslant ( c _ { 1 } c _ { 2 } ) ^ { 1 / 2 }$

PRooF. Actually it must be shown that $K f   \in   L ^ { 2 } ( \mu )$ , but this will follow from the argument that demonstrates the boundedness of K. If $f   \in   L ^ { 2 } ( \mu )$

$$
\begin{align*}|Kf(x)| & \leqslant \int |k(x,y)|   |f(y)|   d\mu(y) \\& = \int |k(x,y)|^{1/2} |k(x,y)|^{1/2} |f(y)|   d\mu(y) \\& \leqslant \left[ \int |k(x,y)|   d\mu(y) \right]^{1/2} \left[ \int |k(x,y)|   |f(y)|^2   d\mu(y) \right]^{1/2} \\& \leqslant c_1^{1/2} \left[ \int |k(x,y)|   |f(y)|^2   d\mu(y) \right]^{1/2}.\end{align*}
$$

Hence

$$
\begin{align*}\int |Kf(x)|^2   d\mu(x) & \leqslant c_1 \int |k(x,y)|   |f(y)|^2   d\mu(y)   d\mu(x) \\& = c_1 \int |f(y)|^2 \int |k(x,y)|   d\mu(x)   d\mu(y) \\& \leqslant c_1 c_2   \|f\|^2.\end{align*}
$$

Now this shows that the formula used to define K fis finite a.e. $[ \mu ] , K f \in L ^ { 2 } ( \mu ) ,$ and $\| K f \| ^ { 2 } \leqslant c _ { 1 } c _ { 2 } \| f \| ^ { 2 }$

The operator described above is called an integral operator and the function k is called its kernel. There are conditions on the kernel other than the one in (1.6) that will imply that K is bounded.

A particular example of an integral operator is the Volterra operator defined below.

1.7. Example. Let $k \colon [ 0 , 1 ] \times [ 0 , 1 ]   \to   \mathbb { R }$ be the characteristic function of $\{ ( x , y ) ;   y < x \}$ . The corresponding operator $V \colon L ^ { 2 } ( 0 , 1 ) \to L ^ { 2 } ( 0 , 1 )$ defined by $V f(x)=\int_{0}^{1} k(x, y) f(y) d y$ is called the Volterra operator. Note that

$$
V f ( x ) = \int _ { 0 } ^ { x } f ( y )   d y .
$$

Another example of an operator was defined in Example 1.5.3. The nonsurjective isometry defined there is called the unilateral shift. It will be studied in more detail later in this book. Note that any isometry is a bounded operator with norm 1.

EXERCISES

1. Prove Proposition 1.1

2. Prove Proposition 1.2

3. Suppose $\{ e _ { 1 } , e _ { 2 } , \ldots , \}$ is an orthonormal basis for $\mathcal { H }$ and for each n there is a vector $A e _ { n }$ in $\mathcal { H }$ such that $\textstyle \sum \| A e _ { n } \| < \infty$ . Show that A has an unique extension to a bounded operator on $\mathcal { H }$

4. Proposition 1.2 says that $d(A,B)=\left\|A-B\right\|$ is a metric on $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ Show that $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ is complete relative to this metric.

5. Show that a multiplication operator $M _ { \phi } \left( 1 . 5 \right)$ satisfies $M _ { \phi } ^ { 2 } = M _ { \phi }$ if and only if $\phi$ is a characteristic function.

6. Let $( X , \Omega , \mu )$ be a σ-finite measure space and let $k _ { 1 } , k _ { 2 }$ be two kernels satisfying the hypothesis of (1.6). Define

$$
\mathbf { k } \colon X \times X \to \mathbb { F } \quad { \mathrm { b y } } \quad k ( x , y ) = \int k _ { 1 } ( x , z ) k _ { 2 } ( z , y )   d \mu ( z ) .
$$

(a) Show that k also satisfies the hypothesis of (1.6). (b) If $K ,   K _ { 1 } ,   K _ { 2 }$ are the integral operators with kernels $k , k _ { 1 } , k _ { 2 }$ , show that $K = K _ { 1 } K _ { 2 }$ . What does this remind you of? Is more going on than an analogy?

7. If $( X , \Omega , \mu )$ is a measure space and $k { \in } L ^ { 2 } ( \mu \times \mu )$ , show that k defines a bounded integral operator.

8. Let $\{ e _ { n } \}$ be the usual basis for $l ^ { 2 }$ and let $\{ \alpha _ { n } \}$ be a sequence of scalars. Show that there is a bounded operator A on $l ^ { 2 }$ such that $A e _ { n } = \alpha _ { n } e _ { n }$ for all n if and only if $\{ \alpha _ { n } \}$ is uniformly bounded, in which case $\| A \| = \sup \left\{ | \alpha _ { n } | : n \geqslant 1 \right\}$ . This type of operator is called a diagonal operator or is said to be diagonalizable.

9. (Schur test) Let $\left\{ \alpha _ { i j } \right\} _ { i , j = 1 } ^ { \infty }$ be an infinite matrix such that $\alpha _ { i j }   \geqslant   0$ for all $i , j$ and such that there are scalars $p _ { i } > 0$ and $\beta , \gamma   >   0$ with

$$
\sum _ { i \; = \; 1 } ^ { \infty } \alpha _ { i j } p _ { i } \leqslant \beta p _ { j } ,
$$

$$
\sum _ { j = 1 } ^ { \infty } \alpha _ { i j } p _ { j } \leqslant \gamma p _ { i } .
$$

for all $i , j \geqslant 1$ . Show that there is an operator A on $l ^ { 2 } ( \mathbb { N } )$ with $\left\langle A e _ { j } , e _ { i } \right\rangle = \alpha _ { i j }$ and二 $A \parallel ^ { 2 } \leqslant \beta \gamma$

10. (Hilbert matrix) Show that $\langle A e _ { j } , e _ { i } \rangle = ( i + j + 1 ) ^ { - 1 }$ for $0 \leqslant i , j < \infty$ defines a bounded operator on $l ^ { 2 } ( \mathbb { N } \cup \{ 0 \} )$ with $\| { \pmb A } \| \leqslant \pi .$ (See also Choi [1983] and Redheffer and Volkmann [1983].)

11. If $\boldsymbol{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ put $\alpha = [ | a | ^ { 2 } + | b | ^ { 2 } + | c | ^ { 2 } + | d | ^ { 2 } ] ^ { 1 / 2 }$ and show that $\| A \| =$

$\frac{1}{2}(\alpha^{2}+\sqrt{\alpha^{4}-4\delta^{2}})$ , where $\delta ^ { 2 } = \operatorname* { d e t } A ^ { * } A .$

12. (Direct sum of operators) Let $\{ \mathcal { H } _ { i } \}$ be a collection of Hilbert spaces and let $\mathcal { H } = \oplus _ { i } \mathcal { H } _ { i } .$ Suppose $A _ { i } \in \mathcal { B } ( \mathcal { H } _ { i } )$ for all i. Show that there is a bounded operator A on $\mathcal { H }$ such that $A | \mathcal { H } _ { i } = \overline { { A } } _ { i }$ for all i if and only if $\operatorname { s u p } _ { i } \| A _ { i } \| < \infty$ . In this case, $\| A \| = \sup_{i} \| A_i \|$ . The operator A is called the direct sum of the operators $\{ A _ { i } \}$ and is denoted by $\pmb { A } = \oplus _ { i } \pmb { A } _ { i }$

13. (Bari [1951]) Call a sequence of vectors $\{ f _ { n } \}$ in a Hilbert space $\mathcal { H }$ a Bessel sequence $\mathrm { i f } \sum | \langle f , f _ { n } \rangle | ^ { 2 } < \infty$ for every f in $\mathcal { H }$ .Show that a sequence $\{ f _ { n } \}$ of vectors in $\mathcal { H }$ is a Bessel sequence if and only if the infinite matrix $( \langle f _ { m } , f _ { n } \rangle )$ defines a bounded operator on $l ^ { 2 } .$ (Also see Shapiro and Shields [1961], p. 524.)

## §2. The Adjoint of an Operator

2.1. Definition. If $\mathcal { H }$ and $\mathcal { H }$ are Hilbert spaces, a function u: $\mathcal { H } \times \mathcal { H } \rightarrow$ F is a sesquilinear form if for $h , g$ in $\mathcal { H } , k , f$ in $\mathcal { H }$ , and $\alpha , \beta$ in $\mathbb { F } .$

(a) $u ( \alpha h + \beta g , k ) = \alpha u ( h , k ) + \beta u ( g , k ) ;$

(b) $u ( h , \alpha k + \beta f ) = \bar { \alpha } u ( h , k ) + \bar { \beta } u ( h , f ) .$

The prefix “sesqui" is used because the function is linear in one variable but (for $\mathbf { F } = \mathbf { C } )$ only conjugate linear in the other. (“Sesqui" means $\text{" one-and-a-half." }$

A sesquilinear form is bounded if there is a constant M such that $| u ( h , k ) | \leqslant M \| h \| \| k \|$ for all h in $\mathcal { H }$ and k in $\mathcal { H }$ The constant M is called a bound for u.

Sesquilinear forms are used to study operators. If $A \in \mathcal{B}(\mathcal{H}, \mathcal{H})$ then $u ( h , k ) \equiv \langle A h , k \rangle$ is a bounded sesquilinear form. Also, if $B \in \mathcal{B}(\mathcal{H}, \mathcal{H})$ $u ( h , k ) \equiv \langle h , B k \rangle$ is a bounded sesquilinear form. Are there any more? Are these two forms related?

2.2. Theorem. If u: $\mathcal { H } \times \mathcal { H } \rightarrow \mathbb { F }$ is a bounded sesquilinear form with bound M, then there are unique operators A in $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ and B in $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ such that

$$
u ( h , k ) = \langle A h , k \rangle = \langle h , B k \rangle
$$

for all h in $\mathcal { H }$ and k in $\mathcal { H }$ and $\| A \| ,   \| B \| \leqslant M .$

PRooF. Only the existence of A will be shown. For each h in $\mathcal { H } ,$ define $L _ { h } ;$ $\mathcal { H }   \rightarrow   \mathbb { F }$ by $L _ { h } ( k ) = \overline { { u ( h , k ) } }$ . Then $L _ { h }$ is linear and $| L _ { h } ( k ) | \leqslant M \| h \| \| k \|$ . By the Riesz Representation Theorem there is a unique vector f in $\mathcal { H }$ such that $\langle k , f \rangle = L _ { h } ( k ) = \overline { { u ( h , k ) } }$ and $\parallel f \parallel \leqslant M \parallel h \parallel$ . Let $A h   =   f$ . It is left as an exercise to show that A is linear (use the uniqueness part of the Riesz Theorem). Also, $\langle A h , k \rangle = \langle \overline { { k , A h } } \rangle = \langle \overline { { k , f } } \rangle = u ( h , k )$

If $A_{1} \in \mathcal{B}(\mathcal{H}, \mathcal{H})$ and $u ( h , k ) = \langle A _ { 1 } h , k \rangle$ , then $\langle A h - A _ { 1 } h , k \rangle = 0$ for all $k ;$ thus $A h - A _ { 1 } h = 0$ for all h. Thus, A is unique.

2.4. Definition. If $A \in \mathcal{B}(\mathcal{H}, \mathcal{H})$ , then the unique operator B in $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ satisfying (2.3) is called the adjoint of A and is denoted by $B = A ^ { * }$

The adjoint of an operator will usually be used for operators in $\mathcal { B } ( \mathcal { H } )$ rather than $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ . There is one notable exception.

2.5. Proposition. If $U \in \mathcal { B } ( \mathcal { H } , \mathcal { H } )$ , then U is an isomorphism if and only if U is invertible and $U ^ { - 1 } = U ^ { * }$

PROOF. Exercise.

From now on we will examine and prove results for the adjoint of operators in $\mathcal { B } ( \mathcal { H } )$ . Often, as in the next proposition, there are analogous results for the adjoint of operators in $\mathcal { B } ( \mathcal { H } , \mathcal { H } )$ . This simplification is justified, however, by the cleaner statements that result. Also, the interested reader will have no trouble formulating the more general statement when it is needed.

2.6. Proposition. If $A,B \in \mathcal{B}(\mathcal{H})$ and $\alpha \in \mathbf { F } ,$ , then:

(a) $( \alpha A + B ) ^ { * } = { \bar { \alpha } } A ^ { * } + B ^ { * } .$

(b) $( A B ) ^ { * } = B ^ { * } A ^ { * } .$

(c) $A ^ { * * } \equiv ( A ^ { * } ) ^ { * } = A .$

(d) $I f A$ is invertible in $\mathcal { B } ( \mathcal { H } )$ and $A ^ { - 1 }$ is its inverse, then $A ^ { * }$ is invertible and $(A^{*})^{-1} = (A^{-1})^{*}.$

The proof of the preceding proposition is left as an exercise, but a word about part (d) might be helpful. The hypothesis that A is invertible in $\mathcal { B } ( \mathcal { H } )$ means that there is an operator $A ^ { - 1 }$ in $\mathcal { B } ( \mathcal { H } )$ such that $A A ^ { - 1 } = A ^ { - 1 } A = I$ It is a remarkable fact that if A is only assumed to be bijective, then A is invertible in $\mathcal { B } ( \mathcal { H } )$ . This is a consequence of the Open Mapping Theorem which will be proved later.

2.7. Proposition. $\mathit { I f } \; A   \in   \mathcal { B } ( \mathcal { H } ) , \; \| A \| = \| A ^ { \star } \| = \| A ^ { \star } A \| ^ { 1 / 2 } .$

PROOF. For $h \quad  in  \quad \mathcal{H}, \quad \| h \| \leqslant 1, \quad \| A h \|^2 = \langle A h, A h \rangle = \langle A^* A h, h \rangle \leqslant$ $\| A ^ { \star } A h \| \; \| h \| \leqslant \| A ^ { \star } A \| \leqslant \| A ^ { \star } \| \; \| A \|$ Hence $\| A \| ^ { 2 } \leqslant \| A ^ { * } A \| \leqslant \| A ^ { * } \| \| A \|$ Using the two ends of this string of inequalities gives $\| \boldsymbol { A } \| \leqslant \| \boldsymbol { A } ^ { * } \|$ when $\| A \|$ is cancelled. But $A = A ^ { * * }$ and so if $A ^ { * }$ is substituted for A, we get $\left\| \left. A ^ { * } \right\| \leqslant \left\| \left. A ^ { * * } \right\| = \left\| \left. A \right. \right\| \right. \right.$ . Hence $\| { \boldsymbol { A } } \| = \| { \boldsymbol { A } } ^ { \star } \|$ . Thus the string of inequalities becomes a string of equalities and the proof is complete.

2.8. Example. Let $( X , \Omega , \mu )$ be a $\sigma - \mathrm { f i n i t e }$ measure space and let $M _ { \phi }$ be the multiplication operator with symbol φ (1.5). Then $M _ { \phi } ^ { * }$ is $M _ { \bar { \phi } } ,$ the multi-plication operator with symbol $\bar { \phi } .$

If an operator on $\mathbb { F } ^ { d }$ is presented by a matrix, then its adjoint is represented by the conjuagate transpose of the matrix.

2.9. Example. If K is the integral operator with kernel k as in (1.6), then $K ^ { * }$ is the integral operator with kernel $k ^ { * } ( x , y ) \equiv \widehat { k ( y , x ) }$

2.10. Proposition. $I f S \colon l ^ { 2 } \to l ^ { 2 }$ is defined by $S(\alpha_{1},\alpha_{2},\ldots)=(0,\alpha_{1},\alpha_{2},\ldots)$ , then S is an isometry and $S ^ { * } ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots ) = ( \alpha _ { 2 } , \alpha _ { 3 } , \ldots ) .$

ProoF. It has already been mentioned that S is an isometry (I.5.3). For $( \alpha _ { n } )$ and $( \beta _ { n } )$ in $l ^ { 2 } , \left\langle S ^ { * } \left( \alpha _ { n } \right) , \left( \beta _ { n } \right) \right\rangle = \left\langle \left( \alpha _ { n } \right) , S \left( \beta _ { n } \right) \right\rangle = \left\langle \left( \alpha _ { 1 } , \alpha _ { 2 } , \ldots \right) , \left( 0 , \beta _ { 1 } , \beta _ { 2 } , \ldots \right) \right\rangle =$ $\alpha_{2}\bar{\beta}_{1} + \alpha_{3}\bar{\beta}_{2} + \cdots = \langle (\alpha_{2},\alpha_{3},\ldots),(\beta_{1},\beta_{2},\ldots) \rangle$ . Since this holds for every $( \beta _ { n } ) ,$ the result is proved. ■

The operator S in (2.10) is called the unilateral shift and the operator $S ^ { * }$ is called the backward shift

The operation of taking the adjoint of an operator is, as the reader may have seen from the examples above, analogous to taking the conjugate of a complex number. It is good to keep the analogy in mind, but do not become too religious about it.

2.11. Definition. If $A \in \mathcal { B } ( \mathcal { H } )$ , then: (a) is hermitian or self-adjoint if $A ^ { * } = A .$ (b) A is normal if $A A ^ { * } = A ^ { * } A$

In the analogy between the adjoint and the complex conjugate, hermitian operators become the analogues of real numbers and, by (2.5), unitaries are the analogues of complex numbers of modulus 1. Normal operators, as we shall see, are the true analogues of complex numbers. Notice that hermitian and unitary operators are normal.

In light of (2.8), every multiplication operator $M _ { \phi }$ is normal; $M _ { \phi }$ is hermitian if and only if $\phi$ is real-valued; $M _ { \phi }$ is unitary if and only if $| \phi | \equiv 1$ a.e. [μ]. By (2.9), an integral operator K with kernel k is hermitian if and only $\mathrm{if} k(x, y) = k(y, x) \mathrm{a.e.} [\mu \times \mu]$ . The unilateral shift is not normal (Exercise 6).

2.12. Proposition. If  is a C-Hilbert space and $A \in \mathcal { B } ( \mathcal { H } )$ , then A is hermitian if and only $if \langle A h, h \rangle \in \mathbb{R}$ for all h in $\mathcal { H }$

PROOF. If $A = A ^ { * }$ , then $\langle A h , h \rangle = \langle h , A h \rangle = \langle \widetilde { A h , h } \rangle$ hence $\langle A h , h \rangle \in \mathbb { R }$

For the converse, assume $\langle A h , h \rangle$ is real for every h in $\mathcal { H } ,$ If $\alpha \in \mathbf { C }$ and $h , g \in \mathcal { H }$ then $\langle A ( h + \alpha g ) , h + \alpha g \rangle = \langle A h , h \rangle + \bar { \alpha } \langle A h , g \rangle + \alpha \langle A g , h \rangle +$ $| \alpha | ^ { 2 } \langle A g , g \rangle \in \mathbb { R }$ . So this expression equals its complex conjugate. Using the fact that $\langle A h , h \rangle$ and $\langle A g , g \rangle \in \mathbb { R }$ yields

$$
\begin{align*}\alpha \langle A g, h \rangle + \bar{\alpha} \langle A h, g \rangle = & \bar{\alpha} \langle h, A g \rangle + \alpha \langle g, A h \rangle \\= & \bar{\alpha} \langle A^* h, g \rangle + \alpha \langle A^* g, h \rangle.\end{align*}
$$

By first taking $\alpha = 1$ and then $\alpha = i ,$ we obtain the two equations

$$
\langle A g , h \rangle + \langle A h , g \rangle = \langle A ^ { * } h , g \rangle + \langle A ^ { * } g , h \rangle ,
$$

$$
i \langle A g , h \rangle - i \langle A h , g \rangle = - i \langle A ^ { * } h , g \rangle + i \langle A ^ { * } g , h \rangle .
$$

A little arithmetic implies $\langle A g , h \rangle = \langle A ^ { * } g , h \rangle , \mathrm { s o } A = A ^ { * } .$

The preceding proposition is false if it is only assumed that $\mathcal { H }$ is an R-Hilbert space. For example, if $\boldsymbol{A} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$ on $\mathbb { R } ^ { 2 }$ , then $\langle A h , h \rangle = 0$ for