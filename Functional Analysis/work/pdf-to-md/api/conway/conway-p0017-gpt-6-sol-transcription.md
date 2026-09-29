$\alpha u(0,y)=0$ for all $y$ in $\mathcal X$. This and similar reasoning shows that for a semi-inner product $u$,

(e) $u(x,0)=u(0,y)=0$ for all $x,y$ in $\mathcal X$.

In particular, $u(0,0)=0$.

An *inner product* on $\mathcal X$ is a semi-inner product that also satisfies the following:

(f) If $u(x,x)=0$, then $x=0$.

An inner product in this book will be denoted by

$$
\langle x,y\rangle=u(x,y).
$$

There is no universally accepted notation for an inner product and the reader will often see $(x,y)$ and $(x\mid y)$ used in the literature.

**1.2. Example.** Let $\mathcal X$ be the collection of all sequences $\{\alpha_n:n\geqslant 1\}$ of scalars $\alpha_n$ from $\mathbb F$ such that $\alpha_n=0$ for all but a finite number of values of $n$. If addition and scalar multiplication are defined on $\mathcal X$ by

$$
\begin{aligned}
\{\alpha_n\}+\{\beta_n\}&\equiv\{\alpha_n+\beta_n\},\\
\alpha\{\alpha_n\}&=\{\alpha\alpha_n\},
\end{aligned}
$$

then $\mathcal X$ is a vector space over $\mathbb F$.

If $u(\{\alpha_n\},\{\beta_n\})\equiv\sum_{n=1}^{\infty}\alpha_{2n}\overline{\beta}_{2n}$, then $u$ is a semi-inner product that is not an inner product. On the other hand,

$$
\langle\{\alpha_n\},\{\beta_n\}\rangle
=\sum_{n=1}^{\infty}\alpha_n\overline{\beta}_n,
$$

$$
\langle\{\alpha_n\},\{\beta_n\}\rangle
=\sum_{n=1}^{\infty}\frac{1}{n}\alpha_n\overline{\beta}_n,
$$

$$
\langle\{\alpha_n\},\{\beta_n\}\rangle
=\sum_{n=1}^{\infty}n^5\alpha_n\overline{\beta}_n,
$$

all define inner products on $\mathcal X$.

**1.3. Example.** Let $(X,\Omega,\mu)$ be a measure space consisting of a set $X$, a $\sigma$-algebra $\Omega$ of subsets of $X$, and a countably additive measure $\mu$ defined on $\Omega$ with values in the non-negative extended real numbers. If $f$ and $g\in L^2(\mu)\equiv L^2(X,\Omega,\mu)$, then Hölder’s inequality implies $f\overline g\in L^1(\mu)$. If

$$
\langle f,g\rangle=\int f\overline g\,d\mu,
$$

then this defines an inner product on $L^2(\mu)$.

Note that Hölder’s inequality also states that $\left|\int f\overline g\,d\mu\right|\leqslant\left[\int|f|^2\,d\mu\right]^{1/2}\left[\int|g|^2\,d\mu\right]^{1/2}$. This is, in fact, a consequence of the following result on semi-inner products.
