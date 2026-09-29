**3.7. Proposition.** If $A\in\mathcal{B}(\mathcal{H})$, $\mathcal{M}\leq\mathcal{H}$, and $P=P_{\mathcal{M}}$, then statements (a) through (c) are equivalent.

(a) $\mathcal{M}$ is invariant for $A$.  
(b) $PAP=AP$.  
(c) In (3.6), $Y=0$.

Also, statements (d) through (g) are equivalent.

(d) $\mathcal{M}$ reduces $A$.  
(e) $PA=AP$.  
(f) In (3.6), $Y$ and $X$ are $0$.  
(g) $\mathcal{M}$ is invariant for both $A$ and $A^*$.

**Proof.** (a)$\Rightarrow$(b): If $h\in\mathcal{H}$, $Ph\in\mathcal{M}$. So $APh\in\mathcal{M}$. Hence, $P(APh)=APh$. That is, $PAP=AP$.

(b)$\Rightarrow$(c): If $P$ is represented as a $2\times2$ operator matrix relative to $\mathcal{H}=\mathcal{M}\oplus\mathcal{M}^{\perp}$, then

$$
P=\begin{bmatrix}I&0\\0&0\end{bmatrix}.
$$

Hence,

$$
PAP=\begin{bmatrix}W&0\\0&0\end{bmatrix}
=AP=\begin{bmatrix}W&0\\Y&0\end{bmatrix}.
$$

So $Y=0$.

(c)$\Rightarrow$(a): If $Y=0$ and $h\in\mathcal{M}$, then

$$
Ah=\begin{bmatrix}W&X\\0&Z\end{bmatrix}
\begin{bmatrix}h\\0\end{bmatrix}
=\begin{bmatrix}Wh\\0\end{bmatrix}\in\mathcal{M}.
$$

(d)$\Rightarrow$(e): Since both $\mathcal{M}$ and $\mathcal{M}^{\perp}$ are invariant for $A$, (b) implies that $AP=PAP$ and $A(I-P)=(I-P)A(I-P)$. Multiplying this second equation gives $A-AP=A-AP-PA+PAP$. Thus $PA=PAP=AP$.

(e)$\Rightarrow$(f): Exercise.

(f)$\Rightarrow$(g): If $X=Y=0$, then

$$
A=\begin{bmatrix}W&0\\0&Z\end{bmatrix}
\quad\text{and}\quad
A^*=\begin{bmatrix}W^*&0\\0&Z^*\end{bmatrix}.
$$

By (c), $\mathcal{M}$ is invariant for both $A$ and $A^*$.

(g)$\Rightarrow$(d): If $h\in\mathcal{M}^{\perp}$ and $g\in\mathcal{M}$, then $\langle g,Ah\rangle=\langle A^*g,h\rangle=0$ since $A^*g\in\mathcal{M}$. Since $g$ was an arbitrary vector in $\mathcal{M}$, $Ah\in\mathcal{M}^{\perp}$. That is, $A\mathcal{M}^{\perp}\subseteq\mathcal{M}^{\perp}$. $\blacksquare$

If $\mathcal{M}$ reduces $A$, then $X=Y=0$ in (3.6). This says that a study of $A$ is reduced to the study of the smaller operators $W$ and $Z$. This is the reason for the terminology.

If $A\in\mathcal{B}(\mathcal{H})$ and $\mathcal{M}$ is an invariant subspace for $A$, then $A|_{\mathcal{M}}$ is used to denote the restriction of $A$ to $\mathcal{M}$. That is, $A|_{\mathcal{M}}$ is the operator on $\mathcal{M}$ defined
