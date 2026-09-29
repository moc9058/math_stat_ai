**Claim.** If $|\lambda-\mu|<|\beta|$, $\ker(A^*-\mu)\cap[\ker(A^*-\lambda)]^\perp=(0)$.

Suppose this is not so. Then there is an $f$ in $\ker(A^*-\mu)\cap[\ker(A^*-\lambda)]^\perp$ with $\|f\|=1$. By (2.5c), $\operatorname{ran}(A-\bar\lambda)$ is closed. Hence $f\in[\ker(A^*-\lambda)]^\perp=\operatorname{ran}(A-\bar\lambda)$. Let $g\in\operatorname{dom}A$ such that $f=(A-\bar\lambda)g$. Since $f\in\ker(A^*-\mu)$,

$$
\begin{aligned}
0&=\langle(A^*-\mu)f,g\rangle=\langle f,(A-\bar\mu)g\rangle\\
&=\langle f,(A-\bar\lambda+\bar\lambda-\bar\mu)g\rangle\\
&=\|f\|^2+(\lambda-\mu)\langle f,g\rangle.
\end{aligned}
$$

Hence $1=\|f\|^2=|\lambda-\mu|\,|\langle f,g\rangle|\leq|\lambda-\mu|\,\|g\|$. But (2.5a) implies that $1=\|f\|=\|(A-\bar\lambda)g\|\geq|\beta|\,\|g\|$; so $\|g\|\leq|\beta|^{-1}$. Hence $1\leq|\lambda-\mu|\,\|g\|\leq|\lambda-\mu|\,|\beta|^{-1}<1$ if $|\lambda-\mu|<|\beta|$. This contradiction establishes the claim.

Combining the claim with Lemma 2.6 gives that $\dim\ker(A^*-\mu)\leq\dim\ker(A^*-\lambda)$ if $|\lambda-\mu|<|\beta|=|\operatorname{Im}\lambda|$. Note that if $|\lambda-\mu|<\frac12|\beta|$, then $|\lambda-\mu|<|\operatorname{Im}\mu|$, so that the other inequality also holds. This shows that the function $\lambda\mapsto\dim\ker(A^*-\lambda)$ is locally constant on $\mathbb C\setminus\mathbb R$. A simple topological argument demonstrates the theorem. $\blacksquare$

**2.8. Theorem.** *If $A$ is a closed symmetric operator, then one and only one of the following possibilities occurs:*

(a) $\sigma(A)=\mathbb C$;

(b) $\sigma(A)=\{\lambda\in\mathbb C:\operatorname{Im}\lambda\geq0\}$;

(c) $\sigma(A)=\{\lambda\in\mathbb C:\operatorname{Im}\lambda\leq0\}$;

(d) $\sigma(A)\subseteq\mathbb R$.

**Proof.** Let $H_\pm=\{\lambda\in\mathbb C:\pm\operatorname{Im}\lambda>0\}$. By (2.5) for $\lambda$ in $H_\pm$, $A-\lambda$ is injective and has closed range. So if $A-\lambda$ is surjective, $\lambda\in\rho(A)$. But $[\operatorname{ran}(A-\lambda)]^\perp=\ker(A^*-\bar\lambda)$. So the preceding theorem implies that either $H_\pm\subset\sigma(A)$ or $H_\pm\cap\sigma(A)=\square$. Since $\sigma(A)$ is closed, if $H_\pm\subseteq\sigma(A)$, then either $\sigma(A)=\mathbb C$ or $\sigma(A)=\operatorname{cl}H_\pm$. If $H_\pm\cap\sigma(A)=\square$, $\sigma(A)\subseteq\mathbb R$. $\blacksquare$

**2.9. Corollary.** *If $A$ is a closed symmetric operator, the following statements are equivalent.*

(a) $A$ is self-adjoint.

(b) $\sigma(A)\subseteq\mathbb R$.

(c) $\ker(A^*-i)=\ker(A^*+i)=(0)$.

**Proof.** If $A$ is symmetric, every eigenvalue of $A$ is real (Exercise 1). So if $A=A^*$ and $\operatorname{Im}\lambda\neq0$, $\ker(A^*-\lambda)=\ker(A-\lambda)=(0)$. Thus $A-\lambda$ is injective and has dense range. By (2.5), $A-\lambda$ has closed range and so $A-\lambda$ has a bounded inverse (1.15) whenever $\operatorname{Im}\lambda\neq0$. That is, $\sigma(A)\subseteq\mathbb R$ and so (a) implies (b).

If $\sigma(A)\subseteq\mathbb R$, $\ker(A^*\pm i)=[\operatorname{ran}(A\mp i)]^\perp=\mathcal H^\perp=(0)$. Hence (b) implies (c).

If (c) holds, then this, combined with (2.5c) and (1.13), implies $A+i$ is
