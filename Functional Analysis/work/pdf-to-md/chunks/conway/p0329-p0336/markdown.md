So $B = A ^ { * } | \mathcal { D }$ is symmetric. Note that gra ${ \mathcal { A } } \perp \operatorname { g r a } ( A ^ { * } | { \mathcal { M } } )$ in $\mathcal { H } \oplus \mathcal { H }$ . Since both of these spaces are closed, gra B, given by (2.16), is closed.

Now let B be any closed symmetric extension of A. As discussed before, $A \subseteq B \subseteq A ^ { * }$ so gra $A \subseteq { \mathrm { g r a } }   B \subseteq { \mathrm { g r a } }   A ^ { * } = { \mathrm { g r a } }   A \oplus { \mathcal { H } } _ { + } \oplus { \mathcal { H } } _ { - }$ Let $\mathcal { G } =$ gra $B \cap ( \mathcal { H } _ { + } \oplus \mathcal { H } _ { - } )$ and let $\mathcal { M } = \mathrm { t h } \mathrm { e }$ set of first coordinates of elements in G. Clearly, M is a manifold in $\mathcal { L } _ { + } + \mathcal { L } _ { - }$ and M ⊆ dom B. Hence for $f , g$ in $\mathcal { M } , \langle A ^ { * } f , g \rangle = \langle B f , g \rangle = \langle f , B g \rangle = \langle f , A ^ { * } g \rangle$ . So M is A-symmetric. Clearly, gra $( A ^ { * } | \mathcal { M } ) = \mathcal { G }$ so M is A-closed. If h⊕ Bh∈gra B. let $h \oplus B h = ( f \oplus A f ) + k$ where f∈dom A and $k \in \mathcal { H } _ { + } \oplus \mathcal { H } _ { - }$ . Since $A \subseteq B , k \in$ gra B; so $k \in \mathcal { G }$ This shows that (2.16) holds

2.17. Theorem. Let A be a closed symmetric operator. If W is a partial isometry with initial space in ${ \mathcal { L } } .$ and final subspace in $\mathcal { L } _ { - }$ , let

$$
\mathcal { D } _ { W } = \left\{ f + g + W g : f \in \mathrm { d o m } A , g \in \mathrm { i n i t i a l } W \right\}\tag{2.18}
$$

and define $A _ { W }$ on $\mathcal { D } _ { W }$ by

$$
A _ { W } ( f + g + W g ) = A f + i g - i W g .\tag{2.19}
$$

Then $A _ { W }$ is a closed symmetric extension of A. Conversely, if B is any closed symmetric extension of A, then there is a unique partial isometry W such that $B = A _ { W }$ as in (2.19).

If W is such a partial isometry and W has finite rank, then

$$
n _ { \pm } ( A _ { W } ) = n _ { \pm } ( A ) - \dim ( \operatorname { r a n } W ) .
$$

ProoF. Let W be a partial isometry with initial space $I _ { + }$ in $\mathcal { L } _ { + }$ and final space $I _ { - }$ in $\mathcal { L } _ { - }$ . Define $\mathcal { D } _ { \boldsymbol { W } }$ and $A _ { W }$ as in (2.18) and (2.19). Let $\mathcal { M } = \{ g + W g :$ $g \in I _ { + } \} ; \mathrm { s o } \mathcal { M }$ is a manifold in $\mathcal { L } _ { + } + \mathcal { L } _ { - } . \mathrm { I f }   g , h \in I _ { + }$ , then $\langle W g , W h \rangle = \langle g , h \rangle$ Hence $\langle A ^ { * } ( g + W g ) , h + W h \rangle = \langle A ^ { * } g , h \rangle + \langle A ^ { * } g , W h \rangle + \langle A ^ { * } W g , h \rangle +$ $\langle A ^ { * } W g , W h \rangle$ . Since $g   \in   \ker ( A ^ { \star } - i )$ and $\mathbf { \mathit { W g } }   \in   \ker ( \mathbf { \mathit { A } } ^ { * } + i ) .$

$$
\begin{align*}\langle A^{\star}(g + Wg), h + Wh \rangle &= i\langle g, h \rangle + i\langle g, Wh \rangle - i\langle Wg, h \rangle - i\langle Wg, Wh \rangle \\&= i\langle g, Wh \rangle - i\langle Wg, h \rangle.\end{align*}
$$

Similarly, $\langle g + W g , A ^ { * } ( h + W h ) \rangle = i \langle g , W h \rangle - i \langle W g , h \rangle$ , so that M is A-symmetric. If $\{ g _ { n } \} \subseteq I _ { + } \mathrm { ~ a n d ~ } ( g _ { n } + W g _ { n } ) \oplus ( i g _ { n } - i W g _ { n } ) \to f \oplus h$ in $\mathcal { H } \oplus \mathcal { H }$ then $2 i g _ { n } = i ( g _ { n } + W g _ { n } ) + ( i g _ { n } - i W g _ { n } ) \rightarrow i f + h$ and $2 i W g _ { n } = i ( g _ { n } + W g _ { n } ) -$ $( i g _ { n } - i W g _ { n } ) \rightarrow i f - h . \mathrm { I f } g = ( 2 i ) ^ { - 1 } ( i f + h ) ,$ then $f   =   g + W g$ and $\begin{array} { r } { \pmb { h } = i \pmb { g } - i \pmb { W } \pmb { g } . } \end{array}$ Hence $\mathcal { M }$ is A-closed. By Lemma 2.15, $A _ { W }$ is a closed symmetric extension of A.

To prove that $n _ { + } ( A _ { W } ) = n _ { + } ( A ) - \dim I _ { + }$ , let f edom A, $g   \in   I _ { + }$ . Then

$$
\begin{align*}(A_{W} + i)(f + g + Wg) = & (A + i)f +ig - iWg +ig + iWg \\= & (A + i)f + 2ig.\end{align*}
$$

Thus ran $( A _ { W } + i ) = \mathrm { r a n } ( A + i ) \oplus I _ { + }$ , and so $n_{+}(A_{W}) = \dim \left[ \mathrm{ran}(A_{W} + i) \right]^{\perp} =$ dim $\left( \mathcal { L } _ { + } \ominus I _ { + } \right) = n _ { + } ( A ) - \dim I _ { + }$ . Similarly, $n_{-}(A_{W}) = n_{-}(A) - \dim I_{-} =$ $n_{-}(A) - \dim I_{+}$

Now let B be a closed symmetric extension of A. By Lemma 2.15 there is an A-symmetric, A-closed manifold $\mathcal { M }$ in $\mathcal { L } _ { + } + \mathcal { L } _ { - }$ such that gra $B = \mathrm{grad} A + \mathrm{grad} (A^*|\mathcal{M})$ If $f \in \mathcal { M } ,$ let $f = f ^ { + } + f ^ { - }$ , where $f ^ { \pm }   \in   \mathcal { L } _ { \pm }$ ; put $I _ { + } = \left\{ f ^ { + } \colon f { \in } { \mathcal { M } } \right\}$ . Since $\mathcal { M }$ is A-symmetric, $0 = \langle A ^ { * } f , f \rangle - \langle f , A ^ { * } f \rangle =$ $2 i \langle f ^ { + } , f ^ { + } \rangle - 2 i \langle f ^ { - } , f ^ { - } \rangle ;$ hence $\| f ^ { + } \| = \| f ^ { - } \|$ for all $f$ in M. So if $W f ^ { + } = f ^ { - }$ whenever $f = f ^ { + } + f ^ { - } \in \mathcal { M }$ and if $I _ { + }$ is closed, W is a partial isometry and (2.18) and $(2.19)$ are easily seen to hold. It remains to show that $I _ { + }$ is closed. Suppose $\{ f _ { n } \} \leq \mathcal { M }$ and $f _ { n } ^ { + }   \rightarrow   g ^ { + }$ in $\mathcal { L } _ { + }$ . Since $\| f _ { n } ^ { + } - f _ { m } ^ { + } \| =$ $\| f _ { n } ^ { - } - f _ { m } ^ { - } \|$ , there is a g− in $\mathcal { L } .$ such that $f _ { n } ^ { - }   \rightarrow   g ^ { - }$ . Clearly $f _ { n } \rightarrow g ^ { + } + g ^ { - } = g .$ Also, $A ^ { \stackrel { \leftrightarrow \righta} { \ast } } f _ { n } ^ { \pm } = \pm   i f _ { n } ^ { \pm } rrow \pm   i g ^ { \pm }$ . It follows that $g \oplus A^{*}g \in \mathrm{cl}  \mathrm{grad}(A^{*} \mid \mathcal{M}) =$ gra $( A ^ { * } | \mathcal { M } )$ ; thus $\boldsymbol { g } ^ { + }   \in   \boldsymbol { I } _ { + }$

2.20. Theorem. Let A be a closed symmetric operator with deficiency indices $n _ { \pm }$

(a) A is self-adjoint if and only if $n _ { + } = n _ { - } = 0 .$

(b) A has a self-adjoint extension if and only $\mathit { i f } \: n _ { + } = n _ { - }$ . In this case the set of self-adjoint extensions is in natural correspondence with the set of isomorphisms of $\mathcal { L } .$ + onto $\mathcal { L } _ { - }$

(c) A is a maximal symmetric operator that is not self-adjoint if and only if either $n _ { + } = 0$ and $n _ { - }   >   0$ or $n _ { + }   >   0$ and $n _ { - } = 0$

ProoF. Part (a) is a rephrasing of Corollary 2.9. For (b), $\pmb { n } _ { + } = \pmb { n } _ { - }$ if and only if $\mathcal { L } .$ and $\mathcal { L } _ { - }$ are isomorphic. But this is equivalent to stating that there is a partial isometry on $\mathcal { H }$ with initial and final spaces $\mathcal { L } _ { + }$ and ${ \mathcal { L } } _ { - } ,$ respectively. Part (c) follows easily from the preceding theorem.

2.21. Example. Let A and  be as in Example 1.11; so A is symmetric. The operator B of Example 1.12 is a self-adjoint extension of A. Let us determine all self-adjoint extensions of A. To do this it is necessary to determine $\mathcal { L } _ { \pm } .$ Now $f \in \mathcal { L } _ { \pm }$ if and only if $f { \in } \mathbf { d o m } \; A ^ { * }$ and $\pm \: i f = A ^ { * } f = i f ^ { \prime }$ , so $\mathcal { L } _ { \pm } = \{ \alpha e ^ { \pm x }$ $\alpha \in \mathbb { C } \}$ . Hence $n _ { \pm } = 1$ . Also, the isomorphisms of ${ \mathcal { L } } .$ onto $\mathcal { L } _ { - }$ are all of the form $W _ { \lambda } e ^ { x } = \lambda e ^ { - x }$ where $| \lambda | = e . \mathrm { I f } | \lambda | = e$ , let

$$
\mathcal { D } _ { \lambda } \equiv \{ f + \alpha e ^ { x } + \lambda \alpha e ^ { - x } : \alpha { \in } \mathbb { C } , f { \in } \mathcal { D } \} .
$$

$$
A _ { \lambda } ( f + \alpha e ^ { x } + \lambda \alpha e ^ { - x } ) = i f ^ { \prime } + \alpha i e ^ { x } - i \lambda \alpha e ^ { - x } ,
$$

if $f \in { \mathcal { D } } ,   { \pmb { \alpha } }   \in   { \pmb { \mathfrak { C } } } .$

According to Theorem 2.17, $\left\{ \left( A _ { \lambda } , \mathcal { D } _ { \lambda } \right) : \left| \lambda \right| = e \right\}$ are all of the self-adjoint extensions of A. The operator B of Example 1.12 is the extension $A _ { e }$

For more information on symmetric operators and the relation of the problem of finding self-adjoint extensions to physical problems, see Reed and Simon [1975] from which much of the present development is taken.

## EXERCISES

1. If A is symmetric, show that all of the eigenvalues of A are real.

2. If A is symmetric and $\lambda , \mu$ are distinct eigenvalues, show that ker $(A - \lambda) \perp \ker(A - \mu)$

3. Show that the closure of a symmetric operator is symmetric.

4. Let $\mathcal { D } = \{ f { \in } L ^ { 2 } ( 0 , \infty ) \}$ for every $c   >   0 , f$ is absolutely continuous on $[ 0 , c ] , f ( 0 ) = 0 ,$ and $f ^ { \prime }   \in   L ^ { 2 } ( 0 , \infty ) \}$ . Define $A f = i f ^ { \prime }$ for f in . Show that A is a densely defined closed operator and find dom $A ^ { * }$ Show that A is symmetric with deficiency indices $n _ { + } = 0$ and $n _ { - } = 1$

5. Let $\mathcal { S } = \{ f \in L ^ { 2 } ( - \infty , 0 ) :$ for every $c   <   0 ,$ f is absolutely continuous on $[ c , 0 ] ,$ $f ( 0 ) = 0 ,$ and $f ^ { \prime }   \in   L ^ { 2 } ( - \infty , 0 ) \}$ . Define $A f = i f ^ { \prime }$ for f in $\pmb { \mathscr { S } } .$ Show that A is a densely defined closed operator and find dom $A ^ { * }$ .Show that A is symmetric with deficiency indices $n _ { + } = 1 ,   n _ { - } = 0 .$

6. If k, l are any nonnegative integers or $\infty ,$ show that there is a closed symmetric operator A with $n _ { + } = k$ and $n _ { - } = l .$ (Hint: Use Exercises 4 and 5.)

7. Let $C _ { c } ^ { 2 } ( 0 , 1 )$ be all twice continuously differentiable functions on $( 0 , 1 )$ with compact support and let $A f = - f ^ { \prime \prime }$ for f in $C _ { c } ^ { 2 } ( 0 , 1 )$ . Show that the closure of A is a densely defined symmetric operator and determine all of its self-adjoint extensions.

8. If $A \in \mathcal { C } ( \mathcal { H } ) ,$ show that $A^{*}A$ is self-adjoint (see Exercise 1.11).

9. Say that an operator A is positive $\mathbf{if} \langle \mathbf{A} \mathbf{h}, \mathbf{h} \rangle \geqslant 0$ for all h in dom A. Prove that if A is positive and self-adjoint, then $\sigma ( A ) \in [ 0 , \infty )$ . If A is only assumed to be closed and positive, show that this conclusion may fail. (Hint: Look at the operator in Exercise 7.)

10. (Lasser [1972]) Let M be a dense linear manifold in $\mathcal { H }$ and let $\alpha$ consist of all linear transformations A such that dom $A = \mathcal { M } , \; A \mathcal { M } \subseteq \mathcal { M } ,$ the adjoint of A exists, $\mathcal { M } \subseteq \mathrm { d o m } A ^ { * } ,$ and $A ^ { * } \mathcal { M } \subseteq \mathcal { M }$ .Prove that $A \rightarrow A ^ { * } | \mathcal { M }$ defines an involution on $\varkappa$

## §3. The Cayley Transform

Consider the Möbius transformation

$$
M ( z ) = \frac { z - i } { z + i } .
$$

It is immediate that $M(0)=-1,\;M(1)=-i,$ and $M ( \infty ) = 1$ . Thus M maps the upper half plane onto D and $M ( \mathbb { R } \cup \infty ) = \partial \mathbb { D } .$ So if A is self-adjoint, $M ( A )$ should be unitary. Suppose A is symmetric; does $M ( A )$ make sense? What is $M ( A ) ?$

To answer these questions, we should first investigate the meaning of $M ( A )$ if A is symmetric. We want to define $M ( A )$ as $( A - i ) ( A + i ) ^ { - 1 }$ . As was seen in the last section, however, ran $( A + i )$ is not necessarily all of  if A is not self-adjoint. In fact, $( \operatorname { r a n } ( A + i ) ) ^ { \perp } = { \mathcal { L } }$ + and $( \operatorname { r a n } ( A - i ) ) ^ { \perp } = { \mathcal { L } } _ { - }$ , the deficiency spaces for A. However (2.5), if A is closed and symmetric, ran $( A \pm i )$ is closed. Also, realize that if $w = M ( z ) ,$ then $z = M ^ { - 1 } ( w ) = i ( 1 + w ) / ( 1 - w )$

3.1. Theorem. (a) If A is a closed densely defined symmetric operator with deficiency subspaces $\mathcal { L } _ { \pm }$ , and if $U \colon { \mathcal { H } } \to { \mathcal { H } }$ is defined by letting $U   =   0$ on ${ \mathcal { L } } .$ X and

$$
U   =   ( A - i ) ( A + i ) ^ { - 1 }
$$

on $\mathcal { L } _ { + } ^ { \perp }$ , then U is a partial isometry with initial space $\mathcal { L } _ { + } ^ { \perp }$ , final space $\mathcal { L } _ { - } ^ { \perp }$ and such that $( 1 - U ) ( \mathcal { L } _ { + } ^ { \perp } )$ is dense in $\mathcal { H }$

(b) If U is a partial isometry with initial and final spaces M and $\mathcal { N } ,$ respectively, and such that $( 1 - U ) \mathcal { M }$ is dense in $\mathcal { H } ,$ then

## 3.3

$$
A = i ( 1 + U ) ( 1 - U ) ^ { - 1 }
$$

is a densely defined closed symmetric operator with deficiency subspaces $\mathcal { L } _ { + } = \mathcal { M } ^ { \perp }$ and $\mathcal { L } _ { - } = \mathcal { N } ^ { \perp }$

(c) If A is given as in (a) and U is defined by (3.2), then A and U satisfy (3.3). If U is given as in (b) and A is defined by (3.3), then A and U satisfy (3.2).

PROOF. (a) By (2.5c), ran $( A \pm i )$ is closed and so $\mathcal { L } _ { \pm } ^ { \perp } = \mathrm { r a n } ( A \pm i )$ . By (2.5b), $\ker(A + i) = (0), \operatorname{so}(A + i)^{-1}$ is well defined on $\mathcal { L } _ { + } ^ { \perp }$ . Moreover, $(A + i)^{-1} \mathcal{L}_{+}^{\perp} \subseteq$ dom A so that U defined by (3.2) makes sense and gives a well-defined operator. If $h \in \mathcal { L } _ { + } ^ { \perp } ,$ then $\boldsymbol{h} = (A + i)f$ for a unique f in dom A. Hence $\| U h \| ^ { 2 } = \| ( A - i ) f \| ^ { 2 } = ( 2 . 5 \mathrm { a } ) \| A f \| ^ { 2 } + \| f \| ^ { 2 } = \| ( A + i ) f \| ^ { 2 } = \| h \| ^ { 2 }$ . Hence U is a partial isometry, (ker $U ) ^ { \perp } = \mathcal { L } _ { \pm } ^ { \perp } ,$ and ran $U = \mathcal { L } _ { - } ^ { \perp }$ . Once again, if f∈dom A and $\boldsymbol { h }   =   ( A + i ) f ,$ then $(1 - U)h = h - (A - i)f = (A + i)f -$ $(A - i)f = 2if. So (1 - U)\mathcal{L}_{+}^{\perp} =  dom A$ and is dense in $\mathcal { H } ,$

(b) Now assume that U is a partial isometry as in (b). It follows that ker $( 1 - U )   =   ( 0 )$ In fact, if $f   \in   \ker   ( 1 - U )$ , then $U f   =   f ;$ sO $\|   f \| = \|   U f \|$ and hence feinitial U. Since $U ^ { * } U$ is the projection onto initial U, $f = U ^ { \star } U f = U ^ { \star } f ;$ sO $f \in \ker(1 - U^*) = \operatorname{ran}(1 - U)^\perp \subseteq [(1 - U) \mathcal{M}]^\perp = (0)$ by hypothesis. Thus $f = 0$ and 1 - U is injective.

Let $\mathcal { D } = ( 1 - U ) \mathcal { M }$ and define $( 1 - U ) ^ { - 1 }$ on D. Because $1 - U$ is bounded, $\mathbf { g r a } ( 1 - U ) ^ { - 1 }$ is closed. If A is defined as in (3.3), it follows that A is a closed densely defined operator. $\operatorname { I f } f , g   \in   { \mathcal { D } }$ , let $f = ( 1 - U ) h$ and $g = ( 1 - U ) k , h , k \in \mathcal { M }$ Hence

$$
\begin{align*}\langle Af, g \rangle = &   i \langle (1 + U)h, (1 - U)k \rangle \\= &   i[\langle h, k \rangle + \langle Uh, k \rangle - \langle h, Uk \rangle - \langle Uh, Uk \rangle].\end{align*}
$$

Since $h , k \in \mathcal { M } , \langle U h , U k \rangle = \langle h , k \rangle ;$ hence $\langle A f , g \rangle = i [ \langle U h , k \rangle - \langle h , U k \rangle ]$ Similarly, $\langle f , A g \rangle = - i \langle ( 1 - U ) h , ( 1 + U ) k \rangle = - i [ \langle h , U k \rangle - \langle U h , k \rangle ] =$ $\langle A f , g \rangle$ . Hence A is symmetric.

Finally, if $h \in \mathcal { M }$ and $f   =   ( 1 - U ) h ,$ then $( A + i ) f = A f + i f = i ( 1 + U ) h +$ $i ( 1 - U ) h = 2 i h$ Thus ran $( A + i ) = \mathcal { M }$ Similarly, $( A - i ) f = i ( 1 + U ) h -$ $i ( 1 - U ) h = 2 U h ,$ , so that ran $(A - i) = \tan U = \mathcal{N}$

(c) Suppose A is as in (a) and U is defined as in (3.2). If $g { \in } ( 1 - U ) \mathcal { L } _ { + } ^ { \perp }$ put $g = ( 1 - U ) h ,$ where $h \in \mathcal{L}_{+}^{\perp} = \mathrm{ran}(A + i)$ .Hence $\boldsymbol { h } = ( A + i ) f$ for some f in dom A. Thus $g = h - U\dot{h} = (A + i)f - (A - i)f = 2if; \quad  so  \quad f = -\frac{1}{2}ig.$

Also,

$$
\begin{aligned} i(1 + U)(1 - U)^{-1}g &= i(1 + U)h \\&= i[h + Uh] \\&= i[(A + i)f + (A - i)f] \\&= 2iAf \\&= Ag.\\ \end{aligned}
$$

Therefore (3.3) holds.

The proof of the remainder of (c) is left to the reader.

3.4. Definition. If A is a densely defined closed symmetric operator, the partial isometry U defined by (3.2) is called the Cayley transform of A.

3.5. Corollary. If A is a self-adjoint operator and U is its Cayley transform, then U is a unitary operator with ker $( 1 - U )   =   ( 0 )$ . Conversely, if U is a unitary with $1 { \notin } \sigma _ { p } ( U )$ , then the operator A defined by (3.3) is self-adjoint.

PRooF. If A is a densely defined ·symmetric operator, then A is self-adjoint if and only if $\mathcal { L } _ { \pm }   =   ( 0 )$ . A partial isometry is a unitary operator if and only if its initial and final spaces are all of . This corollary is now seen to follow from Theorem 3.1.

One use of the Cayley transform is to study self-adjoint operators by using the theory of unitary operators. Indeed, the preceding results say that there is a bijective correspondence between self-adjoint operators and the set of unitary operators without 1 as an eigenvalue.

## EXERCISES

1. If U is a partial isometry, show that the following statements are equivalent: (a) ker $(1 - U) = (0);$ (b) ker $( 1 - U ^ { * } ) = ( 0 ) ;$ (c) $\operatorname { \mathsf { r a n } } ( 1 - U )$ is dense; (d) ran $( 1 - U ^ { * } )$ is dense.

2. Let U be a partial isometry with initial and final spaces M and N, respectively. Show that the following statements are equivalent: (a) (1 – U)M is dense; (b) $( 1 - U ^ { * } ) \mathcal { N }$ is dense; (c) ker $\left( U ^ { * } - U ^ { * } U \right) = ( 0 ) ;$ (d) ker(U − UU\*) = (0).

3. Find a partial isometry U such that ker(1 - U) = (0) but $(1 - U)(\ker U)^{\perp}$ is not dense.

4. If A is a densely defined closed symmetric operator and B and C are the operators defined in Exercises 1.11 and 1.12, then the Cayley transform of A is an extension of $( C - i B ) ( C + i B ) ^ { - 1 }$

5. Find the Cayley transform of the operator in Example 1.9 when each $\alpha _ { n }$ is real.

6. Find the Cayley transform of the operator in Example 1.10 when φ is real valued.

7. Let S be the unilateral shift of multiplicity 1 (see Exercise IX.6.4) and find the symmetric operator A such that S is the Cayley transform of A.

8. Let $U = S ^ { * }$ , where S is the unilateral shift of multiplicity 1. Is U the Cayley transform of a symmetric operator A? If so, find it.

## §4. Unbounded Normal Operators and the Spectral Theorem

If A is self-adjoint, the classical way to obtain the spectral decomposition of A is to let U be the Cayley transform of A, obtain the spectral decomposition of U, and then use the inverse Cayley transform to translate this back to a decomposition for A. There is a spectral theorem for unbounded normal operators, however, and the Cayley transform is not applicable here.

In this section the approach is to prove the spectral theorem for normal operators by using that theorem for the bounded case. The spectral theorem for self-adjoint operators is then only a special case.

4.1. Definition. A linear operator N on $\mathcal { H }$ is normal if N is closed, densely defined, and $N ^ { * } N = N N ^ { * }$

Note that the equation $N ^ { * } N = N N ^ { * }$ that appears in Definition 4.1 implicitly carries the condition that dom $N^{*}N = \mathrm{dom} NN^{*}$ . The operators in Examples 1.9 and 1.10 are normal and every self-adjoint operator is normal. Examining Example 1.9 it is easy to see that for a normal operator it is not necessarily the case that dom $N ^ { * } N = \mathrm { d o m } \; N .$

Parts of the next result have appeared in various exercises in this chapter, but a complete proof is given here.

## 4.2. Proposition. If $A \in \mathcal { C } ( \mathcal { H } ) ,$ then

(a) $1 + A ^ { * } A$ has a bounded inverse defined on all of $\mathcal { H }$

(b) $I f B = ( 1 + A ^ { * } A ) ^ { - 1 }$ , then $\| \pmb { B } \| \leqslant \mathbf { 1 }$ and $B \geqslant 0 .$

(c) The operator $C = A ( 1 + A ^ { * } A ) ^ { - 1 }$ is a contraction.

(d) $A ^ { * } A$ is self-adjoint.

(e) {h⊕ Ah: h∈dom $A ^ { * } A \}$ is dense in gra A.

PROOF. Define J: $\mathcal { H } \oplus \mathcal { H } \to \mathcal { H } \oplus \mathcal { H }$ by $J ( h \oplus k ) = ( - k ) \oplus h .$ By Lemma 1.7, gra $A^{*} = \left[ J \mathrm{grad} A \right]^{\perp}$ . So if $h \in \mathcal { H }$ , there are f in dom A and $g$ in dom $A ^ { * }$ such that 0⊕ $h = J(f \oplus A f) + g \oplus A^* g = (-A f) \oplus f + g \oplus A^* g$ Hence $0 = - A f + g ,$ or $g = A f ;$ also, $h = f + A^{*}g = f + A^{*}Af = (1 + A^{*}A)f.$ Thus ran $(1 + A^{*}A) = \mathcal{H}$

Also, for $f$ in dom $A ^ { * } A ,$ Af∈dom $A ^ { * }$ and $\| f + A ^ { * } A f \| ^ { 2 } = \| f \| ^ { 2 } +$ $2 \left\| A f \right\| ^ { 2 } + \left\| A ^ { * } A f \right\| ^ { 2 } \geqslant \left\| f \right\| ^ { 2 }$ .Hence $\ker(1 + A^{*}A) = (0)$ . Thus $( 1 + A ^ { * } A ) ^ { - 1 }$ exists and is defined on all of $\mathcal { H }$ . In the next paragraph (the proof of (b)) it will be shown that $( 1 + A ^ { * } A ) ^ { - 1 }$ is a contraction, completing the proof of (a).

It was shown that $\| ( 1 + A ^ { * } A ) f \| \geqslant \| f \|$ whenever f∈dom $A ^ { * } A$ . If $h   =   ( 1 + A ^ { * } A ) f$ and $B = (1 + A^{*}A)^{-1}$ , then this implies that $\| \boldsymbol{B} \boldsymbol{h} \| \leqslant \| \boldsymbol{h} \|$

Hence $\| B \| \leqslant 1$ . In addition, $\langle B h , h \rangle = \langle f , ( 1 + A ^ { * } A ) f \rangle = \| f \| ^ { 2 } + \| A f \| ^ { 2 } \geqslant 0 ,$ so (b) holds.

Put $C = A(1 + A^{*}A)^{-1} = AB;$ if f ∈dom $A ^ { * } A$ and $( 1 + A ^ { * } A ) f = h ,$ then $\| C h \| ^ { 2 } = \| A f \| ^ { 2 } \leqslant \| ( 1 + A ^ { * } A ) f \| ^ { 2 } = \| h \| ^ { 2 }$ by the argument used to prove (a). Hence $\| C \| \leqslant 1$ , so (c) is proved.

Now to prove (e). Since A is closed, it suffices to show that no nonzero vector in gra A is orthogonal to $\{ h \oplus A h \}$ h∈dom $A ^ { * } A \}$ . So let $g \in \mathbf { d o m }$ A and suppose that for every h in dom $A ^ { * } A$

$$
\begin{aligned} 0 &= \langle g \oplus A g, h \oplus A h \rangle \\&= \langle g, h \rangle + \langle A g, A h \rangle \\&= \langle g, h \rangle + \langle g, A^* A h \rangle \\&= \langle g, (1 + A^* A) h \rangle.\\ \end{aligned}
$$

So $g \perp \mathrm{ran}(1 + A^{*}A) = \mathcal{H}$ ; hence $g = 0 .$

To prove (d), note that (e) implies that dom $A ^ { * } A$ is dense. Now let f, g∈dom $A ^ { * } A ;$ SO $f , g \in \operatorname { d o m } A$ and $A f , A g \in \mathrm { d o m } A ^ { * }$ . Hence $\langle A ^ { * } A f , g \rangle =$ $\langle A f , A g \rangle = \langle f , A ^ { * } A g \rangle$ . Thus $A ^ { * } A$ is symmetric. Also, $1 + A ^ { * } A$ has a bounded inverse. This implies two things. First, $1 + A ^ { * } A$ is closed, and so $A ^ { * } A$ is closed. $\mathrm{A}\mathrm{l}\mathrm{s}\mathrm{o},-1\notin\sigma(A^{*}A)$ so that by Corollary $2 . 1 0 , A ^ { * } \bar { A }$ is self-adjoint.

4.3. Proposition. If N is a normal operator, then dom $N = \mathrm{dom} N^*$ and $\|   N f \| = \|   N ^ { * } f \|$ for every f in dom N.

PRooF. First observe that if h∈dom $N^{*}N = \mathrm{dom} NN^{*}$ , then Nh∈dom $N ^ { * }$ and $N ^ { * } h \epsilon$ dom N. Hence $\| N h \| ^ { 2 } = \langle N ^ { * } N h , h \rangle = \langle N N ^ { * } h , h \rangle = \| N ^ { * } h \| ^ { 2 }$ Now if f∈dom N, (4.2e) implies that there is a sequence $\{ h _ { n } \}$ in dom $N ^ { * } N$ such that $h _ { n } \oplus N h _ { n } \rightarrow f \oplus N f ; \mathrm { s o } \| N h _ { n } - N f \| \rightarrow 0$ But from the first part of this proof, $\|   N ^ { * } h _ { n } - N ^ { * } h _ { m } \| = \|   N h _ { n } - N h _ { m } \|$ . So there is a g in $\mathcal { H }$ such that $N ^ { * } h _ { n }   \rightarrow   g$ Thus $h _ { n }   \oplus N ^ { * } h _ { n }   \to f   \oplus g$ . But $N ^ { * }$ is closed; thus f ∈dom $N ^ { * }$ and $g = N ^ { * } f .$ So dom $N \subseteq \operatorname { d o m } N ^ { * }$ and $\| N f \| = \lim \| N h _ { n } \| = \lim \| N ^ { * } h _ { n } \| = \| N ^ { * } f \|$

On the other hand, $N ^ { * }$ is normal $( \mathbf { W h y } ? )$ , and so dom $N ^ { * } \subseteq$ dom $N ^ { * * } =$ dom N.

4.4. Lemma. Let $\mathcal { H } _ { 1 } , \mathcal { H } _ { 2 } , \ldots$ be Hilbert spaces and let $A _ { n } \in \mathcal { B } ( \mathcal { H } _ { n } )$ for all $n \geqslant 1$ $If \mathcal{D} = \left\{ (h_n) \in \oplus_n \mathcal{H}_n : \sum_{n=1}^{\infty} \| A_n h_n \|^2 < \infty \right\}$ and A is defined on $\mathcal { H } = \oplus _ { n } \mathcal { H } _ { n }$ by $A(h_n) = (A_n h_n)$ whenever $( h _ { n } ) \in \mathcal { D }$ , then $A \in \mathcal { C } ( \mathcal { H } )$ . A is a normal operator if and only if each $A _ { n }$ is normal.

PROOF. Since $\mathcal { H } _ { n } \subseteq \mathcal { D }$ for each $n , \mathcal { D }$ is dense in $\mathcal { H }$ Clearly A is linear. If $\{ h ^ { ( j ) } \} \subseteq$ dom A and $h ^ { ( j ) }   \oplus   A h ^ { ( j ) }   \to   h   \oplus   g$ in $\mathcal { H } \oplus \mathcal { H } ,$ then for each n, $\dot { h } _ { n } ^ { ( j ) } \oplus A _ { n } h _ { n } ^ { ( j ) } \to h _ { n } \oplus g _ { n }$ . Since $A _ { n }$ is bounded, $A _ { n } h _ { n } = g _ { n } .$ Hence $\begin{array} { r } { \sum _ { n } \| A \boldsymbol { h } _ { n } \| ^ { 2 } = } \end{array}$ $\sum \| g_n \|^2 = \| g \|^2 < \infty;$ so h∈dom A. Clearly $A h = g ,$ SO $A \in \mathcal { C } ( \mathcal { H } )$

It is left to the reader to show that dom $A^{*} = \left\{ (h_{n}) \in \mathcal{H} : \sum_{n = 1}^{\infty} \| A_{n}^{*} h_{n} \|^{2} < \infty \right\}$ and $A^{*}(h_{n}) = (A_{n}^{*}h_{n})$ when $(h_n) \in \mathrm{dom}$ $A ^ { * }$ . From this the rest of the lemma easily follows. ■

If (X, Ω) is a measurable space and $\mathcal { H }$ is a Hilbert space, recall the definition of a spectral measure E for $( X , \Omega , \mathcal { H } ) ~ ( \mathrm { I X } . 1 . 1 )$ . If $h , k   \in   \mathcal { H }$ , let $E _ { h , k }$ be the complex-valued measure given by $E _ { h , k } ( \Delta ) = \langle E ( \Delta ) h , k \rangle$ for each ∆ in Ω.

Let $\phi \colon X   \to   \mathbb { C }$ be an Ω-measurable function and for each n let $\Delta _ { n } = \{ x \in X$ $n - 1 \leqslant | \phi ( x ) | < n \}$ So $\chi _ { \Delta _ { n } } \phi$ is a bounded Ω-measurable function. Put $\mathcal { H } _ { n } = E ( \Delta _ { n } ) \mathcal { H }$ . Since $\bigcup_{n = 1}^{\infty} \Delta_{n} = X$ and the sets $\{ \Delta _ { n } \}$ are pairwise disjoint, $\oplus_{n = 1}^{\infty} \mathcal{H}_{n} = \mathcal{H}$ . If $E _ { n } ( \Delta ) = E ( \Delta \cap \Delta _ { n } )$ $E _ { n }$ is a spectral measure for $( X , \Omega , \mathcal { H } _ { n } )$ $\mathrm { A l s o } , \int   \phi   d E _ { n }$ is a normal operator on $\mathcal { H } _ { n }$ . Define

4.5

$$
\mathcal { D } _ { \phi } \equiv \left\{ h \in \mathcal { H } : \sum _ { n = 1 } ^ { \infty } \left\| \left( \int \phi d E _ { n } \right) E ( \Delta _ { n } ) h \right\| ^ { 2 } < \infty \right\} .
$$

By Lemma 4.4, $N _ { \phi } \colon \mathcal { H } \to \mathcal { H }$ given by

4.6

$$
N _ { \phi } h = \sum _ { n = 1 } ^ { \infty } \left( \int \phi d E _ { n } \right) E ( \Delta _ { n } ) h
$$

for h in $\mathcal { D } _ { \phi }$ is a normal operator. The operator $N _ { \phi }$ is also denoted by

$$
N _ { \phi } = \int \phi d E .
$$

4.7. Theorem. If E is a spectral measure for $( X , \Omega , \mathcal { H } ) , \quad \phi \colon X   \to   \pmb { \bar { \Omega } }$ is an Ω-measurable function, and $\mathcal { D } _ { \phi }$ and $N _ { \phi }$ are defined as in (4.5) and (4.6), then:

(a) $\mathcal { D } _ { \phi } = \{ h \in \mathcal { H } : \int | \phi | ^ { 2 } d E _ { h , h } < \infty \}$ 4

(b) for h in $\mathcal { D } _ { \phi }$ and f in $\mathcal { H } ,   \phi   \in   L ^ { 1 } ( | E _ { h , f } | )$ with

4.8

$$
\int | \phi | d | E _ { h , f } | \leqslant \| f \| \left( \int | \phi | ^ { 2 } d E _ { h , h } \right) ^ { 1 / 2 } ,
$$

4.9

$$
\left\langle \left( \int \phi   d E \right) h , f \right\rangle = \int \phi   d E _ { h , f } ,
$$

and

$$
\left\| \left( \int \phi   d E \right) h \right\| ^ { 2 } = \int \left| \phi \right| ^ { 2 } d E _ { h , h } .
$$

ProoF. Using the \*-homomorphic properties associated with a spectral measure (IX.1.12), one obtains

$$
\begin{align*}\left\| \left( \int \phi   dE_n \right) E(\Delta_n) h \right\|^2 &= \left\langle \left( \int \chi_{\Delta_n} \phi   dE \right)^* \left( \int \chi_{\Delta_n} \phi   dE \right) h, h \right\rangle \\&= \int_{\Delta_n} |\phi|^2 dE_{h,h}.\end{align*}
$$

From here, (a) is immediate.

Now let $h { \in } { \mathcal { D } } _ { \phi } , \; f { \in } { \mathcal { H } }$ . By the Radon-Nikodym Theorem, there is an Ω-measurable function u such that $| u | \equiv 1$ and $| E _ { h , f } | = u E _ { h , f }$ , where $| E _ { h , f } |$ is