uses of Proposition 4.4 in this book will occur when $K=\sigma(a)$. If $f:G\to\mathbb C$ is analytic and $\sigma(a)\subseteq G$, we will define an element $f(a)$ in $\mathcal A$ by

$$
f(a)=\frac{1}{2\pi i}\int_\Gamma f(z)(z-a)^{-1}\,dz. \tag{4.5}
$$

where $\Gamma$ is as in Proposition 4.4 with $K=\sigma(a)$. But first it must be shown that (4.5) does not depend on the choice of $\Gamma$. That is, it must be shown that $f(a)$ is well defined.

**4.6. Proposition.** *Let $\mathcal A$ be a Banach algebra with identity, let $a\in\mathcal A$, and let $G$ be an open subset of $\mathbb C$ such that $\sigma(a)\subseteq G$. If $\Gamma=\{\gamma_1,\ldots,\gamma_m\}$ and $\Lambda=\{\lambda_1,\ldots,\lambda_k\}$ are two positively oriented collections of curves in $G$ such that $\sigma(a)\subseteq\operatorname{ins}\Gamma\subseteq G$ and $\sigma(a)\subseteq\operatorname{ins}\Lambda\subseteq G$ and if $f:G\to\mathbb C$ is analytic, then*

$$
\int_\Gamma f(z)(z-a)^{-1}\,dz
=
\int_\Lambda f(z)(z-a)^{-1}\,dz.
$$

**Proof.** For $1\leq j\leq k$, let $\gamma_{m+j}=\lambda_j^{-1}$; that is, $\gamma_{m+j}(t)=\lambda_j(1-t)$ for $0\leq t\leq1$. If $z\notin G\setminus\sigma(a)$, then either $z\in\mathbb C\setminus G$ or $z\in\sigma(a)$. If $z\in\mathbb C\setminus G$, then $\sum_{j=1}^{m+k}n(\gamma_j;z)=n(\Gamma;z)-n(\Lambda;z)=0-0=0$. If $z\in\sigma(a)$, then $\sum_{j=1}^{m+k}n(\gamma_j;z)=n(\Gamma;z)-n(\Lambda;z)=1-1=0$. Thus $\Sigma\equiv\{\gamma_j:1\leq j\leq m+k\}$ is a system of closed curves in $U=G\setminus\sigma(a)$ such that $n(\Sigma;z)=0$ for all $z$ in $\mathbb C\setminus U$. Since $z\mapsto f(z)(z-a)^{-1}$ is analytic on $U$, Cauchy’s Theorem implies

$$
0=\int_\Sigma f(z)(z-a)^{-1}\,dz
=\int_\Gamma f(z)(z-a)^{-1}\,dz
-\int_\Lambda f(z)(z-a)^{-1}\,dz.
\qquad\blacksquare
$$

As was pointed out before, Proposition 4.6 implies that (4.5) gives a well-defined element $f(a)$ of $\mathcal A$ whenever $f$ is analytic in a neighborhood of $\sigma(a)$. Let $\operatorname{Hol}(a)=$ all of the functions that are analytic in a neighborhood of $\sigma(a)$. Note that $\operatorname{Hol}(a)$ is an algebra where if $f,g\in\operatorname{Hol}(a)$ and $f$ and $g$ have domains $D(f)$ and $D(g)$, then $fg$ and $f+g$ have domain $D(f)\cap D(g)$. $\operatorname{Hol}(a)$ is not, however, a Banach algebra.

**4.7. The Riesz Functional Calculus.** *Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$.*

(a) *The map $f\mapsto f(a)$ of $\operatorname{Hol}(a)\to\mathcal A$ is an algebra homomorphism.*

(b) *If $f(z)=\sum_{k=0}^{\infty}\alpha_kz^k$ has radius of convergence $>r(a)$, then $f\in\operatorname{Hol}(a)$ and $f(a)=\sum_{k=0}^{\infty}\alpha_ka^k$.*

(c) *If $f(z)\equiv1$, then $f(a)=1$.*

(d) *If $f(z)=z$ for all $z$, $f(a)=a$.*

(e) *If $f,f_1,f_2,\ldots$ are all analytic on $G$, $\sigma(a)\subseteq G$, and $f_n(z)\to f(z)$ uniformly on compact subsets of $G$, then $\|f_n(a)-f(a)\|\to0$ as $n\to\infty$.*

**Proof.** (a) Let $f,g\in\operatorname{Hol}(a)$ and let $G$ be an open neighborhood of $\sigma(a)$ on which both $f$ and $g$ are analytic. Let $\Gamma$ be a positively oriented system of
