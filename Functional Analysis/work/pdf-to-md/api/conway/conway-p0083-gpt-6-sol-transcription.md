The proof of the first result is similar to that of Proposition I.3.1 and is left to the reader. [Also see (II.1.1).] $\mathcal{B}(\mathcal{X},\mathcal{Y})=$ all continuous linear transformations $A:\mathcal{X}\to\mathcal{Y}$.

**2.1. Proposition.** *If $\mathcal{X}$ and $\mathcal{Y}$ are normed spaces and $A:\mathcal{X}\to\mathcal{Y}$ is a linear transformation, the following statements are equivalent.*

(a) $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$.

(b) $A$ is continuous at $0$.

(c) $A$ is continuous at some point.

(d) There is a positive constant $c$ such that $\|Ax\|\leq c\|x\|$ for all $x$ in $\mathcal{X}$.

*If $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$ and*

$$
\|A\|=\sup\{\|Ax\|:\|x\|\leq 1\},
$$

*then*

$$
\begin{aligned}
\|A\|&=\sup\{\|Ax\|:\|x\|=1\}\\
&=\sup\{\|Ax\|/\|x\|:x\ne 0\}\\
&=\inf\{c>0:\|Ax\|\leq c\|x\|\text{ for }x\text{ in }\mathcal{X}\}.
\end{aligned}
$$

$\|A\|$ is called the *norm* of $A$ and $\mathcal{B}(\mathcal{X},\mathcal{Y})$ becomes a normed space if addition and scalar multiplication are defined pointwise. $\mathcal{B}(\mathcal{X},\mathcal{Y})$ is a Banach space if $\mathcal{Y}$ is a Banach space (Exercise 1). A continuous linear operator is also called a *bounded linear operator*.

The following examples are reminiscent of those that were given in Section II.1.

**2.2. Example.** If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\phi\in L^\infty(X,\Omega,\mu)$, define $M_\phi:L^p(X,\Omega,\mu)\to L^p(X,\Omega,\mu)$, $1\leq p\leq\infty$, by $M_\phi f=\phi f$ for all $f$ in $L^p(X,\Omega,\mu)$. Then $M_\phi\in\mathcal{B}(L^p(X,\Omega,\mu))$ and $\|M_\phi\|=\|\phi\|_\infty$.

**2.3. Example.** If $(X,\Omega,\mu)$, $k$, $c_1$, and $c_2$ are as in Example II.1.6 and $1\leq p\leq\infty$, then $K:L^p(\mu)\to L^p(\mu)$, defined by

$$
(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)
$$

for all $f$ in $L^p(\mu)$ and $x$ in $X$, is a bounded operator on $L^p(\mu)$ and $\|K\|\leq c_1^{1/q}c_2^{1/p}$, where $1/p+1/q=1$.

**2.4. Example.** If $X$ and $Y$ are compact spaces and $\tau:Y\to X$ is a continuous map, define $A:C(X)\to C(Y)$ by $(Af)(y)=f(\tau(y))$. Then $A\in\mathcal{B}(C(X),C(Y))$ and $\|A\|=1$.

## EXERCISES

1. Show that for $\mathcal{B}(\mathcal{X},\mathbb{F})\ne(0)$, $\mathcal{B}(\mathcal{X},\mathcal{Y})$ is a Banach space if and only if $\mathcal{Y}$ is a Banach space.
