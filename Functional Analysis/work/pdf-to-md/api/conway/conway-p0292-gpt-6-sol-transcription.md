Since $\begin{bmatrix}0&1\\0&0\end{bmatrix}\in\{A\oplus A\}'$, matrix multiplication shows that $B_{11}=B_{22}$ and $B_{21}=0$. Similarly, the fact that $\begin{bmatrix}0&0\\1&0\end{bmatrix}$ commutes with $A\oplus A$ implies that $B_{12}=0$. If $C=B_{11}(=B_{22})$, $B=C\oplus C$. If $T\in\{A\}'$, then $T\oplus T\in\{A\oplus A\}'$, so $B(T\oplus T)=(T\oplus T)B$. This shows that $C\in\{A\}''$. $\blacksquare$

The next result is a corollary of the preceding proof.

**6.3. Corollary.** *If $\mathcal S\subseteq\mathcal B(\mathcal H)$, $\{\mathcal S^{(n)}\}''=\{\mathcal S''\}^{(n)}$.*

Say that a subspace $\mathcal M$ of $\mathcal H$ reduces a collection $\mathcal S$ of operators if it reduces each operator in $\mathcal S$. By Proposition II.3.7, $\mathcal M$ reduces $\mathcal S$ if and only if the projection of $\mathcal H$ onto $\mathcal M$ belongs to $\mathcal S'$. This is important in the next theorem, due to von Neumann [1929].

**6.4. The Double Commutant Theorem.** *If $\mathcal A$ is a $C^*$-subalgebra of $\mathcal B(\mathcal H)$ containing $1$, then $\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A=\mathrm{WOT}\text{-}\mathrm{cl}\,\mathcal A=\mathcal A''$.*

**Proof.** By Corollary 5.2, $\mathrm{WOT}\text{-}\mathrm{cl}\,\mathcal A=\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A$. Also, since $\mathcal A''$ is SOT closed (Exercise 2) and $\mathcal A\subseteq\mathcal A''$, $\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A\subseteq\mathcal A''$.

It remains to show that $\mathcal A''\subseteq\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A$. To do this Proposition 5.3 will be used.

Let $B\in\mathcal A''$, $n\geq1$, and let $\mathcal M\in\operatorname{Lat}\mathcal A^{(n)}$. It must be shown that $B^{(n)}\mathcal M\subseteq\mathcal M$. Because $\mathcal A$ is a $C^*$-algebra, so is $\mathcal A^{(n)}$. So the fact that $\mathcal M\in\operatorname{Lat}\mathcal A^{(n)}$ and $A^{*(n)}\in\mathcal A^{(n)}$ whenever $A^{(n)}\in\mathcal A^{(n)}$ implies that $\mathcal M$ reduces $A^{(n)}$ for each $A$ in $\mathcal A$. Si if $P$ is the projection of $\mathcal H^{(n)}$ onto $\mathcal M$, $P\in\{\mathcal A^{(n)}\}'$. But $B\in\mathcal A''$; so by Corollary 6.3, $B^{(n)}\in\{\mathcal A^{(n)}\}''$. Hence $B^{(n)}P=PB^{(n)}$ and $\mathcal M\in\operatorname{Lat}B^{(n)}$. $\blacksquare$

**6.5. Corollary.** *If $\mathcal A$ is a SOT closed $C^*$-subalgebra of $\mathcal B(\mathcal H)$ containing $1$ and $A\in\mathcal B(\mathcal H)$ such that $A(P\mathcal H)\subseteq P\mathcal H$ for every projection $P$ in $\mathcal A'$, then $A\in\mathcal A$.*

**Proof.** This uses, in addition to the Double Commutant Theorem, Proposition 4.8 as applied to $\mathcal A'$. Indeed, $\mathcal A'$ is a SOT closed $C^*$-algebra and hence it is the norm-closed linear span of its projections. So if $A\in\mathcal B(\mathcal H)$ and $AP\mathcal H\subseteq P\mathcal H$ for every projection $P$ in $\mathcal A'$, then $A(1-P)\mathcal H\subseteq(1-P)\mathcal H$ for every projection $P$ in $\mathcal A'$. Thus $P\mathcal H$ reduces $A$ and, hence, $AP=PA$. By (4.8), $A\in\mathcal A''=\mathcal A$. $\blacksquare$

**6.6. Theorem.** *If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\phi\in L^\infty(\mu)$, define $M_\phi$ on $L^2(\mu)$ by $M_\phi f=\phi f$. If $\mathcal A_\mu\equiv\{M_\phi:\phi\in L^\infty(\mu)\}$, then $\mathcal A_\mu'=\mathcal A_\mu=\mathcal A_\mu''$.*

**Proof.** It is easy to see that if $\mathcal A=\mathcal A'$, then $\mathcal A=\mathcal A''$. Since $\mathcal A_\mu\subseteq\mathcal A_\mu'$, it suffices to show that $\mathcal A_\mu'\subseteq\mathcal A_\mu$. So fix $A$ in $\mathcal A_\mu'$; it must be shown that $A=M_\phi$ for some $\phi$ in $L^\infty(\mu)$.

*Case 1:* $\mu(X)<\infty$. Here $1\in L^2(\mu)$; put $\phi=A(1)$. Thus $\phi\in L^2(\mu)$. If $\psi\in L^\infty(\mu)$,
