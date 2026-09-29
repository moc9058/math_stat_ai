$\mu$. Hence $\rho(\bar u_i)\rightarrow\tilde{\rho}(\bar\phi)$. But $\rho(u_i)^*=\rho(\bar u_i)$ since $\rho$ is a *-homomorphism. Thus $\tilde{\rho}(\phi)^*=\tilde{\rho}(\bar\phi)$ and $\tilde{\rho}$ is a representation.

For any Borel subset $\Delta$ of $X$ let $E(\Delta)\equiv\tilde{\rho}(\chi_\Delta)$. We want to show that $E$ is a spectral measure. Since $\chi_\Delta$ is a hermitian idempotent in $B(X)$, $E(\Delta)$ is a projection by (1.17). Since $\chi_\square=0$ and $\chi_X=1$, $E(\square)=0$ and $E(X)=1$. Also, $E(\Delta_1\cap\Delta_2)=\tilde{\rho}(\chi_{\Delta_1\cap\Delta_2})=\tilde{\rho}(\chi_{\Delta_1}\chi_{\Delta_2})=E(\Delta_1)E(\Delta_2)$. Now let $\{\Delta_n\}$ be a pairwise disjoint sequence of Borel sets and put $\Lambda_n=\bigcup_{k=n+1}^{\infty}\Delta_k$. It is easy to see that $E$ is finitely additive so if $h\in\mathcal H$, then

$$
\begin{aligned}
\left\|E\left(\bigcup_{k=1}^{\infty}\Delta_k\right)h-\sum_{k=1}^{n}E(\Delta_k)h\right\|^2
&=\langle E(\Lambda_n)h,E(\Lambda_n)h\rangle\\
&=\langle E(\Lambda_n)h,h\rangle\\
&=\langle\tilde{\rho}(\chi_{\Lambda_n})h,h\rangle\\
&=\int\chi_{\Lambda_n}\,d\mu_{h,h}\\
&=\sum_{k=n+1}^{\infty}\mu_{h,h}(\Delta_k)\rightarrow 0
\end{aligned}
$$

as $n\rightarrow\infty$. Therefore $E$ is a spectral measure.

It remains to show that $\rho(u)=\int u\,dE$. It will be shown that $\tilde{\rho}(\phi)=\int\phi\,dE$ for every $\phi$ in $B(X)$. Fix $\phi$ in $B(X)$ and $\varepsilon>0$. If $\{\Delta_1,\ldots,\Delta_n\}$ is any Borel partition of $X$ such that $\sup\{|\phi(x)-\phi(x')|:x,x'\in\Delta_k\}<\varepsilon$ for $1\leqslant k\leqslant n$, then $\left\|\phi-\sum_{k=1}^{n}\phi(x_k)\chi_{\Delta_k}\right\|_\infty<\varepsilon$ for any choice of $x_k$ in $\Delta_k$. Since $\|\tilde{\rho}\|=1$, $\varepsilon>\left\|\tilde{\rho}(\phi)-\sum_{k=1}^{n}\phi(x_k)E(\Delta_k)\right\|$. This implies that $\tilde{\rho}(\phi)=\int\phi\,dE$ for any $\phi$ in $B(X)$.

The proof of the uniqueness of $E$ is left to the reader. ■

## EXERCISES

1. Prove Proposition 1.3.

2. Show that ball $\mathcal B(\mathcal H)$ is WOT compact.

3. Show that $\operatorname{Re}\mathcal B(\mathcal H)$ and $\mathcal B(\mathcal H)_1$ are WOT and SOT closed.

4. If $L:\mathcal B(\mathcal H)\rightarrow\mathbb C$ is a linear functional, show that the following statements are equivalent: (a) $L$ is SOT-continuous; (b) $L$ is WOT-continuous; (c) there are vectors $h_1,\ldots,h_n,g_1,\ldots,g_n$ in $\mathcal H$ such that $L(A)=\sum_{j=1}^{n}\langle Ah_j,g_j\rangle$.

5. Show that a convex subset of $\mathcal B(\mathcal H)$ is WOT closed if and only if it is SOT closed.

6. Verify the statement in Example 1.5.

7. Verify the statements made in Examples 1.6, 1.7, and 1.8.

8. For the spectral measures in (1.6), (1.7), and (1.8), give the corresponding representations.

9. If $\{E_i\}$ is a net of projections and $E$ is a projection, show that $E_i\rightarrow E$ (WOT) if and only if $E_i\rightarrow E$ (SOT).
