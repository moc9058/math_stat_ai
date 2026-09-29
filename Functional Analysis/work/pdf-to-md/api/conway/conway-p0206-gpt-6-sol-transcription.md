## EXERCISES

1. Let $\mathcal A$ be an algebra that is also a Banach space and such that if $a\in\mathcal A$, the maps $x\mapsto ax$ and $x\mapsto xa$ of $\mathcal A\to\mathcal A$ are continuous. Let $\mathcal A_1=\mathcal A\times\mathbb F$ as in Proposition 1.3. If $a\in\mathcal A$, define $L_a:\mathcal A_1\to\mathcal A_1$ by $L_a(x,\xi)=(ax+\xi a,0)$. Show that $L_a\in\mathcal B(\mathcal A_1)$ and if $\lvert\!\lvert\!\lvert a\rvert\!\rvert\!\rvert=\|L_a\|$, then $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert$ is equivalent to the norm of $\mathcal A$ and $\mathcal A$ with $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert$ is a Banach algebra.

2. Complete the proof of Proposition 1.3.

3. Verify the statements made in Examples (1.4) through (1.9) and (1.11).

4. Let $G$ be a locally compact group. (a) If $\phi\in C_c(G)$ and $\varepsilon>0$, show that there is an open neighborhood $U$ of $e$ in $G$ such that $\|\phi_x-\phi_y\|<\varepsilon$ whenever $xy^{-1}\in U$. [Here $\phi_x(z)=\phi(xz)$.] (b) Show that if $f\in L^p(G)$, $1\leqslant p<\infty$, and $\varepsilon>0$, there is an open neighborhood $U$ of $e$ in $G$ such that $\|f_x-f_y\|_p<\varepsilon$ whenever $xy^{-1}\in U$. (c) Show that if $f\in L^1(G)$ and $g\in L^\infty(G)$, $h(x)=\int f(xy^{-1})g(y)\,dm(y)$ defines a bounded continuous function $h:G\to\mathbb F$. (d) If $f,g\in L^1(G)$ and $h$ is defined as in (c), show that $h\in L^1(G)$.

5. Prove Proposition 1.12.

6. Let $\{\mathcal A_i:i\in I\}$ be a collection of Banach algebras. (a) Show that $\bigoplus_0\mathcal A_i$ is a closed ideal of $\bigoplus_\infty\mathcal A_i$. (b) Show that $\bigoplus_\infty\mathcal A_i$ has an identity if and only if each $\mathcal A_i$ has an identity. (c) Show that $\bigoplus_0\mathcal A_i$ has an identity if $I$ is finite and each $\mathcal A_i$ has an identity.

7. If $X$, $Y$ are completely regular, show that $C_b(X)\oplus_\infty C_b(Y)$ is isometrically isomorphic to $C_b(X\oplus Y)$, where $X\oplus Y$ is the disjoint union of $X$ and $Y$.

8. If $X$ and $Y$ are locally compact, show that $C_0(X)\oplus_\infty C_0(Y)$ is isometrically isomorphic to $C_0(X\oplus Y)$.

9. Let $\{X_i:i\in I\}$ be a collection of locally compact spaces and let $X=$ the disjoint union of these spaces furnished with the topology $\{U\subseteq X:U\cap X_i\text{ is open in }X_i\text{ for all }i\}$. Show that $X$ is locally compact and $\bigoplus_0 C_0(X_i)$ is isometrically isomorphic to $C_0(X)$.

## §2. Ideals and Quotients

If $\mathcal A$ is an algebra, a *left ideal* of $\mathcal A$ is a subalgebra $\mathcal M$ of $\mathcal A$ such that $ax\in\mathcal M$ whenever $a\in\mathcal A$, $x\in\mathcal M$. A *right ideal* of $\mathcal A$ is a subalgebra $\mathcal M$ such that $xa\in\mathcal M$ whenever $a\in\mathcal A$, $x\in\mathcal M$. A *(bilateral) ideal* is a subalgebra of $\mathcal A$ that is both a left ideal and a right ideal.

If $a\in\mathcal A$ and $\mathcal A$ has an identity 1, say that $a$ is *left invertible* if there is an $x$ in $\mathcal A$ with $xa=1$. Similarly, define *right invertible* and *invertible* elements. If $a$ is invertible and $x,y\in\mathcal A$ such that $xa=1=ay$, then $y=1y=(xa)y=x(ay)=x1=x$. So if $a$ is invertible, there is a unique element $a^{-1}$ such that $aa^{-1}=a^{-1}a=1$.

If $\mathcal M$ is a left ideal in $\mathcal A$, $a\in\mathcal M$, and $a$ is left invertible, then $\mathcal M=\mathcal A$. In
