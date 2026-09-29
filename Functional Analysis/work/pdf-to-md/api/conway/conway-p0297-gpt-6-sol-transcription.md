$\rho(T)=T\oplus T$. Then $\rho$ is a $*$-isomorphism. However, $\mathcal A_\mu$ and $\mathcal A_\mu^{(2)}$ are not *spatially isomorphic*. That is, there is no Hilbert space isomorphism $U:L^2(\mu)\to L^2(\mu)\oplus L^2(\mu)$ such that $U\mathcal A_\mu U^{-1}=\mathcal A_\mu^{(2)}$. Why? One way to see that no such $U$ exists is to note that $\mathcal A_\mu$ has a cyclic vector (give an example). However, $\mathcal A_\mu^{(2)}$ does not have a cyclic vector as shall be seen presently (Theorem 7.8).

**7.5. Definition.** If $\mathcal A\subseteq\mathcal B(\mathcal H)$ and $e_0\in\mathcal H$, then $e_0$ is a *separating vector* for $\mathcal A$ if the only operator $A$ in $\mathcal A$ such that $Ae_0=0$ is the operator $A=0$.

If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $f\in L^2(\mu)$ such that $\mu(\{x\in X:f(x)=0\})=0$ (Why does such an $f$ exist?), then $f$ is a separating vector for $\mathcal A_\mu$ as well as a cyclic vector. If $\mathcal A=\mathcal B(\mathcal H)$, then no vector in $\mathcal H$ is separating for $\mathcal A$ while every nonzero vector is a cyclic vector. If $\mathcal A=\mathbb C$ and $\dim\mathcal H>1$, then $\mathcal A$ has no cyclic vectors but every nonzero vector is separating for $\mathcal A$.

**7.6. Proposition.** *If $e_0$ is a cyclic vector for $\mathcal A$, then $e_0$ is a separating vector for $\mathcal A'$.*

**Proof.** If $T\in\mathcal A'$ and $Te_0=0$, then for every $A$ in $\mathcal A$, $TAe_0=ATe_0=0$. Since $\bigvee\mathcal A e_0=\mathcal H$, $T=0$. $\blacksquare$

**7.7. Corollary.** *If $\mathcal A$ is an abelian subalgebra of $\mathcal B(\mathcal H)$, then every cyclic vector for $\mathcal A$ is a separating vector for $\mathcal A$.*

**Proof.** Because $\mathcal A$ is abelian, $\mathcal A\subseteq\mathcal A'$. $\blacksquare$

Since $\mathcal B(\mathcal H)'=\mathbb C$, Proposition 7.6 explains some of the duality exhibited prior to (7.6). Also note that if $(X,\Omega,\mu)$ is a finite measure space, $1\oplus0$, $0\oplus1$, and $1\oplus1$ are all separating vectors for $\mathcal A_\mu^{(2)}$. Because $\mathcal A_\mu^{(2)}\ne(\mathcal A_\mu^{(2)})'$, the next theorem says that $\mathcal A_\mu^{(2)}$ has no cyclic vector.

Although it is easy to see that conditions (a) and (b) in the next result are equivalent, irrespective of any assumption on $\mathcal H$, the equivalence of the remaining parts to (a) and (b) is not true unless some additional assumption is made on $\mathcal H$ or $\mathcal A$ (see Exercise 5). We are content to assume that $\mathcal H$ is separable.

**7.8. Theorem.** *Assume that $\mathcal H$ is separable and $\mathcal A$ is an abelian $C^*$-subalgebra of $\mathcal B(\mathcal H)$. The following statements are equivalent.*

(a) $\mathcal A$ is a maximal abelian von Neumann algebra.

(b) $\mathcal A=\mathcal A'$.

(c) $\mathcal A$ has a cyclic vector, contains $1$, and is SOT closed.

(d) There is a compact metric space $X$, a positive Borel measure $\mu$ with support $X$, and an isomorphism $U:L^2(\mu)\to\mathcal H$ such that $U\mathcal A_\mu U^{-1}=\mathcal A$.

**Proof.** The proof that (a) and (b) are equivalent is left as an exercise.
