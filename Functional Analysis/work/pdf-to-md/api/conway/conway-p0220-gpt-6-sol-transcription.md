$1-e\neq 0$, $a_1$ cannot be invertible. However, consider the algebra $\mathcal A_1\equiv\{b\in\mathcal A:ab=ba\text{ and }be=eb=b\}$. It is left to the reader to show that $\mathcal A_1$ is a Banach algebra and $e$ is the identity for $\mathcal A_1$. If $a_1$ is considered as an element of the algebra $\mathcal A_1$, then its spectrum as an element of $\mathcal A_1$ is $F_1$. This is an illustration of how the spectrum depends on the Banach algebra (the subject of the next section; also see Exercise 9).

## Exercises

1. Let $\mathcal A=C(X)$, $X$ compact (see Example 3.2). If $g\in C(X)$ and $f\in\operatorname{Hol}(g)$, show that $f(g)=f\circ g$.

2. Let $a$ be a nilpotent element of $\mathcal A$. For $f,g$ in $\operatorname{Hol}(a)$, give a necessary and sufficient condition on $f$ and $g$ that $f(a)=g(a)$.

3. Let $d\geq 1$ and let $A\in M_d(\mathbb C)$. Give a necessary and sufficient condition on $f$ in $\operatorname{Hol}(A)$ such that $f(A)=0$. (Hint: Consider the Jordan canonical form for $A$.)

4. If $\mathcal A$ is a Banach algebra with identity, $a\in\mathcal A$, $f\in\operatorname{Hol}(a)$, and $g$ is analytic in a neighborhood of $f(\sigma(a))$, then $g\circ f\in\operatorname{Hol}(a)$ and $g(f(a))=g\circ f(a)$.

5. If $\mathcal X$ is a Banach space, $A\in\mathcal B(\mathcal X)$, and $\mathcal M\leq\mathcal X$ such that $(A-\alpha)^{-1}\mathcal M\subseteq\mathcal M$ for all $\alpha$ in $\rho(A)$, show that $f(A)\mathcal M\subseteq\mathcal M$ whenever $f\in\operatorname{Hol}(A)$.

6. If $\mathcal X$ is a Banach space, $A\in\mathcal B(\mathcal X)$, and $f\in\operatorname{Hol}(A)$, show that $f(A)^*=f(A^*)$. (See (6.1) below.)

7. If $\mathcal H$ is a Hilbert space, $A\in\mathcal B(\mathcal H)$, and $f\in\operatorname{Hol}(A)$, show that $f(A)^*=\widetilde f(A^*)$, where $\widetilde f(z)=\overline{f(\bar z)}$ (See (6.1) below.)

8. If $\mathcal H$ is a Hilbert space, $A$ is a normal operator on $\mathcal H$, and $f\in\operatorname{Hol}(A)$, show that $f(A)$ is normal.

9. Let $\mathcal X$ be a Banach space and let $A\in\mathcal B(\mathcal X)$. Show that if $\sigma(A)=F_1\cup F_2$ where $F_1,F_2$ are disjoint closed subsets of $\mathbb C$, then there are topologically complementary subspaces $\mathcal X_1,\mathcal X_2$ of $\mathcal X$ such that (a) $B\mathcal X_j\subseteq\mathcal X_j$ $(j=1,2)$ whenever $BA=AB$; (b) if $A_j=A|_{\mathcal X_j}$, $\sigma(A_j)=F_j$; (c) there is an invertible operator $R:\mathcal X\to\mathcal X_1\oplus_1\mathcal X_2$ such that $RAR^{-1}=A_1\oplus A_2$.

10. Let $A\in M_d(\mathbb C)$, $\sigma(A)=\{\alpha_1,\ldots,\alpha_n\}$, where $\alpha_i\neq\alpha_j$ for $i\neq j$. Show that for $1\leq j\leq n$ there is a matrix $A_j$ in $M_{d_j}(\mathbb C)$ such that $\sigma(A_j)=\{\alpha_j\}$ and $A$ is similar to $A_1\oplus\cdots\oplus A_n$.

11. If $\mathcal A$ is a Banach algebra, $I$ is an ideal of $\mathcal A$ (not necessarily closed), $a\in I$, and $f\in\operatorname{Hol}(a)$ such that $f(0)=0$, show that $f(a)\in I$.

## §5. Dependence of the Spectrum on the Algebra

If $\partial\mathbb D=\{z\in\mathbb C:|z|=1\}$, let $\mathcal B=$ the uniform closure of the polynomials in $C(\partial\mathbb D)$. (Here “polynomial” means a polynomial in $z$.) If $\mathcal A=C(\partial\mathbb D)$, then the spectrum of $z$ as an element of $\mathcal A$ is $\partial\mathbb D$ (Example 3.2). That is,

$$
\sigma_{\mathcal A}(z)=\partial\mathbb D.
$$
