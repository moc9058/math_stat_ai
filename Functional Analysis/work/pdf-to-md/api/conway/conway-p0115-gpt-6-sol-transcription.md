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
