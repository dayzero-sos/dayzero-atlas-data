# DayZero Requirements Atlas: data

The public data lake behind the DayZero Requirements Atlas: the obligations that U.S. defense development programs owe for ten program data products, extracted from publicly released government documents, rewritten as verifiable requirements, and hashed.

- `records/F1..F10.json`: one record per obligation (1804 in release 1), each with the verbatim source passage, its SHA-256, the engineered wording, its SHA-256, actor, condition, verification intent, `binding` (operative vs guidance) and `status`. Every record in this repository is `sample`: a paraphrase awaiting human review. Reviewed records are not published here.
- `contracts/F1..F10.json`: the data contract for each feed (formats, keys, required fields, acceptance rules, canonical form) with three fictional HALCYON sample rows.
- `catalog/`: the governing-document register with editions, issuers, release statements and copyright classes; per-feed source audits; the MIL-HDBK-539A sections cited.
- `edges.csv`: invokes / implements / tailors / supersedes / companion relations between records and documents.
- `schema/`: the record schema and the hashing rule. `tools/verify.py` recomputes every hash, the release manifest, and fails on any personal or employer identifier.

The ten feeds: F1 requirements baseline, F2 contract set (SOW, CDRL, spec tree), F3 IMS, F4 EVM/IPMDAR, F5 WBS, F6 risk/issue/opportunity register, F7 technical review record, F8 verification evidence, F9 configuration status accounting, F10 RACI/staffing.

Known gaps in release 1 (listed per feed in `catalog/`): DoDI 5000.88, DoDM 5010.12, DoDI 5230.24, DoDI 5200.48, DoDM 5200.01 Vol 2 and 4, DD Forms 1423/1692/1694 instructions. Nothing was extracted from them.

Every scenario is fictional (HALCYON). No program, contractor or customer content. Copyrighted SDO standards (SAE, ISO/IEC/IEEE, OMG, RTCA) appear as metadata only.

Licence: see LICENSE (ODbL for data, Apache-2.0 for schema and tools).
