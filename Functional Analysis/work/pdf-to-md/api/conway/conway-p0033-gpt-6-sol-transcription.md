## Exercises

1. Verify the statements in Example 4.3.

2. Verify the statements in Example 4.4.

3. Verify the statements in Example 4.5.

4. Find an infinite orthonormal set in the Hilbert space of Example 1.8.

5. Using the notation of the Gram–Schmidt Orthogonalization Process, show that up to scalar multiple $e_1=h_1/\|h_1\|$ and for $n\geq 2$, $e_n=\|h_n-f_n\|^{-1}(h_n-f_n)$, where $f_n$ is the vector defined formally by
   $$
   f_n=\frac{-1}{\det[\langle h_i,h_j\rangle]_{i,j=1}^{n-1}}
   \det\begin{bmatrix}
   \langle h_1,h_1\rangle & \cdots & \langle h_{n-1},h_1\rangle & \langle h_n,h_1\rangle\\
   \vdots & & \vdots & \vdots\\
   \langle h_1,h_{n-1}\rangle & \cdots & \langle h_{n-1},h_{n-1}\rangle & \langle h_n,h_{n-1}\rangle\\
   h_1 & \cdots & h_{n-1} & 0
   \end{bmatrix}.
   $$

In the next three exercises, the reader is asked to apply the Gram–Schmidt Orthogonalization Process to a given sequence in a Hilbert space. A reference for this material is pp. 82–96 of Courant and Hilbert [1953].

6. If the sequence $1,x,x^2,\ldots$ is orthogonalized in $L^2(-1,1)$, the sequence $e_n(x)=[\tfrac12(2n+1)]^{1/2}P_n(x)$ is obtained, where
   $$
   P_n(x)=\frac{1}{2^n n!}\left(\frac{d}{dx}\right)^n(x^2-1)^n.
   $$
   The functions $P_n(x)$ are called Legendre polynomials.

7. If the sequence $e^{-x^2/2},xe^{-x^2/2},x^2e^{-x^2/2},\ldots$ is orthogonalized in $L^2(-\infty,\infty)$, the sequence $e_n(x)=[2^n n!\sqrt{\pi}]^{-1/2}H_n(x)e^{-x^2/2}$ is obtained, where
   $$
   H_n(x)=(-1)^n e^{x^2}\left(\frac{d}{dx}\right)^n e^{-x^2}.
   $$
   The functions $H_n$ are Hermite polynomials and satisfy $H_n'(x)=2nH_{n-1}(x)$.

8. If the sequence $e^{-x/2},xe^{-x/2},x^2e^{-x/2},\ldots$ is orthogonalized in $L^2(0,\infty)$, the sequence $e_n(x)=e^{-x/2}L_n(x)/n!$ is obtained, where
   $$
   L_n(x)=e^x\left(\frac{d}{dx}\right)^n(x^n e^{-x}).
   $$
   The functions $L_n$ are called Laguerre polynomials.

9. Prove Corollary 4.10 using Definition 4.11.

10. If $\{h_n\}$ is a sequence in Hilbert space and $\sum\{h_n:n\in\mathbb N\}$ converges to $h$ (Definition 4.11), then $\lim_n\sum_{k=1}^n h_k=h$. Show that the converse is false.

11. If $\{h_n\}$ is a sequence in a Hilbert space and $\sum_{n=1}^{\infty}\|h_n\|<\infty$, show that $\sum\{h_n:n\in\mathbb N\}$ converges in the sense of Definition 4.11.

12. Let $\{\alpha_n\}$ be a sequence in $\mathbb F$ and prove that the following statements are equivalent: (a) $\sum\{\alpha_n:n\in\mathbb N\}$ converges in the sense of Definition 4.11. (b) If $\pi$ is any permutation of $\mathbb N$, then $\sum_{n=1}^{\infty}\alpha_{\pi(n)}$ converges (unconditional convergence). (c) $\sum_{n=1}^{\infty}|\alpha_n|<\infty$.
