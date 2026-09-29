$\{A_n\}$ is a sequence in $\mathcal{B}(\mathcal{X},\mathcal{Y})$ with the property that for every $x$ in $\mathcal{X}$ there is a $y$ in $\mathcal{Y}$ such that $\|A_nx-y\|\to 0$, then there is an $A$ in $\mathcal{B}(\mathcal{X},\mathcal{Y})$ such that $\|A_nx-Ax\|\to 0$ for every $x$ in $\mathcal{X}$ and $\sup_n\|A_n\|<\infty$.

**Proof.** If $x\in\mathcal{X}$, let $Ax=\lim_{n\to\infty}A_nx$. By hypothesis $A:\mathcal{X}\to\mathcal{Y}$ is defined and it is easy to see that it is linear. To show that $A$ is bounded, note that the PUB implies that there is a constant $M>0$ such that $\|A_n\|\leq M$ for all $n$. If $x\in\mathcal{X}$ and $\|x\|\leq 1$, then for any $n\geq 1$, $\|Ax\|\leq\|Ax-A_nx\|+\|A_nx\|\leq\|Ax-A_nx\|+M$. Letting $n\to\infty$ shows that $\|Ax\|\leq M$ whenever $\|x\|\leq 1$. $\blacksquare$

The Banach–Steinhaus Theorem is a result about sequences, not nets. Note that if $I$ is the identity operator on $\mathcal{X}$ and for each $n\geq 1$, $A_n=n^{-1}I$ and for $n\leq 0$, $A_n=nI$, then $\{A_n:n\in\mathbb{Z}\}$ is a countable net that converges in norm to $0$, but the net is not bounded.

**14.7. Proposition.** *Let $X$ be locally compact and let $\{f_n\}$ be a sequence in $C_0(X)$. Then $\int f_n\,d\mu\to\int f\,d\mu$ for every $\mu$ in $M(X)$ if and only if $\sup_n\|f_n\|<\infty$ and $f_n(x)\to f(x)$ for every $x$ in $X$.*

**Proof.** Suppose $\int f_n\,d\mu\to\int f\,d\mu$ for every $\mu$ in $M(X)$. Since $M(X)=C_0(X)^*$, (14.3) implies that $\sup_n\|f_n\|<\infty$. By letting $\mu=\delta_x$, the unit point mass at $x$, we see that $\int f_n\,d\delta_x=f_n(x)\to f(x)$. The converse follows by the Lebesgue Dominated Convergence Theorem. $\blacksquare$

## Exercises

1. Here is another proof of the PUB using the Baire Category Theorem. With the notation of (14.1), let $B_n\equiv\{x\in\mathcal{X}:\|Ax\|\leq n\text{ for all }A\text{ in }\mathcal{A}\}$. By hypothesis, $\bigcup_{n=1}^{\infty}B_n=\mathcal{X}$. Now apply the Baire Category Theorem.

2. If $1<p<\infty$ and $\{x_n\}\subseteq l^p$, then $\sum_{j=1}^{\infty}x_n(j)y(j)\to 0$ for every $y$ in $l^q$, $1/p+1/q=1$, if and only if $\sup_n\|x_n\|_p<\infty$ and $x_n(j)\to 0$ for every $j\geq 1$.

3. If $\{x_n\}\subseteq l^1$, then $\sum_{j=1}^{\infty}x_n(j)y(j)\to 0$ for every $y$ in $c_0$ if and only if $\sup_n\|x_n\|_1<\infty$ and $x_n(j)\to 0$ for every $j\geq 1$.

4. If $(X,\Omega,\mu)$ is a measure space, $1<p<\infty$, and $\{f_n\}\subseteq L^p(X,\Omega,\mu)$, then $\int f_ng\,d\mu\to 0$ for every $g$ in $L^q(\mu)$, $1/p+1/q=1$, if and only if $\sup\{\|f_n\|_p:n\geq 1\}<\infty$ and for every set $E$ in $\Omega$ with $\mu(E)<\infty$, $\int_E f_n\,d\mu\to 0$ as $n\to\infty$.

5. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\{f_n\}$ is a sequence in $L^1(X,\Omega,\mu)$, then $\int f_ng\,d\mu\to 0$ for every $g$ in $L^\infty(\mu)$ if and only if $\sup\{\|f_n\|_1:n\geq 1\}<\infty$ and $\int_E f_n\,d\mu\to 0$ for every $E$ in $\Omega$.

6. Let $\mathcal{H}$ be a Hilbert space and let $\mathcal{E}$ be an orthonormal basis for $\mathcal{H}$. Show that a sequence $\{h_n\}$ in $\mathcal{H}$ satisfies $\langle h_n,h\rangle\to 0$ for every $h$ in $\mathcal{H}$ if and only if $\sup\{\|h_n\|:n\geq 1\}<\infty$ and $\langle h_n,e\rangle\to 0$ for every $e$ in $\mathcal{E}$.

7. If $X$ is locally compact and $\{\mu_n\}$ is a sequence in $M(X)$, then $L(\mu_n)\to 0$ for every $L$ in $M(X)^*$ if and only if $\sup\{\|\mu_n\|:n\geq 1\}<\infty$ and $\mu_n(E)\to 0$ for every Borel set $E$.

8. In (14.6), show that $\|A\|\leq\liminf\|A_n\|$.
