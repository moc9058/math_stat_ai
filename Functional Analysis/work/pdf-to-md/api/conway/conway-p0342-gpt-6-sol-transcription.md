$\phi_n$ such that $N_n\cong M_{\phi_n}$. Let $X$ = the disjoint union of $\{X_n\}$ and let $\Omega=\{\Delta\subseteq X:\Delta\cap X_n\in\Omega_n\text{ for every }n\}$. If $\Delta\in\Omega$, let $\mu(\Delta)=\sum_{1}^{\infty}\mu_n(\Delta\cap X_n)$. Let $\phi:X\to\mathbb C$ be defined by $\phi(x)=\phi_n(x)$ if $x\in X_n$. Then $\phi$ is $\Omega$-measurable and $N\cong M_\phi$ on $L^2(X,\Omega,\mu)$.

## Exercises

1. Prove Theorem 4.10.

2. Show that if $A$ is a symmetric operator that is normal, then $A$ is self-adjoint.

3. With the notation of Theorem 4.7, show that for $h$ in $\mathcal D_\phi$, $\|(\int\phi\,dE)h\|^2=\int|\phi|^2\,dE_{h,h}$.

4. Using the notation of Theorem 4.10, what is $\sigma(\int\phi\,dE)$?

5. If $\Delta_n$ and $E_n$ are as in the proof of the Spectral Theorem, show that $E_n(\Delta_{n+1})=E_n(\Delta_{n-1})=0$.

6. Use the Spectral Theorem to show that if $0<a\leq b<\infty$, $\Delta=\{z\in\mathbb C:a\leq|z|\leq b\}$, and $N=\int z\,dE(z)$ is the spectral decomposition of the normal operator $N$, then
   $$
   E(\Delta)\mathcal H=\{h\in\operatorname{dom}N:a^n\|h\|\leq\|N^nh\|\leq b^n\|h\|\text{ for all }n\geq1\}.
   $$

7. State and prove a polar decomposition for operators in $\mathcal C(\mathcal H,\mathcal H)$.

8. If $A$ is self-adjoint, prove that $\exp(iA)$ is unitary.

9. (Fuglede–Putnam Theorem.) If $N$, $M$ are normal operators and $A$ is a bounded operator such that $AN\subseteq MA$, then $AN^*\subseteq M^*A$.

10. Prove Theorem 4.18.

11. If $\mu_1,\mu_2$ are finite measures on $\mathbb C$ and $N_{\mu_1},N_{\mu_2}$ are defined as in Example 4.17, show that $N_{\mu_1}\cong N_{\mu_2}$ iff $[\mu_1]=[\mu_2]$.

12. Fill in the details of the proof of Theorem 4.19.

## §5. Stone’s Theorem

If $A$ is a self-adjoint operator on $\mathcal H$, then $\exp(iA)$ is a unitary operator (Exercise 4.7). Hence $U(t)=\exp(itA)$ is unitary for all $t$ in $\mathbb R$. The purpose of this section is not to investigate the individual operators $\exp(itA)$, but rather the entire collection of operators $\{\exp(itA):t\in\mathbb R\}$. In fact, as the first theorem shows, $U:\mathbb R\to$ unitaries on $\mathcal H$ is a group homomorphism with certain properties. Stone’s Theorem provides a converse to this; every such homomorphism arises in this way.

**5.1. Theorem.** *If $A$ is self-adjoint and $U(t)=\exp(itA)$ for $t$ in $\mathbb R$, then*

(a) $U(t)$ is unitary;

(b) $U(s+t)=U(s)U(t)$ for all $s$ in $\mathbb R$;

(c) if $h\in\mathcal H$, then $\lim_{s\to t}U(s)h=U(t)h$;
