$\alpha\geqslant 1$, then $\|x/\alpha\|<r/\alpha\leqslant r$, and hence $\|x/\alpha\|_{\infty}<1$ by (3.2), a contradiction. Thus $\|x\|_{\infty}=\alpha<1$ and the claim is established.

By Lemma 1.4, $\|x\|_{\infty}\leqslant r^{-1}\|x\|$ for all $x$ and so the proof is complete. $\blacksquare$

**3.3. Proposition.** *If $\mathcal X$ is a normed space and $\mathcal M$ is a finite dimensional linear manifold in $\mathcal X$, then $\mathcal M$ is closed.*

**Proof.** Using a Hamel basis $\{e_1,\ldots,e_n\}$ for $\mathcal M$, define a norm $\|\cdot\|_{\infty}$ on $\mathcal M$ as in the proof of Theorem 3.1. It is easy to see that $\mathcal M$ is complete with respect to this new norm. But then Theorem 3.1 implies that $\mathcal M$ is complete with respect to its original norm and hence must be a closed subspace of $\mathcal X$. $\blacksquare$

**3.4. Proposition.** *Let $\mathcal X$ be a finite dimensional normed space and let $\mathcal Y$ be any normed space. If $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is continuous.*

**Proof.** Since all norms on $\mathcal X$ are equivalent and $T:\mathcal X\to\mathcal Y$ is continuous with respect to one norm on $\mathcal X$ precisely when it is continuous with respect to any equivalent norm, we may assume that $\|\sum_{j=1}^{d}\xi_j e_j\|=\max\{|\xi_j|:1\leqslant j\leqslant d\}$, where $\{e_j\}$ is a Hamel basis for $\mathcal X$. Thus, for $x=\sum_j\xi_j e_j$, $\|Tx\|=\|\sum_j\xi_jTe_j\|\leqslant\sum_j|\xi_j|\|Te_j\|\leqslant C\|x\|$, where $C=\sum_j\|Te_j\|$. By (2.1), $T$ is continuous. $\blacksquare$

**Exercises**

1. Show that if $\mathcal X$ is a locally compact normed space, then $\mathcal X$ is finite dimensional. (This same result, due to F Riesz, is valid in the more general topological vector spaces—see IV.1.1 for the definition. For a nice proof of this look at Pitcairn [1966].)

2. Show that $\|\cdot\|_{\infty}$ defined in the proof of Theorem 3.1 is a norm.

## §4. Quotients and Products of Normed Spaces

Let $\mathcal X$ be a normed space, let $\mathcal M$ be a linear manifold in $\mathcal X$, and let $Q:\mathcal X\to\mathcal X/\mathcal M$ be the natural map $Qx=x+\mathcal M$. We want to make $\mathcal X/\mathcal M$ into a normed space, so define

$$
\|x+\mathcal M\|=\inf\{\|x+y\|:y\in\mathcal M\}. \tag{4.1}
$$

Note that because $\mathcal M$ is a linear space, $\|x+\mathcal M\|=\inf\{\|x-y\|:y\in\mathcal M\}=\operatorname{dist}(x,\mathcal M)$, the distance from $x$ to $\mathcal M$. It is left to the reader to show that (4.1) defines a seminorm on $\mathcal X/\mathcal M$. But if $\mathcal M$ is not closed in $\mathcal X$, (4.1) cannot define a norm. (Why?) If, however, $\mathcal M$ is closed, then (4.1) does define a norm.

**4.2. Theorem.** *If $\mathcal M\leqslant\mathcal X$ and $\|x+\mathcal M\|$ is defined as in (4.1), then $\|\cdot\|$ is a norm on $\mathcal X/\mathcal M$. Also:*

(a) *$\|Q(x)\|\leqslant\|x\|$ for all $x$ in $\mathcal X$ and hence $Q$ is continuous.*

(b) *If $\mathcal X$ is a Banach space, then so is $\mathcal X/\mathcal M$.*
