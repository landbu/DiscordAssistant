from dotenv import load_dotenv
import os
import bot
if __name__=="__main__":
    try: load_dotenv()
    except Exception as e: print("Failed to load eviorment variables. Error:\n", e)
    else: bot.run_discord_bot(os.getenv("TOKEN2"))   #change token to change bot


