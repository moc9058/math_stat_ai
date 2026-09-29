application of Zorn's Lemma implies that $\mathcal { E }$ has a maximal element $E _ { 0 }$ . Let $\mathcal { H } _ { 0 } = \oplus \left\{ \operatorname { c l } \left[ \pi ( \mathcal { A } ) e \right] : e \in E _ { 0 } \right\}$ . If $h \in \mathcal { H } \ominus \mathcal { H } _ { 0 }$ , then $0 = \langle \pi ( a ) e , h \rangle$ for every a in  and e in $E _ { 0 }$ .So if a, b∈ and $e \in E _ { 0 } , 0 = \langle \pi ( b ^ { * } a ) e , h \rangle = \langle \pi ( b ) ^ { * } \pi ( a ) e , h \rangle =$ $\langle \pi ( a ) e , \pi ( b ) h \rangle$ . That is, $\pi ( \mathcal { A } ) e \perp \pi ( \mathcal { A } ) h$ for all e in $E _ { 0 }$ . Hence $E _ { 0 } \cup \{ h \} \in \mathcal { E }$ by the maximality of $E _ { 0 }$ it must be that $h = 0$ . Therefore $\mathcal { H } = \mathcal { H } _ { 0 }$

For e in $E _ { 0 }$ let $\mathcal { H } _ { e } = \mathrm { c l } \left[ \pi ( \mathcal { A } ) e \right]$ . If $a \in \mathcal { A } _ { 1 }$ clearly $\pi ( a ) \mathcal { H } _ { e } \subseteq \mathcal { H } _ { e }$ . Since $a ^ { * } \in \mathcal { A }$ and $\pi ( a ) ^ { * } = \pi ( a ^ { * } )$ $\mathcal { H } ,$ reduces $\pi ( a )$ So if $\pi _ { e } \colon \mathcal { A } \to \mathcal { B } ( \mathcal { H } _ { e } )$ is defined by $\pi _ { e } ( a ) = \pi ( a ) | \mathcal { H } _ { e } ,   \pi _ { e }$ is a representation of a. Clearly $\pi = \oplus \left\{ \pi _ { e } \colon e { \in } E _ { 0 } \right\}$

In light of the preceding theorem, it becomes important to understand cyclic representations. To do this, let $\pi : \mathcal { A } \rightarrow \mathcal { B } ( \mathcal { H } )$ be a cyclic representation with cyclic vector e. Define $f \colon { \mathcal { A } }   \to   \mathbb { C }$ by $f(a) = \langle \pi(a)e, e \rangle$ . Note that f is a bounded linear functional on $\varkappa$ with $\| f \| \leqslant \| e \| ^ { 2 }$ Since $f ( 1 ) = \| e \| ^ { 2 } ,$ $\| f \| = \| e \| ^ { 2 }$ . Moreover, $f ( a ^ { * } a ) = \langle \pi ( a ^ { * } a ) e , e \rangle = \langle \pi ( a ) ^ { * } \pi ( a ) e , e \rangle = \| \pi ( a ) e \| ^ { 2 } \geqslant 0 .$

5.10. Definition. If  is a C\*-algebra, a linear functional $f \colon { \mathcal { A } }   \to   \mathbb { C }$ is positive if $f ( a ) \geqslant 0$ whenever $a \in \mathcal { A } _ { + }$ . A state on $\varkappa$ is a positive linear functional on $\varkappa$ of norm 1.

5.11. Proposition. If f is a positive linear functional on a C\*-algebra $\alpha ,$ then

$$
| f ( y ^ { * } x ) | ^ { 2 } \leqslant f ( y ^ { * } y ) f ( x ^ { * } x )
$$

for every $x , y$ in $\varkappa$

PROOF. I $\mathbf { f } \left[ x , y \right] = f ( y ^ { * } x )$ for $x , y$ in $\alpha ,$ then $[ \cdot , \cdot ]$ is a semi-inner product on. The proposition now follows by the CBS inequality (I.1.4).

5.12. Corollary. If f is a non-zero positive linear functional on the $C ^ { * } { - a l g e b r a }$ A, then f is bounded and $\| f \| = f ( 1 )$

5.13. Example. If X is a compact space, then the positive linear functionals on $C ( X )$ correspond to the positive measures on X. The states correspond to the probability measures on X.

As was shown above, each cyclic representation gives rise to a positive linear functional. It turns out that each positive linear functional gives rise to a cyclic representation.

5.14. Gelfand-Naimark-Segal Construction. Let $\varkappa$ be a $C ^ { * }$ -algebra with identity.

(a) If f is a positive linear functional on A, then there is a cyclic representation $( \pi _ { f } , \mathcal { H } _ { f } )$ of A with cyclic vector e such that $f(a) = \langle \pi_f(a)e, e \rangle$ for all a in A.

(b) $I f \left( \pi , \mathcal { H } \right)$ is a cyclic representation of $\varkappa$ with cyclic vector e and $f(a) \equiv \langle \pi(a)e, e \rangle$ and $if \left( \pi_{f}, \mathcal{H}_{f} \right)$ is constructed as in (a), then π and $\pi _ { f }$ are equivalent.

Before beginning the proof, it will be helpful if the theorem is examined when $\varkappa$ is abelian. So let ${ \mathcal { A } } = C ( X )$ where X is compact. If f is a positive linear functional on $\varkappa$ , then there is a positive measure $\mu$ on $X$ such that $f ( \phi ) = \int \phi   d \mu$ for all $\phi$ in $\mathcal { A }$ The representation $( \pi _ { f } , \mathcal { H } _ { f } )$ is the one obtained by letting $\mathcal { H } _ { f }   =   L ^ { 2 } ( \mu )$ and $\pi _ { f } ( \phi ) = M _ { \phi }$ , but let us look a little closer. One way to obtain $L ^ { 2 } ( \mu )$ from $C ( X )$ and $\mu$ is to let $\mathcal { L } = \left\{ \phi \in C ( X ) : \int | \phi | ^ { 2 } d \mu = 0 \right\}$ Note that $\mathcal { L }$ is an ideal in C(X). Define an inner product on $C ( X ) / { \mathcal { L } }$ by $\langle \phi + \mathcal { L } , \psi + \mathcal { L } \rangle = \int \phi \bar { \psi } d \mu$ . The completion of $C ( X ) / { \mathcal { L } }$ with respect to this inner product is $L ^ { 2 } ( \mu )$

To see part (b) in the abelian case, let $\pi : C(X) \to \mathcal{B}(\mathcal{H})$ be a cyclic representation with cyclic vector e. Let $\mu$ be the positive measure on X such that $\int \phi   d \mu = \langle \pi ( \phi ) e , e \rangle = f ( \phi )$ . Now define $U _ { 1 } \colon C ( X ) \to { \mathcal { H } }$ by $U _ { 1 } ( \phi ) = \pi ( \phi ) e$ Note that $U _ { 1 }$ is linear and has dense range. If $\mathcal { L }$ is in the preceding paragraph and $\phi \in { \mathcal { L } } ,$ then $\| U _ { 1 } ( \phi ) \| ^ { 2 } = \langle \pi ( \phi ) e , \pi ( \phi ) e \rangle = \langle \pi ( \phi ^ { * } \phi ) e , e \rangle =$ $\int | \phi | ^ { 2 } d \mu = 0 . \mathrm { S o } \dot { U } _ { 1 } \mathcal { L } = 0$ Thus $U _ { 1 }$ induces a linear map $U \colon C ( X ) / { \mathcal { L } } \to { \mathcal { H } }$ where $U ( \phi + \mathcal { L } )   =   \pi ( \phi ) e .$ If $\langle \phi + \mathcal { L } , \psi + \mathcal { L } \rangle \equiv \int \phi \bar { \psi } d \mu ,$ then $\langle U ( \phi + \mathcal { L } ) ,$ $U(\psi + \mathcal{L}) = \langle \pi(\phi)e, \pi(\psi)e \rangle = \langle \pi(\phi \psi^*)e, e \rangle = \int \phi \psi d\mu = \langle \phi + \mathcal{L}, \psi + \mathcal{L} \rangle$ Thus U extends to an isomorphism U from the completion of $\mathcal { A } / \mathcal { L } = L ^ { 2 } ( \mu )$ onto $\mathcal { H }$ So $U \colon L ^ { 2 } ( \mu ) \to { \mathcal { H } }$ and if $\phi   \in   C ( X )$ and we think of $C ( X )$ as a (dense) subset of $L ^ { 2 } ( \mu ) , U \phi = \pi ( \phi ) e$ . If $\phi , \psi \in C ( X )$ , then $U M _ { \phi } \psi = U ( \phi \psi ) = \pi ( \phi \psi ) e =$ $\pi ( \phi ) \pi ( \psi ) e = \pi ( \phi ) U ( \psi ) ,$ ; that is, $U M _ { \phi } = \pi ( \phi ) U$ on a dense subset of $L ^ { 2 } ( \mu )$ and, hence, $U M _ { \phi } = \pi ( \phi ) U$ for every $\phi$ in $C ( X )$ . In other words, π is equivalent to the representation $\phi   \mapsto   M _ { \phi }$

PROOF OF THEOREM 5.14. Let $f$ be a positive linear functional on $\varkappa$ and put $\mathcal { L } = \{ x \in \mathcal { A } : f ( x ^ { * } x ) = 0 \}$ . It is easy to see that $\mathcal { L }$ is closed in $\varkappa$ Also if $a   \in   \mathcal { A }$ and $x \in \mathcal { L }$ , then (5.11) implies that

$$
\begin{aligned}f((ax)^{*}(ax))^{2} &= f(x^{*}(a^{*}ax))^{2} \\& \leqslant f(x^{*}x)f(x^{*}a^{*}aa^{*}ax) \\&= 0.\end{aligned}
$$

That is, $\mathcal { L }$ is a closed left ideal in $\not { x }$ Now consider $\mathcal { A } / \mathcal { L }$ as a vector space. (Since $\mathcal { L }$ is only a left ideal, $\mathcal { A } / \mathcal { L }$ is not an algebra.) For $x , y$ in $\alpha ,$ define

$$
\langle x + { \mathcal { L } } , y + { \mathcal { L } } \rangle = f ( y ^ { * } x ) .
$$

It is left as an exercise for the reader to show that $\langle \cdot , \cdot \rangle$ is a well-defined inner product on $\mathcal { A } / \mathcal { L }$ . Let $\mathcal { H } _ { f }$ be the completion of $\mathcal { A } / \mathcal { L }$ with respect to the norm defined on $\mathcal { A } / \mathcal { L }$ by this inner product.

Because $\mathcal { L }$ is a left ideal of ${ \mathcal { A } } , x + { \mathcal { L } } { \mapsto } a x + { \mathcal { L } }$ is a well-defined linear transformation on $\mathcal { A } / \mathcal { L }$ Also, $\| a x + \mathcal { L } \| ^ { 2 } = \langle a x + \mathcal { L } , a x + \mathcal { L } \rangle = f ( x ^ { * } a ^ { * } a x ) .$ Now if $\| a a ^ { * } \|$ is considered as an element of  (it is a multiple of the identity), then an appeal to the functional calculus for $a ^ { * } a$ shows that $\| a ^ { * } a \| - a ^ { * } a \geqslant 0$

Hence (Exercise 3.7) $0 \leqslant x^{*}(\left \| a^{*}a \right \| - a^{*}a)x = \left \| a \right \|^{2}x^{*}x - x^{*}a^{*}ax;$ that is, $x^{*}a^{*}ax \leqslant \|a\|^{2}x^{*}x$ .Therefore $\| a x + \mathcal { L } \| ^ { 2 } \leqslant \| a \| ^ { 2 } f ( x ^ { * } x ) = \| a \| ^ { 2 } \| x + \mathcal { L } \| ^ { 2 }$ Thus if $\pi _ { f } ( a ) \colon { \mathcal { A } } / { \mathcal { L } } \to { \mathcal { A } } / { \mathcal { L } }$ is defined by $\pi _ { f } ( a ) ( x + { \mathcal { L } } ) = a x + { \mathcal { L } } , \pi _ { f } ( a )$ is a bounded linear operator with $\| \pi _ { f } ( a ) \| \leqslant \| \dot { a } \|$ . Hence $\pi _ { f } ( a )$ extends to an element of $\mathcal { B } ( \mathcal { H } _ { f } )$ . It is left to the reader to verify that $\dot { \pi } _ { f } \colon \mathcal { A } \to \mathcal { B } ( \mathcal { H } _ { f } )$ is a representation.

Put $e = 1 + \mathcal { L }$ in $\mathcal { H } _ { f } .$ Then $\pi_{f}(\mathcal{A})e=\{a+\mathcal{L}:a\in\mathcal{A}\}=\mathcal{A}/\mathcal{L}$ which, by definition, is dense in $\mathcal { H } _ { f }$ . Thus e is a cyclic vector for $\pi _ { f }$ . [Also note that $\langle \pi _ { f } ( a ) e , e \rangle = f ( a ) . ]$ This proves (a).

Now let $( \pi , \mathcal { H } ) , e .$ , and f be as in (b) and let $( \pi _ { f } , \mathcal { H } _ { f } )$ be the representation constructed. Let $e _ { f }$ be the cyclic vector for $\pi _ { f }$ so that $f ( a ) = \langle \pi _ { f } ( a ) e _ { f } , e _ { f } \rangle$ for all $a$ in $\rtimes$ Hence $\langle \pi _ { f } ( a ) e _ { f } , e _ { f } \rangle = \langle \pi ( a ) e , e \rangle$ for all a in $\varkappa$ Define $U$ on the dense manifold $\pi _ { f } ( \mathcal { A } ) e _ { f }$ in $\mathcal { H } _ { f }$ by $U \pi _ { f } ( a ) e _ { f } = \pi ( a ) e .$ Note that $\| \pi (a)e \|^2 = \langle \pi (a)e, \pi (a)e \rangle = \langle \pi (a^*a)e, \quad e \rangle = \langle \pi_f (a^*a)e_f, \quad e_f \rangle = \| \pi_f (a)e_f \|^2$ This implies that U is well defined and an isometry. Thus U extends to an isomorphism of $\mathcal { H } _ { f }$ onto $\mathcal { H }$ . If $x ,   a   \in { \mathcal { A } } ,$ then $U \pi _ { f } ( a ) \pi _ { f } ( x ) e _ { f } = U \pi _ { f } ( a x ) e _ { f } =$ $\pi ( a ) \pi ( x ) e = \pi ( a ) U \pi _ { f } ( x ) e _ { f }$ . Thus $\pi ( a ) U = U \pi _ { f } ( a )$ so that π and $\pi _ { f }$ are equivalent.

The Gelfand-Naimark-Segal construction is often called the GNS construction.

It is not difficult to show that if f is a positive linear functional on $\varkappa$ and $\alpha   >   0 ,$ then the representations $\pi _ { f }$ and $\pi _ { \alpha f }$ are equivalent (Exercise 8). So it is appropriate to only consider the cyclic representations corresponding to states. If $\varkappa$ is a $C ^ { * } \mathtt { - a l g e b r a }$ , let $S _ { \mathcal { A } } = \mathbf { t h } \mathbf { e }$ collection of all states on $\varkappa$ Note that $S _ { \mathcal { A } } \subseteq \mathrm { b a l l } \mathcal { A } ^ { * } . S _ { \mathcal { A } }$ is called the state space of $\varkappa$

5.15. Proposition. If A is a C\*-algebra with identity, then $s _ { \mathcal { A } }$ is a wea $l k ^ { * }$ compact convex subset of $\mathcal { A } ^ { * }$ and if $a \in \mathcal { A } _ { + }$ , then $\| a \| = \sup \left\{ f(a) : f \in S_{\mathcal{A}} \right\}$ and this supremum is attained.

PROOF. Since $S _ { \mathcal { A } } \subseteq \mathrm { b a l l } \mathcal { A } ^ { * }$ , to show that $s _ { \mathcal { A } }$ is wea $\mathbf { k } ^ { * }$ compact, it suffices to show that $S _ { \mathcal { A } }$ is weak\* closed. The reader can supply this proof using nets. Clearly $S _ { \mathcal { A } }$ is convex.

If ${ \mathcal { A } } = C ( X )$ with X compact and $f { \in } C ( X ) _ { + }$ , then there is a point x in X such that $f ( x )   =   \|   f   \|$ . Thus $\| f \| = \int f d \delta _ { x } = \sup \left\{ \int f d \mu : \mu \in \mathbb { C } \right\}$ (ball $M ( X ) ) _ { + } \}$ . If $\varkappa$ is arbitrary and $a \in \mathcal { A } _ { + }$ , then $\| a \| \geqslant \sup \left\{ f(a) : f \in S_{\mathcal{A}} \right\}$ . Also, from the argument in the abelian case, there is a state $f _ { 1 }$ on $C ^ { * } ( a )$ such that $f _ { 1 } ( a ) = \| a \|$ If we can show that $f _ { 1 }$ extends to a state $f$ on $\varkappa$ , the proof is complete. That this can be done is a consequence of the next result.

5.16. Proposition. Let $\mathcal { A } , \mathcal { B }$ be $C ^ { * } { - a l g e b r a s }$ with ${ \mathcal { B } } \subseteq { \mathcal { A } } . ~ I f f _ { 1 }$ is a state on B, then there is a state f on A such that $f | { \mathcal { B } } = f _ { 1 }$

ProoF. Consider the real linear spaces Re and $\mathbf { R e } \mathcal { B }$ If $a \in \mathcal { A } _ { + }$ , then $a \leqslant \| a \|$ in $\alpha$ Since $1 \in \mathbb { R e } \mathcal { B }$ , Re $\mathcal { B }$ has an order unit. By Corollary III.9.12, i $f _ { 1 }   \in   \mathrm { S } _ { \mathcal { H } }$ there is a positive linear functional f on Re  such that $f | \operatorname { R e } { \mathcal { B } } = f _ { 1 }$ Since $1 \in \mathcal { B } , f ( 1 ) = f _ { 1 } ( 1 ) = 1$ . Now let $f ( a ) = f ( ( a + a ^ { * } ) / 2 ) + i f ( ( a - a ^ { * } ) / 2 i )$ for an arbitrary a in . It follows that $f   \in   \mathcal { S } _ { \mathcal { A } }$ and $f | { \mathcal { B } } = f _ { 1 }$ ■

The next result says that every $C ^ { * } \mathtt { - a l g e b r a }$ is isomorphic to a C\*-algebra contained in $\mathcal { B } ( \mathcal { H } )$ for some $\mathcal { H }$ . Thus each C\*-algebra $\text{" } \mathbf{i} \mathbf{S} \text{" }$ an algebra of operators.

5.17. Theorem. If A is a C\*-algebra, then there is a representation $( \pi , \mathcal { H } )$ of $\mathcal { A }$ such that π is an isometry. If A is separable, then H can be chosen separable.

ProOF. Let F be a weak\* dense subset of $S _ { \mathcal { A } }$ and let $\pi = \oplus \left\{ \pi _ { f } \colon f { \in } F \right\}$ $\mathcal { H } = \oplus \left\{ \mathcal { H } _ { f } \colon f { \in } F \right\}$ . Thus $\| a \| ^ { 2 } \geqslant \| \pi ( a ) \| ^ { 2 } = \sup _ { f } \| \pi _ { f } ( a ) \| ^ { 2 }$ . If $e _ { f }$ is the cyclic vector for $\pi _ { f } ,$ then $\| e _ { f } \| ^ { 2 } = \langle e _ { f } , e _ { f } \rangle = \langle \pi _ { f } ( 1 ) e _ { f } , e _ { f } \rangle = f ( 1 ) = 1$ . Hence $\| \pi _ { f } ( a ) \| ^ { 2 } \geqslant \| \pi _ { f } ^ { ' } ( a ) e _ { f } \| ^ { 2 } = \langle \pi _ { f } ( a ^ { * } a ) e _ { f } ^ { ' } , e _ { f } ^ { ' } \rangle = f ( a ^ { * } a ) ,$ and $\| a \| ^ { 2 } \geqslant \| \pi ( a ) \| ^ { 2 } \geqslant$ sup $\{ f ( a ^ { * } a ) : { \stackrel { \cdot } { f \in F } } \}$ . Since F is weak\* dense in $S _ { \mathcal { A } } .$ , Proposition 5.15 implies sup $\{ f ( a ^ { * } a ) : f { \in } F \} = \| a ^ { * } a \| = \| a \| ^ { 2 }$ . Hence π is an isometry.

If  is separable, (ball $\mathcal { A } ^ { * } , \mathbf { w } \mathbf { k } ^ { * } )$ is a compact metric space (V.5.1). Hence $S _ { \mathcal { A } }$ is weak\* separable so that the set F of the preceding paragraph can be chosen to be countable. Now if $f { \in } F , \pi ( { \mathcal { A } } ) e _ { f }$ is a separable dense submanifold in $\mathcal { H } _ { f }$ since $\sphericalangle$ is separable. Thus $\mathcal { H } _ { f }$ is separable. It follows that $\mathcal { H }$ is separable. ■

Actually, more can be said if $\mathcal { A }$ is separable. In fact, every separable $c ^ { * } - a ^ { \prime }$ gebra has a cyclic representation that is isometric (Exercise 11).

## EXERCISES

1. Let $\mathcal { A }$ be a C\*-algebra with identity and let π: $\mathcal { A } \rightarrow \mathcal { B } ( \mathcal { H } )$ be a \*-homomorphism [but don't assume that $\pi ( 1 ) = 1 ]$ . Let $P _ { 1 } = \pi ( 1 )$ .Show that $P _ { 1 }$ is a projection and $\mathcal { H } _ { 1 } \equiv P _ { 1 } \mathcal { H }$ reduces $\pi ( \alpha )$ . If $\pi _ { 1 } ( a ) = \pi ( a ) | \mathcal { H } _ { 1 }$ , show that $\pi _ { 1 } \colon { \mathcal { A } } \to { \mathcal { B } } ( { \mathcal { H } } _ { 1 } )$ is a representation.

2. Show that the representation in Example 5.4 is a cyclic representation and find all of the cyclic vectors.

3. Show that the representation in Example 5.5 is a cyclic representation and find all the cyclic vectors.

4. If X is compact and $\mu$ is a positive measure on X, let $\pi _ { \mu } : C ( X ) \to { \mathcal { B } } ( L ^ { 2 } ( \mu ) )$ be the representation defined in Example 5.5. If $\mu , \nu$ are positive measures on X show that $\pi _ { \mu } \oplus \pi _ { \nu }$ is cyclic if and only if $\mu \perp \nu .$ If $\mu \perp v ,$ then $\pi _ { \mu } \oplus \pi _ { v }$ is equivalent to $\pi_{\mu + v} \cdot \mathrm{Also}, \pi_{\mu}^{(n)}$ is not cyclic if $n \geqslant 2$

5. Verify the statements in Example 5.8

6. If $\mathcal { A } = \mathbb { C } + \mathcal { B } _ { 0 } ( \mathcal { H } )$ and π: $\mathcal { A } \rightarrow \mathcal { B } ( \mathcal { H } )$ is the identity representation, show that $\pi ^ { ( \propto ) }$ is a cyclic representation.

7. Fix a Banach limit LIM on $l ^ { \infty } ( \mathbf { N } )$ and let $\mathcal { H }$ be a separable Hilbert space with an orthonormal basis $\{ e _ { n } \}$ . Define $f : \mathcal { B } ( \mathcal { H } ) \to \mathbb { C }$ by $f(T) = \mathrm{LIM} \left\{ \langle T e_n, e_n \rangle \right\}$ .Show that f is a state on $\mathcal { B } ( \mathcal { H } )$ . If $\pi _ { f }$ is the corresponding cyclic representation, show that ker $\pi _ { f }   =   \mathcal { B } _ { 0 } ( \mathcal { H } )$ . Hence $\pi _ { f }$ induces a cyclic representation of $\mathcal { B } ( \mathcal { H } ) / \mathcal { B } _ { 0 } ( \mathcal { H } )$ that is isometric. Is $\mathcal { H } _ { f }$ separable?

8. If f is a positive linear functional on $\nsim$ and $\alpha \in (0,\infty)$ , show that $\pi _ { f }$ and $\pi _ { \alpha f }$ are equivalent representations.

9. If $a   \in   \mathcal { A } .$ then $a   \geqslant   0$ if and only if $f(a) \geqslant 0$ for every state $f .$

10. If $a \in \mathcal { A }$ and $a \neq 0 ,$ then there is a state f on $\varkappa$ such that $f ( a ) \neq 0$

11. If $\varkappa$ is a separable C\*-algebra and $\{ f _ { n } \}$ is a countable weak\* dense subset of $s _ { \mathcal { A } } ,$ let $f = \textstyle \sum _ { n } 2 ^ { - n } f _ { n }$ . Show that $\pi _ { f }$ is an isometry.

# CHAPTER IX Normal Operators on Hilbert Space

In this chapter the Spectral Theorem for normal operators on a Hilbert space is proved. This theorem is then used to answer a number of questions concerning normal operators. In fact, the Spectral Theorem can be used to answer essentially every question about normal operators.

## §1. Spectral Measures and Representations of Abelian C\*-Algebras

Before beginning this section the reader should familiarize himself with the definitions and examples in (VIII.5.1) through (VIII.5.8)

In this secton we want to focus our attention on representations of abelian C\*-algebras. The reason for this is that the Spectral Theorem and its generalizations can be obtained as a special case of such a theory. The idea is the following. Let N be a normal operator on $\mathcal { H }$ Then $C ^ { * } ( N )$ is an abelian $C ^ { * }$ -algebra and the functional calculus $f { \mapsto } f ( N )$ is a \*-isomorphism of $C ( \sigma ( N ) )$ onto $C ^ { * } ( N )$ (VIII.2.6). Thus $f   \mapsto   f ( N )$ is a representation $C ( \sigma ( N ) )   \rightarrow   \mathcal { B } ( \mathcal { H } )$ of the abelian C\*-algebra $C ( \sigma ( N ) )$ . A diagnosis of such representations yields the Spectral Theorem.

A representation $\rho \colon C(X) \to \mathcal{B}(\mathcal{H})$ is a \*-homomorphism with $\rho ( 1 )   =   1$ Also, $\|   \rho   \| = 1 ( \mathrm { V I I I . 1 . 1 1 d } )$ . If $f   \in   { \cal C } ( X ) _ { + }$ , then $f = g ^ { 2 }$ where $g \in C ( X ) _ { + } ;$ hence $\rho ( f ) = \rho ( g ) ^ { 2 } = \rho ( g ) ^ { * } \rho ( g ) \geqslant 0.$ So $\rho$ is a positive map. One might expect, by analogy with the Riesz Representation Theorem, that $\rho ( f ) = \int f d E$ for some type of measure E whose values are operators rather than scalars. This is indeed the case. We begin by introducing these measures and defining the integral of a scalar-valued function with respect to one of them.

1.1. Definition. If X is a set, Ω is a σ-algebra of subsets of $X ,$ and $\mathcal { H }$ is a Hilbert space, a spectral measure for $( X , \Omega , \mathcal { H } )$ is a function $E \colon \Omega \to { \mathcal { B } } ( { \mathcal { H } } )$ such that:

(a) for each $\Delta$ in $\Omega ,   E ( \Delta )$ is a projection;

(b) $E ( \square ) = 0$ and $E ( X ) = 1 ;$

(c) $E ( \Delta _ { 1 } \cap \Delta _ { 2 } ) = E ( \Delta _ { 1 } ) E ( \Delta _ { 2 } )$ for $\Delta _ { 1 }$ and $\Delta _ { 2 }$ in $\Omega ;$

(d) if $\left\{ \Delta _ { n } \right\} _ { n = 1 } ^ { \infty }$ are pairwise disjoint sets from Ω, then

$$
E\left( \bigcup_{n = 1}^{\infty} \Delta_{n} \right) = \sum_{n = 1}^{\infty} E(\Delta_{n}).
$$

A word or two concerning condition (d) in the preceding definition. If $\{ E _ { n } \}$ is a sequence of pairwise orthogonal projections on $\mathcal { H }$ , then it was shown in Exercise II.3.5 that for each h in $\mathcal { H } , \sum _ { n = 1 } ^ { \infty } E _ { n } ( h )$ converges in $\mathcal { H }$ to $E ( h )$ , where E is the orthogonal projection of $\mathcal { H }$ onto $\vee \left\{ E_{n}(\mathcal{H}) : n \geqslant 1 \right\}$ . Thus it is legitimate to write $\begin{array} { r } { E = \sum _ { n = 1 } ^ { \infty } E _ { n } . } \end{array}$ Now if $\Delta _ { 1 } \cap \Delta _ { 2 } = \Box .$ , then (b) and (c) above imply that $0 = E(\Delta_{1})E(\Delta_{2}) = E(\Delta_{2})E(\Delta_{1});$ that is, $E ( \Delta _ { 1 } )$ and $E ( \Delta _ { 2 } )$ have orthogonal ranges. So if $\{ \Delta _ { n } \} _ { 1 } ^ { \infty }$ is a sequence of pairwise disjoint sets in $\Omega ,$ the ranges of $\{ E ( \Delta _ { n } ) \}$ are pairwise orthogonal. Thus the equation $E ( \bigcup _ { 1 } ^ { \infty } \Delta _ { n } ) = \Sigma _ { 1 } ^ { \infty } E ( \Delta _ { n } )$ in (d) has the precise meaning just discussed.

Another way to discuss this is by the introduction of two topologies that will also be of value later.

1.2. Definition. If $\mathcal { H }$ is a Hilbert space, the weak operator topology (WOT) on $\mathcal { B } ( \mathcal { H } )$ is the locally convex topology defined by the seminorms $\{ p _ { h , k ^ { * } }$ $h , k \in \mathcal { H }$ where $p _ { h , k } ( A ) = | \langle A h , k \rangle |$ . The strong operator topology (SOT) is the topology defined on $\mathcal { B } ( \mathcal { H } )$ by the family of seminorms $\{ p _ { h } : h \in \mathcal { H } \}$ , where $p _ { h } ( A ) = \| A h \|$

1.3. Proposition. Let H be a Hilbert space and let $\{ A _ { i } \}$ be a net in $\mathcal { B } ( \mathcal { H } )$

(a) $A _ { i } \rightarrow A \left( \mathrm { W O T } \right)$ if and only $\mathit { i f } \left\langle A _ { i } h , k \right\rangle \rightarrow \left\langle A h , k \right\rangle$ for all h, k in $\mathcal { H }$ (b) If $\operatorname { \mathfrak { s u p } } _ { i } \| A _ { i } \| < \infty$ and $\mathcal { T }$ is a total subset of $\mathcal { H }$ , then $A _ { i } \rightarrow A ( \mathrm { W O T } )   i f$ and only $i f \left\langle A _ { i } h , k \right\rangle \rightarrow \left\langle A h , k \right\rangle$ for all h, k in $\mathcal { T }$

(c) $A _ { i }   \rightarrow   A ( \mathrm { S O T } ) i f$ and only $if \parallel A_i h - A h \parallel \rightarrow 0$ for all h in $\mathcal { H } ,$ (d) $If \sup_{i} \| A_{i} \| < \infty$ and $\mathcal { T }$ is a total subset of $\mathcal { H }$ , then $A _ { i }   \rightarrow   A$ (SOT) if and only $if \left\| A_{i}h - A h \right\| \rightarrow 0$ for all h in $\mathcal { T }$

(e) If $\mathcal { H }$ is separable, then the WOT and SOT are metrizable on bounded subsets of $\mathcal { B } ( \mathcal { H } )$

ProoF. The proofs of (a) through (d) are left as exercises. $\mathbf { F o r } \left( \mathbf { e } \right)$ , let $\{ h _ { n } \}$ be any countable total subset of ball $\mathcal { H }$ If A, $B   \in   \mathcal { B } ( \mathcal { H } )$ , let

$$
d _ { s } ( A , B ) = \sum _ { n = 1 } ^ { \infty } 2 ^ { - n } \| ( A - B ) h _ { n } \| ,
$$

$$
d _ { w } ( A , B ) = \sum _ { m , n = 1 } ^ { \infty } 2 ^ { - n - m } | \zeta ( A - B ) h _ { n } , h _ { m } | .
$$

Then $d _ { s }$ and $d _ { w }$ are metrics on $\mathcal { B } ( \mathcal { H } )$ . It is left as an exercise to show that $d _ { s }$ and $d _ { w }$ define the SOT and WOT on bounded subsets of $\mathcal { B } ( \mathcal { H } )$ 1.

1.4. Example. Let $( X , \Omega , \mu )$ be a σ-finite measure space. If $\phi   \in   L ^ { \infty } ( \mu )$ , let $M _ { \phi }$ be the multiplication operator on $L ^ { 2 } ( \mu )$ . Then a net $\{ \phi _ { i } \}$ in $L ^ { \infty } ( \mu )$ converges weak\*to $\phi$ if and only if $M _ { \phi _ { i } }   \rightarrow   M _ { \phi } \left( \mathrm { W O T } \right)$ . In fact, if $f , g { \in } L ^ { 2 } ( \mu )$ and $\phi _ { i }   \rightarrow   \phi$ wea $\mathbf { k } ^ { * }$ in $L ^ { \infty } ( \mu ) _ { \mathrm { i } }$ then $\langle M _ { \phi _ { i } } ^ { ' } f , g \rangle = \int \phi _ { i } f \bar { g }   d \mu \to \int \phi f \bar { g }   d \mu = \langle M _ { \phi } f , g \rangle$ since $f { \bar { g } } { \in } L ^ { 1 } ( \mu )$ . Conversely, if $M _ { \phi _ { i } } \dot { \rightarrow } M _ { \phi } \left( \mathrm { W O T } \right)$ and $f   \in   \dot { L } ^ { 1 } ( \mu )$ , then $f = g _ { 1 } \bar { g } _ { 2 } .$ where $g _ { 1 } ,   g _ { 2 } { \in } L ^ { 2 } ( \mu )$ . (Why?) So $\int \phi _ { i } f d \mu = \langle M _ { \phi _ { i } } g _ { 1 } , g _ { 2 } \rangle \rightarrow \langle M _ { \phi } g _ { 1 } , g _ { 2 } \rangle = \int \phi f d \mu .$

1.5. Example. If $\{ E _ { n } \}$ is a sequence of pairwise orthogonal projections on $\mathcal { H } .$ then $\textstyle \sum _ { 1 } ^ { \infty } E _ { n }$ converges (SOT) to the projection of $\mathcal { H }$ onto $\textsf { V } \left\{ E _ { n } ( \mathcal { H } ) \right.$ $n \geqslant 1 \}$

In light of (1.5), a spectral measure for $( X , \Omega , \mathcal { H } )$ could be defined as a SOT-countably additive projection-valued measure.

1.6. Example. Let X be a compact set. $\Omega = \mathrm { t h e }$ Borel subsets of $X , \mu = a$ measure on $\Omega ,$ and $\mathcal { H } = L ^ { 2 } ( \mu )$ For ∆ in $\Omega ,$ let $E ( \Delta ) = { \mathrm { m u l t i p l i c a t i o n } }$ by $\chi _ { \Delta } ,$ the characteristic function of ∆. E is a spectral measure for $( X , \Omega , \mathcal { H } )$

1.7. Example. If E is a spectral measure for $( X , \Omega , { \mathcal { H } } ) .$ , the inflation, $E ^ { ( n ) }$ of E, defined by $E ^ { ( n ) } ( \Delta ) = E ( \Delta ) ^ { ( n ) }$ , is a spectral measure for $( X , \Omega , \mathcal { H } ^ { ( n ) } )$

1.8. Example. Let X be any set, $\Omega = a \Pi$ the subsets of $X , \mathcal { H } = \mathrm { a n y }$ separable Hilbert space, and fix a sequence $\left\{ x _ { n } \right\}$ in X. If $\{ e _ { 1 } , e _ { 2 } , \ldots \}$ is some orthonormal basis for $\mathcal { H }$ , define E(∆) = the projection onto $\vee \left\{ e _ { n } \colon x _ { n } { \in } \Delta \right\}$ . E is a spectral measure for $( X , \Omega , \mathcal { H } )$

The next lemma is useful in studying spectral measures as it allows us to prove things about spectral measures from known facts about complexvalued measures.

1.9. Lemma. If E is a spectral measure for $( X , \Omega , \mathcal { H } )$ and $g ,   h \in \mathcal { H } ,$ then

$$
E _ { g , h } ( \Delta ) \equiv \langle E ( \Delta ) g , h \rangle
$$

defines a countably additive measure on Ω with total variation $\leqslant \| g \| \| \boldsymbol { h } \|$

PROOF. That $\mu = E _ { g , h }$ as defined above, is a countably additive measure is left for the reader to verify. If $\Delta _ { 1 } , \ldots , \Delta _ { n }$ are pairwise disjoint sets in $\Omega ,$ let $\alpha _ { i } { \in } { \mathbb { C } }$ such that $| \alpha _ { j } | = 1$ and $| \langle E ( \Delta _ { j } ) g , h \rangle | = \alpha _ { j } \langle E ( \Delta _ { j } ) g , h \rangle$ . So $\begin{array} { r } { \sum _ { j } \lvert \mu ( \Delta _ { j } ) \rvert = } \end{array}$ $\sum_{j} \alpha_{j} \langle E(\Delta_{j})g, h \rangle = \langle \sum_{j} E(\Delta_{j})\alpha_{j}g, h \rangle \leq \| \sum_{j} E(\Delta_{j})\alpha_{j}g \| \| h \|$ .Now $\left\{ E ( \Delta _ { j } ) \alpha _ { j } g : 1 \leqslant j \leqslant n \right\}$ is a finite sequence of pairwise orthogonal vectors so that $\begin{array} { r } { \| \sum _ { j } \widehat { E ( \Delta _ { j } ) } \alpha _ { j } g \| ^ { 2 } = } \end{array}$ $\begin{array} { r } { \sum _ { j } \| E ( \Delta _ { j } ) g \| ^ { 2 } = \| E ( \bigcup _ { j = 1 } ^ { n } \Delta _ { j } ) g \| ^ { 2 } \leqslant \| g \| ^ { 2 } ; } \end{array}$ hence $\begin{array} { r } { \sum _ { j } | \mu ( \Delta _ { j } ) | \leqslant \| \stackrel { \cdot } { g } \|   \| \stackrel { \cdot } { h } \| } \end{array}$ Thus $\left\| \boldsymbol { \mu } \right\| \leqslant \left\| \boldsymbol { g } \right\| \left\| \boldsymbol { h } \right\|$ ■

It is possible to use spectral measures to define representations. The next