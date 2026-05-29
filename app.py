import streamlit as st

st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💌"
)

st.title("💌 연애 코칭 앱")
st.write("연애 고민을 입력하면 조언을 해드립니다.")

user_input = st.text_area(
    "고민 입력",
    placeholder="예: 좋아하는 사람이 있는데 연락을 먼저 해야 할지 모르겠어요."
)

if st.button("조언 받기"):

    if user_input.strip() == "":
        st.warning("고민을 입력해주세요.")
    else:

        # 아주 단순한 기본 코칭 로직
        if "연락" in user_input:
            answer = """
            너무 부담스럽지 않게 짧고 편하게 연락해보세요.
            상대 반응을 천천히 보는 게 중요합니다.
            """

        elif "고백" in user_input:
            answer = """
            상대와 충분히 친밀감이 생겼는지 먼저 확인해보세요.
            급하게 하기보다 자연스러운 분위기가 좋아요.
            """

        elif "싸움" in user_input:
            answer = """
            감정이 격할 때 바로 해결하려 하지 말고,
            조금 진정된 뒤 차분하게 대화해보세요.
            """

        else:
            answer = """
            상대방 마음을 너무 단정하지 말고,
            자신의 감정도 건강하게 챙기는 게 중요해요.
            """

        st.success("코칭 결과")
        st.write(answer)
