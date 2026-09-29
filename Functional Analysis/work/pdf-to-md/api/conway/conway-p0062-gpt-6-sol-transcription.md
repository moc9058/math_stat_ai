The proof of Theorem 5.1 requires a few preliminary results. Before beginning this process, let’s look at a few consequences.

**5.3. Corollary.** *With the notation of (5.1):*

(a) $\ker T=\left[\bigvee\{P_n\mathcal H:n\geqslant1\}\right]^\perp=(\operatorname{ran}T)^\perp$;

(b) *each $P_n$ has finite rank;*

(c) $\|T\|=\sup\{|\lambda_n|:n\geqslant1\}$ *and* $\lambda_n\to0$ *as* $n\to\infty$.

**Proof.** Since $P_n\perp P_m$ for $n\ne m$, if $h\in\mathcal H$, then (5.2) implies $\|Th\|^2=\sum_{n=1}^{\infty}\|\lambda_nP_nh\|^2=\sum_{n=1}^{\infty}|\lambda_n|^2\|P_nh\|^2$. Hence $Th=0$ if and only if $P_nh=0$ for all $n$. That is, $h\in\ker T$ if and only if $h\perp P_n\mathcal H$ for all $n$, whence (a).

Part (b) follows by Proposition 4.13.

For part (c), if $\mathcal L=\operatorname{cl}[\operatorname{ran}T]$, $\mathcal L$ is invariant for $T$. Since $T=T^*$, $\mathcal L=(\ker T)^\perp$ and $\mathcal L$ reduces $T$. So we can consider the restriction of $T$ to $\mathcal L$, $T|_{\mathcal L}$. Now $\mathcal L=\bigvee\{P_n\mathcal H:n\geqslant1\}$ by (a). Let $\{e_j^{(n)}:1\leqslant j\leqslant N_n\}$ be a basis for $P_n\mathcal H=\ker(T-\lambda_n)$, so $Te_j^{(n)}=\lambda_ne_j^{(n)}$ for $1\leqslant j\leqslant N_n$. Thus $\{e_j^{(n)}:1\leqslant j\leqslant N_n,\ n\geqslant1\}$ is a basis for $\mathcal L$ and $T|_{\mathcal L}$ is diagonalizable with respect to this basis. Part (c) now follows by (4.6). ■

The proof of (c) in the preceding corollary revealed an interesting fact that deserves a statement of its own.

**5.4. Corollary.** *If $T$ is a compact self-adjoint operator, then there is a sequence $\{\mu_n\}$ of real numbers and an orthonormal basis $\{e_n\}$ for $(\ker T)^\perp$ such that for all $h$,*

$$
Th=\sum_{n=1}^{\infty}\mu_n\langle h,e_n\rangle e_n.
$$

Note that there may be repetitions in the sequence $\{\mu_n\}$ in (5.4). How many repetitions?

**5.5. Corollary.** *If $T\in\mathcal B_0(\mathcal H)$, $T=T^*$, and $\ker T=(0)$, then $\mathcal H$ is separable.*

Also note that by (4.6), if (5.2) holds, $T\in\mathcal B_0(\mathcal H)$.

To begin the proof of Theorem 5.1, we prove a few results about not necessarily compact operators.

**5.6. Proposition.** *If $A$ is a normal operator and $\lambda\in\mathbb F$, then $\ker(A-\lambda)=\ker(A-\lambda)^*$ and $\ker(A-\lambda)$ is a reducing subspace for $A$.*

**Proof.** Since $A$ is normal, so is $A-\lambda$. Hence $\|(A-\lambda)h\|=\|(A-\lambda)^*h\|$ (2.16). Thus $\ker(A-\lambda)=\ker(A-\lambda)^*$. If $h\in\ker(A-\lambda)$, $Ah=\lambda h\in\ker(A-\lambda)$. Also $A^*h=\bar\lambda h\in\ker(A-\lambda)$. Therefore $\ker(A-\lambda)$ reduces $A$. ■

**5.7. Proposition.** *If $A$ is a normal operator and $\lambda,\mu$ are distinct eigenvalues of $A$, then $\ker(A-\lambda)\perp\ker(A-\mu)$.*
