**1.1. Definition.** If $X$ is a set, $\Omega$ is a $\sigma$-algebra of subsets of $X$, and $\mathcal H$ is a Hilbert space, a *spectral measure* for $(X,\Omega,\mathcal H)$ is a function $E:\Omega\to\mathcal B(\mathcal H)$ such that:

(a) for each $\Delta$ in $\Omega$, $E(\Delta)$ is a projection;

(b) $E(\square)=0$ and $E(X)=1$;

(c) $E(\Delta_1\cap\Delta_2)=E(\Delta_1)E(\Delta_2)$ for $\Delta_1$ and $\Delta_2$ in $\Omega$;

(d) if $\{\Delta_n\}_{n=1}^{\infty}$ are pairwise disjoint sets from $\Omega$, then

$$
E\left(\bigcup_{n=1}^{\infty}\Delta_n\right)
=\sum_{n=1}^{\infty}E(\Delta_n).
$$

A word or two concerning condition (d) in the preceding definition. If $\{E_n\}$ is a sequence of pairwise orthogonal projections on $\mathcal H$, then it was shown in Exercise II.3.5 that for each $h$ in $\mathcal H$, $\sum_{n=1}^{\infty}E_n(h)$ converges in $\mathcal H$ to $E(h)$, where $E$ is the orthogonal projection of $\mathcal H$ onto $\bigvee\{E_n(\mathcal H):n\geq 1\}$. Thus it is legitimate to write $E=\sum_{n=1}^{\infty}E_n$. Now if $\Delta_1\cap\Delta_2=\square$, then (b) and (c) above imply that $0=E(\Delta_1)E(\Delta_2)=E(\Delta_2)E(\Delta_1)$; that is, $E(\Delta_1)$ and $E(\Delta_2)$ have orthogonal ranges. So if $\{\Delta_n\}_1^\infty$ is a sequence of pairwise disjoint sets in $\Omega$, the ranges of $\{E(\Delta_n)\}$ are pairwise orthogonal. Thus the equation $E(\bigcup_1^\infty\Delta_n)=\sum_1^\infty E(\Delta_n)$ in (d) has the precise meaning just discussed.

Another way to discuss this is by the introduction of two topologies that will also be of value later.

**1.2. Definition.** If $\mathcal H$ is a Hilbert space, the *weak operator topology* (WOT) on $\mathcal B(\mathcal H)$ is the locally convex topology defined by the seminorms $\{p_{h,k}:h,k\in\mathcal H\}$ where $p_{h,k}(A)=|\langle Ah,k\rangle|$. The *strong operator topology* (SOT) is the topology defined on $\mathcal B(\mathcal H)$ by the family of seminorms $\{p_h:h\in\mathcal H\}$, where $p_h(A)=\|Ah\|$.

**1.3. Proposition.** Let $\mathcal H$ be a Hilbert space and let $\{A_i\}$ be a net in $\mathcal B(\mathcal H)$.

(a) $A_i\to A$ (WOT) if and only if $\langle A_i h,k\rangle\to\langle Ah,k\rangle$ for all $h,k$ in $\mathcal H$.

(b) If $\sup_i\|A_i\|<\infty$ and $\mathcal T$ is a total subset of $\mathcal H$, then $A_i\to A$ (WOT) if and only if $\langle A_i h,k\rangle\to\langle Ah,k\rangle$ for all $h,k$ in $\mathcal T$.

(c) $A_i\to A$ (SOT) if and only if $\|A_i h-Ah\|\to 0$ for all $h$ in $\mathcal H$.

(d) If $\sup_i\|A_i\|<\infty$ and $\mathcal T$ is a total subset of $\mathcal H$, then $A_i\to A$ (SOT) if and only if $\|A_i h-Ah\|\to 0$ for all $h$ in $\mathcal T$.

(e) If $\mathcal H$ is separable, then the WOT and SOT are metrizable on bounded subsets of $\mathcal B(\mathcal H)$.

**Proof.** The proofs of (a) through (d) are left as exercises. For (e), let $\{h_n\}$ be any countable total subset of ball $\mathcal H$. If $A,B\in\mathcal B(\mathcal H)$, let

$$
d_s(A,B)=\sum_{n=1}^{\infty}2^{-n}\|(A-B)h_n\|,
$$

$$
d_w(A,B)=\sum_{m,n=1}^{\infty}2^{-n-m}
\left|\left\langle(A-B)h_n,h_m\right\rangle\right|.
$$
