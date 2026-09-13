"""
SAFE Engine — Argument Strength Coefficient (ASC) calculator

Version: 1.0.0
Transparent, versioned, pure function.
Ethical desirability never enters the calculation.
"""

from __future__ import annotations
from typing import Dict, Any, Optional
import math


ASC_VERSION = "1.0.0"

# Default weights (must sum to 1.0 for the seven 0-100 components).
# F is treated as a signed adjustment outside the weighted average.
DEFAULT_WEIGHTS = {
    "E_evidence_quality": 0.18,
    "R_source_reliability": 0.15,
    "I_independence": 0.15,
    "P_replication": 0.12,
    "C_contradiction_resistance": 0.15,
    "T_temporal_stability": 0.10,
    "M_methodology": 0.15,
}

# F (fundamental laws) is a signed adjustment, typically -20 … +20
F_SCALE = 1.0  # multiplier applied to the F value before adding


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def compute_asc(
    components: Dict[str, float],
    weights: Optional[Dict[str, float]] = None,
    include_sensitivity: bool = True,
) -> Dict[str, Any]:
    """
    Compute the Argument Strength Coefficient from component scores.

    Parameters
    ----------
    components : dict
        Must contain the eight keys:
        E_evidence_quality, R_source_reliability, I_independence,
        P_replication, C_contradiction_resistance, T_temporal_stability,
        F_fundamental_laws, M_methodology
        (or the short forms E, R, I, P, C, T, F, M — both accepted).

    weights : optional dict
        Override default weights for the seven 0-100 components.
        Must sum approximately to 1.0.

    include_sensitivity : bool
        If True, attach a short sensitivity note.

    Returns
    -------
    dict with keys:
        asc_score (0-100),
        confidence (LOW/MEDIUM/HIGH/VERY_HIGH),
        components (normalised),
        version,
        sensitivity_note (optional)
    """
    # Normalise short keys to long form
    key_map = {
        "E": "E_evidence_quality",
        "R": "R_source_reliability",
        "I": "I_independence",
        "P": "P_replication",
        "C": "C_contradiction_resistance",
        "T": "T_temporal_stability",
        "F": "F_fundamental_laws",
        "M": "M_methodology",
    }
    norm: Dict[str, float] = {}
    for k, v in components.items():
        long_key = key_map.get(k, k)
        norm[long_key] = float(v)

    required = [
        "E_evidence_quality",
        "R_source_reliability",
        "I_independence",
        "P_replication",
        "C_contradiction_resistance",
        "T_temporal_stability",
        "F_fundamental_laws",
        "M_methodology",
    ]
    missing = [k for k in required if k not in norm]
    if missing:
        raise ValueError(f"Missing required component(s): {missing}")

    w = weights if weights is not None else DEFAULT_WEIGHTS.copy()

    # Weighted average of the seven 0-100 components
    weighted_sum = 0.0
    weight_total = 0.0
    for key, weight in w.items():
        if key not in norm:
            continue
        weighted_sum += norm[key] * weight
        weight_total += weight

    if weight_total <= 0:
        raise ValueError("Sum of weights must be positive")

    base = weighted_sum / weight_total

    # Apply F as signed adjustment
    f_adj = norm["F_fundamental_laws"] * F_SCALE
    asc = _clamp(base + f_adj)

    # Qualitative confidence band (simple heuristic)
    # Also consider variance of components as a rough uncertainty proxy
    vals = [norm[k] for k in required if k != "F_fundamental_laws"]
    mean = sum(vals) / len(vals)
    variance = sum((x - mean) ** 2 for x in vals) / len(vals)
    std = math.sqrt(variance)

    if asc >= 85 and std < 12:
        confidence = "VERY_HIGH"
    elif asc >= 70 and std < 18:
        confidence = "HIGH"
    elif asc >= 50:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    result: Dict[str, Any] = {
        "asc_score": round(asc, 2),
        "confidence": confidence,
        "components": {
            "E_evidence_quality": round(norm["E_evidence_quality"], 2),
            "R_source_reliability": round(norm["R_source_reliability"], 2),
            "I_independence": round(norm["I_independence"], 2),
            "P_replication": round(norm["P_replication"], 2),
            "C_contradiction_resistance": round(norm["C_contradiction_resistance"], 2),
            "T_temporal_stability": round(norm["T_temporal_stability"], 2),
            "F_fundamental_laws": round(norm["F_fundamental_laws"], 2),
            "M_methodology": round(norm["M_methodology"], 2),
        },
        "version": ASC_VERSION,
    }

    if include_sensitivity:
        # Simple sensitivity: what happens if we drop the highest and lowest weighted components
        result["sensitivity_note"] = (
            f"ASC {asc:.1f} under default weights v{ASC_VERSION}. "
            f"Component std≈{std:.1f}. "
            "Re-run with alternative weights for robustness checks."
        )

    return result


def validate_claim_object(claim: Dict[str, Any]) -> bool:
    """
    Minimal structural validation against the claims schema expectations.
    Full JSON-Schema validation should be added later (jsonschema library).
    """
    required_top = ["claim", "type", "status", "argument_strength", "fundamental_gate"]
    for k in required_top:
        if k not in claim:
            return False

    asc = claim["argument_strength"]
    if "asc_score" not in asc or "components" not in asc or "version" not in asc:
        return False

    comps = asc["components"]
    needed = [
        "E_evidence_quality", "R_source_reliability", "I_independence",
        "P_replication", "C_contradiction_resistance", "T_temporal_stability",
        "F_fundamental_laws", "M_methodology"
    ]
    return all(k in comps for k in needed)


if __name__ == "__main__":
    # Example usage matching the architecture document
    example_components = {
        "E": 91,
        "R": 94,
        "I": 82,
        "P": 77,
        "C": 84,
        "T": 96,
        "F": 2,
        "M": 88,
    }
    result = compute_asc(example_components)
    print("ASC Result:")
    for k, v in result.items():
        print(f"  {k}: {v}")
