last statement requires a bit of proof. Let $f\in L^1[0,1]$ such that $\|f\|_1=1$. Choose $x$ in $[0,1]$ such that $\int_0^x |f(t)|\,dt=\frac12$. Let $h(t)=2f(t)$ if $t\leq x$ and $0$ otherwise; let $g(t)=2f(t)$ if $t\geq x$ and $0$ otherwise. Then $\|h\|_1=\|g\|_1=1$ and $f=\frac12(h+g)$. So ball $L^1[0,1]$ has no extreme points.

The next proposition is left as an exercise.

**7.3. Proposition.** If $K$ is a convex subset of a vector space $\mathcal X$ and $a\in K$, then the following statements are equivalent.

(a) $a\in\operatorname{ext}K$.

(b) If $x_1,x_2\in\mathcal X$ and $a=\frac12(x_1+x_2)$, then either $x_1\notin K$ or $x_2\notin K$ or $x_1=x_2=a$.

(c) If $x_1,x_2\in\mathcal X$, $0<t<1$, and $a=tx_1+(1-t)x_2$, then either $x_1\notin K$, $x_2\notin K$, or $x_1=x_2=a$.

(d) If $x_1,\ldots,x_n\in K$ and $a\in\operatorname{co}\{x_1,\ldots,x_n\}$, then $a=x_k$ for some $k$.

(e) $K\setminus\{a\}$ is a convex set.

**7.4. The Krein–Milman Theorem.** If $K$ is a nonempty compact convex subset of a LCS $\mathcal X$, then $\operatorname{ext}K\neq\square$ and $K=\overline{\operatorname{co}}(\operatorname{ext}K)$.

**Proof.** (Léger [1968].) Note that (7.3e) says that a point $a$ is an extreme point if and only if $K\setminus\{a\}$ is a relatively open convex subset. We thus look for a maximal proper relatively open convex subset of $K$. Let $\mathcal U$ be all the proper relatively open convex subsets of $K$. Since $\mathcal X$ is a LCS and $K\neq\square$ (and let’s assume that $K$ is not a singleton), $\mathcal U\neq\square$. Let $\mathcal U_0$ be a chain in $\mathcal U$ and put $U_0=\bigcup\{U:U\in\mathcal U_0\}$. Clearly $U_0$ is open, and since $\mathcal U_0$ is a chain, $U_0$ is convex. If $U_0=K$, then the compactness of $K$ implies that there is a $U$ in $\mathcal U_0$ with $U=K$, a contradiction to the property of $\mathcal U$. Thus $U_0\in\mathcal U$. By Zorn’s Lemma, $\mathcal U$ has a maximal element $U$.

If $x\in K$ and $0\leq\lambda\leq1$, let $T_{x,\lambda}:K\to K$ be defined by $T_{x,\lambda}(y)=\lambda y+(1-\lambda)x$. Note that $T_{x,\lambda}$ is continuous and $T_{x,\lambda}\bigl(\sum_{j=1}^n\alpha_jy_j\bigr)=\sum_{j=1}^n\alpha_jT_{x,\lambda}(y_j)$ whenever $y_1,\ldots,y_n\in K$, $\alpha_1,\ldots,\alpha_n\geq0$, and $\sum_{j=1}^n\alpha_j=1$. (This means that $T_{x,\lambda}$ is an affine map of $K$ into $K$.) If $x\in U$ and $0\leq\lambda<1$, then $T_{x,\lambda}(U)\subseteq U$. Thus $U\subseteq T_{x,\lambda}^{-1}(U)$ and $T_{x,\lambda}^{-1}(U)$ is an open convex subset of $K$. If $y\in(\operatorname{cl}U)\setminus U$, $T_{x,\lambda}(y)\in[x,y)\subseteq U$ by Proposition IV.1.11. So $\operatorname{cl}U\subseteq T_{x,\lambda}^{-1}(U)$ and hence the maximality of $U$ implies $T_{x,\lambda}^{-1}(U)=K$. That is,

$$
T_{x,\lambda}(K)\subseteq U
\quad\text{if}\quad x\in U
\quad\text{and}\quad 0\leq\lambda<1.
\tag{7.5}
$$

**Claim.** If $V$ is any open convex subset of $K$, then either $V\cup U=U$ or $V\cup U=K$.

In fact, (7.5) implies that $V\cup U$ is convex so that the claim follows from the maximality of $U$.

It now follows from the claim that $K\setminus U$ is a singleton. In fact, if $a,b\in K\setminus U$ and $a\neq b$, let $V_a,V_b$ be disjoint open convex subsets of $K$ such that $a\in V_a$
