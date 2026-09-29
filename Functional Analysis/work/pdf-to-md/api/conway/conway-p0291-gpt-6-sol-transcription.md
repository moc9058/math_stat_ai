2. Show that $\mathcal{B}_{00}$ is SOT dense in $\mathcal{B}$.

3. If $\{A_k\}$ and $\{B_k\}$ are sequences in $\mathcal{B}(\mathcal{H})$ such that $A_k\to A$ (WOT) and $B_k\to B$ (SOT), then $A_kB_k\to AB$ (WOT).

4. With the notation of Exercise 3, show that if $A_k\to A$ (SOT), then $A_kB_k\to AB$ (SOT).

5. Let $S$ be the unilateral shift on $l^2(\mathbb{N})$ (II.2.10). Examine the sequences $\{S^k\}$ and $\{S^{*k}\}$ and their relation to Exercises 3 and 4.

6. (Halmos.) Fix an orthonormal basis $\{e_n:n\geqslant 1\}$ for $\mathcal{H}$. (a) Show that $0\in$ weak closure of $\{\sqrt{n}e_n:n\geqslant 1\}$ (Halmos [1982], Solution 28). (b) Let $\{n_i\}$ be a net of integers such that $\sqrt{n_i}e_{n_i}\to 0$ weakly. Define $A_if=\sqrt{n_i}\langle f,e_{n_i}\rangle e_{n_i}$ for $f$ in $\mathcal{H}$. Show that $A_i\to 0$ (SOT) but $\{A_i^2\}$ does not converge to $0$ (SOT).

## §6. Commuting Operators

If $\mathcal{S}\subseteq\mathcal{B}(\mathcal{H})$, let $\mathcal{S}'\equiv\{A\in\mathcal{B}(\mathcal{H}):AS=SA\text{ for every }S\text{ in }\mathcal{S}\}$. $\mathcal{S}'$ is called the *commutant* of $\mathcal{S}$. It is not difficult to see that $\mathcal{S}'$ is always an algebra. Similarly, $\mathcal{S}''\equiv(\mathcal{S}')'$ is called the *double commutant* of $\mathcal{S}$. This process can continue, but (happily) $\mathcal{S}'''=\mathcal{S}'$ (Exercise 1). In some circumstances, $\mathcal{S}=\mathcal{S}''$.

The problem of determining the commutant or double commutant of a single operator or a collection of operators leads to some exciting and interesting mathematics. The commutant is an algebraic object and the idea is to bring the force of analysis to bear in the characterization of this algebra.

We begin by examining the commutant of a direct sum of operators. Recall that if $\mathcal{H}=\mathcal{H}_1\oplus\mathcal{H}_2\oplus\cdots$ and $A_n\in\mathcal{B}(\mathcal{H}_n)$ for $n\geqslant 1$, then $A=A_1\oplus A_2\oplus\cdots$ defines a bounded operator on $\mathcal{H}$ if and only if $\sup_n\|A_n\|<\infty$; in this case $\|A\|=\sup_n\|A_n\|$. Also, each operator $B$ on $\mathcal{H}$ has a matrix representation $[B_{ij}]$ where $B_{ij}\in\mathcal{B}(\mathcal{H}_j,\mathcal{H}_i)$.

**6.1. Proposition.** (a) *If $A=A_1\oplus A_2\oplus\cdots$ is a bounded operator on $\mathcal{H}=\mathcal{H}_1\oplus\mathcal{H}_2\oplus\cdots$ and $B=[B_{ij}]\in\mathcal{B}(\mathcal{H})$, then $AB=BA$ if and only if $B_{ij}A_j=A_iB_{ij}$ for all $i,j$.*

(b) *If $B=[B_{ij}]\in\mathcal{B}(\mathcal{H}^{(n)})$, $BA^{(n)}=A^{(n)}B$ if and only if $B_{ij}A=AB_{ij}$ for all $i,j$.*

The proof of this proposition is an easy exercise in matrix manipulation and is left to the reader.

**6.2. Proposition.** *If $A\in\mathcal{B}(\mathcal{H})$ and $1\leqslant n\leqslant\infty$, then $\{A^{(n)}\}''=\{B^{(n)}:B\in\{A\}''\}=\{\{A\}''\}^{(n)}$.*

**Proof.** The second equality in the statement is a tautology and it is the first equality that forms the substance of the proposition. If $B\in\{A\}''$, then the preceding proposition implies that $B^{(n)}\in\{A^{(n)}\}''$. Now let $B\in\{A^{(n)}\}''$. To simplify the notation, assume $n=2$. So $B\in\{A\oplus A\}''$; let $B=[B_{ij}]$, $B_{ij}\in\mathcal{B}(\mathcal{H})$.
