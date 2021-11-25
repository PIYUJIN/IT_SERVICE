import json

import cv2
import requests
import sys
import re

import API_KEY
LIMIT_PX = 1024
LIMIT_BYTE = 1024 * 1024  # 1MB
LIMIT_BOX = 40


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

def main(image_path:str):
    if len(sys.argv) != 3:
        print("Please run with args: $ python example.py /path/to/image appkey")
    image_path, appkey = image_path, API_KEY.appkey

    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        # print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(image_path, appkey).json()
    outputdata = json.dumps(output, ensure_ascii=False,sort_keys=True, indent=2)
    #print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=False)))
    # 받은 데이터 array로 변환
    outputdata = json.loads(outputdata)

    #여기 ocr_result 배열 추가했습니다
    ocr_result = []

    #변수 초기화
    sum_num = '0'

    for i in range(len(outputdata['result'])):
    #box 모양으로 잘라서 보여주기
        x = outputdata['result'][i]['boxes'][0][0]
        y = outputdata['result'][i]['boxes'][0][1]
        w =  (outputdata['result'][i]['boxes'][1][0] -  outputdata['result'][i]['boxes'][0][0])
        h =  (outputdata['result'][i]['boxes'][2][1] -  outputdata['result'][i]['boxes'][0][1])

        print_outputdata = outputdata['result'][i]['recognition_words'][0]
        #print(print_outputdata)

        #print_outputdata 배열에 추가
        ocr_result.append(print_outputdata)


        if outputdata['result'][i]['recognition_words'][0] == '결제금액' or \
            outputdata['result'][i]['recognition_words'][0] == '결제금액:' or \
            outputdata['result'][i]['recognition_words'][0] == '-결제금액:' or \
            outputdata['result'][i]['recognition_words'][0] == '-결제무단:' or \
            outputdata['result'][i]['recognition_words'][0] == '합계':
            sum = outputdata['result'][i + 1]['recognition_words'][0]
            sum_n = re.findall(r'\d+', sum)
            sum_num = ''.join(sum_n)
            print(sum_num)



    p = re.compile(
        '((\d{4})|\d{2})?(-|/|.)?(?P<year>[1-9]|0[1-9]|1[0-2])(-|/|.|년 )?(?P<month>[1-9]|0[1-9]|1[0-2])(-|/|.|월 )(?P<date>([1-9]|0[1-9]|[1-2][0-9]|3[01]))일?$')
    # print(ocr_result)

    dateList = []
    for i in ocr_result:
        m = p.match(i)
        if m and ((1 if (int(m.group("date")) <= 28) else 0) if int(m.group("month")) == 2 else 1):
            date_n = re.findall(r'\d+', i)
            date_num_sum = ''.join(date_n)
            dateList.append(date_num_sum)
        else:
            continue
    date_num = dateList[0]
    print('날짜')
    print(date_num)

    return (date_num, sum_num)








if __name__ == "__main__":
    main("images/receipt4.png")

