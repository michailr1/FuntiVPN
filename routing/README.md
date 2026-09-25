# Funti VPN routing

This directory contains the Funti-owned split-routing policy.

## Goal

Russian infrastructure and selected Russian services should use the user's normal Internet connection (DIRECT).
Everything else stays on the selected VPN node.

The source of truth is `routing/rules.json`.

## v1 policy

DIRECT:
- private/LAN IPv4 ranges;
- GeoIP RU;
- Gosuslugi, FNS and Moscow public-service domains;
- major Russian banks and NSPK/Mir;
- Ozon, Wildberries;
- Yandex, VK;
- Avito, 2GIS, RZD and Russian Post.

VPN:
- everything not matched above.

We intentionally do not use a blanket `.ru -> DIRECT` rule in v1. Some .ru domains may themselves need a VPN. GeoIP RU plus an explicit service allowlist is safer.

## Community basis

The design follows patterns already used by the Remnawave/VPN community:
- legiz-ru/my-remnawave: separate routing import on subscription pages and RU routing templates;
- NikitaNekhay/vpn-routing-rules: V2Box iOS route import through `v2box://routes?multi=...`;
- common Shadowrocket configs: external RULE-SET + GEOIP + FINAL ordering.

We maintain our own lists and generated artifacts instead of depending on third-party rule URLs at runtime.

## Files

- `rules.json` - source of truth;
- `generate.py` - generates client artifacts;
- `shadowrocket/ru-direct.list` - Shadowrocket rule set;
- `shadowrocket/funti-ru-direct.conf` - importable Shadowrocket routing config;
- `v2box/v2box-routes.json` - readable V2Box routes;
- `v2box/v2box-import.txt` - V2Box iOS deep link.

After editing `rules.json`, run:

```bash
python3 routing/generate.py
```

Then review the diff before publishing.
