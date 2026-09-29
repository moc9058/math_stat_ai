$k$ is a Volterra kernel, define $V_k:L^p(0,1)\to L^p(0,1)$ by

$$
V_kf(x)=\int_0^1 k(x,y)f(y)\,dy=\int_0^x k(x,y)f(y)\,dy.
$$

Then $V_k\in\mathcal{B}(L^p)$ and $\|V_k\|\leq\|k\|_\infty$ (III.2.3).

If $k$, $h$ are Volterra kernels and

$$
(hk)(x,y)=\int_0^1 h(x,t)k(t,y)\,dt,
$$

then $hk$ is a Volterra kernel, $\|hk\|_\infty\leq\|h\|_\infty\|k\|_\infty$, and $V_{hk}=V_hV_k$. Note that if $k(x,y)$ is the characteristic function of $\{(x,y)\in[0,1]\times[0,1]:y<x\}$, then $V_k$ is the Volterra operator (II.1.7).

If $k$ is a Volterra kernel, then

$$
\sigma(V_k)=\{0\}.
$$

Indeed, from the preceding paragraph it is known that $V_k^n=V_{k^n}$. This will be used to show that the spectral radius of $V_k$ is 0.

**6.15. Claim.** $|k^n(x,y)|\leq(\|k\|_\infty^n/(n-1)!)(x-y)^{n-1}$ for $y<x$.

This is proved by induction. Clearly it holds for $n=1$. Suppose (6.15) is true for some $n\geq1$. Then

$$
\begin{aligned}
|k^{n+1}(x,y)|
&=\left|\int_y^x k(x,t)k^n(t,y)\,dt\right|\\
&\leq\int_y^x |k(x,t)|\,|k^n(t,y)|\,dt\\
&\leq\|k\|_\infty\frac{\|k\|_\infty^n}{(n-1)!}
\int_y^x(t-y)^{n-1}\,dt\\
&\leq\frac{\|k\|_\infty^{n+1}}{n!}(x-y)^n.
\end{aligned}
$$

This establishes the claim.

From (6.15) it follows that

$$
\|V_k^n\|\leq\|k^n\|_\infty\leq\frac{\|k\|_\infty^n}{(n-1)!}.
$$

Therefore

$$
\|V_k^n\|^{1/n}\leq\|k\|_\infty[(n-1)!]^{-1/n}.
$$

Since $[(n-1)!]^{-1/n}\to0$ as $n\to\infty$, $r(V_k)=0$. Thus $\square\ne\sigma(V_k)\subseteq\{\lambda\in\mathbb{C}:|\lambda|\leq0\}$; that is, $\sigma(V_k)=\{0\}$.

It is possible for $\ker V_k$ to be nontrivial. For example, if $k(x,y)=\chi_{(0,1/2)}(y)$
