(c) A subset $W$ of $\mathcal{X}/\mathcal{M}$ is open relative to the norm if and only if $Q^{-1}(W)$ is open in $\mathcal{X}$.

(d) If $U$ is open in $\mathcal{X}$, then $Q(U)$ is open in $\mathcal{X}/\mathcal{M}$.

**Proof.** It is left as an exercise to show that (4.1) defines a norm on $\mathcal{X}/\mathcal{M}$. To show (a), $\|Q(x)\|=\|x+\mathcal{M}\|\leq\|x\|$ since $0\in\mathcal{M}$; $Q$ is therefore continuous by (2.1).

(b) Let $\{x_n+\mathcal{M}\}$ be a Cauchy sequence in $\mathcal{X}/\mathcal{M}$. There is a subsequence $\{x_{n_k}+\mathcal{M}\}$ such that

$$
\|(x_{n_k}+\mathcal{M})-(x_{n_{k+1}}+\mathcal{M})\|
=\|x_{n_k}-x_{n_{k+1}}+\mathcal{M}\|<2^{-k}.
$$

Let $y_1=0$. Choose $y_2$ in $\mathcal{M}$ such that

$$
\|x_{n_1}-x_{n_2}+y_2\|
\leq\|x_{n_1}-x_{n_2}+\mathcal{M}\|+2^{-1}
<2\cdot2^{-1}.
$$

Choose $y_3$ in $\mathcal{M}$ such that

$$
\|(x_{n_2}+y_2)-(x_{n_3}+y_3)\|
\leq\|x_{n_2}-x_{n_3}+\mathcal{M}\|+2^{-2}
<2\cdot2^{-2}.
$$

Continuing, there is a sequence $\{y_k\}$ in $\mathcal{M}$ such that

$$
\|(x_{n_k}+y_k)-(x_{n_{k+1}}+y_{k+1})\|<2\cdot2^{-k}.
$$

Thus $\{x_{n_k}+y_k\}$ is a Cauchy sequence in $\mathcal{X}$ (Why?). Since $\mathcal{X}$ is complete, there is an $x_0$ in $\mathcal{X}$ such that $x_{n_k}+y_k\to x_0$ in $\mathcal{X}$. By (a), $x_{n_k}+\mathcal{M}=Q(x_{n_k}+y_k)\to Qx_0=x_0+\mathcal{M}$. Since $\{x_n+\mathcal{M}\}$ is a Cauchy sequence, $x_n+\mathcal{M}\to x_0+\mathcal{M}$ and $\mathcal{X}/\mathcal{M}$ is complete (Exercise 3).

(c) If $W$ is open in $\mathcal{X}/\mathcal{M}$, then $Q^{-1}(W)$ is open in $\mathcal{X}$ because $Q$ is continuous. Now assume that $W\subseteq\mathcal{X}/\mathcal{M}$ and $Q^{-1}(W)$ is open in $\mathcal{X}$. Let $r>0$ and put $B_r=\{x\in\mathcal{X}:\|x\|<r\}$. It will be shown that $Q(B_r)=\{x+\mathcal{M}:\|x+\mathcal{M}\|<r\}$. In fact, if $\|x\|<r$, then $\|x+\mathcal{M}\|\leq\|x\|<r$. On the other hand, if $\|x+\mathcal{M}\|<r$, then there is a $y$ in $\mathcal{M}$ such that $\|x+y\|<r$. Thus $x+\mathcal{M}=Q(x+y)\in Q(B_r)$. If $x_0+\mathcal{M}\in W$, then $x_0\in Q^{-1}(W)$. Since $Q^{-1}(W)$ is open, there is an $r>0$ such that $x_0+B_r=\{x:\|x-x_0\|<r\}\subseteq Q^{-1}(W)$. The preceding argument now implies that $W=QQ^{-1}(W)\supseteq Q(x_0+B_r)=\{x+\mathcal{M}:\|x-x_0+\mathcal{M}\|<r\}$. Hence $W$ is open.

(d) If $U$ is open in $\mathcal{X}$, then $Q^{-1}(Q(U))=U+\mathcal{M}\equiv\{u+y:u\in U,\ y\in\mathcal{M}\}=\bigcup\{U+y:y\in\mathcal{M}\}$. Each $U+y$ is open, so $Q^{-1}(Q(U))$ is open in $\mathcal{X}$. By (c), $Q(U)$ is open in $\mathcal{X}/\mathcal{M}$. $\blacksquare$

Because $Q$ is an open map [part (d)], it does not follow that $Q$ is a closed map (Exercise 4).

**4.3. Proposition.** *If $\mathcal{X}$ is a normed space, $\mathcal{M}\leq\mathcal{X}$, and $\mathcal{N}$ is a finite dimensional subspace of $\mathcal{X}$, then $\mathcal{M}+\mathcal{N}$ is a closed subspace of $\mathcal{X}$.*

**Proof.** Consider $\mathcal{X}/\mathcal{M}$ and the quotient map $Q:\mathcal{X}\to\mathcal{X}/\mathcal{M}$. Since $\dim Q(\mathcal{N})\leq\dim\mathcal{N}<\infty$, $Q(\mathcal{N})$ is closed in $\mathcal{X}/\mathcal{M}$. Since $Q$ is continuous $Q^{-1}(Q(\mathcal{N}))$ is closed in $\mathcal{X}$; but $Q^{-1}(Q(\mathcal{N}))=\mathcal{M}+\mathcal{N}$. $\blacksquare$
