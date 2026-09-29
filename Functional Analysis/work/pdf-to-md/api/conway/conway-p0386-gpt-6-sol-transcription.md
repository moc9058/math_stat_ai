The preceding proposition is especially useful if $\mathcal M=\ker T$. In that case $\hat T$ is injective.

The last proposition of this section will be quite helpful in the book.

**1.4. Proposition.** *Let $f,f_1,\ldots,f_n$ be linear functionals in $\mathcal X$. If $\ker f\supseteq\bigcap_{k=1}^n\ker f_k$, then there are scalars $\alpha_1,\ldots,\alpha_n$ such that $f=\sum_{k=1}^n\alpha_kf_k$ (that is, $f(x)=\sum_{k=1}^n\alpha_kf_k(x)$ for every $x$ in $\mathcal X$).*

**Proof.** It may be assumed without loss of generality that for $1\leq k\leq n$,

$$
\bigcap_{j\ne k}\ker f_j\ne\bigcap_{j=1}^n\ker f_j.
$$

(Why?) So for $1\leq k\leq n$, there is a $y_k$ in $\bigcap_{j\ne k}\ker f_j$ such that $y_k\notin\bigcap_{j=1}^n\ker f_j$. So $f_j(y_k)=0$ for $j\ne k$, but $f_k(y_k)\ne0$. Let $x_k=[f_k(y_k)]^{-1}y_k$. Hence $f_k(x_k)=1$ and $f_j(x_k)=0$ for $j\ne k$.

Now let $f$ be as in the statement of the proposition and put $\alpha_k=f(x_k)$. If $x\in\mathcal X$, let $y=x-\sum_{k=1}^n f_k(x)x_k$. Then $f_j(y)=f_j(x)-\sum_{k=1}^n f_k(x)f_j(x_k)=0$. By hypothesis, $f(y)=0$. Thus

$$
\begin{aligned}
0&=f(x)-\sum_{k=1}^n f_k(x)f(x_k)\\[6pt]
 &=f(x)-\sum_{k=1}^n\alpha_kf_k(x);
\end{aligned}
$$

equivalently, $f=\sum_{k=1}^n\alpha_kf_k$. $\blacksquare$

## §2. Topology

In this book all topological spaces are assumed to be Hausdorff.

This section will review some of the concepts and results using *nets*, as this idea is frequently used in the text.

A *directed set* is a partially ordered set $(I,\leq)$ such that if $i_1,i_2\in I$, then there is an $i_3$ in $I$ such that $i_3\geq i_1$ and $i_3\geq i_2$. A good example of a directed set is to let $(X,\mathcal S)$ be a topological space and for a fixed $x_0$ in $X$ let $\mathcal U=\{U\text{ in }\mathcal S:x_0\in U\}$. If $U,V\in\mathcal U$, define $U\geq V$ if $U\subseteq V$ (so bigger is smaller). $\mathcal U$ is said to be *ordered by reverse inclusion*. Another example is found if $S$ is any set and $\mathcal F$ is the collection of all finite subsets of $S$. Define $F_1\geq F_2$ in $\mathcal F$ if $F_1\supseteq F_2$ (bigger means bigger). Here $\mathcal F$ is said to be *ordered by inclusion*. Both of these examples are used frequently in the text.

A *net* in $X$ is a pair $((I,\leq),x)$ where $(I,\leq)$ is a directed set and $x$ is a function from $I$ into $X$. Usually we will write $x_i$ instead of $x(i)$ and will use the phrase “let $\{x_i\}$ be a net in $X$.”

Note that $\mathbf N$, the natural numbers, is a directed set, so every sequence is
