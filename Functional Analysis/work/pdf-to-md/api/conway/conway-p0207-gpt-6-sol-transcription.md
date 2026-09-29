fact, if $xa=1$, then $1\in\mathcal M$ since $\mathcal M$ is a left ideal. Thus for $y$ in $\mathcal A$, $y=y1\in\mathcal M$. This forms a link between ideals and invertibility.

In the case of a Banach algebra some bonuses occur due to the interplay of the norm and the algebra. The results of this section will be for Banach algebras with an identity. To discuss invertibility this is, of course, the only feasible setting. For Banach algebras without an identity some analogous results can be obtained, however, by a consideration of the algebra obtained by adjoining an identity (1.3). The concept of a modular ideal and a modular unit can also be employed (see Exercise 6).

The next proof is based on the geometric series.

**2.1. Lemma.** *If $\mathcal A$ is a Banach algebra with identity and $x\in\mathcal A$ such that $\|x-1\|<1$, then $x$ is invertible.*

**Proof.** Let $y=1-x$; so $\|y\|=r<1$. Since $\|y^n\|\leqslant\|y\|^n=r^n$ (Why?), $\sum_{n=0}^{\infty}\|y^n\|<\infty$. Hence $z=\sum_{n=0}^{\infty}y^n$ converges in $\mathcal A$. If $z_n=1+y+y^2+\cdots+y^n$,

$$
z_n(1-y)=(1+y+\cdots+y^n)-(y+y^2+\cdots+y^{n+1})=1-y^{n+1}.
$$

But $\|y^{n+1}\|\leqslant r^{n+1}$, so $y^{n+1}\to0$ as $n\to\infty$. Hence $z(1-y)=\lim z_n(1-y)=1$. Similarly, $(1-y)z=1$. So $(1-y)$ is invertible and $(1-y)^{-1}=z=\sum_0^\infty y^n$. But $1-y=1-(1-x)=x$. $\blacksquare$

Note that completeness was used to show that $\sum y^n$ converges.

**2.2. Theorem.** *If $\mathcal A$ is a Banach algebra with identity, $G_l=\{a\in\mathcal A:a\text{ is left invertible}\}$, $G_r=\{a\in\mathcal A:a\text{ is right invertible}\}$, and $G=\{a\in\mathcal A:a\text{ is invertible}\}$, then $G_l$, $G_r$, and $G$ are open subsets of $\mathcal A$. Also, the map $a\mapsto a^{-1}$ of $G\to G$ is continuous.*

**Proof.** Let $a_0\in G_l$ and let $b_0\in\mathcal A$ such that $b_0a_0=1$. If $\|a-a_0\|<\|b_0\|^{-1}$, then $\|b_0a-1\|=\|b_0(a-a_0)\|<1$. By the preceding lemma, $x=b_0a$ is invertible. If $b=x^{-1}b_0$, then $ba=1$. Hence $G_l\supseteq\{a\in\mathcal A:\|a-a_0\|<\|b_0\|^{-1}\}$ and $G_l$ must be open. Similarly, $G_r$ is open. Since $G=G_l\cap G_r$ (Why?), $G$ is open.

To prove that $a\mapsto a^{-1}$ is a continuous map of $G\to G$, first assume that $\{a_n\}$ is a sequence in $G$ such that $a_n\to1$. Let $0<\delta<1$ and suppose $\|a_n-1\|<\delta$. From the preceding lemma, $a_n^{-1}=(1-(1-a_n))^{-1}=\sum_{k=0}^{\infty}(1-a_n)^k=1+\sum_{k=1}^{\infty}(1-a_n)^k$. Hence

$$
\begin{aligned}
\|a_n^{-1}-1\|
&=\left\|\sum_{k=1}^{\infty}(1-a_n)^k\right\|\\
&\leqslant\sum_{k=1}^{\infty}\|1-a_n\|^k\\
&<\delta/(1-\delta).
\end{aligned}
$$
