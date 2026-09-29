$$
\widehat{f*g}(\gamma)
=\int g(y)\gamma(y^{-1})
\left[\int f(x)\gamma(x^{-1})\,dx\right]dy
=\hat f(\gamma)\hat g(\gamma).
$$

So $f\mapsto\hat f(\gamma)$ is a homomorphism. Since $\gamma$ is continuous and $\gamma(G)\subseteq\mathbb T$, $\gamma\in L^\infty(G)$ and $\|\gamma\|_\infty=1$. Thus $f\mapsto\hat f(\gamma)$ is not identically zero.

Now assume that $h:L^1(G)\to\mathbb C$ is a nonzero homomorphism. Since $h$ is a bounded linear functional, there is a $\phi$ in $L^\infty(G)$ such that $h(f)=\int f(x)\phi(x)\,dx$ and $\|\phi\|_\infty=\|h\|=1$. If $f,\ g\in L^1(G)$, then $h(f*g)=\int(f*g)(x)\phi(x)\,dx=\int g(y)[\int f(xy^{-1})\phi(x)\,dx]\,dy=\int g(y)h(f_y)\,dy$. [Note that $y\mapsto h(f_y)$ is a continuous scalar-valued function by Proposition 9.2.] But $h(f*g)=h(f)h(g)=\int g(y)h(f)\phi(y)\,dy$. So

$$
0=\int g(y)[h(f_y)-h(f)\phi(y)]\,dy
$$

for every $g$ in $L^1(G)$. But $y\mapsto h(f_y)-h(f)\phi(y)$ belongs to $L^\infty(G)$, so for any $f$ in $L^1(G)$,

$$
\tag{9.8} h(f_y)=h(f)\phi(y)
$$

for locally almost all $y$ in $G$. Pick $f$ in $L^1(G)$ such that $h(f)\ne0$. By (9.8), $\phi(y)=h(f_y)/h(f)$ a.e. But the right-hand side of this equation is continuous. Hence we may assume that $\phi$ is a continuous function. Thus for every $f$ in $L^1(G)$, (9.8) holds everywhere.

In (9.8), replace $y$ by $xy$ and we obtain $h(f)\phi(xy)=h(f_{xy})=h((f_x)_y)$. Now replace $f$ in (9.8) by $f_x$ to get $h(f_x)\phi(y)=h(f_{xy})$. Thus $h(f)\phi(xy)=h(f_x)\phi(y)=[h(f)\phi(x)]\phi(y)$. If $h(f)\ne0$, this implies $\phi(xy)=\phi(x)\phi(y)$ for all $x,y$ in $G$. Thus $\phi:G\to\mathbb C$ is a homomorphism and $|\phi(x)|\leq1$ for all $x$. But $1=\phi(e)=\phi(x)\phi(x^{-1})=\phi(x)\phi(x)^{-1}$ and $|\phi(x)|,|\phi(x)^{-1}|\leq1$. Hence $|\phi(x)|=1$ for all $x$ in $G$. If $\gamma(x)=\phi(x^{-1})$, then $\gamma:G\to\mathbb T$ is a continuous homomorphism and $h(f)=\hat f(\gamma)$ for all $f$ in $L^1(G)$. $\blacksquare$

Let $\Sigma$ be the set of nonzero homomorphisms on $L^1(G)$, where $G$ is assumed to be abelian (both here and throughout the rest of the chapter). So $\Sigma\subseteq\operatorname{ball}L^1(G)^*$. If $h\in\operatorname{ball}L^1(G)^*$ and $\{h_i\}$ is a net in $\Sigma$ such that $h_i\to h$ weak$^*$, then it is easy to see that $h$ is multiplicative. Thus the weak$^*$ closure of $\Sigma\subseteq\Sigma\cup\{0\}$. Hence the relative weak$^*$ topology on $\Sigma$ makes $\Sigma$ into a locally compact Hausdorff space (see Exercise 8.4).

Let $\Gamma=$ all the continuous homomorphisms $\gamma:G\to\mathbb T$. By Theorem 9.6, $\Sigma$ and $\Gamma$ can be identified using formula (9.7). In fact, the map defined in (9.7) is the Gelfand transform when this identification is made. (Just look at the definitions.) Since $\Sigma$ and $\Gamma$ are identified and $\Sigma$ has a topology, $\Gamma$ can be given a topology. Thus $\Gamma$ becomes a locally compact space with this topology. (For another description of the topology, see Exercise 6.) The functions in $\Gamma$ are called *characters* and are sometimes denoted by $\Gamma=\hat G$ and called the *dual group*.
