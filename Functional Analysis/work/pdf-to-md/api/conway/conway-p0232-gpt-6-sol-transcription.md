The next result has a number of applications in the theory of integral equations.

**7.9. The Fredholm Alternative.** *If $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\in\mathbb{C}$, and $\lambda\neq 0$, then $\operatorname{ran}(A-\lambda)$ is closed and $\dim\ker(A-\lambda)=\dim\ker(A-\lambda)^*<\infty$.*

**Proof.** It suffices to assume that $\lambda\in\sigma(A)$. Put $\Delta=\sigma(A)\setminus\{\lambda\}$, $\mathcal{X}_\lambda=E(\lambda)\mathcal{X}$, $\mathcal{X}_\Delta=E(\Delta)\mathcal{X}$, $A_\lambda=A|_{\mathcal{X}_\lambda}$, and $A_\Delta=A|_{\mathcal{X}_\Delta}$. Now $\lambda\notin\Delta=\sigma(A_\Delta)$, so $A_\Delta-\lambda$ is invertible. Thus $\operatorname{ran}(A_\Delta-\lambda)=\mathcal{X}_\Delta$. Hence $\operatorname{ran}(A-\lambda)=(A-\lambda)\mathcal{X}_\lambda+(A-\lambda)\mathcal{X}_\Delta=\operatorname{ran}(A_\lambda-\lambda)+\mathcal{X}_\Delta$. Since $\dim\mathcal{X}_\lambda<\infty$, $\operatorname{ran}(A-\lambda)$ is closed (III.4.3).

Also note that

$$
\begin{aligned}
\mathcal{X}/\operatorname{ran}(A-\lambda)
&=(\mathcal{X}_\Delta+\mathcal{X}_\lambda)/
[\operatorname{ran}(A_\lambda-\lambda)+\mathcal{X}_\Delta]\\
&\approx\mathcal{X}_\lambda/\operatorname{ran}(A_\lambda-\lambda).
\end{aligned}
$$

Since $\dim\mathcal{X}_\lambda<\infty$, $\dim[\mathcal{X}/\operatorname{ran}(A-\lambda)]=\dim\mathcal{X}_\lambda-\dim\operatorname{ran}(A_\lambda-\lambda)=\dim\ker(A_\lambda-\lambda)=\dim\ker(A-\lambda)<\infty$ since $\ker(A-\lambda)\subseteq\mathcal{X}_\lambda$ (7.8). But $[\mathcal{X}/\operatorname{ran}(A-\lambda)]^*=[\operatorname{ran}(A-\lambda)]^\perp$ (III.10.2) $=\ker(A-\lambda)^*$. Hence $\dim\ker(A-\lambda)=\dim\ker(A-\lambda)^*$. $\blacksquare$

**7.10. Corollary.** *If $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\in\mathbb{C}$, and $\lambda\neq 0$, then for every $y$ in $\mathcal{X}$ there is an $x$ in $\mathcal{X}$ such that*

$$
(A-\lambda)x=y \tag{7.11}
$$

*if and only if the only vector $x$ such that $(A-\lambda)x=0$ is $x=0$. If this condition is satisfied, then the solution to (7.11) is unique.*

This corollary is a rephrasing of part of the Fredholm Alternative together with the fact that an operator has dense range if and only if its adjoint has a trivial kernel.

The applications of the Fredholm Alternative occur by taking the compact operator to be an integral operator.

## Exercises

1. If $\mathcal{M},\mathcal{N}$ are finite dimensional spaces and $\mathcal{M}\leq\mathcal{N}$, $\mathcal{M}\neq\mathcal{N}$, then there is a $y$ in $\mathcal{N}$ such that $\|y\|=1$ and $\operatorname{dist}(y,\mathcal{M})=1$.

2. Let $A\in\mathcal{B}(\mathcal{X})$ and let $\lambda_1,\ldots,\lambda_n$ be distinct points in $\sigma_p(A)$. If $x_k\in\ker(A-\lambda_k)$, $1\leq k\leq n$, and $x_k\neq 0$, show that $\{x_1,\ldots,x_n\}$ is a linearly independent set.

3. Let $\mathcal{X}_1,\mathcal{X}_2,\ldots$ be Banach spaces and put $\mathcal{X}=\bigoplus_p\mathcal{X}_n$. Let $A_n\in\mathcal{B}(\mathcal{X}_n)$ such that $\sup_n\|A_n\|<\infty$ and define $A:\mathcal{X}\to\mathcal{X}$ by $A\{x_n\}=\{A_nx_n\}$. Show that $A\in\mathcal{B}(\mathcal{X})$ and $\|A\|=\sup_n\|A_n\|$. Show that $A\in\mathcal{B}_0(\mathcal{X})$ if and only if each $A_n\in\mathcal{B}_0(\mathcal{X})$ and $\lim\|A_n\|=0$.

4. Suppose $A\in\mathcal{B}(\mathcal{X})$ and there is a polynomial $p$ such that $p(A)\in\mathcal{B}_0(\mathcal{X})$. What can be said about $\sigma(A)$?
