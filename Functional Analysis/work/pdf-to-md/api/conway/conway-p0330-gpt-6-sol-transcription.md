Now let $B$ be a closed symmetric extension of $A$. By Lemma 2.15 there is an $A$-symmetric, $A$-closed manifold $\mathcal M$ in $\mathcal L_+ + \mathcal L_-$ such that $\operatorname{gra}B=\operatorname{gra}A+\operatorname{gra}(A^*|\mathcal M)$. If $f\in\mathcal M$, let $f=f^++f^-$, where $f^\pm\in\mathcal L_\pm$; put $I_+=\{f^+:f\in\mathcal M\}$. Since $\mathcal M$ is $A$-symmetric, $0=\langle A^*f,f\rangle-\langle f,A^*f\rangle=2i\langle f^+,f^+\rangle-2i\langle f^-,f^-\rangle$; hence $\|f^+\|=\|f^-\|$ for all $f$ in $\mathcal M$. So if $Wf^+=f^-$ whenever $f=f^++f^-\in\mathcal M$ and if $I_+$ is closed, $W$ is a partial isometry and (2.18) and (2.19) are easily seen to hold. It remains to show that $I_+$ is closed. Suppose $\{f_n\}\subseteq\mathcal M$ and $f_n^+\to g^+$ in $\mathcal L_+$. Since $\|f_n^+-f_m^+\|=\|f_n^--f_m^-\|$, there is a $g^-$ in $\mathcal L_-$ such that $f_n^-\to g^-$. Clearly $f_n\to g^++g^-=g$. Also, $A^*f_n^\pm=\pm if_n^\pm\to\pm ig^\pm$. It follows that $g\oplus A^*g\in\operatorname{cl}\operatorname{gra}(A^*|\mathcal M)=\operatorname{gra}(A^*|\mathcal M)$; thus $g^+\in I_+$. $\blacksquare$

**2.20. Theorem.** Let $A$ be a closed symmetric operator with deficiency indices $n_\pm$.

(a) $A$ is self-adjoint if and only if $n_+=n_-=0$.

(b) $A$ has a self-adjoint extension if and only if $n_+=n_-$. In this case the set of self-adjoint extensions is in natural correspondence with the set of isomorphisms of $\mathcal L_+$ onto $\mathcal L_-$.

(c) $A$ is a maximal symmetric operator that is not self-adjoint if and only if either $n_+=0$ and $n_->0$ or $n_+>0$ and $n_-=0$.

**Proof.** Part (a) is a rephrasing of Corollary 2.9. For (b), $n_+=n_-$ if and only if $\mathcal L_+$ and $\mathcal L_-$ are isomorphic. But this is equivalent to stating that there is a partial isometry on $\mathcal H$ with initial and final spaces $\mathcal L_+$ and $\mathcal L_-$, respectively. Part (c) follows easily from the preceding theorem. $\blacksquare$

**2.21. Example.** Let $A$ and $\mathcal D$ be as in Example 1.11; so $A$ is symmetric. The operator $B$ of Example 1.12 is a self-adjoint extension of $A$. Let us determine all self-adjoint extensions of $A$. To do this it is necessary to determine $\mathcal L_\pm$. Now $f\in\mathcal L_\pm$ if and only if $f\in\operatorname{dom}A^*$ and $\pm if=A^*f=if'$, so $\mathcal L_\pm=\{\alpha e^{\pm x}:\alpha\in\mathbb C\}$. Hence $n_\pm=1$. Also, the isomorphisms of $\mathcal L_+$ onto $\mathcal L_-$ are all of the form $W_\lambda e^x=\lambda e^{-x}$ where $|\lambda|=e$. If $|\lambda|=e$, let

$$
\mathcal D_\lambda\equiv\{f+\alpha e^x+\lambda\alpha e^{-x}:\alpha\in\mathbb C,\ f\in\mathcal D\}.
$$

$$
A_\lambda(f+\alpha e^x+\lambda\alpha e^{-x})
=if'+\alpha ie^x-i\lambda\alpha e^{-x},
$$

if $f\in\mathcal D$, $\alpha\in\mathbb C$.

According to Theorem 2.17, $\{(A_\lambda,\mathcal D_\lambda):|\lambda|=e\}$ are all of the self-adjoint extensions of $A$. The operator $B$ of Example 1.12 is the extension $A_e$.

For more information on symmetric operators and the relation of the problem of finding self-adjoint extensions to physical problems, see Reed and Simon [1975] from which much of the present development is taken.

## EXERCISES

1. If $A$ is symmetric, show that all of the eigenvalues of $A$ are real.

2. If $A$ is symmetric and $\lambda,\mu$ are distinct eigenvalues, show that $\ker(A-\lambda)\perp\ker(A-\mu)$.
