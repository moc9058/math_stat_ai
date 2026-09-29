Thus $B\in\mathcal{SF}$ and $\operatorname{ind}B=\dim\ker B$. By (3.12) and (6.5) there is a $\delta>0$ such that if $|\mu|<\delta$, then $\dim\ker(B-\mu)\leq\dim\ker B$, $\dim\operatorname{ran}(B-\mu)^\perp=0$, and $\operatorname{ind}(B-\mu)=\operatorname{ind}B$. Thus $\dim\ker(B-\mu)=\dim\ker B$ for $|\mu|<\delta$. Also, choose $\delta$ such that $\operatorname{ind}(A-\mu)=\operatorname{ind}A$ for $|\mu|<\delta$.

On the other hand, if $\mu\ne0$, then $\ker(A-\mu)\subseteq\mathcal M$. In fact, if $h\in\ker(A-\mu)$, then $A^nh=\mu^nh$, so that $h=A^n(\mu^{-n}h)\in\mathcal M_n$ for every $n$. Thus for $0<|\mu|<\delta$, $\dim\ker(A-\mu)=\dim\ker(B-\mu)=\dim\ker B$; that is, $\dim\ker(A-\mu)$ is constant for $0<|\mu|<\delta$. Since $\operatorname{ind}(A-\mu)$ is constant for these values of $\mu$, $\dim\operatorname{ran}(A-\mu)^\perp$ is also constant. $\blacksquare$

The next result is from Putnam [1968].

**6.8. Theorem.** *If $\lambda\in\partial\sigma(A)$, then either $\lambda$ is an isolated point of $\sigma(A)$ or $\lambda\in\sigma_{le}(A)\cap\sigma_{re}(A)$.*

**Proof.** Suppose $\lambda\in\partial\sigma(A)$ but $\lambda$ is not a point of $\sigma_{le}(A)\cap\sigma_{re}(A)$. Thus $A-\lambda\in\mathcal{SF}$. By the preceding theorem, there is a $\delta>0$ such that $A-\mu\in\mathcal{SF}$ and $\dim\ker(A-\mu)$ and $\dim\operatorname{ran}(A-\mu)^\perp$ are constant for $0<|\mu-\lambda|<\delta$. Since $\lambda\in\partial\sigma(A)$, there is a $\nu$ with $0<|\lambda-\nu|<\delta$ such that $A-\nu$ is invertible. Therefore $\ker(A-\mu)=(0)=\operatorname{ran}(A-\mu)^\perp$ for $0<|\lambda-\mu|<\delta$. But $A-\mu\in\mathcal{SF}$ for these values of $\mu$ and hence has closed range. It follows that $A-\mu$ is invertible whenever $0<|\lambda-\mu|<\delta$. This says that $\lambda$ is an isolated point of $\sigma(A)$. $\blacksquare$

What happens if $\lambda$ is an isolated point of $\sigma(A)$?

**6.9. Proposition.** *If $\lambda$ is an isolated point of $\sigma(A)$, the following statements are equivalent.*

(a) $\lambda\notin\sigma_{le}(A)\cap\sigma_{re}(A)$.

(b) The Riesz idempotent $E(\lambda)$ has finite rank.

(c) $A-\lambda\in\mathcal F$ and $\operatorname{ind}(A-\lambda)=0$.

**Proof.** Exercise 4.

If $n\in\mathbb Z\cup\{\pm\infty\}$ and $A\in\mathcal B(\mathcal H)$, define

$$
P_n(A)\equiv\{\lambda\in\sigma(A):A-\lambda\in\mathcal{SF}\text{ and }\operatorname{ind}(A-\lambda)=n\}.
$$

So for $n\ne0$, $P_n(A)$ is an open subset of the plane; the set $P_0(A)$ consists of an open set together with some isolated points of $\sigma(A)$. In fact, Proposition 6.9 can be used to show that $P_0(A)$ contains precisely the isolated points of $\sigma(A)$ for which the Riesz idempotent has finite rank. The proof of the next result is easy.

**6.10. Proposition.** *If $A\in\mathcal B(\mathcal H)$, then $\sigma_e(A)=[\sigma_{le}(A)\cap\sigma_{re}(A)]\cup P_{+\infty}(A)\cup P_{-\infty}(A)$.*
