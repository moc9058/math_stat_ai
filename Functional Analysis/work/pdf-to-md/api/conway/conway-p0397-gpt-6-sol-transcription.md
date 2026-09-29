Now we will show that $I(f_1+f_2)=I(f_1)+I(f_2)$ whenever $f_1,f_2\in C(X)_+$. If $\varepsilon>0$, let $g_1,g_2\in C_0(X)$ such that $|g_j|\leqslant f_j$ and $|F(g_j)|>I(f_j)-\frac12\varepsilon$ for $j=1,2$. There are complex numbers $\beta_j$, $j=1,2$, with $|\beta_j|=1$ and $F(g_j)=\beta_j|F(g_j)|$. Thus

$$
\begin{aligned}
I(f_1)+I(f_2)
&<\varepsilon+|F(g_1)|+|F(g_2)|\\
&=\varepsilon+\bar{\beta}_1F(g_1)+\bar{\beta}_2F(g_2)\\
&=\varepsilon+\left|F(\bar{\beta}_1g_1+\bar{\beta}_2g_2)\right|.
\end{aligned}
$$

But $|\bar{\beta}_1g_1+\bar{\beta}_2g_2|\leqslant|g_1|+|g_2|\leqslant f_1+f_2$. Hence $I(f_1)+I(f_2)\leqslant\varepsilon+I(f_1+f_2)$. Since $\varepsilon$ was arbitrary, we have half of the desired equality.

For the other half of the equality, let $g\in C_0(X)$ such that $|g|\leqslant f_1+f_2$ and $I(f_1+f_2)<|F(g)|+\varepsilon$. Let $h_1=\min(|g|,f_1)$ and $h_2=|g|-h_1$. Clearly $h_1,h_2\in C_0(X)_+$, $h_1\leqslant f_1$, $h_2\leqslant f_2$, and $h_1+h_2=|g|$. Define $g_j:X\to\mathbb C$ by

$$
g_j(x)=
\begin{cases}
0 & \text{if }g(x)=0,\\[4pt]
\dfrac{h_j(x)g(x)}{|g(x)|} & \text{if }g(x)\ne0.
\end{cases}
$$

It is left to the reader to verify that $g_j\in C_0(X)$ and $g_1+g_2=g$. Hence

$$
\begin{aligned}
I(f_1+f_2)
&<|F(g_1)+F(g_2)|+\varepsilon\\
&\leqslant|F(g_1)|+|F(g_2)|+\varepsilon\\
&\leqslant I(f_1)+I(f_2)+\varepsilon.
\end{aligned}
$$

Now let $\varepsilon\to0$.

If $f$ is a real-valued function in $C_0(X)$, then $f=f_1-f_2$ where $f_1,f_2\in C_0(X)_+$. If also $f=g_1-g_2$ for some $g_1,g_2$ in $C_0(X)_+$, then $g_1+f_2=f_1+g_2$. By the preceding argument $I(g_1)+I(f_2)=I(f_1)+I(g_2)$. Hence if we define $I:\operatorname{Re}C_0(X)\to\mathbb R$ by $I(f)=I(f_1)-I(f_2)$ where $f=f_1-f_2$ with $f_1,f_2$ in $C_0(X)_+$, $I$ is well defined. It is left to the reader to verify that $I$ is $\mathbb R$-linear.

If $f\in C_0(X)$, then $f=f_1+if_2$, where $f_1,f_2\in\operatorname{Re}C_0(X)$. Let $I(f)=I(f_1)+iI(f_2)$. It is left to the reader to show that $I:C_0(X)\to\mathbb C$ is a linear functional.

To prove that $\|I\|=\|F\|$, first let $f\in C_0(X)$ and put $I(f)=\alpha|I(f)|$ where $|\alpha|=1$. Hence $\bar{\alpha}f=f_1+if_2$, where $f_1,f_2\in\operatorname{Re}C_0(X)$. Thus $|I(f)|=\bar{\alpha}I(f)=I(f_1)+iI(f_2)$. Since $|I(f)|$ is a positive real number, $I(f_2)=0$ and $I(f_1)=|I(f)|$. But $f_1=\operatorname{Re}(\bar{\alpha}f)\leqslant|f|$. Hence

$$
|I(f)|\leqslant I(|f|).
$$

From here we get, as in the beginning of this proof, that $\|I\|\leqslant\|F\|$. For the other half, if $\varepsilon>0$, let $f\in C_0(X)$ such that $\|f\|\leqslant1$ and $\|F\|<|F(f)|+\varepsilon$. Thus $\|F\|<I(|f|)+\varepsilon\leqslant\|I\|+\varepsilon$. $\blacksquare$

**C.17. Theorem.** *If $I:C_0(X)\to\mathbb C$ is a bounded linear functional such that $I(f)\geqslant0$ whenever $f\in C_0(X)_+$, then there is a positive measure $\nu$ in $M(X)$ such that $I(f)=\int f\,d\nu$ for every $f$ in $C_0(X)$ and $\|I\|=\nu(X)$.*
