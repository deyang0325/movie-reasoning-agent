# TMDb 한국 영화 수집기 (TMDb Korean Movie Collector)

이 프로젝트는 TMDb API를 활용하여 특정 연도에 개봉한 한국 영화의 메타데이터를 자동으로 수집하는 도구입니다.

---

## 주요 기능

- TMDb API 기반의 연도별 한국 영화 데이터 자동 수집
- 영화 제목, 원제, 개봉일, 장르, 국가, 줄거리, 감독, 주연 등 다양한 정보 포함
- 수집된 데이터를 CSV 형식으로 저장
- 연도 설정만으로 유동적으로 사용 가능

---

## 필요 환경

- Python 3.7 이상
- 설치 라이브러리: `requests`, `pandas`

### 설치 방법

```bash
pip install -r requirements.txt
```

---

## 사용 방법

1. `collect_tmdb.py` 파일에서 아래 변수 수정

```python
collect_year = 2024
```

2. 스크립트 실행

```bash
python collect_tmdb.py
```

3. 실행 후 `tmdb_korean_movies_2024.csv` 파일이 생성됩니다.

---

## 예시 출력

| 제목 | 개봉일 | 장르 | 감독 | 주연 |
|------|--------|------|--------|------|
| 파묘 | 2024-02-22 | 미스터리, 스릴러 | 장재현 | 김고은, 최민식 |

---

## 주의사항

- TMDb API Key가 필요합니다.  
  [TMDb 공식 사이트](https://developer.themoviedb.org/)에서 발급받아야 합니다.
- 본 프로젝트는 연구 및 비상업적 목적에 한하여 사용할 수 있습니다.

---

## 파일 구성

```
├── collect_tmdb.py          # 영화 데이터 수집 메인 스크립트
├── requirements.txt         # 필요 라이브러리 목록
├── README.md                # 프로젝트 설명서
└── tmdb_korean_movies_2024.csv   # 수집된 예시 데이터 파일 (출력 결과)
```