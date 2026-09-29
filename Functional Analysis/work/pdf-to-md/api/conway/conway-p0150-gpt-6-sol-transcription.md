definition of the relative weak-star topology on ball $\mathcal X^*$, for each $n$ there is a finite set $F_n$ contained in $\mathcal X$ such that $\{x^*\in\operatorname{ball}\mathcal X^*:|\langle x,x^*\rangle|<1\text{ for all }x\text{ in }F_n\}\subseteq U_n$. Let $F=\bigcup_{n=1}^{\infty}F_n$; so $F$ is countable. Also, ${}^{\perp}(F^{\perp})$ is the closed linear span of $F$ and this subspace of $\mathcal X$ is separable. But if $x^*\in F^{\perp}$, then for each $n\geqslant1$ and for each $x$ in $F_n$, $|\langle x,x^*/\|x^*\|\rangle|=0<1$. Hence $x^*/\|x^*\|\in U_n$ for all $n\geqslant1$; thus $x^*=0$. Since $F^{\perp}=(0)$, ${}^{\perp}(F^{\perp})=\mathcal X$ and $\mathcal X$ must be separable. $\blacksquare$

Is there a corresponding result for the weak topology? If $\mathcal X^*$ is separable, then the weak topology on ball $\mathcal X$ is metrizable. In fact, this follows from Theorem 5.1 if the embedding of $\mathcal X$ into $\mathcal X^{**}$ is considered. This result is not very useful since there are few examples of Banach spaces $\mathcal X$ such that $\mathcal X^*$ is separable. Of course if $\mathcal X$ is separable and reflexive, then $\mathcal X^*$ is separable (Exercise 3), but in this case the weak topology on $\mathcal X$ is the same as its weak-star topology when $\mathcal X$ is identified with $\mathcal X^{**}$. Thus (5.1) is adequate for a discussion of the weak topology on the unit ball of a separable reflexive space. If $\mathcal X=c_0$, then $\mathcal X^*=l^1$ and this is separable but not reflexive. This is one of the few nonreflexive spaces with a separable dual space.

If $\mathcal X$ is separable, is (ball $\mathcal X$, wk) metrizable? The answer is no, as the following result of Schur demonstrates.

**5.2. Proposition.** *If a sequence in $l^1$ converges weakly, it converges in norm.*

**Proof.** Recall that $l^\infty=(l^1)^*$. Since $l^1$ is separable, Theorem 5.1 implies that ball $l^\infty$ is $\mathrm{wk}^*$ metrizable. By Alaoglu’s Theorem, ball $l^\infty$ is $\mathrm{wk}^*$ compact. Hence (ball $l^\infty$, $\mathrm{wk}^*$) is a complete metric space and the Baire Category Theorem is applicable.

Let $\{f_n\}$ be a sequence of elements in $l^1$ such that $f_n\to0$ weakly and let $\varepsilon>0$. For each positive integer $m$ let

$$
F_m=\{\phi\in\operatorname{ball}l^\infty:|\langle f_n,\phi\rangle|\leqslant\varepsilon/3\text{ for }n\geqslant m\}.
$$

It is easy to see that $F_m$ is $\mathrm{wk}^*$ closed in ball $l^\infty$ and, because $f_n\to0(\mathrm{wk})$, $\bigcup_{m=1}^{\infty}F_m=\operatorname{ball}l^\infty$. By the theorem of Baire, there is an $F_m$ with non-empty weak-star interior.

An equivalent metric on (ball $l^\infty$, $\mathrm{wk}^*$) is given by

$$
d(\phi,\psi)=\sum_{j=1}^{\infty}2^{-j}|\phi(j)-\psi(j)|
$$

(see Exercise 4). Since $F_m$ has a nonempty $\mathrm{wk}^*$ interior, there is a $\phi$ in $F_m$ and a $\delta>0$ such that $\{\psi\in\operatorname{ball}l^\infty:d(\phi,\psi)<\delta\}\subseteq F_m$. Let $J\geqslant1$ such that $2^{-(J-1)}<\delta$. Fix $n\geqslant m$ and define $\psi$ in $l^\infty$ by $\psi(j)=\phi(j)$ for $1\leqslant j\leqslant J$ and $\psi(j)=\operatorname{sign}(f_n(j))$ for $j>J$. Thus $\psi(j)f_n(j)=|f_n(j)|$ for $j>J$. It is easy to see that $\psi\in\operatorname{ball}l^\infty$. Also, $d(\phi,\psi)=\sum_{j=J+1}^{\infty}2^{-j}|\phi(j)-\psi(j)|\leqslant2\cdot2^{-J}=2^{-(J-1)}<\delta$.
