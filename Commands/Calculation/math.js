const { MessageEmbed } = require("discord.js")
const math = require("mathjs")

module.exports = {
    name: "math",
    usage: "`-math <operation>`",
    description: "Gives the result of entered operation.",
    run: async(message,args) => {
        try{
            let embed = new MessageEmbed()
            .setTitle("Math")
            .addField(this.name="Input",value="```js\n" + args.join(" ") + "\n```")
            .addField(this.name="Output",value="```js\n" + math.evaluate(args.join(" ")) + "\n```",inline=false)
            .setColor("#00ff94")
            .setFooter(`Requested by ${message.author.tag}`,message.author.avatarURL())
            message.channel.send({embeds: [embed]})
        }catch(error) {
            message.reply("Please enter a correct operation, then try again!")
            console.log(error)
        }
    }
}