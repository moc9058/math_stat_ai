Because $f'$ is continuous with compact support, $f'$ is uniformly continuous. Let $K=\{x:\operatorname{dist}(x,\operatorname{spt}f')\leq 2\}$. So $K$ is compact. For $\varepsilon>0$, let $\delta(\varepsilon)<1$ be such that if $|x-y|<\delta(\varepsilon)$, then $|f'(x)-f'(y)|<\varepsilon$. Hence $\|t^{-1}[Vf-f]+f'\|_2\leq\varepsilon^2|K|$, where $|K|=$ the Lebesgue measure of $K$. Thus $C_c^{(1)}(\mathbb R)\subseteq\operatorname{dom}B$ and $Bf=Af$ for $f$ in $C_c^{(1)}(\mathbb R)$. But if $f\in\operatorname{dom}A$, there is a sequence $\{f_n\}\subseteq C_c^{(1)}(\mathbb R)$ such that $f_n\oplus Af_n\to f\oplus Af$ in $\operatorname{gra}A$ (Exercise 1). But $f_n\oplus Af_n=f_n\oplus Bf_n\in\operatorname{gra}B$, so $f\oplus Af\in\operatorname{gra}B$; that is, $A\subseteq B$. Since self-adjoint operators are maximal symmetric operators (2.11), $A=B$. ■

To show that the Fourier transform demonstrates that $M_x$ and $id/dx$ are unitarily equivalent, we introduce the Schwartz space of rapidly decreasing functions.

**6.3. Definition.** A function $\phi:\mathbb R\to\mathbb R$ is *rapidly decreasing* if $\phi$ is infinitely differentiable and for all integers $m,n\geq 0$,

$$
\tag{6.4}
\|\phi\|_{m,n}\equiv\sup\{|x^m\phi^{(n)}(x)|:x\in\mathbb R\}<\infty.
$$

Let $\mathcal S=\mathcal S(\mathbb R)$ be the set of all rapidly decreasing functions on $\mathbb R$.

Note that if $\phi\in\mathcal S$, then for all $m,n\geq 0$ there is a constant $C_{m,n}$ such that

$$
|\phi^{(n)}(x)|\leq C_{m,n}|x|^{-m}.
$$

Thus if $p$ is any polynomial and $n\geq 0$, $|p(x)\phi^{(n)}(x)|\to 0$ as $|x|\to\infty$. In fact, this is equivalent to $\phi$ belonging to $\mathcal S$ (Exercise 3). Also note that if $\phi\in\mathcal S$, then $x^m\phi^{(n)}\in\mathcal S$ for all $m,n\geq 0$.

It is not difficult to see that $\|\cdot\|_{m,n}$ is a seminorm on $\mathcal S$. Also, $\mathcal S$ with all of these seminorms is a Fréchet space (Exercise 2). The space $\mathcal S$ is sometimes called the *Schwartz space* after Laurent Schwartz.

**6.5. Proposition.** *If $1\leq p\leq\infty$, $\mathcal S\subseteq L^p(\mathbb R)$. If $1\leq p<\infty$, $\mathcal S$ is dense in $L^p(\mathbb R)$; $\mathcal S$ is weak-star dense in $L^\infty(\mathbb R)$.*

**Proof.** We already have that $\mathcal S\subseteq L^\infty(\mathbb R)$. If $1\leq p<\infty$ and $\phi\in\mathcal S$, then

$$
\begin{aligned}
\int_{-\infty}^{\infty}|\phi|^p\,dx
&=\int_{-\infty}^{\infty}(1+x^2)^{-p}(1+x^2)^p|\phi|^p\,dx\\
&\leq\|(1+x^2)^p|\phi|^p\|_\infty
\int_{-\infty}^{\infty}(1+x^2)^{-p}\,dx.
\end{aligned}
$$

Since $(1+x^2)^p\geq 1+x^2$,

$$
\begin{aligned}
\|\phi\|_p
&\leq\pi^{1/p}\|(1+x^2)\phi\|_\infty\\
&\leq\pi^{1/p}\bigl[\|\phi\|_{0,0}+\|\phi\|_{2,0}\bigr].
\end{aligned}
$$

Since $C_c^{(\infty)}(\mathbb R)\subseteq\mathcal S$, the density statements are immediate. ■

**6.6. Definition.** If $f\in L^1(\mathbb R)$, the *Fourier transform* of $f$ is the function $\hat f$ defined
