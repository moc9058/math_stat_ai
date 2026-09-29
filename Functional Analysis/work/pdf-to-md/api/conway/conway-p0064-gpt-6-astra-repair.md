§6. An Application: Sturm–Liouville Systems　　　　　　　　　　　　　　　　　49

Now put $P_n=$ the projection of $\mathcal H$ onto $\mathcal E_n$ and examine $T-\sum_{j=1}^{n}\lambda_jP_j$. If $h\in\mathcal E_k$, $1\leq k\leq n$, then $(T-\sum_{j=1}^{n}\lambda_jP_j)h=Th-\lambda_kh=0$. Hence $\mathcal E_1\oplus\cdots\oplus\mathcal E_n\subseteq\ker(T-\sum_{j=1}^{n}\lambda_jP_j)$. If $h\in(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp$, then $P_jh=0$ for $1\leq j\leq n$; so $(T-\sum_{j=1}^{n}\lambda_jP_j)h=Th$. These two statements, together with the fact that $(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp$ reduces $T$, imply that
$$
\begin{aligned}
\left\|T-\sum_{j=1}^{n}\lambda_jP_j\right\|
&=\left\|T|(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp\right\|\\
&=|\lambda_{n+1}|\to0.
\end{aligned}
$$
Therefore the series $\sum_{n=1}^{\infty}\lambda_nP_n$ converges in the metric of $\mathcal B(\mathcal H)$ to $T$. ■

Theorem 5.1 is called the *Spectral Theorem* for compact self-adjoint operators. Using it, one can answer virtually every question about compact hermitian operators, as will be seen before the end of this chapter.

If in Theorem 5.1 it is assumed that $T$ is normal and compact, then the same conclusion, except for the statement that each $\lambda_n$ is real, is true provided that $\mathcal H$ is a $\mathbb C$-Hilbert space. The proof of this will be given in Section 7.

## EXERCISES

1. Prove Corollary 5.4.

2. Prove Corollary 5.5.

3. Let $K$ and $k$ be as in Proposition 4.7 and suppose that $k(x,y)=\overline{k(y,x)}$. Show that $K$ is self-adjoint and if $\{\mu_n\}$ are the eigenvalues of $K$, each repeated $\dim\ker(K-\mu_n)$ times, then $\sum_{1}^{\infty}|\mu_n|^2<\infty$.

4. If $T$ is a compact self-adjoint operator and $\{e_n\}$ and $\{\mu_n\}$ are as in (5.4) and if $h$ is a given vector in $\mathcal H$, show that there is a vector $f$ in $\mathcal H$ such that $Tf=h$ if and only if $h\perp\ker T$ and $\sum_n\mu_n^{-2}|\langle h,e_n\rangle|^2<\infty$. Find the form of the general vector $f$ such that $Tf=h$.

5. Let $T$, $\{\mu_n\}$, and $\{e_n\}$ be as in (5.4). If $\lambda\neq0$ and $\lambda\neq\mu_n$ for any $\mu_n$, then for every $h$ in $\mathcal H$ there is a unique $f$ in $\mathcal H$ such that $(\lambda-T)f=h$. Moreover, $f=\lambda^{-1}[h+\sum_{n=1}^{\infty}\lambda_n(\lambda-\lambda_n)^{-1}\langle h,e_n\rangle e_n]$. Interpret this when $T$ is an integral operator.

## §6*. An Application: Sturm–Liouville Systems

In this section, $[a,b]$ will be a proper interval with $-\infty<a<b<\infty$. $C[a,b]$ denotes the continuous functions $f:[a,b]\to\mathbb R$ and for $n\geq1$, $C^{(n)}[a,b]$ denotes those functions in $C[a,b]$ that have $n$ continuous derivatives. $C_{\mathbb C}^{(n)}[a,b]$ denotes the corresponding spaces of complex-valued functions. We want to consider the differential equation

$$
\tag{6.1}
-h''+qh-\lambda h=f,
$$
