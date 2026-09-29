8. If $S$ is the unilateral shift, show that for every $\varepsilon>0$ there is a rank one operator $F$ with $\|F\|<\varepsilon$ such that $\sigma(S^*\oplus S+F)=\partial\mathbf D$.

9. Let $G$ be an open connected subset of $\sigma(A)\backslash\sigma_{le}(A)\cup\sigma_{re}(A)$ and suppose $\lambda_0\in G$ such that $\operatorname{ind}(A-\lambda_0)=0$. Show that there is a finite rank operator $F$ such that $A+F-\lambda_0$ is invertible. Show that $A+F-\lambda$ is invertible for every $\lambda$ in $G$.

## §5. The Components of $\mathcal{SF}$

Since the index is continuous on $\mathcal{SF}$ and assumes every possible value (Exercise 3.4), $\mathcal{SF}$ cannot be connected. What are its components?

Note that because $\mathcal{SF}$ is an open subset of a Banach space, its components are arcwise connected (Exercise IV.1.24).

**5.1. Theorem.** *If $A,B\in\mathcal{SF}$, then $A$ and $B$ belong to the same component of $\mathcal{SF}$ if and only if $\operatorname{ind}A=\operatorname{ind}B$.*

Half of this theorem is easy. For the other half we first prove a lemma.

**5.2. Lemma.** *If $A\in\mathcal F$ and $\operatorname{ind}A=0$, then there is a path $\gamma:[0,1]\to\mathcal F$ such that $\gamma(0)=1$ and $\gamma(1)=A$.*

**Proof.** By Exercise 3.7 there is a finite-rank operator $F$ such that $A+F$ is invertible. If $\gamma(t)=A+tF$, $\gamma(0)=A$, $\gamma(1)=A+F$, and $\gamma(t)\in\mathcal F$ for all $t$. Thus we may assume that $A$ is invertible.

Let $A=U|A|$ be the polar decomposition of $A$. Because $A$ is invertible, $U$ is a unitary operator and $|A|$ is invertible. Using the Spectral Theorem, $U=\exp(iB)$ where $B$ is hermitian. Also, since $0\notin\sigma(|A|)$, $|A|=\int_{[\delta,r]}x\,dE(x)$, where $0<\delta<r=\|A\|$. Define $\gamma:[0,1]\to\mathcal B(\mathcal H)$ by

$$
\gamma(t)=e^{itB}\int_{[\delta,r]}x^t\,dE(x)=e^{itB}|A|^t.
$$

It is easy to check that $\gamma$ is continuous, $\gamma(0)=1$, and $\gamma(1)=A$. Also, each $\gamma(t)$ is invertible so $\gamma(t)\in\mathcal F$. ■

**Proof of Theorem 5.1.** First assume that $A,B\in\mathcal F$ and $\operatorname{ind}A=\operatorname{ind}B$. So there is an operator $C$ such that $CB=1+K$ for some compact operator $K$. Thus $C\in\mathcal F_r$ and $\operatorname{ind}C=-\operatorname{ind}B=-\operatorname{ind}A$. Hence $AC\in\mathcal F$ and $\operatorname{ind}AC=0$. By the preceding lemma there is a path $\gamma:[0,1]\to\mathcal F$ such that $\gamma(0)=1$ and $\gamma(1)=AC$. Put $\rho(t)=\gamma(t)B-tAK$. Because $AK\in\mathcal B_0$, $\rho(t)\in\mathcal F$ for all $t$ in $[0,1]$. Also, $\rho(0)=B$ and $\rho(1)=ACB-AK=A(1+K)-AK=A$.

Now assume that $\operatorname{ind}A=-\infty$; so $\dim(\operatorname{ran}A)^\perp=\infty$ and $\dim\ker A<\infty$. Let $F$ be a finite-rank operator such that $\ker(A+tF)=0$ for $t\ne0$. (Why does $F$ exist?) This path shows that we may assume that $\ker A=(0)$. Let $V$ be any isometry such that $\dim(\operatorname{ran}V)^\perp=\infty$ and consider the polar decom-
