$|f(x)|\leqslant p(x)$ for all $x$ in $\mathcal M$, then there is a linear functional $F:\mathcal X\to\mathbb F$ such that $F|_{\mathcal M}=f$ and $|F(x)|\leqslant p(x)$ for all $x$ in $\mathcal X$.

**Proof.** *Case 1: $\mathbb F=\mathbb R$.* Note that $f(x)\leqslant |f(x)|\leqslant p(x)$ for $x$ in $\mathcal M$. By (6.2) there is an extension $F:\mathcal X\to\mathbb R$ of $f$ such that $F(x)\leqslant p(x)$ for all $x$. Hence $-F(x)=F(-x)\leqslant p(-x)=p(x)$. Thus $|F|\leqslant p$.

*Case 2: $\mathbb F=\mathbb C$.* Let $f_1=\operatorname{Re}f$. By (6.3c), $|f_1|\leqslant p$. By Case 1, there is an $\mathbb R$-linear functional $F_1:\mathcal X\to\mathbb R$ such that $F_1|_{\mathcal M}=f_1$ and $|F_1|\leqslant p$. Let $F(x)=F_1(x)-iF_1(ix)$ for all $x$ in $\mathcal X$. By (6.3c), $|F|\leqslant p$. Clearly, $F|_{\mathcal M}=f$. $\blacksquare$

**6.5. Corollary.** *If $\mathcal X$ is a normed space, $\mathcal M$ is a linear manifold in $\mathcal X$, and $f:\mathcal M\to\mathbb F$ is a bounded linear functional, then there is an $F$ in $\mathcal X^*$ such that $F|_{\mathcal M}=f$ and $\|F\|=\|f\|$.*

**Proof.** Use Corollary 6.4 with $p(x)=\|f\|\|x\|$. $\blacksquare$

**6.6. Corollary.** *If $\mathcal X$ is a normed space, $\{x_1,x_2,\ldots,x_d\}$ is a linearly independent subset of $\mathcal X$, and $\alpha_1,\alpha_2,\ldots,\alpha_d$ are arbitrary scalars, then there is an $f$ in $\mathcal X^*$ such that $f(x_j)=\alpha_j$ for $1\leqslant j\leqslant d$.*

**Proof.** Let $\mathcal M=$ the linear span of $x_1,\ldots,x_d$ and define $g:\mathcal M\to\mathbb F$ by $g(\sum_j\beta_jx_j)=\sum_j\beta_j\alpha_j$. So $g$ is linear. Since $\mathcal M$ is finite dimensional, $g$ is continuous. Let $f$ be a continuous extension of $g$ to $\mathcal X$. $\blacksquare$

**6.7. Corollary.** *If $\mathcal X$ is a normed space and $x\in\mathcal X$, then*

$$
\|x\|=\sup\{|f(x)|:f\in\mathcal X^*\text{ and }\|f\|\leqslant 1\}.
$$

*Moreover, this supremum is attained.*

**Proof.** Let $\alpha=\sup\{|f(x)|:f\in\mathcal X^*\text{ and }\|f\|\leqslant 1\}$. If $f\in\mathcal X^*$ and $\|f\|\leqslant 1$, then $|f(x)|\leqslant\|f\|\|x\|\leqslant\|x\|$; hence $\alpha\leqslant\|x\|$. Now let $\mathcal M=\{\beta x:\beta\in\mathbb F\}$, define $g:\mathcal M\to\mathbb F$ by $g(\beta x)=\beta\|x\|$. Then $g\in\mathcal M^*$ and $\|g\|=1$. By Corollary 6.5, there is an $f$ in $\mathcal X^*$ such that $\|f\|=1$ and $f(x)=g(x)=\|x\|$. $\blacksquare$

This introduces a certain symmetry in the definitions of the norms in $\mathcal X$ and $\mathcal X^*$ that will be explored later (§11).

**6.8. Corollary.** *If $\mathcal X$ is a normed space, $\mathcal M\leqslant\mathcal X$, $x_0\in\mathcal X\setminus\mathcal M$, and $d=\operatorname{dist}(x_0,\mathcal M)$, then there is an $f$ in $\mathcal X^*$ such that $f(x_0)=1$, $f(x)=0$ for all $x$ in $\mathcal M$, and $\|f\|=d^{-1}$.*

**Proof.** Let $Q:\mathcal X\to\mathcal X/\mathcal M$ be the natural map. Since $\|x_0+\mathcal M\|=d$, by the preceding corollary there is a $g$ in $(\mathcal X/\mathcal M)^*$ such that $g(x_0+\mathcal M)=d$ and $\|g\|=1$. Let $f=d^{-1}g\circ Q:\mathcal X\to\mathbb F$. Then $f$ is continuous, $f(x)=0$ for $x$ in $\mathcal M$, and $f(x_0)=1$. Also, $|f(x)|=d^{-1}|g(Q(x))|\leqslant d^{-1}\|Q(x)\|\leqslant d^{-1}\|x\|$; hence $\|f\|\leqslant d^{-1}$. On the other hand, $\|g\|=1$ so there is a sequence $\{x_n\}$ such
