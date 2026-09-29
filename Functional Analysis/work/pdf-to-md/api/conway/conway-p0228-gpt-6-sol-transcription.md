when $y<x$ and $0$ otherwise, then

$$
V_kf(x)=
\begin{cases}
\displaystyle\int_0^x f(y)\,dy & \text{if }x\leq\frac12,\\[6pt]
\displaystyle\int_0^{1/2} f(y)\,dy & \text{if }x\geq\frac12.
\end{cases}
$$

So if $f(y)=0$ for $0\leq y\leq\frac12$, $V_kf=0$.

On the other hand, the Volterra operator $V$ [$=V_k$ for $k(x,y)=$ the characteristic function of $\{(x,y):y<x\}$] has $\ker V=(0)$. In fact, if $0=Vf$, then for all $x$, $0=\int_0^x f(y)\,dy$. Differentiating gives that $f=0$.

Is there an analogy between $V_k$ for a Volterra kernel $k$ and a lower triangular matrix?

## Exercises

1. Prove Proposition 6.1.

2. Show that for $\mathcal{X}$ a Banach space and $A$ in $\mathcal{B}(\mathcal{X})$, $\sigma_l(A)=\sigma_r(A^*)$. What happens in a Hilbert space?

3. If $\mathcal{H}$ is an infinite dimension Hilbert space and $K$ is a non-empty compact subset of $\mathbb{C}$, show that there is an $A$ in $\mathcal{B}(\mathcal{H})$ such that $\sigma(A)=K$. Can $A$ be found such that $\sigma(A)=\sigma_{ap}(A)=K$?

4. Let $K$ be a compact subset of $\mathbb{C}$. Does there exist an operator $A$ in $\mathcal{B}(C[0,1])$ such that $\sigma(A)=K$?

5. If $\mathcal{X}$ is a Banach space and $A\in\mathcal{B}(\mathcal{X})$, show that $A$ is left invertible if and only if $\ker A=(0)$ and $\operatorname{ran}A$ is a closed complemented subspace of $\mathcal{X}$.

6. If $\mathcal{X}$ is a Banach space and $A\in\mathcal{B}(\mathcal{X})$, show that $A$ is right invertible if and only if $\operatorname{ran}A=\mathcal{X}$ and $\ker A$ is a complemented subspace of $\mathcal{X}$.

7. If $\mathcal{X}$ is a Banach space and $T:\mathcal{X}\to\mathcal{X}$ is an isometry, then either $\sigma(T)\subseteq\partial\mathbb{D}$ or $\sigma(T)=\operatorname{cl}\mathbb{D}$.

8. Verify the statements made in Example 6.10.

9. Let $1\leq p\leq\infty$ and suppose $0<\alpha_1\leq\alpha_2\cdots$ such that $r=\lim\alpha_n<\infty$. Define $A:\ell^p\to\ell^p$ by $A(x_1,x_2,\ldots)=(0,\alpha_1x_1,\alpha_2x_2,\ldots)$. Show that $\sigma(A)=\{z\in\mathbb{C}:|z|\leq r\}$ and $\sigma_{ap}(A)=\partial\sigma(A)$. If $|\lambda|<r$, then $\operatorname{ran}(A-\lambda)$ is closed and has codimension 1. Also, $\sigma_p(A)=\square$.

10. Verify the statements made in Example 6.14.

11. Let $1\leq p\leq\infty$ and let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space. For $\phi$ in $L^\infty(\mu)$, define $M_\phi$ on $L^p(\mu)$ as in Example III.2.2. Find $\sigma(M_\phi)$, $\sigma_{ap}(M_\phi)$, and $\sigma_p(M_\phi)$.

12. If $A\in\mathcal{B}(\mathcal{X})$, $f\in\operatorname{Hol}(A)$, and $\lambda\in\sigma_p(A)$, is $f(\lambda)\in\sigma_p(f(A))$? If $\lambda\in\sigma_{ap}(A)$, is $f(\lambda)\in\sigma_{ap}(f(A))$? Is there a relation between $f(\sigma_{ap}(A))$ and $\sigma_{ap}(f(A))$?

13. If $A\in\mathcal{B}(\mathcal{X})$, say that a complex number $\lambda$ has *finite index* if there is a positive integer $k$ such that $\ker(A-\lambda)^k=\ker(A-\lambda)^{k+1}$; the *index* of $\lambda$, denoted by $\nu(\lambda)$
