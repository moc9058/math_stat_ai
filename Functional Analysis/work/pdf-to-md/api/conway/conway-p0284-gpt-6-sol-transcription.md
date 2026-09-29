**Proof.** It is easy to see that $C^*(A)$ and $\{p(A):p=\text{a polynomial}\}$ are separable subalgebras of $\mathcal{B}(\mathcal{H})$. Now use (3.2). ■

Let $\mu$ be a compactly supported measure on $\mathbb{C}$ and let $N_\mu$ be defined on $L^2(\mu)$ as in Example 2.5. If $K=\operatorname{support}\mu$, then $C^*(N_\mu)=\{M_u:u\in C(K)\}$. Since $C(K)$ is dense in $L^2(\mu)$, it follows that $1$ is a star-cyclic vector for $N_\mu$. The converse of this is also true.

**3.4. Theorem.** *A normal operator $N$ is star-cyclic if and only if $N$ is unitarily equivalent to $N_\mu$ for some compactly supported measure $\mu$ on $\mathbb{C}$. If $e_0$ is a star-cyclic vector for $N$, then $\mu$ can be chosen such that there is an isomorphism $V:\mathcal{H}\to L^2(\mu)$ with $Ve_0=1$ and $VNV^{-1}=N_\mu$. Under these conditions, $V$ is unique.*

**Proof.** If $N\cong N_\mu$, then we have already seen that $N$ is star-cyclic. So suppose that $N$ has a star-cyclic vector $e_0$. If $E$ is the spectral measure for $N$, put $\mu(\Delta)=\|E(\Delta)e_0\|^2=\langle E(\Delta)e_0,e_0\rangle$ for every Borel subset $\Delta$ of $\mathbb{C}$ (see Lemma 1.9). Let $K=\operatorname{support}\mu$.

If $\phi\in B(K)$, then (2.4) implies

$$
\begin{aligned}
\|\phi(N)e_0\|^2
&=\langle\phi(N)e_0,\phi(N)e_0\rangle\\
&=\langle|\phi|^2(N)e_0,e_0\rangle\\
&=\int|\phi(z)|^2\,d\langle E(z)e_0,e_0\rangle\\
&=\int|\phi|^2\,d\mu.
\end{aligned}
$$

So if $B(K)$ is considered as a submanifold of $L^2(\mu)$, $U\phi=\phi(N)e_0$ defines an isometry from $B(K)$ onto $\{\phi(N)e_0:\phi\in B(K)\}$. But $e_0$ is a star-cyclic vector, so the range of $U$ is dense in $\mathcal{H}$. Hence $U$ extends to an isomorphism $U:L^2(\mu)\to\mathcal{H}$.

If $\phi\in B(K)$, then $UN_\mu U^{-1}(\phi(N)e_0)=UN_\mu(\phi)=U(z\phi)=N\phi(N)e_0$. Hence $UN_\mu U^{-1}=N$ on $\{\phi(N)e_0:\phi\in B(K)\}$, which is dense in $\mathcal{H}$. So $UN_\mu U^{-1}=N$. Let $V=U^{-1}$.

The proof of the uniqueness statement is an exercise. ■

Any theorem about the operators $N_\mu$ is a theorem about star-cyclic normal operators. With this in mind, the next theorem gives a complete unitary invariant for star-cyclic normal operators. But first, a definition.

**3.5. Definition.** Two measures, $\mu_1$ and $\mu_2$, are *mutually absolutely continuous* if they have the same sets of measure zero; that is, $\mu_1(\Delta)=0$ if and only if $\mu_2(\Delta)=0$. This will be denoted by $[\mu_1]=[\mu_2]$. (The more standard notation in the literature is $\mu_1\equiv\mu_2$, but this seems insufficient.) If $[\mu_1]=[\mu_2]$, then the Radon–Nikodym derivatives $d\mu_1/d\mu_2$ and $d\mu_2/d\mu_1$ are well defined. Say
