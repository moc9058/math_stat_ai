*Then $F_\mu\in C_0(X)^*$ and the map $\mu\mapsto F_\mu$ is an isometric isomorphism of $M(X)$ onto $C_0(X)^*$.*

There are special cases of these theorems that deserve to be pointed out.

**5.8. Example.** The dual of $c_0$ is isometrically isomorphic to $l^1$. In fact, $c_0=C_0(\mathbb N)$, if $\mathbb N$ is given the discrete topology, and $l^1=M(\mathbb N)$.

**5.9. Example.** The dual of $l^1$ is isometrically isomorphic to $l^\infty$. In fact, $l^1=L^1(\mathbb N,2^{\mathbb N},\mu)$, where $\mu(\Delta)=$ the number of points in $\Delta$. Also, $l^\infty=L^\infty(\mathbb N,2^{\mathbb N},\mu)$.

**5.10. Example.** If $1<p<\infty$, the dual of $l^p$ is $l^q$, where $1=1/p+1/q$.

What is the dual of $L^\infty(X,\Omega,\mu)$? There are two possible representations. One is to identify $L^\infty(X,\Omega,\mu)^*$ with the space of finitely additive measures defined on $\Omega$ that are “absolutely continuous” with respect to $\mu$ and have finite total variation (see Dunford and Schwartz [1958], p. 296). Another representation is to obtain a compact space $Z$ such that $L^\infty(X,\Omega,\mu)$ is isometrically isomorphic to $C(Z)$ and then use the Riesz Representation Theorem. This will be done later in this book (VIII.2.1).

What is the dual of $M(X)$? For this, define $L^\infty(M(X))$ as the set of all $F$ in $\prod\{L^\infty(\mu):\mu\in M(X)\}$ such that if $\mu\ll\nu$, then $F(\mu)=F(\nu)$ a.e. $[\mu]$. This is an inverse limit of the spaces $L^\infty(\mu)$, $\mu$ in $M(X)$.

**5.11. Lemma.** *If $F\in L^\infty(M(X))$, then*

$$
\|F\|=\sup_\mu\|F(\mu)\|_\infty<\infty.
$$

**Proof.** If $\|F\|=\infty$, then there is a sequence $\{\mu_n\}$ in $M(X)$ such that $\|F(\mu_n)\|_\infty\geq n$. Let $\mu=\sum_{n=1}^\infty 2^{-n}|\mu_n|/\|\mu_n\|$. Then $\mu_n\ll\mu$ for all $n$, so $F(\mu_n)=F(\mu)$ a.e. $[\mu_n]$ for each $n$. Hence $\|F(\mu)\|_\infty\geq\|F(\mu_n)\|_\infty\geq n$ for each $n$, a contradiction. ■

**5.12. Theorem.** *If $X$ is locally compact and $F\in L^\infty(M(X))$, define $\Phi_F:M(X)\to\mathbb F$ by*

$$
\Phi_F(\mu)=\int F(\mu)\,d\mu.
$$

*Then $\Phi_F\in M(X)^*$ and the map $F\mapsto\Phi_F$ is an isometric isomorphism of $L^\infty(M(X))$ onto $M(X)^*$.*

**Proof.** It is easy to see that $\Phi_F$ is linear. Also, $|\Phi_F(\mu)|\leq\int|F(\mu)|\,d|\mu|\leq\|F(\mu)\|_\infty\|\mu\|\leq\|F\|\|\mu\|$. Thus $\Phi_F\in M(X)^*$ and $\|\Phi_F\|\leq\|F\|$.

Now fix $\Phi$ in $M(X)^*$. If $\mu\in M(X)$ and $f\in L^1(|\mu|)$, then $\nu=f\mu\in M(X)$. (That is, $\nu(\Delta)=\int_\Delta f\,d\mu$ for every Borel set $\Delta$.) Also $\|\nu\|=\int|f|\,d|\mu|$. In fact, the
