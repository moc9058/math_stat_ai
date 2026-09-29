Since $\sum_k \|y_{n_k}\|<\infty$, $\sum_k y_{n_k}=y$ in $\mathcal{X}$ (here is where the completeness of $\mathcal{X}$ is used.) Now for any $k\geq 1$,

$$
\begin{aligned}
\|A_{n_{k+1}}y\|
&=\left\|\sum_{j=1}^{k}A_{n_{k+1}}y_{n_j}
+A_{n_{k+1}}y_{n_{k+1}}
+\sum_{j=k+2}^{\infty}A_{n_{k+1}}y_{n_j}\right\|\\
&=\left\|A_{n_{k+1}}y_{n_{k+1}}
-\left[-\sum_{j=1}^{k}A_{n_{k+1}}y_{n_j}
-\sum_{j=k+2}^{\infty}A_{n_{k+1}}y_{n_j}\right]\right\|\\
&\geq \|A_{n_{k+1}}y_{n_{k+1}}\|
-\left\|\sum_{j=1}^{k}A_{n_{k+1}}y_{n_j}
+\sum_{j=k+2}^{\infty}A_{n_{k+1}}y_{n_j}\right\|\\
&\geq 1+k+\sum_{j=1}^{k}M(y_{n_j})
-\left[\sum_{j=1}^{k}M(y_{n_j})
+\sum_{j=k+2}^{\infty}\|A_{n_{k+1}}\|\,\|y_{n_j}\|\right]\\
&\geq 1+k-\sum_{j=k+2}^{\infty}2^{-j}\\
&\geq k.
\end{aligned}
$$

That is, $M(y)\geq k$ for all $k$, a contradiction. $\blacksquare$

**14.3. Corollary.** *If $\mathcal{X}$ is a normed space and $A\subseteq\mathcal{X}$, then $A$ is a bounded set if and only if for every $f$ in $\mathcal{X}^{*}$, $\sup\{|f(a)|:a\in A\}<\infty$.*

**PROOF.** Consider $\mathcal{X}$ as a subset of $\mathcal{B}(\mathcal{X}^{*},\mathbb{F})$ $(=\mathcal{X}^{**})$ by letting $\hat{x}(f)=f(x)$ for every $f$ in $\mathcal{X}^{*}$. Since $\mathcal{X}^{*}$ is a Banach space and $\|x\|=\|\hat{x}\|$ for all $x$, the corollary is a special case of the PUB. $\blacksquare$

**14.4. Corollary.** *If $\mathcal{X}$ is a Banach space and $A\subseteq\mathcal{X}^{*}$, then $A$ is a bounded set if and only if for every $x$ in $\mathcal{X}$, $\sup\{|f(x)|:f\in A\}<\infty$.*

**PROOF.** Consider $\mathcal{X}^{*}$ as $\mathcal{B}(\mathcal{X},\mathbb{F})$. $\blacksquare$

Using Corollary 14.3, it is possible to prove the following improvement of (14.1).

**14.5. Corollary.** *If $\mathcal{X}$ is a Banach space and $\mathcal{Y}$ is a normed space and if $\mathcal{A}\subseteq\mathcal{B}(\mathcal{X},\mathcal{Y})$ such that for every $x$ in $\mathcal{X}$ and $g$ in $\mathcal{Y}^{*}$,*

$$
\sup\{|g(A(x))|:A\in\mathcal{A}\}<\infty,
$$

*then $\sup\{\|A\|:A\in\mathcal{A}\}<\infty$.*

**PROOF.** Fix $x$ in $\mathcal{X}$. By the hypothesis and Corollary 14.3, $\sup\{\|A(x)\|:A\in\mathcal{A}\}<\infty$. By (14.1), $\sup\{\|A\|:A\in\mathcal{A}\}<\infty$. $\blacksquare$

A special form of the PUB that is quite useful is the following.

**14.6. The Banach–Steinhaus Theorem.** *If $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces and*
