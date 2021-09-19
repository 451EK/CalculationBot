const { MessageEmbed } = require("discord.js")
defaultPrefix = "-"

module.exports = {
    name: "length",
    usage: "`-length <message>`",
    description: "Shows the length of entered message.",
    run: async(message) => {
        const args = message.content.slice(defaultPrefix.length + this.name).split(/ +/)
        if(args.length === 1){
            message.reply("Provide a message!")
            return
        }
        var le = args.slice(1).reduce((a, b) => a + b, 0)
        rle = le.substring(1)
        let embed = new MessageEmbed()
        .setTitle("Length")
        .addField(this.name="Message",value="```js\n" + rle + "\n```")
        .addField(this.name="Length",value="```js\n" + rle.length + "\n```",inline=false)
        .setColor("#00ff94")
        .setFooter(`Requested by ${message.author.tag}`,message.author.avatarURL())
        message.channel.send({embeds: [embed]})
    }
}