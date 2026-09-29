Note that $W'=h_a h_b''-h_a''h_b=h_a(qh_b)-(qh_a)h_b=0$. Hence $W(x)\equiv W(a)$ for all $x$.

**6.6. Lemma.** Assuming (6.4), $W(a)\neq 0$ and so $h_a$ and $h_b$ are linearly independent.

**Proof.** If $W(a)=0$, then linear algebra tells us that the column vectors in the matrix used to define $W(a)$ are linearly dependent. Thus there is a $\lambda$ in $\mathbb R$ such that $h_b(a)=\lambda h_a(a)$ and $h_b'(a)=\lambda h_a'(a)$. Thus $h_b\in\mathcal D$ and $L(h_b)=0$. By (6.4), $h_b\equiv 0$, contradiction. $\blacksquare$

Put $c=-W(a)$ and define $g:[a,b]\times[a,b]\to\mathbb R$ by

**6.7**
$$
g(x,y)=
\begin{cases}
c^{-1}h_a(x)h_b(y) & \text{if }a\leq x\leq y\leq b,\\
c^{-1}h_a(y)h_b(x) & \text{if }a\leq y\leq x\leq b.
\end{cases}
$$

The function $g$ is the *Green function* for $L$.

**6.8. Lemma.** The function $g$ defined in (6.7) is real-valued, continuous, and $g(x,y)=g(y,x)$.

**Proof.** Exercise.

**6.9. Theorem.** Assume (6.4). If $g$ is the Green function for $L$ defined in (6.7) and $G:L^2[a,b]\to L^2[a,b]$ is the integral operator defined by

$$
(Gf)(x)=\int_a^b g(x,y)f(y)\,dy,
$$

then $G$ is a compact self-adjoint operator, $\operatorname{ran}G=\mathcal D$, $LGf=f$ for all $f$ in $L^2[a,b]$, and $GLh=h$ for all $h$ in $\mathcal D$.

**Proof.** That $G$ is self-adjoint follows from the fact that $g$ is real-valued and $g(x,y)=g(y,x)$; $G$ is compact by (4.7). Fix $f$ in $L^2[a,b]$ and put $h=Gf$. It must be shown that $h\in\mathcal D$.

Put

$$
H_a(x)=c^{-1}\int_a^x h_a(y)f(y)\,dy
\quad\text{and}\quad
H_b(x)=c^{-1}\int_x^b h_b(y)f(y)\,dy.
$$

Then

$$
\begin{aligned}
h(x)
&=\int_a^b g(x,y)f(y)\,dy\\
&=c^{-1}\int_a^x h_a(y)h_b(x)f(y)\,dy
+c^{-1}\int_x^b h_a(x)h_b(y)f(y)\,dy.
\end{aligned}
$$

That is, $h=H_a h_b+h_a H_b$. Differentiating this equation gives $h'=(c^{-1}h_a f)h_b+H_a h_b'+h_a'H_b+h_a(-c^{-1}h_b f)=H_a h_b'+h_a'H_b$ a.e. Since $H_a h_b'+h_a'H_b$ is absolutely continuous, as part of showing that $h\in\mathcal D$ we want to show the following.
