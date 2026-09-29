The preceding two examples illustrate the fact that the calculation of the adjoint depends on the domain of the operator, not just the formal definition of the operator. Note the fact that the next result generalizes (II.2.19).

**1.13. Proposition.** *If $A:\mathcal H\to\mathcal H$ is densely defined, then*

$$
(\operatorname{ran}A)^\perp=\ker A^*.
$$

*If $A$ is also closed, then*

$$
(\operatorname{ran}A^*)^\perp=\ker A.
$$

**Proof.** If $h\perp\operatorname{ran}A$, then for every $f$ in $\operatorname{dom}A$, $0=\langle Af,h\rangle$. Hence $h\in\operatorname{dom}A^*$ and $A^*h=0$. The other inclusion is clear. By Corollary 1.8, if $A\in\mathcal C(\mathcal H,\mathcal H)$, $A^{**}=A$. So the second equality follows from the first. $\blacksquare$

**1.14. Definition.** If $A:\mathcal H\to\mathcal H$ is a linear operator, $A$ is *boundedly invertible* if there is a bounded linear operator $B:\mathcal H\to\mathcal H$ such that $AB=1$ and $BA\subseteq1$.

Note that if $BA\subseteq1$, then $BA$ is bounded on its domain. Call $B$ a *(bounded) inverse* of $A$.

**1.15. Proposition.** *Let $A:\mathcal H\to\mathcal H$ be a linear operator.*

(a) *$A$ is boundedly invertible if and only if $\ker A=(0)$, $\operatorname{ran}A=\mathcal H$, and the graph of $A$ is closed.*

(b) *If $A$ is boundedly invertible, its inverse is unique and denoted by $A^{-1}$.*

**Proof.** (a) Let $B$ be a bounded inverse of $A$. So $\operatorname{dom}B=\mathcal H$. Since $BA\subseteq1$, $\ker A=(0)$; since $AB=1$, $\operatorname{ran}A=\mathcal H$. Also, $\operatorname{gra}A=\{h\oplus Ah:h\in\operatorname{dom}A\}=\{Bk\oplus k:k\in\mathcal H\}$. Since $B$ is bounded, $\operatorname{gra}A$ is closed. Conversely, if $A$ has the stated properties, $Bk=A^{-1}k$ for $k$ in $\mathcal H$ is a well-defined operator on $\mathcal H$. Because $\operatorname{gra}A$ is closed, $\operatorname{gra}B$ is closed. By the Closed Graph Theorem, $B\in\mathcal B(\mathcal H,\mathcal H)$.

(b) This is an exercise. $\blacksquare$

**1.16. Definition.** If $A:\mathcal H\to\mathcal H$ is a linear operator, $\rho(A)$, the *resolvent set* for $A$, is defined by $\rho(A)=\{\lambda\in\mathbb C:\lambda-A\text{ is boundedly invertible}\}$. The *spectrum* of $A$ is the set $\sigma(A)=\mathbb C\setminus\rho(A)$.

It is easy to see that if $A:\mathcal H\to\mathcal H$ is a linear operator and $\lambda\in\mathbb C$, $\operatorname{gra}A$ is closed if and only if $\operatorname{gra}(A-\lambda)$ is closed. So if $A$ does not have closed graph, $\sigma(A)=\mathbb C$. Even if $A$ has closed graph, it is possible that $\sigma(A)$ is empty (see Exercise 10). The spectrum of an unbounded operator, however, does enjoy some of the properties possessed by the spectrum of an element of a Banach algebra. The proof of the next result is left to the reader.

**1.17. Proposition.** *If $A:\mathcal H\to\mathcal H$ is a linear operator, then $\sigma(A)$ is closed and $z\mapsto(z-A)^{-1}$ is an analytic function on $\rho(A)$.*
