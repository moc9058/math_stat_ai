Theorem and the Fuglede–Putnam Theorem. If $\phi\in B(\sigma(N))$, $N=\int z\,dE(z)$, and $T\in\{N\}'$, then $T\in\{N,N^*\}'$ by the Fuglede–Putnam Theorem and $TE(\Delta)=E(\Delta)T$ for every Borel set $\Delta$ by the Spectral Theorem. Hence $T\phi(N)=\phi(N)T$ since $\phi(N)=\int\phi\,dE$. $\blacksquare$

The purpose of this section is to prove that the containment in the preceding proposition is an equality. In fact, more will be proved. A measure $\mu$ whose support is $\sigma(N)$ will be found such that $\phi(N)$ is well defined if $\phi\in L^\infty(\mu)$ and the map $\phi\mapsto\phi(N)$ is a *-isomorphism of $L^\infty(\mu)$ onto $W^*(N)$. To find $\mu$, Corollary 7.9 (which requires the separability of $\mathcal H$) is used.

By Corollary 7.9, $W^*(N)$, being an abelian von Neumann algebra, has a separating vector $e_0$. Define a measure $\mu$ on $\sigma(N)$ by

$$
\tag{8.2}
\mu(\Delta)=\langle E(\Delta)e_0,e_0\rangle=\|E(\Delta)e_0\|^2.
$$

**8.3. Proposition.** $\mu(\Delta)=0$ if and only if $E(\Delta)=0$.

**Proof.** If $\mu(\Delta)=0$, then $E(\Delta)e_0=0$. But $E(\Delta)=\chi_\Delta(N)\in W^*(N)$. Since $e_0$ is a separating vector, $E(\Delta)=0$. The reverse implication is clear. $\blacksquare$

**8.4. Definition.** A *scalar-valued spectral measure for* $N$ is a positive Borel measure $\mu$ on $\sigma(N)$ such that $\mu(\Delta)=0$ if and only if $E(\Delta)=0$; that is, $\mu$ and $E$ are mutually absolutely continuous.

So Proposition 8.3 says that scalar-valued spectral measures exist. It will be shown (8.9) that every scalar-valued spectral measure is defined by (8.2) where $e_0$ is a separating vector for $W^*(N)$. In the process additional information is obtained about a normal operator and its functional calculus.

If $h\in\mathcal H$, let $\mu_h\equiv E_{h,h}$ and let $\mathcal H_h\equiv\operatorname{cl}[W^*(N)h]$. Note that $\mathcal H_h$ is the smallest reducing subspace for $N$ that contains $h$. Let $N_h\equiv N|_{\mathcal H_h}$. Thus $N_h$ is a *-cyclic normal operator with *-cyclic vector $h$. The uniqueness of the spectral measure for a normal operator implies that the spectral measure for $N_h$ is $E(\Delta)|_{\mathcal H_h}$; that is, $\chi_\Delta(N_h)=\chi_\Delta(N)|_{\mathcal H_h}=E(\Delta)|_{\mathcal H_h}$. Thus Theorem 3.4 implies there is a unique isomorphism $U_h:\mathcal H_h\to L^2(\mu_h)$ such that $U_hh=1$ and $U_hN_hU_h^{-1}f=zf$ for all $f$ in $L^2(\mu_h)$. The notation of this paragraph is used repeatedly in this section.

The way to understand what is going on is to consider each $N_h$ as a localization of $N$. Since $N_h$ is unitarily equivalent to $M_z$ on $L^2(\mu_h)$ we can agree that we thoroughly understand the local behavior of $N$. Can we put together this local behavior of $N$ to understand the global behavior of $N$? This is precisely what is done in §10.

In the present section the objective is to show that if $h$ is a separating vector for $W^*(N)$, then the functional calculus for $N$ is completely determined by the functional calculus for $N_h$. The sense in which this “determination” is made is the following. If $A\in W^*(N)$, then the definition of $\mathcal H_h$ shows that $A\mathcal H_h\subseteq\mathcal H_h$. Since $A^*\in W^*(N)$, $\mathcal H_h$ reduces each operator in $W^*(N)$; thus
