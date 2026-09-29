§11. An Application: Haar Measure on a Compact Group  157

for $x,y$ in $G$. Hence

$$
\begin{aligned}
(S_0L_xR_y)(S_0L_uR_v)
&=(L_{y^{-1}}R_{x^{-1}}S_0)(S_0L_uR_v)\\
&=L_{y^{-1}}R_{x^{-1}}L_uR_v\\
&=L_{y^{-1}}L_uR_{x^{-1}}R_v\\
&=L_{uy^{-1}}R_{x^{-1}v}.
\end{aligned}
$$

Hence if $S_1=$ the identity on $M(G)$,

$$
\mathcal{S}=\{S_iL_xR_y:i=0,1;\ x,y\in G\}
$$

is a group of surjective linear isometries of $M(G)$. Let $Q=$ the probability measures on $G$; that is, $Q=\{\mu\in M(G):\mu\geqslant0\text{ and }\mu(G)=1\}$. So $Q$ is a convex subset of $M(G)$ that is $\mathrm{wk}^{*}$ compact. Furthermore, $T(Q)\subseteq Q$ for every $T$ in $\mathcal{S}$.

**11.8. Claim.** If $\mu\in M(G)$ and $\mu\neq0$, then $0\notin$ the weak* closure of $\{T(\mu):T\in\mathcal{S}\}$.

In fact, Lemma 11.6 implies that $\{T(\mu):T\in\mathcal{S}\}$ is weak* closed. Since each $T$ in $\mathcal{S}$ is an isometry, $T(\mu)\neq0$ for every $T$ in $\mathcal{S}$.

By Claim 11.8, $\mathcal{S}$ is a noncontracting family of affine maps of $Q$ into itself. Moreover, if $T=S_0L_xR_y$ and $\{\mu_i\}$ is a net in $Q$ such that $\mu_i\to\mu(\mathrm{wk}^{*})$, then for every $f$ in $C(G)$, $\langle f,T(\mu_i)\rangle=\int f(xs^{-1}y)\,d\mu_i(s)\to\int f(xs^{-1}y)\,d\mu=\langle f,T(\mu)\rangle$. So each $T$ in $\mathcal{S}$ in $\mathrm{wk}^{*}$ continuous on $Q$. By the Ryll–Nardzewski Fixed Point Theorem, there is a measure $m$ in $Q$ such that $T(m)=m$ for all $T$ in $\mathcal{S}$.

By definition, (a) holds. Also, for any $x$ in $G$ and $f$ in $C(G)$, $\int f(xs)\,dm(s)=\langle f,L_x(m)\rangle=\int f\,dm$. By similar equations, (c) holds. Now suppose $f\in C(G)$, $f\geqslant0$, and $f\neq0$. Then there is an $\varepsilon>0$ such that $U=\{x\in G:f(x)>\varepsilon\}$ is nonempty. Since $U$ is open, $G=\bigcup\{Ux:x\in G\}$, and $G$ is compact, there are $x_1,x_2,\ldots,x_n$ in $G$ such that $G\subseteq\bigcup_{k=1}^{n}Ux_k$. (Why is $Ux$ open?) Define $g_k(x)=f(xx_k^{-1})$ and put $g=\sum_{k=1}^{n}g_k$. Then $g\in C(G)$ and $\int g\,dm=\sum_{k=1}^{n}\int g_k\,dm=n\int f\,dm$ by (c). But for any $x$ in $G$ there is an $x_k$ such that $xx_k^{-1}\in U$; hence $g(x)\geqslant g_k(x)=f(xx_k^{-1})>\varepsilon$. Thus

$$
\int f\,dm=\frac{1}{n}\int g\,dm\geqslant\varepsilon/n>0.
$$

This proves (b).

To prove uniqueness, let $\mu$ be a probability measure on $G$ having properties (a), (b), (c). If $f\in C(G)$ and $x\in G$, then $\int f\,d\mu=\int {}_x f\,d\mu$. Hence

$$
\begin{aligned}
\int f\,d\mu
&=\int\left[\int f(y)\,d\mu(y)\right]dm(x)\\
&=\int\left[\int f(xy)\,d\mu(y)\right]dm(x)
\end{aligned}
$$
