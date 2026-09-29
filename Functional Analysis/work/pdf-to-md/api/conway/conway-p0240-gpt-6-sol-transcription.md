$\|f-\phi\|_p<\varepsilon/3$. Let $K=\operatorname{spt}\phi$. Note that because Haar measure is translation invariant, for any $y$ in $G$, $\|f_y-\phi_y\|_p=\|f-\phi\|_p<\varepsilon/3$. Now by Proposition 9.1, there is a neighborhood $U$ of $e$ such that $|\phi(y)-\phi(w)|<\frac{1}{3}\varepsilon[2m(K)]^{-1/p}$ whenever $y^{-1}w\in U$. Put $V=Ux$. If $y\in V$, then

$$
\|\phi_y-\phi_x\|_p^p=\int|\phi(zy^{-1})-\phi(zx^{-1})|^p\,dz.
$$

But $y=ux$ for some $u$ in $U$, so $(zy^{-1})^{-1}(zx^{-1})=yx^{-1}=u\in U$. Thus

$$
\begin{aligned}
\|\phi_y-\phi_x\|_p^p
&=\int_{Ky\cup Kx}|\phi(zy^{-1})-\phi(zx^{-1})|^p\,dz\\
&\leq\left(\frac{\varepsilon}{3}\right)^p[2m(K)]^{-1}m(Ky\cup Kx)\\
&\leq\left(\frac{\varepsilon}{3}\right)^p.
\end{aligned}
$$

Therefore if $y\in V$, $\|f_x-f_y\|_p\leq\|f_x-\phi_x\|_p+\|\phi_x-\phi_y\|_p+\|\phi_y-f_y\|_p<\varepsilon$. $\blacksquare$

The aim of this section is to discuss the homomorphisms on $L^1(G)$ when $G$ is abelian and to examine the Gelfand transform. There is a bit of a difficulty here since $L^1(G)$ does not have an identity when $G$ is not discrete. If $\delta_e$ is the unit point mass at $e$, then $\delta_e$ is the identity for $M(G)$ and hence acts as an identity for $L^1(G)$. Nevertheless $\delta_e\notin L^1(G)$ if $G$ is not discrete. All is not lost as $L^1(G)$ has an approximate identity (Exercise 2.8) of a nice type.

**9.3. Proposition.** *If $f\in L^1(G)$ and $\varepsilon>0$, then there is a neighborhood $U$ of $e$ such that if $g$ is a non-negative Borel function on $G$ that vanishes off $U$ and has $\int g(x)\,dx=1$, then $\|f-f*g\|_1<\varepsilon$.*

**Proof.** By the preceding proposition, there is a neighborhood $U$ of $e$ such that $\|f-f_y\|_1<\varepsilon$ whenever $y\in U$. If $g$ satisfies the conditions, then $f(x)-f*g(x)=\int[f(x)-f(xy^{-1})]g(y)\,dy$ for all $x$. Thus,

$$
\begin{aligned}
\|f-f*g\|_1
&=\int\left|\int_U[f(x)-f(xy^{-1})]g(y)\,dy\right|dx\\
&\leq\int_U g(y)\int|f(x)-f(xy^{-1})|\,dx\,dy\\
&=\int_U g(y)\|f-f_y\|_1\,dy\\
&\leq\varepsilon.
\end{aligned}
$$

$\blacksquare$

**9.4. Corollary.** *There is a net $\{e_i\}$ of non-negative functions in $L^1(G)$ such that $\int e_i\,dm=1$ for all $i$ and $\|e_i*f-f\|_1\to0$ for all $f$ in $L^1(G)$.*
