#!/usr/bin/env python3
"""Generate Funti VPN routing artifacts from routing/rules.json."""
from __future__ import annotations
import base64
import json
import re
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "rules.json"

def stable_name(label: str) -> str:
    return "route." + str(uuid.uuid5(uuid.NAMESPACE_URL, "https://funti.cc/routing/" + label)).upper()

def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    direct = data["direct"]

    shadow = [
        "# Funti RU Direct rules",
        "# Generated from routing/rules.json. Do not edit manually.",
    ]
    shadow += [f"DOMAIN-SUFFIX,{d},DIRECT" for d in direct["domain_suffix"]]
    shadow += [f"DOMAIN-KEYWORD,{d},DIRECT" for d in direct["domain_keyword"]]
    shadow += [
        "IP-CIDR,10.0.0.0/8,DIRECT,no-resolve",
        "IP-CIDR,172.16.0.0/12,DIRECT,no-resolve",
        "IP-CIDR,192.168.0.0/16,DIRECT,no-resolve",
        "GEOIP,RU,DIRECT",
    ]
    (ROOT / "shadowrocket" / "ru-direct.list").write_text("\n".join(shadow) + "\n", encoding="utf-8")

    suffix_regex = ["regexp:(^|\\\\.)" + re.escape(d) + "$" for d in direct["domain_suffix"]]
    routes = [
        {
            "name": stable_name("keywords"),
            "type": "Domain",
            "tag": "direct",
            "matchMode": "keyword",
            "listIP": [],
            "remark": "Funti RU services -> DIRECT",
            "isEnable": True,
            "list": direct["domain_keyword"],
        },
        {
            "name": stable_name("suffixes"),
            "type": "Domain",
            "tag": "direct",
            "matchMode": "regexp",
            "listIP": [],
            "remark": "Funti RU domain suffixes -> DIRECT",
            "isEnable": True,
            "list": suffix_regex,
        },
        {
            "name": stable_name("geoip"),
            "type": "IP",
            "tag": "direct",
            "matchMode": "full",
            "listIP": ["geoip:private", "geoip:RU"],
            "remark": "Funti RU/private IP -> DIRECT",
            "isEnable": True,
            "list": [],
        },
    ]
    route_json = json.dumps(routes, ensure_ascii=False, indent=2) + "\n"
    (ROOT / "v2box" / "v2box-routes.json").write_text(route_json, encoding="utf-8")
    compact = json.dumps(routes, ensure_ascii=False, separators=(",", ":"))
    link = "v2box://routes?multi=" + base64.b64encode(compact.encode("utf-8")).decode("ascii")
    (ROOT / "v2box" / "v2box-import.txt").write_text(link + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
