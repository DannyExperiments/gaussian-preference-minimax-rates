# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay checks 324 logistic loss decompositions, 180 exact information-scale and crossover cases, 343 geometry fixtures, and six witnesses from deleting a face. It compares the two sides of each algebraic identity by rational arithmetic. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/nearby-comparison-explorer.zip) and open index.html to rotate the feasible box or remove a comparison. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font parameters. [Build the paper](paper/BUILD.md).
