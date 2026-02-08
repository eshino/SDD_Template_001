# Recommended Structure

```text
.
├─ AGENT.md
├─ README.md
├─ app/
├─ tests/
├─ contracts/
│  └─ openapi.yaml
├─ docs/
│  └─ sdd/
│     ├─ README.md
│     ├─ templates/
│     │  ├─ 00_definition_of_done.md
│     │  ├─ 01_product_vision.md
│     │  ├─ ...
│     │  └─ 18_risk_debt_register.md
│     └─ steering/
│        ├─ README.md
│        ├─ product.md
│        ├─ tech.md
│        ├─ structure.md
│        ├─ changelog.md
│        └─ templates/
│           ├─ steering_product_template.md
│           ├─ steering_tech_template.md
│           ├─ steering_structure_template.md
│           └─ steering_changelog_template.md
├─ scripts/
│  └─ check_sdd_matrix.py
└─ .github/
   └─ workflows/
      └─ sdd-doc-gate.yml
```

## Notes
- `docs/sdd/templates/` は永続情報（仕様の正本）
- `docs/sdd/steering/` は判断基準の正本
- 画面モックは `docs/mockups/`、実装UIは `app/ui/` に分離する
