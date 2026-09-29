8. Give an example of an invertible operator $T$ on a Banach space $\mathcal X$ and an invariant subspace $\mathcal M$ for $T$ such that $\mathcal M$ is not invariant for $T^{-1}$.

9. Let $\mathcal X$ be a Banach space over $\mathbb C$, let $K\in\mathcal B_0(\mathcal X)$ and show that if $\mathcal C$ is a maximal chain in $\operatorname{Lat}K$, then $\mathcal C$ is a maximal chain in the lattice of all subspaces of $\mathcal X$.

## §5. Weakly Compact Operators

**5.1. Definition.** If $\mathcal X$ and $\mathcal Y$ are Banach spaces, an operator $T$ in $\mathcal B(\mathcal X,\mathcal Y)$ is *weakly compact* if the closure of $T(\operatorname{ball}\mathcal X)$ is weakly compact.

Weakly compact operators are generalizations of compact operators, but the hypothesis is not sufficiently strong to yield good information about their structure.

Recall that in a reflexive Banach space the weak closure of any bounded set is weakly compact. Also, a bounded operator $T:\mathcal X\to\mathcal Y$ is continuous if both $\mathcal X$ and $\mathcal Y$ have their weak topologies (1.1). With these facts in mind, the proof of the next result becomes an easy exercise for the reader.

**5.2. Proposition.**

(a) *If either $\mathcal X$ or $\mathcal Y$ is reflexive, then every operator in $\mathcal B(\mathcal X,\mathcal Y)$ is weakly compact.*

(b) *If $T:\mathcal X\to\mathcal Y$ is weakly compact and $A\in\mathcal B(\mathcal Y,\mathcal X)$, then $AT$ is weakly compact.*

(c) *If $T:\mathcal X\to\mathcal Y$ is weakly compact and $B\in\mathcal B(\mathcal X,\mathcal X)$, then $TB$ is weakly compact.*

This proposition shows that assuming that an operator is weakly compact is not that strong an assumption. For example, if $\mathcal X$ is reflexive, every operator in $\mathcal B(\mathcal X)$ is weakly compact. In particular, every operator on a Hilbert space is weakly compact. So any theorem about weakly compact operators is a theorem about all operators on a reflexive space.

In fact, there is a degree of validity for the converse of this statement. In a certain sense, theorems about operators on reflexive spaces are also theorems about weakly compact operators. The precise meaning of this statement is the content of Theorem 5.4 below. But before we begin to prove this, a lemma is needed.

Let $\mathcal Y$ be a Banach space and let $W$ be a bounded convex balanced subset of $\mathcal Y$. For $n>1$ put $U_n=2^nW+2^{-n}\operatorname{int}[\operatorname{ball}\mathcal Y]$. Let $p_n=$ the gauge of $U_n$ (IV.1.14). Because $U_n\supseteq 2^{-n}\operatorname{int}[\operatorname{ball}\mathcal Y]$, it is easy to check that $p_n$ is a norm on $\mathcal Y$. In fact, $p_n$ and $\|\cdot\|$ are equivalent norms. To see this note that if $\|y\|<1$, then $2^{-n}y\in U_n$ so that $p_n(y)<2^n$. Hence $p_n(y)\leqslant 2^n\|y\|$. Also, because $W$ is bounded, $U_n$ must be bounded; let $M>\sup\{\|y\|:y\in U_n\}$. So if $p_n(y)<1$, $\|y\|<M$. Thus $\|y\|\leqslant Mp_n(y)$, and $\|\cdot\|$ and $p_n$ are equivalent norms.
