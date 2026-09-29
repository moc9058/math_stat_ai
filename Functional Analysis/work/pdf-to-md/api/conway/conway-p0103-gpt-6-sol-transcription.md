# Exercises

1. Prove Proposition 9.3.

2. Prove Proposition 9.4.

3. Show that $e$ is an order unit for $(\mathcal{X},\leqslant)$ if and only if for every $x$ in $\mathcal{X}$ there is a $\delta>0$ such that $e\pm tx\geqslant 0$ for $0\leqslant t\leqslant\delta$.

4. Show that $C(\mathbb{R})$, the space of all continuous real-valued functions on $\mathbb{R}$, has no order unit.

5. Prove (9.11).

6. Characterize the order units of $C_b(X)$. Does $C_b(X)$ always have an order unit?

7. Characterize the order units of $C_0(X)$ if $X$ is locally compact. Does $C_0(X)$ always have an order unit?

8. Let $\mathcal{X}=M_2(\mathbb{R})$, the $2\times2$ matrices over $\mathbb{R}$. Define $A$ in $M_2(\mathbb{R})$ to be positive if $A=A^*$ and $\langle Ax,x\rangle\geqslant0$ for all $x$ in $\mathbb{R}^2$. Characterize the order units of $M_2(\mathbb{R})$.

9. If $1\leqslant p<\infty$ and $\mathcal{X}=L^p(0,1)$, define $f\leqslant g$ to mean that $f(x)\leqslant g(x)$ a.e. Show that $\mathcal{X}$ is an ordered vector space that has no order unit.

# §10. The Dual of a Quotient Space and a Subspace

Let $\mathcal{X}$ be a normed space and $\mathcal{M}\leqslant\mathcal{X}$. If $f\in\mathcal{X}^*$, then $f|_{\mathcal{M}}$, the restriction of $f$ to $\mathcal{M}$, belongs to $\mathcal{M}^*$ and $\|f|_{\mathcal{M}}\|\leqslant\|f\|$. According to the Hahn–Banach Theorem, every bounded linear functional on $\mathcal{M}$ is obtainable as the restriction of a functional from $\mathcal{X}^*$. In fact, more can be said.

Note that if $\mathcal{M}^{\perp}\equiv\{g\in\mathcal{X}^*:g(\mathcal{M})=0\}$ (note the analogy with Hilbert space notation); then $\mathcal{M}^{\perp}$ is a closed subspace of the Banach space $\mathcal{X}^*$. Hence $\mathcal{X}^*/\mathcal{M}^{\perp}$ is a Banach space. Moreover, if $f+\mathcal{M}^{\perp}\in\mathcal{X}^*/\mathcal{M}^{\perp}$, then $f+\mathcal{M}^{\perp}$ induces a linear functional on $\mathcal{M}$, namely $f|_{\mathcal{M}}$.

**10.1. Theorem.** *If $\mathcal{M}\leqslant\mathcal{X}$ and $\mathcal{M}^{\perp}\equiv\{g\in\mathcal{X}^*:g(\mathcal{M})=0\}$, then the map $\rho:\mathcal{X}^*/\mathcal{M}^{\perp}\to\mathcal{M}^*$ defined by*

$$
\rho(f+\mathcal{M}^{\perp})=f|_{\mathcal{M}}
$$

*is an isometric isomorphism.*

**Proof.** It is easy to see that $\rho$ is linear and injective. If $f\in\mathcal{X}^*$ and $g\in\mathcal{M}^{\perp}$, then $\|f|_{\mathcal{M}}\|=\|(f+g)|_{\mathcal{M}}\|\leqslant\|f+g\|$. Taking the infimum over all $g$ we get that $\|f|_{\mathcal{M}}\|\leqslant\|f+\mathcal{M}^{\perp}\|$. Suppose $\phi\in\mathcal{M}^*$. The Hahn–Banach Theorem implies that there is an $f$ in $\mathcal{X}^*$ such that $f|_{\mathcal{M}}=\phi$ and $\|f\|=\|\phi\|$. Hence $\phi=\rho(f+\mathcal{M}^{\perp})$ and $\|\phi\|=\|f\|\geqslant\|f+\mathcal{M}^{\perp}\|$. ■

Now consider $\mathcal{X}/\mathcal{M}$; what is $(\mathcal{X}/\mathcal{M})^*$? Let $Q:\mathcal{X}\to\mathcal{X}/\mathcal{M}$ be the natural map. If $f\in(\mathcal{X}/\mathcal{M})^*$, then $f\circ Q\in\mathcal{X}^*$ and $\|f\circ Q\|\leqslant\|f\|$. (Why?) This gives a way of mapping $(\mathcal{X}/\mathcal{M})^*\to\mathcal{X}^*$. What is its image? Is it an isometry?
