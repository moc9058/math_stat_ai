$l^\infty(\mathbb C)\to\mathcal B(\mathcal H)$ has the following properties:

(a) $\phi\mapsto\phi(T)$ is a multiplicative linear map of $l^\infty(\mathbb C)$ into $\mathcal B(\mathcal H)$. If $\phi=1$, $\phi(T)=1$; if $\phi(z)=z$ on $\sigma_p(T)\cup\{0\}$, then $\phi(T)=T$.

(b) $\|\phi(T)\|=\sup\{|\phi(\lambda)|:\lambda\in\sigma_p(T)\}$.

(c) $\phi(T)^*=\phi^*(T)$, where $\phi^*$ is the function defined by $\phi^*(z)=\overline{\phi(z)}$.

(d) If $A\in\mathcal B(\mathcal H)$ and $AT=TA$, then $A\phi(T)=\phi(T)A$ for all $\phi$ in $l^\infty(\mathbb C)$.

**Proof.** Adopt the notation of Theorem 7.6 and (7.10).

(a) If $\phi,\psi\in l^\infty(\mathbb C)$, then $(\phi\psi)(z)=\phi(z)\psi(z)$ for $z$ in $\mathbb C$. Also,
$\phi(T)\psi(T)h=[\phi(0)P_0+\sum_n\phi(\lambda_n)P_n][\psi(0)P_0+\sum_m\psi(\lambda_m)P_m]h
=[\phi(0)P_0+\sum_n\phi(\lambda_n)P_n][\psi(0)P_0h+\sum_m\psi(\lambda_m)P_mh]$.
Since $P_nP_m=0$ when $n\ne m$, this gives that
$\phi(T)\psi(T)h=\phi(0)\psi(0)P_0h+\sum_n\phi(\lambda_n)\psi(\lambda_n)P_nh=(\phi\psi)(T)h$.
Thus $\phi\mapsto\phi(T)$ is multiplicative. The linearity of the map is left to the reader. If $\phi(z)=1$, then $\phi(T)=1(T)=P_0+\sum_{n=1}^{\infty}P_n=1$ since $\{P_0,P_1,\ldots\}$ is a partition of the identity. If $\phi(z)=z$, $\phi(\lambda_n)=\lambda_n$ and so $\phi(T)=T$.

Parts (b) and (c) follow from Exercise 5.

(d) If $AT=TA$, Theorem 7.5 implies that $P_0\mathcal H,P_1\mathcal H,\ldots$ all reduce $A$. Fix $h_n$ in $P_n\mathcal H$, $n\geq 0$. If $\phi\in l^\infty(\mathbb C)$, then $Ah_n\in P_n\mathcal H$ and so $\phi(T)Ah_n=\phi(\lambda_n)Ah_n=A(\phi(\lambda_n)h_n)=A\phi(T)h_n$. If $h\in\mathcal H$, then $h=\sum_{n=0}^{\infty}h_n$, where $h_n\in P_n$. Hence $\phi(T)Ah=\sum_{n=0}^{\infty}\phi(T)Ah_n=\sum_{n=0}^{\infty}A\phi(T)h_n=A\phi(T)h$. (Justify the first equality.) $\blacksquare$

Which operators on $\mathcal H$ can be expressed as $\phi(T)$ for some $\phi$ in $l^\infty(\mathbb C)$? Part (d) of the preceding theorem provides the answer.

**7.12. Theorem.** *If $T$ is a compact normal operator on a C-Hilbert space, then $\{\phi(T):\phi\in l^\infty(\mathbb C)\}$ is equal to*
$$
\{B\in\mathcal B(\mathcal H):BA=AB\text{ whenever }AT=TA\}.
$$

**Proof.** Half of the desired equality is obtained from (7.11d). So let $B\in\mathcal B(\mathcal H)$ and assume that $BA=AB$ whenever $AT=TA$. Thus, $B$ must commute with $T$ itself. By (7.5), $B$ is reduced by each $P_n\mathcal H\equiv\mathcal H_n$, $n\geq 0$; put $B_n=B|_{\mathcal H_n}$. Fix $n\geq 0$ for the moment and let $A_n$ be any bounded operator in $\mathcal B(\mathcal H_n)$. Define $Ah=A_nh$ if $h\in\mathcal H_n$ and $Ah=0$ if $h\in\mathcal H_m$, $m\ne n$, and extend $A$ to $\mathcal H$ by linearity; so $A=\bigoplus_{m=0}^{\infty}A_m$ where $A_m=0$ if $m\ne n$. By (7.5), $AT=TA$; hence $BA=AB$. This implies that $B_nA_n=A_nB_n$. Since $A_n$ was arbitrarily chosen from $\mathcal B(\mathcal H_n)$, $B_n=\beta_n$ for some $\beta_n$ (Exercise 7). If $\phi:\mathbb C\to\mathbb C$ is defined by $\phi(0)=\beta_0$ and $\phi(\lambda_n)=\beta_n$ for $n\geq 1$, then $B=\phi(T)$. $\blacksquare$

**7.13. Definition.** If $A\in\mathcal B(\mathcal H)$, then $A$ is *positive* if $\langle Ah,h\rangle\geq 0$ for all $h$ in $\mathcal H$. In symbols this is denoted by $A\geq 0$.

Note that by Proposition 2.12 every positive operator on a complex Hilbert space is self-adjoint.
