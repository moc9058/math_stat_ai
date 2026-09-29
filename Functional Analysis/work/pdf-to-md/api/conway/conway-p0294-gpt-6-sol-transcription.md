assumption that $N=M$. As stated, the theorem was proved in Putnam [1951]. The proof given here is due to Rosenblum [1958]. Another proof is in Radjavi and Rosenthal [1973]. Berberian [1959] observed that Putnam’s version can be derived from Fuglede’s original theorem by the following matrix trick. If

$$
L=\begin{bmatrix}N&0\\0&M\end{bmatrix}
\quad\text{and}\quad
A=\begin{bmatrix}0&B\\0&0\end{bmatrix}
$$

then $L$ is normal on $\mathcal H\oplus\mathcal H$ and $LA=AL$. Hence $L^*A=AL^*$, and this gives Putnam’s version.

**6.8. Corollary.** *If $N=\int z\,dE(z)$ and $BN=NB$, then $BE(\Delta)=E(\Delta)B$ for every Borel set $\Delta$.*

**Proof.** If $BN=NB$, then $BN^*=N^*B$; the conclusion now follows by The Spectral Theorem. ■

The Fuglede–Putnam Theorem can be combined with some other results we have obtained to yield the following.

**6.9. Corollary.** *If $\mu$ is a compactly supported measure on $\mathbb C$, then*

$$
\{N_\mu\}'=\mathcal A_\mu\equiv\{M_\phi:\phi\in L^\infty(\mu)\}.
$$

**Proof.** Clearly $\mathcal A_\mu\subseteq\{N_\mu\}'$. If $A\in\{N_\mu\}'$, then Theorem 6.7 implies $AN_\mu^*=N_\mu^*A$. By an easy algebraic argument, $AM_\phi=M_\phi A$ whenever $\phi$ is a polynomial in $z$ and $\bar z$. By taking weak* limits of such polynomials, it follows that $A\in\mathcal A_\mu'$. By Theorem 6.6 $A\in\mathcal A_\mu$. ■

Putnam applied his generalization of Fuglede’s Theorem to show that similar normal operators must be unitarily equivalent. This has a formal generalization which is useful.

**6.10. Proposition.** *Let $N_1$ and $N_2$ be normal operators on $\mathcal H_1$ and $\mathcal H_2$. If $X:\mathcal H_1\to\mathcal H_2$ is an operator such that $XN_1=N_2X$, then:*

(a) $\operatorname{cl}(\operatorname{ran}X)$ reduces $N_2$;

(b) $\ker X$ reduces $N_1$;

(c) If $M_1=N_1|(\ker X)^\perp$ and $M_2=N_2|\operatorname{cl}(\operatorname{ran}X)$, then $M_1\cong M_2$.

**Proof.** (a) If $f_1\in\mathcal H_1$, $N_2Xf_1=XN_1f_1\in\operatorname{ran}X$; so $\operatorname{cl}(\operatorname{ran}X)$ is invariant for $N_2$. By the Fuglede–Putnam Theorem, $XN_1^*=N_2^*X$, so $\operatorname{cl}(\operatorname{ran}X)$ is invariant for $N_2^*$.

(b) Exercise.

(c) Since $X(\ker X)^\perp\subseteq\operatorname{cl}(\operatorname{ran}X)$, part (c) will be proved if it can be shown that $N_1\cong N_2$ when $\ker X=(0)$ and $\operatorname{ran}X$ is dense. So make these assumptions and consider the polar decomposition of $X$, $X=UA$ (see Exercise 11).
