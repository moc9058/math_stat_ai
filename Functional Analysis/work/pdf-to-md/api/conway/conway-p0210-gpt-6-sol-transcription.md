8. If $\mathcal A$ is a Banach algebra, a net $\{e_i\}$ in $\mathcal A$ is called an *approximate identity* for $\mathcal A$ if $\sup_i\|e_i\|<\infty$ and for each $a$ in $\mathcal A$, $e_i a\to a$ and $ae_i\to a$. Show that $\mathcal A$ has an approximate identity if and only if there is a bounded subset $E$ of $\mathcal A$ such that for every $\varepsilon>0$ and for every $a$ in $\mathcal A$ there is an $e$ in $E$ with $\|ae-a\|+\|ea-a\|<\varepsilon$. See Wichmann [1973] for more information.

9. Show that if $X$ is locally compact, then $C_0(X)$ has an approximate identity.

10. If $\mathcal H$ is a Hilbert space, show that $\mathcal B_0(\mathcal H)$ has an approximate identity.

11. If $G$ is a locally compact group, show that $L^1(G)$ (1.11) has an approximate identity. [Hint: Let $\mathcal U=$ all neighborhoods $U$ of the identity $e$ of $G$ such that $\operatorname{cl}U$ is compact. Order $\mathcal U$ by reverse inclusion. For $U$ in $\mathcal U$, let $f_U=m(U)^{-1}\chi_U$. Then $\{f_U:U\in\mathcal U\}$ is an approximate identity for $L^1(G)$.]

12. For $0<r<1$, let $P_r:\partial\mathbb D\to[0,\infty)$ defined by $P_r(z)=\sum_{n=-\infty}^{\infty}r^{|n|}z^n$ (the *Poisson kernel*). Show that $\{P_r\}$ is an approximate identity for $L^1(\partial\mathbb D)$ (under convolution).

13. If $\mathcal H$ is a Hilbert space and $P$ is a projection, show that $\mathcal B_0(\mathcal H)P$ is a closed modular left ideal of $\mathcal B_0(\mathcal H)$. What is the associated right modular unit?

14. Find the minimal proper left ideals of $M_n(\mathbb F)$.

15. Find the minimal closed proper left ideals of $\mathcal B_0(\mathcal H)$, $\mathcal H$ a Hilbert space. How about for $\mathcal B_0(\mathcal X)$, $\mathcal X$ a Banach space?

16. What are the maximal modular left ideals of $\mathcal B_0(\mathcal H)$, $\mathcal H$ a Hilbert space?

## §3. The Spectrum

**3.1. Definition.** If $\mathcal A$ is a Banach algebra with identity and $a\in\mathcal A$, the *spectrum* of $a$, denoted by $\sigma(a)$, is defined by

$$
\sigma(a)=\{\alpha\in\mathbb F:a-\alpha\text{ is not invertible}\}.
$$

The *left spectrum*, $\sigma_l(a)$, is the set $\{\alpha\in\mathbb F:a-\alpha\text{ is not left invertible}\}$; the *right spectrum*, $\sigma_r(a)$, is defined similarly.

The *resolvent set* of $a$ is defined by $\rho(a)=\mathbb F\setminus\sigma(a)$. The *left* and *right resolvents* of $a$ are $\rho_l(a)=\mathbb F\setminus\sigma_l(a)$ and $\rho_r(a)=\mathbb F\setminus\sigma_r(a)$.

**3.2. Example.** Let $X$ be compact. If $f\in C(X)$, then $\sigma(f)=f(X)$. In fact, if $\alpha=f(x_0)$, then $f-\alpha$ has a zero and cannot be invertible. So $f(X)\subseteq\sigma(f)$. On the other hand, if $\alpha\notin f(X)$, $f-\alpha$ is a nonvanishing continuous function on $X$. Hence $(f-\alpha)^{-1}\in C(X)$ and so $f-\alpha$ is invertible. Thus $\alpha\notin\sigma(f)$.

**3.3. Example.** If $\mathcal X$ is a Banach space and $A\in\mathcal B(\mathcal X)$, then $\sigma(A)=\{\alpha\in\mathbb F:\text{ either }\ker(A-\alpha)\ne(0)\text{ or }\operatorname{ran}(A-\alpha)\ne\mathcal X\}$. In fact, this means that $\rho(A)=\mathbb F\setminus\sigma(A)=\{\alpha\in\mathbb F:A-\alpha\text{ is bijective}\}$. If $\alpha\in\rho(A)$, there is an operator $T$ in $\mathcal B(\mathcal X)$ such that $T(A-\alpha)=(A-\alpha)T=1$; clearly, $A-\alpha$ is bijective. On the other hand, if $A-\alpha$ is bijective, $(A-\alpha)^{-1}\in\mathcal B(\mathcal X)$ by the Inverse Mapping Theorem.
