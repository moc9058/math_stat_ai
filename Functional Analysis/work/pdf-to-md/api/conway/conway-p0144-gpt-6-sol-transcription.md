**2.2. Theorem.** *If $\mathcal X$ is a LCS, $\mathcal M\leq\mathcal X$, and $Q:\mathcal X\to\mathcal X/\mathcal M$ is the natural map, then $f\mapsto f\circ Q$ defines a linear bijection between $(\mathcal X/\mathcal M)^*$ and $\mathcal M^\perp$. If $(\mathcal X/\mathcal M)^*$ has its weak-star topology $\sigma((\mathcal X/\mathcal M)^*,\mathcal X/\mathcal M)$ and $\mathcal M^\perp$ has the relative weak-star topology $\sigma(\mathcal X^*,\mathcal X)|\mathcal M^\perp$, then this bijection is a homeomorphism. If $\mathcal X$ is a normed space, then this bijection is an isometry.*

**Proof.** Let $\rho:(\mathcal X/\mathcal M)^*\to\mathcal M^\perp$ be defined by $\rho(f)=f\circ Q$. It was shown prior to the statement of the theorem that $\rho$ is well defined and maps $(\mathcal X/\mathcal M)^*$ into $\mathcal M^\perp$. It is easy to see that $\rho$ is linear and if $0=\rho(f)=f\circ Q$, then $f=0$ since $Q$ is surjective. So $\rho$ is injective. Now let $x^*\in\mathcal M^\perp$ and define $f:\mathcal X/\mathcal M\to\mathbb F$ by $f(x+\mathcal M)=\langle x,x^*\rangle$. Because $\mathcal M\subseteq\ker x^*$, $f$ is well defined and linear. Also, $Q^{-1}\{x+\mathcal M:|f(x+\mathcal M)|<1\}=\{x\in\mathcal X:|\langle x,x^*\rangle|<1\}$ and this is open in $\mathcal X$ since $x^*$ is continuous. Thus $\{x+\mathcal M:|f(x+\mathcal M)|<1\}$ is open in $\mathcal X/\mathcal M$ and so $f$ is continuous. Clearly $\rho(f)=x^*$, so $\rho$ is a bijection.

If $\mathcal X$ is a normed space, it was shown in (III.10.2) that $\rho$ is an isometry. It remains to show that $\rho$ is a weak-star homeomorphism. Let $\mathrm{wk}^*=\sigma(\mathcal X^*,\mathcal X)$ and let $\sigma^*=\sigma((\mathcal X/\mathcal M)^*,\mathcal X/\mathcal M)$. If $\{f_i\}$ is a net in $(\mathcal X/\mathcal M)^*$ and $f_i\to0(\sigma^*)$, then for each $x$ in $\mathcal X$, $\langle x,\rho(f_i)\rangle=f_i(Q(x))\to0$. Hence $\rho(f_i)\to0(\mathrm{wk}^*)$. Conversely, if $\rho(f_i)\to0(\mathrm{wk}^*)$, then for each $x$ in $\mathcal X$, $f_i(x+\mathcal M)=\langle x,\rho(f_i)\rangle\to0$; hence $f_i\to0(\sigma^*)$. ■

Once again let $\mathcal M\leq\mathcal X$. If $x^*\in\mathcal X^*$, then the restriction of $\mathcal X^*$ to $\mathcal M$, $x^*|\mathcal M$, belongs to $\mathcal M^*$. Also, the Hahn–Banach Theorem implies that the map $x^*\mapsto x^*|\mathcal M$ is surjective. If $\rho(x^*)=x^*|\mathcal M$, then $\rho:\mathcal X^*\to\mathcal M^*$ is clearly linear as well as surjective. It fails, however, to be injective. How does it fail? It’s easy to see that $\ker\rho=\mathcal M^\perp$. Thus $\rho$ induces a linear bijection $\tilde\rho:\mathcal X^*/\mathcal M^\perp\to\mathcal M^*$.

**2.3. Theorem.** *If $\mathcal X$ is a LCS, $\mathcal M\leq\mathcal X$, and $\rho:\mathcal X^*\to\mathcal M^*$ is the restriction map, then $\rho$ induces a linear bijection $\tilde\rho:\mathcal X^*/\mathcal M^\perp\to\mathcal M^*$. If $\mathcal X^*/\mathcal M^\perp$ has the quotient topology induced by $\sigma(\mathcal X^*,\mathcal X)$ and $\mathcal M^*$ has its weak-star topology $\sigma(\mathcal M^*,\mathcal M)$, then $\tilde\rho$ is a homeomorphism. If $\mathcal X$ is a normed space, then $\tilde\rho$ is an isometry.*

**Proof.** The fact that $\tilde\rho$ is an isometry when $\mathcal X$ is a normed space was shown in (III.10.1). Let $\mathrm{wk}^*=\sigma(\mathcal M^*,\mathcal M)$ and let $\eta^*$ be the quotient topology on $\mathcal X^*/\mathcal M^\perp$ defined by $\sigma(\mathcal X^*,\mathcal X)$. Let $Q:\mathcal X^*\to\mathcal X^*/\mathcal M^\perp$ be the natural map. Therefore the diagram

[FIGURE: Commutative triangular diagram. $\mathcal X^*$ is at the upper left, $\mathcal M^*$ at the upper right, and $\mathcal X^*/\mathcal M^\perp$ below; arrows are $\rho$ from $\mathcal X^*$ to $\mathcal M^*$, $Q$ from $\mathcal X^*$ to $\mathcal X^*/\mathcal M^\perp$, and $\tilde\rho$ from $\mathcal X^*/\mathcal M^\perp$ to $\mathcal M^*$.]

commutes. If $y\in\mathcal M$, then the commutativity of the diagram implies that

$$
\begin{aligned}
Q^{-1}\bigl(\tilde\rho^{-1}\{y^*\in\mathcal M^*:|\langle y,y^*\rangle|<1\}\bigr)
&=Q^{-1}\{x^*+\mathcal M^\perp:|\langle y,x^*\rangle|<1\}\\
&=\{x^*\in\mathcal X^*:|\langle y,x^*\rangle|<1\},
\end{aligned}
$$
