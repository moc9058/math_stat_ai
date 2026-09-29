**3.5. Lemma.** *Let $A:\mathcal H\to\mathcal H'$, $\mathcal H=\mathcal M\oplus\mathcal N$, $\mathcal H'=\mathcal M'\oplus\mathcal N'$, and suppose $A$ has the matrix*

$$
\begin{bmatrix}
A_1 & X\\
0 & A_2
\end{bmatrix}
$$

*relative to these two decompositions of $\mathcal H$ and $\mathcal H'$. If $A_1$ is invertible and $\mathcal N$ and $\mathcal N'$ are finite dimensional, then $A$ is Fredholm and $\operatorname{ind}A=\dim\mathcal N-\dim\mathcal N'$.*

**Proof.** It is easy to see that $\operatorname{ran}A$ is closed since $\operatorname{ran}A_1=\mathcal M'$ and $\dim\mathcal N<\infty$. Let’s show that $\ker A^*=\ker A_2^*$ and $\dim(\ker A)=\dim(\ker A_2)$. If this is done, then $\operatorname{ind}A=\dim(\ker A)-\dim(\ker A^*)=\dim(\ker A_2)-\dim(\ker A_2^*)=\dim\mathcal N-\dim\mathcal N'$ by Proposition 3.2.

For the first of the two desired equalities, let $f'\in\mathcal M'$ and $g'\in\mathcal N'$. Then $A^*(f'\oplus g')=A_1^*f'\oplus(X^*f'+A_2^*g')$. So $f'\oplus g'\in\ker A^*$ if and only if $A_1^*f'=0$ and $A_2^*g'=-X^*f'$. But $A_1$ is invertible, so this happens exactly when $f'=0$, and hence $A_2^*g'=0$. From here it is clear that $\ker A^*=\ker A_2^*$. For the second equality, note that $g\to-A_1^{-1}Xg\oplus g$ is a bijection between $\ker A_2$ and $\ker A$. $\blacksquare$

The second lemma is elementary and its proof is left to the reader.

**3.6. Lemma.** *Let $\mathcal M$ and $\mathcal N$ be two closed subspaces of the Hilbert space $\mathcal H$.*

(a) *If $\mathcal M\cap\mathcal N=(0)$ and $\dim\mathcal N=\infty$, then $\dim\mathcal M^\perp=\infty$.*

(b) *If $\dim\mathcal M^\perp=\infty$ and $\dim\mathcal N<\infty$, then $\dim(\mathcal M+\mathcal N)^\perp<\infty$.*

**3.7. Theorem.** *If $A:\mathcal H\to\mathcal H'$ and $B:\mathcal H'\to\mathcal H''$ are left semi-Fredholm operators, then $BA$ is a left semi-Fredholm operator and $\operatorname{ind}BA=\operatorname{ind}A+\operatorname{ind}B$.*

**Proof.** By definition, there are operators $X$ and $Y$ such that $XA=1+K$ and $YB=1+K'$, where $K$ and $K'$ are compact operators on the appropriate spaces. Hence $(XY)(BA)=X(1+K')A=1+(K+XK'A)$, and $K+XK'A$ is compact. Therefore $BA$ is left semi-Fredholm.

To prove the formula for the index, we consider 4 cases.

**Case 1.** Both $A$ and $B$ are Fredholm.

Let $\mathcal M'=(\operatorname{ran}A)\cap(\ker B)^\perp$ and put $\mathcal N'=\mathcal M'^\perp$.

**Claim 1:** $\mathcal N'$ is finite dimensional.

To see this note that $\mathcal N'=\mathcal M'^\perp=(\operatorname{ran}A)^\perp\vee(\ker B)$. Since both of these spaces are finite dimensional, so is $\mathcal N'$. Let $\mathcal M=A^{-1}(\mathcal M')\cap(\ker A)^\perp$; $\mathcal N=\mathcal M^\perp$; $\mathcal M''=B\mathcal M'$; $\mathcal N''=\mathcal M''^\perp$. Note the following: $A(\mathcal M)=\mathcal M'$; $A|_{\mathcal M}$ is invertible (because $\ker(A|_{\mathcal M})=\ker A\cap\mathcal M=(0)$); $B|_{\mathcal M'}$ is invertible.
