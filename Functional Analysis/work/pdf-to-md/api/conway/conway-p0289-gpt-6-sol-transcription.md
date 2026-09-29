6. If $(X,\Omega,\mu)$ is a measure space, then $(X,\Omega,\mu)$ is $\sigma$-finite or $L^2(\mu)$ is finite dimensional if and only if every collection of pairwise orthogonal projections in $\{M_\phi\in L^\infty(\mu)\}$ is countable.

7. If $N=\int z\,dE(z)$ and $\varepsilon>0$, show that $\operatorname{ran}E(\{z:|z|>\varepsilon\})\subseteq\operatorname{ran}N$.

8. (Calkin [1939]) Let $\mathcal M$ be a linear manifold in $\mathcal H$ and show that $\mathcal M$ has the property that $\mathcal M$ contains no closed infinite dimensional subspaces if and only if whenever $A\in\mathcal B(\mathcal H)$ and $\operatorname{ran}A\subseteq\mathcal M$, then $A$ is compact.

9. Show that the extreme points of $\{A\in\mathcal B(\mathcal H):0\leq A\leq 1\}$ are the projections.

10. (Halmos [1972]) If $N$ is a normal operator, show that there is a hermitian operator $A$ and a continuous function $f$ such that $N=f(A)$. (Hint: Use Theorem 4.6.)

## §5. Topologies on $\mathcal B(\mathcal H)$

In this section some results on the SOT and WOT on $\mathcal B(\mathcal H)$ are presented. These results are necessary for understanding some of the results that are to follow in later sections and also for a proper comprehension of a number of other subjects in mathematics.

The first result appeared as Exercise 1.4.

**5.1. Proposition.** If $L:\mathcal B(\mathcal H)\to\mathbb C$ is a linear functional, then the following statements are equivalent.

(a) $L$ is SOT continuous.

(b) $L$ is WOT continuous.

(c) There are vectors $g_1,\ldots,g_n,h_1,\ldots,h_n$ in $\mathcal H$ such that $L(A)=\sum_{k=1}^n\langle Ag_k,h_k\rangle$ for every $A$ in $\mathcal B(\mathcal H)$.

**Proof.** Clearly (c) implies (b) and (b) implies (a). So assume (a). By (IV.3.1f) there are vectors $g_1,\ldots,g_n$ in $\mathcal H$ such that

$$
|L(A)|\leq\sum_{k=1}^n\|Ag_k\|\leq\sqrt n\left[\sum_{k=1}^n\|Ag_k\|^2\right]^{1/2}
$$

for every $A$ in $\mathcal B(\mathcal H)$. Replacing $g_k$ by $\sqrt n\,g_k$, it may be assumed that

$$
|L(A)|\leq\left[\sum_{k=1}^n\|Ag_k\|^2\right]^{1/2}\equiv p(A).
$$

Now $p$ is a seminorm and $p(A)=0$ implies $L(A)=0$. Let $\mathcal K=\operatorname{cl}\{Ag_1\oplus Ag_2\oplus\cdots\oplus Ag_n:A\in\mathcal B(\mathcal H)\}$; so $\mathcal K\subseteq\mathcal H\oplus\cdots\oplus\mathcal H$ ($n$ times). Note that if $Ag_1\oplus\cdots\oplus Ag_n=0$, $p(A)=0$, and hence, $L(A)=0$. Thus $F(Ag_1\oplus\cdots\oplus Ag_n)=L(A)$ is a well-defined linear functional on a dense manifold in $\mathcal K$. But

$$
|F(Ag_1\oplus\cdots\oplus Ag_n)|\leq p(A)=\|Ag_1\oplus\cdots\oplus Ag_n\|.
$$
