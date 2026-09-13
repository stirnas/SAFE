"""
SAFE Engine — Fundamental Knowledge Gate (stub)

Future: maintain a small, versioned, publicly auditable seed set of
hard constraints (conservation laws, high-replication null results, etc.).
Route claims into: unknown | tension | strong_conflict | anomaly
"""

from __future__ import annotations
from typing import Dict, Any, List


# Seed constraints (illustrative only — expand via documented process)
SEED_CONSTRAINTS = [
    {
        "id": "energy_conservation",
        "statement": "In isolated systems, total energy is conserved.",
        "domain": "physics",
    },
    {
        "id": "second_law",
        "statement": "Entropy of an isolated system does not decrease.",
        "domain": "physics",
    },
]


def evaluate_fundamental_consistency(claim_text: str, domain_hints: List[str] | None = None) -> Dict[str, Any]:
    """
    Placeholder. Always returns 'unknown' until a real constraint matcher is built.
    """
    return {
        "result": "unknown",
        "explanation": "Stub gate — no constraint matching implemented yet.",
        "referenced_constraints": [],
        "seed_version": "0.1.0-illustrative",
    }
