import psycopg2
import yaml
import os

# connect to Postgres by reading info from config file
# connection needs to be closed after this function is called
def connect():
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__), '../../config/db.yml')
    with open(yml_path, 'r') as file:
      config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                          user=config['user'],
                          password=config['password'],
                          host=config['host'],
                          port=config['port'])

def exec_sql_file(path):
    """Opens up an SQL file and executes everything in it. Commits changes."""
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()

def exec_get_one(sql, args={}):
    """Runs a query and only returns the top result. Does *not* commit changes."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

def exec_get_all(sql, args={}):
    """Runs a query and returns all results as a list of tuples. Does *not* commit changes."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    # https://www.psycopg.org/docs/cursor.html#cursor.fetchall

    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

def exec_commit(sql, args={}):
    """Runs SQL and commits the operation. Use for making updates to code."""
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result

def exec_commit_return(sql, args={}):
    """Runs SQL, commits the operation, and returns the resulting commit. Requires use of a RETURNING query.
    Use for making updates to code."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    result = cur.fetchone()
    conn.commit()
    conn.close()
    return result