# §3. Compact Operators

The following definition generalizes the concept of a compact operator from a Hilbert space to a Banach space.

**3.1. Definition.** If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $A:\mathcal X\to\mathcal Y$ is a linear transformation, then $A$ is *compact* if $\operatorname{cl} A(\operatorname{ball}\mathcal X)$ is compact in $\mathcal Y$.

The reader should become reacquainted with Section II.4.

It is easy to see that compact operators are bounded.

For operators on a Hilbert space the following concept is equivalent to compactness, as will be seen.

**3.2. Definition.** If $\mathcal X$ and $\mathcal Y$ are Banach spaces and $A\in\mathcal B(\mathcal X,\mathcal Y)$, then $A$ is *completely continuous* if for any sequence $\{x_n\}$ in $\mathcal X$ such that $x_n\to x$ weakly it follows that $\|Ax_n-Ax\|\to 0$.

**3.3. Proposition.** *Let $\mathcal X$ and $\mathcal Y$ be Banach spaces and let $A\in\mathcal B(\mathcal X,\mathcal Y)$.*

(a) *If $A$ is a compact operator, then $A$ is completely continuous.*

(b) *If $\mathcal X$ is reflexive and $A$ is completely continuous, then $A$ is compact.*

**Proof.** (a) Let $\{x_n\}$ be a sequence in $\mathcal X$ such that $x_n\to 0$ weakly. By the PUB, $M=\sup_n\|x_n\|<\infty$. Without loss of generality, it may be assumed that $M\leq 1$. Hence $\{Ax_n\}\subseteq\operatorname{cl}A(\operatorname{ball}\mathcal X)$. Since $A$ is compact, there is a subsequence $\{x_{n_k}\}$ and a $y$ in $\mathcal Y$ such that $\|Ax_{n_k}-y\|\to 0$. But $x_{n_k}\to 0$ (wk) and $A:(\mathcal X,\mathrm{wk})\to(\mathcal Y,\mathrm{wk})$ is continuous (1.1c). Hence $Ax_{n_k}\to A(0)=0$ (wk). Thus $y=0$. Since $0$ is the unique cluster point of $\{Ax_n\}$ and this sequence is contained in a compact set, $\|Ax_n\|\to 0$.

(b) First assume that $\mathcal X$ is separable; so $(\operatorname{ball}\mathcal X,\mathrm{wk})$ is a compact metric space. So if $\{x_n\}$ is a sequence in $\operatorname{ball}\mathcal X$ there is an $x$ in $\mathcal X$ and a subsequence $\{x_{n_k}\}$ such that $x_{n_k}\to x$ weakly. Since $A$ is completely continuous, $\|Ax_{n_k}-Ax\|\to 0$. Thus $A(\operatorname{ball}\mathcal X)$ is sequentially compact; that is, $A$ is a compact operator.

Now let $\mathcal X$ be arbitrary and let $\{x_n\}\subseteq\operatorname{ball}\mathcal X$. If $\mathcal X_1=$ the closed linear span of $\{x_n\}$, then $\mathcal X_1$ is separable and reflexive. If $A_1=A|_{\mathcal X_1}$, then $A_1:\mathcal X_1\to\mathcal Y$ is easily seen to be completely continuous. By the first paragraph, $A_1$ is compact. Thus $\{Ax_n\}=\{A_1x_n\}$ has a convergent subsequence. Since $\{x_n\}$ was arbitrary, $A$ is a compact operator. $\blacksquare$

In the proof of (3.3b), the fact that $A(\operatorname{ball}\mathcal X)$ is compact, and hence closed, is a consequence of the reflexivity of $\mathcal X$.

By Proposition V.5.2, every operator in $\mathcal B(l^1)$ is completely continuous. However, there are noncompact operators in $\mathcal B(l^1)$ (for example, the identity operator).

There has been relatively little study of completely continuous operators
