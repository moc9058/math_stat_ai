$U_{21}U_{11}^{*}f=0$, so $U_{12}^{*}f\in\ker U_{22}$. Hence $f\in U_{12}(\ker U_{22})$. Thus

$$
\mathcal M_1=\ker U_{11}^{*}.
$$

Similarly,

$$
\mathcal M_2=\ker U_{11}.
$$

Until this point we have not used the fact that $N$ is *-cyclic. Equation $(10.7)_{11}$ implies that $U_{11}\in\{N'\}'$. By Theorem 3.4 and Corollary 6.9 this implies that $U_{11}$ is normal. Hence, $\ker U_{11}^{*}=\ker U_{11}$, or $\mathcal M_1=\mathcal M_2$. $\blacksquare$

If the hypothesis in the preceding proposition that $N$ is *-cyclic is deleted, the conclusion is no longer valid. For example, let $N$ and $A$ be the identities on separable infinite dimensional spaces and let $B$ be the identity on a finite dimensional space. Then $N\oplus A\cong N\oplus B$, but $A$ and $B$ are not equivalent. However, the requirement that $N$ be *-cyclic can be replaced by another, even when $N$, $A$, and $B$ are not assumed to be normal. For the details see Kadison and Singer [1957].

The proof of Theorem 10.1(b) is now a straightforward argument as outlined before the statement of Proposition 10.6. The details are left to the reader.

If $\mu$ and $\nu$ are measures and $\nu\ll\mu$, then there is a Borel set $\Delta$ such that $[\nu]=[\mu|_\Delta]$. Using this fact, Theorem 10.1 can be restated as follows.

**10.12. Corollary.** (a) If $N$ is a normal operator with scalar-valued spectral measure $\mu$, then there is a decreasing sequence $\{\Delta_n\}$ of Borel subsets of $\sigma(N)$ such that $\Delta_1=\sigma(N)$ and

$$
N\cong N_\mu\oplus N_{\mu|_{\Delta_2}}\oplus N_{\mu|_{\Delta_3}}\oplus\cdots.
$$

(b) If $M$ is another normal operator with scalar-valued spectral measure $\nu$ and if $\{\Sigma_n\}$ is a decreasing sequence of Borel subsets of $\sigma(M)$ such that $M\cong N_\nu\oplus N_{\nu|_{\Sigma_2}}\oplus N_{\nu|_{\Sigma_3}}\oplus\cdots$, then $N\cong M$ if and only if (i) $[\mu]=[\nu]$ and (ii) $\mu(\Delta_n\setminus\Sigma_n)=0=\mu(\Sigma_n\setminus\Delta_n)$ for all $n$.

**10.13. Example.** Let $\mu$ be Lebesgue measure on $[0,1]$ and let $\mu_n$ be Lebesgue measure on $[1/(n+1),1/n]$ for $n\geqslant1$. (So $\mu=\sum\mu_n$.) Let $N=N_{\mu_1}\oplus N_{\mu_2}^{(2)}\oplus N_{\mu_3}^{(3)}\oplus\cdots$. The direct sum decomposition of $N$ that appears in Corollary 10.12 is obtained by letting $\Delta_n=[0,1/n]$, $n\geqslant1$. Then $N\cong N_\mu\oplus N_{\mu|_{\Delta_2}}\oplus N_{\mu|_{\Delta_3}}\oplus\cdots$.

What does Theorem 10.1 say for normal operators on a finite dimensional space? If $\dim\mathcal H<\infty$, there is an orthonormal basis $\{e_n\}$ for $\mathcal H$ consisting of eigenvectors for $N$. Observe that $N$ is *-cyclic if and only if each eigenvalue has multiplicity 1. So each summand that appears in (10.2) must operate on a subspace of $\mathcal H$ that contains only one basis element $e_n$ per eigenvalue. Moreover, since $\mu_1$ is a scalar-valued spectral measure for $N$, it must be that the first summand in (10.2) contains one basis element for each eigenvalue
