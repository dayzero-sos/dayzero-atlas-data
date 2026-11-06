# Hashing rule

Every SHA-256 in this dataset is computed over the text after: UTF-8, Unicode NFC, trim, internal whitespace collapsed to single spaces, no trailing newline; lowercase hex digest.

`passageSHA256` covers `source.passage` (verbatim source text). `wordingSHA256` covers `wording` (the engineered requirement). A release manifest hashes the sorted list of `(id, wordingSHA256, source.docId, source.paragraph, passageSHA256)` as canonical JSON without whitespace. Guidance records (`binding: false`) are catalogued but excluded from baseline manifests.
