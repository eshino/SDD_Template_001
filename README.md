# SDD_Template_001

このフォルダは、次回プロジェクトをSDDでゼロから開始するための雛形一式です。

## 使い方
1. この `sdd_starter/` 配下を新規リポジトリのルートへコピー
2. `AGENT.md` をプロジェクト固有情報で更新
3. `docs/sdd/steering/templates/` から `docs/sdd/steering/*.md` を作成
4. `docs/sdd/templates/` を順に埋める
5. `scripts/check_sdd_matrix.py` と `.github/workflows/sdd-doc-gate.yml` を有効化

## 収録内容
- 永続ドキュメントテンプレート: `docs/sdd/templates/`
- ステアリングテンプレート: `docs/sdd/steering/templates/`
- 運用ルールファイル: `AGENT.md`
- 推奨フォルダ構成: `STRUCTURE.md`
- 文書更新ゲート雛形: `.github/workflows/sdd-doc-gate.yml`, `scripts/check_sdd_matrix.py`
