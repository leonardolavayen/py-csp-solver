from typing import Dict, List, Any

class Constraint:
    def __init__(self, variables: List[str]):
        self.variables = variables
        
    def satisfied(self, assignment: Dict[str, Any]) -> bool:
        raise NotImplementedError

class CSPSolver:
    def __init__(self, variables: List[str], domains: Dict[str, List[Any]]):
        self.variables = variables
        self.domains = domains
        self.constraints: Dict[str, List[Constraint]] = {var: [] for var in variables}

    def add_constraint(self, constraint: Constraint):
        for var in constraint.variables:
            self.constraints[var].append(constraint)

    def is_consistent(self, var: str, assignment: Dict[str, Any]) -> bool:
        for constraint in self.constraints[var]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def solve(self, assignment: Dict[str, Any] = {}) -> Dict[str, Any] | None:
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]

        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            
         
            if self.is_consistent(first, local_assignment):
                result = self.solve(local_assignment)
                if result is not None:
                    return result
                    
        return None 
    