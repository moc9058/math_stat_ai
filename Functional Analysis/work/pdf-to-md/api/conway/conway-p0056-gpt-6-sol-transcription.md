# §4. Compact Operators

It turns out that most of the statements about linear transformations on finite dimensional spaces have nice generalizations to a certain class of operators on infinite dimensional spaces—namely, to the compact operators. Let ball $\mathcal H$ denote the closed unit ball in $\mathcal H$.

**4.1. Definition.** A linear transformation $T:\mathcal H\to\mathcal K$ is *compact* if $T(\text{ball }\mathcal H)$ has compact closure in $\mathcal K$. The set of compact operators from $\mathcal H$ into $\mathcal K$ is denoted by $\mathcal B_0(\mathcal H,\mathcal K)$, and $\mathcal B_0(\mathcal H)=\mathcal B_0(\mathcal H,\mathcal H)$.

**4.2. Proposition.**  
(a) $\mathcal B_0(\mathcal H,\mathcal K)\subseteq\mathcal B(\mathcal H,\mathcal K)$.

(b) $\mathcal B_0(\mathcal H,\mathcal K)$ is a linear space and if $\{T_n\}\subseteq\mathcal B_0(\mathcal H,\mathcal K)$ and $T\in\mathcal B(\mathcal H,\mathcal K)$ such that $\|T_n-T\|\to0$, then $T\in\mathcal B_0(\mathcal H,\mathcal K)$.

(c) If $A\in\mathcal B(\mathcal H)$, $B\in\mathcal B(\mathcal K)$, and $T\in\mathcal B_0(\mathcal H,\mathcal K)$, then $TA$ and $BT\in\mathcal B_0(\mathcal H,\mathcal K)$.

**Proof.** (a) If $T\in\mathcal B_0(\mathcal H,\mathcal K)$, then $\operatorname{cl}[T(\text{ball }\mathcal H)]$ is compact in $\mathcal K$. Hence there is a constant $C>0$ such that $T(\text{ball }\mathcal H)\subseteq\{k\in\mathcal K:\|k\|\leq C\}$. Thus $\|T\|\leq C$.

(b) It is left to the reader to show that $\mathcal B_0(\mathcal H,\mathcal K)$ is a linear space. For the second part of (b), it will be shown that $T(\text{ball }\mathcal H)$ is totally bounded. Since $\mathcal K$ is a complete metric space, this is equivalent to showing that $T(\text{ball }\mathcal H)$ has compact closure. Let $\varepsilon>0$ and choose $n$ such that $\|T-T_n\|<\varepsilon/3$. Since $T_n$ is compact, there are vectors $h_1,\ldots,h_m$ in ball $\mathcal H$ such that $T_n(\text{ball }\mathcal H)\subseteq\bigcup_{j=1}^{m}B(T_nh_j;\varepsilon/3)$. So if $\|h\|\leq1$, there is an $h_j$ with $\|T_nh_j-T_nh\|<\varepsilon/3$. Thus

$$
\begin{aligned}
\|Th_j-Th\|
&\leq \|Th_j-T_nh_j\|+\|T_nh_j-T_nh\|+\|T_nh-Th\|\\
&<2\|T-T_n\|+\varepsilon/3\\
&<\varepsilon.
\end{aligned}
$$

Hence $T(\text{ball }\mathcal H)\subseteq\bigcup_{j=1}^{m}B(Th_j;\varepsilon)$.

The proof of (c) is left to the reader. $\blacksquare$

**4.3. Definition.** An operator $T$ on $\mathcal H$ has *finite rank* if $\operatorname{ran}T$ is finite dimensional. The set of continuous finite rank operators is denoted by $\mathcal B_{00}(\mathcal H,\mathcal K)$; $\mathcal B_{00}(\mathcal H)=\mathcal B_{00}(\mathcal H,\mathcal H)$.

It is easy to see that $\mathcal B_{00}(\mathcal H,\mathcal K)$ is a linear space and $\mathcal B_{00}(\mathcal H,\mathcal K)\subseteq\mathcal B_0(\mathcal H,\mathcal K)$ (Exercise 2). Before giving other examples of compact operators, however, the next result should be proved.

**4.4. Theorem.** If $T\in\mathcal B(\mathcal H,\mathcal K)$, the following statements are equivalent.

(a) $T$ is compact.

(b) $T^*$ is compact.

(c) There is a sequence $\{T_n\}$ of operators of finite rank such that $\|T-T_n\|\to0$.
