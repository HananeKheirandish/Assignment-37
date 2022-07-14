import cv2
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()

    if ret == False:
        break

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        x, y, w, h = cv2.boundingRect(bbox[0])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 6)
        cv2.putText(frame, data, (x+30, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 3)

        if cv2.waitKey(1) == ord("a"):
            webbrowser.open(str(data))
    
    cv2.imshow("QRCODEscanner", frame)

    if cv2.waitKey(1) == ord("q"):
	    break

cap.release()
cv2.destroyAllWindows()