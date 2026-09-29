14. Give an example of a TVS $\mathcal X$ that is not locally convex and a subspace $\mathcal Y$ of $\mathcal X$ such that there is a continuous linear functional $f$ on $\mathcal Y$ with no continuous extension to $\mathcal X$.

15. Let $\mathcal X$ be a real LCS and let $A$ and $B$ be disjoint compact convex subsets of $\mathcal X$. Suppose $\mathcal Y$ is a subspace of $\mathcal X$ and $f_0:\mathcal Y\to\mathbb R$ is a continuous linear functional such that $f_0(a)<0$ for $a$ in $A\cap\mathcal Y$ and $f_0(b)>0$ for $b$ in $B\cap\mathcal Y$. Show by an example that it is not always possible to extend $f_0$ to a continuous linear functional on $\mathcal X$ such that $f(a)<0$ or $a$ in $A$ and $f(b)>0$ for $b$ in $B$. (Hint: Let $\mathcal X=\mathbb R^3$ and let $\mathcal Y$ be the plane.)

## §4*. Some Examples of the Dual Space of a Locally Convex Space

As with a normed space, if $\mathcal X$ is a LCS, $\mathcal X^*$ denotes the space of all continuous linear functionals $f:\mathcal X\to\mathbb F$. $\mathcal X^*$ is called the *dual space* of $\mathcal X$.

**4.1. Proposition.** *Let $X$ be completely regular and let $C(X)$ be topologized as in Example 1.5. If $L:C(X)\to\mathbb F$ is a continuous linear functional, then there is a compact set $K$ and a regular Borel measure $\mu$ on $K$ such that $L(f)=\int_K f\,d\mu$ for every $f$ in $C(X)$. Conversely, each such measure defines an element of $C(X)^*$.*

**Proof.** It is easy to see that each measure $\mu$ supported on a compact set $K$ defines an element of $C(X)^*$. In fact, if $p_K(f)=\sup\{|f(x)|:x\in K\}$ and $L(f)=\int_K f\,d\mu$, then $|L(f)|\leq\|\mu\|p_K(f)$, and so $L$ is continuous.

Now assume $L\in C(X)^*$. There are compact sets $K_1,\ldots,K_n$ and positive numbers $\alpha_1,\ldots,\alpha_n$ such that $|L(f)|\leq\sum_{j=1}^n\alpha_jp_{K_j}(f)$ (3.1f). Let $K=\bigcup_{j=1}^nK_j$ and $\alpha=\max\{\alpha_j:1\leq j\leq n\}$. Then $|L(f)|\leq\alpha p_K(f)$. Hence if $f\in C(X)$ and $f|K\equiv0$, then $L(f)=0$.

Define $F:C(K)\to\mathbb F$ as follows. If $g\in C(K)$, let $\tilde g$ be any continuous extension of $g$ to $X$ and put $F(g)=L(\tilde g)$. To check that $F$ is well defined, suppose that $\tilde g_1$ and $\tilde g_2$ are both extensions of $g$ to $X$. Then $\tilde g_1-\tilde g_2=0$ on $K$, and hence $L(\tilde g_1)=L(\tilde g_2)$. Thus $F$ is well defined. It is left as an exercise for the reader to show that $F:C(K)\to\mathbb F$ is linear. If $g\in C(K)$ and $\tilde g$ is an extension in $C(X)$, then $|F(g)|=|L(\tilde g)|\leq\alpha p_K(\tilde g)=\alpha\|g\|$, where the norm is the norm of $C(K)$. By (III.5.7) there is a measure $\mu$ in $M(K)$ such that $F(g)=\int_K g\,d\mu$. If $f\in C(X)$, then $g=f|K\in C(K)$ and so $L(f)=F(g)=\int_K f\,d\mu$. ■

If $\gamma:[0,1]\to\mathbb C$ is a rectifiable curve and $f$ is a continuous function defined on the trace of $\gamma$, $\gamma([0,1])$, then $\int_\gamma f$ is the line integral of $f$ over $\gamma$. That is, $\int_\gamma f=\int_0^1 f(\gamma(t))\,d\gamma(t)$. (See Conway [1978].) The next result generalizes to arbitrary regions in the plane, but for simplicity it is stated only for the disk $\mathbb D$. Recall the definition of $H(\mathbb D)$ from Example 1.6.

**4.2. Proposition.** *$L\in H(\mathbb D)^*$ if and only if there is an $r<1$ and a unique function*
