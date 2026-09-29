**2.5. Example.** If $\mu$ is a regular Borel measure on $\mathbb C$ with compact support $K$, define $N_\mu$ on $L^2(\mu)$ by $N_\mu f=zf$ for each $f$ in $L^2(\mu)$. It is easy to check that $N_\mu^*f=\bar zf$, and, hence, $N_\mu$ is normal.

(a) $\sigma(N_\mu)=K=\operatorname{support}$ of $\mu$. (Exercise.)

(b) If, for a bounded Borel function $\phi$, we define $M_\phi$ on $L^2(\mu)$ by $M_\phi f=\phi f$, then $\phi(N_\mu)=M_\phi$.

Indeed, this is an easy application of the uniqueness part of (2.3).

(c) If $E$ is the spectral measure for $N_\mu$, then $E(\Delta)=M_{\chi_\Delta}$.

Just note that $E(\Delta)=\chi_\Delta(N_\mu)$.

**2.6. Example.** Let $(X,\Omega,\mu)$ be any $\sigma$-finite measure space and put $\mathcal H=L^2(X,\Omega,\mu)$. For $\phi$ in $L^\infty(\mu)\equiv L^\infty(X,\Omega,\mu)$, define $M_\phi$ on $\mathcal H$ by $M_\phi f=\phi f$.

(a) $M_\phi$ is normal and $M_\phi^*=M_{\bar\phi}$ (II.2.8).

(b) $\phi\mapsto M_\phi$ is a representation of $L^\infty(\mu)$ (VIII.5.4).

(c) If $\phi\in L^\infty(\mu)$, $\|\phi\|_\infty=\|M_\phi\|$ (II.1.5).

(d) Define the *essential range* of $\phi$ by
$$
\operatorname{ess-ran}(\phi)\equiv
\bigcap\{\operatorname{cl}(\phi(\Delta)):\Delta\in\Omega
\text{ and }\mu(X\setminus\Delta)=0\}.
$$

Then $\sigma(M_\phi)=\operatorname{ess-ran}(\phi)$. (This appears as Exercise VII.3.3, but a proof is given here.)

First assume that $\lambda\notin\operatorname{ess-ran}(\phi)$. So there is a set $\Delta$ in $\Omega$ with $\mu(X\setminus\Delta)=0$ and $\lambda$ not in $\operatorname{cl}(\phi(\Delta))$; thus there is a $\delta>0$ with $|\phi(x)-\lambda|\geq\delta$ for all $x$ in $\Delta$. If $\psi=(\phi-\lambda)^{-1}$, $\psi\in L^\infty(\mu)$ and $M_\psi=(M_\phi-\lambda)^{-1}$.

Conversely, assume $\lambda\in\operatorname{ess-ran}(\phi)$. It follows that for every integer $n$ there is a set $\Delta_n$ in $\Omega$ such that $0<\mu(\Delta_n)<\infty$ and $|\phi(x)-\lambda|<1/n$ for all $x$ in $\Delta_n$. Put $f_n=(\mu(\Delta_n))^{-1/2}\chi_{\Delta_n}$; so $f_n\in L^2(\mu)$ and $\|f_n\|_2=1$. However, $\|(M_\phi-\lambda)f_n\|_2^2=(\mu(\Delta_n))^{-1}\int_{\Delta_n}|\phi-\lambda|^2\,d\mu\leq 1/n^2$, showing that $\lambda\in\sigma_{ap}(M_\phi)$.

(e) If $E$ is the spectral measure for $M_\phi$ [so $E$ is defined on the Borel subsets of $\sigma(M_\phi)=\operatorname{ess-ran}(\phi)\subseteq\mathbb C$], then for every Borel subset $\Delta$ of $\sigma(M_\phi)$, $E(\Delta)=M_{\chi_{\phi^{-1}(\Delta)}}$.

**2.7. Proposition.** *If for $k\geq 1$, $N_k$ is a normal operator on $\mathcal H_k$ with $\sup_k\|N_k\|<\infty$, $E_k$ is the spectral measure for $N_k$, and if $N=\bigoplus_{k=1}^{\infty}N_k$ on $\mathcal H=\bigoplus_{k=1}^{\infty}\mathcal H_k$, then:*

(a) $\sigma(N)=\operatorname{cl}\left[\bigcup_{k=1}^{\infty}\sigma(N_k)\right]$;

(b) *if $E$ is the spectral measure for $N$, $E(\Delta)=\bigoplus_{k=1}^{\infty}E_k(\Delta\cap\sigma(N_k))$ for every Borel subset $\Delta$ of $\sigma(N)$.*

**Proof.** Exercise.

A historical account of the spectral theorem is an enormous undertaking
