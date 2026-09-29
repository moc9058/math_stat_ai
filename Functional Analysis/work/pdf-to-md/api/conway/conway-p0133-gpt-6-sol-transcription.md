limit topology. Then

(a) the relative topology on $\mathcal X_i$ induced by $\mathcal T$ (viz., $\mathcal T|_{\mathcal X_i}$) is smaller than $\mathcal T_i$;

(b) if $\mathcal U$ is a locally convex topology on $\mathcal X$ such that for every $i$, $\mathcal U|_{\mathcal X_i}\subseteq\mathcal T_i$, then $\mathcal U\subseteq\mathcal T$;

(c) a seminorm $p$ on $\mathcal X$ is continuous if and only if $p|_{\mathcal X_i}$ is continuous for each $i$.

**Proof.** Exercise 3.

**5.7. Proposition.** Let $(\mathcal X,\mathcal T)$ be the inductive limit of the spaces $\{(\mathcal X_i,\mathcal T_i):i\in I\}$. If $\mathcal Y$ is a LCS and $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is continuous if and only if the restriction of $T$ to each $\mathcal X_i$ is $\mathcal T_i$-continuous.

**Proof.** Suppose $T:\mathcal X\to\mathcal Y$ is continuous. By (5.6a), the inclusion map $(\mathcal X_i,\mathcal T_i)\to(\mathcal X,\mathcal T)$ is continuous. Since the restriction of $T$ to $\mathcal X_i$ is the composition of the inclusion map $\mathcal X_i\to\mathcal X$ and $T$, the restriction is continuous.

Now assume that each restriction is continuous. If $p$ is a continuous seminorm on $\mathcal Y$, then $p\circ T|_{\mathcal X_i}$ is a $\mathcal T_i$-continuous seminorm for every $i$. By (5.6c), $p\circ T$ is continuous on $\mathcal X$. By Exercise 1.23, $T$ is continuous. ■

It may have occurred to the reader that the definition of the inductive limit topology depends on the choice of the spaces $\mathcal X_i$ in more than the obvious way. That is, if $\mathcal X=\bigcup_j\mathcal Y_j$ and each $\mathcal Y_j$ has a topology that is “compatible” with that of the spaces $\{\mathcal X_i\}$, perhaps the inductive limit topology defined by the spaces $\{\mathcal Y_j\}$ will differ from that defined by the $\{\mathcal X_i\}$. This is not the case.

**5.8. Proposition.** Let $(\mathcal X,\{(\mathcal X_i,\mathcal T_i)\})$ and $(\mathcal X,\{(\mathcal Y_j,\mathcal U_j)\})$ be two inductive systems and let $\mathcal T$ and $\mathcal U$ be the corresponding inductive limit topologies on $\mathcal X$. If for every $i$ there is a $j$ such that $\mathcal X_i\subseteq\mathcal Y_j$ and $\mathcal U_j|_{\mathcal X_i}\subseteq\mathcal T_i$, then $\mathcal U\subseteq\mathcal T$.

**Proof.** Let $V$ be a convex balanced subset of $\mathcal X$ such that for every $j$, $V\cap\mathcal Y_j\in\mathcal U_j$. If $\mathcal X_i$ is given, let $j$ be such that $\mathcal X_i\subseteq\mathcal Y_j$ and $\mathcal U_j|_{\mathcal X_i}\subseteq\mathcal T_i$. Hence $V\cap\mathcal X_i=(V\cap\mathcal Y_j)\cap\mathcal X_i\in\mathcal T_i$. Thus $V\in\mathcal B$ [as defined in (5.3)]. It now follows that $\mathcal U\subseteq\mathcal T$. ■

**5.9. Example.** Let $\mathcal X$ be any vector space and let $\{\mathcal X_i:i\in I\}$ be all of the finite dimensional subspaces of $\mathcal X$. Give each $\mathcal X_i$ the unique topology from its identification with a Euclidean space. Then $(\mathcal X,\{\mathcal X_i\})$ is an inductive system. Let $\mathcal T$ be the inductive limit topology. If $\mathcal Y$ is a LCS and $T:\mathcal X\to\mathcal Y$ is a linear transformation, then $T$ is $\mathcal T$-continuous.

**5.10. Example.** Let $X$ be a locally compact space and let $\{K_i:i\in I\}$ be the collection of all compact subsets of $X$. Let $\mathcal X_i$ = all $f$ in $C(X)$ such that $\operatorname{spt}f\subseteq K_i$. Then $\bigcup_i\mathcal X_i=C_c(X)$, the continuous functions on $X$ with compact support. Topologize each $\mathcal X_i$ by giving it the supremum norm. Then $(C_c(X),\{\mathcal X_i\})$ is an inductive system.
