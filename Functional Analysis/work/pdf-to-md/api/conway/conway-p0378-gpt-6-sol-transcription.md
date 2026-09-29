position $A=U|A|$ of $A$. Since $A\in\mathcal{SF}$ and $\ker A=(0)$, $|A|$ is invertible and $U$ is an isometry. Also, $\operatorname{ran}U=\operatorname{ran}A$, so (Exercise 4) there is a path $\rho:[0,1]\to\mathcal{B}(\mathcal{H})$ such that $\rho(t)$ is an isometry for every $t$ and $\rho(0)=U$ and $\rho(1)=V$. Let $\gamma:[0,1]\to\mathcal{F}$ be a path such that $\gamma(0)=|A|$ and $\gamma(1)=1$. Then $\sigma(t)=\rho(t)\gamma(t)$ for $0\leq t\leq 1$ defines a path $\sigma:[0,1]\to\mathcal{SF}$ (Why?) such that $\sigma(0)=A$ and $\sigma(1)=V$. Similarly, if $\operatorname{ind}B=-\infty$, there is a path connecting $B$ to $V$; so $A$ and $B$ belong to the same component of $\mathcal{SF}$.

If $\operatorname{ind}A=\operatorname{ind}B=+\infty$, apply the preceding paragraph to $A^*$ and $B^*$. ■

**5.3. Corollary.** *The component of the identity in $\mathcal{F}$, $\mathcal{F}_0$, is a normal sub-group of $\mathcal{F}$ and $\mathcal{F}/\mathcal{F}_0$ is an infinite cyclic group.*

**Proof.** By Theorem 3.7, $\operatorname{ind}:\mathcal{F}\to\mathbb{Z}$ is a group homomorphism and it is surjective (Exercise 3.4). By Theorem 5.1, $\ker(\operatorname{ind})=\mathcal{F}_0$. ■

**Exercises**

1. Let $G$ be any topological group and let $G_0$ be the component of the identity. Show that $G_0$ is a normal subgroup of $G$.

2. What are the components of the set of invertible elements in $C(\partial\mathbb{D})$?

3. If $S=$ the unilateral shift, what are the components of the set of invertible elements of $C^*(S)$?

4. If $U$ and $V$ are isometries, show that there is a path consisting entirely of isometries connecting $U$ to $V$ if and only if $\dim(\operatorname{ran}U)^\perp=\dim(\operatorname{ran}V)^\perp$.

5. Find the components of the set of partial isometries.

## §6. A Finer Analysis of the Spectrum

In this section we will examine the spectrum and index more closely. For example, one question that arises: If $A$ is semi-Fredholm and $\delta>0$ is chosen so that $B$ is semi-Fredholm and $\operatorname{ind}B=\operatorname{ind}A$ whenever $\|B-A\|<\delta$ (Corollary 3.13), how does $\dim\ker B$ differ from $\dim\ker A$?

Begin this investigation by associating with every bounded operator $A$ the following number:

$$
\gamma(A)=\inf\{\|Ah\|:\|h\|=1\text{ and }h\perp\ker A\}.
$$

The first proposition contains some elementary properties of $\gamma$ and its proof is left to the reader. (Actually part (a) has appeared several times in this book under different guises.)

**6.1. Proposition.** *Let $A$ be a bounded operator on $\mathcal{H}$.*

(a) $\gamma(A)>0$ if and only if $A$ has closed range.
