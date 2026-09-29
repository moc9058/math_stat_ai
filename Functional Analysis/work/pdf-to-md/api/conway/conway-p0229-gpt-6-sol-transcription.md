or $\nu_A(\lambda)$, is the smallest such integer $k$. (a) Show that if $\lambda$ is an isolated point of $\sigma(A)$ and a pole of order $n$ of $(z-A)^{-1}$, then $\nu(\lambda)=n$. (b) If $\nu(\lambda)<\infty$, show that

$$
\ker(A-\lambda)^{\nu(\lambda)}
=\ker(A-\lambda)^{\nu(\lambda)+k}
\quad\text{for all }k\geq 0.
$$

(c) If $\mathcal X=\mathbb C^n$ and

$$
A=\begin{bmatrix}
0 & & & & \\
1 & 0 & & & \\
& 1 & \ddots & & \\
& & \ddots & \ddots & \\
& & & 1 & 0
\end{bmatrix},
$$

then $\sigma(A)=\{0\}$ and $\nu(0)=n$.

14. If $V$ is the Volterra operator, show that $0$ is an essential singularity of $(z-V)^{-1}$.

15. Let $\mathcal A$ be a Banach algebra with identity. If $a\in\mathcal A$, define $L_a,R_a\in\mathcal B(\mathcal A)$ by $L_a(x)=ax$ and $R_a(x)=xa$. Show that $\sigma(L_a)=\sigma(R_a)=\sigma(a)$.

16. If $E$ is a projection on a Hilbert space and $E$ is neither $0$ nor $1$, then $\sigma(E)=\{0,1\}$.

17. (McCabe [1984]) If $\mathcal X$ is a complex Banach space and $T\in\mathcal B(\mathcal X)$, show that the following statements are equivalent. (a) $r(T)<1$. (b) $\|T^m\|<1$ for some positive integer $m$. (c) $\sum_n\|T^n(x)\|<\infty$ for every $x$ in $\mathcal X$.

## §7. The Spectral Theory of a Compact Operator

Recall that for a Banach space $\mathcal X$, $\mathcal B_0(\mathcal X)$ is the algebra of all compact operators. This Banach algebra has no identity, so if $A\in\mathcal B_0(\mathcal X)$, then $\sigma(A)$ refers to the spectrum of $A$ as an element of $\mathcal B(\mathcal X)$. Of course, if $\mathcal A=\mathcal B_0(\mathcal X)+\mathbb C$, then $\mathcal A$ is a Banach algebra with identity (Why?) and we could consider $\sigma_{\mathcal A}(A)$ for $A$ in $\mathcal B_0(\mathcal X)$. By Theorem 5.4, $\sigma(A)\subseteq\sigma_{\mathcal A}(A)$, $\partial\sigma_{\mathcal A}(A)\subseteq\sigma(A)$, and $\sigma(A)^{\wedge}=\sigma_{\mathcal A}(A)^{\wedge}$. Below, in Theorem 7.1, it will be shown that $\sigma(A)$ is a countable set and hence $\sigma(A)=\partial\sigma(A)=\sigma(A)^{\wedge}$. Thus $\sigma(A)=\sigma_{\mathcal A}(A)$.

**7.1. Theorem.** (F. Riesz) *If $\dim\mathcal X=\infty$ and $A\in\mathcal B_0(\mathcal X)$, then one and only one of the following possibilities occurs.*

(a) $\sigma(A)=\{0\}$.

(b) $\sigma(A)=\{0,\lambda_1,\ldots,\lambda_n\}$, where for $1\leq k\leq n$, $\lambda_k\neq 0$, each $\lambda_k$ is an eigenvalue of $A$, and $\dim\ker(A-\lambda_k)<\infty$.

(c) $\sigma(A)=\{0,\lambda_1,\lambda_2,\ldots\}$, where for each $k\geq 1$, $\lambda_k$ is an eigenvalue of $A$, $\dim\ker(A-\lambda_k)<\infty$, and, moreover, $\lim\lambda_k=0$.

The proof will use several lemmas. The first lemma was given in the case that $\mathcal X$ is a Hilbert space in Proposition II.4.14. The proof is identical and will not be repeated here.

**7.2. Lemma.** *If $A\in\mathcal B_0(\mathcal X)$, $\lambda\neq 0$, and $\ker(A-\lambda)=(0)$, then $\operatorname{ran}(A-\lambda)$ is closed.*
