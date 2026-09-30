of $B$ to $\mathcal H_1'$. Clearly $B_1$ is invertible. If $P$ is the orthogonal projection of $\mathcal H'$ onto $\mathcal H_1'$, let $A_1:\mathcal H\to\mathcal H_1'$ be defined by $A_1=PA$. Now both $P$ and $A$ are left semi-Fredholm, so $A_1$ is left semi-Fredholm as was established at the opening of the proof.

Note that Lemma 3.6(b) implies that $\dim(\operatorname{ran}A+\ker B)^\perp=\infty$. But $(\operatorname{ran}A_1)^\perp=\ker A_1^*=\ker A^*P=\ker B+(\ker A^*)\cap(\ker B)^\perp=\ker B+(\operatorname{ran}A+\ker B)^\perp$ and so $\operatorname{ind}A_1=-\infty$. According to Case 3, $\operatorname{ind}B_1A_1=-\infty$.

This is equivalent to the condition that $\infty=\dim(\operatorname{ran}B_1A_1)^\perp=\dim(\mathcal H_1''\cap[B(\operatorname{ran}A_1)]^\perp)$. But $B(\operatorname{ran}A_1)=BP(\operatorname{ran}A)=B(\operatorname{ran}A)=\operatorname{ran}BA$ and so $\mathcal H_1''\cap[B(\operatorname{ran}A_1)]^\perp\subseteq(\operatorname{ran}BA)^\perp$. Thus $\operatorname{ind}BA=-\infty$. ■

**3.8. Corollary.** *If $A\in\mathcal F_\ell$ and $R$ is an invertible operator, then $RAR^{-1}\in\mathcal F_\ell$ and $\operatorname{ind}RAR^{-1}=\operatorname{ind}A$.*

Before going further, let’s look at some examples.

**3.9. Example.** Let $S$ be the unilateral shift of multiplicity $\alpha$. We saw in Example 2.2 that $S$ is left semi-Fredholm. It is easy to calculate that $\operatorname{ind}S=-\alpha$. According to the preceding theorem, $\operatorname{ind}S^2=-2\alpha$. But, of course, $S^2$ is the unilateral shift of multiplicity $2\alpha$.

**3.10. Example.** Let $S$ be the unilateral shift of multiplicity $\alpha$ on the Hilbert space $\mathcal H$ and put $A=S\oplus S^*$. Note that $\ker A=(0)\oplus\ker S^*$ and $\operatorname{ran}A=(\operatorname{ran}S)\oplus\mathcal H$. Thus $A$ has closed range. The operator $A$, however, is semi-Fredholm if and only if $\alpha<\infty$, in which case $A$ is a Fredholm operator. Also when $\alpha<\infty$, $\operatorname{ind}A=0$.

**3.11. Theorem.** *If $A:\mathcal H\to\mathcal H'$ is a left (respectively, right) semi-Fredholm operator and $K:\mathcal H\to\mathcal H'$ is a compact operator, then $A+K$ is left (respectively, right) semi-Fredholm and $\operatorname{ind}A=\operatorname{ind}(A+K)$.*

**Proof.** Assume that $A$ is a left semi-Fredholm operator. By definition there is an operator $X:\mathcal H'\to\mathcal H$ and a compact operator $K_0:\mathcal H\to\mathcal H$ such that $XA=1+K_0$. Thus $X(A+K)=1+(K_0+XK)$ and so $A+K$ is left semi-Fredholm.

To verify that $\operatorname{ind}A=\operatorname{ind}(A+K)$, first assume that $A$ is Fredholm. So there is a Fredholm operator $X$ and a compact operator $L$ such that $XA=1+L$. But Theorem 3.7 implies that $XA$ is Fredholm and, using Proposition 3.3, $0=\operatorname{ind}(1+L)=\operatorname{ind}A+\operatorname{ind}X$; so $\operatorname{ind}A=-\operatorname{ind}X$. But $X(A+K)=1+(L+XK)$ and so the same type of reasoning implies that $\operatorname{ind}(A+K)=-\operatorname{ind}X=\operatorname{ind}A$.

Now assume that $A$ is left semi-Fredholm; so $A+K$ is also left semi-Fredholm. If $\operatorname{ind}A$ is finite, then $A$ is Fredholm and we are done by the preceding paragraph. If $\operatorname{ind}A$ is $-\infty$, then $\operatorname{ind}(A+K)$ must also be $-\infty$ for otherwise $A+K$ is Fredholm and it follows that $A=(A+K)-K$ is also Fredholm, a contradiction. ■
