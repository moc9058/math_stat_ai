§2. Abelian $C^*$-Algebras and the Functional Calculus in $C^*$-Algebras 239

the Riesz Functional Calculus. If $f\in C(\sigma(a))$, then there is a sequence $\{p_n\}$ of polynomials in $z$ and $\bar z$ such that $p_n(z,\bar z)\to f(z)$ uniformly on $\sigma(a)$. But $\tau(p_n)=p_n(a,a^*)$, $\tau(p_n)\to\tau(f)$ (1.11d), and $p_n(a,a^*)\to f(a)$. Hence $\tau(f)=f(a)$. $\blacksquare$

Because of the uniqueness statement in the preceding theorem, it is not necessary to remember the form of the functional calculus $f\mapsto f(a)$, but only the fact that it is an isometric *-monomorphism that extends the Riesz Functional Calculus. Indeed, by the uniqueness of the Riesz Functional Calculus, it suffices to have that $f\mapsto f(a)$ is an isometric *-monomorphism such that if $f(z)\equiv 1$, then $f(a)=1$, and if $f(z)=z$, then $f(a)=a$. Any properties or applications of the functional calculus can be derived or justified using only these properties. There may, however, be an occasion when the precise form of the functional calculus [viz., (2.4)] facilitates a proof. There are also situations in which the definition of the functional calculus gets in the way of a proof and the properties in (2.6) give the clean way of applying this powerful tool.

**2.7. Spectral Mapping Theorem.** *If $\mathcal A$ is a $C^*$-algebra and $a$ is a normal element of $\mathcal A$, then for every $f$ in $C(\sigma(a))$,*

$$
\sigma(f(a))=f(\sigma(a)).
$$

**Proof.** Let $\rho\colon C(\sigma(a))\to C^*(a)$ be defined by $\rho(f)=f(a)$. So $\rho$ is a *-isomorphism. Hence $\sigma(f(a))=\sigma(\rho(f))=\sigma(f)$. But $\sigma(f)=f(\sigma(a))$ (VII.3.2). $\blacksquare$

Once again (1.14) was used implicitly in the preceding proof.

## Exercises

1. Prove a converse to Proposition 2.3. If $K$ is a compact subset of $\mathbb C$, $C(K)$ is a singly generated $C^*$-algebra.

2. If $\mathcal A$ is an abelian $C^*$-algebra with a finite number of $C^*$-generators $a_1,\ldots,a_n$, then there is a compact subset $X$ of $\mathbb C^n$ and an isometric *-isomorphism $\rho\colon\mathcal A\to C(X)$ such that $\rho(a_k)=z_k$, $1\leq k\leq n$, where $z_k(\lambda_1,\ldots,\lambda_n)=\lambda_k$ (see Exercise VII.8.12).

3. If $X$ is a compact Hausdorff space, show that $X$ is totally disconnected if and only if $C(X)$ is the closed linear span of its projections ($\equiv$ hermitian idempotents).

4. Using the terminology of Exercise 3, show that if $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, the maximal ideal space of $L^\infty(X,\Omega,\mu)$ is totally disconnected.

5. If $\mathcal A$ is a $C^*$-algebra with identity and $a=a^*$, show that $\exp(ia)=u$ is unitary. Is the converse true?

6. Let $X$ be compact and fix a point $x_0$ in $X$. Let $\mathcal A=\{\{f_n\}: f_n\in C(X),\ \sup_n\|f_n\|<\infty,\text{ and }\{f_n(x_0)\}\text{ is a convergent sequence}\}$. Show that $\mathcal A$ is an abelian $C^*$-algebra with identity and find its maximal ideal space.
