"""
Optimization Model for Raw Material Blending
--------------------------------------------
Problem: Minimize cost of producing a final product by blending 5 raw oils 
(Vegetable and Non-Vegetable) subject to:
  1. Hardness constraints (Quality Control)
  2. Refining capacity constraints (Logistics)
  3. Production targets

Solvers Compared: 
  - GLOP (Google Linear Optimization Package) - Simplex-based
  - PDLP (Primal Dual Hybrid Gradient) - First-order method suitable for large scale
  - SCIP (Solving Constraint Integer Programs) - Mixed-Integer Solver

Author: Pedro Henrique Antunes de Oliveira
Reference: H.P. Williams, Model Building in Mathematical Programming (Example 1.2)
"""

from ortools.linear_solver import pywraplp

def solve_blending_problem(solver_name="GLOP"):
    print(f"\n--- Running Optimization with {solver_name} ---")
    
    # 1. Initialize Solver
    solver = pywraplp.Solver.CreateSolver(solver_name)
    if not solver:
        print(f"Error: Could not create solver {solver_name}")
        return

    # 2. Data / Parameters
    # Oils: VEG1, VEG2, NVEG1, NVEG2, NVEG3
    costs = [110, 120, 130, 110, 115]      # Cost per ton
    hardness = [8.8, 6.1, 2.0, 5.2, 5.0]   # Hardness index
    
    # Capacities
    max_veg = 200
    max_nveg = 250
    
    # Product Requirements
    min_hardness = 3.0
    max_hardness = 6.0
    revenue_per_ton = 150
    
    oil_names = ["VEG1", "VEG2", "NVEG1", "NVEG2", "NVEG3"]
    veg_oil_indices = [0, 1]
    nveg_oil_indices = [2, 3, 4]
    num_oils = len(oil_names)

    # 3. Decision Variables
    # x[i] = tons of oil i to use. 
    # Continuous variables (>= 0).
    x = [solver.NumVar(0, solver.infinity(), name) for name in oil_names]

    # 4. Constraints
    
    # Helper expressions
    total_production = sum(x)
    total_hardness_weighted = sum(x[i] * hardness[i] for i in range(num_oils))
    
    # Constraint A: Refining Capacity (Vegetable Oils)
    # 𝚺_{i in VEG} x[i] <= 200
    solver.Add(sum(x[i] for i in veg_oil_indices) <= max_veg)

    # Constraint B: Refining Capacity (Non-Vegetable Oils)
    # 𝚺_{i in NVEG} x[i] <= 250
    solver.Add(sum(x[i] for i in nveg_oil_indices) <= max_nveg)

    # Constraint C: Hardness Range (Linearized)
    # Original: 3 <= (Weighted_Hardness / Total_Prod) <= 6
    # Linearized Lower: 3 * Total_Prod - Weighted_Hardness <= 0
    solver.Add(3 * total_production - total_hardness_weighted <= 0)
    
    # Linearized Upper: Weighted_Hardness - 6 * Total_Prod <= 0
    solver.Add(total_hardness_weighted - 6 * total_production <= 0)

    # 5. Objective Function: Maximize Profit
    # Profit = Revenue - Cost
    total_cost = sum(x[i] * costs[i] for i in range(num_oils))
    total_revenue = revenue_per_ton * total_production
    solver.Maximize(total_revenue - total_cost)

    # 6. Solve and Report
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Status: OPTIMAL")
        print(f"Total Profit: ${solver.Objective().Value():.2f}")
        print(f"Total Production: {total_production.solution_value():.2f} tons")
        
        # Calculate final hardness to verify constraint
        final_h = total_hardness_weighted.solution_value() / total_production.solution_value()
        print(f"Final Hardness: {final_h:.2f} (Target: {min_hardness}-{max_hardness})")
        
        print("Composition:")
        for i in range(num_oils):
            if x[i].solution_value() > 0:
                print(f"  - {oil_names[i]}: {x[i].solution_value():.2f} tons")
                
        # Performance Metrics
        print(f"Solver Time: {solver.wall_time()/1000.0:.4f} ms")
        print(f"Iterations: {solver.iterations()}")
    else:
        print("The problem does not have an optimal solution.")

if __name__ == "__main__":
    # Compare different solvers to validate stability and performance
    solve_blending_problem("GLOP") # Simplex
    solve_blending_problem("PDLP") # First-order method
    solve_blending_problem("SCIP") # Mixed-Integer