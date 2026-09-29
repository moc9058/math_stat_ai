**Proof.** Let $\mathcal U$ be the collection of all neighborhoods of $e$ and order $\mathcal U$ by reverse inclusion. Let $\mathcal U=\{U_i:i\in I\}$ where $i\leq j$ if and only if $U_j\subseteq U_i$. For each $i$ in $I$ put $e_i=m(U_i)^{-1}\chi_{U_i}$, so $e_i\geq 0$ and $\int e_i\,dm=1$. If $f\in L^1(G)$ and $\varepsilon>0$, let $U_i$ be as in the preceding proposition. So if $j\geq i$, $e_j$ satisfies the conditions on $g$ in (9.3) and hence $\|f-f*e_j\|_1<\varepsilon$. $\blacksquare$

**9.5. Corollary.** If $h:L^1(G)\to\mathbb C$ is a nonzero homomorphism, then $h$ is bounded and $\|h\|=1$.

**Proof.** The fact that $h$ is bounded and $\|h\|\leq 1$ is Exercise 8.3. In light of the preceding corollary if $h(f)\neq 0$, $h(f)=\lim h(f*e_i)=h(f)\lim h(e_i)$. Hence $h(e_i)\to 1$. Since $\|e_i\|=1$ for all $i$, $\|h\|=1$. $\blacksquare$

Even though Haar measure on most of the popular examples is $\sigma$-finite, this is not true in general. For example, if $D$ is an uncountable discrete group, the Haar measure on $D$ is counting measure and, hence, not $\sigma$-finite. Similarly, Haar measure on $D\times\mathbb R$ is not $\sigma$-finite. Nevertheless, it is true that $L^1(G)^*=L^\infty(G)$ for any locally compact group because $(G,m)$ is an example of a decomposable measure space, though $L^\infty(G)$ must be redefined to be the equivalence classes of bounded Borel functions that are equal a.e. on every set of finite Haar measure. This fact will be assumed here. The interested reader can consult Hewitt and Ross [1963].

**9.6. Theorem.** If $G$ is a locally compact abelian group and $\gamma:G\to\mathbb T$ is a continuous homomorphism, define $\hat f(\gamma)$ by

$$
\hat f(\gamma)=\int f(x)\gamma(x^{-1})\,dx \tag{9.7}
$$

for every $f$ in $L^1(G)$. Then $f\mapsto\hat f(\gamma)$ is a nonzero homomorphism on $L^1(G)$. Conversely, if $h:L^1(G)\to\mathbb C$ is a nonzero homomorphism, there is a continuous homomorphism $\gamma:G\to\mathbb T$ such that $h(f)=\hat f(\gamma)$.

**Proof.** First note that if $\gamma:G\to\mathbb T$ is a homomorphism, $\gamma(xy)=\gamma(x)\gamma(y)$ and $\gamma(x^{-1})=\gamma(x)^{-1}=\overline{\gamma(x)}$, the complex conjugate of $\gamma(x)$. If $f,g\in L^1(G)$, then

$$
\begin{aligned}
\widehat{f*g}(\gamma)
&=\int(f*g)(x)\gamma(x^{-1})\,dx\\
&=\int\gamma(x^{-1})\int f(xy^{-1})g(y)\,dy\,dx\\
&=\int g(y)\gamma(y^{-1})
  \left[\int f(xy^{-1})\gamma\bigl((xy^{-1})^{-1}\bigr)\,dx\right]dy.
\end{aligned}
$$

But the invariance of the Haar integral gives that $\int f(xy^{-1})\gamma\bigl((xy^{-1})^{-1}\bigr)\,dx=\int f(x)\gamma(x^{-1})\,dx$. Hence
