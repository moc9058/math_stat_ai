Now let $A\in\mathcal{B}(\mathcal{H})$ such that $AN\subseteq NA$ and $AN^*\subseteq N^*A$. Thus $A(1+N^*N)\subseteq(1+N^*N)A$. It follows that $AB=BA$. By the Spectral Theorem for bounded operators, $A$ commutes with the spectral projections of $B$. In particular, each $\mathcal{H}_n$ reduces $A$ and if $A_n\equiv A|_{\mathcal{H}_n}$, then $A_nN_n=N_nA_n$. Hence $A_nE_n(\Delta)=E_n(\Delta)A_n$ for every Borel set $\Delta$ contained in $\Delta_n$. It follows that $AE(\Delta)=E(\Delta)A$ for every Borel set $\Delta$. The remaining details of the proof of (d) are left to the reader. $\blacksquare$

The Fuglede–Putnam Theorem holds for unbounded normal operators (Exercise 8), so that the hypothesis in part (d) of the Spectral Theorem can be weakened to $AN\subseteq NA$.

**4.16. Definition.** If $N$ is a normal operator on $\mathcal{H}$, then a vector $e_0$ is a *star-cyclic* vector for $N$ if for all non-negative integers $k$ and $l$, $e_0\in\operatorname{dom}(N^{*k}N^l)$ and $\mathcal{H}=\bigvee\{N^{*k}N^le_0:k,l\geqslant0\}$.

**4.17. Example.** Let $\mu$ be a finite measure on $\mathbb{C}$ such that every polynomial in $z$ and $\bar z$ belongs to $L^2(\mu)$ and the collection of such polynomials is dense in $L^2(\mu)$. Let $\mathcal{D}_\mu=\{f\in L^2(\mu):zf\in L^2(\mu)\}$ and define $N_\mu f=zf$ for $f$ in $\mathcal{D}_\mu$. Then $N_\mu$ is a normal operator and $1$ is a star-cyclic vector for $N_\mu$.

Note that $d\mu(z)=e^{-|z|}d\operatorname{Area}(z)$ is a measure satisfying the conditions of (4.17).

**4.18. Theorem.** *If $N$ is a normal operator on $\mathcal{H}$ with a star-cyclic vector $e_0$, then there is a finite measure $\mu$ on $\mathbb{C}$ such that every polynomial in $z$ and $\bar z$ belongs to $L^2(\mu)$ and there is an isomorphism $W:\mathcal{H}\to L^2(\mu)$ such that $We_0=1$ and $WNW^{-1}=N_\mu$.*

The proof of Theorem 4.18 can be accomplished by using the Spectral Theorem to write $N$ as the direct sum (in the sense of Lemma 4.4) of bounded normal operators $N_n$ on $\mathcal{H}_n$ with spectral measures that are pairwise mutually singular and such that each $N_n$ has $e_n$, the projection of $e_0$ onto $\mathcal{H}_n$, as a *-cyclic vector. If $\mu_n=E_{e_n,e_n}$, then (IX.3.4) implies that there is an isomorphism $W_n:\mathcal{H}_n\to L^2(\mu_n)$ such that $W_nN_nW_n^{-1}=N_{\mu_n}$. If $W=\bigoplus_1^\infty W_n$, then $W$ is an isomorphism of $\mathcal{H}$ onto $\bigoplus_1^\infty L^2(\mu_n)$. But the fact that the measures $\mu_n$ are pairwise mutually singular implies that $\bigoplus_1^\infty L^2(\mu_n)=L^2(\mu)$, where $\mu=\sum_{n=1}^\infty\mu_n=E_{e_0,e_0}$. Clearly $WNW^{-1}=N_\mu$.

**4.19. Theorem.** *If $N$ is a normal operator on the separable Hilbert space $\mathcal{H}$, then there is a $\sigma$-finite measure space $(X,\Omega,\mu)$ and an $\Omega$-measurable function $\phi$ such that $N$ is unitarily equivalent to $M_\phi$ on $L^2(\mu)$.*

The proof of Theorem 4.19 is only sketched. Write $N$ as the (unbounded) direct sum of bounded normal operators $\{N_n\}$. By Theorem IX.4.6, there is a $\sigma$-finite measure space $(X_n,\Omega_n,\mu_n)$ and a bounded $\Omega_n$-measurable function
