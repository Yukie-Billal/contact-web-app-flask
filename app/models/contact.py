from . import nama, cursor, db

def create_table() :
    sql = "SHOW TABLES LIKE 'contact'"
    
    try :
        check = cursor.execute(sql)
        if check == 0 :
            sql = """
            CREATE TABLE contact (
                id int NOT NULL AUTO_INCREMENT,
                nama varchar(50) NOT NULL,
                nohp varchar(13) NOT NULL,
                PRIMARY KEY (`id`)
            ) AUTO_INCREMENT=1
            """
            cursor.execute(sql)
            print("Tabel Dibuat")
            db.close()
        else :
            print("Sudah Tersedia")
    except Exception as e :
        print(e)
        
def insert(nama:str, nohp:str) :
    sql = "INSERT INTO contact (nama,nohp) VALUES ('%s','%s')" % (nama,nohp)
    
    try :
        cursor.execute(sql)
        db.commit()
    except Exception as e :
        print(e)
        db.rollback()

def update(id,nama,nohp) :
    sql = "UPDATE contact SET nama = '%s', nohp = '%s' WHERE id=%d" % (nama,nohp,id)
    
    try :
        cursor.execute(sql)
        db.commit()
        print("Updated")
    except Exception as e :
        print(e)
        
def destroy(id) :
    sql = "DELETE FROM contact WHERE id=%d" % id
    try :
        cursor.execute(sql)
        db.commit()
        print("Deleted")
    except Exception as e :
        print(e)
    
def getContact() -> list:
    sql = "SELECT * FROM contact"
    try :
        cursor.execute(sql)
        
        return cursor.fetchall()
    except Exception as e :
        return []
    
def getContactId(id) -> list:
    sql = "SELECT * FROM contact WHERE id=%d" % id 
    try :
        cursor.execute(sql)
        type(cursor.fetchone)
        print(cursor.fetchone)
        return cursor.fetchone()
    except Exception as e :
        return False    