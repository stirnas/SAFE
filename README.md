#SAFE — Source-aware Argument Fidelity & Evidence
Open, vendor-neutral protocol · Machine-readable scoring engine · Web runtime

SAFE treats model output as claims, never as evidence.
Every substantive claim is extracted, classified, provenance-tracked, scored, audited, and returned as a structured, auditable object that any model or human can consume.

Constitutional North Star
Every design decision is evaluated against:

Civilisational continuation
Planetary restoration
Abundance for future generations
Core Epistemic Principles
Model Output ≠ Evidence
Claims are first-class, typed, machine-readable objects
Evidence Provenance Graph (independent convergence ≠ derivative echo)
Fundamental Knowledge Gate (Unknown / Tension / Strong Conflict / Potential Anomaly)
Bounded Ethical Audit (cannot inflate factual weight)
Transparent ASC (Argument Strength Coefficient) with full component breakdown
ASC Components
Code	Name	Description
E	Evidence Quality	Strength, directness, and relevance of supporting data
R	Source Reliability	Venue quality, peer-review status, author track record
I	Independence	Number of independent primary lineages (not reposts)
P	Replication	Existence and quality of independent replications
C	Contradiction Resistance	How well the claim survives high-quality contradictory evidence
T	Temporal Stability	Consistency of the evidence base over time
F	Fundamental Laws	Consistency with repeatedly validated physical / logical constraints
M	Methodology	Soundness of the methods used to generate the evidence
ASC is a transparent composite. All component scores and the aggregation function are versioned and auditable.

Repository Layout
SAFE/
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── protocol/               # JSON schemas (single source of truth)
│   ├── claims.schema.json
│   ├── evidence.schema.json
│   └── audit.schema.json
├── engine/                 # Core scoring & pipeline
│   ├── claim_extractor.py
│   ├── provenance.py
│   ├── scoring.py          # ASC calculator (minimal working version)
│   └── physics_gate.py
├── adapters/               # Model integration layers
│   ├── grok/
│   └── generic_api/
├── sources/                # Evidence fetchers (stubs)
├── web/                    # Duda-compatible runtime (next phase)
│   ├── safe.js
│   └── embed.html
├── benchmarks/
└── docs/
Quick Start (Engine)
cd engine
python -c "
from scoring import compute_asc
components = {
    'E': 91, 'R': 94, 'I': 82, 'P': 77,
    'C': 84, 'T': 96, 'F': 2, 'M': 88
}
result = compute_asc(components)
print(result)
"
Status
Phase 1 (current): Protocol schemas + minimal ASC engine
Phase 2: Full provenance graph + fundamental gate + reasoning audit
Phase 3: Web runtime (Duda embed) + Grok adapter
Phase 4: Live source connectors + adversarial benchmarks
Licence
MIT — see LICENSE

Contributing
See CONTRIBUTING.md. All contributions are evaluated against the constitutional tests above.
