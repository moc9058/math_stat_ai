$$
\operatorname{cl}K(S)\subseteq\bigcup_{T\in\mathcal A}\{y:\|Ty-x_0\|<1\}.
$$

Because $\operatorname{cl}K(S)$ is compact, there are $T_1,\ldots,T_n$ in $\mathcal A$ such that

$$
\operatorname{cl}K(S)\subseteq\bigcup_{j=1}^{n}\{y:\|T_jy-x_0\|<1\}. \tag{4.11}
$$

For $y$ in $\operatorname{cl}K(S)$ and $1\leq j\leq n$, let $a_j(y)=\max\{0,1-\|T_jy-x_0\|\}$. By (4.11), $\sum_{j=1}^{n}a_j(y)>0$ for all $y$ in $\operatorname{cl}K(S)$. Define $b_j:\operatorname{cl}K(S)\to\mathbb R$ by

$$
b_j(y)=\frac{a_j(y)}{\sum_{i=1}^{n}a_i(y)},
$$

and define $\psi:S\to\mathcal X$ by

$$
\psi(x)=\sum_{j=1}^{n}b_j(Kx)T_jKx.
$$

It is easy to see that $a_j:\operatorname{cl}K(S)\to[0,1]$ is a continuous function. Hence $b_j$ and $\psi$ are continuous.

If $x\in S$, then $Kx\in K(S)$. If $b_j(Kx)>0$, then $a_j(Kx)>0$ and so $\|T_jKx-x_0\|<1$. That is, $T_jKx\in S$ whenever $b_j(Kx)>0$. Since $S$ is a convex set and $\sum_{j=1}^{n}b_j(Kx)=1$ for $x$ in $S$,

$$
\psi(S)\subseteq S.
$$

Note that $T_jK\in\mathcal B_0(\mathcal X)$ for each $j$ so that $\bigcup_{j=1}^{n}T_jK(S)$ has compact closure. By Mazur’s Theorem, $\overline{\operatorname{co}}\bigl(\bigcup_{j=1}^{n}T_jK(S)\bigr)$ is compact. But this convex set contains $\psi(S)$ so that $\operatorname{cl}\psi(S)$ is compact. This is, $\psi$ is a compact map. By the Schauder Fixed-Point Theorem, there is a vector $x_1$ in $S$ such that $\psi(x_1)=x_1$.

Let $\beta_j=b_j(Kx_1)$ and put $A=\sum_{j=1}^{n}\beta_jT_j$. So $A\in\mathcal A$ and $AKx_1=\psi(x_1)=x_1$. Since $x_1\ne0$ (Why?), $\ker(AK-1)\ne0$. ■

**4.12. Definition.** If $T\in\mathcal B(\mathcal X)$, then a *hyperinvariant subspace* for $T$ is a subspace $\mathcal M$ of $\mathcal X$ such that $A\mathcal M\subseteq\mathcal M$ for every operator $A$ in the commutant of $T$, $\{T\}'$; that is, $A\mathcal M\subseteq\mathcal M$ whenever $AT=TA$.

Note that every hyperinvariant subspace for $T$ is invariant.

**4.13. Lomonosov’s Theorem.** *If $\mathcal X$ is a Banach space over $\mathbb C$, $T\in\mathcal B(\mathcal X)$, $T$ is not a multiple of the identity, and $TK=KT$ for some nonzero compact operator $K$, then $T$ has a nontrivial hyperinvariant subspace.*

**Proof.** Let $\mathcal A=\{T\}'$. We want to show that $\operatorname{Lat}\mathcal A\ne\{(0),\mathcal X\}$. If this is not the case, then Lomonosov’s Lemma implies that there is an operator $A$ in $\mathcal A$ such that $\mathcal N=\ker(AK-1)\ne(0)$. But $\mathcal N\in\operatorname{Lat}(AK)$ and $AK|_{\mathcal N}$ is the
