from typing import Dict, Any, List, Optional

class FormAutofillMultiStepDependencyFiller:
    """
    Plans sequential fill actions for interdependent form fields
    (e.g., selecting Country unlocks State/Province dropdown, which enables City input).
    """
    DEPENDENCY_EDGES = {
        "state": "country",
        "province": "country",
        "postal_code": "state",
        "shipping_method": "postal_code"
    }

    def plan_autofill_sequence(self, target_data: Dict[str, Any], available_fields: List[str]) -> Dict[str, Any]:
        execution_order = []
        visited = set()

        def visit(field):
            if field in visited:
                return
            parent = self.DEPENDENCY_EDGES.get(field)
            if parent and parent in target_data and parent in available_fields:
                visit(parent)
            visited.add(field)
            execution_order.append(field)

        for f in available_fields:
            if f in target_data:
                visit(f)

        plan = []
        for step_num, field_name in enumerate(execution_order, 1):
            val = target_data.get(field_name)
            is_parent = any(p == field_name for p in self.DEPENDENCY_EDGES.values())
            plan.append({
                "step": step_num,
                "field": field_name,
                "value": val,
                "requires_change_event_dispatch": is_parent,
                "settle_delay_ms": 300 if is_parent else 50
            })

        return {
            "total_steps": len(plan),
            "execution_plan": plan
        }
