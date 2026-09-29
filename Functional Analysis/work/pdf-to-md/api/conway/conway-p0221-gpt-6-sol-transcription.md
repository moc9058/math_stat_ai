Now $z\in\mathcal B$ and so it has a spectrum as an element of this algebra; denote this spectrum by $\sigma_{\mathcal B}(z)$. There is no reason to believe that $\sigma_{\mathcal B}(z)=\sigma_{\mathcal A}(z)$. In fact, they are not equal.

**5.1. Example.** If $\mathcal B=$ the closure in $C(\partial\mathbb D)$ of the polynomials in $z$, then $\sigma_{\mathcal B}(z)=\operatorname{cl}\mathbb D$.

To see this first note that $\|z\|=1$, so that $\sigma_{\mathcal B}(z)\subseteq\operatorname{cl}\mathbb D$ by Theorem 3.6. If $|\lambda|\leqslant1$ and $\lambda\notin\sigma_{\mathcal B}(z)$, there is an $f$ in $\mathcal B$ such that $(z-\lambda)f=1$. Note that this implies that $|\lambda|<1$. Because $f\in\mathcal B$, there is a sequence of polynomials $\{p_n\}$ such that $p_n\to f$ uniformly on $\partial\mathbb D$. Thus for every $\varepsilon>0$ there is an $N$ such that for $m,n\geqslant N$,
$\varepsilon>\|p_n-p_m\|_{\partial\mathbb D}\equiv\sup\{|p_n(z)-p_n(z)|:z\in\partial\mathbb D\}$. By the Maximum Principle, $\varepsilon>\|p_n-p_m\|_{\operatorname{cl}\mathbb D}$ for $m,n\geqslant N$. Thus $g(z)=\lim p_n(z)$ is analytic on $\mathbb D$ and continuous on $\operatorname{cl}\mathbb D$; also, $g|_{\partial\mathbb D}=f$. By the same argument, since $p_n(z)(z-\lambda)\to1$ uniformly on $\partial\mathbb D$, $p_n(z)(z-\lambda)\to1$ uniformly on $\mathbb D$. Thus $g(z)(z-\lambda)=1$ on $\mathbb D$. But $1=g(\lambda)(\lambda-\lambda)=0$, a contradiction. Thus, $\operatorname{cl}\mathbb D\subseteq\sigma_{\mathcal B}(z)$.

Thus the spectrum not only depends on the element of the algebra, but also on the algebra. Precisely how this dependence occurs is given below, but it can be said that the example above is typical, both in its statement and its proof, of the general situation. To phrase these results it is necessary to introduce the polynomially convex hull of a compact subset of $\mathbb C$.

**5.2. Definition.** If $A$ is a set and $f:A\to\mathbb C$, define

$$
\|f\|_A\equiv\sup\{|f(z)|:z\in A\}.
$$

If $K$ is a compact subset of $\mathbb C$, define the *polynomially convex hull* of $K$ to be the set $\widehat K$ given by

$$
\widehat K\equiv\{z\in\mathbb C:|p(z)|\leqslant\|p\|_K\text{ for every polynomial }p\}.
$$

The set $K$ is *polynomially convex* if $K=\widehat K$.

Note that the polynomially convex hull of $\partial\mathbb D$ is $\operatorname{cl}\mathbb D$. This is, again, quite typical. If $K$ is any compact set, then $\mathbb C\setminus K$ has a countable number of components, only one of which is unbounded. The bounded components are sometimes called the *holes* of $K$; a few pictures should convince the reader of the appropriateness of this terminology.

**5.3. Proposition.** *If $K$ is a compact subset of $\mathbb C$, then $\mathbb C\setminus\widehat K$ is the unbounded component of $\mathbb C\setminus K$. Hence $K$ is polynomially convex if and only if $\mathbb C\setminus K$ is connected.*

**Proof.** Let $U_0,U_1,\ldots$ be the components of $\mathbb C\setminus K$, where $U_0$ is unbounded. Put $L=\mathbb C\setminus U_0$; hence $L=K\cup\bigcup_{n=1}^{\infty}U_n$. Clearly $K\subseteq\widehat K$. If $n\geqslant1$, then $U_n$ is a bounded open set and a topological argument implies $\partial U_n\subseteq K$. By the Maximum Principle $U_n\subseteq\widehat K$. Thus, $L\subseteq\widehat K$.
