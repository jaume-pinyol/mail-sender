import pymysql

REGION = "eu-west-1"
rds_host = ""  # This should be passed as env var
db_name = ""  # This should be passed as env var
user = "user"  # This should be passed as env var
password = "password"  # This should be passed as secret


def get_rows():
    conn = pymysql.connect(host=rds_host, user=user, passwd=password, db=db_name, connect_timeout=5)
    rows = []
    with conn.cursor() as cursor:
        cursor.execute("select * from db")
        conn.commit()
        cursor.close()
        for row in cursor:
            rows.append(list(row))

    return rows


def send_email(row):
    return


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    """

    for row in get_rows():
        send_email(row)
