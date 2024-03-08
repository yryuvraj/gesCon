import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
fm = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
sw, sh = pyautogui.size()
while True:
    _, f = cam.read()
    f = cv2.flip(f, 1)
    rf = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    o = fm.process(rf)
    lp = o.multi_face_landmarks
    fh, fw, _ = f.shape
    if lp:
        l = lp[0].landmark
        for i, m in enumerate(l[474:478]):
            x = int(m.x * fw)
            y = int(m.y * fh)
            cv2.circle(f, (x, y), 3, (0, 255, 0))
            if i == 1:
                sx = sw * m.x
                sy = sh * m.y
                pyautogui.moveTo(sx, sy)
        left = [l[145], l[159]]
        for m in left:
            x = int(m.x * fw)
            y = int(m.y * fh)
            cv2.circle(f, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse', f)
    cv2.waitKey(1)
