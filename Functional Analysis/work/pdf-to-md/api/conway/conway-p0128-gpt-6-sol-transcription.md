If $G$ is a nonempty open convex subset of $L^p(0,1)$, then

**3.20**
$$
G=L^p(0,1).
$$

To see this, first suppose $f\in L^p(0,1)$ and $((f))_p=r<R$. As a function of $t$, $\int_0^t |f(x)|^p\,dx$ is continuous, assumes the value $0$ at $t=0$, and assumes the value $r$ at $t=1$. Let $0<t<1$ such that $\int_0^t |f(x)|^p\,dx=r/2$. Define $g,h:(0,1)\to\mathbb R$ by $g(x)=f(x)$ for $x\leq t$ and $0$ otherwise; $h(x)=f(x)$ for $x\geq t$ and $0$ otherwise. Now $f=g+h=\frac12(2g+2h)$ and $((2g))_p=((2h))_p=2^p(r/2)=r/2^{1-p}$. Hence $f\in\operatorname{co}B(0;R/2^{1-p})$. This implies that $B(0;R)\subseteq\operatorname{co}B(0;R/2^{1-p})$, or, equivalently, $B(0;2^{1-p}R)\subseteq\operatorname{co}B(0;R)$. Hence $B(0;4^{1-p}R)\subseteq\operatorname{co}B(0;2^{1-p}R)\subseteq\operatorname{co}B(0;R)$. Continuing we see that for all $n$, $B(0;2^{n(1-p)}R)\subseteq\operatorname{co}B(0;R)$.

So if $G$ is a nonempty open convex subset of $L^p(0,1)$, then by translation it may be assumed that $0\in G$. Thus there is an $R>0$ with $B(0;R)\subseteq G$. By the preceding paragraph, $B(0;2^{n(1-p)}R)\subseteq\operatorname{co}B(0;R)\subseteq G$ for all $n\geq1$. Therefore $L^p(0,1)\subseteq G$.

Also note that this says that the only continuous linear functional on $L^p(0,1)$, $0<p<1$, is the identically zero functional.

## EXERCISES

1. Prove Theorem 3.1.

2. Let $p$ be a sublinear functional, $G\equiv\{x:p(x)<1\}$, and define the sublinear functional $q$ for the set $G$ as in Proposition 3.2. Show that $q(x)=\max(p(x),0)$ for all $x$ in $\mathcal X$.

3. Let $\mathcal M\subseteq\mathcal X$, a TVS, and show that the following statements are equivalent: (a) $\mathcal M$ is an affine hyperplane; (b) there exists an $x_0$ in $\mathcal M$ such that $\mathcal M-x_0$ is a hyperplane; (c) there is a non-zero linear function $f:\mathcal X\to\mathbb F$ and an $\alpha$ in $\mathbb F$ such that $\mathcal M=\{x\in\mathcal X:f(x)=\alpha\}$.

4. Let $\mathcal X$ be a real TVS. Show: (a) if $G$ is an open connected subset of $\mathcal X$, then $G$ is arcwise connected; (b) if $f:\mathcal X\to\mathbb R$ is a continuous non-zero linear functional, then $\mathcal X\setminus\ker f$ has two components, $\{x:f(x)>0\}$ and $\{x:f(x)<0\}$.

5. If $\mathcal X$ is a complex TVS and $f:\mathcal X\to\mathbb C$ is a nonzero continuous linear function, show that $\mathcal X\setminus\ker f$ is connected.

6. Prove Proposition 3.6.

7. If $f:\mathcal X\to\mathbb R$ is a continuous $\mathbb R$-linear functional and $A$ is an open convex subset of $\mathcal X$, then $f(A)$ is an open interval.

8. Prove Corollary 3.12.

9. Prove Theorem 3.13.

10. State and prove a version of Theorem 3.7 for a complex TVS.

11. State and prove a version of Corollary 3.11 for a complex LCS.

12. State and prove a version of Corollary 3.12 for a complex LCS.

13. Prove (3.18).
