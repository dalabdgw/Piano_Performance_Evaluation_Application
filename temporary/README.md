# [**피아노 데이터 평가 및 수집 프로그램**]

### 본 리포지토리는DGU DAlab의 피아노 데이터 평가 및 수집 프로그램 소스 코드 입니다.
---
---

## 기술 스택

- **Frontend**  
  ![Flutter](https://img.shields.io/badge/flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)  ![Figma](https://img.shields.io/badge/-Figma-F24E1E?logo=figma&logoColor=white)

- **Backend**  
  ![flask](https://img.shields.io/badge/-flask-092E20?logo=flask&logoColor=white)  ![Swagger](https://img.shields.io/badge/-Swagger-85EA2D?logo=swagger&logoColor=black)  ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)

- **DevOps**  
  ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white)  ![AWS](https://img.shields.io/badge/-AWS-181717?logo=AWS&logoColor=white)  ![AWS](https://img.shields.io/badge/-EC2-181717?logo=EC2&logoColor=white)
---

## 서비스 소개

### [**기능 소개**]
- 본 서비스는 피아노 연주 데이터를 평가 받기 위해 업로드 및 관리
- 피아노 연주 데이터 재생 및 항목별 평가

---

## 주요 기능(상세)

- ### 회원가입 및 로그인
![로그인](.,/docs/img/login.PNG)

 처음 접속하면 위와 같은 **로그인 / 회원가입 화면**이 나타납니다.  
  사용 방법은 다음과 같이 아주 단순합니다.

  | 단계 | 화면 동작 |
  |------|-----------|
  | **1. 회원가입** | **회원가입** 버튼을 눌러<br>아이디·비밀번호·이름 등 기본 정보를 입력합니다. |
  | **2. 로그인** | 가입한 아이디/비밀번호를 입력하고 **시스템 로그인** 버튼을 클릭합니다. |
  | **3. 홈 화면 이동** | 인증이 완료되면 자동으로 홈(곡 목록) 화면으로 이동합니다.<br>여기서 곡을 선택해 **세그먼트 재생·평가** 기능을 바로 이용할 수 있습니다. |

  #### 입력 유효성 & 예외 처리
  - **아이디 중복 검사** : 아이디 입력란 옆에 “사용 가능 / 사용 중” 메시지가 바로 표시됩니다.  
  - **비밀번호 규칙**  : 영문·숫자 조합 8자 이상(특수문자 선택) — 규칙에 맞지 않으면 즉시 안내 문구가 뜹니다.  
  - **로그인 실패**   : 아이디 또는 비밀번호가 틀린 경우 상단에 오류 메시지가 표시됩니다.

  > 회원가입과 로그인을 마치면 별다른 추가 설정 없이<br>
  > **검색·세그먼트 재생·15개 항목 평가** 기능을 자유롭게 사용하실 수 있습니다.

- ### 회원가입
![이미지 에러](././docs/img/register.png)

- ### 음악 검색
![이미지 에러](./docs/img/search.PNG)
- ### 10초 단위의 데이터 평가
![이미지 에러](./docs/img/10s.PNG)
- ### 곡 악보 표시 및 재생
![이미지 에러](./docs/img/score.PNG)
- ### 15가지 항목을 기준으로 평가 지원
   - 톤, 레가토, 해석, 프레이징, 멜로디, 음악성(음악적표현력), 보이싱, 음정, 셈여림, 셈여림 변화, 템포, 템포의 변화, 음의 길이와 관련된 아티큘레이션, 리듬, 페달링
![이미지 에러](./docs/img/evaluation.PNG)
- 연주자 익명 평가 시스템
![이미지 에러](./docs/img/anonymous_evaluation.PNG)
- SQL을 통해 평가결과 내보내기

---

## 서비스 아키텍처

![서비스 아키텍처](./docs/img/service.PNG)

---


## 설치 및 실행 방법

1. 저장소 클론

```bash
git clone https://github.com/dalabdgw/Piano_Performance_Evaluation_Application.git
```

2. 프로젝트 디렉터리로 이동

```bash
cd Piano_Performance_Evaluation_Application
```

3. 파이썬 개발 환경 설정
```bash
python -m venv venv
pip install -r requirements.txt
```

4. 다트 개발 환경 설정
Flutter 개발 환경이 설정되어 있지 않다면, [Flutter 설치 가이드](https://dart-ko.dev/)를 참고하여 설치하세요.

```bash
flutter pub get
```

5. 파이썬 플라스크 서버 실행

```bash
python main.py
```


---

## CI/CD 구축 및 배포 방법(추가 예정)

aws ec2를 통한 배포 및 서비스 제공

빌드 오류를 낮추기 위해서 사용
```bash
flutter clean
```
빌드 오류를 낮추기 위해서 사용


```bash
flutter pub get
```
패키지 적용

```bash
flutter build
```
빌드 파일 생성


```bash
cd ./build/web
```

```bash
move web ./backend/templates
```


```bash
cd ./backend/templates
```

```bash
git --version
```
깃허브 버전 확인
- 실행이 안된다면 깃허브 설치 후 시도

```bash
git --version
```

```bash
git add .
```

혹은

```bash
git add 파일명.확장자
```

```bash
git commit -m "[docs] 배포 버전 업로드"
```
커밋 메시지 작성 시

'[작업 카테고리] 작업한 내용' 으로 작성


```bash
git remore -v
```
업스트림 확인 후

origin  https://github.com/dalabdgw/Piano_Performance_Evaluation_Application.git (fetch)
origin  https://github.com/dalabdgw/Piano_Performance_Evaluation_Application.git (push) 

으로 출력되는 경우

```bash
git push origin main
```
만약 업스트림이 다음이 아닌 경우

```bash
git remote add origin https://github.com/dalabdgw/Piano_Performance_Evaluation_Application.git
```
을 사용해서 업스트림 적용 후 업로드 진행

---

 - aws 보안 설명 및 서버 로그인 하는 방법

aws 콘솔 접속
 key.pem
키를 활용해서 윈도우 암호 획득

---
