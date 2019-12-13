import mysql.connector
from mysql.connector import Error

class BD:
    def __init__(self):
        pass
    
    def setJugadores(self, ganador):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='oca',
                                                user='root',
                                                password='')
            if connection.is_connected():
                
                mySql_insert_query = "INSERT INTO `oca`.`puntuaciones` (`jugador`, `puntos`) VALUES ('"+ganador+"', 1);"
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                print(cursor.rowcount, "jugador insertado owo")
                cursor.close()


        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def getPuntuaciones(self):

        connection = mysql.connector.connect(host='localhost',
                                            database='oca',
                                            user='root',
                                            password='')

        sql_select_Query = "select * from puntuaciones"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        arreglo = []
        arreglonombres = []
        pos=[]
        puntos=0
        personas=0
        arreglonombres=records

        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])

            print("Puntos  = ", row[2])
        for row in records:
            nombre=row[1]
            personas+=1
            puntos=0
           
            for row in arreglonombres:
                aux=0
                if nombre==row[1]:
                    puntos+=1
                
            
            arreglo.append([nombre,puntos])
        print(arreglo[:])

            



            
        return arreglo

     