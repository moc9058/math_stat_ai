If $\mathcal K$ is a Hilbert space with a basis $\mathcal F$, $\mathcal K$ is isomorphic to $l^2(\mathcal F)$. If $\dim\mathcal H=\dim\mathcal K$, $\mathcal E$ and $\mathcal F$ have the same cardinality; it is easy to see that $l^2(\mathcal E)$ and $l^2(\mathcal F)$ must be isomorphic. Therefore $\mathcal H$ and $\mathcal K$ are isomorphic. ■

**5.5. Corollary.** *All separable infinite dimensional Hilbert spaces are isomorphic.*

This section concludes with a rather important example of an isomorphism, the Fourier transform on the circle.

The proof of the next result can be found as an Exercise on p. 263 of Conway [1978]. Another proof will be given latter in this book after the Stone–Weierstrass Theorem is proved. So the reader can choose to assume this for the moment. Let $\mathbb D=\{z\in\mathbb C:|z|<1\}$.

**5.6. Theorem.** *If $f:\partial\mathbb D\to\mathbb C$ is a continuous function, then there is a sequence $\{p_n(z,\bar z)\}$ of polynomials in $z$ and $\bar z$ such that $p_n(z,\bar z)\to f(z)$ uniformly on $\partial\mathbb D$.*

Note that if $z\in\partial\mathbb D$, $\bar z=z^{-1}$. Thus a polynomial in $z$ and $\bar z$ on $\partial\mathbb D$ becomes a function of the form

$$
\sum_{k=-m}^{n}\alpha_k z^k.
$$

If we put $z=e^{i\theta}$, this becomes a function of the form

$$
\sum_{k=-m}^{n}\alpha_k e^{ik\theta}.
$$

Such functions are called *trigonometric polynomials*.

We can now show that the orthonormal set in Example 4.3 is a basis for $L_{\mathbb C}^{2}[0,2\pi]$. This is a rather important result.

**5.7. Theorem.** *If for each $n$ in $\mathbb Z$, $e_n(t)\equiv(2\pi)^{-1/2}\exp(int)$, then $\{e_n:n\in\mathbb Z\}$ is a basis for $L_{\mathbb C}^{2}[0,2\pi]$.*

**Proof.** Let $\mathcal T=\{\sum_{k=-n}^{n}\alpha_k e_k:\alpha_k\in\mathbb C,\ n\geq 0\}$. Then $\mathcal T$ is a subalgebra of $C_{\mathbb C}[0,2\pi]$, the algebra of all continuous $\mathbb C$-valued functions on $[0,2\pi]$. Note that if $f\in\mathcal T$, $f(0)=f(2\pi)$. We want to show that the uniform closure of $\mathcal T$ is $\mathcal C\equiv\{f\in C_{\mathbb C}[0,2\pi]:f(0)=f(2\pi)\}$. To do this, let $f\in\mathcal C$ and define $F:\partial\mathbb D\to\mathbb C$ by $F(e^{it})=f(t)$. $F$ is continuous. (Why?) By (5.6) there is a sequence of polynomials in $z$ and $\bar z$, $\{p_n(z,\bar z)\}$, such that $p_n(z,\bar z)\to F(z)$ uniformly on $\partial\mathbb D$. Thus $p_n(e^{it},e^{-it})\to f(t)$ uniformly on $[0,2\pi]$. But $p_n(e^{it},e^{-it})\in\mathcal T$.

Now the closure of $\mathcal C$ in $L_{\mathbb C}^{2}[0,2\pi]$ is all of $L_{\mathbb C}^{2}[0,2\pi]$ (Exercise 6). Hence $\bigvee\{e_n:n\in\mathbb Z\}=L_{\mathbb C}^{2}[0,2\pi]$ and $\{e_n\}$ is thus a basis (4.13). ■

Actually, it is usually preferred to normalize the measure on $[0,2\pi]$. That is, replace $dt$ by $(2\pi)^{-1}\,dt$, so that the total measure of $[0,2\pi]$ is 1. Now define
