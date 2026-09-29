**10.5. Lemma.** *Let $\mu$ be a compactly supported measure on $\mathbb C$, $\Delta$ a Borel subset of the support of $\mu$, and put $\nu=\mu|_\Delta$. If $N=N_\mu\oplus N_\nu$ on $L^2(\mu)\oplus L^2(\nu)$ and $g\oplus h\in L^2(\mu)\oplus L^2(\nu)$ such that $h(z)\ne0$ a.e. $[\nu]$, then there is an $f$ in $L^2(\mu)$ such that $f\oplus h$ is a separating vector for $W^*(N)$ and $g\oplus h\in\operatorname{cl}[W^*(N)(f\oplus h)]$.*

**Proof.** Define $f(z)=g(z)$ for $z$ in $\Delta$ and $f(z)=1$ for $z$ not in $\Delta$. Put $\mathcal H=\operatorname{cl}[W^*(N)(f\oplus h)]=\operatorname{cl}\{\phi f\oplus\phi h:\phi\in L^\infty(\mu)\}$ since $\mu$ is a scalar-valued spectral measure for $N$. If $\Delta'$ is the complement of $\Delta$, then note that $\phi\chi_{\Delta'}\oplus0=\phi\chi_{\Delta'}(f\oplus h)\in\mathcal H$ for all $\phi$ in $L^\infty(\mu)$. Hence $L^2(\mu|_{\Delta'})\oplus0\subseteq\mathcal H$. This implies that $(1-g)\chi_{\Delta'}\oplus0\in\mathcal H$, so $g\oplus h=f\oplus h-(1-g)\chi_{\Delta'}\oplus0\in\mathcal H$.

On the other hand, if $\phi\in L^\infty(\mu)$ and $0=\phi f\oplus\phi h$, then $\phi f=\phi h=0$ a.e. $[\mu]$. Since $h(z)\ne0$ a.e. $[\nu]$, $\phi(z)=0$ a.e. $[\mu]$ on $\Delta$. But for $z$ in $\Delta'$, $f(z)=1$; hence $\phi(z)=0$ a.e. $[\mu]$ on $\Delta'$. Thus, $f\oplus h$ is a separating vector for $W^*(N)$. $\blacksquare$

**Proof of Theorem 10.1 (a):** Let $e_1$ be a separating vector for $W^*(N)$ and let $\{f_n\}$ be an orthonormal basis for $\mathcal H$ such that $f_1=e_1$. Put $\mathcal H_1=\operatorname{cl}[W^*(N)e_1]$, $\mu_1(\Delta)=\|E(\Delta)e_1\|^2$, and $N_2=N|_{\mathcal H_1^\perp}$. Let $f'_2$ be the orthogonal projection of $f_2$ onto $\mathcal H_1^\perp$. By Proposition 10.4 there is a separating vector $e_2$ for $W^*(N_2)$ such that $f'_2\in\operatorname{cl}[W^*(N_2)e_2]\equiv\mathcal H_2$. Note that $\mathcal H_2=\operatorname{cl}[W^*(N)e_2]$ and $\{f_1,f_2\}\subseteq\mathcal H_1\oplus\mathcal H_2$. Put $\mu_2(\Delta)=\|E(\Delta)e_2\|^2$. Now continue by induction. $\blacksquare$

Now for part (b) of Theorem 10.1. If $[\mu_n]=[\nu_n]$ (the notation is that of Theorem 10.1) for every $n$, then $N_{\mu_n}\cong N_{\nu_n}$ by Theorem 3.6. Therefore $N\cong M$. Thus it is the converse that causes difficulties. So assume that $N\cong M$. If $M\in\mathcal B(\mathcal K)$, $U:\mathcal H\to\mathcal K$ is an isomorphism such that $UNU^{-1}=M$, and $e_1$ is a separating vector for $W^*(N)$, then $Ue_1=f_1$ is easily seen to be a separating vector for $W^*(M)$. Since $\mu_1$ and $\nu_1$ are scalar-valued spectral measures for $N$ and $M$, respectively, it follows that $[\mu_1]=[\nu_1]$; thus $N_{\mu_1}\cong N_{\nu_1}$ by Theorem 3.6. However, here is the difficulty—the isomorphism that shows that $N_{\mu_1}\cong N_{\nu_1}$ may not be related to $U$; that is, if $\mathcal H=\bigoplus_n\mathcal H_n$, $\mathcal K=\bigoplus_n\mathcal K_n$, where $N|_{\mathcal H_n}\cong N_{\mu_n}$ and $M|_{\mathcal K_n}\cong N_{\nu_n}$, then $N|_{\mathcal H_1}\cong M|_{\mathcal K_1}$, but we do not know that $U\mathcal H_1=\mathcal K_1$. Thus we want to argue that because $N\cong M$ and $N|_{\mathcal H_1}\cong M|_{\mathcal K_1}$, then $N|_{\mathcal H_0^\perp}\cong M|_{\mathcal K_1^\perp}$. In this way we can prove (10.1.b) by induction. This step is justified by the following.

**10.6. Proposition.** *If $N$, $A$, and $B$ are normal operators, $N$ is $*$-cyclic, and $N\oplus A\cong N\oplus B$, then $A\cong B$.*

**Proof.** Let $N\in\mathcal B(\mathcal H)$, $A\in\mathcal B(\mathcal H_A)$, $B\in\mathcal B(\mathcal H_B)$, and let $U:\mathcal H\oplus\mathcal H_A\to\mathcal H\oplus\mathcal H_B$ be an isomorphism such that $U(N\oplus A)U^{-1}=N\oplus B$. Now $U$ can be written as a $2\times2$ matrix,

$$
U=\begin{bmatrix}
U_{11}&U_{12}\\
U_{21}&U_{22}
\end{bmatrix},
$$

where $U_{11}:\mathcal H\to\mathcal H$, $U_{12}:\mathcal H_A\to\mathcal H$, $U_{21}:\mathcal H\to\mathcal H_B$, $U_{22}:\mathcal H_A\to\mathcal H_B$.
