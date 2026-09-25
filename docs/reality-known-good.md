# Reality known-good

Проверенная на мобильном интернете рабочая схема для DE-1 и FR-1:

- protocol: VLESS
- security: Reality
- transport: TCP/raw
- public port: 9443
- serverName: `www.googletagmanager.com`
- dest: `www.googletagmanager.com:443`
- show: `false`
- xver: `0`
- spiderX: `/`
- client fingerprint: `chrome`
- flow: absent on both server user and client config in current working setup

## Important

Не возвращаться к `www.microsoft.com` без отдельного теста: на текущей инфраструктуре рабочий эталон подтверждён именно с `www.googletagmanager.com`.

Секретные параметры (Reality private keys, shortId, user UUID, subscription token, Node SECRET_KEY) здесь не хранятся.
