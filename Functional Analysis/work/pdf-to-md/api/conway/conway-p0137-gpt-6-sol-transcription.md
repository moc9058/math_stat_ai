hand, it is assumed that $y_i+z_i\to y+z$, then $y=P(y+z)=\lim P(y_i+z_i)=\lim y_i$ and $z_i=(y_i+z_i)-y_i\to z$. This proves (a). $\blacksquare$

**5.23. Definition.** If $\mathcal X$ is a TVS and $\mathcal Y\leq\mathcal X$, $\mathcal Y$ is *topologically complemented* in $\mathcal X$ if either (a) or (b) of (5.22) is satisfied.

**5.24. Proposition.** *If $\mathcal X$ is a LCS and $\mathcal Y\leq\mathcal X$ such that either $\dim\mathcal Y<\infty$ or $\dim\mathcal X/\mathcal Y<\infty$, then $\mathcal Y$ is topologically complemented in $\mathcal X$.*

**Proof.** The proof will only be sketched. The reader is asked to supply the details (Exercise 9).

(a) Suppose $d=\dim\mathcal Y<\infty$ and let $y_1,\ldots,y_d$ be a basis for $\mathcal Y$. By the Hahn–Banach Theorem (III.6.6), there are $f_1,\ldots,f_d$ in $\mathcal X^*$ such that $f_i(y_j)=1$ if $i=j$ and $0$ otherwise. Define $Px=\sum_{j=1}^d f_j(x)y_j$.

(b) Suppose $d=\dim\mathcal X/\mathcal Y<\infty$, $Q:\mathcal X\to\mathcal X/\mathcal Y$ is the natural map, and $z_1,\ldots,z_d\in\mathcal X$ such that $Q(z_1),\ldots,Q(z_d)$ is a basis for $\mathcal X/\mathcal Y$. Let $\mathcal Z=\vee\{z_1,\ldots,z_d\}$. $\blacksquare$

**Proof of Proposition 5.16.** Suppose $\mathcal X$ is the strict inductive limit of $\{(\mathcal X_n,\mathcal T_n)\}$ and $B$ is a bounded subset of $\mathcal X$. It must be shown that there is an $n$ such that $B\subseteq\mathcal X_n$ (the rest of the proof is easy). Suppose this is not the case. By replacing $\{\mathcal X_n\}$ by a subsequence if necessary, it follows that for each $n$ there is an $x_n$ in $(B\cap\mathcal X_{n+1})\setminus\mathcal X_n$. Let $p_1$ be a continuous seminorm on $\mathcal X_1$ such that $p_1(x_1)=1$.

**5.25. Claim.** For every $n\geq2$ there is a continuous seminorm $p_n$ on $\mathcal X_n$ such that $p_n(x_n)=n$ and $p_n|_{\mathcal X_{n-1}}=p_{n-1}$.

The proof of (5.25) is by induction. Suppose $p_n$ is given and let $\mathcal Y=\mathcal X_n\vee\{x_{n+1}\}$. By (5.24), $\mathcal X_n$ and $\vee\{x_{n+1}\}$ are topologically complementary in $\mathcal Y$. Define $q:\mathcal Y\to[0,\infty)$ by $q(x+\alpha x_{n+1})=p_n(x)+(n+1)|\alpha|$, where $x\in\mathcal X_n$ and $\alpha\in\mathbb F$. Then $q$ is a continuous seminorm on $(\mathcal Y,\mathcal T_{n+1}|_{\mathcal Y})$. (Verify!) By Proposition 5.13 there is a continuous seminorm $p_{n+1}$ on $\mathcal X_{n+1}$ such that $p_{n+1}|_{\mathcal Y}=q$. Thus $p_{n+1}|_{\mathcal X_n}=p_n$ and $p_{n+1}(x_{n+1})=n+1$. This proves the claim.

Now define $p:\mathcal X\to[0,\infty)$ by $p(x)=p_n(x)$ if $x\in\mathcal X_n$. By (5.25), $p$ is well defined. It is easy to see that $p$ is a continuous seminorm. However, $\sup\{p(x):x\in B\}=\infty$, so $B$ is not bounded (Exercise 2.4f). $\blacksquare$

## Exercises

1. Verify the statements made in Example 5.2.
2. Fill in the details of the proof of Proposition 5.3.
3. Prove Proposition 5.6.
4. Verify the statements made in Example 5.9.
5. Verify the statements made in Example 5.10.
