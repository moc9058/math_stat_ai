$$
\begin{aligned}
&= \int \left[\int f(xy)\,dm(x)\right]d\mu(y)\\
&= \int \left[\int f(x)\,dm(x)\right]d\mu(y)\\
&= \int f\,dm.
\end{aligned}
$$

Hence $\mu=m$. $\blacksquare$

For further information on Haar measure see Nachbin [1965].

What happens if $G$ is only a semigroup? In this case $L_x$ and $R_x$ may not be isometries, so $\{L_xR_y:x,y\in G\}$ may not be noncontractive. However, there are measures for some semigroups that are invariant (see Exercise 7). For further reading see Greenleaf [1969].

## Exercises

1. Let $G$ be a group and a topological space. Show that $G$ is a topological group if and only if the map of $G\times G\to G$ defined by $(x,y)\mapsto x^{-1}y$ is continuous.

2. Verify the statements in (11.2).

3. Show that Theorems (11.4) and (11.5) are equivalent.

4. Let $G$ be a locally compact group. If $m$ is a regular Borel measure on $G$, show that any two of the following properties imply the third: (a) $m(\Delta x)=m(\Delta)$ for every Borel set $\Delta$ and every $x$ in $G$; (b) $m(x\Delta)=m(\Delta)$ for every Borel set $\Delta$ and every $x$ in $G$; (c) $m(\Delta)=m(\Delta^{-1})$ for every Borel set $\Delta$.

5. Show that the maps $S_0,L_x,R_x$ are linear isometries of $M(G)$ onto $M(G)$.

6. Prove (11.7).

7. Let $S$ be an abelian semigroup and show that there is a positive linear functional $L:l^\infty(S)\to\mathbb F$ such that (a) $L(1)=1$, (b) $L(f_x)=L(f)$ for every $f$ in $l^\infty(S)$.

8. If $S=\mathbb N$, what does Exercise 7 say about Banach limits?

9. If $G$ is a compact group, $f:G\to\mathbb F$ is a continuous function, and $\varepsilon>0$, show that there is a neighborhood $U$ of the identity in $G$ such that $|f(x)-f(y)|<\varepsilon$ whenever $xy^{-1}\in U$. (Note that this say that every continuous function on a compact group is uniformly continuous.)

10. If $G$ is a locally compact group and $f\in C_b(G)$, let $\mathcal O(f)\equiv$ the closure of $\{f_x:x\in G\}$ in $C_b(G)$. Let $AP(G)=\{f\in C_b(G):\mathcal O(f)\text{ is compact}\}$. Functions in $AP(G)$ are called *almost periodic*. (a) Show that every periodic function in $C_b(\mathbb R)$ belongs to $AP(\mathbb R)$. (b) If $G$ is compact, show that $AP(G)=C(G)$. (c) Show that if $f\in C_b(\mathbb R)$, then $f\in AP(\mathbb R)$ if and only if for every $\varepsilon>0$ there is a positive number $T$ such that in every interval of length $T$ there is a number $p$ such that $|f(x)-f(x+p)|<\varepsilon$ for all $x$ in $\mathbb R$. (d) If $G$ is not compact, then the only function in $AP(G)$ having compact support is the zero function. For more information on this topic, see Exercise 13.5 below.
