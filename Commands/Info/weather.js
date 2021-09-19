const Discord = require('discord.js');
const weather = require('weather-js');

module.exports = {
    name: "weather",
    usage: "`-weather <location>`",
    description:"Gives the info about weather in given location.",
    run: async(client, message, args) => {
        weather.find({search: args.join(" "), degreeType: 'C'}, function(err, result) {
            if (result === undefined || result.length === 0) return;
            if (err) console.log(err);
            var current = result[0].current;
            var location = result[0].location;
            const embed = new Discord.MessageEmbed()
            .setDescription(`__${current.skytext}__`)
            .setAuthor(`Weather in ${current.observationpoint}`)
            .setThumbnail(current.imageUrl)
            .setColor("#00ff94")
            .addField('Timezone', `UTC${location.timezone}`, true)
            .addField('Temperature', `${current.temperature} Degrees`, true)
            .addField('Feels Like', `${current.feelslike} Degrees`, true)
            .addField('Winds', current.winddisplay, true)
            .addField('Humidity', `${current.humidity}%`, true)
            message.channel.send({embeds:[embed]});
          })
    }
}
