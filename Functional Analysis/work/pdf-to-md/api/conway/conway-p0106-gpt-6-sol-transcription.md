To prove (12.3), fix $y_1$ in $\operatorname{cl}A(B(r/2))$. By (12.2), $0\in\operatorname{int}[\operatorname{cl}A(B(2^{-2}r))]$. Hence
$[y_1-\operatorname{cl}A(B(2^{-2}r))]\cap A(B(r/2))\ne\varnothing$.
Let $x_1\in B(r/2)$ such that $A(x_1)\in[y_1-\operatorname{cl}A(B(2^{-2}r))]$; now $A(x_1)=y_1-y_2$, where $y_2\in\operatorname{cl}A(B(2^{-2}r))$. Using induction, we obtain a sequence $\{x_n\}$ in $\mathscr{X}$ and a sequence $\{y_n\}$ in $\mathscr{Y}$ such that

$$
\tag{12.4}
\left\{
\begin{array}{ll}
\text{(i)} & x_n\in B(2^{-n}r),\\
\text{(ii)} & y_n\in\operatorname{cl}A(B(2^{-n}r)),\\
\text{(iii)} & y_{n+1}=y_n-A(x_n).
\end{array}
\right.
$$

But $\|x_n\|<2^{-n}r$, so $\sum_1^\infty\|x_n\|<\infty$; hence $x=\sum_{n=1}^\infty x_n$ exists in $\mathscr{X}$ and $\|x\|<r$. Also,

$$
\sum_{k=1}^{n}A(x_k)
=\sum_{k=1}^{n}(y_k-y_{k+1})
=y_1-y_{n+1}.
$$

But (12.4ii) implies $\|y_n\|\leqslant\|A\|2^{-n}r$; hence $y_n\to0$. Therefore $y_1=\sum_{k=1}^\infty A(x_k)=A(x)\in A(B(r))$, proving (12.3) and completing the proof of the theorem. $\blacksquare$

The same method used to prove the Open Mapping Theorem can also be used to prove the Tietze Extension Theorem. See Grabiner [1986].

The Open Mapping Theorem has several applications. Here are two important ones.

**12.5. The Inverse Mapping Theorem.** *If $\mathscr{X}$ and $\mathscr{Y}$ are Banach spaces and $A:\mathscr{X}\to\mathscr{Y}$ is a bounded linear transformation that is bijective, then $A^{-1}$ is bounded.*

**Proof.** Because $A$ is continuous, bijective, and open by Theorem 12.1, $A$ is a homeomorphism. $\blacksquare$

**12.6. The Closed Graph Theorem.** *If $\mathscr{X}$ and $\mathscr{Y}$ are Banach spaces and $A:\mathscr{X}\to\mathscr{Y}$ is a linear transformation such that the graph of $A$,

$$
\operatorname{gra}A\equiv
\{x\oplus Ax\in\mathscr{X}\oplus_1\mathscr{Y}:x\in\mathscr{X}\}
$$

is closed, then $A$ is continuous.*

**Proof.** Let $\mathscr{G}=\operatorname{gra}A$. Since $\mathscr{X}\oplus_1\mathscr{Y}$ is a Banach space and $\mathscr{G}$ is closed, $\mathscr{G}$ is a Banach space. Define $P:\mathscr{G}\to\mathscr{X}$ by $P(x\oplus Ax)=x$. It is easy to check that $P$ is bounded and bijective. (Do it). By the Inverse Mapping Theorem, $P^{-1}:\mathscr{X}\to\mathscr{G}$ is continuous. Thus $A:\mathscr{X}\to\mathscr{Y}$ is the composition of the continuous map $P^{-1}:\mathscr{X}\to\mathscr{G}$ and the continuous map of $\mathscr{G}\to\mathscr{Y}$ defined by $x\oplus Ax\mapsto Ax$; $A$ is therefore continuous. $\blacksquare$

Let $\mathscr{X}=$ all functions $f:[0,1]\to\mathbb{F}$ such that the derivative $f'$ exists and is continuous on $[0,1]$. Let $\mathscr{Y}=C[0,1]$ and give both $\mathscr{X}$ and $\mathscr{Y}$ the supremum norm: $\|f\|=\sup\{|f(t)|:t\in[0,1]\}$. So $\mathscr{X}$ is not a Banach space, though $\mathscr{Y}$ is. Define $A:\mathscr{X}\to\mathscr{Y}$ by $Af=f'$. Clearly, $A$ is linear. If $\{f_n\}\subseteq\mathscr{X}$ and
