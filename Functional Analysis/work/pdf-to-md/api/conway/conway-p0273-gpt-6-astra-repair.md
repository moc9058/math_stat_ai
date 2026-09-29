258  
IX. Normal Operators on Hilbert Space

result is crucial for this purpose. It tells us how to integrate with respect to a spectral measure.

**1.10. Proposition.** *If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$ and $\phi:X\to\mathbb C$ is a bounded $\Omega$-measurable function, then there is a unique operator $A$ in $\mathcal B(\mathcal H)$ such that if $\varepsilon>0$ and $\{\Delta_1,\ldots,\Delta_n\}$ is an $\Omega$-partition of $X$ with $\sup\{|\phi(x)-\phi(x')|:x,x'\in\Delta_k\}<\varepsilon$ for $1\leq k\leq n$, then for any $x_k$ in $\Delta_k$,*

$$
\left\|A-\sum_{k=1}^{n}\phi(x_k)E(\Delta_k)\right\|<\varepsilon.
$$

**Proof.** Define $B(g,h)\equiv\int\phi\,dE_{g,h}$ for $g,h$ in $\mathcal H$. By the preceding lemma it is easy to see that $B$ is a sesquilinear form with $|B(g,h)|\leq\|\phi\|_\infty\|g\|\|h\|$. Hence there is a unique operator $A$ such that $B(g,h)=\langle Ag,h\rangle$ for all $g$ and $h$ in $\mathcal H$.

Let $\{\Delta_1,\ldots,\Delta_n\}$ be an $\Omega$-partition satisfying the condition in the statement of the proposition. If $g$ and $h$ are arbitrary vectors in $\mathcal H$ and $x_k\in\Delta_k$ for $1\leq k\leq n$, then

$$
\begin{aligned}
\left|\langle Ag,h\rangle-\sum_{k=1}^{n}\phi(x_k)\langle E(\Delta_k)g,h\rangle\right|
&=\left|\sum_{k=1}^{n}\int_{\Delta_k}[\phi(x)-\phi(x_k)]\,d\langle E(x)g,h\rangle\right|\\
&\leq\sum_{k=1}^{n}\int_{\Delta_k}|\phi(x)-\phi(x_k)|\,d|\langle E(x)g,h\rangle|\\
&\leq\varepsilon\int d|\langle E(x)g,h\rangle|
\leq\varepsilon\|g\|\|h\|.
\end{aligned}
$$

$\blacksquare$

The operator $A$ obtained in the preceding proposition is the *integral of $\phi$ with respect to $E$* and is denoted by

$$
\int\phi\,dE.
$$

Therefore if $g,h\in\mathcal H$ and $\phi$ is a bounded $\Omega$-measurable function on $X$, the preceding proof implies that

$$
\left\langle\left(\int\phi\,dE\right)g,h\right\rangle
=\int\phi\,dE_{g,h}. \tag{1.11}
$$

Let $B(X,\Omega)$ denote the set of bounded $\Omega$-measurable functions $\phi:X\to\mathbb C$ and let $\|\phi\|=\sup\{|\phi(x)|:x\in X\}$. It is easy to see that $B(X,\Omega)$ is a Banach algebra with identity. In fact, if $\phi^*(x)\equiv\overline{\phi(x)}$, then $B(X,\Omega)$ is an abelian $C^*$-algebra. The properties of the integral $\int\phi\,dE$ are summarized by the following result.

**1.12. Proposition.** *If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$ and $\rho:B(X,\Omega)\to\mathcal B(\mathcal H)$ is defined by $\rho(\phi)=\int\phi\,dE$, then $\rho$ is representation of $B(X,\Omega)$ and $\rho(\phi)$ is a normal operator for every $\phi$ in $B(X,\Omega)$.*
