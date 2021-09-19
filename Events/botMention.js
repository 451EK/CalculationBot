const client = require("../app.js")
defaultPrefix = "`-`"

client.on("messageCreate", message => {
    if (message.content.includes("@here") || message.content.includes("@everyone")) return false;
    if (message.mentions.has(client.user.id)) {
        message.reply(`Hello, my prefix is **${defaultPrefix}**(dash).\nUse the help command to see all commands!`);
        message.react("👋")
    };
})