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
            status = "<:Online:901757472958713856> Online"
        }
        if (status === "idle"){
            status = "<:Idle:901757472912601139> Idle"
        }
        if (status === "dnd"){
            status = "<:DoNotDisturb:901757473080348672> Do Not Disturb"
        }
        if (status === "offline"){
            status = "<:Offline:901757472824496169> Offline"
        }

        let verifiedBotDeveloperBadge = ""
        let earlySupporterBadge = ""
        let hypesquadEventsBadge = ""
        let discordPartnerBadge = ""
        let hypesquadBravery = ""
        let hypesquadBrilliance = ""
        let hypesquadBalance = ""

        if (user.flags.has("PARTNERED_SERVER_OWNER")){
            discordPartnerBadge = "<:DiscordPartnerBadge:901757473071972363>"
        }
        if (user.flags.has("HOUSE_BALANCE")){
            hypesquadBalance = "<:HypeSquadBalance:901757473420095529>"
        }
        if (user.flags.has("EARLY_VERIFIED_BOT_DEVELOPER")){
            verifiedBotDeveloperBadge = "<:VerifiedDeveloperBadge:901757472975499314>"
        }
        if (user.flags.has("EARLY_SUPPORTER")){
            earlySupporterBadge = "<:EarlySupporterBadge:901757473424297985>"
        }
        if (user.flags.has("HYPESQUAD_EVENTS")){
            hypesquadEventsBadge = "<:HypeSquadEvents:901757473382350888>"
        }
        if (user.flags.has("HOUSE_BRAVERY")){
            hypesquadBravery = "<:HypeSquadBravery:901757473214582835>"
        }
        if (user.flags.has("HOUSE_BRILLIANCE")){
            hypesquadBrilliance = "<:HypeSquadBrilliance:901757473210372106>"
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
