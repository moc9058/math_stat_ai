**6.11. Definition.** If $A\in\mathcal{B}(\mathcal{H})$, then the *Weyl spectrum* of $A$, $\sigma_w(A)$, is defined by

$$
\sigma_w(A)=\bigcap\{\sigma(A+K):K\in\mathcal{B}_0\}.
$$

Note that since $\sigma_e(A+K)=\sigma_e(A)$ for every compact operator, $\sigma_w(A)$ is nonempty and $\sigma_e(A)\subseteq\sigma_w(A)$. The way to think of the Weyl spectrum is that it is the largest part of the spectrum of $A$ that remains unchanged under compact perturbations. It is clear that $\sigma_w(A)=\sigma_w(A+K)$ for every $K$ in $\mathcal{B}_0$ and $\sigma_w(A)\subseteq\sigma(A)$. The following is a result of Schechter [1965].

**6.12. Theorem.** *If $A\in\mathcal{B}(\mathcal{H})$, then $\sigma_w(A)=\sigma_e(A)\cup\bigcup_{n\ne0}P_n(A)$.*

**PROOF.** Clearly $X\equiv\sigma_e(A)\cup\bigcup_{n\ne0}P_n(A)\subseteq\sigma_w(A)$. Now suppose $\lambda\notin X$. Then $A-\lambda\in\mathcal{F}$ and $\operatorname{ind}(A-\lambda)=0$. By Exercise 3.7 there is a finite rank operator $F$ such that $A+F-\lambda$ is invertible. Hence $\lambda\notin\sigma(A+F)$ so that $\lambda\notin\sigma_w(A)$. ■

So for every operator $A$ in $\mathcal{B}(\mathcal{H})$ there is a *spectral picture* for $A$ (a term coined in Pearcy [1978]). There are the open sets $\{P_n(A):0<|n|\leq\infty\}$, the set $P_0(A)=G_0\cup D$ where $D$ consists of isolated points $\lambda$ for which $\dim E(\lambda)=n_\lambda<\infty$, and there is the remainder of $\sigma(A)$, which is the set $\sigma_{le}(A)\cap\sigma_{re}(A)$. The next result is due to Conway [1985].

**6.13. Proposition.** *Let $K$ be a compact subset of $\mathbb{C}$, let $\{G_n:-\infty\leq n\leq\infty\}$ be disjoint open subsets of $K$ (some possibly empty), let $D$ be a subset of the set of isolated points of $K$, and for each $\lambda$ in $D$ let $n_\lambda\in\{1,2,\ldots\}$. Then there is an operator $A$ on $\mathcal{H}$ such that $\sigma(A)=K$, $P_n(A)=G_n$ for $0<|n|\leq\infty$, $P_0(A)=G_0\cup D$, and $\dim E(\lambda)=n_\lambda$ for every $\lambda$ in $D$.*

We prove only a special case of this result; the general case is left to the reader. Let $K$ be any compact subset of $\mathbb{C}$ and let $G$ be an open subset of $K$. Put $H=\operatorname{int}[\operatorname{cl}G]$; so $G\subseteq H$, but it may be that $H\ne G$. However, $\partial H=\partial[\operatorname{cl}H]$. Let $Tf=zf$ for $f$ in $L_a^2(H)$, so $H=P_{-1}(T)$, $\sigma(T)=\operatorname{cl}H$, and $\sigma_{le}(T)\cap\sigma_{re}(T)=\partial H=\partial[\operatorname{cl}G]$. Let $\{\lambda_k\}$ be a countable dense subset of $K\setminus G$ and let $N$ be the diagonalizable normal operator with $\sigma_p(N)=\{\lambda_k\}$ and such that $\dim\ker(N-\lambda_k)=\infty$ for each $\lambda_k$. If $0<n\leq\infty$ and $A=N\oplus T^{(n)}$, then $\sigma(A)=K$, $P_{-n}(A)=G$, and $K\setminus G=\sigma_{le}(A)\cap\sigma_{re}(A)$.

## EXERCISES

1. If $A$ is an invertible operator, show that $\gamma(A)=\|A^{-1}\|^{-1}$.

2. Let $A\in\mathcal{F}$ and suppose that $\ker A\ne(0)$ and $\operatorname{ran}A^\perp\ne(0)$. Show that for every $\delta>0$ there is an operator $B$ in $\mathcal{F}$ such that $\|B-A\|<\delta$, $\dim\ker B<\dim\ker A$, and $\dim\operatorname{ran}B^\perp<\dim\operatorname{ran}A^\perp$.

3. If $A\in\mathcal{SF}$, show that there is a $\delta>0$ such that $\dim\ker(A-\mu)=\dim\ker A$ and $\dim\operatorname{ran}(A-\mu)^\perp=\dim\operatorname{ran}A^\perp$ for $|\mu|<\delta$ if $\ker A\subseteq\operatorname{ran}A^n$ for every $n\geq1$.

4. Prove Proposition 6.9.
