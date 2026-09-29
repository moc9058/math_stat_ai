# APPENDIX A

# Preliminaries

As was stated in the Preface, the prerequisites for understanding this book are a good course in measure and integration theory and, as a corequisite, analytic function theory. In this and the succeeding appendices an attempt is made to fill in some of the gaps and standardize some notation. These sections are not meant to be a substitute for serious study of these topics.

In Section 1 of this appendix some results from infinite dimensional linear algebra are set forth. Most of this is meant as review. Proposition 1.4, however, seems to be a fact that is not stressed or covered in courses but that is used often in functional analysis. Section 2 on topology is presented mainly to discuss nets. This topic is often not covered in the basic courses and it is especially useful in discussing various ideas and proving results in functional analysis.

## §1. Linear Algebra

Let $\mathcal{X}$ be a vector space over $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$. A subset $E$ of $\mathcal{X}$ is *linearly independent* if for any finite subset $\{e_1,\ldots,e_n\}$ of $E$ and for any finite set of scalars $\{\alpha_1,\ldots,\alpha_n\}$, if $\sum_{k=1}^{n}\alpha_k e_k=0$, then $\alpha_1=\cdots=\alpha_n=0$. A *Hamel basis* is a maximal linearly independent subset of $\mathcal{X}$.

**1.1. Proposition.** *If $E$ is a linearly independent subset of $\mathcal{X}$, then $E$ is a Hamel basis if and only if every vector $x$ in $\mathcal{X}$ can be written as $x=\sum_{k=1}^{n}\alpha_k e_k$ for scalars $\alpha_1,\ldots,\alpha_n$ and $\{e_1,\ldots,e_n\}\subseteq E$.*

**Proof.** Suppose $E$ is a basis and $x\in\mathcal{X}$, $x\notin E$. Then $E\cup\{x\}$ is not linearly independent. Thus there are $\alpha_0,\alpha_1,\ldots,\alpha_n$ in $\mathbb{F}$ and $e_1,\ldots,e_n$ in $E$ such that $0=\alpha_0x+\alpha_1e_1+\cdots+\alpha_ne_n$, with $\alpha_0\ne0$. (Why?) Thus $x=\sum_{k=1}^{n}(-\alpha_k/\alpha_0)e_k$.
