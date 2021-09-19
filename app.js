const Discord = require("discord.js")
const fs = require("fs")
const { Intents,Collection } = Discord;
const client = new Discord.Client({
    "intents": [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]
})
const config = require("./config.json")

module.exports = client;
client.commands = new Collection();
client.aliases = new Collection();
client.categories = fs.readdirSync("./Commands/");

["command", "event"].forEach(handler => {
    require(`./handlers/${handler}`)(client);
});

client.login(config.token)