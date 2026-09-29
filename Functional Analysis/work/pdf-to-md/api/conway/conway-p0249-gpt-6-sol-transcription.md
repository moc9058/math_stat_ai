is a $*$-homomorphism, then $v_1:\mathcal A_1\to\mathcal C$, defined by $v_1(a+\alpha)=v(a)+\alpha$ for $a$ in $\mathcal A$ and $\alpha$ in $\mathbb C$, is a $*$-homomorphism.

**Proof.** It may be assumed that $\mathcal A$ does not have an identity. Let $\mathcal A_1=\{a+\alpha:a\in\mathcal A,\alpha\in\mathbb C\}$ ($a+\alpha$ is just a formal sum). Define multiplication and addition in the obvious way. Let $(a+\alpha)^*=a^*+\bar\alpha$ and define the norm on $\mathcal A_1$ by

$$
\|a+\alpha\|=\sup\{\|ax+\alpha x\|:x\in\mathcal A,\ \|x\|\leqslant1\}.
$$

Clearly, this is a norm on $\mathcal A_1$. It must be shown that $\|y^*y\|=\|y\|^2$ for every $y$ in $\mathcal A_1$.

Fix $a$ in $\mathcal A$ and $\alpha$ in $\mathbb C$. If $\varepsilon>0$, then there is an $x$ in $\mathcal A$ such that $\|x\|\leqslant1$ and

$$
\begin{aligned}
\|a+\alpha\|^2-\varepsilon
&<\|ax+\alpha x\|^2
 =\|(x^*a^*+\bar\alpha x^*)(ax+\alpha x)\|\\
&=\|x^*(a+\alpha)^*(a+\alpha)x\|
 \leqslant\|(a+\alpha)^*(a+\alpha)\|.
\end{aligned}
$$

Thus $\|a+\alpha\|^2\leqslant\|(a+\alpha)^*(a+\alpha)\|$.

It is left to the reader to prove that the norm on $\mathcal A_1$ makes $\mathcal A_1$ a Banach algebra. For the other inequality, note that $\|(a+\alpha)^*(a+\alpha)\|\leqslant\|(a+\alpha)^*\|\|a+\alpha\|$. So the proof will be complete if it can be shown that $\|(a+\alpha)^*\|\leqslant\|a+\alpha\|$. Now if $x,y\in\mathcal A$ and $\|x\|,\|y\|\leqslant1$, then $\|y(a+\alpha)^*x\|=\|ya^*x+\bar\alpha yx\|=\|x^*ay^*+\alpha x^*y^*\|=\|x^*(a+\alpha)y^*\|\leqslant\|a+\alpha\|$. Taking the supremum over all such $x,y$ gives the desired inequality.

It remains to prove the statement concerning the $*$-homomorphism $v$, that $v(a^*)=v(a)^*$. The details are left to the reader. $\blacksquare$

If $\mathcal A$ is a $C^*$-algebra with identity and $a\in\mathcal A$, then $\sigma(a)$, the spectrum of $a$, is well defined. If $\mathcal A$ does not have an identity, $\sigma(a)$ is defined as the spectrum of $a$ as an element of the $C^*$-algebra $\mathcal A_1$ obtained in Proposition 1.9.

**1.10. Definition.** If $\mathcal A$ is a $C^*$-algebra and $a\in\mathcal A$, then (a) $a$ is *hermitian* if $a=a^*$; (b) $a$ is *normal* if $a^*a=aa^*$; (c) $a$ is *unitary* if $a^*a=aa^*=1$ (this only makes sense if $\mathcal A$ has an identity).

**1.11. Proposition.** *Let $\mathcal A$ be a $C^*$-algebra and let $a\in\mathcal A$.*

(a) *If $a$ is invertible, then $a^*$ is invertible and $(a^*)^{-1}=(a^{-1})^*$.*

(b) *$a=x+iy$ where $x$ and $y$ are hermitian elements of $\mathcal A$.*

(c) *If $u$ is a unitary element of $\mathcal A$, $\|u\|=1$.*

(d) *If $\mathcal B$ is a $C^*$-algebra and $\rho:\mathcal A\to\mathcal B$ is a $*$-homomorphism, then $\|\rho(a)\|\leqslant\|a\|$.*

(e) *If $a=a^*$, then $\|a\|=r(a)$.*

**Proof.** The proofs of (a), (b), and (c) are left as exercises.

(e) Since $a^*=a$, $\|a^2\|=\|a^*a\|=\|a\|^2$; by induction, $\|a^{2^n}\|=\|a\|^{2^n}$ for $n\geqslant1$. That is, $\|a^{2^n}\|^{1/2^n}=\|a\|$ for $n\geqslant1$. Hence $r(a)=\lim\|a^{2^n}\|^{1/2^n}=\|a\|$.

(d) If $\mathcal A$ has an identity, it is not assumed that $\rho(1)=$ the identity of $\mathcal B$. However, it is easy to see that $\rho(1)$ is the identity for $\operatorname{cl}\rho(\mathcal A)$. If $\mathcal A$ does not have an identity, then $\rho$ can be extended to a $*$-homomorphism $\rho_1:\mathcal A_1\to\mathcal B_1$
