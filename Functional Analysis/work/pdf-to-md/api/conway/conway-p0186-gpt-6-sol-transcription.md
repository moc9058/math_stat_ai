$n$, $\alpha_{mn}\to 0$ as $m\to\infty$. Conversely, if $\{\alpha_{mn}:m,n\geqslant 1\}$ are scalars satisfying (a) and (b), then

$$
(Ax)(m)=\sum_{n=1}^{\infty}\alpha_{mn}x(n)
$$

defines a bounded operator $A$ on $c_0$ and $\|A\|=M$. Find $A^*$.

8. Let $A\in\mathcal B(l^1)$ and for $n\geqslant 1$ define $e_n$ in $l^1$ by $e_n(n)=1$, $e_n(m)=0$ for $m\neq n$. Put $\alpha_{mn}=(Ae_n)(m)$ for $m,n\geqslant 1$. Prove: (a) $M\equiv\sup_n\sum_{m=1}^{\infty}|\alpha_{mn}|<\infty$; (b) for every $m$, $\sup_n|\alpha_{mn}|<\infty$. Conversely, if $\{\alpha_{mn}:m,n\geqslant 1\}$ are scalars satisfying (a) and (b), then

$$
(Af)(m)=\sum_{n=1}^{\infty}\alpha_{mn}f(n)
$$

defines a bounded operator $A$ on $l^1$ and $\|A\|=M$. Find $A^*$.

9. (Bonsall [1986]) Let $\mathcal X$ be a Banach space, $Z$ a nonempty set, and $u:Z\to\mathcal X$. If there are positive constants $M_1$ and $M_2$ such that (i) $\|u(z)\|\leqslant M_1$ for all $z$ in $Z$ and (ii) for every $x^*$ in $\mathcal X^*$, $\sup\{|\langle u(z),x^*\rangle|:z\in Z\}\geqslant M_2\|x^*\|$; then for every $x$ in $\mathcal X$ there is an $f$ in $l^1(Z)$ such that $(*)\ x=\sum\{f(z)u(z):z\in Z\}$ and $M_2\inf\|f\|_1\leqslant\|x\|\leqslant M_1\inf\|f\|_1$, where the infimum is taken over all $f$ in $l^1(Z)$ such that $(*)$ holds. (Hint: define $T:l^1(Z)\to\mathcal X$ by $Tf=\sum\{f(z)u(z):z\in Z\}$.)

10. (Bonsall [1986]) Let $m$ be normalized Lebesgue measure on $\partial\mathbf D$ and for $|z|<1$ and $|w|=1$ let $p_z(w)=(1-|z|^2)/|1-\bar zw|^2$. So $p_z$ is the Poisson kernel. Show that if $f\in L^1(m)$, then there is a sequence $\{z_n\}\subseteq\mathbf D$ and a sequence $\{\lambda_n\}$ in $l^1$ such that $(*)\ f=\sum_{n=1}^{\infty}\lambda_np_{z_n}$. Moreover, $\|f\|_1=\inf\sum_{n=1}^{\infty}|\lambda_n|$, where the infimum is taken over all $\{\lambda_n\}$ in $l^1$ such that $(*)$ holds. (Hint: use Exercise 9.)

11. If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $B\in\mathcal B(\mathcal Y^*,\mathcal X^*)$, then there is an operator $A$ in $\mathcal B(\mathcal X,\mathcal Y)$ such that $B=A^*$ if and only if $B$ is wk*-continuous.

12. If $\mathcal X$ is a Banach space and $\mathcal M$ and $\mathcal N$ are closed subspaces, show that the following statements are equivalent. (a) $\mathcal M+\mathcal N$ is closed. (b) the range of the linear transformation $x\to(x+\mathcal M)\oplus(x+\mathcal N)$ from $\mathcal X$ into $\mathcal X/\mathcal M\oplus\mathcal X/\mathcal N$ is closed. (c) $\mathcal M^\perp+\mathcal N^\perp$ is norm closed in $\mathcal X^*$; (d) $\mathcal M^\perp+\mathcal N^\perp$ is weak* closed in $\mathcal X^*$.

## §2*. The Banach–Stone Theorem

As an application of the adjoint of a linear map, the isometries between spaces of the form $C(X)$ and $C(Y)$ will be characterized. Note that if $X$ and $Y$ are compact spaces, $\tau:Y\to X$ is continuous map, and $Af=f\circ\tau$ for $f$ in $C(X)$, then (III.2.4) $A$ is a bounded linear map and $\|A\|=1$. Moreover, $A$ is an isometry if and only if $\tau$ is surjective. If $A$ is a surjective isometry, then $\tau$ must be a homeomorphism. Indeed, suppose $A$ is a surjective isometry; it must be shown that $\tau$ is injective. If $y_0,y_1\in Y$ and $y_0\neq y_1$, then there is a $g$
