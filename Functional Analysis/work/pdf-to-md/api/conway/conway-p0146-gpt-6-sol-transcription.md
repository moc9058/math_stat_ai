onto $\tau(\operatorname{ball}\mathcal{X}^*)$ with the relative topology from $D$, and that $\tau(\operatorname{ball}\mathcal{X}^*)$ is closed in $D$. Thus it will follow that $\tau(\operatorname{ball}\mathcal{X}^*)$, and hence $\operatorname{ball}\mathcal{X}^*$, is compact.

To see that $\tau$ is injective, suppose that $\tau(x_1^*)=\tau(x_2^*)$. Then for each $x$ in $\operatorname{ball}\mathcal{X}$, $\langle x,x_1^*\rangle=\langle x,x_2^*\rangle$. It follows by definition that $x_1^*=x_2^*$.

Now let $\{x_i^*\}$ be a net in $\operatorname{ball}\mathcal{X}^*$ such that $x_i^*\to x^*$. Then for each $x$ in $\operatorname{ball}\mathcal{X}$, $\tau(x_i^*)(x)=\langle x,x_i^*\rangle\to\langle x,x^*\rangle=\tau(x^*)(x)$. That is, each coordinate of $\{\tau(x_i^*)\}$ converges to $\tau(x^*)$. Hence $\tau(x_i^*)\to\tau(x^*)$ and $\tau$ is continuous.

Let $x_i^*$ be a net in $\operatorname{ball}\mathcal{X}^*$, let $f\in D$, and suppose $\tau(x_i^*)\to f$ in $D$. So $f(x)=\lim\langle x,x_i^*\rangle$ exists for every $x$ in $\operatorname{ball}\mathcal{X}$. If $x\in\mathcal{X}$, let $\alpha>0$ such that $\|\alpha x\|\leq 1$. Then define $f(x)=\alpha^{-1}f(\alpha x)$. If also $\beta>0$ such that $\|\beta x\|\leq 1$, then $\alpha^{-1}f(\alpha x)=\alpha^{-1}\lim\langle\alpha x,x_i^*\rangle=\beta^{-1}\lim\langle\beta x,x_i^*\rangle=\beta^{-1}f(\beta x)$. So $f(x)$ is well defined. It is left as an exercise for the reader to show that $f:\mathcal{X}\to\mathbb{F}$ is a linear functional. Also, if $\|x\|\leq 1$, $f(x)\in D_x$ so $|f(x)|\leq 1$. Thus $x^*\in\operatorname{ball}\mathcal{X}^*$ and $\tau(x^*)=f$. Thus $\tau(\operatorname{ball}\mathcal{X}^*)$ is closed in $D$. This implies that $\tau(\operatorname{ball}\mathcal{X}^*)$ is compact. The proof that $\tau^{-1}$ is continuous is left to the reader. $\blacksquare$

## Exercises

1. Show that the functional $f$ occurring in the proof of Alaoglu’s Theorem is linear.

2. Let $\mathcal{X}$ be a LCS and let $V$ be an open neighborhood of $0$. Show that $V^\circ$ is weak-star compact in $\mathcal{X}^*$.

3. If $\mathcal{X}$ is a Banach space, show that there is a compact space $X$ such that $\mathcal{X}$ is isometrically isomorphic to a closed subspace of $C(X)$.

## §4. Reflexivity Revisited

In §III.11 a Banach space $\mathcal{X}$ was defined to be reflexive if the natural embedding of $\mathcal{X}$ into its double dual, $\mathcal{X}^{**}$, is surjective. Recall that if $x\in\mathcal{X}$, then the image of $x$ in $\mathcal{X}^{**}$, $\hat{x}$, is defined by (using our recent notation)

$$
\langle x^*,\hat{x}\rangle=\langle x,x^*\rangle
$$

for all $x^*$ in $\mathcal{X}^*$. Also recall that the map $x\mapsto\hat{x}$ is an isometry.

To begin, note that $\mathcal{X}^{**}$, being the dual space of $\mathcal{X}^*$, has its weak-star topology $\sigma(\mathcal{X}^{**},\mathcal{X}^*)$. Also note that if $\mathcal{X}$ is considered as a subspace of $\mathcal{X}^{**}$, then the topology $\sigma(\mathcal{X}^{**},\mathcal{X}^*)$ when relativized to $\mathcal{X}$ is $\sigma(\mathcal{X},\mathcal{X}^*)$, the weak topology on $\mathcal{X}$. This will be important later when it is combined with Alaoglu’s Theorem applied to $\mathcal{X}^{**}$ in the discussion of reflexivity. But now the next result must occupy us.

**4.1. Proposition.** *If $\mathcal{X}$ is a normed space, then $\operatorname{ball}\mathcal{X}$ is $\sigma(\mathcal{X}^{**},\mathcal{X}^*)$ dense in $\operatorname{ball}\mathcal{X}^{**}$.*

**Proof.** Let $B=$ the $\sigma(\mathcal{X}^{**},\mathcal{X}^*)$ closure of $\operatorname{ball}\mathcal{X}$ in $\mathcal{X}^{**}$; clearly, $B\subseteq\operatorname{ball}\mathcal{X}^{**}$. If there is an $x_0^{**}$ in $\operatorname{ball}\mathcal{X}^{**}\setminus B$, then the Hahn–Banach Theorem implies
