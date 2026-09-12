import cv2
webcam = cv2.VideoCapture(0) #conexão com a webcam
detector = cv2.FaceDetectorYN.create(  
        "face_detection_yunet_2026may.onnx",        
        "", 
        (640, 480))
while True:
    ler = webcam.read() #lendo o frame capturado pela webcam
    boleano, resto = ler
    if boleano == True:
        condicao = cv2.waitKey(10)
        teste = detector.detect(resto, 1)
        conclusao, valores = teste
        try:
            for lista in valores:
                x = int(lista[0])
                y = int(lista[1])
                w = int(lista[2])
                h = int(lista[3])
                break
            cv2.rectangle(resto, (int(x), int(y)), (int(x) + int(w), int(y) + int(h)), (0, 255, 0), 2)
            cv2.imshow('Janela teste', resto)
            if condicao == ord('q'):
                break
        except Exception:
            print("O rosto não foi detectado!") 
            break       
    else:
        raise Exception("Não foi possivel ler sua imagem")
cv2.destroyAllWindows()



