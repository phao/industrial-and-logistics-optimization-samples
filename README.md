# Supply Chain Optimization: Blending Problem

This repository demonstrates a **Linear Programming (LP)** approach to solving a multi-constraint blending problem, commonly found in process industries (Chemical, Food, Cosmetics).

## The Challenge
We must determine the optimal mix of 5 raw materials (Oils) to produce a final product that meets:
1.  **Quality Standards:** The final product's "hardness" must be between 3.0 and 6.0.
2.  **Operational Constraints:** Refining capacity is limited for Vegetable (200 tons) and Non-Vegetable (250 tons) oils.
3.  **Business Objective:** Maximize total profit given fluctuating raw material costs.

## Implementation Details
-   **Library:** Google OR-Tools (`pywraplp`).
-   **Solvers Tested:**
    -   **GLOP:** Google's primal simplex solver (Standard for LP).
    -   **PDLP:** Primal-Dual Hybrid Gradient (Suitable for very large-scale problems).
    -   **SCIP:** Solving Constraint Integer Programs (demonstrating MIP capability).
-   **Technique:** The non-linear quality constraint `3 <= (Weighted_Sum / Total) <= 6` was linearized to the equivalent pair `Weighted_Sum - 6*Total <= 0` and `3*Total - Weighted_Sum <= 0` to fit the **Standard Linear Programming** framework ($Ax \le b$).

## Results
The model successfully converges to an optimal profit of **$16,666.67**, utilizing full capacity of Non-Vegetable refining (250 tons) and partial Vegetable capacity, achieving the exact upper bound of hardness (6.0) to minimize cost.
