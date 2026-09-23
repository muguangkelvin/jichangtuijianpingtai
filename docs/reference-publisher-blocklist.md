# 内部第三方参考发布者黑名单隔离 (docs/reference-publisher-blocklist.md)

本文件包含仅限内部审计的屏蔽词汇，公开页面与生成的 HTML/RSS/Sitemap 中**严禁**出现以下名称、品牌或域名句式：

- 三毛机场
- 猫梦博客
- Gaterank
- 星维机场
- 一毛机场
- 一份机场
- 二毛博客
- "根据某某博客"
- "某评测站称"
- "资料来自某博客"

审计机制：`python scripts/verify_seo.py` 脚本将在生产构建后扫描全部 `public/` 产物，确保上述字符串全零出现。
