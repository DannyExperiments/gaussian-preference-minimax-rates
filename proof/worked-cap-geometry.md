# Six comparison cuts in three dimensions

Take the true mean at zero and use the six outward normals ±e₁, ±e₂, ±e₃. For a normal u, set the midpoint M = u/16 and take X = M + u/2 and Y = M − u/2. Then Y is nearer to zero. The comparison requires that any feasible displacement h satisfy u·h ≤ 1/16. These six constraints cut the parameter cube down to [−1/16,1/16]³. Its greatest Euclidean distance from the truth is √3/16.

The proof tests a radius t = 1/2 by considering offsets at most t/(4√3) = 1/(8√3). All six offsets qualify. For any direction v, the largest coordinate magnitude is at least 1/√3, so one signed coordinate normal has dot product at least 1/√3 with v. This exceeds the proof's cap threshold 1/(2√3). Every candidate of length greater than t fails a comparison, as seen directly from the smaller feasible cube as well.

Removing any one constraint admits a point at distance 3/4 in its outward direction. This gives a simple illustration of the need for simultaneous directional coverage. The constructed comparisons are deterministic examples. The theorem obtains suitable nearby constraints from the specified Gaussian experiment and uses all observed constraints in its estimator.

[Exact checks](../verification/results/replay.txt) · [Offline explorer](../visualization/nearby-comparison-explorer.zip)
