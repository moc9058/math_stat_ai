So $F$ can be extended to a bounded linear functional $F_1$ on $\mathcal H^{(n)}$. Hence there are vectors $h_1,\ldots,h_n$ in $\mathcal H$ such that

$$
\begin{aligned}
F_1(f_1\oplus\cdots\oplus f_n)
&=\langle f_1\oplus\cdots\oplus f_n,\,
h_1\oplus\cdots\oplus h_n\rangle\\
&=\sum_{k=1}^{n}\langle f_k,h_k\rangle.
\end{aligned}
$$

In particular, $L(A)=F(Ag_1\oplus\cdots\oplus Ag_n)=\sum_{k=1}^{n}\langle Ag_k,h_k\rangle$. $\blacksquare$

**5.2. Corollary.** *If $\mathcal C$ is a convex subset of $\mathcal B(\mathcal H)$, the WOT closure of $\mathcal C$ equals the SOT closure of $\mathcal C$.*

**Proof.** Combine the preceding proposition with Corollary V.1.4. $\blacksquare$

When discussing the closure (WOT or SOT) of a convex set it is usually better to discuss the SOT. Shortly an “algebraic” characterization of the SOT closure of a subalgebra of $\mathcal B(\mathcal H)$ will be given. But first recall (VIII.5.3) that if $1\leq n\leq\infty$, $\mathcal H^{(n)}$ denotes the direct sum of $\mathcal H$ with itself $n$ times ($\aleph_0$ times if $n=\infty$). If $A\in\mathcal B(\mathcal H)$, $A^{(n)}$ is the operator on $\mathcal H^{(n)}$ defined by $A^{(n)}(h_1,\ldots,h_n)=(Ah_1,\ldots,Ah_n)$. If $\mathcal S\subset\mathcal B(\mathcal H)$, $\mathcal S^{(n)}\equiv\{A^{(n)}:A\in\mathcal S\}$. It is rather interesting that the SOT closure of an algebra can be characterized using its lattice of invariant subspaces.

**5.3. Proposition.** *If $\mathcal A$ is a subalgebra of $\mathcal B(\mathcal H)$ containing $1$, then the SOT closure of $\mathcal A$ is*

$$
\tag{5.4}
\{B\in\mathcal B(\mathcal H):\text{for every finite }n,\ 
\operatorname{Lat}\mathcal A^{(n)}\subseteq\operatorname{Lat}B^{(n)}\}.
$$

**Proof.** It is left as an exercise for the reader to show that if $B\in\operatorname{SOT-cl}\mathcal A$, $B$ belongs to the set (5.4). Now assume that $B$ belongs to the set (5.4). Fix $f_1,f_2,\ldots,f_n$ in $\mathcal H$ and $\varepsilon>0$. It must be shown that there is an $A$ in $\mathcal A$ such that $\|(A-B)f_k\|<\varepsilon$ for $1\leq k\leq n$.

Let $\mathcal M=\bigvee\{(Af_1,\ldots,Af_n):A\in\mathcal A\}$. Because $\mathcal A$ is an algebra, $\mathcal M\in\operatorname{Lat}\mathcal A^{(n)}$, hence $\mathcal M\in\operatorname{Lat}B^{(n)}$. Because $1\in\mathcal A$, $(f_1,\ldots,f_n)\in\mathcal M$. Since $\{(Af_1,\ldots,Af_n):A\in\mathcal A\}$ is a dense manifold and $(Bf_1,\ldots,Bf_n)\in\mathcal M$, there is an $A$ in $\mathcal A$ with $\varepsilon^2>\sum_{k=1}^{n}\|(A-B)f_k\|^2$; hence $B\in\operatorname{SOT-cl}\mathcal A$. $\blacksquare$

**5.5. Proposition.** *The closed unit ball of $\mathcal B(\mathcal H)$ is WOT compact.*

**Proof.** The proof of this proposition follows along the lines of the proof of Alaoglu’s Theorem. For each $h$ in $\operatorname{ball}\mathcal H$ let $X_h=$ a copy of $\operatorname{ball}\mathcal H$ with the weak topology. Put $X=\prod\{X_h:\|h\|\leq1\}$. If $A\in\operatorname{ball}\mathcal B(\mathcal H)$ let $\tau(A)\in X$ defined by $\tau(A)_h=Ah$. Give $X$ the product topology. Then $\tau:(\operatorname{ball}\mathcal B(\mathcal H),\mathrm{WOT})\to X$ is a continuous function and a homeomorphism onto its image (verify). Now show that $\tau(\operatorname{ball}\mathcal B(\mathcal H))$ is closed in $X$. From here it follows that $\operatorname{ball}\mathcal B(\mathcal H)$ is WOT compact. $\blacksquare$

## Exercises

1. Show that if $B\in\operatorname{SOT-cl}\mathcal A$, then $B$ belongs to the set defined in (5.4).
