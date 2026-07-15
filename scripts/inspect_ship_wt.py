#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import time
import requests

API = "https://wiki.biligame.com/wjdlglr/api.php"
s = requests.Session()
s.headers["User-Agent"] = "guoyunkaituo-kb/1.0 (novel research)"

for title in [
    "FG300型-装甲护卫舰",
    "AC721-重型导弹驱逐舰",
    "光锥级-TE-综合导弹巡洋舰",
    "KCCPV2.0-轻型载机巡洋舰",
    "CV3000级-快速航空母舰",
]:
    time.sleep(0.8)
    r = s.get(
        API,
        params={"action": "parse", "page": title, "prop": "wikitext", "format": "json"},
        timeout=60,
    )
    print("status", r.status_code, title, "ctype", r.headers.get("Content-Type"), "len", len(r.text))
    if not r.text.strip().startswith("{"):
        print(r.text[:300])
        continue
    wt = r.json()["parse"]["wikitext"]["*"]
    print("====", title, "wt", len(wt))
    params = re.findall(r"\|\s*([^\|=\n]{1,30})\s*=\s*([^\|\n]*)", wt)
    for k, v in params:
        v = v.strip()
        if not v:
            continue
        if any(
            x in k
            for x in [
                "结构",
                "装甲",
                "抵抗",
                "护盾",
                "巡航",
                "曲率",
                "金属",
                "晶体",
                "重氢",
                "指挥",
                "对舰",
                "对空",
                "攻城",
                "仓储",
                "长度",
                "稀有",
                "所属",
                "生产",
                "满",
            ]
        ):
            print(f"  {k.strip()} = {v[:80]}")
    print()
