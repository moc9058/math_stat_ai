**4.3. Proposition.** Let $A\in\mathcal B(\mathcal H)$.

(a) $\lambda\in\sigma_{le}(A)$ if and only if $\dim\ker(A-\lambda)=\infty$ or $\operatorname{ran}(A-\lambda)$ is not closed.

(b) $\lambda\in\sigma_{re}(A)$ if and only if $\dim[\operatorname{ran}(A-\lambda)]^\perp=\infty$ or $\operatorname{ran}(A-\lambda)$ is not closed.

The reader should compare Proposition 4.3 and Proposition 1.1.

**4.4. Proposition.** If $A\in\mathcal B(\mathcal H)$, then
$$
\sigma_{ap}(A)=\sigma_{le}(A)\cup\{\lambda\in\sigma_p(A):\dim\ker(A-\lambda)<\infty\}.
$$

**Proof.** If $\lambda\in\sigma_{ap}(A)$, then (1.1) either $\operatorname{ran}(A-\lambda)$ is not closed or $\ker(A-\lambda)\ne0$. If $\operatorname{ran}(A-\lambda)$ is not closed or if $\dim\ker(A-\lambda)=\infty$, then $\lambda\in\sigma_{le}(A)$ by (4.3). The proof of other inclusion is left to the reader. ■

**4.5. Proposition.** If $N$ is a normal operator and $\lambda\in\sigma(N)$, then $\operatorname{ran}(N-\lambda)$ is closed if and only if $\lambda$ is not a limit point of $\sigma(N)$.

**Proof.** Assume $\lambda$ is an isolated point of $\sigma(N)$; thus $X=\sigma(N)\backslash\{\lambda\}$ is a closed subset of $\sigma(N)$. If $N=\int z\,dE(z)$ and $\mathcal H_1=E(X)\mathcal H$, then $\mathcal H_1$ reduces $N$ and $\sigma(N|\mathcal H_1)=X$. Hence $(N-\lambda)\mathcal H_1$ is closed. Since $\mathcal H_1^\perp=\ker(N-\lambda)$, $\operatorname{ran}(N-\lambda)=(N-\lambda)\mathcal H_1$; hence $N-\lambda$ has closed range.

Now assume that $\lambda\in\sigma(N)$ but $\lambda$ is not an isolated point. Then there is a strictly decreasing sequence $\{r_n\}$ of positive real numbers such that $r_n\to0$ and such that each open annulus $A_n=\{z:r_{n+1}<|z-\lambda|<r_n\}$ has non-empty intersection with $\sigma(N)$. Thus $E(A_n)\mathcal H\ne(0)$; let $e_n$ be a unit vector in $E(A_n)\mathcal H$. Then $e_n\perp\ker(N-\lambda)\;(=E(\{\lambda\})\mathcal H)$ and
$$
\|(N-\lambda)e_n\|^2
=\int_{A_n}|z-\lambda|^2\,dE_{e_n,e_n}(z)
\le r_n^2\to0.
$$

That is, $\inf\{\|(N-\lambda)h\|:\|h\|=1,\ h\perp\ker(N-\lambda)\}=0$ and so, by the Open Mapping Theorem, $N-\lambda$ does not have closed range. ■

**4.6. Proposition.** If $N$ is a normal operator, then $\sigma_e(N)=\sigma_{le}(N)=\sigma_{re}(N)$ and
$$
\sigma(N)\backslash\sigma_e(N)
=\{\lambda\in\sigma(N):\lambda\text{ is an isolated point of }\sigma(N)\text{ that is an eigenvalue of finite multiplicity}\}.
$$

**Proof.** The first part follows by applying Proposition 1.3 to the Calkin algebra. If $\lambda$ is an isolated point of $\sigma(N)$, then $\operatorname{ran}(N-\lambda)$ is closed by the preceding proposition. So if $\dim\ker(N-\lambda)<\infty$, $\lambda\notin\sigma_{le}(N)=\sigma_e(N)$ by Proposition 4.3. Conversely, if $\lambda\in\sigma(N)\backslash\sigma_e(N)$, then $\operatorname{ran}(N-\lambda)$ is closed and $\dim\ker(N-\lambda)<\infty$. By the preceding proposition, $\lambda$ is an isolated point of $\sigma(N)$. ■

**4.7. Example.** Let $G$ be a bounded region in $\mathbb C$ and, to avoid pathologies, assume $\partial G=\partial[\operatorname{cl}G]$. Let $\mathcal H=L_a^2(G)$ (I.1.10) and define $S:\mathcal H\to\mathcal H$ by $(Sf)(z)=zf(z)$. Then $\sigma(S)=\operatorname{cl}G$, $\sigma_e(S)=\sigma_{le}(S)=\sigma_{re}(S)=\partial G=\sigma_{ap}(S)$,
