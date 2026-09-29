If $X$ is a compact space $\mathcal{X}=C(X)$, then any non-zero constant function is an order unit. ($f\leq g$ if and only if $f(x)\leq g(x)$ for all $x$.) If $\mathcal{X}=C(\mathbb{R})$, all real-valued continuous functions on $\mathbb{R}$, then $\mathcal{X}$ has no order unit (Exercise 4). If $e$ is an order unit, then $\{ne:n\geq 1\}$ is cofinal.

**9.7. Definition.** If $(\mathcal{X},\leq)$ and $(\mathcal{Y},\leq)$ are ordered vector spaces and $T:\mathcal{X}\to\mathcal{Y}$ is a linear map, then $T$ is *positive* (in symbols $T\geq 0$) if $Tx\geq 0$ whenever $x\geq 0$.

The principal result of this section is the following.

**9.8. Theorem.** *Let $(\mathcal{X},\leq)$ be an ordered vector space and let $\mathcal{Y}$ be a linear manifold in $\mathcal{X}$ that is cofinal. If $f:\mathcal{Y}\to\mathbb{R}$ is a positive linear functional, then there is a positive linear functional $\tilde f:\mathcal{X}\to\mathbb{R}$ such that $\tilde f|_{\mathcal{Y}}=f$.*

**Proof.** Let $P=\{x\in\mathcal{X}:x\geq 0\}$ and put $\mathcal{X}_1=\mathcal{Y}+P-P$. It is easy to see that $\mathcal{X}_1$ is a linear manifold in $\mathcal{X}$. If there is a positive linear functional $g:\mathcal{X}_1\to\mathbb{R}$ that extends $f$, let $\tilde f$ be any linear functional on $\mathcal{X}$ that extends $g$ (use a Hamel basis). If $x\geq 0$, then $x\in P\subseteq\mathcal{X}_1$ so that $\tilde f(x)=g(x)\geq 0$. Hence $\tilde f$ is positive. Thus, we may assume that $\mathcal{X}=\mathcal{Y}+P-P$.

**9.9. Claim.** $\mathcal{X}=\mathcal{Y}+P=\mathcal{Y}-P$.

Let $x\in\mathcal{X}$; so $x=y+p_1-p_2$, $y$ in $\mathcal{Y}$, $p_1,p_2$ in $P$. Since $\mathcal{Y}$ is cofinal there is a $y_1$ in $\mathcal{Y}$ such that $y_1\geq p_1$. Hence $p_1=y_1-(y_1-p_1)\in\mathcal{Y}-P$. Thus $x=y-p_2+p_1\in(\mathcal{Y}-P)+(\mathcal{Y}-P)\subseteq\mathcal{Y}-P$. So $\mathcal{X}=\mathcal{Y}-P$. Also, $\mathcal{X}=-\mathcal{X}=-\mathcal{Y}+P=\mathcal{Y}+P$.

**9.10. Claim.** If $x\in\mathcal{X}$, there are $y_1,y_2$ in $\mathcal{Y}$ such that $y_2\leq x\leq y_1$.

In fact, Claim 9.9 states that we can write $x=y_1-p_1=y_2+p_2$, $p_1,p_2\in P$ and $y_1,y_2\in\mathcal{Y}$. Thus $y_2\leq x\leq y_1$.

By Claim 9.10, it is possible to define for each $x$ in $\mathcal{X}$,

$$
q(x)=\inf\{f(y):y\in\mathcal{Y}\text{ and }y\geq x\}.
$$

**9.11. Claim.** The function $q$ is a sublinear functional on $\mathcal{X}$.

The proof of (9.11) is left as an exercise.

For $y$ in $\mathcal{Y}$, let $y_1\in\mathcal{Y}$ such that $y_1\geq y$. Because $f$ is positive, $f(y)\leq f(y_1)$. Hence $f(y)\leq q(y)$ for all $y$ in $\mathcal{Y}$. The Hahn–Banach Theorem implies that there is a linear functional $\tilde f:\mathcal{X}\to\mathbb{R}$ such that $\tilde f|_{\mathcal{Y}}=f$ and $\tilde f\leq q$ on $\mathcal{X}$. If $x\in P$, then $-x\leq 0$ (and $0\in\mathcal{Y}$). Hence $q(-x)\leq f(0)$. Thus $-\tilde f(x)=\tilde f(-x)\leq q(-x)\leq 0$, or $\tilde f(x)\geq 0$. Therefore $\tilde f$ is positive. ■

**9.12. Corollary.** *Let $(\mathcal{X},\leq)$ be an ordered vector space with an order unit $e$. If $\mathcal{Y}$ is a linear manifold in $\mathcal{X}$ and $e\in\mathcal{Y}$, then any positive linear functional defined on $\mathcal{Y}$ has an extension to a positive linear functional defined on $\mathcal{X}$.*
