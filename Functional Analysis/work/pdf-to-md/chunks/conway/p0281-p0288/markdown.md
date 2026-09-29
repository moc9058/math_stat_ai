by itself. One such account in Steen [1973]. You might also consult the notes in Dunford and Schwartz [1963] and Halmos [1951].

## EXERCISES

Throughout these exercises, N is a normal operator on $\mathcal { H }$ with spectral measure E.

1. Show that $\lambda   \in   \sigma _ { p } ( N )$ if and only if $E ( \{ \lambda \} ) \neq 0 .$ Moreover, if $\lambda { \in } \sigma _ { p } ( N ) ,   E ( \{ \lambda \} )$ is the orthogonal projection onto ker $( N - \lambda )$

2. If ∆ is a clopen subset of $\sigma ( N ) ,$ show that $E ( \Delta )$ is the Riesz idempotent associated with ∆.

3. Prove Theorem II.5.1 and its corollaries by using the Spectral Theorem.

4. Prove Theorem II.7.6 and its corollaries by using the Spectral Theorem.

5. Obtain Theorem II.7.11 as a consequence of (2.3).

6. Verify the statements in Example 2.5.

7. Verify (2.6e).

8. Show that if $\mathcal { H }$ is separable, there are at most a countable number of points $\{ z _ { n } \}$ in $\sigma ( N )$ such that $E(z_n) \neq 0$ .By Exercise 1, these are the eigenvalues of N.

9. Show that a normal operator N is (a) hermitian if and only if $\sigma ( N )   \subseteq   \mathbb { R }$ (b) positive if and only if $\sigma ( N ) \in [ 0 , \infty ) ;$ (c) unitary if and only if $\sigma ( N )   \subseteq   \partial \mathbb { D }$

10. Let A be a hermitian operator with spectral measure E on a separable space. For each real number t define a projection $P ( t ) = E ( - \infty , t )$ Show:

(a) $P(s) \leq P(t)$ for $s \leqslant t ;$

(b) if $t _ { n } \leqslant t _ { n + 1 }$ and $t_{n} \rightarrow t, P(t_{n}) \rightarrow P(t)   (SOT);$

(c) for all but a countable number of points t, $P(t_n) \to P(t)   (SOT)   if   t_n \to t;$

(d) for $f \mathrm { i n } C ( \sigma ( A ) ) , f ( A ) = \int _ { - \infty } ^ { \infty } f ( t ) d P ( t ) ,$ where this integral is to be defined (by the reader) in the Riemann-Stieltjes sense.

11. If $\sigma _ { p } ( N )$ is a Borel set, show that $E ( \sigma ( N ) \backslash \sigma _ { p } ( N ) ) = 0$ if and only if N is diagonalizable; that is, there is a basis for $\mathcal { H }$ consisting of eigenvectors for N. If $\sigma _ { p } ( N )$ is not assumed to be a Borel set, is it still possible to characterize diagonalizable normal operators in a similar way? Give an example of a normal operator N such that $\sigma _ { p } ( N )$ is not a Borel set.

12. Show that if $N = U | N | \quad ( | N | = ( N ^ { * } N ) ^ { 1 / 2 } )$ is the polar decomposition of $N ,$ $U = \phi ( N )$ for some Borel function φ on $\sigma ( N )$ . Hence $U | N |   =   | N | U$ (see Exercise VIII.3.21).

13. Show that $N = W | N |$ for some unitary W that is a function of N.

14. Prove that if A is hermitian, exp(iA) is unitary. Is the converse true?

15. Show that there is a normal operator M such that $M ^ { 2 } = N$ and $M = \phi ( N )$ for some Borel function φ. How many such normal operators M are there?

16. Define $N \colon L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ by $(Nf)(t) = f(t + 1)$ .Show that N is normal and find its spectral decomposition. ((X.6.17) is useful here.)

17. Suppose that $N _ { 1 } , \ldots , N _ { d }$ are normal operators such that $\bar { N } _ { j } N _ { k } ^ { * } = N _ { k } ^ { * } N _ { j }$ for

$1 \leqslant j , k \leqslant d .$ Show that there is a subset X of $\mathbb { C } ^ { d }$ and a spectral measure E defined on the Borel subsets of X such that $N _ { k } = \int z _ { k }   d E ( z )$ for $1 \leqslant k \leqslant d \quad (z_k =$ the kth coordinate function) (see Exercise VIII.2.2).

18. If $N _ { 1 } , \ldots , N _ { d }$ are as in Exercise 17 and each is compact, show that there is a basis for  consisting of eigenvectors for each $N _ { k }$ . (This is the simultaneous diagonalization of $N _ { 1 } , \ldots , N _ { d } . )$

19. This exercise gives the properties of Hilbert-Schmidt operators (defined below). (a) If $\left\{ e _ { i } \right\}$ and $\{ f _ { j } \}$ are two orthonormal bases for $\mathcal { H }$ and $A   \in   \mathcal { B } ( \mathcal { H } )$ , then

$$
\sum _ { i } \| A e _ { i } \| ^ { 2 } = \sum _ { j } \| A f _ { j } \| ^ { 2 } = \sum _ { i } \sum _ { j } | \langle A e _ { i } , f _ { j } \rangle | ^ { 2 } .
$$

(b) If $A   \in   \mathcal { B } ( \mathcal { H } )$ and $\left\{ e _ { i } \right\}$ is a basis for $\mathcal { H }$ , define

$$
\| A \| _ { 2 } = \left[ \sum _ { i } \| A e _ { i } \| ^ { 2 } \right] ^ { 1 / 2 } .
$$

By $(a) \parallel \boldsymbol{A} \parallel_2$ is independent of the basis chosen and hence is well defined. If $\| A \| _ { 2 } < \infty ,$ A is called a Hilbert-Schmidt operator. $\mathcal { B } _ { 2 } = \mathcal { B } _ { 2 } ( \mathcal { H } )$ denotes the set of all Hilbert-Schmidt operators. (c) $\left\| \boldsymbol{A} \right\| \leqslant \left\| \boldsymbol{A} \right\|_2$ for every A in $\mathcal { B } ( \mathcal { H } )$ and $\left\| \cdot \right\| _ { 2 }$ is a norm on $\mathcal { B } _ { 2 }$ . (d) If $T \in \mathcal { B } = \mathcal { B } ( \mathcal { H } )$ and $A   \in   \mathcal { B } _ { 2 }$ , then $\| T A \| _ { 2 } \leqslant \| T \| \| A \| _ { 2 } ,$ $\| A ^ { \star } \| _ { 2 } = \| \overline { { A } } \| _ { 2 }$ , and $\| A T \| _ { 2 } \leqslant \| A \| _ { 2 } \| T \| . ( \mathrm { e } ) \mathcal { B } _ { 2 }$ is an ideal of  that contains $\mathcal { B } _ { \mathbf { 0 0 } }$ , the finite-rank operators. $(f) $A { \in } { \mathcal { B } } _ { 2 }$$ if and only $\mathrm{if} |A| \equiv (A^* A)^{1/2} \in \mathcal{B}_2$ in this case $\left\| A \right\|_2 = \left\| \left| A \right| \right\|_2 . \quad (g) \quad \mathcal{B}_2 \subseteq \mathcal{B}_0;$ moreover, if A is a compact operator and $\lambda _ { 1 } , \lambda _ { 2 } , \ldots$ are the eigenvalues of $| A | ,$ each repeated as often as its multiplicity, then $A   \in   \mathcal { B } _ { 2 } ( \mathcal { H } )$ iff $\sum_{n = 1}^{\infty} \lambda_{n}^{2} < \infty$ . In this case, $\| A \| _ { 2 } = ( \sum \lambda _ { n } ^ { 2 } ) ^ { 1 / 2 }$ . (h) If $( X , \Omega , \mu )$ is a measure space and ke $L ^ { 2 } ( \mu \times \mu ) ,$ , let $K \colon L ^ { 2 } ( \mu ) \to L ^ { 2 } ( \mu )$ be the integral operator with kernel k. Then $K { \in } { \mathcal { B } } _ { 2 } ( L ^ { 2 } ( \mu ) )$ and $\| K \| _ { 2 } = \| k \| _ { 2 }$ (see Proposition II.4.7 and Lemma II.4.8). (i) Interpret part (h) for a purely atomic measure space. More information on $\mathcal { B } _ { 2 }$ is contained in the next exercise.

20. This exercise discusses trace-class operators (defined below) and assumes a knowledge of Exercise 19. $\mathcal { B } _ { 1 } ( \mathcal { H } ) = \{ A B :$ A and $B   \in   \mathcal { B } _ { 2 } ( \mathcal { H } ) _ { \beta } ^ { 2 }$ . Operators belonging to $\mathcal { B } _ { 1 } ( \mathcal { H } )$ are called trace-class operators and $\mathcal { B } _ { 1 } ( \mathcal { H } ) = \mathcal { B } _ { 1 }$ is called the trace class. (a) If $A   \in   \mathcal { B } _ { 1 } ( \mathcal { H } )$ and $\left\{ e _ { i } \right\}$ is a basis, then $\textstyle \sum \lvert \langle A e _ { i } , e _ { i } \rangle \rvert < \infty$ . Moreover, the sum $\Sigma \langle A e _ { i } , e _ { i } \rangle$ is independent of the choice of basis. (Hint: If $A = C ^ { * } B ,   B ,   C$ in $\mathcal { B } _ { 2 }$ show that $| \langle A e _ { i } , e _ { i } \rangle | \equiv { \textstyle { \frac { 1 } { 2 } } } ( \| B e _ { i } \| ^ { 2 } + \| C e _ { i } \| ^ { 2 } ) .$ (b) If $\left\{ e _ { i } \right\}$ is a basis for $\mathcal { H } ,$ define tr: $\mathcal { B } _ { 1 }   \rightarrow   \mathbb { C }$ by

$$
\operatorname { t r } ( A ) = \sum _ { i } \langle A e _ { i } , e _ { i } \rangle .
$$

By (a) the definition of $\mathbf { t r } ( A )$ does not depend on the choice of a basis; $\mathbf { t r } ( A )$ is called the trace of A. If dim $\mathcal { H } < \infty$ , then $\mathbf { t r } ( A )$ is precisely the sum of the diagonal terms of any matrix representation of A. (c) If $A   \in   \mathcal { B } ( \mathcal { H } )$ , then the following are equivalent: (1) $A \in \mathcal{B}_{1}; (2) \left| A \right| = \left( A^{*}A \right)^{1/2} \in \mathcal{B}_{1}; (3) \left| A \right|^{1/2} \in \mathcal{B}_{2}; (4) \mathrm{tr}(|A|) < \infty$ . (d) If $A   \in   \mathcal { B } _ { 1 }$ and $T { \in } { \mathcal { B } } .$ then $A T$ and TA are in $\mathcal { B } _ { 1 }$ and $\mathrm{tr}(\boldsymbol{A}\boldsymbol{T}) = \mathrm{tr}(\boldsymbol{T}\boldsymbol{A})$ . Moreover, t $\mathbf { r } \colon \mathcal { B } _ { 1 }   \to   \mathbb { C }$ is a positive linear functional such that if $A   \in   \mathcal { B } _ { 1 } ,   A \geqslant 0 ,$ and $\operatorname { t r } ( A ) = 0$ then $A = 0 .$ (e) If $A   \in   \hat { \mathcal { B } } _ { 1 }$ , define $\| A \| _ { 1 } \equiv \operatorname { t r } ( | A | )$ . If $A   \in   \mathcal { B } _ { 1 }$ and $T { \in } { \mathcal { B } } .$ show that $| \operatorname { t r } ( T A ) | \leqslant \| T \|   \| A \| _ { 1 } . { \mathrm { ~ ( f ) ~ } }   \| A \| _ { 1 } = \| A ^ { \star } \|$ if $A   \in   \mathcal { B } _ { 1 } . ~ ( \mathsf { g } )$ If $T { \in } { \mathcal { B } }$ and $A   \in   \mathcal { B } _ { 1 }$ , then $\|   T A   \| _ { 1 } \leqslant \|   T   \|   \|   A   \| _ { 1 }$ and $\| A T \| _ { 1 } \leqslant \| T \| \| A \| _ { 1 } . ( \mathrm { h } ) \| \cdot \| _ { 1 }$ is a norm on $\mathcal { B } _ { 1 }$ . It is called the trace norm. (i) $\mathcal { B } _ { 1 }$ is an ideal in $\mathcal { B } ( \mathcal { H } )$ that contains $\mathcal { B } _ { 0 0 } . ~ ( \dot { \mathbf { j } } )$ If $A   \in   { \mathcal { B } } _ { 1 }$ and $\{ e _ { i } \}$ and $\{ f _ { i } \}$ are two bases for $\mathcal { H } .$ then $\begin{array} { r } { \sum _ { i } | \langle A e _ { i } , f _ { i } \rangle | \leqslant \| A \| _ { 1 } . \mathrm { ~ ( d ) ~ } \mathcal { B } _ { 1 } \subseteq \mathcal { B } _ { 0 } } \end{array}$ Also, if $A   \in   \mathcal { B } _ { 0 }$ and $\lambda _ { 1 } , \lambda _ { 2 } , \ldots$ are the eigenvalues of $| A | ,$ each repeated as often as its multiplicity, then $A   \in   \mathcal { B } _ { \mathrm { r } }$ if and only if $\sum _ { n = 1 } ^ { \infty } \lambda _ { n } < \infty$ . In this case, $\begin{array} { r } { \| \boldsymbol { A } \| _ { 1 } = \sum _ { n = 1 } ^ { \infty } \lambda _ { n } . } \end{array}$ (1) If A and $B   \in   \mathcal { B } _ { 2 }$ , define $(A,B)=\mathrm{tr}(B^{*}\hat{A})$ Then $( \cdot , \cdot )$ is an inner product on $\mathcal { B } _ { 2 }$ $\| \cdot \| _ { 2 }$ is the norm defined by this inner product, and $\mathcal { B } _ { 2 }$ is $\left\| \cdot \right\| _ { 2 }$ complete. In other words, $\mathcal { B } _ { 2 }$ is a Hilbert space. (m) $( \mathcal { B } _ { 1 } , \left\| \cdot \right\| _ { 1 } )$ is a Banach space. (n) $\mathcal { B } _ { 0 0 }$ is dense in both $\mathcal { B } _ { 1 }$ and $\mathcal { B } _ { 2 }$ . (For more on these matters, see Ringrose [1971] and Schatten [1960].)

21. This exercise assumes a knowledge of Exercise 20. If $g , h \in \mathcal { H }$ , let $\textstyle g \otimes h$ denote the rank-one operator defined by $( g \otimes h ) ( f ) = \langle f , h \rangle g .$ (a) If $g , h \in \mathcal { H }$ and $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ $\mathrm{tr}(A(g \otimes h)) = \langle A g, h \rangle$ . (b) If $T   \in   \mathcal { B } _ { 1 }$ , then $\| T \| _ { 1 } = \sup \left\{ \left| \operatorname { t r } ( C T ) \right| : C \in \mathcal { B } _ { 0 } , \| C \| \leqslant 1 \right\}$ (c) If $T { \in } { \mathcal { B } } _ { 1 }$ , define $L _ { T } \colon \mathcal { B } _ { 0 }   \to   \mathbb { C }$ by $L _ { T } ( C ) = \operatorname { t r } ( T C ) ( = \operatorname { t r } ( C T ) )$ . Show that the map $T   \mapsto   L _ { T }$ is an isometric isomorphism of $\mathcal { B } _ { 1 }$ onto $\mathcal { B } _ { 0 } ^ { * }$ . (d) If $B \in { \mathcal { B } }$ , define $F _ { B } : \mathcal { B } _ { 1 } \to \mathbb { C }$ by $F _ { B } ( T ) = \operatorname { t r } ( B T )$ .Show that $B   \mapsto   F _ { B }$ is an isometric isomorphism of  onto $\mathcal { B } _ { 1 } ^ { * }$ (e) If $L { \in } { \mathcal { B } } ^ { * }$ show that $L = L _ { 0 } + L _ { 1 }$ where $L _ { 0 } ,   L _ { 1 }   \in   \mathcal { B } ^ { * } ,   L _ { 1 } ( B )   =   \mathrm { t r } ( B T )$ for some T in $\mathcal { B } _ { 1 }$ , and $L _ { 0 } ( C ) = 0$ for every compact operator C. Show that $\| { \boldsymbol { L } } \| = \| { \boldsymbol { L } } _ { 0 } \| + \| { \boldsymbol { L } } _ { 1 } \|$ and that $L _ { 0 }$ and $L _ { 1 }$ are unique. Give necessary and sufficient conditions on $\mathcal { H }$ for $\mathcal { B } ( \mathcal { H } )$ to be a reflexive Banach space.

22. Prove that if U is any unitary operator on $\mathcal { H } ,$ then there is a continuous function u: $[ 0 , 1 ] \to { \mathcal { B } } ( { \mathcal { H } } )$ such that $u ( t )$ is unitary for all $t ,   u ( 0 ) = U ,$ and $u ( 1 ) = 1$

23. If N is normal, show that there is a sequence of invertible normal operators that converges to N.

## §3. Star-Cyclic Normal Operators

Recall the definition of a reducing subspace and some of its equivalent formulations (Section II.3).

3.1. Definition. A vector $e _ { 0 }$ in $\mathcal { H }$ is a star-cyclic vector for A if $\mathcal { H }$ is the smallest reducing subspace for A that contains $e _ { 0 } .$ The operator A is star cyclic if it has a star-cyclic vector. A vector $e _ { 0 }$ is cyclic for A if $\mathcal { H }$ is the smallest invariant subspace for A that contains $e _ { 0 } ; A$ is cyclic if it has a cyclic vector.

3.2. Proposition. (a) A vector $e _ { 0 }$ is a star-cyclic vector for A if and only if $\mathcal { H } = \operatorname { c l } \{ T e _ { 0 } \colon T \in C ^ { * } ( A ) \}$ , where $C ^ { * } ( A ) = t h e$ C\*-algebra generated by A. (b) A vector $e _ { 0 }$ is a cyclic vector for A if and only $if \mathcal{H} = \mathrm{cl} \left\{ p(A)e_0: p = a \right.$ polynomial}.

PROOF. Exercise.

Note that if $e _ { 0 }$ is a star-cyclic vector for A, then it is a cyclic vector for the algebra $C ^ { * } ( A )$

3.3. Proposition. If A has either a cyclic or a star-cyclic vector, then $\mathcal { H }$ is separable.

PROOF. It is easy to see that $C ^ { * } ( A )$ and $\{ p ( A ) : p = a$ polynomial} are separable subalgebras of $\mathcal { B } ( \mathcal { H } )$ . Now use (3.2). ■

Let $\mu$ be a compactly supported measure on C and let $N _ { \mu }$ be defined on $L ^ { 2 } ( \mu )$ as in Example 2.5. If $K = \mathbf { s u p p o r t }$ $\mu ,$ then $C ^ { * } ( N _ { u } ) = \{ M _ { u } : u \in C ( K ) \}$ Since $C ( K )$ is dense in $L ^ { 2 } ( \mu )$ , it follows that 1 is a star-cyclic vector for $N _ { \mu } .$ The converse of this is also true.

3.4. Theorem. A normal operator N is star-cyclic if and only if N is unitarily equivalent to $N _ { \mu }$ for some compactly supported measure µ on C. If $e _ { 0 }$ is a star-cyclic vector for N, then µ can be chosen such that there is an isomorphism $V \colon { \mathcal { H } }   \to   L ^ { 2 } ( \mu )$ with $V e _ { 0 } = 1$ and $V N V ^ { - 1 } = N _ { \mu ^ { \prime } }$ Under these conditions, V is unique.

PROOF. If $N \cong N _ { \mu } ,$ then we have already seen that N is star-cyclic. So suppose that N has a star-cyclic vector $e _ { 0 }$ . If E is the spectral measure for N, put $\mu ( \Delta ) = \| E ( \Delta ) e _ { 0 } \| ^ { 2 } = \langle E ( \Delta ) e _ { 0 } , e _ { 0 } \rangle$ for every Borel subset ∆ of C (see Lemma 1.9). Let K = support µ.

If $\phi   \in   B ( K )$ , then (2.4) implies

$$
\begin{align*}\| \phi(N) e_0 \|^2 &= \langle \phi(N) e_0, \phi(N) e_0 \rangle \\&= \langle |\phi|^2 (N) e_0, e_0 \rangle \\&= \int |\phi(z)|^2 d \langle E(z) e_0, e_0 \rangle \\&= \int |\phi|^2 d\mu.\end{align*}
$$

So if $B ( K )$ is considered as a submanifold of $L ^ { 2 } ( \mu ) , \; U \phi = \phi ( N ) e _ { 0 }$ defines an isometry from B(K) onto $\left\{ \phi ( N ) e _ { 0 } \colon \phi { \in } B ( K ) \right\}$ . But $e _ { 0 }$ is a star-cyclic vector, so the range of U is dense in $\mathcal { H }$ . Hence U extends to an isomorphism U: $L ^ { 2 } ( \mu )   \to   \mathcal { H }$

If φ∈B(K), then $U N _ { \mu } U ^ { - 1 } ( \phi ( N ) e _ { 0 } ) = U N _ { \mu } ( \phi ) = U ( z \phi ) = N \phi ( N ) e _ { 0 } .$ Hence $U N _ { \mu } U ^ { -   1 } = N$ on $\{ \phi ( N ) e _ { 0 } ^ { ' } : \phi \in B ( K ) \}$ , which is dense in H. So $U N _ { \mu } U ^ { -   1 } = N$ Let $\left[ V = U ^ { - 1 } \right.$

The proof of the uniqueness statement is an exercise.

Any theorem about the operators $N _ { \mu }$ is a theorem about star-cyclic normal operators. With this in mind, the next theorem gives a complete unitary invariant for star-cyclic normal operators. But first, a definition.

3.5. Definition. Two measures, $\mu _ { 1 }$ and $\mu _ { 2 } .$ , are mutually absolutely continuous if they have the same sets of measure zero; that is, $\mu _ { 1 } ( \Delta ) = 0$ if and ony if $\mu _ { 2 } ( \Delta ) = 0$ .This will be denoted by $[ \mu _ { 1 } ] = [ \mu _ { 2 } ]$ . (The more standard notation in the literature is $\mu _ { 1 } \equiv \mu _ { 2 } .$ , but this seems insufficient.) If $[ \mu _ { 1 } ] = [ \mu _ { 2 } ]$ , then the Radon-Nikodym derivatives $d \mu _ { 1 } / d \mu _ { 2 }$ and $d \mu _ { 2 } / d \mu _ { 1 }$ are well defined. Say that $\mu _ { 1 }$ and $\mu _ { 2 }$ are boundedly mutually absolutely continuous if $[ \mu _ { 1 } ] = [ \mu _ { 2 } ]$ and the Radon-Nikodym derivatives are essentially bounded functions.

## 3.6. Theorem. $N _ { \mu _ { 1 } } \cong N _ { \mu _ { 2 } }$ if and only $\begin{array} { r } { i f \left[ \mu _ { 1 } \right] = \left[ \mu _ { 2 } \right] . } \end{array}$

PrOOF. Suppose $[ \mu _ { 1 } ] = [ \mu _ { 2 } ]$ and put $\phi = d \mu _ { 1 } / d \mu _ { 2 }$ . So if $g \in L ^ { 1 } ( \mu _ { 1 } ) , g \phi \in L ^ { 1 } ( \mu _ { 2 } )$ and $\int g \phi d \mu _ { 2 } = \int g d \mu _ { 1 }$ . Hence, if $f \in L ^ { 2 } ( \mu _ { 1 } ) , \sqrt { \phi } f \in L ^ { 2 } ( \mu _ { 2 } )$ and $\| { \sqrt { \phi } } f \| _ { 2 } = \| f \| _ { 2 } ;$ that is, $U : L ^ { 2 } ( \mu _ { 1 } ) \to L ^ { 2 } ( \mu _ { 2 } )$ defined by $U f = { \sqrt { \phi } } f$ is an isometry. If $g   \in   L ^ { 2 } ( \mu _ { 2 } ) ,$ then $f = \phi ^ { - 1 / 2 } g \in L ^ { 2 } ( \mu _ { 1 } )$ and $U f = g ;$ hence U is surjective and $U ^ { - 1 } g = \phi ^ { - 1 / 2 } g$ for g in $L ^ { 2 } ( \mu _ { 2 } )$ . If $g   \in   L ^ { 2 } ( \mu _ { 2 } ) ,$ then $U N _ { \mu _ { 1 } } U ^ { - 1 } g = U N _ { \mu _ { 1 } } \phi ^ { - 1 / 2 } g = U z \phi ^ { - 1 / 2 } g = z g ,$ and so $U N _ { \mu _ { 1 } } U ^ { - 1 } = N _ { \mu _ { 2 } }$

Now assume that $V : \widetilde { L } ^ { 2 } ( \mu _ { 1 } ) \to L ^ { 2 } ( \mu _ { 2 } )$ is an isomorphism such that $V N _ { \mu _ { 1 } } V ^ { - 1 } =$ $N _ { \mu _ { 2 } }$ . Put $\psi = V ( 1 ) ; \mathrm { s o }   \psi   \in L ^ { 2 } ( \mu _ { 2 } )$ .For convenience, put $N _ { j } = N _ { \mu _ { j } } , j = 1 , 2$ It is easy to see that $V N _ { 1 } ^ { k } V ^ { - 1 } = N _ { 2 } ^ { k }$ and $V N _ { 1 } ^ { * k } V ^ { - 1 } = \bar { N _ { 2 } ^ { * k } }$ . Hence $\stackrel { \leftrightarrow } { V } p ( N _ { 1 } , N _ { 1 } ^ { * } ) V ^ { - 1 } =$ $p ( N _ { 2 } , N _ { 2 } ^ { * } )$ for any polynomial p in z and ž. Since $N _ { 1 } \cong N _ { 2 } , \; \sigma ( N _ { 1 } ) = \sigma ( N _ { 2 } ) ;$ hence support $\mu _ { 1 } = \mathtt { s u p p o }$ rt $\mu _ { 2 } = K$ . By taking uniform limits of polynomials in z and ž, $V u ( N _ { 1 } ) V ^ { - 1 } = u ( N _ { 2 } )$ for u in $C ( K )$ . Hence for u in $C ( K ) ,$ $V ( u ) = V u ( N _ { 1 } ) 1 = u ( N _ { 2 } ) V 1 = u \psi$ . Because V is an isometry, this implies that $\int | u | ^ { 2 } d \mu _ { 1 } = \int | u | ^ { 2 } | \psi | ^ { 2 } d \mu _ { 2 }$ for every u in $C ( K )$ . Hence $\int v d \mu _ { 1 } = \int v | \psi | ^ { 2 } d \mu _ { 2 }$ for v in $C ( K ) ,   v \geqslant 0 .$ By the uniqueness part of the Riesz Representation Theorem, $\mu _ { 1 } = | \psi | ^ { 2 } \mu _ { 2 } , \mathrm { s o } \mu _ { 1 } \ll \mu _ { 2 }$

By using $V ^ { - 1 }$ instead of V and reversing the roles of $N _ { 1 }$ and $N _ { 2 }$ in the preceding argument, it follows that $\mu _ { 2 } \ll \mu _ { 1 }$ . Hence $[ \mu _ { 1 } ] = [ \mu _ { 2 } ]$

## EXERCISES

1. If µ is a compactly supported measure on C and $f   \in   L ^ { 2 } ( \mu ) , f$ is a star-cyclic vector for $N _ { \mu }$ if and only if $\mu ( \{ x : f ( x ) = 0 \} ) = 0$

2. Prove Proposition 3.2.

3. If $\mu _ { 1 }$ and $\mu _ { 2 }$ are compactly supported measures on C, show that the following statements are equivalent: (a) $\mu _ { 1 }$ and $\mu _ { 2 }$ are boundedly mutually absolutely continuous; (b) there is an isomorphism V: $L ^ { 2 } ( \mu _ { 1 } ) \to L ^ { 2 } ( \mu _ { 2 } )$ such that $V N _ { \mu _ { 1 } } V ^ { - 1 } = N _ { \mu _ { 2 } }$ and $V L ^ { \infty } ( \mu _ { 1 } ) = L ^ { \infty } ( \mu _ { 2 } ) ;$ (c) there is a bounded bijection R: $L ^ { 2 } ( \mu _ { 1 } ) \rightarrow L ^ { 2 } ( \mu _ { 2 } )$ such that $R p ( z , \bar { z } ) = p ( z , \bar { z } )$ for every polynomial in z and ž.

4. Show that if N is a star-cyclic normal operator and $\lambda   \in   \sigma _ { p } ( N )$ then dim ker $( N - \lambda ) = 1$

5. If N is diagonalizable and star-cyclic and if $\sigma _ { p } ( N ) = \{ \lambda _ { 1 } , \lambda _ { 2 } , \ldots \}$ , show that N is unitarily equivalent to $N _ { \mu } ,$ where $\mu = \sum_{n = 1}^{\infty} 2^{-n} \delta_{\lambda_n}$ (see Exercise 2.11).

6. Let N be a diagonalizable normal operator. Show that $N \cong M$ if and only if M is a diagonalizable normal operator, $\sigma _ { p } ( N ) = \sigma _ { p } ( M )$ , and dim ker $( N - \lambda ) =$ dim ker $( M - \lambda )$ for all λ. (Compare this with Theorem II.8.3.)

7. Let U be the bilateral shift on $l ^ { 2 } ( \mathbb { Z } )$ . If $e _ { 0 }$ is the vector in $l ^ { 2 } ( \mathbb { Z } )$ that has 1 in the zeroth place and zeros elsewhere, then $e _ { 0 }$ is a star-cyclic vector for $U .   \mathrm { { H } }   \mu$ is the compactly supported measure on C and $V : l ^ { 2 } ( \mathbb { Z } ) \to L ^ { 2 } ( \mu )$ is the isomorphism such that $V e _ { 0 } = 1$ and $V U V ^ { - 1 } = N _ { \mu } ,$ then

(a) µ = m = normalized arc length on $\partial \mathbf { D } ;$

(b) V -1 = the Fourier transform on $L ^ { 2 } ( m ) = L ^ { 2 } ( \partial \mathbb { D } )$

8. Suppose $N _ { 1 } , \ldots , N _ { d }$ are normal operators such that $N _ { j } N _ { k } ^ { * } = N _ { k } ^ { * } N _ { j }$ for $1 \leqslant j ,   k \leqslant d$ and suppose there is a vector $e _ { 0 }$ in $\mathcal { H }$ such that $\mathcal { H }$ is the only subspace of $\mathcal { H }$ containing $e _ { 0 }$ that reduces each of the operators $N _ { 1 } { , \ldots , } N _ { d } { . }$ Show that there is a compactly supported measure $\mu$ on $\mathbf { C } ^ { d }$ and an isomorphism $V \colon { \mathcal { H } } \to L ^ { 2 } ( \mu )$ such that $V N _ { k } V ^ { - 1 } f = z _ { k } f$ for f in $L ^ { 2 } ( \mu )$ and $1 \leqslant k \leqslant d \left( z _ { k } = \right.$ the kth coordinate function) (see Exercise 2.17).

## §4. Some Applications of the Spectral Theorem

In this section a few diverse applications of the Spectral Theorem are presented. These will show the power and finesse of the Spectral Theorem as well as demonstrate some of the methods used to apply it. One result in this section (Theorem 4.6) is more than an application. Indeed, many regard this as the optimal statement of the Spectral Theorem.

If N is a normal operator and $N = \int z   d E ( z )$ is its spectral representation, then $\phi \mapsto \phi ( N ) \equiv \int \phi   d E$ is a \*-homomorphism of $B ( \pmb { \mathbb { C } } )$ into $\mathcal { B } ( \mathcal { H } )$ . Thus, if $\phi ,$ $\psi \in B ( \mathbb { C } ) ,   ( \int \phi   d E ) ( \int \psi   d E ) = \int \phi \psi   d E$ and $\| \int \phi d E \| \leq \sup \{ | \phi ( z ) | : z \in \sigma ( N ) \}$

4.1. Proposition. If N is a normal operator and $N = \int z   d E ( z ) ,$ , then N is compact if and only if for every $\varepsilon > 0 ,   E ( \left\{ z : | z | > \varepsilon \right\} )$ has finite rank.

PROOF. If $\varepsilon   >   0 ,$ let $\Delta _ { \varepsilon } = \left\{ z : | z | > \varepsilon \right\}$ and $E _ { \varepsilon } = E ( \Delta _ { \varepsilon } )$ Then

$$
\begin{align*}N - NE_{\varepsilon} &= \int zdE(z) - \int z\chi_{\Delta}(z)dE(z) \\&= \int z\chi_{\mathbb{C}\backslash\Delta_{\varepsilon}}(z)dE(z) = \phi(N)\end{align*}
$$

where $\phi ( z ) = z \chi _ { \mathbb { C } \setminus \Delta _ { \mathbb { C } } } ( z )$ . Thus $\| N - N E _ { \varepsilon } \| \leqslant \sup \{ | z | : z \in \mathbb { C } \backslash \Delta _ { \varepsilon } \} \leqslant \varepsilon .$ If $E _ { \varepsilon }$ has finite rank for every $\varepsilon > 0 ,$ then so does $N E _ { \varepsilon }$ Thus $N { \in } { \mathcal { B } } _ { 0 } ( { \mathcal { H } } )$

Now assume that N is compact and let $\varepsilon   >   0$ Put $\phi ( z ) = z ^ { - 1 } \chi _ { \Delta _ { i } } ( z ) ;$ sO $\phi   \in   B ( \mathbb { C } )$ . Since N is compact, so is $N \phi ( N )$ . But $N \phi ( N ) = \int z z ^ { - 1 } \chi _ { \Delta _ { \varepsilon } } ( z ) d E ( z ) = E _ { \varepsilon } .$ Since $E _ { \varepsilon }$ is a compact projection, it must have finite rank. (Why?)

The preceding result could have been proved by using the fact that compact normal operators are diagonalizable and the eigenvalues must converge to 0.

4.2. Theorem. If H is separable and I is an ideal of $\mathcal { B } ( \mathcal { H } )$ that contains a noncompact operator, then $I = \mathcal { B } ( \mathcal { H } )$

PROOF. $\mathrm { I f } \quad A   \in   I$ and $A   \notin   \mathcal { B } _ { 0 } ( \mathcal { H } )$ consider $A^{*}A;$ let $A^{*} A = \int t   dE(t)$ $( \sigma ( A ^ { * } A ) \subseteq [ 0 , \infty ) )$ . By the preceding proposition, there is an $\varepsilon   >   0$ such that

$P = E ( \varepsilon , \infty )$ has infinite rank. But $P = \left( \int t ^ { - 1 } \chi _ { ( \varepsilon , \infty ) } ( t ) d E ( t ) \right) A ^ { * } A \in I$ . Since $\mathcal { H }$ is separable, dim $P \mathcal { H } = \dim$ $\mathcal { H } = \aleph _ { 0 }$ Let $\dot{U}:\mathcal{H}\rightarrow P\mathcal{H}$ be a surjective isometry. It is easy to check that $\mathbf { l } = U ^ { * } P U$ . But $P { \in } I ,$ so $1   \in   { I }$ .Hence $I = \mathcal { B } ( \mathcal { H } )$ ■

In Proposition VIII.4.10, it was shown that every nonzero ideal of $\mathcal { B } ( \mathcal { H } )$ contains the finite-rank operators. When combined with the preceding result, this yields the following.

4.3. Corollary. $\mathit { 1 5 4 }$ is separable, then the only nontrivial closed ideal of $\mathcal { B } ( \mathcal { H } )$ is the ideal of compact operators.

The next proposition is related to Theorem VIII.5.9. Indeed, it is a consequence of it so that the proof will only be sketched.

Let N be a normal operator on $\mathcal { H }$ and for every vector $e$ in $\mathcal { H }$ let $\mathcal { H } _ { e } \equiv \vee \left\{ N ^ { * k } N ^ { j } e \colon k , j \geqslant 0 \right\}$ .So $\mathcal { H } _ { e }$ is the smallest subspace of $\mathcal { H }$ that contains e and reduces N. Also, $N | \mathcal { H } _ { e }$ is a star-cyclic normal operator.

4.4. Proposition. If N is a normal operator on $\mathcal { H } ,$ ,then there are reducing subspaces $\{ \mathcal { H } _ { i } : i { \in } I \}$ for N such that $\mathcal { H } = \oplus _ { i } \mathcal { H } _ { i }$ and $N | \mathcal { H } _ { i }$ is star cyclic.

ProoF. Using Zorn's Lemma find a maximal set of vectors $\mathcal { E }$ in $\mathcal { H }$ such that if $e ,   f   \in   \ell ^ { \ell }$ and $e \neq f ,$ then $\mathcal { H } _ { e } \bot \mathcal { H } _ { f }$ It follows that $\mathcal { H } = \oplus _ { e } \mathcal { H } _ { e } .$ ■

4.5. Corollary. Every normal operator is unitarily equivalent to the direct sum $o f$ star-cyclic normal operators.

By combining the preceding proposition with Theorem 3.4 on the representation of star-cyclic normal operators we can obtain the following theorem.

4.6. Theorem. If N is a normal operator on $\mathcal { H }$ , then there is a measure space $( X , \Omega , \mu )$ and a function φ in $L ^ { \infty } ( X , \Omega , \mu )$ such that N is unitarily equivalent to $M _ { \phi }$ on $L ^ { 2 } ( X , \Omega , \mu )$

PRooF. If M is a reducing subspace for N, then $N \cong N | \mathcal { M } \oplus N | \mathcal { M } ^ { \perp }$ ; thus $\sigma ( N | \mathcal { M } )   \subseteq   \sigma ( N )$ . So if $\left\{ N _ { i } \right\}$ is a collection of star-cyclic normal operators such that $N \cong \oplus _ { i } N _ { i } \left( 4 . 5 \right)$ , then $\sigma ( N _ { i } ) \in \sigma ( N )$ for every $N _ { i ^ { * } }$ By Theorem 3.4 there is a measure $\mu _ { i }$ supported on $\sigma ( N )$ such that $N _ { i } \cong N _ { \mu _ { i } }$ . Let $X _ { i }   =$ the support of $\mu _ { i }$ and let $\Omega _ { i } = \mathrm { t h e }$ Borel subsets of $X _ { i }$ Let X = the disjoint union of $\left\{ X _ { i } \right\}$ Define $\Omega$ to be the collection of all subsets ∆ of X such that $\Delta   \cap   X _ { i }   \in   \Omega _ { i }$ for all i. It is easy to check that Ω is a σ-algebra. If $\Delta { \in } \Omega$ let $\begin{array} { r } { \mu ( \Delta )   \equiv   \sum _ { i }   \mu _ { i } ( \Delta   \cap   X _ { i } ) ; } \end{array}$ then $( X , \Omega , \mu )$ is a measure space. If $f   \in   L ^ { 2 } ( X , \Omega , \mu )$ then $f _ { i } = f | X _ { i } \in L ^ { 2 } ( \mu _ { i } )$ Moreover, the map U: $L ^ { 2 } ( \mu )   \rightarrow   \oplus _ { i } L ^ { 2 } ( \mu _ { i } )$ defined by $U f = \oplus _ { i } ( f | X _ { i } )$ is easily seen to be an isomorphism. Define φ: $X   \to   \mathbb { C }$ by letting $\phi(z) = z   if   z \in X_i \in \mathbb{C};$ since $X _ { i } \subseteq \sigma ( N )$ for every $i , \phi$ is a bounded function. If G is an open subset of $\mathbf { C } ,$ $\phi ^ { - 1 } ( G ) \cap X _ { i } = G \cap X _ { i } \in \Omega _ { i } ;$ hence $\phi$ is Ω-measurable. Therefore $\phi { \in } L ^ { \infty } ( X , \Omega , \mu )$ It is left to the reader to check that $U M _ { \phi } U ^ { - 1 } = \oplus _ { i } N _ { \mu _ { i } } \cong N .$

4.7. Proposition. If $\mathcal { H }$ is separable, then the measure space in Theorem 4.6 is $\sigma \text {-} \mathit { f i n i t e } .$

PRoOF. First note that the measure space $( X , \Omega , \mu )$ constructed in the preceding theorem has no infinite atoms. Now let $\mathcal { E }$ be a collection of pairwise disjoint sets from Ω having non-zero finite measure. A computation shows that $\{ ( \mu ( \Delta ) ) ^ { - 1 / 2 } \chi _ { \Delta } : \Delta { \in } { \mathcal { E } } \}$ are pairwise orthogonal vectors in $L ^ { 2 } ( \mu )$ . If $L ^ { 2 } ( \mu )$ is separable, then $\mathcal { E }$ must be countable. Therefore $( X , \Omega , \mu )$ is σ-finite.

Of course if $( X , \Omega , \mu )$ is finite it is not necessarily true that $L ^ { 2 } ( \mu )$ is separable.

The next result will be useful later in this book and it also provides a different type of application of the Spectral Theorem.

4.8. Proposition. If A is an SOT closed $C ^ { * } .$ -subalgebra of $\mathcal { B } ( \mathcal { H } )$ , then $\varkappa$ is the norm closed linear span of the projections in $\varkappa$

PROOF. If $A { \in } { \mathcal { A } } , A + A ^ { * }$ and $A - A ^ { * } { \in } { \mathcal { A } } ;$ hence $\varkappa$ is the linear span of $R e . d .$ Suppose $A   \in   \mathrm { R e }   \mathcal { A }$ and $A = \int t   d E ( t )$ . If $[ a , b ] \subseteq \mathbb { R }$ , then there is a sequence $\{ u _ { n } \}$ in C(IR) such that $0 \leqslant u_{n} \leqslant 1,\; u_{n}(t) = 1$ for $a \leqslant t \leqslant b - n^{-1}, u_n(t) = 0$ for $t \leqslant a - n ^ { - 1 }$ and $t \geqslant b$ .Hence $u _ { n } ( t )   \rightarrow   \chi _ { [ a , b ) } ( t )$ as $n   \to   \infty$ . If $h \in \mathcal { H }$ , then

$$
\| \left\{ u _ { n } ( A ) - E [ a , b ) \right\} h \| ^ { 2 } = \int \left| u _ { n } ( t ) - \chi _ { [ a , b ) } ( t ) \right| ^ { 2 } d E _ { h , h } ( t ) \rightarrow 0
$$

by the Lebesgue Dominated Convergence Theorem. That is, $u_{n}(A) \to E[a,b)$ (SOT). Since $\rtimes$ is SOT-closed, $E[a,b) \in \mathcal{A}$ Now let $( \alpha , \beta )$ be an open interval containing $\sigma ( A )$ . If $\varepsilon   >   0 .$ , then there is a partition $\left\{ \alpha = t _ { 0 } < \cdots < t _ { n } = \beta \right\}$ such that $\begin{array} { r } { | t - \sum _ { k = 1 } ^ { n } t _ { k } \chi _ { [ t _ { k - 1 } , t _ { k } ) } ( t ) | < \varepsilon } \end{array}$ for t in $\sigma ( A ) ;$ hence $\begin{array} { r } { \| A - \sum _ { k = 1 } ^ { n } t _ { k } E [ t _ { k - 1 } , t _ { k } ) \| < \varepsilon . } \end{array}$ Thus every self-adjoint operator in $\varkappa$ belongs to the closed linear span of the projections in $\varkappa$

## EXERCISES

1. If N is a normal operator show that ran N is closed if and only if 0 is not a limit point of $\sigma ( N )$

2. Give an example of a non-normal operator A such that 0 is an isolated point of $\sigma ( A )$ and ran A is closed. Give an example of a non-normal operator B such that ran B is closed and 0 is not an isolated point of $\sigma ( B )$

3. If $\mathcal { H }$ is a nonseparable Hilbert space find an example of a nontrivial closed ideal $\mathcal { B } ( \mathcal { H } )$ that is different from $\mathcal { B } _ { 0 } ( \mathcal { H } )$

4. Let $( X , \Omega , \mu )$ be the measure space obtained in the proof of Theorem $4 . 6$ and show that $L ^ { 1 } ( X , \Omega , \mu ) ^ { * }$ is isometrically isomorphic to $L ^ { \infty } ( X , \Omega , \mu )$

5. Show that $\mathcal { H }$ is separable if and only if every collection of pairwise orthogonal projections in $\mathcal { B } ( \mathcal { H } )$ is countable.