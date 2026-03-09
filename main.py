import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- INSERISCI QUI IL TUO TOKEN ---
# Ricordati di rigenerarlo su BotFather dopo averlo incollato qui
TOKEN = "8520852137:AAEm_TcwWmz2Uiu5GX92vEelpK2l4RtWzFw"
# ----------------------------------

async def meteo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Coordinate di Lecco e parametri richiesti (temp e umidità)
    url = "https://api.open-meteo.com/v1/forecast?latitude=45.85&longitude=9.39&current=temperature_2m,relative_humidity_2m&hourly=temperature_2m&forecast_days=5"
    
    try:
        response = requests.get(url).json()
        
        # Dati attuali
        temp = response['current']['temperature_2m']
        umidita = response['current']['relative_humidity_2m']
        
        # Risposta formattata
        messaggio = (
            f"📍 *Meteo a Lecco*\n\n"
            f"🌡 Temperatura attuale: {temp}°C\n"
            f"💧 Umidità: {umidita}%\n\n"
            f"Il bot è operativo e pronto a darti i dati!"
        )
        
        await update.message.reply_text(messaggio, parse_mode="Markdown")
        
    except Exception as e:
        await update.message.reply_text("Errore nel recupero dei dati dal server.")

if __name__ == '__main__':
    # Configurazione bot
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("meteo", meteo))
    
    print("Il bot è online. Premi Ctrl+C per fermarlo.")
    app.run_polling()