where λ is a given complex number, $q { \in } C [ a , b ]$ , and $f { \in } L ^ { 2 } [ a , b ]$ , together with the boundary conditions

## 6.2

$$
\left\{ \begin{aligned} (a) \alpha h(a) + \alpha_{1} h^{\prime}(a) &= 0 \\ (b) \beta h(b) + \beta_{1} h^{\prime}(b) &= 0 \end{aligned} \right.
$$

where $\alpha ,   \alpha _ { 1 } ,   \beta ,$ and $\beta _ { 1 }$ are real numbers and $\alpha ^{2}+\alpha _{1}^{2}>0,\beta ^{2}+\beta _{1}^{2}>0.$

Equation (6.1) together with the boundary conditions (6.2) is called a (regular) Sturm-Liouville system. Such systems arise in a number of physical problems, including the description of the motion of a vibrating string. In this section we will discuss solutions of the Sturm–Liouville system by relating the system to a certain compact self-adjoint integral operator.

Recall that an absolutely continuous function h on $[ a , b ]$ has a derivative a.e. and $h(x) = \int_{a}^{x} h^{\prime}(t)   dt + h(a)$ for all x.

Define

$$
\mathcal { D } _ { a } \equiv \{ h \in C _ { \mathbb { C } } ^ { ( 1 ) } [ a , b ] \colon h ^ { \prime } \mathrm { ~ i s ~ a b s o l u t e l y ~ c o n t i n u o u s } ,
$$

$$
h ^ { \prime \prime } \in L ^ { 2 } [ a , b ] , \mathrm { a n d } h \mathrm { s a t i s f i e s } ( 6 . 2 a ) \} .
$$

$\mathcal { D } _ { b }$ is defined similarly but each h in $\mathcal { D } _ { b }$ satisfies (6.2b) instead of (6.2a). The space $\mathcal { D } = \mathcal { D } _ { a } \cap \mathcal { D } _ { b }$

Define $L \colon { \mathcal { D } }   \to   L ^ { 2 } [ a , b ]$ by

## 6.3

$$
L h = - h ^ { \prime \prime } + q h .
$$

L is called a Sturm-Liouville operator.

Note that $\mathcal { D }$ is a linear space and L is a linear transformation. The Sturm-Liouville problem thus becomes: if $\lambda \in \mathbf { C }$ and $f   \in   L ^ { 2 } [ a , b ]$ , is there an h in $\mathcal { D }$ with $( L - \lambda ) h = f$ . Equivalently, for which λ is f in $\operatorname { r a n } ( L - \lambda ) ?$

By placing a suitable norm on , L can be made into a bounded operator. This does not help much. The best procedure is to consider $( L - \lambda ) ^ { - 1 }$ Integration is the inverse of differentiation, and it turns out that $( L - \lambda ) ^ { - 1 }$ (when we can define it) is an integral operator.

Begin by considering the case when $\lambda   =   0 .$ (Equivalently, replace q by $q - \lambda . )$ To define $L ^ { - 1 }$ (even if only on the range of $L ) ,$ we need that L is injective. Thus we make an assumption;

## 6.4

$$
\mathrm { i f } ~ h \in \mathcal { D } \quad \mathrm { a n d } \quad L h = 0 , \quad \mathrm { t h e n } \quad h = 0 .
$$

The first lemma is from ordinary differential equations and says that certain initial-value problems have nontrivial (nonzero) solutions.

6.5. Lemma. If $\alpha , \alpha _ { 1 } , \beta , \beta _ { 1 } \in \mathbb { R } , \alpha ^ { 2 } + \alpha _ { 1 } ^ { 2 } > 0 ,$ and $\beta ^ { 2 } + \beta _ { 1 } ^ { 2 } > 0 ,$ , then there are functions $h _ { a } ,   h _ { b }$ in $\mathcal { D } _ { a } , \mathcal { D } _ { b } ,$ respectively, such that $L ( h _ { a } ) = 0$ and $L ( h _ { b } ) = 0$ and $h _ { a } , h _ { b }$ are real-valued and not identically zero.

The Wronskian of $h _ { a }$ and $h _ { b }$ is the function

$$
W = \det \begin{bmatrix} h_a & h_b \\ h_a' & h_b' \end{bmatrix} = h_a h_b' - h_a' h_b.
$$

Note that $W ^ { \prime } = h _ { a } h _ { b } ^ { \prime \prime } - h _ { a } ^ { \prime \prime } h _ { b } = h _ { a } ( q h _ { b } ) - ( q h _ { a } ) h _ { b } = 0$ Hence $W ( x ) \equiv W ( a )$ for all x.

## 6.6. Lemma. Assuming (6.4), $W ( a ) \neq 0$ and so $h _ { a }$ and $h _ { b }$ are linearly independent.

PROOF. If $W ( a ) = 0 ,$ then linear algebra tells us that the column vectors in the matrix used to define $W ( a )$ are linearly dependent. Thus there is a λ in R such that $h _ { b } ( a ) = \lambda h _ { a } ( a )$ and $h_{b}^{\prime}(a)=\lambda h_{a}^{\prime}(a)$ . Thus $h _ { b } \in \mathcal { D }$ and $L ( h _ { b } )   =   0$ .By (6.4), $h _ { b }   \equiv   0 .$ , contradiction. ■

Put $c = -   W ( a )$ and define $g \colon [ a , b ] \times [ a , b ] \to \mathbb { R }$ by

6.7

$$
g ( x , y ) = \left\{ \begin{aligned} { c ^ { - 1 } h _ { a } ( x ) h _ { b } ( y ) } & { { } \quad \mathrm { i f } a \leqslant x \leqslant y \leqslant b } \\ { c ^ { - 1 } h _ { a } ( y ) h _ { b } ( x ) } & { { } \quad \mathrm { i f } a \leqslant y \leqslant x \leqslant b . } \end{aligned} \right.
$$

The function g is the Green function for $L$

6.8. Lemma. The function g defined in (6.7) is real-valued, continuous, and $g ( x , y ) = g ( y , x )$

PROOF. Exercise.

6.9. Theorem. Assume (6.4). If g is the Green function for L defined in (6.7) and G: $L ^ { 2 } [ a , b ] \to L ^ { 2 } [ a , b ]$ is the integral operator defined by

$$
( G f ) ( x ) = \int _ { a } ^ { b } g ( x , y ) f ( y ) d y ,
$$

then G is a compact self-adjoint operator, ran $G = \mathcal { D } , \; L G f = f   f o r$ all f in $L ^ { 2 } [ a , b ]$ , and $G L h = h$ for all h in $\mathcal { D }$

ProoF. That G is self-adjoint follows from the fact that g is real-valued and $g ( x , y ) = g ( y , x ) ;$ G is compact by (4.7). Fix f in $L ^ { 2 } [ a , b ]$ and put $h = G f$ . It must be shown that $h \in \mathcal { D }$

Put

$$
H _ { a } ( x ) = c ^ { - 1 } \int _ { a } ^ { x } h _ { a } ( y ) f ( y ) d y \quad \mathrm { a n d } \quad H _ { b } ( x ) = c ^ { - 1 } \int _ { x } ^ { b } h _ { b } ( y ) f ( y ) d y.
$$

Then

$$
\begin{align*}h(x) &= \int_{a}^{b} g(x,y) f(y) dy \\&= c^{-1} \int_{a}^{x} h_a(y) h_b(x) f(y) dy + c^{-1} \int_{x}^{b} h_a(x) h_b(y) f(y) dy.\end{align*}
$$

That is, $h = H _ { a } h _ { b } + h _ { a } H _ { b }$ Differentiating this equation gives $h ^ { \prime } = ( c ^ { - 1 } h _ { a } f ) h _ { b } +$ $H_{a}h_{b}^{\prime}+h_{a}^{\prime}H_{b}+h_{a}(-c^{-1}h_{b}f)=H_{a}h_{b}^{\prime}+h_{a}^{\prime}H_{b}$ a.e. Since $H _ { a } h _ { b } ^ { \prime } + h _ { a } ^ { \prime } H _ { b }$ is absolutely continuous, as part of showing that $h { \in } { \mathcal { D } }$ we want to show the following.

Claim. $h ^ { \prime } = H _ { a } h _ { b } ^ { \prime } + h _ { a } ^ { \prime } H _ { b }$ everywhere.

Put $\phi = H _ { a } h _ { b } ^ { \prime } + h _ { a } ^ { \prime } H _ { b }$ and put $\psi ( x ) = h ( a ) + \int _ { a } ^ { x } \phi ( y ) d y .$ So $\phi$ and $\psi$ are absolutely continuous, $h ( a ) = \psi ( a )$ , and $h ^ { \prime } = \psi ^ { \prime }$ a.e. Thus $h = \psi$ everywhere. But $\psi$ has a continuous derivative $\phi ,$ so h does too. That is, the claim is proved.

Differentiating $h ^ { \prime } = H _ { a } h _ { b } ^ { \prime } + h _ { a } ^ { \prime } H _ { b }$ gives that a.e., $h ^ { \prime \prime } = ( c ^ { - 1 } h _ { a } f ) h _ { b } ^ { \prime } + H _ { a } h _ { b } ^ { \prime \prime } +$ $h _ { a } ^ { \prime \prime } H _ { b } + h _ { a } ^ { \prime } ( - c ^ { - 1 } h _ { b } f ) ;$ since each of these summands belongs to $L ^ { 2 } [ a , b ]$ $\hat { h ^ { \prime \prime } } \in L ^ { 2 } [ a , b ]$

Because $H _ { a } ( a ) = 0$ and $h _ { a } \in \mathcal { D } _ { a } ,   \alpha h ( a ) + \alpha _ { 1 } h ^ { \prime } ( a ) = \alpha h _ { a } ( a ) H _ { b } ( a ) + \alpha _ { 1 } h _ { a } ^ { \prime } ( a ) H _ { b } ( a ) =$ $[ \alpha h _ { a } ( a ) + \alpha _ { 1 } h _ { a } ^ { \prime } ( a ) ] H _ { b } ( a ) = 0$ Hence $h \in \mathcal { D } _ { a }$ Similarly, $h \in \mathcal { D } _ { b }$ Thus $h \in \mathcal { D }$ Hence ran $G \subseteq { \mathcal { D } } .$

Now to show that $L G f = f$ . If $h = G f , L ( h ) = - h ^ { \prime \prime } + q h = - ( c ^ { - 1 } h _ { a } h _ { b } ^ { \prime } f +$ $H_{a}h_{b}^{\prime\prime}+h_{a}^{\prime\prime}H_{b}-c^{-1}h_{a}^{\prime}h_{b}f]+q(H_{a}h_{b}+h_{a}H_{b})=(-h_{b}^{\prime\prime}+qh_{b})H_{a}+(-h_{a}^{\prime\prime}+qh_{a})H_{b}+$ $c ^ { - 1 } ( h _ { a } ^ { \prime } h _ { b } - h _ { a } h _ { b } ^ { \prime } ) f = f$ since $L ( h _ { a } ) = L ( h _ { b } ) = 0$ and $h _ { a } ^ { \prime } h _ { b } - h _ { a } h _ { b } ^ { \prime } = W = c .$

If $h { \in } { \mathcal { D } }$ then $L h { \in } L ^ { 2 } [ a , b ]$ . So by the first part of the proof, $L G L h = L h$ Thus $0 = L ( G L h - h )$ . Since ker $L = ( 0 ) ,   h = G L h$ and so $h \in \operatorname { r a n } G .$

6.10. Corollary. Assume (6.4). $I f h \in \mathcal { D } , \lambda \in \mathfrak { C } \backslash \{ 0 \}$ , and $L h = \lambda h$ , then $G h = \lambda ^ { - 1 } h .$ $If   h \in L^2[a,b]$ and $G h = \lambda ^ { - 1 } h$ , then $h { \in } { \mathcal { D } }$ and $L h = \lambda h$

PRoOF. This is immediate from the theorem.

6.11. Lemma. Assume (6.4). If $\alpha   \in   \sigma _ { p } ( G )$ and $\alpha \neq 0 ,$ then dim ker $( G - \alpha ) = 1$

PRooF. Suppose there are linearly independent functions $h _ { 1 } , h _ { 2 }$ in ker $( G - \alpha )$ By (6.10), $h _ { 1 } , h _ { 2 }$ are solutions of the equation

$$
- h ^ { \prime \prime } + ( q - \alpha ^ { - 1 } ) h = 0 .
$$

Since this is a second-order linear differential equation, every solution of it must be a linear combination of $h _ { 1 }$ and $h _ { 2 }$ . But $h _ { 1 } ,   h _ { 2 }   \in   \mathcal { D }$ so they satisfy (6.2). But a solution can be found to this equation satisfying any initial conditions at a—and thus not satisfying (6.2). This contradiction shows that linearly independent $h _ { 1 } ,   h _ { 2 }$ in ker $( G - \alpha )$ cannot be found.

6.12. Theorem. Assume (6.4). Then there is a sequence $\{ \lambda _ { 1 } , \lambda _ { 2 } , \ldots \}$ of real numbers and a basis $\{ e _ { 1 } , e _ { 2 } , \ldots \}$ for $L ^ { 2 } [ a , b ]$ such that

(a) $0 < | \lambda _ { 1 } | < | \lambda _ { 2 } | < \cdots  { a n d } | \lambda _ { n } | \to \infty$

(b) $e _ { n } \in \mathcal { D }$ and $L e _ { n } = \lambda _ { n } e _ { n }$ for all n.

(c) $\mathrm { I } f \lambda \neq \lambda _ { n }$ for any $\lambda _ { n }$ and $f { \in } L ^ { 2 } [ a , b ]$ , then there is a unique h in $\mathcal { D }$ with $Lh - \lambda h = f$

(d) $If \lambda = \lambda_n for$ some n and $f { \in } L ^ { 2 } [ a , b ]$ , then there is an h in $\mathcal { D }$ with $Lh - \lambda h = f$ if and only $if \langle f, e_n \rangle = 0. If \langle f, e_n \rangle = 0$ , any two solutions of $L h - \lambda h = f$ differ by a multiple of $e _ { n } .$

ProoF. Parts (a) and (b) follow by Theorem 5.1, Corollary 6.10, and

Lemma 6.1. For parts (c) and (d), first note that

## 6.13

$$
L h - \lambda h = f \quad  if   and   only if  \quad h - \lambda G h = G f.
$$

This is, in fact, a straightforward consequence of Theorem $6 . 9$

(c) The case where $\lambda   =   0$ is left to the reader. If $\lambda \neq \lambda _ { n }$ for any $n , \lambda ^ { - 1 } \notin \sigma _ { p } ( G )$ Since $G = G ^ { * }$ , Corollary 4.15 implies $G - \lambda ^ { - 1 }$ is bijective. So if $f { \in } L ^ { 2 } [ { \dot { a } } , b ]$ there is a unique h in $\dot { L } ^ { 2 } [ a , b ]$ with $G f = ( \lambda ^ { - 1 } - G ) h$ . Thus $h \in \mathcal { D }$ and (6.13) implies $L ( h / \lambda ) - \lambda ( h / \lambda ) = f$

(d) Suppose $\lambda = \lambda _ { n }$ for some n. If $L h - \lambda _ { n } h = f$ , then $h - \lambda_{n}Gh = Gf$ Hence $\langle G f , e _ { n } \rangle = \langle h , e _ { n } \rangle - \lambda _ { n } \langle G h , e _ { n } \rangle = \langle h , e _ { n } \rangle - \lambda _ { n } \langle h , G e _ { n } \rangle = \langle h , e _ { n } \rangle -$ $\lambda_{n}\lambda_{n}^{-1}\left\langle h,e_{n}\right\rangle=0.\ \mathrm{So}\ 0=\left\langle Gf,e_{n}\right\rangle=\left\langle f,Ge_{n}\right\rangle=\lambda_{n}\left\langle f,e_{n}\right\rangle$ . Hence $f \bot e _ { n }$

Since ① $e _ { n } = \ker ( G - \lambda _ { n } ^ { - 1 } ) , \left[ e _ { n } \right] ^ { \perp } \equiv \mathcal { N }$ reduces G. Let $G _ { 1 } = G | \mathcal { N }$ . So $G _ { 1 }$ is a compact self-adjoint operator on $\mathcal { N }$ and $\lambda _ { n } ^ { - 1 } \not \in \sigma _ { p } ( G _ { 1 } )$ By (4.15), ran $( G _ { 1 } - \lambda _ { n } ^ { - 1 } ) = \mathcal { N }$ As in the proof of (c), if $f \perp e _ { n } ,$ there is a unique h and $\mathcal { N }$ such that $L h - \lambda _ { n } h = f$ . Note that $h + \alpha e _ { n }$ is also a solution. If $h _ { 1 } , h _ { 2 }$ are two solutions, $h _ { 1 } - h _ { 2 } \in \ker ( L - \lambda _ { n } ) ,$ SO $h _ { 1 } - h _ { 2 } = \alpha e _ { n } .$

What happens if ker $L \neq ( 0 ) ?$ In this case it is possible to find a real number $\mu$ such that ker $( L - \mu ) = ( 0 )$ (Exercise 6). Replacing $q$ by $q - \mu ,$ Theorem 6.12 now applies. More information on this problem can be found in Exercises 2 through 5.

## EXERCISES

1. Consider the Sturm-Liouville operator $L h = - h ^ { \prime \prime }$ with $a = 0 ,   b = 1$ , and for each of the following boundary conditions find the eigenvalues $\{ \lambda _ { n } \}$ , the eigenvectors $\{ e _ { n } \}$ , and the Green function g(x, y): (a) h(0) = h(1) = 0; (b) $h ^ { \prime } ( 0 ) = h ^ { \prime } ( 1 ) = 0 ;$ (c) $h ( 0 ) = 0$ and $h^{\prime}(1)=0; (d) h(0)=h^{\prime}(0)$ and $h(1) = -h'(1)$

2. In Theorem 6.12 show that $\sum_{n = 1}^{\infty}\lambda_{n}^{- 2} < \infty$ (see Exercise 5.3).

3. In Theorem 6.12 show that $h { \in } { \mathcal { D } }$ if and only if he $L ^ { 2 } [ a , b ]$ and $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \lambda _ { n } ^ { 2 } | \langle h , e _ { n } \rangle | ^ { 2 } < \infty } \end{array}$ If $h { \in } { \mathcal { D } }$ , show that $h(x) = \sum_{n = 1}^{\infty} \langle h, e_n \rangle e_n(x)$ , where this series converges uniformly and absolutely on $[ a , b ]$

4. In Theorem 6.12(c), show that $h(x) = \sum_{n = 1}^{\infty} (\lambda_n - \lambda)^{-1} \langle f, e_n \rangle e_n(x)$ and this series converges uniformly and absolutely on $[ a , b ]$

5. In Theorem 6.12(d), show that if $f \perp e _ { n }$ and $L h - \lambda _ { n } h = f .$ then $h ( x ) =$ $\begin{array} { r } { \sum _ { j \neq n } ( \lambda _ { j } - \lambda _ { n } ) ^ { - 1 } \langle f , e _ { j } \rangle e _ { j } ( x ) + \alpha e _ { n } ( x ) } \end{array}$ for some $\alpha ,$ where the series converges uniformly and absolutely on $[ a , b ]$

6. This exercise demonstrates how to handle the case in which ker $L \neq ( 0 )$ (a) If $h , g { \in } C ^ { ( 1 ) } [ a , b ]$ with $h ^ { \prime } , g ^ { \prime }$ absolutely continuous and $h ^ { \prime \prime } , g ^ { \prime \prime } \in L ^ { 2 } [ a , b ]$ , show that

$$
\int _ { a } ^ { b } \left( h ^ { \prime \prime } g - h g ^ { \prime \prime } \right) = \left[ h ^ { \prime } ( b ) g ( b ) - h ( b ) g ^ { \prime } ( b ) \right] - \left[ h ^ { \prime } ( a ) g ( a ) - h ( a ) g ^ { \prime } ( a ) \right] .
$$

(b) If $h ,   g   \in   \mathcal { D }$ , show that $\langle L h , g \rangle = \langle h , L g \rangle$ . (The inner product is in $L ^ { 2 } [ a , b ] . )$ (c) If $h , g   \in   \mathcal { D }$ and $\lambda ,   \mu { \in } \mathbb { R } ,   \lambda \neq \mu ,$ and if h∈ker $( L - \lambda )$ , g∈ker $( L - \mu )$ , then $h   \bot   g .$

(d) Show that there is a real number $\mu$ with ker $( L - \mu ) = ( 0 )$

## $\S 7 ^ { * }$ The Spectral Theorem and Functional Calculus for Compact Normal Operators

We begin by characterizing the operators that commute with a diagonalizable operator. If one considers the definition of a diagonalizable operator (4.6), it is possible to reformulate it in a way that is more tractable for the present purpose and closer to the form of a compact self-adjoint operator given in (5.2). Unlike (4.6), it will not be assumed that the underlying Hilbert space is separable.

7.1. Proposition. Let $\left\{ P _ { i ^ { \cdot } } \; i { \in } I \right\}$ be a family of pairwise orthogonal projections in $\mathcal { B } ( \mathcal { H } )$ . (That is, $P _ { i } P _ { j } = P _ { j } P _ { i } = 0$ for $i \neq j . )$ If $h \in \mathcal { H }$ , then $\scriptstyle \sum _ { i } \left\{ P _ { i } h : i \in I \right\}$ converges in $\mathcal { H }$ to Ph, where P is the projection of $\mathcal { H }$ onto $\vee \left\{ P _ { i } \mathcal { H } \colon i { \in } I \right\}$

This appeared as Exercise 3.5 and its proof is left to the reader.

If $\left\{ P _ { i ^ { \cdot } } \; i { \in } I \right\}$ is as in the preceding proposition and $\mathcal { M } _ { i } = P _ { i } \mathcal { H } _ { i }$ , then with the notation of Definition 3.4, P is the projection of $\mathcal { H }$ onto $\oplus _ { i } \mathcal { M } _ { i }$ Write $\boldsymbol { P } = \sum _ { i } \boldsymbol { P } _ { i } .$ A word of caution here: $\begin{array} { r } { \pmb { P } \pmb { h } = \sum _ { i } \pmb { P } _ { i } \pmb { h } _ { i } } \end{array}$ where the convergence is in the norm of $\mathcal { H }$ . However, $\sum _ { i } P _ { i }$ does not converge to $P$ in the norm of $\mathcal { B } ( \mathcal { H } )$ In fact, it never does unless I is finite (Exercise 1).

7.2. Definition. A partition of the identity on $\mathcal { H }$ is a family $\{ P _ { i } ; i { \in } I \}$ of pairwise orthogonal projections on $\mathcal { H }$ such that $\nabla _ { i } P _ { i } \mathcal { H } = \mathcal { H }$ .This might be indicated by $\mathbf { 1 } = { \sum _ { i } } \pmb { P } _ { i }$ or $\mathbf { 1 } = \oplus _ { i } P _ { i }$ . [Note that 1 is often used to denote the operator on $\mathcal { H }$ defined by $1 ( h ) = h$ for all h. Similarly if $\alpha \in \mathbb { F } ,$ α is the operator defined by $\alpha ( h ) = \alpha h$ for all h.]

7.3. Definition. An operator A on $\mathcal { H }$ is diagonalizable if there is a partition of the identity on $\mathcal { H } ,   \{ P _ { i } \colon i { \in } I \}$ , and a family of scalars $\{ \alpha _ { i } ;   i { \in } I \}$ such that su $\mathbf { p } _ { i } | \alpha _ { i } | < \infty$ and $A { \pmb h } = \alpha _ { i } { \pmb h }$ whenever heran $P _ { i } .$

It is easy to see that this is equivalent to the definition given in (4.6) when $\mathcal { H }$ is separable (Exercise 2). Also, $\| A \| = \operatorname{supp}_{i} | \alpha_{i} |$

To denote a diagonalizable operator satisfying the conditions of(7.3), write

$$
A = \sum _ { i } \alpha _ { i } P _ { i } \quad { \mathrm { o r } } \quad A = \oplus _ { i } \alpha _ { i } P _ { i } .
$$

Note that it was not assumed that the scalars $\alpha _ { i }$ in (7.3) are distinct. There is no loss in generality in assuming this, however. In fact, if $\alpha _ { i } = \alpha _ { j i }$ then we can replace $P _ { i }$ and $P _ { j }$ with $P _ { i } + P _ { j } ,$

7.4. Proposition. An operator A on $\mathcal { H }$ is diagonalizable if and only if there is an orthonormal basis for $\mathcal { H }$ consisting of eigenvectors for A.

PROOF. Exercise.

Also note that if $\pmb { A } = \oplus _ { i } \alpha _ { i } \pmb { P } _ { i } ,$ then $\bar { A } ^ { * } = \oplus _ { i } \bar { \alpha } _ { i } \bar { P } _ { i }$ and A is normal (Exercise 5).

7.5. Theorem. If $\boldsymbol { A } = \oplus _ { i } \alpha _ { i } \boldsymbol { P } _ { i }$ is diagonalizable and all the $\alpha _ { i }$ are distinct, then an operator B in $\mathcal { B } ( \mathcal { H } )$ satisfies $AB = BA$ if and only if for each i, ran $P _ { i }$ reduces B.

PROOF. If all the $\alpha _ { i }$ are distinct, then ran $P _ { i } = \ker ( A - \alpha _ { i } )$ . If $A B = B A$ and $A h = \alpha _ { i } h _ { i }$ then $ABh = BAh = B(\alpha_i h) = \alpha_i Bh;$ hence Bheran $P _ { i }$ whenever heran $P _ { i } .$ Thus ran $P _ { i }$ is left invariant by B. Therefore B leaves $\forall \left\{ \operatorname { r a n } P _ { j } \right\}$ $j \neq i \} = { \mathcal { N } }$ invariant. But since $\oplus_{i}P_{i}=1,\mathcal{N}_{i}=(\mathrm{ran}P_{i})^{\perp}$ . Thus ran $P _ { i }$ reduces B.

Now assume that B is reduced by each ran $P _ { i } .$ Thus $\boldsymbol{B}\boldsymbol{P}_{i}=\boldsymbol{P}_{i}\boldsymbol{B}$ for all i. If $h \in \mathcal { H }$ then $\begin{array} { r } { \pmb { A } \pmb { h }   =   \sum _ { i }   \alpha _ { i } \pmb { P } _ { i } \pmb { h } } \end{array}$ Hence $\begin{array} { r } { B A h = \sum _ { i } \alpha _ { i } B P _ { i } h = \sum _ { i } \alpha _ { i } P _ { i } B h = A B h . } \end{array}$ (Why is the first equality valid?)

Using the notation of the preceding theorem, if $AB = BA$ let $B_{i} = B \left| \tan P_{i} \right|$ Then it is appropriate to write $\pmb { B } = \oplus _ { i } \pmb { B } _ { i }$ on $\mathcal { H } = \oplus _ { i } ( P _ { i } \mathcal { H } )$ . One might paraphrase Theorem 7.5 by saying that B commutes with a diagonalizable operator if and only if B can be “diagonalized with operator entries."

7.6. Spectral Theorem for Compact Normal Operators. If T is a compact normal operator on the complex Hilbert space $\mathcal { H } ,$ , then T has only a countable number of distinct eigenvalues. $\mathit { I f } \{ \lambda _ { 1 } , \lambda _ { 2 } , \ldots \}$ are the distinct nonzero eigenvalues of T, and $P _ { n }$ is the projection of $\mathcal { H }$ onto ker $( T - \lambda _ { n } ) ,$ then $P_{n}P_{m}=P_{m}P_{n}=0$ if n≠m and

## 7.7

$$
T = \sum _ { n = 1 } ^ { \infty } \lambda _ { n } P _ { n } ,
$$

where this series converges to T in the metric defined by the norm on $\mathcal { B } ( \mathcal { H } )$

PROOF. Let $A = ( T + T ^ { * } ) / 2 , B = ( T - T ^ { * } ) / 2 i .$ So A, B are compact self-adjoint operators, $T = A + i B ,$ and $AB = BA$ since T is normal. The idea of the proof is rather simple. We'll get started in this proof together but the reader will have to complete the details.

By Theorem 5.1, $\begin{array} { r } { \pmb { A } = \sum _ { 1 } ^ { \infty } \alpha _ { n } E _ { n } , } \end{array}$ where $\alpha _ { n } \in \mathbb { R } , \alpha _ { n } \neq \alpha _ { m }$ i $n \neq m ,$ and $E _ { n }$ is the projection of $\mathcal { H }$ onto $\ker ( A - \alpha _ { n } )$ . Since $AB = BA$ , the idea is to use Theorem 7.5 and Theorem 5.1 applied to B to diagonalize A and B simultaneously; that is, to find an orthonormal basis for $\mathcal { H }$ consisting of vectors that are simultaneously eigenvectors of A and B.

Since $BA = AB,   E_n \mathcal{H} = \mathcal{L}_n$ reduces B for every n (7.5). Let $B _ { n } = B | \mathcal { L } _ { n }$ then $B _ { n } = B _ { n } ^ { * }$ and dim $\mathcal { L } _ { n } < \infty$ . Applying (5.1) (or, rather, the corresponding theorem from linear algebra) to $B _ { n } ,$ there is a basis $\left\{ e^{(n)} : 1 \leqslant j \leqslant d_n \right\}$ for $\mathcal { L } _ { n }$ and real numbers $\left\{ \beta _ { j } ^ { ( n ) } : \quad 1 \leqslant j \leqslant d _ { n } \right\}$ such that $B_{n}e_{j}^{(n)} = \beta_{j}^{(n)}e_{j}^{(n)}$ Thus $T e _ { i } ^ { ( n ) } = A e _ { i } ^ { ( n ) } + i B e _ { i } ^ { ( n ) } = ( \alpha _ { n } + i \beta _ { i } ^ { ( n ) } ) e _ { i } ^ { ( n ) } .$

Therefore $\left\{ e_{j}^{(n)} : 1 \leqslant j \leqslant d_{n}, n \geqslant 1 \right\}$ is a basis for cl(ran A) consisting of eigenvectors for T. It may be that cl(ran $A) \ne \mathrm{cl}(\mathrm{ran} T)$ . Since B is reduced by ker $A = ( \tan A )^{\perp}$ and $B _ { 0 } = B |$ ker A is a compact self-adjoint operator there is an orthonormal basis $\big \{ e _ { j } ^ { ( 0 ) } \colon j \geqslant 1 \big \}$ for cl(ran $B _ { 0 } )$ and scalars $\big \{ \beta _ { j } ^ { ( 0 ) } ;   j \geqslant 1 \big \}$ such that $B e _ { j } ^ { ( 0 ) }   =   \beta _ { j } ^ { ( 0 ) } e _ { j } ^ { ( 0 ) }$ .It follows that $\tilde { T e _ { j } ^ { ( 0 ) } } = i \beta _ { j } ^ { ( 0 ) } e _ { j } ^ { ( 0 ) }$ Moreover, ker $T ^ { * } \supseteq$ ker $A \cap$ ker $B _ { 0 }$ so cl(ran $T )   \subseteq   \mathbf { c l }$ (ran A)⊕cl(ran $\dot { \pmb { B _ { 0 } } } )$

The remainder of the proof now consists in a certain amount of bookeeping to gather together the eigenvectors belonging to the same eigenvalues of $T$ and the performing of some light housekeeping chores to obtain the convergence of the series (7.7) ■

7.8. Corollary. With the notation of (7.6):

(a) ker $T = [ \vee \{ P _ { n } \mathcal { H } \colon n \geqslant 1 \} ] ^ { \perp } ;$

(b) each $P _ { n }$ has finite rank;

(c) | $\| T \| = \sup \{ | \lambda_n | : n \geqslant 1 \}$ and either $\{ \lambda _ { n } \}$ is finite or $\lambda _ { n }   \to   0$ as $n   \to   \infty$

The proof of (7.8) is similar to the proof of (5.3).

7.9. Corollary. If T is a compact operator on a complex Hilbert space, then $T$ is normal if and only if T is diagonalizable.

If $T$ is a normal operator which is not necessarily compact, there is a spectral theorem for $T$ which has a somewhat different form. This theorem states that $T$ can be represented as an integral with respect to a measure whose values are not numbers but projections on a Hilbert space. Theorem 7.6 will be a consequence of this more general theorem and correspond to the case in which this projection-valued measure is “atomic."

The approach to this more general spectral theorem will be to develop a functional calculus for normal operators T. That is, an operator $\phi ( T )$ will be defined for every bounded Borel function $\phi$ on $\pmb { \mathbf { C } }$ and certain properties of the map $\phi { \mapsto } \phi ( T )$ will be deduced. The projection-valued measure will then be obtained by letting $\mu ( \Delta ) = \chi _ { \Delta } ( T )$ , where $\chi _ { \Delta }$ is the characteristic function of the set $\mathbf { \Delta } .$ These matters are taken up in Chapter $\mathbf { I } \mathbf { X }$

At this point, Theorem 7.6 will be used to develop a functional calculus for compact normal operators. For the remainder of this section $\mathcal { H }$ is a complex Hilbert space.

7.10. Definition. Denote by $l ^ { \infty } ( \mathbf { C } )$ all the bounded functions φ: $\mathbf { C }   \to   \mathbf { C }$ If T is a compact normal operator satisfying (7.7), define $\phi ( T ) : { \mathcal { H } } \to { \mathcal { H } }$ by

$$
\phi ( T ) = \sum _ { n = 1 } ^ { \infty } \phi ( \lambda _ { n } ) P _ { n } + \phi ( 0 ) P _ { 0 } ,
$$

where $P _ { 0 } =$ the projection of $\mathcal { H }$ onto ker $T .$

Note that $\phi ( T )$ is a diagonalizable operator and $\| \phi ( T ) \| = \operatorname* { s u p } \{ | \phi ( 0 ) |$ $| \phi ( \lambda _ { 1 } ) | , \ldots \}$ (4.6). Much more can be said.

7.11. Functional Calculus for Compact Normal Operators. If T is a compact normal operator on a C-Hilbert space $\mathcal { H } ,$ then the map $\phi   \mapsto   \phi ( T )$ of $l ^ { \infty } ( \mathbb { C } ) \to { \mathcal { B } } ( { \mathcal { H } } )$ has the following properties:

(a) $\phi   \mapsto   \phi ( T )$ is a multiplicative linear map of $l ^ { \infty } ( \pmb { \mathbb { C } } )$ into $\mathcal { B } ( \mathcal { H } )$ .If $\phi \equiv 1$ $\phi ( T ) = 1 ; \; i f \; \phi ( z ) = z \; \mathrm { o n } \; \sigma _ { p } ( T ) \cup \{ 0 \}$ , then $\phi ( T ) = T .$

(b) $\phi ( T ) \parallel = \operatorname* { s u p } \{ | \phi ( \lambda ) | : \lambda \in \sigma _ { p } ( T ) \}$

(c) $\phi ( T ) ^ { * }   =   \phi ^ { * } ( T ) ,$ where $\phi ^ { * }$ is the function defined by $\phi ^ { * } ( z ) = { \overline { { \phi ( z ) } } }$

(d) If $A   \in   \mathcal { B } ( \mathcal { H } )$ and $A T = T A$ then $A \phi ( T ) = \phi ( T ) A$ for all $\phi$ in $l ^ { \infty } ( \pmb { \mathbb { C } } )$

PRooF. Adopt the notation of Theorem 7.6 and (7.10).

(a) If $\phi ,   \psi   \in   l ^ { \infty } ( \mathbb { C } )$ , then $( \phi \psi ) ( z ) = \phi ( z ) \psi ( z )$ for z in C. Also, $\phi ( T ) \psi ( T ) h =$ $\left[ \phi ( 0 ) P _ { 0 } + \sum \phi ( \lambda _ { n } ) P _ { n } \right] \left[ \psi ( 0 ) P _ { 0 } + \sum \psi ( \lambda _ { m } ) P _ { m } \right] h = \left[ \phi ( 0 ) P _ { 0 } + \sum \phi ( \lambda _ { n } ) P _ { n } \right]$ $[ \psi ( 0 ) P _ { 0 } h + \textstyle { \sum _ { m } } \psi ( \lambda _ { m } ) P _ { m } h ]$ Since $P _ { n } P _ { m } = 0$ when $n \neq m ,$ this gives that $\begin{array} { r } { \phi ( T ) \psi ( T ) h = \phi ( 0 ) \psi ( 0 ) P _ { 0 } h + \sum _ { n } \phi ( \lambda _ { n } ) \psi ( \lambda _ { n } ) P _ { n } h = ( \phi \psi ) ( T ) h . } \end{array}$ Thus $\phi { \mapsto } \phi ( T )$ is multiplicative. The linearity of the map is left to the reader. If $\phi ( z ) = 1$ , then $\phi(T)=1(T)=P_{0}+\sum_{n = 1}^{\infty}P_{n}=1$ since $\{ \boldsymbol { P } _ { 0 } , \boldsymbol { P } _ { 1 } , \ldots \}$ is a partition of the identity. If $\phi ( z ) = z , \phi ( \lambda _ { n } ) = \lambda _ { n }$ and so $\phi ( T ) = T .$

Parts (b) and (c) follow from Exercise 5.

(d) If $A T = T A ,$ Theorem 7.5 implies that $\boldsymbol{P}_{0} \mathcal{H}, \boldsymbol{P}_{1} \mathcal{H}, \ldots$ . all reduce A. Fix $h _ { n }$ in $P _ { n } \mathcal { H } , \quad n \geqslant 0$ If $\phi   \in   l ^ { \infty } ( \mathbb { C } )$ , then $A h _ { n } \in P _ { n } \mathcal { H }$ and so $\phi ( T ) A h _ { n } =$ $\phi ( \lambda _ { n } ) A h _ { n } = A ( \phi ( \lambda _ { n } ) h _ { n } ) = A \phi ( T ) h _ { n }$ If $h \in \mathcal { H }$ then $h = \sum _ { n = 0 } ^ { \infty } h _ { n } ,$ where $h _ { n } { \in } P _ { n ^ { * } }$ Hence $\begin{array} { r } { \phi ( T ) A h = \sum _ { n = 0 } ^ { \infty } \phi ( T ) A h _ { n } = \sum _ { n = 0 } ^ { \infty } A \phi ( T ) h _ { n } = A \phi ( T ) h . } \end{array}$ (Justify the first equality.)

Which operators on $\mathcal { H }$ can be expressed as $\phi ( T )$ for some $\phi$ in $l ^ { \infty } ( \mathbb { C } ) ?$ Part (d) of the preceding theorem provides the answer.

7.12. Theorem. If T is a compact normal operator on a C-Hilbert space, then $\{ \phi ( T ) { : } \phi { \in } l ^ { \infty } ( \mathbb { C } ) \}$ is equal to

$$
\{ B { \in } { \mathcal { B } } ( { \mathcal { H } } ) { : ~ } B A = A B { ~ w h e n e v e r ~ } A T = T A \} .
$$

PRooF. Half of the desired equality is obtained from (7.11d). So let $B \in \mathcal { B } ( \mathcal { H } )$ and assume that $BA = AB$ whenever. $A T = T A$ . Thus, B must commute with T itself. By (7.5), B is reduced by each $P _ { n } \mathcal { H } \equiv \mathcal { H } _ { n } , n \geqslant 0 ;$ put $B _ { n } = B \left| \mathcal { H } _ { n } \right|$ Fix $n   \geqslant   0$ for the moment and let $A _ { n }$ be any bounded operator in $\mathcal { B } ( \mathcal { H } _ { n } )$ Define $A h = A _ { n } h \text { if } h \in \mathcal { H } _ { n }$ and $A h = 0 \text { if } h \in \mathcal { H } _ { m } , m \neq n$ , and extend A to $\mathcal { H }$ by linearity; so $A = \bigoplus_{m = 0}^{\infty} A_{m}$ where $A_{m}=0 \text { if } m \neq n. \text { By } (7.5), A T=T A$ ; hence $BA = AB$ This implies that $B_{n}A_{n}=A_{n}B_{n}.$ Since $A _ { n }$ was arbitrarily chosen from $\mathcal { B } ( \mathcal { H } _ { n } ) ,$ $B _ { n } = \beta _ { n }$ for some $\beta _ { n }$ (Exercise 7). If $\phi \colon \mathbf { C }   \to   \mathbf { C }$ is defined by $\phi ( 0 ) = \beta _ { 0 }$ and $\phi ( \lambda _ { n } ) = \beta _ { n }$ for $n \geqslant 1$ , then $B = \phi ( T )$

7.13. Definition. If $A   \in   \mathcal { B } ( \mathcal { H } ) .$ , then A is positive if $\langle A h , h \rangle \geqslant 0$ for all h in $\mathcal { H } ,$ In symbols this is denoted by $A \geqslant 0$

Note that by Proposition 2.12 every positive operator on a complex Hilbert space is self-adjoint.