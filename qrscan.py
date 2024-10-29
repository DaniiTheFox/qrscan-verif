import mysql.connector
import cv2
import webbrowser

#connect SQL
cnx = mysql.connector.connect(user='daniis', password='passwd',host='127.0.0.1',database='qr_code',
			     charset='utf8mb4', collation='utf8mb4_general_ci');
# Initialize the cam
cap = cv2.VideoCapture(0);
detector = cv2.QRCodeDetector();

while True:
	_, img = cap.read();
	# detect and decode
	data, bbox, _ = detector.detectAndDecode(img);
	# test if qr exist>
	if data:
		a=data
		break;
	#cv2 display result
	cv2.imshow("QRCODEscanner", img)
	if cv2.waitKey(1) == ord("q"):
		break;

print (str(a));

mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM qr_codes WHERE QRCODEID='"+str(a)+"';")

myresult = mycursor.fetchall()

row_count = mycursor.rowcount;

print ("rows> " + str(row_count));

for x in myresult:
  print(x)

if row_count > 0:
	print ("ACCESS GRANTED");
else:
	print ("ACCESS DENIED");

cap.release();
cv2.destroyAllWindows();
