3. Suppose $\{e_1,e_2,\ldots\}$ is an orthonormal basis for $\mathcal H$ and for each $n$ there is a vector $Ae_n$ in $\mathcal H$ such that $\sum\|Ae_n\|<\infty$. Show that $A$ has an unique extension to a bounded operator on $\mathcal H$.

4. Proposition 1.2 says that $d(A,B)=\|A-B\|$ is a metric on $\mathcal B(\mathcal H,\mathcal H)$. Show that $\mathcal B(\mathcal H,\mathcal H)$ is complete relative to this metric.

5. Show that a multiplication operator $M_\phi$ (1.5) satisfies $M_\phi^2=M_\phi$ if and only if $\phi$ is a characteristic function.

6. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $k_1,k_2$ be two kernels satisfying the hypothesis of (1.6). Define

   $$k:X\times X\to\mathbb F\quad\text{by}\quad k(x,y)=\int k_1(x,z)k_2(z,y)\,d\mu(z).$$

   (a) Show that $k$ also satisfies the hypothesis of (1.6). (b) If $K,K_1,K_2$ are the integral operators with kernels $k,k_1,k_2$, show that $K=K_1K_2$. What does this remind you of? Is more going on than an analogy?

7. If $(X,\Omega,\mu)$ is a measure space and $k\in L^2(\mu\times\mu)$, show that $k$ defines a bounded integral operator.

8. Let $\{e_n\}$ be the usual basis for $l^2$ and let $\{\alpha_n\}$ be a sequence of scalars. Show that there is a bounded operator $A$ on $l^2$ such that $Ae_n=\alpha_ne_n$ for all $n$ if and only if $\{\alpha_n\}$ is uniformly bounded, in which case $\|A\|=\sup\{|\alpha_n|:n\geqslant1\}$. This type of operator is called a *diagonal operator* or is said to be *diagonalizable*.

9. (Schur test) Let $\{\alpha_{ij}\}_{i,j=1}^{\infty}$ be an infinite matrix such that $\alpha_{ij}\geqslant0$ for all $i,j$ and such that there are scalars $p_i>0$ and $\beta,\gamma>0$ with

   $$\sum_{i=1}^{\infty}\alpha_{ij}p_i\leqslant\beta p_j,$$

   $$\sum_{j=1}^{\infty}\alpha_{ij}p_j\leqslant\gamma p_i$$

   for all $i,j\geqslant1$. Show that there is an operator $A$ on $l^2(\mathbb N)$ with $\langle Ae_j,e_i\rangle=\alpha_{ij}$ and $\|A\|^2\leqslant\beta\gamma$.

10. (Hilbert matrix) Show that $\langle Ae_j,e_i\rangle=(i+j+1)^{-1}$ for $0\leqslant i,j<\infty$ defines a bounded operator on $l^2(\mathbb N\cup\{0\})$ with $\|A\|\leqslant\pi$. (See also Choi [1983] and Redheffer and Volkmann [1983].)

11. If $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, put $\alpha=[|a|^2+|b|^2+|c|^2+|d|^2]^{1/2}$ and show that $\|A\|=$

    $$\frac12\bigl(\alpha^2+\sqrt{\alpha^4-4\delta^2}\bigr),$$

    where $\delta^2=\det A^*A$.

12. (Direct sum of operators) Let $\{\mathcal H_i\}$ be a collection of Hilbert spaces and let $\mathcal H=\bigoplus_i\mathcal H_i$. Suppose $A_i\in\mathcal B(\mathcal H_i)$ for all $i$. Show that there is a bounded operator $A$ on $\mathcal H$ such that $A|_{\mathcal H_i}=A_i$ for all $i$ if and only if $\sup_i\|A_i\|<\infty$. In this case, $\|A\|=\sup_i\|A_i\|$. The operator $A$ is called the direct sum of the operators $\{A_i\}$ and is denoted by $A=\bigoplus_i A_i$.
