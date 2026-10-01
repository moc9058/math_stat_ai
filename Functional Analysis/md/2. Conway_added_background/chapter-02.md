# II. Operators on Hilbert Space


<a id="pdf-page-41"></a>
# CHAPTER II

# Operators on Hilbert Space

A large area of current research interest is centered around the theory of operators on Hilbert space. Several other chapters in this book will be devoted to this topic.

There is a marked contrast here between Hilbert spaces and the Banach spaces that are studied in the next chapter. Essentially all of the information about the geometry of Hilbert space is contained in the preceding chapter. The geometry of Banach space lies in darkness and has attracted the attention of many talented research mathematicians. However, the theory of linear operators (linear transformations) on a Banach space has very few general results, whereas Hilbert space operators have an elegant and well-developed general theory. Indeed, the reason for this dichotomy is related to the opposite status of the geometric considerations. Questions concerning operators on Hilbert space don’t necessitate or imply any geometric difficulties.

In addition to the fundamentals of operators, this chapter will also present an interesting application to differential equations in Section 6.

## §1. Elementary Properties and Examples

<!-- BEGIN BACKGROUND BG-II.block1 -->
<a id="bg-ii-1"></a>
### Lemma BG-II.1. Extending an operator from a dense domain

If $D$ is a dense linear manifold in a normed space $X$, $Y$ is complete, and $A:D\to Y$ is linear with $\|Ax\|\leq M\|x\|$, then there is a unique bounded extension $\widetilde A:X\to Y$ with the same norm.

**Proof.** For $x\in X$ choose $x_n\in D$ tending to $x$. Then $\|Ax_n-Ax_m\|\leq M\|x_n-x_m\|$ gives a limit; define $\widetilde Ax$ to be that limit. Applying the same inequality to two approximating sequences shows independence of choice. Limits preserve addition, scalar multiplication and the bound. Every continuous extension must have these values. Restricting to $D$ gives $\|A\|\leq\|\widetilde A\|$, while the construction with $M=\|A\|$ gives the reverse inequality. Thus assigning values on basis vectors alone does not automatically define a bounded operator: one must first check this estimate on finite combinations. $\square$

<a id="bg-ii-2"></a>
### Definition BG-II.2. Essential supremum

For a measurable $\phi$, $\|\phi\|_\infty=\inf\{M\geq0:|\phi|\leq M\text{ a.e.}\}$. This is not the pointwise supremum: altering values on a null set changes neither the $L^\infty$ element nor a multiplication operator on $L^2$.

<a id="bg-ii-3"></a>
### Lemma BG-II.3. Computing a multiplication-operator norm

On a $\sigma$-finite measure space, $\|M_\phi\|=\|\phi\|_\infty$ for bounded measurable $\phi$ acting on a nonzero $L^2$ space.

**Proof.** Integrating $|\phi f|^2\leq\|\phi\|_\infty^2|f|^2$ proves the upper bound. If $0\leq c<\|\phi\|_\infty$, the set $\{|φ|>c\}$ has positive measure. By $\sigma$-finiteness it contains a measurable $E$ of finite positive measure. For $f=\chi_E/\sqrt{\mu(E)}$, $\|f\|_2=1$ and $\|M_\phi f\|_2\geq c$. Let $c$ increase to the essential supremum. The zero-symbol case is immediate. $\square$

<a id="bg-ii-4"></a>
### Theorem BG-II.4. The integral-interchange rule behind kernel operators

For $\sigma$-finite measure spaces, a nonnegative product-measurable $u(x,y)$ has equal product and iterated integrals, allowing $+\infty$ (Tonelli). If $\iint|u|<\infty$, the same equality holds for scalar $u$, with its sections integrable a.e. (Fubini).

**Proof.** On finite-measure spaces the equality and measurability of section integrals hold for indicators of measurable rectangles. The class of sets for which they hold is closed under complements and countable disjoint unions, by subtraction from the finite total mass and monotone convergence. The elementary monotone-class argument therefore extends the assertion from rectangles to their generated product $\sigma$-algebra: a class closed in this manner and containing a generating family closed under finite intersections contains its $\sigma$-algebra. Apply this on an increasing exhaustion by finite-measure rectangles for the $\sigma$-finite case. Nonnegative simple functions follow by linearity, and arbitrary nonnegative functions by increasing simple approximation and monotone convergence. If $\iint|u|<\infty$, Tonelli shows that the integrals of $|u|$ along sections are finite outside a null set. Apply the nonnegative assertion to the positive and negative parts of the real and imaginary parts of $u$ and subtract. $\square$

<a id="bg-ii-5"></a>
### Corollary BG-II.5. Square-integrable kernels and their adjoints

On a $\sigma$-finite measure space, if $k\in L^2(\mu\times\mu)$, then $Kf(x)=\int k(x,y)f(y)\,d\mu(y)$ defines an a.e. class in $L^2$, $\|K\|\leq\|k\|_2$, and its adjoint has kernel $\overline{k(y,x)}$.

**Proof.** For a.e. $x$, Schwarz gives $|Kf(x)|^2\leq(\int|k(x,y)|^2d\mu(y))\|f\|_2^2$. Integration proves the bound. For $f,g\in L^2$, product-space Schwarz bounds

$$
\iint|k(x,y)f(y)\overline{g(x)}|\,d\mu(y)d\mu(x)
\leq\|k\|_2\|f\|_2\|g\|_2.
$$

Fubini is therefore justified in computing $\langle Kf,g\rangle$; moving the conjugation gives exactly $\langle f,K^*g\rangle$ with the stated kernel. For the more general Schur kernels in Example 1.6, the same justification follows from Schwarz with weight $|k|$: the absolute double integral is at most $(c_2\|f\|_2^2)^{1/2}(c_1\|g\|_2^2)^{1/2}$. It is this absolute-integrability check, not merely the formal appearance of two integrals, that licenses the interchange. $\square$
<!-- END BACKGROUND BG-II.block1 -->

The proof of the next proposition is similar to that of Proposition I.3.1 and is left to the reader.

**1.1. Proposition.** *Let $\mathcal{H}$ and $\mathcal{K}$ be Hilbert spaces and $A\colon\mathcal{H}\to\mathcal{K}$ a linear transformation. The following statements are equivalent.*

(a) *$A$ is continuous.*

(b) *$A$ is continuous at $0$.*



<a id="pdf-page-42"></a>
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



<a id="pdf-page-43"></a>
**Exercise 11.** A sufficient condition for the boundedness of an infinite matrix that is useful is known. (See Exercise 9.) Another sufficient condition for a matrix to be bounded can be found on page 61 of Maddox [1980].

**1.5. Theorem.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and put $\mathcal H=L^2(X,\Omega,\mu)\equiv L^2(\mu)$. If $\phi\in L^\infty(\mu)$, define $M_\phi:L^2(\mu)\to L^2(\mu)$ by $M_\phi f=\phi f$. Then $M_\phi\in\mathcal B(L^2(\mu))$ and $\|M_\phi\|=\|\phi\|_\infty$.

**Proof.** Here $\|\phi\|_\infty$ is the $\mu$-essential supremum norm. That is,

$$
\begin{aligned}
\|\phi\|_\infty
&\equiv \inf\{\sup\{|\phi(x)|:x\notin N\}:N\in\Omega,\ \mu(N)=0\}\\
&=\inf\{c>0:\mu(\{x\in X:|\phi(x)|>c\})=0\}.
\end{aligned}
$$

Thus $\|\phi\|_\infty$ is the infimum of all $c>0$ such that $|\phi(x)|\leqslant c$ a.e. $[\mu]$ and, moreover, $|\phi(x)|\leqslant\|\phi\|_\infty$ a.e. $[\mu]$. Thus we can, and do, assume that $\phi$ is a bounded measurable function and $|\phi(x)|\leqslant\|\phi\|_\infty$ for all $x$. So if $f\in L^2(\mu)$, then $\int|\phi f|^2\,d\mu\leqslant\|\phi\|_\infty^2\int|f|^2\,d\mu$. That is, $M_\phi\in\mathcal B(L^2(\mu))$ and $\|M_\phi\|\leqslant\|\phi\|_\infty$. If $\varepsilon>0$, the $\sigma$-finiteness of the measure space implies that there is a set $\Delta$ in $\Omega$, $0<\mu(\Delta)<\infty$, such that $|\phi(x)|\geqslant\|\phi\|_\infty-\varepsilon$ on $\Delta$. (Why?) If $f=(\mu(\Delta))^{-1/2}\chi_\Delta$, then $f\in L^2(\mu)$ and $\|f\|_2=1$. So $\|M_\phi\|^2\geqslant\|\phi f\|_2^2=(\mu(\Delta))^{-1}\int_\Delta|\phi|^2\,d\mu\geqslant(\|\phi\|_\infty-\varepsilon)^2$. Letting $\varepsilon\to0$, we get that $\|M_\phi\|\geqslant\|\phi\|_\infty$. ■

The operator $M_\phi$ is called a *multiplication operator*. The function $\phi$ is its *symbol*.

If the measure space $(X,\Omega,\mu)$ is not $\sigma$-finite, then the conclusion of Theorem 1.5 is not necessarily valid. Indeed, let $\Omega=$ the Borel subsets of $[0,1]$ and define $\mu$ on $\Omega$ by $\mu(\Delta)=$ the Lebesgue measure of $\Delta$ if $0\notin\Delta$ and $\mu(\Delta)=\infty$ if $0\in\Delta$. This measure has an infinite atom at $0$ and, therefore, is not $\sigma$-finite. Let $\phi=\chi_{\{0\}}$. Then $\phi\in L^\infty(\mu)$ and $\|\phi\|_\infty=1$. If $f\in L^2(\mu)$, then $\infty>\int|f|^2\,d\mu\geqslant|f(0)|^2\mu(\{0\})$. Hence every function in $L^2(\mu)$ vanishes at $0$. Therefore $M_\phi=0$ and $\|M_\phi\|<\|\phi\|_\infty$.

There are more general measure spaces for which (1.5) is valid—the decomposable measure spaces (see Kelley [1966]).

**1.6. Theorem.** Let $(X,\Omega,\mu)$ be a measure space and suppose $k:X\times X\to\mathbb F$ is an $\Omega\times\Omega$-measurable function for which there are constants $c_1$ and $c_2$ such that

$$
\begin{aligned}
\int_X |k(x,y)|\,d\mu(y)&\leqslant c_1 \qquad \text{a.e. }[\mu],\\
\int_X |k(x,y)|\,d\mu(x)&\leqslant c_2 \qquad \text{a.e. }[\mu].
\end{aligned}
$$

If $K:L^2(\mu)\to L^2(\mu)$ is defined by

$$
(Kf)(x)=\int k(x,y)f(y)\,d\mu(y),
$$

then $K$ is a bounded linear operator and $\|K\|\leqslant(c_1c_2)^{1/2}$.



<a id="pdf-page-44"></a>
**Proof.** Actually it must be shown that $Kf\in L^2(\mu)$, but this will follow from the argument that demonstrates the boundedness of $K$. If $f\in L^2(\mu)$,

$$
\begin{aligned}
|Kf(x)|
&\leqslant \int |k(x,y)|\,|f(y)|\,d\mu(y)\\
&= \int |k(x,y)|^{1/2}|k(x,y)|^{1/2}|f(y)|\,d\mu(y)\\
&\leqslant
\left[\int |k(x,y)|\,d\mu(y)\right]^{1/2}
\left[\int |k(x,y)|\,|f(y)|^2\,d\mu(y)\right]^{1/2}\\
&\leqslant c_1^{1/2}
\left[\int |k(x,y)|\,|f(y)|^2\,d\mu(y)\right]^{1/2}.
\end{aligned}
$$

Hence

$$
\begin{aligned}
\int |Kf(x)|^2\,d\mu(x)
&\leqslant c_1\int\!\!\int |k(x,y)|\,|f(y)|^2\,d\mu(y)\,d\mu(x)\\
&=c_1\int |f(y)|^2\int |k(x,y)|\,d\mu(x)\,d\mu(y)\\
&\leqslant c_1c_2\|f\|^2.
\end{aligned}
$$

Now this shows that the formula used to define $Kf$ is finite a.e. $[\mu]$, $Kf\in L^2(\mu)$, and $\|Kf\|^2\leqslant c_1c_2\|f\|^2$. ■

The operator described above is called an *integral operator* and the function $k$ is called its kernel. There are conditions on the kernel other than the one in (1.6) that will imply that $K$ is bounded.

A particular example of an integral operator is the *Volterra operator* defined below.

**1.7. Example.** Let $k:[0,1]\times[0,1]\to\mathbb{R}$ be the characteristic function of $\{(x,y):y<x\}$. The corresponding operator $V:L^2(0,1)\to L^2(0,1)$ defined by $Vf(x)=\int_0^1 k(x,y)f(y)\,dy$ is called the *Volterra operator*. Note that

$$
Vf(x)=\int_0^x f(y)\,dy.
$$

Another example of an operator was defined in Example 1.5.3. The nonsurjective isometry defined there is called the *unilateral shift*. It will be studied in more detail later in this book. Note that any isometry is a bounded operator with norm 1.

## Exercises

1. Prove Proposition 1.1.
2. Prove Proposition 1.2.



   <a id="pdf-page-45"></a>
3. Suppose $\{e_1,e_2,\ldots\}$ is an orthonormal basis for $\mathcal H$ and for each $n$ there is a vector $Ae_n$ in $\mathcal H$ such that $\sum\|Ae_n\|<\infty$. Show that $A$ has an unique extension to a bounded operator on $\mathcal H$.

4. Proposition 1.2 says that $d(A,B)=\|A-B\|$ is a metric on $\mathcal B(\mathcal H,\mathcal K)$. Show that $\mathcal B(\mathcal H,\mathcal K)$ is complete relative to this metric.

5. Show that a multiplication operator $M_\phi$ (1.5) satisfies $M_\phi^2=M_\phi$ if and only if $\phi$ is a characteristic function.

6. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $k_1,k_2$ be two kernels satisfying the hypothesis of (1.6). Define

   $$k:X\times X\to\mathbb F\quad\text{by}\quad k(x,y)=\int k_1(x,z)k_2(z,y)\,d\mu(z).$$

   (a) Show that $k$ also satisfies the hypothesis of (1.6). (b) If $K,K_1,K_2$ are the integral operators with kernels $k,k_1,k_2$, show that $K=K_1K_2$. What does this remind you of? Is more going on than an analogy?

7. If $(X,\Omega,\mu)$ is a measure space and $k\in L^2(\mu\times\mu)$, show that $k$ defines a bounded integral operator.

8. Let $\{e_n\}$ be the usual basis for $l^2$ and let $\{\alpha_n\}$ be a sequence of scalars. Show that there is a bounded operator $A$ on $l^2$ such that $Ae_n=\alpha_ne_n$ for all $n$ if and only if $\{\alpha_n\}$ is uniformly bounded, in which case $\|A\|=\sup\{|\alpha_n|:n\geqslant1\}$. This type of operator is called a *diagonal operator* or is said to be *diagonalizable*.

9. (Schur test) Let $\{\alpha_{ij}\}_{i,j=1}^{\infty}$ be an infinite matrix such that $\alpha_{ij}\geqslant0$ for all $i,j$ and such that there are scalars $p_i>0$ and $\beta,\gamma>0$ with

   $$\sum_{i=1}^{\infty}\alpha_{ij}p_i\leqslant\beta p_j,$$

   $$\sum_{j=1}^{\infty}\alpha_{ij}p_j\leqslant\gamma p_i$$

   for all $i,j\geqslant1$. Show that there is an operator $A$ on $l^2(\mathbb N)$ with $\langle Ae_j,e_i\rangle=\alpha_{ij}$ and $\|A\|^2\leqslant\beta\gamma$.

10. (Hilbert matrix) Show that $\langle Ae_j,e_i\rangle=(i+j+1)^{-1}$ for $0\leqslant i,j<\infty$ defines a bounded operator on $l^2(\mathbb N\cup\{0\})$ with $\|A\|\leqslant\pi$. (See also Choi [1983] and Redheffer and Volkmann [1983].)

11. If $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, put $\alpha=[|a|^2+|b|^2+|c|^2+|d|^2]^{1/2}$ and show that $\|A\|=\frac12(\alpha^2+\sqrt{\alpha^4-4\delta^2})$, where $\delta^2=\det A^*A$.

12. (Direct sum of operators) Let $\{\mathcal H_i\}$ be a collection of Hilbert spaces and let $\mathcal H=\bigoplus_i\mathcal H_i$. Suppose $A_i\in\mathcal B(\mathcal H_i)$ for all $i$. Show that there is a bounded operator $A$ on $\mathcal H$ such that $A|_{\mathcal H_i}=A_i$ for all $i$ if and only if $\sup_i\|A_i\|<\infty$. In this case, $\|A\|=\sup_i\|A_i\|$. The operator $A$ is called the *direct sum* of the operators $\{A_i\}$ and is denoted by $A=\bigoplus_i A_i$.


    <a id="pdf-page-46"></a>
13. (Bari [1951]) Call a sequence of vectors $\{f_n\}$ in a Hilbert space $\mathcal H$ a *Bessel sequence* if $\sum |\langle f,f_n\rangle|^2<\infty$ for every $f$ in $\mathcal H$. Show that a sequence $\{f_n\}$ of vectors in $\mathcal H$ is a Bessel sequence if and only if the infinite matrix $(\langle f_m,f_n\rangle)$ defines a bounded operator on $l^2$. (Also see Shapiro and Shields [1961], p. 524.)

# §2. The Adjoint of an Operator

**2.1. Definition.** If $\mathcal H$ and $\mathcal K$ are Hilbert spaces, a function $u:\mathcal H\times\mathcal K\to\mathbb F$ is a *sesquilinear form* if for $h,g$ in $\mathcal H$, $k,f$ in $\mathcal K$, and $\alpha,\beta$ in $\mathbb F$,

(a) $u(\alpha h+\beta g,k)=\alpha u(h,k)+\beta u(g,k)$;

(b) $u(h,\alpha k+\beta f)=\bar\alpha u(h,k)+\bar\beta u(h,f)$.

The prefix “sesqui” is used because the function is linear in one variable but (for $\mathbb F=\mathbb C$) only conjugate linear in the other. (“Sesqui” means “one-and-a-half.”)

A sesquilinear form is *bounded* if there is a constant $M$ such that $|u(h,k)|\leq M\|h\|\|k\|$ for all $h$ in $\mathcal H$ and $k$ in $\mathcal K$. The constant $M$ is called a bound for $u$.

Sesquilinear forms are used to study operators. If $A\in\mathcal B(\mathcal H,\mathcal K)$, then $u(h,k)\equiv\langle Ah,k\rangle$ is a bounded sesquilinear form. Also, if $B\in\mathcal B(\mathcal K,\mathcal H)$, $u(h,k)\equiv\langle h,Bk\rangle$ is a bounded sesquilinear form. Are there any more? Are these two forms related?

**2.2. Theorem.** *If $u:\mathcal H\times\mathcal K\to\mathbb F$ is a bounded sesquilinear form with bound $M$, then there are unique operators $A$ in $\mathcal B(\mathcal H,\mathcal K)$ and $B$ in $\mathcal B(\mathcal K,\mathcal H)$ such that*

$$
\tag{2.3} u(h,k)=\langle Ah,k\rangle=\langle h,Bk\rangle
$$

*for all $h$ in $\mathcal H$ and $k$ in $\mathcal K$ and $\|A\|,\ \|B\|\leq M$.*

**Proof.** Only the existence of $A$ will be shown. For each $h$ in $\mathcal H$, define $L_h:\mathcal K\to\mathbb F$ by $L_h(k)=\overline{u(h,k)}$. Then $L_h$ is linear and $|L_h(k)|\leq M\|h\|\|k\|$. By the Riesz Representation Theorem there is a unique vector $f$ in $\mathcal K$ such that $\langle k,f\rangle=L_h(k)=\overline{u(h,k)}$ and $\|f\|\leq M\|h\|$. Let $Ah=f$. It is left as an exercise to show that $A$ is linear (use the uniqueness part of the Riesz Theorem). Also, $\langle Ah,k\rangle=\overline{\langle k,Ah\rangle}=\overline{\langle k,f\rangle}=u(h,k)$.

If $A_1\in\mathcal B(\mathcal H,\mathcal K)$ and $u(h,k)=\langle A_1h,k\rangle$, then $\langle Ah-A_1h,k\rangle=0$ for all $k$; thus $Ah-A_1h=0$ for all $h$. Thus, $A$ is unique. $\blacksquare$

**2.4. Definition.** If $A\in\mathcal B(\mathcal H,\mathcal K)$, then the unique operator $B$ in $\mathcal B(\mathcal K,\mathcal H)$ satisfying (2.3) is called the *adjoint* of $A$ and is denoted by $B=A^*$.

The adjoint of an operator will usually be used for operators in $\mathcal B(\mathcal H)$, rather than $\mathcal B(\mathcal H,\mathcal K)$. There is one notable exception.



<a id="pdf-page-47"></a>
**2.5. Proposition.** If $U\in\mathcal{B}(\mathcal{H},\mathcal{K})$, then $U$ is an isomorphism if and only if $U$ is invertible and $U^{-1}=U^*$.

**Proof.** Exercise.

From now on we will examine and prove results for the adjoint of operators in $\mathcal{B}(\mathcal{H})$. Often, as in the next proposition, there are analogous results for the adjoint of operators in $\mathcal{B}(\mathcal{H},\mathcal{K})$. This simplification is justified, however, by the cleaner statements that result. Also, the interested reader will have no trouble formulating the more general statement when it is needed.

**2.6. Proposition.** If $A,B\in\mathcal{B}(\mathcal{H})$ and $\alpha\in\mathbb{F}$, then:

(a) $(\alpha A+B)^*=\bar{\alpha}A^*+B^*$.

(b) $(AB)^*=B^*A^*$.

(c) $A^{**}\equiv(A^*)^*=A$.

(d) If $A$ is invertible in $\mathcal{B}(\mathcal{H})$ and $A^{-1}$ is its inverse, then $A^*$ is invertible and $(A^*)^{-1}=(A^{-1})^*$.

The proof of the preceding proposition is left as an exercise, but a word about part (d) might be helpful. The hypothesis that $A$ is invertible in $\mathcal{B}(\mathcal{H})$ means that there is an operator $A^{-1}$ in $\mathcal{B}(\mathcal{H})$ such that $AA^{-1}=A^{-1}A=I$. It is a remarkable fact that if $A$ is only assumed to be bijective, then $A$ is invertible in $\mathcal{B}(\mathcal{H})$. This is a consequence of the Open Mapping Theorem, which will be proved later.

**2.7. Proposition.** If $A\in\mathcal{B}(\mathcal{H})$, $\|A\|=\|A^*\|=\|A^*A\|^{1/2}$.

**Proof.** For $h$ in $\mathcal{H}$, $\|h\|\leq 1$,
$$
\|Ah\|^2=\langle Ah,Ah\rangle=\langle A^*Ah,h\rangle
\leq\|A^*Ah\|\,\|h\|\leq\|A^*A\|\leq\|A^*\|\,\|A\|.
$$
Hence $\|A\|^2\leq\|A^*A\|\leq\|A^*\|\,\|A\|$. Using the two ends of this string of inequalities gives $\|A\|\leq\|A^*\|$ when $\|A\|$ is cancelled. But $A=A^{**}$ and so if $A^*$ is substituted for $A$, we get $\|A^*\|\leq\|A^{**}\|=\|A\|$. Hence $\|A\|=\|A^*\|$. Thus the string of inequalities becomes a string of equalities and the proof is complete. $\blacksquare$

**2.8. Example.** Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space and let $M_\phi$ be the multiplication operator with symbol $\phi$ (1.5). Then $M_\phi^*$ is $M_{\bar\phi}$, the multiplication operator with symbol $\bar\phi$.

If an operator on $\mathbb{F}^d$ is presented by a matrix, then its adjoint is represented by the conjuagate transpose of the matrix.

**2.9. Example.** If $K$ is the integral operator with kernel $k$ as in (1.6), then $K^*$ is the integral operator with kernel $k^*(x,y)\equiv\overline{k(y,x)}$.

**2.10. Proposition.** If $S:\ell^2\to\ell^2$ is defined by $S(\alpha_1,\alpha_2,\ldots)=(0,\alpha_1,\alpha_2,\ldots)$, then $S$ is an isometry and $S^*(\alpha_1,\alpha_2,\ldots)=(\alpha_2,\alpha_3,\ldots)$.



<a id="pdf-page-48"></a>
**Proof.** It has already been mentioned that $S$ is an isometry (I.5.3). For $(\alpha_n)$ and $(\beta_n)$ in $l^2$,
$$
\begin{aligned}
\langle S^*(\alpha_n),(\beta_n)\rangle
&=\langle(\alpha_n),S(\beta_n)\rangle\\
&=\langle(\alpha_1,\alpha_2,\ldots),(0,\beta_1,\beta_2,\ldots)\rangle\\
&=\alpha_2\overline{\beta}_1+\alpha_3\overline{\beta}_2+\cdots\\
&=\langle(\alpha_2,\alpha_3,\ldots),(\beta_1,\beta_2,\ldots)\rangle.
\end{aligned}
$$
Since this holds for every $(\beta_n)$, the result is proved. ■

The operator $S$ in (2.10) is called the *unilateral shift* and the operator $S^*$ is called the *backward shift*.

The operation of taking the adjoint of an operator is, as the reader may have seen from the examples above, analogous to taking the conjugate of a complex number. It is good to keep the analogy in mind, but do not become too religious about it.

**2.11. Definition.** If $A\in\mathcal{B}(\mathcal{H})$, then: (a) is *hermitian* or *self-adjoint* if $A^*=A$; (b) $A$ is *normal* if $AA^*=A^*A$.

In the analogy between the adjoint and the complex conjugate, hermitian operators become the analogues of real numbers and, by (2.5), unitaries are the analogues of complex numbers of modulus 1. Normal operators, as we shall see, are the true analogues of complex numbers. Notice that hermitian and unitary operators are normal.

In light of (2.8), every multiplication operator $M_\phi$ is normal; $M_\phi$ is hermitian if and only if $\phi$ is real-valued; $M_\phi$ is unitary if and only if $|\phi|\equiv 1$ a.e. $[\mu]$. By (2.9), an integral operator $K$ with kernel $k$ is hermitian if and only if $k(x,y)=\overline{k(y,x)}$ a.e. $[\mu\times\mu]$. The unilateral shift is not normal (Exercise 6).

**2.12. Proposition.** If $\mathcal{H}$ is a $\mathbb{C}$-Hilbert space and $A\in\mathcal{B}(\mathcal{H})$, then $A$ is hermitian if and only if $\langle Ah,h\rangle\in\mathbb{R}$ for all $h$ in $\mathcal{H}$.

**Proof.** If $A=A^*$, then $\langle Ah,h\rangle=\langle h,Ah\rangle=\overline{\langle Ah,h\rangle}$; hence $\langle Ah,h\rangle\in\mathbb{R}$.

For the converse, assume $\langle Ah,h\rangle$ is real for every $h$ in $\mathcal{H}$. If $\alpha\in\mathbb{C}$ and $h,g\in\mathcal{H}$, then $\langle A(h+\alpha g),h+\alpha g\rangle=\langle Ah,h\rangle+\overline{\alpha}\langle Ah,g\rangle+\alpha\langle Ag,h\rangle+|\alpha|^2\langle Ag,g\rangle\in\mathbb{R}$. So this expression equals its complex conjugate. Using the fact that $\langle Ah,h\rangle$ and $\langle Ag,g\rangle\in\mathbb{R}$ yields
$$
\begin{aligned}
\alpha\langle Ag,h\rangle+\overline{\alpha}\langle Ah,g\rangle
&=\overline{\alpha}\langle h,Ag\rangle+\alpha\langle g,Ah\rangle\\
&=\overline{\alpha}\langle A^*h,g\rangle+\alpha\langle A^*g,h\rangle.
\end{aligned}
$$
By first taking $\alpha=1$ and then $\alpha=i$, we obtain the two equations
$$
\langle Ag,h\rangle+\langle Ah,g\rangle
=\langle A^*h,g\rangle+\langle A^*g,h\rangle,
$$
$$
i\langle Ag,h\rangle-i\langle Ah,g\rangle
=-i\langle A^*h,g\rangle+i\langle A^*g,h\rangle.
$$
A little arithmetic implies $\langle Ag,h\rangle=\langle A^*g,h\rangle$, so $A=A^*$. ■

The preceding proposition is false if it is only assumed that $\mathcal{H}$ is an $\mathbb{R}$-Hilbert space. For example, if $A=\begin{bmatrix}0&1\\-1&0\end{bmatrix}$ on $\mathbb{R}^2$, then $\langle Ah,h\rangle=0$ for



<a id="pdf-page-49"></a>
all $h$ in $\mathbb{R}^{2}$. However, $A^{*}$ is the transpose of $A$ and so $A^{*}\ne A$. Indeed, for any operator $A$ on an $\mathbb{R}$-Hilbert space, $\langle Ah,g\rangle\in\mathbb{R}$.

**2.13. Proposition.** *If $A=A^{*}$, then*

$$
\|A\|=\sup\{|\langle Ah,h\rangle|:\|h\|=1\}.
$$

**Proof.** Put $M=\sup\{|\langle Ah,h\rangle|:\|h\|=1\}$. If $\|h\|=1$, then $|\langle Ah,h\rangle|\leqslant\|A\|$; hence $M\leqslant\|A\|$. On the other hand, if $\|h\|=\|g\|=1$, then

$$
\begin{aligned}
\langle A(h\pm g),h\pm g\rangle
&=\langle Ah,h\rangle\pm\langle Ah,g\rangle\pm\langle Ag,h\rangle+\langle Ag,g\rangle\\
&=\langle Ah,h\rangle\pm\langle Ah,g\rangle\pm\langle g,A^{*}h\rangle+\langle Ag,g\rangle.
\end{aligned}
$$

Since $A=A^{*}$, this implies

$$
\langle A(h\pm g),h\pm g\rangle
=\langle Ah,h\rangle\pm 2\operatorname{Re}\langle Ah,g\rangle+\langle Ag,g\rangle.
$$

Subtracting one of these two equations from the other gives

$$
4\operatorname{Re}\langle Ah,g\rangle
=\langle A(h+g),h+g\rangle-\langle A(h-g),h-g\rangle.
$$

Now it is easy to verify that $|\langle Af,f\rangle|\leqslant M\|f\|^{2}$ for any $f$ in $\mathcal H$. Hence using the parallelogram law we get

$$
\begin{aligned}
4\operatorname{Re}\langle Ah,g\rangle
&\leqslant M(\|h+g\|^{2}+\|h-g\|^{2})\\
&=2M(\|h\|^{2}+\|g\|^{2})\\
&=4M
\end{aligned}
$$

since $h$ and $g$ are unit vectors. Now suppose $\langle Ah,g\rangle=e^{i\theta}|\langle Ah,g\rangle|$. Replacing $h$ in the inequality above with $e^{-i\theta}h$ gives $|\langle Ah,g\rangle|\leqslant M$ if $\|h\|=\|g\|=1$. Taking the supremum over all $g$ gives $\|Ah\|\leqslant M$ when $\|h\|=1$. Thus $\|A\|\leqslant M$. $\blacksquare$

**2.14. Corollary.** *If $A=A^{*}$ and $\langle Ah,h\rangle=0$ for all $h$, then $A=0$.*

The preceding corollary is not true unless $A=A^{*}$, as the example given after Proposition 2.12 shows. However, if a complex Hilbert space is present, this hypothesis can be deleted.

**2.15. Proposition.** *If $\mathcal H$ is a $\mathbb C$-Hilbert space and $A\in\mathcal B(\mathcal H)$ such that $\langle Ah,h\rangle=0$ for all $h$ in $\mathcal H$, then $A=0$.*

The proof of (2.15) is left to the reader.

If $\mathcal H$ is a $\mathbb C$-Hilbert space and $A\in\mathcal B(\mathcal H)$, then $B=(A+A^{*})/2$ and $C=(A-A^{*})/2i$ are self-adjoint and $A=B+iC$. The operators $B$ and $C$ are called, respectively, the *real and imaginary parts* of $A$.

**2.16. Proposition.** *If $A\in\mathcal B(\mathcal H)$, the following statement are equivalent.*

(a) $A$ is normal.



<a id="pdf-page-50"></a>
(b) $\|Ah\|=\|A^*h\|$ for all $h$.

If $\mathcal H$ is a $\mathbb C$-Hilbert space, then these statements are also equivalent to:

(c) The real and imaginary parts of $A$ commute.

**Proof.** If $h\in\mathcal H$, then $\|Ah\|^2-\|A^*h\|^2=\langle Ah,Ah\rangle-\langle A^*h,A^*h\rangle=\langle(A^*A-AA^*)h,h\rangle$. Since $A^*A-AA^*$ is hermitian, the equivalence of (a) and (b) follows from Corollary 2.14.

If $B,C$ are real and imaginary parts of $A$, then a calculation yields

$$
A^*A=B^2-iCB+iBC+C^2,
$$

$$
AA^*=B^2+iCB-iBC+C^2.
$$

Hence $A^*A=AA^*$ if and only if $CB=BC$, and so (a) and (c) are equivalent. $\blacksquare$

**2.17. Proposition.** *If $A\in\mathcal B(\mathcal H)$, the following statements are equivalent.*

(a) $A$ is an isometry.

(b) $A^*A=I$.

(c) $\langle Ah,Ag\rangle=\langle h,g\rangle$ for all $h,g$ in $\mathcal H$.

**Proof.** The proof that (a) and (c) are equivalent was seen in Proposition I.5.2. Note that if $h,g\in\mathcal H$, then $\langle A^*Ah,g\rangle=\langle Ah,Ag\rangle$. Hence (b) and (c) are easily seen to be equivalent. $\blacksquare$

**2.18. Proposition.** *If $A\in\mathcal B(\mathcal H)$, then the following statements are equivalent.*

(a) $A^*A=AA^*=I$.

(b) $A$ is unitary. (That is, $A$ is a surjective isometry.)

(c) $A$ is a normal isometry.

**Proof.** (a)$\Rightarrow$(b): Proposition I.5.2.

(b)$\Rightarrow$(c): By (2.17), $A^*A=I$. But it is easy to see that the fact that $A$ is a surjective isometry implies that $A^{-1}$ is also. Hence by (2.17) $I=(A^{-1})^*A^{-1}=(A^*)^{-1}A^{-1}=(AA^*)^{-1}$; this implies that $A^*A=AA^*=I$.

(c)$\Rightarrow$(a): By (2.17), $A^*A=I$. Since $A$ is also normal, $AA^*=A^*A=I$ and so $A$ is surjective. $\blacksquare$

We conclude with a very important, though easily proved, result.

**2.19. Theorem.** *If $A\in\mathcal B(\mathcal H)$, then $\ker A=(\operatorname{ran}A^*)^\perp$.*

**Proof.** If $h\in\ker A$ and $g\in\mathcal H$, then $\langle h,A^*g\rangle=\langle Ah,g\rangle=0$, so $\ker A\subseteq(\operatorname{ran}A^*)^\perp$. On the other hand, if $h\perp\operatorname{ran}A^*$ and $g\in\mathcal H$, then $\langle Ah,g\rangle=\langle h,A^*g\rangle=0$; so $(\operatorname{ran}A^*)^\perp\subseteq\ker A$. $\blacksquare$

Two facts should be noted. Since $A^{**}=A$, it also holds that $\ker A^*=(\operatorname{ran}A)^\perp$. Second, it is not true that $(\ker A)^\perp=\operatorname{ran}A^*$ since $\operatorname{ran}A^*$ may not



<a id="pdf-page-51"></a>
be closed. All that can be said is that $(\ker A)^\perp=\operatorname{cl}(\operatorname{ran}A^*)$ and $(\ker A^*)^\perp=\operatorname{cl}(\operatorname{ran}A)$.

## Exercises

1. Prove Proposition 2.5.

2. Prove Proposition 2.6.

3. Verify the statement in Example 2.8.

4. Verify the statement in Example 2.9.

5. Find the adjoint of a diagonal operator (Exercise 1.8).

6. Let $S$ be the unilateral shift and compute $SS^*$ and $S^*S$. Also compute $S^nS^{*n}$ and $S^{*n}S^n$.

7. Compute the adjoint of the Volterra operator $V$ (1.7) and $V+V^*$. What is $\operatorname{ran}(V+V^*)$?

8. Where was the hypothesis that $\mathcal H$ is a Hilbert space over $\mathbb C$ used in the proof of Proposition 2.12?

9. Suppose $A=B+iC$, where $B$ and $C$ are hermitian and prove that $B=(A+A^*)/2$, $C=(A-A^*)/2i$.

10. Prove Proposition 2.15.

11. If $A$ and $B$ are self-adjoint, show that $AB$ is self-adjoint if and only if $AB=BA$.

12. Let $\sum_{n=0}^{\infty}\alpha_nz^n$ be a power series with radius of convergence $R$, $0<R\leqslant\infty$. If $A\in\mathcal B(\mathcal H)$ and $\|A\|<R$, show that there is an operator $T$ in $\mathcal B(\mathcal H)$ such that for any $h,g$ in $\mathcal H$, $\langle Th,g\rangle=\sum_{n=0}^{\infty}\alpha_n\langle A^nh,g\rangle$. [If $f(z)=\sum\alpha_nz^n$, the operator $T$ is usually denoted by $f(A)$.]

13. Let $A$ and $T$ be as in Exercise 12 and show that $\|T-\sum_{k=0}^{n}\alpha_kA^k\|\to0$ as $n\to\infty$. If $BA=AB$, show that $BT=TB$.

14. If $f(z)=\exp z=\sum_{n=0}^{\infty}z^n/n!$ and $A$ is hermitian, show that $f(iA)$ is unitary.

15. If $A$ is a normal operator on $\mathcal H$, show that $A$ is injective if and only if $A$ has dense range. Give an example of an operator $B$ such that $\ker B=(0)$ but $\operatorname{ran}B$ is not dense. Give an example of an operator $C$ such that $C$ is surjective but $\ker C\ne(0)$.

16. Let $M_\phi$ be a multiplication operator (1.5) and show that $\ker M_\phi=0$ if and only if $\mu(\{x:\phi(x)=0\})=0$. Give necessary and sufficient conditions on $\phi$ that $\operatorname{ran}M_\phi$ be closed.

## §3. Projections and Idempotents; Invariant and Reducing Subspaces

**3.1. Definition.** An *idempotent* on $\mathcal H$ is a bounded linear operator $E$ on $\mathcal H$ such that $E^2=E$. A *projection* is an idempotent $P$ such that $\ker P=(\operatorname{ran}P)^\perp$.



<a id="pdf-page-52"></a>
If $\mathcal M\leq\mathcal H$, then $P_{\mathcal M}$ is a projection (Theorem I.2.7). It is not difficult to construct an idempotent that is not a projection (Exercise 1).

Let $E$ be any idempotent and set $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$. Since $E$ is continuous, $\mathcal N$ is a closed subspace of $\mathcal H$. Notice that $(I-E)^2=I-2E+E^2=I-2E+E=I-E$; thus $I-E$ is also an idempotent. Also, $0=(I-E)h=h-Eh$, if and only if $Eh=h$. So $\operatorname{ran}E\supseteq\ker(I-E)$. On the other hand, if $h\in\operatorname{ran}E$, $h=Eg$ and so $Eh=E^2g=Eg=h$; hence $\operatorname{ran}E=\ker(I-E)$. Similarly, $\operatorname{ran}(I-E)=\ker E$. These facts are recorded here.

**3.2. Proposition.** (a) $E$ is an idempotent if and only if $I-E$ is an idempotent. (b) $\operatorname{ran}E=\ker(I-E)$, $\ker E=\operatorname{ran}(I-E)$, and both $\operatorname{ran}E$ and $\ker E$ are closed linear subspaces of $\mathcal H$. (c) If $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$, then $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N=\mathcal H$.

The proof of part (c) is left as an exercise. There is also a converse to (c). If $\mathcal M,\mathcal N\leq\mathcal H$, $\mathcal M\cap\mathcal N=(0)$, and $\mathcal M+\mathcal N=\mathcal H$, then there is an idempotent $E$ such that $\mathcal M=\operatorname{ran}E$ and $\mathcal N=\ker E$; moreover, $E$ is unique. The difficult part in proving this converse is to show that $E$ is bounded. The same fact is true in more generality (for Banach spaces) and so this proof will be postponed.

Now we turn our attention to projections, which are peculiar to Hilbert space.

**3.3. Proposition.** If $E$ is an idempotent on $\mathcal H$ and $E\neq0$, the following statements are equivalent.

(a) $E$ is a projection.

(b) $E$ is the orthogonal projection of $\mathcal H$ onto $\operatorname{ran}E$.

(c) $\|E\|=1$.

(d) $E$ is hermitian.

(e) $E$ is normal.

(f) $\langle Eh,h\rangle\geq0$ for all $h$ in $\mathcal H$.

**PROOF.** $(a)\Rightarrow(b)$: Let $\mathcal M=\operatorname{ran}E$ and $P=P_{\mathcal M}$. If $h\in\mathcal H$, $Ph=$ the unique vector in $\mathcal M$ such that $h-Ph\in\mathcal M^\perp=(\operatorname{ran}E)^\perp=\ker E$ by (a). But $h-Eh=(I-E)h\in\ker E$. Hence $Eh=Ph$ by uniqueness.

$(b)\Rightarrow(c)$: By (I.2.7), $\|E\|\leq1$. But $Eh=h$ for $h$ in $\operatorname{ran}E$, so $\|E\|=1$.

$(c)\Rightarrow(a)$: Let $h\in(\ker E)^\perp$. Now $\operatorname{ran}(I-E)=\ker E$, so $h-Eh\in\ker E$. Hence $0=\langle h-Eh,h\rangle=\|h\|^2-\langle Eh,h\rangle$. Hence $\|h\|^2=\langle Eh,h\rangle\leq\|Eh\|\|h\|\leq\|h\|^2$. So for $h$ in $(\ker E)^\perp$, $\|Eh\|=\|h\|=\langle Eh,h\rangle^{1/2}$. But then for $h$ in $(\ker E)^\perp$,

$$
\|h-Eh\|^2=\|h\|^2-2\operatorname{Re}\langle Eh,h\rangle+\|Eh\|^2=0.
$$

That is, $(\ker E)^\perp\subseteq\ker(I-E)=\operatorname{ran}E$. On the other hand, if $g\in\operatorname{ran}E$, $g=g_1+g_2$, where $g_1\in\ker E$ and $g_2\in(\ker E)^\perp$. Thus $g=Eg=Eg_2=g_2$; that is, $\operatorname{ran}E\subseteq(\ker E)^\perp$. Therefore $\operatorname{ran}E=(\ker E)^\perp$ and $E$ is a projection.



<a id="pdf-page-53"></a>
$(b)\Rightarrow(f)$: If $h\in\mathcal H$, write $h=h_1+h_2$, $h_1\in\operatorname{ran}E$, $h_2\in\ker E=(\operatorname{ran}E)^\perp$. Hence $\langle Eh,h\rangle=\langle E(h_1+h_2),h_1+h_2\rangle=\langle Eh_1,h_1\rangle=\langle h_1,h_1\rangle=\|h_1\|^2\geq 0$.

$(f)\Rightarrow(a)$: Let $h_1\in\operatorname{ran}E$ and $h_2\in\ker E$. Then by (f), $0\leq\langle E(h_1+h_2),h_1+h_2\rangle=\langle h_1,h_1\rangle+\langle h_1,h_2\rangle$. Hence $-\|h_1\|^2\leq\langle h_1,h_2\rangle$ for all $h_1$ in $\operatorname{ran}E$ and $h_2$ in $\ker E$. If there are such $h_1$ and $h_2$ with $\langle h_1,h_2\rangle=\bar\alpha\neq 0$, then substituting $k_2=-2\alpha^{-1}\|h_1\|^2h_2$ for $h_2$ in this inequality, we obtain $-\|h_1\|^2\leq-2\|h_1\|^2$, a contradiction. Hence $\langle h_1,h_2\rangle=0$ whenever $h_1\in\operatorname{ran}E$ and $h_2\in\ker E$. That is, $E$ is a projection.

$(a)\Rightarrow(d)$: Let $h,g\in\mathcal H$ and put $h=h_1+h_2$ and $g=g_1+g_2$, where $h_1,g_1\in\operatorname{ran}E$ and $h_2,g_2\in\ker E=(\operatorname{ran}E)^\perp$. Hence $\langle Eh,g\rangle=\langle h_1,g_1\rangle$. Also, $\langle E^*h,g\rangle=\langle h,Eg\rangle=\langle h_1,g_1\rangle=\langle Eh,g\rangle$. Thus $E=E^*$.

$(d)\Rightarrow(e)$: clear.

$(e)\Rightarrow(a)$: By (2.16), $\|Eh\|=\|E^*h\|$ for every $h$. Hence $\ker E=\ker E^*$. But by (2.19), $\ker E^*=(\operatorname{ran}E)^\perp$, so $E$ is a projection. $\blacksquare$

Note that by part (b) of the preceding proposition, if $E$ is a projection and $\mathcal M=\operatorname{ran}E$, then $E=P_{\mathcal M}$.

Let $P$ be a projection with $\operatorname{ran}P=\mathcal M$ and $\ker P=\mathcal N$. So both $\mathcal M$ and $\mathcal N$ are closed subspaces of $\mathcal H$ and, hence, are also Hilbert spaces. As in (I.6.1), we can form $\mathcal M\oplus\mathcal N$. If $U:\mathcal M\oplus\mathcal N\to\mathcal H$ is defined by $U(h\oplus g)=h+g$ for $h$ in $\mathcal M$ and $g$ in $\mathcal N$, then it is easy to see that $U$ is an isomorphism. Making this identification, we will often write $\mathcal H=\mathcal M\oplus\mathcal N$.

More generally, the following will be used.

**3.4. Definition.** If $\{\mathcal M_i\}$ is a collection of pairwise orthogonal subspaces of $\mathcal H$, then
$$
\bigoplus_i\mathcal M_i\equiv\bigvee_i\mathcal M_i.
$$

If $\mathcal M$ and $\mathcal N$ are two closed linear subspaces of $\mathcal H$, then
$$
\mathcal M\ominus\mathcal N\equiv\mathcal M\cap\mathcal N^\perp.
$$

This is called the *orthogonal difference* of $\mathcal M$ and $\mathcal N$.

Note that if $\mathcal M,\mathcal N\leq\mathcal H$ and $\mathcal M\perp\mathcal N$, then $\mathcal M+\mathcal N$ is closed. (Why?) Hence $\mathcal M\oplus\mathcal N=\mathcal M+\mathcal N$. The same is true, of course, for any finite collection of pairwise orthogonal subspaces but not for infinite collections.

**3.5. Definition.** If $A\in\mathcal B(\mathcal H)$ and $\mathcal M\leq\mathcal H$, say that $\mathcal M$ is an *invariant subspace* for $A$ if $Ah\in\mathcal M$ whenever $h\in\mathcal M$. In other words, if $A\mathcal M\subseteq\mathcal M$. Say that $\mathcal M$ is a *reducing subspace* for $A$ if $A\mathcal M\subseteq\mathcal M$ and $A\mathcal M^\perp\subseteq\mathcal M^\perp$.

If $\mathcal M\leq\mathcal H$, then $\mathcal H=\mathcal M\oplus\mathcal M^\perp$. If $A\in\mathcal B(\mathcal H)$, then $A$ can be written as a $2\times2$ matrix with operator entries,
$$
A=\begin{bmatrix}W&X\\Y&Z\end{bmatrix},\tag{3.6}
$$
where $W\in\mathcal B(\mathcal M)$, $X\in\mathcal B(\mathcal M^\perp,\mathcal M)$, $Y\in\mathcal B(\mathcal M,\mathcal M^\perp)$, and $Z\in\mathcal B(\mathcal M^\perp)$.


<a id="pdf-page-54"></a>
**3.7. Proposition.** If $A\in\mathcal{B}(\mathcal{H})$, $\mathcal{M}\leq\mathcal{H}$, and $P=P_{\mathcal{M}}$, then statements (a) through (c) are equivalent.

(a) $\mathcal{M}$ is invariant for $A$.  
(b) $PAP=AP$.  
(c) In (3.6), $Y=0$.

Also, statements (d) through (g) are equivalent.

(d) $\mathcal{M}$ reduces $A$.  
(e) $PA=AP$.  
(f) In (3.6), $Y$ and $X$ are $0$.  
(g) $\mathcal{M}$ is invariant for both $A$ and $A^*$.

**Proof.** (a)$\Rightarrow$(b): If $h\in\mathcal{H}$, $Ph\in\mathcal{M}$. So $APh\in\mathcal{M}$. Hence, $P(APh)=APh$. That is, $PAP=AP$.

(b)$\Rightarrow$(c): If $P$ is represented as a $2\times2$ operator matrix relative to $\mathcal{H}=\mathcal{M}\oplus\mathcal{M}^{\perp}$, then

$$
P=\begin{bmatrix}I&0\\0&0\end{bmatrix}.
$$

Hence,

$$
PAP=\begin{bmatrix}W&0\\0&0\end{bmatrix}
=AP=\begin{bmatrix}W&0\\Y&0\end{bmatrix}.
$$

So $Y=0$.

(c)$\Rightarrow$(a): If $Y=0$ and $h\in\mathcal{M}$, then

$$
Ah=\begin{bmatrix}W&X\\0&Z\end{bmatrix}
\begin{bmatrix}h\\0\end{bmatrix}
=\begin{bmatrix}Wh\\0\end{bmatrix}\in\mathcal{M}.
$$

(d)$\Rightarrow$(e): Since both $\mathcal{M}$ and $\mathcal{M}^{\perp}$ are invariant for $A$, (b) implies that $AP=PAP$ and $A(I-P)=(I-P)A(I-P)$. Multiplying this second equation gives $A-AP=A-AP-PA+PAP$. Thus $PA=PAP=AP$.

(e)$\Rightarrow$(f): Exercise.

(f)$\Rightarrow$(g): If $X=Y=0$, then

$$
A=\begin{bmatrix}W&0\\0&Z\end{bmatrix}
\quad\text{and}\quad
A^*=\begin{bmatrix}W^*&0\\0&Z^*\end{bmatrix}.
$$

By (c), $\mathcal{M}$ is invariant for both $A$ and $A^*$.

(g)$\Rightarrow$(d): If $h\in\mathcal{M}^{\perp}$ and $g\in\mathcal{M}$, then $\langle g,Ah\rangle=\langle A^*g,h\rangle=0$ since $A^*g\in\mathcal{M}$. Since $g$ was an arbitrary vector in $\mathcal{M}$, $Ah\in\mathcal{M}^{\perp}$. That is, $A\mathcal{M}^{\perp}\subseteq\mathcal{M}^{\perp}$. $\blacksquare$

If $\mathcal{M}$ reduces $A$, then $X=Y=0$ in (3.6). This says that a study of $A$ is reduced to the study of the smaller operators $W$ and $Z$. This is the reason for the terminology.

If $A\in\mathcal{B}(\mathcal{H})$ and $\mathcal{M}$ is an invariant subspace for $A$, then $A|_{\mathcal{M}}$ is used to denote the restriction of $A$ to $\mathcal{M}$. That is, $A|_{\mathcal{M}}$ is the operator on $\mathcal{M}$ defined



<a id="pdf-page-55"></a>
by $(A|_{\mathcal M})h=Ah$ whenever $h\in\mathcal M$. Note that $A|_{\mathcal M}\in\mathcal B(\mathcal M)$ and $\|A|_{\mathcal M}\|\leq\|A\|$. Also, if $\mathcal M$ is invariant for $A$ and $A$ has the representation (3.6) with $Y=0$, then $W=A|_{\mathcal M}$.

## Exercises

1. Let $\mathcal H$ be the two-dimensional real Hilbert space $\mathbb R^2$, let $\mathcal M\equiv\{(x,0)\in\mathbb R^2:x\in\mathbb R\}$ and let $\mathcal N\equiv\{(x,x\tan\theta):x\in\mathbb R\}$, where $0<\theta<\frac12\pi$. Find a formula for the idempotent $E_\theta$ with $\operatorname{ran}E_\theta=\mathcal M$ and $\ker E_\theta=\mathcal N$. Show that $\|E_\theta\|=(\sin\theta)^{-1}$.

2. Prove Proposition 3.2 (c).

3. Let $\{\mathcal M_i:i\in I\}$ be a collection of closed subspaces of $\mathcal H$ and show that $\bigcap\{\mathcal M_i^\perp:i\in I\}=[\bigvee\{\mathcal M_i:i\in I\}]^\perp$ and $[\bigcap\{\mathcal M_i:i\in I\}]^\perp=\bigvee\{\mathcal M_i^\perp:i\in I\}$.

4. Let $P$ and $Q$ be projections. Show: (a) $P+Q$ is a projection if and only if $\operatorname{ran}P\perp\operatorname{ran}Q$. If $P+Q$ is a projection, then $\operatorname{ran}(P+Q)=\operatorname{ran}P+\operatorname{ran}Q$ and $\ker(P+Q)=\ker P\cap\ker Q$. (b) $PQ$ is a projection if and only if $PQ=QP$. If $PQ$ is a projection, then $\operatorname{ran}PQ=\operatorname{ran}P\cap\operatorname{ran}Q$ and $\ker PQ=\ker P+\ker Q$.

5. Generalize Exercise 4 as follows. Suppose $\{\mathcal M_i:i\in I\}$ is a collection of subspaces of $\mathcal H$ such that $\mathcal M_i\perp\mathcal M_j$ if $i\ne j$. Let $P_i$ be the projection of $\mathcal H$ onto $\mathcal M_i$ and show that for all $h$ in $\mathcal H$, $\sum\{P_i h:i\in I\}$ converges to $Ph$, where $P$ is the projection of $\mathcal H$ onto $\bigvee\{\mathcal M_i:i\in I\}$.

6. If $P$ and $Q$ are projections, then the following statements are equivalent. (a) $P-Q$ is a projection. (b) $\operatorname{ran}Q\subseteq\operatorname{ran}P$. (c) $PQ=Q$. (d) $QP=Q$. If $P-Q$ is a projection, then $\operatorname{ran}(P-Q)=(\operatorname{ran}P)\ominus(\operatorname{ran}Q)$ and $\ker(P-Q)=\operatorname{ran}Q+\ker P$.

7. Let $P$ and $Q$ be projections. Show that $PQ=QP$ if and only if $P+Q-PQ$ is a projection. If this is the case, then $\operatorname{ran}(P+Q-PQ)=\operatorname{ran}P+\operatorname{ran}Q$ and $\ker(P+Q-PQ)=\ker P\cap\ker Q$.

8. Give an example of two noncommuting projections.

9. Let $A\in\mathcal B(\mathcal H)$ and let $\mathcal N=\operatorname{graph}A\subseteq\mathcal H\oplus\mathcal H$. That is, $\mathcal N=\{h\oplus Ah:h\in\mathcal H\}$. Because $A$ is continuous and linear, $\mathcal N\leq\mathcal H\oplus\mathcal H$. Let $\mathcal M=\mathcal H\oplus(0)\leq\mathcal H\oplus\mathcal H$. Prove the following statements. (a) $\mathcal M\cap\mathcal N=(0)$ if and only if $\ker A=(0)$. (b) $\mathcal M+\mathcal N$ is dense in $\mathcal H\oplus\mathcal H$ if and only if $\operatorname{ran}A$ is dense in $\mathcal H$. (c) $\mathcal M+\mathcal N=\mathcal H\oplus\mathcal H$ if and only if $A$ is surjective.

10. Find two closed linear subspaces $\mathcal M,\mathcal N$ of an infinite dimensional Hilbert space $\mathcal H$ such that $\mathcal M\cap\mathcal N=(0)$ and $\mathcal M+\mathcal N$ is dense in $\mathcal H$, but $\mathcal M+\mathcal N\ne\mathcal H$.

11. Define $A:\ell^2(\mathbb Z)\to\ell^2(\mathbb Z)$ by $A(\ldots,\alpha_{-1},\hat\alpha_0,\alpha_1,\ldots)=(\ldots,\hat\alpha_{-1},\alpha_0,\alpha_1,\ldots)$, where $\hat{\ }$ sits above the coefficient in the 0-place. Find an invariant subspace of $A$ that does not reduce $A$. This operator is called the *bilateral shift*.

12. Let $\mu=\mathrm{Area}$ measure on $\mathbb D\equiv\{z\in\mathbb C:|z|<1\}$ and define $A:L^2(\mu)\to L^2(\mu)$ by $(Af)(z)=zf(z)$ for $|z|<1$ and $f$ in $L^2(\mu)$. Find a nontrivial reducing subspace for $A$ and an invariant subspace that does not reduce $A$.



<a id="pdf-page-56"></a>
# §4. Compact Operators

<!-- BEGIN BACKGROUND BG-II.block2 -->
<a id="bg-ii-6"></a>
### Definition BG-II.6. Compactness versus boundedness

A space is **compact** if every open cover has a finite subcover. A metric subset is **totally bounded** if for each $\varepsilon>0$ finitely many balls of radius $\varepsilon$ cover it. It is **relatively compact** if its closure is compact. Boundedness requires only one ball of some finite radius and is much weaker than total boundedness.

<a id="bg-ii-7"></a>
### Theorem BG-II.7. Metric compactness criteria

A metric space is compact exactly when it is complete and totally bounded, equivalently when every sequence has a convergent subsequence. In a complete ambient space, a subset is relatively compact exactly when it is totally bounded.

**Proof.** Compactness gives finite epsilon-ball covers. Every sequence in a compact space has a cluster point: otherwise each point has a neighborhood containing only finitely many terms, and a finite subcover contradicts infinitely many indices. Balls of radii $1/n$ at a cluster point select a convergent subsequence. A Cauchy sequence with a convergent subsequence converges, so compactness also implies completeness.

Conversely, finite covers by balls of radii $2^{-k}$ allow successive infinite subsequences lying in single such balls; the diagonal subsequence is Cauchy and hence converges in a complete space. To pass from this sequential property to the open-cover property, first observe that it implies total boundedness, since failure gives an infinite epsilon-separated sequence. Any open cover then has a Lebesgue number: if no $\delta>0$ made every ball of radius $\delta$ lie in a member, select $x_n$ whose radius-$1/n$ ball does not; a convergent subsequence tends to a point in an open member, a contradiction. A finite cover by sufficiently small balls now yields a finite subcover from the original cover. Finally the closure of a totally bounded set remains totally bounded (enlarge the radii), and it is complete when the ambient space is complete. $\square$

<a id="bg-ii-8"></a>
### Corollary BG-II.8. The sequential test for compact operators

A bounded linear $T:H\to K$ is compact exactly when every bounded sequence $(x_n)$ has a subsequence for which $(Tx_n)$ converges. A compact metric set is separable, whereas the unit ball of an infinite-dimensional Hilbert space is not compact.

**Proof.** Rescale a bounded sequence into the unit ball and apply Theorem BG-II.7 to its compact image closure. Conversely, for any sequence in the image closure choose image points within $1/n$; the assumed test supplies a convergent subsequence and the same is true of the original sequence. For separability take the union of finite $1/n$-nets. In an infinite-dimensional Hilbert space recursively choose orthogonal unit vectors; their pairwise distance $\sqrt2$ prevents a convergent subsequence. $\square$

<a id="bg-ii-9"></a>
### Lemma BG-II.9. Uniformity on a compact set

Suppose bounded operators $S_n:X\to Y$ satisfy $\sup_n\|S_n\|\leq M$ and $S_nx\to0$ for each $x$. Then $\sup_{x\in C}\|S_nx\|\to0$ for each compact $C\subset X$.

**Proof.** If $M=0$ there is nothing to prove. Otherwise choose a finite $\varepsilon/(2M)$-net $x_1,\ldots,x_r$ for $C$. For large enough $n$, all $\|S_nx_j\|<\varepsilon/2$ simultaneously. For $x$ near $x_j$, $\|S_nx\|\leq M\|x-x_j\|+\|S_nx_j\|<\varepsilon$. This is the finite-net argument used in Theorem 4.4, with $S_n=I-P_n$ on the closure of the range. Pointwise convergence on the whole unit ball is not enough: the coordinate projections $P_n$ on $\ell^2$ satisfy $P_nx\to x$ but $\|I-P_n\|=1$. $\square$
<!-- END BACKGROUND BG-II.block2 -->

It turns out that most of the statements about linear transformations on finite dimensional spaces have nice generalizations to a certain class of operators on infinite dimensional spaces—namely, to the compact operators. Let ball $\mathcal H$ denote the closed unit ball in $\mathcal H$.

**4.1. Definition.** A linear transformation $T:\mathcal H\to\mathcal K$ is *compact* if $T(\text{ball }\mathcal H)$ has compact closure in $\mathcal K$. The set of compact operators from $\mathcal H$ into $\mathcal K$ is denoted by $\mathcal B_0(\mathcal H,\mathcal K)$, and $\mathcal B_0(\mathcal H)=\mathcal B_0(\mathcal H,\mathcal H)$.

**4.2. Proposition.**  
(a) $\mathcal B_0(\mathcal H,\mathcal K)\subseteq\mathcal B(\mathcal H,\mathcal K)$.

(b) $\mathcal B_0(\mathcal H,\mathcal K)$ is a linear space and if $\{T_n\}\subseteq\mathcal B_0(\mathcal H,\mathcal K)$ and $T\in\mathcal B(\mathcal H,\mathcal K)$ such that $\|T_n-T\|\to0$, then $T\in\mathcal B_0(\mathcal H,\mathcal K)$.

(c) If $A\in\mathcal B(\mathcal H)$, $B\in\mathcal B(\mathcal K)$, and $T\in\mathcal B_0(\mathcal H,\mathcal K)$, then $TA$ and $BT\in\mathcal B_0(\mathcal H,\mathcal K)$.

**Proof.** (a) If $T\in\mathcal B_0(\mathcal H,\mathcal K)$, then $\operatorname{cl}[T(\text{ball }\mathcal H)]$ is compact in $\mathcal K$. Hence there is a constant $C>0$ such that $T(\text{ball }\mathcal H)\subseteq\{k\in\mathcal K:\|k\|\leq C\}$. Thus $\|T\|\leq C$.

(b) It is left to the reader to show that $\mathcal B_0(\mathcal H,\mathcal K)$ is a linear space. For the second part of (b), it will be shown that $T(\text{ball }\mathcal H)$ is totally bounded. Since $\mathcal K$ is a complete metric space, this is equivalent to showing that $T(\text{ball }\mathcal H)$ has compact closure. Let $\varepsilon>0$ and choose $n$ such that $\|T-T_n\|<\varepsilon/3$. Since $T_n$ is compact, there are vectors $h_1,\ldots,h_m$ in ball $\mathcal H$ such that $T_n(\text{ball }\mathcal H)\subseteq\bigcup_{j=1}^{m}B(T_nh_j;\varepsilon/3)$. So if $\|h\|\leq1$, there is an $h_j$ with $\|T_nh_j-T_nh\|<\varepsilon/3$. Thus

$$
\begin{aligned}
\|Th_j-Th\|
&\leq \|Th_j-T_nh_j\|+\|T_nh_j-T_nh\|+\|T_nh-Th\|\\
&<2\|T-T_n\|+\varepsilon/3\\
&<\varepsilon.
\end{aligned}
$$

Hence $T(\text{ball }\mathcal H)\subseteq\bigcup_{j=1}^{m}B(Th_j;\varepsilon)$.

The proof of (c) is left to the reader. $\blacksquare$

**4.3. Definition.** An operator $T$ on $\mathcal H$ has *finite rank* if $\operatorname{ran}T$ is finite dimensional. The set of continuous finite rank operators is denoted by $\mathcal B_{00}(\mathcal H,\mathcal K)$; $\mathcal B_{00}(\mathcal H)=\mathcal B_{00}(\mathcal H,\mathcal H)$.

It is easy to see that $\mathcal B_{00}(\mathcal H,\mathcal K)$ is a linear space and $\mathcal B_{00}(\mathcal H,\mathcal K)\subseteq\mathcal B_0(\mathcal H,\mathcal K)$ (Exercise 2). Before giving other examples of compact operators, however, the next result should be proved.

**4.4. Theorem.** If $T\in\mathcal B(\mathcal H,\mathcal K)$, the following statements are equivalent.

(a) $T$ is compact.

(b) $T^*$ is compact.

(c) There is a sequence $\{T_n\}$ of operators of finite rank such that $\|T-T_n\|\to0$.



<a id="pdf-page-57"></a>
**Proof.** (c) $\Rightarrow$ (a): This is immediate from (4.2b) and the fact that $\mathcal B_{00}(\mathcal H,\mathcal K)\subseteq\mathcal B_0(\mathcal H,\mathcal K)$.

(a) $\Rightarrow$ (c): Since $\operatorname{cl}[T(\operatorname{ball}\mathcal H)]$ is compact, it is separable. Therefore $\operatorname{cl}(\operatorname{ran}T)=\mathcal L$ is a separable subspace of $\mathcal K$. Let $\{e_1,e_2,\ldots\}$ be a basis for $\mathcal L$ and let $P_n$ be the orthogonal projection of $\mathcal K$ onto $\bigvee\{e_j:1\leq j\leq n\}$. Put $T_n=P_nT$; note that each $T_n$ has finite rank. It will be shown that $\|T_n-T\|\to0$, but first we prove the following:

**Claim.** If $h\in\mathcal H$, $\|T_nh-Th\|\to0$.

In fact, $k=Th\in\mathcal L$, so $\|P_nk-k\|\to0$ by (I.4.13d) and (I.4.7). That is, $\|P_nTh-Th\|\to0$ and the claim is proved.

Since $T$ is compact, if $\varepsilon>0$, there are vectors $h_1,\ldots,h_m$ in $\operatorname{ball}\mathcal H$ such that $T(\operatorname{ball}\mathcal H)\subseteq\bigcup_{j=1}^m B(Th_j;\varepsilon/3)$. So if $\|h\|\leq1$, choose $h_j$ with $\|Th-Th_j\|<\varepsilon/3$. Thus for any integer $n$,

$$
\begin{aligned}
\|Th-T_nh\|
&\leq \|Th-Th_j\|+\|Th_j-T_nh_j\|+\|P_n(Th_j-Th)\|\\
&\leq 2\|Th-Th_j\|+\|Th_j-T_nh_j\|\\
&\leq 2\varepsilon/3+\|Th_j-T_nh_j\|.
\end{aligned}
$$

Using the claim we can find an integer $n_0$ such that $\|Th_j-T_nh_j\|<\varepsilon/3$ for $1\leq j\leq m$ and $n\geq n_0$. So $\|Th-T_nh\|<\varepsilon$ uniformly for $h$ in $\operatorname{ball}\mathcal H$. Therefore $\|T-T_n\|<\varepsilon$ for $n\geq n_0$.

(c) $\Rightarrow$ (b): If $\{T_n\}$ is a sequence in $\mathcal B_{00}(\mathcal H,\mathcal K)$ such that $\|T_n-T\|\to0$, then $\|T_n^*-T^*\|=\|T_n-T\|\to0$. But $T_n^*\in\mathcal B_{00}(\mathcal H,\mathcal K)$ (Exercise 3). Since (c) implies (a), $T^*$ is compact.

(b) $\Rightarrow$ (a): Exercise. $\blacksquare$

A fact emerged in the proof that (a) implies (c) in the preceding theorem that is worth recording.

**4.5. Corollary.** *If $T\in\mathcal B_0(\mathcal H,\mathcal K)$, then $\operatorname{cl}(\operatorname{ran}T)$ is separable and if $\{e_n\}$ is a basis for $\operatorname{cl}(\operatorname{ran}T)$ and $P_n$ is the projection of $\mathcal K$ onto $\bigvee\{e_j:1\leq j\leq n\}$, then $\|P_nT-T\|\to0$.*

**4.6. Proposition.** *Let $\mathcal H$ be a separable Hilbert space with basis $\{e_n\}$; let $\{\alpha_n\}\subseteq\mathbb F$ with $M=\sup\{|\alpha_n|:n\geq1\}<\infty$. If $Ae_n=\alpha_ne_n$ for all $n$, then $A$ extends by linearity to a bounded operator on $\mathcal H$ with $\|A\|=M$. The operator $A$ is compact if and only if $\alpha_n\to0$ as $n\to\infty$.*

**Proof.** The fact that $A$ is bounded and $\|A\|=M$ is an exercise; such an operator is said to be diagonalizable (see Exercise 1.8). Let $P_n$ be the projection of $\mathcal H$ onto $\bigvee\{e_1,\ldots,e_n\}$. Then $A_n=A-AP_n$ is seen to be diagonalizable with $A_ne_j=\alpha_je_j$ if $j>n$ and $A_ne_j=0$ if $j\leq n$. So $AP_n\in\mathcal B_{00}(\mathcal H)$ and $\|A_n\|=\sup\{|\alpha_j|:j>n\}$. If $\alpha_n\to0$, then $\|A_n\|\to0$ and so $A$ is compact since


<a id="pdf-page-58"></a>
it is the limit of a sequence of finite-rank operators. Conversely, if $A$ is compact, then Corollary 4.5 implies $\|A_n\|\to 0$; hence $\alpha_n\to 0$. $\blacksquare$

**4.7. Proposition.** *If $(X,\Omega,\mu)$ is a measure space and $k\in L^2(X\times X,\Omega\times\Omega,\mu\times\mu)$, then*

$$
(Kf)(x)=\int k(x,y)f(y)\,d\mu(y)
$$

*is a compact operator and $\|K\|\leq\|k\|_2$.*

The following lemma is useful for proving this proposition. The proof is left to the reader.

**4.8. Lemma.** *If $\{e_i:i\in I\}$ is a basis for $L^2(X,\Omega,\mu)$ and*

$$
\phi_{ij}(x,y)=e_j(x)\overline{e_i(y)}
$$

*for $i,j$ in $I$ and $x,y$ in $X$, then $\{\phi_{ij}:i,j\in I\}$ is an orthonormal set in $L^2(X\times X,\Omega\times\Omega,\mu\times\mu)$. If $k$ and $K$ are as in the preceding proposition, then $\langle k,\phi_{ij}\rangle=\langle Ke_j,e_i\rangle$.*

**Proof of Proposition 4.7.** First we show that $K$ defines a bounded operator. In fact, if $f\in L^2(\mu)$,
$$
\begin{aligned}
\|Kf\|^2
&=\int\left|\int k(x,y)f(y)\,d\mu(y)\right|^2d\mu(x)\\
&\leq\int\left(\int|k(x,y)|^2\,d\mu(y)\right)
\left(\int|f(y)|^2\,d\mu(y)\right)d\mu(x)
=\|k\|^2\|f\|^2.
\end{aligned}
$$
Hence $K$ is bounded and $\|K\|\leq\|k\|_2$.

Now let $\{e_i\}$ be a basis for $L^2(\mu)$ and define $\phi_{ij}$ as in Lemma 4.8. Thus
$$
\|k\|^2\geq\sum_{i,j}|\langle k,\phi_{ij}\rangle|^2
=\sum_{i,j}|\langle Ke_j,e_i\rangle|^2.
$$

Since $k\in L^2(\mu\times\mu)$, there are at most a countable number of $i$ and $j$ such that $\langle k,\phi_{ij}\rangle\ne 0$; denote these by $\{\psi_{km}:1\leq k,m<\infty\}$. Note that $\langle Ke_j,e_i\rangle=0$ unless $\phi_{ij}\in\{\psi_{km}\}$. Let $\psi_{km}(x,y)=e_k(x)\overline{e_m(y)}$, let $P_n$ be the orthogonal projection onto $\bigvee\{e_k:1\leq k\leq n\}$, and put $K_n=KP_n+P_nK-P_nKP_n$; so $K_n$ is a finite rank operator. We will show that $\|K-K_n\|\to 0$ as $n\to\infty$, thus showing that $K$ is compact.

Let $f\in L^2(\mu)$ with $\|f\|^2\leq 1$; so $f=\sum_j\alpha_je_j$. Hence
$$
\begin{aligned}
\|Kf-K_nf\|^2
&=\sum_i|\langle Kf-K_nf,e_i\rangle|^2\\
&=\sum_i\left|\sum_j\alpha_j\langle(K-K_n)e_j,e_i\rangle\right|^2\\
&=\sum_k\left|\sum_m\alpha_m\langle(K-K_n)e_m,e_k\rangle\right|^2\\
&\leq\sum_k\left[\sum_m|\alpha_m|^2\right]
\left[\sum_m|\langle(K-K_n)e_m,e_k\rangle|^2\right].
\end{aligned}
$$



<a id="pdf-page-59"></a>
$$
\begin{aligned}
&\leqslant \|f\|^2\sum_k\sum_m\bigl|\langle Ke_m,e_k\rangle-\langle KP_ne_m,P_ne_k\rangle\\
&\qquad-\langle KP_ne_m,P_ne_k\rangle+\langle KP_ne_m,P_ne_k\rangle\bigr|^2\\
&=\sum_{k=n+1}^{\infty}\sum_{m=n+1}^{\infty}|\langle Ke_m,e_k\rangle|^2\\
&=\sum_{k=n+1}^{\infty}\sum_{m=n+1}^{\infty}|\langle k,\psi_{km}\rangle|^2.
\end{aligned}
$$

Since $\sum_{k,m}|\langle k,\psi_{km}\rangle|^2<\infty$, $n$ can be chosen sufficiently large such that for any $\varepsilon>0$ this last sum will be smaller than $\varepsilon^2$. Thus $\|K-K_n\|\to0$. $\blacksquare$

In particular, note that the preceding proposition shows that the Volterra operator (1.7) is compact.

One of the dominant tools in the study of linear transformation on finite dimensional spaces is the concept of eigenvalue.

**4.9. Definition.** If $A\in\mathcal B(\mathcal H)$, a scalar $\alpha$ is an *eigenvalue* of $A$ if $\ker(A-\alpha)\ne(0)$. If $h$ is a nonzero vector in $\ker(A-\alpha)$, $h$ is called an *eigenvector* for $\alpha$; thus $Ah=\alpha h$. Let $\sigma_p(A)$ denote the set of eigenvalues of $A$.

**4.10. Example.** Let $A$ be the diagonalizable operator in Proposition 4.6. Then $\sigma_p(A)=\{\alpha_1,\alpha_2,\ldots\}$. If $\alpha\in\sigma_p(A)$, let $J_\alpha=\{j\in\mathbb N:\alpha_j=\alpha\}$. Then $h$ is an eigenvector for $\alpha$ if and only if $h\in\bigvee\{e_j:j\in J_\alpha\}$.

**4.11. Example.** The Volterra operator has no eigenvalues.

**4.12. Example.** Let $h\in\mathcal H=L_{\mathbb C}^2(-\pi,\pi)$ and define $K:\mathcal H\to\mathcal H$ by $(Kf)(x)=(2\pi)^{-1/2}\int_{-\pi}^{\pi}h(x-y)f(y)\,dy$. If $\lambda_n=(2\pi)^{-1/2}\int_{-\pi}^{\pi}h(x)\exp(-inx)\,dx=\hat h(n)$, the $n$th Fourier coefficient of $h$, then $Ke_n=\lambda_ne_n$, where $e_n(x)=(2\pi)^{-1/2}\exp(-inx)$.

The way to see this is to extend functions in $L_{\mathbb C}^2(-\pi,\pi)$ to $\mathbb R$ by periodicity and perform a change of variables in the formula for $(Ke_n)(x)$. The details are left to the reader.

Operators on finite dimensional spaces over $\mathbb C$ always have eigenvalues. As the Volterra operator illustrates, the analogy between operators on finite dimensional spaces and compact operators breaks down here. If, however, a compact operator has an eigenvalue, several nice things can be said if the eigenvalue is not zero.

**4.13. Proposition.** *If $T\in\mathcal B_0(\mathcal H)$, $\lambda\in\sigma_p(T)$, and $\lambda\ne0$, then the eigenspace $\ker(T-\lambda)$ is finite dimensional.*

**Proof.** Suppose there is an infinite orthonormal sequence $\{e_n\}$ in $\ker(T-\lambda)$. Since $T$ is compact, there is a subsequence $\{e_{n_k}\}$ such that $\{Te_{n_k}\}$ converges.



<a id="pdf-page-60"></a>
Thus, $\{Te_{n_k}\}$ is a Cauchy sequence. But for $n_k\ne n_j$, $\|Te_{n_k}-Te_{n_j}\|^2=\|\lambda e_{n_k}-\lambda e_{n_j}\|^2=2|\lambda|^2>0$ since $\lambda\ne0$. This contradiction shows that $\ker(T-\lambda)$ must be finite dimensional. ■

The next result on the existence of eigenvalues is not a practical way to show that a specific example has a nonzero eigenvalue, but it is a good theoretical tool that will be used later in this book (in particular, in the next section).

**4.14. Proposition.** *If $T$ is a compact operator on $\mathcal H$, $\lambda\ne0$, and $\inf\{\|(T-\lambda)h\|:\|h\|=1\}=0$, then $\lambda\in\sigma_p(T)$.*

**Proof.** By hypothesis, there is a sequence of unit vectors $\{h_n\}$ such that $\|(T-\lambda)h_n\|\to0$. Since $T$ is compact, there is a vector $f$ in $\mathcal H$ and a subsequence $\{h_{n_k}\}$ such that $\|Th_{n_k}-f\|\to0$. But $h_{n_k}=\lambda^{-1}[(\lambda-T)h_{n_k}+Th_{n_k}]\to\lambda^{-1}f$. So $1=\|\lambda^{-1}f\|=|\lambda|^{-1}\|f\|$ and $f\ne0$. Also, it must be that $Th_{n_k}\to\lambda^{-1}Tf$. Since $Th_{n_k}\to f$, $f=\lambda^{-1}Tf$, or $Tf=\lambda f$. That is, $f\in\ker(T-\lambda)$ and $f\ne0$, so $\lambda\in\sigma_p(T)$. ■

**4.15. Corollary.** *If $T$ is a compact operator on $\mathcal H$, $\lambda\ne0$, $\lambda\notin\sigma_p(T)$, and $\bar\lambda\notin\sigma_p(T^*)$, then $\operatorname{ran}(T-\lambda)=\mathcal H$ and $(T-\lambda)^{-1}$ is a bounded operator on $\mathcal H$.*

**Proof.** Since $\lambda\notin\sigma_p(T)$, the preceding proposition implies that there is a constant $c>0$ such that $\|(T-\lambda)h\|\ge c\|h\|$ for all $h$ in $\mathcal H$. If $f\in\operatorname{cl}\operatorname{ran}(T-\lambda)$, then there is a sequence $\{h_n\}$ in $\mathcal H$ such that $(T-\lambda)h_n\to f$. Thus $\|h_n-h_m\|\le c^{-1}\|(T-\lambda)h_n-(T-\lambda)h_m\|$ and so $\{h_n\}$ is a Cauchy sequence. Hence $h_n\to h$ for some $h$ in $\mathcal H$. Thus $(T-\lambda)h=f$. So $\operatorname{ran}(T-\lambda)$ is closed and, by (2.19), $\operatorname{ran}(T-\lambda)=[\ker(T-\lambda)^*]^\perp=\mathcal H$, by hypothesis.

So for $f$ in $\mathcal H$ let $Af=$ the unique vector $h$ such that $(T-\lambda)h=f$. Thus $(T-\lambda)Af=f$ for all $f$ in $\mathcal H$. From the inequality above, $c\|Af\|\le\|(T-\lambda)Af\|=\|f\|$. So $\|Af\|\le c^{-1}\|f\|$ and $A$ is bounded. Also, $(T-\lambda)A(T-\lambda)h=(T-\lambda)h$, so $0=(T-\lambda)[A(T-\lambda)h-h]$. Since $\lambda\notin\sigma_p(T)$, $A(T-\lambda)h=h$. That is, $A=(T-\lambda)^{-1}$. ■

It will be proved in a later chapter that if $\lambda\notin\sigma_p(T)$ and $\lambda\ne0$, then $\bar\lambda\notin\sigma_p(T^*)$. More will be shown about arbitrary compact operators in Chapter VI. In the next section the theory of compact self-adjoint operators will be explored.

## Exercises

1. Prove Proposition 4.2(c).

2. Show that every operator of finite rank is compact.

3. If $T\in\mathcal B_{00}(\mathcal H,\mathcal K)$, show that $T^*\in\mathcal B_{00}(\mathcal K,\mathcal H)$ and $\dim(\operatorname{ran}T)=\dim(\operatorname{ran}T^*)$.

4. Show that an idempotent is compact if and only if it has finite rank.


   <a id="pdf-page-61"></a>
5. Show that no nonzero multiplication operator on $L^2(0,1)$ is compact.

6. Show that if $T:\mathcal H\to\mathcal H$ is a compact operator and $\{e_n\}$ is any orthonormal sequence in $\mathcal H$, then $\|Te_n\|\to 0$. Is the converse true?

7. If $T$ is compact and $\mathcal M$ is an invariant subspace for $T$, show that $T|_{\mathcal M}$ is compact.

8. If $h,g\in\mathcal H$, define $T:\mathcal H\to\mathcal H$ by $Tf=\langle f,h\rangle g$. Show that $T$ has rank 1 [that is, $\dim(\operatorname{ran}T)=1$]. Moreover, every rank 1 operator can be so represented. Show that if $T$ is a finite rank operator, then there are orthonormal vectors $e_1,\ldots,e_n$ and vectors $g_1,\ldots,g_n$ such that $Th=\sum_{j=1}^{n}\langle h,e_j\rangle g_j$ for all $h$ in $\mathcal H$. In this case show that $T$ is normal if $g_j=\lambda_j e_j$ for some scalars $\lambda_1,\ldots,\lambda_n$. Find $\sigma_p(T)$.

9. Show that a diagonalizable operator is normal.

10. Verify the statements in Example 4.10.

11. Verify the statement in Example 4.11.

12. Verify the statement in Example 4.12. (Note that the operator $K$ in this example is diagonalizable.)

13. If $T_n\in\mathcal B(\mathcal H_n)$, $n\geq 1$, with $\sup_n\|T_n\|<\infty$ and $T=\bigoplus_{n=1}^{\infty}T_n$ on $\mathcal H=\bigoplus_{n=1}^{\infty}\mathcal H_n$, show that $T$ is compact if and only if each $T_n$ is compact and $\|T_n\|\to 0$.

14. In Lemma 4.8, show that if $L^2(X,\Omega,\mu)$ is separable, then $\{\varphi_{ij}\}$ is a basis for $L^2(X\times X,\Omega\times\Omega,\mu\times\mu)$. What if $L^2(X,\Omega,\mu)$ is not separable?

## §5*. The Diagonalization of Compact Self-Adjoint Operators

This section and the remaining ones in this chapter may be omitted if the reader intends to continue through to the end of this book, as the material in these sections (save for Section 6) will be obtained in greater generality in Chapter IX. It is worthwhile, however, to examine this material even if Chapter IX is to be read, since the intuition provided by this special case is valuable.

The main result of this section is the following.

**5.1. Theorem.** *If $T$ is a compact self-adjoint operator on $\mathcal H$, then $T$ has only a countable number of distinct eigenvalues. If $\{\lambda_1,\lambda_2,\ldots\}$ are the distinct nonzero eigenvalues of $T$, and $P_n$ is the projection of $\mathcal H$ onto $\ker(T-\lambda_n)$, then $P_nP_m=P_mP_n=0$ if $n\neq m$, each $\lambda_n$ is real, and*

$$
T=\sum_{n=1}^{\infty}\lambda_nP_n, \tag*{5.2}
$$

*where the series converges to $T$ in the metric defined by the norm of $\mathcal B(\mathcal H)$. [Of course, (5.2) may be only a finite sum.]*


<a id="pdf-page-62"></a>
The proof of Theorem 5.1 requires a few preliminary results. Before beginning this process, let’s look at a few consequences.

**5.3. Corollary.** *With the notation of (5.1):*

(a) $\ker T=\left[\bigvee\{P_n\mathcal H:n\geqslant1\}\right]^\perp=(\operatorname{ran}T)^\perp$;

(b) *each $P_n$ has finite rank;*

(c) $\|T\|=\sup\{|\lambda_n|:n\geqslant1\}$ *and* $\lambda_n\to0$ *as* $n\to\infty$.

**Proof.** Since $P_n\perp P_m$ for $n\ne m$, if $h\in\mathcal H$, then (5.2) implies $\|Th\|^2=\sum_{n=1}^{\infty}\|\lambda_nP_nh\|^2=\sum_{n=1}^{\infty}|\lambda_n|^2\|P_nh\|^2$. Hence $Th=0$ if and only if $P_nh=0$ for all $n$. That is, $h\in\ker T$ if and only if $h\perp P_n\mathcal H$ for all $n$, whence (a).

Part (b) follows by Proposition 4.13.

For part (c), if $\mathcal L=\operatorname{cl}[\operatorname{ran}T]$, $\mathcal L$ is invariant for $T$. Since $T=T^*$, $\mathcal L=(\ker T)^\perp$ and $\mathcal L$ reduces $T$. So we can consider the restriction of $T$ to $\mathcal L$, $T|_{\mathcal L}$. Now $\mathcal L=\bigvee\{P_n\mathcal H:n\geqslant1\}$ by (a). Let $\{e_j^{(n)}:1\leqslant j\leqslant N_n\}$ be a basis for $P_n\mathcal H=\ker(T-\lambda_n)$, so $Te_j^{(n)}=\lambda_ne_j^{(n)}$ for $1\leqslant j\leqslant N_n$. Thus $\{e_j^{(n)}:1\leqslant j\leqslant N_n,\ n\geqslant1\}$ is a basis for $\mathcal L$ and $T|_{\mathcal L}$ is diagonalizable with respect to this basis. Part (c) now follows by (4.6). ■

The proof of (c) in the preceding corollary revealed an interesting fact that deserves a statement of its own.

**5.4. Corollary.** *If $T$ is a compact self-adjoint operator, then there is a sequence $\{\mu_n\}$ of real numbers and an orthonormal basis $\{e_n\}$ for $(\ker T)^\perp$ such that for all $h$,*

$$
Th=\sum_{n=1}^{\infty}\mu_n\langle h,e_n\rangle e_n.
$$

Note that there may be repetitions in the sequence $\{\mu_n\}$ in (5.4). How many repetitions?

**5.5. Corollary.** *If $T\in\mathcal B_0(\mathcal H)$, $T=T^*$, and $\ker T=(0)$, then $\mathcal H$ is separable.*

Also note that by (4.6), if (5.2) holds, $T\in\mathcal B_0(\mathcal H)$.

To begin the proof of Theorem 5.1, we prove a few results about not necessarily compact operators.

**5.6. Proposition.** *If $A$ is a normal operator and $\lambda\in\mathbb F$, then $\ker(A-\lambda)=\ker(A-\lambda)^*$ and $\ker(A-\lambda)$ is a reducing subspace for $A$.*

**Proof.** Since $A$ is normal, so is $A-\lambda$. Hence $\|(A-\lambda)h\|=\|(A-\lambda)^*h\|$ (2.16). Thus $\ker(A-\lambda)=\ker(A-\lambda)^*$. If $h\in\ker(A-\lambda)$, $Ah=\lambda h\in\ker(A-\lambda)$. Also $A^*h=\bar\lambda h\in\ker(A-\lambda)$. Therefore $\ker(A-\lambda)$ reduces $A$. ■

**5.7. Proposition.** *If $A$ is a normal operator and $\lambda,\mu$ are distinct eigenvalues of $A$, then $\ker(A-\lambda)\perp\ker(A-\mu)$.*



<a id="pdf-page-63"></a>
**Proof.** If $h\in\ker(A-\lambda)$ and $g\in\ker(A-\mu)$, then the fact (5.6) that $A^*g=\bar\mu g$ implies that
$$
\lambda\langle h,g\rangle=\langle Ah,g\rangle=\langle h,A^*g\rangle
=\langle h,\bar\mu g\rangle=\mu\langle h,g\rangle.
$$
Thus $(\lambda-\mu)\langle h,g\rangle=0$. Since $\lambda-\mu\ne0$, $h\perp g$. ■

**5.8. Proposition.** *If $A=A^*$ and $\lambda\in\sigma_p(A)$, then $\lambda$ is a real number.*

**Proof.** If $Ah=\lambda h$, then $Ah=A^*h=\bar\lambda h$ by (5.6). So $(\lambda-\bar\lambda)h=0$. Since $h$ can be chosen different from $0$, $\lambda=\bar\lambda$. ■

The main result prior to entering the proof of Theorem 5.1 is to show that a compact self-adjoint operator has nonzero eigenvalues. If (5.3c) is examined, we see that there is a $\lambda_n$ in $\sigma_p(T)$ with $|\lambda_n|=\|T\|$. Since the preceding proposition says that $\lambda_n\in\mathbb R$, it must be that $\lambda_n=\pm\|T\|$. That is, either $\pm\|T\|\in\sigma_p(T)$. This is the key to showing that $\sigma_p(T)$ is nonvoid.

**5.9. Lemma.** *If $T$ is a compact self-adjoint operator, then either $\pm\|T\|$ is an eigenvalue of $T$.*

**Proof.** If $T=0$, the result is clear. So suppose $T\ne0$. By Proposition 2.13 there is a sequence $\{h_n\}$ of unit vectors such that $|\langle Th_n,h_n\rangle|\to\|T\|$. By passing to a subsequence if necessary, we may assume that $\langle Th_n,h_n\rangle\to\lambda$, where $|\lambda|=\|T\|$. It will be shown that $\lambda\in\sigma_p(T)$. Since $|\lambda|=\|T\|$,
$$
0\le\|(T-\lambda)h_n\|^2
=\|Th_n\|^2-2\lambda\langle Th_n,h_n\rangle+\lambda^2
\le 2\lambda^2-2\lambda\langle Th_n,h_n\rangle\to0.
$$
Hence $\|(T-\lambda)h_n\|\to0$. By (4.14), $\lambda\in\sigma_p(T)$. ■

**Proof of Theorem 5.1.** By Lemma 5.9 there is a real number $\lambda_1$ in $\sigma_p(T)$ with $|\lambda_1|=\|T\|$. Let $\mathcal E_1=\ker(T-\lambda_1)$, $P_1=$ the projection onto $\mathcal E_1$, $\mathcal H_2=\mathcal E_1^\perp$. By (5.6) $\mathcal E_1$ reduces $T$, so $\mathcal H_2$ reduces $T$. Let $T_2=T|_{\mathcal H_2}$; then $T_2$ is a self-adjoint compact operator on $\mathcal H_2$. (Why?)

By (5.9) there is an eigenvalue $\lambda_2$ for $T_2$ such that $|\lambda_2|=\|T_2\|$. Let $\mathcal E_2=\ker(T_2-\lambda_2)$. Note that $(0)\ne\mathcal E_2\subseteq\ker(T-\lambda_2)$. If it were the case that $\lambda_1=\lambda_2$, then $\mathcal E_2\subseteq\ker(T-\lambda_1)=\mathcal E_1$. Since $\mathcal E_1\perp\mathcal E_2$, it must be that $\lambda_1\ne\lambda_2$. Let $P_2=$ the projection of $\mathcal H$ onto $\mathcal E_2$ and put $\mathcal H_3=(\mathcal E_1\oplus\mathcal E_2)^\perp$. Note that $\|T_2\|\le\|T\|$ so that $|\lambda_2|\le|\lambda_1|$.

Using induction (give the details) we obtain a sequence $\{\lambda_n\}$ of real eigenvalues of $T$ such that

(i) $|\lambda_1|\ge|\lambda_2|\ge\cdots$;

(ii) If $\mathcal E_n=\ker(T-\lambda_n)$, $|\lambda_{n+1}|=\|T|_{(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp}\|$.

By (i) there is a nonnegative number $\alpha$ such that $|\lambda_n|\to\alpha$.

**Claim.** $\alpha=0$; that is, $\lim\lambda_n=0$.

In fact, let $e_n\in\mathcal E_n$, $\|e_n\|=1$. Since $T$ is compact, there is an $h$ in $\mathcal H$ and a subsequence $\{e_{n_j}\}$ such that $\|Te_{n_j}-h\|\to0$. But $e_n\perp e_m$ for $n\ne m$ and $Te_{n_j}=\lambda_{n_j}e_{n_j}$. Hence $\|Te_{n_j}-Te_{n_i}\|^2=\lambda_{n_j}^2+\lambda_{n_i}^2\ge2\alpha^2$. Since $\{Te_{n_j}\}$ is a Cauchy sequence, $\alpha=0$.



<a id="pdf-page-64"></a>
Now put $P_n=$ the projection of $\mathcal H$ onto $\mathcal E_n$ and examine $T-\sum_{j=1}^{n}\lambda_jP_j$. If $h\in\mathcal E_k$, $1\leq k\leq n$, then $(T-\sum_{j=1}^{n}\lambda_jP_j)h=Th-\lambda_kh=0$. Hence $\mathcal E_1\oplus\cdots\oplus\mathcal E_n\subseteq\ker(T-\sum_{j=1}^{n}\lambda_jP_j)$. If $h\in(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp$, then $P_jh=0$ for $1\leq j\leq n$; so $(T-\sum_{j=1}^{n}\lambda_jP_j)h=Th$. These two statements, together with the fact that $(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp$ reduces $T$, imply that
$$
\begin{aligned}
\left\|T-\sum_{j=1}^{n}\lambda_jP_j\right\|
&=\left\|T|(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp\right\|\\
&=|\lambda_{n+1}|\to0.
\end{aligned}
$$
Therefore the series $\sum_{n=1}^{\infty}\lambda_nP_n$ converges in the metric of $\mathcal B(\mathcal H)$ to $T$. ■

Theorem 5.1 is called the *Spectral Theorem* for compact self-adjoint operators. Using it, one can answer virtually every question about compact hermitian operators, as will be seen before the end of this chapter.

If in Theorem 5.1 it is assumed that $T$ is normal and compact, then the same conclusion, except for the statement that each $\lambda_n$ is real, is true provided that $\mathcal H$ is a $\mathbb C$-Hilbert space. The proof of this will be given in Section 7.

## EXERCISES

1. Prove Corollary 5.4.

2. Prove Corollary 5.5.

3. Let $K$ and $k$ be as in Proposition 4.7 and suppose that $k(x,y)=\overline{k(y,x)}$. Show that $K$ is self-adjoint and if $\{\mu_n\}$ are the eigenvalues of $K$, each repeated $\dim\ker(K-\mu_n)$ times, then $\sum_{1}^{\infty}|\mu_n|^2<\infty$.

4. If $T$ is a compact self-adjoint operator and $\{e_n\}$ and $\{\mu_n\}$ are as in (5.4) and if $h$ is a given vector in $\mathcal H$, show that there is a vector $f$ in $\mathcal H$ such that $Tf=h$ if and only if $h\perp\ker T$ and $\sum_n\mu_n^{-2}|\langle h,e_n\rangle|^2<\infty$. Find the form of the general vector $f$ such that $Tf=h$.

5. Let $T$, $\{\mu_n\}$, and $\{e_n\}$ be as in (5.4). If $\lambda\neq0$ and $\lambda\neq\mu_n$ for any $\mu_n$, then for every $h$ in $\mathcal H$ there is a unique $f$ in $\mathcal H$ such that $(\lambda-T)f=h$. Moreover, $f=\lambda^{-1}[h+\sum_{n=1}^{\infty}\lambda_n(\lambda-\lambda_n)^{-1}\langle h,e_n\rangle e_n]$. Interpret this when $T$ is an integral operator.

## §6*. An Application: Sturm–Liouville Systems

<!-- BEGIN BACKGROUND BG-II.block3 -->
<a id="bg-ii-10"></a>
### Theorem BG-II.10. The initial-value theorem needed below

If $q$ is continuous on $[a,b]$, then for prescribed $h(t_0)=u$, $h'(t_0)=v$ there is exactly one $C^2$ solution of $h''=qh$ on $[a,b]$. The solution depends linearly on $(u,v)$; in particular the solution space is two-dimensional.

**Proof.** Write $Y=(h,h')$ and $Y'=A(t)Y$, where $A(t)=\begin{bmatrix}0&1\\q(t)&0\end{bmatrix}$. On an interval of length $\delta$ starting at $t_0$, the map

$$
(\Phi Y)(t)=(u,v)+\int_{t_0}^t A(s)Y(s)\,ds
$$

on continuous vector functions satisfies $\|\Phi Y-\Phi Z\|_\infty\leq\delta\sup\|A\|\,\|Y-Z\|_\infty$. Choose $\delta$ so this constant is less than one. Iteration converges: successive differences are bounded by a geometric series, completeness gives a limit, and continuity of $\Phi$ makes it a fixed point. The same estimate shows two fixed points coincide. The integral equation gives $Y\in C^1$ and hence $h\in C^2$. Finitely many such intervals extend the solution to both endpoints; uniqueness on overlaps makes the extensions agree. Sums and scalar multiples solve the corresponding initial-value problems, so uniqueness gives linear dependence on initial data. Evaluation $(h(t_0),h'(t_0))$ is therefore a linear bijection from the solution space to $\mathbb F^2$. $\square$

<a id="bg-ii-11"></a>
### Corollary BG-II.11. Boundary conditions and the Wronskian

For real $q$, the solution with $(h_a(a),h_a'(a))=(\alpha_1,-\alpha)$ is real, nonzero and satisfies the left boundary condition. The corresponding choice $(\beta_1,-\beta)$ at $b$ gives $h_b$. For any two solutions of $h''=qh$, $W=h_ah_b'-h_a'h_b$ is constant and vanishes exactly when they are dependent.

**Proof.** The initial vector is nonzero, so uniqueness prevents the identically zero solution; complex conjugation and uniqueness show that real data give real solutions. Differentiation gives $W'=h_ah_b''-h_a''h_b=0$. If $W(t_0)=0$, the two initial vectors are dependent. Their same linear combination is zero initial data, so uniqueness makes that combination identically zero. The converse is immediate. Consequently imposing one nontrivial separated boundary condition leaves a one-dimensional space of solutions, explaining simplicity of the eigenspaces in Lemma 6.11. $\square$

<a id="bg-ii-12"></a>
### Lemma BG-II.12. Differentiating the Green-function formula safely

If $f\in L^2[a,b]$ and $u$ is continuous, then $uf\in L^1$. Its indefinite integral is absolutely continuous. If an absolutely continuous $h$ has $h'=\phi$ a.e. with $\phi$ continuous, then $h$ is $C^1$ and $h'=\phi$ everywhere. For absolutely continuous $u,v$, integration by parts holds whenever the expressions are integrable:

$$
\int_a^b u'v=[uv]_a^b-\int_a^b uv'.
$$

**Proof.** Schwarz and boundedness of $u$ give $\int|uf|\leq\|u\|_\infty\sqrt{b-a}\|f\|_2$. The Lebesgue fundamental theorem recalled in Chapter I gives absolute continuity of its primitive. The same theorem yields $h(x)=h(a)+\int_a^x\phi$, and the ordinary fundamental theorem for continuous $\phi$ gives the everywhere derivative. Products of absolutely continuous functions are absolutely continuous, since they are bounded and $|u(b)v(b)-u(a)v(a)|\leq\|u\|_\infty|v(b)-v(a)|+\|v\|_\infty|u(b)-u(a)|$. Their a.e. derivative is $u'v+uv'$, so integration yields the formula. These observations justify the a.e. differentiations and their upgrade to an everywhere first derivative in Theorem 6.9. $\square$

**Sign checkpoint.** With the source's definitions, $W=h_ah_b'-h_a'h_b$ and $c=-W$, so $h_a'h_b-h_ah_b'=c$, not $W$. The printed calculation is preserved below; the identity $c^{-1}(h_a'h_b-h_ah_b')=1$ is the one that proves $LGf=f$.
<!-- END BACKGROUND BG-II.block3 -->

In this section, $[a,b]$ will be a proper interval with $-\infty<a<b<\infty$. $C[a,b]$ denotes the continuous functions $f:[a,b]\to\mathbb R$ and for $n\geq1$, $C^{(n)}[a,b]$ denotes those functions in $C[a,b]$ that have $n$ continuous derivatives. $C_{\mathbb C}^{(n)}[a,b]$ denotes the corresponding spaces of complex-valued functions. We want to consider the differential equation

$$
\tag{6.1}
-h''+qh-\lambda h=f,
$$


<a id="pdf-page-65"></a>
50
 II. Operators on Hilbert Space

where $\lambda$ is a given complex number, $q\in C[a,b]$, and $f\in L^{2}[a,b]$, together with the boundary conditions

**6.2**
$$
\left\{
\begin{aligned}
\text{(a)}\quad \alpha h(a)+\alpha_{1}h'(a)&=0\\
\text{(b)}\quad \beta h(b)+\beta_{1}h'(b)&=0,
\end{aligned}
\right.
$$

where $\alpha$, $\alpha_{1}$, $\beta$, and $\beta_{1}$ are real numbers and $\alpha^{2}+\alpha_{1}^{2}>0$, $\beta^{2}+\beta_{1}^{2}>0$.

Equation (6.1) together with the boundary conditions (6.2) is called a *(regular) Sturm–Liouville system*. Such systems arise in a number of physical problems, including the description of the motion of a vibrating string. In this section we will discuss solutions of the Sturm–Liouville system by relating the system to a certain compact self-adjoint integral operator.

Recall that an absolutely continuous function $h$ on $[a,b]$ has a derivative a.e. and $h(x)=\int_a^x h'(t)\,dt+h(a)$ for all $x$.

Define
$$
\mathcal D_a\equiv\{h\in C_{\mathbb C}^{(1)}[a,b]: h'\text{ is absolutely continuous, }
h''\in L^2[a,b],\text{ and }h\text{ satisfies (6.2a)}\}.
$$

$\mathcal D_b$ is defined similarly but each $h$ in $\mathcal D_b$ satisfies (6.2b) instead of (6.2a). The space $\mathcal D=\mathcal D_a\cap\mathcal D_b$.

Define $L:\mathcal D\to L^2[a,b]$ by

**6.3**
$$
Lh=-h''+qh.
$$

$L$ is called a *Sturm–Liouville operator*.

Note that $\mathcal D$ is a linear space and $L$ is a linear transformation. The Sturm–Liouville problem thus becomes: if $\lambda\in\mathbb C$ and $f\in L^2[a,b]$, is there an $h$ in $\mathcal D$ with $(L-\lambda)h=f$. Equivalently, for which $\lambda$ is $f$ in $\operatorname{ran}(L-\lambda)$?

By placing a suitable norm on $\mathcal D$, $L$ can be made into a bounded operator. This does not help much. The best procedure is to consider $(L-\lambda)^{-1}$. Integration is the inverse of differentiation, and it turns out that $(L-\lambda)^{-1}$ (when we can define it) is an integral operator.

Begin by considering the case when $\lambda=0$. (Equivalently, replace $q$ by $q-\lambda$.) To define $L^{-1}$ (even if only on the range of $L$), we need that $L$ is injective. Thus we make an assumption;

**6.4**
$$
\text{if }h\in\mathcal D\quad\text{and}\quad Lh=0,\quad\text{then}\quad h=0.
$$

The first lemma is from ordinary differential equations and says that certain initial-value problems have nontrivial (nonzero) solutions.

**6.5. Lemma.** *If $\alpha,\alpha_{1},\beta,\beta_{1}\in\mathbb R$, $\alpha^{2}+\alpha_{1}^{2}>0$, and $\beta^{2}+\beta_{1}^{2}>0$, then there are functions $h_a$, $h_b$ in $\mathcal D_a$, $\mathcal D_b$, respectively, such that $L(h_a)=0$ and $L(h_b)=0$ and $h_a$, $h_b$ are real-valued and not identically zero.*

The *Wronskian* of $h_a$ and $h_b$ is the function
$$
W=\det\begin{bmatrix}h_a&h_b\\h_a'&h_b'\end{bmatrix}
=h_a h_b'-h_a'h_b.
$$



<a id="pdf-page-66"></a>
Note that $W'=h_a h_b''-h_a''h_b=h_a(qh_b)-(qh_a)h_b=0$. Hence $W(x)\equiv W(a)$ for all $x$.

**6.6. Lemma.** Assuming (6.4), $W(a)\neq 0$ and so $h_a$ and $h_b$ are linearly independent.

**Proof.** If $W(a)=0$, then linear algebra tells us that the column vectors in the matrix used to define $W(a)$ are linearly dependent. Thus there is a $\lambda$ in $\mathbb R$ such that $h_b(a)=\lambda h_a(a)$ and $h_b'(a)=\lambda h_a'(a)$. Thus $h_b\in\mathcal D$ and $L(h_b)=0$. By (6.4), $h_b\equiv 0$, contradiction. $\blacksquare$

Put $c=-W(a)$ and define $g:[a,b]\times[a,b]\to\mathbb R$ by

**6.7**
$$
g(x,y)=
\begin{cases}
c^{-1}h_a(x)h_b(y) & \text{if }a\leq x\leq y\leq b,\\
c^{-1}h_a(y)h_b(x) & \text{if }a\leq y\leq x\leq b.
\end{cases}
$$

The function $g$ is the *Green function* for $L$.

**6.8. Lemma.** The function $g$ defined in (6.7) is real-valued, continuous, and $g(x,y)=g(y,x)$.

**Proof.** Exercise.

**6.9. Theorem.** Assume (6.4). If $g$ is the Green function for $L$ defined in (6.7) and $G:L^2[a,b]\to L^2[a,b]$ is the integral operator defined by

$$
(Gf)(x)=\int_a^b g(x,y)f(y)\,dy,
$$

then $G$ is a compact self-adjoint operator, $\operatorname{ran}G=\mathcal D$, $LGf=f$ for all $f$ in $L^2[a,b]$, and $GLh=h$ for all $h$ in $\mathcal D$.

**Proof.** That $G$ is self-adjoint follows from the fact that $g$ is real-valued and $g(x,y)=g(y,x)$; $G$ is compact by (4.7). Fix $f$ in $L^2[a,b]$ and put $h=Gf$. It must be shown that $h\in\mathcal D$.

Put

$$
H_a(x)=c^{-1}\int_a^x h_a(y)f(y)\,dy
\quad\text{and}\quad
H_b(x)=c^{-1}\int_x^b h_b(y)f(y)\,dy.
$$

Then

$$
\begin{aligned}
h(x)
&=\int_a^b g(x,y)f(y)\,dy\\
&=c^{-1}\int_a^x h_a(y)h_b(x)f(y)\,dy
+c^{-1}\int_x^b h_a(x)h_b(y)f(y)\,dy.
\end{aligned}
$$

That is, $h=H_a h_b+h_a H_b$. Differentiating this equation gives $h'=(c^{-1}h_a f)h_b+H_a h_b'+h_a'H_b+h_a(-c^{-1}h_b f)=H_a h_b'+h_a'H_b$ a.e. Since $H_a h_b'+h_a'H_b$ is absolutely continuous, as part of showing that $h\in\mathcal D$ we want to show the following.



<a id="pdf-page-67"></a>
**Claim.** $h'=H_a h_b'+h_a'H_b$ everywhere.

Put $\phi=H_a h_b'+h_a'H_b$ and put $\psi(x)=h(a)+\int_a^x\phi(y)\,dy$. So $\phi$ and $\psi$ are absolutely continuous, $h(a)=\psi(a)$, and $h'=\psi'$ a.e. Thus $h=\psi$ everywhere. But $\psi$ has a continuous derivative $\phi$, so $h$ does too. That is, the claim is proved.

Differentiating $h'=H_a h_b'+h_a'H_b$ gives that a.e.,
$$
h''=(c^{-1}h_a f)h_b'+H_a h_b''+h_a''H_b+h_a'(-c^{-1}h_b f);
$$
since each of these summands belongs to $L^2[a,b]$, $h''\in L^2[a,b]$.

Because $H_a(a)=0$ and $h_a\in\mathcal D_a$,
$$
\alpha h(a)+\alpha_1h'(a)
=\alpha h_a(a)H_b(a)+\alpha_1h_a'(a)H_b(a)
=[\alpha h_a(a)+\alpha_1h_a'(a)]H_b(a)=0.
$$
Hence $h\in\mathcal D_a$. Similarly, $h\in\mathcal D_b$. Thus $h\in\mathcal D$. Hence $\operatorname{ran}G\subseteq\mathcal D$.

Now to show that $LGf=f$. If $h=Gf$,
$$
\begin{aligned}
L(h)&=-h''+qh\\
&=-\bigl(c^{-1}h_a h_b'f+H_a h_b''+h_a''H_b-c^{-1}h_a'h_bf\bigr)
  +q(H_a h_b+h_aH_b)\\
&=(-h_b''+qh_b)H_a+(-h_a''+qh_a)H_b
  +c^{-1}(h_a'h_b-h_a h_b')f\\
&=f
\end{aligned}
$$
since $L(h_a)=L(h_b)=0$ and $h_a'h_b-h_a h_b'=W=c$.

If $h\in\mathcal D$, then $Lh\in L^2[a,b]$. So by the first part of the proof, $LGLh=Lh$. Thus $0=L(GLh-h)$. Since $\ker L=(0)$, $h=GLh$ and so $h\in\operatorname{ran}G$. $\blacksquare$

**6.10. Corollary.** Assume (6.4). If $h\in\mathcal D$, $\lambda\in\mathbb C\setminus\{0\}$, and $Lh=\lambda h$, then $Gh=\lambda^{-1}h$. If $h\in L^2[a,b]$ and $Gh=\lambda^{-1}h$, then $h\in\mathcal D$ and $Lh=\lambda h$.

**Proof.** This is immediate from the theorem. $\blacksquare$

**6.11. Lemma.** Assume (6.4). If $\alpha\in\sigma_p(G)$ and $\alpha\ne0$, then $\dim\ker(G-\alpha)=1$.

**Proof.** Suppose there are linearly independent functions $h_1,h_2$ in $\ker(G-\alpha)$. By (6.10), $h_1,h_2$ are solutions of the equation
$$
-h''+(q-\alpha^{-1})h=0.
$$
Since this is a second-order linear differential equation, every solution of it must be a linear combination of $h_1$ and $h_2$. But $h_1,h_2\in\mathcal D$ so they satisfy (6.2). But a solution can be found to this equation satisfying any initial conditions at $a$—and thus not satisfying (6.2). This contradiction shows that linearly independent $h_1,h_2$ in $\ker(G-\alpha)$ cannot be found. $\blacksquare$

**6.12. Theorem.** Assume (6.4). Then there is a sequence $\{\lambda_1,\lambda_2,\ldots\}$ of real numbers and a basis $\{e_1,e_2,\ldots\}$ for $L^2[a,b]$ such that

(a) $0<|\lambda_1|<|\lambda_2|<\cdots$ and $|\lambda_n|\to\infty$.

(b) $e_n\in\mathcal D$ and $Le_n=\lambda_n e_n$ for all $n$.

(c) If $\lambda\ne\lambda_n$ for any $\lambda_n$ and $f\in L^2[a,b]$, then there is a unique $h$ in $\mathcal D$ with $Lh-\lambda h=f$.

(d) If $\lambda=\lambda_n$ for some $n$ and $f\in L^2[a,b]$, then there is an $h$ in $\mathcal D$ with $Lh-\lambda h=f$ if and only if $\langle f,e_n\rangle=0$. If $\langle f,e_n\rangle=0$, any two solutions of $Lh-\lambda h=f$ differ by a multiple of $e_n$.

**Proof.** Parts (a) and (b) follow by Theorem 5.1, Corollary 6.10, and



<a id="pdf-page-68"></a>
Lemma 6.1. For parts (c) and (d), first note that

$$
\tag{6.13}
Lh-\lambda h=f\quad\text{if and only if}\quad h-\lambda Gh=Gf.
$$

This is, in fact, a straightforward consequence of Theorem 6.9.

(c) The case where $\lambda=0$ is left to the reader. If $\lambda\ne\lambda_n$ for any $n$, $\lambda^{-1}\notin\sigma_p(G)$. Since $G=G^*$, Corollary 4.15 implies $G-\lambda^{-1}$ is bijective. So if $f\in L^2[a,b]$, there is a unique $h$ in $L^2[a,b]$ with $Gf=(\lambda^{-1}-G)h$. Thus $h\in\mathcal D$ and (6.13) implies $L(h/\lambda)-\lambda(h/\lambda)=f$.

(d) Suppose $\lambda=\lambda_n$ for some $n$. If $Lh-\lambda_nh=f$, then $h-\lambda_nGh=Gf$. Hence $\langle Gf,e_n\rangle=\langle h,e_n\rangle-\lambda_n\langle Gh,e_n\rangle=\langle h,e_n\rangle-\lambda_n\langle h,Ge_n\rangle=\langle h,e_n\rangle-\lambda_n\lambda_n^{-1}\langle h,e_n\rangle=0$. So $0=\langle Gf,e_n\rangle=\langle f,Ge_n\rangle=\lambda_n\langle f,e_n\rangle$. Hence $f\perp e_n$.

Since $\mathbb C e_n=\ker(G-\lambda_n^{-1})$, $[e_n]^\perp\equiv\mathcal N$ reduces $G$. Let $G_1=G|_{\mathcal N}$. So $G_1$ is a compact self-adjoint operator on $\mathcal N$ and $\lambda_n^{-1}\notin\sigma_p(G_1)$. By (4.15), $\operatorname{ran}(G_1-\lambda_n^{-1})=\mathcal N$. As in the proof of (c), if $f\perp e_n$, there is a unique $h\in\mathcal N$ such that $Lh-\lambda_nh=f$. Note that $h+\alpha e_n$ is also a solution. If $h_1,h_2$ are two solutions, $h_1-h_2\in\ker(L-\lambda_n)$, so $h_1-h_2=\alpha e_n$. ■

What happens if $\ker L\ne(0)$? In this case it is possible to find a real number $\mu$ such that $\ker(L-\mu)=(0)$ (Exercise 6). Replacing $q$ by $q-\mu$, Theorem 6.12 now applies. More information on this problem can be found in Exercises 2 through 5.

## EXERCISES

1. Consider the Sturm–Liouville operator $Lh=-h''$ with $a=0$, $b=1$, and for each of the following boundary conditions find the eigenvalues $\{\lambda_n\}$, the eigenvectors $\{e_n\}$, and the Green function $g(x,y)$: (a) $h(0)=h(1)=0$; (b) $h'(0)=h'(1)=0$; (c) $h(0)=0$ and $h'(1)=0$; (d) $h(0)=h'(0)$ and $h(1)=-h'(1)$.

2. In Theorem 6.12 show that $\sum_{n=1}^{\infty}\lambda_n^{-2}<\infty$ (see Exercise 5.3).

3. In Theorem 6.12 show that $h\in\mathcal D$ if and only if $h\in L^2[a,b]$ and $\sum_{n=1}^{\infty}\lambda_n^2|\langle h,e_n\rangle|^2<\infty$. If $h\in\mathcal D$, show that $h(x)=\sum_{n=1}^{\infty}\langle h,e_n\rangle e_n(x)$, where this series converges uniformly and absolutely on $[a,b]$.

4. In Theorem 6.12(c), show that $h(x)=\sum_{n=1}^{\infty}(\lambda_n-\lambda)^{-1}\langle f,e_n\rangle e_n(x)$ and this series converges uniformly and absolutely on $[a,b]$.

5. In Theorem 6.12(d), show that if $f\perp e_n$ and $Lh-\lambda_nh=f$, then $h(x)=\sum_{j\ne n}(\lambda_j-\lambda_n)^{-1}\langle f,e_j\rangle e_j(x)+\alpha e_n(x)$ for some $\alpha$, where the series converges uniformly and absolutely on $[a,b]$.

6. This exercise demonstrates how to handle the case in which $\ker L\ne(0)$. (a) If $h,g\in C^{(1)}[a,b]$ with $h',g'$ absolutely continuous and $h'',g''\in L^2[a,b]$, show that

   $$
   \int_a^b(h''g-hg'')=[h'(b)g(b)-h(b)g'(b)]-[h'(a)g(a)-h(a)g'(a)].
   $$

   (b) If $h,g\in\mathcal D$, show that $\langle Lh,g\rangle=\langle h,Lg\rangle$. (The inner product is in $L^2[a,b]$.)

   (c) If $h,g\in\mathcal D$ and $\lambda,\mu\in\mathbb R$, $\lambda\ne\mu$, and if $h\in\ker(L-\lambda)$, $g\in\ker(L-\mu)$, then $h\perp g$.

   (d) Show that there is a real number $\mu$ with $\ker(L-\mu)=(0)$.


<a id="pdf-page-69"></a>
## §7*. The Spectral Theorem and Functional Calculus for Compact Normal Operators

<!-- BEGIN BACKGROUND BG-II.block4 -->
<a id="bg-ii-13"></a>
### Definition BG-II.13. Strong convergence versus norm convergence of operators

An operator sequence $A_n$ converges **strongly** to $A$ if $\|A_nh-Ah\|\to0$ for every fixed $h$. It converges in **operator norm** if $\sup_{\|h\|\leq1}\|A_nh-Ah\|\to0$. Norm convergence implies strong convergence, but the coordinate-projection example in Lemma BG-II.9 disproves the converse.

<a id="bg-ii-14"></a>
### Lemma BG-II.14. Orthogonal projection series and functional calculus

Let $P_j$ be pairwise orthogonal projections with $\sum_jP_jh=h$ for each $h$, and let $(a_j)$ be bounded. Then $Ah=\sum_ja_jP_jh$ converges in vector norm, defines a bounded operator, and

$$
\|A\|=\sup_{j:P_j\ne0}|a_j|,\qquad
\left\|\sum_{j>N}a_jP_j\right\|=\sup_{j>N:P_j\ne0}|a_j|.
$$

**Proof.** Orthogonality gives $\sum_j\|P_jh\|^2=\|h\|^2$. Thus squared norms of tails are at most $(\sup_j|a_j|)^2\sum_{j>N}\|P_jh\|^2$, which tends to zero for each $h$. The same computation gives $\|Ah\|\leq(\sup|a_j|)\|h\|$. A unit vector in any nonzero range $P_jH$ yields the reverse inequality. Applying this argument just to a tail proves the second identity. Bounded operators preserve these convergent vector series by continuity, justifying multiplication of diagonal expansions in Theorem 7.11. The series for $\phi(T)$ need only converge strongly; it converges in operator norm along the indicated truncations precisely when its tail coefficient supremum tends to zero. A coefficient on a zero projection does not contribute to the norm; in particular $\phi(0)$ contributes only when $\ker T\ne\{0\}$. $\square$
<!-- END BACKGROUND BG-II.block4 -->

We begin by characterizing the operators that commute with a diagonalizable operator. If one considers the definition of a diagonalizable operator (4.6), it is possible to reformulate it in a way that is more tractable for the present purpose and closer to the form of a compact self-adjoint operator given in (5.2). Unlike (4.6), it will not be assumed that the underlying Hilbert space is separable.

**7.1. Proposition.** *Let $\{P_i:i\in I\}$ be a family of pairwise orthogonal projections in $\mathcal B(\mathcal H)$. (That is, $P_iP_j=P_jP_i=0$ for $i\ne j$.) If $h\in\mathcal H$, then $\sum_i\{P_i h:i\in I\}$ converges in $\mathcal H$ to $Ph$, where $P$ is the projection of $\mathcal H$ onto $\bigvee\{P_i\mathcal H:i\in I\}$.*

This appeared as Exercise 3.5 and its proof is left to the reader.

If $\{P_i:i\in I\}$ is as in the preceding proposition and $\mathcal M_i=P_i\mathcal H$, then with the notation of Definition 3.4, $P$ is the projection of $\mathcal H$ onto $\bigoplus_i\mathcal M_i$. Write $P=\sum_iP_i$. A word of caution here: $Ph=\sum_iP_i h$, where the convergence is in the norm of $\mathcal H$. However, $\sum_iP_i$ does not converge to $P$ in the norm of $\mathcal B(\mathcal H)$. In fact, it never does unless $I$ is finite (Exercise 1).

**7.2. Definition.** A *partition of the identity* on $\mathcal H$ is a family $\{P_i:i\in I\}$ of pairwise orthogonal projections on $\mathcal H$ such that $\bigvee_iP_i\mathcal H=\mathcal H$. This might be indicated by $1=\sum_iP_i$ or $1=\bigoplus_iP_i$. [Note that $1$ is often used to denote the operator on $\mathcal H$ defined by $1(h)=h$ for all $h$. Similarly if $\alpha\in\mathbb F$, $\alpha$ is the operator defined by $\alpha(h)=\alpha h$ for all $h$.]

**7.3. Definition.** An operator $A$ on $\mathcal H$ is *diagonalizable* if there is a partition of the identity on $\mathcal H$, $\{P_i:i\in I\}$, and a family of scalars $\{\alpha_i:i\in I\}$ such that $\sup_i|\alpha_i|<\infty$ and $Ah=\alpha_i h$ whenever $h\in\operatorname{ran}P_i$.

It is easy to see that this is equivalent to the definition given in (4.6) when $\mathcal H$ is separable (Exercise 2). Also, $\|A\|=\sup_i|\alpha_i|$.

To denote a diagonalizable operator satisfying the conditions of (7.3), write

$$
A=\sum_i\alpha_iP_i
\quad\text{or}\quad
A=\bigoplus_i\alpha_iP_i.
$$

Note that it was not assumed that the scalars $\alpha_i$ in (7.3) are distinct. There is no loss in generality in assuming this, however. In fact, if $\alpha_i=\alpha_j$, then we can replace $P_i$ and $P_j$ with $P_i+P_j$.

**7.4. Proposition.** *An operator $A$ on $\mathcal H$ is diagonalizable if and only if there is an orthonormal basis for $\mathcal H$ consisting of eigenvectors for $A$.*

**Proof.** Exercise.

Also note that if $A=\bigoplus_i\alpha_iP_i$, then $A^*=\bigoplus_i\overline{\alpha_i}P_i$ and $A$ is normal (Exercise 5).



<a id="pdf-page-70"></a>
**7.5. Theorem.** *If $A=\bigoplus_i\alpha_iP_i$ is diagonalizable and all the $\alpha_i$ are distinct, then an operator $B$ in $\mathscr B(\mathcal H)$ satisfies $AB=BA$ if and only if for each $i$, $\operatorname{ran}P_i$ reduces $B$.*

**Proof.** If all the $\alpha_i$ are distinct, then $\operatorname{ran}P_i=\ker(A-\alpha_i)$. If $AB=BA$ and $Ah=\alpha_i h$, then $ABh=BAh=B(\alpha_i h)=\alpha_i Bh$; hence $Bh\in\operatorname{ran}P_i$ whenever $h\in\operatorname{ran}P_i$. Thus $\operatorname{ran}P_i$ is left invariant by $B$. Therefore $B$ leaves $\bigvee\{\operatorname{ran}P_j:j\ne i\}=\mathcal N_i$ invariant. But since $\bigoplus_iP_i=1$, $\mathcal N_i=(\operatorname{ran}P_i)^\perp$. Thus $\operatorname{ran}P_i$ reduces $B$.

Now assume that $B$ is reduced by each $\operatorname{ran}P_i$. Thus $BP_i=P_iB$ for all $i$. If $h\in\mathcal H$, then $Ah=\sum_i\alpha_iP_i h$. Hence $BAh=\sum_i\alpha_iBP_i h=\sum_i\alpha_iP_iBh=ABh$. (Why is the first equality valid?) $\blacksquare$

Using the notation of the preceding theorem, if $AB=BA$, let $B_i=B|_{\operatorname{ran}P_i}$. Then it is appropriate to write $B=\bigoplus_iB_i$ on $\mathcal H=\bigoplus_i(P_i\mathcal H)$. One might paraphrase Theorem 7.5 by saying that $B$ commutes with a diagonalizable operator if and only if $B$ can be “diagonalized with operator entries.”

**7.6. Spectral Theorem for Compact Normal Operators.** *If $T$ is a compact normal operator on the complex Hilbert space $\mathcal H$, then $T$ has only a countable number of distinct eigenvalues. If $\{\lambda_1,\lambda_2,\ldots\}$ are the distinct nonzero eigenvalues of $T$, and $P_n$ is the projection of $\mathcal H$ onto $\ker(T-\lambda_n)$, then $P_nP_m=P_mP_n=0$ if $n\ne m$ and*

$$
\tag{7.7} T=\sum_{n=1}^{\infty}\lambda_nP_n,
$$

*where this series converges to $T$ in the metric defined by the norm on $\mathscr B(\mathcal H)$.*

**Proof.** Let $A=(T+T^*)/2$, $B=(T-T^*)/2i$. So $A,B$ are compact self-adjoint operators, $T=A+iB$, and $AB=BA$ since $T$ is normal. The idea of the proof is rather simple. We’ll get started in this proof together but the reader will have to complete the details.

By Theorem 5.1, $A=\sum_1^\infty\alpha_nE_n$, where $\alpha_n\in\mathbb R$, $\alpha_n\ne\alpha_m$ if $n\ne m$, and $E_n$ is the projection of $\mathcal H$ onto $\ker(A-\alpha_n)$. Since $AB=BA$, the idea is to use Theorem 7.5 and Theorem 5.1 applied to $B$ to diagonalize $A$ and $B$ simultaneously; that is, to find an orthonormal basis for $\mathcal H$ consisting of vectors that are simultaneously eigenvectors of $A$ and $B$.

Since $BA=AB$, $E_n\mathcal H=\mathcal L_n$ reduces $B$ for every $n$ (7.5). Let $B_n=B|_{\mathcal L_n}$; then $B_n=B_n^*$ and $\dim\mathcal L_n<\infty$. Applying (5.1) (or, rather, the corresponding theorem from linear algebra) to $B_n$, there is a basis $\{e_j^{(n)}:1\le j\le d_n\}$ for $\mathcal L_n$ and real numbers $\{\beta_j^{(n)}:1\le j\le d_n\}$ such that $B_ne_j^{(n)}=\beta_j^{(n)}e_j^{(n)}$. Thus $Te_j^{(n)}=Ae_j^{(n)}+iBe_j^{(n)}=(\alpha_n+i\beta_j^{(n)})e_j^{(n)}$.

Therefore $\{e_j^{(n)}:1\le j\le d_n,\ n\ge1\}$ is a basis for $\operatorname{cl}(\operatorname{ran}A)$ consisting of eigenvectors for $T$. It may be that $\operatorname{cl}(\operatorname{ran}A)\ne\operatorname{cl}(\operatorname{ran}T)$. Since $B$ is reduced by $\ker A=(\operatorname{ran}A)^\perp$ and $B_0=B|_{\ker A}$ is a compact self-adjoint operator there



<a id="pdf-page-71"></a>
is an orthonormal basis $\{e_j^{(0)}:j\geqslant 1\}$ for $\operatorname{cl}(\operatorname{ran}B_0)$ and scalars $\{\beta_j^{(0)}:j\geqslant 1\}$ such that $Be_j^{(0)}=\beta_j^{(0)}e_j^{(0)}$. It follows that $Te_j^{(0)}=i\beta_j^{(0)}e_j^{(0)}$. Moreover, $\ker T^*\supseteq\ker A\cap\ker B_0$ so $\operatorname{cl}(\operatorname{ran}T)\subseteq\operatorname{cl}(\operatorname{ran}A)\oplus\operatorname{cl}(\operatorname{ran}B_0)$.

The remainder of the proof now consists in a certain amount of bookkeeping to gather together the eigenvectors belonging to the same eigenvalues of $T$ and the performing of some light housekeeping chores to obtain the convergence of the series (7.7) ■

**7.8. Corollary.** *With the notation of (7.6):*

(a) $\ker T=[\bigvee\{P_n\mathcal H:n\geqslant 1\}]^\perp$;

(b) *each $P_n$ has finite rank;*

(c) $\|T\|=\sup\{|\lambda_n|:n\geqslant 1\}$ *and either $\{\lambda_n\}$ is finite or $\lambda_n\to 0$ as $n\to\infty$.*

The proof of (7.8) is similar to the proof of (5.3).

**7.9. Corollary.** *If $T$ is a compact operator on a complex Hilbert space, then $T$ is normal if and only if $T$ is diagonalizable.*

If $T$ is a normal operator which is not necessarily compact, there is a spectral theorem for $T$ which has a somewhat different form. This theorem states that $T$ can be represented as an integral with respect to a measure whose values are not numbers but projections on a Hilbert space. Theorem 7.6 will be a consequence of this more general theorem and correspond to the case in which this projection-valued measure is “atomic.”

The approach to this more general spectral theorem will be to develop a functional calculus for normal operators $T$. That is, an operator $\phi(T)$ will be defined for every bounded Borel function $\phi$ on $\mathbb C$ and certain properties of the map $\phi\mapsto\phi(T)$ will be deduced. The projection-valued measure will then be obtained by letting $\mu(\Delta)=\chi_\Delta(T)$, where $\chi_\Delta$ is the characteristic function of the set $\Delta$. These matters are taken up in Chapter IX.

At this point, Theorem 7.6 will be used to develop a functional calculus for compact normal operators. For the remainder of this section $\mathcal H$ is a complex Hilbert space.

**7.10. Definition.** Denote by $l^\infty(\mathbb C)$ all the bounded functions $\phi:\mathbb C\to\mathbb C$. If $T$ is a compact normal operator satisfying (7.7), define $\phi(T):\mathcal H\to\mathcal H$ by

$$
\phi(T)=\sum_{n=1}^{\infty}\phi(\lambda_n)P_n+\phi(0)P_0,
$$

where $P_0=$ the projection of $\mathcal H$ onto $\ker T$.

Note that $\phi(T)$ is a diagonalizable operator and $\|\phi(T)\|=\sup\{|\phi(0)|,|\phi(\lambda_1)|,\ldots\}$ (4.6). Much more can be said.

**7.11. Functional Calculus for Compact Normal Operators.** *If $T$ is a compact normal operator on a $\mathbb C$-Hilbert space $\mathcal H$, then the map $\phi\mapsto\phi(T)$ of*



<a id="pdf-page-72"></a>
§7. The Spectral Theorem and Functional Calculus  57

$l^\infty(\mathbb C)\to\mathcal B(\mathcal H)$ *has the following properties:*

(a) $\phi\mapsto\phi(T)$ *is a multiplicative linear map of* $l^\infty(\mathbb C)$ *into* $\mathcal B(\mathcal H)$. *If* $\phi\equiv 1$, $\phi(T)=1$; *if* $\phi(z)=z$ *on* $\sigma_p(T)\cup\{0\}$, *then* $\phi(T)=T$.

(b) $\|\phi(T)\|=\sup\{|\phi(\lambda)|:\lambda\in\sigma_p(T)\}$.

(c) $\phi(T)^*=\phi^*(T)$, *where* $\phi^*$ *is the function defined by* $\phi^*(z)=\overline{\phi(z)}$.

(d) *If* $A\in\mathcal B(\mathcal H)$ *and* $AT=TA$, *then* $A\phi(T)=\phi(T)A$ *for all* $\phi$ *in* $l^\infty(\mathbb C)$.

**Proof.** Adopt the notation of Theorem 7.6 and (7.10).

(a) If $\phi,\psi\in l^\infty(\mathbb C)$, then $(\phi\psi)(z)=\phi(z)\psi(z)$ for $z$ in $\mathbb C$. Also, $\phi(T)\psi(T)h=[\phi(0)P_0+\sum_n\phi(\lambda_n)P_n][\psi(0)P_0+\sum_m\psi(\lambda_m)P_m]h=[\phi(0)P_0+\sum_n\phi(\lambda_n)P_n][\psi(0)P_0h+\sum_m\psi(\lambda_m)P_mh]$. Since $P_nP_m=0$ when $n\ne m$, this gives that $\phi(T)\psi(T)h=\phi(0)\psi(0)P_0h+\sum_n\phi(\lambda_n)\psi(\lambda_n)P_nh=(\phi\psi)(T)h$. Thus $\phi\mapsto\phi(T)$ is multiplicative. The linearity of the map is left to the reader. If $\phi(z)=1$, then $\phi(T)=1(T)=P_0+\sum_{n=1}^{\infty}P_n=1$ since $\{P_0,P_1,\ldots\}$ is a partition of the identity. If $\phi(z)=z$, $\phi(\lambda_n)=\lambda_n$ and so $\phi(T)=T$.

Parts (b) and (c) follow from Exercise 5.

(d) If $AT=TA$, Theorem 7.5 implies that $P_0\mathcal H,P_1\mathcal H,\ldots$ all reduce $A$. Fix $h_n$ in $P_n\mathcal H$, $n\geq 0$. If $\phi\in l^\infty(\mathbb C)$, then $Ah_n\in P_n\mathcal H$ and so $\phi(T)Ah_n=\phi(\lambda_n)Ah_n=A(\phi(\lambda_n)h_n)=A\phi(T)h_n$. If $h\in\mathcal H$, then $h=\sum_{n=0}^{\infty}h_n$, where $h_n\in P_n$. Hence $\phi(T)Ah=\sum_{n=0}^{\infty}\phi(T)Ah_n=\sum_{n=0}^{\infty}A\phi(T)h_n=A\phi(T)h$. (Justify the first equality.) $\blacksquare$

Which operators on $\mathcal H$ can be expressed as $\phi(T)$ for some $\phi$ in $l^\infty(\mathbb C)$? Part (d) of the preceding theorem provides the answer.

**7.12. Theorem.** *If $T$ is a compact normal operator on a $\mathbb C$-Hilbert space, then $\{\phi(T):\phi\in l^\infty(\mathbb C)\}$ is equal to*
$$
\{B\in\mathcal B(\mathcal H):BA=AB\text{ whenever }AT=TA\}.
$$

**Proof.** Half of the desired equality is obtained from (7.11d). So let $B\in\mathcal B(\mathcal H)$ and assume that $BA=AB$ whenever $AT=TA$. Thus, $B$ must commute with $T$ itself. By (7.5), $B$ is reduced by each $P_n\mathcal H\equiv\mathcal H_n$, $n\geq 0$; put $B_n=B|_{\mathcal H_n}$. Fix $n\geq 0$ for the moment and let $A_n$ be any bounded operator in $\mathcal B(\mathcal H_n)$. Define $Ah=A_nh$ if $h\in\mathcal H_n$ and $Ah=0$ if $h\in\mathcal H_m$, $m\ne n$, and extend $A$ to $\mathcal H$ by linearity; so $A=\bigoplus_{m=0}^{\infty}A_m$ where $A_m=0$ if $m\ne n$. By (7.5), $AT=TA$; hence $BA=AB$. This implies that $B_nA_n=A_nB_n$. Since $A_n$ was arbitrarily chosen from $\mathcal B(\mathcal H_n)$, $B_n=\beta_n$ for some $\beta_n$ (Exercise 7). If $\phi:\mathbb C\to\mathbb C$ is defined by $\phi(0)=\beta_0$ and $\phi(\lambda_n)=\beta_n$ for $n\geq 1$, then $B=\phi(T)$. $\blacksquare$

**7.13. Definition.** If $A\in\mathcal B(\mathcal H)$, then $A$ is *positive* if $\langle Ah,h\rangle\geq 0$ for all $h$ in $\mathcal H$. In symbols this is denoted by $A\geq 0$.

Note that by Proposition 2.12 every positive operator on a complex Hilbert space is self-adjoint.



<a id="pdf-page-73"></a>
**7.14. Proposition.** *If $T$ is a compact normal operator, then $T$ is positive if and only if all its eigenvalues are non-negative real numbers.*

**Proof.** Let $T=\sum_{1}^{\infty}\lambda_nP_n$. If $T\geq 0$ and $h\in P_n\mathcal H$ with $\|h\|=1$, then $Th=\lambda_nh$. Hence $\lambda_n=\langle Th,h\rangle\geq 0$. Conversely, assume each $\lambda_n\geq 0$. If $h\in\mathcal H$, $h=h_0+\sum_{n=1}^{\infty}h_n$, where $h_0\in\ker T$ and $h_n\in P_n\mathcal H$ for $n\geq 1$. Then $Th=\sum_{1}^{\infty}\lambda_nh_n$. Hence

$$
\begin{aligned}
\langle Th,h\rangle
&=\left\langle\sum_{n=1}^{\infty}\lambda_nh_n,\,
h_0+\sum_{m=1}^{\infty}h_m\right\rangle\\
&=\sum_{n=1}^{\infty}\sum_{m=0}^{\infty}
\lambda_n\langle h_n,h_m\rangle
=\sum_{n=1}^{\infty}\lambda_n\|h_n\|^2\geq 0
\end{aligned}
$$

since $\langle h_n,h_m\rangle=0$ when $n\ne m$. ■

**7.15. Theorem.** *If $T$ is a compact self-adjoint operator, then there are unique positive compact operators $A,B$ such that $T=A-B$ and $AB=BA=0$.*

**Proof.** Let $T=\sum_{n=1}^{\infty}\lambda_nP_n$ as in (7.6). Define $\phi,\psi:\mathbb C\to\mathbb C$ by $\phi(\lambda_n)=\lambda_n$ if $\lambda_n>0$, $\phi(z)=0$ otherwise; $\psi(\lambda_n)=-\lambda_n$ if $\lambda_n<0$, $\psi(z)=0$ otherwise. Put $A=\phi(T)$ and $B=\psi(T)$. Then $A=\sum\{\lambda_nP_n:\lambda_n>0\}$ and $B=\sum\{-\lambda_nP_n:\lambda_n<0\}$. Thus $T=A-B$. Since $\phi\psi=0$, $AB=BA=0$ by (7.11a). Since $\phi,\psi\geq 0$, $A,B\geq 0$ by the preceding proposition. It remains to show that $A,B$ are unique.

Suppose $T=C-D$ where $C,D$ are compact positive operators and $CD=DC=0$. It is easy to check that $C$ and $D$ commute with $T$. Put $\lambda_0=0$ and $P_0=$ the projection of $\mathcal H$ onto $\ker T$. Thus $C$ and $D$ are reduced by $P_n\mathcal H\equiv\mathcal H_n$ for all $n\geq 0$. Let $C_n=C|_{\mathcal H_n}$ and $D_n=D|_{\mathcal H_n}$. So $C_nD_n=D_nC_n=0$, $\lambda_nP_n=T|_{\mathcal H_n}=C_n-D_n$, and $C_n,D_n$ are positive. Suppose $\lambda_n>0$ and let $h\in\mathcal H_n$. Since $C_nD_n=0$, $\ker C_n\supseteq\operatorname{cl}[\operatorname{ran}D_n]=(\ker D_n)^\perp$. So if $h\in(\ker D_n)^\perp$, then $\lambda_nh=-D_nh$. Hence $\lambda_n\|h\|^2=-\langle D_nh,h\rangle\leq 0$. Thus $h=0$ since $\lambda_n>0$. That is, $\ker D_n=\mathcal H_n$. Thus $D_n=0=B|_{\mathcal H_n}$ and $C_n=\lambda_nP_n=A|_{\mathcal H_n}$. Similarly, if $\lambda_n<0$, $C_n=0=A|_{\mathcal H_n}$ and $D_n=-\lambda_nP_n=B|_{\mathcal H_n}$. On $\mathcal H_0$, $T|_{\mathcal H_0}=0=C_0-D_0$. Thus $C_0=D_0$. But $0=C_0D_0=C_0^2$. Thus $0=\langle C_0^2h,h\rangle=\|C_0h\|^2$, so $C_0=0=A|_{\mathcal H_0}$ and $D_0=0=B|_{\mathcal H_0}$. Therefore $C=A$ and $D=B$. ■

Positive operators are analogous to positive numbers. With this in mind, the next result seems reasonable.

**7.16. Theorem.** *If $T$ is a positive compact operator, then there is a unique positive compact operator $A$ such that $A^2=T$.*

**Proof.** Let $T=\sum_{n=1}^{\infty}\lambda_nP_n$ as in the Spectral Theorem. Since $T\geq 0$, $\lambda_n>0$ for all $n$ (7.14). Let $\phi(\lambda_n)=\lambda_n^{1/2}$ and $\phi(z)=0$ otherwise; put $A=\phi(T)$. It is easy to check that $A\geq 0$; $A=\sum_{1}^{\infty}\lambda_n^{1/2}P_n$ so that $A$ is compact; and $A^2=T$. The proof of uniqueness is left to the reader. ■

**Exercises**

1. If $\{P_n\}$ is a sequence of pairwise orthogonal nonzero projections and $P=\sum P_n$, show that $\left\|P-\sum_{j=1}^{n}P_j\right\|=1$ for all $n$.

2. If $\mathcal H$ is separable, show that the definitions of a diagonalizable operator in (4.6) and (7.3) are equivalent.



   <a id="pdf-page-74"></a>
3. If $A=\sum_i\alpha_iP_i$ as in (7.3), show that $A$ is compact if and only if: (a) $\alpha_i=0$ for all but a countable number of $i$; (b) $P_i$ has finite rank whenever $\alpha_i\ne0$; (c) if $\{\alpha_1,\alpha_2,\ldots\}=\{\alpha_i:\alpha_i\ne0\}$, then $\alpha_n\to0$ as $n\to\infty$.

4. Prove Proposition 7.4.

5. If $A=\bigoplus_i\alpha_iP_i$, show that $A^*=\bigoplus_i\bar\alpha_iP_i$, $A$ is normal, and $\|A\|=\sup\{|\alpha_i|:i\in I\}$.

6. Give the remaining details in the proof of (7.6).

7. If $A\in\mathcal B(\mathcal H)$ and $AT=TA$ for every compact operator $T$, show that $A$ is a multiple of the identity operator.

8. Suppose $T$ is a compact normal operator on a $\mathbb C$-Hilbert space such that $\dim\ker(T-\lambda)\leq1$ for all $\lambda$ in $\mathbb C$. Show that if $A\in\mathcal B(\mathcal H)$ and $AT=TA$, then $A=\phi(T)$ for some $\phi$ in $l^\infty(\mathbb C)$.

9. Prove a converse to Exercise 8: if $T$ is a compact normal operator such that $\{A\in\mathcal B(\mathcal H):AT=TA\}=\{\phi(T):\phi\in l^\infty(\mathbb C)\}$, then $\dim\ker(T-\lambda)\leq1$ for all $\lambda$ in $\mathbb C$.

10. Let $T$ be a compact normal operator and show that $\dim\ker(T-\lambda)\leq1$ for all $\lambda$ in $\mathbb C$ if and only if there is a vector $h$ in $\mathcal H$ such that $\{p(T)h:p\text{ is a polynomial in one variable}\}$ is dense in $\mathcal H$. (Such a vector $h$ is called a *cyclic vector* for $T$.)

11. If $\lambda\in\mathbb C$, let $\delta_\lambda$ be the unit point mass at $\lambda$; that is, $\delta_\lambda$ is the measure on $\mathbb C$ such that $\delta_\lambda(\Delta)=1$ if $\lambda\in\Delta$ and $\delta_\lambda(\Delta)=0$ if $\lambda\notin\Delta$. If $\{\lambda_1,\lambda_2,\ldots\}$ is a bounded sequence of distinct complex numbers and $\{\alpha_n\}$ is a sequence of real numbers with $\alpha_n>0$ and $\sum_n\alpha_n<\infty$, let $\mu=\sum_{n=1}^{\infty}\alpha_n\delta_{\lambda_n}$; so $\mu$ is a finite measure. If $\phi\in l^\infty(\mathbb C)$, let $M_\phi$ be the multiplication operator on $L^2(\mu)$. Define $T:L^2(\mu)\to L^2(\mu)$ by $(Tf)(\lambda_n)=\lambda_nf(\lambda_n)$. Prove: (a) $T$ is a normal operator; (b) $T$ has a cyclic vector (see Exercise 10); (c) if $A\in\mathcal B(\mathcal H)$ and $AT=TA$, then $A=M_\phi$ for some $\phi$ in $l^\infty(\mathbb C)$; (d) $T$ is compact if and only if $\lambda_n\to0$. (e) If $T$ is compact, find all of the cyclic vectors for $T$. (f) If $T$ is compact, find the decomposition (7.7) for $T$.

12. Using the notation of Theorem 7.11, give necessary and sufficient conditions on $T$ and $\phi$ that $\phi(T)$ be compact. (Hint: consider separately the cases where $\ker T$ is finite or infinite dimensional.)

13. Prove the uniqueness part of Theorem 7.16.

14. If $T\in\mathcal B(\mathcal H)$, show that $T^*T\geq0$.

15. Let $T$ be a compact normal operator and show that there is a compact positive operator $A$ and a unitary operator $U$ such that $T=UA=AU$. discuss the uniqueness of $A$ and $U$.

16. (*Polar decomposition of compact operators.*) Let $T\in\mathcal B_0(\mathcal H)$ and let $A$ be the unique positive square root of $T^*T$ [(7.16) and Exercise 14]. (a) Show that $\|Ah\|=\|Th\|$ for all $h$ in $\mathcal H$. (b) Show that there is a unique operator $U$ such that $\|Uh\|=\|h\|$ when $h\perp\ker T$, $Uh=0$ when $h\in\ker T$, and $UA=T$. (c) If $U$ and $A$ are as in (a) and (b), show that $T=AU$ if and only if $T$ is normal.

17. Prove the following uniqueness statement for the functional calculus (7.11). If $T$ is a compact normal operator on a $\mathbb C$-Hilbert space $\mathcal H$ and $\tau:l^\infty(\mathbb C)\to\mathcal B(\mathcal H)$ is



<a id="pdf-page-75"></a>
a multiplicative linear map such that $\|\tau(\phi)\|=\sup\{|\phi(\lambda)|:\lambda\in\sigma_p(T)\}$, $\tau(1)=1$, and $\tau(\psi)=T$ whenever $\psi(z)=z$ on $\sigma_p(T)\cup\{0\}$, then $\tau(\phi)=\phi(T)$ for every $\phi$ in $l^\infty(\mathbb C)$.

## §8*. Unitary Equivalence for Compact Normal Operators

In Section I.5 the concept of an isomorphism between Hilbert spaces was defined as the natural equivalence relation on Hilbert spaces. This equivalence relation between the spaces induces a natural equivalence relation between the operators on the spaces.

**8.1. Definition.** If $A,B$ are bounded operators on Hilbert spaces $\mathcal H,\mathcal K$, then $A$ and $B$ are *unitarily equivalent* if there is an isomorphism $U:\mathcal H\to\mathcal K$ such that $UAU^{-1}=B$. In symbols this is denoted by $A\cong B$.

Some of the elementary properties of unitary equivalence are contained in Exercises 1 and 2. Note that if $UAU^{-1}=B$, then $UA=BU$.

The purpose of this section is to give necessary and sufficient conditions that two compact normal operators be unitarily equivalent. Later, in Section IX.10, necessary and sufficient conditions that any two normal operators be unitarily equivalent are given and the results of this section are subsumed by those of that section.

**8.2. Definition.** If $T$ is a compact operator, the *multiplicity function* for $T$ is the cardinal number valued function $m_T$ defined for every complex number $\lambda$ by $m_T(\lambda)=\dim\ker(T-\lambda)$.

Hence $m_T(\lambda)\geq 0$ for all $\lambda$ and $m_T(\lambda)>0$ if and only if $\lambda$ is an eigenvalue for $T$. Note that by Proposition 4.13, $m_T(\lambda)<\infty$ if $\lambda\neq 0$.

If $T,S$ are compact operators on Hilbert spaces and $U:\mathcal H\to\mathcal K$ is an isomorphism with $UTU^{-1}=S$, then $U\ker(T-\lambda)=\ker(S-\lambda)$ for every $\lambda$ in $\mathbb C$. In fact, if $Th=\lambda h$, then $SUh=UTh=\lambda Uh$ and so $Uh\in\ker(S-\lambda)$. Conversely, if $k\in\ker(S-\lambda)$ and $h=U^{-1}k$, then $Th=TU^{-1}k=U^{-1}Sk=\lambda h$. In particular, it must be that $m_T=m_S$. If $S$ and $T$ are normal, this condition is also sufficient for unitary equivalence.

**8.3. Theorem.** *Two compact normal operators are unitarily equivalent if and only if they have the same multiplicity function.*

**Proof.** Let $T,S$ be compact normal operators on Hilbert spaces $\mathcal H,\mathcal K$. If $T\cong S$, then it has already been shown that $m_T=m_S$. Suppose now that $m_T=m_S$. We must manufacture a unitary operator $U:\mathcal H\to\mathcal K$ such that $UTU^{-1}=S$.

Let $T=\sum_{n=1}^{\infty}\lambda_nP_n$ and let $S=\sum_{n=1}^{\infty}\mu_nQ_n$ as in the Spectral Theorem (7.6). So if $n\neq m$, then $\lambda_n\neq\lambda_m$ and $\mu_n\neq\mu_m$, and each of the projections $P_n$ and $Q_n$



<a id="pdf-page-76"></a>
§8. Unitary Equivalence for Compact Normal Operators　61

has finite rank. Let $P_0,Q_0$ be the projections of $\mathcal H,\mathcal K$ onto $\ker T,\ker S$; so $P_0=(\sum_1^\infty P_n)^\perp$ and $Q_0=(\sum_1^\infty Q_n)^\perp$. Put $\lambda_0=\mu_0=0$.

Since $m_T=m_S$, $0<m_T(\lambda_n)=m_S(\lambda_n)$. Hence there is a unique $\mu_j$ such that $\mu_j=\lambda_n$. Define $\pi:\mathbb N\to\mathbb N$ by letting $\mu_{\pi(n)}=\lambda_n$. Let $\pi(0)=0$. Note that $\pi$ is one-to-one. Also, since $0<m_S(\mu_n)=m_T(\mu_n)$, for every $n$ there is a $j$ such that $\pi(j)=n$. Thus $\pi:\mathbb N\cup\{0\}\to\mathbb N\cup\{0\}$ is a bijection or permutation. Since $\dim P_n=m_T(\lambda_n)=m_S(\mu_{\pi(n)})=\dim Q_{\pi(n)}$, there is an isomorphism $U_n:P_n\mathcal H\to Q_{\pi(n)}\mathcal K$ for $n\geq 0$. Define $U:\mathcal H\to\mathcal K$ by letting $U=U_n$ on $P_n\mathcal H$ and extending by linearity. Hence $U=\bigoplus_{n=0}^{\infty}U_n$. It is easy to check that $U$ is an isomorphism. Also, if $h\in P_n\mathcal H$, $n\geq 0$, then $UTh=\lambda_nUh=\mu_{\pi(n)}Uh=SUh$. Hence $UTU^{-1}=S$. ■

If $V$ is the Volterra operator, then $m_V\equiv 0$ (4.11) and $V$ and the zero operator are definitely not unitarily equivalent, so the preceding theorem only applies to compact normal operators. There are no known necessary and sufficient conditions for two arbitrary compact operators to be unitarily equivalent. In fact, there are no known necessary and sufficient conditions that two arbitrary operators on a finite-dimensional space be unitarily equivalent.

## EXERCISES

1. Show that “unitary equivalence” is an equivalence relation on $\mathcal B(\mathcal H)$.

2. Let $U:\mathcal H\to\mathcal K$ be an isomorphism and define $\rho:\mathcal B(\mathcal H)\to\mathcal B(\mathcal K)$ by $\rho(A)=UAU^{-1}$. Prove: (a) $\|\rho(A)\|=\|A\|$, $\rho(A^*)=\rho(A^*)$, and $\rho$ is an isomorphism between the two algebras $\mathcal B(\mathcal H)$ and $\mathcal B(\mathcal K)$. (b) $\rho(A)\in\mathcal B_0(\mathcal K)$ if and only if $A\in\mathcal B_0(\mathcal H)$. (c) If $T\in\mathcal B(\mathcal H)$, then $AT=TA$ if and only if $\rho(T)\rho(A)=\rho(A)\rho(T)$. (d) If $A\in\mathcal B(\mathcal H)$ and $\mathcal M\leq\mathcal H$, then $\mathcal M$ is invariant (reducing) for $A$ if and only if $U\mathcal M$ is invariant (reducing) for $\rho(A)$.

3. Say that an operator $A$ on $\mathcal H$ is *irreducible* if the only reducing subspaces for $A$ are $(0)$ and $\mathcal H$. Prove: (a) The Volterra operator is irreducible. (b) The unilateral shift is irreducible.

4. Suppose $A=\bigoplus\{A_i:i\in I\}$ and $B=\bigoplus\{B_i:i\in I\}$ where each $A_i$ and $B_i$ is irreducible (Exercise 3). Show that $A\cong B$ if and only if there is a bijection $\pi:I\to I$ such that $A_i\cong B_{\pi(i)}$.

5. If $T$ is a compact normal operator and $m_T=m$ is its multiplicity function, prove: (a) $\{\lambda:m(\lambda)>0\}$ is countable and $0$ is its only possible cluster point; (b) $m(\lambda)<\infty$ if $\lambda\ne 0$. Show that if $m:\mathbb C\to\mathbb N\cup\{0,\infty\}$ is any function satisfying (a) and (b), then there is a compact normal operator $T$ such that $m_T=m$.

6. Show that two projections $P$ and $Q$ are unitarily equivalent if and only if $\dim(\operatorname{ran}P)=\dim(\operatorname{ran}Q)$ and $\dim(\ker P)=\dim(\ker Q)$.

7. Let $A:L^2(0,1)\to L^2(0,1)$ be defined by $(Af)(x)=xf(x)$ for $f$ in $L^2(0,1)$ and $x$ in $(0,1)$. Show that $A\cong A^2$.

8. Say that a compact normal operator $T$ is *simple* if $m_T\leq 1$. (See Exercises 7.10 and 7.11.) Show that every compact normal operator $T$ on a separable Hilbert



   <a id="pdf-page-77"></a>
   space is unitarily equivalent to $\bigoplus_{n=1}^{\infty}T_n$, where each $T_n$ is a simple compact normal operator and $m_{T_n}\geq m_{T_{n+1}}$ for all $n$. Show that $\|T_n\|\to 0$. (Of course, there may only be a finite number of $T_n$.)

9. Using the notation of Exercise 8, suppose also that $S$ is a compact normal operator and $S\cong\bigoplus_{n=1}^{\infty}S_n$, where $S_n$ is a simple compact normal operator and $m_{S_n}\geq m_{S_{n+1}}$ for all $n$. Show that $T\cong S$ if and only if $T_n\cong S_n$ for all $n$.

10. If $T$ is a compact normal operator on a separable Hilbert space, show that there are simple compact normal operators $T_1,T_2,\ldots$ such that $T\cong 0\oplus T_1\oplus T_2^{(2)}\oplus T_2^{(3)}\oplus\cdots$, where: (a) for any operator $A$, $A^{(n)}\equiv A\oplus\cdots\oplus A$ ($n$ times); (b) $0$ is the zero operator on an infinite dimensional space; (c) for $n\ne k$, $m_{T_n}m_{T_k}\equiv 0$; and (d) if $\ker T$ is infinite dimensional, then $\ker T_n=(0)$ for all $n$. (Of course not all of the summands need be present.) Show that $\|T_n\|\to 0$.

11. Using the notation of Exercise 10, let $S$ be a compact normal operator and let $0\oplus S_1\oplus S_2^{(2)}\oplus\cdots$ be the corresponding decomposition. Show that $T\cong S$ if and only if $T_n\cong S_n$ and $\ker T$ and $\ker S$ have the same dimension.

12. If $T$ is a non-zero compact normal operator, show that $T$ and $T\oplus T$ are not unitarily equivalent.

13. Give an example of a nontrivial operator $T$ such that $T\cong T\oplus T$. Show that if $T\cong T\oplus T$, then $T\cong T\oplus T\oplus\cdots$. Characterize the diagonalizable normal operators $T$ such that $T\cong T\oplus T$.

14. Let $\mathscr H$ be the space defined in Example I.1.8 and let $U:\mathscr H\to L^2(0,1)$ be the isomorphism defined by $Uf=f'$ (Exercise I.1.4). If $(Af)(x)=xf(x)$ for $f$ in $\mathscr H$, what is $UAU^{-1}$?

<!-- BEGIN SOLUTIONS II -->
<a id="exercise-solutions"></a>
## Exercise Solutions

These added English study solutions cover all 97 numbered exercises in §§1–8,
including the 17 exercises under the differently formatted heading in §7.
`Solution II.s.n` refers to Exercise n of §s. Inner products are linear in the
first variable. Unless explicitly called an idempotent, a projection is an
orthogonal projection. Statements involving complex spectral theory use complex
Hilbert spaces. An empty direct sum means the zero space.

Editorial qualifications are part of the solutions, not alterations of the
source. In particular, II.1.11 needs an outer square root; II.4.12 has a Fourier
sign mismatch; II.6.1(b) has no ordinary inverse Green function; II.7.17 needs
an additional hypothesis; and the converse in II.8.5 needs bounded support.
These points are explained rather than used as unproved assertions.

### §1. Elementary Properties and Examples

#### Solution II.1.1 — Continuity and boundedness of a linear map

Continuity everywhere implies continuity at zero and at some point. If $A$
is continuous at $x_0$, then $Ah=A(x_0+h)-Ax_0\to0$ as $h\to0$, so it is
continuous at zero. Choose $\delta>0$ such that $\|u\|<\delta$ implies
$\|Au\|<1$. For $h\ne0$, apply this to $u=\delta h/(2\|h\|)$ to get
$\|Ah\|\leq(2/\delta)\|h\|$; it also holds at zero. Conversely such a
bound gives $\|Ax-Ay\|\leq c\|x-y\|$, proving continuity everywhere.
This proves all four equivalences. Normalizing nonzero vectors gives the
sphere and ratio formulas for the norm; a number bounds all these ratios
exactly when it is an admissible operator bound. Taking their supremum also
proves $\|Ah\|\leq\|A\|\|h\|$. On the zero space use norm zero.

#### Solution II.1.2 — The operator-norm inequalities

All three operators are linear by expansion. For every $h$,
$\|(A+B)h\|\leq(\|A\|+\|B\|)\|h\|$,
$\|\alpha Ah\|=|\alpha|\|Ah\|$, and
$\|BAh\|\leq\|B\|\|A\|\|h\|$. These bounds prove boundedness and,
on taking the supremum over the unit ball, give (a), the equality in (b),
and (c). Norm zero forces $Ah=0$ for all $h$, so together with these
inequalities the operator norm really is a norm.

#### Solution II.1.3 — Extending prescribed basis images

Write $v_n=Ae_n$ and $C=\sum_n\|v_n\|<\infty$. On finite linear
combinations define $A_0(\sum a_ne_n)=\sum a_nv_n$. Uniqueness of basis
coordinates makes this well defined, and $|a_n|\leq\|\sum a_je_j\|$ gives
$\|A_0h\|\leq C\|h\|$. For general $h$, its finite basis truncations
$h_N$ converge to $h$, and $(A_0h_N)$ is Cauchy by that bound. Define
$Ah=\lim_NA_0h_N$. Taking limits proves linearity and the same bound.
Any bounded extension must take these same limits, so it is unique.

#### Solution II.1.4 — Completeness of the operator space

Let $(A_n)$ be Cauchy in operator norm. For each $h$, the bound
$\|A_nh-A_mh\|\leq\|A_n-A_m\|\|h\|$ makes $(A_nh)$ Cauchy in the
complete codomain. Put $Ah=\lim_nA_nh$. Taking limits proves linearity;
since $\sup_n\|A_n\|=C<\infty$, it also gives $\|Ah\|\leq C\|h\|$.
Given $\varepsilon>0$, choose $N$ with $\|A_n-A_m\|\leq\varepsilon$
for $m,n\geq N$. Letting $m\to\infty$ yields
$\|(A_n-A)h\|\leq\varepsilon\|h\|$, hence $\|A_n-A\|\leq\varepsilon$.
Thus the convergence is in operator norm, not just at individual vectors.

#### Solution II.1.5 — Idempotent multiplication

$M_\phi^2-M_\phi=M_{\phi^2-\phi}$. The multiplication norm formula,
valid under the sigma-finiteness in (1.5), shows this is zero exactly when
$\phi^2-\phi=0$ almost everywhere. The scalar equation $z(z-1)=0$ says
$z\in\{0,1\}$. Consequently $\phi=\mathbf1_E$ almost everywhere for
the measurable set $E=\{\phi=1\}$. Conversely such a symbol plainly
gives an idempotent. The assertion concerns equivalence classes, so it is
not a claim about values on null sets.

#### Solution II.1.6 — Composition of kernel operators

Let the row and column bounds of $k_j$ be $r_j,c_j$, respectively.
Tonelli gives

$$
\int\!\int |k_1(x,z)k_2(z,y)|\,d\mu(z)d\mu(y)
\leq r_2\int|k_1(x,z)|\,d\mu(z)\leq r_1r_2
$$

for almost every $x$. Similarly the column integral is bounded by $c_1c_2$.
Thus the defining integral exists almost everywhere on the product; set it
to zero on the exceptional measurable null set. Parameter integration gives
a measurable representative $k$ satisfying the two required bounds.

For $f\in L^2$, apply the same argument to the positive composed kernel
$\widetilde k(x,y)=\int|k_1(x,z)k_2(z,y)|\,d\mu(z)$. Schur's estimate
shows $\int\widetilde k(x,y)|f(y)|\,d\mu(y)$ is finite for almost every
$x$. Fubini is therefore legitimate in the following calculation:

$$
(K_1K_2f)(x)=\int k_1(x,z)\left(\int k_2(z,y)f(y)\,d\mu(y)\right)d\mu(z)
=\int k(x,y)f(y)\,d\mu(y).
$$

So $K=K_1K_2$. For counting measure this is literally matrix multiplication,
$k_{ij}=\sum_\ell(k_1)_{i\ell}(k_2)_{\ell j}$; it is more than a formal
analogy, since matrices are integral kernels on discrete measure spaces.

#### Solution II.1.7 — Square-integrable kernels

First suppose the measure is sigma-finite. For almost every $x$,
Cauchy–Schwarz gives

$$
|Kf(x)|^2\leq\left(\int|k(x,y)|^2\,d\mu(y)\right)\|f\|_2^2.
$$

Fubini applied to $|k|^2$ then proves that $Kf$ is defined almost everywhere,
measurable, and $\|Kf\|_2\leq\|k\|_{L^2(\mu\times\mu)}\|f\|_2$.
The estimate on a difference proves independence of representatives.

For the arbitrary measure space as printed, specify the usual outer-measure
product constructed by countable measurable-rectangle covers. Here the same
proof localizes to sigma-finite subsets. Indeed each finite-product-measure
set has a countable rectangle cover with finite total cost. Every rectangle
of positive cost has both factors of finite measure; every zero-cost rectangle
has at least one null factor. Applied to the sets $\{|k|>1/n\}$, these
covers put $k$, modulo a countable union of zero-cost rectangles, inside
$S\times S$ for a sigma-finite measurable $S\subset X$. On those zero-cost
rectangles the sections vanish almost everywhere except possibly at a null
set of $x$'s. Replace $k$ by its restriction to $S\times S$, perform the
sigma-finite calculation, and extend the output by zero. This proves the
claim for that product convention without assuming all of $X$ sigma-finite.
An unspecified extension agreeing only on rectangle measures must not be
silently substituted; see the product-measure qualification in II.4.14.

#### Solution II.1.8 — Bounded diagonal operators

Necessity follows from $|\alpha_n|=\|Ae_n\|\leq\|A\|$. If
$M=\sup_n|\alpha_n|<\infty$, define $A(a_n)=(\alpha_na_n)$. Then
$\|Aa\|^2\leq M^2\sum|a_n|^2$, so $A$ is bounded with norm at most
$M$. Testing on each $e_n$ gives the opposite inequality and hence equality.
Continuity and density of finite sequences show this is the unique operator
with the prescribed images.

#### Solution II.1.9 — Schur's weighted test

For a finite-support sequence $x$, weighted Cauchy–Schwarz gives

$$
\left|\sum_j\alpha_{ij}x_j\right|^2
\leq\left(\sum_j\alpha_{ij}p_j\right)
       \left(\sum_j\alpha_{ij}\frac{|x_j|^2}{p_j}\right)
\leq\gamma p_i\sum_j\alpha_{ij}\frac{|x_j|^2}{p_j}.
$$

Summing in $i$ and interchanging nonnegative sums yields
$\sum_i|(Ax)_i|^2\leq\gamma\sum_j(|x_j|^2/p_j)
\sum_i p_i\alpha_{ij}\leq\beta\gamma\|x\|_2^2$.
The dense-domain extension argument in II.1.3 therefore supplies a bounded
operator with the required matrix and $\|A\|^2\leq\beta\gamma$.

#### Solution II.1.10 — The Hilbert matrix bound

Use $p_j=(j+1/2)^{-1/2}$ for $j\geq0$. Fix $a=i+1/2>0$ and let
$F_a(x)=x^{-1/2}/(a+x)$ on $x>0$. It is convex: both factors are positive,
decreasing, and strictly convex, so the three terms in its product-rule
second derivative are positive. Convexity gives the midpoint bound
$F_a(j+1/2)\leq\int_j^{j+1}F_a(x)\,dx$ (also for $j=0$ by an improper
limit). Consequently

$$
\sum_{j\geq0}\frac{p_j}{i+j+1}
\leq\int_0^\infty\frac{dx}{\sqrt x(a+x)}
=\frac{\pi}{\sqrt a}=\pi p_i.
$$

The substitution $x=at^2$ evaluates the integral as
$2a^{-1/2}\int_0^\infty(1+t^2)^{-1}dt$. The matrix is symmetric, so
the column bound is identical. II.1.9 with $\beta=\gamma=\pi$ gives
$\|A\|\leq\pi$.

#### Solution II.1.11 — Correcting the 2-by-2 norm formula

The displayed expression in the question is $\|A\|^2$, not $\|A\|$.
For instance $A=2I$ makes that expression four but the norm is two.
To derive the correct formula, put $B=A^*A$. It is a positive Hermitian
matrix with trace $\alpha^2$ and determinant $\delta^2$. Its characteristic
polynomial is $t^2-\alpha^2t+\delta^2$, so its eigenvalues are
$t_\pm=(\alpha^2\pm\sqrt{\alpha^4-4\delta^2})/2$.
Unitary diagonalization shows $\sup_{\|x\|=1}\langle Bx,x\rangle=t_+$.
Since $\|Ax\|^2=\langle Bx,x\rangle$, the answer is

$$
\boxed{\displaystyle\|A\|=
\sqrt{\frac{\alpha^2+\sqrt{\alpha^4-4\delta^2}}{2}}.}
$$

#### Solution II.1.12 — Direct sums of operators

Restricting any proposed bounded $A$ to the isometric copy of
$\mathcal H_i$ gives $\|A_i\|\leq\|A\|$. Conversely, for
$M=\sup_i\|A_i\|<\infty$, define $A(h_i)=(A_ih_i)$. Then
$\sum_i\|A_ih_i\|^2\leq M^2\sum_i\|h_i\|^2$; hence this is a
bounded operator on the Hilbert direct sum. It has norm at most $M$,
and the restriction inequality proves equality. Finite-component vectors
are dense, so its restrictions determine it uniquely.

#### Solution II.1.13 — Bessel sequences and the Gram operator

The definition initially asserts finiteness separately for each $f$; a
uniform bound must be proved. Put
$F_Nf=(\langle f,f_1\rangle,\ldots,\langle f,f_N\rangle)$, padded with
zeros in $\ell^2$. Each $F_N$ is bounded and $\sup_N\|F_Nf\|<\infty$.
Here is the uniform-boundedness argument. The closed sets
$E_m=\{f:\sup_N\|F_Nf\|\leq m\}$ cover the complete space.
By the Baire theorem proved in Solution I.4.16, some $E_m$ contains a
ball $B(f_0,r)$. Subtracting values at $f_0+h$ and $f_0$ shows
$\|F_Nh\|\leq2m$ for $\|h\|<r$, uniformly in $N$. Scaling gives
$\sup_N\|F_N\|<\infty$. Therefore the analysis map
$Ff=(\langle f,f_n\rangle)_n$ is bounded.

Its adjoint is the synthesis map $S=F^*$, with $Se_n=f_n$.
The matrix entries of $S^*S$ are
$\langle S^*Se_j,e_i\rangle=\langle f_j,f_i\rangle$.
Thus the usual Gram matrix is bounded. If the printed matrix
$(\langle f_m,f_n\rangle)$ uses $m$ as the row index instead, it is its
transpose: the two are related by coordinate conjugation and have the same
boundedness and norm.
Conversely assume this Gram matrix defines a bounded operator $G$, using
the entry convention $G_{ij}=\langle f_j,f_i\rangle$. For finite $a$,
$\|\sum_j a_jf_j\|^2=\langle Ga,a\rangle\leq\|G\|\|a\|^2$.
Synthesis therefore extends boundedly to $\ell^2$, and its adjoint has
coordinates $\langle f,f_n\rangle$. They are square summable for every
$f$, as required.

### §2. The Adjoint of an Operator

#### Solution II.2.1 — Unitary inverses and adjoints

If $U$ is an onto isometry, polarization shows
$\langle Uh,Ug\rangle=\langle h,g\rangle$. Thus $U^*U=I$; surjectivity
then gives $UU^*=I$ and $U^*=U^{-1}$. Conversely these inverse identities
give $\|Uh\|^2=\langle U^*Uh,h\rangle=\|h\|^2$, and invertibility
already gives surjectivity. The inverse is bounded, being an isometry.

#### Solution II.2.2 — Algebraic rules for adjoints

(a) For all $h,g$,
$\langle(\alpha A+B)h,g\rangle
=\langle h,(\overline\alpha A^*+B^*)g\rangle$.
(b) Similarly $\langle ABh,g\rangle=\langle h,B^*A^*g\rangle$.
Uniqueness of adjoints proves both formulas. (c) Conjugate the identity
$\langle Ag,h\rangle=\langle g,A^*h\rangle$ to obtain the defining
identity for $(A^*)^*=A$. (d) Apply (b) to $AA^{-1}=A^{-1}A=I$;
it gives both inverse identities for $A^*$ and $(A^{-1})^*$.

#### Solution II.2.3 — Adjoint of multiplication

For $f,g\in L^2$, Cauchy–Schwarz makes all integrals finite and
$\langle M_\phi f,g\rangle=\int\phi f\overline g
=\int f\overline{\overline\phi g}=\langle f,M_{\overline\phi}g\rangle$.
The proposed adjoint is bounded since $\overline\phi\in L^\infty$.
Therefore $M_\phi^*=M_{\overline\phi}$.

#### Solution II.2.4 — Adjoint of a kernel operator

The row and column bounds interchange for
$k^*(x,y)=\overline{k(y,x)}$, so this defines a bounded operator.
To justify exchanging integrals, weighted Cauchy–Schwarz on the product gives

$$
\iint|k(x,y)f(y)\overline{g(x)}|\,d\mu(y)d\mu(x)
\leq(c_2\|f\|_2^2)^{1/2}(c_1\|g\|_2^2)^{1/2}.
$$

Fubini then gives $\langle Kf,g\rangle=\langle f,K^*g\rangle$ with the
stated kernel. For arbitrary measures one can first restrict $x,y$ to the
sigma-finite supports of $g,f$; the equality defines the same bounded
adjoint wherever the kernel operators in (1.6) are defined. This avoids an
unjustified global use of sigma-finite Fubini.

#### Solution II.2.5 — Adjoint of a diagonal operator

If $Ae_n=\alpha_ne_n$, then
$A^*(a_n)=(\overline\alpha_na_n)$, as follows by substituting into
$\sum\alpha_na_n\overline{b_n}$ and conjugating the second argument.
The sequence of conjugate entries has the same bound, so this formula
defines a bounded operator on all of $\ell^2$.

#### Solution II.2.6 — Shift identities

For $S(a_1,a_2,\ldots)=(0,a_1,a_2,\ldots)$, its adjoint is
$S^*(a_1,a_2,\ldots)=(a_2,a_3,\ldots)$. Thus $S^*S=I$ and
$SS^*=I-P_1$, where $P_1$ projects onto $\mathbb Fe_1$.
Iterating, $S^{*n}S^n=I$ and $S^nS^{*n}=I-P_n$, with $P_n$ the
projection onto $\operatorname{span}(e_1,\ldots,e_n)$. These identities
can also be read off by deleting and then inserting $n$ initial coordinates.

#### Solution II.2.7 — The Volterra adjoint

The transposed kernel is $\mathbf1_{\{x<y\}}$, so
$(V^*f)(x)=\int_x^1f(y)\,dy$. Therefore
$((V+V^*)f)(x)=\int_0^1f(y)\,dy=\langle f,1\rangle1$.
Its range is the one-dimensional subspace of constant functions; it is
exactly the orthogonal projection onto that subspace because $\|1\|_2=1$.

#### Solution II.2.8 — Where complex scalars are needed

The proof uses $\alpha=i$ after $\alpha=1$ to separate the two mixed
inner-product terms. Over $\mathbb R$ only their sum is determined by
the diagonal quadratic form. In fact every real inner product is real,
so that hypothesis is automatic for every real operator. The matrix
$\begin{bmatrix}0&1\\-1&0\end{bmatrix}$ is nonzero skew-adjoint and has
$\langle Ah,h\rangle=0$ for all real $h$; it is not self-adjoint.

#### Solution II.2.9 — Real and imaginary Hermitian parts

Taking adjoints of $A=B+iC$ gives $A^*=B-iC$, since $B^*=B$ and $C^*=C$.
Adding and subtracting yields $B=(A+A^*)/2$ and $C=(A-A^*)/(2i)$.
These expressions are themselves self-adjoint by the adjoint rules, so
they prove existence as well as uniqueness of this decomposition.

#### Solution II.2.10 — A zero quadratic form

Let $b(h,g)=\langle Ah,g\rangle$. Expanding the hypothesis at $h+g$
gives $b(h,g)+b(g,h)=0$. Expanding at $h+ig$ gives
$-ib(h,g)+ib(g,h)=0$. Solving gives $b(h,g)=0$ for all $h,g$.
Choose $g=Ah$ to obtain $\|Ah\|^2=0$. Hence $A=0$, proving 2.15.
Again the complex test vector is essential.

#### Solution II.2.11 — Products of self-adjoint operators

Since $(AB)^*=B^*A^*=BA$, the equality $(AB)^*=AB$ is equivalent to
$BA=AB$. Both directions follow from this identity; no claim that arbitrary
products of self-adjoint operators remain self-adjoint is valid.

#### Solution II.2.12 — Substituting an operator in a power series

Choose $r$ with $\|A\|<r<R$ (or any larger finite $r$ if $R=\infty$).
Absolute convergence of the scalar power series gives
$\sum_n|\alpha_n|\|A\|^n<\infty$. Since $\|A^n\|\leq\|A\|^n$,
the operator series $T=\sum_n\alpha_nA^n$ is Cauchy in operator norm and
converges by II.1.4. For fixed $h,g$, the functional
$B\mapsto\langle Bh,g\rangle$ is continuous with bound $\|h\|\|g\|$.
Applying it to partial sums gives the requested identity. It also shows
uniqueness: identical matrix elements determine an operator.

#### Solution II.2.13 — Norm convergence and the commutant

The stronger estimate
$\|T-\sum_{k=0}^n\alpha_kA^k\|\leq\sum_{k>n}|\alpha_k|\|A\|^k\to0$
follows from the same proof. If $BA=AB$, induction gives $BA^k=A^kB$,
so $B$ commutes with every partial sum. Left and right multiplication by
$B$ are norm-continuous, both with bound $\|B\|$, so passing to the limit
gives $BT=TB$.

#### Solution II.2.14 — Exponentials of skew-adjoint operators

Norm convergence and the adjoint rules give $(e^{iA})^*=e^{-iA}$ when
$A=A^*$. Absolute convergence permits multiplying the two operator series
and grouping by total degree. The coefficient in degree $n>0$ is
$\sum_{k=0}^n i^k(-i)^{n-k}/(k!(n-k)!)=0$ by the binomial identity;
degree zero contributes $I$. Thus $e^{iA}e^{-iA}=e^{-iA}e^{iA}=I$.
By II.2.1, $e^{iA}$ is unitary.

#### Solution II.2.15 — Normal kernels and dense range

Normality gives $\|Ah\|^2=\langle A^*Ah,h\rangle
=\langle AA^*h,h\rangle=\|A^*h\|^2$. Hence $\ker A=\ker A^*$.
Also $(\operatorname{ran}A)^\perp=\ker A^*$, since orthogonality to
every $Ax$ is exactly $A^*h=0$. Taking orthogonal complements proves
that $A$ is injective exactly when its range is dense.
The unilateral shift $S$ is injective but its range misses the first
coordinate. Its adjoint $S^*$ is onto, since $S^*S=I$, but
$\ker S^*=\mathbb Fe_1\ne0$. These are the two requested counterexamples.

#### Solution II.2.16 — Closed range of multiplication

Let $Z=\{\phi=0\}$ and $E=X\setminus Z$. The kernel consists precisely
of $L^2$ functions supported on $Z$. Sigma-finiteness shows it is zero
exactly when $\mu(Z)=0$: any positive-measure $Z$ contains a set of
finite positive measure whose indicator is a nonzero kernel vector.
The range is closed exactly when

$$
\text{there exists }c>0\text{ such that }|\phi|\geq c
\text{ almost everywhere on }E.
$$

If this holds, division by $\phi$ on $E$ shows the range is the closed
space of functions vanishing on $Z$. For necessity we give a direct
argument without using the open mapping theorem. If the condition fails,
select disjoint positive-measure sets $E_n\subset E$ on which
$0<|\phi|\leq2^{-n}$, with $0<\mu(E_n)<\infty$; choose successive
nonempty level bands tending to zero and then finite-measure subsets.
Put $u_n=\mathbf1_{E_n}/\sqrt{\mu(E_n)}$ and
$g=\sum_n\phi u_n$. Disjoint supports and the displayed upper bound
make this an $L^2$ sum. Its finite partial sums belong to the range.
Any preimage of $g$, however, must equal $u_n$ on every $E_n$, so its
squared norm is at least $\sum_n1=\infty$. Thus $g$ is in the closure
of the range but not the range, a contradiction to closedness.

### §3. Projections and Idempotents; Invariant and Reducing Subspaces

#### Solution II.3.1 — An oblique projection in the plane

Decompose $(x,y)=(x-y\cot\theta,0)+(y\cot\theta,y)$. The second
vector lies on $\mathcal N$, so
$E_\theta(x,y)=(x-y\cot\theta,0)$ and
$E_\theta=\begin{bmatrix}1&-\cot\theta\\0&0\end{bmatrix}$.
Its square is itself and its range and kernel are exactly those prescribed.
Cauchy–Schwarz gives norm $\sqrt{1+\cot^2\theta}=1/\sin\theta$,
attained on the unit vector proportional to $(1,-\cot\theta)$.
This also shows why a nonorthogonal idempotent need not have norm one.

#### Solution II.3.2 — The range–kernel decomposition of an idempotent

If $x=Ey$ is also in $\ker E$, then $x=E^2y=Ex=0$.
Every $h$ decomposes as $Eh+(I-E)h$, with the first summand in the range
and the second in the kernel because $E(I-E)=0$. Thus their intersection
is zero and their algebraic sum is the whole space, proving 3.2(c).

#### Solution II.3.3 — Orthogonal complements of intersections and spans

A vector is orthogonal to every $\mathcal M_i$ exactly when it is
orthogonal to their algebraic span and, by continuity, to its closure.
This proves $\bigcap_i\mathcal M_i^\perp=(\bigvee_i\mathcal M_i)^\perp$.
Apply this identity to $\mathcal M_i^\perp$ and take orthogonal
complements. Since each $\mathcal M_i$ and their intersection are closed,
the double-complement identity gives
$(\bigcap_i\mathcal M_i)^\perp=\bigvee_i\mathcal M_i^\perp$.

#### Solution II.3.4 — Sums and products of projections

(a) If $P+Q$ is a projection, expanding its square gives $PQ+QP=0$.
For $x\in\operatorname{ran}P$, take the quadratic form to get
$0=2\langle Qx,x\rangle=2\|Qx\|^2$. Thus $QP=0$, and adjoints give
$PQ=0$. This is exactly orthogonality of the ranges. Conversely orthogonal
ranges give these zero products, so the sum is self-adjoint and idempotent.
Its range is their orthogonal sum. The identity
$\|(P+Q)x\|^2=\|Px\|^2+\|Qx\|^2$ gives the stated kernel.

(b) If $PQ$ is a projection, self-adjointness gives $PQ=(PQ)^*=QP$.
Conversely commutation makes $PQ$ self-adjoint and idempotent.
Its range is the intersection, because $PQx$ is fixed by both projections
and every common fixed vector is fixed by their product. If $PQx=0$,
write $x=(I-Q)x+Qx$: the first term is in $\ker Q$ and the second in
$\ker P$. Conversely $PQ$ kills both kernels, using commutation for
$\ker P$. Thus $\ker PQ=\ker P+\ker Q$; in this commuting case this
algebraic sum is closed, since it is a kernel.

#### Solution II.3.5 — Summing orthogonal projections strongly

For finite $F\subset I$, orthogonality gives
$\|\sum_{i\in F}P_ih\|^2=\sum_{i\in F}\|P_ih\|^2\leq\|h\|^2$,
because the finite sum is itself a projection. The supremum of these
nonnegative scalar sums is finite, so tails can be made arbitrarily small.
The same squared-norm identity makes the finite-subset net of vector sums
Cauchy; equivalently enumerate its at most countably many nonzero terms
and use the square-tail estimate to recover unordered convergence.
Let its limit be $v$. It lies in $M=\bigvee_i\mathcal M_i$, and for
each $i$ its projection onto $\mathcal M_i$ is $P_ih$. Thus $h-v$ is
orthogonal to every $\mathcal M_i$ and hence to $M$. The projection
theorem gives $v=Ph$. This is strong convergence, not in general norm
convergence of operators.

#### Solution II.3.6 — Differences of nested projections

If $R=P-Q$ is a projection and $x\in\operatorname{ran}Q$, then
$0\leq\langle Rx,x\rangle=\|Px\|^2-\|x\|^2\leq0$.
Equality implies $(I-P)x=0$, so $\operatorname{ran}Q\subseteq\operatorname{ran}P$.
This containment is equivalent to $PQ=Q$; taking adjoints gives its
equivalence to $QP=Q$. Under these identities, $(P-Q)^2=P-Q$ and the
difference is self-adjoint. This proves all four equivalences.
Its range is precisely the vectors fixed by $P$ and killed by $Q$, namely
$\operatorname{ran}P\ominus\operatorname{ran}Q$. Decomposing
$x=Px+(I-P)x$ shows $Rx=0$ exactly when $Px\in\operatorname{ran}Q$,
which proves $\ker R=\operatorname{ran}Q+\ker P$.

#### Solution II.3.7 — The join of two commuting projections

If $R=P+Q-PQ$ is a projection, its self-adjointness gives
$P+Q-PQ=P+Q-QP$, hence $PQ=QP$. Conversely, for commuting projections,
$I-R=(I-P)(I-Q)$ is a projection by II.3.4(b), so $R$ is too.
The formulas from that solution applied to the complementary projections
give $\ker R=\ker P\cap\ker Q$ and
$\operatorname{ran}R=\operatorname{ran}P+\operatorname{ran}Q$.
One can see the latter directly from $Rx=Px+Q(I-P)x$ and the fact that
$R$ fixes both ranges.

#### Solution II.3.8 — Noncommuting orthogonal projections

On $\mathbb R^2$ or $\mathbb C^2$ take
$P=\begin{bmatrix}1&0\\0&0\end{bmatrix}$ and
$Q=\tfrac12\begin{bmatrix}1&1\\1&1\end{bmatrix}$.
Both are self-adjoint idempotents, but
$PQ=\tfrac12\begin{bmatrix}1&1\\0&0\end{bmatrix}$ whereas
$QP=\tfrac12\begin{bmatrix}1&0\\1&0\end{bmatrix}$.

#### Solution II.3.9 — Sums with a graph subspace

The graph is closed: $h_n\to h$ and $Ah_n\to k$ imply $k=Ah$ by
continuity. Its intersection with $\mathcal H\oplus0$ is
$\{h\oplus0:h\in\ker A\}$, proving (a). Further,

$$
(\mathcal H\oplus0)+\operatorname{graph}A
=\{(x+h)\oplus Ah:x,h\in\mathcal H\}
=\mathcal H\oplus\operatorname{ran}A.
$$

Its closure is $\mathcal H\oplus\overline{\operatorname{ran}A}$,
proving (b); without taking closures the same equality proves (c).

#### Solution II.3.10 — A dense nonclosed sum of closed subspaces

On $H_0=\ell^2$, let $Ae_n=e_n/n$. It is bounded and injective, and its
range contains every finite sequence, so is dense. The vector $(1/n)_n$
lies in $\ell^2$ but has no preimage there, since its only formal preimage
is $(1,1,\ldots)$. In $\mathcal H=H_0\oplus H_0$ choose
$\mathcal M=H_0\oplus0$ and $\mathcal N=\operatorname{graph}A$.
II.3.9 proves that these closed subspaces have zero intersection and a
dense proper sum. Thus closure cannot generally be omitted when summing
closed subspaces.

#### Solution II.3.11 — An invariant half of the bilateral shift

The displayed shift sends $e_j$ to $e_{j+1}$. Hence
$M=\overline{\operatorname{span}}\{e_j:j\geq0\}$ is invariant.
But $A^*e_0=e_{-1}\notin M$, so $M$ is not invariant under the adjoint
and does not reduce $A$. Equivalently $e_{-1}\in M^\perp$ but
$Ae_{-1}=e_0\notin M^\perp$.

#### Solution II.3.12 — Reducing and merely invariant disk subspaces

For $E=\{z:|z|<1/2\}$, the functions supported in $E$ form a nonzero
proper closed subspace of $L^2(\mathbb D)$. Multiplication by $z$ and
by $\overline z=A^*$ preserves support, so this subspace reduces $A$.
The Bergman space $L_a^2(\mathbb D)$ is closed, is nonzero and proper,
and is invariant under multiplication by $z$. It is not reducing:
$1$ belongs to it but $A^*1=\overline z$ is not holomorphic. The latter
can be checked at zero by taking real and imaginary difference quotients,
which give incompatible derivatives. It cannot agree almost everywhere
with a holomorphic function either, since both would be continuous and
thus agree everywhere.

### §4. Compact Operators

#### Solution II.4.1 — The two-sided ideal property

If $(h_n)$ is bounded, then $(Ah_n)$ is bounded, so compactness of $T$
gives a subsequence on which $TAh_n$ converges. This proves $TA$ compact.
Likewise select a subsequence for which $Th_n$ converges; continuity of $B$
makes $BTh_n$ converge. The sequential compactness criterion therefore
proves $BT$ compact. The proof works with the distinct domain and codomain
spaces in 4.2(c).

#### Solution II.4.2 — Finite rank implies compactness

Here a finite-rank operator is bounded, as in the notation
$\mathcal B_{00}$. Its unit-ball image is bounded in the finite-dimensional
space $\operatorname{ran}T$. That space is closed, and closed bounded sets
in it are compact by the finite-dimensional Heine–Borel theorem. Thus
the closure of the image is compact. Without boundedness, an arbitrary
algebraic finite-rank linear transformation need not be continuous or compact.

#### Solution II.4.3 — The rank of an adjoint

Let $M=\operatorname{ran}T$ have finite dimension $r$. Since
$\ker T^*=M^\perp$, $T^*$ vanishes on $M^\perp$ and maps $M$ injectively:
a vector in $M\cap\ker T^*$ must be zero. Decomposing the domain of $T^*$
as $M\oplus M^\perp$ therefore shows
$\operatorname{ran}T^*=T^*M$ has dimension $r$. The adjoint is bounded,
so it too is a finite-rank operator.

#### Solution II.4.4 — Compact idempotents

Finite rank implies compactness by II.4.2. Conversely, if $E^2=E$ is
compact, its range $M=\ker(I-E)$ is closed and $E|_M=I_M$.
The unit ball of $M$ is a closed subset of the compact closure of
$E(\operatorname{ball}\mathcal H)$, so is compact. Solution I.4.19 implies
$M$ is finite dimensional. Orthogonality of $E$ is not needed.

#### Solution II.4.5 — Nonzero multiplication on an interval is not compact

If $M_\phi\ne0$, some $E=\{|\phi|\geq\varepsilon\}$ has positive
Lebesgue measure for an $\varepsilon>0$. Split $E$ into infinitely many
disjoint measurable sets $E_n$ of positive measure. Such a splitting exists
because $t\mapsto |E\cap(0,t)|$ is continuous, letting one repeatedly
bisect positive-measure pieces. The normalized indicators $u_n$ are
orthonormal. Their images have disjoint supports and norms at least
$\varepsilon$, so for $n\ne m$,
$\|M_\phi u_n-M_\phi u_m\|^2\geq2\varepsilon^2$.
There is no convergent image subsequence. This contradicts compactness.

#### Solution II.4.6 — An orthonormal-sequence criterion

For each fixed $g$, Bessel's inequality gives
$\langle Te_n,g\rangle=\langle e_n,T^*g\rangle\to0$.
If $T$ is compact and the norms fail to tend to zero, a subsequence with
norms bounded below has a further norm-convergent image subsequence.
Its limit must have zero inner product with every $g$, hence is zero,
contradicting that lower bound.

The converse is true if the assertion holds for **every** orthonormal
sequence, as the exercise asks. Otherwise, if $T$ were not compact, there
would be $\varepsilon>0$ such that $\|T|_{F^\perp}\|>\varepsilon$ for
every finite-dimensional $F$. Indeed failure of this statement for every
$\varepsilon$ would approximate $T$ in norm by the finite-rank operators
$TP_F$. Recursively choose unit $e_n$ orthogonal to its predecessors with
$\|Te_n\|>\varepsilon$. This contradicts the assumed property.
Testing only one fixed orthonormal basis is weaker and is not sufficient.
For example take the direct sum, over blocks of sizes $n$, of the rank-one
projections onto each block's normalized constant vector. Images of the
coordinate basis tend to zero, but these constant unit vectors are fixed
and form an infinite orthonormal sequence, so the operator is not compact.

#### Solution II.4.7 — Restriction to an invariant closed subspace

Every bounded sequence in $M$ is bounded in $\mathcal H$, so its images
under $T$ have a convergent subsequence in $\mathcal H$. Invariance puts
the images in $M$, and closedness puts their limit there too. The same
subsequence proves compactness of $T|_M:M\to M$. Closedness is part of
the book's meaning of invariant subspace here.

#### Solution II.4.8 — Rank-one and finite-rank formulas

$Tf=\langle f,h\rangle g$ is bounded with norm $\|h\|\|g\|$, by
Cauchy–Schwarz and equality at $f=h/\|h\|$ when $h\ne0$.
Its rank is one provided both $h$ and $g$ are nonzero; if either is zero,
its rank is zero, an exception omitted in the printed wording.
Conversely, if $\operatorname{ran}T=\mathbb Fg$ with $g\ne0$, write
$Tf=L(f)g$, where $L(f)=\langle Tf,g\rangle/\|g\|^2$ is bounded.
Riesz representation writes $L(f)=\langle f,h\rangle$.

For general finite rank, II.4.3 and
$(\ker T)^\perp=\overline{\operatorname{ran}T^*}$ show this complement
has a finite orthonormal basis $e_1,\ldots,e_n$. Put $g_j=Te_j$.
Decompose a vector into this finite span and $\ker T$ to obtain
$Tf=\sum_j\langle f,e_j\rangle g_j$.
If $g_j=\lambda_je_j$, the operator is diagonal on that span and zero
on its orthogonal complement; its adjoint conjugates the diagonal entries,
so it is normal. Its point spectrum is the set of the $\lambda_j$,
together with zero if that complementary space is nonzero (or if some
$\lambda_j=0$). Zero is not automatically an eigenvalue in finite dimension
when all the diagonal entries are nonzero and the span is the entire space.

Without the special condition $g_j=\lambda_je_j$, the nonzero point
spectrum is the nonzero spectrum of the finite matrix
$C_{ij}=\langle g_j,e_i\rangle$. To see this, let $P$ take coordinates
along the $e_j$ and let $S(a_j)=\sum_ja_jg_j$, so $T=SP$ and $C=PS$.
If $Tf=\lambda f$ with $\lambda\ne0$, then $Pf\ne0$ and
$C(Pf)=\lambda Pf$. Conversely, $Ca=\lambda a$ implies $Sa\ne0$
and $T(Sa)=\lambda Sa$. Zero is an eigenvalue exactly when $\ker T\ne0$.
For rank one this says the only possible nonzero eigenvalue is
$\langle g,h\rangle$, with eigenvector $g$ when this scalar is nonzero.

#### Solution II.4.9 — Diagonal operators are normal

On an orthonormal eigenbasis, $Ae_j=\alpha_je_j$ and
$A^*e_j=\overline\alpha_je_j$. Therefore both $A^*A$ and $AA^*$ send
$e_j$ to $|\alpha_j|^2e_j$. Equality on the dense linear span, followed
by continuity, proves equality everywhere. The argument works for an
arbitrarily indexed orthonormal basis as well.

#### Solution II.4.10 — The point spectrum of a diagonal operator

For $h=\sum_jh_je_j$, the equation $Ah=\alpha h$ is equivalent to
$(\alpha_j-\alpha)h_j=0$ for every $j$. Thus a nonzero solution exists
exactly when $\alpha=\alpha_j$ for some $j$. The entire eigenspace is
$\overline{\operatorname{span}}\{e_j:\alpha_j=\alpha\}$.
The word eigenvector excludes its zero vector. A limit of diagonal values
need not itself be an eigenvalue unless it actually occurs among them.

#### Solution II.4.11 — The Volterra operator has no eigenvalues

If $Vf=0$, the absolutely continuous primitive $F(x)=\int_0^xf$ is zero
almost everywhere, hence everywhere by continuity; its derivative gives
$f=0$ almost everywhere. Thus zero is not an eigenvalue.
If $Vf=\lambda f$ with $\lambda\ne0$, choose the absolutely continuous
representative $f=F/\lambda$. It satisfies $f'=f/\lambda$ almost
everywhere and $f(0)=0$. The product $e^{-x/\lambda}f(x)$ is absolutely
continuous with derivative zero almost everywhere, so is constant and
therefore zero. Again $f=0$. No eigenvalue exists.

#### Solution II.4.12 — Circular convolution and a Fourier sign correction

Extend $h$ periodically to the real line; otherwise $h(x-y)$ outside
$(-\pi,\pi)$ is not defined by the given data. With the printed basis
$e_n(x)=(2\pi)^{-1/2}e^{-inx}$, substitution $t=x-y$ and periodicity give

$$
(Ke_n)(x)=\frac{e^{-inx}}{2\pi}\int_{-\pi}^{\pi}h(t)e^{int}\,dt
=\widehat h(-n)e_n(x).
$$

Thus the eigenvalue for this sign convention is $\widehat h(-n)$, not
$\widehat h(n)$. Alternatively use the basis
$\widetilde e_n=(2\pi)^{-1/2}e^{inx}$, for which the printed
$\lambda_n=\widehat h(n)$ is correct. The kernel is square integrable:
its squared product norm is $\|h\|_2^2$, using periodic translation
invariance and its factor $(2\pi)^{-1/2}$. Hence $K$ is bounded and compact.
The Fourier basis is complete, so this computation genuinely diagonalizes
$K$, not just a proper part of the space.

#### Solution II.4.13 — Compactness of a countable block sum

If $T$ is compact, each $T_n$ is its composition with the bounded inclusion
of $\mathcal H_n$ and coordinate projection onto $\mathcal H_n$, so is
compact. If the block norms do not tend to zero, choose unit vectors in
infinitely many distinct blocks whose image norms exceed a fixed
$\varepsilon>0$. These images are mutually orthogonal and hence have no
convergent subsequence, a contradiction. Conversely, if each block is
compact, $T^{(N)}=T_1\oplus\cdots\oplus T_N\oplus0\oplus\cdots$ is
compact: successively select convergent subsequences in its finitely many
components. The direct-sum norm formula gives
$\|T-T^{(N)}\|=\sup_{n>N}\|T_n\|\to0$, proving compactness of $T$.

#### Solution II.4.14 — Product bases, including the nonseparable case

Use the rectangle-cover product measure specified in II.1.7. The functions
$\varphi_{ij}(x,y)=e_j(x)\overline{e_i(y)}$ are orthonormal: factor the
integral of a product into the two inner products, which is valid on the
sigma-finite supports of these $L^2$ functions.
To prove completeness, first note that finite linear combinations of
$f(x)g(y)$ with $f,g\in L^2(\mu)$ are dense in the product $L^2$ space.
For sigma-finite factors, finite-measure rectangle indicators generate
a dense space: on finite-measure rectangles the class of sets whose
indicators are approximable is closed under complements and countable
disjoint unions (truncate the union in measure), hence contains the
generated sigma-algebra. Exhaust by finite-measure rectangles and then
approximate simple functions. For arbitrary factors, the rectangle-cover
localization in II.1.7 puts each finite-product-measure set, modulo a null
set, into a product of sigma-finite subsets. The same argument applies
there and proves the density assertion globally.

Approximate $f$ and $\overline g$ by finite sums from the given basis.
The product norm identity $\|f(x)g(y)\|_2=\|f\|_2\|g\|_2$ and the
triangle inequality show these approximations converge in the product
norm. Thus the span of the $\varphi_{ij}$ is dense. Separability is not
needed: the family is a basis also for nonseparable $L^2(\mu)$ under this
product convention. Countable series for one vector do not require the
whole basis to be countable.

Two qualifications matter. With the printed definition of $\varphi_{ij}$,
the coefficient identity in Lemma 4.8 reads
$\langle k,\varphi_{ij}\rangle=\langle Ke_i,e_j\rangle$; the displayed
identity there has its indices interchanged. Also, outside sigma-finiteness
a measure merely agreeing on rectangles need not have the same density
property. This product-measure distinction is discussed in
[Tausk, *Tensor Products of L² Spaces*](https://www.ime.usp.br/~tausk/texts/TensorL2.pdf).

### §5. The Diagonalization of Compact Self-Adjoint Operators

#### Solution II.5.1 — An eigenvector expansion

For each distinct nonzero eigenvalue $\lambda$, choose an orthonormal
basis of the finite-dimensional eigenspace. The spectral theorem says
their union is a basis of $(\ker T)^\perp$. There are at most countably
many such vectors: for each $\varepsilon>0$ only finitely many mutually
orthogonal eigenvectors can have eigenvalues of modulus at least
$\varepsilon$, since their images would contradict compactness. Enumerate
them as $e_n$ and repeat the corresponding real eigenvalue as $\mu_n$.
Expanding a vector into its kernel component and these coordinates gives
$Th=\sum_n\mu_n\langle h,e_n\rangle e_n$, with norm convergence
because the coefficient square sum is bounded by $\|T\|^2\|h\|^2$.
An eigenvalue is repeated exactly the dimension of its eigenspace; finite
rank means that this list is finite.

#### Solution II.5.2 — An injective compact self-adjoint operator

When $\ker T=0$, the preceding countable orthonormal basis spans all of
$\mathcal H$. Finite linear combinations with rational real coefficients,
or rational real and imaginary parts, form a countable dense set. Thus
$\mathcal H$ is separable. Finite-dimensional and zero spaces satisfy the
same conclusion.

#### Solution II.5.3 — Symmetric square-integrable kernels

The adjoint-kernel formula gives $K^*=K$ from the assumed symmetry, and
4.7 gives compactness. Let $(e_n)$ be orthonormal eigenvectors for all
nonzero eigenvalues repeated according to multiplicity. For a finite set
of these vectors, Bessel's inequality applied to
$\overline{k(x,\cdot)}$ gives

$$
\sum_{n=1}^N|Ke_n(x)|^2\leq\int|k(x,y)|^2\,d\mu(y).
$$

Integrating gives
$\sum_{n=1}^N|\mu_n|^2=\sum_{n=1}^N\|Ke_n\|^2\leq\|k\|_2^2$.
Let $N\to\infty$. The product-measure localization in II.1.7 justifies
the same calculation for that non-sigma-finite convention. Zero
eigenvectors contribute zero; an uncountable kernel is not meant to be
enumerated in a sequence.

#### Solution II.5.4 — Solving a compact self-adjoint equation

If $Tf=h$, then $h\perp\ker T$ and
$\langle h,e_n\rangle=\mu_n\langle f,e_n\rangle$. Parseval therefore
gives the necessary condition
$\sum_n|\mu_n|^{-2}|\langle h,e_n\rangle|^2<\infty$.
Conversely that condition defines a vector
$f_0=\sum_n\mu_n^{-1}\langle h,e_n\rangle e_n$ in $(\ker T)^\perp$.
Boundedness of $T$ allows applying it to the convergent partial sums;
the result is $h$ because $h$ has no kernel component. All solutions are
$f=f_0+u$ with arbitrary $u\in\ker T$: their differences must, and may,
belong to the kernel. Since the eigenvalues are real,
$|\mu_n|^{-2}=\mu_n^{-2}$ as written in the question.

#### Solution II.5.5 — The resolvent away from the eigenvalues

There is $d>0$ with $|\lambda-\mu_n|\geq d$ for all $n$: all but
finitely many $\mu_n$ have modulus below $|\lambda|/2$, and none of
the remaining finite set equals $\lambda$. Write $h=h_0+\sum c_ne_n$
with $h_0\in\ker T$. Then the unique solution is

$$
f=\lambda^{-1}h_0+\sum_n\frac{c_n}{\lambda-\mu_n}e_n
=\lambda^{-1}\left[h+\sum_n\frac{\mu_n}{\lambda-\mu_n}c_ne_n\right].
$$

The separation bound proves convergence and verifies the equation
coordinatewise; it also proves uniqueness. The $\lambda_n$ in the
question's last formula denotes the same eigenvalues called $\mu_n$
earlier, not a different sequence. For a kernel operator this solves
$\lambda f(x)-\int k(x,y)f(y)\,d\mu(y)=h(x)$ by expansion in
eigenfunctions. The equality is an $L^2$ equality; additional regularity
is needed before asserting pointwise convergence of its series.

### §6. An Application: Sturm–Liouville Systems

#### Solution II.6.1 — Four boundary conditions for −h″

For each case, solve $-h''=\lambda h$ and normalize in $L^2(0,1)$.
The Green function for an inverse must satisfy the boundary conditions
in $x$, be continuous at $x=y$, and have derivative jump
$g_x(y+,y)-g_x(y-,y)=-1$.

(a) Dirichlet conditions give $\lambda_n=n^2\pi^2$ and
$e_n(x)=\sqrt2\sin(n\pi x)$ for $n\geq1$. The linear solution at
$\lambda=0$ is zero; negative $\lambda$ is excluded by
$\langle Lh,h\rangle=\int|h'|^2$. The Green function is
$g(x,y)=\min(x,y)(1-\max(x,y))$. Its slopes on the two sides differ
by $-1$ and it vanishes at both endpoints, verifying the inverse formula.

(b) Neumann conditions give the normalized constant $e_0=1$ with
$\lambda_0=0$, and $e_n(x)=\sqrt2\cos(n\pi x)$,
$\lambda_n=n^2\pi^2$ for $n\geq1$. There is no Green function for an
inverse on all of $L^2$, since constants lie in the kernel. The solvability
condition is $\int_0^1 f=0$, obtained by integrating $-h''=f$ and using
the boundary derivatives. On the mean-zero subspace the reduced Green
kernel is

$$
g_0(x,y)=\frac{x^2+y^2}{2}-\max(x,y)+\frac13.
$$

Its endpoint derivatives vanish, its derivative jump is $-1$, and
$\int_0^1g_0(x,y)\,dx=0$. Differentiating the two integrals on either
side of $y=x$ gives $-(G_0f)''=f-\int_0^1f$. Thus for mean-zero $f$
it gives the unique mean-zero solution; add any constant for all solutions.
It would be incorrect to present this as an ordinary inverse Green function.

(c) The mixed conditions give
$\lambda_n=((n+1/2)\pi)^2$ and
$e_n(x)=\sqrt2\sin((n+1/2)\pi x)$ for $n\geq0$.
The zero and negative cases are excluded as in (a). The kernel is
$g(x,y)=\min(x,y)$: it is zero at $x=0$, has derivative zero at $x=1$,
and the required jump.

(d) Integration by parts gives
$\langle Lh,h\rangle=\int_0^1|h'|^2+|h(0)|^2+|h(1)|^2$.
Thus all eigenvalues are strictly positive. Write $\lambda=k^2$, $k>0$.
The first condition makes every eigenfunction proportional to
$u_k(x)=\cos(kx)+k^{-1}\sin(kx)$. The second condition becomes

$$
(1-k^2)\sin k+2k\cos k=0.
$$

Let $k_1<k_2<\cdots$ be its positive roots. Equivalently they are the
unique solutions of $k_n=n\pi-2\arctan k_n$, $n\geq1$: writing
$u_k$ as a multiple of $\sin(kx+\arctan k)$ proves this equivalence,
and $k+2\arctan k$ is strictly increasing from zero to infinity.
Then $\lambda_n=k_n^2$ and
$e_n=u_{k_n}/(\int_0^1u_{k_n}^2)^{1/2}$. This integral is positive and
specifies the normalization without an implicit sign choice. The apparent
root $k=0$ of the multiplied characteristic equation is extraneous:
a zero-eigenvalue solution would be $a(1+x)$ and the right condition
would require $2a=-a$.
For the Green function choose $h_a(x)=1+x$, $h_b(x)=2-x$.
Their Wronskian is $-3$, so
$g(x,y)=(1+\min(x,y))(2-\max(x,y))/3$. Direct differentiation verifies
both Robin conditions and the jump. In all four cases orthogonality of
distinct eigenfunctions follows from integration by parts, and completeness
follows from the compact Green-operator theorem (using the reduced inverse
plus the constant vector in (b)).

#### Solution II.6.2 — Square summability of inverse eigenvalues

Under (6.4), $G=L^{-1}$ has a continuous kernel on the compact square,
so $g\in L^2([a,b]^2)$. Its eigenvalues are $1/\lambda_n$ by 6.10,
with the same normalized eigenfunctions. II.5.3 gives
$\sum_n\lambda_n^{-2}\leq\iint|g(x,y)|^2\,dx\,dy<\infty$.
No eigenvalue is zero under (6.4).

#### Solution II.6.3 — The domain and uniform absolute convergence

Put $c_n=\langle h,e_n\rangle$. Since $\mathcal D=\operatorname{ran}G$
and $Ge_n=\lambda_n^{-1}e_n$, the range criterion of II.5.4 gives
$h\in\mathcal D$ exactly when
$\sum_n\lambda_n^2|c_n|^2<\infty$.
Strictly speaking an $L^2$ class then has a unique continuous representative
in $\mathcal D$. For $h\in\mathcal D$, the coefficients of $Lh$ are
$\lambda_nc_n$.

For convergence a uniform bound on Green-kernel sections is useful. The
identity $Ge_n(x)=e_n(x)/\lambda_n$ holds at every $x$ by continuity.
Bessel's inequality in the $y$ variable therefore gives

$$
\sum_n\frac{|e_n(x)|^2}{\lambda_n^2}
\leq\int_a^b|g(x,y)|^2\,dy\leq C^2,
\qquad
C^2=\max_{x\in[a,b]}\int_a^b|g(x,y)|^2\,dy<\infty.
$$

Consequently
$\sup_x\sum_{n>N}|c_ne_n(x)|
\leq C(\sum_{n>N}\lambda_n^2|c_n|^2)^{1/2}\to0$.
This proves absolute convergence at each point with uniformly vanishing
absolute tails. The uniform limit equals $h$ in $L^2$ and hence everywhere
for its continuous representative. No unproved uniform bound on individual
eigenfunctions is being assumed.

#### Solution II.6.4 — The nonresonant eigenfunction expansion

For $\lambda\ne\lambda_n$, the sequence
$\lambda_n/(\lambda_n-\lambda)$ is bounded: $|\lambda_n|\to\infty$,
and the remaining finitely many denominators are nonzero. Thus
$c_n=\langle f,e_n\rangle/(\lambda_n-\lambda)$ satisfies
$\sum\lambda_n^2|c_n|^2<\infty$ by Parseval. II.6.3 supplies
$h=\sum_nc_ne_n\in\mathcal D$, with uniform and absolute convergence.
The coefficients of $(L-\lambda)h$ are precisely those of $f$, proving
the equation. The homogeneous equation has all coefficients zero, proving
uniqueness. This argument also covers $\lambda=0$ under (6.4).

#### Solution II.6.5 — The resonant equation

At $\lambda=\lambda_n$ the $n$th coefficient equation is
$0=\langle f,e_n\rangle$, which is the necessary compatibility condition.
For $j\ne n$, take
$c_j=\langle f,e_j\rangle/(\lambda_j-\lambda_n)$ and choose $c_n=\alpha$
freely. Distinct eigenvalues have one-dimensional eigenspaces for these
separated boundary conditions; this follows from uniqueness of an ODE
solution with its initial data and the one-dimensional allowable data at
$a$. The same ratio bound as in II.6.4 shows weighted square summability.
Therefore II.6.3 proves the stated expansion, its uniform absolute
convergence, and membership in $\mathcal D$. All solutions differ by
$\alpha e_n$. Only distinctness and escape to infinity are needed here;
no stronger ordering by strictly increasing absolute values is required.

#### Solution II.6.6 — Removing the zero-kernel assumption by a shift

(a) The absolutely continuous product
$h'g-hg'$ has derivative $h''g-hg''$ almost everywhere. The product rule
is legitimate because $h,g$ and their first derivatives are bounded on
the compact interval and the second derivatives are integrable.
Integrating its derivative gives the displayed endpoint identity.

(b) Apply (a) to $h$ and $\overline g$. At either endpoint the vectors
$(h,h')$ and $(\overline g,\overline{g'})$ satisfy the same nonzero real
linear boundary equation. They are therefore linearly dependent, making
the boundary determinant zero. Since $q$ is real, its multiplication
terms cancel as well, giving $\langle Lh,g\rangle=\langle h,Lg\rangle$.

(c) Substitution of the two eigenvalue equations gives
$(\lambda-\mu)\langle h,g\rangle=0$. Distinct real eigenvalues imply
orthogonality. In fact every eigenvalue is real, since (b) makes
$\langle Lh,h\rangle$ real and it equals $\lambda\|h\|^2$.

(d) If every real number were an eigenvalue, choose a normalized eigenvector
for each one. Part (c) would give an uncountable orthonormal set in the
separable space $L^2[a,b]$, impossible by the disjoint-ball argument of
Solution I.4.18. Thus some real $\mu$ is not an eigenvalue, equivalently
$\ker(L-\mu)=0$. Replacing $q$ by the still real continuous function
$q-\mu$ makes the injective Green-function theory applicable. This argument
does not assume the spectral theorem for $L$ before constructing its inverse.

### §7. The Spectral Theorem and Functional Calculus for Compact Normal Operators

#### Solution II.7.1 — Why a projection series need not converge in norm

The difference $R_n=P-\sum_{j=1}^nP_j$ is the projection onto the closed
sum of the remaining ranges. It is nonzero because $P_{n+1}\ne0$.
Every nonzero orthogonal projection has norm one: it is contractive and
fixes a unit vector in its range. Thus $\|R_n\|=1$ for every $n$,
although $R_nh\to0$ for every fixed $h$ by II.3.5.

#### Solution II.7.2 — The two definitions of diagonalizability

If $Ae_n=\alpha_ne_n$ on an orthonormal basis, the rank-one projections
onto $\mathbb Fe_n$ partition the identity and meet definition 7.3.
Conversely, choose an orthonormal basis in each nonzero $P_i\mathcal H$.
Their union is orthonormal and spans densely because the projections
partition the identity. Every such basis vector is an eigenvector with
value $\alpha_i$. In a separable space this union is countable (or finite),
which is precisely the basis formulation used in 4.6. Zero projection
blocks may simply be discarded.

#### Solution II.7.3 — Compact diagonal block operators

Discard zero projections and interpret the list of nonzero $\alpha_i$
as indexed by blocks, retaining repetitions; alternatively first combine
all equal scalar blocks into their full eigenspaces. The exact criterion is
that, for every $\varepsilon>0$, only finitely many nonzero blocks have
$|\alpha_i|\geq\varepsilon$, and each of these blocks has finite rank.
Indeed an infinite-dimensional such block, or infinitely many such blocks,
supplies orthonormal vectors with mutually orthogonal images of norm at
least $\varepsilon$, contradicting compactness. Taking
$\varepsilon=1,1/2,1/3,\ldots$ gives countably many nonzero blocks and
the convergence to zero asserted in (a)–(c).
Conversely retain finitely many nonzero blocks and set all others to zero.
These are finite-rank operators, and their norm error is the supremum of
the omitted $|\alpha_i|$, which tends to zero. Thus $A$ is compact.
If the word “set” in (c) were used to discard repetitions without combining
their projections, it would lose information: infinitely many scalar-one
rank-one blocks give the noncompact identity. The indexed interpretation
avoids this ambiguity.

#### Solution II.7.4 — An eigenbasis characterizes diagonalizability

From a scalar projection partition, choose a basis in each range as in
II.7.2; their union is an orthonormal eigenbasis, even without separability.
Conversely, given such a basis $(e_i)$, use its rank-one projections.
Boundedness of $A$ gives $|\alpha_i|=\|Ae_i\|\leq\|A\|$.
Expansion of each vector in the basis proves the projection formula and
all the requirements of 7.3. This proves Proposition 7.4.

#### Solution II.7.5 — Adjoint, normality, and norm of scalar blocks

For the orthogonal decompositions $h=\sum P_ih$ and $g=\sum P_ig$,
$\langle Ah,g\rangle=\sum_i\alpha_i\langle P_ih,P_ig\rangle$.
Cauchy–Schwarz makes this sum absolutely convergent. Moving the scalar
to the second argument conjugates it, so
$A^*=\bigoplus_i\overline\alpha_iP_i$. Both products $A^*A$ and
$AA^*$ are $\bigoplus_i|\alpha_i|^2P_i$, proving normality.
The square-norm identity gives $\|A\|\leq\sup_i|\alpha_i|$, and testing
unit vectors in each nonzero block gives equality. As usual, zero blocks
are excluded when taking that supremum.

#### Solution II.7.6 — Completing the compact normal spectral theorem

Write $T=A+iB$ with compact self-adjoint $A,B$. Normality is equivalent
to $AB=BA$. Each nonzero eigenspace of $A$ is finite dimensional and
reduces $B$. Diagonalize $B$ inside it to get joint eigenvectors, as in
the text. On $\ker A$, diagonalize the compact self-adjoint restriction
$B_0$ on $(\ker B_0)^\perp$, and append any orthonormal basis of
$\ker A\cap\ker B$. These vectors are joint eigenvectors of $A,B$,
and their union spans $\mathcal H$ by the two self-adjoint spectral
decompositions. They therefore form an eigenbasis for $T$.

Group the basis vectors with the same nonzero value $\lambda$ into the
projection $P_\lambda$. Distinct groups are orthogonal. Only finitely
many eigenbasis vectors can have eigenvalue modulus at least any fixed
$\varepsilon>0$, or their images contradict compactness. Thus each
nonzero eigenspace is finite dimensional, the nonzero eigenvalues are
countable, and any enumeration of the distinct ones tends to zero.
The remaining basis vectors span $\ker T$. On this basis the norm error
after finitely many groups is exactly the supremum of the omitted moduli.
It tends to zero, proving (7.7) in operator norm and completing the
bookkeeping omitted in the text. Finite lists terminate instead.

#### Solution II.7.7 — Commuting with every compact operator

For every unit $e$, the rank-one projection $P_e$ is compact. The identity
$AP_e=P_eA$ implies $Ae\in\mathbb Fe$, so every nonzero vector is an
eigenvector of $A$. If $x,y$ are independent and
$Ax=\alpha x$, $Ay=\beta y$, $A(x+y)=\gamma(x+y)$, independence gives
$\alpha=\beta=\gamma$. Any two nonzero vectors either are dependent or
can be compared this way, so one common scalar works on the whole space.
Thus $A=cI$; on the zero space the conclusion is automatic.

#### Solution II.7.8 — A simple compact normal operator has scalar commutant blocks

An operator commuting with $T$ leaves every eigenspace invariant. Because
the eigenspaces, including the kernel, span $\mathcal H$ orthogonally,
it also leaves each complementary sum invariant, so each eigenspace reduces
it. Under the dimension hypothesis each nonzero eigenspace is a line.
The restriction of $A$ there is a scalar $a_\lambda$, with
$|a_\lambda|\leq\|A\|$. Define $\phi(\lambda)=a_\lambda$ on eigenvalues
and zero elsewhere. This is a bounded function, and its spectral action
agrees with $A$ on every eigenvector, hence everywhere. The argument
includes a possible one-dimensional kernel.

#### Solution II.7.9 — Why a larger eigenspace prevents that conclusion

Suppose $E=\ker(T-\lambda)$ has dimension at least two. Choose a
one-dimensional subspace of $E$ and let $Q$ be its orthogonal projection
on all of $\mathcal H$. As $T$ is scalar on $E$ and $E$ reduces $T$,
$Q$ commutes with $T$. But every $\phi(T)$ restricts to the scalar
$\phi(\lambda)I_E$, while $Q|_E$ is neither zero nor identity and is
not scalar. This contradicts the stated equality of algebras. Therefore
each eigenspace, including the kernel, has dimension at most one.

#### Solution II.7.10 — Cyclicity and simple eigenvalues

If $h$ is cyclic and an eigenspace $E_\lambda$ contains a nonzero vector
$u$ orthogonal to $P_\lambda h$, then
$\langle p(T)h,u\rangle=p(\lambda)\langle P_\lambda h,u\rangle=0$
for every polynomial. This contradicts density. Thus every eigenspace has
dimension at most one, and a cyclic vector must have a nonzero component
on each eigenline.

Conversely enumerate the eigenlines (including the kernel if nonzero) as
$\mathbb Ce_j$ and choose a square-summable sequence of nonzero coefficients,
for example $2^{-j}$, to define $h=\sum_j2^{-j}e_j$; use any nonzero
coefficients if there are finitely many. Let $M$ be the closed polynomial
orbit of $h$. We prove more generally that any $h$ whose eigenline
coefficients $c_j$ are all nonzero is cyclic.
Fix a nonzero eigenvalue $\lambda$. There are only finitely many other
eigenvalues $\mu$ with $|\mu|\geq|\lambda|$. Choose a polynomial $q$
vanishing on all of them but with $q(\lambda)=1$.
Then $q(T)(T/\lambda)^Nh\in M$. Its $\lambda$ component is
$c_\lambda e_\lambda$; the larger and equal-modulus unwanted components
are zero. Every smaller nonzero component tends to zero, and their
squared norms are dominated by
$\sup_{|z|\leq\|T\|}|q(z)|^2|c_j|^2$. The kernel component is zero
for $N\geq1$. A finite-head and small-tail argument for this summable
bound shows norm convergence to $c_\lambda e_\lambda$. Hence every
nonzero eigenline lies in $M$. Subtract their convergent expansion from
$h$ to obtain its kernel component, which spans the kernel if present.
Thus $M=\mathcal H$. This proof uses polynomials in $T$ alone, not in
$T$ and $T^*$, an important distinction for complex eigenvalues.

#### Solution II.7.11 — A diagonal model on an atomic measure space

The vectors $u_n=\alpha_n^{-1/2}\mathbf1_{\{\lambda_n\}}$ form an
orthonormal basis of $L^2(\mu)$, and $Tu_n=\lambda_nu_n$.
(a) Boundedness of the $\lambda_n$ gives boundedness of $T$; its adjoint
conjugates them, so it is normal.

(b) Even without compactness a cyclic vector exists, but it need not be
the constant function. Here is a construction with the requisite tail
control. Choose a closed disk containing all the $\lambda_n$. For each
$m$, let $p_{mj}$, $1\leq j\leq m$, be the Lagrange polynomials taking
value one at $\lambda_j$ and zero at the other first $m$ points. Let
$C_m=\max_{j\leq m}\sup_{z\text{ in the disk}}|p_{mj}(z)|$.
Choose positive numbers

$$
c_n=\frac{2^{-n}}{1+\max_{k<n}C_k},
\quad\text{where the maximum of an empty set is }0,
\qquad h=\sum_nc_nu_n.
$$

For fixed $j$ and $m\geq j$, the first $m$ coordinates of
$p_{mj}(T)h/c_j$ equal those of $u_j$. Its remaining norm is at most
$(C_m/c_j)(\sum_{n>m}c_n^2)^{1/2}\leq2^{-m}/c_j$, which tends to
zero. Every $u_j$ therefore lies in the closed polynomial orbit of $h$,
proving cyclicity.

(c) Commutation sends the one-dimensional eigenspace $\mathbb Cu_n$ into
itself, so $Au_n=a_nu_n$ with $\sup|a_n|\leq\|A\|$. Set
$\phi(\lambda_n)=a_n$ and zero elsewhere; then $A=M_\phi$.
(d) The diagonal compactness criterion gives compactness exactly when
$\lambda_n\to0$. (e) In that compact case II.7.10 shows the cyclic
vectors are exactly those $f\in L^2(\mu)$ with $f(\lambda_n)\ne0$ for
every $n$. These point values are meaningful because every atom has
positive mass. (f) With $P_nf=f(\lambda_n)\mathbf1_{\{\lambda_n\}}$,
the spectral expansion is $T=\sum_{\lambda_n\ne0}\lambda_nP_n$ in
operator norm; a possible zero atom gives its kernel projection.

#### Solution II.7.12 — When a bounded functional calculus value is compact

Write the distinct nonzero eigenvalues as $\lambda_n$ with finite-rank
projections $P_n$, and let $P_0$ project onto $\ker T$.
Then $\phi(T)=\phi(0)P_0+\sum_n\phi(\lambda_n)P_n$ strongly.
The necessary and sufficient conditions are that for every
$\varepsilon>0$ only finitely many $n$ have $|\phi(\lambda_n)|\geq\varepsilon$,
and that either $\dim\ker T<\infty$ or $\phi(0)=0$.
For an infinite list the first condition says $\phi(\lambda_n)\to0$;
for a finite list it is automatic. Necessity follows by testing orthonormal
vectors in the relevant eigenspaces. Sufficiency follows by finite-rank
truncation, whose error is the supremum of the omitted scalar moduli.
Values of $\phi$ away from the point spectrum play no role.

#### Solution II.7.13 — Uniqueness of the positive square root

Let $A\geq0$ be compact with $A^2=T$. It commutes with $T$, so each
nonzero eigenspace $E_\lambda$ of $T$ reduces $A$.
On that finite-dimensional space diagonalize the positive self-adjoint
restriction of $A$. Each of its eigenvalues is nonnegative with square
$\lambda$, hence equals $\sqrt\lambda$. Thus
$A|_{E_\lambda}=\sqrt\lambda I$.
For $h\in\ker T$, $\|Ah\|^2=\langle A^2h,h\rangle=0$, so $Ah=0$.
These eigenspaces and the kernel span the entire space. Consequently $A$
is forced to be the root constructed in 7.16, proving uniqueness.

#### Solution II.7.14 — Positivity of T*T

The adjoint rules give $(T^*T)^*=T^*T$, and
$\langle T^*Th,h\rangle=\langle Th,Th\rangle=\|Th\|^2\geq0$.
These are exactly the two requirements for positivity. This does not
require compactness of $T$.

#### Solution II.7.15 — Polar factors of a compact normal operator

On each nonzero eigenspace set $A=|\lambda|I$ and
$U=(\lambda/|\lambda|)I$. On $\ker T$ set $A=0$ and choose any unitary
$U_0$ (the identity is one choice). The orthogonal block formulas show
$A\geq0$, $U$ unitary, and $UA=AU=T$. Since the nonzero scalar moduli
tend to zero with finite-dimensional eigenspaces, $A$ is compact.
For any such factorization, $T^*T=A^2$, so uniqueness of the positive
root makes $A$ unique. The values of $U$ are forced on
$\overline{\operatorname{ran}A}=(\ker T)^\perp$. Unitarity then leaves
exactly the freedom of a unitary on $\ker T$. Thus $U$ is unique when
the kernel is zero, and otherwise has precisely that freedom.

#### Solution II.7.16 — Polar decomposition without normality

The compact ideal property makes $T^*T$ compact and positive, so its
positive square root $A$ exists. (a)
$\|Ah\|^2=\langle A^2h,h\rangle=\|Th\|^2$, and therefore
$\ker A=\ker T$.

(b) Define $U(Ah)=Th$ on $\operatorname{ran}A$. Part (a) proves that
this is well defined and isometric. Extend it continuously to
$\overline{\operatorname{ran}A}=(\ker T)^\perp$, and define it to be
zero on $\ker T$. The resulting bounded linear map has exactly the
properties requested and satisfies $UA=T$. These prescriptions force
its values on a dense subspace of the first summand and on all of the
second, proving uniqueness. Its range is
$\overline{\operatorname{ran}T}$, since the extended isometry has closed
range and contains $\operatorname{ran}T$ densely there.

(c) If $T$ is normal, its eigenbasis shows that this $U$ multiplies each
nonzero eigenline by $\lambda/|\lambda|$ and vanishes on the kernel;
it commutes with $A$, so $T=AU$. Conversely suppose $UA=AU$.
Each positive eigenspace $E_s$ of the compact positive $A$ is finite
dimensional and is invariant under $U$. The restriction is an isometry,
so in finite dimension it is onto and unitary. The operator is zero on
$\ker A$ by construction. Thus both $T^*T$ and $TT^*$ restrict to
$s^2I$ on $E_s$ and to zero on the kernel. The spectral decomposition of
$A$ proves $T$ normal. This finite-dimensional step is what rules out
a nonsurjective isometry on a positive eigenspace.

#### Solution II.7.17 — A missing hypothesis in the uniqueness assertion

As transcribed, this statement is false when zero is an accumulation point
and the kernel has room for an extra representation. Here is a counterexample
satisfying every displayed assumption. On $\ell^2\oplus\mathbb C\oplus\mathbb C$
let $T=\operatorname{diag}(1,1/2,1/3,\ldots)\oplus0\oplus0$.
Fix a free ultrafilter $\mathcal U$ on $\mathbb N$, and define

$$
\tau(\phi)=\operatorname{diag}(\phi(1),\phi(1/2),\ldots)
\oplus\phi(0)\oplus\lim_{n\to\mathcal U}\phi(1/n).
$$

For completeness, a free ultrafilter is a maximal family of subsets closed
under finite intersections and supersets, containing all cofinite sets but
no finite set; its existence follows by extending the cofinite filter with
the usual maximality principle. A bounded complex sequence has a unique
ultrafilter limit in a compact disk: finite intersections of the closures
of its values on filter sets are nonempty, compactness gives a point in all
of them, and the ultrafilter property separates two proposed distinct
limits. Continuity of addition and multiplication then shows that this
limit operation is linear, multiplicative, and sends one to one. It agrees
with ordinary limits and has absolute value at most the supremum norm.

It follows that $\tau$ is multiplicative, linear, and unital. The diagonal
coordinates and the first zero coordinate already give
$\|\tau(\phi)\|=\sup_{\lambda\in\sigma_p(T)}|\phi(\lambda)|$;
the ultrafilter coordinate cannot enlarge this norm. If $\psi(z)=z$
on the specified set, its last coordinate is $\lim_{\mathcal U}1/n=0$,
so $\tau(\psi)=T$. But for $\phi=\mathbf1_{\{0\}}$,
$\tau(\phi)=0\oplus1\oplus0$, while $\phi(T)=0\oplus1\oplus1$.
Thus the requested uniqueness cannot be proved from the listed assumptions.

A sufficient repair is to add $\tau(\mathbf1_{\{0\}})=P_{\ker T}$.
Here is a proof of uniqueness under that repair. For an isolated nonzero
eigenvalue $\lambda$, choose a bounded function $r$ equal to
$(z-\lambda)^{-1}$ on the other eigenvalues and zero at $\lambda$.
It is bounded there because $\lambda$ is isolated. The norm assumption
makes functions equal on the point spectrum have equal images. Therefore,
with $Q=\tau(\mathbf1_{\{\lambda\}})$,
$(T-\lambda)Q=0$ and $I-Q=(T-\lambda)\tau(r)$.
All images commute with $T$, so these identities make $Q$ the identity
on $E_\lambda$ and zero on every other eigenspace, including the kernel.
Their dense span gives $Q=P_\lambda$. Multiplicativity now yields
$\tau(\phi)P_\lambda=\phi(\lambda)P_\lambda$, and the added hypothesis
gives the same formula on the kernel. Equality follows everywhere.
Alternatively bounded pointwise-to-strong continuity of the calculus gives
the needed kernel projection by approximating its indicator with one minus
finite sums of nonzero eigenvalue indicators. Continuity is a genuine
additional condition, not a consequence of the stated norm equality;
compare the continuity-based uniqueness discussion in
[Kritchevski's notes on bounded Borel functions](https://www.math.ubc.ca/~rfroese/math511/bb_functions.pdf).

### §8. Unitary Equivalence for Compact Normal Operators

#### Solution II.8.1 — The equivalence relation

The identity implements $A\cong A$. If $UAU^{-1}=B$, the inverse unitary
gives $U^{-1}BU=A$. If also $VBV^{-1}=C$, then the unitary $VU$ gives
$(VU)A(VU)^{-1}=C$. These prove reflexivity, symmetry, and transitivity.

#### Solution II.8.2 — Conjugation by a Hilbert-space isomorphism

(a) The unitary $U$ maps the unit ball onto the unit ball, so
$\|UAU^{-1}\|=\|A\|$. Linearity and multiplicativity follow by
canceling $U^{-1}U$; conjugation by $U^{-1}$ is the inverse map.
Also $(UAU^{-1})^*=UA^*U^{-1}$ because $U^{-1}=U^*$.
Thus the intended adjoint identity is $\rho(A)^*=\rho(A^*)$; the
printed $\rho(A^*)=\rho(A^*)$ is a tautology, not the useful assertion.
(b) A unitary carries relatively compact sets to relatively compact sets,
and the same is true of its inverse, proving equivalence of compactness.
(c) Multiplicativity and injectivity give
$AT=TA$ exactly when $\rho(A)\rho(T)=\rho(T)\rho(A)$.
(d) The identity $\rho(A)Uh=UAh$ gives equivalence of invariance.
Since $(UM)^\perp=U(M^\perp)$, applying it to the complementary spaces
gives the reducing-subspace assertion as well.

#### Solution II.8.3 — Irreducibility of Volterra and the shift

A closed subspace reduces an operator exactly when its orthogonal projection
$P$ commutes with that operator and its adjoint.
(a) If $P$ reduces $V$, it commutes with $V+V^*=P_{\mathbb C1}$ by
II.2.7. Hence $P1$ lies in $\mathbb C1$. Since $P$ is a projection,
$P1$ is either zero or one. Further $V^n1=x^n/n!$, so commutation gives
$P(V^n1)=V^nP1$. If $P1=0$, $P$ kills every polynomial; if $P1=1$,
it fixes every polynomial. Polynomials are dense in $L^2(0,1)$:
continuous functions are dense and polynomial uniform approximation on
$[0,1]$ follows, for example, from Bernstein polynomials. To recall their
convergence, the weights $\binom nkx^k(1-x)^{n-k}$ have total one,
mean $nx$, and variance $nx(1-x)$; uniform continuity controls terms
with $|k/n-x|<\delta$, and the remaining total weight is at most
$1/(4n\delta^2)$. This proves uniform approximation. Thus continuity
forces $P=0$ or $I$, proving irreducibility of $V$.

(b) If $P$ reduces $S$, it commutes with $I-SS^*=P_{\mathbb Ce_1}$,
so $Pe_1=0$ or $e_1$. Commutation with $S$ gives
$Pe_n=S^{n-1}Pe_1$ for every $n$. The coordinate basis spans densely,
so again $P=0$ or $I$.

#### Solution II.8.4 — Matching irreducible summands

We use complex Hilbert spaces and nonzero irreducible summands, discarding
zero spaces. If zero-space operators are counted as irreducible under the
literal definition, they must first be removed: their number is not
determined by the operator, so the claimed matching cannot count them.
The easy direction is to take the direct sum of the unitary
intertwiners $A_i\cong B_{\pi(i)}$ and then permute the summands.
For necessity we supply the irreducible-intertwiner fact and the multiplicity
argument, since pairwise existence of matches alone would not prove a
bijection with correct repetitions.

**Auxiliary fact.** If $C$ is irreducible, every self-adjoint operator $R$
commuting with $C$ and $C^*$ is scalar. One elementary proof uses positive
square roots for bounded positive operators, not only compact ones.
For self-adjoint $S$ and $c\geq\|S\|$, $c>0$, put
$D=I-S^2/c^2$, a positive contraction. The scalar expansion
$1-\sqrt{1-t}=\sum_{n\geq1}a_nt^n$ has $a_n\geq0$ and
$\sum a_n=1$ (take $t\uparrow1$). Therefore
$|S|=c(I-\sum_{n\geq1}a_nD^n)$ converges in operator norm, is positive,
and squares to $S^2$ by multiplication of absolutely convergent series.
Positivity follows because each $D^n$ is a positive contraction and the
coefficients sum to one. All operators commuting with $S$ commute with
this square root.
If $R$ were not scalar, its unit-vector quadratic form would have distinct
infimum and supremum; otherwise polarization would make $R$ scalar.
Choose $t$ strictly between them and set $S=R-tI$. The two self-adjoint
operators $C_+=(|S|+S)/2$ and $C_-=(|S|-S)/2$ have product zero, commute
with $C,C^*$, and are both nonzero: vanishing of either would force $S$
to have only one sign. Their nonzero orthogonal closed ranges are reducing
subspaces for $C$, contradicting irreducibility. This proves the fact.

If $X$ intertwines two irreducible operators and also their adjoints, then
$X^*X$ commutes with the first pair and $XX^*$ with the second. The fact
just proved makes them $aI$ and $bI$. When $X\ne0$, both constants are
positive and equal to $\|X\|^2$. Thus $X/\|X\|$ is a unitary
intertwiner. In addition, any operator commuting with an irreducible pair
is scalar, by applying the fact to its real and imaginary Hermitian parts.
So, after fixing one unitary identification between equivalent summands,
every intertwiner of the pairs is a scalar multiple of that identification.

Now let $U$ implement $A\cong B$. Its block $U_{ji}$ intertwines
$A_i,B_j$ and their adjoints, since the summands reduce the operators.
It must vanish unless $A_i\cong B_j$. Fix one equivalence class of
irreducible summands and identify all its copies with a representative on
$H_0$. Then the corresponding blocks of $U$ are $u_{ji}I_{H_0}$.
Unitarity means the scalar matrix $(u_{ji})$ is a unitary between the
$\ell^2$ spaces of the two index sets in this class: test on vectors
whose $H_0$ coordinate is a fixed unit vector, and use the same test for
$U^*$. Those index sets therefore have equal cardinalities, by invariance
of Hilbert dimension. Choose a bijection in each class and combine them.
This gives the desired global $\pi$, including arbitrary repetitions and
possibly uncountable index sets.

#### Solution II.8.5 — Multiplicity functions and a missing boundedness condition

For compact normal $T$, only finitely many orthonormal eigenvectors can
have eigenvalues of modulus at least $\varepsilon>0$, since their images
would be separated by at least $\sqrt2\varepsilon$. Thus every nonzero
eigenspace is finite dimensional; the nonzero eigenvalues form a countable
set with only possible cluster point zero. Adding a possible zero
eigenvalue preserves countability of this set. These prove (a) and (b).

The converse as printed also needs the support
$S=\{\lambda:m(\lambda)>0\}$ to be bounded. Without it,
$m(n)=1$ for positive integers $n$ and $m=0$ elsewhere satisfies (a)
and (b), but no bounded operator can have these eigenvalues.
With boundedness added, every set
$\{\lambda\in S:|\lambda|\geq\varepsilon\}$ is finite: otherwise
compactness of a bounded closed annulus would give a nonzero cluster
point. Construct

$$
\mathcal H=\bigoplus_{\lambda\in S}\mathbb C^{m(\lambda)},
\qquad T=\bigoplus_{\lambda\in S}\lambda I_{\mathbb C^{m(\lambda)}}.
$$

Use a countably infinite-dimensional space when $m(0)=\infty$;
for general cardinal-valued multiplicity one can use that Hilbert
dimension instead. The direct sum is bounded and normal. Truncating to
the finitely many nonzero eigenvalues of modulus at least $\varepsilon$
gives finite rank and error at most $\varepsilon$, so $T$ is compact.
Its eigenspaces have exactly the prescribed dimensions, proving the
corrected converse. If $S$ is empty, take the zero operator on the zero space.

#### Solution II.8.6 — Unitary equivalence of projections

An intertwining unitary maps the range (the eigenvalue-one subspace) onto
the range, and the kernel onto the kernel, so their dimensions must match.
Conversely choose unitary maps separately between the two ranges and
between the two kernels, possible by equality of Hilbert dimensions.
Their orthogonal direct sum is a unitary taking $P$ to $Q$, because
both operators act as identity on the first summand and zero on the second.

#### Solution II.8.7 — Multiplication by x and by x²

Define $(Uf)(x)=\sqrt{2x}\,f(x^2)$ for $0<x<1$.
The substitution $t=x^2$ gives
$\int_0^1|Uf(x)|^2dx=\int_0^1|f(t)|^2dt$. The same identity proves
well-definedness on equivalence classes. Its inverse is
$(U^{-1}g)(t)=g(\sqrt t)/(\sqrt2\,t^{1/4})$, which belongs to $L^2$
by that substitution and inverts the formula almost everywhere.
Finally $(UAf)(x)=x^2(Uf)(x)=(A^2Uf)(x)$.
Thus $UAU^{-1}=A^2$, proving unitary equivalence. The square-root Jacobian
factor is essential; composition alone is not an isometry.

#### Solution II.8.8 — Decomposition into nested simple layers

Choose an orthonormal basis $e_{\lambda,k}$ for each eigenspace, with
$1\leq k\leq m_T(\lambda)$, allowing all positive integers for an
infinite kernel. For each $n$ let
$H_n=\overline{\operatorname{span}}\{e_{\lambda,n}:m_T(\lambda)\geq n\}$
and $T_n=T|_{H_n}$. The spaces are orthogonal and reduce $T$; their
direct sum is the whole space. Each $T_n$ is compact and simple, and

$$
m_{T_n}(\lambda)=\mathbf1_{\{m_T(\lambda)\geq n\}},
$$

so these multiplicity functions decrease in $n$.
For $\varepsilon>0$, only finitely many eigenvalues have modulus at
least $\varepsilon$, and each has finite multiplicity. Once $n$ exceeds
their maximum multiplicity none occurs in $T_n$, so $\|T_n\|<\varepsilon$
(or at most $\varepsilon$ after changing the threshold). Hence the norms
tend to zero. Zero-dimensional layers may be omitted; zero operators on
one-dimensional layers, arising from an infinite kernel, must be retained.

#### Solution II.8.9 — Uniqueness of the nested layers

For each fixed $\lambda$, the nonincreasing sequence
$m_{T_n}(\lambda)\in\{0,1\}$ has sum $m_T(\lambda)$. It is therefore
forced to be one precisely for $n\leq m_T(\lambda)$, or for every $n$
if that multiplicity is infinite. Thus the layer multiplicity functions
are completely determined by $m_T$. If $T\cong S$, their full
multiplicity functions agree, so the corresponding layer functions agree;
Theorem 8.3 gives $T_n\cong S_n$. Conversely equivalence of all layers
gives equality of the sums of multiplicities and hence $T\cong S$.
Pad a finite list with operators on zero spaces for the indexing comparison.

#### Solution II.8.10 — Decomposition by exact multiplicity

The repeated $T_2^{(3)}$ in the displayed formula is read as $T_3^{(3)}$:
the general term is $T_n^{(n)}$. For $n\geq1$ put
$S_n=\{\lambda:m_T(\lambda)=n\}$ and let $T_n$ be the simple diagonal
operator with one eigenline of value $\lambda$ for each $\lambda\in S_n$.
Each is compact because its nonzero eigenvalues form a subset of those of
$T$. The sets $S_n$ are disjoint, so
$m_{T_n}m_{T_k}=0$ for $n\ne k$. Repeating $T_n$ exactly $n$ times
reproduces every finite multiplicity, including a finite positive kernel
dimension by putting zero in its appropriate $S_n$.
If the kernel is infinite dimensional, add one separate zero operator
on a countably infinite-dimensional space. In that case zero belongs to
none of the $S_n$, so all $T_n$ are injective. If the kernel is finite,
the separate infinite-dimensional zero summand must be omitted; it is
not an obligatory part of the formula. Equality of multiplicities now
proves the decomposition. Finally, above any modulus threshold only
finitely many eigenvalues occur, with finitely many multiplicities, so
for all sufficiently large $n$ none lies in $S_n$. Thus $\|T_n\|\to0$.

#### Solution II.8.11 — Uniqueness of the exact-multiplicity decomposition

Equivalence of $T$ and $S$ gives equality of all eigenspace dimensions,
hence equality of their exact-multiplicity sets $S_n$ and of their kernel
dimensions. The simple factors then have the same multiplicity functions
and are unitarily equivalent. Conversely, equivalence of corresponding
simple factors reconstructs all finite nonzero multiplicities, while
the separately stated equality of kernel dimensions handles any infinite
zero block. Thus $m_T=m_S$ and Theorem 8.3 gives $T\cong S$.
An absent factor is again interpreted as acting on the zero space.

#### Solution II.8.12 — A nonzero compact normal operator cannot equal its double

Such a $T$ has a nonzero eigenvalue $\lambda$ by the spectral theorem.
Its multiplicity is a positive finite integer $m$. In $T\oplus T$ that
eigenspace has dimension $2m$, whereas unitary equivalence would preserve
its dimension. Since $m\ne2m$, the operators cannot be equivalent.
Nonzero and normal are relevant: the zero operator on an infinite-dimensional
space is equivalent to its double, and a nonnormal compact operator can
have no eigenvalues.

#### Solution II.8.13 — Operators equivalent to repeated copies of themselves

For an example take the identity on $\ell^2$. Interleaving two sequences
gives a unitary from $\ell^2\oplus\ell^2$ onto $\ell^2$, and it
intertwines the identities. More generally assume $T\cong T\oplus T$.
We prove carefully that this implies equivalence to the countable sum;
an unexplained infinite iteration of a finite direct-sum identity would
not itself be a proof.

Call an isometry a reducing intertwiner if it intertwines the operators
and their adjoints. A unitary from two copies onto one gives two such
isometries $V_0,V_1$ into $\mathcal H$, with orthogonal ranges summing
to $\mathcal H$. The maps $V_0^nV_1$, $n\geq0$, have mutually
orthogonal ranges, since cancellation in their pairwise inner products
uses $V_1^*V_0=0$. They give a reducing isometric embedding of
$T\oplus T\oplus\cdots$ into $T$. The coordinate inclusion gives a
reducing embedding in the other direction.

Here is the Hilbert-space version of the two-embedding argument, with
the operator compatibility retained. Suppose $V:H\to K$ and $W:K\to H$
are reducing isometric intertwiners for operators $A,B$. Put
$H_0=H\ominus WK$, $H_n=(WV)^nH_0$, and
$L=\bigoplus_{n\geq0}H_n$. These are orthogonal reducing subspaces:
$H_0\perp\operatorname{ran}(WV)$, and iterating the isometry preserves
orthogonality. Define $F=V$ on $L$ and $F=W^{-1}$ on $L^\perp$.
The latter is defined since $L^\perp\subset WK$. Its image is precisely
$K\ominus VL$, because
$WVL=\bigoplus_{n\geq1}H_n$ and
$WK\ominus WVL=L^\perp$. Thus $F$ is a unitary onto $K$.
Both pieces intertwine the respective restrictions, so $FA=BF$.
Applying this construction to the two embeddings proves the countable-sum
assertion.

Finally, for a diagonalizable normal $T$, unitary equivalence is determined
by the dimensions of all its eigenspaces: choose eigenbases and map
corresponding bases. Doubling replaces each multiplicity $\kappa$ by
$\kappa+\kappa$. Therefore $T\cong T\oplus T$ exactly when every
nonzero eigenspace has infinite dimension, including the eigenspace at
zero if present. Here “nonzero eigenspace” means a space of positive
dimension, not an eigenspace with a nonzero eigenvalue. Infinite cardinal
dimensions satisfy $\kappa+\kappa=\kappa$; positive finite ones do not.

#### Solution II.8.14 — Conjugating multiplication in the derivative norm

For $g\in L^2(0,1)$, $U^{-1}g(x)=\int_0^xg(t)\,dt$ by the derivative
isomorphism. The product rule for absolutely continuous functions gives

$$
(UAU^{-1}g)(x)
=\frac{d}{dx}\left(x\int_0^xg(t)\,dt\right)
=xg(x)+\int_0^xg(t)\,dt
$$

almost everywhere. Thus $UAU^{-1}=M_x+V$ on $L^2(0,1)$.
Both terms are bounded, which also verifies boundedness of the original
$A$ in the derivative-space norm. The product $xf(x)$ still vanishes
at zero and has square-integrable derivative, so it belongs to that
space. The source's parenthetical reference to Exercise I.1.4 should be
read as the derivative isomorphism proved in Exercise I.5.4 (and I.1.3).

<!-- END SOLUTIONS II -->
