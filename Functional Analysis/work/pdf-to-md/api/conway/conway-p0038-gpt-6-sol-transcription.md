functions—not really functions. Since $\{0,2\pi\}$ has zero measure, there is really no ambiguity. In this way $L_{\mathbb C}^{2}[0,2\pi]$ can be identified with $L_{\mathbb C}^{2}(\partial\mathbb D)$, where the measure on $\partial\mathbb D$ is normalized arc-length measure (normalized so that the total measure of $\partial\mathbb D$ is 1). So $L_{\mathbb C}^{2}[0,2\pi]$ and $L_{\mathbb C}^{2}(\partial\mathbb D)$ are (naturally) isomorphic. Thus, Theorem 5.11 is a theorem about the Fourier transform of the circle.

The importance of Theorem 5.11 is not the fact that $L_{\mathbb C}^{2}[0,2\pi]$ and $l^{2}(\mathbb Z)$ are isomorphic, but that the Fourier transform is an isomorphism. The fact that these two spaces are isomorphic follows from the abstract result that all separable infinite dimensional Hilbert spaces are isomorphic (5.5).

## Exercises

1. Verify the statements in Example 5.3.

2. Define $V:L^{2}(0,\infty)\to L^{2}(0,\infty)$ by $(Vf)(t)=f(t-1)$ if $t>1$ and $(Vf)(t)=0$ if $t\leq 1$. Show that $V$ is an isometry that is not surjective.

3. Define $V:L^{2}(\mathbb R)\to L^{2}(\mathbb R)$ by $(Vf)(t)=f(t-1)$ and show that $V$ is an isomorphism (a unitary operator).

4. Let $\mathcal H$ be the Hilbert space of Example 1.8 and define $U:\mathcal H\to L^{2}(0,1)$ by $Uf=f'$. Show that $U$ is an isomorphism and find a formula for $U^{-1}$.

5. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $u:X\to\mathbb F$ be an $\Omega$-measurable function such that $\sup\{|u(x)|:x\in X\}<\infty$. Show that $U:L^{2}(X,\Omega,\mu)\to L^{2}(X,\Omega,\mu)$ defined by $Uf=uf$ is an isometry if and only if $|u(x)|=1$ a.e. $[\mu]$, in which case $U$ is surjective.

6. Let $\mathcal C=\{f\in C[0,2\pi]:f(0)=f(2\pi)\}$ and show that $\mathcal C$ is dense in $L^{2}[0,2\pi]$.

7. Show that $\{1/\sqrt{2\pi},\ (1/\sqrt{\pi})\cos nt,\ (1/\sqrt{\pi})\sin nt:1\leq n<\infty\}$ is a basis for $L^{2}[-\pi,\pi]$.

8. Let $(X,\Omega)$ be a measurable space and let $\mu,\nu$ be two $\sigma$-finite measures defined on $(X,\Omega)$. Suppose $\nu\ll\mu$ and $\phi$ is the Radon–Nikodym derivative of $\nu$ with respect to $\mu$ $(\phi=d\nu/d\mu)$. Define $V:L^{2}(\nu)\to L^{2}(\mu)$ by $Vf=\sqrt{\phi}f$. Show that $V$ is a well-defined linear isometry and $V$ is an isomorphism if and only if $\mu\ll\nu$ (that is, $\mu$ and $\nu$ are mutually absolutely continuous).

9. If $\mathcal H$ and $\mathcal K$ are Hilbert spaces and $U:\mathcal H\to\mathcal K$ is a surjective function such that $\langle Uf,Ug\rangle=\langle f,g\rangle$ for all vectors $f$ and $g$ in $\mathcal H$, then $U$ is linear.

## §6. The Direct Sum of Hilbert Spaces

Suppose $\mathcal H$ and $\mathcal K$ are Hilbert spaces. We want to define $\mathcal H\oplus\mathcal K$ so that it becomes a Hilbert space. This is not a difficult assignment. For any vector spaces $\mathcal X$ and $\mathcal Y$, $\mathcal X\oplus\mathcal Y$ is defined as the Cartesian product $\mathcal X\times\mathcal Y$ where the operations are defined on $\mathcal X\times\mathcal Y$ coordinatewise. That is, if elements of
