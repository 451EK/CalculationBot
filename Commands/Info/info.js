const Discord = require("discord.js")
const { MessageEmbed, MessageButton, MessageActionRow } = require("discord.js")
const ms = require("ms")

module.exports = {
    name : "info",
    usage: "`-info`",
    description: "Shows information about the bot.",
    run : async(client,message) => {
        const components = new Discord.MessageActionRow()
            .addComponents([
                new Discord.MessageButton()
                .setLabel("Support Server")
                .setURL("https://discord.gg/tXd9gPtKCj")
                .setStyle("LINK"),

                new Discord.MessageButton()
                .setLabel("Vote")
                .setURL("https://top.gg/bot/869500014899122246/vote")
                .setStyle("LINK"),
            ]);
        const ping = ~~client.ws.ping
        let allUsers = [];
        client.guilds.cache.forEach(guilds => allUsers.push(guilds.memberCount))
        let users = allUsers.reduce((a, b) => a + b)
        const servers = client.guilds.cache.size
        let totalSeconds = process.uptime();
        let d = Math.floor((totalSeconds % 31536000) / 86400); // days
        let h = Math.floor((totalSeconds / 3600) % 24); // hours
        let m = Math.floor((totalSeconds / 60) % 60); // minutes
        const embed = new MessageEmbed()
        .setTitle(title="**Info**")
        .setDescription(this.description="Calculator is a discord bot developed to help you for your basic math operations.")
        .setFields(
            {name : "Author",value: "[451#2950](https://discord.com/users/453613270725558292)", inline:true},
            {name: "Library", value:"[discord.js](https://discord.js.org/#/)",inline:true},
            {name: "Uptime", value:`${d}d, ${h}h, ${m}m`,inline:true},
            {name: "Users", value:`${users}`,inline:true},
            {name:"Servers",value:`${servers}`,inline:true},
            {name:"Ping", value:`${ping}ms`,inline:true},
            {name: "Links", value:"[Github](https://github.com/M451z/Calculator) | [Invite](https://discord.com/api/oauth2/authorize?client_id=869500014899122246&permissions=259845909568&scope=bot%20applications.commands)"}
        )
        .setThumbnail(url="https://i.imgur.com/AJXNGEW.png")
        .setTimestamp()
        .setFooter(text=`Requested by ${message.author.tag}`,iconURL = message.author.avatarURL())
        .setColor("#00ff94")
        message.channel.send({embeds:[embed],components:[components]})
    }
}