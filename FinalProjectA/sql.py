import sqlite3

def create_table():
    conn = sqlite3.connect('infosys_project.db')    
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='available_jobs'
    ''')
    if cursor.fetchone():
        conn.close()
        print("Table already exists ... ")
        return
    else:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS available_jobs (
                idx INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT NOT NULL,
                employer TEXT NOT NULL,
                salary TEXT,
                url TEXT
            )
        ''')
        print("Table created ... ")
        conn.commit()
        conn.close()

def insert_records(job_title, employer, salary, url):
    create_table()

    conn = sqlite3.connect('infosys_project.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM available_jobs WHERE (job_title = ? AND employer = ? AND url = ?)
    ''', (job_title, employer, url))

    if cursor.fetchone()[0] > 0:
        return
    
    cursor.execute('''
        INSERT INTO available_jobs (job_title, employer, salary, url)
        VALUES (?, ?, ?, ?) 
    ''', (job_title, employer, salary, url))

    conn.commit()
    conn.close()

    print(f"Job: {job_title} from {employer} added to the table ...")

insert_records('test_title2', 'test_employer', 'test_salary', 'test_url')
