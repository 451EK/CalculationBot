const Discord = require("discord.js")
const fs = require("fs")
const { Intents,Collection } = Discord;
const client = new Discord.Client({
    "intents": [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.GUILD_PRESENCES]
})
const { AutoPoster } = require('topgg-autoposter')
const config = require("./config.json")

const ap = AutoPoster("TOP.GG TOKEN", client)

ap.on('posted', () => {
  console.log('Posted stats to Top.gg!')
})

module.exports = client;
client.commands = new Collection();
client.aliases = new Collection();
client.categories = fs.readdirSync("./Commands/");

["command", "event"].forEach(handler => {
    require(`./handlers/${handler}`)(client);
});

client.login(config.token)
