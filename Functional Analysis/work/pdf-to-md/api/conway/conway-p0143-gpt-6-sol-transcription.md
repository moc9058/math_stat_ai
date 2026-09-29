3. Prove Theorem 1.3.

4. Let $\mathscr{X}$ be a complex LCS and let $\mathscr{X}_{\mathbb R}^{*}$ denote the collection of all continuous real linear functionals on $\mathscr{X}$. Use the elements of $\mathscr{X}_{\mathbb R}^{*}$ to define seminorms on $\mathscr{X}$ and let $\sigma(\mathscr{X},\mathscr{X}_{\mathbb R}^{*})$ be the corresponding topology. Show that $\sigma(\mathscr{X},\mathscr{X}^{*})=\sigma(\mathscr{X},\mathscr{X}_{\mathbb R}^{*})$.

5. Prove the remainder of Proposition 1.7.

6. If $A\subseteq\mathscr{X}$, show that $A$ is weakly bounded if and only if $A^{\circ}$ is absorbing in $\mathscr{X}^{*}$.

7. Let $\mathscr{X}$ be a normed space and let $\{x_n\}$ be a sequence in $\mathscr{X}$ such that $x_n\to x$ weakly. Show that there is a sequence $\{y_n\}$ such that $y_n\in\operatorname{co}\{x_1,x_2,\ldots,x_n\}$ and $\|y_n-x\|\to0$. (Hint: use Theorem 1.4.)

8. If $\mathscr{H}$ is a Hilbert space and $\{h_n\}$ is a sequence in $\mathscr{H}$ such that $h_n\to h$ weakly and $\|h_n\|\to\|h\|$, then $\|h_n-h\|\to0$. (The same type of result is true for $L^p$-spaces if $1<p<\infty$. See W.P. Novinger [1972].)

9. If $\mathscr{X}$ is a normed space show that the norm on $\mathscr{X}$ is lower semicontinuous for the weak topology and the norm of $\mathscr{X}^{*}$ is lower semicontinuous for the weak-star topology.

10. Suppose $\mathscr{X}$ is an infinite-dimensional normed space. If $S=\{x\in\mathscr{X}:\|x\|=1\}$, then the weak closure of $S$ is $\{x:\|x\|\leqslant1\}$.

## §2. The Dual of a Subspace and a Quotient Space

In §III.4 the quotient of a normed space $\mathscr{X}$ by a closed subspace $\mathcal{M}$ was defined and in (III.10.2) it was shown that the dual of a quotient space $\mathscr{X}/\mathcal{M}$ is isometrically isomorphic to $\mathcal{M}^{\perp}$. These results are generalized in this section to the setting of a LCS and, moreover, it is shown that when $(\mathscr{X}/\mathcal{M})^{*}$ and $\mathcal{M}^{\perp}$ are identified, the weak-star topology on $(\mathscr{X}/\mathcal{M})^{*}$ is precisely the relative weak-star topology that $\mathcal{M}^{\perp}$ receives as a subspace of $\mathscr{X}^{*}$.

The first result was presented in abbreviated form as Exercise IV.1.16.

**2.1. Proposition.** *If $p$ is a seminorm on $\mathscr{X}$, $\mathcal{M}$ is a linear manifold in $\mathscr{X}$, and $\bar p:\mathscr{X}/\mathcal{M}\to[0,\infty)$ is defined by*

$$
\bar p(x+\mathcal{M})=\inf\{p(x+y):y\in\mathcal{M}\},
$$

*then $\bar p$ is a seminorm on $\mathscr{X}/\mathcal{M}$. If $\mathscr{X}$ is a locally convex space and $\mathcal{P}$ is the family of all continuous seminorms on $\mathscr{X}$, then the family $\bar{\mathcal{P}}\equiv\{\bar p:p\in\mathcal{P}\}$ defines the quotient topology on $\mathscr{X}/\mathcal{M}$.*

**Proof.** Exercise.

Thus if $\mathscr{X}$ is a LCS and $\mathcal{M}\leqslant\mathscr{X}$, then $\mathscr{X}/\mathcal{M}$ is a LCS. Let $f\in(\mathscr{X}/\mathcal{M})^{*}$. If $Q:\mathscr{X}\to\mathscr{X}/\mathcal{M}$ is the natural map, then $f\circ Q\in\mathscr{X}^{*}$. Moreover, $f\circ Q\in\mathcal{M}^{\perp}$. Hence $f\mapsto f\circ Q$ is a map of $(\mathscr{X}/\mathcal{M})^{*}\to\mathcal{M}^{\perp}\subseteq\mathscr{X}^{*}$.
