# Contributing

Thank you for considering a contribution.

## Before opening an issue

- Search existing issues.
- Do not upload confidential operational data, personal data or credentials.
- For bugs, provide the Python version, dependency versions, steps to reproduce, expected behaviour and observed behaviour.
- For model changes, explain the evaluation design and include results for minority-class recall as well as overall metrics.

## Pull requests

1. Create a focused branch.
2. Make one coherent change.
3. Add or update tests where practical.
4. Update documentation if behaviour changes.
5. Confirm that no restricted dataset or secret is included.
6. Describe limitations and trade-offs honestly.

Suggested commit style:

```text
docs: document dataset provenance and licence
fix: prevent leakage during resampling
feat: add reproducible model-evaluation command
test: validate prediction input schema
```

By contributing original code or documentation, you agree that your contribution may be distributed under the repository's MIT License. Do not submit the XAI Drilling Dataset or other third-party material unless redistribution is expressly permitted. Dataset-derived material must comply with the original CC BY-NC-SA 4.0 terms, including attribution, non-commercial use and ShareAlike requirements.
