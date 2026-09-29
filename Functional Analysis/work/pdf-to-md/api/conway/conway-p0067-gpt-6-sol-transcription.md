**Claim.** $h'=H_a h_b'+h_a'H_b$ everywhere.

Put $\phi=H_a h_b'+h_a'H_b$ and put $\psi(x)=h(a)+\int_a^x\phi(y)\,dy$. So $\phi$ and $\psi$ are absolutely continuous, $h(a)=\psi(a)$, and $h'=\psi'$ a.e. Thus $h=\psi$ everywhere. But $\psi$ has a continuous derivative $\phi$, so $h$ does too. That is, the claim is proved.

Differentiating $h'=H_a h_b'+h_a'H_b$ gives that a.e.,
$$
h''=(c^{-1}h_a f)h_b'+H_a h_b''+h_a''H_b+h_a'(-c^{-1}h_b f);
$$
since each of these summands belongs to $L^2[a,b]$, $h''\in L^2[a,b]$.

Because $H_a(a)=0$ and $h_a\in\mathcal D_a$,
$$
\alpha h(a)+\alpha_1h'(a)
=\alpha h_a(a)H_b(a)+\alpha_1h_a'(a)H_b(a)
=[\alpha h_a(a)+\alpha_1h_a'(a)]H_b(a)=0.
$$
Hence $h\in\mathcal D_a$. Similarly, $h\in\mathcal D_b$. Thus $h\in\mathcal D$. Hence $\operatorname{ran}G\subseteq\mathcal D$.

Now to show that $LGf=f$. If $h=Gf$,
$$
\begin{aligned}
L(h)&=-h''+qh\\
&=-\bigl(c^{-1}h_a h_b'f+H_a h_b''+h_a''H_b-c^{-1}h_a'h_bf\bigr)
  +q(H_a h_b+h_aH_b)\\
&=(-h_b''+qh_b)H_a+(-h_a''+qh_a)H_b
  +c^{-1}(h_a'h_b-h_a h_b')f\\
&=f
\end{aligned}
$$
since $L(h_a)=L(h_b)=0$ and $h_a'h_b-h_a h_b'=W=c$.

If $h\in\mathcal D$, then $Lh\in L^2[a,b]$. So by the first part of the proof, $LGLh=Lh$. Thus $0=L(GLh-h)$. Since $\ker L=(0)$, $h=GLh$ and so $h\in\operatorname{ran}G$. $\blacksquare$

**6.10. Corollary.** Assume (6.4). If $h\in\mathcal D$, $\lambda\in\mathbb C\setminus\{0\}$, and $Lh=\lambda h$, then $Gh=\lambda^{-1}h$. If $h\in L^2[a,b]$ and $Gh=\lambda^{-1}h$, then $h\in\mathcal D$ and $Lh=\lambda h$.

**Proof.** This is immediate from the theorem. $\blacksquare$

**6.11. Lemma.** Assume (6.4). If $\alpha\in\sigma_p(G)$ and $\alpha\ne0$, then $\dim\ker(G-\alpha)=1$.

**Proof.** Suppose there are linearly independent functions $h_1,h_2$ in $\ker(G-\alpha)$. By (6.10), $h_1,h_2$ are solutions of the equation
$$
-h''+(q-\alpha^{-1})h=0.
$$
Since this is a second-order linear differential equation, every solution of it must be a linear combination of $h_1$ and $h_2$. But $h_1,h_2\in\mathcal D$ so they satisfy (6.2). But a solution can be found to this equation satisfying any initial conditions at $a$—and thus not satisfying (6.2). This contradiction shows that linearly independent $h_1,h_2$ in $\ker(G-\alpha)$ cannot be found. $\blacksquare$

**6.12. Theorem.** Assume (6.4). Then there is a sequence $\{\lambda_1,\lambda_2,\ldots\}$ of real numbers and a basis $\{e_1,e_2,\ldots\}$ for $L^2[a,b]$ such that

(a) $0<|\lambda_1|<|\lambda_2|<\cdots$ and $|\lambda_n|\to\infty$.

(b) $e_n\in\mathcal D$ and $Le_n=\lambda_n e_n$ for all $n$.

(c) If $\lambda\ne\lambda_n$ for any $\lambda_n$ and $f\in L^2[a,b]$, then there is a unique $h$ in $\mathcal D$ with $Lh-\lambda h=f$.

(d) If $\lambda=\lambda_n$ for some $n$ and $f\in L^2[a,b]$, then there is an $h$ in $\mathcal D$ with $Lh-\lambda h=f$ if and only if $\langle f,e_n\rangle=0$. If $\langle f,e_n\rangle=0$, any two solutions of $Lh-\lambda h=f$ differ by a multiple of $e_n$.

**Proof.** Parts (a) and (b) follow by Theorem 5.1, Corollary 6.10, and
