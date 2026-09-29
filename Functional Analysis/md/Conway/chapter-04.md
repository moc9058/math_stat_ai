# IV. Locally Convex Spaces


<a id="pdf-page-114"></a>
# CHAPTER IV

# Locally Convex Spaces

A topological vector space is a generalization of the concept of a Banach space. The locally convex spaces are encountered repeatedly when discussing weak topologies on a Banach space, sets of operators on Hilbert space, or the theory of distributions. This book will only skim the surface of this theory, but it will treat locally convex spaces in sufficient detail as to enable the reader to understand the use of these spaces in the three areas of analysis just mentioned. For more details on this theory, see Bourbaki [1967], Robertson and Robertson [1966], or Schaefer [1971].

## §1. Elementary Properties and Examples

A topological vector space is a vector space that is also a topological space such that the linear structure and the topological structure are vitally connected.

**1.1. Definition.** A *topological vector space* (TVS) is a vector space $\mathscr{X}$ together with a topology such that with respect to this topology

(a) the map of $\mathscr{X}\times\mathscr{X}\to\mathscr{X}$ defined by $(x,y)\mapsto x+y$ is continuous;  
(b) the map of $\mathbb{F}\times\mathscr{X}\to\mathscr{X}$ defined by $(\alpha,x)\mapsto\alpha x$ is continuous.

It is easy to see that a normed space is a TVS (Proposition III.1.3).

Suppose $\mathscr{X}$ is a vector space and $\mathscr{P}$ is a family of seminorms on $\mathscr{X}$. Let $\mathscr{T}$ be the topology on $\mathscr{X}$ that has as a subbase the sets $\{x:p(x-x_0)<\varepsilon\}$, where $p\in\mathscr{P}$, $x_0\in\mathscr{X}$, and $\varepsilon>0$. Thus a subset $U$ of $\mathscr{X}$ is open if and only if for every $x_0$ in $U$ there are $p_1,\ldots,p_n$ in $\mathscr{P}$ and $\varepsilon_1,\ldots,\varepsilon_n>0$ such that



<a id="pdf-page-115"></a>
$$
\bigcap_{j=1}^{n}\{x\in\mathcal{X}:p_j(x-x_0)<\varepsilon_j\}\subseteq U.
$$
It is not difficult to show that $\mathcal{X}$ with this topology is a TVS (Exercise 2).

**1.2. Definition.** A *locally convex space* (LCS) is a TVS whose topology is defined by a family of seminorms $\mathcal{P}$ such that $\bigcap_{p\in\mathcal{P}}\{x:p(x)=0\}=(0)$.

The attitude that has been adopted in this book is that all topological spaces are Hausdorff. The condition in Definition 1.2 that $\bigcap_{p\in\mathcal{P}}\{x:p(x)=0\}=(0)$ is imposed precisely so that the topology defined by $\mathcal{P}$ be Hausdorff. In fact, suppose that $x\ne y$. Then there is a $p$ in $\mathcal{P}$ such that $p(x-y)\ne0$; let $p(x-y)>\varepsilon>0$. If $U=\{z:p(x-z)<\frac12\varepsilon\}$ and $V=\{z:p(y-z)<\frac12\varepsilon\}$, then $U\cap V=\square$ and $U$ and $V$ are neighborhoods of $x$ and $y$, respectively.

If $\mathcal{X}$ is a TVS and $x_0\in\mathcal{X}$, then $x\mapsto x+x_0$ is a homeomorphism of $\mathcal{X}$; also, if $\alpha\in\mathbb{F}$ and $\alpha\ne0$, $x\mapsto\alpha x$ is a homeomorphism of $\mathcal{X}$ (Exercise 4). Thus the topology of $\mathcal{X}$ looks the same at any point. This might make the next statement less surprising.

**1.3. Proposition.** *Let $\mathcal{X}$ be a TVS and let $p$ be a seminorm on $\mathcal{X}$. The following statements are equivalent.*

(a) $p$ is continuous.

(b) $\{x\in\mathcal{X}:p(x)<1\}$ is open.

(c) $0\in\operatorname{int}\{x\in\mathcal{X}:p(x)<1\}$.

(d) $0\in\operatorname{int}\{x\in\mathcal{X}:p(x)\leq1\}$.

(e) $p$ is continuous at $0$.

(f) There is a continuous seminorm $q$ on $\mathcal{X}$ such that $p\leq q$.

**Proof.** It is clear that (a)$\Rightarrow$(b)$\Rightarrow$(c)$\Rightarrow$(d).

(d) implies (e): Clearly (d) implies that for every $\varepsilon>0$, $0\in\operatorname{int}\{x\in\mathcal{X}:p(x)\leq\varepsilon\}$; so if $\{x_i\}$ is a net in $\mathcal{X}$ that converges to $0$ and $\varepsilon>0$, there is an $i_0$ such that $x_i\in\{x:p(x)\leq\varepsilon\}$ for $i\geq i_0$; that is, $p(x_i)\leq\varepsilon$ for $i\geq i_0$. So $p$ is continuous at $0$.

(e) implies (a): If $x_i\to x$, then $|p(x)-p(x_i)|\leq p(x-x_i)$. Since $x-x_i\to0$, (e) implies that $p(x-x_i)\to0$. Hence $p(x_i)\to p(x)$.

Clearly (a) implies (f). So it remains to show that (f) implies (e). If $x_i\to0$ in $\mathcal{X}$, then $q(x_i)\to0$. But $0\leq p(x_i)\leq q(x_i)$, so $p(x_i)\to0$. $\blacksquare$

**1.4. Proposition.** *If $\mathcal{X}$ is a TVS and $p_1,\ldots,p_n$ are continuous seminorms, then $p_1+\cdots+p_n$ and $\max_i(p_i(x))$ are continuous seminorms. If $\{p_i\}$ is a family of continuous seminorms such that there is a continuous seminorm $q$ with $p_i\leq q$ for all $i$, then $x\mapsto\sup_i\{p_i(x)\}$ defines a continuous seminorm.*

**Proof.** Exercise.

If $\mathcal{P}$ is a family of seminorms of $\mathcal{X}$ that makes $\mathcal{X}$ into a LCS, it is often convenient to enlarge $\mathcal{P}$ by assuming that $\mathcal{P}$ is closed under the formation of finite sums and supremums of bounded families [as in (1.4)]. Sometimes



<a id="pdf-page-116"></a>
it is convenient to assume that $\mathcal{P}$ consists of all continuous seminorms. In either case the resulting topology on $\mathcal{X}$ remains unchanged.

**1.5. Example.** Let $X$ be completely regular and let $C(X)=$ all continuous functions from $X$ into $\mathbb{F}$. If $K$ is a compact subset of $X$, define $p_K(f)=\sup\{|f(x)|:x\in K\}$. Then $\{p_K:K\text{ compact in }X\}$ is a family of seminorms that makes $C(X)$ into a LCS.

**1.6. Example.** Let $G$ be an open subset of $\mathbb{C}$ and let $H(G)$ be the subset of $C_{\mathbb{C}}(G)$ consisting of all analytic functions on $G$. Define the seminorms of (1.5) on $H(G)$. Then $H(G)$ is a LCS. Also, the topology defined on $H(G)$ by these seminorms is the topology of uniform convergence on compact subsets—the usual topology for discussing analytic functions.

**1.7. Example.** Let $\mathcal{X}$ be a normed space. For each $x^*$ in $\mathcal{X}^*$, define $p_{x^*}(x)=|x^*(x)|$. Then $p_{x^*}$ is a seminorm and if $\mathcal{P}=\{p_{x^*}:x^*\in\mathcal{X}^*\}$, $\mathcal{P}$ makes $\mathcal{X}$ into a LCS. The topology defined on $\mathcal{X}$ by these seminorms is called the *weak topology* and is often denoted by $\sigma(\mathcal{X},\mathcal{X}^*)$.

**1.8. Example.** Let $\mathcal{X}$ be a normed space and for each $x$ in $\mathcal{X}$ define $p_x:\mathcal{X}^*\to[0,\infty)$ by $p_x(x^*)=|x^*(x)|$. Then $p_x$ is a seminorm and $\mathcal{P}=\{p_x:x\in\mathcal{X}\}$ makes $\mathcal{X}^*$ into a LCS. The topology defined by these seminorms is called the *weak-star* (or *weak*$^*$ or $\mathrm{wk}^*$) *topology* on $\mathcal{X}^*$. It is often denoted by $\sigma(\mathcal{X}^*,\mathcal{X})$.

The spaces $\mathcal{X}$ with its weak topology and $\mathcal{X}^*$ with its weak$^*$ topology are very important and will be explored in depth in Chapter V.

Recall the definition of convex set from (I.2.4). If $a,b\in\mathcal{X}$, then the *line segment* from $a$ to $b$ is defined as $[a,b]\equiv\{tb+(1-t)a:0\leq t\leq1\}$. So a set $A$ is convex if and only if $[a,b]\subseteq A$ whenever $a,b\in A$. The proof of the next result is left to the reader.

**1.9. Proposition.** (a) *A set $A$ is convex if and only if whenever $x_1,\ldots,x_n\in A$ and $t_1,\ldots,t_n\in[0,1]$ with $\sum_jt_j=1$, then $\sum_jt_jx_j\in A$.* (b) *If $\{A_i:i\in I\}$ is a collection of convex sets, then $\bigcap_i A_i$ is convex.*

**1.10. Definition.** If $A\subseteq\mathcal{X}$, the *convex hull* of $A$, denoted by $\operatorname{co}(A)$, is the intersection of all convex sets that contain $A$. If $\mathcal{X}$ is a TVS, then the *closed convex hull* of $A$ is the intersection of all closed convex subsets of $\mathcal{X}$ that contain $A$; it is denoted by $\overline{\operatorname{co}}(A)$.

Since a vector space is itself convex, each subset of $\mathcal{X}$ is contained in a convex set. This fact and Proposition 1.9(b) imply that $\operatorname{co}(A)$ is well defined and convex. Also, $\overline{\operatorname{co}}(A)$ is a closed convex set.

If $\mathcal{X}$ is a normed space, then $\{x:\|x\|\leq1\}$ and $\{x:\|x\|<1\}$ are both convex sets. If $f\in\mathcal{X}^*$, $\{x:|f(x)|\leq1\}$, $\{x:\operatorname{Re}f(x)\leq1\}$, $\{x:\operatorname{Re}f(x)>1\}$ are


<a id="pdf-page-117"></a>
all convex. In fact, if $T:\mathscr{X}\to\mathscr{Y}$ is a real linear map and $C$ is a convex subset of $\mathscr{Y}$, then $T^{-1}(C)$ is convex in $\mathscr{X}$.

**1.11. Proposition.** *Let $\mathscr{X}$ be a TVS and let $A$ be a convex subset of $\mathscr{X}$. Then (a) $\operatorname{cl}A$ is convex; (b) if $a\in\operatorname{int}A$ and $b\in\operatorname{cl}A$, then $[a,b)\equiv\{tb+(1-t)a:0\leq t<1\}\subseteq\operatorname{int}A$.*

**PROOF.** Let $a\in A$, $b\in\operatorname{cl}A$, and $0\leq t\leq1$. Let $\{x_i\}$ be a net in $A$ such that $x_i\to b$. Then $tx_i+(1-t)a\to tb+(1-t)a$. This shows that

$$
\tag*{1.12}
b\text{ in }\operatorname{cl}A\text{ and }a\text{ in }A\text{ imply }[a,b]\subseteq\operatorname{cl}A.
$$

Using (1.12) it is easy to show that $\operatorname{cl}A$ is convex. To prove (b), fix $t$, $0<t<1$, and put $c=tb+(1-t)a$, where $a\in\operatorname{int}A$ and $b\in\operatorname{cl}A$. There is an open set $V$ in $\mathscr{X}$ such that $0\in V$ and $a+V\subseteq A$. (Why?) Hence for any $d$ in $A$

$$
\begin{aligned}
A&\supseteq td+(1-t)(a+V)\\
 &=t(d-b)+tb+(1-t)(a+V)\\
 &=[t(d-b)+(1-t)V]+c.
\end{aligned}
$$

If it can be shown that there is an element $d$ in $A$ such that $0\in t(d-b)+(1-t)V=U$, then the preceding inclusion shows that $c\in\operatorname{int}A$ since $U$ is open (Exercise 4). Note that the finding of such a $d$ in $A$ is equivalent to finding a $d$ such that $0\in t^{-1}(1-t)V+(d-b)$ or $d\in b-t^{-1}(1-t)V$. But $0\in-t^{-1}(1-t)V$ and this set is open. Since $b\in\operatorname{cl}A$, $d$ can be found in $A$. ■

**1.13. Corollary.** *If $A\subseteq\mathscr{X}$, then $\overline{\operatorname{co}}(A)$ is the closure of $\operatorname{co}(A)$.*

A set $A\subseteq\mathscr{X}$ is *balanced* if $\alpha x\in A$ whenever $x\in A$ and $|\alpha|\leq1$. A set $A$ is *absorbing* if for each $x$ in $\mathscr{X}$ there is an $\varepsilon>0$ such that $tx\in A$ for $0\leq t<\varepsilon$. Note that an absorbing set must contain the origin. If $a\in A$, then $A$ is *absorbing at $a$* if the set $A-a$ is absorbing. Equivalently, $A$ is absorbing at $a$ if for every $x$ in $\mathscr{X}$ there is an $\varepsilon>0$ such that $a+tx\in A$ for $0\leq t<\varepsilon$.

If $\mathscr{X}$ is a vector space and $p$ is a seminorm, then $V=\{x:p(x)<1\}$ is a convex balanced set that is absorbing at each of its points. It is rather remarkable that the converse of this is true. This fact will be used to give an abstract formulation of a LCS and also to explore some geometric consequences of the Hahn–Banach Theorem.

**1.14. Proposition.** *If $\mathscr{X}$ is a vector space over $\mathbb{F}$ and $V$ is a nonempty convex, balanced set that is absorbing at each of its points, then there is a unique seminorm $p$ on $\mathscr{X}$ such that $V=\{x\in\mathscr{X}:p(x)<1\}$.*

**PROOF.** Define $p(x)$ by

$$
p(x)=\inf\{t:t\geq0\text{ and }x\in tV\}.
$$

Since $V$ is absorbing, $\mathscr{X}=\bigcup_{n=1}^{\infty}nV$, so that the set whose infimum is $p(x)$ is


<a id="pdf-page-118"></a>
nonempty. Clearly $p(0)=0$. To see that $p(\alpha x)=|\alpha|p(x)$, we can suppose that $\alpha\ne0$. Hence, because $V$ is balanced,

$$
\begin{aligned}
p(\alpha x)
&=\inf\{t\geq0:\alpha x\in tV\}\\
&=\inf\left\{t\geq0:x\in t\left(\frac{1}{\alpha}V\right)\right\}\\
&=\inf\left\{t\geq0:x\in t\left(\frac{1}{|\alpha|}V\right)\right\}\\
&=|\alpha|\inf\left\{\frac{t}{|\alpha|}:x\in\frac{t}{|\alpha|}V\right\}\\
&=|\alpha|p(x).
\end{aligned}
$$

To complete the proof that $p$ is a seminorm, note that if $\alpha,\beta\geq0$ and $a,b\in V$, then

$$
\alpha a+\beta b=(\alpha+\beta)\left(\frac{\alpha}{\alpha+\beta}a+\frac{\beta}{\alpha+\beta}b\right)\in(\alpha+\beta)V
$$

by the convexity of $V$. If $x,y\in\mathscr X$, $p(x)=\alpha$, and $p(y)=\beta$, let $\delta>0$. Then $x\in(\alpha+\delta)V$ and $y\in(\beta+\delta)V$. (Why?) Hence $x+y\in(\alpha+\delta)V+(\beta+\delta)V=(\alpha+\beta+2\delta)V$ (Exercise 11). Letting $\delta\to0$ shows that $p(x+y)\leq\alpha+\beta=p(x)+p(y)$.

It remains to show that $V=\{x:p(x)<1\}$. If $p(x)=\alpha<1$, then $\alpha<\beta<1$ implies $x\in\beta V\subseteq V$ since $V$ is balanced. Thus $V\supseteq\{x:p(x)<1\}$. If $x\in V$, then $p(x)\leq1$. Since $V$ is absorbing at $x$, there is an $\varepsilon>0$ such that for $0<t<\varepsilon$, $x+tx=y\in V$. But $x=(1+t)^{-1}y$, $y\in V$. Hence $p(x)=(1+t)^{-1}p(y)\leq(1+t)^{-1}<1$.

Uniqueness follows by (III.1.4). $\blacksquare$

The seminorm $p$ defined in the preceding proposition is called the *Minkowski function* of $V$ or the *gauge* of $V$.

Note that if $\mathscr X$ is a TVS space and $V$ is an open set in $\mathscr X$, then $V$ is absorbing at each of its points.

Using Proposition 1.14, the following characterization of a LCS can be obtained. The proof is left to the reader.

**1.15. Proposition.** *Let $\mathscr X$ be a TVS and let $\mathscr U$ be the collection of all open convex balanced subsets of $\mathscr X$. Then $\mathscr X$ is locally convex if and only if $\mathscr U$ is a basis for the neighborhood system at $0$.*

## Exercises

1. Let $\mathscr X$ be a TVS and let $\mathscr U$ be all the open sets containing $0$. Prove the following.  
   (a) If $U\in\mathscr U$, there is a $V$ in $\mathscr U$ such that $V+V\subseteq U$.  
   (b) If $U\in\mathscr U$, there is a $V$ in $\mathscr U$ such that $V\subseteq U$ and $\alpha V\subseteq V$ for all $|\alpha|\leq1$. ($V$ is balanced.)  
   (Hint: If $W\in\mathscr U$ and $\alpha W\subseteq U$ for $|\alpha|\leq\varepsilon$, then $\varepsilon W\subseteq\beta U$ for $|\beta|\geq1$.)



<a id="pdf-page-119"></a>
2. Show that a LCS is a TVS.

3. Suppose that $\mathcal X$ is a TVS but do not assume that $\mathcal X$ is Hausdorff. (a) Show that $\mathcal X$ is Hausdorff if and only if the singleton set $\{0\}$ is closed. (b) If $\mathcal X$ is Hausdorff, show that $\mathcal X$ is a regular topological space.

4. Let $\mathcal X$ be a TVS. Show: (a) if $x_0\in\mathcal X$, the map $x\mapsto x+x_0$ is a homeomorphism of $\mathcal X$ onto $\mathcal X$; (b) if $\alpha\in\mathbf F$ and $\alpha\ne0$, the map $x\mapsto\alpha x$ is a homeomorphism.

5. Prove Proposition 1.4.

6. Verify the statements made in Example 1.5. Show that a net $\{f_i\}$ in $C(X)$ converges to $f$ if and only if $f_i\to f$ uniformly on compact subsets of $X$.

7. Show that the space $H(G)$ defined in (1.6) is complete. (Every Cauchy net converges.)

8. Verify the statements made in Example 1.7. Give a basis for the neighborhood system at 0.

9. Verify the statements made in Example 1.8.

10. Prove Proposition 1.9.

11. Show that if $A$ is a convex set and $\alpha,\beta>0$, then $\alpha A+\beta A=(\alpha+\beta)A$, Give an example of a nonconvex set $A$ for which this is untrue.

12. If $\mathcal X$ is a TVS and $A$ is closed, show that $A$ is convex if and only if $\frac12(x+y)\in A$ whenever $x$ and $y\in A$.

13. Let $s=$ the space of all sequences of scalars. Thus $s=$ all functions $x:\mathbf N\to\mathbf F$. Define addition and scalar multiplication in the usual way. If $x,y\in s$, define

    $$
    d(x,y)=\sum_{n=1}^{\infty}2^{-n}\frac{|x(n)-y(n)|}{1+|x(n)-y(n)|}.
    $$

    Show that $d$ is a metric on $s$ and that with this topology $s$ is a TVS. Also show that $s$ is complete.

14. Let $(X,\Omega,\mu)$ be a finite measure space, let $\mathcal M$ be the space of $\Omega$-measurable functions, and identify two functions that agree a.e. $[\mu]$. If $f,g\in\mathcal M$, define

    $$
    d(f,g)=\int\frac{|f-g|}{1+|f-g|}\,d\mu.
    $$

    Then $d$ is a metric on $\mathcal M$ and $(\mathcal M,d)$ is a complete TVS. Is there a relationship between this example and the space $s$ of Exercise 13?

15. If $\mathcal X$ is a TVS and $A\subseteq\mathcal X$, then $\operatorname{cl}A=\bigcap\{A+V:0\in V\text{ and }V\text{ is open}\}$.

16. If $\mathcal X$ is a TVS and $\mathcal M$ is a closed linear space, then $\mathcal X/\mathcal M$ with the quotient topology is a TVS. If $p$ is a seminorm on $\mathcal X$, define $\bar p$ on $\mathcal X/\mathcal M$ by $\bar p(x+\mathcal M)=\inf\{p(x+y):y\in\mathcal M\}$. Show that $\bar p$ is a seminorm on $\mathcal X/\mathcal M$. Show that if $\mathcal X$ is a LCS, then so is $\mathcal X/\mathcal M$.

17. If $\{\mathcal X_i:i\in I\}$ is a family of TVS’s, then $\mathcal X=\prod\{\mathcal X_i:i\in I\}$ with the product topology is a TVS. If each $\mathcal X_i$ is a LCS, then so is $\mathcal X$. If $\mathcal X$ is a LCS, must each $\mathcal X_i$ be a LCS?



<a id="pdf-page-120"></a>
18. If $\mathcal{X}$ is a finite-dimensional vector space and $\mathcal{T}_1,\mathcal{T}_2$ are two topologies on $\mathcal{X}$ that make $\mathcal{X}$ into a TVS, then $\mathcal{T}_1=\mathcal{T}_2$.

19. If $\mathcal{X}$ is a TVS and $\mathcal{M}$ is a finite dimensional linear manifold in $\mathcal{X}$, then $\mathcal{M}$ is closed and $\mathcal{Y}+\mathcal{M}$ is closed for any closed subspace $\mathcal{Y}$ of $\mathcal{X}$.

20. Let $\mathcal{X}$ be any infinite dimensional vector space and let $\mathcal{T}$ be the collection of all subsets $W$ of $\mathcal{X}$ such that if $x\in W$, then there is a convex balanced set $U$ with $x+U\subseteq W$ and $U\cap\mathcal{M}$ open in $\mathcal{M}$ for every finite dimensional linear manifold $\mathcal{M}$ in $\mathcal{X}$. (Each such $\mathcal{M}$ is given its usual topology.) Show: (a) $(\mathcal{X},\mathcal{T})$ is a LCS; (b) a set $F$ is closed in $\mathcal{X}$ if and only if $F\cap\mathcal{M}$ is closed for every finite dimensional subspace $\mathcal{M}$ of $\mathcal{X}$; (c) if $Y$ is a topological space and $f:\mathcal{X}\to Y$ (not necessarily linear), then $f$ is continuous if and only if $f|_{\mathcal{M}}$ is continuous for every finite dimensional space $\mathcal{M}$; (d) if $\mathcal{Y}$ is a TVS and $T:\mathcal{X}\to\mathcal{Y}$ is a linear map, then $T$ is continuous.

21. Let $X$ be a locally compact space and for each $\phi$ in $C_0(X)$, define $p_\phi(f)=\|\phi f\|_\infty$ for $f$ in $C_b(X)$. Show that $p_\phi$ is a seminorm on $C_b(X)$. Let $\beta=$ the topology defined by these seminorms. Show that $(C_b(X),\beta)$ is a LCS that is complete. $\beta$ is called the *strict topology*.

22. For $0<p<1$, let $l^p=$ all sequences $x$ such that $\sum_{n=1}^{\infty}|x(n)|^p<\infty$. Define $d(x,y)=\sum_{n=1}^{\infty}|x(n)-y(n)|^p$ (no $p$th root). Then $d$ is a metric and $(l^p,d)$ is a TVS that is not locally convex.

23. Let $\mathcal{X}$ and $\mathcal{Y}$ be locally convex spaces and let $T:\mathcal{X}\to\mathcal{Y}$ be a linear transformation. Show that $T$ is continuous if and only if for every continuous seminorm $p$ on $\mathcal{Y}$, $p\circ T$ is a continuous seminorm on $\mathcal{X}$.

24. Let $\mathcal{X}$ be a LCS and let $G$ be an open connected subset of $\mathcal{X}$. Show that $G$ is arcwise connected.

## §2. Metrizable and Normable Locally Convex Spaces

Which LCS’s are metrizable? That is, which have a topology which is defined by a metric? Which LCS’s have a topology that is defined by a norm? Both are interesting questions and both answers could be useful.

If $\mathcal{P}$ is a family of seminorms on $\mathcal{X}$ and $\mathcal{X}$ is a TVS, say that $\mathcal{P}$ determines the topology on $\mathcal{X}$ if the topology of $\mathcal{X}$ is the same as the topology induced by $\mathcal{P}$.

**2.1. Proposition.** *Let $\{p_1,p_2,\ldots\}$ be a sequence of seminorms on $\mathcal{X}$ such that $\bigcap_{n=1}^{\infty}\{x:p_n(x)=0\}=(0)$. For $x$ and $y$ in $\mathcal{X}$, define*

$$
d(x,y)=\sum_{n=1}^{\infty}2^{-n}\frac{p_n(x-y)}{1+p_n(x-y)}.
$$

*Then $d$ is a metric on $\mathcal{X}$ and the topology on $\mathcal{X}$ defined by $d$ is the topology*



<a id="pdf-page-121"></a>
on $\mathcal X$ defined by the seminorms $\{p_1,p_2,\ldots\}$. Thus a LCS is metrizable if and only if its topology is determined by a countable family of seminorms.

**Proof.** It is left as an exercise for the reader to show that $d$ is a metric and induces the same topology as $\{p_n\}$. If $\mathcal X$ is a LCS and its topology is determined by a countable family of seminorms, it is immediate that $\mathcal X$ is metrizable. For the converse, assume that $\mathcal X$ is metrizable and its metric is $\rho$. Let $U_n=\{x:\rho(x,0)<1/n\}$. Because $\mathcal X$ is locally convex, there are continuous seminorms $q_1,\ldots,q_k$ and positive numbers $\varepsilon_1,\ldots,\varepsilon_k$ such that $\bigcap_{j=1}^{k}\{x:q_j(x)<\varepsilon_j\}\subseteq U_n$. If $p_n=\varepsilon_1^{-1}q_1+\cdots+\varepsilon_k^{-1}q_k$, then $x\in U_n$ whenever $p_n(x)<1$. Clearly, $p_n$ is continuous for each $n$. Thus if $x_j\to0$ in $\mathcal X$, then for each $n$, $p_n(x_j)\to0$ as $j\to\infty$. Conversely, suppose that for each $n$, $p_n(x_j)\to0$ as $j\to\infty$. If $\varepsilon>0$, let $n>\varepsilon^{-1}$. Then there is a $j_0$ such that for $j\geq j_0$, $p_n(x_j)<1$. Thus, for $j\geq j_0$, $x_j\in U_n\subseteq\{x:\rho(x,0)<\varepsilon\}$. That is, $\rho(x_j,0)<\varepsilon$ for $j\geq j_0$ and so $x_j\to0$ in $\mathcal X$. This shows that $\{p_n\}$ determines the topology on $\mathcal X$. (Why?) ■

**2.2. Example.** If $C(X)$ is as in Example 1.5, then $C(X)$ is metrizable if and only if $X=\bigcup_{n=1}^{\infty}K_n$, where each $K_n$ is compact, $K_1\subseteq K_2\subseteq\cdots$, and if $K$ is any compact subset of $X$, then $K\subseteq K_n$ for some $n$.

**2.3. Example.** If $X$ is locally compact and $C(X)$ is as in Example 1.5, then $C(X)$ is metrizable if and only if $X$ is $\sigma$-compact (that is, $X$ is the union of a sequence of compact sets). If $H(G)$ is as in Example 1.6, then $H(G)$ is metrizable.

If $\mathcal X$ is a vector space and $d$ is a metric on $\mathcal X$, say that $d$ is *translation invariant* if $d(x+z,y+z)=d(x,y)$ for all $x,y,z$ in $\mathcal X$. Note that the metric defined by a norm as well as the metric defined in (2.1) are translation invariant.

**2.4. Definition.** A *Fréchet space* is a TVS $\mathcal X$ whose topology is defined by a translation invariant metric $d$ and such that $(\mathcal X,d)$ is complete.

It should be pointed out that some authors include in the definition of a Fréchet space the assumption that $\mathcal X$ is locally convex.

**2.5. Definition.** If $\mathcal X$ is a TVS and $B\subseteq\mathcal X$, then $B$ is *bounded* if for every open set $U$ containing $0$, there is an $\varepsilon>0$ such that $\varepsilon B\subseteq U$.

If $\mathcal X$ is a normed space, then it is easy to see that a set $B$ is bounded if and only if $\sup\{\|b\|:b\in B\}<\infty$, so the definition is intuitively correct.

Also, notice that if $\|\cdot\|$ is a norm, $\{x:\|x\|<1\}$ is itself bounded. This is not true for seminorms. For example, if $C(\mathbb R)$ is topologized as in (1.5), let $p(f)=\sup\{|f(t)|:0\leq t\leq1\}$. Then $p$ is a continuous seminorm. However,



<a id="pdf-page-122"></a>
$\{f:p(f)<1\}$ is not bounded. In fact, if $f_0$ is any function in $C(\mathbb{R})$ that vanishes on $[0,1]$, $\{\alpha f_0:\alpha\in\mathbb{R}\}\subseteq\{f:p(f)<1\}$. The fact that a normed space possesses a bounded open set is characteristic.

**2.6. Proposition.** *If $\mathscr{X}$ is a LCS, then $\mathscr{X}$ is normable if and only if $\mathscr{X}$ has a nonempty bounded open set.*

**Proof.** It has already been shown that a normed space has a bounded open set. So assume that $\mathscr{X}$ is a LCS that has a bounded open set $U$. It must be shown that there is norm on $\mathscr{X}$ that defines the same topology. By translation, it may be assumed that $0\in U$ (see Exercise 4i). By local convexity, there is a continuous seminorm $p$ such that $\{x:p(x)<1\}\equiv V\subseteq U$ (Why?). It will be shown that $p$ is a norm and defines the topology on $\mathscr{X}$.

To see that $p$ is a norm, suppose that $x\in\mathscr{X}$, $x\ne0$. Let $W_0,W_x$ be disjoint open sets such that $0\in W_0$ and $x\in W_x$. Then there is an $\varepsilon>0$ such that $W_0\supseteq\varepsilon U\supseteq\varepsilon V$. But $\varepsilon V=\{y:p(y)<\varepsilon\}$. Since $x\notin W_0$, $p(x)\geq\varepsilon$. Hence $p$ is a norm.

Because $p$ is continuous on $\mathscr{X}$, to show that $p$ defines the topology of $\mathscr{X}$ it suffices to show that if $q$ is any continuous seminorm on $\mathscr{X}$, there is an $\alpha>0$ such that $q\leq\alpha p$ (Why?). But because $q$ is continuous, there is an $\varepsilon>0$ such that $\{x:q(x)<1\}\supseteq\varepsilon U\supseteq\varepsilon V$. That is, $p(x)<\varepsilon$ implies $q(x)<1$. By Lemma III.1.4, $q\leq\varepsilon^{-1}p$. $\blacksquare$

## Exercises

1. Supply the missing details in the proof of Proposition 2.1.

2. Verify the statements in Example 2.2.

3. Verify the statements in Example 2.3.

4. Let $\mathscr{X}$ be a TVS and prove the following: (a) If $B$ is a bounded subset of $\mathscr{X}$, then so is $\operatorname{cl}B$. (b) The finite union of bounded sets is bounded. (c) Every compact set is bounded. (d) If $B\subseteq\mathscr{X}$, then $B$ is bounded if and only if for every sequence $\{x_n\}$ contained in $B$ and for every $\{\alpha_n\}$ in $c_0$, $\alpha_nx_n\to0$ in $\mathscr{X}$. (e) If $\mathscr{Y}$ is a TVS, $T:\mathscr{X}\to\mathscr{Y}$ is a continuous linear transformation, and $B$ is a bounded subset of $\mathscr{X}$, then $T(B)$ is a bounded subset of $\mathscr{Y}$. (f) If $\mathscr{X}$ is a LCS and $B\subseteq\mathscr{X}$, then $B$ is bounded if and only if for every continuous seminorm $p$, $\sup\{p(b):b\in B\}<\infty$. (g) If $\mathscr{X}$ is a normed space and $B\subseteq\mathscr{X}$, then $B$ is bounded if and only if $\sup\{\|b\|:b\in B\}<\infty$. (h) If $\mathscr{X}$ is a Fréchet space, then bounded sets have finite diameter, but not conversely. (i) The translate of a bounded set is bounded.

5. If $\mathscr{X}$ is a LCS, show that $\mathscr{X}$ is metrizable if and only if $\mathscr{X}$ is first countable. Is this equivalent to saying that $\{0\}$ is a $G_\delta$ set?

6. Let $X$ be a locally compact space and give $C_b(X)$ the strict topology defined in Exercise 1.21. Show that a subset of $C_b(X)$ is $\beta$-bounded if and only if it is norm bounded.

7. With the notation of Exercise 6, show that $(C_b(X),\beta)$ is metrizable if and only if $X$ is compact.

8. Prove the Open Mapping Theorem for Fréchet spaces.



<a id="pdf-page-123"></a>
## §3. Some Geometric Consequences of the Hahn–Banach Theorem

In order to exploit the Hahn–Banach Theorem in the setting of a LCS, it is necessary to establish some properties of continuous linear functionals. The proofs of the relevant propositions are similar to the proofs of the corresponding facts about linear functionals on normed spaces given in §III.5. For example, a hyperplane in a TVS is either closed or dense (see III.5.2). The proof of the next fact is similar to the proof of (III.2.1) and (III.5.3) and will not be given.

**3.1. Theorem.** *If $\mathscr{X}$ is a TVS and $f:\mathscr{X}\to\mathbb{F}$ is a linear functional, then the following statements are equivalent.*

(a) $f$ is continuous.

(b) $f$ is continuous at 0.

(c) $f$ is continuous at some point.

(d) $\ker f$ is closed.

(e) $x\mapsto |f(x)|$ is a continuous seminorm.

*If $\mathscr{X}$ is a LCS and $\mathscr{P}$ is a family of seminorms that defines the topology on $\mathscr{X}$, then the statements above are equivalent to the following:*

(f) There are $p_1,\ldots,p_n$ in $\mathscr{P}$ and positive scalars $\alpha_1,\ldots,\alpha_n$ such that $|f(x)|\leq\sum_{k=1}^{n}\alpha_kp_k(x)$ for all $x$.

The proof of the next proposition is similar to the proof of Proposition 1.14 and will not be given.

**3.2. Proposition.** *Let $\mathscr{X}$ be a TVS and suppose that $G$ is an open convex subset of $\mathscr{X}$ that contains the origin. If*

$$
q(x)=\inf\{t:t\geq 0\text{ and }x\in tG\},
$$

*then $q$ is a non-negative continuous sublinear functional and $G=\{x:q(x)<1\}$.*

Note that the difference between the preceding proposition and (1.14) is that here $G$ is not assumed to be balanced and the consequence is a sublinear functional ($q(\alpha x)=\alpha q(x)$ if $\alpha\geq 0$) that is not necessarily a seminorm.

The geometric consequences of the Hahn–Banach Theorem are achieved by interpreting that theorem in light of the correspondence between linear functionals and hyperplanes and between sublinear functionals and open convex neighborhoods of the origin. The next result is typical.

**3.3. Theorem.** *If $\mathscr{X}$ is a TVS and $G$ is an open convex nonempty subset of $\mathscr{X}$ that does not contain the origin, then there is a closed hyperplane $\mathscr{M}$ such that $\mathscr{M}\cap G=\square$.*



<a id="pdf-page-124"></a>
**Proof.** *Case 1.* $\mathcal{X}$ is an $\mathbb{R}$-linear space. Pick any $x_0$ in $G$ and let $H=x_0-G$. Then $H$ is an open convex set containing $0$. (Verify). By (3.2) there is a continuous nonnegative sublinear functional $q:\mathcal{X}\to\mathbb{R}$ such that $H=\{x:q(x)<1\}$. Since $x_0\notin H$, $q(x_0)\geq 1$.

Let $\mathcal{Y}\equiv\{\alpha x_0:\alpha\in\mathbb{R}\}$ and define $f_0:\mathcal{Y}\to\mathbb{R}$ by $f_0(\alpha x_0)=\alpha q(x_0)$. If $\alpha\geq 0$, then $f_0(\alpha x_0)=\alpha q(x_0)=q(\alpha x_0)$; if $\alpha<0$, then $f_0(\alpha x_0)=\alpha q(x_0)\leq\alpha<0\leq q(\alpha x_0)$. So $f_0\leq q$ on $\mathcal{Y}$. Let $f:\mathcal{X}\to\mathbb{R}$ be a linear functional such that $f|_{\mathcal{Y}}=f_0$ and $f\leq q$ on $\mathcal{X}$. Put $\mathcal{M}=\ker f$.

Now if $x\in G$, then $x_0-x\in H$ and so $f(x_0)-f(x)=f(x_0-x)\leq q(x_0-x)<1$. Therefore $f(x)>f(x_0)-1=q(x_0)-1\geq 0$ for all $x$ in $G$. Thus $\mathcal{M}\cap G=\square$.

*Case 2.* $\mathcal{X}$ is a $\mathbb{C}$-linear space. Lemma III.6.3 will be used here. Using Case 1 and the fact that $\mathcal{X}$ is also an $\mathbb{R}$-linear space, there is a continuous $\mathbb{R}$-linear functional $f:\mathcal{X}\to\mathbb{R}$ such that $G\cap\ker f=\square$. If $F(x)=f(x)-if(ix)$, then $F$ is a $\mathbb{C}$-linear functional and $f=\operatorname{Re}F$ (III.6.3). Hence $F(x)=0$ if and only if $f(x)=f(ix)=0$; that is, $\mathcal{M}=\ker F=\ker f\cap[i\ker f]$. So $\mathcal{M}$ is a closed hyperplane and $\mathcal{M}\cap G=\square$. $\blacksquare$

An *affine hyperplane* in $\mathcal{X}$ is a set $\mathcal{M}$ such that for every $x_0$ in $\mathcal{M}$, $\mathcal{M}-x_0$ is a hyperplane. (See Exercise 3.) An *affine manifold* in $\mathcal{X}$ is a set $\mathcal{Y}$ such that for every $x_0$ in $\mathcal{Y}$, $\mathcal{Y}-x_0$ is a linear manifold in $\mathcal{X}$. An *affine subspace* of a TVS $\mathcal{X}$ is a closed affine manifold.

**3.4. Corollary.** *Let $\mathcal{X}$ be a TVS and let $G$ be an open convex nonempty subset of $\mathcal{X}$. If $\mathcal{Y}$ is an affine subspace of $\mathcal{X}$ such that $\mathcal{Y}\cap G=\square$, then there is a closed affine hyperplane $\mathcal{M}$ in $\mathcal{X}$ such that $\mathcal{Y}\subseteq\mathcal{M}$ and $\mathcal{M}\cap G=\square$.*

**Proof.** By considering $G-x_0$ and $\mathcal{Y}-x_0$ for any $x_0$ in $\mathcal{Y}$, it may be assumed that $\mathcal{Y}$ is a linear subspace of $\mathcal{X}$. Let $Q:\mathcal{X}\to\mathcal{X}/\mathcal{Y}$ be the natural map. Since $Q^{-1}(Q(G))=\{y+G:y\in\mathcal{Y}\}$, $Q(G)$ is open in $\mathcal{X}/\mathcal{Y}$. It is easy to see that $Q(G)$ is also convex. Since $\mathcal{Y}\cap G=\square$, $0\notin Q(G)$. By the preceding theorem, there is a closed hyperplane $\mathcal{N}$ in $\mathcal{X}/\mathcal{Y}$ such that $\mathcal{N}\cap Q(G)=\square$. Let $\mathcal{M}=Q^{-1}(\mathcal{N})$. It is easy to check that $\mathcal{M}$ has the desired properties. $\blacksquare$

There is a great advantage inherent in a geometric discussion of real TVS’s. Namely, if $f:\mathcal{X}\to\mathbb{R}$ is a nonzero continuous $\mathbb{R}$-linear functional, then the hyperplane $\ker f$ disconnects the space. That is, $\mathcal{X}\setminus\ker f$ has two components (see Exercises 4 and 5). It thus becomes convenient to make the following definitions.

**3.5. Definition.** Let $\mathcal{X}$ be a real TVS. A subset $S$ of $\mathcal{X}$ is called an *open half-space* if there is a continuous linear functional $f:\mathcal{X}\to\mathbb{R}$ such that $S=\{x\in\mathcal{X}:f(x)>\alpha\}$ for some $\alpha$. $S$ is a *closed half-space* if there is a continuous linear functional $f:\mathcal{X}\to\mathbb{R}$ such that $S=\{x\in\mathcal{X}:f(x)\geq\alpha\}$ for some $\alpha$.

Two subsets $A$ and $B$ of $\mathcal{X}$ are said to be *strictly separated* if they are contained in disjoint open half-spaces; they are *separated* if they are contained in two closed half-spaces whose intersection is a closed affine hyperplane.



<a id="pdf-page-125"></a>
**3.6. Proposition.** Let $\mathcal{X}$ be a real TVS.

(a) The closure of an open half-space is a closed half-space and the interior of a closed half-space is an open half-space.

(b) If $A,B\subseteq\mathcal{X}$, then $A$ and $B$ are strictly separated (separated) if and only if there is a continuous linear functional $f:\mathcal{X}\to\mathbb{R}$ and a real scalar $\alpha$ such that $f(a)>\alpha$ for all $a$ in $A$ and $f(b)<\alpha$ for all $b$ in $B$ ($f(a)\geq\alpha$ for all $a$ in $A$ and $f(b)\leq\alpha$ for all $b$ in $B$).

**Proof.** Exercise 6.

In many ways, the next result is the most important “separation” theorem as the other separation theorems follow from this one. However, the most used separation theorem is Theorem 3.9 below.

**3.7. Theorem.** If $\mathcal{X}$ is a real TVS and $A$ and $B$ are disjoint convex sets with $A$ open, then there is a continuous linear functional $f:\mathcal{X}\to\mathbb{R}$ and a real scalar $\alpha$ such that $f(a)<\alpha$ for all $a$ in $A$ and $f(b)\geq\alpha$ for all $b$ in $B$. If $B$ is also open, then $A$ and $B$ are strictly separated.

**Proof.** Let $G=A-B\equiv\{a-b:a\in A,b\in B\}$; it is easy to verify that $G$ is convex (do it!). Also, $G=\bigcup\{A-b:b\in B\}$, so $G$ is open. Moreover, because $A\cap B=\varnothing$, $0\notin G$. By Theorem 3.3 there is a closed hyperplane $\mathcal{M}$ in $\mathcal{X}$ such that $\mathcal{M}\cap G=\varnothing$. Let $f:\mathcal{X}\to\mathbb{R}$ be a linear functional such that $\mathcal{M}=\ker f$. Now $f(G)$ is a convex subset of $\mathbb{R}$ and $0\notin f(G)$. Hence either $f(x)>0$ for all $x$ in $G$ or $f(x)<0$ for all $x$ in $G$; suppose $f(x)>0$ for all $x$ in $G$. Thus if $a\in A$ and $b\in B$, $0<f(a-b)=f(a)-f(b)$; that is, $f(a)>f(b)$. Therefore there is a real number $\alpha$ such that

$$
\sup\{f(b):b\in B\}\leq\alpha\leq\inf\{f(a):a\in A\}.
$$

But $f(A)$ and $f(B)$ are open intervals if $B$ is open (Exercise 7), so $f<\alpha$ on $B$ and $f>\alpha$ on $A$. ■

**3.8. Lemma.** If $\mathcal{X}$ is a TVS, $K$ is a compact subset of $\mathcal{X}$, and $V$ is an open subset of $\mathcal{X}$ such that $K\subseteq V$, then there is an open neighborhood of $0$, $U$, such that $K+U\subseteq V$.

**Proof.** Let $\mathcal{U}_0=$ all of the open neighborhoods of $0$. Suppose that for each $U$ in $\mathcal{U}_0$, $K+U$ is not contained in $V$. Thus, for each $U$ in $\mathcal{U}_0$ there is a vector $x_U$ in $K$ and a $y_U$ in $U$ such that $x_U+y_U\in\mathcal{X}\setminus V$. Order $\mathcal{U}_0$ by reverse inclusion; that is, $U_1\geq U_2$ if $U_1\subseteq U_2$. Then $\mathcal{U}_0$ is a directed set and $\{x_U\}$ and $\{y_U\}$ are nets. Now $y_U\to0$ in $\mathcal{X}$. Because $K$ is compact there is an $x$ in $K$ such that $x_U\underset{\mathrm{cl}}{\longrightarrow}x$ ($\{x_U\}$ cluster at $x$). Hence $x_U+y_U\underset{\mathrm{cl}}{\longrightarrow}x+0=x$. (Why?) Hence $x\in\operatorname{cl}(\mathcal{X}\setminus V)=\mathcal{X}\setminus V$, a contradiction. ■

The condition that $K$ be compact in the preceding lemma is necessary; it is not enough to assume that $K$ is closed. (What is a counterexample?)



<a id="pdf-page-126"></a>
**3.9. Theorem.** Let $\mathscr{X}$ be a real LCS and let $A$ and $B$ be two disjoint closed convex subsets of $\mathscr{X}$. If $B$ is compact, then $A$ and $B$ are strictly separated.

**Proof.** By hypothesis, $B$ is a compact subset of the open set $\mathscr{X}\setminus A$. The preceding lemma implies there is an open neighborhood $U_1$ of $0$ such that $B+U_1\subseteq\mathscr{X}\setminus A$. Because $\mathscr{X}$ is locally convex, there is a continuous seminorm $p$ on $\mathscr{X}$ such that $\{x:p(x)<1\}\subseteq U_1$. Put $U=\{x:p(x)<\frac12\}$. Then $(B+U)\cap(A+U)=\square$ (Verify!), and $A+U$ and $B+U$ are open convex subsets of $\mathscr{X}$ that contain $A$ and $B$, respectively. (Why?) So the result follows from Theorem 3.7. $\blacksquare$

The fact that one of the two closed convex sets in the preceding theorem is assumed to be compact is necessary. In fact, if $\mathscr{X}=\mathbb{R}^2$, $A=\{(x,y)\in\mathbb{R}^2:y\leqslant0\}$, and $B=\{(x,y)\in\mathbb{R}^2:y\geqslant x^{-1}>0\}$, then $A$ and $B$ are disjoint closed convex subsets of $\mathbb{R}^2$ that cannot be strictly separated.

The next result generalizes Corollary III.6.8, though, of course, the metric content of (III.6.8) is missing.

**3.10. Corollary.** If $\mathscr{X}$ is a real LCS, $A$ is a closed convex subset of $\mathscr{X}$, and $x\notin A$, then $x$ is strictly separated from $A$.

**3.11. Corollary.** If $\mathscr{X}$ is a real LCS and $A\subseteq\mathscr{X}$, then $\overline{\operatorname{co}}(A)$ is the intersection of the closed half-spaces containing $A$.

**Proof.** Let $\mathscr{H}$ be the collection of all closed half-spaces containing $A$. Since each set in $\mathscr{H}$ is closed and convex, $\overline{\operatorname{co}}(A)\subseteq\bigcap\{H:H\in\mathscr{H}\}$. On the other hand, if $x_0\notin\overline{\operatorname{co}}(A)$, then (3.10) implies there is a continuous linear functional $f:\mathscr{X}\to\mathbb{R}$ and an $\alpha$ in $\mathbb{R}$ such that $f(x_0)>\alpha$ and $f(x)<\alpha$ for all $x$ in $\overline{\operatorname{co}}(A)$. Thus $H=\{x:f(x)\leqslant\alpha\}$ belongs to $\mathscr{H}$ and $x_0\notin H$. $\blacksquare$

The next result generalizes Theorem III.6.13.

**3.12. Corollary.** If $\mathscr{X}$ is a real LCS and $A\subseteq\mathscr{X}$, then the closed linear span of $A$ is the intersection of all closed hyperplanes containing $A$.

If $\mathscr{X}$ is a complex LCS, it is also a real LCS. This can be used to formulate and prove versions of the preceding results. As a sample, the following complex version of Theorem 3.9 is presented.

**3.13. Theorem.** Let $\mathscr{X}$ be a complex LCS and let $A$ and $B$ be two disjoint closed convex subsets of $\mathscr{X}$. If $B$ is compact, then there is a continuous linear functional $f:\mathscr{X}\to\mathbb{C}$, an $\alpha$ in $\mathbb{R}$, and an $\varepsilon>0$ such that for $a$ in $A$ and $b$ in $B$,

$$
\operatorname{Re}f(a)\leqslant\alpha<\alpha+\varepsilon\leqslant\operatorname{Re}f(b).
$$

**3.14. Corollary.** If $\mathscr{X}$ is a LCS and $\mathscr{Y}$ is a linear manifold in $\mathscr{X}$, then $\mathscr{Y}$ is



<a id="pdf-page-127"></a>
*dense in $\mathcal X$ if and only if the only continuous linear functional on $\mathcal X$ that vanishes on $\mathcal Y$ is the identically zero functional.*

**3.15. Corollary.** *If $\mathcal X$ is a LCS, $\mathcal Y$ is a closed linear subspace of $\mathcal X$, and $x_0\in\mathcal X\setminus\mathcal Y$, then there is a continuous linear functional $f:\mathcal X\to\mathbf F$ such that $f(y)=0$ for all $y$ in $\mathcal Y$ and $f(x_0)=1$.*

These results imply that on a LCS there are many continuous linear functionals. Compare the results of this section with those of §III.6.

The hypothesis that $\mathcal X$ is locally convex does not appear in the results prior to Theorem 3.9. The reason for this is that in the preceding results the existence of an open convex subset of $\mathcal X$ is assumed. In Theorem 3.9 such a set must be manufactured. Without the hypothesis of local convexity it may be that the only open convex sets are the whole space itself and the empty set.

**3.16. Example.** For $0<p<1$, let $L^p(0,1)$ be the collection of equivalence classes of measurable functions $f:(0,1)\to\mathbf R$ such that

$$
((f))_p=\int_0^1 |f(x)|^p\,dx<\infty.
$$

It will be shown that $d(f,g)=((f-g))_p$ is a metric on $L^p(0,1)$ and that with this metric $L^p(0,1)$ is a Fréchet space. It will also be shown, however, that $L^p(0,1)$ has only one nonempty open convex set, namely itself. So $L^p(0,1)$, $0<p<1$, is most emphatically not locally convex. The proof of these facts begins with the following inequality.

**3.17** For $s,t$ in $[0,\infty)$ and $0<p<1$, $(s+t)^p\leq s^p+t^p$.

To see this, let $f(t)=s^p+t^p-(s+t)^p$ for $t\geq0$, $s$ fixed. Then $f'(t)=pt^{p-1}-p(s+t)^{p-1}$. Since $p-1<0$ and $s+t\geq t$, $f'(t)\geq0$. Thus $0=f(0)\leq f(t)$. This proves (3.17)

If $d(f,g)=((f-g))_p$ for $f,g$ in $L^p(0,1)$, then (3.17) implies that $d(f,g)\leq d(f,h)+d(h,g)$ for all $f,g,h$ in $L^p(0,1)$. It follows that $d$ is a metric on $L^p(0,1)$. Clearly $d$ is translation invariant.

**3.18** $L^p(0,1)$, $0<p<1$, is complete.

The proof of this is left as an exercise.

**3.19** $L^p(0,1)$ is a TVS.

The continuity of addition is a direct consequence of the translation invariance of $d$. If $f_n\to f$ and $\alpha_n\to\alpha$, $\alpha_n$ in $\mathbf R$,

$$
\begin{aligned}
d(\alpha_n f_n,\alpha f)
&=((\alpha_n f_n-\alpha f))_p\\
&\leq ((\alpha_n f_n-\alpha_n f))_p+((\alpha_n f-\alpha f))_p\\
&=|\alpha_n|^p((f_n-f))_p+|\alpha_n-\alpha|^p((f))_p\\
&\leq C((f_n-f))_p+|\alpha_n-\alpha|^p((f))_p,
\end{aligned}
$$

where $C$ is a constant independent of $n$. Hence $\alpha_n f_n\to\alpha f$. Thus $L^p(0,1)$ is a Fréchet space.



<a id="pdf-page-128"></a>
If $G$ is a nonempty open convex subset of $L^p(0,1)$, then

**3.20**
$$
G=L^p(0,1).
$$

To see this, first suppose $f\in L^p(0,1)$ and $((f))_p=r<R$. As a function of $t$, $\int_0^t |f(x)|^p\,dx$ is continuous, assumes the value $0$ at $t=0$, and assumes the value $r$ at $t=1$. Let $0<t<1$ such that $\int_0^t |f(x)|^p\,dx=r/2$. Define $g,h:(0,1)\to\mathbb R$ by $g(x)=f(x)$ for $x\leq t$ and $0$ otherwise; $h(x)=f(x)$ for $x\geq t$ and $0$ otherwise. Now $f=g+h=\frac12(2g+2h)$ and $((2g))_p=((2h))_p=2^p(r/2)=r/2^{1-p}$. Hence $f\in\operatorname{co}B(0;R/2^{1-p})$. This implies that $B(0;R)\subseteq\operatorname{co}B(0;R/2^{1-p})$, or, equivalently, $B(0;2^{1-p}R)\subseteq\operatorname{co}B(0;R)$. Hence $B(0;4^{1-p}R)\subseteq\operatorname{co}B(0;2^{1-p}R)\subseteq\operatorname{co}B(0;R)$. Continuing we see that for all $n$, $B(0;2^{n(1-p)}R)\subseteq\operatorname{co}B(0;R)$.

So if $G$ is a nonempty open convex subset of $L^p(0,1)$, then by translation it may be assumed that $0\in G$. Thus there is an $R>0$ with $B(0;R)\subseteq G$. By the preceding paragraph, $B(0;2^{n(1-p)}R)\subseteq\operatorname{co}B(0;R)\subseteq G$ for all $n\geq1$. Therefore $L^p(0,1)\subseteq G$.

Also note that this says that the only continuous linear functional on $L^p(0,1)$, $0<p<1$, is the identically zero functional.

## EXERCISES

1. Prove Theorem 3.1.

2. Let $p$ be a sublinear functional, $G\equiv\{x:p(x)<1\}$, and define the sublinear functional $q$ for the set $G$ as in Proposition 3.2. Show that $q(x)=\max(p(x),0)$ for all $x$ in $\mathcal X$.

3. Let $\mathcal M\subseteq\mathcal X$, a TVS, and show that the following statements are equivalent: (a) $\mathcal M$ is an affine hyperplane; (b) there exists an $x_0$ in $\mathcal M$ such that $\mathcal M-x_0$ is a hyperplane; (c) there is a non-zero linear function $f:\mathcal X\to\mathbb F$ and an $\alpha$ in $\mathbb F$ such that $\mathcal M=\{x\in\mathcal X:f(x)=\alpha\}$.

4. Let $\mathcal X$ be a real TVS. Show: (a) if $G$ is an open connected subset of $\mathcal X$, then $G$ is arcwise connected; (b) if $f:\mathcal X\to\mathbb R$ is a continuous non-zero linear functional, then $\mathcal X\setminus\ker f$ has two components, $\{x:f(x)>0\}$ and $\{x:f(x)<0\}$.

5. If $\mathcal X$ is a complex TVS and $f:\mathcal X\to\mathbb C$ is a nonzero continuous linear function, show that $\mathcal X\setminus\ker f$ is connected.

6. Prove Proposition 3.6.

7. If $f:\mathcal X\to\mathbb R$ is a continuous $\mathbb R$-linear functional and $A$ is an open convex subset of $\mathcal X$, then $f(A)$ is an open interval.

8. Prove Corollary 3.12.

9. Prove Theorem 3.13.

10. State and prove a version of Theorem 3.7 for a complex TVS.

11. State and prove a version of Corollary 3.11 for a complex LCS.

12. State and prove a version of Corollary 3.12 for a complex LCS.

13. Prove (3.18).



<a id="pdf-page-129"></a>
14. Give an example of a TVS $\mathcal X$ that is not locally convex and a subspace $\mathcal Y$ of $\mathcal X$ such that there is a continuous linear functional $f$ on $\mathcal Y$ with no continuous extension to $\mathcal X$.

15. Let $\mathcal X$ be a real LCS and let $A$ and $B$ be disjoint compact convex subsets of $\mathcal X$. Suppose $\mathcal Y$ is a subspace of $\mathcal X$ and $f_0:\mathcal Y\to\mathbb R$ is a continuous linear functional such that $f_0(a)<0$ for $a$ in $A\cap\mathcal Y$ and $f_0(b)>0$ for $b$ in $B\cap\mathcal Y$. Show by an example that it is not always possible to extend $f_0$ to a continuous linear functional on $\mathcal X$ such that $f(a)<0$ or $a$ in $A$ and $f(b)>0$ for $b$ in $B$. (Hint: Let $\mathcal X=\mathbb R^3$ and let $\mathcal Y$ be the plane.)

## §4*. Some Examples of the Dual Space of a Locally Convex Space

As with a normed space, if $\mathcal X$ is a LCS, $\mathcal X^*$ denotes the space of all continuous linear functionals $f:\mathcal X\to\mathbb F$. $\mathcal X^*$ is called the *dual space* of $\mathcal X$.

**4.1. Proposition.** *Let $X$ be completely regular and let $C(X)$ be topologized as in Example 1.5. If $L:C(X)\to\mathbb F$ is a continuous linear functional, then there is a compact set $K$ and a regular Borel measure $\mu$ on $K$ such that $L(f)=\int_K f\,d\mu$ for every $f$ in $C(X)$. Conversely, each such measure defines an element of $C(X)^*$.*

**Proof.** It is easy to see that each measure $\mu$ supported on a compact set $K$ defines an element of $C(X)^*$. In fact, if $p_K(f)=\sup\{|f(x)|:x\in K\}$ and $L(f)=\int_K f\,d\mu$, then $|L(f)|\leq\|\mu\|p_K(f)$, and so $L$ is continuous.

Now assume $L\in C(X)^*$. There are compact sets $K_1,\ldots,K_n$ and positive numbers $\alpha_1,\ldots,\alpha_n$ such that $|L(f)|\leq\sum_{j=1}^n\alpha_jp_{K_j}(f)$ (3.1f). Let $K=\bigcup_{j=1}^nK_j$ and $\alpha=\max\{\alpha_j:1\leq j\leq n\}$. Then $|L(f)|\leq\alpha p_K(f)$. Hence if $f\in C(X)$ and $f|K\equiv0$, then $L(f)=0$.

Define $F:C(K)\to\mathbb F$ as follows. If $g\in C(K)$, let $\tilde g$ be any continuous extension of $g$ to $X$ and put $F(g)=L(\tilde g)$. To check that $F$ is well defined, suppose that $\tilde g_1$ and $\tilde g_2$ are both extensions of $g$ to $X$. Then $\tilde g_1-\tilde g_2=0$ on $K$, and hence $L(\tilde g_1)=L(\tilde g_2)$. Thus $F$ is well defined. It is left as an exercise for the reader to show that $F:C(K)\to\mathbb F$ is linear. If $g\in C(K)$ and $\tilde g$ is an extension in $C(X)$, then $|F(g)|=|L(\tilde g)|\leq\alpha p_K(\tilde g)=\alpha\|g\|$, where the norm is the norm of $C(K)$. By (III.5.7) there is a measure $\mu$ in $M(K)$ such that $F(g)=\int_K g\,d\mu$. If $f\in C(X)$, then $g=f|K\in C(K)$ and so $L(f)=F(g)=\int_K f\,d\mu$. ■

If $\gamma:[0,1]\to\mathbb C$ is a rectifiable curve and $f$ is a continuous function defined on the trace of $\gamma$, $\gamma([0,1])$, then $\int_\gamma f$ is the line integral of $f$ over $\gamma$. That is, $\int_\gamma f\equiv\int_0^1 f(\gamma(t))\,d\gamma(t)$. (See Conway [1978].) The next result generalizes to arbitrary regions in the plane, but for simplicity it is stated only for the disk $\mathbb D$. Recall the definition of $H(\mathbb D)$ from Example 1.6.

**4.2. Proposition.** *$L\in H(\mathbb D)^*$ if and only if there is an $r<1$ and a unique function*


<a id="pdf-page-130"></a>
$g$ analytic on $\mathbb C_\infty\setminus\overline B(0;r)$ with $g(\infty)=0$ such that

$$
\tag{4.3}
L(f)=\frac{1}{2\pi i}\int_\gamma fg
$$

for every $f$ in $H(\mathbb D)$, where $\gamma(t)=\rho e^{it}$, $0\leq t\leq2\pi$, and $r<\rho<1$.

**Proof.** Let $g$ be given and define $L$ as in (4.3). If $K=\{z:|z|=\rho\}$, then

$$
\begin{aligned}
|L(f)|
&=\frac{1}{2\pi}\left|\int_0^{2\pi}f(\rho e^{it})g(\rho e^{it})i\rho e^{it}\,dt\right|\\
&\leq\frac{1}{2\pi}p_K(f)p_K(g)2\pi\rho.
\end{aligned}
$$

So if $c=\rho p_K(g)$, $|L(f)|\leq cp_K(f)$, and $L\in H(\mathbb D)^*$.

Now assume that $L\in H(\mathbb D)^*$. The Hahn–Banach Theorem implies there is an $F$ in $C(\mathbb D)^*$ such that $F|H(\mathbb D)=L$. By Proposition 4.1 there is a compact set $K$ contained in $\mathbb D$ and a measure $\mu$ on $K$ such that $L(f)=\int_K f\,d\mu$ for every $f$ in $H(\mathbb D)$. Define $g:\mathbb C_\infty\setminus K\to\mathbb C$ by $g(\infty)=0$ and $g(z)=-\int_K 1/(w-z)\,d\mu(w)$ for $z$ in $\mathbb C\setminus K$. By Lemma III.8.2, $g$ is analytic on $\mathbb C_\infty\setminus K$. Let $\rho<1$ such that $K\subseteq B(0;\rho)$. If $\gamma(t)=\rho e^{it}$, $0\leq t\leq2\pi$, then Cauchy’s Integral Formula implies

$$
f(w)=\frac{1}{2\pi i}\int_\gamma\frac{f(z)}{z-w}\,dz
$$

for $|w|<\rho$; in particular, this is true for $w$ in $K$. Thus,

$$
\begin{aligned}
L(f)
&=\int_K f(w)\,d\mu(w)\\
&=\int_K\left[\frac{\rho}{2\pi}\int_0^{2\pi}
\frac{f(\rho e^{it})}{\rho e^{it}-w}e^{it}\,dt\right]d\mu(w)\\
&=\frac{\rho}{2\pi}\int_0^{2\pi}f(\rho e^{it})e^{it}
\left[\int_K\frac{1}{\rho e^{it}-w}\,d\mu(w)\right]dt\\
&=\frac{1}{2\pi i}\int_\gamma f(z)g(z)\,dz.
\end{aligned}
$$

This completes the proof except for the uniqueness of $g$ (Exercise 3). $\blacksquare$

## Exercises

1. Let $\{\mathcal X_i:i\in I\}$ be a family of LCS’s and give $\mathcal X=\prod\{\mathcal X_i:i\in I\}$ the product topology. (See Exercise 1.17.) Show that $L\in\mathcal X^*$ if and only if there is a finite subset $F$ contained in $I$ and there are $x_j^*$ in $\mathcal X_j^*$ for $j$ in $F$ such that $L(x)=\sum_{j\in F}x_j^*(x(j))$ for each $x$ in $\mathcal X$.

2. Show that the space $s$ (Exercise 1.13) is linearly homeomorphic to $C(\mathbb N)$ and describe $s^*$.



<a id="pdf-page-131"></a>
3. Show that the function $g$ obtained in Proposition 4.2 is unique.

4. Show that $L\in H(\mathbb D)^*$ if and only if there are scalars $b_0,b_1,\ldots$ in $\mathbb C$ such that $\limsup |b_n|^{1/n}<1$ and $L(f)=\sum_{n=0}^{\infty}\frac{1}{n!}f^{(n)}(0)b_n$.

5. If $G$ is an annulus, describe $H(G)^*$.

6. (Buck [1958]). Let $X$ be locally compact and let $\beta$ be the strict topology on $C_b(X)$ defined in Exercise 1.21. (Also see Exercises 2.6 and 2.7.) Prove the following statements: (a) If $\mu\in M(X)$ and $\varepsilon_n\downarrow 0$, then there are compact sets $K_1,K_2,\ldots$ such that for each $n\geqslant 1$, $K_n\subseteq\operatorname{int}K_{n+1}$ and $|\mu|(X\setminus K_n)<\varepsilon_n$. (b) If $\mu\in M(X)$, then there is a $\phi$ in $C_0(X)$ such that $\phi\geqslant 0$, $|\mu|(X\setminus\{x:\phi(x)>0\})=0$, $1/\phi\in L^1(|\mu|)$, and $\int 1/\phi\,d|\mu|\leqslant 1$. (c) Show that if $\mu\in M(X)$ and $L(f)=\int f\,d\mu$ for $f$ in $C_b(X)$, then $L\in(C_b(X),\beta)^*$. (d) Conversely, if $L\in(C_b(X),\beta)^*$, then there is a $\mu$ in $M(X)$ such that $L(f)=\int f\,d\mu$ for $f$ in $C_b(X)$.

7. Let $X$ be completely regular and let $\mathcal M$ be a linear manifold in $C(X)$. Show that if for every compact subset $K$ of $X$, $\mathcal M|K\equiv\{f|K:f\in\mathcal M\}$ is dense in $C(K)$, then $\mathcal M$ is dense in $C(X)$.

## §5*. Inductive Limits and the Space of Distributions

In this section the most general definition of an inductive limit will not be presented. Rather one that removes certain technicalities from the arguments and yet covers the most important examples will be given. For the more general definition see Köthe [1969], Robertson and Robertson [1966], or Schaefer [1971].

**5.1. Definition.** An *inductive system* is a pair $(\mathcal X,\{\mathcal X_i:i\in I\})$, where $\mathcal X$ is a vector space, $\mathcal X_i$ is a linear manifold in $\mathcal X$ that has a topology $\mathcal T_i$ such that $(\mathcal X_i,\mathcal T_i)$ is a LCS, and, moreover:

(a) $I$ is a directed set and $\mathcal X_i\subseteq\mathcal X_j$ if $i\leqslant j$;

(b) if $i\leqslant j$ and $U_j\in\mathcal T_j$, then $U_j\cap\mathcal X_i\in\mathcal T_i$;

(c) $\mathcal X=\bigcup\{\mathcal X_i:i\in I\}$.

Note that condition (b) is equivalent to the condition that the inclusion map $\mathcal X_i\hookrightarrow\mathcal X_j$ is continuous.

**5.2. Example.** Let $d\geqslant 1$ and let $\Omega$ be an open subset of $\mathbb R^d$. Denote by $C_c^{(\infty)}(\Omega)$ all the functions $\phi:\Omega\to\mathbb F$ such that $\phi$ is infinitely differentiable and has compact support in $\Omega$. (The support of $\phi$ is defined by $\operatorname{spt}\phi\equiv\operatorname{cl}\{x:\phi(x)\ne 0\}$.) If $K$ is a compact subset of $\Omega$, define $\mathcal D(K)\equiv\{\phi\in C_c^{(\infty)}(\Omega):\operatorname{spt}\phi\subseteq K\}$. Let $\mathcal D(K)$ have the topology defined by the seminorms

$$
p_{K,m}(\phi)=\sup\{|\phi^{(k)}(x)|:|k|\leqslant m,\ x\in K\},
$$



<a id="pdf-page-132"></a>
§5. Inductive Limits and the Space of Distributions  117

where $k=(k_1,\ldots,k_d)$, $k_j\in\mathbb{N}\cup\{0\}$, $|k|=k_1+\cdots+k_d$, and

$$
\phi^{(k)}=\frac{\partial^{|k|}\phi}{\partial x_1^{k_1}\cdots\partial x_d^{k_d}}.
$$

Then $(C_c^{(\infty)}(\Omega),\{\mathcal{D}(K): K\text{ is compact in }\Omega\})$ is an inductive system. The space $C_c^{(\infty)}(\Omega)$ is often denoted in the literature by $\mathcal{D}(\Omega)$, as it will be in this book.

This example of an inductive system is the most important one as it is connected with the theory of distributions (below). In fact, this example was the inspiration for the definition of an inductive limit given now.

**5.3. Proposition.** *If $(\mathcal{X},\{\mathcal{X}_i,\mathcal{T}_i\})$ is an inductive system, let $\mathcal{B}=$ all convex balanced sets $V$ such that $V\cap\mathcal{X}_i\in\mathcal{T}_i$ for all $i$. Let $\mathcal{T}=$ the collection of all subsets $U$ of $\mathcal{X}$ such that for every $x_0$ in $U$ there is a $V$ in $\mathcal{B}$ with $x_0+V\subseteq U$. Then $(\mathcal{X},\mathcal{T})$ is a (not necessarily Hausdorff) LCS.*

Before proving this proposition, it seems appropriate to make the following definition.

**5.4. Definition.** If $(\mathcal{X},\{\mathcal{X}_i\})$ is an inductive system and $\mathcal{T}$ is the topology defined in (5.3), $\mathcal{T}$ is called the *inductive limit topology* and $(\mathcal{X},\mathcal{T})$ is said to be the inductive limit of $\{\mathcal{X}_i\}$.

**5.5. Lemma.** *With the notation as in (5.3), $\mathcal{B}\subseteq\mathcal{T}$.*

**PROOF.** Fix $V$ is $\mathcal{B}$. It will be shown that $V$ is absorbing at each of its points. Indeed, if $x_0\in V$ and $x\in\mathcal{X}$, then there is an $\mathcal{X}_i$ and an $\mathcal{X}_j$ such that $x_0\in\mathcal{X}_i$ and $x\in\mathcal{X}_j$. Since $I$ is directed, there is a $k$ in $I$ with $k\geq i,j$. Hence $x_0,x\in\mathcal{X}_k$. But $V\cap\mathcal{X}_k\in\mathcal{T}_k$. Thus there is an $\varepsilon>0$ such that $x_0+\alpha x\in V\cap\mathcal{X}_k\subseteq V$ for $|\alpha|<\varepsilon$.

Since $V$ is convex, balanced, and absorbing at each of its points, there is a seminorm $p$ on $\mathcal{X}$ such that $V=\{x\in\mathcal{X}:p(x)<1\}$ (1.14). So if $x_0\in V$, $p(x_0)=r_0<1$. Let $W=\{x\in\mathcal{X}:p(x)<\frac12(1-r_0)\}$. Then $W=\frac12(1-r_0)V$ and so $W\in\mathcal{B}$. Since $x_0+W\subseteq V$, $V\in\mathcal{T}$. ■

**PROOF OF PROPOSITION 5.3.** The proof that $\mathcal{T}$ is a topology is left as an exercise. To see that $(\mathcal{X},\mathcal{T})$ is a LCS, note that Lemma 5.5 and Theorem 1.14 imply that $\mathcal{T}$ is defined by a family of seminorms. ■

For all we know the inductive limit topology may be trivial. However, the fact that this topology has not been shown to be Hausdorff need not concern us, since we will concentrate on a particular type of inductive limit which will be shown to be Hausdorff. But for the moment we will continue at the present level of generality.

**5.6. Proposition.** *Let $(\mathcal{X},\{\mathcal{X}_i\})$ be an inductive system and let $\mathcal{T}$ be the inductive*



<a id="pdf-page-133"></a>
limit topology. Then

(a) the relative topology on $\mathcal X_i$ induced by $\mathcal T$ (viz., $\mathcal T|_{\mathcal X_i}$) is smaller than $\mathcal T_i$;

(b) if $\mathcal U$ is a locally convex topology on $\mathcal X$ such that for every $i$, $\mathcal U|_{\mathcal X_i}\subseteq\mathcal T_i$, then $\mathcal U\subseteq\mathcal T$;

(c) a seminorm $p$ on $\mathcal X$ is continuous if and only if $p|_{\mathcal X_i}$ is continuous for each $i$.

**Proof.** Exercise 3.

**5.7. Proposition.** Let $(\mathcal X,\mathcal T)$ be the inductive limit of the spaces $\{(\mathcal X_i,\mathcal T_i):i\in I\}$. If $\mathcal Y$ is a LCS and $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is continuous if and only if the restriction of $T$ to each $\mathcal X_i$ is $\mathcal T_i$-continuous.

**Proof.** Suppose $T:\mathcal X\to\mathcal Y$ is continuous. By (5.6a), the inclusion map $(\mathcal X_i,\mathcal T_i)\to(\mathcal X,\mathcal T)$ is continuous. Since the restriction of $T$ to $\mathcal X_i$ is the composition of the inclusion map $\mathcal X_i\to\mathcal X$ and $T$, the restriction is continuous.

Now assume that each restriction is continuous. If $p$ is a continuous seminorm on $\mathcal Y$, then $p\circ T|_{\mathcal X_i}$ is a $\mathcal T_i$-continuous seminorm for every $i$. By (5.6c), $p\circ T$ is continuous on $\mathcal X$. By Exercise 1.23, $T$ is continuous. ■

It may have occurred to the reader that the definition of the inductive limit topology depends on the choice of the spaces $\mathcal X_i$ in more than the obvious way. That is, if $\mathcal X=\bigcup_j\mathcal Y_j$ and each $\mathcal Y_j$ has a topology that is “compatible” with that of the spaces $\{\mathcal X_i\}$, perhaps the inductive limit topology defined by the spaces $\{\mathcal Y_j\}$ will differ from that defined by the $\{\mathcal X_i\}$. This is not the case.

**5.8. Proposition.** Let $(\mathcal X,\{(\mathcal X_i,\mathcal T_i)\})$ and $(\mathcal X,\{(\mathcal Y_j,\mathcal U_j)\})$ be two inductive systems and let $\mathcal T$ and $\mathcal U$ be the corresponding inductive limit topologies on $\mathcal X$. If for every $i$ there is a $j$ such that $\mathcal X_i\subseteq\mathcal Y_j$ and $\mathcal U_j|_{\mathcal X_i}\subseteq\mathcal T_i$, then $\mathcal U\subseteq\mathcal T$.

**Proof.** Let $V$ be a convex balanced subset of $\mathcal X$ such that for every $j$, $V\cap\mathcal Y_j\in\mathcal U_j$. If $\mathcal X_i$ is given, let $j$ be such that $\mathcal X_i\subseteq\mathcal Y_j$ and $\mathcal U_j|_{\mathcal X_i}\subseteq\mathcal T_i$. Hence $V\cap\mathcal X_i=(V\cap\mathcal Y_j)\cap\mathcal X_i\in\mathcal T_i$. Thus $V\in\mathcal B$ [as defined in (5.3)]. It now follows that $\mathcal U\subseteq\mathcal T$. ■

**5.9. Example.** Let $\mathcal X$ be any vector space and let $\{\mathcal X_i:i\in I\}$ be all of the finite dimensional subspaces of $\mathcal X$. Give each $\mathcal X_i$ the unique topology from its identification with a Euclidean space. Then $(\mathcal X,\{\mathcal X_i\})$ is an inductive system. Let $\mathcal T$ be the inductive limit topology. If $\mathcal Y$ is a LCS and $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is $\mathcal T$-continuous.

**5.10. Example.** Let $X$ be a locally compact space and let $\{K_i:i\in I\}$ be the collection of all compact subsets of $X$. Let $\mathcal X_i$ = all $f$ in $C(X)$ such that $\operatorname{spt}f\subseteq K_i$. Then $\bigcup_i\mathcal X_i=C_c(X)$, the continuous functions on $X$ with compact support. Topologize each $\mathcal X_i$ by giving it the supremum norm. Then $(C_c(X),\{\mathcal X_i\})$ is an inductive system.



<a id="pdf-page-134"></a>
Let $\{U_j\}$ be the open subsets of $X$ such that $\operatorname{cl} U_j$ is compact. Let $C_0(U_j)$ be the continuous functions on $U_j$ vanishing at $\infty$ with the supremum norm. If $f\in C_0(U_j)$ and $f$ is defined on $X$ by letting it be identically $0$ on $X\setminus U_j$, then $f\in C_c(X)$. Thus $(C_c(X),\{C_0(U_j)\})$ is an inductive system. Proposition 5.8 implies that these two inductive systems define the same inductive limit topology on $C_c(X)$.

**5.11. Example.** Let $d\geqslant 1$ and put $K_n=\{x\in\mathbb R^d:\|x\|\leqslant n\}$. Then $(\mathcal D(\mathbb R^d),\{\mathcal D(K_n)\}_{n=1}^{\infty})$ is an inductive system. By (5.9), the inductive limit topology defined on $\mathcal D(\mathbb R^d)$ by this system equals the inductive limit topology defined by the system given in Example 5.2.

If $\Omega$ is any subset of $\mathbb R^d$, then $\Omega$ can be written as the union of a sequence of compact subsets $\{K_n\}$ such that $K_n\subseteq\operatorname{int}K_{n+1}$. It follows by (5.9) that $\{\mathcal D(K_n)\}$ defines the same topology on $\mathcal D(\Omega)$ as was defined in Example 5.2.

The preceding example inspires the following definition.

**5.12. Definition.** A strict inductive system is an inductive system $(\mathcal X,\{\mathcal X_n,\mathcal T_n\}_{n=1}^{\infty})$ such that for every $n\geqslant 1$, $\mathcal X_n\subseteq\mathcal X_{n+1}$, $\mathcal T_{n+1}|_{\mathcal X_n}=\mathcal T_n$, and $\mathcal X_n$ is closed in $\mathcal X_{n+1}$. The inductive limit topology defined on $\mathcal X$ by such a system is called a *strict inductive limit topology* and $\mathcal X$ is said to be the *strict inductive limit* of $\{\mathcal X_n\}$.

Example 5.11 shows that $\mathcal D(\mathbb R^d)$, indeed $\mathcal D(\Omega)$, is a strict inductive limit. The following lemma is useful in the study of strict inductive limits as well as in other situations.

**5.13. Proposition.** *If $\mathcal X$ is a LCS, $\mathcal Y\leqslant\mathcal X$, and $p$ is a continuous seminorm on $\mathcal Y$, then there is a continuous seminorm $\tilde p$ on $\mathcal X$ such that $\tilde p|_{\mathcal Y}=p$.*

**Proof.** Let $U=\{y\in\mathcal Y:p(y)<1\}$. So $U$ is open in $\mathcal Y$; hence there is an open subset $V_1$ of $\mathcal X$ such that $V_1\cap\mathcal Y=U$. Since $0\in V_1$ and $\mathcal X$ is a LCS, there is an open convex balanced set $V$ in $\mathcal X$ such that $V\subseteq V_1$. Let $q=$ the gauge of $V$. So if $y\in\mathcal Y$ and $q(y)<1$, then $p(y)<1$. By Lemma III.1.4, $p\leqslant q|_{\mathcal Y}$.

Let $W=\operatorname{co}(U\cup V)$; it is easy to see that $W$ is convex and balanced since both $U$ and $V$ are. It will be shown that $W$ is open. First observe that $W=\{tu+(1-t)v:0\leqslant t\leqslant 1,\ u\in U,\ v\in V\}$ (verify). Hence $W=\bigcup\{tU+(1-t)V:0\leqslant t\leqslant 1\}$. Put $W_t=tU+(1-t)V$. So $W_0=V$, which is open. If $0<t<1$, $W_t=\bigcup\{tu+(1-t)V:u\in U\}$, and hence is open. But $W_1=U$, which is not open. However, if $u\in U$, then there is an $\varepsilon>0$ such that $\varepsilon u\in V$. For $0<t<1$, let $y_t=t^{-1}[1-\varepsilon+t\varepsilon]u$ $(\in\mathcal Y)$. As $t\to 1$, $y_t\to u$. Since $U$ is open in $\mathcal Y$, there is a $t$, $0<t<1$, with $y_t$ in $U$. Thus $u=ty_t+(1-t)(\varepsilon u)\in W_t$. Therefore $W=\bigcup\{W_t:0\leqslant t<1\}$ and $W$ is open.

**5.14. Claim.** $W\cap\mathcal Y=U$.



<a id="pdf-page-135"></a>
In fact, $U\subseteq W$, so $U\subset W\cap\mathcal Y$. If $w\in W\cap\mathcal Y$, then $w=tu+(1-t)v$, $u$ in $U$, $v$ in $V$, $0\leq t\leq1$; it may be assumed that $0<t<1$. (Why?) Hence, $v=(1-t)^{-1}(w-tu)\in\mathcal Y$. So $v\in V\cap\mathcal Y\subseteq U$; hence $w\in U$.

Let $\tilde p=$ the gauge of $W$. By Claim 5.14, $\{y\in\mathcal Y:\tilde p(y)<1\}=\{y\in\mathcal Y:p(y)<1\}$. By the uniqueness of the gauge, $\tilde p|_{\mathcal Y}=p$. ■

**5.15. Corollary.** *If $\mathcal X$ is the strict inductive limit of $\{\mathcal X_n\}$, $k$ is fixed, and $p_k$ is a continuous seminorm on $\mathcal X_k$, then there is a continuous seminorm $p$ on $\mathcal X$ such that $p|_{\mathcal X_k}=p_k$. In particular, the inductive limit topology is Hausdorff and the topology on $\mathcal X$ when restricted to $\mathcal X_k$ equals the original topology of $\mathcal X_k$.*

**Proof.** By (5.13) and induction, for every integer $n>k$, there is a continuous seminorm $p_n$ such that $p_n|_{\mathcal X_{n-1}}=p_{n-1}$. If $x\in\mathcal X$, define $p(x)=p_n(x)$ when $x\in\mathcal X_n$. Since $\mathcal X_n\subseteq\mathcal X_{n+1}$ for all $n$, the properties of $\{p_n\}$ insure that $p$ is well defined. Clearly $p$ is a seminorm and by (5.6c) $p$ is continuous.

If $x\in\mathcal X$ and $x\ne0$, there is a $k\geq1$ such that $x\in\mathcal X_k$. Thus there is a continuous seminorm $p_k$ on $\mathcal X_k$ such that $p_k(x)\ne0$. Using the first part of the corollary, we get a continuous seminorm $p$ on $\mathcal X$ such that $p(x)\ne0$. Thus $(\mathcal X,\mathcal T)$ is Hausdorff. The proof that the topology on $\mathcal X$ when relativized to $\mathcal X_k$ equals the original topology is an easy application of (5.13). ■

**5.16. Proposition.** *Let $\mathcal X$ be the strict inductive limit of $\{\mathcal X_n\}$. A subset $B$ of $\mathcal X$ is bounded if and only if there is an $n\geq1$ such that $B\subseteq\mathcal X_n$ and $B$ is bounded in $\mathcal X_n$.*

The proof will be accomplished only after a few preliminaries are settled. Before doing this, here are a few consequences of (5.16).

**5.17. Corollary.** *If $\mathcal X$ is the strict inductive limit of $\{\mathcal X_n\}$, then a subset $K$ of $\mathcal X$ is compact if and only if there is an $n\geq1$ such that $K\subseteq\mathcal X_n$ and $K$ is compact in $\mathcal X_n$.*

**5.18. Corollary.** *If $\mathcal X$ is the strict inductive limit of Fréchet spaces $\{\mathcal X_n\}$, $\mathcal Y$ is a LCS, and $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is continuous if and only if $T$ is sequentially continuous.*

**Proof.** By Proposition 5.7, $T$ is continuous if and only if $T|_{\mathcal X_n}$ is continuous for every $n$. Since each $\mathcal X_n$ is metrizable, the result follows. ■

Note that using Example 5.11 it follows that for an open subset $\Omega$ of $\mathbf R^d$, $\mathcal D(\Omega)$ is the strict inductive limit of Fréchet spaces [each $\mathcal D(K_n)$ is a Fréchet space by Proposition 2.1]. So (5.18) applies.

**5.19. Definition.** If $\Omega$ is an open subset of $\mathbf R^d$, a *distribution* on $\Omega$ is a continuous linear functional on $\mathcal D(\Omega)$.



<a id="pdf-page-136"></a>
Distributions are, in a certain sense, generalizations of the concept of function as the following example illustrates.

**5.20. Example.** Let $f$ be a Lebesgue measurable function on $\Omega$ that is locally integrable (that is, $\int_K |f|\,d\lambda<\infty$ for every compact subset $K$ of $\Omega$—here $\lambda$ is $d$-dimensional Lebesgue measure). If $L_f:\mathcal D(\Omega)\to\mathbb F$ is defined by $L_f(\phi)=\int f\phi\,d\lambda$, $L_f$ is a distribution.

From Corollary 5.18 we arrive at the following.

**5.21. Proposition.** *A linear functional $L:\mathcal D(\Omega)\to\mathbb F$ is a distribution if and only if for every sequence $\{\phi_n\}$ in $\mathcal D(\Omega)$ such that $\operatorname{cl}\!\left[\bigcup_{n=1}^{\infty}\operatorname{spt}\phi_n\right]=K$ is compact in $\Omega$ and $\phi_n^{(k)}(x)\to0$ uniformly on $K$ as $n\to\infty$ for every $k=(k_1,\ldots,k_d)$, it follows that $L(\phi_n)\to0$.*

Proposition 5.21 is usually taken as the definition of a distribution in books on differential equations. There is the advantage that (5.21) can be understood with no knowledge of locally convex spaces and inductive limits. Moreover, most theorems on distributions can be proved by using (5.21). However, the realization that a distribution is precisely a continuous linear functional on a LCS contributes more than cultural edification. This knowledge brings power as it enables you to apply the theory of LCS’s (including the Hahn-Banach Theorem).

The exercises contain more results on distributions, but now we must return to the proof of Proposition 5.16. To do this the idea of a topological complement is needed. We have seen this idea in Section III.13.

**5.22. Proposition.** *If $\mathcal X$ is a TVS and $\mathcal Y\leq\mathcal X$, the following statements are equivalent.*

(a) *There is a closed linear subspace $\mathcal Z$ of $\mathcal X$ such that $\mathcal Y\cap\mathcal Z=(0)$, $\mathcal Y+\mathcal Z=\mathcal X$, and the map of $\mathcal Y\times\mathcal Z\to\mathcal X$ given by $(y,z)\mapsto y+z$ is a homeomorphism.*

(b) *There is a continuous linear map $P:\mathcal X\to\mathcal X$ such that $P\mathcal X=\mathcal Y$ and $P^2=P$.*

**Proof.** (a) $\Rightarrow$ (b): Define $P:\mathcal X\to\mathcal X$ by $P(y+z)=y$, for $y$ in $\mathcal Y$ and $z$ in $\mathcal Z$. It is easy to verify that $P$ is linear and $P\mathcal X=\mathcal Y$. Also, $P^2(y+z)=PP(y+z)=Py=y=P(y+z)$; so $P^2=P$. If $\{y_i+z_i\}$ is a net in $\mathcal X$ such that $y_i+z_i\to y+z$, then (a) implies that $y_i\to y$ (and $z_i\to z$). Hence $P(y_i+z_i)\to P(y+z)$ and $P$ is continuous.

(b) $\Rightarrow$ (a): If $P$ is given, let $\mathcal Z=\ker P$. So $\mathcal Z\leq\mathcal X$. Also, $x=Px+(x-Px)$ and $y=Px\in\mathcal Y$, and $z=x-Px$ has $Pz=Px-P^2x=Px-Px=0$, so $z\in\mathcal Z$. Thus, $\mathcal Y+\mathcal Z=\mathcal X$. If $x\in\mathcal Y\cap\mathcal Z$, then $Px=0$ since $x\in\mathcal Z$; but also $x=Pw$ for some $w$ in $\mathcal X$ since $x\in\mathcal Y=P\mathcal X$. Therefore $0=Px=P^2w=Pw=x$; that is, $\mathcal Y\cap\mathcal Z=(0)$. Now suppose that $\{y_i\}$ and $\{z_i\}$ are nets in $\mathcal Y$ and $\mathcal Z$. If $y_i\to y$ and $z_i\to z$, then $y_i+z_i\to y+z$ because addition is continuous. If, on the other



<a id="pdf-page-137"></a>
hand, it is assumed that $y_i+z_i\to y+z$, then $y=P(y+z)=\lim P(y_i+z_i)=\lim y_i$ and $z_i=(y_i+z_i)-y_i\to z$. This proves (a). $\blacksquare$

**5.23. Definition.** If $\mathcal X$ is a TVS and $\mathcal Y\leq\mathcal X$, $\mathcal Y$ is *topologically complemented* in $\mathcal X$ if either (a) or (b) of (5.22) is satisfied.

**5.24. Proposition.** *If $\mathcal X$ is a LCS and $\mathcal Y\leq\mathcal X$ such that either $\dim\mathcal Y<\infty$ or $\dim\mathcal X/\mathcal Y<\infty$, then $\mathcal Y$ is topologically complemented in $\mathcal X$.*

**Proof.** The proof will only be sketched. The reader is asked to supply the details (Exercise 9).

(a) Suppose $d=\dim\mathcal Y<\infty$ and let $y_1,\ldots,y_d$ be a basis for $\mathcal Y$. By the Hahn–Banach Theorem (III.6.6), there are $f_1,\ldots,f_d$ in $\mathcal X^*$ such that $f_i(y_j)=1$ if $i=j$ and $0$ otherwise. Define $Px=\sum_{j=1}^d f_j(x)y_j$.

(b) Suppose $d=\dim\mathcal X/\mathcal Y<\infty$, $Q:\mathcal X\to\mathcal X/\mathcal Y$ is the natural map, and $z_1,\ldots,z_d\in\mathcal X$ such that $Q(z_1),\ldots,Q(z_d)$ is a basis for $\mathcal X/\mathcal Y$. Let $\mathcal Z=\vee\{z_1,\ldots,z_d\}$. $\blacksquare$

**Proof of Proposition 5.16.** Suppose $\mathcal X$ is the strict inductive limit of $\{(\mathcal X_n,\mathcal T_n)\}$ and $B$ is a bounded subset of $\mathcal X$. It must be shown that there is an $n$ such that $B\subseteq\mathcal X_n$ (the rest of the proof is easy). Suppose this is not the case. By replacing $\{\mathcal X_n\}$ by a subsequence if necessary, it follows that for each $n$ there is an $x_n$ in $(B\cap\mathcal X_{n+1})\setminus\mathcal X_n$. Let $p_1$ be a continuous seminorm on $\mathcal X_1$ such that $p_1(x_1)=1$.

**5.25. Claim.** For every $n\geq2$ there is a continuous seminorm $p_n$ on $\mathcal X_n$ such that $p_n(x_n)=n$ and $p_n|_{\mathcal X_{n-1}}=p_{n-1}$.

The proof of (5.25) is by induction. Suppose $p_n$ is given and let $\mathcal Y=\mathcal X_n\vee\{x_{n+1}\}$. By (5.24), $\mathcal X_n$ and $\vee\{x_{n+1}\}$ are topologically complementary in $\mathcal Y$. Define $q:\mathcal Y\to[0,\infty)$ by $q(x+\alpha x_{n+1})=p_n(x)+(n+1)|\alpha|$, where $x\in\mathcal X_n$ and $\alpha\in\mathbb F$. Then $q$ is a continuous seminorm on $(\mathcal Y,\mathcal T_{n+1}|_{\mathcal Y})$. (Verify!) By Proposition 5.13 there is a continuous seminorm $p_{n+1}$ on $\mathcal X_{n+1}$ such that $p_{n+1}|_{\mathcal Y}=q$. Thus $p_{n+1}|_{\mathcal X_n}=p_n$ and $p_{n+1}(x_{n+1})=n+1$. This proves the claim.

Now define $p:\mathcal X\to[0,\infty)$ by $p(x)=p_n(x)$ if $x\in\mathcal X_n$. By (5.25), $p$ is well defined. It is easy to see that $p$ is a continuous seminorm. However, $\sup\{p(x):x\in B\}=\infty$, so $B$ is not bounded (Exercise 2.4f). $\blacksquare$

## Exercises

1. Verify the statements made in Example 5.2.
2. Fill in the details of the proof of Proposition 5.3.
3. Prove Proposition 5.6.
4. Verify the statements made in Example 5.9.
5. Verify the statements made in Example 5.10.



<a id="pdf-page-138"></a>
6. Verify the statements made in Example 5.11.

7. With the notation of (5.10), show that if $X$ is $\sigma$-compact, then the dual of $C_c(X)$ is the space of all extended $\mathbb{F}$-valued measures.

8. Is the inductive limit topology on $C_c(X)$ (5.10) different from the topology of uniform convergence on compact subsets of $X$ (1.5)?

9. Prove Proposition 5.24.

10. Verify the statements made in Example 5.20.

For the remaining exercises, $\Omega$ is always an open subset of $\mathbb{R}^d$, $d\geq 1$.

11. If $\mu$ is a measure on $\Omega$, $\phi\mapsto\int\phi\,d\mu$ is a distribution $\Omega$.

12. Let $f:\Omega\to\mathbb{F}$ be a function with continuous partial derivatives and let $L_f$ be defined as in (5.20). Show that for every $\phi$ in $\mathcal{D}(\Omega)$ and $1\leq j\leq d$, $L_f(\partial\phi/\partial x_j)=-L_g(\phi)$, where $g=\partial f/\partial x_j$. (Hint: Use integration by parts.)

13. Exercise 12 motivates the following definition. If $L$ is a distribution on $\Omega$, define $\partial L/\partial x_j:\mathcal{D}(\Omega)\to\mathbb{F}$ by $\partial L/\partial x_j(\phi)=-L(\partial\phi/\partial x_j)$ for all $\phi$ in $\mathcal{D}(\Omega)$. Show that $\partial L/\partial x_j$ is a distribution.

14. Using Example 5.20 and Exercise 13, one is justified to talk of the derivative of any locally integrable function as a *distribution*. By Exercise 11 we can differentiate measures. Let $f:\mathbb{R}\to\mathbb{R}$ be the characteristic function of $[0,\infty)$ and show that its derivative as a distribution is $\delta_0$, the unit point mass at 0. [That is, $\delta_0$ is the measure such that $\delta_0(\Delta)=1$ if $0\in\Delta$ and $\delta_0(\Delta)=0$ if $0\notin\Delta$.]

15. Let $f$ be an absolutely continuous function on $\mathbb{R}$ and show that $(L_f)'=L_{f'}$.

16. Let $f$ be a left continuous nondecreasing function on $\mathbb{R}$ and show that $(L_f)'$ is the distribution defined by the measure $\mu$ such that $\mu[a,b)=f(b)-f(a)$ for all $a<b$.

17. Let $f$ be a $C^\infty$ function on $\Omega$ and let $L$ be a distribution on $\mathcal{D}(\Omega)$. Show that $M(\phi)\equiv L(\phi f)$, $\phi$ in $\mathcal{D}(\Omega)$, is a distribution. State and prove a product rule for finding the derivative of $M$.

