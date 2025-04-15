import psycopg2

try:
    conn = psycopg2.connect(
        dbname="coffe_db",
        user="dasha",
        password="1234",
        host="127.0.0.1",
        port="5432"
    )
    print("✅ Успешное подключение!")
except Exception as e:
    print("❌ Ошибка подключения:", e)
