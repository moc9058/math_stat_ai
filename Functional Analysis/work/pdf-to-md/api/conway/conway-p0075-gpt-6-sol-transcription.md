a multiplicative linear map such that $\|\tau(\phi)\|=\sup\{|\phi(\lambda)|:\lambda\in\sigma_p(T)\}$, $\tau(1)=1$, and $\tau(\psi)=T$ whenever $\psi(z)=z$ on $\sigma_p(T)\cup\{0\}$, then $\tau(\phi)=\phi(T)$ for every $\phi$ in $l^\infty(\mathbb C)$.

## §8*. Unitary Equivalence for Compact Normal Operators

In Section I.5 the concept of an isomorphism between Hilbert spaces was defined as the natural equivalence relation on Hilbert spaces. This equivalence relation between the spaces induces a natural equivalence relation between the operators on the spaces.

**8.1. Definition.** If $A,B$ are bounded operators on Hilbert spaces $\mathcal H,\mathcal K$, then $A$ and $B$ are *unitarily equivalent* if there is an isomorphism $U:\mathcal H\to\mathcal K$ such that $UAU^{-1}=B$. In symbols this is denoted by $A\cong B$.

Some of the elementary properties of unitary equivalence are contained in Exercises 1 and 2. Note that if $UAU^{-1}=B$, then $UA=BU$.

The purpose of this section is to give necessary and sufficient conditions that two compact normal operators be unitarily equivalent. Later, in Section IX.10, necessary and sufficient conditions that any two normal operators be unitarily equivalent are given and the results of this section are subsumed by those of that section.

**8.2. Definition.** If $T$ is a compact operator, the *multiplicity function* for $T$ is the cardinal number valued function $m_T$ defined for every complex number $\lambda$ by $m_T(\lambda)=\dim\ker(T-\lambda)$.

Hence $m_T(\lambda)\geq 0$ for all $\lambda$ and $m_T(\lambda)>0$ if and only if $\lambda$ is an eigenvalue for $T$. Note that by Proposition 4.13, $m_T(\lambda)<\infty$ if $\lambda\neq 0$.

If $T,S$ are compact operators on Hilbert spaces and $U:\mathcal H\to\mathcal K$ is an isomorphism with $UTU^{-1}=S$, then $U\ker(T-\lambda)=\ker(S-\lambda)$ for every $\lambda$ in $\mathbb C$. In fact, if $Th=\lambda h$, then $SUh=UTh=\lambda Uh$ and so $Uh\in\ker(S-\lambda)$. Conversely, if $k\in\ker(S-\lambda)$ and $h=U^{-1}k$, then $Th=TU^{-1}k=U^{-1}Sk=\lambda h$. In particular, it must be that $m_T=m_S$. If $S$ and $T$ are normal, this condition is also sufficient for unitary equivalence.

**8.3. Theorem.** *Two compact normal operators are unitarily equivalent if and only if they have the same multiplicity function.*

**Proof.** Let $T,S$ be compact normal operators on Hilbert spaces $\mathcal H,\mathcal K$. If $T\cong S$, then it has already been shown that $m_T=m_S$. Suppose now that $m_T=m_S$. We must manufacture a unitary operator $U:\mathcal H\to\mathcal K$ such that $UTU^{-1}=S$.

Let $T=\sum_{n=1}^{\infty}\lambda_nP_n$ and let $S=\sum_{n=1}^{\infty}\mu_nQ_n$ as in the Spectral Theorem (7.6). So if $n\neq m$, then $\lambda_n\neq\lambda_m$ and $\mu_n\neq\mu_m$, and each of the projections $P_n$ and $Q_n$
