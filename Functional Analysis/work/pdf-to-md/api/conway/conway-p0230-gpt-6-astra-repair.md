§7. The Spectral Theory of a Compact Operator　　　　　　　　　　　　　　　　　215

The proof of the next lemma is like that of Corollary II.4.15.

**7.3. Lemma.** *If $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\ne0$, and $\lambda\in\sigma(A)$, then either $\lambda\in\sigma_p(A)$ or $\lambda\in\sigma_p(A^*)$.*

**7.4. Lemma.** *If $\mathcal{M}\leqslant\mathcal{N}$, $\mathcal{M}\ne\mathcal{N}$, and $\varepsilon>0$, then there is a $y$ in $\mathcal{N}$ such that $\|y\|=1$ and $\operatorname{dist}(y,\mathcal{M})\geqslant1-\varepsilon$.*

**Proof.** Let $\delta(y)=\operatorname{dist}(y,\mathcal{M})$ for every $y$ in $\mathcal{N}$. Now if $y_1\in\mathcal{N}\setminus\mathcal{M}$, there is an $x_0$ in $\mathcal{M}$ such that $\delta(y_1)\leqslant\|x_0-y_1\|\leqslant(1+\varepsilon)\delta(y_1)$. Let $y_2=y_1-x_0$. Then $(1+\varepsilon)\delta(y_2)=(1+\varepsilon)\inf\{\|y_2-x\|:x\in\mathcal{M}\}=(1+\varepsilon)\inf\{\|y_1-x_0-x\|:x\in\mathcal{M}\}=(1+\varepsilon)\delta(y_1)$ since $x_0\in\mathcal{M}$. Thus $(1+\varepsilon)\delta(y_2)>\|x_0-y_1\|=\|y_2\|$. Let $y=\|y_2\|^{-1}y_2$. So $\|y\|=1$, $y\in\mathcal{N}$, and if $x\in\mathcal{M}$, then
$$
\begin{aligned}
\|y-x\|&=\bigl\|\|y_2\|^{-1}y_2-x\bigr\|\\
&=\|y_2\|^{-1}\bigl\|y_2-\|y_2\|x\bigr\|>[(1+\varepsilon)\delta(y_2)]^{-1}\bigl\|y_2-\|y_2\|x\bigr\|\\
&\geqslant(1+\varepsilon)^{-1}>1-\varepsilon.
\end{aligned}
$$
$\blacksquare$

If $\mathcal{M}$ and $\mathcal{N}$ are finite dimensional in the preceding lemma, then $y$ can be chosen in $\mathcal{N}$ such that $\|y\|=1$ and $\operatorname{dist}(y,\mathcal{M})=1$ (see Exercise 1).

**7.5. Lemma.** *If $A\in\mathcal{B}_0(\mathcal{X})$ and $\{\lambda_n\}$ is a sequence of distinct elements in $\sigma_p(A)$, then $\lim\lambda_n=0$.*

**Proof.** For each $n$ let $x_n\in\ker(A-\lambda_n)$ such that $x_n\ne0$. It follows that if $\mathcal{M}_n=\bigvee\{x_1,\ldots,x_n\}$, then $\dim\mathcal{M}_n=n$ (Exercise). Hence $\mathcal{M}_n\leqslant\mathcal{M}_{n+1}$ and $\mathcal{M}_n\ne\mathcal{M}_{n+1}$. By the preceding lemma there is a vector $y_n$ in $\mathcal{M}_n$ such that $\|y_n\|=1$ and $\operatorname{dist}(y_n,\mathcal{M}_{n-1})>\frac12$. Let $y_n=\alpha_1x_1+\cdots+\alpha_nx_n$. Hence
$$
(A-\lambda_n)y_n=\alpha_1(\lambda_1-\lambda_n)x_1+\cdots+\alpha_{n-1}(\lambda_{n-1}-\lambda_n)x_{n-1}\in\mathcal{M}_{n-1}.
$$
So if $n>m$,
$$
\begin{aligned}
A(\lambda_n^{-1}y_n)-A(\lambda_m^{-1}y_m)
&=\lambda_n^{-1}(A-\lambda_n)y_n-\lambda_m^{-1}(A-\lambda_m)y_m+y_n-y_m\\
&=y_n-[y_m+\lambda_m^{-1}(A-\lambda_m)y_m-\lambda_n^{-1}(A-\lambda_n)y_n].
\end{aligned}
$$
But the bracketed expression belongs to $\mathcal{M}_{n-1}$. Hence $\|A(\lambda_n^{-1}y_n)-A(\lambda_m^{-1}y_m)\|\geqslant\operatorname{dist}(y_n,\mathcal{M}_{n-1})>\frac12$. Therefore $A(\lambda_n^{-1}y_n)$ can have no convergent subsequence. But $A$ is a compact operator so that if $S$ is any bounded subset of $\mathcal{X}$, $\operatorname{cl}A(S)$ is compact. Thus it must be that $\{\lambda_n^{-1}y_n\}$ has no bounded subsequence. Since $\|y_n\|=1$ for all $n$, it must be that $\|\lambda_n^{-1}y_n\|=|\lambda_n|^{-1}\to\infty$. That is, $0=\lim\lambda_n$. $\blacksquare$

**Proof of Theorem 7.1.** The first step is to establish the following.

**7.6. Claim.** If $\lambda\in\sigma(A)$ and $\lambda\ne0$, then $\lambda$ is an isolated point of $\sigma(A)$.

In fact, if $\{\lambda_n\}\subseteq\sigma(A)$ and $\lambda_n\to\lambda$, then each $\lambda_n$ belongs to either $\sigma_p(A)$ or $\sigma_p(A^*)$ (7.3). So either there is a subsequence $\{\lambda_{n_k}\}$ that is contained in $\sigma_p(A)$
