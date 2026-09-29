**5.4. Theorem.** *If $\mathcal X,\mathcal Y$ are Banach spaces and $T\in\mathcal B(\mathcal X,\mathcal Y)$, then $T$ is weakly compact if and only if there is a reflexive space $\mathcal R$ and operators $A$ in $\mathcal B(\mathcal R,\mathcal Y)$ and $B$ in $\mathcal B(\mathcal X,\mathcal R)$ such that $T=AB$.*

**Proof.** If $T=AB$, where $A$, $B$ have the described form, then $T$ is weakly compact by Proposition 5.2.

Now assume that $T$ is weakly compact and put $W=T(\operatorname{ball}\mathcal X)$. Define $\mathcal R$ as in Lemma 5.3. By (5.3d), $\mathcal R$ is reflexive. Let $A:\mathcal R\to\mathcal Y$ be the inclusion map. Note that if $x\in\operatorname{ball}\mathcal X$, then $Tx\in W$. By (5.3a), $\lVert\!\lVert\!\lVert Tx\rVert\!\rVert\!\rVert<1$ whenever $\lVert x\rVert\leqslant1$. So $B:\mathcal X\to\mathcal R$ defined by $Bx=Tx$ is a bounded operator. Clearly $AB=T$. ■

The preceding result can be used to prove several standard results from antiquity.

**5.5. Theorem.** *If $\mathcal X,\mathcal Y$ are Banach spaces and $T\in\mathcal B(\mathcal X,\mathcal Y)$, the following statements are equivalent.*

(a) $T$ is weakly compact.

(b) $T^{**}(\mathcal X^{**})\subseteq\mathcal Y$.

(c) $T^*$ is weakly compact.

**Proof.** (a)$\Rightarrow$(b): Let $\mathcal R$ be a reflexive space, $A\in\mathcal B(\mathcal R,\mathcal Y)$, and $B\in\mathcal B(\mathcal X,\mathcal R)$ such that $T=AB$. So $T^{**}=A^{**}B^{**}$. But $A^{**}:\mathcal R\to\mathcal Y^{**}$ since $\mathcal R^{**}=\mathcal R$. Hence $A^{**}=A$. Thus $T^{**}=AB^{**}$, and so $\operatorname{ran}T^{**}\subseteq\operatorname{ran}A\subseteq\mathcal Y$.

(b)$\Rightarrow$(a): $T^{**}(\operatorname{ball}\mathcal X^{**})$ is $\sigma(\mathcal Y^{**},\mathcal Y^*)$ compact by Alaoglu’s Theorem and the weak* continuity of $T^{**}$. By (b), $T^{**}(\operatorname{ball}\mathcal X^{**})=C$ is $\sigma(\mathcal Y,\mathcal Y^*)$ compact in $\mathcal Y$. Hence $T(\operatorname{ball}\mathcal X)\subseteq C$ and must have weakly compact closure.

(c)$\Rightarrow$(a): Let $\mathcal S$ be a reflexive space, $C\in\mathcal B(\mathcal Y^*,\mathcal S)$, $D\in\mathcal B(\mathcal S,\mathcal X^*)$ such that $T^*=DC$. So $T^{**}=C^*D^*$, $D^*:\mathcal X^{**}\to\mathcal S^*$, and $C^*:\mathcal S^*\to\mathcal Y^{**}$. Put $\mathcal R=\operatorname{cl}D^*(\mathcal X)$ and $B=D^*|_{\mathcal X}$; then $B:\mathcal X\to\mathcal R$ and $\mathcal R$ is reflexive. Let $A=C^*|_{\mathcal R}$; so $A:\mathcal R\to\mathcal Y^{**}$. But if $x\in\mathcal X$, $ABx=C^*D^*x=T^{**}x=Tx\in\mathcal Y$. Thus $A:\mathcal R\to\mathcal Y$. Clearly $AB=T$.

(a)$\Rightarrow$(c): Exercise. ■

## Exercises

1. Prove Proposition 5.2.

2. If $\mathcal R$ and $\mathcal X$ are Banach spaces and $\Phi:\mathcal R\to\mathcal X$ is an isometry, give an elementary proof that $\Phi^*$ is surjective.

3. Let $\mathcal X$ be a Banach space and recall the definition of a weakly Cauchy sequence (V.4.4). (a) Show that every bounded sequence in $c_0$ has a weakly Cauchy subsequence, but not every weakly Cauchy sequence in $c_0$ converges. (b) Show that if $T\in\mathcal B(c_0)$ and $T$ is weakly compact, then $T$ is compact.

4. Say that a Banach space $\mathcal X$ is *weakly compactly generated* (WCG) if there is a weakly compact subset $K$ of $\mathcal X$ such that $\mathcal X$ is the closed linear span of $K$. Prove
