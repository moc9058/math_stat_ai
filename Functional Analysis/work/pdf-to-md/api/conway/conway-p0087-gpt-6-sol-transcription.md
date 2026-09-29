Now for the product or direct sum of normed spaces. Here there is a difficulty because, unlike Hilbert space, there is no canonical way to proceed. Suppose $\{\mathcal X_i:i\in I\}$ is a collection of normed spaces. Then $\prod\{\mathcal X_i:i\in I\}$ is a vector space if the linear operations are defined coordinatewise. The idea is to put a norm on a linear subspace of this product.

Let $\|\cdot\|$ denote the norm on each $\mathcal X_i$. For $1\leq p<\infty$, define

$$
\bigoplus_p\mathcal X_i\equiv
\left\{x\in\prod_i\mathcal X_i:\|x\|\equiv
\left[\sum_i\|x(i)\|^p\right]^{1/p}<\infty\right\}.
$$

Define

$$
\bigoplus_\infty\mathcal X_i\equiv
\left\{x\in\prod_i\mathcal X_i:\|x\|\equiv
\sup_i\|x(i)\|<\infty\right\}.
$$

If $\{\mathcal X_1,\mathcal X_2,\ldots\}$ is a sequence of normed spaces, define

$$
\bigoplus_0\mathcal X_n\equiv
\left\{x\in\prod_{n=1}^{\infty}\mathcal X_n:\|x(n)\|\to0\right\};
$$

give $\bigoplus_0\mathcal X_n$ the norm it has as a subspace of $\bigoplus_\infty\mathcal X_n$.

The proof of the next proposition is left as an exercise.

**4.4. Proposition.** Let $\{\mathcal X_i:i\in I\}$ be a collection of normed spaces and let $\mathcal X=\bigoplus_p\mathcal X_i$, $1\leq p\leq\infty$.

(a) $\mathcal X$ is a normed space and the projection $P_i:\mathcal X\to\mathcal X_i$ is a continuous linear map with $\|P_i(x)\|\leq\|x\|$ for each $x$ in $\mathcal X$.

(b) $\mathcal X$ is a Banach space if and only if each $\mathcal X_i$ is a Banach space.

(c) Each projection $P_i$ is an open map of $\mathcal X$ onto $\mathcal X_i$.

A similar result holds for $\bigoplus_0\mathcal X_n$, but the formulation and proof of this is left to the reader.

## EXERCISES

1. Show that if $\mathcal M\leq\mathcal X$, then (4.1) defines a norm on $\mathcal X/\mathcal M$.

2. Prove that $\mathcal X$ is a Banach space if and only if whenever $\{x_n\}$ is a sequence in $\mathcal X$ such that $\sum\|x_n\|<\infty$, then $\sum_{n=1}^{\infty}x_n$ converges in $\mathcal X$.

3. Show that if $(X,d)$ is a metric space and $\{x_n\}$ is a Cauchy sequence such that there is a subsequence $\{x_{n_k}\}$ that converges to $x_0$, then $x_n\to x_0$.

4. Find a Banach space $\mathcal X$ and a closed subspace $\mathcal M$ such that the natural map $Q:\mathcal X\to\mathcal X/\mathcal M$ is not a closed map. Can the natural map ever be a closed map?

5. Prove the converse of (4.2b): If $\mathcal X$ is a normed space, $\mathcal M\leq\mathcal H$, and both $\mathcal M$ and $\mathcal X/\mathcal M$ are complete, then $\mathcal X$ is complete. (This is an example of what is called a “two-out-of-three” result. If any two of $\mathcal X$, $\mathcal M$, and $\mathcal X/\mathcal M$ are complete, so is the third.)

6. Let $\mathcal M=\{x\in\ell^p:x(2n)=0\text{ for all }n\}$, $1\leq p\leq\infty$. Show that $\ell^p/\mathcal M$ is isometrically isomorphic to $\ell^p$.
