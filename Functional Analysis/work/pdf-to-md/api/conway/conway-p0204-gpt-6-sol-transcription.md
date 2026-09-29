**1.7. Example.** Let $\mathcal X$ be a Banach space and put $\mathcal A=\mathcal B(\mathcal X)$. If multiplication is defined by composition, then $\mathcal A$ is a Banach algebra with identity, $1$. If $\dim\mathcal X\geq 2$, $\mathcal A$ is not abelian.

**1.8. Example.** If $\mathcal X$ is a Banach space and $\mathcal A=\mathcal B_0(\mathcal X)$, the compact operators on $\mathcal X$, then $\mathcal A$ is a Banach algebra without identity if $\dim\mathcal X=\infty$. In fact, $\mathcal B_0(\mathcal X)$ is an ideal of $\mathcal B(\mathcal X)$.

Note that a special case of Example 1.7 occurs when $\mathcal A=M_n(\mathbb F)$, the $n\times n$ matrices, where $\mathcal A$ is given the norm resulting when $M_n(\mathbb F)$ is identified with $\mathcal B(\mathbb F^n)$.

**1.9. Example.** Let $G$ be a locally compact topological group and let $M(G)=$ all finite regular Borel measures on $G$. If $\mu,\nu\in M(G)$, define $L:C_0(G)\to\mathbb F$ by

$$
L(f)=\iint f(xy)\,d\mu(x)\,d\nu(y)
=\iint f(xy)\,d\nu(y)\,d\mu(x).
$$

Then $L$ is a linear functional on $C_0(G)$ and

$$
\begin{aligned}
|L(f)|&\leq\iint |f(xy)|\,d|\mu|(x)\,d|\nu|(y)\\
&\leq\|f\|\,\|\mu\|\,\|\nu\|.
\end{aligned}
$$

So $L\in C_0(G)^*=M(G)$. Define $\mu*\nu$ by $L(f)=\int f\,d(\mu*\nu)$ for $f$ in $C_0(G)$. That is,

$$
\int f\,d(\mu*\nu)=\iint f(xy)\,d\mu(x)\,d\nu(y). \tag{1.10}
$$

Note that $\|\mu*\nu\|=\|L\|\leq\|\mu\|\,\|\nu\|$. If follows that $M(G)$ is a Banach algebra with this definition of multiplication. The product $\mu*\nu$ is called the *convolution* of $\mu$ and $\nu$.

Let $e=$ the identity of $G$ and let $\delta_e=$ the unit point mass at $e$. If $f\in C_0(G)$, then

$$
\begin{aligned}
\int f\,d(\mu*\delta_e)
&=\iint f(xy)\,d\mu(x)\,d\delta_e(y)\\
&=\int f(xe)\,d\mu(x)\\
&=\int f\,d\mu.
\end{aligned}
$$

So $\mu*\delta_e=\mu$; similarly, $\delta_e*\mu=\mu$. Hence $\delta_e$ is the identity for $M(G)$.

If $x,y\in G$, then it is easy to check that $\delta_x*\delta_y=\delta_{xy}$, and $M(G)$ is abelian if and only if $G$ is abelian.
