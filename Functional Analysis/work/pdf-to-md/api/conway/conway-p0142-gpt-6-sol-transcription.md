If $A$ is a linear manifold in $\mathcal X$ and $x^*\in A^\circ$, then $ta\in A$ for all $t>0$ and $a$ in $A$. So $1\geqslant|\langle ta,x^*\rangle|=t|\langle a,x^*\rangle|$. Letting $t\to\infty$ show that $A^\circ=A^\perp$, where

$$
A^\perp\equiv\{x^*\text{ in }\mathcal X^*:\langle a,x^*\rangle=0\text{ for all }a\text{ in }A\}.
$$

Similarly, if $B$ is a linear manifold in $\mathcal X^*$, ${}^\circ B={}^\perp B$, where

$$
{}^\perp B\equiv\{x\text{ in }\mathcal X:\langle x,b^*\rangle=0\text{ for all }b^*\text{ in }B\}.
$$

The next result is a slight generalization of Corollary IV.3.12.

**1.8. Bipolar Theorem.** *If $\mathcal X$ is a LCS and $A\subseteq\mathcal X$, then ${}^\circ A^\circ$ is the closed convex balanced hull of $A$.*

**PROOF.** Let $A_1$ be the intersection of all closed convex balanced subsets of $\mathcal X$ that contain $A$. It must be shown that $A_1={}^\circ A^\circ$. Since ${}^\circ A^\circ$ is closed, convex, and balanced and $A\subseteq{}^\circ A^\circ$, it follows that $A_1\subseteq{}^\circ A^\circ$.

Now assume that $x_0\in\mathcal X\setminus A_1$. $A_1$ is a closed convex balanced set so by (IV.3.13) there is an $x^*$ in $\mathcal X^*$, an $\alpha$ in $\mathbb R$, and an $\varepsilon>0$ such that

$$
\operatorname{Re}\langle a_1,x^*\rangle<\alpha<\alpha+\varepsilon<\operatorname{Re}\langle x_0,x^*\rangle
$$

for all $a_1$ in $A_1$. Since $0\in A_1$, $0=\langle0,x^*\rangle<\alpha$. By replacing $x^*$ with $\alpha^{-1}x^*$ it follows that there is an $\varepsilon>0$ (not the same as the first $\varepsilon$) such that

$$
\operatorname{Re}\langle a_1,x^*\rangle<1<1+\varepsilon<\operatorname{Re}\langle x_0,x^*\rangle
$$

for all $a_1$ in $A_1$. If $a_1\in A_1$ and $\langle a_1,x^*\rangle=|\langle a_1,x^*\rangle|e^{-i\theta}$, then $e^{-i\theta}a_1\in A_1$ and so

$$
|\langle a_1,x^*\rangle|=\operatorname{Re}\langle e^{-i\theta}a_1,x^*\rangle<1<\operatorname{Re}\langle x_0,x^*\rangle
$$

for all $a_1$ in $A_1$. Hence $x^*\in A_1^\circ$, and $x_0\notin{}^\circ A^\circ$. That is, $\mathcal X\setminus A_1\subseteq\mathcal X\setminus{}^\circ A^\circ$. $\blacksquare$

**1.9. Corollary.** *If $\mathcal X$ is a LCS and $B\subseteq\mathcal X^*$, then $({}^\circ B)^\circ$ is the wk$^*$ closed convex balanced hull of $B$.*

Using the weak and weak$^*$ topologies and the concept of a bounded subset of a LCS (IV.2.5), it is possible to rephrase the results associated with the Principle of Uniform Boundedness (§III.14). As an example we offer the following reformulation of Corollary III.14.5 (which is, in fact, the most general form of the result).

**1.10. Theorem.** *If $\mathcal X$ is a Banach space, $\mathcal Y$ is a normed space, and $\mathcal A\subseteq\mathcal B(\mathcal X,\mathcal Y)$ such that for every $x$ in $\mathcal X$, $\{Ax:A\in\mathcal A\}$ is weakly bounded in $\mathcal Y$, then $\mathcal A$ is norm bounded in $\mathcal B(\mathcal X,\mathcal Y)$.*

## EXERCISES

1. Show that wk is the smallest topology on $\mathcal X$ such that each $x^*$ in $\mathcal X^*$ is continuous.
2. Show that wk$^*$ is the smallest topology on $\mathcal X^*$ such that for each $x$ in $\mathcal X$, $x^*\mapsto\langle x,x^*\rangle$ is continuous.
