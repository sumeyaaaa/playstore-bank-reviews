import oracledb




def create_table(conn, table_sql):
    """Create a table with the given SQL statement."""
    with conn.cursor() as cur:
        cur.execute(table_sql)
        conn.commit()

def insert_data(conn, sql, data):
    """Insert single or multiple records into the table."""
    with conn.cursor() as cur:
        if isinstance(data[0], (tuple, list)):
            cur.executemany(sql, data)
        else:
            cur.execute(sql, data)
        conn.commit()

def fetch_data(conn, sql, params=None):
    """Fetch data as a list of tuples."""
    with conn.cursor() as cur:
        cur.execute(sql, params or ())
        return cur.fetchall()

def close_connection(conn):
    """Close the Oracle DB connection."""
    conn.close()
