Continuing in this way produces a sequence of vectors $\{e_n\}$ such that if $\mathcal H_n=\operatorname{cl}[W^*(N)e_n]$ and $\mu_n(\Delta)=\|E(\Delta)e_n\|^2$, then $\mathcal H_n\perp\mathcal H_m$ for $n\ne m$, $\mu_{n+1}\ll\mu_n$, and $N\mid\mathcal H_n\cong N_{\mu_n}$. The difficulty here is that $\mathcal H$ is not necessarily equal to $\bigoplus_n\mathcal H_n$ so that $N$ and $\bigoplus_n N_{\mu_n}$ cannot be proved to be unitarily equivalent. (Actually, $N$ and $\bigoplus_n N_{\mu_n}$ are unitarily equivalent, but to show this we need the force of Theorem 10.1. See Exercise 2.) The following provides us with a look at an example to see what can go wrong.

**10.3. Example.** For $n\geqslant 1$ let $\mu_n=$ Lebesgue measure on $[0,1+2^{-n}]$ and let $\mu_\infty=$ Lebesgue measure on $[0,1]$. Put $N=\bigoplus_{n=1}^{\infty}N_{\mu_n}\oplus N_{\mu_\infty}$. If the process of the preceding paragraph is followed, it might be that vectors $\{e_n\}$ that are chosen are the vectors with a 1 in the $L^2(\mu_n)$ coordinate and zeros elsewhere. Thus the spaces $\{\mathcal H_n\}$ are precisely the spaces $\{L^2(\mu_n)\}$ and $[\bigoplus_1^\infty\mathcal H_n]^\perp=L^2(\mu_\infty)$.

(Nevertheless, $N\cong\bigoplus_1^\infty N_{\mu_n}$. Indeed, let $\nu_n=\mu_n|[1,1+2^{-n}]$; so $\mu_n=\mu_\infty+\nu_n$ and $\mu_\infty\perp\nu_n$. Thus $N_{\mu_n}\cong N_{\nu_n}\oplus N_{\mu_\infty}$. Therefore

$$
\begin{aligned}
N&=\bigoplus_1^\infty N_{\mu_n}\oplus N_{\mu_\infty}\\
&\cong\bigoplus_1^\infty N_{\nu_n}\oplus N_{\mu_\infty}^{(\infty)}\oplus N_{\mu_\infty}\\
&\cong\bigoplus_1^\infty N_{\nu_n}\oplus N_{\mu_\infty}^{(\infty)}\\
&\cong\bigoplus_1^\infty N_{\mu_n}.)
\end{aligned}
$$

After an examination of the statement of Theorem 10.1, it becomes clear that some procedure like the one outlined in the paragraph preceding Example 10.3 should be used. It only becomes necessary to modify this procedure so that the vectors $\{e_n\}$ can be chosen in such a way that $\mathcal H=\bigoplus_1^\infty\mathcal H_n$. For example, let, as above, $e_1$ be a separating vector for $W^*(N)$ and let $\{f_n\}$ be an orthonormal basis for $\mathcal H$ such that $f_1=e_1$. We now want to choose the vectors $\{e_n\}$ such that $\{f_1,\ldots,f_n\}\subseteq\mathcal H_1\oplus\cdots\oplus\mathcal H_n$. In this way we will meet success. The vital link here is the next result.

**10.4. Proposition.** *If $N$ is a normal operator on $\mathcal H$ and $e\in\mathcal H$, then there is a separating vector $e_0$ for $W^*(N)$ such that $e\in\operatorname{cl}[W^*(N)e_0]$.*

**Proof.** Let $f_0$ be any separating vector for $W^*(N)$, let $E$ be the spectral measure for $N$, let $\mu(\Delta)=\|E(\Delta)f_0\|^2$, and put $\mathcal G=\operatorname{cl}[W^*(N)f_0]$. Write $e=g_1+h_1$, where $g_1\in\mathcal G$ and $h_1\in\mathcal G^\perp$.

Let $\eta(\Delta)=\|E(\Delta)h_1\|^2$ and let $\mathcal L=\operatorname{cl}[W^*(N)h_1]$. Hence $\eta\ll\mu$, $N$ is reduced by both $\mathcal L$ and $\mathcal G$, and $\mathcal L\perp\mathcal G$. Moreover, $N\mid\mathcal G\cong N_\mu$ and $N\mid\mathcal L\cong N_\eta$. Now the fact that $\eta\ll\mu$ implies that there is a Borel set $\Delta$ such that $[\eta]=[\mu|\Delta]$. (Why?) Hence $N\mid\mathcal L\cong N_\nu$ if $\nu=\mu|\Delta$ (Theorem 3.6). Let $U:\mathcal G\oplus\mathcal L\to L^2(\mu)\oplus L^2(\nu)$ be an isomorphism such that $U((0)\oplus\mathcal L)\subseteq(0)\oplus L^2(\nu)$ and $U(N\mid\mathcal G\oplus\mathcal L)U^{-1}=N_\mu\oplus N_\nu$. Since $e=g_1+h_1\in\mathcal G\oplus\mathcal L$, let $Ue=g\oplus h$. Because $h_1$ is a $*$-cyclic vector for $N\mid\mathcal L$, $h(z)\ne0$ a.e. $[\nu]$.

This reduces the proof of this proposition to proving the next lemma. $\blacksquare$
