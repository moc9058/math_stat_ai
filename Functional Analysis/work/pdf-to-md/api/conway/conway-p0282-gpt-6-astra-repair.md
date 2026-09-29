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

20. This exercise discusses trace-class operators (defined below) and assumes a knowledge of Exercise 19. $\mathcal B_1(\mathcal H)=\{AB:A\text{ and }B\in\mathcal B_2(\mathcal H)\}$. Operators belonging to $\mathcal B_1(\mathcal H)$ are called *trace-class operators* and $\mathcal B_1(\mathcal H)=\mathcal B_1$ is called the trace class. (a) If $A\in\mathcal B_1(\mathcal H)$ and $\{e_i\}$ is a basis, then $\sum|\langle Ae_i,e_i\rangle|<\infty$. Moreover, the sum $\sum\langle Ae_i,e_i\rangle$ is independent of the choice of basis. (Hint: If $A=C^*B$, $B,C$ in $\mathcal B_2$, show that $|\langle Ae_i,e_i\rangle|=\frac12(\|Be_i\|^2+\|Ce_i\|^2)$.) (b) If $\{e_i\}$ is a basis for $\mathcal H$, define $\operatorname{tr}:\mathcal B_1\to\mathbb C$ by
$$
\operatorname{tr}(A)=\sum_i\langle Ae_i,e_i\rangle.
$$

By (a) the definition of $\operatorname{tr}(A)$ does not depend on the choice of a basis; $\operatorname{tr}(A)$ is called the *trace* of $A$. If $\dim\mathcal H<\infty$, then $\operatorname{tr}(A)$ is precisely the sum of the diagonal terms of any matrix representation of $A$. (c) If $A\in\mathcal B(\mathcal H)$, then the following are equivalent: (1) $A\in\mathcal B_1$; (2) $|A|=(A^*A)^{1/2}\in\mathcal B_1$; (3) $|A|^{1/2}\in\mathcal B_2$; (4) $\operatorname{tr}(|A|)<\infty$. (d) If $A\in\mathcal B_1$ and $T\in\mathcal B$, then $AT$ and $TA$ are in $\mathcal B_1$ and $\operatorname{tr}(AT)=\operatorname{tr}(TA)$. Moreover, $\operatorname{tr}:\mathcal B_1\to\mathbb C$ is a positive linear functional such that if $A\in\mathcal B_1$, $A\geq0$, and $\operatorname{tr}(A)=0$, then $A=0$. (e) If $A\in\mathcal B_1$, define $\|A\|_1\equiv\operatorname{tr}(|A|)$. If $A\in\mathcal B_1$ and $T\in\mathcal B$, show that $|\operatorname{tr}(TA)|\leq\|T\|\|A\|_1$. (f) $\|A\|_1=\|A^*\|_1$ if $A\in\mathcal B_1$. (g) If $T\in\mathcal B$ and $A\in\mathcal B_1$, then $\|TA\|_1\leq\|T\|\|A\|_1$ and $\|AT\|_1\leq\|T\|\|A\|_1$. (h) $\|\cdot\|_1$ is a norm on $\mathcal B_1$. It is called the *trace norm*. (i) $\mathcal B_1$ is an ideal in $\mathcal B(\mathcal H)$ that contains $\mathcal B_{00}$. (j) If $A\in\mathcal B_1$
