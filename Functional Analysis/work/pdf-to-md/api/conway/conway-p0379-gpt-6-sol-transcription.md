(b) $\gamma(A)=\sup\{\gamma:\|Ah\|\geq\gamma\|h\|\text{ for all }h\text{ in }(\ker A)^\perp\}=\inf\{\|Ah\|/\|h\|:h\in(\ker A)^\perp\setminus\{0\}\}$.

**6.2. Proposition.** If $A\in\mathcal{B}(\mathcal{H})$, then $\gamma(A)=\gamma(A^*)$.

**Proof.** Let $h\perp\ker A$. Then $\|A^*Ah\|=\||A||A|h\|=\|A|A|h\|$. But $|A|h\in\operatorname{cl}\operatorname{ran}A^*$ (Why?) $=(\ker A)^\perp$. Hence the definition of $\gamma(A)$ implies that $\|A^*Ah\|\geq\gamma(A)\||A|h\|=\gamma(A)\|Ah\|$; that is, $\|A^*f\|\geq\gamma(A)\|f\|$ for every $f$ in $\operatorname{ran}A$. Since $\operatorname{ran}A$ is dense in $(\ker A^*)^\perp$, $\gamma(A^*)\geq\gamma(A)$. But $A=A^{**}$, so $\gamma(A)\geq\gamma(A^*)$. ■

Note that the preceding two propositions give a proof of the fact that an operator on a Hilbert space has closed range if and only if its adjoint does. See Theorem VI.1.10 and Exercise 2.1.

**6.3. Lemma.** If $\mathcal{M},\mathcal{N}\leq\mathcal{H}$, $\mathcal{N}$ is finite dimensional, and $\dim\mathcal{M}>\dim\mathcal{N}$, then there is a non-zero vector $m$ in $\mathcal{M}$ such that $\|m\|=\operatorname{dist}(m,\mathcal{N})$.

**Proof.** Let $P$ be the projection of $\mathcal{H}$ onto $\mathcal{M}$, so $\dim P(\mathcal{N})\leq\dim\mathcal{N}<\dim\mathcal{M}$. Thus $P(\mathcal{N})$ is a proper subspace of $\mathcal{M}$; let $m\in\mathcal{M}\cap P(\mathcal{N})^\perp$. If $n\in\mathcal{N}$, then $0=\langle Pn,m\rangle=\langle n,Pm\rangle=\langle n,m\rangle$, so $m\perp\mathcal{N}$. Hence $\|m\|=\operatorname{dist}(m,\mathcal{N})$. ■

**6.4. Lemma.** If $h\in\mathcal{H}$, then $\gamma(A)\operatorname{dist}(h,\ker A)\leq\|Ah\|$.

**Proof.** Let $P$ be the projection of $\mathcal{H}$ onto $(\ker A)^\perp$; then $\|Ph\|=\operatorname{dist}(h,\ker A)$. Hence $\|Ah\|=\|APh\|\geq\gamma(A)\|Ph\|=\gamma(A)\operatorname{dist}(h,\ker A)$. ■

If the role of $\gamma(A)$ in the next and subsequent propositions impresses the reader as somewhat mysterious, reflect that if $A$ is invertible, then $\gamma(A)=\|A^{-1}\|^{-1}$ (Exercise 1). Now in Corollary VII.2.3, it was shown that if $\mathcal{A}$ is a Banach algebra, $a_0\in\mathcal{A}$, and $b_0a_0=1$, then $a+b$ is left invertible whenever $\|b\|<\|b_0\|^{-1}$. Of course, a similar result holds for right invertible elements. The number $\gamma(A)$ is trying to play the role of the reciprocal of the norm of a one-sided inverse.

For example, if $A$ is left invertible, then $\operatorname{ran}A$ is closed and $\ker A=(0)$; hence $A\in\mathcal{SF}$. The next result implies that if $\|B\|<\gamma(A)$, then $A+B$ is left invertible.

**6.5. Proposition.** If $A\in\mathcal{SF}$ and $B\in\mathcal{B}(\mathcal{H})$ such that $\|B\|<\gamma(A)$, then $A+B\in\mathcal{SF}$ and:

(a) $\dim\ker(A+B)\leq\dim\ker A$;

(b) $\dim\operatorname{ran}(A+B)^\perp\leq\dim\operatorname{ran}A^\perp$.

**Proof.** First note that because $A\in\mathcal{SF}$, $\gamma(A)>0$.

If $h\in\ker(A+B)$ and $h\ne0$, then $Ah=-Bh$. By Lemma 6.4, $\gamma(A)\operatorname{dist}(h,\ker A)\leq\|Bh\|\leq\|B\|\|h\|<\gamma(A)\|h\|$. Thus $\operatorname{dist}(h,\ker A)<\|h\|$ for every nonzero vector $h$ in $\ker(A+B)$. By Lemma 6.3, (a) holds.
