**2.5. Proposition.** If $U\in\mathcal{B}(\mathcal{H},\mathcal{K})$, then $U$ is an isomorphism if and only if $U$ is invertible and $U^{-1}=U^*$.

**Proof.** Exercise.

From now on we will examine and prove results for the adjoint of operators in $\mathcal{B}(\mathcal{H})$. Often, as in the next proposition, there are analogous results for the adjoint of operators in $\mathcal{B}(\mathcal{H},\mathcal{K})$. This simplification is justified, however, by the cleaner statements that result. Also, the interested reader will have no trouble formulating the more general statement when it is needed.

**2.6. Proposition.** If $A,B\in\mathcal{B}(\mathcal{H})$ and $\alpha\in\mathbb{F}$, then:

(a) $(\alpha A+B)^*=\bar{\alpha}A^*+B^*$.

(b) $(AB)^*=B^*A^*$.

(c) $A^{**}\equiv(A^*)^*=A$.

(d) If $A$ is invertible in $\mathcal{B}(\mathcal{H})$ and $A^{-1}$ is its inverse, then $A^*$ is invertible and $(A^*)^{-1}=(A^{-1})^*$.

The proof of the preceding proposition is left as an exercise, but a word about part (d) might be helpful. The hypothesis that $A$ is invertible in $\mathcal{B}(\mathcal{H})$ means that there is an operator $A^{-1}$ in $\mathcal{B}(\mathcal{H})$ such that $AA^{-1}=A^{-1}A=I$. It is a remarkable fact that if $A$ is only assumed to be bijective, then $A$ is invertible in $\mathcal{B}(\mathcal{H})$. This is a consequence of the Open Mapping Theorem, which will be proved later.

**2.7. Proposition.** If $A\in\mathcal{B}(\mathcal{H})$, $\|A\|=\|A^*\|=\|A^*A\|^{1/2}$.

**Proof.** For $h$ in $\mathcal{H}$, $\|h\|\leq 1$,
$$
\|Ah\|^2=\langle Ah,Ah\rangle=\langle A^*Ah,h\rangle
\leq\|A^*Ah\|\,\|h\|\leq\|A^*A\|\leq\|A^*\|\,\|A\|.
$$
Hence $\|A\|^2\leq\|A^*A\|\leq\|A^*\|\,\|A\|$. Using the two ends of this string of inequalities gives $\|A\|\leq\|A^*\|$ when $\|A\|$ is cancelled. But $A=A^{**}$ and so if $A^*$ is substituted for $A$, we get $\|A^*\|\leq\|A^{**}\|=\|A\|$. Hence $\|A\|=\|A^*\|$. Thus the string of inequalities becomes a string of equalities and the proof is complete. $\blacksquare$

**2.8. Example.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $M_\phi$ be the multiplication operator with symbol $\phi$ (1.5). Then $M_\phi^*$ is $M_{\bar\phi}$, the multiplication operator with symbol $\bar\phi$.

If an operator on $\mathbb{F}^d$ is presented by a matrix, then its adjoint is represented by the conjuagate transpose of the matrix.

**2.9. Example.** If $K$ is the integral operator with kernel $k$ as in (1.6), then $K^*$ is the integral operator with kernel $k^*(x,y)\equiv\overline{k(y,x)}$.

**2.10. Proposition.** If $S:\ell^2\to\ell^2$ is defined by $S(\alpha_1,\alpha_2,\ldots)=(0,\alpha_1,\alpha_2,\ldots)$, then $S$ is an isometry and $S^*(\alpha_1,\alpha_2,\ldots)=(\alpha_2,\alpha_3,\ldots)$.
