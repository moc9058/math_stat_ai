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
