$\mathcal H_\Delta=P(\Delta)\mathcal H\subseteq\operatorname{dom}N$, $\mathcal H_\Delta$ is invariant for both $N$ and $N^*$, and $N|_{\mathcal H_\Delta}$ is a bounded normal operator with $\|N|_{\mathcal H_\Delta}\|\leq[(1-\delta)/\delta]^{1/2}$.

**Proof.** If $h\in\mathcal H_\Delta$, then because $P(\Delta)=\chi_\Delta(B)$,
$\|Bh\|^2=\langle B^2P(\Delta)h,h\rangle=\int_\Delta t^2\,dP_{h,h}\geq\delta^2\|h\|^2$. So $B|_{\mathcal H_\Delta}$ is invertible and there is a $g$ in $\mathcal H_\Delta$ such that $h=Bg$. But $\operatorname{ran}B=\operatorname{dom}(1+N^*N)\subseteq\operatorname{dom}N$. Hence $h\in\operatorname{dom}N$; that is, $\mathcal H_\Delta\subseteq\operatorname{dom}N$.

Let $h\in\mathcal H_\Delta$ and again let $g\in\mathcal H_\Delta$ such that $h=Bg$. Hence $Nh=NBg=Cg$. By Lemma 4.12, $BC=CB$; so by (IX.2.2), $P(\Delta)C=CP(\Delta)$. Since $g\in\mathcal H_\Delta$, $Nh=Cg\in\mathcal H_\Delta$. Note that if $M=N^*$ and $B_1=(1+M^*M)^{-1}$, then $B_1=B$. From the preceding argument $N^*\mathcal H_\Delta=M\mathcal H_\Delta\subseteq\mathcal H_\Delta$. It easily follows that $N|_{\mathcal H_\Delta}$ is normal.

Finally, if $h\in\mathcal H_\Delta$, then

$$
\begin{aligned}
\|Nh\|^2
&=\langle N^*Nh,h\rangle\\
&=\langle[(N^*N+1)-1]h,h\rangle\\
&=\int_\delta^1(t^{-1}-1)\,dP_{h,h}(t)
\leq\|h\|^2(1-\delta)/\delta.
\end{aligned}
$$

Hence $\|N|_{\mathcal H_\Delta}\|\leq[(1-\delta)/\delta]^{1/2}$. $\blacksquare$

**Proof of the Spectral Theorem.** Let $B=(1+N^*N)^{-1}$ and $C=N(1+N^*N)^{-1}$ as in Lemma 4.12. Let $B=\int_0^1t\,dP(t)$ be the spectral decomposition of $B$ and put $P_n=P(1/(n+1),1/n]$ for $n\geq1$. Since $\ker B=(0)=P(\{0\})\mathcal H$, $\sum_{n=1}^\infty P_n=1$. Let $\mathcal H_n=P_n\mathcal H$. By Lemma 4.13, $\mathcal H_n\subseteq\operatorname{dom}N$, $\mathcal H_n$ reduces $N$, and $N_n\equiv N|_{\mathcal H_n}$ is a bounded normal operator with $\|N_n\|\leq n^{1/2}$. Also, if $h\in\mathcal H_n$, $(1+N_n^*N_n)Bh=B(1+N_n^*N_n)h=h$; that is,

$$
B|_{\mathcal H_n}=(1+N_n^*N_n)^{-1}.
$$

Thus if $\lambda\in\sigma(N_n)$, $(1+|\lambda|^2)^{-1}\in\sigma(B|_{\mathcal H_n})\subseteq[1/(n+1),1/n]$. Thus $\sigma(N_n)\subseteq\{z\in\mathbb C:(n-1)^{1/2}\leq|z|\leq n^{1/2}\}\equiv\Delta_n$. Let $N_n=\int z\,dE_n(z)$ be the spectral decomposition of $N_n$. For any Borel subset $\Delta$ of $\mathbb C$, let $E(\Delta)$ be defined by

$$
\tag{4.14}
E(\Delta)=\sum_{n=1}^{\infty}E_n(\Delta\cap\Delta_n).
$$

Note that $E_n(\Delta\cap\Delta_n)$ is a projection with range in $\mathcal H_n$. Since $\mathcal H_n\perp\mathcal H_m$ for $n\neq m$, (4.14) defines a projection in $\mathcal B(\mathcal H)$. (Technically $E(\Delta)$ should be defined by $E(\Delta)=\sum_{n=1}^\infty E_n(\Delta\cap\Delta_n)P_n$. But this technicality does not add anything to understanding.)

Now to show that $E$ is a spectral measure. Clearly $E(\mathbb C)=1$ and $E(\square)=0$. If $\Lambda_1$ and $\Lambda_2$ are Borel subsets of $\mathbb C$, then

$$
\begin{aligned}
E(\Lambda_1\cap\Lambda_2)
&=\sum_{n=1}^{\infty}E_n(\Lambda_1\cap\Lambda_2\cap\Delta_n)\\
&=\sum_{n=1}^{\infty}E_n(\Lambda_1\cap\Delta_n)E_n(\Lambda_2\cap\Delta_n).
\end{aligned}
$$
