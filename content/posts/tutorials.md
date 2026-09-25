---
title: "客户端教程 - Clash、Sing-box、Shadowrocket 全平台指南"
summary: "系统梳理 Clash、Sing-box、Shadowrocket 三大主流代理客户端的核心特性、选型矩阵、全平台配置步骤及常见报错排查技巧。"
date: 2026-09-25
lastmod: 2026-09-25
keywords: ["Clash教程", "Sing-box配置", "Shadowrocket教程", "Clash Verge Rev", "小火箭订阅导入", "TUN模式设置", "节点超时排查", "全平台代理客户端"]
---

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-left: 4px solid #0056b3; border-radius: 8px; padding: 18px 22px; margin: 18px 0 25px 0; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
  <p style="margin: 0 0 12px 0; font-size: 0.95rem; color: #475569; line-height: 1.65; border-bottom: 1px dashed #cbd5e1; padding-bottom: 10px;">
    📌 <strong>架构定位：</strong>本指南专为全平台（Windows / macOS / iOS / Android）代理软件用户设计，围绕 <strong>Clash 生态、Sing-box、Shadowrocket (小火箭)</strong> 三大核心方案构建系统化使用体系。帮助读者完成全平台客户端选型、快速订阅导入、TUN 虚拟网卡配置及网络故障排查。
  </p>
  <p style="margin: 0; font-size: 0.98rem; color: #1e293b; line-height: 1.75; font-weight: 500;">
    📖 <strong>导读与摘要：</strong>在当今多样化的网络环境中，找到一款稳定、高效且适合自身操作系统的网络代理客户端，是提升工作与信息检索效率的关键。目前市面上工具众多，但协议支持、内核更新速度和跨平台表现各有差异。其中，Clash 生态、新一代通用网络核心 Sing-box，以及 iOS 平台的常青树 Shadowrocket（小火箭），构成了目前最主流的三大方案。本指南系统梳理这三款主流工具的核心特性、适用系统，并提供清晰的配置步骤与避坑建议，帮助你快速完成全平台网络环境的搭建。
  </p>
</div>

欢迎来到客户端教程专栏！无论您使用的是 PC 电脑、MacBook，还是 iPhone 或 Android 智能手机，均可在本指南中找到最适合的代理客户端及其优化技巧。

---

## 一、主流客户端横向对比与选型建议

选择客户端前，了解它们各自的底层逻辑与生态定位，有助于避免后续因配置不兼容而反复更换：

- ⚙️ <strong>Clash 系列（开源核心 / GUI 衍生版）</strong>：规则分流系统的集大成者。虽然 Clash 原核心已停止维护，但社区驱动的 <strong>Mihomo (Clash.Meta)</strong> 内核延续了强大的生态生命力。其成熟的分流策略、直观的 Web 界面和面板扩展（如 <strong>Clash Verge Rev</strong>、Clash Nyanpasu）使其依然是 Windows 与 macOS 上的主流首选。
- ⚡ <strong>Sing-box</strong>：下一代全能网络核心平台。由 SagerNet 团队开发，以<strong>轻量、极低内存占用</strong>以及原生支持全协议（如 Shadowsocks、Vmess、Vless、Trojan、Hysteria 2、TUIC 等）著称。配置采用现代化 JSON 架构，适合追求极低延迟与跨平台一致性的极客与重度用户。
- 📱 <strong>Shadowrocket（小火箭）</strong>：iOS / iPadOS 平台的经典标杆。买断制独立应用，对各类订阅协议兼容性极强，支持<strong>一键扫码、节点健康度批量测试</strong>以及强大的本地脚本规则，是苹果移动端综合体验最省心的选择。

### 📊 主流客户端横向选型矩阵表

<div style="overflow-x:auto; margin:20px 0;">
  <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.9rem; background:#fff; border:1px solid #e2e8f0; border-radius:6px;">
    <thead>
      <tr style="background:#f1f5f9; border-bottom:2px solid #cbd5e1; color:#1e293b;">
        <th style="padding:12px; border:1px solid #cbd5e1;">客户端</th>
        <th style="padding:12px; border:1px solid #cbd5e1;">主力支持平台</th>
        <th style="padding:12px; border:1px solid #cbd5e1;">协议支持范围</th>
        <th style="padding:12px; border:1px solid #cbd5e1;">配置门槛</th>
        <th style="padding:12px; border:1px solid #cbd5e1;">核心优势</th>
      </tr>
    </thead>
    <tbody style="color:#334155; line-height:1.6;">
      <tr style="border-bottom:1px solid #e2e8f0;">
        <td style="padding:12px; border:1px solid #e2e8f0; font-weight:bold; color:#0f172a;">Clash (Mihomo 衍生)</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">Windows / macOS / Linux / Android</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">广泛支持（含现代主流协议）</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">中等（UI 直观）</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">规则分流生态成熟，桌面端体验佳</td>
      </tr>
      <tr style="border-bottom:1px solid #e2e8f0; background:#f8fafc;">
        <td style="padding:12px; border:1px solid #e2e8f0; font-weight:bold; color:#0f172a;">Sing-box</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">全平台 (含 iOS / Android / 桌面)</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">全面（首发支持最新协议）</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">偏高（需熟悉 JSON）</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">资源占用极低，核心性能卓越</td>
      </tr>
      <tr>
        <td style="padding:12px; border:1px solid #e2e8f0; font-weight:bold; color:#0f172a;">Shadowrocket</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">iOS / iPadOS / Apple Silicon Mac</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">极广泛</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">极低（开箱即用）</td>
        <td style="padding:12px; border:1px solid #e2e8f0;">手机端操作流畅，扫码一键导入</td>
      </tr>
    </tbody>
  </table>
</div>

---

## 二、平台配置实战与步骤拆解

### 1. Clash 生态（推荐客户端：Clash Verge Rev）
- **适用平台**：Windows / macOS / Linux
- **获取与安装**：下载对应操作系统的最新安装包（如 Windows 的 `.exe` 或 macOS 的 `.dmg`），完成安装并授权网络权限。
- **导入订阅**：
  1. 进入客户端侧边栏的 **“订阅 (Profiles)”** 界面；
  2. 将服务提供商提供的订阅链接粘贴至地址栏，点击 **“导入 (Import)”**；
  3. 右键选中导入的配置并激活（切换为选中高亮状态）。
- **启动与分流**：
  1. 转到 **“代理 (Proxies)”** 界面，在顶部策略组中选择 **“Rule（规则模式）”**；
  2. 展开节点分组，选择合适的可用节点或测速后选中延迟最低的节点；
  3. 在主界面开启 **“系统代理 (System Proxy)”** 开关即可生效。

### 2. Sing-box（图形端：GUI.for.SingBox 或移动端官方 App）
- **适用平台**：Android / iOS / Windows / macOS
- **配置获取与导入**：
  1. 若使用支持 Sing-box 格式的订阅源，复制对应链接；
  2. 打开应用后，选择 **Profiles -> Add Profile**，类型选择 **Remote**，填入订阅 URL 并点击拉取；
  3. 若仅有通用节点链接，建议使用订阅转换工具将其规范化为 Sing-box 的标准 JSON 格式。
- **核心运行设置**：
  1. 在主设置中勾选 **Tun 模式**（虚拟网卡全局拦截），该模式可让所有系统进程无缝走规则分流，无需单独配置系统代理端口；
  2. 点击主界面顶部的 **Start / 连接** 按钮启动内核。

### 3. Shadowrocket（小火箭）
- **适用平台**：iOS / iPadOS
- **账户准备与安装**：Shadowrocket 仅在部分海外地区的 App Store 上架，需准备海外 Apple ID 并完成付费下载。
- **订阅配置导入**：
  - **方式一（扫码）**：点击首页左上角的扫描图标，直接扫描服务商后台提供的二维码。
  - **方式二（链接）**：点击右上角 **“+”**，在 **“类型 (Type)”** 下拉菜单中选择 **“Subscribe”**，将订阅 URL 粘贴至 **“URL”** 栏，点击右上角保存。
- **模式选择与连接**：
  1. 返回首页，底部选择 **“配置 (Config)”** 模式（即规则分流模式，自动避开国内直连网站）；
  2. 在节点列表中点击选中目标节点，打开顶部的连接总开关；
  3. 首次连接会弹出 iOS 的 VPN 配置权限申请，根据系统提示验证指纹或面容即可。

---

## 三、常见网络问题排查与优化技巧

- 🚨 <strong>节点全部超时（Timeout）</strong>：优先排查本机系统时间。若设备时钟与网络标准时间偏差超过 <strong>90 秒</strong>，基于 TLS 证书的安全握手将直接失败。前往系统设置开启“自动同步时间”通常能直接解决。
- 🔒 <strong>网页提示证书风险或无法联网</strong>：检查是否误开了多重客户端，导致本地监听端口冲突（如 <strong>7890 端口被占满</strong>）；若开启了 Tun 虚拟网卡模式，先关闭其他虚拟网卡类软件（如虚拟机网络适配器或杀毒软件防火墙）。
- 🚀 <strong>国内网站访问变慢或打不开</strong>：确认分流模式是否处于 <strong>全局（Global）</strong>。日常使用请务必保持在 <strong>规则（Rule / Config）</strong> 模式，避免将国内直连流量绕道境外节点。

---

> 💡 <strong>总结建议</strong>：选择客户端没有绝对的优劣，关键在于使用习惯与设备生态——移动端图省心首选 <strong>Shadowrocket</strong>，桌面端看重视觉与规则便利可选 <strong>Clash Verge Rev</strong>，而对性能与最新协议有极致追求的则推荐逐步迁移至 <strong>Sing-box</strong>。完成首次配置后，定期更新订阅与规则库，即可长期享受稳定纯净的网络环境。

---

## 热门全平台教程
- [Clash Verge Rev 零基础配置教程：从节点导入到规则分流](/posts/clash-verge-rev-beginner-tutorial/)
- [2026 新手魔法上网入门：梯子与机场如何选择？](/posts/beginner-guide-to-cross-firewall/)
- [节点超时与订阅无法更新？5 大故障排查](/posts/airport-node-timeout-troubleshooting/)

## 推荐搭配机场
搭配高连通率专线节点，才能发挥客户端的最佳性能：
- **灵动云**（全站 TOP 1 首选推荐，专线与 BGP 节点，支持按量与包月切换，[查看测评](/providers/lingdong-cloud/)）
- **暮光网络**（全站 TOP 2 推荐，影音大带宽，4K/8K 无卡顿，专享 8 折优惠码 `mm88`，[查看测评](/providers/twilight/)）
- **飞猫云**（全站 TOP 3 推荐，高性价比年付，折合 7 元/月起，专享 8 折优惠码 `flycat888`，[查看测评](/providers/flycat-cloud/)）
- **微风网络**（全站 TOP 4 推荐，日常轻量稳定备用方案，支持常规协议导入，[查看测评](/providers/breezenet/)）
