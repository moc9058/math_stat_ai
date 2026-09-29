Clearly, $\lambda a \geqslant 0$ if $a   \geqslant   0$ and $\lambda \geqslant 0 .$ Let $a , b \in \mathcal { A } _ { + } ;$ it must be shown that $a + b \geqslant 0$ . It suffices to assume that $\| a \| , \| b \| \leqslant 1$ . But $\|   1 -   \textstyle { \frac { 1 } { 2 } } ( a + b )   \| =$ $\textstyle { \frac { 1 } { 2 } } \| ( 1 - a ) + ( 1 - b ) \| \leq 1$ by (3.6d). So by (3.6e), $\textstyle { \frac { 1 } { 2 } } ( a + b ) \geq 0$

If $a \in \mathcal { A } _ { + } \cap ( - \mathcal { A } _ { + } )$ then $a   =   a ^ { * }$ and $\sigma ( a ) = \{ 0 \}$ . But $\| a \| = r(a)   (1.11\mathrm{e}).$

Now to look at one more example—a very important one.

3.8. Theorem. If $\mathcal { H }$ is a Hilbert space and $A   \in   \mathcal { B } ( \mathcal { H } )$ , then $A \geqslant 0$ if and only $if \langle A h, h \rangle \geqslant 0$ for all h in $\mathcal { H }$

PROOF. If $A \geqslant 0 ,$ then (3.6c) $A = T ^ { * } T$ for some T in $\mathcal { B } ( \mathcal { H } )$ Hence $\langle A h , h \rangle =$ $\| T h \| ^ { 2 } \geqslant 0 .$ Conversely, suppose $\langle A h , h \rangle \geqslant 0$ for all h in $\mathcal { H }$ .By (II.2.12), $A = A ^ { * }$ . It remains to show that $\sigma ( A ) \in [ 0 , \infty )$ . If $h \in \mathcal { H }$ and $\lambda < 0 ,$ then

$$
\begin{align*}\| (A - \lambda) h \|^2 &= \| A h \|^2 - 2 \lambda \langle A h, h \rangle + \lambda^2 \| h \|^2 \\&\geqslant - 2 \lambda \langle A h, h \rangle + \lambda^2 \| h \|^2 \geqslant \lambda^2 \| h \|^2\end{align*}
$$

since $\lambda   <   0$ and $\langle A h , h \rangle \geqslant 0 .$ By (VII.6.4), λ∉σa(A). But this implies that $A - \lambda$ is left invertible (Exercise VII.6.5). Since $A - \lambda$ is self-adjoint, $A - \lambda$ is also right invertible. Thus $\lambda \notin \sigma ( A )$ and $A \geqslant 0 .$ ■

3.9. Definition. If  is a $C ^ { * } .$ -algebra and $a,b \in \mathbb{R} \mathbb{C} \mathcal{A}$ then $a \leqslant b \text { if } b - a \in \mathcal { A } _ { + }$

This ordering makes a C\*-algebra as well as Rea into ordered vector spaces.

Note that if A and B are hermitian operators on the Hilbert space $\mathcal { H }$ then $A \leqslant B$ if and only $\mathrm{if} \langle A h, h \rangle \leqslant \langle B h, h \rangle$ for all h in $\mathcal { H }$

This section closes with an application of positivity to obtain the polar decomposition of an operator. If $\lambda \in \mathbf { C }$ , then $\lambda ^ { \bar { } } = | \lambda | e ^ { i \theta }$ for some $\theta ;$ this is the polar decomposition of λ. Can an analogue be found for operators? To answer this question we might first ask what is the analogue of $| \lambda |$ and $e ^ { i \theta }$ among operators. If $A   \in   \mathcal { B } ( \mathcal { H } )$ , then the proper definition for $| A |$ would seem to be $| A | \equiv ( A ^ { * } A ) ^ { 1 / 2 } \left[ \mathrm { s e e } ( 3 . 5 ) \right]$ . How about an analogue of $e ^ { i \theta } ?$ Should it be a unitary operator? An isometry? For an arbitrary operator neither of these is appropriate. The following new class of operators is needed.

3.10. Definition. A partial isometry is an operator W such that for h in $( \ker W ) ^ { \perp } ,   \| W h \| = \| h \|$ . The space (ker $W ) ^ { \perp }$ is called the initial space of W and the space ran W is called the final space of W. See Exercises 15–20 for more on partial isometries.

3.11. Polar Decomposition. If $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ , then there is a partial isometry W with (ker $A ) ^ { \perp }$ as its initial space and cl(ran A) as its final space such that $A = W | A | .$ Moreover, if $A = U P$ where $P   \geqslant   0$ and U is a partial isometry with ker $U = \ker P ,$ then $P   =   | A |$ and $U = W ,$

PROOF. If $h \in \mathcal { H }$ , then $\| A h \| ^ { 2 } = \langle A h , A h \rangle = \langle A ^ { * } A h , h \rangle = \langle | A | h , | A | h \rangle$ . Thus

## 3.12

$$
\| A h \| ^ { 2 } = \| | A | h \| ^ { 2 } .
$$

Since (ran $A ^ { * } ) ^ { \perp } =$ ker A, ran $A ^ { * }$ is dense in (ker $A ) ^ { \perp }$ . If $f { \in } { \mathrm { r a n } }   A ^ { * } , f = A ^ { * } g$ for g in (ker $A ^ { * } ) ^ { \perp } =$ cl ran A. Therefore, $\{ A ^ { * } A k : k \in \mathcal { H } \}$ is dense in cl $\left[ \tan A^{*} \right] =$ $( \ker A ) ^ { \perp }$ . But $A^{*} A k = |A|^{2} k = |A| h.$ , where $\pmb { h } = | \pmb { A } | k$ That is, $\{ | A | h \colon h \in \mathcal { H } \}$ is dense in (ker A)↓. If $W \colon \operatorname { r a n } | A | \to$ ran A is defined by

## 3.13

$$
W ( | A | h ) = A h ,
$$

then (3.12) implies that W is a well-defined isometry. Thus W extends to an isometry $W : ( \ker A ) ^ { \perp } \to \operatorname { c l } ( \operatorname { r a n } A )$ . If Wh is defined to be 0 for h in ker A, W is a partial isometry. By (3.13) $W | A | = A .$

For the uniqueness, note that $A^{*}A = PU^{*}UP$ . Now $U ^ { \star } U = E \equiv \mathrm { t h } ($ e projection onto the initial space of U (Exercise 16), (ker $U ) ^ { \perp } = ( \ker P ) ^ { \perp } =$ cl (ran P). Thus $A^{*}A = PEP = P^{2}$ . By the uniqueness of the positive square root, $P   =   | A | .$ Since $A = U | A | , U | A | h = A h = W | A | h .$ That is, U and W agree on a dense subset of their common initial space. Hence $U = W .$ ■

## EXERCISES

1. Prove the uniqueness statement in Proposition 3.4 for the case that $\varkappa$ is abelian.

2. Prove Proposition 3.5.

3. Let $A   \in   \mathcal { B } ( L ^ { 2 } ( 0 , 1 ) )$ be defined by $( A f ) ( t ) = t f ( t )$ Show that $A \geqslant 0$ and find $A ^ { 1 / n }$

4. Let $( X , \Omega , \mu )$ be a σ-finite measure space, let $\phi   \in   L ^ { \infty } ( X ,   \Omega , \mu )$ , and define $M _ { \phi }$ as in Theorem II.1.5. Show that $M _ { \phi }   \geqslant   0$ if and only if $\phi ( x ) \geqslant 0 \mathrm { a . e . } [ \mu ]$ . What is $M _ { \phi } ^ { 1 / n \gamma }$ If $M _ { \phi } \in \operatorname { R e } { \mathcal { B } } ( { \mathcal { H } } )$ , find the positive and negative parts of $M _ { \phi }$

5. Find an example of a positive operator on a Hilbert space that has a nonhermitian square root.

6. If $a \in \operatorname { R e } \mathcal { A } ,$ show that $| a | \equiv ( a ^ { 2 } ) ^ { 1 / 2 } = a _ { + } + a _ { - }$

7. If $a \in \mathcal { A } _ { + }$ , show that $x ^ { * } a x { \in } { \mathcal { A } } .$ for every x in $\measuredangle$

8. If $a,b \in \mathcal{A}, 0 \leqslant a \leqslant b.$ and a is invertible, then b is invertible and $b ^ { - 1 } \leqslant a ^ { - 1 }$

9. If $a,b \in \mathbb{R}\mathbb{C} \times \mathbb{C}, a \leqslant b.$ and $a b = b a .$ then $f ( a ) \leqslant f ( b )$ for every increasing continuous function f on IR.

10. If $a   \in   \mathbf { R e } .   \mathcal { A }$ and $\| a \| \leqslant 1$ , show that a is the sum of two unitaries. (Hint: First solve this for $\mathcal { A } = \mathbb { C } . )$

11. If $\alpha > 0 ,$ define $f_{a}:(-\alpha^{-1},\infty)\to\mathbb{R}\quad by\quad f_{a}(t)=t/(1+\alpha t)=\alpha^{-1}\left[1-(1+\alpha t)^{-1}\right]$ Show:

(a) If $0 \leqslant a \leqslant b$ in A, $f_{\alpha}(a) \leqslant f_{\alpha}(b)$ for all $\alpha > 0 ;$

(b) $f _ { x } ( t ) < \operatorname* { m i n } \left\{ t , \alpha ^ { - 1 } \right\}$ for $t > 0 ;$

(c) $\operatorname* { l i m } _ { \alpha \to 0 } f _ { \alpha } ( t ) = t$ uniformly on bounded intervals in $[ 0 , \infty ) ;$

(d) if $0 \leqslant \alpha \leqslant \beta, f_{\alpha} \leqslant f_{\beta}$ on $[ 0 , \infty ) ;$

(e) $f _ { \alpha } \circ f _ { \beta } = f _ { \alpha + \beta } ;$

(f) $\operatorname* { l i m } _ { \alpha \to \infty } \alpha f _ { \alpha } ( t ) = 1$ uniformly on bounded intervals in $[ 0 , \infty )$

12. If $a , b \in \mathcal { A }$ + and $a \leqslant b ,$ show that $a ^ { \pmb { \beta } } \leqslant b ^ { \pmb { \beta } }$ for $0 \leqslant \beta \leqslant 1. \left( a^{\beta} = f(a) \right.$ where $f ( t ) = t ^ { \beta } . )$ (Hint: Let $f _ { \alpha }$ be as in Exercise 11 and show that $\int _ { 0 } ^ { \infty } f _ { \alpha } ( t ) \alpha ^ { - \beta } d \alpha = \gamma t ^ { \beta }$ where $\gamma   >   0$ Use the definition of the improper integral and the functional calculus.)

13. Give an example of a C\*-algebra $\varkappa$ and positive elements $a , b$ in $\mathcal { A }$ such that $a \leqslant b$ but $b ^ { 2 } - a ^ { 2 } \neq \mathcal { A } _ { + }$

14. Let $\mathcal { A } = \mathcal { B } ( l ^ { 2 } )$ , let $a = \mathbf { t h e }$ unilateral shift on $l ^ { 2 } ,$ and let $b   =   a ^ { * }$ . Show that $\sigma ( a b ) \neq \sigma ( b a )$

15. Let $\mathcal { W } \in \mathcal { B } ( \mathcal { H } )$ and show that the following statements are equivalent: (a) W is a partial isometry; (b) $W ^ { * }$ is a partial isometry; (c) $W ^ { * } W$ is a projection; (d) $W W ^ { * }$ is a projection; (e) W $W ^ { * } W = W ;$ (f) $W ^ { * } W W ^ { * } = W ^ { * }$

16. If W is a partial isometry, show that $W ^ { * } W$ is the projection onto the initial space of Wand $W W ^ { * }$ is the projection onto the final space of W.

17. If $W _ { 1 } ,   W _ { 2 }$ are partial isometries, define $W _ { 1 } \lesssim W _ { 2 }$ to mean that $W_{1}^{*}W_{1} \leqslant W_{2}^{*}W_{2}$ $W_{1}W_{1}^{*} \leqslant W_{2}W_{2}^{*}$ , and $W _ { 2 } h = W _ { 1 }$ h whenever h is in the initial space of $W _ { 1 }$ . Show that $\lesssim$ is a partial ordering on the set of partial isometries and that a partial isometry W is a maximal element in this ordering if and only if either W or $W ^ { * }$ is an isometry.

18. Using the terminology of Exercise 17, show that the extreme points of ball $\mathcal { B } ( \mathcal { H } )$ are the maximal partial isometries. (See Exercise V.7.10.)

19. Find the polar decomposition of each of the following operators: (a) $M _ { \phi }$ as defined in (II.1.5); (b) the unilateral shift; (c) the weighted unilateral shift $\left[ A ( x _ { 1 } , x _ { 2 } , \ldots ) = \right.$ $( 0 , \alpha _ { 1 } x _ { 1 } , \alpha _ { 2 } x _ { 2 } , \ldots )$ for x in $l ^ { 2 }$ and $\sup_{n} | \alpha_{n} | < \infty$ with nonzero weights; (d) A ⊕ α (in terms of the polar decomposition of A)

20. Let $A   \in   \mathcal { B } ( \mathcal { H } )$ such that ker $A = ( 0 )$ and $A \geqslant 0$ and define S on ${ \mathcal { H } } = { \mathcal { H } } \oplus { \mathcal { H } } \oplus \cdots$ by $S(h_1, h_2, \ldots) = (0, A h_1, A h_2, \ldots)$ . Find the polar decomposition of $S , S = W | S |$ and show that $S = | S |   W .$

21. Show that the parts of the polar decomposition of a normal operator commute.

22. If $A \in \mathcal { B } ( \mathcal { H } )$ , show that there is a positive operator P and a partial isometry W such that $A = P W .$ Discuss the uniqueness of P and W.

23. If A is normal and invertible, show that the parts of the polar decomposition of A belong to $C ^ { * } ( A )$

24. Give an example of a normal operator A such that the partial isometry in the polar decomposition of A does not belong to $C ^ { * } ( A )$

25. Show that for an arbitrary C\*-algebra $\varkappa$ it is not necessarily true that $a b \in \mathcal { A }$ + whenever a and $b \in \mathcal { A } _ { + } . \mathrm { I f } ,$ however, $a , b \in \mathcal { A }$ + and $a b = b a ,$ then $a b \in \mathcal { A } _ { + }$

## $\S 4 ^ { * }$ . Ideals and Quotients of C\*-Algebras

We begin with a basic result.

4.1. Proposition. If I is a closed left or right ideal in the C\*-algebra $\varkappa$ $a   \in   I$ with $a = a ^ { * }$ , and $if \in C(\sigma(a))$ with $f ( 0 ) = 0 ,$ then $f ( a ) { \in } I$

PRooF. Note that if I is proper, then $0   \in   \sigma ( a )$ since a cannot be invertible. Since $\sigma ( a ) \subseteq \mathbb { R }$ , the Weierstrass Theorem implies there is a sequence $\{ p _ { n } \}$ of polynomials such that $p _ { n } ( t )   \to   f ( t )$ uniformly for $\begin{array} { r } { \begin{array} { r l r } { t } & { { } \mathrm { i n } } & { \sigma ( a ) } \end{array} } \end{array}$ Hence $p _ { n } ( 0 )   \to   f ( 0 )   = 0 .$ Thus $q _ { n } ( t ) = p _ { n } ( t ) - p _ { n } ( 0 ) \to f ( t )$ uniformly on σ(a) and $q _ { n } ( 0 ) = 0$ for all n. Thus $q _ { n } ( a )   \in   { \pmb I }$ and by the functional calculus, $\| q _ { n } ( a ) - f ( a ) \| \to 0 .$ Hence $f ( a )   \in   I .$

4.2. Corollary. $I f I$ is a closed left or right ideal, $a   \in   I$ with $a   =   a ^ { * }$ , then $a _ { + } , a _ { - } ,$ $\vert a \vert ,$ and $| a | ^ { 1 / \vec { 2 } }   \in   \vec { I } .$

Note that if I is a left ideal of $\alpha ,$ then $\left\{ a ^ { * } { : }   a { \in } I \right\}$ is a right ideal. Therefore a left ideal I is an ideal if $a ^ { * }   \in I$ whenever $a   \in   I ,$

4.3. Theorem. If I is a closed ideal in the C\*-algebra $\alpha ,$ then $a ^ { * }   \in   I$ whenever $a   \in   I .$

PROOF. Fix a in I. Thus $a ^ { * } a   \in   I$ since I is an ideal. The idea is to construct a sequence $\{ u _ { n } \}$ of continuous functions defined on $[ 0 , \infty )$ such that

$$
u_{n}(0)=0   and   u_{n}(t) \geq 0   for all   t;
$$

4.4

$$
\left\| a u _ { n } ( a ^ { * } a ) - a \right\| \rightarrow 0 \text { as } n \rightarrow \infty.
$$

Note that if such a sequence $\{ u _ { n } \}$ can be constructed, then $u _ { n } ( a ^ { * } a ) \geqslant 0$ and $u _ { n } ( a ^ { * } a )   \in I$ by Proposition 4.1. Also, $u _ { n } ( a ^ { * } a ) a ^ { * } \in I$ since I is an ideal and $\| u _ { n } ( a ^ { * } a ) a ^ { * } - a ^ { * } \| = \| a u _ { n } ( a ^ { * } a ) - a \| \to 0$ by (ii). Thus $a ^ { * }   \in   I$ whenever $a   \in   I .$ It remains to construct the sequence $\{ u _ { n } \}$

Note that

$$
\begin{align*}& \|   a u_n(a^* a) - a \|^2 \\& \quad = \|   [ a u_n(a^* a) - a ]^* [ a u_n(a^* a) - a ]   \| \\& \quad = \|   u_n(a^* a) a^* a u_n(a^* a) - a^* a u_n(a^* a) - u_n(a^* a) a^* a + a^* a   \|.\end{align*}
$$

If $b = a ^ { * } a .$ then the fact that $b u _ { n } ( b ) = u _ { n } ( b ) b$ implies that $\| a u _ { n } ( a ^ { * } a ) - a \| ^ { 2 } =$ $\| f _ { n } ( b ) \| \leqslant \sup \left\{ \left| f _ { n } ( t ) \right| : t \geqslant 0 \right\}$ , where $f _ { n } ( t ) = t u _ { n } ( t ) ^ { 2 } - 2 t u _ { n } ( t ) + t = t [ u _ { n } ( t ) - 1 ] ^ { 2 }$ If $u _ { n } ( t ) = n t$ for $0 \leqslant t \leqslant n^{-1}$ and $u ( t ) = 1$ for $t \geqslant n ^ { -   1 }$ , then it is seen that sup $\left\{ | f _ { n } ( t ) | : t \geqslant 0 \right\} = 4 / 2 7 n \rightarrow 0$ as $n   \rightarrow   \infty ;$ so (4.4) is satisfied.

Notice that the construction of the sequence $\{ u _ { n } \}$ satisfying (4.4) actually proves more. It shows that there is a “local"approximate identity. That is, the proof of the preceding theorem shows that the following holds.

4.5. Proposition. If  is $a C ^ { * } - a l g e b r a$ and I is an ideal of $\alpha ,$ then for every a in I there is a sequence $\{ e _ { n } \}$ of positive elements in I such that:

(a) $e _ { 1 } \leqslant e _ { 2 } \leqslant \cdots$ and $\| e _ { n } \| \leqslant 1$ for all $n _ { y }$

(b) $a e _ { n } - a \parallel \rightarrow 0$ as $n   \to   \infty$

In the preceding proposition the sequence $\{ e _ { n } \}$ depends on the element a. It is also true that there is a positive increasing net $\{ e _ { i } \}$ in I such that $\| e _ { i } a - a \| \to 0$ and $\| a e _ { i } - a \| \rightarrow 0$ for every a in I (see p. 36 of Arveson [1976]).

We turn now to an important consequence of Theorem 4.3.

4.6. Theorem. If A is a $C ^ { * } { - a l g e b r a }$ and I is a closed ideal of $\alpha ,$ then for each $a + I$ in $\mathcal { A } / I$ define $( a + I ) ^ { * } = a ^ { * } + I .$ Then $\mathcal { A } / I$ with its quotient norm is a $C ^ { * } { \text-- } a l g e b r a .$

To prove (4.6), a lemma is needed.

4.7. Lemma. If I is an ideal in a C\*-algebra $\varkappa$ and $a \in \mathcal { A } ,$ then $\| a + I \| = \inf \left\{ \| a - a x \| : x \in I,   x \geqslant 0, \right.$ and $\| x \| \leqslant 1 \}$

PROOF. If (ball I)+ = {x∈ball $I \colon x \geqslant 0 \}$ , then clearly $\| a + I \| \leqslant \inf \left\{ \| a - ax \| : \right\}$ $x \in ( \mathrm { b a l l }   I ) _ { + } \}$ since a $I I \subseteq I .$ Let $y   \in   I$ and let $\{ e _ { n } \}$ be a sequence in (ball I)+ such that $\| y - y e _ { n } \|   \to   0$ as $n   \to   \infty$ . Now $0 \leqslant 1 - e_{n} \leqslant 1$ ,so $\| ( a + y ) ( 1 - e _ { n } ) \| \leqslant$ $\| a + y \|$ . Hence

$$
\begin{aligned}\| a + y \| & \geqslant \liminf \| (a + y)(1 - e_n) \| \\& = \liminf \| (a - ae_n) + (y - ye_n) \| \\& = \liminf \| a - ae_n \|\end{aligned}
$$

since $\| y - y e _ { n } \| \to 0$ Thus $\| a + y \| \geqslant \inf_{n} \| a - a e_{n} \| \geqslant \inf \left\{ \| a - a x \| : x \in ( \mathrm{ball} I )_{+} \right\}$ Taking the infimum over all y in I gives the desired remaining inequality.■

PROOF OF THEOREM 4.6. The only difficult part of this proof is to show that $\| a + I \| ^ { 2 } = \| a ^ { * } a + I \|$ for every a in $\alpha .$ Since $x ^ { * }   \in   I$ whenever $x   \in   I$ (4.3), $\| \boldsymbol { a } ^ { \star } + \boldsymbol { I } \| = \| \boldsymbol { a } + \boldsymbol { I } \|$ for all a in $\varkappa$ Thus the submultiplicativity of the norm in $\mathcal { A } / I$ (VII.2.6) implies

$$
\begin{aligned}\| \boldsymbol{a}^{*} \boldsymbol{a} + \boldsymbol{I} \| &= \| (\boldsymbol{a}^{*} + \boldsymbol{I})(\boldsymbol{a} + \boldsymbol{I}) \| \\& \leqslant \| \boldsymbol{a}^{*} + \boldsymbol{I} \| \| \boldsymbol{a} + \boldsymbol{I} \| \\&= \| \boldsymbol{a} + \boldsymbol{I} \|^2.\end{aligned}
$$

On the other hand, the preceding lemma gives that

$$
\begin{align*}\|a + I\|^2 = \inf\{\|a - ax\|^2: x \in ( ball I)_+\} \\= \inf\{\|a(1 - x)\|^2: x \in ( ball I)_+\} \\= \inf\{\|(1 - x)a^*a(1 - x)\|: x \in ( ball I)_+\}.\end{align*}
$$

$$
\begin{aligned} &\leqslant \inf \{ \| a^{*} a(1 - x) \| \colon x \in (\mathrm{ball}   I)_{+} \}\\ &= \inf \{ \| a^{*} a - a^{*} a x \| \colon x \in (\mathrm{ball}   I)_{+} \}\\ &= \| a^{*} a + I \|.\\ \end{aligned}
$$

If $\mathcal { A } , \mathcal { B }$ are C\*-algebras with ideals $I , J ,$ respectively, and $\rho \colon { \mathcal { A } }   \to   { \mathcal { B } }$ is a \*-homomorphism such that $\rho ( I ) \subseteq J ,$ , then $\rho$ induces a \*-homomorphism $\tilde { \rho } ;$ $\mathcal { A } / I   \to   \mathcal { B } / J$ defined by $\tilde { \rho } ( a + I ) = \rho ( a ) + J .$ In particular, if $I = \ker \rho$ and $J = ( 0 ) ,$ then $\tilde { \rho } ;$ A/ker $\rho   \rightarrow   \mathcal { B }$ is a \*-homomorphism and $\tilde { \pmb { \rho } }   \circ   \pmb { \pi } = \pmb { \rho } ,$ where $\pi \cdot$ $\mathcal { A }   \to   \mathcal { A } / \ker \rho$ is the natural map. Keep these facts in mind when reading the proof of the next result.

4.8. Theorem. If $\mathcal { A } , \mathcal { B }$ are C\*-algebras and ρ: $\mathcal { A } \rightarrow \mathcal { B }$ is a \*-homomorphism, then $\rho(a) \| \leqslant \| a$ ∥ for all a and ran $\rho$ is closed in B. If ρ is a \*-monomorphism, then $\rho$ is an isometry.

PROOF. The fact that $\| \rho ( a ) \| \leqslant \| a \|$ is a restatement of (1.11d). Now assume that $\rho$ is a \*-monomorphism. As in the proof of (1.11d), it suffices to assume that $\varkappa$ and $\mathcal { B }$ have identities and $\rho(1) = 1. (\mathrm{Why?})$

If $a \in \mathcal { A }$ and $a   =   a ^ { * }$ , then it is easy to see that $\rho ( a ) = \rho ( a ) ^ { * }$ and $\sigma ( \rho ( a ) ) \subseteq \sigma ( a )$ If $\sigma ( \rho ( a ) ) \neq \sigma ( a )$ , there is a continuous function f on $\sigma ( a )$ such that $f ( t ) = 0$ for all t in $\sigma ( \rho ( a ) )$ but $f$ is not identically zero on $\sigma ( a )$ . Thus $f ( \rho ( a ) )   =   0 ,$ but $f ( a ) \neq 0 .$ Let $\{ p _ { n } \}$ be polynomials such that $p _ { n } ( t )   \rightarrow   f ( t )$ uniformly on $\sigma ( a )$ Thus $p _ { n } ( a )   \to   f ( a )$ and $p_{n}(\rho(a)) \to f(\rho(a)) = 0$ But $p _ { n } ( \rho ( a ) ) = \rho ( p _ { n } ( a ) ) \to \rho ( f ( a ) )$ Thus $\rho ( f ( a ) ) = f ( \rho ( a ) ) = 0$ Since $\rho$ was assumed injective, $f ( a ) = 0 ,$ a contradiction. Hence $\sigma ( a ) = \sigma ( \rho ( a ) ) { \mathrm { ~ i f ~ } } a = a ^ { * }$ .Thus by $(1.11\mathrm{e}), \| a \| = r(a) =$ $r ( \rho ( a ) ) = \| \rho ( a ) \| { \mathrm { ~ i f ~ } } a = a ^ { * }$ . But then for arbitrary $a , \left\| a \right\| ^ { 2 } = \left\| a ^ { * } a \right\| = \left\| \rho ( a ^ { * } a ) \right\| =$ $\| \rho ( a ) ^ { \star } \rho ( a ) \| = \| \rho ( a ) \| ^ { 2 }$ and $\rho$ is an isometry.

To complete the proof let $\rho \colon { \mathcal { A } }   \to   { \mathcal { B } }$ be a \*-homomorphism and let $\tilde { \rho } ;$ $\mathcal { A } / \ker \rho   \to   \mathcal { B }$ be the induced \*-monomorphism. So $\tilde { \rho }$ is an isometry and hence ran $\tilde { \rho }$ is closed. But ran $\tilde { \rho } = \operatorname { r a n } \rho$ ■

We turn now to some specific examples of C\*-algebras and their ideals.

4.9. Proposition. If X is compact and I is a closed ideal of $C ( X ) ,$ , then there is a closed subset F of X such that $I = \{ f \in C ( X ) : f ( x ) = 0$ for all $x$ in $F \}$ Moreover, $C ( X ) / I$ is isometrically isomorphic to $C ( F )$

PROOF. Let $F = \{ x \in X : f(x) = 0$ for all f in $I \}$ , so F is a closed subset of X. If $\mu   \in   M ( X )$ and $\mu \bot I ,$ then $\int | f | ^ { 2 }   d \mu = 0$ for every f in I since $| f | ^ { 2 } = f { \bar { f } } \in I$ whenever $f { \in } I .$ Thus each f must vanish on the support of $\mu ,$ hence $| \mu | ( X \setminus F ) = 0$ . Conversely, if $\mu   \in   M ( X )$ and the support of $\mu$ is contained in $F , \int f d \mu   =   0$ for every f in I. Thus $I ^ { \perp } = \{ \mu \in M ( X ) : | \mu | ( X \setminus F ) = 0 \}$ . Since I is closed, $I = { } ^ { \perp } ( I ^ { \perp } ) = \{ f \in C ( X ) : f ( x ) = 0$ for all x in $F \}$ . The remainder of the proof is left to the reader. L

4.10. Proposition. If I is a closed ideal of $\mathcal { B } ( \mathcal { H } )$ , then $I   \supseteq   \mathcal { B } _ { 0 } ( \mathcal { H } )$ or $I = ( 0 )$

PROOF. Suppose $I \neq ( 0 )$ and let T be a nonzero operator in I. Thus there are vectors $f _ { 0 } , f _ { 1 }$ in $\mathcal { H }$ such that $T f _ { 0 } = f _ { 1 } \neq 0 .$ Let $g _ { 0 } , g _ { 1 }$ be arbitrary nonzero vectors $\mathcal { H }$ Define A: $\mathcal { H } \rightarrow \mathcal { H }$ by letting $A h = \left\| g _ { 0 } \right\| ^ { - 2 } \left\langle h , g _ { 0 } \right\rangle f _ { 0 }$ Then $A g _ { 0 } = f _ { 0 }$ and $A h = 0$ if $h   \perp   g _ { 0 }$ . Define B: $\mathcal { H } \rightarrow \mathcal { H }$ by letting $B h =$ $\| f _ { 1 } \| ^ { - 2 } \langle h , f _ { 1 } \rangle g _ { 1 } . \mathrm { S o } B f _ { 1 } = g _ { 1 }$ and $Bh = 0   if   h \perp f_1$ . Thus $BTAh = 0   if   h \perp g_0$ and $B T A g _ { 0 } = g _ { 1 }$ . Hence for any pair of nonzero vectors $g _ { 0 } , g _ { 1 }$ in $\mathcal { H }$ the rank-one operator that takes $g _ { 0 }$ to $g _ { 1 }$ and is zero on $[ g _ { 0 } ] ^ { \perp }$ belongs to $I .$ From here it easily follows that I contains all finite-rank operators. Since I is closed, $I   \supseteq   \mathcal { B } _ { 0 } ( \mathcal { H } )$

It will be shown in (IX.4.2), after we have spectral theorem, that if I is a closed ideal in $\mathcal { B } ( \mathcal { H } )$ and $\mathcal { H }$ is separable, then $I = ( 0 ) , \mathcal { B } _ { 0 } ( \mathcal { H } ) ,$ , or $\mathcal { B } ( \mathcal { H } )$

## EXERCISES

1. Complete the proof of Proposition 4.9.

2. Show that $M _ { n } ( \mathbb { C } )$ has no nontrivial ideals. Find all of the left ideals.

3. If α is an infinite cardinal number, let $I _ { \alpha } = \{ A \in \mathcal { B } ( \mathcal { H } )$ dim cl(ran $A ) \leqslant \alpha )$ . Show that $I _ { \alpha }$ is a closed ideal in $\mathcal { B } ( \mathcal { H } )$

4. Let S be the unilateral shift on $l ^ { 2 } .$ Show that $C ^ { * } ( S ) \supseteq \mathcal { B } _ { 0 } ( l ^ { 2 } )$ and $C ^ { * } ( S ) / \mathcal { B } _ { 0 } ( l ^ { 2 } )$ is abelian. Show that the maximal ideal space of $C ^ { * } ( S ) / \mathcal { B } _ { 0 } ( l ^ { 2 } )$ is homeomorphic to ∂D.

5. If V is the Volterra operator on $L ^ { 2 } ( 0 , 1 )$ , show that $C ^ { * } ( V ) = \mathbb { C } + \mathcal { B } _ { 0 } ( L ^ { 2 } ( 0 , 1 ) ) .$

6. If $\nsim$ is a $C ^ { * }$ -algebra, I is a closed ideal of $\alpha ,$ and $\pmb { \mathscr { B } }$ is a $C ^ { * }$ -subalgebra of $\varkappa ,$ show that the C\*-algebra generated by $I \cup \mathcal { B }$ $I + { \mathcal { B } } .$

7. If $\sphericalangle$ is a C\*-algebra and I and J are closed ideals in $\alpha ,$ show that $I + J$ is a closed ideal of $\nsim$

# $\S 5 ^ { * }$ Representations of $C ^ { * } - A I$ gebras and the Gelfand-Naimark-Segal Construction

5.1. Definition. A representation of a $C ^ { * } \mathtt { - a l g e b e r a }$ is a pair $( \pi , \mathcal { H } )$ , where $\mathcal { H }$ is a Hilbert space and π: $\mathcal { A } \rightarrow \mathcal { B } ( \mathcal { H } )$ is a \*-homomorphism. If  has an identity, it is assumed that $\pi ( 1 ) = 1$ . (The algebras considered in this book are assumed to have an identity. The reader should be aware that not all authors make this assumption and so he should be cautious when consulting the literature.) Often mention of is suppressed and we say that π is a representation. $\mathcal { H }$

5.2. Example. If $\mathcal { H }$ is a Hilbert space and $\varkappa$ is a $C ^ { * }$ -subalgebra of $\mathcal { B } ( \mathcal { H } )$ then the inclusion map $\mathcal { A } \hookrightarrow \mathcal { B } ( \mathcal { H } )$ is a representation.

5.3. Example. If n is any cardinal number and $\mathcal { H }$ is a Hilbert space, let $\mathcal { H } ^ { ( n ) }$ denote the direct sum of $\mathcal { H }$ with itself n times. If $A   \in   \mathcal { B } ( \mathcal { H } )$ , then $A ^ { ( n ) }$ is the direct sum of A with itself n times; so $A^{(n)} \in \mathcal{B}(\mathcal{H}^{(n)})$ and $\| A ^ { ( n ) } \| = \| A \|$ . The operator $A ^ { ( n ) }$ is called the inflation of A. If $\pi \colon \mathcal { A } \to \mathcal { B } ( \mathcal { H } )$ is a representation, the inflation of $\pi$ is the map $\pi ^ { ( n ) } \colon { \mathcal { A } } \to { \mathcal { B } } ( { \mathcal { H } } ^ { ( n ) } )$ defined by $\pi ^ { ( n ) } ( a ) = \pi ( a ) ^ { ( n ) }$ for all a in $\measuredangle$

5.4. Example. If $( X , \Omega , \mu )$ is a σ-finite measure space and ${ \mathcal { H } } = L ^ { 2 } ( \mu )$ , then $\pi \cdot$ $L ^ { \infty } ( \mu ) \to { \mathcal { B } } ( { \mathcal { H } } )$ defined by $\pi ( \phi ) = M _ { \phi }$ is a representation.

5.5. Example. If X is a compact space and μ is a positive Borel measure on X, then π: $C ( X ) \to { \mathcal { B } } ( L ^ { 2 } ( \mu ) )$ defined by $\pi ( f )   =   M _ { f }$ is a representation.

5.6. Definition. A representation π of a C\*-algebra $\varkappa$ is cyclic if there is a vector $e$ in $\mathcal { H }$ such that cl $[ \pi ( \mathcal { A } ) e ] = \mathcal { H } ;$ e is said to be a cyclic vector for the representation π.

Note that the representations in Examples 5.4 and 5.5 are cyclic (Exercises 2 and 3). Also, the identity representation i: $\mathcal { B } ( \mathcal { H } ) \rightarrow \mathcal { B } ( \mathcal { H } )$ is cyclic and every nonzero vector is a cyclic vector for this representation. If $\mathcal { A } = \mathbb { C } + \mathcal { B } _ { 0 } ( \mathcal { H } )$ then the identity representation is cyclic. On the other hand, if $n \geqslant 2 ,$ then the inflation $\pi ^ { ( n ) }$ of a representation of $C ( X )$ is never cyclic (Exercise 4).

There is another way to obtain representations.

5.7. Definition. If $\{ ( \pi _ { i } , \mathcal { H } _ { i } ) : i { \in } I \}$ is a family of representations of $\alpha ,$ then the direct sum of this family is the representation $( \pi , \mathcal { H } )$ , where $\mathcal { H } = \oplus _ { i } \mathcal { H } _ { i }$ and $\pi ( a ) = \{ \pi _ { i } ( a ) \}$ for every a in $\not { x } ,$

Note that since $\| \pi _ { i } ( a ) \| \leqslant \| a \|$ for every i (4.8), π(a) is a bounded operator on $\mathcal { H }$ . It is easy to check that π is a representation.

5.8. Example. Let X be a compact space and let $\{ \mu _ { n } \}$ be a sequence of measures on X. For each n let $\pi _ { n } : C ( X ) \to { \mathcal { B } } ( L ^ { 2 } ( \mu _ { n } ) )$ be defined by $\pi _ { n } ( f ) = M _ { f }$ on $L ^ { 2 } ( \mu _ { n } )$ .Then $\pi = \oplus _ { n } \pi _ { n }$ is a representation. If the measures $\{ \mu _ { n } \}$ are pairwise mutually singular, then π is equivalent (below) to the representation $f   \rightarrow   M _ { f }$ of $C ( X ) \to { \mathcal { B } } ( L ^ { 2 } ( \mu ) )$ , where $\mu = \sum_{n = 1}^{\infty} \mu_{n} / 2^{n} \left\| \mu_{n} \right\|$ (Exercise 5).

The concept of equivalence for representations is that of unitary equivalence. That is, two representations of a $c * - a l$ gebra $\mathcal { A } ,   ( \pi _ { 1 } , \mathcal { H } _ { 1 } )$ and $( \pi _ { 2 } , \mathcal { H } _ { 2 } ) ,$ are equivalent if there is an isomorphism $U \colon \mathcal { H } _ { 1 }   \to   \mathcal { H } _ { 2 }$ such that $U \pi _ { 1 } ( a ) U ^ { - 1 } = \pi _ { 2 } ( a )$ for every a in $\prec$ The importance of cyclic representations arises from the fact, given in the next result, that every representation is equivalent to the direct sum of cyclic representations.

5.9. Theorem. If π is a representation of the C\*-algebra $\alpha ,$ then there is a family of cyclic representations $\left\{ \pi _ { i } \right\}$ of Asuch thatπ and $\textcircled{9}  { } _ { i } \pi _ { i }$ are equivalent.

PROOF. let $\mathcal { S } =$ the collection of all subsets E of nonzero vectors in $\mathcal { H }$ such that $\pi ( \mathcal { A } ) e \perp \pi ( \mathcal { A } ) f$ for $e , f$ in E with $e \neq f$ . Order $\mathcal { E }$ by inclusion. An