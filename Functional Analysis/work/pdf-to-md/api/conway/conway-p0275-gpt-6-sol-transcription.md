Representation Theorem for linear functionals on $C(X)$. We wish to extend $\rho$ to a representation $\tilde{\rho}:B(X)\to\mathcal{B}(\mathcal{H})$, where $B(X)$ is the $C^*$-algebra of bounded Borel functions. The measure $E$ of a Borel set $\Delta$ is then defined by letting $E(\Delta)=\tilde{\rho}(\chi_\Delta)$. In fact, it is possible to give a proof of the theorem patterned on the proof of the Riesz Representation Theorem. Here, however, the proof will use the Riesz Representation Theorem to simplify the technical details.

If $g,h\in\mathcal{H}$, then $u\mapsto\langle\rho(u)g,h\rangle$ is a linear functional on $C(X)$ with norm $\leq\|g\|\|h\|$. Hence there is a unique measure, $\mu_{g,h}$ in $M(X)$ such that

$$
\langle\rho(u)g,h\rangle=\int u\,d\mu_{g,h}. \tag{1.15}
$$

for all $u$ in $C(X)$. It is easy to verify that the map $(g,h)\mapsto\mu_{g,h}$ is sesquilinear (use uniqueness) and $\|\mu_{g,h}\|\leq\|g\|\|h\|$. Now fix $\phi$ in $B(X)$ and define $[g,h]=\int\phi\,d\mu_{g,h}$. Then $[\cdot,\cdot]$ is a sesquilinear form and $|[g,h]|\leq\|\phi\|\|g\|\|h\|$. Hence there is a unique bounded operator $A$ such that $[g,h]=\langle Ag,h\rangle$ and $\|A\|\leq\|\phi\|$ (II.2.2). Denote the operator $A$ by $\tilde{\rho}(\phi)$. So $\tilde{\rho}:B(X)\to\mathcal{B}(\mathcal{H})$ is a well-defined function, $\|\tilde{\rho}(\phi)\|\leq\|\phi\|$, and for all $g,h$ in $\mathcal{H}$,

$$
\langle\tilde{\rho}(\phi)g,h\rangle=\int\phi\,d\mu_{g,h}. \tag{1.16}
$$

**1.17. Claim.** $\tilde{\rho}:B(X)\to\mathcal{B}(\mathcal{H})$ is a representation and $\tilde{\rho}|_{C(X)}=\rho$.

The fact that $\tilde{\rho}(u)=\rho(u)$ whenever $u\in C(X)$ follows immediately from (1.15) and (1.16). If $\phi\in B(X)$, consider $\phi$ as an element of $M(X)^*$ $(=C(X)^{**})$; that is, $\phi$ corresponds to the linear functional $\mu\mapsto\int\phi\,d\mu$. By Proposition V.4.1, $\{u\in C(X):\|u\|\leq\|\phi\|\}$ is $\sigma(M(X)^*,M(X))$ dense in $\{L\in M(X)^*:\|L\|\leq\|\phi\|\}$. Thus there is a net $\{u_i\}$ in $C(X)$ such that $\|u_i\|\leq\|\phi\|$ for all $u_i$ and $\int u_i\,d\mu\to\int\phi\,d\mu$ for every $\mu$ in $M(X)$. If $\psi\in B(X)$, then $\psi\mu\in M(X)$ whenever $\mu\in M(X)$. Hence $\int u_i\psi\,d\mu\to\int\phi\psi\,d\mu$ for every $\psi$ in $B(X)$ and $\mu$ in $M(X)$. By (1.16), $\tilde{\rho}(u_i\psi)\to\tilde{\rho}(\phi\psi)$ (WOT) for all $\psi$ in $B(X)$. In particular, if $\psi\in C(X)$, then $\tilde{\rho}(\phi\psi)=\operatorname{WOT}-\lim\tilde{\rho}(u_i\psi)=\operatorname{WOT}-\lim\rho(u_i)\rho(\psi)=\tilde{\rho}(\phi)\rho(\psi)$. That is,

$$
\tilde{\rho}(\phi\psi)=\tilde{\rho}(\phi)\rho(\psi)
$$

whenever $\phi\in B(X)$ and $\psi\in C(X)$. Hence $\tilde{\rho}(u_i\psi)=\rho(u_i)\tilde{\rho}(\psi)$ for any $\psi$ in $B(X)$ and for all $u_i$. Since $\tilde{\rho}(u_i)\to\tilde{\rho}(\phi)$ (WOT) and $\tilde{\rho}(u_i\psi)\to\tilde{\rho}(\phi\psi)$ (WOT), this implies that

$$
\tilde{\rho}(\phi\psi)=\tilde{\rho}(\phi)\tilde{\rho}(\psi)
$$

whenever $\phi,\psi\in B(X)$.

The proof that $\tilde{\rho}$ is linear is immediate by (1.16). To see that $\tilde{\rho}(\phi)^*=\tilde{\rho}(\bar{\phi})$. Let $\{u_i\}$ be the net obtained in the preceding paragraph. If $\mu\in M(X)$, let $\bar{\mu}$ be the measure defined by $\bar{\mu}(\Delta)=\overline{\mu(\Delta)}$. Then $\rho(u_i)\to\tilde{\rho}(\phi)$ (WOT) and so $\rho(u_i)^*\to\tilde{\rho}(\phi)^*$ (WOT). But $\int\bar{u}_i\,d\mu=\overline{\int u_i\,d\bar{\mu}}\to\overline{\int\phi\,d\bar{\mu}}=\int\bar{\phi}\,d\mu$ for every measure
