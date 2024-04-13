import psycopg2

# Define the function conectar_db
def conectar_db():
    try:
        miConexion = psycopg2.connect(
            dbname="kqjurbyz",
            user="kqjurbyz",
            password="ckOilkZBjplfiLQ11Mr6fZivW2dZDBEe",
            host="kesavan.db.elephantsql.com",
            port="5432"
        )
        return miConexion
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None
