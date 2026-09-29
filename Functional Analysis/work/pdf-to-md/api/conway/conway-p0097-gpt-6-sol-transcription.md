10. Let $P=\{p|_{\partial\mathbb D}:p=\text{an analytic polynomial}\}$ and consider $P$ as a manifold in $C(\partial\mathbb D)$. Show that if $\mu$ is a real-valued measure on $\partial\mathbb D$ such that $\int p\,d\mu=0$ for every $p$ in $P$, then $\mu=0$. Give an example of a complex-valued measure $\mu$ such that $\mu\ne0$ but $\int p\,d\mu=0$ for every $p$ in $P$.

## §7*. An Application: Banach Limits

If $x=\{x(n)\}\in c$, define $L(x)=\lim x(n)$. Then $L$ is a linear functional, $\|L\|=1$, and, if for $x$ in $c$, $x'$ is defined by $x'=(x(2),x(3),\ldots)$, then $L(x)=L(x')$. Also, if $x\geqslant0$ [that is, $x(n)\geqslant0$ for all $n$], then $L(x)\geqslant0$. In this section it will be shown that these properties of the limit functional can be extended to $l^\infty$. The proof uses the Hahn–Banach Theorem.

**7.1. Theorem.** There is a linear functional $L:l^\infty\to\mathbb F$ such that

(a) $\|L\|=1$.

(b) If $x\in c$, $L(x)=\lim x(n)$.

(c) If $x\in l^\infty$ and $x(n)\geqslant0$ for all $n$, then $L(x)\geqslant0$.

(d) If $x\in l^\infty$ and $x'\equiv(x(2),x(3),\ldots)$, then $L(x)=L(x')$.

**Proof.** First assume $\mathbb F=\mathbb R$; that is, $l^\infty=l_{\mathbb R}^\infty$. If $x\in l^\infty$, let $x'$ denote the element of $l^\infty$ defined in part (d) above. Put $\mathcal M=\{x-x':x\in l^\infty\}$. Note that $(x+\alpha y)'=x'+\alpha y'$ for any $x,y$ in $l^\infty$ and $\alpha$ in $\mathbb R$; hence $\mathcal M$ is a linear manifold in $l^\infty$. Let $1$ denote the sequence $(1,1,1,\ldots)$ in $l^\infty$.

**7.2. Claim.** $\operatorname{dist}(1,\mathcal M)=1$.

Since $0\in\mathcal M$, $\operatorname{dist}(1,\mathcal M)\leqslant1$. Let $x\in l^\infty$; if $(x-x')(n)\leqslant0$ for any $n$, then $\|1-(x-x')\|_\infty\geqslant|1-(x(n)-x'(n))|\geqslant1$. Suppose $0\leqslant(x-x')(n)=x(n)-x'(n)=x(n)-x(n+1)$ for all $n$. Thus $x(n+1)\leqslant x(n)$ for all $n$. Since $x\in l^\infty$, $\alpha=\lim x(n)$ exists. Thus $\lim(x-x')(n)=0$ and $\|1-(x-x')\|_\infty\geqslant1$. This proves the claim.

By Corollary 6.8 there is a linear functional $L:l^\infty\to\mathbb R$ such that $\|L\|=1$, $L(1)=1$, and $L(\mathcal M)=0$. So this functional satisfies (a) and (d) of the theorem. To prove (b), we establish the following.

**7.3. Claim.** $c_0\subseteq\ker L$.

If $x\in c_0$, let $x^{(1)}=x'$ and let $x^{(n+1)}=(x^{(n)})'$ for $n\geqslant1$. Note that $x^{(n+1)}-x=[x^{(n+1)}-x^{(n)}]+\cdots+[x'-x]\in\mathcal M$. Hence $L(x)=L(x^{(n)})$ for all $n\geqslant1$. If $\varepsilon>0$, then let $n$ be such that $|x(m)|<\varepsilon$ for $m>n$. Hence $|L(x)|=|L(x^{(n)})|\leqslant\|x^{(n)}\|_\infty=\sup\{|x(m)|:m>n\}<\varepsilon$. Thus $x\in\ker L$. Condition (b) is now clear.

To show (c), suppose there is an $x$ in $l^\infty$ such that $x(n)\geqslant0$ for all $n$ and $L(x)<0$. If $x$ is replaced by $x/\|x\|_\infty$, it remains true that $L(x)<0$ and it is
