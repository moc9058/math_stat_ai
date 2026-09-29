Again, the fact that the spaces $\{\mathcal H_n\}$ are pairwise orthogonal implies

$$
\begin{aligned}
E(\Lambda_1\cap\Lambda_2)
&=\left(\sum_{n=1}^{\infty}E_n(\Lambda_1\cap\Delta_n)\right)
  \left(\sum_{n=1}^{\infty}E_n(\Lambda_2\cap\Delta_n)\right)\\
&=E(\Lambda_1)E(\Lambda_2).
\end{aligned}
$$

If $h\in\mathcal H$, then $\langle E(\Delta)h,h\rangle=\sum_{n=1}^{\infty}\langle E_n(\Delta\cap\Delta_n)h,h\rangle$. So if $\{\Lambda_j\}_{j=1}^{\infty}$ are pairwise disjoint Borel sets,

$$
\begin{aligned}
\left\langle E\left(\bigcup_{j=1}^{\infty}\Lambda_j\right)h,h\right\rangle
&=\sum_{n=1}^{\infty}
\left\langle E_n\left(\left(\bigcup_{j=1}^{\infty}\Lambda_j\right)\cap\Delta_n\right)h,h\right\rangle\\
&=\sum_{n=1}^{\infty}\sum_{j=1}^{\infty}
\langle E_n(\Lambda_j\cap\Delta_n)h,h\rangle.
\end{aligned}
$$

Since each term in this double summation is non-negative, the order of summation can be reversed. Thus

$$
\begin{aligned}
\left\langle E\left(\bigcup_{j=1}^{\infty}\Lambda_j\right)h,h\right\rangle
&=\sum_{j=1}^{\infty}\sum_{n=1}^{\infty}
\langle E_n(\Lambda_j\cap\Delta_n)h,h\rangle\\
&=\sum_{j=1}^{\infty}\langle E(\Lambda_j)h,h\rangle.
\end{aligned}
$$

So $E(\bigcup_{j=1}^{\infty}\Lambda_j)=\sum_{j=1}^{\infty}E(\Lambda_j)$; therefore $E$ is a spectral measure.

Let $M=\int z\,dE(z)$ be defined as in Theorem 4.7. Thus $\mathcal H_n\subseteq\operatorname{dom}M$ and by the Spectral Theorem for bounded operators, $Mh=N_nh=Nh$ if $h\in\mathcal H_n$. If $h$ is any vector in $\operatorname{dom}M$, $h=\sum_1^\infty h_n$, $h_n\in\mathcal H_n$, and $\sum_1^\infty\|Nh_n\|^2<\infty$. Because $N$ is closed, $h\in\operatorname{dom}N$ and $Nh=Mh$. Thus $M\subseteq N$. To prove the other inclusion, note that $M$ is a closed operator by Lemma 4.4. Thus, by (4.2.e), it suffices to show that $\{h\oplus Nh:h\in\operatorname{dom}N^*N\}\subseteq\operatorname{gra}M$. If $h\in\operatorname{dom}N^*N$, there is a vector $g$ such that $h=Bg$. Then $P_nNh=P_nNBg=P_nCg=CP_ng$ (Why?) $=NP_nh$. If $h_n=P_nh$, then $\sum\|Nh_n\|^2=\sum\|P_nNh\|^2=\|Nh\|^2<\infty$. Therefore $h\in\operatorname{dom}M$ and so, by the preceding argument, $Nh=Mh$. That is, $h\oplus Nh\in\operatorname{gra}M$. This proves (a).

**4.15. Claim.**

$$
\sigma(N)=\operatorname{cl}\left[\bigcup_{n=1}^{\infty}\sigma(N_n)\right].
$$

It is left to the reader to show that $\bigcup_{n=1}^{\infty}\sigma(N_n)\subseteq\sigma(N)$. Since $\sigma(N)$ is closed, this proves half of (4.15). If $\lambda\notin\operatorname{cl}[\bigcup_{n=1}^{\infty}\sigma(N_n)]$, then there is a $\delta>0$ such that $|\lambda-z|\geq\delta$ for all $z$ in $\bigcup_{n=1}^{\infty}\sigma(N_n)$. Thus $(N_n-\lambda)^{-1}$ exists and $\|(N_n-\lambda)^{-1}\|\leq\delta^{-1}$ for all $n$. Thus $A=\bigoplus_{n=1}^{\infty}(N_n-\lambda)^{-1}$ is a bounded operator. It follows that $A=(N-\lambda)^{-1}$, so $\lambda\notin\sigma(N)$.

By (4.15) if $\Delta\cap\sigma(N)=\square$, $\Delta\cap\sigma(N_n)=\square$ for all $n$. Thus $E_n(\Delta)=0$ for all $n$. Hence $E(\Delta)=0$ and (b) holds.

If $U$ is open and $U\cap\sigma(N)\ne\square$, then (4.15) implies $U\cap\sigma(N_n)\ne\square$ for some $n$. Since $E_n(U)\ne0$, $E(U)\ne0$ and (c) is true.
