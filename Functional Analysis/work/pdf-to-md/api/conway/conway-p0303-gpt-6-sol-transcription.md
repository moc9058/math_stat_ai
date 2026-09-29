(8.5) $\phi_i(N_h)\to A|_{\mathcal H_h}$ (WOT) for any $h$ in $\mathcal H$. Also, by Lemma 8.5, for every $h$ in $\mathcal H$ there is a $\phi_h$ in $B(\mathbb C)$ such that $A|_{\mathcal H_h}=\phi_h(N_h)$. Fix a separating vector $e$ for $W^*(N)$; hence $\mu_e$ is a scalar-valued spectral measure for $N$.

If $h\in\mathcal H$, then the fact that $\phi_i(N_h)\to\phi_h(N_h)$ (WOT) implies $\phi_i\to\phi_h$ weak* in $L^\infty(\mu_h)$. Also, $\phi_i\to\phi_e$ weak* in $L^\infty(\mu_e)$. But $\mu_h\ll\mu_e$ so that $d\mu_h/d\mu_e\in L^1(\mu_e)$; hence for any Borel set $\Delta$

$$
\int_\Delta \phi_i\,d\mu_h
=\int_\Delta \phi_i\frac{d\mu_h}{d\mu_e}\,d\mu_e
\to\int_\Delta \phi_e\,d\mu_h.
$$

But also

$$
\int_\Delta \phi_i\,d\mu_h\to\int_\Delta \phi_h\,d\mu_h.
$$

So $0=\int_\Delta(\phi_e-\phi_h)\,d\mu_h$ for every Borel set $\Delta$. Therefore $\phi_h=\phi_e$ a.e. $[\mu_h]$. But if $g\in\mathcal H_h$, then $\langle\phi_h(N_h)g,g\rangle=\langle\phi_h(N)g,g\rangle=\int\phi_h\,d\mu_g=\int\phi_e\,d\mu_g$ since $\mu_g\ll\mu_h$. Thus $\langle\phi_h(N_h)g,g\rangle=\langle\phi_e(N_h)g,g\rangle$; that is, $\phi_h(N_h)=\phi_e(N_h)$. In particular, $Ah=\phi_h(N_h)h=\phi_e(N_h)h=\phi_e(N)h$. Since $h$ was arbitrary, $A=\phi_e(N)$. ■

**8.8. Corollary.** *If $\rho_h:W^*(N)\to W^*(N_h)$ is the $*$-epimorphism of Lemma 8.5, then $\ker\rho_h=\{\phi(N):\phi=0\text{ a.e. }[\mu_h]\}$.*

**8.9. Theorem.** *If $N$ is a normal operator and $e\in\mathcal H$, the following statements are equivalent.*

(a) $e$ is a separating vector for $W^*(N)$.

(b) $\mu_e$ is a scalar-valued spectral measure for $N$.

(c) The map $\rho_e:W^*(N)\to W^*(N_e)$ defined in (8.5) is a $*$-isomorphism.

(d) $\{\phi\in B(\sigma(N)):\phi(N)=0\}=\{\phi\in B(\sigma(N)):\phi=0\text{ a.e. }[\mu_e]\}$.

**Proof.** (a)$\Rightarrow$(b): Proposition 8.3.

(b)$\Rightarrow$(c): By Lemma 8.5, $\rho_e$ is a $*$-epimorphism. By Corollary 8.8, $\ker\rho_e=\{\phi(N):\phi=0\text{ a.e. }[\mu_e]\}$. But if $\phi=0$ a.e. $[\mu_e]$, (b) implies that $\phi=0$ off a set $\Delta$ such that $E(\Delta)=0$. Thus $\phi(N)=\int_\Delta\phi\,dE=0$.

(c)$\Rightarrow$(d): Combine (c) with Corollary 8.8.

(d)$\Rightarrow$(a): Suppose $A\in W^*(N)$ and $Ae=0$. By Lemma 8.7, there is a $\phi$ in $B(\sigma(N))$ such that $\phi(N)=A$. Thus, $0=\|Ae\|^2=\langle A^*Ae,e\rangle=\int|\phi|^2\,d\mu_e$. So $\phi=0$ a.e. $[\mu_e]$. By (d), $A=0$. ■

These results can now be combined to yield the final statement of the functional calculus for normal operators.

**8.10. The Functional Calculus for a Normal Operator.** *If $N$ is a normal operator on the separable Hilbert space $\mathcal H$ and $\mu$ is a scalar-valued spectral measure for $N$, then there is a well-defined map $\rho:L^\infty(\mu)\to W^*(N)$ given by the formula $\rho(\phi)=\phi(N)$ such that*
