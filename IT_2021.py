import json

import cv2
import requests
import sys
import re

import csv
import pandas as pd

import API_KEY
LIMIT_PX = 1024
LIMIT_BYTE = 1024 * 1024  # 1MB
LIMIT_BOX = 40

def main(image_path:str):
    if len(sys.argv) != 3:
        print("Please run with args: $ python example.py /path/to/image appkey")
    image_path, appkey = image_path, API_KEY.appkey

    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(image_path, appkey).json()
    outputdata = json.dumps(output, ensure_ascii=False,sort_keys=True, indent=2)
    #print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=False)))
    # 받은 데이터 array로 변환
    outputdata = json.loads(outputdata)

    for i in range(len(outputdata['result'])):
    #box 모양으로 잘라서 보여주기
      x = outputdata['result'][i]['boxes'][0][0]
      y = outputdata['result'][i]['boxes'][0][1]
      w =  (outputdata['result'][i]['boxes'][1][0] -  outputdata['result'][i]['boxes'][0][0])
      h =  (outputdata['result'][i]['boxes'][2][1] -  outputdata['result'][i]['boxes'][0][1])
   #원본 이미지
      org_image = cv2.imread('receipt.jpg')
   #자른 이미지
      img_trim = org_image[y:y+h, x:x+w]
   #자른 이미지 보여주기
      #cv2_imshow(img_trim)
      print_outputdata = outputdata['result'][i]['recognition_words'][0]
      #print(print_outputdata)
      if outputdata['result'][i]['recognition_words'][0] == '결제금액' or outputdata['result'][i]['recognition_words'][0] == '합계':
        sum = outputdata['result'][i + 1]['recognition_words'][0]
        sum_n = re.findall(r'\d+', sum)
        sum_num = ''.join(sum_n)
        print(sum_num)
      if outputdata['result'][i]['recognition_words'][0] == '결제일시':
        date = outputdata['result'][i + 1]['recognition_words'][0]+outputdata['result'][i + 2]['recognition_words'][0]+outputdata['result'][i + 3]['recognition_words'][0]
        date_n = re.findall(r'\d+',date)
        date_num = ''.join(date_n)
        print(date_num)
    return (date_num,sum_num)

def kakao_ocr_resize(image_path: str):
    """
    ocr detect/recognize api helper
    ocr api의 제약사항이 넘어서는 이미지는 요청 이전에 전처리가 필요.

    pixel 제약사항 초과: resize
    용량 제약사항 초과  : 다른 포맷으로 압축, 이미지 분할 등의 처리 필요. (예제에서 제공하지 않음)


    :param image_path: 이미지파일 경로
    :return:
    """
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        cv2.imwrite(image_path, image)

        return image_path
    return None


def kakao_ocr(image_path: str, appkey: str):
    """
    OCR api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode("receipt2.png", image)[1]
    data = jpeg_image.tobytes()

    return requests.post(API_URL, headers=headers, files={"image": data})

def readCsv(csv_path:str):
    f = pd.read_csv('IT_2.csv', encoding='euc-kr')
    print(f)
    print("\n")
    print(f.columns)
    print("\n")
    com = f[['날짜', '영수증번호', ' 상세내용 ', ' 지출 ']]
    print(com)
    print("\n")
    print(com.loc[0])
    print("\n")
    #f[f[' 지출 '].str.contains('24600')]

    # rdr = csv.reader(f)
    # for line in rdr:
    #     print(line)
    # f.close()


def getInput(sum_num,date_num,com):
    a = int(input("영수증 번호를 입력해주세요: "))

    # 엑셀 파일에서 영수증 번호 받아와서 비교하기
    for i in range(len(com)):
        data = com.loc[i]
        num = data[1]
        # print(num)
        # print(type(num))
        # print(data[1])
        # print(int(a))
        if num == a:
            # test_compare = f.loc[f['영수증번호'] == str(a)]
            # print(test_compare)
            print(data)
            print(data[3])
            date_sp = data[0].split('.')
            date_split = ''.join(date_sp)
            print(date_split)
            if data[3] == int(sum_num):
                if int(date_split)== int(date_num):
                    print("날짜와 금액이 모두 일치합니다!")

                else:
                    print("금액은 일치하나, 날짜가 일치하지 않습니다!")
            else:
                #print("금액이 일치하지 않습니다!")
                if int(date_split) == int(date_num):
                    print("날짜는 일치하나, 금액이 일치하지 않습니다!")

                else:
                    print("금액, 날짜 모두 일치하지 않습니다!")

        else:
            continue











if __name__ == "__main__":
    main()