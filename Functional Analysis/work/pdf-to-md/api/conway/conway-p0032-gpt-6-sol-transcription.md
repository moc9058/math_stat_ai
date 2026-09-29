(e) If $g$ and $h\in\mathcal H$, then

$$
\langle g,h\rangle=\sum\{\langle g,e\rangle\langle e,h\rangle:e\in\mathcal E\}.
$$

(f) If $h\in\mathcal H$, then $\|h\|^2=\sum\{|\langle h,e\rangle|^2:e\in\mathcal E\}$ (Parseval’s Identity).

**Proof.** (a)$\Rightarrow$(b): Suppose $h\perp\mathcal E$ and $h\ne0$; then $\mathcal E\cup\{h/\|h\|\}$ is an orthonormal set that properly contains $\mathcal E$, contradicting maximality.

(b)$\Leftrightarrow$(c): By Corollary 2.11, $\bigvee\mathcal E=\mathcal H$ if and only if $\mathcal E^\perp=(0)$.

(b)$\Rightarrow$(d): If $h\in\mathcal H$, then $f=h-\sum\{\langle h,e\rangle e:e\in\mathcal E\}$ is a well-defined vector by Lemma 4.12. If $e_1\in\mathcal E$, then $\langle f,e_1\rangle=\langle h,e_1\rangle-\sum\{\langle h,e\rangle\langle e,e_1\rangle:e\in\mathcal E\}=\langle h,e_1\rangle-\langle h,e_1\rangle=0$. That is, $f\in\mathcal E^\perp$. Hence $f=0$. (Is everything legitimate in that string of equalities? We don’t want any illegitimate equalities.)

(d)$\Rightarrow$(e): This is left as an exercise for the reader.

(e)$\Rightarrow$(f): Since $\|h\|^2=\langle h,h\rangle$, this is immediate.

(f)$\Rightarrow$(a): If $\mathcal E$ is not a basis, then there is a unit vector $e_0$ ($\|e_0\|=1$) in $\mathcal H$ such that $e_0\perp\mathcal E$. Hence, $0=\sum\{|\langle e_0,e\rangle|^2:e\in\mathcal E\}$, contradicting (f). $\blacksquare$

Just as in finite dimensional spaces, a basis in Hilbert space can be used to define a concept of dimension. For this purpose the next result is pivotal.

**4.14. Proposition.** *If $\mathcal H$ is a Hilbert space, any two bases have the same cardinality.*

**Proof.** Let $\mathcal E$ and $\mathcal F$ be two bases for $\mathcal H$ and put $\varepsilon=$ the cardinality of $\mathcal E$, $\eta=$ the cardinality of $\mathcal F$. If $\varepsilon$ or $\eta$ is finite, then $\varepsilon=\eta$ (Exercise 15). Suppose both $\varepsilon$ and $\eta$ are infinite. For $e$ in $\mathcal E$, let $\mathcal F_e\equiv\{f\in\mathcal F:\langle e,f\rangle\ne0\}$; so $\mathcal F_e$ is countable. By (4.13b), each $f$ in $\mathcal F$ belongs to at least one set $\mathcal F_e$, $e$ in $\mathcal E$. That is, $\mathcal F=\bigcup\{\mathcal F_e:e\in\mathcal E\}$. Hence $\eta\leq\varepsilon\cdot\aleph_0=\varepsilon$. Similarly, $\varepsilon\leq\eta$. $\blacksquare$

**4.15. Definition.** The *dimension* of a Hilbert space is the cardinality of a basis and is denoted by $\dim\mathcal H$.

If $(X,d)$ is a metric space that is separable and $\{B_i=B(x_i;\varepsilon_i):i\in I\}$ is a collection of pairwise disjoint open balls in $X$, then $I$ must be countable. Indeed, if $D$ is a countable dense subset of $X$, $B_i\cap D\ne\square$ for each $i$ in $I$. Thus there is a point $x_i$ in $B_i\cap D$. So $\{x_i:i\in I\}$ is a subset of $D$ having the cardinality of $I$; thus $I$ must be countable.

**4.16. Proposition.** *If $\mathcal H$ is an infinite dimensional Hilbert space, then $\mathcal H$ is separable if and only if $\dim\mathcal H=\aleph_0$.*

**Proof.** Let $\mathcal E$ be a basis for $\mathcal H$. If $e_1,e_2\in\mathcal E$, then $\|e_1-e_2\|^2=\|e_1\|^2+\|e_2\|^2=2$. Hence $\{B(e;1/\sqrt{2}):e\in\mathcal E\}$ is a collection of pairwise disjoint open balls in $\mathcal H$. From the discussion preceding this proposition, the assumption that $\mathcal H$ is separable implies $\mathcal E$ is countable. The converse is an exercise. $\blacksquare$
