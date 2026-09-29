(a) $\mu=m=$ normalized arc length on $\partial\mathbb D$;

(b) $V^{-1}=$ the Fourier transform on $L^2(m)=L^2(\partial\mathbb D)$.

8. Suppose $N_1,\ldots,N_d$ are normal operators such that $N_jN_k^*=N_k^*N_j$ for $1\leq j,k\leq d$ and suppose there is a vector $e_0$ in $\mathcal H$ such that $\mathcal H$ is the only subspace of $\mathcal H$ containing $e_0$ that reduces each of the operators $N_1,\ldots,N_d$. Show that there is a compactly supported measure $\mu$ on $\mathbb C^d$ and an isomorphism $V:\mathcal H\to L^2(\mu)$ such that $VN_kV^{-1}f=z_kf$ for $f$ in $L^2(\mu)$ and $1\leq k\leq d$ ($z_k=$ the $k$th coordinate function) (see Exercise 2.17).

## §4. Some Applications of the Spectral Theorem

In this section a few diverse applications of the Spectral Theorem are presented. These will show the power and finesse of the Spectral Theorem as well as demonstrate some of the methods used to apply it. One result in this section (Theorem 4.6) is more than an application. Indeed, many regard this as the optimal statement of the Spectral Theorem.

If $N$ is a normal operator and $N=\int z\,dE(z)$ is its spectral representation, then $\phi\mapsto\phi(N)\equiv\int\phi\,dE$ is a $*$-homomorphism of $B(\mathbb C)$ into $\mathcal B(\mathcal H)$. Thus, if $\phi,\psi\in B(\mathbb C)$, $(\int\phi\,dE)(\int\psi\,dE)=\int\phi\psi\,dE$ and $\|\int\phi\,dE\|\leq\sup\{|\phi(z)|:z\in\sigma(N)\}$.

**4.1. Proposition.** *If $N$ is a normal operator and $N=\int z\,dE(z)$, then $N$ is compact if and only if for every $\varepsilon>0$, $E(\{z:|z|>\varepsilon\})$ has finite rank.*

**Proof.** If $\varepsilon>0$, let $\Delta_\varepsilon=\{z:|z|>\varepsilon\}$ and $E_\varepsilon=E(\Delta_\varepsilon)$. Then

$$
\begin{aligned}
N-NE_\varepsilon
&=\int z\,dE(z)-\int z\chi_{\Delta_\varepsilon}(z)\,dE(z)\\
&=\int z\chi_{\mathbb C\setminus\Delta_\varepsilon}(z)\,dE(z)=\phi(N)
\end{aligned}
$$

where $\phi(z)=z\chi_{\mathbb C\setminus\Delta_\varepsilon}(z)$. Thus $\|N-NE_\varepsilon\|\leq\sup\{|z|:z\in\mathbb C\setminus\Delta_\varepsilon\}\leq\varepsilon$. If $E_\varepsilon$ has finite rank for every $\varepsilon>0$, then so does $NE_\varepsilon$. Thus $N\in\mathcal B_0(\mathcal H)$.

Now assume that $N$ is compact and let $\varepsilon>0$. Put $\phi(z)=z^{-1}\chi_{\Delta_\varepsilon}(z)$; so $\phi\in B(\mathbb C)$. Since $N$ is compact, so is $N\phi(N)$. But $N\phi(N)=\int zz^{-1}\chi_{\Delta_\varepsilon}(z)\,dE(z)=E_\varepsilon$. Since $E_\varepsilon$ is a compact projection, it must have finite rank. (Why?) $\blacksquare$

The preceding result could have been proved by using the fact that compact normal operators are diagonalizable and the eigenvalues must converge to 0.

**4.2. Theorem.** *If $\mathcal H$ is separable and $I$ is an ideal of $\mathcal B(\mathcal H)$ that contains a noncompact operator, then $I=\mathcal B(\mathcal H)$.*

**Proof.** If $A\in I$ and $A\notin\mathcal B_0(\mathcal H)$, consider $A^*A$; let $A^*A=\int t\,dE(t)$ ($\sigma(A^*A)\subseteq[0,\infty)$). By the preceding proposition, there is an $\varepsilon>0$ such that
