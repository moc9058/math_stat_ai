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
