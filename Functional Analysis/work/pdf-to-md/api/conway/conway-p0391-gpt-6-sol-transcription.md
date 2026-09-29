$\int \chi_\Delta g\,d\mu$ for every $\Delta$ in $\Omega$. It follows that

$$
\tag{B.1} F(f)=\int fg\,d\mu
$$

for every simple function $f$.

**B.2. Claim.** $g\in L^q(\mu)$ and $\|g\|_q\leq\|F\|$.

Note that once this claim is proven, the proof of Case 1 is complete. Indeed, (B.2) says that $F_g\in L^p(\mu)^*$ and since $F$ and $F_g$ agree on a dense subset of $L^p(\mu)$ (B.1), $F=F_g$. Also, $\|g\|_q\leq\|F\|=\|F_g\|\leq\|g\|_q$.

To prove (B.2), let $t>0$ and put $E_t=\{x\in X:|g(x)|\leq t\}$. If $f\in L^p(\mu)$ such that $f=0$ off $E_t$, then there is a sequence $\{f_n\}$ of simple functions such that for every $n$, $f_n=0$ off $E_t$, $|f_n|\leq|f|$, and $f_n(x)\to f(x)$ a.e. $[\mu]$. (Why?) Thus $|(f_n-f)g|\leq 2t|f|$ and $\int|f|\,d\mu=\int|f|\cdot1\,d\mu\leq\|f\|_p\mu(X)^{1/q}<\infty$. By the Lebesgue Dominated Convergence Theorem, $F(f_n)=\int f_ng\,d\mu\to\int fg\,d\mu$. Also, $|f_n-f|^p\leq 2^p|f|^p$, so $\|f_n-f\|_p\to0$; thus $F(f_n)\to F(f)$. Combining these results we get that for any $t>0$ and any $f$ in $L^p(\mu)$ that vanishes off $E_t$, (B.1) holds.

*Case 1a:* $1<p<\infty$. So $1<q<\infty$. Let $f=\chi_{E_t}|g|^q/g$, where $g(x)\ne0$, and put $f(x)=0$ when $g(x)=0$. If $A=\{x:g(x)\ne0\}$, then

$$
\int|f|^p\,d\mu
=\int_{E_t\cap A}\frac{|g|^{pq}}{|g|^p}\,d\mu
=\int_{E_t}|g|^q\,d\mu
$$

since $pq-p=q$. Therefore

$$
\int_{E_t}|g|^q\,d\mu
=\int fg\,d\mu
=F(f)
\leq\|F\|\|f\|_p
=\|F\|\left[\int_{E_t}|g|^q\,d\mu\right]^{1/p}.
$$

Thus

$$
\|F\|\geq
\left[\int_{E_t}|g|^q\,d\mu\right]^{1-1/p}
\geq
\left[\int_{E_t}|g|^q\,d\mu\right]^{1/q}.
$$

Letting $t\to\infty$ gives that $\|g\|_q\leq\|F\|$.

*Case 1b:* $p=1$. So $q=\infty$. For $\varepsilon>0$ let $A=\{x:|g(x)|>\|F\|+\varepsilon\}$. For $t>0$ let $f=\chi_{E_t\cap A}\bar g/|g|$. Then $\|f\|_1=\mu(A\cap E_t)$, and so

$$
\|F\|\mu(A\cap E_t)
\geq\int fg\,d\mu
=\int_{A\cap E_t}|g|\,d\mu
\geq(\|F\|+\varepsilon)\mu(A\cap E_t).
$$

Letting $t\to\infty$ we get that $\|F\|\mu(A)\geq(\|F\|+\varepsilon)\mu(A)$, which can only be if $\mu(A)=0$. Thus $\|g\|_\infty\leq\|F\|$.

*Case 2:* $(X,\Omega,\mu)$ is arbitrary. Let $\mathcal E=$ all of the sets $E$ in $\Omega$ such that $\mu(E)<\infty$. For $E$ in $\Omega$ let $\Omega_E=\{\Delta\in\Omega:\Delta\subseteq E\}$ and define $(\mu|E)(\Delta)=\mu(\Delta)$ for $\Delta$ in $\Omega_E$. Put $L^p(\mu|E)=L^p(E,\Omega_E,\mu|E)$ and notice that $L^p(\mu|E)$ can be identified in a natural way with the functions in $L^p(X,\Omega,\mu)$ that vanish off $E$. Make this identification and consider the restriction of $F:L^p(\mu)\to\mathbb F$ to $L^p(\mu|E)$;
