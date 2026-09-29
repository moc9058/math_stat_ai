If $A\subseteq\mathcal{H}$, Let $A^\perp\equiv\{f\in\mathcal{H}:f\perp g\text{ for all }g\text{ in }A\}$. It is easy to see that $A^\perp$ is a closed linear subspace of $\mathcal{H}$.

Note that Theorem 2.6, together with the uniqueness statement in Theorem 2.5, shows that if $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$ and $h\in\mathcal{H}$, then there is a unique element $f_0$ in $\mathcal{M}$ such that $h-f_0\in\mathcal{M}^\perp$. Thus a function $P:\mathcal{H}\to\mathcal{M}$ can be defined by $Ph=f_0$.

**2.7. Theorem.** If $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$ and $h\in\mathcal{H}$, let $Ph$ be the unique point in $\mathcal{M}$ such that $h-Ph\perp\mathcal{M}$. Then

(a) $P$ is a linear transformation on $\mathcal{H}$,

(b) $\|Ph\|\leq\|h\|$ for every $h$ in $\mathcal{H}$,

(c) $P^2=P$ (here $P^2$ means the composition of $P$ with itself),

(d) $\ker P=\mathcal{M}^\perp$ and $\operatorname{ran}P=\mathcal{M}$.

**Proof.** Keep in mind that for every $h$ in $\mathcal{H}$, $h-Ph\in\mathcal{M}^\perp$ and $\|h-Ph\|=\operatorname{dist}(h,\mathcal{M})$.

(a) Let $h_1,h_2\in\mathcal{H}$ and $\alpha_1,\alpha_2\in\mathbb{F}$. If $f\in\mathcal{M}$, then
$$
\left\langle[\alpha_1h_1+\alpha_2h_2]-[\alpha_1Ph_1+\alpha_2Ph_2],f\right\rangle
=\alpha_1\langle h_1-Ph_1,f\rangle+\alpha_2\langle h_2-Ph_2,f\rangle=0.
$$
By the uniqueness statement of (2.6), $P(\alpha_1h_1+\alpha_2h_2)=\alpha_1Ph_1+\alpha_2Ph_2$.

(b) If $h\in\mathcal{H}$, then $h=(h-Ph)+Ph$, $Ph\in\mathcal{M}$, and $h-Ph\in\mathcal{M}^\perp$. Thus
$$
\|h\|^2=\|h-Ph\|^2+\|Ph\|^2\geq\|Ph\|^2.
$$

(c) If $f\in\mathcal{M}$, then $Pf=f$. For any $h$ in $\mathcal{H}$, $Ph\in\mathcal{M}$; hence $P^2h\equiv P(Ph)=Ph$. That is, $P^2=P$.

(d) If $Ph=0$, then $h=h-Ph\in\mathcal{M}^\perp$. Conversely, if $h\in\mathcal{M}^\perp$, then $0$ is the unique vector in $\mathcal{M}$ such that $h-0=h\perp\mathcal{M}$. Therefore $Ph=0$. That $\operatorname{ran}P=\mathcal{M}$ is clear. ■

**2.8. Definition.** If $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$ and $P$ is the linear map defined in the preceding theorem, then $P$ is called the *orthogonal projection* of $\mathcal{H}$ onto $\mathcal{M}$. If we wish to show this dependence of $P$ on $\mathcal{M}$, we will denote the orthogonal projection of $\mathcal{H}$ onto $\mathcal{M}$ by $P_{\mathcal{M}}$.

It also seems appropriate to introduce the notation $\mathcal{M}\leq\mathcal{H}$ to signify that $\mathcal{M}$ is a closed linear subspace of $\mathcal{H}$. We will use the term *linear manifold* to designate a linear subspace of $\mathcal{H}$ that is not necessarily closed. A *linear subspace* of $\mathcal{H}$ will always mean a closed linear subspace.

**2.9. Corollary.** If $\mathcal{M}\leq\mathcal{H}$, then $(\mathcal{M}^\perp)^\perp=\mathcal{M}$.

**Proof.** If $I$ is used to designate the identity operator on $\mathcal{H}$ (viz., $Ih=h$) and $P=P_{\mathcal{M}}$, then $I-P$ is the orthogonal projection of $\mathcal{H}$ onto $\mathcal{M}^\perp$ (Exercise 2). By part (d) of the preceding theorem, $(\mathcal{M}^\perp)^\perp=\ker(I-P)$. But $0=(I-P)h$ iff $h=Ph$. Thus $(\mathcal{M}^\perp)^\perp=\ker(I-P)=\operatorname{ran}P=\mathcal{M}$. ■

**2.10. Corollary.** If $A\subseteq\mathcal{H}$, then $(A^\perp)^\perp$ is the closed linear span of $A$ in $\mathcal{H}$.
