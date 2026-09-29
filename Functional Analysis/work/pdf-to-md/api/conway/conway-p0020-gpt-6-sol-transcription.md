Recall that an absolutely continuous function on the unit interval $[0,1]$ has a derivative a.e. on $[0,1]$.

**1.8. Example.** Let $\mathcal H$ = the collection of all absolutely continuous functions $f:[0,1]\to\mathbb F$ such that $f(0)=0$ and $f'\in L^2(0,1)$. If $\langle f,g\rangle=\int_0^1 f'(t)\overline{g'(t)}\,dt$ for $f$ and $g$ in $\mathcal H$, then $\mathcal H$ is a Hilbert space (Exercise 3).

Suppose $\mathcal X$ is a vector space with an inner product $\langle\cdot,\cdot\rangle$ and the norm is defined by the inner product. What happens if $(\mathcal X,d)$ ($d(x,y)\equiv\|x-y\|$) is not complete?

**1.9. Proposition.** *If $\mathcal X$ is a vector space and $\langle\cdot,\cdot\rangle_{\mathcal X}$ is an inner product on $\mathcal X$ and if $\mathcal H$ is the completion of $\mathcal X$ with respect to the metric induced by the norm on $\mathcal X$, then there is an inner product $\langle\cdot,\cdot\rangle_{\mathcal H}$ on $\mathcal H$ such that $\langle x,y\rangle_{\mathcal H}=\langle x,y\rangle_{\mathcal X}$ for $x$ and $y$ in $\mathcal X$ and the metric on $\mathcal H$ is induced by this inner product. That is, the completion of $\mathcal X$ is a Hilbert space.*

The preceding result says that an incomplete inner product space can be completed to a Hilbert space. It is also true that a Hilbert space over $\mathbb R$ can be imbedded in a complex Hilbert space (see Exercise 7).

This section closes with an example of a Hilbert space from analytic function theory.

**1.10. Definition.** If $G$ is an open subset of the complex plane $\mathbb C$, then $L_a^2(G)$ denotes the collection of all analytic functions $f:G\to\mathbb C$ such that

$$
\iint_G |f(x+iy)|^2\,dx\,dy<\infty.
$$

$L_a^2(G)$ is called the *Bergman space* for $G$.

Several alternatives for the integral with respect to two-dimensional Lebesgue measure will be used. In addition to $\iint_G f(x+iy)\,dx\,dy$ we will also see

$$
\iint_G f \quad\text{and}\quad \int_G f\,d\mathrm{Area}.
$$

Note that $L_a^2(G)\subseteq L^2(\mu)$, where $\mu=\mathrm{Area}|G$, so that $L_a^2(G)$ has a natural inner product and norm from $L^2(\mu)$.

**1.11. Lemma.** *If $f$ is analytic in a neighborhood of $\overline{B}(a;r)$, then*

$$
f(a)=\frac{1}{\pi r^2}\iint_{B(a;r)} f.
$$

[Here $B(a;r)\equiv\{z:|z-a|<r\}$ and $\overline{B}(a;r)\equiv\{z:|z-a|\leq r\}$.]
