invertible and hence left semi-Fredholm. Also $SS^{*}=1-P_{0}$, where $P_{0}$ is the projection of $\mathcal H$ onto $\mathcal H_{0}$. So $S$ is Fredholm if $\alpha<\infty$.

In the next result, the equivalence of the first three conditions is referred to as Atkinson’s Theorem. The rest of this theorem is from Wolf [1959], Schechter [1968], and Fillmore, Stampfli and Williams [1972].

**2.3. Theorem.** *If $A:\mathcal H\to\mathcal H'$ is a bounded operator, the following statements are equivalent.*

(a) *$A$ is left semi-Fredholm.*

(b) *$\operatorname{ran}A$ is closed and $\dim\ker A<\infty$.*

(c) *There is a bounded operator $B:\mathcal H'\to\mathcal H$ and a finite rank operator $F$ on $\mathcal H$ such that $BA=1+F$.*

(d) *There is no sequence $\{h_n\}$ of unit vectors in $\mathcal H$ such that $h_n\to0$ weakly and $\lim\|Ah_n\|=0$.*

(e) *There is no orthonormal sequences $\{e_n\}$ in $\mathcal H$ such that $\lim\|Ae_n\|=0$.*

(f) *There is a $\delta>0$ such that $\{h\in\mathcal H:\|Ah\|\leq\delta\|h\|\}$ contains no infinite dimensional manifold.*

(g) *If the positive operator $(A^{*}A)^{1/2}=\int_{0}^{\infty}t\,dE(t)$, then there is a $\delta>0$ such that $E[0,\delta]\mathcal H$ is finite dimensional.*

(h) *If $K\in\mathcal B_{0}(\mathcal H)$, then $\dim\ker(A+K)<\infty$.*

**Proof.** (a) implies (b). According to (a) there is a bounded operator $B$ such that $\pi(B)\pi(A)=1$; that is, $\pi(BA-1)=0$. Hence $BA=1+K$ for some compact operator $K$. But $\ker A\subseteq\ker BA=\ker(1+K)$. Since the eigenspace corresponding to nonzero eigenvalues of compact operators are finite dimensional, $\dim\ker A<\infty$. Also, the Fredholm Alternative (VII.7.9) implies $\operatorname{ran}BA=\operatorname{ran}(K+1)$ is closed. Hence there is a constant $c>0$ such that for $h\perp\ker(BA)$, $\|BAh\|\geq c\|h\|$. Thus if $h\in[\ker BA]^{\perp}$, $c\|h\|\leq\|B\|\|Ah\|$, or $\|Ah\|\geq(c/\|B\|)\|h\|$. This implies that $A([\ker BA]^{\perp})$ is closed. But $\operatorname{ran}A=A([\ker BA]^{\perp})+A(\ker BA)$. Since $A(\ker BA)$ is finite dimensional, $\operatorname{ran}A$ is closed.

(b) implies (c). First define $A_{1}:(\ker A)^{\perp}\to\operatorname{ran}A$ by $A_{1}=A|(\ker A)^{\perp}$ and note that $A_{1}$ is invertible by The Open Mapping Theorem. Let $P$ be the projection of $\mathcal H'$ onto $\operatorname{ran}A$ and define $B:\mathcal H'\to\mathcal H$ by $B=A_{1}^{-1}P$. It is left to the reader to check that $BA=1-F$, where $F$ is the orthogonal projection of $\mathcal H$ onto $\ker A$. Since $\ker A$ is finite dimensional, this establishes (c).

(c) implies (a). This is clear.

(a) implies (d). Suppose $\{h_n\}$ is a sequence of unit vectors in $\mathcal H$ that converges weakly to $0$ and let $B:\mathcal H'\to\mathcal H$ and $K$ be as in the definition of a left semi-Fredholm operator. Since $BA=1+K$, $|1-\|BAh_n\||=|\|h_n\|-\|BAh_n\||\leq\|Kh_n\|$ and $\|Kh_n\|\to0$ since $K$ is compact. Thus $\|BAh_n\|\to1$ and so it is impossible for $\{Ah_n\}$ to converge to $0$ in norm.

(d) implies (e). Orthonormal sequences converge weakly to $0$.

(e) implies (f). If (f) is false, then for every positive integer $n$ there is an infinite dimensional manifold $\mathcal M_n$ such that $\|Ah\|\leq(1/n)\|h\|$ for all $h$ in $\mathcal M_n$.
