all h in $\mathbb { R } ^ { 2 }$ However, $A ^ { * }$ is the transpose of A and so $A ^ { * } \neq A$ . Indeed, for any operator A on an R-Hilbert space, $\langle A h , g \rangle \in \mathbb { R }$

## 2.13. Proposition. $If   A = A^*$ , then

$$
\| A \| = \sup \left\{ \left| \langle A h, h \rangle \right| : \| h \| = 1 \right\}.
$$

PROOF. $\mathrm{Put} M = \sup \{ | \langle A h , h \rangle | : \| h \| = 1 \}. \mathrm{If} \| h \| = 1.$ then $| \langle A h , h \rangle | \leqslant \| A \|$ hence $M \leqslant \| A \|$ . On the other hand, if $\| { \boldsymbol { h } } \| = \| { \boldsymbol { g } } \| = 1$ , then

$$
\begin{align*}\langle A(h \pm g), h \pm g \rangle = \langle Ah, h \rangle \pm \langle Ah, g \rangle \pm \langle Ag, h \rangle + \langle Ag, g \rangle \\= \langle Ah, h \rangle \pm \langle Ah, g \rangle \pm \langle g, A^*h \rangle + \langle Ag, g \rangle.\end{align*}
$$

Since $A = A ^ { * }$ , this implies

$$
\langle A ( h \pm g ) , h \pm g \rangle = \langle A h , h \rangle \pm 2 \mathrm { R e } \langle A h , g \rangle + \langle A g , g \rangle .
$$

Subtracting one of these two equations from the other gives

$$
4 \mathrm { R e } \left\langle A h , g \right\rangle = \left\langle A ( h + g ) , h + g \right\rangle - \left\langle A ( h - g ) , h - g \right\rangle .
$$

Now it is easy to verify that $| \langle A f , f \rangle | \leqslant M \| f \| ^ { 2 }$ for any f in $\mathcal { H }$ .Hence using the parallelogram law we get

$$
\begin{align*}4\operatorname{Re}\langle A h, g \rangle & \leqslant M(\| h + g \|^2 + \| h - g \|^2) \\& = 2M(\| h \|^2 + \| g \|^2) \\& = 4M\end{align*}
$$

since h and $g$ are unit vectors. Now suppose $\langle A h , g \rangle = e ^ { i \theta } | \langle A h , g \rangle | .$ Replacing h in the inequality above with $e ^ { - i \theta } \vec { h }$ gives $| \langle A h , g \rangle | \leqslant M$ if $\| \boldsymbol { h } \| = \| \boldsymbol { g } \| = 1$ Taking the supremum over all g gives $\| A \boldsymbol{h} \| \leqslant M$ when $\| \boldsymbol { h } \| = 1$ . Thus $\| A \| \leqslant M$

## 2.14. Corollary. $If   \boldsymbol{A} = \boldsymbol{A}^*$ and $\langle A h , h \rangle = 0$ for all h, then $A   =   0$

The preceding corollary is not true unless $A = A ^ { * }$ , as the example given after Proposition 2.12 shows. However, if a complex Hilbert space is present, this hypothesis can be deleted.

2.15. Proposition. If $\mathcal { H }$ is a C-Hilbert space and $A \in \mathcal { B } ( \mathcal { H } )$ such that $\langle A h , h \rangle = 0   f o r$ all h in $\mathcal { H }$ , then $A   =   0 .$

The proof of (2.15) is left to the reader.

If $\mathcal { H }$ is a C-Hilbert space and $A   \in   \mathcal { B } ( \mathcal { H } )$ , then $B   =   ( A + A ^ { * } ) / 2$ and $C = ( A - A ^ { * } ) / 2 i$ are self-adjoint and $A = B + i C$ . The operators B and $c$ are called, respectively, the real and imaginary parts of A.

## 2.16. Proposition. If $A   \in   \mathcal { B } ( \mathcal { H } )$ , the following statement are equivalent.

(a) A is normal.

(b) $\| A \bar { h } \| = \| A ^ { * } h \|$ for all h.

If H is a C-Hilbert space, then these statements are also equivalent to:

(c) The real and imaginary parts of A commute.

PROOF. $\mathbf { I f } \quad h \in { \mathcal { H } } .$ then $\| A \boldsymbol{h} \|^2 - \| A^* \boldsymbol{h} \|^2 = \langle A \boldsymbol{h}, A \boldsymbol{h} \rangle - \langle A^* \boldsymbol{h}, A^* \boldsymbol{h} \rangle =$ $\left\langle ( A ^ { * } A - A A ^ { * } ) h , h \right\rangle$ . Since $A ^ { * } A - A A ^ { * }$ is hermitian, the equivalence of (a) and (b) follows from Corollarv 2.14.

If $B , C$ are real and imaginary parts of A, then a calculation yields

$$
A ^ { * } A = B ^ { 2 } - i C B + i B C + C ^ { 2 } ,
$$

$$
A A ^ { * } = B ^ { 2 } + i C B - i B C + C ^ { 2 } .
$$

Hence $A^{*}A = AA^{*}$ if and only if $CB = BC$ , and so (a) and (c) are equivalent.

2.17. Proposition. If $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ , the following statements are equivalent.

(a) A is an isometry.

(b) $A ^ { * } A = I .$

(c) $\langle A h , A g \rangle = \langle h , g \rangle \; { \it f o r ~ a l l ~ } h , g { \it i n ~ } \mathcal { H } .$

PRooF. The proof that (a) and (c) are equivalent was seen in Proposition I.5.2. Note that if $h , g \in \mathcal { H }$ , then $\langle A ^ { * } A h , g \rangle = \langle A h , A g \rangle$ . Hence (b) and (c) are easily seen to be equivalent. ■

2.18. Proposition. If $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ , then the following statements are equivalent.

(a) $A^{*}A = AA^{*} = I.$

(b) A is unitary. (That is, A is a surjective isometry.)

(c) A is a normal isometry.

PROOF. $(a) \Rightarrow (b);$ Proposition I.5.2.

(b)⇒(c): By (2.17), $A ^ { * } A = I .$ But it is easy to see that the fact that A is a surjective isometry implies that $A ^ { - 1 }$ is also. Hence by (2.17) $I = (A^{-1})^{*}A^{-1}$ $(A^{*})^{-1}A^{-1}=(AA^{*})^{-1}$ ; this implies that $A^{*}A = A\overline{A^{*}} = I$

$(c) \Rightarrow (a)$ By (2.17), $A ^ { * } A = I .$ Since A is also normal, $A A ^ { * } = A ^ { * } A = I$ and so A is surjective. ■

We conclude with a very important, though easily proved, result.

2.19. Theorem. $If   A \in \mathcal{B}(\mathcal{H})$ , then ker $A = ( \operatorname{rank} A^* )^{\perp}$

PROOF. If h∈ker A and $g \in \mathcal { H }$ then $\langle h , A ^ { * } g \rangle = \langle A h , g \rangle = 0 ,$ so ker $\mathbf { A } \subseteq$ (ran $A ^ { * } ) ^ { \perp }$ . On the other hand, if $h \perp \tan A^{*}$ and $g \in \mathcal { H }$ , then $\langle A h , g \rangle =$ $\langle h , A ^ { * } g \rangle = 0 ;$ so (ran A\*)⊥ ⊆ ker A. ■

Two facts should be noted. Since $A ^ { * * } = A$ , it also holds that ker $A ^ { * } =$ $( \operatorname { r a n } A ) ^ { \perp }$ . Second, it is not true that $( \ker A ) ^ { \perp } = \operatorname { r a n } A ^ { * }$ since ran $A ^ { * }$ may not be closed. All that can be said is that $( \ker A ) ^ { \perp } = \operatorname { c l } ( \operatorname { r a n } A ^ { * } )$ and (ker $A^{*} )^{\perp} = \mathrm{cl} \left( \mathrm{rank} A \right)$

## EXERCISES

1. Prove Proposition 2.5.

2. Prove Proposition 2.6.

3. Verify the statement in Example 2.8.

4. Verify the statement in Example 2.9.

5. Find the adjoint of a diagonal operator (Exercise 1.8).

6. Let S be the unilateral shift and compute $S S ^ { * }$ and $S ^ { * } S .$ Also compute $S ^ { n } S ^ { * n }$ and $S ^ { * n } S ^ { n }$

7. Compute the adjoint of the Volterra operator V (1.7) and $V + V ^ { * }$ . What is ran $( V + V ^ { * } ) ?$

8. Where was the hypothesis that $\mathcal { H }$ is a Hilbert space over C used in the proof of Proposition 2.12?

9. Suppose $A = B + i C .$ where B and C are hermitian and prove that $B =$ $( A + A ^ { * } ) / 2 ,   C = ( A - A ^ { * } ) / 2 i .$

10. Prove Proposition 2.15.

11. If A and B are self-adjoint, show that AB is self-adjoint if and only if $AB = BA$

12. Let $\sum _ { n = 0 } ^ { \infty } \alpha _ { n } z ^ { n }$ be a power series with radius of convergence $R , 0 < R \leqslant \infty$ . If $A   \in   \mathcal { B } ( \mathcal { H } )$ and $\| \pmb { A } \| < R$ , show that there is an operator T in $\mathcal { B } ( \mathcal { H } )$ such that for any $h , g$ in $\begin{array} { r } { \mathcal { H } , \langle T h , g \rangle = \sum _ { n = 0 } ^ { \infty } \alpha _ { n } \langle A ^ { n } h , g \rangle } \end{array}$ . [If $f(z) = \sum \alpha_n z^n$ , the operator $T$ is usually denoted by f(A).]

13. Let A and T be as in Exercise 12 and show that $\begin{array} { r } { \| T - \sum _ { k = 0 } ^ { n } \alpha _ { k } A ^ { k } \| \rightarrow 0 } \end{array}$ as $n \to \infty$ If $BA = AB,$ show that $B T = T B .$

14. If $f(z) = \exp z = \sum_{n = 0}^{\infty} z^n / n!$ and A is hermitian, show that $f ( i A )$ is unitary.

15. If A is a normal operator on $\mathcal { H } ,$ show that A is injective if and only if A has dense range. Give an example of an operator B such that ker $B = ( 0 )$ but ran B is not dense. Give an example of an operator C such that C is surjective but ker $C \neq ( 0 )$

16. Let $M _ { \phi }$ be a multiplication operator (1.5) and show that ker $M _ { \phi }   =   0$ if and only if $\mu ( \{ x : \phi ( x ) = 0 \} ) = 0$ Give necessary and sufficient conditions on $\phi$ that ran $M _ { \phi }$ be closed.

## §3. Projections and Idempotents; Invariant and Reducing Subspaces

3.1. Definition. An idempotent on $\mathcal { H }$ is a bounded linear operator E on $\mathcal { H }$ such that $E ^ { 2 } = E .   \mathbf { A }$ projection is an idempotent P such that ker $P = ( \tan P ) ^ { \perp }$

If $\mathcal { M } \leqslant \mathcal { H }$ , then $P _ { \mathcal { M } }$ is a projection (Theorem I.2.7). It is not difficult to construct an idempotent that is not a projection (Exercise 1).

Let E be any idempotent and set $\mathcal { M } = \operatorname { r a n } E$ and $\mathcal { N } = \ker E .$ Since E is continuous, $\mathcal { N }$ is a closed subspace of . Notice that $( I - E ) ^ { 2 } = I - 2 E + E ^ { 2 } =$ $\boldsymbol{I}-2 \boldsymbol{E}+\boldsymbol{E}=\boldsymbol{I}-\boldsymbol{E};$ thus $I - E$ is also an idempotent. Also, $0 = (I - E)h =$ $h - E h ,$ if and only if $E h = h .$ So ran $E \supseteq \ker ( I - E )$ . On the other hand, if $h \in \operatorname { r a n } E$ $h = E g$ and so $E h = E ^ { 2 } g = E g = h ;$ hence ran $E = \ker ( I - E )$ Similarly, $\operatorname { r a n } ( I - E ) = \ker E .$ These facts are recorded here.

3.2. Proposition. (a) E is an idempotent if and only if $I - E$ is an idempotent. (b) ran $E = \ker ( I - E )$ , ker $E = \operatorname { r a n } ( I - E ) ,$ , and both ran E and ker E are closed linear subspaces of H. (c) If $\mathcal { M } = \operatorname { r a n } E$ and $\mathcal { N } = \ker E .$ then $\mathcal { M } \cap \mathcal { N } = ( 0 )$ and $\mathcal { M } + \mathcal { N } = \mathcal { H }$

The proof of part (c) is left as an exercise. There is also a converse to (c) If $\mathcal { M } , \mathcal { N } \leq \mathcal { H } , \mathcal { M } \cap \mathcal { N } = ( 0 )$ , and $\mathcal { M } + \mathcal { N } = \mathcal { H }$ , then there is an idempotent E such that $\mathcal { M } = \operatorname { r a n } E$ and $\mathcal { N } = \ker E ;$ moreover, E is unique. The difficult part in proving this converse is to show that E is bounded. The same fact is true in more generality (for Banach spaces) and so this proof will be postponed.

Now we turn our attention to projections, which are peculiar to Hilbert space.

3.3. Proposition. If E is an idempotent on $\mathcal { H }$ and $E \neq 0 ,$ the following statements are equivalent.

(a) E is a projection.

(b) E is the orthogonal projection of  onto ran E.

(c) $E \parallel = 1$

(d) E is hermitian.

(e) E is normal.

(f) $\langle E h , h \rangle \geqslant 0$ for all h in $\mathcal { H } .$

PROOF. $(a) \Rightarrow (b);$ Let $\mathcal { M } = \operatorname { r a n } E$ and $P = P_{\mathcal{M}} \quad  If   h \in \mathcal{H},   P h =$ the unique vector in M such that $h - P h \in \mathcal{M}^{\perp} = (\mathrm{ran}   E)^{\perp} = \mathrm{ker}   E$ by (a). But $h - E h = ( I - E ) h \in$ ker E. Hence $E h = P h$ by uniqueness.

$$( \mathsf { b } ) { \Rightarrow } ( \mathsf { c } ) { : } \mathrm { ~ B y ~ } ( \mathrm { I } . 2 . 7 ) , \; \| \: E \: \| \leqslant 1$$ . But $E h = h$ for h in ran E, so $\| E \| = 1$

$(c) \Rightarrow (a):  Let   h \in (kerE)^{\perp}$ . Now ran $( I - E ) = \ker E ,$ so h — Eh∈ker E. Hence $0 = \langle h - E h , h \rangle = \| h \| ^ { 2 } - \langle E h , h \rangle$ Hence $\| h \| ^ { 2 } = \langle E h , h \rangle \leqslant \| E h \| \| h \| \leqslant$ $\| h \| ^ { 2 }$ . So for h in (ker $E ) ^ { \perp } , \quad \| E h \| = \| h \| = \langle E h , h \rangle ^ { 1 / 2 }$ . But then for h in $( \ker E ) ^ { \perp }$

$$
\| h - E h \| ^ { 2 } = \| h \| ^ { 2 } - 2 \operatorname { R e } \langle E h , h \rangle + \| E h \| ^ { 2 } = 0 .
$$

That is, (ker $E ) ^ { \perp } \subseteq \ker ( I - E ) = \operatorname { r a n } E$ . On the other hand, if geran $E ,$ $\boldsymbol { g } = \boldsymbol { g } _ { 1 } + \boldsymbol { g } _ { 2 }$ , where $g _ { 1 }   \in   \ker E$ and $g_{2} \in (\ker E)^{\perp}$ . Thus $g = E g = E g _ { 2 } = g _ { 2 } ;$ that is, ran $E \subseteq ( \ker E ) ^ { \perp }$ . Therefore ran $E = ( \ker E ) ^ { \perp }$ and E is a projection.

$( b ) \Rightarrow ( f ) :$ If $h \in \mathcal { H }$ , write $h = h _ { 1 } + h _ { 2 } ,   h _ { 1 }$ eran E, $h _ { 2 } \in$ ker $E = ( \tan E ) ^ { \perp }$ . Hence $\langle E h , h \rangle = \langle E ( h _ { 1 } + h _ { 2 } ) , h _ { 1 } + h _ { 2 } \rangle = \langle E h _ { 1 } , h _ { 1 } \rangle = \langle h _ { 1 } , h _ { 1 } \rangle = \| h _ { 1 } \| ^ { 2 } \geqslant 0.$

$(f) \Rightarrow (a);$ Let $h _ { 1 }   \in   \operatorname { r a n } E$ and $h _ { 2 } \in \ker E .$ Then by $0 \leqslant \langle E(h_1 + h_2),$ $h _ { 1 } + h _ { 2 } \rangle = \langle h _ { 1 } , h _ { 1 } \rangle + \langle h _ { 1 } , h _ { 2 } \rangle$ . Hence $- \left\| h _ { 1 } \right\| ^ { 2 } \leqslant \left\langle h _ { 1 } , h _ { 2 } \right\rangle$ for all $h _ { 1 }$ in ran E and $h _ { 2 }$ in ker E. If there are such $h _ { 1 }$ and $h _ { 2 }$ with $\langle h _ { 1 } , h _ { 2 } \rangle = \bar { \alpha } \neq 0 ,$ then substituting $k_{2} = - 2\alpha^{- 1}\left\| h_{1} \right\|^{2}h_{2}$ for $h _ { 2 }$ in this inequality, we obtain $- \left\| h _ { 1 } \right\| ^ { 2 } \leqslant - 2 \left\| h _ { 1 } \right\| ^ { 2 } ,$ a contradiction. Hence $\langle h _ { 1 } , h _ { 2 } \rangle = 0$ whenever $h _ { 1 }   \in   \operatorname { r a n } E$ and $h _ { 2 } { \in } { 1 }$ ker E. That is, E is a projection.

$(a) \Rightarrow (d)$ Let $h , g \in \mathcal { H }$ and put $\boldsymbol { h } = \boldsymbol { h } _ { 1 } + \boldsymbol { h } _ { 2 }$ and $\boldsymbol { g } = \boldsymbol { g } _ { 1 } + \boldsymbol { g } _ { 2 } ,$ where $h _ { 1 } , g _ { 1 } { \in } { \mathrm { r a n } } E$ and $h_{2},g_{2}\in \ker E=(\operatorname{ran}E)^{\perp}$ . Hence $\langle E h , g \rangle = \langle h _ { 1 } , g _ { 1 } \rangle$ . Also, $\langle E ^ { * } h , g \rangle = \langle h , E g \rangle = \langle h _ { 1 } , g _ { 1 } \rangle = \langle E h , g \rangle$ . Thus $E = E ^ { * }$

(d)⇒(e): clear.

(e)⇒(a): By (2.16), $\|   E h   \| = \|   E ^ { * } h   \|$ for every h. Hence ker $E = \ker E ^ { * }$ . But by (2.19), ker $E^{*} = (\tan E)^{\perp}$ , so E is a projection.

Note that by part (b) of the preceding proposition, if E is a projection and $\mathcal { M } = \operatorname { r a n } E ,$ then $E = P _ { \mathcal { M } }$

Let P be a projection with ran $P = \mathcal { M }$ and ker $P = \mathcal { N }$ . So both $\mathcal { M }$ and $\mathcal { N }$ are closed subspaces of $\mathcal { H }$ and, hence, are also Hilbert spaces. As in (I.6.1), we can form $\mathcal { M } \oplus \mathcal { N }$ . If $U : { \mathcal { M } } \oplus { \mathcal { N } } \to { \mathcal { H } }$ is defined by $U ( h \oplus g ) = h + g$ for h in $\mathcal { M }$ and $g$ in $\mathcal { N } ,$ then it is easy to see that U is an isomorphism. Making this identification, we will often write $\mathcal { H } = \mathcal { M } \oplus \mathcal { N }$

More generally, the following will be used.

3.4. Definition. If $\{ \mathcal { M } _ { i } \}$ is a collection of pairwise orthogonal subspaces of $\mathcal { H } ,$ then

$$
\oplus _ { i } \mathcal { M } _ { i } \equiv \nabla _ { i } \mathcal { M } _ { i } .
$$

If M and $\mathcal { N }$ are two closed linear subspaces of $\mathcal { H } ,$ then

$$
\mathcal { M } \ominus \mathcal { N } \equiv \mathcal { M } \cap \mathcal { N } ^ { \perp } .
$$

This is called the orthogonal difference of $\mathcal { M }$ and $\mathcal { N } .$

Note that if $\mathcal { M } , \mathcal { N } \leqslant \mathcal { H }$ and $\mathcal { M } \bot \mathcal { N }$ , then $\mathcal { M } + \mathcal { N }$ is closed. (Why?) Hence $\mathcal { M } \oplus \mathcal { N } = \mathcal { M } + \mathcal { N }$ . The same is true, of course, for any finite collection of pairwise orthogonal subspaces but not for infinite collections.

3.5. Definition. If $A   \in   \mathcal { B } ( \mathcal { H } )$ and $\mathcal { M } \leqslant \mathcal { H }$ , say that $\mathcal { M }$ is an invariant subspace for A if $A h \in \mathcal { M }$ whenever $h \in \mathcal { M }$ . In other words, if $A \mathcal { M } \subseteq \mathcal { M }$ . Say that $\mathcal { M }$ is a reducing subspace for A if $\mathcal { A } \mathcal { M } \subseteq \mathcal { M }$ and $\mathcal { A } \mathcal { M } ^ { \perp } \subseteq \mathcal { M } ^ { \perp }$

If $\mathcal { M } \leqslant \mathcal { H }$ , then $\mathcal { H } = \mathcal { M } \oplus \mathcal { M } ^ { \perp }$ . If $A   \in   \mathcal { B } ( \mathcal { H } )$ , then A can be written as a $2 \times 2$ matrix with operator entries,

$$
A = { \left[ \begin{matrix} { W } & { X } \\ { Y } & { Z } \end{matrix} \right] } ,
$$

where $W   \in   \mathcal { B } ( \mathcal { M } ) , \; X   \in   \mathcal { B } ( \mathcal { M } ^ { \perp } , \mathcal { M } ) , \; Y   \in   \mathcal { B } ( \mathcal { M } , \mathcal { M } ^ { \perp } ) ,$ and $Z \in \mathcal { B } ( \mathcal { M } ^ { \perp } )$

3.7. Proposition. $If A \in \mathcal{B}(\mathcal{H}), \mathcal{M} \leq \mathcal{H}$ , and $P = P _ { \mathcal { M } } ,$ then statements (a) through (c) are equivalent.

(a) M is invariant for A.

(b) $PAP = AP.$

(c) In $( 3 . 6 ) , \; Y = 0 .$

Also, statements (d) through (g) are equivalent.

(d) M reduces A.

(e) $PA = AP.$

(f) In (3.6), Y and X are 0.

(g) M is invariant for both A and $A ^ { * }$

PROOF. (a)⇒(b): If $h \in \mathcal { H }$ , PheM. So $A P h \in \mathcal { M }$ Hence, $P(APh) = APh$ That is, $PAP = AP$

(b)⇒(c): If P is represented as a $2 \times 2$ operator matrix relative to $\mathcal { H } = \mathcal { M } \oplus \mathcal { M } ^ { \perp }$ , then

$$
P = { \left[ \begin{matrix} { I } & { 0 } \\ { 0 } & { 0 } \end{matrix} \right] } .
$$

Hence,

$$
PAP = \begin{bmatrix} W & 0 \\ 0 & 0 \end{bmatrix} = AP = \begin{bmatrix} W & 0 \\ Y & 0 \end{bmatrix}.
$$

So $Y   =   0 ,$

(c)⇒(a): If Y = 0 and $h \in \mathcal { M } ,$ then

$$
\boldsymbol { A } \boldsymbol { h } = \left[ \begin{array} { c c } { \boldsymbol { W } } & { \boldsymbol { X } } \\ { 0 } & { \boldsymbol { Z } } \end{array} \right] \left[ \begin{array} { c } { \boldsymbol { h } } \\ { 0 } \end{array} \right] = \left[ \begin{array} { c } { \boldsymbol { W } \boldsymbol { h } } \\ { 0 } \end{array} \right] \in \mathcal { M } .
$$

$(d) \Rightarrow (c);$ Since both M and $\mathcal { M } ^ { \perp }$ are invariant for A, (b) implies that $AP = PAP$ and $A(I - P) = (I - P)A(I - P)$ . Multiplying this second equation gives $A - AP = A - AP - PA + PAP.$ Thus $PA = PAP = AP.$

(e)⇒(f): Exercise.

(f)⇒(g): If $X = Y = 0 ,$ then

$$
A = \left[ \begin{matrix} { W } & { 0 } \\ { 0 } & { Z } \\ \end{matrix} \right] \quad \mathrm { a n d } \quad A ^ { * } = \left[ \begin{matrix} { W ^ { * } } & { 0 } \\ { 0 } & { Z ^ { * } } \\ \end{matrix} \right] .
$$

By (c), M is invariant for both A and $A ^ { * } ,$

(g)⇒(d): If $h \in \mathcal { M } ^ { \perp }$ and $g \in \mathcal { M } _ { 1 }$ then $\langle g , A h \rangle = \langle A ^ { * } g , h \rangle = 0$ since $A ^ { * } g \in { \mathcal { M } }$ Since g was an arbitrary vector in $\mathcal { M } ,   A h \in \mathcal { M } ^ { \perp }$ . That is, $A M ^ { \perp } \subseteq \mathcal { M } ^ { \perp }$

If M reduces A, then $X = Y = 0$ in (3.6). This says that a study of A is reduced to the study of the smaller operators W and Z. This is the reason for the terminology.

If $A   \in   \mathcal { B } ( \mathcal { H } )$ and M is an invariant subspace for A, then $A \vert \mathcal { M }$ is used to denote the restriction of A to M. That is, $A | \mathcal { M }$ is the operator on M defined by $( A \mid \mathcal { M } ) h = A h$ whenever $h \in \mathcal { M }$ .Note that $\mathcal { A } | \mathcal { M } \in \mathcal { B } ( \mathcal { M } )$ and $\| A \| \mathcal { M } \| \leqslant \| A \|$ Also, if M is invariant for A and A has the representation (3.6) with $Y   =   0$ then $W = A \vert \mathcal { M }$

## EXERCISES

1. Let $\mathcal { H }$ be the two-dimensional real Hilbert space $\begin{array} { r } { \mathbb { R } ^ { 2 } , } \end{array}$ let $\mathcal { M } \equiv \left\{ ( x , 0 ) \in \mathbb { R } ^ { 2 } : x \in \mathbb { R } \right\}$ and let $\mathcal { N } \equiv \{ ( x , x \tan \theta ) : x \in \mathbb { R } \}$ , where $0 < \theta < \frac { 1 } { 2 } \pi$ . Find a formula for the idempotent $E _ { \theta }$ with ran $E _ { \theta } = \mathcal { M }$ and ker $E _ { \theta }   =   \mathcal { N }$ . Šhow that $\| E _ { \theta } \| = ( \sin \theta ) ^ { - 1 }$

2. Prove Proposition 3.2 (c).

3. Let $\{ \mathcal { M } _ { i } ; i { \in } I \}$ be a collection of closed subspaces of $\mathcal { H }$ and show that $n \{ \mathcal { M } _ { i } ^ { \perp }$ $i { \in } I \} = [ \vee \{ { \mathcal { M } } _ { i } { : } i { \in } I \} ] ^ { \perp }$ and $[ \cap \{ \mathcal { M } _ { i } \colon i { \in } I \} ] ^ { \perp } = \vee \; \{ \mathcal { M } _ { i } ^ { \perp } \colon i { \in } I \}$

4. Let P and Q be projections. Show: (a) $P + Q$ is a projection if and only if ran P ⊥ ran Q. If $P + Q$ is a projection, then ran $(P + Q) = \mathrm{ran} P + \mathrm{ran} Q$ and ker $(P + Q) = \ker P \cap$ ker Q. (b) PQ is a projection if and only if $PQ = QP$ If PQ is a projection, then ran PQ = ran P∩ ran Q and ker $PQ = \ker P + \ker Q.$

5. Generalize Exercise 4 as follows. Suppose $\{ \mathcal { M } _ { i } ; i { \in } I \}$ is a collection of subspaces of $\mathcal { H }$ such that $\mathcal { M } _ { i } \bot \mathcal { M } _ { j }$ if $i \neq j .$ Let $P _ { i }$ be the projection of $\mathcal { H }$ onto $\mathcal { M } _ { i }$ and show that for all h in $\mathcal { H } , \sum \{ P _ { i } h \colon i { \in } I \}$ converges to Ph, where P is the projection of $\mathcal { H }$ onto $\vee \left\{ { \mathcal { M } } _ { i } ; i { \in } I \right\}$

6. If P and Q are projections, then the following statements are equivalent. (a) $P - Q$ is a projection. (b) ran $Q \subseteq \operatorname { r a n } P$ (c) PQ = Q. (d) QP = Q. If P − Q is a projection, then ran $(P - Q) = (\mathrm{ran} P) \ominus (\mathrm{ran} Q)$ and ker $( P - Q ) = \mathrm { r a n } \; Q + \mathrm { k e r } \; P .$

7. Let P and Q be projections. Show that $PQ = QP$ if and only if $P + Q - PQ$ is a projection. If this is the case, then ran $(P + Q - PQ) = \tan P + \tan Q$ and $\ker(P + Q - PQ) = \ker P \cap \ker Q.$

8. Give an example of two noncommuting projections.

9. Let $A \in \mathcal { B } ( \mathcal { H } )$ and let N = graph $A \subseteq { \mathcal { H } } \oplus { \mathcal { H } }$ That is, $\mathcal { N } = \{ h \oplus A h \colon h { \in } \mathcal { H } \}$ Because A is continuous and linear, $\mathcal { N } \leqslant \mathcal { H } \oplus \mathcal { H }$ Let $\mathcal { M } = \mathcal { H } \oplus ( 0 ) \leq \mathcal { H } \oplus \mathcal { H }$ Prove the following statements. (a) $\mathcal { M } \cap \mathcal { N } = ( 0 )$ if and only if ker $A = ( 0 )$ (b) $\mathcal { M } + \mathcal { N }$ is dense in $\mathcal { H } \oplus \mathcal { H }$ if and only if ran A is dense in f. (c) $\mathcal { M } + \mathcal { N } = \mathcal { H } \oplus \mathcal { H }$ if and only if A is surjective.

10. Find two closed linear subspaces $\mathcal { M } , \mathcal { N }$ of an infinite dimensional Hilbert space $\mathcal { H }$ such that $\mathcal { M } \cap \mathcal { N } = ( 0 )$ and $\mathcal { M } + \mathcal { N }$ is dense in $\mathcal { H }$ , but $\mathcal { M } + \mathcal { N } \neq \mathcal { H }$

11. Define A: $l ^ { 2 } ( \mathbb { Z } ) \to l ^ { 2 } ( \mathbb { Z } )$ by $A(\ldots,\alpha_{-1},\alpha_{0},\alpha_{1},\ldots)=(\ldots,\alpha_{-1},\alpha_{0},\alpha_{1},\ldots),$ where  sits above the coefficient in the 0-place. Find an invariant subspace of A that does not reduce A. This operator is called the bilateral shift.

12. Let $\mu = \mathbf { A r e a }$ measure on $\mathbb { D }   \equiv   \{ z   \in   \mathbb { C } \colon | z | < 1 \}$ and define A: $L ^ { 2 } ( \mu )   \to   L ^ { 2 } ( \mu )$ by $(Af)(z) = zf(z)  for  |z| < 1$ and f in $L ^ { 2 } ( \mu )$ . Find a nontrivial reducing subspace for A and an invariant subspace that does not reduce A.

## §4. Compact Operators

It turns out that most of the statements about linear transformations on finite dimensional spaces have nice generalizations to a certain class of operators on infinite dimensional spaces—namely, to the compact operators, Let ball $\mathcal { H }$ denote the closed unit ball in $\mathcal { H }$

4.1. Definition. A linear transformation T: $\mathcal { H } \rightarrow \mathcal { H }$ is compact if T(ball $\mathcal { H } )$ has compact closure in $\mathcal { H }$ The set of compact operators from $\mathcal { H }$ into $\mathcal { H }$ is denoted by $\mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$ and $\mathcal { B } _ { 0 } ( \mathcal { H } ) = \mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$

4.2. Proposition. (a) $\mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } ) \subseteq \mathcal { B } ( \mathcal { H } , \mathcal { H } )$

(b) $\mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$ is a linear space and $if\{T_n\}\subseteq\mathcal{B}_0(\mathcal{H},\mathcal{H})$ and $T \in \mathcal { B } ( \mathcal { H } , \mathcal { H } )$ such that $\| T _ { n } - T \| \to 0 ,$ then $T   \in   \mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } ) .$

(c) If $A \in \mathcal{B}(\mathcal{H}),   B \in \mathcal{B}(\mathcal{H})$ , and $T   \in   \mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$ , then TA and $B T \in \mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$

PROOF. (a) If $T   \in   \mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$ , then cl[T(ball )] is compact in $\mathcal { H }$ Hence there is a constant $C > 0$ such that T(ball $\mathcal { H } ) \subseteq \{ k \in \mathcal { H } : \| k \| \leqslant C \}$ . Thus $\| T \| \leqslant C .$

(b) It is left to the reader to show that $\mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$ is a linear space. For the second part of (b), it will be shown that T(ball $\mathcal { H } )$ is totally bounded. Since $\mathcal { H }$ is a complete metric space, this is equivalent to showing that T(ball $\mathcal { H } )$ has compact closure. Let $\varepsilon   >   0$ and choose n such that $\| T - T _ { n } \| < \varepsilon / 3$ Since $T _ { n }$ is compact, there are vectors $h _ { 1 } , \ldots , h _ { m }$ in ball $\mathcal { H }$ such that $T _ { n } ($ ball $\mathcal { H } ) \subseteq \bigcup _ { j = 1 } ^ { m } B ( T _ { n } h _ { j } ; \varepsilon / 3 )$ . So if $\| h \| \leqslant 1$ , there is an $h _ { j }$ with二 $T _ { n } h _ { j } - T _ { n } h \parallel < \varepsilon / 3$ . Thus

$$
\begin{align*}\|   T h_j - T h   \| & \leqslant \|   T h_j - T_n h_j \| + \|   T_n h_j - T_n h   \| + \|   T_n h - T h   \| \\& < 2 \|   T - T_n   \| + \varepsilon / 3 \\& < \varepsilon.\end{align*}
$$

Hence T(ball $\mathcal { H } ) \subseteq \bigcup _ { j = 1 } ^ { m } B ( T h _ { j } ; \varepsilon ) .$

The proof of (c) is left to the reader.

4.3. Definition. An operator $T$ on $\mathcal { H }$ has finite rank if ran $T$ is finite dimensional. The set of continuous finite rank operators is denoted by $\mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } ) ;   \mathcal { B } _ { 0 0 } ( \mathcal { H } ) = \mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } )$

It is easy to see that $\mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } )$ is a linear space and $\mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } ) \subseteq$ $\mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$ (Exercise 2). Before giving other examples of compact operators, however, the next result should be proved.

4.4. Theorem. If $T \in \mathcal { B } ( \mathcal { H } , \mathcal { H } )$ , the following statements are equivalent.

(a) $T$ is compact.

(b) $T ^ { * }$ is compact.

(c) There is a sequence $\{ T _ { n } \}$ of operators of finite rank such that $\| T - T _ { n } \| \to 0 .$