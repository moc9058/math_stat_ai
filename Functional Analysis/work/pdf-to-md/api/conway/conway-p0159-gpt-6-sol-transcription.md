Since $x_0\in K$, $x_0=\sum_{k=1}^{n}\alpha_kx_k$, $x_k\in K_k$, $\alpha_k\geqslant 0$, $\alpha_1+\cdots+\alpha_n=1$. But $x_0$ is an extreme point of $K$. Thus, $x_0=x_k\in K_k$ for some $k$. But this implies that $x_0\in K_k\subseteq y_k+\operatorname{cl}U_0\subseteq\operatorname{cl}(F+U_0)$, a contradiction. ■

You might think that the set of extreme points of a compact convex subset would have to be closed. This is untrue even if the LCS is finite dimensional, as Figure V-1 illustrates.

[FIGURE: A triangular outline with a horizontal base and an apex above its midpoint. Two curved lines run from the apex to the midpoint of the base, forming a narrow lens; the left curve is dashed and the right curve is solid. No labels appear within the drawing.]

Figure V-1

**7.9. Proposition.** *If $K$ is a compact convex subset of a LCS $\mathcal X$, $\mathcal Y$ is a LCS, and $T:K\to\mathcal Y$ is a continuous affine map, then $T(K)$ is a compact convex subset of $\mathcal Y$ and if $y$ is an extreme point of $T(K)$, then there is an extreme point $x$ of $K$ such that $T(x)=y$.*

**PROOF.** Because $T$ is affine, $T(K)$ is convex and it is compact by the continuity of $T$. Let $y$ be an extreme point of $T(K)$. It is easy to see that $T^{-1}(y)$ is compact and convex. Let $x$ be an extreme point of $T^{-1}(y)$. It now follows that $x\in\operatorname{ext}K$ (Exercise 9). ■

Note that it is possible that there are extreme points $x$ of $K$ such that $T(x)$ is not an extreme point of $T(K)$. For example, let $T$ be the orthogonal projection of $\mathbb R^3$ onto $\mathbb R^2$ and let $K=\operatorname{ball}\mathbb R^3$.

## Exercises

1. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $1<p<\infty$, then the set of extreme points of $\operatorname{ball}L^p(\mu)$ is $\{f\in L^p(\mu):\|f\|_p=1\}$.

2. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, the set of extreme points of $\operatorname{ball}L^1(\mu)$ is $\{\alpha\chi_E:E\text{ is an atom of }\mu,\ \alpha\in\mathbb F,\text{ and }|\alpha|=\mu(E)^{-1}\}$.

3. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, the set of extreme points of $\operatorname{ball}L^\infty(\mu)$ is $\{f\in L^\infty(\mu):|f(x)|=1\text{ a.e. }[\mu]\}$.

4. If $X$ is completely regular, the set of extreme points of $\operatorname{ball}C_b(X)$ is $\{f\in C_b(X):|f(x)|=1\text{ for all }x\}$. So $\operatorname{ball}C_{\mathbb R}[0,1]$ has only two extreme points.

5. Let $X$ be a totally disconnected compact space. (That is, $X$ is compact and if $x\in X$ and $U$ is an neighborhood of $x$, then there is a subset $V$ of $X$ that is both open and closed and such that $x\in V\subseteq U$. The Cantor set is an example of such a space.) Show that $\operatorname{ball}C(X)$ is the norm closure of the convex hull of its extreme points. (If $\mathbb F=\mathbb C$, the result is true for all compact Hausdorff spaces $X$ (Phelps
