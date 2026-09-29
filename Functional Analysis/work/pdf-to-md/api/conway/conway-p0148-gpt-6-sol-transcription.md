is weakly bounded. By the PUB there is a constant $M$ such that $\|x_n\|\leq M$ for all $n\geq 1$. But $\{x\in\mathcal X:\|x\|\leq M\}$ is weakly compact since $\mathcal X$ is reflexive. Thus there is an $x$ in $\mathcal X$ such that $x_n\xrightarrow[\mathrm{cl}]{}x$ weakly. But for each $x^*$ in $\mathcal X^*$, $\lim\langle x_n,x^*\rangle$ exists. Hence $\langle x_n,x^*\rangle\to\langle x,x^*\rangle$, so $x_n\to x$ weakly. ■

Not all Banach spaces are weakly sequentially complete.

**4.5. Example.** $C[0,1]$ is not weakly sequentially complete. In fact, let $f_n(t)=(1-nt)$ if $0\leq t\leq 1/n$ and $f_n(t)=0$ if $1/n\leq t\leq 1$. If $\mu\in M[0,1]$, then $\int f_n\,d\mu\to\mu(\{0\})$ by the Monotone Convergence Theorem. Hence $\{f_n\}$ is a weakly Cauchy sequence. However, $\{f_n\}$ does not converge weakly to any continuous function on $[0,1]$.

**4.6. Corollary.** *If $\mathcal X$ is a reflexive Banach space, $\mathcal M\leq\mathcal X$, and $x_0\in\mathcal X\setminus\mathcal M$, then there is a point $y_0$ in $\mathcal M$ such that $\|x_0-y_0\|=\operatorname{dist}(x_0,\mathcal M)$.*

**PROOF.** $x\mapsto\|x-x_0\|$ is weakly lower semicontinuous (Exercise 1.9). If $d=\operatorname{dist}(x_0,\mathcal M)$, then $\mathcal M\cap\{x:\|x-x_0\|\leq 2d\}$ is weakly compact and a lower semicontinuous function attains its minimum on a compact set. ■

It is not generally true that the distance from a point to a linear subspace is attained. If $\mathcal M\subseteq\mathcal X$, call $\mathcal M$ *proximinal* if for every $x$ in $\mathcal X$ there is a $y$ in $\mathcal M$ such that $\|x-y\|=\operatorname{dist}(x,\mathcal M)$. So if $\mathcal X$ is reflexive, Corollary 4.6 implies that every closed linear subspace of $\mathcal X$ is proximinal. If $\mathcal X$ is any Banach space and $\mathcal M$ is a finite dimensional subspace, then it is easy to see that $\mathcal M$ is proximinal. How about if $\dim(\mathcal X/\mathcal M)<\infty$?

**4.7. Proposition.** *If $\mathcal X$ is a Banach space and $x^*\in\mathcal X^*$, then $\ker x^*$ is proximinal if and only if there is an $x$ in $\mathcal X$, $\|x\|=1$, such that $\langle x,x^*\rangle=\|x^*\|$.*

**PROOF.** Let $\mathcal M=\ker x^*$ and suppose that $\mathcal M$ is proximinal. If $f:\mathcal X/\mathcal M\to\mathbb F$ is defined by $f(x+\mathcal M)=\langle x,x^*\rangle$, then $f$ is a linear functional and $\|f\|=\|x^*\|$. Since $\dim\mathcal X/\mathcal M=1$, there is an $x$ in $\mathcal X$ such that $\|x+\mathcal M\|=1$ and $f(x+\mathcal M)=\|f\|$. Because $\mathcal M$ is proximinal, there is a $y$ in $\mathcal M$ such that $1=\|x+\mathcal M\|=\|x+y\|$. Thus $\langle x+y,x^*\rangle=\langle x,x^*\rangle=f(x+\mathcal M)=\|f\|=\|x^*\|$.

Now assume that there is an $x_0$ in $\mathcal X$ such that $\|x_0\|=1$ and $\langle x_0,x^*\rangle=\|x^*\|$. If $x\in\mathcal X$ and $\|x+\mathcal M\|=\alpha>0$, then $\|\alpha^{-1}x+\mathcal M\|=1$. But also $\|x_0+\mathcal M\|=1$. (Why?) Since $\dim\mathcal X/\mathcal M=1$, there is a $\beta$ in $\mathbb F$, $|\beta|=1$, such that $\alpha^{-1}x+\mathcal M=\beta(x_0+\mathcal M)$. Hence $\alpha^{-1}x-\beta x_0\in\mathcal M$, or, equivalently, $x-\alpha\beta x_0\in\mathcal M$. However, $\|x-(x-\alpha\beta x_0)\|=\|\alpha\beta x_0\|=\alpha=\operatorname{dist}(x,\mathcal M)$. So the distance from $x$ to $\mathcal M$ is attained at $x-\alpha\beta x_0$. ■

**4.8. Example.** If $L:C[0,1]\to\mathbb F$ is defined by

$$
L(f)=\int_0^{1/2}f(x)\,dx-\int_{1/2}^{1}f(x)\,dx,
$$
