$\bigcap_{k=0}^{n-1}F_k^\circ\cap A$. Note that $Q$ is $\mathrm{wk}^*$ compact. So if $Q\cap F^\circ\neq\square$ for every finite subset $F$ of $n^{-1}\operatorname{ball}\mathcal X$, then $\square\neq Q\cap\bigcap\{F^\circ:F\text{ is a finite subset of }n^{-1}(\operatorname{ball}\mathcal X)\}=Q\cap[n(\operatorname{ball}\mathcal X^*)]$ by the preceding lemma. This contradicts (12.4ii). Therefore there is a finite subset $F_n$ of $n^{-1}(\operatorname{ball}\mathcal X)$ such that $Q\cap F_n^\circ=\square$. This proves (12.4).

If $\{F_n\}_{n=1}^{\infty}$ satisfies (12.4), then $A\cap\bigcap_{n=1}^{\infty}F_n^\circ=\square$. Arrange the elements of $\bigcup_{n=1}^{\infty}F_n$ in a sequence and denote this sequence by $\{x_n\}$. Note that $\lim\|x_n\|=0$. Thus if $x^*\in\mathcal X^*$, $\{\langle x_n,x^*\rangle\}\in c_0$. Define $T:\mathcal X^*\to c_0$ by $T(x^*)=\{\langle x_n,x^*\rangle\}$. It is easy to see that $T$ is linear (and bounded, though this fact is unnecessary). Hence $T(A)$ is a convex subset of $c_0$. Also, from the construction of $\{x_n\}=\bigcup_{n=1}^{\infty}F_n$, for each $x^*$ in $A$, $\|T(x^*)\|=\sup_n|\langle x_n,x^*\rangle|>1$. That is, $T(A)\cap\operatorname{ball}c_0=\square$. Thus Theorem IV.3.7 applies to the sets $T(A)$ and $\operatorname{int}[\operatorname{ball}c_0]$ and there is an $f$ in $\ell^1=c_0^*$ and an $\alpha$ in $\mathbb R$ such that $\operatorname{Re}\langle\phi,f\rangle<\alpha\leq\operatorname{Re}\langle T(x^*),f\rangle$ for every $\phi$ in $\operatorname{int}[\operatorname{ball}c_0]$ and $x^*$ in $A$. That is

$$
\operatorname{Re}\sum_{n=1}^{\infty}\phi(n)f(n)
<\alpha\leq
\operatorname{Re}\sum_{n=1}^{\infty}\langle x_n,x^*\rangle f(n).
\tag{12.5}
$$

for every $\phi$ in $c_0$ with $\|\phi\|<1$ and for every $x^*$ in $A$. Replacing $f$ by $f/\|f\|$ and $\alpha$ by $\alpha/\|f\|$, it is clear that it may be assumed that (12.5) holds with $\|f\|=1$. If $\phi\in c_0$, $\|\phi\|<1$, let $\mu\in\mathbb F$ such that $|\mu|=1$ and $\langle\mu\phi,f\rangle=|\langle\phi,f\rangle|$. Applying this to (12.5) and taking the supremum over all $\phi$ in $\operatorname{int}[\operatorname{ball}c_0]$ gives that $1\leq\operatorname{Re}\sum_{n=1}^{\infty}\langle x_n,x^*\rangle f(n)$ for all $x^*$ in $A$. But $f\in\ell^1$ so $x=\sum_{n=1}^{\infty}f(n)x_n\in\mathcal X$ and $1\leq\operatorname{Re}\langle x,x^*\rangle$ for all $x^*$ in $A$. $\blacksquare$

Where was the completeness of $\mathcal X$ used in the preceding proof?

**Proof of the Krein–Smulian Theorem.** Let $x_0^*\in\mathcal X^*\setminus A$; it will be shown that $x_0^*\notin\mathrm{wk}^*-\operatorname{cl}A$. It is easy to see that $A$ is norm closed. So there is an $r>0$ such that $\{x^*\in\mathcal X^*:\|x^*-x_0^*\|\leq r\}\cap A=\square$. But this implies that $\operatorname{ball}\mathcal X^*\cap[r^{-1}(A-x_0^*)]=\square$. With this it is easy to see that $r^{-1}(A-x_0^*)$ satisfies the hypothesis of the preceding lemma. Therefore there is an $x$ in $\mathcal X$ such that $\operatorname{Re}\langle x,x^*\rangle\geq1$ for all $x^*$ in $r^{-1}(A-x_0^*)$. In particular, $0\notin\mathrm{wk}^*-\operatorname{cl}[r^{-1}(A-x_0^*)]$ and hence $x_0^*\notin\mathrm{wk}^*-\operatorname{cl}A$. $\blacksquare$

**12.6. Corollary.** *If $\mathcal X$ is a Banach space and $\mathcal Y$ is a linear manifold in $\mathcal X^*$, then $\mathcal Y$ is weak-star closed if and only if $\mathcal Y\cap\operatorname{ball}\mathcal X^*$ is weak-star closed.*

**12.7. Corollary.** *If $\mathcal X$ is a separable Banach space and $A$ is a convex subset of $\mathcal X^*$ that is weak-star sequentially closed, then $A$ is weak-star closed.*

**Proof.** Because $\mathcal X$ is separable, $r(\operatorname{ball}\mathcal X^*)$ is weak-star metrizable for every $r>0$ (Theorem 5.1). So if $A$ is weak-star sequentially closed, $A\cap[r(\operatorname{ball}\mathcal X^*)]$ is weak-star closed for every $r>0$. Hence the Krein–Smulian Theorem applies. $\blacksquare$
