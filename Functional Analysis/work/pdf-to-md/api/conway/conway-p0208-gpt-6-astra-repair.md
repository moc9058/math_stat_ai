§2. Ideals and Quotients　　　　　　　　　　　　　　　　　193

If $\varepsilon>0$ is given, then $\delta$ can be chosen such that $\delta/(1-\delta)<\varepsilon$. So $\|a_n-1\|<\delta$ implies $\|a_n^{-1}-1\|<\varepsilon$. Hence $\lim a_n^{-1}=1$.

Now let $a\in G$ and suppose $\{a_n\}$ is a sequence in $G$ such that $a_n\to a$. Hence $a^{-1}a_n\to 1$. By the preceding paragraph, $a_n^{-1}a=(a^{-1}a_n)^{-1}\to 1$. Hence $a_n^{-1}=a_n^{-1}aa^{-1}\to a^{-1}$. ■

Two facts surfaced in the preceding proofs that are worth recording for the future.

**2.3. Corollary.** *Let $\mathcal A$ be a Banach algebra with identity.*

(a) *If $\|a-1\|<1$, then $a^{-1}=\sum_{k=0}^{\infty}(1-a)^k$.*

(b) *If $b_0a_0=1$ and $\|a-a_0\|<\|b_0\|^{-1}$, then $a$ is left invertible.*

A *maximal ideal* is a proper ideal that is contained in no larger proper ideal.

**2.4. Corollary.** *If $\mathcal A$ is a Banach algebra with identity, then*

(a) *the closure of a proper left, right, or bilateral ideal is a proper left, right, or bilateral ideal;*

(b) *a maximal left, right, or bilateral ideal is closed.*

**Proof.** (a) Let $\mathcal M$ be a proper left ideal and let $G_l$ be the set of left-invertible elements in $\mathcal A$. It follows that $\mathcal M\cap G_l=\square$. (See the introduction to this section.) Thus $\mathcal M\subseteq\mathcal A\setminus G_l$. By the preceding theorem, $\mathcal A\setminus G_l$ is closed. Hence $\operatorname{cl}\mathcal M\subseteq\mathcal A\setminus G_l$; and thus $\operatorname{cl}\mathcal M\ne\mathcal A$. It is easy to check that $\operatorname{cl}\mathcal M$ is an ideal. The proof of the remainder of (a) is similar.

(b) If $\mathcal M$ is a maximal left ideal, $\operatorname{cl}\mathcal M$ is a proper left ideal by (a). Hence $\mathcal M=\operatorname{cl}\mathcal M$ by maximality. ■

If $\mathcal A$ does not have an identity, then $\mathcal A$ may contain some proper, dense ideals. For example, let $\mathcal A=C_0(\mathbb R)$. Then $C_c(\mathbb R)$, the continuous functions with compact support, is a dense ideal in $C_0(\mathbb R)$. There is something that can be said, however (see Exercise 6).

**2.5. Proposition.** *If $\mathcal A$ is a Banach algebra with identity, then every proper left, right, or bilateral ideal is contained in a maximal ideal of the same type.*

The proof of the preceding proposition is an exercise in the application of Zorn’s Lemma and is left to the reader. Actually, this is a theorem from algebra and it is not necessary to assume that $\mathcal A$ is a Banach algebra.

Let $\mathcal A$ be a Banach algebra and let $\mathcal M$ be a proper closed ideal. Note that $\mathcal A/\mathcal M$ becomes an algebra. Indeed, $(x+\mathcal M)(y+\mathcal M)=xy+\mathcal M$ is a well-defined multiplication on $\mathcal A/\mathcal M$. (Why?)

**2.6. Theorem.** *If $\mathcal A$ is a Banach algebra and $\mathcal M$ is a proper closed ideal in $\mathcal A$, then $\mathcal A/\mathcal M$ is a Banach algebra. If $\mathcal A$ has an identity, so does $\mathcal A/\mathcal M$.*
