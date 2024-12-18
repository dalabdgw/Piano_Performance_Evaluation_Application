# [**피아노 데이터 평가 및 수집 프로그램**]

### 본 리포지토리는DGU DAlab의 피아노 데이터 평가 및 수집 프로그램 소스 코드 입니다.
---
---

## 기술 스택

- **Frontend**  
  ![Flutter](https://img.shields.io/badge/flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)  ![Figma](https://img.shields.io/badge/-Figma-F24E1E?logo=figma&logoColor=white)

- **Backend**  
  ![flask](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white)  ![Swagger](https://img.shields.io/badge/-Swagger-85EA2D?logo=swagger&logoColor=black)  ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)

- **DevOps**  
  ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white)
---

## 서비스 소개

### [**기능 소개**]
- 본 서비스는 피아노 연주 데이터를 평가 받기 위해 업로드 및 관리
- 피아노 연주 데이터 재생 및 항목별 평가

---

## 주요 기능

- 10초 단위의 데이터 평가
- 15가지 항목을 기준으로 평가 지원
- 연주자 익명 평가 시스템
- .CSV형태로의 파일 내보내기 기능

---

## 서비스 아키텍처

![서비스 아키텍처(추가 예정)](./System_Architecture.png)

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

---

## 유지보수 안내 사항



