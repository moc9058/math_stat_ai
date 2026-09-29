## §7*. The Spectral Theorem and Functional Calculus for Compact Normal Operators

We begin by characterizing the operators that commute with a diagonalizable operator. If one considers the definition of a diagonalizable operator (4.6), it is possible to reformulate it in a way that is more tractable for the present purpose and closer to the form of a compact self-adjoint operator given in (5.2). Unlike (4.6), it will not be assumed that the underlying Hilbert space is separable.

**7.1. Proposition.** *Let $\{P_i:i\in I\}$ be a family of pairwise orthogonal projections in $\mathcal B(\mathcal H)$. (That is, $P_iP_j=P_jP_i=0$ for $i\ne j$.) If $h\in\mathcal H$, then $\sum_i\{P_i h:i\in I\}$ converges in $\mathcal H$ to $Ph$, where $P$ is the projection of $\mathcal H$ onto $\bigvee\{P_i\mathcal H:i\in I\}$.*

This appeared as Exercise 3.5 and its proof is left to the reader.

If $\{P_i:i\in I\}$ is as in the preceding proposition and $\mathcal M_i=P_i\mathcal H$, then with the notation of Definition 3.4, $P$ is the projection of $\mathcal H$ onto $\bigoplus_i\mathcal M_i$. Write $P=\sum_iP_i$. A word of caution here: $Ph=\sum_iP_i h$, where the convergence is in the norm of $\mathcal H$. However, $\sum_iP_i$ does not converge to $P$ in the norm of $\mathcal B(\mathcal H)$. In fact, it never does unless $I$ is finite (Exercise 1).

**7.2. Definition.** A *partition of the identity* on $\mathcal H$ is a family $\{P_i:i\in I\}$ of pairwise orthogonal projections on $\mathcal H$ such that $\bigvee_iP_i\mathcal H=\mathcal H$. This might be indicated by $1=\sum_iP_i$ or $1=\bigoplus_iP_i$. [Note that $1$ is often used to denote the operator on $\mathcal H$ defined by $1(h)=h$ for all $h$. Similarly if $\alpha\in\mathbb F$, $\alpha$ is the operator defined by $\alpha(h)=\alpha h$ for all $h$.]

**7.3. Definition.** An operator $A$ on $\mathcal H$ is *diagonalizable* if there is a partition of the identity on $\mathcal H$, $\{P_i:i\in I\}$, and a family of scalars $\{\alpha_i:i\in I\}$ such that $\sup_i|\alpha_i|<\infty$ and $Ah=\alpha_i h$ whenever $h\in\operatorname{ran}P_i$.

It is easy to see that this is equivalent to the definition given in (4.6) when $\mathcal H$ is separable (Exercise 2). Also, $\|A\|=\sup_i|\alpha_i|$.

To denote a diagonalizable operator satisfying the conditions of (7.3), write

$$
A=\sum_i\alpha_iP_i
\quad\text{or}\quad
A=\bigoplus_i\alpha_iP_i.
$$

Note that it was not assumed that the scalars $\alpha_i$ in (7.3) are distinct. There is no loss in generality in assuming this, however. In fact, if $\alpha_i=\alpha_j$, then we can replace $P_i$ and $P_j$ with $P_i+P_j$.

**7.4. Proposition.** *An operator $A$ on $\mathcal H$ is diagonalizable if and only if there is an orthonormal basis for $\mathcal H$ consisting of eigenvectors for $A$.*

**Proof.** Exercise.

Also note that if $A=\bigoplus_i\alpha_iP_i$, then $A^*=\bigoplus_i\overline{\alpha_i}P_i$ and $A$ is normal (Exercise 5).
