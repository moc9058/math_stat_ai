6. If $\mathbf { f } \left( X , \Omega , \mu \right)$ is a measure space, then $( X , \Omega , \mu )$ is σ-finite or $L ^ { 2 } ( \mu )$ is finite dimensional if and only if every collection of pairwise orthogonal projections in $\{ M _ { \phi } { \in } L ^ { \infty } ( \mu ) \}$ is countable.

7. If $N = \int z   d E ( z )$ and $\varepsilon   >   0 .$ , show that ran $E ( \{ z : | z | > \varepsilon \} ) \subseteq \operatorname { r a n } N$

8. (Calkin [1939]) Let M be a linear manifold in $\mathcal { H }$ and show that $\mathcal { M }$ has the property that M contains no closed infinite dimensional subspaces if and only if whenever $A \in \mathcal { B } ( \mathcal { H } )$ and ran $A \subseteq { \mathcal { M } }$ , then A is compact.

9. Show that the extreme points of $\{ A \in \mathcal{B}(\mathcal{H}); 0 \leq A \leq 1 \}$ are the projections.

10. (Halmos [1972]) If N is a normal operator, show that there is a hermitian operator A and a continuous function f such that $N = f ( A )$ . (Hint: Use Theorem 4.6.)

## §5. Topologies on $\mathcal { B } ( \mathcal { H } )$

In this section some results on the SOT and WOT on $\mathcal { B } ( \mathcal { H } )$ are presented. These results are necessary for understanding some of the results that are to follow in later sections and also for a proper comprehension of a number of other subjects in mathematics.

The first result appeared as Exercise 1.4.

5.1. Proposition. If $L : \mathcal { B } ( \mathcal { H } ) \rightarrow \mathbb { C }$ is a linear functional, then the following statements are equivalent.

(a) L is SOT continuous.

(b) L is WOT continuous.

(c) There are vectors $g _ { 1 } , \ldots , g _ { n } , h _ { 1 } , \ldots , h _ { n }$ in H such that $L(A)=\sum_{k = 1}^{n}\langle Ag_{k},h_{k}\rangle$ for every A in $\mathcal { B } ( \mathcal { H } ) .$

PRooF. Clearly (c) implies (b) and (b) implies (a). So assume (a). By (IV.3.1f) there are vectors $g _ { 1 } , \ldots , g _ { n }$ in $\mathcal { H }$ such that

$$
\left| L ( A ) \right| \leqslant \sum _ { k = 1 } ^ { n } \left\| A g _ { k } \right\| \leqslant \sqrt { n } \left[ \sum _ { k = 1 } ^ { n } \left\| A g _ { k } \right\| ^ { 2 } \right] ^ { 1 / 2 }
$$

for every A in $\mathcal { B } ( \mathcal { H } )$ . Replacing $g _ { k }$ by $\sqrt { n } g _ { k } ,$ it may be assumed that

$$
| L ( A ) | \leqslant \left[ \sum _ { k = 1 } ^ { n } \| A g _ { k } \| ^ { 2 } \right] ^ { 1 / 2 } \equiv p ( A ) .
$$

Now p is a seminorm and $p(A)=0$ implies $L ( A ) = 0 .$ Let $\mathcal { H } = \mathrm { c l } \left\{ A g _ { 1 } \oplus A g _ { 2 } \right\}$ $\oplus \cdots \oplus \overline{A} g_n \colon A \in \mathcal{B}(\mathcal{H})$ ; so ${ \mathcal { H } } \subseteq { \mathcal { H } } \oplus \cdots \oplus { \mathcal { H } }$ (n times). Note that if $A g _ { 1 } \oplus \cdots \oplus A g _ { n } = 0 , p ( A ) = 0 ,$ and hence, $L ( A ) = 0 .$ Thus $F ( A g _ { 1 } \oplus \cdots \oplus A g _ { n } ) =$ $L ( A )$ is a well-defined linear functional on a dense manifold in $\varkappa$ But

$$
| F ( A g _ { 1 } \oplus \cdots \oplus A g _ { n } ) | \leqslant p ( A ) = \| A g _ { 1 } \oplus \cdots \oplus A g _ { n } \|.
$$

So F can be extended to a bounded linear functional $F _ { 1 }$ on $\mathcal { H } ^ { ( n ) }$ .Hence there are vectors $h _ { 1 } , \ldots , h _ { n }$ in $\mathcal { H }$ such that

$$
\begin{align*}\boldsymbol{F}_{1}(f_{1} \oplus \cdots \oplus f_{n}) &= \langle f_{1} \oplus \cdots \oplus f_{n}, h_{1} \oplus \cdots \oplus h_{n} \rangle \\&= \sum_{k=1}^{n} \langle f_{k}, h_{k} \rangle.\end{align*}
$$

In particular, $L(A) = F(Ag_1 \oplus \cdots \oplus Ag_n) = \sum_{k=1}^{n} \langle Ag_k, h_k \rangle.$

5.2. Corollary. $\mathit { I f } \mathcal { C }$ is a convex subset of $\mathcal { B } ( \mathcal { H } )$ , the WOT closure of $\mathcal { C }$ equals the SOT closure $o f \mathcal { C } .$

ProoF. Combine the preceding proposition with Corollary V.1.4.

When discussing the closure (WOT or SOT) of a convex set it is usually better to discuss the SOT. Shortly an “algebraic" characterization of the SOT closure of a subalgebra of $\mathcal { B } ( \mathcal { H } )$ will be given. But first recall (VIII.5.3) that if $1 \leqslant n \leqslant \infty, \mathcal{H}^{(n)}$ denotes the direct sum of $\mathcal { H }$ with itself n times $\mathbf { \otimes _ { 0 } }$ times if $n = \infty )$ . If $A \in \mathcal{B}(\mathcal{H}), A^{(n)}$ is the operator on $\mathcal { H } ^ { ( n ) }$ defined by $A^{(n)}(h_1,\ldots,h_n)=(Ah_1,\ldots,Ah_n). \mathrm{If} \mathcal{S} \subset \mathcal{B}(\mathcal{H}), \mathcal{S}^{(n)} \equiv \{A^{(n)}; A \in \mathcal{S}\}$ . It is rather interesting that the SOT closure of an algebra can be characterized using its lattice of invariant subspaces.

5.3. Proposition. $\mathit { I f } \: \mathcal { A }$ is a subalgebra of $\mathcal { B } ( \mathcal { H } )$ containing 1, then the SOT closure of A is

$$
\{ B   \in   \mathcal { B } ( \mathcal { H } ) \colon f o r e v e r y f i n i t e n , \mathrm { L a t } \mathcal { A } ^ { ( n ) } \subseteq \mathrm { L a t } B ^ { ( n ) } \} .
$$

ProoF. It is left as an exercise for the reader to show that if $B { \in } \mathrm { S O T - c l . } { \mathcal { A } } ,$ B belongs to the set (5.4). Now assume that B belongs to the set (5.4). Fix $f _ { 1 } , f _ { 2 } , \ldots , f _ { n }$ in $\mathcal { H }$ and $\varepsilon   >   0$ It must be shown that there is an A in $\alpha$ such that $\| ( A - B ) f _ { k } \| < \varepsilon$ for $1 \leqslant k \leqslant n$

Let $\mathcal { M } = \vee \left\{ ( A f _ { 1 } , \ldots , A f _ { n } ) : A \in \mathcal { A } \right\}$ . Because $\varkappa$ is an algebra, $\mathcal { M }   \in   \mathrm { L a t }   \mathcal { A } ^ { ( n ) } ,$ hence $\mathcal { M } \in \mathrm { L a t } B ^ { ( n ) }$ . Because $1 \in \mathcal { A } , ( f _ { 1 } , \ldots , f _ { n } ) \in \mathcal { M }$ .Since $\{ ( A f _ { 1 } , \ldots , A f _ { n } ) ; A \in { \mathcal { A } } \}$ is a dense manifold and $( B f _ { 1 } , \ldots , B f _ { n } ) \in \mathcal { M } ,$ there is an A in $\varkappa$ with $\varepsilon^{2}>\sum_{k = 1}^{n}\left\| (A - B)f_{k} \right\|^{2}$ ; hence $B \in \mathrm { S O T } - \mathrm { c l } \; { \mathcal { A } } .$ ■

## 5.5. Proposition. The closed unit ball of $\mathcal { B } ( \mathcal { H } )$ is WOT compact.

ProoF. The proof of this proposition follows along the lines of the proof of Alaoglu's Theorem. For each h in ball $\mathcal { H }$ let $X _ { h } = a \exp y$ of ball $\mathcal { H }$ with the weak topology. Put $\overline{X} = \Pi \left\{ X_{h} : \| h \| \leqslant 1 \right\}$ . If A∈ball $\mathcal { B } ( \mathcal { H } )$ let $\tau ( A )   \in   X$ defined by $\tau ( A ) _ { h } = A h$ Give X the product topology. Then t: (ball $\mathcal { B } ( \mathcal { H } ) ,$ $\mathbf { W O T } )   \rightarrow   \mathbf { X }$ is a continuous function and a homeomorphism onto its image (verify). Now show that τ(ball $\mathcal { B } ( \mathcal { H } ) )$ is closed in X. From here it follows that ball $\mathcal { B } ( \mathcal { H } )$ is WOT compact.

## EXERCISES

1. Show that if $B \in \mathrm { S O T } - \mathrm { c l } \mathcal { A } ,$ then B belongs to the set defined in (5.4).

2. Show that $\mathcal { B } _ { \mathbf { 0 0 } }$ is SOT dense in $\mathcal { B } .$

3. If $\{ A _ { k } \}$ and $\{ \pmb { B } _ { k } \}$ are sequences in $\mathcal { B } ( \mathcal { H } )$ such that $A_{k} \rightarrow A(\mathrm{WOT})$ and $B _ { k } \rightarrow B ( \mathrm { S O T } )$ then $A _ { k } B _ { k } \rightarrow A B ( \mathrm { W O T } )$

4. With the notation of Exercise 3, show that if $A _ { k } \to A ( \mathrm { S O T } )$ , then $A _ { k } B _ { k } \rightarrow A B ( \mathrm { S O T } )$

5. Let S be the unilateral shift on $l ^ { 2 } ( \mathbb { N } )$ (II.2.10). Examine the sequences $\{ \pmb { S } ^ { k } \}$ and $\left\{ S ^ { * k } \right\}$ and their relation to Exercises 3 and 4.

6. (Halmos.) Fix an orthonormal basis $\{ e _ { n } : n \geqslant 1 \}$ for $\mathcal { H } . ( a )$ Show that O∈weak closure of $\left\{ \sqrt{n} e_{n} ; n \geqslant 1 \right\}$ (Halmos [1982], Solution 28). (b) Let $\{ n _ { i } \}$ be a net of integers such that $\sqrt { n _ { i } e _ { n _ { i } } }   \rightarrow   0$ weakly. Define $A_{i}f = \sqrt{n_{i}}\langle f, e_{n_{i}}\rangle e_{n_{i}}$ for f in $\mathcal { H } .$ Show that $A _ { i }   \rightarrow   0   \mathrm { ( S O T ) }$ but $\{ \dot { A } _ { i } ^ { 2 } \}$ does not converge to 0 (SOT).

## §6. Commuting Operators

If $\mathcal { S } \subseteq \mathcal { B } ( \mathcal { H } ) .$ let $\mathcal { S } ^ { \prime } \equiv \{ A \in \mathcal { B } ( \mathcal { H } ) : A S = S A$ for every S in $\mathcal { P } \} . \mathcal { P } ^ { \prime }$ is called the commutant of $\mathcal { S }$ .It is not difficult to see that $\mathcal { S } ^ { \prime }$ is always an algebra. Similarly, ${ \mathcal { S } } ^ { \prime \prime } \equiv ( { \mathcal { S } } ^ { \prime } ) ^ { \prime }$ is called the double commutant of $\mathcal { L }$ This process can continue, but (happily) $\mathcal { S } ^ { \prime \prime } = \mathcal { S } ^ { \prime }$ (Exercise 1). In some circumstances, $\mathcal { S } = \mathcal { S } ^ { \prime \prime }$

The problem of determining the commutant or double commutant of a single operator or a collection of operators leads to some exciting and interesting mathematics. The commutant is an algebraic object and the idea is to bring the force of analysis to bear in the characterization of this algebra.

We begin by examining the commutant of a direct sum of operators. Recall that if $\mathcal { H } = \mathcal { H } _ { 1 } \oplus \mathcal { H } _ { 2 } \oplus \cdots$ and $A _ { n } \in \mathcal { B } ( \mathcal { H } _ { n } )$ for $n \geqslant 1$ then ${ \pmb A } = { \pmb A } _ { 1 } \oplus { \pmb A } _ { 2 } \oplus \cdots$ defines a bounded operator on $\mathcal { H }$ if and only if $\sup_{n} \| A_{n} \| < \infty;$ in this case $\| A \| = \sup_{n} \| A_{n} \|$ . Also, each operator B on $\mathcal { H }$ has a matrix representation $[ B _ { i j } ]$ where $B _ { i j } \in \mathcal { B } ( \mathcal { H } _ { j } , \mathcal { H } _ { i } )$

6.1. Proposition. (a) If ${ \pmb A } = { \pmb A } _ { 1 } \oplus { \pmb A } _ { 2 } \oplus \cdots i s$ a bounded operator on $\mathcal { H } =$ ${ \mathcal { H } } _ { 1 } \oplus { \mathcal { H } } _ { 2 } \oplus \cdots$ and $B = [B_{ij}] \in \mathcal{B}(\mathcal{H})$ , then $AB = BA$ if and only $f B _ { i j } A _ { j } = A _ { i } B _ { i j }$ for all $i , j .$

(b) If $B = [ B _ { i j } ] \in \mathcal { B } ( \mathcal { H } ^ { ( n ) } ) ,   B A ^ { ( n ) } = A ^ { ( n ) } B$ if and only $if B_{ij}A = AB_{ij}$ for all $i , j .$

The proof of this proposition is an easy exercise in matrix manipulation and is left to the reader.

6.2. Proposition. $If A \in \mathcal{B}(\mathcal{H})$ and $1 \leqslant n \leqslant \infty$ , then $\left\{ A ^ { ( n ) } \right\} ^ { \prime \prime } = \left\{ B ^ { ( n ) } : B \in \left\{ A \right\} ^ { \prime \prime } \right\} =$ $\{ \{ A \} '' \} ^ { n }$

ProoF. The second equality in the statement is a tautology and it is the first equality that forms the substance of the proposition. If $B \in \{ A \} ^ { \prime \prime } ,$ then the preceding proposition implies that $B^{(n)} \in \left\{ A^{(n)} \right\}$ . Now let $\mathbf{B} \in \left\{ A^{(n)} \right\}$ To simplify the notation, assume $n   =   2$ So $B \in \{ A \oplus A \} ''$ let $B = [ B _ { i j } ] , B _ { i j } \in \mathcal { B } ( \mathcal { H } )$

Since ${ \left[ \begin{matrix} { 0 } & { 1 } \\ { 0 } & { 0 } \end{matrix} \right] } { \in } \{ A \oplus A \} ^ { \prime }$ , matrix multiplication shows that $B _ { 1 1 } = B _ { 2 2 }$ and $B _ { 2 1 } = 0$ Similarly, the fact that $\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$ commutes with A ⊕ A implies that $B _ { 1 2 } = 0 . \mathrm { I f } C = B _ { 1 1 } ( = B _ { 2 2 } ) , B = C \oplus C .$ If $T   \in   \{ A \} ^ { \prime }$ , then $T \oplus T \in \{ A \oplus A \} ^ { \prime }$ , so $B ( T \oplus T ) = ( T \oplus T ) B .$ This shows that $C \in \{ A \}$

The next result is a corollary of the preceding proof

## 6.3. Corollary. $If   \mathcal{S} \subseteq \mathcal{B}(\mathcal{H}),   \{\mathcal{S}^{(n)}\}^{\prime\prime} = \{\mathcal{S}^{\prime\prime}\}^{(n)}.$

Say that a subspace $\mathcal { M }$ of $\mathcal { H }$ reduces a collection $\mathcal { S }$ of operators if it reduces each operator in $\mathcal { L }$ By Proposition $\Pi . 3 . 7 , \mathcal { M }$ reduces $\mathcal { S }$ if and only if the projection of $\mathcal { H }$ onto M belongs to $\mathcal { S } ^ { \prime }$ . This is important in the next theorem, due to von Neumann [1929].

6.4. The Double Commutant Theorem. If  is a $C ^ { * }$ -subalgebra of $\mathcal { B } ( \mathcal { H } )$ containing 1, then SOT — cl $\mathcal{A} = \mathrm{WOT} - \mathrm{cl} \mathcal{A} = \mathcal{A}$

PRoOF. By Corollary 5.2, $\mathrm{WOT-cl.\mathcal{A}=SOT-cl.\mathcal{A}}$ Also, since $\alpha ^ { n }$ is SOT closed (Exercise 2) and $\mathcal { A } \subseteq \mathcal { A } ^ { \prime \prime } ,   \mathrm { S O T - c l }   \mathcal { A } \subseteq \mathcal { A } ^ { \prime \prime }$

It remains to show that $\mathcal { A } ^ { \prime \prime } \subseteq \mathrm { S O T - c l } \mathcal { A }$ .To do this Proposition 5.3 will be used.

Let $B { \in } { \mathcal { A } } ^ { \prime \prime } ,   n \geqslant 1$ , and let $\mathcal { M }   \in   \mathrm { L a t }   \mathcal { A } ^ { ( n ) }$ . It must be shown that $B ^ { ( n ) } \mathcal { M } \subseteq \mathcal { M }$ Because is a $C ^ { * } \text {-} \mathrm { a l g e b r a }$ so is $\mathcal { A } ^ { ( n ) }$ So the fact that $\mathcal { M } \in \mathrm { L a t } \mathcal { A } ^ { ( n ) }$ and $A ^ { * ( n ) } \in { \mathcal { A } } ^ { ( n ) }$ whenever $A ^ { ( n ) } \in \mathcal { A } ^ { ( n ) }$ implies that $\mathcal { M }$ reduces $A ^ { ( n ) }$ for each A in $\varkappa$ Si if P is the projection of $\mathcal { H } ^ { ( n ) }$ onto M, $P \in \{ \mathcal { A } ^ { ( n ) } \} ^ { \prime }$ . But $B \in \mathcal { A } ^ { \prime \prime } ;$ so by Corollary 6.3, $B ^ { ( n ) }   \in   \{ { \mathcal { A } } ^ { ( n ) } \} ^ { \prime \prime }$ . Hence $B^{(n)}P = PB^{(n)}$ and $\mathcal { M } \in \mathrm { L a t } B ^ { ( n ) }$ ■

6.5. Corollary. If A is a SOT closed C\*-subalgebra of $\mathcal { B } ( \mathcal { H } )$ containing 1 and $A   \in   \mathcal { B } ( \mathcal { H } )$ such that $A ( P \mathcal { H } ) \subseteq P \mathcal { H }$ for every projection P in $\mathcal { A } ,$ , then $A \in \mathcal { A }$

ProoF. This uses, in addition to the Double Commutant Theorem, Proposition 4.8 as applied to $\varkappa$ . Indeed, $\alpha ^ { \prime }$ is a SOT closed C\*-algebra and hence it is the norm-closed linear span of its projections. So if $A   \in   \mathcal { B } ( \mathcal { H } )$ and $AP\mathcal{H} \subseteq P\mathcal{H}$ for every projection $P$ in $\mathcal { A } ,$ then $A(1 - P)\mathcal{H} \subseteq (1 - P)\mathcal{H}$ for every projection $P$ in $\mathcal { A }$ Thus $P \mathcal { H }$ reduces A and, hence, $AP = PA$ By (4.8), $A   \in   \mathcal { A } ^ { \prime \prime } = \mathcal { A }$

6.6. Theorem. $I f ( X , \Omega , \mu )$ is a σ-finite measure space and $\phi   \in   L ^ { \infty } ( \mu )$ , define $M _ { \phi }$ on $L ^ { 2 } ( \mu )$ by $M _ { \phi } f = \phi f . ~ I f \mathcal { A } _ { \mu } \equiv \left\{ M _ { \phi } \colon \phi { \in } L ^ { \infty } ( \mu ) \right\}$ , then $\mathcal { A } _ { \mu } ^ { \prime } = \mathcal { A } _ { \mu } = \mathcal { A } _ { \mu } ^ { \prime \prime }$

PRoOF. It is easy to see that if $\mathcal { A } = \mathcal { A } ^ { \prime }$ , then $\mathcal { A } = \mathcal { A } ^ { \prime \prime }$ . Since $\mathcal { A } _ { \mu } \subseteq \mathcal { A } _ { \mu } ^ { \prime }$ it suffices to show that $\mathcal { A } _ { \mu } ^ { \prime } \subseteq \mathcal { A } _ { \mu ^ { \prime } }$ So fix A in $\mathcal { A } _ { \mu ^ { \flat } } ^ { \prime }$ it must be shown that $A = M _ { \phi }$ for some φ in $L ^ { \infty } ( \mu )$

Case $I : \mu ( X ) < \infty$ . Here $1   \in   L ^ { 2 } ( \mu ) ;$ put $\phi = A ( 1 )$ . Thus $\phi   \in   L ^ { 2 } ( \mu )$ . If $\psi   \in   L ^ { \infty } ( \mu )$

then $\psi   \in   L ^ { 2 } ( \mu )$ and $A ( \psi ) = A M _ { \psi } 1 = M _ { \psi } A 1 = M _ { \psi } \phi = \phi \psi$ Also, $\| \phi \psi \| _ { 2 } =$ $\| A \psi \| _ { 2 } \leqslant \| A \| \| \psi \| _ { 2 } .$

Let $\Delta _ { n } = \{ x \in X : | \phi ( x ) | \geqslant n \}$ . Putting $\psi = \chi _ { \Delta _ { n } }$ in the preceding argument gives

$$
\| A \| ^ { 2 } \mu ( \Delta _ { n } ) = \| A \| ^ { 2 } \| \psi \| ^ { 2 } \geqslant \| \phi \psi \| ^ { 2 } = \int _ { \Delta _ { n } } | \phi | ^ { 2 } d \mu \geqslant n ^ { 2 } \mu ( \Delta _ { n } ) .
$$

So if $\mu ( \Delta _ { n } ) \neq 0 , \| A \| \geqslant n$ .Since A is bounded, $\mu ( \Delta _ { n } ) = 0$ for some n; equivalently, $\phi   \in   L ^ { \infty } ( \mu )$ . But $A = M _ { \phi }$ on $L ^ { \infty } ( \mu )$ and $L ^ { \infty } ( \mu )$ is dense in $L ^ { 2 } ( \mu ) ,$ so $A = M _ { \phi }$ on $L ^ { 2 } ( \mu ) .$

Case $2 \colon \mu ( X ) = \infty . { \mathrm { ~ I f ~ } } \mu ( \Delta ) < \infty$ , let $L ^ { 2 } ( \mu | \Delta ) = \{ f \in L ^ { 2 } ( \mu ) : f = 0$ off $\Delta \}$ . For f in $L ^ { 2 } ( \mu | \Delta ) ,   A f = A \chi _ { \Delta } f = \chi _ { \Delta } A f \in L ^ { 2 } ( \mu | \Delta )$ Let $A _ { \pm } =$ the restriction of A to $L ^ { 2 } ( \mu | \Delta )$ . By Case 1, there is a $\phi _ { \Delta }$ in $L ^ { \infty } ( \mu | \Delta )$ such that $A _ { \Delta }   =   M _ { \phi _ { \Delta } }$ Now if $\mu ( \Delta _ { 1 } ) < \infty$ and $\mu ( \Delta _ { 2 } ) < \infty , \phi _ { \Delta _ { 1 } } | \Delta _ { 1 } \cap \Delta _ { 2 } = \phi _ { \Delta _ { 2 } } | \Delta _ { 1 } \cap \Delta _ { 2 }$ (Exercise).

Write $X = \bigcup _ { n = 1 } ^ { \infty } \Delta _ { n } ,$ where $\Delta _ { n } { \in } \Omega$ and $\mu ( \Delta _ { n } ) < \infty$ . From the argument above, if $\phi ( x ) = \phi _ { \Delta _ { n } } ( x )$ when $x { \in } \Delta _ { n } ,$ φ is a well-defined measurable function on X. Now $\|   \phi _ { \Delta } \| _ { \infty } ^ { \mathrm { ~ \tiny ~ \ddot { ~ } ~ } } = \|   M _ { \phi _ { \Delta } } \| ( \mathrm { I I } . 1 . 5 ) = \|   A _ { \Delta } \| \leqslant \|   A   \|$ ; hence $\| \phi \| \leqslant A \|$ . It is easy to check that $A = M _ { \phi ^ { * } }$ ■

The next result will enable us to solve a number of problems concerning normal operators. It can be considered as a result that removes a technicality, but it is much more than that.

6.7. The Fuglede-Putnam Theorem. If N and M are normal operators on $\mathcal { H }$ and K, and $B : \mathcal { H } \to \mathcal { H }$ is an operator such that $N B = B M ,$ , then $N ^ { * } B = B M ^ { * }$

ProoF. Note that it follows from the hypothesis that $N ^ { k } B = B M ^ { k }$ for all $k   \geqslant   0 .$ So if $p ( z )$ is a polynomial, $p ( N ) B = B p ( M )$ . Since for a fixed z in C, exp(izN) and $\exp ( i \bar { z } M )$ are limits of polynomials in N and M, respectively, it follows that $\exp ( i \bar { z } N ) B = B \exp ( i \bar { z } M )$ for all z in C. Equivalently, $B = e ^ { - i \bar { z } N } B e ^ { i \bar { z } M }$ Because $\exp(X + Y) = (\exp X)(\exp Y)$ when X and Y commute, the fact that N and M are normal implies that

$$
\begin{aligned} f ( z ) & \equiv e ^ { -   i z N ^ { * } } B e ^ { i z M ^ { * } } \\& = e ^ { -   i z N ^ { * } } e ^ { -   i \bar { z } N } B e ^ { i \bar { z } M } e ^ { i z M ^ { * } } \\& = e ^ { -   i ( z N ^ { * } + \bar { z } N ) } B e ^ { i ( \bar { z } M ^ { } + z M ^ { * } ) } .\\ \end{aligned}
$$

But for every z in C, $z N ^ { * } + \bar { z } N$ and $z M ^ { * } + \bar { z } M$ are hermitian operators. Hence $\exp \left[ - i ( z N ^ { * } + \bar { z } N ) \right]$ and exp $\left[ i ( z M ^ { * } + \bar { z } M ) \right]$ are unitary (Exercise 2.14). Therefore $\| f ( z ) \| \leqslant \| B \|$ . But $f \colon \mathbb { C }   \to   \mathcal { B } ( \mathcal { H } , \mathcal { H } )$ is an entire function. By Liouville's Theorem, f is constant.

Thus, $0 = f ^ { \prime } ( z ) = - i N ^ { * } e ^ { - i z N ^ { * } } B e ^ { i z M ^ { * } } + i e ^ { - i z N ^ { * } } B M ^ { * } e ^ { i z M ^ { * } }$ Putting $z   =   0$ gives $0 = -   i N ^ { * } B + i B M ^ { * }$ , whence the theorem. ■

This theorem was originally proved in Fuglede [1950] under the assumption that $N = M .$ As stated, the theorem was proved in Putnam [1951]. The proof given here is due to Rosenblum [1958]. Another proof is in Radjavi and Rosenthal [1973]. Berberian [1959] observed that Putnam's version can be derived from Fuglede's original theorem by the following matrix trick. If

$$
L = \left[ \begin{matrix} { N } & { 0 } \\ { 0 } & { M } \\ \end{matrix} \right] \quad \mathrm { a n d } \quad A = \left[ \begin{matrix} { 0 } & { B } \\ { 0 } & { 0 } \\ \end{matrix} \right]
$$

then $L$ is normal on $\mathcal { H } \oplus \mathcal { H }$ and $L A = A L$ . Hence $L ^ { * } A = A L ^ { * }$ , and this gives Putnam's version.

6.8. Corollary. If $N = \int z   d E ( z )$ and $B N = N B ,$ then $B E ( \Delta ) = E ( \Delta ) B$ for every Borel set ∆.

PROOF. If $B N = N B ,$ then $B N ^ { * } = N ^ { * } \overline { { B } } ;$ the conclusion now follows by The Spectral Theorem. ■

The Fuglede-Putnam Theorem can be combined with some other results we have obtained to yield the following.

6.9. Corollary. If µ is a compactly supported measure on $\mathbf { C } _ { s }$ then

$$
\{ N _ { \mu } \} ^ { \prime } = { \mathcal { A } } _ { \mu } \equiv \{ M _ { \phi } \colon \phi { \in } L ^ { \infty } ( \mu ) \} .
$$

PROOF. Clearly $\mathcal { A } _ { \mu } \subseteq \{ N _ { \mu } \} ^ { \prime } . \quad \mathrm { I f } \quad A \in \{ N _ { \mu } \} ^ { \prime }$ , then Theorem 6.7 implies $A N _ { \mu } ^ { * } = N _ { \mu } ^ { * } \overline { { A } } .$ By an easy algebraic argument, $A M _ { \phi } = M _ { \phi } A$ whenever $\phi$ is a polynomial in z and ž. By taking weak\* limits of such polynomials, it follows that $A \in \mathcal { A } _ { \mu } ^ { \prime }$ . By Theorem 6.6 $A \in \mathcal { A } _ { \mu }$ ■

Putnam applied his generalization of Fuglede's Theorem to show that similar normal operators must be unitarily equivalent. This has a formal generalization which is useful.

6.10. Proposition. Let $N _ { 1 }$ and $N _ { 2 }$ be normal operators on $\mathcal { H } _ { 1 }$ and $\mathcal { H } _ { 2 }$ . If $X \colon { \mathcal { H } } _ { 1 } \to { \mathcal { H } } _ { 2 }$ is an operator such that $X N _ { 1 } = N _ { 2 } X$ , then:

(a) cl(ran X) reduces $N _ { z }$

(b) ker X reduces $N _ { 1 } ;$

(c) If $M _ { 1 } = N _ { 1 } | ( \ker X ) ^ { \perp }$ and $M_{2}=N_{2}\left|\mathrm{cl}(\tan X)\right|$ , then $M _ { 1 } \cong M _ { 2 }$

PROOF. (a) If $f_{1} \in \mathcal{H}_{1}, N_{2}Xf_{1} = XN_{1}f_{1} \in \mathrm{ran} X;$ so cl(ran X) is invariant for $N _ { 2 }$ . By the Fuglede-Putnam Theorem, $X N _ { 1 } ^ { * } = N _ { 2 } ^ { * } X$ , so cl(ran X) is invariant for $N _ { 2 } ^ { * }$

(b) Exercise.

(c) Since X(ker $X ) ^ { \perp } \subseteq$ cl(ran X), part (c) will be proved if it can be shown that $N _ { 1 } \cong N _ { 2 }$ when ker $X = ( 0 )$ and ran X is dense. So make these assumptions and consider the polar decomposition of X, $X = U A$ (see Exercise 11).

Because ker $X = ( 0 )$ and ran X is dense, A is a positive operator on $\mathcal { H } _ { 1 }$ and $U \colon { \mathcal { H } } _ { 1 } \to { \mathcal { H } } _ { 2 }$ is an isomorphism. Now $X ^ { * } N _ { 2 } ^ { * } = N _ { 1 } ^ { * } X ^ { * }$ , so $X ^ { * } N _ { 2 } = N _ { 1 } X ^ { * }$ A calculation shows that $A ^ { 2 } = X ^ { * } X { \in } { \left\{ N _ { 1 } \right\} } ^ { \prime } ,$ so $A   \in   \{ N _ { 1 } \} ^ { \prime }$ . (Why?) Hence $N_{2}UA = N_{2}X = UAN_{1} = UN_{1}A;$ that is, $N _ { 2 } U = U N _ { 1 }$ on the range of A. But ker $A = ( 0 )$ , so ran A is dense in $\mathcal { H } _ { 1 }$ . Therefore $N _ { 2 } U = U N _ { 1 }$ , or $N _ { 2 } =$ $U N _ { 1 } U ^ { - 1 }$

## 6.11. Corollary. Two similar normal operators are unitarily equivalent.

The corollary appears in Putnam [1951], while Proposition 6.10 first appeared in Douglas [1969]

## EXERCISES

1. If $\mathcal { S } \subseteq \mathcal { B } ( \mathcal { H } )$ , show that $\mathcal { S } ^ { \prime } = \mathcal { S } ^ { \prime \prime }$

2. If $\mathcal { S } \subseteq \mathcal { B } ( \mathcal { H } )$ , show that $\mathcal { S } ^ { \prime }$ is always a SOT closed subalgebra of $\mathcal { B } ( \mathcal { H } )$

3. Prove Proposition 6.1.

4. Let $\mathcal { H }$ be a Hilbert space of dimension α and define S: ${ \mathcal { H } } ^ { ( \infty ) }   \to   { \mathcal { H } } ^ { ( \infty ) }$ by $S(h_1, h_2, \ldots) = (0, h_1, h_2, \ldots).$ . S is called the unilateral shift of multiplicity α. (a) Show that $A = \left[ A_{ij} \right] \in \left\{ S \right\}'$ if and only if $A _ { i j }   =   0$ for $j   >   i$ and $A _ { i j } = A _ { i + 1 , j + 1 }$ for $i   \geqslant   j .$ (b) Show that $A = \left[ A_{ij} \right] \in \left\{ S \right\}$ if and only if $A _ { i j }   =   0$ for $j   >   i$ and $A _ { i j } = A _ { i + 1 , j + 1 } = \mathbf { a }$ multiple of the identity for $i   \geqslant   j .$

5. What is $\{ N _ { \mu } \oplus N _ { \mu } \} { \mathrm { ? ~ } } \{ N _ { \mu } \oplus N _ { \mu } \} { \mathrm { '' ? ~ } }$

6. If $\varkappa$ is a subalgebra of $\mathcal { B } ( \mathcal { H } )$ , show that $\varkappa$ is a maximal abelian subalgebra of $\mathcal { B } ( \mathcal { H } )$ if and only if $\mathcal { A } = \mathcal { A } ^ { \prime }$

7. Find a non-normal operator that is similar to a normal operator. (Hint: Try dim $\mathcal { H } = 2 . )$

8. Let $\mu$ be a compactly supported measure on C and let $\varkappa$ be a separable Hilbert space. A function $f \colon \mathbb { C }   \to   \mathcal { H }$ is a Borel function if $[ f ^ { - 1 } ( G )$ is a Borel set when G is weakly open in $\varkappa$ . Define $L ^ { 2 } ( \mu , \mathcal { H } )$ to be the equivalence classes of Borel functions $f \colon \mathbb { C }   \to   \mathcal { H }$ such that $\int \| f(x) \|^2   d\mu(x) < \infty$ . Define $\langle f , g \rangle = \int \langle f ( x ) , g ( x ) \rangle   d \mu ( x )$ for fandg in $L ^ { 2 } ( \mu , \mathcal { H } )$ (a) Show that $L ^ { 2 } ( \mu , \mathcal { H } )$ is a Hilbert space. Define N on $L ^ { 2 } ( \mu , \mathcal { H } )$ by $(Nf)(z) = zf(z).$ (b) Show that N is a normal operator and $\sigma ( N ) =$ support µ. Calculate $N ^ { * }$ (c) Show that $N \cong N _ { \mu } ^ { ( \alpha ) }$ , where $\alpha = \dim \mathcal{H}$ . (d) Find $\{ N \} ^ { \prime }$ . (Hint: Use 6.1.) (e) Find $\{ N \} ''$

9. Let $\mathcal { H }$ be separable with basis $\{ e _ { n } \}$ . Let A be the diagonal operator on $\mathcal { H }$ given by $A e _ { n } = \lambda _ { n } e _ { n } ,$ where $\sup_{n} \left| \lambda_{n} \right| < \infty$ . Determine $\{ A \} ^ { \prime }$ and $\{ A \} ''$ . Give necessary and sufficient conditions on $\{ l _ { n } \}$ such that $\{ A \}' = \{ A \}''$

10. Let $\alpha$ be a $C ^ { * } .$ -subalgebra of $\mathcal { B } ( \mathcal { H } )$ but do not assume that $\varkappa$ contains the identity operator. Let $\mathcal{M} = \lor \{ \mathrm{rank}   A : A \in \mathcal{A} \}$ and let P = the projection of $\mathcal { H }$ onto M. Show that $\mathrm{SOT-cl} \mathcal{A} = \mathcal{A}^{\prime \prime} P = P \mathcal{A}^{\prime \prime}$

11. Formulate and prove a polar decomposition for operators between different Hilbert spaces.

12. Let $( X , \Omega , \mu )$ be an arbitrary measure space and let $L { \in } L ^ { 1 } ( \mu ) ^ { * }$ . (a) Show that for every f in $L ^ { 2 } ( \mu ) ,$ there is an h in $L ^ { 2 } ( \mu )$ such that $L ( g \bar { f } ) = \int g \bar { h }   d \mu$ for all $g$ in $L ^ { 2 } ( \mu )$ (b) If $f   \in   L ^ { 2 } ( \mu )$ , let $T f$ be the function h in $L ^ { 2 } ( \mu )$ obtained in part (a). Show that $T : L ^ { 2 } ( \mu ) \to L ^ { 2 } ( \mu )$ defines a bounded linear operator and $T$ commutes with $M _ { \phi }$ for every φ in $L ^ { \infty } ( \mu )$ . (c) In light of parts (a) and (b), compare Theorem 6.6 and Example 20.17 in Hewitt and Stromberg [1975].

## §7. Abelian von Neumann Algebras

7.1. Definition. A von Neumann algebra $\alpha$ is a C\*-subalgebra of $\mathcal { B } ( \mathcal { H } )$ such that $\mathcal { A } = \mathcal { A } ^ { \prime \prime }$

Note that if $\alpha$ is a von Neumann algebra, then $1 \in \mathcal { A }$ and $\alpha$ is SOT closed. Conversely, if $1 \in \mathcal { A }$ and $\varkappa$ is a SOT closed C\*-subalgebra of $\mathcal { B } ( \mathcal { H } )$ then $\varkappa$ is a von Neumann algebra by the Double Commutant Theorem.

It is a result of S. Sakai that a C\*-algebra is isomorphic to a von Neumann algebra if it is the dual of a Banach space. The converse to this is an easy consequence of the fact that $\mathcal { B } ( \mathcal { H } )$ is a dual space (Exercise 2.21). For an account of the history of this result and its predecessors, as well as a number of proofs, see Kadison [1985].

7.2. Examples. (a) $\mathcal { B } ( \mathcal { H } )$ and C are von Neumann algebras.

(b) If $( X , \Omega , \mu )$ is a σ-finite measure space, then $\mathcal { A } _ { \mu } \equiv \left\{ M _ { \phi } \colon \phi   \in   L ^ { \infty } ( \mu ) \right\} \subseteq$ $\mathcal { B } ( L ^ { 2 } ( \mu ) )$ is an abelian von Neumann algebra by Theorem 6.6. In fact, it is a maximal abelian von Neumann algebra.

It will be shown in this section that $\mathcal { A } _ { \mu }$ is the only abelian von Neumann algebra up to a \*-isomorphism. However, there are many others that are not unitarily equivalent to $\mathcal { A } _ { \mu }$

For $\mathcal { A } _ { j } \subseteq \mathcal { B } ( \mathcal { H } _ { j } ) , j \geqslant 1 , \mathcal { A } _ { 1 } \oplus \mathcal { A } _ { 2 } \oplus \cdots$ is used to denote the $l ^ { \infty }$ direct sum of ${ \mathcal { A } } _ { 1 } , { \mathcal { A } } _ { 2 } , \ldots .$ That $\mathrm{is}, \mathcal{A}_{1} \oplus \mathcal{A}_{2} \oplus \cdots = \{A_{1} \oplus A_{2} \oplus \cdots : A_{j} \in \mathcal{A}_{j}$ for $j   \geqslant   1$ and $\operatorname { s u p } _ { j } \| A _ { j } \| < \infty \}$ Note that $\mathcal { A } _ { 1 } \oplus \mathcal { A } _ { 2 } \oplus \cdots \subseteq \mathcal { B } ( \mathcal { H } _ { 1 } \oplus \mathcal { H } _ { 2 } \oplus \cdots )$ and $\vec { A _ { 1 } \oplus A _ { 2 } \oplus \cdots \parallel } = \operatorname* { s u p } _ { j } \| A _ { j } \|$

7.3. Proposition. (a) If ${ \mathcal { A } } _ { 1 } , { \mathcal { A } } _ { 2 } , \ldots a r e$ von Neumann, algebras, then so is ${ \mathcal { A } } _ { 1 } \oplus { \mathcal { A } } _ { 2 } \oplus \cdots ( { \mathsf { b } } )$ If A is a von Neumann algebra and $1 \leqslant n \leqslant \infty$ , then $\mathcal { A } ^ { ( n ) }$ is a von Neumann algebra.

PROOF. Exercise.

The proof of the next result is also an exercise.

7.4. Proposition. Let $\mathcal { A } _ { j }$ be a von Neumann algebra on $\mathcal { H } _ { j } ,   j = 1 , 2$ . If U: $\mathcal { H } _ { 1 }   \rightarrow   \mathcal { H } _ { 2 }$ is an isomorphism such that $U \mathcal { A } _ { 1 } U ^ { - 1 } = \mathcal { A } _ { 2 } .$ , then $\dot { U } \mathcal { A } _ { 1 } ^ { \prime } U ^ { - 1 } = \mathcal { A } _ { 2 } ^ { \prime }$

Now let $( X , \Omega , \mu )$ be a σ-finite measure space and define $\rho \colon \mathcal { A } _ { \mu } \to \mathcal { A } _ { \mu } ^ { ( 2 ) }$ by