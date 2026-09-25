# Architecture

## Control plane

- `core.funti.cc` — GreenCloud, основной Remnawave control plane / Subscription Page / FuntiDesk.
- `free.funti.cc` — Remnawave admin panel.
- `sub.funti.cc` — пользовательские подписки / Subscription Page.

## VPN nodes

- `DE-1` — `de.funti.cc:9443`, VLESS Reality.
- `FR-1` — `france.funti.cc:9443`, VLESS Reality.

Пользователям выдаётся одна постоянная Remnawave subscription URL. Ноды добавляются в неё централизованно через Internal Squad `Main-VPN`.

## Legacy France

3x-ui пока сохраняется параллельно как rollback и для отдельных proxy-сервисов. Не удалять до отдельного решения.
