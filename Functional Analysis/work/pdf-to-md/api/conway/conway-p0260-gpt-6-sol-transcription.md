# §4*. Ideals and Quotients of $C^*$-Algebras

We begin with a basic result.

**4.1. Proposition.** *If $I$ is a closed left or right ideal in the $C^*$-algebra $\mathcal A$, $a\in I$ with $a=a^*$, and if $f\in C(\sigma(a))$ with $f(0)=0$, then $f(a)\in I$.*

**Proof.** Note that if $I$ is proper, then $0\in\sigma(a)$ since $a$ cannot be invertible. Since $\sigma(a)\subseteq\mathbb R$, the Weierstrass Theorem implies there is a sequence $\{p_n\}$ of polynomials such that $p_n(t)\to f(t)$ uniformly for $t$ in $\sigma(a)$. Hence $p_n(0)\to f(0)=0$. Thus $q_n(t)=p_n(t)-p_n(0)\to f(t)$ uniformly on $\sigma(a)$ and $q_n(0)=0$ for all $n$. Thus $q_n(a)\in I$ and by the functional calculus, $\|q_n(a)-f(a)\|\to0$. Hence $f(a)\in I$. $\blacksquare$

**4.2. Corollary.** *If $I$ is a closed left or right ideal, $a\in I$ with $a=a^*$, then $a_+$, $a_-$, $|a|$, and $|a|^{1/2}\in I$.*

Note that if $I$ is a left ideal of $\mathcal A$, then $\{a^*:a\in I\}$ is a right ideal. Therefore a left ideal $I$ is an ideal if $a^*\in I$ whenever $a\in I$.

**4.3. Theorem.** *If $I$ is a closed ideal in the $C^*$-algebra $\mathcal A$, then $a^*\in I$ whenever $a\in I$.*

**Proof.** Fix $a$ in $I$. Thus $a^*a\in I$ since $I$ is an ideal. The idea is to construct a sequence $\{u_n\}$ of continuous functions defined on $[0,\infty)$ such that

$$
\begin{aligned}
\text{(i)}\quad &u_n(0)=0\text{ and }u_n(t)\geq0\text{ for all }t;\\
\text{(ii)}\quad &\|au_n(a^*a)-a\|\to0\text{ as }n\to\infty.
\end{aligned}
\tag{4.4}
$$

Note that if such a sequence $\{u_n\}$ can be constructed, then $u_n(a^*a)\geq0$ and $u_n(a^*a)\in I$ by Proposition 4.1. Also, $u_n(a^*a)a^*\in I$ since $I$ is an ideal and $\|u_n(a^*a)a^*-a^*\|=\|au_n(a^*a)-a\|\to0$ by (ii). Thus $a^*\in I$ whenever $a\in I$. It remains to construct the sequence $\{u_n\}$.

Note that

$$
\begin{aligned}
\|au_n(a^*a)-a\|^2
&=\|[au_n(a^*a)-a]^*[au_n(a^*a)-a]\|\\
&=\|u_n(a^*a)a^*au_n(a^*a)-a^*au_n(a^*a)-u_n(a^*a)a^*a+a^*a\|.
\end{aligned}
$$

If $b=a^*a$, then the fact that $bu_n(b)=u_n(b)b$ implies that $\|au_n(a^*a)-a\|^2=\|f_n(b)\|\leq\sup\{|f_n(t)|:t\geq0\}$, where $f_n(t)=tu_n(t)^2-2tu_n(t)+t=t[u_n(t)-1]^2$. If $u_n(t)=nt$ for $0\leq t\leq n^{-1}$ and $u(t)=1$ for $t\geq n^{-1}$, then it is seen that $\sup\{|f_n(t)|:t\geq0\}=4/27n\to0$ as $n\to\infty$; so (4.4) is satisfied. $\blacksquare$

Notice that the construction of the sequence $\{u_n\}$ satisfying (4.4) actually proves more. It shows that there is a “local” approximate identity. That is, the proof of the preceding theorem shows that the following holds.
