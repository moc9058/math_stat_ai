ProoF. By the mean value property, if $0 < t \leqslant r,f(a) = (1/2\pi)\int_{-\pi}^{\pi} f(a + te^{i\theta})d\theta.$ Hence

$$
\begin{align*}\left( \pi r^{2} \right)^{-1} \int_{B(a;r)}^{r} f = & \left( \pi r^{2} \right)^{-1} \int_{0}^{r} t \left[ \int_{-\pi}^{\pi} f(a + t e^{i \theta}) d \theta \right] dt \\= & \left( 2 / r^{2} \right) \int_{0}^{r} t f(a) dt = f(a).\end{align*}
$$

1.12. Corollary. $If f \in L_{a}^{2}(G), a \in G$ , and $0 < r < \mathrm{dist}(a, \partial G)$ then

$$
| f ( a ) | \leqslant \frac { 1 } { r \sqrt { \pi } } \| f \| _ { 2 } .
$$

PROOF. Since $\bar { B } ( a ; r ) \subseteq G ,$ , the preceding lemma and the CBS inequality imply

$$
\begin{align*}|f(a)| = & \frac{1}{\pi r^2} \left| \int_{B(a;r)} f \cdot 1 \right| \\\leqslant & \frac{1}{\pi r^2} \left[ \int_{B(a;r)} |f|^2 \right]^{1/2} \left[ \int_{B(a;r)} 1^2 \right]^{1/2} \\\leqslant & \frac{1}{\pi r^2} \parallel f \parallel_2 r \sqrt{\pi}.\end{align*}
$$

1.13. Proposition. $L _ { a } ^ { 2 } ( G )$ is a Hilbert space.

PROOF. If $\mu =$ area measure on $G ,$ then $L ^ { 2 } ( \mu )$ is a Hilbert space and $L _ { a } ^ { 2 } ( G ) \subseteq L ^ { 2 } ( \mu )$ . So it suffices to show that $L _ { a } ^ { 2 } ( G )$ is closed in $L ^ { 2 } ( \mu )$ Let $\{ f _ { n } \}$ be a sequence in $L _ { a } ^ { 2 } ( G )$ and let $f   \in   L ^ { 2 } ( \mu )$ such that $\int | f _ { n } - f | ^ { 2 }   d \mu \to 0$ as $n   \to   \infty$

Suppose $\tilde { B } ( a ; r ) \subseteq G$ and let $0 < \rho < \mathrm { d i s t } ( B ( a ; r ) , \partial G )$ . By the preceding corollary there is a constant C such that $| f _ { n } ( z ) - f _ { m } ( z ) | \leqslant C \| f _ { n } - f _ { m } \| _ { 2 }$ for all $n ,$ m and for $| z - a | \leqslant \rho .$ Thus $\{ f _ { n } \}$ is a uniformly Cauchy sequence on any closed disk in G. By standard results from analytic function theory (Montel's Theorem or Morera's Theorem, for example), there is an analytic function g on G such that $f _ { n } ( z ) \to g ( z )$ uniformly on compact subsets of G. But since $\int | f _ { n } - f | ^ { 2 }   d \mu \to 0 ,$ a result of Riesz implies there is a subsequence $\{ f _ { n _ { k } } \}$ such that $f _ { n _ { k } } ( z ) \to f ( z ) \mathrm { ~ a . e . ~ } [ \mu ]$ . Thus $f = g \mathrm { a . e . } [ \mu ]$ and so $f   \in   \bar { L _ { a } ^ { 2 } ( G ) }$

## EXERCISES

1. Verify the statements made in Example 1.2.

2. Verify that $l ^ { 2 } ( I )$ (Example 1.7) is a Hilbert space.

3. Show that the space $\mathcal { H }$ in Example 1.8 is a Hilbert space.

4. Describe the Hilbert spaces obtained by completing the space $\mathcal { X }$ in Example 1.2 with respect to the norm defined by each of the inner products given there.