identity operator. Since $AK\in\mathcal B_0(\mathcal X)$, $AK|_{\mathcal N}\in\mathcal B_0(\mathcal N)$. Thus $\dim\mathcal N<\infty$. Since $AK\in\mathcal A=\{T\}'$, for any $x$ in $\mathcal N$, $AK(Tx)=T(AKx)=Tx$; hence $T\mathcal N\subseteq\mathcal N$. But $\dim\mathcal N<\infty$ so that $T|_{\mathcal N}$ must have an eigenvalue $\lambda$. Thus $\ker(T-\lambda)=\mathcal M\ne(0)$. But $\mathcal M\ne\mathcal X$ since $T$ is not a multiple of the identity. It is easy to check that $\mathcal M$ is hyperinvariant for $T$. $\blacksquare$

A proof of a slightly weaker version of Lomonosov’s Theorem that avoids Schauder’s Fixed Point Theorem can be found in Michaels [1977].

**4.14. Corollary.** (Aronszajn–Smith [1954].) *If $K\in\mathcal B_0(\mathcal X)$, then $\operatorname{Lat}K$ is nontrivial.*

The next result appeared in Bernstein and Robinson [1966], where it is proved using nonstandard analysis. Halmos [1966] gave a proof using standard analysis. Now it is an easy consequence of Lomonosov’s Theorem.

**4.15. Corollary.** *If $\mathcal X$ is infinite dimensional, $A\in\mathcal B(\mathcal X)$, and there is a polynomial in one variable, $p$, such that $p(A)\in\mathcal B_0(\mathcal X)$, then $\operatorname{Lat}A$ is nontrivial.*

**Proof.** If $p(A)\ne0$, then Lomonosov’s Theorem applies. If $p(A)=0$, let $p(z)=\alpha_0+\alpha_1z+\cdots+\alpha_nz^n$, $\alpha_n\ne0$. For $x\ne0$, let $\mathcal M=\bigvee\{x,Ax,\ldots,A^{n-1}x\}$. Since $A^n=-\alpha_n^{-1}[\alpha_0+\alpha_1A+\cdots+\alpha_{n-1}A^{n-1}]$, $\mathcal M\in\operatorname{Lat}A$. Since $x\in\mathcal M$, $\mathcal M\ne(0)$; since $\dim\mathcal M<\infty$, $\mathcal M\ne\mathcal X$. $\blacksquare$

**4.16. Corollary.** *If $K_1,K_2\in\mathcal B_0(\mathcal X)$ and $K_1K_2=K_2K_1$, then $K_1$ and $K_2$ have a common nontrivial invariant subspace.*

## Exercises

1. Let $A,B,T\in\mathcal B(\mathcal X)$ such that $TA=BT$. Show that $\operatorname{graph}(T)\in\operatorname{Lat}(A\oplus B)$.

2. Prove that $\mathcal M\in\operatorname{Lat}T$ if and only if $\mathcal M^\perp\in\operatorname{Lat}T^*$. What does the map $\mathcal M\mapsto\mathcal M^\perp$ of $\operatorname{Lat}T$ into $\operatorname{Lat}T^*$ do to the lattice operations?

3. Let $\{e_1,e_2,e_3\}$ be the usual basis for $\mathbb F^3$ and let $\alpha_1,\alpha_2,\alpha_3\in\mathbb F$. Define $T:\mathbb F^3\to\mathbb F^3$ by $Te_j=\alpha_je_j$, $1\le j\le3$. (a) If $\alpha_1,\alpha_2,\alpha_3$ are all distinct, show that $\mathcal M\in\operatorname{Lat}T$ if and only if $\mathcal M=\bigvee E$, where $E\subseteq\{e_1,e_2,e_3\}$. (b) If $\alpha_1=\alpha_2\ne\alpha_3$, show that $\mathcal M\in\operatorname{Lat}T$ if and only if $\mathcal M=\mathcal N+\mathcal L$, where $\mathcal N\le\bigvee\{e_1,e_2\}$ and $\mathcal L\le\{\alpha e_3:\alpha\in\mathbb F\}$.

4. Generalize Exercise 3 by characterizing $\operatorname{Lat}T$, where $T$ is defined by $Te_j=\alpha_je_j$, $1\le j\le d$, for any choice of scalars $\alpha_1,\ldots,\alpha_d$ and where $\{e_1,\ldots,e_d\}$ is the usual basis for $\mathbb F^d$.

5. Let $\{e_1,\ldots,e_d\}$ be the usual basis for $\mathbb F^d$, let $\{\alpha_1,\ldots,\alpha_{d-1}\}\subseteq\mathbb F$ with no $\alpha_j=0$. If $Te_j=\alpha_je_{j+1}$ for $1\le j\le d-1$ and $Te_d=0$, find $\operatorname{Lat}T$.

6. If $T\in\mathcal B(\mathbb R^d)$ and $d\ge3$, show that $T$ has a nontrivial subspace.

7. Show that if $T\in\mathcal B(\mathcal X)$ and $\mathcal X$ is not separable, then $T$ has a nontrivial invariant subspace.
