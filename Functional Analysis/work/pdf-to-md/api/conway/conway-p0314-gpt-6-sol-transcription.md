$\nu_n=\mu|_{\Delta_n}$, $1\leq n<\infty$. Now $\Delta_n=\Sigma_\infty\cup(\Delta_n\setminus\Delta_{n+1})\cup(\Delta_{n+1}\setminus\Delta_{n+2})\cup\cdots=\Sigma_\infty\cup\Sigma_n\cup\Sigma_{n+1}\cup\cdots$. Hence $\nu_n=\mu_\infty+\mu_n+\mu_{n+1}+\cdots$ and the measures $\mu_\infty,\mu_n,\mu_{n+1},\ldots$ are pairwise singular. Hence $N_{\nu_n}\cong N_{\mu_\infty}\oplus N_{\mu_n}\oplus N_{\mu_{n+1}}\oplus\cdots$. Combining this with Corollary 10.12 gives

$$
\begin{aligned}
N
&\cong N_{\nu_1}\oplus N_{\nu_2}\oplus N_{\nu_3}\oplus\cdots\\
&\cong (N_{\mu_\infty}\oplus N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots)
 \oplus (N_{\mu_\infty}\oplus N_{\mu_2}\oplus N_{\mu_3}\oplus\cdots)\\
&\qquad\oplus (N_{\mu_\infty}\oplus N_{\mu_3}\oplus N_{\mu_4}\oplus\cdots)\oplus\cdots\\
&\cong N_{\mu_\infty}^{(\infty)}\oplus N_{\mu_1}\oplus N_{\mu_2}^{(2)}
 \oplus N_{\mu_3}^{(3)}\oplus\cdots.
\end{aligned}
$$

The proof of the uniqueness part of the theorem is left to the reader. $\blacksquare$

Note that the form of the normal operator presented in Example 10.13 is the form of the operator given in the conclusion of the preceding theorem.

Now to discuss $\{N\}'$. Fix a compactly supported positive Borel measure $\mu$ on $\mathbb C$ and let $\mathcal H_n$ be an $n$-dimensional Hilbert space, $1\leq n\leq\infty$. Define a function $f:\mathbb C\to\mathcal H_n$ to be a Borel function if $z\mapsto\langle f(z),g\rangle$ is a Borel function for each $g$ in $\mathcal H_n$. If $f:\mathbb C\to\mathcal H_n$ is a Borel function and $\{e_j\}$ is an orthonormal basis for $\mathcal H_n$, then $\|f(z)\|^2=\sum_j|\langle f(z),e_j\rangle|^2$, so $z\mapsto\|f(z)\|^2$ is a Borel function. Let $L^2(\mu;\mathcal H_n)$ be the space of all Borel functions $f:\mathbb C\to\mathcal H_n$ such that $\|f\|^2\equiv\int\|f(z)\|^2\,d\mu(z)<\infty$, where two functions agreeing a.e. $[\mu]$ are identified. If $f$ and $g\in L^2(\mu;\mathcal H_n)$, $\langle f,g\rangle\equiv\int\langle f(z),g(z)\rangle\,d\mu(z)$ defines an inner product on $L^2(\mu;\mathcal H_n)$. It is not difficult to show that $L^2(\mu;\mathcal H_n)$ is a Hilbert space.

**10.17. Proposition.** *If $N$ is multiplication by $z$ on $L^2(\mu;\mathcal H_n)$, then $N\cong N_\mu^{(n)}$.*

**Proof.** Let $\{e_j:1\leq j\leq n\}$ be an orthonormal basis for $\mathcal H_n$ and define $U:L^2(\mu;\mathcal H_n)\to L^2(\mu)^{(n)}$ by $Uf=(\langle f(\cdot),e_1\rangle,\langle f(\cdot),e_2\rangle,\ldots)$. Then $U$ is an isomorphism and $UNU^{-1}=N_\mu^{(n)}$. The details are left to the reader. $\blacksquare$

Combining the preceding proposition with Proposition 6.1(b), we can find $\{N\}'$; namely, $\{N_\mu^{(n)}\}'=$ all matrices $(T_{ij})$ on $\mathcal B(L^2(\mu)^{(n)})$ such that $T_{ij}\in\{N_\mu\}'$ for all $i,j$. By Corollary 6.9, $\{N_\mu^{(n)}\}'=$ matrices $(M_{\phi_{ij}})$ that belong to $\mathcal B(L^2(\mu)^{(n)})$, such that $\phi_{ij}\in L^\infty(\mu)$. Now the idea is to use Proposition 10.17 to bring this back to $\mathcal B(L^2(\mu;\mathcal H_n))$ and describe $\{N\}'$.

A function $\phi:\mathbb C\to\mathcal B(\mathcal H_n)$ is defined to be a Borel function if for each $f$ and $g$ in $\mathcal H_n$, $z\mapsto\langle\phi(z)f,g\rangle$ is a Borel function. If $\{f_j\}$ is a countable dense subset of the unit ball of $\mathcal H_n$, $\|\phi(z)\|=\sup\{|\langle\phi(z)f_i,f_j\rangle|:1\leq i,j<\infty\}$, so $z\mapsto\|\phi(z)\|$ is a Borel function. Let $L^\infty(\mu;\mathcal B(\mathcal H_n))$ be the equivalence classes of bounded Borel functions from $\mathbb C$ into $\mathcal B(\mathcal H_n)$ furnished with the $\mu$-essential supremum norm.

If $\phi\in L^\infty(\mu;\mathcal B(\mathcal H_n))$ and $f\in L^2(\mu;\mathcal H_n)$, let $f(z)=\sum_j f_j(z)e_j$, where $\{e_j\}$ is an orthonormal basis for $\mathcal H_n$ and $f_j(z)=\langle f(z),e_j\rangle$, so $\sum_j|f_j(z)|^2=\|f(z)\|^2$. Thus $\phi(z)f(z)=\sum_j f_j(z)\phi(z)e_j$. So for any $e$ in $\mathcal H_n$, $\langle\phi(z)f(z),e\rangle=\sum_j f_j(z)\langle\phi(z)e_j,e\rangle$ is a Borel function. It is easy to check that $\phi f\in L^2(\mu;\mathcal H_n)$ and
