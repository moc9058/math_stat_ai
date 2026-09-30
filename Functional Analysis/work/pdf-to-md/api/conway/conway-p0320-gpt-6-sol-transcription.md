$$
\operatorname{dom}A^*=\{k\in\mathcal K:h\mapsto\langle Ah,k\rangle\text{ is a bounded linear functional on }\operatorname{dom}A\}.
$$

Because $\operatorname{dom}A$ is dense in $\mathcal H$, if $k\in\operatorname{dom}A^*$, then there is a unique vector $f$ in $\mathcal H$ such that $\langle Ah,k\rangle=\langle h,f\rangle$ for all $h$ in $\operatorname{dom}A$. Denote this unique vector $f$ by $f=A^*k$. Thus

$$
\langle Ah,k\rangle=\langle h,A^*k\rangle
$$

for $h$ in $\operatorname{dom}A$ and $k$ in $\operatorname{dom}A^*$.

**1.6. Proposition.** If $A:\mathcal H\to\mathcal K$ is a densely defined operator, then:

(a) $A^*$ is a closed operator;  
(b) $A^*$ is densely defined if and only if $A$ is closable;  
(c) if $A$ is closable, then its closure is $(A^*)^*\equiv A^{**}$.

Before proving this, a lemma is needed which will also be useful later.

**1.7. Lemma.** If $A:\mathcal H\to\mathcal K$ is densely defined and $J:\mathcal H\oplus\mathcal K\to\mathcal K\oplus\mathcal H$ is defined by $J(h\oplus k)=(-k)\oplus h$, then $J$ is an isomorphism and

$$
\operatorname{gra}A^*=[J\operatorname{gra}A]^\perp.
$$

**Proof.** It is clear that $J$ is an isomorphism. To prove the formula for $\operatorname{gra}A^*$, note that $\operatorname{gra}A^*=\{k\oplus A^*k\in\mathcal K\oplus\mathcal H:k\in\operatorname{dom}A^*\}$. So if $k\in\operatorname{dom}A^*$ and $h\in\operatorname{dom}A$,

$$
\begin{aligned}
\langle k\oplus A^*k,J(h\oplus Ah)\rangle
&=\langle k\oplus A^*k,-Ah\oplus h\rangle\\
&=-\langle k,Ah\rangle+\langle A^*k,h\rangle=0.
\end{aligned}
$$

Thus $\operatorname{gra}A^*\subseteq[J\operatorname{gra}A]^\perp$. Conversely, if $k\oplus f\in[J\operatorname{gra}A]^\perp$, then for every $h$ in $\operatorname{dom}A$, $0=\langle k\oplus f,-Ah\oplus h\rangle=-\langle k,Ah\rangle+\langle f,h\rangle$, so $\langle Ah,k\rangle=\langle h,f\rangle$. By definition $k\in\operatorname{dom}A^*$ and $A^*k=f$. $\blacksquare$

**Proof of Proposition 1.6.** The proof of (a) is clear from Lemma 1.7. For the remainder of the proof notice that because the map $J$ in (1.7) is an isomorphism, $J^*=J^{-1}$ and so $J^*(k\oplus h)=h\oplus(-k)$.

(b) Assume $A$ is closable and let $k_0\in(\operatorname{dom}A^*)^\perp$. We want to show that $k_0=0$. Thus $k_0\oplus0\in[\operatorname{gra}A^*]^\perp=[J\operatorname{gra}A]^{\perp\perp}=\operatorname{cl}[J\operatorname{gra}A]=J[\operatorname{cl}(\operatorname{gra}A)]$. So $0\oplus-k_0=J^*(k_0\oplus0)\in J^*J[(\operatorname{gra}A)]=\operatorname{cl}(\operatorname{gra}A)$. But because $A$ is closable, $\operatorname{cl}(\operatorname{gra}A)$ is a graph; hence $k_0=0$. For the converse, assume $\operatorname{dom}A^*$ is dense in $\mathcal K$. Thus $A^{**}\equiv(A^*)^*$ is defined. By (a), $A^{**}$ is a closed operator. It is easy to see that $A\subseteq A^{**}$, so $A$ has a closed extension.

(c) Note that by Lemma 1.7 $\operatorname{gra}A^{**}=[J^*\operatorname{gra}A^*]^\perp=[J^*[J\operatorname{gra}A]^\perp]^\perp$. But for any linear manifold $\mathcal M$ and any isomorphism $J$, $(J\mathcal M)^\perp=J(\mathcal M^\perp)$. Hence $J^*[(J\mathcal M)^\perp]=\mathcal M^\perp$ and, thus, $[J^*[J\mathcal M]^\perp]^\perp=\mathcal M^{\perp\perp}=\operatorname{cl}\mathcal M$. Putting $\mathcal M=\operatorname{gra}A$ gives that $\operatorname{gra}A^{**}=\operatorname{cl}\operatorname{gra}A$. $\blacksquare$

**1.8. Corollary.** If $A\in\mathcal C(\mathcal H,\mathcal K)$, then $A^*\in\mathcal C(\mathcal K,\mathcal H)$ and $A^{**}=A$.
