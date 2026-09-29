14. Give an example of a TVS $\mathcal { R }$ that is not locally convex and a subspace @ of $\mathcal { X }$ such that there is a continuous linear functional f on $\pmb { g }$ with no continuous extension to $\mathcal { X } .$

15. Let ¿ be a real LCS and let A and B be disjoint compact convex subsets of ${ \mathcal { X } } .$ Suppose Y is a subspace of X and $f _ { 0 } : \mathcal { Y } \rightarrow \mathbb { R }$ is a continuous linear functional such that $f _ { 0 } ( a ) < 0$ for a in $A \cap \mathcal { Y }$ and $f _ { 0 } ( b ) > 0$ for b in $B \cap \mathcal { Y }$ Show by an example that it is not always possible to extend $f _ { 0 }$ to a continuous linear functional on X such that $f ( a ) < 0$ or a in A and $f ( b )   >   0$ for b in B. (Hint: Let $\mathcal { X }   =   \mathbb { R } ^ { 3 }$ and let @ be the plane.)

## ş $4 ^ { * }$ . Some Examples of the Dual Space of a Locally Convex Space

As with a normed space, if X is a LCS, $\mathcal { X } ^ { * }$ denotes the space of all continuous linear functionals $f \colon { \mathcal { X } }   \to   \mathbb { F } . ~ { \mathcal { X } } ^ { \star }$ is called the dual space of $\mathcal { X }$

4.1. Proposition. Let X be completely regular and let C(X) be topologized as in Example 1.5. If L: $C ( X )   \to   \mathbb { F }$ is a continuous linear functional, then there is a compact set K and a regular Borel measure $\mu$ on K such that $L ( f ) = \int _ { K } f d \mu$ for every f in C(X). Conversely, each such measure defines an element of ${ \mathsf { ^ { * } C } } ( X ) ^ { * }$

ProoF. It is easy to see that each measure μ supported on a compact set K defines an element of $C ( X ) ^ { * }$ . In fact, if $p _ { K } ( f ) = \operatorname* { s u p } \left\{ | f ( x ) | \right\}$ $x { \in } K \}$ and $L ( f ) = \int _ { K } f   d \mu ,$ then $| L ( f ) | \leqslant \| \mu \| p _ { K } ( f )$ , and so L is continuous.

Now assume $L { \in } C ( X ) ^ { * }$ . There are compact sets $K _ { 1 } , \ldots , K _ { n }$ and positive numbers $\alpha _ { 1 } , \ldots , \alpha _ { n }$ such that $\begin{array} { r } { | L ( f ) | \leqslant \sum _ { j = 1 } ^ { n } \alpha _ { j } p _ { K _ { j } } ( f ) } \end{array}$ (3.1f). Let $K = \bigcup _ { j = 1 } ^ { n } K _ { j }$ and α = max $\left\{ \alpha _ { j } : 1 \leqslant j \leqslant n \right\}$ . Then $| L ( \dot { f } ) | \leqslant \alpha p _ { K } ( f )$ . Hence if $f { \in } C ( { \widetilde { X ) } }$ and $f | K \equiv 0 ,$ then $\dot { L ( f ) }   =   0$

Define $F \colon C ( K ) \to \mathbb { F }$ as follows. If $g   \in   C ( K )$ , let $\tilde { g }$ be any continuous extension of g to X and put $F ( g ) = L ( \tilde { g } )$ . To check that F is well defined, suppose that $\tilde { g } _ { 1 }$ and $\tilde { g } _ { 2 }$ are both extensions of $g$ to X. Then $\tilde { g } _ { 1 } - \tilde { g } _ { 2 } = 0$ on $K$ , and hence $L ( \tilde { g } _ { 1 } )   =   L ( \tilde { g } _ { 2 } )$ Thus F is well defined. It is left as an exercise for the reader to show that $F \colon C ( K ) \to \mathbb { F }$ is linear. If $g   \in   C ( K )$ and $\tilde { g }$ is an extension in C(X). then $| F ( g ) | = | L ( \tilde { g } ) | \leqslant \alpha p _ { K } ( \tilde { g } ) = \alpha \| g \|$ , where the norm is the norm of C(K). By (III.5.7) there is a measure $\mu$ in $M ( K )$ such that $F ( g ) = \int _ { K } g   d \mu .$ If $f { \in } C ( X )$ 2 then $g = f \mid K \in C ( K )$ and so $L(f) = F(g) = \int_{K} f   d\mu$ ■

If $\gamma \colon [ 0 , 1 ]   \to   \pmb { \mathbb { C } }$ is a rectifiable curve and f is a continuous function defined on the trace of $\gamma ,   \gamma ( [ 0 , 1 ] )$ , then $\int _ { \gamma } f$ is the line integral of $f$ over γ. That is, $\int _ { \gamma } f \equiv \int _ { 0 } ^ { 1 } f ( \gamma ( t ) ) d \gamma ( t )$ . (See Conway [1978].) The next result generalizes to arbitrary regions in the plane, but for simplicity it is stated only for the disk ID. Recall the definition of $H ( \mathbb { D } )$ from Example 1.6.

4.2. Proposition. $L { \in } H ( \mathbb { D } ) ^ { * }$ if and only if there is an $r < 1$ and a unique function

g analytic on $\mathbf { \bar { C } } _ { \infty } \backslash \bar { B } ( 0 ; r )$ with $g ( \infty )   =   0$ such that

4.3

$$
L ( f ) = { \frac { 1 } { 2 \pi i } } \int _ { \gamma } f g
$$

for every f in H(ID), where $\gamma(t) = \rho e^{it}, \; 0 \leqslant t \leqslant 2\pi.$ and $r < \rho < 1$

PROOF. Let $g$ be given and define L as in (4.3). If $K = \left\{ z \colon | z | = \rho \right\}$ , then

$$
\begin{align*}|L(f)| = & \frac{1}{2\pi} \Bigg| \int_{0}^{2\pi} f(\rho e^{it}) g(\rho e^{it}) i \rho e^{it}   dt \Bigg| \\\leqslant & \frac{1}{2\pi} p_K(f) p_K(g) 2\pi \rho.\end{align*}
$$

So if $c = \rho p _ { K } ( g ) ,   | L ( f ) | \leqslant c p _ { K } ( f ) .$ , and $L { \in } H ( \mathbb { D } ) ^ { * }$

Now assume that $L { \in } H ( \mathbb { D } ) ^ { * }$ . The Hahn-Banach Theorem implies there is an F in $C ( \mathbf { D } ) ^ { * }$ such that $F | H ( \mathbf { D } ) = L$ . By Proposition 4.1 there is a compact set K contained in D and a measure μ on K such that $L ( f ) = \int _ { K } f   d \mu$ for every f in H(ID). Define $g \colon \mathbf { \mathfrak { C } } _ { \infty } \backslash K   \to   \mathbf { \mathfrak { C } }$ by $g ( \infty )   =   0$ and $g ( z ) = - \int _ { K } 1 / ( w - z ) d \mu ( w )$ for z in $\mathbf { C } \backslash K$ . By Lemma III.8.2, g is analytic on $\mathbf { C } _ { \infty } \backslash K$ . Let $\rho < 1$ such that $K \subseteq B(0;\rho).  If  \gamma(t) = \rho e^{it}, 0 \leqslant t \leqslant 2\pi$ , then Cauchy's Integral Formula implies

$$
f(w) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(z)}{z - w} dz.
$$

for $| w | < \rho ;$ in particular, this is true for w in K. Thus,

$$
\begin{align*}L(f) = & \int_{K} f(w)   d\mu(w) \\= & \int_{K} \left[ \frac{\rho}{2\pi} \int_{0}^{2\pi} \frac{f(\rho e^{it})}{\rho e^{it} - w}   e^{it}   dt \right] d\mu(w) \\= & \frac{\rho}{2\pi} \int_{0}^{2\pi} f(\rho e^{it}) e^{it} \left[ \int_{K} \frac{1}{\rho e^{it} - w}   d\mu(w) \right] dt \\= & \frac{1}{2\pi i} \int_{\gamma} f(z) g(z) dz.\end{align*}
$$

This completes the proof except for the uniqueness of g (Exercise 3).

## EXERCISES

1. Let $\{ \mathcal { X } _ { i } ; i { \in } I \}$ be a family of LCS's and give $\mathcal { X } = \prod \{ \mathcal { X } _ { i } : i { \in } I \}$ the product topology. (See Exercise 1.17.) Show that $L { \in } { \mathcal { X } } ^ { * }$ if and only if there is a finite subset F contained in I and there are $x _ { j } ^ { * }$ in $\mathcal { X } _ { j } ^ { * }$ for j in F such that $\begin{array} { r } { L ( x ) = \sum _ { j \in F } x _ { j } ^ { * } ( x ( j ) ) } \end{array}$ for each x in $\mathcal { X }$

2. Show that the space s (Exercise 1.13) is linearly homeomorphic to C(IN) and describe $s ^ { * }$ 4

3. Show that the function g obtained in Proposition 4.2 is unique.

4. Show that $L { \in } H ( \mathbb { D } ) ^ { * }$ if and only if there are scalars $b _ { 0 } , b _ { 1 } , \ldots$ in C such that lim sup $| b _ { n } | ^ { 1 / n } < 1$ and $L(f) = \sum_{n = 0}^{\infty} 1 / (n!) f^{(n)}(0) b_n$

5. If G is an annulus, describe $H ( G ) ^ { * }$

6. (Buck [1958]). Let X be locally compact and let β be the strict topology on $C _ { b } ( X )$ defined in Exercise 1.21. (Also see Exercises 2.6 and 2.7.) Prove the following statements: (a) If $\mu { \in } M ( X )$ and $\varepsilon _ { n } \downarrow 0 ,$ then there are compact sets $K _ { 1 } , K _ { 2 } , \ldots$ . such that for each $n \geqslant 1, K_n \in \mathrm{int} K_{n+1}$ and $| \mu | ( X \backslash K _ { n } ) < \varepsilon _ { n }$ . (b) If $\mu { \in } M ( X )$ , then there is a $\phi$ in $C _ { 0 } ( X )$ such that $\phi \geqslant 0 , \quad | \mu | ( X \backslash \{ x : \phi ( x ) > 0 \} ) = 0 , \quad 1 / \phi \in L ^ { 1 } ( | \mu | ) ,$ and $\int   1 / \phi   d | \mu | \leqslant 1$ . (c) Show that if $\mu { \in } M ( X )$ and $L ( f ) = \int f   d \mu$ for $f$ in $C _ { b } ( X )$ , then $\scriptstyle { \tilde { L } } \in ( C _ { b } ( X ) , \beta ) ^ { * }$ . (d) Conversely, if $L { \in } ( C _ { b } ( X ) , \beta ) ^ { * }$ , then there is $\mathbf { a }   \mu$ in $M ( X )$ such that $L ( f ) = \int f   d \mu$ for f in $C _ { b } ( X )$

7. Let X be completely regular and let M be a linear manifold in C(X). Show that if for every compact subset K of X, $\mathcal { M } | K \equiv \{ f | K \colon f \in \mathcal { M } \}$ is dense in $C ( K )$ , then $\mathcal { M }$ is dense in C(X).

## $\S 5 ^ { * }$ . Inductive Limits and the Space of Distributions

In this section the most general definition of an inductive limit will not be presented. Rather one that removes certain technicalities from the arguments and yet covers the most important examples will be given. For the more general definition see Köthe [1969], Robertson and Robertson [1966], or Schaefer [1971].

5.1. Definition. An inductive system is a pair $( \mathcal { X } , \{ \mathcal { X } _ { i } ; i { \in } I \} )$ , where $\mathcal { X }$ is a vector space, $\mathcal { X } _ { i }$ is a linear manifold in X that has a topology $\mathcal { T } _ { i }$ such that $( \mathcal { X } _ { i } , \mathcal { T } _ { i } )$ is a LCS, and, moreover:

(a) I is a directed set and $\mathcal { X } _ { i }   \subseteq   \mathcal { X } _ { j }$ i $i   \leqslant   j ;$

(b) if $i   \leqslant   j$ and $U _ { j } { \in } { \mathcal { T } } _ { j } ,$ then $U _ { i } { \cap } { \mathcal { X } } _ { i } { \in } { \mathcal { T } } _ { i } ;$

(c) $\mathcal { X } = \cup \{ \mathcal { X } _ { i } \colon i { \in } I \}$

Note that condition (b) is equivalent to the condition that the inclusion map $\mathcal { X } _ { i }   \subset   \to   \mathcal { X } _ { j }$ is continuous.

5.2. Example. Let $d \geqslant 1$ and let Ω be an open subset of $\mathbb { R } ^ { d }$ .Denote by $C _ { c } ^ { ( \infty ) } ( \Omega )$ all the functions $\phi \colon \mathbf { \Omega }   \to   \mathbf { F }$ such that $\phi$ is infinitely differentiable and has compact support in Ω. (The support of $\phi$ is defined by spt $\phi \equiv \mathrm{cl} \left\{ x : \phi(x) \neq 0 \right\}.$ If K is a compact subset of $\mathbf { \Omega } ,$ define $\mathcal { D } ( K ) \equiv \{ \phi \in C _ { c } ^ { ( \infty ) } ( \Omega ) : \mathrm { s p t } \phi \subseteq K \}$ . Let $\mathcal { D } ( K )$ have the topology defined by the seminorms

$$
p _ { K , m } ( \phi ) = \sup \left\{ \left| \phi ^ { ( k ) } ( x ) \right| : \left| k \right| \leqslant m , x \in K \right\} ,
$$

where $k = ( k _ { 1 } , \ldots , k _ { d } ) ,   k _ { j } \in \mathbb { N } \cup \{ 0 \} ,   | k | = k _ { 1 } + \cdots + k _ { d } .$ and

$$
\phi ^ { ( k ) } = \frac { \partial ^ { | k | } \phi } { \partial x _ { 1 } ^ { k _ { 1 } } \cdots \partial x _ { d } ^ { k _ { d } } } .
$$

Then $( C _ { c } ^ { ( \infty ) } ( \Omega ) ,   \{ \mathcal { D } ( K ) ;$ K is compact in $( \Omega ) )$ is an inductive system. The space $C _ { c } ^ { ( \infty ) } ( \Omega )$ is often denoted in the literature by (Ω), as it will be in this book.

This example of an inductive system is the most important one as it is connected with the theory of distributions (below). In fact, this example was the inspiration for the definition of an inductive limit given now.

5.3. Proposition. If $( \mathcal { X } , \{ \mathcal { X } _ { i } , \mathcal { T } _ { i } \} )$ is an inductive system, let $\mathcal { B } = a l l$ convex balanced sets V such that $V   \cap   \mathcal { X } _ { i }   \in   \mathcal { T } _ { i }$ for all i. Let $\mathcal { T } = t h e$ collection of all subsets U of X such that for every $x _ { 0 }$ in U there is aV in $\mathcal { B }$ with $x _ { 0 } + V \subseteq U$ Then $( \mathcal { X } , \mathcal { T } )$ is a (not necessarily Hausdorff) LCS.

Before proving this proposition, it seems appropriate to make the following definition.

5.4. Definition. If $( \mathcal { X } , \{ \mathcal { X } _ { i } \} )$ is an inductive system and $\mathcal { T }$ is the topology defined in (5.3), $\mathcal { T }$ is called the inductive limit topology and $( \mathcal { X } , \mathcal { T } )$ is said to be the inductive limit of $\{ \mathcal { X } _ { i } \}$

5.5. Lemma. With the notation as in (5.3), $\mathcal { B } \subseteq \mathcal { T }$

PROOF. Fix V is $\mathcal { B } ,$ It will be shown that V is absorbing at each of its points. Indeed, if $x _ { 0 }   \in   V$ and $x   \in   \mathcal { X }$ , then there is an $\mathcal { X } _ { i }$ and an $\mathcal { X } _ { j }$ such that $x _ { 0 } { \in } { \mathcal { X } } _ { i }$ and $x { \in } { \mathcal { X } } _ { i }$ . Since I is directed, there is a k in I with $k \geqslant i , \dot { j } .$ Hence $x _ { 0 } , x { \in } \mathcal { X } _ { k }$ But $V   \cap   \mathcal { X } _ { \pmb { k } }   \in   \mathcal { T } _ { \pmb { k } }$ . Thus there is an $\varepsilon   >   0$ such that $x _ { 0 } + \alpha x \in V \cap \mathcal { X } _ { k } \subseteq V$ for $| \alpha | < \varepsilon .$

Since V is convex, balanced, and absorbing at each of its points, there is a seminorm p on x such that $V = \{ x \in \mathcal { X } : p ( x ) < 1 \}$ (1.14). So if $x _ { 0 }   \in   V ,$ $p ( x _ { 0 } ) = r _ { 0 } < 1$ . Let $W = \{ x \in \mathcal{X} : p(x) < \frac{1}{2}(1 - r_0) \}$ . Then $W = \frac { 1 } { 2 } ( 1 - r _ { 0 } ) V$ and so $W { \in } { \mathcal { B } } .$ Since $x _ { 0 } + W \subseteq V , V \in { \mathcal { T } }$ ■

PROOF OF PROPOSITION 5.3. The proof that $\mathcal { F }$ is a topology is left as an exercise. To see that $( \mathcal { X } , \mathcal { T } )$ is a LCS, note that Lemma 5.5 and Theorem 1.14 imply that $\mathcal { T }$ is defined by a family of seminorms.

For all we know the inductive limit topology may be trivial. However, the fact that this topology has not been shown to be Hausdorff need not concern us, since we will concentrate on a particular type of inductive limit which will be shown to be Hausdorff. But for the moment we will continue at the present level of generality.

5.6. Proposition. Let $( \mathcal { X } , \{ \mathcal { X } _ { i } \} )$ be an inductive system and let $\mathcal { T }$ be the inductive

limit topology. Then

(a) the relative topology on $\mathcal { X } _ { i }$ induced by $\mathcal { T } \left( \mathrm { v i z . } , \mathcal { T } | \mathcal { X } _ { i } \right)$ is smaller than $\mathcal { T } _ { i }$ (b) if u is a locally convex topology on $\mathcal { X }$ such that for every i, $\mathcal { U }   |   \mathcal { X } _ { i }   \subseteq   \mathcal { T } _ { i }$ then $\mathcal { U } \subseteq \mathcal { T }$ 9

(c) a seminorm p on $\mathcal { X }$ is continuous if and only if $[ p | \mathcal { X } _ { i }$ is continuous for each i.

PROOF. Exercise 3.

5.7. Proposition. Let $( \mathcal { X } , \mathcal { T } )$ be the inductive limit of the spaces $\left\{ ( \mathcal { X } _ { i } , \mathcal { T } _ { i } ) ; i { \in } I \right\}$ If Y is a LCS and $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear transformation, then $T$ is continuous if and only if the restriction of T to each $\mathcal { X } _ { i }$ is $\mathcal { F } _ { i }$ -continuous.

PROOF. Suppose $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is continuous. By (5.6a), the inclusion map $( \mathcal { X } _ { i } , \mathcal { T } _ { i } )   \rightarrow   ( \mathcal { X } , \mathcal { T } )$ is continuous. Since the restriction of $T$ to $\mathcal { X } _ { i }$ is the composition of the inclusion map $\mathcal { X } _ { i }   \rightarrow   \mathcal { X }$ and $T ,$ the restriction is continuous.

Now assume that each restriction is continuous. If $p$ is a continuous seminorm on $\theta ,$ then $p   \circ T | \mathcal { X } _ { i }$ is a $\mathcal { T } _ { i }$ -continuous seminorm for every i. By (5.6c), $p \circ T$ is continuous on $\mathcal { X }$ . By Exercise 1.23, T is continuous.

It may have occurred to the reader that the definition of the inductive limit topology depends on the choice of the spaces $\mathcal { X } _ { i }$ in more than the obvious way. That is, if $\mathcal { X } = { \bigcup } _ { j } \mathcal { Y } _ { j }$ and each $\mathcal { G } _ { j }$ has a topology that is "compatible" with that of the spaces $\{ \mathcal { X } _ { i } \}$ , perhaps the inductive limit topology defined by the spaces $\{ \mathcal { G } _ { j } \}$ will differ from that defined by the $\{ \mathcal { X } _ { i } \}$ This is not the case.

5.8. Proposition. Let $( \mathcal { X } , \{ ( \mathcal { X } _ { i } , \mathcal { T } _ { i } ) \} )$ and $( \mathcal { X } , \{ ( \mathcal { Y } _ { j } , \mathcal { U } _ { j } ) \} )$ be two inductive systems and let $\mathcal { T }$ and u be the corresponding inductive limit topologies on $\mathcal { X }$ If for every i there is $a j$ such that $\mathcal { X } _ { i } \subseteq \mathcal { Y } _ { j }$ and $\mathcal { U } _ { j } | \mathcal { X } _ { i }   \subseteq   \mathcal { T } _ { i }$ , then $\mathcal { U } \subseteq \mathcal { T }$

ProoF. Let V be a convex balanced subset of $\mathcal { X }$ such that for every $j ,$ $V \cap \mathcal { G } _ { j } \in \mathcal { U } _ { j }$ . If $\mathcal { X } _ { i }$ is given, let $j$ be such that $\mathcal { X } _ { i } \subseteq \mathcal { Y } _ { j }$ and $\mathcal { U } _ { j } | \mathcal { X } _ { i } \subseteq \mathcal { T } _ { i }$ . Hence $V \cap \mathcal{X}_{i} = (V \cap \mathcal{Y}_{j}) \cap \mathcal{X}_{i} \in \mathcal{T}_{i}$ . Thus $V { \in } { \mathcal { B } }$ [as defined in (5.3)]. It now follows that $\mathcal { U } \subseteq \mathcal { T }$

5.9. Example. Let $\mathcal { X }$ be any vector space and let $\{ \mathcal { X } _ { i } ; i { \in } I \}$ be all of the finite dimensional subspaces of ${ \mathcal { X } } .$ Give each $\mathcal { X } _ { i }$ the unique topology from its identification with a Euclidean space. Then $( \mathcal { X } , \{ \mathcal { X } _ { i } \} )$ is an inductive system. Let $\mathcal { T }$ be the inductive limit topology. If $\mathcal { Y }$ is a LCS and T: $\mathcal { X }   \rightarrow   \mathcal { Y }$ is a linear transformation, then $T$ is $\mathcal { T }$ -continuous.

5.10. Example. Let X be a locally compact space and let $\{ K _ { i } ; i { \in } I \}$ be the collection of all compact subsets of $X .$ Let $\mathcal { X } _ { i }   =   a \Pi f$ in $C ( X )$ such that spt $f \subseteq K _ { i }$ . Then $\bigcup_{i} \mathcal{X}_{i} = C_{c}(X)$ , the continuous functions on X with compact support. Topologize each $\mathcal { X } _ { i }$ by giving it the supremum norm. Then $( C _ { c } ( X ) , \{ \mathcal { X } _ { i } \} )$ is an inductive system.

Let $\{ U _ { j } \}$ be the open subsets of X such that cl $U _ { j }$ is compact. Let $C _ { 0 } ( U _ { j } )$ be the continuous functions on $U _ { j }$ vanishing at $\infty$ with the supremum norm. If $f { \in } C _ { 0 } ( U _ { j } )$ and $f$ is defined on X by letting it be identically 0 on $X \backslash U _ { j } .$ then $f { \in } C _ { c } { \dot { ( } } X { \dot { ) } }$ . Thus $( C _ { c } ( X ) , \{ C _ { 0 } ( U _ { j } ) \} )$ is an inductive system. Proposition 5.8 implies that these two inductive systems define the same inductive limit topology on $C _ { c } ( X )$

5.11. Example. Let $d \geqslant 1$ and put $K_{n}=\left\{x \in \mathbb{R}^{d}:\|x\| \leqslant n\right\}$ . Then $( \mathcal { D } ( \mathbb { R } ^ { d } )$ $\left\{ \mathcal { D } ( K _ { n } ) \right\} _ { n = 1 } ^ { \infty }$ is an inductive system. By (5.9), the inductive limit topology defined on $\mathcal { D } ( \mathbb { R } ^ { d } )$ by this system equals the inductive limit topology defined by the system given in Example 5.2.

If Ω is any subset of $\mathbb { R } ^ { d } ,$ , then Ω can be written as the union of a sequence of compact subsets $\left\{ K _ { n } \right\}$ such that $K_{n} \in \mathrm{int} K_{n+1}$ . It follows by (5.9) that $\left\{ \mathcal { D } ( K _ { n } ) \right\}$ defines the same topology on $\mathcal { D } ( \Omega )$ as was defined in Example 5.2.

The preceding example inspires the following definition.

5.12. Definition. A strict inductive system is an inductive system $( \mathcal { X } , \{ \mathcal { X } _ { n } , \mathcal { T } _ { n } \} _ { n = 1 } ^ { \infty } )$ such that for every $n \geqslant 1, \mathcal{X}_n \subseteq \mathcal{X}_{n+1}, \mathcal{T}_{n+1} \mid \mathcal{X}_n = \mathcal{T}_n,$ and $\mathcal { X } _ { n }$ is closed in $\mathcal { X } _ { \pmb { n } \pmb { + 1 } }$ . The inductive limit topology defined on $\mathcal { X }$ by such a system is called a strict inductive limit topology and $\mathcal { X }$ is said to be the strict inductive limit of $\{ \mathcal { X } _ { n } \}$

Example 5.11 shows that $\mathcal { D } ( \mathbb { R } ^ { d } )$ , indeed $\mathcal { D } ( \Omega )$ , is a strict inductive limit.

The following lemma is useful in the study of strict inductive limits as well as in other situations.

5.13. Proposition. If X is a LCS, $\mathcal { Y } \leqslant \mathcal { X }$ , and p is a continuous seminorm on Y, then there is a continuous seminorm p on $\mathcal { X }$ such that $\tilde { p } | \mathcal { Y } = p .$

PROOF. Let $U = \{ y \in \mathcal { Y } : p ( y ) < 1 \}$ . So U is open in $另 ;$ hence there is an open subset $V _ { 1 }$ of X such that $V _ { 1 } \cap \mathcal { B } = U$ . Since $0   \in   { \cal V } _ { 1 }$ and $\mathcal { X }$ is a LCS, there is an open convex balanced set V in ¿ such that $V \subseteq V _ { 1 }$ . Let $q = \mathbf { t h e }$ gauge of V. So if $y \in \mathcal { Y }$ and $q ( y ) < 1$ , then $p ( y ) < 1$ . By Lemma III.1.4, $p \leqslant q \mid \mathcal { Y }$

Let $W = \mathrm{co}(U \cup V);$ it is easy to see that W is convex and balanced since both U and V are. It will be shown that W is open. First observe that $W = \left\{ t u + ( 1 - t ) v : 0 \leqslant t \leqslant 1 \right.$ , u∈U, v∈V} (verify). Hence $W = \cup \left\{ t U + \right.$ $(1 - t)V : 0 \leqslant t \leqslant 1 \}$ . Put $W _ { t } = t U + ( 1 - t ) V .$ So $W _ { 0 } = V ,$ which is open. If $0 < t < 1, W_t = \cup \{tu + (1 - t)V: u \in U\}$ , and hence is open. But $W _ { 1 } = U$ , which is not open. However, if $u   \in   U$ , then there is an $\varepsilon   >   0$ such that εu∈V. For $0 < t < 1$ , let $y_{t}=t^{-1}\left[1-\varepsilon+t\varepsilon\right]u\ (\in\mathcal{U}). \mathrm{As}\ t\to1,\ y_{t}\to u.$ Since U is open in Y, there is a $t , 0 < t < 1$ , with $y _ { t }$ in U. Thus $u = t y _ { t } + ( 1 - t ) ( \varepsilon u ) \in W _ { t }$ . Therefore $W = \cup \left\{ W_t : 0 \leqslant t < 1 \right\}$ and W is open.

## 5.14. Claim. $W \cap { \mathcal { B } } = U$

In fact, $U \subseteq W ,$ so $U \subset W \cap { \mathcal { Y } }$ If $w   \in   W \cap { \mathcal { G } } .$ then $w = t u + ( 1 - t ) v ,$ u in $U ,$ v in $V, 0 \leqslant t \leqslant 1;$ it may be assumed that $0 < t < 1$ . (Why?) Hence, $v = (1 - t)^{-1}(w - tu) \in \mathcal{Y}$ So $v   \in   V   \cap   \mathcal { Y } \subseteq U ;$ hence $w { \in } U$

Let $\tilde { p } = \mathrm { t h } \mathbf { e }$ gauge of W. By Claim 5.14, $\{ y \in \mathcal { Y } : \tilde { p } ( y ) < 1 \} = \{ y \in \mathcal { Y } : p ( y ) < 1 \}$ By the uniqueness of the gauge, $\tilde { p } | \mathcal { Y } = p$

5.15. Corollary. If $\mathcal { X }$ is the strict inductive limit of $\{ \mathcal { X } _ { n } \}$ , k is fixed, and $p _ { k }$ is a continuous seminorm on $\mathcal { X } _ { k }$ , then there is a continuous seminorm p on $\mathcal { X }$ such that $p | \mathcal { X } _ { k } = p _ { k }$ . In particular, the inductive limit topology is Hausdorff and the topology on X when restricted to $\mathcal { X } _ { k }$ equals the original topology of $\mathcal { X } _ { k }$

PRoOF. By (5.13) and induction, for every integer $n > k ,$ there is a continuous seminorm $p _ { n }$ such that $p_{n}|\mathcal{X}_{n - 1} = p_{n - 1}$ $\operatorname { I f } x { \in } { \mathcal { X } }$ , define $p ( x ) = p _ { n } ( x )$ when $x { \in } { \mathcal { X } } _ { n } .$ Since $\mathcal { X } _ { n } \subseteq \mathcal { X } _ { n + 1 }$ for all n, the properties of $\{ p _ { n } \}$ insure that p is well defined. Clearly p is a seminorm and by (5.6c) p is continuous.

If $x { \in } { \mathcal { X } }$ and $x \neq 0 ,$ there is a $k \geqslant 1$ such that $x   \in   \mathcal { X } _ { k }$ . Thus there is a continuous seminorm $p _ { k }$ on $\mathcal { X } _ { k }$ such that $p _ { k } ( x ) \neq 0$ . Using the first part of the corollary, we get a continuous seminorm p on $\mathcal { X }$ such that $p ( x ) \neq 0 .$ Thus $( \mathcal { X } , \mathcal { T } )$ is Hausdorff. The proof that the topology on $\mathcal { X }$ when relativized to $\mathcal { X } _ { k }$ equals the original topology is an easy application of (5.13).

5.16. Proposition. Let X be the strict inductive limit of $\{ \mathcal { X } _ { n } \}$ . A subset B of X is bounded if and only if there is an $n \geqslant 1$ such that $B \subseteq { \mathcal { X } } _ { n }$ and B is bounded in ${ \mathcal { X } } _ { n }$

The proof will be accomplished only after a few preliminaries are settled. Before doing this, here are a few consequences of (5.16).

5.17. Corollary. If X is the strict inductive limit of $\{ \mathcal { X } _ { n } \}$ , then a subset K of X is compact if and only if there is an $n \geqslant 1$ such that $K \subseteq { \mathcal { X } } _ { n }$ and K is compact in $\mathcal { X } _ { n }$

5.18. Corollary. If X is the strict inductive limit of Fréchet spaces $\{ \mathcal { X } _ { n } \}$ , Y is a LCS, and $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear transformation, then T is continuous if and only if T is sequentially continuous.

ProoF. By Proposition 5.7, T is continuous if and only if $T | \mathcal { X } _ { n }$ is continuous for every n. Since each $\mathcal { X } _ { n }$ is metrizable, the result follows. ■

Note that using Example 5.11 it follows that for an open subset Ω of $\mathbb { R } ^ { d }$ D(Ω) is the strict inductive limit of Fréchet spaces [each $\mathcal { D } ( K _ { n } )$ is a Fréchet space by Proposition 2.1]. So (5.18) applies.

5.19. Definition. If Ω is an open subset of $\mathbf { R } ^ { d } ,$ a distribution on Ω is a continuous linear functional on $\mathcal { D } ( \Omega )$

Distributions are, in a certain sense, generalizations of the concept of function as the following example illustrates.

5.20. Example. Let f be a Lebesgue measurable function on Ω that is locally integrable (that is, $\int _ { K } | f |   d \lambda < \infty$ for every compact subset K of Ω—here λ is d-dimensional Lebesgue measure). If $L _ { f } \colon { \mathcal { D } } ( \Omega ) \to \mathbb { F }$ is defined by $L _ { f } ( \phi ) =$ $\int   f \phi   d \lambda ,   L _ { f }$ is a distribution.

From Corollary 5.18 we arrive at the following.

5.21. Proposition. A linear functional $L \colon { \mathcal { D } } ( \Omega )   \to   \mathbb { F }$ is a distribution if and only if for every sequence $\{ \phi _ { n } \}$ $\mathcal { D } ( \Omega )$ such that cl $\left[ \bigcup _ { n = 1 } ^ { \infty } \operatorname { s p t } \phi _ { n } \right] = K$ is compact in Ω and $\phi _ { n } ^ { ( k ) } ( x )   \rightarrow   0$ uniformly on K as $n   \to   \infty$ for every $k   =   ( k _ { 1 } , \ldots , k _ { d } ) ,$ it follows that $L ( \phi _ { n } )   \to   0$

Proposition 5.21 is usually taken as the definition of a distribution in books on differential equations. There is the advantage that (5.21) can be understood with no knowledge of locally convex spaces and inductive limits. Moreover, most theorems on distributions can be proved by using (5.21). However, the realization that a distribution is precisely a continuous linear functional on a LCS contributes more than cultural edification. This knowledge brings power as it enables you to apply the theory of LCS's (including the Hahn-Banach Theorem).

The exercises contain more results on distributions, but now we must return to the proof of Proposition 5.16. To do this the idea of a topological complement is needed. We have seen this idea in Section III.13.

5.22. Proposition. If $\mathcal { X }$ is a TVS and $\mathcal { Y } \leqslant \mathcal { X }$ , the following statements are equivalent.

(a) There is a closed linear subspace $\mathcal { I }$ of X such that y $\cap \mathcal { X } = ( 0 ) , \mathcal { Y } + \mathcal { X } = \mathcal { X } ,$ and the map of $\mathcal { Y } \times \mathcal { X }   \rightarrow   \mathcal { X }$ given by $( y , z ) { \mapsto } y + z$ is a homeomorphism. (b) There is a continuous linear map $P \colon { \mathcal { X } }   \to   { \mathcal { X } }$ such that $P \mathcal{X} = \mathcal{Y}   and   P^2 = P$

PROOF. $( \mathsf { a } ) \Rightarrow ( \mathsf { b } )$ : Define $P \colon { \mathcal { X } }   \to   { \mathcal { X } }$ by $P ( y + z ) = y ,$ for y in $\theta$ and z in $\mathcal { X }$ It is easy to verify that P is linear and $\mathcal { P } \mathcal { X } = \mathcal { Y }$ . Also, $P^{2}(y + z) = PP(y + z) =$ $P y = y = P ( y + z ) ;$ so $P^{2} = P.\  If \ \left\{ y_{i} + z_{i} \right\}$ is a net in $\mathcal { X }$ such that $y _ { i } + z _ { i }   \rightarrow   y + z ,$ then (a) implies that $y _ { i }   \rightarrow   y$ (and $z _ { i }   \to   z )$ . Hence $P(y_i + z_i) \to P(y + z)$ and $P$ is continuous.

(b) ⇒ (a): If P is given, let Z = ker P. So $\mathcal { L } \leqslant \mathcal { X }$ . Also, $x = P x + ( x - P x )$ and $y = P x \in \mathcal { Y }$ , and $z = x - P x$ has $Pz = Px - P^{2}x = Px - Px = 0, \quad \mathrm{so} \quad z \in \mathcal{X}$ Thus, $\mathcal { Y } + \mathcal { X } = \mathcal { X }$ If $x \in \mathcal { Y } \cap \mathcal { Z }$ , then $P x = 0$ since x∈x; but also $x = P w$ for some w in $\mathcal { X }$ since $x \in \mathcal { Y } = P \mathcal { X }$ . Therefore $0 = P x = P ^ { 2 } w = P w = x ;$ that is, $\mathcal { Y } \cap \mathcal { X } = ( 0 )$ . Now suppose that $\left\{ y _ { i } \right\}$ and $\left\{ z _ { i } \right\}$ are nets in $\theta$ and ${ \mathcal { L } } . { \mathrm { ~ I f ~ } } y _ { i }   \to   y$ and $z _ { i }   \rightarrow   z _ { 1 }$ then $y _ { i } + z _ { i }   \rightarrow   y + z$ because addition is continuous. If, on the other