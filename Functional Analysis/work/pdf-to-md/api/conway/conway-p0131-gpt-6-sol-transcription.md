3. Show that the function $g$ obtained in Proposition 4.2 is unique.

4. Show that $L\in H(\mathbb D)^*$ if and only if there are scalars $b_0,b_1,\ldots$ in $\mathbb C$ such that $\limsup |b_n|^{1/n}<1$ and $L(f)=\sum_{n=0}^{\infty}\frac{1}{n!}f^{(n)}(0)b_n$.

5. If $G$ is an annulus, describe $H(G)^*$.

6. (Buck [1958]). Let $X$ be locally compact and let $\beta$ be the strict topology on $C_b(X)$ defined in Exercise 1.21. (Also see Exercises 2.6 and 2.7.) Prove the following statements: (a) If $\mu\in M(X)$ and $\varepsilon_n\downarrow 0$, then there are compact sets $K_1,K_2,\ldots$ such that for each $n\geqslant 1$, $K_n\subseteq\operatorname{int}K_{n+1}$ and $|\mu|(X\setminus K_n)<\varepsilon_n$. (b) If $\mu\in M(X)$, then there is a $\phi$ in $C_0(X)$ such that $\phi\geqslant 0$, $|\mu|(X\setminus\{x:\phi(x)>0\})=0$, $1/\phi\in L^1(|\mu|)$, and $\int 1/\phi\,d|\mu|\leqslant 1$. (c) Show that if $\mu\in M(X)$ and $L(f)=\int f\,d\mu$ for $f$ in $C_b(X)$, then $L\in(C_b(X),\beta)^*$. (d) Conversely, if $L\in(C_b(X),\beta)^*$, then there is a $\mu$ in $M(X)$ such that $L(f)=\int f\,d\mu$ for $f$ in $C_b(X)$.

7. Let $X$ be completely regular and let $\mathcal M$ be a linear manifold in $C(X)$. Show that if for every compact subset $K$ of $X$, $\mathcal M|K\equiv\{f|K:f\in\mathcal M\}$ is dense in $C(K)$, then $\mathcal M$ is dense in $C(X)$.

## §5*. Inductive Limits and the Space of Distributions

In this section the most general definition of an inductive limit will not be presented. Rather one that removes certain technicalities from the arguments and yet covers the most important examples will be given. For the more general definition see Köthe [1969], Robertson and Robertson [1966], or Schaefer [1971].

**5.1. Definition.** An *inductive system* is a pair $(\mathcal X,\{\mathcal X_i:i\in I\})$, where $\mathcal X$ is a vector space, $\mathcal X_i$ is a linear manifold in $\mathcal X$ that has a topology $\mathcal T_i$ such that $(\mathcal X_i,\mathcal T_i)$ is a LCS, and, moreover:

(a) $I$ is a directed set and $\mathcal X_i\subseteq\mathcal X_j$ if $i\leqslant j$;

(b) if $i\leqslant j$ and $U_j\in\mathcal T_j$, then $U_j\cap\mathcal X_i\in\mathcal T_i$;

(c) $\mathcal X=\bigcup\{\mathcal X_i:i\in I\}$.

Note that condition (b) is equivalent to the condition that the inclusion map $\mathcal X_i\hookrightarrow\mathcal X_j$ is continuous.

**5.2. Example.** Let $d\geqslant 1$ and let $\Omega$ be an open subset of $\mathbb R^d$. Denote by $C_c^{(\infty)}(\Omega)$ all the functions $\phi:\Omega\to\mathbb F$ such that $\phi$ is infinitely differentiable and has compact support in $\Omega$. (The support of $\phi$ is defined by $\operatorname{spt}\phi\equiv\operatorname{cl}\{x:\phi(x)\ne 0\}$.) If $K$ is a compact subset of $\Omega$, define $\mathcal D(K)\equiv\{\phi\in C_c^{(\infty)}(\Omega):\operatorname{spt}\phi\subseteq K\}$. Let $\mathcal D(K)$ have the topology defined by the seminorms

$$
p_{K,m}(\phi)=\sup\{|\phi^{(k)}(x)|:|k|\leqslant m,\ x\in K\},
$$
