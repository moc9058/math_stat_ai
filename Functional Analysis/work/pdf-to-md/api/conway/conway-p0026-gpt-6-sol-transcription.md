The proof is left to the reader; see Exercise 4 for a discussion of the term “closed linear span.”

**2.11. Corollary.** *If $\mathcal Y$ is a linear manifold in $\mathcal H$, then $\mathcal Y$ is dense in $\mathcal H$ iff $\mathcal Y^\perp=(0)$.*

**Proof.** Exercise.

## Exercises

1. Let $\mathcal H$ be a Hilbert space and suppose $f$ and $g$ are linearly independent vectors in $\mathcal H$ with $\|f\|=\|g\|=1$. Show that $\|tf+(1-t)g\|<1$ for $0<t<1$. What does this say about $\{h\in\mathcal H:\|h\|\leq 1\}$?

2. If $\mathcal M\leq\mathcal H$ and $P=P_{\mathcal M}$, show that $I-P$ is the orthogonal projection of $\mathcal H$ onto $\mathcal M^\perp$.

3. If $\mathcal M\leq\mathcal H$, show that $\mathcal M\cap\mathcal M^\perp=(0)$ and every $h$ in $\mathcal H$ can be written as $h=f+g$ where $f\in\mathcal M$ and $g\in\mathcal M^\perp$. If $\mathcal M+\mathcal M^\perp\equiv\{(f,g):f\in\mathcal M,\ g\in\mathcal M^\perp\}$ and $T:\mathcal M+\mathcal M^\perp\to\mathcal H$ is defined by $T(f,g)=f+g$, show that $T$ is a linear bijection and a homeomorphism if $\mathcal M+\mathcal M^\perp$ is given the product topology. (This is usually phrased by stating the $\mathcal M$ and $\mathcal M^\perp$ are *topologically complementary* in $\mathcal H$.)

4. If $A\subseteq\mathcal H$, let $\vee A\equiv$ the intersection of all closed linear subspaces of $\mathcal H$ that contain $A$. $\vee A$ is called the *closed linear span* of $A$. Prove the following:

   (a) $\vee A\leq\mathcal H$ and $\vee A$ is the smallest closed linear subspace of $\mathcal H$ that contains $A$.

   (b) $\vee A=$ the closure of $\left\{\sum_{k=1}^{n}\alpha_k f_k:n\geq 1,\ \alpha_k\in\mathbb F,\ f_k\in A\right\}$.

5. Prove Corollary 2.10.

6. Prove Corollary 2.11.

## §3. The Riesz Representation Theorem

The title of this section is somewhat ambiguous as there are at least two Riesz Representation Theorems. There is one so-called theorem that represents bounded linear functionals on the space of continuous functions on a compact Hausdorff space. That theorem will be discussed later in this book. The present section deals with the representation of certain linear functionals on Hilbert space. But first we have a few preliminaries to dispose of.

**3.1. Proposition.** *Let $\mathcal H$ be a Hilbert space and $L:\mathcal H\to\mathbb F$ a linear functional. The following statements are equivalent.*

(a) $L$ is continuous.

(b) $L$ is continuous at $0$.

(c) $L$ is continuous at some point.

(d) There is a constant $c>0$ such that $|L(h)|\leq c\|h\|$ for every $h$ in $\mathcal H$.

**Proof.** It is clear that $(a)\Rightarrow(b)\Rightarrow(c)$ and $(d)\Rightarrow(b)$. Let’s show that $(c)\Rightarrow(a)$ and $(b)\Rightarrow(d)$.
