# Substrate Delta Sieve

Multi-metric field-delta evaluator for streamed workloads.

The module exposes three evaluators that each reduce one kind of delta to a comparable signal:
- `angular`
- `statistical`
- `symbolic`

It is intentionally dependency-light so it can run in a notebook or on a GPU node.

## Install

```bash
git clone https://github.com/COMMENCINGTHESCOURGE/SubstrateDeltaSieve.git
cd SubstrateDeltaSieve
python -m SUBSTRATE_DELTA_SIEVE
```

## Run

```bash
python -m SUBSTRATE_DELTA_SIEVE
```

## Usage

```python
from SUBSTRATE_DELTA_SIEVE import SubstrateDeltaSieve

sieve = SubstrateDeltaSieve()

angular = sieve.process_delta('angular', (1.0, 0.0, 0.0), (0.9, 0.1, 0.0))
statistical = sieve.process_delta('statistical', [0.8, 0.9, 0.7, 0.85], 0.5)
symbolic = sieve.process_delta('symbolic', 'GlassToWallRatio', ['GlassToWallRatio', 'Pangea Principle', 'Ghost Braid'])
```

## Validate

```bash
python -m unittest discover
```

## Output contract

- `angular` returns cosine similarity in [-1.0, 1.0]
- `statistical` returns variance as a float
- `symbolic` returns True when the node is in the ontology list
