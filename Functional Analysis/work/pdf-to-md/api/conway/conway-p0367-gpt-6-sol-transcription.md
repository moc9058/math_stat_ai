**2.4. Corollary.** *A bounded operator $A:\mathcal H\to\mathcal H'$ is Fredholm if and only if $\operatorname{ran}A$ is closed and both $\ker A$ and $\ker A^*$ are finite dimensional.*

In the case of a bounded operator $A$ from a Hilbert space $\mathcal H$ into itself, the concept of a semi-Fredholm operator can be rephrased in terms of the corresponding concept in the Calkin algebra, $\mathcal B/\mathcal B_0$. In fact, this will be the primary situation in which the ideas of Fredholm theory are applied. The next result is immediate from the definition.

**2.5. Proposition.** *For a Hilbert space $\mathcal H$, let $\pi:\mathcal B\to\mathcal B/\mathcal B_0$ be the natural map and let $A\in\mathcal B=\mathcal B(\mathcal H)$. The operator $A$ is left (respectively, right) semi-Fredholm if and only if $\pi(A)$ is left (respectively, right) invertible in the Calkin algebra.*

For notation, let $\mathcal F_\ell=\mathcal F_\ell(\mathcal H)$ and $\mathcal F_r=\mathcal F_r(\mathcal H)$ be the set of left and right semi-Fredholm operators on the Hilbert space $\mathcal H$. So $\mathcal F=\mathcal F_\ell\cap\mathcal F_r$ and $\mathcal{SF}=\mathcal F_\ell\cup\mathcal F_r$ are the sets of Fredholm and semi-Fredholm operators on $\mathcal H$. Since $\mathcal F_\ell=$ the inverse image under $\pi$ of the left invertible elements of the Banach algebra $\mathcal B/\mathcal B_0$, the next proposition is immediate.

**2.6. Proposition.** *Each of the sets $\mathcal F_\ell$, $\mathcal F_r$, $\mathcal F$, and $\mathcal{SF}$ are open subjects of $\mathcal B$.*

## EXERCISES

1. If $A\in\mathcal B(\mathcal H)$ and $\operatorname{ran}A$ is closed, prove than $\operatorname{ran}A^*$ is closed without using Theorem VI.1.10. [Hint: Show that there is a bounded operator $B$ on $\mathcal H$ such that $BA=$ the projection of $\mathcal H$ onto $(\ker A)^\perp$.]

2. Give a direct proof that (b) implies (a) in Theorem 2.3.

3. Let $A,B,C\in\mathcal B(\mathcal H)$ and define $X:\mathcal H^{(2)}\to\mathcal H^{(2)}$ by the matrix $X=\begin{bmatrix}A&B\\0&C\end{bmatrix}$. (a) Show that if $A\in\mathcal F$, then $X\in\mathcal F$ if and only if $C\in\mathcal F$. (b) If $A\in\mathcal F$, show that $X\in\mathcal{SF}$ if and only if $C\in\mathcal{SF}$. (c) Suppose $A,C\in\mathcal{SF}$ with $\dim\ker A=\infty$ and $\dim\ker C^*=\infty$. Show that $X\notin\mathcal{SF}$.

4. If $A\in\mathcal B(\mathcal H)$, show that $A\mathcal M$ is closed for every closed subspace $\mathcal M$ of $\mathcal H$ if and only if $A$ has finite rank or $A$ is left Fredholm.

5. If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $T\in\mathcal B(\mathcal X,\mathcal Y)$ such that the Hamel basis dimension (that is, the algebraic dimension) of $\mathcal Y/(\operatorname{ran}T)$ is finite, then $\operatorname{ran}T$ is closed.

6. Show that a normal operator is Fredholm if and only if $0$ is not a limit point of $\sigma(N)$ and $\dim\ker N<\infty$. (See Proposition 4.5 below.)

## §3. The Fredholm Index

I wish to acknowledge that the basis of this section is a development of the Fredholm index which I learned from my colleague Hari Bercovici.
