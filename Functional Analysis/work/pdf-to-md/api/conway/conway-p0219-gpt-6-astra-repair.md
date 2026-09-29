204 VII. Banach Algebras and Spectral Theory

that $f_n(z)\to f(z)$ uniformly on compact subsets of $G$. By (c) of the hypothesis, $\tau(f_n)\to\tau(f)$. But $\tau(f_n)=f_n(a)$ and $f_n(a)\to f(a)$ by (4.7e). Hence $\tau(f)=f(a)$. $\blacksquare$

A fact that has been implicit in the manipulations involving the functional calculus is that $f(a)$ and $g(a)$ commute for all $f$ and $g$ in $\operatorname{Hol}(a)$. In fact, if $\tau:\operatorname{Hol}(a)\to\mathcal A$ is defined by $\tau(f)=f(a)$, then $f(a)g(a)=\tau(fg)=\tau(gf)=g(a)f(a)$. Still more can be said.

**4.9. Proposition.** *If $a,b\in\mathcal A$, $ab=ba$, and $f\in\operatorname{Hol}(a)$, then $f(a)b=bf(a)$.*

**Proof.** An algebraic exercise demonstrates that $f(a)b=bf(a)$ if $f$ is a rational function with poles off $\sigma(a)$. The general result now follows by Runge’s Theorem. $\blacksquare$

**4.10. The Spectral Mapping Theorem.** *If $a\in\mathcal A$ and $f\in\operatorname{Hol}(a)$, then*

$$
\sigma(f(a))=f(\sigma(a)).
$$

**Proof.** If $\alpha\in\sigma(a)$, let $g\in\operatorname{Hol}(a)$ such that $f(z)-f(\alpha)=(z-\alpha)g(z)$. If it were the case that $f(\alpha)\notin\sigma(f(a))$, then $(a-\alpha)$ would be invertible with inverse $g(a)[f(a)-f(\alpha)]^{-1}$. Hence $f(\alpha)\in\sigma(f(a))$; that is, $f(\sigma(a))\subseteq\sigma(f(a))$.

Conversely, if $\beta\notin f(\sigma(a))$, then $g(z)=[f(z)-\beta]^{-1}\in\operatorname{Hol}(a)$ and so $g(a)[f(a)-\beta]=1$. Thus $\beta\notin\sigma(f(a))$; that is, $\sigma(f(a))\subseteq f(\sigma(a))$. $\blacksquare$

This section closes with an application of the functional calculus that is typical.

**4.11. Proposition.** *Suppose $a\in\mathcal A$ and $\sigma(a)=F_1\cup F_2$, where $F_1$ and $F_2$ are disjoint nonempty closed sets. Then there is a nontrivial idempotent $e$ in $\mathcal A$ such that*

(a) *if $ba=ab$, then $be=eb$;*

(b) *if $a_1=ae$ and $a_2=a(1-e)$, then $a=a_1+a_2$ and $a_1a_2=a_2a_1=0$;*

(c) *$\sigma(a_1)=F_1\cup\{0\}$, $\sigma(a_2)=F_2\cup\{0\}$.*

**Proof.** Let $G_1,G_2$ be disjoint open subsets of $\mathbb C$ such that $F_j\subset G_j$, $j=1,2$. Let $\Gamma$ be a positively oriented system of closed curves in $G_1$ such that $F_1\subseteq\operatorname{ins}\Gamma$, $F_2\subseteq\operatorname{out}\Gamma$. If $f=$ the characteristic function of $G_1$, $f\in\operatorname{Hol}(a)$; let $e=f(a)$. Since $f^2=f$, $e^2=e$. Part (a) follows from (4.9).

Note that $e(1-e)=0=(1-e)e$. Hence (b) is immediate. Let $f_1(z)=zf(z)$, $f_2(z)=z(1-f(z))$. It follows from (4.7a) that $a_j=f_j(a)$, $j=1,2$. Hence the Spectral Mapping Theorem implies that $\sigma(a_j)=f_j(\sigma(a))=F_j\cup\{0\}$. The proof that $e$ is neither 0 nor 1 is left to the reader. $\blacksquare$

Part (c) of the preceding proposition has the somewhat unattractive conclusion that $\sigma(a_1)=F_1\cup\{0\}$. It would be much neater if the conclusion were that $\sigma(a_1)=F_1$. This is, in a sense, the case. Since $a_1(1-e)=0$ and
