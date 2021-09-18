import discord, database
from discord import message
from datetime import datetime
from discord.ext import commands
from discord.utils import get

token = "ODg3NzE5MDM2MDIzMDgzMDA4.YUIOxw.sCKYW5UL79T5xcZ4Sf1jTtmRAOc"

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix="$", description="Hello there ;)", intents=intents)
client.remove_command("help")


help_text = """help --> Mostra aquest missatge
say --> re envia el text ue li diguis, si es mes d'na paraula ha d'star entre cometes"""

@client.event
async def on_ready():
    print(f"{client.user} has connected to de server")

@client.event
async def on_member_join(member):
    with open("./log.txt", "a") as f:
        f.write(f"{datetime.now()}: {member.name}({member.id}) joined the server\n")
    channel = client.get_channel(888451461879578684)
    if len(database.check_balance(member.id)) == 0:
        database.add_user(member.id, member.name)
    embed = discord.Embed(title="Welcome!",description=f"{member.mention} Acaba d'arribar")
    user_role = get(member.guild.roles, name="User")
    await member.add_roles(user_role)
    await channel.send(embed=embed)

@client.command()
async def cartera(ctx):
    with open("./log.txt", "a") as f:
        f.write(f"{datetime.now()}: {ctx.message.author.name}({ctx.message.author.id}) checked his ballance\n")
    data = database.check_balance(ctx.message.author.id)
    embed = discord.Embed(title="Cartera",description=f"La cartera d'en <@{ctx.message.author.id}> conte {data[0][2]} ligma")
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    with open("./log.txt", "a") as f:
        f.write(f"{datetime.now()}: {ctx.message.author.name}({ctx.message.author.id}) asked for help\n")
    embed = discord.Embed(title="Nessesites ajuda?",description=help_text)
    await ctx.send(embed=embed)


@client.command()
async def sell(ctx, titol, descripcio, preu):
    with open("./abs_num.txt", "r") as f:
        num = int(f.read())
    with open("./abs_num.txt", "w") as f:
        f.write(str(num+1))
    
    id_seller = "_".join(titol.split(" "))+">"+str(num)
    id_buyer = id_seller+"_buy"

    guild = ctx.guild
    await guild.create_role(name=id_seller)
    await guild.create_role(name=id_buyer)

    role_seller = get(guild.roles, name=id_seller)
    role_buyer = get(guild.roles, name=id_buyer)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
        role_seller: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        role_buyer: discord.PermissionOverwrite(read_messages=True)
    }

    await guild.create_text_channel(id_seller, overwrites=overwrites)
    await ctx.message.author.add_roles(role_seller)

    database.add_oferta(id_seller, titol, descripcio, ctx.message.author.id, ctx.message.author.name, preu)

    embed = discord.Embed(title="Fet",description=f"S'ha posat a la venta '{titol}' per {preu}")
    await ctx.send(embed=embed)

    ofertes = database.check_ofertes()
    text = ""
    for oferta in ofertes:
        text += f"""< {oferta[1]} > 
        Venedor: {oferta[4]}
        Preu: {oferta[5]} ligma
        Id: {oferta[0]}
        Descripció: {oferta[2]}
        
        """
    channel = client.get_channel(888452914023120937)

    with open("./log.txt", "a") as f:
        f.write(f"{datetime.now()}: {ctx.message.author.name}({ctx.message.author.id}) started to sell {titol} with a description stating: {descripcio} for a price of {preu} ligma\n")

    embed = discord.Embed(title="Ofertes!",description=text)

    await channel.send(embed=embed)

@client.command()
async def create_db_user(ctx):
    if ctx.message.author.id == 631113961999302666:
        database.add_user(ctx.message.author.id, ctx.message.author.name)
    else:
        await ctx.send("No tens permis per aquest comandament")

@client.command()
async def buy(ctx, product_id):
    buyer = database.check_balance(ctx.message.author.id)
    product = database.search_oferta(product_id)
    if not len(product) == 1:
        return "ID incorrecte"
    price = product[0][5]
    seller = database.check_balance(product[0][3])
    if buyer[0][2] >= price:
        database.modificar_cartera(seller[0][0], price)
        database.modificar_cartera(buyer[0][0], -price)
        with open("./log.txt", "a") as f:
            f.write(f"{datetime.now()}: {ctx.message.author.name}({ctx.message.author.id}) bought {product[0][1]} for {product[0][5]} ligma from {seller[0][1]}({seller[0][0]}\n")
        role = get(ctx.guild.roles, name=product[0][0]+"_buy")
        await ctx.message.author.add_roles(role)
        embed = discord.Embed(title="Fet!!",description=f"Has comprat {product[0][0]} per {product[0][5]} ligma")
        await ctx.send(embed=embed)
    else:
        return "No hi han prous diners"

client.run(token)