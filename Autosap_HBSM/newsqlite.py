# ****************************************************************************
#  Program Description : Script Executes SQL Commands(Cretae, Insert, Read)  *
#  Program Name:  AutosapHBSM/newsqlite.py                                   *
#          Date:  21/06/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Erry Lavakumar                                             *
#  Return Codes:                                                             *
#                 0 - Success                                                *
#                 1 - Error check log file                                   *
# ****************************************************************************
#  AutoSAP Automation                                                        *
#  --------------------                                                      *
#  Sr.         Role           Member          Email                          *
#  ---------   ----------     --------------  -------------------------------*
#  1           Developer      NIKHIL CHALIKWAR  nikhil.x.chalikwar@gsk.com   *
#  2           Developer      erry lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      akoju sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************


import sqlite3

def create_db(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()

        # Create a table with 'name', 'date', and 'time' fields
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hbsm_entries (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                date DATE,
                time TIME
            )
        """)

        print(f"Table 'hbsm_entries' created successfully.")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def read_from_db(filename,name):

    conn = None
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()

        # Execute a SELECT query
        cursor.execute(f"SELECT name FROM hbsm_entries where name like '{name}' ")
        row = cursor.fetchone()

    except sqlite3.Error as e:
        print(e)
        return []
    finally:
        if conn:
            conn.close()
    
    return row


def insert_into_db(filename, name, date, time):

    conn = None
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()

        # Insert data into the table
        cursor.execute("INSERT INTO hbsm_entries (name, date, time) VALUES (?, ?, ?)", (name, date, time))
        conn.commit()

        print(f"Data inserted successfully.")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_db("my.db")

