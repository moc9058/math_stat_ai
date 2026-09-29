20. Let $1\leq p\leq\infty$ and let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space. If $A\in\mathcal B_0(L^p(\mu))$, show that there is a sequence $\{A_n\}$ of finite-rank operators such that $\|A_n-A\|\to0$. (Hint: Use Exercise 19.)

21. Let $X$ be compact and let $\mathcal U$ be the collection of all pairs $(C,F)$ where $C=\{U_1,\ldots,U_n\}$ is a finite open cover of $X$ and $F=\{x_1,\ldots,x_n\}\subseteq X$ such that $x_j\in U_j$ for $1\leq j\leq n$. If $(C_1,F_1)$ and $(C_2,F_2)\in\mathcal U$, define $(C_1,F_1)\leq(C_2,F_2)$ to mean: (a) $C_2$ is a refinement of $C_1$; that is, each member of $C_2$ is contained in some member of $C_1$. (b) $F_1\subseteq F_2$. If $\alpha=(C,F)\in\mathcal U$ let $\{\phi_1,\ldots,\phi_n\}$ be a partition of unity subordinate to $C$. If $F=\{x_1,\ldots,x_n\}$, define $T_\alpha:C(X)\to C(X)$ by

   $$
   (T_\alpha f)(x)=\sum_{j=1}^{n}f(x_j)\phi_j(x).
   $$

   Then: (a) $T_\alpha\in\mathcal B_{00}(C(X))$; (b) $\|T_\alpha\|=1$; (c) $(\mathcal U,\leq)$ is a directed set and $\{T_\alpha:\alpha\in\mathcal U\}$ is a net; (d) $\|T_\alpha f-f\|\to0$ for each $f$. Now apply Exercise 19 to obtain a new proof of Theorem 3.11.

## §4. Invariant Subspaces

**4.1. Definition.** If $\mathcal X$ is a Banach space and $T\in\mathcal B(\mathcal X)$, an *invariant subspace* for $T$ is a closed linear subspace $\mathcal M$ of $\mathcal X$ such that $Tx\in\mathcal M$ whenever $x\in\mathcal M$. $\mathcal M$ is nontrivial if $\mathcal M\neq(0)$ or $\mathcal X$. $\operatorname{Lat}T=$ the collection of all invariant subspaces for $T$. If $\mathcal A\subseteq\mathcal B(\mathcal X)$, then $\operatorname{Lat}\mathcal A=\bigcap\{\operatorname{Lat}T:T\in\mathcal A\}$.

This generalizes the corresponding concept of invariant subspace for an operator on Hilbert space (II.3.5). Note that the idea of a reducing subspace for an operator on a Hilbert space has no generalization to Banach spaces since there is no concept of an orthogonal complement in Banach spaces.

**4.2. Proposition.**

(a) If $\mathcal M_1,\mathcal M_2\in\operatorname{Lat}T$, then $\mathcal M_1\vee\mathcal M_2\equiv\operatorname{cl}(\mathcal M_1+\mathcal M_2)\in\operatorname{Lat}T$ and $\mathcal M_1\wedge\mathcal M_2\equiv\mathcal M_1\cap\mathcal M_2\in\operatorname{Lat}T$.

(b) If $\{\mathcal M_i:i\in I\}\subseteq\operatorname{Lat}T$, then $\vee\{\mathcal M_i:i\in I\}$, the closed linear span of $\bigcup_i\mathcal M_i$, and $\wedge\{\mathcal M_i:i\in I\}\equiv\bigcap_i\mathcal M_i$ belong to $\operatorname{Lat}T$.

The proof of this proposition is left as an exercise. The proposition, however, does justify the use of the symbol “Lat” to denote the collection of invariant subspaces. With the operations $\vee$ and $\wedge$, $\operatorname{Lat}T$ is a lattice (a) that is complete (b). Moreover, $\operatorname{Lat}T$ has a largest element, $\mathcal X$, and a smallest element, $(0)$.

The main question is: does $\operatorname{Lat}T$ have any elements besides $(0)$ and $\mathcal X$? In other words, does $T$ have a nontrivial invariant subspace? C.J. Read [1984] showed the existence of a Banach space and an operator on the Banach space having no non-trivial invariant subspaces. This was preceded by some work of P Enflo (not published, but circulated) which did the same
