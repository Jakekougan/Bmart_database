FOR THE extra credit Data Analysis stuff


"""def check_store_time(state, day_of_week, time ):
    cnx = get_connection()
    
    if cnx is None or not cnx.is_connected():
        raise ValueError("failed to connected to the database")
    
    try:
        with cnx.cursor() as cursor:
            time_query = "Select store_num, city, state, opening_time, closing_time FROM hrs_operating" \
            "JOIN store ON hrs_operating.store_num = store.store_num WHERE store.store = %s" 
            "AND hrs_operating.days_of_week = %s AND opening_time <= AND closing_time >= %s"
            cursor.execute(time_query, (state, day_of_week, time, time))

            stores_opened = cursor.fetchall()

            if stores_opened:

                print(blah blah )
            
            else:
                print("no stores are open during the time and date requested")"""


