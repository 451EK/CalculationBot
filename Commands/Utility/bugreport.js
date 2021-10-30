const { MessageEmbed } = require('discord.js');

module.exports = {
    name: "bugreport",
    usage: "`-bugreport <message>`",
    description: "Sends a bug report message to developer.",
    note: "Please do not abuse this command.",
    run: async(client,message,args) => {
        channel = client.channels.cache.get("901756235035082832")
        embed = new MessageEmbed()
        .setTitle("New Bug Report")
        .setDescription(`🚨 ${args.join(" ")}`)
        .setTimestamp()
        .setColor("#00ff94")
        .setFooter(`Sent by ${message.author.tag}`,message.author.avatarURL())
        doneEmbed = new MessageEmbed()
        .setTitle("**Your Report Has Successfully Been Sent!**")
        .setColor("#00ff94")
        channel.send({embeds:[embed]})
        message.channel.send({embeds:[doneEmbed]})
        message.delete()
    }
}
