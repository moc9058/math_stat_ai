surjective. Let $h\in\operatorname{dom}A^*$. Then there is an $f$ in $\operatorname{dom}A$ such that $(A+i)f=(A^*+i)h$. But $A^*+i\supseteq A+i$, so $(A^*+i)f=(A^*+i)h$. But $A^*+i$ is injective, so $h=f\in\operatorname{dom}A$. Thus $A=A^*$. $\blacksquare$

**2.10. Corollary.** *If $A$ is a closed symmetric operator and $\sigma(A)$ does not contain $\mathbb{R}$, then $A=A^*$.*

It may have occurred to the reader that a symmetric operator $A$ fails to be self-adjoint because its domain is too small and that this can be rectified by merely increasing the size of the domain. Indeed, if $A$ is the symmetric operator in Example 1.11, then the operator $B$ of Example 1.12 is a self-adjoint extension of $A$. However, the general situation is not always so cooperative.

Fix a symmetric operator $A$ and suppose $B$ is a symmetric extension of $A$: $A\subseteq B$. It is easy to verify that $B^*\subseteq A^*$. Since $B\subseteq B^*$, we get $A\subseteq B\subseteq B^*\subseteq A^*$. Thus every symmetric extension of $A$ is a restriction of $A^*$.

**2.11. Proposition.** *(a) A symmetric operator has a maximal symmetric extension. (b) Maximal symmetric extensions are closed. (c) A self-adjoint operator is a maximal symmetric operator.*

**Proof.** Part (a) is an easy application of Zorn’s Lemma. If $A$ is symmetric, $A\subseteq A^*$ and so $A$ is closable. The closure of a symmetric operator is symmetric (Exercise 3), so part (b) is immediate. Part (c) is a consequence of the comments preceding this proposition. $\blacksquare$

**2.12. Definition.** Let $A$ be a closed symmetric operator. The *deficiency subspaces* of $A$ are the spaces

$$
\begin{aligned}
\mathcal L_+ &= \ker(A^*-i)=[\operatorname{ran}(A+i)]^\perp,\\
\mathcal L_- &= \ker(A^*+i)=[\operatorname{ran}(A-i)]^\perp.
\end{aligned}
$$

The *deficiency indices* of $A$ are the numbers $n_\pm=\dim\mathcal L_\pm$.

It is possible for any pair of deficiency indices to occur (see Exercise 6).

In order to study the closed symmetric extensions of a symmetric operator we also introduce the spaces

$$
\begin{aligned}
\mathcal K_+ &= \{f\oplus if:f\in\mathcal L_+\},\\
\mathcal K_- &= \{g\oplus(-ig):g\in\mathcal L_-\}.
\end{aligned}
$$

So $\mathcal K_\pm\leq\mathcal H\oplus\mathcal H$. Notice that $\mathcal K_\pm$ are contained in $\operatorname{gra}A^*$ and are the portions of graph of $A^*$ that lie above $\mathcal L_\pm$. The next lemma will indicate why the deficiency subspaces are so named.

**2.13. Lemma.** *If $A$ is a closed symmetric operator,*

$$
\operatorname{gra}A^*=\operatorname{gra}A\oplus\mathcal K_+\oplus\mathcal K_-.
$$
