If $\alpha\in U_0$, $(z-\alpha)^{-1}$ is analytic in a neighborhood of $L$. By (III.8.5), there is a sequence of polynomials $\{p_n\}$ such that $\|p_n-(z-\alpha)^{-1}\|_L\to0$. If $q_n=(z-\alpha)p_n$, then $\|q_n-1\|_L\to0$. Thus for large $n$, $\|q_n-1\|_L<1/2$. Since $K\subset L$ and $|q_n(\alpha)-1|=1$, this implies that $\alpha\notin K^{\wedge}$. Thus $K^{\wedge}\subseteq L$. ■

**5.4. Theorem.** *If $\mathcal A$ and $\mathcal B$ are Banach algebras with a common identity such that $\mathcal B\subseteq\mathcal A$ and $a\in\mathcal B$, then*

(a) $\sigma_{\mathcal A}(a)\subseteq\sigma_{\mathcal B}(a)$ and $\partial\sigma_{\mathcal B}(a)\subseteq\partial\sigma_{\mathcal A}(a)$.

(b) $\sigma_{\mathcal A}(a)^{\wedge}=\sigma_{\mathcal B}(a)^{\wedge}$.

(c) *If $G$ is a hole of $\sigma_{\mathcal A}(a)$, then either $G\subseteq\sigma_{\mathcal B}(a)$ or $G\cap\sigma_{\mathcal B}(a)=\varnothing$.*

(d) *If $\mathcal B$ is the closure in $\mathcal A$ of all polynomials in $a$, then $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)^{\wedge}$.*

**Proof.** (a) If $\alpha\notin\sigma_{\mathcal B}(a)$, then there is a $b$ in $\mathcal B$ such that $b(a-\alpha)=(a-\alpha)b=1$. Since $\mathcal B\subseteq\mathcal A$, $\alpha\notin\sigma_{\mathcal A}(a)$. Now assume that $\lambda\in\partial\sigma_{\mathcal B}(a)$. Since $\operatorname{int}\sigma_{\mathcal A}(a)\subseteq\operatorname{int}\sigma_{\mathcal B}(a)$, it suffices to show that $\lambda\in\sigma_{\mathcal A}(a)$. Suppose $\lambda\notin\sigma_{\mathcal A}(a)$; there is thus an $x$ in $\mathcal A$ such that $x(a-\lambda)=(a-\lambda)x=1$. Since $\lambda\in\partial\sigma_{\mathcal B}(a)$, there is a sequence $\{\lambda_n\}$ in $\mathbb C\setminus\sigma_{\mathcal B}(a)$ such that $\lambda_n\to\lambda$. Let $(a-\lambda_n)^{-1}$ be the inverse of $(a-\lambda_n)$ in $\mathcal B$, so $(a-\lambda_n)^{-1}\in\mathcal A$. Since $\lambda_n\to\lambda$, $(a-\lambda_n)\to(a-\lambda)$. By Theorem 2.2, $(a-\lambda_n)^{-1}\to x$. Thus $x\in\mathcal B$ since $\mathcal B$ is complete. This contradicts the fact that $\lambda\in\sigma_{\mathcal B}(a)$.

(b) This is a consequence of (a) and the Maximum Principle.

(c) Let $G$ be a hole of $\sigma_{\mathcal A}(a)$ and put $G_1=G\cap\sigma_{\mathcal B}(a)$ and $G_2=G\setminus\sigma_{\mathcal B}(a)$. So $G=G_1\cup G_2$ and $G_1\cap G_2=\varnothing$. Clearly $G_2$ is open. On the other hand, the fact that $\partial\sigma_{\mathcal B}(a)\subseteq\sigma_{\mathcal A}(a)$ and $G\cap\sigma_{\mathcal A}(a)=\varnothing$ implies that $G_1=G\cap\operatorname{int}\sigma_{\mathcal B}(a)$, so $G_1$ is open. Because $G$ is connected, either $G_1$ or $G_2$ is empty.

(d) Let $\mathcal B$ be as in (d). From (a) and (b) it is known that $\sigma_{\mathcal A}(a)\subseteq\sigma_{\mathcal B}(a)\subseteq\sigma_{\mathcal A}(a)^{\wedge}$. Fix $\lambda$ in $\sigma_{\mathcal A}(a)^{\wedge}$. If $\lambda\notin\sigma_{\mathcal B}(a)$, $(a-\lambda)^{-1}\in\mathcal B\subseteq\mathcal A$. Hence there is a sequence of polynomials $\{p_n\}$ such that $p_n(a)\to(a-\lambda)^{-1}$. Let $q_n(z)=(z-\lambda)p_n(z)$. Thus $\|q_n(a)-1\|\to0$. By the Spectral Mapping Theorem, $\sigma_{\mathcal A}(q_n(a))=q_n(\sigma_{\mathcal A}(a))$. Thus, because $\lambda\in\sigma_{\mathcal A}(a)^{\wedge}$,

$$
\begin{aligned}
\|q_n(a)-1\|&\geq r(q_n(a)-1)\\
&=\sup\{|z-1|:z\in\sigma_{\mathcal A}(q_n(a))\}\\
&=\sup\{|q_n(w)-1|:w\in\sigma_{\mathcal A}(a)\}\\
&\geq |q_n(\lambda)-1|\\
&=1.
\end{aligned}
$$

This is a contradiction. ■

**Exercises**

1. If $K$ is a compact subset of $\mathbb C$, let $P(K)$ be the closure of the polynomials in $C(K)$. Show that the identity map on polynomials extends to an isometric isomorphism of $P(K)$ onto $P(K^{\wedge})$.

2. If $K$ is a compact subset of $\mathbb C$, let $R(K)$ be the closure in $C(K)$ of all rational functions with poles off $K$. If $f\in R(K)$, show that $\sigma_{R(K)}(f)=f(K)$. If $f\in P(K)$, show that $\sigma_{P(K)}(f)=\hat f(K^{\wedge})$, where $\hat f$ is a natural extension of $f$ to $K^{\wedge}$.
