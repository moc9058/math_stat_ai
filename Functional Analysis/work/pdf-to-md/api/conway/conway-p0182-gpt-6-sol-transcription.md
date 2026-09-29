(a) $T$ is bounded.

(b) $T'(\mathcal Y^*)\subseteq\mathcal X^*$.

(c) $T:(\mathcal X,\text{weak})\to(\mathcal Y,\text{weak})$ is continuous.

**Proof.** (a)$\Rightarrow$(b): If $y^*\in\mathcal Y^*$, then $T'(y^*)\in\mathcal X'$; it must be shown that $T'(y^*)\in\mathcal X^*$. But
$$
|T'(y^*)(x)|=|y^*\circ T(x)|=|\langle T(x),y^*\rangle|
\leq\|T(x)\|\|y^*\|\leq\|T\|\|y^*\|\|x\|.
$$
So $T'(y^*)\in\mathcal X^*$.

(b)$\Rightarrow$(c): If $\{x_i\}$ is a net in $\mathcal X$ and $x_i\to0$ weakly, then for $y^*$ in $\mathcal Y^*$,
$$
\langle T(x_i),y^*\rangle=T'(y^*)(x_i)\to0
$$
since $T'(y^*)\in\mathcal X^*$. Hence $T(x_i)\to0$ weakly in $\mathcal Y$.

(c)$\Rightarrow$(b): If $y^*\in\mathcal Y^*$, then $y^*\circ T:\mathcal X\to\mathbb F$ is weakly continuous by (c). Hence $T'(y^*)=y^*\circ T\in\mathcal X^*$ by (V.1.2).

(b)$\Rightarrow$(a): Let $y^*\in\mathcal Y^*$ and put $x^*=T'(y^*)$. So $x^*\in\mathcal X^*$ by (b). So if $x\in\operatorname{ball}\mathcal X$,
$$
|\langle T(x),y^*\rangle|=|\langle x,x^*\rangle|\leq\|x^*\|.
$$
That is, $\sup\{|\langle T(x),y^*\rangle|:x\in\operatorname{ball}\mathcal X\}<\infty$. Hence $T(\operatorname{ball}\mathcal X)$ is weakly bounded; by the PUB, $T(\operatorname{ball}\mathcal X)$ is norm bounded and so $\|T\|<\infty$. $\blacksquare$

The preceding result is useful, though strictly speaking it is not necessary for the purpose of defining the adjoint of an operator $A$ in $\mathcal B(\mathcal X,\mathcal Y)$, which we now turn to. If $A\in\mathcal B(\mathcal X,\mathcal Y)$ and $y^*\in\mathcal Y^*$, then $y^*\circ A=A'(y^*)\in\mathcal X^*$. This defines a map $A^*:\mathcal Y^*\to\mathcal X^*$, where $A^*=A'|_{\mathcal Y^*}$. Hence

**1.2**
$$
\langle x,A^*(y^*)\rangle=\langle A(x),y^*\rangle
$$

for $x$ in $\mathcal X$ and $y^*$ in $\mathcal Y^*$. $A^*$ is called the *adjoint* of $A$.

Before exploring the concept let’s see how this compares with the definition of the adjoint of an operator on Hilbert space given in §II.2. There is a difference, but only a small one. When $\mathcal H$ is identified with $\mathcal H^*$, the dual space of $\mathcal H$, the identification is not linear but conjugate linear (if $\mathbb F=\mathbb C$). The isometry $h\mapsto L_h$ of $\mathcal H$ onto $\mathcal H^*$, where $L_h(f)=\langle f,h\rangle$, satisfies $L_{\alpha h}=\bar\alpha L_h$. Thus the definition of $A^*$ given in (1.2) above is not the same as the adjoint of an operator on Hilbert space, since in (1.2) $A^*$ is defined on $\mathcal Y^*$ and not some conjugate-linear isomorphic image of it. In particular, if the definition (1.2) is applied to a matrix $A$ acting on $\mathbb C^d$ considered as a Banach space, its adjoint corresponds to the transpose of $A$. If $\mathbb C^d$ is considered as a Hilbert space, then the matrix of $A^*$ is the conjugate transpose of the matrix of $A$. This difference will not confuse us but it will serve to explain minor differences that will appear in the treatment of the two types of adjoints. The first of these occurs in the next result.

**1.3. Proposition.** *If $\mathcal X$ and $\mathcal Y$ are Banach spaces, $A,B\in\mathcal B(\mathcal X,\mathcal Y)$, and $\alpha,\beta\in\mathbb F$, then $(\alpha A+\beta B)^*=\alpha A^*+\beta B^*$. Moreover, $A^*:(\mathcal Y^*,\mathrm{wk}^*)\to(\mathcal X^*,\mathrm{wk}^*)$ is continuous.*

Note the absence of conjugates. The proof is left to the reader.

If $A\in\mathcal B(\mathcal X,\mathcal Y)$, then it is easy to see that $A^*\in\mathcal B(\mathcal Y^*,\mathcal X^*)$. In fact, if $y^*\in\operatorname{ball}\mathcal Y^*$ and $x\in\operatorname{ball}\mathcal X$, then
$$
|\langle x,A^*y^*\rangle|=|\langle Ax,y^*\rangle|\leq\|Ax\|\leq\|A\|.
$$
Hence $\|A^*y^*\|\leq\|A\|$ if $y^*\in\operatorname{ball}\mathcal Y^*$, so that $\|A^*\|\leq\|A\|$. This implies that
