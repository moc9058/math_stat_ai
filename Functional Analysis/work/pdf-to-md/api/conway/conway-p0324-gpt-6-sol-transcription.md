sense of the concept of equality. This points out the distinction between symmetric and self-adjoint operators that it is necessary to make in the theory of unbounded operators.

**2.1. Definition.** An operator $A:\mathcal H\to\mathcal H$ is *symmetric* if $A$ is densely defined and $\langle Af,g\rangle=\langle f,Ag\rangle$ for all $f,g$ in $\operatorname{dom}A$.

The proof of the next proposition is left to the reader.

**2.2. Proposition.** If $A$ is densely defined, the following statements are equivalent.

(a) $A$ is symmetric.  
(b) $\langle Af,f\rangle\in\mathbb R$ for all $f$ in $\operatorname{dom}A$.  
(c) $A\subseteq A^*$.

If $A$ is symmetric, then the fact that $A\subseteq A^*$ implies $\operatorname{dom}A^*$ is dense. Hence $A$ is closable by Proposition 1.6. Symmetric operators can behave cantankerously. For example, there is an example of a closed symmetric operator $T$ such that $\operatorname{dom}(T^2)=(0)$. See Chernoff [1983].

It is easy to check that the operators in Examples 1.11 and 1.12 are symmetric.

**2.3. Definition.** A densely defined operator $A:\mathcal H\to\mathcal H$ is *self-adjoint* if $A=A^*$.

Let us emphasize that the condition that $A=A^*$ in the preceding definition carries with it the requirement that $\operatorname{dom}A=\operatorname{dom}A^*$. Now clearly every self-adjoint operator is symmetric, but the operator $A$ in Example 1.11 shows that there are symmetric operators that are not self-adjoint. If, however, an operator is bounded, then it is self-adjoint if and only if it is symmetric. The operator $B$ in Example 1.12 is an unbounded self-adjoint operator and Examples 1.9 and 1.10 can be used to furnish additional examples of unbounded self-adjoint operators.

Note that Proposition 1.6 implies that a self-adjoint operator is necessarily closed.

**2.4. Proposition.** Suppose $A$ is a symmetric operator on $\mathcal H$.

(a) If $\operatorname{ran}A$ is dense, then $A$ is injective.  
(b) If $A=A^*$ and $A$ is injective, then $\operatorname{ran}A$ is dense and $A^{-1}$ is self-adjoint.  
(c) If $\operatorname{dom}A=\mathcal H$, then $A=A^*$ and $A$ is bounded.  
(d) If $\operatorname{ran}A=\mathcal H$, then $A=A^*$ and $A^{-1}\in\mathcal B(\mathcal H)$.

**Proof.** The proof of (a) is trivial and (b) is an easy consequence of (1.13) and some manipulation.
