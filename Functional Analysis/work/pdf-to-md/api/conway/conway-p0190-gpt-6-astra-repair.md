§3. Compact Operators　　　　　　　　　　　　　　　　　175

It was shown in (II.4.4) that if $\mathcal H$ is a Hilbert space, then $\mathcal B_0(\mathcal H)$ is indeed the closure of $\mathcal B_{00}(\mathcal H)$. Note that the availability of an orthonormal basis in a Hilbert space played a significant role in the proof of this theorem. There is a concept of a basis for a Banach space called a Schauder basis. Any Banach space $\mathcal X$ with a Schauder basis has the property that $\mathcal B_{00}(\mathcal X)$ is dense in $\mathcal B_0(\mathcal X)$. Enflo [1973] gave an example of a separable reflexive Banach space $\mathcal X$ for which $\mathcal B_{00}(\mathcal X)$ is not dense in $\mathcal B_0(\mathcal X)$, and, hence, $\mathcal H$ has no Schauder basis. Davie [1973] and [1975] have simplifications of Enflo’s proof. For the classical Banach spaces, however, every compact operator is the limit of a sequence of finite-rank operators.

The remainder of this section is devoted to proving that for $X$ compact, $\mathcal B_{00}(C(X))$ is dense in $\mathcal B_0(C(X))$. This begins with material that may be familiar to many readers but will be presented for those who are unacquainted with it.

**3.7. Definition.** If $X$ is completely regular and $\mathcal F\subseteq C(X)$, then $\mathcal F$ is *equicontinuous* if for every $\varepsilon>0$ and for every $x_0$ in $X$ there is a neighborhood $U$ of $x_0$ such that $|f(x)-f(x_0)|<\varepsilon$ for all $x$ in $U$ and for all $f$ in $\mathcal F$.

Note that for a single function $f$ in $C(X)$, $\mathcal F=\{f\}$ is equicontinuous. The concept of equicontinuity states that one neighborhood works for all $f$ in $\mathcal F$.

**3.8. The Arzela–Ascoli Theorem.** *If $X$ is compact and $\mathcal F\subseteq C(X)$, then $\mathcal F$ is totally bounded if and only if $\mathcal F$ is bounded and equicontinuous.*

PROOF. Suppose $\mathcal F$ is totally bounded. It is easy to see that $\mathcal F$ is bounded. If $\varepsilon>0$, then there are $f_1,\ldots,f_n$ in $\mathcal F$ such that $\mathcal F\subseteq\bigcup_{k=1}^{n}\{f\in C(X):\|f-f_k\|<\varepsilon/3\}$. If $x_0\in X$, let $U$ be an open neighborhood of $x_0$ such that for $1\leq k\leq n$ and $x$ in $U$, $|f_k(x)-f_k(x_0)|<\varepsilon/3$. If $f\in\mathcal F$, let $f_k$ be such that $\|f-f_k\|<\varepsilon/3$. Then for $x$ in $U$,

$$
\begin{aligned}
|f(x)-f(x_0)|
&\leq |f(x)-f_k(x)|+|f_k(x)-f_k(x_0)|\\
&\qquad+|f_k(x_0)-f(x_0)|\\
&<\varepsilon.
\end{aligned}
$$

Hence $\mathcal F$ is equicontinuous.

Now assume that $\mathcal F$ is equicontinuous and $\mathcal F\subseteq\operatorname{ball}C(X)$. Let $\varepsilon>0$. For each $x$ in $X$, let $U_x$ be an open neighborhood of $x$ such that $|f(x)-f(y)|<\varepsilon/3$ for $f$ in $\mathcal F$ and $y$ in $U_x$. Now $\{U_x:x\in X\}$ is an open covering of $X$. Since $X$ is compact, there are points $x_1,\ldots,x_n$ in $X$ such that $X=\bigcup_{j=1}^{n}U_{x_j}$.

Let $\{\alpha_1,\ldots,\alpha_m\}\subseteq\mathbb D$ such that $\operatorname{cl}\mathbb D\subseteq\bigcup_{k=1}^{m}\{\alpha:|\alpha-\alpha_k|<\varepsilon/6\}$. Consider the collection $B$ of those ordered $n$-tuples $b=(\beta_1,\ldots,\beta_n)$ for which there is a function $f_b$ in $\mathcal F$ such that $|f_b(x_j)-\beta_j|<\varepsilon/6$ for $1\leq j\leq n$. Note that $B$ is
