§8. Unitary Equivalence for Compact Normal Operators　61

has finite rank. Let $P_0,Q_0$ be the projections of $\mathcal H,\mathcal K$ onto $\ker T,\ker S$; so $P_0=(\sum_1^\infty P_n)^\perp$ and $Q_0=(\sum_1^\infty Q_n)^\perp$. Put $\lambda_0=\mu_0=0$.

Since $m_T=m_S$, $0<m_T(\lambda_n)=m_S(\lambda_n)$. Hence there is a unique $\mu_j$ such that $\mu_j=\lambda_n$. Define $\pi:\mathbb N\to\mathbb N$ by letting $\mu_{\pi(n)}=\lambda_n$. Let $\pi(0)=0$. Note that $\pi$ is one-to-one. Also, since $0<m_S(\mu_n)=m_T(\mu_n)$, for every $n$ there is a $j$ such that $\pi(j)=n$. Thus $\pi:\mathbb N\cup\{0\}\to\mathbb N\cup\{0\}$ is a bijection or permutation. Since $\dim P_n=m_T(\lambda_n)=m_S(\mu_{\pi(n)})=\dim Q_{\pi(n)}$, there is an isomorphism $U_n:P_n\mathcal H\to Q_{\pi(n)}\mathcal K$ for $n\geq 0$. Define $U:\mathcal H\to\mathcal K$ by letting $U=U_n$ on $P_n\mathcal H$ and extending by linearity. Hence $U=\bigoplus_{n=0}^{\infty}U_n$. It is easy to check that $U$ is an isomorphism. Also, if $h\in P_n\mathcal H$, $n\geq 0$, then $UTh=\lambda_nUh=\mu_{\pi(n)}Uh=SUh$. Hence $UTU^{-1}=S$. ■

If $V$ is the Volterra operator, then $m_V\equiv 0$ (4.11) and $V$ and the zero operator are definitely not unitarily equivalent, so the preceding theorem only applies to compact normal operators. There are no known necessary and sufficient conditions for two arbitrary compact operators to be unitarily equivalent. In fact, there are no known necessary and sufficient conditions that two arbitrary operators on a finite-dimensional space be unitarily equivalent.

## EXERCISES

1. Show that “unitary equivalence” is an equivalence relation on $\mathcal B(\mathcal H)$.

2. Let $U:\mathcal H\to\mathcal K$ be an isomorphism and define $\rho:\mathcal B(\mathcal H)\to\mathcal B(\mathcal K)$ by $\rho(A)=UAU^{-1}$. Prove: (a) $\|\rho(A)\|=\|A\|$, $\rho(A^*)=\rho(A^*)$, and $\rho$ is an isomorphism between the two algebras $\mathcal B(\mathcal H)$ and $\mathcal B(\mathcal K)$. (b) $\rho(A)\in\mathcal B_0(\mathcal K)$ if and only if $A\in\mathcal B_0(\mathcal H)$. (c) If $T\in\mathcal B(\mathcal H)$, then $AT=TA$ if and only if $\rho(T)\rho(A)=\rho(A)\rho(T)$. (d) If $A\in\mathcal B(\mathcal H)$ and $\mathcal M\leq\mathcal H$, then $\mathcal M$ is invariant (reducing) for $A$ if and only if $U\mathcal M$ is invariant (reducing) for $\rho(A)$.

3. Say that an operator $A$ on $\mathcal H$ is *irreducible* if the only reducing subspaces for $A$ are $(0)$ and $\mathcal H$. Prove: (a) The Volterra operator is irreducible. (b) The unilateral shift is irreducible.

4. Suppose $A=\bigoplus\{A_i:i\in I\}$ and $B=\bigoplus\{B_i:i\in I\}$ where each $A_i$ and $B_i$ is irreducible (Exercise 3). Show that $A\cong B$ if and only if there is a bijection $\pi:I\to I$ such that $A_i\cong B_{\pi(i)}$.

5. If $T$ is a compact normal operator and $m_T=m$ is its multiplicity function, prove: (a) $\{\lambda:m(\lambda)>0\}$ is countable and $0$ is its only possible cluster point; (b) $m(\lambda)<\infty$ if $\lambda\ne 0$. Show that if $m:\mathbb C\to\mathbb N\cup\{0,\infty\}$ is any function satisfying (a) and (b), then there is a compact normal operator $T$ such that $m_T=m$.

6. Show that two projections $P$ and $Q$ are unitarily equivalent if and only if $\dim(\operatorname{ran}P)=\dim(\operatorname{ran}Q)$ and $\dim(\ker P)=\dim(\ker Q)$.

7. Let $A:L^2(0,1)\to L^2(0,1)$ be defined by $(Af)(x)=xf(x)$ for $f$ in $L^2(0,1)$ and $x$ in $(0,1)$. Show that $A\cong A^2$.

8. Say that a compact normal operator $T$ is *simple* if $m_T\leq 1$. (See Exercises 7.10 and 7.11.) Show that every compact normal operator $T$ on a separable Hilbert
