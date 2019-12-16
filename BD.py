import mysql.connector
from mysql.connector import Error

class BD:
    def __init__(self):
        pass
    
    def setJugadores(self, ganador, jugadores):
        yeah=jugadores
        print (jugadores)
        print (yeah)
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='oca',
                                                user='root',
                                                password='')
            if connection.is_connected():
                aux=len(yeah)
                for i in range(aux):
                    if yeah[i]==ganador:
                        sql_select_Query = "select * from puntuaciones where jugador ='"+ganador+"'"
                        cursor = connection.cursor()
                        cursor.execute(sql_select_Query)
                        records = cursor.fetchall()
                        print (records)

                        if records == []:
                            mySql_insert_query = "INSERT INTO `oca`.`puntuaciones` (`jugador`, `puntos`, `juegos`) VALUES ('"+ganador+"', 1, 1);"
                            cursor = connection.cursor()
                            cursor.execute(mySql_insert_query)
                            connection.commit()
                            print(cursor.rowcount, "jugador insertado owo")
                            cursor.close()

                        else:
                            juegos = records[0][3]+1
                            puntos = records[0][2]+1
                            print (puntos,juegos)
                            mySql_insert_query = "UPDATE `oca`.`puntuaciones` SET `puntos` = "+str(puntos)+", `juegos` = "+str(juegos)+" WHERE (`jugador` = '"+ganador+"');"
                            cursor = connection.cursor()
                            cursor.execute(mySql_insert_query)
                            connection.commit()
                            print(cursor.rowcount, "jugador actualizado owo")
                            cursor.close()
                    else:
                        ayuda=yeah[i]
                        sql_select_Query = "select * from puntuaciones where jugador ='" + ayuda + "'"
                        cursor = connection.cursor()
                        cursor.execute(sql_select_Query)
                        records = cursor.fetchall()
                        print (records)

                        if records == []:
                            mySql_insert_query = "INSERT INTO `oca`.`puntuaciones` (`jugador`, `puntos`, `juegos`) VALUES ('" + ayuda + "', 0, 0);"
                            cursor = connection.cursor()
                            cursor.execute(mySql_insert_query)
                            connection.commit()
                            print(cursor.rowcount, "jugador insertado owo")
                            cursor.close()

                        else:
                            juegos = records[0][3] + 1
                            puntos = records[0][2]
                            print (puntos, juegos)
                            mySql_insert_query = "UPDATE `oca`.`puntuaciones` SET `puntos` = " + str(
                                puntos) + ", `juegos` = " + str(juegos) + " WHERE (`jugador` = '" + ayuda + "');"
                            cursor = connection.cursor()
                            cursor.execute(mySql_insert_query)
                            connection.commit()
                            print(cursor.rowcount, "jugador actualizado owo")


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

        sql_select_Query = "select * from puntuaciones order by puntos DESC"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        arreglo = []
        arreglonombres = []
        pos = []
        puntos = 0
        personas = 0
        arreglonombres = records

        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Puntos  = ", row[2])
            print("Juegos  = ", row[3])
        for row in records:
            nombre=row[1]
            personas+=1
            puntos=row[2]
            juegos = row[3]
           
            for row in arreglonombres:
                aux=0
                if nombre==row[2]:
                    puntos+=1
            arreglo.append([nombre,puntos,juegos])
        print(records)
        return arreglo

    #setJugadores(1,'pidi',['ayuda', 'pitote', 'pidi', 'nose'])