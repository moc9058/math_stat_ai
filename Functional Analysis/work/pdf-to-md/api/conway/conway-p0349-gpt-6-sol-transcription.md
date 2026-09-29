Since each self-adjoint operator on a separable Hilbert space can be represented as a multiplication operator (Theorem 4.19), the preceding proposition gives a representation of all strongly continuous one parameter semigroups.

## Exercises

1. If $U:\mathbb R\to\mathcal B(\mathcal H)$ is such that $U(t)$ is unitary for all $t$, $U(s+t)=U(s)U(t)$ for all $s$, $t$, and $U:\mathbb R\to(\mathcal B(\mathcal H),\mathrm{WOT})$ is continuous, then $U$ is SOT-continuous.

2. Show that for every integer $n$ there is a continuously differentiable function $\phi_n$ such that both $\phi_n$ and $\phi_n'\in L^1(0,\infty)$, $\phi_n(t)=0$ if $t\geq 1/n$, and $\int_0^\infty\phi_n(t)\,dt=1$.

3. Prove Claim 5.13.

4. Adopt the notation from the proof of Stone’s Theorem. Let $\phi,\psi\in\mathcal L$ and show: (a) $T_\phi^*=S_{\bar\phi}$; (b) $T_\phi T_\psi=T_{\phi*\psi}$ and $S_\phi S_\psi=S_{\phi*\psi}$; (c) $T_\phi A\subseteq AT_\phi$.

5. Let $U$ be a strongly continuous one parameter unitary group with infinitesimal generator $A$. Suppose $e$ is a nonzero vector in $\mathcal H$ such that $Ae=\lambda e$. What is $U(t)e$? Conversely, suppose there is a nonzero $t$ such that $U(t)$ has an eigenvector. What can be said about $A$? $U(s)$?

6. (This exercise is designed to give another proof of Proposition 5.15 as well as give additional information. My thanks to R.B. Burckel for pointing this out to me.) Let $U$ be a strongly continuous one-parameter unitary group with infinitesimal generator $A$. Show that if $\|U(t)-1\|\to0$ as $t\to0$, then as $t\to0$, $t^{-1}\int_a^{a+t}U(s)\,ds\to U(a)$ in norm. From here show that as $t\to0$, $t^{-1}[U(t)-1]$ has a norm limit, and hence $A$ is a bounded operator since it is the norm limit of bounded operators.

## §6. The Fourier Transform and Differentiation

Perhaps the best way to begin this section is by examining an example.

**6.1. Example.** Let $\mathcal D=\{f\in L^2(\mathbb R): f\text{ is absolutely continuous on every bounded interval in }\mathbb R\text{ and }f'\in L^2(\mathbb R)\}$. For $f$ in $\mathcal D$, let $Af=if'$. Then $A$ is self-adjoint.

First let’s show that $A$ is symmetric. If $f\in\mathcal D$, note that $f(x)\to0$ as $x\to\pm\infty$ since $f$ and $f'\in L^2(\mathbb R)$. So if $f,g\in\mathcal D$, $0<a<\infty$,

$$
i\int_{-a}^{a}f'(x)\overline{g(x)}\,dx
=i\bigl[f(a)\overline{g(a)}-f(-a)\overline{g(-a)}\bigr]
-i\int_{-a}^{a}f(x)\overline{g'(x)}\,dx.
$$

Hence $\langle Af,g\rangle=\langle f,Ag\rangle$ and $A$ is symmetric.

Now let $g\in\operatorname{dom}A^*$ and for $0<a<\infty$ let $\mathcal D_a=\{f\in\mathcal D:f(x)=0\text{ for }|x|\geq a\}$. The proof that $g\in\operatorname{dom}A$ follows the lines of the argument used in Example 1.11. In fact, let $h=A^*g$. So if $f\in\mathcal D_a$, then $\int f(x)\overline{h(x)}\,dx=i\int f'(x)\overline{g(x)}\,dx$. Let $H(x)=\int_0^x h(t)\,dt$. Then using integration by parts we get that
