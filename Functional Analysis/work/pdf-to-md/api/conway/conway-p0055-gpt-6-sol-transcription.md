by $(A|_{\mathcal M})h=Ah$ whenever $h\in\mathcal M$. Note that $A|_{\mathcal M}\in\mathcal B(\mathcal M)$ and $\|A|_{\mathcal M}\|\leq\|A\|$. Also, if $\mathcal M$ is invariant for $A$ and $A$ has the representation (3.6) with $Y=0$, then $W=A|_{\mathcal M}$.

## Exercises

1. Let $\mathcal H$ be the two-dimensional real Hilbert space $\mathbb R^2$, let $\mathcal M\equiv\{(x,0)\in\mathbb R^2:x\in\mathbb R\}$ and let $\mathcal N\equiv\{(x,x\tan\theta):x\in\mathbb R\}$, where $0<\theta<\frac12\pi$. Find a formula for the idempotent $E_\theta$ with $\operatorname{ran}E_\theta=\mathcal M$ and $\ker E_\theta=\mathcal N$. Show that $\|E_\theta\|=(\sin\theta)^{-1}$.

2. Prove Proposition 3.2 (c).

3. Let $\{\mathcal M_i:i\in I\}$ be a collection of closed subspaces of $\mathcal H$ and show that $\bigcap\{\mathcal M_i^\perp:i\in I\}=[\bigvee\{\mathcal M_i:i\in I\}]^\perp$ and $[\bigcap\{\mathcal M_i:i\in I\}]^\perp=\bigvee\{\mathcal M_i^\perp:i\in I\}$.

4. Let $P$ and $Q$ be projections. Show: (a) $P+Q$ is a projection if and only if $\operatorname{ran}P\perp\operatorname{ran}Q$. If $P+Q$ is a projection, then $\operatorname{ran}(P+Q)=\operatorname{ran}P+\operatorname{ran}Q$ and $\ker(P+Q)=\ker P\cap\ker Q$. (b) $PQ$ is a projection if and only if $PQ=QP$. If $PQ$ is a projection, then $\operatorname{ran}PQ=\operatorname{ran}P\cap\operatorname{ran}Q$ and $\ker PQ=\ker P+\ker Q$.

5. Generalize Exercise 4 as follows. Suppose $\{\mathcal M_i:i\in I\}$ is a collection of subspaces of $\mathcal H$ such that $\mathcal M_i\perp\mathcal M_j$ if $i\ne j$. Let $P_i$ be the projection of $\mathcal H$ onto $\mathcal M_i$ and show that for all $h$ in $\mathcal H$, $\sum\{P_i h:i\in I\}$ converges to $Ph$, where $P$ is the projection of $\mathcal H$ onto $\bigvee\{\mathcal M_i:i\in I\}$.

6. If $P$ and $Q$ are projections, then the following statements are equivalent. (a) $P-Q$ is a projection. (b) $\operatorname{ran}Q\subseteq\operatorname{ran}P$. (c) $PQ=Q$. (d) $QP=Q$. If $P-Q$ is a projection, then $\operatorname{ran}(P-Q)=(\operatorname{ran}P)\ominus(\operatorname{ran}Q)$ and $\ker(P-Q)=\operatorname{ran}Q+\ker P$.

7. Let $P$ and $Q$ be projections. Show that $PQ=QP$ if and only if $P+Q-PQ$ is a projection. If this is the case, then $\operatorname{ran}(P+Q-PQ)=\operatorname{ran}P+\operatorname{ran}Q$ and $\ker(P+Q-PQ)=\ker P\cap\ker Q$.

8. Give an example of two noncommuting projections.

9. Let $A\in\mathcal B(\mathcal H)$ and let $\mathcal N=\operatorname{graph}A\subseteq\mathcal H\oplus\mathcal H$. That is, $\mathcal N=\{h\oplus Ah:h\in\mathcal H\}$. Because $A$ is continuous and linear, $\mathcal N\leq\mathcal H\oplus\mathcal H$. Let $\mathcal M=\mathcal H\oplus(0)\leq\mathcal H\oplus\mathcal H$. Prove the following statements. (a) $\mathcal M\cap\mathcal N=(0)$ if and only if $\ker A=(0)$. (b) $\mathcal M+\mathcal N$ is dense in $\mathcal H\oplus\mathcal H$ if and only if $\operatorname{ran}A$ is dense in $\mathcal H$. (c) $\mathcal M+\mathcal N=\mathcal H\oplus\mathcal H$ if and only if $A$ is surjective.

10. Find two closed linear subspaces $\mathcal M,\mathcal N$ of an infinite dimensional Hilbert space $\mathcal H$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N$ is dense in $\mathcal H$, but $\mathcal M+\mathcal N\ne\mathcal H$.

11. Define $A:\ell^2(\mathbb Z)\to\ell^2(\mathbb Z)$ by $A(\ldots,\alpha_{-1},\hat\alpha_0,\alpha_1,\ldots)=(\ldots,\hat\alpha_{-1},\alpha_0,\alpha_1,\ldots)$, where $\hat{\ }$ sits above the coefficient in the 0-place. Find an invariant subspace of $A$ that does not reduce $A$. This operator is called the *bilateral shift*.

12. Let $\mu=\mathrm{Area}$ measure on $\mathbb D\equiv\{z\in\mathbb C:|z|<1\}$ and define $A:L^2(\mu)\to L^2(\mu)$ by $(Af)(z)=zf(z)$ for $|z|<1$ and $f$ in $L^2(\mu)$. Find a nontrivial reducing subspace for $A$ and an invariant subspace that does not reduce $A$.
