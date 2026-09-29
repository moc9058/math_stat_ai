But

$$
\begin{aligned}
\frac{d}{dt}\|h(t)\|^2
&= \langle h'(t),h(t)\rangle+\langle h(t),h'(t)\rangle\\
&= \langle iAh(t),h(t)\rangle+\langle h(t),iAh(t)\rangle.
\end{aligned}
$$

Thus $(d/dt)\|h(t)\|^2=0$ and so $\|h\|:\mathbb R\to\mathbb R$ is a constant function. But $h(0)=0$, so $h(t)\equiv0$. This says that $U(t)h=V(t)h$ for all $h$ in $\mathscr D$ and all $t$ in $\mathbb R$. Since $\mathscr D$ is dense, $U=V$. ■

**5.14. Definition.** If $U$ is a strongly continuous one parameter unitary group, then the self-adjoint operator $A$ such that $U(t)=\exp(itA)$ is called the *infinitesimal generator* of $U$.

By virtue of Stone’s Theorem and Theorem 5.1, there is a one-to-one correspondence between self-adjoint operators and strongly continuous one-parameter unitary groups. Thus, it should be possible to characterize certain properties of a group in terms of its infinitesimal generator and vice versa. For example, suppose the infinitesimal generator is bounded; what can be said about the group? (Also see Exercise 6.)

**5.15. Proposition.** *If $U$ is a strongly continuous one parameter unitary group with infinitesimal generator $A$, then $A$ is bounded if and only if $\lim_{t\to0}\|U(t)-1\|=0$.*

**Proof.** First assume that $A$ is bounded. Hence $\|U(t)-1\|=\|\exp(itA)-1\|=\sup\{|e^{itx}-1|:x\in\sigma(A)\}\to0$ as $t\to0$ since $\sigma(A)$ is compact.

Now assume that $\|U(t)-1\|\to0$ as $t\to0$. Let $0<\varepsilon<\pi/4$; then there is a $t_0>0$ such that $\|U(t)-1\|<\varepsilon$ for $|t|<t_0$. Since $U(t)-1=\int_{\sigma(A)}(e^{ixt}-1)\,dE(t)$, $\sup\{|e^{ixt}-1|:x\in\sigma(A)\}=\|U(t)-1\|<\varepsilon$ for $|t|<t_0$. Thus for a small $\delta$, $tx\in\bigcup_{n=-\infty}^{\infty}(2\pi n-\delta,2\pi n+\delta)\equiv G$ whenever $x\in\sigma(A)$ and $|t|<t_0$. In fact, if $\varepsilon$ is chosen sufficiently small, then $\delta$ is small enough that the intervals $\{(2\pi n-\delta,2\pi n+\delta)\}$ are the components of $G$. If $x\in\sigma(A)$, $\{tx:0\leq t<t_0\}$ is the interval from $0$ to $t_0x$ and is contained in $G$. Hence $tx\in(-\delta,\delta)$ for $x$ in $\sigma(A)$ and $|t|<t_0$. In particular, $t_0\sigma(A)\subseteq[-\delta,\delta]$ so $\sigma(A)$ is compact and $A$ is bounded. ■

Let $\mu$ be a positive measure on $\mathbb R$ and let $A_\mu f=xf$ for $f$ in $\mathscr D_\mu=\{f\in L^2(\mu):xf\in L^2(\mu)\}$. We have already seen that $A_\mu$ is self-adjoint. Clearly $\exp(itA_\mu)=M_{e_t}$ on $L^2(\mathbb R)$, where $e_t$ is the function $e_t(x)=\exp(itx)$. This can be generalized a bit.

**5.16. Proposition.** *Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $\phi$ be a real-valued $\Omega$-measurable function on $X$. If $A=M_\phi$ on $L^2(\mu)$ and $U(t)=\exp(itA)$, then $U(t)=M_{e_t}$, where $e_t(x)=\exp(it\phi(x))$.*
