# SEO 替换契约与多站防同质化规范 (docs/seo-profile-replacement-contract.md)

本文件规定当使用新的 SEO 提示词替换 `site-seo-profile.json` 时的自动化替换契约。

## 替换接口协议
当另一条万能替换提示词生效时，仅需更新 `docs/site-seo-profile.json` 字段：
- `primaryKeywords`
- `secondaryKeywords`
- `longTailKeywords`
- `heroKeywords`
- `footerKeywords`
- `navigationItems`

## 替换执行流程
1. 读取旧 `site-seo-profile.json` 与活动 URL 清单。
2. 规范化新关键词并更新组件引用。
3. 旧导航 URL 如果已有收录，创建 301 重定向映射。
4. 重新运行 `python scripts/verify_seo.py` 自动化检测脚本。
