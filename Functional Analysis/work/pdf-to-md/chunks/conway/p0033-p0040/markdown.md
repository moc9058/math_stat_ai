## EXERCISES

1. Verify the statements in Example 4.3.

2. Verify the statements in Example 4.4.

3. Verify the statements in Example 4.5.

4. Find an infinite orthonormal set in the Hilbert space of Example 1.8.

5. Using the notation of the Gram-Schmidt Orthogonalization Process, show that up to scalar multiple $e _ { 1 }   =   h _ { 1 } / \|   h _ { 1 }   \|$ and for $n \geqslant 2, e_n = \| h_n - f_n \|^{-1} (h_n - f_n).$ , where $f _ { n }$ is the vector defined formally by

$$
f_{n} = \frac{-1}{\det\left[ \left\langle h_{i}, h_{j} \right\rangle \right]_{i,j=1}^{n-1}} \det \begin{bmatrix} \left\langle h_{1}, h_{1} \right\rangle & \cdots & \left\langle h_{n-1}, h_{1} \right\rangle & \left\langle h_{n}, h_{1} \right\rangle \\ \vdots & & \vdots & \vdots \\ \left\langle h_{1}, h_{n-1} \right\rangle & \cdots & \left\langle h_{n-1}, h_{n-1} \right\rangle & \left\langle h_{n}, h_{n-1} \right\rangle \\ h_{1} & \cdots & h_{n-1} & 0 \end{bmatrix}
$$

In the next three exercises, the reader is asked to apply the Gram-Schmidt Orthogonalization Process to a given sequence in a Hilbert space. A reference for this material is pp. 82–96 of Courant and Hilbert [1953].

6. If the sequence $1 , x , x ^ { 2 } , \ldots$ . is orthogonalized in $L ^ { 2 } ( - 1 , 1 )$ the sequence $e _ { n } ( x ) = [ \frac { 1 } { 2 } ( 2 n + 1 ) ] ^ { 1 / 2 } P _ { n } ( x )$ is obtained, where

$$
P _ { n } ( x ) = \frac { 1 } { 2 ^ { n } n ! } \left( \frac { d } { d x } \right) ^ { n } ( x ^ { 2 } - 1 ) ^ { n } .
$$

The functions $P _ { \pmb { n } } ( \pmb { x } )$ are called Legendre polynomials.

7. If the sequence $e^{-x^{2}/2}, xe^{-x^{2}/2}, x^{2}e^{-x^{2}/2}$ . is orthogonalized in $L ^ { 2 } ( - \infty , \infty )$ , the sequence $e _ { n } ( x ) = \left[ 2 ^ { n } n ! \sqrt { \pi } \right] ^ { - 1 / 2 } H _ { n } ( x ) e ^ { - x ^ { 2 } / 2 }$ is obtained, where

$$
H _ { n } ( x ) = ( - 1 ) ^ { n } e ^ { x ^ { 2 } } \left( \frac { d } { d x } \right) ^ { n } e ^ { - x ^ { 2 } } .
$$

The functions $H _ { n }$ are Hermite polynomials and satisfy $H_{n}^{\prime}(x) = 2nH_{n - 1}(x)$

8. If the sequence $e^{-x/2},xe^{-x/2},x^{2}e^{-x/2}$ . is orthogonalized in $L ^ { 2 } ( 0 , \infty )$ , the sequence $e _ { n } ( x ) = e ^ { - x / 2 } L _ { n } ( x ) / n !$ is obtained, where

$$
L _ { n } ( x ) = e ^ { x } \left( \frac { d } { d x } \right) ^ { n } \left( x ^ { n } e ^ { - x } \right).
$$

The functions $L _ { n }$ are called Laguerre polynomials.

9. Prove Corollary 4.10 using Definition 4.11.

10. If $\{ h _ { n } \}$ is a sequence in Hilbert space and $\sum \{ h _ { n } ; n \in \mathbb { N } \}$ converges to h (Definition 4.11), then lim $\sum_{n = 1}^{n} h_{k} = h$ Show that the converse is false.

11. If $\{ h _ { n } \}$ is a sequence in a Hilbert space and $\textstyle \sum _ { n = 1 } ^ { \infty } \| h _ { n } \| < \infty$ , show that $\scriptstyle \sum \left\{ h _ { n } : n \in \mathbb { N } \right\}$ converges in the sense of Definition 4.11.

12. Let $\{ \alpha _ { n } \}$ be a sequence in F and prove that the following statements are equivalent: $(a) \sum \{ \alpha_{n} : n \in \mathbb{N} \}$ converges in the sense of Definition 4.11. (b) If π is any permutation of N, then $\sum _ { n = 1 } ^ { \infty } \alpha _ { \pi ( n ) }$ converges (unconditional convergence). (c) $\textstyle \sum _ { n = 1 } ^ { \infty } | \alpha _ { n } | < \infty$

13. Let $\mathcal { E }$ be an orthonormal subset of $\mathcal { H }$ and let $\mathcal { M } = \nabla \mathcal { E }$ If $P$ is the orthogonal projection of $\mathcal { H }$ onto $\mathcal { M } ,$ show that $P h = \sum \{ \langle h , e \rangle e : e \in \mathcal { E } \}$ for every h in $\mathcal { H }$

14. Let $\lambda = \mathbf { A r e a }$ measure on $\{ z { \in } \mathbb { C } ; | z | < 1 \}$ and show that $1 , z , z ^ { 2 } , \ldots$ are orthogonal vectors in $L ^ { 2 } ( \lambda )$ . Find $\| z ^ { n } \| , n \geqslant 0.$ If $e _ { n } = \left\| z ^ { n } \right\| ^ { - 1 } z ^ { n } , n \geqslant 0 ,$ is $\{ e _ { 0 } , e _ { 1 } , \ldots \}$ a basis for $L ^ { 2 } ( \lambda ) ?$

15. In the proof of (4.14), show that if either ε or $\eta$ is finite, then $\varepsilon = \eta .$

16. If $\mathcal { H }$ is an infinite dimensional Hilbert space, show that no orthonormal basis for $\mathcal { H }$ is a Hamel basis. Show that a Hamel basis is uncountable.

17. Let $d \geqslant 1$ and let $\mu$ be a regular Borel measure on $\mathbf { R } ^ { d } .$ Show that $L ^ { 2 } ( \mu )$ is separable.

18. Suppose $L ^ { 2 } ( X , \Omega , \mu )$ is separable and $\left\{ E _ { i } ;   i { \in } I \right\}$ is a collection of pairwise disjoint subsets of $X ,   E _ { i } { \in } \Omega .$ and $0 < \mu ( E _ { i } ) < \infty$ for all i.. Show that I is countable. Can you allow $\mu ( E _ { i } ) = \infty ?$

19. If $\{ h { \in } { \mathcal { H } } \colon \| h \| \leqslant 1 \}$ is compact, show that dim $\mathcal { H } < \infty$

20. What is the cardinality of a Hamel basis for $l ^ { 2 } { \stackrel { \leftrightarrow } { . } }$

## §5. Isomorphic Hilbert Spaces and the Fourier Transform for the Circle

Every mathematical theory has its concept of isomorphism. In topology there is homeomorphism and homotopy equivalence; algebra calls them isomorphisms. The basic idea is to define a map which preserves the basic structure of the spaces in the category.

5.1. Definition. If $\mathcal { H }$ and $\mathcal { H }$ are Hilbert spaces, an isomorphism between $\mathcal { H }$ and $\mathcal { H }$ is a linear surjection $U \colon { \mathcal { H } } \to { \mathcal { H } }$ such that

$$
\langle U h , U g \rangle = \langle h , g \rangle
$$

for all $h , g$ in $\mathcal { H }$ In this case $\mathcal { H }$ and $\mathcal { H }$ are said to be isomorphic.

It is easy to see that if $U \colon { \mathcal { H } } \to { \mathcal { H } }$ is an isomorphism, then so is $U ^ { - 1 }$ $\mathcal { H } \rightarrow \mathcal { H }$ . Similar such arguments show that the concept of “isomorphic" is an equivalence relation on Hilbert spaces. It is also certain that this is the correct equivalence relation since an inner product is the essential ingredient for a Hilbert space and isomorphic Hilbert spaces have the “same"inner product. One might object that completeness is another essential ingredient in the definition of a Hilbert space. So it is! However, this too is preserved by an isomorphism. An isometry between metric spaces is a map that preserves distance.

5.2. Proposition. If $V \colon { \mathcal { H } } \to { \mathcal { H } }$ is a linear map between Hilbert spaces, then $V$ is an isometry $i f$ and only $if \langle Vh, Vg \rangle = \langle h, g \rangle$ for all $h , g$ in $\mathcal { H }$

PROOF. Assume $\langle V h , V g \rangle = \langle h , g \rangle$ for all $h , g$ in $\mathcal { H }$ Then $\| V h \| ^ { 2 } = \langle V h , V h \rangle =$ $\langle h , h \rangle = \| h \| ^ { 2 }$ and V is an isometry.

Now assume that V is an isometry. If $h , g \in \mathcal { H }$ and $\lambda \in \mathbf { F } ,$ then $\| h + \lambda g \| ^ { 2 } = \| V h + \lambda V g \| ^ { 2 }$ . Using the polar identity on both sides of this equation gives

$$
\| h \| ^ { 2 } + 2 \operatorname { R e } \bar { \lambda } \langle h , g \rangle + | \lambda | ^ { 2 } \| g \| ^ { 2 } = \| V h \| ^ { 2 } + 2 \operatorname { R e } \bar { \lambda } \langle V h , V g \rangle + | \lambda | ^ { 2 } \| V g \| ^ { 2 } .
$$

But $\|   V { \pmb h }   \| = \|   { \pmb h }   \|$ and $\| V g \| = \| g \|$ , so this equation becomes

$$
\mathrm { R e } \bar { \lambda } \langle h , g \rangle = \mathrm { R e } \bar { \lambda } \langle V h , V g \rangle
$$

for any λ in F. If $\mathbf { F }   =   \mathbf { R }$ , take $\lambda = 1.  If  \mathbb{F} = \mathbb{C},$ first take $\lambda   =   1$ and then take $\lambda = i$ to find that $\langle h , g \rangle$ and $\langle V h , V g \rangle$ have the same real and imaginary parts.

Note that an isometry between metric spaces maps Cauchy sequences into Cauchy sequences. Thus an isomorphism also preserves completeness. That is, if an inner product space is isomorphic to a Hilbert space, then it must be complete.

5.3. Example. Definite S: $l ^ { 2 }   \rightarrow   l ^ { 2 }$ by $S(\alpha_{1},\alpha_{2},\ldots)=(0,\alpha_{1},\alpha_{2},\ldots)$ Then $s$ is an isometry that is not surjective.

The preceding example shows that isometries need not be isomorphisms.

A word about terminology. Many call what we call an isomorphism a unitary operator. We shall define a unitary operator as a linear transformation $U \colon { \mathcal { H } } \to { \mathcal { H } }$ that is a surjective isometry. That $\mathbf { i s } ,$ a unitary operator is an isomorphism whose range coincides with its domain. This may seem to be a minor distinction, and in many ways it is. But experience has taught me that there is some benefit in making such a distinction, or at least in being aware of it.

5.4. Theorem. Two Hilbert spaces are isomorphic if and only if they have the same dimension.

PROOF. If $U \colon { \mathcal { H } } \to { \mathcal { H } }$ is an isomorphism and $\mathcal { E }$ is a basis for $\mathcal { H }$ , then it is easy to see that $U \mathcal { E } \equiv \{ U e \colon e { \in } \mathcal { E } \}$ is a basis for $\mathcal { H }$ . Hence, dim $\mathcal { H } = \dim \mathcal { H }$

Let $\mathcal { H }$ be a Hilbert space and let $\mathcal { E }$ be a basis for $\mathcal { H }$ .Consider the Hilbert space $l ^ { 2 } ( \mathcal { S } )$ If $h \in \mathcal { H }$ , define $\hat { h } \colon \mathcal { E } \to \mathbb { F }$ by $\hat { h } ( e ) = \langle h , e \rangle$ . By Parseval's Identity $\hat { h }   \in   l ^ { 2 } ( \mathcal { E } )$ and $\| \boldsymbol { h } \| = \| \hat { \boldsymbol { h } } \|$ . Define $U \colon { \mathcal { H } }   \to   l ^ { 2 } ( { \mathcal { E } } )$ by $U h = { \hat { h } } .$ Thus $U$ is linear and an isometry. It is easy to see that ran U contains all the functions $f$ in $l ^ { 2 } ( \mathcal { S } )$ such that $f ( e ) = 0$ for all but a finite number of $e ,$ that is, ran $U$ is dense. But $U ,$ being an isometry, must have closed range. Hence U: $\mathcal { H } \rightarrow l ^ { 2 } ( \mathcal { E } )$ is an isomorphism.

If $\mathcal { H }$ is a Hilbert space with a basis $\mathcal { F } , \mathcal { H }$ is isomorphic to $l ^ { 2 } ( \mathcal { F } )$ If dim $\mathcal{H} = \dim \mathcal{H}, \mathcal{E}$ and $\mathcal { F }$ have the same cardinality; it is easy to see that $l ^ { 2 } ( \mathcal { S } )$ and $l ^ { 2 } ( \mathcal { F } )$ must be isomorphic. Therefore $\mathcal { H }$ and $\mathcal { H }$ are isomorphic.

5.5. Corollary. All separable infinite dimensional Hilbert spaces are isomorphic.

This section concludes with a rather important example of an isomorphism, the Fourier transform on the circle.

The proof of the next result can be found as an Exercise on p. 263 of Conway [1978]. Another proof will be given latter in this book after the Stone-Weierstrass Theorem is proved. So the reader can choose to assume this for the moment. Let $\mathbf { D }   =   \{ z   \in   \pmb { \mathbb { C } } : | z | < 1 \}$

5.6. Theorem. If $f \colon \partial \mathbb { D }   \to   \mathbb { C }$ is a continuous function, then there is a sequence $\left\{ p _ { n } ( z , { \bar { z } } ) \right\}$ of polynomials in z and ž such that $p _ { n } ( z , { \bar { z } } ) \to f ( z )$ uniformly on ∂D.

Note that if $z { \in } { \partial } \mathbb { D } ,   \bar { z } = z ^ { - 1 }$ . Thus a polynomial in z and $\bar { z }$ on ∂ID becomes a function of the form

$$
\sum _ { k = - n } ^ { n } \alpha _ { k } z ^ { k } .
$$

If we put $z = e ^ { i \theta } ,$ this becomes a function of the form

$$
\sum _ { k = - m } ^ { n } \alpha _ { k } e ^ { i k \theta } .
$$

Such functions are called trigonometric polynomials.

We can now show that the orthonormal set in Example 4.3 is a basis for $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ . This is a rather important result.

5.7. Theorem. If for each n in $e _ { n } ( t ) \equiv ( 2 \pi ) ^ { - 1 / 2 } \exp ( i n t ) ,$ then $\{ e _ { n } ; n { \in } \mathbb { Z } \}$ is a basis for $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$

PROOF. Let $\mathcal { T } = \left\{ \sum _ { k = - n } ^ { n } \alpha _ { k } e _ { k } : \alpha _ { k } \in \mathbb { C } , n \geqslant 0 \right\}$ . Then $\mathcal { T }$ is a subalgebra of $C _ { \mathbb { C } } [ 0 , 2 \pi ] ,$ the algebra of all continuous C-valued functions on [0, 2π]. Note that if $f   \in   \mathcal { T } ,   f ( 0 )   =   f ( 2 \pi )$ .We want to show that the uniform closure of $\mathcal { T }$ is ${ \mathcal { C } } \equiv \left\{ f \in C _ { \mathbb { C } } [ 0 , 2 \pi ] : f ( 0 ) = f ( 2 \pi ) \right\}$ . To do this, let $f \in \mathcal { C }$ and define $F : \partial \mathbb { D } \to \mathbb { C }$ by $F ( e ^ { i t } ) = f ( t )$ F is continuous. (Why?) By (5.6) there is a sequence of polynomials in z and $\bar { z } ,   \left\{ p _ { n } ( z , \bar { z } ) \right\}$ , such that $p _ { n } ( z , \bar { z } ) \to F ( z )$ uniformly on ∂D. Thus $p _ { n } ( e ^ { i t } , e ^ { - i t } ) \to f ( t )$ uniformly on [0, 2π]. But $p _ { n } ( e ^ { i t } , e ^ { - i t } ) \in \mathcal { T }$

Now the closure of € in $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ is all of $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ (Exercise 6). Hence $\nabla \left\{ e _ { n } \colon n { \in } \mathbb { Z } \right\} = L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ and $\{ e _ { n } \}$ is thus a basis (4.13). ■

Actually, it is usually preferred to normalize the measure on [0, 2π]. That is, replace dt by $( 2 \pi ) ^ { -   1 }   d t$ , so that the total measure of [0, 2π] is 1. Now define $e _ { n } ( t ) = \exp ( i n t )$ . Hence $\{ e _ { n } \colon n { \in } \mathbb { Z } \}$ is a basis for $\mathcal { H } \equiv L _ { \mathbb { C } } ^ { 2 } ( [ 0 , 2 \pi ] , ( 2 \pi ) ^ { - 1 } d t )$ . If $f \in \mathcal { H }$ , then

$$
\hat { f } ( n ) \equiv \langle f , e _ { n } \rangle = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) e ^ { - i n t } d t\tag{5.8}
$$

is called the nth Fourier coefficient of f, n in Z. By (5.7) and (4.13d)

$$
f = \sum _ { n = - \infty } ^ { \infty } { \hat { f } } ( n ) e _ { n } ,\tag{5.9}
$$

where this infinite series converges to $f$ in the metric defined by the norm of $\mathcal { H }$ . This is called the Fourier series of $f .$ This terminology is classical and has been adopted for a general Hilbert space.

If $\mathcal { H }$ is any Hilbert space and $\mathcal { E }$ is a basis, the scalars $\{ \langle h , e \rangle ; e { \in } { \mathcal { E } } \}$ are called the Fourier coefficients of h (relative to ) and the series in (4.13d) is called the Fourier expansion of h (relative to $\mathcal { S } )$

Note that Parseval's Identity applied to (5.9) gives that $\scriptstyle \sum _ { n = - \infty } ^ { \infty } | { \hat { f } } ( n ) | ^ { 2 } < \infty$ This proves a classical result.

5.10. The Riemann-Lebesgue Lemma. $I f f \in L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ then $\int_{0}^{2\pi} f(t) e^{-int} dt \rightarrow 0$ as $n   \rightarrow \pm \infty$

If $f   \in   L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ , then the Fourier series of f converges to $f$ in $L ^ { 2 } \mathrm { - n o r m }$ It was conjectured by Lusin that the series converges to f almost everywhere. This was proved in Carleson [1966]. Hunt [1967] showed that if $f { \in } L _ { \mathbb { C } } ^ { p } [ 0 , 2 \pi ] , 1 < p \leqslant \infty$ , then the Fourier series also converges to f a.e. Long before that, Kolmogoroff had furnished an example of a function $f$ in $L _ { \mathbb { C } } ^ { 1 } [ 0 , 2 \pi ]$ whose Fourier series a.e. does not converge to $f .$

For f in $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ] .$ , the function $\hat { f } \colon \mathbf { Z } \to \mathbf { C }$ is called the Fourier transform of f; the map $\tilde { U } : L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ] \to l ^ { 2 } ( \mathbb { Z } )$ defined by $U f = { \hat { f } }$ is the Fourier transform. The results obtained so far can be applied to this situation to yield the following.

5.11. Theorem. The Fourier transform is a linear isometry from $L _ { \mathfrak { C } } ^ { 2 } [ 0 , 2 \pi ]$ onto $l ^ { 2 } ( \mathbb { Z } )$

PROOF. Let U: $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ] \to l ^ { 2 } ( \mathbb { Z } )$ be the Fourier transform. That U maps $L ^ { 2 } \equiv L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ into $l ^ { 2 } ( \mathbb { Z } )$ and satisfies $\|   U f   \| = \|   f   \|$ is a consequence of Parseval's Identity. That U is linear is an exercise. If $\{ \alpha _ { n } \} \in l ^ { 2 } ( \mathbb { Z } )$ and $\alpha _ { n } = 0$ for all but a finite number of $n ,$ then $f = \sum _ { n = - \infty } ^ { \infty } \alpha _ { n } e _ { n } \in \dot { L } ^ { 2 }$ . It is easy to check that $\hat { f } ( n ) = \alpha _ { n }$ for all n, so $U f = \{ \alpha _ { n } \}$ . Thus ran $U$ is dense in $l ^ { 2 } ( \mathbb { Z } )$ . But $U$ is an isometry, so ran $U$ is closed; hence U is surjective.

Note that functions in $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ can be defined on ∂D by letting $f ( e ^ { i \theta } ) = f ( \theta )$ . The ambiguity for $\theta   =   0$ and 2π (or $e ^ { i \theta } = 1 )$ might cause us to pause, but remember that elements of $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ are equivalence classes of functions—not really functions. Since $\{ 0 , 2 \pi \}$ has zero measure, there is really no ambiguity. In this way $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ can be identified with $L _ { \mathbb { C } } ^ { 2 } ( \partial \mathbf { D } )$ , where the measure on ∂D is normalized arc-length measure (normalized so that the total measure of ∂D is 1). So $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ and $L _ { \mathbb { C } } ^ { 2 } ( \partial \mathbb { D } )$ are (naturally) isomorphic. Thus, Theorem 5.11 is a theorem about the Fourier transform of the circle.

The importance of Theorem 5.11 is not the fact that $L _ { \mathbb { C } } ^ { 2 } [ 0 , 2 \pi ]$ and $l ^ { 2 } ( \mathbb { Z } )$ are isomorphic, but that the Fourier transform is an isomorphism. The fact that these two spaces are isomorphic follows from the abstract result that all separable infinite dimensional Hilbert spaces are isomorphic (5.5).

## EXERCISES

1. Verify the statements in Example 5.3.

2. Define $V \colon L ^ { 2 } ( 0 , \infty ) { \to } L ^ { 2 } ( 0 , \infty )$ by $(Vf)(t) = f(t - 1)$ if $t   >   1$ and $( V f ) ( t ) = 0$ if $t   \leqslant   1$ Show that V is an isometry that is not surjective.

3. Define $V : L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ by $(Vf)(t) = f(t - 1)$ and show that V is an isomorphism (a unitary operator).

4. Let $\mathcal { H }$ be the Hilbert space of Example 1.8 and define $U \colon { \mathcal { H } } \to L ^ { 2 } ( 0 , 1 )$ by $U f = f ^ { \prime }$ Show that U is an isomorphism and find a formula for $U ^ { - 1 }$

5. Let $( X , \Omega , \mu )$ be a σ-finite measure space and let u: $X   \to   \mathbb { F }$ be an Ω-measurable function such that sup $\{ | u ( x ) | \colon x { \in } X \} < \infty$ . Show that $U \colon L ^ { 2 } ( X , \mathbf { \Omega } , \mu )   \to   L ^ { 2 } ( X , \mathbf { \Omega } , \mu )$ defined by $U f = u f$ is an isometry if and only if $|u(x)| = 1   a.e.   [\mu]$ , in which case U is surjective.

6. Let $\mathcal { C } = \left\{ f \in C [ 0 , 2 \pi ] : f ( 0 ) = f ( 2 \pi ) \right\}$ and show that $\mathcal { C }$ is dense in $L ^ { 2 } [ 0 , 2 \pi ]$

7. Show that $\{ ( 1 / \sqrt { 2 \pi } ) , ( 1 / \sqrt { \pi } )$ cos nt, $( 1 / { \sqrt { \pi } } )$ sin nt: $1 \leqslant n < \infty \}$ is a basis for $L ^ { 2 } [ - \pi , \pi ]$

8. Let $( X , \Omega )$ be a measurable space and let $\mu , \nu$ be two σ-finite measures defined on (X, Ω). Suppose $\nu \ll \mu$ and $\phi$ is the Radon-Nikodym derivative of v with respect to $\mu \quad ( \phi = d v / d \mu )$ Define $V \colon L ^ { 2 } ( v ) \to L ^ { 2 } ( \mu )$ by $V f = { \sqrt { \phi } } f$ Show that $V$ is a well-defined linear isometry and V is an isomorphism if and only if $\mu \ll \nu$ (that is, $\mu$ and v are mutually absolutely continuous).

9. If H and $\mathcal { H }$ are Hilbert spaces and $U \colon { \mathcal { H } } \to { \mathcal { H } }$ is a surjective function such that $\langle U f , U g \rangle = \langle f , g \rangle$ for all vectors f and g in $\mathcal { H }$ , then U is linear.

## §6. The Direct Sum of Hilbert Spaces

Suppose $\mathcal { H }$ and $\mathcal { H }$ are Hilbert spaces. We want to define $\mathcal { H } \oplus \mathcal { H }$ so that it becomes a Hilbert space. This is not a difficult assignment. For any vector spaces $\mathcal { X }$ and $\mathcal { B } ,   \mathcal { X }   \oplus   \mathcal { Y }$ is defined as the Cartesian product $\mathcal { X } \times \mathcal { Y }$ where the operations are defined on $\mathcal { X } \times \mathcal { Y }$ coordinatewise. That is, if elements of $\mathcal { X } \oplus \mathcal { Y }$ are defined as $\{ x   \oplus   y { : ~ } x   \in   { \mathcal { X } } , ~ y   \in   { \mathcal { Y } } \}$ , then $(x_{1} \oplus y_{1}) + (x_{2} \oplus y_{2}) \equiv$ $( x _ { 1 } + x _ { 2 } ) \oplus ( y _ { 1 } + y _ { 2 } )$ , and so on.

6.1. Definition. If $\mathcal { H }$ and $\mathcal { H }$ are Hilbert spaces, ${ \mathcal { H } } \oplus { \mathcal { H } } = \{ h \oplus k \colon h { \in } { \mathcal { H } }$ $k \in \mathcal { H } \}$ and

$$
\langle h _ { 1 } \oplus k _ { 1 } , h _ { 2 } \oplus k _ { 2 } \rangle \equiv \langle h _ { 1 } , h _ { 2 } \rangle + \langle k _ { 1 } , k _ { 2 } \rangle .
$$

It must be shown that this defines an inner product on $\mathcal { H } \oplus \mathcal { H }$ and that $\mathcal { H } \oplus \mathcal { H }$ is complete (Exercise).

Now what happens if we want to define ${ \mathcal { H } } _ { 1 } \oplus { \mathcal { H } } _ { 2 } \oplus \cdots$ for a sequence of Hilbert spaces $\mathcal { H } _ { 1 } , \mathcal { H } _ { 2 } , \ldots$ There is a problem about the completeness of this infinite direct sum, but this can be overcome as follows.

6.2. Proposition. $If \mathcal{H}_1, \mathcal{H}_2, \ldots$ . are Hilbert spaces, let $\mathcal { H } = \left\{ \left( h _ { n } \right) _ { n = 1 } ^ { \infty } : h _ { n } \in \mathcal { H } _ { n } \right\}$ for all n and $\scriptstyle \sum _ { n = 1 } ^ { \infty } \| h _ { n } \| ^ { 2 } < \infty \}$ . For $h = ( h _ { n } )$ and $g = ( g _ { n } )$ in $\mathcal { H } ,$ define

$$
\langle h , g \rangle = \sum _ { n = 1 } ^ { \infty } \langle h _ { n } , g _ { n } \rangle .\tag{6.3}
$$

Then $\langle \cdot , \cdot \rangle$ is an inner product on $\mathcal { H }$ and the norm relative to this inner product is $\begin{array} { r } { \| h \| = [ \sum _ { n = 1 } ^ { \infty } \| h _ { n } \| ^ { 2 } ] ^ { 1 / 2 } } \end{array}$ . With this inner product $\mathcal { H }$ is a Hilbert space.

PROOF. If $h = ( h _ { n } )$ and $g = (g_n) \in \mathcal{H}$ , then the CBS inequality implies $\sum \left| \left\langle h_{n}, g_{n} \right\rangle \right| \leqslant \sum \left\| h_{n} \right\| \left\| g_{n} \right\| \leqslant \left( \sum \left\| h_{n} \right\|^{2} \right)^{1 / 2} \left( \sum \left\| g_{n} \right\|^{2} \right)^{1 / 2} < \infty$ . Hence the series in (6.3) converges absolutely. The remainder of the proof is left to the reader.

6.4. Definition. If $\mathcal { H } _ { 1 } , \mathcal { H } _ { 2 } , \ldots$ are Hilbert spaces, the space $\mathcal { H }$ of Proposition 6.2 is called the direct sum of $\mathcal { H } _ { 1 } , \mathcal { H } _ { 2 } , \ldots$ and is denoted by ${ \mathcal { H } } \equiv { \mathcal { H } } _ { 1 } \oplus { \mathcal { H } } _ { 2 } \oplus \cdots$

This is part of a more general process. If $\{ { \mathcal { H } } _ { i } ;   i { \in } I \}$ is a collection of Hilbert spaces, $\mathcal { H } \equiv \oplus \left\{ \mathcal { H } _ { i } \colon i { \in } I \right\}$ is defined as the collection of functions h: $I   \rightarrow   \cup   \{ \mathcal { H } _ { i } ; i   \in   I \}$ such that $h ( i )   \in   \mathcal { H } _ { i }$ for all i and $\textstyle \sum \{ \| h ( i ) \| ^ { 2 } : i { \in } I \} < \infty . { \mathrm { ~ I f ~ } } h , g { \in } { \mathcal { H } }$ $\langle h , g \rangle \equiv \sum \{ \langle h ( i ) , g ( i ) \rangle : i \in I \} ; \mathcal { H }$ is a Hilbert space.

The main reason for considering direct sums is that they provide a way of manufacturing operators on Hilbert space. In fact, Hilbert space is a rather dull subject, except for the fact that there are numerous interesting questions about the linear operators on them that are as yet unresolved. This subject is introduced in the next chapter.

## EXERCISES

1. Let $\left\{ ( X _ { i } , \Omega _ { i } , \mu _ { i } ) \colon i { \in } I \right\}$ be a collection of measure spaces and define X, Ω, and $\mu$ as follows. Let $X =$ the disjoint union of $\{ X _ { i } ; i { \in } I \}$ and let $\mathbf { \Omega } = \{ \mathbf { \Delta } \subseteq X \colon \mathbf { \Delta } \cap X _ { i } { \in } \mathbf { \Omega } _ { i }$ for all $i \}$ For ∆ in Ω put $\mu ( \Delta )   =   \textstyle \sum _ { i }   \mu _ { i } ( \Delta   \cap   X _ { i } )$ Show that $( X , \Omega , \mu )$ is a measure space and $L ^ { 2 } ( X , \Omega , \mu )$ is isomorphic to $\oplus \left\{ L ^ { 2 } ( \boldsymbol { X } _ { i } , \boldsymbol { \Omega } _ { i } , \mu _ { i } ) \colon i { \in } I \right\}$

2. Let $( X , \Omega )$ be a measurable space, let $\mu _ { 1 } , \mu _ { 2 }$ be σ-finite measures defined on $( X , \Omega ) ,$ and put $\mu = \mu _ { 1 } + \mu _ { 2 }$ . Show that the map $V \colon L ^ { 2 } ( X , \mathbf { \Omega } , \mu )   \to   L ^ { 2 } ( X , \mathbf { \Omega } , \mu _ { 1 } )   \oplus   L ^ { 2 } ( X , \mathbf { \Omega } , \mu _ { 2 } )$ defined by $V f = f _ { 1 } \oplus f _ { 2 } ,$ where $f _ { j }$ is the equivalence class of $L ^ { 2 } ( X , \Omega , \mu _ { j } )$ corresponding to f, is well defined, linear, and injective. Show that V is an isomorphism iff $\mu _ { 1 }$ and $\mu _ { 2 }$ are mutually singular.