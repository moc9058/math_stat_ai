7. Let $X$ be a normal locally compact space and $F$ a closed subset of $X$. If $\mathcal M\equiv\{f\in C_0(X):f(x)=0\text{ for all }x\text{ in }F\}$, then $C_0(X)/\mathcal M$ is isometrically isomorphic to $C_0(F)$.

8. Prove Proposition 4.4.

9. Formulate and prove a version of Proposition 4.4 for $\bigoplus_0\mathcal X_n$.

10. If $\{\mathcal X_1,\ldots,\mathcal X_n\}$ is a finite collection of normed spaces and $1\leq p\leq\infty$, show that the norms on $\bigoplus_p\mathcal X_k$ are all equivalent.

11. Here is an abstraction of Proposition 4.4. Suppose $\{\mathcal X_i:i\in I\}$ is a collection of normed spaces and $Y$ is a normed space contained in $\mathbb F^I$. Define $\mathcal X\equiv\{x\in\prod_i\mathcal X_i:\text{ there is a }y\text{ in }Y\text{ with }\|x(i)\|\leq y(i)\text{ for all }i\}$. If $x\in\mathcal X$, define $\|x\|\equiv\inf\{\|y\|:\|x(i)\|\leq y(i)\text{ for all }i\}$. Then $(\mathcal X,\|\cdot\|)$ is a normed space. Give necessary and sufficient conditions on $Y$ that each of the parts of (4.4) be valid for $\mathcal X$.

12. Let $\mathcal X$ be a normed space and $\mathcal M\leq\mathcal X$. (a) If $\mathcal X$ is separable, so is $\mathcal X/\mathcal M$. (b) If $\mathcal X/\mathcal M$ and $\mathcal M$ are separable, then $\mathcal X$ is separable. (c) Give an example such that $\mathcal X/\mathcal M$ is separable but $\mathcal X$ is not.

13. Let $\{\mathcal X_i:i\in I\}$ be a collection of non-zero normed spaces. For $1\leq p<\infty$, put $\mathcal X=\bigoplus_p\mathcal X_i$. Show that $\mathcal X$ is separable if and only if $I$ is countable and each $\mathcal X_i$ is separable. Show that $\bigoplus_\infty\mathcal X_i$ is separable if and only if $I$ is finite and each $\mathcal X_i$ is separable.

14. Show that $\bigoplus_0\mathcal X_n$ is separable if and only if each $\mathcal X_n$ is separable.

15. Let $J\subseteq I$, and $\mathcal X\equiv\bigoplus_p\{\mathcal X_i:i\in I\}$, $\mathcal M\equiv\{x\in\mathcal X:x(j)=0\text{ for }j\text{ in }J\}$. Show that $\mathcal X/\mathcal M$ is isometrically isomorphic to $\bigoplus_p\{\mathcal X_j:j\in J\}$.

16. Let $\mathcal H$ be a Hilbert space and suppose $\mathcal M\leq\mathcal H$. Show that if $Q:\mathcal H\to\mathcal H/\mathcal M$ is the natural map, then $Q:\mathcal M^\perp\to\mathcal H/\mathcal M$ is an isometric isomorphism.

## §5. Linear Functionals

Let $\mathcal X$ be a vector space over $\mathbb F$. A *hyperplane* in $\mathcal X$ is a linear manifold $\mathcal M$ in $\mathcal X$ such that $\dim(\mathcal X/\mathcal M)=1$. If $f:\mathcal X\to\mathbb F$ is a linear functional and $f\ne0$, then $\ker f$ is a hyperplane. In fact, $f$ induces an isomorphism between $\mathcal X/\ker f$ and $\mathbb F$. Conversely, if $\mathcal M$ is a hyperplane, let $Q:\mathcal X\to\mathcal X/\mathcal M$ be the natural map and let $T:\mathcal X/\mathcal M\to\mathbb F$ be an isomorphism. Then $f\equiv T\circ Q$ is a linear functional on $\mathcal X$ and $\ker f=\mathcal M$.

Suppose now that $f$ and $g$ are linear functionals on $\mathcal X$ such that $\ker f=\ker g$. Let $x_0\in\mathcal X$ such that $f(x_0)=1$; so $g(x_0)\ne0$. If $x\in\mathcal X$ and $\alpha=f(x)$, then $x-\alpha x_0\in\ker f=\ker g$. So $0=g(x)-\alpha g(x_0)$, or $g(x)=(g(x_0))\alpha=(g(x_0))f(x)$. Thus $g=\beta f$ for a scalar $\beta$. This is summarized as follows.

**5.1. Proposition.** *A linear manifold in $\mathcal X$ is a hyperplane if and only if it is the kernel of a non-zero linear functional. Two linear functionals have the same kernel if and only if one is a non-zero multiple of the other.*
