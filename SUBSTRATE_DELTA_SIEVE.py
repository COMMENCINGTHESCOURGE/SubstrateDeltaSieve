import math
from typing import Dict, Tuple

class SubstrateDeltaSieve:
    '''
    Operator Voice - Patch xiii: Multi-Metric Evaluation
    Match the delta type (Angular, Statistical, Symbolic) to the coordinate system.
    This acts as the Layer 1 filtering mechanism for processing external backend data 
    (from the 10.0.0.102 Cognitive Matrix).
    '''
    def __init__(self):
        self.metrics = {
            'angular': self._evaluate_angular,
            'statistical': self._evaluate_statistical,
            'symbolic': self._evaluate_symbolic
        }

    def _evaluate_angular(self, vector_a: Tuple[float, float, float], vector_b: Tuple[float, float, float]) -> float:
        # Cosine similarity for directional deviation
        dot = sum(a * b for a, b in zip(vector_a, vector_b))
        mag_a = math.sqrt(sum(a * a for a in vector_a))
        mag_b = math.sqrt(sum(b * b for b in vector_b))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot / (mag_a * mag_b)

    def _evaluate_statistical(self, current_distribution: list, historical_mean: float) -> float:
        # Variance-based sieve for constraint deviations (e.g. HordeThreat scaling)
        if not current_distribution:
            return 0.0
        variance = sum((x - historical_mean) ** 2 for x in current_distribution) / len(current_distribution)
        return variance

    def _evaluate_symbolic(self, semantic_node: str, established_ontology: list) -> bool:
        # Determines if a structural component fundamentally aligns with the Pangea Principle
        return semantic_node in established_ontology

    def process_delta(self, delta_type: str, *args) -> any:
        if delta_type not in self.metrics:
            raise ValueError(f"Delta type {delta_type} not supported by the Sieve.")
        
        return self.metrics[delta_type](*args)

if __name__ == "__main__":
    print("=== SUBSTRATE DELTA SIEVE: ONLINE ===")
    sieve = SubstrateDeltaSieve()
    
    # Example 2.5D Interpolation Check (Patch xi/xii)
    ang_diff = sieve.process_delta('angular', (1.0, 0.0, 0.0), (0.9, 0.1, 0.0))
    print(f"Angular Deviation: {ang_diff:.4f} (Checking snappiness integrity...)")
    
    # Constraint Field Variance
    stat_diff = sieve.process_delta('statistical', [0.8, 0.9, 0.7, 0.85], 0.5)
    print(f"Statistical Variance (Morale Drop): {stat_diff:.4f}")
    
    # Symbolic Grounding
    sym_check = sieve.process_delta('symbolic', 'GlassToWallRatio', ['GlassToWallRatio', 'Pangea Principle', 'Ghost Braid'])
    print(f"Symbolic Node Found: {sym_check}")
