# 1. 3.11-slim
FROM python:3.11-slim

# 2. Рабочая папка
WORKDIR /app

# 3. Не под  рутом
RUN useradd -m -u 1000 appuser

# 4. Копируем 
COPY --chown=appuser:appuser app.py .

# 5. Переключаемся
USER appuser

# 6. Порт 8080
EXPOSE 8080

# 7. Старт
CMD ["python", "app.py"]