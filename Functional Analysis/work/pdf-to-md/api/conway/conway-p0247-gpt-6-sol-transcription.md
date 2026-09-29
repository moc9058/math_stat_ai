# CHAPTER VIII

# $C^*$-Algebras

A $C^*$-algebra is a particular type of Banach algebra that is intimately connected with the theory of operators on a Hilbert space. If $\mathcal H$ is a Hilbert space, then $\mathcal B(\mathcal H)$ is an example of a $C^*$-algebra. Moreover, if $\mathcal A$ is any $C^*$-algebra, then it is isomorphic to a subalgebra of $\mathcal B(\mathcal H)$ (see Section 5). Some of the general theory developed in this chapter will be used in the next chapter to prove the Spectral Theorem, which reveals the structure of normal operators.

A more thorough treatment of $C^*$-algebras is available in Arveson [1976] or Sakai [1971].

## §1. Elementary Properties and Examples

If $\mathcal A$ is a Banach algebra, an *involution* is a map $a\mapsto a^*$ of $\mathcal A$ into $\mathcal A$ such that the following properties hold for $a$ and $b$ in $\mathcal A$ and $\alpha$ in $\mathbb C$:

(i) $(a^*)^*=a$;  
(ii) $(ab)^*=b^*a^*$;  
(iii) $(\alpha a+b)^*=\bar\alpha a^*+b^*$.

Note that if $\mathcal A$ has involution and an identity, then $1^*\cdot a=(1^*\cdot a)^{**}=(a^*\cdot1)^*=(a^*)^*=a$; similarly, $a\cdot1^*=a$. Since the identity is unique, $1^*=1$. Also, for any $\alpha$ in $\mathbb C$, $\alpha^*=\bar\alpha$.

**1.1. Definition.** A $C^*$-algebra is a Banach algebra $\mathcal A$ with an involution such that for every $a$ in $\mathcal A$,

$$
\|a^*a\|=\|a\|^2.
$$
