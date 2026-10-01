# IX. Normal Operators on Hilbert Space


<a id="pdf-page-270"></a>
# CHAPTER IX

# Normal Operators on Hilbert Space

In this chapter the Spectral Theorem for normal operators on a Hilbert space is proved. This theorem is then used to answer a number of questions concerning normal operators. In fact, the Spectral Theorem can be used to answer essentially every question about normal operators.

## §1. Spectral Measures and Representations of Abelian C*-Algebras

<!-- BEGIN BACKGROUND BG-IX.block1 -->
<a id="bg-ix-1"></a>
### Definition BG-IX.1 — Measurability and simple approximation

A $\sigma$-algebra contains $X$ and is closed under complements and countable unions. A complex function is measurable when inverse images of open subsets of $\mathbb C$ belong to that collection. A **simple function** has finite range and measurable level sets. Every bounded measurable complex function is a uniform limit of simple functions: partition a bounded square containing its range into finitely many half-open squares of side $1/n$ and select one value in each occupied square. The error is at most $\sqrt2/n$ everywhere.

<a id="bg-ix-2"></a>
### Theorem BG-IX.2 — Monotone, Fatou, and dominated convergence

For a positive measure $\mu$: (i) if $0\leq f_n\uparrow f$, then $\int f_n\uparrow\int f$; (ii) if $f_n\geq0$, then $\int\liminf f_n\leq\liminf\int f_n$; (iii) if $f_n\to f$ almost everywhere and $|f_n|\leq g\in L^1(\mu)$, then $\int|f_n-f|\to0$ and $\int f_n\to\int f$.

**Proof.** For (i), write $L=\lim\int f_n\leq\int f$. If $s$ is a nonnegative simple function below $f$ and $0<c<1$, the sets $A_n=\{f_n\geq cs\}$ increase to a set containing $\{s>0\}$. Continuity from below for measures follows by writing an increasing union as the disjoint union of successive differences. Apply it to the finitely many level sets of $s$ to get $L\geq c\int s$. Take the supremum over $s$ and then $c\uparrow1$. For (ii), apply (i) to $h_n=\inf_{k\geq n}f_k$ and use $\int h_n\leq\inf_{k\geq n}\int f_k$. For (iii), $|f|\leq g$ almost everywhere. Apply (ii) to $2g-|f_n-f|$ to get $2\int g\leq2\int g-\limsup\int|f_n-f|$. The integral triangle inequality finishes the proof. $\square$

For a complex measure $\nu$, use its positive total variation $|\nu|$ for domination and $|\int h\,d\nu|\leq\int|h|\,d|\nu|$. A proof of the Radon–Nikodym tool is supplied in [Appendix C](appendix-c.md).
<!-- END BACKGROUND BG-IX.block1 -->

Before beginning this section the reader should familiarize himself with the definitions and examples in (VIII.5.1) through (VIII.5.8).

In this section we want to focus our attention on representations of abelian $C^*$-algebras. The reason for this is that the Spectral Theorem and its generalizations can be obtained as a special case of such a theory. The idea is the following. Let $N$ be a normal operator on $\mathcal H$. Then $C^*(N)$ is an abelian $C^*$-algebra and the functional calculus $f\mapsto f(N)$ is a $*$-isomorphism of $C(\sigma(N))$ onto $C^*(N)$ (VIII.2.6). Thus $f\mapsto f(N)$ is a representation $C(\sigma(N))\to\mathcal B(\mathcal H)$ of the abelian $C^*$-algebra $C(\sigma(N))$. A diagnosis of such representations yields the Spectral Theorem.

A representation $\rho:C(X)\to\mathcal B(\mathcal H)$ is a $*$-homomorphism with $\rho(1)=1$. Also, $\|\rho\|=1$ (VIII.1.11d). If $f\in C(X)_+$, then $f=g^2$ where $g\in C(X)_+$; hence $\rho(f)=\rho(g)^2=\rho(g)^*\rho(g)\geq 0$. So $\rho$ is a positive map. One might expect, by analogy with the Riesz Representation Theorem, that $\rho(f)=\int f\,dE$ for some type of measure $E$ whose values are operators rather than scalars. This is indeed the case. We begin by introducing these measures and defining the integral of a scalar-valued function with respect to one of them.



<a id="pdf-page-271"></a>
**1.1. Definition.** If $X$ is a set, $\Omega$ is a $\sigma$-algebra of subsets of $X$, and $\mathcal H$ is a Hilbert space, a *spectral measure* for $(X,\Omega,\mathcal H)$ is a function $E:\Omega\to\mathcal B(\mathcal H)$ such that:

(a) for each $\Delta$ in $\Omega$, $E(\Delta)$ is a projection;

(b) $E(\square)=0$ and $E(X)=1$;

(c) $E(\Delta_1\cap\Delta_2)=E(\Delta_1)E(\Delta_2)$ for $\Delta_1$ and $\Delta_2$ in $\Omega$;

(d) if $\{\Delta_n\}_{n=1}^{\infty}$ are pairwise disjoint sets from $\Omega$, then

$$
E\left(\bigcup_{n=1}^{\infty}\Delta_n\right)
=\sum_{n=1}^{\infty}E(\Delta_n).
$$

A word or two concerning condition (d) in the preceding definition. If $\{E_n\}$ is a sequence of pairwise orthogonal projections on $\mathcal H$, then it was shown in Exercise II.3.5 that for each $h$ in $\mathcal H$, $\sum_{n=1}^{\infty}E_n(h)$ converges in $\mathcal H$ to $E(h)$, where $E$ is the orthogonal projection of $\mathcal H$ onto $\bigvee\{E_n(\mathcal H):n\geq 1\}$. Thus it is legitimate to write $E=\sum_{n=1}^{\infty}E_n$. Now if $\Delta_1\cap\Delta_2=\square$, then (b) and (c) above imply that $0=E(\Delta_1)E(\Delta_2)=E(\Delta_2)E(\Delta_1)$; that is, $E(\Delta_1)$ and $E(\Delta_2)$ have orthogonal ranges. So if $\{\Delta_n\}_1^\infty$ is a sequence of pairwise disjoint sets in $\Omega$, the ranges of $\{E(\Delta_n)\}$ are pairwise orthogonal. Thus the equation $E(\bigcup_1^\infty\Delta_n)=\sum_1^\infty E(\Delta_n)$ in (d) has the precise meaning just discussed.

Another way to discuss this is by the introduction of two topologies that will also be of value later.

**1.2. Definition.** If $\mathcal H$ is a Hilbert space, the *weak operator topology* (WOT) on $\mathcal B(\mathcal H)$ is the locally convex topology defined by the seminorms $\{p_{h,k}:h,k\in\mathcal H\}$ where $p_{h,k}(A)=|\langle Ah,k\rangle|$. The *strong operator topology* (SOT) is the topology defined on $\mathcal B(\mathcal H)$ by the family of seminorms $\{p_h:h\in\mathcal H\}$, where $p_h(A)=\|Ah\|$.

**1.3. Proposition.** Let $\mathcal H$ be a Hilbert space and let $\{A_i\}$ be a net in $\mathcal B(\mathcal H)$.

(a) $A_i\to A$ (WOT) if and only if $\langle A_i h,k\rangle\to\langle Ah,k\rangle$ for all $h,k$ in $\mathcal H$.

(b) If $\sup_i\|A_i\|<\infty$ and $\mathcal T$ is a total subset of $\mathcal H$, then $A_i\to A$ (WOT) if and only if $\langle A_i h,k\rangle\to\langle Ah,k\rangle$ for all $h,k$ in $\mathcal T$.

(c) $A_i\to A$ (SOT) if and only if $\|A_i h-Ah\|\to 0$ for all $h$ in $\mathcal H$.

(d) If $\sup_i\|A_i\|<\infty$ and $\mathcal T$ is a total subset of $\mathcal H$, then $A_i\to A$ (SOT) if and only if $\|A_i h-Ah\|\to 0$ for all $h$ in $\mathcal T$.

(e) If $\mathcal H$ is separable, then the WOT and SOT are metrizable on bounded subsets of $\mathcal B(\mathcal H)$.

**Proof.** The proofs of (a) through (d) are left as exercises. For (e), let $\{h_n\}$ be any countable total subset of ball $\mathcal H$. If $A,B\in\mathcal B(\mathcal H)$, let

$$
d_s(A,B)=\sum_{n=1}^{\infty}2^{-n}\|(A-B)h_n\|,
$$

$$
d_w(A,B)=\sum_{m,n=1}^{\infty}2^{-n-m}
\left|\left\langle(A-B)h_n,h_m\right\rangle\right|.
$$



<a id="pdf-page-272"></a>
§1. Spectral Measures and Representations of Abelian $C^*$-Algebras  257

Then $d_s$ and $d_w$ are metrics on $\mathcal B(\mathcal H)$. It is left as an exercise to show that $d_s$ and $d_w$ define the SOT and WOT on bounded subsets of $\mathcal B(\mathcal H)$. ■

**1.4. Example.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space. If $\phi\in L^\infty(\mu)$, let $M_\phi$ be the multiplication operator on $L^2(\mu)$. Then a net $\{\phi_i\}$ in $L^\infty(\mu)$ converges weak* to $\phi$ if and only if $M_{\phi_i}\to M_\phi$ (WOT). In fact, if $f,g\in L^2(\mu)$ and $\phi_i\to\phi$ weak* in $L^\infty(\mu)$, then $\langle M_{\phi_i}f,g\rangle=\int\phi_i f\bar g\,d\mu\to\int\phi f\bar g\,d\mu=\langle M_\phi f,g\rangle$ since $f\bar g\in L^1(\mu)$. Conversely, if $M_{\phi_i}\to M_\phi$ (WOT) and $f\in L^1(\mu)$, then $f=g_1\bar g_2$, where $g_1,g_2\in L^2(\mu)$. (Why?) So $\int\phi_i f\,d\mu=\langle M_{\phi_i}g_1,g_2\rangle\to\langle M_\phi g_1,g_2\rangle=\int\phi f\,d\mu$.

**1.5. Example.** If $\{E_n\}$ is a sequence of pairwise orthogonal projections on $\mathcal H$, then $\sum_1^\infty E_n$ converges (SOT) to the projection of $\mathcal H$ onto $\bigvee\{E_n(\mathcal H):n\geq 1\}$.

In light of (1.5), a spectral measure for $(X,\Omega,\mathcal H)$ could be defined as a SOT-countably additive projection-valued measure.

**1.6. Example.** Let $X$ be a compact set. $\Omega=$ the Borel subsets of $X$, $\mu=$ a measure on $\Omega$, and $\mathcal H=L^2(\mu)$. For $\Delta$ in $\Omega$, let $E(\Delta)=$ multiplication by $\chi_\Delta$, the characteristic function of $\Delta$. $E$ is a spectral measure for $(X,\Omega,\mathcal H)$.

**1.7. Example.** If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$, the *inflation*, $E^{(n)}$, of $E$, defined by $E^{(n)}(\Delta)=E(\Delta)^{(n)}$, is a spectral measure for $(X,\Omega,\mathcal H^{(n)})$.

**1.8. Example.** Let $X$ be any set, $\Omega=$ all the subsets of $X$, $\mathcal H=$ any separable Hilbert space, and fix a sequence $\{x_n\}$ in $X$. If $\{e_1,e_2,\ldots\}$ is some orthonormal basis for $\mathcal H$, define $E(\Delta)=$ the projection onto $\bigvee\{e_n:x_n\in\Delta\}$. $E$ is a spectral measure for $(X,\Omega,\mathcal H)$.

The next lemma is useful in studying spectral measures as it allows us to prove things about spectral measures from known facts about complex-valued measures.

**1.9. Lemma.** *If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$ and $g,h\in\mathcal H$, then*

$$
E_{g,h}(\Delta)\equiv\langle E(\Delta)g,h\rangle
$$

*defines a countably additive measure on $\Omega$ with total variation $\leq\|g\|\|h\|$.*

**PROOF.** That $\mu=E_{g,h}$ as defined above, is a countably additive measure is left for the reader to verify. If $\Delta_1,\ldots,\Delta_n$ are pairwise disjoint sets in $\Omega$, let $\alpha_j\in\mathbb C$ such that $|\alpha_j|=1$ and $|\langle E(\Delta_j)g,h\rangle|=\alpha_j\langle E(\Delta_j)g,h\rangle$. So $\sum_j|\mu(\Delta_j)|=\sum_j\alpha_j\langle E(\Delta_j)g,h\rangle=\langle\sum_j E(\Delta_j)\alpha_jg,h\rangle\leq\|\sum_j E(\Delta_j)\alpha_jg\|\|h\|$. Now $\{E(\Delta_j)\alpha_jg:1\leq j\leq n\}$ is a finite sequence of pairwise orthogonal vectors so that $\|\sum_j E(\Delta_j)\alpha_jg\|^2=\sum_j\|E(\Delta_j)g\|^2=\|E(\bigcup_{j=1}^n\Delta_j)g\|^2\leq\|g\|^2$; hence $\sum_j|\mu(\Delta_j)|\leq\|g\|\|h\|$. Thus $\|\mu\|\leq\|g\|\|h\|$. ■

It is possible to use spectral measures to define representations. The next



<a id="pdf-page-273"></a>
258  
IX. Normal Operators on Hilbert Space

result is crucial for this purpose. It tells us how to integrate with respect to a spectral measure.

**1.10. Proposition.** *If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$ and $\phi:X\to\mathbb C$ is a bounded $\Omega$-measurable function, then there is a unique operator $A$ in $\mathcal B(\mathcal H)$ such that if $\varepsilon>0$ and $\{\Delta_1,\ldots,\Delta_n\}$ is an $\Omega$-partition of $X$ with $\sup\{|\phi(x)-\phi(x')|:x,x'\in\Delta_k\}<\varepsilon$ for $1\leq k\leq n$, then for any $x_k$ in $\Delta_k$,*

$$
\left\|A-\sum_{k=1}^{n}\phi(x_k)E(\Delta_k)\right\|<\varepsilon.
$$

**Proof.** Define $B(g,h)\equiv\int\phi\,dE_{g,h}$ for $g,h$ in $\mathcal H$. By the preceding lemma it is easy to see that $B$ is a sesquilinear form with $|B(g,h)|\leq\|\phi\|_\infty\|g\|\|h\|$. Hence there is a unique operator $A$ such that $B(g,h)=\langle Ag,h\rangle$ for all $g$ and $h$ in $\mathcal H$.

Let $\{\Delta_1,\ldots,\Delta_n\}$ be an $\Omega$-partition satisfying the condition in the statement of the proposition. If $g$ and $h$ are arbitrary vectors in $\mathcal H$ and $x_k\in\Delta_k$ for $1\leq k\leq n$, then

$$
\begin{aligned}
\left|\langle Ag,h\rangle-\sum_{k=1}^{n}\phi(x_k)\langle E(\Delta_k)g,h\rangle\right|
&=\left|\sum_{k=1}^{n}\int_{\Delta_k}[\phi(x)-\phi(x_k)]\,d\langle E(x)g,h\rangle\right|\\
&\leq\sum_{k=1}^{n}\int_{\Delta_k}|\phi(x)-\phi(x_k)|\,d|\langle E(x)g,h\rangle|\\
&\leq\varepsilon\int d|\langle E(x)g,h\rangle|
\leq\varepsilon\|g\|\|h\|.
\end{aligned}
$$

$\blacksquare$

The operator $A$ obtained in the preceding proposition is the *integral of $\phi$ with respect to $E$* and is denoted by

$$
\int\phi\,dE.
$$

Therefore if $g,h\in\mathcal H$ and $\phi$ is a bounded $\Omega$-measurable function on $X$, the preceding proof implies that

$$
\left\langle\left(\int\phi\,dE\right)g,h\right\rangle
=\int\phi\,dE_{g,h}. \tag{1.11}
$$

Let $B(X,\Omega)$ denote the set of bounded $\Omega$-measurable functions $\phi:X\to\mathbb C$ and let $\|\phi\|=\sup\{|\phi(x)|:x\in X\}$. It is easy to see that $B(X,\Omega)$ is a Banach algebra with identity. In fact, if $\phi^*(x)\equiv\overline{\phi(x)}$, then $B(X,\Omega)$ is an abelian $C^*$-algebra. The properties of the integral $\int\phi\,dE$ are summarized by the following result.

**1.12. Proposition.** *If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$ and $\rho:B(X,\Omega)\to\mathcal B(\mathcal H)$ is defined by $\rho(\phi)=\int\phi\,dE$, then $\rho$ is representation of $B(X,\Omega)$ and $\rho(\phi)$ is a normal operator for every $\phi$ in $B(X,\Omega)$.*



<a id="pdf-page-274"></a>
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



<a id="pdf-page-275"></a>
Representation Theorem for linear functionals on $C(X)$. We wish to extend $\rho$ to a representation $\tilde{\rho}:B(X)\to\mathcal{B}(\mathcal{H})$, where $B(X)$ is the $C^*$-algebra of bounded Borel functions. The measure $E$ of a Borel set $\Delta$ is then defined by letting $E(\Delta)=\tilde{\rho}(\chi_\Delta)$. In fact, it is possible to give a proof of the theorem patterned on the proof of the Riesz Representation Theorem. Here, however, the proof will use the Riesz Representation Theorem to simplify the technical details.

If $g,h\in\mathcal{H}$, then $u\mapsto\langle\rho(u)g,h\rangle$ is a linear functional on $C(X)$ with norm $\leq\|g\|\|h\|$. Hence there is a unique measure, $\mu_{g,h}$ in $M(X)$ such that

$$
\langle\rho(u)g,h\rangle=\int u\,d\mu_{g,h} \tag{1.15}
$$

for all $u$ in $C(X)$. It is easy to verify that the map $(g,h)\mapsto\mu_{g,h}$ is sesquilinear (use uniqueness) and $\|\mu_{g,h}\|\leq\|g\|\|h\|$. Now fix $\phi$ in $B(X)$ and define $[g,h]=\int\phi\,d\mu_{g,h}$. Then $[\cdot,\cdot]$ is a sesquilinear form and $|[g,h]|\leq\|\phi\|\|g\|\|h\|$. Hence there is a unique bounded operator $A$ such that $[g,h]=\langle Ag,h\rangle$ and $\|A\|\leq\|\phi\|$ (II.2.2). Denote the operator $A$ by $\tilde{\rho}(\phi)$. So $\tilde{\rho}:B(X)\to\mathcal{B}(\mathcal{H})$ is a well-defined function, $\|\tilde{\rho}(\phi)\|\leq\|\phi\|$, and for all $g,h$ in $\mathcal{H}$,

$$
\langle\tilde{\rho}(\phi)g,h\rangle=\int\phi\,d\mu_{g,h}. \tag{1.16}
$$

**1.17. Claim.** $\tilde{\rho}:B(X)\to\mathcal{B}(\mathcal{H})$ is a representation and $\tilde{\rho}|C(X)=\rho$.

The fact that $\tilde{\rho}(u)=\rho(u)$ whenever $u\in C(X)$ follows immediately from (1.15) and (1.16). If $\phi\in B(X)$, consider $\phi$ as an element of $M(X)^*$ $(=C(X)^{**})$; that is, $\phi$ corresponds to the linear functional $\mu\mapsto\int\phi\,d\mu$. By Proposition V.4.1, $\{u\in C(X):\|u\|\leq\|\phi\|\}$ is $\sigma(M(X)^*,M(X))$ dense in $\{L\in M(X)^*:\|L\|\leq\|\phi\|\}$. Thus there is a net $\{u_i\}$ in $C(X)$ such that $\|u_i\|\leq\|\phi\|$ for all $u_i$ and $\int u_i\,d\mu\to\int\phi\,d\mu$ for every $\mu$ in $M(X)$. If $\psi\in B(X)$, then $\psi\mu\in M(X)$ whenever $\mu\in M(X)$. Hence $\int u_i\psi\,d\mu\to\int\phi\psi\,d\mu$ for every $\psi$ in $B(X)$ and $\mu$ in $M(X)$. By (1.16), $\tilde{\rho}(u_i\psi)\to\tilde{\rho}(\phi\psi)$ (WOT) for all $\psi$ in $B(X)$. In particular, if $\psi\in C(X)$, then $\tilde{\rho}(\phi\psi)=\operatorname{WOT}-\lim\tilde{\rho}(u_i\psi)=\operatorname{WOT}-\lim\rho(u_i)\rho(\psi)=\tilde{\rho}(\phi)\rho(\psi)$. That is,

$$
\tilde{\rho}(\phi\psi)=\tilde{\rho}(\phi)\rho(\psi)
$$

whenever $\phi\in B(X)$ and $\psi\in C(X)$. Hence $\tilde{\rho}(u_i\psi)=\rho(u_i)\tilde{\rho}(\psi)$ for any $\psi$ in $B(X)$ and for all $u_i$. Since $\tilde{\rho}(u_i)\to\tilde{\rho}(\phi)$ (WOT) and $\tilde{\rho}(u_i\psi)\to\tilde{\rho}(\phi\psi)$ (WOT), this implies that

$$
\tilde{\rho}(\phi\psi)=\tilde{\rho}(\phi)\tilde{\rho}(\psi)
$$

whenever $\phi,\psi\in B(X)$.

The proof that $\tilde{\rho}$ is linear is immediate by (1.16). To see that $\tilde{\rho}(\phi)^*=\tilde{\rho}(\bar{\phi})$. Let $\{u_i\}$ be the net obtained in the preceding paragraph. If $\mu\in M(X)$, let $\bar{\mu}$ be the measure defined by $\bar{\mu}(\Delta)=\overline{\mu(\Delta)}$. Then $\rho(u_i)\to\tilde{\rho}(\phi)$ (WOT) and so $\rho(u_i)^*\to\tilde{\rho}(\phi)^*$ (WOT). But $\int\bar{u}_i\,d\mu=\overline{\int u_i\,d\bar{\mu}}\to\overline{\int\phi\,d\bar{\mu}}=\int\bar{\phi}\,d\mu$ for every measure


<a id="pdf-page-276"></a>
$\mu$. Hence $\rho(\bar u_i)\rightarrow\tilde{\rho}(\bar\phi)$. But $\rho(u_i)^*=\rho(\bar u_i)$ since $\rho$ is a *-homomorphism. Thus $\tilde{\rho}(\phi)^*=\tilde{\rho}(\bar\phi)$ and $\tilde{\rho}$ is a representation.

For any Borel subset $\Delta$ of $X$ let $E(\Delta)\equiv\tilde{\rho}(\chi_\Delta)$. We want to show that $E$ is a spectral measure. Since $\chi_\Delta$ is a hermitian idempotent in $B(X)$, $E(\Delta)$ is a projection by (1.17). Since $\chi_\square=0$ and $\chi_X=1$, $E(\square)=0$ and $E(X)=1$. Also, $E(\Delta_1\cap\Delta_2)=\tilde{\rho}(\chi_{\Delta_1\cap\Delta_2})=\tilde{\rho}(\chi_{\Delta_1}\chi_{\Delta_2})=E(\Delta_1)E(\Delta_2)$. Now let $\{\Delta_n\}$ be a pairwise disjoint sequence of Borel sets and put $\Lambda_n=\bigcup_{k=n+1}^{\infty}\Delta_k$. It is easy to see that $E$ is finitely additive so if $h\in\mathcal H$, then

$$
\begin{aligned}
\left\|E\left(\bigcup_{k=1}^{\infty}\Delta_k\right)h-\sum_{k=1}^{n}E(\Delta_k)h\right\|^2
&=\langle E(\Lambda_n)h,E(\Lambda_n)h\rangle\\
&=\langle E(\Lambda_n)h,h\rangle\\
&=\langle\tilde{\rho}(\chi_{\Lambda_n})h,h\rangle\\
&=\int\chi_{\Lambda_n}\,d\mu_{h,h}\\
&=\sum_{k=n+1}^{\infty}\mu_{h,h}(\Delta_k)\rightarrow 0
\end{aligned}
$$

as $n\rightarrow\infty$. Therefore $E$ is a spectral measure.

It remains to show that $\rho(u)=\int u\,dE$. It will be shown that $\tilde{\rho}(\phi)=\int\phi\,dE$ for every $\phi$ in $B(X)$. Fix $\phi$ in $B(X)$ and $\varepsilon>0$. If $\{\Delta_1,\ldots,\Delta_n\}$ is any Borel partition of $X$ such that $\sup\{|\phi(x)-\phi(x')|:x,x'\in\Delta_k\}<\varepsilon$ for $1\leqslant k\leqslant n$, then $\left\|\phi-\sum_{k=1}^{n}\phi(x_k)\chi_{\Delta_k}\right\|_\infty<\varepsilon$ for any choice of $x_k$ in $\Delta_k$. Since $\|\tilde{\rho}\|=1$, $\varepsilon>\left\|\tilde{\rho}(\phi)-\sum_{k=1}^{n}\phi(x_k)E(\Delta_k)\right\|$. This implies that $\tilde{\rho}(\phi)=\int\phi\,dE$ for any $\phi$ in $B(X)$.

The proof of the uniqueness of $E$ is left to the reader. ■

## EXERCISES

1. Prove Proposition 1.3.

2. Show that ball $\mathcal B(\mathcal H)$ is WOT compact.

3. Show that $\operatorname{Re}\mathcal B(\mathcal H)$ and $\mathcal B(\mathcal H)_1$ are WOT and SOT closed.

4. If $L:\mathcal B(\mathcal H)\rightarrow\mathbb C$ is a linear functional, show that the following statements are equivalent: (a) $L$ is SOT-continuous; (b) $L$ is WOT-continuous; (c) there are vectors $h_1,\ldots,h_n,g_1,\ldots,g_n$ in $\mathcal H$ such that $L(A)=\sum_{j=1}^{n}\langle Ah_j,g_j\rangle$.

5. Show that a convex subset of $\mathcal B(\mathcal H)$ is WOT closed if and only if it is SOT closed.

6. Verify the statement in Example 1.5.

7. Verify the statements made in Examples 1.6, 1.7, and 1.8.

8. For the spectral measures in (1.6), (1.7), and (1.8), give the corresponding representations.

9. If $\{E_i\}$ is a net of projections and $E$ is a projection, show that $E_i\rightarrow E$ (WOT) if and only if $E_i\rightarrow E$ (SOT).



   <a id="pdf-page-277"></a>
10. For the representation in (VIII.5.5), find the corresponding spectral measure.

11. In Example VIII.5.4, the representation is not quite covered by Theorem 1.14 since it is a representation of $L^\infty(\mu)$ and not $C(X)$. Nevertheless, this representation is given by a spectral measure defined on $\Omega$. Find it.

12. Let $X$ be a compact Hausdorff space and let $\{x_n\}$ be a sequence in $X$. Let $\{e_n\}$ be an orthonormal basis for $\mathcal H$ and for each $u$ in $C(X)$ define $\rho(u)$ in $\mathcal B(\mathcal H)$ by $\rho(u)e_n=u(x_n)e_n$. Show that $\rho$ is a representation and find the corresponding spectral measure.

13. A representation $\rho:\mathcal A\to\mathcal B(\mathcal H)$ is *irreducible* if the only projections in $\mathcal B(\mathcal H)$ that commute with every $\rho(a)$, $a$ in $\mathcal A$, are 0 and 1. Prove that if $\mathcal A$ is abelian and $\rho$ is an irreducible representation of $\mathcal A$, then $\dim\mathcal H=1$. Find the corresponding spectral measure.

14. Show that a representation $\rho:C(X)\to\mathcal B(\mathcal H)$ is injective if and only if $E(G)\ne0$ for every non-empty open set $G$, where $E$ is the corresponding spectral measure.

15. Let $\{A_i\}$ be a net of hermitian operators on $\mathcal H$ and suppose that there is a hermitian operator $T$ such that $A_i\leq T$ for all $i$. If $\{\langle A_i h,h\rangle\}$ is an increasing net in $\mathbb R$ for every $h$ in $\mathcal H$, then there is a hermitian operator $A$ such that $A_i\to A\;(\mathrm{WOT})$.

16. Show that there is a contraction $\tau:\mathcal B(\mathcal H)^{**}\to\mathcal B(\mathcal H)$ such that $\tau(T)=T$ for $T$ in $\mathcal B(\mathcal H)$. If $\rho:C(X)\to\mathcal B(\mathcal H)$ is a representation, show that the map $\tilde\rho$ in the proof of Theorem 1.14 is given by $\tilde\rho(\phi)=\tau\circ\rho^{**}(\phi)$.

## §2. The Spectral Theorem

The Spectral Theorem is a landmark in the theory of operators on a Hilbert space. It provides a complete statement about the nature and structure of normal operators. This accolade will be seen to be deserved when in Section 10 the Spectral Theorem is used to give a complete set of unitary invariants. Two operators $A$ and $B$ are *unitarily equivalent* if there is a unitary operator $U$ such that $UAU^*=B$; in symbols, $A\cong B$. Using the Spectral Theorem, a (countable) set of objects is attached to a normal operator $N$ on a (separable) Hilbert space. It is then shown that two normal operators are unitarily equivalent if and only if these objects are equal.

The Spectral Theorem for a normal operator $N$ on a Hilbert space with $\dim\mathcal H=d<\infty$ says that $N$ can be diagonalized. That is, if $\alpha_1,\ldots,\alpha_d$ are the eigenvalues of $N$ (repeated as often as their multiplicities), then the corresponding eigenvectors $e_1,e_2,\ldots,e_d$ from an orthonormal basis for $\mathcal H$. In infinite dimensional spaces a normal operator need not have eigenvalues. For example, let $N=$ multiplication by the independent variable on $L^2(0,1)$. So an alternative formulation that can be generalized is desired.

Let $N$ be normal on $\mathcal H$, $\dim\mathcal H=d<\infty$. Let $\lambda_1,\ldots,\lambda_n$ be the distinct eigenvalues of $N$ and let $E_k$ be the orthogonal projection of $\mathcal H$ onto



<a id="pdf-page-278"></a>
$\ker(N-\lambda_k)$, $1\leq k\leq n$. Then the Spectral Theorem says that

$$
N=\sum_{k=1}^{n}\lambda_kE_k. \tag{2.1}
$$

In this form a generalization is possible. Rather than discuss orthogonal projections on eigenspaces (which may not exist), the concept of a spectral measure is used; rather than the sum that appears in (2.1), an integral is used. It is worth mentioning that the finite dimensional version is a corollary of the general theorem (see Exercise 4).

**2.2. The Spectral Theorem.** *If $N$ is a normal operator, there is a unique spectral measure $E$ on the Borel subsets of $\sigma(N)$ such that:*

(a) $N=\int z\,dE(z)$;

(b) *if $G$ is a nonempty relatively open subset of $\sigma(N)$, $E(G)\neq 0$;*

(c) *if $A\in\mathcal{B}(\mathcal{H})$, then $AN=NA$ and $AN^*=N^*A$ if and only if $AE(\Delta)=E(\Delta)A$ for every $\Delta$.*

**Proof.** Let $\mathcal{A}=C^*(N)$, the $C^*$-algebra generated by $N$. So $\mathcal{A}$ is the closure of all polynomials in $N$ and $N^*$. By Theorem VIII.2.6, there is an isometric isomorphism $\rho:C(\sigma(N))\to\mathcal{A}\subseteq\mathcal{B}(\mathcal{H})$ given by $\rho(u)=u(N)$ (the functional calculus). By Theorem 1.14 there is a unique spectral measure $E$ defined on the Borel subsets of $\sigma(N)$ such that $\rho(u)=\int u\,dE$ for all $u$ in $C(\sigma(N))$. In particular, (a) holds since $N=\rho(z)$.

If $G$ is a nonempty relatively open subset of $\sigma(N)$, there is a nonzero continuous function $u$ on $\sigma(N)$ such that $0\leq u\leq\chi_G$. Using Claim 1.17, one obtains that $E(G)=\tilde{\rho}(\chi_G)\geq\rho(u)\neq 0$; so (b) holds.

Now let $A\in\mathcal{B}(\mathcal{H})$ such that $AN=NA$ and $AN^*=N^*A$. It is not hard to see that this implies, by the Stone-Weierstrass Theorem, that $A\rho(u)=\rho(u)A$ for every $u$ in $C(\sigma(N))$; that is, $Au(N)=u(N)A$ for all $u$ in $C(\sigma(N))$. Let $\Omega=\{\Delta:\Delta\text{ is a Borel set and }AE(\Delta)=E(\Delta)A\}$. It is left to the reader to show that $\Omega$ is a $\sigma$-algebra. If $G$ is an open set in $\sigma(N)$, there is a sequence $\{u_n\}$ of positive continuous functions on $\sigma(N)$ such that $u_n(z)\uparrow\chi_G(z)$ for all $z$. Thus

$$
\begin{aligned}
\langle AE(G)g,h\rangle
&=\langle E(G)g,A^*h\rangle\\
&=E_{g,A^*h}(G)\\
&=\lim\int u_n\,dE_{g,A^*h}\\
&=\lim\langle u_n(N)g,A^*h\rangle\\
&=\lim\langle Au_n(N)g,h\rangle\\
&=\lim\langle u_n(N)Ag,h\rangle\\
&=\langle E(G)Ag,h\rangle.
\end{aligned}
$$



<a id="pdf-page-279"></a>
So $\Omega$ contains every open set and, hence, it must be the collection of Borel sets. The converse is left to the reader. $\blacksquare$

The unique spectral measure $E$ obtained in the Spectral Theorem is called the *spectral measure for $N$*. An abbreviation for the Spectral Theorem is to say, “Let $N=\int\lambda\,dE(\lambda)$ be the *spectral decomposition* of $N$.” If $\phi$ is a bounded Borel function on $\sigma(N)$, define $\phi(N)$ by

$$
\phi(N)\equiv\int\phi\,dE,
$$

where $E$ is the spectral measure for $N$.

**2.3. Theorem.** *If $N$ is a normal operator on $\mathcal H$ with spectral measure $E$ and $B(\sigma(N))$ is the $C^*$-algebra of bounded Borel functions on $\sigma(N)$, then the map*

$$
\phi\mapsto\phi(N)
$$

*is a representation of the $C^*$-algebra $B(\sigma(N))$. If $\{\phi_i\}$ is a net in $B(\sigma(N))$ such that $\int\phi_i\,d\mu\to0$ for every $\mu$ in $M(\sigma(N))$, then $\phi_i(N)\to0$ (WOT). This map is unique in the sense that if $\tau:B(\sigma(N))\to\mathcal B(\mathcal H)$ is a representation such that $\tau(z)=N$ and $\tau(\phi_i)\to0$ (WOT) whenever $\{\phi_i\}$ is a bounded net in $B(\sigma(N))$ such that $\int\phi_i\,d\mu\to0$ for every $\mu$ in $M(\sigma(N))$, then $\tau(\phi)=\phi(N)$ for all $\phi$ in $B(\sigma(N))$.*

**Proof.** The fact that $\phi\mapsto\phi(N)$ is a representation is a consequence of Proposition 1.12. If $\{\phi_i\}$ is as in the statement, then the fact that $E_{g,h}\in M(\sigma(N))$ implies that $\phi_i(N)\to0$ (WOT).

To prove uniqueness, let $\tau:B(\sigma(N))\to\mathcal B(\mathcal H)$ be a representation with the appropriate properties. Then $\tau(u)=u(N)$ if $u\in C(\sigma(N))$ by the uniqueness of the functional calculus for normal elements of a $C^*$-algebra (VIII.2.6). If $\phi\in B(\sigma(N))$, then Proposition V.4.1 implies that there is a net $\{u_i\}$ in $C(\sigma(N))$ such that $\|u_i\|\leq\|\phi\|$ for all $u_i$ and $\int u_i\,d\mu\to\int\phi\,d\mu$ for every $\mu$ in $M(\sigma(N))$. Thus $u_i(N)\to\phi(N)$ (WOT). But $\tau(\phi)=\mathrm{WOT}\!-\!\lim\tau(u_i)=\mathrm{WOT}\!-\!\lim u_i(N)$; therefore $\tau(\phi)=\phi(N)$. $\blacksquare$

It is worthwhile to rewrite (1.11) as

$$
\tag{2.4}
\langle\phi(N)g,h\rangle=\int\phi\,dE_{g,h}
$$

for $\phi$ in $B(\sigma(N))$ and $g,h$ in $\mathcal H$. If $\phi\in B(\mathbb C)$, then the restriction of $\phi$ to $\sigma(N)$ belongs to $B(\sigma(N))$. Since the support of each measure $E_{g,h}$ is contained in $\sigma(N)$, (2.4) holds for every bounded Borel function $\phi$ on $\mathbb C$. This has certain technical advantages that will become apparent when we begin to apply (2.4).

Proposition 2.3 thus extends the functional calculus for normal operators. This functional calculus or, equivalently, the Spectral Theorem, will be exploited in this chapter. But right now we look at some examples.



<a id="pdf-page-280"></a>
**2.5. Example.** If $\mu$ is a regular Borel measure on $\mathbb C$ with compact support $K$, define $N_\mu$ on $L^2(\mu)$ by $N_\mu f=zf$ for each $f$ in $L^2(\mu)$. It is easy to check that $N_\mu^*f=\bar zf$, and, hence, $N_\mu$ is normal.

(a) $\sigma(N_\mu)=K=\operatorname{support}$ of $\mu$. (Exercise.)

(b) If, for a bounded Borel function $\phi$, we define $M_\phi$ on $L^2(\mu)$ by $M_\phi f=\phi f$, then $\phi(N_\mu)=M_\phi$.

Indeed, this is an easy application of the uniqueness part of (2.3).

(c) If $E$ is the spectral measure for $N_\mu$, then $E(\Delta)=M_{\chi_\Delta}$.

Just note that $E(\Delta)=\chi_\Delta(N_\mu)$.

**2.6. Example.** Let $(X,\Omega,\mu)$ be any $\sigma$-finite measure space and put $\mathcal H=L^2(X,\Omega,\mu)$. For $\phi$ in $L^\infty(\mu)\equiv L^\infty(X,\Omega,\mu)$, define $M_\phi$ on $\mathcal H$ by $M_\phi f=\phi f$.

(a) $M_\phi$ is normal and $M_\phi^*=M_{\bar\phi}$ (II.2.8).

(b) $\phi\mapsto M_\phi$ is a representation of $L^\infty(\mu)$ (VIII.5.4).

(c) If $\phi\in L^\infty(\mu)$, $\|\phi\|_\infty=\|M_\phi\|$ (II.1.5).

(d) Define the *essential range* of $\phi$ by
$$
\operatorname{ess-ran}(\phi)\equiv
\bigcap\{\operatorname{cl}(\phi(\Delta)):\Delta\in\Omega
\text{ and }\mu(X\setminus\Delta)=0\}.
$$

Then $\sigma(M_\phi)=\operatorname{ess-ran}(\phi)$. (This appears as Exercise VII.3.3, but a proof is given here.)

First assume that $\lambda\notin\operatorname{ess-ran}(\phi)$. So there is a set $\Delta$ in $\Omega$ with $\mu(X\setminus\Delta)=0$ and $\lambda$ not in $\operatorname{cl}(\phi(\Delta))$; thus there is a $\delta>0$ with $|\phi(x)-\lambda|\geq\delta$ for all $x$ in $\Delta$. If $\psi=(\phi-\lambda)^{-1}$, $\psi\in L^\infty(\mu)$ and $M_\psi=(M_\phi-\lambda)^{-1}$.

Conversely, assume $\lambda\in\operatorname{ess-ran}(\phi)$. It follows that for every integer $n$ there is a set $\Delta_n$ in $\Omega$ such that $0<\mu(\Delta_n)<\infty$ and $|\phi(x)-\lambda|<1/n$ for all $x$ in $\Delta_n$. Put $f_n=(\mu(\Delta_n))^{-1/2}\chi_{\Delta_n}$; so $f_n\in L^2(\mu)$ and $\|f_n\|_2=1$. However, $\|(M_\phi-\lambda)f_n\|_2^2=(\mu(\Delta_n))^{-1}\int_{\Delta_n}|\phi-\lambda|^2\,d\mu\leq 1/n^2$, showing that $\lambda\in\sigma_{ap}(M_\phi)$.

(e) If $E$ is the spectral measure for $M_\phi$ [so $E$ is defined on the Borel subsets of $\sigma(M_\phi)=\operatorname{ess-ran}(\phi)\subseteq\mathbb C$], then for every Borel subset $\Delta$ of $\sigma(M_\phi)$, $E(\Delta)=M_{\chi_{\phi^{-1}(\Delta)}}$.

**2.7. Proposition.** *If for $k\geq 1$, $N_k$ is a normal operator on $\mathcal H_k$ with $\sup_k\|N_k\|<\infty$, $E_k$ is the spectral measure for $N_k$, and if $N=\bigoplus_{k=1}^{\infty}N_k$ on $\mathcal H=\bigoplus_{k=1}^{\infty}\mathcal H_k$, then:*

(a) $\sigma(N)=\operatorname{cl}\left[\bigcup_{k=1}^{\infty}\sigma(N_k)\right]$;

(b) *if $E$ is the spectral measure for $N$, $E(\Delta)=\bigoplus_{k=1}^{\infty}E_k(\Delta\cap\sigma(N_k))$ for every Borel subset $\Delta$ of $\sigma(N)$.*

**Proof.** Exercise.

A historical account of the spectral theorem is an enormous undertaking



<a id="pdf-page-281"></a>
by itself. One such account in Steen [1973]. You might also consult the notes in Dunford and Schwartz [1963] and Halmos [1951].

## EXERCISES

Throughout these exercises, $N$ is a normal operator on $\mathcal H$ with spectral measure $E$.

1. Show that $\lambda\in\sigma_p(N)$ if and only if $E(\{\lambda\})\ne 0$. Moreover, if $\lambda\in\sigma_p(N)$, $E(\{\lambda\})$ is the orthogonal projection onto $\ker(N-\lambda)$.

2. If $\Delta$ is a clopen subset of $\sigma(N)$, show that $E(\Delta)$ is the Riesz idempotent associated with $\Delta$.

3. Prove Theorem II.5.1 and its corollaries by using the Spectral Theorem.

4. Prove Theorem II.7.6 and its corollaries by using the Spectral Theorem.

5. Obtain Theorem II.7.11 as a consequence of (2.3).

6. Verify the statements in Example 2.5.

7. Verify (2.6e).

8. Show that if $\mathcal H$ is separable, there are at most a countable number of points $\{z_n\}$ in $\sigma(N)$ such that $E(z_n)\ne 0$. By Exercise 1, these are the eigenvalues of $N$.

9. Show that a normal operator $N$ is (a) hermitian if and only if $\sigma(N)\subseteq\mathbb R$; (b) positive if and only if $\sigma(N)\subseteq[0,\infty)$; (c) unitary if and only if $\sigma(N)\subseteq\partial\mathbb D$.

10. Let $A$ be a hermitian operator with spectral measure $E$ on a separable space. For each real number $t$ define a projection $P(t)=E(-\infty,t)$. Show:

    (a) $P(s)\leq P(t)$ for $s\leq t$;

    (b) if $t_n\leq t_{n+1}$ and $t_n\to t$, $P(t_n)\to P(t)$ (SOT);

    (c) for all but a countable number of points $t$, $P(t_n)\to P(t)$ (SOT) if $t_n\to t$;

    (d) for $f$ in $C(\sigma(A))$, $f(A)=\int_{-\infty}^{\infty}f(t)\,dP(t)$, where this integral is to be defined (by the reader) in the Riemann–Stieltjes sense.

11. If $\sigma_p(N)$ is a Borel set, show that $E(\sigma(N)\backslash\sigma_p(N))=0$ if and only if $N$ is diagonalizable; that is, there is a basis for $\mathcal H$ consisting of eigenvectors for $N$. If $\sigma_p(N)$ is not assumed to be a Borel set, is it still possible to characterize diagonalizable normal operators in a similar way? Give an example of a normal operator $N$ such that $\sigma_p(N)$ is not a Borel set.

12. Show that if $N=U|N|$ ($|N|=(N^*N)^{1/2}$) is the polar decomposition of $N$, $U=\phi(N)$ for some Borel function $\phi$ on $\sigma(N)$. Hence $U|N|=|N|U$ (see Exercise VIII.3.21).

13. Show that $N=W|N|$ for some unitary $W$ that is a function of $N$.

14. Prove that if $A$ is hermitian, $\exp(iA)$ is unitary. Is the converse true?

15. Show that there is a normal operator $M$ such that $M^2=N$ and $M=\phi(N)$ for some Borel function $\phi$. How many such normal operators $M$ are there?

16. Define $N:L^2(\mathbb R)\to L^2(\mathbb R)$ by $(Nf)(t)=f(t+1)$. Show that $N$ is normal and find its spectral decomposition. ((X.6.17) is useful here.)

17. Suppose that $N_1,\ldots,N_d$ are normal operators such that $N_jN_k^*=N_k^*N_j$ for



<a id="pdf-page-282"></a>
## §2. The Spectral Theorem

267

$1\leq j,k\leq d$. Show that there is a subset $X$ of $\mathbb C^d$ and a spectral measure $E$ defined on the Borel subsets of $X$ such that $N_k=\int z_k\,dE(z)$ for $1\leq k\leq d$ ($z_k=$ the $k$th coordinate function) (see Exercise VIII.2.2).

18. If $N_1,\ldots,N_d$ are as in Exercise 17 and each is compact, show that there is a basis for $\mathcal H$ consisting of eigenvectors for each $N_k$. (This is the *simultaneous diagonalization of $N_1,\ldots,N_d$*.)

19. This exercise gives the properties of Hilbert–Schmidt operators (defined below). (a) If $\{e_i\}$ and $\{f_j\}$ are two orthonormal bases for $\mathcal H$ and $A\in\mathcal B(\mathcal H)$, then
$$
\sum_i\|Ae_i\|^2=\sum_j\|Af_j\|^2=\sum_i\sum_j|\langle Ae_i,f_j\rangle|^2.
$$

(b) If $A\in\mathcal B(\mathcal H)$ and $\{e_i\}$ is a basis for $\mathcal H$, define
$$
\|A\|_2=\left[\sum_i\|Ae_i\|^2\right]^{1/2}.
$$

By (a) $\|A\|_2$ is independent of the basis chosen and hence is well defined. If $\|A\|_2<\infty$, $A$ is called a *Hilbert–Schmidt operator*. $\mathcal B_2=\mathcal B_2(\mathcal H)$ denotes the set of all Hilbert–Schmidt operators. (c) $\|A\|\leq\|A\|_2$ for every $A$ in $\mathcal B(\mathcal H)$ and $\|\cdot\|_2$ is a norm on $\mathcal B_2$. (d) If $T\in\mathcal B=\mathcal B(\mathcal H)$ and $A\in\mathcal B_2$, then $\|TA\|_2\leq\|T\|\|A\|_2$, $\|A^*\|_2=\|A\|_2$, and $\|AT\|_2\leq\|A\|_2\|T\|$. (e) $\mathcal B_2$ is an ideal of $\mathcal B$ that contains $\mathcal B_{00}$, the finite-rank operators. (f) $A\in\mathcal B_2$ if and only if $|A|\equiv(A^*A)^{1/2}\in\mathcal B_2$; in this case $\|A\|_2=\||A|\|_2$. (g) $\mathcal B_2\subseteq\mathcal B_0$; moreover, if $A$ is a compact operator and $\lambda_1,\lambda_2,\ldots$ are the eigenvalues of $|A|$, each repeated as often as its multiplicity, then $A\in\mathcal B_2(\mathcal H)$ iff $\sum_{n=1}^{\infty}\lambda_n^2<\infty$. In this case, $\|A\|_2=(\sum\lambda_n^2)^{1/2}$. (h) If $(X,\Omega,\mu)$ is a measure space and $k\in L^2(\mu\times\mu)$, let $K:L^2(\mu)\to L^2(\mu)$ be the integral operator with kernel $k$. Then $K\in\mathcal B_2(L^2(\mu))$ and $\|K\|_2=\|k\|_2$ (see Proposition II.4.7 and Lemma II.4.8). (i) Interpret part (h) for a purely atomic measure space. More information on $\mathcal B_2$ is contained in the next exercise.

20. This exercise discusses trace-class operators (defined below) and assumes a knowledge of Exercise 19. $\mathcal B_1(\mathcal H)=\{AB:A\text{ and }B\in\mathcal B_2(\mathcal H)\}$. Operators belonging to $\mathcal B_1(\mathcal H)$ are called *trace-class operators* and $\mathcal B_1(\mathcal H)=\mathcal B_1$ is called the trace class. (a) If $A\in\mathcal B_1(\mathcal H)$ and $\{e_i\}$ is a basis, then $\sum|\langle Ae_i,e_i\rangle|<\infty$. Moreover, the sum $\sum\langle Ae_i,e_i\rangle$ is independent of the choice of basis. (Hint: If $A=C^*B$, $B,C$ in $\mathcal B_2$, show that $|\langle Ae_i,e_i\rangle|\equiv\frac12(\|Be_i\|^2+\|Ce_i\|^2)$.) (b) If $\{e_i\}$ is a basis for $\mathcal H$, define $\operatorname{tr}:\mathcal B_1\to\mathbb C$ by
$$
\operatorname{tr}(A)=\sum_i\langle Ae_i,e_i\rangle.
$$

By (a) the definition of $\operatorname{tr}(A)$ does not depend on the choice of a basis; $\operatorname{tr}(A)$ is called the *trace* of $A$. If $\dim\mathcal H<\infty$, then $\operatorname{tr}(A)$ is precisely the sum of the diagonal terms of any matrix representation of $A$. (c) If $A\in\mathcal B(\mathcal H)$, then the following are equivalent: (1) $A\in\mathcal B_1$; (2) $|A|=(A^*A)^{1/2}\in\mathcal B_1$; (3) $|A|^{1/2}\in\mathcal B_2$; (4) $\operatorname{tr}(|A|)<\infty$. (d) If $A\in\mathcal B_1$ and $T\in\mathcal B$, then $AT$ and $TA$ are in $\mathcal B_1$ and $\operatorname{tr}(AT)=\operatorname{tr}(TA)$. Moreover, $\operatorname{tr}:\mathcal B_1\to\mathbb C$ is a positive linear functional such that if $A\in\mathcal B_1$, $A\geq0$, and $\operatorname{tr}(A)=0$, then $A=0$. (e) If $A\in\mathcal B_1$, define $\|A\|_1\equiv\operatorname{tr}(|A|)$. If $A\in\mathcal B_1$ and $T\in\mathcal B$, show that $|\operatorname{tr}(TA)|\leq\|T\|\|A\|_1$. (f) $\|A\|_1=\|A^*\|_1$ if $A\in\mathcal B_1$. (g) If $T\in\mathcal B$ and $A\in\mathcal B_1$, then $\|TA\|_1\leq\|T\|\|A\|_1$ and $\|AT\|_1\leq\|T\|\|A\|_1$. (h) $\|\cdot\|_1$ is a norm on $\mathcal B_1$. It is called the *trace norm*. (i) $\mathcal B_1$ is an ideal in $\mathcal B(\mathcal H)$ that contains $\mathcal B_{00}$. (j) If $A\in\mathcal B_1$



<a id="pdf-page-283"></a>
and $\{e_i\}$ and $\{f_i\}$ are two bases for $\mathcal H$, then $\sum_i |\langle Ae_i,f_i\rangle|\leq \|A\|_1$. (d) $\mathcal B_1\subseteq\mathcal B_0$. Also, if $A\in\mathcal B_0$ and $\lambda_1,\lambda_2,\ldots$ are the eigenvalues of $|A|$, each repeated as often as its multiplicity, then $A\in\mathcal B_1$ if and only if $\sum_{n=1}^{\infty}\lambda_n<\infty$. In this case, $\|A\|_1=\sum_{n=1}^{\infty}\lambda_n$. (l) If $A$ and $B\in\mathcal B_2$, define $(A,B)=\operatorname{tr}(B^*A)$. Then $(\cdot,\cdot)$ is an inner product on $\mathcal B_2$, $\|\cdot\|_2$ is the norm defined by this inner product, and $\mathcal B_2$ is $\|\cdot\|_2$ complete. In other words, $\mathcal B_2$ is a Hilbert space. (m) $(\mathcal B_1,\|\cdot\|_1)$ is a Banach space. (n) $\mathcal B_{00}$ is dense in both $\mathcal B_1$ and $\mathcal B_2$. (For more on these matters, see Ringrose [1971] and Schatten [1960].)

21. This exercise assumes a knowledge of Exercise 20. If $g,h\in\mathcal H$, let $g\otimes h$ denote the rank-one operator defined by $(g\otimes h)(f)=\langle f,h\rangle g$. (a) If $g,h\in\mathcal H$ and $A\in\mathcal B(\mathcal H)$, $\operatorname{tr}(A(g\otimes h))=\langle Ag,h\rangle$. (b) If $T\in\mathcal B_1$, then $\|T\|_1=\sup\{|\operatorname{tr}(CT)|:C\in\mathcal B_0,\ \|C\|\leq 1\}$. (c) If $T\in\mathcal B_1$, define $L_T:\mathcal B_0\to\mathbb C$ by $L_T(C)=\operatorname{tr}(TC)\ (=\operatorname{tr}(CT))$. Show that the map $T\mapsto L_T$ is an isometric isomorphism of $\mathcal B_1$ onto $\mathcal B_0^*$. (d) If $B\in\mathcal B$, define $F_B:\mathcal B_1\to\mathbb C$ by $F_B(T)=\operatorname{tr}(BT)$. Show that $B\mapsto F_B$ is an isometric isomorphism of $\mathcal B$ onto $\mathcal B_1^*$. (e) If $L\in\mathcal B^*$ show that $L=L_0+L_1$ where $L_0,L_1\in\mathcal B^*$, $L_1(B)=\operatorname{tr}(BT)$ for some $T$ in $\mathcal B_1$, and $L_0(C)=0$ for every compact operator $C$. Show that $\|L\|=\|L_0\|+\|L_1\|$ and that $L_0$ and $L_1$ are unique. Give necessary and sufficient conditions on $\mathcal H$ for $\mathcal B(\mathcal H)$ to be a reflexive Banach space.

22. Prove that if $U$ is any unitary operator on $\mathcal H$, then there is a continuous function $u:[0,1]\to\mathcal B(\mathcal H)$ such that $u(t)$ is unitary for all $t$, $u(0)=U$, and $u(1)=1$.

23. If $N$ is normal, show that there is a sequence of invertible normal operators that converges to $N$.

## §3. Star-Cyclic Normal Operators

<!-- BEGIN BACKGROUND BG-IX.block2 -->
<a id="bg-ix-3"></a>
### Lemma BG-IX.3 — Bounded pointwise convergence becomes strong convergence

Let $E$ be a spectral measure and $\mu_h(\Delta)=\langle E(\Delta)h,h\rangle$. If bounded measurable $f_n,f$ satisfy $f_n\to f$ pointwise and $\sup_n\|f_n\|_\infty\leq M$, then $\int f_n\,dE\to\int f\,dE$ strongly. Uniform convergence implies operator-norm convergence, but bounded pointwise convergence usually does not.

**Proof.** The calculus gives
$$
\left\|\left(\int(f_n-f)\,dE\right)h\right\|^2=\int|f_n-f|^2\,d\mu_h.
$$
Since $\mu_h(X)=\|h\|^2$ and $|f_n-f|^2\leq4M^2$, dominated convergence applies. On $L^2[0,1]$, multiplication by $\chi_{(0,1/n)}$ nevertheless has norm one for every $n$ while converging strongly to zero. $\square$

This is a **sequence** theorem. For arbitrary nets bounded pointwise convergence is insufficient: direct finite subsets $F$ of $[0,1]$ by inclusion. Then $\chi_{[0,1]\setminus F}\to0$ pointwise, but all Lebesgue integrals equal one. This explains the stronger integral-convergence hypotheses on nets in this chapter.

<a id="bg-ix-4"></a>
### Lemma BG-IX.4 — Changing measure in a multiplication model

For finite positive measures with the same null sets, write $w=d\mu/d\nu$. Then $0<w<\infty$ almost everywhere for $\nu$, and $Uf=\sqrt w f$ is unitary from $L^2(\mu)$ to $L^2(\nu)$, intertwining multiplication by every bounded measurable function.

**Proof.** Radon–Nikodym gives $w\geq0$ integrable. The set $\{w=0\}$ is $\mu$-null, hence $\nu$-null. Also $\|Uf\|_{L^2(\nu)}^2=\int|f|^2w\,d\nu=\|f\|_{L^2(\mu)}^2$. Each $g\in L^2(\nu)$ has preimage $g/\sqrt w\in L^2(\mu)$. Commuting scalar factors proves intertwining. Neither $w$ nor $1/w$ needs to be bounded: the two spaces carry different measures. $\square$
<!-- END BACKGROUND BG-IX.block2 -->

Recall the definition of a reducing subspace and some of its equivalent formulations (Section II.3).

**3.1. Definition.** A vector $e_0$ in $\mathcal H$ is a *star-cyclic vector* for $A$ if $\mathcal H$ is the smallest reducing subspace for $A$ that contains $e_0$. The operator $A$ is *star cyclic* if it has a star-cyclic vector. A vector $e_0$ is *cyclic* for $A$ if $\mathcal H$ is the smallest invariant subspace for $A$ that contains $e_0$; $A$ is *cyclic* if it has a cyclic vector.

**3.2. Proposition.** (a) A vector $e_0$ is a star-cyclic vector for $A$ if and only if $\mathcal H=\operatorname{cl}\{Te_0:T\in C^*(A)\}$, where $C^*(A)=$ the $C^*$-algebra generated by $A$. (b) A vector $e_0$ is a cyclic vector for $A$ if and only if $\mathcal H=\operatorname{cl}\{p(A)e_0:p=\text{a polynomial}\}$.

**Proof.** Exercise.

Note that if $e_0$ is a star-cyclic vector for $A$, then it is a cyclic vector for the algebra $C^*(A)$.

**3.3. Proposition.** If $A$ has either a cyclic or a star-cyclic vector, then $\mathcal H$ is separable.



<a id="pdf-page-284"></a>
**Proof.** It is easy to see that $C^*(A)$ and $\{p(A):p=\text{a polynomial}\}$ are separable subalgebras of $\mathcal{B}(\mathcal{H})$. Now use (3.2). ■

Let $\mu$ be a compactly supported measure on $\mathbb{C}$ and let $N_\mu$ be defined on $L^2(\mu)$ as in Example 2.5. If $K=\operatorname{support}\mu$, then $C^*(N_\mu)=\{M_u:u\in C(K)\}$. Since $C(K)$ is dense in $L^2(\mu)$, it follows that $1$ is a star-cyclic vector for $N_\mu$. The converse of this is also true.

**3.4. Theorem.** *A normal operator $N$ is star-cyclic if and only if $N$ is unitarily equivalent to $N_\mu$ for some compactly supported measure $\mu$ on $\mathbb{C}$. If $e_0$ is a star-cyclic vector for $N$, then $\mu$ can be chosen such that there is an isomorphism $V:\mathcal{H}\to L^2(\mu)$ with $Ve_0=1$ and $VNV^{-1}=N_\mu$. Under these conditions, $V$ is unique.*

**Proof.** If $N\cong N_\mu$, then we have already seen that $N$ is star-cyclic. So suppose that $N$ has a star-cyclic vector $e_0$. If $E$ is the spectral measure for $N$, put $\mu(\Delta)=\|E(\Delta)e_0\|^2=\langle E(\Delta)e_0,e_0\rangle$ for every Borel subset $\Delta$ of $\mathbb{C}$ (see Lemma 1.9). Let $K=\operatorname{support}\mu$.

If $\phi\in B(K)$, then (2.4) implies

$$
\begin{aligned}
\|\phi(N)e_0\|^2
&=\langle\phi(N)e_0,\phi(N)e_0\rangle\\
&=\langle|\phi|^2(N)e_0,e_0\rangle\\
&=\int|\phi(z)|^2\,d\langle E(z)e_0,e_0\rangle\\
&=\int|\phi|^2\,d\mu.
\end{aligned}
$$

So if $B(K)$ is considered as a submanifold of $L^2(\mu)$, $U\phi=\phi(N)e_0$ defines an isometry from $B(K)$ onto $\{\phi(N)e_0:\phi\in B(K)\}$. But $e_0$ is a star-cyclic vector, so the range of $U$ is dense in $\mathcal{H}$. Hence $U$ extends to an isomorphism $U:L^2(\mu)\to\mathcal{H}$.

If $\phi\in B(K)$, then $UN_\mu U^{-1}(\phi(N)e_0)=UN_\mu(\phi)=U(z\phi)=N\phi(N)e_0$. Hence $UN_\mu U^{-1}=N$ on $\{\phi(N)e_0:\phi\in B(K)\}$, which is dense in $\mathcal{H}$. So $UN_\mu U^{-1}=N$. Let $V=U^{-1}$.

The proof of the uniqueness statement is an exercise. ■

Any theorem about the operators $N_\mu$ is a theorem about star-cyclic normal operators. With this in mind, the next theorem gives a complete unitary invariant for star-cyclic normal operators. But first, a definition.

**3.5. Definition.** Two measures, $\mu_1$ and $\mu_2$, are *mutually absolutely continuous* if they have the same sets of measure zero; that is, $\mu_1(\Delta)=0$ if and only if $\mu_2(\Delta)=0$. This will be denoted by $[\mu_1]=[\mu_2]$. (The more standard notation in the literature is $\mu_1\equiv\mu_2$, but this seems insufficient.) If $[\mu_1]=[\mu_2]$, then the Radon–Nikodym derivatives $d\mu_1/d\mu_2$ and $d\mu_2/d\mu_1$ are well defined. Say



<a id="pdf-page-285"></a>
that $\mu_1$ and $\mu_2$ are *boundedly mutually absolutely continuous* if $[\mu_1]=[\mu_2]$ and the Radon–Nikodym derivatives are essentially bounded functions.

**3.6. Theorem.** $N_{\mu_1}\cong N_{\mu_2}$ if and only if $[\mu_1]=[\mu_2]$.

**Proof.** Suppose $[\mu_1]=[\mu_2]$ and put $\phi=d\mu_1/d\mu_2$. So if $g\in L^1(\mu_1)$, $g\phi\in L^1(\mu_2)$ and $\int g\phi\,d\mu_2=\int g\,d\mu_1$. Hence, if $f\in L^2(\mu_1)$, $\sqrt{\phi}f\in L^2(\mu_2)$ and $\|\sqrt{\phi}f\|_2=\|f\|_2$; that is, $U:L^2(\mu_1)\to L^2(\mu_2)$ defined by $Uf=\sqrt{\phi}f$ is an isometry. If $g\in L^2(\mu_2)$, then $f=\phi^{-1/2}g\in L^2(\mu_1)$ and $Uf=g$; hence $U$ is surjective and $U^{-1}g=\phi^{-1/2}g$ for $g$ in $L^2(\mu_2)$. If $g\in L^2(\mu_2)$, then $UN_{\mu_1}U^{-1}g=UN_{\mu_1}\phi^{-1/2}g=Uz\phi^{-1/2}g=zg$, and so $UN_{\mu_1}U^{-1}=N_{\mu_2}$.

Now assume that $V:L^2(\mu_1)\to L^2(\mu_2)$ is an isomorphism such that $VN_{\mu_1}V^{-1}=N_{\mu_2}$. Put $\psi=V(1)$; so $\psi\in L^2(\mu_2)$. For convenience, put $N_j=N_{\mu_j}$, $j=1,2$. It is easy to see that $VN_1^kV^{-1}=N_2^k$ and $VN_1^{*k}V^{-1}=N_2^{*k}$. Hence $Vp(N_1,N_1^*)V^{-1}=p(N_2,N_2^*)$ for any polynomial $p$ in $z$ and $\bar z$. Since $N_1\cong N_2$, $\sigma(N_1)=\sigma(N_2)$; hence support $\mu_1=\operatorname{support}\mu_2=K$. By taking uniform limits of polynomials in $z$ and $\bar z$, $Vu(N_1)V^{-1}=u(N_2)$ for $u$ in $C(K)$. Hence for $u$ in $C(K)$, $V(u)=Vu(N_1)1=u(N_2)V1=u\psi$. Because $V$ is an isometry, this implies that $\int |u|^2\,d\mu_1=\int |u|^2|\psi|^2\,d\mu_2$ for every $u$ in $C(K)$. Hence $\int v\,d\mu_1=\int v|\psi|^2\,d\mu_2$ for $v$ in $C(K)$, $v\geq 0$. By the uniqueness part of the Riesz Representation Theorem, $\mu_1=|\psi|^2\mu_2$, so $\mu_1\ll\mu_2$.

By using $V^{-1}$ instead of $V$ and reversing the roles of $N_1$ and $N_2$ in the preceding argument, it follows that $\mu_2\ll\mu_1$. Hence $[\mu_1]=[\mu_2]$. $\blacksquare$

## Exercises

1. If $\mu$ is a compactly supported measure on $\mathbb C$ and $f\in L^2(\mu)$, $f$ is a star-cyclic vector for $N_\mu$ if and only if $\mu(\{x:f(x)=0\})=0$.

2. Prove Proposition 3.2.

3. If $\mu_1$ and $\mu_2$ are compactly supported measures on $\mathbb C$, show that the following statements are equivalent: (a) $\mu_1$ and $\mu_2$ are boundedly mutually absolutely continuous; (b) there is an isomorphism $V:L^2(\mu_1)\to L^2(\mu_2)$ such that $VN_{\mu_1}V^{-1}=N_{\mu_2}$ and $VL^\infty(\mu_1)=L^\infty(\mu_2)$; (c) there is a bounded bijection $R:L^2(\mu_1)\to L^2(\mu_2)$ such that $Rp(z,\bar z)=p(z,\bar z)$ for every polynomial in $z$ and $\bar z$.

4. Show that if $N$ is a star-cyclic normal operator and $\lambda\in\sigma_p(N)$, then $\dim\ker(N-\lambda)=1$.

5. If $N$ is diagonalizable and star-cyclic and if $\sigma_p(N)=\{\lambda_1,\lambda_2,\ldots\}$, show that $N$ is unitarily equivalent to $N_\mu$, where $\mu=\sum_{n=1}^{\infty}2^{-n}\delta_{\lambda_n}$ (see Exercise 2.11).

6. Let $N$ be a diagonalizable normal operator. Show that $N\cong M$ if and only if $M$ is a diagonalizable normal operator, $\sigma_p(N)=\sigma_p(M)$, and $\dim\ker(N-\lambda)=\dim\ker(M-\lambda)$ for all $\lambda$. (Compare this with Theorem II.8.3.)

7. Let $U$ be the bilateral shift on $l^2(\mathbb Z)$. If $e_0$ is the vector in $l^2(\mathbb Z)$ that has 1 in the zeroth place and zeros elsewhere, then $e_0$ is a star-cyclic vector for $U$. If $\mu$ is the compactly supported measure on $\mathbb C$ and $V:l^2(\mathbb Z)\to L^2(\mu)$ is the isomorphism such that $Ve_0=1$ and $VUV^{-1}=N_\mu$, then



   <a id="pdf-page-286"></a>
   (a) $\mu=m=$ normalized arc length on $\partial\mathbb D$;

   (b) $V^{-1}=$ the Fourier transform on $L^2(m)=L^2(\partial\mathbb D)$.

8. Suppose $N_1,\ldots,N_d$ are normal operators such that $N_jN_k^*=N_k^*N_j$ for $1\leq j,k\leq d$ and suppose there is a vector $e_0$ in $\mathcal H$ such that $\mathcal H$ is the only subspace of $\mathcal H$ containing $e_0$ that reduces each of the operators $N_1,\ldots,N_d$. Show that there is a compactly supported measure $\mu$ on $\mathbb C^d$ and an isomorphism $V:\mathcal H\to L^2(\mu)$ such that $VN_kV^{-1}f=z_kf$ for $f$ in $L^2(\mu)$ and $1\leq k\leq d$ ($z_k=$ the $k$th coordinate function) (see Exercise 2.17).

## §4. Some Applications of the Spectral Theorem

In this section a few diverse applications of the Spectral Theorem are presented. These will show the power and finesse of the Spectral Theorem as well as demonstrate some of the methods used to apply it. One result in this section (Theorem 4.6) is more than an application. Indeed, many regard this as the optimal statement of the Spectral Theorem.

If $N$ is a normal operator and $N=\int z\,dE(z)$ is its spectral representation, then $\phi\mapsto\phi(N)\equiv\int\phi\,dE$ is a $*$-homomorphism of $B(\mathbb C)$ into $\mathcal B(\mathcal H)$. Thus, if $\phi,\psi\in B(\mathbb C)$, $(\int\phi\,dE)(\int\psi\,dE)=\int\phi\psi\,dE$ and $\|\int\phi\,dE\|\leq\sup\{|\phi(z)|:z\in\sigma(N)\}$.

**4.1. Proposition.** *If $N$ is a normal operator and $N=\int z\,dE(z)$, then $N$ is compact if and only if for every $\varepsilon>0$, $E(\{z:|z|>\varepsilon\})$ has finite rank.*

**Proof.** If $\varepsilon>0$, let $\Delta_\varepsilon=\{z:|z|>\varepsilon\}$ and $E_\varepsilon=E(\Delta_\varepsilon)$. Then

$$
\begin{aligned}
N-NE_\varepsilon
&=\int z\,dE(z)-\int z\chi_{\Delta_\varepsilon}(z)\,dE(z)\\
&=\int z\chi_{\mathbb C\setminus\Delta_\varepsilon}(z)\,dE(z)=\phi(N)
\end{aligned}
$$

where $\phi(z)=z\chi_{\mathbb C\setminus\Delta_\varepsilon}(z)$. Thus $\|N-NE_\varepsilon\|\leq\sup\{|z|:z\in\mathbb C\setminus\Delta_\varepsilon\}\leq\varepsilon$. If $E_\varepsilon$ has finite rank for every $\varepsilon>0$, then so does $NE_\varepsilon$. Thus $N\in\mathcal B_0(\mathcal H)$.

Now assume that $N$ is compact and let $\varepsilon>0$. Put $\phi(z)=z^{-1}\chi_{\Delta_\varepsilon}(z)$; so $\phi\in B(\mathbb C)$. Since $N$ is compact, so is $N\phi(N)$. But $N\phi(N)=\int zz^{-1}\chi_{\Delta_\varepsilon}(z)\,dE(z)=E_\varepsilon$. Since $E_\varepsilon$ is a compact projection, it must have finite rank. (Why?) $\blacksquare$

The preceding result could have been proved by using the fact that compact normal operators are diagonalizable and the eigenvalues must converge to 0.

**4.2. Theorem.** *If $\mathcal H$ is separable and $I$ is an ideal of $\mathcal B(\mathcal H)$ that contains a noncompact operator, then $I=\mathcal B(\mathcal H)$.*

**Proof.** If $A\in I$ and $A\notin\mathcal B_0(\mathcal H)$, consider $A^*A$; let $A^*A=\int t\,dE(t)$ ($\sigma(A^*A)\subseteq[0,\infty)$). By the preceding proposition, there is an $\varepsilon>0$ such that



<a id="pdf-page-287"></a>
$P=E(\varepsilon,\infty)$ has infinite rank. But $P=\left(\int t^{-1}\chi_{(\varepsilon,\infty)}(t)\,dE(t)\right)A^*A\in I$. Since $\mathcal H$ is separable, $\dim P\mathcal H=\dim\mathcal H=\aleph_0$. Let $U:\mathcal H\to P\mathcal H$ be a surjective isometry. It is easy to check that $1=U^*PU$. But $P\in I$, so $1\in I$. Hence $I=\mathcal B(\mathcal H)$. ■

In Proposition VIII.4.10, it was shown that every nonzero ideal of $\mathcal B(\mathcal H)$ contains the finite-rank operators. When combined with the preceding result, this yields the following.

**4.3. Corollary.** *If $\mathcal H$ is separable, then the only nontrivial closed ideal of $\mathcal B(\mathcal H)$ is the ideal of compact operators.*

The next proposition is related to Theorem VIII.5.9. Indeed, it is a consequence of it so that the proof will only be sketched.

Let $N$ be a normal operator on $\mathcal H$ and for every vector $e$ in $\mathcal H$ let $\mathcal H_e\equiv\bigvee\{N^{*k}N^je:k,j\geq 0\}$. So $\mathcal H_e$ is the smallest subspace of $\mathcal H$ that contains $e$ and reduces $N$. Also, $N|\mathcal H_e$ is a star-cyclic normal operator.

**4.4. Proposition.** *If $N$ is a normal operator on $\mathcal H$, then there are reducing subspaces $\{\mathcal H_i:i\in I\}$ for $N$ such that $\mathcal H=\bigoplus_i\mathcal H_i$ and $N|\mathcal H_i$ is star cyclic.*

**Proof.** Using Zorn’s Lemma find a maximal set of vectors $\mathcal E$ in $\mathcal H$ such that if $e,f\in\mathcal E$ and $e\ne f$, then $\mathcal H_e\perp\mathcal H_f$. It follows that $\mathcal H=\bigoplus_e\mathcal H_e$. ■

**4.5. Corollary.** *Every normal operator is unitarily equivalent to the direct sum of star-cyclic normal operators.*

By combining the preceding proposition with Theorem 3.4 on the representation of star-cyclic normal operators we can obtain the following theorem.

**4.6. Theorem.** *If $N$ is a normal operator on $\mathcal H$, then there is a measure space $(X,\Omega,\mu)$ and a function $\phi$ in $L^\infty(X,\Omega,\mu)$ such that $N$ is unitarily equivalent to $M_\phi$ on $L^2(X,\Omega,\mu)$.*

**Proof.** If $\mathcal M$ is a reducing subspace for $N$, then $N\cong N|\mathcal M\oplus N|\mathcal M^\perp$; thus $\sigma(N|\mathcal M)\subseteq\sigma(N)$. So if $\{N_i\}$ is a collection of star-cyclic normal operators such that $N\cong\bigoplus_iN_i$ (4.5), then $\sigma(N_i)\subseteq\sigma(N)$ for every $N_i$. By Theorem 3.4 there is a measure $\mu_i$ supported on $\sigma(N)$ such that $N_i\cong N_{\mu_i}$. Let $X_i=$ the support of $\mu_i$ and let $\Omega_i=$ the Borel subsets of $X_i$. Let $X=$ the disjoint union of $\{X_i\}$. Define $\Omega$ to be the collection of all subsets $\Delta$ of $X$ such that $\Delta\cap X_i\in\Omega_i$ for all $i$. It is easy to check that $\Omega$ is a $\sigma$-algebra. If $\Delta\in\Omega$ let $\mu(\Delta)\equiv\sum_i\mu_i(\Delta\cap X_i)$; then $(X,\Omega,\mu)$ is a measure space. If $f\in L^2(X,\Omega,\mu)$ then $f_i=f|X_i\in L^2(\mu_i)$. Moreover, the map $U:L^2(\mu)\to\bigoplus_iL^2(\mu_i)$ defined by $Uf=\bigoplus_i(f|X_i)$ is easily seen to be an isomorphism. Define $\phi:X\to\mathbb C$ by letting $\phi(z)=z$ if $z\in X_i$ ($\subseteq\mathbb C$); since $X_i\subseteq\sigma(N)$ for every $i$, $\phi$ is a bounded function. If $G$ is an open subset of $\mathbb C$,



<a id="pdf-page-288"></a>
$\phi^{-1}(G)\cap X_i=G\cap X_i\in\Omega_i$; hence $\phi$ is $\Omega$-measurable. Therefore $\phi\in L^\infty(X,\Omega,\mu)$. It is left to the reader to check that $UM_\phi U^{-1}=\bigoplus_i N_{\mu_i}\cong N$. $\blacksquare$

**4.7. Proposition.** *If $\mathcal H$ is separable, then the measure space in Theorem 4.6 is $\sigma$-finite.*

**Proof.** First note that the measure space $(X,\Omega,\mu)$ constructed in the preceding theorem has no infinite atoms. Now let $\mathcal E$ be a collection of pairwise disjoint sets from $\Omega$ having non-zero finite measure. A computation shows that $\{(\mu(\Delta))^{-1/2}\chi_\Delta:\Delta\in\mathcal E\}$ are pairwise orthogonal vectors in $L^2(\mu)$. If $L^2(\mu)$ is separable, then $\mathcal E$ must be countable. Therefore $(X,\Omega,\mu)$ is $\sigma$-finite. $\blacksquare$

Of course if $(X,\Omega,\mu)$ is finite it is not necessarily true that $L^2(\mu)$ is separable.

The next result will be useful later in this book and it also provides a different type of application of the Spectral Theorem.

**4.8. Proposition.** *If $\mathcal A$ is an SOT closed $C^*$-subalgebra of $\mathcal B(\mathcal H)$, then $\mathcal A$ is the norm closed linear span of the projections in $\mathcal A$.*

**Proof.** If $A\in\mathcal A$, $A+A^*$ and $A-A^*\in\mathcal A$; hence $\mathcal A$ is the linear span of $\operatorname{Re}\mathcal A$. Suppose $A\in\operatorname{Re}\mathcal A$ and $A=\int t\,dE(t)$. If $[a,b]\subseteq\mathbb R$, then there is a sequence $\{u_n\}$ in $C(\mathbb R)$ such that $0\leq u_n\leq1$, $u_n(t)=1$ for $a\leq t\leq b-n^{-1}$, $u_n(t)=0$ for $t\leq a-n^{-1}$ and $t\geq b$. Hence $u_n(t)\to\chi_{[a,b)}(t)$ as $n\to\infty$. If $h\in\mathcal H$, then

$$
\|\{u_n(A)-E[a,b)\}h\|^2
=\int |u_n(t)-\chi_{[a,b)}(t)|^2\,dE_{h,h}(t)\to0
$$

by the Lebesgue Dominated Convergence Theorem. That is, $u_n(A)\to E[a,b)$ (SOT). Since $\mathcal A$ is SOT-closed, $E[a,b)\in\mathcal A$. Now let $(\alpha,\beta)$ be an open interval containing $\sigma(A)$. If $\varepsilon>0$, then there is a partition $\{\alpha=t_0<\cdots<t_n=\beta\}$ such that $\left|t-\sum_{k=1}^n t_k\chi_{[t_{k-1},t_k)}(t)\right|<\varepsilon$ for $t$ in $\sigma(A)$; hence $\left\|A-\sum_{k=1}^n t_kE[t_{k-1},t_k)\right\|<\varepsilon$. Thus every self-adjoint operator in $\mathcal A$ belongs to the closed linear span of the projections in $\mathcal A$. $\blacksquare$

## Exercises

1. If $N$ is a normal operator show that $\operatorname{ran}N$ is closed if and only if $0$ is not a limit point of $\sigma(N)$.

2. Give an example of a non-normal operator $A$ such that $0$ is an isolated point of $\sigma(A)$ and $\operatorname{ran}A$ is closed. Give an example of a non-normal operator $B$ such that $\operatorname{ran}B$ is closed and $0$ is not an isolated point of $\sigma(B)$.

3. If $\mathcal H$ is a nonseparable Hilbert space find an example of a nontrivial closed ideal of $\mathcal B(\mathcal H)$ that is different from $\mathcal B_0(\mathcal H)$.

4. Let $(X,\Omega,\mu)$ be the measure space obtained in the proof of Theorem 4.6 and show that $L^1(X,\Omega,\mu)^*$ is isometrically isomorphic to $L^\infty(X,\Omega,\mu)$.

5. Show that $\mathcal H$ is separable if and only if every collection of pairwise orthogonal projections in $\mathcal B(\mathcal H)$ is countable.



   <a id="pdf-page-289"></a>
6. If $(X,\Omega,\mu)$ is a measure space, then $(X,\Omega,\mu)$ is $\sigma$-finite or $L^2(\mu)$ is finite dimensional if and only if every collection of pairwise orthogonal projections in $\{M_\phi\in L^\infty(\mu)\}$ is countable.

7. If $N=\int z\,dE(z)$ and $\varepsilon>0$, show that $\operatorname{ran}E(\{z:|z|>\varepsilon\})\subseteq\operatorname{ran}N$.

8. (Calkin [1939]) Let $\mathcal M$ be a linear manifold in $\mathcal H$ and show that $\mathcal M$ has the property that $\mathcal M$ contains no closed infinite dimensional subspaces if and only if whenever $A\in\mathcal B(\mathcal H)$ and $\operatorname{ran}A\subseteq\mathcal M$, then $A$ is compact.

9. Show that the extreme points of $\{A\in\mathcal B(\mathcal H):0\leq A\leq 1\}$ are the projections.

10. (Halmos [1972]) If $N$ is a normal operator, show that there is a hermitian operator $A$ and a continuous function $f$ such that $N=f(A)$. (Hint: Use Theorem 4.6.)

## §5. Topologies on $\mathcal B(\mathcal H)$

<!-- BEGIN BACKGROUND BG-IX.block3 -->
<a id="bg-ix-5"></a>
### Lemma BG-IX.5 — Passing operator identities to limits

If $A_i\to A$ strongly and $B$ is fixed and bounded, then $BA_i\to BA$ and $A_iB\to AB$ strongly. The analogous assertions hold weakly. If $A_i\to A$, $B_i\to B$ strongly and $\sup_i\|A_i\|<\infty$, then $A_iB_i\to AB$ strongly.

**Proof.** Use $\|B(A_i-A)h\|\leq\|B\|\|(A_i-A)h\|$ and replace $h$ by $Bh$ for right multiplication. Weak convergence follows from $\langle BA_ih,k\rangle=\langle A_ih,B^*k\rangle$. For moving products,
$$
\|(A_iB_i-AB)h\|\leq\|A_i\|\|(B_i-B)h\|+\|(A_i-A)Bh\|.
$$
In particular commutants are strongly and weakly closed. The uniform bound is automatic for strongly convergent sequences by uniform boundedness; this argument does not justify omitting it for arbitrary nets. $\square$
<!-- END BACKGROUND BG-IX.block3 -->

In this section some results on the SOT and WOT on $\mathcal B(\mathcal H)$ are presented. These results are necessary for understanding some of the results that are to follow in later sections and also for a proper comprehension of a number of other subjects in mathematics.

The first result appeared as Exercise 1.4.

**5.1. Proposition.** If $L:\mathcal B(\mathcal H)\to\mathbb C$ is a linear functional, then the following statements are equivalent.

(a) $L$ is SOT continuous.

(b) $L$ is WOT continuous.

(c) There are vectors $g_1,\ldots,g_n,h_1,\ldots,h_n$ in $\mathcal H$ such that $L(A)=\sum_{k=1}^n\langle Ag_k,h_k\rangle$ for every $A$ in $\mathcal B(\mathcal H)$.

**Proof.** Clearly (c) implies (b) and (b) implies (a). So assume (a). By (IV.3.1f) there are vectors $g_1,\ldots,g_n$ in $\mathcal H$ such that

$$
|L(A)|\leq\sum_{k=1}^n\|Ag_k\|\leq\sqrt n\left[\sum_{k=1}^n\|Ag_k\|^2\right]^{1/2}
$$

for every $A$ in $\mathcal B(\mathcal H)$. Replacing $g_k$ by $\sqrt n\,g_k$, it may be assumed that

$$
|L(A)|\leq\left[\sum_{k=1}^n\|Ag_k\|^2\right]^{1/2}\equiv p(A).
$$

Now $p$ is a seminorm and $p(A)=0$ implies $L(A)=0$. Let $\mathcal K=\operatorname{cl}\{Ag_1\oplus Ag_2\oplus\cdots\oplus Ag_n:A\in\mathcal B(\mathcal H)\}$; so $\mathcal K\subseteq\mathcal H\oplus\cdots\oplus\mathcal H$ ($n$ times). Note that if $Ag_1\oplus\cdots\oplus Ag_n=0$, $p(A)=0$, and hence, $L(A)=0$. Thus $F(Ag_1\oplus\cdots\oplus Ag_n)=L(A)$ is a well-defined linear functional on a dense manifold in $\mathcal K$. But

$$
|F(Ag_1\oplus\cdots\oplus Ag_n)|\leq p(A)=\|Ag_1\oplus\cdots\oplus Ag_n\|.
$$



<a id="pdf-page-290"></a>
So $F$ can be extended to a bounded linear functional $F_1$ on $\mathcal H^{(n)}$. Hence there are vectors $h_1,\ldots,h_n$ in $\mathcal H$ such that

$$
\begin{aligned}
F_1(f_1\oplus\cdots\oplus f_n)
&=\langle f_1\oplus\cdots\oplus f_n,\,
h_1\oplus\cdots\oplus h_n\rangle\\
&=\sum_{k=1}^{n}\langle f_k,h_k\rangle.
\end{aligned}
$$

In particular, $L(A)=F(Ag_1\oplus\cdots\oplus Ag_n)=\sum_{k=1}^{n}\langle Ag_k,h_k\rangle$. $\blacksquare$

**5.2. Corollary.** *If $\mathcal C$ is a convex subset of $\mathcal B(\mathcal H)$, the WOT closure of $\mathcal C$ equals the SOT closure of $\mathcal C$.*

**Proof.** Combine the preceding proposition with Corollary V.1.4. $\blacksquare$

When discussing the closure (WOT or SOT) of a convex set it is usually better to discuss the SOT. Shortly an “algebraic” characterization of the SOT closure of a subalgebra of $\mathcal B(\mathcal H)$ will be given. But first recall (VIII.5.3) that if $1\leq n\leq\infty$, $\mathcal H^{(n)}$ denotes the direct sum of $\mathcal H$ with itself $n$ times ($\aleph_0$ times if $n=\infty$). If $A\in\mathcal B(\mathcal H)$, $A^{(n)}$ is the operator on $\mathcal H^{(n)}$ defined by $A^{(n)}(h_1,\ldots,h_n)=(Ah_1,\ldots,Ah_n)$. If $\mathcal S\subset\mathcal B(\mathcal H)$, $\mathcal S^{(n)}\equiv\{A^{(n)}:A\in\mathcal S\}$. It is rather interesting that the SOT closure of an algebra can be characterized using its lattice of invariant subspaces.

**5.3. Proposition.** *If $\mathcal A$ is a subalgebra of $\mathcal B(\mathcal H)$ containing $1$, then the SOT closure of $\mathcal A$ is*

$$
\tag{5.4}
\{B\in\mathcal B(\mathcal H):\text{for every finite }n,\ 
\operatorname{Lat}\mathcal A^{(n)}\subseteq\operatorname{Lat}B^{(n)}\}.
$$

**Proof.** It is left as an exercise for the reader to show that if $B\in\operatorname{SOT-cl}\mathcal A$, $B$ belongs to the set (5.4). Now assume that $B$ belongs to the set (5.4). Fix $f_1,f_2,\ldots,f_n$ in $\mathcal H$ and $\varepsilon>0$. It must be shown that there is an $A$ in $\mathcal A$ such that $\|(A-B)f_k\|<\varepsilon$ for $1\leq k\leq n$.

Let $\mathcal M=\bigvee\{(Af_1,\ldots,Af_n):A\in\mathcal A\}$. Because $\mathcal A$ is an algebra, $\mathcal M\in\operatorname{Lat}\mathcal A^{(n)}$, hence $\mathcal M\in\operatorname{Lat}B^{(n)}$. Because $1\in\mathcal A$, $(f_1,\ldots,f_n)\in\mathcal M$. Since $\{(Af_1,\ldots,Af_n):A\in\mathcal A\}$ is a dense manifold and $(Bf_1,\ldots,Bf_n)\in\mathcal M$, there is an $A$ in $\mathcal A$ with $\varepsilon^2>\sum_{k=1}^{n}\|(A-B)f_k\|^2$; hence $B\in\operatorname{SOT-cl}\mathcal A$. $\blacksquare$

**5.5. Proposition.** *The closed unit ball of $\mathcal B(\mathcal H)$ is WOT compact.*

**Proof.** The proof of this proposition follows along the lines of the proof of Alaoglu’s Theorem. For each $h$ in $\operatorname{ball}\mathcal H$ let $X_h=$ a copy of $\operatorname{ball}\mathcal H$ with the weak topology. Put $X=\prod\{X_h:\|h\|\leq1\}$. If $A\in\operatorname{ball}\mathcal B(\mathcal H)$ let $\tau(A)\in X$ defined by $\tau(A)_h=Ah$. Give $X$ the product topology. Then $\tau:(\operatorname{ball}\mathcal B(\mathcal H),\mathrm{WOT})\to X$ is a continuous function and a homeomorphism onto its image (verify). Now show that $\tau(\operatorname{ball}\mathcal B(\mathcal H))$ is closed in $X$. From here it follows that $\operatorname{ball}\mathcal B(\mathcal H)$ is WOT compact. $\blacksquare$

## Exercises

1. Show that if $B\in\operatorname{SOT-cl}\mathcal A$, then $B$ belongs to the set defined in (5.4).



   <a id="pdf-page-291"></a>
2. Show that $\mathcal{B}_{00}$ is SOT dense in $\mathcal{B}$.

3. If $\{A_k\}$ and $\{B_k\}$ are sequences in $\mathcal{B}(\mathcal{H})$ such that $A_k\to A$ (WOT) and $B_k\to B$ (SOT), then $A_kB_k\to AB$ (WOT).

4. With the notation of Exercise 3, show that if $A_k\to A$ (SOT), then $A_kB_k\to AB$ (SOT).

5. Let $S$ be the unilateral shift on $l^2(\mathbb{N})$ (II.2.10). Examine the sequences $\{S^k\}$ and $\{S^{*k}\}$ and their relation to Exercises 3 and 4.

6. (Halmos.) Fix an orthonormal basis $\{e_n:n\geqslant 1\}$ for $\mathcal{H}$. (a) Show that $0\in$ weak closure of $\{\sqrt{n}e_n:n\geqslant 1\}$ (Halmos [1982], Solution 28). (b) Let $\{n_i\}$ be a net of integers such that $\sqrt{n_i}e_{n_i}\to 0$ weakly. Define $A_if=\sqrt{n_i}\langle f,e_{n_i}\rangle e_{n_i}$ for $f$ in $\mathcal{H}$. Show that $A_i\to 0$ (SOT) but $\{A_i^2\}$ does not converge to $0$ (SOT).

## §6. Commuting Operators

<!-- BEGIN BACKGROUND BG-IX.block4 -->
<a id="bg-ix-6"></a>
### Lemma BG-IX.6 — Why Liouville's theorem applies to operator functions

If $F:\mathbb C\to\mathcal B(\mathcal K,\mathcal H)$ is norm-holomorphic and bounded, it is constant. In particular this applies to products of operator exponentials.

**Proof.** Each scalar function $z\mapsto\langle F(z)h,k\rangle$ is entire and bounded by $\sup_z\|F(z)\|\|h\|\|k\|$. The scalar Liouville theorem, proved in the [complex-analysis primer](background-complex-analysis.md), makes it constant. Thus $\langle(F(z)-F(0))h,k\rangle=0$ for every $h,k$, which implies $F(z)=F(0)$. For fixed bounded $T$, $e^{zT}=\sum_{n\geq0}z^nT^n/n!$ and its derivative series converge uniformly in norm on bounded disks, by comparison with scalar exponential series. Termwise differentiation gives $(e^{zT})'=Te^{zT}$. The product rule is valid by continuity of bounded-operator multiplication. $\square$

In the Fuglede–Putnam proof, the formula containing $\bar z$ is used only to estimate the norm. Holomorphicity comes from the other formula, involving $z$ and fixed operators only.
<!-- END BACKGROUND BG-IX.block4 -->

If $\mathcal{S}\subseteq\mathcal{B}(\mathcal{H})$, let $\mathcal{S}'\equiv\{A\in\mathcal{B}(\mathcal{H}):AS=SA\text{ for every }S\text{ in }\mathcal{S}\}$. $\mathcal{S}'$ is called the *commutant* of $\mathcal{S}$. It is not difficult to see that $\mathcal{S}'$ is always an algebra. Similarly, $\mathcal{S}''\equiv(\mathcal{S}')'$ is called the *double commutant* of $\mathcal{S}$. This process can continue, but (happily) $\mathcal{S}'''=\mathcal{S}'$ (Exercise 1). In some circumstances, $\mathcal{S}=\mathcal{S}''$.

The problem of determining the commutant or double commutant of a single operator or a collection of operators leads to some exciting and interesting mathematics. The commutant is an algebraic object and the idea is to bring the force of analysis to bear in the characterization of this algebra.

We begin by examining the commutant of a direct sum of operators. Recall that if $\mathcal{H}=\mathcal{H}_1\oplus\mathcal{H}_2\oplus\cdots$ and $A_n\in\mathcal{B}(\mathcal{H}_n)$ for $n\geqslant 1$, then $A=A_1\oplus A_2\oplus\cdots$ defines a bounded operator on $\mathcal{H}$ if and only if $\sup_n\|A_n\|<\infty$; in this case $\|A\|=\sup_n\|A_n\|$. Also, each operator $B$ on $\mathcal{H}$ has a matrix representation $[B_{ij}]$ where $B_{ij}\in\mathcal{B}(\mathcal{H}_j,\mathcal{H}_i)$.

**6.1. Proposition.** (a) *If $A=A_1\oplus A_2\oplus\cdots$ is a bounded operator on $\mathcal{H}=\mathcal{H}_1\oplus\mathcal{H}_2\oplus\cdots$ and $B=[B_{ij}]\in\mathcal{B}(\mathcal{H})$, then $AB=BA$ if and only if $B_{ij}A_j=A_iB_{ij}$ for all $i,j$.*

(b) *If $B=[B_{ij}]\in\mathcal{B}(\mathcal{H}^{(n)})$, $BA^{(n)}=A^{(n)}B$ if and only if $B_{ij}A=AB_{ij}$ for all $i,j$.*

The proof of this proposition is an easy exercise in matrix manipulation and is left to the reader.

**6.2. Proposition.** *If $A\in\mathcal{B}(\mathcal{H})$ and $1\leqslant n\leqslant\infty$, then $\{A^{(n)}\}''=\{B^{(n)}:B\in\{A\}''\}=\{\{A\}''\}^{(n)}$.*

**Proof.** The second equality in the statement is a tautology and it is the first equality that forms the substance of the proposition. If $B\in\{A\}''$, then the preceding proposition implies that $B^{(n)}\in\{A^{(n)}\}''$. Now let $B\in\{A^{(n)}\}''$. To simplify the notation, assume $n=2$. So $B\in\{A\oplus A\}''$; let $B=[B_{ij}]$, $B_{ij}\in\mathcal{B}(\mathcal{H})$.



<a id="pdf-page-292"></a>
Since $\begin{bmatrix}0&1\\0&0\end{bmatrix}\in\{A\oplus A\}'$, matrix multiplication shows that $B_{11}=B_{22}$ and $B_{21}=0$. Similarly, the fact that $\begin{bmatrix}0&0\\1&0\end{bmatrix}$ commutes with $A\oplus A$ implies that $B_{12}=0$. If $C=B_{11}(=B_{22})$, $B=C\oplus C$. If $T\in\{A\}'$, then $T\oplus T\in\{A\oplus A\}'$, so $B(T\oplus T)=(T\oplus T)B$. This shows that $C\in\{A\}''$. $\blacksquare$

The next result is a corollary of the preceding proof.

**6.3. Corollary.** *If $\mathcal S\subseteq\mathcal B(\mathcal H)$, $\{\mathcal S^{(n)}\}''=\{\mathcal S''\}^{(n)}$.*

Say that a subspace $\mathcal M$ of $\mathcal H$ reduces a collection $\mathcal S$ of operators if it reduces each operator in $\mathcal S$. By Proposition II.3.7, $\mathcal M$ reduces $\mathcal S$ if and only if the projection of $\mathcal H$ onto $\mathcal M$ belongs to $\mathcal S'$. This is important in the next theorem, due to von Neumann [1929].

**6.4. The Double Commutant Theorem.** *If $\mathcal A$ is a $C^*$-subalgebra of $\mathcal B(\mathcal H)$ containing $1$, then $\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A=\mathrm{WOT}\text{-}\mathrm{cl}\,\mathcal A=\mathcal A''$.*

**Proof.** By Corollary 5.2, $\mathrm{WOT}\text{-}\mathrm{cl}\,\mathcal A=\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A$. Also, since $\mathcal A''$ is SOT closed (Exercise 2) and $\mathcal A\subseteq\mathcal A''$, $\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A\subseteq\mathcal A''$.

It remains to show that $\mathcal A''\subseteq\mathrm{SOT}\text{-}\mathrm{cl}\,\mathcal A$. To do this Proposition 5.3 will be used.

Let $B\in\mathcal A''$, $n\geq1$, and let $\mathcal M\in\operatorname{Lat}\mathcal A^{(n)}$. It must be shown that $B^{(n)}\mathcal M\subseteq\mathcal M$. Because $\mathcal A$ is a $C^*$-algebra, so is $\mathcal A^{(n)}$. So the fact that $\mathcal M\in\operatorname{Lat}\mathcal A^{(n)}$ and $A^{*(n)}\in\mathcal A^{(n)}$ whenever $A^{(n)}\in\mathcal A^{(n)}$ implies that $\mathcal M$ reduces $A^{(n)}$ for each $A$ in $\mathcal A$. Si if $P$ is the projection of $\mathcal H^{(n)}$ onto $\mathcal M$, $P\in\{\mathcal A^{(n)}\}'$. But $B\in\mathcal A''$; so by Corollary 6.3, $B^{(n)}\in\{\mathcal A^{(n)}\}''$. Hence $B^{(n)}P=PB^{(n)}$ and $\mathcal M\in\operatorname{Lat}B^{(n)}$. $\blacksquare$

**6.5. Corollary.** *If $\mathcal A$ is a SOT closed $C^*$-subalgebra of $\mathcal B(\mathcal H)$ containing $1$ and $A\in\mathcal B(\mathcal H)$ such that $A(P\mathcal H)\subseteq P\mathcal H$ for every projection $P$ in $\mathcal A'$, then $A\in\mathcal A$.*

**Proof.** This uses, in addition to the Double Commutant Theorem, Proposition 4.8 as applied to $\mathcal A'$. Indeed, $\mathcal A'$ is a SOT closed $C^*$-algebra and hence it is the norm-closed linear span of its projections. So if $A\in\mathcal B(\mathcal H)$ and $AP\mathcal H\subseteq P\mathcal H$ for every projection $P$ in $\mathcal A'$, then $A(1-P)\mathcal H\subseteq(1-P)\mathcal H$ for every projection $P$ in $\mathcal A'$. Thus $P\mathcal H$ reduces $A$ and, hence, $AP=PA$. By (4.8), $A\in\mathcal A''=\mathcal A$. $\blacksquare$

**6.6. Theorem.** *If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\phi\in L^\infty(\mu)$, define $M_\phi$ on $L^2(\mu)$ by $M_\phi f=\phi f$. If $\mathcal A_\mu\equiv\{M_\phi:\phi\in L^\infty(\mu)\}$, then $\mathcal A_\mu'=\mathcal A_\mu=\mathcal A_\mu''$.*

**Proof.** It is easy to see that if $\mathcal A=\mathcal A'$, then $\mathcal A=\mathcal A''$. Since $\mathcal A_\mu\subseteq\mathcal A_\mu'$, it suffices to show that $\mathcal A_\mu'\subseteq\mathcal A_\mu$. So fix $A$ in $\mathcal A_\mu'$; it must be shown that $A=M_\phi$ for some $\phi$ in $L^\infty(\mu)$.

*Case 1:* $\mu(X)<\infty$. Here $1\in L^2(\mu)$; put $\phi=A(1)$. Thus $\phi\in L^2(\mu)$. If $\psi\in L^\infty(\mu)$,



<a id="pdf-page-293"></a>
then $\psi\in L^{2}(\mu)$ and $A(\psi)=AM_{\psi}1=M_{\psi}A1=M_{\psi}\phi=\phi\psi$. Also, $\|\phi\psi\|_{2}=\|A\psi\|_{2}\leq\|A\|\|\psi\|_{2}$.

Let $\Delta_{n}=\{x\in X:|\phi(x)|\geq n\}$. Putting $\psi=\chi_{\Delta_{n}}$ in the preceding argument gives

$$
\|A\|^{2}\mu(\Delta_{n})
=\|A\|^{2}\|\psi\|^{2}
\geq\|\phi\psi\|^{2}
=\int_{\Delta_{n}}|\phi|^{2}\,d\mu
\geq n^{2}\mu(\Delta_{n}).
$$

So if $\mu(\Delta_{n})\neq0$, $\|A\|\geq n$. Since $A$ is bounded, $\mu(\Delta_{n})=0$ for some $n$; equivalently, $\phi\in L^{\infty}(\mu)$. But $A=M_{\phi}$ on $L^{\infty}(\mu)$ and $L^{\infty}(\mu)$ is dense in $L^{2}(\mu)$, so $A=M_{\phi}$ on $L^{2}(\mu)$.

*Case 2:* $\mu(X)=\infty$. If $\mu(\Delta)<\infty$, let $L^{2}(\mu|\Delta)=\{f\in L^{2}(\mu):f=0\text{ off }\Delta\}$. For $f$ in $L^{2}(\mu|\Delta)$, $Af=A\chi_{\Delta}f=\chi_{\Delta}Af\in L^{2}(\mu|\Delta)$. Let $A_{\Delta}$ be the restriction of $A$ to $L^{2}(\mu|\Delta)$. By Case 1, there is a $\phi_{\Delta}$ in $L^{\infty}(\mu|\Delta)$ such that $A_{\Delta}=M_{\phi_{\Delta}}$. Now if $\mu(\Delta_{1})<\infty$ and $\mu(\Delta_{2})<\infty$, $\phi_{\Delta_{1}}|\Delta_{1}\cap\Delta_{2}=\phi_{\Delta_{2}}|\Delta_{1}\cap\Delta_{2}$ (Exercise).

Write $X=\bigcup_{n=1}^{\infty}\Delta_{n}$, where $\Delta_{n}\in\Omega$ and $\mu(\Delta_{n})<\infty$. From the argument above, if $\phi(x)=\phi_{\Delta_{n}}(x)$ when $x\in\Delta_{n}$, $\phi$ is a well-defined measurable function on $X$. Now $\|\phi_{\Delta}\|_{\infty}=\|M_{\phi_{\Delta}}\|$ (II.1.5) $=\|A_{\Delta}\|\leq\|A\|$; hence $\|\phi\|\leq\|A\|$. It is easy to check that $A=M_{\phi}$. ■

The next result will enable us to solve a number of problems concerning normal operators. It can be considered as a result that removes a technicality, but it is much more than that.

**6.7. The Fuglede–Putnam Theorem.** *If $N$ and $M$ are normal operators on $\mathcal H$ and $\mathcal K$, and $B:\mathcal K\to\mathcal H$ is an operator such that $NB=BM$, then $N^{*}B=BM^{*}$.*

**Proof.** Note that it follows from the hypothesis that $N^{k}B=BM^{k}$ for all $k\geq0$. So if $p(z)$ is a polynomial, $p(N)B=Bp(M)$. Since for a fixed $z$ in $\mathbb C$, $\exp(i\bar zN)$ and $\exp(i\bar zM)$ are limits of polynomials in $N$ and $M$, respectively, it follows that $\exp(i\bar zN)B=B\exp(i\bar zM)$ for all $z$ in $\mathbb C$. Equivalently, $B=e^{-i\bar zN}Be^{i\bar zM}$. Because $\exp(X+Y)=(\exp X)(\exp Y)$ when $X$ and $Y$ commute, the fact that $N$ and $M$ are normal implies that

$$
\begin{aligned}
f(z)&\equiv e^{-izN^{*}}Be^{izM^{*}}\\
&=e^{-izN^{*}}e^{-i\bar zN}Be^{i\bar zM}e^{izM^{*}}\\
&=e^{-i(zN^{*}+\bar zN)}Be^{i(\bar zM+zM^{*})}.
\end{aligned}
$$

But for every $z$ in $\mathbb C$, $zN^{*}+\bar zN$ and $zM^{*}+\bar zM$ are hermitian operators. Hence $\exp[-i(zN^{*}+\bar zN)]$ and $\exp[i(zM^{*}+\bar zM)]$ are unitary (Exercise 2.14). Therefore $\|f(z)\|\leq\|B\|$. But $f:\mathbb C\to\mathcal B(\mathcal K,\mathcal H)$ is an entire function. By Liouville’s Theorem, $f$ is constant.

Thus, $0=f'(z)=-iN^{*}e^{-izN^{*}}Be^{izM^{*}}+ie^{-izN^{*}}BM^{*}e^{izM^{*}}$. Putting $z=0$ gives $0=-iN^{*}B+iBM^{*}$, whence the theorem. ■

This theorem was originally proved in Fuglede [1950] under the


<a id="pdf-page-294"></a>
assumption that $N=M$. As stated, the theorem was proved in Putnam [1951]. The proof given here is due to Rosenblum [1958]. Another proof is in Radjavi and Rosenthal [1973]. Berberian [1959] observed that Putnam’s version can be derived from Fuglede’s original theorem by the following matrix trick. If

$$
L=\begin{bmatrix}N&0\\0&M\end{bmatrix}
\quad\text{and}\quad
A=\begin{bmatrix}0&B\\0&0\end{bmatrix}
$$

then $L$ is normal on $\mathcal H\oplus\mathcal H$ and $LA=AL$. Hence $L^*A=AL^*$, and this gives Putnam’s version.

**6.8. Corollary.** *If $N=\int z\,dE(z)$ and $BN=NB$, then $BE(\Delta)=E(\Delta)B$ for every Borel set $\Delta$.*

**Proof.** If $BN=NB$, then $BN^*=N^*B$; the conclusion now follows by The Spectral Theorem. ■

The Fuglede–Putnam Theorem can be combined with some other results we have obtained to yield the following.

**6.9. Corollary.** *If $\mu$ is a compactly supported measure on $\mathbb C$, then*

$$
\{N_\mu\}'=\mathcal A_\mu\equiv\{M_\phi:\phi\in L^\infty(\mu)\}.
$$

**Proof.** Clearly $\mathcal A_\mu\subseteq\{N_\mu\}'$. If $A\in\{N_\mu\}'$, then Theorem 6.7 implies $AN_\mu^*=N_\mu^*A$. By an easy algebraic argument, $AM_\phi=M_\phi A$ whenever $\phi$ is a polynomial in $z$ and $\bar z$. By taking weak* limits of such polynomials, it follows that $A\in\mathcal A_\mu'$. By Theorem 6.6 $A\in\mathcal A_\mu$. ■

Putnam applied his generalization of Fuglede’s Theorem to show that similar normal operators must be unitarily equivalent. This has a formal generalization which is useful.

**6.10. Proposition.** *Let $N_1$ and $N_2$ be normal operators on $\mathcal H_1$ and $\mathcal H_2$. If $X:\mathcal H_1\to\mathcal H_2$ is an operator such that $XN_1=N_2X$, then:*

(a) $\operatorname{cl}(\operatorname{ran}X)$ reduces $N_2$;

(b) $\ker X$ reduces $N_1$;

(c) If $M_1=N_1|(\ker X)^\perp$ and $M_2=N_2|\operatorname{cl}(\operatorname{ran}X)$, then $M_1\cong M_2$.

**Proof.** (a) If $f_1\in\mathcal H_1$, $N_2Xf_1=XN_1f_1\in\operatorname{ran}X$; so $\operatorname{cl}(\operatorname{ran}X)$ is invariant for $N_2$. By the Fuglede–Putnam Theorem, $XN_1^*=N_2^*X$, so $\operatorname{cl}(\operatorname{ran}X)$ is invariant for $N_2^*$.

(b) Exercise.

(c) Since $X(\ker X)^\perp\subseteq\operatorname{cl}(\operatorname{ran}X)$, part (c) will be proved if it can be shown that $N_1\cong N_2$ when $\ker X=(0)$ and $\operatorname{ran}X$ is dense. So make these assumptions and consider the polar decomposition of $X$, $X=UA$ (see Exercise 11).



<a id="pdf-page-295"></a>
Because $\ker X=(0)$ and $\operatorname{ran}X$ is dense, $A$ is a positive operator on $\mathcal H_1$ and $U:\mathcal H_1\to\mathcal H_2$ is an isomorphism. Now $X^*N_2^*=N_1^*X^*$, so $X^*N_2=N_1X^*$. A calculation shows that $A^2=X^*X\in\{N_1\}'$, so $A\in\{N_1\}'$. (Why?) Hence $N_2UA=N_2X=UAN_1=UN_1A$; that is, $N_2U=UN_1$ on the range of $A$. But $\ker A=(0)$, so $\operatorname{ran}A$ is dense in $\mathcal H_1$. Therefore $N_2U=UN_1$, or $N_2=UN_1U^{-1}$. $\blacksquare$

**6.11. Corollary.** *Two similar normal operators are unitarily equivalent.*

The corollary appears in Putnam [1951], while Proposition 6.10 first appeared in Douglas [1969].

## Exercises

1. If $\mathcal S\subseteq\mathcal B(\mathcal H)$, show that $\mathcal S'=\mathcal S'''$.

2. If $\mathcal S\subseteq\mathcal B(\mathcal H)$, show that $\mathcal S'$ is always a SOT closed subalgebra of $\mathcal B(\mathcal H)$.

3. Prove Proposition 6.1.

4. Let $\mathcal H$ be a Hilbert space of dimension $\alpha$ and define $S:\mathcal H^{(\infty)}\to\mathcal H^{(\infty)}$ by $S(h_1,h_2,\ldots)=(0,h_1,h_2,\ldots)$. $S$ is called the *unilateral shift of multiplicity* $\alpha$. (a) Show that $A=[A_{ij}]\in\{S\}'$ if and only if $A_{ij}=0$ for $j>i$ and $A_{ij}=A_{i+1,j+1}$ for $i\geq j$. (b) Show that $A=[A_{ij}]\in\{S\}''$ if and only if $A_{ij}=0$ for $j>i$ and $A_{ij}=A_{i+1,j+1}=$ a multiple of the identity for $i\geq j$.

5. What is $\{N_\mu\oplus N_\mu\}'$? $\{N_\mu\oplus N_\mu\}''$?

6. If $\mathcal A$ is a subalgebra of $\mathcal B(\mathcal H)$, show that $\mathcal A$ is a maximal abelian subalgebra of $\mathcal B(\mathcal H)$ if and only if $\mathcal A=\mathcal A'$.

7. Find a non-normal operator that is similar to a normal operator. (Hint: Try $\dim\mathcal H=2$.)

8. Let $\mu$ be a compactly supported measure on $\mathbb C$ and let $\mathcal H$ be a separable Hilbert space. A function $f:\mathbb C\to\mathcal H$ is a Borel function if $f^{-1}(G)$ is a Borel set when $G$ is weakly open in $\mathcal H$. Define $L^2(\mu,\mathcal H)$ to be the equivalence classes of Borel functions $f:\mathbb C\to\mathcal H$ such that $\int\|f(x)\|^2\,d\mu(x)<\infty$. Define $\langle f,g\rangle=\int\langle f(x),g(x)\rangle\,d\mu(x)$ for $f$ and $g$ in $L^2(\mu,\mathcal H)$. (a) Show that $L^2(\mu,\mathcal H)$ is a Hilbert space. Define $N$ on $L^2(\mu,\mathcal H)$ by $(Nf)(z)=zf(z)$. (b) Show that $N$ is a normal operator and $\sigma(N)=\operatorname{support}\mu$. Calculate $N^*$. (c) Show that $N\cong N_\mu^{(\alpha)}$, where $\alpha=\dim\mathcal H$. (d) Find $\{N\}'$. (Hint: Use 6.1.) (e) Find $\{N\}''$.

9. Let $\mathcal H$ be separable with basis $\{e_n\}$. Let $A$ be the diagonal operator on $\mathcal H$ given by $Ae_n=\lambda_ne_n$, where $\sup_n|\lambda_n|<\infty$. Determine $\{A\}'$ and $\{A\}''$. Give necessary and sufficient conditions on $\{\lambda_n\}$ such that $\{A\}'=\{A\}''$.

10. Let $\mathcal A$ be a $C^*$-subalgebra of $\mathcal B(\mathcal H)$ but do not assume that $\mathcal A$ contains the identity operator. Let $\mathcal M=\bigvee\{\operatorname{ran}A:A\in\mathcal A\}$ and let $P=$ the projection of $\mathcal H$ onto $\mathcal M$. Show that $\operatorname{SOT\!-\!cl}\mathcal A=\mathcal A''P=P\mathcal A''$.

11. Formulate and prove a polar decomposition for operators between different Hilbert spaces.



    <a id="pdf-page-296"></a>
12. Let $(X,\Omega,\mu)$ be an arbitrary measure space and let $L\in L^{1}(\mu)^{*}$. (a) Show that for every $f$ in $L^{2}(\mu)$, there is an $h$ in $L^{2}(\mu)$ such that $L(g\bar f)=\int g\bar h\,d\mu$ for all $g$ in $L^{2}(\mu)$. (b) If $f\in L^{2}(\mu)$, let $Tf$ be the function $h$ in $L^{2}(\mu)$ obtained in part (a). Show that $T:L^{2}(\mu)\to L^{2}(\mu)$ defines a bounded linear operator and $T$ commutes with $M_{\phi}$ for every $\phi$ in $L^{\infty}(\mu)$. (c) In light of parts (a) and (b), compare Theorem 6.6 and Example 20.17 in Hewitt and Stromberg [1975].

## §7. Abelian von Neumann Algebras

<!-- BEGIN BACKGROUND BG-IX.block5 -->
<a id="bg-ix-7"></a>
### Lemma BG-IX.7 — A cyclic vector on a $\sigma$-finite measure space

If $\mu$ is $\sigma$-finite, there is $f\in L^2(\mu)$ positive almost everywhere. Such an $f$ is both cyclic and separating for the algebra of bounded multiplication operators.

**Proof.** Choose a measurable partition $X=\bigcup_nE_n$ with $\mu(E_n)<\infty$ and put $f=\sum_n2^{-n}(1+\mu(E_n))^{-1/2}\chi_{E_n}$. This is positive everywhere and its squared integral is at most $\sum_n4^{-n}$. If $M_\phi f=0$, positivity gives $\phi=0$ almost everywhere, proving separation. For $g\in L^2$, set $\phi_n=(g/f)\chi_{\{|g/f|\leq n\}}$. These are bounded measurable functions and $\phi_nf\to g$ in $L^2$ by dominated convergence. Thus the orbit of $f$ is dense. $\square$
<!-- END BACKGROUND BG-IX.block5 -->

**7.1. Definition.** A *von Neumann algebra* $\mathcal A$ is a C\*-subalgebra of $\mathcal B(\mathcal H)$ such that $\mathcal A=\mathcal A''$.

Note that if $\mathcal A$ is a von Neumann algebra, then $1\in\mathcal A$ and $\mathcal A$ is SOT closed. Conversely, if $1\in\mathcal A$ and $\mathcal A$ is a SOT closed C\*-subalgebra of $\mathcal B(\mathcal H)$, then $\mathcal A$ is a von Neumann algebra by the Double Commutant Theorem.

It is a result of S. Sakai that a C\*-algebra is isomorphic to a von Neumann algebra if it is the dual of a Banach space. The converse to this is an easy consequence of the fact that $\mathcal B(\mathcal H)$ is a dual space (Exercise 2.21). For an account of the history of this result and its predecessors, as well as a number of proofs, see Kadison [1985].

**7.2. Examples.** (a) $\mathcal B(\mathcal H)$ and $\mathbb C$ are von Neumann algebras.

(b) If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, then $\mathcal A_{\mu}\equiv\{M_{\phi}:\phi\in L^{\infty}(\mu)\}\subseteq\mathcal B(L^{2}(\mu))$ is an abelian von Neumann algebra by Theorem 6.6. In fact, it is a maximal abelian von Neumann algebra.

It will be shown in this section that $\mathcal A_{\mu}$ is the only abelian von Neumann algebra up to a \*-isomorphism. However, there are many others that are not unitarily equivalent to $\mathcal A_{\mu}$.

For $\mathcal A_j\subseteq\mathcal B(\mathcal H_j)$, $j\geq 1$, $\mathcal A_1\oplus\mathcal A_2\oplus\cdots$ is used to denote the $l^{\infty}$ direct sum of $\mathcal A_1,\mathcal A_2,\ldots$. That is, $\mathcal A_1\oplus\mathcal A_2\oplus\cdots=\{A_1\oplus A_2\oplus\cdots:A_j\in\mathcal A_j$ for $j\geq 1$ and $\sup_j\|A_j\|<\infty\}$. Note that $\mathcal A_1\oplus\mathcal A_2\oplus\cdots\subseteq\mathcal B(\mathcal H_1\oplus\mathcal H_2\oplus\cdots)$ and $\|A_1\oplus A_2\oplus\cdots\|=\sup_j\|A_j\|$.

**7.3. Proposition.** *(a) If $\mathcal A_1,\mathcal A_2,\ldots$ are von Neumann algebras, then so is $\mathcal A_1\oplus\mathcal A_2\oplus\cdots$. (b) If $\mathcal A$ is a von Neumann algebra and $1\leq n\leq\infty$, then $\mathcal A^{(n)}$ is a von Neumann algebra.*

**Proof.** Exercise.

The proof of the next result is also an exercise.

**7.4. Proposition.** *Let $\mathcal A_j$ be a von Neumann algebra on $\mathcal H_j$, $j=1,2$. If $U:\mathcal H_1\to\mathcal H_2$ is an isomorphism such that $U\mathcal A_1U^{-1}=\mathcal A_2$, then $U\mathcal A_1'U^{-1}=\mathcal A_2'$.*

Now let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and define $\rho:\mathcal A_{\mu}\to\mathcal A_{\mu}^{(2)}$ by



<a id="pdf-page-297"></a>
$\rho(T)=T\oplus T$. Then $\rho$ is a $*$-isomorphism. However, $\mathcal A_\mu$ and $\mathcal A_\mu^{(2)}$ are not *spatially isomorphic*. That is, there is no Hilbert space isomorphism $U:L^2(\mu)\to L^2(\mu)\oplus L^2(\mu)$ such that $U\mathcal A_\mu U^{-1}=\mathcal A_\mu^{(2)}$. Why? One way to see that no such $U$ exists is to note that $\mathcal A_\mu$ has a cyclic vector (give an example). However, $\mathcal A_\mu^{(2)}$ does not have a cyclic vector as shall be seen presently (Theorem 7.8).

**7.5. Definition.** If $\mathcal A\subseteq\mathcal B(\mathcal H)$ and $e_0\in\mathcal H$, then $e_0$ is a *separating vector* for $\mathcal A$ if the only operator $A$ in $\mathcal A$ such that $Ae_0=0$ is the operator $A=0$.

If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $f\in L^2(\mu)$ such that $\mu(\{x\in X:f(x)=0\})=0$ (Why does such an $f$ exist?), then $f$ is a separating vector for $\mathcal A_\mu$ as well as a cyclic vector. If $\mathcal A=\mathcal B(\mathcal H)$, then no vector in $\mathcal H$ is separating for $\mathcal A$ while every nonzero vector is a cyclic vector. If $\mathcal A=\mathbb C$ and $\dim\mathcal H>1$, then $\mathcal A$ has no cyclic vectors but every nonzero vector is separating for $\mathcal A$.

**7.6. Proposition.** *If $e_0$ is a cyclic vector for $\mathcal A$, then $e_0$ is a separating vector for $\mathcal A'$.*

**Proof.** If $T\in\mathcal A'$ and $Te_0=0$, then for every $A$ in $\mathcal A$, $TAe_0=ATe_0=0$. Since $\bigvee\mathcal A e_0=\mathcal H$, $T=0$. $\blacksquare$

**7.7. Corollary.** *If $\mathcal A$ is an abelian subalgebra of $\mathcal B(\mathcal H)$, then every cyclic vector for $\mathcal A$ is a separating vector for $\mathcal A$.*

**Proof.** Because $\mathcal A$ is abelian, $\mathcal A\subseteq\mathcal A'$. $\blacksquare$

Since $\mathcal B(\mathcal H)'=\mathbb C$, Proposition 7.6 explains some of the duality exhibited prior to (7.6). Also note that if $(X,\Omega,\mu)$ is a finite measure space, $1\oplus0$, $0\oplus1$, and $1\oplus1$ are all separating vectors for $\mathcal A_\mu^{(2)}$. Because $\mathcal A_\mu^{(2)}\ne(\mathcal A_\mu^{(2)})'$, the next theorem says that $\mathcal A_\mu^{(2)}$ has no cyclic vector.

Although it is easy to see that conditions (a) and (b) in the next result are equivalent, irrespective of any assumption on $\mathcal H$, the equivalence of the remaining parts to (a) and (b) is not true unless some additional assumption is made on $\mathcal H$ or $\mathcal A$ (see Exercise 5). We are content to assume that $\mathcal H$ is separable.

**7.8. Theorem.** *Assume that $\mathcal H$ is separable and $\mathcal A$ is an abelian $C^*$-subalgebra of $\mathcal B(\mathcal H)$. The following statements are equivalent.*

(a) $\mathcal A$ is a maximal abelian von Neumann algebra.

(b) $\mathcal A=\mathcal A'$.

(c) $\mathcal A$ has a cyclic vector, contains $1$, and is SOT closed.

(d) There is a compact metric space $X$, a positive Borel measure $\mu$ with support $X$, and an isomorphism $U:L^2(\mu)\to\mathcal H$ such that $U\mathcal A_\mu U^{-1}=\mathcal A$.

**Proof.** The proof that (a) and (b) are equivalent is left as an exercise.



<a id="pdf-page-298"></a>
(b)$\Rightarrow$(c): By Zorn’s Lemma and the separability of $\mathcal H$, there is a maximal sequence of unit vectors $\{e_n\}$ such that for $n\ne m$, $\operatorname{cl}[\mathcal A e_n]\perp\operatorname{cl}[\mathcal A e_m]$. It follows from the maximality of $\{e_n\}$ that $\mathcal H=\bigoplus_{n=1}^{\infty}\operatorname{cl}[\mathcal A e_n]$.

Let $e_0=\sum_{n=1}^{\infty}e_n/\sqrt{2^n}$. Since $e_n\perp e_m$ for $n\ne m$, $\|e_0\|^2=\sum 2^{-n}=1$. Let $P_n=$ the projection of $\mathcal H$ onto $\mathcal H_n=\operatorname{cl}[\mathcal A e_n]$. Clearly $\mathcal A$ leaves $\mathcal H_n$ invariant and so, since $\mathcal A$ is a $*$-algebra, $\mathcal H_n$ reduces $\mathcal A$. Thus $P_n\in\mathcal A'=\mathcal A$ and $\operatorname{cl}[\mathcal A e_0]\supseteq\operatorname{cl}[\mathcal A P_n e_0]=\operatorname{cl}[\mathcal A e_n]=\mathcal H_n$. Therefore $\operatorname{cl}[\mathcal A e_0]=\mathcal H$ and $e_0$ is a cyclic vector for $\mathcal A$.

(c)$\Rightarrow$(d): Since $\mathcal H$ is separable, ball $\mathcal A$ is WOT metrizable and compact (1.3 and 5.5). By picking a countable WOT dense subset of ball $\mathcal A$ and letting $\mathcal A_1$ be the $C^*$-algebra generated by this countable dense subset, it follows that $\mathcal A_1$ is a separable $C^*$-algebra whose SOT closure is $\mathcal A$. Let $X$ be the maximal ideal space of $\mathcal A_1$ and let $\rho:C(X)\to\mathcal A_1\subseteq\mathcal A\subseteq\mathcal B(\mathcal H)$ be the inverse of the Gelfand map. By Theorem 1.14 there is a spectral measure $E$ defined on the Borel subsets of $X$ such that $\rho(u)=\int u\,dE$ for $u$ in $C(X)$. If $\phi\in B(X)$ and $\{u_i\}$ is a net in $C(X)$ such that $\int u_i\,d\nu\to\int\phi\,d\nu$ for every $\nu$ in $M(X)$, then $\rho(u_i)=\int u_i\,dE\to\int\phi\,dE$ (WOT). Thus $\{\int\phi\,dE:\phi\in B(X)\}\subseteq\mathcal A$ since $\mathcal A$ is SOT closed.

Let $e_0$ be a cyclic vector for $\mathcal A$ and put $\mu(\Delta)=\|E(\Delta)e_0\|^2=\langle E(\Delta)e_0,e_0\rangle$. Thus $\langle(\int\phi\,dE)e_0,e_0\rangle=\int\phi\,d\mu$ for every $\phi$ in $B(X)$. Consider $B(X)$ as a linear manifold in $L^2(\mu)$ by identifying functions that agree a.e. $[\mu]$. If $\phi\in B(X)$, then

$$
\begin{aligned}
\left\|\left(\int\phi\,dE\right)e_0\right\|^2
&=\left\langle\left(\int\phi\,dE\right)^*
\left(\int\phi\,dE\right)e_0,e_0\right\rangle\\
&=\int|\phi|^2\,d\mu.
\end{aligned}
$$

This says two things. First, if $\phi=0$ a.e. $[\mu]$, then $(\int\phi\,dE)e_0=0$. Hence $U:B(X)\to\mathcal H$ defined by $U\phi=(\int\phi\,dE)e_0$ is a well-defined map from the dense manifold $B(X)$ in $L^2(\mu)$ into $\mathcal H$. Second, $U$ is an isometry. Since the domain and range of $U$ are dense (Why?), $U$ extends to an isomorphism $U:L^2(\mu)\to\mathcal H$.

If $\phi\in B(X)$ and $\psi\in L^\infty(\mu)$, then $UM_\psi\phi=U(\psi\phi)=(\int\psi\phi\,dE)e_0=(\int\psi\,dE)(\int\phi\,dE)e_0=(\int\psi\,dE)U\phi$. Hence $UM_\psi U^{-1}=\int\psi\,dE$ and $U\mathcal A_\mu U^{-1}\subseteq\mathcal A$. On the other hand, $U\mathcal A_\mu U^{-1}$ is a SOT closed $C^*$-subalgebra of $\mathcal B(\mathcal H)$ that contains $UC(X)U^{-1}=\mathcal A_1$. (Why?) So $U\mathcal A_\mu U^{-1}=\mathcal A$.

Because $\mathcal A_1$ is separable, $X$ is metrizable.

(d)$\Rightarrow$(b): This is a consequence of Theorem 6.6 and Proposition 7.4. $\blacksquare$

Mercer (1986) shows that for a maximal abelian von Neumann algebra $\mathcal A$, there is an orthonormal basis for the underlying Hilbert space consisting of vectors that are cyclic and separating for $\mathcal A$.

**7.9. Corollary.** *If $\mathcal A$ is an abelian $C^*$-subalgebra of $\mathcal B(\mathcal H)$ and $\mathcal H$ is separable, then $\mathcal A$ has a separating vector.*



<a id="pdf-page-299"></a>
**PROOF.** By Zorn’s Lemma, $\mathcal A$ is contained in a maximal abelian $C^*$-algebra, $\mathcal A_m$. It is easy to see that $\mathcal A_m$ must be SOT closed, so $\mathcal A_m$ is a maximal abelian von Neumann algebra. By the preceding theorem, there is a cyclic vector $e_0$ for $\mathcal A_m$. But (7.7) $e_0$ is separating for $\mathcal A_m$, and hence for any subset of $\mathcal A_m$. $\blacksquare$

The preceding corollary may seem innocent, but it is, in fact, the basis for the next section.

## EXERCISES

1. Prove Proposition 7.3.

2. Prove Proposition 7.4.

3. Why are $\mathcal A_\mu$ and $\mathcal A_\mu^{(2)}$ not spatially isomorphic?

4. Show that if $X$ is any compact metric space, there is a separable Hilbert space $\mathcal H$ and a $*$-monomorphism $\tau\colon C(X)\to\mathcal B(\mathcal H)$. Find the spectral measure for $\tau$.

5. Let $\mathcal A$ be an abelian $C^*$-subalgebra of $\mathcal B(\mathcal H)$ such that $\mathcal A'$ contains no uncountable collection of pairwise orthogonal projections. Show that the following statements are equivalent: (a) $\mathcal A$ is a maximal abelian von Neumann algebra; (b) $\mathcal A=\mathcal A'$; (c) $\mathcal A$ has a cyclic vector and is SOT closed; (d) there is a finite measure space $(X,\Omega,\mu)$ and an isomorphism $U\colon L^2(\mu)\to\mathcal H$ such that $U\mathcal A_\mu U^{-1}=\mathcal A$.

6. Let $\{P_n\}$ be a sequence of commuting projections in $\mathcal B(\mathcal H)$ and put $A=\sum_{n=1}^{\infty}3^{-n}(2P_n-1)$. Show that $C^*(A)$ is the $C^*$-algebra generated by $\{P_n\}$. (Do you see a connection between $A$ and the Cantor–Lebesgue function?)

7. If $\mathcal A$ is an abelian von Neumann algebra on a separable Hilbert space $\mathcal H$, show that there is a hermitian operator $A$ such that $\mathcal A$ equals the smallest von Neumann algebra containing $A$. (Hint: Let $\{P_n\}$ be a countable WOT dense subset of the set projections in $\mathcal A$ and use Exercise 6. This proof is due to Rickart [1960], pp. 293–294. Also see Jenkins [1972].)

8. If $X$ is a compact space, show that $C(X)$ is generated as a $C^*$-algebra by its characteristic functions if and only if $X$ is totally disconnected. If $A$ is as in Exercise 6, show that $\sigma(A)$ is totally disconnected.

9. If $X$ and $Y$ are compact spaces and $\tau\colon C(X)\to C(Y)$ is a homomorphism with $\tau(1)=1$, show that there is a continuous function $\phi\colon Y\to X$ such that $\tau(u)=u\circ\phi$ for every $u$ in $C(X)$. Show that $\tau$ is injective if and only if $\phi$ is surjective, and, in this case, $\tau$ is an isometry. Show that $\tau$ is surjective if and only if $\phi$ is injective.

10. Let $X$ and $Z$ be compact spaces, $Y=X\times Z$, and let $\phi\colon Y\to X$ be the projection onto the first coordinate. Define $\tau\colon C(X)\to C(Y)$ by $\tau(u)=u\circ\phi$. Describe the range of $\tau$.

11. Adopt the notation of Exercise 9. Define an equivalence relation $\sim$ on $Y$ by saying $y_1\sim y_2$ if and only if $\phi(y_1)=\phi(y_2)$. Let $q\colon Y\to Y/{\sim}$ be the natural map and $q^*\colon C(Y/{\sim})\to C(Y)$ the induced homomorphism. Show that there is a $*$-epimorphism $\rho\colon C(X)\to C(Y/{\sim})$ such that the diagram



    <a id="pdf-page-300"></a>
    ![](assets/p0300-page_299_image_2.jpg)

    commutes. Find the corresponding injection $Y/{\sim}\to X$.

12. If $X$ is any compact metric space, show that there is a totally disconnected compact metric space $Y$ and a continuous surjection $\phi\colon Y\to X$. (Hint: Start by embedding $C(X)$ into $\mathscr{B}(\mathscr{H})$ and use Exercises 7 and 8.)

13. Show that every totally disconnected compact metric space is the continuous image of the Cantor ternary set. (Do this directly; do not try to use $C^*$-algebras.) Combine this with Exercise 12 to get that every compact metric space is the continuous image of the Cantor set.

14. If $\mathscr{A}$ is an abelian von Neumann algebra and $X$ is its maximal ideal space, then $X$ is a *Stonean space*; that is, if $U$ is open in $X$, then $\operatorname{cl}U$ is open in $X$.

15. This exercise assumes Exercise 2.21 where it was proved that $\mathscr{B}_1^*=\mathscr{B}$. When referring to the weak* topology on $\mathscr{B}=\mathscr{B}(\mathscr{H})$, we mean the topology $\mathscr{B}$ has as the Banach dual of $\mathscr{B}_1$. (a) Show that on bounded subsets of $\mathscr{B}$ the weak* topology = WOT. (b) Show that a $C^*$-subalgebra of $\mathscr{B}(\mathscr{H})$ is von Neumann algebra if and only if $\mathscr{A}$ is weak* closed. (c) Show that WOT and the weak* topology agree on abelian von Neumann algebras (See Takeda [1951] and Pallu de la Barrière [1954].) (d) Give an example of a weak* closed subspace of $\mathscr{B}$ that is not WOT closed. (See von Neumann [1936].)

16. Prove the converse of Proposition 7.6.

## §8. The Functional Calculus for Normal Operators: The Conclusion of the Saga

In this section it will always be assumed that

*all Hilbert spaces are separable.*

Indeed, this assumption will remain in force for the rest of the chapter. This assumption is necessary for the validity of some of the results and minimizes the technical details in others.

If $N$ is a normal operator on $\mathscr{H}$, let $W^*(N)$ be the von Neumann algebra generated by $N$. That is, $W^*(N)$ is the intersection of all of the von Neumann algebras containing $N$. Hence $W^*(N)$ is the WOT closure of $\{p(N,N^*):p(z,\bar z)\text{ is a polynomial in }z\text{ and }\bar z\}$.

**8.1. Proposition.** *If $N$ is a normal operator, then $W^*(N)=\{N\}''\supseteq\{\phi(N):\phi\in B(\sigma(N))\}$.*

**Proof.** The equality results from combining the Double Commutant



<a id="pdf-page-301"></a>
Theorem and the Fuglede–Putnam Theorem. If $\phi\in B(\sigma(N))$, $N=\int z\,dE(z)$, and $T\in\{N\}'$, then $T\in\{N,N^*\}'$ by the Fuglede–Putnam Theorem and $TE(\Delta)=E(\Delta)T$ for every Borel set $\Delta$ by the Spectral Theorem. Hence $T\phi(N)=\phi(N)T$ since $\phi(N)=\int\phi\,dE$. $\blacksquare$

The purpose of this section is to prove that the containment in the preceding proposition is an equality. In fact, more will be proved. A measure $\mu$ whose support is $\sigma(N)$ will be found such that $\phi(N)$ is well defined if $\phi\in L^\infty(\mu)$ and the map $\phi\mapsto\phi(N)$ is a *-isomorphism of $L^\infty(\mu)$ onto $W^*(N)$. To find $\mu$, Corollary 7.9 (which requires the separability of $\mathcal H$) is used.

By Corollary 7.9, $W^*(N)$, being an abelian von Neumann algebra, has a separating vector $e_0$. Define a measure $\mu$ on $\sigma(N)$ by

$$
\tag{8.2}
\mu(\Delta)=\langle E(\Delta)e_0,e_0\rangle=\|E(\Delta)e_0\|^2.
$$

**8.3. Proposition.** $\mu(\Delta)=0$ if and only if $E(\Delta)=0$.

**Proof.** If $\mu(\Delta)=0$, then $E(\Delta)e_0=0$. But $E(\Delta)=\chi_\Delta(N)\in W^*(N)$. Since $e_0$ is a separating vector, $E(\Delta)=0$. The reverse implication is clear. $\blacksquare$

**8.4. Definition.** A *scalar-valued spectral measure for* $N$ is a positive Borel measure $\mu$ on $\sigma(N)$ such that $\mu(\Delta)=0$ if and only if $E(\Delta)=0$; that is, $\mu$ and $E$ are mutually absolutely continuous.

So Proposition 8.3 says that scalar-valued spectral measures exist. It will be shown (8.9) that every scalar-valued spectral measure is defined by (8.2) where $e_0$ is a separating vector for $W^*(N)$. In the process additional information is obtained about a normal operator and its functional calculus.

If $h\in\mathcal H$, let $\mu_h\equiv E_{h,h}$ and let $\mathcal H_h\equiv\operatorname{cl}[W^*(N)h]$. Note that $\mathcal H_h$ is the smallest reducing subspace for $N$ that contains $h$. Let $N_h\equiv N|_{\mathcal H_h}$. Thus $N_h$ is a *-cyclic normal operator with *-cyclic vector $h$. The uniqueness of the spectral measure for a normal operator implies that the spectral measure for $N_h$ is $E(\Delta)|_{\mathcal H_h}$; that is, $\chi_\Delta(N_h)=\chi_\Delta(N)|_{\mathcal H_h}=E(\Delta)|_{\mathcal H_h}$. Thus Theorem 3.4 implies there is a unique isomorphism $U_h:\mathcal H_h\to L^2(\mu_h)$ such that $U_hh=1$ and $U_hN_hU_h^{-1}f=zf$ for all $f$ in $L^2(\mu_h)$. The notation of this paragraph is used repeatedly in this section.

The way to understand what is going on is to consider each $N_h$ as a localization of $N$. Since $N_h$ is unitarily equivalent to $M_z$ on $L^2(\mu_h)$ we can agree that we thoroughly understand the local behavior of $N$. Can we put together this local behavior of $N$ to understand the global behavior of $N$? This is precisely what is done in §10.

In the present section the objective is to show that if $h$ is a separating vector for $W^*(N)$, then the functional calculus for $N$ is completely determined by the functional calculus for $N_h$. The sense in which this “determination” is made is the following. If $A\in W^*(N)$, then the definition of $\mathcal H_h$ shows that $A\mathcal H_h\subseteq\mathcal H_h$. Since $A^*\in W^*(N)$, $\mathcal H_h$ reduces each operator in $W^*(N)$; thus



<a id="pdf-page-302"></a>
§8. The Functional Calculus for Normal Operators  287

$A|_{\mathcal H_h}$ is meaningful. It will be shown that the map $A\to A|_{\mathcal H_h}$ is a $*$-isomorphism of $W^*(N)$ onto $W^*(N_h)$ if $h$ is a separating vector for $W^*(N)$. Since $N_h$ is $*$-cyclic, Theorem 6.6 and Corollary 6.9 show how to determine $W^*(N_h)$.

We begin with a modest lemma.

**8.5. Lemma.** *If $h\in\mathcal H$ and $\rho_h:W^*(N)\to W^*(N_h)$ is defined by $\rho_h(A)=A|_{\mathcal H_h}$, then $\rho_h$ is a $*$-epimorphism that is WOT-continuous. Moreover, If $\psi\in B(\sigma(N))$, then $\rho_h(\psi(N))=\psi(N_h)$ and if $A\in W^*(N)$, then there is a $\phi$ in $B(\sigma(N_h))$ such that $\rho_h(A)=\phi(N_h)$.*

**Proof.** First let us see that $\rho_h$ maps $W^*(N)$ into $W^*(N_h)$. If $p(z,\bar z)$ is a polynomial in $z$ and $\bar z$ then $\rho_h[p(N,N^*)]=p(N_h,N_h^*)$ as an algebraic manipulation shows. If $\{p_i\}$ is a net of such polynomials such that $p_i(N,N^*)\to A$ (WOT), then for $f,g$ in $\mathcal H_h$, $\langle p_i(N,N^*)f,g\rangle\to\langle Af,g\rangle$; thus $p_i(N_h,N_h^*)\to\rho_h(A)$ (WOT) and so $\rho_h(A)\in W^*(N_h)$. It is left as an exercise for the reader to show that $\rho_h$ is a $*$-homomorphism. Also, the preceding argument can be used to show that $\rho_h$ is WOT continuous.

If $\psi\in B(\sigma(N))$, there is a net $\{p_i(z,\bar z)\}$ of polynomials in $z$ and $\bar z$ such that $\int p_i\,d\nu\to\int\psi\,d\nu$ for every $\nu$ in $M(\sigma(N))$. (Why?) Since $\sigma(N_h)\subseteq\sigma(N)$ (Why?), $\int p_i\,d\eta\to\int\psi\,d\eta$ for every $\eta$ in $M(\sigma(N_h))$. Therefore $p_i(N,N^*)\to\psi(N)$ (WOT) and $p_i(N_h,N_h^*)\to\psi(N_h)$ (WOT). But $\rho_h(p_i(N,N^*))=p_i(N_h,N_h^*)$ and $\rho_h(p_i(N,N^*))\to\rho_h(\psi(N))$; hence $\rho_h(\psi(N))=\psi(N_h)$.

Let $U_h:\mathcal H_h\to L^2(\mu_h)$ be the isomorphism such that $U_hh=1$ and $U_hN_hU_h^{-1}=N_{\mu_h}$. If $A\in W^*(N)$ and $A_h=\rho_h(A)$, then $A_hN_h=N_hA_h$; thus $U_hA_hU_h^{-1}\in\{N_{\mu_h}\}'$. By Corollary 6.9, there is a $\phi$ in $B(\sigma(N_h))$ such that $U_hA_hU_h^{-1}=M_\phi$. It follows (How?) that $A_h=\phi(N_h)$.

Finally, to show that $\rho_h$ is surjective note that if $B\in W^*(N_h)$, then (use the argument in the preceding paragraph) $B=\psi(N_h)$ for some $\psi$ in $B(\sigma(N_h))$. Extend $\psi$ to $\sigma(N)$ by letting $\psi=0$ on $\sigma(N)\setminus\sigma(N_h)$. Then $\psi(N)\in W^*(N)$ and $\rho_h(\psi(N))=\psi(N_h)=B$. $\blacksquare$

**8.6. Lemma.** *If $e\in\mathcal H$ such that $\mu_e$ is a scalar-valued spectral measure for $N$ and if $\nu$ is a positive measure on $\sigma(N)$ such that $\nu\ll\mu_e$, then there is an $h$ in $\mathcal H_e$ such that $\nu=\mu_h$.*

**Proof.** This proof is just an application of the Radon–Nikodym Theorem once certain identifications are made; namely, $f=[d\nu/d\mu_e]^{1/2}\in L^2(\mu_e)$, so put $h=U_e^{-1}f$. Hence $h\in\mathcal H_e$. For any Borel set $\Delta$, $\nu(\Delta)=\int\chi_\Delta\,d\nu=\int\chi_\Delta f\bar f\,d\mu_e=\langle M_{\chi_\Delta}f,f\rangle=\langle U_e^{-1}M_{\chi_\Delta}f,U_e^{-1}f\rangle=\langle E(\Delta)h,h\rangle=\mu_h(\Delta)$. $\blacksquare$

**8.7. Lemma.** $W^*(N)=\{\phi(N):\phi\in B(\sigma(N))\}$.

**Proof.** Let $\mathcal A=\{\phi(N):\phi\in B(\sigma(N))\}$. Hence $\mathcal A$ is a $*$-algebra and $\mathcal A\subseteq W^*(N)$ by Proposition 8.1. Since $N\in\mathcal A$ it suffices to prove that $\mathcal A$ is WOT closed. Let $\{\phi_i\}$ be a net in $B(\sigma(N))$ such that $\phi_i(N)\to A$ (WOT); so $A\in W^*(N)$. By



<a id="pdf-page-303"></a>
(8.5) $\phi_i(N_h)\to A|_{\mathcal H_h}$ (WOT) for any $h$ in $\mathcal H$. Also, by Lemma 8.5, for every $h$ in $\mathcal H$ there is a $\phi_h$ in $B(\mathbb C)$ such that $A|_{\mathcal H_h}=\phi_h(N_h)$. Fix a separating vector $e$ for $W^*(N)$; hence $\mu_e$ is a scalar-valued spectral measure for $N$.

If $h\in\mathcal H$, then the fact that $\phi_i(N_h)\to\phi_h(N_h)$ (WOT) implies $\phi_i\to\phi_h$ weak* in $L^\infty(\mu_h)$. Also, $\phi_i\to\phi_e$ weak* in $L^\infty(\mu_e)$. But $\mu_h\ll\mu_e$ so that $d\mu_h/d\mu_e\in L^1(\mu_e)$; hence for any Borel set $\Delta$

$$
\int_\Delta \phi_i\,d\mu_h
=\int_\Delta \phi_i\frac{d\mu_h}{d\mu_e}\,d\mu_e
\to\int_\Delta \phi_e\,d\mu_h.
$$

But also

$$
\int_\Delta \phi_i\,d\mu_h\to\int_\Delta \phi_h\,d\mu_h.
$$

So $0=\int_\Delta(\phi_e-\phi_h)\,d\mu_h$ for every Borel set $\Delta$. Therefore $\phi_h=\phi_e$ a.e. $[\mu_h]$. But if $g\in\mathcal H_h$, then $\langle\phi_h(N_h)g,g\rangle=\langle\phi_h(N)g,g\rangle=\int\phi_h\,d\mu_g=\int\phi_e\,d\mu_g$ since $\mu_g\ll\mu_h$. Thus $\langle\phi_h(N_h)g,g\rangle=\langle\phi_e(N_h)g,g\rangle$; that is, $\phi_h(N_h)=\phi_e(N_h)$. In particular, $Ah=\phi_h(N_h)h=\phi_e(N_h)h=\phi_e(N)h$. Since $h$ was arbitrary, $A=\phi_e(N)$. ■

**8.8. Corollary.** *If $\rho_h:W^*(N)\to W^*(N_h)$ is the $*$-epimorphism of Lemma 8.5, then $\ker\rho_h=\{\phi(N):\phi=0\text{ a.e. }[\mu_h]\}$.*

**8.9. Theorem.** *If $N$ is a normal operator and $e\in\mathcal H$, the following statements are equivalent.*

(a) $e$ is a separating vector for $W^*(N)$.

(b) $\mu_e$ is a scalar-valued spectral measure for $N$.

(c) The map $\rho_e:W^*(N)\to W^*(N_e)$ defined in (8.5) is a $*$-isomorphism.

(d) $\{\phi\in B(\sigma(N)):\phi(N)=0\}=\{\phi\in B(\sigma(N)):\phi=0\text{ a.e. }[\mu_e]\}$.

**Proof.** (a)$\Rightarrow$(b): Proposition 8.3.

(b)$\Rightarrow$(c): By Lemma 8.5, $\rho_e$ is a $*$-epimorphism. By Corollary 8.8, $\ker\rho_e=\{\phi(N):\phi=0\text{ a.e. }[\mu_e]\}$. But if $\phi=0$ a.e. $[\mu_e]$, (b) implies that $\phi=0$ off a set $\Delta$ such that $E(\Delta)=0$. Thus $\phi(N)=\int_\Delta\phi\,dE=0$.

(c)$\Rightarrow$(d): Combine (c) with Corollary 8.8.

(d)$\Rightarrow$(a): Suppose $A\in W^*(N)$ and $Ae=0$. By Lemma 8.7, there is a $\phi$ in $B(\sigma(N))$ such that $\phi(N)=A$. Thus, $0=\|Ae\|^2=\langle A^*Ae,e\rangle=\int|\phi|^2\,d\mu_e$. So $\phi=0$ a.e. $[\mu_e]$. By (d), $A=0$. ■

These results can now be combined to yield the final statement of the functional calculus for normal operators.

**8.10. The Functional Calculus for a Normal Operator.** *If $N$ is a normal operator on the separable Hilbert space $\mathcal H$ and $\mu$ is a scalar-valued spectral measure for $N$, then there is a well-defined map $\rho:L^\infty(\mu)\to W^*(N)$ given by the formula $\rho(\phi)=\phi(N)$ such that*



<a id="pdf-page-304"></a>
(a) $\rho$ is a $*$-isomorphism and an isometry;

(b) $\rho\colon (L^\infty(\mu),\text{ weak}^*)\to(W^*(N),\mathrm{WOT})$ is a homeomorphism.

**Proof.** Let $e$ be a separating vector such that $\mu=\mu_e$ [by (8.6) and (8.9)]. If $\phi\in B(\sigma(N))$ and $\phi=0$ a.e. $[\mu]$, then $\phi(N)=0$ by (8.9d); so $\rho(\phi)=\phi(N)$ is a well-defined map. It is left to the reader to show that $\rho$ is a $*$-homomorphism. By Lemma 8.7, $\rho$ is surjective. Also, if $\rho(\phi)=\phi(N)=0$, then $\phi=0$ a.e. $[\mu]$ by (8.9d). Thus $\rho$ is a $*$-isomorphism. By (VIII.4.8) $\rho$ is an isometry. (A proof avoiding (VIII.4.8) is possible—it is left as an exercise.) This proves (a).

Let $\{\phi_i\}$ be a net in $L^\infty(\mu)$ and suppose that $\phi_i(N)\to0$ (WOT). If $f\in L^1(\mu)$ and $f\geq0$, $f\mu\ll\mu=\mu_e$. By Lemma 8.6 there is a vector $h$ such that $f\mu=\mu_h$. Thus $\int\phi_i f\,d\mu=\int\phi_i\,d\mu_h=\langle\phi_i(N)h,h\rangle\to0$. Thus $\phi_i\to0$ (weak$^*$) in $L^\infty(\mu)$. This proves half of (b); the other half is left as an exercise. $\blacksquare$

**8.11. The Spectral Mapping Theorem.** *If $N$ is a normal operator on a separable space and $\mu$ is a scalar-valued spectral measure for $N$ and if $\phi\in L^\infty(\mu)$, then $\sigma(\phi(N))=$ the $\mu$-essential range of $\phi$.*

**Proof.** Use (8.10) and the fact (2.6) that the $\mu$-essential range of $\phi$ is the spectrum of $\phi$ as an element of $L^\infty(\mu)$. $\blacksquare$

**8.12. Proposition.** *Let $N$, $\mu$, $\phi$ be as in (8.11). If $N=\int z\,dE$, then $\mu\circ\phi^{-1}$ is a scalar-valued spectral measure for $\phi(N)$ and $E\circ\phi^{-1}$ is its spectral measure.*

## Exercises

1. What is a scalar-valued spectral measure for a diagonalizable normal operator?

2. Let $N_1$ and $N_2$ be normal operators with scalar-valued spectral measures $\mu_1$ and $\mu_2$. What is a scalar spectral measure for $N_1\oplus N_2$?

3. Let $\{e_n\}$ be an orthonormal basis for $\mathcal H$ and put $\mu(\Delta)=\sum_{n=1}^{\infty}2^{-n}\|E(\Delta)e_n\|^2$. Show that $\mu$ is a scalar-valued spectral measure for $N$.

4. Give an example of a normal operator on a nonseparable space which has no scalar-valued spectral measure.

5. Prove that the map $\rho$ in (8.10) is an isometry without using (VIII.4.8).

6. Prove Proposition 8.12.

7. Show that if $\mu$ and $\nu$ are compactly supported measures on $\mathbf C$, the following statements are equivalent: (a) $N_\mu\oplus N_\nu$ is $*$-cyclic; (b) $W^*(N_\mu\oplus N_\nu)=W^*(N_\mu)\oplus W^*(N_\nu)$; (c) $\mu\perp\nu$.

8. If $M$ and $N$ are normal operators with scalar-valued spectral measures $\mu$ and $\nu$, respectively, show that the following are equivalent: (a) $W^*(M\oplus N)=W^*(M)\oplus W^*(N)$; (b) $\{M\oplus N\}'=\{M\}'\oplus\{N\}'$; (c) there is no operator $A$ such that $MA=AN$ other than $A=0$; (d) $\mu\perp\nu$.

9. If $M$ and $N$ are normal operators, show that $C^*(M\oplus N)=C^*(M)\oplus C^*(N)$ if and only if $\sigma(M)\cap\sigma(N)=\square$.



   <a id="pdf-page-305"></a>
10. Give an example of two normal operators $M$ and $N$ such that $W^*(M\oplus N)=W^*(M)\oplus W^*(N)$ but $C^*(M\oplus N)\ne C^*(M)\oplus C^*(N)$. In fact, find $M$ and $N$ such that $W^*(M\oplus N)$ splits, but $\sigma(M)=\sigma(N)$.

11. If $U$ is the bilateral shift and $V$ is any unitary operator, show that $W^*(U\oplus V)=W^*(U)\oplus W^*(V)$ if and only if $V$ has a spectral measure that is singular to arc length on $\partial\mathbb D$. (See Exercise 3.7.)

12. If $\mathcal A$ is an abelian von Neumann algebra on a separable space, show that there is a compactly supported measure $\mu$ on $\mathbb R$ such that $\mathcal A$ is $*$-isomorphic to $L^\infty(\mu)$. (Hint: Use Exercise 7.7.)

13. (This exercise assumes a knowledge of Exercise 2.21.) Let $N=\int z\,dE(z)$ be a normal operator with scalar-valued spectral measure $\mu$ and define $\alpha:\mathcal B_1(\mathcal H)\to L^1(\mu)$ by $\alpha(T)(\Delta)=\operatorname{tr}(TE(\Delta))$. Show that $\alpha$ is a surjective contraction. What is $\alpha^*$? [$L^1(\mu)$ is identified, via the Radon–Nikodym Theorem, with the set of complex-valued measures that are absolutely continuous with respect to $\mu$.]

14. Let $\pi:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)/\mathcal B_0(\mathcal H)$ be the natural map and let $A\in\mathcal B(\mathcal H)$. (a) If $\pi(A)$ is hermitian, show that there is a hermitian operator $B$ such that $A-B$ is compact. (b) If $\pi(A)$ is positive, show that there is a positive operator $B$ such that $A-B$ is compact. (See Exercise XI.3.14.)

15. (L.G. Brown) If $\pi:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)/\mathcal B_0(\mathcal H)$ is the natural map and $A$ and $B$ are hermitian operators such that $\pi(A)\leq 0\leq\pi(B)$, then there is a hermitian compact operator $K$ such that $A\leq K\leq B$.

## §9. Invariant Subspaces for Normal Operators

Remember that we continue to assume that all Hilbert spaces are separable.

Every normal operator on a Hilbert space of dimension at least 2 has a nontrivial invariant subspace. This is an easy consequence of the Spectral Theorem. Indeed, if $N=\int z\,dE(z)$, $E(\Delta)\mathcal H$ is a reducing subspace for every Borel set $\Delta$.

If $A\in\mathcal B(\mathcal H)$, $\mathcal M$ is a linear subspace of $\mathcal H$, and $P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M$, then $\mathcal M$ reduces $A$ if and only if $P\in\{A\}'$. Also, $\mathcal M\in\operatorname{Lat}A$ (= the lattice of invariant subspaces for $A$) if and only if $AP=PAP$. Since the spectral projections of a normal operator belong to $W^*(N)$, they are even more than reducing.

**9.1. Definition.** An operator $A$ is *reductive* if every invariant subspace for $A$ reduces $A$. Equivalently, $A$ is reductive if and only if $\operatorname{Lat}A\subseteq\operatorname{Lat}A^*$.

Thus, every self-adjoint operator is reductive. Every normal operator on a finite dimensional space is reductive. More generally, every normal compact operator is reductive (Andô [1963]). However, the bilateral shift is not reductive. Indeed, if $U$ is the bilateral shift on $\ell^2(\mathbb Z)$, $\mathcal H=\{f\in\ell^2(\mathbb Z):f(n)=0$



<a id="pdf-page-306"></a>
if $n<0\}\in\operatorname{Lat}U$, but $\mathcal H\notin\operatorname{Lat}U^*$. Wermer [1952] first studied reductive normal operators and characterized the reductive unitary operators. A first step towards characterizing the reductive normal operators will be taken here. The final step has been taken but it will not be viewed in this book. The result is due to Sarason [1972]. Also see Conway [1981], §VII.5.

**9.2. Definition.** If $\mu$ is a compactly supported measure on $\mathbb C$, $P^\infty(\mu)$ denotes the weak* closure of the polynomials in $L^\infty(\mu)$.

Because the support of $\mu$ is compact, every polynomial, when restricted to that support, belongs to $L^\infty(\mu)$.

For any operator $A$, let $W(A)$ denote the WOT closed subalgebra of $\mathcal B(\mathcal H)$ generated by $A$; that is, $W(A)$ is the WOT closure in $\mathcal B(\mathcal H)$ of the polynomials in $A$. The next result is an immediate consequence of The Functional Calculus for Normal Operators.

**9.3. Theorem.** *If $N$ is a normal operator and $\mu$ is a scalar-valued spectral measure for $N$, then the functional calculus, when restricted to $P^\infty(\mu)$, is an isometric isomorphism $\rho:P^\infty(\mu)\to W(N)$ and a weak*-WOT homeomorphism. Also, $\rho(z)=N$.*

**9.4. Definition.** An operator $A$ is *reflexive* if whenever $B\in\mathcal B(\mathcal H)$ and $\operatorname{Lat}A\subseteq\operatorname{Lat}B$, then $B\in W(A)$.

It is easy to see that if $B\in W(A)$, then $\operatorname{Lat}A\subseteq\operatorname{Lat}B$ (Exercise). An operator is reflexive precisely when it has sufficiently many invariant subspaces to characterize $W(A)$. For a survey of reflexive operators and some related topics, see Radjavi and Rosenthal [1973].

**9.5. Theorem.** (Sarason [1966].) *Every normal operator is reflexive.*

**Proof.** Suppose $N$ is normal and $\operatorname{Lat}N\subseteq\operatorname{Lat}A$. If $P$ is a projection in $\{N\}'$, then $P\mathcal H$ and $(P\mathcal H)^\perp\in\operatorname{Lat}N\subseteq\operatorname{Lat}A$, so $AP=PA$. By Corollary 6.5, $A\in W^*(N)$. Let $\mu$ be a scalar-valued spectral measure for $N$. By Theorem 8.10, there is a $\phi$ in $L^\infty(\mu)$ such that $A=\phi(N)$. By Theorem 9.3, it must be shown that $\phi\in P^\infty(\mu)$.

Now let’s focus our attention on a special case. Assume that $N$ is *-cyclic; thus $N=N_\mu$. Suppose $f\in L^1(\mu)$ and $\int f\psi\,d\mu=0$ for every $\psi$ in $P^\infty(\mu)$. If it can be shown that $\int f\phi\,d\mu=0$, then the Hahn–Banach Theorem implies that $\phi\in P^\infty(\mu)$. This is the strategy we follow. Let $f=g\bar h$ for some $g,h$ in $L^2(\mu)$. Put $\mathcal M=\bigvee\{z^kg:k\geqslant0\}$. Clearly $\mathcal M\in\operatorname{Lat}N$, so $\mathcal M\in\operatorname{Lat}A=\operatorname{Lat}\phi(N)=\operatorname{Lat}M_\phi$. Hence $\phi g\in\mathcal M$. But $0=\int z^kf\,d\mu=\int z^kg\bar h\,d\mu=\langle N^kg,h\rangle$ for all $k\geqslant0$; hence $h\perp\mathcal M$. Thus $0=\langle\phi g,h\rangle=\int\phi g\bar h\,d\mu=\int\phi f\,d\mu$, and $\phi\in P^\infty(\mu)$.

Now we return to the general case. By (7.9) and (8.9) there is a separating vector $e$ for $W^*(N)$ such that $\mu(\Delta)=\|E(\Delta)e\|^2$, where $N=\int z\,dE(z)$. Let



<a id="pdf-page-307"></a>
$\mathcal K=\bigvee\{N^{*k}N^je:k,j\geq 0\}$. Clearly $\mathcal K$ reduces $N$ and $N|_{\mathcal K}$ is $*$-cyclic. Hence $\mathcal K$ reduces $A$ and $A|_{\mathcal K}=\phi(N|_{\mathcal K})$. By the preceding paragraph $\phi\in P^\infty(\mu)$. $\blacksquare$

An immediate consequence of the preceding theorem is the first step in the characterization of reductive normal operators.

**9.6. Corollary.** *If $N$ is a normal operator and $\mu$ is a scalar-valued spectral measure for $N$, then $N$ is reductive if and only if $P^\infty(\mu)=L^\infty(\mu)$.*

**PROOF.** If $\mathcal M\in\operatorname{Lat}N$, then $\mathcal M\in\operatorname{Lat}\phi(N)$ for every $\phi$ in $P^\infty(\mu)$. So if $P^\infty(\mu)=L^\infty(\mu)$, $\bar z\in P^\infty(\mu)$ and, hence, $\mathcal M\in\operatorname{Lat}N^*$ whenever $\mathcal M\in\operatorname{Lat}N$.

Now suppose $N$ is reductive. This means that $\operatorname{Lat}N\subseteq\operatorname{Lat}N^*$. By the preceding theorem, this implies $N^*\in W(N)$; equivalently, $\bar z\in P^\infty(\mu)$. Since $P^\infty(\mu)$ is an algebra, every polynomial in $z$ and $\bar z$ belongs to $P^\infty(\mu)$. By taking weak* limits this implies that $P^\infty(\mu)=L^\infty(\mu)$. $\blacksquare$

The preceding corollary fails to be a good characterization of reductive normal operators since it only says that one difficult problem is equivalent to another. A way is needed to determine when $P^\infty(\mu)=L^\infty(\mu)$. This is what was done in Sarason [1972].

Are there any reductive operators that are not normal? This natural and seemingly innocent question has much more to it than meets the eye. Dyer, Pedersen, and Porcelli [1972] have shown that this question has an affirmative answer if and only if every operator on a Hilbert space has a nontrivial invariant subspace.

## EXERCISES

1. (Andô [1963].) Use Corollary 9.6 to show that every compact normal operator is reductive.

2. Determine all of the invariant subspaces of a compact normal operator.

3. (Andô [1963].) Show that every reductive compact operator is normal. (Also see Rosenthal [1968].)

4. Show that an operator $A$ is reductive if and only if $\operatorname{Lat}A=\operatorname{Lat}A^*$.

5. Let $N$ be a normal operator on a Hilbert space $\mathcal H$, let $\mathcal R$ be an invariant subspace for $N$, and let $S=N|_{\mathcal R}$. Show that $S$ is normal if and only if $\mathcal R$ is a reducing subspace for $N$.

6. Let $\mu$ be a compactly supported regular Borel measure on $\mathbb C$ and let $P^2(\mu)$ denote the closure in $L^2(\mu)$ of the analytic polynomials; that is, $P^2(\mu)$ is the closed linear span of $\{z^n:n\geq 0\}$. Show that $P^2(\mu)$ is invariant for $N_\mu$ and that $N_\mu|_{P^2(\mu)}$ is normal if and only if $P^2(\mu)=L^2(\mu)$.

7. With the notation of Exercise 6, show that if $\mathcal R$ is a reducing subspace for $N_\mu$ and $P^2(\mu)\subseteq\mathcal R$, then $\mathcal R=L^2(\mu)$.


<a id="pdf-page-308"></a>
§10. Multiplicity Theory for Normal Operators  293

## §10. Multiplicity Theory for Normal Operators: A Complete Set of Unitary Invariants

<!-- BEGIN BACKGROUND BG-IX.block6 -->
<a id="bg-ix-8"></a>
### Lemma BG-IX.8 — Replacing absolute continuity by restriction to a set

For finite positive measures $\nu\ll\mu$, let $w=d\nu/d\mu$ and $\Delta=\{w>0\}$. Then $\nu$ and $\mu|_\Delta$ have the same null sets. If $\nu_{n+1}\ll\nu_n\ll\mu$, the corresponding sets can be chosen decreasing modulo null sets.

**Proof.** $\nu(E)=\int_{E\cap\Delta}w\,d\mu$ vanishes exactly when $\mu(E\cap\Delta)=0$: for the nontrivial implication, intersect with $\{w\geq1/k\}$ and take their countable union. If $\Delta_n=\{d\nu_n/d\mu>0\}$, absolute continuity implies $\mu(\Delta_{n+1}\setminus\Delta_n)=0$. Replacing $\Delta_n$ by $\bigcap_{j\leq n}\Delta_j$ produces genuinely decreasing representatives without changing measure classes. $\square$

Multiplicity records how many copies of the multiplication space occur on these measurable pieces, not simply the number of points in a fiber of a chosen scalar function. Countable null-set changes do not alter any $L^2$ model.
<!-- END BACKGROUND BG-IX.block6 -->

Throughout this section only separable Hilbert spaces are considered.

When are two normal operators unitarily equivalent? The answer to this question must be given in the following way: to each normal operator we must attach a collection of objects such that two normal operators are unitarily equivalent if and only if the two collections are equal (or equivalent). Furthermore, it should be easier to verify that these collections are equivalent than to verify that the normal operators are equivalent. This is contained in the following result due to Hellinger [1907]. Note that it generalizes Theorem 3.6.

**10.1. Theorem.** (a) *If $N$ is a normal operator, then there is a sequence (possibly finite) of measures $\{\mu_n\}$ on $\mathbb C$ such that $\mu_{n+1}\ll\mu_n$ for all $n$ and*

$$
\tag*{10.2}
N\cong N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots.
$$

(b) *If $N$ and $\{\mu_n\}$ are as in (a) and $M\cong N_{\nu_1}\oplus N_{\nu_2}\oplus\cdots$, where $\nu_{n+1}\ll\nu_n$ for all $n$, then $N\cong M$ if and only if $[\mu_n]=[\nu_n]$ for all $n$.*

The proof of this theorem requires several lemmas. Before beginning, we will examine a couple of false starts for a proof. This will cause us to arrive at the correct strategy for a proof and show us the necessity for some of the lemmas.

Let $N=\int z\,dE(z)$. If $e\in\mathcal H$ and $\mathcal H_e=\operatorname{cl}[W^*(N)e]$, then $N|\mathcal H_e$ is a $*$-cyclic normal operator. An application of Zorn’s Lemma and the separability of $\mathcal H$ produces a maximal sequence $\{e_n\}$ in $\mathcal H$ such that $\mathcal H_{e_n}\perp\mathcal H_{e_m}$. By the maximality of $\{e_n\}$, $\mathcal H=\bigoplus_n\mathcal H_{e_n}$. If $N_n=N|\mathcal H_{e_n}$, $N_n=N_{\mu_n}$, where $\mu_n(\Delta)=\|E(\Delta)e_n\|^2$; thus $N\cong\bigoplus_nN_{\mu_n}$. The trouble here is that $\mu_{n+1}$ is not necessarily absolutely continuous with respect to $\mu_n$. Just using Zorn’s Lemma to produce the sequence $\{\mu_n\}$ eliminates any possibility of having $\{\mu_n\}$ canonical and producing the unitary invariant desired for normal operators. Let’s try again.

Note that if $\mu_{n+1}\ll\mu_n$ for all $n$ in (10.2), then $\mu_n\ll\mu_1$ for all $n$. This in turn implies that $\mu_1$ is a scalar-valued spectral measure for $N$. Using Lemma 8.6 we are thus led to choose $\mu_1$ as follows. Let $e_1$ be a separating vector for $W^*(N)$; this exists by Corollary 7.9 and the separability of $\mathcal H$. Put $\mu_1(\Delta)=\|E(\Delta)e_1\|^2$. If $\mathcal H_1=\operatorname{cl}[W^*(N)e_1]$. then $N|\mathcal H_1\cong N_{\mu_1}$. Let $N_2\equiv N|\mathcal H_1^\perp$; so $N_2$ is normal. A pair of easy exercises shows that the spectral measure $E_2$ for $N_2$ is given by $E_2(\Delta)=E(\Delta)|\mathcal H_1^\perp$ and $W^*(N_2)=W^*(N)|\mathcal H_1^\perp$ $(\equiv\{A\in\mathcal B(\mathcal H_1^\perp):A=T|\mathcal H_1^\perp\text{ for some }T\text{ in }W^*(N)\})$. Let $e_2$ be a separating vector for $W^*(N_2)$ and put $\mu_2(\Delta)=\|E_2(\Delta)e_2\|^2$. By the easy exercises above, $\mu_2(\Delta)=\|E(\Delta)e_2\|^2$, so that $\mu_2\ll\mu_1$, and $\mathcal H_2\equiv\operatorname{cl}[W^*(N)e_2]=\operatorname{cl}[W^*(N_2)e_2]\leqslant\mathcal H_1^\perp$. Also, $N|\mathcal H_2\cong N_{\mu_2}$.



<a id="pdf-page-309"></a>
Continuing in this way produces a sequence of vectors $\{e_n\}$ such that if $\mathcal H_n=\operatorname{cl}[W^*(N)e_n]$ and $\mu_n(\Delta)=\|E(\Delta)e_n\|^2$, then $\mathcal H_n\perp\mathcal H_m$ for $n\ne m$, $\mu_{n+1}\ll\mu_n$, and $N\mid\mathcal H_n\cong N_{\mu_n}$. The difficulty here is that $\mathcal H$ is not necessarily equal to $\bigoplus_n\mathcal H_n$ so that $N$ and $\bigoplus_n N_{\mu_n}$ cannot be proved to be unitarily equivalent. (Actually, $N$ and $\bigoplus_n N_{\mu_n}$ are unitarily equivalent, but to show this we need the force of Theorem 10.1. See Exercise 2.) The following provides us with a look at an example to see what can go wrong.

**10.3. Example.** For $n\geqslant 1$ let $\mu_n=$ Lebesgue measure on $[0,1+2^{-n}]$ and let $\mu_\infty=$ Lebesgue measure on $[0,1]$. Put $N=\bigoplus_{n=1}^{\infty}N_{\mu_n}\oplus N_{\mu_\infty}$. If the process of the preceding paragraph is followed, it might be that vectors $\{e_n\}$ that are chosen are the vectors with a 1 in the $L^2(\mu_n)$ coordinate and zeros elsewhere. Thus the spaces $\{\mathcal H_n\}$ are precisely the spaces $\{L^2(\mu_n)\}$ and $[\bigoplus_1^\infty\mathcal H_n]^\perp=L^2(\mu_\infty)$.

(Nevertheless, $N\cong\bigoplus_1^\infty N_{\mu_n}$. Indeed, let $\nu_n=\mu_n|[1,1+2^{-n}]$; so $\mu_n=\mu_\infty+\nu_n$ and $\mu_\infty\perp\nu_n$. Thus $N_{\mu_n}\cong N_{\nu_n}\oplus N_{\mu_\infty}$. Therefore

$$
\begin{aligned}
N&=\bigoplus_1^\infty N_{\mu_n}\oplus N_{\mu_\infty}\\
&\cong\bigoplus_1^\infty N_{\nu_n}\oplus N_{\mu_\infty}^{(\infty)}\oplus N_{\mu_\infty}\\
&\cong\bigoplus_1^\infty N_{\nu_n}\oplus N_{\mu_\infty}^{(\infty)}\\
&\cong\bigoplus_1^\infty N_{\mu_n}.)
\end{aligned}
$$

After an examination of the statement of Theorem 10.1, it becomes clear that some procedure like the one outlined in the paragraph preceding Example 10.3 should be used. It only becomes necessary to modify this procedure so that the vectors $\{e_n\}$ can be chosen in such a way that $\mathcal H=\bigoplus_1^\infty\mathcal H_n$. For example, let, as above, $e_1$ be a separating vector for $W^*(N)$ and let $\{f_n\}$ be an orthonormal basis for $\mathcal H$ such that $f_1=e_1$. We now want to choose the vectors $\{e_n\}$ such that $\{f_1,\ldots,f_n\}\subseteq\mathcal H_1\oplus\cdots\oplus\mathcal H_n$. In this way we will meet success. The vital link here is the next result.

**10.4. Proposition.** *If $N$ is a normal operator on $\mathcal H$ and $e\in\mathcal H$, then there is a separating vector $e_0$ for $W^*(N)$ such that $e\in\operatorname{cl}[W^*(N)e_0]$.*

**Proof.** Let $f_0$ be any separating vector for $W^*(N)$, let $E$ be the spectral measure for $N$, let $\mu(\Delta)=\|E(\Delta)f_0\|^2$, and put $\mathcal G=\operatorname{cl}[W^*(N)f_0]$. Write $e=g_1+h_1$, where $g_1\in\mathcal G$ and $h_1\in\mathcal G^\perp$.

Let $\eta(\Delta)=\|E(\Delta)h_1\|^2$ and let $\mathcal L=\operatorname{cl}[W^*(N)h_1]$. Hence $\eta\ll\mu$, $N$ is reduced by both $\mathcal L$ and $\mathcal G$, and $\mathcal L\perp\mathcal G$. Moreover, $N\mid\mathcal G\cong N_\mu$ and $N\mid\mathcal L\cong N_\eta$. Now the fact that $\eta\ll\mu$ implies that there is a Borel set $\Delta$ such that $[\eta]=[\mu|\Delta]$. (Why?) Hence $N\mid\mathcal L\cong N_\nu$ if $\nu=\mu|\Delta$ (Theorem 3.6). Let $U:\mathcal G\oplus\mathcal L\to L^2(\mu)\oplus L^2(\nu)$ be an isomorphism such that $U((0)\oplus\mathcal L)\subseteq(0)\oplus L^2(\nu)$ and $U(N\mid\mathcal G\oplus\mathcal L)U^{-1}=N_\mu\oplus N_\nu$. Since $e=g_1+h_1\in\mathcal G\oplus\mathcal L$, let $Ue=g\oplus h$. Because $h_1$ is a $*$-cyclic vector for $N\mid\mathcal L$, $h(z)\ne0$ a.e. $[\nu]$.

This reduces the proof of this proposition to proving the next lemma. $\blacksquare$



<a id="pdf-page-310"></a>
**10.5. Lemma.** *Let $\mu$ be a compactly supported measure on $\mathbb C$, $\Delta$ a Borel subset of the support of $\mu$, and put $\nu=\mu|_\Delta$. If $N=N_\mu\oplus N_\nu$ on $L^2(\mu)\oplus L^2(\nu)$ and $g\oplus h\in L^2(\mu)\oplus L^2(\nu)$ such that $h(z)\ne0$ a.e. $[\nu]$, then there is an $f$ in $L^2(\mu)$ such that $f\oplus h$ is a separating vector for $W^*(N)$ and $g\oplus h\in\operatorname{cl}[W^*(N)(f\oplus h)]$.*

**Proof.** Define $f(z)=g(z)$ for $z$ in $\Delta$ and $f(z)=1$ for $z$ not in $\Delta$. Put $\mathcal H=\operatorname{cl}[W^*(N)(f\oplus h)]=\operatorname{cl}\{\phi f\oplus\phi h:\phi\in L^\infty(\mu)\}$ since $\mu$ is a scalar-valued spectral measure for $N$. If $\Delta'$ is the complement of $\Delta$, then note that $\phi\chi_{\Delta'}\oplus0=\phi\chi_{\Delta'}(f\oplus h)\in\mathcal H$ for all $\phi$ in $L^\infty(\mu)$. Hence $L^2(\mu|_{\Delta'})\oplus0\subseteq\mathcal H$. This implies that $(1-g)\chi_{\Delta'}\oplus0\in\mathcal H$, so $g\oplus h=f\oplus h-(1-g)\chi_{\Delta'}\oplus0\in\mathcal H$.

On the other hand, if $\phi\in L^\infty(\mu)$ and $0=\phi f\oplus\phi h$, then $\phi f=\phi h=0$ a.e. $[\mu]$. Since $h(z)\ne0$ a.e. $[\nu]$, $\phi(z)=0$ a.e. $[\mu]$ on $\Delta$. But for $z$ in $\Delta'$, $f(z)=1$; hence $\phi(z)=0$ a.e. $[\mu]$ on $\Delta'$. Thus, $f\oplus h$ is a separating vector for $W^*(N)$. $\blacksquare$

**Proof of Theorem 10.1 (a):** Let $e_1$ be a separating vector for $W^*(N)$ and let $\{f_n\}$ be an orthonormal basis for $\mathcal H$ such that $f_1=e_1$. Put $\mathcal H_1=\operatorname{cl}[W^*(N)e_1]$, $\mu_1(\Delta)=\|E(\Delta)e_1\|^2$, and $N_2=N|_{\mathcal H_1^\perp}$. Let $f'_2$ be the orthogonal projection of $f_2$ onto $\mathcal H_1^\perp$. By Proposition 10.4 there is a separating vector $e_2$ for $W^*(N_2)$ such that $f'_2\in\operatorname{cl}[W^*(N_2)e_2]\equiv\mathcal H_2$. Note that $\mathcal H_2=\operatorname{cl}[W^*(N)e_2]$ and $\{f_1,f_2\}\subseteq\mathcal H_1\oplus\mathcal H_2$. Put $\mu_2(\Delta)=\|E(\Delta)e_2\|^2$. Now continue by induction. $\blacksquare$

Now for part (b) of Theorem 10.1. If $[\mu_n]=[\nu_n]$ (the notation is that of Theorem 10.1) for every $n$, then $N_{\mu_n}\cong N_{\nu_n}$ by Theorem 3.6. Therefore $N\cong M$. Thus it is the converse that causes difficulties. So assume that $N\cong M$. If $M\in\mathcal B(\mathcal K)$, $U:\mathcal H\to\mathcal K$ is an isomorphism such that $UNU^{-1}=M$, and $e_1$ is a separating vector for $W^*(N)$, then $Ue_1=f_1$ is easily seen to be a separating vector for $W^*(M)$. Since $\mu_1$ and $\nu_1$ are scalar-valued spectral measures for $N$ and $M$, respectively, it follows that $[\mu_1]=[\nu_1]$; thus $N_{\mu_1}\cong N_{\nu_1}$ by Theorem 3.6. However, here is the difficulty—the isomorphism that shows that $N_{\mu_1}\cong N_{\nu_1}$ may not be related to $U$; that is, if $\mathcal H=\bigoplus_n\mathcal H_n$, $\mathcal K=\bigoplus_n\mathcal K_n$, where $N|_{\mathcal H_n}\cong N_{\mu_n}$ and $M|_{\mathcal K_n}\cong N_{\nu_n}$, then $N|_{\mathcal H_1}\cong M|_{\mathcal K_1}$, but we do not know that $U\mathcal H_1=\mathcal K_1$. Thus we want to argue that because $N\cong M$ and $N|_{\mathcal H_1}\cong M|_{\mathcal K_1}$, then $N|_{\mathcal H_0^\perp}\cong M|_{\mathcal K_1^\perp}$. In this way we can prove (10.1.b) by induction. This step is justified by the following.

**10.6. Proposition.** *If $N$, $A$, and $B$ are normal operators, $N$ is $*$-cyclic, and $N\oplus A\cong N\oplus B$, then $A\cong B$.*

**Proof.** Let $N\in\mathcal B(\mathcal H)$, $A\in\mathcal B(\mathcal H_A)$, $B\in\mathcal B(\mathcal H_B)$, and let $U:\mathcal H\oplus\mathcal H_A\to\mathcal H\oplus\mathcal H_B$ be an isomorphism such that $U(N\oplus A)U^{-1}=N\oplus B$. Now $U$ can be written as a $2\times2$ matrix,

$$
U=\begin{bmatrix}
U_{11}&U_{12}\\
U_{21}&U_{22}
\end{bmatrix},
$$

where $U_{11}:\mathcal H\to\mathcal H$, $U_{12}:\mathcal H_A\to\mathcal H$, $U_{21}:\mathcal H\to\mathcal H_B$, $U_{22}:\mathcal H_A\to\mathcal H_B$.



<a id="pdf-page-311"></a>
Expressing $N\oplus A$ and $N\oplus B$ as

$$
\begin{bmatrix}N&0\\0&A\end{bmatrix}
\quad\text{and}\quad
\begin{bmatrix}N&0\\0&B\end{bmatrix}
$$

respectively, the equation $U(N\oplus A)=(N\oplus B)U$ becomes

$$
\begin{bmatrix}
U_{11}N&U_{12}A\\
U_{21}N&U_{22}A
\end{bmatrix}
=
\begin{bmatrix}
NU_{11}&NU_{12}\\
BU_{21}&BU_{22}
\end{bmatrix}.
\tag{10.7}
$$

Similarly, $U(N\oplus A)^*=(N\oplus B)^*U$ becomes

$$
\begin{bmatrix}
U_{11}N^*&U_{12}A^*\\
U_{21}N^*&U_{22}A^*
\end{bmatrix}
=
\begin{bmatrix}
N^*U_{11}&N^*U_{12}\\
B^*U_{21}&B^*U_{22}
\end{bmatrix}.
\tag{10.7*}
$$

Parts of the preceding equations will be referred to as $(10.7)_{ij}$ and $(10.7)_{ij}^*$, $i,j=1,2$.

An examination of the equation $U^*U=1$ and $UU^*=1$, written in matrix form, yields the equations

$$
\left.
\begin{aligned}
\text{(a)}\quad&U_{11}^*U_{12}+U_{21}^*U_{22}=0
&&(\text{on }\mathscr{H}_A)\\
\text{(b)}\quad&U_{11}U_{11}^*+U_{12}U_{12}^*=1
&&(\text{on }\mathscr{K})\\
\text{(c)}\quad&U_{21}U_{11}^*+U_{22}U_{12}^*=0
&&(\text{on }\mathscr{K}).
\end{aligned}
\right\}
\tag{10.8}
$$

Now equation $(10.7)_{22}$ and Proposition 6.10 imply that $(\ker U_{22})^\perp$ reduces $A$, $\operatorname{cl}(\operatorname{ran}U_{22})=(\ker U_{22}^*)^\perp$ reduces $B$, and

$$
A|(\ker U_{22})^\perp\cong B|(\ker U_{22}^*)^\perp.
\tag{10.9}
$$

What about $A|\ker U_{22}$ and $B|\ker U_{22}^*$? If they are unitarily equivalent, then $A\cong B$ and we are done. If $h\in\ker U_{22}\subseteq\mathscr{H}_A$, then

$$
\begin{bmatrix}U_{11}&U_{12}\\U_{21}&U_{22}\end{bmatrix}
\begin{bmatrix}0\\h\end{bmatrix}
=
\begin{bmatrix}U_{12}h\\0\end{bmatrix}.
$$

Since $U$ is an isometry, it follows that $U_{12}$ maps $\ker U_{22}$ isometrically onto a closed subspace of $\mathscr{K}$. Put $\mathcal{M}_1=U_{12}(\ker U_{22})$. Equations $(10.7)_{12}$ and $(10.7)_{12}^*$ and the fact that $\ker U_{22}$ reduces $A$ imply that $\mathcal{M}_1$ reduces $N$. Thus, the restriction of $U_{12}$ to $\ker U_{22}$ is the required isomorphism to show that

$$
A|\ker U_{22}\cong N|\mathcal{M}_1.
\tag{10.10}
$$

Similarly, $U_{21}^*$ maps $\ker U_{22}^*=(\operatorname{ran}U_{22})^\perp$ isometrically into $\mathcal{M}_2=U_{21}^*(\ker U_{22}^*)$, $\mathcal{M}_2$ reduces $N$, and

$$
B|\ker U_{22}^*\cong N|\mathcal{M}_2.
\tag{10.11}
$$

Note that if $\mathcal{M}_1=\mathcal{M}_2$, then (10.9), (10.10), and (10.11) show that $A\cong B$. Could it be that $\mathcal{M}_1$ and $\mathcal{M}_2$ are equal?

If $h\in\ker U_{22}$, then (10.8.a) implies that $U_{11}^*U_{12}h=-U_{21}^*U_{22}h=0$. Hence $\mathcal{M}_1=U_{12}(\ker U_{22})\subseteq\ker U_{11}^*$. On the other hand, if $f\in\ker U_{11}^*$, then (10.8.b) implies $f=(U_{11}U_{11}^*+U_{12}U_{12}^*)f=U_{12}U_{12}^*f$. But by (10.8.c), $U_{22}U_{12}^*f=-$



<a id="pdf-page-312"></a>
$U_{21}U_{11}^{*}f=0$, so $U_{12}^{*}f\in\ker U_{22}$. Hence $f\in U_{12}(\ker U_{22})$. Thus

$$
\mathcal M_1=\ker U_{11}^{*}.
$$

Similarly,

$$
\mathcal M_2=\ker U_{11}.
$$

Until this point we have not used the fact that $N$ is *-cyclic. Equation $(10.7)_{11}$ implies that $U_{11}\in\{N'\}'$. By Theorem 3.4 and Corollary 6.9 this implies that $U_{11}$ is normal. Hence, $\ker U_{11}^{*}=\ker U_{11}$, or $\mathcal M_1=\mathcal M_2$. $\blacksquare$

If the hypothesis in the preceding proposition that $N$ is *-cyclic is deleted, the conclusion is no longer valid. For example, let $N$ and $A$ be the identities on separable infinite dimensional spaces and let $B$ be the identity on a finite dimensional space. Then $N\oplus A\cong N\oplus B$, but $A$ and $B$ are not equivalent. However, the requirement that $N$ be *-cyclic can be replaced by another, even when $N$, $A$, and $B$ are not assumed to be normal. For the details see Kadison and Singer [1957].

The proof of Theorem 10.1(b) is now a straightforward argument as outlined before the statement of Proposition 10.6. The details are left to the reader.

If $\mu$ and $\nu$ are measures and $\nu\ll\mu$, then there is a Borel set $\Delta$ such that $[\nu]=[\mu|_\Delta]$. Using this fact, Theorem 10.1 can be restated as follows.

**10.12. Corollary.** (a) If $N$ is a normal operator with scalar-valued spectral measure $\mu$, then there is a decreasing sequence $\{\Delta_n\}$ of Borel subsets of $\sigma(N)$ such that $\Delta_1=\sigma(N)$ and

$$
N\cong N_\mu\oplus N_{\mu|_{\Delta_2}}\oplus N_{\mu|_{\Delta_3}}\oplus\cdots.
$$

(b) If $M$ is another normal operator with scalar-valued spectral measure $\nu$ and if $\{\Sigma_n\}$ is a decreasing sequence of Borel subsets of $\sigma(M)$ such that $M\cong N_\nu\oplus N_{\nu|_{\Sigma_2}}\oplus N_{\nu|_{\Sigma_3}}\oplus\cdots$, then $N\cong M$ if and only if (i) $[\mu]=[\nu]$ and (ii) $\mu(\Delta_n\setminus\Sigma_n)=0=\mu(\Sigma_n\setminus\Delta_n)$ for all $n$.

**10.13. Example.** Let $\mu$ be Lebesgue measure on $[0,1]$ and let $\mu_n$ be Lebesgue measure on $[1/(n+1),1/n]$ for $n\geqslant1$. (So $\mu=\sum\mu_n$.) Let $N=N_{\mu_1}\oplus N_{\mu_2}^{(2)}\oplus N_{\mu_3}^{(3)}\oplus\cdots$. The direct sum decomposition of $N$ that appears in Corollary 10.12 is obtained by letting $\Delta_n=[0,1/n]$, $n\geqslant1$. Then $N\cong N_\mu\oplus N_{\mu|_{\Delta_2}}\oplus N_{\mu|_{\Delta_3}}\oplus\cdots$.

What does Theorem 10.1 say for normal operators on a finite dimensional space? If $\dim\mathcal H<\infty$, there is an orthonormal basis $\{e_n\}$ for $\mathcal H$ consisting of eigenvectors for $N$. Observe that $N$ is *-cyclic if and only if each eigenvalue has multiplicity 1. So each summand that appears in (10.2) must operate on a subspace of $\mathcal H$ that contains only one basis element $e_n$ per eigenvalue. Moreover, since $\mu_1$ is a scalar-valued spectral measure for $N$, it must be that the first summand in (10.2) contains one basis element for each eigenvalue



<a id="pdf-page-313"></a>
for $N$. Thus, if $\sigma(N)=\{\lambda_1,\lambda_2,\ldots,\lambda_n\}$, where $\lambda_i\ne\lambda_j$ for $i\ne j$, then (10.2) becomes

$$
N\cong D_1\oplus D_2\oplus\cdots\oplus D_m, \tag{10.14}
$$

where $D_1=\operatorname{diag}(\lambda_1,\lambda_2,\ldots,\lambda_n)$ and, for $k\geq 2$, $D_k$ is a diagonalizable operator whose diagonal consists of one, and only one, of each of the eigenvalues of $N$ having multiplicity at least $k$.

There is another decomposition for normal operators that furnishes a complete set of unitary invariants and has a connection with the concept of multiplicity. For normal operators on a finite dimensional space, this decomposition takes on the following form.

Let $\Lambda_k=$ the eigenvalues of $N$ having multiplicity $k$. So for $\lambda$ in $\Lambda_k$, $\dim\ker(N-\lambda)=k$. If $\Lambda_k=\{\lambda_j^{(k)}:1\leq j\leq m_k\}$, let $N_k$ be the diagonalizable operator on a $km_k$ dimensional space whose diagonal contains each $\lambda_j^{(k)}$ repeated $k$ times. So $N\cong N_1\oplus N_2\oplus\cdots\oplus N_p$, if $\sigma(N)=\Lambda_1\cup\cdots\cup\Lambda_p$. Now $\sigma(N_k)=\Lambda_k$ and each eigenvalue of $N_k$ has multiplicity $k$. Thus $N_k\cong A_k^{(k)}$, where $A_k$ is a diagonalizable operator on an $m_k$ dimensional space with $\sigma(A_k)=\Lambda_k$. Thus

$$
N\cong A_1\oplus A_2^{(2)}\oplus\cdots\oplus A_p^{(p)}, \tag{10.15}
$$

and $\sigma(A_i)\cap\sigma(A_j)=\square$ for $i\ne j$.

Now the big advantage of the decomposition (10.15) is that it permits a discussion of $\{N\}'$. Because the spectra of the operators $A_k$ are disjoint,

$$
\{N\}'=\{N_1\}'\oplus\{N_2\}'\oplus\cdots\oplus\{N_p\}'.
$$

(Why?) If $\mathcal H_j^{(k)}=\ker(N-\lambda_j^{(k)})$, then $\dim\mathcal H_j^{(k)}=k$ and $\bigoplus_{j=1}^{m_k}\mathcal H_j^{(k)}=$ the domain of $N_k$. Since $\lambda_i^{(k)}\ne\lambda_j^{(k)}$ for $i\ne j$,

$$
\{N_k\}'=\mathcal B(\mathcal H_1^{(k)})\oplus\cdots\oplus\mathcal B(\mathcal H_{m_k}^{(k)}),
$$

and each $\mathcal B(\mathcal H_j^{(k)})$ is isomorphic to the $k\times k$ matrices.

The decomposition of an arbitrary normal operator that is analogous to decomposition (10.15) for finite dimensional normal operators is contained in the next result. The corresponding discussion of the commutant will follow this theorem.

**10.16. Theorem.** *If $N$ is a normal operator, then there are mutually singular measures $\mu_\infty,\mu_1,\mu_2,\ldots$ (some of which may be zero) such that*

$$
N\cong N_{\mu_\infty}^{(\infty)}\oplus N_{\mu_1}\oplus N_{\mu_2}^{(2)}\oplus\cdots.
$$

*If $M$ is another normal operator with corresponding measures $\nu_\infty,\nu_1,\nu_2,\ldots$, then $N\cong M$ if and only if $[\mu_n]=[\nu_n]$ for $1\leq n\leq\infty$.*

**Proof.** Let $\mu$ be a scalar-valued spectral measure for $N$ and let $\{\Delta_n\}$ be the sequence of Borel subsets of $\sigma(N)$ obtained in Corollary 10.12. Put $\Sigma_\infty=\bigcap_{n=1}^{\infty}\Delta_n$ and $\Sigma_n=\Delta_n\setminus\Delta_{n+1}$ for $1\leq n<\infty$; let $\mu_n=\mu|_{\Sigma_n}$, $1\leq n\leq\infty$. Put



<a id="pdf-page-314"></a>
$\nu_n=\mu|_{\Delta_n}$, $1\leq n<\infty$. Now $\Delta_n=\Sigma_\infty\cup(\Delta_n\setminus\Delta_{n+1})\cup(\Delta_{n+1}\setminus\Delta_{n+2})\cup\cdots=\Sigma_\infty\cup\Sigma_n\cup\Sigma_{n+1}\cup\cdots$. Hence $\nu_n=\mu_\infty+\mu_n+\mu_{n+1}+\cdots$ and the measures $\mu_\infty,\mu_n,\mu_{n+1},\ldots$ are pairwise singular. Hence $N_{\nu_n}\cong N_{\mu_\infty}\oplus N_{\mu_n}\oplus N_{\mu_{n+1}}\oplus\cdots$. Combining this with Corollary 10.12 gives

$$
\begin{aligned}
N
&\cong N_{\nu_1}\oplus N_{\nu_2}\oplus N_{\nu_3}\oplus\cdots\\
&\cong (N_{\mu_\infty}\oplus N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots)
 \oplus (N_{\mu_\infty}\oplus N_{\mu_2}\oplus N_{\mu_3}\oplus\cdots)\\
&\qquad\oplus (N_{\mu_\infty}\oplus N_{\mu_3}\oplus N_{\mu_4}\oplus\cdots)\oplus\cdots\\
&\cong N_{\mu_\infty}^{(\infty)}\oplus N_{\mu_1}\oplus N_{\mu_2}^{(2)}
 \oplus N_{\mu_3}^{(3)}\oplus\cdots.
\end{aligned}
$$

The proof of the uniqueness part of the theorem is left to the reader. $\blacksquare$

Note that the form of the normal operator presented in Example 10.13 is the form of the operator given in the conclusion of the preceding theorem.

Now to discuss $\{N\}'$. Fix a compactly supported positive Borel measure $\mu$ on $\mathbb C$ and let $\mathcal H_n$ be an $n$-dimensional Hilbert space, $1\leq n\leq\infty$. Define a function $f:\mathbb C\to\mathcal H_n$ to be a Borel function if $z\mapsto\langle f(z),g\rangle$ is a Borel function for each $g$ in $\mathcal H_n$. If $f:\mathbb C\to\mathcal H_n$ is a Borel function and $\{e_j\}$ is an orthonormal basis for $\mathcal H_n$, then $\|f(z)\|^2=\sum_j|\langle f(z),e_j\rangle|^2$, so $z\mapsto\|f(z)\|^2$ is a Borel function. Let $L^2(\mu;\mathcal H_n)$ be the space of all Borel functions $f:\mathbb C\to\mathcal H_n$ such that $\|f\|^2\equiv\int\|f(z)\|^2\,d\mu(z)<\infty$, where two functions agreeing a.e. $[\mu]$ are identified. If $f$ and $g\in L^2(\mu;\mathcal H_n)$, $\langle f,g\rangle\equiv\int\langle f(z),g(z)\rangle\,d\mu(z)$ defines an inner product on $L^2(\mu;\mathcal H_n)$. It is not difficult to show that $L^2(\mu;\mathcal H_n)$ is a Hilbert space.

**10.17. Proposition.** *If $N$ is multiplication by $z$ on $L^2(\mu;\mathcal H_n)$, then $N\cong N_\mu^{(n)}$.*

**Proof.** Let $\{e_j:1\leq j\leq n\}$ be an orthonormal basis for $\mathcal H_n$ and define $U:L^2(\mu;\mathcal H_n)\to L^2(\mu)^{(n)}$ by $Uf=(\langle f(\cdot),e_1\rangle,\langle f(\cdot),e_2\rangle,\ldots)$. Then $U$ is an isomorphism and $UNU^{-1}=N_\mu^{(n)}$. The details are left to the reader. $\blacksquare$

Combining the preceding proposition with Proposition 6.1(b), we can find $\{N\}'$; namely, $\{N_\mu^{(n)}\}'=$ all matrices $(T_{ij})$ on $\mathcal B(L^2(\mu)^{(n)})$ such that $T_{ij}\in\{N_\mu\}'$ for all $i,j$. By Corollary 6.9, $\{N_\mu^{(n)}\}'=$ matrices $(M_{\phi_{ij}})$ that belong to $\mathcal B(L^2(\mu)^{(n)})$, such that $\phi_{ij}\in L^\infty(\mu)$. Now the idea is to use Proposition 10.17 to bring this back to $\mathcal B(L^2(\mu;\mathcal H_n))$ and describe $\{N\}'$.

A function $\phi:\mathbb C\to\mathcal B(\mathcal H_n)$ is defined to be a Borel function if for each $f$ and $g$ in $\mathcal H_n$, $z\mapsto\langle\phi(z)f,g\rangle$ is a Borel function. If $\{f_j\}$ is a countable dense subset of the unit ball of $\mathcal H_n$, $\|\phi(z)\|=\sup\{|\langle\phi(z)f_i,f_j\rangle|:1\leq i,j<\infty\}$, so $z\mapsto\|\phi(z)\|$ is a Borel function. Let $L^\infty(\mu;\mathcal B(\mathcal H_n))$ be the equivalence classes of bounded Borel functions from $\mathbb C$ into $\mathcal B(\mathcal H_n)$ furnished with the $\mu$-essential supremum norm.

If $\phi\in L^\infty(\mu;\mathcal B(\mathcal H_n))$ and $f\in L^2(\mu;\mathcal H_n)$, let $f(z)=\sum_j f_j(z)e_j$, where $\{e_j\}$ is an orthonormal basis for $\mathcal H_n$ and $f_j(z)=\langle f(z),e_j\rangle$, so $\sum_j|f_j(z)|^2=\|f(z)\|^2$. Thus $\phi(z)f(z)=\sum_j f_j(z)\phi(z)e_j$. So for any $e$ in $\mathcal H_n$, $\langle\phi(z)f(z),e\rangle=\sum_j f_j(z)\langle\phi(z)e_j,e\rangle$ is a Borel function. It is easy to check that $\phi f\in L^2(\mu;\mathcal H_n)$ and



<a id="pdf-page-315"></a>
$\|\phi f\|\leq\|\phi\|_\infty\|f\|$. Let $M_\phi:L^2(\mu;\mathcal H_n)\to L^2(\mu;\mathcal H_n)$ be defined by $M_\phi f=\phi f$. Combined with the preceding remarks, the following result can be shown to hold. (The proof is left to the reader.)

**10.18. Proposition.** *If $N$ is multiplication by $z$ on $L^2(\mu;\mathcal H_n)$, then*

$$
\{N\}'=\{M_\phi:\phi\in L^\infty(\mu;\mathcal B(\mathcal H_n))\}.
$$

*Also, $\|M_\phi\|=\|\phi\|_\infty$ for every $\phi$ in $L^\infty(\mu;\mathcal B(\mathcal H_n))$.*

The next lemma is a consequence of Proposition 6.10 and the fact that unitarily equivalent normal operators have mutually absolutely continuous scalar-valued spectral measures.

**10.19. Lemma.** *If $N_1$ and $N_2$ are normal operators with mutually singular scalar spectral measures and $XN_1=N_2X$, then $X=0$.*

Using the observation made prior to Corollary 6.8, the preceding lemma implies that $\{N_1\oplus N_2\}'=\{N_1\}'\oplus\{N_2\}'$ whenever $N_1$ and $N_2$ are as in the lemma.

The next theorem of this section can be proved by piecing together Theorem 10.16 and the remaining results of this section. The details are left to the reader.

**10.20. Theorem.** *If $N$ is a normal operator on $\mathcal H$, there are mutually singular measures $\mu_\infty,\mu_1,\mu_2,\ldots$ and an isomorphism*

$$
U:\mathcal H\to L^2(\mu_\infty;\mathcal H_\infty)\oplus L^2(\mu_1)\oplus L^2(\mu_2;\mathcal H_2)\oplus\cdots
$$

*such that*

$$
UNU^{-1}=N_\infty\oplus N_1\oplus N_2\oplus\cdots
$$

*where $N_n=$ multiplication by $z$ on $L^2(\mu_n;\mathcal H_n)$. Also,*

$$
\begin{aligned}
\{N_\infty\oplus N_1\oplus N_2\oplus\cdots\}'
={}&L^\infty(\mu_\infty;\mathcal B(\mathcal H_\infty))\oplus L^\infty(\mu_1)\\
&\oplus L^\infty(\mu_2;\mathcal B(\mathcal H_2))\oplus\cdots.
\end{aligned}
$$

Using the notation of the preceding theorem, if $\mu$ is a scalar-valued spectral measure for $N$, then there are pairwise disjoint Borel sets $\Delta_\infty,\Delta_1,\ldots$ such that $[\mu_n]=[\mu|_{\Delta_n}]$. Define a function $m_N:\mathbb C\to\{0,1,\ldots,\infty\}$ by letting $m_N=\infty\chi_{\Delta_\infty}+\chi_{\Delta_1}+2\chi_{\Delta_2}+\cdots$. As it stands the definition of $m_N$ depends on the choice of the sets $\{\Delta_n\}$ as well as $N$. However, any two choices of the sets $\{\Delta_n\}$ differ from one another by sets of $\mu$-measure zero. The function $m_N$ is called the *multiplicity function* for $N$. Note that $m_N$ is a Borel function.

If $m:\mathbb C\to\{\infty,0,1,2,\ldots\}$ is a Borel function and $\mu$ is a compactly supported measure such that $\mu(\{z:m(z)=0\})=0$, let $\Delta_n=\{z:m(z)=n\}$, $n=\infty,1,2,\ldots$. If $N_n=N_{\mu|_{\Delta_n}}$, then $N=N_\infty^{(\infty)}\oplus N_1\oplus N_2^{(2)}\oplus\cdots$ is a normal operator whose spectral measure is $\mu$ and whose multiplicity function agrees with $m$ a.e. $[\mu]$.



<a id="pdf-page-316"></a>
**10.21. Theorem.** *Two normal operators are unitarily equivalent if and only if they have the same scalar-valued spectral measure $\mu$ and their multiplicity functions are equal a.e. $[\mu]$.*

There is some notation that is used by many and we should mention its connection with what we have just finished. Suppose $m:\mathbb C\to\{\infty,1,2,\ldots\}$ is a Borel function and $\mu$ is a compactly supported measure on $\mathbb C$ such that $\mu(\{z:m(z)=0\})=0$. If $z\in\mathbb C$ let $\mathcal H(z)$ be a Hilbert space of dimension $m(z)$. The *direct integral* of the spaces $\mathcal H(z)$, denoted by $\int\mathcal H(z)\,d\mu(z)$, is precisely the space

$$
L^2(\mu|_{\Delta_\infty};\mathcal H_\infty)
\oplus L^2(\mu|_{\Delta_1})
\oplus L^2(\mu|_{\Delta_2};\mathcal H_2)
\oplus\cdots,
$$

where $\Delta_n=\{z:m(z)=n\}$ and $\dim\mathcal H_n=n$. If $\phi:\mathbb C\to\mathcal B(\mathcal H_\infty)\cup\mathcal B(\mathbb C)\cup\mathcal B(\mathcal H_2)\cup\cdots$ such that $\phi(z)\in\mathcal B(\mathcal H_n)$ when $z\in\Delta_n$, $\phi:\Delta_n\to\mathcal B(\mathcal H_n)$ is a Borel function, and there is a constant $M$ such that $\|\phi(z)\|\leq M$ a.e. $[\mu]$, then $\int\phi(z)\,d\mu(z)$ denotes the operator $M_{\phi|_{\Delta_\infty}}\oplus\cdots$ as in (10.20). Although the direct integral notation is quite suggestive, one must revert to the notation of (10.20) to produce proofs.

**Remarks.** There are several sources for multiplicity theory. Most begin by proving Theorem 10.16. This is done for nonseparable spaces in Halmos [1951] and Brown [1974]. Another source is Arveson [1976], where the theory is set in the context of $C^*$-algebras which is its proper milieu. Also, Arveson shows that the theory can be applied to some non-normal operators. The details of this more general multiplicity theory are carried out in Ernest [1976] as part of a more general classification scheme. Another source for multiplicity theory is Dunford and Schwartz [1963].

By Theorem 4.6, every normal operator is unitarily equivalent to a multiplication operator $M_\phi$ on $L^2(X,\Omega,\mu)$ for some measure space $(X,\Omega,\mu)$. The scalar-valued spectral measure for $M_\phi$ is $\mu\circ\phi^{-1}$. What is the multiplicity function for $M_\phi$? One is tempted to say that $m_{M_\phi}(z)=$ the number of points in $\phi^{-1}(z)$. This is not quite correct. The answer can be found in Abrahamse and Kriete [1973]. Also, Abrahamse [1978] contains a survey of spectral multiplicity for normal operators treated from this point of view. An especially accessible and readable account of this can be found in Kriete [1986].

## EXERCISES

1. Let $A$ and $B$ be operators on $\mathcal H$ and $\mathcal K$, respectively. Let $\mathcal H_0$ and $\mathcal K_0$ be reducing subspaces for $A$ and $B$ and suppose that $A\cong B|_{\mathcal K_0}$ and $B\cong A|_{\mathcal H_0}$. Show that $A\cong B$.

2. Let $\mu_1,\mu_2,\ldots$ be compactly supported measures on $\mathbb C$ such that $\mu_{n+1}\ll\mu_n$ for all $n$. Show that if $M$ is any normal operator whose spectral measure is absolutely continuous with respect to each $\mu_n$, then
   $$
   N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots
   \cong (N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots)\oplus M.
   $$



   <a id="pdf-page-317"></a>
3. If $\mu=$ Lebesgue measure on $[0,1]$, show that $N_\mu\cong N_\mu^p$ for $0<p<\infty$.

4. Let $\mu=$ Lebesgue measure on $[0,1]$ and characterize the functions $\phi$ in $L^\infty(\mu)$ such that $N_\mu\cong\phi(N_\mu)$.

5. Let $\mu=$ area measure on $\mathbb D$ and show that $N_\mu$ and $N_\mu^2$ are not unitarily equivalent.

6. Let $\mu=$ Lebesgue measure on $[0,1]$ and let $\nu=$ Lebesgue measure on $[-1,1]$. Show that $N_\nu^2\cong N_\mu\oplus N_\mu$. How about $N_\nu^3$?

7. Let $\mu$ be Lebesgue measure on $\mathbb R$ and $N=$ multiplication by $\sin x$ on $L^2(\mu)$. Find the decompositions of $N$ obtained in Theorem 10.1 and 10.16.

8. If $\mu$ is Lebesgue measure on $\mathbb R$ and $N=$ multiplication by $e^{ix}$ on $L^2(\mu)$, show that $N\cong N_m^{(\infty)}$ where $m=$ arc length measure on $\partial\mathbb D$.

9. Define $U:L^2(\mathbb R)\to L^2(\mathbb R)$ by $(Uf)(t)=f(t-1)$. Show that $U$ is unitary and find its scalar-valued spectral measure and multiplicity function.

10. Represent $N$ as in Theorem 10.1 and find the corresponding representation for $N\oplus N=N^{(2)}$; for $N^{(3)}$, for $N^{(\infty)}$. (Are you surprised by the result for $N^{(\infty)}$?)

11. Prove the results and solve the exercises from §II.8.

12. Let $N$ be a normal operator and show that $N\cong N^{(2)}$ if and only if there is a $*$-cyclic normal operator $M$ such that $N\cong M^{(\infty)}$. What does this say about the multiplicity function for $N$?

13. Let $(X,\Omega,\mu)$ be a measure space such that $L^2(\mu)$ is separable, let $\phi\in L^\infty(\mu)$, and let $N=M_\phi$ on $L^2(\mu)$. Find the decompositions of $N$ obtained in Theorems 10.1 and 10.16.

14. Let $\mu$ be a compactly supported measure on $\mathbb C$, $\phi$ a bounded Borel function on $\mathbb C$, and suppose $\{\Delta_n\}$ are pairwise disjoint Borel sets such that $\phi$ is one-to-one on each $\Delta_n$ and $\mu(\mathbb C\setminus\bigcup_{n=1}^{\infty}\Delta_n)=0$. Let $\phi_n=\phi\chi_{\Delta_n}$ and $\mu_n=\mu\circ\phi_n^{-1}$ for $n\geq1$. Prove that $M_\phi$ on $L^2(\mu)$ is unitarily equivalent to $\bigoplus_{n=1}^{\infty}N_{\mu_n}$.

