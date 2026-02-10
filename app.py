import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="YDS 100 Soru Bankası", page_icon="🎓", layout="centered")

# 2. Soru Havuzu (Senin PDF'lerinden Ayıklanan Tam 100 Soru)
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
        {"q": "If I ---- about the traffic jam, I would have taken the train instead of driving.", "a": ["had known", "knew", "know", "have known", "will know"], "c": "had known"},
        {"q": "The archeologists were surprised to find that the ancient ruins were ---- preserved.", "a": ["remarkably", "narrowly", "vaguely", "randomly", "silently"], "c": "remarkably"},
        {"q": "Psychologists emphasize that regular exercise is ---- beneficial for mental health as it is for physical health.", "a": ["as", "so", "more", "too", "much"], "c": "as"},
        {"q": "Many scientists are concerned that global temperatures will continue to ---- unless drastic measures are taken.", "a": ["rise", "fall", "stabilize", "decline", "fluctuate"], "c": "rise"},
        {"q": "The invention of the internet has had a profound ---- on how we consume information.", "a": ["impact", "neglect", "rejection", "denial", "suspension"], "c": "impact"},
        {"q": "---- the weather was extremely cold, they decided to go for a long walk in the park.", "a": ["Even though", "Because", "Unless", "As long as", "Once"], "c": "Even though"},
        {"q": "The government is considering ---- new taxes to fund the public health system.", "a": ["implementing", "ignoring", "cancelling", "avoiding", "refusing"], "c": "implementing"},
        {"q": "By next year, the team ---- the research project and published their findings.", "a": ["will have finished", "finished", "has finished", "is finishing", "had finished"], "c": "will have finished"},
        {"q": "It is essential that everyone ---- the rules to ensure the safety of the participants.", "a": ["follow", "follows", "followed", "will follow", "following"], "c": "follow"},
        {"q": "The new drug has been proven to be ---- effective in treating the disease in early trials.", "a": ["highly", "vaguely", "barely", "narrowly", "randomly"], "c": "highly"},
        {"q": "---- children are taught about environmental protection, the better their future will be.", "a": ["The earlier", "The earliest", "Early", "Earlier", "Too early"], "c": "The earlier"},
        {"q": "The building, ---- roof was damaged in the storm, is now being repaired.", "a": ["whose", "which", "where", "whom", "that"], "c": "whose"},
        {"q": "He ---- have left his umbrella on the bus, as he doesn't have it with him now.", "a": ["must", "should", "can't", "won't", "ought"], "c": "must"},
        {"q": "The company has decided to ---- the launch of its new product due to technical issues.", "a": ["postpone", "accelerate", "celebrate", "ignore", "dismiss"], "c": "postpone"},
        {"q": "---- the high cost of the tickets, the concert was completely sold out.", "a": ["Despite", "Because", "Unless", "As long as", "Once"], "c": "Despite"},
        {"q": "The teacher recommended that the students ---- more time practicing their speaking skills.", "a": ["spend", "spends", "spent", "will spend", "spending"], "c": "spend"},
        {"q": "Rarely ---- such a talented musician in our small town.", "a": ["do we see", "we see", "we have seen", "did we see", "we saw"], "c": "do we see"},
        {"q": "The research team is working hard to ---- a cure for the rare disease.", "a": ["discover", "avoid", "fail", "ignore", "cancel"], "c": "discover"},
        {"q": "The results of the survey were ---- than the researchers had expected.", "a": ["more encouraging", "encouraging", "as encouraging", "the most encouraging", "so encouraging"], "c": "more encouraging"},
        {"q": "---- you have any questions, please do not hesitate to contact us.", "a": ["Should", "Would", "Could", "Might", "Will"], "c": "Should"},
        {"q": "The city council is planning to ---- a new park in the center of the town.", "a": ["establish", "destroy", "ignore", "cancel", "avoid"], "c": "establish"},
        {"q": "She is ---- the most dedicated student I have ever taught in my career.", "a": ["by far", "nearly", "almost", "too", "so"], "c": "by far"},
        {"q": "The project was cancelled ---- the lack of sufficient funding from the government.", "a": ["due to", "instead of", "as well as", "rather than", "in addition to"], "c": "due to"},
        {"q": "If the team ---- more carefully, they would have avoided the mistakes.", "a": ["had planned", "planned", "plan", "have planned", "will plan"], "c": "had planned"},
        {"q": "The new library, ---- opened last week, has already attracted many visitors.", "a": ["which", "who", "whom", "whose", "where"], "c": "which"},
        {"q": "He is not only a great athlete ---- a very successful businessman.", "a": ["but also", "yet", "so", "than", "as"], "c": "but also"},
        {"q": "The students ---- for the exam for weeks before they finally took it.", "a": ["had been studying", "studied", "have been studying", "study", "are studying"], "c": "had been studying"},
        {"q": "---- of the many challenges, the team managed to complete the project on time.", "a": ["In spite", "Despite", "Because", "Unless", "Although"], "c": "In spite"},
        {"q": "The manager asked the employees ---- their reports by the end of the day.", "a": ["to submit", "submitting", "submit", "submitted", "to be submitted"], "c": "to submit"},
        {"q": "Technology has advanced so rapidly that it is hard to ---- with the latest trends.", "a": ["keep up", "take up", "give up", "look up", "break up"], "c": "keep up"},
        {"q": "The discovery of the new planet has ---- a lot of excitement among astronomers.", "a": ["generated", "ignored", "refused", "delayed", "dismissed"], "c": "generated"},
        {"q": "---- you work hard, you will be able to achieve your goals in life.", "a": ["If", "Unless", "Although", "Even if", "Whether"], "c": "If"},
        {"q": "The students were ---- excited about the field trip that they couldn't sleep.", "a": ["so", "such", "too", "very", "more"], "c": "so"},
        {"q": "He decided to ---- his job and travel around the world for a year.", "a": ["quit", "accept", "promote", "ignore", "continue"], "c": "quit"},
        {"q": "The company is ---- for a new marketing manager with at least five years of experience.", "a": ["looking", "working", "waiting", "asking", "calling"], "c": "looking"},
        {"q": "The information provided in the brochure was ---- and easy to understand.", "a": ["clear", "vague", "bare", "narrow", "random"], "c": "clear"},
        {"q": "---- we receive the final report, we cannot make a decision about the budget.", "a": ["Until", "While", "As soon as", "Once", "Before"], "c": "Until"},
        {"q": "The historical document, ---- was found in the attic, provides valuable information.", "a": ["which", "who", "whom", "whose", "where"], "c": "which"},
        {"q": "He ---- have been at the scene of the crime, as he was in another city at that time.", "a": ["can't", "must", "should", "might", "ought"], "c": "can't"},
        {"q": "The team worked ---- to finish the project before the deadline.", "a": ["tirelessly", "vaguely", "barely", "narrowly", "randomly"], "c": "tirelessly"},
        {"q": "---- some people enjoy the winter, others find the cold weather very difficult.", "a": ["While", "Because", "Unless", "If", "Provided that"], "c": "While"},
        {"q": "The company has decided to ---- its production capacity to meet the increasing demand.", "a": ["expand", "reduce", "ignore", "cancel", "fail"], "c": "expand"},
        {"q": "If I ---- more time, I would have visited more museums during my stay in Paris.", "a": ["had had", "had", "have", "have had", "will have"], "c": "had had"},
        {"q": "The results of the experiment were ---- than the scientists had predicted.", "a": ["more significant", "significant", "as significant", "the most significant", "so significant"], "c": "more significant"},
        {"q": "---- you are looking for a reliable car, you should consider this brand.", "a": ["If", "Unless", "Although", "Even if", "Whether"], "c": "If"},
        {"q": "The museum, ---- is located in the city center, is open every day except Monday.", "a": ["which", "who", "whom", "whose", "where"], "c": "which"},
        {"q": "He is ---- talented that he won the first prize in the national competition.", "a": ["so", "such", "too", "very", "more"], "c": "so"},
        {"q": "The students were asked to ---- their opinions on the current education system.", "a": ["express", "ignore", "refuse", "delay", "dismiss"], "c": "express"},
        {"q": "The new law is expected to have a ---- impact on the local economy.", "a": ["positive", "vague", "bare", "narrow", "random"], "c": "positive"},
        {"q": "---- the difficulty of the task, the team managed to complete it successfully.", "a": ["Despite", "Because", "Unless", "As long as", "Once"], "c": "Despite"},
        {"q": "The manager suggested that the meeting ---- until next Monday.", "a": ["be postponed", "postpones", "postponed", "will postpone", "postponing"], "c": "be postponed"},
        {"q": "Hardly ---- the train left the station when I realized I had forgotten my bag.", "a": ["had", "did", "was", "has", "is"], "c": "had"},
        {"q": "The company is looking for a way to ---- its carbon footprint.", "a": ["reduce", "increase", "ignore", "cancel", "avoid"], "c": "reduce"},
        {"q": "---- people are becoming more aware of the importance of recycling.", "a": ["More and more", "Less and less", "Few and few", "Many and many", "So and so"], "c": "More and more"},
        {"q": "The historical site, ---- was discovered last year, is now open to the public.", "a": ["which", "who", "whom", "whose", "where"], "c": "which"},
        {"q": "He is considered to be ---- most influential scientist of our time.", "a": ["the", "a", "an", "one", "some"], "c": "the"},
        {"q": "---- the internet has many advantages, it also has some serious drawbacks.", "a": ["While", "Because", "Unless", "If", "Provided that"], "c": "While"},
        {"q": "The team is confident that they ---- the project by the end of the year.", "a": ["will finish", "finished", "has finished", "is finishing", "had finished"], "c": "will finish"},
        {"q": "The book, ---- was written by a famous historian, became a bestseller.", "a": ["which", "who", "whom", "whose", "where"], "c": "which"},
        {"q": "He ---- have forgotten our meeting, otherwise he would have called by now.", "a": ["must", "should", "can't", "won't", "ought"], "c": "must"},
        {"q": "The students worked ---- to prepare for the final presentation.", "a": ["diligently", "vaguely", "barely", "narrowly", "randomly"], "c": "diligently"},
        {"q": "---- you need any help, do not hesitate to ask your teacher.", "a": ["If", "Unless", "Although", "Even if", "Whether"], "c": "If"},
        {"q": "The city, ---- population is growing rapidly, faces many challenges.", "a": ["whose", "which", "where", "whom", "that"], "c": "whose"},
        {"q": "He is ---- intelligent that he can solve complex problems in minutes.", "a": ["so", "such", "too", "very", "more"], "c": "so"},
        {"q": "The researchers are trying to ---- the causes of the mysterious phenomenon.", "a": ["determine", "ignore", "refuse", "delay", "dismiss"], "c": "determine"},
        {"q": "The new project is expected to ---- many job opportunities for local people.", "a": ["create", "destroy", "ignore", "cancel", "avoid"], "c": "create"},
        {"q": "---- the rain, the football match was not cancelled.", "a": ["Despite", "Because", "Unless", "As long as", "Once"], "c": "Despite"},
        {"q": "The manager insisted that everyone ---- on time for the meeting.", "a": ["be", "is", "was", "will be", "being"], "c": "be"},
        {"q": "No sooner ---- the sun risen than they started their long journey.", "a": ["had", "did", "was", "has", "is"], "c": "had"},
        {"q": "The company is trying to ---- its customer service standards.", "a": ["improve", "ignore", "reduce", "cancel", "avoid"], "c": "improve"},
        {"q": "---- people are opting for electric cars to reduce pollution.", "a": ["An increasing number of", "A decreasing number of", "Few", "Little", "Much"], "c": "An increasing number of"},
        {"q": "The ancient city, ---- ruins were found last month, is a major discovery.", "a": ["whose", "which", "where", "whom", "that"], "c": "whose"},
        {"q": "He is ---- talented musician that everyone was amazed by his performance.", "a": ["such a", "so", "too", "very", "more"], "c": "such a"},
        {"q": "The scientists are working hard to ---- a sustainable source of energy.", "a": ["develop", "ignore", "refuse", "delay", "dismiss"], "c": "develop"},
        {"q": "The new policy is intended to ---- economic growth in the region.", "a": ["boost", "ignore", "reduce", "cancel", "avoid"], "c": "boost"},
        {"q": "---- the lack of resources, the team managed to finish the project.", "a": ["Despite", "Because", "Unless", "As long as", "Once"], "c": "Despite"}
    ]
    random.shuffle(st.session_state.questions)

# 3. Uygulama Değişkenlerini Başlatma
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'score' not in st.session_state: st.session_state.score = 0

# 4. Arayüz
st.title("🇬🇧 YDS 100 Soru Bankası")
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
