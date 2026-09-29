**11.1. Definition.** A *topological semigroup* is a semigroup $G$ that also is a topological space and such that the map $G\times G\to G$ defined by $(x,y)\mapsto xy$ is continuous. A *topological group* is a topological semigroup that is also a group such that the map $G\to G$ defined by $x\mapsto x^{-1}$ is continuous.

So a topological group is both a group and a topological space with a property that ties these two structures together.

$\mathbb{R}_{\geq 0}$ means the set of non-negative real numbers.

## 11.2. Examples

(a) $\mathbb{N}$ and $\mathbb{R}_{\geq 0}$ are topological semigroups under addition.

(b) $\mathbb{Z}$, $\mathbb{R}$, and $\mathbb{C}$ are topological groups under addition.

(c) $\partial\mathbb{D}$ is a topological group under multiplication.

(d) If $X$ is a topological space and $G=\{f\in C(X): f(X)\subset\partial\mathbb{D}\}$, define $(fg)(x)=f(x)g(x)$ for $f,g$ in $G$ and $x$ in $X$. Then $G$ is a group. If $G$ is given the topology of uniform convergence on $X$, $G$ is a topological group.

(e) For $n\geq 1$, let $M_n(\mathbb{C})=$ the $n\times n$ matrices with entries in $\mathbb{C}$; $O(n)\equiv\{A\in M_n(\mathbb{C}): A\text{ is invertible and }A^{-1}=A^*\}$; $SO(n)\equiv\{A\in O(n):\det A=1\}$. If $M_n(\mathbb{C})$ is given the usual topology, $O(n)$ and $SO(n)$ are compact topological groups under multiplication.

There are many more examples and the subject is a self-sustaining area of research. Some good references are Hewitt and Ross [1963] and Rudin [1962].

**11.3. Definition.** If $S$ is a semigroup and $f:S\to\mathbb{F}$, then for every $x$ in $S$ define $f_x:S\to\mathbb{F}$ and ${}_xf:S\to\mathbb{F}$ by $f_x(s)=f(sx)$ and ${}_xf(s)=f(xs)$ for all $s$ in $S$. If $S$ is also a group, let $f^\#(s)=f(s^{-1})$ for all $s$ in $S$.

**11.4. Theorem.** *If $G$ is a compact topological group, then there is a unique positive regular Borel measure $m$ on $G$ such that*

(a) $m(G)=1$;

(b) *if $U$ is a nonempty open subset of $G$, then* $m(U)>0$;

(c) *if $\Delta$ is any Borel subset of $G$ and $x\in G$, then* $m(\Delta)=m(\Delta x)=m(x\Delta)=m(\Delta^{-1})$, *where* $\Delta x\equiv\{ax:a\in\Delta\}$, $x\Delta\equiv\{xa:a\in\Delta\}$, *and* $\Delta^{-1}\equiv\{a^{-1}:a\in\Delta\}$.

The measure $m$ is called the *Haar measure* for $G$. If $G$ is locally compact, then it is also true that there is a positive Borel measure $m$ on $G$ satisfying (b) and such that $m(\Delta x)=m(\Delta)$ for all $x$ in $G$ and every Borel subset $\Delta$ of $G$. It is not necessarily true that $m(\Delta)=m(x\Delta)$, let alone that $m(\Delta)=m(\Delta^{-1})$ (see Exercise 4). The measure $m$ is necessarily unbounded if $G$ is not compact, so that (a) is not possible. Uniqueness, however, is still true in a modified form: if $m_1,m_2$ are two such measures, then $m_1=\alpha m_2$ for some $\alpha>0$.

By using the Riesz Representation Theorem for representing bounded linear functionals on $C(G)$, Theorem 11.4 is equivalent to the following.
