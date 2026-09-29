which is weak-star open in $\mathcal X^*$. Hence $\tilde\rho:(\mathcal X^*/\mathcal M^\perp,\eta^*)\to(\mathcal M^*,\mathrm{wk}^*)$ is continuous.

How is the topology on $\mathcal X^*/\mathcal M^\perp$ defined? If $x\in\mathcal X$, $p_x(x^*)=|\langle x,x^*\rangle|$ is a typical seminorm on $\mathcal X^*$. By Proposition 2.1, the topology on $\mathcal X^*/\mathcal M^\perp$ is defined by the seminorms $\{\bar p_x:x\in\mathcal X\}$, where

$$
\bar p_x(x^*+\mathcal M^\perp)
=\inf\{|\langle x,x^*+z^*\rangle|:z^*\in\mathcal M^\perp\}.
$$

**2.4. Claim.** If $x\notin\mathcal M$, then $\bar p_x=0$.

In fact, let $\mathcal L=\{\alpha x:\alpha\in\mathbb F\}$. If $x\notin\mathcal M$, then $\mathcal L\cap\mathcal M=(0)$. Since $\dim\mathcal L<\infty$, $\mathcal M$ is topologically complemented in $\mathcal L+\mathcal M$. Let $x^*\in\mathcal X^*$ and define $f:\mathcal L+\mathcal M\to\mathbb F$ by $f(\alpha x+y)=\langle y,x^*\rangle$ for $y$ in $\mathcal M$ and $\alpha$ in $\mathbb F$. Because $\mathcal M$ is topologically complemented in $\mathcal L+\mathcal M$, if $\alpha_i x+y_i\to0$, then $y_i\to0$. Hence $f(\alpha_i x+y_i)=\langle y_i,x^*\rangle\to0$. Thus $f$ is continuous. By the Hahn–Banach Theorem, there is an $x_1^*$ in $\mathcal X^*$ that extends $f$. Note that $x^*-x_1^*\in\mathcal M^\perp$. Thus $\bar p_x(x^*+\mathcal M^\perp)=\bar p_x(x_1^*+\mathcal M^\perp)\leq p_x(x_1^*)=|\langle x,x_1^*\rangle|=0$. This proves (2.4).

Now suppose that $\{x_i^*+\mathcal M^\perp\}$ is a net in $\mathcal X^*/\mathcal M^\perp$ such that $\tilde\rho(x_i^*+\mathcal M^\perp)=x_i^*|_{\mathcal M}\to0(\mathrm{wk}^*)$ in $\mathcal M^*$. If $x\in\mathcal X$ and $x\notin\mathcal M$, the Claim (2.4) implies that $\bar p_x(x_i^*+\mathcal M^\perp)=0$. If $x\in\mathcal M$, then $\bar p_x(x_i^*+\mathcal M^\perp)\leq|\langle x,x_i^*\rangle|\to0$. Thus $x_i^*+\mathcal M^\perp\to0(\eta^*)$ and $\tilde\rho$ is a weak-star homeomorphism. ■

## Exercises

1. In relation to Claim 2.4, show that if $\mathcal L\leq\mathcal X$, $\dim\mathcal L<\infty$, and $\mathcal M\leq\mathcal X$, then $\mathcal L+\mathcal M$ is closed.

2. Show that if $\mathcal M\leq\mathcal X$ and $\mathcal M$ is topologically complemented in $\mathcal X$, then $\mathcal M^\perp$ is topologically complemented in $\mathcal X^*$ and that its complement is weak-star and linearly homeomorphic to $\mathcal X^*/\mathcal M^\perp$.

## §3. Alaoglu’s Theorem

If $\mathcal X$ is any normed space, let’s agree to denote by $\operatorname{ball}\mathcal X$ the closed unit ball in $\mathcal X$. So $\operatorname{ball}\mathcal X\equiv\{x\in\mathcal X:\|x\|\leq1\}$.

**3.1. Alaoglu’s Theorem.** *If $\mathcal X$ is a normed space, then $\operatorname{ball}\mathcal X^*$ is weak-star compact.*

**Proof.** For each $x$ in $\operatorname{ball}\mathcal X$, let $D_x\equiv\{\alpha\in\mathbb F:|\alpha|\leq1\}$ and put $D=\prod\{D_x:x\in\operatorname{ball}\mathcal X\}$. By Tychonoff’s Theorem, $D$ is compact. Define $\tau:\operatorname{ball}\mathcal X^*\to D$ by

$$
\tau(x^*)(x)=\langle x,x^*\rangle.
$$

That is, $\tau(x^*)$ is the element of the product space $D$ whose $x$ coordinate is $\langle x,x^*\rangle$. It will be shown that $\tau$ is a homeomorphism from $(\operatorname{ball}\mathcal X^*,\mathrm{wk}^*)$
