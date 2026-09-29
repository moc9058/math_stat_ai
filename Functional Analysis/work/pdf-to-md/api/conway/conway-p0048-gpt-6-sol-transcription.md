**Proof.** It has already been mentioned that $S$ is an isometry (I.5.3). For $(\alpha_n)$ and $(\beta_n)$ in $l^2$,
$$
\begin{aligned}
\langle S^*(\alpha_n),(\beta_n)\rangle
&=\langle(\alpha_n),S(\beta_n)\rangle\\
&=\langle(\alpha_1,\alpha_2,\ldots),(0,\beta_1,\beta_2,\ldots)\rangle\\
&=\alpha_2\overline{\beta}_1+\alpha_3\overline{\beta}_2+\cdots\\
&=\langle(\alpha_2,\alpha_3,\ldots),(\beta_1,\beta_2,\ldots)\rangle.
\end{aligned}
$$
Since this holds for every $(\beta_n)$, the result is proved. ■

The operator $S$ in (2.10) is called the *unilateral shift* and the operator $S^*$ is called the *backward shift*.

The operation of taking the adjoint of an operator is, as the reader may have seen from the examples above, analogous to taking the conjugate of a complex number. It is good to keep the analogy in mind, but do not become too religious about it.

**2.11. Definition.** If $A\in\mathcal{B}(\mathcal{H})$, then: (a) is *hermitian* or *self-adjoint* if $A^*=A$; (b) $A$ is *normal* if $AA^*=A^*A$.

In the analogy between the adjoint and the complex conjugate, hermitian operators become the analogues of real numbers and, by (2.5), unitaries are the analogues of complex numbers of modulus 1. Normal operators, as we shall see, are the true analogues of complex numbers. Notice that hermitian and unitary operators are normal.

In light of (2.8), every multiplication operator $M_\phi$ is normal; $M_\phi$ is hermitian if and only if $\phi$ is real-valued; $M_\phi$ is unitary if and only if $|\phi|\equiv 1$ a.e. $[\mu]$. By (2.9), an integral operator $K$ with kernel $k$ is hermitian if and only if $k(x,y)=\overline{k(y,x)}$ a.e. $[\mu\times\mu]$. The unilateral shift is not normal (Exercise 6).

**2.12. Proposition.** If $\mathcal{H}$ is a $\mathbb{C}$-Hilbert space and $A\in\mathcal{B}(\mathcal{H})$, then $A$ is hermitian if and only if $\langle Ah,h\rangle\in\mathbb{R}$ for all $h$ in $\mathcal{H}$.

**Proof.** If $A=A^*$, then $\langle Ah,h\rangle=\langle h,Ah\rangle=\overline{\langle Ah,h\rangle}$; hence $\langle Ah,h\rangle\in\mathbb{R}$.

For the converse, assume $\langle Ah,h\rangle$ is real for every $h$ in $\mathcal{H}$. If $\alpha\in\mathbb{C}$ and $h,g\in\mathcal{H}$, then $\langle A(h+\alpha g),h+\alpha g\rangle=\langle Ah,h\rangle+\overline{\alpha}\langle Ah,g\rangle+\alpha\langle Ag,h\rangle+|\alpha|^2\langle Ag,g\rangle\in\mathbb{R}$. So this expression equals its complex conjugate. Using the fact that $\langle Ah,h\rangle$ and $\langle Ag,g\rangle\in\mathbb{R}$ yields
$$
\begin{aligned}
\alpha\langle Ag,h\rangle+\overline{\alpha}\langle Ah,g\rangle
&=\overline{\alpha}\langle h,Ag\rangle+\alpha\langle g,Ah\rangle\\
&=\overline{\alpha}\langle A^*h,g\rangle+\alpha\langle A^*g,h\rangle.
\end{aligned}
$$
By first taking $\alpha=1$ and then $\alpha=i$, we obtain the two equations
$$
\langle Ag,h\rangle+\langle Ah,g\rangle
=\langle A^*h,g\rangle+\langle A^*g,h\rangle,
$$
$$
i\langle Ag,h\rangle-i\langle Ah,g\rangle
=-i\langle A^*h,g\rangle+i\langle A^*g,h\rangle.
$$
A little arithmetic implies $\langle Ag,h\rangle=\langle A^*g,h\rangle$, so $A=A^*$. ■

The preceding proposition is false if it is only assumed that $\mathcal{H}$ is an $\mathbb{R}$-Hilbert space. For example, if $A=\begin{bmatrix}0&1\\-1&0\end{bmatrix}$ on $\mathbb{R}^2$, then $\langle Ah,h\rangle=0$ for
