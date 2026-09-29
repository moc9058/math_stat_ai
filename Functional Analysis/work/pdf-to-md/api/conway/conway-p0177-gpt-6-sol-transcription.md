To see that $\mathcal M_\Omega=\mathcal M_\alpha$ for some $\alpha<\Omega$, let $\{x_n^*\}$ be a countable wk* dense subset of $\operatorname{ball}\mathcal M_\Omega$. For each $n$ there is an $\alpha_n$ such that $x_n^*\in\mathcal M_{\alpha_n}$. But $\alpha=\sup_n\alpha_n$. So $\{x_n^*\}\subset\operatorname{ball}\mathcal M_\alpha$. But $\operatorname{ball}\mathcal M_\Omega$ is a compact metric space in the weak-star topology, so $\{x_n^*\}$ is wk* sequentially dense in $\operatorname{ball}\mathcal M_\Omega$. Therefore $\operatorname{ball}\mathcal M_\Omega\subseteq\operatorname{ball}\mathcal M_{\alpha+1}$ and $\mathcal M_\Omega=\mathcal M_{\alpha+1}$. ■

When is $\mathcal M$ weak-star sequentially dense in $\mathcal X^*$? The following result of Banach answers this question.

**12.11. Theorem.** *If $\mathcal X$ is a separable Banach space and $\mathcal M$ is a linear manifold in $\mathcal X^*$, then the following statements are equivalent.*

(a) $\mathcal M$ is weak-star sequentially dense in $\mathcal X^*$.

(b) There is a positive constant $c$ such that for every $x$ in $\mathcal X$,

$$
\|x\|\leqslant\sup\{|\langle x,x^*\rangle|:x^*\in\mathcal M,\ \|x^*\|\leqslant c\}.
$$

(c) There is a positive constant $c$ such that if $x^*\in\operatorname{ball}\mathcal X^*$, there is a sequence $\{x_k^*\}$ in $\mathcal M$, $\|x_k^*\|\leqslant c$, such that $x_k^*\to x^*$ (wk*).

**Proof.** It is clear that (c) implies (a). The proof will consist in showing that (a) implies (c) and that (b) and (c) are equivalent.

$(a)\Rightarrow(c)$: For each positive integer $n$, let $A_n=$ the wk* closure of $n(\operatorname{ball}\mathcal M)$. If $x^*\in\mathcal X^*$, let $\{x_k^*\}$ be a sequence in $\mathcal M$ such that $x_k^*\to x^*$ (wk*). By the PUB, there is an $n$ such that $\|x_k^*\|\leqslant n$ for all $k$. Hence $x^*\in A_n$. That is, $\bigcup_{n=1}^{\infty}A_n=\mathcal X^*$. Clearly each $A_n$ is norm closed, so the Baire Category Theorem implies that there is an $A_n$ that has interior in the norm topology. Thus there is an $x_0^*$ in $A_n$ and an $r>0$ such that $A_n\supseteq\{x^*\in\mathcal X^*:\|x^*-x_0^*\|\leqslant r\}$. Let $\{x_k^*\}\subseteq n(\operatorname{ball}\mathcal M)$ such that $x_k^*\to x_0^*$ (wk*). If $x^*\in\operatorname{ball}\mathcal X^*$, then $x_0^*+rx^*\in A_n$; hence there is a sequence $\{y_k^*\}$ in $n(\operatorname{ball}\mathcal M)$ such that $y_k^*\to x_0^*+rx^*$ (wk*). Thus $r^{-1}(y_k^*-x_k^*)\to x^*$ (wk*) and $r^{-1}(y_k^*-x_k^*)\in c(\operatorname{ball}\mathcal M)$, where $c=2n/r$ is independent of $x^*$.

$(c)\Rightarrow(b)$: If $x\in\mathcal X$, then Alaoglu’s Theorem implies there is an $x^*$ in $\operatorname{ball}\mathcal X^*$ such that $\langle x,x^*\rangle=\|x\|$. By (c), there is a sequence $\{x_k^*\}$ in $c(\operatorname{ball}\mathcal M)$ such that $x_k^*\to x^*$ (wk*). Thus $\langle x_k^*,x\rangle\to\|x\|$ and (b) holds.

$(b)\Rightarrow(c)$: According to (b), $\operatorname{ball}\mathcal X\supseteq{}^\circ[c(\operatorname{ball}\mathcal M)]$. Hence $\operatorname{ball}\mathcal X^*=(\operatorname{ball}\mathcal X)^\circ\subseteq{}^\circ[c(\operatorname{ball}\mathcal M)]^\circ$. By (1.8), ${}^\circ[c(\operatorname{ball}\mathcal M)]^\circ=$ the weak-star closure of $c(\operatorname{ball}\mathcal M)$. But bounded subsets of $\mathcal X^*$ are weak-star metrizable (5.1) and hence (c) follows. ■

## Exercises

1. Suppose $\mathcal X$ is a normed space and that the only hyperplanes $\mathcal M$ in $\mathcal X^*$ such that $\mathcal M\cap\operatorname{ball}\mathcal X^*$ is weak-star closed are those that are weak-star closed. Prove that $\mathcal X$ is a Banach space.

2. (von Neumann) Let $A$ be the subset of $l^2$ consisting of all vectors $\{x_{mn}:1\leqslant m<n<\infty\}$ where $x_{mn}(m)=1$, $x_{mn}(n)=m$, and $x_{mn}(k)=0$ if $k\ne m,n$. Show that $0\in\operatorname{wk\!-\!cl}A$ but no sequence in $A$ converges weakly to $0$.
