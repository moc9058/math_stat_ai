(d) $\bar{\lambda}\notin\sigma_r(A^*)$.

(e) $\operatorname{ran}(A^*-\bar{\lambda})=\mathcal H$.

**Proof.** By Proposition VII.6.4, (a) and (b) are equivalent. Also, if $B\in\mathcal B(\mathcal H)$, then $B(A-\lambda)=1$ if and only if $(A^*-\bar{\lambda})B^*=1$ so that (c) and (d) are easily seen to be equivalent.

*(b) implies (c).* Let $\mathcal M=\operatorname{ran}(A-\lambda)$ and define $T:\mathcal H\to\mathcal M$ by $Th=(A-\lambda)h$; then $T$ is bijective. By the Open Mapping Theorem, $T^{-1}:\mathcal M\to\mathcal H$ is continuous. Define $B:\mathcal H\to\mathcal H$ by letting $B=T^{-1}$ on $\mathcal M$ and $B=0$ on $\mathcal M^\perp$. Then $B\in\mathcal B(\mathcal H)$ and $B(A-\lambda)=1$. (Note that we used a property of Hilbert spaces here; see Exercise VII.6.5.)

*(d) implies (e).* Since $\bar{\lambda}\notin\sigma_r(A^*)$, there is an operator $C$ in $\mathcal B(\mathcal H)$ such that $(A^*-\bar{\lambda})C=1$. Hence $\mathcal H=(A^*-\bar{\lambda})C\mathcal H\subseteq\operatorname{ran}(A^*-\bar{\lambda})$.

*(e) implies (a).* Let $\mathcal N=\ker(A^*-\bar{\lambda})^\perp$ and define $T:\mathcal N\to\mathcal H$ by $Th=(A^*-\bar{\lambda})h$. Then $T$ is bijective and hence invertible. Let $C:\mathcal H\to\mathcal H$ be defined by $Ch=T^{-1}h$. Then $C\mathcal H=\mathcal N$ and $(A^*-\bar{\lambda})C=1$. Thus $C^*(A-\lambda)=1$ so that if $h\in\mathcal H$, $\|h\|=\|C^*(A-\lambda)h\|\leq\|C^*\|\|(A-\lambda)h\|$. Hence $\inf\{\|(A-\lambda)h\|:\|h\|=1\}\geq\|C^*\|^{-1}$. $\blacksquare$

If $\Delta\subseteq\mathbb C$, $\Delta^*\equiv\{\bar{\lambda}:\lambda\in\Delta\}$.

**1.2. Corollary.** *If $A\in\mathcal B(\mathcal H)$, then $\partial\sigma(A)\subseteq\sigma_l(A)\cap\sigma_r(A)=\sigma_{ap}(A)\cap\sigma_{ap}(A^*)^*$.*

**Proof.** The equality is immediate from the preceding theorem. In fact, $\sigma_l(A)=\sigma_{ap}(A)$ and $\sigma_r(A)=\sigma_l(A^*)^*=\sigma_{ap}(A^*)^*$. If $\lambda\in\partial\sigma(A)$, then (VII.6.7) $\lambda\in\sigma_{ap}(A)$. But $\bar{\lambda}\in\partial\sigma(A^*)$ so that $\bar{\lambda}\in\sigma_{ap}(A^*)$. $\blacksquare$

For normal elements there is less variety. The pertinent result is proved here in a more general setting than that of operators.

**1.3. Proposition.** *Let $\mathcal A$ be a $C^*$-algebra with identity. If $a$ is a normal element of $\mathcal A$, then the following statements are equivalent.*

(a) $a$ is invertible.

(b) $a$ is left invertible.

(c) $a$ is right invertible.

**Proof.** Assume that $a$ is left invertible, so there is a $b$ in $\mathcal A$ such that $ba=1$. Thus for any $x$ in $\mathcal A$, $\|x\|=\|bax\|\leq\|b\|\|ax\|$, and hence $\|ax\|\geq\|b\|^{-1}\|x\|$. In particular, this is true whenever $x\in C^*(a)$. Because $a$ is normal, $C^*(a)$ is isomorphic to $C(K)$ where $K=\sigma(a)$ and where the isomorphism takes $a$ into the function $z$ ($z(w)=w$). The inequality above thus becomes: $\|zf\|\geq\|b\|^{-1}\|f\|$ for every $f$ in $C(K)$. It must be shown that $0\notin K$ ($=\sigma(a)$). If $0\in K$, then for every integer $n$ there is a function $f_n$ in $C(K)$ such that $0\leq f_n\leq1$, $f_n(0)=1$ and $f_n(z)=0$ for $z$ in $K$ and $|z|\geq n^{-1}$. Since $0\in K$, $\|f_n\|=1$. But $\|zf_n\|\leq1/n$. This contradicts the inequality and so $0\notin\sigma(a)$; that is, $a$ is invertible.

The argument above shows that (b) implies (a). If $a$ is right invertible, then
