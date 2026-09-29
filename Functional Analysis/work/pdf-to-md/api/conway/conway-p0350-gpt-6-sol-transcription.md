for $f$ in $\mathcal D_a$,

$$
\begin{aligned}
\int_{-a}^{a} f\bar h
&= \overline{H(a)}f(a)-\overline{H(-a)}f(-a)-\int_{-a}^{a}f'\bar H\\
&= -\int_{-a}^{a}f'\bar H.
\end{aligned}
$$

Therefore $\int_{-a}^{a}f'[\bar H-(\bar i\bar g)]=0$ for every $f$ in $\mathcal D_a$. As in (1.11), it follows that $H-ig$ is constant on $[-a,a]$ and $g$ is absolutely continuous. Moreover, $0=H'-ig'=h-ig'$; hence $A^*g=h=ig'$. Thus $g\in\mathcal D$ and $A$ is self-adjoint.

If $A$ is the differentiation operator in Example 6.1, what is the group $U(t)=\exp(itA)$? Since $A$ is not represented as a multiplication operator, Proposition 5.16 cannot be applied. One could proceed to try and discover the spectral measure for $A$. Since $A=\int x\,dE(x)$, $U(t)=\int e^{itx}\,dE(x)$. Or one could be clever.

Later in this section it will be shown that if $\mathcal F:L^2(\mathbb R)\to L^2(\mathbb R)$ is the Fourier–Plancherel transform, then $\mathcal F$ is a unitary operator (6.17) and $\mathcal F^{-1}A\mathcal F=$ the operator on $L^2(\mathbb R)$ of multiplication by the independent variable (6.18). Thus $\mathcal F^{-1}U(t)\mathcal F$ is multiplication by $e^{ixt}$. But it is possible to find $U(t)$ directly.

Recall that if $f\in\operatorname{dom}A$,

$$
Af=-i\lim_{t\to0}\frac{U(t)f-f}{t}.
$$

So

$$
f'(x)=\lim_{t\to0}-\frac{(U(t)f)(x)-f(x)}{t}.
$$

Being clever, one might guess that $(U(t)f)(x)=f(x-t)$.

**6.2. Theorem.** If $A$ and $\mathcal D$ are as in Example 6.1 and $U(t)=\exp(itA)$, then $(U(t)f)(x)=f(x-t)$ for all $f$ in $L^2(\mathbb R)$ and $x,t$ in $\mathbb R$.

**Proof.** Let $(V(t)f)(x)=f(x-t)$. It is easy to see that $V$ is a strongly continuous one parameter unitary group. Let $B$ be the infinitesimal generator of $V$. It must be shown that $B=A$.

Note that $f\in\operatorname{dom}B$ if and only if $\lim_{t\to0}t^{-1}(V(t)f-f)$ exists. Let $f\in C_c^{(1)}(\mathbb R)$; that is, $f$ is continuously differentiable and has compact support. Thus for $t>0$,

$$
\left[\frac{V(t)f-f}{t}\right](x)
=\frac{f(x-t)-f(x)}{t}
=-\frac1t\int_{x-t}^{x}f'(y)\,dy
$$

and

$$
\begin{aligned}
\left|\frac{V(t)f(x)-f(x)}{t}+f'(x)\right|
&\leqslant \frac1t\int_{x-t}^{x}|f'(x)-f'(y)|\,dy\\
&\leqslant \sup\{|f'(x)-f'(y)|:|x-y|\leqslant t\}.
\end{aligned}
$$
