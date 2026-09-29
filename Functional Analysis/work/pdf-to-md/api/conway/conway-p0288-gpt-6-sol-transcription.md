$\phi^{-1}(G)\cap X_i=G\cap X_i\in\Omega_i$; hence $\phi$ is $\Omega$-measurable. Therefore $\phi\in L^\infty(X,\Omega,\mu)$. It is left to the reader to check that $UM_\phi U^{-1}=\bigoplus_i N_{\mu_i}\cong N$. $\blacksquare$

**4.7. Proposition.** *If $\mathcal H$ is separable, then the measure space in Theorem 4.6 is $\sigma$-finite.*

**Proof.** First note that the measure space $(X,\Omega,\mu)$ constructed in the preceding theorem has no infinite atoms. Now let $\mathcal E$ be a collection of pairwise disjoint sets from $\Omega$ having non-zero finite measure. A computation shows that $\{(\mu(\Delta))^{-1/2}\chi_\Delta:\Delta\in\mathcal E\}$ are pairwise orthogonal vectors in $L^2(\mu)$. If $L^2(\mu)$ is separable, then $\mathcal E$ must be countable. Therefore $(X,\Omega,\mu)$ is $\sigma$-finite. $\blacksquare$

Of course if $(X,\Omega,\mu)$ is finite it is not necessarily true that $L^2(\mu)$ is separable.

The next result will be useful later in this book and it also provides a different type of application of the Spectral Theorem.

**4.8. Proposition.** *If $\mathcal A$ is an SOT closed $C^*$-subalgebra of $\mathcal B(\mathcal H)$, then $\mathcal A$ is the norm closed linear span of the projections in $\mathcal A$.*

**Proof.** If $A\in\mathcal A$, $A+A^*$ and $A-A^*\in\mathcal A$; hence $\mathcal A$ is the linear span of $\operatorname{Re}\mathcal A$. Suppose $A\in\operatorname{Re}\mathcal A$ and $A=\int t\,dE(t)$. If $[a,b]\subseteq\mathbb R$, then there is a sequence $\{u_n\}$ in $C(\mathbb R)$ such that $0\leq u_n\leq1$, $u_n(t)=1$ for $a\leq t\leq b-n^{-1}$, $u_n(t)=0$ for $t\leq a-n^{-1}$ and $t\geq b$. Hence $u_n(t)\to\chi_{[a,b)}(t)$ as $n\to\infty$. If $h\in\mathcal H$, then

$$
\|\{u_n(A)-E[a,b)\}h\|^2
=\int |u_n(t)-\chi_{[a,b)}(t)|^2\,dE_{h,h}(t)\to0
$$

by the Lebesgue Dominated Convergence Theorem. That is, $u_n(A)\to E[a,b)$ (SOT). Since $\mathcal A$ is SOT-closed, $E[a,b)\in\mathcal A$. Now let $(\alpha,\beta)$ be an open interval containing $\sigma(A)$. If $\varepsilon>0$, then there is a partition $\{\alpha=t_0<\cdots<t_n=\beta\}$ such that $\left|t-\sum_{k=1}^n t_k\chi_{[t_{k-1},t_k)}(t)\right|<\varepsilon$ for $t$ in $\sigma(A)$; hence $\left\|A-\sum_{k=1}^n t_kE[t_{k-1},t_k)\right\|<\varepsilon$. Thus every self-adjoint operator in $\mathcal A$ belongs to the closed linear span of the projections in $\mathcal A$. $\blacksquare$

## Exercises

1. If $N$ is a normal operator show that $\operatorname{ran}N$ is closed if and only if $0$ is not a limit point of $\sigma(N)$.

2. Give an example of a non-normal operator $A$ such that $0$ is an isolated point of $\sigma(A)$ and $\operatorname{ran}A$ is closed. Give an example of a non-normal operator $B$ such that $\operatorname{ran}B$ is closed and $0$ is not an isolated point of $\sigma(B)$.

3. If $\mathcal H$ is a nonseparable Hilbert space find an example of a nontrivial closed ideal of $\mathcal B(\mathcal H)$ that is different from $\mathcal B_0(\mathcal H)$.

4. Let $(X,\Omega,\mu)$ be the measure space obtained in the proof of Theorem 4.6 and show that $L^1(X,\Omega,\mu)^*$ is isometrically isomorphic to $L^\infty(X,\Omega,\mu)$.

5. Show that $\mathcal H$ is separable if and only if every collection of pairwise orthogonal projections in $\mathcal B(\mathcal H)$ is countable.
