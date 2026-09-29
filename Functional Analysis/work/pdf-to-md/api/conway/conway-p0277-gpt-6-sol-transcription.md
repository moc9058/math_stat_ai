10. For the representation in (VIII.5.5), find the corresponding spectral measure.

11. In Example VIII.5.4, the representation is not quite covered by Theorem 1.14 since it is a representation of $L^\infty(\mu)$ and not $C(X)$. Nevertheless, this representation is given by a spectral measure defined on $\Omega$. Find it.

12. Let $X$ be a compact Hausdorff space and let $\{x_n\}$ be a sequence in $X$. Let $\{e_n\}$ be an orthonormal basis for $\mathcal H$ and for each $u$ in $C(X)$ define $\rho(u)$ in $\mathcal B(\mathcal H)$ by $\rho(u)e_n=u(x_n)e_n$. Show that $\rho$ is a representation and find the corresponding spectral measure.

13. A representation $\rho:\mathcal A\to\mathcal B(\mathcal H)$ is *irreducible* if the only projections in $\mathcal B(\mathcal H)$ that commute with every $\rho(a)$, $a$ in $\mathcal A$, are 0 and 1. Prove that if $\mathcal A$ is abelian and $\rho$ is an irreducible representation of $\mathcal A$, then $\dim\mathcal H=1$. Find the corresponding spectral measure.

14. Show that a representation $\rho:C(X)\to\mathcal B(\mathcal H)$ is injective if and only if $E(G)\ne0$ for every non-empty open set $G$, where $E$ is the corresponding spectral measure.

15. Let $\{A_i\}$ be a net of hermitian operators on $\mathcal H$ and suppose that there is a hermitian operator $T$ such that $A_i\leq T$ for all $i$. If $\{\langle A_i h,h\rangle\}$ is an increasing net in $\mathbb R$ for every $h$ in $\mathcal H$, then there is a hermitian operator $A$ such that $A_i\to A\;(\mathrm{WOT})$.

16. Show that there is a contraction $\tau:\mathcal B(\mathcal H)^{**}\to\mathcal B(\mathcal H)$ such that $\tau(T)=T$ for $T$ in $\mathcal B(\mathcal H)$. If $\rho:C(X)\to\mathcal B(\mathcal H)$ is a representation, show that the map $\tilde\rho$ in the proof of Theorem 1.14 is given by $\tilde\rho(\phi)=\tau\circ\rho^{**}(\phi)$.

## §2. The Spectral Theorem

The Spectral Theorem is a landmark in the theory of operators on a Hilbert space. It provides a complete statement about the nature and structure of normal operators. This accolade will be seen to be deserved when in Section 10 the Spectral Theorem is used to give a complete set of unitary invariants. Two operators $A$ and $B$ are *unitarily equivalent* if there is a unitary operator $U$ such that $UAU^*=B$; in symbols, $A\cong B$. Using the Spectral Theorem, a (countable) set of objects is attached to a normal operator $N$ on a (separable) Hilbert space. It is then shown that two normal operators are unitarily equivalent if and only if these objects are equal.

The Spectral Theorem for a normal operator $N$ on a Hilbert space with $\dim\mathcal H=d<\infty$ says that $N$ can be diagonalized. That is, if $\alpha_1,\ldots,\alpha_d$ are the eigenvalues of $N$ (repeated as often as their multiplicities), then the corresponding eigenvectors $e_1,e_2,\ldots,e_d$ from an orthonormal basis for $\mathcal H$. In infinite dimensional spaces a normal operator need not have eigenvalues. For example, let $N=$ multiplication by the independent variable on $L^2(0,1)$. So an alternative formulation that can be generalized is desired.

Let $N$ be normal on $\mathcal H$, $\dim\mathcal H=d<\infty$. Let $\lambda_1,\ldots,\lambda_n$ be the distinct eigenvalues of $N$ and let $E_k$ be the orthogonal projection of $\mathcal H$ onto
