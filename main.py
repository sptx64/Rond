import streamlit as st
import pickle
import os
import pandas as pd

"## Ton nom"
with st.form("nom") :
    name = st.text_input("Ton nom :", placeholder="NOM")
    go = st.form_submit_button("Envoyer")
    if go :
        if name == "" or name is None :
            st.toast("Ne fais pas le timide...")

if name == "" or name is None :
    st.stop()

fpath = "dict.pkl"

if os.path.exists(fpath) :
    with open(fpath, "rb") as f :
        dict_rond = pickle.load(f)
else :
     dict_rond = {}

if name in dict_rond :
    dict_rond[name] += 1
else :
    dict_rond[name] = 1

with open(fpath, "wb") as f :
    pickle.dump(dict_rond, f)

f"## Hello {name}"
st.image("Screenshot_20251031-125958.png")

"## Scores"
df = pd.DataFrame({
    "noms" : [ x for x in dict_rond],
    "score" : [ dict_rond[x] for x in dict_rond ]
})

df