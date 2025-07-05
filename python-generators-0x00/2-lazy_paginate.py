def paginate_users(page_size, offset):
    from seed import connect_to_prodev
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def lazy_pagination(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
