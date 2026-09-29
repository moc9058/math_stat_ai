Conversely, if $\mathcal { X }$ is the linear span of $E ,$ then for every x in $\mathcal { X } \backslash E ,   E \cup \{ x \}$ is not linearly independent. Thus E is a basis.

1.2. Proposition. If $E _ { 0 }$ is a linearly independent subset of $\mathcal { X }$ , then there is a basis E that contains $E _ { 0 }$

PRoOF. Use Zorn's Lemma.

A linear functional on $\mathcal { X }$ is a function $f \colon { \mathcal { X } }   \to   \mathbb { F }$ such that $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$ for $x , y$ in $\mathcal { X }$ and $\alpha , \beta$ in F. If $\mathcal { X }$ and $\pmb { y }$ are vector spaces over $\mathbb { F } ,$ a linear transformation from $\mathcal { X }$ into $\pmb { y }$ is a function $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ such that $T(\alpha_{1}x_{1} + \alpha_{2}x_{2}) = \alpha_{1}T(x_{1}) + \alpha_{2}T(x_{2})   for   x_{1},x_{2}$ in $\mathcal { X }$ and $\alpha _ { 1 } , \alpha _ { 2 }$ in $\mathbb { F } .$

If $A , B \subseteq { \mathcal { X } }$ , then $A + B \equiv \{ a + b \colon a { \in } A ,   b { \in } B \} ;   A - B \equiv \{ a - b \colon a { \in } A ,   b { \in } B \}$ For α in F and $A \subseteq \mathcal{X}, \alpha A \equiv \{ \alpha a : a \in A \}$ . If M is a linear manifold in $\mathcal { X }$ (that is, $\mathcal { M } \subseteq \mathcal { X }$ and M is also a vector space with the same operations defined on $\mathcal { X } ) ,$ , then define $x / M$ to be the collection of all the subsets of $\mathcal { X }$ of the form $x + \mathcal { M }$ A set of the form $x + \mathcal { M }$ is called a coset of $\mathcal { M } ,$ Note that $( x + \mathcal { M } ) + ( y + \mathcal { M } ) = ( x + y ) + \mathcal { M }$ and $\alpha ( x + \mathcal { M } ) = \alpha x + \mathcal { M }$ since $\mathcal { M }$ is a linear manifold. Hence $x / M$ becomes a vector space over $\mathbb { E }$ It is called the quotient space of $\mathcal { X }$ mod $\mathcal { M }$

Define Q: $\mathcal { X } \rightarrow \mathcal { X } / \mathcal { M }$ by $Q ( x ) = x + { \mathcal { M } }$ . It is easy to see that $Q$ is a linear transformation. It is called the quotient map.

If $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear transformation,

$$
\begin{aligned}\ker T & \equiv \{ x { \in } { \mathcal { X } } { : } \; T x = 0 \} , \\\operatorname { r a n } T & \equiv \{ T x { : } \; x { \in } { \mathcal { X } } \} ;\end{aligned}
$$

ker T is the kernel of T and ran T is the range of T. If ran $T = \mathcal { Y } ,$ T is surjective; if ker $T = ( 0 ) ,$ T is injective. If T is both injective and surjective, then $T$ is bijective. It is easy to see that the natural map $\mathcal { Q } \colon \mathcal { X } \to \mathcal { X } / \mathcal { M }$ is surjective and ker $Q = M$

Suppose now that $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear transformation and M is a linear manifold in $\mathcal { X } .$ We want to define a map $\hat { T } : \mathcal { X } / \mathcal { M } \rightarrow \mathcal { Y }$ by $\hat { T } ( x + \mathcal { M } ) = T x .$ But $\hat { T }$ may not be well defined. To ensure that it is we must have $T x _ { 1 } = T x _ { 2 }$ i $x _ { 1 } + \mathcal { M } = x _ { 2 } + \mathcal { M }$ But $x _ { 1 } + \mathcal { M } = x _ { 2 } + \mathcal { M }$ if and only if $x _ { 1 } - x _ { 2 } \in \mathcal { M }$ , and $T x _ { 1 } = T x _ { 2 }$ if and only if $x _ { 1 } - x _ { 2 }$ eker T. So $\hat { T }$ is well defined if $\mathcal { M } \subseteq \ker T$ It is easy to check that if $\hat { T }$ is well defined, $\hat { T }$ is linear.

1.3. Proposition. If $T \colon { \mathcal { X } }   \to   { \mathcal { Y } }$ is a linear transformation and $\mathcal { M }$ is a linear manifold in $\mathcal { X }$ contained in ker $T ,$ then there is a linear transformation $\hat { T } ;$ $\mathcal { X } / \mathcal { M } \rightarrow \mathcal { Y }$ such that the diagram

![](images/page_384_image_13.jpg)

commutes.

The preceding proposition is especially useful if $\mathcal { M } = \ker T$ . In that case $\hat { T }$ is injective.

The last proposition of this section will be quite helpful in the book.

1.4. Proposition. Let $f , f _ { 1 } , \ldots , f _ { n }$ be linear functionals in $\mathcal { X } .$ If ker $f \supseteq$ $\bigcap _ { k = 1 } ^ { n }$ ker $f _ { \mathbf { k } }$ then there are scalars $\alpha _ { 1 } , \ldots , \alpha _ { n }$ such that $f = \sum _ { k = 1 } ^ { n } \alpha _ { k } f _ { k }$ (that is, $f(x) = \sum_{k = 1}^{n} \alpha_{k} f_{k}(x)$ for every x in X).

ProoF. It may be assumed without loss of generality that for $1 \leqslant k \leqslant n,$

$$
\bigcap_{j \ne k} \ker f_{j} \ne \bigcap_{j=1}^{n} \ker f_{j}.
$$

(Why?). So for $1 \leqslant k \leqslant n ,$ there is a $y _ { k }$ in $\bigcap _ { j \neq k } \ker f _ { j }$ such that $y _ { k } \notin \bigcap _ { j = 1 } ^ { n }$ ker $f _ { j } .$ So $f _ { j } ( y _ { k } ) = 0$ for $j \neq k ,$ but $f _ { k } ( y _ { k } ) \neq 0$ Let $x_{k} = \left[ f_{k}(y_{k}) \right]^{-1} y_{k}$ . Hence $f _ { k } ( x _ { k } ) = 1$ and $f _ { j } ( x _ { k } ) = 0$ for $j \neq k .$

Now let f be as in the statement of the proposition and put $\alpha _ { k } = f ( x _ { k } )$ $\operatorname { I f } x { \in } { \mathcal { X } } .$ , let $y = x - \sum_{k = 1}^{n} f_{k}(x)x_{k}.$ Then $f _ { j } ( y ) = f _ { j } ( x ) - \sum _ { k = 1 } ^ { n } f _ { k } ( x ) f _ { j } ( x _ { k } ) = 0$ By hypothesis, $f ( y ) = 0 .$ Thus

$$
0 = f(x) - \sum_{k = 1}^{n} f_{k}(x) f(x_{k})
$$

$$
f(x) - \sum_{k = 1}^{n} \alpha_{k} f_{k}(x);
$$

equivalently, $\begin{array} { r } { f = \sum _ { k = 1 } ^ { n } \alpha _ { k } f _ { k } . } \end{array}$

## §2. Topology

In this book all topological spaces are assumed to be Hausdorff.

This section will review some of the concepts and results using nets, as this idea is frequently used in the text.

A directed set is a partially ordered set $( I ,   \leqslant )$ such that if $i _ { 1 } , i _ { 2 } { \in } I ,$ , then there is an $i _ { 3 }$ in I such that $i _ { 3 } \geqslant i _ { 1 }$ and $i _ { 3 } \geqslant i _ { 2 } ^ { \; \prime } .$ A good example of a directed set is to let $( X , { \mathcal { S } } )$ be a topological space and for a fixed $x _ { 0 }$ in X let $\mathcal { U } =$ $\{ U \mathrm { i n } \mathcal { S } : x _ { 0 } \in U \}$ . If $U , V   \in   \mathcal { U }$ , define $U \geqslant V \mathrm{~if~} U \subseteq V$ (so bigger is smaller). u is said to be ordered by reverse inclusion. Another example is found if S is any set and $\mathcal { F }$ is the collection of all finite subsets of S. Define $F _ { 1 } \geqslant F _ { 2 }$ in $\mathcal { F }$ if $F _ { 1 } \supseteq F _ { 2 }$ (bigger means bigger). Here $\mathcal { F }$ is said to be ordered by inclusion. Both of these examples are used frequently in the text.

A net in X is a pair $( ( I , \leqslant ) , x )$ where $( I , \leqslant )$ is a directed set and x is a function from I into X. Usually we will write $x _ { i }$ instead of $x ( i )$ and will use the phrase “let $\left\{ x _ { i } \right\}$ be a net in $X .$

Note that $\mathbf { N } ,$ the natural numbers, is a directed set, so every sequence is a net. If $( X , { \mathcal { T } } )$ is a topological space, $x _ { 0 } { \in } X$ , and $\mathcal { U } = \{ U$ in ${ \mathcal { T } } \colon { \pmb { x } } _ { 0 } { \in } { \pmb { U } } \big \}$ , then let $x _ { v } { \in } U$ for every U in U. So $\{ x _ { v } \colon U { \in } { \mathcal { U } } \}$ is a net in X.

2.1. Definition. If $\left\{ x _ { i } \right\}$ is a net in a topological space X, then $\{ x _ { i } \}$ converges to $x _ { 0 }$ (in symbols, $x _ { i }   \rightarrow   x _ { 0 }$ or $x_{0} = \lim_{} x_{i}$ if for every open subset U of X such that $x _ { 0 } { \in } U$ , there is an $i _ { 0 } = i _ { 0 } ( U )$ such that $x _ { i } { \in } U$ for $i   \geqslant   i _ { 0 }$ . The net clusters at $x _ { 0 }$ (in symbols, $x _ { i }   \xrightarrow [ \mathrm { c l } ] { \mathrm { ~ \tiny ~ \mathrm { ~ \scriptsize ~ \mathrm { ~ \scriptsize ~ } ~ } ~ } }   x _ { 0 } )$ if for every $i _ { 0 }$ and for every open neighborhood U of $x _ { 0 } ,$ there exists an $i   \geqslant   i _ { 0 }$ such that $x _ { i } { \in } U$

These notions generalize the corresponding concepts for sequences. Also, if $x _ { i }   \rightarrow   x _ { 0 } ,$ then $x _ { i }   \xrightarrow [ \mathrm { c l } ] { \quad }   x _ { 0 }$ . Note that the net $\{ x _ { v } \colon U { \in } { \mathcal { U } } \}$ defined just prior to the definition converges to $x _ { 0 }$ . This is a very important example of a convergent net.

2.2. Proposition. If X is a topological space and $A \subseteq X$ , then x∈cl A (closure of A) if and only if there is a net $\{ a _ { i } \}$ in A such that $a _ { i }   \rightarrow   { \pmb x } .$

PROOF. Let $\mathcal { U } = \{ U \colon U$ is open and $\scriptstyle { \boldsymbol { x } } \in { \boldsymbol { U } } \big \}$ . If x∈cl A, then for each U in $q$ there is a point $a _ { U }$ in $A \cap U$ . if $U _ { 0 } { \in } { \mathcal { U } }$ , then $a _ { v } { \in } U _ { 0 }$ for every $U \geqslant U _ { 0 } ;$ therefore $x = \lim_{U \to \infty} a_U$ . Conversely, if $\{ a _ { i } \}$ is a net in A and $a _ { i }   \rightarrow   { \pmb x } _ { i }$ , then each U in $q$ contains a point $a _ { i }$ and $a _ { i }   \in   \mathsf { A }   \cap   U$ . Thus x∈cl A.

2.3. Proposition. If $A \subseteq X ,   \{ a _ { i } \}$ is a net in A, and $a _ { i } \xrightarrow [ \mathrm { c l } ] { } x _ { i }$ , then x∈cl A.

PROOF. Exercise.

There is a concept of a subnet of a net and with this concept it is possible to prove that if a net clusters at a point x, then there is a subnet that converges to x. The concept of a subnet is, however, somewhat technical and is not what you might at first think it should be. Since this concept is not used in this book, the interested reader is referred to Kelley [1955]. It might also be appropriate to mention that a topological space is Hausdorff if and only if each convergent net has a unique limit point.

2.4. Proposition. If X and Y are topological spaces and $f \colon X \to Y ,$ then f is continuous at $x _ { 0 }$ if and only if $f ( x _ { i } )   \rightarrow   f ( x _ { 0 } )$ whenever $x _ { i }   \rightarrow   x _ { 0 }$

ProoF. First assume that f is continuous at $x _ { 0 }$ and let $\{ x _ { i } \}$ be a net in X such that $x _ { i }   \rightarrow   x _ { 0 }$ in X. If V is open in Y and $f ( x _ { 0 } )   \in   \pmb { V }$ , then there is an open set U in X such that $x _ { 0 } { \in } U$ and $f ( U ) \subseteq V$ . Let $i _ { 0 }$ be such that $x _ { i } { \in } U$ for $i   \geqslant   i _ { 0 } ,$ Hence $f ( x _ { i } )   \in   V$ for $i   \geqslant   i _ { 0 }$ .This says that $f ( x _ { i } )   \rightarrow   f ( x _ { 0 } )$

Let $\mathcal { U } = \{ U \colon U$ is open in X and $x _ { 0 } { \in } U \}$ . Suppose f is not continuous at $x _ { 0 } .$ Then there is an open subset V of Y such that $f ( x _ { 0 } )   \in   \pmb { V }$ and $f(U) \backslash V \neq \square$ for every U in U. Thus for each U in ¿ there is a point $x _ { U }$ in U with $f ( \pmb { x } _ { U } ) { \notin } \pmb { V }$ But $\left\{ x _ { v } \right\}$ is a net in X with $x _ { v }   \rightarrow   x _ { 0 }$ and clearly $\{ f ( \pmb { x } _ { U } ) \}$ cannot converge to $f ( x _ { 0 } )$

2.5. Proposition. ${ \mathit { I f } } f \colon X \to Y , f$ is continuous at $x _ { 0 } ,$ and $\{ x _ { i } \}$ is a net in X that clusters at $x _ { 0 } ,$ then $\{ f ( x _ { i } ) \}$ clusters at $f ( x _ { 0 } )$

PROOF. Exercise.

2.6. Proposition. Let $K \subseteq X$ . Then K is compact if and only if each net in K has a cluster point in K.

PpRoOF. Suppose that K is compact and let $\left\{ x _ { i } ; i { \in } I \right\}$ be a net in K. For each i let $F _ { i } = \mathrm { c l } \left\{ x _ { j } ; j \geqslant i \right\}$ , so each $F _ { i }$ is a closed subset of K. It will be shown that $\left\{ F _ { i } ; i { \in } I \right\}$ has the finite intersection property. In fact, since I is directed, if $i _ { 1 } , \ldots , i _ { n } { \in } I ,$ , then there is an $i \geqslant i _ { 1 } , \ldots , i _ { n } .$ Thus $F_{i} \subseteq \bigcap_{k = 1}^{n} F_{i_{k}}$ and $\left\{ F _ { i } \right\}$ has the finite intersection property. Because K is compact, there is an $x _ { 0 }$ in $\bigcap _ { i } F _ { i ^ { \bullet } }$ But if U is open with $x _ { 0 }$ in U and $i _ { 0 } { \in } I ,$ the fact that $x_{0} \in \mathrm{cl}\left\{ x_{i}: i \geqslant i_{0} \right\}$ , implies there is an $i \geqslant i _ { 0 }$ with $x _ { i }$ in U. Thus $x _ { i }   \xrightarrow [ \mathrm { c l } ] { \quad }   x _ { 0 } .$

Now assume that each net in K has a cluster point in K. Let $\{ K _ { \alpha } ; \alpha { \in } A \}$ be a collection of relatively closed subsets of K having the finite intersection property. If $\mathcal { F } =$ the collection of all finite subsets of A, order $\mathcal { F }$ by inclusion. By hypothesis, if $F   \in   \mathcal { F }$ , there is a point $x _ { F }$ in $\bigcap \{ K _ { \alpha } ; \alpha { \in } F \}$ . Thus $\{ x _ { F } \}$ is a net in K. By hypothesis, $\left\{ x _ { F } \right\}$ has a cluster point $x _ { 0 }$ in K. Let $\alpha \in A ,$ so $\{ \alpha \} \in \mathcal { F }$ Thus if U is any open set containing $x _ { 0 }$ there is an F in $\mathcal { F }$ such that $\alpha { \in } F$ and $x _ { F } { \in } U$ Thus $x _ { F } { \in } U { \cap } K _ { \alpha } ;$ that is, for each α in A and for every open set U containing $x _ { 0 } ,   U \cap K _ { \alpha } \neq \square$ . Since $K _ { \alpha }$ is relatively closed, $x _ { 0 } { \in } K _ { \alpha }$ for each α in A. Thus $x _ { 0 } { \in } { \bigcap } _ { \alpha } K _ { \alpha }$ and K must be compact.

The next result is used repeatedly in this book.

2.7. Proposition. If X is compact, $\{ x _ { i } \}$ is a net in X, and $x _ { 0 }$ is the only cluster point of $\{ x _ { i } \}$ , then the net $\left\{ x _ { i } \right\}$ converges to $x _ { 0 }$

ProoF. Let U be an open neighborhood of $x _ { 0 }$ and let $J = \left\{ j { \in } I { : } x _ { j } { \notin } U \right\}$ . If $\{ x _ { i } \}$ does not converge to $x _ { 0 }$ , then for every i in I there is a j in J such that $j \geqslant i .$ In particular, J is also a directed set. Hence $\left\{ x _ { j } ; j { \in } J \right\}$ is a net in the compact set $X \backslash U$ . Thus it has a cluster point $y _ { 0 }$ . But the property of J mentioned before implies that $y _ { 0 }$ is also a cluster point of $\left\{ x _ { i } ; j { \in } I \right\}$ contradicting the assumption. Thus $x _ { i }   \rightarrow   x _ { 0 }$

The next result is rather easy, but it will be used so often that it should be explicitly stated and proved.

2.8. Proposition. If f: X → Y is bijective and continuous and X is compact, then f is a homeomorphism.

ProoF. If F is a closed subset of X, then F is compact. Thus $f ( F )$ is compact in Y and hence closed. Since f maps closed sets to closed sets, $f ^ { - 1 }$ is continuous.

Note that the Hausdorff property was used in the preceding proof when we said that a compact subset of Y is closed.

In the study of functional analysis it is often the case that the mathematician is presented with a set that has two topologies. It is useful to know how properties of one topology relate to the other and when the two topologies are, in fact, one.

If X is a set and $\mathcal { T } _ { 1 } , \mathcal { T } _ { 2 }$ are two topologies on X, say that $\mathcal { T } _ { 2 }$ is larger or stronger than $\mathcal { T } _ { 1 }$ if $\mathcal { T } _ { 2 } \mathop { \supseteq } \mathcal { T } _ { 1 } ;$ in this case you may also say that $\mathcal { T } _ { 1 }$ is smaller or weaker. In the literature there is also an unfortunate nomenclature for these concepts; the words “finer"and “coarser"are used.

The following result is easy to prove (it is an exercise) but it is enormously useful in discussing a set with two topologies.

2.9. Lemma. $I f \mathcal { T } _ { 1 } , \mathcal { T } _ { 2 }$ are topologies on X, then $\mathcal { T } _ { 2 }$ is larger than $\mathcal { T } _ { 1 }$ if and only if the identity map i: $( X , { \mathcal { T } } _ { 2 } )   \rightarrow   ( X , { \mathcal { T } } _ { 1 } )$ is continuous.

2.10. Proposition. Let $\mathcal { T } _ { 1 } , \mathcal { T } _ { 2 }$ be topologies on X and assume that $\mathcal { T } _ { 2 }$ is larger than $\mathcal { T } _ { 1 }$

(a) If F is $\mathcal { T } _ { 1 }$ -closed, F is $\mathcal { T } _ { 2 } - c l o s e d .$

(b) If $f \colon Y   \to   \left( X , { \mathcal { T } } _ { 2 } \right)$ is continuous, then $f \colon Y   \to   \left( X , { \mathcal { T } } _ { 1 } \right)$ is continuous.

(c) If $f ( X , { \mathcal { T } } _ { 1 } )   \to   Y$ is continuous, then $f \colon ( X , { \mathcal { T } } _ { 2 } ) \to Y$ is continuous.

(d) If K is $\mathcal { T } _ { 2 } - c o m p a c t$ , then K is $\mathcal { T } _ { 1 } - c o m p a c t .$

(e) If X is $\mathcal { T } _ { 2 } - c o m p a c t ,$ then $\mathcal { T } _ { 1 } = \mathcal { T } _ { 2 }$

PROOF. (b) Note that $f \colon Y   \to   \left( X , { \mathcal { T } } _ { 1 } \right)$ is the composition of $f \colon Y   \to   \left( X , { \mathcal { T } } _ { 2 } \right)$ and i: $( X , { \mathcal { T } } _ { 2 } )   \to   ( X , { \mathcal { T } } _ { 1 } )$ and use Lemma 2.9.

(d) Use Lemma 2.9.

(e) Use Lemma 2.9 and Proposition 2.8.

The remainder of the proof is an exercise.

APPENDIX B

The Dual of $L ^ { p } ( \mu )$

In this section we will prove the following which appears as III.5.5 and III.5.6 in the text.

Theorem. Let $( X , \Omega , \mu )$ be a measure space, let $1 \leqslant p < \infty$ , and let $1 / p + 1 / q = 1$ If $g   \in   L ^ { q } ( \mu )$ , define $F _ { g } \colon L ^ { p } ( \mu ) \to \mathbb { F }$ by

$$
F _ { g } ( f ) = \int f g d \mu .
$$

If $1 < p < \infty$ , the map $g { \mapsto } F _ { g }$ defines an isometric isomorphism of $L ^ { \pmb q } ( \mu )$ onto $L ^ { p } ( \mu ) ^ { * } . I f   p = 1$ and $( X , \Omega , \mu )$ is σ-finite, $g { \mapsto } F _ { g }$ is an isometric isomorphism of $L ^ { \infty } ( \mu )$ onto $L ^ { 1 } ( \mu ) ^ { * }$

PROOF. If $g   \in   L ^ { q } ( \mu )$ , then Hölder's Inequality implies that $| F _ { g } ( f ) | \leqslant \| f \| _ { p } \| g \| _ { q }$ for all f in $L ^ { p } ( \mu )$ . Hence $F _ { g } \in L ^ { p } ( \mu ) ^ { * }$ and $\| \boldsymbol { F } _ { g } \| \leqslant \| g \| _ { q } .$ Therefore $g { \mapsto } F _ { g }$ is a linear contraction. It must be shown that this map is surjective and an isometry. Assume $F   \in   L ^ { p } ( \mu ) ^ { * }$

Case 1: $\mu ( X ) < \infty$ . Here $\chi _ { \Delta }   \in   L ^ { p } ( \mu )$ for every ∆ in Ω. Define $v ( \Delta ) = F ( \chi _ { \Delta } )$ It is easy to see that v is finitely additive. If $\{ \Delta _ { n } \} \subseteq \Omega$ with $\mathbf { \Delta _ { 1 } } \supseteq \mathbf { \Delta _ { 2 } } \supseteq \cdots$ and $\bigcap_{n = 1}^{\infty} \Delta_{n} = \square$ , then

$$
\begin{align*}\| \chi_{\Delta_n} \|_p = & \left[ \int |\chi_{\Delta_n}|^p   d\mu \right]^{1/p} \\= & \mu(\Delta_n)^{1/p} \to 0.\end{align*}
$$

Hence $v ( \Delta _ { n } ) \to 0$ since F is bounded. It follows by standard measure theory that v is a countably additive measure. Moreover, if $\mu ( \Delta ) = 0 , \chi _ { \Delta } = 0$ in $L ^ { p } ( \mu ) ;$ hence $v ( \Delta ) = 0$ . that is, $\pmb { v } \ll \pmb { \mu } .$ By the Radon-Nikodym Theorem there is an Ω-measurable function g such $v ( \Delta ) = \int _ { \Delta } g   d \mu$ for every $\Delta$ in $\boldsymbol { \Omega } ;$ that is, $F ( \chi _ { \Delta } )   =$ $f \chi _ { \Delta } g d \mu$ for every ∆ in Ω. It follows that

B.1

$$
F ( f ) = \int f g d \mu
$$

for every simple function $f .$

## B.2. Claim. $g   \in   L ^ { q } ( \mu )$ and $\| g \| _ { q } \leqslant \| F \|$

Note that once this claim is proven, the proof of Case 1 is complete. Indeed, (B.2) says that $F _ { g } \in L ^ { p } ( \mu ) ^ { * }$ and since F and $F _ { \pmb { g } }$ agree on a dense subset of $L ^ { p } ( \mu ) ( \mathbf { B } . 1 )$ $F = \bar { F _ { g } } .$ Also, | $g \parallel _ { q } \leqslant \| F \| = \| F _ { g } \| \leqslant \| g \| _ { q } .$

To prove (B.2), let $t   >   0$ and put $E_{t}=\left\{x \in X:|g(x)| \leq t\right\}$ . If $f   \in   L ^ { p } ( \mu )$ such that $f = 0$ off $E _ { t } ,$ then there is a sequence $\{ f _ { n } \}$ of simple functions such that for every n, $f _ { n } = 0$ off $E_{t}, \left| f_{n} \right| \leqslant \left| f \right|$ , and $f _ { n } ( x )   \to   f ( x )$ a.e. [µμ]. (Why?) Thus $| ( f _ { n } - f ) g | \leqslant 2 t | f |$ and $\int | f | d \mu = \int | f | \cdot 1 d \mu \leqslant \| f \| _ { p } \mu ( X ) ^ { 1 / q } < \infty$ By the Lebesgue Dominated Convergence Theorem, $F ( f _ { n } ) = \int f _ { n } g   d \mu \rightarrow \int f g   d \mu .$ Also, $| f _ { n } - f | ^ { p } \leqslant 2 ^ { p } | f | ^ { p } ,$ so $\| f _ { n } - f \| _ { p } \to 0 ;$ thus $F(f_n) \to \dot{F(f)}$ Combining these results we get that for any $t   >   0$ and any f in $L ^ { p } ( \mu )$ that vanishes off $E _ { t } , ( \mathbf { B } . 1 )$ holds.

Case 1a: $1 < p < \infty$ . So $1 < q < \infty$ . Let $f = \chi _ { E _ { t } } | g | ^ { q } / g ,$ where $g ( x ) \neq 0 ,$ and put $f ( x ) = 0$ when $g ( x ) = 0 .$ If $A = \{ x : g ( x ) \neq 0 \}$ , then

$$
\int | f | ^ { p } d \mu = \int _ { E _ { t } \cap A } \frac { | g | ^ { p q } } { | g | ^ { p } } d \mu = \int _ { E _ { t } } | g | ^ { q } d \mu .
$$

since $p q - p = q$ Therefore

$$
\int _ { E _ { t } } | g | ^ { q } d \mu = \int f g d \mu = F ( f ) \leqslant \| F \| \| f \| _ { p } = \| F \| \left[ \int _ { E _ { t } } | g | ^ { q } d \mu \right] ^ { 1 / p } .
$$

Thus

$$
\| F \| \geqslant \left[ \int_{E_t} |g|^q d\mu \right]^{1-1/p} \geqslant \left[ \int_{E_t} |g|^q d\mu \right]^{1/q}.
$$

Letting $t   \to   \infty$ gives that $g \parallel _ { q } \leqslant \| F \|$

Case 1b: $p = 1$ . So $q = \infty . \mathrm { F o r } \varepsilon > 0$ let $A = \{ x : | g ( x ) | > \| F \| + \varepsilon \}$ . For $t   >   0$ let $f = \chi _ { E _ { t } \cap A } \bar { g } / | g |$ . Then $\| f \| _ { 1 } = \mu ( A \cap E _ { t } ) ,$ and so

$$
\| F \| \mu ( A \cap E _ { t } ) \geqslant \int f g d \mu = \int _ { A \cap E _ { t } } | g | d \mu \geqslant ( \| F \| + \varepsilon ) \mu ( A \cap E _ { t } ) .
$$

Letting $t   \rightarrow   \infty$ we get that $\| F \| \mu ( A ) \geqslant ( \| F \| + \varepsilon ) \mu ( A )$ , which can only be if $\mu ( A ) = 0 .$ Thus $\| g \| _ { \infty } \leqslant \| F \|$

Case $2 { : } ( X ,   \Omega ,   \mu )$ is arbitrary. Let $\mathcal { E } = \mathbf { a } \mathbf { l } \mathbf { l }$ of the sets E in Ω such that $\mu ( E ) < \infty$ . For E in Ω let $\mathbf { \Omega } _ { E } = \left\{ \mathbf { \Delta }   \in   \mathbf { \Omega } : \mathbf { \Delta }   \subseteq   E \right\}$ and define $( \mu | E ) ( \Delta ) = \mu ( \Delta )$ for $\Delta \operatorname { i n } \Omega _ { E }$ Put $L ^ { p } ( \mu | E ) = L ^ { p } ( E , \Omega _ { E } , \mu | E )$ and notice that $L ^ { p } ( \mu | E )$ can be identified in a natural way with the functions in $L ^ { p } ( X , \Omega , \mu )$ that vanish off E. Make this identification and consider the restriction of $F \colon L ^ { p } ( \mu ) \to \mathbb { F }$ to $L ^ { p } ( \mu | E ) ;$

denote the restriction by $F _ { E } : L ^ { p } ( \mu | E ) \to \mathbb { F }$ Clearly $F _ { E }$ is bounded and $\| \boldsymbol { F } _ { E } \| \leqslant \| \boldsymbol { F } \|$ for every E in $\mathcal { E } .$

By Case 1, for every E in $\mathcal { E }$ there is a $g _ { E }$ in $L ^ { q } ( \mu | E )$ such that for f in $L ^ { p } ( \mu | E )$ 2

$$
F ( f ) = \int _ { E } f g _ { E } d \mu \mathrm { a n d } \| g _ { E } \| _ { q } \leqslant \| F \| .\tag{B.3}
$$

If $D , E   \in   { \pmb \delta } ,$ then $L ^ { p } ( \mu | D \cap E )$ is contained in both $L ^ { p } ( \mu | D )$ and $L ^ { p } ( \mu | E )$ Moreover, $F _ { D } | L ^ { p } ( \mu | D \cap E ) = F _ { E } | L ^ { p } ( \mu | D \cap E ) = F _ { D \cap E } .$ Hence $g _ { D } = g _ { E } = g _ { D \cap E }$ a.e. [µ] on $D \cap E$ .Thus, a function g can be defined on $\bigcup \left\{ E \colon E { \in } { \mathcal { E } } \right\}$ by letting $g = g _ { E }$ on $E ;$ put $g   =   0$ off $\bigcup \left\{ E \colon E { \in } { \mathcal { E } } \right\}$ . A difficulty arises here in trying to show that g is measurable.

Case 2a: $I < p < \infty$ . Put $\sigma = \operatorname* { s u p } \left\{ \left\| g _ { E } \right\| _ { q } : E { \in } { \mathcal { E } } \right\}$ ; so $\sigma \leqslant \| F \| < \infty$ . Since $\| g _ { D } \| _ { q } \leqslant \| g _ { E } \| _ { q } \text { if } D \subseteq E$ , there is a sequence $\{ E _ { n } \}$ in $\pmb { \mathscr { E } }$ such that $E _ { n } \subseteq E _ { n + 1 }$ for all n and $g _ { E _ { n } } \| _ { q }   \rightarrow   \sigma$ Let $G = \bigcup _ { n = 1 } ^ { \infty } E _ { n }$ If $E \in \mathcal { G }$ and $E \cap G = \square$ , then $\| g _ { E \cup E _ { n } } \| _ { q } ^ { q } = \| g _ { E } \| _ { q } ^ { q } + \| g _ { E _ { n } } \| _ { q } ^ { q } \to \| g _ { E } \| _ { q } ^ { q } + \sigma ^ { q } ;$ thus $g _ { E }   =   0$ Therefore $g   =   0$ off $G$ and clearly g is measurable. Moreover, $g   \in   L ^ { q } ( \mu )$ with $\| g \| _ { q } = \sigma .$

If $f   \in   L ^ { p } ( \mu ) .$ then $\left\{ x : f(x) \neq 0 \right\} = \bigcup_{n = 1}^{\infty} D_{n}$ where $D _ { n } \in \pmb { \delta }$ and $D_{n} \subseteq D_{n + 1}$ for all n. Thus $\chi _ { D _ { n } } f   \rightarrow   f$ in $L ^ { p } ( \mu )$ and so F( f) = lim $F(\chi_{D_n} f) = (B.3)$ lim $\int _ { D _ { n } } g f d \mu =$ $\int   g f d \mu .$ Thus $F = F _ { g }$ and $\| F \| = \| F_g \| \leqslant \| g \|_q \leqslant \sigma \leqslant \| F \|$

Case 2b: $p = \infty$ and (X,Ω, µ) is σ-finite. This is left to the reader. ■

## EXERCISE

Look at the proof of the theorem and see if you can represent $L ^ { 1 } ( X , \Omega , \mu ) ^ { * }$ for an arbitrary measure space.