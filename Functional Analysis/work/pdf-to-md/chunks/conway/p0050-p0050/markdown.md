(b) $\| A \bar { h } \| = \| A ^ { * } h \|$ for all h.

If H is a C-Hilbert space, then these statements are also equivalent to:

(c) The real and imaginary parts of A commute.

PROOF. $\mathbf { I f } \quad h \in { \mathcal { H } } .$ then $\| A \boldsymbol{h} \|^2 - \| A^* \boldsymbol{h} \|^2 = \langle A \boldsymbol{h}, A \boldsymbol{h} \rangle - \langle A^* \boldsymbol{h}, A^* \boldsymbol{h} \rangle =$ $\left\langle ( A ^ { * } A - A A ^ { * } ) h , h \right\rangle$ . Since $A ^ { * } A - A A ^ { * }$ is hermitian, the equivalence of (a) and (b) follows from Corollarv 2.14.

If $B , C$ are real and imaginary parts of A, then a calculation yields

$$
A ^ { * } A = B ^ { 2 } - i C B + i B C + C ^ { 2 } ,
$$

$$
A A ^ { * } = B ^ { 2 } + i C B - i B C + C ^ { 2 } .
$$

Hence $A^{*}A = AA^{*}$ if and only if $CB = BC$ , and so (a) and (c) are equivalent.

2.17. Proposition. If $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ , the following statements are equivalent.

(a) A is an isometry.

(b) $A ^ { * } A = I .$

(c) $\langle A h , A g \rangle = \langle h , g \rangle \; { \it f o r ~ a l l ~ } h , g { \it i n ~ } \mathcal { H } .$

PRooF. The proof that (a) and (c) are equivalent was seen in Proposition I.5.2. Note that if $h , g \in \mathcal { H }$ , then $\langle A ^ { * } A h , g \rangle = \langle A h , A g \rangle$ . Hence (b) and (c) are easily seen to be equivalent. ■

2.18. Proposition. If $A   \in   \mathcal { B } ( \mathcal { H } ) ,$ , then the following statements are equivalent.

(a) $A^{*}A = AA^{*} = I.$

(b) A is unitary. (That is, A is a surjective isometry.)

(c) A is a normal isometry.

PROOF. $(a) \Rightarrow (b);$ Proposition I.5.2.

(b)⇒(c): By (2.17), $A ^ { * } A = I .$ But it is easy to see that the fact that A is a surjective isometry implies that $A ^ { - 1 }$ is also. Hence by (2.17) $I = (A^{-1})^{*}A^{-1}$ $(A^{*})^{-1}A^{-1}=(AA^{*})^{-1}$ ; this implies that $A^{*}A = A\overline{A^{*}} = I$

$(c) \Rightarrow (a)$ By (2.17), $A ^ { * } A = I .$ Since A is also normal, $A A ^ { * } = A ^ { * } A = I$ and so A is surjective. ■

We conclude with a very important, though easily proved, result.

2.19. Theorem. $If   A \in \mathcal{B}(\mathcal{H})$ , then ker $A = ( \operatorname{rank} A^* )^{\perp}$

PROOF. If h∈ker A and $g \in \mathcal { H }$ then $\langle h , A ^ { * } g \rangle = \langle A h , g \rangle = 0 ,$ so ker $\mathbf { A } \subseteq$ (ran $A ^ { * } ) ^ { \perp }$ . On the other hand, if $h \perp \tan A^{*}$ and $g \in \mathcal { H }$ , then $\langle A h , g \rangle =$ $\langle h , A ^ { * } g \rangle = 0 ;$ so $( \operatorname { r a n } A ^ { * } ) ^ { \perp } \subseteq \ker A$ ■

Two facts should be noted. Since $A ^ { * * } = A$ , it also holds that ker $A ^ { * } =$ $( \operatorname { r a n } A ) ^ { \perp }$ . Second, it is not true that $( \ker A ) ^ { \perp } = \operatorname { r a n } A ^ { * }$ since ran $A ^ { * }$ may not