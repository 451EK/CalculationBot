const { MessageEmbed } = require("discord.js")

module.exports = {
    name: "google",
    usage: "-google <whatYouWant>",
    description: "Searches google for you with using `lmgtfy`.",
    run: async(client,message,args) => {
        let query = args.join(" ").toString()
        let url = query.replace(/ /g, "+")
        const embed = new MessageEmbed()
        .setAuthor("Click Here To See The Result",message.author.avatarURL(),`https://lmgtfy.app/?qtype=search&q=${url}`)
        .setColor("#00ff94")
        message.reply({embeds:[embed]})
    }
}