positive and negative parts of $a$ and are denoted by $u=a_+$ and $v=a_-$. Note that $a_-\geq 0$.

If $a\in\mathcal A_+$, then the unique $b$ obtained in (3.5) is called the $n$th root of $a$ and is denoted by $b=a^{1/n}$. Note that if $b$ is not assumed to be positive, it is not necessarily unique (see Exercise 5).

If $X$ is compact and $f\in C(X)_+$, then notice that $|f(x)-t|\leq t$ for every real number $t\geq\|f\|$. Conversely, if $|f(x)-t|\leq t$ for some $t\geq\|f\|$, then $f(x)\geq 0$ for all $x$ and so $f\geq 0$. These observations are behind some of the statements in the next result.

**3.6. Theorem.** *If $\mathcal A$ is a $C^*$-algebra and $a\in\mathcal A$, then the following statements are equivalent.*

(a) $a\geq 0$.

(b) $a=b^2$ for some $b$ in $\operatorname{Re}\mathcal A$.

(c) $a=x^*x$ for some $x$ in $\mathcal A$.

(d) $a=a^*$ and $\|t-a\|\leq t$ for all $t\geq\|a\|$.

(e) $a=a^*$ and $\|t-a\|\leq t$ for some $t\geq\|a\|$.

**Proof.** It is clear that (b) implies (c) and (d) implies (e). By (3.5), (a) implies (b).

(e)$\Rightarrow$(a): Since $a=a^*$, $C^*(a)$ is abelian. If $X=\sigma(a)$, $X\subseteq\mathbb R$ and $f\mapsto f(a)$ is a $*$-isomorphism of $C(X)$ onto $C^*(a)$. Using this isomorphism and (e), $|t-x|\leq t$ for some $t\geq\|a\|=\sup\{|s|:s\in X\}$ and all $x$ in $X$. From the discussions preceding this theorem (with $f(x)=x$), $x\geq 0$ for all $x$ in $X$. That is, $X=\sigma(a)\subseteq[0,\infty)$. Hence $a\geq 0$.

(a)$\Rightarrow$(d): This proof follows the lines of the preceding paragraph and is left to the reader.

(c)$\Rightarrow$(a): If $a=x^*x$ for some $x$ in $\mathcal A$, then it is clear that $a=a^*$. Let $a=u-v$, where $u,v\geq 0$ and $uv=vu=0$. It must be shown that $v=0$.

If $xv^{1/2}=b+ic$, where $b,c\in\operatorname{Re}\mathcal A$, then $(xv^{1/2})^*(xv^{1/2})=(b-ic)(b+ic)=b^2+c^2+i(bc-cb)$. But also $(xv^{1/2})^*(xv^{1/2})=v^{1/2}x^*xv^{1/2}=v^{1/2}(u-v)v^{1/2}=-v^2$. Hence $i(bc-cb)=-v^2-b^2-c^2$. By Proposition 3.7 below, $i(bc-cb)\leq 0$. Also $(xv^{1/2})^*(xv^{1/2})=-v^2\leq 0$ because (a) and (b) are equivalent. By Exercise VII.3.7, $(xv^{1/2})(xv^{1/2})^*\leq 0$. Put $(xv^{1/2})(xv^{1/2})^*=-y$, where $y\in\mathcal A_+$. So $-y=(b+ic)(b-ic)=b^2+c^2-i(bc-cb)$. Hence $i(bc-cb)=b^2+c^2+y\in\mathcal A_+$ by (3.7). Therefore $i(bc-cb)\in(-\mathcal A_+)\cap\mathcal A_+=(0)$. But this implies that $-v^2=(xv^{1/2})^*(xv^{1/2})=b^2+c^2\in(-\mathcal A_+)\cap\mathcal A_+$, so that $v^2=0$. But $v\leq 0$ so $v=0$. That is, $a=u\geq 0$. $\blacksquare$

The next result will be proved only using the equivalence of (a), (d), and (e) from the preceding theorem.

**3.7. Proposition.** *If $\mathcal A$ is a $C^*$-algebra, then $\mathcal A_+$ is a closed cone.*

**Proof.** Let $\{a_n\}\subseteq\mathcal A_+$ and suppose $a_n\to a$. Clearly $a\in\operatorname{Re}\mathcal A$. By (3.6d), $\|a_n-\|a_n\|\|\leq\|a_n\|$. Hence $\|a-\|a\|\|\leq\|a\|$, so by (3.6e), $a\geq 0$.
