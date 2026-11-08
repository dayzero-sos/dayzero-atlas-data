# Hashing rule

Every SHA-256 in this dataset is computed over the text after: UTF-8, Unicode NFC, trim, internal whitespace collapsed to single spaces, no trailing newline; lowercase hex digest.

`passageSHA256` covers `source.passage` (verbatim source text). `wordingSHA256` covers `wording` (the engineered requirement). A release manifest hashes the sorted list of `(id, wordingSHA256, source.docId, source.paragraph, passageSHA256)` as canonical JSON without whitespace. Guidance records (`binding: false`) are catalogued but excluded from baseline manifests.

## Schema v1.1 (2026-11-08)

Optional fields `party`, `rights`, `tailoring` and `prov` were added to the record schema. They are additive: a v1 record is a valid v1.1 record, and none of them enters the manifest rows, so a release hashes to the same manifest under both versions. `tools/verify.py` reads both and fails on an invalid value when a field is present.
