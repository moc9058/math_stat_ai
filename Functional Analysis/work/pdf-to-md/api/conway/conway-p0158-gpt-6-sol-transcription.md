and $b\in V_b$. By the claim $V_a\cup U=K$ since $a\notin U$. But $b\notin V_a\cup U$, a contradiction. Thus $K\setminus U=\{a\}$ and $a\in\operatorname{ext}K$ by (7.3e). Hence $\operatorname{ext}K\ne\square$.

Note that we have actually proved the following.

**7.6** If $V$ is an open convex subset of $\mathcal X$ and $\operatorname{ext}K\subseteq V$, then $K\subseteq V$.

Assume (7.6) is false. That is, assume there is an open convex subset $V$ of $\mathcal X$ such that $\operatorname{ext}K\subseteq V$ but $V\cap K\ne K$. Then $V\cap K\in\mathcal U$ and is contained in a maximal element $U$ of $\mathcal U$. Since $K\setminus U=\{a\}$ for some $a$ in $\operatorname{ext}K$, this is a contradiction. Thus (7.6) holds.

Let $E=\overline{\operatorname{co}}(\operatorname{ext}K)$. If $x^*\in\mathcal X^*$, $\alpha\in\mathbb R$, and $E\subseteq\{x\in\mathcal X:\operatorname{Re}\langle x,x^*\rangle<\alpha\}=V$, then $K\subseteq V$ by (7.6). Thus the Hahn–Banach Theorem (IV.3.13) implies $E=K$. $\blacksquare$

The Krein–Milman Theorem seems innocent enough, but it has widespread application. Two such applications will be seen in Sections 8 and 10; another will occur later when $C^*$-algebras are studied. Here a small application is given.

If $\mathcal X$ is a Banach space, then $\operatorname{ball}\mathcal X^*$ is weak* compact by Alaoglu’s Theorem. By the Krein–Milman Theorem, $\operatorname{ball}\mathcal X^*$ has many extreme points. Keep this in mind.

**7.7. Example.** $c_0$ is not the dual of a Banach space. That is, $c_0$ is not isometrically isomorphic to the dual of a Banach space. In light of the preceding comments, in order to prove this statement, it suffices to show that $\operatorname{ball}c_0$ has few extreme points. In fact, $\operatorname{ball}c_0$ has no extreme points. Let $x\in\operatorname{ball}c_0$. It must be that $0=\lim x(n)$. Let $N$ be such that $|x(n)|<\frac12$ for $n\geq N$. Define $y_1,y_2$ in $c_0$ by letting $y_1(n)=y_2(n)=x(n)$ for $n\leq N$, and for $n>N$ let $y_1(n)=x(n)+2^{-n}$ and $y_2(n)=x(n)-2^{-n}$. It is easy to check that $y_1$ and $y_2\in\operatorname{ball}c_0$, $\frac12(y_1+y_2)=x$, and $y_1\ne x$.

In light of Example 7.2(f), $L^1[0,1]$ is not the dual of a Banach space.

The next two results are often useful in applying the Krein–Milman Theorem. Indeed, the first is often taken as part of that result.

**7.8. Theorem.** *If $\mathcal X$ is a LCS, $K$ is a compact convex subset of $\mathcal X$, and $F\subseteq K$ such that $K=\overline{\operatorname{co}}(F)$, then $\operatorname{ext}K\subseteq\operatorname{cl}F$.*

**Proof.** Clearly it suffices to assume that $F$ is closed. Suppose that there is an extreme point $x_0$ of $K$ such that $x_0\notin F$. Let $p$ be a continuous seminorm on $\mathcal X$ such that $F\cap\{x\in\mathcal X:p(x-x_0)<1\}=\square$. Let $U_0=\{x\in\mathcal X:p(x)<\frac13\}$. So $(x_0+U_0)\cap(F+U_0)=\square$; hence $x_0\notin\operatorname{cl}(F+U_0)$.

Because $F$ is compact, there are $y_1,\ldots,y_n$ in $F$ such that $F\subseteq\bigcup_{k=1}^{n}(y_k+U_0)$. Let $K_k=\overline{\operatorname{co}}(F\cap(y_k+U_0))$. Thus $K_k\subseteq y_k+\operatorname{cl}U_0$ (Why?), and $K_k\subseteq K$. Now that fact that $K_1,\ldots,K_n$ are compact and convex implies that $\overline{\operatorname{co}}(K_1\cup\cdots\cup K_n)=\operatorname{co}(K_1\cup\cdots\cup K_n)$ (Exercise 8). Therefore

$$
K=\overline{\operatorname{co}}(F)=\operatorname{co}(K_1\cup\cdots\cup K_n).
$$
