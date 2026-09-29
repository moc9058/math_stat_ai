Radon–Nikodym Theorem can be interpreted as an identification (isometrically isomorphic) of $L^1(|\mu|)$ with $\{\eta\in M(X):\eta\ll|\mu|\}$. Thus $f\mapsto\Phi(f\mu)$ is a linear functional on $L^1(|\mu|)$ and $|\Phi(f\mu)|\leq\|\Phi\|\int|f|\,d|\mu|$. Hence there is an $F(\mu)$ in $L^\infty(|\mu|)$ such that $\Phi(f\mu)=\int fF(\mu)\,d\mu$ for every $f$ in $L^1(|\mu|)$ and $\|F(\mu)\|_\infty\leq\|\Phi\|$. (We have been a little nonchalant about using $\mu$ or $|\mu|$, but what was said is perfectly correct. Fill in the details.) In particular, taking $f=1$ gives $\Phi(\mu)=\int F(\mu)\,d\mu$. It must be shown that $F\in L^\infty(M(X))$; it then follows that $\Phi=\Phi_F$ and $\|\Phi_F\|\geq\|F\|_\infty$.

To show that $F\in L^\infty(M(X))$, let $\mu$ and $\nu$ be measures such that $\nu\ll\mu$. By the Radon–Nikodym Theorem, there is an $f$ in $L^1(|\mu|)$ such that $\nu=f\mu$. Hence if $g\in L^1(|\nu|)$, then $gf\in L^1(|\mu|)$ and $\int g\,d\nu=\int gf\,d\mu$. Thus,
$$
\int gF(\nu)\,d\nu
=\Phi(g\nu)
=\Phi(gf\mu)
=\int gfF(\mu)\,d\mu
=\int gF(\mu)\,d\nu.
$$
So $F(\nu)=F(\mu)$ a.e. $[\nu]$ and $F\in L^\infty(M(X))$. ■

## Exercises

1. Complete the proof of Proposition 5.4.

2. Show that $\mathcal{X}^*$ is a normed space.

3. Give an example of a measure space $(X,\Omega,\mu)$ that is not $\sigma$-finite for which the conclusion of Theorem 5.6 is false.

4. Let $\{\mathcal{X}_i:i\in I\}$ be a collection of normed spaces. If $1\leq p<\infty$, show that the dual space of $\bigoplus_p\mathcal{X}_i$ is isometrically isomorphic to $\bigoplus_q\mathcal{X}_i^*$, where $1/p+1/q=1$.

5. If $\mathcal{X}_1,\mathcal{X}_2,\ldots$ are normed spaces, show that $(\bigoplus_0\mathcal{X}_n)^*$ is isometrically isomorphic to $\bigoplus_1\mathcal{X}_n^*$.

6. Let $n\geq1$ and let $C^{(n)}[0,1]$ be defined as in Example 1.10. Show that
   $$
   \|f\|=\sum_{k=0}^{n-1}|f^{(k)}(0)|+\sup\{|f^{(n)}(x)|:0\leq x\leq1\}
   $$
   is an equivalent norm on $C^{(n)}[0,1]$. Show that $L\in(C^{(n)}[0,1])^*$ if and only if there are scalars $\alpha_0,\alpha_1,\ldots,\alpha_{n-1}$ and a measure $\mu$ on $[0,1]$ such that
   $$
   L(f)=\sum_{k=0}^{n-1}\alpha_k f^{(k)}(0)+\int f^{(n)}\,d\mu.
   $$
   If $C^{(n)}[0,1]$ is given this new norm, find a formula for $\|L\|$ in terms of $|\alpha_0|,|\alpha_1|,\ldots,|\alpha_{n-1}|$, and $\|\mu\|$?

7. Give $\mathcal{X}=C([0,1])$ the norm $\|f\|=\int|f(t)|\,dt$ and define $L:\mathcal{X}\to F$ by $L(f)=f(\tfrac12)$. Show directly (without using Theorem 5.6) that $L$ is not bounded. Now prove this as a consequence of (5.6).

## §6. The Hahn–Banach Theorem

The Hahn–Banach Theorem is one of the most important results in mathematics. It is used so often it is rightly considered as a cornerstone of functional analysis. It is one of those theorems that when it or one of its immediate consequences is used, it is used without quotation or reference and the reader is assumed to realize that it is being invoked.

**6.1. Definition.** If $\mathcal{X}$ is a vector space, a *sublinear functional* is a function
