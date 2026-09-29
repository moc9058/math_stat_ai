for $N$. Thus, if $\sigma(N)=\{\lambda_1,\lambda_2,\ldots,\lambda_n\}$, where $\lambda_i\ne\lambda_j$ for $i\ne j$, then (10.2) becomes

$$
N\cong D_1\oplus D_2\oplus\cdots\oplus D_m, \tag{10.14}
$$

where $D_1=\operatorname{diag}(\lambda_1,\lambda_2,\ldots,\lambda_n)$ and, for $k\geq 2$, $D_k$ is a diagonalizable operator whose diagonal consists of one, and only one, of each of the eigenvalues of $N$ having multiplicity at least $k$.

There is another decomposition for normal operators that furnishes a complete set of unitary invariants and has a connection with the concept of multiplicity. For normal operators on a finite dimensional space, this decomposition takes on the following form.

Let $\Lambda_k=$ the eigenvalues of $N$ having multiplicity $k$. So for $\lambda$ in $\Lambda_k$, $\dim\ker(N-\lambda)=k$. If $\Lambda_k=\{\lambda_j^{(k)}:1\leq j\leq m_k\}$, let $N_k$ be the diagonalizable operator on a $km_k$ dimensional space whose diagonal contains each $\lambda_j^{(k)}$ repeated $k$ times. So $N\cong N_1\oplus N_2\oplus\cdots\oplus N_p$, if $\sigma(N)=\Lambda_1\cup\cdots\cup\Lambda_p$. Now $\sigma(N_k)=\Lambda_k$ and each eigenvalue of $N_k$ has multiplicity $k$. Thus $N_k\cong A_k^{(k)}$, where $A_k$ is a diagonalizable operator on an $m_k$ dimensional space with $\sigma(A_k)=\Lambda_k$. Thus

$$
N\cong A_1\oplus A_2^{(2)}\oplus\cdots\oplus A_p^{(p)}, \tag{10.15}
$$

and $\sigma(A_i)\cap\sigma(A_j)=\square$ for $i\ne j$.

Now the big advantage of the decomposition (10.15) is that it permits a discussion of $\{N\}'$. Because the spectra of the operators $A_k$ are disjoint,

$$
\{N\}'=\{N_1\}'\oplus\{N_2\}'\oplus\cdots\oplus\{N_p\}'.
$$

(Why?) If $\mathcal H_j^{(k)}=\ker(N-\lambda_j^{(k)})$, then $\dim\mathcal H_j^{(k)}=k$ and $\bigoplus_{j=1}^{m_k}\mathcal H_j^{(k)}=$ the domain of $N_k$. Since $\lambda_i^{(k)}\ne\lambda_j^{(k)}$ for $i\ne j$,

$$
\{N_k\}'=\mathcal B(\mathcal H_1^{(k)})\oplus\cdots\oplus\mathcal B(\mathcal H_{m_k}^{(k)}),
$$

and each $\mathcal B(\mathcal H_j^{(k)})$ is isomorphic to the $k\times k$ matrices.

The decomposition of an arbitrary normal operator that is analogous to decomposition (10.15) for finite dimensional normal operators is contained in the next result. The corresponding discussion of the commutant will follow this theorem.

**10.16. Theorem.** *If $N$ is a normal operator, then there are mutually singular measures $\mu_\infty,\mu_1,\mu_2,\ldots$ (some of which may be zero) such that*

$$
N\cong N_{\mu_\infty}^{(\infty)}\oplus N_{\mu_1}\oplus N_{\mu_2}^{(2)}\oplus\cdots.
$$

*If $M$ is another normal operator with corresponding measures $\nu_\infty,\nu_1,\nu_2,\ldots$, then $N\cong M$ if and only if $[\mu_n]=[\nu_n]$ for $1\leq n\leq\infty$.*

**Proof.** Let $\mu$ be a scalar-valued spectral measure for $N$ and let $\{\Delta_n\}$ be the sequence of Borel subsets of $\sigma(N)$ obtained in Corollary 10.12. Put $\Sigma_\infty=\bigcap_{n=1}^{\infty}\Delta_n$ and $\Sigma_n=\Delta_n\setminus\Delta_{n+1}$ for $1\leq n<\infty$; let $\mu_n=\mu|_{\Sigma_n}$, $1\leq n\leq\infty$. Put
