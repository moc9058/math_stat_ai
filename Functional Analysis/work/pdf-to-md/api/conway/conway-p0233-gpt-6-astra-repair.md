218  VII. Banach Algebras and Spectral Theory

5. Suppose $A\in\mathcal{B}(\mathcal{X})$ and there is an entire function $f$ such that $f(A)\in\mathcal{B}_0(\mathcal{X})$. What can be said about $\sigma(A)$?

6. With the terminology of Exercise 6.13, if $A\in\mathcal{B}_0(\mathcal{X})$, $\lambda\in\sigma(A)$, and $\lambda\ne0$, what can be said about the index of $\lambda$?

## §8. Abelian Banach Algebras

Recall that it is assumed that every Banach algebra is over $\mathbb{C}$. Also assume that all Banach algebras contain an identity.

A *division algebra* is an algebra such that every nonzero element has a multiplicative inverse. It may seem incongruous that the first theorem in this section allows the algebra to be nonabelian. However, the conclusion is that the algebra is abelian—and much more.

**8.1. The Gelfand–Mazur Theorem.** *If $\mathcal{A}$ is a Banach algebra that is also a division ring, then $\mathcal{A}=\mathbb{C}\;(=\{\lambda1:\lambda\in\mathbb{C}\})$.*

**Proof.** If $a\in\mathcal{A}$, then $\sigma(a)\ne\square$. If $\lambda\in\sigma(a)$, then $a-\lambda$ has no inverse. But $\mathcal{A}$ is a division ring, so $a-\lambda=0$. That is, $a=\lambda$. ■

As a corollary of the preceding theorem, the algebra of quaternions, $\mathbb{H}$, is not a Banach algebra. That is, it is impossible to put a norm on $\mathbb{H}$ that makes it into a Banach algebra over $\mathbb{C}$. Can you show this directly?

**8.2. Proposition.** *If $\mathcal{A}$ is an abelian Banach algebra and $\mathcal{M}$ is a maximal ideal, then there is a homomorphism $h:\mathcal{A}\to\mathbb{C}$ such that $\mathcal{M}=\ker h$. Conversely, if $h:\mathcal{A}\to\mathbb{C}$ is a nonzero homomorphism, then $\ker h$ is a maximal ideal. Moreover, this correspondence $h\mapsto\ker h$ between homomorphisms and maximal ideals is bijective.*

**Proof.** If $\mathcal{M}$ is a maximal ideal, then $\mathcal{M}$ is closed (2.4b). Hence $\mathcal{A}/\mathcal{M}$ is a Banach algebra with identity. Let $\pi:\mathcal{A}\to\mathcal{A}/\mathcal{M}$ be the natural map. If $a\in\mathcal{A}$ and $\pi(a)$ is not invertible in $\mathcal{A}/\mathcal{M}$, then $\pi(\mathcal{A}a)=\pi(a)[\mathcal{A}/\mathcal{M}]$ is an ideal in $\mathcal{A}/\mathcal{M}$ that is proper. Let $I=\{b\in\mathcal{A}:\pi(b)\in\pi(\mathcal{A}a)\}=\pi^{-1}(\pi(\mathcal{A}a))$. Then $I$ is a proper ideal of $\mathcal{A}$ and $\mathcal{M}\subseteq I$. Since $\mathcal{M}$ is maximal, $\mathcal{M}=I$. Thus $\pi(a\mathcal{A})\subseteq\pi(I)=\pi(\mathcal{M})=(0)$. That is, $\pi(a)=0$. This says that $\mathcal{A}/\mathcal{M}$ is a field. By the Gelfand–Mazur Theorem $\mathcal{A}/\mathcal{M}=\mathbb{C}=\{\lambda+\mathcal{M}:\lambda\in\mathbb{C}\}$. Define $\tilde h:\mathcal{A}/\mathcal{M}\to\mathbb{C}$ by $\tilde h(\lambda+\mathcal{M})=\lambda$ and define $h:\mathcal{A}\to\mathbb{C}$ by $h=\tilde h\circ\pi$. Then $h$ is a homomorphism and $\ker h=\mathcal{M}$.

Conversely, suppose $h:\mathcal{A}\to\mathbb{C}$ is a nonzero homomorphism. Then $\ker h=\mathcal{M}$ is a nontrivial ideal and $\mathcal{A}/\mathcal{M}\approx\mathbb{C}$. (Why?) So $\mathcal{M}$ is maximal.

If $h,h'$ are two nonzero homomorphisms and $\ker h=\ker h'$, then there is an $\alpha$ in $\mathbb{C}$ such that $h=\alpha h'$ (A.1.4). But $1=h(1)=\alpha h'(1)=\alpha$, so $h=h'$. ■
