##Effective Mobile Test

Nginx + Python

Простая связка прокси-сервера и бэкенда в Docker.

Схема работы
Client -> Nginx (80) -> Python (8080)

Взаимодействие контейнеров идет через внутреннюю сеть Docker. Бэкенд изолирован от внешнего мира.

Требования к запуску:

- Docker (версии 20.10+)
- Docker Compose ( V2, встроенный в Docker )
- Git ( для клонирования репозитория )

Запуск:

```
git clone https://git.iiba.pw/h2nexuspl/effective.git
cd effective
```

```
docker compose up -d
```

Проверка:

```
curl http://localhost
```

Ожидаемый вывод: Hello from Effective Mobile!

Технические детали:

Base images: nginx:1.27-alpine, python:3.11-slim.

Security: Бэкенд работает под appuser.

Nginx: Настроен upstream, пробрасываются заголовки Host, X-Real-IP и X-Forwarded-For.

Network: Сервисы объединены в bridge-сеть effective_net.
