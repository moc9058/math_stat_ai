# CHAPTER X

# Unbounded Operators

It is unfortunate for the world we live in that all of the operators that arise naturally are not bounded. But that is indeed the case. Thus it is important to study such operators.

The idea here is not to study an arbitrary linear transformation on a Hilbert space. In fact, such a study is the province of linear algebra rather than analysis. The operators that are to be studied do possess certain properties that connect them to the underlying Hilbert space. The properties that will be isolated are inspired by natural examples.

All Hilbert spaces in this chapter are assumed separable.

## §1. Basic Properties and Examples

The first relaxation in the concept of operator is not to assume that the operators are defined everywhere on the Hilbert space.

**1.1. Definition.** If $\mathcal H,\mathcal K$ are Hilbert spaces, a *linear operator* $A:\mathcal H\to\mathcal K$ is a function whose domain of definition is a linear manifold, $\operatorname{dom}A$, in $\mathcal H$ and such that $A(\alpha f+\beta g)=\alpha Af+\beta Ag$ for $f,g$ in $\operatorname{dom}A$ and $\alpha,\beta$ in $\mathbb C$. $A$ is *bounded* if there is a constant $c>0$ such that $\|Af\|\leq c\|f\|$ for all $f$ in $\operatorname{dom}A$.

Note that if $A$ is bounded, then $A$ can be extended to a bounded linear operator on $\operatorname{cl}[\operatorname{dom}A]$ and then extended to $\mathcal H$ by letting $A$ be $0$ on $(\operatorname{dom}A)^\perp$. So unless it is specified to the contrary, a bounded operator will always be assumed to be defined on all of $\mathcal H$.

If $A$ is a linear operator from $\mathcal H$ into $\mathcal K$, then $A$ is also a linear operator
