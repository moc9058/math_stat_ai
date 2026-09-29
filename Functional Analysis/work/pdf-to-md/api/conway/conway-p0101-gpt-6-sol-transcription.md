## §9*. An Application: Ordered Vector Spaces

In this section only vector spaces over $\mathbf{R}$ are considered.

There are numerous spaces in which there is a notion of $\leq$ in addition to the vector space structure. The $L^p$ spaces and $C(X)$ are some that spring to mind. The concept of an ordered vector space is an attempt to study such spaces in an abstract setting. The first step is to abstract the notion of the positive elements.

**9.1. Definition.** An *ordered vector space* is a pair $(\mathscr{X},\leq)$ where $\mathscr{X}$ is a vector space over $\mathbf{R}$ and $\leq$ is a relation on $\mathscr{X}$ satisfying

(a) $x\leq x$ for all $x$;  
(b) if $x\leq y$ and $y\leq z$, then $x\leq z$;  
(c) if $x\leq y$ and $z\in\mathscr{X}$, then $x+z\leq y+z$;  
(d) if $x\leq y$ and $\alpha\in[0,\infty)$, then $\alpha x\leq\alpha y$.

Note that it is not assumed that $\leq$ is *antisymmetric*. That is, it is not assumed that if $x\leq y$ and $y\leq x$, then $x=y$.

**9.2. Definition.** If $\mathscr{X}$ is a real vector space, a *wedge* is a nonempty subset $P$ of $\mathscr{X}$ such that

(a) if $x,y\in P$, then $x+y\in P$;  
(b) if $x\in P$ and $\alpha\in[0,\infty)$, then $\alpha x\in P$.

**9.3. Proposition.** *(a) If $(\mathscr{X},\leq)$ is an ordered vector space and $P=\{x\in\mathscr{X}:x\geq0\}$, then $P$ is a wedge. (b) If $P$ is a wedge in the real vector space $\mathscr{X}$ and $\leq$ is defined on $\mathscr{X}$ by declaring $x\leq y$ if and only if $y-x\in P$, then $(\mathscr{X},\leq)$ is an ordered vector space.*

**Proof.** Exercise.

If $(\mathscr{X},\leq)$ is an ordered vector space, $P=\{x\in\mathscr{X}:x\geq0\}$ is called the *wedge of positive elements*. The next result is also left as an exercise.

**9.4. Proposition.** *If $(\mathscr{X},\leq)$ is an ordered vector space and $P$ is the wedge of positive elements, $\leq$ is antisymmetric if and only if $P\cap(-P)=(0)$.*

**9.5. Definition.** A *cone* in $\mathscr{X}$ is a wedge $P$ such that $P\cap(-P)=(0)$.

**9.6. Definition.** If $(\mathscr{X},\leq)$ is an ordered vector space, a subset $A$ of $\mathscr{X}$ is *cofinal* if for every $x\geq0$ in $\mathscr{X}$ there is an $a$ in $A$ such that $a\geq x$. An element $e$ of $\mathscr{X}$ is an *order unit* if for every $x$ in $\mathscr{X}$ there is a positive integer $n$ such that $-ne\leq x\leq ne$.
