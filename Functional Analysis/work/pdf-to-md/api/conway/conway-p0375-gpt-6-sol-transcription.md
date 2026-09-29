$\sigma_p(S)=\square$, and for $\lambda$ in $G$, $\operatorname{ran}(S-\lambda)$ is closed and $\dim[\operatorname{ran}(S-\lambda)]^\perp=1$. Thus $\operatorname{ind}(S-\lambda)=-1$ for $\lambda$ in $G$.

To show that these statements are true, begin by proving:

**4.8** If $\lambda\in G$, $\operatorname{ran}(S-\lambda)=\{f\in L_a^2(G):f(\lambda)=0\}$.

In fact, if $h\in L_a^2(G)$, then $[(S-\lambda)h](z)=(z-\lambda)h(z)$ so that $f=(z-\lambda)h$ vanishes at $\lambda$. Conversely, suppose $f\in L_a^2(G)$ and $f(\lambda)=0$; then $f(z)=(z-\lambda)h(z)$ for some analytic function $h$ on $G$. It must be shown that $h\in L_a^2(G)$. Let $r>0$ such that $D=\{z:|z-\lambda|\leq r\}\subseteq G$. Then

$$
\iint |h|^2=\iint_D |h|^2+\iint_{G\setminus D}|h|^2.
$$

Now $\iint_D|h|^2<\infty$ since $h$ is bounded on $D$. For $z$ in $G\setminus D$, $|h(z)|=|f(z)|/|z-\lambda|\leq r^{-1}|f(z)|$. Hence

$$
\iint_{G\setminus D}|h|^2\leq r^{-2}\iint_G|f|^2<\infty.
$$

Thus $h\in L_a^2(G)$ and $f=(S-\lambda)h$. This proves (4.8).

Using Corollary I.1.12, $f\mapsto f(\lambda)$ is a bounded linear functional on $L_a^2(G)$ whenever $\lambda\in G$. By (4.8), $\operatorname{ran}(S-\lambda)$ is the kernel of this linear functional and hence is closed.

Because $G$ is bounded, the constant functions belong to $L_a^2(G)$. So if $f\in L_a^2(G)$, $f=[f-f(\lambda)]+f(\lambda)$ and $f-f(\lambda)\in\operatorname{ran}(S-\lambda)$. Thus $L_a^2(G)=\operatorname{ran}(S-\lambda)+\mathbb C$. Therefore $\dim[\operatorname{ran}(S-\lambda)]^\perp=\dim[L_a^2(G)/\operatorname{ran}(S-\lambda)]=1$ when $\lambda\in G$.

If $\lambda\in G$, then $S-\lambda$ is not surjective; hence $G\subseteq\sigma(S)$. If $\lambda\notin\operatorname{cl}G$, then $(z-\lambda)^{-1}$ is a bounded analytic function on $G$. If $Af=(z-\lambda)^{-1}f$, then $A$ is a bounded operator on $L_a^2(G)$ and it is easy to check that $A(S-\lambda)=(S-\lambda)A=1$. Thus $\sigma(S)\subseteq\operatorname{cl}G$. Combining these two containments, we get $\sigma(S)=\operatorname{cl}G$.

From Corollary 2.4 we have that $S-\lambda$ is a Fredholm operator whenever $\lambda\in G$; thus $G\cap\sigma_e(S)=\square$. So $\sigma_e(S)\subseteq\partial G=\partial[\operatorname{cl}G]$. If $\lambda\in\partial G$, then $\lambda\in\partial\sigma(S)$; thus $\lambda\in\sigma_{ap}(S)$ (1.2). Since $\ker(S-\lambda)=(0)$, $\operatorname{ran}(S-\lambda)$ is not closed. Thus $\partial G\subseteq\sigma_{le}(S)\cap\sigma_{re}(S)$. This proves that $\sigma_e(S)=\sigma_{le}(S)=\sigma_{re}(S)=\partial G=\sigma_{ap}(S)$.

One of the primary uses of Fredholm theory is the examination of the values of $\operatorname{ind}(A-\lambda)$ for all $\lambda$ for which this makes sense. Such an examination often leads to structural information about the operator $A$. Note that $\operatorname{ind}(A-\lambda)$ is defined when $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$.

**4.9. Proposition.** *If $A\in\mathcal B(\mathcal H)$, then $\operatorname{ind}(A-\lambda)$ is constant on the components of $\mathbb C\setminus[\sigma_{le}(A)\cap\sigma_{re}(A)]$. If $\lambda$ is a boundary point of $\sigma(A)$ and $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$, then $\operatorname{ind}(A-\lambda)=0$.*

**Proof.** The map $\lambda\mapsto A-\lambda$ is a continuous map of $\mathbb C\setminus[\sigma_{le}(A)\cap\sigma_{re}(A)]$ into $\mathcal{SF}$. So the first part of the proposition follows from Corollary 3.13. If $\lambda$ is a
