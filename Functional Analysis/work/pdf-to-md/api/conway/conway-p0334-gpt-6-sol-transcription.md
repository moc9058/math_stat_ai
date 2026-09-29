8. Let $U=S^*$, where $S$ is the unilateral shift of multiplicity 1. Is $U$ the Cayley transform of a symmetric operator $A$? If so, find it.

## §4. Unbounded Normal Operators and the Spectral Theorem

If $A$ is self-adjoint, the classical way to obtain the spectral decomposition of $A$ is to let $U$ be the Cayley transform of $A$, obtain the spectral decomposition of $U$, and then use the inverse Cayley transform to translate this back to a decomposition for $A$. There is a spectral theorem for unbounded normal operators, however, and the Cayley transform is not applicable here.

In this section the approach is to prove the spectral theorem for normal operators by using that theorem for the bounded case. The spectral theorem for self-adjoint operators is then only a special case.

**4.1. Definition.** A linear operator $N$ on $\mathcal{H}$ is *normal* if $N$ is closed, densely defined, and $N^*N=NN^*$.

Note that the equation $N^*N=NN^*$ that appears in Definition 4.1 implicitly carries the condition that $\operatorname{dom}N^*N=\operatorname{dom}NN^*$. The operators in Examples 1.9 and 1.10 are normal and every self-adjoint operator is normal. Examining Example 1.9 it is easy to see that for a normal operator it is not necessarily the case that $\operatorname{dom}N^*N=\operatorname{dom}N$.

Parts of the next result have appeared in various exercises in this chapter, but a complete proof is given here.

**4.2. Proposition.** *If $A\in\mathcal{C}(\mathcal{H})$, then*

(a) *$1+A^*A$ has a bounded inverse defined on all of $\mathcal{H}$.*

(b) *If $B=(1+A^*A)^{-1}$, then $\|B\|\leqslant 1$ and $B\geqslant 0$.*

(c) *The operator $C=A(1+A^*A)^{-1}$ is a contraction.*

(d) *$A^*A$ is self-adjoint.*

(e) *$\{h\oplus Ah:h\in\operatorname{dom}A^*A\}$ is dense in $\operatorname{gra}A$.*

**Proof.** Define $J:\mathcal{H}\oplus\mathcal{H}\to\mathcal{H}\oplus\mathcal{H}$ by $J(h\oplus k)=(-k)\oplus h$. By Lemma 1.7, $\operatorname{gra}A^*=[J\operatorname{gra}A]^\perp$. So if $h\in\mathcal{H}$, there are $f$ in $\operatorname{dom}A$ and $g$ in $\operatorname{dom}A^*$ such that $0\oplus h=J(f\oplus Af)+g\oplus A^*g=(-Af)\oplus f+g\oplus A^*g$. Hence $0=-Af+g$, or $g=Af$; also, $h=f+A^*g=f+A^*Af=(1+A^*A)f$. Thus $\operatorname{ran}(1+A^*A)=\mathcal{H}$.

Also, for $f$ in $\operatorname{dom}A^*A$, $Af\in\operatorname{dom}A^*$ and $\|f+A^*Af\|^2=\|f\|^2+2\|Af\|^2+\|A^*Af\|^2\geqslant\|f\|^2$. Hence $\ker(1+A^*A)=(0)$. Thus $(1+A^*A)^{-1}$ exists and is defined on all of $\mathcal{H}$. In the next paragraph (the proof of (b)) it will be shown that $(1+A^*A)^{-1}$ is a contraction, completing the proof of (a).

It was shown that $\|(1+A^*A)f\|\geqslant\|f\|$ whenever $f\in\operatorname{dom}A^*A$. If $h=(1+A^*A)f$ and $B=(1+A^*A)^{-1}$, then this implies that $\|Bh\|\leqslant\|h\|$.
