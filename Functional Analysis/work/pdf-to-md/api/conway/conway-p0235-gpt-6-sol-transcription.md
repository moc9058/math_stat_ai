there is a measure $\mu$ in $M(X)$ such that $h(f)=\int f\,d\mu$ for all $f$ in $C(X)$. Also, $\|\mu\|=\|h\|=1$ and $\mu(X)=\int 1\,d\mu=h(1)=1$. Hence $\mu\geq 0$ (Exercises III.7.2). Let $x\in\operatorname{support}(\mu)$. It will be shown that $h=\delta_x$.

Let $\mathcal M=\{f\in C(X):f(x)=0\}$. So $\mathcal M$ is a maximal ideal of $C(X)$. Note that if it can be shown that $\ker h\subseteq\mathcal M$, then it must be that $\ker h=\mathcal M$ and so $h=\delta_x$. So let $f\in\ker h$. Because $\ker h$ is an ideal, $|f|^2=f\overline f\in\ker h$. Hence $0=h(|f|^2)=\int|f|^2\,d\mu$. Since $\mu\geq 0$ and $|f|^2\geq 0$, it must be that $f=0$ a.e. $[\mu]$. Since $f$ is continuous, $f\equiv 0$ on $\operatorname{support}(\mu)$. In particular, $f(x)=0$ and so $f\in\mathcal M$. ■

It follows from the preceding theorem that the maximal ideals of $C(X)$ are all of the form $\{f\in C(X):f(x)=0\}$ for some $x$ in $X$.

**8.8. Definition.** Let $\mathcal A$ be an abelian Banach algebra with maximal ideal space $\Sigma$. If $a\in\mathcal A$, then the *Gelfand transform* of $a$ is the function $\hat a:\Sigma\to\mathbb C$ defined by $\hat a(h)=h(a)$.

**8.9. Theorem.** *If $\mathcal A$ is an abelian Banach algebra with maximal ideal space $\Sigma$ and $a\in\mathcal A$, then the Gelfand transform of $a$, $\hat a$, belongs to $C(\Sigma)$. The map $a\mapsto\hat a$ of $\mathcal A$ into $C(\Sigma)$ is a continuous homomorphism of $\mathcal A$ into $C(\Sigma)$ of norm 1 and its kernel is*

$$
\bigcap\{\mathcal M:\mathcal M\text{ is a maximal ideal of }\mathcal A\}.
$$

*Moreover, for each $a$ in $\mathcal A$,*

$$
\|\hat a\|_\infty=\lim_{n\to\infty}\|a^n\|^{1/n}.
$$

**Proof.** If $h_i\to h$ in $\Sigma$, then $h_i\to h$ weak* in $\mathcal A^*$. So if $a\in\mathcal A$, $\hat a(h_i)=h_i(a)\to h(a)=\hat a(h)$. Thus $\hat a\in C(\Sigma)$.

Define $\gamma:\mathcal A\to C(\Sigma)$ by $\gamma(a)=\hat a$. If $a,b\in\mathcal A$, then $\gamma(ab)(h)=\widehat{ab}(h)=h(ab)=h(a)h(b)=\hat a(h)\hat b(h)$. Therefore $\gamma(ab)=\gamma(a)\gamma(b)$. It is easy to see that $\gamma$ is linear, so $\gamma$ is a homomorphism. Also, by (8.4), if $a\in\mathcal A$, $|\hat a(h)|=|h(a)|\leq\|a\|$; thus $\|\gamma(a)\|_\infty=\|\hat a\|_\infty\leq\|a\|$. So $\gamma$ is continuous and $\|\gamma\|\leq 1$. Since $\gamma(1)=1$, $\|\gamma\|=1$.

Note that $a\in\ker\gamma$ if and only if $\hat a\equiv 0$; that is, $a\in\ker\gamma$ if and only if $h(a)=0$ for each $h$ in $\Sigma$. Thus $a\in\ker\gamma$ if and only if $a$ belongs to every maximal ideal of $\mathcal A$.

Finally, by Theorem 8.6, if $a\in\mathcal A$, then $\|\hat a\|_\infty=\sup\{|\lambda|:\lambda\in\sigma(a)\}$. The last part of this theorem is thus a consequence of this observation and Proposition 3.8. ■

The homomorphism $a\mapsto\hat a$ of $\mathcal A$ into $C(\Sigma)$ is called the *Gelfand transform* of $\mathcal A$. The kernel of the Gelfand transform is called the *radical* of $\mathcal A$, $\operatorname{rad}\mathcal A$. So

$$
\operatorname{rad}\mathcal A=\bigcap\{\mathcal M:\mathcal M\text{ is a maximal ideal of }\mathcal A\}.
$$
