**Proof.** If $x_n\to x$ and $y_n\to y$, then $\|(x_n+y_n)-(x+y)\|=\|(x_n-x)+(y_n-y)\|\leq\|x_n-x\|+\|y_n-y\|\to0$ as $n\to\infty$. This proves (a). The proof of (b) is left to the reader. $\blacksquare$

The next lemma is quite useful.

**1.4. Lemma.** *If $p$ and $q$ are seminorms on a vector space $\mathcal{X}$, then the following statements are equivalent.*

(a) $p(x)\leq q(x)$ *for all* $x$. (*That is,* $p\leq q$.)

(b) $\{x\in\mathcal{X}:q(x)<1\}\subseteq\{x\in\mathcal{X}:p(x)<1\}$.

(b′) $p(x)<1$ *whenever* $q(x)<1$.

(c) $\{x:q(x)\leq1\}\subseteq\{x:p(x)\leq1\}$.

(c′) $p(x)\leq1$ *whenever* $q(x)\leq1$.

(d) $\{x:q(x)<1\}\subseteq\{x:p(x)\leq1\}$.

(d′) $p(x)\leq1$ *whenever* $q(x)<1$.

**Proof.** It is clear that (b) and (b′), (c) and (c′), and (d) and (d′) are equivalent. It is also clear that (a) implies all of the remaining conditions and that both (b) and (c) imply (d). It remains to show that (d) implies (a).

Assume that (d) holds and put $q(x)=\alpha$. If $\varepsilon>0$, then $q((\alpha+\varepsilon)^{-1}x)=(\alpha+\varepsilon)^{-1}\alpha<1$. By (d), $1\geq p((\alpha+\varepsilon)^{-1}x)=(\alpha+\varepsilon)^{-1}p(x)$, so $p(x)\leq\alpha+\varepsilon=q(x)+\varepsilon$. Letting $\varepsilon\to0$ shows (a). $\blacksquare$

If $\|\cdot\|_1$ and $\|\cdot\|_2$ are two norms on $\mathcal{X}$, they are said to be *equivalent norms* if they define the same topology on $\mathcal{X}$.

**1.5. Proposition.** *If $\|\cdot\|_1$ and $\|\cdot\|_2$ are two norms on $\mathcal{X}$, then these norms are equivalent if and only if there are positive constants $c$ and $C$ such that*

$$
c\|x\|_1\leq\|x\|_2\leq C\|x\|_1
$$

*for all $x$ in $\mathcal{X}$.*

**Proof.** Suppose there are constants $c$ and $C$ such that $c\|x\|_1\leq\|x\|_2\leq C\|x\|_1$ for all $x$ in $\mathcal{X}$. Fix $x_0$ in $\mathcal{X}$, $\varepsilon>0$. Then

$$
\{x\in\mathcal{X}:\|x-x_0\|_1<\varepsilon/C\}\subseteq
\{x\in\mathcal{X}:\|x-x_0\|_2<\varepsilon\},
$$

$$
\{x\in\mathcal{X}:\|x-x_0\|_2<c\varepsilon\}\subseteq
\{x\in\mathcal{X}:\|x-x_0\|_1<\varepsilon\}.
$$

This shows that the two topologies are the same. Now assume that the two norms are equivalent. Hence $\{x:\|x\|_1<1\}$ is an open neighborhood of $0$ in the topology defined by $\|\cdot\|_2$. Therefore there is an $r>0$ such that $\{x:\|x\|_2<r\}\subseteq\{x:\|x\|_1<1\}$. If $q(x)=r^{-1}\|x\|_2$ and $p(x)=\|x\|_1$, the preceding lemma implies $\|x\|_1\leq r^{-1}\|x\|_2$ or $c\|x\|_1\leq\|x\|_2$, where $c=r$. The other inequality is left to the reader. $\blacksquare$

There are two types of properties of a Banach space: those that are topological and those that are metric. The metric properties depend on the
