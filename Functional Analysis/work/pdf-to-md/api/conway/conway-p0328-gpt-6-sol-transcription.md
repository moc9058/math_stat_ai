**Proof.** Let $f\in\mathcal L_+$ and $h\in\operatorname{dom}A$. Then
$$
\begin{aligned}
\langle h\oplus Ah,f\oplus if\rangle
&=\langle h,f\rangle-i\langle Ah,f\rangle\\
&=-i\langle(A+i)h,f\rangle\\
&=0
\end{aligned}
$$
since $\mathcal L_+=[\operatorname{ran}(A+i)]^\perp$. The remainder of the proof that $\operatorname{gra}A$, $\mathcal K_+$, and $\mathcal K_-$ are pairwise orthogonal is left to the reader. Since it is clear that $\operatorname{gra}A\oplus\mathcal K_+\oplus\mathcal K_-\subseteq\operatorname{gra}A^*$, it remains to show that this direct sum is dense in $\operatorname{gra}A^*$.

Let $h\in\operatorname{dom}A^*$ and assume $h\oplus A^*h\perp\operatorname{gra}A\oplus\mathcal K_+\oplus\mathcal K_-$. Since $h\oplus A^*h\perp\operatorname{gra}A$, for every $f$ in $\operatorname{dom}A$, $0=\langle h\oplus A^*h,f\oplus Af\rangle=\langle h,f\rangle+\langle A^*h,Af\rangle$. So $\langle A^*h,Af\rangle=-\langle h,f\rangle$ for every $f$ in $\operatorname{dom}A$. This implies that $A^*h\in\operatorname{dom}A^*$ and $A^*A^*h=-h$. Therefore $(A^*-i)(A^*+i)h=(A^*A^*+1)h=0$. Thus $(A^*+i)h\in\mathcal L_+$. Reversing the order of these factors also shows that $(A^*-i)h\in\mathcal L_-$. But if $g\in\mathcal L_+$, $0=\langle h\oplus A^*h,g\oplus ig\rangle=\langle h,g\rangle-i\langle A^*h,g\rangle=-i\langle(A^*+i)h,g\rangle$. Since $g$ can be taken equal to $(A^*+i)h$, we get that $(A^*+i)h=0$, or $h\in\mathcal L_-$. Similarly, $h\in\mathcal L_+$. So $h\in\mathcal L_+\cap\mathcal L_-=(0)$. $\blacksquare$

**2.14. Definition.** If $A$ is a closed symmetric operator and $\mathcal M$ is a linear manifold in $\operatorname{dom}A^*$, then $\mathcal M$ is *$A$-symmetric* if $\langle A^*f,g\rangle=\langle f,A^*g\rangle$ for all $f,g$ in $\mathcal M$. Call such a manifold *$A$-closed* if $\{f\oplus A^*f:f\in\mathcal M\}$ is closed in $\mathcal H\oplus\mathcal H$.

So $\mathcal M$ is both $A$-symmetric and $A$-closed precisely when $A^*|_{\mathcal M}$, the restriction of $A^*$ to $\mathcal M$, is a closed symmetric operator; if $\mathcal M\supseteq\operatorname{dom}A$, then $A^*|_{\mathcal M}$ is a closed symmetric extension of $A$.

**2.15. Lemma.** *If $A$ is a closed symmetric operator on $\mathcal H$ and $B$ is a closed symmetric extension of $A$, then there is an $A$-closed, $A$-symmetric submanifold $\mathcal M$ of $\mathcal L_++\mathcal L_-$ such that*
$$
\tag{2.16}
\operatorname{gra}B=\operatorname{gra}A+\operatorname{gra}(A^*|_{\mathcal M}).
$$
*Conversely, if $\mathcal M$ is an $A$-closed, $A$-symmetric manifold in $\mathcal L_++\mathcal L_-$, then there is a closed symmetric extension $B$ of $A$ such that (2.16) holds.*

**Proof.** If the $A$-symmetric manifold $\mathcal M$ in $\mathcal L_++\mathcal L_-$ is given, let $\mathcal D=\operatorname{dom}A+\mathcal M$. Since $\mathcal D\subseteq\operatorname{dom}A^*$, $B=A^*|_{\mathcal D}$ is well defined. Let $f=f_0+f_1$, $g=g_0+g_1$, $f_0,g_0$ in $\operatorname{dom}A$ and $f_1,g_1$ in $\mathcal M$. Then
$$
\begin{aligned}
\langle A^*f,g\rangle
&=\langle A^*f_0+A^*f_1,g_0+g_1\rangle\\
&=\langle Af_0,g_0\rangle+\langle Af_0,g_1\rangle
+\langle A^*f_1,g_0\rangle+\langle A^*f_1,g_1\rangle.
\end{aligned}
$$
Using the $A$-symmetry of $\mathcal M$, the symmetry of $A$, and the definition of $A^*$ we get
$$
\begin{aligned}
\langle A^*f,g\rangle
&=\langle f_0,Ag_0\rangle+\langle f_0,A^*g_1\rangle
+\langle f_1,Ag_0\rangle+\langle f_1,A^*g_1\rangle\\
&=\langle f,A^*g\rangle.
\end{aligned}
$$
