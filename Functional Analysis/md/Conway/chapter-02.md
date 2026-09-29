# II. Operators on Hilbert Space

<!-- OCR draft; page images require independent visual review. -->


<a id="pdf-page-41"></a>
# CHAPTER II

# Operators on Hilbert Space

A large area of current research interest is centered around the theory of operators on Hilbert space. Several other chapters in this book will be devoted to this topic.

There is a marked contrast here between Hilbert spaces and the Banach spaces that are studied in the next chapter. Essentially all of the information about the geometry of Hilbert space is contained in the preceding chapter. The geometry of Banach space lies in darkness and has attracted the attention of many talented research mathematicians. However, the theory of linear operators (linear transformations) on a Banach space has very few general results, whereas Hilbert space operators have an elegant and well-developed general theory. Indeed, the reason for this dichotomy is related to the opposite status of the geometric considerations. Questions concerning operators on Hilbert space don’t necessitate or imply any geometric difficulties.

In addition to the fundamentals of operators, this chapter will also present an interesting application to differential equations in Section 6.

## §1. Elementary Properties and Examples

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
30　　　　　　　　　　　　　　　　　II. Operators on Hilbert Space

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
38  II. Operators on Hilbert Space

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
42  II. Operators on Hilbert Space

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
46  II. Operators on Hilbert Space

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

