## Exercises

1. If $x\in X$ and $\delta_x(f)=f(x)$ for all $f$ in $C_b(X)$, show that $\|\delta_x\|=1$.

2. Prove that a subset of a completely regular space is completely regular.

3. Fill in the details of the proof of Theorem 6.2.

4. If $X$ is completely regular, $\Omega$ is compact, and $f:X\to\Omega$ is continuous, show that there is a continuous map $f^\beta:\beta X\to\Omega$ such that $f^\beta|X=f$.

5. If $X$ is completely regular, show that $X$ is open in $\beta X$ if and only if $X$ is locally compact.

6. Let $\mathbf N$ have the discrete topology. Let $\{r_n:n\in\mathbf N\}$ be an enumeration of the rational numbers in $[0,1]$. Let $S=$ the irrational numbers in $[0,1]$ and for each $s$ in $S$ let $\{r_n:n\in N_s\}$ be a subsequence of $\{r_n\}$ such that $s=\lim\{r_n:n\in N_s\}$. Show: (a) if $s,t\in S$ and $s\ne t$, $N_s\cap N_t$ is finite; (b) if for each $s$ in $S$, $\operatorname{cl}N_s=$ the closure of $N_s$ in $\beta\mathbf N$ and $A_s=(\operatorname{cl}N_s)\setminus\mathbf N$, then $\{A_s:s\in S\}$ are pairwise disjoint subsets of $\beta\mathbf N\setminus\mathbf N$ that are both open and closed.

7. Show that if $X$ is normal, $\tau\in\beta X$, and there is a sequence $\{x_n\}$ in $X$ such that $x_n\to\tau$ in $\beta X$, then $\tau\in X$. If $X$ is not normal, is the result still true?

8. Let $X$ be the space of all ordinals less than the first uncountable ordinal and give $X$ the order topology. Show that $\beta X=$ the one point compactification of $X$. (You can find the pertinent definitions in Kelley [1955].)

## §7. The Krein–Milman Theorem

**7.1. Definition.** If $K$ is a convex subset of a vector space $\mathcal X$, then a point $a$ in $K$ is an *extreme point* of $K$ if there is no proper open line segment that contains $a$ and lies entirely in $K$. Let $\operatorname{ext}K$ be the set of extreme points of $K$.

Recall that an open line segment is a set of the form $(x_1,x_2)\equiv\{tx_2+(1-t)x_1:0<t<1\}$, and to say that this line segment is proper is to say that $x_1\ne x_2$.

**7.2. Examples.**

(a) If $\mathcal X=\mathbb R^2$ and $K=\{(x,y)\in\mathbb R^2:x^2+y^2\leqslant1\}$, then $\operatorname{ext}K=\{(x,y):x^2+y^2=1\}$.

(b) If $\mathcal X=\mathbb R^2$ and $K=\{(x,y)\in\mathbb R^2:x\leq0\}$, then $\operatorname{ext}K=\square$.

(c) If $\mathcal X=\mathbb R^2$ and $K=\{(x,y)\in\mathbb R^2:x<0\}\cup\{(0,0)\}$, then $\operatorname{ext}K=\{(0,0)\}$.

(d) If $K=$ the closed region in $\mathbb R^2$ bordered by a regular polygon, then $\operatorname{ext}K=$ the vertices of the polygon.

(e) If $\mathcal X$ is any normed space and $K=\{x\in\mathcal X:\|x\|\leqslant1\}$, then $\operatorname{ext}K\subseteq\{x:\|x\|=1\}$, though for all we know it may be that $\operatorname{ext}K=\square$.

(f) If $\mathcal X=L^1[0,1]$ and $K=\{f\in L^1[0,1]:\|f\|_1\leqslant1\}$, then $\operatorname{ext}K=\square$. This
