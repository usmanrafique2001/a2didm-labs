# A2-DIDM Labs

Small, hands-on Python labs that rebuild the building blocks behind **A2-DIDM**, a scheme for proving ownership of a deep neural network without revealing the model or its training data. Later labs play the attacker: faking a model's training history and designing rules to catch the fakes.

Paper: T. Xie, K. Gai, J. Yu and L. Zhu, *A2-DIDM: Privacy-preserving Accumulator-enabled Auditing for Decentralized Identity of DNN Model*. [arXiv:2405.04108](https://arxiv.org/abs/2405.04108)

> These are toy models for learning. They are not secure and are not the paper's implementation.

## Play the game

**The Stolen Model Case** (`index.html`) is a short detective game that explains the same ideas through everyday stories, with no maths needed. It's hosted with GitHub Pages at `https://usmanrafique2001.github.io/a2didm-labs/`.

## The labs

| Lab | File | Idea | Link to A2-DIDM |
| --- | --- | --- | --- |
| 1 | `lab1.sh` | Hash sensitivity: same input, same hash; one change, a completely new hash | Checkpoint integrity |
| 2 | `lab2.py` | Salted commitment: seal a value now, reveal it later | Commitment to each checkpoint |
| 3 | `lab3.py` | Toy blockchain: tampering with one block breaks the chain | Tamper-evident public record |
| 4 | `lab4.py` | Merkle tree: one root commits to a whole list | Ledger digest |
| 5 | `lab5.py` | Schnorr proof: prove you know a secret without revealing it | Zero-knowledge proof |
| 6 | `lab6.py` | Commitments on a chain: a thief's own commitment verifies, but can't be swapped in | Ownership needs both |
| 6b | `lab6b.py` | A rebuilt chain is valid but doesn't match the copy everyone holds | 51% assumption |
| 7 | `lab7.py` | Merkle inclusion proof: prove one item is in the tree with a short path | Small proofs |
| 8 | `lab8.py` | Cave game simulation: a bluffer's odds halve every round | Completeness, soundness, zero knowledge |
| 9 | `lab9.py` | Faking a training history: two rules catch two fakers, a third slips through | Predicates and attacks M1, M2 |
| 9b | `lab9b.py` | My own rule: a "wander score" catches a too-straight fake | Designing detection rules |
| 10 | `lab10.py` | My own rule: real training slows down; a steady-pace fake doesn't | Echoes the paper's reason for Φ_CWCD |

Rules 2 to 4 in Labs 9 to 10 are my own simplified designs, not the paper's predicates. The paper's three predicates are Φ_CWCD (stops interpolation, M1), Φ_IWFW (stops starting near the final weights, M2) and Φ_MWCD (stops distillation, M3).

## Running

Python 3, standard library only.

```
bash lab1.sh
python3 lab2.py
```

The random labs (2, 5, 6, 6b, 8) print slightly different numbers each run, but the True/False pattern stays the same.

## Author

Usman Rafique, final-year cyber security and forensics student.
