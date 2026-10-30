from typing import Dict, Any
from solver.csp import Constraint


class UniqueConstraint(Constraint):
    def satisfied(self, assignment: Dict[str, Any]) -> bool:
        assigned_values = [
            assignment[var] for var in self.variables 
            if var in assignment
        ]
        return len(assigned_values) == len(set(assigned_values))


