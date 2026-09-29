3. Where were the hypotheses of the separability and completeness of $\mathcal X$ used in the proof of Theorem 12.11?

4. Let $\mathcal X$ be a separable Banach space. If $\mathcal M$ is a linear manifold in $\mathcal X^*$ give necessary and sufficient conditions that every functional in $\operatorname{wk}^*\text{-}\operatorname{cl}\mathcal M$ be the $\operatorname{wk}^*$ limit of a sequence from $\mathcal M$.

5. Let $\mathcal X$ be a normed space and let $\mathcal T$ be a locally convex topology on $\mathcal X$ such that $\operatorname{ball}\mathcal X$ is $\mathcal T$-compact. Show that there is a Banach space $\mathcal Y$ such that $\mathcal X$ is isometrically isomorphic to $\mathcal Y^*$. (Hint: Let $\mathcal Y=\{x^*\in\mathcal X^*:x^*|_{\operatorname{ball}\mathcal X}\text{ is }\mathcal T\text{-continuous}\}$.)

6. If $X$ is a compact connected topological space that is not a singleton, show that $C(X)$ is not the dual of a Banach space. (For $C_{\mathbb R}(X)$ this is a consequence of Exercise 7.4. For the complex case, show that if $C(X)$ is a dual space, then $C_{\mathbb R}(X)$ is a weak* closed real linear subspace of $C(X)$. Hint (S. Axler): Suppose $\{u_j\}$ is a net in $\operatorname{ball}C_{\mathbb R}(X)$ such that $u_j\to u+iv$ weak*. If $v(x)=t>0$, choose $n$ such that $1+n^2<(n+t)^2$ and examine the net $\{u_j+in\}$.)

## §13*. Weak Compactness

In this section, two results are stated without proof. These results are among the deepest in the study of weak topologies.

**13.1. The Eberlein–Smulian Theorem.** *If $\mathcal X$ is a Banach space and $A\subseteq\mathcal X$, then the following statements are equivalent.*

(a) *Each sequence of elements of $A$ has a subsequence that is weakly convergent.*

(b) *Each sequence of elements of $A$ has a weak cluster point.*

(c) *The weak closure of $A$ is weakly compact.*

An elementary proof of the Eberlein–Smulian Theorem can be found in Whitley [1967] and Kremp [1986]. Another proof can be found in Dunford and Schwartz [1958], p. 430. The serious student should examine Chapter V of Dunford and Schwartz [1958] for several results not presented here as well as for some of the history behind the material of this chapter.

The following is a consequence of the Eberlein–Smulian Theorem.

**13.2. Corollary.** *If $\mathcal X$ is a Banach space and $A\subseteq\mathcal X$, then $A$ is weakly compact if and only if $A\cap\mathcal M$ is weakly compact for every separable subspace $\mathcal M$ of $\mathcal X$.*

If $\mathcal X$ is Banach space and $A$ is a weakly compact subset of $\mathcal X$, then for each $x^*$ in $\mathcal X^*$ there is an $x_0$ in $A$ such that $|\langle x_0,x^*\rangle|=\sup\{|\langle x,x^*\rangle|:x\in A\}$. It is a rather deep fact due to R.C. James [1964a] that the converse is true.

**13.3. James’s Theorem.** *If $\mathcal X$ is a Banach space and $A$ is a closed convex subset of $\mathcal X$ such that for each $x^*$ in $\mathcal X^*$ there is an $x_0$ in $A$ with*

$$
|\langle x_0,x^*\rangle|=\sup\{|\langle x,x^*\rangle|:x\in A\},
$$

*then $A$ is weakly compact.*
