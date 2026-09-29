# §6*. An Application: The Stone–Čech Compactification

Let $X$ be any topological space and consider the Banach space $C_b(X)$. Unless some assumption is made regarding $X$, it may be that $C_b(X)$ is “very small.” If, for example, it is assumed that $X$ is completely regular, then $C_b(X)$ has many elements. The next result says that this assumption is also necessary in order for $C_b(X)$ to be “large.” But first, here is some notation.

If $x\in X$, let $\delta_x:C_b(X)\to\mathbb F$ be defined by $\delta_x(f)=f(x)$ for every $f$ in $C_b(X)$. It is easy to see that $\delta_x\in C_b(X)^*$ and $\|\delta_x\|=1$. Let $\Delta:X\to C_b(X)^*$ be defined by $\Delta(x)=\delta_x$. If $\{x_i\}$ is a net in $X$ and $x_i\to x$, then $f(x_i)\to f(x)$ for every $f$ in $C_b(X)$. This says that $\delta_{x_i}\to\delta_x\;(\mathrm{wk}^*)$ in $C_b(X)^*$. Hence $\Delta:X\to(C_b(X)^*,\mathrm{wk}^*)$ is continuous. Is $\Delta$ a homeomorphism of $X$ onto $\Delta(X)$?

**6.1. Proposition.** *The map $\Delta:X\to(\Delta(X),\mathrm{wk}^*)$ is a homeomorphism if and only if $X$ is completely regular.*

**Proof.** Assume $X$ is completely regular. If $x_1\ne x_2$, then there is an $f$ in $C_b(X)$ such that $f(x_1)=1$ and $f(x_2)=0$; thus $\delta_{x_1}(f)\ne\delta_{x_2}(f)$. Hence $\Delta$ is injective. To show that $\Delta:X\to(\Delta(X),\mathrm{wk}^*)$ is an open map, let $U$ be an open subset of $X$ and let $x_0\in U$. Since $X$ is completely regular, there is an $f$ in $C_b(X)$ such that $f(x_0)=1$ and $f\equiv0$ on $X\setminus U$. Let $V_1=\{\mu\in C_b(X)^*:\langle f,\mu\rangle>0\}$. Then $V_1$ is $\mathrm{wk}^*$ open in $C_b(X)^*$ and $V_1\cap\Delta(X)=\{\delta_x:f(x)>0\}$. So if $V=V_1\cap\Delta(X)$, $V$ is $\mathrm{wk}^*$ open in $\Delta(X)$ and $\delta_{x_0}\in V\subseteq\Delta(U)$. Since $x_0$ was arbitrary, $\Delta(U)$ is open in $\Delta(X)$. Therefore $\Delta:X\to(\Delta(X),\mathrm{wk}^*)$ is a homeomorphism.

Now assume that $\Delta$ is a homeomorphism onto its image. Since $(\operatorname{ball}C_b(X)^*,\mathrm{wk}^*)$ is a compact space, it is completely regular. Since $\Delta(X)\subseteq\operatorname{ball}C_b(X)^*$, $\Delta(X)$ is completely regular (Exercise 2). Thus $X$ is completely regular. ■

**6.2. Stone–Čech Compactification.** *If $X$ is completely regular, then there is a compact space $\beta X$ such that:*

(a) *there is a continuous map $\Delta:X\to\beta X$ with the property that $\Delta:X\to\Delta(X)$ is a homeomorphism;*

(b) *$\Delta(X)$ is dense in $\beta X$;*

(c) *if $f\in C_b(X)$, then there is a continuous map $f^\beta:\beta X\to\mathbb F$ such that $f^\beta\circ\Delta=f$.*

*Moreover, if $\Omega$ is a compact space having these properties, then $\Omega$ is homeomorphic to $\beta X$.*

**Proof.** Let $\Delta:X\to C_b(X)^*$ be the map defined by $\Delta(x)=\delta_x$ and let $\beta X=$ the weak-star closure of $\Delta(X)$ in $C_b(X)^*$. By Alaoglu’s Theorem and the fact that $\|\delta_x\|=1$ for all $x$, $\beta X$ is compact. By the preceding proposition, (a) holds. Part (b) is true by definition. It remains to show (c).
