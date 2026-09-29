all convex. In fact, if $T:\mathscr{X}\to\mathscr{Y}$ is a real linear map and $C$ is a convex subset of $\mathscr{Y}$, then $T^{-1}(C)$ is convex in $\mathscr{X}$.

**1.11. Proposition.** *Let $\mathscr{X}$ be a TVS and let $A$ be a convex subset of $\mathscr{X}$. Then (a) $\operatorname{cl}A$ is convex; (b) if $a\in\operatorname{int}A$ and $b\in\operatorname{cl}A$, then $[a,b)\equiv\{tb+(1-t)a:0\leq t<1\}\subseteq\operatorname{int}A$.*

**Proof.** Let $a\in A$, $b\in\operatorname{cl}A$, and $0\leq t\leq1$. Let $\{x_i\}$ be a net in $A$ such that $x_i\to b$. Then $tx_i+(1-t)a\to tb+(1-t)a$. This shows that

$$
\tag{1.12}
b\text{ in }\operatorname{cl}A\text{ and }a\text{ in }A\text{ imply }[a,b]\subseteq\operatorname{cl}A.
$$

Using (1.12) it is easy to show that $\operatorname{cl}A$ is convex. To prove (b), fix $t$, $0<t<1$, and put $c=tb+(1-t)a$, where $a\in\operatorname{int}A$ and $b\in\operatorname{cl}A$. There is an open set $V$ in $\mathscr{X}$ such that $0\in V$ and $a+V\subseteq A$. (Why?) Hence for any $d$ in $A$

$$
\begin{aligned}
A&\supseteq td+(1-t)(a+V)\\
 &=t(d-b)+tb+(1-t)(a+V)\\
 &=[t(d-b)+(1-t)V]+c.
\end{aligned}
$$

If it can be shown that there is an element $d$ in $A$ such that $0\in t(d-b)+(1-t)V=U$, then the preceding inclusion shows that $c\in\operatorname{int}A$ since $U$ is open (Exercise 4). Note that the finding of such a $d$ in $A$ is equivalent to finding a $d$ such that $0\in t^{-1}(1-t)V+(d-b)$ or $d\in b-t^{-1}(1-t)V$. But $0\in-t^{-1}(1-t)V$ and this set is open. Since $b\in\operatorname{cl}A$, $d$ can be found in $A$. ■

**1.13. Corollary.** *If $A\subseteq\mathscr{X}$, then $\overline{\operatorname{co}}(A)$ is the closure of $\operatorname{co}(A)$.*

A set $A\subseteq\mathscr{X}$ is *balanced* if $\alpha x\in A$ whenever $x\in A$ and $|\alpha|\leq1$. A set $A$ is *absorbing* if for each $x$ in $\mathscr{X}$ there is an $\varepsilon>0$ such that $tx\in A$ for $0\leq t<\varepsilon$. Note that an absorbing set must contain the origin. If $a\in A$, then $A$ is *absorbing at $a$* if the set $A-a$ is absorbing. Equivalently, $A$ is absorbing at $a$ if for every $x$ in $\mathscr{X}$ there is an $\varepsilon>0$ such that $a+tx\in A$ for $0\leq t<\varepsilon$.

If $\mathscr{X}$ is a vector space and $p$ is a seminorm, then $V=\{x:p(x)<1\}$ is a convex balanced set that is absorbing at each of its points. It is rather remarkable that the converse of this is true. This fact will be used to give an abstract formulation of a LCS and also to explore some geometric consequences of the Hahn–Banach Theorem.

**1.14. Proposition.** *If $\mathscr{X}$ is a vector space over $\mathbb{F}$ and $V$ is a nonempty convex, balanced set that is absorbing at each of its points, then there is a unique seminorm $p$ on $\mathscr{X}$ such that $V=\{x\in\mathscr{X}:p(x)<1\}$.*

**Proof.** Define $p(x)$ by

$$
p(x)=\inf\{t:t\geq0\text{ and }x\in tV\}.
$$

Since $V$ is absorbing, $\mathscr{X}=\bigcup_{n=1}^{\infty}nV$, so that the set whose infimum is $p(x)$ is
