**C.3. Definition.** If $\mu$ is a measure on $(X,\Omega)$ and $\Delta\in\Omega$, define the *variation* of $\mu$, $|\mu|$, by

$$
|\mu|(\Delta)=\sup\left\{\sum_{j=1}^{m}|\mu(E_j)|:\{E_j\}_{1}^{m}\text{ is a measurable partition of }\Delta\right\}.
$$

**C.4. Proposition.** *If $\mu$ is a measure on $(X,\Omega)$, then $|\mu|$ is a positive finite measure on $(X,\Omega)$. If $\mu$ is a signed measure, $|\mu|$ is a positive measure. If (C.2) is satisfied, then $|\mu|(\Delta)\leq\sum_{k=1}^{4}\mu_k(\Delta)$; if $\mu$ is a signed measure, then $|\mu|=\mu_1+\mu_2$.*

**Proof.** Clearly $|\mu|(\Delta)\geq 0$. Let $\{\Delta_n\}$ be pairwise disjoint measurable sets and let $\Delta=\bigcup_{n=1}^{\infty}\Delta_n$. If $\varepsilon>0$, then there is a measurable partition $\{E_j\}_{j=1}^{m}$ of $\Delta$ such that $|\mu|(\Delta)-\varepsilon<\sum_{j=1}^{m}|\mu(E_j)|$. Hence

$$
\begin{aligned}
|\mu|(\Delta)-\varepsilon
&\leq \sum_{j=1}^{m}\left|\sum_{n=1}^{\infty}\mu(E_j\cap\Delta_n)\right|\\
&\leq \sum_{n=1}^{\infty}\sum_{j=1}^{m}|\mu(E_j\cap\Delta_n)|.
\end{aligned}
$$

But $\{E_j\cap\Delta_n\}_{j=1}^{m}$ is a partition of $\Delta_n$, so $|\mu|(\Delta)-\varepsilon\leq\sum_{n=1}^{\infty}|\mu|(\Delta_n)$. Therefore $|\mu|(\Delta)\leq\sum_{n=1}^{\infty}|\mu|(\Delta_n)$. For the reverse inequality we may assume that $|\mu|(\Delta)<\infty$. It follows that $|\mu|(\Delta_n)<\infty$ for every $n$. (Why?) Let $\varepsilon>0$ and for each $n\geq 1$ let $\{E_1^{(n)},\ldots,E_{m_n}^{(n)}\}$ be a partition of $\Delta_n$ such that $\sum_j|\mu(E_j^{(n)})|>|\mu|(\Delta_n)-\varepsilon/2^n$. Then

$$
\begin{aligned}
\sum_{n=1}^{N}|\mu|(\Delta_n)
&<\sum_{n=1}^{N}\left[\frac{\varepsilon}{2^n}+\sum_j|\mu(E_j^{(n)})|\right]\\
&\leq\varepsilon+\sum_{n=1}^{N}\sum_j|\mu(E_j^{(n)})|\\
&\leq\varepsilon+|\mu|(\Delta).
\end{aligned}
$$

Letting $N\to\infty$ and $\varepsilon\to 0$ gives that $\sum_{1}^{\infty}|\mu|(\Delta_n)\leq|\mu|(\Delta)$.

Clearly $|\mu(\Delta)|\leq\sum_{k=1}^{4}\mu_k(\Delta)$, so $|\mu|\leq\sum_{k=1}^{4}\mu_k$. It is left to the reader to show that $|\mu|=\mu_1+\mu_2$ if $\mu$ is a signed measure. Since $\mu_1,\mu_2,\mu_3,\mu_4$ are all finite, $|\mu|$ is finite if $\mu$ is complex-valued. $\blacksquare$

**C.5. Definition.** If $\mu$ is a measure on $(X,\Omega)$ and $\nu$ is a positive measure on $(X,\Omega)$, say that $\mu$ is *absolutely continuous* with respect to $\nu$ ($\mu\ll\nu$) if $\mu(\Delta)=0$ whenever $\nu(\Delta)=0$. If $\nu$ is complex-valued, $\mu\ll\nu$ means $\mu\ll|\nu|$.

**C.6. Proposition.** *Let $\mu$ be a measure and $\nu$ a positive measure on $(X,\Omega)$. The following statements are equivalent.*

(a) $\mu\ll\nu$.

(b) $|\mu|\ll\nu$.

(c) If (C.2) holds, $\mu_k\ll\nu$ for $1\leq k\leq 4$.
