import streamlit as st
import pandas as pd
import plotly.express as px
import re

# 페이지 설정
st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

st.title("📊 Enterprise Data Visualization Tool")
st.markdown("Raw Data(Excel/CSV)를 업로드하면 즉시 시각화 리포트를 생성합니다.")

# 1. 파일 업로드 섹션
uploaded_file = st.file_uploader("데이터 파일을 업로드하세요", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # 2. 데이터 로드 및 전처리
    @st.cache_data
    def load_data(file):
        try:
            if file.name.endswith('csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
        except:
            df = pd.read_csv(file, encoding='cp949') # 한글 인코딩 대응

        # 컬럼명 영문 변환 (필요시 매핑 수정)
        col_map = {
            '제목': 'Title', '작업 상태': 'Status', '원본 언어': 'Source_Language',
            '번역 언어': 'Target_Language', '내보내기 생성일': 'Created_Date',
            '원본 영상 길이': 'Duration_Str', '사용자 Seq': 'User_ID'
        }
        df = df.rename(columns=col_map)

        # 날짜/시간 파싱
        df['Created_Date'] = pd.to_datetime(df['Created_Date'], errors='coerce')
        df['Date'] = df['Created_Date'].dt.date
        df['Hour'] = df['Created_Date'].dt.hour

        # 영상 길이(문자열) -> 분(Minute) 변환
        def parse_dur(x):
            if pd.isna(x): return 0
            x = str(x)
            m = re.search(r'(\d+)분', x)
            s = re.search(r'(\d+)초', x)
            return (int(m.group(1)) if m else 0) + (int(s.group(1))/60 if s else 0)

        df['Duration_Min'] = df['Duration_Str'].apply(parse_dur)
        return df

    df = load_data(uploaded_file)
    st.success(f"✅ 데이터 로드 성공! 총 {len(df):,}건의 작업 내역이 확인되었습니다.")

    # 3. 대시보드 레이아웃

    # [KPI 지표]
    c1, c2, c3 = st.columns(3)
    c1.metric("총 작업 건수", f"{len(df):,}")
    c2.metric("평균 영상 길이", f"{df['Duration_Min'].mean():.1f}분")
    c3.metric("가장 인기있는 언어", df['Source_Language'].mode()[0])

    st.divider()

    # [차트 섹션]
    tab1, tab2, tab3 = st.tabs(["📈 트렌드 분석", "🌍 언어 분포", "⏱️ 시간대 패턴"])

    with tab1:
        st.subheader("일별 작업량 추이")
        daily = df.groupby('Date').size().reset_index(name='Jobs')
        fig_trend = px.line(daily, x='Date', y='Jobs', markers=True)
        st.plotly_chart(fig_trend, use_container_width=True)

    with tab2:
        st.subheader("소스 언어 vs 타겟 언어")
        col_a, col_b = st.columns(2)
        with col_a:
            top_src = df['Source_Language'].value_counts().head(5)
            fig_src = px.bar(x=top_src.index, y=top_src.values, title="Top 5 원본 언어")
            st.plotly_chart(fig_src, use_container_width=True)
        with col_b:
            top_tgt = df['Target_Language'].value_counts().head(5)
            fig_tgt = px.pie(values=top_tgt.values, names=top_tgt.index, title="Top 5 번역 언어")
            st.plotly_chart(fig_tgt, use_container_width=True)

    with tab3:
        st.subheader("시간대별 활동 히트맵")
        heatmap_data = df.pivot_table(index=df['Created_Date'].dt.day_name(), columns='Hour', values='User_ID', aggfunc='count', fill_value=0)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_data = heatmap_data.reindex(days)
        fig_heat = px.imshow(heatmap_data, aspect='auto', color_continuous_scale='RdBu_r')
        st.plotly_chart(fig_heat, use_container_width=True)

    # 4. 데이터 다운로드
    st.markdown("### 📥 분석 데이터 다운로드")
    st.download_button("CSV로 내려받기", df.to_csv(index=False).encode('utf-8-sig'), "cleaned_data.csv")
