Now $K$ is compact and so $K-K$ is also. If $U$ is an open neighborhood of $0$ in $\mathscr{X}$, there is an integer $n\geqslant 1$ such that $n^{-1}[K-K]\subseteq U$. Therefore $T(x_0)-x_0\in U$ for every open neighborhood $U$ of $0$. This implies that $T(x_0)-x_0=0$. $\blacksquare$

If $p$ is a seminorm on $\mathscr{X}$ and $A\subseteq\mathscr{X}$, define the $p$-diameter of $A$ to be the number
$$
p\text{-}\operatorname{diam} A\equiv\sup\{p(x-y):x,y\in A\}.
$$

**10.2. Lemma.** *If $\mathscr{X}$ is a LCS, $K$ is a nonempty separable weakly compact convex subset of $\mathscr{X}$, and $p$ is a continuous seminorm on $\mathscr{X}$, then for every $\varepsilon>0$ there is a closed convex subset $C$ of $K$ such that:*

(a) $C\neq K$;

(b) $p\text{-}\operatorname{diam}(K\setminus C)\leqslant\varepsilon$.

**Proof.** Let $S=\{x\in\mathscr{X}:p(x)\leqslant\varepsilon/4\}$ and let $D=$ the weak closure of the set of extreme points of $K$. Note that $D\subseteq K$. By hypothesis there is a countable subset $A$ of $K$ such that $D\subseteq K\subseteq\bigcup\{a+S:a\in A\}$. Now each $a+S$ is weakly closed. (Why?) Since $D$ is weakly compact, there is an $a$ in $A$ such that $(a+S)\cap D$ has interior in the relative weak topology of $D$ (Exercise 2). Thus, there is a weakly open subset $W$ of $\mathscr{X}$ such that

$$
\tag{10.3}
(a+S)\cap D\supseteq W\cap D\neq\square.
$$

Let $K_1=\overline{\operatorname{co}}(D\setminus W)$ and $K_2=\overline{\operatorname{co}}(D\cap W)$. Because $K_1$ and $K_2$ are compact and convex and $K_1\cup K_2$ contains the extreme points of $K$, the Krein–Milman Theorem and Exercise 7.8 imply $K=\operatorname{co}(K_1\cup K_2)$.

**10.4. Claim.** $K_1\neq K$.

In fact, if $K_1=K$, then $K=\overline{\operatorname{co}}(D\setminus W)$ so that $\operatorname{ext}K\subseteq D\setminus W$ (Theorem 7.8). This implies that $D\subseteq D\setminus W$, or that $W\cap D=\square$, a contradiction to (10.3).

Now (10.3) implies that $K_2\subseteq a+S$; so the definition of $S$ implies that $p\text{-}\operatorname{diam}K_2\leqslant\varepsilon/2$. Let $0<r\leqslant 1$ and define $f_r:K_1\times K_2\times[r,1]\to K$ by $f_r(x_1,x_2,t)=tx_1+(1-t)x_2$. So $f_r$ is continuous and $C_r\equiv f_r(K_1\times K_2\times[r,1])$ is weakly compact and convex. (Verify!)

**10.5. Claim.** $C_r\neq K$ for $0<r\leqslant 1$.

In fact, if $C_r=K$ and $e\in\operatorname{ext}K$, then $e=tx_1+(1-t)x_2$ for some $t$, $r\leqslant t\leqslant 1$, $x_j$ in $K_j$. Because $e$ is an extreme point and $t\neq 0$, $e=x_1$. Thus $\operatorname{ext}K\subseteq K_1$ and $K=K_1$, contradicting (10.4).

Let $y\in K\setminus C_r$. The definition of $C_r$ and the fact that $K=\operatorname{co}(K_1\cup K_2)$ imply $y=tx_1+(1-t)x_2$ with $x_j$ in $K_j$ and $0\leqslant t<r$. Hence $p(y-x_2)=p(t(x_1-x_2))=tp(x_1-x_2)\leqslant rd$, where $d=p\text{-}\operatorname{diam}K$. Therefore, if $y'=t'x'_1+(1-t')x'_2\in K\setminus C_r$, then $p(y-y')\leqslant p(y-x_2)+p(x_2-x'_2)+p(x'_2-y')\leqslant 2rd+p\text{-}\operatorname{diam}K_2\leqslant 2rd+\varepsilon/2$. Choosing $r=\varepsilon/4d$ and putting $C=C_r$, we have proved the lemma. $\blacksquare$
