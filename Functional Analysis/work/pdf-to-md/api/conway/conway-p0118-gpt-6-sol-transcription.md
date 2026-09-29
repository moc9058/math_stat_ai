nonempty. Clearly $p(0)=0$. To see that $p(\alpha x)=|\alpha|p(x)$, we can suppose that $\alpha\ne0$. Hence, because $V$ is balanced,

$$
\begin{aligned}
p(\alpha x)
&=\inf\{t\geq0:\alpha x\in tV\}\\
&=\inf\left\{t\geq0:x\in t\left(\frac{1}{\alpha}V\right)\right\}\\
&=\inf\left\{t\geq0:x\in t\left(\frac{1}{|\alpha|}V\right)\right\}\\
&=|\alpha|\inf\left\{\frac{t}{|\alpha|}:x\in\frac{t}{|\alpha|}V\right\}\\
&=|\alpha|p(x).
\end{aligned}
$$

To complete the proof that $p$ is a seminorm, note that if $\alpha,\beta\geq0$ and $a,b\in V$, then

$$
\alpha a+\beta b=(\alpha+\beta)\left(\frac{\alpha}{\alpha+\beta}a+\frac{\beta}{\alpha+\beta}b\right)\in(\alpha+\beta)V
$$

by the convexity of $V$. If $x,y\in\mathscr X$, $p(x)=\alpha$, and $p(y)=\beta$, let $\delta>0$. Then $x\in(\alpha+\delta)V$ and $y\in(\beta+\delta)V$. (Why?) Hence $x+y\in(\alpha+\delta)V+(\beta+\delta)V=(\alpha+\beta+2\delta)V$ (Exercise 11). Letting $\delta\to0$ shows that $p(x+y)\leq\alpha+\beta=p(x)+p(y)$.

It remains to show that $V=\{x:p(x)<1\}$. If $p(x)=\alpha<1$, then $\alpha<\beta<1$ implies $x\in\beta V\subseteq V$ since $V$ is balanced. Thus $V\supseteq\{x:p(x)<1\}$. If $x\in V$, then $p(x)\leq1$. Since $V$ is absorbing at $x$, there is an $\varepsilon>0$ such that for $0<t<\varepsilon$, $x+tx=y\in V$. But $x=(1+t)^{-1}y$, $y\in V$. Hence $p(x)=(1+t)^{-1}p(y)\leq(1+t)^{-1}<1$.

Uniqueness follows by (III.1.4). $\blacksquare$

The seminorm $p$ defined in the preceding proposition is called the *Minkowski function* of $V$ or the *gauge* of $V$.

Note that if $\mathscr X$ is a TVS space and $V$ is an open set in $\mathscr X$, then $V$ is absorbing at each of its points.

Using Proposition 1.14, the following characterization of a LCS can be obtained. The proof is left to the reader.

**1.15. Proposition.** *Let $\mathscr X$ be a TVS and let $\mathscr U$ be the collection of all open convex balanced subsets of $\mathscr X$. Then $\mathscr X$ is locally convex if and only if $\mathscr U$ is a basis for the neighborhood system at $0$.*

## Exercises

1. Let $\mathscr X$ be a TVS and let $\mathscr U$ be all the open sets containing $0$. Prove the following.  
   (a) If $U\in\mathscr U$, there is a $V$ in $\mathscr U$ such that $V+V\subseteq U$.  
   (b) If $U\in\mathscr U$, there is a $V$ in $\mathscr U$ such that $V\subseteq U$ and $\alpha V\subseteq V$ for all $|\alpha|\leq1$. ($V$ is balanced.)  
   (Hint: If $W\in\mathscr U$ and $\alpha W\subseteq U$ for $|\alpha|\leq\varepsilon$, then $\varepsilon W\subseteq\beta U$ for $|\beta|\geq1$.)
