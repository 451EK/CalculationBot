const Discord = require("discord.js")
const { MessageButton, MessageEmbed } = require("discord.js")

module.exports = {
    name: "curcodes",
    usage: "`-curcodes`",
    description: "Sends a link that shows the currency codes.",
    run: async(message) => {
        const button = new Discord.MessageActionRow()
            .addComponents([
                new Discord.MessageButton()
                .setLabel('Click Here')
                .setStyle('LINK')
                .setEmoji('💵')
                .setURL("https://paste.gg/p/anonymous/a8be7bc6c9eb48e6bf315148ce04324f")
            ]);
        const embed = new MessageEmbed()
        .setTitle("Currency Codes")
        .setDescription("Click the button below to see all currency codes.")
        .setTimestamp()
        .setThumbnail(url="https://i.imgur.com/AJXNGEW.png")
        .setColor("#00ff94")
        message.channel.send({embeds:[embed], components: [button]})
    }
}