Then $\widehat{\phi}(\gamma_i\lambda_i^{-1})=\int_K\phi(x)\gamma_i(x^{-1})\lambda_i(x)\,dx$. By the preceding lemma, $\gamma_i(x^{-1})\to\gamma(x^{-1})$ and $\lambda_i(x)\to\lambda(x)$ uniformly for $x$ in $K$. Thus $\widehat{\phi}(\gamma_i\lambda_i^{-1})\to\widehat{\phi}(\gamma\lambda^{-1})$. If $f\in L^1(G)$ and $\varepsilon>0$, let $\phi\in C_c(G)$ such that $\|f-\phi\|_1<\varepsilon/3$. Then

$$
\left|\widehat f(\gamma_i\lambda_i^{-1})-\widehat f(\gamma\lambda^{-1})\right|
<\frac{2\varepsilon}{3}
+\left|\widehat\phi(\gamma_i\lambda_i^{-1})-\widehat\phi(\gamma\lambda^{-1})\right|.
$$

It follows that $\widehat f(\gamma_i\lambda_i^{-1})\to\widehat f(\gamma\lambda^{-1})$ for every $f$ in $L^1(G)$. Hence $\gamma_i\lambda_i^{-1}\to\gamma\lambda^{-1}$ in $\Gamma$. ■

Since $\Gamma$ is a locally compact abelian group, it too has a dual group. Let $\widehat\Gamma$ be this dual group. If $x\in G$, define $\rho(x):\Gamma\to\mathbb T$ by $\rho(x)(\gamma)=\gamma(x)$. It is easy to see that $\rho$ is a homomorphism. It is a rather deep fact, entitled the Pontryagin Duality Theorem, that $\rho:G\to\widehat\Gamma$ is a homeomorphism and an isomorphism. That is, $G$ “is” the dual group of its dual group. The interested reader may consult Rudin [1962]. We turn now to some examples.

**9.11. Theorem.** *If $y\in\mathbb R$, then $\gamma_y(x)=e^{ixy}$ defines a character on $\mathbb R$ and every character on $\mathbb R$ has this form. The map $y\mapsto\gamma_y$ is a homeomorphism and an isomorphism of $\mathbb R$ onto $\widehat{\mathbb R}$. If $y\in\mathbb R$ and $f\in L^1(\mathbb R)$, then*

$$
\tag{9.12}
\widehat f(\gamma_y)=\widehat f(y)=\int_{-\infty}^{\infty}f(x)e^{-ixy}\,dx,
$$

*the Fourier transform of $f$.*

**Proof.** If $y\in\mathbb R$, then $|\gamma_y(x)|=1$ for all $x$ and $\gamma_y(x_1+x_2)=\gamma_y(x_1)\gamma_y(x_2)$. So $\gamma_y\in\widehat{\mathbb R}$. Also, $\gamma_{y_1+y_2}(x)=\gamma_{y_1}(x)\gamma_{y_2}(x)$. Hence $y\mapsto\gamma_y$ is a homomorphism of $\mathbb R$ into $\widehat{\mathbb R}$.

Now let $\gamma\in\widehat{\mathbb R}$. $\gamma(0)=1$ so that there is a $\delta>0$ such that $\int_0^\delta\gamma(x)\,dx=a\ne0$. Thus

$$
\begin{aligned}
a\gamma(x)
&=\gamma(x)\int_0^\delta\gamma(t)\,dt\\
&=\int_0^\delta\gamma(x+t)\,dt\\
&=\int_x^{x+\delta}\gamma(t)\,dt.
\end{aligned}
$$

Hence $\gamma(x)=a^{-1}\int_x^{x+\delta}\gamma(t)\,dt$. Because $\gamma$ is continuous, the Fundamental Theorem of Calculus implies that $\gamma$ is differentiable. Also,

$$
\frac{\gamma(x+h)-\gamma(x)}{h}
=\gamma(x)\left[\frac{\gamma(h)-1}{h}\right].
$$

So $\gamma'(x)=\gamma'(0)\gamma(x)$. Since $\gamma(0)=1$ and $|\gamma(x)|=1$ for all $x$, the elementary
