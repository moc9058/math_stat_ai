CHAPTER I

# Hilbert Spaces

A Hilbert space is the abstraction of the finite-dimensional Euclidean spaces of geometry. Its properties are very regular and contain few surprises, though the presence of an infinity of dimensions guarantees a certain amount of surprise. Historically, it was the properties of Hilbert spaces that guided mathematicians when they began to generalize. Some of the properties and results seen in this chapter and the next will be encountered in more general settings later in this book, or we shall see results that come close to these but fail to achieve the full power possible in the setting of Hilbert space.

## §1. Elementary Properties and Examples

Throughout this book $\mathbb{F}$ will denote either the real field, $\mathbb{R}$, or the complex field, $\mathbb{C}$.

**1.1. Definition.** If $\mathscr{X}$ is a vector space over $\mathbb{F}$, a *semi-inner product* on $\mathscr{X}$ is a function $u:\mathscr{X}\times\mathscr{X}\to\mathbb{F}$ such that for all $\alpha,\beta$ in $\mathbb{F}$, and $x,y,z$ in $\mathscr{X}$, the following are satisfied:

(a) $u(\alpha x+\beta y,z)=\alpha u(x,z)+\beta u(y,z),$

(b) $u(x,\alpha y+\beta z)=\bar{\alpha}u(x,y)+\bar{\beta}u(x,z),$

(c) $u(x,x)\geqslant 0,$

(d) $u(x,y)=\overline{u(y,x)}.$

Here, for $\alpha$ in $\mathbb{F}$, $\bar{\alpha}=\alpha$ if $\mathbb{F}=\mathbb{R}$ and $\bar{\alpha}$ is the complex conjugate of $\alpha$ if $\mathbb{F}=\mathbb{C}$. If $\alpha\in\mathbb{C}$, the statement that $\alpha\geqslant 0$ means that $\alpha\in\mathbb{R}$ and $\alpha$ is non-negative.

Note that if $\alpha=0$, then property (a) implies that $u(0,y)=u(\alpha\cdot 0,y)=$
