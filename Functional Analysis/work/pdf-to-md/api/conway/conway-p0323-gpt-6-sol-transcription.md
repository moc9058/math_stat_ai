Note that if $A$ is defined as in Example 1.9, then $\sigma(A)=\operatorname{cl}\{\alpha_n\}$. Hence it is possible for $\sigma(A)$ to equal any closed subset of $\mathbb C$.

**1.18. Proposition.** Let $A\in\mathcal C(\mathcal H)$.

(a) $\lambda\in\rho(A)$ if and only if $\ker(A-\lambda)=(0)$ and $\operatorname{ran}(A-\lambda)=\mathcal H$.

(b) $\sigma(A^*)=\{\bar\lambda:\lambda\in\sigma(A)\}$ and for $\lambda$ in $\rho(A)$, $(A-\lambda)^{*-1}=[(A-\lambda)^{-1}]^*$.

**Proof.** Exercise.

## Exercises

1. If $A$, $B$, and $AB$ are densely defined linear operators, show that $(AB)^*\supseteq B^*A^*$.

2. Verify the statements in Example 1.9.

3. Verify the statements in Example 1.10.

4. Define an unbounded weighted shift and determine its adjoint.

5. Verify the statements in Example 1.11.

6. If $\mathcal H$ is infinite dimensional, show that there is a linear operator $A:\mathcal H\to\mathcal H$ such that $\operatorname{gra}A$ is dense in $\mathcal H\oplus\mathcal H$. What does this say about $\operatorname{dom}A^*$? (See Lindsay [1984].)

7. Let $\mathcal D$ be the set of absolutely continuous functions $f$ such that $f'\in L^2(0,1)$. Let $Df=f'$ for $f$ in $\mathcal D$ and let $(Af)(x)=xf(x)$ for $f$ in $L^2(0,1)$. Show that $DA-AD\subseteq 1$.

8. If $\mathcal A$ is a Banach algebra with identity, show that there are no elements $a,b$ in $\mathcal A$ such that $ab-ba=1$. (Hint: compute $a^nb-ba^n$.)

9. Prove Proposition 1.18.

10. Define $A:L^2(\mathbb R)\to L^2(\mathbb R)$ by $(Af)(x)=\exp(-x^2)f(x-1)$ for all $f$ in $L^2(\mathbb R)$. (a) Show that $A\in\mathcal B(L^2(\mathbb R))$. (b) Find $\|A^n\|$ and show that $r(A)=0$ so that $\sigma(A)=\{0\}$. (c) Show that $A$ is injective. (d) Find $A^*$ and show that $\operatorname{ran}A$ is dense. (e) Define $B=A^{-1}$ with $\operatorname{dom}B=\operatorname{ran}A$ and show that $B\in\mathcal C(L^2(\mathbb R))$ with $\sigma(B)=\square$.

11. If $A\in\mathcal C(\mathcal H)$, show that $A^*A\in\mathcal C(\mathcal H)$. Show that $-1\notin\sigma(A^*A)$ and that if $B=(1+A^*A)^{-1}$, $\|B\|\leq 1$.

12. If $B$ is the bounded operator obtained in Exercise 11, show that $C=AB$ is also bounded and $\|C\|\leq 1$.

13. If $A$ is a self-adjoint operator, then $\lambda\in\rho(A)$ if and only if $A-\lambda$ is surjective.

## §2. Symmetric and Self-Adjoint Operators

An appropriate introduction to this section consists in a careful examination of Examples 1.11 and 1.12 in the preceding section. In (1.11) we saw that the operator $A$ seemed to be inclined to be self-adjoint, but $\operatorname{dom}A^*$ was different from $\operatorname{dom}A$ so we could not truly say that $A=A^*$. In (1.12), $B=B^*$ in any
