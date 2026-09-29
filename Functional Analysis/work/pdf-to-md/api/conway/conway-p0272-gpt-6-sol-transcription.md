Then $d_s$ and $d_w$ are metrics on $\mathcal B(\mathcal H)$. It is left as an exercise to show that $d_s$ and $d_w$ define the SOT and WOT on bounded subsets of $\mathcal B(\mathcal H)$. ■

**1.4. Example.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space. If $\phi\in L^\infty(\mu)$, let $M_\phi$ be the multiplication operator on $L^2(\mu)$. Then a net $\{\phi_i\}$ in $L^\infty(\mu)$ converges weak* to $\phi$ if and only if $M_{\phi_i}\to M_\phi$ (WOT). In fact, if $f,g\in L^2(\mu)$ and $\phi_i\to\phi$ weak* in $L^\infty(\mu)$, then $\langle M_{\phi_i}f,g\rangle=\int\phi_i f\bar g\,d\mu\to\int\phi f\bar g\,d\mu=\langle M_\phi f,g\rangle$ since $f\bar g\in L^1(\mu)$. Conversely, if $M_{\phi_i}\to M_\phi$ (WOT) and $f\in L^1(\mu)$, then $f=g_1\bar g_2$, where $g_1,g_2\in L^2(\mu)$. (Why?) So $\int\phi_i f\,d\mu=\langle M_{\phi_i}g_1,g_2\rangle\to\langle M_\phi g_1,g_2\rangle=\int\phi f\,d\mu$.

**1.5. Example.** If $\{E_n\}$ is a sequence of pairwise orthogonal projections on $\mathcal H$, then $\sum_1^\infty E_n$ converges (SOT) to the projection of $\mathcal H$ onto $\bigvee\{E_n(\mathcal H):n\geq 1\}$.

In light of (1.5), a spectral measure for $(X,\Omega,\mathcal H)$ could be defined as a SOT-countably additive projection-valued measure.

**1.6. Example.** Let $X$ be a compact set, $\Omega=$ the Borel subsets of $X$, $\mu=$ a measure on $\Omega$, and $\mathcal H=L^2(\mu)$. For $\Delta$ in $\Omega$, let $E(\Delta)=$ multiplication by $\chi_\Delta$, the characteristic function of $\Delta$. $E$ is a spectral measure for $(X,\Omega,\mathcal H)$.

**1.7. Example.** If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$, the *inflation*, $E^{(n)}$, of $E$, defined by $E^{(n)}(\Delta)=E(\Delta)^{(n)}$, is a spectral measure for $(X,\Omega,\mathcal H^{(n)})$.

**1.8. Example.** Let $X$ be any set, $\Omega=$ all the subsets of $X$, $\mathcal H=$ any separable Hilbert space, and fix a sequence $\{x_n\}$ in $X$. If $\{e_1,e_2,\ldots\}$ is some orthonormal basis for $\mathcal H$, define $E(\Delta)=$ the projection onto $\bigvee\{e_n:x_n\in\Delta\}$. $E$ is a spectral measure for $(X,\Omega,\mathcal H)$.

The next lemma is useful in studying spectral measures as it allows us to prove things about spectral measures from known facts about complex-valued measures.

**1.9. Lemma.** *If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$ and $g,h\in\mathcal H$, then*

$$
E_{g,h}(\Delta)\equiv\langle E(\Delta)g,h\rangle
$$

*defines a countably additive measure on $\Omega$ with total variation $\leq\|g\|\|h\|$.*

**Proof.** That $\mu=E_{g,h}$, as defined above, is a countably additive measure is left for the reader to verify. If $\Delta_1,\ldots,\Delta_n$ are pairwise disjoint sets in $\Omega$, let $\alpha_j\in\mathbb C$ such that $|\alpha_j|=1$ and $|\langle E(\Delta_j)g,h\rangle|=\alpha_j\langle E(\Delta_j)g,h\rangle$. So
$$
\sum_j|\mu(\Delta_j)|
=\sum_j\alpha_j\langle E(\Delta_j)g,h\rangle
=\left\langle\sum_j E(\Delta_j)\alpha_jg,h\right\rangle
\leq\left\|\sum_j E(\Delta_j)\alpha_jg\right\|\|h\|.
$$
Now $\{E(\Delta_j)\alpha_jg:1\leq j\leq n\}$ is a finite sequence of pairwise orthogonal vectors so that
$$
\left\|\sum_j E(\Delta_j)\alpha_jg\right\|^2
=\sum_j\|E(\Delta_j)g\|^2
=\left\|E\left(\bigcup_{j=1}^n\Delta_j\right)g\right\|^2
\leq\|g\|^2;
$$
hence $\sum_j|\mu(\Delta_j)|\leq\|g\|\|h\|$. Thus $\|\mu\|\leq\|g\|\|h\|$. ■

It is possible to use spectral measures to define representations. The next
