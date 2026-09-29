**10.6. Definition.** Let $\mathcal X$ be a LCS and let $Q$ be a nonempty subset of $\mathcal X$. If $\mathcal S$ is a family of maps (not necessarily linear) of $Q$ into $Q$, then $\mathcal S$ is said to be a *noncontracting family of maps* if for two distinct points $x$ and $y$ in $Q$,

$$
0\notin\operatorname{cl}\{T(x)-T(y):T\in\mathcal S\}.
$$

The next lemma has a straightforward proof whose discovery is left to the reader.

**10.7. Lemma.** *If $\mathcal X$ is a LCS, $Q\subseteq\mathcal X$, and $\mathcal S$ is a family of maps of $Q$ into $Q$, then $\mathcal S$ is a noncontracting family if and only if for every pair of distinct points $x$ and $y$ in $Q$ there is a continuous seminorm $p$ such that*

$$
\inf\{p(T(x)-T(y)):T\in\mathcal S\}>0.
$$

**10.8. The Ryll–Nardzewski Fixed Point Theorem.** *If $\mathcal X$ is a LCS, $Q$ is a weakly compact convex subset of $\mathcal X$, and $\mathcal S$ is a noncontracting semigroup of weakly continuous affine maps of $Q$ into $Q$, then there is a point $x_0$ in $Q$ such that $T(x_0)=x_0$ for every $T$ in $\mathcal S$.*

**Proof.** The proof begins by showing that every finite subset of $\mathcal S$ has a common fixed point.

**10.9. Claim.** If $\{T_1,\ldots,T_n\}\subseteq\mathcal S$, then there is an $x_0$ in $Q$ such that $T_kx_0=x_0$ for $1\leq k\leq n$.

Put $T_0=(T_1+\cdots+T_n)/n$; so $T_0:Q\to Q$ and $T_0$ is weakly continuous and affine. By (10.1), there is an $x_0$ in $Q$ such that $T_0(x_0)=x_0$. It will be shown that $T_k(x_0)=x_0$ for $1\leq k\leq n$. In fact, if $T_k(x_0)\ne x_0$ for some $k$, then by renumbering the $T_k$, it can be assumed that there is an integer $m$ such that $T_k(x_0)\ne x_0$ for $1\leq k\leq m$ and $T_k(x_0)=x_0$ for $m<k\leq n$. Let $T'_0=(T_1+\cdots+T_m)/m$. Then

$$
\begin{aligned}
x_0&=T_0(x_0)\\
&=\frac{1}{n}[T_1(x_0)+\cdots+T_m(x_0)]
+\left(\frac{n-m}{n}\right)x_0.
\end{aligned}
$$

Hence

$$
\begin{aligned}
T'_0(x_0)
&=\frac{1}{m}[T_1(x_0)+\cdots+T_m(x_0)]\\
&=\frac{n}{m}\frac{1}{n}[T_1(x_0)+\cdots+T_m(x_0)]\\
&=\frac{n}{m}\left[x_0-\left(\frac{n-m}{n}\right)x_0\right]\\
&=x_0.
\end{aligned}
$$
