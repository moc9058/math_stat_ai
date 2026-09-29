# §12*. The Krein–Smulian Theorem

Let $A$ be a convex subset of a Banach space $\mathcal{X}$. If $A$ is weakly closed, then for every $r>0$, $A\cap\{x\in\mathcal{X}:\|x\|\leq r\}$ is weakly closed; this is clear since each of the sets in the intersection is weakly closed. But the converse of this is also true: if $A$ is convex and $A\cap\{X\in\mathcal{X}:\|x\|\leq r\}$ is weakly closed for every $r>0$, then $A$ is weakly closed. In fact, because $A$ is convex it suffices to prove that $A$ is norm closed (Corollary 1.5). If $\{x_n\}\subseteq A$ and $\|x_n-x_0\|\to0$, then there is a constant $r$ such that $\|x_n\|\leq r$ for all $n$. By hypothesis, $A\cap\{x\in\mathcal{X}:\|x\|\leq r\}$ is weakly closed and hence norm closed. Thus $x_0\in A$.

Now let $A$ be a convex subset of $\mathcal{X}^*$, $\mathcal{X}$ a Banach space. If $A\cap\{x^*\in\mathcal{X}^*:\|x^*\|\leq r\}$ is weak-star closed for every $r>0$, is $A$ weak-star closed? If $\mathcal{X}$ is reflexive, then this is the same question that was asked and answered affirmatively in the preceding paragraph. If $\mathcal{X}$ is not reflexive, then the preceding argument fails since there are norm closed convex subsets of $\mathcal{X}^*$ that are not weak-star closed. (Example: let $x^{**}\in\mathcal{X}^{**}\setminus\mathcal{X}$ and consider $A=\ker x^{**}$.) Nevertheless, even though the argument fails, the statement is true.

**12.1. The Krein–Smulian Theorem.** *If $\mathcal{X}$ is a Banach space and $A$ is a convex subset of $\mathcal{X}^*$ such that $A\cap\{x^*\in\mathcal{X}^*:\|x^*\|\leq r\}$ is weak-star closed for every $r>0$, then $A$ is weak-star closed.*

To prove this theorem, two lemmas are needed.

**12.2. Lemma.** *If $\mathcal{X}$ is a Banach space, $r>0$, and $\mathcal{F}_r$ is the collection of all finite subsets of $\{x\in\mathcal{X}:\|x\|\leq r^{-1}\}$, then*

$$
\bigcap\{F^\circ:F\in\mathcal{F}_r\}
=\{x^*\in\mathcal{X}^*:\|x^*\|\leq r\}.
$$

**Proof.** Let $E=\bigcap\{F^\circ:F\in\mathcal{F}_r\}$; it is easy to see that $r(\operatorname{ball}\mathcal{X}^*)\subseteq E$. If $x^*\notin r(\operatorname{ball}\mathcal{X}^*)$, then there is an $x$ in $\operatorname{ball}\mathcal{X}$ such that $|\langle x,x^*\rangle|>r$. Hence $|\langle r^{-1}x,x^*\rangle|>1$ and $x^*\notin E$. $\blacksquare$

**12.3. Lemma.** *If $A$ and $\mathcal{X}$ satisfy the hypothesis of the Krein–Smulian Theorem and, moreover, $A\cap\operatorname{ball}\mathcal{X}^*=\square$, then there is an $x$ in $\mathcal{X}$ such that*

$$
\operatorname{Re}\langle x,x^*\rangle\geq1
$$

*for all $x^*$ in $A$.*

**Proof.** The proof begins by showing that there are finite subsets $F_0,F_1,\ldots$ of $\mathcal{X}$ such that

$$
\tag{12.4}
\left\{
\begin{aligned}
\text{(i)}\quad &nF_n\subseteq\operatorname{ball}\mathcal{X};\\
\text{(ii)}\quad &n(\operatorname{ball}\mathcal{X}^*)\cap
\bigcap_{k=0}^{n-1}F_k^\circ\cap A=\square.
\end{aligned}
\right.
$$

To establish (12.4) use induction as follows. Let $F_0=(0)$. Suppose that $F_0,\ldots,F_{n-1}$ have been chosen satisfying (12.4) and set $Q=[(n+1)\operatorname{ball}\mathcal{X}^*]\cap$
