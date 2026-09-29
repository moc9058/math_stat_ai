**7.5. Theorem.** *If $A=\bigoplus_i\alpha_iP_i$ is diagonalizable and all the $\alpha_i$ are distinct, then an operator $B$ in $\mathscr B(\mathcal H)$ satisfies $AB=BA$ if and only if for each $i$, $\operatorname{ran}P_i$ reduces $B$.*

**Proof.** If all the $\alpha_i$ are distinct, then $\operatorname{ran}P_i=\ker(A-\alpha_i)$. If $AB=BA$ and $Ah=\alpha_i h$, then $ABh=BAh=B(\alpha_i h)=\alpha_i Bh$; hence $Bh\in\operatorname{ran}P_i$ whenever $h\in\operatorname{ran}P_i$. Thus $\operatorname{ran}P_i$ is left invariant by $B$. Therefore $B$ leaves $\bigvee\{\operatorname{ran}P_j:j\ne i\}=\mathcal N_i$ invariant. But since $\bigoplus_iP_i=1$, $\mathcal N_i=(\operatorname{ran}P_i)^\perp$. Thus $\operatorname{ran}P_i$ reduces $B$.

Now assume that $B$ is reduced by each $\operatorname{ran}P_i$. Thus $BP_i=P_iB$ for all $i$. If $h\in\mathcal H$, then $Ah=\sum_i\alpha_iP_i h$. Hence $BAh=\sum_i\alpha_iBP_i h=\sum_i\alpha_iP_iBh=ABh$. (Why is the first equality valid?) $\blacksquare$

Using the notation of the preceding theorem, if $AB=BA$, let $B_i=B|_{\operatorname{ran}P_i}$. Then it is appropriate to write $B=\bigoplus_iB_i$ on $\mathcal H=\bigoplus_i(P_i\mathcal H)$. One might paraphrase Theorem 7.5 by saying that $B$ commutes with a diagonalizable operator if and only if $B$ can be “diagonalized with operator entries.”

**7.6. Spectral Theorem for Compact Normal Operators.** *If $T$ is a compact normal operator on the complex Hilbert space $\mathcal H$, then $T$ has only a countable number of distinct eigenvalues. If $\{\lambda_1,\lambda_2,\ldots\}$ are the distinct nonzero eigenvalues of $T$, and $P_n$ is the projection of $\mathcal H$ onto $\ker(T-\lambda_n)$, then $P_nP_m=P_mP_n=0$ if $n\ne m$ and*

$$
\tag{7.7} T=\sum_{n=1}^{\infty}\lambda_nP_n,
$$

*where this series converges to $T$ in the metric defined by the norm on $\mathscr B(\mathcal H)$.*

**Proof.** Let $A=(T+T^*)/2$, $B=(T-T^*)/2i$. So $A,B$ are compact self-adjoint operators, $T=A+iB$, and $AB=BA$ since $T$ is normal. The idea of the proof is rather simple. We’ll get started in this proof together but the reader will have to complete the details.

By Theorem 5.1, $A=\sum_1^\infty\alpha_nE_n$, where $\alpha_n\in\mathbb R$, $\alpha_n\ne\alpha_m$ if $n\ne m$, and $E_n$ is the projection of $\mathcal H$ onto $\ker(A-\alpha_n)$. Since $AB=BA$, the idea is to use Theorem 7.5 and Theorem 5.1 applied to $B$ to diagonalize $A$ and $B$ simultaneously; that is, to find an orthonormal basis for $\mathcal H$ consisting of vectors that are simultaneously eigenvectors of $A$ and $B$.

Since $BA=AB$, $E_n\mathcal H=\mathcal L_n$ reduces $B$ for every $n$ (7.5). Let $B_n=B|_{\mathcal L_n}$; then $B_n=B_n^*$ and $\dim\mathcal L_n<\infty$. Applying (5.1) (or, rather, the corresponding theorem from linear algebra) to $B_n$, there is a basis $\{e_j^{(n)}:1\le j\le d_n\}$ for $\mathcal L_n$ and real numbers $\{\beta_j^{(n)}:1\le j\le d_n\}$ such that $B_ne_j^{(n)}=\beta_j^{(n)}e_j^{(n)}$. Thus $Te_j^{(n)}=Ae_j^{(n)}+iBe_j^{(n)}=(\alpha_n+i\beta_j^{(n)})e_j^{(n)}$.

Therefore $\{e_j^{(n)}:1\le j\le d_n,\ n\ge1\}$ is a basis for $\operatorname{cl}(\operatorname{ran}A)$ consisting of eigenvectors for $T$. It may be that $\operatorname{cl}(\operatorname{ran}A)\ne\operatorname{cl}(\operatorname{ran}T)$. Since $B$ is reduced by $\ker A=(\operatorname{ran}A)^\perp$ and $B_0=B|_{\ker A}$ is a compact self-adjoint operator there
