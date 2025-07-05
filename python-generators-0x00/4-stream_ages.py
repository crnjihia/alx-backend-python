def stream_user_ages():
    from seed import connect_to_prodev
    conn = connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age
    cursor.close()
    conn.close()

def calculate_average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    print(f"Average age of users: {total / count if count else 0}")
