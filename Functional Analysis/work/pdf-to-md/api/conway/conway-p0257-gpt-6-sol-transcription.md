Clearly, $\lambda a\geq 0$ if $a\geq 0$ and $\lambda\geq 0$. Let $a,b\in\mathcal A_+$; it must be shown that $a+b\geq 0$. It suffices to assume that $\|a\|,\|b\|\leq 1$. But $\|1-\frac12(a+b)\|=\frac12\|(1-a)+(1-b)\|\leq 1$ by (3.6d). So by (3.6e), $\frac12(a+b)\geq 0$.

If $a\in\mathcal A_+\cap(-\mathcal A_+)$, then $a=a^*$ and $\sigma(a)=\{0\}$. But $\|a\|=r(a)$ (1.11e). ■

Now to look at one more example—a very important one.

**3.8. Theorem.** *If $\mathcal H$ is a Hilbert space and $A\in\mathcal B(\mathcal H)$, then $A\geq 0$ if and only if $\langle Ah,h\rangle\geq 0$ for all $h$ in $\mathcal H$.*

**PROOF.** If $A\geq 0$, then (3.6c) $A=T^*T$ for some $T$ in $\mathcal B(\mathcal H)$. Hence $\langle Ah,h\rangle=\|Th\|^2\geq 0$. Conversely, suppose $\langle Ah,h\rangle\geq 0$ for all $h$ in $\mathcal H$. By (II.2.12), $A=A^*$. It remains to show that $\sigma(A)\subseteq[0,\infty)$. If $h\in\mathcal H$ and $\lambda<0$, then

$$
\begin{aligned}
\|(A-\lambda)h\|^2
&=\|Ah\|^2-2\lambda\langle Ah,h\rangle+\lambda^2\|h\|^2\\
&\geq-2\lambda\langle Ah,h\rangle+\lambda^2\|h\|^2
\geq\lambda^2\|h\|^2
\end{aligned}
$$

since $\lambda<0$ and $\langle Ah,h\rangle\geq 0$. By (VII.6.4), $\lambda\notin\sigma_{ap}(A)$. But this implies that $A-\lambda$ is left invertible (Exercise VII.6.5). Since $A-\lambda$ is self-adjoint, $A-\lambda$ is also right invertible. Thus $\lambda\notin\sigma(A)$ and $A\geq 0$. ■

**3.9. Definition.** If $\mathcal A$ is a $C^*$-algebra and $a,b\in\operatorname{Re}\mathcal A$, then $a\leq b$ if $b-a\in\mathcal A_+$.

This ordering makes a $C^*$-algebra as well as $\operatorname{Re}\mathcal A$ into ordered vector spaces.

Note that if $A$ and $B$ are hermitian operators on the Hilbert space $\mathcal H$, then $A\leq B$ if and only if $\langle Ah,h\rangle\leq\langle Bh,h\rangle$ for all $h$ in $\mathcal H$.

This section closes with an application of positivity to obtain the polar decomposition of an operator. If $\lambda\in\mathbb C$, then $\lambda=|\lambda|e^{i\theta}$ for some $\theta$; this is the polar decomposition of $\lambda$. Can an analogue be found for operators? To answer this question we might first ask what is the analogue of $|\lambda|$ and $e^{i\theta}$ among operators. If $A\in\mathcal B(\mathcal H)$, then the proper definition for $|A|$ would seem to be $|A|\equiv(A^*A)^{1/2}$ [see (3.5)]. How about an analogue of $e^{i\theta}$? Should it be a unitary operator? An isometry? For an arbitrary operator neither of these is appropriate. The following new class of operators is needed.

**3.10. Definition.** A *partial isometry* is an operator $W$ such that for $h$ in $(\ker W)^\perp$, $\|Wh\|=\|h\|$. The space $(\ker W)^\perp$ is called the *initial space* of $W$ and the space $\operatorname{ran}W$ is called the *final space* of $W$. See Exercises 15–20 for more on partial isometries.

**3.11. Polar Decomposition.** *If $A\in\mathcal B(\mathcal H)$, then there is a partial isometry $W$ with $(\ker A)^\perp$ as its initial space and $\operatorname{cl}(\operatorname{ran}A)$ as its final space such that $A=W|A|$. Moreover, if $A=UP$ where $P\geq 0$ and $U$ is a partial isometry with $\ker U=\ker P$, then $P=|A|$ and $U=W$.*
