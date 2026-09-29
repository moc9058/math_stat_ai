$A|_{\mathcal H_h}$ is meaningful. It will be shown that the map $A\mapsto A|_{\mathcal H_h}$ is a $*$-isomorphism of $W^*(N)$ onto $W^*(N_h)$ if $h$ is a separating vector for $W^*(N)$. Since $N_h$ is $*$-cyclic, Theorem 6.6 and Corollary 6.9 show how to determine $W^*(N_h)$.

We begin with a modest lemma.

**8.5. Lemma.** *If $h\in\mathcal H$ and $\rho_h:W^*(N)\to W^*(N_h)$ is defined by $\rho_h(A)=A|_{\mathcal H_h}$, then $\rho_h$ is a $*$-epimorphism that is WOT-continuous. Moreover, If $\psi\in B(\sigma(N))$, then $\rho_h(\psi(N))=\psi(N_h)$ and if $A\in W^*(N)$, then there is a $\phi$ in $B(\sigma(N_h))$ such that $\rho_h(A)=\phi(N_h)$.*

**Proof.** First let us see that $\rho_h$ maps $W^*(N)$ into $W^*(N_h)$. If $p(z,\bar z)$ is a polynomial in $z$ and $\bar z$ then $\rho_h[p(N,N^*)]=p(N_h,N_h^*)$ as an algebraic manipulation shows. If $\{p_i\}$ is a net of such polynomials such that $p_i(N,N^*)\to A$ (WOT), then for $f,g$ in $\mathcal H_h$, $\langle p_i(N,N^*)f,g\rangle\to\langle Af,g\rangle$; thus $p_i(N_h,N_h^*)\to\rho_h(A)$ (WOT) and so $\rho_h(A)\in W^*(N_h)$. It is left as an exercise for the reader to show that $\rho_h$ is a $*$-homomorphism. Also, the preceding argument can be used to show that $\rho_h$ is WOT continuous.

If $\psi\in B(\sigma(N))$, there is a net $\{p_i(z,\bar z)\}$ of polynomials in $z$ and $\bar z$ such that $\int p_i\,d\nu\to\int\psi\,d\nu$ for every $\nu$ in $M(\sigma(N))$. (Why?) Since $\sigma(N_h)\subseteq\sigma(N)$ (Why?), $\int p_i\,d\eta\to\int\psi\,d\eta$ for every $\eta$ in $M(\sigma(N_h))$. Therefore $p_i(N,N^*)\to\psi(N)$ (WOT) and $p_i(N_h,N_h^*)\to\psi(N_h)$ (WOT). But $\rho_h(p_i(N,N^*))=p_i(N_h,N_h^*)$ and $\rho_h(p_i(N,N^*))\to\rho_h(\psi(N))$; hence $\rho_h(\psi(N))=\psi(N_h)$.

Let $U_h:\mathcal H_h\to L^2(\mu_h)$ be the isomorphism such that $U_hh=1$ and $U_hN_hU_h^{-1}=N_{\mu_h}$. If $A\in W^*(N)$ and $A_h=\rho_h(A)$, then $A_hN_h=N_hA_h$; thus $U_hA_hU_h^{-1}\in\{N_{\mu_h}\}'$. By Corollary 6.9, there is a $\phi$ in $B(\sigma(N_h))$ such that $U_hA_hU_h^{-1}=M_\phi$. It follows (How?) that $A_h=\phi(N_h)$.

Finally, to show that $\rho_h$ is surjective note that if $B\in W^*(N_h)$, then (use the argument in the preceding paragraph) $B=\psi(N_h)$ for some $\psi$ in $B(\sigma(N_h))$. Extend $\psi$ to $\sigma(N)$ by letting $\psi=0$ on $\sigma(N)\setminus\sigma(N_h)$. Then $\psi(N)\in W^*(N)$ and $\rho_h(\psi(N))=\psi(N_h)=B$. $\blacksquare$

**8.6. Lemma.** *If $e\in\mathcal H$ such that $\mu_e$ is a scalar-valued spectral measure for $N$ and if $\nu$ is a positive measure on $\sigma(N)$ such that $\nu\ll\mu_e$, then there is an $h$ in $\mathcal H_e$ such that $\nu=\mu_h$.*

**Proof.** This proof is just an application of the Radon–Nikodym Theorem once certain identifications are made; namely, $f=[d\nu/d\mu_e]^{1/2}\in L^2(\mu_e)$, so put $h=U_e^{-1}f$. Hence $h\in\mathcal H_e$. For any Borel set $\Delta$, $\nu(\Delta)=\int\chi_\Delta\,d\nu=\int\chi_\Delta ff\,d\mu_e=\langle M_{\chi_\Delta}f,f\rangle=\langle U_e^{-1}M_{\chi_\Delta}f,U_e^{-1}f\rangle=\langle E(\Delta)h,h\rangle=\mu_h(\Delta)$. $\blacksquare$

**8.7. Lemma.** $W^*(N)=\{\phi(N):\phi\in B(\sigma(N))\}$.

**Proof.** Let $\mathcal A=\{\phi(N):\phi\in B(\sigma(N))\}$. Hence $\mathcal A$ is a $*$-algebra and $\mathcal A\subseteq W^*(N)$ by Proposition 8.1. Since $N\in\mathcal A$ it suffices to prove that $\mathcal A$ is WOT closed. Let $\{\phi_i\}$ be a net in $B(\sigma(N))$ such that $\phi_i(N)\to A$ (WOT); so $A\in W^*(N)$. By
