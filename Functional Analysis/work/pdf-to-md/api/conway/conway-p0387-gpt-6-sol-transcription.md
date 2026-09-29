a net. If $(X,\mathcal T)$ is a topological space, $x_0\in X$, and $\mathcal U=\{U\text{ in }\mathcal T:x_0\in U\}$, then let $x_U\in U$ for every $U$ in $\mathcal U$. So $\{x_U:U\in\mathcal U\}$ is a net in $X$.

**2.1. Definition.** If $\{x_i\}$ is a net in a topological space $X$, then $\{x_i\}$ *converges* to $x_0$ (in symbols, $x_i\to x_0$ or $x_0=\lim x_i$) if for every open subset $U$ of $X$ such that $x_0\in U$, there is an $i_0=i_0(U)$ such that $x_i\in U$ for $i\geqslant i_0$. The net *clusters* at $x_0$ (in symbols, $x_i\xrightarrow[\mathrm{cl}]{}x_0$) if for every $i_0$ and for every open neighborhood $U$ of $x_0$, there exists an $i\geqslant i_0$ such that $x_i\in U$.

These notions generalize the corresponding concepts for sequences. Also, if $x_i\to x_0$, then $x_i\xrightarrow[\mathrm{cl}]{}x_0$. Note that the net $\{x_U:U\in\mathcal U\}$ defined just prior to the definition converges to $x_0$. This is a very important example of a convergent net.

**2.2. Proposition.** *If $X$ is a topological space and $A\subseteq X$, then $x\in\operatorname{cl}A$ (closure of $A$) if and only if there is a net $\{a_i\}$ in $A$ such that $a_i\to x$.*

**Proof.** Let $\mathcal U=\{U:U\text{ is open and }x\in U\}$. If $x\in\operatorname{cl}A$, then for each $U$ in $\mathcal U$ there is a point $a_U$ in $A\cap U$. If $U_0\in\mathcal U$, then $a_U\in U_0$ for every $U\geqslant U_0$; therefore $x=\lim a_U$. Conversely, if $\{a_i\}$ is a net in $A$ and $a_i\to x$, then each $U$ in $\mathcal U$ contains a point $a_i$ and $a_i\in A\cap U$. Thus $x\in\operatorname{cl}A$. $\blacksquare$

**2.3. Proposition.** *If $A\subseteq X$, $\{a_i\}$ is a net in $A$, and $a_i\xrightarrow[\mathrm{cl}]{}x$, then $x\in\operatorname{cl}A$.*

**Proof.** Exercise.

There is a concept of a subnet of a net and with this concept it is possible to prove that if a net clusters at a point $x$, then there is a subnet that converges to $x$. The concept of a subnet is, however, somewhat technical and is not what you might at first think it should be. Since this concept is not used in this book, the interested reader is referred to Kelley [1955]. It might also be appropriate to mention that a topological space is Hausdorff if and only if each convergent net has a unique limit point.

**2.4. Proposition.** *If $X$ and $Y$ are topological spaces and $f:X\to Y$, then $f$ is continuous at $x_0$ if and only if $f(x_i)\to f(x_0)$ whenever $x_i\to x_0$.*

**Proof.** First assume that $f$ is continuous at $x_0$ and let $\{x_i\}$ be a net in $X$ such that $x_i\to x_0$ in $X$. If $V$ is open in $Y$ and $f(x_0)\in V$, then there is an open set $U$ in $X$ such that $x_0\in U$ and $f(U)\subseteq V$. Let $i_0$ be such that $x_i\in U$ for $i\geqslant i_0$. Hence $f(x_i)\in V$ for $i\geqslant i_0$. This says that $f(x_i)\to f(x_0)$.

Let $\mathcal U=\{U:U\text{ is open in }X\text{ and }x_0\in U\}$. Suppose $f$ is not continuous at $x_0$. Then there is an open subset $V$ of $Y$ such that $f(x_0)\in V$ and $f(U)\setminus V\neq\square$ for every $U$ in $\mathcal U$. Thus for each $U$ in $\mathcal U$ there is a point $x_U$ in $U$ with $f(x_U)\notin V$. But $\{x_U\}$ is a net in $X$ with $x_U\to x_0$ and clearly $\{f(x_U)\}$ cannot converge to $f(x_0)$. $\blacksquare$
