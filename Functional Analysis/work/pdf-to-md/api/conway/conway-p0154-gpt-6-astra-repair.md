§6. An Application: The Stone–Čech Compactification　139

Stone–Čech compactification is the book by Gillman and Jerison [1960], though the approach to $\beta X$ is somewhat different there than here. Two recent works on the Stone–Čech compactification are Johnstone [1982] and Walker [1974].

**6.4. Corollary.** *if $X$ is completely regular and $\mu\in M(\beta X)$, define $L_\mu:C_b(X)\to\mathbb F$ by*

$$
L_\mu(f)=\int_{\beta X}f^\beta\,d\mu
$$

*for each $f$ in $C_b(X)$. Then the map $\mu\mapsto L_\mu$ is an isometric isomorphism of $M(\beta X)$ onto $C_b(X)^*$.*

**Proof.** Define $V:C_b(X)\to C(\beta X)$ by $Vf=f^\beta$. It is easy to see that $V$ is linear. Considering $X$ as a subset of $\beta X$, the fact that $\beta X=\operatorname{cl}X$ implies that $V$ is an isometry. If $g\in C(\beta X)$ and $f=g|X$, then $g=f^\beta=Vf$; hence $V$ is surjective.

If $\mu\in M(\beta X)=C(\beta X)^*$, it is easy to check that $L_\mu\in C_b(X)^*$ and $\|L_\mu\|=\|\mu\|$ since $V$ is an isometry. Conversely, if $L\in C_b(X)^*$, then $L\circ V^{-1}\in C(\beta X)^*$ and $\|L\circ V^{-1}\|=\|L\|$. Hence there is a $\mu$ in $M(\beta X)$ such that $\int g\,d\mu=L\circ V^{-1}(g)$ for every $g$ in $C(\beta X)$. Since $V^{-1}g=|X$, it follows that $L=L_\mu$. ■

The next result is from topology. It may be known to the reader, but it is presented here for the convenience of those to whom it is not.

**6.5. Partition of Unity.** *If $X$ is normal and $\{U_1,\ldots,U_n\}$ is an open covering of $X$, then there are continuous functions $f_1,\ldots,f_n$ from $X$ into $[0,1]$ such that*

(a) $\sum_{k=1}^{n}f_k(x)=1$ *for all $x$ in $X$;*

(b) $f_k(x)=0$ *for $x$ in $X\setminus U_k$ and $1\leq k\leq n$.*

**Proof.** First observe that it may be assumed that $\{U_1,\ldots,U_n\}$ has no proper subcover. The proof now proceeds by induction.

If $n=1$, let $f_1\equiv1$. Suppose $n=2$. Then $X\setminus U_1$ and $X\setminus U_2$ are disjoint closed subsets of $X$. By Urysohn’s Lemma there is a continuous function $f_1:X\to[0,1]$ such that $f_1(x)=0$ for $x$ in $X\setminus U_1$ and $f_1(x)=1$ for $x$ in $X\setminus U_2$. Let $f_2=1-f_1$ and the proof of this case is complete.

Now suppose the theorem has been proved for some $n\geq2$ and $\{U_1,\ldots,U_{n+1}\}$ is an open cover of $X$ that is minimal. Let $F=X\setminus U_{n+1}$; then $F$ is closed, nonempty, and $F\subseteq\bigcup_{k=1}^{n}U_k$. Let $V$ be an open subset of $X$ such that $F\subseteq V\subseteq\operatorname{cl}V\subseteq\bigcup_{k=1}^{n}U_k$. Since $\operatorname{cl}V$ is normal and $\{U_1\cap\operatorname{cl}V,\ldots,U_n\cap\operatorname{cl}V\}$ is an open cover of $\operatorname{cl}V$, the induction hypothesis implies that there are continuous functions $g_1,\ldots,g_n$ on $\operatorname{cl}V$ such that $\sum_{k=1}^{n}g_k=1$ and for $1\leq k\leq n$, $0\leq g_k\leq1$, and $g_k(\operatorname{cl}V\setminus U_k)=0$. By Tietze’s Extension Theorem there are continuous functions $\tilde g_1,\ldots,\tilde g_n$ on $X$ such that $\tilde g_k=g_k$ on $\operatorname{cl}V$ and $0\leq\tilde g_k\leq1$ for $1\leq k\leq n$.

Also, there is a continuous function $h:X\to[0,1]$ such that $h=0$ on $X\setminus V$
