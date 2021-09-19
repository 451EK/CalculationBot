const { MessageEmbed } = require("discord.js")
const Math = require("mathjs")

module.exports = {
    name: "sqrt",
    usage: "`-sqrt <number>`",
    description: "Sends the square root of entered number.",
    run: async(message,args) => {
        try{
            let embed = new MessageEmbed()
            .setTitle("Square Root")
            .addField(this.name="Input",value="```js\n" + `√${args.join(" ")}` + "\n```")
            .addField(this.name="Output",value="```js\n" + Math.sqrt(args.join(" ")) + "\n```",inline=false)
            .setColor("#00ff94")
            .setFooter(`Requested by ${message.author.tag}`,message.author.avatarURL())
            message.channel.send({embeds: [embed]})
        }catch(error) {
            message.reply("Please enter an integer, then try again!")
            console.log(error)
        }
    }
}