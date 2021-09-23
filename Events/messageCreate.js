const client = require('../app.js');
defaultPrefix = "-"

client.on("messageCreate", message => {
    if (!message.guild) return;
    if (!message.content.startsWith(defaultPrefix) || message.author.bot) return;

    const args = message.content.slice(defaultPrefix.length).split(/ +/)
    const command = args.shift().toLowerCase()
    if (command == "ping"){
        client.commands.get("ping").run(client,message)
    }
    else if(command == "info"){
        client.commands.get("info").run(client,message)
    }
    else if(command == "purge"){
        client.commands.get("purge").run(client,message)
    }
    else if(command == "math"){
        client.commands.get("math").run(message,args)
    }
    else if(command == "calculator"){
        client.commands.get("calculator").run(client,message)
    }
    else if(command == "curcodes"){
        client.commands.get("curcodes").run(message)
    }
    else if(command == "sqrt"){
        client.commands.get("sqrt").run(message,args)
    }
    else if(command == "factorial"){
        client.commands.get("factorial").run(message,args)
    }
    else if(command == "length"){
        client.commands.get("length").run(message)
    }
    else if(command == "time"){
        client.commands.get("time").run(message)
    }
    else if(command == "bugreport"){
        client.commands.get("bugreport").run(client,message,args)
    }
    else if(command== "help"){
        client.commands.get("help").run(client,message,args)
    }
    else if(command== "weather"){
        client.commands.get("weather").run(client,message,args)
    }
})
