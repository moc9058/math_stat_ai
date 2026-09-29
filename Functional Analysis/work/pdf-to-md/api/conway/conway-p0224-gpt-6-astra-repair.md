§6. The Spectrum of a Linear Operator　　　　　　　　　　　　　　　　　209

(c) *There is a constant $c>0$ such that $\|(A-\lambda)x\|\geq c\|x\|$ for all $x$.*

**Proof.** Clearly it may be assumed that $\lambda=0$.

(a)$\Rightarrow$(c): Suppose (c) fails to hold; then for every $n$ there is a non-zero vector $x_n$ with $\|Ax_n\|\leq\|x_n\|/n$. If $y_n=x_n/\|x_n\|$, $\|y_n\|=1$ and $\|Ay_n\|\to0$. Hence $0\in\sigma_{ap}(A)$.

(c)$\Rightarrow$(b): Suppose $\|Ax\|\geq c\|x\|$. Clearly $\ker A=(0)$. If $Ax_n\to y$, $\|x_n-x_m\|\leq c^{-1}\|Ax_n-Ax_m\|$, so $\{x_n\}$ is a Cauchy sequence. Let $x=\lim x_n$; therefore $Ax=y$ and $\operatorname{ran}A$ is closed.

(b)$\Rightarrow$(a): Let $\mathcal Y=\operatorname{ran}A$; so $A:\mathcal X\to\mathcal Y$ is a continuous bijection. By the Inverse Mapping Theorem, there is a bounded operator $B:\mathcal Y\to\mathcal X$ such that $BAx=x$ for all $x$ in $\mathcal X$. Thus if $\|x\|=1$, $1=\|BAx\|\leq\|B\|\|Ax\|$. That is, $\|Ax\|\geq\|B\|^{-1}$ whenever $\|x\|=1$. Hence $0\notin\sigma_{ap}(A)$. ■

It may be that $\sigma_p(A)$ is empty, but it will be shown that $\sigma_{ap}(A)$ is never empty. The first statement follows from the next result (or from other examples that have been presented); the second statement will be proved later.

**6.5. Proposition.** *If $1\leq p\leq\infty$, define $S:l^p\to l^p$ by $S(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots)$. Then $\sigma(S)=\operatorname{cl}\mathbb D$, $\sigma_p(S)=\square$, and $\sigma_{ap}(S)=\partial\mathbb D$. Moreover, for $|\lambda|<1$, $\operatorname{ran}(S-\lambda)$ is closed and $\dim[l^p/\operatorname{ran}(S-\lambda)]=1$.*

**Proof.** Let $S_p$ be the shift on $l^p$. For $1\leq p\leq\infty$, define $T_p:l^p\to l^p$ by $T_p(x_1,x_2,\ldots)=(x_2,x_3,\ldots)$. It is easy to check that for $1\leq p<\infty$ and $1/p+1/q=1$, $S_p^*=T_q$. Since $\|S_p\|=1$, $\sigma(S_p)\subseteq\operatorname{cl}\mathbb D$.

Suppose $x=(x_1,x_2,\ldots)\in l^p$, $\lambda\neq0$. If $S_px=\lambda x$, $0=\lambda x_1$, $x_1=\lambda x_2,\ldots$. Hence $0=x_1=x_2=\cdots$. Since $S_p$ is an isometry, $\ker S_p=(0)$. Thus $\sigma_p(S_p)=\square$.

Let $1\leq p\leq\infty$ and $|\lambda|<1$. Put $x_\lambda=(1,\lambda,\lambda^2,\ldots)$. Then $\|x_\lambda\|_p^p=\sum_{n=0}^{\infty}|\lambda^p|^n<\infty$. Also, $T_px_\lambda=(\lambda,\lambda^2,\ldots)=\lambda x_\lambda$. Hence $\lambda\in\sigma_p(T_p)$ and $x_\lambda\in\ker(T_p-\lambda)$. If $1\leq p<\infty$ and $1/p+1/q=1$, $T_q=S_p^*$; so $\mathbb D\subseteq\sigma(T_q)=\sigma(S_p)$. Also, $S_\infty=T_1^*$, so $\mathbb D\subseteq\sigma(S_\infty)$. Thus for all $p$, $\mathbb D\subseteq\sigma(S_p)\subseteq\operatorname{cl}\mathbb D$. Since $\sigma(S_p)$ is necessarily closed, $\sigma(S_p)=\operatorname{cl}\mathbb D$.

If $|\lambda|\neq1$ and $x\in l^p$, $\|(S_p-\lambda)x\|_p=\|S_px-\lambda x\|_p\geq\bigl|\|S_px\|_p-|\lambda|\|x\|_p\bigr|=\bigl|\|x\|_p-|\lambda|\|x\|_p\bigr|=\bigl|1-|\lambda|\bigr|\|x\|_p$. By (6.4), $\lambda\notin\sigma_{ap}(S_p)$. Hence $\sigma_{ap}(S)\subseteq\partial\mathbb D$. The fact that $\sigma_{ap}(S_p)=\partial\mathbb D$ follows from the next proposition (6.7).

Fix $|\lambda|<1$; we will show that $\dim\ker(T_p-\lambda)=1$ for $1\leq p\leq\infty$. Indeed, if $x\in l^p$ and $T_px=\lambda x$, then $(x_2,x_3,\ldots)=(\lambda x_1,\lambda x_2,\ldots)$. So $x_{n+1}=\lambda x_n$ for all $n$. Thus $x_{n+1}=\lambda^n x_1$ for $n\geq1$. That is, if $x_\lambda=(1,\lambda,\lambda^2,\ldots)$, then $x=x_1x_\lambda$. Since it has already been shown that $x_\lambda\in\ker(T_p-\lambda)$, we have that the dimension of this kernel is 1. Therefore, if $1\leq p<\infty$, $1=\dim\ker(T_q-\lambda)=\dim\ker(S_p^*-\lambda)=\dim[\operatorname{ran}(S_p-\lambda)^\perp]$ (VI.1.8) $=\dim[l^p/\operatorname{ran}(S_p-\lambda)]^*$ (Why?). But this implies that $\dim[l^p/\operatorname{ran}(S_p-\lambda)]=1$, completing the proof for the case where $p$ is finite. The proof for $p=\infty$ is similar and is left to the reader. ■

**6.6. Corollary.** *If $1\leq p\leq\infty$ and $T:l^p\to l^p$ is defined by $T(x_1,x_2,\ldots)=(x_2,x_3,\ldots)$,*
