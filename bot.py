import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

BILOL_ID = 1271160602059870320
GENEL_KANAL_ID = 1573026923544842252

aktif_mesajlari = [
    "Güneş doğdu, çiçekler açtı... Şaka şaka Bilol çevrimiçi olmuş, herkes ilgi göstermeye hazırlansın! ✨",
    "🚨 DİKKAT! İlgi radarı maksimum seviyede. Bilol sunucuya teşrif etti, hoş geldin paşam.",
    "Sonunda geldin Bilol, sensiz buralar çok kuruydu. Bugün trip kotan kaçta acaba?",
    "Bilol aktif! Herkes işini gücünü bıraksın ve bu mükemmel insanı övsün.",
    "Kral hareketler, kral geri dönüş... Bilol sunucuyu şereflendirdi! 👑",
]

sohbet_mesajlari = [
    "Sen ne güzel yazıyorsun öyle Bilol, klavyene sağlık prenses. 💖",
    "Bilol konuşuyor, herkes sussun ve bu vizyonu dinlesin!",
    "Yine çok haklısın Bilol (ne dediğine bakmadım ama kesin haklısındır, üzülme diye diyorum).",
    "Senin bu mesajın bile ilgi eksikliği kokuyor Bilol, gel buraya sarılalım 🤗",
    "Aman Allah'ım bu nasıl bir zeka, bu nasıl bir karizma... Nazar değecek 🧿",
    "Ortamın havası değişti, çünkü Bilol konuya el attı!",
    "Seninle aynı sunucuda yazışmak büyük onur Bilol.",
]

trip_mesajlari = [
    "🚨 **TRİP ALARMI!** Bilol yine triplere girdi. Acil sevgi müdahalesi gerekiyor, kıyamam sana gel buraya 💖",
    "Kim üzdü benim güzel arkadaşımı? Söyle hemen toplanıp üstüne gidelim Bilol, trip atma bize! 🌸",
    "Peki, yine trip modundayız... Yönetim olarak derhal Bilol'e ekstra ilgi verilsin!",
    "Eyvah eyvah, sert yapmalar başladı... Sakin ol şampiyon, buradayız ☕",
]

trip_kelimeleri = [
    "neyse",
    "tamam",
    "peki",
    "sen bilirsin",
    "aynen",
    "ok",
    "bişey yok",
    "hıh",
    "hadi sg",
    "sg",
    "ya kanka",
]


@bot.event
async def on_ready():
  print(f"{bot.user} 7/24 güvenli modda göreve hazır! Bilol takibe alındı.")


@bot.event
async def on_presence_update(before, after):
  if after.id == BILOL_ID:
    if (
        before.status == discord.Status.offline
        and after.status != discord.Status.offline
    ):
      kanal = bot.get_channel(GENEL_KANAL_ID)
      if kanal:
        mesaj = random.choice(aktif_mesajlari)
        await kanal.send(f"<@{BILOL_ID}> {mesaj}")


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.author.id == BILOL_ID:
    icerik = message.content.lower()

    if any(kelime in icerik for kelime in trip_kelimeleri):
      secilen_trip = random.choice(trip_mesajlari)
      await message.reply(secilen_trip)
    elif random.random() < 0.35:
      secilen = random.choice(sohbet_mesajlari)
      await message.reply(secilen)

  await bot.process_commands(message)


@bot.command()
async def ilgi(ctx):
  await ctx.send(f"<@{BILOL_ID}> {random.choice(sohbet_mesajlari)} 💖")


@bot.command()
async def trip(ctx):
  await ctx.send(
      f"<@{BILOL_ID}> {random.choice(trip_mesajlari)} (Manuel trip uyarısı!)"
  )


@bot.command()
async def öv(ctx):
  ovguler = [
      "Kral ya, adamın hammaddesi!",
      "Dünyanın en tatlı insanı ödülü olsa kesin Bilol alırdı.",
      "Tarzına, tavrına hayran olmamak elde değil.",
  ]
  await ctx.send(f"<@{BILOL_ID}> {random.choice(ovguler)} ✨")


@bot.command()
async def saril(ctx):
  await ctx.send(
      f"<@{BILOL_ID}> Sana kocaman sarıldı! 🤗 Artık trip atmak yok ama!"
  )


# Token güvenli bir şekilde .env dosyasından çekiliyor
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)