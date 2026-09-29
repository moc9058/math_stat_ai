and $h=1$ on $F$. Put $f_k=\tilde g_kh$ for $1\leqslant k\leqslant n$ and let $f_{n+1}=1-\sum_{k=1}^n f_k$. Clearly $0\leqslant f_k\leqslant 1$ if $1\leqslant k\leqslant n$. If $x\in\operatorname{cl}V$, then $f_{n+1}(x)=1-\left(\sum_{k=1}^n g_k(x)\right)h(x)=1-h(x)$; so $0\leqslant f_{n+1}(x)\leqslant 1$ on $\operatorname{cl}V$. If $x\in X\setminus V$, then $f_{n+1}(x)=1$ since $h(x)=0$. Hence $0\leqslant f_{n+1}\leqslant 1$.

Clearly (a) holds. Let $1\leqslant k\leqslant n$; if $x\in X\setminus U_k$, then either $x\in(\operatorname{cl}V)\setminus U_k$ or $x\in(X\setminus\operatorname{cl}V)\setminus U_k$. If the first alternative is the case, then $g_k(x)=0$, so $f_k(x)=0$. If the second alternative is true, then $h(x)=0$ so that $f_k(x)=0$. If $x\in X\setminus U_{n+1}=F$, then $h(x)=1$ and so $f_{n+1}(x)=1-\sum_{k=1}^n g_k(x)=0$. $\blacksquare$

Partitions of unity are a standard way to put together local results to obtain global results. If $\{f_k\}$ is related to $\{U_k\}$ as in the statement of (6.5), then $\{f_k\}$ is said to be a partition of unity *subordinate to the cover* $\{U_k\}$.

**6.6. Theorem.** *If $X$ is completely regular, then $C_b(X)$ is separable if and only if $X$ is a compact metric space.*

**Proof.** Suppose $X$ is a compact metric space with metric $d$. For each $n$, let $\{U_k^{(n)}:1\leqslant k\leqslant N_n\}$ be an open cover of $X$ by balls of radius $1/n$. Let $\{f_k^{(n)}:1\leqslant k\leqslant N_n\}$ be a partition of unity subordinate to $\{U_k^{(n)}:1\leqslant k\leqslant N_n\}$. Let $\mathscr{Y}$ be the rational (or complex-rational) linear span of $\{f_k^{(n)}:n\geqslant 1,\ 1\leqslant k\leqslant N_n\}$; thus $\mathscr{Y}$ is countable. It will be shown that $\mathscr{Y}$ is dense in $C(X)$.

Fix $f$ in $C(X)$ and $\varepsilon>0$. Since $f$ is uniformly continuous there is a $\delta>0$ such that $|f(x_1)-f(x_2)|<\varepsilon/2$ whenever $d(x_1,x_2)<\delta$. Choose $n>2/\delta$ and consider the cover $\{U_k^{(n)}:1\leqslant k\leqslant N_n\}$. If $x_1,x_2\in U_k^{(n)}$, $d(x_1,x_2)<2/n<\delta$; hence $|f(x_1)-f(x_2)|<\varepsilon/2$. Pick $x_k$ in $U_k^{(n)}$ and let $\alpha_k\in\mathbb{Q}+i\mathbb{Q}$ such that $|\alpha_k-f(x_k)|<\varepsilon/2$. Let $g=\sum_k\alpha_k f_k^{(n)}$, so $g\in\mathscr{Y}$. Therefore for every $x$ in $X$,

$$
\begin{aligned}
|f(x)-g(x)|
&=\left|\sum_k f(x)f_k^{(n)}(x)-\sum_k\alpha_k f_k^{(n)}(x)\right|\\
&\leqslant\sum_k|f(x)-\alpha_k|f_k^{(n)}(x).
\end{aligned}
$$

Examine each of these summands. If $x\in U_k^{(n)}$, then $|f(x)-\alpha_k|\leqslant|f(x)-f(x_k)|+|f(x_k)-\alpha_k|<\varepsilon$. If $x\notin U_k^{(n)}$, then $f_k^{(n)}(x)=0$. Hence $|f(x)-g(x)|<\sum_k\varepsilon f_k^{(n)}(x)=\varepsilon$. Thus $\|f-g\|<\varepsilon$ and $\mathscr{Y}$ is dense in $C(X)$. This shows that $C(X)$ is separable.

Now assume that $C_b(X)$ is separable. Thus $(\operatorname{ball}C_b(X)^*,\mathrm{wk}^*)$ is metrizable (5.1). Since $X$ is homeomorphic to a subset of $\operatorname{ball}C_b(X)^*$ (6.1), $X$ is metrizable. It also follows that $\beta X$ is metrizable. It must be shown that $X=\beta X$.

Suppose there is a $\tau$ in $\beta X\setminus X$. Let $\{x_n\}$ be a sequence in $X$ such that $x_n\to\tau$. It can be assumed that $x_n\ne x_m$ for $n\ne m$. Let $A=\{x_n:n\text{ is even}\}$ and $B=\{x_n:n\text{ is odd}\}$. Then $A$ and $B$ are disjoint closed subsets of $X$ (not closed in $\beta X$, but in $X$) since $A$ and $B$ contain all of their limit points in $X$. Since $X$ is normal, there is a continuous function $f:X\to[0,1]$ such that $f=0$ on $A$ and $f=1$ on $B$. But then $f^\beta(\tau)=\lim f(x_{2n})=0$ and $f^\beta(\tau)=\lim f(x_{2n+1})=1$, a contradiction. Thus $\beta X\setminus X=\square$. $\blacksquare$
