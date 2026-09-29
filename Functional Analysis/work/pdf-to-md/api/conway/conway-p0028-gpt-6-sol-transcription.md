**3.4. The Riesz Representation Theorem.** If $L:\mathcal H\to\mathbb F$ is a bounded linear functional, then there is a unique vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$. Moreover, $\|L\|=\|h_0\|$.

**Proof.** Let $\mathcal M=\ker L$. Because $L$ is continuous $\mathcal M$ is a closed linear subspace of $\mathcal H$. Since we may assume that $\mathcal M\ne\mathcal H$, $\mathcal M^\perp\ne(0)$. Hence there is a vector $f_0$ in $\mathcal M^\perp$ such that $L(f_0)=1$. Now if $h\in\mathcal H$ and $\alpha=L(h)$, then $L(h-\alpha f_0)=L(h)-\alpha=0$; so $h-L(h)f_0\in\mathcal M$. Thus

$$
\begin{aligned}
0&=\langle h-L(h)f_0,f_0\rangle\\
 &=\langle h,f_0\rangle-L(h)\|f_0\|^2.
\end{aligned}
$$

So if $h_0=\|f_0\|^{-2}f_0$, $L(h)=\langle h,h_0\rangle$ for all $h$ in $\mathcal H$.

If $h_0'\in\mathcal H$ such that $\langle h,h_0\rangle=\langle h,h_0'\rangle$ for all $h$, then $h_0-h_0'\perp\mathcal H$. In particular, $h_0-h_0'\perp h_0-h_0'$ and so $h_0'=h_0$. The fact that $\|L\|=\|h_0\|$ was shown in the discussion preceding the theorem. ■

**3.5. Corollary.** If $(X,\Omega,\mu)$ is a measure space and $F:L^2(\mu)\to\mathbb F$ is a bounded linear functional, then there is a unique $h_0$ in $L^2(\mu)$ such that

$$
F(h)=\int h\overline{h_0}\,d\mu
$$

for every $h$ in $L^2(\mu)$.

Of course the preceding corollary is a special case of the theorem on representing bounded linear functionals on $L^p(\mu)$, $1\leq p<\infty$. But it is interesting to note that it is a consequence of the result for Hilbert space [and the result that $L^2(\mu)$ is a Hilbert space].

## EXERCISES

1. Prove Proposition 3.3.

2. Let $\mathcal H=\ell^2(\mathbb N)$. If $N\geq1$ and $L:\mathcal H\to\mathbb F$ is defined by $L(\{\alpha_n\})=\alpha_N$, find the vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$.

3. Let $\mathcal H=\ell^2(\mathbb N\cup\{0\})$. (a) Show that if $\{\alpha_n\}\in\mathcal H$, then the power series $\sum_{n=0}^{\infty}\alpha_n z^n$ has radius of convergence $\geq1$. (b) If $|\lambda|<1$ and $L:\mathcal H\to\mathbb F$ is defined by $L(\{\alpha_n\})=\sum_{n=0}^{\infty}\alpha_n\lambda^n$, find the vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$. (c) What is the norm of the linear functional $L$ defined in (b)?

4. With the notation as in Exercise 3, define $L:\mathcal H\to\mathbb F$ by $L(\{\alpha_n\})=\sum_{n=1}^{\infty}n\alpha_n\lambda^{n-1}$, where $|\lambda|<1$. Find a vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for every $h$ in $\mathcal H$.

5. Let $\mathcal H$ be the Hilbert space described in Example 1.8. If $0<t\leq1$, define $L:\mathcal H\to\mathbb F$ by $L(h)=h(t)$. Show that $L$ is a bounded linear functional, find $\|L\|$, and find the vector $h_0$ in $\mathcal H$ such that $L(h)=\langle h,h_0\rangle$ for all $h$ in $\mathcal H$.

6. Let $\mathcal H=L^2(0,1)$ and let $C^{(1)}$ be the set of all continuous functions on $[0,1]$ that have a continuous derivative. Let $t\in[0,1]$ and define $L:C^{(1)}\to\mathbb F$ by $L(h)=h'(t)$. Show that there is no bounded linear functional on $\mathcal H$ that agrees with $L$ on $C^{(1)}$.
