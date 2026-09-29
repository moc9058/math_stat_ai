# CHAPTER IV

# Locally Convex Spaces

A topological vector space is a generalization of the concept of a Banach space. The locally convex spaces are encountered repeatedly when discussing weak topologies on a Banach space, sets of operators on Hilbert space, or the theory of distributions. This book will only skim the surface of this theory, but it will treat locally convex spaces in sufficient detail as to enable the reader to understand the use of these spaces in the three areas of analysis just mentioned. For more details on this theory, see Bourbaki [1967], Robertson and Robertson [1966], or Schaefer [1971].

## §1. Elementary Properties and Examples

A topological vector space is a vector space that is also a topological space such that the linear structure and the topological structure are vitally connected.

**1.1. Definition.** A *topological vector space* (TVS) is a vector space $\mathscr{X}$ together with a topology such that with respect to this topology

(a) the map of $\mathscr{X}\times\mathscr{X}\to\mathscr{X}$ defined by $(x,y)\mapsto x+y$ is continuous;  
(b) the map of $\mathbb{F}\times\mathscr{X}\to\mathscr{X}$ defined by $(\alpha,x)\mapsto\alpha x$ is continuous.

It is easy to see that a normed space is a TVS (Proposition III.1.3).

Suppose $\mathscr{X}$ is a vector space and $\mathscr{P}$ is a family of seminorms on $\mathscr{X}$. Let $\mathscr{T}$ be the topology on $\mathscr{X}$ that has as a subbase the sets $\{x:p(x-x_0)<\varepsilon\}$, where $p\in\mathscr{P}$, $x_0\in\mathscr{X}$, and $\varepsilon>0$. Thus a subset $U$ of $\mathscr{X}$ is open if and only if for every $x_0$ in $U$ there are $p_1,\ldots,p_n$ in $\mathscr{P}$ and $\varepsilon_1,\ldots,\varepsilon_n>0$ such that
