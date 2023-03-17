import mysql.connector
from flask import make_response, abort


def read_node_status():

    conn = mysql.connector.connect(
        host='34.87.52.98',
        user='root',
        passwd='QCS\B5/_?]ycS7Id',
        database='mycare'
    )
    node_status =[]
    c = conn.cursor()
    c.execute(
        'SELECT * FROM mycare_backend_sensorinfo')
    results = c.fetchall()

    for result in results:
        node_status.append({'1': result[0], '2': result[1], 'status': result[2]})

    conn.close()
    return results

