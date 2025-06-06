# TMDb API를 활용한 한국영화 메타데이터 수집 스크립트

import requests
import pandas as pd
import time
from google.colab import files

# 수집 연도 설정
collect_year = 2021

# TMDb API 설정
API_KEY = 'e5173679a9900e5ec21696cd293f39e2'
BASE_URL = 'https://api.themoviedb.org/3'

# 영화 수집 ( 한국영화 대상 )
def get_korean_movies(year, total_pages=100):
    all_movies = []
    for page in range(1, total_pages + 1):
        print(f"🔄 [{year}] 페이지 수집 중: {page}")
        url = f"{BASE_URL}/discover/movie"
        params = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'region': 'KR',
            'sort_by': 'primary_release_date.asc',
            'include_adult': False,
            'include_video': False,
            'primary_release_year': year,
            'with_original_language': 'ko',
            'page': page
        }
        res = requests.get(url, params=params).json()
        movies = res.get("results", [])
        if not movies:
            break
        all_movies += movies
        time.sleep(0.5)
    return all_movies

# 상세 정보 수집
def get_movie_full_details(movie_id):
    details_url = f"{BASE_URL}/movie/{movie_id}"
    credits_url = f"{BASE_URL}/movie/{movie_id}/credits"

    details = requests.get(details_url, params={'api_key': API_KEY, 'language': 'ko-KR'}).json()
    credits = requests.get(credits_url, params={'api_key': API_KEY, 'language': 'ko-KR'}).json()
    time.sleep(0.5)

    director = next((c['name'] for c in credits.get('crew', []) if c['job'] == 'Director'), None)
    cast_list = [c['name'] for c in credits.get('cast', [])[:4]]

    return {
        '영화 ID': details.get('id'),
        '제목': details.get('title'),
        '원제': details.get('original_title'),
        '개봉일': details.get('release_date'),
        '줄거리': details.get('overview'),
        '장르': ', '.join([g['name'] for g in details.get('genres', [])]),
        '국가': ', '.join([c['name'] for c in details.get('production_countries', [])]),
        '제작사': ', '.join([p['name'] for p in details.get('production_companies', [])]),
        '포스터 URL': f"https://image.tmdb.org/t/p/w500{details.get('poster_path')}" if details.get('poster_path') else None,
        '러닝타임': details.get('runtime'),
        '평점': details.get('vote_average'),
        '투표수': details.get('vote_count'),
        '인기도': details.get('popularity'),
        '감독': director,
        '주연': ', '.join(cast_list)
    }

# 실행
raw_movies = get_korean_movies(collect_year, total_pages=100)
unique_movies = {movie['id']: movie for movie in raw_movies}.values()

results = []
for movie in unique_movies:
    print(f"🎬 [{collect_year}] 상세 정보 수집 중: {movie['title']}")
    try:
        details = get_movie_full_details(movie['id'])
        results.append(details)
    except Exception as e:
        print(f"⚠️ 오류 발생: {movie['title']} / {e}")

# 저장
file_name = f"tmdb_korean_movies_{collect_year}.csv"
df = pd.DataFrame(results)
df.to_csv(file_name, index=False, encoding="utf-8-sig")
files.download(file_name)
