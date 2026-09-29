$x^{-1}(y-x)y^{-1}$, let $x=(\alpha+h-a)$ and $y=(\alpha-a)$, where $\alpha\in\rho(a)$ and $h\in\mathbb C$ such that $h\ne0$ and $\alpha+h\in\rho(a)$. This gives

$$
\begin{aligned}
\frac{F(\alpha+h)-F(\alpha)}{h}
&=\frac{(\alpha+h-a)^{-1}(-h)(\alpha-a)^{-1}}{h}\\
&=-(\alpha+h-a)^{-1}(\alpha-a)^{-1}.
\end{aligned}
$$

Since $(\alpha+h-a)^{-1}\to(\alpha-a)^{-1}$ as $h\to0$, $F'(\alpha)$ exists and

$$
F'(\alpha)=-(\alpha-a)^{-2}.
$$

Clearly $F':\rho(a)\to\mathcal A$ is continuous, so $F$ is analytic on $\rho(a)$.

From the first paragraph of the proof and Corollary 2.3, if $|z|>\|a\|$, then $F(z)=z^{-1}(1-a/z)^{-1}$. But as $z\to\infty$, $(1-a/z)\to1$ and so $(1-a/z)^{-1}\to1$. Thus $F(z)\to0$ as $z\to\infty$.

Therefore if $\rho(a)=\mathbb C$, $F$ is an entire function that vanishes at $\infty$. By Liouville’s Theorem $F$ is constant. Since $F'\ne0$, this is a contradiction. Thus $\rho(a)\ne\mathbb C$, or $\sigma(a)\ne\square$. ■

Because the spectrum of an element of a complex Banach algebra is not empty, the following assumption is made.

**Assumption.** *Henceforward, all Banach spaces and all Banach algebras are over $\mathbb C$.*

**3.7. Definition.** If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$, the *spectral radius* of $a$, $r(a)$, is defined by

$$
r(a)=\sup\{|\alpha|:\alpha\in\sigma(a)\}.
$$

Because $\sigma(a)\ne\square$ and is bounded, $r(a)$ is well defined and finite; because $\sigma(a)$ is compact, this supremum is attained.

Let $\mathcal A=M_2(\mathbb C)$ and let $A=\begin{bmatrix}0&0\\1&0\end{bmatrix}$. Then $A^2=0$ and $\sigma(A)=\{0\}$; so $r(A)=0$. So it is possible to have $r(A)=0$ with $A\ne0$.

**3.8. Proposition.** *If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$, $\lim\|a^n\|^{1/n}$ exists and*

$$
r(a)=\lim\|a^n\|^{1/n}.
$$

**Proof.** Let $G=\{z\in\mathbb C:z=0\text{ or }z^{-1}\in\rho(a)\}$. Define $f:G\to\mathcal A$ by $f(0)=0$ and for $z\ne0$, $f(z)=(z^{-1}-a)^{-1}$. Since $(a-\alpha)^{-1}\to0$ as $\alpha\to\infty$, $f$ is analytic on $G$, and so $f$ has a power series expansion. In fact, by Corollary 2.3, for $|z|<\|a\|^{-1}$,

$$
f(z)=\sum_{n=0}^{\infty}a^n/(z^{-1})^{n+1}
=z\sum_{n=0}^{\infty}z^na^n.
$$
