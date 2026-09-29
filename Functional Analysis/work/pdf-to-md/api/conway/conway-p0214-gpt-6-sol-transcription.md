5. If $\mathcal A$ is a Banach algebra with identity, $\{a_n\}\subseteq\mathcal A$, $a_n\to a$, $\alpha_n\in\sigma(a_n)$, and $\alpha_n\to\alpha$, then $\alpha\in\sigma(a)$.

6. If $\mathcal A$ is a Banach algebra with identity and $r:\mathcal A\to[0,\infty)$ is the spectral radius, show that $r$ is upper semicontinuous. If $a\in\mathcal A$ such that $r(a)=0$, show that $r$ is continuous at $a$.

7. If $\mathcal A$ is a Banach algebra with identity, $a,b\in\mathcal A$, and $\alpha$ is a nonzero scalar such that $(\alpha-ab)$ is invertible, show that $(\alpha-ba)$ is invertible and $(\alpha-ba)^{-1}=\alpha^{-1}+\alpha^{-1}b(\alpha-ab)^{-1}a$. Show that $\sigma(ab)\cup\{0\}=\sigma(ba)\cup\{0\}$ and give an example such that $\sigma(ab)\ne\sigma(ba)$.

## §4. The Riesz Functional Calculus

Before coming to the main course of this section, it is necessary to have an appetizer from complex analysis. Many of these topics can be found in Conway [1978] with complete proofs. Only a few results are presented here.

If $\gamma$ is a closed rectifiable curve in $\mathbb C$ and $a\notin\{\gamma\}\equiv\{\gamma(t):0\leq t\leq1\}$, then the *winding number of $\gamma$ about $a$* is defined to be the number

$$
n(\gamma;a)=\frac{1}{2\pi i}\int_\gamma\frac{1}{z-a}\,dz.
$$

The number $n(\gamma;a)$ is always an integer and is constant on each component of $\mathbb C\setminus\{\gamma\}$ and vanishes on the unbounded component of $\mathbb C\setminus\{\gamma\}$.

Let $G$ be an open subset of $\mathbb C$ and let $\mathcal X$ be a Banach space. If $f:G\to\mathcal X$ is analytic and $x^*\in\mathcal X^*$, then $z\mapsto\langle f(z),x^*\rangle$ is analytic on $G$ and its derivative is $\langle f'(z),x^*\rangle$. By Exercise 4 of the preceding section, if $f:G\to\mathcal X$ is a function such that $z\mapsto\langle f(z),x^*\rangle$ is analytic for each $x^*$ in $\mathcal X^*$, then $f:G\to\mathcal X$ is analytic. These facts will help in discussing and proving many of the results below.

If $\gamma$ is a rectifiable curve in $G$ and $f$ is a continuous function defined in a neighborhood of $\{\gamma\}$ with values in $\mathcal X$, then $\int_\gamma f$ can be defined as for a scalar-valued $f$ as the limit in $\mathcal X$ of sums of the form

$$
\sum_j[\gamma(t_j)-\gamma(t_{j-1})]f(\gamma(t_j)),
$$

where $\{t_0,t_1,\ldots,t_n\}$ is a partition of $[0,1]$. Hence $\int_\gamma f=\int_0^1 f(\gamma(t))\,d\gamma(t)\in\mathcal X$. It is easy to see that for every $x^*$ in $\mathcal X^*$, $\left\langle\int_\gamma f,x^*\right\rangle=\int_\gamma\langle f(\cdot),x^*\rangle$.

**4.1. Cauchy’s Theorem.** If $\mathcal X$ is a Banach space, $G$ is an open subset of $\mathbb C$, $f:G\to\mathcal X$ is an analytic function, and $\gamma_1,\ldots,\gamma_m$ are closed rectifiable curves in $G$ such that $\sum_{j=1}^m n(\gamma_j;a)=0$ for all $a$ in $\mathbb C\setminus G$, then $\sum_{j=1}^m\int_{\gamma_j}f=0$.

**Proof.** If $x^*\in\mathcal X^*$, then
$$
\left\langle\sum_{j=1}^m\int_{\gamma_j}f,x^*\right\rangle
=\sum_{j=1}^m\int_{\gamma_j}\langle f(\cdot),x^*\rangle=0
$$
by the scalar-valued version of Cauchy’s Theorem. Hence $\sum_{j=1}^m\int_{\gamma_j}f=0$. $\blacksquare$
