§5. Inductive Limits and the Space of Distributions  117

where $k=(k_1,\ldots,k_d)$, $k_j\in\mathbb{N}\cup\{0\}$, $|k|=k_1+\cdots+k_d$, and

$$
\phi^{(k)}=\frac{\partial^{|k|}\phi}{\partial x_1^{k_1}\cdots\partial x_d^{k_d}}.
$$

Then $(C_c^{(\infty)}(\Omega),\{\mathcal{D}(K): K\text{ is compact in }\Omega\})$ is an inductive system. The space $C_c^{(\infty)}(\Omega)$ is often denoted in the literature by $\mathcal{D}(\Omega)$, as it will be in this book.

This example of an inductive system is the most important one as it is connected with the theory of distributions (below). In fact, this example was the inspiration for the definition of an inductive limit given now.

**5.3. Proposition.** *If $(\mathcal{X},\{\mathcal{X}_i,\mathcal{T}_i\})$ is an inductive system, let $\mathcal{B}=$ all convex balanced sets $V$ such that $V\cap\mathcal{X}_i\in\mathcal{T}_i$ for all $i$. Let $\mathcal{T}=$ the collection of all subsets $U$ of $\mathcal{X}$ such that for every $x_0$ in $U$ there is a $V$ in $\mathcal{B}$ with $x_0+V\subseteq U$. Then $(\mathcal{X},\mathcal{T})$ is a (not necessarily Hausdorff) LCS.*

Before proving this proposition, it seems appropriate to make the following definition.

**5.4. Definition.** If $(\mathcal{X},\{\mathcal{X}_i\})$ is an inductive system and $\mathcal{T}$ is the topology defined in (5.3), $\mathcal{T}$ is called the *inductive limit topology* and $(\mathcal{X},\mathcal{T})$ is said to be the inductive limit of $\{\mathcal{X}_i\}$.

**5.5. Lemma.** *With the notation as in (5.3), $\mathcal{B}\subseteq\mathcal{T}$.*

**PROOF.** Fix $V$ is $\mathcal{B}$. It will be shown that $V$ is absorbing at each of its points. Indeed, if $x_0\in V$ and $x\in\mathcal{X}$, then there is an $\mathcal{X}_i$ and an $\mathcal{X}_j$ such that $x_0\in\mathcal{X}_i$ and $x\in\mathcal{X}_j$. Since $I$ is directed, there is a $k$ in $I$ with $k\geq i,j$. Hence $x_0,x\in\mathcal{X}_k$. But $V\cap\mathcal{X}_k\in\mathcal{T}_k$. Thus there is an $\varepsilon>0$ such that $x_0+\alpha x\in V\cap\mathcal{X}_k\subseteq V$ for $|\alpha|<\varepsilon$.

Since $V$ is convex, balanced, and absorbing at each of its points, there is a seminorm $p$ on $\mathcal{X}$ such that $V=\{x\in\mathcal{X}:p(x)<1\}$ (1.14). So if $x_0\in V$, $p(x_0)=r_0<1$. Let $W=\{x\in\mathcal{X}:p(x)<\frac12(1-r_0)\}$. Then $W=\frac12(1-r_0)V$ and so $W\in\mathcal{B}$. Since $x_0+W\subseteq V$, $V\in\mathcal{T}$. ■

**PROOF OF PROPOSITION 5.3.** The proof that $\mathcal{T}$ is a topology is left as an exercise. To see that $(\mathcal{X},\mathcal{T})$ is a LCS, note that Lemma 5.5 and Theorem 1.14 imply that $\mathcal{T}$ is defined by a family of seminorms. ■

For all we know the inductive limit topology may be trivial. However, the fact that this topology has not been shown to be Hausdorff need not concern us, since we will concentrate on a particular type of inductive limit which will be shown to be Hausdorff. But for the moment we will continue at the present level of generality.

**5.6. Proposition.** *Let $(\mathcal{X},\{\mathcal{X}_i\})$ be an inductive system and let $\mathcal{T}$ be the inductive*
