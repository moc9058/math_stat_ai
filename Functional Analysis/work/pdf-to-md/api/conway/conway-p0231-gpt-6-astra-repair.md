216  VII. Banach Algebras and Spectral Theory

or there is a subsequence contained in $\sigma_p(A^*)$. If $\{\lambda_{n_k}\}\subseteq\sigma_p(A)$, then Lemma 7.5 implies $\lambda_{n_k}\to 0$, a contradiction. If $\{\lambda_{n_k}\}\subseteq\sigma_p(A^*)$, then the fact that $A^*$ is compact gives the same contradiction. Thus $\lambda$ must be isolated if $\lambda\ne 0$.

**7.7. Claim.** If $\lambda\in\sigma(A)$ and $\lambda\ne 0$, then $\lambda\in\sigma_p(A)$ and $\dim\ker(A-\lambda)<\infty$.

By (7.6), $\lambda$ is an isolated point of $\sigma(A)$ so that $E(\lambda)$ can be defined as in (6.9). Let $\mathcal X_\lambda=E(\lambda)\mathcal X$ and $A_\lambda=A|_{\mathcal X_\lambda}$. By Exercise 4.9 [also see (4.11)], $\sigma(A_\lambda)=\{\lambda\}$. Thus $A_\lambda$ is an invertible compact operator. By Exercise VI.3.5, $\dim\mathcal X_\lambda<\infty$. If $n=\dim\mathcal X_\lambda$, then $A_\lambda-\lambda$ is a nilpotent operator on an $n$-dimensional space. Thus $(A_\lambda-\lambda)^n=0$. Let $\nu=$ the positive integer such that $(A_\lambda-\lambda)^\nu=0$ but $(A_\lambda-\lambda)^{\nu-1}\ne 0$. Let $x\in\mathcal X_\lambda$ such that $0\ne(A_\lambda-\lambda)^{\nu-1}x=y$; then $(A-\lambda)y=0$. Thus $\lambda\in\sigma_p(A)$.

Also, $\ker(A-\lambda)\in\operatorname{Lat}A$ and $A|_{\ker(A-\lambda)}$ is compact. But $Ax=\lambda x$ for all $x$ in $\ker(A-\lambda)$, so $\dim\ker(A-\lambda)<\infty$.

Now for the *dénouement*. If $\dim\mathcal X=\infty$ and $A\in\mathcal B_0(\mathcal X)$, then $A$ cannot be invertible (Exercise VI.3.5). Thus $0\in\sigma(A)$. If $\lambda\in\sigma(A)$ and $\lambda\ne 0$, then Claim 7.7 says that $\lambda\in\sigma_p(A)$ and $\dim\ker(A-\lambda)<\infty$. So if $\sigma(A)$ is finite, either (a) or (b) of (7.1) hold. If $\sigma(A)$ is infinite, then Claim 7.6 implies that $\sigma(A)$ is countable. So let $\sigma(A)=\{0,\lambda_1,\lambda_2,\ldots\}$. By Lemma 7.5 and Claim 7.7, (c) holds. ■

Part of the following surfaced in the proof of the theorem.

**7.8. Corollary.** *If $A\in\mathcal B_0(\mathcal X)$ and $\lambda\in\sigma(A)$ with $\lambda\ne 0$, then $\lambda$ is a pole of $(z-A)^{-1}$, $\ker(A-\lambda)\subseteq E(\lambda)\mathcal X$, and $\dim E(\lambda)\mathcal X<\infty$.*

**Proof.** The only part of this corollary that did not appear in the preceding proof is the fact that $\ker(A-\lambda)\subseteq E(\lambda)\mathcal X$.

Let $\Delta=\sigma(A)\setminus\{\lambda\}$, $\mathcal X_\Delta=E(\Delta)\mathcal X$, $A_\Delta=A|_{\mathcal X_\Delta}$. By Exercise 4.9, $\sigma(A_\Delta)=\Delta$; so $A_\Delta-\lambda$ is invertible on $\mathcal X_\Delta$. If $x\in\ker(A-\lambda)$, then $x=E(\lambda)x+E(\Delta)x$. Hence $0=(A-\lambda)x=(A-\lambda)E(\lambda)x+(A-\lambda)E(\Delta)x=(A_\lambda-\lambda)E(\lambda)x+(A_\Delta-\lambda)E(\Delta)x$. But $\mathcal X_\lambda$ and $\mathcal X_\Delta\in\operatorname{Lat}A$, so $(A_\lambda-\lambda)E(\lambda)x\in\mathcal X_\lambda$ and $(A_\Delta-\lambda)E(\Delta)x\in\mathcal X_\Delta$; since $\mathcal X_\lambda\cap\mathcal X_\Delta=(0)$, $0=(A_\lambda-\lambda)E(\lambda)x=(A_\Delta-\lambda)E(\Delta)x$. But $A_\Delta-\lambda$ is invertible so $E(\Delta)x=0$; that is, $x=E(\lambda)x\in\mathcal X_\lambda$. Hence $\ker(A-\lambda)\subseteq\mathcal X_\lambda$. ■

If $k$ is a Volterra kernel (6.14), then $V_k$ is a compact operator (Exercise VI.3.6) and $\sigma(V_k)=\{0\}$. So the first possibility of Theorem 7.1 can occur. If $V$ is the Volterra operator, then $\sigma_p(V)=\square$.

Let $V$ be the Volterra operator on $L^p(0,1)$, $1<p<\infty$. If $\lambda_1,\ldots,\lambda_n\in\mathbb C$, let $D:\mathbb C^n\to\mathbb C^n$ be defined by $D(z_1,\ldots,z_n)=(\lambda_1z_1,\ldots,\lambda_nz_n)$. Then $A=V\oplus D$ on $L^p(0,1)\oplus\mathbb C^n$ is compact and $\sigma(A)=\{0,\lambda_1,\ldots,\lambda_n\}$. So the second possibility of (7.1) occurs. If $\{\lambda_n\}\subseteq\mathbb C$ and $\lim\lambda_n=0$, then define $D:\ell^p\to\ell^p$ $(1\le p\le\infty)$ by $(Dx)(n)=\lambda_nx(n)$. If $A=V\oplus D$ on $L^p(0,1)\oplus\ell^p$, $A$ is compact and $\sigma(A)=\{0,\lambda_1,\lambda_2,\ldots\}$ (see Exercise 3).
