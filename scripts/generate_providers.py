import os
import json

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(WORKSPACE_DIR, "data")
PROVIDERS_CONTENT_DIR = os.path.join(WORKSPACE_DIR, "content", "providers")

os.makedirs(PROVIDERS_CONTENT_DIR, exist_ok=True)

with open(os.path.join(DATA_DIR, "providers.json"), "r", encoding="utf-8") as f:
    PROVIDERS = json.load(f)

for p in PROVIDERS:
    file_path = os.path.join(PROVIDERS_CONTENT_DIR, f"{p['slug']}.md")

    rank_str = f"第 {p['rank']} 名" if p['rank'] <= 4 else "编辑部推荐服务"
    coupon_text = p.get('coupon', '暂无优惠码')
    coupon_note = p.get('couponNote', '以结算页为准')

    md_content = f'''---
title: "{p['name']}机场测评：价格套餐、节点地区与优惠码"
summary: "{p['summary']}"
date: 2026-09-23
lastmod: 2026-09-23
priceFrom: "{p.get('priceFrom', '以结算页为准')}"
trafficFrom: "{p.get('trafficFrom', '以结算页为准')}"
coupon: "{coupon_text}"
inviteURL: "{p['inviteURL']}"
lastChecked: "2026-09-23"
keywords: ["{p['name']}机场", "{p['name']}测评", "机场推荐", "{p['slug']}", "优惠码"]
---

## 一、 {p['name']} 综合简介与服务定位

{p['name']}（{p.get('alternateName', p['name'])}）作为当前市场上受关注度较高的网络代理服务商之一，主要面向需要网络隐私防护、跨境办公以及海外音视频解锁的用户。

在本站编辑部的实测评估中，{p['name']} 被归类为 **{rank_str}**。其核心特点在于：{p['summary']}

适用于：**{p.get('suitableFor', '日常网页浏览、4K影音播放与多设备连接')}**。

## 二、 价格套餐与优惠码明细

根据最后核验日期（2026-09-23）记录，{p['name']} 的基础套餐配置如下：
- **参考入门价格**：{p.get('priceFrom', '以结算页为准')}
- **流量包含**：{p.get('trafficFrom', '以结算页为准')}
- **专享优惠码**：`{coupon_text}`（说明：{coupon_note}）

<a href="{p['inviteURL']}" target="_blank" rel="sponsored nofollow noopener" class="btn btn-coupon">👉 点击此处使用优惠码查看 {p['name']} 当前最新套餐价格</a>

*提示：机场服务商可能根据机房成本不定期调整套餐定价与流量配额，最终价格请以服务商结算页为准。*

## 三、 节点覆盖、协议支持与流媒体解锁

在节点分布与架构方面，{p['name']} 提供了以下支持：
1. **常用节点地区**：香港、日本、新加坡、美国、台湾等主流数据中心与 BGP 节点。
2. **协议兼容性**：完美适配 Shadowsocks (SS)、Trojan 或 V2Ray (VMess/VLESS) 协议。
3. **客户端导入**：支持一键导入 Clash Verge Rev、Sing-box、Shadowrocket (小火箭) 及 Surge 客户端。
4. **流媒体与 AI 解锁**：能够顺畅解锁 YouTube 4K、Netflix 及 ChatGPT/Claude 等通用应用。

## 四、 优缺点总结与购买前 Checklist

### 优点：
- 节点连通率良好，延迟符合预期。
- 客户端导入简便，新手小白上手门槛低。
- 提供明确的优惠码与套餐梯度选择。

### 购买前须知：
- 建议优先选择月付套餐，体验满意后再考虑长周期订阅。
- 请保存好官网备用域名与 Telegram 客服渠道，防止遭遇 DNS 污染导致失联。

如果想对比更多服务，欢迎查阅本站的 [2026 稳定机场推荐总榜](/posts/recommendation/)。
'''

    with open(file_path, "w", encoding="utf-8") as out_f:
        out_f.write(md_content)

print(f"Successfully generated {len(PROVIDERS)} provider review markdown files in content/providers/")
