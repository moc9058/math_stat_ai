**7.14. Proposition.** *If $T$ is a compact normal operator, then $T$ is positive if and only if all its eigenvalues are non-negative real numbers.*

**Proof.** Let $T=\sum_{1}^{\infty}\lambda_nP_n$. If $T\geq 0$ and $h\in P_n\mathcal H$ with $\|h\|=1$, then $Th=\lambda_nh$. Hence $\lambda_n=\langle Th,h\rangle\geq 0$. Conversely, assume each $\lambda_n\geq 0$. If $h\in\mathcal H$, $h=h_0+\sum_{n=1}^{\infty}h_n$, where $h_0\in\ker T$ and $h_n\in P_n\mathcal H$ for $n\geq 1$. Then $Th=\sum_{1}^{\infty}\lambda_nh_n$. Hence

$$
\begin{aligned}
\langle Th,h\rangle
&=\left\langle\sum_{n=1}^{\infty}\lambda_nh_n,\,
h_0+\sum_{m=1}^{\infty}h_m\right\rangle\\
&=\sum_{n=1}^{\infty}\sum_{m=0}^{\infty}
\lambda_n\langle h_n,h_m\rangle
=\sum_{n=1}^{\infty}\lambda_n\|h_n\|^2\geq 0
\end{aligned}
$$

since $\langle h_n,h_m\rangle=0$ when $n\ne m$. ■

**7.15. Theorem.** *If $T$ is a compact self-adjoint operator, then there are unique positive compact operators $A,B$ such that $T=A-B$ and $AB=BA=0$.*

**Proof.** Let $T=\sum_{n=1}^{\infty}\lambda_nP_n$ as in (7.6). Define $\phi,\psi:\mathbb C\to\mathbb C$ by $\phi(\lambda_n)=\lambda_n$ if $\lambda_n>0$, $\phi(z)=0$ otherwise; $\psi(\lambda_n)=-\lambda_n$ if $\lambda_n<0$, $\psi(z)=0$ otherwise. Put $A=\phi(T)$ and $B=\psi(T)$. Then $A=\sum\{\lambda_nP_n:\lambda_n>0\}$ and $B=\sum\{-\lambda_nP_n:\lambda_n<0\}$. Thus $T=A-B$. Since $\phi\psi=0$, $AB=BA=0$ by (7.11a). Since $\phi,\psi\geq 0$, $A,B\geq 0$ by the preceding proposition. It remains to show that $A,B$ are unique.

Suppose $T=C-D$ where $C,D$ are compact positive operators and $CD=DC=0$. It is easy to check that $C$ and $D$ commute with $T$. Put $\lambda_0=0$ and $P_0=$ the projection of $\mathcal H$ onto $\ker T$. Thus $C$ and $D$ are reduced by $P_n\mathcal H\equiv\mathcal H_n$ for all $n\geq 0$. Let $C_n=C|_{\mathcal H_n}$ and $D_n=D|_{\mathcal H_n}$. So $C_nD_n=D_nC_n=0$, $\lambda_nP_n=T|_{\mathcal H_n}=C_n-D_n$, and $C_n,D_n$ are positive. Suppose $\lambda_n>0$ and let $h\in\mathcal H_n$. Since $C_nD_n=0$, $\ker C_n\supseteq\operatorname{cl}[\operatorname{ran}D_n]=(\ker D_n)^\perp$. So if $h\in(\ker D_n)^\perp$, then $\lambda_nh=-D_nh$. Hence $\lambda_n\|h\|^2=-\langle D_nh,h\rangle\leq 0$. Thus $h=0$ since $\lambda_n>0$. That is, $\ker D_n=\mathcal H_n$. Thus $D_n=0=B|_{\mathcal H_n}$ and $C_n=\lambda_nP_n=A|_{\mathcal H_n}$. Similarly, if $\lambda_n<0$, $C_n=0=A|_{\mathcal H_n}$ and $D_n=-\lambda_nP_n=B|_{\mathcal H_n}$. On $\mathcal H_0$, $T|_{\mathcal H_0}=0=C_0-D_0$. Thus $C_0=D_0$. But $0=C_0D_0=C_0^2$. Thus $0=\langle C_0^2h,h\rangle=\|C_0h\|^2$, so $C_0=0=A|_{\mathcal H_0}$ and $D_0=0=B|_{\mathcal H_0}$. Therefore $C=A$ and $D=B$. ■

Positive operators are analogous to positive numbers. With this in mind, the next result seems reasonable.

**7.16. Theorem.** *If $T$ is a positive compact operator, then there is a unique positive compact operator $A$ such that $A^2=T$.*

**Proof.** Let $T=\sum_{n=1}^{\infty}\lambda_nP_n$ as in the Spectral Theorem. Since $T\geq 0$, $\lambda_n>0$ for all $n$ (7.14). Let $\phi(\lambda_n)=\lambda_n^{1/2}$ and $\phi(z)=0$ otherwise; put $A=\phi(T)$. It is easy to check that $A\geq 0$; $A=\sum_{1}^{\infty}\lambda_n^{1/2}P_n$ so that $A$ is compact; and $A^2=T$. The proof of uniqueness is left to the reader. ■

**Exercises**

1. If $\{P_n\}$ is a sequence of pairwise orthogonal nonzero projections and $P=\sum P_n$, show that $\left\|P-\sum_{j=1}^{n}P_j\right\|=1$ for all $n$.

2. If $\mathcal H$ is separable, show that the definitions of a diagonalizable operator in (4.6) and (7.3) are equivalent.
