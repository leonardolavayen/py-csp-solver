from typing import Dict, Any, List
from solver.csp import Constraint

class SumConstraint(Constraint):
    def __init__(self, variables: List[str], target_sum: int):
        super().__init__(variables)
        self.target_sum = target_sum

    def satisfied(self, assignment: Dict[str, Any]) -> bool:
        assigned = [assignment[var] for var in self.variables if var in assignment]
        unassigned_count = len(self.variables) - len(assigned)
        current_sum = sum(assigned)
        
        if current_sum > self.target_sum:
            return False
            
        if current_sum + unassigned_count < self.target_sum:
            return False
            
        return True

