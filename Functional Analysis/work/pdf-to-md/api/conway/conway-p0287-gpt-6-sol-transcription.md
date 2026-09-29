$P=E(\varepsilon,\infty)$ has infinite rank. But $P=\left(\int t^{-1}\chi_{(\varepsilon,\infty)}(t)\,dE(t)\right)A^*A\in I$. Since $\mathcal H$ is separable, $\dim P\mathcal H=\dim\mathcal H=\aleph_0$. Let $U:\mathcal H\to P\mathcal H$ be a surjective isometry. It is easy to check that $1=U^*PU$. But $P\in I$, so $1\in I$. Hence $I=\mathcal B(\mathcal H)$. ■

In Proposition VIII.4.10, it was shown that every nonzero ideal of $\mathcal B(\mathcal H)$ contains the finite-rank operators. When combined with the preceding result, this yields the following.

**4.3. Corollary.** *If $\mathcal H$ is separable, then the only nontrivial closed ideal of $\mathcal B(\mathcal H)$ is the ideal of compact operators.*

The next proposition is related to Theorem VIII.5.9. Indeed, it is a consequence of it so that the proof will only be sketched.

Let $N$ be a normal operator on $\mathcal H$ and for every vector $e$ in $\mathcal H$ let $\mathcal H_e\equiv\bigvee\{N^{*k}N^je:k,j\geq 0\}$. So $\mathcal H_e$ is the smallest subspace of $\mathcal H$ that contains $e$ and reduces $N$. Also, $N|\mathcal H_e$ is a star-cyclic normal operator.

**4.4. Proposition.** *If $N$ is a normal operator on $\mathcal H$, then there are reducing subspaces $\{\mathcal H_i:i\in I\}$ for $N$ such that $\mathcal H=\bigoplus_i\mathcal H_i$ and $N|\mathcal H_i$ is star cyclic.*

**Proof.** Using Zorn’s Lemma find a maximal set of vectors $\mathcal E$ in $\mathcal H$ such that if $e,f\in\mathcal E$ and $e\ne f$, then $\mathcal H_e\perp\mathcal H_f$. It follows that $\mathcal H=\bigoplus_e\mathcal H_e$. ■

**4.5. Corollary.** *Every normal operator is unitarily equivalent to the direct sum of star-cyclic normal operators.*

By combining the preceding proposition with Theorem 3.4 on the representation of star-cyclic normal operators we can obtain the following theorem.

**4.6. Theorem.** *If $N$ is a normal operator on $\mathcal H$, then there is a measure space $(X,\Omega,\mu)$ and a function $\phi$ in $L^\infty(X,\Omega,\mu)$ such that $N$ is unitarily equivalent to $M_\phi$ on $L^2(X,\Omega,\mu)$.*

**Proof.** If $\mathcal M$ is a reducing subspace for $N$, then $N\cong N|\mathcal M\oplus N|\mathcal M^\perp$; thus $\sigma(N|\mathcal M)\subseteq\sigma(N)$. So if $\{N_i\}$ is a collection of star-cyclic normal operators such that $N\cong\bigoplus_iN_i$ (4.5), then $\sigma(N_i)\subseteq\sigma(N)$ for every $N_i$. By Theorem 3.4 there is a measure $\mu_i$ supported on $\sigma(N)$ such that $N_i\cong N_{\mu_i}$. Let $X_i=$ the support of $\mu_i$ and let $\Omega_i=$ the Borel subsets of $X_i$. Let $X=$ the disjoint union of $\{X_i\}$. Define $\Omega$ to be the collection of all subsets $\Delta$ of $X$ such that $\Delta\cap X_i\in\Omega_i$ for all $i$. It is easy to check that $\Omega$ is a $\sigma$-algebra. If $\Delta\in\Omega$ let $\mu(\Delta)\equiv\sum_i\mu_i(\Delta\cap X_i)$; then $(X,\Omega,\mu)$ is a measure space. If $f\in L^2(X,\Omega,\mu)$ then $f_i=f|X_i\in L^2(\mu_i)$. Moreover, the map $U:L^2(\mu)\to\bigoplus_iL^2(\mu_i)$ defined by $Uf=\bigoplus_i(f|X_i)$ is easily seen to be an isomorphism. Define $\phi:X\to\mathbb C$ by letting $\phi(z)=z$ if $z\in X_i$ ($\subseteq\mathbb C$); since $X_i\subseteq\sigma(N)$ for every $i$, $\phi$ is a bounded function. If $G$ is an open subset of $\mathbb C$,
