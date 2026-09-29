2. Let $\mathcal X$ be a normed space, let $\mathcal Y$ be a Banach space, and let $\widehat{\mathcal X}$ be the completion of $\mathcal X$. Show that if $\rho:\mathcal B(\widehat{\mathcal X},\mathcal Y)\to\mathcal B(\mathcal X,\mathcal Y)$ is defined by $\rho(A)=A|_{\mathcal X}$, then $\rho$ is an isometric isomorphism.

3. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, $\phi:X\to\mathbb F$ is an $\Omega$-measurable function, $1\leq p\leq\infty$, and $\phi f\in L^p(\mu)$ whenever $f\in L^p(\mu)$, then show that $\phi\in L^\infty(\mu)$.

4. Verify the statements in Example 2.2.

5. Verify the statements in Example 2.3.

6. Verify the statements in Example 2.4.

7. Let $A$ and $\tau$ be as in Example 2.4. (a) Give necessary and sufficient conditions on $\tau$ that $A$ be injective. (b) Give such a condition that $A$ be surjective. (c) Give such a condition that $A$ be an isometry. (d) If $X=Y$, show that $A^2=A$ if and only if $\tau$ is a retraction.

8. (Wilansky [1951]) Assume that $A:\mathcal X\to\mathcal Y$ is an additive mapping (that is, $A(x_1+x_2)=A(x_1)+A(x_2)$ for all $x_1$ and $x_2$ in $\mathcal X$) and show that conditions (b), (c), and (d) in Proposition 2.1 are equivalent to the continuity of $A$.

## §3. Finite Dimensional Normed Spaces

In functional analysis it is always good to see what significance a concept has for finite dimensional spaces.

**3.1. Theorem.** *If $\mathcal X$ is a finite dimensional vector space over $\mathbb F$, then any two norms on $\mathcal X$ are equivalent.*

**Proof.** Let $\{e_1,\ldots,e_d\}$ be a Hamel basis for $\mathcal X$. For $x=\sum_{j=1}^{d}x_je_j$, define $\|x\|_\infty\equiv\max\{|x_j|:1\leq j\leq d\}$. It is left to the reader to verify that $\|\cdot\|_\infty$ is a norm. Let $\|\cdot\|$ be any norm on $\mathcal X$. It will be shown that $\|\cdot\|$ and $\|\cdot\|_\infty$ are equivalent.

If $x=\sum_j x_je_j$, then $\|x\|\leq\sum_j|x_j|\|e_j\|\leq C\|x\|_\infty$, when $C=\sum_j\|e_j\|$. To show the other inequality, let $\mathcal T$ be the topology defined on $\mathcal X$ by $\|\cdot\|_\infty$ and let $\mathcal U$ be the topology defined on $\mathcal X$ by $\|\cdot\|$. Put $B=\{x\in\mathcal X:\|x\|_\infty\leq1\}$. The first part of the proof implies $\mathcal T\supseteq\mathcal U$. Since $B$ is $\mathcal T$-compact and $\mathcal T\supseteq\mathcal U$, $B$ is $\mathcal U$-compact and the relativizations of the two topologies to $B$ agree. Let $A=\{x\in\mathcal X:\|x\|_\infty<1\}$. Since $A$ is $\mathcal T$-open, it is open in $(B,\mathcal U)$. Hence there is a set $U$ in $\mathcal U$ such that $U\cap B=A$. Thus $0\in U$ and there is an $r>0$ such that $\{x\in\mathcal X:\|x\|<r\}\subseteq U$. Hence

$$
\|x\|<r\text{ and }\|x\|_\infty\leq1\text{ implies }\|x\|_\infty<1. \tag{3.2}
$$

**Claim.** $\|x\|<r$ implies $\|x\|_\infty<1$.

Let $\|x\|<r$ and put $x=\sum_jx_je_j$, $\alpha=\|x\|_\infty$. So $\|x/\alpha\|_\infty=1$ and $x/\alpha\in B$. If
