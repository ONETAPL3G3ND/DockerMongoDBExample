from pymongo import MongoClient

# Подключение к MongoDB, запущенной в контейнере Docker
client = MongoClient('localhost', 27017)

# Выбор базы данных
db = client['mydatabase']

# Выбор коллекции
collection = db['mycollection']

# Вставка документа
result = collection.insert_one({'name': 'John', 'age': 30})

# Вывод id вставленного документа
print(f'Inserted document id: {result.inserted_id}')

# Поиск всех документов в коллекции
for document in collection.find():
    print(document)

# Отключение от MongoDB
client.close()
