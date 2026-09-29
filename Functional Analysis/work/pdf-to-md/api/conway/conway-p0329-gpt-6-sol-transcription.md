So $B=A^*|_{\mathcal D}$ is symmetric. Note that $\operatorname{gra}A\perp\operatorname{gra}(A^*|_{\mathcal M})$ in $\mathcal H\oplus\mathcal H$. Since both of these spaces are closed, $\operatorname{gra}B$, given by (2.16), is closed.

Now let $B$ be any closed symmetric extension of $A$. As discussed before, $A\subseteq B\subseteq A^*$; so $\operatorname{gra}A\subseteq\operatorname{gra}B\subseteq\operatorname{gra}A^*=\operatorname{gra}A\oplus\mathcal H_+\oplus\mathcal H_-$. Let $\mathcal G=\operatorname{gra}B\cap(\mathcal H_+\oplus\mathcal H_-)$ and let $\mathcal M=$ the set of first coordinates of elements in $\mathcal G$. Clearly, $\mathcal M$ is a manifold in $\mathcal L_++\mathcal L_-$ and $\mathcal M\subseteq\operatorname{dom}B$. Hence for $f,g$ in $\mathcal M$, $\langle A^*f,g\rangle=\langle Bf,g\rangle=\langle f,Bg\rangle=\langle f,A^*g\rangle$. So $\mathcal M$ is $A$-symmetric. Clearly, $\operatorname{gra}(A^*|_{\mathcal M})=\mathcal G$, so $\mathcal M$ is $A$-closed. If $h\oplus Bh\in\operatorname{gra}B$, let $h\oplus Bh=(f\oplus Af)+k$ where $f\in\operatorname{dom}A$ and $k\in\mathcal H_+\oplus\mathcal H_-$. Since $A\subseteq B$, $k\in\operatorname{gra}B$; so $k\in\mathcal G$. This shows that (2.16) holds. ■

**2.17. Theorem.** *Let $A$ be a closed symmetric operator. If $W$ is a partial isometry with initial space in $\mathcal L_+$ and final subspace in $\mathcal L_-$, let*

$$
\mathcal D_W=\{f+g+Wg:f\in\operatorname{dom}A,\ g\in\operatorname{initial}W\}. \tag{2.18}
$$

*and define $A_W$ on $\mathcal D_W$ by*

$$
A_W(f+g+Wg)=Af+ig-iWg. \tag{2.19}
$$

*Then $A_W$ is a closed symmetric extension of $A$. Conversely, if $B$ is any closed symmetric extension of $A$, then there is a unique partial isometry $W$ such that $B=A_W$ as in (2.19).*

*If $W$ is such a partial isometry and $W$ has finite rank, then*

$$
n_\pm(A_W)=n_\pm(A)-\dim(\operatorname{ran}W).
$$

**Proof.** Let $W$ be a partial isometry with initial space $I_+$ in $\mathcal L_+$ and final space $I_-$ in $\mathcal L_-$. Define $\mathcal D_W$ and $A_W$ as in (2.18) and (2.19). Let $\mathcal M=\{g+Wg:g\in I_+\}$; so $\mathcal M$ is a manifold in $\mathcal L_++\mathcal L_-$. If $g,h\in I_+$, then $\langle Wg,Wh\rangle=\langle g,h\rangle$. Hence $\langle A^*(g+Wg),h+Wh\rangle=\langle A^*g,h\rangle+\langle A^*g,Wh\rangle+\langle A^*Wg,h\rangle+\langle A^*Wg,Wh\rangle$. Since $g\in\ker(A^*-i)$ and $Wg\in\ker(A^*+i)$,

$$
\begin{aligned}
\langle A^*(g+Wg),h+Wh\rangle
&=i\langle g,h\rangle+i\langle g,Wh\rangle-i\langle Wg,h\rangle-i\langle Wg,Wh\rangle\\
&=i\langle g,Wh\rangle-i\langle Wg,h\rangle.
\end{aligned}
$$

Similarly, $\langle g+Wg,A^*(h+Wh)\rangle=i\langle g,Wh\rangle-i\langle Wg,h\rangle$, so that $\mathcal M$ is $A$-symmetric. If $\{g_n\}\subseteq I_+$ and $(g_n+Wg_n)\oplus(ig_n-iWg_n)\to f\oplus h$ in $\mathcal H\oplus\mathcal H$, then $2ig_n=i(g_n+Wg_n)+(ig_n-iWg_n)\to if+h$ and $2iWg_n=i(g_n+Wg_n)-(ig_n-iWg_n)\to if-h$. If $g=(2i)^{-1}(if+h)$, then $f=g+Wg$ and $h=ig-iWg$. Hence $\mathcal M$ is $A$-closed. By Lemma 2.15, $A_W$ is a closed symmetric extension of $A$.

To prove that $n_+(A_W)=n_+(A)-\dim I_+$, let $f\in\operatorname{dom}A$, $g\in I_+$. Then

$$
\begin{aligned}
(A_W+i)(f+g+Wg)&=(A+i)f+ig-iWg+ig+iWg\\
&=(A+i)f+2ig.
\end{aligned}
$$

Thus $\operatorname{ran}(A_W+i)=\operatorname{ran}(A+i)\oplus I_+$, and so $n_+(A_W)=\dim[\operatorname{ran}(A_W+i)]^\perp=\dim(\mathcal L_+\ominus I_+)=n_+(A)-\dim I_+$. Similarly, $n_-(A_W)=n_-(A)-\dim I_-=n_-(A)-\dim I_+$.
