import cv2
import pickle
import numpy as np

with open("men_women_model.pkl", "rb") as file:
    model = pickle.load(file)

classes = ['Men', 'Women']
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(rgb_frame, (224, 224))
    normalized = resized.astype(np.float32) / 255.0
    input_data = np.expand_dims(normalized, axis=0)

    predictions = model.predict(input_data, verbose=0)[0]
    class_idx = np.argmax(predictions)
    confidence = predictions[class_idx] * 100
    label = f"{classes[class_idx]}: {confidence:.1f}%"

    color = (255, 0, 0) if class_idx == 0 else (203, 192, 255)
    cv2.putText(frame, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    cv2.imshow('Men / Women Classifier', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
