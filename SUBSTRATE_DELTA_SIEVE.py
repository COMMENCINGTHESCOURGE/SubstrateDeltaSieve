import math
from typing import Dict, Tuple, List, Union, Any

class SubstrateDeltaSieve:
    '''
    Multi-Metric Field-Delta Evaluator
    Harmonizes legacy documentation contracts with FracType/Mod-9 Vinculum Governance.
    '''
    def __init__(self):
        self.metrics = {
            'angular': self._evaluate_angular,
            'statistical': self._evaluate_statistical,
            'symbolic': self._evaluate_symbolic
        }

    def _evaluate_angular(self, *args) -> float:
        """
        Handles both thermal/EM vectors and standard tuple dot products.
        Returns cosine similarity / stealth rating in [-1.0, 1.0].
        """
        if len(args) == 2:
            vec_a, vec_b = args[0], args[1]
        else:
            raise ValueError("Angular evaluation requires 2 vector inputs.")
            
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        mag_a = math.sqrt(sum(a * a for a in vec_a))
        mag_b = math.sqrt(sum(b * b for b in vec_b))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot / (mag_a * mag_b)

    def _evaluate_statistical(self, *args) -> float:
        """
        Polymorphic statistical evaluator:
        - If passed (solution_nodes: List[int], common_ancestor: int): returns Mycelium compression ratio.
        - If passed (data_list: List[float], target: float): returns population variance float.
        """
        if len(args) == 2 and isinstance(args[0], list):
            data, param = args[0], args[1]
            if all(isinstance(x, int) for x in data) and isinstance(param, int):
                if not data or param == 0:
                    return 0.0
                unique_roots = set(node // param for node in data if node % param == 0)
                apparent_count = len(data)
                true_count = len(unique_roots) if unique_roots else 1
                return apparent_count / true_count
            else:
                mean = sum(data) / len(data) if data else 0.0
                variance = sum((x - mean) ** 2 for x in data) / len(data) if data else 0.0
                return float(variance)
        raise ValueError("Invalid parameters for statistical evaluation.")

    def _evaluate_symbolic(self, *args) -> bool:
        """
        Polymorphic symbolic evaluator:
        - Ontology Mode: process_delta('symbolic', node_name, ontology_list) -> bool
        - FracType Mode: process_delta('symbolic', base_class, omega_mult, apparent, hidden) -> bool
        """
        if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], list):
            node, ontology = args[0], args[1]
            return node in ontology
        elif len(args) >= 2 and isinstance(args[0], int) and isinstance(args[1], int):
            base_class, omega_multiplier = args[0], args[1]
            resulting_state = (base_class * omega_multiplier) % 9
            if (resulting_state * 3) % 9 in {0, 3, 6} and omega_multiplier == 3:
                return False
            return True
        else:
            return False

    def process_delta(self, delta_type: str, *args) -> Any:
        if delta_type not in self.metrics:
            raise ValueError(f"Delta type '{delta_type}' not supported.")
        return self.metrics[delta_type](*args)


if __name__ == "__main__":
    sieve = SubstrateDeltaSieve()
    
    # Legacy / README usage
    print("Angular Similarity:", sieve.process_delta('angular', (1.0, 0.0, 0.0), (0.9, 0.1, 0.0)))
    print("Statistical Variance:", sieve.process_delta('statistical', [0.8, 0.9, 0.7, 0.85], 0.5))
    print("Symbolic Ontology Match:", sieve.process_delta('symbolic', 'GlassToWallRatio', ['GlassToWallRatio', 'Pangea Principle']))
    
    # Advanced FracType / Mycelium usage
    print("Mycelium Compression:", sieve.process_delta('statistical', [32000000, 32000000, 128000000], 32000000))
    print("FracType x3 Breach Detection:", sieve.process_delta('symbolic', 2, 3, "Public_UI", "Hidden_Torsion"))
