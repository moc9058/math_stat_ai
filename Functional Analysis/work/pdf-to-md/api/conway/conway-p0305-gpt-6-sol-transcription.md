10. Give an example of two normal operators $M$ and $N$ such that $W^*(M\oplus N)=W^*(M)\oplus W^*(N)$ but $C^*(M\oplus N)\ne C^*(M)\oplus C^*(N)$. In fact, find $M$ and $N$ such that $W^*(M\oplus N)$ splits, but $\sigma(M)=\sigma(N)$.

11. If $U$ is the bilateral shift and $V$ is any unitary operator, show that $W^*(U\oplus V)=W^*(U)\oplus W^*(V)$ if and only if $V$ has a spectral measure that is singular to arc length on $\partial\mathbb D$. (See Exercise 3.7.)

12. If $\mathcal A$ is an abelian von Neumann algebra on a separable space, show that there is a compactly supported measure $\mu$ on $\mathbb R$ such that $\mathcal A$ is $*$-isomorphic to $L^\infty(\mu)$. (Hint: Use Exercise 7.7.)

13. (This exercise assumes a knowledge of Exercise 2.21.) Let $N=\int z\,dE(z)$ be a normal operator with scalar-valued spectral measure $\mu$ and define $\alpha:\mathcal B_1(\mathcal H)\to L^1(\mu)$ by $\alpha(T)(\Delta)=\operatorname{tr}(TE(\Delta))$. Show that $\alpha$ is a surjective contraction. What is $\alpha^*$? [$L^1(\mu)$ is identified, via the Radon–Nikodym Theorem, with the set of complex-valued measures that are absolutely continuous with respect to $\mu$.]

14. Let $\pi:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)/\mathcal B_0(\mathcal H)$ be the natural map and let $A\in\mathcal B(\mathcal H)$. (a) If $\pi(A)$ is hermitian, show that there is a hermitian operator $B$ such that $A-B$ is compact. (b) If $\pi(A)$ is positive, show that there is a positive operator $B$ such that $A-B$ is compact. (See Exercise XI.3.14.)

15. (L.G. Brown) If $\pi:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)/\mathcal B_0(\mathcal H)$ is the natural map and $A$ and $B$ are hermitian operators such that $\pi(A)\leq 0\leq\pi(B)$, then there is a hermitian compact operator $K$ such that $A\leq K\leq B$.

## §9. Invariant Subspaces for Normal Operators

Remember that we continue to assume that all Hilbert spaces are separable.

Every normal operator on a Hilbert space of dimension at least 2 has a nontrivial invariant subspace. This is an easy consequence of the Spectral Theorem. Indeed, if $N=\int z\,dE(z)$, $E(\Delta)\mathcal H$ is a reducing subspace for every Borel set $\Delta$.

If $A\in\mathcal B(\mathcal H)$, $\mathcal M$ is a linear subspace of $\mathcal H$, and $P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M$, then $\mathcal M$ reduces $A$ if and only if $P\in\{A\}'$. Also, $\mathcal M\in\operatorname{Lat}A$ (= the lattice of invariant subspaces for $A$) if and only if $AP=PAP$. Since the spectral projections of a normal operator belong to $W^*(N)$, they are even more than reducing.

**9.1. Definition.** An operator $A$ is *reductive* if every invariant subspace for $A$ reduces $A$. Equivalently, $A$ is reductive if and only if $\operatorname{Lat}A\subseteq\operatorname{Lat}A^*$.

Thus, every self-adjoint operator is reductive. Every normal operator on a finite dimensional space is reductive. More generally, every normal compact operator is reductive (Andô [1963]). However, the bilateral shift is not reductive. Indeed, if $U$ is the bilateral shift on $\ell^2(\mathbb Z)$, $\mathcal H=\{f\in\ell^2(\mathbb Z):f(n)=0$
