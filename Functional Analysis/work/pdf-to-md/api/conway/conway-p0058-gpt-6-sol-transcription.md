it is the limit of a sequence of finite-rank operators. Conversely, if $A$ is compact, then Corollary 4.5 implies $\|A_n\|\to 0$; hence $\alpha_n\to 0$. $\blacksquare$

**4.7. Proposition.** *If $(X,\Omega,\mu)$ is a measure space and $k\in L^2(X\times X,\Omega\times\Omega,\mu\times\mu)$, then*

$$
(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)
$$

*is a compact operator and $\|K\|\leq\|k\|_2$.*

The following lemma is useful for proving this proposition. The proof is left to the reader.

**4.8. Lemma.** *If $\{e_i:i\in I\}$ is a basis for $L^2(X,\Omega,\mu)$ and*

$$
\phi_{ij}(x,y)=e_j(x)\overline{e_i(y)}
$$

*for $i,j$ in $I$ and $x,y$ in $X$, then $\{\phi_{ij}:i,j\in I\}$ is an orthonormal set in $L^2(X\times X,\Omega\times\Omega,\mu\times\mu)$. If $k$ and $K$ are as in the preceding proposition, then $\langle k,\phi_{ij}\rangle=\langle Ke_j,e_i\rangle$.*

**Proof of Proposition 4.7.** First we show that $K$ defines a bounded operator. In fact, if $f\in L^2(\mu)$,
$$
\begin{aligned}
\|Kf\|^2
&=\int\left|\int k(x,y)f(y)\,d\mu(y)\right|^2d\mu(x)\\
&\leq\int\left(\int|k(x,y)|^2\,d\mu(y)\right)
\left(\int|f(y)|^2\,d\mu(y)\right)d\mu(x)
=\|k\|^2\|f\|^2.
\end{aligned}
$$
Hence $K$ is bounded and $\|K\|\leq\|k\|_2$.

Now let $\{e_i\}$ be a basis for $L^2(\mu)$ and define $\phi_{ij}$ as in Lemma 4.8. Thus
$$
\|k\|^2\geq\sum_{i,j}|\langle k,\phi_{ij}\rangle|^2
=\sum_{i,j}|\langle Ke_j,e_i\rangle|^2.
$$

Since $k\in L^2(\mu\times\mu)$, there are at most a countable number of $i$ and $j$ such that $\langle k,\phi_{ij}\rangle\ne 0$; denote these by $\{\psi_{km}:1\leq k,m<\infty\}$. Note that $\langle Ke_j,e_i\rangle=0$ unless $\phi_{ij}\in\{\psi_{km}\}$. Let $\psi_{km}(x,y)=e_k(x)\overline{e_m(y)}$, let $P_n$ be the orthogonal projection onto $\bigvee\{e_k:1\leq k\leq n\}$, and put $K_n=KP_n+P_nK-P_nKP_n$; so $K_n$ is a finite rank operator. We will show that $\|K-K_n\|\to 0$ as $n\to\infty$, thus showing that $K$ is compact.

Let $f\in L^2(\mu)$ with $\|f\|^2\leq 1$; so $f=\sum_j\alpha_je_j$. Hence
$$
\begin{aligned}
\|Kf-K_nf\|^2
&=\sum_i|\langle Kf-K_nf,e_i\rangle|^2\\
&=\sum_i\left|\sum_j\alpha_j\langle(K-K_n)e_j,e_i\rangle\right|^2\\
&=\sum_k\left|\sum_m\alpha_m\langle(K-K_n)e_m,e_k\rangle\right|^2\\
&\leq\sum_k\left[\sum_m|\alpha_m|^2\right]
\left[\sum_m|\langle(K-K_n)e_m,e_k\rangle|^2\right].
\end{aligned}
$$
