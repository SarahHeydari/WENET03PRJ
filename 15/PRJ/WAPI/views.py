import sqlite3
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt 
def AddPoint(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            x = data.get('x')
            y = data.get('y')
            

            if  not x or not y:
                return JsonResponse({"error": "x and y are required."}, status=400)
            

            # Set the path to DB
            Path = r'E:/Master/Network/15/appDB.db'  

            # Connect to DB
            connection = sqlite3.connect(Path)
            cursor = connection.cursor()

            # Insert X,Y into the 'points' table
            cursor.execute('''
                INSERT into points (x, y)
                VALUES (?, ?)
            ''', (x, y))

            # Commit  and close
            connection.commit()
            connection.close()

            return JsonResponse({
                "point": {
                    "x": x,
                    "y": y,
                }
            })

        except sqlite3.Error as e:
            # Handle DB errors
            return JsonResponse({"error": f"Database error: {e}"}, status=500)
        except json.JSONDecodeError:
            # Handle JSON errors
            return JsonResponse({"error": "Invalid JSON."}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)


@csrf_exempt 
def CountPoint(request):
    if request.method == 'GET':
        try:

            # Set the path to DB
            Path = r'E:/Master/Network/15/appDB.db'

            # Connect to DB
            connection = sqlite3.connect(Path)
            cursor = connection.cursor()

            # Retrieve the user by email
            cursor.execute('select count(id) from points')
            point = cursor.fetchone()

            # If the user does not exist
            if not point:
                return JsonResponse({"error": "point not found."}, status=404)

            # The stored hashed password from the database
            p_num = point[0]  # number of points stored in first col
            

            # Check if the provided password matches the stored hashed password
            if p_num:
                return JsonResponse({
                    "numberPoints": p_num
                })
            else:
                #it doesnt make sense but i did it like others
                return JsonResponse({"error": "there is an error in stored number"} , status=401) 

        except sqlite3.Error as e:
            # Handle DB errors
            return JsonResponse({"error": f"Database error: {e}"}, status=500)
        except json.JSONDecodeError:
            # Handle JSON decode errors
            return JsonResponse({"error": "Invalid JSON."}, status=400)

    return JsonResponse({"error": "Only GET requests are allowed."}, status=405)
