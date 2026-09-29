§1. The Adjoint of a Linear Operator　　　　　　　　　　　　　　　　　169

This enables us to prove the converse of Proposition 1.4c.

**1.9. Proposition.** *If $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$, then $A$ is invertible if and only if $A^*$ is invertible.*

**Proof.** In light of (1.4c) it suffices to assume that $A^*$ is invertible and show that $A$ is invertible. Since $A^*$ is an open mapping, there is a constant $c>0$ such that $A^*(\operatorname{ball}\mathcal{Y}^*)\supseteq\{x^*\in\mathcal{X}^*:\|x^*\|\leq c\}$. So if $x\in\mathcal{X}$, then

$$
\begin{aligned}
\|Ax\|
&=\sup\{|\langle Ax,y^*\rangle|:y^*\in\operatorname{ball}\mathcal{Y}^*\}\\
&=\sup\{|\langle x,A^*y^*\rangle|:y^*\in\operatorname{ball}\mathcal{Y}^*\}\\
&\geq\sup\{|\langle x,x^*\rangle|:x^*\in\mathcal{X}^*\text{ and }\|x^*\|\leq c\}\\
&=c^{-1}\|x\|.
\end{aligned}
$$

Thus $\ker A=(0)$ and $\operatorname{ran}A$ is closed. (Why?) On the other hand, $(\operatorname{ran}A)^\perp=\ker A^*=(0)$ since $A^*$ is invertible. Thus $\operatorname{ran}A$ is also dense. This implies that $A$ is surjective and thus invertible. $\blacksquare$

This section concludes with the following useful result that seems to be somewhat unfamiliar to parts of the mathematical community.

**1.10. Theorem.** *If $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces and $A\in\mathcal{B}(\mathcal{X},\mathcal{Y})$, then the following statements are equivalent.*

(a) $\operatorname{ran}A$ *is closed.*  
(b) $\operatorname{ran}A^*$ *is weak$^*$ closed.*  
(c) $\operatorname{ran}A^*$ *is norm closed.*

**Proof.** It is clear that (b) implies (c), so it will be shown that (a) implies (b) and (c) implies (a). Before this is done, it will be shown that it suffices to prove the theorem under the additional hypothesis that $A$ is injective and has dense range.

Let $\mathcal{L}=\operatorname{cl}(\operatorname{ran}A)$. Thus $A:\mathcal{X}\to\mathcal{L}$ induces a bounded linear map $B:\mathcal{X}/\ker A\to\mathcal{L}$ defined by $B(x+\ker A)=Ax$. If $Q:\mathcal{X}\to\mathcal{X}/\ker A$ is the natural map, the diagram

$$
\begin{array}{ccccc}
\mathcal{X}&\xrightarrow{\ A\ }&\mathcal{L}&\hookrightarrow&\mathcal{Y}\\
{\scriptstyle Q}\searrow&&\nearrow{\scriptstyle B}&&\\
&\mathcal{X}/\ker A&&&
\end{array}
$$

commutes. (Why is $B$ bounded?) It is easy to see that $B$ is injective and that $B$ has dense range. In fact, $\operatorname{ran}B=\operatorname{ran}A$, so $\operatorname{ran}A$ is closed if and only if $\operatorname{ran}B$ is closed. Let’s examine $B^*:\mathcal{L}^*\to(\mathcal{X}/\ker A)^*$. By (V.2.2), $(\mathcal{X}/\ker A)^*=(\ker A)^\perp=\operatorname{wk}^*\operatorname{cl}(\operatorname{ran}A^*)\subseteq\mathcal{X}^*$ by (1.8). Also by (V.2.3), since $\mathcal{L}\leq\mathcal{Y}$, $\mathcal{L}^*=\mathcal{Y}^*/\mathcal{L}^\perp=\mathcal{Y}^*/(\operatorname{ran}A)^\perp=\mathcal{Y}^*/\ker A^*$ by (1.8). Thus,

$$
B^*:\mathcal{Y}^*/\ker A^*\to(\ker A)^\perp.
$$
