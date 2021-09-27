const { MessageEmbed, DiscordAPIError, Message } = require("discord.js")

module.exports = {
    name : 'ping',
    usage: "`-ping`",
    description : 'Shows bot latency.',
    run : async(client, message) => {
        const botIcon = client.user.displayAvatarURL()
        const ping = ~~client.ws.ping // bot latency
        msg = message.channel.send("_Calculating Ping_ <a:an_loading:873267683179765781>").then(m => {
            if (ping > 100){
                const latency = m.createdTimestamp - message.createdTimestamp
                let embed = new MessageEmbed()
                .setTitle(title="Latency")
                .setDescription(this.description=`**Roundtrip**\n<:low_performance:872498172646277141> **${ping}ms**\n\n**Heartbeat**\n<:heart_beat:873322591891378176> **${latency}ms**`)
                .setTimestamp()
                .setFooter(text="Calculator#0261",iconURL = botIcon)
                .setColor("#00ff94")
                m.delete()
                message.channel.send({embeds:[embed]})
            }
            else if (ping < 100){
                const latency = m.createdTimestamp - message.createdTimestamp
                let embed2 = new MessageEmbed()
                .setTitle(title="Latency")
                .setDescription(this.description=`**Roundtrip**\n<:normal_performance:872498173292208239> **${ping}ms**\n\n**Heartbeat**\n<:heart_beat:873322591891378176> **${latency}ms**`)
                .setTimestamp()
                .setFooter(text="Calculator#0261",iconURL = botIcon)
                .setColor("#00ff94")
                m.delete()
                message.channel.send({embeds:[embed2]})        
            }
        });
}
}
