5. (A variation on Example 1.8) Let $n\geq 2$ and let $\mathcal H =$ the collection of all function $f:[0,1]\to\mathbb F$ such that (a) $f(0)=0$; (b) for $1\leq k\leq n-1$, $f^{(k)}(t)$ exists for all $t$ in $[0,1]$ and $f^{(k)}$ is continuous on $[0,1]$; (c) $f^{(n-1)}$ is absolutely continuous and $f^{(n)}\in L^2(0,1)$. For $f$ and $g$ in $\mathcal H$, define

   $$
   \langle f,g\rangle=\sum_{k=1}^{n}\int_0^1 f^{(k)}(t)\overline{g^{(k)}(t)}\,dt.
   $$

   Show that $\mathcal H$ is a Hilbert space.

6. Let $u$ be a semi-inner product on $\mathcal X$ and put $\mathcal N=\{x\in\mathcal X:u(x,x)=0\}$.

   (a) Show that $\mathcal N$ is a linear subspace of $\mathcal X$.

   (b) Show that if

   $$
   \langle x+\mathcal N,y+\mathcal N\rangle\equiv u(x,y)
   $$

   for all $x+\mathcal N$ and $y+\mathcal N$ in the quotient space $\mathcal X/\mathcal N$, then $\langle\cdot,\cdot\rangle$ is a well-defined inner product on $\mathcal X/\mathcal N$.

7. Let $\mathcal H$ be a Hilbert space over $\mathbb R$ and show that there is a Hilbert space $\mathcal K$ over $\mathbb C$ and a map $U:\mathcal H\to\mathcal K$ such that (a) $U$ is linear; (b) $\langle Uh_1,Uh_2\rangle=\langle h_1,h_2\rangle$ for all $h_1,h_2$ in $\mathcal H$; (c) for any $k$ in $\mathcal K$ there are unique $h_1,h_2$ in $\mathcal H$ such that $k=Uh_1+iUh_2$. ($\mathcal K$ is called the *complexification* of $\mathcal H$.)

8. If $G=\{z\in\mathbb C:0<|z|<1\}$ show that every $f$ in $L_a^2(G)$ has a removable singularity at $z=0$.

9. Which functions are in $L_a^2(\mathbb C)$?

10. Let $G$ be an open subset of $\mathbb C$ and show that if $a\in G$, then $\{f\in L_a^2(G):f(a)=0\}$ is closed in $L_a^2(G)$.

11. If $\{h_n\}$ is a sequence in a Hilbert space $\mathcal H$ such that $\sum_n\|h_n\|<\infty$, then show that $\sum_{n=1}^{\infty}h_n$ converges in $\mathcal H$.

## §2. Orthogonality

The greatest advantage of a Hilbert space is its underlying concept of orthogonality.

**2.1. Definition.** If $\mathcal H$ is a Hilbert space and $f,g\in\mathcal H$, then $f$ and $g$ are *orthogonal* if $\langle f,g\rangle=0$. In symbols, $f\perp g$. If $A,B\subseteq\mathcal H$, then $A\perp B$ if $f\perp g$ for every $f$ in $A$ and $g$ in $B$.

If $\mathcal H=\mathbb R^2$, this is the correct concept. Two non-zero vectors in $\mathbb R^2$ are orthogonal precisely when the angle between them is $\pi/2$.

**2.2. The Pythagorean Theorem.** *If $f_1,f_2,\ldots,f_n$ are pairwise orthogonal vectors in $\mathcal H$, then*

$$
\|f_1+f_2+\cdots+f_n\|^2
=\|f_1\|^2+\|f_2\|^2+\cdots+\|f_n\|^2.
$$
