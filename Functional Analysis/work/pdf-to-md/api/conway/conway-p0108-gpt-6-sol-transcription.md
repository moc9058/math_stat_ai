$\{x:|\phi(x)|\geq 1+\delta\}$ with $\mu(E)<\infty$. We want to show that $\mu(E)=0$. But if $f=\chi_E$, then
$$
\mu(E)=\|f\|_p^p\geq\|Af\|_p^p=\|\phi f\|_p^p
=\int_E|\phi|^p\,d\mu\geq(1+\delta)^p\mu(E).
$$
Hence $\mu(E)=0$. Since $E$ was arbitrary it follows that $\phi$ is an essentially bounded function and $\|\phi\|_\infty\leq 1$. $\blacksquare$

**12.8. Definition.** If $\mathcal X,\mathcal Y$ are Banach spaces, an *isomorphism* of $\mathcal X$ and $\mathcal Y$ is a linear bijection $T:\mathcal X\to\mathcal Y$ that is a homeomorphism. Say that $\mathcal X$ and $\mathcal Y$ are *isomorphic* if there is an isomorphism of $\mathcal X$ onto $\mathcal Y$.

Note that the Inverse Mapping Theorem says that a continuous bijection is an isomorphism.

The use of the word “isomorphism” is counter to the spirit of category theory, but it is traditional in Banach space theory.

## Exercises

1. Suppose $\mathcal X$ and $\mathcal Y$ are Banach spaces. If $A\in\mathcal B(\mathcal X,\mathcal Y)$ and $\operatorname{ran}A$ is a second category space, show that $\operatorname{ran}A$ is closed.

2. Give both $C^{(1)}[0,1]$ and $C[0,1]$ the supremum norm. If $A:C^{(1)}[0,1]\to C[0,1]$ is defined by $Af=f'$, show that $A$ is not bounded.

3. Prove Proposition 12.7.

4. Let $\mathcal X$ be a vector space and suppose $\|\cdot\|_1$ and $\|\cdot\|_2$ are two norms on $\mathcal X$ and that $\mathscr T_1$ and $\mathscr T_2$ are the corresponding topologies. Show that if $\mathcal X$ is complete in both norms and $\mathscr T_1\supseteq\mathscr T_2$, then $\mathscr T_1=\mathscr T_2$.

5. Let $\mathcal X$ and $\mathcal Y$ be Banach spaces and let $A\in\mathcal B(\mathcal X,\mathcal Y)$. Show that there is a constant $c>0$ such that $\|Ax\|\geq c\|x\|$ for all $x$ in $\mathcal X$ if and only if $\ker A=(0)$ and $\operatorname{ran}A$ is closed.

6. Let $X$ be compact and suppose that $\mathcal X$ is a Banach subspace of $C(X)$. If $E$ is a closed subset of $X$ such that for every $g$ in $C(E)$ there is an $f$ in $\mathcal X$ with $f|E=g$, show that there is a constant $c>0$ such that for each $g$ in $C(E)$ there is an $f$ in $\mathcal X$ with $f|E=g$ and $\max\{|f(x)|:x\in X\}\leq c\max\{|g(x)|:x\in E\}$.

7. Let $1\leq p\leq\infty$ and suppose $(\alpha_{ij})$ is a matrix such that $(Af)(i)=\sum_{j=1}^{\infty}\alpha_{ij}f(j)$ defines an element $Af$ of $l^p$ for every $f$ in $l^p$. Show that $A\in\mathcal B(l^p)$.

8. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space, $1\leq p<\infty$, and suppose that $k:X\times X\to\mathbb F$ is an $\Omega\times\Omega$ measurable function such that for $f$ in $L^p(\mu)$ and a.e. $x$, $k(x,\cdot)f(\cdot)\in L^1(\mu)$ and $(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)$ defines an element $Kf$ of $L^p(\mu)$. Show that $K:L^p(\mu)\to L^p(\mu)$ is a bounded operator.

## §13. Complemented Subspaces of a Banach Space

If $\mathcal X$ is a Banach space and $\mathcal M\leq\mathcal X$, say that $\mathcal M$ is *algebraically complemented* in $\mathcal X$ if there is an $\mathcal N\leq\mathcal X$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal X$. Of course, the definition makes sense in a purely algebraic setting, so the requirement that $\mathcal M$ and $\mathcal N$ be closed seems fatuous. Why is it made?
