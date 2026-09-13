"""
SAFE Engine — Evidence Provenance Graph (stub)

Future responsibilities:
- Deduplicate derivative sources (news → blog → Wikipedia → AI answer)
- Assign lineage_ids to independent primary studies
- Compute independence score (I component)
"""

from __future__ import annotations
from typing import List, Dict, Any


def build_provenance_graph(evidence_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Placeholder. Returns a trivial graph treating every item as independent.
    """
    lineages = {}
    for i, item in enumerate(evidence_items):
        lid = item.get("lineage_id") or f"lineage_{i}"
        if lid not in lineages:
            lineages[lid] = []
        lineages[lid].append(item.get("id", f"ev_{i}"))

    return {
        "lineages": lineages,
        "independent_count": len(lineages),
        "note": "Stub implementation — treats every evidence item as independent primary.",
    }


def independence_score(graph: Dict[str, Any]) -> float:
    """Simple heuristic: more independent lineages → higher score (capped)."""
    n = graph.get("independent_count", 0)
    if n <= 0:
        return 0.0
    if n == 1:
        return 40.0
    if n == 2:
        return 65.0
    if n == 3:
        return 80.0
    return min(100.0, 80.0 + (n - 3) * 5)
