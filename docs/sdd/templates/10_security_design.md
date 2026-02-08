# 10 Security Design

## 認証
- Bearer JWT専用

## 認可
- ロール: AGENT, UNDERWRITER, POLICY_ADMIN, AUDITOR

## 監査
- 重要操作はaudit_logsへ記録
