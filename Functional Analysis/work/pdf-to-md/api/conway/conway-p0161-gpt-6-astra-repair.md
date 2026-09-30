146　　　　　　　　　　　　　　　　　V. Weak Topologies

Let $x\in X$, $x\ne x_0$. By (b) there is an $f_1$ in $\mathcal A$ such that $f_1(x_0)\ne f_1(x)=\beta$. By (a), the function $\beta\in\mathcal A$. Hence $f_2=f_1-\beta\in\mathcal A$, $f_2(x_0)\ne 0=f_2(x)$. By (c), $f_3=|f_2|^2=f_2\overline{f_2}\in\mathcal A$. Also, $f_3(x)=0<f_3(x_0)$ and $f_3\geq 0$. Put $f=(\|f_3\|+1)^{-1}f_3$. Then $f\in\mathcal A$, $f(x)=0$, $f(x_0)>0$, and $0\leq f<1$ on $X$. Moreover, because $\mathcal A$ is an algebra, $gf$ and $g(1-f)\in\mathcal A$ for every $g$ in $\mathcal A$. Because $\mu\in\mathcal A^\perp$, $0=\int gf\,d\mu=\int g(1-f)\,d\mu$ for every $g$ in $\mathcal A$. Therefore $f\mu$ and $(1-f)\mu\in\mathcal A^\perp$.

(For any bounded Borel function $h$ on $X$, $h\mu$ denotes the measure whose value at a Borel set $\Delta$ is $\int_\Delta h\,d\mu$. Note that $\|h\mu\|=\int |h|\,d|\mu|$.)

Put $\alpha=\|f\mu\|=\int f\,d|\mu|$. Since $f(x_0)>0$, there is an open neighborhood $U$ of $x_0$ and an $\varepsilon>0$ such that $f(y)>\varepsilon$ for $y$ in $U$. Thus, $\alpha=\int f\,d|\mu|\geq\int_U f\,d|\mu|\geq\varepsilon|\mu|(U)>0$ since $U\cap K\ne\square$. Similarly, since $f(x_0)<1$, $\alpha<1$. Therefore, $0<\alpha<1$. Also, $1-\alpha=1-\int f\,d|\mu|=\int(1-f)\,d|\mu|=\|(1-f)\mu\|$. Since

$$
\mu=\alpha\left[\frac{f\mu}{\|f\mu\|}\right]+(1-\alpha)\left[\frac{(1-f)\mu}{\|(1-f)\mu\|}\right]
$$

and $\mu$ is an extreme point of ball $\mathcal A^\perp$, $\mu=f\mu\|f\mu\|^{-1}=\alpha^{-1}f\mu$. But the only way that the measures $\mu$ and $\alpha^{-1}f\mu$ can be equal is if $\alpha^{-1}f=1$ a.e. $[\mu]$. Since $f$ is continuous, it must be that $f=\alpha$ on $K$. Since $x_0\in K$, $f(x_0)=\alpha$. But $f(x_0)>f(x)=0$. Hence $x\notin K$. This establishes that $K=\{x_0\}$ and so $\mu=\gamma\delta_{x_0}$ where $|\gamma|=1$. But $\mu\in\mathcal A^\perp$ and $1\in\mathcal A$, so $0=\int 1\,d\mu=\gamma$, a contradiction. Therefore $\mathcal A^\perp=(0)$ and $\mathcal A=C(X)$. $\blacksquare$

With an important theorem it is good to ask what happens if part of the hypothesis is deleted. If $x_0\in X$ and $\mathcal A=\{f\in C(X):f(x_0)=0\}$, then $\mathcal A$ is a closed subalgebra of $C(X)$ that satisfies (b) and (c) but $\mathcal A\ne C(X)$. This is the worst that can happen.

**8.2. Corollary.** *If $X$ is compact and $\mathcal A$ is a closed subalgebra of $C(X)$ that separates the points of $X$ and is closed under complex conjugation, then either $\mathcal A=C(X)$ or there is a point $x_0$ in $X$ such that $\mathcal A=\{f\in C(X):f(x_0)=0\}$.*

**Proof.** Identify $\mathbb F$ and the one-dimensional subspace of $C(X)$ consisting of the constant functions. Since $\mathcal A$ is closed, $\mathcal A+\mathbb F$ is closed (III.4.3). It is easy to see that $\mathcal A+\mathbb F$ is an algebra and satisfies the hypothesis of the Stone–Weierstrass Theorem; hence $\mathcal A+\mathbb F=C(X)$. Suppose $\mathcal A\ne C(X)$. Then $C(X)/\mathcal A$ is one dimensional; thus $\mathcal A^\perp$ is one dimensional (Theorem 2.2). Let $\mu\in\mathcal A^\perp$, $\|\mu\|=1$. If $f\in\mathcal A$, then $f\mu\in\mathcal A^\perp$; hence there is an $\alpha$ in $\mathbb F$ such that $f\mu=\alpha\mu$. This implies that each $f$ in $\mathcal A$ is constant on the support of $\mu$. But the functions in $\mathcal A$ separate the points of $X$. Hence the support of $\mu$ is a single point $x_0$ and so $\mathcal A^\perp=\{\beta\delta_{x_0}:\beta\in\mathbb F\}$. Thus $\mathcal A=\mathcal A^\perp=\{f\in C(X):f(x_0)=0\}$. $\blacksquare$

There are many examples of subalgebras of $C(X)$ that separate the points of $X$, contain the constants, but are not necessarily closed under complex
