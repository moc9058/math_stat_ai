$a^*$ is left invertible. By the preceding argument $a^*$ is invertible, and hence so is $a$. ■

**1.4. Proposition.** *If $N$ is a normal operator, then $\sigma(N)=\sigma_r(N)=\sigma_l(N)$. If $\lambda$ is an isolated point of $\sigma(N)$, then $\lambda\in\sigma_p(N)$.*

**Proof.** The first part of the proposition is immediate from the preceding result. If $\lambda$ is an isolated point of $\sigma(N)$ and $N=\int z\,dE(z)$, then $0\neq E(\{\lambda\})\mathcal H=\ker(N-\lambda)$ (Exercise IX.2.1). ■

## Exercises

1. Let $S$ be the unilateral shift of multiplicity 1 on $l^2(\mathbb N)$ and find $\sigma_l(S)$ and $\sigma_r(S)$.

2. The *compression spectrum* of $A$, $\sigma_c(A)$, is defined by $\sigma_c(A)=\{\lambda\in\mathbb C:\operatorname{ran}(A-\lambda)\text{ is not dense in }\mathcal H\}$. Show: (a) $\lambda\in\sigma_c(A)$ if and only if $\bar\lambda\in\sigma_p(A^*)$. (b) $\sigma_c(A)\subseteq\sigma_r(A)$, but this inclusion may be proper. (c) $\sigma_c(A)$ is not necessarily closed. (d) $\sigma(A)=\sigma_{ap}(A)\cup\sigma_c(A)$.

3. If $A\in\mathcal B(\mathcal H)$ and $f\in\operatorname{Hol}(A)$, then $f(\sigma_p(A))\subseteq\sigma_p(f(A))$. If $f$ is not constant on any component of its domain, then $f(\sigma_p(A))=\sigma_p(f(A))$.

4. If $A\in\mathcal B(\mathcal H)$ and $f\in\operatorname{Hol}(A)$, then $f(\sigma_{ap}(A))=\sigma_{ap}(f(A))$.

## §2. Fredholm Operators

We begin with a definition.

**2.1. Definition.** If $\mathcal H$ and $\mathcal H'$ are Hilbert spaces and $A:\mathcal H\to\mathcal H'$ is a bounded operator, then $A$ is said to be *left semi-Fredholm* if there is a bounded operator $B:\mathcal H'\to\mathcal H$ and a compact operator $K$ on $\mathcal H$ such that $BA=1+K$. Analogously, $A$ is *right semi-Fredholm* if there is a such a bounded operator $B$ and a compact operator $K'$ on $\mathcal H'$ such that $AB=1+K'$. $A$ is a *semi-Fredholm operator* if it is either left or right semi-Fredholm and $A$ is a *Fredholm operator* if it is both left and right semi-Fredholm.

Observe that $A$ is left semi-Fredholm if and only if $A^*$ is right semi-Fredholm. Thus results about semi-Fredholm operators will usually only be phrased in terms of left semi-Fredholm operators and the reader will be allowed to make the appropriate statement for right semi-Fredholm operators.

Note that a left invertible operator is left semi-Fredholm. However it is easy to get left semi-Fredholm operators that are not left invertible.

**2.2. Example.** Let $\mathcal H=\mathcal H_0\oplus\mathcal H_1\oplus\cdots$, where $\dim\mathcal H_j=\alpha$ for all $j\geq 0$, and let $S$ be the unilateral shift of multiplicity $\alpha$ with respect to this decomposition. (So $S$ maps $\mathcal H_j$ isometrically onto $\mathcal H_{j+1}$.) Recall that $S^*S=1$ so $S$ is left
