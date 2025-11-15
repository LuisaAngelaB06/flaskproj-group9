import os
from sqlalchemy.engine.url import make_url
import mysql.connector
from mysql.connector import Error # Note: Changed 'error' to 'Error' for standard import
from config import Config # <-- FIX: Import the class 'Config'
def create_database_if_not_exists():
    try:
        # 1. Corrected config object name from Config to config
        url = make_url(Config().SQLALCHEMY_DATABASE_URI) # Instantiate and access
        if url.get_backend_name() != "mysql":
            # 2. Corrected 'pritnt' typo
            print("only mysql is supported by this script")
            return False
        # Coerce values that are empty or the literal string 'None' -> treat as missing
        def _clean(val, default=None):
            if val is None:
                return default
            s = str(val).strip()
            if s == "" or s.lower() == "none":
                return default
            return s

        user = _clean(url.username, "")
        password = _clean(url.password, "")
        host = _clean(url.host, "localhost")
        port = url.port or 3306
        database = _clean(url.database, None)
        # 3. Added colon to if statement
        if not database:
            print("No database name in SQLALCHEMY URI")
            return False
        # 4. Corrected call to mysql.connector.connect()
        conn = mysql.connector.connect(host=host, user=user, password=password, port=port)
        cur = conn.cursor()
        # 5. Corrected SQL: changed EXIST to EXISTS, and fixed formatting/quoting
        # Quote the database name to be safe and choose a reasonable charset/collation
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS `{database}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        print(f"Database '{database}' is ready")
        # 6. Separated close calls with a semicolon or put on separate lines
        cur.close()
        conn.close()
        return True
    except Error as e:
        print(f"MySQL error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
# 7. Corrected the if __name__ == "__main__": block
if __name__ == '__main__':
    ok = create_database_if_not_exists()
    print("Done" if ok else "Failed")