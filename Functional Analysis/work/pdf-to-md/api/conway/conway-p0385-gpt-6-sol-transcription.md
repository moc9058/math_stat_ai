Conversely, if $\mathscr{X}$ is the linear span of $E$, then for every $x$ in $\mathscr{X}\setminus E$, $E\cup\{x\}$ is not linearly independent. Thus $E$ is a basis. $\blacksquare$

**1.2. Proposition.** *If $E_0$ is a linearly independent subset of $\mathscr{X}$, then there is a basis $E$ that contains $E_0$.*

**Proof.** Use Zorn’s Lemma.

A *linear functional* on $\mathscr{X}$ is a function $f:\mathscr{X}\to\mathbb{F}$ such that $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$ for $x,y$ in $\mathscr{X}$ and $\alpha,\beta$ in $\mathbb{F}$. If $\mathscr{X}$ and $\mathscr{Y}$ are vector spaces over $\mathbb{F}$, a *linear transformation* from $\mathscr{X}$ into $\mathscr{Y}$ is a function $T:\mathscr{X}\to\mathscr{Y}$ such that $T(\alpha_1x_1+\alpha_2x_2)=\alpha_1T(x_1)+\alpha_2T(x_2)$ for $x_1,x_2$ in $\mathscr{X}$ and $\alpha_1,\alpha_2$ in $\mathbb{F}$.

If $A,B\subseteq\mathscr{X}$, then $A+B\equiv\{a+b:a\in A,\ b\in B\}$; $A-B\equiv\{a-b:a\in A,\ b\in B\}$. For $\alpha$ in $\mathbb{F}$ and $A\subseteq\mathscr{X}$, $\alpha A\equiv\{\alpha a:a\in A\}$. If $\mathcal{M}$ is a *linear manifold* in $\mathscr{X}$ (that is, $\mathcal{M}\subseteq\mathscr{X}$ and $\mathcal{M}$ is also a vector space with the same operations defined on $\mathscr{X}$), then define $\mathscr{X}/\mathcal{M}$ to be the collection of all the subsets of $\mathscr{X}$ of the form $x+\mathcal{M}$. A set of the form $x+\mathcal{M}$ is called a *coset* of $\mathcal{M}$. Note that $(x+\mathcal{M})+(y+\mathcal{M})=(x+y)+\mathcal{M}$ and $\alpha(x+\mathcal{M})=\alpha x+\mathcal{M}$ since $\mathcal{M}$ is a linear manifold. Hence $\mathscr{X}/\mathcal{M}$ becomes a vector space over $\mathbb{F}$. It is called the *quotient space* of $\mathscr{X}$ mod $\mathcal{M}$.

Define $Q:\mathscr{X}\to\mathscr{X}/\mathcal{M}$ by $Q(x)=x+\mathcal{M}$. It is easy to see that $Q$ is a linear transformation. It is called the *quotient map*.

If $T:\mathscr{X}\to\mathscr{Y}$ is a linear transformation,

$$
\begin{aligned}
\ker T&\equiv\{x\in\mathscr{X}:Tx=0\},\\
\operatorname{ran}T&\equiv\{Tx:x\in\mathscr{X}\};
\end{aligned}
$$

$\ker T$ is the *kernel* of $T$ and $\operatorname{ran}T$ is the *range* of $T$. If $\operatorname{ran}T=\mathscr{Y}$, $T$ is *surjective*; if $\ker T=(0)$, $T$ is *injective*. If $T$ is both injective and surjective, then $T$ is *bijective*. It is easy to see that the natural map $Q:\mathscr{X}\to\mathscr{X}/\mathcal{M}$ is surjective and $\ker Q=\mathcal{M}$.

Suppose now that $T:\mathscr{X}\to\mathscr{Y}$ is a linear transformation and $\mathcal{M}$ is a linear manifold in $\mathscr{X}$. We want to define a map $\hat T:\mathscr{X}/\mathcal{M}\to\mathscr{Y}$ by $\hat T(x+\mathcal{M})=Tx$. But $\hat T$ may not be well defined. To ensure that it is we must have $Tx_1=Tx_2$ if $x_1+\mathcal{M}=x_2+\mathcal{M}$. But $x_1+\mathcal{M}=x_2+\mathcal{M}$ if and only if $x_1-x_2\in\mathcal{M}$, and $Tx_1=Tx_2$ if and only if $x_1-x_2\in\ker T$. So $\hat T$ is well defined if $\mathcal{M}\subseteq\ker T$. It is easy to check that if $\hat T$ is well defined, $\hat T$ is linear.

**1.3. Proposition.** *If $T:\mathscr{X}\to\mathscr{Y}$ is a linear transformation and $\mathcal{M}$ is a linear manifold in $\mathscr{X}$ contained in $\ker T$, then there is a linear transformation $\hat T:\mathscr{X}/\mathcal{M}\to\mathscr{Y}$ such that the diagram*

[FIGURE: Commutative triangular diagram near the bottom of the page. $\mathscr{X}$ is at upper left, $\mathscr{Y}$ at upper right, and $\mathscr{X}/\mathcal{M}$ below; arrows are $\mathscr{X}\xrightarrow{T}\mathscr{Y}$, $\mathscr{X}\xrightarrow{Q}\mathscr{X}/\mathcal{M}$, and $\mathscr{X}/\mathcal{M}\xrightarrow{\hat T}\mathscr{Y}$.]

*commutes.*
