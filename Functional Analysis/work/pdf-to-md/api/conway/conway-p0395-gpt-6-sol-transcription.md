**Proof.** Exercise.

The Radon–Nikodym Theorem can now be proved for complex-valued measures $\mu$ by using (C.6) and applying the usual theorem to the real and imaginary parts of $\mu$. The details are left to the reader.

**C.7. Radon–Nikodym Theorem.** *If $(X,\Omega,\nu)$ is a $\sigma$-finite measure space and $\mu$ is a complex-valued measure on $(X,\Omega)$ such that $\mu\ll\nu$, then there is a unique complex-valued function $f$ in $L^1(X,\Omega,\nu)$ such that $\mu(\Delta)=\int_\Delta f\,d\nu$ for every $\Delta$ in $\Omega$.*

The function $f$ obtained in (C.7) is called the *Radon–Nikodym derivative* of $\mu$ with respect to $\nu$ and is denoted by $f=d\mu/d\nu$.

**C.8. Theorem.** *Let $(X,\Omega,\nu)$ be a $\sigma$-finite measure space and let $\mu$ be a complex-valued measure on $(X,\Omega)$ such that $\mu\ll\nu$ and let $f=d\mu/d\nu$.*

(a) *If $g\in L(X,\Omega,|\mu|)$, then $gf\in L^1(X,\Omega,\nu)$ and $\int g\,d\mu=\int gf\,d\nu$.*

(b) *For $\Delta$ in $\Omega$, $|\mu|(\Delta)=\int_\Delta |f|\,d\nu$.*

**Proof.** Part (a) follows from the corresponding result for signed measures by using (C.2) and a similar decomposition for $f$.

To prove (b), let $\{E_j\}$ be a measurable partition of $\Delta$. Then

$$
\sum_j|\mu(E_j)|\leqslant\sum_j\int_{E_j}|f|\,d\nu
=\int_\Delta |f|\,d\nu.
$$

For the reverse inequality, let $g(x)=\overline{f(x)}/|f(x)|$ if $x\in\Delta$ and $f(x)\neq0$; let $g(x)=0$ otherwise. Let $\{g_n\}$ be a sequence of $\Omega$-measurable simple functions such that $g_n(x)=0$ off $\Delta$, $|g_n|\leqslant|g|\leqslant1$, and $g_n(x)\to g(x)$ a.e. $[\nu]$. Thus $fg_n\to|f|\chi_\Delta$ a.e. $[\nu]$. Also, $|fg_n|\leqslant|f|\chi_\Delta$ and $f\chi_\Delta\in L^1(\nu)$ [see (C.2)]. By the Lebesgue Dominated Convergence Theorem, $\int fg_n\,d\nu\to\int_\Delta|f|\,d\nu$. If $g_n=\sum_j\alpha_j\chi_{E_j}$, where $\{E_j\}$ is a partition of $\Delta$ and $|\alpha_j|\leqslant1$, then $|\int fg_n\,d\nu|=|\int g_n\,d\mu|=|\sum_j\alpha_j\mu(E_j)|\leqslant|\mu|(\Delta)$. Thus $\int_\Delta|f|\,d\nu\leqslant|\mu|(\Delta)$. ■

One way of phrasing (C.8b) is that $|d\mu/d\nu|=d|\mu|/d\nu$. The next result is left to the reader.

**C.9. Corollary.** *If $\mu$ is a complex-valued measure on $(X,\Omega)$, then there is an $\Omega$-measurable function $f$ on $X$ such that $|f|=1$ a.e. $[|\mu|]$ and $\mu(\Delta)=\int_\Delta f\,d|\mu|$ for each $\Delta$ in $\Omega$.*

**C.10. Definition.** Let $X$ be a locally compact space and let $\Omega$ be the smallest $\sigma$-algebra of subsets of $X$ that contains the open sets. Sets in $\Omega$ are called *Borel sets*. A positive measure $\mu$ on $(X,\Omega)$ is a *regular Borel measure* if (a) $\mu(K)<\infty$ for every compact subset $K$ of $X$; (b) for any $E$ in $\Omega$, $\mu(E)=\sup\{\mu(K):K\subseteq E\text{ and }K\text{ is compact}\}$; (c) for any $E$ in $\Omega$, $\mu(E)=\inf\{\mu(U):U\supseteq E\text{ and }U\text{ is open}\}$. If $\mu$ is a complex-valued measure on $(X,\Omega)$, $\mu$ is a regular Borel
