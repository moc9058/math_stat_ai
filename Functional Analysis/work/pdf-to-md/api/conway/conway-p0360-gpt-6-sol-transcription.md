$$
\begin{aligned}
&= \sum_{\substack{j=0\\ k=1}}^{\infty} m_{j+k}\alpha_j\overline{\beta}_{k-1}\\
&= [x,T_0y].
\end{aligned}
$$

In particular, if $x\in\mathcal K_0$, then the preceding equation and the CBS inequality imply that

$$
\begin{aligned}
\left|[T_0x,T_0x]\right|
&=\left|[T_0^2x,x]\right|
\leqslant [T_0^2x,T_0^2x][x,x]\\
&=0.
\end{aligned}
$$

Hence $T_0\mathcal K_0\subseteq\mathcal K_0$. Thus $T_0$ induces a linear transformation $T$ on $\mathcal H_1$ defined by $T(x+\mathcal K_0)=T_0x+\mathcal K_0$. It follows that $\langle Th,f\rangle=\langle h,Tf\rangle$ for all $h,f$ in $\mathcal H_1$. Since $\mathcal H_1$ is, by definition, dense in $\mathcal H$, $T$ is a densely defined symmetric operator on $\mathcal H$. Now to show that $T$ has a self-adjoint extension.

Define $J_0:\mathcal H_0\to\mathcal H_0$ by $J_0(\{\alpha_n\})=\{\overline{\alpha}_n\}$. It is easy to see that $J_0$ is conjugate linear and $J_0^2=1$. Also, $J_0T_0=T_0J_0$. An easy calculation shows that $[J_0x,J_0y]=[x,y]$ for all $x,y$ in $\mathcal H_0$. So $J_0\mathcal K_0\subseteq\mathcal K_0$ and $J_0$ induces a conjugate linear function $J_1:\mathcal H_1\to\mathcal H_1$ defined by $J_1(x+\mathcal K_0)=J_0x+\mathcal K_0$. It follows that $J_1T=TJ_1$, $J_1^2=1$, and $\|J_1h\|=\|h\|$ for all $h$ in $\mathcal H_1$. Thus $J_1$ extends to a conjugate linear $J:\mathcal H\to\mathcal H$ such that $J^2=1$ and $\|Jh\|=\|h\|$ for all $h$ in $\mathcal H$. Hence $J$ is continuous. Also, $J\operatorname{dom}T=J_1\mathcal H_1\subseteq\mathcal H_1=\operatorname{dom}T$ and $TJ\subseteq JT$. By Proposition 7.2, $T$ has a self-adjoint extension $A$.

Let $e_0=\{1,0,0,\ldots\}\in\mathcal H_0$. Hence $T_0^ne_0$ has a 1 in the $n$th place and zeros elsewhere. If $e=e_0+\mathcal K_0$, then $e\in\operatorname{dom}T^n\subseteq\operatorname{dom}A^n$ for all $n\geqslant0$. Also,

$$
\langle A^ne,e\rangle=[T_0^ne_0,e_0]=m_n
$$

for $n\geqslant0$.

(c) implies (a). By the Spectral Theorem there is a spectral measure $E$ for $A$. Let $\mu=E_{e,e}$; by (4.11) $\mu$ is supported on $\mathbf R$ and, since $e\in\operatorname{dom}A$, $\mu$ is finite. Moreover, since $e\in\operatorname{dom}A^n$ for every $n\geqslant0$ it follows (supply the details) that $\int t^n\,d\mu(t)<\infty$ for every $n\geqslant0$. Finally, by (4.9), $m_n=\langle A^ne,e\rangle=\int t^n\,d\mu(t)$ for every $n\geqslant0$. $\blacksquare$

The measure obtained in Theorem 7.1 need not be unique since, in the proof that (b) implies (c) above, the self-adjoint extension of $T$ may not be unique. See pages 201–202 of Berg, Christensen, and Ressel [1984] for an example as well as further discussions of moment problems.

## Exercises

1. (Stieltjes.) Let $\{m_n:n\geqslant0\}$ be a sequence of real numbers and show that the following statements are equivalent. (a) There is a positive regular Borel measure $\mu$ on $[0,\infty)$ such that $m_n=\int t^n\,d\mu(t)$ for all $n\geqslant0$. (b) If $\alpha_0,\ldots,\alpha_n\in\mathbf C$, then $\sum_{j,k=0}^{n}m_{j+k}\alpha_j\overline{\alpha}_k\geqslant0$ and $\sum_{j,k=0}^{n}m_{j+k+1}\alpha_j\overline{\alpha}_k\geqslant0$. (c) There is a self-adjoint operator $A$ with $\sigma(A)\subseteq[0,\infty)$ and a vector $e$ in $\operatorname{dom}A^n$ for all $n\geqslant0$ such that $m_n=\langle A^ne,e\rangle$ for $n\geqslant0$.

2. (Bochner.) Let $m:\mathbf R\to\mathbf C$ be a function and show that the following statements are
