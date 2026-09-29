is an orthonormal basis $\{e_j^{(0)}:j\geqslant 1\}$ for $\operatorname{cl}(\operatorname{ran}B_0)$ and scalars $\{\beta_j^{(0)}:j\geqslant 1\}$ such that $Be_j^{(0)}=\beta_j^{(0)}e_j^{(0)}$. It follows that $Te_j^{(0)}=i\beta_j^{(0)}e_j^{(0)}$. Moreover, $\ker T^*\supseteq\ker A\cap\ker B_0$ so $\operatorname{cl}(\operatorname{ran}T)\subseteq\operatorname{cl}(\operatorname{ran}A)\oplus\operatorname{cl}(\operatorname{ran}B_0)$.

The remainder of the proof now consists in a certain amount of bookkeeping to gather together the eigenvectors belonging to the same eigenvalues of $T$ and the performing of some light housekeeping chores to obtain the convergence of the series (7.7) ■

**7.8. Corollary.** *With the notation of (7.6):*

(a) $\ker T=[\bigvee\{P_n\mathcal H:n\geqslant 1\}]^\perp$;

(b) *each $P_n$ has finite rank;*

(c) $\|T\|=\sup\{|\lambda_n|:n\geqslant 1\}$ *and either $\{\lambda_n\}$ is finite or $\lambda_n\to 0$ as $n\to\infty$.*

The proof of (7.8) is similar to the proof of (5.3).

**7.9. Corollary.** *If $T$ is a compact operator on a complex Hilbert space, then $T$ is normal if and only if $T$ is diagonalizable.*

If $T$ is a normal operator which is not necessarily compact, there is a spectral theorem for $T$ which has a somewhat different form. This theorem states that $T$ can be represented as an integral with respect to a measure whose values are not numbers but projections on a Hilbert space. Theorem 7.6 will be a consequence of this more general theorem and correspond to the case in which this projection-valued measure is “atomic.”

The approach to this more general spectral theorem will be to develop a functional calculus for normal operators $T$. That is, an operator $\phi(T)$ will be defined for every bounded Borel function $\phi$ on $\mathbb C$ and certain properties of the map $\phi\mapsto\phi(T)$ will be deduced. The projection-valued measure will then be obtained by letting $\mu(\Delta)=\chi_\Delta(T)$, where $\chi_\Delta$ is the characteristic function of the set $\Delta$. These matters are taken up in Chapter IX.

At this point, Theorem 7.6 will be used to develop a functional calculus for compact normal operators. For the remainder of this section $\mathcal H$ is a complex Hilbert space.

**7.10. Definition.** Denote by $l^\infty(\mathbb C)$ all the bounded functions $\phi:\mathbb C\to\mathbb C$. If $T$ is a compact normal operator satisfying (7.7), define $\phi(T):\mathcal H\to\mathcal H$ by

$$
\phi(T)=\sum_{n=1}^{\infty}\phi(\lambda_n)P_n+\phi(0)P_0,
$$

where $P_0=$ the projection of $\mathcal H$ onto $\ker T$.

Note that $\phi(T)$ is a diagonalizable operator and $\|\phi(T)\|=\sup\{|\phi(0)|,|\phi(\lambda_1)|,\ldots\}$ (4.6). Much more can be said.

**7.11. Functional Calculus for Compact Normal Operators.** *If $T$ is a compact normal operator on a $\mathbb C$-Hilbert space $\mathcal H$, then the map $\phi\mapsto\phi(T)$ of*
