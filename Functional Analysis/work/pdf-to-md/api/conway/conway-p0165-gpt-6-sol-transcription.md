where $m_a(x)=0$ if $\|x-a\|\geq\varepsilon$ and $m_a(x)=\varepsilon-\|x-a\|$ if $\|x-a\|\leq\varepsilon$. Then $\phi_A$ is a continuous function and

$$
\|\phi_A(x)-x\|<\varepsilon
$$

for all $x$ in $K$.

**Proof.** Note that for each $a$ in $A$, $m_a(x)\geq 0$ and $\sum\{m_a(x):a\in A\}>0$ for all $x$ in $K$. So $\phi_A$ is well defined on $K$. The fact that $\phi_A$ is continuous follows from the fact that for each $a$ in $A$, $m_a:K\to[0,\varepsilon]$ is continuous. (Verify!)

If $x\in K$, then

$$
\phi_A(x)-x=
\frac{\sum\{m_a(x)[a-x]:a\in A\}}
{\sum\{m_a(x):a\in A\}}.
$$

If $m_a(x)>0$, then $\|x-a\|<\varepsilon$. Hence

$$
\|\phi_A(x)-x\|
\leq
\frac{\sum\{m_a(x)\|a-x\|:a\in A\}}
{\sum\{m_a(x):a\in A\}}
<\varepsilon.
$$

This concludes the proof. $\blacksquare$

**9.5. The Schauder Fixed Point Theorem.** Let $E$ be a closed bounded convex subset of a normed space $\mathscr{X}$. If $f:E\to\mathscr{X}$ is a compact map such that $f(E)\subseteq E$, then there is an $x$ in $E$ such that $f(x)=x$.

**Proof.** Let $K=\operatorname{cl}f(E)$, so $K\subseteq E$. For each positive integer $n$ let $A_n$ be a finite subset of $K$ such that $K\subseteq\bigcup\{B(a;1/n):a\in A_n\}$. For each $n$ let $\phi_n=\phi_{A_n}$ as in the preceding lemma. Now the definition of $\phi_n$ clearly implies that $\phi_n(K)\subseteq\operatorname{co}(K)\subseteq E$ since $E$ is convex; thus $f_n\equiv\phi_n\circ f$ maps $E$ into $E$. Also, Lemma 9.4 implies

$$
\|f_n(x)-f(x)\|<1/n\qquad\text{for }x\text{ in }E. \tag{9.6}
$$

Let $\mathscr{X}_n$ be the linear span of the set $A_n$ and put $E_n=E\cap\mathscr{X}_n$. So $\mathscr{X}_n$ is a finite dimensional normed space, $E_n$ is a compact convex subset of $\mathscr{X}_n$, and $f_n:E_n\to E_n$ (Why?) is continuous. By Corollary 9.2, there is a point $x_n$ in $E_n$ such that $f_n(x_n)=x_n$.

Now $\{f(x_n)\}$ is a sequence in the compact set $K$, so there is a point $x_0$ and a subsequence $\{f(x_{n_j})\}$ such that $f(x_{n_j})\to x_0$. Since $f_{n_j}(x_{n_j})=x_{n_j}$, (9.6) implies

$$
\begin{aligned}
\|x_{n_j}-x_0\|
&\leq \|f_{n_j}(x_{n_j})-f(x_{n_j})\|
   +\|f(x_{n_j})-x_0\|\\
&\leq \frac{1}{n_j}+\|f(x_{n_j})-x_0\|.
\end{aligned}
$$

Thus $x_{n_j}\to x_0$. Since $f$ is continuous, $f(x_0)=\lim f(x_{n_j})=x_0$. $\blacksquare$

There is a generalization of Schauder’s Theorem where $\mathscr{X}$ is only assumed to be a LCS. See Dunford and Schwartz [1958], p. 456.
