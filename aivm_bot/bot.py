import discord
import aivm_client as aic
import os
import torch
from aivm_bot.env import TOKEN

# Create an instance of the bot
intents = discord.Intents.default()
intents.message_content = True  # Ensure that the bot can read message content
client = discord.Client(intents=intents)

# Emoji to react with
EMOJIS_A = ["👎", "😐", "😁"]
EMOJIS_B = ["😔", "🤔", "👍"]
EMOJIS_C = ["😢", "🙄", "🔥"]


MODEL_NAME = "bert-tiny-sentiment-analysis"
@client.event
async def on_ready():
    print(f'Bot is ready! Logged in as {client.user}')
    path = os.path.join(os.path.dirname(__file__), "twitter_bert_tiny.onnx")
    try:
        aic.upload_bert_tiny_model(path, MODEL_NAME)
    except:
        print("Model already exists")

@client.event
async def on_message(message):
    # Avoid the bot reacting to its own messages
    if message.author == client.user:
        return
    
    tokens = aic.tokenize(message.content)
    inputs = aic.BertTinyCryptensor(*tokens)
    result = aic.get_prediction(inputs, MODEL_NAME)
    for emojis in [EMOJIS_A, EMOJIS_B, EMOJIS_C]:

        emoji = emojis[torch.argmax(result).item()]
        # Add an emoji reaction to every message

        await message.add_reaction(emoji)


def main():
    # Run the bot with your token
    client.run(TOKEN)

if __name__ == "__main__":
    main()