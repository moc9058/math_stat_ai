# CHAPTER VI

# Linear Operators on a Banach Space

As has been said before in this book, the theory of bounded linear operators on a Banach space has seen relatively little activity owing to the difficult geometric problems inherent in the concept of a Banach space. In this chapter several of the general concepts of this theory are presented. When combined with the few results from the next chapter, they constitute essentially the whole of the general theory of these operators.

We begin with a study of the adjoint of a Banach space operator. Unlike the adjoint of an operator on a Hilbert space (Section II.2), the adjoint of a bounded linear operator on a Banach space does not operate on the space but on the dual space.

## §1. The Adjoint of a Linear Operator

Suppose $\mathcal{X}$ and $\mathcal{Y}$ are vector spaces and $T:\mathcal{X}\to\mathcal{Y}$ is a linear transformation. Let $\mathcal{Y}'=$ all of the linear functionals of $\mathcal{Y}\to\mathbb{F}$. If $y'\in\mathcal{Y}'$, then $y'\circ T:\mathcal{X}\to\mathbb{F}$ is easily seen to be a linear functional on $\mathcal{X}$. That is, $y'\circ T\in\mathcal{X}'$. This defines a map

$$
T':\mathcal{Y}'\to\mathcal{X}'
$$

by $T'(y')=y'\circ T$. The first result shows that if $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces, then the map $T'$ can be used to determine when $T$ is bounded. Another equivalent formulation of boundedness is given by means of the weak topology.

**1.1. Theorem.** *If $\mathcal{X}$ and $\mathcal{Y}$ are Banach spaces and $T:\mathcal{X}\to\mathcal{Y}$ is a linear transformation, then the following statements are equivalent.*
