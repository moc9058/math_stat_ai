$(b)\Rightarrow(f)$: If $h\in\mathcal H$, write $h=h_1+h_2$, $h_1\in\operatorname{ran}E$, $h_2\in\ker E=(\operatorname{ran}E)^\perp$. Hence
$$
\langle Eh,h\rangle
=\langle E(h_1+h_2),h_1+h_2\rangle
=\langle Eh_1,h_1\rangle
=\langle h_1,h_1\rangle
=\|h_1\|^2\geq 0.
$$

$(f)\Rightarrow(a)$: Let $h_1\in\operatorname{ran}E$ and $h_2\in\ker E$. Then by (f), $0\leq\langle E(h_1+h_2),h_1+h_2\rangle=\langle h_1,h_1\rangle+\langle h_1,h_2\rangle$. Hence $-\|h_1\|^2\leq\langle h_1,h_2\rangle$ for all $h_1$ in $\operatorname{ran}E$ and $h_2$ in $\ker E$. If there are such $h_1$ and $h_2$ with $\langle h_1,h_2\rangle=\bar\alpha\neq 0$, then substituting $k_2=-2\alpha^{-1}\|h_1\|^2h_2$ for $h_2$ in this inequality, we obtain $-\|h_1\|^2\leq-2\|h_1\|^2$, a contradiction. Hence $\langle h_1,h_2\rangle=0$ whenever $h_1\in\operatorname{ran}E$ and $h_2\in\ker E$. That is, $E$ is a projection.

$(a)\Rightarrow(d)$: Let $h,g\in\mathcal H$ and put $h=h_1+h_2$ and $g=g_1+g_2$, where $h_1,g_1\in\operatorname{ran}E$ and $h_2,g_2\in\ker E=(\operatorname{ran}E)^\perp$. Hence $\langle Eh,g\rangle=\langle h_1,g_1\rangle$. Also, $\langle E^*h,g\rangle=\langle h,Eg\rangle=\langle h_1,g_1\rangle=\langle Eh,g\rangle$. Thus $E=E^*$.

$(d)\Rightarrow(e)$: clear.

$(e)\Rightarrow(a)$: By (2.16), $\|Eh\|=\|E^*h\|$ for every $h$. Hence $\ker E=\ker E^*$. But by (2.19), $\ker E^*=(\operatorname{ran}E)^\perp$, so $E$ is a projection.

Note that by part (b) of the preceding proposition, if $E$ is a projection and $\mathcal M=\operatorname{ran}E$, then $E=P_{\mathcal M}$.

Let $P$ be a projection with $\operatorname{ran}P=\mathcal M$ and $\ker P=\mathcal N$. So both $\mathcal M$ and $\mathcal N$ are closed subspaces of $\mathcal H$ and, hence, are also Hilbert spaces. As in (I.6.1), we can form $\mathcal M\oplus\mathcal N$. If $U:\mathcal M\oplus\mathcal N\to\mathcal H$ is defined by $U(h\oplus g)=h+g$ for $h$ in $\mathcal M$ and $g$ in $\mathcal N$, then it is easy to see that $U$ is an isomorphism. Making this identification, we will often write $\mathcal H=\mathcal M\oplus\mathcal N$.

More generally, the following will be used.

**3.4. Definition.** If $\{\mathcal M_i\}$ is a collection of pairwise orthogonal subspaces of $\mathcal H$, then
$$
\bigoplus_i\mathcal M_i\equiv\bigvee_i\mathcal M_i.
$$

If $\mathcal M$ and $\mathcal N$ are two closed linear subspaces of $\mathcal H$, then
$$
\mathcal M\ominus\mathcal N\equiv\mathcal M\cap\mathcal N^\perp.
$$

This is called the *orthogonal difference* of $\mathcal M$ and $\mathcal N$.

Note that if $\mathcal M,\mathcal N\leq\mathcal H$ and $\mathcal M\perp\mathcal N$, then $\mathcal M+\mathcal N$ is closed. (Why?) Hence $\mathcal M\oplus\mathcal N=\mathcal M+\mathcal N$. The same is true, of course, for any finite collection of pairwise orthogonal subspaces but not for infinite collections.

**3.5. Definition.** If $A\in\mathcal B(\mathcal H)$ and $\mathcal M\leq\mathcal H$, say that $\mathcal M$ is an *invariant subspace* for $A$ if $Ah\in\mathcal M$ whenever $h\in\mathcal M$. In other words, if $A\mathcal M\subseteq\mathcal M$. Say that $\mathcal M$ is a *reducing subspace* for $A$ if $A\mathcal M\subseteq\mathcal M$ and $A\mathcal M^\perp\subseteq\mathcal M^\perp$.

If $\mathcal M\leq\mathcal H$, then $\mathcal H=\mathcal M\oplus\mathcal M^\perp$. If $A\in\mathcal B(\mathcal H)$, then $A$ can be written as a $2\times2$ matrix with operator entries,
$$
A=\begin{bmatrix}W&X\\Y&Z\end{bmatrix},\tag{3.6}
$$
where $W\in\mathcal B(\mathcal M)$, $X\in\mathcal B(\mathcal M^\perp,\mathcal M)$, $Y\in\mathcal B(\mathcal M,\mathcal M^\perp)$, and $Z\in\mathcal B(\mathcal M^\perp)$.
