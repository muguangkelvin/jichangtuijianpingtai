import os
import sys
import json
import csv
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PUBLIC_DIR = os.path.join(WORKSPACE_DIR, "public")
DOCS_DIR = os.path.join(WORKSPACE_DIR, "docs")

# Blocklist
BLOCKLIST = ["三毛机场", "猫梦博客", "Gaterank", "星维机场", "一毛机场", "一份机场", "二毛博客"]

def verify():
    print("=== Starting Full Automated SEO & Compliance Audit ===")
    errors = []
    warnings = []

    # 1. Verify Public Directory Exists
    if not os.path.exists(PUBLIC_DIR):
        errors.append("PUBLIC_DIR does not exist. Run build_site.py first!")
        print("\n".join(errors))
        sys.exit(1)

    # 2. Check essential static files
    for req_file in ["index.html", "robots.txt", "sitemap.xml", "index.xml"]:
        fp = os.path.join(PUBLIC_DIR, req_file)
        if not os.path.exists(fp):
            errors.append(f"Missing required static output file: {req_file}")
        else:
            print(f"[OK] Found {req_file}")

    # 3. Walk HTML files and check HTML structure, Canonical, H1, Meta, Sponsored links, and Blocklist
    html_count = 0
    for root, dirs, files in os.walk(PUBLIC_DIR):
        for file in files:
            if file.endswith(".html"):
                html_count += 1
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, PUBLIC_DIR)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check Blocklist
                for blocked in BLOCKLIST:
                    if blocked in content:
                        errors.append(f"[{rel_path}] Found blocked reference publisher term: '{blocked}'")

                # Check H1 count
                h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
                if len(h1_matches) == 0:
                    errors.append(f"[{rel_path}] Missing <h1> tag")
                elif len(h1_matches) > 1:
                    errors.append(f"[{rel_path}] Found {len(h1_matches)} <h1> tags (Expected exactly 1)")

                # Check Title
                if "<title>" not in content or "</title>" not in content:
                    errors.append(f"[{rel_path}] Missing <title> tag")

                # Check Meta Description
                if 'name="description"' not in content:
                    errors.append(f"[{rel_path}] Missing <meta name=\"description\"> tag")

                # Check Canonical
                if 'rel="canonical"' not in content:
                    errors.append(f"[{rel_path}] Missing <link rel=\"canonical\"> tag")

                # Check Affiliate link rel attributes
                aff_links = re.findall(r'href="(https?://[^"]+code=[^"]+)"([^>]*)>', content)
                for aff_url, attrs in aff_links:
                    if 'rel="sponsored nofollow noopener"' not in attrs and "sponsored" not in attrs:
                        warnings.append(f"[{rel_path}] Affiliate link missing rel='sponsored nofollow noopener': {aff_url}")

    print(f"[OK] Audited {html_count} HTML pages.")

    # 4. Verify 100 FAQ CSV dataset
    faq_csv = os.path.join(DOCS_DIR, "faq-keywords-100.csv")
    if not os.path.exists(faq_csv):
        errors.append("Missing docs/faq-keywords-100.csv dataset!")
    else:
        with open(faq_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if len(rows) != 100:
                errors.append(f"docs/faq-keywords-100.csv has {len(rows)} entries (Expected exactly 100)")
            else:
                print(f"[OK] docs/faq-keywords-100.csv verified with exactly 100 FAQ entries!")

    # 5. Output Results
    print("\n=== Verification Audit Summary ===")
    if warnings:
        print(f"Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  [FAIL] {e}")
        sys.exit(1)
    else:
        print("ALL SEO, HTML, CANONICAL, & COMPLIANCE AUDITS PASSED CLEANLY!")

if __name__ == "__main__":
    verify()
