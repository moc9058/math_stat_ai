the variation for $E_{h,f}$. Let $\phi_n=\sum_{k=1}^n\chi_{\Delta_k}\phi$; so $\phi_n$ is bounded, as is $u\phi_n$. Thus

$$
\begin{aligned}
\int |\phi_n|\,d|E_{h,f}|
&=\int |\phi_n|u\,dE_{h,f}\\
&=\left\langle\left(\int |\phi_n|u\,dE\right)h,f\right\rangle\\
&\leq \|f\|\left\|\left(\int |\phi_n|u\,dE\right)h\right\|.
\end{aligned}
$$

But

$$
\begin{aligned}
\left\|\left(\int |\phi_n|u\,dE\right)h\right\|^2
&=\left\langle\left(\int |\phi_n|u\,dE\right)h,
\left(\int |\phi_n|u\,dE\right)h\right\rangle\\
&=\left\langle\left(\int |\phi_n|^2\,dE\right)h,h\right\rangle\\
&=\int |\phi_n|^2\,dE_{h,h}\\
&\leq \int |\phi|^2\,dE_{h,h}.
\end{aligned}
$$

Combining this with the preceding inequality gives that $\int |\phi_n|\,d|E_{h,f}|\leq \|f\|(\int |\phi|^2\,dE_{h,h})^{1/2}$ for all $n$. Letting $n\to\infty$ gives (4.8). Since $\phi_n$ is bounded, $\left\langle(\int\phi_n\,dE)h,f\right\rangle=\int\phi_n\,dE_{h,f}$. If $h\in\mathcal D_\phi$ and $f\in\mathcal H$, then (4.8) and the Lebesgue Dominated Convergence Theorem imply that $\int\phi_n\,dE_{h,f}\to\int\phi\,dE_{h,f}$ as $n\to\infty$. But

$$
\begin{aligned}
\left(\int\phi_n\,dE\right)h
&=\left(\int\phi\,dE\right)E\left(\bigcup_{j=1}^n\Delta_j\right)h\\
&=E\left(\bigcup_{j=1}^n\Delta_j\right)\left(\int\phi\,dE\right)h.
\end{aligned}
$$

Since $E(\bigcup_{j=1}^n\Delta_j)\to E(X)=1$ (SOT) as $n\to\infty$, $\left\langle(\int\phi_n\,dE)h,f\right\rangle\to\left\langle(\int\phi\,dE)h,f\right\rangle$ as $n\to\infty$. This proves (4.9). ■

Note that as a consequence of (4.7) $\operatorname{dom}N_\phi$ and the definition of $N_\phi$ do not depend on the choice of the sets $\{\Delta_n\}$, as would seem to be the case from (4.5) and (4.6). Also, by (4.7.a), $E(\Delta)h\in\operatorname{dom}N_\phi$ if $h\in\operatorname{dom}N_\phi$.

**4.10. Theorem.** *If $(X,\Omega)$ is a measurable space, $\mathcal H$ is a Hilbert space, and $E$ is a spectral measure for $(X,\Omega,\mathcal H)$, let $\Phi(X,\Omega)$ be the algebra of all $\Omega$-measurable functions $\phi:X\to\mathbb C$ and define $\rho:\Phi(X,\Omega)\to\mathcal C(\mathcal H)$ by $\rho(\phi)=\int\phi\,dE$. Then for $\phi,\psi$ in $\Phi(X,\Omega)$:*

(a) $\rho(\phi)^*=\rho(\overline{\phi})$;

(b) $\rho(\phi\psi)\supseteq\rho(\phi)\rho(\psi)$ and $\operatorname{dom}(\rho(\phi)\rho(\psi))=\mathcal D_\psi\cap\mathcal D_{\phi\psi}$;
