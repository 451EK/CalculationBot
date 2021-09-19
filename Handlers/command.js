const {readdirSync} = require('fs');

module.exports = (client) => {
    readdirSync('./Commands/').forEach(dir => {
        const Commands = readdirSync(`./Commands/${dir}/`).filter(file => file.endsWith('.js'));
        for(let file of Commands){
            let pull = require(`../Commands/${dir}/${file}`);
            if(pull.name){
                client.commands.set(pull.name, pull);
            } else {
                continue;
            }if(pull.aliases && Array.isArray(pull.aliases)) pull.aliases.forEach(alias => client.aliases.set(alias, pull.name))
        }
    });
}