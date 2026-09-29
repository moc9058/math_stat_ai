PROOF. $(c) \Rightarrow (a);$ This is immediate from (4.2b) and the fact that $\mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } ) \subseteq \mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$

$(a) \Rightarrow (c);$ Since cl $\left[ T ( { \mathrm { b a l l } } { \mathcal { H } } ) \right]$ is compact, it is separable. Therefore cl $( \operatorname { r a n } T ) = { \mathcal { L } }$ is a separable subspace of $\mathcal { H }$ . Let $\{ e _ { 1 } , e _ { 2 } , \ldots \}$ be a basis for $\mathcal { L }$ and let $P _ { n }$ be the orthogonal projection of $\mathcal { H }$ onto $\vee \left\{ e_{j} : 1 \leqslant j \leqslant n \right\}$ . Put $T _ { n } = P _ { n } T ;$ note that each $T _ { n }$ has finite rank. It will be shown that $\| T _ { n } - T \| \to 0$ but first we prove the following:

Claim. If $h \in \mathcal { H } , \| T _ { n } h - T h \| \rightarrow 0 .$

In fact, $k = T h \in { \mathcal { L } } ,$ so $\| P _ { n } k - k \| \to 0$ by (I.4.13d) and (I.4.7). That is, $\| P _ { n } T h - T h \| \to 0$ and the claim is proved.

Since T is compact, if $\varepsilon   >   0 ,$ , there are vectors $h _ { 1 } , \ldots , h _ { m }$ in ball $\mathcal { H }$ such that T(ball $\mathcal { H } ) \subseteq \bigcup _ { j = 1 } ^ { m } B ( T h _ { j } ; \varepsilon / 3 )$ So if $\| h \| \leqslant 1$ , choose $h _ { j }$ with $\| T h - T h _ { j } \| < \varepsilon / 3$ . Thus for any integer n,

$$
\begin{align*}\|   Th - T_n h \| & \leqslant \|   Th - T h_j \| + \|   Th_j - T_n h_j \| + \|   P_n (T h_j - T h) \| \\& \leqslant 2 \|   Th - T h_j \| + \|   Th_j - T_n h_j \| \\& \leqslant 2 \varepsilon / 3 + \|   Th_j - T_n h_j \|.\end{align*}
$$

Using the claim we can find an integer $n _ { 0 }$ such that $\| T h _ { j } - T _ { n } h _ { j } \| < \varepsilon / 3$ for $1 \leqslant j \leqslant$ m and $n \geqslant n_{0}. \mathrm{So} \parallel T h - T_{n} h \parallel < \varepsilon$ uniformly for h in ball $\mathcal { H }$ . Therefore $\| T - T _ { n } \| < \varepsilon$ for $n \geqslant n _ { 0 }$

$(c) \Rightarrow (b) : \mathrm{If} \left\{ T_n \right\}$ is a sequence in $\mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } )$ such that $\| T _ { n } - T \| \to 0 ,$ then $\| T _ { n } ^ { * } - T ^ { * } \| = \| T _ { n } - T \| \rightarrow 0 .$ But $T _ { n } ^ { * } { \in } \mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } )$ (Exercise 3). Since (c) implies (a), $T ^ { * }$ is compact.

(b)⇒(a): Exercise.

A fact emerged in the proof that (a) implies (c) in the preceding theorem that is worth recording.

4.5. Corollary. If $T   \in   \mathcal { B } _ { 0 } ( \mathcal { H } , \mathcal { H } )$ , then cl(ran T) is separable and $\textit { i f } \left\{ e _ { n } \right\}$ is a basis for cl(ran T) and $P _ { n }$ is the projection of $\mathcal { H }$ onto $\lor \left\{ e_{j} : 1 \leqslant j \leqslant n \right\}$ , then $\| P _ { n } T - T \| \to 0 .$

4.6. Proposition. Let $\mathcal { H }$ be a separable Hilbert space with basis $\{ e _ { n } \}$ ; let $\{ \alpha _ { n } \} \subseteq \mathbb { F } \text { w i t h } M = \sup \{ | \alpha _ { n } | : n \geqslant 1 \} < \infty . \text { I f } A e _ { n } = \alpha _ { n } e _ { n } \text { f o r }$ all n, then A extends by linearity to a bounded operator on  with $\| { \pmb A } \| = M$ . The operator A is compact if and only $if   \alpha_n \to 0   as   n \to \infty$

PRoOF. The fact that A is bounded and $\| A \| = M$ is an exercise; such an operator is said to be diagonalizable (see Exercise 1.8). Let $P _ { n }$ be the projection of $\mathcal { H }$ onto $\vee \; \{ e _ { 1 } , \ldots , e _ { n } \}$ . Then $A_{n}=A-AP_{n}$ is seen to be diagonalizable with $A _ { n } e _ { j } = \alpha _ { j } e _ { j } \quad \mathrm { i f } \quad j > n$ and $A _ { n } e _ { j }   =   0$ if $j \leqslant n$ So A $P _ { n } \in \mathcal { B } _ { 0 0 } ( \mathcal { H } )$ and $\| A_n \| = \sup \{ | \alpha_j | : j > n \}$ . If $\alpha _ { n }   \to   0 .$ then $\| A _ { n } \|   \to   0$ and so A is compact since it is the limit of a sequence of finite-rank operators. Conversely, if A is compact, then Corollary 4.5 implies $\| A _ { n } \|   \to   0 ;$ hence $\alpha _ { n }   \to   0$ ■

4.7. Proposition. $I f \left( X , \Omega , \mu \right)$ is a measure space and $k { \in } L ^ { 2 } ( X \times X , \mathbf { \Omega } \times \mathbf { \Omega } , \mu \times \mu ) ,$ then

$$
(Kf)(x) = \int k(x,y)f(y)d\mu(y)
$$

is a compact operator and $\| K \| \leqslant \| k \| _ { 2 }$

The following lemma is useful for proving this proposition. The proof is left to the reader.

4.8. Lemma. $I f \left\{ e _ { i } \colon i { \in } I \right\}$ is a basis for $L ^ { 2 } ( X , \Omega , \mu )$ and

$$
\phi _ { i j } ( x , y ) = e _ { j } ( x ) e _ { i } ( y )
$$

for $i , j$ in I and $x , y$ in $X ,$ then $\{ \phi _ { i j } { : } i , j { \in } I \}$ is an orthonormal set in $L ^ { 2 } ( X \times X ,$ $\boldsymbol { \Omega } \times \boldsymbol { \Omega } , \quad \mu \times \mu )$ . If k and K are as in the preceding proposition, then $\langle k , \phi _ { i j } \rangle = \langle K e _ { j } , e _ { i } \rangle$

PRoOF OF PROPOsITION 4.7. First we show that K defines a bounded operator. In fact, if $f \in L^{2}(\mu), \|Kf\|^{2} = \int \left| \int k(x,y)f(y)d\mu(y) \right|^{2} d\mu(x) \leqslant \int \left( \int \left| k(x,y) \right|^{2} d\mu(y) \right)^{2}$ $\left( \int | f ( y ) | ^ { 2 } d \mu ( y ) \right) d \mu ( x ) = \| k \| ^ { 2 } \| \dot { f } \| ^ { 2 }$ .Hence K is bounded and $\| K \| \leqslant \| k \| _ { 2 }$ Now let $\left\{ e _ { i } \right\}$ be a basis for $L ^ { 2 } ( \mu )$ and define $\phi _ { i j }$ as in Lemma 4.8. Thus

$$
\| k \| ^ { 2 } \geqslant \sum _ { i , j } | \langle k , \phi _ { i j } \rangle | ^ { 2 } = \sum _ { i , j } | \langle K e _ { j } , e _ { i } \rangle | ^ { 2 } .
$$

Since $k { \in } L ^ { 2 } ( \mu \times \mu )$ , there are at most a countable number of i and j such that $\langle k , \phi _ { i j } \rangle \neq 0 ;$ denote these by $\left\{ \psi _ { k m } : 1 \leqslant k , m < \infty \right\}$ . Note that $\langle K e _ { j } , e _ { i } \rangle = 0$ unless $\phi _ { i j } { \in } \{ \psi _ { k m } \}$ . Let $\psi _ { k m } ( x , y ) = e _ { k } ( x ) e _ { m } ( y ) .$ , let $P _ { n }$ be the orthogonal projection onto $\lor \left\{ e_{k} : 1 \leqslant k \leqslant n \right\}$ , and put $K_{n}=KP_{n}+P_{n}K-P_{n}KP_{n};$ so $K _ { n }$ is a finite rank operator. We will show that $\| K - K _ { n } \|   \to   0$ as $n   \to   \infty$ , thus showing that K is compact.

Let $f   \in   L ^ { 2 } ( \mu )$ with $\| f \| ^ { 2 } \leqslant 1 ;$ SO $\begin{array} { r } { f = \sum _ { j } \alpha _ { j } e _ { j } , } \end{array}$ Hence

$$
\begin{align*}\| K f - K_n f \|^2 = & \sum_i | \langle K f - K_n f, e_i \rangle |^2 \\= & \sum_i \left| \sum_j \alpha_j \langle (K - K_n) e_j, e_i \rangle \right|^2 \\= & \sum_k \left| \sum_m \alpha_m \langle (K - K_n) e_m, e_k \rangle \right|^2 \\\leqslant & \sum_k \left[ \sum_m | \alpha_m |^2 \right] \left[ \sum_m | \langle (K - K_n) e_m, e_k \rangle |^2 \right].\end{align*}
$$

$$
\begin{aligned} &\leqslant \| f \| ^ { 2 } \sum _ { k } \sum _ { m } \left| \left\langle K e _ { m } , e _ { k } \right\rangle - \left\langle K P _ { n } e _ { m } , P _ { n } e _ { k } \right\rangle \right| ^ { 2 }\\ &\quad - \left\langle K P _ { n } e _ { m } , P _ { n } e _ { k } \right\rangle + \left\langle K P _ { n } e _ { m } , P _ { n } e _ { k } \right\rangle | ^ { 2 }\\ &= \sum _ { k = n + 1 } ^ { \infty } \sum _ { m = n + 1 } ^ { \infty } \left| \left\langle K e _ { m } , e _ { k } \right\rangle \right| ^ { 2 }\\ &= \sum _ { k = n + 1 } ^ { \infty } \sum _ { m = n + 1 } ^ { \infty } \left| \left\langle k , \psi _ { k m } \right\rangle \right| ^ { 2 } .\\ \end{aligned}
$$

Since $\begin{array} { r } { \sum _ { k , m } | \langle k , \psi _ { k m } \rangle | ^ { 2 } < \infty } \end{array}$ , n can be chosen sufficiently large such that for any $\varepsilon   >   0$ this last sum will be smaller than $\varepsilon ^ { 2 }$ Thus $\left\| K - K _ { n } \right\| \rightarrow 0 .$

In particular, note that the preceding proposition shows that the Volterra operator (1.7) is compact.

One of the dominant tools in the study of linear transformation on finite dimensional spaces is the concept of eigenvalue.

4.9. Definition. If $A   \in   \mathcal { B } ( \mathcal { H } )$ , a scalar α is an eigenvalue of A if ker $( A - \alpha ) \neq ( 0 )$ If h is a nonzero vector in $\ker ( A - \alpha )$ , h is called an eigenvector for $\alpha ,$ thus $A h = \alpha h .$ Let $\sigma _ { p } ( A )$ denote the set of eigenvalues of A.

4.10. Example. Let A be the diagonalizable operator in Proposition 4.6. Then $\sigma _ { p } ( A ) = \{ \alpha _ { 1 } , \alpha _ { 2 } , \ldots \}$ . If ${ \alpha } { \in } { \sigma } _ { p } ( A ) ,$ let $J _ { \alpha } = \{ j \in \mathbb { N } : \alpha _ { j } = \alpha \}$ . Then h is an eigenvector for α if and only if $\scriptstyle { \boldsymbol { h } } \in   { \mathsf { V } } \; \{ e _ { j } : \; j \in J _ { \alpha } \}$

4.11. Example. The Volterra operator has no eigenvalues.

4.12. Example. Let $h \in \mathcal { H } = L _ { \mathbb { C } } ^ { 2 } ( - \pi , \pi )$ and define $K : \mathcal { H } \to \mathcal { H }$ by $(Kf)(x) =$ $( 2 \pi ) ^ { - 1 / 2 } \int _ { - \pi } ^ { \pi } h ( x - y ) f ( y ) d y$ If $\lambda _ { n } = ( 2 \pi ) ^ { - 1 / 2 } \int _ { - \pi } ^ { \pi } h ( x ) \exp ( - i n x ) d x = \hat { h } ( n ) .$ the nth Fourier coefficient of h, then $\boldsymbol { K } \boldsymbol { e } _ { n } = \lambda _ { n } \boldsymbol { e } _ { n }$ , whëre $e _ { n } ( x ) = ( 2 \pi ) ^ { - 1 / 2 } \exp ( - i n x )$

The way to see this is to extend functions in $L _ { \mathfrak { C } } ^ { 2 } ( - \pi , \pi )$ to IR by periodicity and perform a change of variables in the formula for $( K e _ { n } ) ( x )$ .The details are left to the reader.

Operators on finite dimensional spaces over C always have eigenvalues. As the Volterra operator illustrates, the analogy between operators on finite dimensional spaces and compact operators breaks down here. If, however, a compact operator has an eigenvalue, several nice things can be said if the eigenvalue is not zero.

4.13. Proposition. If $T   \in   \mathcal { B } _ { 0 } ( \mathcal { H } )$ $\lambda   \in   \sigma _ { p } ( T )$ , and $\lambda \neq 0$ , then the eigenspace ker $( T - \lambda )$ is finite dimensional.

ProoF. Suppose there is an infinite orthonormal sequence $\{ e _ { n } \}$ in ker $( T - \lambda )$ Since T is compact, there is a subsequence $\{ e _ { n _ { k } } \}$ such that $\{ T e _ { n _ { k } } \}$ converges.

Thus, $\{ T e _ { _ { n _ { k } } } \}$ is a Cauchy sequence. But for $n _ { k } \neq n _ { j } , \quad \| T e _ { n _ { k } } - T e _ { n _ { j } } \| ^ { 2 } =$ $\| \lambda e_{n_k} - \lambda e_{n_j} \|^2 = 2 |\lambda|^2 > 0$ since $\lambda \neq 0$ This contradiction shows that ker $( T - \lambda )$ must be finite dimensional.

The next result on the existence of eigenvalues is not a practical way to show that a specific example has a nonzero eigenvalue, but it is a good theoretical tool that will be used later in this book (in particular, in the next section).

4.14. Proposition. If T is a compact operator on $\mathcal { H } , \lambda \neq 0 ,$ , and inf $\{ \| ( T - \lambda ) \boldsymbol { h } \|$二 $\left\| \boldsymbol{h} \right\| = 1 \} = 0$ , then $\lambda   \in   \sigma _ { p } ( T )$

ProoF. By hypothesis, there is a sequence of unit vectors $\{ h _ { n } \}$ such that $\| ( T - \lambda ) h _ { n } \| \to 0 .$ Since T is compact, there is a vector f in  and a subsequence $\left\{ h _ { n _ { k } } \right\}$ such that $\| T h _ { n _ { k } } - f \| \to 0$ . But $h _ { n _ { k } } = \lambda ^ { - 1 } \left[ ( \lambda - T ) h _ { n _ { k } } + T h _ { n _ { k } } \right] \rightarrow$ $i ^ { - 1 } f$ So $\hat { 1 } = \| \lambda ^ { - 1 } f \| = | \lambda | ^ { - 1 } \| f \|$ and $f \neq 0 .$ Also, it must be that $\overrightarrow{Th_{n_k}} \rightarrow \lambda^{-1}Tf$ Since $T h _ { n _ { k } } \rightarrow f , f = \lambda ^ { - 1 } T f ,$ or $T f   =   \lambda f .$ That is, $f { \in } \ker ( T - \lambda )$ and $f \neq 0 ,$ so $\lambda { \in } \sigma _ { p } ( T )$ ■

4.15. Corollary. If T is a compact operator on $\mathcal { H } , \lambda \neq 0 , \lambda \notin \sigma _ { p } ( T ) ,$ and $\bar { \lambda } { \notin } \sigma _ { p } ( T ^ { * } )$ , then ran $( T - \lambda ) = \mathcal { H }$ and $( T - \lambda ) ^ { - 1 }$ is a bounded operator on $\mathcal { H } .$

PROOF. Since $\lambda { \notin } \sigma _ { p } ( T )$ , the preceding proposition implies that there is a constant $c   >   0$ such that $\| (T - \lambda) h \| \geqslant c \| h \|$ for all h in $\mathcal { H }$ . If $f \in \mathrm{cl} \tan(T - \lambda)$ , then there is a sequence $\{ h _ { n } \}$ in $\mathcal { H }$ such that $( T - \lambda ) h _ { n } \to f$ Thus $\| h _ { n } - h _ { m } \| \leqslant c ^ { - 1 } \| ( T - \lambda ) h _ { n } - ( T - \lambda ) h _ { m } \|$ and so $\{ h _ { n } \}$ is a Cauchy sequence. Hence $h _ { n }   \rightarrow   h$ for some h in $\mathcal { H }$ . Thus $( T - \lambda ) h = f$ . So ran $( T - \lambda )$ is closed and, by (2.19), ran $(T - \lambda) = \left[ \ker(T - \lambda)^* \right]^\perp = \mathcal{H}$ , by hypothesis.

So for f in $\mathcal { H }$ let $Af = \mathrm{the}$ unique vector h such that $( T - \lambda ) h = f$ . Thus $(T - \lambda)Af = f$ for all f in . From the inequality above, $c \left\|   A f   \right\| \leqslant$ $\| ( T - \lambda ) A f \| = \| f \|$ . So $\| A f \| \leqslant c^{-1} \| f \|$ and A is bounded. Also, $(T - \lambda)A(T - \lambda)h = (T - \lambda)h, \quad \mathrm{so} \quad 0 = (T - \lambda)[A(T - \lambda)h - h]$ . Since $\lambda \not \in \sigma _ { p } ( T )$ $A ( T - \lambda ) h = h .$ That is, $A = ( T - \lambda ) ^ { - 1 }$ ■

It will be proved in a later chapter that if $\lambda \not \in \sigma _ { p } ( T )$ and $\lambda \neq 0 ,$ then $\bar { \lambda } \notin \sigma _ { p } ( T ^ { * } )$ More will be shown about arbitrary compact operators in Chapter VI. In the next section the theory of compact self-adjoint operators will be explored.

## EXERCISES

1. Prove Proposition 4.2(c).

2. Show that every operator of finite rank is compact.

3. If $T { \in } \mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } )$ , show that $T ^ { * } { \in } \mathcal { B } _ { 0 0 } ( \mathcal { H } , \mathcal { H } )$ and $\dim(\operatorname{ran} T) = \dim(\operatorname{ran} T^*)$

4. Show that an idempotent is compact if and only if it has finite rank.

5. Show that no nonzero multiplication operator on $L ^ { 2 } ( 0 , 1 )$ is compact.

6. Show that if $T \colon { \mathcal { H } } \to { \mathcal { H } }$ is a compact operator and $\{ e _ { n } \}$ is any orthonormal sequence in $\mathcal { H } ,$ then $\| T e _ { n } \| \to 0 .$ Is the converse true?

7. If T is compact and M is an invariant subspace for T, show that $T | \mathcal { M }$ is compact.

8. If $h , g \in \mathcal { H }$ , define T: $\mathcal { H } \rightarrow \mathcal { H }$ by $T f = \langle f , h \rangle g .$ Show that T has rank 1 [that is, dim(ran $T )   =   1 ]$ . Moreover, every rank 1 operator can be so represented. Show that if T is a finite rank operator, then there are orthonormal vectors $e _ { 1 } , \ldots , e _ { n }$ and vectors $g _ { 1 } , \ldots , g _ { n }$ such that $\begin{array} { r } { T h = \sum _ { j = 1 } ^ { n } \langle h , e _ { j } \rangle g _ { j } } \end{array}$ for all h in $\mathcal { H } .$ In this case show that T is normal if $g _ { j }   =   \lambda _ { j } e _ { j }$ for some scalars $\lambda _ { 1 } , \ldots , \lambda _ { n } .$ Find $\sigma _ { p } ( T )$

9. Show that a diagonalizable operator is normal.

10. Verify the statements in Example 4.10.

11. Verify the statement in Example 4.11.

12. Verify the statement in Example 4.12. (Note that the operator K in this example is diagonalizable.)

13. If $T _ { n } \in \mathcal { B } ( \mathcal { H } _ { n } ) , \; n \geqslant 1$ , with $\sup_{n} \| T_{n} \| < \infty$ and $T = \bigoplus_{n = 1}^{\infty} T_{n}$ on $\mathcal { H } = \bigoplus _ { n = 1 } ^ { \infty } \mathcal { H } _ { n } ,$ show that T is compact if and only if each $T _ { n }$ is compact and $\| T _ { n } \|   \to   0 .$

14. In Lemma 4.8, show that if $L ^ { 2 } ( X , \Omega , \mu )$ is separable, then $\left\{ \varphi _ { i j } \right\}$ is a basis for $L ^ { 2 } ( X \times X ,   \Omega \times \Omega ,   \mu \times \mu )$ .What if $L ^ { 2 } ( X , \Omega , \mu )$ is not separable?

## $\S 5 ^ { * }$ The Diagonalization of Compact Self-Adjoint Operators

This section and the remaining ones in this chapter may be omitted if the reader intends to continue through to the end of this book, as the material in these sections (save for Section 6) will be obtained in greater generality in Chapter IX. It is worthwhile, however, to examine this material even if Chapter IX is to be read, since the intuition provided by this special case is valuable.

The main result of this section is the following.

5.1. Theorem. If T is a compact self-adjoint operator on $\mathcal { H } .$ , then T has only a countable number of distinct eigenvalues. $\mathit { I f } \{ \lambda _ { 1 } , \lambda _ { 2 } , \ldots \}$ are the distinct nonzero eigenvalues of T, and $P _ { n }$ is the projection of $\mathcal { H }$ onto ker $( T - \lambda _ { n } )$ then $P _ { n } P _ { m } = P _ { m } P _ { n } = 0$ if $n \neq m ,$ each $\lambda _ { n }$ is real, and

## 5.2

$$
T = \sum _ { n = 1 } ^ { \infty } \lambda _ { n } P _ { n } ,
$$

where the series converges to T in the metric defined by the norm of $\mathcal { B } ( \mathcal { H } )$ [Of course, (5.2) may be only a finite sum.]

The proof of Theorem 5.1 requires a few preliminary results. Before beginning this process, let's look at a few consequences.

## 5.3. Corollary. With the notation of (5.1):

(a) ker $T = \left[ \vee \left\{ P_n \mathcal{H} : n \geqslant 1 \right\} \right]^{\perp} = (\mathrm{ran} T)^{\perp};$

(b) each $P _ { n }$ has finite rank;

(c) || $\| T \| = \sup \{ | \lambda _ { n } | : n \geqslant 1 \}$ and $\lambda _ { n }   \to   0$ as $n   \to   \infty$

PROOF. Since $P _ { n } \bot P _ { m }$ for $n \neq m ,$ if $h \in \mathcal { H } _ { 1 }$ , then (5.2) implies $\| T h \| ^ { 2 } =$ $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \| \lambda _ { n } \boldsymbol { P } _ { n } \boldsymbol { h } \| ^ { 2 } = \sum _ { n = 1 } ^ { \infty } | \lambda _ { n } | ^ { 2 } \| \boldsymbol { P } _ { n } \boldsymbol { h } \| ^ { 2 } } \end{array}$ . Hence $T h = 0$ if and only if $P _ { n } h = 0$ for all n. That is, h∈ker T if and only if $h \bot P _ { n } \mathcal { H }$ for all n, whence (a)

Part (b) follows by Proposition 4.13.

For part (c), if $\mathcal { L } = \mathrm { c l } [ \mathrm { r a n } T ] , \mathcal { L }$ is invariant for T. Since $T = T ^ { * }$ $\mathcal { L } = ( \ker T ) ^ { \perp }$ and $\mathcal { L }$ reduces T. So we can consider the restriction of $T$ to $\mathcal { L } ,   T | \mathcal { L }$ Now $\mathcal { L } = \vee \left\{ P _ { n } \mathcal { H } \colon n \geqslant 1 \right\}$ by (a). Let $\left\{ e_{j}^{(n)}: 1 \leqslant j \leqslant N_{n} \right\}$ be a basis for $P _ { n } \mathcal { H } = \ker ( T - \lambda _ { n } )$ , so $T e _ { j } ^ { ( n ) } = \lambda _ { n } e _ { j } ^ { ( n ) }$ for $1 \leqslant j \leqslant \dot { N } _ { n }$ Thus $\left\{ e _ { j } ^ { ( n ) } : 1 \leqslant j \leqslant N _ { n } \right\}$ $n \geqslant 1 \}$ is a basis for $\mathcal { L }$ and $T | \mathcal { L }$ is diagonalizable with respect to this basis. Part (c) now follows by (4.6). ■

The proof of (c) in the preceding corollary revealed an interesting fact that deserves a statement of its own.

5.4. Corollary. If T is a compact self-adjoint operator, then there is a sequence $\{ \mu _ { n } \}$ of real numbers and an orthonormal basis $\{ e _ { n } \}$ for (ker $T ) ^ { \perp }$ such that for all h,

$$
T h = \sum _ { n = 1 } ^ { \infty } \mu _ { n } \langle h , e _ { n } \rangle e _ { n } .
$$

Note that there may be repetitions in the sequence $\{ \mu _ { n } \}$ in (5.4). How many repetitions?

5.5. Corollary. If $T   \in   \mathcal { B } _ { 0 } ( \mathcal { H } ) ,   T = T ^ { * }$ , and ker $T = ( 0 ) ,$ then $\mathcal { H }$ is separable.

Also note that by (4.6), if (5.2) holds, $T   \in   \mathcal { B } _ { 0 } ( \mathcal { H } )$

To begin the proof of Theorem 5.1, we prove a few results about not necessarily compact operators.

5.6. Proposition. If A is a normal operator and $\lambda \in \mathbf { F } ,$ then ker $( A - \lambda ) =$ ker $( A - \lambda ) ^ { * }$ and ker $( A - \lambda )$ is a reducing subspace for A.

PRooF. Since A is normal, so is $A - \lambda$ Hence $\| ( A - \lambda ) h \| = \| ( A - \lambda ) ^ { * } h \|$ (2.16). Thus ker $(A - \lambda) = \ker(A - \lambda)^*$ . If heker $( A - \lambda )$ $A h = \lambda h \in \ker ( A - \lambda )$ . Also $A^{*}h = \bar{\lambda}h \in \ker(A - \lambda)$ . Therefore ker $( A - \lambda )$ reduces A. ■

5.7. Proposition. If A is a normal operator and $\lambda , \mu$ are distinct eigenvalues of A, then ker $( A - \lambda ) \bot \ker ( A - \mu )$

PROOF. If h∈ker $( A - \lambda )$ and $g { \in } \ker ( A - \mu ) ,$ then the fact (5.6) that $A ^ { * } g = \bar { \mu } g$ implies that $\lambda \left\langle \boldsymbol{h}, \boldsymbol{g} \right\rangle = \left\langle \boldsymbol{A} \boldsymbol{h}, \boldsymbol{g} \right\rangle = \left\langle \boldsymbol{h}, \boldsymbol{A}^* \boldsymbol{g} \right\rangle = \left\langle \boldsymbol{h}, \bar{\mu} \boldsymbol{g} \right\rangle = \mu \left\langle \boldsymbol{h}, \boldsymbol{g} \right\rangle$ Thus $( \lambda - \mu ) \langle h , g \rangle = 0 .$ Since $\lambda - \mu \neq 0,   h \perp g.$ ■

## 5.8. Proposition. If $A = A ^ { * }$ and $\lambda   \in   \sigma _ { p } ( A ) .$ , then λ is a real number.

PROOF. If $A h = \lambda h$ then $A h = A ^ { * } h = \overline { { \lambda } } h$ by (5.6). So $( \lambda - \tilde{\lambda} ) h = 0$ . Since h can be chosen different from $0 , \lambda = \bar { \lambda }$

The main result prior to entering the proof of Theorem 5.1 is to show that a compact self-adjoint operator has nonzero eigenvalues. If (5.3c) is examined, we see that there is a $\lambda _ { n }$ in $\sigma _ { p } ( T )$ with $| \lambda _ { n } | = \| T \|$ . Since the preceding proposition says that $\lambda _ { n } \in \mathbb { R }$ , it must be that $\lambda _ { n } = \pm \parallel T \parallel$ . That is, either $\pm \parallel   \pm \pm \sigma _ { p } ( T )$ . This is the key to showing that $\sigma _ { p } ( T )$ is nonvoid.

5.9. Lemma. If T is a compact self-adjoint operator, then either $\pm   \|   T   \|$ is an eigenvalue of T.

PROOF. If $T = 0 ,$ the result is clear. So suppose $T \neq 0 .$ By Proposition 2.13 there is a sequence $\{ h _ { n } \}$ of unit vectors such that $| \langle T h _ { n } , h _ { n } \rangle | \to \| T \|$ . By passing to a subsequence if necessary, we may assume that $\langle T h _ { n } , h _ { n } \rangle \to \lambda ,$ where $| \lambda | = \| T \|$ . It will be shown that $\lambda   \in   \sigma _ { p } ( T )$ .Since $| \lambda | = \| T \| , 0 \leqslant \| ( T - \lambda ) h _ { n } \| ^ { 2 } =$一 $\| T h _ { n } \| ^ { 2 } - 2 \lambda \langle T h _ { n } , h _ { n } \rangle + \lambda ^ { 2 } \leqslant 2 \lambda ^ { 2 } - 2 \lambda \langle T h _ { n } , h _ { n } \rangle \rightarrow 0$ . Hence $\| ( T - \lambda ) h _ { n } \| \to 0 .$ By $( 4 . 1 4 ) ,   \lambda { \in } \sigma _ { p } ( T )$

PROOF OF THEOREM 5.1. By Lemma 5.9 there is a real number $\lambda _ { 1 }$ in $\sigma _ { p } ( T )$ with $| \lambda _ { 1 } | = \| \boldsymbol { T } \|$ . Let $\mathcal{S}_{1} = \ker(T - \lambda_{1}), P_{1} =$ the projection onto $\mathcal { E } _ { 1 } , \mathcal { H } _ { 2 } = \mathcal { E } _ { 1 } ^ { \perp }$ By $( 5 . 6 ) ~ \ell _ { 1 }$ reduces T, so $\mathcal { H } _ { 2 }$ reduces T. Let $T _ { 2 } = T | \mathcal { H } _ { 2 } ;$ then $T _ { 2 }$ is a self-adjoint compact operator on $\mathcal{H}_{2}.(\mathrm{Why?})$

By (5.9) there is an eigenvalue $\lambda _ { 2 }$ for $T _ { 2 }$ such that $| \lambda _ { 2 } | = \| T _ { 2 } \|$ . Let $\mathcal { E } _ { 2 } = \ker ( T _ { 2 } - \lambda _ { 2 } )$ .Note that $(0) \neq \mathcal{E}_{2} \subseteq \ker(T - \lambda_{2})$ . If it were the case that $\lambda _ { 1 } = \lambda _ { 2 }$ , then $\mathcal { S } _ { 2 } \subseteq \ker ( T - \lambda _ { 1 } ) = \mathcal { S } _ { 1 }$ . Since $\ell _ { 1 } \bot \ell _ { 2 }$ , it must be that $\lambda _ { 1 } \neq \lambda _ { 2 }$ Let $P _ { 2 } = \mathrm { t h } \mathbf { e }$ projection of $\mathcal { H }$ onto $\mathcal { E } _ { 2 }$ and put $\mathcal { H } _ { 3 } = ( \mathcal { E } _ { 1 } \oplus \mathcal { E } _ { 2 } ) ^ { \perp }$ . Note that $\|   T _ { 2 }   \| \leqslant \|   T   \|$ so that $| \lambda _ { 2 } | \leqslant | \lambda _ { 1 } |$

Using induction (give the details) we obtain a sequence $\{ l _ { n } \}$ of real eigenvalues of T such that

(i) $| \lambda _ { 1 } | \geqslant | \lambda _ { 2 } | \geqslant \cdots ;$

$$
\mathrm { I f } \mathcal { E } _ { n } = \ker ( T - \lambda _ { n } ) , \left| \lambda _ { n + 1 } \right| = \left\| T \right| \left( \mathcal { E } _ { 1 } \oplus \cdots \oplus \mathcal { E } _ { n } \right) ^ { \perp } \left\| \mathcal { E } _ { 1 } \right\|
$$

By (i) there is a nonnegative number α such that $| \lambda _ { n } | \rightarrow \alpha .$

Claim. $\alpha = 0 ;$ that is, lim $\lambda _ { n } = 0 .$

In fact, let $e _ { n } { \in } { \mathcal { E } } _ { n } ,   \| e _ { n } \| = 1$ . Since $T$ is compact, there is an h in $\mathcal { H }$ and a subsequence $\{ e _ { n _ { j } } \}$ such that $\| T e _ { n _ { i } } - h \| \rightarrow 0 .$ But $e _ { n } \bot e _ { m }$ for $n \neq m$ and $T e _ { n _ { j } } = \lambda _ { n _ { j } } e _ { n _ { j } }$ . Hence $\left\| T e _ { n _ { j } } - T e _ { n _ { i } } \right\| ^ { 2 } = \lambda _ { n _ { j } } ^ { 2 } + \lambda _ { n _ { i } } ^ { 2 } \geqslant 2 \alpha ^ { 2 }$ . Since $\{ T e _ { n _ { j } } \}$ is a Cauchy sequence, $\alpha = 0$

Now put $P _ { n } =$ the projection of $\mathcal { H }$ onto $\mathcal { E } _ { n }$ and examine $\begin{array} { r } { T - \sum _ { j = 1 } ^ { n } \lambda _ { j } P _ { j } . } \end{array}$ If $h \in \mathcal { E } _ { k } , 1 \leqslant k \leqslant n ,$ then $\begin{array} { r } { ( T - \sum _ { j = 1 } ^ { n } \lambda _ { j } P _ { j } ) h = T h - \lambda _ { k } h = 0 . } \end{array}$ Hence $\stackrel{\circ}{\mathcal{E}}_{1}^{\cdot} \oplus \cdots \oplus$ $\mathcal { S } _ { n } \subseteq \ker ( T - \sum _ { j = 1 } ^ { n } \lambda _ { j } P _ { j } )$ If $h \in ( \mathcal { E } _ { 1 } \oplus \cdots \oplus \mathcal { E } _ { n } ) ^ { \perp }$ , then $P _ { j } h   =   0$ for $1 \leqslant j \leqslant n;$ sO $(T - \sum_{j = 1}^{n} \lambda_{j} P_{j}) h = T h$ .These two statements, together with the fact that $( \mathcal { E } _ { 1 } \oplus \cdots \oplus \mathcal { E } _ { n } ) ^ { \perp }$ reduces T, imply that

$$
\begin{align*}\left\| T - \sum_{j=1}^n \lambda_j P_j \right\| &= \|   T | (\mathcal{E}_1 \oplus \cdots \oplus \mathcal{E}_n)^\perp \| \\&= |\lambda_{n+1}| \to 0.\end{align*}
$$

Therefore the series $\sum _ { n = 1 } ^ { \infty } \lambda _ { n } P _ { n }$ converges in the metric of $\mathcal { B } ( \mathcal { H } )$ to T.■

Theorem 5.1 is called the Spectral Theorem for compact self-adjoint operators. Using it, one can answer virtually every question about compact hermitian operators, as will be seen before the end of this chapter.

If in Theorem 5.1 it is assumed that T is normal and compact, then the same conclusion, except for the statement that each $\lambda _ { n }$ is real, is true provided that  is a C-Hilbert space. The proof of this will be given in Section 7.

## EXERCISES

1. Prove Corollary 5.4.

2. Prove Corollary 5.5

3. Let K and k be as in Proposition 4.7 and suppose that $k ( x , y ) = k ( y , x )$ .Show that K is self-adjoint and if $\{ \mu _ { n } \}$ are the eigenvalues of K, each repeated dim ker $( K - \mu _ { n } )$ times, then $\textstyle \sum _ { 1 } ^ { \infty } | \mu _ { n } | ^ { 2 } < \infty$

4. If T is a compact self-adjoint operator and $\{ e _ { n } \}$ and $\{ \mu _ { n } \}$ are as in (5.4) and if h is a given vector in $\mathcal { H }$ , show that there is a vector f in $\mathcal { H }$ such that $T f = h$ if and only if h ⊥ ker T and $\begin{array} { r } { \sum _ { n } \mu _ { n } ^ { - 2 } | \langle h , e _ { n } \rangle | ^ { 2 } < \infty } \end{array}$ . Find the form of the general vector f such that $T f = h .$

5. Let $T ,   \{ \mu _ { n } \}$ , and $\{ e _ { n } \}$ be as in (5.4). If $\lambda \neq 0$ and $\lambda \neq \mu _ { n }$ for any $\mu _ { n } ,$ then for every h in  there is a unique f in $\mathcal { H }$ such that $( \lambda - T ) f = h$ Moreover, $f = \lambda^{-1} \left[ h + \sum_{n=1}^{\infty} \lambda_n (\lambda - \lambda_n)^{-1} \langle h, e_n \rangle e_n \right]$ . Interpret this when T is an integral operator.

## $\S 6 ^ { * }$ . An Application: Sturm-Liouville Systems

In this section, $[ a , b ]$ will be a proper interval with $- \; \infty < a < b < \infty . \; C [ a , b ]$ denotes the continuous functions $f \colon [ a , b ] \to \mathbb { R }$ and for $n \geqslant 1,C^{(n)}[a,b]$ denotes those functions in $C [ a , b ]$ that have n continuous derivatives. $C _ { \mathbb { C } } ^ { ( n ) } [ a , b ]$ denotes the corresponding spaces of complex-valued functions. We want to consider the differential equation

6.1

$$
- h ^ { \prime \prime } + q h - \lambda h = f ,
$$