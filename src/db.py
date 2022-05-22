import sqlite3
import os
import pathlib
import hashlib


def get_file_list(folder, extensions=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    """
    Returns list of files in folder with given extensions.
    """
    file_list = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = pathlib.Path(dirpath + '\\' + filename)
            if path.suffix.lower() in extensions:
                file_list.append(str(path))
    return file_list


def db_create_table():
    with sqlite3.connect('testdb.db') as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE files (path text, hash text, tags text)")
    conn.close()


def db_get_tables():
    with sqlite3.connect('testdb.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        print(cur.fetchall())
    conn.close()


def db_get_record(path: str): #w jakiej formie zwraca?
    result = ""
    with sqlite3.connect('testdb.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM files WHERE path=:path;", {"path": path})
        result = cur.fetchone()
    conn.close()
    return result


def db_hash_exist(hash: str):
    result = ""
    with sqlite3.connect('testdb.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT hash FROM files WHERE hash=:hash;", {"hash": hash})
        result = cur.fetchone()
    conn.close()
    return result


def db_get_tags(hash: str):
    result = ""
    with sqlite3.connect('testdb.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT tags FROM files WHERE hash=:hash;", {"hash": hash})
        result = cur.fetchone()
    conn.close()
    return result


def db_insert_row(path: str, hash: str, tags: str):
    with sqlite3.connect('testdb.db') as conn:
        conn.execute("INSERT INTO files VALUES(:path, :hash, :tags);", {"path": path, "hash": hash, "tags": tags})
    conn.close()


def db_update_record(path: str, hash: str, tags: str):
    with sqlite3.connect('testdb.db') as conn:
        conn.execute("UPDATE files SET hash=:hash, tags=:tags WHERE path=:path", {"hash": hash, "tags": tags, "path": path})
    conn.close()


def get_hash(img_path):
    with open(img_path, "rb") as f:
        img_hash = hashlib.sha1()
        while chunk := f.read(8192):
            img_hash.update(chunk)
    return img_hash.hexdigest()

# with sqlite3.connect('testdb.db') as conn:
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM files")
#     result = cur.fetchall()
#     print(result)
# conn.close()

# with sqlite3.connect('testdb.db') as conn:
#     cur = conn.cursor()
#     cur.execute("DELETE FROM files")
#     result = cur.fetchall()
#     print(result)
# conn.close()