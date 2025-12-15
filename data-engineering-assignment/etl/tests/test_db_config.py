"""
Smoke test for database configuration.

Purpose:
- Verify DB credentials are loaded correctly
- Verify NeonDB/PostgreSQL connection works
- Ensure db_config.get_db_connection() is usable by ETL
"""

from etl.config.db_config import get_db_connection


def test_db_connection():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()

        assert result[0] == 1
        print("✅ Database connection test PASSED")

    except Exception as e:
        print("❌ Database connection test FAILED")
        raise e

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    test_db_connection()
