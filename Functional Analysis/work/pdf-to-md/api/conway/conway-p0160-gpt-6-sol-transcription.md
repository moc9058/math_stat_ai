[1965]). If $\mathbf F=\mathbf R$, then this characterizes totally disconnected compact spaces (Goodner [1964]).)

6. Show that ball $l^1$ is the norm closure of the convex hull of its extreme points.

7. Show that if $X$ is locally compact but not compact, then ball $C_0(X)$ has no extreme points.

8. If $\mathcal X$ is a LCS and $K_1,\ldots,K_n$ are compact convex subsets of $\mathcal X$, then $\overline{\operatorname{co}}(K_1\cup\cdots\cup K_n)=\operatorname{co}(K_1\cup\cdots\cup K_n)$ and this convex hull is compact.

9. Let $K$ be convex and let $T:K\to\mathcal Y$ be an affine map. If $y$ is an extreme point of $T(K)$ and $x$ is an extreme point of $T^{-1}(y)$, then $x$ is an extreme point of $K$.

10. If $\mathcal H$ is a Hilbert space and either $T$ or $T^*$ is an isometry, show that $T$ is an extreme point of the closed unit ball of $\mathcal B(\mathcal H)$. (The converse of this is also true, but it may be hard unless you use the Polar Decomposition of operators (VIII.3.11).)

## §8. An Application: The Stone–Weierstrass Theorem

If $f:X\to\mathbf C$ is a function, then $\bar f$ denotes the function from $X$ into $\mathbf C$ whose value at each $x$ is the complex conjugate of $f(x)$, $\overline{f(x)}$.

**8.1. The Stone–Weierstrass Theorem.** *If $X$ is compact and $\mathcal A$ is a closed subalgebra of $C(X)$ such that:*

(a) $1\in\mathcal A$;

(b) *if $x,y\in X$ and $x\ne y$, then there is an $f$ in $\mathcal A$ such that $f(x)\ne f(y)$;*

(c) *if $f\in\mathcal A$, then $\bar f\in\mathcal A$;*

*then $\mathcal A=C(X)$.*

If $C(X)$ is the algebra of continuous functions from $X$ into $\mathbf R$, then condition (c) is not needed. Also, an algebra in $C(X)$ that has property (b) is said to *separate the points* of $X$ (see Exercise 1).

The proof of this result that will be presented here makes use of the Krein–Milman Theorem and is due to L. de Branges [1959].

**Proof of the Stone–Weierstrass Theorem.** To prove the theorem it suffices to show that $\mathcal A^\perp=(0)$ (III.6.14). Suppose $\mathcal A^\perp\ne(0)$. By Alaoglu’s Theorem, ball $\mathcal A^\perp$ is weak* compact. By the Krein–Milman Theorem, there is an extreme point $\mu$ of ball $\mathcal A^\perp$. Let $K=$ the support of $\mu$. That is,

$$
K=X\setminus\bigcup\{V:V\text{ is open and }|\mu|(V)=0\}.
$$

Hence $|\mu|(X\setminus K)=0$ and $\int f\,d\mu=\int_K f\,d\mu$ for all continuous functions $f$ on $X$. Since $\mathcal A^\perp\ne(0)$, $\|\mu\|=1$ and $K\ne\Box$. Fix $x_0$ in $K$. It will be shown that $K=\{x_0\}$.
