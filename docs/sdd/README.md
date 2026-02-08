# docs/sdd README

## Goal
仕様を先に固め、実装・テスト・運用が同じ基準で進む状態を維持する。

## Rules
- `templates/` は永続情報。実装完了後も参照され続ける。
- `steering/` は意思決定の基準。基準変更は `steering/changelog.md` 必須。
- 変更タイプに応じた文書同時更新を厳守する（`AGENT.md` の matrix）。

## Recommended Order
1. steering確認
2. DoD確認
3. templates更新
4. 実装
5. テスト
6. PR Gate確認
