# 2021 IT 서비스 공모전 개발
### 이지재감 - OCR을 활용한 영수증 인식을 통한 사무 보조 프로그램
서울과학기술대학교 ITM학과 학생들이 IT 서비스 공모전 준비를 위해 개발한 프로그램 입니다.

### 사용한 API
1. [카카오 OCR API](https://vision-api.kakao.com/#ocr)

### 개발진
- **기획/프론트앤드 개발**: 김찬혁(ITM학과)  
- **기획/백엔드 개발**: 피유진(ITM학과)
- **기획/백엔드 개발**: 황유정(ITM학과)
- **기획**: 권대훈(ITM학과)
- 기타 문의: cksgur97@gmail.com

---

# 기능 설명
#### 엑셀 데이터와 영수증 이미지로부터 OCR기술을 이용하여 추출한 데이터를 비교해주는 보조 프로그램입니다. 세부 기능은 아래와 같습니다.

1. 처음 프로그램 실행시 화면은 아래와 같습니다.  
<img width="720" alt="mask-stores" src="https://user-images.githubusercontent.com/76461625/143190791-83adf3db-03ef-4027-b1c9-7863b66b0200.png">  

2. 먼저 엑셀파일을 올려줍니다. 해당 엑셀파일에서 필요한 데이터들만 불러옵니다.
<img width="720" alt="patients" src="https://user-images.githubusercontent.com/76461625/143190814-bf1c03e1-8404-4e60-b725-2f892b9e4fb0.png">  

3. 엑셀 불러오기가 끝나고 데이터 비교를 위해 영수증 이미지 파일을 불러옵니다.
<img width="720" alt="hospitals" src="https://user-images.githubusercontent.com/76461625/143190818-4d546e21-5d00-4170-b6b2-0b9f8c6e3165.png">  

4. 이미지 불러오기가 끝나고 해당 이미지로부터 결제 날짜와 결제 금액을 불러옵니다.   
<img width="720" alt="hospitals" src="https://user-images.githubusercontent.com/76461625/143190822-3b5b5e79-7229-4911-b30f-25b21986eb79.png">  

5. **Side Box**에서 영수증 번호를 입력하고 영수증 비교하기 버튼을 클릭시, 엑셀 데이터와 ocr데이터를 비교하게 되고 일치/불일치를 알림창으로 알려줍니다.  
<img width="720" alt="patient-admin" src="https://user-images.githubusercontent.com/76461625/143190826-36185463-2e65-4166-8016-3c5a73a5c0a0.png">  

---

# 가이드 라인

## 초기 설정
#### - 다운로드 및 패키지 설치
1. `git clone https://github.com/muhanmu2jo/IT_SERVICE.git` 로 다운로드
2. 가상환경 생성 및 활성화 후, `python -m pip install --upgrade pip` 로 pip 업그레이드
3. `pip install -r requirements.txt`로 필요한 패키지 설치

## 실행
#### - main.py 실행

