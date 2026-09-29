(c) We have $A\subseteq A^*$. If $\operatorname{dom}A=\mathcal H$, then $A=A^*$ and so $A$ is closed. By the Closed Graph Theorem $A\in\mathcal B(\mathcal H)$.

(d) If $\operatorname{ran}A=\mathcal H$, then $A$ is injective by (a). Let $B=A^{-1}$ with $\operatorname{dom}B=\operatorname{ran}A=\mathcal H$. If $f=Ag$ and $h=Ak$, with $g,k$ in $\operatorname{dom}A$, then $\langle Bf,h\rangle=\langle g,Ak\rangle=\langle Ag,k\rangle=\langle f,k\rangle=\langle f,Bh\rangle$. Hence $B$ is symmetric. By (c), $B=B^*\in\mathcal B(\mathcal H)$. By (b), $A=B^{-1}$ is self-adjoint. $\blacksquare$

We now will turn our attention to the spectral properties of symmetric and self-adjoint operators. In particular, it will be seen that symmetric operators can have nonreal numbers in their spectra, though the nature of the spectrum can be completely diagnosed (2.8). Self-adjoint operators, however, must have real spectra. The next result begins this spectral discussion.

**2.5. Proposition.** *Let $A$ be a symmetric operator and let $\lambda=\alpha+i\beta$, $\alpha$ and $\beta$ real numbers.*

(a) *For each $f$ in $\operatorname{dom}A$, $\|(A-\lambda)f\|^2=\|(A-\alpha)f\|^2+\beta^2\|f\|^2$.*

(b) *If $\beta\ne0$, $\ker(A-\lambda)=(0)$.*

(c) *If $A$ is closed and $\beta\ne0$, $\operatorname{ran}(A-\lambda)$ is closed.*

**Proof.** Note that

$$
\begin{aligned}
\|(A-\lambda)f\|^2
&=\|(A-\alpha)f-i\beta f\|^2\\
&=\|(A-\alpha)f\|^2+2\operatorname{Re}i\langle(A-\alpha)f,\beta f\rangle+\beta^2\|f\|^2.
\end{aligned}
$$

But

$$
\langle(A-\alpha)f,\beta f\rangle
=\beta\langle Af,f\rangle-\alpha\beta\|f\|^2\in\mathbb R,
$$

so (a) follows. Part (b) is immediate from (a). To prove (c), note that $\|(A-\lambda)f\|^2\geqslant\beta^2\|f\|^2$. Let $\{f_n\}\subseteq\operatorname{dom}A$ such that $(A-\lambda)f_n\to g$. The preceding inequality implies that $\{f_n\}$ is a Cauchy sequence in $\mathcal H$; let $f=\lim f_n$. But $f_n\oplus(A-\lambda)f_n\in\operatorname{gra}(A-\lambda)$ and $f_n\oplus(A-\lambda)f_n\to f\oplus g$. Hence $f\oplus g\in\operatorname{gra}(A-\lambda)$ and so $g=(A-\lambda)f\in\operatorname{ran}(A-\lambda)$. This proves (c). $\blacksquare$

**2.6. Lemma.** *If $\mathcal M,\mathcal N$ are closed subspaces of $\mathcal H$ and $\mathcal M\cap\mathcal N^\perp=(0)$, then $\dim\mathcal M\leqslant\dim\mathcal N$.*

**Proof.** Let $P$ be the orthogonal projection of $\mathcal H$ onto $\mathcal N$ and define $T:\mathcal M\to\mathcal N$ by $Tf=Pf$ for $f$ in $\mathcal M$. Since $\mathcal M\cap\mathcal N^\perp=(0)$, $T$ is injective. If $\mathcal L$ is a finite dimensional subspace of $\mathcal M$, $\dim\mathcal L=\dim T\mathcal L\leqslant\dim\mathcal N$. Since $\mathcal L$ was arbitrary, $\dim\mathcal M\leqslant\dim\mathcal N$. $\blacksquare$

**2.7. Theorem.** *If $A$ is a closed symmetric operator, then $\dim\ker(A^*-\lambda)$ is constant for $\operatorname{Im}\lambda>0$ and constant for $\operatorname{Im}\lambda<0$.*

**Proof.** Let $\lambda=\alpha+i\beta$, $\alpha$ and $\beta$ real numbers and $\beta\ne0$.
