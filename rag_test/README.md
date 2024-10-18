Here’s the `README.md` document in Finnish for your **Proof of Concept** for **Retrieval-Augmented Generation (RAG)** liittyen työsopimuksiin suomeksi ja englanniksi:

---

# Retrieval-Augmented Generation (RAG) - Työsopimukset (Suomi & Englanti)

Tämä projekti esittelee **Proof of Conceptin (PoC)** **Retrieval-Augmented Generationin (RAG)** hyödyntämiseksi työsopimusten käsittelyssä sekä suomeksi että englanniksi. Se käyttää **Streamlit-sovellusta** käyttäjävuorovaikutukseen ja **Chroma-tietokantaa** dokumenttien hakuun.

### Sisällysluettelo
- [Vaatimukset](#vaatimukset)
- [Asennusohjeet](#asennusohjeet)
- [Suorittaminen](#suorittaminen)
- [Käyttö](#käyttö)
- [Jatkokehitys](#jatkokehitys)

---

## Vaatimukset

- **Docker**: Asenna Docker sovelluksen kontittamiseksi ja ajamiseksi.
  - [Asenna Docker](https://docs.docker.com/get-docker/)
- **Docker Compose** (Valinnainen): Jos haluat hallita useita palveluja, kuten Chroma-tietokantaa ja Streamlit-sovellusta yhdessä.
  - [Asenna Docker Compose](https://docs.docker.com/compose/install/)

Varmista, että nämä on asennettu ennen jatkamista.

---

## Asennusohjeet

### 1. Kloonaa Repositorio

```bash
git clone https://github.com/your-repo/rag-employment-contracts.git
cd rag-employment-contracts
```

### 2. Projektin rakenne

Varmista, että projektihakemistosi näyttää tältä:

```
project/
│
├── app.py                # Streamlit-sovellus
├── file1.pdf             # Työsopimus englanniksi
├── file2.pdf             # Työsopimus suomeksi
├── requirements.txt      # Python-riippuvuudet
├── Dockerfile            # Dockerfile sovelluksen kontittamiseen
└── docker-compose.yml    # (Valinnainen) Docker Compose -tiedosto usean palvelun asetuksiin
```

### 3. Ympäristömuuttujat (Valinnainen)

Jos tarvitset API-avaimia tai muita salaisuuksia, luo `.env`-tiedosto projektin juureen seuraavanlaisella sisällöllä:

```
# Esimerkki .env-tiedostosta
CHROMA_API_KEY=chroma_api_avaimesi
```

Varmista, että sovelluksesi osaa lukea nämä ympäristömuuttujat.

---

## Suorittaminen

### Vaihtoehto 1: Dockerin käyttö

1. **Rakenna Docker-image**:

   ```bash
   docker build -t streamlit-chroma-app .
   ```

2. **Aja kontti**:

   ```bash
   docker run -p 8501:8501 streamlit-chroma-app
   ```

3. **Avaa sovellus**:

   Avaa selain ja mene osoitteeseen `http://localhost:8501` käyttämään Streamlit-sovellusta.

### Vaihtoehto 2: Docker Composen käyttö (Suositeltava)

Jos integrointi **Chroma-tietokannan** kanssa on tarpeen:

1. **Rakenna ja aja palvelut**:

   ```bash
   docker-compose up --build
   ```

2. **Avaa sovellus**:

   Avaa selain ja mene osoitteeseen `http://localhost:8501` käyttääksesi Streamlit-sovellusta.

   Chroma-tietokanta on saatavilla osoitteessa `http://localhost:8000` (jos tarpeen).

---

## Käyttö

Tämä Proof of Concept tukee **retrieval-augmented generation** -tekniikkaa työsopimusten käsittelyyn. Sovellus voi:

1. Ladata ja käsitellä työsopimuksia sekä **englanniksi** että **suomeksi**.
2. Yhdistyä **Chroma-tietokantaan** relevantin tiedon hakemiseksi ja asiakirjojen käsittelyn parantamiseksi.
3. Suorittaa kielikohtaisia toimintoja työsopimuksille, sopeutuen valittuun kieleen (englanti/suomi).

### Vaiheet:

1. **Työsopimusten lataaminen**: Sovellus lataa kaksi valmiiksi olemassa olevaa PDF-työsopimusta, joista toinen on englanniksi ja toinen suomeksi.
2. **Sopimusten tarkastelu ja vuorovaikutus**: Sovellus näyttää sopimukset ja antaa käyttäjän olla vuorovaikutuksessa niiden kanssa.
3. **Tietojen haku**: Sovellus hakee ja täydentää relevantteja tietoja **Chroma-tietokannan** avulla, analysoiden sopimuksia kattavammin.

---

## Jatkokehitys

- Laajenna kielituki kattamaan useampia kieliä kuin englanti ja suomi.
- Implementoi kehittyneempi **luonnollisen kielen ymmärtämismalli (NLU)** sopimusten tarkempaan analysointiin.
- Lisää lisädokumenttityyppejä ja monimutkaisempia haku-generointi käyttötapauksia.

---

### Huomautuksia

- Varmista, että **Docker** ja **Docker Compose** ovat ajan tasalla.
- Tämä Proof of Concept keskittyy työsopimuksiin ja esittelee **monikielistä tietojen hakua** RAG-tekniikoiden avulla.

