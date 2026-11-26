# Q598: Sharp dimension dependence for isotropic Gaussian noiseless preferences

For n,d≥1, the minimax expected Euclidean error over θ∈[−1,1]^d is

  Θ(min{√(d/n), d^(3/2)/n}),

with absolute constants. This closes the source's dimension gap and removes logarithmic factors for the specified Gaussian model.

## Representation

Write M=(X+Y)/2 and U=(X−Y)/||X−Y||. Then M∼N_d(θ,I/2) and U is independently uniform on the unit sphere. Set B=U·M and T=U·θ. The sign of the log Gaussian density difference equals sign(T−B) by expanding the two squared distances. Ties and X=Y have probability zero. Write G=B−T. Conditional on U and θ, G∼N(0,1/2), so G is independent of U. Use iid copies for all observations.

## Lower bound: labels carry O(a) nats per pair under a hypercube prior

Take θ=aS with independent fair signs S_j, a=c min{n^(−1/2),d/n}, and c>0 a sufficiently small universal constant (in particular c≤1). All points lie in the cube. Let W denote all observed Gaussian pairs and Z all comparison labels. Relative to the law for θ=0, each pair has Gaussian KL ||θ||²=da². The usual reference-law decomposition gives I(S;W)≤nda².

For the labels use, as a reference predictor using only each observed pair, a logistic forecast which favors sign(−B) at log odds |B|/a. Its log loss at the actual label is log(1+exp(−|B|/a)) plus (|B|/a) times the indicator that B lies strictly between 0 and T, ignoring null ties. This follows by comparing logistic losses at complementary labels. Conditional on θ,U the B-density is bounded by 1/√π. Thus expected first term is at most 2a/√π (bound log(1+z) by z and integrate), and the flip term is at most T²/(2a√π) (integrate |B|/a between 0 and T). By spherical symmetry E_U[T²|θ]=||θ||²/d=a². The sum is at most C a. Conditional entropy is at most any reference conditional cross entropy, so H(Z|W)≤Cna, using the product of the forecasts as reference. No independence of the actual labels after conditioning on W is needed. Consequently I(S;W,Z)≤nda²+Cna≤(c²+Cc)d. Here na≤cd and na²≤c² by the definition of a.

Choosing c small enough makes I≤d(log 2−h(1/4)), where h is binary entropy in nats. For the coordinatewise best sign guesses, with error probabilities e_j, conditional entropy subadditivity and binary Fano give d log 2−I≤Σ_j h(e_j)≤d h(Σ_j e_j/d). These guesses have error ≤1/2, so the expected Hamming error is at least d/4, and any other guesses are no better. For an arbitrary estimator infer its coordinate signs, breaking zeros deterministically. A sign error entails coordinate absolute error ≥a. For Hamming error H, its Euclidean error is ≥a√H≥a H/√d. The Bayes risk, hence minimax risk, is at least a√d/4, as required.

## Upper bound: all consistent parameters localize at the sharp scale

Intersect the cube with the halfspaces given by all the observed labels, in the form Z_i U_i·(θ'−M_i)≥0. Take any measurable feasible output (for example, choose the lexicographically minimized coordinates over the compact feasible polytope). Equivalently one can select the first rational point in a fixed enumeration of the cube satisfying the inequalities strictly: the true θ satisfies all strictly almost surely, so a relative neighborhood contains such a rational point. For a displacement h=θ'−θ, consistency is equivalent to V_i·h≤|G_i| for every i, where V_i=sgn(G_i)U_i. The V_i are iid spherical and independent of the magnitudes |G_i|.

For 0<t≤2√d, select observations with |G_i|≤t/(4√d). Their count N_t is binomial of mean μ≥c₀nt/√d, by the positive minimum of the N(0,1/2) density on [−1/2,1/2]. Given the selection and count, their V_i are still iid uniform. For each unit vector v, the cap {V:V·v≥1/(2√d)} has mass at least 3/32: E(V·v)²=1/d, E(V·v)^4=3/[d(d+2)]≤3/d², and Paley–Zygmund at one quarter of the second moment, then sign symmetry, give 3/32. For d=1 the direct two-point sphere has cap mass 1/2, also sufficient.

An iid spherical sample of m≥C₁d hits all these caps except with probability ≤C₂exp(−c₁m). Indeed the caps are a subclass of affine halfspaces, of VC dimension ≤d+1. In the double-sampling proof, if the first m misses a cap of mass at least p₀=3/32, the second m contains at least p₀m/2 points of it with probability at least 1/2 for m large enough. Condition on the combined pool and randomly partition it into the two samples. There are at most (2em/(d+1))^(d+1) distinct index traces by the Sauer–Shelah bound, and for each trace of size at least p₀m/2 the chance all its indices are in the second half is at most 2^(−p₀m/2). Twice their product is ≤C₂exp(−c₁m) for m≥C₁d with a sufficiently large universal C₁. Standard VC measurability applies to these finite-dimensional halfspaces; alternatively use a countable dense sphere of v with an arbitrarily small reduction in the cap threshold if needed, preserving a strict margin over 1/(4√d).

When the selected directions hit all caps, any h with ||h||>t violates consistency: hit the cap of v=h/||h||, so V_i·h>t/(2√d)>|G_i|. By a binomial lower-tail bound and the preceding event, uniformly in true θ, for C₃d^(3/2)/n≤t≤2√d we have
 Pr(||θ̂−θ||>t) ≤ C₄ exp(−c₂ nt/√d).
Integrating the tail gives expected error O(d^(3/2)/n); if the lower endpoint exceeds the cube's diameter, the trivial bound already suffices. The clipped average of the M_i has expected norm error ≤√(d/(2n)) by its covariance and nonexpansive clipping. Pick the appropriate estimator by n versus d² to get the minimum of the two rates.

## Scope

[Jourdan, Yüce and Flammarion, §5 “Dimensionality gap”](https://arxiv.org/html/2505.23557v1#S5) explicitly pose the gap in the Gaussian specialization; their feasible set and basic Gaussian representation are known inputs (see §4 and Appendix F). The new lower bound uses conditional entropy rather than worst-pair comparison. The upper bound uses all directions from the small-offset subsample, without a mesh of vanishing angular radius. This is for means in the stated cube, known identity covariance, parameter-dependent Gaussian draws and noiseless preferences. No generalization to other preference models or claim of priority.
