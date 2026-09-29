Since $\|B\|=\|B^*\|$ and $\gamma(A)=\gamma(A^*)$, (a) implies that $\dim\ker(A^*+B^*)\leq\dim\ker A^*$. But this inequality is equivalent to (b).

It remains to prove that $\operatorname{ran}(A+B)$ is closed. Since $A\in\mathcal{SF}$, either $\dim\ker A<\infty$ or $\dim\ker A^*<\infty$. Suppose $\dim\ker A<\infty$. It will be shown that $A+B\in\mathcal{F}_l$ by using Theorem 2.3(f) and showing that if $\delta<\gamma(A)-\|B\|$, then $\{h:\|(A+B)h\|\leq\delta\|h\|\}$ contains no infinite dimensional manifold. Indeed, if it did, it would contain a finite dimensional subspace $\mathcal M$ with $\dim\mathcal M>\dim\ker A$. By Lemma 6.3 there is a non-zero vector $h$ in $\mathcal M$ with $\|h\|=\operatorname{dist}(h,\ker A)$. Now $\|(A+B)h\|\leq\delta\|h\|$, so Lemma 6.4 implies that
$$
\gamma(A)\|h\|=\gamma(A)\operatorname{dist}(h,\ker A)
\leq\|Ah\|\leq\|(A+B)h\|+\|Bh\|
\leq(\delta+\|B\|)\|h\|<\gamma(A)\|h\|,
$$
a contradiction. Thus $A+B\in\mathcal{F}_l$ and so $\operatorname{ran}(A+B)$ is closed.

If $\dim\ker A=\infty$, then $\dim\ker A^*<\infty$. The argument of the preceding paragraph gives that $\operatorname{ran}(A^*+B^*)$ is closed. By (VI.1.10), $\operatorname{ran}(A+B)$ is closed. $\blacksquare$

**6.6. Proposition.** *If $A\in\mathcal{SF}$ and either $\ker A=(0)$ or $\operatorname{ran}A=\mathcal H$, then there is a $\delta>0$ such that if $\|B-A\|<\delta$, then $\dim\ker B=\dim\ker A$ and $\dim\operatorname{ran}B=\dim\operatorname{ran}A$.*

**Proof.** By Proposition 6.5 and Theorem 3.12 there is a $\delta>0$ such that if $\|B-A\|<\delta$, then $\operatorname{ind}A=\operatorname{ind}B$, $\dim\ker B\leq\dim\ker A$, and $\dim(\operatorname{ran}B)^\perp\leq\dim(\operatorname{ran}A)^\perp$. Since one of these dimensions for $A$ is 0, the proposition is proved. $\blacksquare$

If both $\ker A$ and $\operatorname{ran}A$ are nonzero, then there are semi-Fredholm operators $B$ that are arbitrarily close to $A$ such that $\dim\ker B<\dim\ker A$ (see Exercise 2). In fact, just about anything that can go wrong here does go wrong. However, $\dim\ker(A-\lambda)$ does behave rather nicely as a function of $\lambda$.

**6.7. Theorem.** *If $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$, then there is a $\delta>0$ such that $\dim\ker(A-\mu)$ and $\dim(\operatorname{ran}(A-\mu))^\perp$ are constant for $0<|\mu-\lambda|<\delta$.*

**Proof.** We may assume that $\lambda=0$. We may also assume that $\ker A$ is finite dimensional. Indeed, if this is not the case, then $\ker A^*$ must be finite dimensional and the proof that follows applies to $A^*$. But observe that if the conclusion of the theorem is demonstrated for $A^*$, then it also holds for $A$. It follows that for each $n\geq1$, $A^n\in\mathcal{SF}$ (Theorem 3.7). Thus $\mathcal M_n=\operatorname{ran}A^n$ is closed. Note that $\mathcal M_{n+1}\subseteq\mathcal M_n$ and $A\mathcal M_n=\mathcal M_{n+1}$. Let $\mathcal M=\bigcap_{n=1}^{\infty}\mathcal M_n$ and put $B=A|_{\mathcal M}$.

**Claim.** $B\mathcal M=\mathcal M$.

Since $\ker A$ is finite dimensional and the spaces $\mathcal M_n$ are decreasing, there is an integer $m$ such that $\mathcal M_n\cap\ker A=\mathcal M_m\cap\ker A$ for all $n\geq m$. If $h\in\mathcal M$ and $n\geq m$, there is an $f_n$ in $\mathcal M_n$ such that $h=Af_n$. But $f_m-f_n\in(\ker A)\cap\mathcal M_m=(\ker A)\cap\mathcal M_n$. Therefore $f_m\in\mathcal M_n$ for every $n\geq m$. That is, $f_m\in\mathcal M$ and so $h=Af_m=Bf_m\in B\mathcal M$.
