50
 II. Operators on Hilbert Space

where $\lambda$ is a given complex number, $q\in C[a,b]$, and $f\in L^{2}[a,b]$, together with the boundary conditions

**6.2**
$$
\left\{
\begin{aligned}
\text{(a)}\quad \alpha h(a)+\alpha_{1}h'(a)&=0\\
\text{(b)}\quad \beta h(b)+\beta_{1}h'(b)&=0,
\end{aligned}
\right.
$$

where $\alpha$, $\alpha_{1}$, $\beta$, and $\beta_{1}$ are real numbers and $\alpha^{2}+\alpha_{1}^{2}>0$, $\beta^{2}+\beta_{1}^{2}>0$.

Equation (6.1) together with the boundary conditions (6.2) is called a *(regular) Sturm–Liouville system*. Such systems arise in a number of physical problems, including the description of the motion of a vibrating string. In this section we will discuss solutions of the Sturm–Liouville system by relating the system to a certain compact self-adjoint integral operator.

Recall that an absolutely continuous function $h$ on $[a,b]$ has a derivative a.e. and $h(x)=\int_a^x h'(t)\,dt+h(a)$ for all $x$.

Define
$$
\mathcal D_a\equiv\{h\in C_{\mathbb C}^{(1)}[a,b]: h'\text{ is absolutely continuous, }
h''\in L^2[a,b],\text{ and }h\text{ satisfies (6.2a)}\}.
$$

$\mathcal D_b$ is defined similarly but each $h$ in $\mathcal D_b$ satisfies (6.2b) instead of (6.2a). The space $\mathcal D=\mathcal D_a\cap\mathcal D_b$.

Define $L:\mathcal D\to L^2[a,b]$ by

**6.3**
$$
Lh=-h''+qh.
$$

$L$ is called a *Sturm–Liouville operator*.

Note that $\mathcal D$ is a linear space and $L$ is a linear transformation. The Sturm–Liouville problem thus becomes: if $\lambda\in\mathbb C$ and $f\in L^2[a,b]$, is there an $h$ in $\mathcal D$ with $(L-\lambda)h=f$. Equivalently, for which $\lambda$ is $f$ in $\operatorname{ran}(L-\lambda)$?

By placing a suitable norm on $\mathcal D$, $L$ can be made into a bounded operator. This does not help much. The best procedure is to consider $(L-\lambda)^{-1}$. Integration is the inverse of differentiation, and it turns out that $(L-\lambda)^{-1}$ (when we can define it) is an integral operator.

Begin by considering the case when $\lambda=0$. (Equivalently, replace $q$ by $q-\lambda$.) To define $L^{-1}$ (even if only on the range of $L$), we need that $L$ is injective. Thus we make an assumption;

**6.4**
$$
\text{if }h\in\mathcal D\quad\text{and}\quad Lh=0,\quad\text{then}\quad h=0.
$$

The first lemma is from ordinary differential equations and says that certain initial-value problems have nontrivial (nonzero) solutions.

**6.5. Lemma.** *If $\alpha,\alpha_{1},\beta,\beta_{1}\in\mathbb R$, $\alpha^{2}+\alpha_{1}^{2}>0$, and $\beta^{2}+\beta_{1}^{2}>0$, then there are functions $h_a$, $h_b$ in $\mathcal D_a$, $\mathcal D_b$, respectively, such that $L(h_a)=0$ and $L(h_b)=0$ and $h_a$, $h_b$ are real-valued and not identically zero.*

The *Wronskian* of $h_a$ and $h_b$ is the function
$$
W=\det\begin{bmatrix}h_a&h_b\\h_a'&h_b'\end{bmatrix}
=h_a h_b'-h_a'h_b.
$$
