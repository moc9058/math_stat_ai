# §9*. The Schauder Fixed Point Theorem

Fixed-point theorems hold a fascination for mathematicians and they are very applicable to a variety of mathematical and physical situations. In this section and the next two such theorems are presented.

The results of this section are different from the rest of this book in an essential way. Although we will continue to look at convex subsets of Banach spaces, the functions will not be assumed to be linear or affine. This is a small part of nonlinear functional analysis.

To begin with, recall the following classical result whose proof can be found in any algebraic topology book. (Also see Dugundji [1966].)

**9.1. Brouwer’s Fixed Point Theorem.** *If $1\leq d<\infty$, $B=$ the closed unit ball of $\mathbb{R}^d$, and $f:B\to B$ is a continuous map, then there is a point $x$ in $B$ such that $f(x)=x$.*

**9.2. Corollary.** *If $K$ is a nonempty compact convex subset of a finite dimensional normed space $\mathcal{X}$ and $f:K\to K$ is a continuous function, then there is a point $x$ in $K$ such that $f(x)=x$.*

**Proof.** Since $\mathcal{X}$ is isomorphic to either $\mathbb{C}^d$ or $\mathbb{R}^d$, it is homeomorphic to either $\mathbb{R}^{2d}$ or $\mathbb{R}^d$. So it suffices to assume that $\mathcal{X}=\mathbb{R}^d$, $1\leq d<\infty$. If $K=\{x\in\mathbb{R}^d:\|x\|\leq r\}$, then the result is immediate from Brouwer’s Theorem (Exercise). If $K$ is any compact convex subset of $\mathbb{R}^d$, let $r>0$ such that $K\subseteq B\equiv\{x\in\mathbb{R}^d:\|x\|\leq r\}$. Let $\phi:B\to K$ be the function defined by $\phi(x)=$ the unique point $y$ in $K$ such that $\|x-y\|=\operatorname{dist}(x,K)$ (I.2.5). Then $\phi$ is continuous (Exercise) and $\phi(x)=x$ for each $x$ in $K$. (In topological parlance, $K$ is a retract of $B$.) Hence $f\circ\phi:B\to K\subseteq B$ is continuous. By Brouwer’s Theorem, there is an $x$ in $B$ such that $f(\phi(x))=x$. Since $f\circ\phi(B)\subseteq K$, $x\in K$. Hence $\phi(x)=x$ and $f(x)=x$. ■

Schauder’s Fixed Point Theorem is a generalization of the preceding corollary to infinite dimensional spaces.

**9.3. Definition.** If $\mathcal{X}$ is a normed space and $E\subseteq\mathcal{X}$, a function $f:E\to\mathcal{X}$ is said to be *compact* if $f$ is continuous and $\operatorname{cl}f(A)$ is compact whenever $A$ is a bounded subset of $E$.

If $E$ is itself a compact subset of $\mathcal{X}$, then every continuous function from $E$ into $\mathcal{X}$ is compact.

The following lemma will be needed in the proof of Schauder’s Theorem.

**9.4. Lemma.** *If $K$ is a compact subset of the normed space $\mathcal{X}$, $\varepsilon>0$, and $A$ is a finite subset of $K$ such that $K\subseteq\bigcup\{B(a;\varepsilon):a\in A\}$, define $\phi_A:K\to\mathcal{X}$ by*

$$
\phi_A(x)=\frac{\sum\{m_a(x)a:a\in A\}}{\sum\{m_a(x):a\in A\}},
$$
