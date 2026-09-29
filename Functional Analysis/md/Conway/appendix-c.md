# Appendix C. The Dual of C0(X)

<!-- OCR draft; page images require independent visual review. -->


<a id="pdf-page-393"></a>
APPENDIX C

# The Dual of $C_0(X)$

The purpose of this section is to show that the dual of $C_0(X)$ is the space of regular Borel measures on $X$ and to put this result, and the accompanying definitions, in the context of complex-valued measures and functions.

Let $X$ be any set and let $\Omega$ be a $\sigma$-algebra of subsets of $X$; so $(X,\Omega)$ is a *measurable space*. If $\mu$ is a countably additive function defined on $\Omega$ such that $\mu(\square)=0$ and $0\leq\mu(\Delta)\leq\infty$ for all $\Delta$ in $\Omega$, call $\mu$ a *positive measure* on $(X,\Omega)$; $(X,\Omega,\mu)$ is called a *measure space*.

If $(X,\Omega)$ is a measurable space, a *signed measure* is a countably additive function $\mu$ defined on $\Omega$ such that $\mu(\square)=0$ and $\mu$ takes its values in $\mathbb{R}\cup\{\pm\infty\}$. (Note: $\mu$ can assume only one of the values $\pm\infty$.) It is assumed that the reader is familiar with the following result.

**C.1. Hahn–Jordan Decomposition.** *If $\mu$ is a signed measure on $(X,\Omega)$, then $\mu=\mu_1-\mu_2$, where $\mu_1$ and $\mu_2$ are positive measures, and $X=E_1\cup E_2$, where $E_1,E_2\in\Omega$, $E_1\cap E_2=\square$, $\mu_1(E_2)=0=\mu_2(E_1)$. The measures $\mu_1$ and $\mu_2$ are unique and the sets $E_1$ and $E_2$ are unique up to sets of $\mu_1+\mu_2$ measure zero.*

A *measure* (or *complex-valued measure*) is a complex-valued function $\mu$ defined on $\Omega$ that is countably additive and such that $\mu(\square)=0$. Note that $\mu$ does not assume any infinite values. If $\mu$ is a measure, then $(\operatorname{Re}\mu)(\Delta)\equiv\operatorname{Re}(\mu(\Delta))$ is a signed measure, as is $(\operatorname{Im}\mu)(\Delta)\equiv\operatorname{Im}(\mu(\Delta))$; hence $\mu=\operatorname{Re}\mu+i\operatorname{Im}\mu$. Applying (C.1) to $\operatorname{Re}\mu$ and $\operatorname{Im}\mu$ we get

**C.2**
$$
\mu=(\mu_1-\mu_2)+i(\mu_3-\mu_4)
$$

where $\mu_j$ $(1\leq j\leq-4)$ are positive measures, $\mu_1\perp\mu_2$ ($\mu_1$ and $\mu_2$ are *mutually singular*) and $\mu_3\perp\mu_4$. (C.2) will also be called the Hahn–Jordan decomposition of $\mu$.



<a id="pdf-page-394"></a>
**C.3. Definition.** If $\mu$ is a measure on $(X,\Omega)$ and $\Delta\in\Omega$, define the *variation* of $\mu$, $|\mu|$, by

$$
|\mu|(\Delta)=\sup\left\{\sum_{j=1}^{m}|\mu(E_j)|:\{E_j\}_{1}^{m}\text{ is a measurable partition of }\Delta\right\}.
$$

**C.4. Proposition.** *If $\mu$ is a measure on $(X,\Omega)$, then $|\mu|$ is a positive finite measure on $(X,\Omega)$. If $\mu$ is a signed measure, $|\mu|$ is a positive measure. If (C.2) is satisfied, then $|\mu|(\Delta)\leq\sum_{k=1}^{4}\mu_k(\Delta)$; if $\mu$ is a signed measure, then $|\mu|=\mu_1+\mu_2$.*

**Proof.** Clearly $|\mu|(\Delta)\geq 0$. Let $\{\Delta_n\}$ be pairwise disjoint measurable sets and let $\Delta=\bigcup_{n=1}^{\infty}\Delta_n$. If $\varepsilon>0$, then there is a measurable partition $\{E_j\}_{j=1}^{m}$ of $\Delta$ such that $|\mu|(\Delta)-\varepsilon<\sum_{j=1}^{m}|\mu(E_j)|$. Hence

$$
\begin{aligned}
|\mu|(\Delta)-\varepsilon
&\leq \sum_{j=1}^{m}\left|\sum_{n=1}^{\infty}\mu(E_j\cap\Delta_n)\right|\\
&\leq \sum_{n=1}^{\infty}\sum_{j=1}^{m}|\mu(E_j\cap\Delta_n)|.
\end{aligned}
$$

But $\{E_j\cap\Delta_n\}_{j=1}^{m}$ is a partition of $\Delta_n$, so $|\mu|(\Delta)-\varepsilon\leq\sum_{n=1}^{\infty}|\mu|(\Delta_n)$. Therefore $|\mu|(\Delta)\leq\sum_{n=1}^{\infty}|\mu|(\Delta_n)$. For the reverse inequality we may assume that $|\mu|(\Delta)<\infty$. It follows that $|\mu|(\Delta_n)<\infty$ for every $n$. (Why?) Let $\varepsilon>0$ and for each $n\geq 1$ let $\{E_1^{(n)},\ldots,E_{m_n}^{(n)}\}$ be a partition of $\Delta_n$ such that $\sum_j|\mu(E_j^{(n)})|>|\mu|(\Delta_n)-\varepsilon/2^n$. Then

$$
\begin{aligned}
\sum_{n=1}^{N}|\mu|(\Delta_n)
&<\sum_{n=1}^{N}\left[\frac{\varepsilon}{2^n}+\sum_j|\mu(E_j^{(n)})|\right]\\
&\leq\varepsilon+\sum_{n=1}^{N}\sum_j|\mu(E_j^{(n)})|\\
&\leq\varepsilon+|\mu|(\Delta).
\end{aligned}
$$

Letting $N\to\infty$ and $\varepsilon\to 0$ gives that $\sum_{1}^{\infty}|\mu|(\Delta_n)\leq|\mu|(\Delta)$.

Clearly $|\mu(\Delta)|\leq\sum_{k=1}^{4}\mu_k(\Delta)$, so $|\mu|\leq\sum_{k=1}^{4}\mu_k$. It is left to the reader to show that $|\mu|=\mu_1+\mu_2$ if $\mu$ is a signed measure. Since $\mu_1,\mu_2,\mu_3,\mu_4$ are all finite, $|\mu|$ is finite if $\mu$ is complex-valued. $\blacksquare$

**C.5. Definition.** If $\mu$ is a measure on $(X,\Omega)$ and $\nu$ is a positive measure on $(X,\Omega)$, say that $\mu$ is *absolutely continuous* with respect to $\nu$ ($\mu\ll\nu$) if $\mu(\Delta)=0$ whenever $\nu(\Delta)=0$. If $\nu$ is complex-valued, $\mu\ll\nu$ means $\mu\ll|\nu|$.

**C.6. Proposition.** *Let $\mu$ be a measure and $\nu$ a positive measure on $(X,\Omega)$. The following statements are equivalent.*

(a) $\mu\ll\nu$.

(b) $|\mu|\ll\nu$.

(c) If (C.2) holds, $\mu_k\ll\nu$ for $1\leq k\leq 4$.



<a id="pdf-page-395"></a>
**Proof.** Exercise.

The Radon–Nikodym Theorem can now be proved for complex-valued measures $\mu$ by using (C.6) and applying the usual theorem to the real and imaginary parts of $\mu$. The details are left to the reader.

**C.7. Radon–Nikodym Theorem.** *If $(X,\Omega,\nu)$ is a $\sigma$-finite measure space and $\mu$ is a complex-valued measure on $(X,\Omega)$ such that $\mu\ll\nu$, then there is a unique complex-valued function $f$ in $L^1(X,\Omega,\nu)$ such that $\mu(\Delta)=\int_\Delta f\,d\nu$ for every $\Delta$ in $\Omega$.*

The function $f$ obtained in (C.7) is called the *Radon–Nikodym derivative* of $\mu$ with respect to $\nu$ and is denoted by $f=d\mu/d\nu$.

**C.8. Theorem.** *Let $(X,\Omega,\nu)$ be a $\sigma$-finite measure space and let $\mu$ be a complex-valued measure on $(X,\Omega)$ such that $\mu\ll\nu$ and let $f=d\mu/d\nu$.*

(a) *If $g\in L(X,\Omega,|\mu|)$, then $gf\in L^1(X,\Omega,\nu)$ and $\int g\,d\mu=\int gf\,d\nu$.*

(b) *For $\Delta$ in $\Omega$, $|\mu|(\Delta)=\int_\Delta |f|\,d\nu$.*

**Proof.** Part (a) follows from the corresponding result for signed measures by using (C.2) and a similar decomposition for $f$.

To prove (b), let $\{E_j\}$ be a measurable partition of $\Delta$. Then

$$
\sum_j|\mu(E_j)|\leqslant\sum_j\int_{E_j}|f|\,d\nu
=\int_\Delta |f|\,d\nu.
$$

For the reverse inequality, let $g(x)=\overline{f(x)}/|f(x)|$ if $x\in\Delta$ and $f(x)\neq0$; let $g(x)=0$ otherwise. Let $\{g_n\}$ be a sequence of $\Omega$-measurable simple functions such that $g_n(x)=0$ off $\Delta$, $|g_n|\leqslant|g|\leqslant1$, and $g_n(x)\to g(x)$ a.e. $[\nu]$. Thus $fg_n\to|f|\chi_\Delta$ a.e. $[\nu]$. Also, $|fg_n|\leqslant|f|\chi_\Delta$ and $f\chi_\Delta\in L^1(\nu)$ [see (C.2)]. By the Lebesgue Dominated Convergence Theorem, $\int fg_n\,d\nu\to\int_\Delta|f|\,d\nu$. If $g_n=\sum_j\alpha_j\chi_{E_j}$, where $\{E_j\}$ is a partition of $\Delta$ and $|\alpha_j|\leqslant1$, then $|\int fg_n\,d\nu|=|\int g_n\,d\mu|=|\sum_j\alpha_j\mu(E_j)|\leqslant|\mu|(\Delta)$. Thus $\int_\Delta|f|\,d\nu\leqslant|\mu|(\Delta)$. ■

One way of phrasing (C.8b) is that $|d\mu/d\nu|=d|\mu|/d\nu$. The next result is left to the reader.

**C.9. Corollary.** *If $\mu$ is a complex-valued measure on $(X,\Omega)$, then there is an $\Omega$-measurable function $f$ on $X$ such that $|f|=1$ a.e. $[|\mu|]$ and $\mu(\Delta)=\int_\Delta f\,d|\mu|$ for each $\Delta$ in $\Omega$.*

**C.10. Definition.** Let $X$ be a locally compact space and let $\Omega$ be the smallest $\sigma$-algebra of subsets of $X$ that contains the open sets. Sets in $\Omega$ are called *Borel sets*. A positive measure $\mu$ on $(X,\Omega)$ is a *regular Borel measure* if (a) $\mu(K)<\infty$ for every compact subset $K$ of $X$; (b) for any $E$ in $\Omega$, $\mu(E)=\sup\{\mu(K):K\subseteq E\text{ and }K\text{ is compact}\}$; (c) for any $E$ in $\Omega$, $\mu(E)=\inf\{\mu(U):U\supseteq E\text{ and }U\text{ is open}\}$. If $\mu$ is a complex-valued measure on $(X,\Omega)$, $\mu$ is a regular Borel



<a id="pdf-page-396"></a>
measure if $|\mu|$ is. Let $M(X)=$ all of the complex-valued regular Borel measures on $X$. Note that $M(X)$ is a vector space over $\mathbb C$. For $\mu$ in $M(X)$, let

$$
\|\mu\|\equiv|\mu|(X). \tag{C.11}
$$

**C.12. Proposition.** *(C.11) defines a norm on $M(X)$.*

**Proof.** Exercise.

**C.13. Lemma.** *If $\mu\in M(X)$, define $F_\mu\colon C_0(X)\to\mathbb C$ by $F_\mu(f)=\int f\,d\mu$. Then $F_\mu\in C_0(X)^*$ and $\|F_\mu\|=\|\mu\|$.*

**Proof.** If $f\in C_0(X)$, then $|F_\mu(f)|\leq\int|f|\,d|\mu|\leq\|f\|\|\mu\|$. Hence $F_\mu\in C_0(X)^*$ and $\|F_\mu\|\leq\|\mu\|$.

To show equality, let $f_0$ be a Borel function such that $|f_0|=1$ a.e. $[|\mu|]$ and $\mu(\Delta)=\int_\Delta f_0\,d|\mu|$. By Lusin’s Theorem, if $\varepsilon>0$, there is a continuous function $\phi$ on $X$ with compact support such that $\int|\phi-\overline{f_0}|\,d|\mu|<\varepsilon$ and $\|\phi\|\leq\sup|f_0(x)|=1$. Thus

$$
\begin{aligned}
\|\mu\|
&=\int f_0\overline{f_0}\,d|\mu|
\overset{\text{(C.8a)}}{=}\int\overline{f_0}\,d\mu
=\left|\int\overline{f_0}\,d\mu\right|\\
&\leq\left|\int(\overline{f_0}-\phi)\,d\mu\right|
+\left|\int\phi\,d\mu\right|
\leq\varepsilon+|F_\mu(\phi)|
\leq\varepsilon+\|F_\mu\|.
\end{aligned}
$$

Hence $\|\mu\|\leq\|F_\mu\|$. ■

**C.14. Corollary.** *(a) If $U$ is an open subset of $X$ and $\mu\in M(X)$, then $|\mu|(U)=\sup\{|\int\phi\,d\mu|:\phi\in C_c(X),\ \operatorname{spt}\phi\subseteq U,\text{ and }\|\phi\|\leq1\}$. (b) If $\mu\geq0$, $\mu(K)=\inf\{\int\phi\,d\mu:\phi\in C_0(X)\text{ and }\phi\geq\chi_K\}$.*

**Proof.** (a) If $U$ is given the relative topology from $X$, $U$ is locally compact. Let $\nu$ be the restriction of $\mu$ to $U$. Then (a) becomes a restatement of (C.13) for the space $U$ together with the fact that $C_c(U)$ is norm dense in $C_0(U)$.

(b) If $\phi\geq\chi_K$, then because $\mu$ is positive, $\int\phi\,d\mu\geq\mu(K)$. Thus $\mu(K)\leq\alpha\equiv\inf\{\int\phi\,d\mu:\phi\in C_0(X)\text{ and }\phi\geq\chi_K\}$. Using the regularity of $\mu$, for every integer $n$ there is an open set $U_n$ such that $K\subseteq U_n$ and $\mu(U_n\setminus K)<n^{-1}$. Let $\psi_n\in C_c(X)$ such that $0\leq\psi_n\leq1$, $\psi_n=1$ on $K$, and $\psi_n=0$ off $U_n$. Thus $\psi_n\geq\chi_K$ and so $\alpha\leq\int\psi_n\,d\mu\leq\mu(U_n)<\mu(K)+n^{-1}$. ■

The next step in the process of representing bounded linear functionals on $C_0(X)$ by measures is to associate with each such functional a positive functional. If $\mu\in M(X)$, then the next lemma would associate with the functional $F_\mu$ the positive functional $I=F_{|\mu|}$.

**C.15. Lemma.** *If $F\colon C_0(X)\to\mathbb C$ is a bounded linear functional, then there is a unique linear functional $I\colon C_0(X)\to\mathbb C$ such that if $f\in C_0(X)$ and $f\geq0$, then*

$$
I(f)=\sup\{|F(g)|:g\in C_0(X)\text{ and }|g|\leq f\}. \tag{C.16}
$$

*Moreover $\|I\|=\|f\|$.*

**Proof.** Let $C_0(X)_+$ be the positive functions in $C_0(X)$ and for $f$ in $C_0(X)_+$ define $I(f)$ as in (C.16). If $\alpha>0$, then clearly $I(\alpha f)=\alpha I(f)$ if $f\in C_0(X)_+$. Also, if $g\in C_0(X)$ and $|g|\leq f$, then $|F(g)|\leq\|F\|\|g\|\leq\|F\|\|f\|$. Hence $I(f)\leq\|F\|\|f\|<\infty$.



<a id="pdf-page-397"></a>
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



<a id="pdf-page-398"></a>
The proof of this is an involved construction. Inspired by Corollary C.14, one defines $\nu(U)$ for an open set $U$ by

$$
\nu(U)=\sup\{I(\phi):\phi\in C_c(X)_+,\ \phi\leqslant 1,\ \operatorname{spt}\phi\subseteq U\}.
$$

Then for any Borel set $E$, let

$$
\nu(E)=\inf\{\nu(U):E\subseteq U\text{ and }U\text{ is open}\}.
$$

It must now be shown that $\nu$ is a positive measure and $I(f)=\int f\,d\nu$. For the details see (12.36) in Hewitt and Stromberg [1975] or §56 in Halmos [1974]. Indeed, Theorem C.17 is often called the Riesz Representation Theorem.

**C.18. Riesz Representation Theorem.** *If $X$ is a locally compact space and $\mu\in M(X)$, define $F_\mu:C_0(X)\to\mathbb C$ by*

$$
F_\mu(f)=\int f\,d\mu.
$$

*Then $F_\mu\in C_0(X)^*$ and the map $\mu\mapsto F_\mu$ is an isometric isomorphism of $M(X)$ onto $C_0(X)^*$.*

**Proof.** The fact that $\mu\mapsto F_\mu$ is an isometry is the content of Lemma C.13. It remains to show that $\mu\mapsto F_\mu$ is surjective. Let $F\in C_0(X)^*$ and define $I:C_0(X)\to\mathbb C$ as in Lemma C.15. By Theorem C.17, there is a positive measure $\nu$ in $M(X)$ such that $I(f)=\int f\,d\nu$ for all $f$ in $C_0(X)$. If $f\in C_0(X)$, then the definition of $I$ implies that $|F(f)|\leqslant I(|f|)=\int |f|\,d\nu$. Thus, $f\mapsto F(f)$ defines a bounded linear functional on $C_0(X)$ considered as a linear manifold in $L^1(\nu)$. Now $C_0(X)$ is dense in $L^1(\nu)$ (Why?), so $F$ has a unique extension to a bounded linear functional on $L^1(\nu)$. By Theorem B.1 there is a function $\phi$ in $L^\infty(\nu)$ such that $F(f)=\int f\phi\,d\nu$ for every $f$ in $C_0(X)$ and $\|\phi\|_\infty\leqslant 1$. Let $\mu(E)=\int_E\phi\,d\nu$ for every Borel set $E$. Then $\mu\in M(X)$ and by Theorem C.8(a), $F(f)=\int f\,d\mu$; that is, $F=F_\mu$. $\blacksquare$

