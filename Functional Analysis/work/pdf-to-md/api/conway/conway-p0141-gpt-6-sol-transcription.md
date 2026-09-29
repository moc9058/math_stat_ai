**1.4. Theorem.** *If $\mathcal X$ is a LCS and $A$ is a convex subset of $\mathcal X$, then $\operatorname{cl}A=\mathrm{wk}\text{-}\operatorname{cl}A$.*

**Proof.** If $\mathcal T$ is the original topology of $\mathcal X$, then $\mathrm{wk}\subseteq\mathcal T$, hence $\operatorname{cl}A\subseteq\mathrm{wk}\text{-}\operatorname{cl}A$. Conversely, if $x\in\mathcal X\setminus\operatorname{cl}A$, then (IV.3.13) implies that there is an $x^*$ in $\mathcal X^*$, an $\alpha$ in $\mathbb R$, and an $\varepsilon>0$ such that

$$
\operatorname{Re}\langle a,x^*\rangle\leq\alpha<\alpha+\varepsilon\leq\operatorname{Re}\langle x,x^*\rangle
$$

for all $a$ in $\operatorname{cl}A$. Hence $\operatorname{cl}A\subseteq B\equiv\{y\in\mathcal X:\operatorname{Re}\langle y,x^*\rangle\leq\alpha\}$. But $B$ is clearly $\mathrm{wk}$-closed since $x^*$ is $\mathrm{wk}$-continuous. Thus $\mathrm{wk}\text{-}\operatorname{cl}A\subseteq B$. Since $x\notin B$, $x\notin\mathrm{wk}\text{-}\operatorname{cl}A$. ■

**1.5. Corollary.** *A convex subset of $\mathcal X$ is closed if and only if it is weakly closed.*

There is a useful observation that can be made here. Because of (III.6.3) it can be shown that if $\mathcal X$ is a complex linear space, then the weak topology on $\mathcal X$ is the same as the weak topology it has if it is considered as a real linear space (Exercise 4). This will be used in the future.

**1.6. Definition.** If $A\subseteq\mathcal X$, the *polar* of $A$, denoted by $A^\circ$, is the subset of $\mathcal X^*$ defined by

$$
A^\circ\equiv\{x^*\in\mathcal X^*:|\langle a,x^*\rangle|\leq 1\text{ for all }a\text{ in }A\}.
$$

If $B\subseteq\mathcal X^*$, the *prepolar* of $B$, denoted by ${}^\circ B$, is the subset of $\mathcal X$ defined by

$$
{}^\circ B\equiv\{x\in\mathcal X:|\langle x,b^*\rangle|\leq 1\text{ for all }b^*\text{ in }B\}.
$$

If $A\subseteq\mathcal X$ the *bipolar* of $A$ is the set ${}^\circ(A^\circ)$. If there is no confusion, then it is also denoted by ${}^\circ A^\circ$.

The prototype for this idea is that if $A$ is the unit ball in a normed space, $A^\circ$ is the unit ball in the dual space.

**1.7. Proposition.** *If $A\subseteq\mathcal X$, then*

(a) $A^\circ$ is convex and balanced.

(b) If $A_1\subseteq A$, then $A^\circ\subseteq A_1^\circ$.

(c) If $\alpha\in\mathbb F$ and $\alpha\ne 0$, $(\alpha A)^\circ=\alpha^{-1}A^\circ$.

(d) $A\subseteq{}^\circ A^\circ$.

(e) $A^\circ=({}^\circ A^\circ)^\circ$.

**Proof.** The proofs of parts (a) through (d) are left as an exercise. To prove (e) note that $A\subseteq{}^\circ A^\circ$ by (d), so $({}^\circ A^\circ)^\circ\subseteq A^\circ$ by (b). But $A^\circ\subseteq{}^\circ(A^\circ)^\circ$ by an analog of (d) for prepolars. Also, ${}^\circ(A^\circ)^\circ=({}^\circ A^\circ)^\circ$. ■

There is an analogous result for prepolars. In fact, it is more than analogy that is at work here. By Theorem 1.3, $(\mathcal X^*,\mathrm{wk}^*)^*=\mathcal X$. Thus the result for prepolars is a consequence of the preceding proposition.
