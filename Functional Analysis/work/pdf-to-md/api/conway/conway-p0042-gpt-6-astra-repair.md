§1. Elementary Properties and Examples  27

(c) *$A$ is continuous at some point.*

(d) *There is a constant $c>0$ such that $\|Ah\|\leq c\|h\|$ for all $h$ in $\mathcal H$.*

As in (I.3.3), if

$$
\|A\|=\sup\{\|Ah\|:h\in\mathcal H,\ \|h\|\leq 1\},
$$

then

$$
\begin{aligned}
\|A\|
&=\sup\{\|Ah\|:\|h\|=1\}\\
&=\sup\{\|Ah\|/\|h\|:h\ne 0\}\\
&=\inf\{c>0:\|Ah\|\leq c\|h\|,\ h\text{ in }\mathcal H\}.
\end{aligned}
$$

Also, $\|Ah\|\leq\|A\|\|h\|$. $\|A\|$ is called the *norm* of $A$ and a linear transformation with finite norm is called *bounded*. Let $\mathcal B(\mathcal H,\mathcal K)$ be the set of bounded linear transformations from $\mathcal H$ into $\mathcal K$. For $\mathcal H=\mathcal K$, $\mathcal B(\mathcal H,\mathcal H)\equiv\mathcal B(\mathcal H)$. Note that $\mathcal B(\mathcal H,\mathbb F)=$ all the bounded linear functionals on $\mathcal H$.

**1.2. Proposition.** (a) *If $A$ and $B\in\mathcal B(\mathcal H,\mathcal K)$, then $A+B\in\mathcal B(\mathcal H,\mathcal K)$, and $\|A+B\|\leq\|A\|+\|B\|$.*

(b) *If $\alpha\in\mathbb F$ and $A\in\mathcal B(\mathcal H,\mathcal K)$, then $\alpha A\in\mathcal B(\mathcal H,\mathcal K)$ and $\|\alpha A\|=|\alpha|\|A\|$.*

(c) *If $A\in\mathcal B(\mathcal H,\mathcal K)$ and $B\in\mathcal B(\mathcal K,\mathcal L)$, then $BA\in\mathcal B(\mathcal H,\mathcal L)$ and $\|BA\|\leq\|B\|\|A\|$.*

PROOF. Only (c) will be proved; the rest of the proof is left to the reader. If $k\in\mathcal K$, then $\|Bk\|\leq\|B\|\|k\|$. Hence, if $h\in\mathcal H$, $k=Ah\in\mathcal K$ and so $\|BAh\|\leq\|B\|\|Ah\|\leq\|B\|\|A\|\|h\|$. $\blacksquare$

By virtue of preceding proposition, $d(A,B)=\|A-B\|$ defines a metric on $\mathcal B(\mathcal H,\mathcal K)$. So it makes sense to consider $\mathcal B(\mathcal H,\mathcal K)$ as a metric space. This will not be examined closely until later in the book, but later in this chapter the idea of the convergence of a sequence of operators will be used.

**1.3. Example.** If $\dim\mathcal H=n<\infty$ and $\dim\mathcal K=m<\infty$, let $\{e_1,\ldots,e_n\}$ be an orthonormal basis for $\mathcal H$ and let $\{\varepsilon_1,\ldots,\varepsilon_m\}$ be an orthonormal basis for $\mathcal K$. It can be shown that every linear transformation from $\mathcal H$ into $\mathcal K$ is bounded (Exercise 3). If $1\leq j\leq n$, $1\leq i\leq m$, let $a_{ij}=\langle Ae_j,\varepsilon_i\rangle$. Then the $m\times n$ matrix $(\alpha_{ij})$ represents $A$ and every such matrix represents an element of $\mathcal B(\mathcal H,\mathcal K)$.

**1.4. Example.** Let $l^2=l^2(\mathbb N)$ and let $e_1,e_2,\ldots$ be its usual basis. If $A\in\mathcal B(l^2)$, form $\alpha_{ij}=\langle Ae_j,e_i\rangle$. The infinite matrix $(\alpha_{ij})$ represents $A$ as finite matrices represent operators on finite dimensional spaces. However, this representation has limited value unless the matrix has a special form. One difficulty is that it is unknown how to find the norm of $A$ in terms of the entries in the matrix. In fact, if $4<n<\infty$, there is no known formula for the norm of an $n\times n$ matrix in terms of its entries. (This restriction on the values of $n$ is due to our inability to solve polynomial equations of degree greater than 4.) See
