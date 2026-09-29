3.5. Lemma. Let A: $\mathcal { H } \rightarrow \mathcal { H } ^ { \prime } , \mathcal { H } = \mathcal { M } \oplus \mathcal { N } , \mathcal { H } ^ { \prime } = \mathcal { M } ^ { \prime } \oplus \mathcal { N } ^ { \prime } ,$ , and suppose A has the matrix

$$
\begin{bmatrix} A_{1} & X \\ 0 & A_{2} \end{bmatrix}
$$

relative to these two decompositions of $\mathcal { H }$ and ${ \mathcal { H } } ^ { \prime } . ~ I f ~ A _ { 1 }$ is invertible and $\mathcal { N }$ and $\mathcal { N } ^ { \prime }$ are finite dimensional, then A is Fredholm and ind $A = \dim \mathcal{N} -$ dim $\mathcal { N } ^ { \prime }$

ProoF. It is easy to see that ran A is closed since ran $A _ { 1 } = \mathcal { M } ^ { \prime }$ and dim $\mathcal { N } < \infty$ Let's show that ker $A^{*} = \ker A_{2}^{*}$ and dim(ker A) = dim(ker $A _ { 2 } )$ . If this is done, then ind A = dim(ker A) – dim(ker A\*) = dim(ker $A _ { 2 } ) -$ dim(ker $A _ { 2 } ^ { * } )   =$ dim $\mathcal { N } - \dim \mathcal { N } ^ { \prime }$ by Proposition 3.2.

For the first of the two desired equalities, let $f ^ { \prime } \in \mathcal { M } ^ { \prime }$ and $g ^ { \prime } \in \mathcal { N } ^ { \prime }$ . Then $A ^ { * } ( f ^ { \prime }   \oplus   g ^ { \prime } )   =   A _ { 1 } ^ { * } f ^ { \prime }   \oplus   ( X ^ { * } f ^ { \prime } + A _ { 2 } ^ { * } g ^ { \prime } )$ So $f ^ { \prime } \oplus g ^ { \prime }$ eker $A ^ { * }$ if and only if $A _ { 1 } ^ { * } f ^ { \prime }   =   0$ and $A _ { 2 } ^ { * } g ^ { \prime } = -   \bar { X } ^ { * } f ^ { \prime }$ . But $\mathbf { A _ { 1 } }$ is invertible, so this happens exactly when $f ^ { \prime }   =   0 ,$ and hence $A _ { 2 } ^ { * } g ^ { \prime } = 0$ From here it is clear that ker $A ^ { * } = \ker A _ { 2 } ^ { * }$ . For the second equality, note that $g \to - A _ { 1 } ^ { - 1 } X g \oplus g$ is a bijection between ker $A _ { 2 }$ and ker $A .$

The second lemma is elementary and its proof is left to the reader.

3.6. Lemma. Let M and N be two closed subspaces of the Hilbert space $\mathcal { H }$

(a) If $\mathcal { M } \cap \mathcal { N } = ( 0 )$ and dim $\mathcal { N } = \infty$ , then dim $\mathcal { M } ^ { \perp } = \infty$

(b) If dim $\mathcal { M } ^ { \perp } = \infty$ and dim $\mathcal { N } < \infty$ , then dim $( \mathcal { M } + \mathcal { N } ) ^ { \perp } < \infty$

3.7. Theorem. $I f A : { \mathcal { H } } \to { \mathcal { H } } ^ { \prime }$ and B: $\mathcal { H } ^ { \prime } \rightarrow \mathcal { H } ^ { \prime \prime }$ are left semi-Fredholm operators, then BA is a left semi-Fredholm operator and ind $BA = \mathrm{ind} A + \mathrm{ind} B.$

ProoF. By definition, there are operators X and Y such that $X A = 1 + K$ and $Y B = 1 + K ^ { \prime }$ , where K and $K ^ { \prime }$ are compact operators on the appropriate spaces. Hence $(XY)(BA)=X(1+K')A=1+(K+XK'A)$ , and $K + X K ^ { \prime } A$ is compact. Therefore BA is left semi-Fredholm.

To prove the formula for the index, we consider 4 cases.

Case 1. Both A and B are Fredholm.

Let $\mathcal { M } ^ { \prime } \equiv ( \operatorname { r a n } A ) \cap ( \ker B ) ^ { \perp }$ and put $\mathcal { N } ^ { \prime } = \mathcal { M } ^ { \prime } { } ^ { \perp }$

Claim 1: $\mathcal { N } ^ { \prime }$ is finite dimensional.

To see this note that $\mathcal { N } ^ { \prime } = \mathcal { M } ^ { \prime } ^ { \perp } = ( \operatorname { r a n } A ) ^ { \perp } \vee ( \ker B ) .$ Since both of these spaces are finite dimensional, so is $\mathcal { N } ^ { \prime }$ Let $\mathcal { M } = A ^ { - 1 } ( \mathcal { M } ^ { \prime } ) \cap ( \ker A ) ^ { \perp } ;$ $\mathcal { N } = \mathcal { M } ^ { \perp } ; \mathcal { M } ^ { \prime \prime } = B \mathcal { M } ; \mathcal { N } ^ { \prime \prime } = \mathcal { M } ^ { \prime \prime } { } ^ { \perp }$ . Note the following: $A ( \mathcal { M } ) = \mathcal { M } ^ { \prime } ; A | \mathcal { M }$ is invertible (because ker $( A \vert \mathcal { M } ) =$ ker $A \cap \mathcal { M } = ( 0 ) ;   B | \mathcal { M } ^ { \prime }$ is invertible.

Claim 2: N is finite dimensional.

Indeed, let $A_{1} \equiv \mathbf{A} \left| (\ker A)^{\perp} \right|$ sO $A_{1}: (\ker A)^{\perp} \to \operatorname{ran} A$ is invertible. But $A _ { 1 } ^ { - 1 } ( \mathcal { M } ) = \mathcal { M } ,$ , so dim[(ker $A ) ^ { \perp } \cap \mathcal { M } ^ { \perp } ] = \dim [ ( \operatorname { r a n } A ) \cap \mathcal { M } ^ { \perp } ]$ , and this last dimension is finite since $\mathcal { N } ^ { \prime }$ is finite dimensional

Claim 3: $\mathcal { N } ^ { \prime \prime }$ is finite dimensional.

In fact, dim[(ker $B ) ^ { \perp } \cap \mathcal { M } ^ { \perp } ] < \infty$ and so dim $[ ( \tan B ) \cap \mathcal { M } ^ { \prime \prime } ] < \infty$ . This implies that dim $\mathcal { N } ^ { \prime \prime } < \infty$ . Now represent the operators as $2 \times 2$ matrices:

$$
A = \begin{bmatrix} A_{1} & X \\ 0 & A_{2} \end{bmatrix} : \begin{aligned} \mathcal{M} & \quad & \mathcal{M}' \\ \oplus & \quad \rightarrow \quad & \oplus \\ \mathcal{N} & \quad & \mathcal{N}' \end{aligned},
$$

$$
B = \left[ \begin{matrix} { B _ { 1 } } & { Y } \\ { 0 } & { B _ { 2 } } \\ \end{matrix} \right] : \begin{matrix} { \mathcal { M } ^ { \prime } } & { } & { \mathcal { M } ^ { \prime \prime } } \\ { \oplus } & { \rightarrow } & { \oplus } \\ { \mathcal { N } ^ { \prime } } & { } & { \mathcal { N } ^ { \prime \prime } } \\ \end{matrix} ,
$$

$$
\boldsymbol{B} \boldsymbol{A}=\left[\begin{matrix}\boldsymbol{B}_{1} \boldsymbol{A}_{1} & \boldsymbol{Z} \\0 & \boldsymbol{B}_{2} \boldsymbol{A}_{2}\end{matrix}\right]:\begin{aligned}\boldsymbol{\mathcal{M}} & \quad & \boldsymbol{\mathcal{M}}'' \\\boldsymbol{\Theta} & \rightarrow & \boldsymbol{\Theta} \\\boldsymbol{\mathcal{N}} & \quad & \boldsymbol{\mathcal{N}}''\end{aligned}.
$$

It follows that $B _ { 1 }$ and $A _ { 1 }$ are invertible. Since $\mathcal { N } , \mathcal { N } ^ { \prime } ,$ and $\mathcal { N } ^ { \prime \prime }$ are finite dimensional, the preceding lemma implies that ind $A = \dim \mathcal{N} - \dim \mathcal{N}'$ ind $B = \dim \mathcal{N}' - \dim \mathcal{N}''$ , and ind $BA = \dim \mathcal{N} - \dim \mathcal{N} = \operatorname{ind} A + \operatorname{ind} B.$

Case 2. Assume ind $B = - \infty$

This is equivalent to the assumption that $\dim(\tan B)^{\perp} = \infty$ . But ran $B \supseteq \tan B A$ and so dim $( \tan B A ) ^ { \perp } = \infty$ . Hence ind $BA = -\infty = \mathrm{ind} A +$ ind B.

Case 3. Assume B is invertible.

Without loss of generality we may assume that ind $A = - \infty$ since the alternative situation is covered in Case 1. If $\mathcal{M}=B(\tan A)=\tan BA$ and $\mathcal { N } = B ( [ \operatorname { r a n } A ) ^ { \perp } )$ , then the fact that B is invertible implies that $\mathcal { M } \cap \mathcal { N } = ( 0 )$ and $\mathcal { N } \mathrm { ~ i s ~ }$ infinite dimensional. Thus Lemma 3.6(a) implies that $\infty = \dim \mathcal{M}^{\perp} = \dim (\operatorname{ran} B A)^{\perp}$ and so ind $BA = -\infty = \mathrm{ind} A + \mathrm{ind} B.$

Case 4. B is a Fredholm operator.

Again, without loss of generality we may assume that ind $A = - \infty$ . It must be shown that ind $BA = -\infty$

Put $\mathcal{H}'_1 = (\ker B)^{\perp}$ and $\mathcal{H}_{1}^{\prime}=\tan B;$ define $B _ { 1 } \colon \mathcal { H } _ { 1 } ^ { \prime }   \to   \mathcal { H } _ { 1 } ^ { \prime \prime }$ as the restriction of B to $\mathcal { H } _ { 1 } ^ { \prime }$ . Clearly $B _ { 1 }$ is invertible. If P is the orthogonal projecton of $\mathcal { H }$ onto $\mathcal { H } _ { 1 ^ { \prime } } ^ { \prime }$ let $A _ { 1 } : \mathcal { H } \rightarrow \mathcal { H } _ { 1 } ^ { \prime }$ be defined by $A _ { 1 } = P A$ .Now both P and A are left semi-Fredholm, so $A _ { 1 }$ is left semi-Fredholm as was established at the opening of the proof.

Note that Lemma 3.6(b) implies that $\dim(\operatorname{ran}A+\ker B)^{\perp}=\infty$ . But (ran $A _ { 1 } ) ^ { \perp } =$ ker $A _ { 1 } ^ { * } = \ker A ^ { * } P = \ker B + ( \ker A ^ { * } ) \cap ( \ker B ) ^ { \perp } = \ker B + ( \operatorname { r a n } A + \operatorname { r a n } A ) ^ { \perp }$ ker $B ) ^ { \perp }$ and so ind $A _ { 1 } = - \infty$ . According to Case 3, ind $\pmb { B } _ { 1 } \pmb { A } _ { 1 } = - \infty$

This is equivalent to the condition that $\infty = \dim$ (ran $B_{1}A_{1})^{\perp} = \dim(\mathcal{H}_{1}^{\prime\prime} \cap$ [B(ran $A _ { 1 } ) ] ] ^ { \perp } )$ . But B(ran $A_{1}) = BP(\mathrm{ran} A) = B(\mathrm{ran} A) = \mathrm{ran} BA$ and so $\mathcal { H } _ { 1 } ^ { \prime \prime } \cap$ [B(ran $A_{1})^{\perp} \in (\mathrm{ran} BA)^{\perp}$ . Thus ind $BA = -\infty$

3.8. Corollary. If $A   \in   \mathcal { F } _ { r }$ and R is an invertible operator, then $R A R ^ { - 1 } \in \mathcal { F } _ { \ell }$ and ind $R A R ^ { - 1 } = \operatorname { i n d } A$

Before going further, let's look at some examples.

3.9. Example. Let S be the unilateral shift of multiplicity α. We saw in Example 2.2 that S is left semi-Fredholm. It is easy to calculate that ind $S = - \alpha .$ According to the preceding theorem, ind $\begin{array} { r } { \mathcal { S } ^ { 2 } = - 2 \alpha , } \end{array}$ But, of course, $S ^ { 2 }$ is the unilateral shift of multiplicity 2α.

3.10. Example. Let S be the unilateral shift of multiplicity α on the Hilbert space $\mathcal { H }$ and put $A = S \oplus S ^ { * }$ Note that ker $A = ( 0 ) \oplus$ ker $S ^ { * }$ and ran $A = ( \tan S ) \oplus \mathcal{H}$ .Thus A has closed range. The operator A, however, is semi-Fredholm if and only if $\alpha < \infty$ , in which case A is a Fredholm operator. Also when $\alpha < \infty$ , ind $A   =   0$

3.11. Theorem. If $A \colon { \mathcal { H } } \to { \mathcal { H } } ^ { \prime }$ is a left (respectively, right) semi-Fredholm operator and $K : { \mathcal { H } } \to { \mathcal { H } } ^ { \prime }$ is a compact operator, then $A + K$ is left (respectively, right) semi-Fredholm and ind $A = \mathrm{ind}(A + K)$

ProoF. Assume that A is a left semi-Fredholm operator. By definition there is an operator $X \colon { \mathcal { H } } ^ { \prime }   \to   { \mathcal { H } }$ and a compact operator $K _ { 0 } : \mathcal { H } \rightarrow \mathcal { H }$ such that $X A = 1 + K _ { 0 } .$ Thus $X(A + K) = 1 + (K_0 + XK)$ and so $A + K$ is left semi-Fredholm.

To verify that ind $A = \mathrm{ind}(A + K)$ , first assume that A is Fredholm. So there is a Fredholm operator X and a compact operator L such that $X A = 1 + L$ . But Theorem 3.7 implies that XA is Fredholm and, using Proposition 3.3, $0 = \mathrm{ind}(1 + L) = \mathrm{ind} A + \mathrm{ind} X;$ so ind $A = - \operatorname { i n d } X$ . But $X ( A + K ) = 1 + ( L + X K )$ and so the same type of reasoning implies that $\mathrm{ind}(A + K) = -\mathrm{ind} X = \mathrm{ind} A.$

Now assume that A is left semi-Fredholm; so $A + K$ is also left semi-Fredholm. If ind A is finite, then A is Fredholm and we are done by the preceding paragraph. If ind $A { \mathrm { ~ i s ~ } } { \mathrm { - ~ } } \infty$ , then ind $( A + K )$ must also be $- \infty$ for otherwise $A + K$ is Fredholm and it follows that $A = ( A + K ) - K$ is also Fredholm, a contradiction.

The preceding theorem says that the value of the index is impervious to compact perturbations. The next result, the third in the list of important properties of the Fredholm index, says that the value of the index is unchanged for all perturbations of the operator, provided that the size of the perturbation is sufficiently small.

3.12. Theorem. $If A: \mathcal{H} \rightarrow \mathcal{H}'$ is a Fredholm operator, then there is an $\varepsilon   >   0$ such that if $Y \in \mathcal{B}(\mathcal{H}, \mathcal{H}')$ and $\| Y \| < \varepsilon ,$ then $A + Y$ is Fredholm and ind $A = \mathrm{ind}(A + Y)$

ProoF. With respect to the decompositions $\mathcal{H} = (\ker A)^{\perp}$ ⊕ker A and $\mathcal{H}' = \mathrm{rank} A \oplus$ ker $A ^ { * }$ , the operator A has the matrix

$$
\begin{bmatrix} A_{1} & 0 \\ 0 & 0 \end{bmatrix}
$$

and $A_{1}:(\ker A)^{\perp}\to\operatorname{ran}A$ is invertible since A is Fredholm. Thus there is an $\varepsilon   >   0$ such that if $\| Y _ { 1 } \| < \varepsilon ,$ then $A _ { 1 } + Y _ { 1 }$ is invertible. If Y: $\mathcal { H } \rightarrow \mathcal { H } ^ { \prime }$ and $Y \| < \varepsilon ,$ then, with respect to the same decomposition of $\mathcal { H }$

$$
Y = \begin{bmatrix} Y_{1} & Y_{2} \\ Y_{3} & Y_{4} \end{bmatrix}
$$

and so

$$
A + Y = \begin{bmatrix} A_{1} + Y_{1} & Y_{2} \\ Y_{3} & Y_{4} \end{bmatrix} = \begin{bmatrix} A_{1} + Y_{1} & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & Y_{2} \\ Y_{3} & Y_{4} \end{bmatrix},
$$

where the first matrix represents a Fredholm operator and the second represents a finite rank operator. Therefore ind $( A + Y )$ is the index of the first matrix. But since $A _ { 1 } + Y _ { 1 }$ is invertible, Lemma 3.5 implies that this index is equal to dim(ker A) − dim(ker A\*) = ind A.

3.13. Corollary. If $\mathcal { S } \mathcal { F }$ is given the norm topology and $\mathbb { Z } \cup \{ \pm \infty \}$ is given the discrete topology, then the Fredholm index is a continuous function from $\mathcal { I F }$ into $\mathbb { Z } \cup \{ \pm \infty \}$

This continuity statement has an equivalent formulation. Because $\mathcal { S } \mathcal { F }$ is an open subset of $\mathcal { B } ( \mathcal { H } )$ , its components are open sets. Thus the continuity of the index is equivalent to the statement that it is constant on the components of $\mathcal { I F }$

For a treatment of the Fredholm index applicable to unbounded operators on a Banach space, see Kato [1966], pp. 229–244. For other approaches to Fredholm theory, with variations and generalizations of the material in this book, see Caradus, Pfaffenberger, and Yood [1974] and Harte [1982].

## EXERCISES

1. Prove Lemma 3.6.

2. If $A   \in   \mathcal { B } ( \mathcal { H } )$ and ran A is closed, show that ran $A ^ { ( \infty ) }$ is closed. If $A   \in   \mathcal { S P }$ and ker $A = ( 0 )$ , show that $A ^ { ( \infty ) } { \in } { \mathcal { P F } }$ and ind $A ^ { ( \infty ) }   =   - \infty$ or 0.

3. Does the unilateral shift of multiplicity 1 have a square root?

4. Show that for every n in $\mathbb { Z } \cup \{ \pm \infty \}$ there is an operator A in $\mathcal { I F }$ such that ind $A = n .$

5. If $A   \in   \mathcal { S } \mathcal { F }$ , then for every $n \geqslant 1,   A^n \in \mathcal{S} \mathcal{F}$ and ind $A^{n} = n(\bmod A)$

6. If $A : \mathcal { H } \rightarrow \mathcal { H } ^ { \prime }$ is a left semi-Fredholm operator, then there is a finite rank operator $F : { \mathcal { H } } \to { \mathcal { H } } ^ { \prime }$ such that ker $(A + F) = (0)$ and $\mathrm{ind}(A + F) = \mathrm{ind} A.$

7. If A is a Fredholm operator in $\mathcal { B } ( \mathcal { H } )$ , prove that the following statements are equivalent. (a) ind $A   =   0 .$ (b) There is a compact operator K such that $A + K$ is invertible. (c) There is a finite rank operator F such that $A + F$ is invertible.

8. If U is the unilateral shift of multiplicity 1 and π: $\mathcal { B } ( \mathcal { H } ) \rightarrow \mathcal { B } ( \mathcal { H } ) / \mathcal { B } _ { 0 } ( \mathcal { H } )$ is the natural map, show that $\pi ( U )$ is normal in $\mathcal { B } ( \mathcal { H } ) / \mathcal { B } _ { 0 } ( \mathcal { H } )$ but there is no normal operator N such that $U - N$ is compact. (See Exercise IX.8.14.)

## §4. The Essential Spectrum

Now concentrate on operators acting on a single Hilbert space and let $\mathcal { H }$ π: $\mathcal { B } \rightarrow \mathcal { B } / \mathcal { B } _ { 0 }$ be the natural map from $\mathcal { B } ( \mathcal { H } )$ into the Calkin algebra. Since the Calkin algebra is a Banach algebra with identity, the next definition makes sense.

4.1. Definition. If $A \in \mathcal { B } ( \mathcal { H } ) ,$ , the essential spectrum of $A , \sigma _ { e } ( A )$ , is the spectrum of $\pi ( A )$ in $\mathcal { B } / \mathcal { B } _ { 0 } ;$ that is, $\sigma _ { e } ( A ) = \sigma ( \pi ( A ) )$ . Similarly the left and right essential spectrum of A are defined by $\sigma _ { \ell e } ( A ) = \sigma _ { \ell } ( \pi ( A ) )$ and $\sigma _ { r e } ( A ) = \sigma _ { r } ( \pi ( A ) )$ respectively.

The proof of the next proposition is a straightforward application of the general properties of the various spectra in an arbitrary Banach algebra.

4.2. Proposition. Let $A \in \mathcal { B } ( \mathcal { H } )$

(a) $\sigma _ { e } ( A ) = \sigma _ { \ell e } ( A ) \cup \sigma _ { r e } ( A ) .$

(b) $\sigma _ { \ell e } ( A ) = \sigma _ { r e } ( A ^ { * } ) ^ { * } .$

(c) $\sigma _ { \ell e } ( A ) \subseteq \sigma _ { \ell } ( A ) ,   \sigma _ { r e } ( A ) \subseteq \sigma _ { r } ( A ) ,$ and $\sigma _ { e } ( A ) \subseteq \sigma ( A )$

(d) $\sigma _ { \ell e } ( A ) ,   \sigma _ { r e } ( A )$ , and $\sigma _ { e } ( A )$ are compact sets.

(e) If K is a compact operator, $\sigma _ { \ell e } ( A + K ) = \sigma _ { \ell e } ( A ) , \sigma _ { r e } ( A + K ) = \sigma _ { r e } ( A ) .$ , and $\sigma _ { e } ( A + K ) = \sigma _ { e } ( A ) .$

Our understanding of semi-Fredholm operators gained in the preceding sections can now be applied to better understand the essential spectrum. Indeed, $\sigma _ { \zeta e } ( A ) = \{ \lambda \in \mathbb { C } : A - \lambda \notin \mathcal { F } _ { \zeta } \}$ . Thus an application of Theorem 2.3 gives us the following.

## 4.3. Proposition. Let $A   \in   \mathcal { B } ( \mathcal { H } )$

(a) $\lambda { \in } \sigma _ { l e } ( A )$ if and only if dim ker $( A - \lambda ) = \infty$ or $\operatorname { r a n } ( A - \lambda )$ is not closed.

(b) $\lambda   \in   \sigma _ { r e } ( A )$ if and only if dim[ran $(A - \lambda)]^{\perp} = \infty$ or ran(A — λ) is not closed.

The reader should compare Proposition 4.3 and Proposition 1.1.

4.4. Proposition. $If A \in \mathcal{B}(\mathcal{H})$ then $\sigma _ { a p } ( A ) = \sigma _ { l e } ( A ) \cup \{ \lambda \in \sigma _ { p } ( A ) \}$ dim ker $( A - \lambda )$ $< \infty \}$

PROOF. $\mathbf { I f }   \lambda   \in   \sigma _ { a p } ( A )$ , then (1.1) either ran $( A - \lambda )$ is not closed or ker $( A - \lambda ) \neq 0$ If ran $( A - \lambda )$ is not closed or if dim ker $( A - \lambda ) = \infty$ , then $\lambda   \in   \sigma _ { l e } ( A )$ by (4.3). The proof of other inclusion is left to the reader. ■

4.5. Proposition. If N is a normal operator and $\lambda   \in   \sigma ( N ) ,$ , then ran $( N - \lambda )$ is closed if and only if λ is not a limit point of $\sigma ( N )$

PRooF. Assume λ is an isolated point of $\sigma ( N ) ;$ thus $X = \sigma(N) \backslash \{\lambda\}$ is a closed subset of $\sigma ( N ) .$ If $N = \int z   d E ( z )$ and $\mathcal{H}_{1} = E(X)\mathcal{H}$ then $\mathcal { H } _ { 1 }$ reduces N and $\sigma ( N | \mathcal { H } _ { 1 } ) = X$ . Hence $( N - \lambda ) \mathcal { H } _ { 1 }$ is closed. Since $\mathcal { H } _ { 1 } ^ { \perp } = \ker ( N - \lambda ) ,$ ran $(N - \lambda) = (N - \lambda)\mathcal{H}_1$ ; hence $N - \lambda$ has closed range.

Now assume that $\lambda   \in   \sigma ( N )$ but λ is not an isolated point. Then there is a strictly decreasing sequence $\{ r _ { n } \}$ of positive real numbers such that $r _ { n }   \to   0$ and such that each open annulus $A _ { n } = \left\{ z : r _ { n + 1 } < | z - \lambda | < r _ { n } \right\}$ has non-empty intersection with $\sigma ( N )$ Thus $E(A_n) \mathcal{H} \neq (0);$ let $e _ { n }$ be a unit vector in $E(A_{n})\mathcal{H}$ Then $e _ { n } \perp \ker ( N - \lambda ) ( = E ( \{ \lambda \} ) \mathcal { H } )$ and

$$
\| (N - \lambda)e_n \|^2 = \int_{A_n} |z - \lambda|^2   dE_{e_n, e_n}(z) \leqslant r_n^2 \to 0.
$$

That is, inf $\left\{ \left\| (N - \lambda)h \right\| : \left\| h \right\| = 1,   h \perp \ker(N - \lambda) \right\} = 0$ and so, by the Open Mapping Theorem, $N - \lambda$ does not have closed range.

4.6. Proposition. If N is a normal operator, then $\sigma _ { e } ( N ) = \sigma _ { l e } ( N ) = \sigma _ { r e } ( N )$ and $\sigma ( N ) \backslash \sigma _ { e } ( N ) = \{ \lambda \in \sigma ( N ) : \lambda$ is an isolated point of $\sigma ( N )$ that is an eigenvalue of finite multiplicity}

ProoF. The first part follows by applying Proposition 1.3 to the Calkin algebra. If λ is an isolated point of $\sigma ( N )$ , then ran $( N - \lambda )$ is closed by the preceding proposition. So if dim ker $( N - \lambda ) < \infty$ $\lambda \notin \sigma _ { l e } ( N ) = \sigma _ { e } ( N )$ by Proposition 4.3. Conversely, if $\lambda \in \sigma ( N ) \backslash \sigma _ { e } ( N )$ , then ran $( N - \lambda )$ is closed and dim ker $( N - \lambda ) < \infty$ . By the preceding proposition, λ is an isolated point of $\sigma ( N )$

4.7. Example. Let G be a bounded region in C and, to avoid pathologies, assume $\partial G = \partial [ \operatorname { c l } G ]$ . Let $\mathcal { H } = L _ { a } ^ { 2 } ( G )$ (I.1.10) and define $S : \mathcal { H } \rightarrow \mathcal { H }$ by $( \mathrm { S } f ) ( z ) = z f ( z ) .$ Then $\sigma ( S ) = \mathrm { c l } \; G , \quad \sigma _ { e } ( S ) = \sigma _ { l e } ( S ) = \sigma _ { r e } ( S ) = \partial G = \sigma _ { a p } ( S ) ,$ $\sigma _ { p } ( S ) = \Box$ , and for λ in G, ran $( S - \lambda )$ is closed and dim $\left[ \operatorname { r a n } ( S - \lambda ) \right] ^ { \perp } = 1$ Thus ind $( S - \lambda ) = - 1$ for λ in G.

To show that these statements are true, begin by proving:

$$
\mathrm { I f } \lambda \in G , \quad \mathrm { r a n } ( S - \lambda ) = \{ f \in L _ { a } ^ { 2 } ( G ) : f ( \lambda ) = 0 \} .
$$

In fact, if $h { \in } L _ { a } ^ { 2 } ( G )$ , then $[ ( S - \lambda ) h ] ( z ) = ( z - \lambda ) h ( z )$ so that $f = (z - \lambda)h$ vanishes at λ. Conversely, suppose $f   \in   L _ { a } ^ { 2 } ( G )$ and $f(\lambda) = 0;$ then $f(z) = (z - \lambda)h(z)$ for some analytic function h on G. It must be shown that $h   \in   L _ { a } ^ { 2 } ( G )$ . Let $r   >   0$ such that $D = \left\{ z : | z - \lambda | \leqslant r \right\} \subseteq G$ . Then

$$
\int \lvert h \rvert ^ { 2 } = \int \int _ { D } \lvert h \rvert ^ { 2 } + \int \int _ { G \setminus D } \lvert h \rvert ^ { 2 } .
$$

Now $\iint_{D} |h|^2 < \infty$ since h is bounded on D. For z in $G \backslash D, \left| h(z) \right| = \left| f(z) \right| / \left| z - \lambda \right| \leqslant$ $r ^ { - 1 } | \tilde { f } ( z ) |$ . Hence

$$
\iint _ { G \backslash D } | h | ^ { 2 } \leqslant r ^ { - 2 } \iint _ { G } | f | ^ { 2 } < \infty.
$$

Thus $h { \in } L _ { a } ^ { 2 } ( G )$ and $f   =   ( \mathcal { S } - \lambda ) \pmb { h }$ This proves (4.8).

Using Corollary $I.1.12,   f \mapsto f(\lambda)$ is a bounded linear functional on $L _ { a } ^ { 2 } ( G )$ whenever $\lambda \in G .$ By (4.8), ran $( S - \lambda )$ is the kernel of this linear functional and hence is closed.

Because G is bounded, the constant functions belong to $L _ { a } ^ { 2 } ( G )$ So if $f { \in } L _ { a } ^ { 2 } ( G ) , \quad f = [ f - f ( \lambda ) ] + f ( \lambda )$ and $f - f(\lambda) \in \mathrm{ran}(S - \lambda)$ Thus $L _ { a } ^ { 2 } ( G )   =$ ran $( S - \lambda ) + \mathbb { C } .$ Therefore dim[ran $\left[ \left( S - \lambda \right) \right] ^ { \perp } = \dim \left[ L _ { a } ^ { 2 } \left( G \right) / \operatorname { r a n } \left( S - \hat { \lambda } \right) \right] = 1$ when $\lambda \in G .$

If $\lambda \in G$ , then $S - \lambda$ is not surjective; hence $G \subseteq \sigma ( S )$ . If λ∉cl G, then $( z - \lambda ) ^ { - 1 }$ is a bounded analytic function on G. If $A f = ( z - \lambda ) ^ { - 1 } f ,$ then A is a bounded operator on $L _ { a } ^ { 2 } ( G )$ and it is easy to check that $A(S - \lambda) = (S - \lambda)A = 1$ . Thus $\sigma ( S ) \subseteq \operatorname { c l } G$ Combining these two containments, we get $\sigma ( S ) = \operatorname { c l } G .$

From Corollary 2.4 we have that $S - \lambda$ is a Fredholm operator whenever $\lambda \in G ;$ thus $G \cap \sigma _ { e } ( S ) = \square$ . So $\sigma _ { e } ( S ) \subseteq \partial G = \partial [ \operatorname { c l } G ]$ . If $\lambda { \in } \partial G ,$ then $\lambda   \in   \partial \sigma ( S ) ;$ thus $\lambda { \in } \sigma _ { a p } ( S ) ( 1 . 2 )$ . Since ker $( S - \lambda ) = ( 0 )$ $\operatorname { \mathsf { r a n } } ( S - \lambda )$ is not closed. Thus $\partial G \subseteq \sigma _ { l e } ( S ) \cap \sigma _ { r e } ( S )$ . This proves that $\sigma _ { e } ( S ) = \sigma _ { l e } ( S ) = \sigma _ { r e } ( S ) = \partial G = \sigma _ { a p } ( S )$

One of the primary uses of Fredholm theory is the examination of the values of ind $( A - \lambda )$ for all λ for which this makes sense. Such an examination often leads to structural information about the operator A. Note that ind $( A - \lambda )$ is defined when $\lambda \notin \sigma _ { l e } ( A ) \cap \sigma _ { r e } ( A )$

4.9. Proposition. If $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ , then ind $( A - \lambda )$ is constant on the components of $\mathbf{C} \backslash \sigma_{le}(A) \cap \sigma_{re}(A)$ . If λ is a boundary point of $\sigma ( A )$ and $\lambda \notin \sigma _ { l e } ( A ) \cap \sigma _ { r e } ( A )$ then ind $(A - \lambda) = 0$

PROOF. The map $\lambda { \mapsto } A - \lambda$ is a continuous map of $\mathbf{C} \backslash \sigma_{le}(A) \cap \sigma_{re}(A)$ into $\mathcal { I F }$ . So the first part of the proposition follows from Corollary 3.13. If λ is a boundary point of $\sigma ( A )$ and $\lambda \notin \sigma _ { l e } ( A ) \cap \sigma _ { r e } ( A )$ , then there is a sequence $\{ \lambda _ { n } \}$ in $\mathbf { C } \backslash \sigma ( A )$ such that $\lambda _ { n } \rightarrow \lambda$ . Thus ind $(A - \lambda_n) \to \mathrm{ind}(A - \lambda)$ . Since ind $( A - \lambda _ { n } ) = 0$ for all n, the result follows. ■

Here is the remaining spectral information about an old friend.

4.10. Example. Let S be the unilateral shift on $l ^ { 2 }$ Then $\sigma _ { l e } ( S ) = \sigma _ { r e } ( S ) = \partial \mathbf { D }$ and ind $(S - \lambda) = -1   for   |\lambda| < 1$

In Proposition $\mathrm { V I I . 6 . 5 }$ it was shown that σ(S) = cl D, $\sigma _ { p } ( S ) = \square$ , and $\sigma _ { a p } ( S ) = \partial \mathbf { D } .$ Thus for $| \lambda | = 1$ $\mathtt { r a n } ( S - \lambda )$ is not closed and hence $\partial \mathbf { D } \subseteq$ $\sigma _ { l e } ( S ) \cap \sigma _ { r e } ( S )$ . Also, if $| \lambda | < 1$ , it was shown that ran $( S - \lambda )$ is closed and dim $\left[ \operatorname { r a n } ( S - \lambda ) \right] ^ { \perp } = 1$ This implies that $\partial \mathbf { D } = \sigma _ { l e } ( S ) = \sigma _ { r e } ( S )$ and ind $( S - \lambda ) = - 1$ for λ in D.

Using this information about the shift and Proposition 3.4(c) we can get complete information about another operator. (Also see Example 3.10.)

4.11. Example. Let S be the unilateral shift of multiplicity 1 and put $A = S \oplus S ^ { * }$ It follows that $\sigma _ { l e } ( A ) = \sigma _ { r e } ( A ) = \partial \mathbb { D } , \quad \sigma ( A ) = \mathrm { c l }   \mathbb { D } ,$ and ind $( A - \lambda ) = 0$ for $| \lambda | < 1$

## EXERCISES

1. Show that the material of this section is only significant for infinite dimensional Hilbert spaces by showing that the essential spectrum of every operator on $\mathcal { H }$ is non-empty if and only if  is infinite dimensional.

2. Let G be a bounded region in C such that $\partial G = \partial [ \operatorname { c l } G ]$ and let φ be a function that is analytic in a neighborhood of cl G. Define A: $L _ { a } ^ { 2 } ( G ) \to L _ { a } ^ { 2 } ( G )$ by $A f = \phi f .$ Find all of the parts of the spectrum of A.

3. (Fillmore, Stampfli, and Williams [1972].) If $\lambda   \in   \sigma _ { l e } ( A )$ , then there is a projection P, having infinite rank, such that $\pi ( A - \lambda ) \pi ( P ) = 0.$

4. (Fillmore, Stampfli, and Williams [1972].) Let $A   \in   \mathcal { B } ( \mathcal { H } )$ . (a) If A has a cyclic vector e, show that dim $\{ A e , A ^ { 2 } e , \ldots \} ^ { \perp } \leqslant 1$ . (b) Let $\lambda { \in } \sigma _ { l e } ( A ^ { * } )$ . If $\varepsilon   >   0 ,$ let $f _ { 1 } , f _ { 2 }$ be orthonormal vectors such that $\| ( A ^ { \star } - \lambda ) f _ { j } \| < \varepsilon$ for $j   =   1 , 2$ and let $P =$ the projection onto $\vee \left\{ f _ { 1 } , f _ { 2 } \right\}$ . Put $B = \bar{\lambda} P + (1 - P)A$ . Show that $\| \boldsymbol{B} - \boldsymbol{A} \| < 2\varepsilon.$ (c) Show that the noncyclic operators are dense in $\mathcal { B } ( \mathcal { H } )$ if dim $\mathcal { H } > 1$

5. Let $A   \in   \mathcal { F }$ and suppose f is analytic in a neighborhood of $\sigma ( A )$ and does not vanish on $\sigma _ { e } ( A )$ . Show that $f(A) \in \mathcal{F}$ and find ind $f ( A )$

6. Let S be the unilateral shift and let f be an analytic function in a neighborhood of cl D such that $f(z) \neq 0   if   |z| = 1$ . Let $\gamma(t) = f(\exp(2\pi it)), \; 0 \leqslant t \leqslant 1$ . Show that $\sigma _ { e } ( f ( S ) ) = f ( \partial \mathbf { D } ) = \{ \gamma ( t ) : 0 \leq t \leq 1 \}$ and that if $\lambda \notin f ( \partial \mathbf { D } ) ,$ ind $( f ( S ) - \lambda ) = - n ( \gamma ; \lambda ) ,$ where $n ( \gamma ; \lambda ) =$ the winding number of γ about λ. Moreover, show that if ind $( f ( S ) - \lambda ) = 0 ,$ then $\lambda \notin \sigma(f(S))$

7. Let S be the operator defined in Example 2.11 where $G = \mathbf { D } ,$ Show that there is a compact operator K such that $S + K$ is unitarily equivalent to the unilateral shift.