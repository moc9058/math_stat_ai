Let $\{U_j\}$ be the open subsets of $X$ such that $\operatorname{cl} U_j$ is compact. Let $C_0(U_j)$ be the continuous functions on $U_j$ vanishing at $\infty$ with the supremum norm. If $f\in C_0(U_j)$ and $f$ is defined on $X$ by letting it be identically $0$ on $X\setminus U_j$, then $f\in C_c(X)$. Thus $(C_c(X),\{C_0(U_j)\})$ is an inductive system. Proposition 5.8 implies that these two inductive systems define the same inductive limit topology on $C_c(X)$.

**5.11. Example.** Let $d\geqslant 1$ and put $K_n=\{x\in\mathbb R^d:\|x\|\leqslant n\}$. Then $(\mathcal D(\mathbb R^d),\{\mathcal D(K_n)\}_{n=1}^{\infty})$ is an inductive system. By (5.9), the inductive limit topology defined on $\mathcal D(\mathbb R^d)$ by this system equals the inductive limit topology defined by the system given in Example 5.2.

If $\Omega$ is any subset of $\mathbb R^d$, then $\Omega$ can be written as the union of a sequence of compact subsets $\{K_n\}$ such that $K_n\subseteq\operatorname{int}K_{n+1}$. It follows by (5.9) that $\{\mathcal D(K_n)\}$ defines the same topology on $\mathcal D(\Omega)$ as was defined in Example 5.2.

The preceding example inspires the following definition.

**5.12. Definition.** A strict inductive system is an inductive system $(\mathcal X,\{\mathcal X_n,\mathcal T_n\}_{n=1}^{\infty})$ such that for every $n\geqslant 1$, $\mathcal X_n\subseteq\mathcal X_{n+1}$, $\mathcal T_{n+1}|_{\mathcal X_n}=\mathcal T_n$, and $\mathcal X_n$ is closed in $\mathcal X_{n+1}$. The inductive limit topology defined on $\mathcal X$ by such a system is called a *strict inductive limit topology* and $\mathcal X$ is said to be the *strict inductive limit* of $\{\mathcal X_n\}$.

Example 5.11 shows that $\mathcal D(\mathbb R^d)$, indeed $\mathcal D(\Omega)$, is a strict inductive limit. The following lemma is useful in the study of strict inductive limits as well as in other situations.

**5.13. Proposition.** *If $\mathcal X$ is a LCS, $\mathcal Y\leqslant\mathcal X$, and $p$ is a continuous seminorm on $\mathcal Y$, then there is a continuous seminorm $\tilde p$ on $\mathcal X$ such that $\tilde p|_{\mathcal Y}=p$.*

**Proof.** Let $U=\{y\in\mathcal Y:p(y)<1\}$. So $U$ is open in $\mathcal Y$; hence there is an open subset $V_1$ of $\mathcal X$ such that $V_1\cap\mathcal Y=U$. Since $0\in V_1$ and $\mathcal X$ is a LCS, there is an open convex balanced set $V$ in $\mathcal X$ such that $V\subseteq V_1$. Let $q=$ the gauge of $V$. So if $y\in\mathcal Y$ and $q(y)<1$, then $p(y)<1$. By Lemma III.1.4, $p\leqslant q|_{\mathcal Y}$.

Let $W=\operatorname{co}(U\cup V)$; it is easy to see that $W$ is convex and balanced since both $U$ and $V$ are. It will be shown that $W$ is open. First observe that $W=\{tu+(1-t)v:0\leqslant t\leqslant 1,\ u\in U,\ v\in V\}$ (verify). Hence $W=\bigcup\{tU+(1-t)V:0\leqslant t\leqslant 1\}$. Put $W_t=tU+(1-t)V$. So $W_0=V$, which is open. If $0<t<1$, $W_t=\bigcup\{tu+(1-t)V:u\in U\}$, and hence is open. But $W_1=U$, which is not open. However, if $u\in U$, then there is an $\varepsilon>0$ such that $\varepsilon u\in V$. For $0<t<1$, let $y_t=t^{-1}[1-\varepsilon+t\varepsilon]u$ $(\in\mathcal Y)$. As $t\to 1$, $y_t\to u$. Since $U$ is open in $\mathcal Y$, there is a $t$, $0<t<1$, with $y_t$ in $U$. Thus $u=ty_t+(1-t)(\varepsilon u)\in W_t$. Therefore $W=\bigcup\{W_t:0\leqslant t<1\}$ and $W$ is open.

**5.14. Claim.** $W\cap\mathcal Y=U$.
