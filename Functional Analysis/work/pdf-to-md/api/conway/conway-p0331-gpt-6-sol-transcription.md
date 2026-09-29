3. Show that the closure of a symmetric operator is symmetric.

4. Let $\mathcal D=\{f\in L^2(0,\infty):$ for every $c>0$, $f$ is absolutely continuous on $[0,c]$, $f(0)=0$, and $f'\in L^2(0,\infty)\}$. Define $Af=if'$ for $f$ in $\mathcal D$. Show that $A$ is a densely defined closed operator and find $\operatorname{dom}A^*$. Show that $A$ is symmetric with deficiency indices $n_+=0$ and $n_-=1$.

5. Let $\mathcal E=\{f\in L^2(-\infty,0):$ for every $c<0$, $f$ is absolutely continuous on $[c,0]$, $f(0)=0$, and $f'\in L^2(-\infty,0)\}$. Define $Af=if'$ for $f$ in $\mathcal E$. Show that $A$ is a densely defined closed operator and find $\operatorname{dom}A^*$. Show that $A$ is symmetric with deficiency indices $n_+=1$, $n_-=0$.

6. If $k,l$ are any nonnegative integers or $\infty$, show that there is a closed symmetric operator $A$ with $n_+=k$ and $n_-=l$. (Hint: Use Exercises 4 and 5.)

7. Let $C_c^2(0,1)$ be all twice continuously differentiable functions on $(0,1)$ with compact support and let $Af=-f''$ for $f$ in $C_c^2(0,1)$. Show that the closure of $A$ is a densely defined symmetric operator and determine all of its self-adjoint extensions.

8. If $A\in\mathcal C(\mathcal H)$, show that $A^*A$ is self-adjoint (see Exercise 1.11).

9. Say that an operator $A$ is positive if $\langle Ah,h\rangle\geq 0$ for all $h$ in $\operatorname{dom}A$. Prove that if $A$ is positive and self-adjoint, then $\sigma(A)\subseteq[0,\infty)$. If $A$ is only assumed to be closed and positive, show that this conclusion may fail. (Hint: Look at the operator in Exercise 7.)

10. (Lasser [1972]) Let $\mathcal M$ be a dense linear manifold in $\mathcal H$ and let $\mathcal A$ consist of all linear transformations $A$ such that $\operatorname{dom}A=\mathcal M$, $A\mathcal M\subseteq\mathcal M$, the adjoint of $A$ exists, $\mathcal M\subseteq\operatorname{dom}A^*$, and $A^*\mathcal M\subseteq\mathcal M$. Prove that $A\mapsto A^*|_{\mathcal M}$ defines an involution on $\mathcal A$.

## §3. The Cayley Transform

Consider the Möbius transformation

$$
M(z)=\frac{z-i}{z+i}.
$$

It is immediate that $M(0)=-1$, $M(1)=-i$, and $M(\infty)=1$. Thus $M$ maps the upper half plane onto $\mathbb D$ and $M(\mathbb R\cup\infty)=\partial\mathbb D$. So if $A$ is self-adjoint, $M(A)$ should be unitary. Suppose $A$ is symmetric; does $M(A)$ make sense? What is $M(A)$?

To answer these questions, we should first investigate the meaning of $M(A)$ if $A$ is symmetric. We want to define $M(A)$ as $(A-i)(A+i)^{-1}$. As was seen in the last section, however, $\operatorname{ran}(A+i)$ is not necessarily all of $\mathcal H$ if $A$ is not self-adjoint. In fact, $(\operatorname{ran}(A+i))^\perp=\mathcal L_+$ and $(\operatorname{ran}(A-i))^\perp=\mathcal L_-$, the deficiency spaces for $A$. However (2.5), if $A$ is closed and symmetric, $\operatorname{ran}(A\pm i)$ is closed. Also, realize that if $w=M(z)$, then $z=M^{-1}(w)=i(1+w)/(1-w)$.
