by
$$
\hat f(x)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb R}f(t)e^{-ixt}\,dt.
$$

Because $f\in L^1(\mathbb R)$, this integral is well defined.

The interested reader may want to peruse §VII.9, where the Fourier transform is presented in the more general context of locally compact abelian groups. That section will not be assumed here.

Recall that if $f,g\in L^1$, then the convolution of $f$ and $g$,
$$
f*g(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt,
$$
belongs to $L^1(\mathbb R)$ and $\|f*g\|_1\leq\|f\|_1\|g\|_1$ if the norm of a function $f$ in $L^1(\mathbb R)$ is defined as $\|f\|_1\equiv(2\pi)^{-1/2}\int|f(x)|\,dx$. It is also true that if $f\in L^p(\mathbb R)$, $1\leq p\leq\infty$, then $f*g\in L^p(\mathbb R)$ and $\|f*g\|_p\leq\|f\|_p\|g\|_1$ (see Exercise 4).

**6.7. Theorem.** (a) If $f\in L^1(\mathbb R)$, then $\hat f$ is a continuous function on $\mathbb R$ that vanishes at $\pm\infty$. Also, $\|\hat f\|_\infty\leq\|f\|_1$.

(b) If $\phi\in\mathcal S$, $\hat\phi\in\mathcal S$. Also for $m,n\geq0$,
$$
(ix)^m\left(\frac{d}{dx}\right)^n\hat\phi
=\left[\left(\frac{d}{dx}\right)^m\left((-ix)^n\phi\right)\right]^{\wedge}.
\tag{6.8}
$$

(c) If $f,g\in L^1(\mathbb R)$, then $(f*g)^{\wedge}=\hat f\hat g$. If $f$ and $g\in\mathcal S$, then $f*g\in\mathcal S$. (Note: $[\ \ ]^{\wedge}=$ the Fourier transform of the function defined in the brackets.)

**Proof.** (a) The fact that $\hat f$ is continuous is an easy consequence of Lebesgue’s Dominated Convergence Theorem; it is clear that $\|\hat f\|_\infty\leq\|f\|_1$. For the other part of (a), let $f=$ the characteristic function of the interval $(a,b)$. Then $\hat f(x)=i(2\pi)^{-1/2}x^{-1}[e^{-ixb}-e^{-ixa}]\to0$ as $|x|\to\infty$. So $\hat f(x)$ vanishes at $\pm\infty$ if $f$ is a linear combination of such characteristic functions. The result for a general $f$ follows by approximation.

(b) It is convenient to introduce the notation $D\phi=\phi'$. Thus $D^n\phi=\phi^{(n)}$. Also in this proof, as in many others of this section, $x$ will be used to denote the function whose value at $t$ is $t$ and it will also be used occasionally to denote the independent variable.

If $\phi\in\mathcal S$, then differentiation under the integral sign (Why is this justified?) gives
$$
\begin{aligned}
(D\hat\phi)(y)
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}(-it)e^{-iyt}\phi(t)\,dt\\
&=[(-ix)\phi]^{\wedge}(y).
\end{aligned}
$$
By induction we get that for $n\geq0$,
$$
D^n\hat\phi=[(-ix)^n\phi]^{\wedge}.
\tag{6.9}
$$
