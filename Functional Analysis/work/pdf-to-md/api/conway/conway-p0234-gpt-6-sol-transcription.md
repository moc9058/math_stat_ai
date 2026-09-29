**8.3. Corollary.** If $\mathcal A$ is an abelian Banach algebra and $h:\mathcal A\to\mathbb C$ is a homomorphism, then $h$ is continuous.

**Proof.** Maximal ideals are closed (2.4b). ■

The next result improves the preceding corollary a little. Remember that by (8.3) if $h:\mathcal A\to\mathbb C$ is a homomorphism, then $h\in\mathcal A^*$ (the Banach space dual of $\mathcal A$).

**8.4. Proposition.** If $\mathcal A$ is abelian and $h:\mathcal A\to\mathbb C$ is a non-zero homomorphism, then $\|h\|=1$.

**Proof.** Let $a\in\mathcal A$ and put $\lambda=h(a)$. If $|\lambda|>\|a\|$, then $\|a/\lambda\|<1$. Hence $1-a/\lambda$ is invertible. Let $b=(1-a/\lambda)^{-1}$, so $1=b(1-a/\lambda)=b-ba/\lambda$. Since $h(1)=1$, $1=h(b-ba/\lambda)=h(b)-h(b)h(a)/\lambda=h(b)-h(b)=0$, a contradiction. Hence $\|a\|\geq|\lambda|=|h(a)|$; so $\|h\|\leq1$. Since $h(1)=1$, $\|h\|=1$. ■

**8.5. Definition.** If $\mathcal A$ is an abelian Banach algebra, let $\Sigma=$ the collection of all nonzero homomorphisms of $\mathcal A\to\mathbb C$. Give $\Sigma$ the relative weak* topology that it has as a subset of $\mathcal A^*$. $\Sigma$ with this topology is called the *maximal ideal space* of $\mathcal A$.

**8.6. Theorem.** If $\mathcal A$ is an abelian Banach algebra, then its maximal ideal space $\Sigma$ is a compact Hausdorff space. Moreover, if $a\in\mathcal A$, then $\sigma(a)=\Sigma(a)\equiv\{h(a):h\in\Sigma\}$.

**Proof.** Since $\Sigma\subseteq\operatorname{ball}\mathcal A^*$, it suffices for the proof of the first part of the theorem to show that $\Sigma$ is weak* closed. Let $\{h_i\}$ be a net in $\Sigma$ and suppose $h\in\operatorname{ball}\mathcal A^*$ such that $h_i\to h$ weak*. If $a,b\in\mathcal A$, then $h(ab)=\lim_i h_i(ab)=\lim_i h_i(a)h_i(b)=h(a)h(b)$. So $h$ is a homomorphism. Since $h(1)=\lim_i h_i(1)=1$, $h\in\Sigma$. Thus $\Sigma$ is compact.

If $h\in\Sigma$ and $\lambda=h(a)$, then $a-\lambda\in\ker h$. So $a-\lambda$ is not invertible and $\lambda\in\sigma(a)$; that is, $\Sigma(a)\subseteq\sigma(a)$. Now assume that $\lambda\in\sigma(a)$; so $a-\lambda$ is not invertible and, hence, $(a-\lambda)\mathcal A$ is a proper ideal. Let $\mathcal M$ be a maximal ideal in $\mathcal A$ such that $(a-\lambda)\mathcal A\subseteq\mathcal M$. If $h\in\Sigma$ such that $\mathcal M=\ker h$, then $0=h(a-\lambda)=h(a)-\lambda$; hence $\sigma(a)\subseteq\Sigma(a)$. ■

Now it is time for an example. Here is one that is a little more than an example. If $X$ is compact and $x\in X$, let $\delta_x:C(X)\to\mathbb C$ be defined by $\delta_x(f)=f(x)$. It is easy to see that $\delta_x$ is a homomorphism on the algebra $C(X)$.

**8.7. Theorem.** If $X$ is compact and $\Sigma$ is the maximal ideal space of $C(X)$, then the map $x\mapsto\delta_x$ is a homeomorphism of $X$ onto $\Sigma$.

**Proof.** Let $\Delta:X\to\Sigma$ be defined by $\Delta(x)=\delta_x$. As was pointed out before, $\Delta(X)\subseteq\Sigma$. It was shown in Proposition V.6.1 that $\Delta:X\to(\Delta(X),\text{ weak}^*)$ is a homeomorphism. Thus it only remains to show that $\Delta(X)=\Sigma$. If $h\in\Sigma$, then
