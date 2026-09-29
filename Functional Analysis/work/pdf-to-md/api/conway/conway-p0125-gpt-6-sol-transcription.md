**3.6. Proposition.** Let $\mathcal{X}$ be a real TVS.

(a) The closure of an open half-space is a closed half-space and the interior of a closed half-space is an open half-space.

(b) If $A,B\subseteq\mathcal{X}$, then $A$ and $B$ are strictly separated (separated) if and only if there is a continuous linear functional $f:\mathcal{X}\to\mathbb{R}$ and a real scalar $\alpha$ such that $f(a)>\alpha$ for all $a$ in $A$ and $f(b)<\alpha$ for all $b$ in $B$ ($f(a)\geq\alpha$ for all $a$ in $A$ and $f(b)\leq\alpha$ for all $b$ in $B$).

**Proof.** Exercise 6.

In many ways, the next result is the most important “separation” theorem as the other separation theorems follow from this one. However, the most used separation theorem is Theorem 3.9 below.

**3.7. Theorem.** If $\mathcal{X}$ is a real TVS and $A$ and $B$ are disjoint convex sets with $A$ open, then there is a continuous linear functional $f:\mathcal{X}\to\mathbb{R}$ and a real scalar $\alpha$ such that $f(a)<\alpha$ for all $a$ in $A$ and $f(b)\geq\alpha$ for all $b$ in $B$. If $B$ is also open, then $A$ and $B$ are strictly separated.

**Proof.** Let $G=A-B\equiv\{a-b:a\in A,b\in B\}$; it is easy to verify that $G$ is convex (do it!). Also, $G=\bigcup\{A-b:b\in B\}$, so $G$ is open. Moreover, because $A\cap B=\varnothing$, $0\notin G$. By Theorem 3.3 there is a closed hyperplane $\mathcal{M}$ in $\mathcal{X}$ such that $\mathcal{M}\cap G=\varnothing$. Let $f:\mathcal{X}\to\mathbb{R}$ be a linear functional such that $\mathcal{M}=\ker f$. Now $f(G)$ is a convex subset of $\mathbb{R}$ and $0\notin f(G)$. Hence either $f(x)>0$ for all $x$ in $G$ or $f(x)<0$ for all $x$ in $G$; suppose $f(x)>0$ for all $x$ in $G$. Thus if $a\in A$ and $b\in B$, $0<f(a-b)=f(a)-f(b)$; that is, $f(a)>f(b)$. Therefore there is a real number $\alpha$ such that

$$
\sup\{f(b):b\in B\}\leq\alpha\leq\inf\{f(a):a\in A\}.
$$

But $f(A)$ and $f(B)$ are open intervals if $B$ is open (Exercise 7), so $f<\alpha$ on $B$ and $f>\alpha$ on $A$. ■

**3.8. Lemma.** If $\mathcal{X}$ is a TVS, $K$ is a compact subset of $\mathcal{X}$, and $V$ is an open subset of $\mathcal{X}$ such that $K\subseteq V$, then there is an open neighborhood of $0$, $U$, such that $K+U\subseteq V$.

**Proof.** Let $\mathcal{U}_0=$ all of the open neighborhoods of $0$. Suppose that for each $U$ in $\mathcal{U}_0$, $K+U$ is not contained in $V$. Thus, for each $U$ in $\mathcal{U}_0$ there is a vector $x_U$ in $K$ and a $y_U$ in $U$ such that $x_U+y_U\in\mathcal{X}\setminus V$. Order $\mathcal{U}_0$ by reverse inclusion; that is, $U_1\geq U_2$ if $U_1\subseteq U_2$. Then $\mathcal{U}_0$ is a directed set and $\{x_U\}$ and $\{y_U\}$ are nets. Now $y_U\to0$ in $\mathcal{X}$. Because $K$ is compact there is an $x$ in $K$ such that $x_U\underset{\mathrm{cl}}{\longrightarrow}x$ ($\{x_U\}$ cluster at $x$). Hence $x_U+y_U\underset{\mathrm{cl}}{\longrightarrow}x+0=x$. (Why?) Hence $x\in\operatorname{cl}(\mathcal{X}\setminus V)=\mathcal{X}\setminus V$, a contradiction. ■

The condition that $K$ be compact in the preceding lemma is necessary; it is not enough to assume that $K$ is closed. (What is a counterexample?)
