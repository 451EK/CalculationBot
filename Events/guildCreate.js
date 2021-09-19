const { MessageEmbed, Guild } = require('discord.js');
const client = require('../app.js');

client.on("guildCreate", guild => {
    const me = guild.members.fetch(client.user.id)
    let channel = guild.channels.cache.find(g => g.name === "general") || guild.channels.cache.filter(c => c.permissionsFor(me).has('SEND_MESSAGES') && c.type === 'text').first()
    if (!channel) channel = guild.owner
    embed = new MessageEmbed()
    .setTitle("Thanks For Adding The Calculator")
    .setDescription("\n• The prefix is `-`. ||You will be able to use slash commands soon..||\n• Use `-help` or `-info` commands to learn more!\n• If you need help, you can join the [Support Server](https://discord.gg/tXd9gPtKCj)!")
    .setTimestamp()
    .setFooter("Calculator#0261", client.user.avatarURL())
    .setColor("#00ff94")
    channel.send({embeds:[embed]}).catch((err) => { console.log(err); guild.owner.send({embeds:[embed]}) })
})