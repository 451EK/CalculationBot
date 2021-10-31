const client = require('../app.js');

client.on('ready', async client =>{
    let allUsers = []

    client.guilds.cache.forEach(guild => {
      guild.members.cache.forEach(member => {
        if(member.user.bot) return
        allUsers.push(member)
      })
    })
    console.log(`Logged in as ${client.user.tag} on ${client.guilds.cache.size} servers!`)
    let statuses = [
        `⚒️ -help`
    ]
    let i = 0;
    setInterval(() => {
        let status = statuses[i];
        if(!status){
            status = statuses[0];
            i = 0;
        }
        client.user.setActivity(status)
        i++;
    }, 15000);
})