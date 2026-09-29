Hyperplanes in a normed space fall into one of two categories.

**5.2. Proposition.** *If $\mathcal X$ is a normed space and $\mathcal M$ is a hyperplane in $\mathcal X$, then either $\mathcal M$ is closed or $\mathcal M$ is dense.*

**Proof.** Consider $\operatorname{cl}\mathcal M$, the closure of $\mathcal M$. By Proposition 1.3, $\operatorname{cl}\mathcal M$ is a linear manifold in $\mathcal X$. Since $\mathcal M\subseteq\operatorname{cl}\mathcal M$ and $\dim\mathcal X/\mathcal M=1$, either $\operatorname{cl}\mathcal M=\mathcal M$ or $\operatorname{cl}\mathcal M=\mathcal X$. $\blacksquare$

If $\mathcal X=c_0$ and $f:\mathcal X\to\mathbf F$ is defined by $f(\alpha_1,\alpha_2,\ldots)=\alpha_1$, then $\ker f=\{(\alpha_n)\in c_0:\alpha_1=0\}$ is closed in $c_0$. To get an example of a dense hyperplane, let $\mathcal X=c_0$ and let $e_n$ be the element of $c_0$ such that $e_n(k)=0$ if $k\ne n$ and $e_n(n)=1$. (It is best to think of $c_0$ as a collection of functions on $\mathbb N$.) Let $x_0(n)=1/n$ for all $n$; so $x_0\in c_0$ and $\{x_0,e_1,e_2,\ldots\}$ is a linearly independent set in $c_0$. Let $\mathcal B$ = a Hamel basis in $c_0$ which contains $\{x_0,e_1,e_2,\ldots\}$. Put $\mathcal B=\{x_0,e_1,e_2,\ldots\}\cup\{b_i:i\in I\}$, $b_i\ne x_0$ or $e_n$ for any $i$ or $n$. Define $f:c_0\to\mathbf F$ by $f(\alpha_0x_0+\sum_{n=1}^{\infty}\alpha_ne_n+\sum_i\beta_ib_i)=\alpha_0$. (Remember that in the preceding expression at most a finite number of the $\alpha_n$ and $\beta_i$ are not zero.) Since $e_n\in\ker f$ for all $n\geq1$, $\ker f$ is dense but clearly $\ker f\ne c_0$.

The dichotomy that exists for hyperplanes should be reflected in a dichotomy for linear functionals.

**5.3. Theorem.** *If $\mathcal X$ is a normed space and $f:\mathcal X\to\mathbf F$ is a linear functional, then $f$ is continuous if and only if $\ker f$ is closed.*

**Proof.** If $f$ is continuous, $\ker f=f^{-1}(\{0\})$ and so $\ker f$ must be closed. Assume now that $\ker f$ is closed and let $Q:\mathcal X\to\mathcal X/\ker f$ be the natural map. By (4.2), $Q$ is continuous. Let $T:\mathcal X/\ker f\to\mathbf F$ be an isomorphism; by (3.4), $T$ is continuous. Thus, if $g=T\circ Q:\mathcal X\to\mathbf F$, $g$ is continuous and $\ker f=\ker g$. Hence (5.1) $f=\alpha g$ for some $\alpha$ in $\mathbf F$ and so $f$ is continuous. $\blacksquare$

If $f:\mathcal X\to\mathbf F$ is a linear functional, then $f$ is a linear transformation and so Proposition 2.1 applies. Continuous linear functionals are also called *bounded linear functionals* and

$$
\|f\|\equiv\sup\{|f(x)|:\|x\|\leq1\}.
$$

The other formulas for $\|f\|$ given in (2.1) are also valid here. Let $\mathcal X^*\equiv$ the collection of all bounded linear functionals on $\mathcal X$. If $f,g\in\mathcal X^*$ and $\alpha\in\mathbf F$, define $(\alpha f+g)(x)=\alpha f(x)+g(x)$; $\mathcal X^*$ is called the *dual space* of $\mathcal X$. Note that $\mathcal X^*=\mathcal B(\mathcal X,\mathbf F)$.

**5.4. Proposition.** *If $\mathcal X$ is a normed space, $\mathcal X^*$ is a Banach space.*

**Proof.** It is left as an exercise for the reader to show that $\mathcal X^*$ is a normed space. To show that $\mathcal X^*$ is complete, let $B=\{x\in\mathcal X:\|x\|\leq1\}$. If $f\in\mathcal X^*$, define $\rho(f):B\to\mathbf F$ by $\rho(f)(x)=f(x)$; that is, $\rho(f)$ is the restriction of $f$ to $B$. Note that $\rho:\mathcal X^*\to C_b(B)$ is a linear isometry. Thus to show that $\mathcal X^*$ is complete,
