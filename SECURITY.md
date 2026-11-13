# Security Policy


Please report security-sensitive issues privately to the maintainer rather than opening a public issue.

### 私密报告与理论／实现边界 / Private reporting and theory-to-implementation boundary

中文：在公开 Issue、PR、研究实例与 CI 输出中避免披露凭据、私人材料或未修复漏洞；文档讨论安全假设不表示已实现安全控制；对确切程序和环境的漏洞应走私密渠道，检查结果只适用实际测试范围

English: Do not disclose secrets, private materials or unpatched exploit details in public issues, PRs, research examples or CI output. Discussion of security assumptions does not implement controls. Report concrete vulnerabilities privately; test results apply only to their executed scope

## Scope

Security reports should concern repository-owned code, automation, validation logic, workflows, or documentation that could materially mislead users about a security boundary. Research claims, external systems, and third-party services remain governed by their own evidence and security boundaries.

Do not include credentials, private data, or exploit details in public issues or pull requests.

The repository does not claim to provide a deployed security, authorization, sandboxing, or autonomous-agent control system unless a current executable artifact and repository evidence explicitly establish that capability.
