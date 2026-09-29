**2.5. Proposition.** *If $f:X\to Y$, $f$ is continuous at $x_0$, and $\{x_i\}$ is a net in $X$ that clusters at $x_0$, then $\{f(x_i)\}$ clusters at $f(x_0)$.*

**Proof.** Exercise.

**2.6. Proposition.** *Let $K\subseteq X$. Then $K$ is compact if and only if each net in $K$ has a cluster point in $K$.*

**Pproof.** Suppose that $K$ is compact and let $\{x_i:i\in I\}$ be a net in $K$. For each $i$ let $F_i=\operatorname{cl}\{x_j:j\geq i\}$, so each $F_i$ is a closed subset of $K$. It will be shown that $\{F_i:i\in I\}$ has the finite intersection property. In fact, since $I$ is directed, if $i_1,\ldots,i_n\in I$, then there is an $i\geq i_1,\ldots,i_n$. Thus $F_i\subseteq\bigcap_{k=1}^{n}F_{i_k}$ and $\{F_i\}$ has the finite intersection property. Because $K$ is compact, there is an $x_0$ in $\bigcap_i F_i$. But if $U$ is open with $x_0$ in $U$ and $i_0\in I$, the fact that $x_0\in\operatorname{cl}\{x_i:i\geq i_0\}$ implies there is an $i\geq i_0$ with $x_i$ in $U$. Thus $x_i\xrightarrow[\mathrm{cl}]{}x_0$.

Now assume that each net in $K$ has a cluster point in $K$. Let $\{K_\alpha:\alpha\in A\}$ be a collection of relatively closed subsets of $K$ having the finite intersection property. If $\mathcal{F}=$ the collection of all finite subsets of $A$, order $\mathcal{F}$ by inclusion. By hypothesis, if $F\in\mathcal{F}$, there is a point $x_F$ in $\bigcap\{K_\alpha:\alpha\in F\}$. Thus $\{x_F\}$ is a net in $K$. By hypothesis, $\{x_F\}$ has a cluster point $x_0$ in $K$. Let $\alpha\in A$, so $\{\alpha\}\in\mathcal{F}$. Thus if $U$ is any open set containing $x_0$ there is an $F$ in $\mathcal{F}$ such that $\alpha\in F$ and $x_F\in U$. Thus $x_F\in U\cap K_\alpha$; that is, for each $\alpha$ in $A$ and for every open set $U$ containing $x_0$, $U\cap K_\alpha\ne\square$. Since $K_\alpha$ is relatively closed, $x_0\in K_\alpha$ for each $\alpha$ in $A$. Thus $x_0\in\bigcap_\alpha K_\alpha$ and $K$ must be compact. $\blacksquare$

The next result is used repeatedly in this book.

**2.7. Proposition.** *If $X$ is compact, $\{x_i\}$ is a net in $X$, and $x_0$ is the only cluster point of $\{x_i\}$, then the net $\{x_i\}$ converges to $x_0$.*

**Proof.** Let $U$ be an open neighborhood of $x_0$ and let $J=\{j\in I:x_j\notin U\}$. If $\{x_i\}$ does not converge to $x_0$, then for every $i$ in $I$ there is a $j$ in $J$ such that $j\geq i$. In particular, $J$ is also a directed set. Hence $\{x_j:j\in J\}$ is a net in the compact set $X\setminus U$. Thus it has a cluster point $y_0$. But the property of $J$ mentioned before implies that $y_0$ is also a cluster point of $\{x_i:j\in I\}$, contradicting the assumption. Thus $x_i\to x_0$. $\blacksquare$

The next result is rather easy, but it will be used so often that it should be explicitly stated and proved.

**2.8. Proposition.** *If $f:X\to Y$ is bijective and continuous and $X$ is compact, then $f$ is a homeomorphism.*

**Proof.** If $F$ is a closed subset of $X$, then $F$ is compact. Thus $f(F)$ is compact in $Y$ and hence closed. Since $f$ maps closed sets to closed sets, $f^{-1}$ is continuous. $\blacksquare$
