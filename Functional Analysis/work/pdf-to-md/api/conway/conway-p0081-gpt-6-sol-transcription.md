**1.8. Example.** If $(X,\Omega,\mu)$ is a measure space and $1\leq p\leq\infty$, then $L^p(X,\Omega,\mu)$ is a Banach space.

The preceding example is usually proved in courses on integration and no proof is given here.

**1.9. Example.** Let $I$ be a set and $1\leq p<\infty$. Define $\ell^p(I)$ to be the set of all functions $f:I\to\mathbf F$ such that $\sum\{|f(i)|^p:i\in I\}<\infty$; and define $\|f\|_p=(\sum\{|f(i)|^p:i\in I\})^{1/p}$. Then $\ell^p(I)$ is a Banach space. If $I=\mathbf N$, then $\ell^p(\mathbf N)=\ell^p$.

If $\Omega=$ all subsets of $I$ and for each $\Delta$ in $\Omega$, $\mu(\Delta)=$ the number of points in $\Delta$ if $\Delta$ is finite and $\mu(\Delta)=\infty$ otherwise, then $\ell^p(I)=L^p(I,\Omega,\mu)$. So the statement in (1.9) is a consequence of the one in (1.8).

**1.10. Example.** Let $n\geq1$ and let $C^{(n)}[0,1]=$ the collection of functions $f:[0,1]\to\mathbf F$ such that $f$ has $n$ continuous derivatives. Define $\|f\|=\sup_{0\leq k\leq n}\{\sup\{|f^{(k)}(x)|:0\leq x\leq1\}\}$. Then $C^{(n)}[0,1]$ is a Banach space.

**1.11. Example.** Let $1\leq p<\infty$ and $n\geq1$ and let $W_p^n[0,1]=$ the functions $f:[0,1]\to\mathbf F$ such that $f$ has $n-1$ continuous derivatives, $f^{(n-1)}$ is absolutely continuous, and $f^{(n)}\in L^p[0,1]$. For $f$ in $W_p^n[0,1]$, define

$$
\|f\|=\sum_{k=0}^{n}\left[\int_0^1|f^{(k)}(x)|^p\,dx\right]^{1/p}.
$$

Then $W_p^n[0,1]$ is a Banach space.

The following is a useful fact about seminorms.

**1.12. Proposition.** If $p$ is a seminorm on $\mathcal X$, $|p(x)-p(y)|\leq p(x-y)$ for all $x,y$ in $\mathcal X$. If $\|\cdot\|$ is a norm, then $|\|x\|-\|y\||\leq\|x-y\|$ for all $x,y$ in $\mathcal X$.

**Proof.** Of course, the inequality for norms is a consequence of the one for seminorms. Note that if $x,y\in\mathcal X$, $p(x)=p(x-y+y)\leq p(x-y)+p(y)$, so $p(x)-p(y)\leq p(x-y)$. Similarly, $p(y)-p(x)\leq p(x-y)$. ■

There is the concept of “isomorphism” for the category of Banach spaces.

**1.13. Definition.** If $\mathcal X$ and $\mathcal Y$ are normed spaces, $\mathcal X$ and $\mathcal Y$ are *isometrically isomorphic* if there is a surjective linear isometry from $\mathcal X$ onto $\mathcal Y$.

The term *isomorphism* in Banach space theory is reserved for linear bijections $T:\mathcal X\to\mathcal Y$ that are homeomorphisms.

**EXERCISES**

1. Complete the proof of Proposition 1.3.
2. Complete the proof of Proposition 1.5.
