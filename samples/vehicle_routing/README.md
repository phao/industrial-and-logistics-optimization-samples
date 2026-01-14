# Vehicle Routing Problem (VRP)

This example demonstrates solving the classic Vehicle Routing Problem using Google OR-Tools.

## Problem Description

The Vehicle Routing Problem (VRP) is a combinatorial optimization problem where:
- A fleet of vehicles must serve a set of customers
- All vehicles start and end at a central depot
- The goal is to minimize the total distance traveled
- Each customer must be visited exactly once
- Vehicles have constraints (capacity, maximum distance, etc.)

## Implementation

This implementation uses Google OR-Tools' constraint solver to find an optimal or near-optimal solution.

### Features:
- Distance matrix representation of locations
- Multiple vehicle routing
- Distance constraints per vehicle
- First solution heuristic for fast initial solution

## Running the Example

```bash
# Make sure you're in the project root and have installed dependencies
pip install -r requirements.txt

# Run the VRP solver
python samples/vehicle_routing/vrp_solver.py
```

## Expected Output

The solver will output:
- Total objective value (minimized distance)
- Route for each vehicle
- Distance traveled by each vehicle
- Maximum route distance

Example:
```
Objective: 6208
Route for vehicle 0:
 0 -> 9 -> 14 -> 16 -> 0
Distance of the route: 1552m

Route for vehicle 1:
 0 -> 7 -> 1 -> 4 -> 3 -> 0
Distance of the route: 1552m

...
```

## Customization

You can modify the problem by editing `vrp_solver.py`:
- **Distance matrix**: Change the distances between locations
- **Number of vehicles**: Adjust `data['num_vehicles']`
- **Depot location**: Change `data['depot']`
- **Maximum distance**: Modify the distance constraint in `AddDimension()`
- **Solution strategy**: Try different first solution heuristics

## References

- [OR-Tools VRP Documentation](https://developers.google.com/optimization/routing/vrp)
- [Vehicle Routing Problem (Wikipedia)](https://en.wikipedia.org/wiki/Vehicle_routing_problem)
