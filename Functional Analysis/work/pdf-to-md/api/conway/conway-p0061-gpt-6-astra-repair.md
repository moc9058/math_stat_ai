46  II. Operators on Hilbert Space

5. Show that no nonzero multiplication operator on $L^2(0,1)$ is compact.

6. Show that if $T:\mathcal H\to\mathcal H$ is a compact operator and $\{e_n\}$ is any orthonormal sequence in $\mathcal H$, then $\|Te_n\|\to 0$. Is the converse true?

7. If $T$ is compact and $\mathcal M$ is an invariant subspace for $T$, show that $T|_{\mathcal M}$ is compact.

8. If $h,g\in\mathcal H$, define $T:\mathcal H\to\mathcal H$ by $Tf=\langle f,h\rangle g$. Show that $T$ has rank 1 [that is, $\dim(\operatorname{ran}T)=1$]. Moreover, every rank 1 operator can be so represented. Show that if $T$ is a finite rank operator, then there are orthonormal vectors $e_1,\ldots,e_n$ and vectors $g_1,\ldots,g_n$ such that $Th=\sum_{j=1}^{n}\langle h,e_j\rangle g_j$ for all $h$ in $\mathcal H$. In this case show that $T$ is normal if $g_j=\lambda_j e_j$ for some scalars $\lambda_1,\ldots,\lambda_n$. Find $\sigma_p(T)$.

9. Show that a diagonalizable operator is normal.

10. Verify the statements in Example 4.10.

11. Verify the statement in Example 4.11.

12. Verify the statement in Example 4.12. (Note that the operator $K$ in this example is diagonalizable.)

13. If $T_n\in\mathcal B(\mathcal H_n)$, $n\geq 1$, with $\sup_n\|T_n\|<\infty$ and $T=\bigoplus_{n=1}^{\infty}T_n$ on $\mathcal H=\bigoplus_{n=1}^{\infty}\mathcal H_n$, show that $T$ is compact if and only if each $T_n$ is compact and $\|T_n\|\to 0$.

14. In Lemma 4.8, show that if $L^2(X,\Omega,\mu)$ is separable, then $\{\varphi_{ij}\}$ is a basis for $L^2(X\times X,\Omega\times\Omega,\mu\times\mu)$. What if $L^2(X,\Omega,\mu)$ is not separable?

## §5*. The Diagonalization of Compact Self-Adjoint Operators

This section and the remaining ones in this chapter may be omitted if the reader intends to continue through to the end of this book, as the material in these sections (save for Section 6) will be obtained in greater generality in Chapter IX. It is worthwhile, however, to examine this material even if Chapter IX is to be read, since the intuition provided by this special case is valuable.

The main result of this section is the following.

**5.1. Theorem.** *If $T$ is a compact self-adjoint operator on $\mathcal H$, then $T$ has only a countable number of distinct eigenvalues. If $\{\lambda_1,\lambda_2,\ldots\}$ are the distinct nonzero eigenvalues of $T$, and $P_n$ is the projection of $\mathcal H$ onto $\ker(T-\lambda_n)$, then $P_nP_m=P_mP_n=0$ if $n\neq m$, each $\lambda_n$ is real, and*

$$
T=\sum_{n=1}^{\infty}\lambda_nP_n, \tag*{5.2}
$$

*where the series converges to $T$ in the metric defined by the norm of $\mathcal B(\mathcal H)$. [Of course, (5.2) may be only a finite sum.]*
