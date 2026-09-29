**11.5. Theorem.** *If $G$ is a compact topological group, then there exists a unique positive linear functional $I:C(G)\to\mathbb F$ such that*

(a) $I(1)=1$;

(b) *if $f\in C(G)$, $f\geq 0$, and $f\neq 0$, then $I(f)>0$;*

(c) *if $f\in C(G)$ and $x\in G$, then $I(f)=I(f_x)=I({}_x f)=I(f^\#)$.*

Before proving Theorem 11.5, we need the following lemma. For a compact topological group $G$, if $x\in G$, define $L_x:M(G)\to M(G)$ and $R_x:M(G)\to M(G)$ by

$$
\langle f,L_x(\mu)\rangle=\int {}_x f\,d\mu,
$$

$$
\langle f,R_x(\mu)\rangle=\int f_x\,d\mu
$$

for $f$ in $C(G)$ and $\mu$ in $M(G)$. Define $S_0:M(G)\to M(G)$ by

$$
\langle f,S_0(\mu)\rangle=\int f^\#\,d\mu
$$

for $f$ in $C(G)$ and $\mu$ in $M(G)$. It is easy to check that $L_x$, $R_x$, and $S_0$ are linear isometries of $M(G)$ onto $M(G)$ (Exercise 5).

**11.6. Lemma.** *If $G$ is a compact topological group, $\mu\in M(G)$, and $\rho:G\times G\to(M(G),\mathrm{wk}^*)$ is defined by $\rho(x,y)=L_xR_y(\mu)$, then $\rho$ is continuous. Similarly, if $\rho_0:G\times G\to(M(G),\mathrm{wk}^*)$ is defined by $\rho_0(x,y)=S_0L_xR_y(\mu)$, then $\rho$ is continuous.*

**Proof.** Let $f\in C(G)$ and let $\varepsilon>0$. Then (Exercise 10) there is a neighborhood $U$ of $e$ (the identity of $G$) such that $|f(x)-f(y)|<\varepsilon$ whenever $xy^{-1}\in U$ or $x^{-1}y\in U$. Suppose $\{(x_i,y_i)\}$ is a net in $G\times G$ such that $(x_i,y_i)\to(x,y)$. Let $i_0$ be such that for $i\geq i_0$, $x_ix^{-1}\in U$ and $y_i^{-1}y\in U$. If $z\in G$, then
$$
|f(x_i z y_i)-f(xzy)|
\leq |f(x_i z y_i)-f(xzy_i)|+|f(xzy_i)-f(xzy)|.
$$
But if $i\geq i_0$ and $z\in G$, $(x_i z y_i)(xzy_i)^{-1}=x_ix^{-1}\in U$ and $(xzy_i)^{-1}(xzy)=y_i^{-1}y\in U$. Hence $|f(x_i z y_i)-f(xzy)|<2\varepsilon$ for $i\geq i_0$ and for all $z$ in $G$. Thus $\lim_i\int f(x_i z y_i)\,d\mu(z)=\int f(xzy)\,d\mu(z)$. Since $f$ was arbitrary, this implies that $\rho(x_i,y_i)\to\rho(x,y)$ $\mathrm{wk}^*$ in $M(G)$. The proof for $\rho_0$ is similar. $\blacksquare$

**Proof of Theorem 11.5.** If $e=$ the identity of $G$, then

$$
\tag{11.7}
\left\{
\begin{aligned}
L_xR_y&=R_yL_x\\
L_xL_y&=L_{yx}\\
R_xR_y&=R_{xy}\\
S_0^2&=L_e=R_e=\text{the identity on }M(G)\\
S_0L_xR_y&=L_{y^{-1}}R_{x^{-1}}S_0
\end{aligned}
\right.
$$
