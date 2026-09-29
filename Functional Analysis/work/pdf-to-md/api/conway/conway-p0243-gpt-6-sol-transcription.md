Also notice that in a natural way $\Gamma$ is a group. If $\gamma_1,\gamma_2\in\Gamma$, then $(\gamma_1\gamma_2)(x)\equiv\gamma_1(x)\gamma_2(x)$ and $\gamma_1\gamma_2\in\Gamma$.

**9.9. Proposition.** $\Gamma$ is a *locally compact abelian group*.

Clearly $\Gamma$ is an abelian group and we know that $\Gamma$ is a locally compact space. It must be shown that $\Gamma$ is a topological group. To do this we first prove a lemma.

**9.10. Lemma.**

(a) *The map $(x,\gamma)\mapsto\gamma(x)$ of $G\times\Gamma\to\mathbb T$ is continuous.*

(b) *If $\{\gamma_i\}$ is a net in $\Gamma$ and $\gamma_i\to\gamma$ in $\Gamma$, then $\gamma_i(x)\to\gamma(x)$ uniformly for $x$ belonging to any compact subset of $G$.*

**Proof.** First note that if $x\in G$ and $f\in L^1(G)$, then for every $\gamma$ in $\Gamma$,

$$
\begin{aligned}
\widehat f_x(\gamma)
&=\int f_x(y)\gamma(y^{-1})\,dy\\
&=\int f(yx^{-1})\gamma(y^{-1})\,dy\\
&=\int f(z)\gamma(z^{-1}x^{-1})\,dz\\
&=\gamma(x^{-1})\widehat f(\gamma).
\end{aligned}
$$

So if $\gamma_i\to\gamma$ in $\Gamma$ and $x_i\to x$ in $G$,

$$
\begin{aligned}
\left|\widehat f(\gamma_i)\gamma_i(x_i)-\widehat f(\gamma)\gamma(x)\right|
&=\left|\widehat f_{x_i^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma)\right|\\
&\leq\left|\widehat f_{x_i^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma_i)\right|
+\left|\widehat f_{x^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma)\right|.
\end{aligned}
$$

But $\left|\widehat f_{x_i^{-1}}(\gamma_i)-\widehat f_{x^{-1}}(\gamma_i)\right|\leq\|f_{x_i^{-1}}-f_{x^{-1}}\|_1\to0$ by (9.2). Because $f_{x^{-1}}\in L^1(G)$, $\widehat f_{x^{-1}}(\gamma_i)\to\widehat f_{x^{-1}}(\gamma)$ since $\gamma_i\to\gamma$. Thus $\widehat f(\gamma_i)\gamma_i(x_i)\to\widehat f(\gamma)\gamma(x)$. If $f$ is chosen so that $\widehat f(\gamma)\ne0$, then because $\widehat f(\gamma_i)\to\widehat f(\gamma)$, there is an $i_0$ such that $\widehat f(\gamma_i)\ne0$ for $i\geq i_0$. Therefore $\gamma_i(x_i)\to\gamma(x)$ and (a) is proven.

Now let $K$ be a compact subset of $G$ and let $\{\gamma_i\}$ be a net in $\Gamma$ such that $\gamma_i\to\gamma_0$. Suppose $\{\gamma_i(x)\}$ does not converge uniformly on $K$ to $\gamma_0(x)$. Then there is an $\varepsilon>0$ such that for every $i$, there is a $j_i\geq i$ and an $x_i$ in $K$ such that $|\gamma_{j_i}(x_i)-\gamma_0(x_i)|\geq\varepsilon$. Now $\{\gamma_{j_i}\}$ is a net and $\gamma_{j_i}\to\gamma_0$ (Exercise). Since $K$ is compact, there is an $x_0$ in $K$ such that $x_i\xrightarrow[\mathrm{cl}]{}x_0$. Now part (a) implies that the map $(x,\gamma)\mapsto(\gamma(x),\gamma_0(x))$ of $G\times\Gamma$ into $\mathbb T\times\mathbb T$ is continuous. Since $(x_i,\gamma_{j_i})\xrightarrow[\mathrm{cl}]{}(x_0,\gamma_0)$ in $G\times\Gamma$, $(\gamma_{j_i}(x_i),\gamma_0(x_i))\xrightarrow[\mathrm{cl}]{}(\gamma_0(x_0),\gamma_0(x_0))$. So for any $i_0$, there is an $i\geq i_0$ such that $|\gamma_{j_i}(x_i)-\gamma_0(x_0)|<\varepsilon/2$ and $|\gamma_0(x_i)-\gamma_0(x_0)|<\varepsilon/2$. Hence $|\gamma_{j_i}(x_i)-\gamma_0(x_i)|<\varepsilon$, a contradiction. $\blacksquare$

**Proof of Proposition 9.9.** Let $\{\gamma_i\}$, $\{\lambda_i\}$ be nets in $\Gamma$ such that $\gamma_i\to\gamma$ and $\lambda_i\to\lambda$. It must be shown that $\gamma_i\lambda_i^{-1}\to\gamma\lambda^{-1}$. Let $\phi\in C_c(G)$ and put $K=\operatorname{spt}\phi$.
