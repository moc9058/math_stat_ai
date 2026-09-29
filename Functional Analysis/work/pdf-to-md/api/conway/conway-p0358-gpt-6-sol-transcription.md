# §7. Moments

To understand this section, the preceding two sections are unnecessary.

Let $\mu$ be a positive Borel measure on $\mathbb{R}$ such that $\int |t|^n\,d\mu(t)=m_n<\infty$ for every $n\geq 0$. The numbers $\{m_n\}$ are called the *moments* of $\mu$ in analogy with the corresponding concept from mechanics. The central problem here, called the *Hamburger moment problem*, is to characterize those sequences of numbers that are moment sequences. Just as self-adjoint operators are connected to measures, the theory of self-adjoint operators is connected to the solution of this moment problem.

**7.1. Theorem.** If $\{m_n:n\geq 0\}$ is a sequence of real numbers, the following statements are equivalent.

(a) There is a positive regular Borel measure $\mu$ on $\mathbb{R}$ such that $\int |t|^n\,d\mu(t)<\infty$ for all $n\geq 0$ and $m_n=\int t^n\,d\mu(t)$.

(b) If $\alpha_0,\ldots,\alpha_n\in\mathbb{C}$, then $\sum_{j,k=0}^{n}m_{j+k}\alpha_j\bar{\alpha}_k\geq 0$.

(c) There is a self-adjoint operator $A$ and a vector $e$ such that $e\in\operatorname{dom}A^n$ for all $n$ and $m_n=\langle A^ne,e\rangle$ for all $n\geq 0$.

Before proving this theorem, a preliminary result is needed. This result is useful in many other situations and is one of the standard ways to show that a symmetric operator has a self-adjoint extension.

**7.2. Proposition.** Let $T$ be a symmetric operator on $\mathcal{H}$ and suppose there is a function $J:\mathcal{H}\to\mathcal{H}$ having the following properties:

(a) $J$ is conjugate linear (that is, $J(h+g)=Jh+Jg$ and $J(\alpha h)=\bar{\alpha}Jh$);

(b) $J^2=1$;

(c) $J$ is continuous;

(d) $J\operatorname{dom}T\subseteq\operatorname{dom}T$ and $TJ\subseteq JT$.

Then $T$ has a self-adjoint extension.

**Proof.** First note that if $h\in\operatorname{dom}T$, then $Jh\in\operatorname{dom}T$ and $h=J(Jh)$. Hence $J\operatorname{dom}T=\operatorname{dom}T$ and $JT=TJ$.

Let $h\in\mathcal{H}$ and define $L:\mathcal{H}\to\mathbb{C}$ by $L(f)=\langle h,Jf\rangle$. Since $J$ is conjugate linear, $L$ is a linear functional. By (c), $L$ is continuous. Thus there is a unique vector $h^*$ in $\mathcal{H}$ such that $L(f)=\langle f,h^*\rangle$. Let $J^*h=h^*$. Thus $J^*:\mathcal{H}\to\mathcal{H}$ and

$$
\langle f,J^*h\rangle=\langle h,Jf\rangle. \tag{7.3}
$$

It is clear that $J^*$ is additive. If $\alpha\in\mathbb{C}$, then $\langle f,J^*(\alpha h)\rangle=\langle\alpha h,Jf\rangle=\alpha\langle f,J^*h\rangle=\langle f,\bar{\alpha}J^*h\rangle$. Thus $J^*$ is conjugate linear. Since $J^2=1$, it follows that $J^{*2}=1$.

Let $h\in\operatorname{dom}T^*$ and $f\in\operatorname{dom}T$. Then $\langle TJf,h\rangle=\langle Jf,T^*h\rangle=\langle J^*T^*h,f\rangle$ by (7.3). But also by (d), $\langle TJf,h\rangle=\langle JTf,h\rangle=\langle J^*h,Tf\rangle$. So $\langle J^*T^*h,f\rangle=\langle J^*h,Tf\rangle$ for all $h$ in $\operatorname{dom}T^*$ and $f$ in $\operatorname{dom}T$. But this says that $J^*h\in\operatorname{dom}T^*$.
