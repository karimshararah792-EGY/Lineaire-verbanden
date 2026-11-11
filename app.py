import streamlit as st

st.set_page_config(page_title="Lineaire Verbanden Coach", page_icon="📈", layout="centered")
st.markdown("""<style>.block-container{max-width:780px;padding-top:2rem}div.stButton>button{border-radius:12px}h1{font-size:2rem}</style>""", unsafe_allow_html=True)

Q = [
 dict(title="Richtingscoëfficiënt",context="Wat gebeurt er met de grafiek van y = 2x + 3, als de a verandert van 2 naar 4?",parts=[dict(prompt="Kies het juiste antwoord",options=["steiler","minder steil","verschuift"],correct="steiler",good="Goed! Als a groter wordt, dan stijgt de grafiek sneller.",retry="Juist! Goed hersteld",hint="Grotere a → steilere grafiek.",wrong="als a groter wordt, dan stijgt de grafiek sneller.")]),
 dict(title="Bakkerij De Korrel · Economie",context="Bakkerij De Korrel heeft totale kosten TK = 2q + 3. Hierbij is q het aantal broden (× 100) en TK de kosten in honderden euro. Door duurder meel stijgen de variabele kosten per broodeenheid van 2 naar 4.",parts=[dict(prompt="Hoe verandert de kostenlijn?",options=["wordt steiler","wordt minder steil","schuift omhoog"],correct="wordt steiler",good="De lijn wordt steiler. De vaste kosten blijven gelijk, dus het startpunt verandert niet.",hint="Kijk naar de verandering van 2q naar 4q. Verandert a of b?",wrong="de lijn wordt steiler; het startpunt blijft hetzelfde."),dict(prompt="Welk getal in de oorspronkelijke formule stelt de variabele kosten per eenheid voor?",options=["2","3","q"],correct="2",good="Het getal 2 voor q is de richtingscoëfficiënt en stelt de variabele kosten per eenheid voor.",hint="Bij TK = aq + b geeft a aan hoeveel de kosten toenemen als q met 1 stijgt.",wrong="het getal 2, de coëfficiënt van q (na de verandering wordt dit 4).")]),
 dict(title="Startgetal",context="Wat gebeurt er met de grafiek als y = 2x + 3 wordt veranderd naar y = 2x - 1?",parts=[dict(prompt="Kies het juiste antwoord",options=["omhoog","omlaag","steiler"],correct="omlaag",good="Klopt! Kleiner b → grafiek omlaag.",retry="Juist! De grafiek verschuift omlaag",hint="kijk wat er gebeurt als x = 0.",wrong="grafiek verschuift omlaag.")]),
 dict(title="Subsidie · Economie",context="De bakkerij krijgt een gemeentesubsidie die hoger is dan de huur. Daardoor verandert de kostenformule van TK = 2q + 3 naar TK = 2q - 1.",parts=[dict(prompt="Wat stelt het getal achter 2q voor?",options=["variabele kosten","vaste kosten (netto)","aantal broden"],correct="vaste kosten (netto)",good="Het startgetal geeft de vaste kosten weer, hier na verrekening van de subsidie.",hint="Welk bedrag blijft over als q = 0?",wrong="de vaste kosten, na verrekening van de subsidie."),dict(prompt="Wat betekent het economisch dat de lijn bij q = 0 onder nul begint?",options=["de bakkerij houdt bij nul productie geld over door de subsidie","de variabele kosten zijn negatief","de lijn is steiler"],correct="de bakkerij houdt bij nul productie geld over door de subsidie",good="Bij nul productie is TK = -1 (honderd euro): de subsidie is groter dan de vaste lasten. De lijn schuift 4 omlaag.",hint="Vul q = 0 in. Wat betekent een negatief bedrag aan netto kosten?",wrong="de subsidie is groter dan de vaste lasten; bij nul productie blijft er netto geld over.")]),
 dict(title="Dalende grafiek",context="Hoe ziet de grafiek van y = -2x + 4 eruit?",parts=[dict(prompt="Kies het juiste antwoord",options=["stijgend","dalend","horizontaal"],correct="dalend",good="Goed bezig! Een negatieve a betekent een dalende grafiek.",retry="Juist! Negatieve a betekent een dalende grafiek",hint="wat gebeurt er als x groter wordt?",wrong="dalende grafiek.")]),
 dict(title="Energiedrankjes · Economie",context="De vraag naar energiedrankjes in de schoolkantine is q = -2p + 4. Hierbij is p de prijs in euro en q de gevraagde hoeveelheid (× 100 blikjes per week).",parts=[dict(prompt="Waarom loopt deze lijn naar beneden?",options=["hogere prijs betekent minder vraag","hogere prijs betekent meer vraag","de vraag blijft gelijk"],correct="hogere prijs betekent minder vraag",good="De richtingscoëfficiënt is -2: als p stijgt, daalt q.",hint="Kijk naar het minteken voor 2p.",wrong="bij een hogere prijs neemt de gevraagde hoeveelheid af."),dict(prompt="Bij welke prijs koopt niemand meer een blikje? (vul het bedrag in euro in)",correct="2",good="Bij q = 0 geldt -2p + 4 = 0, dus p = €2.",hint="Niemand koopt iets als q = 0. Los dan 0 = -2p + 4 op.",wrong="€2.")]),
 dict(title="Evenwijdige lijnen",context="Kunnen de grafieken van y = 3x + 2 en y = 3x - 4 elkaar snijden?",parts=[dict(prompt="Kies het juiste antwoord",options=["ja","nee","ik weet niet"],correct="nee",good="Goed gezien! De grafieken zijn even steil (zelfde a), dus lopen ze parallel aan elkaar.",retry="Juist! Ze zijn parallel, dus geen snijpunt.",hint="Zijn ze even steil?",wrong="Nee. De grafieken zijn even steil (zelfde a), dus lopen ze parallel aan elkaar.")]),
 dict(title="Snijpunt: x-coördinaat",context="Snijpunt van y = 3x + 2 en y = -x + 10.",parts=[dict(prompt="Wat is de x-coördinaat van het snijpunt?",correct="2",good="Goed! Bij x = 2 hebben beide grafieken dezelfde y-waarde.",retry="Juist! Bij x = 2 hebben beide grafieken dezelfde y-waarde.",hint="Stel ze gelijk aan elkaar. Dus 3x + 2 = -x + 10.",wrong="x = 2.")]),
 dict(title="Snijpunt: y-coördinaat",context="Snijpunt van y = 3x + 2 en y = -x + 10.",parts=[dict(prompt="Wat is de y-coördinaat van het snijpunt?",correct="8",good="Goed! De coördinaten van het snijpunt zijn (2, 8)",retry="Juist! De coördinaten van het snijpunt zijn (2, 8)",hint="vul x = 2 in een van de formules, bijvoorbeeld in y = 3x + 2",wrong="y = 8.")]),
 dict(title="Schoolboekenmarkt · Economie",context="Op de markt voor tweedehands schoolboeken is het aanbod q = 3p + 2 en de vraag q = -p + 10, met p in euro en q in honderden boeken.",parts=[dict(prompt="Wat is de evenwichtsprijs? (in euro)",correct="2",good="De evenwichtsprijs is €2. Stel aanbod en vraag gelijk: 3p + 2 = -p + 10.",hint="Bij evenwicht zijn aanbod en vraag gelijk. Los 3p + 2 = -p + 10 op.",wrong="€2."),dict(prompt="Hoeveel boeken worden er dan verhandeld? (aantal boeken, niet in honderden)",correct="800",good="Er worden 800 boeken verhandeld: q = 8 betekent 8 × 100 boeken.",hint="Vul p = 2 in bij q = 3p + 2. Let op: q is in honderden boeken.",wrong="800 boeken."),dict(prompt="Wat valt je op als je dit vergelijkt met vraag 8 en 9?",options=["dezelfde berekening en hetzelfde snijpunt","andere richtingscoëfficiënten","er is geen snijpunt"],correct="dezelfde berekening en hetzelfde snijpunt",good="Het is dezelfde berekening: het snijpunt (2, 8) is nu het marktevenwicht.",hint="Vergelijk 3x + 2 = -x + 10 met 3p + 2 = -p + 10.",wrong="dezelfde berekening en hetzelfde snijpunt (2, 8), maar nu met economische betekenis.")])
]

def is_correct(value, expected):
    if value == expected: return True
    if not value: return False
    v = value.strip().lower().replace("€", "").replace("euro", "").replace("boeken", "").strip().replace(",", ".")
    if expected in ("2", "8", "800"):
        try: return float(v) == float(expected)
        except ValueError: return v == {"2":"twee","8":"acht"}.get(expected, "")
    return v == expected

for key, default in {"name":"", "started":False,"index":0,"part":0,"attempt":0,"outcomes":{},"feedback":None,"finished_part":False,"score":0}.items():
    if key not in st.session_state: st.session_state[key] = default

st.title("📈 Lineaire Verbanden Coach")
if not st.session_state.started:
    st.write("Welkom bij de uitdaging over lineaire grafieken! We onderzoeken hoe a en b invloed hebben in y = ax + b, en passen dit toe in de economie.")
    name = st.text_input("Wat is je naam?", value=st.session_state.name)
    if st.button("Start met oefenen", type="primary", disabled=not name.strip(), use_container_width=True):
        st.session_state.name = name.strip()
        st.session_state.started = True
        st.rerun()
elif st.session_state.index >= len(Q):
    st.success(f"Knap gewerkt, {st.session_state.name}! Je score is {st.session_state.score} van 10.")
    st.write("⭐ Terugblik. Je hebt geoefend met de steilheid (a), de verschuiving (b) en het bepalen van snijpunten.")
    st.write("Je hebt deze kennis ook toegepast op kosten, subsidies, vraag en marktevenwicht.")
    if st.button("Opnieuw oefenen", use_container_width=True):
        for k,v in {"started":False,"index":0,"part":0,"attempt":0,"outcomes":{},"feedback":None,"finished_part":False,"score":0}.items(): st.session_state[k]=v
        st.rerun()
else:
    i=st.session_state.index
    q=Q[i]
    j=st.session_state.part
    part=q["parts"][j]
    st.caption(f"Vraag {i+1} van 10 · {st.session_state.name}")
    st.progress(i/10)
    st.subheader(q["title"])
    st.write(q["context"])
    if len(q["parts"])>1: st.markdown(f"**Onderdeel {chr(97+j)} van {len(q['parts'])}**")
    st.markdown("**"+part["prompt"]+"**")
    if not st.session_state.finished_part:
        key=f"answer_{i}_{j}_{st.session_state.attempt}"
        if "options" in part:
            ans=st.radio("Kies je antwoord:", part["options"], index=None, key=key)
        else:
            ans=st.text_input("Vul je antwoord in:",key=key,placeholder="Typ een getal, bijvoorbeeld 2")
        if st.button("Controleer antwoord", type="primary", use_container_width=True,disabled=not ans):
            if is_correct(ans,part["correct"]):
                st.session_state.outcomes[(i,j)]=True
                msg=part.get("retry", "Juist! Goed hersteld. "+part["good"]) if st.session_state.attempt else part["good"]
                st.session_state.feedback=("success",msg)
                st.session_state.finished_part=True
            elif st.session_state.attempt==0:
                st.session_state.feedback=("warning","💡 Hint: "+part["hint"])
                st.session_state.attempt=1
            else:
                st.session_state.outcomes[(i,j)]=False
                st.session_state.feedback=("error","❌ Fout. Juiste antwoord: "+part["wrong"])
                st.session_state.finished_part=True
            st.rerun()
    if st.session_state.feedback:
        kind,msg=st.session_state.feedback
        getattr(st,kind)(msg)
    if st.session_state.finished_part:
        last=j==len(q["parts"])-1
        if st.button("Volgende vraag" if last else "Volgend onderdeel",use_container_width=True):
            if last:
                if all(st.session_state.outcomes.get((i,k),False) for k in range(len(q["parts"]))): st.session_state.score+=1
                st.session_state.index+=1
                st.session_state.part=0
            else: st.session_state.part+=1
            st.session_state.attempt=0
            st.session_state.feedback=None
            st.session_state.finished_part=False
            st.rerun()
