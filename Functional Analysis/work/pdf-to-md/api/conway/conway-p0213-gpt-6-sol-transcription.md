From complex variable theory, this power series converges for $|z|<R\equiv\operatorname{dist}(0,\partial G)=\operatorname{dist}(0,\sigma(a)^{-1})$ (Here $\sigma(a)^{-1}=\{z^{-1}:z\in\sigma(a)\}$). Thus $R=\inf\{|\alpha|:\alpha^{-1}\in\sigma(a)\}=r(a)^{-1}$. Also, from the theory of power series, $R^{-1}=\limsup\|a^n\|^{1/n}$. Thus

$$
r(a)=\limsup\|a^n\|^{1/n}.
$$

Now if $\alpha\in\mathbb C$ and $n\geqslant1$, $\alpha^n-a^n=(\alpha-a)(\alpha^{n-1}+\alpha^{n-2}a+\cdots+a^{n-1})=(\alpha^{n-1}+\alpha^{n-2}a+\cdots+a^{n-1})(\alpha-a)$. So if $\alpha^n-a^n$ is invertible, $\alpha-a$ is invertible and $(\alpha-a)^{-1}=(\alpha^n-a^n)^{-1}(\alpha^{n-1}+\cdots+a^{n-1})$. So for $\alpha$ in $\sigma(a)$, $\alpha^n-a^n$ is not invertible for every $n\geqslant1$. By Theorem 3.6, $|\alpha|^n\leqslant\|a^n\|$. Hence $|\alpha|\leqslant\|a^n\|^{1/n}$ for all $n\geqslant1$ and $\alpha$ in $\sigma(a)$. So if $\alpha\in\sigma(a)$, $|\alpha|\leqslant\liminf\|a^n\|^{1/n}$. Taking the supremum over all $\alpha$ in $\sigma(a)$ gives that $r(a)\leqslant\liminf\|a^n\|^{1/n}\leqslant\limsup\|a^n\|^{1/n}=r(a)$. So $r(a)=\lim\|a^n\|^{1/n}$. $\blacksquare$

**3.9. Proposition.** Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$.

(a) If $\alpha\in\rho(a)$, then $\operatorname{dist}(\alpha,\sigma(a))\geqslant\|(\alpha-a)^{-1}\|^{-1}$.

(b) If $\alpha,\beta\in\rho(a)$, then

$$
\begin{aligned}
(\alpha-a)^{-1}-(\beta-a)^{-1}
&=(\beta-\alpha)(\alpha-a)^{-1}(\beta-a)^{-1}\\
&=(\beta-\alpha)(\beta-a)^{-1}(\alpha-a)^{-1}.
\end{aligned}
$$

**Proof.** (a) By Corollary 2.3, if $\alpha\in\rho(a)$ and $\|x-(\alpha-a)\|<\|(\alpha-a)^{-1}\|^{-1}$, $x$ is invertible. So if $\beta\in\mathbb C$ and $|\beta|<\|(\alpha-a)^{-1}\|^{-1}$, $(\beta+\alpha-a)$ is invertible; that is, $\alpha+\beta\in\rho(a)$. Hence $\operatorname{dist}(\alpha,\sigma(a))\geqslant\|(\alpha-a)^{-1}\|^{-1}$. (b) This follows by letting $x=\alpha-a$ and $y=\beta-a$ in the identity $x^{-1}-y^{-1}=x^{-1}(y-x)y^{-1}=y^{-1}(y-x)x^{-1}$. $\blacksquare$

The identity in part (b) of the preceding proposition is called the *resolvent identity* and the function $\alpha\mapsto(\alpha-a)^{-1}$ of $\rho(a)\to\mathcal A$ is called the *resolvent* of $a$.

## Exercises

1. Let $S$ be the unilateral shift on $l^2$ (II.2.10). Show that $S$ is left invertible but not right invertible.

2. If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$ and is nilpotent (that is, $a^n=0$ for some $n$), then $\sigma(a)=\{0\}$.

3. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $\mathcal A=L^\infty(X,\Omega,\mu)$ (1.6). If $\phi\in\mathcal A$, show that the following are equivalent: (a) $\alpha\in\sigma(\phi)$; (b) $0=\sup\{\inf\{|\phi(x)-\alpha|:x\in X\setminus\Delta\}:\Delta\in\Omega\text{ and }\mu(\Delta)=0\}$; (c) if $\varepsilon>0$, $\mu(\{x\in X:|\phi(x)-\alpha|<\varepsilon\})>0$; (d) if $\nu$ is the measure defined on the Borel subsets of $\mathbb C$ by $\nu(\Delta)=\mu(\phi^{-1}(\Delta))$, then $\alpha$ is in the support of $\nu$.

4. If $G$ is an open subset of $\mathbb C$ and $f:G\to\mathcal X$ is a function such that for each $x^*$ in $\mathcal X^*$, $x^*\circ f:G\to\mathbb C$ is analytic, then $f$ is analytic. If the word “continuous” is substituted for both occurrences of the word “analytic”, is the preceding statement still true?
