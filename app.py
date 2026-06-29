import streamlit as st
import os

# ကျောနံပါတ် 1 မှ 11 အထိ ကစားသမား Data များ (နိုင်ငံ ဒေတာ ထပ်ဖြည့်ထားသည်)
players_db = {
    "1": {
        "name": "Alisson Becker",
        "team": "Liverpool",
        "country": "Brazil 🇧🇷",
        "position": "Goalkeeper",
        "age": 33,
        "photo": "images/alisson.jpg"
    },
    "2": {
        "name": "Achraf Hakimi",
        "team": "PSG",
        "country": "Morocco 🇲🇦",
        "position": "Defender (Right Back)",
        "age": 27,
        "photo": "images/hakimi.jpg"
    },
    "3": {
        "name": "Ruben Dias",
        "team": "Manchester City",
        "country": "Portugal 🇵🇹",
        "position": "Defender (Center Back)",
        "age": 29,
        "photo": "images/dias.jpg"
    },
    "4": {
        "name": "Virgil van Dijk",
        "team": "Liverpool",
        "country": "Netherlands 🇳🇱",
        "position": "Defender (Center Back)",
        "age": 34,
        "photo": "images/vandijk.jpg"
    },
    "5": {
        "name": "Jude Bellingham",
        "team": "Real Madrid",
        "country": "England 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "position": "Midfielder",
        "age": 22,
        "photo": "images/bellingham.jpg"
    },
    "6": {
        "name": "Joshua Kimmich",
        "team": "Bayern Munich",
        "country": "Germany 🇩🇪",
        "position": "Midfielder",
        "age": 31,
        "photo": "images/kimmich.jpg"
    },
    "7": {
        "name": "Cristiano Ronaldo",
        "team": "Al Nassr",
        "country": "Portugal 🇵🇹",
        "position": "Forward",
        "age": 41,
        "photo": "images/ronaldo.jpg"
    },
    "8": {
        "name": "Martin Odegaard",
        "team": "Arsenal",
        "country": "Norway 🇳🇴",
        "position": "Midfielder",
        "age": 27,
        "photo": "images/odegaard.jpg"
    },
    "9": {
        "name": "Erling Haaland",
        "team": "Manchester City",
        "country": "Norway 🇳🇴",
        "position": "Forward (Striker)",
        "age": 25,
        "photo": "images/haaland.jpg"
    },
    "10": {
        "name": "Lionel Messi",
        "team": "Inter Miami",
        "country": "Argentina 🇦🇷",
        "position": "Forward / Playmaker",
        "age": 39,
        "photo": "images/messi.jpg"
    },
    "11": {
        "name": "Mohamed Salah",
        "team": "Liverpool",
        "country": "Egypt 🇪🇬",
        "position": "Forward (Winger)",
        "age": 34,
        "photo": "images/salah.jpg"
    }
}

# --- UI ပိုင်း ပြင်ဆင်ခြင်း ---
st.set_page_config(page_title="Football Squad Finder", page_icon="⚽", layout="centered")

st.title("Dream Squad Finder ⚽")
st.write("ကျောနံပါတ် (**1 မှ 11**) သို့မဟုတ် ကစားသမားနာမည် ရိုက်ထည့်ပြီး ရှာဖွေနိုင်ပါသည်။")

# အသုံးပြုသူ ရိုက်ထည့်မည့် နေရာ
search_query = st.text_input("Enter Player Name or Squad Number:", placeholder="e.g., 7, 10, Haaland, Salah")

# ရှာဖွေမှု အလုပ်လုပ်ပုံ (Logic)
if search_query:
    found = False
    query = search_query.strip().lower()
    
    for num, data in players_db.items():
        # နံပါတ် ကွက်တိတူရင် သို့မဟုတ် နာမည်ထဲမှာ ပါဝင်နေရင်
        if query == num or query in data["name"].lower():
            st.success(f"🎯 Player Found: {data['name']}")
            
            # စာသားနှင့် ပုံကို ဘယ်/ညာ ခွဲပြရန် Column ဆောက်ခြင်း
            col1, col2 = st.columns([1.2, 1])
            
            with col1:
                st.markdown(f"### ✨ **{data['name']}**")
                st.write("---")
                st.markdown(f"👕 **Squad Number:** `{num}`")
                st.markdown(f"🌍 **Nationality:** {data['country']}") # နိုင်ငံပြသပေးမည့် နေရာ
                st.markdown(f"🏰 **Current Club:** {data['team']}")
                st.markdown(f"🏃‍♂️ **Position:** {data['position']}")
                st.markdown(f"📅 **Age:** {data['age']} years old")
                
            with col2:
                # ဓာတ်ပုံ ရှိမရှိ စစ်ဆေးပြီး ပြသခြင်း
                if os.path.exists(data["photo"]):
                    st.image(data["photo"], caption=f"No.{num} - {data['name']}", use_container_width=True)
                else:
                    st.info(f"💡 `{data['photo']}` လမ်းကြောင်းမှာ ဓာတ်ပုံထည့်ပေးရင် ပုံပါ မြင်ရမှာဖြစ်ပါတယ်။")
                    
            found = True
            break
            
    if not found:
        st.error("❌ ကစားသမား မတွေ့ပါ။ နံပါတ် 1 မှ 11 အတွင်း သို့မဟုတ် နာမည်ကို မှန်ကန်စွာ ပြန်ရိုက်ပေးပါ။")

# --- အောက်ခြေတွင် ကစားသမားစာရင်း အကျဉ်းချုပ်ပြပေးထားခြင်း ---
with st.expander("📋 လက်ရှိအသင်းထဲမှာ ပါဝင်တဲ့ ကစားသမားများ စာရင်းကို ကြည့်ရန်"):
    # နိုင်ငံပါ တွဲပြပေးခြင်း
    for num, data in players_db.items():
        st.write(f"**No.{num}** - {data['name']} ({data['country']})")