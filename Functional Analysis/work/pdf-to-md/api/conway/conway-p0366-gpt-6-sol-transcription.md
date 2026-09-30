Let $e_1$ be a unit vector in $\mathcal M_1$. Suppose $e_1,\ldots,e_n$ are orthonormal vectors such that $e_k\in\mathcal M_k$, $1\leq k\leq n$. Let $E$ be the projection of $\mathcal H$ onto $\bigvee\{e_1,\ldots,e_n\}$. If $\mathcal M_{n+1}\cap[e_1,\ldots,e_n]^\perp=(0)$, then $E$ is injective on $\mathcal M_{n+1}$. Since $\dim\mathcal M_{n+1}=\infty$ and $\dim\operatorname{ran}E<\infty$, this is impossible. Thus there is a unit vector $e_{n+1}$ in $\mathcal M_{n+1}$ such that $e_{n+1}\perp\{e_1,\ldots,e_n\}$. The orthonormal sequence $\{e_n\}$ shows that (e) does not hold.

(f) *implies* (g). Let $|A|=\int t\,dE(t)$ and let $\delta>0$. If $h\in E[0,\delta]\mathcal H$, then

$$
\begin{aligned}
\|Ah\|^2
&=\langle A^*Ah,h\rangle\\
&=\langle |A|^2h,h\rangle\\
&=\int_0^\delta t^2\,dE_{h,h}(t)\leq\delta^2E_{h,h}[0,\delta]\\
&=\delta^2\|h\|^2.
\end{aligned}
$$

So $E[0,\delta]\mathcal H\subseteq\{h:\|Ah\|\leq\delta\|h\|\}$. By (f) there is a $\delta>0$ such that $E[0,\delta)\mathcal H$ is finite dimensional.

(g) *implies* (c). Let $\mathcal M_\delta=\{E[0,\delta]\mathcal H\}^\perp$. Now $|A|$ maps $\mathcal M_\delta$ bijectively onto $\mathcal M_\delta$. In fact, the inverse of $|A|:\mathcal M_\delta\to\mathcal M_\delta$ is $\left(\int_\delta^\infty t^{-1}\,dE(t)\right)|\mathcal M_\delta$. Let $A=U|A|$ be the polar decomposition of $A$. Since $\mathcal M_\delta\subseteq\operatorname{ran}|A|\subseteq\text{initial }U$, $U$ maps $\mathcal M_\delta$ isometrically onto some closed subspace $\mathcal L$ of $\operatorname{ran}A$. Let $V=$ the inverse of $U$ on $\mathcal L$ and $V=0$ on $\mathcal L^\perp$; that is, $V|\mathcal L^\perp=0$ and $V|\mathcal L=(U|\mathcal M_\delta)^{-1}$. Hence $V$ is a partial isometry. Let $B_1=\int_\delta^\infty t^{-1}\,dE(t)$ and put $B=B_1V$. If $h\in\mathcal M_\delta$, then $BAh=B_1VU|A|h=h$. If $h\in\mathcal M_\delta^\perp=E[0,\delta]h$, $|A|h\in\mathcal M_\delta^\perp$ and so $U|A|h\perp\mathcal L$; thus $BAh=0$. Hence $BA=E(\delta,\infty)=1-E[0,\delta]$, and $E[0,\delta]$ has finite rank.

(a) *implies* (h). Let $B:\mathcal H'\to\mathcal H$ be a bounded operator such that $BA=1+L$, where $L$ is a compact operator on $\mathcal H$. If $K:\mathcal H\to\mathcal H'$ is any compact operator, then $B(A+K)=1+(L+BK)$ and $L+BK$ is compact. By definition $A+K$ is left semi-Fredholm. Since we have already shown that (a) implies (b), $\dim\ker(A+K)<\infty$.

(h) *implies* (e). Suppose (e) does not hold. So there is an orthonormal sequence, $\{e_n\}$ usch that $\|Ae_n\|\to0$. By passing to a subsequence if necessary, it may be assumed that $\sum_{n=1}^\infty\|Ae_n\|^2<\infty$. Thus for any $h$ in $\mathcal H$,

$$
\begin{aligned}
\sum|\langle h,e_n\rangle|\,\|Ae_n\|
&\leq\left[\sum|\langle h,e_n\rangle|^2\right]^{1/2}
\left[\sum\|Ae_n\|^2\right]^{1/2}\\
&\leq C\|h\|,
\end{aligned}
$$

where $C=\left[\sum\|Ae_n\|^2\right]^{1/2}$. Thus $Kh=\sum_{n=1}^\infty\langle h,e_n\rangle Ae_n$ defines a bounded operator. Moreover, if $K_nh=\sum_{j=1}^n\langle h,e_j\rangle Ae_j$, it is easy to see that $\|K_n-K\|\to0$. Thus $K$ is compact. But $(A-K)e_n=0$ for every $n$, so $\dim\ker(A-K)=\infty$. ■

As mentioned previously, the result for right semi-Fredholm operators that is analogous to the preceding theorem is left for the reader to state. We will, however, make explicit part of this result for Fredholm operators.
