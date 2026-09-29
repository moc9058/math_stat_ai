not empty since $f(x)\subseteq\operatorname{cl}\mathbb D$ for every $f$ in $\mathcal F$. In fact, each $f$ in $\mathcal F$ gives rise to such a $b$ in $B$. Moreover $B$ is finite. Fix one function $f_b$ in $\mathcal F$ associated as above with $b$ in $B$.

**3.9. Claim.** $\displaystyle \mathcal F\subseteq\bigcup_{b\in B}\{f:\|f-f_b\|<\varepsilon\}$.

Note that (3.9) implies that $\mathcal F$ is totally bounded.

If $f\in\mathcal F$, there is a $b$ in $B$ such that $|f(x_j)-f_b(x_j)|<\varepsilon/3$ for $1\leq j\leq n$. Therefore if $x\in X$, let $x_j$ be chosen such that $x\in U_{x_j}$. Thus $|f(x)-f_b(x)|\leq |f(x)-f(x_j)|+|f(x_j)-f_b(x_j)|+|f_b(x_j)-f_b(x)|<\varepsilon$. Since $x$ was arbitrary, $\|f-f_b\|<\varepsilon$. ■

**3.10. Corollary.** *If $X$ is compact and $\mathcal F\subseteq C(X)$, then $\mathcal F$ is compact if and only if $\mathcal F$ is closed, bounded, and equicontinuous.*

**3.11. Theorem.** *If $X$ is compact, then $\mathcal B_{00}(C(X))$ is dense in $\mathcal B_0(C(X))$.*

**PROOF.** Let $T\in\mathcal B_0(C(X))$. Thus $T(\operatorname{ball}C(X))$ is bounded and equicontinuous by the Arzela–Ascoli Theorem. If $\varepsilon>0$ and $x\in X$, let $U_x$ be an open neighborhood of $x$ such that $|(Tf)(x)-(Tf)(y)|<\varepsilon$ for all $f$ in $\operatorname{ball}C(X)$ and $y$ in $U_x$. Let $\{x_1,\ldots,x_n\}\subseteq X$ such that $X\subseteq\bigcup_{j=1}^n U_{x_j}$. Let $\{\phi_1,\ldots,\phi_n\}$ be a partition of unity subordinate to $\{U_{x_1},\ldots,U_{x_n}\}$. Define $T_\varepsilon:C(X)\to C(X)$ by

$$
T_\varepsilon f=\sum_{j=1}^n(Tf)(x_j)\phi_j.
$$

Since $\operatorname{ran}T_\varepsilon\subseteq\bigvee\{\phi_1,\ldots,\phi_n\}$, $T_\varepsilon\in\mathcal B_{00}(C(X))$.

If $f\in\operatorname{ball}C(X)$ and $x\in X$, then

$$
\begin{aligned}
|(T_\varepsilon f)(x)-(Tf)(x)|
&=\left|\sum_{j=1}^n\bigl[(Tf)(x_j)-(Tf)(x)\bigr]\phi_j(x)\right|\\
&\leq\sum_{j=1}^n |(Tf)(x_j)-(Tf)(x)|\phi_j(x)\\
&<\varepsilon.
\end{aligned}
$$

■

If $X$ is locally compact, then the operators on $C_0(X)$ of finite rank are dense in $\mathcal B_0(C_0(X))$. See Exercise 18.

## Exercises

1. If $\mathcal X$ is reflexive and $A\in\mathcal B(\mathcal X,\mathcal Y)$, show that $A(\operatorname{ball}\mathcal X)$ is closed in $\mathcal Y$.
2. Prove Proposition 3.5.
3. If $A\in\mathcal B_0(\mathcal X,\mathcal Y)$, show that $\operatorname{cl}[\operatorname{ran}A]$ is separable.
