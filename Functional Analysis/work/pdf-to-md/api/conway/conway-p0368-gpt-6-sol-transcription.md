If $A$ is a semi-Fredholm operator, define the (*Fredholm*) index of $A$, $\operatorname{ind}A$, by

$$
\begin{aligned}
\operatorname{ind}A
&=\dim\ker A-\dim(\operatorname{ran}A)^\perp\\
&=\dim\ker A-\dim\ker A^*.
\end{aligned}
\tag{3.1}
$$

Note that $\operatorname{ind}A\in\mathbb Z\cup\{\pm\infty\}$ and it is necessary for either $\ker A$ or $\ker A^*$ to be finite dimensional in order for (3.1) to make sense. For $\operatorname{ind}A$ to be well defined, it is not necessary that $\operatorname{ran}A$ be closed (the other part of the definition of semi-Fredholm operators), but this property will be used in a critical way when the properties of the index are established.

See Dieudonné [1985] for some historical notes on the Fredholm index.

The main properties of the Fredholm index are contained in Theorems 3.7, 3.11, and 3.12 below. But we will begin with some elementary results.

**3.2. Proposition.** *If $A:\mathcal H\to\mathcal H'$ and $\mathcal H$ and $\mathcal H'$ are finite dimensional, then $A$ is Fredholm and $\operatorname{ind}A=\dim\mathcal H-\dim\mathcal H'$.*

**Proof.** Clearly $A$ is Fredholm. From linear algebra we know that $\dim\mathcal H=\dim(\operatorname{ran}A)+\dim(\ker A)=[\dim\mathcal H'-\dim(\operatorname{ran}A)^\perp]+\dim(\ker A)$. Thus $\operatorname{ind}A=\dim(\ker A)-\dim(\operatorname{ran}A)^\perp=\dim\mathcal H-\dim\mathcal H'$. ■

The next result is actually just a restatement of the Fredholm Alternative (VII. 7.9).

**3.3. Proposition.** *If $K:\mathcal H\to\mathcal H$ is a compact operator and $\lambda\ne0$, then $\lambda+K$ is Fredholm and $\operatorname{ind}(\lambda+K)=0$.*

We already observed that the adjoint of a semi-Fredholm operator is also a semi-Fredholm operator. This same reasoning produces the calculation of the index.

**3.4. Proposition.** (a) *If $A$ is a semi-Fredholm operator, then $A^*$ is also semi-Fredholm and $\operatorname{ind}A^*=-\operatorname{ind}A$.*

(b) *If $N$ is a normal operator on a Hilbert space $\mathcal H$, then $N$ is semi-Fredholm if and only if $N$ is Fredholm, in which case $\operatorname{ind}N=0$.*

(c) *If $A$ and $B$ are Fredholm operators, then $A\oplus B$ is Fredholm and $\operatorname{ind}(A\oplus B)=\operatorname{ind}A+\operatorname{ind}B$.*

**Proof.** As stated, the proof of (a) is easy. For part (b), recall that for a normal operator $N$, $\|Nh\|=\|N^*h\|$ for every vector $h$ in $\mathcal H$. Thus $\ker N=\ker N^*$. The result is now immediate. The proof of (c) is left to the reader. ■

Also see Exercise 2.6 and Proposition 4.5 below.

The next theorem is one of the main properties of the Fredholm index. But first two lemmas are required.
