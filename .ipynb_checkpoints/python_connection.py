import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

# =============================================
# STEP 1: APNI DETAILS YAHAN BHARO
# =============================================
DB_USER     = "root"           # MySQL username
DB_PASSWORD = "root"  # MySQL password
DB_HOST     = "localhost"
DB_NAME     = "hr_analysis"
CSV_PATH    = r"C:\Users\Sistech Computer\Downloads\emp_attrition.csv"  # CSV ka path

# =============================================
# STEP 2: DATABASE BANAO (agar nahi bana)
# =============================================
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
print(f"✅ Database '{DB_NAME}' ready!")
conn.close()

# =============================================
# STEP 3: CSV LOAD KARO
# =============================================
df = pd.read_csv(CSV_PATH)
print(f"✅ CSV loaded! Total Rows: {len(df)}, Total Columns: {len(df.columns)}")
print(df.head(2))

# =============================================
# STEP 4: MYSQL MEIN DATA IMPORT KARO
# =============================================
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

df.to_sql("hr_attrition", con=engine, if_exists="replace", index=False)

print(f"✅ {len(df)} rows successfully imported into MySQL!")