**4.2. Cauchy’s Integral Formula.** If $\mathcal{X}$ is a Banach space, $G$ is an open subset of $\mathbb{C}$, $f:G\to\mathcal{X}$ is analytic, $\gamma$ is a closed rectifiable curve in $G$ such that $n(\gamma;a)=0$ for every $a$ in $\mathbb{C}\setminus G$, and $\lambda\in G\setminus\{\gamma\}$, then for every integer $k\geq 0$,

$$
n(\gamma;\lambda)f^{(k)}(\lambda)
=\frac{k!}{2\pi i}\int_\gamma (z-\lambda)^{-(k+1)}f(z)\,dz.
$$

**4.3. Definition.** A closed rectifiable curve $\gamma$ is *positively oriented* if for every $a$ in $G\setminus\{\gamma\}$, $n(\gamma;a)$ is either 0 or 1. In this case the *inside* of $\gamma$, denoted by ins $\gamma$, is defined by

$$
\operatorname{ins}\gamma\equiv
\{a\in\mathbb{C}\setminus\{\gamma\}:n(\gamma;a)=1\}.
$$

The *outside* of $\gamma$, denoted by out $\gamma$, is defined by

$$
\operatorname{out}\gamma\equiv
\{a\in\mathbb{C}\setminus\{\gamma\}:n(\gamma;a)=0\}.
$$

Thus $\mathbb{C}=\{\gamma\}\cup\operatorname{ins}\gamma\cup\operatorname{out}\gamma$.

A curve $\gamma:[0,1]\to\mathbb{C}$ is *simple* if $\gamma(s)=\gamma(t)$ implies that either $s=t$ or $s=0$ and $t=1$. The Jordan Curve Theorem says that if $\gamma$ is a simple closed rectifiable curve, then $\mathbb{C}\setminus\{\gamma\}$ has two components and $\{\gamma\}$ is the boundary of each. Hence $n(\gamma;a)$ takes on only two values and one of these must be 0; the other must be $\pm1$.

If $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ is a collection of closed rectifiable curves, then $\Gamma$ is *positively oriented* if: (a) $\{\gamma_i\}\cap\{\gamma_j\}=\square$ for $i\ne j$; (b) for $a$ in $\mathbb{C}\setminus\bigcup_{j=1}^{m}\{\gamma_j\}$, $n(\Gamma;a)\equiv\sum_{j=1}^{m}n(\gamma_j;a)$ is either 0 or 1; (c) each $\gamma_j$ is a simple curve. The *inside* of $\Gamma$, ins $\Gamma$, is defined by

$$
\operatorname{ins}\Gamma\equiv\{a:n(\Gamma;a)=1\}.
$$

The *outside* of $\Gamma$, out $\Gamma$, is defined by

$$
\operatorname{out}\Gamma\equiv\{a:n(\Gamma;a)=0\}.
$$

Let $\{\Gamma\}\equiv\bigcup\{\gamma_j:1\leq j\leq m\}$.

**4.4. Proposition.** If $G$ is an open subset of $\mathbb{C}$ and $K$ is a compact subset of $G$, then there is a positively oriented system of curves $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ in $G\setminus K$ such that $K\subseteq\operatorname{ins}\Gamma$ and $\mathbb{C}\setminus G\subseteq\operatorname{out}\Gamma$. The curves $\gamma_1,\ldots,\gamma_m$ can be found such that they are infinitely differentiable.

The proof of this proposition can be found on p. 195 of Conway [1978], though some details are missing.

If $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ and each $\gamma_j$ is rectifiable, define

$$
\int_\Gamma f=\sum_{j=1}^{m}\int_{\gamma_j}f
$$

whenever $f$ is continuous in a neighborhood of $\{\Gamma\}$.

Let $\mathcal{A}$ be a Banach algebra with identity and let $a\in\mathcal{A}$. One of the principal
