const { Discord, MessageActionRow, MessageSelectMenu } = require("discord.js")
const { MessageEmbed } = require("discord.js")

module.exports = {
    name: "help",
    usage: "`-help <command[OPTIONAL]>`",
    description: "Shows the help message.",
    run: async(client,message,args) => {
        if(args[0] == "calculator"){
            let embed = new MessageEmbed()
            .setTitle("Command `calculator`")
            .setDescription(`• **Usage**: ${client.commands.get("calculator").usage}\n• **Description**: ${client.commands.get("calculator").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "factorial"){
            let embed = new MessageEmbed()
            .setTitle("Command `factorial`")
            .setDescription(`• **Usage**: ${client.commands.get("factorial").usage}\n• **Description**: ${client.commands.get("factorial").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "length"){
            let embed = new MessageEmbed()
            .setTitle("Command `length`")
            .setDescription(`• **Usage**: ${client.commands.get("length").usage}\n• **Description**: ${client.commands.get("length").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "math"){
            let embed = new MessageEmbed()
            .setTitle("Command `math`")
            .setDescription(`• **Usage**: ${client.commands.get("math").usage}\n• **Description**: ${client.commands.get("math").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "sqrt"){
            let embed = new MessageEmbed()
            .setTitle("Command `sqrt`")
            .setDescription(`• **Usage**: ${client.commands.get("sqrt").usage}\n• **Description**: ${client.commands.get("sqrt").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "help"){
            let embed = new MessageEmbed()
            .setTitle("Command `help`")
            .setDescription(`• **Usage**: ${client.commands.get("help").usage}\n• **Description**: ${client.commands.get("help").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "info"){
            let embed = new MessageEmbed()
            .setTitle("Command `info`")
            .setDescription(`• **Usage**: ${client.commands.get("info").usage}\n• **Description**: ${client.commands.get("info").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "ping"){
            let embed = new MessageEmbed()
            .setTitle("Command `ping`")
            .setDescription(`• **Usage**: ${client.commands.get("ping").usage}\n• **Description**: ${client.commands.get("ping").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "time"){
            let embed = new MessageEmbed()
            .setTitle("Command `time`")
            .setDescription(`• **Usage**: ${client.commands.get("time").usage}\n• **Description**: ${client.commands.get("time").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "weather"){
            let embed = new MessageEmbed()
            .setTitle("Command `weather`")
            .setDescription(`• **Usage**: ${client.commands.get("weather").usage}\n• **Description**: ${client.commands.get("weather").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "purge"){
            let embed = new MessageEmbed()
            .setTitle("Command `purge`")
            .setDescription(`• **Usage**: ${client.commands.get("purge").usage}\n• **Description**: ${client.commands.get("purge").description}\n• **Note**: ${client.commands.get("purge").note}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "curcodes"){
            let embed = new MessageEmbed()
            .setTitle("Command `curcodes`")
            .setDescription(`• **Usage**: ${client.commands.get("curcodes").usage}\n• **Description**: ${client.commands.get("curcodes").description}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else if(args[0] == "bugreport"){
            let embed = new MessageEmbed()
            .setTitle("Command `bugreport`")
            .setDescription(`• **Usage**: ${client.commands.get("bugreport").usage}\n• **Description**: ${client.commands.get("bugreport").description}\n• **Note**: ${client.commands.get("bugreport").note}`)
            .setColor("#00ff94")
            message.channel.send({embeds:[embed]})
        }
        else{
        const row = new MessageActionRow()
        .addComponents(
            new MessageSelectMenu()
            .setCustomId("help-menu")
            .setPlaceholder("Select a help option")
            .addOptions([
                {
                    label: "General",
                    description:"General Informations",
                    value: "general",
                    emoji: "📋"
                },
                {
                    label:"Moderation",
                    description:"Moderation Menu",
                    value:"moderation",
                    emoji: "⚙️"
                },
                {
                    label:"Utility",
                    description:"Utility Menu",
                    value:"utility",
                    emoji: "⚒️"
                },
                {
                    label:"Info",
                    description:"Info Menu",
                    value:"info",
                    emoji: "ℹ️"
                },
                {
                    label:"Calculation",
                    description:"Calculation Menu",
                    value:"calculation",
                    emoji: "📑"
                },
                {
                    label:"More",
                    description:"More Commands",
                    value:"more",
                    emoji: "🗂️"
                },
                {
                    label:"All",
                    description:"All Commands",
                    value:"all",
                    emoji: "✨"
                }
            ])
        )
        let mainEmbed = new MessageEmbed()
        .setTitle("**Help**")
        .setDescription(`\n\nStill having issues?\nJoin the Support Server by clicking [here](https://discord.gg/tXd9gPtKCj).`)
        .setColor("#00ff94")
        .setFooter(`Requested by ${message.author.tag}`,message.author.avatarURL())

        let msg = await message.channel.send({content:"ㅤ",ephemeral:true,embeds:[mainEmbed],components:[row]})

        let embed1 = new MessageEmbed()
        .setTitle("General Informations")
        .setDescription("All commands must start with a prefix.\nDefault prefix is -.(Not changeable yet.)\n\nTo view commands via category,select a category in the select menu below.\nTo view more information on a certain command,use help <command>.")
        .setColor("#00ff94")
        .setTimestamp()

        let embed2 = new MessageEmbed()
        .setTitle("**➜ Moderation**")
        .setDescription("\n`purge`")
        .setColor("#00ff94")

        let embed3 = new MessageEmbed()
        .setTitle("**➜ Utility**")
        .setDescription("\n`bugreport`")
        .setColor("#00ff94")

        let embed4 = new MessageEmbed()
        .setTitle("**➜ Info**")
        .setDescription("\n`help`, `info`, `ping`, `time`, `weather`")
        .setColor("#00ff94")

        let embed5 = new MessageEmbed()
        .setTitle("**➜ Calculation**")
        .setDescription("\n`calculator`, `math`, `factorial`, `sqrt`, `length`")
        .setColor("#00ff94")

        let embed7 = new MessageEmbed()
        .setTitle("**➜ More**")
        .setDescription("\n`curcodes`")
        .setColor("#00ff94")

        let embed8 = new MessageEmbed()
        .setTitle("**All Commands (13)**")
        .setDescription("\n`bugreport`, `calculator`, `curcodes`, `factorial`, `help`, `info`, `length`, `math`, `ping`, `purge`, `sqrt`, `time`, `weather`")
        .setColor("#00ff94")

        const collector = message.channel.createMessageComponentCollector({
            componentType : "SELECT_MENU"
        })

        collector.on("collect",async (collected) => {
            const value = collected.values[0]
            if ( value === "general"){
                collected.reply({embeds:[embed1], ephemeral: true})
            }
            else if ( value === "moderation"){
                collected.reply({embeds:[embed2], ephemeral: true})
            }
            else if ( value === "utility"){
                collected.reply({embeds:[embed3], ephemeral: true})
            }
            else if ( value === "info"){
                collected.reply({embeds:[embed4], ephemeral: true})
            }
            else if ( value === "calculation"){
                collected.reply({embeds:[embed5], ephemeral: true})
            }
            else if ( value === "more"){
                collected.reply({embeds:[embed7], ephemeral: true})
            }
            else if ( value === "all"){
                collected.reply({embeds:[embed8], ephemeral: true})
            }
        })
    }
}
}