$$
\begin{aligned}
&\leqslant \|f\|^2\sum_k\sum_m\bigl|\langle Ke_m,e_k\rangle-\langle KP_ne_m,P_ne_k\rangle\\
&\qquad-\langle KP_ne_m,P_ne_k\rangle+\langle KP_ne_m,P_ne_k\rangle\bigr|^2\\
&=\sum_{k=n+1}^{\infty}\sum_{m=n+1}^{\infty}|\langle Ke_m,e_k\rangle|^2\\
&=\sum_{k=n+1}^{\infty}\sum_{m=n+1}^{\infty}|\langle k,\psi_{km}\rangle|^2.
\end{aligned}
$$

Since $\sum_{k,m}|\langle k,\psi_{km}\rangle|^2<\infty$, $n$ can be chosen sufficiently large such that for any $\varepsilon>0$ this last sum will be smaller than $\varepsilon^2$. Thus $\|K-K_n\|\to0$. $\blacksquare$

In particular, note that the preceding proposition shows that the Volterra operator (1.7) is compact.

One of the dominant tools in the study of linear transformation on finite dimensional spaces is the concept of eigenvalue.

**4.9. Definition.** If $A\in\mathcal B(\mathcal H)$, a scalar $\alpha$ is an *eigenvalue* of $A$ if $\ker(A-\alpha)\ne(0)$. If $h$ is a nonzero vector in $\ker(A-\alpha)$, $h$ is called an *eigenvector* for $\alpha$; thus $Ah=\alpha h$. Let $\sigma_p(A)$ denote the set of eigenvalues of $A$.

**4.10. Example.** Let $A$ be the diagonalizable operator in Proposition 4.6. Then $\sigma_p(A)=\{\alpha_1,\alpha_2,\ldots\}$. If $\alpha\in\sigma_p(A)$, let $J_\alpha=\{j\in\mathbb N:\alpha_j=\alpha\}$. Then $h$ is an eigenvector for $\alpha$ if and only if $h\in\bigvee\{e_j:j\in J_\alpha\}$.

**4.11. Example.** The Volterra operator has no eigenvalues.

**4.12. Example.** Let $h\in\mathcal H=L_{\mathbb C}^2(-\pi,\pi)$ and define $K:\mathcal H\to\mathcal H$ by $(Kf)(x)=(2\pi)^{-1/2}\int_{-\pi}^{\pi}h(x-y)f(y)\,dy$. If $\lambda_n=(2\pi)^{-1/2}\int_{-\pi}^{\pi}h(x)\exp(-inx)\,dx=\hat h(n)$, the $n$th Fourier coefficient of $h$, then $Ke_n=\lambda_ne_n$, where $e_n(x)=(2\pi)^{-1/2}\exp(-inx)$.

The way to see this is to extend functions in $L_{\mathbb C}^2(-\pi,\pi)$ to $\mathbb R$ by periodicity and perform a change of variables in the formula for $(Ke_n)(x)$. The details are left to the reader.

Operators on finite dimensional spaces over $\mathbb C$ always have eigenvalues. As the Volterra operator illustrates, the analogy between operators on finite dimensional spaces and compact operators breaks down here. If, however, a compact operator has an eigenvalue, several nice things can be said if the eigenvalue is not zero.

**4.13. Proposition.** *If $T\in\mathcal B_0(\mathcal H)$, $\lambda\in\sigma_p(T)$, and $\lambda\ne0$, then the eigenspace $\ker(T-\lambda)$ is finite dimensional.*

**Proof.** Suppose there is an infinite orthonormal sequence $\{e_n\}$ in $\ker(T-\lambda)$. Since $T$ is compact, there is a subsequence $\{e_{n_k}\}$ such that $\{Te_{n_k}\}$ converges.
