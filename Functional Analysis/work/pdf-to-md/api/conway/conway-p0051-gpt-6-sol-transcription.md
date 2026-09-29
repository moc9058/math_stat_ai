be closed. All that can be said is that $(\ker A)^\perp=\operatorname{cl}(\operatorname{ran}A^*)$ and $(\ker A^*)^\perp=\operatorname{cl}(\operatorname{ran}A)$.

## Exercises

1. Prove Proposition 2.5.

2. Prove Proposition 2.6.

3. Verify the statement in Example 2.8.

4. Verify the statement in Example 2.9.

5. Find the adjoint of a diagonal operator (Exercise 1.8).

6. Let $S$ be the unilateral shift and compute $SS^*$ and $S^*S$. Also compute $S^nS^{*n}$ and $S^{*n}S^n$.

7. Compute the adjoint of the Volterra operator $V$ (1.7) and $V+V^*$. What is $\operatorname{ran}(V+V^*)$?

8. Where was the hypothesis that $\mathcal H$ is a Hilbert space over $\mathbb C$ used in the proof of Proposition 2.12?

9. Suppose $A=B+iC$, where $B$ and $C$ are hermitian and prove that $B=(A+A^*)/2$, $C=(A-A^*)/2i$.

10. Prove Proposition 2.15.

11. If $A$ and $B$ are self-adjoint, show that $AB$ is self-adjoint if and only if $AB=BA$.

12. Let $\sum_{n=0}^{\infty}\alpha_nz^n$ be a power series with radius of convergence $R$, $0<R\leqslant\infty$. If $A\in\mathcal B(\mathcal H)$ and $\|A\|<R$, show that there is an operator $T$ in $\mathcal B(\mathcal H)$ such that for any $h,g$ in $\mathcal H$, $\langle Th,g\rangle=\sum_{n=0}^{\infty}\alpha_n\langle A^nh,g\rangle$. [If $f(z)=\sum\alpha_nz^n$, the operator $T$ is usually denoted by $f(A)$.]

13. Let $A$ and $T$ be as in Exercise 12 and show that $\|T-\sum_{k=0}^{n}\alpha_kA^k\|\to0$ as $n\to\infty$. If $BA=AB$, show that $BT=TB$.

14. If $f(z)=\exp z=\sum_{n=0}^{\infty}z^n/n!$ and $A$ is hermitian, show that $f(iA)$ is unitary.

15. If $A$ is a normal operator on $\mathcal H$, show that $A$ is injective if and only if $A$ has dense range. Give an example of an operator $B$ such that $\ker B=(0)$ but $\operatorname{ran}B$ is not dense. Give an example of an operator $C$ such that $C$ is surjective but $\ker C\ne(0)$.

16. Let $M_\phi$ be a multiplication operator (1.5) and show that $\ker M_\phi=0$ if and only if $\mu(\{x:\phi(x)=0\})=0$. Give necessary and sufficient conditions on $\phi$ that $\operatorname{ran}M_\phi$ be closed.

## §3. Projections and Idempotents; Invariant and Reducing Subspaces

**3.1. Definition.** An *idempotent* on $\mathcal H$ is a bounded linear operator $E$ on $\mathcal H$ such that $E^2=E$. A *projection* is an idempotent $P$ such that $\ker P=(\operatorname{ran}P)^\perp$.
