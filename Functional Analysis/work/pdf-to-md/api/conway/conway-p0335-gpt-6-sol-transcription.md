Hence $\|B\|\leq 1$. In addition, $\langle Bh,h\rangle=\langle f,(1+A^*A)f\rangle=\|f\|^2+\|Af\|^2\geq 0$, so (b) holds.

Put $C=A(1+A^*A)^{-1}=AB$; if $f\in\operatorname{dom}A^*A$ and $(1+A^*A)f=h$, then $\|Ch\|^2=\|Af\|^2\leq\|(1+A^*A)f\|^2=\|h\|^2$ by the argument used to prove (a). Hence $\|C\|\leq 1$, so (c) is proved.

Now to prove (e). Since $A$ is closed, it suffices to show that no nonzero vector in $\operatorname{gra}A$ is orthogonal to $\{h\oplus Ah:h\in\operatorname{dom}A^*A\}$. So let $g\in\operatorname{dom}A$ and suppose that for every $h$ in $\operatorname{dom}A^*A$,

$$
\begin{aligned}
0&=\langle g\oplus Ag,h\oplus Ah\rangle\\
&=\langle g,h\rangle+\langle Ag,Ah\rangle\\
&=\langle g,h\rangle+\langle g,A^*Ah\rangle\\
&=\langle g,(1+A^*A)h\rangle.
\end{aligned}
$$

So $g\perp\operatorname{ran}(1+A^*A)=\mathcal H$; hence $g=0$.

To prove (d), note that (e) implies that $\operatorname{dom}A^*A$ is dense. Now let $f,g\in\operatorname{dom}A^*A$; so $f,g\in\operatorname{dom}A$ and $Af,Ag\in\operatorname{dom}A^*$. Hence $\langle A^*Af,g\rangle=\langle Af,Ag\rangle=\langle f,A^*Ag\rangle$. Thus $A^*A$ is symmetric. Also, $1+A^*A$ has a bounded inverse. This implies two things. First, $1+A^*A$ is closed, and so $A^*A$ is closed. Also, $-1\notin\sigma(A^*A)$ so that by Corollary 2.10, $A^*A$ is self-adjoint. $\blacksquare$

**4.3. Proposition.** *If $N$ is a normal operator, then $\operatorname{dom}N=\operatorname{dom}N^*$ and $\|Nf\|=\|N^*f\|$ for every $f$ in $\operatorname{dom}N$.*

**Proof.** First observe that if $h\in\operatorname{dom}N^*N=\operatorname{dom}NN^*$, then $Nh\in\operatorname{dom}N^*$ and $N^*h\in\operatorname{dom}N$. Hence $\|Nh\|^2=\langle N^*Nh,h\rangle=\langle NN^*h,h\rangle=\|N^*h\|^2$. Now if $f\in\operatorname{dom}N$, (4.2e) implies that there is a sequence $\{h_n\}$ in $\operatorname{dom}N^*N$ such that $h_n\oplus Nh_n\to f\oplus Nf$; so $\|Nh_n-Nf\|\to 0$. But from the first part of this proof, $\|N^*h_n-N^*h_m\|=\|Nh_n-Nh_m\|$. So there is a $g$ in $\mathcal H$ such that $N^*h_n\to g$. Thus $h_n\oplus N^*h_n\to f\oplus g$. But $N^*$ is closed; thus $f\in\operatorname{dom}N^*$ and $g=N^*f$. So $\operatorname{dom}N\subseteq\operatorname{dom}N^*$ and $\|Nf\|=\lim\|Nh_n\|=\lim\|N^*h_n\|=\|N^*f\|$.

On the other hand, $N^*$ is normal (Why?), and so $\operatorname{dom}N^*\subseteq\operatorname{dom}N^{**}=\operatorname{dom}N$. $\blacksquare$

**4.4. Lemma.** *Let $\mathcal H_1,\mathcal H_2,\ldots$ be Hilbert spaces and let $A_n\in\mathcal B(\mathcal H_n)$ for all $n\geq 1$. If $\mathcal D=\{(h_n)\in\bigoplus_n\mathcal H_n:\sum_{n=1}^{\infty}\|A_nh_n\|^2<\infty\}$ and $A$ is defined on $\mathcal H=\bigoplus_n\mathcal H_n$ by $A(h_n)=(A_nh_n)$ whenever $(h_n)\in\mathcal D$, then $A\in\mathcal C(\mathcal H)$. $A$ is a normal operator if and only if each $A_n$ is normal.*

**Proof.** Since $\mathcal H_n\subseteq\mathcal D$ for each $n$, $\mathcal D$ is dense in $\mathcal H$. Clearly $A$ is linear. If $\{h^{(j)}\}\subseteq\operatorname{dom}A$ and $h^{(j)}\oplus Ah^{(j)}\to h\oplus g$ in $\mathcal H\oplus\mathcal H$, then for each $n$, $h_n^{(j)}\oplus A_nh_n^{(j)}\to h_n\oplus g_n$. Since $A_n$ is bounded, $A_nh_n=g_n$. Hence $\sum_n\|Ah_n\|^2=\sum\|g_n\|^2=\|g\|^2<\infty$; so $h\in\operatorname{dom}A$. Clearly $Ah=g$, so $A\in\mathcal C(\mathcal H)$.

It is left to the reader to show that $\operatorname{dom}A^*=\{(h_n)\in\mathcal H:\sum_{n=1}^{\infty}\|A_n^*h_n\|^2<\infty\}$ and $A^*(h_n)=(A_n^*h_n)$ when $(h_n)\in\operatorname{dom}A^*$. From this the rest of the lemma easily follows. $\blacksquare$
