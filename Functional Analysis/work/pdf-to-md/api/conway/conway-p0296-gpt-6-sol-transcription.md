12. Let $(X,\Omega,\mu)$ be an arbitrary measure space and let $L\in L^{1}(\mu)^{*}$. (a) Show that for every $f$ in $L^{2}(\mu)$, there is an $h$ in $L^{2}(\mu)$ such that $L(g\bar f)=\int g\bar h\,d\mu$ for all $g$ in $L^{2}(\mu)$. (b) If $f\in L^{2}(\mu)$, let $Tf$ be the function $h$ in $L^{2}(\mu)$ obtained in part (a). Show that $T:L^{2}(\mu)\to L^{2}(\mu)$ defines a bounded linear operator and $T$ commutes with $M_{\phi}$ for every $\phi$ in $L^{\infty}(\mu)$. (c) In light of parts (a) and (b), compare Theorem 6.6 and Example 20.17 in Hewitt and Stromberg [1975].

## §7. Abelian von Neumann Algebras

**7.1. Definition.** A *von Neumann algebra* $\mathcal A$ is a C\*-subalgebra of $\mathcal B(\mathcal H)$ such that $\mathcal A=\mathcal A''$.

Note that if $\mathcal A$ is a von Neumann algebra, then $1\in\mathcal A$ and $\mathcal A$ is SOT closed. Conversely, if $1\in\mathcal A$ and $\mathcal A$ is a SOT closed C\*-subalgebra of $\mathcal B(\mathcal H)$, then $\mathcal A$ is a von Neumann algebra by the Double Commutant Theorem.

It is a result of S. Sakai that a C\*-algebra is isomorphic to a von Neumann algebra if it is the dual of a Banach space. The converse to this is an easy consequence of the fact that $\mathcal B(\mathcal H)$ is a dual space (Exercise 2.21). For an account of the history of this result and its predecessors, as well as a number of proofs, see Kadison [1985].

**7.2. Examples.** (a) $\mathcal B(\mathcal H)$ and $\mathbb C$ are von Neumann algebras.

(b) If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, then $\mathcal A_{\mu}\equiv\{M_{\phi}:\phi\in L^{\infty}(\mu)\}\subseteq\mathcal B(L^{2}(\mu))$ is an abelian von Neumann algebra by Theorem 6.6. In fact, it is a maximal abelian von Neumann algebra.

It will be shown in this section that $\mathcal A_{\mu}$ is the only abelian von Neumann algebra up to a \*-isomorphism. However, there are many others that are not unitarily equivalent to $\mathcal A_{\mu}$.

For $\mathcal A_j\subseteq\mathcal B(\mathcal H_j)$, $j\geq 1$, $\mathcal A_1\oplus\mathcal A_2\oplus\cdots$ is used to denote the $l^{\infty}$ direct sum of $\mathcal A_1,\mathcal A_2,\ldots$. That is, $\mathcal A_1\oplus\mathcal A_2\oplus\cdots=\{A_1\oplus A_2\oplus\cdots:A_j\in\mathcal A_j$ for $j\geq 1$ and $\sup_j\|A_j\|<\infty\}$. Note that $\mathcal A_1\oplus\mathcal A_2\oplus\cdots\subseteq\mathcal B(\mathcal H_1\oplus\mathcal H_2\oplus\cdots)$ and $\|A_1\oplus A_2\oplus\cdots\|=\sup_j\|A_j\|$.

**7.3. Proposition.** *(a) If $\mathcal A_1,\mathcal A_2,\ldots$ are von Neumann algebras, then so is $\mathcal A_1\oplus\mathcal A_2\oplus\cdots$. (b) If $\mathcal A$ is a von Neumann algebra and $1\leq n\leq\infty$, then $\mathcal A^{(n)}$ is a von Neumann algebra.*

**Proof.** Exercise.

The proof of the next result is also an exercise.

**7.4. Proposition.** *Let $\mathcal A_j$ be a von Neumann algebra on $\mathcal H_j$, $j=1,2$. If $U:\mathcal H_1\to\mathcal H_2$ is an isomorphism such that $U\mathcal A_1U^{-1}=\mathcal A_2$, then $U\mathcal A_1'U^{-1}=\mathcal A_2'$.*

Now let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and define $\rho:\mathcal A_{\mu}\to\mathcal A_{\mu}^{(2)}$ by
