§4. Compact Operators　　　　　　　　　　　　　　　　　45

Thus, $\{Te_{n_k}\}$ is a Cauchy sequence. But for $n_k\ne n_j$, $\|Te_{n_k}-Te_{n_j}\|^2=\|\lambda e_{n_k}-\lambda e_{n_j}\|^2=2|\lambda|^2>0$ since $\lambda\ne0$. This contradiction shows that $\ker(T-\lambda)$ must be finite dimensional. ■

The next result on the existence of eigenvalues is not a practical way to show that a specific example has a nonzero eigenvalue, but it is a good theoretical tool that will be used later in this book (in particular, in the next section).

**4.14. Proposition.** *If $T$ is a compact operator on $\mathcal H$, $\lambda\ne0$, and $\inf\{\|(T-\lambda)h\|:\|h\|=1\}=0$, then $\lambda\in\sigma_p(T)$.*

**Proof.** By hypothesis, there is a sequence of unit vectors $\{h_n\}$ such that $\|(T-\lambda)h_n\|\to0$. Since $T$ is compact, there is a vector $f$ in $\mathcal H$ and a subsequence $\{h_{n_k}\}$ such that $\|Th_{n_k}-f\|\to0$. But $h_{n_k}=\lambda^{-1}[(\lambda-T)h_{n_k}+Th_{n_k}]\to\lambda^{-1}f$. So $1=\|\lambda^{-1}f\|=|\lambda|^{-1}\|f\|$ and $f\ne0$. Also, it must be that $Th_{n_k}\to\lambda^{-1}Tf$. Since $Th_{n_k}\to f$, $f=\lambda^{-1}Tf$, or $Tf=\lambda f$. That is, $f\in\ker(T-\lambda)$ and $f\ne0$, so $\lambda\in\sigma_p(T)$. ■

**4.15. Corollary.** *If $T$ is a compact operator on $\mathcal H$, $\lambda\ne0$, $\lambda\notin\sigma_p(T)$, and $\bar\lambda\notin\sigma_p(T^*)$, then $\operatorname{ran}(T-\lambda)=\mathcal H$ and $(T-\lambda)^{-1}$ is a bounded operator on $\mathcal H$.*

**Proof.** Since $\lambda\notin\sigma_p(T)$, the preceding proposition implies that there is a constant $c>0$ such that $\|(T-\lambda)h\|\ge c\|h\|$ for all $h$ in $\mathcal H$. If $f\in\operatorname{cl}\operatorname{ran}(T-\lambda)$, then there is a sequence $\{h_n\}$ in $\mathcal H$ such that $(T-\lambda)h_n\to f$. Thus $\|h_n-h_m\|\le c^{-1}\|(T-\lambda)h_n-(T-\lambda)h_m\|$ and so $\{h_n\}$ is a Cauchy sequence. Hence $h_n\to h$ for some $h$ in $\mathcal H$. Thus $(T-\lambda)h=f$. So $\operatorname{ran}(T-\lambda)$ is closed and, by (2.19), $\operatorname{ran}(T-\lambda)=[\ker(T-\lambda)^*]^\perp=\mathcal H$, by hypothesis.

So for $f$ in $\mathcal H$ let $Af=$ the unique vector $h$ such that $(T-\lambda)h=f$. Thus $(T-\lambda)Af=f$ for all $f$ in $\mathcal H$. From the inequality above, $c\|Af\|\le\|(T-\lambda)Af\|=\|f\|$. So $\|Af\|\le c^{-1}\|f\|$ and $A$ is bounded. Also, $(T-\lambda)A(T-\lambda)h=(T-\lambda)h$, so $0=(T-\lambda)[A(T-\lambda)h-h]$. Since $\lambda\notin\sigma_p(T)$, $A(T-\lambda)h=h$. That is, $A=(T-\lambda)^{-1}$. ■

It will be proved in a later chapter that if $\lambda\notin\sigma_p(T)$ and $\lambda\ne0$, then $\bar\lambda\notin\sigma_p(T^*)$. More will be shown about arbitrary compact operators in Chapter VI. In the next section the theory of compact self-adjoint operators will be explored.

## Exercises

1. Prove Proposition 4.2(c).

2. Show that every operator of finite rank is compact.

3. If $T\in\mathcal B_{00}(\mathcal H,\mathcal K)$, show that $T^*\in\mathcal B_{00}(\mathcal K,\mathcal H)$ and $\dim(\operatorname{ran}T)=\dim(\operatorname{ran}T^*)$.

4. Show that an idempotent is compact if and only if it has finite rank.
