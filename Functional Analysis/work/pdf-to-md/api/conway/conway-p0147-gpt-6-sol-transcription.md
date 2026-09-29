there is an $x^*$ in $\mathcal X^*$, an $\alpha$ in $\mathbf R$, and an $\varepsilon>0$ such that

$$
\operatorname{Re}\langle x,x^*\rangle<\alpha<\alpha+\varepsilon<\operatorname{Re}\langle x^*,x_0^{**}\rangle
$$

for all $x$ in $\operatorname{ball}\mathcal X$. (Exactly how does the Hahn–Banach Theorem imply this?) Since $0\in\operatorname{ball}\mathcal X$, $0<\alpha$. Dividing by $\alpha$ and replacing $x^*$ by $\alpha^{-1}x^*$, it may be assumed that there is an $x^*$ in $\mathcal X^*$ and an $\varepsilon>0$ such that

$$
\operatorname{Re}\langle x,x^*\rangle<1<1+\varepsilon<\operatorname{Re}\langle x^*,x_0^{**}\rangle
$$

for all $x$ in $\operatorname{ball}\mathcal X$. Since $e^{i\theta}x\in\operatorname{ball}\mathcal X$ whenever $x\in\operatorname{ball}\mathcal X$, this implies that $|\langle x,x^*\rangle|\leq 1$ if $\|x\|\leq 1$. Hence $x^*\in\operatorname{ball}\mathcal X^*$. But then $1+\varepsilon<\operatorname{Re}\langle x^*,x_0^{**}\rangle\leq|\langle x^*,x_0^{**}\rangle|\leq\|x_0^{**}\|\leq 1$, a contradiction. ■

**4.2. Theorem.** *If $\mathcal X$ is a Banach space, the following statements are equivalent.*

(a) $\mathcal X$ is reflexive.

(b) $\mathcal X^*$ is reflexive.

(c) $\sigma(\mathcal X^*,\mathcal X)=\sigma(\mathcal X^*,\mathcal X^{**})$.

(d) $\operatorname{ball}\mathcal X$ is weakly compact.

**Proof.** (a)$\Rightarrow$(c): This is clear since $\mathcal X=\mathcal X^{**}$.

(d)$\Rightarrow$(a): Note that $\sigma(\mathcal X^{**},\mathcal X^*)|\mathcal X=\sigma(\mathcal X,\mathcal X^*)$. By (d), $\operatorname{ball}\mathcal X$ is $\sigma(\mathcal X^{**},\mathcal X^*)$ closed in $\operatorname{ball}\mathcal X^{**}$. But the preceding proposition implies $\operatorname{ball}\mathcal X$ is $\sigma(\mathcal X^{**},\mathcal X^*)$ dense in $\operatorname{ball}\mathcal X^{**}$. Hence $\operatorname{ball}\mathcal X=\operatorname{ball}\mathcal X^{**}$ and so $\mathcal X$ is reflexive.

(c)$\Rightarrow$(b): By Alaoglu’s Theorem, $\operatorname{ball}\mathcal X^*$ is $\sigma(\mathcal X^*,\mathcal X)$-compact. By (c), $\operatorname{ball}\mathcal X^*$ is $\sigma(\mathcal X^*,\mathcal X^{**})$ compact. Since it has already been shown that (d) implies (a), this implies that $\mathcal X^*$ is reflexive.

(b)$\Rightarrow$(a): Now $\operatorname{ball}\mathcal X$ is norm closed in $\mathcal X^{**}$; hence $\operatorname{ball}\mathcal X$ is $\sigma(\mathcal X^{**},\mathcal X^{***})$ closed in $\mathcal X^{**}$ (Corollary 1.5). Since $\mathcal X^*=\mathcal X^{***}$ by (b), this says that $\operatorname{ball}\mathcal X$ is $\sigma(\mathcal X^{**},\mathcal X^*)$ closed in $\mathcal X^{**}$. But, according to (4.1), $\operatorname{ball}\mathcal X$ is $\sigma(\mathcal X^{**},\mathcal X^*)$ dense in $\operatorname{ball}\mathcal X^{**}$. Hence $\operatorname{ball}\mathcal X=\operatorname{ball}\mathcal X^{**}$ and $\mathcal X$ is reflexive.

(a)$\Rightarrow$(d): By Alaoglu’s Theorem, $\operatorname{ball}\mathcal X^{**}$ is $\sigma(\mathcal X^{**},\mathcal X^*)$ compact. Since $\mathcal X=\mathcal X^{**}$, this says that $\operatorname{ball}\mathcal X$ is $\sigma(\mathcal X,\mathcal X^*)$ compact. ■

**4.3. Corollary.** *If $\mathcal X$ is a reflexive Banach space and $\mathcal M\leq\mathcal X$, then $\mathcal M$ is a reflexive Banach space.*

**Proof.** Note that $\operatorname{ball}\mathcal M=\mathcal M\cap[\operatorname{ball}\mathcal X]$, so $\operatorname{ball}\mathcal M$ is $\sigma(\mathcal X,\mathcal X^*)$ compact. It remains to show that $\sigma(\mathcal X,\mathcal X^*)|\mathcal M=\sigma(\mathcal M,\mathcal M^*)$. But this follows by (2.3). (How?) ■

Call a sequence $\{x_n\}$ in $\mathcal X$ a *weakly Cauchy sequence* if for every $x^*$ in $\mathcal X^*$, $\{\langle x_n,x^*\rangle\}$ is a Cauchy sequence in $\mathbf F$.

**4.4. Corollary.** *If $\mathcal X$ is reflexive, then every weakly Cauchy sequence in $\mathcal X$ converges weakly. That is, $\mathcal X$ is weakly sequentially complete.*

**Proof.** Since $\{\langle x_n,x^*\rangle\}$ is a Cauchy sequence in $\mathbf F$ for each $x^*$ in $\mathcal X^*$, $\{x_n\}$
