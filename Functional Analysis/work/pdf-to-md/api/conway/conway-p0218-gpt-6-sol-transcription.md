$G$ such that $\sigma(a)\subseteq\operatorname{ins}\Gamma$. Fix $1\leq k\leq m$; then

$$
\begin{aligned}
\left\|\int_{\gamma_k}f_n(z)(z-a)^{-1}\,dz-\int_{\gamma_k}f(z)(z-a)^{-1}\,dz\right\|
&=\left\|\int_0^1[f_n(\gamma_k(t))-f(\gamma_k(t))][\gamma_k(t)-a]^{-1}\,d\gamma_k(t)\right\|\\
&\leq\int_0^1|f_n(\gamma_k(t))-f(\gamma_k(t))|
\left\|[\gamma_k(t)-a]^{-1}\right\|\,d|\gamma_k|(t).
\end{aligned}
$$

Now $t\mapsto\|[\gamma_k(t)-a]^{-1}\|$ is continuous on $[0,1]$ and hence bounded by some constant, say $M$. Thus

$$
\begin{aligned}
\left\|\int_{\gamma_k}f_n(z)(z-a)^{-1}\,dz-\int_{\gamma_k}f(z)(a-a)^{-1}\,dz\right\|\\
\leq M\|\gamma_k\|\max\{|f_n(z)-f(z)|:z\in\{\gamma_k\}\},
\end{aligned}
$$

where $\|\gamma_k\|$ is the total variation (length) of $\gamma_k$. By hypothesis it follows that $\|f_n(a)-f(a)\|\to0$ as $n\to\infty$.

(b) If $p(z)=\sum_{k=0}^{n}\alpha_kz^k$ is a polynomial, then (a), (c), and (d) combine to give that $p(a)=\sum_{k=0}^{n}\alpha_ka^k$. Now let $f(z)=\sum_{k=0}^{\infty}\alpha_kz^k$ have radius of convergence $R>r(a)$, the spectral radius of $a$. If $p_n(z)=\sum_{k=0}^{n}\alpha_kz^k$, $p_n(z)\to f(z)$ uniformly on compact subsets of $\{z:|z|<R\}$. By (e), $p_n(a)\to f(a)$. So (b) follows. $\blacksquare$

The Riesz Functional Calculus is used in the study of Banach algebras and is especially useful in the study of linear operators on a Banach space (Sections 6 and 7). Now our attention must focus on the basic properties of this functional calculus. The first such property is its uniqueness.

**4.8. Proposition.** *Let $\mathcal A$ be a Banach algebra with identity and let $a\in\mathcal A$. Let $\tau:\operatorname{Hol}(a)\to\mathcal A$ be a homomorphism such that (a) $\tau(1)=1$, (b) $\tau(z)=a$, (c) if $\{f_n\}$ is a sequence of analytic functions on an open set $G$ such that $\sigma(a)\subseteq G$ and $f_n(z)\to f(z)$ uniformly on compact subsets of $G$, then $\tau(f_n)\to\tau(f)$. Then $\tau(f)=f(a)$ for every $f$ in $\operatorname{Hol}(a)$.*

**Proof.** The proof uses Runge’s Theorem (III.8.1), but first it must be shown that $\tau(f)=f(a)$ whenever $f$ is a rational function. If $n\geq1$, $\tau(z^n)=\tau(z)^n=a^n$; hence $\tau(p)=p(a)$ for any polynomial $p$. Let $q$ be a polynomial such that $q$ never vanishes on $\sigma(a)$, so $1/q\in\operatorname{Hol}(a)$. Also, $1=\tau(1)=\tau(q\cdot q^{-1})=\tau(q)\tau(q^{-1})=q(a)\tau(q^{-1})$. Hence $q(a)$ is invertible and $q(a)^{-1}=\tau(q^{-1})$. But using the Riesz Functional Calculus, a similar argument shows that $q(a)^{-1}=(1/q)(a)$. Thus $\tau(q^{-1})=(1/q)(a)$. Therefore if $f=p/q$, where $p$ and $q$ are polynomials and $q$ never vanishes on $\sigma(a)$, $\tau(f)=\tau(p\cdot q^{-1})=\tau(p)\tau(q^{-1})=p(a)(1/q)(a)=f(a)$.

Now let $f\in\operatorname{Hol}(a)$ and suppose $f$ is analytic on an open set $G$ such that $\sigma(a)\subseteq G$. By Runge’s theorem there are rational functions $\{f_n\}$ in $\operatorname{Hol}(a)$ such
