import os
import json
import re
import shutil
import csv
import xml.etree.ElementTree as ET

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT_DIR = os.path.join(WORKSPACE_DIR, "content")
DATA_DIR = os.path.join(WORKSPACE_DIR, "data")
PUBLIC_DIR = os.path.join(WORKSPACE_DIR, "public")
STATIC_DIR = os.path.join(WORKSPACE_DIR, "static")
DOCS_DIR = os.path.join(WORKSPACE_DIR, "docs")

# Load data
with open(os.path.join(DATA_DIR, "providers.json"), "r", encoding="utf-8") as f:
    PROVIDERS = json.load(f)

with open(os.path.join(WORKSPACE_DIR, "docs", "site-seo-profile.json"), "r", encoding="utf-8") as f:
    SEO_PROFILE = json.load(f)

BASE_URL = "https://jichangtuijianpingtai.xyz/"

def render_html_page(title, description, canonical_url, body_content, is_home=False):
    header_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="机场推荐, 梯子推荐, 魔法上网, 魔法机场, Clash教程, Shadowrocket配置, 稳定翻墙">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <style>
    :root {{
      --bg-color: #fcfcfc;
      --text-color: #222;
      --link-color: #0056b3;
      --border-color: #e5e5e5;
      --card-bg: #ffffff;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.6;
      color: var(--text-color);
      background-color: var(--bg-color);
      margin: 0;
      padding: 0 20px;
      max-width: 1240px;
      margin-left: auto;
      margin-right: auto;
    }}
    header {{
      border-bottom: 2px solid var(--border-color);
      padding: 18px 0;
      margin-bottom: 20px;
    }}
    .header-brand {{
      font-size: 1.5rem;
      font-weight: bold;
      text-decoration: none;
      color: var(--text-color);
    }}
    .header-slogan {{
      font-size: 0.9rem;
      color: #666;
      margin-top: 4px;
    }}
    nav {{
      margin-top: 12px;
    }}
    nav a {{
      margin-right: 20px;
      color: var(--link-color);
      text-decoration: none;
      font-weight: 500;
      font-size: 1rem;
    }}
    nav a:hover {{ text-decoration: underline; font-weight: bold; }}
    .hero-box {{
      background: #f0f4f8;
      border-left: 5px solid var(--link-color);
      padding: 20px;
      margin: 15px 0 25px 0;
      border-radius: 6px;
    }}
    .hero-box h1 {{ margin: 0 0 12px 0; font-size: 1.65rem; }}
    .hero-keywords-text {{ font-size: 1rem; color: #333; line-height: 1.65; }}
    .provider-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      margin: 20px 0;
    }}
    @media (min-width: 768px) {{ .provider-grid {{ grid-template-columns: 1fr 1fr; }} }}
    .provider-card {{
      border: 1px solid var(--border-color);
      background: var(--card-bg);
      padding: 18px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.04);
    }}
    .provider-card.top-rank {{
      border: 2px solid var(--link-color);
      background: #fafcfe;
    }}
    .provider-title {{ font-size: 1.25rem; margin: 0 0 8px 0; }}
    .badge {{
      display: inline-block; padding: 3px 8px; font-size: 0.8rem; border-radius: 4px; background: #e2e8f0; color: #334155;
    }}
    .badge-top {{ background: #dbeafe; color: #1e40af; font-weight: bold; }}
    .btn {{
      display: inline-block; padding: 8px 16px; background: var(--link-color); color: #fff !important; text-decoration: none; border-radius: 5px; font-size: 0.95rem; margin-right: 10px; margin-top: 10px;
    }}
    .btn-secondary {{ background: #6c757d; }}
    .btn-coupon {{ background: #28a745; }}
    footer {{
      border-top: 2px solid var(--border-color);
      padding: 25px 0;
      margin-top: 40px;
      font-size: 0.9rem;
      color: #555;
    }}
    .footer-keywords-text {{ margin-bottom: 15px; line-height: 1.6; }}
    .breadcrumbs {{ font-size: 0.9rem; color: #666; margin-bottom: 15px; }}
    .breadcrumbs a {{ color: var(--link-color); text-decoration: none; }}
    .article-meta {{ font-size: 0.9rem; color: #666; margin-bottom: 20px; }}
    .toc-box {{ background: #f8fafc; border: 1px dashed var(--border-color); padding: 12px 18px; margin: 15px 0; font-size: 0.95rem; }}
    .trust-links-bar {{
      margin-top: 30px;
      padding: 12px 18px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      font-size: 0.95rem;
      color: #555;
    }}
    .trust-links-bar a {{
      color: var(--link-color);
      text-decoration: none;
      font-weight: 500;
      margin: 0 4px;
    }}
    .trust-links-bar a:hover {{ text-decoration: underline; }}
    /* Search Dropdown Overlay */
    .search-box {{ position: relative; }}
    #search-results-overlay {{
      display: none;
      position: absolute;
      top: 100%;
      right: 0;
      width: 320px;
      max-height: 350px;
      overflow-y: auto;
      background: #fff;
      border: 1px solid #ccc;
      border-radius: 6px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      z-index: 1000;
      margin-top: 5px;
    }}
    .search-result-item {{
      padding: 10px 12px;
      border-bottom: 1px solid #eee;
      display: block;
      color: #333;
      text-decoration: none;
    }}
    .search-result-item:hover {{ background: #f0f4f8; }}
    .search-result-title {{ font-size: 0.9rem; font-weight: bold; color: #0056b3; }}
    .search-result-snippet {{ font-size: 0.8rem; color: #666; margin-top: 2px; }}
  </style>
</head>
<body>
  <header>
    <div class="header-brand-wrap" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:15px;">
      <div>
        <a href="/" class="header-brand">机场推荐平台</a>
        <div class="header-slogan">客观评测、小白友好、告别繁琐设置的节点与工具选择指南</div>
      </div>
      <div class="header-right-tools" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
        <!-- 实时交互搜索框 -->
        <div class="search-box" style="display:flex; align-items:center; border:1px solid var(--border-color); border-radius:6px; padding:5px 10px; background:#fff;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:6px;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="site-search-input" placeholder="搜索机场、评测或教程..." style="border:none; outline:none; font-size:0.85rem; width:150px; background:transparent;">
          <div id="search-results-overlay"></div>
        </div>

        <!-- TG 频道 Icon 按钮 -->
        <a href="https://t.me/+mhFkczMyua0yM2Rl" target="_blank" rel="noopener" class="header-icon-btn" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; background:#0088cc; color:#fff; text-decoration:none; border-radius:6px; font-size:0.85rem; font-weight:500;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69.01-.03.01-.14-.07-.2-.08-.06-.19-.04-.27-.02-.12.02-1.96 1.25-5.54 3.69-.52.36-1 .54-1.43.53-.47-.01-1.37-.26-2.04-.48-.82-.27-1.47-.42-1.42-.88.03-.24.37-.49 1.02-.75 3.99-1.74 6.66-2.89 8.01-3.45 3.81-1.59 4.6-1.87 5.12-1.88.11 0 .37.03.54.18.14.12.18.28.2.45-.02.07-.02.13-.03.22z"/></svg>
          <span>TG 频道</span>
        </a>

        <!-- GitHub Icon 按钮 -->
        <a href="https://github.com" target="_blank" rel="noopener" class="header-icon-btn" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; background:#24292e; color:#fff; text-decoration:none; border-radius:6px; font-size:0.85rem; font-weight:500;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
          <span>GitHub</span>
        </a>
      </div>
    </div>
    <nav aria-label="主导航">
      <a href="/">首页</a>
      <a href="/posts/recommendation/">推荐指南</a>
      <a href="/posts/tutorials/">客户端教程</a>
      <a href="/posts/faq/">常见排错</a>
      <a href="/providers/">机场评测库</a>
      <a href="/service/">自营服务</a>
    </nav>
  </header>
  <main>
    {body_content}
  </main>
  <footer>
    <div class="footer-keywords-text">
      <p>本站专注当前年份机场推荐、性价比机场推荐、Clash 机场测评与机场节点推荐，持续整理便宜机场、稳定机场、AI 机场推荐、机场订阅、价格套餐、优惠码及购买前须知，为用户提供带核验日期的选择参考。</p>
      <p>声明：本站包含合作推广与邀请链接，排序依据编辑综合评估与商业合规策略。套餐价格、流量与节点地区均以服务商最新结算页面为准。</p>
    </div>
    <div class="footer-links">
      <a href="/about/">关于我们</a> |
      <a href="/editorial-policy/">编辑原则</a> |
      <a href="/methodology/">评测方法</a> |
      <a href="/corrections/">纠错与更新</a> |
      <a href="/affiliate-disclosure/">联盟披露</a> |
      <a href="/privacy/">隐私政策</a> |
      <a href="/terms/">服务条款</a> |
      <a href="/disclaimer/">免责声明</a> |
      <a href="/contact/">联系我们</a> |
      <a href="/sitemap.xml">Sitemap</a> |
      <a href="/index.xml">RSS</a>
    </div>
    <div style="margin-top:10px;">
      © 2026 机场推荐平台 · 纯静态加速与独立评测
    </div>
  </footer>

  <script>
    (function() {{
      var searchInput = document.getElementById('site-search-input');
      var overlay = document.getElementById('search-results-overlay');
      var searchData = null;

      if (!searchInput || !overlay) return;

      function loadSearchData(cb) {{
        if (searchData) return cb(searchData);
        fetch('/search-index.json')
          .then(function(res) {{ return res.json(); }})
          .then(function(data) {{
            searchData = data;
            cb(data);
          }})
          .catch(function(err) {{ console.error('Search data load failed:', err); }});
      }}

      searchInput.addEventListener('input', function() {{
        var q = this.value.trim().toLowerCase();
        if (!q) {{
          overlay.style.display = 'none';
          overlay.innerHTML = '';
          return;
        }}
        loadSearchData(function(data) {{
          var matches = data.filter(function(item) {{
            return (item.title && item.title.toLowerCase().indexOf(q) !== -1) ||
                   (item.summary && item.summary.toLowerCase().indexOf(q) !== -1);
          }}).slice(0, 8);

          if (matches.length === 0) {{
            overlay.innerHTML = '<div style="padding:10px; font-size:0.85rem; color:#888;">未找到匹配结果</div>';
          }} else {{
            var html = '';
            matches.forEach(function(m) {{
              html += '<a href="' + m.url + '" class="search-result-item">' +
                      '<div class="search-result-title">' + m.title + '</div>' +
                      '<div class="search-result-snippet">' + (m.summary || '').substring(0, 50) + '...</div>' +
                      '</a>';
            }});
            overlay.innerHTML = html;
          }}
          overlay.style.display = 'block';
        }});
      }});

      document.addEventListener('click', function(e) {{
        if (!searchInput.contains(e.target) && !overlay.contains(e.target)) {{
          overlay.style.display = 'none';
        }}
      }});
    }})();
  </script>
</body>
</html>'''
    return header_html

def render_table(lines, format_inline_fn):
    if not lines:
        return ""
    
    rows = []
    for l in lines:
        cells = [c.strip() for c in l.strip("|").split("|")]
        rows.append(cells)

    if len(rows) < 1:
        return ""

    table_html = '<div style="overflow-x:auto; margin:15px 0;"><table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.9rem; border:1px solid #e2e8f0;">'
    
    # Header row
    table_html += '<thead><tr style="background:#edf2f7; border-bottom:2px solid #cbd5e0;">'
    for c in rows[0]:
        table_html += f'<th style="padding:10px; border:1px solid #e2e8f0;">{format_inline_fn(c)}</th>'
    table_html += '</tr></thead><tbody>'

    # Data rows (skipping divider line if present)
    for idx, r in enumerate(rows[1:]):
        if all(set(cell.replace(":", "").replace("-", "").strip()) == set() for cell in r if cell):
            continue
        bg_style = ' style="background:#f7fafc;"' if idx % 2 == 1 else ''
        table_html += f'<tr{bg_style}>'
        for c in r:
            table_html += f'<td style="padding:10px; border:1px solid #e2e8f0;">{format_inline_fn(c)}</td>'
        table_html += '</tr>'

    table_html += '</tbody></table></div>'
    return table_html

def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    front_matter = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2]
            for line in fm_text.strip().split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    front_matter[k] = v

    html_lines = []
    in_list = False
    in_code_block = False
    code_block_lines = []
    in_table = False
    table_lines = []

    def format_inline(text):
        text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        def replace_link(m):
            label, url = m.group(1), m.group(2)
            if url.startswith("http://") or url.startswith("https://"):
                return f'<a href="{url}" target="_blank" rel="sponsored nofollow noopener">{label}</a>'
            return f'<a href="{url}">{label}</a>'
        text = re.sub(r'\[(.*?)\]\((.*?)\)', replace_link, text)
        return text

    for line in body.split("\n"):
        raw_line = line
        line_str = line.strip()

        if line_str.startswith("```"):
            if in_code_block:
                code_content = "\n".join(code_block_lines)
                html_lines.append(f'<pre style="background:#1e293b; color:#f8fafc; padding:15px; border-radius:6px; overflow-x:auto; font-family:monospace; font-size:0.85rem; line-height:1.45; margin:15px 0;"><code>{code_content}</code></pre>')
                code_block_lines = []
                in_code_block = False
            else:
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                in_code_block = True
            continue

        if in_code_block:
            code_block_lines.append(raw_line)
            continue

        if not line_str:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if in_table:
                html_lines.append(render_table(table_lines, format_inline))
                table_lines = []
                in_table = False
            continue

        if line_str.startswith("|") and line_str.endswith("|"):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            in_table = True
            table_lines.append(line_str)
            continue

        if in_table:
            html_lines.append(render_table(table_lines, format_inline))
            table_lines = []
            in_table = False

        if line_str.startswith("<"):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(format_inline(line_str))
            continue

        if line_str.startswith("# "):
            html_lines.append(f"<h1>{format_inline(line_str[2:])}</h1>")
        elif line_str.startswith("## "):
            html_lines.append(f"<h2>{format_inline(line_str[3:])}</h2>")
        elif line_str.startswith("### "):
            html_lines.append(f"<h3>{format_inline(line_str[4:])}</h3>")
        elif line_str.startswith("#### "):
            html_lines.append(f"<h4>{format_inline(line_str[5:])}</h4>")
        elif line_str.startswith("> "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f'<blockquote style="border-left:4px solid #0056b3; background:#f8fafc; padding:10px 15px; margin:15px 0; color:#334155;">{format_inline(line_str[2:])}</blockquote>')
        elif line_str.startswith("- ") or line_str.startswith("* "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{format_inline(line_str[2:])}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{format_inline(line_str)}</p>")

    if in_list:
        html_lines.append("</ul>")
    if in_table:
        html_lines.append(render_table(table_lines, format_inline))

    return front_matter, "\n".join(html_lines)

def build():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    urls = []
    search_index_items = []

    # Copy static files
    if os.path.exists(STATIC_DIR):
        for item in os.listdir(STATIC_DIR):
            s = os.path.join(STATIC_DIR, item)
            d = os.path.join(PUBLIC_DIR, item)
            if os.path.isfile(s):
                shutil.copy2(s, d)

    # Make robots.txt if not existing
    robots_path = os.path.join(PUBLIC_DIR, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://jichangtuijianpingtai.xyz/sitemap.xml\n")

    # Walk content directory
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, CONTENT_DIR)

                fm, body_html = parse_markdown(full_path)

                if rel_path == "_index.md":
                    # Homepage
                    out_dir = PUBLIC_DIR
                    canonical = BASE_URL
                    title = SEO_PROFILE["siteTitle"]
                    desc = SEO_PROFILE["siteDescription"]

                    # Inject Homepage Top 4 Provider Cards
                    top4_html = '<div class="provider-grid">'
                    for p in PROVIDERS[:4]:
                        top4_html += f'''
                        <div class="provider-card top-rank">
                          <span class="badge badge-top">TOP {p['rank']} 推荐</span>
                          <h3 class="provider-title">{p['name']}</h3>
                          <p style="font-size:0.85rem; color:#555;"><strong>适用：</strong>{p['suitableFor']}</p>
                          <p style="font-size:0.85rem; color:#555;"><strong>套餐：</strong>{p['priceFrom']} ({p['trafficFrom']}) | 优惠码：<code style="color:#d9534f;">{p['coupon']}</code></p>
                          <p style="font-size:0.9rem; margin-bottom:10px;">{p['summary']}</p>
                          <a href="/providers/{p['slug']}/" class="btn btn-secondary">查看独立测评</a>
                          <a href="{p['inviteURL']}" target="_blank" rel="sponsored nofollow noopener" class="btn btn-coupon">前往官网 / 结算页</a>
                        </div>
                        '''
                    top4_html += '</div>'

                    # Full Homepage HTML
                    hero_html = f'''
                    <div class="hero-box">
                      <h1>当前年份机场推荐与 Clash 机场选择指南</h1>
                      <div class="hero-keywords-text">
                        面向新手提供当前年份机场推荐、性价比机场推荐、Clash 机场推荐与机场测评，覆盖便宜机场、稳定机场、机场节点推荐、机场订阅、AI 机场推荐和机场优惠码，帮助比较价格、流量、节点地区、设备兼容及购买前须知。
                      </div>
                      <div style="margin-top:12px;">
                        <a href="/posts/clash-airport-selection-guide/" class="btn">阅读 2026 选购指南全文</a>
                        <a href="/service/" class="btn btn-secondary">体验自营高可用线路</a>
                      </div>
                    </div>

                    <section style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:25px; margin:25px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                      <article style="line-height:1.75; color:#2d3748;">
                        <h2 style="color:#1a202c; border-bottom:2px solid #0056b3; padding-bottom:8px; margin-top:0;">📖 2026 机场推荐与 Clash 机场选择指南：从避坑到高阶玩法</h2>
                        <p style="font-size:0.95rem; color:#4a5568;">一份标准博客排版风格的《2026 机场推荐与 Clash 机场选择全指南》，涵盖选购逻辑、线路剖析与实操建议。</p>
                        
                        <div style="background:#f7fafc; border-left:4px solid #0056b3; padding:12px 16px; margin:15px 0; border-radius:4px; font-size:0.92rem; color:#4a5568;">
                          <strong>摘要：</strong>在当今网络环境下，无论你是需要访问学术数据库、处理外贸跨境电商业务，还是重度依赖 ChatGPT、Claude 等 AI 工具以及观看 4K 流媒体，一个稳定、高速的代理机场都是核心基础设施。很多新手面对琳琅满目的协议、节点倍率和专线术语时常常无从下手，甚至因贪图便宜购买超长年付套餐而遭遇服务商跑路。本文将拆解如何评估一个优质的 Clash 机场，并梳理选购要点。
                        </div>

                        <h3 style="color:#0056b3; margin-top:20px;">一、核心概念：看懂机场的底层线路</h3>
                        <p>判断一个机场的质量和成本，核心在于它采用的传输链路：</p>
                        
                        <div style="overflow-x:auto; margin:15px 0;">
                          <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.9rem;">
                            <thead>
                              <tr style="background:#edf2f7; border-bottom:2px solid #cbd5e0;">
                                <th style="padding:10px; border:1px solid #e2e8f0;">线路类型</th>
                                <th style="padding:10px; border:1px solid #e2e8f0;">优势</th>
                                <th style="padding:10px; border:1px solid #e2e8f0;">劣势</th>
                                <th style="padding:10px; border:1px solid #e2e8f0;">适用场景</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td style="padding:10px; border:1px solid #e2e8f0;"><strong>直连线路</strong> (VPS 自建/入门)</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">成本极低</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">易受网络波动影响，高峰期丢包严重</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">备用应急、低成本轻度查询</td>
                              </tr>
                              <tr style="background:#f7fafc;">
                                <td style="padding:10px; border:1px solid #e2e8f0;"><strong>国内中转</strong> (BGP/中继)</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">降低本地延迟，速度较快</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">敏感时期仍可能被封锁入口</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">普通网页浏览、常规高清视频</td>
                              </tr>
                              <tr>
                                <td style="padding:10px; border:1px solid #e2e8f0;"><strong>IPLC / IEPL 专线</strong></td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">点对点内网传输，不经过 GFW，无视波动</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">成本较高，单 G 流量单价偏高</td>
                                <td style="padding:10px; border:1px solid #e2e8f0;">AI 生产力、流媒体 4K、电竞加速</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>

                        <div style="background:#ebf8ff; border-left:4px solid #0056b3; padding:10px 15px; margin:15px 0; border-radius:4px; font-size:0.9rem; color:#0056b3;">
                          💡 <strong>关键建议：</strong>优先选择全节点或主力节点为 <strong>IPLC/IEPL 专线</strong> 的服务商。专线即便在特殊时期也能保持极高的连通率与低延迟。
                        </div>

                        <h3 style="color:#0056b3; margin-top:25px;">二、2026 年选购 Clash 机场的 4 大黄金法则</h3>
                        <ol style="padding-left:20px; line-height:1.8;">
                          <li style="margin-bottom:10px;">
                            <strong>坚持“月付”或“季付”，切莫盲目上年付</strong><br>
                            <span style="color:#4a5568; font-size:0.92rem;">再老牌的机场也有运维风险或不可控因素。新接触一家服务商时，一律先购买最低配置的月付套餐进行测速和稳定性验证。即使长期使用，也应保持至少一家备用机场（可备一个按量计费的非月抛节点）。</span>
                          </li>
                          <li style="margin-bottom:10px;">
                            <strong>关注原生 IP 与流媒体/AI 解锁能力</strong><br>
                            <span style="color:#4a5568; font-size:0.92rem;">不同平台对节点机房 IP 的封控力度大不相同：
                            <ul style="margin-top:4px; padding-left:20px;">
                              <li><strong>OpenAI / Claude / Gemini：</strong>对 IP 纯净度和地区有严格限制（香港节点普遍被部分模型屏蔽，需要美、日、新等地区的原生或住宅级 IP）。</li>
                              <li><strong>Netflix / Disney+ / HBO：</strong>需要节点具备流媒体专解能力，否则经常遇到“仅可观看自制剧”或直接报错。</li>
                            </ul>
                            </span>
                          </li>
                          <li style="margin-bottom:10px;">
                            <strong>注意节点倍率机制</strong><br>
                            <span style="color:#4a5568; font-size:0.92rem;">许多机场会设置高倍率节点（如 <code>2x</code>、<code>3x</code>）和低倍率节点（如 <code>0.2x</code>、<code>0.5x</code>）。高倍率节点通常线路更宽裕但耗费流量极快，日常挂后台建议配置规则分流，避免流量在不经意间耗尽。</span>
                          </li>
                          <li style="margin-bottom:10px;">
                            <strong>客户端兼容性与内核支持</strong><br>
                            <span style="color:#4a5568; font-size:0.92rem;">目前主流的 Clash 内核为 <strong>Mihomo (Clash.Meta)</strong>，支持 Vless、Hysteria2、TUIC、Trojan 等新一代低延迟抗封锁协议。挑选机场时，确保其订阅地址能无缝导入 Clash Verge Rev、Flclash 或 Clash Nyanpasu 等现代客户端。</span>
                          </li>
                        </ol>

                        <h3 style="color:#0056b3; margin-top:25px;">三、主流机场梯队与画像推荐</h3>
                        <p style="font-size:0.92rem; color:#4a5568;">根据不同的使用习惯和预算区间，目前的优质机场梯队通常分为以下几类：</p>
                        
                        <div style="display:grid; grid-template-columns:1fr; gap:15px; margin:15px 0;">
                          <div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:6px; padding:15px;">
                            <h4 style="margin:0 0 8px 0; color:#2d3748;">1. 高端专线主力型（适合：外贸、开发、重度生产力）</h4>
                            <p style="font-size:0.9rem; color:#4a5568; margin:0 0 4px 0;"><strong>特征：</strong>全 IPLC/IEPL 内网专线，延迟极低且极度稳定，多地 BGP 入口容灾。</p>
                            <p style="font-size:0.9rem; color:#4a5568; margin:0 0 4px 0;"><strong>代表模式：</strong>老牌企业级服务商（月费通常在 ¥30~¥60+，流量适中，不跑虚标）。</p>
                            <p style="font-size:0.9rem; color:#0056b3; margin:0;"><strong>优点：</strong>敏感时期稳如磐石，客服与工单响应迅速。</p>
                          </div>
                          
                          <div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:6px; padding:15px;">
                            <h4 style="margin:0 0 8px 0; color:#2d3748;">2. 性价比均衡型（适合：日常刷推、YouTube、追剧）</h4>
                            <p style="font-size:0.9rem; color:#4a5568; margin:0 0 4px 0;"><strong>特征：</strong>中转与专线混合配置，节点数量多，提供大流量包（如 ¥15~¥30 提供 150G~300G）。</p>
                            <p style="font-size:0.9rem; color:#0056b3; margin:0;"><strong>优点：</strong>价格适中，多平台解锁支持完善，满足绝大部分日常娱乐与影音需求。</p>
                          </div>
                          
                          <div style="background:#f7fafc; border:1px solid #e2e8f0; border-radius:6px; padding:15px;">
                            <h4 style="margin:0 0 8px 0; color:#2d3748;">3. 按量付费备用型（适合：低频使用、防失联备用）</h4>
                            <p style="font-size:0.9rem; color:#4a5568; margin:0 0 4px 0;"><strong>特征：</strong>不限制使用时间，按实际消耗流量计费（例如 100G/¥20，用完为止）。</p>
                            <p style="font-size:0.9rem; color:#0056b3; margin:0;"><strong>优点：</strong>无需每月续费，适合作为主机场突发故障时的应急跳板。</p>
                          </div>
                        </div>

                        <h3 style="color:#0056b3; margin-top:25px;">四、Clash 基础调优技巧</h3>
                        <p style="font-size:0.92rem; color:#4a5568;">在导入订阅链接后，建议在 Clash 客户端中做两处关键配置：</p>
                        <ul style="padding-left:20px; line-height:1.7; font-size:0.92rem; color:#4a5568;">
                          <li><strong>选择正确的运行模式：</strong>
                            <ul>
                              <li><strong>Rule（规则模式）：</strong>推荐模式，仅命中规则列表的国外网站走代理，国内流量直连，节省流量且国内站点不降速。</li>
                              <li><strong>Global（全局模式）：</strong>全部流量走代理，仅在调试特定锁区服务时开启。</li>
                            </ul>
                          </li>
                          <li style="margin-top:8px;"><strong>启用 TUN / 系统代理混合：</strong>遇到部分不走系统代理的终端命令行或桌面游戏时，在客户端中开启 <strong>TUN 模式</strong>，即可接管全局虚拟网卡流量。</li>
                        </ul>
                    <div style="background: linear-gradient(135deg, #f0f7ff 0%, #ffffff 100%); border: 1px solid #bae6fd; border-left: 5px solid #0284c7; border-radius: 8px; padding: 20px 24px; margin: 30px 0 20px 0; box-shadow: 0 2px 8px rgba(2, 132, 199, 0.06);">
                      <h3 style="margin: 0 0 10px 0; color: #0369a1; font-size: 1.25rem; font-weight: 700; display: flex; align-items: center; gap: 8px;">
                        <span>💡</span> 告别选择困难，找到最适合你的高性价比机场
                      </h3>
                      <p style="margin: 0; color: #334155; font-size: 0.98rem; line-height: 1.7;">
                        我们长期追踪主流与优质小众机场的表现，实时整理最新折扣、晚高峰稳定性测试及翻车避坑指南。不吹不黑，只用真实体验说话，帮你在复杂的网络服务中花最少的预算，买到最稳定的连接体验。
                      </p>
                    </div>

                    <section>
                      <h2>🔥 固定主推机场排行榜（独立实测与核验）</h2>
                      <p style="font-size:0.9rem; color:#666;">编辑部优先推荐的 4 大固定高可用服务，支持原生IP解锁与全客户端订阅导入：</p>
                      {top4_html}
                    </section>
                    <section style="margin-top:30px;">
                      <h2>📚 核心精选指南与客户端配置</h2>
                      <ul>
                        <li><a href="/posts/clash-airport-selection-guide/"><strong>2026 机场推荐与 Clash 机场选择指南：从避坑到高阶玩法</strong></a></li>
                        <li><a href="/posts/beginner-guide-to-cross-firewall/"><strong>2026 新手魔法上网入门：梯子与机场如何选择？（附选型清单）</strong></a></li>
                        <li><a href="/posts/clash-verge-rev-beginner-tutorial/"><strong>Clash Verge Rev 零基础配置教程：从节点导入到规则分流</strong></a></li>
                        <li><a href="/posts/airport-node-timeout-troubleshooting/"><strong>节点超时与订阅无法更新？魔法机场新手常见 5 大故障排查</strong></a></li>
                        <li><a href="/posts/best-proxy-for-chatgpt-and-claude/"><strong>流畅使用 AI 工具：ChatGPT 与 Claude 专线机场选购要点</strong></a></li>
                      </ul>
                    </section>
                    <section style="margin-top:30px;">
                      <h2>🌐 28 家机场服务商全量测评库</h2>
                      <p>查阅完整 28 家机场服务商测评与节点优惠：<a href="/providers/" class="btn btn-secondary">进入机场测评库 (/providers/)</a></p>
                    </section>
                    <section style="margin-top:30px;">
                      <h2>❓ 常见问题排错中心 (FAQ 100)</h2>
                      <p>查阅 Clash、Sing-box、Shadowrocket 常见排错与 100 FAQ 问答：<a href="/posts/faq/">常见排错中心 (/posts/faq/)</a></p>
                    </section>
                    '''
                    page_html = render_html_page(title, desc, canonical, hero_html, is_home=True)
                else:
                    slug = rel_path.replace("\\", "/").replace(".md", "")
                    if slug.endswith("/index"):
                        slug = slug[:-6]
                    
                    out_dir = os.path.join(PUBLIC_DIR, slug)
                    canonical = BASE_URL + slug + "/"

                    title_text = fm.get("title", slug)
                    title = title_text + " - 机场推荐平台"
                    desc = fm.get("summary", fm.get("description", SEO_PROFILE["siteDescription"]))

                    # Breadcrumbs
                    bc_html = f'<div class="breadcrumbs"><a href="/">首页</a> &gt; <span>{title_text}</span></div>'
                    
                    # Check if body_html already has h1 tag
                    has_h1 = "<h1" in body_html.lower()
                    h1_header = f'<h1>{title_text}</h1>' if not has_h1 else ''

                    # Trust links bar at bottom of articles
                    trust_bar_html = '''
                    <div class="trust-links-bar">
                      📖 编辑部透明指引：<a href="/methodology/">评测方法</a> | <a href="/corrections/">纠错与更新</a> | <a href="/terms/">服务条款</a> | <a href="/affiliate-disclosure/">联盟披露</a> | <a href="/contact/">联系我们</a>
                    </div>
                    '''

                    # Content article
                    article_html = f'''
                    <article>
                      {bc_html}
                      {h1_header}
                      {body_html}
                      {trust_bar_html}
                    </article>
                    '''

                    page_html = render_html_page(title, desc, canonical, article_html)

                os.makedirs(out_dir, exist_ok=True)
                with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as out_f:
                    out_f.write(page_html)

                urls.append(canonical)
                search_index_items.append({
                    "title": fm.get("title", slug),
                    "url": "/" + slug + "/",
                    "summary": fm.get("summary", fm.get("description", ""))
                })

    # Build /providers/index.html List Page
    providers_out_dir = os.path.join(PUBLIC_DIR, "providers")
    os.makedirs(providers_out_dir, exist_ok=True)

    provider_cards_html = '<div class="provider-grid">'
    for p in PROVIDERS:
        rank_badge = f'<span class="badge badge-top">TOP {p["rank"]} 推荐</span>' if p.get('isPrimary') else f'<span class="badge">编辑推荐 #{p["rank"]}</span>'
        card_class = "provider-card top-rank" if p.get('isPrimary') else "provider-card"
        
        provider_cards_html += f'''
        <div class="{card_class}">
          {rank_badge}
          <h3 class="provider-title">{p['name']}</h3>
          <p style="font-size:0.85rem; color:#555;"><strong>适用场景：</strong>{p.get('suitableFor', '日常网页浏览、4K影音与多设备办公')}</p>
          <p style="font-size:0.85rem; color:#555;"><strong>参考套餐：</strong>{p.get('priceFrom', '以结算页为准')} ({p.get('trafficFrom', '以结算页为准')}) | 优惠码：<code style="color:#d9534f;">{p.get('coupon', '暂无优惠码')}</code></p>
          <p style="font-size:0.9rem; margin-bottom:12px;">{p['summary']}</p>
          <div>
            <a href="/providers/{p['slug']}/" class="btn btn-secondary">查看独立测评</a>
            <a href="{p['inviteURL']}" target="_blank" rel="sponsored nofollow noopener" class="btn btn-coupon">前往官网 / 结算页</a>
          </div>
        </div>
        '''
    provider_cards_html += '</div>'

    providers_page_content = f'''
    <section>
      <div class="breadcrumbs"><a href="/">首页</a> &gt; <span>28 家机场服务商全量测评库</span></div>
      <h1>28 家机场服务商全量测评与官网入口</h1>
      <p style="color:#555; font-size:0.95rem;">编辑部整理 2026 年 28 家主流魔法上网机场节点服务商，包含中文名称、详细价格、流量配置、专享优惠码及官网结算页直达入口：</p>
      {provider_cards_html}
    </section>
    '''

    providers_index_html = render_html_page(
        "28 家机场服务商全量测评与官网入口 - 机场推荐平台",
        "汇总 2026 年最新 28 家机场服务商独立测评、价格套餐、节点地区、优惠码及直达官网结算页入口。",
        BASE_URL + "providers/",
        providers_page_content
    )

    with open(os.path.join(providers_out_dir, "index.html"), "w", encoding="utf-8") as out_f:
        out_f.write(providers_index_html)
    urls.append(BASE_URL + "providers/")

    # Build /faq/index.html List Page
    faq_out_dir = os.path.join(PUBLIC_DIR, "faq")
    os.makedirs(faq_out_dir, exist_ok=True)

    faq_csv_path = os.path.join(DOCS_DIR, "faq-keywords-100.csv")
    faq_items_html = '<div class="faq-list">'
    if os.path.exists(faq_csv_path):
        with open(faq_csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                faq_items_html += f'''
                <div style="border-bottom:1px dashed #ccc; padding:12px 0;">
                  <h3 style="font-size:1.1rem; margin:0 0 6px 0;">
                    <a href="/faq/{row['slug']}/" style="color:#0056b3; text-decoration:none;">❓ {row['questionTitle']}</a>
                  </h3>
                  <p style="font-size:0.9rem; color:#444; margin:0 0 5px 0;">关于{row['keyword']}的解答：解析{row['searchIntent']}与操作误区。</p>
                  <a href="/faq/{row['slug']}/" style="font-size:0.85rem; color:#0056b3;">查看完整解答 &rarr;</a>
                </div>
                '''
    faq_items_html += '</div>'

    faq_page_content = f'''
    <section>
      <div class="breadcrumbs"><a href="/">首页</a> &gt; <span>常见排错与 FAQ 解答中心 (100)</span></div>
      <h1>常见排错与 FAQ 问答解答中心 (100 项)</h1>
      <p style="color:#555; font-size:0.95rem;">包含 100 项涵盖 Clash、Sing-box、Shadowrocket 客户端配置，节点超时排查，TUN 模式无法联网及防失联指南：</p>
      {faq_items_html}
    </section>
    '''

    faq_index_html = render_html_page(
        "常见排错与 FAQ 问答解答中心 (100项) - 机场推荐平台",
        "涵盖 100 项 Clash、Sing-box、Shadowrocket 客户端配置，节点超时排错，TUN 模式及防失联解答。",
        BASE_URL + "faq/",
        faq_page_content
    )

    with open(os.path.join(faq_out_dir, "index.html"), "w", encoding="utf-8") as out_f:
        out_f.write(faq_index_html)
    urls.append(BASE_URL + "faq/")

    # Generate search-index.json
    with open(os.path.join(PUBLIC_DIR, "search-index.json"), "w", encoding="utf-8") as f:
        json.dump(search_index_items, f, ensure_ascii=False, indent=2)

    # Build Sitemap.xml
    sitemap_path = os.path.join(PUBLIC_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in urls:
            f.write(f'  <url><loc>{url}</loc><lastmod>2026-09-22</lastmod></url>\n')
        f.write('</urlset>\n')

    # Build RSS index.xml
    rss_path = os.path.join(PUBLIC_DIR, "index.xml")
    with open(rss_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n')
        f.write('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n')
        f.write('  <channel>\n')
        f.write('    <title>机场推荐平台 - 节点评测与客户端配置指南</title>\n')
        f.write('    <link>https://jichangtuijianpingtai.xyz/</link>\n')
        f.write('    <description>机场推荐平台专注为新手提供梯子推荐、魔法上网测速对比及 Clash 客户端配置教程。</description>\n')
        f.write('  </channel>\n')
        f.write('</rss>\n')

    print(f"Build completed successfully! Generated {len(urls)} pages in public/ directory.")

if __name__ == "__main__":
    build()
