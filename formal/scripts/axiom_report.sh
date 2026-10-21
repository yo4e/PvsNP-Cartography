#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
lake env lean PvsNPCartography/AxiomAudit.lean
lake env lean PvsNPCartography/SymmetryAxiomAudit.lean
lake env lean PvsNPCartography/LayerAxiomAudit.lean
lake env lean PvsNPCartography/ElevenAxiomAudit.lean
lake env lean PvsNPCartography/BalancedDualAxiomAudit.lean
lake env lean PvsNPCartography/CountingAxiomAudit.lean
lake env lean PvsNPCartography/FibersAxiomAudit.lean
