(a) $\rho$ is a $*$-isomorphism and an isometry;

(b) $\rho\colon (L^\infty(\mu),\text{ weak}^*)\to(W^*(N),\mathrm{WOT})$ is a homeomorphism.

**Proof.** Let $e$ be a separating vector such that $\mu=\mu_e$ [by (8.6) and (8.9)]. If $\phi\in B(\sigma(N))$ and $\phi=0$ a.e. $[\mu]$, then $\phi(N)=0$ by (8.9d); so $\rho(\phi)=\phi(N)$ is a well-defined map. It is left to the reader to show that $\rho$ is a $*$-homomorphism. By Lemma 8.7, $\rho$ is surjective. Also, if $\rho(\phi)=\phi(N)=0$, then $\phi=0$ a.e. $[\mu]$ by (8.9d). Thus $\rho$ is a $*$-isomorphism. By (VIII.4.8) $\rho$ is an isometry. (A proof avoiding (VIII.4.8) is possible—it is left as an exercise.) This proves (a).

Let $\{\phi_i\}$ be a net in $L^\infty(\mu)$ and suppose that $\phi_i(N)\to0$ (WOT). If $f\in L^1(\mu)$ and $f\geq0$, $f\mu\ll\mu=\mu_e$. By Lemma 8.6 there is a vector $h$ such that $f\mu=\mu_h$. Thus $\int\phi_i f\,d\mu=\int\phi_i\,d\mu_h=\langle\phi_i(N)h,h\rangle\to0$. Thus $\phi_i\to0$ (weak$^*$) in $L^\infty(\mu)$. This proves half of (b); the other half is left as an exercise. $\blacksquare$

**8.11. The Spectral Mapping Theorem.** *If $N$ is a normal operator on a separable space and $\mu$ is a scalar-valued spectral measure for $N$ and if $\phi\in L^\infty(\mu)$, then $\sigma(\phi(N))=$ the $\mu$-essential range of $\phi$.*

**Proof.** Use (8.10) and the fact (2.6) that the $\mu$-essential range of $\phi$ is the spectrum of $\phi$ as an element of $L^\infty(\mu)$. $\blacksquare$

**8.12. Proposition.** *Let $N$, $\mu$, $\phi$ be as in (8.11). If $N=\int z\,dE$, then $\mu\circ\phi^{-1}$ is a scalar-valued spectral measure for $\phi(N)$ and $E\circ\phi^{-1}$ is its spectral measure.*

## Exercises

1. What is a scalar-valued spectral measure for a diagonalizable normal operator?

2. Let $N_1$ and $N_2$ be normal operators with scalar-valued spectral measures $\mu_1$ and $\mu_2$. What is a scalar spectral measure for $N_1\oplus N_2$?

3. Let $\{e_n\}$ be an orthonormal basis for $\mathcal H$ and put $\mu(\Delta)=\sum_{n=1}^{\infty}2^{-n}\|E(\Delta)e_n\|^2$. Show that $\mu$ is a scalar-valued spectral measure for $N$.

4. Give an example of a normal operator on a nonseparable space which has no scalar-valued spectral measure.

5. Prove that the map $\rho$ in (8.10) is an isometry without using (VIII.4.8).

6. Prove Proposition 8.12.

7. Show that if $\mu$ and $\nu$ are compactly supported measures on $\mathbf C$, the following statements are equivalent: (a) $N_\mu\oplus N_\nu$ is $*$-cyclic; (b) $W^*(N_\mu\oplus N_\nu)=W^*(N_\mu)\oplus W^*(N_\nu)$; (c) $\mu\perp\nu$.

8. If $M$ and $N$ are normal operators with scalar-valued spectral measures $\mu$ and $\nu$, respectively, show that the following are equivalent: (a) $W^*(M\oplus N)=W^*(M)\oplus W^*(N)$; (b) $\{M\oplus N\}'=\{M\}'\oplus\{N\}'$; (c) there is no operator $A$ such that $MA=AN$ other than $A=0$; (d) $\mu\perp\nu$.

9. If $M$ and $N$ are normal operators, show that $C^*(M\oplus N)=C^*(M)\oplus C^*(N)$ if and only if $\sigma(M)\cap\sigma(N)=\square$.
