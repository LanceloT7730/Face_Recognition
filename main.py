from deepface import DeepFace
import json

def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        with open('result.json', 'w') as file:
            json.dump(result_dict, indent=4, ensure_ascii=False)

        # return result_dict

        if result_dict.get('verified'):
            return 'Check passed. Skip'
        return 'Violator! Detain!!!'

    except Exception as _ex:
        return _ex

def face_recogn():
    try:
        result = DeepFace.find(img_path='faces/downey1.jpg.jpg', db_path='Emilia')
        result = result.values.tolist()
        return result

    except Exception as _ex:
        return _ex

def main():
    #print(face_verify(img_1='faces/em1.jpg', img_2='faces/snoop.jpg'))
    #print(face_recogn())
    print('Hello world!')

if __name__ == '__main__':
    main()