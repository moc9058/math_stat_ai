92  III. Banach Spaces

$(f_n,f_n')\to(f,g)$ in $\mathscr X\times\mathscr Y$, then $f_n'\to g$ uniformly on $[0,1]$. Hence

$$
f_n(t)-f_n(0)=\int_0^t f_n'(s)\,ds\to\int_0^t g(s)\,ds.
$$

But $f_n(t)-f_n(0)\to f(t)-f(0)$, so

$$
f(t)=f(0)+\int_0^t g(s)\,ds.
$$

Thus $f'=g$ and gra $A$ is closed. However, $A$ is not bounded. (Why?)

The preceding example shows that the domain of the operator in the Closed Graph Theorem must be assumed to be complete. The next example (due to Alp Eden) shows that the range must also be assumed to be complete.

Let $\mathscr X$ be a separable infinite-dimensional Banach space and let $\{e_i:i\in I\}$ be a Hamel basis for $\mathscr X$ with $\|e_i\|=1$ for all $i$. Note that a Baire Category argument shows that $I$ is uncountable. If $x\in\mathscr X$, then $x=\sum_i\alpha_i e_i$, $\alpha_i\in\mathbb F$, and $\alpha_i=0$ for all but a finite number of $i$ in $I$. Define $\|x\|_1\equiv\sum_i|\alpha_i|$. It is left as an exercise for the reader to show that $\|\cdot\|_1$ is a norm on $\mathscr X$. Since $\|e_i\|=1$ for all $i$, $\|x\|\leq\sum_i|\alpha_i|=\|x\|_1$. Let $\mathscr Y=\mathscr X$ with the norm $\|\cdot\|_1$ and let $T:\mathscr Y\to\mathscr X$ be defined by $T(x)=x$. Note that it was just shown that $T:\mathscr Y\to\mathscr X$ is a contraction. Therefore gra $T$ is closed and hence so is gra $T^{-1}$. But $T^{-1}$ is not continuous because if it were, then $T$ would be a homeomorphism. Since $\mathscr X$ is separable, it would follow that $\mathscr Y$ is separable. But $\mathscr Y$ is not separable. To see this, note that $\|e_i-e_j\|_1=2$ for $i\ne j$ and since $I$ is uncountable, $\mathscr Y$ cannot be separable.

When applying the Closed Graph Theorem, the following result is useful.

**12.7. Proposition.** *If $\mathscr X$ and $\mathscr Y$ are normed spaces and $A:\mathscr X\to\mathscr Y$ is a linear transformation, then gra $A$ is closed if and only if whenever $x_n\to0$ and $Ax_n\to y$, it must be that $y=0$.*

PROOF. Exercise 3.

Note that (12.7) underlines the advantage of the Closed Graph Theorem. To show that $A$ is continuous, it suffices to show that if $x_n\to0$, then $Ax_n\to0$. By (12.7) this is eased by allowing us to assume that $\{Ax_n\}$ is convergent.

It is possible to give a measure-theoretic solution to Exercise 2.3, but here is one using the Closed Graph Theorem. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space, $1\leq p\leq\infty$, and $\phi:X\to\mathbb F$ an $\Omega$-measurable function such that $\phi f\in L^p(\mu)$ whenever $f\in L^p(\mu)$. Define $A:L^p(\mu)\to L^p(\mu)$ by $Af=\phi f$. Thus $A$ is linear and well defined. Suppose $f_n\to0$ and $\phi f_n\to g$ in $L^p(\mu)$. If $1\leq p<\infty$, then $f_n\to0$ in measure. By a theorem of Riesz, there is a subsequence $\{f_{n_k}\}$ such that $f_{n_k}(x)\to0$ a.e. $[\mu]$. Hence $\phi(x)f_{n_k}(x)\to0$ a.e. $[\mu]$. This implies $g=0$ and so gra $A$ is closed. If $p=\infty$, then $f_n(x)\to0$ a.e. $[\mu]$ and the same argument implies gra $A$ is closed. By the Closed Graph Theorem, $A$ is bounded. Clearly, it may be assumed that $\|A\|=1$. If $\delta>0$, let $E$ be a measurable subset of
