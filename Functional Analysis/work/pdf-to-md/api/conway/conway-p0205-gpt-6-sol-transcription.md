**1.11. Example.** Let $G$ be a $\sigma$-compact locally compact group and let $m=$ right Haar measure on $G$. That is, $m$ is a non-negative regular Borel measure on $G$ such that $m(U)>0$ for every nonempty open subset $U$ of $G$ and $\int f(xy)\,dm(x)=\int f(x)\,dm(x)$ for every $f$ in $C_c(G)$ (the continuous functions $f:G\to\mathbb F$ with compact support). If $G$ is compact, the existence of $m$ was established in Section V.11. If $G$ is not compact, $m$ exists but its existence must be established by nonfunctional analytic methods. If $G$ is not assumed to be $\sigma$-compact, then a Haar measure exists but it is not regular in the sense defined in this book. (See Nachbin [1965].)

If $f,g\in L^1(m)$, let $\mu=fm$ and $\nu=gm$ as in the proof of (V.8.1). Then $\mu,\nu\in M(G)$ and $\|\mu\|=\|f\|_1$, $\|\nu\|=\|g\|_1$. In fact, the Radon–Nikodym Theorem makes it possible to identify $L^1(m)$ with a closed subspace of $M(G)$. Is it a closed subalgebra?

Let $\phi\in C_c(G)$. Then

$$
\begin{aligned}
\int \phi\,d(\mu*\nu)
&=\int\!\!\int \phi(xy)f(x)g(y)\,dm(x)\,dm(y)\\
&=\int g(y)\left[\int \phi(xy)f(x)\,dm(x)\right]dm(y)\\
&=\int g(y)\left[\int \phi(x)f(xy^{-1})\,dm(x)\right]dm(y)\\
&=\int \phi(x)\left[\int f(xy^{-1})g(y)\,dm(y)\right]dm(x)\\
&=\int \phi(x)h(x)\,dm(x),
\end{aligned}
$$

where $h(x)=\int f(xy^{-1})g(y)\,dm(y)$, $x$ in $G$. It follows that $h\in L^1(m)$ (see Exercise 4). Thus $\mu*\nu=hm$, so $L^1(m)$ is a Banach subalgebra of $M(G)$. In fact, the preceding discussion enables us to define $f*g$ in $L^1(m)$ for $f,g$ in $L^1(m)$ by

$$
f*g(x)=\int f(xy^{-1})g(y)\,dm(y).
$$

The algebra $L^1(m)$ is denoted by $L^1(G)$.

It can be shown that $L^1(G)$ is abelian if and only if $G$ is abelian and $L^1(G)$ has an identity if and only if $G$ is discrete (in which case $L^1(G)=M(G)$—what is $m$?). This algebra is examined more closely in Section 9.

If $\{\mathcal A_i\}$ is a collection of Banach algebras, let
$$
\bigoplus_0\mathcal A_i
\equiv
\left\{a\in\prod_i\mathcal A_i:\text{ for all }\varepsilon>0,\ \{i:\|a(i)\|\geq\varepsilon\}\text{ is finite}\right\}.
$$

**1.12. Proposition.** *If $\{\mathcal A_i\}$ is a collection of Banach algebras, $\bigoplus_0\mathcal A_i$ and $\bigoplus_\infty\mathcal A_i$ are Banach algebras.*

**Proof.** Exercise.
