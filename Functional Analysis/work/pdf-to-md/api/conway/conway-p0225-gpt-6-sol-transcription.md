*then $\sigma(T)=\operatorname{cl}\mathbb D$ and for $|\lambda|<1$, $\ker(T-\lambda)$ is the one-dimensional space spanned by the vector $(1,\lambda,\lambda^2,\ldots)$.*

The next result shows that if $S$ is as in (6.5), then $\partial\mathbb D\subseteq\sigma_{ap}(S)$.

**6.7. Proposition.** If $A\in\mathcal B(\mathcal X)$, then $\partial\sigma(A)\subseteq\sigma_{ap}(A)$.

**PROOF.** Let $\lambda\in\partial\sigma(A)$ and let $\{\lambda_n\}\subseteq\mathbb C\setminus\sigma(A)$ such that $\lambda_n\to\lambda$.

**6.8. Claim.** $\|(A-\lambda_n)^{-1}\|\to\infty$ as $n\to\infty$.

In fact, if the claim were false, then by passing to a subsequence if necessary, it follows that there is a constant $M$ such that $\|(A-\lambda_n)^{-1}\|\leq M$ for all $n$. Choose $n$ sufficiently large that $|\lambda_n-\lambda|<M^{-1}$. Then $\|(A-\lambda)-(A-\lambda_n)\|<\|(A-\lambda_n)^{-1}\|^{-1}$. By (2.3b), this implies that $(A-\lambda)$ is invertible, a contradiction. This establishes (6.8).

Let $\|x_n\|=1$ such that $\alpha_n\equiv\|(A-\lambda_n)^{-1}x_n\|>\|(A-\lambda_n)^{-1}\|-n^{-1}$, so $\alpha_n\to\infty$. Put $y_n=\alpha_n^{-1}(A-\lambda_n)^{-1}x_n$; hence $\|y_n\|=1$. Now

$$
\begin{aligned}
(A-\lambda)y_n&=(A-\lambda_n)y_n+(\lambda-\lambda_n)y_n\\
&=\alpha_n^{-1}x_n+(\lambda-\lambda_n)y_n.
\end{aligned}
$$

Thus $\|(A-\lambda)y_n\|\leq\alpha_n^{-1}+|\lambda-\lambda_n|$, so that $\|(A-\lambda)y_n\|\to0$ as $n\to\infty$. That is, $\lambda\in\sigma_{ap}(A)$. $\blacksquare$

Let $A\in\mathcal B(\mathcal X)$ and suppose $\Delta$ is a *clopen* subset of $\sigma(A)$; that is, $\Delta$ is a subset of $\sigma(A)$ that is both closed and relatively open. So $\sigma(A)=\Delta\cup(\sigma(A)\setminus\Delta)$. As in Proposition 4.11 (and Exercise 4.9),

$$
E(\Delta)=E(\Delta;A)=\frac{1}{2\pi i}\int_\Gamma(z-A)^{-1}\,dz, \tag{6.9}
$$

where $\Gamma$ is a positively oriented Jordan system such that $\Delta\subseteq\operatorname{ins}\Gamma$ and $\sigma(A)\setminus\Delta\subseteq\operatorname{out}\Gamma$, is an idempotent. Moreover, $E(\Delta)B=BE(\Delta)$ whenever $AB=BA$ and if $\mathcal X_\Delta=E(\Delta)\mathcal X$, $\sigma(A|_{\mathcal X_\Delta})=\Delta$. Call $E(\Delta)$ the *Riesz idempotent* corresponding to $\Delta$. If $\Delta$ is a singleton set $\{\lambda\}$, let $E(\lambda)=E(\{\lambda\})$ and $\mathcal X_\lambda=\mathcal X_{\{\lambda\}}$. Note that if $\lambda$ is an isolated point of $\sigma(A)$, then $\{\lambda\}$ is a clopen subset of $\sigma(A)$.

**6.10. Example.** Let $\{\alpha_n\}\in l^\infty$, $1\leq p\leq\infty$, and define $A:l^p\to l^p$ by $(Ax)(n)=\alpha_nx(n)$. Then $\sigma(A)=\operatorname{cl}\{\alpha_n\}$ and $\sigma_p(A)=\{\alpha_n\}$. For each $k$, define $N_k=\{n\in\mathbb N;\ \alpha_n=\alpha_k\}$ and define $P_k:l^p\to l^p$ by $P_kx=\chi_{N_k}x$. If $\alpha_k$ is an isolated point of $\sigma(A)$, then $\{\alpha_k\}$ is a clopen subset of $\sigma(A)$ and $E(\{\alpha_k\};A)=P_k$.

Suppose $A\in\mathcal B(\mathcal X)$ and $\lambda_0$ is an isolated point in $\sigma(A)$. Hence $E(\lambda_0)=E(\lambda_0;A)$ is a well-defined idempotent. Also, $\lambda_0$ is an isolated singularity of the analytic function $z\mapsto(z-A)^{-1}$ on $\mathbb C\setminus\sigma(A)$. Perhaps the nature of this singularity (pole
