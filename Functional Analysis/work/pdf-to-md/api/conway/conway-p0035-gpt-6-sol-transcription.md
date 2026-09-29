**Proof.** Assume $\langle Vh,Vg\rangle=\langle h,g\rangle$ for all $h,g$ in $\mathcal H$. Then $\|Vh\|^2=\langle Vh,Vh\rangle=\langle h,h\rangle=\|h\|^2$ and $V$ is an isometry.

Now assume that $V$ is an isometry. If $h,g\in\mathcal H$ and $\lambda\in\mathbb F$, then $\|h+\lambda g\|^2=\|Vh+\lambda Vg\|^2$. Using the polar identity on both sides of this equation gives

$$
\|h\|^2+2\operatorname{Re}\bar\lambda\langle h,g\rangle+|\lambda|^2\|g\|^2
=\|Vh\|^2+2\operatorname{Re}\bar\lambda\langle Vh,Vg\rangle+|\lambda|^2\|Vg\|^2.
$$

But $\|Vh\|=\|h\|$ and $\|Vg\|=\|g\|$, so this equation becomes

$$
\operatorname{Re}\bar\lambda\langle h,g\rangle
=\operatorname{Re}\bar\lambda\langle Vh,Vg\rangle
$$

for any $\lambda$ in $\mathbb F$. If $\mathbb F=\mathbb R$, take $\lambda=1$. If $\mathbb F=\mathbb C$, first take $\lambda=1$ and then take $\lambda=i$ to find that $\langle h,g\rangle$ and $\langle Vh,Vg\rangle$ have the same real and imaginary parts. $\blacksquare$

Note that an isometry between metric spaces maps Cauchy sequences into Cauchy sequences. Thus an isomorphism also preserves completeness. That is, if an inner product space is isomorphic to a Hilbert space, then it must be complete.

**5.3. Example.** Definite $S:l^2\to l^2$ by $S(\alpha_1,\alpha_2,\ldots)=(0,\alpha_1,\alpha_2,\ldots)$. Then $S$ is an isometry that is not surjective.

The preceding example shows that isometries need not be isomorphisms.

A word about terminology. Many call what we call an isomorphism a unitary operator. We shall define a *unitary operator* as a linear transformation $U:\mathcal H\to\mathcal H$ that is a surjective isometry. That is, a unitary operator is an isomorphism whose range coincides with its domain. This may seem to be a minor distinction, and in many ways it is. But experience has taught me that there is some benefit in making such a distinction, or at least in being aware of it.

**5.4. Theorem.** *Two Hilbert spaces are isomorphic if and only if they have the same dimension.*

**Proof.** If $U:\mathcal H\to\mathcal K$ is an isomorphism and $\mathcal E$ is a basis for $\mathcal H$, then it is easy to see that $U\mathcal E\equiv\{Ue:e\in\mathcal E\}$ is a basis for $\mathcal K$. Hence, $\dim\mathcal H=\dim\mathcal K$.

Let $\mathcal H$ be a Hilbert space and let $\mathcal E$ be a basis for $\mathcal H$. Consider the Hilbert space $l^2(\mathcal E)$. If $h\in\mathcal H$, define $\hat h:\mathcal E\to\mathbb F$ by $\hat h(e)=\langle h,e\rangle$. By Parseval’s Identity $\hat h\in l^2(\mathcal E)$ and $\|h\|=\|\hat h\|$. Define $U:\mathcal H\to l^2(\mathcal E)$ by $Uh=\hat h$. Thus $U$ is linear and an isometry. It is easy to see that $\operatorname{ran}U$ contains all the functions $f$ in $l^2(\mathcal E)$ such that $f(e)=0$ for all but a finite number of $e$; that is, $\operatorname{ran}U$ is dense. But $U$, being an isometry, must have closed range. Hence $U:\mathcal H\to l^2(\mathcal E)$ is an isomorphism.
