# Appendix A. Preliminaries

<!-- OCR draft; page images require independent visual review. -->


<a id="pdf-page-384"></a>
# APPENDIX A

# Preliminaries

As was stated in the Preface, the prerequisites for understanding this book are a good course in measure and integration theory and, as a corequisite, analytic function theory. In this and the succeeding appendices an attempt is made to fill in some of the gaps and standardize some notation. These sections are not meant to be a substitute for serious study of these topics.

In Section 1 of this appendix some results from infinite dimensional linear algebra are set forth. Most of this is meant as review. Proposition 1.4, however, seems to be a fact that is not stressed or covered in courses but that is used often in functional analysis. Section 2 on topology is presented mainly to discuss nets. This topic is often not covered in the basic courses and it is especially useful in discussing various ideas and proving results in functional analysis.

## §1. Linear Algebra

Let $\mathcal{X}$ be a vector space over $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$. A subset $E$ of $\mathcal{X}$ is *linearly independent* if for any finite subset $\{e_1,\ldots,e_n\}$ of $E$ and for any finite set of scalars $\{\alpha_1,\ldots,\alpha_n\}$, if $\sum_{k=1}^{n}\alpha_k e_k=0$, then $\alpha_1=\cdots=\alpha_n=0$. A *Hamel basis* is a maximal linearly independent subset of $\mathcal{X}$.

**1.1. Proposition.** *If $E$ is a linearly independent subset of $\mathcal{X}$, then $E$ is a Hamel basis if and only if every vector $x$ in $\mathcal{X}$ can be written as $x=\sum_{k=1}^{n}\alpha_k e_k$ for scalars $\alpha_1,\ldots,\alpha_n$ and $\{e_1,\ldots,e_n\}\subseteq E$.*

**Proof.** Suppose $E$ is a basis and $x\in\mathcal{X}$, $x\notin E$. Then $E\cup\{x\}$ is not linearly independent. Thus there are $\alpha_0,\alpha_1,\ldots,\alpha_n$ in $\mathbb{F}$ and $e_1,\ldots,e_n$ in $E$ such that $0=\alpha_0x+\alpha_1e_1+\cdots+\alpha_ne_n$, with $\alpha_0\ne0$. (Why?) Thus $x=\sum_{k=1}^{n}(-\alpha_k/\alpha_0)e_k$.



<a id="pdf-page-385"></a>
Conversely, if $\mathscr{X}$ is the linear span of $E$, then for every $x$ in $\mathscr{X}\setminus E$, $E\cup\{x\}$ is not linearly independent. Thus $E$ is a basis. $\blacksquare$

**1.2. Proposition.** *If $E_0$ is a linearly independent subset of $\mathscr{X}$, then there is a basis $E$ that contains $E_0$.*

**Proof.** Use Zorn’s Lemma.

A *linear functional* on $\mathscr{X}$ is a function $f:\mathscr{X}\to\mathbb{F}$ such that $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$ for $x,y$ in $\mathscr{X}$ and $\alpha,\beta$ in $\mathbb{F}$. If $\mathscr{X}$ and $\mathscr{Y}$ are vector spaces over $\mathbb{F}$, a *linear transformation* from $\mathscr{X}$ into $\mathscr{Y}$ is a function $T:\mathscr{X}\to\mathscr{Y}$ such that $T(\alpha_1x_1+\alpha_2x_2)=\alpha_1T(x_1)+\alpha_2T(x_2)$ for $x_1,x_2$ in $\mathscr{X}$ and $\alpha_1,\alpha_2$ in $\mathbb{F}$.

If $A,B\subseteq\mathscr{X}$, then $A+B\equiv\{a+b:a\in A,\ b\in B\}$; $A-B\equiv\{a-b:a\in A,\ b\in B\}$. For $\alpha$ in $\mathbb{F}$ and $A\subseteq\mathscr{X}$, $\alpha A\equiv\{\alpha a:a\in A\}$. If $\mathcal{M}$ is a *linear manifold* in $\mathscr{X}$ (that is, $\mathcal{M}\subseteq\mathscr{X}$ and $\mathcal{M}$ is also a vector space with the same operations defined on $\mathscr{X}$), then define $\mathscr{X}/\mathcal{M}$ to be the collection of all the subsets of $\mathscr{X}$ of the form $x+\mathcal{M}$. A set of the form $x+\mathcal{M}$ is called a *coset* of $\mathcal{M}$. Note that $(x+\mathcal{M})+(y+\mathcal{M})=(x+y)+\mathcal{M}$ and $\alpha(x+\mathcal{M})=\alpha x+\mathcal{M}$ since $\mathcal{M}$ is a linear manifold. Hence $\mathscr{X}/\mathcal{M}$ becomes a vector space over $\mathbb{F}$. It is called the *quotient space* of $\mathscr{X}$ mod $\mathcal{M}$.

Define $Q:\mathscr{X}\to\mathscr{X}/\mathcal{M}$ by $Q(x)=x+\mathcal{M}$. It is easy to see that $Q$ is a linear transformation. It is called the *quotient map*.

If $T:\mathscr{X}\to\mathscr{Y}$ is a linear transformation,

$$
\begin{aligned}
\ker T&\equiv\{x\in\mathscr{X}:Tx=0\},\\
\operatorname{ran}T&\equiv\{Tx:x\in\mathscr{X}\};
\end{aligned}
$$

$\ker T$ is the *kernel* of $T$ and $\operatorname{ran}T$ is the *range* of $T$. If $\operatorname{ran}T=\mathscr{Y}$, $T$ is *surjective*; if $\ker T=(0)$, $T$ is *injective*. If $T$ is both injective and surjective, then $T$ is *bijective*. It is easy to see that the natural map $Q:\mathscr{X}\to\mathscr{X}/\mathcal{M}$ is surjective and $\ker Q=\mathcal{M}$.

Suppose now that $T:\mathscr{X}\to\mathscr{Y}$ is a linear transformation and $\mathcal{M}$ is a linear manifold in $\mathscr{X}$. We want to define a map $\hat T:\mathscr{X}/\mathcal{M}\to\mathscr{Y}$ by $\hat T(x+\mathcal{M})=Tx$. But $\hat T$ may not be well defined. To ensure that it is we must have $Tx_1=Tx_2$ if $x_1+\mathcal{M}=x_2+\mathcal{M}$. But $x_1+\mathcal{M}=x_2+\mathcal{M}$ if and only if $x_1-x_2\in\mathcal{M}$, and $Tx_1=Tx_2$ if and only if $x_1-x_2\in\ker T$. So $\hat T$ is well defined if $\mathcal{M}\subseteq\ker T$. It is easy to check that if $\hat T$ is well defined, $\hat T$ is linear.

**1.3. Proposition.** *If $T:\mathscr{X}\to\mathscr{Y}$ is a linear transformation and $\mathcal{M}$ is a linear manifold in $\mathscr{X}$ contained in $\ker T$, then there is a linear transformation $\hat T:\mathscr{X}/\mathcal{M}\to\mathscr{Y}$ such that the diagram*

![](assets/p0385-page_384_image_13.jpg)

*commutes.*



<a id="pdf-page-386"></a>
The preceding proposition is especially useful if $\mathcal M=\ker T$. In that case $\hat T$ is injective.

The last proposition of this section will be quite helpful in the book.

**1.4. Proposition.** *Let $f,f_1,\ldots,f_n$ be linear functionals in $\mathcal X$. If $\ker f\supseteq\bigcap_{k=1}^n\ker f_k$, then there are scalars $\alpha_1,\ldots,\alpha_n$ such that $f=\sum_{k=1}^n\alpha_kf_k$ (that is, $f(x)=\sum_{k=1}^n\alpha_kf_k(x)$ for every $x$ in $\mathcal X$).*

**Proof.** It may be assumed without loss of generality that for $1\leq k\leq n$,

$$
\bigcap_{j\ne k}\ker f_j\ne\bigcap_{j=1}^n\ker f_j.
$$

(Why?) So for $1\leq k\leq n$, there is a $y_k$ in $\bigcap_{j\ne k}\ker f_j$ such that $y_k\notin\bigcap_{j=1}^n\ker f_j$. So $f_j(y_k)=0$ for $j\ne k$, but $f_k(y_k)\ne0$. Let $x_k=[f_k(y_k)]^{-1}y_k$. Hence $f_k(x_k)=1$ and $f_j(x_k)=0$ for $j\ne k$.

Now let $f$ be as in the statement of the proposition and put $\alpha_k=f(x_k)$. If $x\in\mathcal X$, let $y=x-\sum_{k=1}^n f_k(x)x_k$. Then $f_j(y)=f_j(x)-\sum_{k=1}^n f_k(x)f_j(x_k)=0$. By hypothesis, $f(y)=0$. Thus

$$
\begin{aligned}
0&=f(x)-\sum_{k=1}^n f_k(x)f(x_k)\\[6pt]
 &=f(x)-\sum_{k=1}^n\alpha_kf_k(x);
\end{aligned}
$$

equivalently, $f=\sum_{k=1}^n\alpha_kf_k$. $\blacksquare$

## §2. Topology

In this book all topological spaces are assumed to be Hausdorff.

This section will review some of the concepts and results using *nets*, as this idea is frequently used in the text.

A *directed set* is a partially ordered set $(I,\leq)$ such that if $i_1,i_2\in I$, then there is an $i_3$ in $I$ such that $i_3\geq i_1$ and $i_3\geq i_2$. A good example of a directed set is to let $(X,\mathcal S)$ be a topological space and for a fixed $x_0$ in $X$ let $\mathcal U=\{U\text{ in }\mathcal S:x_0\in U\}$. If $U,V\in\mathcal U$, define $U\geq V$ if $U\subseteq V$ (so bigger is smaller). $\mathcal U$ is said to be *ordered by reverse inclusion*. Another example is found if $S$ is any set and $\mathcal F$ is the collection of all finite subsets of $S$. Define $F_1\geq F_2$ in $\mathcal F$ if $F_1\supseteq F_2$ (bigger means bigger). Here $\mathcal F$ is said to be *ordered by inclusion*. Both of these examples are used frequently in the text.

A *net* in $X$ is a pair $((I,\leq),x)$ where $(I,\leq)$ is a directed set and $x$ is a function from $I$ into $X$. Usually we will write $x_i$ instead of $x(i)$ and will use the phrase “let $\{x_i\}$ be a net in $X$.”

Note that $\mathbf N$, the natural numbers, is a directed set, so every sequence is



<a id="pdf-page-387"></a>
a net. If $(X,\mathcal T)$ is a topological space, $x_0\in X$, and $\mathcal U=\{U\text{ in }\mathcal T:x_0\in U\}$, then let $x_U\in U$ for every $U$ in $\mathcal U$. So $\{x_U:U\in\mathcal U\}$ is a net in $X$.

**2.1. Definition.** If $\{x_i\}$ is a net in a topological space $X$, then $\{x_i\}$ *converges* to $x_0$ (in symbols, $x_i\to x_0$ or $x_0=\lim x_i$) if for every open subset $U$ of $X$ such that $x_0\in U$, there is an $i_0=i_0(U)$ such that $x_i\in U$ for $i\geqslant i_0$. The net *clusters* at $x_0$ (in symbols, $x_i\xrightarrow[\mathrm{cl}]{}x_0$) if for every $i_0$ and for every open neighborhood $U$ of $x_0$, there exists an $i\geqslant i_0$ such that $x_i\in U$.

These notions generalize the corresponding concepts for sequences. Also, if $x_i\to x_0$, then $x_i\xrightarrow[\mathrm{cl}]{}x_0$. Note that the net $\{x_U:U\in\mathcal U\}$ defined just prior to the definition converges to $x_0$. This is a very important example of a convergent net.

**2.2. Proposition.** *If $X$ is a topological space and $A\subseteq X$, then $x\in\operatorname{cl}A$ (closure of $A$) if and only if there is a net $\{a_i\}$ in $A$ such that $a_i\to x$.*

**Proof.** Let $\mathcal U=\{U:U\text{ is open and }x\in U\}$. If $x\in\operatorname{cl}A$, then for each $U$ in $\mathcal U$ there is a point $a_U$ in $A\cap U$. If $U_0\in\mathcal U$, then $a_U\in U_0$ for every $U\geqslant U_0$; therefore $x=\lim a_U$. Conversely, if $\{a_i\}$ is a net in $A$ and $a_i\to x$, then each $U$ in $\mathcal U$ contains a point $a_i$ and $a_i\in A\cap U$. Thus $x\in\operatorname{cl}A$. $\blacksquare$

**2.3. Proposition.** *If $A\subseteq X$, $\{a_i\}$ is a net in $A$, and $a_i\xrightarrow[\mathrm{cl}]{}x$, then $x\in\operatorname{cl}A$.*

**Proof.** Exercise.

There is a concept of a subnet of a net and with this concept it is possible to prove that if a net clusters at a point $x$, then there is a subnet that converges to $x$. The concept of a subnet is, however, somewhat technical and is not what you might at first think it should be. Since this concept is not used in this book, the interested reader is referred to Kelley [1955]. It might also be appropriate to mention that a topological space is Hausdorff if and only if each convergent net has a unique limit point.

**2.4. Proposition.** *If $X$ and $Y$ are topological spaces and $f:X\to Y$, then $f$ is continuous at $x_0$ if and only if $f(x_i)\to f(x_0)$ whenever $x_i\to x_0$.*

**Proof.** First assume that $f$ is continuous at $x_0$ and let $\{x_i\}$ be a net in $X$ such that $x_i\to x_0$ in $X$. If $V$ is open in $Y$ and $f(x_0)\in V$, then there is an open set $U$ in $X$ such that $x_0\in U$ and $f(U)\subseteq V$. Let $i_0$ be such that $x_i\in U$ for $i\geqslant i_0$. Hence $f(x_i)\in V$ for $i\geqslant i_0$. This says that $f(x_i)\to f(x_0)$.

Let $\mathcal U=\{U:U\text{ is open in }X\text{ and }x_0\in U\}$. Suppose $f$ is not continuous at $x_0$. Then there is an open subset $V$ of $Y$ such that $f(x_0)\in V$ and $f(U)\setminus V\neq\square$ for every $U$ in $\mathcal U$. Thus for each $U$ in $\mathcal U$ there is a point $x_U$ in $U$ with $f(x_U)\notin V$. But $\{x_U\}$ is a net in $X$ with $x_U\to x_0$ and clearly $\{f(x_U)\}$ cannot converge to $f(x_0)$. $\blacksquare$



<a id="pdf-page-388"></a>
**2.5. Proposition.** *If $f:X\to Y$, $f$ is continuous at $x_0$, and $\{x_i\}$ is a net in $X$ that clusters at $x_0$, then $\{f(x_i)\}$ clusters at $f(x_0)$.*

**Proof.** Exercise.

**2.6. Proposition.** *Let $K\subseteq X$. Then $K$ is compact if and only if each net in $K$ has a cluster point in $K$.*

**Pproof.** Suppose that $K$ is compact and let $\{x_i:i\in I\}$ be a net in $K$. For each $i$ let $F_i=\operatorname{cl}\{x_j:j\geq i\}$, so each $F_i$ is a closed subset of $K$. It will be shown that $\{F_i:i\in I\}$ has the finite intersection property. In fact, since $I$ is directed, if $i_1,\ldots,i_n\in I$, then there is an $i\geq i_1,\ldots,i_n$. Thus $F_i\subseteq\bigcap_{k=1}^{n}F_{i_k}$ and $\{F_i\}$ has the finite intersection property. Because $K$ is compact, there is an $x_0$ in $\bigcap_i F_i$. But if $U$ is open with $x_0$ in $U$ and $i_0\in I$, the fact that $x_0\in\operatorname{cl}\{x_i:i\geq i_0\}$ implies there is an $i\geq i_0$ with $x_i$ in $U$. Thus $x_i\xrightarrow[\mathrm{cl}]{}x_0$.

Now assume that each net in $K$ has a cluster point in $K$. Let $\{K_\alpha:\alpha\in A\}$ be a collection of relatively closed subsets of $K$ having the finite intersection property. If $\mathcal{F}=$ the collection of all finite subsets of $A$, order $\mathcal{F}$ by inclusion. By hypothesis, if $F\in\mathcal{F}$, there is a point $x_F$ in $\bigcap\{K_\alpha:\alpha\in F\}$. Thus $\{x_F\}$ is a net in $K$. By hypothesis, $\{x_F\}$ has a cluster point $x_0$ in $K$. Let $\alpha\in A$, so $\{\alpha\}\in\mathcal{F}$. Thus if $U$ is any open set containing $x_0$ there is an $F$ in $\mathcal{F}$ such that $\alpha\in F$ and $x_F\in U$. Thus $x_F\in U\cap K_\alpha$; that is, for each $\alpha$ in $A$ and for every open set $U$ containing $x_0$, $U\cap K_\alpha\ne\square$. Since $K_\alpha$ is relatively closed, $x_0\in K_\alpha$ for each $\alpha$ in $A$. Thus $x_0\in\bigcap_\alpha K_\alpha$ and $K$ must be compact. $\blacksquare$

The next result is used repeatedly in this book.

**2.7. Proposition.** *If $X$ is compact, $\{x_i\}$ is a net in $X$, and $x_0$ is the only cluster point of $\{x_i\}$, then the net $\{x_i\}$ converges to $x_0$.*

**Proof.** Let $U$ be an open neighborhood of $x_0$ and let $J=\{j\in I:x_j\notin U\}$. If $\{x_i\}$ does not converge to $x_0$, then for every $i$ in $I$ there is a $j$ in $J$ such that $j\geq i$. In particular, $J$ is also a directed set. Hence $\{x_j:j\in J\}$ is a net in the compact set $X\setminus U$. Thus it has a cluster point $y_0$. But the property of $J$ mentioned before implies that $y_0$ is also a cluster point of $\{x_i:j\in I\}$, contradicting the assumption. Thus $x_i\to x_0$. $\blacksquare$

The next result is rather easy, but it will be used so often that it should be explicitly stated and proved.

**2.8. Proposition.** *If $f:X\to Y$ is bijective and continuous and $X$ is compact, then $f$ is a homeomorphism.*

**Proof.** If $F$ is a closed subset of $X$, then $F$ is compact. Thus $f(F)$ is compact in $Y$ and hence closed. Since $f$ maps closed sets to closed sets, $f^{-1}$ is continuous. $\blacksquare$



<a id="pdf-page-389"></a>
Note that the Hausdorff property was used in the preceding proof when we said that a compact subset of $Y$ is closed.

In the study of functional analysis it is often the case that the mathematician is presented with a set that has two topologies. It is useful to know how properties of one topology relate to the other and when the two topologies are, in fact, one.

If $X$ is a set and $\mathcal{T}_1,\mathcal{T}_2$ are two topologies on $X$, say that $\mathcal{T}_2$ is *larger* or *stronger* than $\mathcal{T}_1$ if $\mathcal{T}_2\supseteq\mathcal{T}_1$; in this case you may also say that $\mathcal{T}_1$ is *smaller* or *weaker*. In the literature there is also an unfortunate nomenclature for these concepts; the words “finer” and “coarser” are used.

The following result is easy to prove (it is an exercise) but it is enormously useful in discussing a set with two topologies.

**2.9. Lemma.** *If $\mathcal{T}_1,\mathcal{T}_2$ are topologies on $X$, then $\mathcal{T}_2$ is larger than $\mathcal{T}_1$ if and only if the identity map $i:(X,\mathcal{T}_2)\to(X,\mathcal{T}_1)$ is continuous.*

**2.10. Proposition.** *Let $\mathcal{T}_1,\mathcal{T}_2$ be topologies on $X$ and assume that $\mathcal{T}_2$ is larger than $\mathcal{T}_1$.*

(a) *If $F$ is $\mathcal{T}_1$-closed, $F$ is $\mathcal{T}_2$-closed.*

(b) *If $f:Y\to(X,\mathcal{T}_2)$ is continuous, then $f:Y\to(X,\mathcal{T}_1)$ is continuous.*

(c) *If $f(X,\mathcal{T}_1)\to Y$ is continuous, then $f:(X,\mathcal{T}_2)\to Y$ is continuous.*

(d) *If $K$ is $\mathcal{T}_2$-compact, then $K$ is $\mathcal{T}_1$-compact.*

(e) *If $X$ is $\mathcal{T}_2$-compact, then $\mathcal{T}_1=\mathcal{T}_2$.*

**Proof.** (b) Note that $f:Y\to(X,\mathcal{T}_1)$ is the composition of $f:Y\to(X,\mathcal{T}_2)$ and $i:(X,\mathcal{T}_2)\to(X,\mathcal{T}_1)$ and use Lemma 2.9.

(d) Use Lemma 2.9.

(e) Use Lemma 2.9 and Proposition 2.8.

The remainder of the proof is an exercise. $\blacksquare$

