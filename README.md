Ecco il README aggiornato in entrambe le lingue, con il nome corretto del progetto:

---

# ⚽ Fantacalcio Team Prediction

Un progetto di **Machine Learning** che analizza le statistiche del fantacalcio dal 2017 al 2023 per costruire la squadra ideale per la stagione corrente! 🚀

## 🎯 Obiettivi

Questo progetto mira a creare un modello che seleziona i giocatori migliori per formare la squadra perfetta di fantacalcio. Basandosi su statistiche come goal, assist, ammonizioni e molto altro, l'algoritmo ottimizza la scelta del portiere, difensori, centrocampisti e attaccanti per ottenere il miglior punteggio possibile.

## 📈 Dataset

Il dataset include statistiche dal 2017 al 2023 per ogni giocatore, comprese:

- `role` (Ruolo)
- `name` (Nome)
- `team` (Squadra)
- `win_matches` (Partite vinte)
- `media` (Media voto)
- `fanta_media` (Media fantacalcio)
- `goal_scored` (Goal segnati)
- `goal_subiti` (Goal subiti)
- `rigori_parati` (Rigori parati)
- ... e altre metriche ⚽

## 🛠️ Preprocessing dei Dati

Nel preprocessing, il dataset è stato:

1. 💾 **Pulito**: I valori mancanti sono stati gestiti.
2. 📊 **Normalizzato**: Le statistiche numeriche sono state scalate tra 0 e 1 per una migliore performance del modello.
3. 🏷️ **Verificato**: Sono state incluse tutte le colonne essenziali come `role` e `name`.

### 📂 Come usare il dataset preprocessato

Il dataset preprocessato è stato salvato in un file CSV pronto per essere utilizzato nel modello di machine learning.

```bash
dataset_statistiche_preprocessed.csv
```

## 🧠 Modello di Machine Learning

Il modello di machine learning utilizza le statistiche preprocessate per costruire la squadra ideale in base alla stagione corrente. Ottimizza le seguenti metriche:

- **Portieri**: Massimizza la fanta_media, minimizza i goal subiti.
- **Difensori, Centrocampisti, Attaccanti**: Massimizza goal, assist, e minimizza ammonizioni, espulsioni e autogol.

## 🚀 Come eseguire il progetto

1. Clona il repository:

   ```bash
   git clone https://github.com/Calisti-Daniele/AI-Fantacalcio.git
   ```

2. Installa le dipendenze:

   ```bash
   pip install pandas scikit-learn numpy matplotlib
   ```

3. Esegui il preprocessing dei dati:

   ```bash
   python preprocess_data.py
   ```

4. Allena il modello:

   ```bash
   python train_model.py
   ```

5. Ottieni la squadra ideale per la stagione corrente:

   ```bash
   python build_team.py
   ```

## 🔧 Tecnologie utilizzate

- **Python** 🐍
- **Pandas** 🐼
- **Scikit-learn** 🧠
- **NumPy** 🔢
- **Matplotlib** 📊

## 🚀 Obiettivi Futuri

- Migliorare l'algoritmo di selezione della squadra con tecniche avanzate di ottimizzazione.
- Integrare un'interfaccia web per visualizzare i risultati in modo più interattivo.
- Aggiungere nuove feature nel dataset, come i cartellini gialli/rossi ricevuti dai giocatori.

## 💡 Contributi

Sentiti libero di creare una **pull request** o aprire una **issue** se hai suggerimenti o idee per migliorare il progetto! ✨

## 📬 Contatti

Per qualsiasi domanda o collaborazione, puoi contattarmi via email a ```daniele.calisti03@gmail.com``` o aprire una issue direttamente su GitHub! 😊

---

# ⚽ Fantacalcio Team Prediction (English Version)

A **Machine Learning** project that analyzes fantasy football stats from 2017 to 2023 to build the ideal team for the current season! 🚀

## 🎯 Goals

This project aims to create a model that selects the best players to form the perfect fantasy football team. Based on stats like goals, assists, yellow cards, and more, the algorithm optimizes the choice of goalkeeper, defenders, midfielders, and forwards to achieve the best possible score.

## 📈 Dataset

The dataset includes statistics from 2017 to 2023 for each player, including:

- `role` (Player's role)
- `name` (Player's name)
- `team` (Team)
- `win_matches` (Matches won)
- `media` (Average rating)
- `fanta_media` (Fantasy rating)
- `goal_scored` (Goals scored)
- `goal_subiti` (Goals conceded)
- `rigori_parati` (Penalties saved)
- ... and other key metrics ⚽

## 🛠️ Data Preprocessing

In the preprocessing step, the dataset was:

1. 💾 **Cleaned**: Missing values were handled.
2. 📊 **Normalized**: Numerical statistics were scaled between 0 and 1 for better model performance.
3. 🏷️ **Verified**: All essential columns like `role` and `name` were included.

### 📂 How to Use the Preprocessed Dataset

The preprocessed dataset is saved in a CSV file and is ready to be used in the machine learning model.

```bash
dataset_statistiche_preprocessed.csv
```

## 🧠 Machine Learning Model

The machine learning model uses the preprocessed stats to build the ideal team for the current season. It optimizes the following metrics:

- **Goalkeepers**: Maximize fanta_media, minimize goals conceded.
- **Defenders, Midfielders, Forwards**: Maximize goals, assists, and minimize yellow cards, red cards, and own goals.

## 🚀 How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Calisti-Daniele/AI-Fantacalcio.git
   ```

2. Install the dependencies:

   ```bash
   pip install pandas scikit-learn numpy matplotlib
   ```

3. Run the data preprocessing:

   ```bash
   python preprocess_data.py
   ```

4. Train the model:

   ```bash
   python train_model.py
   ```

5. Get the ideal team for the current season:

   ```bash
   python build_team.py
   ```

## 🔧 Technologies Used

- **Python** 🐍
- **Pandas** 🐼
- **Scikit-learn** 🧠
- **NumPy** 🔢
- **Matplotlib** 📊

## 🚀 Future Goals

- Improve the team selection algorithm with advanced optimization techniques.
- Integrate a web interface to display the results interactively.
- Add new features to the dataset, like yellow/red cards received by players.

## 💡 Contributions

Feel free to submit a **pull request** or open an **issue** if you have suggestions or ideas to improve the project! ✨

## 📬 Contact

For any questions or collaboration, feel free to reach out via email at ```daniele.calisti03@gmail.com``` or open an issue directly on GitHub! 😊

---
