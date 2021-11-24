# 2021 IT 서비스 공모전 개발
### 이지재감 - OCR을 활용한 영수증 인식을 통한 사무 자동화 프로그램
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
#### 엑셀 데이터와 영수증 이미지로부터 OCR기술을 이용하여 추출한 데이터를 비교해주는 자동화 프로그램입니다. 세부 기능은 아래와 같습니다.

1. 지역 내 공적 마스크 판매처와 현황을 마커로 표시해 줍니다.  
<img width="720" alt="mask-stores" src="https://user-images.githubusercontent.com/49309450/77252324-75794f00-6c96-11ea-82b2-c416455c3a5e.png">  

2. 30일 내에 확진자가 다녀간 동선을 주황색 마커로 표시해 줍니다. 다녀간 지 오래될 수록 색이 옅어집니다.  
<img width="720" alt="patients" src="https://user-images.githubusercontent.com/49309450/77252328-7b6f3000-6c96-11ea-9eba-15c120146062.png">  

3. 공적 마스크 판매처와 현황, 확진자 정보, 확진자 동선 정보 등을 주기적으로 **자동 업데이트**하고 확진자 동선이 업데이트될 시 **메일**로 수신 가능합니다.  

4. 지역 내 선별 진료소를 표시해줍니다.  
<img width="720" alt="hospitals" src="https://user-images.githubusercontent.com/49309450/77252331-7d38f380-6c96-11ea-91a6-2b2f4ffd6eb9.png">  

5. 확진자 동선을 GUI로 쉽고 빠르게 추가할 수 있습니다.  
<img width="720" alt="patient-admin" src="https://user-images.githubusercontent.com/49309450/77252326-79a56c80-6c96-11ea-87e3-e1108a22a4e2.png">  

---

# 가이드 라인

## 초기 설정
#### - 다운로드 및 패키지 설치
1. `git clone https://github.com/nero96in/coronamap_deploy.git` 로 다운로드
2. 가상환경 생성 및 활성화 후, `python -m pip install --upgrade pip` 로 pip 업그레이드
3. `pip install -r requirements.txt`로 필요한 패키지 설치

## 실행
#### - main.py 실행

