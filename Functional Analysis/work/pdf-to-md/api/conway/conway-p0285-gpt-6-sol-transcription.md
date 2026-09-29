that $\mu_1$ and $\mu_2$ are *boundedly mutually absolutely continuous* if $[\mu_1]=[\mu_2]$ and the Radon–Nikodym derivatives are essentially bounded functions.

**3.6. Theorem.** $N_{\mu_1}\cong N_{\mu_2}$ if and only if $[\mu_1]=[\mu_2]$.

**Proof.** Suppose $[\mu_1]=[\mu_2]$ and put $\phi=d\mu_1/d\mu_2$. So if $g\in L^1(\mu_1)$, $g\phi\in L^1(\mu_2)$ and $\int g\phi\,d\mu_2=\int g\,d\mu_1$. Hence, if $f\in L^2(\mu_1)$, $\sqrt{\phi}f\in L^2(\mu_2)$ and $\|\sqrt{\phi}f\|_2=\|f\|_2$; that is, $U:L^2(\mu_1)\to L^2(\mu_2)$ defined by $Uf=\sqrt{\phi}f$ is an isometry. If $g\in L^2(\mu_2)$, then $f=\phi^{-1/2}g\in L^2(\mu_1)$ and $Uf=g$; hence $U$ is surjective and $U^{-1}g=\phi^{-1/2}g$ for $g$ in $L^2(\mu_2)$. If $g\in L^2(\mu_2)$, then $UN_{\mu_1}U^{-1}g=UN_{\mu_1}\phi^{-1/2}g=Uz\phi^{-1/2}g=zg$, and so $UN_{\mu_1}U^{-1}=N_{\mu_2}$.

Now assume that $V:L^2(\mu_1)\to L^2(\mu_2)$ is an isomorphism such that $VN_{\mu_1}V^{-1}=N_{\mu_2}$. Put $\psi=V(1)$; so $\psi\in L^2(\mu_2)$. For convenience, put $N_j=N_{\mu_j}$, $j=1,2$. It is easy to see that $VN_1^kV^{-1}=N_2^k$ and $VN_1^{*k}V^{-1}=N_2^{*k}$. Hence $Vp(N_1,N_1^*)V^{-1}=p(N_2,N_2^*)$ for any polynomial $p$ in $z$ and $\bar z$. Since $N_1\cong N_2$, $\sigma(N_1)=\sigma(N_2)$; hence support $\mu_1=\operatorname{support}\mu_2=K$. By taking uniform limits of polynomials in $z$ and $\bar z$, $Vu(N_1)V^{-1}=u(N_2)$ for $u$ in $C(K)$. Hence for $u$ in $C(K)$, $V(u)=Vu(N_1)1=u(N_2)V1=u\psi$. Because $V$ is an isometry, this implies that $\int |u|^2\,d\mu_1=\int |u|^2|\psi|^2\,d\mu_2$ for every $u$ in $C(K)$. Hence $\int v\,d\mu_1=\int v|\psi|^2\,d\mu_2$ for $v$ in $C(K)$, $v\geq 0$. By the uniqueness part of the Riesz Representation Theorem, $\mu_1=|\psi|^2\mu_2$, so $\mu_1\ll\mu_2$.

By using $V^{-1}$ instead of $V$ and reversing the roles of $N_1$ and $N_2$ in the preceding argument, it follows that $\mu_2\ll\mu_1$. Hence $[\mu_1]=[\mu_2]$. $\blacksquare$

## Exercises

1. If $\mu$ is a compactly supported measure on $\mathbb C$ and $f\in L^2(\mu)$, $f$ is a star-cyclic vector for $N_\mu$ if and only if $\mu(\{x:f(x)=0\})=0$.

2. Prove Proposition 3.2.

3. If $\mu_1$ and $\mu_2$ are compactly supported measures on $\mathbb C$, show that the following statements are equivalent: (a) $\mu_1$ and $\mu_2$ are boundedly mutually absolutely continuous; (b) there is an isomorphism $V:L^2(\mu_1)\to L^2(\mu_2)$ such that $VN_{\mu_1}V^{-1}=N_{\mu_2}$ and $VL^\infty(\mu_1)=L^\infty(\mu_2)$; (c) there is a bounded bijection $R:L^2(\mu_1)\to L^2(\mu_2)$ such that $Rp(z,\bar z)=p(z,\bar z)$ for every polynomial in $z$ and $\bar z$.

4. Show that if $N$ is a star-cyclic normal operator and $\lambda\in\sigma_p(N)$, then $\dim\ker(N-\lambda)=1$.

5. If $N$ is diagonalizable and star-cyclic and if $\sigma_p(N)=\{\lambda_1,\lambda_2,\ldots\}$, show that $N$ is unitarily equivalent to $N_\mu$, where $\mu=\sum_{n=1}^{\infty}2^{-n}\delta_{\lambda_n}$ (see Exercise 2.11).

6. Let $N$ be a diagonalizable normal operator. Show that $N\cong M$ if and only if $M$ is a diagonalizable normal operator, $\sigma_p(N)=\sigma_p(M)$, and $\dim\ker(N-\lambda)=\dim\ker(M-\lambda)$ for all $\lambda$. (Compare this with Theorem II.8.3.)

7. Let $U$ be the bilateral shift on $l^2(\mathbb Z)$. If $e_0$ is the vector in $l^2(\mathbb Z)$ that has 1 in the zeroth place and zeros elsewhere, then $e_0$ is a star-cyclic vector for $U$. If $\mu$ is the compactly supported measure on $\mathbb C$ and $V:l^2(\mathbb Z)\to L^2(\mu)$ is the isomorphism such that $Ve_0=1$ and $VUV^{-1}=N_\mu$, then
