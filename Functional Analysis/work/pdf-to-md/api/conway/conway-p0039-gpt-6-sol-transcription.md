$\mathcal X\oplus\mathcal Y$ are defined as $\{x\oplus y:x\in\mathcal X,\ y\in\mathcal Y\}$, then $(x_1\oplus y_1)+(x_2\oplus y_2)\equiv(x_1+x_2)\oplus(y_1+y_2)$, and so on.

**6.1. Definition.** If $\mathcal H$ and $\mathcal K$ are Hilbert spaces, $\mathcal H\oplus\mathcal K=\{h\oplus k:h\in\mathcal H,\ k\in\mathcal K\}$ and

$$
\langle h_1\oplus k_1,h_2\oplus k_2\rangle
\equiv\langle h_1,h_2\rangle+\langle k_1,k_2\rangle.
$$

It must be shown that this defines an inner product on $\mathcal H\oplus\mathcal K$ and that $\mathcal H\oplus\mathcal K$ is complete (Exercise).

Now what happens if we want to define $\mathcal H_1\oplus\mathcal H_2\oplus\cdots$ for a sequence of Hilbert spaces $\mathcal H_1,\mathcal H_2,\ldots$? There is a problem about the completeness of this infinite direct sum, but this can be overcome as follows.

**6.2. Proposition.** *If $\mathcal H_1,\mathcal H_2,\ldots$ are Hilbert spaces, let $\mathcal H=\{(h_n)_{n=1}^{\infty}:h_n\in\mathcal H_n$ for all $n$ and $\sum_{n=1}^{\infty}\|h_n\|^2<\infty\}$. For $h=(h_n)$ and $g=(g_n)$ in $\mathcal H$, define*

$$
\langle h,g\rangle=\sum_{n=1}^{\infty}\langle h_n,g_n\rangle. \tag{6.3}
$$

*Then $\langle\cdot,\cdot\rangle$ is an inner product on $\mathcal H$ and the norm relative to this inner product is $\|h\|=[\sum_{n=1}^{\infty}\|h_n\|^2]^{1/2}$. With this inner product $\mathcal H$ is a Hilbert space.*

**Proof.** If $h=(h_n)$ and $g=(g_n)\in\mathcal H$, then the CBS inequality implies $\sum|\langle h_n,g_n\rangle|\leq\sum\|h_n\|\|g_n\|\leq(\sum\|h_n\|^2)^{1/2}(\sum\|g_n\|^2)^{1/2}<\infty$. Hence the series in (6.3) converges absolutely. The remainder of the proof is left to the reader. $\blacksquare$

**6.4. Definition.** If $\mathcal H_1,\mathcal H_2,\ldots$ are Hilbert spaces, the space $\mathcal H$ of Proposition 6.2 is called the *direct sum* of $\mathcal H_1,\mathcal H_2,\ldots$ and is denoted by $\mathcal H\equiv\mathcal H_1\oplus\mathcal H_2\oplus\cdots$.

This is part of a more general process. If $\{\mathcal H_i:i\in I\}$ is a collection of Hilbert spaces, $\mathcal H\equiv\bigoplus\{\mathcal H_i:i\in I\}$ is defined as the collection of functions $h:I\to\bigcup\{\mathcal H_i:i\in I\}$ such that $h(i)\in\mathcal H_i$ for all $i$ and $\sum\{\|h(i)\|^2:i\in I\}<\infty$. If $h,g\in\mathcal H$, $\langle h,g\rangle\equiv\sum\{\langle h(i),g(i)\rangle:i\in I\}$; $\mathcal H$ is a Hilbert space.

The main reason for considering direct sums is that they provide a way of manufacturing operators on Hilbert space. In fact, Hilbert space is a rather dull subject, except for the fact that there are numerous interesting questions about the linear operators on them that are as yet unresolved. This subject is introduced in the next chapter.

## EXERCISES

1. Let $\{(X_i,\Omega_i,\mu_i):i\in I\}$ be a collection of measure spaces and define $X$, $\Omega$, and $\mu$ as follows. Let $X=$ the disjoint union of $\{X_i:i\in I\}$ and let $\Omega=\{\Delta\subseteq X:\Delta\cap X_i\in\Omega_i$ for all $i\}$. For $\Delta$ in $\Omega$ put $\mu(\Delta)=\sum_i\mu_i(\Delta\cap X_i)$. Show that $(X,\Omega,\mu)$ is a measure space and $L^2(X,\Omega,\mu)$ is isomorphic to $\bigoplus\{L^2(X_i,\Omega_i,\mu_i):i\in I\}$.
