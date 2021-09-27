const { MessageEmbed } = require("discord.js")
const Math = require("mathjs")

module.exports = {
    name: "stats",
    usage: "-stats",
    description: "Shows the system stats.",
    run: async(client,message) => {
        const channels = client.channels.cache.size
        const servers =client.guilds.cache.size
        let allUsers = [];
        client.guilds.cache.forEach(guilds => allUsers.push(guilds.memberCount))
        let users = allUsers.reduce((a, b) => a + b)
        const ToTalSeconds = (client.uptime / 1000);
        const d = Math.floor(ToTalSeconds / 86400);
        const h = Math.floor(ToTalSeconds / 3600);
        const m = Math.floor(ToTalSeconds / 60);
        const s = Math.floor(ToTalSeconds % 60);
        const Uptime = "`"+`${d}d, ${h}h, ${m}m, ${s}s`+"`";
        const os = require("os")
        const OsHostName = os.hostname();
        const MemoryUsage = process.memoryUsage().heapUsed / 1024 / 1024;
        const RamUsed = Math.round(process.cpuUsage().system) / 1024;
        const RamUsage = Math.round(RamUsed);
        const BotPlatform = process.platform;
        const MemoryUsed = Math.round(MemoryUsage);
        const SystemPing = Math.round(client.ws.ping);

        const embed = new MessageEmbed()
        .setTitle("Live Calculator Status")
        .setColor("#00ff94")
        .setThumbnail(client.user.avatarURL())
        .addField("__Bot Uptime __","`"+ Uptime +"`",true)
        .addField("__Bot's Hot Name__","`"+ OsHostName+"`" ,true)
        .addField("__CPU Usage__","`"+RamUsage+"Mb`" ,true)
        .addField("__Memory Usage__","`"+ MemoryUsed +"Mb`",true)
        .addField("__Bot Platform__","`"+ BotPlatform+"`" ,true)
        .addField("__System Ping__","`"+ SystemPing+"ms`",true)
        .addField("__Channels__", "`"+channels +"`",true)
        .addField("__Servers__", "`"+servers +"`",true)
        .addField("__Users__", "`"+users +"`",true)
        .setTimestamp()
        .setFooter(`Requested by ${message.author.tag}`,message.author.avatarURL())

        await message.channel.send({embeds: [embed]})
    }
}
