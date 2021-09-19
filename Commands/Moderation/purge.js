const { MessageEmbed, Permissions } = require("discord.js")

module.exports = {
    name: "purge",
    usage: "`-purge <amount>`",
    description:"Deletes the entered amount of messages.",
    note: "Manage Messages permission is required to use this command.",
    run : async(client,message) => {
        if (!message.member.permissions.has(Permissions.FLAGS.MANAGE_MESSAGES)) {
            return msg.reply("You do not have Manage Messages permission to use this command!")
        }
        else if (message.member.permissions.has(Permissions.FLAGS.MANAGE_MESSAGES)) {
            const args = message.content.split(' ').slice(1)
            const amount = args.join(' ')

            if (!amount) return msg.reply('Give an amount to delete messages!')
            if (isNaN(amount)) return msg.reply('Given amount must be a number!')

            if (amount < 1) return msg.reply('Given amount must be positive!')
            let embed = new MessageEmbed()
            .setTitle(`${amount} messages deleted!`)
            .setColor("#00ff94")
            await message.channel.messages.fetch({ limit: amount }).then(messages => {
                message.channel.bulkDelete(messages
            )})
            await message.channel.send({embeds:[embed]}).then(msg => {
                setTimeout(() => msg.delete(),3000)
            })
        }
    }
}