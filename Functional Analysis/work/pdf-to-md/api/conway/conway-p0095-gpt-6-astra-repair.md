80　　　　　　　　　　　　　　　　　III. Banach Spaces

that $|g(x_n+\mathcal M)|\to 1$ and $\|x_n+\mathcal M\|<1$ for all $n$. Let $y_n\in\mathcal M$ such that $\|x_n+y_n\|<1$. Then $|f(x_n+y_n)|=d^{-1}|g(x_n+\mathcal M)|\to d^{-1}$, so $\|f\|=d^{-1}$. ■

To prove the Hahn–Banach Theorem, we first show that we can extend the functional to a space of one dimension more.

**6.9. Lemma.** *Suppose the hypothesis of (6.2) is satisfied and, in addition, $\dim\mathcal X/\mathcal M=1$. Then the conclusion of (6.2) is valid.*

**Proof.** Fix $x_0$ in $\mathcal X\setminus\mathcal M$; so $\mathcal X=\mathcal M\vee\{x_0\}=\{tx_0+y:t\in\mathbb R,\ y\in\mathcal M\}$. For the moment assume that the extension $F:\mathcal X\to\mathbb R$ of $f$ exists with $F\leq q$. Let’s see what $F$ must look like. Put $\alpha_0=F(x_0)$. If $t>0$ and $y_1\in\mathcal M$, then $F(tx_0+y_1)=t\alpha_0+f(y_1)\leq q(tx_0+y_1)$. Hence $\alpha_0\leq-t^{-1}f(y_1)+t^{-1}q(tx_0+y_1)=-f(y_1/t)+q(x_0+y_1/t)$ for every $y_1$ in $\mathcal M$. Since $y_1/t\in\mathcal M$, this gives that.

$$
\alpha_0\leq-f(y_1)+q(x_0+y_1)
\tag*{6.10}
$$

for all $y_1$ in $\mathcal M$. Also note that if $\alpha_0$ satisfies (6.10), then by reversing the preceding argument, it follows that $t\alpha_0+f(y_1)\leq q(tx_0+y_1)$ whenever $t\geq0$.

If $t\geq0$ and $y_2\in\mathcal M$ and if $F$ exists, then $F(-tx_0+y_2)=-t\alpha_0+f(y_2)\leq q(-tx_0+y_2)$. As above, this implies that

$$
\alpha_0\geq f(y_2)-q(-x_0+y_2)
\tag*{6.11}
$$

for all $y_2$ in $\mathcal M$. Moreover, (6.11) is sufficient that $-t\alpha_0+f(y_2)\leq q(-tx_0+y_2)$ for all $t\geq0$ and $y_2$ in $\mathcal M$.

Combining (6.10) and (6.11) we see that we must show that $\alpha_0$ can be chosen satisfying (6.10) and (6.11) simultaneously. Thus we must show that

$$
f(y_2)-q(-x_0+y_2)\leq-f(y_1)+q(x_0+y_1)
\tag*{6.12}
$$

for all $y_1,y_2$ in $\mathcal M$. But this means we want to show that $f(y_1+y_2)\leq q(x_0+y_1)+q(-x_0+y_2)$. But

$$
\begin{aligned}
f(y_1+y_2)&\leq q(y_1+y_2)=q((y_1+x_0)+(-x_0+y_2))\\
&\leq q(y_1+x_0)+q(-x_0+y_2),
\end{aligned}
$$

so (6.12) is satisfied. If $\alpha_0$ is chosen with $\sup\{f(y_2)-q(-x_0+y_2):y_2\in\mathcal M\}\leq\alpha_0\leq\inf\{-f(y_1)+q(x_0+y_1):y_1\in\mathcal M\}$ and $F(tx_0+y)\equiv t\alpha_0+f(y_1)$, $F$ satisfies the conclusion of (6.2). ■

**Proof of the Hahn–Banach Theorem.** Let $\mathcal S$ be the collection of all pairs $(\mathcal M_1,f_1)$, where $\mathcal M_1$ is a linear manifold in $\mathcal X$ such that $\mathcal M_1\supseteq\mathcal M$ and $f_1:\mathcal M_1\to\mathbb R$ is a linear functional with $f_1|_{\mathcal M}=f$ and $f_1\leq q$ on $\mathcal M_1$. If $(\mathcal M_1,f_1)$ and $(\mathcal M_2,f_2)\in\mathcal S$, define $(\mathcal M_1,f_1)\lesssim(\mathcal M_2,f_2)$ to mean that $\mathcal M_1\subseteq\mathcal M_2$ and $f_2|_{\mathcal M_1}=f_1$. So $(\mathcal S,\lesssim)$ is a partially ordered set. Suppose $\mathcal C=\{(\mathcal M_i,f_i):i\in I\}$ is a chain in $\mathcal S$. If $\mathcal N\equiv\bigcup\{\mathcal M_i:i\in I\}$, then the fact that $\mathcal C$ is a chain implies that $\mathcal N$ is a linear manifold. Define $F:\mathcal N\to\mathbb R$ by setting $F(x)=f_i(x)$ if $x\in\mathcal M_i$.
