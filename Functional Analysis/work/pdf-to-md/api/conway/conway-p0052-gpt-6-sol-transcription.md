If $\mathcal M\leq\mathcal H$, then $P_{\mathcal M}$ is a projection (Theorem I.2.7). It is not difficult to construct an idempotent that is not a projection (Exercise 1).

Let $E$ be any idempotent and set $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$. Since $E$ is continuous, $\mathcal N$ is a closed subspace of $\mathcal H$. Notice that $(I-E)^2=I-2E+E^2=I-2E+E=I-E$; thus $I-E$ is also an idempotent. Also, $0=(I-E)h=h-Eh$, if and only if $Eh=h$. So $\operatorname{ran}E\supseteq\ker(I-E)$. On the other hand, if $h\in\operatorname{ran}E$, $h=Eg$ and so $Eh=E^2g=Eg=h$; hence $\operatorname{ran}E=\ker(I-E)$. Similarly, $\operatorname{ran}(I-E)=\ker E$. These facts are recorded here.

**3.2. Proposition.** (a) $E$ is an idempotent if and only if $I-E$ is an idempotent. (b) $\operatorname{ran}E=\ker(I-E)$, $\ker E=\operatorname{ran}(I-E)$, and both $\operatorname{ran}E$ and $\ker E$ are closed linear subspaces of $\mathcal H$. (c) If $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$, then $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal H$.

The proof of part (c) is left as an exercise. There is also a converse to (c). If $\mathcal M,\mathcal N\leq\mathcal H$, $\mathcal M\cap\mathcal N=(0)$, and $\mathcal M+\mathcal N=\mathcal H$, then there is an idempotent $E$ such that $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$; moreover, $E$ is unique. The difficult part in proving this converse is to show that $E$ is bounded. The same fact is true in more generality (for Banach spaces) and so this proof will be postponed.

Now we turn our attention to projections, which are peculiar to Hilbert space.

**3.3. Proposition.** If $E$ is an idempotent on $\mathcal H$ and $E\neq0$, the following statements are equivalent.

(a) $E$ is a projection.

(b) $E$ is the orthogonal projection of $\mathcal H$ onto $\operatorname{ran}E$.

(c) $\|E\|=1$.

(d) $E$ is hermitian.

(e) $E$ is normal.

(f) $\langle Eh,h\rangle\geq0$ for all $h$ in $\mathcal H$.

**PROOF.** $(a)\Rightarrow(b)$: Let $\mathcal M=\operatorname{ran}E$ and $P=P_{\mathcal M}$. If $h\in\mathcal H$, $Ph=$ the unique vector in $\mathcal M$ such that $h-Ph\in\mathcal M^\perp=(\operatorname{ran}E)^\perp=\ker E$ by (a). But $h-Eh=(I-E)h\in\ker E$. Hence $Eh=Ph$ by uniqueness.

$(b)\Rightarrow(c)$: By (I.2.7), $\|E\|\leq1$. But $Eh=h$ for $h$ in $\operatorname{ran}E$, so $\|E\|=1$.

$(c)\Rightarrow(a)$: Let $h\in(\ker E)^\perp$. Now $\operatorname{ran}(I-E)=\ker E$, so $h-Eh\in\ker E$. Hence $0=\langle h-Eh,h\rangle=\|h\|^2-\langle Eh,h\rangle$. Hence $\|h\|^2=\langle Eh,h\rangle\leq\|Eh\|\|h\|\leq\|h\|^2$. So for $h$ in $(\ker E)^\perp$, $\|Eh\|=\|h\|=\langle Eh,h\rangle^{1/2}$. But then for $h$ in $(\ker E)^\perp$,

$$
\|h-Eh\|^2=\|h\|^2-2\operatorname{Re}\langle Eh,h\rangle+\|Eh\|^2=0.
$$

That is, $(\ker E)^\perp\subseteq\ker(I-E)=\operatorname{ran}E$. On the other hand, if $g\in\operatorname{ran}E$, $g=g_1+g_2$, where $g_1\in\ker E$ and $g_2\in(\ker E)^\perp$. Thus $g=Eg=Eg_2=g_2$; that is, $\operatorname{ran}E\subseteq(\ker E)^\perp$. Therefore $\operatorname{ran}E=(\ker E)^\perp$ and $E$ is a projection.
