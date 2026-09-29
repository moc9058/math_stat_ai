**3.4. Example.** If $\mathcal H$ is a Hilbert space and $A\in\mathcal B(\mathcal H)$, then
$\sigma_l(A)=\{\alpha\in\mathbb F:\inf\{\|(A-\alpha)h\|:\|h\|=1\}=0\}$. In fact, suppose $B\in\mathcal B(\mathcal H)$ such that $B(A-\alpha)=1$. If $\|h\|=1$, then $1=\|h\|=\|B(A-\alpha)h\|\leq\|B\|\|(A-\alpha)h\|$. So $\|(A-\alpha)h\|\geq\|B\|^{-1}$ whenever $\|h\|=1$.

Conversely, suppose $\|(A-\alpha)h\|\geq\delta>0$ whenever $\|h\|=1$. Note that $\ker(A-\alpha)=(0)$. It will now be shown that $\operatorname{ran}(A-\alpha)$ is closed. In fact, assume that $(A-\alpha)f_n\to g$. Then $\delta\|f_n-f_m\|\leq\|(A-\alpha)(f_n-f_m)\|=\|(A-\alpha)f_n-(A-\alpha)f_m\|$. Thus $\{f_n\}$ is a Cauchy sequence. Let $f_n\to f$. Then $g=\lim(A-\alpha)f_n=(A-\alpha)f$; hence $g\in\operatorname{ran}(A-\alpha)$. Let $\mathcal K=\operatorname{ran}(A-\alpha)$; so $(A-\alpha):\mathcal H\to\mathcal K$ is a bijection. Thus $(A-\alpha)^{-1}:\mathcal K\to\mathcal H$ is bounded. Define $B:\mathcal H\to\mathcal H$ by letting $B(k+h)=(A-\alpha)^{-1}k$ when $k\in\mathcal K$ and $h\in\mathcal K^\perp$. Thus $B\in\mathcal B(\mathcal H)$ and $B(A-\alpha)=1$.

**3.5. Example.** If $\mathcal A=M_2(\mathbb R)$ and $A=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$, then $\sigma(A)=\square$. In fact, $A-\alpha$ is not invertible if and only if $0=\det(A-\alpha)=\alpha^2+1$, which is impossible in $\mathbb R$.

The phenomenon of the last example does not occur if $\mathcal A$ is a Banach algebra over $\mathbb C$.

**3.6. Theorem.** *If $\mathcal A$ is a Banach algebra over $\mathbb C$ with an identity, then for each $a$ in $\mathcal A$, $\sigma(a)$ is a nonempty compact subset of $\mathbb C$. Moreover, if $|\alpha|>\|a\|$, $\alpha\notin\sigma(a)$ and $z\mapsto(z-a)^{-1}$ is an $\mathcal A$-valued analytic function defined on $\rho(a)$.*

Before beginning the proof, a few words on vector-valued analytic functions are in order. If $G$ is a region in $\mathbb C$ and $\mathcal X$ is a Banach space, define the derivative of $f:G\to\mathcal X$ at $z_0$ to be $\lim_{h\to0}h^{-1}[f(z_0+h)-f(z_0)]$ if the limit exists. Say that $f$ is analytic if $f$ has a continuous derivative on $G$. The whole theory of analytic functions transfers to this situation. The statements and proofs of such theorems as Cauchy’s Integral Formula, Liouville’s Theorem, etc., transfer verbatim. Also, $f:G\to\mathcal X$ is analytic if and only if for each $z_0$ in $G$ there is a sequence $x_0,x_1,x_2,\ldots$ in $\mathcal X$ such that $f(z)=\sum_{k=0}^{\infty}(z-z_0)^kx_k$ whenever $z\in B(z_0;r)$, where $r=\operatorname{dist}(z_0,\partial G)$. Moreover, the convergence is uniform on compact subsets of $B(z_0;r)$.

There is also a way of obtaining the vector-valued case as a consequence of the scalar-valued case (see Exercise 4).

**Proof of Theorem 3.6.** If $|\alpha|>\|a\|$, then $\alpha-a=\alpha(1-a/\alpha)$ and $\|a/\alpha\|<1$. By Corollary 2.3, $(1-a/\alpha)$ is invertible. Hence $\alpha-a$ is invertible and so $\alpha\notin\sigma(a)$. Thus $\sigma(a)\subseteq\{\alpha\in\mathbb C:|\alpha|\leq\|a\|\}$ and $\sigma(a)$ is bounded.

Let $G$ be the set of invertible elements of $\mathcal A$. The map $\alpha\mapsto(\alpha-a)$ is a continuous function of $\mathbb C\to\mathcal A$. Since $G$ is open and $\rho(a)$ is the inverse image of $G$ under this map, $\rho(a)$ is open. Thus $\sigma(a)=\mathbb C\setminus\rho(a)$ is compact.

Define $F:\rho(a)\to\mathcal A$ by $F(z)=(z-a)^{-1}$. In the identity $x^{-1}-y^{-1}=$
