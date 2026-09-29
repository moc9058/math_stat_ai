whenever $h\in\operatorname{dom}T^*$ and, furthermore, $T^*J^*h=J^*T^*h$. Since $J^{*2}=1$, it follows that $J^*\operatorname{dom}T^*=\operatorname{dom}T^*$ and $J^*T^*=T^*J^*$.

Now let $h\in\ker(T^*\pm i)$. Then $T^*J^*h=J^*T^*h=J^*(\pm ih)=\mp iJ^*h$. Thus $J^*\ker(T^*\pm i)\subseteq\ker(T^*\mp i)$. Since $J^{*2}=1$, $J^*\ker(T^*\pm i)=\ker(T^*\mp i)$. But $J^*$ is injective. Indeed, if $J^*h=0$, then $h=J^*(J^*h)=0$. Thus the deficiency indices of $T$ are equal. By Theorem 2.20, $T$ has a self-adjoint extension. $\blacksquare$

**PROOF OF THEOREM 7.1.** (a) *implies* (b). If $\alpha_0,\ldots,\alpha_n\in\mathbb C$, then

$$
\begin{aligned}
\sum_{j,k=0}^{n}m_{j+k}\alpha_j\overline{\alpha}_k
&=\int\sum_{j,k=0}^{n}\alpha_j\overline{\alpha}_k t^{j+k}\,d\mu(t)\\
&=\int\left(\sum_{j=0}^{n}\alpha_jt^j\right)
          \left(\sum_{k=0}^{n}\overline{\alpha}_kt^k\right)d\mu(t)\\
&=\int\left|\sum_{k=0}^{n}\alpha_kt^k\right|^2d\mu(t)\geqslant0.
\end{aligned}
$$

(b) *implies* (c). Let $\mathcal H_0=$ the collection of all finitely nonzero sequences of complex numbers $\{\alpha_n:n\geqslant0\}$. That is, $\{\alpha_0,\alpha_1,\ldots\}\in\mathcal H_0$ if $\alpha_n\in\mathbb C$ for all $n\geqslant0$ and $\alpha_n=0$ for all but a finite number of values of $n$. If $x=\{\alpha_n\}$, $y=\{\beta_n\}\in\mathcal H_0$ define $[x,y]$ by

$$
[x,y]\equiv\sum_{j,k=0}^{\infty}m_{j+k}\alpha_j\overline{\beta}_k. \tag{7.4}
$$

It is easy to see that $\mathcal H_0$ is a vector space and (7.4) defines a semi-inner product on $\mathcal H_0$. In fact, it is routine that $[\cdot,\cdot]$ is sesquilinear and condition (b) implies that $[x,x]\geqslant0$ for all $x$ in $\mathcal H_0$.

Let $\mathcal N_0=\{x\in\mathcal H_0:[x,x]=0\}$ and let $\mathcal H_1$ be the quotient vector space $\mathcal H_0/\mathcal N_0$. If $h=x+\mathcal N_0$ and $f=y+\mathcal N_0\in\mathcal H_1$, then

$$
\langle h,f\rangle\equiv[x,y] \tag{7.5}
$$

can be verified to be a well-defined inner product on $\mathcal H_1$. Let $\mathcal H$ be the Hilbert space obtained by completing $\mathcal H_1$ with respect to the norm defined by the inner product (7.5).

Now to define some operators. If $x=\{\alpha_n\}\in\mathcal H_0$, let $T_0x=\{0,\alpha_0,\alpha_1,\ldots\}$. It is easy to check that $T_0$ is a linear transformation on $\mathcal H_0$. Also, if $x=\{\alpha_n\}$, $y=\{\beta_n\}\in\mathcal H_0$, let $T_0x=\{\gamma_n\}$. So $\gamma_0=0$ and $\gamma_n=\alpha_{n-1}$ if $n\geqslant1$. Hence

$$
\begin{aligned}
[T_0x,y]
&=\sum_{j,k=0}^{\infty}m_{j+k}\gamma_j\overline{\beta}_k\\
&=\sum_{\substack{j=1\\k=0}}^{\infty}m_{j+k}\alpha_{j-1}\overline{\beta}_k\\
&=\sum_{j,k=0}^{\infty}m_{j+k+1}\alpha_j\overline{\beta}_k.
\end{aligned}
$$
