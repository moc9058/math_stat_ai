$q:\mathcal X\to\mathbb R$ such that

(a) $q(x+y)\leq q(x)+q(y)$ for all $x,y$ in $\mathcal X$;  
(b) $q(\alpha x)=\alpha q(x)$ for $x$ in $\mathcal X$ and $\alpha\geq 0$.

Note that every seminorm is a sublinear functional, but not conversely. In fact, it should be emphasized that a sublinear functional is allowed to assume negative values and that (b) in the definition only holds for $\alpha\geq 0$.

**6.2. The Hahn–Banach Theorem.** *Let $\mathcal X$ be a vector space over $\mathbb R$ and let $q$ be a sublinear functional on $\mathcal X$. If $\mathcal M$ is a linear manifold in $\mathcal X$ and $f:\mathcal M\to\mathbb R$ is a linear functional such that $f(x)\leq q(x)$ for all $x$ in $\mathcal M$, then there is a linear functional $F:\mathcal X\to\mathbb R$ such that $F|_{\mathcal M}=f$ and $F(x)\leq q(x)$ for all $x$ in $\mathcal X$.*

Note that the substance of the theorem is not that the extension exists but that an extension can be found that remains dominated by $q$. Just to find an extension, let $\{e_i\}$ be a Hamel basis for $\mathcal M$ and let $\{y_j\}$ be vectors in $\mathcal X$ such that $\{e_i\}\cup\{y_j\}$ is a Hamel basis for $\mathcal X$. Now define $F:\mathcal X\to\mathbb R$ by $F(\sum_i\alpha_i e_i+\sum_j\beta_j y_j)=\sum_i\alpha_i f(e_i)=f(\sum_i\alpha_i e_i)$. This extends $f$. If $\{\gamma_j\}$ is any collection of real numbers, then $F(\sum_i\alpha_i e_i+\sum_j\beta_j y_j)=f(\sum_i\alpha_i e_i)+\sum_j\beta_j\gamma_j$ is also an extension of $f$. Moreover, any extension of $f$ has this form. The difficulty is that we must find one of these extensions that is dominated by $q$.

Before proving the theorem, let’s see some of its immediate corollaries. The first is an extension of the theorem to complex spaces. For this a lemma is needed. Note that if $\mathcal X$ is a vector space over $\mathbb C$, it is also a vector space over $\mathbb R$. Also, if $f:\mathcal X\to\mathbb C$ is $\mathbb C$-linear, then $\operatorname{Re}f:\mathcal X\to\mathbb R$ is $\mathbb R$-linear. The following lemma is the converse of this.

**6.3. Lemma.** *Let $\mathcal X$ be a vector space over $\mathbb C$.*

(a) *If $f:\mathcal X\to\mathbb R$ is an $\mathbb R$-linear functional, then $\tilde f(x)=f(x)-if(ix)$ is a $\mathbb C$-linear functional and $f=\operatorname{Re}\tilde f$.*

(b) *If $g:\mathcal X\to\mathbb C$ is $\mathbb C$-linear, $f=\operatorname{Re}g$, and $\tilde f$ is defined as in (a), then $\tilde f=g$.*

(c) *If $p$ is a seminorm on $\mathcal X$ and $f$ and $\tilde f$ are as in (a), then $|f(x)|\leq p(x)$ for all $x$ if and only if $|\tilde f(x)|\leq p(x)$ for all $x$.*

(d) *If $\mathcal X$ is a normed space and $f$ and $\tilde f$ are as in (a), then $\|f\|=\|\tilde f\|$.*

**Proof.** The proofs of (a) and (b) are left as an exercise. To prove (c), suppose $|\tilde f(x)|\leq p(x)$. Then $f(x)=\operatorname{Re}\tilde f(x)\leq|\tilde f(x)|\leq p(x)$. Also, $-f(x)=\operatorname{Re}\tilde f(-x)\leq|\tilde f(-x)|\leq p(x)$. Hence $|f(x)|\leq p(x)$. Now assume that $|f(x)|\leq p(x)$. Choose $\theta$ such that $\tilde f(x)=e^{i\theta}|\tilde f(x)|$. Hence $|\tilde f(x)|=\tilde f(e^{-i\theta}x)=\operatorname{Re}\tilde f(e^{-i\theta}x)=f(e^{-i\theta}x)\leq p(e^{-i\theta}x)=p(x)$.

Part (d) is an easy application of (c). $\blacksquare$

**6.4. Corollary.** *Let $\mathcal X$ be a vector space, let $\mathcal M$ be a linear manifold in $\mathcal X$, and let $p:\mathcal X\to[0,\infty)$ be a seminorm. If $f:\mathcal M\to\mathbb F$ is a linear functional such that*
