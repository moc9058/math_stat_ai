**10.2. Theorem.** If $\mathcal M\leqslant\mathcal X$ and $Q:\mathcal X\to\mathcal X/\mathcal M$ is the natural map, then $\rho(f)=f\circ Q$ defines an isometric isomorphism of $(\mathcal X/\mathcal M)^*$ onto $\mathcal M^\perp$.

**Proof.** If $f\in(\mathcal X/\mathcal M)^*$ and $y\in\mathcal M$, then $f\circ Q(y)=0$, so $f\circ Q\in\mathcal M^\perp$. Again, it is easy to see that $\rho:(\mathcal X/\mathcal M)^*\to\mathcal M^\perp$ is linear and, as was seen earlier, $\|\rho(f)\|\leqslant\|f\|$. Let $\{x_n+\mathcal M\}$ be a sequence in $\mathcal X/\mathcal M$ such that $\|x_n+\mathcal M\|<1$ and $|f(x_n+\mathcal M)|\to\|f\|$. For each $n$ there is a $y_n$ in $\mathcal M$ such that $\|x_n+y_n\|<1$. Thus $\|\rho(f)\|\geqslant|\rho(f)(x_n+y_n)|=|f(x_n+\mathcal M)|\to\|f\|$, so $\rho$ is an isometry.

To see that $\rho$ is surjective, let $g\in\mathcal M^\perp$; then $g\in\mathcal X^*$ and $g(\mathcal M)=0$. Define $f:\mathcal X/\mathcal M\to\mathbb F$ by $f(x+\mathcal M)=g(x)$. Because $g(\mathcal M)=0$, $f$ is well defined. Also, if $x\in\mathcal X$ and $y\in\mathcal M$, $|f(x+\mathcal M)|=|g(x)|=|g(x+y)|\leqslant\|g\|\|x+y\|$. Taking the infimum over all $y$ gives $|f(x+\mathcal M)|\leqslant\|g\|\|x+\mathcal M\|$. Hence $f\in(\mathcal X/\mathcal M)^*$, $\rho(f)=g$, and $\|f\|\leqslant\|\rho(f)\|$. $\blacksquare$

## §11. Reflexive Spaces

If $\mathcal X$ is a normed space, then we have seen that $\mathcal X^*$ is a Banach space (5.4). Because $\mathcal X^*$ is a Banach space, it too has a dual space $(\mathcal X^*)^*\equiv\mathcal X^{**}$ and $\mathcal X^{**}$ is a Banach space. Hence $\mathcal X^{**}$ has a dual. Can this be kept up?

Before answering this question, let’s examine a curious phenomenon. If $x\in\mathcal X$, then $x$ defines an element $\hat x$ of $\mathcal X^{**}$; namely, define $\hat x:\mathcal X^*\to\mathbb F$ by

$$
\hat x(x^*)=x^*(x)\tag{11.1}
$$

for every $x^*$ in $\mathcal X^*$. Note that Corollary 6.7 implies that $\|\hat x\|=\|x\|$ for all $x$ in $\mathcal X$. The map $x\to\hat x$ of $\mathcal X\to\mathcal X^{**}$ is called the *natural map* of $\mathcal X$ into its *second dual*.

**11.2. Definition.** A normed space $\mathcal X$ is *reflexive* if $\mathcal X^{**}=\{\hat x:x\in\mathcal X\}$, where $\hat x$ is defined in (11.1).

First note that a reflexive space $\mathcal X$ is isometrically isomorphic to $\mathcal X^{**}$, and hence must be a Banach space. It is not true however, that a Banach space $\mathcal X$ that is isometric to $\mathcal X^{**}$ is reflexive. The definition of reflexivity stipulates that the isometry be the natural embedding of $\mathcal X$ into $\mathcal X^{**}$. In fact, James [1951] gives an example of a nonreflexive space $\mathcal X$ that is isometric to $\mathcal X^{**}$.

**11.3. Example.** If $1<p<\infty$, $L^p(X,\Omega,\mu)$ is reflexive.

**11.4. Example.** $c_0$ is not reflexive. We know that $c_0^*=l^1$, so $c_0^{**}=(l^1)^*=l^\infty$. With these identifications, the natural map $c_0\to c_0^{**}$ is precisely the inclusion map $c_0\to l^\infty$.

A discussion of reflexivity is best pursued after the weak topology is understood (Chapter V). Until that time, we will say *adieu* to reflexivity.
