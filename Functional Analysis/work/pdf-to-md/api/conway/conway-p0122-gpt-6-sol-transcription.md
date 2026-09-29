$\{f:p(f)<1\}$ is not bounded. In fact, if $f_0$ is any function in $C(\mathbb{R})$ that vanishes on $[0,1]$, $\{\alpha f_0:\alpha\in\mathbb{R}\}\subseteq\{f:p(f)<1\}$. The fact that a normed space possesses a bounded open set is characteristic.

**2.6. Proposition.** *If $\mathscr{X}$ is a LCS, then $\mathscr{X}$ is normable if and only if $\mathscr{X}$ has a nonempty bounded open set.*

**Proof.** It has already been shown that a normed space has a bounded open set. So assume that $\mathscr{X}$ is a LCS that has a bounded open set $U$. It must be shown that there is norm on $\mathscr{X}$ that defines the same topology. By translation, it may be assumed that $0\in U$ (see Exercise 4i). By local convexity, there is a continuous seminorm $p$ such that $\{x:p(x)<1\}\equiv V\subseteq U$ (Why?). It will be shown that $p$ is a norm and defines the topology on $\mathscr{X}$.

To see that $p$ is a norm, suppose that $x\in\mathscr{X}$, $x\ne0$. Let $W_0,W_x$ be disjoint open sets such that $0\in W_0$ and $x\in W_x$. Then there is an $\varepsilon>0$ such that $W_0\supseteq\varepsilon U\supseteq\varepsilon V$. But $\varepsilon V=\{y:p(y)<\varepsilon\}$. Since $x\notin W_0$, $p(x)\geq\varepsilon$. Hence $p$ is a norm.

Because $p$ is continuous on $\mathscr{X}$, to show that $p$ defines the topology of $\mathscr{X}$ it suffices to show that if $q$ is any continuous seminorm on $\mathscr{X}$, there is an $\alpha>0$ such that $q\leq\alpha p$ (Why?). But because $q$ is continuous, there is an $\varepsilon>0$ such that $\{x:q(x)<1\}\supseteq\varepsilon U\supseteq\varepsilon V$. That is, $p(x)<\varepsilon$ implies $q(x)<1$. By Lemma III.1.4, $q\leq\varepsilon^{-1}p$. $\blacksquare$

## Exercises

1. Supply the missing details in the proof of Proposition 2.1.

2. Verify the statements in Example 2.2.

3. Verify the statements in Example 2.3.

4. Let $\mathscr{X}$ be a TVS and prove the following: (a) If $B$ is a bounded subset of $\mathscr{X}$, then so is $\operatorname{cl}B$. (b) The finite union of bounded sets is bounded. (c) Every compact set is bounded. (d) If $B\subseteq\mathscr{X}$, then $B$ is bounded if and only if for every sequence $\{x_n\}$ contained in $B$ and for every $\{\alpha_n\}$ in $c_0$, $\alpha_nx_n\to0$ in $\mathscr{X}$. (e) If $\mathscr{Y}$ is a TVS, $T:\mathscr{X}\to\mathscr{Y}$ is a continuous linear transformation, and $B$ is a bounded subset of $\mathscr{X}$, then $T(B)$ is a bounded subset of $\mathscr{Y}$. (f) If $\mathscr{X}$ is a LCS and $B\subseteq\mathscr{X}$, then $B$ is bounded if and only if for every continuous seminorm $p$, $\sup\{p(b):b\in B\}<\infty$. (g) If $\mathscr{X}$ is a normed space and $B\subseteq\mathscr{X}$, then $B$ is bounded if and only if $\sup\{\|b\|:b\in B\}<\infty$. (h) If $\mathscr{X}$ is a Fréchet space, then bounded sets have finite diameter, but not conversely. (i) The translate of a bounded set is bounded.

5. If $\mathscr{X}$ is a LCS, show that $\mathscr{X}$ is metrizable if and only if $\mathscr{X}$ is first countable. Is this equivalent to saying that $\{0\}$ is a $G_\delta$ set?

6. Let $X$ be a locally compact space and give $C_b(X)$ the strict topology defined in Exercise 1.21. Show that a subset of $C_b(X)$ is $\beta$-bounded if and only if it is norm bounded.

7. With the notation of Exercise 6, show that $(C_b(X),\beta)$ is metrizable if and only if $X$ is compact.

8. Prove the Open Mapping Theorem for Fréchet spaces.
