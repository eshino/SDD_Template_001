# 07 Data Model

## テーブル一覧
- applications
- policies
- endorsements
- audit_logs

## 制約
- policies.policy_id UNIQUE
- policies.policy_number UNIQUE

## マイグレーション
- Alembicのみで実施
