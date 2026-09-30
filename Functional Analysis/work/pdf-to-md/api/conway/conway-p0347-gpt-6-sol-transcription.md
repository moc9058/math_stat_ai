Similarly, for $\phi$ in $\mathcal L^{(1)}$ and $h$ in $\mathcal H$,

$$
\tag{5.11}
\lim_{t\to 0}-\frac{i}{t}[U(t)-1]S_\phi h
=-iS_{\phi'}h-i\phi(0)h.
$$

So (5.10) implies that

$$
\mathcal D\supseteq\{T_\phi h:\phi\in\mathcal L^{(1)}\text{ and }h\in\mathcal H\}.
$$

But for every positive integer $n$ there is a $\phi_n$ in $\mathcal L^{(1)}$ such that $\phi_n\geq 0$, $\phi_n(t)=0$ for $t\geq 1/n$, and $\int_0^\infty\phi_n(t)\,dt=1$ (Exercise 2). Hence

$$
T_{\phi_n}h-h=\int_0^{1/n}\phi_n(t)[U(t)-1]h\,dt
$$

and so $\|T_{\phi_n}h-h\|\leq\sup\{\|U(t)h-h\|:0\leq t\leq 1/n\}$. Therefore $\|T_{\phi_n}h-h\|\to 0$ as $n\to\infty$ since $U$ is strongly continuous. This says that $\mathcal D$ is dense.

For $h$ in $\mathcal D$, define

$$
\tag{5.12}
Ah=-i\lim_{t\to 0}\frac{1}{t}[U(t)-1]h.
$$

**5.13. Claim.** $A$ is symmetric.

The proof of this is left to the reader.

By (2.2c), $A$ is closable; also denote the closure of $A$ by $A$. According to Corollary 2.9, to prove that $A$ is self-adjoint it suffices to prove that $\ker(A^*\pm i)=(0)$. Equivalently, it suffices to show that $\operatorname{ran}(A\pm i)$ is dense. It will be shown that there are operators $B_\pm$ such that $(A\pm i)B_\pm=1$, so that $A\pm i$ is surjective.

Notice that according to (5.10),

$$
(A+i)T_\phi=AT_\phi+iT_\phi=i(T_{\phi'}+T_\phi)+i\phi(0).
$$

So taking $\phi(t)=-ie^{-1}$, $(A+i)T_\phi=1$. According to (5.11),

$$
(A-i)S_\psi=AS_\psi-iS_\psi=-i(S_{\psi'}+S_\psi)-i\psi(0).
$$

Taking $\psi(t)=ie^{-1}$, $(A-i)S_\psi=1$. Hence $A$ is self-adjoint.

Put $V(t)=\exp(iAt)$. It remains to show that $V=U$. Let $h\in\mathcal D$. By Theorem 5.1(d),

$$
s^{-1}[V(t+s)-V(t)]h=s^{-1}[V(s)-1]V(t)h\to iAV(t)h;
$$

that is, $V'(t)h=iAV(t)h$. Similarly,

$$
s^{-1}[U(t+s)-U(t)]h=s^{-1}[U(s)-1]U(t)h\to iAU(t)h.
$$

So if $h(t)=U(t)h-V(t)h$, then $h:\mathbb R\to\mathcal H$ is differentiable and

$$
h'(t)=iAU(t)h-iAV(t)h=iAh(t).
$$
