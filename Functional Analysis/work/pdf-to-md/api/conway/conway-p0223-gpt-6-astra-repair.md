208  VII. Banach Algebras and Spectral Theory

3. Let $\mathcal A,\mathcal B$ be as in Theorem 5.4. If $a\in\mathcal B$ and $\sigma_{\mathcal A}(a)\subseteq\mathbb R$, show that $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)$.

4. Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$. If $G_1,G_2,\ldots$ are the holes of $\sigma_{\mathcal A}(a)$ and $1\leq n_1\leq n_2,\ldots$, show that there is a subalgebra $\mathcal B$ of $\mathcal A$ such that $a\in\mathcal B$ and $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)\cup\bigcup_{k=1}^{\infty}G_{n_k}$.

5. If $\mathcal A,\mathcal B$, and $a$ are as in Theorem 5.4, $\mathcal A$ is not abelian, and $\mathcal B$ is a maximal abelian subalgebra of $\mathcal A$, show that $\sigma_{\mathcal A}(a)=\sigma_{\mathcal B}(a)$.

6. If $K$ is a nonempty compact subset of $\mathbb C$ that is polynomially convex, show that the components of $\operatorname{int}K$ are simply connected.

## §6. The Spectrum of a Linear Operator

The proof of the first result is left as an exercise.

**6.1. Proposition.**

(a) *If $\mathcal X$ is a Banach space and $A\in\mathcal B(\mathcal X)$, $\sigma(A^*)=\sigma(A)$.*

(b) *If $\mathcal H$ is a Hilbert space and $A\in\mathcal B(\mathcal H)$, $\sigma(A^*)=\sigma(A)^*$, where for any subset $\Delta$ of $\mathbb C$, $\Delta^*\equiv\{\bar z:z\in\Delta\}$.*

In this section only results about operators on Banach spaces will be given. For the corresponding results about operators on a Hilbert space involving the adjoint, the reader is asked to supply the details. The preceding proposition should be kept in mind as a model of the probable differences.

In this section and the next $\mathcal X$ always denotes a Banach space over $\mathbb C$.

**6.2. Definition.** If $A\in\mathcal B(\mathcal X)$, the *point spectrum* of $A$, $\sigma_p(A)$, is defined by

$$
\sigma_p(A)\equiv\{\lambda\in\mathbb C:\ker(A-\lambda)\ne(0)\}.
$$

As in the case of operators on a Hilbert space, elements of $\sigma_p(A)$ are called *eigenvalues*. If $\lambda\in\sigma_p(A)$, non-zero vectors in $\ker(A-\lambda)$ are called *eigenvectors*; $\ker(A-\lambda)$ is called the *eigenspace* of $A$ at $\lambda$.

**6.3. Definition.** If $A\in\mathcal B(\mathcal X)$, the *approximate point spectrum* of $A$, $\sigma_{ap}(A)$, is defined by

$$
\begin{aligned}
\sigma_{ap}(A)\equiv\{\lambda\in\mathbb C:\;&\text{there is a sequence }\{x_n\}\text{ in }\mathcal X\\
&\text{such that }\|x_n\|=1\text{ for all }n\text{ and }\|(A-\lambda)x_n\|\to0\}.
\end{aligned}
$$

Note that $\sigma_p(A)\subseteq\sigma_{ap}(A)$.

**6.4. Proposition.** *If $A\in\mathcal B(\mathcal X)$ and $\lambda\in\mathbb C$, the following statements are equivalent.*

(a) $\lambda\notin\sigma_{ap}(A)$.

(b) $\ker(A-\lambda)=(0)$ *and* $\operatorname{ran}(A-\lambda)$ *is closed*.
