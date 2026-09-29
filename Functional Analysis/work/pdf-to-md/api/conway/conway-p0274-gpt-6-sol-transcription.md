**Proof.** It will only be shown that $\rho$ is multiplicative; the remainder is an exercise. Let $\phi$ and $\psi\in B(X,\Omega)$. Let $\varepsilon>0$ and choose a Borel partition $\{\Delta_1,\ldots,\Delta_n\}$ of $X$ such that $\sup\{|\omega(x)-\omega(x')|:x,x'\in\Delta_k\}<\varepsilon$ for $\omega=\phi$, $\psi$ or $\phi\psi$ and for $1\leq k\leq n$. Hence, if $x_k\in\Delta_k$ $(1\leq k\leq n)$,

$$
\left\|\int\omega\,dE-\sum_{k=1}^{n}\omega(x_k)E(\Delta_k)\right\|<\varepsilon
$$

for $\omega=\phi$, $\psi$, or $\phi\psi$. Thus, using the triangle inequality,

$$
\begin{aligned}
\left\|\int\phi\psi\,dE-\left(\int\phi\,dE\right)\left(\int\psi\,dE\right)\right\|
&\leq\varepsilon+
\left\|\sum_{k=1}^{n}\phi(x_k)\psi(x_k)E(\Delta_k)
-\left[\sum_{i=1}^{n}\phi(x_i)E(\Delta_i)\right]
\left[\sum_{j=1}^{n}\psi(x_j)E(\Delta_j)\right]\right\|\\
&\quad+
\left\|\left[\sum_{i=1}^{n}\phi(x_i)E(\Delta_i)\right]
\left[\sum_{j=1}^{n}\psi(x_j)E(\Delta_j)\right]
-\left(\int\phi\,dE\right)\left(\int\psi\,dE\right)\right\|.
\end{aligned}
$$

But $E(\Delta_i)E(\Delta_j)=E(\Delta_i\cap\Delta_j)$ and $\{\Delta_1,\ldots,\Delta_n\}$ is a partition. So the middle term in this sum is zero. Hence

$$
\begin{aligned}
\left\|\int\phi\psi\,dE-\left(\int\phi\,dE\right)\left(\int\phi\,dE\right)\right\|
&\leq\varepsilon+
\left\|\left[\sum_{i=1}^{n}\phi(x_i)E(\Delta_i)\right]
\left[\sum_{j=1}^{n}\psi(x_j)E(\Delta_j)-\int\psi\,dE\right]\right\|\\
&\quad+
\left\|\left[\sum_{i=1}^{n}\phi(x_i)E(\Delta_i)-\int\phi\,dE\right]
\left[\int\psi\,dE\right]\right\|
\leq\varepsilon[1+\|\phi\|+\|\psi\|].
\end{aligned}
$$

Since $\varepsilon$ was arbitrary, $\int\phi\psi\,dE=(\int\phi\,dE)(\int\psi\,dE)$. $\blacksquare$

**1.13. Corollary.** *If $X$ is a compact Hausdroff space and $E$ is a spectral measure defined on the Borel subsets of $X$, then $\rho:C(X)\to\mathscr{B}(\mathcal H)$ defined by $\rho(u)=\int u\,dE$ is a representation of $C(X)$.*

The next result is the main result of this section and it states that the converse to the preceding corollary holds.

**1.14. Theorem.** *If $\rho:C(X)\to\mathscr{B}(\mathcal H)$ is a representation, there is a unique spectral measure $E$ defined on the Borel subsets of $X$ such that for all $g$ and $h$ in $\mathcal H$, $E_{g,h}$ is a regular measure and*

$$
\rho(u)=\int u\,dE
$$

*for every $u$ in $C(X)$.*

**Proof.** The idea of the proof is similar to the idea of the proof of the Riesz
