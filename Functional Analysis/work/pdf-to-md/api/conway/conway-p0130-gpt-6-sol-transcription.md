$g$ analytic on $\mathbb C_\infty\setminus\overline B(0;r)$ with $g(\infty)=0$ such that

$$
\tag{4.3}
L(f)=\frac{1}{2\pi i}\int_\gamma fg
$$

for every $f$ in $H(\mathbb D)$, where $\gamma(t)=\rho e^{it}$, $0\leq t\leq2\pi$, and $r<\rho<1$.

**Proof.** Let $g$ be given and define $L$ as in (4.3). If $K=\{z:|z|=\rho\}$, then

$$
\begin{aligned}
|L(f)|
&=\frac{1}{2\pi}\left|\int_0^{2\pi}f(\rho e^{it})g(\rho e^{it})i\rho e^{it}\,dt\right|\\
&\leq\frac{1}{2\pi}p_K(f)p_K(g)2\pi\rho.
\end{aligned}
$$

So if $c=\rho p_K(g)$, $|L(f)|\leq cp_K(f)$, and $L\in H(\mathbb D)^*$.

Now assume that $L\in H(\mathbb D)^*$. The Hahn–Banach Theorem implies there is an $F$ in $C(\mathbb D)^*$ such that $F|H(\mathbb D)=L$. By Proposition 4.1 there is a compact set $K$ contained in $\mathbb D$ and a measure $\mu$ on $K$ such that $L(f)=\int_K f\,d\mu$ for every $f$ in $H(\mathbb D)$. Define $g:\mathbb C_\infty\setminus K\to\mathbb C$ by $g(\infty)=0$ and $g(z)=-\int_K 1/(w-z)\,d\mu(w)$ for $z$ in $\mathbb C\setminus K$. By Lemma III.8.2, $g$ is analytic on $\mathbb C_\infty\setminus K$. Let $\rho<1$ such that $K\subseteq B(0;\rho)$. If $\gamma(t)=\rho e^{it}$, $0\leq t\leq2\pi$, then Cauchy’s Integral Formula implies

$$
f(w)=\frac{1}{2\pi i}\int_\gamma\frac{f(z)}{z-w}\,dz
$$

for $|w|<\rho$; in particular, this is true for $w$ in $K$. Thus,

$$
\begin{aligned}
L(f)
&=\int_K f(w)\,d\mu(w)\\
&=\int_K\left[\frac{\rho}{2\pi}\int_0^{2\pi}
\frac{f(\rho e^{it})}{\rho e^{it}-w}e^{it}\,dt\right]d\mu(w)\\
&=\frac{\rho}{2\pi}\int_0^{2\pi}f(\rho e^{it})e^{it}
\left[\int_K\frac{1}{\rho e^{it}-w}\,d\mu(w)\right]dt\\
&=\frac{1}{2\pi i}\int_\gamma f(z)g(z)\,dz.
\end{aligned}
$$

This completes the proof except for the uniqueness of $g$ (Exercise 3). $\blacksquare$

## Exercises

1. Let $\{\mathcal X_i:i\in I\}$ be a family of LCS’s and give $\mathcal X=\prod\{\mathcal X_i:i\in I\}$ the product topology. (See Exercise 1.17.) Show that $L\in\mathcal X^*$ if and only if there is a finite subset $F$ contained in $I$ and there are $x_j^*$ in $\mathcal X_j^*$ for $j$ in $F$ such that $L(x)=\sum_{j\in F}x_j^*(x(j))$ for each $x$ in $\mathcal X$.

2. Show that the space $s$ (Exercise 1.13) is linearly homeomorphic to $C(\mathbb N)$ and describe $s^*$.
