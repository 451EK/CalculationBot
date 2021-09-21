const client = require("../app.js")

client.on("messageCreate", message => {
    if (message.mentions.has(client.user.id)) {
        message.react("👋")
    };
})
