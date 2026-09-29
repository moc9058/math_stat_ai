theory of differential equations implies that $\gamma=\gamma_y$ for some $y$ in $\mathbb R$. This implies that $y\mapsto\gamma_y$ is an isomorphism of $\mathbb R$ onto $\mathbb R$.

It is clear from (9.7) that (9.12) holds. From here it is easy to see that $y\mapsto\gamma_y$ is a homeomorphism of $\mathbb R$ onto $\widehat{\mathbb R}$. ■

So the preceding result says that $\mathbb R$ is its own dual group. Because of (9.12), the function $\widehat f$ as defined in (9.7) is called the *Fourier transform* of $f$. The next result lends more weight to the use of this terminology.

**9.13. Theorem.** *If $n\in\mathbb Z$, define $\gamma_n:\mathbb T\to\mathbb T$ by $\gamma_n(z)=z^n$. Then $\gamma_n\in\widehat{\mathbb T}$ and the map $n\mapsto\gamma_n$ is a homeomorphism and an isomorphism of $\mathbb Z$ onto $\widehat{\mathbb T}$. If $n\in\mathbb Z$ and $f\in L^1(\mathbb T)$, then*

**9.14**
$$
\widehat f(\gamma_n)=\widehat f(n)\equiv\frac{1}{2\pi}\int_0^{2\pi}f(e^{i\theta})e^{-in\theta}\,d\theta.
$$

**Proof.** It is left to the reader to check that $\gamma_n\in\widehat{\mathbb T}$ and $n\mapsto\gamma_n$ is an injective homomorphism of $\mathbb Z$ into $\widehat{\mathbb T}$. If $\gamma\in\widehat{\mathbb T}$, define $\sigma:\mathbb R\to\mathbb T$ by $\sigma(t)=\gamma(e^{it})$; it follows that $\sigma\in\widehat{\mathbb R}$. By (9.11), $\sigma(t)=e^{iyt}$ for some $y$ in $\mathbb R$. But $\sigma(t+2\pi)=\sigma(t)$, so $e^{2\pi iy}=1$. Hence $y=n\in\mathbb Z$. Thus $\gamma(e^{i\theta})=\sigma(\theta)=e^{in\theta}$, $\gamma=\gamma_n$, and $n\mapsto\gamma_n$ is an isomorphism of $\mathbb Z$ onto $\widehat{\mathbb T}$. Formula (9.14) is immediate from (9.7). The fact that $n\mapsto\gamma_n$ is a homeomorphism is left as an exercise. ■

So $\widehat{\mathbb T}=\mathbb Z$, a discrete group. This can be generalized.

**9.15. Theorem.** *If $G$ is compact, $\widehat G$ is discrete; if $G$ is discrete, $\widehat G$ is compact.*

**Proof.** Put $\Gamma=\widehat G$. If $G$ is discrete, then $L^1(G)$ has an identity. Hence its maximal ideal space is compact. That is, $\Gamma$ is compact.

Now assume that $G$ is compact. Hence $\Gamma\subseteq L^1(G)$ since $m(G)=1$. Suppose $\gamma\in\Gamma$ and $\gamma\ne$ the identity for $\Gamma$, then there is a point $x_0$ in $G$ such that $\gamma(x_0)\ne1$. Thus
$$
\begin{aligned}
\int\gamma(x)\,dx
&=\int\gamma(xx_0^{-1}x_0)\,dx\\
&=\gamma(x_0)\int\gamma(xx_0^{-1})\,dx\\
&=\gamma(x_0)\int\gamma(x)\,dx,
\end{aligned}
$$
since Haar measure is translation invariant. Since $\gamma(x_0)\ne1$, this implies that
$$
\int_G\gamma(x)\,dx=0\qquad\text{if }\gamma\ne1.
$$

Of course if $\gamma=1$, $\int 1\,dx=m(G)=1$. So if $f=1$ on $G$, $f\in L^1(G)$ and
