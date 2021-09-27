const { MessageEmbed, MessageActionRow } = require("discord.js")
const Discord = require("discord.js")
const moment = require("moment")

module.exports = {
    name: "userinfo",
    usage: "-userinfo <user>",
    description: "Shows the information about user.",
    run: async(client,message,args) => {
        let user;
        if (message.mentions.users.first()) {
          user = message.mentions.users.first()
        } else if (args[0]) {
          let pre = message.guild.members.cache.get(args[0]) || message.guild.members.cache.find(member => member.user.username === args[0])
          if (pre) user = pre.user;
          else if(!pre) user= message.author
        } else {
          user = message.author;
        }
        const member = message.guild.members.cache.get(user.id)
        const roles = member.roles.cache.filter(role => role.id !== message.guild.id).map(role => role).join(", ") || "none"

        const button = new MessageActionRow()
        .addComponents([
            new Discord.MessageButton()
            .setLabel("User Profile")
            .setURL(`https://www.discord.com/users/${user.id}`)
            .setStyle("LINK")
        ])

        let status = member.presence?.status
        if (status === "online"){
            status = "<:online:891229323766403092> Online"
        }
        if (status === "idle"){
            status = "<:idle:891229377021480962> Idle"
        }
        if (status === "dnd"){
            status = "<:dnd:891229377403166751> Do Not Disturb"
        }
        if (status === "offline"){
            status = "<:offline:891229323388940300> Offline"
        }

        let verifiedBotDeveloperBadge = ""
        let earlySupporterBadge = ""
        let hypesquadEventsBadge = ""
        let discordPartnerBadge = ""
        let hypesquadBravery = ""
        let hypesquadBrilliance = ""
        let hypesquadBalance = ""

        if (user.flags.has("PARTNERED_SERVER_OWNER")){
            discordPartnerBadge = "<:PartnerBadge:891724938703155270>"
        }
        if (user.flags.has("HOUSE_BALANCE")){
            hypesquadBalance = "<:HypeSquadBalance:891723099211444234>"
        }
        if (user.flags.has("EARLY_VERIFIED_BOT_DEVELOPER")){
            verifiedBotDeveloperBadge = "<:VerifiedBotDeveloperBadge:891720363321471006>"
        }
        if (user.flags.has("EARLY_SUPPORTER")){
            earlySupporterBadge = "<:EarlySupporterBadge:891720643240939581>"
        }
        if (user.flags.has("HYPESQUAD_EVENTS")){
            hypesquadEventsBadge = "<:HypeSquadEventsBadge:891724366746910760>"
        }
        if (user.flags.has("HOUSE_BRAVERY")){
            hypesquadBravery = "<:HypeSquadBravery:891723098666188821>"
        }
        if (user.flags.has("HOUSE_BRILLIANCE")){
            hypesquadBrilliance = "<:HypeSquadBrilliance:891723098934607943>"
        }

        const allBadges = `${verifiedBotDeveloperBadge} ${earlySupporterBadge} ${hypesquadEventsBadge} ${discordPartnerBadge} ${hypesquadBravery} ${hypesquadBrilliance} ${hypesquadBalance}`

        const embed = new MessageEmbed()
        .setAuthor(user.tag, user.avatarURL())
        .setThumbnail(user.avatarURL())
        .setColor("#00ff94")
        .setDescription(`${user} — ${allBadges}`)
        .addField("Account Created",moment(user.createdAt).format("dddd, MMMM Do YYYY, HH:mm:ss"),true)
        .addField("Joined",moment(member.joinedAt).format("dddd, MMMM Do YYYY, HH:mm:ss"),true)
        .addField("Status",status,true)
        .addField(`Roles [${member.roles.cache.size - 1}]`,roles,true)
        .addField("Avatar",`[Click Here](${user.avatarURL()})`,true)
        .setTimestamp()
        .setFooter(`ID: ${user.id}`)

        message.channel.send({embeds:[embed], components:[button]})
    }
}
