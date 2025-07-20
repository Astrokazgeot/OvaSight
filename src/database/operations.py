from src.database.connection import create_connection

def insert_patient(name, age, bmi, prediction_result, ovulation_status):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO patient_records (name, age, bmi, prediction_result, ovulation_status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, age, bmi, prediction_result, ovulation_status))
        conn.commit()
        cursor.close()
        conn.close()

def get_all_patients():
    conn = create_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patient_records ORDER BY uploaded_at DESC")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results


def get_patient_by_id(patient_id: int):
    conn = create_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM patient_records WHERE id = %s"
        cursor.execute(query, (patient_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
