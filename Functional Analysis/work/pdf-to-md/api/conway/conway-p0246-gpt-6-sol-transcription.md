$$
\hat f(\gamma)=\int \gamma(x^{-1})\,dx=\chi_{\{1\}}(\gamma).
$$

Since $\hat f$ is continuous on $\Gamma$, $\{1\}$ is an open set. By translation, every singleton set in $\Gamma$ is open and hence $\Gamma$ is discrete. $\blacksquare$

**9.16. Theorem.** If $a\in\mathbb T$, define $\gamma_a:\mathbb Z\to\mathbb T$ by $\gamma_a(n)=a^n$. Then $\gamma_a\in\widehat{\mathbb Z}$ and the map $a\mapsto\gamma_a$ is a homeomorphism and an isomorphism of $\mathbb T$ onto $\widehat{\mathbb Z}$. If $a\in\mathbb T$ and $f\in L^1(\mathbb Z)=l^1(\mathbb Z)$, then

$$
\hat f(\gamma_a)=\hat f(a)=\sum_{n=-\infty}^{\infty}f(n)a^{-n}. \tag{9.17}
$$

**Proof.** Again the proof that $a\mapsto\gamma_a$ is a monomorphism of $\mathbb T\to\widehat{\mathbb Z}$ is left to the reader. If $\gamma\in\widehat{\mathbb Z}$, let $\gamma(1)=a\in\mathbb T$. Also, $\gamma(n)=\gamma(1)^n=a^n$, so $\gamma=\gamma_a$. Hence $a\mapsto\gamma_a$ is an isomorphism. It is easy to show that this map is continuous and hence, by compactness, a homeomorphism. $\blacksquare$

For additional reading, consult Rudin [1962].

## Exercises

1. Prove that if $L^1(G)$ has an identity, then $G$ is discrete.

2. If $f\in L^\infty(G)$, show that $x\mapsto f_x$ is a continuous function from $G$ into $(L^\infty(G),\mathrm{wk}^*)$.

3. Is there a measure $\mu$ on $\mathbb R$ different from Lebesgue measure such that for $f$ in $L^1(\mu)$, $x\mapsto f_x$ is continuous? Is there a measure for which this map is discontinuous?

4. If $f\in C_0(G)$, show that $x\mapsto f_x$ is a continuous map from $G\to C_0(G)$.

5. If $f\in L^\infty(G)$ and $f$ is uniformly continuous on $G$, show that $x\mapsto f_x$ is a continuous function from $G\to L^\infty(G)$. Is the converse true? See Edwards [1961].

6. If $K$ is a compact subset of $G$, $\gamma_0\in\Gamma$, and $\varepsilon>0$, let $U(K,\gamma_0,\varepsilon)=\{\gamma\in\Gamma:|\gamma(x)-\gamma_0(x)|<\varepsilon\text{ for all }x\in K\}$. Show that the collection of all such sets is a base for the topology of $\Gamma$. (This says that the topology on $\Gamma$ is the *compact-open topology*.)

7. Show that there is a discontinuous homomorphism $\gamma:\mathbb R\to\mathbb T$. If $\gamma:\mathbb R\to\mathbb T$ is a homomorphism that is a Borel function, show that $\gamma$ is continuous.

8. If $G$ is a compact abelian group, show that the linear span of $\Gamma$ is dense in $C(G)$.

9. If $G$ is a compact abelian group, show that $\Gamma$ forms an orthonormal basis in $L^2(G)$.

10. If $G$ is a compact abelian group, show that $G$ is metrizable if and only if $\Gamma$ is countable.

11. Let $\{G_\alpha\}$ be a family of compact abelian groups and $G=\prod_\alpha G_\alpha$. If $\Gamma_\alpha=\widehat{G_\alpha}$, show that the character group of $G$ is $\{\{\gamma_\alpha\}\in\prod_\alpha\Gamma_\alpha:\gamma_\alpha=e\text{ except for at most a finite number of }\alpha\}$.
