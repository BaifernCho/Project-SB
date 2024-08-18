import pyodbc

# สตริงการเชื่อมต่อ
conn_str = (
    r'DRIVER={SQL Server};'  # ใช้ SQL Server Driver
    r'SERVER=(local)\SQLEXPRESS;'  # ชื่อเซิร์ฟเวอร์ที่ต้องการเชื่อมต่อ
    r'DATABASE=NewStock;'  # ระบุชื่อฐานข้อมูล
    r'Trusted_Connection=yes;'  # ใช้การเชื่อมต่อที่เชื่อถือได้ (Windows Authentication)
)

try:
    # สร้างการเชื่อมต่อ
    conn = pyodbc.connect(conn_str)
    print("เชื่อมต่อกับฐานข้อมูลสำเร็จ!")

    # สร้าง cursor เพื่อทำงานกับฐานข้อมูล
    cursor = conn.cursor()

    # รายชื่อตารางที่ต้องการดึงข้อมูล
    tables_to_query = ['Customer']

    # วนลูปผ่านแต่ละตารางที่ระบุ
    for table_name in tables_to_query:
        print(f"\n--- ข้อมูลจากตาราง: {table_name} ---")
        
        # คิวรีข้อมูลจากตารางที่ระบุ
        cursor.execute(f"SELECT * FROM {table_name}")
        
        # ดึงคอลัมน์ของตาราง
        columns = [column[0] for column in cursor.description]
        
        # แสดงผลคอลัมน์
        print("\t".join(columns))
        
        # แสดงผลข้อมูลในตาราง
        for row in cursor.fetchall():
            print("\t".join(str(value) for value in row))

except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
    

finally:
    # ปิดการเชื่อมต่อ
    conn.close()
