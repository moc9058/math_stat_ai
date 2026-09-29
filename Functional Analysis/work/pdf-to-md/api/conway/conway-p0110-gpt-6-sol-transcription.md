## Exercises

1. If $\mathcal X$ is a vector space and $\mathcal M$ is a linear manifold in $\mathcal X$, show that there is a linear manifold $\mathcal N$ in $\mathcal X$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal X$.

2. Let $\mathcal X$ be a Banach space and let $E:\mathcal X\to\mathcal X$ be a linear map such that $E^2=E$ and both $\operatorname{ran}E$ and $\ker E$ are closed. Show that $E$ is continuous.

3. Prove Theorem 13.2.

4. Let $\mathcal X$ be a Banach space and show that if $\mathcal M$ is a complemented subspace of $\mathcal X$, then every complementary subspace is isomorphic to $\mathcal X/\mathcal M$.

5. Let $X$ be a compact set and let $Y$ be a closed subset of $X$. A *simultaneous extension* for $Y$ is a bounded linear map $T:C(Y)\to C(X)$ such that for each $g$ in $C(Y)$, $T(g)|Y=g$. Let $C_0(X\setminus Y)=\{f\in C(X):f(y)=0\text{ for all }y\text{ in }Y\}$. Show that if there is a simultaneous extension for $Y$, then $C_0(X\setminus Y)$ is complemented in $C(X)$.

6. Show that if $Y$ is a closed subset of $[0,1]$, then there is a simultaneous extension for $Y$ (see Exercise 5). (Hint: Write $[0,1]\setminus Y$ as the union of disjoint intervals.)

7. Using the notation of Exercise 5, show that if $Y$ is a retract of $X$, then $C_0(X\setminus Y)$ is complemented in $C(X)$.

## §14. The Principle of Uniform Boundedness

There are several results that may be called the Principle of Uniform Boundedness (PUB) and all of these are called the PUB by various mathematicians. In this book the PUB will refer to any of the results of this section, though in a formal way the next result plays the role of the founder of the family.

**14.1. Principle of Uniform Boundedness (PUB).** *Let $\mathcal X$ be a Banach space and $\mathcal Y$ a normed space. If $\mathcal A\subseteq\mathcal B(\mathcal X,\mathcal Y)$ such that for each $x$ in $\mathcal X$, $\sup\{\|Ax\|:A\in\mathcal A\}<\infty$, then $\sup\{\|A\|:A\in\mathcal A\}<\infty$.*

**Proof.** (Due to William R. Zame, 1978. Also see J. Hennefeld [1980].) For each $x$ in $\mathcal X$ let $M(x)=\sup\{\|Ax\|:A\in\mathcal A\}$, so $\|Ax\|\leq M(x)$ for all $x$ in $\mathcal X$. Suppose $\sup\{\|A\|:A\in\mathcal A\}=\infty$. Then there is a sequence $\{A_n\}\subseteq\mathcal A$ and a sequence $\{x_n\}$ of vectors in $\mathcal X$ such that $\|x_n\|=1$ and $\|A_nx_n\|>4^n$. Let $y_n=2^{-n}x_n$; thus $\|y_n\|=2^{-n}$ and $\|A_ny_n\|>2^n$.

**14.2. Claim.** There is a subsequence $\{y_{n_k}\}$ such that for $k\geq 1$:

(a) $$\|A_{n_{k+1}}y_{n_{k+1}}\|>1+k+\sum_{j=1}^{k}M(y_{n_j});$$

(b) $$\|y_{n_{k+1}}\|<2^{-k-1}\left[\sup\{\|A_{n_j}\|:1\leq j\leq k\}\right]^{-1}.$$

The proof of (14.2) is by induction. Let $n_1=1$. The induction step is valid since $\|y_n\|\to 0$ and $\|A_ny_n\|\to\infty$. The details are left to the reader.
