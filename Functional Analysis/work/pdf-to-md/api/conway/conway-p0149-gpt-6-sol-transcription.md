then $\ker L$ is not proximinal.

There is a result in James [1964b] that states that a Banach space is reflexive if and only if every closed hyperplane is proximinal. This result is very deep. A nice reference on reflexivity is Yang [1967].

## Exercises

1. Show that if $\mathcal X$ is reflexive and $\mathcal M\leqslant\mathcal X$, then $\mathcal X/\mathcal M$ is reflexive.

2. If $\mathcal X$ is a Banach space, $\mathcal M\leqslant\mathcal X$, and both $\mathcal M$ and $\mathcal X/\mathcal M$ are reflexive, must $\mathcal X$ be reflexive?

3. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, show that $L^1(X,\Omega,\mu)$ is reflexive if and only if it is finite dimensional.

4. Give the details of the proofs of the statements made in Example 4.5.

5. Verify the statement made in Example 4.8.

6. If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space, show that $L^\infty(\mu)$ is weak-star sequentially complete but is reflexive if and only if it is finite dimensional.

7. Let $X$ be compact and suppose there is a norm on $C(X)$ that is given by an inner product making $C(X)$ into a Hilbert space such that for every $x$ in $X$ the functional $f\mapsto f(x)$ on $C(X)$ is continuous with respect to the Hilbert space norm. Show that $X$ is finite.

## §5. Separability and Metrizability

The weak and weak-star topologies on an infinite dimensional Banach space are never metrizable. It is possible, however, to show that under certain conditions these topologies are metrizable when restricted to bounded sets. In applications this is often sufficient.

**5.1. Theorem.** *If $\mathcal X$ is a Banach space, then $\operatorname{ball}\mathcal X^*$ is weak-star metrizable if and only if $\mathcal X$ is separable.*

**Proof.** Assume that $\mathcal X$ is separable and let $\{x_n\}$ be a countable dense subset of $\operatorname{ball}\mathcal X$. For each $n$ let $D_n=\{\alpha\in\mathbb F:|\alpha|\leqslant1\}$. Put $X=\prod_{n=1}^{\infty}D_n$; $X$ is a compact metric space. So if $(\operatorname{ball}\mathcal X^*,\mathrm{wk}^*)$ is homeomorphic to a subset of $X$, $\operatorname{ball}\mathcal X^*$ is weak-star metrizable.

Define $\tau:\operatorname{ball}\mathcal X^*\to X$ by $\tau(x^*)=\{\langle x_n,x^*\rangle\}$. If $\{x_i^*\}$ is a net in $\operatorname{ball}\mathcal X^*$ and $x_i^*\to x^*\ (\mathrm{wk}^*)$, then for each $n\geqslant1$, $\langle x_n,x_i^*\rangle\to\langle x_n,x^*\rangle$; hence $\tau(x_i^*)\to\tau(x^*)$ and $\tau$ is continuous. If $\tau(x^*)=\tau(y^*)$, $\langle x_n,x^*-y^*\rangle=0$ for all $n$. Since $\{x_n\}$ is dense, $x^*-y^*=0$. Thus $\tau$ is injective. Since $\operatorname{ball}\mathcal X^*$ is $\mathrm{wk}^*$ compact, $\tau$ is a homeomorphism onto its image (A.2.8) and $\operatorname{ball}\mathcal X^*$ is $\mathrm{wk}^*$ metrizable.

Now assume that $(\operatorname{ball}\mathcal X^*,\mathrm{wk}^*)$ is metrizable. Thus there are open sets $\{U_n:n\geqslant1\}$ in $(\operatorname{ball}\mathcal X^*,\mathrm{wk}^*)$ such that $0\in U_n$ and $\bigcap_{n=1}^{\infty}U_n=(0)$. By the
