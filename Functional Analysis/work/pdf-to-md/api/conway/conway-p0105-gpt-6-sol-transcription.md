## Exercises

1. Show that $(\mathcal{X}^{*})^{**}$ and $(\mathcal{X}^{**})^{*}$ are equal.

2. Show that for a locally compact space $X$, $C_b(X)$ is reflexive if and only if $X$ is finite.

3. Let $\mathcal{M}\leqslant\mathcal{X}$ and let $\rho_{\mathcal{X}}:\mathcal{X}\to\mathcal{X}^{**}$ and $\rho_{\mathcal{M}}:\mathcal{M}\to\mathcal{M}^{**}$ be the natural maps. If $i:\mathcal{M}\to\mathcal{X}$ is the inclusion map, show that there is an isometry $\phi:\mathcal{M}^{**}\to\mathcal{X}^{**}$ such that the diagram

   ![Commutative square for the double dual inclusion](assets/conway-p0105-diagram.png)

   commutes. Prove that $\phi(\mathcal{M}^{**})=(\mathcal{M}^{\perp})^{\perp}\equiv\{x^{**}\in\mathcal{X}^{**}:x^{**}(\mathcal{M}^{\perp})=0\}$.

4. Use Exercise 3 to show that if $\mathcal{X}$ is reflexive, then any closed subspace of $\mathcal{X}$ is also reflexive. See Yang [1967].

## §12. The Open Mapping and Closed Graph Theorems

**12.1. The Open Mapping Theorem.** *If $\mathcal{X},\mathcal{Y}$ are Banach spaces and $A:\mathcal{X}\to\mathcal{Y}$ is a continuous linear surjection, then $A(G)$ is open in $\mathcal{Y}$ whenever $G$ is open in $\mathcal{X}$.*

**Proof.** For $r>0$, let $B(r)=\{x\in\mathcal{X}:\|x\|<r\}$.

**12.2. Claim.** $0\in\operatorname{int}\operatorname{cl}A(B(r))$.

Note that because $A$ is surjective,
$$
\mathcal{Y}
=\bigcup_{k=1}^{\infty}\operatorname{cl}[A(B(kr/2))]
=\bigcup_{k=1}^{\infty}k\operatorname{cl}[A(B(r/2))].
$$
By the Baire Category Theorem, there is a $k\geqslant1$ such that $k\operatorname{cl}[A(B(r/2))]$ has nonempty interior. Thus $V=\operatorname{int}\{\operatorname{cl}[A(B(r/2))]\}\ne\square$. If $y_0\in V$, let $s>0$ such that $\{y\in\mathcal{Y}:\|y-y_0\|<s\}\subseteq V\subseteq\operatorname{cl}A(B(r/2))$. Let $y\in\mathcal{Y}$, $\|y\|<s$. Since $y_0\in\operatorname{cl}A(B(r/2))$, there is a sequence $\{x_n\}$ in $B(r/2)$ such that $A(x_n)\to y_0$. There is also a sequence $\{z_n\}$ in $B(r/2)$ such that $A(z_n)\to y_0+y$. Thus $A(z_n-x_n)\to y$ and $\{z_n-x_n\}\subseteq B(r)$; that is, $\{y\in\mathcal{Y}:\|y\|<s\}\subseteq\operatorname{cl}A(B(r))$. This establishes Claim 12.2.

It will now be shown that

$$
\tag{12.3}
\operatorname{cl}A(B(r/2))\subseteq A(B(r)).
$$

Note that if (12.3) is proved, then Claim 12.2 implies that $0\in\operatorname{int}A(B(r))$ for any $r>0$. From here the theorem is easily proved. Indeed, if $G$ is an open subset of $\mathcal{X}$, then for every $x$ in $G$ let $r_x>0$ such that $B(x;r_x)\subseteq G$. But $0\in\operatorname{int}A(B(r_x))$ and so $A(x)\in\operatorname{int}A(B(x;r_x))$. Thus there is an $s_x>0$ such that $U_x\equiv\{y\in\mathcal{Y}:\|y-A(x)\|<s_x\}\subseteq A(B(x;r_x))$. Therefore $A(G)\supseteq\bigcup\{U_x:x\in G\}$. But $A(x)\in U_x$, so $A(G)=\bigcup\{U_x:x\in G\}$ and hence $A(G)$ is open.
