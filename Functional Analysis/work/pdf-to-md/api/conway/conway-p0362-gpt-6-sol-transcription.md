# CHAPTER XI

# Fredholm Theory

This chapter is entirely independent of the preceding one and only tangentially dependent on Chapters VIII and IX.

The purpose of this chapter is to study certain properties of operators on a Hilbert space that are invariant under compact perturbations. That is, we want to study properties of an operator $A$ in $\mathcal{B}(\mathcal{H})$ that are also possessed by $A+K$ for every $K$ in $\mathcal{B}_0(\mathcal{H})$. The correct view here is to consider this undertaking as a study of the quotient algebra $\mathcal{B}(\mathcal{H})/\mathcal{B}_0(\mathcal{H})=\mathcal{B}/\mathcal{B}_0$—the *Calkin algebra*. Any property associated with an element of the Calkin algebra is a property associated with a coset of operators and vice versa. It is useful—indeed essential—to relate these properties to the way in which the operators act on the underlying Hilbert space.

## §1. The Spectrum Revisited

In Section VII.6 we saw several properties of the spectrum of an operator on a Banach space. In particular, the concepts of point spectrum, $\sigma_p(A)$, and approximate point spectrum, $\sigma_{ap}(A)$, were explored. It was also shown (VII. 6.7) that $\partial\sigma(A)\subseteq\sigma_{ap}(A)$. Recall that $\sigma_l(A)$ is the left spectrum of $A$ and $\sigma_r(A)$ is the right spectrum of $A$.

**1.1. Proposition.** *If $A\in\mathcal{B}(\mathcal{H})$, the following statements are equivalent.*

(a) $\lambda\notin\sigma_{ap}(A)$; that is, $\inf\{\|(A-\lambda)h\|:\|h\|=1\}>0$.

(b) $\operatorname{ran}(A-\lambda)$ is closed and $\dim\ker(A-\lambda)=0$.

(c) $\lambda\notin\sigma_l(A)$.
