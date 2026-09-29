if $f_1\in S_{\mathcal B}$ there is a positive linear functional $f$ on $\operatorname{Re}\mathcal A$ such that $f|_{\operatorname{Re}\mathcal B}=f_1$. Since $1\in\mathcal B$, $f(1)=f_1(1)=1$. Now let $f(a)=f((a+a^*)/2)+if((a-a^*)/2i)$ for an arbitrary $a$ in $\mathcal A$. It follows that $f\in S_{\mathcal A}$ and $f|_{\mathcal B}=f_1$. ■

The next result says that every $C^*$-algebra is isomorphic to a $C^*$-algebra contained in $\mathcal B(\mathcal H)$ for some $\mathcal H$. Thus each $C^*$-algebra “is” an algebra of operators.

**5.17. Theorem.** *If $\mathcal A$ is a $C^*$-algebra, then there is a representation $(\pi,\mathcal H)$ of $\mathcal A$ such that $\pi$ is an isometry. If $\mathcal A$ is separable, then $\mathcal H$ can be chosen separable.*

**Proof.** Let $F$ be a weak* dense subset of $S_{\mathcal A}$ and let $\pi=\bigoplus\{\pi_f:f\in F\}$, $\mathcal H=\bigoplus\{\mathcal H_f:f\in F\}$. Thus $\|a\|^2\geq\|\pi(a)\|^2=\sup_f\|\pi_f(a)\|^2$. If $e_f$ is the cyclic vector for $\pi_f$, then $\|e_f\|^2=\langle e_f,e_f\rangle=\langle\pi_f(1)e_f,e_f\rangle=f(1)=1$. Hence $\|\pi_f(a)\|^2\geq\|\pi_f(a)e_f\|^2=\langle\pi_f(a^*a)e_f,e_f\rangle=f(a^*a)$, and $\|a\|^2\geq\|\pi(a)\|^2\geq\sup\{f(a^*a):f\in F\}$. Since $F$ is weak* dense in $S_{\mathcal A}$, Proposition 5.15 implies $\sup\{f(a^*a):f\in F\}=\|a^*a\|=\|a\|^2$. Hence $\pi$ is an isometry.

If $\mathcal A$ is separable, $(\operatorname{ball}\mathcal A^*,\mathrm{wk}^*)$ is a compact metric space (V.5.1). Hence $S_{\mathcal A}$ is weak* separable so that the set $F$ of the preceding paragraph can be chosen to be countable. Now if $f\in F$, $\pi_f(\mathcal A)e_f$ is a separable dense submanifold in $\mathcal H_f$ since $\mathcal A$ is separable. Thus $\mathcal H_f$ is separable. It follows that $\mathcal H$ is separable. ■

Actually, more can be said if $\mathcal A$ is separable. In fact, every separable $C^*$-algebra has a cyclic representation that is isometric (Exercise 11).

## Exercises

1. Let $\mathcal A$ be a $C^*$-algebra with identity and let $\pi:\mathcal A\to\mathcal B(\mathcal H)$ be a *-homomorphism [but don’t assume that $\pi(1)=1$]. Let $P_1=\pi(1)$. Show that $P_1$ is a projection and $\mathcal H_1\equiv P_1\mathcal H$ reduces $\pi(\mathcal A)$. If $\pi_1(a)=\pi(a)|_{\mathcal H_1}$, show that $\pi_1:\mathcal A\to\mathcal B(\mathcal H_1)$ is a representation.

2. Show that the representation in Example 5.4 is a cyclic representation and find all of the cyclic vectors.

3. Show that the representation in Example 5.5 is a cyclic representation and find all the cyclic vectors.

4. If $X$ is compact and $\mu$ is a positive measure on $X$, let $\pi_\mu:C(X)\to\mathcal B(L^2(\mu))$ be the representation defined in Example 5.5. If $\mu,\nu$ are positive measures on $X$ show that $\pi_\mu\oplus\pi_\nu$ is cyclic if and only if $\mu\perp\nu$. If $\mu\perp\nu$, then $\pi_\mu\oplus\pi_\nu$ is equivalent to $\pi_{\mu+\nu}$. Also, $\pi_\mu^{(n)}$ is not cyclic if $n\geq2$.

5. Verify the statements in Example 5.8.

6. If $\mathcal A=\mathbb C+\mathcal B_0(\mathcal H)$ and $\pi:\mathcal A\to\mathcal B(\mathcal H)$ is the identity representation, show that $\pi^{(\infty)}$ is a cyclic representation.

7. Fix a Banach limit LIM on $l^\infty(\mathbb N)$ and let $\mathcal H$ be a separable Hilbert space with an orthonormal basis $\{e_n\}$. Define $f:\mathcal B(\mathcal H)\to\mathbb C$ by $f(T)=\operatorname{LIM}\{\langle Te_n,e_n\rangle\}$. Show
