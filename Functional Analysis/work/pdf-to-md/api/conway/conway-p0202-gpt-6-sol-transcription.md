CHAPTER VII

# Banach Algebras and Spectral Theory for Operators on a Banach Space

The theory of Banach algebras is a large area in functional analysis with several subdivisions and applications to diverse areas of analysis and the rest of mathematics. Some monographs on this subject are by Bonsall and Duncan [1973] and C.E. Rickart [1960].

A significant change occurs in this chapter that will affect the remainder of this book. In order to prove that the spectrum of an element of a Banach algebra is nonvoid (Section 3), it is necessary to assume that the underlying field of scalars $\mathbb{F}$ is the field of complex numbers $\mathbb{C}$. It will be assumed from Section 3 until the end of this book that all vector spaces are over $\mathbb{C}$. This will also enable us to apply the theory of analytic functions to the study of Banach algebras and linear operators.

In this chapter only the rudiments of this subject are discussed. Enough, however, is presented to allow a treatment of the basics of spectral theory for operators on a Banach space.

## §1. Elementary Properties and Examples

An *algebra* over $\mathbb{F}$ is a vector space $\mathcal{A}$ over $\mathbb{F}$ that also has a multiplication defined on it that makes $\mathcal{A}$ into a ring such that if $\alpha\in\mathbb{F}$ and $a,b\in\mathcal{A}$, $\alpha(ab)=(\alpha a)b=a(\alpha b)$.

**1.1. Definition.** A *Banach algebra* is an algebra $\mathcal{A}$ over $\mathbb{F}$ that has a norm $\|\cdot\|$ relative to which $\mathcal{A}$ is a Banach space and such that for all $a,b$ in $\mathcal{A}$,

$$
\text{1.2}\qquad \|ab\|\leq\|a\|\|b\|.
$$
