§6. An Application: Sturm–Liouville Systems　　　　　　　　　　　　　　　　　53

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
