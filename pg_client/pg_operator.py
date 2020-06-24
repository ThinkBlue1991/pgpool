import psycopg2
import psycopg2.extras
import psycopg2.pool


class PostgresDB(object):
    _pool = None
    _instance = None

    def __new__(cls, host, port, user, password, db_name, min_conn, max_conn,
                cursor_factory=psycopg2.extras.DictCursor):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._pool = psycopg2.pool.ThreadedConnectionPool(
                minconn=min_conn,
                maxconn=max_conn,
                host=host,
                port=port,
                user=user,
                password=password,
                dbname=db_name,
                cursor_factory=cursor_factory)
        return cls._instance

    # def __init__(self):
    #     pass

    @property
    def pool(self) -> psycopg2.pool.ThreadedConnectionPool:
        return self._pool

    @pool.setter
    def pool(self, pool: psycopg2.pool.ThreadedConnectionPool):
        self._pool = pool

    def insert(self, sql):
        try:
            flag = True
            conn = self._pool.getconn()
            cur = conn.cursor()
            cur.execute(sql)
            info = cur.statusmessage
            conn.commit()
        except Exception as ex:
            flag = False
            info = str(ex)
        finally:
            cur.close()
            self._pool.putconn(conn)
            return flag, info

    def delete(self, sql):

        try:
            conn = self._pool.getconn()
            cur = conn.cursor()
            flag = True
            cur.execute(sql)
            info = cur.statusmessage
            conn.commit()
        except Exception as ex:
            flag = False
            info = str(ex)
        finally:
            cur.close()
            self._pool.putconn(conn)
            return flag, info

    def query_all(self, sql):

        try:
            flag = True
            conn = self._pool.getconn()
            cur = conn.cursor()
            cur.execute(sql)
            info = cur.fetchall()
        except Exception as ex:
            flag = False
            info = str(ex)
        finally:
            cur.close()
            self._pool.putconn(conn)
            return flag, info

    def query_one(self, sql):
        try:
            flag = True
            conn = self._pool.getconn()
            cur = conn.cursor()
            cur.execute(sql)
            info = cur.fetchone()
        except Exception as ex:
            flag = False
            info = str(ex)
        finally:
            cur.close()
            self._pool.putconn(conn)
            return flag, info

    def update(self, sql):

        try:
            flag = True
            conn = self._pool.getconn()
            cur = conn.cursor()
            cur.execute(sql)
            info = cur.statusmessage
            conn.commit()
        except Exception as ex:
            flag = False
            info = str(ex)
        finally:
            cur.close()
            self._pool.putconn(conn)
            return flag, info
