# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:14:02 2024

@author: eamir
"""

import streamlit as st
import json
import pydeck as pdk
import datetime as dt


st.title("---Emir Rent A Car---")
st.markdown("Hizmetlerimiz")
st.video("https://www.youtube.com/watch?v=R3gvJ20h_MQ")

lok=[{'name':'Ataköy','lat':40.9787,'lon':28.8751},
     {'name':'Sirinevler','lat':40.9923,'lon':28.8615},
     {'name':'Bakırköy','lat':40.977439,'lon':28.873051},
     {'name':'İstanbul Havalimanı','lat':41.270814,'lon':28.733367},
     {'name':'Sabiha Gökçen Havalimanı','lat':40.892053,'lon':29.311811}]
lay=pdk.Layer("ScatterplotLayer",  
    lok,
    get_position="[lon, lat]",
    get_color="[250, 20, 0, 130]",  
    get_radius=120,  
    )
arac_lok={"Toyota":lok[0],
          "Honda":lok[1],
          "Mercedes":lok[2],
          "BMW":lok[3],
          "Renault":lok[4]}

#st.image("rent.png")


araclar=["Toyota","Honda","Mercedes","BMW","Renault"]
fiyatlar=[1500,2500,3000,2750,1250]


st.sidebar.subheader("Araç Bilgileri")
arac_a=st.sidebar.selectbox("Aracın adını giriniz ",["Aracınızı seçiniz"]+araclar)
arac_g=st.sidebar.text_input("Kaç gün kiralamayı planlıyorsunuz?")
Tarh=st.sidebar.date_input("Başlangıç tarihini giriniz: ",min_value=dt.date.today())
if arac_a in arac_lok:
    selected_lok=arac_lok[arac_a]
    lay=pdk.Layer("ScatterplotLayer",
        data=[selected_lok],
        get_position="[lon, lat]",
        get_color="[200, 30, 0, 160]",
        get_radius=350,
    )
    st.subheader("Aracınızı teslim alacağınız lokasyon")
    view_state = pdk.ViewState(
        latitude=selected_lok["lat"],
        longitude=selected_lok["lon"],
        zoom=11,
        pitch=0,
    )
    st.pydeck_chart(pdk.Deck(layers=[lay], initial_view_state=view_state))
    st.write(view_state)    
else:
    st.write("Haritada bir konum görüntülemek için bir araç seçiniz.")
if arac_a=="Toyota":
    st.sidebar.image("CHRHybrid.png")
    st.write("** Benzin : 10 LT/100 Km")
    st.write("** Vites: Otomatik")
elif arac_a=="Honda":
    st.sidebar.image("honda.png")
    st.write("** Benzin : 5 LT/100 Km")
    st.write("** Vites: Otomatik")
elif arac_a=="Mercedes":
    st.sidebar.image("mercedes3.png")
    st.write("** Benzin : 9 LT/100 Km")
    st.write("** Vites: Otomatik")
elif arac_a=="BMW":
    st.sidebar.image("bmw.png")
    st.write("** Benzin : 7 LT/100 Km")
    st.sidebar.info("Elimizde son bir ürün kaldı")
    st.write("** Vites: Otomatik")
elif arac_a=="Renault":
    st.sidebar.image("renault.gif")
    st.write("** Benzin : 4 LT/100 Km")
    st.write("** Vites: Otomatik")
col1, col2 = st.columns(2)

with col1:
    arac_yorum=st.text_area("Yorum Yapınız")
    kisi=st.text_input("Adınızı Giriniz: ")
    submit=st.button("Yorumu ekle")
tutar=0
submt=st.sidebar.button("Hesapla")

try:
  with open("araba_yorum.json","r",encoding="utf-8")as file:
      try:
        arac_listesi=json.load(file)
      except json.JSONDecodeError:
        arac_listesi = {"araba_yorum": []} 
except FileNotFoundError:
    arac_listesi={"araba_yorum":[]}
if submit:    
    yeni_yorum={"adi":arac_a,"fiyati":arac_g,"yorum":arac_yorum,"kişi":kisi}
    arac_listesi["araba_yorum"].append(yeni_yorum)
    with open ("araba_yorum.json","w",encoding="utf-8") as file :
        json.dump(arac_listesi,file,ensure_ascii=False,indent=4)
    st.success("Yorum başarıyla eklendi!")
    
def islem(arac_a,arac_g):
    if arac_a in araclar:
        ind=araclar.index(arac_a)
        gun=int(arac_g)
        toplam_tutar=fiyatlar[ind]*gun
        return toplam_tutar
    else:
        return None
if submt:
    try:
        toplam_tutar=islem(arac_a,arac_g)
        if toplam_tutar is not None:
            st.sidebar.success(f"Toplam Tutar: {toplam_tutar}")
    except ValueError:
        st.sidebar.error("Lütfen geçerli bir gün sayısı girin!")
with col2 : 
    if len(arac_listesi["araba_yorum"])>0:
       st.subheader("Eklenen Yorumlar")
    for yorum in arac_listesi["araba_yorum"]:
        kisi=yorum.get("kişi","Bilinmiyor")
        st.write(f"Araç: {yorum['adi']} - {yorum['fiyati']} gün - Yorum: {yorum['yorum']}, - kişi: {kisi}")
    else:
        st.write("Henüz yorum eklenmemiş.")

if Tarh:
    form_=Tarh.strftime("%d/%m/%Y")
if arac_g.isdigit() and Tarh:
    rent_l=int(arac_g)+1
    lt=Tarh+dt.timedelta(days=rent_l)
st.sidebar.markdown("Teslim Tarihi: ")
st.sidebar.error(lt)