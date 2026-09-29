by itself. One such account in Steen [1973]. You might also consult the notes in Dunford and Schwartz [1963] and Halmos [1951].

## EXERCISES

Throughout these exercises, $N$ is a normal operator on $\mathcal H$ with spectral measure $E$.

1. Show that $\lambda\in\sigma_p(N)$ if and only if $E(\{\lambda\})\ne 0$. Moreover, if $\lambda\in\sigma_p(N)$, $E(\{\lambda\})$ is the orthogonal projection onto $\ker(N-\lambda)$.

2. If $\Delta$ is a clopen subset of $\sigma(N)$, show that $E(\Delta)$ is the Riesz idempotent associated with $\Delta$.

3. Prove Theorem II.5.1 and its corollaries by using the Spectral Theorem.

4. Prove Theorem II.7.6 and its corollaries by using the Spectral Theorem.

5. Obtain Theorem II.7.11 as a consequence of (2.3).

6. Verify the statements in Example 2.5.

7. Verify (2.6e).

8. Show that if $\mathcal H$ is separable, there are at most a countable number of points $\{z_n\}$ in $\sigma(N)$ such that $E(z_n)\ne 0$. By Exercise 1, these are the eigenvalues of $N$.

9. Show that a normal operator $N$ is (a) hermitian if and only if $\sigma(N)\subseteq\mathbb R$; (b) positive if and only if $\sigma(N)\subseteq[0,\infty)$; (c) unitary if and only if $\sigma(N)\subseteq\partial\mathbb D$.

10. Let $A$ be a hermitian operator with spectral measure $E$ on a separable space. For each real number $t$ define a projection $P(t)=E(-\infty,t)$. Show:

    (a) $P(s)\leq P(t)$ for $s\leq t$;

    (b) if $t_n\leq t_{n+1}$ and $t_n\to t$, $P(t_n)\to P(t)$ (SOT);

    (c) for all but a countable number of points $t$, $P(t_n)\to P(t)$ (SOT) if $t_n\to t$;

    (d) for $f$ in $C(\sigma(A))$, $f(A)=\int_{-\infty}^{\infty}f(t)\,dP(t)$, where this integral is to be defined (by the reader) in the Riemann–Stieltjes sense.

11. If $\sigma_p(N)$ is a Borel set, show that $E(\sigma(N)\backslash\sigma_p(N))=0$ if and only if $N$ is diagonalizable; that is, there is a basis for $\mathcal H$ consisting of eigenvectors for $N$. If $\sigma_p(N)$ is not assumed to be a Borel set, is it still possible to characterize diagonalizable normal operators in a similar way? Give an example of a normal operator $N$ such that $\sigma_p(N)$ is not a Borel set.

12. Show that if $N=U|N|$ ($|N|=(N^*N)^{1/2}$) is the polar decomposition of $N$, $U=\phi(N)$ for some Borel function $\phi$ on $\sigma(N)$. Hence $U|N|=|N|U$ (see Exercise VIII.3.21).

13. Show that $N=W|N|$ for some unitary $W$ that is a function of $N$.

14. Prove that if $A$ is hermitian, $\exp(iA)$ is unitary. Is the converse true?

15. Show that there is a normal operator $M$ such that $M^2=N$ and $M=\phi(N)$ for some Borel function $\phi$. How many such normal operators $M$ are there?

16. Define $N:L^2(\mathbb R)\to L^2(\mathbb R)$ by $(Nf)(t)=f(t+1)$. Show that $N$ is normal and find its spectral decomposition. ((X.6.17) is useful here.)

17. Suppose that $N_1,\ldots,N_d$ are normal operators such that $N_jN_k^*=N_k^*N_j$ for
