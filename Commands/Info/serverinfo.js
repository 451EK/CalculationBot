const { MessageEmbed } = require("discord.js")

module.exports = {
    name:"serverinfo",
    usage: "-serverinfo",
    description: "Shows the information about discord server.",
    run: async(client,message) => {
        const guild = message.guild
        const owner = await guild.fetchOwner();
        const ownerMent = "<@" + owner.id + ">" 
        const channels = message.guild.channels.cache;
        const members = message.guild.members.cache;
        const bots = guild.members.cache.filter(member => member.user.bot).size;
        const humans = guild.members.cache.filter(member => !member.user.bot);
        const roles = guild.roles.cache.sort((a, b) => b.position - a.position).map(role => role.toString());

        let vgate = '<:NOTavailable:872500934998126592>' // MEMBER_VERIFICATION_GATE_ENABLED
        let news = '<:NOTavailable:872500934998126592>' // NEWS
        let community = '<:NOTavailable:872500934998126592>' // COMMUNITY
        let anIcon = "<:NOTavailable:872500934998126592>" // ANIMATED_ICON
        let discovery= "<:NOTavailable:872500934998126592>" // DISCOVERABLE
        let welcomeScreen= "<:NOTavailable:872500934998126592>" // WELCOME_SCREEN_ENABLED
        let banner= "<:NOTavailable:872500934998126592>" // BANNER
        let partner="<:NOTavailable:872500934998126592>" // PARTNERED
        let vanityURL= "<:NOTavailable:872500934998126592>" // VANITY_URL
        let verified="<:NOTavailable:872500934998126592>" // VERIFIED
        let PrivThreads="<:NOTavailable:872500934998126592>" // PRIVATE_THREADS

        features = guild.features
        if (features.includes("ANIMATED_ICON") === true){
            anIcon = "<:available:872499547891449876>"
        }
        if (features.includes("COMMUNITY") === true){
            community = "<:available:872499547891449876>"
        }
        if (features.includes("MEMBER_VERIFICATION_GATE_ENABLED") === true){
            vgate = "<:available:872499547891449876>"
        }
        if (features.includes("NEWS") === true){
            news = "<:available:872499547891449876>"
        }
        if (features.includes("DISCOVERABLE") === true){
            discovery = "<:available:872499547891449876>"
        }
        if (features.includes("WELCOME_SCREEN_ENABLED") === true){
            welcomeScreen = "<:available:872499547891449876>"
        }
        if (features.includes("BANNER") === true){
            banner = "<:available:872499547891449876>"
        }
        if (features.includes("PARTNERED") === true){
            partner = "<:available:872499547891449876>"
        }
        if (features.includes("VANITY_URL") === true){
            vanityURL = "<:available:872499547891449876>"
        }
        if (features.includes("VERIFIED") === true){
            verified = "<:available:872499547891449876>"
        }
        if (features.includes("PRIVATE_THREADS") === true){
            PrivThreads = "<:available:872499547891449876>"
        }

        var textChannels = channels.filter(channel => channel.type === 'GUILD_TEXT').size
        var voiceChannels = channels.filter(channel => channel.type === 'GUILD_VOICE').size
        let boostTier = message.guild.premiumTier
        if (boostTier == "NONE"){
            boostTier = "0"
        }

        const onlineMember = humans.filter(member => member.presence?.status === 'online').size
        const dndMember = humans.filter(member => member.presence?.status === 'dnd').size
        const idleMember = humans.filter(member => member.presence?.status === 'idle').size
        const offlineMember = humans.size - (onlineMember + dndMember + idleMember)
        const allOnline = onlineMember + dndMember + idleMember

        const embed = new MessageEmbed()
        .setAuthor(guild.name, guild.iconURL())
        .setThumbnail(guild.iconURL())
        .setColor("#00ff94")
        .setDescription(`**ID:** ${guild.id}\n**Owner:** ${ownerMent}\n**Verification Level:** ${guild.verificationLevel}`)
        .setTimestamp(guild.createdTimestamp)
        .setFooter(`Server Created`)
        .addField("Features", `${discovery} : Discovery\n${news} : News Channel\n${community} : Community\n${welcomeScreen} : Welcome Screen\n${anIcon} : Animated Icon\n${banner} : Banner\n${partner} : Partnered\n${vanityURL} : Vanity URL\n${verified} : Verified\n ${PrivThreads} : Private Threads\n ${vgate} : Verification Gate`,true)
        .addField("Channels", `<:TextChannel:891594350922960927> ${textChannels}\n<:VoiceChannel:891594350902009906> ${voiceChannels}`,true)
        .addField("Boosts", `<:ServerBoostLevel:891600054761168916> ${boostTier} Level \n<:ServerBoost:891599828465885234> ${message.guild.premiumSubscriptionCount} Boosts`)
        .addField("Members", `Total: ${members.size}\nBots: ${bots}\n<:online:891229323766403092> ${allOnline}  <:offline:891229323388940300> ${offlineMember}`)
        .addField(`Roles`, `${roles.length - 1} Roles\nHighest Role: ${guild.roles.highest}`)
        .addField("Emoji Count",`Total Emoji Count: ${guild.emojis.cache.size}\nRegular Emoji Count: ${guild.emojis.cache.filter(emoji => !emoji.animated).size}\nAnimated Emoji Count: ${guild.emojis.cache.filter(emoji => emoji.animated).size}`)
        await message.channel.send({embeds:[embed]})
    }
}