direct sum of $A$ with itself $n$ times; so $A^{(n)}\in\mathcal B(\mathcal H^{(n)})$ and $\|A^{(n)}\|=\|A\|$. The operator $A^{(n)}$ is called the *inflation* of $A$. If $\pi:\mathcal A\to\mathcal B(\mathcal H)$ is a representation, the inflation of $\pi$ is the map $\pi^{(n)}:\mathcal A\to\mathcal B(\mathcal H^{(n)})$ defined by $\pi^{(n)}(a)=\pi(a)^{(n)}$ for all $a$ in $\mathcal A$.

**5.4. Example.** If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\mathcal H=L^2(\mu)$, then $\pi:L^\infty(\mu)\to\mathcal B(\mathcal H)$ defined by $\pi(\phi)=M_\phi$ is a representation.

**5.5. Example.** If $X$ is a compact space and $\mu$ is a positive Borel measure on $X$, then $\pi:C(X)\to\mathcal B(L^2(\mu))$ defined by $\pi(f)=M_f$ is a representation.

**5.6. Definition.** A representation $\pi$ of a $C^*$-algebra $\mathcal A$ is *cyclic* if there is a vector $e$ in $\mathcal H$ such that $\operatorname{cl}[\pi(\mathcal A)e]=\mathcal H$; $e$ is said to be a *cyclic vector* for the representation $\pi$.

Note that the representations in Examples 5.4 and 5.5 are cyclic (Exercises 2 and 3). Also, the identity representation $i:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)$ is cyclic and every nonzero vector is a cyclic vector for this representation. If $\mathcal A=\mathbb C+\mathcal B_0(\mathcal H)$, then the identity representation is cyclic. On the other hand, if $n\geqslant2$, then the inflation $\pi^{(n)}$ of a representation of $C(X)$ is never cyclic (Exercise 4).

There is another way to obtain representations.

**5.7. Definition.** If $\{(\pi_i,\mathcal H_i):i\in I\}$ is a family of representations of $\mathcal A$, then the *direct sum* of this family is the representation $(\pi,\mathcal H)$, where $\mathcal H=\bigoplus_i\mathcal H_i$ and $\pi(a)=\{\pi_i(a)\}$ for every $a$ in $\mathcal A$.

Note that since $\|\pi_i(a)\|\leqslant\|a\|$ for every $i$ (4.8), $\pi(a)$ is a bounded operator on $\mathcal H$. It is easy to check that $\pi$ is a representation.

**5.8. Example.** Let $X$ be a compact space and let $\{\mu_n\}$ be a sequence of measures on $X$. For each $n$ let $\pi_n:C(X)\to\mathcal B(L^2(\mu_n))$ be defined by $\pi_n(f)=M_f$ on $L^2(\mu_n)$. Then $\pi=\bigoplus_n\pi_n$ is a representation. If the measures $\{\mu_n\}$ are pairwise mutually singular, then $\pi$ is equivalent (below) to the representation $f\to M_f$ of $C(X)\to\mathcal B(L^2(\mu))$, where $\mu=\sum_{n=1}^{\infty}\mu_n/2^n\|\mu_n\|$ (Exercise 5).

The concept of equivalence for representations is that of unitary equivalence. That is, two representations of a $C^*$-algebra $\mathcal A$, $(\pi_1,\mathcal H_1)$ and $(\pi_2,\mathcal H_2)$, are *equivalent* if there is an isomorphism $U:\mathcal H_1\to\mathcal H_2$ such that $U\pi_1(a)U^{-1}=\pi_2(a)$ for every $a$ in $\mathcal A$. The importance of cyclic representations arises from the fact, given in the next result, that every representation is equivalent to the direct sum of cyclic representations.

**5.9. Theorem.** If $\pi$ is a representation of the $C^*$-algebra $\mathcal A$, then there is a family of cyclic representations $\{\pi_i\}$ of $\mathcal A$ such that $\pi$ and $\bigoplus_i\pi_i$ are equivalent.

**Proof.** let $\mathcal E$ = the collection of all subsets $E$ of nonzero vectors in $\mathcal H$ such that $\pi(\mathcal A)e\perp\pi(\mathcal A)f$ for $e,f$ in $E$ with $e\ne f$. Order $\mathcal E$ by inclusion. An
