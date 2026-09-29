**3.9. Theorem.** Let $\mathscr{X}$ be a real LCS and let $A$ and $B$ be two disjoint closed convex subsets of $\mathscr{X}$. If $B$ is compact, then $A$ and $B$ are strictly separated.

**Proof.** By hypothesis, $B$ is a compact subset of the open set $\mathscr{X}\setminus A$. The preceding lemma implies there is an open neighborhood $U_1$ of $0$ such that $B+U_1\subseteq\mathscr{X}\setminus A$. Because $\mathscr{X}$ is locally convex, there is a continuous seminorm $p$ on $\mathscr{X}$ such that $\{x:p(x)<1\}\subseteq U_1$. Put $U=\{x:p(x)<\frac12\}$. Then $(B+U)\cap(A+U)=\square$ (Verify!), and $A+U$ and $B+U$ are open convex subsets of $\mathscr{X}$ that contain $A$ and $B$, respectively. (Why?) So the result follows from Theorem 3.7. $\blacksquare$

The fact that one of the two closed convex sets in the preceding theorem is assumed to be compact is necessary. In fact, if $\mathscr{X}=\mathbb{R}^2$, $A=\{(x,y)\in\mathbb{R}^2:y\leqslant0\}$, and $B=\{(x,y)\in\mathbb{R}^2:y\geqslant x^{-1}>0\}$, then $A$ and $B$ are disjoint closed convex subsets of $\mathbb{R}^2$ that cannot be strictly separated.

The next result generalizes Corollary III.6.8, though, of course, the metric content of (III.6.8) is missing.

**3.10. Corollary.** If $\mathscr{X}$ is a real LCS, $A$ is a closed convex subset of $\mathscr{X}$, and $x\notin A$, then $x$ is strictly separated from $A$.

**3.11. Corollary.** If $\mathscr{X}$ is a real LCS and $A\subseteq\mathscr{X}$, then $\overline{\operatorname{co}}(A)$ is the intersection of the closed half-spaces containing $A$.

**Proof.** Let $\mathscr{H}$ be the collection of all closed half-spaces containing $A$. Since each set in $\mathscr{H}$ is closed and convex, $\overline{\operatorname{co}}(A)\subseteq\bigcap\{H:H\in\mathscr{H}\}$. On the other hand, if $x_0\notin\overline{\operatorname{co}}(A)$, then (3.10) implies there is a continuous linear functional $f:\mathscr{X}\to\mathbb{R}$ and an $\alpha$ in $\mathbb{R}$ such that $f(x_0)>\alpha$ and $f(x)<\alpha$ for all $x$ in $\overline{\operatorname{co}}(A)$. Thus $H=\{x:f(x)\leqslant\alpha\}$ belongs to $\mathscr{H}$ and $x_0\notin H$. $\blacksquare$

The next result generalizes Theorem III.6.13.

**3.12. Corollary.** If $\mathscr{X}$ is a real LCS and $A\subseteq\mathscr{X}$, then the closed linear span of $A$ is the intersection of all closed hyperplanes containing $A$.

If $\mathscr{X}$ is a complex LCS, it is also a real LCS. This can be used to formulate and prove versions of the preceding results. As a sample, the following complex version of Theorem 3.9 is presented.

**3.13. Theorem.** Let $\mathscr{X}$ be a complex LCS and let $A$ and $B$ be two disjoint closed convex subsets of $\mathscr{X}$. If $B$ is compact, then there is a continuous linear functional $f:\mathscr{X}\to\mathbb{C}$, an $\alpha$ in $\mathbb{R}$, and an $\varepsilon>0$ such that for $a$ in $A$ and $b$ in $B$,

$$
\operatorname{Re}f(a)\leqslant\alpha<\alpha+\varepsilon\leqslant\operatorname{Re}f(b).
$$

**3.14. Corollary.** If $\mathscr{X}$ is a LCS and $\mathscr{Y}$ is a linear manifold in $\mathscr{X}$, then $\mathscr{Y}$ is
