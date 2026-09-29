conjugation. Indeed, a subalgebra of $C(X)$ having these properties is called a *uniform algebra* or *function algebra* and their study forms a separate area of mathematics (Gamelin [1969]). One example (the most famous) is obtained by letting $X$ be a subset of $\mathbb{C}$ and letting $\mathcal{A}=R(X)\equiv$ the uniform closure of rational functions with poles off $X$.

Let $x_0,x_1\in X$, $x_0\ne x_1$, and let $\mathcal{A}\equiv\{f\in C(X):f(x_0)=f(x_1)\}$. Then $\mathcal{A}$ is a uniformly closed subalgebra of $C(X)$, contains the constant functions, and is closed under conjugation. In a certain sense this is the worst that can happen if the only hypothesis of the Stone–Weierstrass Theorem that does not hold is that $\mathcal{A}$ fails to separate the points of $X$ (see Exercise 4).

If $X$ is only assumed to be locally compact, then the story is similar.

**8.3. Corollary.** *If $X$ is locally compact and $\mathcal{A}$ is a closed subalgebra of $C_0(X)$ such that*

(a) *for each $x$ in $X$ there is an $f$ in $\mathcal{A}$ such that $f(x)\ne 0$;*  
(b) *$\mathcal{A}$ separates the points of $X$;*  
(c) *$\overline{f}\in\mathcal{A}$ whenever $f\in\mathcal{A}$;*

*then $\mathcal{A}=C_0(X)$.*

**Proof.** Let $X_\infty=$ the one point compactification of $X$ and identify $C_0(X)$ with $\{f\in C(X_\infty):f(\infty)=0\}$. So $\mathcal{A}$ becomes a subalgebra of $C(X_\infty)$. Now apply Corollary 8.2. The details are left to the reader. $\blacksquare$

What are the extreme points of the unit ball of $M(X)$? The characterization of these extreme points as well as the extreme points of the set $P(X)$ of probability measures on $X$ is given in the next theorem. [A probability measure is a positive measure $\mu$ such that $\mu(X)=1$.]

**8.4. Theorem.** *If $X$ is compact, then the set of extreme points of ball $M(X)$ is*

$$
\{\alpha\delta_x:|\alpha|=1\text{ and }x\in X\}.
$$

*The set of extreme points of $P(X)$, the probability measures on $X$, is*

$$
\{\delta_x:x\in X\}.
$$

**Proof.** It is left as an exercise for the reader to show that if $x\in X$, $\delta_x$ is an extreme point of $P(X)$ and $\alpha\delta_x$ is an extreme point of ball $M(X)$ (Exercise 3).

It will now be shown that if $\mu$ is an extreme point of $P(X)$, then $\mu$ is an extreme point of ball $M(X)$. Thus the first part of the theorem implies the second. Suppose $\mu$ is an extreme point of $P(X)$ and $\nu_1,\nu_2\in\operatorname{ball}M(X)$ such that $\mu=\frac12(\nu_1+\nu_2)$. Then $1=\|\mu\|\le\frac12(\|\nu_1\|+\|\nu_2\|)\le 1$; hence $\|\nu_1\|+\|\nu_2\|=2$ and so $\|\nu_1\|=\|\nu_2\|=1$. Also, $1=\mu(X)=\frac12(\nu_1(X)+\nu_2(X))$. Now $|\nu_1(X)|,|\nu_2(X)|\le 1$ and $1$ is an extreme point of $\{\alpha\in\mathbb{F}:|\alpha|\le 1\}$. Hence for $k=1,2$, $\|\nu_k\|=\nu_k(X)=1$. By Exercise III.7.2, $\nu_k\in P(X)$ for $k=1,2$. Since $\mu\in\operatorname{ext}P(X)$, $\mu=\nu_1=\nu_2$. So $\mu$ is an extreme point of ball $M(X)$. Thus it suffices to prove the first part of the theorem.
