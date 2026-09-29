§5. Representations of $C^*$-Algebras　　　　　　　　　　　　　　　　　251

*$f(a)\equiv\langle\pi(a)e,e\rangle$ and if $(\pi_f,\mathcal H_f)$ is constructed as in (a), then $\pi$ and $\pi_f$ are equivalent.*

Before beginning the proof, it will be helpful if the theorem is examined when $\mathcal A$ is abelian. So let $\mathcal A=C(X)$ where $X$ is compact. If $f$ is a positive linear functional on $\mathcal A$, then there is a positive measure $\mu$ on $X$ such that $f(\phi)=\int\phi\,d\mu$ for all $\phi$ in $\mathcal A$. The representation $(\pi_f,\mathcal H_f)$ is the one obtained by letting $\mathcal H_f=L^2(\mu)$ and $\pi_f(\phi)=M_\phi$, but let us look a little closer. One way to obtain $L^2(\mu)$ from $C(X)$ and $\mu$ is to let $\mathcal L=\{\phi\in C(X):\int|\phi|^2\,d\mu=0\}$. Note that $\mathcal L$ is an ideal in $C(X)$. Define an inner product on $C(X)/\mathcal L$ by $\langle\phi+\mathcal L,\psi+\mathcal L\rangle=\int\phi\bar\psi\,d\mu$. The completion of $C(X)/\mathcal L$ with respect to this inner product is $L^2(\mu)$.

To see part (b) in the abelian case, let $\pi:C(X)\to\mathcal B(\mathcal H)$ be a cyclic representation with cyclic vector $e$. Let $\mu$ be the positive measure on $X$ such that $\int\phi\,d\mu=\langle\pi(\phi)e,e\rangle=f(\phi)$. Now define $U_1:C(X)\to\mathcal H$ by $U_1(\phi)=\pi(\phi)e$. Note that $U_1$ is linear and has dense range. If $\mathcal L$ is in the preceding paragraph and $\phi\in\mathcal L$, then $\|U_1(\phi)\|^2=\langle\pi(\phi)e,\pi(\phi)e\rangle=\langle\pi(\phi^*\phi)e,e\rangle=\int|\phi|^2\,d\mu=0$. So $U_1\mathcal L=0$. Thus $U_1$ induces a linear map $U:C(X)/\mathcal L\to\mathcal H$ where $U(\phi+\mathcal L)=\pi(\phi)e$. If $\langle\phi+\mathcal L,\psi+\mathcal L\rangle\equiv\int\phi\bar\psi\,d\mu$, then $\langle U(\phi+\mathcal L),U(\psi+\mathcal L)\rangle=\langle\pi(\phi)e,\pi(\psi)e\rangle=\langle\pi(\phi\psi^*)e,e\rangle=\int\phi\bar\psi\,d\mu=\langle\phi+\mathcal L,\psi+\mathcal L\rangle$. Thus $U$ extends to an isomorphism $U$ from the completion of $\mathcal A/\mathcal L=L^2(\mu)$ onto $\mathcal H$. So $U:L^2(\mu)\to\mathcal H$ and if $\phi\in C(X)$ and we think of $C(X)$ as a (dense) subset of $L^2(\mu)$, $U\phi=\pi(\phi)e$. If $\phi,\psi\in C(X)$, then $UM_\phi\psi=U(\phi\psi)=\pi(\phi\psi)e=\pi(\phi)\pi(\psi)e=\pi(\phi)U(\psi)$; that is, $UM_\phi=\pi(\phi)U$ on a dense subset of $L^2(\mu)$ and, hence, $UM_\phi=\pi(\phi)U$ for every $\phi$ in $C(X)$. In other words, $\pi$ is equivalent to the representation $\phi\mapsto M_\phi$.

**Proof of Theorem 5.14.** Let $f$ be a positive linear functional on $\mathcal A$ and put $\mathcal L=\{x\in\mathcal A:f(x^*x)=0\}$. It is easy to see that $\mathcal L$ is closed in $\mathcal A$. Also if $a\in\mathcal A$ and $x\in\mathcal L$, then (5.11) implies that

$$
\begin{aligned}
f((ax)^*(ax))^2
&=f(x^*(a^*ax))^2\\
&\leqslant f(x^*x)f(x^*a^*aa^*ax)\\
&=0.
\end{aligned}
$$

That is, $\mathcal L$ is a closed left ideal in $\mathcal A$. Now consider $\mathcal A/\mathcal L$ as a vector space. (Since $\mathcal L$ is only a left ideal, $\mathcal A/\mathcal L$ is not an algebra.) For $x,y$ in $\mathcal A$, define

$$
\langle x+\mathcal L,y+\mathcal L\rangle=f(y^*x).
$$

It is left as an exercise for the reader to show that $\langle\cdot;\cdot\rangle$ is a well-defined inner product on $\mathcal A/\mathcal L$. Let $\mathcal H_f$ be the completion of $\mathcal A/\mathcal L$ with respect to the norm defined on $\mathcal A/\mathcal L$ by this inner product.

Because $\mathcal L$ is a left ideal of $\mathcal A$, $x+\mathcal L\mapsto ax+\mathcal L$ is a well-defined linear transformation on $\mathcal A/\mathcal L$. Also, $\|ax+\mathcal L\|^2=\langle ax+\mathcal L,ax+\mathcal L\rangle=f(x^*a^*ax)$. Now if $\|aa^*\|$ is considered as an element of $\mathcal A$ (it is a multiple of the identity), then an appeal to the functional calculus for $a^*a$ shows that $\|a^*a\|-a^*a\geqslant0$.
