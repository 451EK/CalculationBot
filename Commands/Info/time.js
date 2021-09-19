const { MessageEmbed } = require("discord.js")
const moment = require("moment")

module.exports = {
    name: "time",
    usage: "`-time`",
    description: "Displays the time.",
    run: async(message) => {
        var date = moment().format("dddd, MMMM Do YYYY")
        var hrs = moment().format("h:mm:ss a")
        let embed = new MessageEmbed()
        .setTitle("Time")
        .setDescription(`${date}\n${hrs}`)
        .setColor("#00ff94")
        message.channel.send({embeds:[embed]})
    }
}