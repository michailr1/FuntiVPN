# FuntiVPN

Конфигурация и документация Funti VPN на базе Remnawave.

## Структура

- `remnawave/subscription-page/funti-vpn.json` — кастомный шаблон Subscription Page.
- `remnawave/subscription-page/logo.svg` — логотип Funti VPN.
- `docs/architecture.md` — текущая архитектура.
- `docs/reality-known-good.md` — проверенные параметры Reality.

## Безопасность

В репозиторий **не кладём** секреты: Node SECRET_KEY, Reality private keys, UUID пользователей, subscription tokens, пароли, `.env`.

## Subscription Page

Шаблон основан на официальном Remnawave Subscription Page config и сокращён до RU/EN и основных клиентов.

Текущий v1:
- iOS: Shadowrocket
- Android: Happ, v2rayNG
- macOS: Happ
- Windows: Happ

V2Box добавим отдельной карточкой после проверки корректного deeplink/импорта подписки.
