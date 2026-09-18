# CSPC Computer Science for Physics and Chemistry
## PW1 Lab B: Data, Plotting, and Automation

- Data Analysis: The observed radioactive decay data starts at $N_0 = 5000$ and decreases over time, closely following the theoretical decay rate.
- Match with Analytical Law: The side-by-side plot confirms that the observed points closely align with the analytical curve $N(t) = N_0 e^{-\lambda t}$ using $\lambda = 0.3$.
- Snakemake Pipeline: The Snakemake pipeline automates the generation of `figure.png` from `decay_observed.csv` using `plot.py`, ensuring reproducibility by rebuilding the output only when source files change.
