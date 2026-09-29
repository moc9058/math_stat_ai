**Claim 2: $\mathcal N$ is finite dimensional.**

Indeed, let $A_1\equiv A|_{(\ker A)^\perp}$; so $A_1:(\ker A)^\perp\to\operatorname{ran}A$ is invertible. But $A_1^{-1}(\mathcal M')=\mathcal M$, so $\dim[(\ker A)^\perp\cap\mathcal M^\perp]=\dim[(\operatorname{ran}A)\cap(\mathcal M')^\perp]$, and this last dimension is finite since $\mathcal N'$ is finite dimensional.

**Claim 3: $\mathcal N''$ is finite dimensional.**

In fact, $\dim[(\ker B)^\perp\cap(\mathcal M')^\perp]<\infty$ and so $\dim[(\operatorname{ran}B)\cap(\mathcal M'')^\perp]<\infty$. This implies that $\dim\mathcal N''<\infty$. Now represent the operators as $2\times2$ matrices:

$$
A=\begin{bmatrix}A_1&X\\0&A_2\end{bmatrix}:
\begin{matrix}
\mathcal M&&\mathcal M'\\
\oplus&\longrightarrow&\oplus\\
\mathcal N&&\mathcal N'
\end{matrix},
$$

$$
B=\begin{bmatrix}B_1&Y\\0&B_2\end{bmatrix}:
\begin{matrix}
\mathcal M'&&\mathcal M''\\
\oplus&\longrightarrow&\oplus\\
\mathcal N'&&\mathcal N''
\end{matrix},
$$

$$
BA=\begin{bmatrix}B_1A_1&Z\\0&B_2A_2\end{bmatrix}:
\begin{matrix}
\mathcal M&&\mathcal M''\\
\oplus&\longrightarrow&\oplus\\
\mathcal N&&\mathcal N''
\end{matrix}.
$$

It follows that $B_1$ and $A_1$ are invertible. Since $\mathcal N$, $\mathcal N'$, and $\mathcal N''$ are finite dimensional, the preceding lemma implies that $\operatorname{ind}A=\dim\mathcal N-\dim\mathcal N'$, $\operatorname{ind}B=\dim\mathcal N'-\dim\mathcal N''$, and $\operatorname{ind}BA=\dim\mathcal N-\dim\mathcal N''=\operatorname{ind}A+\operatorname{ind}B$.

**Case 2.** Assume $\operatorname{ind}B=-\infty$.

This is equivalent to the assumption that $\dim(\operatorname{ran}B)^\perp=\infty$. But $\operatorname{ran}B\supseteq\operatorname{ran}BA$ and so $\dim(\operatorname{ran}BA)^\perp=\infty$. Hence $\operatorname{ind}BA=-\infty=\operatorname{ind}A+\operatorname{ind}B$.

**Case 3.** Assume $B$ is invertible.

Without loss of generality we may assume that $\operatorname{ind}A=-\infty$ since the alternative situation is covered in Case 1. If $\mathcal M=B(\operatorname{ran}A)=\operatorname{ran}BA$ and $\mathcal N=B[(\operatorname{ran}A)^\perp]$, then the fact that $B$ is invertible implies that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal N$ is infinite dimensional. Thus Lemma 3.6(a) implies that $\infty=\dim\mathcal M^\perp=\dim(\operatorname{ran}BA)^\perp$ and so $\operatorname{ind}BA=-\infty=\operatorname{ind}A+\operatorname{ind}B$.

**Case 4.** $B$ is a Fredholm operator.

Again, without loss of generality we may assume that $\operatorname{ind}A=-\infty$. It must be shown that $\operatorname{ind}BA=-\infty$.

Put $\mathcal H'_1=(\ker B)^\perp$ and $\mathcal H''_1=\operatorname{ran}B$; define $B_1:\mathcal H'_1\to\mathcal H''_1$ as the restriction
