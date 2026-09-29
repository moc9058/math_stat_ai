The preceding theorem says that the value of the index is impervious to compact perturbations. The next result, the third in the list of important properties of the Fredholm index, says that the value of the index is unchanged for all perturbations of the operator, provided that the size of the perturbation is sufficiently small.

**3.12. Theorem.** *If $A:\mathcal H\to\mathcal H'$ is a Fredholm operator, then there is an $\varepsilon>0$ such that if $Y\in\mathcal B(\mathcal H,\mathcal H')$ and $\|Y\|<\varepsilon$, then $A+Y$ is Fredholm and $\operatorname{ind}A=\operatorname{ind}(A+Y)$.*

**Proof.** With respect to the decompositions $\mathcal H=(\ker A)^\perp\oplus\ker A$ and $\mathcal H'=\operatorname{ran}A\oplus\ker A^*$, the operator $A$ has the matrix

$$
\begin{bmatrix}
A_1 & 0\\
0 & 0
\end{bmatrix}
$$

and $A_1:(\ker A)^\perp\to\operatorname{ran}A$ is invertible since $A$ is Fredholm. Thus there is an $\varepsilon>0$ such that if $\|Y_1\|<\varepsilon$, then $A_1+Y_1$ is invertible. If $Y:\mathcal H\to\mathcal H'$ and $\|Y\|<\varepsilon$, then, with respect to the same decomposition of $\mathcal H$,

$$
Y=\begin{bmatrix}
Y_1 & Y_2\\
Y_3 & Y_4
\end{bmatrix}
$$

and so

$$
A+Y
=\begin{bmatrix}
A_1+Y_1 & Y_2\\
Y_3 & Y_4
\end{bmatrix}
=\begin{bmatrix}
A_1+Y_1 & 0\\
0 & 0
\end{bmatrix}
+\begin{bmatrix}
0 & Y_2\\
Y_3 & Y_4
\end{bmatrix},
$$

where the first matrix represents a Fredholm operator and the second represents a finite rank operator. Therefore $\operatorname{ind}(A+Y)$ is the index of the first matrix. But since $A_1+Y_1$ is invertible, Lemma 3.5 implies that this index is equal to $\dim(\ker A)-\dim(\ker A^*)=\operatorname{ind}A$. $\blacksquare$

**3.13. Corollary.** *If $\mathcal{SF}$ is given the norm topology and $\mathbb Z\cup\{\pm\infty\}$ is given the discrete topology, then the Fredholm index is a continuous function from $\mathcal{SF}$ into $\mathbb Z\cup\{\pm\infty\}$.*

This continuity statement has an equivalent formulation. Because $\mathcal{SF}$ is an open subset of $\mathcal B(\mathcal H)$, its components are open sets. Thus the continuity of the index is equivalent to the statement that it is constant on the components of $\mathcal{SF}$.

For a treatment of the Fredholm index applicable to unbounded operators on a Banach space, see Kato [1966], pp. 229–244. For other approaches to Fredholm theory, with variations and generalizations of the material in this book, see Caradus, Pfaffenberger, and Yood [1974] and Harte [1982].

## Exercises

1. Prove Lemma 3.6.

2. If $A\in\mathcal B(\mathcal H)$ and $\operatorname{ran}A$ is closed, show that $\operatorname{ran}A^{(\infty)}$ is closed. If $A\in\mathcal{SF}$ and $\ker A=(0)$, show that $A^{(\infty)}\in\mathcal{SF}$ and $\operatorname{ind}A^{(\infty)}=-\infty$ or $0$.
