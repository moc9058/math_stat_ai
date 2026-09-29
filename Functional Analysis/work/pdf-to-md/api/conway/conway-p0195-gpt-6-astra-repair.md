180  VI. Linear Operators on a Banach Space

are multiplication operators $M_\phi$ for which there is no characterization of $\operatorname{Lat} M_\phi$ as well as some $M_\phi$ for which such a characterization has been achieved. One such example follows: let $\mu=$ Lebesgue area measure on $\mathbb{D}$ and let $(Af)(z)=zf(z)$ for $f$ in $L^2(\mu)$. There is no known characterization of $\operatorname{Lat} A$.

It is necessary at this point to return to the geometry of Banach spaces to prove the following classical theorem, which appeared as Exercise V.13.2.

**4.8. Mazur’s Theorem.** *If $\mathcal{X}$ is a Banach space and $K$ is a compact subset of $\mathcal{X}$, then $\overline{\operatorname{co}}(K)$ is compact.*

**PROOF.** It suffices to show that $\overline{\operatorname{co}}(K)$ is totally bounded. Let $\varepsilon>0$ and choose $x_1,\ldots,x_n$ in $K$ such that $K\subseteq\bigcup_{j=1}^{n}B(x_j;\varepsilon/4)$. Put $C=\operatorname{co}\{x_1,\ldots,x_n\}$. It is easy to see that $C$ is compact (Exercise V.7.8). Hence there are vectors $y_1,\ldots,y_m$ in $C$ such that $C\subseteq\bigcup_{i=1}^{m}B(y_i;\varepsilon/4)$. If $w\in\overline{\operatorname{co}}(K)$, there is a $z$ in $\operatorname{co}(K)$ with $\|w-z\|<\varepsilon/4$. Thus $z=\sum_{p=1}^{l}\alpha_p k_p$, where $k_p\in K$, $\alpha_p\geq 0$, and $\sum\alpha_p=1$. Now for each $k_p$ there is an $x_{j(p)}$ with $\|k_p-x_{j(p)}\|<\varepsilon/4$. Therefore

$$
\begin{aligned}
\left\|z-\sum_{p=1}^{l}\alpha_p x_{j(p)}\right\|
&=\left\|\sum_{p=1}^{l}\alpha_p(k_p-x_{j(p)})\right\|\\
&\leq\sum_{p=1}^{l}\alpha_p\|k_p-x_{j(p)}\|\\
&<\varepsilon/4.
\end{aligned}
$$

But $\sum_p\alpha_p x_{j(p)}\in C$ so there is a $y_i$ with $\|\sum_p\alpha_p x_{j(p)}-y_i\|<\varepsilon/4$. The triangle inequality now shows that $\overline{\operatorname{co}}(K)\subseteq\bigcup_{i=1}^{m}B(y_i;\varepsilon)$ and so $\overline{\operatorname{co}}(K)$ is totally bounded. ■

The next result is from Lomonosov [1973]. When it appeared it caused great excitement, both for the strength of its conclusion and for the simplicity of its proof. The proof uses Schauder’s Fixed-Point Theorem (V.9.5).

**4.9. Lomonosov’s Lemma.** *If $\mathcal{A}$ is a subalgebra of $\mathcal{B}(\mathcal{X})$ such that $1\in\mathcal{A}$ and $\operatorname{Lat}\mathcal{A}=\{(0),\mathcal{X}\}$ and if $K$ is a nonzero compact operator on $\mathcal{X}$, then there is an $A$ in $\mathcal{A}$ such that $\ker(AK-1)\ne(0)$.*

**PROOF.** It may be assumed that $\|K\|=1$. Fix $x_0$ in $\mathcal{X}$ such that $\|Kx_0\|>1$ and put $S=\{x\in\mathcal{X}:\|x-x_0\|\leq 1\}$. It is easy to check that

$$
\tag*{4.10}
0\notin S\ \text{and}\ 0\notin\operatorname{cl}K(S).
$$

Now if $x\in\mathcal{X}$ and $x\ne 0$, $\operatorname{cl}\{Tx:T\in\mathcal{A}\}$ is an invariant subspace for $\mathcal{A}$ (because $\mathcal{A}$ is an algebra) that contains the nonzero vector $x$ (because $1\in\mathcal{A}$). By hypothesis, $\operatorname{cl}\{Tx:T\in\mathcal{A}\}=\mathcal{X}$. By (4.10) this says that for every $y$ in $\operatorname{cl}K(S)$ there is a $T$ in $\mathcal{A}$ with $\|Ty-x_0\|<1$. Equivalently,
