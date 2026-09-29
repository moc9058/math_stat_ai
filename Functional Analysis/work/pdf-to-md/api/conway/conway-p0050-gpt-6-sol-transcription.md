(b) $\|Ah\|=\|A^*h\|$ for all $h$.

If $\mathcal H$ is a $\mathbb C$-Hilbert space, then these statements are also equivalent to:

(c) The real and imaginary parts of $A$ commute.

**Proof.** If $h\in\mathcal H$, then $\|Ah\|^2-\|A^*h\|^2=\langle Ah,Ah\rangle-\langle A^*h,A^*h\rangle=\langle(A^*A-AA^*)h,h\rangle$. Since $A^*A-AA^*$ is hermitian, the equivalence of (a) and (b) follows from Corollary 2.14.

If $B,C$ are real and imaginary parts of $A$, then a calculation yields

$$
A^*A=B^2-iCB+iBC+C^2,
$$

$$
AA^*=B^2+iCB-iBC+C^2.
$$

Hence $A^*A=AA^*$ if and only if $CB=BC$, and so (a) and (c) are equivalent. $\blacksquare$

**2.17. Proposition.** *If $A\in\mathcal B(\mathcal H)$, the following statements are equivalent.*

(a) $A$ is an isometry.

(b) $A^*A=I$.

(c) $\langle Ah,Ag\rangle=\langle h,g\rangle$ for all $h,g$ in $\mathcal H$.

**Proof.** The proof that (a) and (c) are equivalent was seen in Proposition I.5.2. Note that if $h,g\in\mathcal H$, then $\langle A^*Ah,g\rangle=\langle Ah,Ag\rangle$. Hence (b) and (c) are easily seen to be equivalent. $\blacksquare$

**2.18. Proposition.** *If $A\in\mathcal B(\mathcal H)$, then the following statements are equivalent.*

(a) $A^*A=AA^*=I$.

(b) $A$ is unitary. (That is, $A$ is a surjective isometry.)

(c) $A$ is a normal isometry.

**Proof.** (a)$\Rightarrow$(b): Proposition I.5.2.

(b)$\Rightarrow$(c): By (2.17), $A^*A=I$. But it is easy to see that the fact that $A$ is a surjective isometry implies that $A^{-1}$ is also. Hence by (2.17) $I=(A^{-1})^*A^{-1}=(A^*)^{-1}A^{-1}=(AA^*)^{-1}$; this implies that $A^*A=AA^*=I$.

(c)$\Rightarrow$(a): By (2.17), $A^*A=I$. Since $A$ is also normal, $AA^*=A^*A=I$ and so $A$ is surjective. $\blacksquare$

We conclude with a very important, though easily proved, result.

**2.19. Theorem.** *If $A\in\mathcal B(\mathcal H)$, then $\ker A=(\operatorname{ran}A^*)^\perp$.*

**Proof.** If $h\in\ker A$ and $g\in\mathcal H$, then $\langle h,A^*g\rangle=\langle Ah,g\rangle=0$, so $\ker A\subseteq(\operatorname{ran}A^*)^\perp$. On the other hand, if $h\perp\operatorname{ran}A^*$ and $g\in\mathcal H$, then $\langle Ah,g\rangle=\langle h,A^*g\rangle=0$; so $(\operatorname{ran}A^*)^\perp\subseteq\ker A$. $\blacksquare$

Two facts should be noted. Since $A^{**}=A$, it also holds that $\ker A^*=(\operatorname{ran}A)^\perp$. Second, it is not true that $(\ker A)^\perp=\operatorname{ran}A^*$ since $\operatorname{ran}A^*$ may not
