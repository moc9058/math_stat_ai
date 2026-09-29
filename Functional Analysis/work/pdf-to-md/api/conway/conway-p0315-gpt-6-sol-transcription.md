$\|\phi f\|\leq\|\phi\|_\infty\|f\|$. Let $M_\phi:L^2(\mu;\mathcal H_n)\to L^2(\mu;\mathcal H_n)$ be defined by $M_\phi f=\phi f$. Combined with the preceding remarks, the following result can be shown to hold. (The proof is left to the reader.)

**10.18. Proposition.** *If $N$ is multiplication by $z$ on $L^2(\mu;\mathcal H_n)$, then*

$$
\{N\}'=\{M_\phi:\phi\in L^\infty(\mu;\mathcal B(\mathcal H_n))\}.
$$

*Also, $\|M_\phi\|=\|\phi\|_\infty$ for every $\phi$ in $L^\infty(\mu;\mathcal B(\mathcal H_n))$.*

The next lemma is a consequence of Proposition 6.10 and the fact that unitarily equivalent normal operators have mutually absolutely continuous scalar-valued spectral measures.

**10.19. Lemma.** *If $N_1$ and $N_2$ are normal operators with mutually singular scalar spectral measures and $XN_1=N_2X$, then $X=0$.*

Using the observation made prior to Corollary 6.8, the preceding lemma implies that $\{N_1\oplus N_2\}'=\{N_1\}'\oplus\{N_2\}'$ whenever $N_1$ and $N_2$ are as in the lemma.

The next theorem of this section can be proved by piecing together Theorem 10.16 and the remaining results of this section. The details are left to the reader.

**10.20. Theorem.** *If $N$ is a normal operator on $\mathcal H$, there are mutually singular measures $\mu_\infty,\mu_1,\mu_2,\ldots$ and an isomorphism*

$$
U:\mathcal H\to L^2(\mu_\infty;\mathcal H_\infty)\oplus L^2(\mu_1)\oplus L^2(\mu_2;\mathcal H_2)\oplus\cdots
$$

*such that*

$$
UNU^{-1}=N_\infty\oplus N_1\oplus N_2\oplus\cdots
$$

*where $N_n=$ multiplication by $z$ on $L^2(\mu_n;\mathcal H_n)$. Also,*

$$
\begin{aligned}
\{N_\infty\oplus N_1\oplus N_2\oplus\cdots\}'
={}&L^\infty(\mu_\infty;\mathcal B(\mathcal H_\infty))\oplus L^\infty(\mu_1)\\
&\oplus L^\infty(\mu_2;\mathcal B(\mathcal H_2))\oplus\cdots.
\end{aligned}
$$

Using the notation of the preceding theorem, if $\mu$ is a scalar-valued spectral measure for $N$, then there are pairwise disjoint Borel sets $\Delta_\infty,\Delta_1,\ldots$ such that $[\mu_n]=[\mu|_{\Delta_n}]$. Define a function $m_N:\mathbb C\to\{0,1,\ldots,\infty\}$ by letting $m_N=\infty\chi_{\Delta_\infty}+\chi_{\Delta_1}+2\chi_{\Delta_2}+\cdots$. As it stands the definition of $m_N$ depends on the choice of the sets $\{\Delta_n\}$ as well as $N$. However, any two choices of the sets $\{\Delta_n\}$ differ from one another by sets of $\mu$-measure zero. The function $m_N$ is called the *multiplicity function* for $N$. Note that $m_N$ is a Borel function.

If $m:\mathbb C\to\{\infty,0,1,2,\ldots\}$ is a Borel function and $\mu$ is a compactly supported measure such that $\mu(\{z:m(z)=0\})=0$, let $\Delta_n=\{z:m(z)=n\}$, $n=\infty,1,2,\ldots$. If $N_n=N_{\mu|_{\Delta_n}}$, then $N=N_\infty^{(\infty)}\oplus N_1\oplus N_2^{(2)}\oplus\cdots$ is a normal operator whose spectral measure is $\mu$ and whose multiplicity function agrees with $m$ a.e. $[\mu]$.
