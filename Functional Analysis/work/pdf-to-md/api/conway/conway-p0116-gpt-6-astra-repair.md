§1. Elementary Properties and Examples　　　　　　　　　　　　　　　　　101

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
