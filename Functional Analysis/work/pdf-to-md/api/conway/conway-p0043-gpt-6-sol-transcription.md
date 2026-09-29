**Exercise 11.** A sufficient condition for the boundedness of an infinite matrix that is useful is known. (See Exercise 9.) Another sufficient condition for a matrix to be bounded can be found on page 61 of Maddox [1980].

**1.5. Theorem.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and put $\mathcal H=L^2(X,\Omega,\mu)\equiv L^2(\mu)$. If $\phi\in L^\infty(\mu)$, define $M_\phi:L^2(\mu)\to L^2(\mu)$ by $M_\phi f=\phi f$. Then $M_\phi\in\mathcal B(L^2(\mu))$ and $\|M_\phi\|=\|\phi\|_\infty$.

**Proof.** Here $\|\phi\|_\infty$ is the $\mu$-essential supremum norm. That is,

$$
\begin{aligned}
\|\phi\|_\infty
&\equiv \inf\{\sup\{|\phi(x)|:x\notin N\}:N\in\Omega,\ \mu(N)=0\}\\
&=\inf\{c>0:\mu(\{x\in X:|\phi(x)|>c\})=0\}.
\end{aligned}
$$

Thus $\|\phi\|_\infty$ is the infimum of all $c>0$ such that $|\phi(x)|\leqslant c$ a.e. $[\mu]$ and, moreover, $|\phi(x)|\leqslant\|\phi\|_\infty$ a.e. $[\mu]$. Thus we can, and do, assume that $\phi$ is a bounded measurable function and $|\phi(x)|\leqslant\|\phi\|_\infty$ for all $x$. So if $f\in L^2(\mu)$, then $\int|\phi f|^2\,d\mu\leqslant\|\phi\|_\infty^2\int|f|^2\,d\mu$. That is, $M_\phi\in\mathcal B(L^2(\mu))$ and $\|M_\phi\|\leqslant\|\phi\|_\infty$. If $\varepsilon>0$, the $\sigma$-finiteness of the measure space implies that there is a set $\Delta$ in $\Omega$, $0<\mu(\Delta)<\infty$, such that $|\phi(x)|\geqslant\|\phi\|_\infty-\varepsilon$ on $\Delta$. (Why?) If $f=(\mu(\Delta))^{-1/2}\chi_\Delta$, then $f\in L^2(\mu)$ and $\|f\|_2=1$. So $\|M_\phi\|^2\geqslant\|\phi f\|_2^2=(\mu(\Delta))^{-1}\int_\Delta|\phi|^2\,d\mu\geqslant(\|\phi\|_\infty-\varepsilon)^2$. Letting $\varepsilon\to0$, we get that $\|M_\phi\|\geqslant\|\phi\|_\infty$. ■

The operator $M_\phi$ is called a *multiplication operator*. The function $\phi$ is its *symbol*.

If the measure space $(X,\Omega,\mu)$ is not $\sigma$-finite, then the conclusion of Theorem 1.5 is not necessarily valid. Indeed, let $\Omega=$ the Borel subsets of $[0,1]$ and define $\mu$ on $\Omega$ by $\mu(\Delta)=$ the Lebesgue measure of $\Delta$ if $0\notin\Delta$ and $\mu(\Delta)=\infty$ if $0\in\Delta$. This measure has an infinite atom at $0$ and, therefore, is not $\sigma$-finite. Let $\phi=\chi_{\{0\}}$. Then $\phi\in L^\infty(\mu)$ and $\|\phi\|_\infty=1$. If $f\in L^2(\mu)$, then $\infty>\int|f|^2\,d\mu\geqslant|f(0)|^2\mu(\{0\})$. Hence every function in $L^2(\mu)$ vanishes at $0$. Therefore $M_\phi=0$ and $\|M_\phi\|<\|\phi\|_\infty$.

There are more general measure spaces for which (1.5) is valid—the decomposable measure spaces (see Kelley [1966]).

**1.6. Theorem.** Let $(X,\Omega,\mu)$ be a measure space and suppose $k:X\times X\to\mathbb F$ is an $\Omega\times\Omega$-measurable function for which there are constants $c_1$ and $c_2$ such that

$$
\begin{aligned}
\int_X |k(x,y)|\,d\mu(y)&\leqslant c_1 \qquad \text{a.e. }[\mu],\\
\int_X |k(x,y)|\,d\mu(x)&\leqslant c_2 \qquad \text{a.e. }[\mu].
\end{aligned}
$$

If $K:L^2(\mu)\to L^2(\mu)$ is defined by

$$
(Kf)(x)=\int k(x,y)f(y)\,d\mu(y),
$$

then $K$ is a bounded linear operator and $\|K\|\leqslant(c_1c_2)^{1/2}$.
