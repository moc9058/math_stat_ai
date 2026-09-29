that I am aware of. Most of the effort has been devoted to the study of compact operators and this is the direction we now pursue.

**3.4. Schauder’s Theorem.** If $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$, then $A$ is compact if and only if $A^*$ is compact.

**Proof.** Assume $A$ is a compact operator and let $\{y_n^*\}$ be a sequence in ball $\mathcal{Y}^*$. It must be shown that $\{A^*y_n^*\}$ has a norm convergent subsequence or, equivalently, a cluster point in the norm topology. By Alaoglu’s Theorem, there is a $y^*$ in ball $\mathcal{Y}^*$ such that $y_n^*\xrightarrow[\mathrm{cl}]{}y^*$ (weak*). It will be shown that $A^*y_n^*\xrightarrow[\mathrm{cl}]{}A^*y^*$ in norm.

Let $\varepsilon>0$ and fix $N\geqslant1$. Because $A(\operatorname{ball}\mathcal{X})$ has compact closure, there are vectors $y_1,\ldots,y_m$ in $\mathcal{Y}$ such that
$A(\operatorname{ball}\mathcal{X})\subseteq\bigcup_{k=1}^{m}\{y\in\mathcal{Y}:\|y-y_k\|<\varepsilon/3\}$.
Since $y_n^*\xrightarrow[\mathrm{cl}]{}y^*$ (weak*), there is an $n\geqslant N$ such that $|\langle y_k,y^*-y_n^*\rangle|<\varepsilon/3$ for $1\leqslant k\leqslant m$. Let $x$ be an arbitrary element in ball $\mathcal{X}$ and choose $y_k$ such that $\|Ax-y_k\|<\varepsilon/3$. Then

$$
\begin{aligned}
|\langle x,A^*y^*-A^*y_n^*\rangle|
&=|\langle Ax,y^*-y_n^*\rangle|\\
&\leqslant|\langle Ax-y_k,y^*-y_n^*\rangle|
  +|\langle y_k,y^*-y_n^*\rangle|\\
&\leqslant2\|Ax-y_k\|+\varepsilon/3<\varepsilon.
\end{aligned}
$$

Thus $\|A^*y-A^*y_n^*\|\leqslant\varepsilon$.

For the converse, assume $A^*$ is compact. By the first half of the proof, $A^{**}:\mathcal{X}^{**}\to\mathcal{Y}^{**}$ is compact. It is easy to check that $A=A^{**}|_{\mathcal{X}}$ is compact. $\blacksquare$

For Banach spaces $\mathcal{X}$ and $\mathcal{Y}$, $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ denotes the set of all compact operators from $\mathcal{X}$ into $\mathcal{Y}$; $\mathcal{B}_0(\mathcal{X})=\mathcal{B}_0(\mathcal{X},\mathcal{X})$.

**3.5. Proposition.** Let $\mathcal{X}$, $\mathcal{Y}$, and $\mathcal{Z}$ be Banach spaces.

(a) $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ is a closed linear subspace of $\mathcal{B}(\mathcal{X},\mathcal{Y})$.

(b) If $K\in\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ and $A\in\mathcal{B}(\mathcal{Y},\mathcal{Z})$, then $AK\in\mathcal{B}_0(\mathcal{X},\mathcal{Z})$.

(c) If $K\in\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ and $A\in\mathcal{B}(\mathcal{Z},\mathcal{X})$, then $KA\in\mathcal{B}_0(\mathcal{Z},\mathcal{Y})$.

The proof of (3.5) is left as an exercise.

**3.6. Corollary.** If $\mathcal{X}$ is a Banach space, $\mathcal{B}_0(\mathcal{X})$ is a closed two-sided ideal in the algebra $\mathcal{B}(\mathcal{X})$.

Let $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})=$ the bounded operators $T:\mathcal{X}\to\mathcal{Y}$ for which ran $T$ is finite dimensional. Operators in $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})$ are called operators with *finite rank*. It is easy to see that $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})\subseteq\mathcal{B}_0(\mathcal{X},\mathcal{Y})$ and by (3.5a) the closure of $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})$ is contained in $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$. Is $\mathcal{B}_{00}(\mathcal{X},\mathcal{Y})$ dense in $\mathcal{B}_0(\mathcal{X},\mathcal{Y})$?
