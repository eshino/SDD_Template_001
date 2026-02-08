# AGENT.md

## Purpose
このプロジェクトは Specification-Driven Development (SDD) で開発する。
実装前に仕様を更新し、仕様と実装の乖離を防ぐ。

## Source Of Truth
- 永続ドキュメント: `docs/sdd/templates/`
- ステアリング: `docs/sdd/steering/`
- API契約: `contracts/openapi.yaml`

## Required Flow
1. `docs/sdd/steering/product.md` を確認
2. `docs/sdd/steering/tech.md` と `docs/sdd/steering/structure.md` を確認
3. `docs/sdd/templates/00_definition_of_done.md` の DoD を確認
4. 変更タイプを分類（要件/API/DB/認証/運用/ステアリング）
5. `docs/sdd/templates/` の該当文書を先に更新
6. 実装
7. テスト
8. PR Gate を満たす

## Document Update Matrix (Required)
- 要件変更: `04_requirements.md` + `05_spec_sources.md` + `08_adr.md`
- API契約変更: `05_spec_sources.md` + `08_adr.md` + `11_test_strategy.md`
- DBスキーマ変更: `07_data_model.md` + `12_operations.md` + `13_release_change_management.md`
- 認証/認可変更: `10_security_design.md` + `05_spec_sources.md` + `08_adr.md`
- 障害再発防止: `12_operations.md` + `18_risk_debt_register.md`
- ステアリング変更: `docs/sdd/steering/changelog.md` 必須

## Engineering Policies
- DB運用は Alembic を唯一のスキーマ適用手段とする（`create_all` と混在しない）
- 例外はError Modelに正規化する（DB一意制約は409等へ変換）
- 認証は Bearer JWT を標準とし、暫定互換は期限付きで管理する
- テストデータIDは衝突しない命名規約を採用する（timestamp/uuid）
- 参照モックと実装UIの責務を分離する（`docs/mockups` と `app/ui`）

## ADR Lifecycle
- ADR status: `Proposed` / `Accepted` / `Superseded` / `Deprecated`
- 既存判断を変更する場合は旧ADRを `Superseded` に変更し、新ADRを追加する
- `changelog.md` に日付と関連ADRを追記する

## PR Gate (Required)
- 変更タイプ
- 更新した文書一覧
- 未更新文書の理由
- 互換性影響（あり/なし）
- ロールバック手順（破壊的変更時）
- Definition of Done 達成チェック

## CI Gate (Recommended)
- `scripts/check_sdd_matrix.py` を実行し、更新マトリクス違反を検出する
