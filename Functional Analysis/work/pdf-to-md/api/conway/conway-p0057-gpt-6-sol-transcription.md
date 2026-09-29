**Proof.** (c) $\Rightarrow$ (a): This is immediate from (4.2b) and the fact that $\mathcal B_{00}(\mathcal H,\mathcal K)\subseteq\mathcal B_0(\mathcal H,\mathcal K)$.

(a) $\Rightarrow$ (c): Since $\operatorname{cl}[T(\operatorname{ball}\mathcal H)]$ is compact, it is separable. Therefore $\operatorname{cl}(\operatorname{ran}T)=\mathcal L$ is a separable subspace of $\mathcal K$. Let $\{e_1,e_2,\ldots\}$ be a basis for $\mathcal L$ and let $P_n$ be the orthogonal projection of $\mathcal K$ onto $\bigvee\{e_j:1\leq j\leq n\}$. Put $T_n=P_nT$; note that each $T_n$ has finite rank. It will be shown that $\|T_n-T\|\to0$, but first we prove the following:

**Claim.** If $h\in\mathcal H$, $\|T_nh-Th\|\to0$.

In fact, $k=Th\in\mathcal L$, so $\|P_nk-k\|\to0$ by (I.4.13d) and (I.4.7). That is, $\|P_nTh-Th\|\to0$ and the claim is proved.

Since $T$ is compact, if $\varepsilon>0$, there are vectors $h_1,\ldots,h_m$ in $\operatorname{ball}\mathcal H$ such that $T(\operatorname{ball}\mathcal H)\subseteq\bigcup_{j=1}^m B(Th_j;\varepsilon/3)$. So if $\|h\|\leq1$, choose $h_j$ with $\|Th-Th_j\|<\varepsilon/3$. Thus for any integer $n$,

$$
\begin{aligned}
\|Th-T_nh\|
&\leq \|Th-Th_j\|+\|Th_j-T_nh_j\|+\|P_n(Th_j-Th)\|\\
&\leq 2\|Th-Th_j\|+\|Th_j-T_nh_j\|\\
&\leq 2\varepsilon/3+\|Th_j-T_nh_j\|.
\end{aligned}
$$

Using the claim we can find an integer $n_0$ such that $\|Th_j-T_nh_j\|<\varepsilon/3$ for $1\leq j\leq m$ and $n\geq n_0$. So $\|Th-T_nh\|<\varepsilon$ uniformly for $h$ in $\operatorname{ball}\mathcal H$. Therefore $\|T-T_n\|<\varepsilon$ for $n\geq n_0$.

(c) $\Rightarrow$ (b): If $\{T_n\}$ is a sequence in $\mathcal B_{00}(\mathcal H,\mathcal K)$ such that $\|T_n-T\|\to0$, then $\|T_n^*-T^*\|=\|T_n-T\|\to0$. But $T_n^*\in\mathcal B_{00}(\mathcal K,\mathcal H)$ (Exercise 3). Since (c) implies (a), $T^*$ is compact.

(b) $\Rightarrow$ (a): Exercise. $\blacksquare$

A fact emerged in the proof that (a) implies (c) in the preceding theorem that is worth recording.

**4.5. Corollary.** *If $T\in\mathcal B_0(\mathcal H,\mathcal K)$, then $\operatorname{cl}(\operatorname{ran}T)$ is separable and if $\{e_n\}$ is a basis for $\operatorname{cl}(\operatorname{ran}T)$ and $P_n$ is the projection of $\mathcal K$ onto $\bigvee\{e_j:1\leq j\leq n\}$, then $\|P_nT-T\|\to0$.*

**4.6. Proposition.** *Let $\mathcal H$ be a separable Hilbert space with basis $\{e_n\}$; let $\{\alpha_n\}\subseteq\mathbb F$ with $M=\sup\{|\alpha_n|:n\geq1\}<\infty$. If $Ae_n=\alpha_ne_n$ for all $n$, then $A$ extends by linearity to a bounded operator on $\mathcal H$ with $\|A\|=M$. The operator $A$ is compact if and only if $\alpha_n\to0$ as $n\to\infty$.*

**Proof.** The fact that $A$ is bounded and $\|A\|=M$ is an exercise; such an operator is said to be diagonalizable (see Exercise 1.8). Let $P_n$ be the projection of $\mathcal H$ onto $\bigvee\{e_1,\ldots,e_n\}$. Then $A_n=A-AP_n$ is seen to be diagonalizable with $A_ne_j=\alpha_je_j$ if $j>n$ and $A_ne_j=0$ if $j\leq n$. So $AP_n\in\mathcal B_{00}(\mathcal H)$ and $\|A_n\|=\sup\{|\alpha_j|:j>n\}$. If $\alpha_n\to0$, then $\|A_n\|\to0$ and so $A$ is compact since
