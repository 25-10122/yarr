import streamlit as st
import pandas as pd

# 1. 간단한 영화 데이터 생성 (실제 앱에서는 CSV 파일이나 API를 연결할 수 있습니다)
movies = [
    {"title": "인셉션", "genre": "SF/액션", "description": "꿈속으로 들어가 생각을 훔치는 거대한 작전"},
    {"title": "어바웃 타임", "genre": "로맨틱 코미디", "description": "시간을 되돌릴 수 있다면 진정한 사랑을 찾을 수 있을까?"},
    {"title": "쇼생크 탈출", "genre": "드라마", "description": "희망은 사라지지 않는다, 감옥에서의 사투와 우정"},
    {"title": "너의 이름은.", "genre": "애니메이션/로맨스", "description": "꿈속에서 몸이 바뀐 소년과 소녀의 기적 같은 이야기"},
    {"title": "기생충", "genre": "스릴러/드라마", "description": "두 가족의 만남이 가져온 걷잡을 수 없는 사건"},
    {"title": "라라랜드", "genre": "뮤지컬/로맨스", "description": "꿈을 꾸는 사람들을 위한 별들의 도시"},
    {"title": "다크 나이트", "genre": "액션/히어로", "description": "고담시를 지키는 배트맨과 광기 어린 조커의 대결"},
]

# 2. 앱 제목 및 레이아웃
st.set_page_config(page_title="영화 추천기", page_icon="🎬")
st.title("🎬 취향 저격 영화 추천 앱")
st.write("당신이 좋아하는 장르를 알려주시면 영화를 추천해 드려요!")

# 3. 사용자 입력 (사이드바 또는 메인 화면)
st.sidebar.header("설정")
selected_genre = st.sidebar.selectbox(
    "어떤 장르를 좋아하시나요?",
    ["전체", "SF/액션", "로맨틱 코미디", "드라마", "애니메이션/로맨스", "스릴러/드라마", "뮤지컬/로맨스", "액션/히어로"]
)

# 4. 추천 로직
st.subheader(f"📍 '{selected_genre}' 관련 추천 결과")

if selected_genre == "전체":
    recommended_movies = movies
else:
    recommended_movies = [m for m in movies if selected_genre in m["genre"]]

# 5. 결과 출력
if recommended_movies:
    for movie in recommended_movies:
        with st.container():
            st.markdown(f"### {movie['title']}")
            st.caption(f"장르: {movie['genre']}")
            st.write(movie['description'])
            st.divider()
else:
    st.warning("아쉽게도 해당 장르의 추천 영화가 아직 없어요!")

# 6. 추가 기능 (버튼 클릭 시 랜덤 추천)
if st.button("아무거나 하나만 골라줘!"):
    import random
    lucky_movie = random.choice(movies)
    st.balloons()
    st.info(f"오늘의 추천 영화는 바로... **[{lucky_movie['title']}]** 입니다!")
