So if $\mathcal S$ is considered as a subspace of $L^2(\mathbb R)$, $\mathcal F$, the Fourier transform, is an isometry on $\mathcal S$. By Proposition 6.5 and the preceding theorem, $\mathcal F$ extends to a unitary operator on $L^2(\mathbb R)$. $\blacksquare$

Warning! The content of the Plancherel Theorem is that the Fourier transform extends to an isometry. The formula for this isometry is not given by the formula for the Fourier transform. Indeed, this formula does not make sense when $f$ is not an $L^1$ function. However, the same symbol, $\mathcal F$, will be used to denote this unitary operator on $L^2(\mathbb R)$. For emphasis it is called the Plancherel transform.

**6.18. Theorem.** *Let $A$ be the operator on $L^2(\mathbb R)$ given by $Af=if'$ and let $M$ be the operator defined by $Mf=xf$. If $\mathcal F:L^2(\mathbb R)\to L^2(\mathbb R)$ is the Plancherel Transform, then $\mathcal F\operatorname{dom}M=\operatorname{dom}A$ and*

$$
\mathcal F^{-1}A\mathcal F=M.
$$

**Proof.** The fact that $A\mathcal F=\mathcal F M$ on $\mathcal S$ is an immediate consequence of Theorem 6.7(b). Since $\mathcal S$ is dense in both $\operatorname{dom}A$ and $\operatorname{dom}M$, the rest of the result follows (with some work—give the details). $\blacksquare$

Fourier analysis is a subject unto itself. One source is Stein and Weiss [1971]; another is Reed and Simon [1975].

## Exercises

1. If $\mathcal D$ is as in Example 6.1, show that for every $f$ in $\mathcal D$ there is a sequence $\{f_n\}$ in $C_c^{(1)}(\mathbb R)$ such that $f_n\to f$ and $f_n'\to f'$ in $L^2(\mathbb R)$.

2. Show that the Schwartz space $\mathcal S$ with the seminorms $\{\|\cdot\|_{m,n}:m,n\geq 0\}$ is a Fréchet space.

3. If $\phi$ is infinitely differentiable on $\mathbb R$, show that $\phi\in\mathcal S$ if and only if for every integer $n\geq 0$ and every polynomial $p$, $\phi^{(n)}(x)p(x)\to 0$ as $|x|\to\infty$.

4. If $f\in L^p(\mathbb R)$, $1\leq p\leq\infty$, and $g\in L^1(\mathbb R)$, show that $f*g\in L^p(\mathbb R)$ and $\|f*g\|_p\leq\|f\|_p\|g\|_1$. (Hint: See Dunford and Schwartz [1958], p. 530, Exercise 13 for a generalization of Minkowski’s Inequality.)

5. If $\psi$ and $\psi_\varepsilon$ are as Proposition 6.13 and $f\in L^p(\mathbb R)$, $1\leq p<\infty$, show that $\|f*\psi_\varepsilon-f\|_p\to 0$ as $\varepsilon\to 0$. If $f\in L^\infty(\mathbb R)$, show that $f*\psi_\varepsilon\to f$ (weak$^*$).

6. If $f\in L^1(\mathbb R)$ and $\hat f\in L^1(\mathbb R)$, show that $f(x)=(2\pi)^{-1/2}\int_{\mathbb R}\hat f(t)e^{ixt}\,dt$ a.e.

7. If $\mathcal F:L^2(\mathbb R)\to L^2(\mathbb R)$ is the Plancherel Transform and $f\in L^2(\mathbb R)$, show that $(\mathcal F^{-1}f)(x)=(\mathcal Ff)(-x)$.

8. Show that $\mathcal F^4=1$ but $\mathcal F^2\neq 1$. What does this say about $\sigma(\mathcal F)$?

9. Find the Fourier transform of the Hermite polynomials. What do you think? (This exercise is broken up into a series of easier steps on pages 98–99 of Dym and McKean [1972].)
