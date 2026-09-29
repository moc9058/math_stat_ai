Expressing $N\oplus A$ and $N\oplus B$ as

$$
\begin{bmatrix}N&0\\0&A\end{bmatrix}
\quad\text{and}\quad
\begin{bmatrix}N&0\\0&B\end{bmatrix}
$$

respectively, the equation $U(N\oplus A)=(N\oplus B)U$ becomes

$$
\begin{bmatrix}
U_{11}N&U_{12}A\\
U_{21}N&U_{22}A
\end{bmatrix}
=
\begin{bmatrix}
NU_{11}&NU_{12}\\
BU_{21}&BU_{22}
\end{bmatrix}.
\tag{10.7}
$$

Similarly, $U(N\oplus A)^*=(N\oplus B)^*U$ becomes

$$
\begin{bmatrix}
U_{11}N^*&U_{12}A^*\\
U_{21}N^*&U_{22}A^*
\end{bmatrix}
=
\begin{bmatrix}
N^*U_{11}&N^*U_{12}\\
B^*U_{21}&B^*U_{22}
\end{bmatrix}.
\tag{10.7*}
$$

Parts of the preceding equations will be referred to as $(10.7)_{ij}$ and $(10.7)_{ij}^*$, $i,j=1,2$.

An examination of the equations $U^*U=1$ and $UU^*=1$, written in matrix form, yields the equations

$$
\left.
\begin{aligned}
\text{(a)}\quad&U_{11}^*U_{12}+U_{21}^*U_{22}=0
&&(\text{on }\mathscr{H}_A)\\
\text{(b)}\quad&U_{11}U_{11}^*+U_{12}U_{12}^*=1
&&(\text{on }\mathscr{K})\\
\text{(c)}\quad&U_{21}U_{11}^*+U_{22}U_{12}^*=0
&&(\text{on }\mathscr{K}).
\end{aligned}
\right\}
\tag{10.8}
$$

Now equation $(10.7)_{22}$ and Proposition 6.10 imply that $(\ker U_{22})^\perp$ reduces $A$, $\operatorname{cl}(\operatorname{ran}U_{22})=(\ker U_{22}^*)^\perp$ reduces $B$, and

$$
A|(\ker U_{22})^\perp\cong B|(\ker U_{22}^*)^\perp.
\tag{10.9}
$$

What about $A|\ker U_{22}$ and $B|\ker U_{22}^*$? If they are unitarily equivalent, then $A\cong B$ and we are done. If $h\in\ker U_{22}\subseteq\mathscr{H}_A$, then

$$
\begin{bmatrix}U_{11}&U_{12}\\U_{21}&U_{22}\end{bmatrix}
\begin{bmatrix}0\\h\end{bmatrix}
=
\begin{bmatrix}U_{12}h\\0\end{bmatrix}.
$$

Since $U$ is an isometry, it follows that $U_{12}$ maps $\ker U_{22}$ isometrically onto a closed subspace of $\mathscr{K}$. Put $\mathcal{M}_1=U_{12}(\ker U_{22})$. Equations $(10.7)_{12}$ and $(10.7)_{12}^*$ and the fact that $\ker U_{22}$ reduces $A$ imply that $\mathcal{M}_1$ reduces $N$. Thus, the restriction of $U_{12}$ to $\ker U_{22}$ is the required isomorphism to show that

$$
A|\ker U_{22}\cong N|\mathcal{M}_1.
\tag{10.10}
$$

Similarly, $U_{21}^*$ maps $\ker U_{22}^*=(\operatorname{ran}U_{22})^\perp$ isometrically into $\mathcal{M}_2=U_{21}^*(\ker U_{22}^*)$, $\mathcal{M}_2$ reduces $N$, and

$$
B|\ker U_{22}^*\cong N|\mathcal{M}_2.
\tag{10.11}
$$

Note that if $\mathcal{M}_1=\mathcal{M}_2$, then (10.9), (10.10), and (10.11) show that $A\cong B$. Could it be that $\mathcal{M}_1$ and $\mathcal{M}_2$ are equal?

If $h\in\ker U_{22}$, then (10.8.a) implies that $U_{11}^*U_{12}h=-U_{21}^*U_{22}h=0$. Hence $\mathcal{M}_1=U_{12}(\ker U_{22})\subseteq\ker U_{11}^*$. On the other hand, if $f\in\ker U_{11}^*$, then (10.8.b) implies $f=(U_{11}U_{11}^*+U_{12}U_{12}^*)f=U_{12}U_{12}^*f$. But by (10.8.c), $U_{22}U_{12}^*f=-$
