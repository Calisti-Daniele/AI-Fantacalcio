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
      pip install pandas numpy sklearn matplotlib
   ```

3. Esegui il preprocessing dei dati:

   ```bash
      python preprocessing.py
   ```

4. Allena il modello:

   ```bash
      python training.py
   ```

5. Ottieni la squadra ideale per la stagione corrente:

   ```bash
      python predict.py
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

Per qualsiasi domanda o collaborazione, puoi contattarmi vall'email daniele.calisti03@gmail.com o aprire una issue direttamente su GitHub! 😊
