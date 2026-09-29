boundary point of $\sigma(A)$ and $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$, then there is a sequence $\{\lambda_n\}$ in $\mathbb C\setminus\sigma(A)$ such that $\lambda_n\to\lambda$. Thus $\operatorname{ind}(A-\lambda_n)\to\operatorname{ind}(A-\lambda)$. Since $\operatorname{ind}(A-\lambda_n)=0$ for all $n$, the result follows. ■

Here is the remaining spectral information about an old friend.

**4.10. Example.** Let $S$ be the unilateral shift on $l^2$. Then $\sigma_{le}(S)=\sigma_{re}(S)=\partial\mathbb D$ and $\operatorname{ind}(S-\lambda)=-1$ for $|\lambda|<1$.

In Proposition VII.6.5 it was shown that $\sigma(S)=\operatorname{cl}\mathbb D$, $\sigma_p(S)=\square$, and $\sigma_{ap}(S)=\partial\mathbb D$. Thus for $|\lambda|=1$, $\operatorname{ran}(S-\lambda)$ is not closed and hence $\partial\mathbb D\subseteq\sigma_{le}(S)\cap\sigma_{re}(S)$. Also, if $|\lambda|<1$, it was shown that $\operatorname{ran}(S-\lambda)$ is closed and $\dim[\operatorname{ran}(S-\lambda)]^\perp=1$. This implies that $\partial\mathbb D=\sigma_{le}(S)=\sigma_{re}(S)$ and $\operatorname{ind}(S-\lambda)=-1$ for $\lambda$ in $\mathbb D$.

Using this information about the shift and Proposition 3.4(c) we can get complete information about another operator. (Also see Example 3.10.)

**4.11. Example.** Let $S$ be the unilateral shift of multiplicity 1 and put $A=S\oplus S^*$. It follows that $\sigma_{le}(A)=\sigma_{re}(A)=\partial\mathbb D$, $\sigma(A)=\operatorname{cl}\mathbb D$, and $\operatorname{ind}(A-\lambda)=0$ for $|\lambda|<1$.

## EXERCISES

1. Show that the material of this section is only significant for infinite dimensional Hilbert spaces by showing that the essential spectrum of every operator on $\mathcal H$ is non-empty if and only if $\mathcal H$ is infinite dimensional.

2. Let $G$ be a bounded region in $\mathbb C$ such that $\partial G=\partial[\operatorname{cl}G]$ and let $\phi$ be a function that is analytic in a neighborhood of $\operatorname{cl}G$. Define $A:L_a^2(G)\to L_a^2(G)$ by $Af=\phi f$. Find all of the parts of the spectrum of $A$.

3. (Fillmore, Stampfli, and Williams [1972].) If $\lambda\in\sigma_{le}(A)$, then there is a projection $P$, having infinite rank, such that $\pi(A-\lambda)\pi(P)=0$.

4. (Fillmore, Stampfli, and Williams [1972].) Let $A\in\mathcal B(\mathcal H)$. (a) If $A$ has a cyclic vector $e$, show that $\dim\{Ae,A^2e,\ldots\}^\perp\leq 1$. (b) Let $\lambda\in\sigma_{le}(A^*)$. If $\varepsilon>0$, let $f_1,f_2$ be orthonormal vectors such that $\|(A^*-\lambda)f_j\|<\varepsilon$ for $j=1,2$ and let $P=$ the projection onto $\vee\{f_1,f_2\}$. Put $B=\bar\lambda P+(1-P)A$. Show that $\|B-A\|<2\varepsilon$. (c) Show that the noncyclic operators are dense in $\mathcal B(\mathcal H)$ if $\dim\mathcal H>1$.

5. Let $A\in\mathcal F$ and suppose $f$ is analytic in a neighborhood of $\sigma(A)$ and does not vanish on $\sigma_e(A)$. Show that $f(A)\in\mathcal F$ and find $\operatorname{ind}f(A)$.

6. Let $S$ be the unilateral shift and let $f$ be an analytic function in a neighborhood of $\operatorname{cl}\mathbb D$ such that $f(z)\ne0$ if $|z|=1$. Let $\gamma(t)=f(\exp(2\pi it))$, $0\leq t\leq1$. Show that $\sigma_e(f(S))=f(\partial\mathbb D)=\{\gamma(t):0\leq t\leq1\}$ and that if $\lambda\notin f(\partial\mathbb D)$, $\operatorname{ind}(f(S)-\lambda)=-n(\gamma;\lambda)$, where $n(\gamma;\lambda)=$ the winding number of $\gamma$ about $\lambda$. Moreover, show that if $\operatorname{ind}(f(S)-\lambda)=0$, then $\lambda\notin\sigma(f(S))$.

7. Let $S$ be the operator defined in Example 2.11 where $G=\mathbb D$. Show that there is a compact operator $K$ such that $S+K$ is unitarily equivalent to the unilateral shift.
