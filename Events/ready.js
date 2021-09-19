const client = require('../app.js');

client.on('ready', async client =>{
    let allUsers = [];
    client.guilds.cache.forEach(guilds => allUsers.push(guilds.memberCount))
    let users = allUsers.reduce((a, b) => a + b)
    console.log(`Logged in as ${client.user.tag} on ${client.guilds.cache.size} servers!`)

    client.user.setPresence({status: "online", activities:[{name: `-help | ${users} Users`, type:"WATCHING"}]}) 
})