# Appendix B. The Dual of l1


<a id="pdf-page-390"></a>
# APPENDIX B

## The Dual of $L^p(\mu)$

<!-- BEGIN BACKGROUND BG-B.block1 -->
<a id="bg-b-1"></a>
### Lemma BG-B.1 — The duality inequality and its phase convention

If $1<p<\infty$ and $q=p/(p-1)$, then $\int|fg|\leq\|f\|_p\|g\|_q$. For $p=1$, the bound is $\int|fg|\leq\|f\|_1\|g\|_\infty$. The pairing $\int fg$ used below is linear in both variables; unlike a Hilbert-space inner product it has no built-in conjugate.

**Proof.** The scalar Young inequality $ab\leq a^p/p+b^q/q$ follows by maximizing $ab-a^p/p$ over $a\geq0$, whose maximum occurs at $a=b^{q-1}$. Apply it to $|f|/\|f\|_p$ and $|g|/\|g\|_q$ and integrate; zero norms cause no difficulty. The endpoint estimate follows directly from the essential-supremum bound. If $g\ne0$ in $L^q$, the equality test for the un-conjugated pairing is
$$
f=\frac{\overline g}{|g|}\frac{|g|^{q-1}}{\|g\|_q^{q/p}},
$$
set to zero on $\{g=0\}$. Since $(q-1)p=q$, $\|f\|_p=1$ and $\int fg=\|g\|_q$. This proves the norm equality once a representing $g$ is known. $\square$

<a id="bg-b-2"></a>
### Lemma BG-B.2 — Countable additivity from continuity at the empty set

If a finitely additive scalar set function $\nu$ satisfies $\nu(E_n)\to0$ whenever $E_n\downarrow\varnothing$, then it is countably additive.

**Proof.** For disjoint $A_n$, put $A=\bigcup_nA_n$ and $R_N=A\setminus\bigcup_{n\leq N}A_n$. Then $R_N\downarrow\varnothing$ and finite additivity gives $\nu(A)=\sum_{n\leq N}\nu(A_n)+\nu(R_N)$. Let $N\to\infty$. In the text, $\|\chi_{E_n}\|_p=\mu(E_n)^{1/p}\to0$ uses finiteness of the ambient measure; this is why Case 1 begins with $\mu(X)<\infty$. $\square$

<a id="bg-b-3"></a>
### Lemma BG-B.3 — Simple-function density and countable gluing

For $p<\infty$, simple functions supported on sets of finite measure are dense in $L^p(\mu)$, without any $\sigma$-finiteness assumption on the whole space. If countably many measurable functions agree almost everywhere on overlaps of a measurable cover, they can be glued to one measurable function, up to null sets.

**Proof.** For $f\in L^p$, the sets $E_n=\{1/n\leq|f|\leq n\}$ have finite measure, since $\mu(E_n)\leq n^p\|f\|_p^p$. Dominated convergence gives $f\chi_{E_n}\to f$ in $L^p$. Approximate each bounded truncation uniformly by simple functions on $E_n$; the $L^p$ error is at most the uniform error times $\mu(E_n)^{1/p}$. For gluing a countable cover $E_n$, replace it by disjoint pieces $D_n=E_n\setminus\bigcup_{j<n}E_j$, use the $n$th representative on $D_n$, and remove the countable union of exceptional overlap sets. Piecewise definition over a countable measurable partition preserves measurability. Uncountable gluing does not have this justification, explaining the caution in Case 2. $\square$

The Radon–Nikodym theorem used below is proved for finite measures, with its $\sigma$-finite extension, in [Appendix C](appendix-c.md). The final source label “Case 2b: $p=\infty$” should be read in context as the remaining **$p=1$** case of the theorem; the preserved source label is not a claim that $(L^\infty)^*=L^1$.
<!-- END BACKGROUND BG-B.block1 -->

In this section we will prove the following which appears as III.5.5 and III.5.6 in the text.

**Theorem.** *Let $(X,\Omega,\mu)$ be a measure space, let $1\leq p<\infty$, and let $1/p+1/q=1$. If $g\in L^q(\mu)$, define $F_g:L^p(\mu)\to\mathbb F$ by*

$$
F_g(f)=\int fg\,d\mu.
$$

*If $1<p<\infty$, the map $g\mapsto F_g$ defines an isometric isomorphism of $L^q(\mu)$ onto $L^p(\mu)^*$. If $p=1$ and $(X,\Omega,\mu)$ is $\sigma$-finite, $g\mapsto F_g$ is an isometric isomorphism of $L^\infty(\mu)$ onto $L^1(\mu)^*$.*

**Proof.** If $g\in L^q(\mu)$, then Hölder’s Inequality implies that $|F_g(f)|\leq\|f\|_p\|g\|_q$ for all $f$ in $L^p(\mu)$. Hence $F_g\in L^p(\mu)^*$ and $\|F_g\|\leq\|g\|_q$. Therefore $g\mapsto F_g$ is a linear contraction. It must be shown that this map is surjective and an isometry. Assume $F\in L^p(\mu)^*$.

*Case 1:* $\mu(X)<\infty$. Here $\chi_\Delta\in L^p(\mu)$ for every $\Delta$ in $\Omega$. Define $\nu(\Delta)=F(\chi_\Delta)$. It is easy to see that $\nu$ is finitely additive. If $\{\Delta_n\}\subseteq\Omega$ with $\Delta_1\supseteq\Delta_2\supseteq\cdots$ and $\bigcap_{n=1}^{\infty}\Delta_n=\square$, then

$$
\begin{aligned}
\|\chi_{\Delta_n}\|_p
&=\left[\int|\chi_{\Delta_n}|^p\,d\mu\right]^{1/p}\\
&=\mu(\Delta_n)^{1/p}\to0.
\end{aligned}
$$

Hence $\nu(\Delta_n)\to0$ since $F$ is bounded. It follows by standard measure theory that $\nu$ is a countably additive measure. Moreover, if $\mu(\Delta)=0$, $\chi_\Delta=0$ in $L^p(\mu)$; hence $\nu(\Delta)=0$. that is, $\nu\ll\mu$. By the Radon–Nikodym Theorem there is an $\Omega$-measurable function $g$ such $\nu(\Delta)=\int_\Delta g\,d\mu$ for every $\Delta$ in $\Omega$; that is, $F(\chi_\Delta)=$



<a id="pdf-page-391"></a>
$\int \chi_\Delta g\,d\mu$ for every $\Delta$ in $\Omega$. It follows that

$$
\tag{B.1} F(f)=\int fg\,d\mu
$$

for every simple function $f$.

**B.2. Claim.** $g\in L^q(\mu)$ and $\|g\|_q\leq\|F\|$.

Note that once this claim is proven, the proof of Case 1 is complete. Indeed, (B.2) says that $F_g\in L^p(\mu)^*$ and since $F$ and $F_g$ agree on a dense subset of $L^p(\mu)$ (B.1), $F=F_g$. Also, $\|g\|_q\leq\|F\|=\|F_g\|\leq\|g\|_q$.

To prove (B.2), let $t>0$ and put $E_t=\{x\in X:|g(x)|\leq t\}$. If $f\in L^p(\mu)$ such that $f=0$ off $E_t$, then there is a sequence $\{f_n\}$ of simple functions such that for every $n$, $f_n=0$ off $E_t$, $|f_n|\leq|f|$, and $f_n(x)\to f(x)$ a.e. $[\mu]$. (Why?) Thus $|(f_n-f)g|\leq 2t|f|$ and $\int|f|\,d\mu=\int|f|\cdot1\,d\mu\leq\|f\|_p\mu(X)^{1/q}<\infty$. By the Lebesgue Dominated Convergence Theorem, $F(f_n)=\int f_ng\,d\mu\to\int fg\,d\mu$. Also, $|f_n-f|^p\leq 2^p|f|^p$, so $\|f_n-f\|_p\to0$; thus $F(f_n)\to F(f)$. Combining these results we get that for any $t>0$ and any $f$ in $L^p(\mu)$ that vanishes off $E_t$, (B.1) holds.

*Case 1a:* $1<p<\infty$. So $1<q<\infty$. Let $f=\chi_{E_t}|g|^q/g$, where $g(x)\ne0$, and put $f(x)=0$ when $g(x)=0$. If $A=\{x:g(x)\ne0\}$, then

$$
\int|f|^p\,d\mu
=\int_{E_t\cap A}\frac{|g|^{pq}}{|g|^p}\,d\mu
=\int_{E_t}|g|^q\,d\mu
$$

since $pq-p=q$. Therefore

$$
\int_{E_t}|g|^q\,d\mu
=\int fg\,d\mu
=F(f)
\leq\|F\|\|f\|_p
=\|F\|\left[\int_{E_t}|g|^q\,d\mu\right]^{1/p}.
$$

Thus

$$
\|F\|\geq
\left[\int_{E_t}|g|^q\,d\mu\right]^{1-1/p}
\geq
\left[\int_{E_t}|g|^q\,d\mu\right]^{1/q}.
$$

Letting $t\to\infty$ gives that $\|g\|_q\leq\|F\|$.

*Case 1b:* $p=1$. So $q=\infty$. For $\varepsilon>0$ let $A=\{x:|g(x)|>\|F\|+\varepsilon\}$. For $t>0$ let $f=\chi_{E_t\cap A}\bar g/|g|$. Then $\|f\|_1=\mu(A\cap E_t)$, and so

$$
\|F\|\mu(A\cap E_t)
\geq\int fg\,d\mu
=\int_{A\cap E_t}|g|\,d\mu
\geq(\|F\|+\varepsilon)\mu(A\cap E_t).
$$

Letting $t\to\infty$ we get that $\|F\|\mu(A)\geq(\|F\|+\varepsilon)\mu(A)$, which can only be if $\mu(A)=0$. Thus $\|g\|_\infty\leq\|F\|$.

*Case 2:* $(X,\Omega,\mu)$ is arbitrary. Let $\mathcal E=$ all of the sets $E$ in $\Omega$ such that $\mu(E)<\infty$. For $E$ in $\Omega$ let $\Omega_E=\{\Delta\in\Omega:\Delta\subseteq E\}$ and define $(\mu|E)(\Delta)=\mu(\Delta)$ for $\Delta$ in $\Omega_E$. Put $L^p(\mu|E)=L^p(E,\Omega_E,\mu|E)$ and notice that $L^p(\mu|E)$ can be identified in a natural way with the functions in $L^p(X,\Omega,\mu)$ that vanish off $E$. Make this identification and consider the restriction of $F:L^p(\mu)\to\mathbb F$ to $L^p(\mu|E)$;



<a id="pdf-page-392"></a>
denote the restriction by $F_E:L^p(\mu|E)\to\mathbb F$. Clearly $F_E$ is bounded and $\|F_E\|\leqslant\|F\|$ for every $E$ in $\mathcal E$.

By Case 1, for every $E$ in $\mathcal E$ there is a $g_E$ in $L^q(\mu|E)$ such that for $f$ in $L^p(\mu|E)$,

$$
\text{B.3}\qquad F(f)=\int_E fg_E\,d\mu\ \text{and}\ \|g_E\|_q\leqslant\|F\|.
$$

If $D,E\in\mathcal E$, then $L^p(\mu|D\cap E)$ is contained in both $L^p(\mu|D)$ and $L^p(\mu|E)$. Moreover, $F_D|L^p(\mu|D\cap E)=F_E|L^p(\mu|D\cap E)=F_{D\cap E}$. Hence $g_D=g_E=g_{D\cap E}$ a.e. $[\mu]$ on $D\cap E$. Thus, a function $g$ can be defined on $\bigcup\{E:E\in\mathcal E\}$ by letting $g=g_E$ on $E$; put $g=0$ off $\bigcup\{E:E\in\mathcal E\}$. A difficulty arises here in trying to show that $g$ is measurable.

*Case 2a: $1<p<\infty$.* Put $\sigma=\sup\{\|g_E\|_q:E\in\mathcal E\}$; so $\sigma\leqslant\|F\|<\infty$. Since $\|g_D\|_q\leqslant\|g_E\|_q$ if $D\subseteq E$, there is a sequence $\{E_n\}$ in $\mathcal E$ such that $E_n\subseteq E_{n+1}$ for all $n$ and $\|g_{E_n}\|_q\to\sigma$. Let $G=\bigcup_{n=1}^{\infty}E_n$. If $E\in\mathcal E$ and $E\cap G=\square$, then $\|g_{E\cup E_n}\|_q^q=\|g_E\|_q^q+\|g_{E_n}\|_q^q\to\|g_E\|_q^q+\sigma^q$; thus $g_E=0$. Therefore $g=0$ off $G$ and clearly $g$ is measurable. Moreover, $g\in L^q(\mu)$ with $\|g\|_q=\sigma$.

If $f\in L^p(\mu)$, then $\{x:f(x)\ne0\}=\bigcup_{n=1}^{\infty}D_n$ where $D_n\in\mathcal E$ and $D_n\subseteq D_{n+1}$ for all $n$. Thus $\chi_{D_n}f\to f$ in $L^p(\mu)$ and so $F(f)=\lim F(\chi_{D_n}f)\overset{\text{(B.3)}}{=}\lim\int_{D_n}gf\,d\mu=\int gf\,d\mu$. Thus $F=F_g$ and $\|F\|=\|F_g\|\leqslant\|g\|_q\leqslant\sigma\leqslant\|F\|$.

*Case 2b: $p=\infty$ and $(X,\Omega,\mu)$ is $\sigma$-finite.* This is left to the reader. ■

## EXERCISE

Look at the proof of the theorem and see if you can represent $L^1(X,\Omega,\mu)^*$ for an arbitrary measure space.

