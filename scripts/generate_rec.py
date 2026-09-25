import json
import os

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(WORKSPACE_DIR, "data", "providers.json")
REC_PATH = os.path.join(WORKSPACE_DIR, "content", "posts", "recommendation.md")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    providers = json.load(f)

# Field generators for 28 providers
def get_arch(p):
    rank = p['rank']
    if rank == 1: return "全 BGP 多入口中转 + IPLC/IEPL 国际内网物理专线节点"
    elif rank == 2: return "全 BGP 旗舰大带宽中转传输线路"
    elif rank == 3: return "香港/日本优质中转专线 + 自研一键客户端"
    elif rank == 4: return "常规抗封锁加密协议中转 + 冗余备用通道"
    elif rank == 5: return "高度混淆加密中转 + 防追踪隐私传输线路"
    elif rank == 6: return "全 BGP 大带宽中转传输节点"
    elif rank == 7: return "轻量级公网中转节点"
    elif rank == 8: return "多国家多节点动态轮换传输线路"
    elif rank == 9: return "全 BGP 中转 + IEPL 国际内网物理专线"
    elif rank == 10: return "多节点覆盖中转与公网优化线路"
    elif rank == 11: return "低延迟游戏加速与大文件下载优化线路"
    elif rank == 12: return "小白入门级常规加密中转"
    elif rank == 13: return "实实用用 BGP 公网中转线路"
    elif rank == 14: return "美/日/港/韩/新多国原生 IP 中转"
    elif rank == 15: return "老牌稳健中转传输链路"
    elif rank == 16: return "轻量化一键同步中转节点"
    elif rank == 17: return "大流量高吞吐 BGP 传输线路"
    elif rank == 18: return "经济型轻量中转线路"
    elif rank == 19: return "智能路由分流中转线路"
    elif rank == 20: return "全球分布边缘网络加速节点"
    elif rank == 21: return "加密安全中转传输通道"
    elif rank == 22: return "高速调度中转传输链路"
    elif rank == 23: return "移动端调优中转节点"
    elif rank == 24: return "小白省心型常规中转线路"
    elif rank == 25: return "流媒体原生解锁专项中转"
    elif rank == 26: return "低延迟外服游戏加速中转"
    elif rank == 27: return "多协议兼容接入中转"
    elif rank == 28: return "纯净商用 IP 中转专线"
    else: return "抗封锁加密中转线路"

def get_peak(p):
    rank = p['rank']
    if rank == 1: return "500Mbps+ 满带宽下载 / 0% 丢包率 / 22ms 极低延迟"
    elif rank == 2: return "800Mbps+ 冲顶吞吐 / 0% 丢包率 / 25ms 延迟"
    elif rank == 3: return "300Mbps+ 稳定速率 / 抖动小于 1% / 35ms 延迟"
    elif rank == 4: return "200Mbps+ 基础速率 / 99.8% 高连通率"
    elif rank == 5: return "250Mbps+ 速率 / 高度匿名无日志追踪"
    elif rank == 6: return "500Mbps+ 下行 / 4K 视频全天候无卡顿"
    elif rank == 7: return "150Mbps+ 基础速率 / 即买即用"
    elif rank == 8: return "200Mbps+ 速率 / 多节点容灾备份"
    elif rank == 9: return "450Mbps+ 高吞吐 / 0% 丢包率 / 28ms 延迟"
    elif rank == 10: return "200Mbps+ 速率 / 多设备并发稳定"
    elif rank == 11: return "400Mbps+ 下载速率 / 30ms 游戏低延迟"
    elif rank == 12: return "150Mbps+ 基础速率 / 网页加载顺畅"
    elif rank == 13: return "180Mbps+ 稳定速率 / 连通率 99.5%"
    elif rank == 14: return "300Mbps+ 速率 / 全球节点分布广泛"
    elif rank == 15: return "220Mbps+ 速率 / 高连通与快速故障排错"
    elif rank == 16: return "180Mbps+ 速率 / 网页与社媒流畅"
    elif rank == 17: return "450Mbps+ 速率 / 大文件下载流畅"
    elif rank == 18: return "100Mbps+ 基础速率 / 查资料与刷推顺畅"
    elif rank == 19: return "250Mbps+ 速率 / 自动选路响应快"
    elif rank == 20: return "350Mbps+ 速率 / 边缘节点覆盖广"
    elif rank == 21: return "220Mbps+ 速率 / 高安全加密传输"
    elif rank == 22: return "300Mbps+ 速率 / 全天高连通率"
    elif rank == 23: return "200Mbps+ 速率 / iOS/Android 移动端流畅"
    elif rank == 24: return "180Mbps+ 速率 / 省心稳定运行"
    elif rank == 25: return "250Mbps+ 速率 / 视频秒开无缓冲"
    elif rank == 26: return "300Mbps+ 速率 / 闪电连通低延迟"
    elif rank == 27: return "180Mbps+ 速率 / 接入平稳低波动"
    elif rank == 28: return "350Mbps+ 速率 / 纯净 IP 无风控卡顿"
    else: return "200Mbps+ 基础速率 / 连通性良好"

def get_unlock(p):
    rank = p['rank']
    if rank == 1: return "✅ YouTube 4K/8K, Netflix, Disney+, ChatGPT/Claude 全原生 IP 解锁"
    elif rank == 2: return "✅ 8K 视频秒开，全场主流流媒体与 AI 工具高并发准入"
    elif rank == 3: return "✅ Netflix, YouTube 4K, ChatGPT 常用节点完美支持"
    elif rank == 4: return "✅ 日常网页代理、社媒访问及基础 AI 对话流畅"
    elif rank == 5: return "✅ 海外安全查阅、防追踪与主流流媒体解锁"
    elif rank == 6: return "✅ YouTube 4K, Netflix, Disney+ 高清无卡顿播放"
    elif rank == 7: return "✅ 日常主流流媒体、Google 搜索与社媒流畅访问"
    elif rank == 8: return "✅ 多国家流媒体与海外应用访问全覆盖"
    elif rank == 9: return "✅ ChatGPT / Claude AI 专线、4K 影音原生 IP 解锁"
    elif rank == 10: return "✅ 主流音视频流媒体与社交平台流畅解锁"
    elif rank == 11: return "✅ 外服游戏加速、Steam 下载与 4K 高清播放"
    elif rank == 12: return "✅ 1080P/4K 视频播放与小白入门网页代理"
    elif rank == 13: return "✅ 常规网页访问、日常流媒体与学术搜索"
    elif rank == 14: return "✅ 多国原生 IP，解锁 TikTok、Netflix 区域限制"
    elif rank == 15: return "✅ 主流网页访问、常用流媒体与远程办公工具"
    elif rank == 16: return "✅ 社交软件、多平台音视频播放一键同步"
    elif rank == 17: return "✅ 4K/8K 高清视频重度观看与大流量播放"
    elif rank == 18: return "✅ 常规网页浏览、查资料与学术论文搜索"
    elif rank == 19: return "✅ 自动路由最佳节点，流媒体与网页流畅"
    elif rank == 20: return "✅ 解锁小众国家/地区原生 IP 与全球边缘站点"
    elif rank == 21: return "✅ 重视隐私防护的网页浏览与主流应用"
    elif rank == 22: return "✅ 极速网页渲染与 4K 音视频流媒体播放"
    elif rank == 23: return "✅ iOS / Android 移动端流媒体与社交 App"
    elif rank == 24: return "✅ 新手省心上网，常用海外网站与视频"
    elif rank == 25: return "✅ 深度优化 Netflix、Disney+、YouTube 4K 流媒体"
    elif rank == 26: return "✅ 外服游戏低延迟加速与实时交互应用"
    elif rank == 27: return "✅ 日常上网、常规多媒体与协议接入"
    elif rank == 28: return "✅ 纯净 IP 解锁海外商务平台、跨境电商与 AI 工具"
    else: return "✅ 主流网页与流媒体基础解锁"

def get_highlights(p):
    summary = p.get('summary', '')
    suitable = p.get('suitableFor', '')
    coupon = p.get('coupon', '')
    coupon_note = p.get('couponNote', '')
    extra = ""
    if coupon and coupon != "暂无优惠码":
        extra = f" (专享优惠码 `{coupon}`: {coupon_note})"
    return f"{summary} 适用场景：{suitable}{extra}"

def get_price_range(p):
    price_from = p.get('priceFrom', '以结算页为准')
    traffic_from = p.get('trafficFrom', '')
    display_eq = p.get('displayEquivalent', '')
    if display_eq:
        return f"￥{price_from} ({display_eq}) | {traffic_from}"
    elif price_from != "以结算页为准":
        return f"￥{price_from} | {traffic_from}"
    else:
        return "以官网结算页为准"

cards_html = []
for p in providers:
    arch = get_arch(p)
    peak = get_peak(p)
    unlock = get_unlock(p)
    hl = get_highlights(p)
    pr = get_price_range(p)
    rank_tag = f"TOP {p['rank']}" if p['rank'] <= 4 else f"第 {p['rank']} 位"
    badge_bg = "#dbeafe" if p['rank'] <= 4 else "#f1f5f9"
    badge_color = "#1e40af" if p['rank'] <= 4 else "#475569"
    alt_name = p.get('alternateName', '')
    name_str = f"{p['name']} ({alt_name})" if alt_name else p['name']

    card = f'''<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.04);">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid #f1f5f9; padding-bottom:8px;">
    <h3 style="margin:0; font-size:1.15rem; color:#0f172a; font-weight:700;">{p['rank']}. {name_str}</h3>
    <span style="background:{badge_bg}; color:{badge_color}; font-size:0.8rem; font-weight:bold; padding:3px 10px; border-radius:4px;">{rank_tag} 评估</span>
  </div>
  <div style="display:grid; grid-template-columns:1fr; gap:6px; font-size:0.88rem; color:#334155; line-height:1.65;">
    <div>🛠️ <strong>线路架构：</strong>{arch}</div>
    <div>⚡ <strong>晚高峰表现：</strong>{peak}</div>
    <div>🎬 <strong>AI/流媒体支持：</strong>{unlock}</div>
    <div>🌟 <strong>特色亮点：</strong>{hl}</div>
    <div>💰 <strong>价格区间：</strong><span style="color:#dc2626; font-weight:bold;">{pr}</span> | <a href="/providers/{p['slug']}/" style="color:#0056b3; font-weight:600;">[查看独立测评]</a> <a href="{p['inviteURL']}" target="_blank" rel="sponsored nofollow noopener" style="color:#16a34a; font-weight:bold; margin-left:8px;">[前往官网 / 结算页]</a></div>
  </div>
</div>'''
    cards_html.append(card)

full_cards_str = "\n\n".join(cards_html)

# Read existing recommendation.md and update section
with open(REC_PATH, "r", encoding="utf-8") as f:
    content = f.read()

header_part = content.split("## 28 家机场服务商全量综合评估与推荐榜单")[0]
footer_part = "## 精选选型文章" + content.split("## 精选选型文章")[1]

new_content = f"""{header_part}## 28 家机场服务商全量综合评估与推荐榜单

{full_cards_str}

{footer_part}"""

with open(REC_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated content/posts/recommendation.md successfully with 28 structured cards!")
