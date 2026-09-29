all $h$ in $\mathbb{R}^{2}$. However, $A^{*}$ is the transpose of $A$ and so $A^{*}\ne A$. Indeed, for any operator $A$ on an $\mathbb{R}$-Hilbert space, $\langle Ah,g\rangle\in\mathbb{R}$.

**2.13. Proposition.** *If $A=A^{*}$, then*

$$
\|A\|=\sup\{|\langle Ah,h\rangle|:\|h\|=1\}.
$$

**Proof.** Put $M=\sup\{|\langle Ah,h\rangle|:\|h\|=1\}$. If $\|h\|=1$, then $|\langle Ah,h\rangle|\leqslant\|A\|$; hence $M\leqslant\|A\|$. On the other hand, if $\|h\|=\|g\|=1$, then

$$
\begin{aligned}
\langle A(h\pm g),h\pm g\rangle
&=\langle Ah,h\rangle\pm\langle Ah,g\rangle\pm\langle Ag,h\rangle+\langle Ag,g\rangle\\
&=\langle Ah,h\rangle\pm\langle Ah,g\rangle\pm\langle g,A^{*}h\rangle+\langle Ag,g\rangle.
\end{aligned}
$$

Since $A=A^{*}$, this implies

$$
\langle A(h\pm g),h\pm g\rangle
=\langle Ah,h\rangle\pm 2\operatorname{Re}\langle Ah,g\rangle+\langle Ag,g\rangle.
$$

Subtracting one of these two equations from the other gives

$$
4\operatorname{Re}\langle Ah,g\rangle
=\langle A(h+g),h+g\rangle-\langle A(h-g),h-g\rangle.
$$

Now it is easy to verify that $|\langle Af,f\rangle|\leqslant M\|f\|^{2}$ for any $f$ in $\mathcal H$. Hence using the parallelogram law we get

$$
\begin{aligned}
4\operatorname{Re}\langle Ah,g\rangle
&\leqslant M(\|h+g\|^{2}+\|h-g\|^{2})\\
&=2M(\|h\|^{2}+\|g\|^{2})\\
&=4M
\end{aligned}
$$

since $h$ and $g$ are unit vectors. Now suppose $\langle Ah,g\rangle=e^{i\theta}|\langle Ah,g\rangle|$. Replacing $h$ in the inequality above with $e^{-i\theta}h$ gives $|\langle Ah,g\rangle|\leqslant M$ if $\|h\|=\|g\|=1$. Taking the supremum over all $g$ gives $\|Ah\|\leqslant M$ when $\|h\|=1$. Thus $\|A\|\leqslant M$. $\blacksquare$

**2.14. Corollary.** *If $A=A^{*}$ and $\langle Ah,h\rangle=0$ for all $h$, then $A=0$.*

The preceding corollary is not true unless $A=A^{*}$, as the example given after Proposition 2.12 shows. However, if a complex Hilbert space is present, this hypothesis can be deleted.

**2.15. Proposition.** *If $\mathcal H$ is a $\mathbb C$-Hilbert space and $A\in\mathcal B(\mathcal H)$ such that $\langle Ah,h\rangle=0$ for all $h$ in $\mathcal H$, then $A=0$.*

The proof of (2.15) is left to the reader.

If $\mathcal H$ is a $\mathbb C$-Hilbert space and $A\in\mathcal B(\mathcal H)$, then $B=(A+A^{*})/2$ and $C=(A-A^{*})/2i$ are self-adjoint and $A=B+iC$. The operators $B$ and $C$ are called, respectively, the *real and imaginary parts* of $A$.

**2.16. Proposition.** *If $A\in\mathcal B(\mathcal H)$, the following statement are equivalent.*

(a) $A$ is normal.
