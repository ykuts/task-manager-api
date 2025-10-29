# 🧪 Примеры тестирования API

## Замени BASE_URL на свой адрес:
# Локально: http://localhost:5000
# Railway: https://твой-проект.up.railway.app

BASE_URL="http://localhost:5000"

## 1️⃣ Получить все задачи
curl $BASE_URL/tasks

## 2️⃣ Получить задачу по ID
curl $BASE_URL/tasks/1

## 3️⃣ Создать новую задачу
curl -X POST $BASE_URL/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Купить молоко"}'

## 4️⃣ Обновить задачу (отметить как выполненную)
curl -X PATCH $BASE_URL/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

## 5️⃣ Обновить название задачи
curl -X PATCH $BASE_URL/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Купить молоко и хлеб"}'

## 6️⃣ Удалить задачу
curl -X DELETE $BASE_URL/tasks/1

## ❌ Тесты ошибок

# Попытка получить несуществующую задачу
curl $BASE_URL/tasks/999

# Попытка создать задачу без title
curl -X POST $BASE_URL/tasks \
  -H "Content-Type: application/json" \
  -d '{}'

# Попытка создать задачу с пустым title
curl -X POST $BASE_URL/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": ""}'

# Попытка обновить несуществующую задачу
curl -X PATCH $BASE_URL/tasks/999 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Попытка удалить несуществующую задачу
curl -X DELETE $BASE_URL/tasks/999

## 📱 Для тестирования с Railway:
# 1. После деплоя получи свою ссылку
# 2. Замени BASE_URL на: https://твой-проект.up.railway.app
# 3. Запусти команды выше
# 4. Поделись ссылкой с друзьями!
