<%@ Language = "VBScript" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form id="calAge" action="CalAge.asp">
        <label for="chk" >AGE</label>
        <input type="number" id="Age"  required="">

      
        <button type="submit">cala</button>
    </form>
<%
Age= Request.QueryString("Age")
age=CInt(Age)
DateBIRTH=1403-age
Response.write "<p> "&DateBIRTH&" </p>"




%>

</body>
</html>