Also,

$$
\begin{aligned}
i(1+U)(1-U)^{-1}g
&=i(1+U)h\\
&=i[h+Uh]\\
&=i[(A+i)f+(A-i)f]\\
&=2iAf\\
&=Ag.
\end{aligned}
$$

Therefore (3.3) holds.

The proof of the remainder of (c) is left to the reader. $\blacksquare$

**3.4. Definition.** If $A$ is a densely defined closed symmetric operator, the partial isometry $U$ defined by (3.2) is called the *Cayley transform* of $A$.

**3.5. Corollary.** *If $A$ is a self-adjoint operator and $U$ is its Cayley transform, then $U$ is a unitary operator with $\ker(1-U)=(0)$. Conversely, if $U$ is a unitary with $1\notin\sigma_p(U)$, then the operator $A$ defined by (3.3) is self-adjoint.*

**Proof.** If $A$ is a densely defined symmetric operator, then $A$ is self-adjoint if and only if $\mathcal L_\pm=(0)$. A partial isometry is a unitary operator if and only if its initial and final spaces are all of $\mathcal H$. This corollary is now seen to follow from Theorem 3.1. $\blacksquare$

One use of the Cayley transform is to study self-adjoint operators by using the theory of unitary operators. Indeed, the preceding results say that there is a bijective correspondence between self-adjoint operators and the set of unitary operators without 1 as an eigenvalue.

## Exercises

1. If $U$ is a partial isometry, show that the following statements are equivalent: (a) $\ker(1-U)=(0)$; (b) $\ker(1-U^*)=(0)$; (c) $\operatorname{ran}(1-U)$ is dense; (d) $\operatorname{ran}(1-U^*)$ is dense.

2. Let $U$ be a partial isometry with initial and final spaces $\mathcal M$ and $\mathcal N$, respectively. Show that the following statements are equivalent: (a) $(1-U)\mathcal M$ is dense; (b) $(1-U^*)\mathcal N$ is dense; (c) $\ker(U^*-U^*U)=(0)$; (d) $\ker(U-UU^*)=(0)$.

3. Find a partial isometry $U$ such that $\ker(1-U)=(0)$ but $(1-U)(\ker U)^\perp$ is not dense.

4. If $A$ is a densely defined closed symmetric operator and $B$ and $C$ are the operators defined in Exercises 1.11 and 1.12, then the Cayley transform of $A$ is an extension of $(C-iB)(C+iB)^{-1}$.

5. Find the Cayley transform of the operator in Example 1.9 when each $\alpha_n$ is real.

6. Find the Cayley transform of the operator in Example 1.10 when $\phi$ is real valued.

7. Let $S$ be the unilateral shift of multiplicity 1 (see Exercise IX.6.4) and find the symmetric operator $A$ such that $S$ is the Cayley transform of $A$.
