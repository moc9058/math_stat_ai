# 1. The Hahn–Banach Theorems. Introduction to the Theory of Conjugate Convex Functions


<a id="pdf-page-16"></a>
# Chapter 1

# The Hahn–Banach Theorems. Introduction to the Theory of Conjugate Convex Functions

## 1.1 The Analytic Form of the Hahn–Banach Theorem: Extension of Linear Functionals

Let $E$ be a vector space over $\mathbb{R}$. We recall that a *functional* is a function defined on $E$, or on some subspace of $E$, *with values in* $\mathbb{R}$. The main result of this section concerns the extension of a linear functional defined on a linear subspace of $E$ by a linear functional defined on all of $E$.

**Theorem 1.1 (Helly, Hahn–Banach analytic form).** *Let $p:E\to\mathbb{R}$ be a function satisfying*[^1]

$$
p(\lambda x)=\lambda p(x) \qquad \forall x\in E \quad\text{and}\quad \forall\lambda>0, \tag{1}
$$

$$
p(x+y)\leq p(x)+p(y) \qquad \forall x,y\in E. \tag{2}
$$

*Let $G\subset E$ be a linear subspace and let $g:G\to\mathbb{R}$ be a linear functional such that*

$$
g(x)\leq p(x) \qquad \forall x\in G. \tag{3}
$$

*Under these assumptions, there exists a linear functional $f$ defined on all of $E$ that extends $g$, i.e., $g(x)=f(x)$ $\forall x\in G$, and such that*

$$
f(x)\leq p(x) \qquad \forall x\in E. \tag{4}
$$

The proof of Theorem 1.1 depends on Zorn’s lemma, which is a celebrated and very useful property of ordered sets. Before stating Zorn’s lemma we must clarify some notions. Let $P$ be a set with a (partial) order relation $\leq$. We say that a subset $Q\subset P$ is *totally ordered* if for any pair $(a,b)$ in $Q$ either $a\leq b$ or $b\leq a$ (or both!). Let $Q\subset P$ be a subset of $P$; we say that $c\in P$ is an *upper bound* for $Q$ if $a\leq c$ for every $a\in Q$. We say that $m\in P$ is a *maximal* element of $P$ if there is no element

[^1]: A function $p$ satisfying (1) and (2) is sometimes called a *Minkowski functional*.

H. Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*, DOI 10.1007/978-0-387-70914-7_1, © Springer Science+Business Media, LLC 2011



<a id="pdf-page-17"></a>
$x\in P$ such that $m\leq x$, except for $x=m$. Note that a maximal element of $P$ need not be an upper bound for $P$.

We say that $P$ is *inductive* if every totally ordered subset $Q$ in $P$ has an upper bound.

• **Lemma 1.1 (Zorn).** *Every nonempty ordered set that is inductive has a maximal element.*

Zorn’s lemma follows from the axiom of choice, but we shall not discuss its derivation here; see, e.g., J. Dugundji [1], N. Dunford–J. T. Schwartz [1] (Volume 1, Theorem 1.2.7), E. Hewitt–K. Stromberg [1], S. Lang [1], and A. Knapp [1].

*Remark 1.* Zorn’s lemma has many important applications in analysis. It is a *basic tool* in proving some *seemingly innocent existence statements* such as “every vector space has a basis” (see Exercise 1.5) and “on any vector space there are nontrivial linear functionals.” Most analysts do not know how to prove Zorn’s lemma; but it is quite essential for an analyst to understand the statement of Zorn’s lemma and to be able to use it properly!

*Proof of Lemma 1.2.* Consider the set

$$
P=\left\{h:D(h)\subset E\to\mathbb{R}\ \middle|\ \begin{aligned}
&D(h)\text{ is a linear subspace of }E,\\
&h\text{ is linear, }G\subset D(h),\\
&h\text{ extends }g,\text{ and }h(x)\leq p(x)\quad\forall x\in D(h)
\end{aligned}\right\}.
$$

On $P$ we define the order relation

$$
(h_1\leq h_2)\iff(D(h_1)\subset D(h_2)\text{ and }h_2\text{ extends }h_1).
$$

It is clear that $P$ is nonempty, since $g\in P$. We claim that $P$ is *inductive*. Indeed, let $Q\subset P$ be a totally ordered subset; we write $Q$ as $\mathcal{Q}=(h_i)_{i\in I}$ and we set

$$
D(h)=\bigcup_{i\in I}D(h_i),\qquad h(x)=h_i(x)\quad\text{if }x\in D(h_i)\text{ for some }i.
$$

It is easy to see that the definition of $h$ makes sense, that $h\in P$, and that $h$ is an upper bound for $Q$. We may therefore apply Zorn’s lemma, and so we have a maximal element $f$ in $P$. We claim that $D(f)=E$, which completes the proof of Theorem 1.1.

Suppose, by contradiction, that $D(f)\neq E$. Let $x_0\notin D(f)$; set $D(h)=D(f)+\mathbb{R}x_0$, and for every $x\in D(f)$, set $h(x+tx_0)=f(x)+t\alpha$ $(t\in\mathbb{R})$, where the constant $\alpha\in\mathbb{R}$ will be chosen in such a way that $h\in P$. We must ensure that

$$
f(x)+t\alpha\leq p(x+tx_0)\qquad \forall x\in D(f)\quad\text{and}\quad\forall t\in\mathbb{R}.
$$

In view of (1) it suffices to check that



<a id="pdf-page-18"></a>
$$
\begin{cases}
f(x)+\alpha\leq p(x+x_0) & \forall x\in D(f),\\
f(x)-\alpha\leq p(x-x_0) & \forall x\in D(f).
\end{cases}
$$

In other words, we must find some $\alpha$ satisfying

$$
\sup_{y\in D(f)}\{f(y)-p(y-x_0)\}\leq\alpha\leq\inf_{x\in D(f)}\{p(x+x_0)-f(x)\}.
$$

Such an $\alpha$ exists, since

$$
f(y)-p(y-x_0)\leq p(x+x_0)-f(x)\qquad\forall x\in D(f),\quad\forall y\in D(f);
$$

indeed, it follows from (2) that

$$
f(x)+f(y)\leq p(x+y)\leq p(x+x_0)+p(y-x_0).
$$

We conclude that $f\leq h$; but this is impossible, since $f$ is maximal and $h\neq f$.

We now describe some simple applications of Theorem 1.1 to the case in which $E$ is a *normed vector space* (n.v.s.) with norm $\|\ \|$.

**Notation.** We denote by $E^*$ the *dual space* of $E$, that is, the space of all *continuous linear functionals* on $E$; the (dual) *norm on* $E^*$ is defined by

$$
\|f\|_{E^*}=\sup_{\substack{\|x\|\leq1\\x\in E}}|f(x)|
=\sup_{\substack{\|x\|\leq1\\x\in E}}f(x). \tag{5}
$$

When there is no confusion we shall also write $\|f\|$ instead of $\|f\|_{E^*}$.

Given $f\in E^*$ and $x\in E$ we shall often write $\langle f,x\rangle$ instead of $f(x)$; we say that $\langle\ ,\ \rangle$ is the scalar product for the duality $E^*,E$.

It is well known that $E^*$ is a Banach space, i.e., $E^*$ is complete (even if $E$ is not); this follows from the fact that $\mathbb{R}$ is complete.

• **Corollary 1.2.** *Let $G\subset E$ be a linear subspace. If $g:G\to\mathbb{R}$ is a continuous linear functional, then there exists $f\in E^*$ that extends $g$ and such that*

$$
\|f\|_{E^*}=\sup_{\substack{x\in G\\\|x\|\leq1}}|g(x)|=\|g\|_{G^*}.
$$

*Proof.* Use Theorem 1.1 with $p(x)=\|g\|_{G^*}\|x\|$.

• **Corollary 1.3.** *For every $x_0\in E$ there exists $f_0\in E^*$ such that*

$$
\|f_0\|=\|x_0\|\quad\text{and}\quad\langle f_0,x_0\rangle=\|x_0\|^2.
$$

*Proof.* Use Corollary 1.2 with $G=\mathbb{R}x_0$ and $g(tx_0)=t\|x_0\|^2$, so that $\|g\|_{G^*}=\|x_0\|$.

*Remark 2.* The element $f_0$ given by Corollary 1.3 is in general not unique (try to construct an example or see Exercise 1.2). However, if $E^*$ is strictly con-



<a id="pdf-page-19"></a>
vex[^2]—for example if $E$ is a Hilbert space (see Chapter 5) or if $E=L^p(\Omega)$ with $1<p<\infty$ (see Chapter 4)—then $f_0$ is unique. In general, we set, for every $x_0\in E$,

$$
F(x_0)=\left\{f_0\in E^*;\ \|f_0\|=\|x_0\|\text{ and }\langle f_0,x_0\rangle=\|x_0\|^2\right\}.
$$

The (multivalued) map $x_0\mapsto F(x_0)$ is called the *duality map* from $E$ into $E^*$; some of its properties are described in Exercises 1.1, 1.2, and 3.28 and Problem 13.

• **Corollary 1.4.** *For every $x\in E$ we have*

$$
\|x\|=\sup_{\substack{f\in E^*\\\|f\|\leq1}}|\langle f,x\rangle|
=\max_{\substack{f\in E^*\\\|f\|\leq1}}|\langle f,x\rangle|. \tag{6}
$$

*Proof.* We may always assume that $x\neq0$. It is clear that

$$
\sup_{\substack{f\in E^*\\\|f\|\leq1}}|\langle f,x\rangle|\leq\|x\|.
$$

On the other hand, we know from Corollary 1.3 that there is some $f_0\in E^*$ such that $\|f_0\|=\|x\|$ and $\langle f_0,x\rangle=\|x\|^2$. Set $f_1=f_0/\|x\|$, so that $\|f_1\|=1$ and $\langle f_1,x\rangle=\|x\|$.

*Remark 3.* Formula (5)—which is a *definition*—should not be confused with formula (6), which is a *statement*. In general, the “sup” in (5) is *not achieved*; see, e.g., Exercise 1.3. However, the “sup” in (5) is achieved if $E$ is a reflexive Banach space (see Chapter 3); a deep result due to R. C. James asserts the converse: if $E$ is a Banach space such that for every $f\in E^*$ the sup in (5) is achieved, then $E$ is reflexive; see, e.g., J. Diestel [1, Chapter 1] or R. Holmes [1].

## 1.2 The Geometric Forms of the Hahn–Banach Theorem: Separation of Convex Sets

We start with some preliminary facts about hyperplanes. In the following, $E$ denotes an n.v.s.

**Definition.** An affine *hyperplane* is a subset $H$ of $E$ of the form

$$
H=\{x\in E;\ f(x)=\alpha\},
$$

where $f$ is a linear functional[^3] that does not vanish identically and $\alpha\in\mathbb{R}$ is a given constant. We write $H=[f=\alpha]$ and say that $f=\alpha$ is the equation of $H$.

[^2]: A normed space is said to be *strictly convex* if $\|tx+(1-t)y\|<1$, $\forall t\in(0,1)$, $\forall x,y$ with $\|x\|=\|y\|=1$ and $x\neq y$; see Exercise 1.26.

[^3]: We do not assume that $f$ is continuous (in every infinite-dimensional normed space there exist discontinuous linear functionals; see Exercise 1.5).



<a id="pdf-page-20"></a>
**Proposition 1.5.** *The hyperplane $H=[f=\alpha]$ is closed if and only if $f$ is continuous.*

*Proof.* It is clear that if $f$ is continuous then $H$ is closed. Conversely, let us assume that $H$ is closed. The complement $H^c$ of $H$ is open and nonempty (since $f$ does not vanish identically). Let $x_0\in H^c$, so that $f(x_0)\neq\alpha$, for example, $f(x_0)<\alpha$.

Fix $r>0$ such that $B(x_0,r)\subset H^c$, where

$$
B(x_0,r)=\{x\in E;\ \|x-x_0\|<r\}.
$$

We claim that

$$
f(x)<\alpha\qquad\forall x\in B(x_0,r). \tag{7}
$$

Indeed, suppose by contradiction that $f(x_1)>\alpha$ for some $x_1\in B(x_0,r)$. The segment

$$
\{x_t=(1-t)x_0+tx_1;\ t\in[0,1]\}
$$

is contained in $B(x_0,r)$ and thus $f(x_t)\neq\alpha$, $\forall t\in[0,1]$; on the other hand, $f(x_t)=\alpha$ for some $t\in[0,1]$, namely $t=\frac{f(x_1)-\alpha}{f(x_1)-f(x_0)}$, a contradiction, and thus (7) is proved. It follows from (7) that

$$
f(x_0+rz)<\alpha\qquad\forall z\in B(0,1).
$$

Consequently, $f$ is continuous and $\|f\|\leq\frac{1}{r}(\alpha-f(x_0))$.

**Definition.** Let $A$ and $B$ be two subsets of $E$. We say that the hyperplane $H=[f=\alpha]$ *separates* $A$ and $B$ if

$$
\boxed{f(x)\leq\alpha\quad\forall x\in A\quad\text{and}\quad f(x)\geq\alpha\quad\forall x\in B.}
$$

We say that $H$ *strictly separates* $A$ and $B$ if there exists some $\varepsilon>0$ such that

$$
\boxed{f(x)\leq\alpha-\varepsilon\quad\forall x\in A\quad\text{and}\quad f(x)\geq\alpha+\varepsilon\quad\forall x\in B.}
$$

*Geometrically*, the separation means that $A$ lies in one of the half-spaces determined by $H$, and $B$ lies in the other; see Figure 1.

Finally, we recall that a subset $A\subset E$ is *convex* if

$$
\boxed{tx+(1-t)y\in A\quad\forall x,y\in A,\quad\forall t\in[0,1].}
$$

• **Theorem 1.6 (Hahn–Banach, first geometric form).** *Let $A\subset E$ and $B\subset E$ be two nonempty convex subsets such that $A\cap B=\varnothing$. Assume that one of them is open. Then there exists a closed hyperplane that separates $A$ and $B$.*

The proof of Theorem 1.6 relies on the following two lemmas.

**Lemma 1.2.** *Let $C\subset E$ be an open convex set with $0\in C$. For every $x\in E$ set*



<a id="pdf-page-21"></a>
![](assets/p0021-page_20_image_2.jpg)

**Fig. 1**

$$
p(x)=\inf\{\alpha>0;\ \alpha^{-1}x\in C\}. \tag{8}
$$

*($p$ is called the gauge of $C$ or the Minkowski functional of $C$).*

*Then $p$ satisfies (1), (2), and the following properties:*

$$
\text{there is a constant }M\text{ such that }0\leq p(x)\leq M\|x\|\quad\forall x\in E, \tag{9}
$$

$$
C=\{x\in E;\ p(x)<1\}. \tag{10}
$$

*Proof of Lemma 1.2.* It is obvious that (1) holds.

*Proof of (9).* Let $r>0$ be such that $B(0,r)\subset C$; we clearly have

$$
p(x)\leq\frac{1}{r}\|x\|\qquad\forall x\in E.
$$

*Proof of (10).* First, suppose that $x\in C$; since $C$ is open, it follows that $(1+\varepsilon)x\in C$ for $\varepsilon>0$ small enough and therefore $p(x)\leq\frac{1}{1+\varepsilon}<1$. Conversely, if $p(x)<1$ there exists $\alpha\in(0,1)$ such that $\alpha^{-1}x\in C$, and thus $x=\alpha(\alpha^{-1}x)+(1-\alpha)0\in C$.

*Proof of (2).* Let $x,y\in E$ and let $\varepsilon>0$. Using (1) and (10) we obtain that $\frac{x}{p(x)+\varepsilon}\in C$ and $\frac{y}{p(y)+\varepsilon}\in C$. Thus $\frac{tx}{p(x)+\varepsilon}+\frac{(1-t)y}{p(y)+\varepsilon}\in C$ for all $t\in[0,1]$. Choosing the value $t=\frac{p(x)+\varepsilon}{p(x)+p(y)+2\varepsilon}$, we find that $\frac{x+y}{p(x)+p(y)+2\varepsilon}\in C$. Using (1) and (10) once more, we are led to $p(x+y)<p(x)+p(y)+2\varepsilon$, $\forall\varepsilon>0$.

**Lemma 1.3.** *Let $C\subset E$ be a nonempty open convex set and let $x_0\in E$ with $x_0\notin C$. Then there exists $f\in E^*$ such that $f(x)<f(x_0)$ $\forall x\in C$. In particular, the hyperplane $[f=f(x_0)]$ separates $\{x_0\}$ and $C$.*

*Proof of Lemma 1.3.* After a translation we may always assume that $0\in C$. We may thus introduce the gauge $p$ of $C$ (see Lemma 1.2). Consider the linear subspace $G=\mathbb{R}x_0$ and the linear functional $g:G\to\mathbb{R}$ defined by



<a id="pdf-page-22"></a>
$$
g(tx_0)=t,\qquad t\in\mathbb{R}.
$$

It is clear that

$$
g(x)\leq p(x)\qquad\forall x\in G
$$

(consider the two cases $t>0$ and $t\leq0$). It follows from Theorem 1.1 that there exists a linear functional $f$ on $E$ that extends $g$ and satisfies

$$
f(x)\leq p(x)\qquad\forall x\in E.
$$

In particular, we have $f(x_0)=1$ and that $f$ is continuous by (9). We deduce from (10) that $f(x)<1$ for every $x\in C$.

*Proof of Theorem 1.6.* Set $C=A-B$, so that $C$ is convex (check!), $C$ is open (since $C=\bigcup_{y\in B}(A-y)$), and $0\notin C$ (because $A\cap B=\varnothing$). By Lemma 1.3 there is some $f\in E^*$ such that

$$
f(z)<0\qquad\forall z\in C,
$$

that is,

$$
f(x)<f(y)\qquad\forall x\in A,\quad\forall y\in B.
$$

Fix a constant $\alpha$ satisfying

$$
\sup_{x\in A}f(x)\leq\alpha\leq\inf_{y\in B}f(y).
$$

Clearly, the hyperplane $[f=\alpha]$ separates $A$ and $B$.

• **Theorem 1.7 (Hahn–Banach, second geometric form).** *Let $A\subset E$ and $B\subset E$ be two nonempty convex subsets such that $A\cap B=\varnothing$. Assume that $A$ is closed and $B$ is compact. Then there exists a closed hyperplane that strictly separates $A$ and $B$.*

*Proof.* Set $C=A-B$, so that $C$ is convex, closed (check!), and $0\notin C$. Hence, there is some $r>0$ such that $B(0,r)\cap C=\varnothing$. By Theorem 1.6 there is a closed hyperplane that separates $B(0,r)$ and $C$. Therefore, there is some $f\in E^*$, $f\not\equiv0$, such that

$$
f(x-y)\leq f(rz)\qquad\forall x\in A,\quad\forall y\in B,\quad\forall z\in B(0,1).
$$

It follows that $f(x-y)\leq-r\|f\|$ $\forall x\in A$, $\forall y\in B$. Letting $\varepsilon=\frac{1}{2}r\|f\|>0$, we obtain

$$
f(x)+\varepsilon\leq f(y)-\varepsilon\qquad\forall x\in A,\quad\forall y\in B.
$$

Choosing $\alpha$ such that

$$
\sup_{x\in A}f(x)+\varepsilon\leq\alpha\leq\inf_{y\in B}f(y)-\varepsilon,
$$

we see that the hyperplane $[f=\alpha]$ strictly separates $A$ and $B$.

*Remark 4.* Assume that $A\subset E$ and $B\subset E$ are two nonempty convex sets such that $A\cap B=\varnothing$. If we make *no further assumption*, it is in general *impossible* to separate



<a id="pdf-page-23"></a>
A and B by a closed hyperplane. One can even construct such an example in which $A$ and $B$ are both closed (see Exercise 1.14). However, if $E$ is finite-dimensional one can always separate any two nonempty convex sets $A$ and $B$ such that $A \cap B = \varnothing$ (no further assumption is required!); see Exercise 1.9.

We conclude this section with a very useful fact:

**• Corollary 1.8.** *Let $F \subset E$ be a linear subspace such that $\overline{F} \ne E$. Then there exists some $f \in E^\star$, $f \not\equiv 0$, such that*

$$
\langle f,x\rangle=0 \qquad \forall x\in F.
$$

*Proof.* Let $x_0\in E$ with $x_0\notin\overline F$. Using Theorem 1.7 with $A=\overline F$ and $B=\{x_0\}$, we find a closed hyperplane $[f=\alpha]$ that strictly separates $\overline F$ and $\{x_0\}$. Thus, we have

$$
\langle f,x\rangle<\alpha<\langle f,x_0\rangle \qquad \forall x\in F.
$$

It follows that $\langle f,x\rangle=0$ $\forall x\in F$, since $\lambda\langle f,x\rangle<\alpha$ for every $\lambda\in\mathbb R$.

**• Remark 5.** Corollary 1.8 is used very often in proving that a linear subspace $F\subset E$ is dense. It suffices to show that *every continuous linear functional on $E$ that vanishes on $F$ must vanish everywhere on $E$*.

## 1.3 The Bidual $E^{\star\star}$. Orthogonality Relations

Let $E$ be an n.v.s. and let $E^\star$ be the dual space with norm

$$
\|f\|_{E^\star}=\sup_{\substack{x\in E\\\|x\|\le 1}}|\langle f,x\rangle|.
$$

The bidual $E^{\star\star}$ is the dual of $E^\star$ with norm

$$
\|\xi\|_{E^{\star\star}}=\sup_{\substack{f\in E^\star\\\|f\|\le 1}}|\langle\xi,f\rangle| \qquad (\xi\in E^{\star\star}).
$$

There is a *canonical injection* $J:E\to E^{\star\star}$ defined as follows: given $x\in E$, the map $f\mapsto\langle f,x\rangle$ is a continuous linear functional on $E^\star$; thus it is an element of $E^{\star\star}$, which we denote by $Jx$.⁴ We have

$$
\langle Jx,f\rangle_{E^{\star\star},E^\star}=\langle f,x\rangle_{E^\star,E}
\qquad \forall x\in E,\quad\forall f\in E^\star.
$$

It is clear that $J$ is linear and that $J$ is an *isometry*, that is, $\|Jx\|_{E^{\star\star}}=\|x\|_E$; indeed, we have

---

⁴ $J$ should not be confused with the duality map $F:E\to E^\star$ defined in Remark 2.



<a id="pdf-page-24"></a>
$$
\|Jx\|_{E^{\star\star}}=\sup_{\substack{f\in E^\star\\\|f\|\le1}}|\langle Jx,f\rangle|
=\sup_{\substack{f\in E^\star\\\|f\|\le1}}|\langle f,x\rangle|=\|x\|
$$

(by Corollary 1.4).

It may happen that $J$ is *not surjective* from $E$ onto $E^{\star\star}$ (see Chapters 3 and 4). However, it is convenient to *identify $E$ with a subspace of $E^{\star\star}$ using $J$*. If $J$ turns out to be surjective then one says that $E$ is reflexive, and $E^{\star\star}$ is identified with $E$ (see Chapter 3).

**Notation.** If $M\subset E$ is a linear subspace we set

$$
\boxed{M^\perp=\{f\in E^\star;\ \langle f,x\rangle=0\quad\forall x\in M\}.}
$$

If $N\subset E^\star$ is a linear subspace we set

$$
\boxed{N^\perp=\{x\in E;\ \langle f,x\rangle=0\quad\forall f\in N\}.}
$$

Note that—by definition—$N^\perp$ is a subset of $E$ *rather than* $E^{\star\star}$. It is clear that $M^\perp$ (resp. $N^\perp$) is a closed linear subspace of $E^\star$ (resp. $E$). We say that $M^\perp$ (resp. $N^\perp$) is the space orthogonal to $M$ (resp. $N$).

**Proposition 1.9.** *Let $M\subset E$ be a linear subspace. Then*

$$
\boxed{(M^\perp)^\perp=\overline M.}
$$

*Let $N\subset E^\star$ be a linear subspace. Then*

$$
(N^\perp)^\perp\supset\overline N.
$$

*Proof.* It is clear that $M\subset(M^\perp)^\perp$, and since $(M^\perp)^\perp$ is closed we have $\overline M\subset(M^\perp)^\perp$. Conversely, let us show that $(M^\perp)^\perp\subset\overline M$. Suppose by contradiction that there is some $x_0\in(M^\perp)^\perp$ such that $x_0\notin\overline M$. By Theorem 1.7 there is a closed hyperplane that strictly separates $\{x_0\}$ and $\overline M$. Thus, there are some $f\in E^\star$ and some $\alpha\in\mathbb R$ such that

$$
\langle f,x\rangle<\alpha<\langle f,x_0\rangle \qquad \forall x\in M.
$$

Since $M$ is a linear space it follows that $\langle f,x\rangle=0$ $\forall x\in M$ and also $\langle f,x_0\rangle>0$. Therefore $f\in M^\perp$ and consequently $\langle f,x_0\rangle=0$, a contradiction.

It is also clear that $N\subset(N^\perp)^\perp$ and thus $\overline N\subset(N^\perp)^\perp$.

*Remark 6.* It may happen that $(N^\perp)^\perp$ is strictly bigger than $\overline N$ (see Exercise 1.16). It is, however, instructive to “try” to prove that $(N^\perp)^\perp=\overline N$ and see where the argument breaks down. Suppose $f_0\in E^\star$ is such that $f_0\in(N^\perp)^\perp$ and $f_0\notin\overline N$. Applying Hahn–Banach in $E^\star$, we may strictly separate $\{f_0\}$ and $\overline N$. Thus, there is some $\xi\in E^{\star\star}$ such that $\langle\xi,f_0\rangle>0$. But we cannot derive a contradiction, since



<a id="pdf-page-25"></a>
$\xi\notin N^\perp$—unless we happen to know (by chance!) that $\xi\in E$, or more precisely that $\xi=Jx_0$ for some $x_0\in E$. In particular, if $E$ is reflexive, it is indeed true that $(N^\perp)^\perp=\overline N$. In the general case one can show that $(N^\perp)^\perp$ coincides with the closure of $N$ in the weak$^\star$ topology $\sigma(E^\star,E)$ (see Chapter 3).

## 1.4 A Quick Introduction to the Theory of Conjugate Convex Functions

We start with some basic facts about lower semicontinuous functions and convex functions. In this section we consider functions $\varphi$ defined on a set $E$ with values in $(-\infty,+\infty]$, so that $\varphi$ can take the value $+\infty$ (but $-\infty$ is excluded). We denote by $D(\varphi)$ the domain of $\varphi$, that is,

$$
\boxed{D(\varphi)=\{x\in E;\ \varphi(x)<+\infty\}.}
$$

**Notation.** The *epigraph* of $\varphi$ is the set⁵

$$
\operatorname{epi}\varphi=\{[x,\lambda]\in E\times\mathbb R;\ \varphi(x)\le\lambda\}.
$$

We assume now that $E$ is a *topological space*. We recall the following.

**Definition.** A function $\varphi:E\to(-\infty,+\infty]$ is said to be *lower semicontinuous* (l.s.c.) if for every $\lambda\in\mathbb R$ the set

$$
[\varphi\le\lambda]=\{x\in E;\ \varphi(x)\le\lambda\}
$$

is closed.

Here are some well-known elementary facts about l.s.c. functions (see, e.g., G. Choquet, [1], J. Dixmier [1], J. R. Munkres [1], H. L. Royden [1]):

1. If $\varphi$ is l.s.c., then $\operatorname{epi}\varphi$ is closed in $E\times\mathbb R$; and conversely.

2. If $\varphi$ is l.s.c., then for every $x\in E$ and for every $\varepsilon>0$ there is some neighborhood $V$ of $x$ such that

   $$
   \varphi(y)\ge\varphi(x)-\varepsilon \qquad \forall y\in V;
   $$

   and conversely.

   In particular, if $\varphi$ is l.s.c., then for every sequence $(x_n)$ in $E$ such that $x_n\to x$, we have

   $$
   \boxed{\liminf_{n\to\infty}\varphi(x_n)\ge\varphi(x)}
   $$

   and conversely if $E$ is a metric space.

3. If $\varphi_1$ and $\varphi_2$ are l.s.c., then $\varphi_1+\varphi_2$ is l.s.c.

---

⁵ We insist on the fact that $\mathbb R=(-\infty,\infty)$, so that $\lambda$ does not take the value $\infty$.



<a id="pdf-page-26"></a>
4. If $(\varphi_i)_{i\in I}$ is a family of l.s.c. functions then their *superior envelope* is also l.s.c., that is, the function $\varphi$ defined by

   $$
   \varphi(x)=\sup_{i\in I}\varphi_i(x)
   $$

   is l.s.c.

5. If $E$ is *compact* and $\varphi$ is l.s.c., then $\inf_E\varphi$ is achieved.

(If $E$ is a compact metric space one can argue with minimizing sequences. For a general topological compact space consider the sets $[\varphi\le\lambda]$ for appropriate values of $\lambda$.)

We now assume that $E$ is a *vector space*. Recall the following definition.

**Definition.** A function $\varphi:E\to(-\infty,+\infty]$ is said to be *convex* if

$$
\boxed{\varphi(tx+(1-t)y)\le t\varphi(x)+(1-t)\varphi(y)\quad\forall x,y\in E,\quad\forall t\in(0,1).}
$$

We shall use some elementary properties of convex functions:

1. If $\varphi$ is a convex function, then $\operatorname{epi}\varphi$ is a convex set in $E\times\mathbb R$; and conversely.

2. If $\varphi$ is a convex function, then for every $\lambda\in\mathbb R$ the set $[\varphi\le\lambda]$ is convex; but the converse is *not* true.

3. If $\varphi_1$ and $\varphi_2$ are convex, then $\varphi_1+\varphi_2$ is convex.

4. If $(\varphi_i)_{i\in I}$ is a family of convex functions, then the superior envelope, $\sup_i\varphi_i$, is convex.

We assume hereinafter that $E$ is an n.v.s.

**Definition.** Let $\varphi:E\to(-\infty,+\infty]$ be a function such that $\varphi\not\equiv+\infty$ (i.e., $D(\varphi)\ne\varnothing$). We define the *conjugate function* $\varphi^\star:E^\star\to(-\infty,+\infty]$ to be⁶

$$
\boxed{\varphi^\star(f)=\sup_{x\in E}\{\langle f,x\rangle-\varphi(x)\}\qquad(f\in E^\star).}
$$

Note that $\varphi^\star$ is convex and l.s.c. on $E^\star$. Indeed, for each fixed $x\in E$ the function $f\mapsto\langle f,x\rangle-\varphi(x)$ is convex and continuous (and thus l.s.c.) on $E^\star$. It follows that the superior envelope of these functions (as $x$ runs through $E$) is convex and l.s.c.

*Remark 7.* Clearly we have the inequality

$$
\langle f,x\rangle\le\varphi(x)+\varphi^\star(f)\qquad\forall x\in E,\quad\forall f\in E^\star, \tag{11}
$$

which is sometimes called *Young’s inequality*. Of course, this fact is obvious with our definition of $\varphi^\star$! The classical form of Young’s inequality (see the proof of Theorem 4.6 in Chapter 4) asserts that

---

⁶ $\varphi^\star$ is sometimes called the Legendre transform of $\varphi$.



<a id="pdf-page-27"></a>
![](assets/p0027-page_26_image_1.jpg)

**Fig. 2**

$$
ab\le\frac1p a^p+\frac1{p'}b^{p'} \qquad \forall a,b\ge0. \tag{12}
$$

with $1<p<\infty$ and $\frac1p+\frac1{p'}=1$. Inequality (12) becomes a special case of (11) with $E=E^\star=\mathbb R$ and $\varphi(t)=\frac1p|t|^p$, $\varphi^\star(s)=\frac1{p'}|s|^{p'}$ (see Exercise 1.18, question (h)).

**Proposition 1.10.** *Assume that $\varphi:E\to(-\infty,+\infty]$ is convex l.s.c. and $\varphi\not\equiv+\infty$. Then $\varphi^\star\not\equiv+\infty$, and in particular, $\varphi$ is bounded below by an affine continuous function.*

*Proof.* Let $x_0\in D(\varphi)$ and let $\lambda_0<\varphi(x_0)$. We apply Theorem 1.7 (Hahn–Banach, second geometric form) in the space $E\times\mathbb R$ with $A=\operatorname{epi}\varphi$ and $B=\{[x_0,\lambda_0]\}$. So, there exists a closed hyperplane $H=[\Phi=\alpha]$ in $E\times\mathbb R$ that strictly separates $A$ and $B$; see Figure 2. Note that the function $x\in E\mapsto\Phi([x,0])$ is a continuous linear functional on $E$, and thus $\Phi([x,0])=\langle f,x\rangle$ for some $f\in E^\star$. Letting $k=\Phi([0,1])$, we have

$$
\Phi([x,\lambda])=\langle f,x\rangle+k\lambda \qquad \forall[x,\lambda]\in E\times\mathbb R.
$$

Writing that $\Phi>\alpha$ on $A$ and $\Phi<\alpha$ on $B$, we obtain

$$
\langle f,x\rangle+k\lambda>\alpha,\qquad\forall[x,\lambda]\in\operatorname{epi}\varphi,
$$

and

$$
\langle f,x_0\rangle+k\lambda_0<\alpha.
$$

In particular, we have

$$
\langle f,x\rangle+k\varphi(x)>\alpha \qquad \forall x\in D(\varphi) \tag{13}
$$

and thus

$$
\langle f,x_0\rangle+k\varphi(x_0)>\alpha>\langle f,x_0\rangle+k\lambda_0.
$$

It follows that $k>0$. By (13) we have



<a id="pdf-page-28"></a>
$$
\left\langle-\frac1k f,x\right\rangle-\varphi(x)<-\frac\alpha k \qquad \forall x\in D(\varphi)
$$

and therefore $\varphi^\star(-\frac1k f)<+\infty$.

If we iterate the operation $\star$, we obtain a function $\varphi^{\star\star}$ defined on $E^{\star\star}$. Instead, we choose to restrict $\varphi^{\star\star}$ to $E$, that is, we define

$$
\boxed{\varphi^{\star\star}(x)=\sup_{f\in E^\star}\{\langle f,x\rangle-\varphi^\star(f)\}\qquad(x\in E).}
$$

**• Theorem 1.11 (Fenchel–Moreau).** *Assume that $\varphi:E\to(-\infty,+\infty]$ is convex, l.s.c., and $\varphi\not\equiv+\infty$. Then $\varphi^{\star\star}=\varphi$.*

*Proof.* We proceed in two steps:

**Step 1:** We assume in addition that $\varphi\ge0$ and we claim that $\varphi^{\star\star}=\varphi$.

First, it is obvious that $\varphi^{\star\star}\le\varphi$, since $\langle f,x\rangle-\varphi^\star(f)\le\varphi(x)$ $\forall x\in E$ and $\forall f\in E^\star$. In order to prove that $\varphi^{\star\star}=\varphi$ we argue by contradiction, and we assume that $\varphi^{\star\star}(x_0)<\varphi(x_0)$ for some $x_0\in E$. We could possibly have $\varphi(x_0)=+\infty$, but $\varphi^{\star\star}(x_0)$ is always finite. We apply Theorem 1.7 (Hahn–Banach, second geometric form) in the space $E\times\mathbb R$ with $A=\operatorname{epi}\varphi$ and $B=[x_0,\varphi^{\star\star}(x_0)]$. So, there exist, as in the proof of Proposition 1.10, $f\in E^\star$, $k\in\mathbb R$, and $\alpha\in\mathbb R$ such that

$$
\langle f,x\rangle+k\lambda>\alpha \qquad \forall[x,\lambda]\in\operatorname{epi}\varphi, \tag{14}
$$

$$
\langle f,x_0\rangle+k\varphi^{\star\star}(x_0)<\alpha. \tag{15}
$$

It follows that $k\ge0$ (fix some $x\in D(\varphi)$ and let $\lambda\to+\infty$ in (14)). [Here we cannot assert, as in the proof of Proposition 1.10, that $k>0$; we could possibly have $k=0$, which would correspond to a “vertical” hyperplane $H$ in $E\times\mathbb R$.]

Let $\varepsilon>0$; since $\varphi\ge0$, we have by (14),

$$
\langle f,x\rangle+(k+\varepsilon)\varphi(x)\ge\alpha \qquad \forall x\in D(\varphi).
$$

Therefore

$$
\varphi^\star\left(-\frac f{k+\varepsilon}\right)\le-\frac\alpha{k+\varepsilon}.
$$

It follows from the definition of $\varphi^{\star\star}(x_0)$ that

$$
\varphi^{\star\star}(x_0)\ge\left\langle-\frac f{k+\varepsilon},x_0\right\rangle-\varphi^\star\left(-\frac f{k+\varepsilon}\right)
\ge\left\langle-\frac f{k+\varepsilon},x_0\right\rangle+\frac\alpha{k+\varepsilon}.
$$

Thus we have

$$
\langle f,x_0\rangle+(k+\varepsilon)\varphi^{\star\star}(x_0)\ge\alpha \qquad \forall\varepsilon>0,
$$

which contradicts (15).



<a id="pdf-page-29"></a>
**Step 2:** The general case.

Fix some $f_0\in D(\varphi^\star)$ ($D(\varphi^\star)\ne\varnothing$ by Proposition 1.10) and define

$$
\overline\varphi(x)=\varphi(x)-\langle f_0,x\rangle+\varphi^\star(f_0),
$$

so that $\overline\varphi$ is convex l.s.c., $\overline\varphi\not\equiv+\infty$, and $\overline\varphi\ge0$. We know from Step 1 that $(\overline\varphi)^{\star\star}=\overline\varphi$. Let us now compute $(\overline\varphi)^\star$ and $(\overline\varphi)^{\star\star}$. We have

$$
(\overline\varphi)^\star(f)=\varphi^\star(f+f_0)-\varphi^\star(f_0)
$$

and

$$
(\overline\varphi)^{\star\star}(x)=\varphi^{\star\star}(x)-\langle f_0,x\rangle+\varphi^\star(f_0).
$$

Writing that $(\overline\varphi)^{\star\star}=\overline\varphi$, we obtain $\varphi^{\star\star}=\varphi$.

Let us examine some examples.

*Example 1.* Consider $\varphi(x)=\|x\|$. It is easy to check that

$$
\varphi^\star(f)=
\begin{cases}
0 & \text{if }\|f\|\le1,\\
+\infty & \text{if }\|f\|>1.
\end{cases}
$$

It follows that

$$
\varphi^{\star\star}(x)=\sup_{\substack{f\in E^\star\\\|f\|\le1}}\langle f,x\rangle.
$$

Writing the equality

$$
\varphi^{\star\star}=\varphi,
$$

we obtain again part of Corollary 1.4.

*Example 2.* Given a nonempty set $K\subset E$, we set

$$
\boxed{I_K(x)=
\begin{cases}
0 & \text{if }x\in K,\\
+\infty & \text{if }x\notin K.
\end{cases}}
$$

The function $I_K$ is called the *indicator function* of $K$ (and should not be confused with the characteristic function, $\chi_K$, of $K$, which is 1 on $K$ and 0 outside $K$). Note that $I_K$ is a convex function iff $K$ is a convex set, and $I_K$ is l.s.c. iff $K$ is closed. The conjugate function $(I_K)^\star$ is called the *supporting function* of $K$.

It is easy to see that if $K=M$ is a linear subspace then $(I_M)^\star=I_{M^\perp}$ and $(I_M)^{\star\star}=I_{(M^\perp)^\perp}$. Assuming that $M$ is a closed linear space and writing that $(I_M)^{\star\star}=I_M$, we obtain $(M^\perp)^\perp=M$. In some sense, Theorem 1.11 can be viewed as a counterpart of Proposition 1.9.



<a id="pdf-page-30"></a>
We conclude this chapter with another useful property of conjugate functions.

**★ Theorem 1.12 (Fenchel–Rockafellar).** *Let $\varphi,\psi:E\to(-\infty,+\infty]$ be two convex functions. Assume that there is some $x_0\in D(\varphi)\cap D(\psi)$ such that $\varphi$ is continuous at $x_0$. Then*

$$
\begin{aligned}
\inf_{x\in E}\{\varphi(x)+\psi(x)\}
&=\sup_{f\in E^\star}\{-\varphi^\star(-f)-\psi^\star(f)\}\\
&=\max_{f\in E^\star}\{-\varphi^\star(-f)-\psi^\star(f)\}
=-\min_{f\in E^\star}\{\varphi^\star(-f)+\psi^\star(f)\}.
\end{aligned}
$$

The proof of Theorem 1.12 relies on the following lemma.

**Lemma 1.4.** *Let $C\subset E$ be a convex set, then $\operatorname{Int}C$ is convex.⁷ If, in addition, $\operatorname{Int}C\ne\varnothing$, then*

$$
\overline C=\overline{\operatorname{Int}C}.
$$

For the proof of Lemma 1.4, see, e.g., Exercise 1.7.

*Proof of Theorem 1.12.* Set

$$
a=\inf_{x\in E}\{\varphi(x)+\psi(x)\},
$$

$$
b=\sup_{f\in E^\star}\{-\varphi^\star(-f)-\psi^\star(f)\}.
$$

It is clear that $b\le a$. If $a=-\infty$, the conclusion of Theorem 1.12 is obvious. Thus we may assume hereinafter that $a\in\mathbb R$. Let $C=\operatorname{epi}\varphi$, so that $\operatorname{Int}C\ne\varnothing$ (since $\varphi$ is continuous at $x_0$). We apply Theorem 1.6 (Hahn–Banach, first geometric form) with $A=\operatorname{Int}C$ and

$$
B=\{[x,\lambda]\in E\times\mathbb R;\ \lambda\le a-\psi(x)\}.
$$

Then $A$ and $B$ are nonempty convex sets. Moreover, $A\cap B=\varnothing$; indeed, if $[x,\lambda]\in A$, then $\lambda>\varphi(x)$, and on the other hand, $\varphi(x)\ge a-\psi(x)$ (by definition of $a$), so that $[x,\lambda]\notin B$.

Hence there exists a closed hyperplane $H$ that separates $A$ and $B$. It follows that $H$ also separates $\overline A$ and $B$. But we know from Lemma 1.4 that $\overline A=\overline C=C$. Therefore, there exist $f\in E^\star$, $k\in\mathbb R$, and $\alpha\in\mathbb R$ such that the hyperplane $H=[\Phi=\alpha]$ in $E\times\mathbb R$ separates $C$ and $B$, where

$$
\Phi([x,\lambda])=\langle f,x\rangle+k\lambda \qquad \forall[x,\lambda]\in E\times\mathbb R.
$$

Thus we have

$$
\langle f,x\rangle+k\lambda\ge\alpha \qquad \forall[x,\lambda]\in C, \tag{16}
$$

$$
\langle f,x\rangle+k\lambda\le\alpha \qquad \forall[x,\lambda]\in B. \tag{17}
$$

---

⁷ As usual, $\operatorname{Int}C$ denotes the interior of $C$.



<a id="pdf-page-31"></a>
Choosing $x=x_0$ and letting $\lambda\to+\infty$ in (16), we see that $k\ge0$. We claim that

$$
k>0. \tag{18}
$$

Assume by contradiction that $k=0$; it follows that $\|f\|\ne0$ (since $\Phi\not\equiv0$). By (16) and (17) we have

$$
\langle f,x\rangle\ge\alpha \qquad \forall x\in D(\varphi),
$$

$$
\langle f,x\rangle\le\alpha \qquad \forall x\in D(\psi).
$$

But $B(x_0,\varepsilon_0)\subset D(\varphi)$ for some $\varepsilon_0>0$ (small enough), and thus

$$
\langle f,x_0+\varepsilon_0z\rangle\ge\alpha \qquad \forall z\in B(0,1),
$$

which implies that $\langle f,x_0\rangle\ge\alpha+\varepsilon_0\|f\|$. On the other hand, we have $\langle f,x_0\rangle\le\alpha$, since $x_0\in D(\psi)$; therefore we obtain $\|f\|=0$, which is a contradiction and completes the proof of (18).

From (16) and (17) we obtain

$$
\varphi^\star\left(-\frac fk\right)\le-\frac\alpha k
$$

and

$$
\psi^\star\left(\frac fk\right)\le\frac\alpha k-a,
$$

so that

$$
-\varphi^\star\left(-\frac fk\right)-\psi^\star\left(\frac fk\right)\ge a.
$$

On the other hand, from the definition of $b$, we have

$$
-\varphi^\star\left(-\frac fk\right)-\psi^\star\left(\frac fk\right)\le b.
$$

We conclude that

$$
a=b=-\varphi^\star\left(-\frac fk\right)-\psi^\star\left(\frac fk\right).
$$

*Example 3.* Let $K$ be a nonempty convex set. We claim that for every $x_0\in E$ we have

$$
\operatorname{dist}(x_0,K)=\inf_{x\in K}\|x-x_0\|
=\max_{\substack{f\in E^\star\\\|f\|\le1}}\{\langle f,x_0\rangle-I_K^\star(f)\}. \tag{19}
$$

Indeed, we have

$$
\inf_{x\in K}\|x-x_0\|=\inf_{x\in E}\{\varphi(x)+\psi(x)\},
$$

with $\varphi(x)=\|x-x_0\|$ and $\psi(x)=I_K(x)$. Applying Theorem 1.12, we obtain (19). In the special case that $K=M$ is a linear subspace, we obtain the relation



<a id="pdf-page-32"></a>
$$
\operatorname{dist}(x_0,M)=\inf_{x\in M}\|x-x_0\|
=\max_{\substack{f\in M^\perp\\\|f\|\le1}}\langle f,x_0\rangle.
$$

*Remark 8.* Relation (19) may provide us with some useful information in the case that $\inf_{x\in K}\|x-x_0\|$ is not achieved (see, e.g., Exercise 1.17). The theory of minimal surfaces provides an interesting setting in which the *primal problem* (i.e., $\inf_{x\in E}\{\varphi(x)+\psi(x)\}$) need not have a solution, while the *dual problem* (i.e., $\max_{f\in E^\star}\{-\varphi^\star(-f)-\psi^\star(f)\}$) has a solution; see I. Ekeland–R. Temam [1].

*Example 4.* Let $\varphi:E\to\mathbb R$ be convex and continuous and let $M\subset E$ be a linear subspace. Then we have

$$
\inf_{x\in M}\varphi(x)=-\min_{f\in M^\perp}\varphi^\star(f).
$$

It suffices to apply Theorem 1.12 with $\psi=I_M$.

# Comments on Chapter 1

## 1. Generalizations and variants of the Hahn–Banach theorems.

The first geometric form of the Hahn–Banach theorem (Theorem 1.6) is still valid in general topological vector spaces. The second geometric form (Theorem 1.7) holds in *locally convex spaces*—such spaces play an important role, for example, in the *theory of distributions* (see, e.g., L. Schwartz [1] and F. Treves [1]). Interested readers may consult, e.g., N. Bourbaki [1], J. Kelley–I. Namioka [1], G. Choquet [2] (Volume 2), A. Taylor–D. Lay [1], and A. Knapp [2].

## 2. Applications of the Hahn–Banach theorems.

The Hahn–Banach theorems have a *wide* and *diversified* range of applications. Here are two examples:

(a) The Krein–Milman theorem.

The second geometric form of the Hahn–Banach theorem is a basic ingredient in the proof of the Krein–Milman theorem. Before stating this result we need some definitions. Let $E$ be an n.v.s. and let $A$ be a subset of $E$. The *convex hull* of $A$, denoted by $\operatorname{conv}A$, is the smallest convex set containing $A$. Clearly, $\operatorname{conv}A$ consists of all *finite convex combinations* of elements in $A$, i.e.,

$$
\operatorname{conv}A=
\left\{\sum_{i\in I}t_i a_i;\ I\text{ finite},\ a_i\in A\ \forall i,\ t_i\ge0\ \forall i,\text{ and }\sum_{i\in I}t_i=1\right\}.
$$

The *closed convex hull* of $A$, denoted by $\overline{\operatorname{conv}}A$, is the closure of $\operatorname{conv}A$. Given a convex set $K\subset E$ we say that a point $x\in K$ is *extremal* if $x$ cannot be written as a convex combination of two points $x_0,x_1\in K$, i.e., $x\ne(1-t)x_0+tx_1$ with $t\in(0,1)$, and $x_0\ne x_1$.



<a id="pdf-page-33"></a>
**• Theorem 1.13 (Krein–Milman).** *Let $K\subset E$ be a compact convex set. Then $K$ coincides with the closed convex hull of its extremal points.*

The Krein–Milman theorem has itself numerous applications and extensions (such as Choquet’s integral representation theorem, Bochner’s theorem, Bernstein’s theorem, etc.). On this vast subject, see, e.g., N. Bourbaki [1], G. Choquet [2] (Volume 2), R. Phelps [1], C. Dellacherie–P. A. Meyer [1] (Chapter 10), N. Dunford–J. T. Schwartz [1] (Volume 1), W. Rudin [1], R. Larsen [1], J. Kelley–I. Namioka [1], R. Edwards [1]. An interesting application to PDEs, due to Y. Pinchover, is presented in S. Agmon [2]. For a proof of the Krein–Milman theorem, see Problem 1.

(b) In the theory of partial differential equations.

Let us mention, for example, that the existence of a *fundamental solution* for a general differential operator $P(D)$ with constant coefficients (the Malgrange–Ehrenpreis theorem) relies on the analytic form of Hahn–Banach; see, e.g., L. Hörmander [1], [2], K. Yosida [1], W. Rudin [1], F. Treves [2], M. Reed–B. Simon [1] (Volume 2). In the same spirit, let us mention also the proof of the existence of the Green’s function for the Laplacian by the method of P. Lax; see P. Lax [1] (Section 9.5) and P. Garabedian [1]. The proof of the existence of a solution $u\in L^\infty(\Omega)$ for the equation $\operatorname{div}u=f$ in $\Omega\subset\mathbb R^N$, given any $f\in L^N(\Omega)$, relies on Hahn–Banach (see J. Bourgain–H. Brezis [1], [2]). Surprisingly, the $u$ obtained via Hahn–Banach depends *nonlinearly* on $f$. In fact, there exists no bounded linear operator from $L^N$ into $L^\infty$ giving $u$ in terms of $f$. This shows that the use of Zorn’s lemma (and the underlying axiom of choice) in the proof of Hahn–Banach can be delicate and may destroy the linear character of the problem. Sometimes there is no way to circumvent this obstruction.

## 3. Convex functions.

*Convex analysis and duality principles* are topics which have considerably expanded and have become increasingly popular in recent years; see, e.g., J. J. Moreau [1], R. T. Rockafellar [1], [2], I. Ekeland–R. Temam [1], I. Ekeland–T. Turnbull [1], F. Clarke [1], J. P. Aubin–I. Ekeland [1], J. B. Hiriart–Urruty–C. Lemaréchal [1]. Among the applications let us mention the following:

(a) *Game theory, economics, optimization, convex programming*; see J. P. Aubin [1], [2], [3], J. P. Aubin–I. Ekeland [1], S. Karlin [1], A. Balakrishnan [1], V. Barbu–I. Precupanu [1], J. Franklin [1], J. Stoer–C. Witzgall [1].

(b) *Mechanics*; see J. J. Moreau [2], P. Germain [1], [2], G. Duvaut–J. L. Lions [1], R. Temam–G. Strang [1] and the comments by P. Germain following this paper, H. D. Bui [1] and the numerous references therein. Note also the use of (nonconvex) duality by J. F. Toland [1], [2], [3] (for the study of rotating chains), by A. Damlamian [1] (for a problem arising in plasma physics), and by G. Auchmuty [1].

(c) The theory of *monotone operators and nonlinear semigroups*; see H. Brezis [1], F. Browder [1], V. Barbu [1], and R. Phelps [2].

(d) Variational problems involving *periodic solutions of Hamiltonian systems and nonlinear vibrating strings*; see the recent works of F. Clarke, I. Ekeland,



<a id="pdf-page-34"></a>
J. M. Lasry, H. Brezis, J. M. Coron, L. Nirenberg (we refer, e.g., to F. Clarke–I. Ekeland [1], H. Brezis–J. M. Coron–L. Nirenberg [1], H. Brezis [2], J. P. Aubin–I. Ekeland [1], I. Ekeland [1], and their bibliographies).

(e) The theory of *large deviations in probability*; see, e.g., R. Azencott et al. [1], D. W. Stroock [1].

(f) The theory of *partial differential equations and complex analysis*; see L. Hörmander [3].

## 4. Extensions of bounded linear operators.

Let $E$ and $F$ be two Banach spaces and let $G\subset E$ be a closed subspace. Let $S:G\to F$ be a bounded linear operator. One may ask whether it is possible to extend $S$ by a bounded linear operator $T:E\to F$. Note that Corollary 1.2 settles this question only when $F=\mathbb R$. In general, the answer is negative (even if $E$ and $F$ are reflexive spaces; see Exercise 1.27), except in some special cases; for example, the following:

(a) If $\dim F<\infty$. One may choose a basis in $F$ and apply Corollary 1.2 to each component of $S$.

(b) If $G$ admits a topological complement (see Section 2.4). This is true in particular if $\dim G<\infty$ or $\operatorname{codim}G<\infty$ or if $E$ is a Hilbert space.

One may also ask the question whether there is an extension $T$ *with the same norm*, i.e., $\|T\|_{\mathcal L(E,F)}=\|S\|_{\mathcal L(G,F)}$. The answer is yes only in some exceptional cases; see L. Nachbin [1], J. Kelley [1], and Exercise 5.15.

# Exercises for Chapter 1

## 1.1 *Properties of the duality map.*

Let $E$ be an n.v.s. The duality map $F$ is defined for every $x\in E$ by

$$
F(x)=\{f\in E^\star;\ \|f\|=\|x\|\text{ and }\langle f,x\rangle=\|x\|^2\}.
$$

1. Prove that

   $$
   F(x)=\{f\in E^\star;\ \|f\|\le\|x\|\text{ and }\langle f,x\rangle=\|x\|^2\}
   $$

   and deduce that $F(x)$ is nonempty, closed, and convex.

2. Prove that if $E^\star$ is strictly convex, then $F(x)$ contains a single point.

3. Prove that

   $$
   F(x)=\left\{f\in E^\star;\ \frac12\|y\|^2-\frac12\|x\|^2\ge\langle f,y-x\rangle\quad\forall y\in E\right\}.
   $$

4. Deduce that

   $$
   \langle F(x)-F(y),x-y\rangle\ge0 \qquad \forall x,y\in E,
   $$



<a id="pdf-page-35"></a>
and more precisely that

$$
\langle f-g,x-y\rangle\ge0
\qquad \forall x,y\in E,\quad\forall f\in F(x),\quad\forall g\in F(y).
$$

Show that, in fact,

$$
\langle f-g,x-y\rangle\ge(\|x\|-\|y\|)^2
\qquad \forall x,y\in E,\quad\forall f\in F(x),\quad\forall g\in F(y).
$$

5. Assume again that $E^\star$ is strictly convex and let $x,y\in E$ be such that

   $$
   \langle F(x)-F(y),x-y\rangle=0.
   $$

   Show that $Fx=Fy$.

## 1.2

Let $E$ be a vector space of dimension $n$ and let $(e_i)_{1\le i\le n}$ be a basis of $E$. Given $x\in E$, write $x=\sum_{i=1}^n x_i e_i$ with $x_i\in\mathbb R$; given $f\in E^\star$, set $f_i=\langle f,e_i\rangle$.

1. Consider on $E$ the norm

   $$
   \|x\|_1=\sum_{i=1}^n|x_i|.
   $$

   (a) Compute explicitly, in terms of the $f_i$’s, the dual norm $\|f\|_{E^\star}$ of $f\in E^\star$.

   (b) Determine explicitly the set $F(x)$ (duality map) for every $x\in E$.

2. Same questions but where $E$ is provided with the norm

   $$
   \|x\|_\infty=\max_{1\le i\le n}|x_i|.
   $$

3. Same questions but where $E$ is provided with the norm

   $$
   \|x\|_2=\left(\sum_{i=1}^n|x_i|^2\right)^{1/2},
   $$

   and more generally with the norm

   $$
   \|x\|_p=\left(\sum_{i=1}^n|x_i|^p\right)^{1/p},
   \qquad\text{where }p\in(1,\infty).
   $$

## 1.3

Let $E=\{u\in C([0,1];\mathbb R);\ u(0)=0\}$ with its usual norm

$$
\|u\|=\max_{t\in[0,1]}|u(t)|.
$$

Consider the linear functional



<a id="pdf-page-36"></a>
$$
f:u\in E\mapsto f(u)=\int_0^1u(t)\,dt.
$$

1. Show that $f\in E^\star$ and compute $\|f\|_{E^\star}$.

2. Can one find some $u\in E$ such that $\|u\|=1$ and $f(u)=\|f\|_{E^\star}$?

## 1.4

Consider the space $E=c_0$ (sequences tending to zero) with its usual norm (see Section 11.3). For every element $u=(u_1,u_2,u_3,\ldots)$ in $E$ define

$$
f(u)=\sum_{n=1}^\infty\frac1{2^n}u_n.
$$

1. Check that $f$ is a continuous linear functional on $E$ and compute $\|f\|_{E^\star}$.

2. Can one find some $u\in E$ such that $\|u\|=1$ and $f(u)=\|f\|_{E^\star}$?

## 1.5

Let $E$ be an infinite-dimensional n.v.s.

1. Prove (using Zorn’s lemma) that there exists an algebraic basis $(e_i)_{i\in I}$ in $E$ such that $\|e_i\|=1$ $\forall i\in I$.

   Recall that an algebraic basis (or Hamel basis) is a subset $(e_i)_{i\in I}$ in $E$ such that every $x\in E$ may be written uniquely as

   $$
   x=\sum_{i\in J}x_i e_i\quad\text{with }J\subset I,\ J\text{ finite}.
   $$

2. Construct a linear functional $f:E\to\mathbb R$ that is not continuous.

3. Assuming in addition that $E$ is a Banach space, prove that $I$ is not countable.

   **[Hint:** Use Baire category theorem (Theorem 2.1).**]**

## 1.6

Let $E$ be an n.v.s. and let $H\subset E$ be a hyperplane. Let $V\subset E$ be an affine subspace containing $H$.

1. Prove that either $V=H$ or $V=E$.

2. Deduce that $H$ is either closed or dense in $E$.

## 1.7

Let $E$ be an n.v.s. and let $C\subset E$ be convex.

1. Prove that $\overline C$ and $\operatorname{Int}C$ are convex.

2. Given $x\in C$ and $y\in\operatorname{Int}C$, show that $tx+(1-t)y\in\operatorname{Int}C$ $\forall t\in(0,1)$.

3. Deduce that $\overline C=\overline{\operatorname{Int}C}$ whenever $\operatorname{Int}C\ne\varnothing$.

## 1.8

Let $E$ be an n.v.s. with norm $\|\ \|$. Let $C\subset E$ be an open convex set such that $0\in C$. Let $p$ denote the gauge of $C$ (see Lemma 1.2).

1. Assuming $C$ is symmetric (i.e., $-C=C$) and $C$ is bounded, prove that $p$ is a norm which is equivalent to $\|\ \|$.



<a id="pdf-page-37"></a>
2. Let $E=C([0,1];\mathbb R)$ with its usual norm

   $$
   \|u\|=\max_{t\in[0,1]}|u(t)|.
   $$

   Let

   $$
   C=\left\{u\in E;\ \int_0^1|u(t)|^2\,dt<1\right\}.
   $$

   Check that $C$ is convex and symmetric and that $0\in C$. Is $C$ bounded in $E$? Compute the gauge $p$ of $C$ and show that $p$ is a norm on $E$. Is $p$ equivalent to $\|\ \|$?

## 1.9 *Hahn–Banach in finite-dimensional spaces.*

Let $E$ be a finite-dimensional normed space. Let $C\subset E$ be a nonempty convex set such that $0\notin C$. We claim that there always exists some hyperplane that separates $C$ and $\{0\}$.

[Note that every hyperplane is closed (why?). The main point in this exercise is that no additional assumption on $C$ is required.]

1. Let $(x_n)_{n\ge1}$ be a countable subset of $C$ that is dense in $C$ (why does it exist?). For every $n$ let

   $$
   C_n=\operatorname{conv}\{x_1,x_2,\ldots,x_n\}
   =\left\{x=\sum_{i=1}^n t_i x_i;\ t_i\ge0\ \forall i\text{ and }\sum_{i=1}^n t_i=1\right\}.
   $$

   Check that $C_n$ is compact and that $\bigcup_{n=1}^\infty C_n$ is dense in $C$.

2. Prove that there is some $f_n\in E^\star$ such that

   $$
   \|f_n\|=1\text{ and }\langle f_n,x\rangle\ge0 \qquad \forall x\in C_n.
   $$

3. Deduce that there is some $f\in E^\star$ such that

   $$
   \|f\|=1\text{ and }\langle f,x\rangle\ge0 \qquad \forall x\in C.
   $$

   Conclude.

4. Let $A,B\subset E$ be nonempty disjoint convex sets. Prove that there exists some hyperplane $H$ that separates $A$ and $B$.

## 1.10

Let $E$ be an n.v.s. and let $I$ be any set of indices. Fix a subset $(x_i)_{i\in I}$ in $E$ and a subset $(\alpha_i)_{i\in I}$ in $\mathbb R$. Show that the following properties are equivalent:

(A) There exists some $f\in E^\star$ such that $\langle f,x_i\rangle=\alpha_i$ $\forall i\in I$.

(B) There exists a constant $M\ge0$ such that for each finite subset $J\subset I$ and for every choice of real numbers $(\beta_i)_{i\in J}$, we have

$$
\left|\sum_{i\in J}\beta_i\alpha_i\right|\le M\left\|\sum_{i\in J}\beta_i x_i\right\|.
$$



<a id="pdf-page-38"></a>
Note that in the proof of (B) $\Rightarrow$ (A) one may find some $f\in E^\star$ with $\|f\|_{E^\star}\le M$.

**[Hint:** Try first to define $f$ on the linear space spanned by the $(x_i)_{i\in I}$.**]**

## 1.11

Let $E$ be an n.v.s. and let $M>0$. Fix $n$ elements $(f_i)_{1\le i\le n}$ in $E^\star$ and $n$ real numbers $(\alpha_i)_{1\le i\le n}$. Prove that the following properties are equivalent:

(A)

$$
\begin{cases}
\forall\varepsilon>0\quad\exists x_\varepsilon\in E\text{ such that}\\
\|x_\varepsilon\|\le M+\varepsilon\text{ and }\langle f_i,x_\varepsilon\rangle=\alpha_i
\quad\forall i=1,2,\ldots,n.
\end{cases}
$$

(B)

$$
\left|\sum_{i=1}^n\beta_i\alpha_i\right|
\le M\left\|\sum_{i=1}^n\beta_i f_i\right\|
\qquad\forall\beta_1,\beta_2,\ldots,\beta_n\in\mathbb R.
$$

**[Hint:** For the proof of (B) $\Rightarrow$ (A) consider first the case in which the $f_i$’s are linearly independent and imitate the proof of Lemma 3.3.**]**

Compare Exercises 1.10, 1.11 and Lemma 3.3.

## 1.12

Let $E$ be a vector space. Fix $n$ linear functionals $(f_i)_{1\le i\le n}$ on $E$ and $n$ real numbers $(\alpha_i)_{1\le i\le n}$. Prove that the following properties are equivalent:

(A) There exists some $x\in E$ such that $f_i(x)=\alpha_i$ $\forall i=1,2,\ldots,n$.

(B) For any choice of real numbers $\beta_1,\beta_2,\ldots,\beta_n$ such that $\sum_{i=1}^n\beta_i f_i=0$, one also has $\sum_{i=1}^n\beta_i\alpha_i=0$.

## 1.13

Let $E=\mathbb R^n$ and let

$$
P=\{x\in\mathbb R^n;\ x_i\ge0\quad\forall i=1,2,\ldots,n\}.
$$

Let $M$ be a linear subspace of $E$ such that $M\cap P=\{0\}$. Prove that there is some hyperplane $H$ in $E$ such that

$$
M\subset H\text{ and }H\cap P=\{0\}.
$$

**[Hint:** Show first that $M^\perp\cap\operatorname{Int}P\ne\varnothing$.**]**

## 1.14

Let $E=\ell^1$ (see Section 11.3) and consider the two sets

$$
X=\{x=(x_n)_{n\ge1}\in E;\ x_{2n}=0\ \forall n\ge1\}
$$

and

$$
Y=\left\{y=(y_n)_{n\ge1}\in E;\ y_{2n}=\frac1{2^n}y_{2n-1}\ \forall n\ge1\right\}.
$$

1. Check that $X$ and $Y$ are closed linear spaces and that $\overline{X+Y}=E$.

2. Let $c\in E$ be defined by



<a id="pdf-page-39"></a>
$$
\begin{cases}
c_{2n-1}=0 & \forall n\ge1,\\
c_{2n}=\dfrac1{2^n} & \forall n\ge1.
\end{cases}
$$

Check that $c\notin X+Y$.

3. Set $Z=X-c$ and check that $Y\cap Z=\varnothing$. Does there exist a closed hyperplane in $E$ that separates $Y$ and $Z$?

   Compare with Theorem 1.7 and Exercise 1.9.

4. Same questions in $E=\ell^p$, $1<p<\infty$, and in $E=c_0$.

## 1.15

Let $E$ be an n.v.s. and let $C\subset E$ be a convex set such that $0\in C$. Set

$$
C^\star=\{f\in E^\star;\ \langle f,x\rangle\le1\quad\forall x\in C\}, \tag{A}
$$

$$
C^{\star\star}=\{x\in E;\ \langle f,x\rangle\le1\quad\forall f\in C^\star\}. \tag{B}
$$

1. Prove that $C^{\star\star}=\overline C$.

2. What is $C^\star$ if $C$ is a linear space?

## 1.16

Let $E=\ell^1$, so that $E^\star=\ell^\infty$ (see Section 11.3). Consider $N=c_0$ as a closed subspace of $E^\star$.

Determine

$$
N^\perp=\{x\in E;\ \langle f,x\rangle=0\quad\forall f\in N\}
$$

and

$$
N^{\perp\perp}=\{f\in E^\star;\ \langle f,x\rangle=0\quad\forall x\in N^\perp\}.
$$

Check that $N^{\perp\perp}\ne N$.

## 1.17

Let $E$ be an n.v.s. and let $f\in E^\star$ with $f\ne0$. Let $M$ be the hyperplane $[f=0]$.

1. Determine $M^\perp$.

2. Prove that for every $x\in E$,

   $$
   \operatorname{dist}(x,M)=\inf_{y\in M}\|x-y\|=\frac{|\langle f,x\rangle|}{\|f\|}.
   $$

   [Find a direct method or use Example 3 in Section 1.4.]

3. Assume now that $E=\{u\in C([0,1];\mathbb R);\ u(0)=0\}$ and that

   $$
   \langle f,u\rangle=\int_0^1u(t)\,dt,\qquad u\in E.
   $$

   Prove that $\operatorname{dist}(u,M)=\left|\int_0^1u(t)\,dt\right|$ $\forall u\in E$.

   Show that $\inf_{v\in M}\|u-v\|$ is never achieved for any $u\in E\setminus M$.

## 1.18

Check that the functions $\varphi:\mathbb R\to(-\infty,+\infty]$ defined below are convex l.s.c. and determine the conjugate functions $\varphi^\star$. Draw their graphs and mark their epigraphs.



<a id="pdf-page-40"></a>
(a)

$$
\varphi(x)=ax+b,\qquad\text{where }a,b\in\mathbb R.
$$

(b)

$$
\varphi(x)=e^x.
$$

(c)

$$
\varphi(x)=
\begin{cases}
0 & \text{if }|x|\le1,\\
+\infty & \text{if }|x|>1.
\end{cases}
$$

(d)

$$
\varphi(x)=
\begin{cases}
0 & \text{if }x=0,\\
+\infty & \text{if }x\ne0.
\end{cases}
$$

(e)

$$
\varphi(x)=
\begin{cases}
-\log x & \text{if }x>0,\\
+\infty & \text{if }x\le0.
\end{cases}
$$

(f)

$$
\varphi(x)=
\begin{cases}
-(1-x^2)^{1/2} & \text{if }|x|\le1,\\
+\infty & \text{if }|x|>1.
\end{cases}
$$

(g)

$$
\varphi(x)=
\begin{cases}
\dfrac12|x|^2 & \text{if }|x|\le1,\\
|x|-\dfrac12 & \text{if }|x|>1.
\end{cases}
$$

(h)

$$
\varphi(x)=\frac1p|x|^p,\qquad\text{where }1<p<\infty.
$$

(i)

$$
\varphi(x)=x^+=\max\{x,0\}.
$$

(j)

$$
\varphi(x)=
\begin{cases}
\dfrac1p x^p & \text{if }x\ge0,\text{ where }1<p<+\infty,\\
+\infty & \text{if }x<0.
\end{cases}
$$

(k)

$$
\varphi(x)=
\begin{cases}
-\dfrac1p x^p & \text{if }x\ge0,\text{ where }0<p<1,\\
+\infty & \text{if }x<0.
\end{cases}
$$

(l)

$$
\varphi(x)=\frac1p[(|x|-1)^+]^p,\qquad\text{where }1<p<\infty.
$$

## 1.19

Let $E$ be an n.v.s.

1. Let $\varphi,\psi:E\to(-\infty,+\infty]$ be two functions such that $\varphi\le\psi$. Prove that $\psi^\star\le\varphi^\star$.

2. Let $F:\mathbb R\to(-\infty,+\infty]$ be a convex l.s.c. function such that $F(0)=0$ and $F(t)\ge0$ $\forall t\in\mathbb R$. Set $\varphi(x)=F(\|x\|)$.

   Prove that $\varphi$ is convex l.s.c. and that $\varphi^\star(f)=F^\star(\|f\|)$ $\forall f\in E^\star$.

## 1.20

Let $E=\ell^p$ with $1\le p<\infty$ (see Section 11.3). Check that the functions $\varphi:E\to(-\infty,+\infty]$ defined below are convex l.s.c. and determine $\varphi^\star$. For $x=(x_1,x_2,\ldots,x_n,\ldots)$ set

(a)

$$
\varphi(x)=
\begin{cases}
\displaystyle\sum_{k=1}^{+\infty}k|x_k|^2 & \text{if }\displaystyle\sum_{k=1}^{\infty}k|x_k|^2<+\infty,\\
+\infty & \text{otherwise}.
\end{cases}
$$

(b)

$$
\varphi(x)=\sum_{k=2}^{+\infty}|x_k|^k.
$$

(Check that $\varphi(x)<\infty$ for every $x\in E$.)



<a id="pdf-page-41"></a>
(c)

$$
\varphi(x)=
\begin{cases}
\displaystyle\sum_{k=1}^{+\infty}|x_k| & \text{if }\displaystyle\sum_{k=1}^{\infty}|x_k|<+\infty,\\
+\infty & \text{otherwise}.
\end{cases}
$$

## 1.21

Let $E=E^\star=\mathbb R^2$ and let

$$
C=\{[x_1,x_2];\ x_1\ge0,\ x_2\ge0\}.
$$

On $E$ define the function

$$
\varphi(x)=
\begin{cases}
-\sqrt{x_1x_2} & \text{if }x\in C,\\
+\infty & \text{if }x\notin C.
\end{cases}
$$

1. Prove that $\varphi$ is convex l.s.c. on $E$.

2. Determine $\varphi^\star$.

3. Consider the set $D=\{[x_1,x_2];\ x_1=0\}$ and the function $\psi=I_D$. Compute the value of the expressions

   $$
   \inf_{x\in E}\{\varphi(x)+\psi(x)\}
   \quad\text{and}\quad
   \sup_{f\in E^\star}\{-\varphi^\star(-f)-\psi^\star(f)\}.
   $$

4. Compare with the conclusion of Theorem 1.12 and explain the difference.

## 1.22

Let $E$ be an n.v.s. and let $A\subset E$ be a closed nonempty set. Let

$$
\varphi(x)=\operatorname{dist}(x,A)=\inf_{a\in A}\|x-a\|.
$$

1. Check that $|\varphi(x)-\varphi(y)|\le\|x-y\|$ $\forall x,y\in E$.

2. Assuming that $A$ is convex, prove that $\varphi$ is convex.

3. Conversely, assuming that $\varphi$ is convex, prove that $A$ is convex.

4. Prove that $\varphi^\star=(I_A)^\star+I_{B_{E^\star}}$ for every $A$ not necessarily convex.

## 1.23 *Inf-convolution.*

Let $E$ be an n.v.s. Given two functions $\varphi,\psi:E\to(-\infty,+\infty]$, one defines the *inf-convolution* of $\varphi$ and $\psi$ as follows: for every $x\in E$, let

$$
(\varphi\mathbin\nabla\psi)(x)=\inf_{y\in E}\{\varphi(x-y)+\psi(y)\}.
$$

Note the following:

(i) $(\varphi\mathbin\nabla\psi)(x)$ may take the values $\pm\infty$,

(ii) $(\varphi\mathbin\nabla\psi)(x)<+\infty$ iff $x\in D(\varphi)+D(\psi)$.

1. Assuming that $D(\varphi^\star)\cap D(\psi^\star)\ne\varnothing$, prove that $(\varphi\mathbin\nabla\psi)$ does not take the value $-\infty$ and that



<a id="pdf-page-42"></a>
$$
(\varphi\mathbin\nabla\psi)^\star=\varphi^\star+\psi^\star.
$$

2. Assuming that $D(\varphi)\cap D(\psi)\ne\varnothing$, prove that

   $$
   (\varphi+\psi)^\star\le(\varphi^\star\mathbin\nabla\psi^\star)\quad\text{on }E^\star.
   $$

3. Assume that $\varphi$ and $\psi$ are convex and there exists $x_0\in D(\varphi)\cap D(\psi)$ such that $\varphi$ is continuous at $x_0$. Prove that

   $$
   (\varphi+\psi)^\star=(\varphi^\star\mathbin\nabla\psi^\star)\quad\text{on }E^\star.
   $$

4. Assume that $\varphi$ and $\psi$ are convex and l.s.c., and that $D(\varphi)\cap D(\psi)\ne\varnothing$. Prove that

   $$
   (\varphi^\star\mathbin\nabla\psi^\star)^\star=(\varphi+\psi)\quad\text{on }E.
   $$

Given a function $\varphi:E\to(-\infty,+\infty]$, set

$$
\operatorname{epist}\varphi=\{[x,\lambda]\in E\times\mathbb R;\ \varphi(x)<\lambda\}.
$$

5. Check that $\varphi$ is convex iff $\operatorname{epist}\varphi$ is a convex subset of $E\times\mathbb R$.

6. Let $\varphi,\psi:E\to(-\infty,+\infty]$ be functions such that $D(\varphi^\star)\cap D(\psi^\star)\ne\varnothing$. Prove that

   $$
   \operatorname{epist}(\varphi\mathbin\nabla\psi)=(\operatorname{epist}\varphi)+(\operatorname{epist}\psi).
   $$

7. Deduce that if $\varphi,\psi:E\to(-\infty,+\infty]$ are convex functions such that $D(\varphi^\star)\cap D(\psi^\star)\ne\varnothing$, then $(\varphi\mathbin\nabla\psi)$ is a convex function.

## 1.24 *Regularization by inf-convolution.*

Let $E$ be an n.v.s. and let $\varphi:E\to(-\infty,+\infty]$ be a convex l.s.c. function such that $\varphi\not\equiv+\infty$. Our aim is to construct a sequence of functions $(\varphi_n)$ such that we have the following:

(i) For every $n$, $\varphi_n:E\to(-\infty,+\infty)$ is convex and continuous.

(ii) For every $x$, the sequence $(\varphi_n(x))_n$ is nondecreasing and converges to $\varphi(x)$.

For this purpose, let

$$
\varphi_n(x)=\inf_{y\in E}\{n\|x-y\|+\varphi(y)\}.
$$

1. Prove that there is some $N$, large enough, such that for $n\ge N$, $\varphi_n(x)$ is finite for all $x\in E$. From now on, one chooses $n\ge N$.

2. Prove that $\varphi_n$ is convex (see Exercise 1.23) and that

   $$
   |\varphi_n(x_1)-\varphi_n(x_2)|\le n\|x_1-x_2\| \qquad \forall x_1,x_2\in E.
   $$

3. Determine $(\varphi_n)^\star$.

4. Check that $\varphi_n(x)\le\varphi(x)$ $\forall x\in E$, $\forall n$. Prove that for every $x\in E$, the sequence $(\varphi_n(x))_n$ is nondecreasing.



<a id="pdf-page-43"></a>
5. Given $x\in D(\varphi)$, choose $y_n\in E$ such that

   $$
   \varphi_n(x)\le n\|x-y_n\|+\varphi(y_n)\le\varphi_n(x)+\frac1n.
   $$

   Prove that $\lim_{n\to\infty}y_n=x$ and deduce that $\lim_{n\to\infty}\varphi_n(x)=\varphi(x)$.

6. For $x\notin D(\varphi)$, prove that $\lim_{n\to\infty}\varphi_n(x)=+\infty$.

   **[Hint:** Argue by contradiction.**]**

## 1.25 *A semiscalar product.*

Let $E$ be an n.v.s.

1. Let $\varphi:E\to(-\infty,+\infty)$ be convex. Given $x,y\in E$, consider the function

   $$
   h(t)=\frac{\varphi(x+ty)-\varphi(x)}t,\qquad t>0.
   $$

   Check that $h$ is nondecreasing on $(0,+\infty)$ and deduce that

   $$
   \lim_{t\downarrow0}h(t)=\inf_{t>0}h(t)\text{ exists in }[-\infty,+\infty).
   $$

   Define the semiscalar product $[x,y]$ by

   $$
   [x,y]=\inf_{t>0}\frac1{2t}[\|x+ty\|^2-\|x\|^2].
   $$

2. Prove that $|[x,y]|\le\|x\|\|y\|$ $\forall x,y\in E$.

3. Prove that

   $$
   [x,\lambda x+\mu y]=\lambda\|x\|^2+\mu[x,y]
   \qquad\forall x,y\in E,\quad\forall\lambda\in\mathbb R,\quad\forall\mu\ge0
   $$

   and

   $$
   [\lambda x,\mu y]=\lambda\mu[x,y]
   \qquad\forall x,y\in E,\quad\forall\lambda\ge0,\quad\forall\mu\ge0.
   $$

4. Prove that for every $x\in E$, the function $y\mapsto[x,y]$ is convex. Prove that the function $G(x,y)=-[x,y]$ is l.s.c. on $E\times E$.

5. Prove that

   $$
   [x,y]=\max_{f\in F(x)}\langle f,y\rangle \qquad \forall x,y\in E,
   $$

   where $F$ denotes the duality map (see Remark 2 following Corollary 1.3 and Exercise 1.1).

   **[Hint:** Set $\alpha=[x,y]$ and apply Theorem 1.12 to the functions $\varphi$ and $\psi$ defined as follows:

   $$
   \varphi(z)=\frac12\|x+z\|^2-\frac12\|x\|^2,\qquad z\in E,
   $$

   and

   $$
   \psi(z)=
   \begin{cases}
   -t\alpha & \text{when }z=ty\text{ and }t\ge0,\\
   +\infty & \text{otherwise}.
   \end{cases}
   $$

   **]**



<a id="pdf-page-44"></a>
6. Determine explicitly $[x,y]$, where $E=\mathbb R^n$ with the norm $\|x\|_p$, $1\le p\le\infty$ (see Section 11.3).

   **[Hint:** Use the results of Exercise 1.2.**]**

## 1.26 *Strictly convex norms and functions.*

Let $E$ be an n.v.s. One says that the norm $\|\ \|$ is *strictly convex* (or that the space $E$ is strictly convex) if

$$
\|tx+(1-t)y\|<1,
\quad\forall x,y\in E\text{ with }x\ne y,\ \|x\|=\|y\|=1,
\quad\forall t\in(0,1).
$$

One says that a function $\varphi:E\to(-\infty,+\infty]$ is strictly convex if

$$
\varphi(tx+(1-t)y)<t\varphi(x)+(1-t)\varphi(y)
\quad\forall x,y\in E\text{ with }x\ne y,
\quad\forall t\in(0,1).
$$

1. Prove that the norm $\|\ \|$ is strictly convex iff the function $\varphi(x)=\|x\|^2$ is strictly convex.

2. Same question with $\varphi(x)=\|x\|^p$ and $1<p<\infty$.

## 1.27

Let $E$ and $F$ be two Banach spaces and let $G\subset E$ be a closed subspace. Let $T:G\to F$ be a continuous linear map. The aim is to show that sometimes, $T$ cannot be extended by a continuous linear map $\widetilde T:E\to F$. For this purpose, let $E$ be a Banach space and let $G\subset E$ be a closed subspace that admits no complement (see Remark 8 in Chapter 2). Let $F=G$ and $T=I$ (the identity map). Prove that $T$ cannot be extended.

**[Hint:** Argue by contradiction.**]**

Compare with the conclusion of Corollary 1.2.



<a id="pdf-page-45"></a>

