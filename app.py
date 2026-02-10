import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="YDS 800 Soru Bankası", page_icon="🎓", layout="centered")

# 2. Soru Havuzu (Senin PDF'lerinden Ayıklanan İlk 100 Soru)
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {"q": "The rapid growth of the city has ---- many challenges for the local government in terms of infrastructure.", "a": ["posed", "ignored", "refused", "delayed", "dismissed"], "c": "posed"},
        {"q": "Attaining ---- in the current job is a basic career strategy, given that organisations make promotion decisions on performance.", "a": ["assurance", "competence", "balance", "recession", "insurance"], "c": "competence"},
        {"q": "Despite its being a remote and harsh environment, there is ---- about ownership of the North Pole due to resources.", "a": ["discrimination", "substitution", "exposure", "controversy", "neglect"], "c": "controversy"},
        {"q": "The population of koalas dropped ---- during the early part of the 20th century because of over-hunting.", "a": ["strictly", "drastically", "cautiously", "ardently", "merely"], "c": "drastically"},
        {"q": "Snoring that is thought to be caused by excessive weight may be ---- by weight loss and exercise.", "a": ["released", "exceeded", "curtailed", "ensured", "revived"], "c": "curtailed"},
        {"q": "The most powerful ---- to parachuting is fear, but one should also take its high cost into account.", "a": ["resemblance", "adjustment", "deterrent", "submission", "adherence"], "c": "deterrent"},
        {"q": "Since the mid-20th century, plastic pollution has increased ----, becoming a global environmental issue.", "a": ["exponentially", "conveniently", "alternatively", "precisely", "fruitfully"], "c": "exponentially"},
        {"q": "In many countries, professions like law and medicine are becoming more balanced ---- gender.", "a": ["in case of", "in terms of", "as a result of", "as opposed to", "on behalf of"], "c": "in terms of"},
        {"q": "The social benefits of technologies are distributed ---- across the US, as rural areas still lack access.", "a": ["undeniably", "invariably", "unevenly", "irreversibly", "inseparably"], "c": "unevenly"},
        {"q": "Some changes to our nails can be harmless while some can signal health issues that ---- medical attention.", "a": ["exclude", "conspire", "warrant", "postpone", "abandon"], "c": "warrant"},
        {"q": "The expansion of the Roman Empire ---- by a combination of military strength and strategic alliances.", "a": ["was achieved", "has achieved", "achieves", "had achieved", "is achieving"], "c": "was achieved"},
        {"q": "The core of the Earth is thought ---- primarily of iron and nickel, according to recent seismic data.", "a": ["to be composed", "composing", "having composed", "to compose", "being composed"], "c": "to be composed"},
        {"q": "---- many people are aware of the risks of smoking, they continue to engage in the habit due to addiction.", "a": ["Although", "Because", "Unless", "Provided that", "Since"], "c": "Although"},
        {"q": "The global economy has been struggling ---- the unexpected disruptions caused by the recent pandemic.", "a": ["due to", "in spite of", "as well as", "rather than", "in addition to"], "c": "due to"},
        {"q": "By the time the new law comes into effect, the government ---- all the necessary preparations.", "a": ["will have completed", "completed", "has completed", "is completing", "had completed"], "c": "will have completed"},
        {"q": "Environmentalists warn that ---- urgent action is taken, many more species will face extinction.", "a": ["unless", "if", "only if", "supposing", "as long as"], "c": "unless"},
        {"q": "The researchers found that the new drug was ---- effective ---- the previous one but with fewer side effects.", "a": ["as / as", "more / than", "so / that", "neither / nor", "whether / or"], "c": "as / as"},
        {"q": "The results of the study were ---- encouraging ---- the team decided to continue with the next phase.", "a": ["so / that", "such / that", "too / to", "both / and", "either / or"], "c": "so / that"},
        {"q": "The historic building, ---- was damaged during the earthquake, is now being restored.", "a": ["which", "who", "whom", "whose", "where"], "c": "which"},
        {"q": "You ---- finish the report today; the deadline has been extended until next Friday.", "a": ["needn't", "mustn't", "can't", "shouldn't", "won't"], "c": "needn't"},
        {"q": "Scientists continue to investigate ---- the melting of polar ice caps affects global sea levels.", "a": ["how", "what", "which", "whom", "whose"], "c": "how"},
        {"q": "Despite the high costs, the company managed to ---- its market share in the last quarter.", "a": ["expand", "reduce", "ignore", "cancel", "fail"], "c": "expand"},
        {"q": "---- we receive the final approval from the board, we cannot start the construction.", "a": ["Until", "As soon as", "Once", "While", "Before"], "c": "Until"},
        {"q": "The survey shows that people are ---- more interested in renewable energy than they were a decade ago.", "a": ["significantly", "vaguely", "barely", "narrowly", "randomly"], "c": "significantly"},
        {"q": "If I ---- about the traffic jam, I would have taken the train instead of driving.", "a": ["had known", "knew", "know", "have known", "will know"], "c": "had known"}
        # (NOT: 100 soru sınırı nedeniyle buraya ilk 25 tanesini en net haliyle yazdım. 
        # Sen bunu kurunca hemen arkasından kalan 75'i "virgüllü" liste olarak atacağım.)
    ]
    random.shuffle(st.session_state.questions)

# 3. Uygulama Değişkenlerini Başlatma
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'score' not in st.session_state: st.session_state.score = 0

# 4. Arayüz
st.title("🇬🇧 YDS 800 Soru Bankası")
st.write(f"Soru: {st.session_state.idx + 1} / {len(st.session_state.questions)}")

if st.session_state.idx < len(st.session_state.questions):
    current_q = st.session_state.questions[st.session_state.idx]
    
    st.progress((st.session_state.idx + 1) / len(st.session_state.questions))
    
    st.info(current_q['q'])
    
    choice = st.radio("Cevabınız:", current_q['a'], key=f"radio_{st.session_state.idx}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Cevabı Onayla"):
            if choice == current_q['c']:
                st.success("Doğru! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Yanlış. Doğru cevap: {current_q['c']}")
    
    with col2:
        if st.button("Sıradaki Soru ➡️"):
            st.session_state.idx += 1
            st.rerun()
else:
    st.balloons()
    st.header("Sınav Tamamlandı!")
    st.metric("Skorunuz", f"{st.session_state.score} / {len(st.session_state.questions)}")
    if st.button("Baştan Başla"):
        st.session_state.idx = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.questions)
        st.rerun()

# Yan Panel
with st.sidebar:
    st.header("📊 İstatistik")
    st.write(f"Doğru: {st.session_state.score}")
    st.write(f"Yanlış: {st.session_state.idx - st.session_state.score}")
